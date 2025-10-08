#
# PySNMP MIB module FIBROLAN-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fibrolan/FIBROLAN-COMMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fibrolanCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 4467, 1000, 1))
fibrolanCommon.setRevisions(('2015-08-10 00:00', '2009-01-26 00:00',))
if mibBuilder.loadTexts: fibrolanCommon.setLastUpdated('201508100000Z')
if mibBuilder.loadTexts: fibrolanCommon.setOrganization('Fibrolan Ltd.')
fibrolan = MibIdentifier((1, 3, 6, 1, 4, 1, 4467))
fibrolanGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 4467, 1000))
class FlUtilization(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class FlTemperature(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class FlFileServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ftp", 2), ("tftp", 3))

class FlFileXferDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("getFromServer", 1), ("putOnServer", 2))

class FlClockSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 99))
    namedValues = NamedValues(("gps", 1), ("bits", 2), ("syncE", 3), ("ptp", 4), ("external", 5), ("oscillator", 6), ("other", 99))

class FlClockQuality(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 7, 8, 10, 11, 12, 13, 15, 99))
    namedValues = NamedValues(("stu", 0), ("prs", 1), ("prc", 2), ("tnc", 4), ("st2", 7), ("ssu-b", 8), ("st3", 10), ("sec", 11), ("smc", 12), ("st3e", 13), ("dus", 15), ("other", 99))

class FlGeoCoordinateAxis(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

mibBuilder.exportSymbols("FIBROLAN-COMMON-MIB", fibrolanCommon=fibrolanCommon, FlClockSourceType=FlClockSourceType, PYSNMP_MODULE_ID=fibrolanCommon, FlGeoCoordinateAxis=FlGeoCoordinateAxis, FlClockQuality=FlClockQuality, FlFileXferDirection=FlFileXferDirection, FlUtilization=FlUtilization, FlTemperature=FlTemperature, fibrolanGeneric=fibrolanGeneric, FlFileServerType=FlFileServerType, fibrolan=fibrolan)
