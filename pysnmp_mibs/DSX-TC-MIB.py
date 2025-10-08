#
# PySNMP MIB module DSX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/DSX-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntEnterpriseDataTasmanInterfaces, ntEnterpriseDataTasmanModules, ntEnterpriseDataTasmanMgmt = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanInterfaces", "ntEnterpriseDataTasmanModules", "ntEnterpriseDataTasmanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nndsxTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 3, 2))
nndsxTC.setRevisions(('1999-04-23 00:00',))
if mibBuilder.loadTexts: nndsxTC.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: nndsxTC.setOrganization('Nortel Networks')
class AlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class LEDState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("led-off", 1), ("led-green", 2), ("led-red", 3), ("led-yellow", 4), ("led-blinking-green", 5), ("led-blinking-red", 6), ("led-blinking-yellow", 7))

nndsxMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1))
nndsxT1E1IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2))
nndsxT3E3IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 3))
mibBuilder.exportSymbols("DSX-TC-MIB", LEDState=LEDState, AlarmStatus=AlarmStatus, nndsxMIB=nndsxMIB, nndsxTC=nndsxTC, nndsxT3E3IfGroup=nndsxT3E3IfGroup, PYSNMP_MODULE_ID=nndsxTC, nndsxT1E1IfGroup=nndsxT1E1IfGroup)
