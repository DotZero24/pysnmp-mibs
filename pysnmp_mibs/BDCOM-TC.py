#
# PySNMP MIB module BDCOM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bdcom/BDCOM-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bdcomModules, = mibBuilder.importSymbols("BDCOM-SMI", "bdcomModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bdcomTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 12, 1))
bdcomTextualConventions.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: bdcomTextualConventions.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: bdcomTextualConventions.setOrganization('BDCOM, Inc.')
class BDCOMNetworkProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("ipv6", 20), ("cdm", 21), ("nbf", 22), ("bpxIgx", 23), ("clnsPfx", 24), ("http", 25), ("unknown", 65535))

class BDCOMNetworkAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'

class Unsigned64(TextualConvention, Counter64):
    status = 'current'

class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class SAPType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CountryCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class CountryCodeITU(TextualConvention, Unsigned32):
    reference = 'ITU-T T.35 - Section 3.1 Country Code'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BDCOMRowOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class BDCOMPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class BDCOMIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class BDCOMLocationClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8))

class BDCOMLocationSpecifier(TextualConvention, OctetString):
    reference = 'RFC2234, Augmented BNF for syntax specifications: ABNF'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class BDCOMInetAddressMask(TextualConvention, Unsigned32):
    reference = 'RFC2851, Textual Conventions for Internet Network Addresses.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 128)

class BDCOMAbsZeroBasedCounter32(TextualConvention, Gauge32):
    status = 'current'

class BDCOMSnapShotAbsCounter32(TextualConvention, Unsigned32):
    status = 'current'

class BDCOMAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7))

class PerfHighIntervalCount(TextualConvention, Counter64):
    reference = 'RFC 2856(HCNUM-TC MIB). RFC 2493(PerfHist-TC-MIB).'
    status = 'current'

class ConfigIterator(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BulkConfigResult(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ListIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class TimeIntervalSec(TextualConvention, Unsigned32):
    status = 'current'

class TimeIntervalMin(TextualConvention, Unsigned32):
    status = 'current'

class BDCOMMilliSeconds(TextualConvention, Unsigned32):
    status = 'current'

class MicroSeconds(TextualConvention, Unsigned32):
    status = 'current'

mibBuilder.exportSymbols("BDCOM-TC", BDCOMAlarmSeverity=BDCOMAlarmSeverity, BDCOMSnapShotAbsCounter32=BDCOMSnapShotAbsCounter32, ListIndexOrZero=ListIndexOrZero, BDCOMAbsZeroBasedCounter32=BDCOMAbsZeroBasedCounter32, BDCOMIpProtocol=BDCOMIpProtocol, bdcomTextualConventions=bdcomTextualConventions, PerfHighIntervalCount=PerfHighIntervalCount, ListIndex=ListIndex, BDCOMMilliSeconds=BDCOMMilliSeconds, TimeIntervalMin=TimeIntervalMin, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, BDCOMLocationSpecifier=BDCOMLocationSpecifier, BDCOMInetAddressMask=BDCOMInetAddressMask, BDCOMLocationClass=BDCOMLocationClass, SAPType=SAPType, ConfigIterator=ConfigIterator, BDCOMNetworkAddress=BDCOMNetworkAddress, BulkConfigResult=BulkConfigResult, BDCOMPort=BDCOMPort, BDCOMRowOperStatus=BDCOMRowOperStatus, Unsigned64=Unsigned64, TimeIntervalSec=TimeIntervalSec, MicroSeconds=MicroSeconds, PYSNMP_MODULE_ID=bdcomTextualConventions, InterfaceIndexOrZero=InterfaceIndexOrZero, BDCOMNetworkProtocol=BDCOMNetworkProtocol, CountryCode=CountryCode, CountryCodeITU=CountryCodeITU)
