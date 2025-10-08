#
# PySNMP MIB module DASAN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dasan/DASAN-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dasanModules, = mibBuilder.importSymbols("DASAN-SMI", "dasanModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dasanTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 6296, 12, 1))
dasanTextualConventions.setRevisions(('2001-04-19 00:00', '2000-11-21 00:00', '1998-10-28 00:00', '1997-03-13 00:00', '1997-03-13 00:00', '1996-08-14 00:00', '1996-07-08 00:00', '1996-02-22 00:00', '1995-06-07 00:00',))
if mibBuilder.loadTexts: dasanTextualConventions.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: dasanTextualConventions.setOrganization('Dasan Co., Ltd.')
class DasanNetworkProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("unknown", 65535))

class DasanNetworkAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'

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
class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DasanRowOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class DasanPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DasanIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class DasanLocationClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8))

class DasanLocationSpecifier(TextualConvention, OctetString):
    reference = 'RFC2234, Augmented BNF for syntax specifications: ABNF'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class DasanInetAddressMask(TextualConvention, Unsigned32):
    reference = 'RFC2851, Textual Conventions for Internet Network Addresses.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 128)

class DasanAbsZeroBasedCounter32(TextualConvention, Gauge32):
    status = 'current'

class DasanSnapShotAbsCounter32(TextualConvention, Unsigned32):
    status = 'current'

class DasanAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7))

class ModuleIndex(TextualConvention, Integer32):
    status = 'current'

class PortIndex(TextualConvention, Integer32):
    status = 'current'

mibBuilder.exportSymbols("DASAN-TC", DasanPort=DasanPort, CountryCode=CountryCode, SAPType=SAPType, PYSNMP_MODULE_ID=dasanTextualConventions, DasanRowOperStatus=DasanRowOperStatus, dasanTextualConventions=dasanTextualConventions, InterfaceIndexOrZero=InterfaceIndexOrZero, PortIndex=PortIndex, DasanInetAddressMask=DasanInetAddressMask, ModuleIndex=ModuleIndex, DasanIpProtocol=DasanIpProtocol, DasanSnapShotAbsCounter32=DasanSnapShotAbsCounter32, DasanAbsZeroBasedCounter32=DasanAbsZeroBasedCounter32, DasanNetworkAddress=DasanNetworkAddress, DasanAlarmSeverity=DasanAlarmSeverity, DasanLocationClass=DasanLocationClass, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, DasanNetworkProtocol=DasanNetworkProtocol, DasanLocationSpecifier=DasanLocationSpecifier)
