_U='newStormControlInterface'
_T='controlPort'
_S='stormControlType'
_R='stormControlInterface'
_Q='qosLineRateInterface'
_P='disable'
_O='enable'
_N='disabled'
_M='enabled'
_L='l3IpAddress'
_K='aggPort'
_J='aggUnit'
_I='portNumber'
_H='DisplayString'
_G='portFlowAlarmPort'
_F='obsolete'
_E='GBNDeviceSwitch-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnDevice,=mibBuilder.importSymbols('GREENTECH-MASTER-MIB','gbnDevice')
PortList,VlanIndex,dot1qStaticMulticastEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex','dot1qStaticMulticastEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnDeviceSwitch=ModuleIdentity((1,3,6,1,4,1,13464,1,2,2,1))
if mibBuilder.loadTexts:gbnDeviceSwitch.setRevisions(('2018-02-14 00:00','1900-11-02 00:00'))
_GbnDeviceSwitchMirror_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchMirror=_GbnDeviceSwitchMirror_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,1))
class _MirroringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,26))
_MirroringPort_Type.__name__=_C
_MirroringPort_Object=MibScalar
mirroringPort=_MirroringPort_Object((1,3,6,1,4,1,13464,1,2,2,1,1,1),_MirroringPort_Type())
mirroringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirroringPort.setStatus(_A)
_MirroredEgrPort_Type=PortList
_MirroredEgrPort_Object=MibScalar
mirroredEgrPort=_MirroredEgrPort_Object((1,3,6,1,4,1,13464,1,2,2,1,1,2),_MirroredEgrPort_Type())
mirroredEgrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirroredEgrPort.setStatus(_A)
_MirroredIgrPort_Type=PortList
_MirroredIgrPort_Object=MibScalar
mirroredIgrPort=_MirroredIgrPort_Object((1,3,6,1,4,1,13464,1,2,2,1,1,3),_MirroredIgrPort_Type())
mirroredIgrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirroredIgrPort.setStatus(_A)
_GbnDeviceSwitchPort_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchPort=_GbnDeviceSwitchPort_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,2))
_PortTypeTable_Object=MibTable
portTypeTable=_PortTypeTable_Object((1,3,6,1,4,1,13464,1,2,2,1,2,1))
if mibBuilder.loadTexts:portTypeTable.setStatus(_A)
_PortTypeEntry_Object=MibTableRow
portTypeEntry=_PortTypeEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,2,1,1))
portTypeEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:portTypeEntry.setStatus(_A)
class _PortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_PortNumber_Type.__name__=_C
_PortNumber_Object=MibTableColumn
portNumber=_PortNumber_Object((1,3,6,1,4,1,13464,1,2,2,1,2,1,1,1),_PortNumber_Type())
portNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:portNumber.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,9,10,11,12,13)));namedValues=NamedValues(*(('blank',1),('fE',2),('single100FX',3),('double100FX',4),('single1000FX',5),('double1000FX',6),('fE1000',7),('SM-2SC-1310-25',9),('MM-2SC-1310-2',10),('MM-2SC-850-2',11),('SM-1SC-1550-20',12),('SM-1SC-1310-20',13)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,13464,1,2,2,1,2,1,1,2),_PortType_Type())
portType.setMaxAccess(_D)
if mibBuilder.loadTexts:portType.setStatus(_A)
_GbnDeviceSwitchAggregation_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchAggregation=_GbnDeviceSwitchAggregation_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,3))
_AggTable_Object=MibTable
aggTable=_AggTable_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1))
if mibBuilder.loadTexts:aggTable.setStatus(_F)
_AggEntry_Object=MibTableRow
aggEntry=_AggEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1,1))
aggEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:aggEntry.setStatus(_F)
_AggUnit_Type=Integer32
_AggUnit_Object=MibTableColumn
aggUnit=_AggUnit_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1,1,1),_AggUnit_Type())
aggUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:aggUnit.setStatus(_F)
_AggPort_Type=Integer32
_AggPort_Object=MibTableColumn
aggPort=_AggPort_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1,1,2),_AggPort_Type())
aggPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aggPort.setStatus(_F)
_AggPortListPorts_Type=PortList
_AggPortListPorts_Object=MibTableColumn
aggPortListPorts=_AggPortListPorts_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1,1,3),_AggPortListPorts_Type())
aggPortListPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:aggPortListPorts.setStatus(_F)
class _AggRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('srcMAC',1),('destMAC',2),('srcXORDestMAC',3),('srcIP',4),('destIP',5),('srcXORDestIP',6)))
_AggRule_Type.__name__=_C
_AggRule_Object=MibTableColumn
aggRule=_AggRule_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1,1,4),_AggRule_Type())
aggRule.setMaxAccess(_B)
if mibBuilder.loadTexts:aggRule.setStatus(_F)
_AggRowstatus_Type=TruthValue
_AggRowstatus_Object=MibTableColumn
aggRowstatus=_AggRowstatus_Object((1,3,6,1,4,1,13464,1,2,2,1,3,1,1,5),_AggRowstatus_Type())
aggRowstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aggRowstatus.setStatus(_F)
_GbnDeviceSwitchL3_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchL3=_GbnDeviceSwitchL3_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,4))
_L3Table_Object=MibTable
l3Table=_L3Table_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1))
if mibBuilder.loadTexts:l3Table.setStatus(_A)
_L3Entry_Object=MibTableRow
l3Entry=_L3Entry_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1))
l3Entry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:l3Entry.setStatus(_A)
_L3IpAddress_Type=IpAddress
_L3IpAddress_Object=MibTableColumn
l3IpAddress=_L3IpAddress_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1,1),_L3IpAddress_Type())
l3IpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:l3IpAddress.setStatus(_A)
_L3NextHopMacAddress_Type=MacAddress
_L3NextHopMacAddress_Object=MibTableColumn
l3NextHopMacAddress=_L3NextHopMacAddress_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1,2),_L3NextHopMacAddress_Type())
l3NextHopMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:l3NextHopMacAddress.setStatus(_A)
_L3Vlan_Type=VlanIndex
_L3Vlan_Object=MibTableColumn
l3Vlan=_L3Vlan_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1,3),_L3Vlan_Type())
l3Vlan.setMaxAccess(_D)
if mibBuilder.loadTexts:l3Vlan.setStatus(_A)
_L3Port_Type=Integer32
_L3Port_Object=MibTableColumn
l3Port=_L3Port_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1,4),_L3Port_Type())
l3Port.setMaxAccess(_D)
if mibBuilder.loadTexts:l3Port.setStatus(_A)
_L3CreateTime_Type=DateAndTime
_L3CreateTime_Object=MibTableColumn
l3CreateTime=_L3CreateTime_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1,5),_L3CreateTime_Type())
l3CreateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l3CreateTime.setStatus(_A)
_L3UpdateTime_Type=DateAndTime
_L3UpdateTime_Object=MibTableColumn
l3UpdateTime=_L3UpdateTime_Object((1,3,6,1,4,1,13464,1,2,2,1,4,1,1,6),_L3UpdateTime_Type())
l3UpdateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l3UpdateTime.setStatus(_A)
_GbnDeviceSwitchLoopTest_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchLoopTest=_GbnDeviceSwitchLoopTest_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,5))
class _LoopTestPortno_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_LoopTestPortno_Type.__name__=_H
_LoopTestPortno_Object=MibScalar
loopTestPortno=_LoopTestPortno_Object((1,3,6,1,4,1,13464,1,2,2,1,5,1),_LoopTestPortno_Type())
loopTestPortno.setMaxAccess(_B)
if mibBuilder.loadTexts:loopTestPortno.setStatus(_A)
class _LoopTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noop',1),('local',2),('remote',3),('other',4)))
_LoopTestType_Type.__name__=_C
_LoopTestType_Object=MibScalar
loopTestType=_LoopTestType_Object((1,3,6,1,4,1,13464,1,2,2,1,5,2),_LoopTestType_Type())
loopTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:loopTestType.setStatus(_A)
class _LoopTestSuccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_LoopTestSuccess_Type.__name__=_H
_LoopTestSuccess_Object=MibScalar
loopTestSuccess=_LoopTestSuccess_Object((1,3,6,1,4,1,13464,1,2,2,1,5,3),_LoopTestSuccess_Type())
loopTestSuccess.setMaxAccess(_D)
if mibBuilder.loadTexts:loopTestSuccess.setStatus(_A)
_GbnDeviceSwitchSRM_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchSRM=_GbnDeviceSwitchSRM_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,6))
class _SrmHardwareEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SrmHardwareEnable_Type.__name__=_C
_SrmHardwareEnable_Object=MibScalar
srmHardwareEnable=_SrmHardwareEnable_Object((1,3,6,1,4,1,13464,1,2,2,1,6,1),_SrmHardwareEnable_Type())
srmHardwareEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:srmHardwareEnable.setStatus(_A)
class _SrmHardwareDEFCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SrmHardwareDEFCPU_Type.__name__=_C
_SrmHardwareDEFCPU_Object=MibScalar
srmHardwareDEFCPU=_SrmHardwareDEFCPU_Object((1,3,6,1,4,1,13464,1,2,2,1,6,2),_SrmHardwareDEFCPU_Type())
srmHardwareDEFCPU.setMaxAccess(_B)
if mibBuilder.loadTexts:srmHardwareDEFCPU.setStatus(_A)
_GbnDeviceSwitchFlowAlarm_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchFlowAlarm=_GbnDeviceSwitchFlowAlarm_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,7))
_PortFlowAlarmTable_Object=MibTable
portFlowAlarmTable=_PortFlowAlarmTable_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1))
if mibBuilder.loadTexts:portFlowAlarmTable.setStatus(_A)
_PortFlowAlarmEntry_Object=MibTableRow
portFlowAlarmEntry=_PortFlowAlarmEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1,1))
portFlowAlarmEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:portFlowAlarmEntry.setStatus(_A)
class _PortFlowAlarmPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_PortFlowAlarmPort_Type.__name__=_C
_PortFlowAlarmPort_Object=MibTableColumn
portFlowAlarmPort=_PortFlowAlarmPort_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1,1,1),_PortFlowAlarmPort_Type())
portFlowAlarmPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:portFlowAlarmPort.setStatus(_A)
_PortFlowAlarmEnable_Type=TruthValue
_PortFlowAlarmEnable_Object=MibTableColumn
portFlowAlarmEnable=_PortFlowAlarmEnable_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1,1,2),_PortFlowAlarmEnable_Type())
portFlowAlarmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowAlarmEnable.setStatus(_A)
_PortFlowAlarmExceedStatus_Type=TruthValue
_PortFlowAlarmExceedStatus_Object=MibTableColumn
portFlowAlarmExceedStatus=_PortFlowAlarmExceedStatus_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1,1,3),_PortFlowAlarmExceedStatus_Type())
portFlowAlarmExceedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portFlowAlarmExceedStatus.setStatus(_A)
_PortFlowAlarmExceedThreshold_Type=Integer32
_PortFlowAlarmExceedThreshold_Object=MibTableColumn
portFlowAlarmExceedThreshold=_PortFlowAlarmExceedThreshold_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1,1,4),_PortFlowAlarmExceedThreshold_Type())
portFlowAlarmExceedThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowAlarmExceedThreshold.setStatus(_A)
_PortFlowAlarmNormalThreshold_Type=Integer32
_PortFlowAlarmNormalThreshold_Object=MibTableColumn
portFlowAlarmNormalThreshold=_PortFlowAlarmNormalThreshold_Object((1,3,6,1,4,1,13464,1,2,2,1,7,1,1,5),_PortFlowAlarmNormalThreshold_Type())
portFlowAlarmNormalThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowAlarmNormalThreshold.setStatus(_A)
_PortFlowAlarmGlobalEnable_Type=TruthValue
_PortFlowAlarmGlobalEnable_Object=MibScalar
portFlowAlarmGlobalEnable=_PortFlowAlarmGlobalEnable_Object((1,3,6,1,4,1,13464,1,2,2,1,7,2),_PortFlowAlarmGlobalEnable_Type())
portFlowAlarmGlobalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowAlarmGlobalEnable.setStatus(_A)
_PortFlowAlarmTrap_ObjectIdentity=ObjectIdentity
portFlowAlarmTrap=_PortFlowAlarmTrap_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,7,5))
_GbnDeviceSwitchQueneScheduer_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchQueneScheduer=_GbnDeviceSwitchQueneScheduer_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,8))
_QosQueueSchedulerGroup_ObjectIdentity=ObjectIdentity
qosQueueSchedulerGroup=_QosQueueSchedulerGroup_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,8,1))
class _QosWrrQueue1Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue1Weight_Type.__name__=_C
_QosWrrQueue1Weight_Object=MibScalar
qosWrrQueue1Weight=_QosWrrQueue1Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,1),_QosWrrQueue1Weight_Type())
qosWrrQueue1Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue1Weight.setStatus(_A)
class _QosWrrQueue2Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue2Weight_Type.__name__=_C
_QosWrrQueue2Weight_Object=MibScalar
qosWrrQueue2Weight=_QosWrrQueue2Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,2),_QosWrrQueue2Weight_Type())
qosWrrQueue2Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue2Weight.setStatus(_A)
class _QosWrrQueue3Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue3Weight_Type.__name__=_C
_QosWrrQueue3Weight_Object=MibScalar
qosWrrQueue3Weight=_QosWrrQueue3Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,3),_QosWrrQueue3Weight_Type())
qosWrrQueue3Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue3Weight.setStatus(_A)
class _QosWrrQueue4Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue4Weight_Type.__name__=_C
_QosWrrQueue4Weight_Object=MibScalar
qosWrrQueue4Weight=_QosWrrQueue4Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,4),_QosWrrQueue4Weight_Type())
qosWrrQueue4Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue4Weight.setStatus(_A)
class _QosWrrMaxDelayValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QosWrrMaxDelayValue_Type.__name__=_C
_QosWrrMaxDelayValue_Object=MibScalar
qosWrrMaxDelayValue=_QosWrrMaxDelayValue_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,5),_QosWrrMaxDelayValue_Type())
qosWrrMaxDelayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrMaxDelayValue.setStatus(_A)
class _QosQueueSchedulerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strictPriority',1),('wrr',2)))
_QosQueueSchedulerMode_Type.__name__=_C
_QosQueueSchedulerMode_Object=MibScalar
qosQueueSchedulerMode=_QosQueueSchedulerMode_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,6),_QosQueueSchedulerMode_Type())
qosQueueSchedulerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:qosQueueSchedulerMode.setStatus(_A)
class _QosWrrQueue5Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue5Weight_Type.__name__=_C
_QosWrrQueue5Weight_Object=MibScalar
qosWrrQueue5Weight=_QosWrrQueue5Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,7),_QosWrrQueue5Weight_Type())
qosWrrQueue5Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue5Weight.setStatus(_A)
class _QosWrrQueue6Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue6Weight_Type.__name__=_C
_QosWrrQueue6Weight_Object=MibScalar
qosWrrQueue6Weight=_QosWrrQueue6Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,8),_QosWrrQueue6Weight_Type())
qosWrrQueue6Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue6Weight.setStatus(_A)
class _QosWrrQueue7Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue7Weight_Type.__name__=_C
_QosWrrQueue7Weight_Object=MibScalar
qosWrrQueue7Weight=_QosWrrQueue7Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,9),_QosWrrQueue7Weight_Type())
qosWrrQueue7Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue7Weight.setStatus(_A)
class _QosWrrQueue8Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosWrrQueue8Weight_Type.__name__=_C
_QosWrrQueue8Weight_Object=MibScalar
qosWrrQueue8Weight=_QosWrrQueue8Weight_Object((1,3,6,1,4,1,13464,1,2,2,1,8,1,10),_QosWrrQueue8Weight_Type())
qosWrrQueue8Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWrrQueue8Weight.setStatus(_A)
_QosPriorityRemapGroup_ObjectIdentity=ObjectIdentity
qosPriorityRemapGroup=_QosPriorityRemapGroup_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,8,2))
class _QosPriority0Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority0Remap_Type.__name__=_C
_QosPriority0Remap_Object=MibScalar
qosPriority0Remap=_QosPriority0Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,1),_QosPriority0Remap_Type())
qosPriority0Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority0Remap.setStatus(_A)
class _QosPriority1Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority1Remap_Type.__name__=_C
_QosPriority1Remap_Object=MibScalar
qosPriority1Remap=_QosPriority1Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,2),_QosPriority1Remap_Type())
qosPriority1Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority1Remap.setStatus(_A)
class _QosPriority2Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority2Remap_Type.__name__=_C
_QosPriority2Remap_Object=MibScalar
qosPriority2Remap=_QosPriority2Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,3),_QosPriority2Remap_Type())
qosPriority2Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority2Remap.setStatus(_A)
class _QosPriority3Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority3Remap_Type.__name__=_C
_QosPriority3Remap_Object=MibScalar
qosPriority3Remap=_QosPriority3Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,4),_QosPriority3Remap_Type())
qosPriority3Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority3Remap.setStatus(_A)
class _QosPriority4Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority4Remap_Type.__name__=_C
_QosPriority4Remap_Object=MibScalar
qosPriority4Remap=_QosPriority4Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,5),_QosPriority4Remap_Type())
qosPriority4Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority4Remap.setStatus(_A)
class _QosPriority5Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority5Remap_Type.__name__=_C
_QosPriority5Remap_Object=MibScalar
qosPriority5Remap=_QosPriority5Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,6),_QosPriority5Remap_Type())
qosPriority5Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority5Remap.setStatus(_A)
class _QosPriority6Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority6Remap_Type.__name__=_C
_QosPriority6Remap_Object=MibScalar
qosPriority6Remap=_QosPriority6Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,7),_QosPriority6Remap_Type())
qosPriority6Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority6Remap.setStatus(_A)
class _QosPriority7Remap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPriority7Remap_Type.__name__=_C
_QosPriority7Remap_Object=MibScalar
qosPriority7Remap=_QosPriority7Remap_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,8),_QosPriority7Remap_Type())
qosPriority7Remap.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriority7Remap.setStatus(_A)
class _QosPriorityRemapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_QosPriorityRemapStatus_Type.__name__=_C
_QosPriorityRemapStatus_Object=MibScalar
qosPriorityRemapStatus=_QosPriorityRemapStatus_Object((1,3,6,1,4,1,13464,1,2,2,1,8,2,9),_QosPriorityRemapStatus_Type())
qosPriorityRemapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityRemapStatus.setStatus(_A)
_GbnDeviceSwitchLineRate_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchLineRate=_GbnDeviceSwitchLineRate_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,9))
_QosLineRateTable_Object=MibTable
qosLineRateTable=_QosLineRateTable_Object((1,3,6,1,4,1,13464,1,2,2,1,9,1))
if mibBuilder.loadTexts:qosLineRateTable.setStatus(_A)
_QosLineRateEntry_Object=MibTableRow
qosLineRateEntry=_QosLineRateEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,9,1,1))
qosLineRateEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:qosLineRateEntry.setStatus(_A)
class _QosLineRateInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_QosLineRateInterface_Type.__name__=_C
_QosLineRateInterface_Object=MibTableColumn
qosLineRateInterface=_QosLineRateInterface_Object((1,3,6,1,4,1,13464,1,2,2,1,9,1,1,1),_QosLineRateInterface_Type())
qosLineRateInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:qosLineRateInterface.setStatus(_A)
class _QosLineRateTargetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosLineRateTargetRate_Type.__name__=_C
_QosLineRateTargetRate_Object=MibTableColumn
qosLineRateTargetRate=_QosLineRateTargetRate_Object((1,3,6,1,4,1,13464,1,2,2,1,9,1,1,2),_QosLineRateTargetRate_Type())
qosLineRateTargetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qosLineRateTargetRate.setStatus(_A)
_GbnDeviceSwitchPortIsolation_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchPortIsolation=_GbnDeviceSwitchPortIsolation_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,10))
_PortIsolationGroup_ObjectIdentity=ObjectIdentity
portIsolationGroup=_PortIsolationGroup_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,10,1))
_PortIsolationDownLinkPorts_Type=PortList
_PortIsolationDownLinkPorts_Object=MibScalar
portIsolationDownLinkPorts=_PortIsolationDownLinkPorts_Object((1,3,6,1,4,1,13464,1,2,2,1,10,1,1),_PortIsolationDownLinkPorts_Type())
portIsolationDownLinkPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:portIsolationDownLinkPorts.setStatus(_A)
_GbnDeviceSwitchStormControl_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchStormControl=_GbnDeviceSwitchStormControl_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,11))
_StormControlTable_Object=MibTable
stormControlTable=_StormControlTable_Object((1,3,6,1,4,1,13464,1,2,2,1,11,1))
if mibBuilder.loadTexts:stormControlTable.setStatus(_A)
_StormControlEntry_Object=MibTableRow
stormControlEntry=_StormControlEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,11,1,1))
stormControlEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:stormControlEntry.setStatus(_A)
class _StormControlInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_StormControlInterface_Type.__name__=_C
_StormControlInterface_Object=MibTableColumn
stormControlInterface=_StormControlInterface_Object((1,3,6,1,4,1,13464,1,2,2,1,11,1,1,1),_StormControlInterface_Type())
stormControlInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:stormControlInterface.setStatus(_A)
_StormControlType_Type=Integer32
_StormControlType_Object=MibTableColumn
stormControlType=_StormControlType_Object((1,3,6,1,4,1,13464,1,2,2,1,11,1,1,2),_StormControlType_Type())
stormControlType.setMaxAccess(_D)
if mibBuilder.loadTexts:stormControlType.setStatus(_A)
class _StormControlTargetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_StormControlTargetRate_Type.__name__=_C
_StormControlTargetRate_Object=MibTableColumn
stormControlTargetRate=_StormControlTargetRate_Object((1,3,6,1,4,1,13464,1,2,2,1,11,1,1,3),_StormControlTargetRate_Type())
stormControlTargetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:stormControlTargetRate.setStatus(_A)
_StormControlRowStatus_Type=RowStatus
_StormControlRowStatus_Object=MibTableColumn
stormControlRowStatus=_StormControlRowStatus_Object((1,3,6,1,4,1,13464,1,2,2,1,11,1,1,4),_StormControlRowStatus_Type())
stormControlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:stormControlRowStatus.setStatus(_A)
_GbnDeviceSwitchBandWidth_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchBandWidth=_GbnDeviceSwitchBandWidth_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,12))
_BandwidthcontrolTable_Object=MibTable
bandwidthcontrolTable=_BandwidthcontrolTable_Object((1,3,6,1,4,1,13464,1,2,2,1,12,1))
if mibBuilder.loadTexts:bandwidthcontrolTable.setStatus(_A)
_BandwidthcontrolEntry_Object=MibTableRow
bandwidthcontrolEntry=_BandwidthcontrolEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,12,1,1))
bandwidthcontrolEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:bandwidthcontrolEntry.setStatus(_A)
class _ControlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_ControlPort_Type.__name__=_C
_ControlPort_Object=MibTableColumn
controlPort=_ControlPort_Object((1,3,6,1,4,1,13464,1,2,2,1,12,1,1,1),_ControlPort_Type())
controlPort.setMaxAccess(_D)
if mibBuilder.loadTexts:controlPort.setStatus(_A)
class _PortEgressBandwidthcontrol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024000))
_PortEgressBandwidthcontrol_Type.__name__=_C
_PortEgressBandwidthcontrol_Object=MibTableColumn
portEgressBandwidthcontrol=_PortEgressBandwidthcontrol_Object((1,3,6,1,4,1,13464,1,2,2,1,12,1,1,2),_PortEgressBandwidthcontrol_Type())
portEgressBandwidthcontrol.setMaxAccess(_B)
if mibBuilder.loadTexts:portEgressBandwidthcontrol.setStatus(_A)
class _PortIngressBandwidthcontrol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024000))
_PortIngressBandwidthcontrol_Type.__name__=_C
_PortIngressBandwidthcontrol_Object=MibTableColumn
portIngressBandwidthcontrol=_PortIngressBandwidthcontrol_Object((1,3,6,1,4,1,13464,1,2,2,1,12,1,1,3),_PortIngressBandwidthcontrol_Type())
portIngressBandwidthcontrol.setMaxAccess(_B)
if mibBuilder.loadTexts:portIngressBandwidthcontrol.setStatus(_A)
_GbnDeviceSwitchNewStormControl_ObjectIdentity=ObjectIdentity
gbnDeviceSwitchNewStormControl=_GbnDeviceSwitchNewStormControl_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,1,13))
class _NewStormControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),('broadcast',1),('ipmulticast',2),('broadcast-ipmulticast',3),('dlf',4),('broadcast-dlf',5),('ipmulticast-dlf',6),('broadcast-ipmulticast-dlf',7)))
_NewStormControlType_Type.__name__=_C
_NewStormControlType_Object=MibScalar
newStormControlType=_NewStormControlType_Object((1,3,6,1,4,1,13464,1,2,2,1,13,1),_NewStormControlType_Type())
newStormControlType.setMaxAccess(_B)
if mibBuilder.loadTexts:newStormControlType.setStatus(_A)
class _NewStormControlTargetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,12,25,50)));namedValues=NamedValues(*(('rate-one-sixteenth',6),('rate-one-eighth',12),('rate-one-fourth',25),('rate-one-half',50)))
_NewStormControlTargetRate_Type.__name__=_C
_NewStormControlTargetRate_Object=MibScalar
newStormControlTargetRate=_NewStormControlTargetRate_Object((1,3,6,1,4,1,13464,1,2,2,1,13,2),_NewStormControlTargetRate_Type())
newStormControlTargetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:newStormControlTargetRate.setStatus(_A)
_NewStormControlTable_Object=MibTable
newStormControlTable=_NewStormControlTable_Object((1,3,6,1,4,1,13464,1,2,2,1,13,3))
if mibBuilder.loadTexts:newStormControlTable.setStatus(_A)
_NewStormControlEntry_Object=MibTableRow
newStormControlEntry=_NewStormControlEntry_Object((1,3,6,1,4,1,13464,1,2,2,1,13,3,1))
newStormControlEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:newStormControlEntry.setStatus(_A)
class _NewStormControlInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_NewStormControlInterface_Type.__name__=_C
_NewStormControlInterface_Object=MibTableColumn
newStormControlInterface=_NewStormControlInterface_Object((1,3,6,1,4,1,13464,1,2,2,1,13,3,1,1),_NewStormControlInterface_Type())
newStormControlInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:newStormControlInterface.setStatus(_A)
class _NewStormControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_NewStormControlStatus_Type.__name__=_C
_NewStormControlStatus_Object=MibTableColumn
newStormControlStatus=_NewStormControlStatus_Object((1,3,6,1,4,1,13464,1,2,2,1,13,3,1,2),_NewStormControlStatus_Type())
newStormControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newStormControlStatus.setStatus(_A)
portFlowAlarmExceedTrap=NotificationType((1,3,6,1,4,1,13464,1,2,2,1,7,5,1))
portFlowAlarmExceedTrap.setObjects((_E,_G))
if mibBuilder.loadTexts:portFlowAlarmExceedTrap.setStatus(_A)
portFlowAlarmNormalTrap=NotificationType((1,3,6,1,4,1,13464,1,2,2,1,7,5,2))
portFlowAlarmNormalTrap.setObjects((_E,_G))
if mibBuilder.loadTexts:portFlowAlarmNormalTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'gbnDeviceSwitch':gbnDeviceSwitch,'gbnDeviceSwitchMirror':gbnDeviceSwitchMirror,'mirroringPort':mirroringPort,'mirroredEgrPort':mirroredEgrPort,'mirroredIgrPort':mirroredIgrPort,'gbnDeviceSwitchPort':gbnDeviceSwitchPort,'portTypeTable':portTypeTable,'portTypeEntry':portTypeEntry,_I:portNumber,'portType':portType,'gbnDeviceSwitchAggregation':gbnDeviceSwitchAggregation,'aggTable':aggTable,'aggEntry':aggEntry,_J:aggUnit,_K:aggPort,'aggPortListPorts':aggPortListPorts,'aggRule':aggRule,'aggRowstatus':aggRowstatus,'gbnDeviceSwitchL3':gbnDeviceSwitchL3,'l3Table':l3Table,'l3Entry':l3Entry,_L:l3IpAddress,'l3NextHopMacAddress':l3NextHopMacAddress,'l3Vlan':l3Vlan,'l3Port':l3Port,'l3CreateTime':l3CreateTime,'l3UpdateTime':l3UpdateTime,'gbnDeviceSwitchLoopTest':gbnDeviceSwitchLoopTest,'loopTestPortno':loopTestPortno,'loopTestType':loopTestType,'loopTestSuccess':loopTestSuccess,'gbnDeviceSwitchSRM':gbnDeviceSwitchSRM,'srmHardwareEnable':srmHardwareEnable,'srmHardwareDEFCPU':srmHardwareDEFCPU,'gbnDeviceSwitchFlowAlarm':gbnDeviceSwitchFlowAlarm,'portFlowAlarmTable':portFlowAlarmTable,'portFlowAlarmEntry':portFlowAlarmEntry,_G:portFlowAlarmPort,'portFlowAlarmEnable':portFlowAlarmEnable,'portFlowAlarmExceedStatus':portFlowAlarmExceedStatus,'portFlowAlarmExceedThreshold':portFlowAlarmExceedThreshold,'portFlowAlarmNormalThreshold':portFlowAlarmNormalThreshold,'portFlowAlarmGlobalEnable':portFlowAlarmGlobalEnable,'portFlowAlarmTrap':portFlowAlarmTrap,'portFlowAlarmExceedTrap':portFlowAlarmExceedTrap,'portFlowAlarmNormalTrap':portFlowAlarmNormalTrap,'gbnDeviceSwitchQueneScheduer':gbnDeviceSwitchQueneScheduer,'qosQueueSchedulerGroup':qosQueueSchedulerGroup,'qosWrrQueue1Weight':qosWrrQueue1Weight,'qosWrrQueue2Weight':qosWrrQueue2Weight,'qosWrrQueue3Weight':qosWrrQueue3Weight,'qosWrrQueue4Weight':qosWrrQueue4Weight,'qosWrrMaxDelayValue':qosWrrMaxDelayValue,'qosQueueSchedulerMode':qosQueueSchedulerMode,'qosWrrQueue5Weight':qosWrrQueue5Weight,'qosWrrQueue6Weight':qosWrrQueue6Weight,'qosWrrQueue7Weight':qosWrrQueue7Weight,'qosWrrQueue8Weight':qosWrrQueue8Weight,'qosPriorityRemapGroup':qosPriorityRemapGroup,'qosPriority0Remap':qosPriority0Remap,'qosPriority1Remap':qosPriority1Remap,'qosPriority2Remap':qosPriority2Remap,'qosPriority3Remap':qosPriority3Remap,'qosPriority4Remap':qosPriority4Remap,'qosPriority5Remap':qosPriority5Remap,'qosPriority6Remap':qosPriority6Remap,'qosPriority7Remap':qosPriority7Remap,'qosPriorityRemapStatus':qosPriorityRemapStatus,'gbnDeviceSwitchLineRate':gbnDeviceSwitchLineRate,'qosLineRateTable':qosLineRateTable,'qosLineRateEntry':qosLineRateEntry,_Q:qosLineRateInterface,'qosLineRateTargetRate':qosLineRateTargetRate,'gbnDeviceSwitchPortIsolation':gbnDeviceSwitchPortIsolation,'portIsolationGroup':portIsolationGroup,'portIsolationDownLinkPorts':portIsolationDownLinkPorts,'gbnDeviceSwitchStormControl':gbnDeviceSwitchStormControl,'stormControlTable':stormControlTable,'stormControlEntry':stormControlEntry,_R:stormControlInterface,_S:stormControlType,'stormControlTargetRate':stormControlTargetRate,'stormControlRowStatus':stormControlRowStatus,'gbnDeviceSwitchBandWidth':gbnDeviceSwitchBandWidth,'bandwidthcontrolTable':bandwidthcontrolTable,'bandwidthcontrolEntry':bandwidthcontrolEntry,_T:controlPort,'portEgressBandwidthcontrol':portEgressBandwidthcontrol,'portIngressBandwidthcontrol':portIngressBandwidthcontrol,'gbnDeviceSwitchNewStormControl':gbnDeviceSwitchNewStormControl,'newStormControlType':newStormControlType,'newStormControlTargetRate':newStormControlTargetRate,'newStormControlTable':newStormControlTable,'newStormControlEntry':newStormControlEntry,_U:newStormControlInterface,'newStormControlStatus':newStormControlStatus})