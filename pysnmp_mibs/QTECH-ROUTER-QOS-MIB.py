_AG='qtechHQoSIfAppIndex'
_AF='qtechHQoSPortQIndex'
_AE='qtechHQoSVoQDeviceId'
_AD='qtechHQoSTPolicyMapIndex'
_AC='qtechHQoSTPolicyIndex'
_AB='qtechHQoSTBehaviorIndex'
_AA='qtechHQoSTClassifierInstance'
_A9='qtechHQoSTClassifierIndex'
_A8='qtechHQoSFlowMapIndex'
_A7='qtechHQoSFlowQIndex'
_A6='qtechHQoSUserGroupQIndex'
_A5='qtechHQoSUserQIndex'
_A4='qtechIfQosFlowLimitPktDirection'
_A3='qtechIfQosFlowLimitLabelNum'
_A2='qtechIfQosRTPIfApplyIfIndex'
_A1='qtechIfQosGTSACLNum'
_A0='qtechIfQosGTSType'
_z='qtechIfQosGTSIfIndex'
_y='qtechIfQosCARindex'
_x='qtechIfQosCARPktDirection'
_w='qtechIfQosCARIfIndex'
_v='qtechIfQosWredValue'
_u='qtechIfQosWredIfIndex'
_t='qtechIfQosWFQIfIndex'
_s='qtechIfQosCQRunInfoQueNum'
_r='qtechIfQosCQRunInfoIfIndex'
_q='qtechIfQosPQIfIndex'
_p='qtechCBQoSIfWredClassValue'
_o='qtechCBQoSIfWredClassIndex'
_n='qtechCBQoSIfWredIfIndex'
_m='qtechCBQoSIfQueueClassIndex'
_l='qtechCBQoSIfQueuePolicyDirection'
_k='qtechCBQoSIfQueueIfIndex'
_j='qtechCBQoSIfRemarkClassIndex'
_i='qtechCBQoSIfRemarkPolicyDirection'
_h='qtechCBQoSIfRemarkIfIndex'
_g='qtechCBQoSIfCarClassIndex'
_f='qtechCBQoSIfCarPolicyDirection'
_e='qtechCBQoSIfCarIfIndex'
_d='qtechCBQoSIfClassMatchClassIndex'
_c='qtechCBQoSIfClassMatchPolicyDirection'
_b='qtechCBQoSIfClassMatchIfIndex'
_a='qtechCBQoSIfCbwfqPolicyIfIndex'
_Z='QtechLayerType'
_Y='Bits'
_X='set-mpls-exp-transmit'
_W='set-mpls-exp-continue'
_V='transmit'
_U='set-prec-transmit'
_T='set-prec-continue'
_S='set-dscp-transmit'
_R='set-dscp-continue'
_Q='drop'
_P='continue'
_O='TruthValue'
_N='output'
_M='Unsigned32'
_L='input'
_K='QtechCosType'
_J='read-write'
_I='not-accessible'
_H='QtechQType'
_G='kilobits per second'
_F='OctetString'
_E='QTECH-ROUTER-QOS-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Y,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_O)
qtechRouterQoSMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,106))
if mibBuilder.loadTexts:qtechRouterQoSMIB.setRevisions(('2011-12-20 00:00',))
class QtechCosType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cos-be',1),('cos-af1',2),('cos-af2',3),('cos-af3',4),('cos-af4',5),('cos-ef',6),('cos-cs6',7),('cos-cs7',8)))
class QtechQType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('q-lpq',1),('q-wfq',2),('q-pq',3)))
class QtechQDirectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('d-input',1),('d-output',2)))
class QtechLayerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link-layer',1),('all-layer',2)))
_QtechCBQoSMIBObjects_ObjectIdentity=ObjectIdentity
qtechCBQoSMIBObjects=_QtechCBQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,1))
_QtechCBQoSIfStaticsObjects_ObjectIdentity=ObjectIdentity
qtechCBQoSIfStaticsObjects=_QtechCBQoSIfStaticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,1,1))
_QtechCBQoSIfCbwfqRunInfoTable_Object=MibTable
qtechCBQoSIfCbwfqRunInfoTable=_QtechCBQoSIfCbwfqRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1))
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqRunInfoTable.setStatus(_A)
_QtechCBQoSIfCbwfqRunInfoEntry_Object=MibTableRow
qtechCBQoSIfCbwfqRunInfoEntry=_QtechCBQoSIfCbwfqRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1))
qtechCBQoSIfCbwfqRunInfoEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqRunInfoEntry.setStatus(_A)
_QtechCBQoSIfCbwfqPolicyIfIndex_Type=Integer32
_QtechCBQoSIfCbwfqPolicyIfIndex_Object=MibTableColumn
qtechCBQoSIfCbwfqPolicyIfIndex=_QtechCBQoSIfCbwfqPolicyIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,1),_QtechCBQoSIfCbwfqPolicyIfIndex_Type())
qtechCBQoSIfCbwfqPolicyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqPolicyIfIndex.setStatus(_A)
_QtechCBQoSIfCbwfqQueueSize_Type=Integer32
_QtechCBQoSIfCbwfqQueueSize_Object=MibTableColumn
qtechCBQoSIfCbwfqQueueSize=_QtechCBQoSIfCbwfqQueueSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,2),_QtechCBQoSIfCbwfqQueueSize_Type())
qtechCBQoSIfCbwfqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqQueueSize.setStatus(_A)
_QtechCBQoSIfCbwfqDiscard_Type=Counter64
_QtechCBQoSIfCbwfqDiscard_Object=MibTableColumn
qtechCBQoSIfCbwfqDiscard=_QtechCBQoSIfCbwfqDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,3),_QtechCBQoSIfCbwfqDiscard_Type())
qtechCBQoSIfCbwfqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqDiscard.setStatus(_A)
_QtechCBQoSIfCbwfqEfQueueSize_Type=Integer32
_QtechCBQoSIfCbwfqEfQueueSize_Object=MibTableColumn
qtechCBQoSIfCbwfqEfQueueSize=_QtechCBQoSIfCbwfqEfQueueSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,4),_QtechCBQoSIfCbwfqEfQueueSize_Type())
qtechCBQoSIfCbwfqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqEfQueueSize.setStatus(_A)
_QtechCBQoSIfCbwfqAfQueueSize_Type=Integer32
_QtechCBQoSIfCbwfqAfQueueSize_Object=MibTableColumn
qtechCBQoSIfCbwfqAfQueueSize=_QtechCBQoSIfCbwfqAfQueueSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,5),_QtechCBQoSIfCbwfqAfQueueSize_Type())
qtechCBQoSIfCbwfqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqAfQueueSize.setStatus(_A)
_QtechCBQoSIfCbwfqBeQueueSize_Type=Integer32
_QtechCBQoSIfCbwfqBeQueueSize_Object=MibTableColumn
qtechCBQoSIfCbwfqBeQueueSize=_QtechCBQoSIfCbwfqBeQueueSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,6),_QtechCBQoSIfCbwfqBeQueueSize_Type())
qtechCBQoSIfCbwfqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqBeQueueSize.setStatus(_A)
_QtechCBQoSIfCbwfqBeActiveQueueNum_Type=Integer32
_QtechCBQoSIfCbwfqBeActiveQueueNum_Object=MibTableColumn
qtechCBQoSIfCbwfqBeActiveQueueNum=_QtechCBQoSIfCbwfqBeActiveQueueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,7),_QtechCBQoSIfCbwfqBeActiveQueueNum_Type())
qtechCBQoSIfCbwfqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqBeActiveQueueNum.setStatus(_A)
_QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Type=Integer32
_QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Object=MibTableColumn
qtechCBQoSIfCbwfqBeMaxActiveQueueNum=_QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,8),_QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Type())
qtechCBQoSIfCbwfqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqBeMaxActiveQueueNum.setStatus(_A)
_QtechCBQoSIfCbwfqBeTotalQueueNum_Type=Integer32
_QtechCBQoSIfCbwfqBeTotalQueueNum_Object=MibTableColumn
qtechCBQoSIfCbwfqBeTotalQueueNum=_QtechCBQoSIfCbwfqBeTotalQueueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,9),_QtechCBQoSIfCbwfqBeTotalQueueNum_Type())
qtechCBQoSIfCbwfqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqBeTotalQueueNum.setStatus(_A)
_QtechCBQoSIfCbwfqAfAllocatedQueueNum_Type=Integer32
_QtechCBQoSIfCbwfqAfAllocatedQueueNum_Object=MibTableColumn
qtechCBQoSIfCbwfqAfAllocatedQueueNum=_QtechCBQoSIfCbwfqAfAllocatedQueueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,1,1,10),_QtechCBQoSIfCbwfqAfAllocatedQueueNum_Type())
qtechCBQoSIfCbwfqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCbwfqAfAllocatedQueueNum.setStatus(_A)
_QtechCBQoSIfClassMatchRunInfoTable_Object=MibTable
qtechCBQoSIfClassMatchRunInfoTable=_QtechCBQoSIfClassMatchRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2))
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchRunInfoTable.setStatus(_A)
_QtechCBQoSIfClassMatchRunInfoEntry_Object=MibTableRow
qtechCBQoSIfClassMatchRunInfoEntry=_QtechCBQoSIfClassMatchRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1))
qtechCBQoSIfClassMatchRunInfoEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchRunInfoEntry.setStatus(_A)
_QtechCBQoSIfClassMatchIfIndex_Type=Integer32
_QtechCBQoSIfClassMatchIfIndex_Object=MibTableColumn
qtechCBQoSIfClassMatchIfIndex=_QtechCBQoSIfClassMatchIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,1),_QtechCBQoSIfClassMatchIfIndex_Type())
qtechCBQoSIfClassMatchIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchIfIndex.setStatus(_A)
class _QtechCBQoSIfClassMatchPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_QtechCBQoSIfClassMatchPolicyDirection_Type.__name__=_D
_QtechCBQoSIfClassMatchPolicyDirection_Object=MibTableColumn
qtechCBQoSIfClassMatchPolicyDirection=_QtechCBQoSIfClassMatchPolicyDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,2),_QtechCBQoSIfClassMatchPolicyDirection_Type())
qtechCBQoSIfClassMatchPolicyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchPolicyDirection.setStatus(_A)
_QtechCBQoSIfClassMatchClassIndex_Type=Integer32
_QtechCBQoSIfClassMatchClassIndex_Object=MibTableColumn
qtechCBQoSIfClassMatchClassIndex=_QtechCBQoSIfClassMatchClassIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,3),_QtechCBQoSIfClassMatchClassIndex_Type())
qtechCBQoSIfClassMatchClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchClassIndex.setStatus(_A)
_QtechCBQoSIfClassMatchedPackets_Type=Counter64
_QtechCBQoSIfClassMatchedPackets_Object=MibTableColumn
qtechCBQoSIfClassMatchedPackets=_QtechCBQoSIfClassMatchedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,4),_QtechCBQoSIfClassMatchedPackets_Type())
qtechCBQoSIfClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchedPackets.setStatus(_A)
_QtechCBQoSIfClassMatchedBytes_Type=Counter64
_QtechCBQoSIfClassMatchedBytes_Object=MibTableColumn
qtechCBQoSIfClassMatchedBytes=_QtechCBQoSIfClassMatchedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,5),_QtechCBQoSIfClassMatchedBytes_Type())
qtechCBQoSIfClassMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfClassMatchedBytes.setStatus(_A)
_QtechCBQosIfClassPassedPackets_Type=Counter64
_QtechCBQosIfClassPassedPackets_Object=MibTableColumn
qtechCBQosIfClassPassedPackets=_QtechCBQosIfClassPassedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,6),_QtechCBQosIfClassPassedPackets_Type())
qtechCBQosIfClassPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQosIfClassPassedPackets.setStatus(_A)
_QtechCBQosIfClassDroppedPackets_Type=Counter64
_QtechCBQosIfClassDroppedPackets_Object=MibTableColumn
qtechCBQosIfClassDroppedPackets=_QtechCBQosIfClassDroppedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,2,1,7),_QtechCBQosIfClassDroppedPackets_Type())
qtechCBQosIfClassDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQosIfClassDroppedPackets.setStatus(_A)
_QtechCBQoSIfCarRunInfoTable_Object=MibTable
qtechCBQoSIfCarRunInfoTable=_QtechCBQoSIfCarRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3))
if mibBuilder.loadTexts:qtechCBQoSIfCarRunInfoTable.setStatus(_A)
_QtechCBQoSIfCarRunInfoEntry_Object=MibTableRow
qtechCBQoSIfCarRunInfoEntry=_QtechCBQoSIfCarRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1))
qtechCBQoSIfCarRunInfoEntry.setIndexNames((0,_E,_e),(0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:qtechCBQoSIfCarRunInfoEntry.setStatus(_A)
_QtechCBQoSIfCarIfIndex_Type=Integer32
_QtechCBQoSIfCarIfIndex_Object=MibTableColumn
qtechCBQoSIfCarIfIndex=_QtechCBQoSIfCarIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,1),_QtechCBQoSIfCarIfIndex_Type())
qtechCBQoSIfCarIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarIfIndex.setStatus(_A)
class _QtechCBQoSIfCarPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_QtechCBQoSIfCarPolicyDirection_Type.__name__=_D
_QtechCBQoSIfCarPolicyDirection_Object=MibTableColumn
qtechCBQoSIfCarPolicyDirection=_QtechCBQoSIfCarPolicyDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,2),_QtechCBQoSIfCarPolicyDirection_Type())
qtechCBQoSIfCarPolicyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarPolicyDirection.setStatus(_A)
_QtechCBQoSIfCarClassIndex_Type=Integer32
_QtechCBQoSIfCarClassIndex_Object=MibTableColumn
qtechCBQoSIfCarClassIndex=_QtechCBQoSIfCarClassIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,3),_QtechCBQoSIfCarClassIndex_Type())
qtechCBQoSIfCarClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarClassIndex.setStatus(_A)
_QtechCBQoSIfCarConformedPackets_Type=Counter64
_QtechCBQoSIfCarConformedPackets_Object=MibTableColumn
qtechCBQoSIfCarConformedPackets=_QtechCBQoSIfCarConformedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,4),_QtechCBQoSIfCarConformedPackets_Type())
qtechCBQoSIfCarConformedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarConformedPackets.setStatus(_A)
_QtechCBQoSIfCarConformedBytes_Type=Counter64
_QtechCBQoSIfCarConformedBytes_Object=MibTableColumn
qtechCBQoSIfCarConformedBytes=_QtechCBQoSIfCarConformedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,5),_QtechCBQoSIfCarConformedBytes_Type())
qtechCBQoSIfCarConformedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarConformedBytes.setStatus(_A)
_QtechCBQoSIfCarExceededPackets_Type=Counter64
_QtechCBQoSIfCarExceededPackets_Object=MibTableColumn
qtechCBQoSIfCarExceededPackets=_QtechCBQoSIfCarExceededPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,6),_QtechCBQoSIfCarExceededPackets_Type())
qtechCBQoSIfCarExceededPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarExceededPackets.setStatus(_A)
_QtechCBQoSIfCarExceededBytes_Type=Counter64
_QtechCBQoSIfCarExceededBytes_Object=MibTableColumn
qtechCBQoSIfCarExceededBytes=_QtechCBQoSIfCarExceededBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,7),_QtechCBQoSIfCarExceededBytes_Type())
qtechCBQoSIfCarExceededBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarExceededBytes.setStatus(_A)
_QtechCBQoSIfCarViolatedPackets_Type=Counter64
_QtechCBQoSIfCarViolatedPackets_Object=MibTableColumn
qtechCBQoSIfCarViolatedPackets=_QtechCBQoSIfCarViolatedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,8),_QtechCBQoSIfCarViolatedPackets_Type())
qtechCBQoSIfCarViolatedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarViolatedPackets.setStatus(_A)
_QtechCBQoSIfCarViolatedBytes_Type=Counter64
_QtechCBQoSIfCarViolatedBytes_Object=MibTableColumn
qtechCBQoSIfCarViolatedBytes=_QtechCBQoSIfCarViolatedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,3,1,9),_QtechCBQoSIfCarViolatedBytes_Type())
qtechCBQoSIfCarViolatedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfCarViolatedBytes.setStatus(_A)
_QtechCBQoSIfRemarkRunInfoTable_Object=MibTable
qtechCBQoSIfRemarkRunInfoTable=_QtechCBQoSIfRemarkRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4))
if mibBuilder.loadTexts:qtechCBQoSIfRemarkRunInfoTable.setStatus(_A)
_QtechCBQoSIfRemarkRunInfoEntry_Object=MibTableRow
qtechCBQoSIfRemarkRunInfoEntry=_QtechCBQoSIfRemarkRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4,1))
qtechCBQoSIfRemarkRunInfoEntry.setIndexNames((0,_E,_h),(0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:qtechCBQoSIfRemarkRunInfoEntry.setStatus(_A)
_QtechCBQoSIfRemarkIfIndex_Type=Integer32
_QtechCBQoSIfRemarkIfIndex_Object=MibTableColumn
qtechCBQoSIfRemarkIfIndex=_QtechCBQoSIfRemarkIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4,1,1),_QtechCBQoSIfRemarkIfIndex_Type())
qtechCBQoSIfRemarkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfRemarkIfIndex.setStatus(_A)
class _QtechCBQoSIfRemarkPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_QtechCBQoSIfRemarkPolicyDirection_Type.__name__=_D
_QtechCBQoSIfRemarkPolicyDirection_Object=MibTableColumn
qtechCBQoSIfRemarkPolicyDirection=_QtechCBQoSIfRemarkPolicyDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4,1,2),_QtechCBQoSIfRemarkPolicyDirection_Type())
qtechCBQoSIfRemarkPolicyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfRemarkPolicyDirection.setStatus(_A)
_QtechCBQoSIfRemarkClassIndex_Type=Integer32
_QtechCBQoSIfRemarkClassIndex_Object=MibTableColumn
qtechCBQoSIfRemarkClassIndex=_QtechCBQoSIfRemarkClassIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4,1,3),_QtechCBQoSIfRemarkClassIndex_Type())
qtechCBQoSIfRemarkClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfRemarkClassIndex.setStatus(_A)
_QtechCBQoSIfRemarkedPackets_Type=Counter64
_QtechCBQoSIfRemarkedPackets_Object=MibTableColumn
qtechCBQoSIfRemarkedPackets=_QtechCBQoSIfRemarkedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4,1,4),_QtechCBQoSIfRemarkedPackets_Type())
qtechCBQoSIfRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfRemarkedPackets.setStatus(_A)
_QtechCBQoSIfRemarkedBytes_Type=Counter64
_QtechCBQoSIfRemarkedBytes_Object=MibTableColumn
qtechCBQoSIfRemarkedBytes=_QtechCBQoSIfRemarkedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,4,1,5),_QtechCBQoSIfRemarkedBytes_Type())
qtechCBQoSIfRemarkedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfRemarkedBytes.setStatus(_A)
_QtechCBQoSIfQueueRunInfoTable_Object=MibTable
qtechCBQoSIfQueueRunInfoTable=_QtechCBQoSIfQueueRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5))
if mibBuilder.loadTexts:qtechCBQoSIfQueueRunInfoTable.setStatus(_A)
_QtechCBQoSIfQueueRunInfoEntry_Object=MibTableRow
qtechCBQoSIfQueueRunInfoEntry=_QtechCBQoSIfQueueRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1))
qtechCBQoSIfQueueRunInfoEntry.setIndexNames((0,_E,_k),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:qtechCBQoSIfQueueRunInfoEntry.setStatus(_A)
_QtechCBQoSIfQueueIfIndex_Type=Integer32
_QtechCBQoSIfQueueIfIndex_Object=MibTableColumn
qtechCBQoSIfQueueIfIndex=_QtechCBQoSIfQueueIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,1),_QtechCBQoSIfQueueIfIndex_Type())
qtechCBQoSIfQueueIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueIfIndex.setStatus(_A)
class _QtechCBQoSIfQueuePolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_QtechCBQoSIfQueuePolicyDirection_Type.__name__=_D
_QtechCBQoSIfQueuePolicyDirection_Object=MibTableColumn
qtechCBQoSIfQueuePolicyDirection=_QtechCBQoSIfQueuePolicyDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,2),_QtechCBQoSIfQueuePolicyDirection_Type())
qtechCBQoSIfQueuePolicyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueuePolicyDirection.setStatus(_A)
_QtechCBQoSIfQueueClassIndex_Type=Integer32
_QtechCBQoSIfQueueClassIndex_Object=MibTableColumn
qtechCBQoSIfQueueClassIndex=_QtechCBQoSIfQueueClassIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,3),_QtechCBQoSIfQueueClassIndex_Type())
qtechCBQoSIfQueueClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueClassIndex.setStatus(_A)
_QtechCBQoSIfQueueMatchedPackets_Type=Counter64
_QtechCBQoSIfQueueMatchedPackets_Object=MibTableColumn
qtechCBQoSIfQueueMatchedPackets=_QtechCBQoSIfQueueMatchedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,4),_QtechCBQoSIfQueueMatchedPackets_Type())
qtechCBQoSIfQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueMatchedPackets.setStatus(_A)
_QtechCBQoSIfQueueMatchedBytes_Type=Counter64
_QtechCBQoSIfQueueMatchedBytes_Object=MibTableColumn
qtechCBQoSIfQueueMatchedBytes=_QtechCBQoSIfQueueMatchedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,5),_QtechCBQoSIfQueueMatchedBytes_Type())
qtechCBQoSIfQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueMatchedBytes.setStatus(_A)
_QtechCBQoSIfQueueEnqueuedPackets_Type=Counter64
_QtechCBQoSIfQueueEnqueuedPackets_Object=MibTableColumn
qtechCBQoSIfQueueEnqueuedPackets=_QtechCBQoSIfQueueEnqueuedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,6),_QtechCBQoSIfQueueEnqueuedPackets_Type())
qtechCBQoSIfQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueEnqueuedPackets.setStatus(_A)
_QtechCBQoSIfQueueEnqueuedBytes_Type=Counter64
_QtechCBQoSIfQueueEnqueuedBytes_Object=MibTableColumn
qtechCBQoSIfQueueEnqueuedBytes=_QtechCBQoSIfQueueEnqueuedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,7),_QtechCBQoSIfQueueEnqueuedBytes_Type())
qtechCBQoSIfQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueEnqueuedBytes.setStatus(_A)
_QtechCBQoSIfQueueDiscardedPackets_Type=Counter64
_QtechCBQoSIfQueueDiscardedPackets_Object=MibTableColumn
qtechCBQoSIfQueueDiscardedPackets=_QtechCBQoSIfQueueDiscardedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,8),_QtechCBQoSIfQueueDiscardedPackets_Type())
qtechCBQoSIfQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueDiscardedPackets.setStatus(_A)
_QtechCBQoSIfQueueDiscardedBytes_Type=Counter64
_QtechCBQoSIfQueueDiscardedBytes_Object=MibTableColumn
qtechCBQoSIfQueueDiscardedBytes=_QtechCBQoSIfQueueDiscardedBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,5,1,9),_QtechCBQoSIfQueueDiscardedBytes_Type())
qtechCBQoSIfQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfQueueDiscardedBytes.setStatus(_A)
_QtechCBQoSIfWredRunInfoTable_Object=MibTable
qtechCBQoSIfWredRunInfoTable=_QtechCBQoSIfWredRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6))
if mibBuilder.loadTexts:qtechCBQoSIfWredRunInfoTable.setStatus(_A)
_QtechCBQoSIfWredRunInfoEntry_Object=MibTableRow
qtechCBQoSIfWredRunInfoEntry=_QtechCBQoSIfWredRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6,1))
qtechCBQoSIfWredRunInfoEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:qtechCBQoSIfWredRunInfoEntry.setStatus(_A)
_QtechCBQoSIfWredIfIndex_Type=Integer32
_QtechCBQoSIfWredIfIndex_Object=MibTableColumn
qtechCBQoSIfWredIfIndex=_QtechCBQoSIfWredIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6,1,1),_QtechCBQoSIfWredIfIndex_Type())
qtechCBQoSIfWredIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfWredIfIndex.setStatus(_A)
_QtechCBQoSIfWredClassIndex_Type=Integer32
_QtechCBQoSIfWredClassIndex_Object=MibTableColumn
qtechCBQoSIfWredClassIndex=_QtechCBQoSIfWredClassIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6,1,2),_QtechCBQoSIfWredClassIndex_Type())
qtechCBQoSIfWredClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfWredClassIndex.setStatus(_A)
_QtechCBQoSIfWredClassValue_Type=Integer32
_QtechCBQoSIfWredClassValue_Object=MibTableColumn
qtechCBQoSIfWredClassValue=_QtechCBQoSIfWredClassValue_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6,1,3),_QtechCBQoSIfWredClassValue_Type())
qtechCBQoSIfWredClassValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfWredClassValue.setStatus(_A)
_QtechCBQoSIfWredRandomDiscardedPackets_Type=Counter64
_QtechCBQoSIfWredRandomDiscardedPackets_Object=MibTableColumn
qtechCBQoSIfWredRandomDiscardedPackets=_QtechCBQoSIfWredRandomDiscardedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6,1,4),_QtechCBQoSIfWredRandomDiscardedPackets_Type())
qtechCBQoSIfWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfWredRandomDiscardedPackets.setStatus(_A)
_QtechCBQoSIfWredTailDiscardedPackets_Type=Counter64
_QtechCBQoSIfWredTailDiscardedPackets_Object=MibTableColumn
qtechCBQoSIfWredTailDiscardedPackets=_QtechCBQoSIfWredTailDiscardedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,1,1,6,1,5),_QtechCBQoSIfWredTailDiscardedPackets_Type())
qtechCBQoSIfWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCBQoSIfWredTailDiscardedPackets.setStatus(_A)
_QtechIfQoSMIBObjects_ObjectIdentity=ObjectIdentity
qtechIfQoSMIBObjects=_QtechIfQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,2))
_QtechIfQosPQRunInfoTable_Object=MibTable
qtechIfQosPQRunInfoTable=_QtechIfQosPQRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1))
if mibBuilder.loadTexts:qtechIfQosPQRunInfoTable.setStatus(_A)
_QtechIfQosPQRunInfoEntry_Object=MibTableRow
qtechIfQosPQRunInfoEntry=_QtechIfQosPQRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1))
qtechIfQosPQRunInfoEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:qtechIfQosPQRunInfoEntry.setStatus(_A)
_QtechIfQosPQIfIndex_Type=Integer32
_QtechIfQosPQIfIndex_Object=MibTableColumn
qtechIfQosPQIfIndex=_QtechIfQosPQIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,1),_QtechIfQosPQIfIndex_Type())
qtechIfQosPQIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQIfIndex.setStatus(_A)
class _QtechIfQosPQListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QtechIfQosPQListNum_Type.__name__=_D
_QtechIfQosPQListNum_Object=MibTableColumn
qtechIfQosPQListNum=_QtechIfQosPQListNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,2),_QtechIfQosPQListNum_Type())
qtechIfQosPQListNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQListNum.setStatus(_A)
_QtechIfQosPQIfName_Type=OctetString
_QtechIfQosPQIfName_Object=MibTableColumn
qtechIfQosPQIfName=_QtechIfQosPQIfName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,3),_QtechIfQosPQIfName_Type())
qtechIfQosPQIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQIfName.setStatus(_A)
class _QtechIfQosPQHighPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosPQHighPkt_Type.__name__=_D
_QtechIfQosPQHighPkt_Object=MibTableColumn
qtechIfQosPQHighPkt=_QtechIfQosPQHighPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,4),_QtechIfQosPQHighPkt_Type())
qtechIfQosPQHighPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQHighPkt.setStatus(_A)
_QtechIfQosPQHighDiscard_Type=Counter32
_QtechIfQosPQHighDiscard_Object=MibTableColumn
qtechIfQosPQHighDiscard=_QtechIfQosPQHighDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,5),_QtechIfQosPQHighDiscard_Type())
qtechIfQosPQHighDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQHighDiscard.setStatus(_A)
class _QtechIfQosPQHighMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosPQHighMaxQueLen_Type.__name__=_D
_QtechIfQosPQHighMaxQueLen_Object=MibTableColumn
qtechIfQosPQHighMaxQueLen=_QtechIfQosPQHighMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,6),_QtechIfQosPQHighMaxQueLen_Type())
qtechIfQosPQHighMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQHighMaxQueLen.setStatus(_A)
class _QtechIfQosPQMiddlePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosPQMiddlePkt_Type.__name__=_D
_QtechIfQosPQMiddlePkt_Object=MibTableColumn
qtechIfQosPQMiddlePkt=_QtechIfQosPQMiddlePkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,7),_QtechIfQosPQMiddlePkt_Type())
qtechIfQosPQMiddlePkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQMiddlePkt.setStatus(_A)
_QtechIfQosPQMiddleDiscard_Type=Counter32
_QtechIfQosPQMiddleDiscard_Object=MibTableColumn
qtechIfQosPQMiddleDiscard=_QtechIfQosPQMiddleDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,8),_QtechIfQosPQMiddleDiscard_Type())
qtechIfQosPQMiddleDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQMiddleDiscard.setStatus(_A)
class _QtechIfQosPQMiddleMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosPQMiddleMaxQueLen_Type.__name__=_D
_QtechIfQosPQMiddleMaxQueLen_Object=MibTableColumn
qtechIfQosPQMiddleMaxQueLen=_QtechIfQosPQMiddleMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,9),_QtechIfQosPQMiddleMaxQueLen_Type())
qtechIfQosPQMiddleMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQMiddleMaxQueLen.setStatus(_A)
class _QtechIfQosPQNormalPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosPQNormalPkt_Type.__name__=_D
_QtechIfQosPQNormalPkt_Object=MibTableColumn
qtechIfQosPQNormalPkt=_QtechIfQosPQNormalPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,10),_QtechIfQosPQNormalPkt_Type())
qtechIfQosPQNormalPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQNormalPkt.setStatus(_A)
_QtechIfQosPQNormalDiscard_Type=Counter32
_QtechIfQosPQNormalDiscard_Object=MibTableColumn
qtechIfQosPQNormalDiscard=_QtechIfQosPQNormalDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,11),_QtechIfQosPQNormalDiscard_Type())
qtechIfQosPQNormalDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQNormalDiscard.setStatus(_A)
class _QtechIfQosPQNormalMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosPQNormalMaxQueLen_Type.__name__=_D
_QtechIfQosPQNormalMaxQueLen_Object=MibTableColumn
qtechIfQosPQNormalMaxQueLen=_QtechIfQosPQNormalMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,12),_QtechIfQosPQNormalMaxQueLen_Type())
qtechIfQosPQNormalMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQNormalMaxQueLen.setStatus(_A)
class _QtechIfQosPQLowPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosPQLowPkt_Type.__name__=_D
_QtechIfQosPQLowPkt_Object=MibTableColumn
qtechIfQosPQLowPkt=_QtechIfQosPQLowPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,13),_QtechIfQosPQLowPkt_Type())
qtechIfQosPQLowPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQLowPkt.setStatus(_A)
_QtechIfQosPQLowDiscard_Type=Counter32
_QtechIfQosPQLowDiscard_Object=MibTableColumn
qtechIfQosPQLowDiscard=_QtechIfQosPQLowDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,14),_QtechIfQosPQLowDiscard_Type())
qtechIfQosPQLowDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQLowDiscard.setStatus(_A)
class _QtechIfQosPQLowMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosPQLowMaxQueLen_Type.__name__=_D
_QtechIfQosPQLowMaxQueLen_Object=MibTableColumn
qtechIfQosPQLowMaxQueLen=_QtechIfQosPQLowMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,1,1,15),_QtechIfQosPQLowMaxQueLen_Type())
qtechIfQosPQLowMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosPQLowMaxQueLen.setStatus(_A)
_QtechIfQosCQRunInfoTable_Object=MibTable
qtechIfQosCQRunInfoTable=_QtechIfQosCQRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2))
if mibBuilder.loadTexts:qtechIfQosCQRunInfoTable.setStatus(_A)
_QtechIfQosCQRunInfoEntry_Object=MibTableRow
qtechIfQosCQRunInfoEntry=_QtechIfQosCQRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1))
qtechIfQosCQRunInfoEntry.setIndexNames((0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:qtechIfQosCQRunInfoEntry.setStatus(_A)
_QtechIfQosCQRunInfoIfIndex_Type=Integer32
_QtechIfQosCQRunInfoIfIndex_Object=MibTableColumn
qtechIfQosCQRunInfoIfIndex=_QtechIfQosCQRunInfoIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1,1),_QtechIfQosCQRunInfoIfIndex_Type())
qtechIfQosCQRunInfoIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCQRunInfoIfIndex.setStatus(_A)
class _QtechIfQosCQRunInfoQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QtechIfQosCQRunInfoQueNum_Type.__name__=_D
_QtechIfQosCQRunInfoQueNum_Object=MibTableColumn
qtechIfQosCQRunInfoQueNum=_QtechIfQosCQRunInfoQueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1,2),_QtechIfQosCQRunInfoQueNum_Type())
qtechIfQosCQRunInfoQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCQRunInfoQueNum.setStatus(_A)
_QtechIfQosCQRunInfoIfName_Type=OctetString
_QtechIfQosCQRunInfoIfName_Object=MibTableColumn
qtechIfQosCQRunInfoIfName=_QtechIfQosCQRunInfoIfName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1,3),_QtechIfQosCQRunInfoIfName_Type())
qtechIfQosCQRunInfoIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCQRunInfoIfName.setStatus(_A)
class _QtechIfQosCQRunInfoQuePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosCQRunInfoQuePkt_Type.__name__=_D
_QtechIfQosCQRunInfoQuePkt_Object=MibTableColumn
qtechIfQosCQRunInfoQuePkt=_QtechIfQosCQRunInfoQuePkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1,4),_QtechIfQosCQRunInfoQuePkt_Type())
qtechIfQosCQRunInfoQuePkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCQRunInfoQuePkt.setStatus(_A)
_QtechIfQosCQRunInfoQueDiscard_Type=Counter32
_QtechIfQosCQRunInfoQueDiscard_Object=MibTableColumn
qtechIfQosCQRunInfoQueDiscard=_QtechIfQosCQRunInfoQueDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1,5),_QtechIfQosCQRunInfoQueDiscard_Type())
qtechIfQosCQRunInfoQueDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCQRunInfoQueDiscard.setStatus(_A)
class _QtechIfQosCQRunInfoMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosCQRunInfoMaxQueLen_Type.__name__=_D
_QtechIfQosCQRunInfoMaxQueLen_Object=MibTableColumn
qtechIfQosCQRunInfoMaxQueLen=_QtechIfQosCQRunInfoMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,2,1,6),_QtechIfQosCQRunInfoMaxQueLen_Type())
qtechIfQosCQRunInfoMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCQRunInfoMaxQueLen.setStatus(_A)
_QtechIfQosWFQRunInfoTable_Object=MibTable
qtechIfQosWFQRunInfoTable=_QtechIfQosWFQRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3))
if mibBuilder.loadTexts:qtechIfQosWFQRunInfoTable.setStatus(_A)
_QtechIfQosWFQRunInfoEntry_Object=MibTableRow
qtechIfQosWFQRunInfoEntry=_QtechIfQosWFQRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1))
qtechIfQosWFQRunInfoEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:qtechIfQosWFQRunInfoEntry.setStatus(_A)
_QtechIfQosWFQIfIndex_Type=Integer32
_QtechIfQosWFQIfIndex_Object=MibTableColumn
qtechIfQosWFQIfIndex=_QtechIfQosWFQIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,1),_QtechIfQosWFQIfIndex_Type())
qtechIfQosWFQIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQIfIndex.setStatus(_A)
_QtechIfQosWFQIfName_Type=OctetString
_QtechIfQosWFQIfName_Object=MibTableColumn
qtechIfQosWFQIfName=_QtechIfQosWFQIfName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,2),_QtechIfQosWFQIfName_Type())
qtechIfQosWFQIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQIfName.setStatus(_A)
class _QtechIfQosWFQMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosWFQMaxQueLen_Type.__name__=_D
_QtechIfQosWFQMaxQueLen_Object=MibTableColumn
qtechIfQosWFQMaxQueLen=_QtechIfQosWFQMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,3),_QtechIfQosWFQMaxQueLen_Type())
qtechIfQosWFQMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQMaxQueLen.setStatus(_A)
class _QtechIfQosWFQTotalQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*(('a16',16),('a32',32),('a64',64),('a128',128),('a256',256),('a512',512),('a1024',1024),('a2048',2048),('a4096',4096)))
_QtechIfQosWFQTotalQueNum_Type.__name__=_D
_QtechIfQosWFQTotalQueNum_Object=MibTableColumn
qtechIfQosWFQTotalQueNum=_QtechIfQosWFQTotalQueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,4),_QtechIfQosWFQTotalQueNum_Type())
qtechIfQosWFQTotalQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQTotalQueNum.setStatus(_A)
_QtechIfQosWFQCurQueLen_Type=Integer32
_QtechIfQosWFQCurQueLen_Object=MibTableColumn
qtechIfQosWFQCurQueLen=_QtechIfQosWFQCurQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,5),_QtechIfQosWFQCurQueLen_Type())
qtechIfQosWFQCurQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQCurQueLen.setStatus(_A)
_QtechIfQosWFQTotalDiscard_Type=Counter32
_QtechIfQosWFQTotalDiscard_Object=MibTableColumn
qtechIfQosWFQTotalDiscard=_QtechIfQosWFQTotalDiscard_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,6),_QtechIfQosWFQTotalDiscard_Type())
qtechIfQosWFQTotalDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQTotalDiscard.setStatus(_A)
class _QtechIfQosWFQActiveQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosWFQActiveQueNum_Type.__name__=_D
_QtechIfQosWFQActiveQueNum_Object=MibTableColumn
qtechIfQosWFQActiveQueNum=_QtechIfQosWFQActiveQueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,7),_QtechIfQosWFQActiveQueNum_Type())
qtechIfQosWFQActiveQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQActiveQueNum.setStatus(_A)
class _QtechIfQosWFQMaxActiveQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechIfQosWFQMaxActiveQueNum_Type.__name__=_D
_QtechIfQosWFQMaxActiveQueNum_Object=MibTableColumn
qtechIfQosWFQMaxActiveQueNum=_QtechIfQosWFQMaxActiveQueNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,3,1,8),_QtechIfQosWFQMaxActiveQueNum_Type())
qtechIfQosWFQMaxActiveQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWFQMaxActiveQueNum.setStatus(_A)
_QtechIfQosWredRunInfoTable_Object=MibTable
qtechIfQosWredRunInfoTable=_QtechIfQosWredRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,4))
if mibBuilder.loadTexts:qtechIfQosWredRunInfoTable.setStatus(_A)
_QtechIfQosWredRunInfoEntry_Object=MibTableRow
qtechIfQosWredRunInfoEntry=_QtechIfQosWredRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,4,1))
qtechIfQosWredRunInfoEntry.setIndexNames((0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:qtechIfQosWredRunInfoEntry.setStatus(_A)
_QtechIfQosWredIfIndex_Type=Integer32
_QtechIfQosWredIfIndex_Object=MibTableColumn
qtechIfQosWredIfIndex=_QtechIfQosWredIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,4,1,1),_QtechIfQosWredIfIndex_Type())
qtechIfQosWredIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWredIfIndex.setStatus(_A)
_QtechIfQosWredValue_Type=Integer32
_QtechIfQosWredValue_Object=MibTableColumn
qtechIfQosWredValue=_QtechIfQosWredValue_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,4,1,2),_QtechIfQosWredValue_Type())
qtechIfQosWredValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWredValue.setStatus(_A)
_QtechIfQosWredRandomDiscardedPackets_Type=Counter64
_QtechIfQosWredRandomDiscardedPackets_Object=MibTableColumn
qtechIfQosWredRandomDiscardedPackets=_QtechIfQosWredRandomDiscardedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,4,1,3),_QtechIfQosWredRandomDiscardedPackets_Type())
qtechIfQosWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWredRandomDiscardedPackets.setStatus(_A)
_QtechIfQosWredTailDiscardedPackets_Type=Counter64
_QtechIfQosWredTailDiscardedPackets_Object=MibTableColumn
qtechIfQosWredTailDiscardedPackets=_QtechIfQosWredTailDiscardedPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,4,1,4),_QtechIfQosWredTailDiscardedPackets_Type())
qtechIfQosWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosWredTailDiscardedPackets.setStatus(_A)
_QtechIfQosCARTable_Object=MibTable
qtechIfQosCARTable=_QtechIfQosCARTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5))
if mibBuilder.loadTexts:qtechIfQosCARTable.setStatus(_A)
_QtechIfQosCAREntry_Object=MibTableRow
qtechIfQosCAREntry=_QtechIfQosCAREntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1))
qtechIfQosCAREntry.setIndexNames((0,_E,_w),(0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:qtechIfQosCAREntry.setStatus(_A)
_QtechIfQosCARIfIndex_Type=Integer32
_QtechIfQosCARIfIndex_Object=MibTableColumn
qtechIfQosCARIfIndex=_QtechIfQosCARIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,1),_QtechIfQosCARIfIndex_Type())
qtechIfQosCARIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARIfIndex.setStatus(_A)
_QtechIfQosCARIfName_Type=OctetString
_QtechIfQosCARIfName_Object=MibTableColumn
qtechIfQosCARIfName=_QtechIfQosCARIfName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,2),_QtechIfQosCARIfName_Type())
qtechIfQosCARIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARIfName.setStatus(_A)
class _QtechIfQosCARPktDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('outout',2)))
_QtechIfQosCARPktDirection_Type.__name__=_D
_QtechIfQosCARPktDirection_Object=MibTableColumn
qtechIfQosCARPktDirection=_QtechIfQosCARPktDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,3),_QtechIfQosCARPktDirection_Type())
qtechIfQosCARPktDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARPktDirection.setStatus(_A)
class _QtechIfQosCARType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acl',1),('dscp',2),('qos-group',3),('default',4)))
_QtechIfQosCARType_Type.__name__=_D
_QtechIfQosCARType_Object=MibTableColumn
qtechIfQosCARType=_QtechIfQosCARType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,4),_QtechIfQosCARType_Type())
qtechIfQosCARType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARType.setStatus(_A)
_QtechIfQosCARListNum_Type=Integer32
_QtechIfQosCARListNum_Object=MibTableColumn
qtechIfQosCARListNum=_QtechIfQosCARListNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,5),_QtechIfQosCARListNum_Type())
qtechIfQosCARListNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARListNum.setStatus(_A)
_QtechIfQosCARindex_Type=Integer32
_QtechIfQosCARindex_Object=MibTableColumn
qtechIfQosCARindex=_QtechIfQosCARindex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,6),_QtechIfQosCARindex_Type())
qtechIfQosCARindex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARindex.setStatus(_A)
class _QtechIfQosCARCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_QtechIfQosCARCIR_Type.__name__=_D
_QtechIfQosCARCIR_Object=MibTableColumn
qtechIfQosCARCIR=_QtechIfQosCARCIR_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,7),_QtechIfQosCARCIR_Type())
qtechIfQosCARCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARCIR.setStatus(_A)
class _QtechIfQosCARBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_QtechIfQosCARBurstSize_Type.__name__=_D
_QtechIfQosCARBurstSize_Object=MibTableColumn
qtechIfQosCARBurstSize=_QtechIfQosCARBurstSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,8),_QtechIfQosCARBurstSize_Type())
qtechIfQosCARBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARBurstSize.setStatus(_A)
class _QtechIfQosCARExcessBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_QtechIfQosCARExcessBurstSize_Type.__name__=_D
_QtechIfQosCARExcessBurstSize_Object=MibTableColumn
qtechIfQosCARExcessBurstSize=_QtechIfQosCARExcessBurstSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,9),_QtechIfQosCARExcessBurstSize_Type())
qtechIfQosCARExcessBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARExcessBurstSize.setStatus(_A)
class _QtechIfQosCARConformAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_QtechIfQosCARConformAction_Type.__name__=_D
_QtechIfQosCARConformAction_Object=MibTableColumn
qtechIfQosCARConformAction=_QtechIfQosCARConformAction_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,10),_QtechIfQosCARConformAction_Type())
qtechIfQosCARConformAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARConformAction.setStatus(_A)
class _QtechIfQosCARExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_QtechIfQosCARExceedAction_Type.__name__=_D
_QtechIfQosCARExceedAction_Object=MibTableColumn
qtechIfQosCARExceedAction=_QtechIfQosCARExceedAction_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,11),_QtechIfQosCARExceedAction_Type())
qtechIfQosCARExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARExceedAction.setStatus(_A)
class _QtechIfQosCARConformNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechIfQosCARConformNewPrec_Type.__name__=_D
_QtechIfQosCARConformNewPrec_Object=MibTableColumn
qtechIfQosCARConformNewPrec=_QtechIfQosCARConformNewPrec_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,12),_QtechIfQosCARConformNewPrec_Type())
qtechIfQosCARConformNewPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARConformNewPrec.setStatus(_A)
class _QtechIfQosCARExceedNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechIfQosCARExceedNewPrec_Type.__name__=_D
_QtechIfQosCARExceedNewPrec_Object=MibTableColumn
qtechIfQosCARExceedNewPrec=_QtechIfQosCARExceedNewPrec_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,13),_QtechIfQosCARExceedNewPrec_Type())
qtechIfQosCARExceedNewPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARExceedNewPrec.setStatus(_A)
_QtechIfQosCARConformPkt_Type=Counter32
_QtechIfQosCARConformPkt_Object=MibTableColumn
qtechIfQosCARConformPkt=_QtechIfQosCARConformPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,14),_QtechIfQosCARConformPkt_Type())
qtechIfQosCARConformPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARConformPkt.setStatus(_A)
_QtechIfQosCARConformByte_Type=Counter32
_QtechIfQosCARConformByte_Object=MibTableColumn
qtechIfQosCARConformByte=_QtechIfQosCARConformByte_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,15),_QtechIfQosCARConformByte_Type())
qtechIfQosCARConformByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARConformByte.setStatus(_A)
_QtechIfQosCARExceedPkt_Type=Counter32
_QtechIfQosCARExceedPkt_Object=MibTableColumn
qtechIfQosCARExceedPkt=_QtechIfQosCARExceedPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,16),_QtechIfQosCARExceedPkt_Type())
qtechIfQosCARExceedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARExceedPkt.setStatus(_A)
_QtechIfQosCARExceedByte_Type=Counter32
_QtechIfQosCARExceedByte_Object=MibTableColumn
qtechIfQosCARExceedByte=_QtechIfQosCARExceedByte_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,5,1,17),_QtechIfQosCARExceedByte_Type())
qtechIfQosCARExceedByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosCARExceedByte.setStatus(_A)
_QtechIfQosGTSTable_Object=MibTable
qtechIfQosGTSTable=_QtechIfQosGTSTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6))
if mibBuilder.loadTexts:qtechIfQosGTSTable.setStatus(_A)
_QtechIfQosGTSEntry_Object=MibTableRow
qtechIfQosGTSEntry=_QtechIfQosGTSEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1))
qtechIfQosGTSEntry.setIndexNames((0,_E,_z),(0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:qtechIfQosGTSEntry.setStatus(_A)
_QtechIfQosGTSIfIndex_Type=Integer32
_QtechIfQosGTSIfIndex_Object=MibTableColumn
qtechIfQosGTSIfIndex=_QtechIfQosGTSIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,1),_QtechIfQosGTSIfIndex_Type())
qtechIfQosGTSIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSIfIndex.setStatus(_A)
_QtechIfQosGTSIfName_Type=OctetString
_QtechIfQosGTSIfName_Object=MibTableColumn
qtechIfQosGTSIfName=_QtechIfQosGTSIfName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,2),_QtechIfQosGTSIfName_Type())
qtechIfQosGTSIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSIfName.setStatus(_A)
class _QtechIfQosGTSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('acl',1),('all',2)))
_QtechIfQosGTSType_Type.__name__=_D
_QtechIfQosGTSType_Object=MibTableColumn
qtechIfQosGTSType=_QtechIfQosGTSType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,3),_QtechIfQosGTSType_Type())
qtechIfQosGTSType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSType.setStatus(_A)
class _QtechIfQosGTSACLNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_QtechIfQosGTSACLNum_Type.__name__=_D
_QtechIfQosGTSACLNum_Object=MibTableColumn
qtechIfQosGTSACLNum=_QtechIfQosGTSACLNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,4),_QtechIfQosGTSACLNum_Type())
qtechIfQosGTSACLNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSACLNum.setStatus(_A)
class _QtechIfQosGTSCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_QtechIfQosGTSCIR_Type.__name__=_D
_QtechIfQosGTSCIR_Object=MibTableColumn
qtechIfQosGTSCIR=_QtechIfQosGTSCIR_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,5),_QtechIfQosGTSCIR_Type())
qtechIfQosGTSCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSCIR.setStatus(_A)
class _QtechIfQosGTSBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_QtechIfQosGTSBurstSize_Type.__name__=_D
_QtechIfQosGTSBurstSize_Object=MibTableColumn
qtechIfQosGTSBurstSize=_QtechIfQosGTSBurstSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,6),_QtechIfQosGTSBurstSize_Type())
qtechIfQosGTSBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSBurstSize.setStatus(_A)
class _QtechIfQosGTSExcessBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_QtechIfQosGTSExcessBurstSize_Type.__name__=_D
_QtechIfQosGTSExcessBurstSize_Object=MibTableColumn
qtechIfQosGTSExcessBurstSize=_QtechIfQosGTSExcessBurstSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,7),_QtechIfQosGTSExcessBurstSize_Type())
qtechIfQosGTSExcessBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSExcessBurstSize.setStatus(_A)
class _QtechIfQosGTSMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechIfQosGTSMaxQueLen_Type.__name__=_D
_QtechIfQosGTSMaxQueLen_Object=MibTableColumn
qtechIfQosGTSMaxQueLen=_QtechIfQosGTSMaxQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,8),_QtechIfQosGTSMaxQueLen_Type())
qtechIfQosGTSMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSMaxQueLen.setStatus(_A)
_QtechIfQosGTSCurQueLen_Type=Integer32
_QtechIfQosGTSCurQueLen_Object=MibTableColumn
qtechIfQosGTSCurQueLen=_QtechIfQosGTSCurQueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,9),_QtechIfQosGTSCurQueLen_Type())
qtechIfQosGTSCurQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSCurQueLen.setStatus(_A)
_QtechIfQosGTSPassPkt_Type=Counter32
_QtechIfQosGTSPassPkt_Object=MibTableColumn
qtechIfQosGTSPassPkt=_QtechIfQosGTSPassPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,10),_QtechIfQosGTSPassPkt_Type())
qtechIfQosGTSPassPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSPassPkt.setStatus(_A)
_QtechIfQosGTSPassByte_Type=Counter32
_QtechIfQosGTSPassByte_Object=MibTableColumn
qtechIfQosGTSPassByte=_QtechIfQosGTSPassByte_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,11),_QtechIfQosGTSPassByte_Type())
qtechIfQosGTSPassByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSPassByte.setStatus(_A)
_QtechIfQosGTSDiscardPkt_Type=Counter32
_QtechIfQosGTSDiscardPkt_Object=MibTableColumn
qtechIfQosGTSDiscardPkt=_QtechIfQosGTSDiscardPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,12),_QtechIfQosGTSDiscardPkt_Type())
qtechIfQosGTSDiscardPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSDiscardPkt.setStatus(_A)
_QtechIfQosGTSDiscardByte_Type=Counter32
_QtechIfQosGTSDiscardByte_Object=MibTableColumn
qtechIfQosGTSDiscardByte=_QtechIfQosGTSDiscardByte_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,6,1,13),_QtechIfQosGTSDiscardByte_Type())
qtechIfQosGTSDiscardByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosGTSDiscardByte.setStatus(_A)
_QtechIfQosRTPIfQueueRunInfoTable_Object=MibTable
qtechIfQosRTPIfQueueRunInfoTable=_QtechIfQosRTPIfQueueRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7))
if mibBuilder.loadTexts:qtechIfQosRTPIfQueueRunInfoTable.setStatus(_A)
_QtechIfQosRTPIfQueueRunInfoEntry_Object=MibTableRow
qtechIfQosRTPIfQueueRunInfoEntry=_QtechIfQosRTPIfQueueRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7,1))
qtechIfQosRTPIfQueueRunInfoEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:qtechIfQosRTPIfQueueRunInfoEntry.setStatus(_A)
_QtechIfQosRTPIfApplyIfIndex_Type=Integer32
_QtechIfQosRTPIfApplyIfIndex_Object=MibTableColumn
qtechIfQosRTPIfApplyIfIndex=_QtechIfQosRTPIfApplyIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7,1,1),_QtechIfQosRTPIfApplyIfIndex_Type())
qtechIfQosRTPIfApplyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosRTPIfApplyIfIndex.setStatus(_A)
_QtechIfQosRTPIfQueueSize_Type=Counter32
_QtechIfQosRTPIfQueueSize_Object=MibTableColumn
qtechIfQosRTPIfQueueSize=_QtechIfQosRTPIfQueueSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7,1,2),_QtechIfQosRTPIfQueueSize_Type())
qtechIfQosRTPIfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosRTPIfQueueSize.setStatus(_A)
_QtechIfQosRTPIfQueueMaxSize_Type=Counter32
_QtechIfQosRTPIfQueueMaxSize_Object=MibTableColumn
qtechIfQosRTPIfQueueMaxSize=_QtechIfQosRTPIfQueueMaxSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7,1,3),_QtechIfQosRTPIfQueueMaxSize_Type())
qtechIfQosRTPIfQueueMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosRTPIfQueueMaxSize.setStatus(_A)
_QtechIfQosRTPIfQueueOutputs_Type=Counter32
_QtechIfQosRTPIfQueueOutputs_Object=MibTableColumn
qtechIfQosRTPIfQueueOutputs=_QtechIfQosRTPIfQueueOutputs_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7,1,4),_QtechIfQosRTPIfQueueOutputs_Type())
qtechIfQosRTPIfQueueOutputs.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosRTPIfQueueOutputs.setStatus(_A)
_QtechIfQosRTPIfQueueDiscards_Type=Counter32
_QtechIfQosRTPIfQueueDiscards_Object=MibTableColumn
qtechIfQosRTPIfQueueDiscards=_QtechIfQosRTPIfQueueDiscards_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,7,1,5),_QtechIfQosRTPIfQueueDiscards_Type())
qtechIfQosRTPIfQueueDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosRTPIfQueueDiscards.setStatus(_A)
_QtechIfQosFlowLimitRunInfoTable_Object=MibTable
qtechIfQosFlowLimitRunInfoTable=_QtechIfQosFlowLimitRunInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8))
if mibBuilder.loadTexts:qtechIfQosFlowLimitRunInfoTable.setStatus(_A)
_QtechIfQosFlowLimitRunInfoEntry_Object=MibTableRow
qtechIfQosFlowLimitRunInfoEntry=_QtechIfQosFlowLimitRunInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1))
qtechIfQosFlowLimitRunInfoEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:qtechIfQosFlowLimitRunInfoEntry.setStatus(_A)
class _QtechIfQosFlowLimitLabelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QtechIfQosFlowLimitLabelNum_Type.__name__=_D
_QtechIfQosFlowLimitLabelNum_Object=MibTableColumn
qtechIfQosFlowLimitLabelNum=_QtechIfQosFlowLimitLabelNum_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,1),_QtechIfQosFlowLimitLabelNum_Type())
qtechIfQosFlowLimitLabelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitLabelNum.setStatus(_A)
class _QtechIfQosFlowLimitPktDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_QtechIfQosFlowLimitPktDirection_Type.__name__=_D
_QtechIfQosFlowLimitPktDirection_Object=MibTableColumn
qtechIfQosFlowLimitPktDirection=_QtechIfQosFlowLimitPktDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,2),_QtechIfQosFlowLimitPktDirection_Type())
qtechIfQosFlowLimitPktDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitPktDirection.setStatus(_A)
class _QtechIfQosFlowLimitCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_QtechIfQosFlowLimitCIR_Type.__name__=_D
_QtechIfQosFlowLimitCIR_Object=MibTableColumn
qtechIfQosFlowLimitCIR=_QtechIfQosFlowLimitCIR_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,3),_QtechIfQosFlowLimitCIR_Type())
qtechIfQosFlowLimitCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitCIR.setStatus(_A)
class _QtechIfQosFlowLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_QtechIfQosFlowLimitBurstSize_Type.__name__=_D
_QtechIfQosFlowLimitBurstSize_Object=MibTableColumn
qtechIfQosFlowLimitBurstSize=_QtechIfQosFlowLimitBurstSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,4),_QtechIfQosFlowLimitBurstSize_Type())
qtechIfQosFlowLimitBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitBurstSize.setStatus(_A)
class _QtechIfQosFlowLimitExcessBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_QtechIfQosFlowLimitExcessBurstSize_Type.__name__=_D
_QtechIfQosFlowLimitExcessBurstSize_Object=MibTableColumn
qtechIfQosFlowLimitExcessBurstSize=_QtechIfQosFlowLimitExcessBurstSize_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,5),_QtechIfQosFlowLimitExcessBurstSize_Type())
qtechIfQosFlowLimitExcessBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitExcessBurstSize.setStatus(_A)
class _QtechIfQosFlowLimitConformAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_QtechIfQosFlowLimitConformAction_Type.__name__=_D
_QtechIfQosFlowLimitConformAction_Object=MibTableColumn
qtechIfQosFlowLimitConformAction=_QtechIfQosFlowLimitConformAction_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,6),_QtechIfQosFlowLimitConformAction_Type())
qtechIfQosFlowLimitConformAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitConformAction.setStatus(_A)
class _QtechIfQosFlowLimitExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_QtechIfQosFlowLimitExceedAction_Type.__name__=_D
_QtechIfQosFlowLimitExceedAction_Object=MibTableColumn
qtechIfQosFlowLimitExceedAction=_QtechIfQosFlowLimitExceedAction_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,7),_QtechIfQosFlowLimitExceedAction_Type())
qtechIfQosFlowLimitExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitExceedAction.setStatus(_A)
class _QtechIfQosFlowLimitConformNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QtechIfQosFlowLimitConformNewPrec_Type.__name__=_D
_QtechIfQosFlowLimitConformNewPrec_Object=MibTableColumn
qtechIfQosFlowLimitConformNewPrec=_QtechIfQosFlowLimitConformNewPrec_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,8),_QtechIfQosFlowLimitConformNewPrec_Type())
qtechIfQosFlowLimitConformNewPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitConformNewPrec.setStatus(_A)
class _QtechIfQosFlowLimitExceedNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QtechIfQosFlowLimitExceedNewPrec_Type.__name__=_D
_QtechIfQosFlowLimitExceedNewPrec_Object=MibTableColumn
qtechIfQosFlowLimitExceedNewPrec=_QtechIfQosFlowLimitExceedNewPrec_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,9),_QtechIfQosFlowLimitExceedNewPrec_Type())
qtechIfQosFlowLimitExceedNewPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitExceedNewPrec.setStatus(_A)
_QtechIfQosFlowLimitConformPkt_Type=Counter32
_QtechIfQosFlowLimitConformPkt_Object=MibTableColumn
qtechIfQosFlowLimitConformPkt=_QtechIfQosFlowLimitConformPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,10),_QtechIfQosFlowLimitConformPkt_Type())
qtechIfQosFlowLimitConformPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitConformPkt.setStatus(_A)
_QtechIfQosFlowLimitConformByte_Type=Counter32
_QtechIfQosFlowLimitConformByte_Object=MibTableColumn
qtechIfQosFlowLimitConformByte=_QtechIfQosFlowLimitConformByte_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,11),_QtechIfQosFlowLimitConformByte_Type())
qtechIfQosFlowLimitConformByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitConformByte.setStatus(_A)
_QtechIfQosFlowLimitExceedPkt_Type=Counter32
_QtechIfQosFlowLimitExceedPkt_Object=MibTableColumn
qtechIfQosFlowLimitExceedPkt=_QtechIfQosFlowLimitExceedPkt_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,12),_QtechIfQosFlowLimitExceedPkt_Type())
qtechIfQosFlowLimitExceedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitExceedPkt.setStatus(_A)
_QtechIfQosFlowLimitExceedByte_Type=Counter32
_QtechIfQosFlowLimitExceedByte_Object=MibTableColumn
qtechIfQosFlowLimitExceedByte=_QtechIfQosFlowLimitExceedByte_Object((1,3,6,1,4,1,27514,1,1,10,2,106,2,8,1,13),_QtechIfQosFlowLimitExceedByte_Type())
qtechIfQosFlowLimitExceedByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQosFlowLimitExceedByte.setStatus(_A)
_QtechHQoSMIBObjects_ObjectIdentity=ObjectIdentity
qtechHQoSMIBObjects=_QtechHQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3))
_QtechHQoSScalarObjects_ObjectIdentity=ObjectIdentity
qtechHQoSScalarObjects=_QtechHQoSScalarObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,1))
class _QtechHQoSNameType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknownName',0),('userQNameIn',1),('userQNameOut',2),('userGroupQInName',3),('userGroupQOutName',4),('flowQName',5),('flowMapName',6),('trafficClassifierName',7),('trafficBehaviorName',8),('trafficPolicyName',9),('portQName',10)))
_QtechHQoSNameType_Type.__name__=_D
_QtechHQoSNameType_Object=MibScalar
qtechHQoSNameType=_QtechHQoSNameType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,1,1),_QtechHQoSNameType_Type())
qtechHQoSNameType.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSNameType.setStatus(_A)
class _QtechHQoSNameFind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSNameFind_Type.__name__=_F
_QtechHQoSNameFind_Object=MibScalar
qtechHQoSNameFind=_QtechHQoSNameFind_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,1,2),_QtechHQoSNameFind_Type())
qtechHQoSNameFind.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSNameFind.setStatus(_A)
class _QtechHQoSNameIndex_Type(Integer32):defaultValue=0
_QtechHQoSNameIndex_Type.__name__=_D
_QtechHQoSNameIndex_Object=MibScalar
qtechHQoSNameIndex=_QtechHQoSNameIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,1,3),_QtechHQoSNameIndex_Type())
qtechHQoSNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSNameIndex.setStatus(_A)
_QtechHQoSUserQObjects_ObjectIdentity=ObjectIdentity
qtechHQoSUserQObjects=_QtechHQoSUserQObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,2))
_QtechHQoSUserQInIndexNext_Type=Integer32
_QtechHQoSUserQInIndexNext_Object=MibScalar
qtechHQoSUserQInIndexNext=_QtechHQoSUserQInIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,1),_QtechHQoSUserQInIndexNext_Type())
qtechHQoSUserQInIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserQInIndexNext.setStatus(_A)
_QtechHQoSUserQOutIndexNext_Type=Integer32
_QtechHQoSUserQOutIndexNext_Object=MibScalar
qtechHQoSUserQOutIndexNext=_QtechHQoSUserQOutIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,2),_QtechHQoSUserQOutIndexNext_Type())
qtechHQoSUserQOutIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserQOutIndexNext.setStatus(_A)
_QtechHQoSUserQTable_Object=MibTable
qtechHQoSUserQTable=_QtechHQoSUserQTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3))
if mibBuilder.loadTexts:qtechHQoSUserQTable.setStatus(_A)
_QtechHQoSUserQEntry_Object=MibTableRow
qtechHQoSUserQEntry=_QtechHQoSUserQEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1))
qtechHQoSUserQEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:qtechHQoSUserQEntry.setStatus(_A)
_QtechHQoSUserQIndex_Type=Unsigned32
_QtechHQoSUserQIndex_Object=MibTableColumn
qtechHQoSUserQIndex=_QtechHQoSUserQIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,1),_QtechHQoSUserQIndex_Type())
qtechHQoSUserQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSUserQIndex.setStatus(_A)
class _QtechHQoSUserQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSUserQName_Type.__name__=_F
_QtechHQoSUserQName_Object=MibTableColumn
qtechHQoSUserQName=_QtechHQoSUserQName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,2),_QtechHQoSUserQName_Type())
qtechHQoSUserQName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQName.setStatus(_A)
_QtechHQoSUserQDirection_Type=QtechQDirectionType
_QtechHQoSUserQDirection_Object=MibTableColumn
qtechHQoSUserQDirection=_QtechHQoSUserQDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,3),_QtechHQoSUserQDirection_Type())
qtechHQoSUserQDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQDirection.setStatus(_A)
_QtechHQoSUserQRowStatus_Type=RowStatus
_QtechHQoSUserQRowStatus_Object=MibTableColumn
qtechHQoSUserQRowStatus=_QtechHQoSUserQRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,4),_QtechHQoSUserQRowStatus_Type())
qtechHQoSUserQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQRowStatus.setStatus(_A)
class _QtechHQoSUserQFlowQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSUserQFlowQName_Type.__name__=_F
_QtechHQoSUserQFlowQName_Object=MibTableColumn
qtechHQoSUserQFlowQName=_QtechHQoSUserQFlowQName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,5),_QtechHQoSUserQFlowQName_Type())
qtechHQoSUserQFlowQName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQFlowQName.setStatus(_A)
_QtechHQoSUserQFlowQIndex_Type=Unsigned32
_QtechHQoSUserQFlowQIndex_Object=MibTableColumn
qtechHQoSUserQFlowQIndex=_QtechHQoSUserQFlowQIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,6),_QtechHQoSUserQFlowQIndex_Type())
qtechHQoSUserQFlowQIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserQFlowQIndex.setStatus(_A)
class _QtechHQoSUserQGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSUserQGroupName_Type.__name__=_F
_QtechHQoSUserQGroupName_Object=MibTableColumn
qtechHQoSUserQGroupName=_QtechHQoSUserQGroupName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,7),_QtechHQoSUserQGroupName_Type())
qtechHQoSUserQGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQGroupName.setStatus(_A)
_QtechHQoSUserQGroupIndex_Type=Unsigned32
_QtechHQoSUserQGroupIndex_Object=MibTableColumn
qtechHQoSUserQGroupIndex=_QtechHQoSUserQGroupIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,8),_QtechHQoSUserQGroupIndex_Type())
qtechHQoSUserQGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserQGroupIndex.setStatus(_A)
class _QtechHQoSUserQFlowMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSUserQFlowMapName_Type.__name__=_F
_QtechHQoSUserQFlowMapName_Object=MibTableColumn
qtechHQoSUserQFlowMapName=_QtechHQoSUserQFlowMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,9),_QtechHQoSUserQFlowMapName_Type())
qtechHQoSUserQFlowMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQFlowMapName.setStatus(_A)
_QtechHQoSUserQFlowMapIndex_Type=Unsigned32
_QtechHQoSUserQFlowMapIndex_Object=MibTableColumn
qtechHQoSUserQFlowMapIndex=_QtechHQoSUserQFlowMapIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,10),_QtechHQoSUserQFlowMapIndex_Type())
qtechHQoSUserQFlowMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserQFlowMapIndex.setStatus(_A)
class _QtechHQoSUserQCIR_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSUserQCIR_Type.__name__=_M
_QtechHQoSUserQCIR_Object=MibTableColumn
qtechHQoSUserQCIR=_QtechHQoSUserQCIR_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,11),_QtechHQoSUserQCIR_Type())
qtechHQoSUserQCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQCIR.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSUserQCIR.setUnits(_G)
class _QtechHQoSUserQPIR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_QtechHQoSUserQPIR_Type.__name__=_M
_QtechHQoSUserQPIR_Object=MibTableColumn
qtechHQoSUserQPIR=_QtechHQoSUserQPIR_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,2,3,1,12),_QtechHQoSUserQPIR_Type())
qtechHQoSUserQPIR.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserQPIR.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSUserQPIR.setUnits(_G)
_QtechHQoSUserGroupQObjects_ObjectIdentity=ObjectIdentity
qtechHQoSUserGroupQObjects=_QtechHQoSUserGroupQObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,3))
_QtechHQoSUserGroupQInIndexNext_Type=Integer32
_QtechHQoSUserGroupQInIndexNext_Object=MibScalar
qtechHQoSUserGroupQInIndexNext=_QtechHQoSUserGroupQInIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,1),_QtechHQoSUserGroupQInIndexNext_Type())
qtechHQoSUserGroupQInIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserGroupQInIndexNext.setStatus(_A)
_QtechHQoSUserGroupQOutIndexNext_Type=Integer32
_QtechHQoSUserGroupQOutIndexNext_Object=MibScalar
qtechHQoSUserGroupQOutIndexNext=_QtechHQoSUserGroupQOutIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,2),_QtechHQoSUserGroupQOutIndexNext_Type())
qtechHQoSUserGroupQOutIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSUserGroupQOutIndexNext.setStatus(_A)
_QtechHQoSUserGroupQTable_Object=MibTable
qtechHQoSUserGroupQTable=_QtechHQoSUserGroupQTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3))
if mibBuilder.loadTexts:qtechHQoSUserGroupQTable.setStatus(_A)
_QtechHQoSUserGroupQEntry_Object=MibTableRow
qtechHQoSUserGroupQEntry=_QtechHQoSUserGroupQEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3,1))
qtechHQoSUserGroupQEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:qtechHQoSUserGroupQEntry.setStatus(_A)
_QtechHQoSUserGroupQIndex_Type=Unsigned32
_QtechHQoSUserGroupQIndex_Object=MibTableColumn
qtechHQoSUserGroupQIndex=_QtechHQoSUserGroupQIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3,1,1),_QtechHQoSUserGroupQIndex_Type())
qtechHQoSUserGroupQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSUserGroupQIndex.setStatus(_A)
class _QtechHQoSUserGroupQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSUserGroupQName_Type.__name__=_F
_QtechHQoSUserGroupQName_Object=MibTableColumn
qtechHQoSUserGroupQName=_QtechHQoSUserGroupQName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3,1,2),_QtechHQoSUserGroupQName_Type())
qtechHQoSUserGroupQName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserGroupQName.setStatus(_A)
_QtechHQoSUserGroupQDirection_Type=QtechQDirectionType
_QtechHQoSUserGroupQDirection_Object=MibTableColumn
qtechHQoSUserGroupQDirection=_QtechHQoSUserGroupQDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3,1,3),_QtechHQoSUserGroupQDirection_Type())
qtechHQoSUserGroupQDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserGroupQDirection.setStatus(_A)
_QtechHQoSUserGroupQRowStatus_Type=RowStatus
_QtechHQoSUserGroupQRowStatus_Object=MibTableColumn
qtechHQoSUserGroupQRowStatus=_QtechHQoSUserGroupQRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3,1,4),_QtechHQoSUserGroupQRowStatus_Type())
qtechHQoSUserGroupQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserGroupQRowStatus.setStatus(_A)
class _QtechHQoSUserGroupQShaping_Type(Unsigned32):defaultValue=10000000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSUserGroupQShaping_Type.__name__=_M
_QtechHQoSUserGroupQShaping_Object=MibTableColumn
qtechHQoSUserGroupQShaping=_QtechHQoSUserGroupQShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,3,3,1,5),_QtechHQoSUserGroupQShaping_Type())
qtechHQoSUserGroupQShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSUserGroupQShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSUserGroupQShaping.setUnits(_G)
_QtechHQoSFlowQObjects_ObjectIdentity=ObjectIdentity
qtechHQoSFlowQObjects=_QtechHQoSFlowQObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,4))
_QtechHQoSFlowQIndexNext_Type=Integer32
_QtechHQoSFlowQIndexNext_Object=MibScalar
qtechHQoSFlowQIndexNext=_QtechHQoSFlowQIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,1),_QtechHQoSFlowQIndexNext_Type())
qtechHQoSFlowQIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSFlowQIndexNext.setStatus(_A)
_QtechHQoSFlowQTable_Object=MibTable
qtechHQoSFlowQTable=_QtechHQoSFlowQTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2))
if mibBuilder.loadTexts:qtechHQoSFlowQTable.setStatus(_A)
_QtechHQoSFlowQEntry_Object=MibTableRow
qtechHQoSFlowQEntry=_QtechHQoSFlowQEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1))
qtechHQoSFlowQEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:qtechHQoSFlowQEntry.setStatus(_A)
_QtechHQoSFlowQIndex_Type=Unsigned32
_QtechHQoSFlowQIndex_Object=MibTableColumn
qtechHQoSFlowQIndex=_QtechHQoSFlowQIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,1),_QtechHQoSFlowQIndex_Type())
qtechHQoSFlowQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSFlowQIndex.setStatus(_A)
class _QtechHQoSFlowQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQName_Type.__name__=_F
_QtechHQoSFlowQName_Object=MibTableColumn
qtechHQoSFlowQName=_QtechHQoSFlowQName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,2),_QtechHQoSFlowQName_Type())
qtechHQoSFlowQName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQName.setStatus(_A)
_QtechHQoSFlowQRowStatus_Type=RowStatus
_QtechHQoSFlowQRowStatus_Object=MibTableColumn
qtechHQoSFlowQRowStatus=_QtechHQoSFlowQRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,3),_QtechHQoSFlowQRowStatus_Type())
qtechHQoSFlowQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQRowStatus.setStatus(_A)
class _QtechHQoSFlowQBEQType_Type(QtechQType):defaultValue=2
_QtechHQoSFlowQBEQType_Type.__name__=_H
_QtechHQoSFlowQBEQType_Object=MibTableColumn
qtechHQoSFlowQBEQType=_QtechHQoSFlowQBEQType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,4),_QtechHQoSFlowQBEQType_Type())
qtechHQoSFlowQBEQType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQBEQType.setStatus(_A)
class _QtechHQoSFlowQBEQWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQBEQWredWeight_Type.__name__=_D
_QtechHQoSFlowQBEQWredWeight_Object=MibTableColumn
qtechHQoSFlowQBEQWredWeight=_QtechHQoSFlowQBEQWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,5),_QtechHQoSFlowQBEQWredWeight_Type())
qtechHQoSFlowQBEQWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQBEQWredWeight.setStatus(_A)
class _QtechHQoSFlowQBEQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQBEQWredName_Type.__name__=_F
_QtechHQoSFlowQBEQWredName_Object=MibTableColumn
qtechHQoSFlowQBEQWredName=_QtechHQoSFlowQBEQWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,6),_QtechHQoSFlowQBEQWredName_Type())
qtechHQoSFlowQBEQWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQBEQWredName.setStatus(_A)
class _QtechHQoSFlowQBEQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQBEQDepth_Type.__name__=_D
_QtechHQoSFlowQBEQDepth_Object=MibTableColumn
qtechHQoSFlowQBEQDepth=_QtechHQoSFlowQBEQDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,7),_QtechHQoSFlowQBEQDepth_Type())
qtechHQoSFlowQBEQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQBEQDepth.setStatus(_A)
class _QtechHQoSFlowQBEQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQBEQShaping_Type.__name__=_D
_QtechHQoSFlowQBEQShaping_Object=MibTableColumn
qtechHQoSFlowQBEQShaping=_QtechHQoSFlowQBEQShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,8),_QtechHQoSFlowQBEQShaping_Type())
qtechHQoSFlowQBEQShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQBEQShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQBEQShaping.setUnits(_G)
class _QtechHQoSFlowQAF1QType_Type(QtechQType):defaultValue=2
_QtechHQoSFlowQAF1QType_Type.__name__=_H
_QtechHQoSFlowQAF1QType_Object=MibTableColumn
qtechHQoSFlowQAF1QType=_QtechHQoSFlowQAF1QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,9),_QtechHQoSFlowQAF1QType_Type())
qtechHQoSFlowQAF1QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF1QType.setStatus(_A)
class _QtechHQoSFlowQAF1QWredWeight_Type(Integer32):defaultValue=10
_QtechHQoSFlowQAF1QWredWeight_Type.__name__=_D
_QtechHQoSFlowQAF1QWredWeight_Object=MibTableColumn
qtechHQoSFlowQAF1QWredWeight=_QtechHQoSFlowQAF1QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,10),_QtechHQoSFlowQAF1QWredWeight_Type())
qtechHQoSFlowQAF1QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF1QWredWeight.setStatus(_A)
class _QtechHQoSFlowQAF1QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQAF1QWredName_Type.__name__=_F
_QtechHQoSFlowQAF1QWredName_Object=MibTableColumn
qtechHQoSFlowQAF1QWredName=_QtechHQoSFlowQAF1QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,11),_QtechHQoSFlowQAF1QWredName_Type())
qtechHQoSFlowQAF1QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF1QWredName.setStatus(_A)
class _QtechHQoSFlowQAF1QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQAF1QDepth_Type.__name__=_D
_QtechHQoSFlowQAF1QDepth_Object=MibTableColumn
qtechHQoSFlowQAF1QDepth=_QtechHQoSFlowQAF1QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,12),_QtechHQoSFlowQAF1QDepth_Type())
qtechHQoSFlowQAF1QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF1QDepth.setStatus(_A)
class _QtechHQoSFlowQAF1QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQAF1QShaping_Type.__name__=_D
_QtechHQoSFlowQAF1QShaping_Object=MibTableColumn
qtechHQoSFlowQAF1QShaping=_QtechHQoSFlowQAF1QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,13),_QtechHQoSFlowQAF1QShaping_Type())
qtechHQoSFlowQAF1QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF1QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQAF1QShaping.setUnits(_G)
class _QtechHQoSFlowQAF2QType_Type(QtechQType):defaultValue=2
_QtechHQoSFlowQAF2QType_Type.__name__=_H
_QtechHQoSFlowQAF2QType_Object=MibTableColumn
qtechHQoSFlowQAF2QType=_QtechHQoSFlowQAF2QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,14),_QtechHQoSFlowQAF2QType_Type())
qtechHQoSFlowQAF2QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF2QType.setStatus(_A)
class _QtechHQoSFlowQAF2QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQAF2QWredWeight_Type.__name__=_D
_QtechHQoSFlowQAF2QWredWeight_Object=MibTableColumn
qtechHQoSFlowQAF2QWredWeight=_QtechHQoSFlowQAF2QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,15),_QtechHQoSFlowQAF2QWredWeight_Type())
qtechHQoSFlowQAF2QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF2QWredWeight.setStatus(_A)
class _QtechHQoSFlowQAF2QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQAF2QWredName_Type.__name__=_F
_QtechHQoSFlowQAF2QWredName_Object=MibTableColumn
qtechHQoSFlowQAF2QWredName=_QtechHQoSFlowQAF2QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,16),_QtechHQoSFlowQAF2QWredName_Type())
qtechHQoSFlowQAF2QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF2QWredName.setStatus(_A)
class _QtechHQoSFlowQAF2QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQAF2QDepth_Type.__name__=_D
_QtechHQoSFlowQAF2QDepth_Object=MibTableColumn
qtechHQoSFlowQAF2QDepth=_QtechHQoSFlowQAF2QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,17),_QtechHQoSFlowQAF2QDepth_Type())
qtechHQoSFlowQAF2QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF2QDepth.setStatus(_A)
class _QtechHQoSFlowQAF2QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQAF2QShaping_Type.__name__=_D
_QtechHQoSFlowQAF2QShaping_Object=MibTableColumn
qtechHQoSFlowQAF2QShaping=_QtechHQoSFlowQAF2QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,18),_QtechHQoSFlowQAF2QShaping_Type())
qtechHQoSFlowQAF2QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF2QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQAF2QShaping.setUnits(_G)
class _QtechHQoSFlowQAF3QType_Type(QtechQType):defaultValue=2
_QtechHQoSFlowQAF3QType_Type.__name__=_H
_QtechHQoSFlowQAF3QType_Object=MibTableColumn
qtechHQoSFlowQAF3QType=_QtechHQoSFlowQAF3QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,19),_QtechHQoSFlowQAF3QType_Type())
qtechHQoSFlowQAF3QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QType.setStatus(_A)
class _QtechHQoSFlowQAF3QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQAF3QWredWeight_Type.__name__=_D
_QtechHQoSFlowQAF3QWredWeight_Object=MibTableColumn
qtechHQoSFlowQAF3QWredWeight=_QtechHQoSFlowQAF3QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,20),_QtechHQoSFlowQAF3QWredWeight_Type())
qtechHQoSFlowQAF3QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QWredWeight.setStatus(_A)
class _QtechHQoSFlowQAF3QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQAF3QWredName_Type.__name__=_F
_QtechHQoSFlowQAF3QWredName_Object=MibTableColumn
qtechHQoSFlowQAF3QWredName=_QtechHQoSFlowQAF3QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,21),_QtechHQoSFlowQAF3QWredName_Type())
qtechHQoSFlowQAF3QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QWredName.setStatus(_A)
class _QtechHQoSFlowQAF3QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQAF3QDepth_Type.__name__=_D
_QtechHQoSFlowQAF3QDepth_Object=MibTableColumn
qtechHQoSFlowQAF3QDepth=_QtechHQoSFlowQAF3QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,22),_QtechHQoSFlowQAF3QDepth_Type())
qtechHQoSFlowQAF3QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QDepth.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QDepth.setUnits(_G)
class _QtechHQoSFlowQAF3QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQAF3QShaping_Type.__name__=_D
_QtechHQoSFlowQAF3QShaping_Object=MibTableColumn
qtechHQoSFlowQAF3QShaping=_QtechHQoSFlowQAF3QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,23),_QtechHQoSFlowQAF3QShaping_Type())
qtechHQoSFlowQAF3QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQAF3QShaping.setUnits(_G)
class _QtechHQoSFlowQAF4QType_Type(QtechQType):defaultValue=2
_QtechHQoSFlowQAF4QType_Type.__name__=_H
_QtechHQoSFlowQAF4QType_Object=MibTableColumn
qtechHQoSFlowQAF4QType=_QtechHQoSFlowQAF4QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,24),_QtechHQoSFlowQAF4QType_Type())
qtechHQoSFlowQAF4QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF4QType.setStatus(_A)
class _QtechHQoSFlowQAF4QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQAF4QWredWeight_Type.__name__=_D
_QtechHQoSFlowQAF4QWredWeight_Object=MibTableColumn
qtechHQoSFlowQAF4QWredWeight=_QtechHQoSFlowQAF4QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,25),_QtechHQoSFlowQAF4QWredWeight_Type())
qtechHQoSFlowQAF4QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF4QWredWeight.setStatus(_A)
class _QtechHQoSFlowQAF4QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQAF4QWredName_Type.__name__=_F
_QtechHQoSFlowQAF4QWredName_Object=MibTableColumn
qtechHQoSFlowQAF4QWredName=_QtechHQoSFlowQAF4QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,26),_QtechHQoSFlowQAF4QWredName_Type())
qtechHQoSFlowQAF4QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF4QWredName.setStatus(_A)
class _QtechHQoSFlowQAF4QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQAF4QDepth_Type.__name__=_D
_QtechHQoSFlowQAF4QDepth_Object=MibTableColumn
qtechHQoSFlowQAF4QDepth=_QtechHQoSFlowQAF4QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,27),_QtechHQoSFlowQAF4QDepth_Type())
qtechHQoSFlowQAF4QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF4QDepth.setStatus(_A)
class _QtechHQoSFlowQAF4QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_QtechHQoSFlowQAF4QShaping_Type.__name__=_D
_QtechHQoSFlowQAF4QShaping_Object=MibTableColumn
qtechHQoSFlowQAF4QShaping=_QtechHQoSFlowQAF4QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,28),_QtechHQoSFlowQAF4QShaping_Type())
qtechHQoSFlowQAF4QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQAF4QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQAF4QShaping.setUnits(_G)
class _QtechHQoSFlowQEFQType_Type(QtechQType):defaultValue=3
_QtechHQoSFlowQEFQType_Type.__name__=_H
_QtechHQoSFlowQEFQType_Object=MibTableColumn
qtechHQoSFlowQEFQType=_QtechHQoSFlowQEFQType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,29),_QtechHQoSFlowQEFQType_Type())
qtechHQoSFlowQEFQType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQEFQType.setStatus(_A)
class _QtechHQoSFlowQEFQWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQEFQWredWeight_Type.__name__=_D
_QtechHQoSFlowQEFQWredWeight_Object=MibTableColumn
qtechHQoSFlowQEFQWredWeight=_QtechHQoSFlowQEFQWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,30),_QtechHQoSFlowQEFQWredWeight_Type())
qtechHQoSFlowQEFQWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQEFQWredWeight.setStatus(_A)
class _QtechHQoSFlowQEFQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQEFQWredName_Type.__name__=_F
_QtechHQoSFlowQEFQWredName_Object=MibTableColumn
qtechHQoSFlowQEFQWredName=_QtechHQoSFlowQEFQWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,31),_QtechHQoSFlowQEFQWredName_Type())
qtechHQoSFlowQEFQWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQEFQWredName.setStatus(_A)
class _QtechHQoSFlowQEFQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQEFQDepth_Type.__name__=_D
_QtechHQoSFlowQEFQDepth_Object=MibTableColumn
qtechHQoSFlowQEFQDepth=_QtechHQoSFlowQEFQDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,32),_QtechHQoSFlowQEFQDepth_Type())
qtechHQoSFlowQEFQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQEFQDepth.setStatus(_A)
class _QtechHQoSFlowQEFQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQEFQShaping_Type.__name__=_D
_QtechHQoSFlowQEFQShaping_Object=MibTableColumn
qtechHQoSFlowQEFQShaping=_QtechHQoSFlowQEFQShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,33),_QtechHQoSFlowQEFQShaping_Type())
qtechHQoSFlowQEFQShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQEFQShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQEFQShaping.setUnits(_G)
class _QtechHQoSFlowQCS6QType_Type(QtechQType):defaultValue=3
_QtechHQoSFlowQCS6QType_Type.__name__=_H
_QtechHQoSFlowQCS6QType_Object=MibTableColumn
qtechHQoSFlowQCS6QType=_QtechHQoSFlowQCS6QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,34),_QtechHQoSFlowQCS6QType_Type())
qtechHQoSFlowQCS6QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS6QType.setStatus(_A)
class _QtechHQoSFlowQCS6QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQCS6QWredWeight_Type.__name__=_D
_QtechHQoSFlowQCS6QWredWeight_Object=MibTableColumn
qtechHQoSFlowQCS6QWredWeight=_QtechHQoSFlowQCS6QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,35),_QtechHQoSFlowQCS6QWredWeight_Type())
qtechHQoSFlowQCS6QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS6QWredWeight.setStatus(_A)
class _QtechHQoSFlowQCS6QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQCS6QWredName_Type.__name__=_F
_QtechHQoSFlowQCS6QWredName_Object=MibTableColumn
qtechHQoSFlowQCS6QWredName=_QtechHQoSFlowQCS6QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,36),_QtechHQoSFlowQCS6QWredName_Type())
qtechHQoSFlowQCS6QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS6QWredName.setStatus(_A)
class _QtechHQoSFlowQCS6QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQCS6QDepth_Type.__name__=_D
_QtechHQoSFlowQCS6QDepth_Object=MibTableColumn
qtechHQoSFlowQCS6QDepth=_QtechHQoSFlowQCS6QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,37),_QtechHQoSFlowQCS6QDepth_Type())
qtechHQoSFlowQCS6QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS6QDepth.setStatus(_A)
class _QtechHQoSFlowQCS6QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQCS6QShaping_Type.__name__=_D
_QtechHQoSFlowQCS6QShaping_Object=MibTableColumn
qtechHQoSFlowQCS6QShaping=_QtechHQoSFlowQCS6QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,38),_QtechHQoSFlowQCS6QShaping_Type())
qtechHQoSFlowQCS6QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS6QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQCS6QShaping.setUnits(_G)
class _QtechHQoSFlowQCS7QType_Type(QtechQType):defaultValue=3
_QtechHQoSFlowQCS7QType_Type.__name__=_H
_QtechHQoSFlowQCS7QType_Object=MibTableColumn
qtechHQoSFlowQCS7QType=_QtechHQoSFlowQCS7QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,39),_QtechHQoSFlowQCS7QType_Type())
qtechHQoSFlowQCS7QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS7QType.setStatus(_A)
class _QtechHQoSFlowQCS7QWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSFlowQCS7QWredWeight_Type.__name__=_D
_QtechHQoSFlowQCS7QWredWeight_Object=MibTableColumn
qtechHQoSFlowQCS7QWredWeight=_QtechHQoSFlowQCS7QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,40),_QtechHQoSFlowQCS7QWredWeight_Type())
qtechHQoSFlowQCS7QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS7QWredWeight.setStatus(_A)
class _QtechHQoSFlowQCS7QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowQCS7QWredName_Type.__name__=_F
_QtechHQoSFlowQCS7QWredName_Object=MibTableColumn
qtechHQoSFlowQCS7QWredName=_QtechHQoSFlowQCS7QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,41),_QtechHQoSFlowQCS7QWredName_Type())
qtechHQoSFlowQCS7QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS7QWredName.setStatus(_A)
class _QtechHQoSFlowQCS7QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSFlowQCS7QDepth_Type.__name__=_D
_QtechHQoSFlowQCS7QDepth_Object=MibTableColumn
qtechHQoSFlowQCS7QDepth=_QtechHQoSFlowQCS7QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,42),_QtechHQoSFlowQCS7QDepth_Type())
qtechHQoSFlowQCS7QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS7QDepth.setStatus(_A)
class _QtechHQoSFlowQCS7QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSFlowQCS7QShaping_Type.__name__=_D
_QtechHQoSFlowQCS7QShaping_Object=MibTableColumn
qtechHQoSFlowQCS7QShaping=_QtechHQoSFlowQCS7QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,4,2,1,43),_QtechHQoSFlowQCS7QShaping_Type())
qtechHQoSFlowQCS7QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowQCS7QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSFlowQCS7QShaping.setUnits(_G)
_QtechHQoSFlowMapObjects_ObjectIdentity=ObjectIdentity
qtechHQoSFlowMapObjects=_QtechHQoSFlowMapObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,5))
_QtechHQoSFlowMapIndexNext_Type=Integer32
_QtechHQoSFlowMapIndexNext_Object=MibScalar
qtechHQoSFlowMapIndexNext=_QtechHQoSFlowMapIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,1),_QtechHQoSFlowMapIndexNext_Type())
qtechHQoSFlowMapIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSFlowMapIndexNext.setStatus(_A)
_QtechHQoSFlowMapTable_Object=MibTable
qtechHQoSFlowMapTable=_QtechHQoSFlowMapTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2))
if mibBuilder.loadTexts:qtechHQoSFlowMapTable.setStatus(_A)
_QtechHQoSFlowMapEntry_Object=MibTableRow
qtechHQoSFlowMapEntry=_QtechHQoSFlowMapEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1))
qtechHQoSFlowMapEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:qtechHQoSFlowMapEntry.setStatus(_A)
_QtechHQoSFlowMapIndex_Type=Unsigned32
_QtechHQoSFlowMapIndex_Object=MibTableColumn
qtechHQoSFlowMapIndex=_QtechHQoSFlowMapIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,1),_QtechHQoSFlowMapIndex_Type())
qtechHQoSFlowMapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSFlowMapIndex.setStatus(_A)
class _QtechHQoSFlowMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSFlowMapName_Type.__name__=_F
_QtechHQoSFlowMapName_Object=MibTableColumn
qtechHQoSFlowMapName=_QtechHQoSFlowMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,2),_QtechHQoSFlowMapName_Type())
qtechHQoSFlowMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapName.setStatus(_A)
_QtechHQoSFlowMapRowStatus_Type=RowStatus
_QtechHQoSFlowMapRowStatus_Object=MibTableColumn
qtechHQoSFlowMapRowStatus=_QtechHQoSFlowMapRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,3),_QtechHQoSFlowMapRowStatus_Type())
qtechHQoSFlowMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapRowStatus.setStatus(_A)
class _QtechHQoSFlowMapBEQ2PortQ_Type(QtechCosType):defaultValue=1
_QtechHQoSFlowMapBEQ2PortQ_Type.__name__=_K
_QtechHQoSFlowMapBEQ2PortQ_Object=MibTableColumn
qtechHQoSFlowMapBEQ2PortQ=_QtechHQoSFlowMapBEQ2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,4),_QtechHQoSFlowMapBEQ2PortQ_Type())
qtechHQoSFlowMapBEQ2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapBEQ2PortQ.setStatus(_A)
class _QtechHQoSFlowMapAF1Q2PortQ_Type(QtechCosType):defaultValue=2
_QtechHQoSFlowMapAF1Q2PortQ_Type.__name__=_K
_QtechHQoSFlowMapAF1Q2PortQ_Object=MibTableColumn
qtechHQoSFlowMapAF1Q2PortQ=_QtechHQoSFlowMapAF1Q2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,5),_QtechHQoSFlowMapAF1Q2PortQ_Type())
qtechHQoSFlowMapAF1Q2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapAF1Q2PortQ.setStatus(_A)
class _QtechHQoSFlowMapAF2Q2PortQ_Type(QtechCosType):defaultValue=3
_QtechHQoSFlowMapAF2Q2PortQ_Type.__name__=_K
_QtechHQoSFlowMapAF2Q2PortQ_Object=MibTableColumn
qtechHQoSFlowMapAF2Q2PortQ=_QtechHQoSFlowMapAF2Q2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,6),_QtechHQoSFlowMapAF2Q2PortQ_Type())
qtechHQoSFlowMapAF2Q2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapAF2Q2PortQ.setStatus(_A)
class _QtechHQoSFlowMapAF3Q2PortQ_Type(QtechCosType):defaultValue=4
_QtechHQoSFlowMapAF3Q2PortQ_Type.__name__=_K
_QtechHQoSFlowMapAF3Q2PortQ_Object=MibTableColumn
qtechHQoSFlowMapAF3Q2PortQ=_QtechHQoSFlowMapAF3Q2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,7),_QtechHQoSFlowMapAF3Q2PortQ_Type())
qtechHQoSFlowMapAF3Q2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapAF3Q2PortQ.setStatus(_A)
class _QtechHQoSFlowMapAF4Q2PortQ_Type(QtechCosType):defaultValue=5
_QtechHQoSFlowMapAF4Q2PortQ_Type.__name__=_K
_QtechHQoSFlowMapAF4Q2PortQ_Object=MibTableColumn
qtechHQoSFlowMapAF4Q2PortQ=_QtechHQoSFlowMapAF4Q2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,8),_QtechHQoSFlowMapAF4Q2PortQ_Type())
qtechHQoSFlowMapAF4Q2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapAF4Q2PortQ.setStatus(_A)
class _QtechHQoSFlowMapEFQ2PortQ_Type(QtechCosType):defaultValue=6
_QtechHQoSFlowMapEFQ2PortQ_Type.__name__=_K
_QtechHQoSFlowMapEFQ2PortQ_Object=MibTableColumn
qtechHQoSFlowMapEFQ2PortQ=_QtechHQoSFlowMapEFQ2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,9),_QtechHQoSFlowMapEFQ2PortQ_Type())
qtechHQoSFlowMapEFQ2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapEFQ2PortQ.setStatus(_A)
class _QtechHQoSFlowMapCS6Q2PortQ_Type(QtechCosType):defaultValue=7
_QtechHQoSFlowMapCS6Q2PortQ_Type.__name__=_K
_QtechHQoSFlowMapCS6Q2PortQ_Object=MibTableColumn
qtechHQoSFlowMapCS6Q2PortQ=_QtechHQoSFlowMapCS6Q2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,10),_QtechHQoSFlowMapCS6Q2PortQ_Type())
qtechHQoSFlowMapCS6Q2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapCS6Q2PortQ.setStatus(_A)
class _QtechHQoSFlowMapCS7Q2PortQ_Type(QtechCosType):defaultValue=8
_QtechHQoSFlowMapCS7Q2PortQ_Type.__name__=_K
_QtechHQoSFlowMapCS7Q2PortQ_Object=MibTableColumn
qtechHQoSFlowMapCS7Q2PortQ=_QtechHQoSFlowMapCS7Q2PortQ_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,5,2,1,11),_QtechHQoSFlowMapCS7Q2PortQ_Type())
qtechHQoSFlowMapCS7Q2PortQ.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSFlowMapCS7Q2PortQ.setStatus(_A)
_QtechHQoSTClassifierObjects_ObjectIdentity=ObjectIdentity
qtechHQoSTClassifierObjects=_QtechHQoSTClassifierObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,6))
_QtechHQoSTClassifierIndexNext_Type=Integer32
_QtechHQoSTClassifierIndexNext_Object=MibScalar
qtechHQoSTClassifierIndexNext=_QtechHQoSTClassifierIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,1),_QtechHQoSTClassifierIndexNext_Type())
qtechHQoSTClassifierIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSTClassifierIndexNext.setStatus(_A)
_QtechHQoSTClassifierTable_Object=MibTable
qtechHQoSTClassifierTable=_QtechHQoSTClassifierTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2))
if mibBuilder.loadTexts:qtechHQoSTClassifierTable.setStatus(_A)
_QtechHQoSTClassifierEntry_Object=MibTableRow
qtechHQoSTClassifierEntry=_QtechHQoSTClassifierEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1))
qtechHQoSTClassifierEntry.setIndexNames((0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:qtechHQoSTClassifierEntry.setStatus(_A)
_QtechHQoSTClassifierIndex_Type=Unsigned32
_QtechHQoSTClassifierIndex_Object=MibTableColumn
qtechHQoSTClassifierIndex=_QtechHQoSTClassifierIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,1),_QtechHQoSTClassifierIndex_Type())
qtechHQoSTClassifierIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSTClassifierIndex.setStatus(_A)
_QtechHQoSTClassifierInstance_Type=Unsigned32
_QtechHQoSTClassifierInstance_Object=MibTableColumn
qtechHQoSTClassifierInstance=_QtechHQoSTClassifierInstance_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,2),_QtechHQoSTClassifierInstance_Type())
qtechHQoSTClassifierInstance.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSTClassifierInstance.setStatus(_A)
class _QtechHQoSTClassifierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTClassifierName_Type.__name__=_F
_QtechHQoSTClassifierName_Object=MibTableColumn
qtechHQoSTClassifierName=_QtechHQoSTClassifierName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,3),_QtechHQoSTClassifierName_Type())
qtechHQoSTClassifierName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierName.setStatus(_A)
class _QtechHQoSTClassifierType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tc-or',1),('tc-and',2)))
_QtechHQoSTClassifierType_Type.__name__=_D
_QtechHQoSTClassifierType_Object=MibTableColumn
qtechHQoSTClassifierType=_QtechHQoSTClassifierType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,4),_QtechHQoSTClassifierType_Type())
qtechHQoSTClassifierType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierType.setStatus(_A)
_QtechHQoSTClassifierRowStatus_Type=RowStatus
_QtechHQoSTClassifierRowStatus_Object=MibTableColumn
qtechHQoSTClassifierRowStatus=_QtechHQoSTClassifierRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,5),_QtechHQoSTClassifierRowStatus_Type())
qtechHQoSTClassifierRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierRowStatus.setStatus(_A)
class _QtechHQoSTClassifierMatchMask_Type(Bits):namedValues=NamedValues(*(('tc-v4-any',0),('tc-v4-aclID',1),('tc-v4-aclName',2),('tc-v4-dscp',3),('tc-v4-tos',4),('tc-v6-any',5),('tc-v6-aclID',6),('tc-v6-aclName',7),('tc-v6-dscp',8),('tc-vlan-cos',9),('tc-exp',10),('tc-srcmac',11),('tc-dstmac',12)))
_QtechHQoSTClassifierMatchMask_Type.__name__=_Y
_QtechHQoSTClassifierMatchMask_Object=MibTableColumn
qtechHQoSTClassifierMatchMask=_QtechHQoSTClassifierMatchMask_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,6),_QtechHQoSTClassifierMatchMask_Type())
qtechHQoSTClassifierMatchMask.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchMask.setStatus(_A)
class _QtechHQoSTClassifierMatchV4Any_Type(TruthValue):defaultValue=2
_QtechHQoSTClassifierMatchV4Any_Type.__name__=_O
_QtechHQoSTClassifierMatchV4Any_Object=MibTableColumn
qtechHQoSTClassifierMatchV4Any=_QtechHQoSTClassifierMatchV4Any_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,7),_QtechHQoSTClassifierMatchV4Any_Type())
qtechHQoSTClassifierMatchV4Any.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV4Any.setStatus(_A)
class _QtechHQoSTClassifierMatchV4AclID_Type(Integer32):defaultValue=0
_QtechHQoSTClassifierMatchV4AclID_Type.__name__=_D
_QtechHQoSTClassifierMatchV4AclID_Object=MibTableColumn
qtechHQoSTClassifierMatchV4AclID=_QtechHQoSTClassifierMatchV4AclID_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,8),_QtechHQoSTClassifierMatchV4AclID_Type())
qtechHQoSTClassifierMatchV4AclID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV4AclID.setStatus(_A)
class _QtechHQoSTClassifierV4AclName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTClassifierV4AclName_Type.__name__=_F
_QtechHQoSTClassifierV4AclName_Object=MibTableColumn
qtechHQoSTClassifierV4AclName=_QtechHQoSTClassifierV4AclName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,9),_QtechHQoSTClassifierV4AclName_Type())
qtechHQoSTClassifierV4AclName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierV4AclName.setStatus(_A)
class _QtechHQoSTClassifierMatchV4Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QtechHQoSTClassifierMatchV4Dscp_Type.__name__=_D
_QtechHQoSTClassifierMatchV4Dscp_Object=MibTableColumn
qtechHQoSTClassifierMatchV4Dscp=_QtechHQoSTClassifierMatchV4Dscp_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,10),_QtechHQoSTClassifierMatchV4Dscp_Type())
qtechHQoSTClassifierMatchV4Dscp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV4Dscp.setStatus(_A)
class _QtechHQoSTClassifierMatchV4Tos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechHQoSTClassifierMatchV4Tos_Type.__name__=_D
_QtechHQoSTClassifierMatchV4Tos_Object=MibTableColumn
qtechHQoSTClassifierMatchV4Tos=_QtechHQoSTClassifierMatchV4Tos_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,11),_QtechHQoSTClassifierMatchV4Tos_Type())
qtechHQoSTClassifierMatchV4Tos.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV4Tos.setStatus(_A)
class _QtechHQoSTClassifierMatchV6Any_Type(TruthValue):defaultValue=2
_QtechHQoSTClassifierMatchV6Any_Type.__name__=_O
_QtechHQoSTClassifierMatchV6Any_Object=MibTableColumn
qtechHQoSTClassifierMatchV6Any=_QtechHQoSTClassifierMatchV6Any_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,12),_QtechHQoSTClassifierMatchV6Any_Type())
qtechHQoSTClassifierMatchV6Any.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV6Any.setStatus(_A)
_QtechHQoSTClassifierMatchV6AclID_Type=Integer32
_QtechHQoSTClassifierMatchV6AclID_Object=MibTableColumn
qtechHQoSTClassifierMatchV6AclID=_QtechHQoSTClassifierMatchV6AclID_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,13),_QtechHQoSTClassifierMatchV6AclID_Type())
qtechHQoSTClassifierMatchV6AclID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV6AclID.setStatus(_A)
class _QtechHQoSTClassifierV6AclName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTClassifierV6AclName_Type.__name__=_F
_QtechHQoSTClassifierV6AclName_Object=MibTableColumn
qtechHQoSTClassifierV6AclName=_QtechHQoSTClassifierV6AclName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,14),_QtechHQoSTClassifierV6AclName_Type())
qtechHQoSTClassifierV6AclName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierV6AclName.setStatus(_A)
class _QtechHQoSTClassifierMatchV6Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechHQoSTClassifierMatchV6Dscp_Type.__name__=_D
_QtechHQoSTClassifierMatchV6Dscp_Object=MibTableColumn
qtechHQoSTClassifierMatchV6Dscp=_QtechHQoSTClassifierMatchV6Dscp_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,15),_QtechHQoSTClassifierMatchV6Dscp_Type())
qtechHQoSTClassifierMatchV6Dscp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchV6Dscp.setStatus(_A)
class _QtechHQoSTClassifierMatchCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechHQoSTClassifierMatchCos_Type.__name__=_D
_QtechHQoSTClassifierMatchCos_Object=MibTableColumn
qtechHQoSTClassifierMatchCos=_QtechHQoSTClassifierMatchCos_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,16),_QtechHQoSTClassifierMatchCos_Type())
qtechHQoSTClassifierMatchCos.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchCos.setStatus(_A)
class _QtechHQoSTClassifierMatchExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechHQoSTClassifierMatchExp_Type.__name__=_D
_QtechHQoSTClassifierMatchExp_Object=MibTableColumn
qtechHQoSTClassifierMatchExp=_QtechHQoSTClassifierMatchExp_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,17),_QtechHQoSTClassifierMatchExp_Type())
qtechHQoSTClassifierMatchExp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchExp.setStatus(_A)
_QtechHQoSTClassifierMatchSrcMac_Type=MacAddress
_QtechHQoSTClassifierMatchSrcMac_Object=MibTableColumn
qtechHQoSTClassifierMatchSrcMac=_QtechHQoSTClassifierMatchSrcMac_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,18),_QtechHQoSTClassifierMatchSrcMac_Type())
qtechHQoSTClassifierMatchSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchSrcMac.setStatus(_A)
_QtechHQoSTClassifierMatchDstMac_Type=MacAddress
_QtechHQoSTClassifierMatchDstMac_Object=MibTableColumn
qtechHQoSTClassifierMatchDstMac=_QtechHQoSTClassifierMatchDstMac_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,6,2,1,19),_QtechHQoSTClassifierMatchDstMac_Type())
qtechHQoSTClassifierMatchDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTClassifierMatchDstMac.setStatus(_A)
_QtechHQoSTBehaviorObjects_ObjectIdentity=ObjectIdentity
qtechHQoSTBehaviorObjects=_QtechHQoSTBehaviorObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,7))
_QtechHQoSTBehaviorIndexNext_Type=Integer32
_QtechHQoSTBehaviorIndexNext_Object=MibScalar
qtechHQoSTBehaviorIndexNext=_QtechHQoSTBehaviorIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,1),_QtechHQoSTBehaviorIndexNext_Type())
qtechHQoSTBehaviorIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSTBehaviorIndexNext.setStatus(_A)
_QtechHQoSTBehaviorTable_Object=MibTable
qtechHQoSTBehaviorTable=_QtechHQoSTBehaviorTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2))
if mibBuilder.loadTexts:qtechHQoSTBehaviorTable.setStatus(_A)
_QtechHQoSTBehaviorEntry_Object=MibTableRow
qtechHQoSTBehaviorEntry=_QtechHQoSTBehaviorEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1))
qtechHQoSTBehaviorEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:qtechHQoSTBehaviorEntry.setStatus(_A)
_QtechHQoSTBehaviorIndex_Type=Unsigned32
_QtechHQoSTBehaviorIndex_Object=MibTableColumn
qtechHQoSTBehaviorIndex=_QtechHQoSTBehaviorIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,1),_QtechHQoSTBehaviorIndex_Type())
qtechHQoSTBehaviorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSTBehaviorIndex.setStatus(_A)
class _QtechHQoSTBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTBehaviorName_Type.__name__=_F
_QtechHQoSTBehaviorName_Object=MibTableColumn
qtechHQoSTBehaviorName=_QtechHQoSTBehaviorName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,2),_QtechHQoSTBehaviorName_Type())
qtechHQoSTBehaviorName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorName.setStatus(_A)
_QtechHQoSTBehaviorRowStatus_Type=RowStatus
_QtechHQoSTBehaviorRowStatus_Object=MibTableColumn
qtechHQoSTBehaviorRowStatus=_QtechHQoSTBehaviorRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,3),_QtechHQoSTBehaviorRowStatus_Type())
qtechHQoSTBehaviorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorRowStatus.setStatus(_A)
class _QtechHQoSTBehaviorMask_Type(Bits):namedValues=NamedValues(*(('user-queue',0),('set-cos',1),('set-color',2),('remark-v4-dscp',3),('remark-v4-tos',4),('remark-v6-dscp',5),('remark-vlan-cos',6),('remark-exp',7),('sub-policy',8)))
_QtechHQoSTBehaviorMask_Type.__name__=_Y
_QtechHQoSTBehaviorMask_Object=MibTableColumn
qtechHQoSTBehaviorMask=_QtechHQoSTBehaviorMask_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,4),_QtechHQoSTBehaviorMask_Type())
qtechHQoSTBehaviorMask.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorMask.setStatus(_A)
class _QtechHQoSTBehaviorUserQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTBehaviorUserQName_Type.__name__=_F
_QtechHQoSTBehaviorUserQName_Object=MibTableColumn
qtechHQoSTBehaviorUserQName=_QtechHQoSTBehaviorUserQName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,5),_QtechHQoSTBehaviorUserQName_Type())
qtechHQoSTBehaviorUserQName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorUserQName.setStatus(_A)
class _QtechHQoSTBehaviorTCos_Type(QtechCosType):defaultValue=1
_QtechHQoSTBehaviorTCos_Type.__name__=_K
_QtechHQoSTBehaviorTCos_Object=MibTableColumn
qtechHQoSTBehaviorTCos=_QtechHQoSTBehaviorTCos_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,6),_QtechHQoSTBehaviorTCos_Type())
qtechHQoSTBehaviorTCos.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorTCos.setStatus(_A)
class _QtechHQoSTBehaviorTColor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3)))
_QtechHQoSTBehaviorTColor_Type.__name__=_D
_QtechHQoSTBehaviorTColor_Object=MibTableColumn
qtechHQoSTBehaviorTColor=_QtechHQoSTBehaviorTColor_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,7),_QtechHQoSTBehaviorTColor_Type())
qtechHQoSTBehaviorTColor.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorTColor.setStatus(_A)
class _QtechHQoSTBehaviorRV4Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QtechHQoSTBehaviorRV4Dscp_Type.__name__=_D
_QtechHQoSTBehaviorRV4Dscp_Object=MibTableColumn
qtechHQoSTBehaviorRV4Dscp=_QtechHQoSTBehaviorRV4Dscp_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,8),_QtechHQoSTBehaviorRV4Dscp_Type())
qtechHQoSTBehaviorRV4Dscp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorRV4Dscp.setStatus(_A)
class _QtechHQoSTBehaviorRV4Tos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechHQoSTBehaviorRV4Tos_Type.__name__=_D
_QtechHQoSTBehaviorRV4Tos_Object=MibTableColumn
qtechHQoSTBehaviorRV4Tos=_QtechHQoSTBehaviorRV4Tos_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,9),_QtechHQoSTBehaviorRV4Tos_Type())
qtechHQoSTBehaviorRV4Tos.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorRV4Tos.setStatus(_A)
class _QtechHQoSTBehaviorRV6Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechHQoSTBehaviorRV6Dscp_Type.__name__=_D
_QtechHQoSTBehaviorRV6Dscp_Object=MibTableColumn
qtechHQoSTBehaviorRV6Dscp=_QtechHQoSTBehaviorRV6Dscp_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,10),_QtechHQoSTBehaviorRV6Dscp_Type())
qtechHQoSTBehaviorRV6Dscp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorRV6Dscp.setStatus(_A)
class _QtechHQoSTBehaviorRVlanCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechHQoSTBehaviorRVlanCos_Type.__name__=_D
_QtechHQoSTBehaviorRVlanCos_Object=MibTableColumn
qtechHQoSTBehaviorRVlanCos=_QtechHQoSTBehaviorRVlanCos_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,11),_QtechHQoSTBehaviorRVlanCos_Type())
qtechHQoSTBehaviorRVlanCos.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorRVlanCos.setStatus(_A)
class _QtechHQoSTBehaviorRExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechHQoSTBehaviorRExp_Type.__name__=_D
_QtechHQoSTBehaviorRExp_Object=MibTableColumn
qtechHQoSTBehaviorRExp=_QtechHQoSTBehaviorRExp_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,12),_QtechHQoSTBehaviorRExp_Type())
qtechHQoSTBehaviorRExp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorRExp.setStatus(_A)
class _QtechHQoSTBehaviorSubPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTBehaviorSubPolicyName_Type.__name__=_F
_QtechHQoSTBehaviorSubPolicyName_Object=MibTableColumn
qtechHQoSTBehaviorSubPolicyName=_QtechHQoSTBehaviorSubPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,7,2,1,13),_QtechHQoSTBehaviorSubPolicyName_Type())
qtechHQoSTBehaviorSubPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTBehaviorSubPolicyName.setStatus(_A)
_QtechHQoSTPolicyObjects_ObjectIdentity=ObjectIdentity
qtechHQoSTPolicyObjects=_QtechHQoSTPolicyObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,8))
_QtechHQoSTPolicyIndexNext_Type=Integer32
_QtechHQoSTPolicyIndexNext_Object=MibScalar
qtechHQoSTPolicyIndexNext=_QtechHQoSTPolicyIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,1),_QtechHQoSTPolicyIndexNext_Type())
qtechHQoSTPolicyIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSTPolicyIndexNext.setStatus(_A)
_QtechHQoSTPolicyTable_Object=MibTable
qtechHQoSTPolicyTable=_QtechHQoSTPolicyTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,2))
if mibBuilder.loadTexts:qtechHQoSTPolicyTable.setStatus(_A)
_QtechHQoSTPolicyEntry_Object=MibTableRow
qtechHQoSTPolicyEntry=_QtechHQoSTPolicyEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,2,1))
qtechHQoSTPolicyEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:qtechHQoSTPolicyEntry.setStatus(_A)
_QtechHQoSTPolicyIndex_Type=Unsigned32
_QtechHQoSTPolicyIndex_Object=MibTableColumn
qtechHQoSTPolicyIndex=_QtechHQoSTPolicyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,2,1,1),_QtechHQoSTPolicyIndex_Type())
qtechHQoSTPolicyIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSTPolicyIndex.setStatus(_A)
class _QtechHQoSTPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTPolicyName_Type.__name__=_F
_QtechHQoSTPolicyName_Object=MibTableColumn
qtechHQoSTPolicyName=_QtechHQoSTPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,2,1,2),_QtechHQoSTPolicyName_Type())
qtechHQoSTPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyName.setStatus(_A)
_QtechHQoSTPolicyRowStatus_Type=RowStatus
_QtechHQoSTPolicyRowStatus_Object=MibTableColumn
qtechHQoSTPolicyRowStatus=_QtechHQoSTPolicyRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,2,1,3),_QtechHQoSTPolicyRowStatus_Type())
qtechHQoSTPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyRowStatus.setStatus(_A)
_QtechHQoSTPolicyMapIndexNext_Type=Integer32
_QtechHQoSTPolicyMapIndexNext_Object=MibScalar
qtechHQoSTPolicyMapIndexNext=_QtechHQoSTPolicyMapIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,3),_QtechHQoSTPolicyMapIndexNext_Type())
qtechHQoSTPolicyMapIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapIndexNext.setStatus(_A)
_QtechHQoSTPolicyMapTable_Object=MibTable
qtechHQoSTPolicyMapTable=_QtechHQoSTPolicyMapTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4))
if mibBuilder.loadTexts:qtechHQoSTPolicyMapTable.setStatus(_A)
_QtechHQoSTPolicyMapEntry_Object=MibTableRow
qtechHQoSTPolicyMapEntry=_QtechHQoSTPolicyMapEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1))
qtechHQoSTPolicyMapEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:qtechHQoSTPolicyMapEntry.setStatus(_A)
_QtechHQoSTPolicyMapIndex_Type=Unsigned32
_QtechHQoSTPolicyMapIndex_Object=MibTableColumn
qtechHQoSTPolicyMapIndex=_QtechHQoSTPolicyMapIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,1),_QtechHQoSTPolicyMapIndex_Type())
qtechHQoSTPolicyMapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapIndex.setStatus(_A)
class _QtechHQoSTPolicyMapPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTPolicyMapPolicyName_Type.__name__=_F
_QtechHQoSTPolicyMapPolicyName_Object=MibTableColumn
qtechHQoSTPolicyMapPolicyName=_QtechHQoSTPolicyMapPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,2),_QtechHQoSTPolicyMapPolicyName_Type())
qtechHQoSTPolicyMapPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapPolicyName.setStatus(_A)
_QtechHQoSTPolicyMapPolicyIndex_Type=Unsigned32
_QtechHQoSTPolicyMapPolicyIndex_Object=MibTableColumn
qtechHQoSTPolicyMapPolicyIndex=_QtechHQoSTPolicyMapPolicyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,3),_QtechHQoSTPolicyMapPolicyIndex_Type())
qtechHQoSTPolicyMapPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapPolicyIndex.setStatus(_A)
class _QtechHQoSTPolicyMapTClassfierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTPolicyMapTClassfierName_Type.__name__=_F
_QtechHQoSTPolicyMapTClassfierName_Object=MibTableColumn
qtechHQoSTPolicyMapTClassfierName=_QtechHQoSTPolicyMapTClassfierName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,4),_QtechHQoSTPolicyMapTClassfierName_Type())
qtechHQoSTPolicyMapTClassfierName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapTClassfierName.setStatus(_A)
_QtechHQoSTPolicyMapTClassfierIndex_Type=Unsigned32
_QtechHQoSTPolicyMapTClassfierIndex_Object=MibTableColumn
qtechHQoSTPolicyMapTClassfierIndex=_QtechHQoSTPolicyMapTClassfierIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,5),_QtechHQoSTPolicyMapTClassfierIndex_Type())
qtechHQoSTPolicyMapTClassfierIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapTClassfierIndex.setStatus(_A)
class _QtechHQoSTPolicyMapTBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSTPolicyMapTBehaviorName_Type.__name__=_F
_QtechHQoSTPolicyMapTBehaviorName_Object=MibTableColumn
qtechHQoSTPolicyMapTBehaviorName=_QtechHQoSTPolicyMapTBehaviorName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,6),_QtechHQoSTPolicyMapTBehaviorName_Type())
qtechHQoSTPolicyMapTBehaviorName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapTBehaviorName.setStatus(_A)
_QtechHQoSTPolicyMapTBehaviorIndex_Type=Unsigned32
_QtechHQoSTPolicyMapTBehaviorIndex_Object=MibTableColumn
qtechHQoSTPolicyMapTBehaviorIndex=_QtechHQoSTPolicyMapTBehaviorIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,7),_QtechHQoSTPolicyMapTBehaviorIndex_Type())
qtechHQoSTPolicyMapTBehaviorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapTBehaviorIndex.setStatus(_A)
class _QtechHQoSTPolicyMapPrecedence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_QtechHQoSTPolicyMapPrecedence_Type.__name__=_M
_QtechHQoSTPolicyMapPrecedence_Object=MibTableColumn
qtechHQoSTPolicyMapPrecedence=_QtechHQoSTPolicyMapPrecedence_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,8),_QtechHQoSTPolicyMapPrecedence_Type())
qtechHQoSTPolicyMapPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapPrecedence.setStatus(_A)
_QtechHQoSTPolicyMapRowStatus_Type=RowStatus
_QtechHQoSTPolicyMapRowStatus_Object=MibTableColumn
qtechHQoSTPolicyMapRowStatus=_QtechHQoSTPolicyMapRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,8,4,1,9),_QtechHQoSTPolicyMapRowStatus_Type())
qtechHQoSTPolicyMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSTPolicyMapRowStatus.setStatus(_A)
_QtechHQoSVoQObjects_ObjectIdentity=ObjectIdentity
qtechHQoSVoQObjects=_QtechHQoSVoQObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,9))
class _QtechHQoSVoQEnable_Type(TruthValue):defaultValue=2
_QtechHQoSVoQEnable_Type.__name__=_O
_QtechHQoSVoQEnable_Object=MibScalar
qtechHQoSVoQEnable=_QtechHQoSVoQEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,9,1),_QtechHQoSVoQEnable_Type())
qtechHQoSVoQEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSVoQEnable.setStatus(_A)
_QtechHQoSVoQDeviceTable_Object=MibTable
qtechHQoSVoQDeviceTable=_QtechHQoSVoQDeviceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,9,2))
if mibBuilder.loadTexts:qtechHQoSVoQDeviceTable.setStatus(_A)
_QtechHQoSVoQDeviceEntry_Object=MibTableRow
qtechHQoSVoQDeviceEntry=_QtechHQoSVoQDeviceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,9,2,1))
qtechHQoSVoQDeviceEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:qtechHQoSVoQDeviceEntry.setStatus(_A)
_QtechHQoSVoQDeviceId_Type=Unsigned32
_QtechHQoSVoQDeviceId_Object=MibTableColumn
qtechHQoSVoQDeviceId=_QtechHQoSVoQDeviceId_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,9,2,1,1),_QtechHQoSVoQDeviceId_Type())
qtechHQoSVoQDeviceId.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSVoQDeviceId.setStatus(_A)
_QtechHQoSVoQDeviceCredit_Type=Unsigned32
_QtechHQoSVoQDeviceCredit_Object=MibTableColumn
qtechHQoSVoQDeviceCredit=_QtechHQoSVoQDeviceCredit_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,9,2,1,2),_QtechHQoSVoQDeviceCredit_Type())
qtechHQoSVoQDeviceCredit.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSVoQDeviceCredit.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSVoQDeviceCredit.setUnits('Mbit/s')
_QtechHQoSPortQObjects_ObjectIdentity=ObjectIdentity
qtechHQoSPortQObjects=_QtechHQoSPortQObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,10))
_QtechHQoSPortQIndexNext_Type=Integer32
_QtechHQoSPortQIndexNext_Object=MibScalar
qtechHQoSPortQIndexNext=_QtechHQoSPortQIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,1),_QtechHQoSPortQIndexNext_Type())
qtechHQoSPortQIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSPortQIndexNext.setStatus(_A)
_QtechHQoSPortQTable_Object=MibTable
qtechHQoSPortQTable=_QtechHQoSPortQTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2))
if mibBuilder.loadTexts:qtechHQoSPortQTable.setStatus(_A)
_QtechHQoSPortQEntry_Object=MibTableRow
qtechHQoSPortQEntry=_QtechHQoSPortQEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1))
qtechHQoSPortQEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:qtechHQoSPortQEntry.setStatus(_A)
_QtechHQoSPortQIndex_Type=Unsigned32
_QtechHQoSPortQIndex_Object=MibTableColumn
qtechHQoSPortQIndex=_QtechHQoSPortQIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,1),_QtechHQoSPortQIndex_Type())
qtechHQoSPortQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSPortQIndex.setStatus(_A)
class _QtechHQoSPortQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQName_Type.__name__=_F
_QtechHQoSPortQName_Object=MibTableColumn
qtechHQoSPortQName=_QtechHQoSPortQName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,2),_QtechHQoSPortQName_Type())
qtechHQoSPortQName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQName.setStatus(_A)
_QtechHQoSPortQRowStatus_Type=RowStatus
_QtechHQoSPortQRowStatus_Object=MibTableColumn
qtechHQoSPortQRowStatus=_QtechHQoSPortQRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,3),_QtechHQoSPortQRowStatus_Type())
qtechHQoSPortQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQRowStatus.setStatus(_A)
class _QtechHQoSPortQBEQType_Type(QtechQType):defaultValue=2
_QtechHQoSPortQBEQType_Type.__name__=_H
_QtechHQoSPortQBEQType_Object=MibTableColumn
qtechHQoSPortQBEQType=_QtechHQoSPortQBEQType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,4),_QtechHQoSPortQBEQType_Type())
qtechHQoSPortQBEQType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQBEQType.setStatus(_A)
class _QtechHQoSPortQBEQWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQBEQWredWeight_Type.__name__=_D
_QtechHQoSPortQBEQWredWeight_Object=MibTableColumn
qtechHQoSPortQBEQWredWeight=_QtechHQoSPortQBEQWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,5),_QtechHQoSPortQBEQWredWeight_Type())
qtechHQoSPortQBEQWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQBEQWredWeight.setStatus(_A)
class _QtechHQoSPortQBEQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQBEQWredName_Type.__name__=_F
_QtechHQoSPortQBEQWredName_Object=MibTableColumn
qtechHQoSPortQBEQWredName=_QtechHQoSPortQBEQWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,6),_QtechHQoSPortQBEQWredName_Type())
qtechHQoSPortQBEQWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQBEQWredName.setStatus(_A)
class _QtechHQoSPortQBEQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQBEQDepth_Type.__name__=_D
_QtechHQoSPortQBEQDepth_Object=MibTableColumn
qtechHQoSPortQBEQDepth=_QtechHQoSPortQBEQDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,7),_QtechHQoSPortQBEQDepth_Type())
qtechHQoSPortQBEQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQBEQDepth.setStatus(_A)
class _QtechHQoSPortQBEQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQBEQShaping_Type.__name__=_D
_QtechHQoSPortQBEQShaping_Object=MibTableColumn
qtechHQoSPortQBEQShaping=_QtechHQoSPortQBEQShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,8),_QtechHQoSPortQBEQShaping_Type())
qtechHQoSPortQBEQShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQBEQShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQBEQShaping.setUnits(_G)
class _QtechHQoSPortQAF1QType_Type(QtechQType):defaultValue=2
_QtechHQoSPortQAF1QType_Type.__name__=_H
_QtechHQoSPortQAF1QType_Object=MibTableColumn
qtechHQoSPortQAF1QType=_QtechHQoSPortQAF1QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,9),_QtechHQoSPortQAF1QType_Type())
qtechHQoSPortQAF1QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF1QType.setStatus(_A)
class _QtechHQoSPortQAF1QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQAF1QWredWeight_Type.__name__=_D
_QtechHQoSPortQAF1QWredWeight_Object=MibTableColumn
qtechHQoSPortQAF1QWredWeight=_QtechHQoSPortQAF1QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,10),_QtechHQoSPortQAF1QWredWeight_Type())
qtechHQoSPortQAF1QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF1QWredWeight.setStatus(_A)
class _QtechHQoSPortQAF1QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQAF1QWredName_Type.__name__=_F
_QtechHQoSPortQAF1QWredName_Object=MibTableColumn
qtechHQoSPortQAF1QWredName=_QtechHQoSPortQAF1QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,11),_QtechHQoSPortQAF1QWredName_Type())
qtechHQoSPortQAF1QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF1QWredName.setStatus(_A)
class _QtechHQoSPortQAF1QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQAF1QDepth_Type.__name__=_D
_QtechHQoSPortQAF1QDepth_Object=MibTableColumn
qtechHQoSPortQAF1QDepth=_QtechHQoSPortQAF1QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,12),_QtechHQoSPortQAF1QDepth_Type())
qtechHQoSPortQAF1QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF1QDepth.setStatus(_A)
class _QtechHQoSPortQAF1QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQAF1QShaping_Type.__name__=_D
_QtechHQoSPortQAF1QShaping_Object=MibTableColumn
qtechHQoSPortQAF1QShaping=_QtechHQoSPortQAF1QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,13),_QtechHQoSPortQAF1QShaping_Type())
qtechHQoSPortQAF1QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF1QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQAF1QShaping.setUnits(_G)
class _QtechHQoSPortQAF2QType_Type(QtechQType):defaultValue=2
_QtechHQoSPortQAF2QType_Type.__name__=_H
_QtechHQoSPortQAF2QType_Object=MibTableColumn
qtechHQoSPortQAF2QType=_QtechHQoSPortQAF2QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,14),_QtechHQoSPortQAF2QType_Type())
qtechHQoSPortQAF2QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF2QType.setStatus(_A)
class _QtechHQoSPortQAF2QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_QtechHQoSPortQAF2QWredWeight_Type.__name__=_D
_QtechHQoSPortQAF2QWredWeight_Object=MibTableColumn
qtechHQoSPortQAF2QWredWeight=_QtechHQoSPortQAF2QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,15),_QtechHQoSPortQAF2QWredWeight_Type())
qtechHQoSPortQAF2QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF2QWredWeight.setStatus(_A)
class _QtechHQoSPortQAF2QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQAF2QWredName_Type.__name__=_F
_QtechHQoSPortQAF2QWredName_Object=MibTableColumn
qtechHQoSPortQAF2QWredName=_QtechHQoSPortQAF2QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,16),_QtechHQoSPortQAF2QWredName_Type())
qtechHQoSPortQAF2QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF2QWredName.setStatus(_A)
class _QtechHQoSPortQAF2QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQAF2QDepth_Type.__name__=_D
_QtechHQoSPortQAF2QDepth_Object=MibTableColumn
qtechHQoSPortQAF2QDepth=_QtechHQoSPortQAF2QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,17),_QtechHQoSPortQAF2QDepth_Type())
qtechHQoSPortQAF2QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF2QDepth.setStatus(_A)
class _QtechHQoSPortQAF2QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQAF2QShaping_Type.__name__=_D
_QtechHQoSPortQAF2QShaping_Object=MibTableColumn
qtechHQoSPortQAF2QShaping=_QtechHQoSPortQAF2QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,18),_QtechHQoSPortQAF2QShaping_Type())
qtechHQoSPortQAF2QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF2QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQAF2QShaping.setUnits(_G)
class _QtechHQoSPortQAF3QType_Type(QtechQType):defaultValue=2
_QtechHQoSPortQAF3QType_Type.__name__=_H
_QtechHQoSPortQAF3QType_Object=MibTableColumn
qtechHQoSPortQAF3QType=_QtechHQoSPortQAF3QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,19),_QtechHQoSPortQAF3QType_Type())
qtechHQoSPortQAF3QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF3QType.setStatus(_A)
class _QtechHQoSPortQAF3QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQAF3QWredWeight_Type.__name__=_D
_QtechHQoSPortQAF3QWredWeight_Object=MibTableColumn
qtechHQoSPortQAF3QWredWeight=_QtechHQoSPortQAF3QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,20),_QtechHQoSPortQAF3QWredWeight_Type())
qtechHQoSPortQAF3QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF3QWredWeight.setStatus(_A)
class _QtechHQoSPortQAF3QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQAF3QWredName_Type.__name__=_F
_QtechHQoSPortQAF3QWredName_Object=MibTableColumn
qtechHQoSPortQAF3QWredName=_QtechHQoSPortQAF3QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,21),_QtechHQoSPortQAF3QWredName_Type())
qtechHQoSPortQAF3QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF3QWredName.setStatus(_A)
class _QtechHQoSPortQAF3QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQAF3QDepth_Type.__name__=_D
_QtechHQoSPortQAF3QDepth_Object=MibTableColumn
qtechHQoSPortQAF3QDepth=_QtechHQoSPortQAF3QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,22),_QtechHQoSPortQAF3QDepth_Type())
qtechHQoSPortQAF3QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF3QDepth.setStatus(_A)
class _QtechHQoSPortQAF3QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQAF3QShaping_Type.__name__=_D
_QtechHQoSPortQAF3QShaping_Object=MibTableColumn
qtechHQoSPortQAF3QShaping=_QtechHQoSPortQAF3QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,23),_QtechHQoSPortQAF3QShaping_Type())
qtechHQoSPortQAF3QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF3QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQAF3QShaping.setUnits(_G)
class _QtechHQoSPortQAF4QType_Type(QtechQType):defaultValue=2
_QtechHQoSPortQAF4QType_Type.__name__=_H
_QtechHQoSPortQAF4QType_Object=MibTableColumn
qtechHQoSPortQAF4QType=_QtechHQoSPortQAF4QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,24),_QtechHQoSPortQAF4QType_Type())
qtechHQoSPortQAF4QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF4QType.setStatus(_A)
class _QtechHQoSPortQAF4QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQAF4QWredWeight_Type.__name__=_D
_QtechHQoSPortQAF4QWredWeight_Object=MibTableColumn
qtechHQoSPortQAF4QWredWeight=_QtechHQoSPortQAF4QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,25),_QtechHQoSPortQAF4QWredWeight_Type())
qtechHQoSPortQAF4QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF4QWredWeight.setStatus(_A)
class _QtechHQoSPortQAF4QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQAF4QWredName_Type.__name__=_F
_QtechHQoSPortQAF4QWredName_Object=MibTableColumn
qtechHQoSPortQAF4QWredName=_QtechHQoSPortQAF4QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,26),_QtechHQoSPortQAF4QWredName_Type())
qtechHQoSPortQAF4QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF4QWredName.setStatus(_A)
class _QtechHQoSPortQAF4QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQAF4QDepth_Type.__name__=_D
_QtechHQoSPortQAF4QDepth_Object=MibTableColumn
qtechHQoSPortQAF4QDepth=_QtechHQoSPortQAF4QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,27),_QtechHQoSPortQAF4QDepth_Type())
qtechHQoSPortQAF4QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF4QDepth.setStatus(_A)
class _QtechHQoSPortQAF4QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQAF4QShaping_Type.__name__=_D
_QtechHQoSPortQAF4QShaping_Object=MibTableColumn
qtechHQoSPortQAF4QShaping=_QtechHQoSPortQAF4QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,28),_QtechHQoSPortQAF4QShaping_Type())
qtechHQoSPortQAF4QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQAF4QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQAF4QShaping.setUnits(_G)
class _QtechHQoSPortQEFQType_Type(QtechQType):defaultValue=3
_QtechHQoSPortQEFQType_Type.__name__=_H
_QtechHQoSPortQEFQType_Object=MibTableColumn
qtechHQoSPortQEFQType=_QtechHQoSPortQEFQType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,29),_QtechHQoSPortQEFQType_Type())
qtechHQoSPortQEFQType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQEFQType.setStatus(_A)
class _QtechHQoSPortQEFQWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQEFQWredWeight_Type.__name__=_D
_QtechHQoSPortQEFQWredWeight_Object=MibTableColumn
qtechHQoSPortQEFQWredWeight=_QtechHQoSPortQEFQWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,30),_QtechHQoSPortQEFQWredWeight_Type())
qtechHQoSPortQEFQWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQEFQWredWeight.setStatus(_A)
class _QtechHQoSPortQEFQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQEFQWredName_Type.__name__=_F
_QtechHQoSPortQEFQWredName_Object=MibTableColumn
qtechHQoSPortQEFQWredName=_QtechHQoSPortQEFQWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,31),_QtechHQoSPortQEFQWredName_Type())
qtechHQoSPortQEFQWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQEFQWredName.setStatus(_A)
class _QtechHQoSPortQEFQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQEFQDepth_Type.__name__=_D
_QtechHQoSPortQEFQDepth_Object=MibTableColumn
qtechHQoSPortQEFQDepth=_QtechHQoSPortQEFQDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,32),_QtechHQoSPortQEFQDepth_Type())
qtechHQoSPortQEFQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQEFQDepth.setStatus(_A)
class _QtechHQoSPortQEFQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQEFQShaping_Type.__name__=_D
_QtechHQoSPortQEFQShaping_Object=MibTableColumn
qtechHQoSPortQEFQShaping=_QtechHQoSPortQEFQShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,33),_QtechHQoSPortQEFQShaping_Type())
qtechHQoSPortQEFQShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQEFQShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQEFQShaping.setUnits(_G)
class _QtechHQoSPortQCS6QType_Type(QtechQType):defaultValue=3
_QtechHQoSPortQCS6QType_Type.__name__=_H
_QtechHQoSPortQCS6QType_Object=MibTableColumn
qtechHQoSPortQCS6QType=_QtechHQoSPortQCS6QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,34),_QtechHQoSPortQCS6QType_Type())
qtechHQoSPortQCS6QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS6QType.setStatus(_A)
class _QtechHQoSPortQCS6QWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQCS6QWredWeight_Type.__name__=_D
_QtechHQoSPortQCS6QWredWeight_Object=MibTableColumn
qtechHQoSPortQCS6QWredWeight=_QtechHQoSPortQCS6QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,35),_QtechHQoSPortQCS6QWredWeight_Type())
qtechHQoSPortQCS6QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS6QWredWeight.setStatus(_A)
class _QtechHQoSPortQCS6QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQCS6QWredName_Type.__name__=_F
_QtechHQoSPortQCS6QWredName_Object=MibTableColumn
qtechHQoSPortQCS6QWredName=_QtechHQoSPortQCS6QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,36),_QtechHQoSPortQCS6QWredName_Type())
qtechHQoSPortQCS6QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS6QWredName.setStatus(_A)
class _QtechHQoSPortQCS6QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQCS6QDepth_Type.__name__=_D
_QtechHQoSPortQCS6QDepth_Object=MibTableColumn
qtechHQoSPortQCS6QDepth=_QtechHQoSPortQCS6QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,37),_QtechHQoSPortQCS6QDepth_Type())
qtechHQoSPortQCS6QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS6QDepth.setStatus(_A)
class _QtechHQoSPortQCS6QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQCS6QShaping_Type.__name__=_D
_QtechHQoSPortQCS6QShaping_Object=MibTableColumn
qtechHQoSPortQCS6QShaping=_QtechHQoSPortQCS6QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,38),_QtechHQoSPortQCS6QShaping_Type())
qtechHQoSPortQCS6QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS6QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQCS6QShaping.setUnits(_G)
class _QtechHQoSPortQCS7QType_Type(QtechQType):defaultValue=3
_QtechHQoSPortQCS7QType_Type.__name__=_H
_QtechHQoSPortQCS7QType_Object=MibTableColumn
qtechHQoSPortQCS7QType=_QtechHQoSPortQCS7QType_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,39),_QtechHQoSPortQCS7QType_Type())
qtechHQoSPortQCS7QType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS7QType.setStatus(_A)
class _QtechHQoSPortQCS7QWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_QtechHQoSPortQCS7QWredWeight_Type.__name__=_D
_QtechHQoSPortQCS7QWredWeight_Object=MibTableColumn
qtechHQoSPortQCS7QWredWeight=_QtechHQoSPortQCS7QWredWeight_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,40),_QtechHQoSPortQCS7QWredWeight_Type())
qtechHQoSPortQCS7QWredWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS7QWredWeight.setStatus(_A)
class _QtechHQoSPortQCS7QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSPortQCS7QWredName_Type.__name__=_F
_QtechHQoSPortQCS7QWredName_Object=MibTableColumn
qtechHQoSPortQCS7QWredName=_QtechHQoSPortQCS7QWredName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,41),_QtechHQoSPortQCS7QWredName_Type())
qtechHQoSPortQCS7QWredName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS7QWredName.setStatus(_A)
class _QtechHQoSPortQCS7QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QtechHQoSPortQCS7QDepth_Type.__name__=_D
_QtechHQoSPortQCS7QDepth_Object=MibTableColumn
qtechHQoSPortQCS7QDepth=_QtechHQoSPortQCS7QDepth_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,42),_QtechHQoSPortQCS7QDepth_Type())
qtechHQoSPortQCS7QDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS7QDepth.setStatus(_A)
class _QtechHQoSPortQCS7QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSPortQCS7QShaping_Type.__name__=_D
_QtechHQoSPortQCS7QShaping_Object=MibTableColumn
qtechHQoSPortQCS7QShaping=_QtechHQoSPortQCS7QShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,10,2,1,43),_QtechHQoSPortQCS7QShaping_Type())
qtechHQoSPortQCS7QShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHQoSPortQCS7QShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSPortQCS7QShaping.setUnits(_G)
_QtechHQoSIfAppObjects_ObjectIdentity=ObjectIdentity
qtechHQoSIfAppObjects=_QtechHQoSIfAppObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,106,3,11))
_QtechHQoSIfAppTable_Object=MibTable
qtechHQoSIfAppTable=_QtechHQoSIfAppTable_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1))
if mibBuilder.loadTexts:qtechHQoSIfAppTable.setStatus(_A)
_QtechHQoSIfAppEntry_Object=MibTableRow
qtechHQoSIfAppEntry=_QtechHQoSIfAppEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1))
qtechHQoSIfAppEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:qtechHQoSIfAppEntry.setStatus(_A)
_QtechHQoSIfAppIndex_Type=InterfaceIndex
_QtechHQoSIfAppIndex_Object=MibTableColumn
qtechHQoSIfAppIndex=_QtechHQoSIfAppIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,1),_QtechHQoSIfAppIndex_Type())
qtechHQoSIfAppIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechHQoSIfAppIndex.setStatus(_A)
class _QtechHQoSIfAppInPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSIfAppInPolicyName_Type.__name__=_F
_QtechHQoSIfAppInPolicyName_Object=MibTableColumn
qtechHQoSIfAppInPolicyName=_QtechHQoSIfAppInPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,2),_QtechHQoSIfAppInPolicyName_Type())
qtechHQoSIfAppInPolicyName.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSIfAppInPolicyName.setStatus(_A)
_QtechHQoSIfAppInPolicyIndex_Type=Unsigned32
_QtechHQoSIfAppInPolicyIndex_Object=MibTableColumn
qtechHQoSIfAppInPolicyIndex=_QtechHQoSIfAppInPolicyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,3),_QtechHQoSIfAppInPolicyIndex_Type())
qtechHQoSIfAppInPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSIfAppInPolicyIndex.setStatus(_A)
class _QtechHQoSIfAppInPolicyLayer_Type(QtechLayerType):defaultValue=2
_QtechHQoSIfAppInPolicyLayer_Type.__name__=_Z
_QtechHQoSIfAppInPolicyLayer_Object=MibTableColumn
qtechHQoSIfAppInPolicyLayer=_QtechHQoSIfAppInPolicyLayer_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,4),_QtechHQoSIfAppInPolicyLayer_Type())
qtechHQoSIfAppInPolicyLayer.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSIfAppInPolicyLayer.setStatus(_A)
class _QtechHQoSIfAppOutPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSIfAppOutPolicyName_Type.__name__=_F
_QtechHQoSIfAppOutPolicyName_Object=MibTableColumn
qtechHQoSIfAppOutPolicyName=_QtechHQoSIfAppOutPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,5),_QtechHQoSIfAppOutPolicyName_Type())
qtechHQoSIfAppOutPolicyName.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSIfAppOutPolicyName.setStatus(_A)
_QtechHQoSIfAppOutPolicyIndex_Type=Unsigned32
_QtechHQoSIfAppOutPolicyIndex_Object=MibTableColumn
qtechHQoSIfAppOutPolicyIndex=_QtechHQoSIfAppOutPolicyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,6),_QtechHQoSIfAppOutPolicyIndex_Type())
qtechHQoSIfAppOutPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSIfAppOutPolicyIndex.setStatus(_A)
class _QtechHQoSIfAppOutPolicyLayer_Type(QtechLayerType):defaultValue=2
_QtechHQoSIfAppOutPolicyLayer_Type.__name__=_Z
_QtechHQoSIfAppOutPolicyLayer_Object=MibTableColumn
qtechHQoSIfAppOutPolicyLayer=_QtechHQoSIfAppOutPolicyLayer_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,7),_QtechHQoSIfAppOutPolicyLayer_Type())
qtechHQoSIfAppOutPolicyLayer.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSIfAppOutPolicyLayer.setStatus(_A)
class _QtechHQoSIfAppPortQueueName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechHQoSIfAppPortQueueName_Type.__name__=_F
_QtechHQoSIfAppPortQueueName_Object=MibTableColumn
qtechHQoSIfAppPortQueueName=_QtechHQoSIfAppPortQueueName_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,8),_QtechHQoSIfAppPortQueueName_Type())
qtechHQoSIfAppPortQueueName.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSIfAppPortQueueName.setStatus(_A)
_QtechHQoSIfAppPortQueueIndex_Type=Unsigned32
_QtechHQoSIfAppPortQueueIndex_Object=MibTableColumn
qtechHQoSIfAppPortQueueIndex=_QtechHQoSIfAppPortQueueIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,9),_QtechHQoSIfAppPortQueueIndex_Type())
qtechHQoSIfAppPortQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHQoSIfAppPortQueueIndex.setStatus(_A)
class _QtechHQoSIfAppPortQueueShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_QtechHQoSIfAppPortQueueShaping_Type.__name__=_D
_QtechHQoSIfAppPortQueueShaping_Object=MibTableColumn
qtechHQoSIfAppPortQueueShaping=_QtechHQoSIfAppPortQueueShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,106,3,11,1,1,10),_QtechHQoSIfAppPortQueueShaping_Type())
qtechHQoSIfAppPortQueueShaping.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechHQoSIfAppPortQueueShaping.setStatus(_A)
if mibBuilder.loadTexts:qtechHQoSIfAppPortQueueShaping.setUnits(_G)
mibBuilder.exportSymbols(_E,**{_K:QtechCosType,_H:QtechQType,'QtechQDirectionType':QtechQDirectionType,_Z:QtechLayerType,'qtechRouterQoSMIB':qtechRouterQoSMIB,'qtechCBQoSMIBObjects':qtechCBQoSMIBObjects,'qtechCBQoSIfStaticsObjects':qtechCBQoSIfStaticsObjects,'qtechCBQoSIfCbwfqRunInfoTable':qtechCBQoSIfCbwfqRunInfoTable,'qtechCBQoSIfCbwfqRunInfoEntry':qtechCBQoSIfCbwfqRunInfoEntry,_a:qtechCBQoSIfCbwfqPolicyIfIndex,'qtechCBQoSIfCbwfqQueueSize':qtechCBQoSIfCbwfqQueueSize,'qtechCBQoSIfCbwfqDiscard':qtechCBQoSIfCbwfqDiscard,'qtechCBQoSIfCbwfqEfQueueSize':qtechCBQoSIfCbwfqEfQueueSize,'qtechCBQoSIfCbwfqAfQueueSize':qtechCBQoSIfCbwfqAfQueueSize,'qtechCBQoSIfCbwfqBeQueueSize':qtechCBQoSIfCbwfqBeQueueSize,'qtechCBQoSIfCbwfqBeActiveQueueNum':qtechCBQoSIfCbwfqBeActiveQueueNum,'qtechCBQoSIfCbwfqBeMaxActiveQueueNum':qtechCBQoSIfCbwfqBeMaxActiveQueueNum,'qtechCBQoSIfCbwfqBeTotalQueueNum':qtechCBQoSIfCbwfqBeTotalQueueNum,'qtechCBQoSIfCbwfqAfAllocatedQueueNum':qtechCBQoSIfCbwfqAfAllocatedQueueNum,'qtechCBQoSIfClassMatchRunInfoTable':qtechCBQoSIfClassMatchRunInfoTable,'qtechCBQoSIfClassMatchRunInfoEntry':qtechCBQoSIfClassMatchRunInfoEntry,_b:qtechCBQoSIfClassMatchIfIndex,_c:qtechCBQoSIfClassMatchPolicyDirection,_d:qtechCBQoSIfClassMatchClassIndex,'qtechCBQoSIfClassMatchedPackets':qtechCBQoSIfClassMatchedPackets,'qtechCBQoSIfClassMatchedBytes':qtechCBQoSIfClassMatchedBytes,'qtechCBQosIfClassPassedPackets':qtechCBQosIfClassPassedPackets,'qtechCBQosIfClassDroppedPackets':qtechCBQosIfClassDroppedPackets,'qtechCBQoSIfCarRunInfoTable':qtechCBQoSIfCarRunInfoTable,'qtechCBQoSIfCarRunInfoEntry':qtechCBQoSIfCarRunInfoEntry,_e:qtechCBQoSIfCarIfIndex,_f:qtechCBQoSIfCarPolicyDirection,_g:qtechCBQoSIfCarClassIndex,'qtechCBQoSIfCarConformedPackets':qtechCBQoSIfCarConformedPackets,'qtechCBQoSIfCarConformedBytes':qtechCBQoSIfCarConformedBytes,'qtechCBQoSIfCarExceededPackets':qtechCBQoSIfCarExceededPackets,'qtechCBQoSIfCarExceededBytes':qtechCBQoSIfCarExceededBytes,'qtechCBQoSIfCarViolatedPackets':qtechCBQoSIfCarViolatedPackets,'qtechCBQoSIfCarViolatedBytes':qtechCBQoSIfCarViolatedBytes,'qtechCBQoSIfRemarkRunInfoTable':qtechCBQoSIfRemarkRunInfoTable,'qtechCBQoSIfRemarkRunInfoEntry':qtechCBQoSIfRemarkRunInfoEntry,_h:qtechCBQoSIfRemarkIfIndex,_i:qtechCBQoSIfRemarkPolicyDirection,_j:qtechCBQoSIfRemarkClassIndex,'qtechCBQoSIfRemarkedPackets':qtechCBQoSIfRemarkedPackets,'qtechCBQoSIfRemarkedBytes':qtechCBQoSIfRemarkedBytes,'qtechCBQoSIfQueueRunInfoTable':qtechCBQoSIfQueueRunInfoTable,'qtechCBQoSIfQueueRunInfoEntry':qtechCBQoSIfQueueRunInfoEntry,_k:qtechCBQoSIfQueueIfIndex,_l:qtechCBQoSIfQueuePolicyDirection,_m:qtechCBQoSIfQueueClassIndex,'qtechCBQoSIfQueueMatchedPackets':qtechCBQoSIfQueueMatchedPackets,'qtechCBQoSIfQueueMatchedBytes':qtechCBQoSIfQueueMatchedBytes,'qtechCBQoSIfQueueEnqueuedPackets':qtechCBQoSIfQueueEnqueuedPackets,'qtechCBQoSIfQueueEnqueuedBytes':qtechCBQoSIfQueueEnqueuedBytes,'qtechCBQoSIfQueueDiscardedPackets':qtechCBQoSIfQueueDiscardedPackets,'qtechCBQoSIfQueueDiscardedBytes':qtechCBQoSIfQueueDiscardedBytes,'qtechCBQoSIfWredRunInfoTable':qtechCBQoSIfWredRunInfoTable,'qtechCBQoSIfWredRunInfoEntry':qtechCBQoSIfWredRunInfoEntry,_n:qtechCBQoSIfWredIfIndex,_o:qtechCBQoSIfWredClassIndex,_p:qtechCBQoSIfWredClassValue,'qtechCBQoSIfWredRandomDiscardedPackets':qtechCBQoSIfWredRandomDiscardedPackets,'qtechCBQoSIfWredTailDiscardedPackets':qtechCBQoSIfWredTailDiscardedPackets,'qtechIfQoSMIBObjects':qtechIfQoSMIBObjects,'qtechIfQosPQRunInfoTable':qtechIfQosPQRunInfoTable,'qtechIfQosPQRunInfoEntry':qtechIfQosPQRunInfoEntry,_q:qtechIfQosPQIfIndex,'qtechIfQosPQListNum':qtechIfQosPQListNum,'qtechIfQosPQIfName':qtechIfQosPQIfName,'qtechIfQosPQHighPkt':qtechIfQosPQHighPkt,'qtechIfQosPQHighDiscard':qtechIfQosPQHighDiscard,'qtechIfQosPQHighMaxQueLen':qtechIfQosPQHighMaxQueLen,'qtechIfQosPQMiddlePkt':qtechIfQosPQMiddlePkt,'qtechIfQosPQMiddleDiscard':qtechIfQosPQMiddleDiscard,'qtechIfQosPQMiddleMaxQueLen':qtechIfQosPQMiddleMaxQueLen,'qtechIfQosPQNormalPkt':qtechIfQosPQNormalPkt,'qtechIfQosPQNormalDiscard':qtechIfQosPQNormalDiscard,'qtechIfQosPQNormalMaxQueLen':qtechIfQosPQNormalMaxQueLen,'qtechIfQosPQLowPkt':qtechIfQosPQLowPkt,'qtechIfQosPQLowDiscard':qtechIfQosPQLowDiscard,'qtechIfQosPQLowMaxQueLen':qtechIfQosPQLowMaxQueLen,'qtechIfQosCQRunInfoTable':qtechIfQosCQRunInfoTable,'qtechIfQosCQRunInfoEntry':qtechIfQosCQRunInfoEntry,_r:qtechIfQosCQRunInfoIfIndex,_s:qtechIfQosCQRunInfoQueNum,'qtechIfQosCQRunInfoIfName':qtechIfQosCQRunInfoIfName,'qtechIfQosCQRunInfoQuePkt':qtechIfQosCQRunInfoQuePkt,'qtechIfQosCQRunInfoQueDiscard':qtechIfQosCQRunInfoQueDiscard,'qtechIfQosCQRunInfoMaxQueLen':qtechIfQosCQRunInfoMaxQueLen,'qtechIfQosWFQRunInfoTable':qtechIfQosWFQRunInfoTable,'qtechIfQosWFQRunInfoEntry':qtechIfQosWFQRunInfoEntry,_t:qtechIfQosWFQIfIndex,'qtechIfQosWFQIfName':qtechIfQosWFQIfName,'qtechIfQosWFQMaxQueLen':qtechIfQosWFQMaxQueLen,'qtechIfQosWFQTotalQueNum':qtechIfQosWFQTotalQueNum,'qtechIfQosWFQCurQueLen':qtechIfQosWFQCurQueLen,'qtechIfQosWFQTotalDiscard':qtechIfQosWFQTotalDiscard,'qtechIfQosWFQActiveQueNum':qtechIfQosWFQActiveQueNum,'qtechIfQosWFQMaxActiveQueNum':qtechIfQosWFQMaxActiveQueNum,'qtechIfQosWredRunInfoTable':qtechIfQosWredRunInfoTable,'qtechIfQosWredRunInfoEntry':qtechIfQosWredRunInfoEntry,_u:qtechIfQosWredIfIndex,_v:qtechIfQosWredValue,'qtechIfQosWredRandomDiscardedPackets':qtechIfQosWredRandomDiscardedPackets,'qtechIfQosWredTailDiscardedPackets':qtechIfQosWredTailDiscardedPackets,'qtechIfQosCARTable':qtechIfQosCARTable,'qtechIfQosCAREntry':qtechIfQosCAREntry,_w:qtechIfQosCARIfIndex,'qtechIfQosCARIfName':qtechIfQosCARIfName,_x:qtechIfQosCARPktDirection,'qtechIfQosCARType':qtechIfQosCARType,'qtechIfQosCARListNum':qtechIfQosCARListNum,_y:qtechIfQosCARindex,'qtechIfQosCARCIR':qtechIfQosCARCIR,'qtechIfQosCARBurstSize':qtechIfQosCARBurstSize,'qtechIfQosCARExcessBurstSize':qtechIfQosCARExcessBurstSize,'qtechIfQosCARConformAction':qtechIfQosCARConformAction,'qtechIfQosCARExceedAction':qtechIfQosCARExceedAction,'qtechIfQosCARConformNewPrec':qtechIfQosCARConformNewPrec,'qtechIfQosCARExceedNewPrec':qtechIfQosCARExceedNewPrec,'qtechIfQosCARConformPkt':qtechIfQosCARConformPkt,'qtechIfQosCARConformByte':qtechIfQosCARConformByte,'qtechIfQosCARExceedPkt':qtechIfQosCARExceedPkt,'qtechIfQosCARExceedByte':qtechIfQosCARExceedByte,'qtechIfQosGTSTable':qtechIfQosGTSTable,'qtechIfQosGTSEntry':qtechIfQosGTSEntry,_z:qtechIfQosGTSIfIndex,'qtechIfQosGTSIfName':qtechIfQosGTSIfName,_A0:qtechIfQosGTSType,_A1:qtechIfQosGTSACLNum,'qtechIfQosGTSCIR':qtechIfQosGTSCIR,'qtechIfQosGTSBurstSize':qtechIfQosGTSBurstSize,'qtechIfQosGTSExcessBurstSize':qtechIfQosGTSExcessBurstSize,'qtechIfQosGTSMaxQueLen':qtechIfQosGTSMaxQueLen,'qtechIfQosGTSCurQueLen':qtechIfQosGTSCurQueLen,'qtechIfQosGTSPassPkt':qtechIfQosGTSPassPkt,'qtechIfQosGTSPassByte':qtechIfQosGTSPassByte,'qtechIfQosGTSDiscardPkt':qtechIfQosGTSDiscardPkt,'qtechIfQosGTSDiscardByte':qtechIfQosGTSDiscardByte,'qtechIfQosRTPIfQueueRunInfoTable':qtechIfQosRTPIfQueueRunInfoTable,'qtechIfQosRTPIfQueueRunInfoEntry':qtechIfQosRTPIfQueueRunInfoEntry,_A2:qtechIfQosRTPIfApplyIfIndex,'qtechIfQosRTPIfQueueSize':qtechIfQosRTPIfQueueSize,'qtechIfQosRTPIfQueueMaxSize':qtechIfQosRTPIfQueueMaxSize,'qtechIfQosRTPIfQueueOutputs':qtechIfQosRTPIfQueueOutputs,'qtechIfQosRTPIfQueueDiscards':qtechIfQosRTPIfQueueDiscards,'qtechIfQosFlowLimitRunInfoTable':qtechIfQosFlowLimitRunInfoTable,'qtechIfQosFlowLimitRunInfoEntry':qtechIfQosFlowLimitRunInfoEntry,_A3:qtechIfQosFlowLimitLabelNum,_A4:qtechIfQosFlowLimitPktDirection,'qtechIfQosFlowLimitCIR':qtechIfQosFlowLimitCIR,'qtechIfQosFlowLimitBurstSize':qtechIfQosFlowLimitBurstSize,'qtechIfQosFlowLimitExcessBurstSize':qtechIfQosFlowLimitExcessBurstSize,'qtechIfQosFlowLimitConformAction':qtechIfQosFlowLimitConformAction,'qtechIfQosFlowLimitExceedAction':qtechIfQosFlowLimitExceedAction,'qtechIfQosFlowLimitConformNewPrec':qtechIfQosFlowLimitConformNewPrec,'qtechIfQosFlowLimitExceedNewPrec':qtechIfQosFlowLimitExceedNewPrec,'qtechIfQosFlowLimitConformPkt':qtechIfQosFlowLimitConformPkt,'qtechIfQosFlowLimitConformByte':qtechIfQosFlowLimitConformByte,'qtechIfQosFlowLimitExceedPkt':qtechIfQosFlowLimitExceedPkt,'qtechIfQosFlowLimitExceedByte':qtechIfQosFlowLimitExceedByte,'qtechHQoSMIBObjects':qtechHQoSMIBObjects,'qtechHQoSScalarObjects':qtechHQoSScalarObjects,'qtechHQoSNameType':qtechHQoSNameType,'qtechHQoSNameFind':qtechHQoSNameFind,'qtechHQoSNameIndex':qtechHQoSNameIndex,'qtechHQoSUserQObjects':qtechHQoSUserQObjects,'qtechHQoSUserQInIndexNext':qtechHQoSUserQInIndexNext,'qtechHQoSUserQOutIndexNext':qtechHQoSUserQOutIndexNext,'qtechHQoSUserQTable':qtechHQoSUserQTable,'qtechHQoSUserQEntry':qtechHQoSUserQEntry,_A5:qtechHQoSUserQIndex,'qtechHQoSUserQName':qtechHQoSUserQName,'qtechHQoSUserQDirection':qtechHQoSUserQDirection,'qtechHQoSUserQRowStatus':qtechHQoSUserQRowStatus,'qtechHQoSUserQFlowQName':qtechHQoSUserQFlowQName,'qtechHQoSUserQFlowQIndex':qtechHQoSUserQFlowQIndex,'qtechHQoSUserQGroupName':qtechHQoSUserQGroupName,'qtechHQoSUserQGroupIndex':qtechHQoSUserQGroupIndex,'qtechHQoSUserQFlowMapName':qtechHQoSUserQFlowMapName,'qtechHQoSUserQFlowMapIndex':qtechHQoSUserQFlowMapIndex,'qtechHQoSUserQCIR':qtechHQoSUserQCIR,'qtechHQoSUserQPIR':qtechHQoSUserQPIR,'qtechHQoSUserGroupQObjects':qtechHQoSUserGroupQObjects,'qtechHQoSUserGroupQInIndexNext':qtechHQoSUserGroupQInIndexNext,'qtechHQoSUserGroupQOutIndexNext':qtechHQoSUserGroupQOutIndexNext,'qtechHQoSUserGroupQTable':qtechHQoSUserGroupQTable,'qtechHQoSUserGroupQEntry':qtechHQoSUserGroupQEntry,_A6:qtechHQoSUserGroupQIndex,'qtechHQoSUserGroupQName':qtechHQoSUserGroupQName,'qtechHQoSUserGroupQDirection':qtechHQoSUserGroupQDirection,'qtechHQoSUserGroupQRowStatus':qtechHQoSUserGroupQRowStatus,'qtechHQoSUserGroupQShaping':qtechHQoSUserGroupQShaping,'qtechHQoSFlowQObjects':qtechHQoSFlowQObjects,'qtechHQoSFlowQIndexNext':qtechHQoSFlowQIndexNext,'qtechHQoSFlowQTable':qtechHQoSFlowQTable,'qtechHQoSFlowQEntry':qtechHQoSFlowQEntry,_A7:qtechHQoSFlowQIndex,'qtechHQoSFlowQName':qtechHQoSFlowQName,'qtechHQoSFlowQRowStatus':qtechHQoSFlowQRowStatus,'qtechHQoSFlowQBEQType':qtechHQoSFlowQBEQType,'qtechHQoSFlowQBEQWredWeight':qtechHQoSFlowQBEQWredWeight,'qtechHQoSFlowQBEQWredName':qtechHQoSFlowQBEQWredName,'qtechHQoSFlowQBEQDepth':qtechHQoSFlowQBEQDepth,'qtechHQoSFlowQBEQShaping':qtechHQoSFlowQBEQShaping,'qtechHQoSFlowQAF1QType':qtechHQoSFlowQAF1QType,'qtechHQoSFlowQAF1QWredWeight':qtechHQoSFlowQAF1QWredWeight,'qtechHQoSFlowQAF1QWredName':qtechHQoSFlowQAF1QWredName,'qtechHQoSFlowQAF1QDepth':qtechHQoSFlowQAF1QDepth,'qtechHQoSFlowQAF1QShaping':qtechHQoSFlowQAF1QShaping,'qtechHQoSFlowQAF2QType':qtechHQoSFlowQAF2QType,'qtechHQoSFlowQAF2QWredWeight':qtechHQoSFlowQAF2QWredWeight,'qtechHQoSFlowQAF2QWredName':qtechHQoSFlowQAF2QWredName,'qtechHQoSFlowQAF2QDepth':qtechHQoSFlowQAF2QDepth,'qtechHQoSFlowQAF2QShaping':qtechHQoSFlowQAF2QShaping,'qtechHQoSFlowQAF3QType':qtechHQoSFlowQAF3QType,'qtechHQoSFlowQAF3QWredWeight':qtechHQoSFlowQAF3QWredWeight,'qtechHQoSFlowQAF3QWredName':qtechHQoSFlowQAF3QWredName,'qtechHQoSFlowQAF3QDepth':qtechHQoSFlowQAF3QDepth,'qtechHQoSFlowQAF3QShaping':qtechHQoSFlowQAF3QShaping,'qtechHQoSFlowQAF4QType':qtechHQoSFlowQAF4QType,'qtechHQoSFlowQAF4QWredWeight':qtechHQoSFlowQAF4QWredWeight,'qtechHQoSFlowQAF4QWredName':qtechHQoSFlowQAF4QWredName,'qtechHQoSFlowQAF4QDepth':qtechHQoSFlowQAF4QDepth,'qtechHQoSFlowQAF4QShaping':qtechHQoSFlowQAF4QShaping,'qtechHQoSFlowQEFQType':qtechHQoSFlowQEFQType,'qtechHQoSFlowQEFQWredWeight':qtechHQoSFlowQEFQWredWeight,'qtechHQoSFlowQEFQWredName':qtechHQoSFlowQEFQWredName,'qtechHQoSFlowQEFQDepth':qtechHQoSFlowQEFQDepth,'qtechHQoSFlowQEFQShaping':qtechHQoSFlowQEFQShaping,'qtechHQoSFlowQCS6QType':qtechHQoSFlowQCS6QType,'qtechHQoSFlowQCS6QWredWeight':qtechHQoSFlowQCS6QWredWeight,'qtechHQoSFlowQCS6QWredName':qtechHQoSFlowQCS6QWredName,'qtechHQoSFlowQCS6QDepth':qtechHQoSFlowQCS6QDepth,'qtechHQoSFlowQCS6QShaping':qtechHQoSFlowQCS6QShaping,'qtechHQoSFlowQCS7QType':qtechHQoSFlowQCS7QType,'qtechHQoSFlowQCS7QWredWeight':qtechHQoSFlowQCS7QWredWeight,'qtechHQoSFlowQCS7QWredName':qtechHQoSFlowQCS7QWredName,'qtechHQoSFlowQCS7QDepth':qtechHQoSFlowQCS7QDepth,'qtechHQoSFlowQCS7QShaping':qtechHQoSFlowQCS7QShaping,'qtechHQoSFlowMapObjects':qtechHQoSFlowMapObjects,'qtechHQoSFlowMapIndexNext':qtechHQoSFlowMapIndexNext,'qtechHQoSFlowMapTable':qtechHQoSFlowMapTable,'qtechHQoSFlowMapEntry':qtechHQoSFlowMapEntry,_A8:qtechHQoSFlowMapIndex,'qtechHQoSFlowMapName':qtechHQoSFlowMapName,'qtechHQoSFlowMapRowStatus':qtechHQoSFlowMapRowStatus,'qtechHQoSFlowMapBEQ2PortQ':qtechHQoSFlowMapBEQ2PortQ,'qtechHQoSFlowMapAF1Q2PortQ':qtechHQoSFlowMapAF1Q2PortQ,'qtechHQoSFlowMapAF2Q2PortQ':qtechHQoSFlowMapAF2Q2PortQ,'qtechHQoSFlowMapAF3Q2PortQ':qtechHQoSFlowMapAF3Q2PortQ,'qtechHQoSFlowMapAF4Q2PortQ':qtechHQoSFlowMapAF4Q2PortQ,'qtechHQoSFlowMapEFQ2PortQ':qtechHQoSFlowMapEFQ2PortQ,'qtechHQoSFlowMapCS6Q2PortQ':qtechHQoSFlowMapCS6Q2PortQ,'qtechHQoSFlowMapCS7Q2PortQ':qtechHQoSFlowMapCS7Q2PortQ,'qtechHQoSTClassifierObjects':qtechHQoSTClassifierObjects,'qtechHQoSTClassifierIndexNext':qtechHQoSTClassifierIndexNext,'qtechHQoSTClassifierTable':qtechHQoSTClassifierTable,'qtechHQoSTClassifierEntry':qtechHQoSTClassifierEntry,_A9:qtechHQoSTClassifierIndex,_AA:qtechHQoSTClassifierInstance,'qtechHQoSTClassifierName':qtechHQoSTClassifierName,'qtechHQoSTClassifierType':qtechHQoSTClassifierType,'qtechHQoSTClassifierRowStatus':qtechHQoSTClassifierRowStatus,'qtechHQoSTClassifierMatchMask':qtechHQoSTClassifierMatchMask,'qtechHQoSTClassifierMatchV4Any':qtechHQoSTClassifierMatchV4Any,'qtechHQoSTClassifierMatchV4AclID':qtechHQoSTClassifierMatchV4AclID,'qtechHQoSTClassifierV4AclName':qtechHQoSTClassifierV4AclName,'qtechHQoSTClassifierMatchV4Dscp':qtechHQoSTClassifierMatchV4Dscp,'qtechHQoSTClassifierMatchV4Tos':qtechHQoSTClassifierMatchV4Tos,'qtechHQoSTClassifierMatchV6Any':qtechHQoSTClassifierMatchV6Any,'qtechHQoSTClassifierMatchV6AclID':qtechHQoSTClassifierMatchV6AclID,'qtechHQoSTClassifierV6AclName':qtechHQoSTClassifierV6AclName,'qtechHQoSTClassifierMatchV6Dscp':qtechHQoSTClassifierMatchV6Dscp,'qtechHQoSTClassifierMatchCos':qtechHQoSTClassifierMatchCos,'qtechHQoSTClassifierMatchExp':qtechHQoSTClassifierMatchExp,'qtechHQoSTClassifierMatchSrcMac':qtechHQoSTClassifierMatchSrcMac,'qtechHQoSTClassifierMatchDstMac':qtechHQoSTClassifierMatchDstMac,'qtechHQoSTBehaviorObjects':qtechHQoSTBehaviorObjects,'qtechHQoSTBehaviorIndexNext':qtechHQoSTBehaviorIndexNext,'qtechHQoSTBehaviorTable':qtechHQoSTBehaviorTable,'qtechHQoSTBehaviorEntry':qtechHQoSTBehaviorEntry,_AB:qtechHQoSTBehaviorIndex,'qtechHQoSTBehaviorName':qtechHQoSTBehaviorName,'qtechHQoSTBehaviorRowStatus':qtechHQoSTBehaviorRowStatus,'qtechHQoSTBehaviorMask':qtechHQoSTBehaviorMask,'qtechHQoSTBehaviorUserQName':qtechHQoSTBehaviorUserQName,'qtechHQoSTBehaviorTCos':qtechHQoSTBehaviorTCos,'qtechHQoSTBehaviorTColor':qtechHQoSTBehaviorTColor,'qtechHQoSTBehaviorRV4Dscp':qtechHQoSTBehaviorRV4Dscp,'qtechHQoSTBehaviorRV4Tos':qtechHQoSTBehaviorRV4Tos,'qtechHQoSTBehaviorRV6Dscp':qtechHQoSTBehaviorRV6Dscp,'qtechHQoSTBehaviorRVlanCos':qtechHQoSTBehaviorRVlanCos,'qtechHQoSTBehaviorRExp':qtechHQoSTBehaviorRExp,'qtechHQoSTBehaviorSubPolicyName':qtechHQoSTBehaviorSubPolicyName,'qtechHQoSTPolicyObjects':qtechHQoSTPolicyObjects,'qtechHQoSTPolicyIndexNext':qtechHQoSTPolicyIndexNext,'qtechHQoSTPolicyTable':qtechHQoSTPolicyTable,'qtechHQoSTPolicyEntry':qtechHQoSTPolicyEntry,_AC:qtechHQoSTPolicyIndex,'qtechHQoSTPolicyName':qtechHQoSTPolicyName,'qtechHQoSTPolicyRowStatus':qtechHQoSTPolicyRowStatus,'qtechHQoSTPolicyMapIndexNext':qtechHQoSTPolicyMapIndexNext,'qtechHQoSTPolicyMapTable':qtechHQoSTPolicyMapTable,'qtechHQoSTPolicyMapEntry':qtechHQoSTPolicyMapEntry,_AD:qtechHQoSTPolicyMapIndex,'qtechHQoSTPolicyMapPolicyName':qtechHQoSTPolicyMapPolicyName,'qtechHQoSTPolicyMapPolicyIndex':qtechHQoSTPolicyMapPolicyIndex,'qtechHQoSTPolicyMapTClassfierName':qtechHQoSTPolicyMapTClassfierName,'qtechHQoSTPolicyMapTClassfierIndex':qtechHQoSTPolicyMapTClassfierIndex,'qtechHQoSTPolicyMapTBehaviorName':qtechHQoSTPolicyMapTBehaviorName,'qtechHQoSTPolicyMapTBehaviorIndex':qtechHQoSTPolicyMapTBehaviorIndex,'qtechHQoSTPolicyMapPrecedence':qtechHQoSTPolicyMapPrecedence,'qtechHQoSTPolicyMapRowStatus':qtechHQoSTPolicyMapRowStatus,'qtechHQoSVoQObjects':qtechHQoSVoQObjects,'qtechHQoSVoQEnable':qtechHQoSVoQEnable,'qtechHQoSVoQDeviceTable':qtechHQoSVoQDeviceTable,'qtechHQoSVoQDeviceEntry':qtechHQoSVoQDeviceEntry,_AE:qtechHQoSVoQDeviceId,'qtechHQoSVoQDeviceCredit':qtechHQoSVoQDeviceCredit,'qtechHQoSPortQObjects':qtechHQoSPortQObjects,'qtechHQoSPortQIndexNext':qtechHQoSPortQIndexNext,'qtechHQoSPortQTable':qtechHQoSPortQTable,'qtechHQoSPortQEntry':qtechHQoSPortQEntry,_AF:qtechHQoSPortQIndex,'qtechHQoSPortQName':qtechHQoSPortQName,'qtechHQoSPortQRowStatus':qtechHQoSPortQRowStatus,'qtechHQoSPortQBEQType':qtechHQoSPortQBEQType,'qtechHQoSPortQBEQWredWeight':qtechHQoSPortQBEQWredWeight,'qtechHQoSPortQBEQWredName':qtechHQoSPortQBEQWredName,'qtechHQoSPortQBEQDepth':qtechHQoSPortQBEQDepth,'qtechHQoSPortQBEQShaping':qtechHQoSPortQBEQShaping,'qtechHQoSPortQAF1QType':qtechHQoSPortQAF1QType,'qtechHQoSPortQAF1QWredWeight':qtechHQoSPortQAF1QWredWeight,'qtechHQoSPortQAF1QWredName':qtechHQoSPortQAF1QWredName,'qtechHQoSPortQAF1QDepth':qtechHQoSPortQAF1QDepth,'qtechHQoSPortQAF1QShaping':qtechHQoSPortQAF1QShaping,'qtechHQoSPortQAF2QType':qtechHQoSPortQAF2QType,'qtechHQoSPortQAF2QWredWeight':qtechHQoSPortQAF2QWredWeight,'qtechHQoSPortQAF2QWredName':qtechHQoSPortQAF2QWredName,'qtechHQoSPortQAF2QDepth':qtechHQoSPortQAF2QDepth,'qtechHQoSPortQAF2QShaping':qtechHQoSPortQAF2QShaping,'qtechHQoSPortQAF3QType':qtechHQoSPortQAF3QType,'qtechHQoSPortQAF3QWredWeight':qtechHQoSPortQAF3QWredWeight,'qtechHQoSPortQAF3QWredName':qtechHQoSPortQAF3QWredName,'qtechHQoSPortQAF3QDepth':qtechHQoSPortQAF3QDepth,'qtechHQoSPortQAF3QShaping':qtechHQoSPortQAF3QShaping,'qtechHQoSPortQAF4QType':qtechHQoSPortQAF4QType,'qtechHQoSPortQAF4QWredWeight':qtechHQoSPortQAF4QWredWeight,'qtechHQoSPortQAF4QWredName':qtechHQoSPortQAF4QWredName,'qtechHQoSPortQAF4QDepth':qtechHQoSPortQAF4QDepth,'qtechHQoSPortQAF4QShaping':qtechHQoSPortQAF4QShaping,'qtechHQoSPortQEFQType':qtechHQoSPortQEFQType,'qtechHQoSPortQEFQWredWeight':qtechHQoSPortQEFQWredWeight,'qtechHQoSPortQEFQWredName':qtechHQoSPortQEFQWredName,'qtechHQoSPortQEFQDepth':qtechHQoSPortQEFQDepth,'qtechHQoSPortQEFQShaping':qtechHQoSPortQEFQShaping,'qtechHQoSPortQCS6QType':qtechHQoSPortQCS6QType,'qtechHQoSPortQCS6QWredWeight':qtechHQoSPortQCS6QWredWeight,'qtechHQoSPortQCS6QWredName':qtechHQoSPortQCS6QWredName,'qtechHQoSPortQCS6QDepth':qtechHQoSPortQCS6QDepth,'qtechHQoSPortQCS6QShaping':qtechHQoSPortQCS6QShaping,'qtechHQoSPortQCS7QType':qtechHQoSPortQCS7QType,'qtechHQoSPortQCS7QWredWeight':qtechHQoSPortQCS7QWredWeight,'qtechHQoSPortQCS7QWredName':qtechHQoSPortQCS7QWredName,'qtechHQoSPortQCS7QDepth':qtechHQoSPortQCS7QDepth,'qtechHQoSPortQCS7QShaping':qtechHQoSPortQCS7QShaping,'qtechHQoSIfAppObjects':qtechHQoSIfAppObjects,'qtechHQoSIfAppTable':qtechHQoSIfAppTable,'qtechHQoSIfAppEntry':qtechHQoSIfAppEntry,_AG:qtechHQoSIfAppIndex,'qtechHQoSIfAppInPolicyName':qtechHQoSIfAppInPolicyName,'qtechHQoSIfAppInPolicyIndex':qtechHQoSIfAppInPolicyIndex,'qtechHQoSIfAppInPolicyLayer':qtechHQoSIfAppInPolicyLayer,'qtechHQoSIfAppOutPolicyName':qtechHQoSIfAppOutPolicyName,'qtechHQoSIfAppOutPolicyIndex':qtechHQoSIfAppOutPolicyIndex,'qtechHQoSIfAppOutPolicyLayer':qtechHQoSIfAppOutPolicyLayer,'qtechHQoSIfAppPortQueueName':qtechHQoSIfAppPortQueueName,'qtechHQoSIfAppPortQueueIndex':qtechHQoSIfAppPortQueueIndex,'qtechHQoSIfAppPortQueueShaping':qtechHQoSIfAppPortQueueShaping})