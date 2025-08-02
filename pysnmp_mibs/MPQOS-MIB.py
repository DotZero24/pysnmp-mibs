_AA='policyStatisSubClassName'
_A9='policyStatisClassName'
_A8='policyStatisDirection'
_A7='policyStatisIfIndex'
_A6='set-prec-transmit'
_A5='set-prec-continue'
_A4='set-dscp-transmit'
_A3='set-dscp-continue'
_A2='qosCarIfIndex'
_A1='qosCarIndex'
_A0='fair-queue'
_z='ifQosIfIndex'
_y='ifWredPreNo'
_x='ifWredRuleIfIndex'
_w='ifWredIfIndex'
_v='wredGrpPreNo'
_u='wredGrpPreName'
_t='wredGrpName'
_s='customListIndex'
_r='customListNoIndex'
_q='customListNo'
_p='priorityListRuleIndex'
_o='priorityListNoIndex'
_n='tailed-dropped'
_m='random-detect'
_l='priorityListNo'
_k='policyClassClassName'
_j='policyClassPolicyName'
_i='policyMapName'
_h='classMapNestName'
_g='classMapNestClassName'
_f='classMapProtocolName'
_e='classMapProtocolClassName'
_d='classMapMplsExpValue'
_c='classMapMplsExpClassName'
_b='classMapIpDscpValue'
_a='classMapIpDscpClassName'
_Z='classMapIpPrecedenceValue'
_Y='classMapIpPrecedenceClassName'
_X='classMapInputIfName'
_W='classMapInputIfClassName'
_V='classMapAclListName'
_U='classMapAclClassName'
_T='classMapClassName'
_S='fragments'
_R='protocol'
_Q='interface'
_P='pqIndex'
_O='wfqIndex'
_N='enable'
_M='disable'
_L='udp'
_K='tcp'
_J='low'
_I='normal'
_H='medium'
_G='high'
_F='DisplayString'
_E='MPQOS-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpQosMib=ModuleIdentity((1,3,6,1,4,1,5651,3,21))
_WfqListTable_Object=MibTable
wfqListTable=_WfqListTable_Object((1,3,6,1,4,1,5651,3,21,1))
if mibBuilder.loadTexts:wfqListTable.setStatus(_A)
_WfqListEntry_Object=MibTableRow
wfqListEntry=_WfqListEntry_Object((1,3,6,1,4,1,5651,3,21,1,1))
wfqListEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:wfqListEntry.setStatus(_A)
_WfqIndex_Type=Integer32
_WfqIndex_Object=MibTableColumn
wfqIndex=_WfqIndex_Object((1,3,6,1,4,1,5651,3,21,1,1,1),_WfqIndex_Type())
wfqIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wfqIndex.setStatus(_A)
class _WfqListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_WfqListNum_Type.__name__=_C
_WfqListNum_Object=MibTableColumn
wfqListNum=_WfqListNum_Object((1,3,6,1,4,1,5651,3,21,1,1,2),_WfqListNum_Type())
wfqListNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqListNum.setStatus(_A)
class _WfqCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('limitAndNumber',1),('weight',2)))
_WfqCtrlType_Type.__name__=_C
_WfqCtrlType_Object=MibTableColumn
wfqCtrlType=_WfqCtrlType_Object((1,3,6,1,4,1,5651,3,21,1,1,3),_WfqCtrlType_Type())
wfqCtrlType.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqCtrlType.setStatus(_A)
class _WfqQueueLimit_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,96))
_WfqQueueLimit_Type.__name__=_C
_WfqQueueLimit_Object=MibTableColumn
wfqQueueLimit=_WfqQueueLimit_Object((1,3,6,1,4,1,5651,3,21,1,1,4),_WfqQueueLimit_Type())
wfqQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqQueueLimit.setStatus(_A)
class _WfqQueueNumber_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,2048))
_WfqQueueNumber_Type.__name__=_C
_WfqQueueNumber_Object=MibTableColumn
wfqQueueNumber=_WfqQueueNumber_Object((1,3,6,1,4,1,5651,3,21,1,1,5),_WfqQueueNumber_Type())
wfqQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqQueueNumber.setStatus(_A)
class _WfqWeightNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WfqWeightNumber_Type.__name__=_C
_WfqWeightNumber_Object=MibTableColumn
wfqWeightNumber=_WfqWeightNumber_Object((1,3,6,1,4,1,5651,3,21,1,1,6),_WfqWeightNumber_Type())
wfqWeightNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqWeightNumber.setStatus(_A)
class _WfqWeightType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),('icmp',3),('igmp',4)))
_WfqWeightType_Type.__name__=_C
_WfqWeightType_Object=MibTableColumn
wfqWeightType=_WfqWeightType_Object((1,3,6,1,4,1,5651,3,21,1,1,7),_WfqWeightType_Type())
wfqWeightType.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqWeightType.setStatus(_A)
_WfqSrcIp_Type=IpAddress
_WfqSrcIp_Object=MibTableColumn
wfqSrcIp=_WfqSrcIp_Object((1,3,6,1,4,1,5651,3,21,1,1,8),_WfqSrcIp_Type())
wfqSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqSrcIp.setStatus(_A)
class _WfqSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WfqSrcPort_Type.__name__=_C
_WfqSrcPort_Object=MibTableColumn
wfqSrcPort=_WfqSrcPort_Object((1,3,6,1,4,1,5651,3,21,1,1,9),_WfqSrcPort_Type())
wfqSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqSrcPort.setStatus(_A)
_WfqDstIp_Type=IpAddress
_WfqDstIp_Object=MibTableColumn
wfqDstIp=_WfqDstIp_Object((1,3,6,1,4,1,5651,3,21,1,1,10),_WfqDstIp_Type())
wfqDstIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqDstIp.setStatus(_A)
class _WfqDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WfqDstPort_Type.__name__=_C
_WfqDstPort_Object=MibTableColumn
wfqDstPort=_WfqDstPort_Object((1,3,6,1,4,1,5651,3,21,1,1,11),_WfqDstPort_Type())
wfqDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqDstPort.setStatus(_A)
_WfqStatus_Type=RowStatus
_WfqStatus_Object=MibTableColumn
wfqStatus=_WfqStatus_Object((1,3,6,1,4,1,5651,3,21,1,1,12),_WfqStatus_Type())
wfqStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wfqStatus.setStatus(_A)
_PqListTable_Object=MibTable
pqListTable=_PqListTable_Object((1,3,6,1,4,1,5651,3,21,2))
if mibBuilder.loadTexts:pqListTable.setStatus(_A)
_PqListEntry_Object=MibTableRow
pqListEntry=_PqListEntry_Object((1,3,6,1,4,1,5651,3,21,2,1))
pqListEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:pqListEntry.setStatus(_A)
_PqIndex_Type=Integer32
_PqIndex_Object=MibTableColumn
pqIndex=_PqIndex_Object((1,3,6,1,4,1,5651,3,21,2,1,1),_PqIndex_Type())
pqIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pqIndex.setStatus(_A)
class _PqListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PqListNum_Type.__name__=_C
_PqListNum_Object=MibTableColumn
pqListNum=_PqListNum_Object((1,3,6,1,4,1,5651,3,21,2,1,2),_PqListNum_Type())
pqListNum.setMaxAccess(_B)
if mibBuilder.loadTexts:pqListNum.setStatus(_A)
class _PqCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('defaultAndLimit',1),(_Q,2),(_R,3)))
_PqCtrlType_Type.__name__=_C
_PqCtrlType_Object=MibTableColumn
pqCtrlType=_PqCtrlType_Object((1,3,6,1,4,1,5651,3,21,2,1,3),_PqCtrlType_Type())
pqCtrlType.setMaxAccess(_B)
if mibBuilder.loadTexts:pqCtrlType.setStatus(_A)
class _PqDefault_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_PqDefault_Type.__name__=_C
_PqDefault_Object=MibTableColumn
pqDefault=_PqDefault_Object((1,3,6,1,4,1,5651,3,21,2,1,4),_PqDefault_Type())
pqDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:pqDefault.setStatus(_A)
_PqIfIndex_Type=Integer32
_PqIfIndex_Object=MibTableColumn
pqIfIndex=_PqIfIndex_Object((1,3,6,1,4,1,5651,3,21,2,1,5),_PqIfIndex_Type())
pqIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pqIfIndex.setStatus(_A)
class _PqProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ip',1))
_PqProtocol_Type.__name__=_C
_PqProtocol_Object=MibTableColumn
pqProtocol=_PqProtocol_Object((1,3,6,1,4,1,5651,3,21,2,1,6),_PqProtocol_Type())
pqProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pqProtocol.setStatus(_A)
class _PqPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_PqPriority_Type.__name__=_C
_PqPriority_Object=MibTableColumn
pqPriority=_PqPriority_Object((1,3,6,1,4,1,5651,3,21,2,1,7),_PqPriority_Type())
pqPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:pqPriority.setStatus(_A)
class _PqProtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),('gt',2),('list',3),('lt',4),(_K,5),(_L,6)))
_PqProtType_Type.__name__=_C
_PqProtType_Object=MibTableColumn
pqProtType=_PqProtType_Object((1,3,6,1,4,1,5651,3,21,2,1,8),_PqProtType_Type())
pqProtType.setMaxAccess(_B)
if mibBuilder.loadTexts:pqProtType.setStatus(_A)
_PqProtValue_Type=Integer32
_PqProtValue_Object=MibTableColumn
pqProtValue=_PqProtValue_Object((1,3,6,1,4,1,5651,3,21,2,1,9),_PqProtValue_Type())
pqProtValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pqProtValue.setStatus(_A)
class _PqQueueHigh_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PqQueueHigh_Type.__name__=_C
_PqQueueHigh_Object=MibTableColumn
pqQueueHigh=_PqQueueHigh_Object((1,3,6,1,4,1,5651,3,21,2,1,10),_PqQueueHigh_Type())
pqQueueHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:pqQueueHigh.setStatus(_A)
class _PqQueueMedium_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PqQueueMedium_Type.__name__=_C
_PqQueueMedium_Object=MibTableColumn
pqQueueMedium=_PqQueueMedium_Object((1,3,6,1,4,1,5651,3,21,2,1,11),_PqQueueMedium_Type())
pqQueueMedium.setMaxAccess(_B)
if mibBuilder.loadTexts:pqQueueMedium.setStatus(_A)
class _PqQueueNormal_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PqQueueNormal_Type.__name__=_C
_PqQueueNormal_Object=MibTableColumn
pqQueueNormal=_PqQueueNormal_Object((1,3,6,1,4,1,5651,3,21,2,1,12),_PqQueueNormal_Type())
pqQueueNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:pqQueueNormal.setStatus(_A)
class _PqQueueLow_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PqQueueLow_Type.__name__=_C
_PqQueueLow_Object=MibTableColumn
pqQueueLow=_PqQueueLow_Object((1,3,6,1,4,1,5651,3,21,2,1,13),_PqQueueLow_Type())
pqQueueLow.setMaxAccess(_B)
if mibBuilder.loadTexts:pqQueueLow.setStatus(_A)
_PqStatus_Type=RowStatus
_PqStatus_Object=MibTableColumn
pqStatus=_PqStatus_Object((1,3,6,1,4,1,5651,3,21,2,1,14),_PqStatus_Type())
pqStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pqStatus.setStatus(_A)
_ClassMap_ObjectIdentity=ObjectIdentity
classMap=_ClassMap_ObjectIdentity((1,3,6,1,4,1,5651,3,21,3))
_ClassMapTable_Object=MibTable
classMapTable=_ClassMapTable_Object((1,3,6,1,4,1,5651,3,21,3,1))
if mibBuilder.loadTexts:classMapTable.setStatus(_A)
_ClassMapEntry_Object=MibTableRow
classMapEntry=_ClassMapEntry_Object((1,3,6,1,4,1,5651,3,21,3,1,1))
classMapEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:classMapEntry.setStatus(_A)
class _ClassMapClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapClassName_Type.__name__=_F
_ClassMapClassName_Object=MibTableColumn
classMapClassName=_ClassMapClassName_Object((1,3,6,1,4,1,5651,3,21,3,1,1,1),_ClassMapClassName_Type())
classMapClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapClassName.setStatus(_A)
class _ClassMapMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('match-all',0),('match-any',1)))
_ClassMapMatchType_Type.__name__=_C
_ClassMapMatchType_Object=MibTableColumn
classMapMatchType=_ClassMapMatchType_Object((1,3,6,1,4,1,5651,3,21,3,1,1,2),_ClassMapMatchType_Type())
classMapMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapMatchType.setStatus(_A)
_ClassMapRowStatus_Type=RowStatus
_ClassMapRowStatus_Object=MibTableColumn
classMapRowStatus=_ClassMapRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,1,1,3),_ClassMapRowStatus_Type())
classMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapRowStatus.setStatus(_A)
_ClassMapAclTable_Object=MibTable
classMapAclTable=_ClassMapAclTable_Object((1,3,6,1,4,1,5651,3,21,3,10))
if mibBuilder.loadTexts:classMapAclTable.setStatus(_A)
_ClassMapAclEntry_Object=MibTableRow
classMapAclEntry=_ClassMapAclEntry_Object((1,3,6,1,4,1,5651,3,21,3,10,1))
classMapAclEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:classMapAclEntry.setStatus(_A)
class _ClassMapAclClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapAclClassName_Type.__name__=_F
_ClassMapAclClassName_Object=MibTableColumn
classMapAclClassName=_ClassMapAclClassName_Object((1,3,6,1,4,1,5651,3,21,3,10,1,1),_ClassMapAclClassName_Type())
classMapAclClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapAclClassName.setStatus(_A)
class _ClassMapAclListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapAclListName_Type.__name__=_F
_ClassMapAclListName_Object=MibTableColumn
classMapAclListName=_ClassMapAclListName_Object((1,3,6,1,4,1,5651,3,21,3,10,1,2),_ClassMapAclListName_Type())
classMapAclListName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapAclListName.setStatus(_A)
_ClassMapAclRowStatus_Type=RowStatus
_ClassMapAclRowStatus_Object=MibTableColumn
classMapAclRowStatus=_ClassMapAclRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,10,1,3),_ClassMapAclRowStatus_Type())
classMapAclRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapAclRowStatus.setStatus(_A)
_ClassMapInputIfTable_Object=MibTable
classMapInputIfTable=_ClassMapInputIfTable_Object((1,3,6,1,4,1,5651,3,21,3,20))
if mibBuilder.loadTexts:classMapInputIfTable.setStatus(_A)
_ClassMapInputIfEntry_Object=MibTableRow
classMapInputIfEntry=_ClassMapInputIfEntry_Object((1,3,6,1,4,1,5651,3,21,3,20,1))
classMapInputIfEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:classMapInputIfEntry.setStatus(_A)
class _ClassMapInputIfClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapInputIfClassName_Type.__name__=_F
_ClassMapInputIfClassName_Object=MibTableColumn
classMapInputIfClassName=_ClassMapInputIfClassName_Object((1,3,6,1,4,1,5651,3,21,3,20,1,1),_ClassMapInputIfClassName_Type())
classMapInputIfClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapInputIfClassName.setStatus(_A)
class _ClassMapInputIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_ClassMapInputIfName_Type.__name__=_F
_ClassMapInputIfName_Object=MibTableColumn
classMapInputIfName=_ClassMapInputIfName_Object((1,3,6,1,4,1,5651,3,21,3,20,1,2),_ClassMapInputIfName_Type())
classMapInputIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapInputIfName.setStatus(_A)
_ClassMapInputIfRowStatus_Type=RowStatus
_ClassMapInputIfRowStatus_Object=MibTableColumn
classMapInputIfRowStatus=_ClassMapInputIfRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,20,1,3),_ClassMapInputIfRowStatus_Type())
classMapInputIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapInputIfRowStatus.setStatus(_A)
_ClassMapIpPrecedenceTable_Object=MibTable
classMapIpPrecedenceTable=_ClassMapIpPrecedenceTable_Object((1,3,6,1,4,1,5651,3,21,3,30))
if mibBuilder.loadTexts:classMapIpPrecedenceTable.setStatus(_A)
_ClassMapIpPrecedenceEntry_Object=MibTableRow
classMapIpPrecedenceEntry=_ClassMapIpPrecedenceEntry_Object((1,3,6,1,4,1,5651,3,21,3,30,1))
classMapIpPrecedenceEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:classMapIpPrecedenceEntry.setStatus(_A)
class _ClassMapIpPrecedenceClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapIpPrecedenceClassName_Type.__name__=_F
_ClassMapIpPrecedenceClassName_Object=MibTableColumn
classMapIpPrecedenceClassName=_ClassMapIpPrecedenceClassName_Object((1,3,6,1,4,1,5651,3,21,3,30,1,1),_ClassMapIpPrecedenceClassName_Type())
classMapIpPrecedenceClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapIpPrecedenceClassName.setStatus(_A)
class _ClassMapIpPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ClassMapIpPrecedenceValue_Type.__name__=_C
_ClassMapIpPrecedenceValue_Object=MibTableColumn
classMapIpPrecedenceValue=_ClassMapIpPrecedenceValue_Object((1,3,6,1,4,1,5651,3,21,3,30,1,2),_ClassMapIpPrecedenceValue_Type())
classMapIpPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapIpPrecedenceValue.setStatus(_A)
_ClassMapIpPrecedenceRowStatus_Type=RowStatus
_ClassMapIpPrecedenceRowStatus_Object=MibTableColumn
classMapIpPrecedenceRowStatus=_ClassMapIpPrecedenceRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,30,1,3),_ClassMapIpPrecedenceRowStatus_Type())
classMapIpPrecedenceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapIpPrecedenceRowStatus.setStatus(_A)
_ClassMapIpDscpTable_Object=MibTable
classMapIpDscpTable=_ClassMapIpDscpTable_Object((1,3,6,1,4,1,5651,3,21,3,40))
if mibBuilder.loadTexts:classMapIpDscpTable.setStatus(_A)
_ClassMapIpDscpEntry_Object=MibTableRow
classMapIpDscpEntry=_ClassMapIpDscpEntry_Object((1,3,6,1,4,1,5651,3,21,3,40,1))
classMapIpDscpEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:classMapIpDscpEntry.setStatus(_A)
class _ClassMapIpDscpClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapIpDscpClassName_Type.__name__=_F
_ClassMapIpDscpClassName_Object=MibTableColumn
classMapIpDscpClassName=_ClassMapIpDscpClassName_Object((1,3,6,1,4,1,5651,3,21,3,40,1,1),_ClassMapIpDscpClassName_Type())
classMapIpDscpClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapIpDscpClassName.setStatus(_A)
class _ClassMapIpDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ClassMapIpDscpValue_Type.__name__=_C
_ClassMapIpDscpValue_Object=MibTableColumn
classMapIpDscpValue=_ClassMapIpDscpValue_Object((1,3,6,1,4,1,5651,3,21,3,40,1,2),_ClassMapIpDscpValue_Type())
classMapIpDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapIpDscpValue.setStatus(_A)
_ClassMapIpDscpRowStatus_Type=RowStatus
_ClassMapIpDscpRowStatus_Object=MibTableColumn
classMapIpDscpRowStatus=_ClassMapIpDscpRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,40,1,3),_ClassMapIpDscpRowStatus_Type())
classMapIpDscpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapIpDscpRowStatus.setStatus(_A)
_ClassMapMplsExpTable_Object=MibTable
classMapMplsExpTable=_ClassMapMplsExpTable_Object((1,3,6,1,4,1,5651,3,21,3,50))
if mibBuilder.loadTexts:classMapMplsExpTable.setStatus(_A)
_ClassMapMplsExpEntry_Object=MibTableRow
classMapMplsExpEntry=_ClassMapMplsExpEntry_Object((1,3,6,1,4,1,5651,3,21,3,50,1))
classMapMplsExpEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:classMapMplsExpEntry.setStatus(_A)
class _ClassMapMplsExpClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapMplsExpClassName_Type.__name__=_F
_ClassMapMplsExpClassName_Object=MibTableColumn
classMapMplsExpClassName=_ClassMapMplsExpClassName_Object((1,3,6,1,4,1,5651,3,21,3,50,1,1),_ClassMapMplsExpClassName_Type())
classMapMplsExpClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapMplsExpClassName.setStatus(_A)
class _ClassMapMplsExpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ClassMapMplsExpValue_Type.__name__=_C
_ClassMapMplsExpValue_Object=MibTableColumn
classMapMplsExpValue=_ClassMapMplsExpValue_Object((1,3,6,1,4,1,5651,3,21,3,50,1,2),_ClassMapMplsExpValue_Type())
classMapMplsExpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapMplsExpValue.setStatus(_A)
_ClassMapMplsExpRowStatus_Type=RowStatus
_ClassMapMplsExpRowStatus_Object=MibTableColumn
classMapMplsExpRowStatus=_ClassMapMplsExpRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,50,1,3),_ClassMapMplsExpRowStatus_Type())
classMapMplsExpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapMplsExpRowStatus.setStatus(_A)
_ClassMapProtocolTable_Object=MibTable
classMapProtocolTable=_ClassMapProtocolTable_Object((1,3,6,1,4,1,5651,3,21,3,60))
if mibBuilder.loadTexts:classMapProtocolTable.setStatus(_A)
_ClassMapProtocolEntry_Object=MibTableRow
classMapProtocolEntry=_ClassMapProtocolEntry_Object((1,3,6,1,4,1,5651,3,21,3,60,1))
classMapProtocolEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:classMapProtocolEntry.setStatus(_A)
class _ClassMapProtocolClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapProtocolClassName_Type.__name__=_F
_ClassMapProtocolClassName_Object=MibTableColumn
classMapProtocolClassName=_ClassMapProtocolClassName_Object((1,3,6,1,4,1,5651,3,21,3,60,1,1),_ClassMapProtocolClassName_Type())
classMapProtocolClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapProtocolClassName.setStatus(_A)
class _ClassMapProtocolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapProtocolName_Type.__name__=_F
_ClassMapProtocolName_Object=MibTableColumn
classMapProtocolName=_ClassMapProtocolName_Object((1,3,6,1,4,1,5651,3,21,3,60,1,2),_ClassMapProtocolName_Type())
classMapProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapProtocolName.setStatus(_A)
_ClassMapProtocolRowStatus_Type=RowStatus
_ClassMapProtocolRowStatus_Object=MibTableColumn
classMapProtocolRowStatus=_ClassMapProtocolRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,60,1,3),_ClassMapProtocolRowStatus_Type())
classMapProtocolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapProtocolRowStatus.setStatus(_A)
_ClassMapNestTable_Object=MibTable
classMapNestTable=_ClassMapNestTable_Object((1,3,6,1,4,1,5651,3,21,3,70))
if mibBuilder.loadTexts:classMapNestTable.setStatus(_A)
_ClassMapNestEntry_Object=MibTableRow
classMapNestEntry=_ClassMapNestEntry_Object((1,3,6,1,4,1,5651,3,21,3,70,1))
classMapNestEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:classMapNestEntry.setStatus(_A)
class _ClassMapNestClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapNestClassName_Type.__name__=_F
_ClassMapNestClassName_Object=MibTableColumn
classMapNestClassName=_ClassMapNestClassName_Object((1,3,6,1,4,1,5651,3,21,3,70,1,1),_ClassMapNestClassName_Type())
classMapNestClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapNestClassName.setStatus(_A)
class _ClassMapNestName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClassMapNestName_Type.__name__=_F
_ClassMapNestName_Object=MibTableColumn
classMapNestName=_ClassMapNestName_Object((1,3,6,1,4,1,5651,3,21,3,70,1,2),_ClassMapNestName_Type())
classMapNestName.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapNestName.setStatus(_A)
_ClassMapNestRowStatus_Type=RowStatus
_ClassMapNestRowStatus_Object=MibTableColumn
classMapNestRowStatus=_ClassMapNestRowStatus_Object((1,3,6,1,4,1,5651,3,21,3,70,1,3),_ClassMapNestRowStatus_Type())
classMapNestRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:classMapNestRowStatus.setStatus(_A)
_PolicyMap_ObjectIdentity=ObjectIdentity
policyMap=_PolicyMap_ObjectIdentity((1,3,6,1,4,1,5651,3,21,4))
_PolicyMapTable_Object=MibTable
policyMapTable=_PolicyMapTable_Object((1,3,6,1,4,1,5651,3,21,4,10))
if mibBuilder.loadTexts:policyMapTable.setStatus(_A)
_PolicyMapEntry_Object=MibTableRow
policyMapEntry=_PolicyMapEntry_Object((1,3,6,1,4,1,5651,3,21,4,10,1))
policyMapEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:policyMapEntry.setStatus(_A)
class _PolicyMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PolicyMapName_Type.__name__=_F
_PolicyMapName_Object=MibTableColumn
policyMapName=_PolicyMapName_Object((1,3,6,1,4,1,5651,3,21,4,10,1,1),_PolicyMapName_Type())
policyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:policyMapName.setStatus(_A)
_PolicyMapRowStatus_Type=RowStatus
_PolicyMapRowStatus_Object=MibTableColumn
policyMapRowStatus=_PolicyMapRowStatus_Object((1,3,6,1,4,1,5651,3,21,4,10,1,2),_PolicyMapRowStatus_Type())
policyMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:policyMapRowStatus.setStatus(_A)
_PolicyClassTable_Object=MibTable
policyClassTable=_PolicyClassTable_Object((1,3,6,1,4,1,5651,3,21,4,20))
if mibBuilder.loadTexts:policyClassTable.setStatus(_A)
_PolicyClassEntry_Object=MibTableRow
policyClassEntry=_PolicyClassEntry_Object((1,3,6,1,4,1,5651,3,21,4,20,1))
policyClassEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:policyClassEntry.setStatus(_A)
class _PolicyClassPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PolicyClassPolicyName_Type.__name__=_F
_PolicyClassPolicyName_Object=MibTableColumn
policyClassPolicyName=_PolicyClassPolicyName_Object((1,3,6,1,4,1,5651,3,21,4,20,1,1),_PolicyClassPolicyName_Type())
policyClassPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassPolicyName.setStatus(_A)
class _PolicyClassClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PolicyClassClassName_Type.__name__=_F
_PolicyClassClassName_Object=MibTableColumn
policyClassClassName=_PolicyClassClassName_Object((1,3,6,1,4,1,5651,3,21,4,20,1,2),_PolicyClassClassName_Type())
policyClassClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassClassName.setStatus(_A)
class _PolicyClassBandWidthKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_PolicyClassBandWidthKbps_Type.__name__=_C
_PolicyClassBandWidthKbps_Object=MibTableColumn
policyClassBandWidthKbps=_PolicyClassBandWidthKbps_Object((1,3,6,1,4,1,5651,3,21,4,20,1,3),_PolicyClassBandWidthKbps_Type())
policyClassBandWidthKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassBandWidthKbps.setStatus(_A)
class _PolicyClassBandWidthTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_PolicyClassBandWidthTotal_Type.__name__=_C
_PolicyClassBandWidthTotal_Object=MibTableColumn
policyClassBandWidthTotal=_PolicyClassBandWidthTotal_Object((1,3,6,1,4,1,5651,3,21,4,20,1,4),_PolicyClassBandWidthTotal_Type())
policyClassBandWidthTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassBandWidthTotal.setStatus(_A)
class _PolicyClassBandWidthPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PolicyClassBandWidthPercent_Type.__name__=_C
_PolicyClassBandWidthPercent_Object=MibTableColumn
policyClassBandWidthPercent=_PolicyClassBandWidthPercent_Object((1,3,6,1,4,1,5651,3,21,4,20,1,5),_PolicyClassBandWidthPercent_Type())
policyClassBandWidthPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassBandWidthPercent.setStatus(_A)
class _PolicyClassPriorityBps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_PolicyClassPriorityBps_Type.__name__=_C
_PolicyClassPriorityBps_Object=MibTableColumn
policyClassPriorityBps=_PolicyClassPriorityBps_Object((1,3,6,1,4,1,5651,3,21,4,20,1,6),_PolicyClassPriorityBps_Type())
policyClassPriorityBps.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassPriorityBps.setStatus(_A)
class _PolicyClassPriorityPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PolicyClassPriorityPercent_Type.__name__=_C
_PolicyClassPriorityPercent_Object=MibTableColumn
policyClassPriorityPercent=_PolicyClassPriorityPercent_Object((1,3,6,1,4,1,5651,3,21,4,20,1,7),_PolicyClassPriorityPercent_Type())
policyClassPriorityPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassPriorityPercent.setStatus(_A)
class _PolicyClassWredEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_PolicyClassWredEnable_Type.__name__=_C
_PolicyClassWredEnable_Object=MibTableColumn
policyClassWredEnable=_PolicyClassWredEnable_Object((1,3,6,1,4,1,5651,3,21,4,20,1,8),_PolicyClassWredEnable_Type())
policyClassWredEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredEnable.setStatus(_A)
class _PolicyClassWredWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_PolicyClassWredWeight_Type.__name__=_C
_PolicyClassWredWeight_Object=MibTableColumn
policyClassWredWeight=_PolicyClassWredWeight_Object((1,3,6,1,4,1,5651,3,21,4,20,1,9),_PolicyClassWredWeight_Type())
policyClassWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredWeight.setStatus(_A)
class _PolicyClassWredMinThreshold0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold0_Type.__name__=_C
_PolicyClassWredMinThreshold0_Object=MibTableColumn
policyClassWredMinThreshold0=_PolicyClassWredMinThreshold0_Object((1,3,6,1,4,1,5651,3,21,4,20,1,10),_PolicyClassWredMinThreshold0_Type())
policyClassWredMinThreshold0.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold0.setStatus(_A)
class _PolicyClassWredMaxThreshold0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold0_Type.__name__=_C
_PolicyClassWredMaxThreshold0_Object=MibTableColumn
policyClassWredMaxThreshold0=_PolicyClassWredMaxThreshold0_Object((1,3,6,1,4,1,5651,3,21,4,20,1,11),_PolicyClassWredMaxThreshold0_Type())
policyClassWredMaxThreshold0.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold0.setStatus(_A)
class _PolicyClassWredMinThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold1_Type.__name__=_C
_PolicyClassWredMinThreshold1_Object=MibTableColumn
policyClassWredMinThreshold1=_PolicyClassWredMinThreshold1_Object((1,3,6,1,4,1,5651,3,21,4,20,1,12),_PolicyClassWredMinThreshold1_Type())
policyClassWredMinThreshold1.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold1.setStatus(_A)
class _PolicyClassWredMaxThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold1_Type.__name__=_C
_PolicyClassWredMaxThreshold1_Object=MibTableColumn
policyClassWredMaxThreshold1=_PolicyClassWredMaxThreshold1_Object((1,3,6,1,4,1,5651,3,21,4,20,1,13),_PolicyClassWredMaxThreshold1_Type())
policyClassWredMaxThreshold1.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold1.setStatus(_A)
class _PolicyClassWredMinThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold2_Type.__name__=_C
_PolicyClassWredMinThreshold2_Object=MibTableColumn
policyClassWredMinThreshold2=_PolicyClassWredMinThreshold2_Object((1,3,6,1,4,1,5651,3,21,4,20,1,14),_PolicyClassWredMinThreshold2_Type())
policyClassWredMinThreshold2.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold2.setStatus(_A)
class _PolicyClassWredMaxThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold2_Type.__name__=_C
_PolicyClassWredMaxThreshold2_Object=MibTableColumn
policyClassWredMaxThreshold2=_PolicyClassWredMaxThreshold2_Object((1,3,6,1,4,1,5651,3,21,4,20,1,15),_PolicyClassWredMaxThreshold2_Type())
policyClassWredMaxThreshold2.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold2.setStatus(_A)
class _PolicyClassWredMinThreshold3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold3_Type.__name__=_C
_PolicyClassWredMinThreshold3_Object=MibTableColumn
policyClassWredMinThreshold3=_PolicyClassWredMinThreshold3_Object((1,3,6,1,4,1,5651,3,21,4,20,1,16),_PolicyClassWredMinThreshold3_Type())
policyClassWredMinThreshold3.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold3.setStatus(_A)
class _PolicyClassWredMaxThreshold3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold3_Type.__name__=_C
_PolicyClassWredMaxThreshold3_Object=MibTableColumn
policyClassWredMaxThreshold3=_PolicyClassWredMaxThreshold3_Object((1,3,6,1,4,1,5651,3,21,4,20,1,17),_PolicyClassWredMaxThreshold3_Type())
policyClassWredMaxThreshold3.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold3.setStatus(_A)
class _PolicyClassWredMinThreshold4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold4_Type.__name__=_C
_PolicyClassWredMinThreshold4_Object=MibTableColumn
policyClassWredMinThreshold4=_PolicyClassWredMinThreshold4_Object((1,3,6,1,4,1,5651,3,21,4,20,1,18),_PolicyClassWredMinThreshold4_Type())
policyClassWredMinThreshold4.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold4.setStatus(_A)
class _PolicyClassWredMaxThreshold4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold4_Type.__name__=_C
_PolicyClassWredMaxThreshold4_Object=MibTableColumn
policyClassWredMaxThreshold4=_PolicyClassWredMaxThreshold4_Object((1,3,6,1,4,1,5651,3,21,4,20,1,19),_PolicyClassWredMaxThreshold4_Type())
policyClassWredMaxThreshold4.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold4.setStatus(_A)
class _PolicyClassWredMinThreshold5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold5_Type.__name__=_C
_PolicyClassWredMinThreshold5_Object=MibTableColumn
policyClassWredMinThreshold5=_PolicyClassWredMinThreshold5_Object((1,3,6,1,4,1,5651,3,21,4,20,1,20),_PolicyClassWredMinThreshold5_Type())
policyClassWredMinThreshold5.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold5.setStatus(_A)
class _PolicyClassWredMaxThreshold5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold5_Type.__name__=_C
_PolicyClassWredMaxThreshold5_Object=MibTableColumn
policyClassWredMaxThreshold5=_PolicyClassWredMaxThreshold5_Object((1,3,6,1,4,1,5651,3,21,4,20,1,21),_PolicyClassWredMaxThreshold5_Type())
policyClassWredMaxThreshold5.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold5.setStatus(_A)
class _PolicyClassWredMinThreshold6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold6_Type.__name__=_C
_PolicyClassWredMinThreshold6_Object=MibTableColumn
policyClassWredMinThreshold6=_PolicyClassWredMinThreshold6_Object((1,3,6,1,4,1,5651,3,21,4,20,1,22),_PolicyClassWredMinThreshold6_Type())
policyClassWredMinThreshold6.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold6.setStatus(_A)
class _PolicyClassWredMaxThreshold6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold6_Type.__name__=_C
_PolicyClassWredMaxThreshold6_Object=MibTableColumn
policyClassWredMaxThreshold6=_PolicyClassWredMaxThreshold6_Object((1,3,6,1,4,1,5651,3,21,4,20,1,23),_PolicyClassWredMaxThreshold6_Type())
policyClassWredMaxThreshold6.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold6.setStatus(_A)
class _PolicyClassWredMinThreshold7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMinThreshold7_Type.__name__=_C
_PolicyClassWredMinThreshold7_Object=MibTableColumn
policyClassWredMinThreshold7=_PolicyClassWredMinThreshold7_Object((1,3,6,1,4,1,5651,3,21,4,20,1,24),_PolicyClassWredMinThreshold7_Type())
policyClassWredMinThreshold7.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMinThreshold7.setStatus(_A)
class _PolicyClassWredMaxThreshold7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PolicyClassWredMaxThreshold7_Type.__name__=_C
_PolicyClassWredMaxThreshold7_Object=MibTableColumn
policyClassWredMaxThreshold7=_PolicyClassWredMaxThreshold7_Object((1,3,6,1,4,1,5651,3,21,4,20,1,25),_PolicyClassWredMaxThreshold7_Type())
policyClassWredMaxThreshold7.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassWredMaxThreshold7.setStatus(_A)
class _PolicyClassSetIpPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_PolicyClassSetIpPrecedence_Type.__name__=_C
_PolicyClassSetIpPrecedence_Object=MibTableColumn
policyClassSetIpPrecedence=_PolicyClassSetIpPrecedence_Object((1,3,6,1,4,1,5651,3,21,4,20,1,26),_PolicyClassSetIpPrecedence_Type())
policyClassSetIpPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassSetIpPrecedence.setStatus(_A)
class _PolicyClassSetIpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_PolicyClassSetIpDscp_Type.__name__=_C
_PolicyClassSetIpDscp_Object=MibTableColumn
policyClassSetIpDscp=_PolicyClassSetIpDscp_Object((1,3,6,1,4,1,5651,3,21,4,20,1,27),_PolicyClassSetIpDscp_Type())
policyClassSetIpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassSetIpDscp.setStatus(_A)
class _PolicyClassSetMplsImp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_PolicyClassSetMplsImp_Type.__name__=_C
_PolicyClassSetMplsImp_Object=MibTableColumn
policyClassSetMplsImp=_PolicyClassSetMplsImp_Object((1,3,6,1,4,1,5651,3,21,4,20,1,28),_PolicyClassSetMplsImp_Type())
policyClassSetMplsImp.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassSetMplsImp.setStatus(_A)
class _PolicyClassSetMplsTop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_PolicyClassSetMplsTop_Type.__name__=_C
_PolicyClassSetMplsTop_Object=MibTableColumn
policyClassSetMplsTop=_PolicyClassSetMplsTop_Object((1,3,6,1,4,1,5651,3,21,4,20,1,29),_PolicyClassSetMplsTop_Type())
policyClassSetMplsTop.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassSetMplsTop.setStatus(_A)
class _PolicyClassNestName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PolicyClassNestName_Type.__name__=_F
_PolicyClassNestName_Object=MibTableColumn
policyClassNestName=_PolicyClassNestName_Object((1,3,6,1,4,1,5651,3,21,4,20,1,30),_PolicyClassNestName_Type())
policyClassNestName.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassNestName.setStatus(_A)
_PolicyClassRowStatus_Type=RowStatus
_PolicyClassRowStatus_Object=MibTableColumn
policyClassRowStatus=_PolicyClassRowStatus_Object((1,3,6,1,4,1,5651,3,21,4,20,1,31),_PolicyClassRowStatus_Type())
policyClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:policyClassRowStatus.setStatus(_A)
_PriorityList_ObjectIdentity=ObjectIdentity
priorityList=_PriorityList_ObjectIdentity((1,3,6,1,4,1,5651,3,21,5))
_PriorityListTable_Object=MibTable
priorityListTable=_PriorityListTable_Object((1,3,6,1,4,1,5651,3,21,5,1))
if mibBuilder.loadTexts:priorityListTable.setStatus(_A)
_PriorityListEntry_Object=MibTableRow
priorityListEntry=_PriorityListEntry_Object((1,3,6,1,4,1,5651,3,21,5,1,1))
priorityListEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:priorityListEntry.setStatus(_A)
class _PriorityListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PriorityListNo_Type.__name__=_C
_PriorityListNo_Object=MibTableColumn
priorityListNo=_PriorityListNo_Object((1,3,6,1,4,1,5651,3,21,5,1,1,1),_PriorityListNo_Type())
priorityListNo.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListNo.setStatus(_A)
class _PriorityListDefQType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_PriorityListDefQType_Type.__name__=_C
_PriorityListDefQType_Object=MibTableColumn
priorityListDefQType=_PriorityListDefQType_Object((1,3,6,1,4,1,5651,3,21,5,1,1,2),_PriorityListDefQType_Type())
priorityListDefQType.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListDefQType.setStatus(_A)
class _PriorityListQHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_PriorityListQHigh_Type.__name__=_C
_PriorityListQHigh_Object=MibTableColumn
priorityListQHigh=_PriorityListQHigh_Object((1,3,6,1,4,1,5651,3,21,5,1,1,3),_PriorityListQHigh_Type())
priorityListQHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListQHigh.setStatus(_A)
class _PriorityListQMedium_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PriorityListQMedium_Type.__name__=_C
_PriorityListQMedium_Object=MibTableColumn
priorityListQMedium=_PriorityListQMedium_Object((1,3,6,1,4,1,5651,3,21,5,1,1,4),_PriorityListQMedium_Type())
priorityListQMedium.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListQMedium.setStatus(_A)
class _PriorityListQNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,45000))
_PriorityListQNormal_Type.__name__=_C
_PriorityListQNormal_Object=MibTableColumn
priorityListQNormal=_PriorityListQNormal_Object((1,3,6,1,4,1,5651,3,21,5,1,1,5),_PriorityListQNormal_Type())
priorityListQNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListQNormal.setStatus(_A)
class _PriorityListQLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PriorityListQLow_Type.__name__=_C
_PriorityListQLow_Object=MibTableColumn
priorityListQLow=_PriorityListQLow_Object((1,3,6,1,4,1,5651,3,21,5,1,1,6),_PriorityListQLow_Type())
priorityListQLow.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListQLow.setStatus(_A)
_PriorityListWredGrpName_Type=DisplayString
_PriorityListWredGrpName_Object=MibTableColumn
priorityListWredGrpName=_PriorityListWredGrpName_Object((1,3,6,1,4,1,5651,3,21,5,1,1,7),_PriorityListWredGrpName_Type())
priorityListWredGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListWredGrpName.setStatus(_A)
class _PriorityListDropType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_PriorityListDropType_Type.__name__=_C
_PriorityListDropType_Object=MibTableColumn
priorityListDropType=_PriorityListDropType_Object((1,3,6,1,4,1,5651,3,21,5,1,1,8),_PriorityListDropType_Type())
priorityListDropType.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListDropType.setStatus(_A)
_PriorityListStatus_Type=RowStatus
_PriorityListStatus_Object=MibTableColumn
priorityListStatus=_PriorityListStatus_Object((1,3,6,1,4,1,5651,3,21,5,1,1,9),_PriorityListStatus_Type())
priorityListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListStatus.setStatus(_A)
_PriorityListRuleTable_Object=MibTable
priorityListRuleTable=_PriorityListRuleTable_Object((1,3,6,1,4,1,5651,3,21,5,2))
if mibBuilder.loadTexts:priorityListRuleTable.setStatus(_A)
_PriorityListRuleEntry_Object=MibTableRow
priorityListRuleEntry=_PriorityListRuleEntry_Object((1,3,6,1,4,1,5651,3,21,5,2,1))
priorityListRuleEntry.setIndexNames((0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:priorityListRuleEntry.setStatus(_A)
class _PriorityListNoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PriorityListNoIndex_Type.__name__=_C
_PriorityListNoIndex_Object=MibTableColumn
priorityListNoIndex=_PriorityListNoIndex_Object((1,3,6,1,4,1,5651,3,21,5,2,1,1),_PriorityListNoIndex_Type())
priorityListNoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:priorityListNoIndex.setStatus(_A)
_PriorityListRuleIndex_Type=Integer32
_PriorityListRuleIndex_Object=MibTableColumn
priorityListRuleIndex=_PriorityListRuleIndex_Object((1,3,6,1,4,1,5651,3,21,5,2,1,2),_PriorityListRuleIndex_Type())
priorityListRuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListRuleIndex.setStatus(_A)
class _PriorityListRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_PriorityListRuleType_Type.__name__=_C
_PriorityListRuleType_Object=MibTableColumn
priorityListRuleType=_PriorityListRuleType_Object((1,3,6,1,4,1,5651,3,21,5,2,1,3),_PriorityListRuleType_Type())
priorityListRuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListRuleType.setStatus(_A)
class _PriorityListRulePriType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_PriorityListRulePriType_Type.__name__=_C
_PriorityListRulePriType_Object=MibTableColumn
priorityListRulePriType=_PriorityListRulePriType_Object((1,3,6,1,4,1,5651,3,21,5,2,1,4),_PriorityListRulePriType_Type())
priorityListRulePriType.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListRulePriType.setStatus(_A)
_PriorityListforIntIfIndex_Type=Integer32
_PriorityListforIntIfIndex_Object=MibTableColumn
priorityListforIntIfIndex=_PriorityListforIntIfIndex_Object((1,3,6,1,4,1,5651,3,21,5,2,1,5),_PriorityListforIntIfIndex_Type())
priorityListforIntIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListforIntIfIndex.setStatus(_A)
class _PriorityListProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip',1),('arp',2),('llx',3)))
_PriorityListProtocolType_Type.__name__=_C
_PriorityListProtocolType_Object=MibTableColumn
priorityListProtocolType=_PriorityListProtocolType_Object((1,3,6,1,4,1,5651,3,21,5,2,1,6),_PriorityListProtocolType_Type())
priorityListProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListProtocolType.setStatus(_A)
class _PriorityListClassFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),('gt',2),('list',3),('lt',4),(_K,5),(_L,6)))
_PriorityListClassFlag_Type.__name__=_C
_PriorityListClassFlag_Object=MibTableColumn
priorityListClassFlag=_PriorityListClassFlag_Object((1,3,6,1,4,1,5651,3,21,5,2,1,7),_PriorityListClassFlag_Type())
priorityListClassFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListClassFlag.setStatus(_A)
class _PriorityListGtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PriorityListGtSize_Type.__name__=_C
_PriorityListGtSize_Object=MibTableColumn
priorityListGtSize=_PriorityListGtSize_Object((1,3,6,1,4,1,5651,3,21,5,2,1,8),_PriorityListGtSize_Type())
priorityListGtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListGtSize.setStatus(_A)
class _PriorityListLtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PriorityListLtSize_Type.__name__=_C
_PriorityListLtSize_Object=MibTableColumn
priorityListLtSize=_PriorityListLtSize_Object((1,3,6,1,4,1,5651,3,21,5,2,1,9),_PriorityListLtSize_Type())
priorityListLtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListLtSize.setStatus(_A)
class _PriorityListAccListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_PriorityListAccListNo_Type.__name__=_C
_PriorityListAccListNo_Object=MibTableColumn
priorityListAccListNo=_PriorityListAccListNo_Object((1,3,6,1,4,1,5651,3,21,5,2,1,10),_PriorityListAccListNo_Type())
priorityListAccListNo.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListAccListNo.setStatus(_A)
class _PriorityListTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PriorityListTCPPort_Type.__name__=_C
_PriorityListTCPPort_Object=MibTableColumn
priorityListTCPPort=_PriorityListTCPPort_Object((1,3,6,1,4,1,5651,3,21,5,2,1,11),_PriorityListTCPPort_Type())
priorityListTCPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListTCPPort.setStatus(_A)
class _PriorityListUDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PriorityListUDPPort_Type.__name__=_C
_PriorityListUDPPort_Object=MibTableColumn
priorityListUDPPort=_PriorityListUDPPort_Object((1,3,6,1,4,1,5651,3,21,5,2,1,12),_PriorityListUDPPort_Type())
priorityListUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListUDPPort.setStatus(_A)
_PriorityListRuleStatus_Type=RowStatus
_PriorityListRuleStatus_Object=MibTableColumn
priorityListRuleStatus=_PriorityListRuleStatus_Object((1,3,6,1,4,1,5651,3,21,5,2,1,13),_PriorityListRuleStatus_Type())
priorityListRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:priorityListRuleStatus.setStatus(_A)
_CustomList_ObjectIdentity=ObjectIdentity
customList=_CustomList_ObjectIdentity((1,3,6,1,4,1,5651,3,21,6))
_CustomListTable_Object=MibTable
customListTable=_CustomListTable_Object((1,3,6,1,4,1,5651,3,21,6,1))
if mibBuilder.loadTexts:customListTable.setStatus(_A)
_CustomListEntry_Object=MibTableRow
customListEntry=_CustomListEntry_Object((1,3,6,1,4,1,5651,3,21,6,1,1))
customListEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:customListEntry.setStatus(_A)
class _CustomListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CustomListNo_Type.__name__=_C
_CustomListNo_Object=MibTableColumn
customListNo=_CustomListNo_Object((1,3,6,1,4,1,5651,3,21,6,1,1,1),_CustomListNo_Type())
customListNo.setMaxAccess(_B)
if mibBuilder.loadTexts:customListNo.setStatus(_A)
class _CustomListDefNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CustomListDefNo_Type.__name__=_C
_CustomListDefNo_Object=MibTableColumn
customListDefNo=_CustomListDefNo_Object((1,3,6,1,4,1,5651,3,21,6,1,1,2),_CustomListDefNo_Type())
customListDefNo.setMaxAccess(_B)
if mibBuilder.loadTexts:customListDefNo.setStatus(_A)
_CustomListWredName_Type=DisplayString
_CustomListWredName_Object=MibTableColumn
customListWredName=_CustomListWredName_Object((1,3,6,1,4,1,5651,3,21,6,1,1,3),_CustomListWredName_Type())
customListWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:customListWredName.setStatus(_A)
class _CustomListDropType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_CustomListDropType_Type.__name__=_C
_CustomListDropType_Object=MibTableColumn
customListDropType=_CustomListDropType_Object((1,3,6,1,4,1,5651,3,21,6,1,1,4),_CustomListDropType_Type())
customListDropType.setMaxAccess(_B)
if mibBuilder.loadTexts:customListDropType.setStatus(_A)
_CustomListStatus_Type=RowStatus
_CustomListStatus_Object=MibTableColumn
customListStatus=_CustomListStatus_Object((1,3,6,1,4,1,5651,3,21,6,1,1,5),_CustomListStatus_Type())
customListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:customListStatus.setStatus(_A)
_CustomListRuleTable_Object=MibTable
customListRuleTable=_CustomListRuleTable_Object((1,3,6,1,4,1,5651,3,21,6,2))
if mibBuilder.loadTexts:customListRuleTable.setStatus(_A)
_CustomListRuleEntry_Object=MibTableRow
customListRuleEntry=_CustomListRuleEntry_Object((1,3,6,1,4,1,5651,3,21,6,2,1))
customListRuleEntry.setIndexNames((0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:customListRuleEntry.setStatus(_A)
class _CustomListNoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CustomListNoIndex_Type.__name__=_C
_CustomListNoIndex_Object=MibTableColumn
customListNoIndex=_CustomListNoIndex_Object((1,3,6,1,4,1,5651,3,21,6,2,1,1),_CustomListNoIndex_Type())
customListNoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:customListNoIndex.setStatus(_A)
_CustomListIndex_Type=Integer32
_CustomListIndex_Object=MibTableColumn
customListIndex=_CustomListIndex_Object((1,3,6,1,4,1,5651,3,21,6,2,1,2),_CustomListIndex_Type())
customListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:customListIndex.setStatus(_A)
class _CustomListICMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CustomListICMP_Type.__name__=_C
_CustomListICMP_Object=MibTableColumn
customListICMP=_CustomListICMP_Object((1,3,6,1,4,1,5651,3,21,6,2,1,3),_CustomListICMP_Type())
customListICMP.setMaxAccess(_B)
if mibBuilder.loadTexts:customListICMP.setStatus(_A)
class _CustomListIGMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CustomListIGMP_Type.__name__=_C
_CustomListIGMP_Object=MibTableColumn
customListIGMP=_CustomListIGMP_Object((1,3,6,1,4,1,5651,3,21,6,2,1,4),_CustomListIGMP_Type())
customListIGMP.setMaxAccess(_B)
if mibBuilder.loadTexts:customListIGMP.setStatus(_A)
class _CustomListQNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CustomListQNo_Type.__name__=_C
_CustomListQNo_Object=MibTableColumn
customListQNo=_CustomListQNo_Object((1,3,6,1,4,1,5651,3,21,6,2,1,5),_CustomListQNo_Type())
customListQNo.setMaxAccess(_B)
if mibBuilder.loadTexts:customListQNo.setStatus(_A)
class _CustomListFragPktQNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CustomListFragPktQNo_Type.__name__=_C
_CustomListFragPktQNo_Object=MibTableColumn
customListFragPktQNo=_CustomListFragPktQNo_Object((1,3,6,1,4,1,5651,3,21,6,2,1,6),_CustomListFragPktQNo_Type())
customListFragPktQNo.setMaxAccess(_B)
if mibBuilder.loadTexts:customListFragPktQNo.setStatus(_A)
class _CustomListPktEtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1500))
_CustomListPktEtSize_Type.__name__=_C
_CustomListPktEtSize_Object=MibTableColumn
customListPktEtSize=_CustomListPktEtSize_Object((1,3,6,1,4,1,5651,3,21,6,2,1,7),_CustomListPktEtSize_Type())
customListPktEtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:customListPktEtSize.setStatus(_A)
class _CustomListPktGtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1500))
_CustomListPktGtSize_Type.__name__=_C
_CustomListPktGtSize_Object=MibTableColumn
customListPktGtSize=_CustomListPktGtSize_Object((1,3,6,1,4,1,5651,3,21,6,2,1,8),_CustomListPktGtSize_Type())
customListPktGtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:customListPktGtSize.setStatus(_A)
class _CustomListPktLtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1500))
_CustomListPktLtSize_Type.__name__=_C
_CustomListPktLtSize_Object=MibTableColumn
customListPktLtSize=_CustomListPktLtSize_Object((1,3,6,1,4,1,5651,3,21,6,2,1,9),_CustomListPktLtSize_Type())
customListPktLtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:customListPktLtSize.setStatus(_A)
_CustomListIpSrcAddr_Type=IpAddress
_CustomListIpSrcAddr_Object=MibTableColumn
customListIpSrcAddr=_CustomListIpSrcAddr_Object((1,3,6,1,4,1,5651,3,21,6,2,1,10),_CustomListIpSrcAddr_Type())
customListIpSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:customListIpSrcAddr.setStatus(_A)
_CustomListIpSrcAddrMask_Type=IpAddress
_CustomListIpSrcAddrMask_Object=MibTableColumn
customListIpSrcAddrMask=_CustomListIpSrcAddrMask_Object((1,3,6,1,4,1,5651,3,21,6,2,1,11),_CustomListIpSrcAddrMask_Type())
customListIpSrcAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:customListIpSrcAddrMask.setStatus(_A)
_CustomListIpDestAddr_Type=IpAddress
_CustomListIpDestAddr_Object=MibTableColumn
customListIpDestAddr=_CustomListIpDestAddr_Object((1,3,6,1,4,1,5651,3,21,6,2,1,12),_CustomListIpDestAddr_Type())
customListIpDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:customListIpDestAddr.setStatus(_A)
_CustomListIpDestAddrMask_Type=IpAddress
_CustomListIpDestAddrMask_Object=MibTableColumn
customListIpDestAddrMask=_CustomListIpDestAddrMask_Object((1,3,6,1,4,1,5651,3,21,6,2,1,13),_CustomListIpDestAddrMask_Type())
customListIpDestAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:customListIpDestAddrMask.setStatus(_A)
class _CustomListAccListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_CustomListAccListNo_Type.__name__=_C
_CustomListAccListNo_Object=MibTableColumn
customListAccListNo=_CustomListAccListNo_Object((1,3,6,1,4,1,5651,3,21,6,2,1,14),_CustomListAccListNo_Type())
customListAccListNo.setMaxAccess(_B)
if mibBuilder.loadTexts:customListAccListNo.setStatus(_A)
class _CustomListQByteCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CustomListQByteCount_Type.__name__=_C
_CustomListQByteCount_Object=MibTableColumn
customListQByteCount=_CustomListQByteCount_Object((1,3,6,1,4,1,5651,3,21,6,2,1,15),_CustomListQByteCount_Type())
customListQByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:customListQByteCount.setStatus(_A)
class _CustomListQLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CustomListQLimit_Type.__name__=_C
_CustomListQLimit_Object=MibTableColumn
customListQLimit=_CustomListQLimit_Object((1,3,6,1,4,1,5651,3,21,6,2,1,16),_CustomListQLimit_Type())
customListQLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:customListQLimit.setStatus(_A)
_CustomListTCPSrcAddr_Type=IpAddress
_CustomListTCPSrcAddr_Object=MibTableColumn
customListTCPSrcAddr=_CustomListTCPSrcAddr_Object((1,3,6,1,4,1,5651,3,21,6,2,1,17),_CustomListTCPSrcAddr_Type())
customListTCPSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:customListTCPSrcAddr.setStatus(_A)
_CustomListTCPSrcAddrMask_Type=IpAddress
_CustomListTCPSrcAddrMask_Object=MibTableColumn
customListTCPSrcAddrMask=_CustomListTCPSrcAddrMask_Object((1,3,6,1,4,1,5651,3,21,6,2,1,18),_CustomListTCPSrcAddrMask_Type())
customListTCPSrcAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:customListTCPSrcAddrMask.setStatus(_A)
class _CustomListTCPSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CustomListTCPSrcPort_Type.__name__=_C
_CustomListTCPSrcPort_Object=MibTableColumn
customListTCPSrcPort=_CustomListTCPSrcPort_Object((1,3,6,1,4,1,5651,3,21,6,2,1,19),_CustomListTCPSrcPort_Type())
customListTCPSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:customListTCPSrcPort.setStatus(_A)
_CustomListTCPDestAddr_Type=IpAddress
_CustomListTCPDestAddr_Object=MibTableColumn
customListTCPDestAddr=_CustomListTCPDestAddr_Object((1,3,6,1,4,1,5651,3,21,6,2,1,20),_CustomListTCPDestAddr_Type())
customListTCPDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:customListTCPDestAddr.setStatus(_A)
_CustomListTCPDestAddrMask_Type=IpAddress
_CustomListTCPDestAddrMask_Object=MibTableColumn
customListTCPDestAddrMask=_CustomListTCPDestAddrMask_Object((1,3,6,1,4,1,5651,3,21,6,2,1,21),_CustomListTCPDestAddrMask_Type())
customListTCPDestAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:customListTCPDestAddrMask.setStatus(_A)
class _CustomListTCPDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CustomListTCPDestPort_Type.__name__=_C
_CustomListTCPDestPort_Object=MibTableColumn
customListTCPDestPort=_CustomListTCPDestPort_Object((1,3,6,1,4,1,5651,3,21,6,2,1,22),_CustomListTCPDestPort_Type())
customListTCPDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:customListTCPDestPort.setStatus(_A)
_CustomListUDPSrcAddr_Type=IpAddress
_CustomListUDPSrcAddr_Object=MibTableColumn
customListUDPSrcAddr=_CustomListUDPSrcAddr_Object((1,3,6,1,4,1,5651,3,21,6,2,1,23),_CustomListUDPSrcAddr_Type())
customListUDPSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:customListUDPSrcAddr.setStatus(_A)
_CustomListUDPSrcAddrMask_Type=IpAddress
_CustomListUDPSrcAddrMask_Object=MibTableColumn
customListUDPSrcAddrMask=_CustomListUDPSrcAddrMask_Object((1,3,6,1,4,1,5651,3,21,6,2,1,24),_CustomListUDPSrcAddrMask_Type())
customListUDPSrcAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:customListUDPSrcAddrMask.setStatus(_A)
class _CustomListUDPSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CustomListUDPSrcPort_Type.__name__=_C
_CustomListUDPSrcPort_Object=MibTableColumn
customListUDPSrcPort=_CustomListUDPSrcPort_Object((1,3,6,1,4,1,5651,3,21,6,2,1,25),_CustomListUDPSrcPort_Type())
customListUDPSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:customListUDPSrcPort.setStatus(_A)
_CustomListUDPDestAddr_Type=IpAddress
_CustomListUDPDestAddr_Object=MibTableColumn
customListUDPDestAddr=_CustomListUDPDestAddr_Object((1,3,6,1,4,1,5651,3,21,6,2,1,26),_CustomListUDPDestAddr_Type())
customListUDPDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:customListUDPDestAddr.setStatus(_A)
_CustomListUDPDestAddrMask_Type=IpAddress
_CustomListUDPDestAddrMask_Object=MibTableColumn
customListUDPDestAddrMask=_CustomListUDPDestAddrMask_Object((1,3,6,1,4,1,5651,3,21,6,2,1,27),_CustomListUDPDestAddrMask_Type())
customListUDPDestAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:customListUDPDestAddrMask.setStatus(_A)
class _CustomListUDPDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CustomListUDPDestPort_Type.__name__=_C
_CustomListUDPDestPort_Object=MibTableColumn
customListUDPDestPort=_CustomListUDPDestPort_Object((1,3,6,1,4,1,5651,3,21,6,2,1,28),_CustomListUDPDestPort_Type())
customListUDPDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:customListUDPDestPort.setStatus(_A)
_CustomIntListIfIndex_Type=Integer32
_CustomIntListIfIndex_Object=MibTableColumn
customIntListIfIndex=_CustomIntListIfIndex_Object((1,3,6,1,4,1,5651,3,21,6,2,1,29),_CustomIntListIfIndex_Type())
customIntListIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:customIntListIfIndex.setStatus(_A)
_CustomListRuleStatus_Type=RowStatus
_CustomListRuleStatus_Object=MibTableColumn
customListRuleStatus=_CustomListRuleStatus_Object((1,3,6,1,4,1,5651,3,21,6,2,1,30),_CustomListRuleStatus_Type())
customListRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:customListRuleStatus.setStatus(_A)
_WredGroup_ObjectIdentity=ObjectIdentity
wredGroup=_WredGroup_ObjectIdentity((1,3,6,1,4,1,5651,3,21,7))
_WredGrpTable_Object=MibTable
wredGrpTable=_WredGrpTable_Object((1,3,6,1,4,1,5651,3,21,7,1))
if mibBuilder.loadTexts:wredGrpTable.setStatus(_A)
_WredGrpEntry_Object=MibTableRow
wredGrpEntry=_WredGrpEntry_Object((1,3,6,1,4,1,5651,3,21,7,1,1))
wredGrpEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:wredGrpEntry.setStatus(_A)
_WredGrpName_Type=DisplayString
_WredGrpName_Object=MibTableColumn
wredGrpName=_WredGrpName_Object((1,3,6,1,4,1,5651,3,21,7,1,1,1),_WredGrpName_Type())
wredGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpName.setStatus(_A)
_WredGrpExpWeight_Type=Integer32
_WredGrpExpWeight_Object=MibTableColumn
wredGrpExpWeight=_WredGrpExpWeight_Object((1,3,6,1,4,1,5651,3,21,7,1,1,2),_WredGrpExpWeight_Type())
wredGrpExpWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpExpWeight.setStatus(_A)
_WredGrpStatus_Type=RowStatus
_WredGrpStatus_Object=MibTableColumn
wredGrpStatus=_WredGrpStatus_Object((1,3,6,1,4,1,5651,3,21,7,1,1,3),_WredGrpStatus_Type())
wredGrpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpStatus.setStatus(_A)
_WredGrpPreTable_Object=MibTable
wredGrpPreTable=_WredGrpPreTable_Object((1,3,6,1,4,1,5651,3,21,7,2))
if mibBuilder.loadTexts:wredGrpPreTable.setStatus(_A)
_WredGrpPreEntry_Object=MibTableRow
wredGrpPreEntry=_WredGrpPreEntry_Object((1,3,6,1,4,1,5651,3,21,7,2,1))
wredGrpPreEntry.setIndexNames((0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:wredGrpPreEntry.setStatus(_A)
_WredGrpPreName_Type=DisplayString
_WredGrpPreName_Object=MibTableColumn
wredGrpPreName=_WredGrpPreName_Object((1,3,6,1,4,1,5651,3,21,7,2,1,1),_WredGrpPreName_Type())
wredGrpPreName.setMaxAccess(_D)
if mibBuilder.loadTexts:wredGrpPreName.setStatus(_A)
class _WredGrpPreNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WredGrpPreNo_Type.__name__=_C
_WredGrpPreNo_Object=MibTableColumn
wredGrpPreNo=_WredGrpPreNo_Object((1,3,6,1,4,1,5651,3,21,7,2,1,2),_WredGrpPreNo_Type())
wredGrpPreNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpPreNo.setStatus(_A)
class _WredGrpPreMinBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WredGrpPreMinBytes_Type.__name__=_C
_WredGrpPreMinBytes_Object=MibTableColumn
wredGrpPreMinBytes=_WredGrpPreMinBytes_Object((1,3,6,1,4,1,5651,3,21,7,2,1,3),_WredGrpPreMinBytes_Type())
wredGrpPreMinBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpPreMinBytes.setStatus(_A)
class _WredGrpPreMaxBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WredGrpPreMaxBytes_Type.__name__=_C
_WredGrpPreMaxBytes_Object=MibTableColumn
wredGrpPreMaxBytes=_WredGrpPreMaxBytes_Object((1,3,6,1,4,1,5651,3,21,7,2,1,4),_WredGrpPreMaxBytes_Type())
wredGrpPreMaxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpPreMaxBytes.setStatus(_A)
class _WredGrpPreDenominator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WredGrpPreDenominator_Type.__name__=_C
_WredGrpPreDenominator_Object=MibTableColumn
wredGrpPreDenominator=_WredGrpPreDenominator_Object((1,3,6,1,4,1,5651,3,21,7,2,1,5),_WredGrpPreDenominator_Type())
wredGrpPreDenominator.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpPreDenominator.setStatus(_A)
_WredGrpPreRandomDropsBytes_Type=Integer32
_WredGrpPreRandomDropsBytes_Object=MibTableColumn
wredGrpPreRandomDropsBytes=_WredGrpPreRandomDropsBytes_Object((1,3,6,1,4,1,5651,3,21,7,2,1,6),_WredGrpPreRandomDropsBytes_Type())
wredGrpPreRandomDropsBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:wredGrpPreRandomDropsBytes.setStatus(_A)
_WredGrpPreTailDropsBytes_Type=Integer32
_WredGrpPreTailDropsBytes_Object=MibTableColumn
wredGrpPreTailDropsBytes=_WredGrpPreTailDropsBytes_Object((1,3,6,1,4,1,5651,3,21,7,2,1,7),_WredGrpPreTailDropsBytes_Type())
wredGrpPreTailDropsBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:wredGrpPreTailDropsBytes.setStatus(_A)
_WredGrpPreStatus_Type=RowStatus
_WredGrpPreStatus_Object=MibTableColumn
wredGrpPreStatus=_WredGrpPreStatus_Object((1,3,6,1,4,1,5651,3,21,7,2,1,8),_WredGrpPreStatus_Type())
wredGrpPreStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wredGrpPreStatus.setStatus(_A)
_IfWredTable_Object=MibTable
ifWredTable=_IfWredTable_Object((1,3,6,1,4,1,5651,3,21,7,3))
if mibBuilder.loadTexts:ifWredTable.setStatus(_A)
_IfWredEntry_Object=MibTableRow
ifWredEntry=_IfWredEntry_Object((1,3,6,1,4,1,5651,3,21,7,3,1))
ifWredEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:ifWredEntry.setStatus(_A)
_IfWredIfIndex_Type=Integer32
_IfWredIfIndex_Object=MibTableColumn
ifWredIfIndex=_IfWredIfIndex_Object((1,3,6,1,4,1,5651,3,21,7,3,1,1),_IfWredIfIndex_Type())
ifWredIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredIfIndex.setStatus(_A)
class _IfWredExpWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_IfWredExpWeight_Type.__name__=_C
_IfWredExpWeight_Object=MibTableColumn
ifWredExpWeight=_IfWredExpWeight_Object((1,3,6,1,4,1,5651,3,21,7,3,1,2),_IfWredExpWeight_Type())
ifWredExpWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredExpWeight.setStatus(_A)
_IfWredStatus_Type=RowStatus
_IfWredStatus_Object=MibTableColumn
ifWredStatus=_IfWredStatus_Object((1,3,6,1,4,1,5651,3,21,7,3,1,3),_IfWredStatus_Type())
ifWredStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredStatus.setStatus(_A)
_IfWredRuleTable_Object=MibTable
ifWredRuleTable=_IfWredRuleTable_Object((1,3,6,1,4,1,5651,3,21,7,4))
if mibBuilder.loadTexts:ifWredRuleTable.setStatus(_A)
_IfWredRuleEntry_Object=MibTableRow
ifWredRuleEntry=_IfWredRuleEntry_Object((1,3,6,1,4,1,5651,3,21,7,4,1))
ifWredRuleEntry.setIndexNames((0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:ifWredRuleEntry.setStatus(_A)
_IfWredRuleIfIndex_Type=Integer32
_IfWredRuleIfIndex_Object=MibTableColumn
ifWredRuleIfIndex=_IfWredRuleIfIndex_Object((1,3,6,1,4,1,5651,3,21,7,4,1,1),_IfWredRuleIfIndex_Type())
ifWredRuleIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredRuleIfIndex.setStatus(_A)
class _IfWredPreNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_IfWredPreNo_Type.__name__=_C
_IfWredPreNo_Object=MibTableColumn
ifWredPreNo=_IfWredPreNo_Object((1,3,6,1,4,1,5651,3,21,7,4,1,2),_IfWredPreNo_Type())
ifWredPreNo.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredPreNo.setStatus(_A)
class _IfWredPreMinBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,65535))
_IfWredPreMinBytes_Type.__name__=_C
_IfWredPreMinBytes_Object=MibTableColumn
ifWredPreMinBytes=_IfWredPreMinBytes_Object((1,3,6,1,4,1,5651,3,21,7,4,1,3),_IfWredPreMinBytes_Type())
ifWredPreMinBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredPreMinBytes.setStatus(_A)
class _IfWredPreMaxBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_IfWredPreMaxBytes_Type.__name__=_C
_IfWredPreMaxBytes_Object=MibTableColumn
ifWredPreMaxBytes=_IfWredPreMaxBytes_Object((1,3,6,1,4,1,5651,3,21,7,4,1,4),_IfWredPreMaxBytes_Type())
ifWredPreMaxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredPreMaxBytes.setStatus(_A)
class _IfWredPreDenominator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IfWredPreDenominator_Type.__name__=_C
_IfWredPreDenominator_Object=MibTableColumn
ifWredPreDenominator=_IfWredPreDenominator_Object((1,3,6,1,4,1,5651,3,21,7,4,1,5),_IfWredPreDenominator_Type())
ifWredPreDenominator.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredPreDenominator.setStatus(_A)
_IfWredRuleStatus_Type=RowStatus
_IfWredRuleStatus_Object=MibTableColumn
ifWredRuleStatus=_IfWredRuleStatus_Object((1,3,6,1,4,1,5651,3,21,7,4,1,6),_IfWredRuleStatus_Type())
ifWredRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWredRuleStatus.setStatus(_A)
_IfQos_ObjectIdentity=ObjectIdentity
ifQos=_IfQos_ObjectIdentity((1,3,6,1,4,1,5651,3,21,8))
_IfQosTable_Object=MibTable
ifQosTable=_IfQosTable_Object((1,3,6,1,4,1,5651,3,21,8,1))
if mibBuilder.loadTexts:ifQosTable.setStatus(_A)
_IfQosEntry_Object=MibTableRow
ifQosEntry=_IfQosEntry_Object((1,3,6,1,4,1,5651,3,21,8,1,1))
ifQosEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:ifQosEntry.setStatus(_A)
_IfQosIfIndex_Type=Integer32
_IfQosIfIndex_Object=MibTableColumn
ifQosIfIndex=_IfQosIfIndex_Object((1,3,6,1,4,1,5651,3,21,8,1,1,1),_IfQosIfIndex_Type())
ifQosIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosIfIndex.setStatus(_A)
_IfQosOutputPolicyName_Type=DisplayString
_IfQosOutputPolicyName_Object=MibTableColumn
ifQosOutputPolicyName=_IfQosOutputPolicyName_Object((1,3,6,1,4,1,5651,3,21,8,1,1,2),_IfQosOutputPolicyName_Type())
ifQosOutputPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosOutputPolicyName.setStatus(_A)
_IfQosInputPolicyName_Type=DisplayString
_IfQosInputPolicyName_Object=MibTableColumn
ifQosInputPolicyName=_IfQosInputPolicyName_Object((1,3,6,1,4,1,5651,3,21,8,1,1,3),_IfQosInputPolicyName_Type())
ifQosInputPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosInputPolicyName.setStatus(_A)
class _IfQosListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pq',1),('cq',2),('wred',3),('cbwfq',4),(_A0,5),('fifo',6)))
_IfQosListType_Type.__name__=_C
_IfQosListType_Object=MibTableColumn
ifQosListType=_IfQosListType_Object((1,3,6,1,4,1,5651,3,21,8,1,1,4),_IfQosListType_Type())
ifQosListType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosListType.setStatus(_A)
_IfQosListNo_Type=Integer32
_IfQosListNo_Object=MibTableColumn
ifQosListNo=_IfQosListNo_Object((1,3,6,1,4,1,5651,3,21,8,1,1,5),_IfQosListNo_Type())
ifQosListNo.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosListNo.setStatus(_A)
_IfQosTrafficShapeRate_Type=Integer32
_IfQosTrafficShapeRate_Object=MibTableColumn
ifQosTrafficShapeRate=_IfQosTrafficShapeRate_Object((1,3,6,1,4,1,5651,3,21,8,1,1,6),_IfQosTrafficShapeRate_Type())
ifQosTrafficShapeRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosTrafficShapeRate.setStatus(_A)
_IfQosTrafficShapeBurst_Type=Integer32
_IfQosTrafficShapeBurst_Object=MibTableColumn
ifQosTrafficShapeBurst=_IfQosTrafficShapeBurst_Object((1,3,6,1,4,1,5651,3,21,8,1,1,7),_IfQosTrafficShapeBurst_Type())
ifQosTrafficShapeBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosTrafficShapeBurst.setStatus(_A)
_IfQosStatus_Type=RowStatus
_IfQosStatus_Object=MibTableColumn
ifQosStatus=_IfQosStatus_Object((1,3,6,1,4,1,5651,3,21,8,1,1,8),_IfQosStatus_Type())
ifQosStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifQosStatus.setStatus(_A)
_IfQosIfTable_Object=MibTable
ifQosIfTable=_IfQosIfTable_Object((1,3,6,1,4,1,5651,3,21,8,2))
if mibBuilder.loadTexts:ifQosIfTable.setStatus(_A)
_IfQosIfEntry_Object=MibTableRow
ifQosIfEntry=_IfQosIfEntry_Object((1,3,6,1,4,1,5651,3,21,8,2,1))
ifQosIfEntry.setIndexNames((0,_E,'ifQosIfQIndex'))
if mibBuilder.loadTexts:ifQosIfEntry.setStatus(_A)
_IfQosIfQIfIndex_Type=Integer32
_IfQosIfQIfIndex_Object=MibTableColumn
ifQosIfQIfIndex=_IfQosIfQIfIndex_Object((1,3,6,1,4,1,5651,3,21,8,2,1,1),_IfQosIfQIfIndex_Type())
ifQosIfQIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosIfQIfIndex.setStatus(_A)
class _IfQosIfQType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pq',1),('cq',2),('wred',3),('cbwfq',4),(_A0,5)))
_IfQosIfQType_Type.__name__=_C
_IfQosIfQType_Object=MibTableColumn
ifQosIfQType=_IfQosIfQType_Object((1,3,6,1,4,1,5651,3,21,8,2,1,2),_IfQosIfQType_Type())
ifQosIfQType.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosIfQType.setStatus(_A)
_IfQosIfQNum_Type=Integer32
_IfQosIfQNum_Object=MibTableColumn
ifQosIfQNum=_IfQosIfQNum_Object((1,3,6,1,4,1,5651,3,21,8,2,1,3),_IfQosIfQNum_Type())
ifQosIfQNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosIfQNum.setStatus(_A)
_IfQosTotalBytes_Type=Integer32
_IfQosTotalBytes_Object=MibTableColumn
ifQosTotalBytes=_IfQosTotalBytes_Object((1,3,6,1,4,1,5651,3,21,8,2,1,4),_IfQosTotalBytes_Type())
ifQosTotalBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalBytes.setStatus(_A)
_IfQosCurTotalBytes_Type=Integer32
_IfQosCurTotalBytes_Object=MibTableColumn
ifQosCurTotalBytes=_IfQosCurTotalBytes_Object((1,3,6,1,4,1,5651,3,21,8,2,1,5),_IfQosCurTotalBytes_Type())
ifQosCurTotalBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosCurTotalBytes.setStatus(_A)
_IfQosTotalInputPkts_Type=Counter32
_IfQosTotalInputPkts_Object=MibTableColumn
ifQosTotalInputPkts=_IfQosTotalInputPkts_Object((1,3,6,1,4,1,5651,3,21,8,2,1,6),_IfQosTotalInputPkts_Type())
ifQosTotalInputPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalInputPkts.setStatus(_A)
_IfQosTotalInputBytes_Type=Counter32
_IfQosTotalInputBytes_Object=MibTableColumn
ifQosTotalInputBytes=_IfQosTotalInputBytes_Object((1,3,6,1,4,1,5651,3,21,8,2,1,7),_IfQosTotalInputBytes_Type())
ifQosTotalInputBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalInputBytes.setStatus(_A)
_IfQosTotalOutputPkts_Type=Counter32
_IfQosTotalOutputPkts_Object=MibTableColumn
ifQosTotalOutputPkts=_IfQosTotalOutputPkts_Object((1,3,6,1,4,1,5651,3,21,8,2,1,8),_IfQosTotalOutputPkts_Type())
ifQosTotalOutputPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalOutputPkts.setStatus(_A)
_IfQosTotalOutputBytes_Type=Counter32
_IfQosTotalOutputBytes_Object=MibTableColumn
ifQosTotalOutputBytes=_IfQosTotalOutputBytes_Object((1,3,6,1,4,1,5651,3,21,8,2,1,9),_IfQosTotalOutputBytes_Type())
ifQosTotalOutputBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalOutputBytes.setStatus(_A)
_IfQosTotalDropPkts_Type=Counter32
_IfQosTotalDropPkts_Object=MibTableColumn
ifQosTotalDropPkts=_IfQosTotalDropPkts_Object((1,3,6,1,4,1,5651,3,21,8,2,1,10),_IfQosTotalDropPkts_Type())
ifQosTotalDropPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalDropPkts.setStatus(_A)
_IfQosTotalDropBytes_Type=Counter32
_IfQosTotalDropBytes_Object=MibTableColumn
ifQosTotalDropBytes=_IfQosTotalDropBytes_Object((1,3,6,1,4,1,5651,3,21,8,2,1,11),_IfQosTotalDropBytes_Type())
ifQosTotalDropBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosTotalDropBytes.setStatus(_A)
_IfQosActiveQCnt_Type=Integer32
_IfQosActiveQCnt_Object=MibTableColumn
ifQosActiveQCnt=_IfQosActiveQCnt_Object((1,3,6,1,4,1,5651,3,21,8,2,1,12),_IfQosActiveQCnt_Type())
ifQosActiveQCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosActiveQCnt.setStatus(_A)
_IfQosCBWFQActQCnt_Type=Integer32
_IfQosCBWFQActQCnt_Object=MibTableColumn
ifQosCBWFQActQCnt=_IfQosCBWFQActQCnt_Object((1,3,6,1,4,1,5651,3,21,8,2,1,13),_IfQosCBWFQActQCnt_Type())
ifQosCBWFQActQCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosCBWFQActQCnt.setStatus(_A)
class _IfQosRSVPReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_IfQosRSVPReq_Type.__name__=_C
_IfQosRSVPReq_Object=MibTableColumn
ifQosRSVPReq=_IfQosRSVPReq_Object((1,3,6,1,4,1,5651,3,21,8,2,1,14),_IfQosRSVPReq_Type())
ifQosRSVPReq.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosRSVPReq.setStatus(_A)
_IfQosQTable_Object=MibTable
ifQosQTable=_IfQosQTable_Object((1,3,6,1,4,1,5651,3,21,8,3))
if mibBuilder.loadTexts:ifQosQTable.setStatus(_A)
_IfQosQEntry_Object=MibTableRow
ifQosQEntry=_IfQosQEntry_Object((1,3,6,1,4,1,5651,3,21,8,3,1))
ifQosQEntry.setIndexNames((0,_E,'ifQosQIndex'),(0,_E,'ifQosQId'))
if mibBuilder.loadTexts:ifQosQEntry.setStatus(_A)
_IfQosQIfIndex_Type=Integer32
_IfQosQIfIndex_Object=MibTableColumn
ifQosQIfIndex=_IfQosQIfIndex_Object((1,3,6,1,4,1,5651,3,21,8,3,1,1),_IfQosQIfIndex_Type())
ifQosQIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQIfIndex.setStatus(_A)
_IfQosQId_Type=Integer32
_IfQosQId_Object=MibTableColumn
ifQosQId=_IfQosQId_Object((1,3,6,1,4,1,5651,3,21,8,3,1,2),_IfQosQId_Type())
ifQosQId.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQId.setStatus(_A)
_IfQosQLimit_Type=Integer32
_IfQosQLimit_Object=MibTableColumn
ifQosQLimit=_IfQosQLimit_Object((1,3,6,1,4,1,5651,3,21,8,3,1,3),_IfQosQLimit_Type())
ifQosQLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQLimit.setStatus(_A)
_IfQosQSndPkts_Type=Counter32
_IfQosQSndPkts_Object=MibTableColumn
ifQosQSndPkts=_IfQosQSndPkts_Object((1,3,6,1,4,1,5651,3,21,8,3,1,4),_IfQosQSndPkts_Type())
ifQosQSndPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQSndPkts.setStatus(_A)
_IfQosQSndBytes_Type=Counter32
_IfQosQSndBytes_Object=MibTableColumn
ifQosQSndBytes=_IfQosQSndBytes_Object((1,3,6,1,4,1,5651,3,21,8,3,1,5),_IfQosQSndBytes_Type())
ifQosQSndBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQSndBytes.setStatus(_A)
_IfQosQDropPkts_Type=Counter32
_IfQosQDropPkts_Object=MibTableColumn
ifQosQDropPkts=_IfQosQDropPkts_Object((1,3,6,1,4,1,5651,3,21,8,3,1,6),_IfQosQDropPkts_Type())
ifQosQDropPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQDropPkts.setStatus(_A)
_IfQosQDropBytes_Type=Counter32
_IfQosQDropBytes_Object=MibTableColumn
ifQosQDropBytes=_IfQosQDropBytes_Object((1,3,6,1,4,1,5651,3,21,8,3,1,7),_IfQosQDropBytes_Type())
ifQosQDropBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQDropBytes.setStatus(_A)
_IfQosQCurBytes_Type=Integer32
_IfQosQCurBytes_Object=MibTableColumn
ifQosQCurBytes=_IfQosQCurBytes_Object((1,3,6,1,4,1,5651,3,21,8,3,1,8),_IfQosQCurBytes_Type())
ifQosQCurBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQCurBytes.setStatus(_A)
_IfQosQMaxSndBytes_Type=Counter32
_IfQosQMaxSndBytes_Object=MibTableColumn
ifQosQMaxSndBytes=_IfQosQMaxSndBytes_Object((1,3,6,1,4,1,5651,3,21,8,3,1,9),_IfQosQMaxSndBytes_Type())
ifQosQMaxSndBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ifQosQMaxSndBytes.setStatus(_A)
_CbwfqConf_ObjectIdentity=ObjectIdentity
cbwfqConf=_CbwfqConf_ObjectIdentity((1,3,6,1,4,1,5651,3,21,9))
_CbwfqConfMaxClassNum_Type=Integer32
_CbwfqConfMaxClassNum_Object=MibScalar
cbwfqConfMaxClassNum=_CbwfqConfMaxClassNum_Object((1,3,6,1,4,1,5651,3,21,9,1),_CbwfqConfMaxClassNum_Type())
cbwfqConfMaxClassNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cbwfqConfMaxClassNum.setStatus(_A)
_CbwfqConfMaxPolicyNum_Type=Integer32
_CbwfqConfMaxPolicyNum_Object=MibScalar
cbwfqConfMaxPolicyNum=_CbwfqConfMaxPolicyNum_Object((1,3,6,1,4,1,5651,3,21,9,2),_CbwfqConfMaxPolicyNum_Type())
cbwfqConfMaxPolicyNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cbwfqConfMaxPolicyNum.setStatus(_A)
_QosCar_ObjectIdentity=ObjectIdentity
qosCar=_QosCar_ObjectIdentity((1,3,6,1,4,1,5651,3,21,10))
_QosCarTable_Object=MibTable
qosCarTable=_QosCarTable_Object((1,3,6,1,4,1,5651,3,21,10,3))
if mibBuilder.loadTexts:qosCarTable.setStatus(_A)
_QosCarEntry_Object=MibTableRow
qosCarEntry=_QosCarEntry_Object((1,3,6,1,4,1,5651,3,21,10,3,1))
qosCarEntry.setIndexNames((0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:qosCarEntry.setStatus(_A)
_QosCarIndex_Type=Integer32
_QosCarIndex_Object=MibTableColumn
qosCarIndex=_QosCarIndex_Object((1,3,6,1,4,1,5651,3,21,10,3,1,1),_QosCarIndex_Type())
qosCarIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarIndex.setStatus(_A)
_QosCarIfIndex_Type=Integer32
_QosCarIfIndex_Object=MibTableColumn
qosCarIfIndex=_QosCarIfIndex_Object((1,3,6,1,4,1,5651,3,21,10,3,1,2),_QosCarIfIndex_Type())
qosCarIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarIfIndex.setStatus(_A)
_QosCarMaxBw_Type=Integer32
_QosCarMaxBw_Object=MibTableColumn
qosCarMaxBw=_QosCarMaxBw_Object((1,3,6,1,4,1,5651,3,21,10,3,1,3),_QosCarMaxBw_Type())
qosCarMaxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarMaxBw.setStatus(_A)
_QosCarNormalBw_Type=Integer32
_QosCarNormalBw_Object=MibTableColumn
qosCarNormalBw=_QosCarNormalBw_Object((1,3,6,1,4,1,5651,3,21,10,3,1,4),_QosCarNormalBw_Type())
qosCarNormalBw.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarNormalBw.setStatus(_A)
_QosCarExceedBw_Type=Integer32
_QosCarExceedBw_Object=MibTableColumn
qosCarExceedBw=_QosCarExceedBw_Object((1,3,6,1,4,1,5651,3,21,10,3,1,5),_QosCarExceedBw_Type())
qosCarExceedBw.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarExceedBw.setStatus(_A)
class _QosCarConformAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('continue',1),('drop',2),('transmit',3),(_A3,4),(_A4,5),(_A5,6),(_A6,7)))
_QosCarConformAct_Type.__name__=_C
_QosCarConformAct_Object=MibTableColumn
qosCarConformAct=_QosCarConformAct_Object((1,3,6,1,4,1,5651,3,21,10,3,1,6),_QosCarConformAct_Type())
qosCarConformAct.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarConformAct.setStatus(_A)
class _QosCarExceedAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('continue',1),('drop',2),('transmit',3),(_A3,4),(_A4,5),(_A5,6),(_A6,7)))
_QosCarExceedAct_Type.__name__=_C
_QosCarExceedAct_Object=MibTableColumn
qosCarExceedAct=_QosCarExceedAct_Object((1,3,6,1,4,1,5651,3,21,10,3,1,7),_QosCarExceedAct_Type())
qosCarExceedAct.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarExceedAct.setStatus(_A)
_QosCarConformActNo_Type=Integer32
_QosCarConformActNo_Object=MibTableColumn
qosCarConformActNo=_QosCarConformActNo_Object((1,3,6,1,4,1,5651,3,21,10,3,1,8),_QosCarConformActNo_Type())
qosCarConformActNo.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarConformActNo.setStatus(_A)
_QosCarExceedActNo_Type=Integer32
_QosCarExceedActNo_Object=MibTableColumn
qosCarExceedActNo=_QosCarExceedActNo_Object((1,3,6,1,4,1,5651,3,21,10,3,1,9),_QosCarExceedActNo_Type())
qosCarExceedActNo.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarExceedActNo.setStatus(_A)
_QosCarStatus_Type=RowStatus
_QosCarStatus_Object=MibTableColumn
qosCarStatus=_QosCarStatus_Object((1,3,6,1,4,1,5651,3,21,10,3,1,10),_QosCarStatus_Type())
qosCarStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarStatus.setStatus(_A)
_QosCarConformPkts_Type=Counter32
_QosCarConformPkts_Object=MibTableColumn
qosCarConformPkts=_QosCarConformPkts_Object((1,3,6,1,4,1,5651,3,21,10,3,1,11),_QosCarConformPkts_Type())
qosCarConformPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarConformPkts.setStatus(_A)
_QosCarConformBytes_Type=Counter32
_QosCarConformBytes_Object=MibTableColumn
qosCarConformBytes=_QosCarConformBytes_Object((1,3,6,1,4,1,5651,3,21,10,3,1,12),_QosCarConformBytes_Type())
qosCarConformBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarConformBytes.setStatus(_A)
_QosCarExceedPkts_Type=Counter32
_QosCarExceedPkts_Object=MibTableColumn
qosCarExceedPkts=_QosCarExceedPkts_Object((1,3,6,1,4,1,5651,3,21,10,3,1,13),_QosCarExceedPkts_Type())
qosCarExceedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarExceedPkts.setStatus(_A)
_QosCarExceedBytes_Type=Counter32
_QosCarExceedBytes_Object=MibTableColumn
qosCarExceedBytes=_QosCarExceedBytes_Object((1,3,6,1,4,1,5651,3,21,10,3,1,14),_QosCarExceedBytes_Type())
qosCarExceedBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarExceedBytes.setStatus(_A)
class _QosCarDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_QosCarDirection_Type.__name__=_C
_QosCarDirection_Object=MibTableColumn
qosCarDirection=_QosCarDirection_Object((1,3,6,1,4,1,5651,3,21,10,3,1,15),_QosCarDirection_Type())
qosCarDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarDirection.setStatus(_A)
class _QosCarAclGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_QosCarAclGrp_Type.__name__=_C
_QosCarAclGrp_Object=MibTableColumn
qosCarAclGrp=_QosCarAclGrp_Object((1,3,6,1,4,1,5651,3,21,10,3,1,16),_QosCarAclGrp_Type())
qosCarAclGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCarAclGrp.setStatus(_A)
_PolicyStatis_ObjectIdentity=ObjectIdentity
policyStatis=_PolicyStatis_ObjectIdentity((1,3,6,1,4,1,5651,3,21,20))
_PolicyStatisTable_Object=MibTable
policyStatisTable=_PolicyStatisTable_Object((1,3,6,1,4,1,5651,3,21,20,10))
if mibBuilder.loadTexts:policyStatisTable.setStatus(_A)
_PolicyStatisEntry_Object=MibTableRow
policyStatisEntry=_PolicyStatisEntry_Object((1,3,6,1,4,1,5651,3,21,20,10,1))
policyStatisEntry.setIndexNames((0,_E,_A7),(0,_E,_A8),(0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:policyStatisEntry.setStatus(_A)
_PolicyStatisIfIndex_Type=Unsigned32
_PolicyStatisIfIndex_Object=MibTableColumn
policyStatisIfIndex=_PolicyStatisIfIndex_Object((1,3,6,1,4,1,5651,3,21,20,10,1,1),_PolicyStatisIfIndex_Type())
policyStatisIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisIfIndex.setStatus(_A)
class _PolicyStatisDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_PolicyStatisDirection_Type.__name__=_C
_PolicyStatisDirection_Object=MibTableColumn
policyStatisDirection=_PolicyStatisDirection_Object((1,3,6,1,4,1,5651,3,21,20,10,1,2),_PolicyStatisDirection_Type())
policyStatisDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisDirection.setStatus(_A)
class _PolicyStatisClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PolicyStatisClassName_Type.__name__=_F
_PolicyStatisClassName_Object=MibTableColumn
policyStatisClassName=_PolicyStatisClassName_Object((1,3,6,1,4,1,5651,3,21,20,10,1,3),_PolicyStatisClassName_Type())
policyStatisClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisClassName.setStatus(_A)
class _PolicyStatisSubClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PolicyStatisSubClassName_Type.__name__=_F
_PolicyStatisSubClassName_Object=MibTableColumn
policyStatisSubClassName=_PolicyStatisSubClassName_Object((1,3,6,1,4,1,5651,3,21,20,10,1,4),_PolicyStatisSubClassName_Type())
policyStatisSubClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisSubClassName.setStatus(_A)
class _PolicyStatisRemark_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PolicyStatisRemark_Type.__name__=_F
_PolicyStatisRemark_Object=MibTableColumn
policyStatisRemark=_PolicyStatisRemark_Object((1,3,6,1,4,1,5651,3,21,20,10,1,5),_PolicyStatisRemark_Type())
policyStatisRemark.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisRemark.setStatus(_A)
_PolicyStatisPackets_Type=Counter64
_PolicyStatisPackets_Object=MibTableColumn
policyStatisPackets=_PolicyStatisPackets_Object((1,3,6,1,4,1,5651,3,21,20,10,1,6),_PolicyStatisPackets_Type())
policyStatisPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisPackets.setStatus(_A)
_PolicyStatisBytes_Type=Counter64
_PolicyStatisBytes_Object=MibTableColumn
policyStatisBytes=_PolicyStatisBytes_Object((1,3,6,1,4,1,5651,3,21,20,10,1,7),_PolicyStatisBytes_Type())
policyStatisBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:policyStatisBytes.setStatus(_A)
_PolicyStatisRowStatus_Type=RowStatus
_PolicyStatisRowStatus_Object=MibTableColumn
policyStatisRowStatus=_PolicyStatisRowStatus_Object((1,3,6,1,4,1,5651,3,21,20,10,1,8),_PolicyStatisRowStatus_Type())
policyStatisRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:policyStatisRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mpQosMib':mpQosMib,'wfqListTable':wfqListTable,'wfqListEntry':wfqListEntry,_O:wfqIndex,'wfqListNum':wfqListNum,'wfqCtrlType':wfqCtrlType,'wfqQueueLimit':wfqQueueLimit,'wfqQueueNumber':wfqQueueNumber,'wfqWeightNumber':wfqWeightNumber,'wfqWeightType':wfqWeightType,'wfqSrcIp':wfqSrcIp,'wfqSrcPort':wfqSrcPort,'wfqDstIp':wfqDstIp,'wfqDstPort':wfqDstPort,'wfqStatus':wfqStatus,'pqListTable':pqListTable,'pqListEntry':pqListEntry,_P:pqIndex,'pqListNum':pqListNum,'pqCtrlType':pqCtrlType,'pqDefault':pqDefault,'pqIfIndex':pqIfIndex,'pqProtocol':pqProtocol,'pqPriority':pqPriority,'pqProtType':pqProtType,'pqProtValue':pqProtValue,'pqQueueHigh':pqQueueHigh,'pqQueueMedium':pqQueueMedium,'pqQueueNormal':pqQueueNormal,'pqQueueLow':pqQueueLow,'pqStatus':pqStatus,'classMap':classMap,'classMapTable':classMapTable,'classMapEntry':classMapEntry,_T:classMapClassName,'classMapMatchType':classMapMatchType,'classMapRowStatus':classMapRowStatus,'classMapAclTable':classMapAclTable,'classMapAclEntry':classMapAclEntry,_U:classMapAclClassName,_V:classMapAclListName,'classMapAclRowStatus':classMapAclRowStatus,'classMapInputIfTable':classMapInputIfTable,'classMapInputIfEntry':classMapInputIfEntry,_W:classMapInputIfClassName,_X:classMapInputIfName,'classMapInputIfRowStatus':classMapInputIfRowStatus,'classMapIpPrecedenceTable':classMapIpPrecedenceTable,'classMapIpPrecedenceEntry':classMapIpPrecedenceEntry,_Y:classMapIpPrecedenceClassName,_Z:classMapIpPrecedenceValue,'classMapIpPrecedenceRowStatus':classMapIpPrecedenceRowStatus,'classMapIpDscpTable':classMapIpDscpTable,'classMapIpDscpEntry':classMapIpDscpEntry,_a:classMapIpDscpClassName,_b:classMapIpDscpValue,'classMapIpDscpRowStatus':classMapIpDscpRowStatus,'classMapMplsExpTable':classMapMplsExpTable,'classMapMplsExpEntry':classMapMplsExpEntry,_c:classMapMplsExpClassName,_d:classMapMplsExpValue,'classMapMplsExpRowStatus':classMapMplsExpRowStatus,'classMapProtocolTable':classMapProtocolTable,'classMapProtocolEntry':classMapProtocolEntry,_e:classMapProtocolClassName,_f:classMapProtocolName,'classMapProtocolRowStatus':classMapProtocolRowStatus,'classMapNestTable':classMapNestTable,'classMapNestEntry':classMapNestEntry,_g:classMapNestClassName,_h:classMapNestName,'classMapNestRowStatus':classMapNestRowStatus,'policyMap':policyMap,'policyMapTable':policyMapTable,'policyMapEntry':policyMapEntry,_i:policyMapName,'policyMapRowStatus':policyMapRowStatus,'policyClassTable':policyClassTable,'policyClassEntry':policyClassEntry,_j:policyClassPolicyName,_k:policyClassClassName,'policyClassBandWidthKbps':policyClassBandWidthKbps,'policyClassBandWidthTotal':policyClassBandWidthTotal,'policyClassBandWidthPercent':policyClassBandWidthPercent,'policyClassPriorityBps':policyClassPriorityBps,'policyClassPriorityPercent':policyClassPriorityPercent,'policyClassWredEnable':policyClassWredEnable,'policyClassWredWeight':policyClassWredWeight,'policyClassWredMinThreshold0':policyClassWredMinThreshold0,'policyClassWredMaxThreshold0':policyClassWredMaxThreshold0,'policyClassWredMinThreshold1':policyClassWredMinThreshold1,'policyClassWredMaxThreshold1':policyClassWredMaxThreshold1,'policyClassWredMinThreshold2':policyClassWredMinThreshold2,'policyClassWredMaxThreshold2':policyClassWredMaxThreshold2,'policyClassWredMinThreshold3':policyClassWredMinThreshold3,'policyClassWredMaxThreshold3':policyClassWredMaxThreshold3,'policyClassWredMinThreshold4':policyClassWredMinThreshold4,'policyClassWredMaxThreshold4':policyClassWredMaxThreshold4,'policyClassWredMinThreshold5':policyClassWredMinThreshold5,'policyClassWredMaxThreshold5':policyClassWredMaxThreshold5,'policyClassWredMinThreshold6':policyClassWredMinThreshold6,'policyClassWredMaxThreshold6':policyClassWredMaxThreshold6,'policyClassWredMinThreshold7':policyClassWredMinThreshold7,'policyClassWredMaxThreshold7':policyClassWredMaxThreshold7,'policyClassSetIpPrecedence':policyClassSetIpPrecedence,'policyClassSetIpDscp':policyClassSetIpDscp,'policyClassSetMplsImp':policyClassSetMplsImp,'policyClassSetMplsTop':policyClassSetMplsTop,'policyClassNestName':policyClassNestName,'policyClassRowStatus':policyClassRowStatus,'priorityList':priorityList,'priorityListTable':priorityListTable,'priorityListEntry':priorityListEntry,_l:priorityListNo,'priorityListDefQType':priorityListDefQType,'priorityListQHigh':priorityListQHigh,'priorityListQMedium':priorityListQMedium,'priorityListQNormal':priorityListQNormal,'priorityListQLow':priorityListQLow,'priorityListWredGrpName':priorityListWredGrpName,'priorityListDropType':priorityListDropType,'priorityListStatus':priorityListStatus,'priorityListRuleTable':priorityListRuleTable,'priorityListRuleEntry':priorityListRuleEntry,_o:priorityListNoIndex,_p:priorityListRuleIndex,'priorityListRuleType':priorityListRuleType,'priorityListRulePriType':priorityListRulePriType,'priorityListforIntIfIndex':priorityListforIntIfIndex,'priorityListProtocolType':priorityListProtocolType,'priorityListClassFlag':priorityListClassFlag,'priorityListGtSize':priorityListGtSize,'priorityListLtSize':priorityListLtSize,'priorityListAccListNo':priorityListAccListNo,'priorityListTCPPort':priorityListTCPPort,'priorityListUDPPort':priorityListUDPPort,'priorityListRuleStatus':priorityListRuleStatus,'customList':customList,'customListTable':customListTable,'customListEntry':customListEntry,_q:customListNo,'customListDefNo':customListDefNo,'customListWredName':customListWredName,'customListDropType':customListDropType,'customListStatus':customListStatus,'customListRuleTable':customListRuleTable,'customListRuleEntry':customListRuleEntry,_r:customListNoIndex,_s:customListIndex,'customListICMP':customListICMP,'customListIGMP':customListIGMP,'customListQNo':customListQNo,'customListFragPktQNo':customListFragPktQNo,'customListPktEtSize':customListPktEtSize,'customListPktGtSize':customListPktGtSize,'customListPktLtSize':customListPktLtSize,'customListIpSrcAddr':customListIpSrcAddr,'customListIpSrcAddrMask':customListIpSrcAddrMask,'customListIpDestAddr':customListIpDestAddr,'customListIpDestAddrMask':customListIpDestAddrMask,'customListAccListNo':customListAccListNo,'customListQByteCount':customListQByteCount,'customListQLimit':customListQLimit,'customListTCPSrcAddr':customListTCPSrcAddr,'customListTCPSrcAddrMask':customListTCPSrcAddrMask,'customListTCPSrcPort':customListTCPSrcPort,'customListTCPDestAddr':customListTCPDestAddr,'customListTCPDestAddrMask':customListTCPDestAddrMask,'customListTCPDestPort':customListTCPDestPort,'customListUDPSrcAddr':customListUDPSrcAddr,'customListUDPSrcAddrMask':customListUDPSrcAddrMask,'customListUDPSrcPort':customListUDPSrcPort,'customListUDPDestAddr':customListUDPDestAddr,'customListUDPDestAddrMask':customListUDPDestAddrMask,'customListUDPDestPort':customListUDPDestPort,'customIntListIfIndex':customIntListIfIndex,'customListRuleStatus':customListRuleStatus,'wredGroup':wredGroup,'wredGrpTable':wredGrpTable,'wredGrpEntry':wredGrpEntry,_t:wredGrpName,'wredGrpExpWeight':wredGrpExpWeight,'wredGrpStatus':wredGrpStatus,'wredGrpPreTable':wredGrpPreTable,'wredGrpPreEntry':wredGrpPreEntry,_u:wredGrpPreName,_v:wredGrpPreNo,'wredGrpPreMinBytes':wredGrpPreMinBytes,'wredGrpPreMaxBytes':wredGrpPreMaxBytes,'wredGrpPreDenominator':wredGrpPreDenominator,'wredGrpPreRandomDropsBytes':wredGrpPreRandomDropsBytes,'wredGrpPreTailDropsBytes':wredGrpPreTailDropsBytes,'wredGrpPreStatus':wredGrpPreStatus,'ifWredTable':ifWredTable,'ifWredEntry':ifWredEntry,_w:ifWredIfIndex,'ifWredExpWeight':ifWredExpWeight,'ifWredStatus':ifWredStatus,'ifWredRuleTable':ifWredRuleTable,'ifWredRuleEntry':ifWredRuleEntry,_x:ifWredRuleIfIndex,_y:ifWredPreNo,'ifWredPreMinBytes':ifWredPreMinBytes,'ifWredPreMaxBytes':ifWredPreMaxBytes,'ifWredPreDenominator':ifWredPreDenominator,'ifWredRuleStatus':ifWredRuleStatus,'ifQos':ifQos,'ifQosTable':ifQosTable,'ifQosEntry':ifQosEntry,_z:ifQosIfIndex,'ifQosOutputPolicyName':ifQosOutputPolicyName,'ifQosInputPolicyName':ifQosInputPolicyName,'ifQosListType':ifQosListType,'ifQosListNo':ifQosListNo,'ifQosTrafficShapeRate':ifQosTrafficShapeRate,'ifQosTrafficShapeBurst':ifQosTrafficShapeBurst,'ifQosStatus':ifQosStatus,'ifQosIfTable':ifQosIfTable,'ifQosIfEntry':ifQosIfEntry,'ifQosIfQIfIndex':ifQosIfQIfIndex,'ifQosIfQType':ifQosIfQType,'ifQosIfQNum':ifQosIfQNum,'ifQosTotalBytes':ifQosTotalBytes,'ifQosCurTotalBytes':ifQosCurTotalBytes,'ifQosTotalInputPkts':ifQosTotalInputPkts,'ifQosTotalInputBytes':ifQosTotalInputBytes,'ifQosTotalOutputPkts':ifQosTotalOutputPkts,'ifQosTotalOutputBytes':ifQosTotalOutputBytes,'ifQosTotalDropPkts':ifQosTotalDropPkts,'ifQosTotalDropBytes':ifQosTotalDropBytes,'ifQosActiveQCnt':ifQosActiveQCnt,'ifQosCBWFQActQCnt':ifQosCBWFQActQCnt,'ifQosRSVPReq':ifQosRSVPReq,'ifQosQTable':ifQosQTable,'ifQosQEntry':ifQosQEntry,'ifQosQIfIndex':ifQosQIfIndex,'ifQosQId':ifQosQId,'ifQosQLimit':ifQosQLimit,'ifQosQSndPkts':ifQosQSndPkts,'ifQosQSndBytes':ifQosQSndBytes,'ifQosQDropPkts':ifQosQDropPkts,'ifQosQDropBytes':ifQosQDropBytes,'ifQosQCurBytes':ifQosQCurBytes,'ifQosQMaxSndBytes':ifQosQMaxSndBytes,'cbwfqConf':cbwfqConf,'cbwfqConfMaxClassNum':cbwfqConfMaxClassNum,'cbwfqConfMaxPolicyNum':cbwfqConfMaxPolicyNum,'qosCar':qosCar,'qosCarTable':qosCarTable,'qosCarEntry':qosCarEntry,_A1:qosCarIndex,_A2:qosCarIfIndex,'qosCarMaxBw':qosCarMaxBw,'qosCarNormalBw':qosCarNormalBw,'qosCarExceedBw':qosCarExceedBw,'qosCarConformAct':qosCarConformAct,'qosCarExceedAct':qosCarExceedAct,'qosCarConformActNo':qosCarConformActNo,'qosCarExceedActNo':qosCarExceedActNo,'qosCarStatus':qosCarStatus,'qosCarConformPkts':qosCarConformPkts,'qosCarConformBytes':qosCarConformBytes,'qosCarExceedPkts':qosCarExceedPkts,'qosCarExceedBytes':qosCarExceedBytes,'qosCarDirection':qosCarDirection,'qosCarAclGrp':qosCarAclGrp,'policyStatis':policyStatis,'policyStatisTable':policyStatisTable,'policyStatisEntry':policyStatisEntry,_A7:policyStatisIfIndex,_A8:policyStatisDirection,_A9:policyStatisClassName,_AA:policyStatisSubClassName,'policyStatisRemark':policyStatisRemark,'policyStatisPackets':policyStatisPackets,'policyStatisBytes':policyStatisBytes,'policyStatisRowStatus':policyStatisRowStatus})