import netaddr
import re

from ipcalcng.core import log
from ipcalcng.exceptions import AddressFormatException


def parse_prefix(prefixes):
    parsed_prefixes = []
    prefix_index = 0
    while prefix_index < len(prefixes):
        supplement = None
        prefix = prefixes[prefix_index]
        log.debug("inspect %s" % prefix)
        if prefix_index < len(prefixes) - 1 and prefix.find("/") == -1:
            possible_supplement = prefixes[prefix_index+1]
            if re.match("\d+$", possible_supplement) and int(possible_supplement) in range(1, 129):
                log.debug("supplement %s is a CIDR prefix" % possible_supplement)
                supplement = "/%s" % (prefixes.pop(prefix_index + 1))
            elif re.match("[\da-fA-F:.]+", possible_supplement):
                log.debug("supplement %s is a netmask" % possible_supplement)
                supplement = "/%s" % (prefixes.pop(prefix_index + 1))
        try:
            network = netaddr.IPNetwork(prefix)
            if supplement:
                network = netaddr.IPNetwork("%s%s" % (prefix, supplement))
        except netaddr.core.AddrFormatError as e:
            raise AddressFormatException(e)
        prefix_index += 1
        log.info("got %s" % network)
        parsed_prefixes.append(network)
    return parsed_prefixes


def none():
    pass