#
# PySNMP MIB module DSX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/DSX-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntEnterpriseDataTasmanMgmt, ntEnterpriseDataTasmanInterfaces, ntEnterpriseDataTasmanModules = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt", "ntEnterpriseDataTasmanInterfaces", "ntEnterpriseDataTasmanModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("DSX-TC-MIB", nndsxT1E1IfGroup=nndsxT1E1IfGroup, LEDState=LEDState, nndsxMIB=nndsxMIB, nndsxTC=nndsxTC, AlarmStatus=AlarmStatus, nndsxT3E3IfGroup=nndsxT3E3IfGroup, PYSNMP_MODULE_ID=nndsxTC)
