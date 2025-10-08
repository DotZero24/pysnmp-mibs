#
# PySNMP MIB module NMS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bdcom/NMS-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nmsModules, = mibBuilder.importSymbols("NMS-SMI", "nmsModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmsTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 12, 1))
nmsTextualConventions.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: nmsTextualConventions.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: nmsTextualConventions.setOrganization('')
class NMSNetworkProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("ipv6", 20), ("cdm", 21), ("nbf", 22), ("bpxIgx", 23), ("clnsPfx", 24), ("http", 25), ("unknown", 65535))

class NMSNetworkAddress(TextualConvention, OctetString):
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

class NMSRowOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class NMSPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class NMSIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NMSLocationClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8))

class NMSLocationSpecifier(TextualConvention, OctetString):
    reference = 'RFC2234, Augmented BNF for syntax specifications: ABNF'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NMSInetAddressMask(TextualConvention, Unsigned32):
    reference = 'RFC2851, Textual Conventions for Internet Network Addresses.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 128)

class NMSAbsZeroBasedCounter32(TextualConvention, Gauge32):
    status = 'current'

class NMSSnapShotAbsCounter32(TextualConvention, Unsigned32):
    status = 'current'

class NMSAlarmSeverity(TextualConvention, Integer32):
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

class NMSMilliSeconds(TextualConvention, Unsigned32):
    status = 'current'

class MicroSeconds(TextualConvention, Unsigned32):
    status = 'current'

mibBuilder.exportSymbols("NMS-TC", NMSPort=NMSPort, MicroSeconds=MicroSeconds, NMSAlarmSeverity=NMSAlarmSeverity, CountryCode=CountryCode, SAPType=SAPType, NMSAbsZeroBasedCounter32=NMSAbsZeroBasedCounter32, NMSNetworkProtocol=NMSNetworkProtocol, NMSLocationClass=NMSLocationClass, TimeIntervalMin=TimeIntervalMin, NMSIpProtocol=NMSIpProtocol, InterfaceIndexOrZero=InterfaceIndexOrZero, NMSRowOperStatus=NMSRowOperStatus, ListIndex=ListIndex, CountryCodeITU=CountryCodeITU, NMSMilliSeconds=NMSMilliSeconds, ConfigIterator=ConfigIterator, nmsTextualConventions=nmsTextualConventions, Unsigned64=Unsigned64, BulkConfigResult=BulkConfigResult, ListIndexOrZero=ListIndexOrZero, PYSNMP_MODULE_ID=nmsTextualConventions, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, NMSNetworkAddress=NMSNetworkAddress, NMSSnapShotAbsCounter32=NMSSnapShotAbsCounter32, NMSLocationSpecifier=NMSLocationSpecifier, TimeIntervalSec=TimeIntervalSec, PerfHighIntervalCount=PerfHighIntervalCount, NMSInetAddressMask=NMSInetAddressMask)
