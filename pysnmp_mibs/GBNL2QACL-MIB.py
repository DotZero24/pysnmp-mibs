_x='qosTrafficInsertVlanIndex'
_w='qosTrafficRewriteVlanIndex'
_v='stormControlType'
_u='stormControlInterface'
_t='qosTrafficCopyToCpuIndex'
_s='qosLineRateInterface'
_r='qosTrafficStatisticsIndex'
_q='qosTrafficRedirectIndex'
_p='qosTrafficPriorityIndex'
_o='qosRateLimitIndex'
_n='qosMirrorToIndex'
_m='aclActiveIndex'
_l='aclTimeRangePeriodEndMin'
_k='aclTimeRangePeriodEndHour'
_j='aclTimeRangePeriodEndWeekDay'
_i='aclTimeRangePeriodStartMin'
_h='aclTimeRangePeriodStartHour'
_g='aclTimeRangePeriodStartWeekDay'
_f='aclTimeRangePeriodName'
_e='aclTimeRangeAbsoluteEndTime'
_d='aclTimeRangeAbsoluteStartTime'
_c='aclTimeRangeAbsoluteName'
_b='aclTimeRangeName'
_a='aclNamedUserSubNum'
_Z='aclNamedUserName'
_Y='aclNamedLnkSubNum'
_X='aclNamedLnkName'
_W='aclNamedExdSubNum'
_V='aclNamedExdName'
_U='aclNamedStdSubNum'
_T='aclNamedStdName'
_S='aclNamedName'
_R='aclNumUserSubNum'
_Q='aclNumUserNum'
_P='aclNumLnkSubNum'
_O='aclNumLnkNum'
_N='aclNumExdSubNum'
_M='aclNumExdNum'
_L='aclNumStdSubNum'
_K='aclNumStdNum'
_J='config'
_I='aclNumNumber'
_H='TruthValue'
_G='read-create'
_F='GBNL2QACL-MIB'
_E='OctetString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnL2,=mibBuilder.importSymbols('GREENTECH-MASTER-MIB','gbnL2')
TOSType,=mibBuilder.importSymbols('OSPF-MIB','TOSType')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
gbnL2QACL=ModuleIdentity((1,3,6,1,4,1,13464,1,2,4,4))
if mibBuilder.loadTexts:gbnL2QACL.setRevisions(('1903-09-26 00:01',))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
class Action(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101)));namedValues=NamedValues(*(('deny',100),('permit',101)))
class Dscp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class AclType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('standard',1),('extend',2),('link',3),('user',4)))
class PacketFlowType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('multicast',2),('unicast',3)))
_QosQueueSchedulerGroup_ObjectIdentity=ObjectIdentity
qosQueueSchedulerGroup=_QosQueueSchedulerGroup_ObjectIdentity((1,3,6,1,4,1,13464,1,2,4,4,1))
class _QosWrrQueue1Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue1Weight_Type.__name__=_B
_QosWrrQueue1Weight_Object=MibScalar
qosWrrQueue1Weight=_QosWrrQueue1Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,1),_QosWrrQueue1Weight_Type())
qosWrrQueue1Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue1Weight.setStatus(_A)
class _QosWrrQueue2Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue2Weight_Type.__name__=_B
_QosWrrQueue2Weight_Object=MibScalar
qosWrrQueue2Weight=_QosWrrQueue2Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,2),_QosWrrQueue2Weight_Type())
qosWrrQueue2Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue2Weight.setStatus(_A)
class _QosWrrQueue3Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue3Weight_Type.__name__=_B
_QosWrrQueue3Weight_Object=MibScalar
qosWrrQueue3Weight=_QosWrrQueue3Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,3),_QosWrrQueue3Weight_Type())
qosWrrQueue3Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue3Weight.setStatus(_A)
class _QosWrrQueue4Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue4Weight_Type.__name__=_B
_QosWrrQueue4Weight_Object=MibScalar
qosWrrQueue4Weight=_QosWrrQueue4Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,4),_QosWrrQueue4Weight_Type())
qosWrrQueue4Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue4Weight.setStatus(_A)
class _QosWrrMaxDelayValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QosWrrMaxDelayValue_Type.__name__=_B
_QosWrrMaxDelayValue_Object=MibScalar
qosWrrMaxDelayValue=_QosWrrMaxDelayValue_Object((1,3,6,1,4,1,13464,1,2,4,4,1,5),_QosWrrMaxDelayValue_Type())
qosWrrMaxDelayValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrMaxDelayValue.setStatus(_A)
class _QosQueueSchedulerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('strictPriority',1),('wrr',2),('wrrMaxDelay',3)))
_QosQueueSchedulerMode_Type.__name__=_B
_QosQueueSchedulerMode_Object=MibScalar
qosQueueSchedulerMode=_QosQueueSchedulerMode_Object((1,3,6,1,4,1,13464,1,2,4,4,1,6),_QosQueueSchedulerMode_Type())
qosQueueSchedulerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qosQueueSchedulerMode.setStatus(_A)
class _QosWrrQueue5Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue5Weight_Type.__name__=_B
_QosWrrQueue5Weight_Object=MibScalar
qosWrrQueue5Weight=_QosWrrQueue5Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,7),_QosWrrQueue5Weight_Type())
qosWrrQueue5Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue5Weight.setStatus(_A)
class _QosWrrQueue6Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue6Weight_Type.__name__=_B
_QosWrrQueue6Weight_Object=MibScalar
qosWrrQueue6Weight=_QosWrrQueue6Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,8),_QosWrrQueue6Weight_Type())
qosWrrQueue6Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue6Weight.setStatus(_A)
class _QosWrrQueue7Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue7Weight_Type.__name__=_B
_QosWrrQueue7Weight_Object=MibScalar
qosWrrQueue7Weight=_QosWrrQueue7Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,9),_QosWrrQueue7Weight_Type())
qosWrrQueue7Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue7Weight.setStatus(_A)
class _QosWrrQueue8Weight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,97))
_QosWrrQueue8Weight_Type.__name__=_B
_QosWrrQueue8Weight_Object=MibScalar
qosWrrQueue8Weight=_QosWrrQueue8Weight_Object((1,3,6,1,4,1,13464,1,2,4,4,1,10),_QosWrrQueue8Weight_Type())
qosWrrQueue8Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWrrQueue8Weight.setStatus(_A)
_AclNumTable_Object=MibTable
aclNumTable=_AclNumTable_Object((1,3,6,1,4,1,13464,1,2,4,4,2))
if mibBuilder.loadTexts:aclNumTable.setStatus(_A)
_AclNumEntry_Object=MibTableRow
aclNumEntry=_AclNumEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,2,1))
aclNumEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:aclNumEntry.setStatus(_A)
_AclNumNumber_Type=Integer32
_AclNumNumber_Object=MibTableColumn
aclNumNumber=_AclNumNumber_Object((1,3,6,1,4,1,13464,1,2,4,4,2,1,1),_AclNumNumber_Type())
aclNumNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumNumber.setStatus(_A)
_AclNumType_Type=AclType
_AclNumType_Object=MibTableColumn
aclNumType=_AclNumType_Object((1,3,6,1,4,1,13464,1,2,4,4,2,1,2),_AclNumType_Type())
aclNumType.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumType.setStatus(_A)
class _AclNumMatchOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('auto',1)))
_AclNumMatchOrder_Type.__name__=_B
_AclNumMatchOrder_Object=MibTableColumn
aclNumMatchOrder=_AclNumMatchOrder_Object((1,3,6,1,4,1,13464,1,2,4,4,2,1,3),_AclNumMatchOrder_Type())
aclNumMatchOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumMatchOrder.setStatus(_A)
_AclNumTotleSubitems_Type=Integer32
_AclNumTotleSubitems_Object=MibTableColumn
aclNumTotleSubitems=_AclNumTotleSubitems_Object((1,3,6,1,4,1,13464,1,2,4,4,2,1,4),_AclNumTotleSubitems_Type())
aclNumTotleSubitems.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumTotleSubitems.setStatus(_A)
_AclNumRowStatus_Type=RowStatus
_AclNumRowStatus_Object=MibTableColumn
aclNumRowStatus=_AclNumRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,2,1,5),_AclNumRowStatus_Type())
aclNumRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumRowStatus.setStatus(_A)
_AclNumStdSubitemTable_Object=MibTable
aclNumStdSubitemTable=_AclNumStdSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,3))
if mibBuilder.loadTexts:aclNumStdSubitemTable.setStatus(_A)
_AclNumStdSubitemEntry_Object=MibTableRow
aclNumStdSubitemEntry=_AclNumStdSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1))
aclNumStdSubitemEntry.setIndexNames((0,_F,_K),(0,_F,_L))
if mibBuilder.loadTexts:aclNumStdSubitemEntry.setStatus(_A)
class _AclNumStdNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_AclNumStdNum_Type.__name__=_B
_AclNumStdNum_Object=MibTableColumn
aclNumStdNum=_AclNumStdNum_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,1),_AclNumStdNum_Type())
aclNumStdNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumStdNum.setStatus(_A)
class _AclNumStdSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNumStdSubNum_Type.__name__=_B
_AclNumStdSubNum_Object=MibTableColumn
aclNumStdSubNum=_AclNumStdSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,2),_AclNumStdSubNum_Type())
aclNumStdSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumStdSubNum.setStatus(_A)
_AclNumStdSubitemAdminStatus_Type=AdminStatus
_AclNumStdSubitemAdminStatus_Object=MibTableColumn
aclNumStdSubitemAdminStatus=_AclNumStdSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,3),_AclNumStdSubitemAdminStatus_Type())
aclNumStdSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumStdSubitemAdminStatus.setStatus(_A)
_AclNumStdSubitemAction_Type=Action
_AclNumStdSubitemAction_Object=MibTableColumn
aclNumStdSubitemAction=_AclNumStdSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,4),_AclNumStdSubitemAction_Type())
aclNumStdSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumStdSubitemAction.setStatus(_A)
_AclNumStdSubitemSrcAddr_Type=IpAddress
_AclNumStdSubitemSrcAddr_Object=MibTableColumn
aclNumStdSubitemSrcAddr=_AclNumStdSubitemSrcAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,5),_AclNumStdSubitemSrcAddr_Type())
aclNumStdSubitemSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumStdSubitemSrcAddr.setStatus(_A)
_AclNumStdSubitemSrcAddrWldmsk_Type=IpAddress
_AclNumStdSubitemSrcAddrWldmsk_Object=MibTableColumn
aclNumStdSubitemSrcAddrWldmsk=_AclNumStdSubitemSrcAddrWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,6),_AclNumStdSubitemSrcAddrWldmsk_Type())
aclNumStdSubitemSrcAddrWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumStdSubitemSrcAddrWldmsk.setStatus(_A)
class _AclNumStdFragments_Type(TruthValue):defaultValue=2
_AclNumStdFragments_Type.__name__=_H
_AclNumStdFragments_Object=MibTableColumn
aclNumStdFragments=_AclNumStdFragments_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,7),_AclNumStdFragments_Type())
aclNumStdFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumStdFragments.setStatus(_A)
class _AclNumStdTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNumStdTimeRange_Type.__name__=_E
_AclNumStdTimeRange_Object=MibTableColumn
aclNumStdTimeRange=_AclNumStdTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,8),_AclNumStdTimeRange_Type())
aclNumStdTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumStdTimeRange.setStatus(_A)
_AclNumStdSubitemRowStatus_Type=RowStatus
_AclNumStdSubitemRowStatus_Object=MibTableColumn
aclNumStdSubitemRowStatus=_AclNumStdSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,3,1,9),_AclNumStdSubitemRowStatus_Type())
aclNumStdSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumStdSubitemRowStatus.setStatus(_A)
_AclNumExdSubitemTable_Object=MibTable
aclNumExdSubitemTable=_AclNumExdSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,4))
if mibBuilder.loadTexts:aclNumExdSubitemTable.setStatus(_A)
_AclNumExdSubitemEntry_Object=MibTableRow
aclNumExdSubitemEntry=_AclNumExdSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1))
aclNumExdSubitemEntry.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:aclNumExdSubitemEntry.setStatus(_A)
class _AclNumExdNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,199))
_AclNumExdNum_Type.__name__=_B
_AclNumExdNum_Object=MibTableColumn
aclNumExdNum=_AclNumExdNum_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,1),_AclNumExdNum_Type())
aclNumExdNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumExdNum.setStatus(_A)
class _AclNumExdSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNumExdSubNum_Type.__name__=_B
_AclNumExdSubNum_Object=MibTableColumn
aclNumExdSubNum=_AclNumExdSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,2),_AclNumExdSubNum_Type())
aclNumExdSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumExdSubNum.setStatus(_A)
_AclNumExdSubitemAdminStatus_Type=AdminStatus
_AclNumExdSubitemAdminStatus_Object=MibTableColumn
aclNumExdSubitemAdminStatus=_AclNumExdSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,3),_AclNumExdSubitemAdminStatus_Type())
aclNumExdSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumExdSubitemAdminStatus.setStatus(_A)
_AclNumExdSubitemAction_Type=Action
_AclNumExdSubitemAction_Object=MibTableColumn
aclNumExdSubitemAction=_AclNumExdSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,4),_AclNumExdSubitemAction_Type())
aclNumExdSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemAction.setStatus(_A)
class _AclNumExdSubitemProtocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AclNumExdSubitemProtocal_Type.__name__=_B
_AclNumExdSubitemProtocal_Object=MibTableColumn
aclNumExdSubitemProtocal=_AclNumExdSubitemProtocal_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,5),_AclNumExdSubitemProtocal_Type())
aclNumExdSubitemProtocal.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemProtocal.setStatus(_A)
_AclNumExdSubitemSrcAddr_Type=IpAddress
_AclNumExdSubitemSrcAddr_Object=MibTableColumn
aclNumExdSubitemSrcAddr=_AclNumExdSubitemSrcAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,6),_AclNumExdSubitemSrcAddr_Type())
aclNumExdSubitemSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemSrcAddr.setStatus(_A)
_AclNumExdSubitemSrcAddrWldmsk_Type=IpAddress
_AclNumExdSubitemSrcAddrWldmsk_Object=MibTableColumn
aclNumExdSubitemSrcAddrWldmsk=_AclNumExdSubitemSrcAddrWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,7),_AclNumExdSubitemSrcAddrWldmsk_Type())
aclNumExdSubitemSrcAddrWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemSrcAddrWldmsk.setStatus(_A)
_AclNumExdSubitemDstAddr_Type=IpAddress
_AclNumExdSubitemDstAddr_Object=MibTableColumn
aclNumExdSubitemDstAddr=_AclNumExdSubitemDstAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,8),_AclNumExdSubitemDstAddr_Type())
aclNumExdSubitemDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemDstAddr.setStatus(_A)
_AclNumExdSubitemDstAddrWldmsk_Type=IpAddress
_AclNumExdSubitemDstAddrWldmsk_Object=MibTableColumn
aclNumExdSubitemDstAddrWldmsk=_AclNumExdSubitemDstAddrWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,9),_AclNumExdSubitemDstAddrWldmsk_Type())
aclNumExdSubitemDstAddrWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemDstAddrWldmsk.setStatus(_A)
class _AclNumExdSubitemSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNumExdSubitemSrcPort_Type.__name__=_B
_AclNumExdSubitemSrcPort_Object=MibTableColumn
aclNumExdSubitemSrcPort=_AclNumExdSubitemSrcPort_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,10),_AclNumExdSubitemSrcPort_Type())
aclNumExdSubitemSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemSrcPort.setStatus(_A)
class _AclNumExdSubitemSrcPortWldmsk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNumExdSubitemSrcPortWldmsk_Type.__name__=_B
_AclNumExdSubitemSrcPortWldmsk_Object=MibTableColumn
aclNumExdSubitemSrcPortWldmsk=_AclNumExdSubitemSrcPortWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,11),_AclNumExdSubitemSrcPortWldmsk_Type())
aclNumExdSubitemSrcPortWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemSrcPortWldmsk.setStatus(_A)
class _AclNumExdSubitemDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNumExdSubitemDstPort_Type.__name__=_B
_AclNumExdSubitemDstPort_Object=MibTableColumn
aclNumExdSubitemDstPort=_AclNumExdSubitemDstPort_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,12),_AclNumExdSubitemDstPort_Type())
aclNumExdSubitemDstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemDstPort.setStatus(_A)
class _AclNumExdSubitemDstPortWldmsk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNumExdSubitemDstPortWldmsk_Type.__name__=_B
_AclNumExdSubitemDstPortWldmsk_Object=MibTableColumn
aclNumExdSubitemDstPortWldmsk=_AclNumExdSubitemDstPortWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,13),_AclNumExdSubitemDstPortWldmsk_Type())
aclNumExdSubitemDstPortWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemDstPortWldmsk.setStatus(_A)
class _AclNumExdSubitemIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AclNumExdSubitemIcmpType_Type.__name__=_B
_AclNumExdSubitemIcmpType_Object=MibTableColumn
aclNumExdSubitemIcmpType=_AclNumExdSubitemIcmpType_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,14),_AclNumExdSubitemIcmpType_Type())
aclNumExdSubitemIcmpType.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemIcmpType.setStatus(_A)
class _AclNumExdSubitemIcmpCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AclNumExdSubitemIcmpCode_Type.__name__=_B
_AclNumExdSubitemIcmpCode_Object=MibTableColumn
aclNumExdSubitemIcmpCode=_AclNumExdSubitemIcmpCode_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,15),_AclNumExdSubitemIcmpCode_Type())
aclNumExdSubitemIcmpCode.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemIcmpCode.setStatus(_A)
class _AclNumExdSubitemTcpEstablished_Type(TruthValue):defaultValue=2
_AclNumExdSubitemTcpEstablished_Type.__name__=_H
_AclNumExdSubitemTcpEstablished_Object=MibTableColumn
aclNumExdSubitemTcpEstablished=_AclNumExdSubitemTcpEstablished_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,16),_AclNumExdSubitemTcpEstablished_Type())
aclNumExdSubitemTcpEstablished.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemTcpEstablished.setStatus(_A)
class _AclNumExdSubitemPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclNumExdSubitemPrecedence_Type.__name__=_B
_AclNumExdSubitemPrecedence_Object=MibTableColumn
aclNumExdSubitemPrecedence=_AclNumExdSubitemPrecedence_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,17),_AclNumExdSubitemPrecedence_Type())
aclNumExdSubitemPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemPrecedence.setStatus(_A)
_AclNumExdSubitemTos_Type=TOSType
_AclNumExdSubitemTos_Object=MibTableColumn
aclNumExdSubitemTos=_AclNumExdSubitemTos_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,18),_AclNumExdSubitemTos_Type())
aclNumExdSubitemTos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemTos.setStatus(_A)
_AclNumExdSubitemDscp_Type=Dscp
_AclNumExdSubitemDscp_Object=MibTableColumn
aclNumExdSubitemDscp=_AclNumExdSubitemDscp_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,19),_AclNumExdSubitemDscp_Type())
aclNumExdSubitemDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemDscp.setStatus(_A)
class _AclNumExdSubitemFragments_Type(TruthValue):defaultValue=2
_AclNumExdSubitemFragments_Type.__name__=_H
_AclNumExdSubitemFragments_Object=MibTableColumn
aclNumExdSubitemFragments=_AclNumExdSubitemFragments_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,20),_AclNumExdSubitemFragments_Type())
aclNumExdSubitemFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemFragments.setStatus(_A)
class _AclNumExdSubitemTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNumExdSubitemTimeRange_Type.__name__=_E
_AclNumExdSubitemTimeRange_Object=MibTableColumn
aclNumExdSubitemTimeRange=_AclNumExdSubitemTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,21),_AclNumExdSubitemTimeRange_Type())
aclNumExdSubitemTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemTimeRange.setStatus(_A)
_AclNumExdSubitemRowStatus_Type=RowStatus
_AclNumExdSubitemRowStatus_Object=MibTableColumn
aclNumExdSubitemRowStatus=_AclNumExdSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,4,1,22),_AclNumExdSubitemRowStatus_Type())
aclNumExdSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumExdSubitemRowStatus.setStatus(_A)
_AclNumLnkSubitemTable_Object=MibTable
aclNumLnkSubitemTable=_AclNumLnkSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,5))
if mibBuilder.loadTexts:aclNumLnkSubitemTable.setStatus(_A)
_AclNumLnkSubitemEntry_Object=MibTableRow
aclNumLnkSubitemEntry=_AclNumLnkSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1))
aclNumLnkSubitemEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:aclNumLnkSubitemEntry.setStatus(_A)
class _AclNumLnkNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,299))
_AclNumLnkNum_Type.__name__=_B
_AclNumLnkNum_Object=MibTableColumn
aclNumLnkNum=_AclNumLnkNum_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,1),_AclNumLnkNum_Type())
aclNumLnkNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumLnkNum.setStatus(_A)
class _AclNumLnkSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNumLnkSubNum_Type.__name__=_B
_AclNumLnkSubNum_Object=MibTableColumn
aclNumLnkSubNum=_AclNumLnkSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,2),_AclNumLnkSubNum_Type())
aclNumLnkSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumLnkSubNum.setStatus(_A)
_AclNumLnkSubitemAdminStatus_Type=AdminStatus
_AclNumLnkSubitemAdminStatus_Object=MibTableColumn
aclNumLnkSubitemAdminStatus=_AclNumLnkSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,3),_AclNumLnkSubitemAdminStatus_Type())
aclNumLnkSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumLnkSubitemAdminStatus.setStatus(_A)
_AclNumLnkSubitemAction_Type=Action
_AclNumLnkSubitemAction_Object=MibTableColumn
aclNumLnkSubitemAction=_AclNumLnkSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,4),_AclNumLnkSubitemAction_Type())
aclNumLnkSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemAction.setStatus(_A)
class _AclNumLnkSubitemProtocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AclNumLnkSubitemProtocal_Type.__name__=_B
_AclNumLnkSubitemProtocal_Object=MibTableColumn
aclNumLnkSubitemProtocal=_AclNumLnkSubitemProtocal_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,5),_AclNumLnkSubitemProtocal_Type())
aclNumLnkSubitemProtocal.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemProtocal.setStatus(_A)
class _AclNumLnkSubitemCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclNumLnkSubitemCos_Type.__name__=_B
_AclNumLnkSubitemCos_Object=MibTableColumn
aclNumLnkSubitemCos=_AclNumLnkSubitemCos_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,6),_AclNumLnkSubitemCos_Type())
aclNumLnkSubitemCos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemCos.setStatus(_A)
_AclNumLnkSubitemSrcVlanID_Type=VlanId
_AclNumLnkSubitemSrcVlanID_Object=MibTableColumn
aclNumLnkSubitemSrcVlanID=_AclNumLnkSubitemSrcVlanID_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,7),_AclNumLnkSubitemSrcVlanID_Type())
aclNumLnkSubitemSrcVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemSrcVlanID.setStatus(_A)
_AclNumLnkSubitemSrcMacAddr_Type=MacAddress
_AclNumLnkSubitemSrcMacAddr_Object=MibTableColumn
aclNumLnkSubitemSrcMacAddr=_AclNumLnkSubitemSrcMacAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,8),_AclNumLnkSubitemSrcMacAddr_Type())
aclNumLnkSubitemSrcMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemSrcMacAddr.setStatus(_A)
_AclNumLnkSubitemSrcMacWldmsk_Type=MacAddress
_AclNumLnkSubitemSrcMacWldmsk_Object=MibTableColumn
aclNumLnkSubitemSrcMacWldmsk=_AclNumLnkSubitemSrcMacWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,9),_AclNumLnkSubitemSrcMacWldmsk_Type())
aclNumLnkSubitemSrcMacWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemSrcMacWldmsk.setStatus(_A)
_AclNumLnkSubitemDstMacAddr_Type=MacAddress
_AclNumLnkSubitemDstMacAddr_Object=MibTableColumn
aclNumLnkSubitemDstMacAddr=_AclNumLnkSubitemDstMacAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,10),_AclNumLnkSubitemDstMacAddr_Type())
aclNumLnkSubitemDstMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemDstMacAddr.setStatus(_A)
_AclNumLnkSubitemDstMacWldmsk_Type=MacAddress
_AclNumLnkSubitemDstMacWldmsk_Object=MibTableColumn
aclNumLnkSubitemDstMacWldmsk=_AclNumLnkSubitemDstMacWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,11),_AclNumLnkSubitemDstMacWldmsk_Type())
aclNumLnkSubitemDstMacWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemDstMacWldmsk.setStatus(_A)
class _AclNumLnkSubitemSrcPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_AclNumLnkSubitemSrcPortNum_Type.__name__=_B
_AclNumLnkSubitemSrcPortNum_Object=MibTableColumn
aclNumLnkSubitemSrcPortNum=_AclNumLnkSubitemSrcPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,12),_AclNumLnkSubitemSrcPortNum_Type())
aclNumLnkSubitemSrcPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemSrcPortNum.setStatus(_A)
class _AclNumLnkSubitemDstPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_AclNumLnkSubitemDstPortNum_Type.__name__=_B
_AclNumLnkSubitemDstPortNum_Object=MibTableColumn
aclNumLnkSubitemDstPortNum=_AclNumLnkSubitemDstPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,13),_AclNumLnkSubitemDstPortNum_Type())
aclNumLnkSubitemDstPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemDstPortNum.setStatus(_A)
class _AclNumLnkSubitemTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNumLnkSubitemTimeRange_Type.__name__=_E
_AclNumLnkSubitemTimeRange_Object=MibTableColumn
aclNumLnkSubitemTimeRange=_AclNumLnkSubitemTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,14),_AclNumLnkSubitemTimeRange_Type())
aclNumLnkSubitemTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemTimeRange.setStatus(_A)
_AclNumLnkSubitemRowStatus_Type=RowStatus
_AclNumLnkSubitemRowStatus_Object=MibTableColumn
aclNumLnkSubitemRowStatus=_AclNumLnkSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,15),_AclNumLnkSubitemRowStatus_Type())
aclNumLnkSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemRowStatus.setStatus(_A)
_AclNumLnkSubitemSrcEndVlanID_Type=VlanId
_AclNumLnkSubitemSrcEndVlanID_Object=MibTableColumn
aclNumLnkSubitemSrcEndVlanID=_AclNumLnkSubitemSrcEndVlanID_Object((1,3,6,1,4,1,13464,1,2,4,4,5,1,16),_AclNumLnkSubitemSrcEndVlanID_Type())
aclNumLnkSubitemSrcEndVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumLnkSubitemSrcEndVlanID.setStatus(_A)
_AclNumUserSubitemTable_Object=MibTable
aclNumUserSubitemTable=_AclNumUserSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,6))
if mibBuilder.loadTexts:aclNumUserSubitemTable.setStatus(_A)
_AclNumUserSubitemEntry_Object=MibTableRow
aclNumUserSubitemEntry=_AclNumUserSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1))
aclNumUserSubitemEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:aclNumUserSubitemEntry.setStatus(_A)
class _AclNumUserNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,399))
_AclNumUserNum_Type.__name__=_B
_AclNumUserNum_Object=MibTableColumn
aclNumUserNum=_AclNumUserNum_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,1),_AclNumUserNum_Type())
aclNumUserNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumUserNum.setStatus(_A)
class _AclNumUserSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNumUserSubNum_Type.__name__=_B
_AclNumUserSubNum_Object=MibTableColumn
aclNumUserSubNum=_AclNumUserSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,2),_AclNumUserSubNum_Type())
aclNumUserSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumUserSubNum.setStatus(_A)
_AclNumUserSubitemAdminStatus_Type=AdminStatus
_AclNumUserSubitemAdminStatus_Object=MibTableColumn
aclNumUserSubitemAdminStatus=_AclNumUserSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,3),_AclNumUserSubitemAdminStatus_Type())
aclNumUserSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNumUserSubitemAdminStatus.setStatus(_A)
_AclNumUserSubitemAction_Type=Action
_AclNumUserSubitemAction_Object=MibTableColumn
aclNumUserSubitemAction=_AclNumUserSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,4),_AclNumUserSubitemAction_Type())
aclNumUserSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemAction.setStatus(_A)
_AclNumUserSubitemSrcPortNum_Type=Integer32
_AclNumUserSubitemSrcPortNum_Object=MibTableColumn
aclNumUserSubitemSrcPortNum=_AclNumUserSubitemSrcPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,5),_AclNumUserSubitemSrcPortNum_Type())
aclNumUserSubitemSrcPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemSrcPortNum.setStatus(_A)
class _AclNumUserSubitemDstPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_AclNumUserSubitemDstPortNum_Type.__name__=_B
_AclNumUserSubitemDstPortNum_Object=MibTableColumn
aclNumUserSubitemDstPortNum=_AclNumUserSubitemDstPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,6),_AclNumUserSubitemDstPortNum_Type())
aclNumUserSubitemDstPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemDstPortNum.setStatus(_A)
class _AclNumUserSubitemRule_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_AclNumUserSubitemRule_Type.__name__=_E
_AclNumUserSubitemRule_Object=MibTableColumn
aclNumUserSubitemRule=_AclNumUserSubitemRule_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,7),_AclNumUserSubitemRule_Type())
aclNumUserSubitemRule.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemRule.setStatus(_A)
class _AclNumUserSubitemMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_AclNumUserSubitemMask_Type.__name__=_E
_AclNumUserSubitemMask_Object=MibTableColumn
aclNumUserSubitemMask=_AclNumUserSubitemMask_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,8),_AclNumUserSubitemMask_Type())
aclNumUserSubitemMask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemMask.setStatus(_A)
_AclNumUserSubitemSrcVlanID_Type=VlanId
_AclNumUserSubitemSrcVlanID_Object=MibTableColumn
aclNumUserSubitemSrcVlanID=_AclNumUserSubitemSrcVlanID_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,9),_AclNumUserSubitemSrcVlanID_Type())
aclNumUserSubitemSrcVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemSrcVlanID.setStatus(_A)
class _AclNumUserTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNumUserTimeRange_Type.__name__=_E
_AclNumUserTimeRange_Object=MibTableColumn
aclNumUserTimeRange=_AclNumUserTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,10),_AclNumUserTimeRange_Type())
aclNumUserTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserTimeRange.setStatus(_A)
_AclNumUserSubitemRowStatus_Type=RowStatus
_AclNumUserSubitemRowStatus_Object=MibTableColumn
aclNumUserSubitemRowStatus=_AclNumUserSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,6,1,11),_AclNumUserSubitemRowStatus_Type())
aclNumUserSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNumUserSubitemRowStatus.setStatus(_A)
_AclNamedTable_Object=MibTable
aclNamedTable=_AclNamedTable_Object((1,3,6,1,4,1,13464,1,2,4,4,7))
if mibBuilder.loadTexts:aclNamedTable.setStatus(_A)
_AclNamedEntry_Object=MibTableRow
aclNamedEntry=_AclNamedEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,7,1))
aclNamedEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:aclNamedEntry.setStatus(_A)
class _AclNamedName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNamedName_Type.__name__=_E
_AclNamedName_Object=MibTableColumn
aclNamedName=_AclNamedName_Object((1,3,6,1,4,1,13464,1,2,4,4,7,1,1),_AclNamedName_Type())
aclNamedName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedName.setStatus(_A)
_AclNamedType_Type=AclType
_AclNamedType_Object=MibTableColumn
aclNamedType=_AclNamedType_Object((1,3,6,1,4,1,13464,1,2,4,4,7,1,2),_AclNamedType_Type())
aclNamedType.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedType.setStatus(_A)
class _AclNamedMatchOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('auto',1)))
_AclNamedMatchOrder_Type.__name__=_B
_AclNamedMatchOrder_Object=MibTableColumn
aclNamedMatchOrder=_AclNamedMatchOrder_Object((1,3,6,1,4,1,13464,1,2,4,4,7,1,3),_AclNamedMatchOrder_Type())
aclNamedMatchOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedMatchOrder.setStatus(_A)
_AclNamedTotleSubitems_Type=Integer32
_AclNamedTotleSubitems_Object=MibTableColumn
aclNamedTotleSubitems=_AclNamedTotleSubitems_Object((1,3,6,1,4,1,13464,1,2,4,4,7,1,4),_AclNamedTotleSubitems_Type())
aclNamedTotleSubitems.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedTotleSubitems.setStatus(_A)
_AclNamedRowStatus_Type=RowStatus
_AclNamedRowStatus_Object=MibTableColumn
aclNamedRowStatus=_AclNamedRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,7,1,5),_AclNamedRowStatus_Type())
aclNamedRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedRowStatus.setStatus(_A)
_AclNamedStdSubitemTable_Object=MibTable
aclNamedStdSubitemTable=_AclNamedStdSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,8))
if mibBuilder.loadTexts:aclNamedStdSubitemTable.setStatus(_A)
_AclNamedStdSubitemEntry_Object=MibTableRow
aclNamedStdSubitemEntry=_AclNamedStdSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1))
aclNamedStdSubitemEntry.setIndexNames((0,_F,_T),(0,_F,_U))
if mibBuilder.loadTexts:aclNamedStdSubitemEntry.setStatus(_A)
class _AclNamedStdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNamedStdName_Type.__name__=_E
_AclNamedStdName_Object=MibTableColumn
aclNamedStdName=_AclNamedStdName_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,1),_AclNamedStdName_Type())
aclNamedStdName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedStdName.setStatus(_A)
class _AclNamedStdSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNamedStdSubNum_Type.__name__=_B
_AclNamedStdSubNum_Object=MibTableColumn
aclNamedStdSubNum=_AclNamedStdSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,2),_AclNamedStdSubNum_Type())
aclNamedStdSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedStdSubNum.setStatus(_A)
_AclNamedStdSubitemAdminStatus_Type=AdminStatus
_AclNamedStdSubitemAdminStatus_Object=MibTableColumn
aclNamedStdSubitemAdminStatus=_AclNamedStdSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,3),_AclNamedStdSubitemAdminStatus_Type())
aclNamedStdSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedStdSubitemAdminStatus.setStatus(_A)
_AclNamedStdSubitemAction_Type=Action
_AclNamedStdSubitemAction_Object=MibTableColumn
aclNamedStdSubitemAction=_AclNamedStdSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,4),_AclNamedStdSubitemAction_Type())
aclNamedStdSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedStdSubitemAction.setStatus(_A)
_AclNamedStdSubitemSrcAddr_Type=IpAddress
_AclNamedStdSubitemSrcAddr_Object=MibTableColumn
aclNamedStdSubitemSrcAddr=_AclNamedStdSubitemSrcAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,5),_AclNamedStdSubitemSrcAddr_Type())
aclNamedStdSubitemSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedStdSubitemSrcAddr.setStatus(_A)
_AclNamedStdSubitemSrcAddrWldmsk_Type=IpAddress
_AclNamedStdSubitemSrcAddrWldmsk_Object=MibTableColumn
aclNamedStdSubitemSrcAddrWldmsk=_AclNamedStdSubitemSrcAddrWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,6),_AclNamedStdSubitemSrcAddrWldmsk_Type())
aclNamedStdSubitemSrcAddrWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedStdSubitemSrcAddrWldmsk.setStatus(_A)
class _AclNamedStdFragments_Type(TruthValue):defaultValue=2
_AclNamedStdFragments_Type.__name__=_H
_AclNamedStdFragments_Object=MibTableColumn
aclNamedStdFragments=_AclNamedStdFragments_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,7),_AclNamedStdFragments_Type())
aclNamedStdFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedStdFragments.setStatus(_A)
class _AclNamedStdTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AclNamedStdTimeRange_Type.__name__=_E
_AclNamedStdTimeRange_Object=MibTableColumn
aclNamedStdTimeRange=_AclNamedStdTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,8),_AclNamedStdTimeRange_Type())
aclNamedStdTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedStdTimeRange.setStatus(_A)
_AclNamedStdSubitemRowStatus_Type=RowStatus
_AclNamedStdSubitemRowStatus_Object=MibTableColumn
aclNamedStdSubitemRowStatus=_AclNamedStdSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,8,1,9),_AclNamedStdSubitemRowStatus_Type())
aclNamedStdSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedStdSubitemRowStatus.setStatus(_A)
_AclNamedExdSubitemTable_Object=MibTable
aclNamedExdSubitemTable=_AclNamedExdSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,9))
if mibBuilder.loadTexts:aclNamedExdSubitemTable.setStatus(_A)
_AclNamedExdSubitemEntry_Object=MibTableRow
aclNamedExdSubitemEntry=_AclNamedExdSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1))
aclNamedExdSubitemEntry.setIndexNames((0,_F,_V),(0,_F,_W))
if mibBuilder.loadTexts:aclNamedExdSubitemEntry.setStatus(_A)
class _AclNamedExdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNamedExdName_Type.__name__=_E
_AclNamedExdName_Object=MibTableColumn
aclNamedExdName=_AclNamedExdName_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,1),_AclNamedExdName_Type())
aclNamedExdName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedExdName.setStatus(_A)
class _AclNamedExdSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNamedExdSubNum_Type.__name__=_B
_AclNamedExdSubNum_Object=MibTableColumn
aclNamedExdSubNum=_AclNamedExdSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,2),_AclNamedExdSubNum_Type())
aclNamedExdSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedExdSubNum.setStatus(_A)
_AclNamedExdSubitemAdminStatus_Type=AdminStatus
_AclNamedExdSubitemAdminStatus_Object=MibTableColumn
aclNamedExdSubitemAdminStatus=_AclNamedExdSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,3),_AclNamedExdSubitemAdminStatus_Type())
aclNamedExdSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedExdSubitemAdminStatus.setStatus(_A)
_AclNamedExdSubitemAction_Type=Action
_AclNamedExdSubitemAction_Object=MibTableColumn
aclNamedExdSubitemAction=_AclNamedExdSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,4),_AclNamedExdSubitemAction_Type())
aclNamedExdSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemAction.setStatus(_A)
class _AclNamedExdSubitemProtocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AclNamedExdSubitemProtocal_Type.__name__=_B
_AclNamedExdSubitemProtocal_Object=MibTableColumn
aclNamedExdSubitemProtocal=_AclNamedExdSubitemProtocal_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,5),_AclNamedExdSubitemProtocal_Type())
aclNamedExdSubitemProtocal.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemProtocal.setStatus(_A)
_AclNamedExdSubitemSrcAddr_Type=IpAddress
_AclNamedExdSubitemSrcAddr_Object=MibTableColumn
aclNamedExdSubitemSrcAddr=_AclNamedExdSubitemSrcAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,6),_AclNamedExdSubitemSrcAddr_Type())
aclNamedExdSubitemSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemSrcAddr.setStatus(_A)
_AclNamedExdSubitemSrcAddrWldmsk_Type=IpAddress
_AclNamedExdSubitemSrcAddrWldmsk_Object=MibTableColumn
aclNamedExdSubitemSrcAddrWldmsk=_AclNamedExdSubitemSrcAddrWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,7),_AclNamedExdSubitemSrcAddrWldmsk_Type())
aclNamedExdSubitemSrcAddrWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemSrcAddrWldmsk.setStatus(_A)
_AclNamedExdSubitemDstAddr_Type=IpAddress
_AclNamedExdSubitemDstAddr_Object=MibTableColumn
aclNamedExdSubitemDstAddr=_AclNamedExdSubitemDstAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,8),_AclNamedExdSubitemDstAddr_Type())
aclNamedExdSubitemDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemDstAddr.setStatus(_A)
_AclNamedExdSubitemDstAddrWldmsk_Type=IpAddress
_AclNamedExdSubitemDstAddrWldmsk_Object=MibTableColumn
aclNamedExdSubitemDstAddrWldmsk=_AclNamedExdSubitemDstAddrWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,9),_AclNamedExdSubitemDstAddrWldmsk_Type())
aclNamedExdSubitemDstAddrWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemDstAddrWldmsk.setStatus(_A)
class _AclNamedExdSubitemSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNamedExdSubitemSrcPort_Type.__name__=_B
_AclNamedExdSubitemSrcPort_Object=MibTableColumn
aclNamedExdSubitemSrcPort=_AclNamedExdSubitemSrcPort_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,10),_AclNamedExdSubitemSrcPort_Type())
aclNamedExdSubitemSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemSrcPort.setStatus(_A)
class _AclNamedExdSubitemSrcPortWldmsk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNamedExdSubitemSrcPortWldmsk_Type.__name__=_B
_AclNamedExdSubitemSrcPortWldmsk_Object=MibTableColumn
aclNamedExdSubitemSrcPortWldmsk=_AclNamedExdSubitemSrcPortWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,11),_AclNamedExdSubitemSrcPortWldmsk_Type())
aclNamedExdSubitemSrcPortWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemSrcPortWldmsk.setStatus(_A)
class _AclNamedExdSubitemDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNamedExdSubitemDstPort_Type.__name__=_B
_AclNamedExdSubitemDstPort_Object=MibTableColumn
aclNamedExdSubitemDstPort=_AclNamedExdSubitemDstPort_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,12),_AclNamedExdSubitemDstPort_Type())
aclNamedExdSubitemDstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemDstPort.setStatus(_A)
class _AclNamedExdSubitemDstPortWldmsk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclNamedExdSubitemDstPortWldmsk_Type.__name__=_B
_AclNamedExdSubitemDstPortWldmsk_Object=MibTableColumn
aclNamedExdSubitemDstPortWldmsk=_AclNamedExdSubitemDstPortWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,13),_AclNamedExdSubitemDstPortWldmsk_Type())
aclNamedExdSubitemDstPortWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemDstPortWldmsk.setStatus(_A)
class _AclNamedExdSubitemIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AclNamedExdSubitemIcmpType_Type.__name__=_B
_AclNamedExdSubitemIcmpType_Object=MibTableColumn
aclNamedExdSubitemIcmpType=_AclNamedExdSubitemIcmpType_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,14),_AclNamedExdSubitemIcmpType_Type())
aclNamedExdSubitemIcmpType.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemIcmpType.setStatus(_A)
class _AclNamedExdSubitemIcmpCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AclNamedExdSubitemIcmpCode_Type.__name__=_B
_AclNamedExdSubitemIcmpCode_Object=MibTableColumn
aclNamedExdSubitemIcmpCode=_AclNamedExdSubitemIcmpCode_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,15),_AclNamedExdSubitemIcmpCode_Type())
aclNamedExdSubitemIcmpCode.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemIcmpCode.setStatus(_A)
class _AclNamedExdSubitemTcpEstablished_Type(TruthValue):defaultValue=2
_AclNamedExdSubitemTcpEstablished_Type.__name__=_H
_AclNamedExdSubitemTcpEstablished_Object=MibTableColumn
aclNamedExdSubitemTcpEstablished=_AclNamedExdSubitemTcpEstablished_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,16),_AclNamedExdSubitemTcpEstablished_Type())
aclNamedExdSubitemTcpEstablished.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemTcpEstablished.setStatus(_A)
class _AclNamedExdSubitemPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclNamedExdSubitemPrecedence_Type.__name__=_B
_AclNamedExdSubitemPrecedence_Object=MibTableColumn
aclNamedExdSubitemPrecedence=_AclNamedExdSubitemPrecedence_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,17),_AclNamedExdSubitemPrecedence_Type())
aclNamedExdSubitemPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemPrecedence.setStatus(_A)
_AclNamedExdSubitemTos_Type=TOSType
_AclNamedExdSubitemTos_Object=MibTableColumn
aclNamedExdSubitemTos=_AclNamedExdSubitemTos_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,18),_AclNamedExdSubitemTos_Type())
aclNamedExdSubitemTos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemTos.setStatus(_A)
_AclNamedExdSubitemDscp_Type=Dscp
_AclNamedExdSubitemDscp_Object=MibTableColumn
aclNamedExdSubitemDscp=_AclNamedExdSubitemDscp_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,19),_AclNamedExdSubitemDscp_Type())
aclNamedExdSubitemDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemDscp.setStatus(_A)
class _AclNamedExdSubitemFragments_Type(TruthValue):defaultValue=2
_AclNamedExdSubitemFragments_Type.__name__=_H
_AclNamedExdSubitemFragments_Object=MibTableColumn
aclNamedExdSubitemFragments=_AclNamedExdSubitemFragments_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,20),_AclNamedExdSubitemFragments_Type())
aclNamedExdSubitemFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemFragments.setStatus(_A)
class _AclNamedExdSubitemTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AclNamedExdSubitemTimeRange_Type.__name__=_E
_AclNamedExdSubitemTimeRange_Object=MibTableColumn
aclNamedExdSubitemTimeRange=_AclNamedExdSubitemTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,21),_AclNamedExdSubitemTimeRange_Type())
aclNamedExdSubitemTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemTimeRange.setStatus(_A)
_AclNamedExdSubitemRowStatus_Type=RowStatus
_AclNamedExdSubitemRowStatus_Object=MibTableColumn
aclNamedExdSubitemRowStatus=_AclNamedExdSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,9,1,22),_AclNamedExdSubitemRowStatus_Type())
aclNamedExdSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedExdSubitemRowStatus.setStatus(_A)
_AclNamedLnkSubitemTable_Object=MibTable
aclNamedLnkSubitemTable=_AclNamedLnkSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,10))
if mibBuilder.loadTexts:aclNamedLnkSubitemTable.setStatus(_A)
_AclNamedLnkSubitemEntry_Object=MibTableRow
aclNamedLnkSubitemEntry=_AclNamedLnkSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1))
aclNamedLnkSubitemEntry.setIndexNames((0,_F,_X),(0,_F,_Y))
if mibBuilder.loadTexts:aclNamedLnkSubitemEntry.setStatus(_A)
class _AclNamedLnkName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNamedLnkName_Type.__name__=_E
_AclNamedLnkName_Object=MibTableColumn
aclNamedLnkName=_AclNamedLnkName_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,1),_AclNamedLnkName_Type())
aclNamedLnkName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedLnkName.setStatus(_A)
class _AclNamedLnkSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNamedLnkSubNum_Type.__name__=_B
_AclNamedLnkSubNum_Object=MibTableColumn
aclNamedLnkSubNum=_AclNamedLnkSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,2),_AclNamedLnkSubNum_Type())
aclNamedLnkSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedLnkSubNum.setStatus(_A)
_AclNamedLnkSubitemAdminStatus_Type=AdminStatus
_AclNamedLnkSubitemAdminStatus_Object=MibTableColumn
aclNamedLnkSubitemAdminStatus=_AclNamedLnkSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,3),_AclNamedLnkSubitemAdminStatus_Type())
aclNamedLnkSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedLnkSubitemAdminStatus.setStatus(_A)
_AclNamedLnkSubitemAction_Type=Action
_AclNamedLnkSubitemAction_Object=MibTableColumn
aclNamedLnkSubitemAction=_AclNamedLnkSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,4),_AclNamedLnkSubitemAction_Type())
aclNamedLnkSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemAction.setStatus(_A)
class _AclNamedLnkSubitemProtocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AclNamedLnkSubitemProtocal_Type.__name__=_B
_AclNamedLnkSubitemProtocal_Object=MibTableColumn
aclNamedLnkSubitemProtocal=_AclNamedLnkSubitemProtocal_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,5),_AclNamedLnkSubitemProtocal_Type())
aclNamedLnkSubitemProtocal.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemProtocal.setStatus(_A)
class _AclNamedLnkSubitemCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclNamedLnkSubitemCos_Type.__name__=_B
_AclNamedLnkSubitemCos_Object=MibTableColumn
aclNamedLnkSubitemCos=_AclNamedLnkSubitemCos_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,6),_AclNamedLnkSubitemCos_Type())
aclNamedLnkSubitemCos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemCos.setStatus(_A)
_AclNamedLnkSubitemSrcVlanID_Type=VlanId
_AclNamedLnkSubitemSrcVlanID_Object=MibTableColumn
aclNamedLnkSubitemSrcVlanID=_AclNamedLnkSubitemSrcVlanID_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,7),_AclNamedLnkSubitemSrcVlanID_Type())
aclNamedLnkSubitemSrcVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemSrcVlanID.setStatus(_A)
_AclNamedLnkSubitemSrcMacAddr_Type=MacAddress
_AclNamedLnkSubitemSrcMacAddr_Object=MibTableColumn
aclNamedLnkSubitemSrcMacAddr=_AclNamedLnkSubitemSrcMacAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,8),_AclNamedLnkSubitemSrcMacAddr_Type())
aclNamedLnkSubitemSrcMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemSrcMacAddr.setStatus(_A)
_AclNamedLnkSubitemSrcMacWldmsk_Type=MacAddress
_AclNamedLnkSubitemSrcMacWldmsk_Object=MibTableColumn
aclNamedLnkSubitemSrcMacWldmsk=_AclNamedLnkSubitemSrcMacWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,9),_AclNamedLnkSubitemSrcMacWldmsk_Type())
aclNamedLnkSubitemSrcMacWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemSrcMacWldmsk.setStatus(_A)
_AclNamedLnkSubitemDstMacAddr_Type=MacAddress
_AclNamedLnkSubitemDstMacAddr_Object=MibTableColumn
aclNamedLnkSubitemDstMacAddr=_AclNamedLnkSubitemDstMacAddr_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,10),_AclNamedLnkSubitemDstMacAddr_Type())
aclNamedLnkSubitemDstMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemDstMacAddr.setStatus(_A)
_AclNamedLnkSubitemDstMacWldmsk_Type=MacAddress
_AclNamedLnkSubitemDstMacWldmsk_Object=MibTableColumn
aclNamedLnkSubitemDstMacWldmsk=_AclNamedLnkSubitemDstMacWldmsk_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,11),_AclNamedLnkSubitemDstMacWldmsk_Type())
aclNamedLnkSubitemDstMacWldmsk.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemDstMacWldmsk.setStatus(_A)
class _AclNamedLnkSubitemSrcPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_AclNamedLnkSubitemSrcPortNum_Type.__name__=_B
_AclNamedLnkSubitemSrcPortNum_Object=MibTableColumn
aclNamedLnkSubitemSrcPortNum=_AclNamedLnkSubitemSrcPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,12),_AclNamedLnkSubitemSrcPortNum_Type())
aclNamedLnkSubitemSrcPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemSrcPortNum.setStatus(_A)
class _AclNamedLnkSubitemDstPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_AclNamedLnkSubitemDstPortNum_Type.__name__=_B
_AclNamedLnkSubitemDstPortNum_Object=MibTableColumn
aclNamedLnkSubitemDstPortNum=_AclNamedLnkSubitemDstPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,13),_AclNamedLnkSubitemDstPortNum_Type())
aclNamedLnkSubitemDstPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemDstPortNum.setStatus(_A)
class _AclNamedLnkSubitemTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNamedLnkSubitemTimeRange_Type.__name__=_E
_AclNamedLnkSubitemTimeRange_Object=MibTableColumn
aclNamedLnkSubitemTimeRange=_AclNamedLnkSubitemTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,14),_AclNamedLnkSubitemTimeRange_Type())
aclNamedLnkSubitemTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemTimeRange.setStatus(_A)
_AclNamedLnkSubitemRowStatus_Type=RowStatus
_AclNamedLnkSubitemRowStatus_Object=MibTableColumn
aclNamedLnkSubitemRowStatus=_AclNamedLnkSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,15),_AclNamedLnkSubitemRowStatus_Type())
aclNamedLnkSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemRowStatus.setStatus(_A)
_AclNamedLnkSubitemSrcEndVlanID_Type=VlanId
_AclNamedLnkSubitemSrcEndVlanID_Object=MibTableColumn
aclNamedLnkSubitemSrcEndVlanID=_AclNamedLnkSubitemSrcEndVlanID_Object((1,3,6,1,4,1,13464,1,2,4,4,10,1,16),_AclNamedLnkSubitemSrcEndVlanID_Type())
aclNamedLnkSubitemSrcEndVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedLnkSubitemSrcEndVlanID.setStatus(_A)
_AclNamedUserSubitemTable_Object=MibTable
aclNamedUserSubitemTable=_AclNamedUserSubitemTable_Object((1,3,6,1,4,1,13464,1,2,4,4,11))
if mibBuilder.loadTexts:aclNamedUserSubitemTable.setStatus(_A)
_AclNamedUserSubitemEntry_Object=MibTableRow
aclNamedUserSubitemEntry=_AclNamedUserSubitemEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1))
aclNamedUserSubitemEntry.setIndexNames((0,_F,_Z),(0,_F,_a))
if mibBuilder.loadTexts:aclNamedUserSubitemEntry.setStatus(_A)
class _AclNamedUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclNamedUserName_Type.__name__=_E
_AclNamedUserName_Object=MibTableColumn
aclNamedUserName=_AclNamedUserName_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,1),_AclNamedUserName_Type())
aclNamedUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedUserName.setStatus(_A)
class _AclNamedUserSubNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclNamedUserSubNum_Type.__name__=_B
_AclNamedUserSubNum_Object=MibTableColumn
aclNamedUserSubNum=_AclNamedUserSubNum_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,2),_AclNamedUserSubNum_Type())
aclNamedUserSubNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedUserSubNum.setStatus(_A)
_AclNamedUserSubitemAdminStatus_Type=AdminStatus
_AclNamedUserSubitemAdminStatus_Object=MibTableColumn
aclNamedUserSubitemAdminStatus=_AclNamedUserSubitemAdminStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,3),_AclNamedUserSubitemAdminStatus_Type())
aclNamedUserSubitemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNamedUserSubitemAdminStatus.setStatus(_A)
_AclNamedUserSubitemAction_Type=Action
_AclNamedUserSubitemAction_Object=MibTableColumn
aclNamedUserSubitemAction=_AclNamedUserSubitemAction_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,4),_AclNamedUserSubitemAction_Type())
aclNamedUserSubitemAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemAction.setStatus(_A)
_AclNamedUserSubitemSrcPortNum_Type=Integer32
_AclNamedUserSubitemSrcPortNum_Object=MibTableColumn
aclNamedUserSubitemSrcPortNum=_AclNamedUserSubitemSrcPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,5),_AclNamedUserSubitemSrcPortNum_Type())
aclNamedUserSubitemSrcPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemSrcPortNum.setStatus(_A)
class _AclNamedUserSubitemDstPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_AclNamedUserSubitemDstPortNum_Type.__name__=_B
_AclNamedUserSubitemDstPortNum_Object=MibTableColumn
aclNamedUserSubitemDstPortNum=_AclNamedUserSubitemDstPortNum_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,6),_AclNamedUserSubitemDstPortNum_Type())
aclNamedUserSubitemDstPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemDstPortNum.setStatus(_A)
class _AclNamedUserSubitemRule_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_AclNamedUserSubitemRule_Type.__name__=_E
_AclNamedUserSubitemRule_Object=MibTableColumn
aclNamedUserSubitemRule=_AclNamedUserSubitemRule_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,7),_AclNamedUserSubitemRule_Type())
aclNamedUserSubitemRule.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemRule.setStatus(_A)
class _AclNamedUserSubitemMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_AclNamedUserSubitemMask_Type.__name__=_E
_AclNamedUserSubitemMask_Object=MibTableColumn
aclNamedUserSubitemMask=_AclNamedUserSubitemMask_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,8),_AclNamedUserSubitemMask_Type())
aclNamedUserSubitemMask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemMask.setStatus(_A)
_AclNamedUserSubitemSrcVlanID_Type=VlanId
_AclNamedUserSubitemSrcVlanID_Object=MibTableColumn
aclNamedUserSubitemSrcVlanID=_AclNamedUserSubitemSrcVlanID_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,9),_AclNamedUserSubitemSrcVlanID_Type())
aclNamedUserSubitemSrcVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemSrcVlanID.setStatus(_A)
class _AclNamedUserTimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AclNamedUserTimeRange_Type.__name__=_E
_AclNamedUserTimeRange_Object=MibTableColumn
aclNamedUserTimeRange=_AclNamedUserTimeRange_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,10),_AclNamedUserTimeRange_Type())
aclNamedUserTimeRange.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserTimeRange.setStatus(_A)
_AclNamedUserSubitemRowStatus_Type=RowStatus
_AclNamedUserSubitemRowStatus_Object=MibTableColumn
aclNamedUserSubitemRowStatus=_AclNamedUserSubitemRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,11,1,11),_AclNamedUserSubitemRowStatus_Type())
aclNamedUserSubitemRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclNamedUserSubitemRowStatus.setStatus(_A)
_AclTimeRangeTable_Object=MibTable
aclTimeRangeTable=_AclTimeRangeTable_Object((1,3,6,1,4,1,13464,1,2,4,4,12))
if mibBuilder.loadTexts:aclTimeRangeTable.setStatus(_A)
_AclTimeRangeEntry_Object=MibTableRow
aclTimeRangeEntry=_AclTimeRangeEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,12,1))
aclTimeRangeEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:aclTimeRangeEntry.setStatus(_A)
class _AclTimeRangeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclTimeRangeName_Type.__name__=_E
_AclTimeRangeName_Object=MibTableColumn
aclTimeRangeName=_AclTimeRangeName_Object((1,3,6,1,4,1,13464,1,2,4,4,12,1,1),_AclTimeRangeName_Type())
aclTimeRangeName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeName.setStatus(_A)
_AclTimeRangeTotleAbsolutes_Type=Integer32
_AclTimeRangeTotleAbsolutes_Object=MibTableColumn
aclTimeRangeTotleAbsolutes=_AclTimeRangeTotleAbsolutes_Object((1,3,6,1,4,1,13464,1,2,4,4,12,1,2),_AclTimeRangeTotleAbsolutes_Type())
aclTimeRangeTotleAbsolutes.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeTotleAbsolutes.setStatus(_A)
_AclTimeRangeTotlePeriods_Type=Integer32
_AclTimeRangeTotlePeriods_Object=MibTableColumn
aclTimeRangeTotlePeriods=_AclTimeRangeTotlePeriods_Object((1,3,6,1,4,1,13464,1,2,4,4,12,1,3),_AclTimeRangeTotlePeriods_Type())
aclTimeRangeTotlePeriods.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeTotlePeriods.setStatus(_A)
_AclTimeRangeActive_Type=TruthValue
_AclTimeRangeActive_Object=MibTableColumn
aclTimeRangeActive=_AclTimeRangeActive_Object((1,3,6,1,4,1,13464,1,2,4,4,12,1,4),_AclTimeRangeActive_Type())
aclTimeRangeActive.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeActive.setStatus(_A)
_AclTimeRangeRowStatus_Type=RowStatus
_AclTimeRangeRowStatus_Object=MibTableColumn
aclTimeRangeRowStatus=_AclTimeRangeRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,12,1,5),_AclTimeRangeRowStatus_Type())
aclTimeRangeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclTimeRangeRowStatus.setStatus(_A)
_AclTimeRangeAbsoluteTable_Object=MibTable
aclTimeRangeAbsoluteTable=_AclTimeRangeAbsoluteTable_Object((1,3,6,1,4,1,13464,1,2,4,4,13))
if mibBuilder.loadTexts:aclTimeRangeAbsoluteTable.setStatus(_A)
_AclTimeRangeAbsoluteEntry_Object=MibTableRow
aclTimeRangeAbsoluteEntry=_AclTimeRangeAbsoluteEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,13,1))
aclTimeRangeAbsoluteEntry.setIndexNames((0,_F,_c),(0,_F,_d),(0,_F,_e))
if mibBuilder.loadTexts:aclTimeRangeAbsoluteEntry.setStatus(_A)
class _AclTimeRangeAbsoluteName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclTimeRangeAbsoluteName_Type.__name__=_E
_AclTimeRangeAbsoluteName_Object=MibTableColumn
aclTimeRangeAbsoluteName=_AclTimeRangeAbsoluteName_Object((1,3,6,1,4,1,13464,1,2,4,4,13,1,1),_AclTimeRangeAbsoluteName_Type())
aclTimeRangeAbsoluteName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeAbsoluteName.setStatus(_A)
_AclTimeRangeAbsoluteStartTime_Type=Unsigned32
_AclTimeRangeAbsoluteStartTime_Object=MibTableColumn
aclTimeRangeAbsoluteStartTime=_AclTimeRangeAbsoluteStartTime_Object((1,3,6,1,4,1,13464,1,2,4,4,13,1,2),_AclTimeRangeAbsoluteStartTime_Type())
aclTimeRangeAbsoluteStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeAbsoluteStartTime.setStatus(_A)
_AclTimeRangeAbsoluteEndTime_Type=Unsigned32
_AclTimeRangeAbsoluteEndTime_Object=MibTableColumn
aclTimeRangeAbsoluteEndTime=_AclTimeRangeAbsoluteEndTime_Object((1,3,6,1,4,1,13464,1,2,4,4,13,1,3),_AclTimeRangeAbsoluteEndTime_Type())
aclTimeRangeAbsoluteEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangeAbsoluteEndTime.setStatus(_A)
_AclTimeRangeAbsoluteRowStatus_Type=RowStatus
_AclTimeRangeAbsoluteRowStatus_Object=MibTableColumn
aclTimeRangeAbsoluteRowStatus=_AclTimeRangeAbsoluteRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,13,1,4),_AclTimeRangeAbsoluteRowStatus_Type())
aclTimeRangeAbsoluteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclTimeRangeAbsoluteRowStatus.setStatus(_A)
_AclTimeRangePeriodTable_Object=MibTable
aclTimeRangePeriodTable=_AclTimeRangePeriodTable_Object((1,3,6,1,4,1,13464,1,2,4,4,14))
if mibBuilder.loadTexts:aclTimeRangePeriodTable.setStatus(_A)
_AclTimeRangePeriodEntry_Object=MibTableRow
aclTimeRangePeriodEntry=_AclTimeRangePeriodEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1))
aclTimeRangePeriodEntry.setIndexNames((0,_F,_f),(0,_F,_g),(0,_F,_h),(0,_F,_i),(0,_F,_j),(0,_F,_k),(0,_F,_l))
if mibBuilder.loadTexts:aclTimeRangePeriodEntry.setStatus(_A)
class _AclTimeRangePeriodName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclTimeRangePeriodName_Type.__name__=_E
_AclTimeRangePeriodName_Object=MibTableColumn
aclTimeRangePeriodName=_AclTimeRangePeriodName_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,1),_AclTimeRangePeriodName_Type())
aclTimeRangePeriodName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodName.setStatus(_A)
_AclTimeRangePeriodStartWeekDay_Type=Unsigned32
_AclTimeRangePeriodStartWeekDay_Object=MibTableColumn
aclTimeRangePeriodStartWeekDay=_AclTimeRangePeriodStartWeekDay_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,2),_AclTimeRangePeriodStartWeekDay_Type())
aclTimeRangePeriodStartWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodStartWeekDay.setStatus(_A)
_AclTimeRangePeriodStartHour_Type=Unsigned32
_AclTimeRangePeriodStartHour_Object=MibTableColumn
aclTimeRangePeriodStartHour=_AclTimeRangePeriodStartHour_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,3),_AclTimeRangePeriodStartHour_Type())
aclTimeRangePeriodStartHour.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodStartHour.setStatus(_A)
_AclTimeRangePeriodStartMin_Type=Unsigned32
_AclTimeRangePeriodStartMin_Object=MibTableColumn
aclTimeRangePeriodStartMin=_AclTimeRangePeriodStartMin_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,4),_AclTimeRangePeriodStartMin_Type())
aclTimeRangePeriodStartMin.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodStartMin.setStatus(_A)
_AclTimeRangePeriodEndWeekDay_Type=Unsigned32
_AclTimeRangePeriodEndWeekDay_Object=MibTableColumn
aclTimeRangePeriodEndWeekDay=_AclTimeRangePeriodEndWeekDay_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,5),_AclTimeRangePeriodEndWeekDay_Type())
aclTimeRangePeriodEndWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodEndWeekDay.setStatus(_A)
_AclTimeRangePeriodEndHour_Type=Unsigned32
_AclTimeRangePeriodEndHour_Object=MibTableColumn
aclTimeRangePeriodEndHour=_AclTimeRangePeriodEndHour_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,6),_AclTimeRangePeriodEndHour_Type())
aclTimeRangePeriodEndHour.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodEndHour.setStatus(_A)
_AclTimeRangePeriodEndMin_Type=Unsigned32
_AclTimeRangePeriodEndMin_Object=MibTableColumn
aclTimeRangePeriodEndMin=_AclTimeRangePeriodEndMin_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,7),_AclTimeRangePeriodEndMin_Type())
aclTimeRangePeriodEndMin.setMaxAccess(_C)
if mibBuilder.loadTexts:aclTimeRangePeriodEndMin.setStatus(_A)
_AclTimeRangePeriodRowStatus_Type=RowStatus
_AclTimeRangePeriodRowStatus_Object=MibTableColumn
aclTimeRangePeriodRowStatus=_AclTimeRangePeriodRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,14,1,8),_AclTimeRangePeriodRowStatus_Type())
aclTimeRangePeriodRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclTimeRangePeriodRowStatus.setStatus(_A)
_AclActiveTable_Object=MibTable
aclActiveTable=_AclActiveTable_Object((1,3,6,1,4,1,13464,1,2,4,4,15))
if mibBuilder.loadTexts:aclActiveTable.setStatus(_A)
_AclActiveEntry_Object=MibTableRow
aclActiveEntry=_AclActiveEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1))
aclActiveEntry.setIndexNames((0,_F,_m))
if mibBuilder.loadTexts:aclActiveEntry.setStatus(_A)
_AclActiveIndex_Type=Integer32
_AclActiveIndex_Object=MibTableColumn
aclActiveIndex=_AclActiveIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,1),_AclActiveIndex_Type())
aclActiveIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveIndex.setStatus(_A)
class _AclActiveUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AclActiveUserGroupName_Type.__name__=_E
_AclActiveUserGroupName_Object=MibTableColumn
aclActiveUserGroupName=_AclActiveUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,2),_AclActiveUserGroupName_Type())
aclActiveUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:aclActiveUserGroupName.setStatus(_A)
class _AclActiveUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclActiveUserGroupSubitem_Type.__name__=_B
_AclActiveUserGroupSubitem_Object=MibTableColumn
aclActiveUserGroupSubitem=_AclActiveUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,3),_AclActiveUserGroupSubitem_Type())
aclActiveUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:aclActiveUserGroupSubitem.setStatus(_A)
class _AclActiveIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AclActiveIpGroupName_Type.__name__=_E
_AclActiveIpGroupName_Object=MibTableColumn
aclActiveIpGroupName=_AclActiveIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,4),_AclActiveIpGroupName_Type())
aclActiveIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:aclActiveIpGroupName.setStatus(_A)
class _AclActiveIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclActiveIpGroupSubitem_Type.__name__=_B
_AclActiveIpGroupSubitem_Object=MibTableColumn
aclActiveIpGroupSubitem=_AclActiveIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,5),_AclActiveIpGroupSubitem_Type())
aclActiveIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:aclActiveIpGroupSubitem.setStatus(_A)
class _AclActiveLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AclActiveLinkGroupName_Type.__name__=_E
_AclActiveLinkGroupName_Object=MibTableColumn
aclActiveLinkGroupName=_AclActiveLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,6),_AclActiveLinkGroupName_Type())
aclActiveLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:aclActiveLinkGroupName.setStatus(_A)
class _AclActiveLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AclActiveLinkGroupSubitem_Type.__name__=_B
_AclActiveLinkGroupSubitem_Object=MibTableColumn
aclActiveLinkGroupSubitem=_AclActiveLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,7),_AclActiveLinkGroupSubitem_Type())
aclActiveLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:aclActiveLinkGroupSubitem.setStatus(_A)
class _AclActiveBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock0Priority_Type.__name__=_B
_AclActiveBlock0Priority_Object=MibTableColumn
aclActiveBlock0Priority=_AclActiveBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,8),_AclActiveBlock0Priority_Type())
aclActiveBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock0Priority.setStatus(_A)
class _AclActiveBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock1Priority_Type.__name__=_B
_AclActiveBlock1Priority_Object=MibTableColumn
aclActiveBlock1Priority=_AclActiveBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,9),_AclActiveBlock1Priority_Type())
aclActiveBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock1Priority.setStatus(_A)
class _AclActiveBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock2Priority_Type.__name__=_B
_AclActiveBlock2Priority_Object=MibTableColumn
aclActiveBlock2Priority=_AclActiveBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,10),_AclActiveBlock2Priority_Type())
aclActiveBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock2Priority.setStatus(_A)
class _AclActiveBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock3Priority_Type.__name__=_B
_AclActiveBlock3Priority_Object=MibTableColumn
aclActiveBlock3Priority=_AclActiveBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,11),_AclActiveBlock3Priority_Type())
aclActiveBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock3Priority.setStatus(_A)
class _AclActiveBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock4Priority_Type.__name__=_B
_AclActiveBlock4Priority_Object=MibTableColumn
aclActiveBlock4Priority=_AclActiveBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,12),_AclActiveBlock4Priority_Type())
aclActiveBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock4Priority.setStatus(_A)
class _AclActiveConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_AclActiveConfigSequence_Type.__name__=_B
_AclActiveConfigSequence_Object=MibTableColumn
aclActiveConfigSequence=_AclActiveConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,13),_AclActiveConfigSequence_Type())
aclActiveConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveConfigSequence.setStatus(_A)
_AclActiveRunning_Type=TruthValue
_AclActiveRunning_Object=MibTableColumn
aclActiveRunning=_AclActiveRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,14),_AclActiveRunning_Type())
aclActiveRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveRunning.setStatus(_A)
_AclActiveRowStatus_Type=RowStatus
_AclActiveRowStatus_Object=MibTableColumn
aclActiveRowStatus=_AclActiveRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,15),_AclActiveRowStatus_Type())
aclActiveRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:aclActiveRowStatus.setStatus(_A)
class _AclActiveBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock5Priority_Type.__name__=_B
_AclActiveBlock5Priority_Object=MibTableColumn
aclActiveBlock5Priority=_AclActiveBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,16),_AclActiveBlock5Priority_Type())
aclActiveBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock5Priority.setStatus(_A)
class _AclActiveBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock6Priority_Type.__name__=_B
_AclActiveBlock6Priority_Object=MibTableColumn
aclActiveBlock6Priority=_AclActiveBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,17),_AclActiveBlock6Priority_Type())
aclActiveBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock6Priority.setStatus(_A)
class _AclActiveBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock7Priority_Type.__name__=_B
_AclActiveBlock7Priority_Object=MibTableColumn
aclActiveBlock7Priority=_AclActiveBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,18),_AclActiveBlock7Priority_Type())
aclActiveBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock7Priority.setStatus(_A)
class _AclActiveBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock8Priority_Type.__name__=_B
_AclActiveBlock8Priority_Object=MibTableColumn
aclActiveBlock8Priority=_AclActiveBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,19),_AclActiveBlock8Priority_Type())
aclActiveBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock8Priority.setStatus(_A)
class _AclActiveBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock9Priority_Type.__name__=_B
_AclActiveBlock9Priority_Object=MibTableColumn
aclActiveBlock9Priority=_AclActiveBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,20),_AclActiveBlock9Priority_Type())
aclActiveBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock9Priority.setStatus(_A)
class _AclActiveBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock10Priority_Type.__name__=_B
_AclActiveBlock10Priority_Object=MibTableColumn
aclActiveBlock10Priority=_AclActiveBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,21),_AclActiveBlock10Priority_Type())
aclActiveBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock10Priority.setStatus(_A)
class _AclActiveBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclActiveBlock11Priority_Type.__name__=_B
_AclActiveBlock11Priority_Object=MibTableColumn
aclActiveBlock11Priority=_AclActiveBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,15,1,22),_AclActiveBlock11Priority_Type())
aclActiveBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclActiveBlock11Priority.setStatus(_A)
_QosMirrorToTable_Object=MibTable
qosMirrorToTable=_QosMirrorToTable_Object((1,3,6,1,4,1,13464,1,2,4,4,16))
if mibBuilder.loadTexts:qosMirrorToTable.setStatus(_A)
_QosMirrorToEntry_Object=MibTableRow
qosMirrorToEntry=_QosMirrorToEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1))
qosMirrorToEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:qosMirrorToEntry.setStatus(_A)
_QosMirrorToIndex_Type=Integer32
_QosMirrorToIndex_Object=MibTableColumn
qosMirrorToIndex=_QosMirrorToIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,1),_QosMirrorToIndex_Type())
qosMirrorToIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToIndex.setStatus(_A)
class _QosMirrorToUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosMirrorToUserGroupName_Type.__name__=_E
_QosMirrorToUserGroupName_Object=MibTableColumn
qosMirrorToUserGroupName=_QosMirrorToUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,2),_QosMirrorToUserGroupName_Type())
qosMirrorToUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToUserGroupName.setStatus(_A)
class _QosMirrorToUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosMirrorToUserGroupSubitem_Type.__name__=_B
_QosMirrorToUserGroupSubitem_Object=MibTableColumn
qosMirrorToUserGroupSubitem=_QosMirrorToUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,3),_QosMirrorToUserGroupSubitem_Type())
qosMirrorToUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToUserGroupSubitem.setStatus(_A)
class _QosMirrorToIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosMirrorToIpGroupName_Type.__name__=_E
_QosMirrorToIpGroupName_Object=MibTableColumn
qosMirrorToIpGroupName=_QosMirrorToIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,4),_QosMirrorToIpGroupName_Type())
qosMirrorToIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToIpGroupName.setStatus(_A)
class _QosMirrorToIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosMirrorToIpGroupSubitem_Type.__name__=_B
_QosMirrorToIpGroupSubitem_Object=MibTableColumn
qosMirrorToIpGroupSubitem=_QosMirrorToIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,5),_QosMirrorToIpGroupSubitem_Type())
qosMirrorToIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToIpGroupSubitem.setStatus(_A)
class _QosMirrorToLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosMirrorToLinkGroupName_Type.__name__=_E
_QosMirrorToLinkGroupName_Object=MibTableColumn
qosMirrorToLinkGroupName=_QosMirrorToLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,6),_QosMirrorToLinkGroupName_Type())
qosMirrorToLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToLinkGroupName.setStatus(_A)
class _QosMirrorToLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosMirrorToLinkGroupSubitem_Type.__name__=_B
_QosMirrorToLinkGroupSubitem_Object=MibTableColumn
qosMirrorToLinkGroupSubitem=_QosMirrorToLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,7),_QosMirrorToLinkGroupSubitem_Type())
qosMirrorToLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToLinkGroupSubitem.setStatus(_A)
class _QosMirrorToInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_QosMirrorToInterface_Type.__name__=_B
_QosMirrorToInterface_Object=MibTableColumn
qosMirrorToInterface=_QosMirrorToInterface_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,8),_QosMirrorToInterface_Type())
qosMirrorToInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:qosMirrorToInterface.setStatus(_A)
class _QosMirrorToBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock0Priority_Type.__name__=_B
_QosMirrorToBlock0Priority_Object=MibTableColumn
qosMirrorToBlock0Priority=_QosMirrorToBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,9),_QosMirrorToBlock0Priority_Type())
qosMirrorToBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock0Priority.setStatus(_A)
class _QosMirrorToBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock1Priority_Type.__name__=_B
_QosMirrorToBlock1Priority_Object=MibTableColumn
qosMirrorToBlock1Priority=_QosMirrorToBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,10),_QosMirrorToBlock1Priority_Type())
qosMirrorToBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock1Priority.setStatus(_A)
class _QosMirrorToBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock2Priority_Type.__name__=_B
_QosMirrorToBlock2Priority_Object=MibTableColumn
qosMirrorToBlock2Priority=_QosMirrorToBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,11),_QosMirrorToBlock2Priority_Type())
qosMirrorToBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock2Priority.setStatus(_A)
class _QosMirrorToBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock3Priority_Type.__name__=_B
_QosMirrorToBlock3Priority_Object=MibTableColumn
qosMirrorToBlock3Priority=_QosMirrorToBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,12),_QosMirrorToBlock3Priority_Type())
qosMirrorToBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock3Priority.setStatus(_A)
class _QosMirrorToBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock4Priority_Type.__name__=_B
_QosMirrorToBlock4Priority_Object=MibTableColumn
qosMirrorToBlock4Priority=_QosMirrorToBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,13),_QosMirrorToBlock4Priority_Type())
qosMirrorToBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock4Priority.setStatus(_A)
class _QosMirrorToConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosMirrorToConfigSequence_Type.__name__=_B
_QosMirrorToConfigSequence_Object=MibTableColumn
qosMirrorToConfigSequence=_QosMirrorToConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,14),_QosMirrorToConfigSequence_Type())
qosMirrorToConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToConfigSequence.setStatus(_A)
_QosMirrorToRunning_Type=TruthValue
_QosMirrorToRunning_Object=MibTableColumn
qosMirrorToRunning=_QosMirrorToRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,15),_QosMirrorToRunning_Type())
qosMirrorToRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToRunning.setStatus(_A)
_QosMirrorToRowStatus_Type=RowStatus
_QosMirrorToRowStatus_Object=MibTableColumn
qosMirrorToRowStatus=_QosMirrorToRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,16),_QosMirrorToRowStatus_Type())
qosMirrorToRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosMirrorToRowStatus.setStatus(_A)
class _QosMirrorToBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock5Priority_Type.__name__=_B
_QosMirrorToBlock5Priority_Object=MibTableColumn
qosMirrorToBlock5Priority=_QosMirrorToBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,17),_QosMirrorToBlock5Priority_Type())
qosMirrorToBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock5Priority.setStatus(_A)
class _QosMirrorToBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock6Priority_Type.__name__=_B
_QosMirrorToBlock6Priority_Object=MibTableColumn
qosMirrorToBlock6Priority=_QosMirrorToBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,18),_QosMirrorToBlock6Priority_Type())
qosMirrorToBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock6Priority.setStatus(_A)
class _QosMirrorToBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock7Priority_Type.__name__=_B
_QosMirrorToBlock7Priority_Object=MibTableColumn
qosMirrorToBlock7Priority=_QosMirrorToBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,19),_QosMirrorToBlock7Priority_Type())
qosMirrorToBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock7Priority.setStatus(_A)
class _QosMirrorToBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock8Priority_Type.__name__=_B
_QosMirrorToBlock8Priority_Object=MibTableColumn
qosMirrorToBlock8Priority=_QosMirrorToBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,20),_QosMirrorToBlock8Priority_Type())
qosMirrorToBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock8Priority.setStatus(_A)
class _QosMirrorToBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock9Priority_Type.__name__=_B
_QosMirrorToBlock9Priority_Object=MibTableColumn
qosMirrorToBlock9Priority=_QosMirrorToBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,21),_QosMirrorToBlock9Priority_Type())
qosMirrorToBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock9Priority.setStatus(_A)
class _QosMirrorToBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock10Priority_Type.__name__=_B
_QosMirrorToBlock10Priority_Object=MibTableColumn
qosMirrorToBlock10Priority=_QosMirrorToBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,22),_QosMirrorToBlock10Priority_Type())
qosMirrorToBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock10Priority.setStatus(_A)
class _QosMirrorToBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosMirrorToBlock11Priority_Type.__name__=_B
_QosMirrorToBlock11Priority_Object=MibTableColumn
qosMirrorToBlock11Priority=_QosMirrorToBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,16,1,23),_QosMirrorToBlock11Priority_Type())
qosMirrorToBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMirrorToBlock11Priority.setStatus(_A)
_QosRateLimitTable_Object=MibTable
qosRateLimitTable=_QosRateLimitTable_Object((1,3,6,1,4,1,13464,1,2,4,4,17))
if mibBuilder.loadTexts:qosRateLimitTable.setStatus(_A)
_QosRateLimitEntry_Object=MibTableRow
qosRateLimitEntry=_QosRateLimitEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1))
qosRateLimitEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:qosRateLimitEntry.setStatus(_A)
_QosRateLimitIndex_Type=Integer32
_QosRateLimitIndex_Object=MibTableColumn
qosRateLimitIndex=_QosRateLimitIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,1),_QosRateLimitIndex_Type())
qosRateLimitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitIndex.setStatus(_A)
class _QosRateLimitUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosRateLimitUserGroupName_Type.__name__=_E
_QosRateLimitUserGroupName_Object=MibTableColumn
qosRateLimitUserGroupName=_QosRateLimitUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,2),_QosRateLimitUserGroupName_Type())
qosRateLimitUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitUserGroupName.setStatus(_A)
class _QosRateLimitUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosRateLimitUserGroupSubitem_Type.__name__=_B
_QosRateLimitUserGroupSubitem_Object=MibTableColumn
qosRateLimitUserGroupSubitem=_QosRateLimitUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,3),_QosRateLimitUserGroupSubitem_Type())
qosRateLimitUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitUserGroupSubitem.setStatus(_A)
class _QosRateLimitIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosRateLimitIpGroupName_Type.__name__=_E
_QosRateLimitIpGroupName_Object=MibTableColumn
qosRateLimitIpGroupName=_QosRateLimitIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,4),_QosRateLimitIpGroupName_Type())
qosRateLimitIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitIpGroupName.setStatus(_A)
class _QosRateLimitIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosRateLimitIpGroupSubitem_Type.__name__=_B
_QosRateLimitIpGroupSubitem_Object=MibTableColumn
qosRateLimitIpGroupSubitem=_QosRateLimitIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,5),_QosRateLimitIpGroupSubitem_Type())
qosRateLimitIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitIpGroupSubitem.setStatus(_A)
class _QosRateLimitLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosRateLimitLinkGroupName_Type.__name__=_E
_QosRateLimitLinkGroupName_Object=MibTableColumn
qosRateLimitLinkGroupName=_QosRateLimitLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,6),_QosRateLimitLinkGroupName_Type())
qosRateLimitLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitLinkGroupName.setStatus(_A)
class _QosRateLimitLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosRateLimitLinkGroupSubitem_Type.__name__=_B
_QosRateLimitLinkGroupSubitem_Object=MibTableColumn
qosRateLimitLinkGroupSubitem=_QosRateLimitLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,7),_QosRateLimitLinkGroupSubitem_Type())
qosRateLimitLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitLinkGroupSubitem.setStatus(_A)
class _QosRateLimitIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_QosRateLimitIntf_Type.__name__=_B
_QosRateLimitIntf_Object=MibTableColumn
qosRateLimitIntf=_QosRateLimitIntf_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,8),_QosRateLimitIntf_Type())
qosRateLimitIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitIntf.setStatus(_A)
class _QosRateLimitTargetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosRateLimitTargetRate_Type.__name__=_B
_QosRateLimitTargetRate_Object=MibTableColumn
qosRateLimitTargetRate=_QosRateLimitTargetRate_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,9),_QosRateLimitTargetRate_Type())
qosRateLimitTargetRate.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitTargetRate.setStatus(_A)
class _QosRateLimitExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('set-dscp-value',2)))
_QosRateLimitExceedAction_Type.__name__=_B
_QosRateLimitExceedAction_Object=MibTableColumn
qosRateLimitExceedAction=_QosRateLimitExceedAction_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,10),_QosRateLimitExceedAction_Type())
qosRateLimitExceedAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitExceedAction.setStatus(_A)
class _QosRateLimitDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QosRateLimitDscpValue_Type.__name__=_B
_QosRateLimitDscpValue_Object=MibTableColumn
qosRateLimitDscpValue=_QosRateLimitDscpValue_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,11),_QosRateLimitDscpValue_Type())
qosRateLimitDscpValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qosRateLimitDscpValue.setStatus(_A)
class _QosRateLimitBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock0Priority_Type.__name__=_B
_QosRateLimitBlock0Priority_Object=MibTableColumn
qosRateLimitBlock0Priority=_QosRateLimitBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,12),_QosRateLimitBlock0Priority_Type())
qosRateLimitBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock0Priority.setStatus(_A)
class _QosRateLimitBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock1Priority_Type.__name__=_B
_QosRateLimitBlock1Priority_Object=MibTableColumn
qosRateLimitBlock1Priority=_QosRateLimitBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,13),_QosRateLimitBlock1Priority_Type())
qosRateLimitBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock1Priority.setStatus(_A)
class _QosRateLimitBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock2Priority_Type.__name__=_B
_QosRateLimitBlock2Priority_Object=MibTableColumn
qosRateLimitBlock2Priority=_QosRateLimitBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,14),_QosRateLimitBlock2Priority_Type())
qosRateLimitBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock2Priority.setStatus(_A)
class _QosRateLimitBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock3Priority_Type.__name__=_B
_QosRateLimitBlock3Priority_Object=MibTableColumn
qosRateLimitBlock3Priority=_QosRateLimitBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,15),_QosRateLimitBlock3Priority_Type())
qosRateLimitBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock3Priority.setStatus(_A)
class _QosRateLimitBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock4Priority_Type.__name__=_B
_QosRateLimitBlock4Priority_Object=MibTableColumn
qosRateLimitBlock4Priority=_QosRateLimitBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,16),_QosRateLimitBlock4Priority_Type())
qosRateLimitBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock4Priority.setStatus(_A)
class _QosRateLimitConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosRateLimitConfigSequence_Type.__name__=_B
_QosRateLimitConfigSequence_Object=MibTableColumn
qosRateLimitConfigSequence=_QosRateLimitConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,17),_QosRateLimitConfigSequence_Type())
qosRateLimitConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitConfigSequence.setStatus(_A)
_QosRateLimitRunning_Type=TruthValue
_QosRateLimitRunning_Object=MibTableColumn
qosRateLimitRunning=_QosRateLimitRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,18),_QosRateLimitRunning_Type())
qosRateLimitRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitRunning.setStatus(_A)
_QosRateLimitRowStatus_Type=RowStatus
_QosRateLimitRowStatus_Object=MibTableColumn
qosRateLimitRowStatus=_QosRateLimitRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,19),_QosRateLimitRowStatus_Type())
qosRateLimitRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosRateLimitRowStatus.setStatus(_A)
class _QosRateLimitBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock5Priority_Type.__name__=_B
_QosRateLimitBlock5Priority_Object=MibTableColumn
qosRateLimitBlock5Priority=_QosRateLimitBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,20),_QosRateLimitBlock5Priority_Type())
qosRateLimitBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock5Priority.setStatus(_A)
class _QosRateLimitBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock6Priority_Type.__name__=_B
_QosRateLimitBlock6Priority_Object=MibTableColumn
qosRateLimitBlock6Priority=_QosRateLimitBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,21),_QosRateLimitBlock6Priority_Type())
qosRateLimitBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock6Priority.setStatus(_A)
class _QosRateLimitBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock7Priority_Type.__name__=_B
_QosRateLimitBlock7Priority_Object=MibTableColumn
qosRateLimitBlock7Priority=_QosRateLimitBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,22),_QosRateLimitBlock7Priority_Type())
qosRateLimitBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock7Priority.setStatus(_A)
class _QosRateLimitBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock8Priority_Type.__name__=_B
_QosRateLimitBlock8Priority_Object=MibTableColumn
qosRateLimitBlock8Priority=_QosRateLimitBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,23),_QosRateLimitBlock8Priority_Type())
qosRateLimitBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock8Priority.setStatus(_A)
class _QosRateLimitBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock9Priority_Type.__name__=_B
_QosRateLimitBlock9Priority_Object=MibTableColumn
qosRateLimitBlock9Priority=_QosRateLimitBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,24),_QosRateLimitBlock9Priority_Type())
qosRateLimitBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock9Priority.setStatus(_A)
class _QosRateLimitBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock10Priority_Type.__name__=_B
_QosRateLimitBlock10Priority_Object=MibTableColumn
qosRateLimitBlock10Priority=_QosRateLimitBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,25),_QosRateLimitBlock10Priority_Type())
qosRateLimitBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock10Priority.setStatus(_A)
class _QosRateLimitBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosRateLimitBlock11Priority_Type.__name__=_B
_QosRateLimitBlock11Priority_Object=MibTableColumn
qosRateLimitBlock11Priority=_QosRateLimitBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,17,1,26),_QosRateLimitBlock11Priority_Type())
qosRateLimitBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRateLimitBlock11Priority.setStatus(_A)
_QosTrafficPriorityTable_Object=MibTable
qosTrafficPriorityTable=_QosTrafficPriorityTable_Object((1,3,6,1,4,1,13464,1,2,4,4,18))
if mibBuilder.loadTexts:qosTrafficPriorityTable.setStatus(_A)
_QosTrafficPriorityEntry_Object=MibTableRow
qosTrafficPriorityEntry=_QosTrafficPriorityEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1))
qosTrafficPriorityEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:qosTrafficPriorityEntry.setStatus(_A)
_QosTrafficPriorityIndex_Type=Integer32
_QosTrafficPriorityIndex_Object=MibTableColumn
qosTrafficPriorityIndex=_QosTrafficPriorityIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,1),_QosTrafficPriorityIndex_Type())
qosTrafficPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityIndex.setStatus(_A)
class _QosTrafficPriorityUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficPriorityUserGroupName_Type.__name__=_E
_QosTrafficPriorityUserGroupName_Object=MibTableColumn
qosTrafficPriorityUserGroupName=_QosTrafficPriorityUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,2),_QosTrafficPriorityUserGroupName_Type())
qosTrafficPriorityUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityUserGroupName.setStatus(_A)
class _QosTrafficPriorityUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficPriorityUserGroupSubitem_Type.__name__=_B
_QosTrafficPriorityUserGroupSubitem_Object=MibTableColumn
qosTrafficPriorityUserGroupSubitem=_QosTrafficPriorityUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,3),_QosTrafficPriorityUserGroupSubitem_Type())
qosTrafficPriorityUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityUserGroupSubitem.setStatus(_A)
class _QosTrafficPriorityIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficPriorityIpGroupName_Type.__name__=_E
_QosTrafficPriorityIpGroupName_Object=MibTableColumn
qosTrafficPriorityIpGroupName=_QosTrafficPriorityIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,4),_QosTrafficPriorityIpGroupName_Type())
qosTrafficPriorityIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityIpGroupName.setStatus(_A)
class _QosTrafficPriorityIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficPriorityIpGroupSubitem_Type.__name__=_B
_QosTrafficPriorityIpGroupSubitem_Object=MibTableColumn
qosTrafficPriorityIpGroupSubitem=_QosTrafficPriorityIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,5),_QosTrafficPriorityIpGroupSubitem_Type())
qosTrafficPriorityIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityIpGroupSubitem.setStatus(_A)
class _QosTrafficPriorityLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficPriorityLinkGroupName_Type.__name__=_E
_QosTrafficPriorityLinkGroupName_Object=MibTableColumn
qosTrafficPriorityLinkGroupName=_QosTrafficPriorityLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,6),_QosTrafficPriorityLinkGroupName_Type())
qosTrafficPriorityLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityLinkGroupName.setStatus(_A)
class _QosTrafficPriorityLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficPriorityLinkGroupSubitem_Type.__name__=_B
_QosTrafficPriorityLinkGroupSubitem_Object=MibTableColumn
qosTrafficPriorityLinkGroupSubitem=_QosTrafficPriorityLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,7),_QosTrafficPriorityLinkGroupSubitem_Type())
qosTrafficPriorityLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityLinkGroupSubitem.setStatus(_A)
class _QosTrafficPriorityDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QosTrafficPriorityDscp_Type.__name__=_B
_QosTrafficPriorityDscp_Object=MibTableColumn
qosTrafficPriorityDscp=_QosTrafficPriorityDscp_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,8),_QosTrafficPriorityDscp_Type())
qosTrafficPriorityDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityDscp.setStatus(_A)
class _QosTrafficPriorityIpPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosTrafficPriorityIpPrecedence_Type.__name__=_B
_QosTrafficPriorityIpPrecedence_Object=MibTableColumn
qosTrafficPriorityIpPrecedence=_QosTrafficPriorityIpPrecedence_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,9),_QosTrafficPriorityIpPrecedence_Type())
qosTrafficPriorityIpPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityIpPrecedence.setStatus(_A)
class _QosTrafficPriorityCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosTrafficPriorityCos_Type.__name__=_B
_QosTrafficPriorityCos_Object=MibTableColumn
qosTrafficPriorityCos=_QosTrafficPriorityCos_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,10),_QosTrafficPriorityCos_Type())
qosTrafficPriorityCos.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityCos.setStatus(_A)
class _QosTrafficPriorityLocalPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosTrafficPriorityLocalPrecedence_Type.__name__=_B
_QosTrafficPriorityLocalPrecedence_Object=MibTableColumn
qosTrafficPriorityLocalPrecedence=_QosTrafficPriorityLocalPrecedence_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,11),_QosTrafficPriorityLocalPrecedence_Type())
qosTrafficPriorityLocalPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficPriorityLocalPrecedence.setStatus(_A)
class _QosTrafficPriorityBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock0Priority_Type.__name__=_B
_QosTrafficPriorityBlock0Priority_Object=MibTableColumn
qosTrafficPriorityBlock0Priority=_QosTrafficPriorityBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,12),_QosTrafficPriorityBlock0Priority_Type())
qosTrafficPriorityBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock0Priority.setStatus(_A)
class _QosTrafficPriorityBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock1Priority_Type.__name__=_B
_QosTrafficPriorityBlock1Priority_Object=MibTableColumn
qosTrafficPriorityBlock1Priority=_QosTrafficPriorityBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,13),_QosTrafficPriorityBlock1Priority_Type())
qosTrafficPriorityBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock1Priority.setStatus(_A)
class _QosTrafficPriorityBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock2Priority_Type.__name__=_B
_QosTrafficPriorityBlock2Priority_Object=MibTableColumn
qosTrafficPriorityBlock2Priority=_QosTrafficPriorityBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,14),_QosTrafficPriorityBlock2Priority_Type())
qosTrafficPriorityBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock2Priority.setStatus(_A)
class _QosTrafficPriorityBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock3Priority_Type.__name__=_B
_QosTrafficPriorityBlock3Priority_Object=MibTableColumn
qosTrafficPriorityBlock3Priority=_QosTrafficPriorityBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,15),_QosTrafficPriorityBlock3Priority_Type())
qosTrafficPriorityBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock3Priority.setStatus(_A)
class _QosTrafficPriorityBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock4Priority_Type.__name__=_B
_QosTrafficPriorityBlock4Priority_Object=MibTableColumn
qosTrafficPriorityBlock4Priority=_QosTrafficPriorityBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,16),_QosTrafficPriorityBlock4Priority_Type())
qosTrafficPriorityBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock4Priority.setStatus(_A)
class _QosTrafficPriorityConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosTrafficPriorityConfigSequence_Type.__name__=_B
_QosTrafficPriorityConfigSequence_Object=MibTableColumn
qosTrafficPriorityConfigSequence=_QosTrafficPriorityConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,17),_QosTrafficPriorityConfigSequence_Type())
qosTrafficPriorityConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityConfigSequence.setStatus(_A)
_QosTrafficPriorityRunning_Type=TruthValue
_QosTrafficPriorityRunning_Object=MibTableColumn
qosTrafficPriorityRunning=_QosTrafficPriorityRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,18),_QosTrafficPriorityRunning_Type())
qosTrafficPriorityRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityRunning.setStatus(_A)
_QosTrafficPriorityRowStatus_Type=RowStatus
_QosTrafficPriorityRowStatus_Object=MibTableColumn
qosTrafficPriorityRowStatus=_QosTrafficPriorityRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,19),_QosTrafficPriorityRowStatus_Type())
qosTrafficPriorityRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficPriorityRowStatus.setStatus(_A)
class _QosTrafficPriorityBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock5Priority_Type.__name__=_B
_QosTrafficPriorityBlock5Priority_Object=MibTableColumn
qosTrafficPriorityBlock5Priority=_QosTrafficPriorityBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,20),_QosTrafficPriorityBlock5Priority_Type())
qosTrafficPriorityBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock5Priority.setStatus(_A)
class _QosTrafficPriorityBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock6Priority_Type.__name__=_B
_QosTrafficPriorityBlock6Priority_Object=MibTableColumn
qosTrafficPriorityBlock6Priority=_QosTrafficPriorityBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,21),_QosTrafficPriorityBlock6Priority_Type())
qosTrafficPriorityBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock6Priority.setStatus(_A)
class _QosTrafficPriorityBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock7Priority_Type.__name__=_B
_QosTrafficPriorityBlock7Priority_Object=MibTableColumn
qosTrafficPriorityBlock7Priority=_QosTrafficPriorityBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,22),_QosTrafficPriorityBlock7Priority_Type())
qosTrafficPriorityBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock7Priority.setStatus(_A)
class _QosTrafficPriorityBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock8Priority_Type.__name__=_B
_QosTrafficPriorityBlock8Priority_Object=MibTableColumn
qosTrafficPriorityBlock8Priority=_QosTrafficPriorityBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,23),_QosTrafficPriorityBlock8Priority_Type())
qosTrafficPriorityBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock8Priority.setStatus(_A)
class _QosTrafficPriorityBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock9Priority_Type.__name__=_B
_QosTrafficPriorityBlock9Priority_Object=MibTableColumn
qosTrafficPriorityBlock9Priority=_QosTrafficPriorityBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,24),_QosTrafficPriorityBlock9Priority_Type())
qosTrafficPriorityBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock9Priority.setStatus(_A)
class _QosTrafficPriorityBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock10Priority_Type.__name__=_B
_QosTrafficPriorityBlock10Priority_Object=MibTableColumn
qosTrafficPriorityBlock10Priority=_QosTrafficPriorityBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,25),_QosTrafficPriorityBlock10Priority_Type())
qosTrafficPriorityBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock10Priority.setStatus(_A)
class _QosTrafficPriorityBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficPriorityBlock11Priority_Type.__name__=_B
_QosTrafficPriorityBlock11Priority_Object=MibTableColumn
qosTrafficPriorityBlock11Priority=_QosTrafficPriorityBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,18,1,26),_QosTrafficPriorityBlock11Priority_Type())
qosTrafficPriorityBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficPriorityBlock11Priority.setStatus(_A)
_QosTrafficRedirectTable_Object=MibTable
qosTrafficRedirectTable=_QosTrafficRedirectTable_Object((1,3,6,1,4,1,13464,1,2,4,4,19))
if mibBuilder.loadTexts:qosTrafficRedirectTable.setStatus(_A)
_QosTrafficRedirectEntry_Object=MibTableRow
qosTrafficRedirectEntry=_QosTrafficRedirectEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1))
qosTrafficRedirectEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:qosTrafficRedirectEntry.setStatus(_A)
_QosTrafficRedirectIndex_Type=Integer32
_QosTrafficRedirectIndex_Object=MibTableColumn
qosTrafficRedirectIndex=_QosTrafficRedirectIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,1),_QosTrafficRedirectIndex_Type())
qosTrafficRedirectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectIndex.setStatus(_A)
class _QosTrafficRedirectUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficRedirectUserGroupName_Type.__name__=_E
_QosTrafficRedirectUserGroupName_Object=MibTableColumn
qosTrafficRedirectUserGroupName=_QosTrafficRedirectUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,2),_QosTrafficRedirectUserGroupName_Type())
qosTrafficRedirectUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectUserGroupName.setStatus(_A)
class _QosTrafficRedirectUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficRedirectUserGroupSubitem_Type.__name__=_B
_QosTrafficRedirectUserGroupSubitem_Object=MibTableColumn
qosTrafficRedirectUserGroupSubitem=_QosTrafficRedirectUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,3),_QosTrafficRedirectUserGroupSubitem_Type())
qosTrafficRedirectUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectUserGroupSubitem.setStatus(_A)
class _QosTrafficRedirectIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficRedirectIpGroupName_Type.__name__=_E
_QosTrafficRedirectIpGroupName_Object=MibTableColumn
qosTrafficRedirectIpGroupName=_QosTrafficRedirectIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,4),_QosTrafficRedirectIpGroupName_Type())
qosTrafficRedirectIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectIpGroupName.setStatus(_A)
class _QosTrafficRedirectIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficRedirectIpGroupSubitem_Type.__name__=_B
_QosTrafficRedirectIpGroupSubitem_Object=MibTableColumn
qosTrafficRedirectIpGroupSubitem=_QosTrafficRedirectIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,5),_QosTrafficRedirectIpGroupSubitem_Type())
qosTrafficRedirectIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectIpGroupSubitem.setStatus(_A)
class _QosTrafficRedirectLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficRedirectLinkGroupName_Type.__name__=_E
_QosTrafficRedirectLinkGroupName_Object=MibTableColumn
qosTrafficRedirectLinkGroupName=_QosTrafficRedirectLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,6),_QosTrafficRedirectLinkGroupName_Type())
qosTrafficRedirectLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectLinkGroupName.setStatus(_A)
class _QosTrafficRedirectLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficRedirectLinkGroupSubitem_Type.__name__=_B
_QosTrafficRedirectLinkGroupSubitem_Object=MibTableColumn
qosTrafficRedirectLinkGroupSubitem=_QosTrafficRedirectLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,7),_QosTrafficRedirectLinkGroupSubitem_Type())
qosTrafficRedirectLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectLinkGroupSubitem.setStatus(_A)
class _QosTrafficRedirectInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_QosTrafficRedirectInterface_Type.__name__=_B
_QosTrafficRedirectInterface_Object=MibTableColumn
qosTrafficRedirectInterface=_QosTrafficRedirectInterface_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,8),_QosTrafficRedirectInterface_Type())
qosTrafficRedirectInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRedirectInterface.setStatus(_A)
class _QosTrafficRedirectBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock0Priority_Type.__name__=_B
_QosTrafficRedirectBlock0Priority_Object=MibTableColumn
qosTrafficRedirectBlock0Priority=_QosTrafficRedirectBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,9),_QosTrafficRedirectBlock0Priority_Type())
qosTrafficRedirectBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock0Priority.setStatus(_A)
class _QosTrafficRedirectBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock1Priority_Type.__name__=_B
_QosTrafficRedirectBlock1Priority_Object=MibTableColumn
qosTrafficRedirectBlock1Priority=_QosTrafficRedirectBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,10),_QosTrafficRedirectBlock1Priority_Type())
qosTrafficRedirectBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock1Priority.setStatus(_A)
class _QosTrafficRedirectBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock2Priority_Type.__name__=_B
_QosTrafficRedirectBlock2Priority_Object=MibTableColumn
qosTrafficRedirectBlock2Priority=_QosTrafficRedirectBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,11),_QosTrafficRedirectBlock2Priority_Type())
qosTrafficRedirectBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock2Priority.setStatus(_A)
class _QosTrafficRedirectBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock3Priority_Type.__name__=_B
_QosTrafficRedirectBlock3Priority_Object=MibTableColumn
qosTrafficRedirectBlock3Priority=_QosTrafficRedirectBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,12),_QosTrafficRedirectBlock3Priority_Type())
qosTrafficRedirectBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock3Priority.setStatus(_A)
class _QosTrafficRedirectBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock4Priority_Type.__name__=_B
_QosTrafficRedirectBlock4Priority_Object=MibTableColumn
qosTrafficRedirectBlock4Priority=_QosTrafficRedirectBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,13),_QosTrafficRedirectBlock4Priority_Type())
qosTrafficRedirectBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock4Priority.setStatus(_A)
class _QosTrafficRedirectConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosTrafficRedirectConfigSequence_Type.__name__=_B
_QosTrafficRedirectConfigSequence_Object=MibTableColumn
qosTrafficRedirectConfigSequence=_QosTrafficRedirectConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,14),_QosTrafficRedirectConfigSequence_Type())
qosTrafficRedirectConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectConfigSequence.setStatus(_A)
_QosTrafficRedirectRunning_Type=TruthValue
_QosTrafficRedirectRunning_Object=MibTableColumn
qosTrafficRedirectRunning=_QosTrafficRedirectRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,15),_QosTrafficRedirectRunning_Type())
qosTrafficRedirectRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectRunning.setStatus(_A)
_QosTrafficRedirectRowStatus_Type=RowStatus
_QosTrafficRedirectRowStatus_Object=MibTableColumn
qosTrafficRedirectRowStatus=_QosTrafficRedirectRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,16),_QosTrafficRedirectRowStatus_Type())
qosTrafficRedirectRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficRedirectRowStatus.setStatus(_A)
class _QosTrafficRedirectBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock5Priority_Type.__name__=_B
_QosTrafficRedirectBlock5Priority_Object=MibTableColumn
qosTrafficRedirectBlock5Priority=_QosTrafficRedirectBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,17),_QosTrafficRedirectBlock5Priority_Type())
qosTrafficRedirectBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock5Priority.setStatus(_A)
class _QosTrafficRedirectBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock6Priority_Type.__name__=_B
_QosTrafficRedirectBlock6Priority_Object=MibTableColumn
qosTrafficRedirectBlock6Priority=_QosTrafficRedirectBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,18),_QosTrafficRedirectBlock6Priority_Type())
qosTrafficRedirectBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock6Priority.setStatus(_A)
class _QosTrafficRedirectBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock7Priority_Type.__name__=_B
_QosTrafficRedirectBlock7Priority_Object=MibTableColumn
qosTrafficRedirectBlock7Priority=_QosTrafficRedirectBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,19),_QosTrafficRedirectBlock7Priority_Type())
qosTrafficRedirectBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock7Priority.setStatus(_A)
class _QosTrafficRedirectBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock8Priority_Type.__name__=_B
_QosTrafficRedirectBlock8Priority_Object=MibTableColumn
qosTrafficRedirectBlock8Priority=_QosTrafficRedirectBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,20),_QosTrafficRedirectBlock8Priority_Type())
qosTrafficRedirectBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock8Priority.setStatus(_A)
class _QosTrafficRedirectBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock9Priority_Type.__name__=_B
_QosTrafficRedirectBlock9Priority_Object=MibTableColumn
qosTrafficRedirectBlock9Priority=_QosTrafficRedirectBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,21),_QosTrafficRedirectBlock9Priority_Type())
qosTrafficRedirectBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock9Priority.setStatus(_A)
class _QosTrafficRedirectBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock10Priority_Type.__name__=_B
_QosTrafficRedirectBlock10Priority_Object=MibTableColumn
qosTrafficRedirectBlock10Priority=_QosTrafficRedirectBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,22),_QosTrafficRedirectBlock10Priority_Type())
qosTrafficRedirectBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock10Priority.setStatus(_A)
class _QosTrafficRedirectBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRedirectBlock11Priority_Type.__name__=_B
_QosTrafficRedirectBlock11Priority_Object=MibTableColumn
qosTrafficRedirectBlock11Priority=_QosTrafficRedirectBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,19,1,23),_QosTrafficRedirectBlock11Priority_Type())
qosTrafficRedirectBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRedirectBlock11Priority.setStatus(_A)
_QosTrafficStatisticsTable_Object=MibTable
qosTrafficStatisticsTable=_QosTrafficStatisticsTable_Object((1,3,6,1,4,1,13464,1,2,4,4,20))
if mibBuilder.loadTexts:qosTrafficStatisticsTable.setStatus(_A)
_QosTrafficStatisticsEntry_Object=MibTableRow
qosTrafficStatisticsEntry=_QosTrafficStatisticsEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1))
qosTrafficStatisticsEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:qosTrafficStatisticsEntry.setStatus(_A)
_QosTrafficStatisticsIndex_Type=Integer32
_QosTrafficStatisticsIndex_Object=MibTableColumn
qosTrafficStatisticsIndex=_QosTrafficStatisticsIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,1),_QosTrafficStatisticsIndex_Type())
qosTrafficStatisticsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsIndex.setStatus(_A)
class _QosTrafficStatisticsUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficStatisticsUserGroupName_Type.__name__=_E
_QosTrafficStatisticsUserGroupName_Object=MibTableColumn
qosTrafficStatisticsUserGroupName=_QosTrafficStatisticsUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,2),_QosTrafficStatisticsUserGroupName_Type())
qosTrafficStatisticsUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficStatisticsUserGroupName.setStatus(_A)
class _QosTrafficStatisticsUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficStatisticsUserGroupSubitem_Type.__name__=_B
_QosTrafficStatisticsUserGroupSubitem_Object=MibTableColumn
qosTrafficStatisticsUserGroupSubitem=_QosTrafficStatisticsUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,3),_QosTrafficStatisticsUserGroupSubitem_Type())
qosTrafficStatisticsUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficStatisticsUserGroupSubitem.setStatus(_A)
class _QosTrafficStatisticsIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficStatisticsIpGroupName_Type.__name__=_E
_QosTrafficStatisticsIpGroupName_Object=MibTableColumn
qosTrafficStatisticsIpGroupName=_QosTrafficStatisticsIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,4),_QosTrafficStatisticsIpGroupName_Type())
qosTrafficStatisticsIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficStatisticsIpGroupName.setStatus(_A)
class _QosTrafficStatisticsIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficStatisticsIpGroupSubitem_Type.__name__=_B
_QosTrafficStatisticsIpGroupSubitem_Object=MibTableColumn
qosTrafficStatisticsIpGroupSubitem=_QosTrafficStatisticsIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,5),_QosTrafficStatisticsIpGroupSubitem_Type())
qosTrafficStatisticsIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficStatisticsIpGroupSubitem.setStatus(_A)
class _QosTrafficStatisticsLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficStatisticsLinkGroupName_Type.__name__=_E
_QosTrafficStatisticsLinkGroupName_Object=MibTableColumn
qosTrafficStatisticsLinkGroupName=_QosTrafficStatisticsLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,6),_QosTrafficStatisticsLinkGroupName_Type())
qosTrafficStatisticsLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficStatisticsLinkGroupName.setStatus(_A)
class _QosTrafficStatisticsLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficStatisticsLinkGroupSubitem_Type.__name__=_B
_QosTrafficStatisticsLinkGroupSubitem_Object=MibTableColumn
qosTrafficStatisticsLinkGroupSubitem=_QosTrafficStatisticsLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,7),_QosTrafficStatisticsLinkGroupSubitem_Type())
qosTrafficStatisticsLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficStatisticsLinkGroupSubitem.setStatus(_A)
class _QosTrafficStatisticsBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock0Priority_Type.__name__=_B
_QosTrafficStatisticsBlock0Priority_Object=MibTableColumn
qosTrafficStatisticsBlock0Priority=_QosTrafficStatisticsBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,8),_QosTrafficStatisticsBlock0Priority_Type())
qosTrafficStatisticsBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock0Priority.setStatus(_A)
class _QosTrafficStatisticsBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock1Priority_Type.__name__=_B
_QosTrafficStatisticsBlock1Priority_Object=MibTableColumn
qosTrafficStatisticsBlock1Priority=_QosTrafficStatisticsBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,9),_QosTrafficStatisticsBlock1Priority_Type())
qosTrafficStatisticsBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock1Priority.setStatus(_A)
class _QosTrafficStatisticsBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock2Priority_Type.__name__=_B
_QosTrafficStatisticsBlock2Priority_Object=MibTableColumn
qosTrafficStatisticsBlock2Priority=_QosTrafficStatisticsBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,10),_QosTrafficStatisticsBlock2Priority_Type())
qosTrafficStatisticsBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock2Priority.setStatus(_A)
class _QosTrafficStatisticsBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock3Priority_Type.__name__=_B
_QosTrafficStatisticsBlock3Priority_Object=MibTableColumn
qosTrafficStatisticsBlock3Priority=_QosTrafficStatisticsBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,11),_QosTrafficStatisticsBlock3Priority_Type())
qosTrafficStatisticsBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock3Priority.setStatus(_A)
class _QosTrafficStatisticsBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock4Priority_Type.__name__=_B
_QosTrafficStatisticsBlock4Priority_Object=MibTableColumn
qosTrafficStatisticsBlock4Priority=_QosTrafficStatisticsBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,12),_QosTrafficStatisticsBlock4Priority_Type())
qosTrafficStatisticsBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock4Priority.setStatus(_A)
class _QosTrafficStatisticsConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosTrafficStatisticsConfigSequence_Type.__name__=_B
_QosTrafficStatisticsConfigSequence_Object=MibTableColumn
qosTrafficStatisticsConfigSequence=_QosTrafficStatisticsConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,13),_QosTrafficStatisticsConfigSequence_Type())
qosTrafficStatisticsConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsConfigSequence.setStatus(_A)
_QosTrafficStatisticsRunning_Type=TruthValue
_QosTrafficStatisticsRunning_Object=MibTableColumn
qosTrafficStatisticsRunning=_QosTrafficStatisticsRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,14),_QosTrafficStatisticsRunning_Type())
qosTrafficStatisticsRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsRunning.setStatus(_A)
_QosTrafficStatisticsRowStatus_Type=RowStatus
_QosTrafficStatisticsRowStatus_Object=MibTableColumn
qosTrafficStatisticsRowStatus=_QosTrafficStatisticsRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,15),_QosTrafficStatisticsRowStatus_Type())
qosTrafficStatisticsRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficStatisticsRowStatus.setStatus(_A)
_QosTrafficStatisticsCounter_Type=Integer32
_QosTrafficStatisticsCounter_Object=MibTableColumn
qosTrafficStatisticsCounter=_QosTrafficStatisticsCounter_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,16),_QosTrafficStatisticsCounter_Type())
qosTrafficStatisticsCounter.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficStatisticsCounter.setStatus(_A)
class _QosTrafficStatisticsBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock5Priority_Type.__name__=_B
_QosTrafficStatisticsBlock5Priority_Object=MibTableColumn
qosTrafficStatisticsBlock5Priority=_QosTrafficStatisticsBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,17),_QosTrafficStatisticsBlock5Priority_Type())
qosTrafficStatisticsBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock5Priority.setStatus(_A)
class _QosTrafficStatisticsBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock6Priority_Type.__name__=_B
_QosTrafficStatisticsBlock6Priority_Object=MibTableColumn
qosTrafficStatisticsBlock6Priority=_QosTrafficStatisticsBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,18),_QosTrafficStatisticsBlock6Priority_Type())
qosTrafficStatisticsBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock6Priority.setStatus(_A)
class _QosTrafficStatisticsBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock7Priority_Type.__name__=_B
_QosTrafficStatisticsBlock7Priority_Object=MibTableColumn
qosTrafficStatisticsBlock7Priority=_QosTrafficStatisticsBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,19),_QosTrafficStatisticsBlock7Priority_Type())
qosTrafficStatisticsBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock7Priority.setStatus(_A)
class _QosTrafficStatisticsBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock8Priority_Type.__name__=_B
_QosTrafficStatisticsBlock8Priority_Object=MibTableColumn
qosTrafficStatisticsBlock8Priority=_QosTrafficStatisticsBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,20),_QosTrafficStatisticsBlock8Priority_Type())
qosTrafficStatisticsBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock8Priority.setStatus(_A)
class _QosTrafficStatisticsBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock9Priority_Type.__name__=_B
_QosTrafficStatisticsBlock9Priority_Object=MibTableColumn
qosTrafficStatisticsBlock9Priority=_QosTrafficStatisticsBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,21),_QosTrafficStatisticsBlock9Priority_Type())
qosTrafficStatisticsBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock9Priority.setStatus(_A)
class _QosTrafficStatisticsBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock10Priority_Type.__name__=_B
_QosTrafficStatisticsBlock10Priority_Object=MibTableColumn
qosTrafficStatisticsBlock10Priority=_QosTrafficStatisticsBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,22),_QosTrafficStatisticsBlock10Priority_Type())
qosTrafficStatisticsBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock10Priority.setStatus(_A)
class _QosTrafficStatisticsBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficStatisticsBlock11Priority_Type.__name__=_B
_QosTrafficStatisticsBlock11Priority_Object=MibTableColumn
qosTrafficStatisticsBlock11Priority=_QosTrafficStatisticsBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,20,1,23),_QosTrafficStatisticsBlock11Priority_Type())
qosTrafficStatisticsBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficStatisticsBlock11Priority.setStatus(_A)
_QosLineRateTable_Object=MibTable
qosLineRateTable=_QosLineRateTable_Object((1,3,6,1,4,1,13464,1,2,4,4,21))
if mibBuilder.loadTexts:qosLineRateTable.setStatus(_A)
_QosLineRateEntry_Object=MibTableRow
qosLineRateEntry=_QosLineRateEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,21,1))
qosLineRateEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:qosLineRateEntry.setStatus(_A)
class _QosLineRateInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_QosLineRateInterface_Type.__name__=_B
_QosLineRateInterface_Object=MibTableColumn
qosLineRateInterface=_QosLineRateInterface_Object((1,3,6,1,4,1,13464,1,2,4,4,21,1,1),_QosLineRateInterface_Type())
qosLineRateInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:qosLineRateInterface.setStatus(_A)
class _QosLineRateTargetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosLineRateTargetRate_Type.__name__=_B
_QosLineRateTargetRate_Object=MibTableColumn
qosLineRateTargetRate=_QosLineRateTargetRate_Object((1,3,6,1,4,1,13464,1,2,4,4,21,1,2),_QosLineRateTargetRate_Type())
qosLineRateTargetRate.setMaxAccess(_D)
if mibBuilder.loadTexts:qosLineRateTargetRate.setStatus(_A)
_QosTrafficCopyToCpuTable_Object=MibTable
qosTrafficCopyToCpuTable=_QosTrafficCopyToCpuTable_Object((1,3,6,1,4,1,13464,1,2,4,4,22))
if mibBuilder.loadTexts:qosTrafficCopyToCpuTable.setStatus(_A)
_QosTrafficCopyToCpuEntry_Object=MibTableRow
qosTrafficCopyToCpuEntry=_QosTrafficCopyToCpuEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1))
qosTrafficCopyToCpuEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:qosTrafficCopyToCpuEntry.setStatus(_A)
_QosTrafficCopyToCpuIndex_Type=Integer32
_QosTrafficCopyToCpuIndex_Object=MibTableColumn
qosTrafficCopyToCpuIndex=_QosTrafficCopyToCpuIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,1),_QosTrafficCopyToCpuIndex_Type())
qosTrafficCopyToCpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuIndex.setStatus(_A)
class _QosTrafficCopyToCpuUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficCopyToCpuUserGroupName_Type.__name__=_E
_QosTrafficCopyToCpuUserGroupName_Object=MibTableColumn
qosTrafficCopyToCpuUserGroupName=_QosTrafficCopyToCpuUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,2),_QosTrafficCopyToCpuUserGroupName_Type())
qosTrafficCopyToCpuUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficCopyToCpuUserGroupName.setStatus(_A)
class _QosTrafficCopyToCpuUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficCopyToCpuUserGroupSubitem_Type.__name__=_B
_QosTrafficCopyToCpuUserGroupSubitem_Object=MibTableColumn
qosTrafficCopyToCpuUserGroupSubitem=_QosTrafficCopyToCpuUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,3),_QosTrafficCopyToCpuUserGroupSubitem_Type())
qosTrafficCopyToCpuUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficCopyToCpuUserGroupSubitem.setStatus(_A)
class _QosTrafficCopyToCpuIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficCopyToCpuIpGroupName_Type.__name__=_E
_QosTrafficCopyToCpuIpGroupName_Object=MibTableColumn
qosTrafficCopyToCpuIpGroupName=_QosTrafficCopyToCpuIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,4),_QosTrafficCopyToCpuIpGroupName_Type())
qosTrafficCopyToCpuIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficCopyToCpuIpGroupName.setStatus(_A)
class _QosTrafficCopyToCpuIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficCopyToCpuIpGroupSubitem_Type.__name__=_B
_QosTrafficCopyToCpuIpGroupSubitem_Object=MibTableColumn
qosTrafficCopyToCpuIpGroupSubitem=_QosTrafficCopyToCpuIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,5),_QosTrafficCopyToCpuIpGroupSubitem_Type())
qosTrafficCopyToCpuIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficCopyToCpuIpGroupSubitem.setStatus(_A)
class _QosTrafficCopyToCpuLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficCopyToCpuLinkGroupName_Type.__name__=_E
_QosTrafficCopyToCpuLinkGroupName_Object=MibTableColumn
qosTrafficCopyToCpuLinkGroupName=_QosTrafficCopyToCpuLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,6),_QosTrafficCopyToCpuLinkGroupName_Type())
qosTrafficCopyToCpuLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficCopyToCpuLinkGroupName.setStatus(_A)
class _QosTrafficCopyToCpuLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficCopyToCpuLinkGroupSubitem_Type.__name__=_B
_QosTrafficCopyToCpuLinkGroupSubitem_Object=MibTableColumn
qosTrafficCopyToCpuLinkGroupSubitem=_QosTrafficCopyToCpuLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,7),_QosTrafficCopyToCpuLinkGroupSubitem_Type())
qosTrafficCopyToCpuLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficCopyToCpuLinkGroupSubitem.setStatus(_A)
class _QosTrafficCopyToCpuBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock0Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock0Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock0Priority=_QosTrafficCopyToCpuBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,8),_QosTrafficCopyToCpuBlock0Priority_Type())
qosTrafficCopyToCpuBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock0Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock1Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock1Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock1Priority=_QosTrafficCopyToCpuBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,9),_QosTrafficCopyToCpuBlock1Priority_Type())
qosTrafficCopyToCpuBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock1Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock2Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock2Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock2Priority=_QosTrafficCopyToCpuBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,10),_QosTrafficCopyToCpuBlock2Priority_Type())
qosTrafficCopyToCpuBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock2Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock3Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock3Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock3Priority=_QosTrafficCopyToCpuBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,11),_QosTrafficCopyToCpuBlock3Priority_Type())
qosTrafficCopyToCpuBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock3Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock4Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock4Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock4Priority=_QosTrafficCopyToCpuBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,12),_QosTrafficCopyToCpuBlock4Priority_Type())
qosTrafficCopyToCpuBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock4Priority.setStatus(_A)
class _QosTrafficCopyToCpuConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosTrafficCopyToCpuConfigSequence_Type.__name__=_B
_QosTrafficCopyToCpuConfigSequence_Object=MibTableColumn
qosTrafficCopyToCpuConfigSequence=_QosTrafficCopyToCpuConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,13),_QosTrafficCopyToCpuConfigSequence_Type())
qosTrafficCopyToCpuConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuConfigSequence.setStatus(_A)
_QosTrafficCopyToCpuRunning_Type=TruthValue
_QosTrafficCopyToCpuRunning_Object=MibTableColumn
qosTrafficCopyToCpuRunning=_QosTrafficCopyToCpuRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,14),_QosTrafficCopyToCpuRunning_Type())
qosTrafficCopyToCpuRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuRunning.setStatus(_A)
_QosTrafficCopyToCpuRowStatus_Type=RowStatus
_QosTrafficCopyToCpuRowStatus_Object=MibTableColumn
qosTrafficCopyToCpuRowStatus=_QosTrafficCopyToCpuRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,15),_QosTrafficCopyToCpuRowStatus_Type())
qosTrafficCopyToCpuRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficCopyToCpuRowStatus.setStatus(_A)
class _QosTrafficCopyToCpuBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock5Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock5Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock5Priority=_QosTrafficCopyToCpuBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,16),_QosTrafficCopyToCpuBlock5Priority_Type())
qosTrafficCopyToCpuBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock5Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock6Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock6Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock6Priority=_QosTrafficCopyToCpuBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,17),_QosTrafficCopyToCpuBlock6Priority_Type())
qosTrafficCopyToCpuBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock6Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock7Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock7Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock7Priority=_QosTrafficCopyToCpuBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,18),_QosTrafficCopyToCpuBlock7Priority_Type())
qosTrafficCopyToCpuBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock7Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock8Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock8Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock8Priority=_QosTrafficCopyToCpuBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,19),_QosTrafficCopyToCpuBlock8Priority_Type())
qosTrafficCopyToCpuBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock8Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock9Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock9Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock9Priority=_QosTrafficCopyToCpuBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,20),_QosTrafficCopyToCpuBlock9Priority_Type())
qosTrafficCopyToCpuBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock9Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock10Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock10Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock10Priority=_QosTrafficCopyToCpuBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,21),_QosTrafficCopyToCpuBlock10Priority_Type())
qosTrafficCopyToCpuBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock10Priority.setStatus(_A)
class _QosTrafficCopyToCpuBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficCopyToCpuBlock11Priority_Type.__name__=_B
_QosTrafficCopyToCpuBlock11Priority_Object=MibTableColumn
qosTrafficCopyToCpuBlock11Priority=_QosTrafficCopyToCpuBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,22,1,22),_QosTrafficCopyToCpuBlock11Priority_Type())
qosTrafficCopyToCpuBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficCopyToCpuBlock11Priority.setStatus(_A)
_QaclAppPortIsolationGroup_ObjectIdentity=ObjectIdentity
qaclAppPortIsolationGroup=_QaclAppPortIsolationGroup_ObjectIdentity((1,3,6,1,4,1,13464,1,2,4,4,23))
_QaclAppPortIsolationDownLinkPorts_Type=PortList
_QaclAppPortIsolationDownLinkPorts_Object=MibScalar
qaclAppPortIsolationDownLinkPorts=_QaclAppPortIsolationDownLinkPorts_Object((1,3,6,1,4,1,13464,1,2,4,4,23,1),_QaclAppPortIsolationDownLinkPorts_Type())
qaclAppPortIsolationDownLinkPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:qaclAppPortIsolationDownLinkPorts.setStatus(_A)
_StormControlTable_Object=MibTable
stormControlTable=_StormControlTable_Object((1,3,6,1,4,1,13464,1,2,4,4,24))
if mibBuilder.loadTexts:stormControlTable.setStatus(_A)
_StormControlEntry_Object=MibTableRow
stormControlEntry=_StormControlEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,24,1))
stormControlEntry.setIndexNames((0,_F,_u),(0,_F,_v))
if mibBuilder.loadTexts:stormControlEntry.setStatus(_A)
class _StormControlInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_StormControlInterface_Type.__name__=_B
_StormControlInterface_Object=MibTableColumn
stormControlInterface=_StormControlInterface_Object((1,3,6,1,4,1,13464,1,2,4,4,24,1,1),_StormControlInterface_Type())
stormControlInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:stormControlInterface.setStatus(_A)
_StormControlType_Type=PacketFlowType
_StormControlType_Object=MibTableColumn
stormControlType=_StormControlType_Object((1,3,6,1,4,1,13464,1,2,4,4,24,1,2),_StormControlType_Type())
stormControlType.setMaxAccess(_C)
if mibBuilder.loadTexts:stormControlType.setStatus(_A)
class _StormControlTargetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_StormControlTargetRate_Type.__name__=_B
_StormControlTargetRate_Object=MibTableColumn
stormControlTargetRate=_StormControlTargetRate_Object((1,3,6,1,4,1,13464,1,2,4,4,24,1,3),_StormControlTargetRate_Type())
stormControlTargetRate.setMaxAccess(_D)
if mibBuilder.loadTexts:stormControlTargetRate.setStatus(_A)
_StormControlRowStatus_Type=RowStatus
_StormControlRowStatus_Object=MibTableColumn
stormControlRowStatus=_StormControlRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,24,1,4),_StormControlRowStatus_Type())
stormControlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:stormControlRowStatus.setStatus(_A)
_QosTrafficRewriteVlanTable_Object=MibTable
qosTrafficRewriteVlanTable=_QosTrafficRewriteVlanTable_Object((1,3,6,1,4,1,13464,1,2,4,4,25))
if mibBuilder.loadTexts:qosTrafficRewriteVlanTable.setStatus(_A)
_QosTrafficRewriteVlanEntry_Object=MibTableRow
qosTrafficRewriteVlanEntry=_QosTrafficRewriteVlanEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1))
qosTrafficRewriteVlanEntry.setIndexNames((0,_F,_w))
if mibBuilder.loadTexts:qosTrafficRewriteVlanEntry.setStatus(_A)
_QosTrafficRewriteVlanIndex_Type=Integer32
_QosTrafficRewriteVlanIndex_Object=MibTableColumn
qosTrafficRewriteVlanIndex=_QosTrafficRewriteVlanIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,1),_QosTrafficRewriteVlanIndex_Type())
qosTrafficRewriteVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanIndex.setStatus(_A)
class _QosTrafficRewriteVlanUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficRewriteVlanUserGroupName_Type.__name__=_E
_QosTrafficRewriteVlanUserGroupName_Object=MibTableColumn
qosTrafficRewriteVlanUserGroupName=_QosTrafficRewriteVlanUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,2),_QosTrafficRewriteVlanUserGroupName_Type())
qosTrafficRewriteVlanUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanUserGroupName.setStatus(_A)
class _QosTrafficRewriteVlanUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficRewriteVlanUserGroupSubitem_Type.__name__=_B
_QosTrafficRewriteVlanUserGroupSubitem_Object=MibTableColumn
qosTrafficRewriteVlanUserGroupSubitem=_QosTrafficRewriteVlanUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,3),_QosTrafficRewriteVlanUserGroupSubitem_Type())
qosTrafficRewriteVlanUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanUserGroupSubitem.setStatus(_A)
class _QosTrafficRewriteVlanIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficRewriteVlanIpGroupName_Type.__name__=_E
_QosTrafficRewriteVlanIpGroupName_Object=MibTableColumn
qosTrafficRewriteVlanIpGroupName=_QosTrafficRewriteVlanIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,4),_QosTrafficRewriteVlanIpGroupName_Type())
qosTrafficRewriteVlanIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanIpGroupName.setStatus(_A)
class _QosTrafficRewriteVlanIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficRewriteVlanIpGroupSubitem_Type.__name__=_B
_QosTrafficRewriteVlanIpGroupSubitem_Object=MibTableColumn
qosTrafficRewriteVlanIpGroupSubitem=_QosTrafficRewriteVlanIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,5),_QosTrafficRewriteVlanIpGroupSubitem_Type())
qosTrafficRewriteVlanIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanIpGroupSubitem.setStatus(_A)
class _QosTrafficRewriteVlanLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficRewriteVlanLinkGroupName_Type.__name__=_E
_QosTrafficRewriteVlanLinkGroupName_Object=MibTableColumn
qosTrafficRewriteVlanLinkGroupName=_QosTrafficRewriteVlanLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,6),_QosTrafficRewriteVlanLinkGroupName_Type())
qosTrafficRewriteVlanLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanLinkGroupName.setStatus(_A)
class _QosTrafficRewriteVlanLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficRewriteVlanLinkGroupSubitem_Type.__name__=_B
_QosTrafficRewriteVlanLinkGroupSubitem_Object=MibTableColumn
qosTrafficRewriteVlanLinkGroupSubitem=_QosTrafficRewriteVlanLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,7),_QosTrafficRewriteVlanLinkGroupSubitem_Type())
qosTrafficRewriteVlanLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanLinkGroupSubitem.setStatus(_A)
class _QosTrafficRewriteVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_QosTrafficRewriteVlanVid_Type.__name__=_B
_QosTrafficRewriteVlanVid_Object=MibTableColumn
qosTrafficRewriteVlanVid=_QosTrafficRewriteVlanVid_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,8),_QosTrafficRewriteVlanVid_Type())
qosTrafficRewriteVlanVid.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficRewriteVlanVid.setStatus(_A)
class _QosTrafficRewriteVlanBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock0Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock0Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock0Priority=_QosTrafficRewriteVlanBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,9),_QosTrafficRewriteVlanBlock0Priority_Type())
qosTrafficRewriteVlanBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock0Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock1Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock1Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock1Priority=_QosTrafficRewriteVlanBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,10),_QosTrafficRewriteVlanBlock1Priority_Type())
qosTrafficRewriteVlanBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock1Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock2Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock2Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock2Priority=_QosTrafficRewriteVlanBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,11),_QosTrafficRewriteVlanBlock2Priority_Type())
qosTrafficRewriteVlanBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock2Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock3Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock3Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock3Priority=_QosTrafficRewriteVlanBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,12),_QosTrafficRewriteVlanBlock3Priority_Type())
qosTrafficRewriteVlanBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock3Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock4Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock4Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock4Priority=_QosTrafficRewriteVlanBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,13),_QosTrafficRewriteVlanBlock4Priority_Type())
qosTrafficRewriteVlanBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock4Priority.setStatus(_A)
class _QosTrafficRewriteVlanConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosTrafficRewriteVlanConfigSequence_Type.__name__=_B
_QosTrafficRewriteVlanConfigSequence_Object=MibTableColumn
qosTrafficRewriteVlanConfigSequence=_QosTrafficRewriteVlanConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,14),_QosTrafficRewriteVlanConfigSequence_Type())
qosTrafficRewriteVlanConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanConfigSequence.setStatus(_A)
_QosTrafficRewriteVlanRunning_Type=TruthValue
_QosTrafficRewriteVlanRunning_Object=MibTableColumn
qosTrafficRewriteVlanRunning=_QosTrafficRewriteVlanRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,15),_QosTrafficRewriteVlanRunning_Type())
qosTrafficRewriteVlanRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanRunning.setStatus(_A)
_QosTrafficRewriteVlanRowStatus_Type=RowStatus
_QosTrafficRewriteVlanRowStatus_Object=MibTableColumn
qosTrafficRewriteVlanRowStatus=_QosTrafficRewriteVlanRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,16),_QosTrafficRewriteVlanRowStatus_Type())
qosTrafficRewriteVlanRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficRewriteVlanRowStatus.setStatus(_A)
class _QosTrafficRewriteVlanBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock5Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock5Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock5Priority=_QosTrafficRewriteVlanBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,17),_QosTrafficRewriteVlanBlock5Priority_Type())
qosTrafficRewriteVlanBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock5Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock6Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock6Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock6Priority=_QosTrafficRewriteVlanBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,18),_QosTrafficRewriteVlanBlock6Priority_Type())
qosTrafficRewriteVlanBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock6Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock7Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock7Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock7Priority=_QosTrafficRewriteVlanBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,19),_QosTrafficRewriteVlanBlock7Priority_Type())
qosTrafficRewriteVlanBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock7Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock8Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock8Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock8Priority=_QosTrafficRewriteVlanBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,20),_QosTrafficRewriteVlanBlock8Priority_Type())
qosTrafficRewriteVlanBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock8Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock9Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock9Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock9Priority=_QosTrafficRewriteVlanBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,21),_QosTrafficRewriteVlanBlock9Priority_Type())
qosTrafficRewriteVlanBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock9Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock10Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock10Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock10Priority=_QosTrafficRewriteVlanBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,22),_QosTrafficRewriteVlanBlock10Priority_Type())
qosTrafficRewriteVlanBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock10Priority.setStatus(_A)
class _QosTrafficRewriteVlanBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficRewriteVlanBlock11Priority_Type.__name__=_B
_QosTrafficRewriteVlanBlock11Priority_Object=MibTableColumn
qosTrafficRewriteVlanBlock11Priority=_QosTrafficRewriteVlanBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,25,1,23),_QosTrafficRewriteVlanBlock11Priority_Type())
qosTrafficRewriteVlanBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficRewriteVlanBlock11Priority.setStatus(_A)
_QosTrafficInsertVlanTable_Object=MibTable
qosTrafficInsertVlanTable=_QosTrafficInsertVlanTable_Object((1,3,6,1,4,1,13464,1,2,4,4,26))
if mibBuilder.loadTexts:qosTrafficInsertVlanTable.setStatus(_A)
_QosTrafficInsertVlanEntry_Object=MibTableRow
qosTrafficInsertVlanEntry=_QosTrafficInsertVlanEntry_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1))
qosTrafficInsertVlanEntry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:qosTrafficInsertVlanEntry.setStatus(_A)
_QosTrafficInsertVlanIndex_Type=Integer32
_QosTrafficInsertVlanIndex_Object=MibTableColumn
qosTrafficInsertVlanIndex=_QosTrafficInsertVlanIndex_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,1),_QosTrafficInsertVlanIndex_Type())
qosTrafficInsertVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanIndex.setStatus(_A)
class _QosTrafficInsertVlanUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficInsertVlanUserGroupName_Type.__name__=_E
_QosTrafficInsertVlanUserGroupName_Object=MibTableColumn
qosTrafficInsertVlanUserGroupName=_QosTrafficInsertVlanUserGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,2),_QosTrafficInsertVlanUserGroupName_Type())
qosTrafficInsertVlanUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanUserGroupName.setStatus(_A)
class _QosTrafficInsertVlanUserGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficInsertVlanUserGroupSubitem_Type.__name__=_B
_QosTrafficInsertVlanUserGroupSubitem_Object=MibTableColumn
qosTrafficInsertVlanUserGroupSubitem=_QosTrafficInsertVlanUserGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,3),_QosTrafficInsertVlanUserGroupSubitem_Type())
qosTrafficInsertVlanUserGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanUserGroupSubitem.setStatus(_A)
class _QosTrafficInsertVlanIpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficInsertVlanIpGroupName_Type.__name__=_E
_QosTrafficInsertVlanIpGroupName_Object=MibTableColumn
qosTrafficInsertVlanIpGroupName=_QosTrafficInsertVlanIpGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,4),_QosTrafficInsertVlanIpGroupName_Type())
qosTrafficInsertVlanIpGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanIpGroupName.setStatus(_A)
class _QosTrafficInsertVlanIpGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficInsertVlanIpGroupSubitem_Type.__name__=_B
_QosTrafficInsertVlanIpGroupSubitem_Object=MibTableColumn
qosTrafficInsertVlanIpGroupSubitem=_QosTrafficInsertVlanIpGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,5),_QosTrafficInsertVlanIpGroupSubitem_Type())
qosTrafficInsertVlanIpGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanIpGroupSubitem.setStatus(_A)
class _QosTrafficInsertVlanLinkGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QosTrafficInsertVlanLinkGroupName_Type.__name__=_E
_QosTrafficInsertVlanLinkGroupName_Object=MibTableColumn
qosTrafficInsertVlanLinkGroupName=_QosTrafficInsertVlanLinkGroupName_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,6),_QosTrafficInsertVlanLinkGroupName_Type())
qosTrafficInsertVlanLinkGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanLinkGroupName.setStatus(_A)
class _QosTrafficInsertVlanLinkGroupSubitem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_QosTrafficInsertVlanLinkGroupSubitem_Type.__name__=_B
_QosTrafficInsertVlanLinkGroupSubitem_Object=MibTableColumn
qosTrafficInsertVlanLinkGroupSubitem=_QosTrafficInsertVlanLinkGroupSubitem_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,7),_QosTrafficInsertVlanLinkGroupSubitem_Type())
qosTrafficInsertVlanLinkGroupSubitem.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanLinkGroupSubitem.setStatus(_A)
class _QosTrafficInsertVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_QosTrafficInsertVlanVid_Type.__name__=_B
_QosTrafficInsertVlanVid_Object=MibTableColumn
qosTrafficInsertVlanVid=_QosTrafficInsertVlanVid_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,8),_QosTrafficInsertVlanVid_Type())
qosTrafficInsertVlanVid.setMaxAccess(_D)
if mibBuilder.loadTexts:qosTrafficInsertVlanVid.setStatus(_A)
class _QosTrafficInsertVlanBlock0Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock0Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock0Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock0Priority=_QosTrafficInsertVlanBlock0Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,9),_QosTrafficInsertVlanBlock0Priority_Type())
qosTrafficInsertVlanBlock0Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock0Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock1Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock1Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock1Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock1Priority=_QosTrafficInsertVlanBlock1Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,10),_QosTrafficInsertVlanBlock1Priority_Type())
qosTrafficInsertVlanBlock1Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock1Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock2Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock2Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock2Priority=_QosTrafficInsertVlanBlock2Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,11),_QosTrafficInsertVlanBlock2Priority_Type())
qosTrafficInsertVlanBlock2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock2Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock3Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock3Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock3Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock3Priority=_QosTrafficInsertVlanBlock3Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,12),_QosTrafficInsertVlanBlock3Priority_Type())
qosTrafficInsertVlanBlock3Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock3Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock4Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock4Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock4Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock4Priority=_QosTrafficInsertVlanBlock4Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,13),_QosTrafficInsertVlanBlock4Priority_Type())
qosTrafficInsertVlanBlock4Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock4Priority.setStatus(_A)
class _QosTrafficInsertVlanConfigSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosTrafficInsertVlanConfigSequence_Type.__name__=_B
_QosTrafficInsertVlanConfigSequence_Object=MibTableColumn
qosTrafficInsertVlanConfigSequence=_QosTrafficInsertVlanConfigSequence_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,14),_QosTrafficInsertVlanConfigSequence_Type())
qosTrafficInsertVlanConfigSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanConfigSequence.setStatus(_A)
_QosTrafficInsertVlanRunning_Type=TruthValue
_QosTrafficInsertVlanRunning_Object=MibTableColumn
qosTrafficInsertVlanRunning=_QosTrafficInsertVlanRunning_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,15),_QosTrafficInsertVlanRunning_Type())
qosTrafficInsertVlanRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanRunning.setStatus(_A)
_QosTrafficInsertVlanRowStatus_Type=RowStatus
_QosTrafficInsertVlanRowStatus_Object=MibTableColumn
qosTrafficInsertVlanRowStatus=_QosTrafficInsertVlanRowStatus_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,16),_QosTrafficInsertVlanRowStatus_Type())
qosTrafficInsertVlanRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosTrafficInsertVlanRowStatus.setStatus(_A)
class _QosTrafficInsertVlanBlock5Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock5Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock5Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock5Priority=_QosTrafficInsertVlanBlock5Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,17),_QosTrafficInsertVlanBlock5Priority_Type())
qosTrafficInsertVlanBlock5Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock5Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock6Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock6Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock6Priority=_QosTrafficInsertVlanBlock6Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,18),_QosTrafficInsertVlanBlock6Priority_Type())
qosTrafficInsertVlanBlock6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock6Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock7Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock7Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock7Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock7Priority=_QosTrafficInsertVlanBlock7Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,19),_QosTrafficInsertVlanBlock7Priority_Type())
qosTrafficInsertVlanBlock7Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock7Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock8Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock8Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock8Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock8Priority=_QosTrafficInsertVlanBlock8Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,20),_QosTrafficInsertVlanBlock8Priority_Type())
qosTrafficInsertVlanBlock8Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock8Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock9Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock9Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock9Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock9Priority=_QosTrafficInsertVlanBlock9Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,21),_QosTrafficInsertVlanBlock9Priority_Type())
qosTrafficInsertVlanBlock9Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock9Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock10Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock10Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock10Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock10Priority=_QosTrafficInsertVlanBlock10Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,22),_QosTrafficInsertVlanBlock10Priority_Type())
qosTrafficInsertVlanBlock10Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock10Priority.setStatus(_A)
class _QosTrafficInsertVlanBlock11Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosTrafficInsertVlanBlock11Priority_Type.__name__=_B
_QosTrafficInsertVlanBlock11Priority_Object=MibTableColumn
qosTrafficInsertVlanBlock11Priority=_QosTrafficInsertVlanBlock11Priority_Object((1,3,6,1,4,1,13464,1,2,4,4,26,1,23),_QosTrafficInsertVlanBlock11Priority_Type())
qosTrafficInsertVlanBlock11Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTrafficInsertVlanBlock11Priority.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'AdminStatus':AdminStatus,'Action':Action,'Dscp':Dscp,'AclType':AclType,'PacketFlowType':PacketFlowType,'gbnL2QACL':gbnL2QACL,'qosQueueSchedulerGroup':qosQueueSchedulerGroup,'qosWrrQueue1Weight':qosWrrQueue1Weight,'qosWrrQueue2Weight':qosWrrQueue2Weight,'qosWrrQueue3Weight':qosWrrQueue3Weight,'qosWrrQueue4Weight':qosWrrQueue4Weight,'qosWrrMaxDelayValue':qosWrrMaxDelayValue,'qosQueueSchedulerMode':qosQueueSchedulerMode,'qosWrrQueue5Weight':qosWrrQueue5Weight,'qosWrrQueue6Weight':qosWrrQueue6Weight,'qosWrrQueue7Weight':qosWrrQueue7Weight,'qosWrrQueue8Weight':qosWrrQueue8Weight,'aclNumTable':aclNumTable,'aclNumEntry':aclNumEntry,_I:aclNumNumber,'aclNumType':aclNumType,'aclNumMatchOrder':aclNumMatchOrder,'aclNumTotleSubitems':aclNumTotleSubitems,'aclNumRowStatus':aclNumRowStatus,'aclNumStdSubitemTable':aclNumStdSubitemTable,'aclNumStdSubitemEntry':aclNumStdSubitemEntry,_K:aclNumStdNum,_L:aclNumStdSubNum,'aclNumStdSubitemAdminStatus':aclNumStdSubitemAdminStatus,'aclNumStdSubitemAction':aclNumStdSubitemAction,'aclNumStdSubitemSrcAddr':aclNumStdSubitemSrcAddr,'aclNumStdSubitemSrcAddrWldmsk':aclNumStdSubitemSrcAddrWldmsk,'aclNumStdFragments':aclNumStdFragments,'aclNumStdTimeRange':aclNumStdTimeRange,'aclNumStdSubitemRowStatus':aclNumStdSubitemRowStatus,'aclNumExdSubitemTable':aclNumExdSubitemTable,'aclNumExdSubitemEntry':aclNumExdSubitemEntry,_M:aclNumExdNum,_N:aclNumExdSubNum,'aclNumExdSubitemAdminStatus':aclNumExdSubitemAdminStatus,'aclNumExdSubitemAction':aclNumExdSubitemAction,'aclNumExdSubitemProtocal':aclNumExdSubitemProtocal,'aclNumExdSubitemSrcAddr':aclNumExdSubitemSrcAddr,'aclNumExdSubitemSrcAddrWldmsk':aclNumExdSubitemSrcAddrWldmsk,'aclNumExdSubitemDstAddr':aclNumExdSubitemDstAddr,'aclNumExdSubitemDstAddrWldmsk':aclNumExdSubitemDstAddrWldmsk,'aclNumExdSubitemSrcPort':aclNumExdSubitemSrcPort,'aclNumExdSubitemSrcPortWldmsk':aclNumExdSubitemSrcPortWldmsk,'aclNumExdSubitemDstPort':aclNumExdSubitemDstPort,'aclNumExdSubitemDstPortWldmsk':aclNumExdSubitemDstPortWldmsk,'aclNumExdSubitemIcmpType':aclNumExdSubitemIcmpType,'aclNumExdSubitemIcmpCode':aclNumExdSubitemIcmpCode,'aclNumExdSubitemTcpEstablished':aclNumExdSubitemTcpEstablished,'aclNumExdSubitemPrecedence':aclNumExdSubitemPrecedence,'aclNumExdSubitemTos':aclNumExdSubitemTos,'aclNumExdSubitemDscp':aclNumExdSubitemDscp,'aclNumExdSubitemFragments':aclNumExdSubitemFragments,'aclNumExdSubitemTimeRange':aclNumExdSubitemTimeRange,'aclNumExdSubitemRowStatus':aclNumExdSubitemRowStatus,'aclNumLnkSubitemTable':aclNumLnkSubitemTable,'aclNumLnkSubitemEntry':aclNumLnkSubitemEntry,_O:aclNumLnkNum,_P:aclNumLnkSubNum,'aclNumLnkSubitemAdminStatus':aclNumLnkSubitemAdminStatus,'aclNumLnkSubitemAction':aclNumLnkSubitemAction,'aclNumLnkSubitemProtocal':aclNumLnkSubitemProtocal,'aclNumLnkSubitemCos':aclNumLnkSubitemCos,'aclNumLnkSubitemSrcVlanID':aclNumLnkSubitemSrcVlanID,'aclNumLnkSubitemSrcMacAddr':aclNumLnkSubitemSrcMacAddr,'aclNumLnkSubitemSrcMacWldmsk':aclNumLnkSubitemSrcMacWldmsk,'aclNumLnkSubitemDstMacAddr':aclNumLnkSubitemDstMacAddr,'aclNumLnkSubitemDstMacWldmsk':aclNumLnkSubitemDstMacWldmsk,'aclNumLnkSubitemSrcPortNum':aclNumLnkSubitemSrcPortNum,'aclNumLnkSubitemDstPortNum':aclNumLnkSubitemDstPortNum,'aclNumLnkSubitemTimeRange':aclNumLnkSubitemTimeRange,'aclNumLnkSubitemRowStatus':aclNumLnkSubitemRowStatus,'aclNumLnkSubitemSrcEndVlanID':aclNumLnkSubitemSrcEndVlanID,'aclNumUserSubitemTable':aclNumUserSubitemTable,'aclNumUserSubitemEntry':aclNumUserSubitemEntry,_Q:aclNumUserNum,_R:aclNumUserSubNum,'aclNumUserSubitemAdminStatus':aclNumUserSubitemAdminStatus,'aclNumUserSubitemAction':aclNumUserSubitemAction,'aclNumUserSubitemSrcPortNum':aclNumUserSubitemSrcPortNum,'aclNumUserSubitemDstPortNum':aclNumUserSubitemDstPortNum,'aclNumUserSubitemRule':aclNumUserSubitemRule,'aclNumUserSubitemMask':aclNumUserSubitemMask,'aclNumUserSubitemSrcVlanID':aclNumUserSubitemSrcVlanID,'aclNumUserTimeRange':aclNumUserTimeRange,'aclNumUserSubitemRowStatus':aclNumUserSubitemRowStatus,'aclNamedTable':aclNamedTable,'aclNamedEntry':aclNamedEntry,_S:aclNamedName,'aclNamedType':aclNamedType,'aclNamedMatchOrder':aclNamedMatchOrder,'aclNamedTotleSubitems':aclNamedTotleSubitems,'aclNamedRowStatus':aclNamedRowStatus,'aclNamedStdSubitemTable':aclNamedStdSubitemTable,'aclNamedStdSubitemEntry':aclNamedStdSubitemEntry,_T:aclNamedStdName,_U:aclNamedStdSubNum,'aclNamedStdSubitemAdminStatus':aclNamedStdSubitemAdminStatus,'aclNamedStdSubitemAction':aclNamedStdSubitemAction,'aclNamedStdSubitemSrcAddr':aclNamedStdSubitemSrcAddr,'aclNamedStdSubitemSrcAddrWldmsk':aclNamedStdSubitemSrcAddrWldmsk,'aclNamedStdFragments':aclNamedStdFragments,'aclNamedStdTimeRange':aclNamedStdTimeRange,'aclNamedStdSubitemRowStatus':aclNamedStdSubitemRowStatus,'aclNamedExdSubitemTable':aclNamedExdSubitemTable,'aclNamedExdSubitemEntry':aclNamedExdSubitemEntry,_V:aclNamedExdName,_W:aclNamedExdSubNum,'aclNamedExdSubitemAdminStatus':aclNamedExdSubitemAdminStatus,'aclNamedExdSubitemAction':aclNamedExdSubitemAction,'aclNamedExdSubitemProtocal':aclNamedExdSubitemProtocal,'aclNamedExdSubitemSrcAddr':aclNamedExdSubitemSrcAddr,'aclNamedExdSubitemSrcAddrWldmsk':aclNamedExdSubitemSrcAddrWldmsk,'aclNamedExdSubitemDstAddr':aclNamedExdSubitemDstAddr,'aclNamedExdSubitemDstAddrWldmsk':aclNamedExdSubitemDstAddrWldmsk,'aclNamedExdSubitemSrcPort':aclNamedExdSubitemSrcPort,'aclNamedExdSubitemSrcPortWldmsk':aclNamedExdSubitemSrcPortWldmsk,'aclNamedExdSubitemDstPort':aclNamedExdSubitemDstPort,'aclNamedExdSubitemDstPortWldmsk':aclNamedExdSubitemDstPortWldmsk,'aclNamedExdSubitemIcmpType':aclNamedExdSubitemIcmpType,'aclNamedExdSubitemIcmpCode':aclNamedExdSubitemIcmpCode,'aclNamedExdSubitemTcpEstablished':aclNamedExdSubitemTcpEstablished,'aclNamedExdSubitemPrecedence':aclNamedExdSubitemPrecedence,'aclNamedExdSubitemTos':aclNamedExdSubitemTos,'aclNamedExdSubitemDscp':aclNamedExdSubitemDscp,'aclNamedExdSubitemFragments':aclNamedExdSubitemFragments,'aclNamedExdSubitemTimeRange':aclNamedExdSubitemTimeRange,'aclNamedExdSubitemRowStatus':aclNamedExdSubitemRowStatus,'aclNamedLnkSubitemTable':aclNamedLnkSubitemTable,'aclNamedLnkSubitemEntry':aclNamedLnkSubitemEntry,_X:aclNamedLnkName,_Y:aclNamedLnkSubNum,'aclNamedLnkSubitemAdminStatus':aclNamedLnkSubitemAdminStatus,'aclNamedLnkSubitemAction':aclNamedLnkSubitemAction,'aclNamedLnkSubitemProtocal':aclNamedLnkSubitemProtocal,'aclNamedLnkSubitemCos':aclNamedLnkSubitemCos,'aclNamedLnkSubitemSrcVlanID':aclNamedLnkSubitemSrcVlanID,'aclNamedLnkSubitemSrcMacAddr':aclNamedLnkSubitemSrcMacAddr,'aclNamedLnkSubitemSrcMacWldmsk':aclNamedLnkSubitemSrcMacWldmsk,'aclNamedLnkSubitemDstMacAddr':aclNamedLnkSubitemDstMacAddr,'aclNamedLnkSubitemDstMacWldmsk':aclNamedLnkSubitemDstMacWldmsk,'aclNamedLnkSubitemSrcPortNum':aclNamedLnkSubitemSrcPortNum,'aclNamedLnkSubitemDstPortNum':aclNamedLnkSubitemDstPortNum,'aclNamedLnkSubitemTimeRange':aclNamedLnkSubitemTimeRange,'aclNamedLnkSubitemRowStatus':aclNamedLnkSubitemRowStatus,'aclNamedLnkSubitemSrcEndVlanID':aclNamedLnkSubitemSrcEndVlanID,'aclNamedUserSubitemTable':aclNamedUserSubitemTable,'aclNamedUserSubitemEntry':aclNamedUserSubitemEntry,_Z:aclNamedUserName,_a:aclNamedUserSubNum,'aclNamedUserSubitemAdminStatus':aclNamedUserSubitemAdminStatus,'aclNamedUserSubitemAction':aclNamedUserSubitemAction,'aclNamedUserSubitemSrcPortNum':aclNamedUserSubitemSrcPortNum,'aclNamedUserSubitemDstPortNum':aclNamedUserSubitemDstPortNum,'aclNamedUserSubitemRule':aclNamedUserSubitemRule,'aclNamedUserSubitemMask':aclNamedUserSubitemMask,'aclNamedUserSubitemSrcVlanID':aclNamedUserSubitemSrcVlanID,'aclNamedUserTimeRange':aclNamedUserTimeRange,'aclNamedUserSubitemRowStatus':aclNamedUserSubitemRowStatus,'aclTimeRangeTable':aclTimeRangeTable,'aclTimeRangeEntry':aclTimeRangeEntry,_b:aclTimeRangeName,'aclTimeRangeTotleAbsolutes':aclTimeRangeTotleAbsolutes,'aclTimeRangeTotlePeriods':aclTimeRangeTotlePeriods,'aclTimeRangeActive':aclTimeRangeActive,'aclTimeRangeRowStatus':aclTimeRangeRowStatus,'aclTimeRangeAbsoluteTable':aclTimeRangeAbsoluteTable,'aclTimeRangeAbsoluteEntry':aclTimeRangeAbsoluteEntry,_c:aclTimeRangeAbsoluteName,_d:aclTimeRangeAbsoluteStartTime,_e:aclTimeRangeAbsoluteEndTime,'aclTimeRangeAbsoluteRowStatus':aclTimeRangeAbsoluteRowStatus,'aclTimeRangePeriodTable':aclTimeRangePeriodTable,'aclTimeRangePeriodEntry':aclTimeRangePeriodEntry,_f:aclTimeRangePeriodName,_g:aclTimeRangePeriodStartWeekDay,_h:aclTimeRangePeriodStartHour,_i:aclTimeRangePeriodStartMin,_j:aclTimeRangePeriodEndWeekDay,_k:aclTimeRangePeriodEndHour,_l:aclTimeRangePeriodEndMin,'aclTimeRangePeriodRowStatus':aclTimeRangePeriodRowStatus,'aclActiveTable':aclActiveTable,'aclActiveEntry':aclActiveEntry,_m:aclActiveIndex,'aclActiveUserGroupName':aclActiveUserGroupName,'aclActiveUserGroupSubitem':aclActiveUserGroupSubitem,'aclActiveIpGroupName':aclActiveIpGroupName,'aclActiveIpGroupSubitem':aclActiveIpGroupSubitem,'aclActiveLinkGroupName':aclActiveLinkGroupName,'aclActiveLinkGroupSubitem':aclActiveLinkGroupSubitem,'aclActiveBlock0Priority':aclActiveBlock0Priority,'aclActiveBlock1Priority':aclActiveBlock1Priority,'aclActiveBlock2Priority':aclActiveBlock2Priority,'aclActiveBlock3Priority':aclActiveBlock3Priority,'aclActiveBlock4Priority':aclActiveBlock4Priority,'aclActiveConfigSequence':aclActiveConfigSequence,'aclActiveRunning':aclActiveRunning,'aclActiveRowStatus':aclActiveRowStatus,'aclActiveBlock5Priority':aclActiveBlock5Priority,'aclActiveBlock6Priority':aclActiveBlock6Priority,'aclActiveBlock7Priority':aclActiveBlock7Priority,'aclActiveBlock8Priority':aclActiveBlock8Priority,'aclActiveBlock9Priority':aclActiveBlock9Priority,'aclActiveBlock10Priority':aclActiveBlock10Priority,'aclActiveBlock11Priority':aclActiveBlock11Priority,'qosMirrorToTable':qosMirrorToTable,'qosMirrorToEntry':qosMirrorToEntry,_n:qosMirrorToIndex,'qosMirrorToUserGroupName':qosMirrorToUserGroupName,'qosMirrorToUserGroupSubitem':qosMirrorToUserGroupSubitem,'qosMirrorToIpGroupName':qosMirrorToIpGroupName,'qosMirrorToIpGroupSubitem':qosMirrorToIpGroupSubitem,'qosMirrorToLinkGroupName':qosMirrorToLinkGroupName,'qosMirrorToLinkGroupSubitem':qosMirrorToLinkGroupSubitem,'qosMirrorToInterface':qosMirrorToInterface,'qosMirrorToBlock0Priority':qosMirrorToBlock0Priority,'qosMirrorToBlock1Priority':qosMirrorToBlock1Priority,'qosMirrorToBlock2Priority':qosMirrorToBlock2Priority,'qosMirrorToBlock3Priority':qosMirrorToBlock3Priority,'qosMirrorToBlock4Priority':qosMirrorToBlock4Priority,'qosMirrorToConfigSequence':qosMirrorToConfigSequence,'qosMirrorToRunning':qosMirrorToRunning,'qosMirrorToRowStatus':qosMirrorToRowStatus,'qosMirrorToBlock5Priority':qosMirrorToBlock5Priority,'qosMirrorToBlock6Priority':qosMirrorToBlock6Priority,'qosMirrorToBlock7Priority':qosMirrorToBlock7Priority,'qosMirrorToBlock8Priority':qosMirrorToBlock8Priority,'qosMirrorToBlock9Priority':qosMirrorToBlock9Priority,'qosMirrorToBlock10Priority':qosMirrorToBlock10Priority,'qosMirrorToBlock11Priority':qosMirrorToBlock11Priority,'qosRateLimitTable':qosRateLimitTable,'qosRateLimitEntry':qosRateLimitEntry,_o:qosRateLimitIndex,'qosRateLimitUserGroupName':qosRateLimitUserGroupName,'qosRateLimitUserGroupSubitem':qosRateLimitUserGroupSubitem,'qosRateLimitIpGroupName':qosRateLimitIpGroupName,'qosRateLimitIpGroupSubitem':qosRateLimitIpGroupSubitem,'qosRateLimitLinkGroupName':qosRateLimitLinkGroupName,'qosRateLimitLinkGroupSubitem':qosRateLimitLinkGroupSubitem,'qosRateLimitIntf':qosRateLimitIntf,'qosRateLimitTargetRate':qosRateLimitTargetRate,'qosRateLimitExceedAction':qosRateLimitExceedAction,'qosRateLimitDscpValue':qosRateLimitDscpValue,'qosRateLimitBlock0Priority':qosRateLimitBlock0Priority,'qosRateLimitBlock1Priority':qosRateLimitBlock1Priority,'qosRateLimitBlock2Priority':qosRateLimitBlock2Priority,'qosRateLimitBlock3Priority':qosRateLimitBlock3Priority,'qosRateLimitBlock4Priority':qosRateLimitBlock4Priority,'qosRateLimitConfigSequence':qosRateLimitConfigSequence,'qosRateLimitRunning':qosRateLimitRunning,'qosRateLimitRowStatus':qosRateLimitRowStatus,'qosRateLimitBlock5Priority':qosRateLimitBlock5Priority,'qosRateLimitBlock6Priority':qosRateLimitBlock6Priority,'qosRateLimitBlock7Priority':qosRateLimitBlock7Priority,'qosRateLimitBlock8Priority':qosRateLimitBlock8Priority,'qosRateLimitBlock9Priority':qosRateLimitBlock9Priority,'qosRateLimitBlock10Priority':qosRateLimitBlock10Priority,'qosRateLimitBlock11Priority':qosRateLimitBlock11Priority,'qosTrafficPriorityTable':qosTrafficPriorityTable,'qosTrafficPriorityEntry':qosTrafficPriorityEntry,_p:qosTrafficPriorityIndex,'qosTrafficPriorityUserGroupName':qosTrafficPriorityUserGroupName,'qosTrafficPriorityUserGroupSubitem':qosTrafficPriorityUserGroupSubitem,'qosTrafficPriorityIpGroupName':qosTrafficPriorityIpGroupName,'qosTrafficPriorityIpGroupSubitem':qosTrafficPriorityIpGroupSubitem,'qosTrafficPriorityLinkGroupName':qosTrafficPriorityLinkGroupName,'qosTrafficPriorityLinkGroupSubitem':qosTrafficPriorityLinkGroupSubitem,'qosTrafficPriorityDscp':qosTrafficPriorityDscp,'qosTrafficPriorityIpPrecedence':qosTrafficPriorityIpPrecedence,'qosTrafficPriorityCos':qosTrafficPriorityCos,'qosTrafficPriorityLocalPrecedence':qosTrafficPriorityLocalPrecedence,'qosTrafficPriorityBlock0Priority':qosTrafficPriorityBlock0Priority,'qosTrafficPriorityBlock1Priority':qosTrafficPriorityBlock1Priority,'qosTrafficPriorityBlock2Priority':qosTrafficPriorityBlock2Priority,'qosTrafficPriorityBlock3Priority':qosTrafficPriorityBlock3Priority,'qosTrafficPriorityBlock4Priority':qosTrafficPriorityBlock4Priority,'qosTrafficPriorityConfigSequence':qosTrafficPriorityConfigSequence,'qosTrafficPriorityRunning':qosTrafficPriorityRunning,'qosTrafficPriorityRowStatus':qosTrafficPriorityRowStatus,'qosTrafficPriorityBlock5Priority':qosTrafficPriorityBlock5Priority,'qosTrafficPriorityBlock6Priority':qosTrafficPriorityBlock6Priority,'qosTrafficPriorityBlock7Priority':qosTrafficPriorityBlock7Priority,'qosTrafficPriorityBlock8Priority':qosTrafficPriorityBlock8Priority,'qosTrafficPriorityBlock9Priority':qosTrafficPriorityBlock9Priority,'qosTrafficPriorityBlock10Priority':qosTrafficPriorityBlock10Priority,'qosTrafficPriorityBlock11Priority':qosTrafficPriorityBlock11Priority,'qosTrafficRedirectTable':qosTrafficRedirectTable,'qosTrafficRedirectEntry':qosTrafficRedirectEntry,_q:qosTrafficRedirectIndex,'qosTrafficRedirectUserGroupName':qosTrafficRedirectUserGroupName,'qosTrafficRedirectUserGroupSubitem':qosTrafficRedirectUserGroupSubitem,'qosTrafficRedirectIpGroupName':qosTrafficRedirectIpGroupName,'qosTrafficRedirectIpGroupSubitem':qosTrafficRedirectIpGroupSubitem,'qosTrafficRedirectLinkGroupName':qosTrafficRedirectLinkGroupName,'qosTrafficRedirectLinkGroupSubitem':qosTrafficRedirectLinkGroupSubitem,'qosTrafficRedirectInterface':qosTrafficRedirectInterface,'qosTrafficRedirectBlock0Priority':qosTrafficRedirectBlock0Priority,'qosTrafficRedirectBlock1Priority':qosTrafficRedirectBlock1Priority,'qosTrafficRedirectBlock2Priority':qosTrafficRedirectBlock2Priority,'qosTrafficRedirectBlock3Priority':qosTrafficRedirectBlock3Priority,'qosTrafficRedirectBlock4Priority':qosTrafficRedirectBlock4Priority,'qosTrafficRedirectConfigSequence':qosTrafficRedirectConfigSequence,'qosTrafficRedirectRunning':qosTrafficRedirectRunning,'qosTrafficRedirectRowStatus':qosTrafficRedirectRowStatus,'qosTrafficRedirectBlock5Priority':qosTrafficRedirectBlock5Priority,'qosTrafficRedirectBlock6Priority':qosTrafficRedirectBlock6Priority,'qosTrafficRedirectBlock7Priority':qosTrafficRedirectBlock7Priority,'qosTrafficRedirectBlock8Priority':qosTrafficRedirectBlock8Priority,'qosTrafficRedirectBlock9Priority':qosTrafficRedirectBlock9Priority,'qosTrafficRedirectBlock10Priority':qosTrafficRedirectBlock10Priority,'qosTrafficRedirectBlock11Priority':qosTrafficRedirectBlock11Priority,'qosTrafficStatisticsTable':qosTrafficStatisticsTable,'qosTrafficStatisticsEntry':qosTrafficStatisticsEntry,_r:qosTrafficStatisticsIndex,'qosTrafficStatisticsUserGroupName':qosTrafficStatisticsUserGroupName,'qosTrafficStatisticsUserGroupSubitem':qosTrafficStatisticsUserGroupSubitem,'qosTrafficStatisticsIpGroupName':qosTrafficStatisticsIpGroupName,'qosTrafficStatisticsIpGroupSubitem':qosTrafficStatisticsIpGroupSubitem,'qosTrafficStatisticsLinkGroupName':qosTrafficStatisticsLinkGroupName,'qosTrafficStatisticsLinkGroupSubitem':qosTrafficStatisticsLinkGroupSubitem,'qosTrafficStatisticsBlock0Priority':qosTrafficStatisticsBlock0Priority,'qosTrafficStatisticsBlock1Priority':qosTrafficStatisticsBlock1Priority,'qosTrafficStatisticsBlock2Priority':qosTrafficStatisticsBlock2Priority,'qosTrafficStatisticsBlock3Priority':qosTrafficStatisticsBlock3Priority,'qosTrafficStatisticsBlock4Priority':qosTrafficStatisticsBlock4Priority,'qosTrafficStatisticsConfigSequence':qosTrafficStatisticsConfigSequence,'qosTrafficStatisticsRunning':qosTrafficStatisticsRunning,'qosTrafficStatisticsRowStatus':qosTrafficStatisticsRowStatus,'qosTrafficStatisticsCounter':qosTrafficStatisticsCounter,'qosTrafficStatisticsBlock5Priority':qosTrafficStatisticsBlock5Priority,'qosTrafficStatisticsBlock6Priority':qosTrafficStatisticsBlock6Priority,'qosTrafficStatisticsBlock7Priority':qosTrafficStatisticsBlock7Priority,'qosTrafficStatisticsBlock8Priority':qosTrafficStatisticsBlock8Priority,'qosTrafficStatisticsBlock9Priority':qosTrafficStatisticsBlock9Priority,'qosTrafficStatisticsBlock10Priority':qosTrafficStatisticsBlock10Priority,'qosTrafficStatisticsBlock11Priority':qosTrafficStatisticsBlock11Priority,'qosLineRateTable':qosLineRateTable,'qosLineRateEntry':qosLineRateEntry,_s:qosLineRateInterface,'qosLineRateTargetRate':qosLineRateTargetRate,'qosTrafficCopyToCpuTable':qosTrafficCopyToCpuTable,'qosTrafficCopyToCpuEntry':qosTrafficCopyToCpuEntry,_t:qosTrafficCopyToCpuIndex,'qosTrafficCopyToCpuUserGroupName':qosTrafficCopyToCpuUserGroupName,'qosTrafficCopyToCpuUserGroupSubitem':qosTrafficCopyToCpuUserGroupSubitem,'qosTrafficCopyToCpuIpGroupName':qosTrafficCopyToCpuIpGroupName,'qosTrafficCopyToCpuIpGroupSubitem':qosTrafficCopyToCpuIpGroupSubitem,'qosTrafficCopyToCpuLinkGroupName':qosTrafficCopyToCpuLinkGroupName,'qosTrafficCopyToCpuLinkGroupSubitem':qosTrafficCopyToCpuLinkGroupSubitem,'qosTrafficCopyToCpuBlock0Priority':qosTrafficCopyToCpuBlock0Priority,'qosTrafficCopyToCpuBlock1Priority':qosTrafficCopyToCpuBlock1Priority,'qosTrafficCopyToCpuBlock2Priority':qosTrafficCopyToCpuBlock2Priority,'qosTrafficCopyToCpuBlock3Priority':qosTrafficCopyToCpuBlock3Priority,'qosTrafficCopyToCpuBlock4Priority':qosTrafficCopyToCpuBlock4Priority,'qosTrafficCopyToCpuConfigSequence':qosTrafficCopyToCpuConfigSequence,'qosTrafficCopyToCpuRunning':qosTrafficCopyToCpuRunning,'qosTrafficCopyToCpuRowStatus':qosTrafficCopyToCpuRowStatus,'qosTrafficCopyToCpuBlock5Priority':qosTrafficCopyToCpuBlock5Priority,'qosTrafficCopyToCpuBlock6Priority':qosTrafficCopyToCpuBlock6Priority,'qosTrafficCopyToCpuBlock7Priority':qosTrafficCopyToCpuBlock7Priority,'qosTrafficCopyToCpuBlock8Priority':qosTrafficCopyToCpuBlock8Priority,'qosTrafficCopyToCpuBlock9Priority':qosTrafficCopyToCpuBlock9Priority,'qosTrafficCopyToCpuBlock10Priority':qosTrafficCopyToCpuBlock10Priority,'qosTrafficCopyToCpuBlock11Priority':qosTrafficCopyToCpuBlock11Priority,'qaclAppPortIsolationGroup':qaclAppPortIsolationGroup,'qaclAppPortIsolationDownLinkPorts':qaclAppPortIsolationDownLinkPorts,'stormControlTable':stormControlTable,'stormControlEntry':stormControlEntry,_u:stormControlInterface,_v:stormControlType,'stormControlTargetRate':stormControlTargetRate,'stormControlRowStatus':stormControlRowStatus,'qosTrafficRewriteVlanTable':qosTrafficRewriteVlanTable,'qosTrafficRewriteVlanEntry':qosTrafficRewriteVlanEntry,_w:qosTrafficRewriteVlanIndex,'qosTrafficRewriteVlanUserGroupName':qosTrafficRewriteVlanUserGroupName,'qosTrafficRewriteVlanUserGroupSubitem':qosTrafficRewriteVlanUserGroupSubitem,'qosTrafficRewriteVlanIpGroupName':qosTrafficRewriteVlanIpGroupName,'qosTrafficRewriteVlanIpGroupSubitem':qosTrafficRewriteVlanIpGroupSubitem,'qosTrafficRewriteVlanLinkGroupName':qosTrafficRewriteVlanLinkGroupName,'qosTrafficRewriteVlanLinkGroupSubitem':qosTrafficRewriteVlanLinkGroupSubitem,'qosTrafficRewriteVlanVid':qosTrafficRewriteVlanVid,'qosTrafficRewriteVlanBlock0Priority':qosTrafficRewriteVlanBlock0Priority,'qosTrafficRewriteVlanBlock1Priority':qosTrafficRewriteVlanBlock1Priority,'qosTrafficRewriteVlanBlock2Priority':qosTrafficRewriteVlanBlock2Priority,'qosTrafficRewriteVlanBlock3Priority':qosTrafficRewriteVlanBlock3Priority,'qosTrafficRewriteVlanBlock4Priority':qosTrafficRewriteVlanBlock4Priority,'qosTrafficRewriteVlanConfigSequence':qosTrafficRewriteVlanConfigSequence,'qosTrafficRewriteVlanRunning':qosTrafficRewriteVlanRunning,'qosTrafficRewriteVlanRowStatus':qosTrafficRewriteVlanRowStatus,'qosTrafficRewriteVlanBlock5Priority':qosTrafficRewriteVlanBlock5Priority,'qosTrafficRewriteVlanBlock6Priority':qosTrafficRewriteVlanBlock6Priority,'qosTrafficRewriteVlanBlock7Priority':qosTrafficRewriteVlanBlock7Priority,'qosTrafficRewriteVlanBlock8Priority':qosTrafficRewriteVlanBlock8Priority,'qosTrafficRewriteVlanBlock9Priority':qosTrafficRewriteVlanBlock9Priority,'qosTrafficRewriteVlanBlock10Priority':qosTrafficRewriteVlanBlock10Priority,'qosTrafficRewriteVlanBlock11Priority':qosTrafficRewriteVlanBlock11Priority,'qosTrafficInsertVlanTable':qosTrafficInsertVlanTable,'qosTrafficInsertVlanEntry':qosTrafficInsertVlanEntry,_x:qosTrafficInsertVlanIndex,'qosTrafficInsertVlanUserGroupName':qosTrafficInsertVlanUserGroupName,'qosTrafficInsertVlanUserGroupSubitem':qosTrafficInsertVlanUserGroupSubitem,'qosTrafficInsertVlanIpGroupName':qosTrafficInsertVlanIpGroupName,'qosTrafficInsertVlanIpGroupSubitem':qosTrafficInsertVlanIpGroupSubitem,'qosTrafficInsertVlanLinkGroupName':qosTrafficInsertVlanLinkGroupName,'qosTrafficInsertVlanLinkGroupSubitem':qosTrafficInsertVlanLinkGroupSubitem,'qosTrafficInsertVlanVid':qosTrafficInsertVlanVid,'qosTrafficInsertVlanBlock0Priority':qosTrafficInsertVlanBlock0Priority,'qosTrafficInsertVlanBlock1Priority':qosTrafficInsertVlanBlock1Priority,'qosTrafficInsertVlanBlock2Priority':qosTrafficInsertVlanBlock2Priority,'qosTrafficInsertVlanBlock3Priority':qosTrafficInsertVlanBlock3Priority,'qosTrafficInsertVlanBlock4Priority':qosTrafficInsertVlanBlock4Priority,'qosTrafficInsertVlanConfigSequence':qosTrafficInsertVlanConfigSequence,'qosTrafficInsertVlanRunning':qosTrafficInsertVlanRunning,'qosTrafficInsertVlanRowStatus':qosTrafficInsertVlanRowStatus,'qosTrafficInsertVlanBlock5Priority':qosTrafficInsertVlanBlock5Priority,'qosTrafficInsertVlanBlock6Priority':qosTrafficInsertVlanBlock6Priority,'qosTrafficInsertVlanBlock7Priority':qosTrafficInsertVlanBlock7Priority,'qosTrafficInsertVlanBlock8Priority':qosTrafficInsertVlanBlock8Priority,'qosTrafficInsertVlanBlock9Priority':qosTrafficInsertVlanBlock9Priority,'qosTrafficInsertVlanBlock10Priority':qosTrafficInsertVlanBlock10Priority,'qosTrafficInsertVlanBlock11Priority':qosTrafficInsertVlanBlock11Priority})