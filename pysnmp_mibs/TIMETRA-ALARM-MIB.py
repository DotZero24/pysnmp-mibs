#
# PySNMP MIB module TIMETRA-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TIMETRA-ALARM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:38:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tmnxSRObjs, timetraSRMIBModules, tmnxSRNotifyPrefix, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRNotifyPrefix", "tmnxSRConfs")
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
mibBuilder.exportSymbols("TIMETRA-ALARM-MIB", tmnxAlarmConfigTimeStamps=tmnxAlarmConfigTimeStamps, tmnxAlarmAdminState=tmnxAlarmAdminState, tmnxAlarmCompliance=tmnxAlarmCompliance, tmnxAlarmNotifications=tmnxAlarmNotifications, tmnxAlarmV9v0Groups=tmnxAlarmV9v0Groups, tmnxAlarmSystemConfigGroup=tmnxAlarmSystemConfigGroup, tmnxAlarmObjs=tmnxAlarmObjs, tmnxAlarmSystemConfig=tmnxAlarmSystemConfig, tmnxAlarmConfigurations=tmnxAlarmConfigurations, timetraAlarmMIBModule=timetraAlarmMIBModule, tmnxAlarmGroups=tmnxAlarmGroups, PYSNMP_MODULE_ID=timetraAlarmMIBModule, tmnxAlarmConformance=tmnxAlarmConformance, tmnxAlarmNotifyPrefix=tmnxAlarmNotifyPrefix, tmnxAlarmCompliances=tmnxAlarmCompliances)
