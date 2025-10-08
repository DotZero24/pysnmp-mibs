#
# PySNMP MIB module Juniper-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-CLI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniLogSeverity, = mibBuilder.importSymbols("Juniper-TC", "JuniLogSeverity")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
juniCliMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30))
juniCliMIB.setRevisions(('2007-12-10 13:25', '2002-09-16 21:44', '2000-09-26 13:50', '1999-12-01 00:00',))
if mibBuilder.loadTexts: juniCliMIB.setLastUpdated('200712101325Z')
if mibBuilder.loadTexts: juniCliMIB.setOrganization('Juniper Networks, Inc.')
juniCliTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0))
juniCliObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1))
juniCliConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2))
juniCliGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1))
juniCliSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2))
juniCliSecurityTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniCliSecurityTrapEnable.setStatus('current')
juniCliConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3), )
if mibBuilder.loadTexts: juniCliConfigurationTable.setStatus('current')
juniCliConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1), ).setIndexNames((0, "Juniper-CLI-MIB", "juniCliConfigurationIndex"))
if mibBuilder.loadTexts: juniCliConfigurationEntry.setStatus('current')
juniCliConfigurationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: juniCliConfigurationIndex.setStatus('current')
juniCliConfigurationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniCliConfigurationFileName.setStatus('current')
juniCliConfigurationApply = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("juniCliConfigurationReadyToApply", 0), ("juniCliConfigurationApplyNow", 1))).clone('juniCliConfigurationReadyToApply')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniCliConfigurationApply.setStatus('current')
juniCliConfigurationOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("juniCliConfigurationOpNoOp", 0), ("juniCliConfigurationOpSuccessful", 1), ("juniCliConfigurationOpInProgress", 2), ("juniCliConfigurationFileNotFound", 3), ("juniCliConfigurationFileIncompatible", 4), ("juniCliConfigurationOperationFailed", 5))).clone('juniCliConfigurationOpNoOp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniCliConfigurationOpStatus.setStatus('current')
juniCliSecurityAlertPriority = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 1), JuniLogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniCliSecurityAlertPriority.setStatus('current')
juniCliSecurityAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniCliSecurityAlertMessage.setStatus('current')
juniCliSecurityAlertTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniCliSecurityAlertTime.setStatus('current')
juniCliSecurityAlert = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0, 1)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityAlertPriority"), ("Juniper-CLI-MIB", "juniCliSecurityAlertMessage"), ("Juniper-CLI-MIB", "juniCliSecurityAlertTime"))
if mibBuilder.loadTexts: juniCliSecurityAlert.setStatus('current')
juniCliCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1))
juniCliGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2))
juniCliCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 1)).setObjects(("Juniper-CLI-MIB", "juniCliGroup"), ("Juniper-CLI-MIB", "juniCliSecurityAlertGroup"), ("Juniper-CLI-MIB", "juniCliSecurityTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliCompliance = juniCliCompliance.setStatus('obsolete')
juniCliCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 2)).setObjects(("Juniper-CLI-MIB", "juniCliGroup"), ("Juniper-CLI-MIB", "juniCliSecurityAlertGroup"), ("Juniper-CLI-MIB", "juniCliSecurityTrapGroup"), ("Juniper-CLI-MIB", "juniCliConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliCompliance2 = juniCliCompliance2.setStatus('current')
juniCliGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 1)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliGroup = juniCliGroup.setStatus('current')
juniCliSecurityAlertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 2)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityAlertPriority"), ("Juniper-CLI-MIB", "juniCliSecurityAlertMessage"), ("Juniper-CLI-MIB", "juniCliSecurityAlertTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliSecurityAlertGroup = juniCliSecurityAlertGroup.setStatus('current')
juniCliSecurityTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 3)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliSecurityTrapGroup = juniCliSecurityTrapGroup.setStatus('current')
juniCliConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 4)).setObjects(("Juniper-CLI-MIB", "juniCliConfigurationFileName"), ("Juniper-CLI-MIB", "juniCliConfigurationApply"), ("Juniper-CLI-MIB", "juniCliConfigurationOpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliConfigurationGroup = juniCliConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-CLI-MIB", juniCliGeneral=juniCliGeneral, juniCliSecurityAlert=juniCliSecurityAlert, juniCliConfigurationGroup=juniCliConfigurationGroup, juniCliSecurityAlertGroup=juniCliSecurityAlertGroup, juniCliSecurityTrapEnable=juniCliSecurityTrapEnable, juniCliConfigurationIndex=juniCliConfigurationIndex, juniCliConfigurationTable=juniCliConfigurationTable, juniCliMIB=juniCliMIB, juniCliGroup=juniCliGroup, juniCliTrap=juniCliTrap, juniCliSecurityTrapGroup=juniCliSecurityTrapGroup, juniCliSecurityAlertTime=juniCliSecurityAlertTime, juniCliSecurity=juniCliSecurity, juniCliConfigurationFileName=juniCliConfigurationFileName, juniCliConfigurationOpStatus=juniCliConfigurationOpStatus, juniCliCompliance2=juniCliCompliance2, juniCliObjects=juniCliObjects, PYSNMP_MODULE_ID=juniCliMIB, juniCliGroups=juniCliGroups, juniCliConfigurationEntry=juniCliConfigurationEntry, juniCliSecurityAlertMessage=juniCliSecurityAlertMessage, juniCliCompliance=juniCliCompliance, juniCliSecurityAlertPriority=juniCliSecurityAlertPriority, juniCliCompliances=juniCliCompliances, juniCliConformance=juniCliConformance, juniCliConfigurationApply=juniCliConfigurationApply)
