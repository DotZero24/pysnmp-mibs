#
# PySNMP MIB module CISCO-L2-DEV-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-L2-DEV-MONITORING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
ciscoL2DevMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 271))
ciscoL2DevMonMIB.setRevisions(('2003-07-22 00:00', '2001-09-27 00:00',))
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setLastUpdated('200307220000Z')
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setOrganization('Cisco System Inc.')
ciscoL2DevMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 1))
cl2DevMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1))
cl2DevMonInStandbyMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cl2DevMonInStandbyMode.setStatus('current')
cl2DevMonNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cl2DevMonNotifEnabled.setStatus('current')
cl2DevMonActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3), )
if mibBuilder.loadTexts: cl2DevMonActiveTable.setStatus('current')
cl2DevMonActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveMacAddress"))
if mibBuilder.loadTexts: cl2DevMonActiveEntry.setStatus('current')
cl2DevMonActiveMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: cl2DevMonActiveMacAddress.setStatus('current')
cl2DevMonActivePollingFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActivePollingFrequency.setStatus('current')
cl2DevMonActivePollingTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActivePollingTimeOut.setStatus('current')
cl2DevMonActiveRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveRowStatus.setStatus('current')
cl2DevMonActiveRadioMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveRadioMacType.setStatus('current')
cl2DevMonActiveLocalRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveLocalRadioIndex.setStatus('current')
ciscoL2DevMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 0))
cl2DevMonSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 271, 0, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"))
if mibBuilder.loadTexts: cl2DevMonSwitchover.setStatus('current')
ciscoL2DevMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2))
ciscoL2DevMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1))
ciscoL2DevMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2))
ciscoL2DevMonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonConfigGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonCompliance = ciscoL2DevMonCompliance.setStatus('deprecated')
ciscoL2DevMonComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 2)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonConfigGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonNotificationGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonRadioConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonComplianceRev1 = ciscoL2DevMonComplianceRev1.setStatus('current')
ciscoL2DevMonConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonInStandbyMode"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonNotifEnabled"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonConfigGroup = ciscoL2DevMonConfigGroup.setStatus('current')
ciscoL2DevMonNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 2)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonNotificationGroup = ciscoL2DevMonNotificationGroup.setStatus('current')
ciscoL2DevMonRadioConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 3)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRadioMacType"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveLocalRadioIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonRadioConfigGroup = ciscoL2DevMonRadioConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2-DEV-MONITORING-MIB", ciscoL2DevMonMIBCompliances=ciscoL2DevMonMIBCompliances, cl2DevMonSwitchover=cl2DevMonSwitchover, cl2DevMonActiveMacAddress=cl2DevMonActiveMacAddress, cl2DevMonConfig=cl2DevMonConfig, cl2DevMonInStandbyMode=cl2DevMonInStandbyMode, cl2DevMonActiveRadioMacType=cl2DevMonActiveRadioMacType, ciscoL2DevMonMIBObjects=ciscoL2DevMonMIBObjects, cl2DevMonActivePollingFrequency=cl2DevMonActivePollingFrequency, PYSNMP_MODULE_ID=ciscoL2DevMonMIB, cl2DevMonActivePollingTimeOut=cl2DevMonActivePollingTimeOut, ciscoL2DevMonMIBConformance=ciscoL2DevMonMIBConformance, ciscoL2DevMonCompliance=ciscoL2DevMonCompliance, ciscoL2DevMonMIBNotifications=ciscoL2DevMonMIBNotifications, cl2DevMonActiveTable=cl2DevMonActiveTable, ciscoL2DevMonConfigGroup=ciscoL2DevMonConfigGroup, ciscoL2DevMonComplianceRev1=ciscoL2DevMonComplianceRev1, cl2DevMonActiveLocalRadioIndex=cl2DevMonActiveLocalRadioIndex, ciscoL2DevMonNotificationGroup=ciscoL2DevMonNotificationGroup, cl2DevMonNotifEnabled=cl2DevMonNotifEnabled, cl2DevMonActiveEntry=cl2DevMonActiveEntry, ciscoL2DevMonMIBGroups=ciscoL2DevMonMIBGroups, ciscoL2DevMonRadioConfigGroup=ciscoL2DevMonRadioConfigGroup, cl2DevMonActiveRowStatus=cl2DevMonActiveRowStatus, ciscoL2DevMonMIB=ciscoL2DevMonMIB)
