#
# PySNMP MIB module SL-ALS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/smartoptics/SL-ALS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfCurrentCount, PerfTotalCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfTotalCount", "PerfIntervalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
slAlsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 12))
if mibBuilder.loadTexts: slAlsMib.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slAlsMib.setOrganization('Smartoptics')
slAlsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1))
slAlsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 12, 2))
class AlsManualPulseTimeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3))

class AlsAutomaticPulseTimeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3))

slAlsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1), )
if mibBuilder.loadTexts: slAlsConfigTable.setStatus('current')
slAlsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slAlsConfigEntry.setStatus('current')
slAlsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsMode.setStatus('current')
slAlsLosDeclareTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms500", 1), ("ms550", 2), ("ms600", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLosDeclareTime.setStatus('current')
slAlsTestPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("s80", 1), ("s90", 2), ("s100", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsTestPulseTime.setStatus('current')
slAlsManualPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsManualPulseTime.setStatus('current')
slAlsAutomaticPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsAutomaticPulseTime.setStatus('current')
slAlsAutomaticDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsAutomaticDelayTime.setStatus('current')
slAlsLaserTestActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLaserTestActivate.setStatus('current')
slAlsLaserManualActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLaserManualActivate.setStatus('current')
slAlsOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlsOperStatus.setStatus('current')
slAlsResetParams = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsResetParams.setStatus('current')
slAlsStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 12, 2, 1)).setObjects(("IF-MIB", "ifIndex"), ("SL-ALS-MIB", "slAlsOperStatus"))
if mibBuilder.loadTexts: slAlsStatusChangeTrap.setStatus('current')
mibBuilder.exportSymbols("SL-ALS-MIB", slAlsConfigEntry=slAlsConfigEntry, slAlsManualPulseTime=slAlsManualPulseTime, slAlsStatusChangeTrap=slAlsStatusChangeTrap, slAlsLosDeclareTime=slAlsLosDeclareTime, slAlsAutomaticDelayTime=slAlsAutomaticDelayTime, slAlsOperStatus=slAlsOperStatus, slAlsTestPulseTime=slAlsTestPulseTime, slAlsMode=slAlsMode, slAlsAutomaticPulseTime=slAlsAutomaticPulseTime, slAlsResetParams=slAlsResetParams, PYSNMP_MODULE_ID=slAlsMib, slAlsConfig=slAlsConfig, slAlsMib=slAlsMib, slAlsConfigTable=slAlsConfigTable, AlsAutomaticPulseTimeType=AlsAutomaticPulseTimeType, slAlsLaserTestActivate=slAlsLaserTestActivate, slAlsTraps=slAlsTraps, slAlsLaserManualActivate=slAlsLaserManualActivate, AlsManualPulseTimeType=AlsManualPulseTimeType)
