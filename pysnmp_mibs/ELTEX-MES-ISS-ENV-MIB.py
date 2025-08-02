_X='eltMesIssEnvFanSpeedLevel'
_W='eltMesIssEnvFanSpeed'
_V='eltMesIssBatteryLevel'
_U='eltMesIssBatteryStatus'
_T='eltMesIssEnvDryContactsState'
_S='eltMesIssEnvFanEntry'
_R='eltMesIssEnvPowerSourceIndex'
_Q='eltMesIssEnvFanThresholdLevel'
_P='eltMesIssBatteryStatusIndex'
_O='disable'
_N='enable'
_M='operational'
_L='issSwitchFanStatus'
_K='eltMesIssEnvDryContactsIndex'
_J='eltMesIssEnvDryContactsGroup'
_I='TruthValue'
_H='issSwitchFanIndex'
_G='read-write'
_F='ARICENT-ISS-MIB'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='ELTEX-MES-ISS-ENV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
issSwitchFanEntry,issSwitchFanIndex,issSwitchFanStatus=mibBuilder.importSymbols(_F,'issSwitchFanEntry',_H,_L)
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
eltMesIssEnvMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,12))
if mibBuilder.loadTexts:eltMesIssEnvMIB.setRevisions(('2019-04-04 00:00','2020-11-25 00:00','2021-04-01 00:00','2021-06-23 00:00'))
class EltMesIssBatteryState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notoperational',1),('notpresent',2),('recharge',3),('low',4),('discharge',5),(_M,6)))
_EltMesIssEnvObjects_ObjectIdentity=ObjectIdentity
eltMesIssEnvObjects=_EltMesIssEnvObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1))
_EltMesIssEnvDryContacts_ObjectIdentity=ObjectIdentity
eltMesIssEnvDryContacts=_EltMesIssEnvDryContacts_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1,1))
class _EltMesIssEnvDryContactsNotificationEnable_Type(TruthValue):defaultValue=2
_EltMesIssEnvDryContactsNotificationEnable_Type.__name__=_I
_EltMesIssEnvDryContactsNotificationEnable_Object=MibScalar
eltMesIssEnvDryContactsNotificationEnable=_EltMesIssEnvDryContactsNotificationEnable_Object((1,3,6,1,4,1,35265,1,139,12,1,1,1),_EltMesIssEnvDryContactsNotificationEnable_Type())
eltMesIssEnvDryContactsNotificationEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:eltMesIssEnvDryContactsNotificationEnable.setStatus(_A)
_EltMesIssEnvDryContactsStateTable_Object=MibTable
eltMesIssEnvDryContactsStateTable=_EltMesIssEnvDryContactsStateTable_Object((1,3,6,1,4,1,35265,1,139,12,1,1,2))
if mibBuilder.loadTexts:eltMesIssEnvDryContactsStateTable.setStatus(_A)
_EltMesIssEnvDryContactsStateEntry_Object=MibTableRow
eltMesIssEnvDryContactsStateEntry=_EltMesIssEnvDryContactsStateEntry_Object((1,3,6,1,4,1,35265,1,139,12,1,1,2,1))
eltMesIssEnvDryContactsStateEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:eltMesIssEnvDryContactsStateEntry.setStatus(_A)
class _EltMesIssEnvDryContactsGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssEnvDryContactsGroup_Type.__name__=_C
_EltMesIssEnvDryContactsGroup_Object=MibTableColumn
eltMesIssEnvDryContactsGroup=_EltMesIssEnvDryContactsGroup_Object((1,3,6,1,4,1,35265,1,139,12,1,1,2,1,1),_EltMesIssEnvDryContactsGroup_Type())
eltMesIssEnvDryContactsGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssEnvDryContactsGroup.setStatus(_A)
class _EltMesIssEnvDryContactsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssEnvDryContactsIndex_Type.__name__=_C
_EltMesIssEnvDryContactsIndex_Object=MibTableColumn
eltMesIssEnvDryContactsIndex=_EltMesIssEnvDryContactsIndex_Object((1,3,6,1,4,1,35265,1,139,12,1,1,2,1,2),_EltMesIssEnvDryContactsIndex_Type())
eltMesIssEnvDryContactsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssEnvDryContactsIndex.setStatus(_A)
class _EltMesIssEnvDryContactsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('opened',1),('closed',2)))
_EltMesIssEnvDryContactsState_Type.__name__=_C
_EltMesIssEnvDryContactsState_Object=MibTableColumn
eltMesIssEnvDryContactsState=_EltMesIssEnvDryContactsState_Object((1,3,6,1,4,1,35265,1,139,12,1,1,2,1,3),_EltMesIssEnvDryContactsState_Type())
eltMesIssEnvDryContactsState.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvDryContactsState.setStatus(_A)
_EltMesIssEnvResetButton_ObjectIdentity=ObjectIdentity
eltMesIssEnvResetButton=_EltMesIssEnvResetButton_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1,2))
class _EltEnvResetButtonMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),('reset-only',2)))
_EltEnvResetButtonMode_Type.__name__=_C
_EltEnvResetButtonMode_Object=MibScalar
eltEnvResetButtonMode=_EltEnvResetButtonMode_Object((1,3,6,1,4,1,35265,1,139,12,1,2,1),_EltEnvResetButtonMode_Type())
eltEnvResetButtonMode.setMaxAccess(_G)
if mibBuilder.loadTexts:eltEnvResetButtonMode.setStatus(_A)
_EltMesIssEnvBattery_ObjectIdentity=ObjectIdentity
eltMesIssEnvBattery=_EltMesIssEnvBattery_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1,3))
_EltMesIssBatteryStatusTable_Object=MibTable
eltMesIssBatteryStatusTable=_EltMesIssBatteryStatusTable_Object((1,3,6,1,4,1,35265,1,139,12,1,3,1))
if mibBuilder.loadTexts:eltMesIssBatteryStatusTable.setStatus(_A)
_EltMesIssBatteryStatusEntry_Object=MibTableRow
eltMesIssBatteryStatusEntry=_EltMesIssBatteryStatusEntry_Object((1,3,6,1,4,1,35265,1,139,12,1,3,1,1))
eltMesIssBatteryStatusEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:eltMesIssBatteryStatusEntry.setStatus(_A)
_EltMesIssBatteryStatusIndex_Type=Integer32
_EltMesIssBatteryStatusIndex_Object=MibTableColumn
eltMesIssBatteryStatusIndex=_EltMesIssBatteryStatusIndex_Object((1,3,6,1,4,1,35265,1,139,12,1,3,1,1,1),_EltMesIssBatteryStatusIndex_Type())
eltMesIssBatteryStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssBatteryStatusIndex.setStatus(_A)
_EltMesIssBatteryStatus_Type=EltMesIssBatteryState
_EltMesIssBatteryStatus_Object=MibTableColumn
eltMesIssBatteryStatus=_EltMesIssBatteryStatus_Object((1,3,6,1,4,1,35265,1,139,12,1,3,1,1,2),_EltMesIssBatteryStatus_Type())
eltMesIssBatteryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssBatteryStatus.setStatus(_A)
class _EltMesIssBatteryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100),ValueRangeConstraint(255,255))
_EltMesIssBatteryLevel_Type.__name__=_C
_EltMesIssBatteryLevel_Object=MibTableColumn
eltMesIssBatteryLevel=_EltMesIssBatteryLevel_Object((1,3,6,1,4,1,35265,1,139,12,1,3,1,1,3),_EltMesIssBatteryLevel_Type())
eltMesIssBatteryLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssBatteryLevel.setStatus(_A)
class _EltMesIssBatteryMonitorEnable_Type(TruthValue):defaultValue=1
_EltMesIssBatteryMonitorEnable_Type.__name__=_I
_EltMesIssBatteryMonitorEnable_Object=MibScalar
eltMesIssBatteryMonitorEnable=_EltMesIssBatteryMonitorEnable_Object((1,3,6,1,4,1,35265,1,139,12,1,3,2),_EltMesIssBatteryMonitorEnable_Type())
eltMesIssBatteryMonitorEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:eltMesIssBatteryMonitorEnable.setStatus(_A)
_EltMesIssEnvDyingGasp_ObjectIdentity=ObjectIdentity
eltMesIssEnvDyingGasp=_EltMesIssEnvDyingGasp_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1,4))
class _EltMesIssDyingGaspStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_EltMesIssDyingGaspStatus_Type.__name__=_C
_EltMesIssDyingGaspStatus_Object=MibScalar
eltMesIssDyingGaspStatus=_EltMesIssDyingGaspStatus_Object((1,3,6,1,4,1,35265,1,139,12,1,4,1),_EltMesIssDyingGaspStatus_Type())
eltMesIssDyingGaspStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:eltMesIssDyingGaspStatus.setStatus(_A)
_EltMesIssEnvFan_ObjectIdentity=ObjectIdentity
eltMesIssEnvFan=_EltMesIssEnvFan_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1,5))
_EltMesIssEnvFanTable_Object=MibTable
eltMesIssEnvFanTable=_EltMesIssEnvFanTable_Object((1,3,6,1,4,1,35265,1,139,12,1,5,1))
if mibBuilder.loadTexts:eltMesIssEnvFanTable.setStatus(_A)
_EltMesIssEnvFanEntry_Object=MibTableRow
eltMesIssEnvFanEntry=_EltMesIssEnvFanEntry_Object((1,3,6,1,4,1,35265,1,139,12,1,5,1,1))
if mibBuilder.loadTexts:eltMesIssEnvFanEntry.setStatus(_A)
class _EltMesIssEnvFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltMesIssEnvFanSpeed_Type.__name__=_C
_EltMesIssEnvFanSpeed_Object=MibTableColumn
eltMesIssEnvFanSpeed=_EltMesIssEnvFanSpeed_Object((1,3,6,1,4,1,35265,1,139,12,1,5,1,1,1),_EltMesIssEnvFanSpeed_Type())
eltMesIssEnvFanSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvFanSpeed.setStatus(_A)
class _EltMesIssEnvFanSpeedLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_EltMesIssEnvFanSpeedLevel_Type.__name__=_C
_EltMesIssEnvFanSpeedLevel_Object=MibTableColumn
eltMesIssEnvFanSpeedLevel=_EltMesIssEnvFanSpeedLevel_Object((1,3,6,1,4,1,35265,1,139,12,1,5,1,1,2),_EltMesIssEnvFanSpeedLevel_Type())
eltMesIssEnvFanSpeedLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvFanSpeedLevel.setStatus(_A)
_EltMesIssEnvFanThresholdTable_Object=MibTable
eltMesIssEnvFanThresholdTable=_EltMesIssEnvFanThresholdTable_Object((1,3,6,1,4,1,35265,1,139,12,1,5,2))
if mibBuilder.loadTexts:eltMesIssEnvFanThresholdTable.setStatus(_A)
_EltMesIssEnvFanThresholdEntry_Object=MibTableRow
eltMesIssEnvFanThresholdEntry=_EltMesIssEnvFanThresholdEntry_Object((1,3,6,1,4,1,35265,1,139,12,1,5,2,1))
eltMesIssEnvFanThresholdEntry.setIndexNames((0,_F,_H),(0,_B,_Q))
if mibBuilder.loadTexts:eltMesIssEnvFanThresholdEntry.setStatus(_A)
_EltMesIssEnvFanThresholdLevel_Type=Integer32
_EltMesIssEnvFanThresholdLevel_Object=MibTableColumn
eltMesIssEnvFanThresholdLevel=_EltMesIssEnvFanThresholdLevel_Object((1,3,6,1,4,1,35265,1,139,12,1,5,2,1,1),_EltMesIssEnvFanThresholdLevel_Type())
eltMesIssEnvFanThresholdLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssEnvFanThresholdLevel.setStatus(_A)
_EltMesIssEnvFanThresholdMin_Type=Integer32
_EltMesIssEnvFanThresholdMin_Object=MibTableColumn
eltMesIssEnvFanThresholdMin=_EltMesIssEnvFanThresholdMin_Object((1,3,6,1,4,1,35265,1,139,12,1,5,2,1,2),_EltMesIssEnvFanThresholdMin_Type())
eltMesIssEnvFanThresholdMin.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvFanThresholdMin.setStatus(_A)
_EltMesIssEnvFanThresholdMax_Type=Integer32
_EltMesIssEnvFanThresholdMax_Object=MibTableColumn
eltMesIssEnvFanThresholdMax=_EltMesIssEnvFanThresholdMax_Object((1,3,6,1,4,1,35265,1,139,12,1,5,2,1,3),_EltMesIssEnvFanThresholdMax_Type())
eltMesIssEnvFanThresholdMax.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvFanThresholdMax.setStatus(_A)
_EltMesIssEnvPowerSource_ObjectIdentity=ObjectIdentity
eltMesIssEnvPowerSource=_EltMesIssEnvPowerSource_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,1,6))
_EltMesIssEnvPowerSourceTable_Object=MibTable
eltMesIssEnvPowerSourceTable=_EltMesIssEnvPowerSourceTable_Object((1,3,6,1,4,1,35265,1,139,12,1,6,1))
if mibBuilder.loadTexts:eltMesIssEnvPowerSourceTable.setStatus(_A)
_EltMesIssEnvPowerSourceEntry_Object=MibTableRow
eltMesIssEnvPowerSourceEntry=_EltMesIssEnvPowerSourceEntry_Object((1,3,6,1,4,1,35265,1,139,12,1,6,1,1))
eltMesIssEnvPowerSourceEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:eltMesIssEnvPowerSourceEntry.setStatus(_A)
class _EltMesIssEnvPowerSourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssEnvPowerSourceIndex_Type.__name__=_C
_EltMesIssEnvPowerSourceIndex_Object=MibTableColumn
eltMesIssEnvPowerSourceIndex=_EltMesIssEnvPowerSourceIndex_Object((1,3,6,1,4,1,35265,1,139,12,1,6,1,1,1),_EltMesIssEnvPowerSourceIndex_Type())
eltMesIssEnvPowerSourceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssEnvPowerSourceIndex.setStatus(_A)
class _EltMesIssEnvPowerSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),('redundant',2)))
_EltMesIssEnvPowerSourceType_Type.__name__=_C
_EltMesIssEnvPowerSourceType_Object=MibTableColumn
eltMesIssEnvPowerSourceType=_EltMesIssEnvPowerSourceType_Object((1,3,6,1,4,1,35265,1,139,12,1,6,1,1,2),_EltMesIssEnvPowerSourceType_Type())
eltMesIssEnvPowerSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvPowerSourceType.setStatus(_A)
class _EltMesIssEnvPowerSourceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('not-operational',2),('not-present',3)))
_EltMesIssEnvPowerSourceState_Type.__name__=_C
_EltMesIssEnvPowerSourceState_Object=MibTableColumn
eltMesIssEnvPowerSourceState=_EltMesIssEnvPowerSourceState_Object((1,3,6,1,4,1,35265,1,139,12,1,6,1,1,3),_EltMesIssEnvPowerSourceState_Type())
eltMesIssEnvPowerSourceState.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssEnvPowerSourceState.setStatus(_A)
_EltMesIssEnvNotifications_ObjectIdentity=ObjectIdentity
eltMesIssEnvNotifications=_EltMesIssEnvNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,2))
_EltMesIssEnvNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltMesIssEnvNotificationsPrefix=_EltMesIssEnvNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,139,12,2,0))
issSwitchFanEntry.registerAugmentions((_B,_S))
eltMesIssEnvFanEntry.setIndexNames(*issSwitchFanEntry.getIndexNames())
eltMesIssEnvDryContactsTrap=NotificationType((1,3,6,1,4,1,35265,1,139,12,2,0,1))
eltMesIssEnvDryContactsTrap.setObjects(*((_B,_J),(_B,_K),(_B,_T)))
if mibBuilder.loadTexts:eltMesIssEnvDryContactsTrap.setStatus(_A)
eltMesIssBatteryTrap=NotificationType((1,3,6,1,4,1,35265,1,139,12,2,0,2))
eltMesIssBatteryTrap.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:eltMesIssBatteryTrap.setStatus(_A)
eltMesIssEnvFanStatusTrap=NotificationType((1,3,6,1,4,1,35265,1,139,12,2,0,3))
eltMesIssEnvFanStatusTrap.setObjects(*((_F,_H),(_F,_L),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:eltMesIssEnvFanStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EltMesIssBatteryState':EltMesIssBatteryState,'eltMesIssEnvMIB':eltMesIssEnvMIB,'eltMesIssEnvObjects':eltMesIssEnvObjects,'eltMesIssEnvDryContacts':eltMesIssEnvDryContacts,'eltMesIssEnvDryContactsNotificationEnable':eltMesIssEnvDryContactsNotificationEnable,'eltMesIssEnvDryContactsStateTable':eltMesIssEnvDryContactsStateTable,'eltMesIssEnvDryContactsStateEntry':eltMesIssEnvDryContactsStateEntry,_J:eltMesIssEnvDryContactsGroup,_K:eltMesIssEnvDryContactsIndex,_T:eltMesIssEnvDryContactsState,'eltMesIssEnvResetButton':eltMesIssEnvResetButton,'eltEnvResetButtonMode':eltEnvResetButtonMode,'eltMesIssEnvBattery':eltMesIssEnvBattery,'eltMesIssBatteryStatusTable':eltMesIssBatteryStatusTable,'eltMesIssBatteryStatusEntry':eltMesIssBatteryStatusEntry,_P:eltMesIssBatteryStatusIndex,_U:eltMesIssBatteryStatus,_V:eltMesIssBatteryLevel,'eltMesIssBatteryMonitorEnable':eltMesIssBatteryMonitorEnable,'eltMesIssEnvDyingGasp':eltMesIssEnvDyingGasp,'eltMesIssDyingGaspStatus':eltMesIssDyingGaspStatus,'eltMesIssEnvFan':eltMesIssEnvFan,'eltMesIssEnvFanTable':eltMesIssEnvFanTable,_S:eltMesIssEnvFanEntry,_W:eltMesIssEnvFanSpeed,_X:eltMesIssEnvFanSpeedLevel,'eltMesIssEnvFanThresholdTable':eltMesIssEnvFanThresholdTable,'eltMesIssEnvFanThresholdEntry':eltMesIssEnvFanThresholdEntry,_Q:eltMesIssEnvFanThresholdLevel,'eltMesIssEnvFanThresholdMin':eltMesIssEnvFanThresholdMin,'eltMesIssEnvFanThresholdMax':eltMesIssEnvFanThresholdMax,'eltMesIssEnvPowerSource':eltMesIssEnvPowerSource,'eltMesIssEnvPowerSourceTable':eltMesIssEnvPowerSourceTable,'eltMesIssEnvPowerSourceEntry':eltMesIssEnvPowerSourceEntry,_R:eltMesIssEnvPowerSourceIndex,'eltMesIssEnvPowerSourceType':eltMesIssEnvPowerSourceType,'eltMesIssEnvPowerSourceState':eltMesIssEnvPowerSourceState,'eltMesIssEnvNotifications':eltMesIssEnvNotifications,'eltMesIssEnvNotificationsPrefix':eltMesIssEnvNotificationsPrefix,'eltMesIssEnvDryContactsTrap':eltMesIssEnvDryContactsTrap,'eltMesIssBatteryTrap':eltMesIssBatteryTrap,'eltMesIssEnvFanStatusTrap':eltMesIssEnvFanStatusTrap})