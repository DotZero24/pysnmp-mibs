#
# PySNMP MIB module CISCO-UDLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-UDLDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoUdldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 118))
ciscoUdldpMIB.setRevisions(('2009-11-09 09:00', '2007-11-27 00:00', '2003-02-21 00:00', '2002-10-10 00:00', '2000-04-10 00:00', '1998-11-10 00:00',))
if mibBuilder.loadTexts: ciscoUdldpMIB.setLastUpdated('200911090900Z')
if mibBuilder.loadTexts: ciscoUdldpMIB.setOrganization('Cisco Systems, Inc.')
ciscoUdldpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 0))
ciscoUdldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1))
cudldpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1))
cudldpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2))
cudldpFastHello = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3))
cudldpGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpGlobalEnable.setStatus('deprecated')
cudldpHelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 90))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpHelloInterval.setStatus('current')
cudldpGlobalMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("aggressive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpGlobalMode.setStatus('current')
cudldpHelloIntervalExt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 90))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpHelloIntervalExt.setStatus('current')
cudldpFastHelloLinkFailRptNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpFastHelloLinkFailRptNotifEnable.setStatus('current')
cudldpFastHelloStatusChangeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpFastHelloStatusChangeNotifEnable.setStatus('current')
cudldpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1), )
if mibBuilder.loadTexts: cudldpInterfaceTable.setStatus('current')
cudldpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cudldpInterfaceEntry.setStatus('current')
cudldpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpInterfaceEnable.setStatus('deprecated')
cudldpInterfaceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("shutdown", 1), ("indeterminant", 2), ("biDirectional", 3), ("notApplicable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpInterfaceOperStatus.setStatus('current')
cudldpInterfaceAggressiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpInterfaceAggressiveMode.setStatus('deprecated')
cudldpInterfaceAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("aggressive", 3), ("default", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpInterfaceAdminMode.setStatus('current')
cudldpInterfaceOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("aggressive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpInterfaceOperMode.setStatus('current')
cudldpIfFastHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpIfFastHelloInterval.setStatus('current')
cudldpIfOperHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 7), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpIfOperHelloInterval.setStatus('current')
cudldpIfFastHelloOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operational", 1), ("notOperational", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpIfFastHelloOperStatus.setStatus('current')
cudldpFastHelloErrorReportEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpFastHelloErrorReportEnable.setStatus('current')
cudldpFastHelloMaxPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpFastHelloMaxPorts.setStatus('current')
cudldpFastHelloConfigPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpFastHelloConfigPorts.setStatus('current')
cudldpFastHelloOperationalPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpFastHelloOperationalPorts.setStatus('current')
cudldpFastHelloLinkFailRptNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 118, 0, 1)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: cudldpFastHelloLinkFailRptNotification.setStatus('current')
cudldpFastHelloStatusChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 118, 0, 2)).setObjects(("CISCO-UDLDP-MIB", "cudldpHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfFastHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfOperHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfFastHelloOperStatus"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: cudldpFastHelloStatusChangeNotification.setStatus('current')
ciscoUdldpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 3))
ciscoUdldpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1))
ciscoUdldpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2))
ciscoUdldpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 1)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBCompliance = ciscoUdldpMIBCompliance.setStatus('deprecated')
ciscoUdldpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 2)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup"), ("CISCO-UDLDP-MIB", "ciscoUdldpAggreModeOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev1 = ciscoUdldpMIBComplianceRev1.setStatus('deprecated')
ciscoUdldpMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 3)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev2 = ciscoUdldpMIBComplianceRev2.setStatus('deprecated')
ciscoUdldpMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 4)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup2"), ("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev3 = ciscoUdldpMIBComplianceRev3.setStatus('deprecated')
ciscoUdldpMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 5)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup2"), ("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup3"), ("CISCO-UDLDP-MIB", "ciscoUdldpFastHelloGroup"), ("CISCO-UDLDP-MIB", "ciscoUdldpFastHelloNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev4 = ciscoUdldpMIBComplianceRev4.setStatus('current')
ciscoUdldpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 1)).setObjects(("CISCO-UDLDP-MIB", "cudldpGlobalEnable"), ("CISCO-UDLDP-MIB", "cudldpInterfaceEnable"), ("CISCO-UDLDP-MIB", "cudldpInterfaceOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBGroup = ciscoUdldpMIBGroup.setStatus('deprecated')
ciscoUdldpAggreModeOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 2)).setObjects(("CISCO-UDLDP-MIB", "cudldpInterfaceAggressiveMode"), ("CISCO-UDLDP-MIB", "cudldpHelloInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpAggreModeOptionalGroup = ciscoUdldpAggreModeOptionalGroup.setStatus('deprecated')
ciscoUdldpMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 3)).setObjects(("CISCO-UDLDP-MIB", "cudldpGlobalMode"), ("CISCO-UDLDP-MIB", "cudldpInterfaceAdminMode"), ("CISCO-UDLDP-MIB", "cudldpInterfaceOperMode"), ("CISCO-UDLDP-MIB", "cudldpHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpInterfaceOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBGroup2 = ciscoUdldpMIBGroup2.setStatus('current')
ciscoUdldpMIBGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 4)).setObjects(("CISCO-UDLDP-MIB", "cudldpHelloIntervalExt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBGroup3 = ciscoUdldpMIBGroup3.setStatus('current')
ciscoUdldpFastHelloGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 5)).setObjects(("CISCO-UDLDP-MIB", "cudldpIfFastHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfOperHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfFastHelloOperStatus"), ("CISCO-UDLDP-MIB", "cudldpFastHelloErrorReportEnable"), ("CISCO-UDLDP-MIB", "cudldpFastHelloLinkFailRptNotifEnable"), ("CISCO-UDLDP-MIB", "cudldpFastHelloStatusChangeNotifEnable"), ("CISCO-UDLDP-MIB", "cudldpFastHelloMaxPorts"), ("CISCO-UDLDP-MIB", "cudldpFastHelloConfigPorts"), ("CISCO-UDLDP-MIB", "cudldpFastHelloOperationalPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpFastHelloGroup = ciscoUdldpFastHelloGroup.setStatus('current')
ciscoUdldpFastHelloNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 6)).setObjects(("CISCO-UDLDP-MIB", "cudldpFastHelloLinkFailRptNotification"), ("CISCO-UDLDP-MIB", "cudldpFastHelloStatusChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpFastHelloNotificationGroup = ciscoUdldpFastHelloNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-UDLDP-MIB", ciscoUdldpMIBConformance=ciscoUdldpMIBConformance, cudldpFastHello=cudldpFastHello, ciscoUdldpMIB=ciscoUdldpMIB, ciscoUdldpMIBGroup=ciscoUdldpMIBGroup, cudldpInterface=cudldpInterface, ciscoUdldpMIBObjects=ciscoUdldpMIBObjects, cudldpHelloIntervalExt=cudldpHelloIntervalExt, cudldpGlobalEnable=cudldpGlobalEnable, ciscoUdldpMIBGroups=ciscoUdldpMIBGroups, ciscoUdldpFastHelloGroup=ciscoUdldpFastHelloGroup, PYSNMP_MODULE_ID=ciscoUdldpMIB, cudldpIfOperHelloInterval=cudldpIfOperHelloInterval, cudldpHelloInterval=cudldpHelloInterval, cudldpInterfaceAdminMode=cudldpInterfaceAdminMode, cudldpIfFastHelloInterval=cudldpIfFastHelloInterval, ciscoUdldpAggreModeOptionalGroup=ciscoUdldpAggreModeOptionalGroup, ciscoUdldpMIBComplianceRev1=ciscoUdldpMIBComplianceRev1, cudldpIfFastHelloOperStatus=cudldpIfFastHelloOperStatus, ciscoUdldpMIBNotifs=ciscoUdldpMIBNotifs, cudldpFastHelloErrorReportEnable=cudldpFastHelloErrorReportEnable, ciscoUdldpMIBCompliance=ciscoUdldpMIBCompliance, ciscoUdldpMIBGroup2=ciscoUdldpMIBGroup2, cudldpInterfaceOperStatus=cudldpInterfaceOperStatus, cudldpInterfaceAggressiveMode=cudldpInterfaceAggressiveMode, cudldpFastHelloStatusChangeNotification=cudldpFastHelloStatusChangeNotification, cudldpInterfaceOperMode=cudldpInterfaceOperMode, cudldpFastHelloLinkFailRptNotifEnable=cudldpFastHelloLinkFailRptNotifEnable, ciscoUdldpMIBComplianceRev3=ciscoUdldpMIBComplianceRev3, cudldpFastHelloLinkFailRptNotification=cudldpFastHelloLinkFailRptNotification, ciscoUdldpMIBCompliances=ciscoUdldpMIBCompliances, cudldpInterfaceTable=cudldpInterfaceTable, ciscoUdldpFastHelloNotificationGroup=ciscoUdldpFastHelloNotificationGroup, ciscoUdldpMIBComplianceRev4=ciscoUdldpMIBComplianceRev4, ciscoUdldpMIBGroup3=ciscoUdldpMIBGroup3, ciscoUdldpMIBComplianceRev2=ciscoUdldpMIBComplianceRev2, cudldpGlobal=cudldpGlobal, cudldpFastHelloStatusChangeNotifEnable=cudldpFastHelloStatusChangeNotifEnable, cudldpInterfaceEntry=cudldpInterfaceEntry, cudldpInterfaceEnable=cudldpInterfaceEnable, cudldpFastHelloOperationalPorts=cudldpFastHelloOperationalPorts, cudldpFastHelloMaxPorts=cudldpFastHelloMaxPorts, cudldpGlobalMode=cudldpGlobalMode, cudldpFastHelloConfigPorts=cudldpFastHelloConfigPorts)
