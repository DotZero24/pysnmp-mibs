#
# PySNMP MIB module TIMETRA-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TIMETRA-ALARM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tmnxSRConfs, tmnxSRObjs, timetraSRMIBModules, tmnxSRNotifyPrefix = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRConfs", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRNotifyPrefix")
TmnxEnabledDisabled, = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxEnabledDisabled")
timetraAlarmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 77))
timetraAlarmMIBModule.setRevisions(('2011-02-01 00:00',))
if mibBuilder.loadTexts: timetraAlarmMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraAlarmMIBModule.setOrganization('Nokia')
tmnxAlarmObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77))
tmnxAlarmConfigTimeStamps = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 1))
tmnxAlarmConfigurations = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2))
tmnxAlarmSystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2, 1))
tmnxAlarmAdminState = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2, 1, 1), TmnxEnabledDisabled().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxAlarmAdminState.setStatus('current')
tmnxAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77))
tmnxAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1))
tmnxAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1, 1)).setObjects(("TIMETRA-ALARM-MIB", "tmnxAlarmSystemConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxAlarmCompliance = tmnxAlarmCompliance.setStatus('current')
tmnxAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2))
tmnxAlarmV9v0Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1))
tmnxAlarmSystemConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1, 1)).setObjects(("TIMETRA-ALARM-MIB", "tmnxAlarmAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxAlarmSystemConfigGroup = tmnxAlarmSystemConfigGroup.setStatus('current')
tmnxAlarmNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 77))
tmnxAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 77, 0))
mibBuilder.exportSymbols("TIMETRA-ALARM-MIB", PYSNMP_MODULE_ID=timetraAlarmMIBModule, tmnxAlarmAdminState=tmnxAlarmAdminState, tmnxAlarmConformance=tmnxAlarmConformance, tmnxAlarmNotifyPrefix=tmnxAlarmNotifyPrefix, tmnxAlarmV9v0Groups=tmnxAlarmV9v0Groups, tmnxAlarmConfigurations=tmnxAlarmConfigurations, tmnxAlarmObjs=tmnxAlarmObjs, tmnxAlarmConfigTimeStamps=tmnxAlarmConfigTimeStamps, tmnxAlarmCompliances=tmnxAlarmCompliances, tmnxAlarmGroups=tmnxAlarmGroups, tmnxAlarmSystemConfig=tmnxAlarmSystemConfig, tmnxAlarmSystemConfigGroup=tmnxAlarmSystemConfigGroup, timetraAlarmMIBModule=timetraAlarmMIBModule, tmnxAlarmNotifications=tmnxAlarmNotifications, tmnxAlarmCompliance=tmnxAlarmCompliance)
