#
# PySNMP MIB module CISCO-DOT11-RADIO-DIAGNOSTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DOT11-RADIO-DIAGNOSTIC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDot11RadioDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 105))
ciscoDot11RadioDiagMIB.setRevisions(('2003-12-23 00:00', '2003-05-08 00:00',))
if mibBuilder.loadTexts: ciscoDot11RadioDiagMIB.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoDot11RadioDiagMIB.setOrganization('Cisco System Inc.')
cDot11RadioDiagMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 0))
cDot11RadioDiagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 1))
cDot11RadioDiagConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1))
cDot11RadioDiagTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11RadioDiagTable.setStatus('current')
cDot11RadioDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11RadioDiagEntry.setStatus('current')
cDot11RadioDiagTempChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(100, 100), ValueRangeConstraint(104, 104), ValueRangeConstraint(108, 108), ValueRangeConstraint(112, 112), ValueRangeConstraint(116, 116), ValueRangeConstraint(120, 120), ValueRangeConstraint(124, 124), ValueRangeConstraint(128, 128), ValueRangeConstraint(132, 132), ValueRangeConstraint(136, 136), ValueRangeConstraint(140, 140), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempChannel.setStatus('current')
cDot11RadioDiagTempTxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempTxPowerLevel.setStatus('current')
cDot11RadioDiagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("apRadioDiscovery", 2), ("siteSurveyTempSettings", 3), ("siteSurveyNonTempSettings", 4))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagMode.setStatus('current')
cDot11RadioDiagSettingsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagSettingsEnabled.setStatus('current')
cDot11RadioDiagTempClientTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempClientTxPower.setStatus('current')
cDot11RadioDiagTempDataRateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 126))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempDataRateSet.setStatus('current')
cDot11RadioDiagMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 2))
cDot11RadioDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1))
cDot11RadioDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2))
cDot11RadioDiagMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1, 1)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagConfigGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagMIBCompliance = cDot11RadioDiagMIBCompliance.setStatus('deprecated')
cDot11RadioDiagMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1, 2)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagConfigGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagMIBComplianceRev1 = cDot11RadioDiagMIBComplianceRev1.setStatus('current')
cDot11RadioDiagConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2, 1)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempChannel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempTxPowerLevel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagMode"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagSettingsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagConfigGlobalGroup = cDot11RadioDiagConfigGlobalGroup.setStatus('deprecated')
cDot11RadioDiagConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2, 2)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempChannel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempTxPowerLevel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagMode"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagSettingsEnabled"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempClientTxPower"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempDataRateSet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagConfigGroupRev1 = cDot11RadioDiagConfigGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", cDot11RadioDiagConfigGroupRev1=cDot11RadioDiagConfigGroupRev1, cDot11RadioDiagTempChannel=cDot11RadioDiagTempChannel, cDot11RadioDiagSettingsEnabled=cDot11RadioDiagSettingsEnabled, cDot11RadioDiagTempTxPowerLevel=cDot11RadioDiagTempTxPowerLevel, PYSNMP_MODULE_ID=ciscoDot11RadioDiagMIB, cDot11RadioDiagTempDataRateSet=cDot11RadioDiagTempDataRateSet, cDot11RadioDiagMIBGroups=cDot11RadioDiagMIBGroups, cDot11RadioDiagTable=cDot11RadioDiagTable, cDot11RadioDiagMode=cDot11RadioDiagMode, cDot11RadioDiagMIBCompliances=cDot11RadioDiagMIBCompliances, cDot11RadioDiagMIBObjects=cDot11RadioDiagMIBObjects, cDot11RadioDiagConfigGlobalGroup=cDot11RadioDiagConfigGlobalGroup, cDot11RadioDiagMIBCompliance=cDot11RadioDiagMIBCompliance, cDot11RadioDiagConfigGlobal=cDot11RadioDiagConfigGlobal, ciscoDot11RadioDiagMIB=ciscoDot11RadioDiagMIB, cDot11RadioDiagEntry=cDot11RadioDiagEntry, cDot11RadioDiagMIBConform=cDot11RadioDiagMIBConform, cDot11RadioDiagMIBComplianceRev1=cDot11RadioDiagMIBComplianceRev1, cDot11RadioDiagMIBNotifs=cDot11RadioDiagMIBNotifs, cDot11RadioDiagTempClientTxPower=cDot11RadioDiagTempClientTxPower)
