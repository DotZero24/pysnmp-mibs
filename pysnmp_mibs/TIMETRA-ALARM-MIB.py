_E='tmnxAlarmSystemConfigGroup'
_D='tmnxAlarmAdminState'
_C='TmnxEnabledDisabled'
_B='TIMETRA-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxEnabledDisabled,=mibBuilder.importSymbols('TIMETRA-TC-MIB',_C)
timetraAlarmMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,77))
if mibBuilder.loadTexts:timetraAlarmMIBModule.setRevisions(('2011-02-01 00:00',))
_TmnxAlarmConformance_ObjectIdentity=ObjectIdentity
tmnxAlarmConformance=_TmnxAlarmConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,77))
_TmnxAlarmCompliances_ObjectIdentity=ObjectIdentity
tmnxAlarmCompliances=_TmnxAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,77,1))
_TmnxAlarmGroups_ObjectIdentity=ObjectIdentity
tmnxAlarmGroups=_TmnxAlarmGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,77,2))
_TmnxAlarmV9v0Groups_ObjectIdentity=ObjectIdentity
tmnxAlarmV9v0Groups=_TmnxAlarmV9v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,77,2,1))
_TmnxAlarmObjs_ObjectIdentity=ObjectIdentity
tmnxAlarmObjs=_TmnxAlarmObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,77))
_TmnxAlarmConfigTimeStamps_ObjectIdentity=ObjectIdentity
tmnxAlarmConfigTimeStamps=_TmnxAlarmConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,77,1))
_TmnxAlarmConfigurations_ObjectIdentity=ObjectIdentity
tmnxAlarmConfigurations=_TmnxAlarmConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,77,2))
_TmnxAlarmSystemConfig_ObjectIdentity=ObjectIdentity
tmnxAlarmSystemConfig=_TmnxAlarmSystemConfig_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,77,2,1))
class _TmnxAlarmAdminState_Type(TmnxEnabledDisabled):defaultValue=1
_TmnxAlarmAdminState_Type.__name__=_C
_TmnxAlarmAdminState_Object=MibScalar
tmnxAlarmAdminState=_TmnxAlarmAdminState_Object((1,3,6,1,4,1,6527,3,1,2,77,2,1,1),_TmnxAlarmAdminState_Type())
tmnxAlarmAdminState.setMaxAccess('read-write')
if mibBuilder.loadTexts:tmnxAlarmAdminState.setStatus(_A)
_TmnxAlarmNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxAlarmNotifyPrefix=_TmnxAlarmNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,77))
_TmnxAlarmNotifications_ObjectIdentity=ObjectIdentity
tmnxAlarmNotifications=_TmnxAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,77,0))
tmnxAlarmSystemConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,77,2,1,1))
tmnxAlarmSystemConfigGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:tmnxAlarmSystemConfigGroup.setStatus(_A)
tmnxAlarmCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,77,1,1))
tmnxAlarmCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:tmnxAlarmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraAlarmMIBModule':timetraAlarmMIBModule,'tmnxAlarmConformance':tmnxAlarmConformance,'tmnxAlarmCompliances':tmnxAlarmCompliances,'tmnxAlarmCompliance':tmnxAlarmCompliance,'tmnxAlarmGroups':tmnxAlarmGroups,'tmnxAlarmV9v0Groups':tmnxAlarmV9v0Groups,_E:tmnxAlarmSystemConfigGroup,'tmnxAlarmObjs':tmnxAlarmObjs,'tmnxAlarmConfigTimeStamps':tmnxAlarmConfigTimeStamps,'tmnxAlarmConfigurations':tmnxAlarmConfigurations,'tmnxAlarmSystemConfig':tmnxAlarmSystemConfig,_D:tmnxAlarmAdminState,'tmnxAlarmNotifyPrefix':tmnxAlarmNotifyPrefix,'tmnxAlarmNotifications':tmnxAlarmNotifications})