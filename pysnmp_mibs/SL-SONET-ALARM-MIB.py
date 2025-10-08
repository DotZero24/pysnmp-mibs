#
# PySNMP MIB module SL-SONET-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/smartoptics/SL-SONET-ALARM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfTotalCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfTotalCount", "PerfIntervalCount")
slSonetMib, = mibBuilder.importSymbols("SL-SONET-MIB", "slSonetMib")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
slSonetAlarmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4))
if mibBuilder.loadTexts: slSonetAlarmMib.setLastUpdated('0008280000Z')
if mibBuilder.loadTexts: slSonetAlarmMib.setOrganization('Smartoptics AS')
class SonetAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("losSonetAlarm", 1), ("lofSonetAlarm", 2), ("lopSonetAlarm", 3), ("aisSonetAlarm", 4), ("rfiSonetAlarm", 5), ("uneqSonetAlarm", 6), ("tim", 7), ("slm", 8), ("sd", 9), ("sf", 10), ("hwfail", 11))

slSonetAlarmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1))
slSonetAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2))
slSonetAlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1), )
if mibBuilder.loadTexts: slSonetAlarmConfigTable.setStatus('current')
slSonetAlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1), ).setIndexNames((0, "SL-SONET-ALARM-MIB", "slSonetAlarmIfIndex"), (0, "SL-SONET-ALARM-MIB", "slSonetAlarmType"))
if mibBuilder.loadTexts: slSonetAlarmConfigEntry.setStatus('current')
slSonetAlarmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetAlarmIfIndex.setStatus('current')
slSonetAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 2), SonetAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetAlarmType.setStatus('current')
slSonetAlarmMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSonetAlarmMask.setStatus('current')
slSonetAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetAlarmStatus.setStatus('current')
slSonetAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noAlarm", 0), ("critical", 1), ("major", 2), ("minor", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetAlarmSeverity.setStatus('current')
slSonetAlarmServiceAffect = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSonetAlarmServiceAffect.setStatus('current')
slSonetAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2, 3)).setObjects(("SL-SONET-ALARM-MIB", "slSonetAlarmIfIndex"), ("SL-SONET-ALARM-MIB", "slSonetAlarmType"), ("SL-SONET-ALARM-MIB", "slSonetAlarmStatus"), ("SL-SONET-ALARM-MIB", "slSonetAlarmSeverity"), ("SL-SONET-ALARM-MIB", "slSonetAlarmServiceAffect"))
if mibBuilder.loadTexts: slSonetAlarmTrap.setStatus('current')
mibBuilder.exportSymbols("SL-SONET-ALARM-MIB", slSonetAlarmConfig=slSonetAlarmConfig, slSonetAlarmTraps=slSonetAlarmTraps, slSonetAlarmMask=slSonetAlarmMask, slSonetAlarmConfigTable=slSonetAlarmConfigTable, slSonetAlarmConfigEntry=slSonetAlarmConfigEntry, slSonetAlarmServiceAffect=slSonetAlarmServiceAffect, SonetAlarmType=SonetAlarmType, slSonetAlarmTrap=slSonetAlarmTrap, slSonetAlarmSeverity=slSonetAlarmSeverity, slSonetAlarmStatus=slSonetAlarmStatus, PYSNMP_MODULE_ID=slSonetAlarmMib, slSonetAlarmIfIndex=slSonetAlarmIfIndex, slSonetAlarmMib=slSonetAlarmMib, slSonetAlarmType=slSonetAlarmType)
