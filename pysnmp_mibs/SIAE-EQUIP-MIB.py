_Y='equipManagerWakeUpAlarm'
_X='equipManagerWakeUpIpAddr'
_W='equipGosipAddress'
_V='equipLocation'
_U='equipStationID'
_T='equipConfigChange'
_S='equipMngtStatus'
_R='notActive'
_Q='trapEnable'
_P='trapDisable'
_O='AutonomousType'
_N='AlarmSeverityCode'
_M='trapV3'
_L='trapV2'
_K='trapV1'
_J='DisplayString'
_I='InterfaceIndex'
_H='equipLOMConnected'
_G='OctetString'
_F='equipIpSnmpAgentAddress'
_E='read-only'
_D='SIAE-EQUIP-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_I)
AlarmSeverityCode,AlarmStatus,alarmTrap=mibBuilder.importSymbols('SIAE-ALARM-MIB',_N,'AlarmStatus','alarmTrap')
equipTypeUnknown,=mibBuilder.importSymbols('SIAE-EQUIPTYPE-MIB','equipTypeUnknown')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,_J,'PhysAddress','TextualConvention')
equipment=ModuleIdentity((1,3,6,1,4,1,3373,1103,1))
if mibBuilder.loadTexts:equipment.setRevisions(('2018-11-29 00:00','2018-03-07 00:00','2015-03-23 00:00','2014-12-03 00:00','2014-07-01 00:00','2014-06-23 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _EquipMibVersion_Type(Integer32):defaultValue=1
_EquipMibVersion_Type.__name__=_C
_EquipMibVersion_Object=MibScalar
equipMibVersion=_EquipMibVersion_Object((1,3,6,1,4,1,3373,1103,1,1),_EquipMibVersion_Type())
equipMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:equipMibVersion.setStatus(_A)
_EquipCurrentTime_Type=TimeTicks
_EquipCurrentTime_Object=MibScalar
equipCurrentTime=_EquipCurrentTime_Object((1,3,6,1,4,1,3373,1103,1,2),_EquipCurrentTime_Type())
equipCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:equipCurrentTime.setStatus(_A)
_EquipUpTime_Type=TimeTicks
_EquipUpTime_Object=MibScalar
equipUpTime=_EquipUpTime_Object((1,3,6,1,4,1,3373,1103,1,3),_EquipUpTime_Type())
equipUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:equipUpTime.setStatus(_A)
class _EquipType_Type(AutonomousType):defaultValue=1,3,6,1,4,1,3373,1103,1,5,1
_EquipType_Type.__name__=_O
_EquipType_Object=MibScalar
equipType=_EquipType_Object((1,3,6,1,4,1,3373,1103,1,4),_EquipType_Type())
equipType.setMaxAccess(_E)
if mibBuilder.loadTexts:equipType.setStatus(_A)
_EquipIpEthOsiAddress_Type=IpAddress
_EquipIpEthOsiAddress_Object=MibScalar
equipIpEthOsiAddress=_EquipIpEthOsiAddress_Object((1,3,6,1,4,1,3373,1103,1,6),_EquipIpEthOsiAddress_Type())
equipIpEthOsiAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthOsiAddress.setStatus(_A)
class _EquipGosipAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EquipGosipAddress_Type.__name__=_G
_EquipGosipAddress_Object=MibScalar
equipGosipAddress=_EquipGosipAddress_Object((1,3,6,1,4,1,3373,1103,1,7),_EquipGosipAddress_Type())
equipGosipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipGosipAddress.setStatus(_A)
_EquipIpEthOsiNetMask_Type=IpAddress
_EquipIpEthOsiNetMask_Object=MibScalar
equipIpEthOsiNetMask=_EquipIpEthOsiNetMask_Object((1,3,6,1,4,1,3373,1103,1,8),_EquipIpEthOsiNetMask_Type())
equipIpEthOsiNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthOsiNetMask.setStatus(_A)
class _EquipL1L2IsIsRouting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l1',1),('l2',2)))
_EquipL1L2IsIsRouting_Type.__name__=_C
_EquipL1L2IsIsRouting_Object=MibScalar
equipL1L2IsIsRouting=_EquipL1L2IsIsRouting_Object((1,3,6,1,4,1,3373,1103,1,9),_EquipL1L2IsIsRouting_Type())
equipL1L2IsIsRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:equipL1L2IsIsRouting.setStatus(_A)
class _EquipStationID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_EquipStationID_Type.__name__=_J
_EquipStationID_Object=MibScalar
equipStationID=_EquipStationID_Object((1,3,6,1,4,1,3373,1103,1,10),_EquipStationID_Type())
equipStationID.setMaxAccess(_B)
if mibBuilder.loadTexts:equipStationID.setStatus(_A)
class _EquipLOMConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_EquipLOMConfigEnable_Type.__name__=_C
_EquipLOMConfigEnable_Object=MibScalar
equipLOMConfigEnable=_EquipLOMConfigEnable_Object((1,3,6,1,4,1,3373,1103,1,11),_EquipLOMConfigEnable_Type())
equipLOMConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:equipLOMConfigEnable.setStatus(_A)
class _EquipLOMConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cleared',1),('connectionAsMonitor',2),('connectionAsConfig',3)))
_EquipLOMConnected_Type.__name__=_C
_EquipLOMConnected_Object=MibScalar
equipLOMConnected=_EquipLOMConnected_Object((1,3,6,1,4,1,3373,1103,1,12),_EquipLOMConnected_Type())
equipLOMConnected.setMaxAccess(_E)
if mibBuilder.loadTexts:equipLOMConnected.setStatus(_A)
class _EquipLOMConnectedTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('trapEnableWithAck',3)))
_EquipLOMConnectedTrapEnable_Type.__name__=_C
_EquipLOMConnectedTrapEnable_Object=MibScalar
equipLOMConnectedTrapEnable=_EquipLOMConnectedTrapEnable_Object((1,3,6,1,4,1,3373,1103,1,13),_EquipLOMConnectedTrapEnable_Type())
equipLOMConnectedTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:equipLOMConnectedTrapEnable.setStatus(_A)
class _EquipConfigChange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_EquipConfigChange_Type.__name__=_G
_EquipConfigChange_Object=MibScalar
equipConfigChange=_EquipConfigChange_Object((1,3,6,1,4,1,3373,1103,1,14),_EquipConfigChange_Type())
equipConfigChange.setMaxAccess(_B)
if mibBuilder.loadTexts:equipConfigChange.setStatus(_A)
class _EquipConfigChangeTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('trapEnableWithACK',3)))
_EquipConfigChangeTrapEnable_Type.__name__=_C
_EquipConfigChangeTrapEnable_Object=MibScalar
equipConfigChangeTrapEnable=_EquipConfigChangeTrapEnable_Object((1,3,6,1,4,1,3373,1103,1,15),_EquipConfigChangeTrapEnable_Type())
equipConfigChangeTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:equipConfigChangeTrapEnable.setStatus(_A)
class _EquipRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,11,20,21,50,100,125,126,127)));namedValues=NamedValues(*((_R,0),('restart',1),('applyIfChange',2),('revertIfChange',3),('configClearAndRestart',4),('routeTableClear',5),('uploadBaseBand',6),('offLineRouteRetrieve',7),('offLineRouteSave',8),('hotApplyIfChange',11),('ipStackConfigure',20),('osiStackConfigure',21),('atuTableReset',50),('siaeReservedReq1',100),('siaeReservedReq26',125),('siaeReservedReq27',126),('switchFactoryDefault',127)))
_EquipRequest_Type.__name__=_C
_EquipRequest_Object=MibScalar
equipRequest=_EquipRequest_Object((1,3,6,1,4,1,3373,1103,1,16),_EquipRequest_Type())
equipRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:equipRequest.setStatus(_A)
_EquipIpEthAddress_Type=IpAddress
_EquipIpEthAddress_Object=MibScalar
equipIpEthAddress=_EquipIpEthAddress_Object((1,3,6,1,4,1,3373,1103,1,17),_EquipIpEthAddress_Type())
equipIpEthAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthAddress.setStatus(_A)
_EquipIpEthNetMask_Type=IpAddress
_EquipIpEthNetMask_Object=MibScalar
equipIpEthNetMask=_EquipIpEthNetMask_Object((1,3,6,1,4,1,3373,1103,1,18),_EquipIpEthNetMask_Type())
equipIpEthNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthNetMask.setStatus(_A)
class _EquipOsiamParameter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,41))
_EquipOsiamParameter_Type.__name__=_G
_EquipOsiamParameter_Object=MibScalar
equipOsiamParameter=_EquipOsiamParameter_Object((1,3,6,1,4,1,3373,1103,1,19),_EquipOsiamParameter_Type())
equipOsiamParameter.setMaxAccess(_B)
if mibBuilder.loadTexts:equipOsiamParameter.setStatus(_A)
_EquipIpSnmpAgentAddress_Type=IpAddress
_EquipIpSnmpAgentAddress_Object=MibScalar
equipIpSnmpAgentAddress=_EquipIpSnmpAgentAddress_Object((1,3,6,1,4,1,3373,1103,1,20),_EquipIpSnmpAgentAddress_Type())
equipIpSnmpAgentAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpSnmpAgentAddress.setStatus(_A)
class _EquipOperationInProgress_Type(Integer32):defaultValue=0
_EquipOperationInProgress_Type.__name__=_C
_EquipOperationInProgress_Object=MibScalar
equipOperationInProgress=_EquipOperationInProgress_Object((1,3,6,1,4,1,3373,1103,1,21),_EquipOperationInProgress_Type())
equipOperationInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipOperationInProgress.setStatus(_A)
_EquipManagerWakeUpAlarm_Type=AlarmStatus
_EquipManagerWakeUpAlarm_Object=MibScalar
equipManagerWakeUpAlarm=_EquipManagerWakeUpAlarm_Object((1,3,6,1,4,1,3373,1103,1,22),_EquipManagerWakeUpAlarm_Type())
equipManagerWakeUpAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:equipManagerWakeUpAlarm.setStatus(_A)
class _EquipManagerWakeUpAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=1
_EquipManagerWakeUpAlarmSeverityCode_Type.__name__=_N
_EquipManagerWakeUpAlarmSeverityCode_Object=MibScalar
equipManagerWakeUpAlarmSeverityCode=_EquipManagerWakeUpAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,1,23),_EquipManagerWakeUpAlarmSeverityCode_Type())
equipManagerWakeUpAlarmSeverityCode.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManagerWakeUpAlarmSeverityCode.setStatus(_A)
class _EquipManagerWakeUpTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_EquipManagerWakeUpTimeout_Type.__name__=_C
_EquipManagerWakeUpTimeout_Object=MibScalar
equipManagerWakeUpTimeout=_EquipManagerWakeUpTimeout_Object((1,3,6,1,4,1,3373,1103,1,24),_EquipManagerWakeUpTimeout_Type())
equipManagerWakeUpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManagerWakeUpTimeout.setStatus(_A)
_EquipManagerWakeUpIpAddr_Type=IpAddress
_EquipManagerWakeUpIpAddr_Object=MibScalar
equipManagerWakeUpIpAddr=_EquipManagerWakeUpIpAddr_Object((1,3,6,1,4,1,3373,1103,1,25),_EquipManagerWakeUpIpAddr_Type())
equipManagerWakeUpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManagerWakeUpIpAddr.setStatus(_A)
class _EquipManagerWakeUpGosipAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EquipManagerWakeUpGosipAddress_Type.__name__=_G
_EquipManagerWakeUpGosipAddress_Object=MibScalar
equipManagerWakeUpGosipAddress=_EquipManagerWakeUpGosipAddress_Object((1,3,6,1,4,1,3373,1103,1,26),_EquipManagerWakeUpGosipAddress_Type())
equipManagerWakeUpGosipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManagerWakeUpGosipAddress.setStatus(_A)
class _EquipManagerWakeUpTrapVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_EquipManagerWakeUpTrapVersion_Type.__name__=_C
_EquipManagerWakeUpTrapVersion_Object=MibScalar
equipManagerWakeUpTrapVersion=_EquipManagerWakeUpTrapVersion_Object((1,3,6,1,4,1,3373,1103,1,27),_EquipManagerWakeUpTrapVersion_Type())
equipManagerWakeUpTrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManagerWakeUpTrapVersion.setStatus(_A)
_EquipManager1IpAddr_Type=IpAddress
_EquipManager1IpAddr_Object=MibScalar
equipManager1IpAddr=_EquipManager1IpAddr_Object((1,3,6,1,4,1,3373,1103,1,28),_EquipManager1IpAddr_Type())
equipManager1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManager1IpAddr.setStatus(_A)
_EquipManager2IpAddr_Type=IpAddress
_EquipManager2IpAddr_Object=MibScalar
equipManager2IpAddr=_EquipManager2IpAddr_Object((1,3,6,1,4,1,3373,1103,1,29),_EquipManager2IpAddr_Type())
equipManager2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManager2IpAddr.setStatus(_A)
class _EquipManager1TrapVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_EquipManager1TrapVersion_Type.__name__=_C
_EquipManager1TrapVersion_Object=MibScalar
equipManager1TrapVersion=_EquipManager1TrapVersion_Object((1,3,6,1,4,1,3373,1103,1,30),_EquipManager1TrapVersion_Type())
equipManager1TrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManager1TrapVersion.setStatus(_A)
class _EquipManager2TrapVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_EquipManager2TrapVersion_Type.__name__=_C
_EquipManager2TrapVersion_Object=MibScalar
equipManager2TrapVersion=_EquipManager2TrapVersion_Object((1,3,6,1,4,1,3373,1103,1,31),_EquipManager2TrapVersion_Type())
equipManager2TrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:equipManager2TrapVersion.setStatus(_A)
class _EquipDailyPmTimeZone_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_EquipDailyPmTimeZone_Type.__name__=_C
_EquipDailyPmTimeZone_Object=MibScalar
equipDailyPmTimeZone=_EquipDailyPmTimeZone_Object((1,3,6,1,4,1,3373,1103,1,32),_EquipDailyPmTimeZone_Type())
equipDailyPmTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:equipDailyPmTimeZone.setStatus(_A)
class _EquipOperationMngtControl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('startOperation',1),('confirmOperation',2)))
_EquipOperationMngtControl_Type.__name__=_C
_EquipOperationMngtControl_Object=MibScalar
equipOperationMngtControl=_EquipOperationMngtControl_Object((1,3,6,1,4,1,3373,1103,1,33),_EquipOperationMngtControl_Type())
equipOperationMngtControl.setMaxAccess(_B)
if mibBuilder.loadTexts:equipOperationMngtControl.setStatus(_A)
_EquipOperationMngtInProgress_Type=Integer32
_EquipOperationMngtInProgress_Object=MibScalar
equipOperationMngtInProgress=_EquipOperationMngtInProgress_Object((1,3,6,1,4,1,3373,1103,1,34),_EquipOperationMngtInProgress_Type())
equipOperationMngtInProgress.setMaxAccess(_E)
if mibBuilder.loadTexts:equipOperationMngtInProgress.setStatus(_A)
class _EquipLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_EquipLocation_Type.__name__=_J
_EquipLocation_Object=MibScalar
equipLocation=_EquipLocation_Object((1,3,6,1,4,1,3373,1103,1,35),_EquipLocation_Type())
equipLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:equipLocation.setStatus(_A)
_EquipLongitude_Type=Integer32
_EquipLongitude_Object=MibScalar
equipLongitude=_EquipLongitude_Object((1,3,6,1,4,1,3373,1103,1,36),_EquipLongitude_Type())
equipLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:equipLongitude.setStatus(_A)
_EquipLatitude_Type=Integer32
_EquipLatitude_Object=MibScalar
equipLatitude=_EquipLatitude_Object((1,3,6,1,4,1,3373,1103,1,37),_EquipLatitude_Type())
equipLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:equipLatitude.setStatus(_A)
class _EquipIpEthVlanId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_EquipIpEthVlanId_Type.__name__=_C
_EquipIpEthVlanId_Object=MibScalar
equipIpEthVlanId=_EquipIpEthVlanId_Object((1,3,6,1,4,1,3373,1103,1,38),_EquipIpEthVlanId_Type())
equipIpEthVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthVlanId.setStatus(_A)
_EquipIpEthDefGateway_Type=IpAddress
_EquipIpEthDefGateway_Object=MibScalar
equipIpEthDefGateway=_EquipIpEthDefGateway_Object((1,3,6,1,4,1,3373,1103,1,39),_EquipIpEthDefGateway_Type())
equipIpEthDefGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthDefGateway.setStatus(_A)
class _EquipIpEthDefGatewayIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_EquipIpEthDefGatewayIfIndex_Type.__name__=_I
_EquipIpEthDefGatewayIfIndex_Object=MibScalar
equipIpEthDefGatewayIfIndex=_EquipIpEthDefGatewayIfIndex_Object((1,3,6,1,4,1,3373,1103,1,40),_EquipIpEthDefGatewayIfIndex_Type())
equipIpEthDefGatewayIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:equipIpEthDefGatewayIfIndex.setStatus(_A)
_EquipMngtTable_Object=MibTable
equipMngtTable=_EquipMngtTable_Object((1,3,6,1,4,1,3373,1103,1,41))
if mibBuilder.loadTexts:equipMngtTable.setStatus(_A)
_EquipMngtTableEntry_Object=MibTableRow
equipMngtTableEntry=_EquipMngtTableEntry_Object((1,3,6,1,4,1,3373,1103,1,41,1))
equipMngtTableEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:equipMngtTableEntry.setStatus(_A)
class _EquipMngtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operational',1),('administrative',2)))
_EquipMngtStatus_Type.__name__=_C
_EquipMngtStatus_Object=MibTableColumn
equipMngtStatus=_EquipMngtStatus_Object((1,3,6,1,4,1,3373,1103,1,41,1,1),_EquipMngtStatus_Type())
equipMngtStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:equipMngtStatus.setStatus(_A)
_EquipMngtIpAddress_Type=IpAddress
_EquipMngtIpAddress_Object=MibTableColumn
equipMngtIpAddress=_EquipMngtIpAddress_Object((1,3,6,1,4,1,3373,1103,1,41,1,2),_EquipMngtIpAddress_Type())
equipMngtIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIpAddress.setStatus(_A)
_EquipMngtIpNetMask_Type=IpAddress
_EquipMngtIpNetMask_Object=MibTableColumn
equipMngtIpNetMask=_EquipMngtIpNetMask_Object((1,3,6,1,4,1,3373,1103,1,41,1,3),_EquipMngtIpNetMask_Type())
equipMngtIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIpNetMask.setStatus(_A)
_EquipMngtIpDefGateway_Type=IpAddress
_EquipMngtIpDefGateway_Object=MibTableColumn
equipMngtIpDefGateway=_EquipMngtIpDefGateway_Object((1,3,6,1,4,1,3373,1103,1,41,1,4),_EquipMngtIpDefGateway_Type())
equipMngtIpDefGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIpDefGateway.setStatus(_A)
class _EquipMngtIpDefGatewayIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_EquipMngtIpDefGatewayIfIndex_Type.__name__=_I
_EquipMngtIpDefGatewayIfIndex_Object=MibTableColumn
equipMngtIpDefGatewayIfIndex=_EquipMngtIpDefGatewayIfIndex_Object((1,3,6,1,4,1,3373,1103,1,41,1,5),_EquipMngtIpDefGatewayIfIndex_Type())
equipMngtIpDefGatewayIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIpDefGatewayIfIndex.setStatus(_A)
class _EquipMngtIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ethernet',1),('loopback',2),('vlan',3)))
_EquipMngtIfType_Type.__name__=_C
_EquipMngtIfType_Object=MibTableColumn
equipMngtIfType=_EquipMngtIfType_Object((1,3,6,1,4,1,3373,1103,1,41,1,6),_EquipMngtIfType_Type())
equipMngtIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIfType.setStatus(_A)
class _EquipMngtIfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_EquipMngtIfId_Type.__name__=_C
_EquipMngtIfId_Object=MibTableColumn
equipMngtIfId=_EquipMngtIfId_Object((1,3,6,1,4,1,3373,1103,1,41,1,7),_EquipMngtIfId_Type())
equipMngtIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIfId.setStatus(_A)
_EquipMngtIfPortVlanId_Type=InterfaceIndex
_EquipMngtIfPortVlanId_Object=MibTableColumn
equipMngtIfPortVlanId=_EquipMngtIfPortVlanId_Object((1,3,6,1,4,1,3373,1103,1,41,1,8),_EquipMngtIfPortVlanId_Type())
equipMngtIfPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:equipMngtIfPortVlanId.setStatus(_A)
class _EquipLastRestartType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,41))
_EquipLastRestartType_Type.__name__=_G
_EquipLastRestartType_Object=MibScalar
equipLastRestartType=_EquipLastRestartType_Object((1,3,6,1,4,1,3373,1103,1,42),_EquipLastRestartType_Type())
equipLastRestartType.setMaxAccess(_E)
if mibBuilder.loadTexts:equipLastRestartType.setStatus(_A)
equipLOMConnectedMonitor=NotificationType((1,3,6,1,4,1,3373,1103,0,109))
equipLOMConnectedMonitor.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:equipLOMConnectedMonitor.setStatus(_A)
equipLOMConnectedConfig=NotificationType((1,3,6,1,4,1,3373,1103,0,110))
equipLOMConnectedConfig.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:equipLOMConnectedConfig.setStatus(_A)
equipLOMDisconnected=NotificationType((1,3,6,1,4,1,3373,1103,0,111))
equipLOMDisconnected.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:equipLOMDisconnected.setStatus(_A)
equipConfigChangeStatus=NotificationType((1,3,6,1,4,1,3373,1103,0,114))
equipConfigChangeStatus.setObjects(*((_D,_F),(_D,_T)))
if mibBuilder.loadTexts:equipConfigChangeStatus.setStatus(_A)
equipManagerWakeUpNotify=NotificationType((1,3,6,1,4,1,3373,1103,0,123))
equipManagerWakeUpNotify.setObjects(*((_D,_F),(_D,_U),(_D,_V),(_D,_F),(_D,_W),(_D,_X),(_D,_Y)))
if mibBuilder.loadTexts:equipManagerWakeUpNotify.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'equipLOMConnectedMonitor':equipLOMConnectedMonitor,'equipLOMConnectedConfig':equipLOMConnectedConfig,'equipLOMDisconnected':equipLOMDisconnected,'equipConfigChangeStatus':equipConfigChangeStatus,'equipManagerWakeUpNotify':equipManagerWakeUpNotify,'equipment':equipment,'equipMibVersion':equipMibVersion,'equipCurrentTime':equipCurrentTime,'equipUpTime':equipUpTime,'equipType':equipType,'equipIpEthOsiAddress':equipIpEthOsiAddress,_W:equipGosipAddress,'equipIpEthOsiNetMask':equipIpEthOsiNetMask,'equipL1L2IsIsRouting':equipL1L2IsIsRouting,_U:equipStationID,'equipLOMConfigEnable':equipLOMConfigEnable,_H:equipLOMConnected,'equipLOMConnectedTrapEnable':equipLOMConnectedTrapEnable,_T:equipConfigChange,'equipConfigChangeTrapEnable':equipConfigChangeTrapEnable,'equipRequest':equipRequest,'equipIpEthAddress':equipIpEthAddress,'equipIpEthNetMask':equipIpEthNetMask,'equipOsiamParameter':equipOsiamParameter,_F:equipIpSnmpAgentAddress,'equipOperationInProgress':equipOperationInProgress,_Y:equipManagerWakeUpAlarm,'equipManagerWakeUpAlarmSeverityCode':equipManagerWakeUpAlarmSeverityCode,'equipManagerWakeUpTimeout':equipManagerWakeUpTimeout,_X:equipManagerWakeUpIpAddr,'equipManagerWakeUpGosipAddress':equipManagerWakeUpGosipAddress,'equipManagerWakeUpTrapVersion':equipManagerWakeUpTrapVersion,'equipManager1IpAddr':equipManager1IpAddr,'equipManager2IpAddr':equipManager2IpAddr,'equipManager1TrapVersion':equipManager1TrapVersion,'equipManager2TrapVersion':equipManager2TrapVersion,'equipDailyPmTimeZone':equipDailyPmTimeZone,'equipOperationMngtControl':equipOperationMngtControl,'equipOperationMngtInProgress':equipOperationMngtInProgress,_V:equipLocation,'equipLongitude':equipLongitude,'equipLatitude':equipLatitude,'equipIpEthVlanId':equipIpEthVlanId,'equipIpEthDefGateway':equipIpEthDefGateway,'equipIpEthDefGatewayIfIndex':equipIpEthDefGatewayIfIndex,'equipMngtTable':equipMngtTable,'equipMngtTableEntry':equipMngtTableEntry,_S:equipMngtStatus,'equipMngtIpAddress':equipMngtIpAddress,'equipMngtIpNetMask':equipMngtIpNetMask,'equipMngtIpDefGateway':equipMngtIpDefGateway,'equipMngtIpDefGatewayIfIndex':equipMngtIpDefGatewayIfIndex,'equipMngtIfType':equipMngtIfType,'equipMngtIfId':equipMngtIfId,'equipMngtIfPortVlanId':equipMngtIfPortVlanId,'equipLastRestartType':equipLastRestartType})