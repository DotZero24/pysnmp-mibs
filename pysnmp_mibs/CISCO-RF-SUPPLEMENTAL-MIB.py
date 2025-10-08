#
# PySNMP MIB module CISCO-RF-SUPPLEMENTAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-RF-SUPPLEMENTAL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ConfigCopyState, = mibBuilder.importSymbols("CISCO-CONFIG-COPY-MIB", "ConfigCopyState")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
ifIndex, ifOperStatus, ifAdminStatus = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifOperStatus", "ifAdminStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
ciscoRfSupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 198))
ciscoRfSupMIB.setRevisions(('2019-02-22 00:00', '2004-05-27 00:00', '2004-03-04 00:00', '2001-03-16 00:00',))
if mibBuilder.loadTexts: ciscoRfSupMIB.setLastUpdated('201902220000Z')
if mibBuilder.loadTexts: ciscoRfSupMIB.setOrganization('Cisco Systems, Inc.')
class RfSupSyncAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enableAutoSync", 1), ("disableAutoSync", 2))

class RfSupSyncOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("inSync", 1), ("lastUpdateFailed", 2), ("commDown", 3), ("syncDisabled", 4), ("noStandbyPresent", 5))

ciscoRfSupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 0))
ciscoRfSupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1))
cRfSupSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1))
cRfSupCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2))
cRfSupAction = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3))
cRfSupSysAvailableStartTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysAvailableStartTime.setStatus('current')
cRfSupSysSwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysSwitchoverTime.setStatus('current')
cRfSupSysSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysSwitchovers.setStatus('current')
cRfSupSysRunningConfigSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysRunningConfigSyncTime.setStatus('current')
cRfSupSysRunningConfigAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 5), RfSupSyncAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysRunningConfigAdmin.setStatus('current')
cRfSupSysRunningConfigOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 6), RfSupSyncOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysRunningConfigOper.setStatus('current')
cRfSupSysStartupConfigSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysStartupConfigSyncTime.setStatus('current')
cRfSupSysStartupConfigAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 8), RfSupSyncAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysStartupConfigAdmin.setStatus('current')
cRfSupSysStartupConfigOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 9), RfSupSyncOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysStartupConfigOper.setStatus('current')
cRfSupSysBootImageSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysBootImageSyncTime.setStatus('current')
cRfSupSysBootImageAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 11), RfSupSyncAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysBootImageAdmin.setStatus('current')
cRfSupSysBootImageOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 12), RfSupSyncOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysBootImageOper.setStatus('current')
cRfSupSysStandbyBootFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysStandbyBootFile.setStatus('current')
cRfSupNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupNotificationsEnabled.setStatus('current')
cRfSupSysIfCounterSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysIfCounterSync.setStatus('current')
cRfSupSysFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysFailureReason.setStatus('current')
cRfSupSysSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("informational", 4), ("clear", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysSeverity.setStatus('current')
cRfSupSysErrorType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35))).clone(namedValues=NamedValues(("download-config", 1), ("download-code", 2), ("download-icon", 3), ("download-image", 4), ("download-signature", 5), ("download-webadmincert", 6), ("download-webauthcert", 7), ("download-webauthbundle", 8), ("download-eapdevcert", 9), ("download-eapcacert", 10), ("download-login-banner", 11), ("upload-config", 12), ("upload-debug-file", 13), ("upload-crashfile", 14), ("upload-watchdog-crash-file", 15), ("upload-panic-crash-file", 16), ("upload-coredump", 17), ("upload-errorlog", 18), ("upload-invalid-config", 19), ("upload-pac", 20), ("upload-radio-core-dump", 21), ("upload-ap-crash-data", 22), ("upload-signature", 23), ("upload-systemtrace", 24), ("upload-packet-capture", 25), ("upload-traplog", 26), ("route-add", 27), ("route-del", 28), ("interface-service-port", 29), ("reset", 30), ("other", 31), ("config-sync-fail", 32), ("peer-maintenance", 33), ("peer-loss", 34), ("rfTrapClearTemplist", 35)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysErrorType.setStatus('current')
cRfSupCpuTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1), )
if mibBuilder.loadTexts: cRfSupCpuTable.setStatus('current')
cRfSupCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuUniqueIndex"))
if mibBuilder.loadTexts: cRfSupCpuEntry.setStatus('current')
cRfSupCpuUniqueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 1), PhysicalIndex())
if mibBuilder.loadTexts: cRfSupCpuUniqueIndex.setStatus('current')
cRfSupCpuActiveSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("nonFaulty", 0), ("nonTrafficAffectingFault", 1), ("partialTrafficAffectingFault", 2), ("fullyTrafficAffectingFault", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupCpuActiveSeverity.setStatus('current')
cRfSupCpuInitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupCpuInitTime.setStatus('current')
cRfSupActionManualSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("runningConfig", 2), ("startupConfig", 3), ("bootImage", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupActionManualSync.setStatus('current')
cRfSupActionLastSyncResult = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3, 2), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupActionLastSyncResult.setStatus('current')
ciscoRfSupTimeChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 1)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"))
if mibBuilder.loadTexts: ciscoRfSupTimeChangeEvent.setStatus('current')
ciscoRfSupTimeZoneChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 2)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"))
if mibBuilder.loadTexts: ciscoRfSupTimeZoneChangeEvent.setStatus('current')
ciscoRfSupHAFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 3)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionManualSync"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionLastSyncResult"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysFailureReason"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSeverity"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysErrorType"))
if mibBuilder.loadTexts: ciscoRfSupHAFailureEvent.setStatus('current')
ciscoRfSupPeerLinkStateChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"))
if mibBuilder.loadTexts: ciscoRfSupPeerLinkStateChangeEvent.setStatus('current')
ciscoRfSupMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 2))
ciscoRfSupMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1))
ciscoRfSupMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2))
ciscoRfSupMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 1)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibCompliance = ciscoRfSupMibCompliance.setStatus('deprecated')
ciscoRfSupMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 2)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibComplianceRev1 = ciscoRfSupMibComplianceRev1.setStatus('deprecated')
ciscoRfSupMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 3)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupNotifGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalSyncGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibComplianceRev2 = ciscoRfSupMibComplianceRev2.setStatus('deprecated')
ciscoRfSupMibComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 4)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupNotifGroupRev1"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalSyncGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibComplianceRev3 = ciscoRfSupMibComplianceRev3.setStatus('current')
ciscoRfSupSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 1)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchovers"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigAdmin"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigOper"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigAdmin"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigOper"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageAdmin"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageOper"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStandbyBootFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupSysGroup = ciscoRfSupSysGroup.setStatus('current')
ciscoRfSupCpuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 2)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuActiveSeverity"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuInitTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupCpuGroup = ciscoRfSupCpuGroup.setStatus('current')
ciscoRfSupActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 3)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionManualSync"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionLastSyncResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupActionGroup = ciscoRfSupActionGroup.setStatus('current')
ciscoRfSupSysOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 4)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupNotificationsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupSysOptionalGroup = ciscoRfSupSysOptionalGroup.setStatus('current')
ciscoRfSupNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 5)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeChangeEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupNotifGroup = ciscoRfSupNotifGroup.setStatus('deprecated')
ciscoRfSupSysOptionalSyncGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 6)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysIfCounterSync"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupSysOptionalSyncGroup = ciscoRfSupSysOptionalSyncGroup.setStatus('current')
ciscoRfSupNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 7)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeChangeEvent"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeZoneChangeEvent"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupHAFailureEvent"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupPeerLinkStateChangeEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupNotifGroupRev1 = ciscoRfSupNotifGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-RF-SUPPLEMENTAL-MIB", cRfSupSysSwitchovers=cRfSupSysSwitchovers, cRfSupSysRunningConfigOper=cRfSupSysRunningConfigOper, ciscoRfSupMibConformance=ciscoRfSupMibConformance, cRfSupAction=cRfSupAction, ciscoRfSupMibComplianceRev2=ciscoRfSupMibComplianceRev2, ciscoRfSupMIBObjects=ciscoRfSupMIBObjects, ciscoRfSupSysGroup=ciscoRfSupSysGroup, cRfSupSystem=cRfSupSystem, cRfSupSysSwitchoverTime=cRfSupSysSwitchoverTime, cRfSupSysIfCounterSync=cRfSupSysIfCounterSync, cRfSupSysStartupConfigAdmin=cRfSupSysStartupConfigAdmin, cRfSupSysFailureReason=cRfSupSysFailureReason, cRfSupCpuInitTime=cRfSupCpuInitTime, cRfSupCpuEntry=cRfSupCpuEntry, ciscoRfSupMIB=ciscoRfSupMIB, cRfSupSysAvailableStartTime=cRfSupSysAvailableStartTime, cRfSupSysBootImageAdmin=cRfSupSysBootImageAdmin, cRfSupSysRunningConfigSyncTime=cRfSupSysRunningConfigSyncTime, ciscoRfSupSysOptionalGroup=ciscoRfSupSysOptionalGroup, cRfSupCpuUniqueIndex=cRfSupCpuUniqueIndex, ciscoRfSupTimeChangeEvent=ciscoRfSupTimeChangeEvent, ciscoRfSupNotifGroup=ciscoRfSupNotifGroup, cRfSupSysStartupConfigOper=cRfSupSysStartupConfigOper, ciscoRfSupMIBNotifs=ciscoRfSupMIBNotifs, RfSupSyncOperState=RfSupSyncOperState, PYSNMP_MODULE_ID=ciscoRfSupMIB, cRfSupSysStandbyBootFile=cRfSupSysStandbyBootFile, ciscoRfSupTimeZoneChangeEvent=ciscoRfSupTimeZoneChangeEvent, ciscoRfSupNotifGroupRev1=ciscoRfSupNotifGroupRev1, cRfSupNotificationsEnabled=cRfSupNotificationsEnabled, cRfSupCpu=cRfSupCpu, ciscoRfSupHAFailureEvent=ciscoRfSupHAFailureEvent, cRfSupCpuActiveSeverity=cRfSupCpuActiveSeverity, ciscoRfSupPeerLinkStateChangeEvent=ciscoRfSupPeerLinkStateChangeEvent, ciscoRfSupCpuGroup=ciscoRfSupCpuGroup, cRfSupSysBootImageSyncTime=cRfSupSysBootImageSyncTime, RfSupSyncAdminState=RfSupSyncAdminState, ciscoRfSupSysOptionalSyncGroup=ciscoRfSupSysOptionalSyncGroup, cRfSupSysStartupConfigSyncTime=cRfSupSysStartupConfigSyncTime, ciscoRfSupMibGroups=ciscoRfSupMibGroups, cRfSupActionLastSyncResult=cRfSupActionLastSyncResult, cRfSupSysSeverity=cRfSupSysSeverity, cRfSupSysErrorType=cRfSupSysErrorType, ciscoRfSupMibCompliances=ciscoRfSupMibCompliances, ciscoRfSupMibComplianceRev3=ciscoRfSupMibComplianceRev3, ciscoRfSupActionGroup=ciscoRfSupActionGroup, cRfSupSysBootImageOper=cRfSupSysBootImageOper, ciscoRfSupMibCompliance=ciscoRfSupMibCompliance, ciscoRfSupMibComplianceRev1=ciscoRfSupMibComplianceRev1, cRfSupCpuTable=cRfSupCpuTable, cRfSupSysRunningConfigAdmin=cRfSupSysRunningConfigAdmin, cRfSupActionManualSync=cRfSupActionManualSync)
