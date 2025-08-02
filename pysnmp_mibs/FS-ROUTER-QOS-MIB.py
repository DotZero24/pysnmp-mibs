_AG='fsHQoSIfAppIndex'
_AF='fsHQoSPortQIndex'
_AE='fsHQoSVoQDeviceId'
_AD='fsHQoSTPolicyMapIndex'
_AC='fsHQoSTPolicyIndex'
_AB='fsHQoSTBehaviorIndex'
_AA='fsHQoSTClassifierInstance'
_A9='fsHQoSTClassifierIndex'
_A8='fsHQoSFlowMapIndex'
_A7='fsHQoSFlowQIndex'
_A6='fsHQoSUserGroupQIndex'
_A5='fsHQoSUserQIndex'
_A4='fsIfQosFlowLimitPktDirection'
_A3='fsIfQosFlowLimitLabelNum'
_A2='fsIfQosRTPIfApplyIfIndex'
_A1='fsIfQosGTSACLNum'
_A0='fsIfQosGTSType'
_z='fsIfQosGTSIfIndex'
_y='fsIfQosCARindex'
_x='fsIfQosCARPktDirection'
_w='fsIfQosCARIfIndex'
_v='fsIfQosWredValue'
_u='fsIfQosWredIfIndex'
_t='fsIfQosWFQIfIndex'
_s='fsIfQosCQRunInfoQueNum'
_r='fsIfQosCQRunInfoIfIndex'
_q='fsIfQosPQIfIndex'
_p='fsCBQoSIfWredClassValue'
_o='fsCBQoSIfWredClassIndex'
_n='fsCBQoSIfWredIfIndex'
_m='fsCBQoSIfQueueClassIndex'
_l='fsCBQoSIfQueuePolicyDirection'
_k='fsCBQoSIfQueueIfIndex'
_j='fsCBQoSIfRemarkClassIndex'
_i='fsCBQoSIfRemarkPolicyDirection'
_h='fsCBQoSIfRemarkIfIndex'
_g='fsCBQoSIfCarClassIndex'
_f='fsCBQoSIfCarPolicyDirection'
_e='fsCBQoSIfCarIfIndex'
_d='fsCBQoSIfClassMatchClassIndex'
_c='fsCBQoSIfClassMatchPolicyDirection'
_b='fsCBQoSIfClassMatchIfIndex'
_a='fsCBQoSIfCbwfqPolicyIfIndex'
_Z='FSLayerType'
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
_K='FSCosType'
_J='read-write'
_I='not-accessible'
_H='FSQType'
_G='kilobits per second'
_F='OctetString'
_E='FS-ROUTER-QOS-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Y,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_O)
fsRouterQoSMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,106))
if mibBuilder.loadTexts:fsRouterQoSMIB.setRevisions(('2011-12-20 00:00',))
class FSCosType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cos-be',1),('cos-af1',2),('cos-af2',3),('cos-af3',4),('cos-af4',5),('cos-ef',6),('cos-cs6',7),('cos-cs7',8)))
class FSQType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('q-lpq',1),('q-wfq',2),('q-pq',3)))
class FSQDirectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('d-input',1),('d-output',2)))
class FSLayerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('l3-layer',0),('link-layer',1),('all-layer',2)))
_FsCBQoSMIBObjects_ObjectIdentity=ObjectIdentity
fsCBQoSMIBObjects=_FsCBQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,1))
_FsCBQoSIfStaticsObjects_ObjectIdentity=ObjectIdentity
fsCBQoSIfStaticsObjects=_FsCBQoSIfStaticsObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,1,1))
_FsCBQoSIfCbwfqRunInfoTable_Object=MibTable
fsCBQoSIfCbwfqRunInfoTable=_FsCBQoSIfCbwfqRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1))
if mibBuilder.loadTexts:fsCBQoSIfCbwfqRunInfoTable.setStatus(_A)
_FsCBQoSIfCbwfqRunInfoEntry_Object=MibTableRow
fsCBQoSIfCbwfqRunInfoEntry=_FsCBQoSIfCbwfqRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1))
fsCBQoSIfCbwfqRunInfoEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:fsCBQoSIfCbwfqRunInfoEntry.setStatus(_A)
_FsCBQoSIfCbwfqPolicyIfIndex_Type=Integer32
_FsCBQoSIfCbwfqPolicyIfIndex_Object=MibTableColumn
fsCBQoSIfCbwfqPolicyIfIndex=_FsCBQoSIfCbwfqPolicyIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,1),_FsCBQoSIfCbwfqPolicyIfIndex_Type())
fsCBQoSIfCbwfqPolicyIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqPolicyIfIndex.setStatus(_A)
_FsCBQoSIfCbwfqQueueSize_Type=Integer32
_FsCBQoSIfCbwfqQueueSize_Object=MibTableColumn
fsCBQoSIfCbwfqQueueSize=_FsCBQoSIfCbwfqQueueSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,2),_FsCBQoSIfCbwfqQueueSize_Type())
fsCBQoSIfCbwfqQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqQueueSize.setStatus(_A)
_FsCBQoSIfCbwfqDiscard_Type=Counter64
_FsCBQoSIfCbwfqDiscard_Object=MibTableColumn
fsCBQoSIfCbwfqDiscard=_FsCBQoSIfCbwfqDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,3),_FsCBQoSIfCbwfqDiscard_Type())
fsCBQoSIfCbwfqDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqDiscard.setStatus(_A)
_FsCBQoSIfCbwfqEfQueueSize_Type=Integer32
_FsCBQoSIfCbwfqEfQueueSize_Object=MibTableColumn
fsCBQoSIfCbwfqEfQueueSize=_FsCBQoSIfCbwfqEfQueueSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,4),_FsCBQoSIfCbwfqEfQueueSize_Type())
fsCBQoSIfCbwfqEfQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqEfQueueSize.setStatus(_A)
_FsCBQoSIfCbwfqAfQueueSize_Type=Integer32
_FsCBQoSIfCbwfqAfQueueSize_Object=MibTableColumn
fsCBQoSIfCbwfqAfQueueSize=_FsCBQoSIfCbwfqAfQueueSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,5),_FsCBQoSIfCbwfqAfQueueSize_Type())
fsCBQoSIfCbwfqAfQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqAfQueueSize.setStatus(_A)
_FsCBQoSIfCbwfqBeQueueSize_Type=Integer32
_FsCBQoSIfCbwfqBeQueueSize_Object=MibTableColumn
fsCBQoSIfCbwfqBeQueueSize=_FsCBQoSIfCbwfqBeQueueSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,6),_FsCBQoSIfCbwfqBeQueueSize_Type())
fsCBQoSIfCbwfqBeQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqBeQueueSize.setStatus(_A)
_FsCBQoSIfCbwfqBeActiveQueueNum_Type=Integer32
_FsCBQoSIfCbwfqBeActiveQueueNum_Object=MibTableColumn
fsCBQoSIfCbwfqBeActiveQueueNum=_FsCBQoSIfCbwfqBeActiveQueueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,7),_FsCBQoSIfCbwfqBeActiveQueueNum_Type())
fsCBQoSIfCbwfqBeActiveQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqBeActiveQueueNum.setStatus(_A)
_FsCBQoSIfCbwfqBeMaxActiveQueueNum_Type=Integer32
_FsCBQoSIfCbwfqBeMaxActiveQueueNum_Object=MibTableColumn
fsCBQoSIfCbwfqBeMaxActiveQueueNum=_FsCBQoSIfCbwfqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,8),_FsCBQoSIfCbwfqBeMaxActiveQueueNum_Type())
fsCBQoSIfCbwfqBeMaxActiveQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqBeMaxActiveQueueNum.setStatus(_A)
_FsCBQoSIfCbwfqBeTotalQueueNum_Type=Integer32
_FsCBQoSIfCbwfqBeTotalQueueNum_Object=MibTableColumn
fsCBQoSIfCbwfqBeTotalQueueNum=_FsCBQoSIfCbwfqBeTotalQueueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,9),_FsCBQoSIfCbwfqBeTotalQueueNum_Type())
fsCBQoSIfCbwfqBeTotalQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqBeTotalQueueNum.setStatus(_A)
_FsCBQoSIfCbwfqAfAllocatedQueueNum_Type=Integer32
_FsCBQoSIfCbwfqAfAllocatedQueueNum_Object=MibTableColumn
fsCBQoSIfCbwfqAfAllocatedQueueNum=_FsCBQoSIfCbwfqAfAllocatedQueueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,10),_FsCBQoSIfCbwfqAfAllocatedQueueNum_Type())
fsCBQoSIfCbwfqAfAllocatedQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqAfAllocatedQueueNum.setStatus(_A)
_FsCBQoSIfCbwfqPass_Type=Counter64
_FsCBQoSIfCbwfqPass_Object=MibTableColumn
fsCBQoSIfCbwfqPass=_FsCBQoSIfCbwfqPass_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,11),_FsCBQoSIfCbwfqPass_Type())
fsCBQoSIfCbwfqPass.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqPass.setStatus(_A)
class _FsCBQoSIfCbwfqDroppedRateIn5Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsCBQoSIfCbwfqDroppedRateIn5Min_Type.__name__=_D
_FsCBQoSIfCbwfqDroppedRateIn5Min_Object=MibTableColumn
fsCBQoSIfCbwfqDroppedRateIn5Min=_FsCBQoSIfCbwfqDroppedRateIn5Min_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,12),_FsCBQoSIfCbwfqDroppedRateIn5Min_Type())
fsCBQoSIfCbwfqDroppedRateIn5Min.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqDroppedRateIn5Min.setStatus(_A)
_FsCBQoSIfCbwfqPassBytes_Type=Counter64
_FsCBQoSIfCbwfqPassBytes_Object=MibTableColumn
fsCBQoSIfCbwfqPassBytes=_FsCBQoSIfCbwfqPassBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,13),_FsCBQoSIfCbwfqPassBytes_Type())
fsCBQoSIfCbwfqPassBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqPassBytes.setStatus(_A)
_FsCBQoSIfCbwfqDiscardBytes_Type=Counter64
_FsCBQoSIfCbwfqDiscardBytes_Object=MibTableColumn
fsCBQoSIfCbwfqDiscardBytes=_FsCBQoSIfCbwfqDiscardBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,1,1,14),_FsCBQoSIfCbwfqDiscardBytes_Type())
fsCBQoSIfCbwfqDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCbwfqDiscardBytes.setStatus(_A)
_FsCBQoSIfClassMatchRunInfoTable_Object=MibTable
fsCBQoSIfClassMatchRunInfoTable=_FsCBQoSIfClassMatchRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2))
if mibBuilder.loadTexts:fsCBQoSIfClassMatchRunInfoTable.setStatus(_A)
_FsCBQoSIfClassMatchRunInfoEntry_Object=MibTableRow
fsCBQoSIfClassMatchRunInfoEntry=_FsCBQoSIfClassMatchRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1))
fsCBQoSIfClassMatchRunInfoEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:fsCBQoSIfClassMatchRunInfoEntry.setStatus(_A)
_FsCBQoSIfClassMatchIfIndex_Type=Integer32
_FsCBQoSIfClassMatchIfIndex_Object=MibTableColumn
fsCBQoSIfClassMatchIfIndex=_FsCBQoSIfClassMatchIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,1),_FsCBQoSIfClassMatchIfIndex_Type())
fsCBQoSIfClassMatchIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassMatchIfIndex.setStatus(_A)
class _FsCBQoSIfClassMatchPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_FsCBQoSIfClassMatchPolicyDirection_Type.__name__=_D
_FsCBQoSIfClassMatchPolicyDirection_Object=MibTableColumn
fsCBQoSIfClassMatchPolicyDirection=_FsCBQoSIfClassMatchPolicyDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,2),_FsCBQoSIfClassMatchPolicyDirection_Type())
fsCBQoSIfClassMatchPolicyDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassMatchPolicyDirection.setStatus(_A)
_FsCBQoSIfClassMatchClassIndex_Type=Integer32
_FsCBQoSIfClassMatchClassIndex_Object=MibTableColumn
fsCBQoSIfClassMatchClassIndex=_FsCBQoSIfClassMatchClassIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,3),_FsCBQoSIfClassMatchClassIndex_Type())
fsCBQoSIfClassMatchClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassMatchClassIndex.setStatus(_A)
_FsCBQoSIfClassMatchedPackets_Type=Counter64
_FsCBQoSIfClassMatchedPackets_Object=MibTableColumn
fsCBQoSIfClassMatchedPackets=_FsCBQoSIfClassMatchedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,4),_FsCBQoSIfClassMatchedPackets_Type())
fsCBQoSIfClassMatchedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassMatchedPackets.setStatus(_A)
_FsCBQoSIfClassMatchedBytes_Type=Counter64
_FsCBQoSIfClassMatchedBytes_Object=MibTableColumn
fsCBQoSIfClassMatchedBytes=_FsCBQoSIfClassMatchedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,5),_FsCBQoSIfClassMatchedBytes_Type())
fsCBQoSIfClassMatchedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassMatchedBytes.setStatus(_A)
_FsCBQosIfClassPassedPackets_Type=Counter64
_FsCBQosIfClassPassedPackets_Object=MibTableColumn
fsCBQosIfClassPassedPackets=_FsCBQosIfClassPassedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,6),_FsCBQosIfClassPassedPackets_Type())
fsCBQosIfClassPassedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQosIfClassPassedPackets.setStatus(_A)
_FsCBQosIfClassDroppedPackets_Type=Counter64
_FsCBQosIfClassDroppedPackets_Object=MibTableColumn
fsCBQosIfClassDroppedPackets=_FsCBQosIfClassDroppedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,7),_FsCBQosIfClassDroppedPackets_Type())
fsCBQosIfClassDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQosIfClassDroppedPackets.setStatus(_A)
class _FsCBQoSIfPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsCBQoSIfPolicyName_Type.__name__=_F
_FsCBQoSIfPolicyName_Object=MibTableColumn
fsCBQoSIfPolicyName=_FsCBQoSIfPolicyName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,8),_FsCBQoSIfPolicyName_Type())
fsCBQoSIfPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfPolicyName.setStatus(_A)
class _FsCBQoSIfClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsCBQoSIfClassName_Type.__name__=_F
_FsCBQoSIfClassName_Object=MibTableColumn
fsCBQoSIfClassName=_FsCBQoSIfClassName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,9),_FsCBQoSIfClassName_Type())
fsCBQoSIfClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassName.setStatus(_A)
_FsCBQoSIfClassPassBytes_Type=Counter64
_FsCBQoSIfClassPassBytes_Object=MibTableColumn
fsCBQoSIfClassPassBytes=_FsCBQoSIfClassPassBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,10),_FsCBQoSIfClassPassBytes_Type())
fsCBQoSIfClassPassBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassPassBytes.setStatus(_A)
_FsCBQoSIfClassDiscardBytes_Type=Counter64
_FsCBQoSIfClassDiscardBytes_Object=MibTableColumn
fsCBQoSIfClassDiscardBytes=_FsCBQoSIfClassDiscardBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,2,1,11),_FsCBQoSIfClassDiscardBytes_Type())
fsCBQoSIfClassDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfClassDiscardBytes.setStatus(_A)
_FsCBQoSIfCarRunInfoTable_Object=MibTable
fsCBQoSIfCarRunInfoTable=_FsCBQoSIfCarRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3))
if mibBuilder.loadTexts:fsCBQoSIfCarRunInfoTable.setStatus(_A)
_FsCBQoSIfCarRunInfoEntry_Object=MibTableRow
fsCBQoSIfCarRunInfoEntry=_FsCBQoSIfCarRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1))
fsCBQoSIfCarRunInfoEntry.setIndexNames((0,_E,_e),(0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:fsCBQoSIfCarRunInfoEntry.setStatus(_A)
_FsCBQoSIfCarIfIndex_Type=Integer32
_FsCBQoSIfCarIfIndex_Object=MibTableColumn
fsCBQoSIfCarIfIndex=_FsCBQoSIfCarIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,1),_FsCBQoSIfCarIfIndex_Type())
fsCBQoSIfCarIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarIfIndex.setStatus(_A)
class _FsCBQoSIfCarPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_FsCBQoSIfCarPolicyDirection_Type.__name__=_D
_FsCBQoSIfCarPolicyDirection_Object=MibTableColumn
fsCBQoSIfCarPolicyDirection=_FsCBQoSIfCarPolicyDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,2),_FsCBQoSIfCarPolicyDirection_Type())
fsCBQoSIfCarPolicyDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarPolicyDirection.setStatus(_A)
_FsCBQoSIfCarClassIndex_Type=Integer32
_FsCBQoSIfCarClassIndex_Object=MibTableColumn
fsCBQoSIfCarClassIndex=_FsCBQoSIfCarClassIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,3),_FsCBQoSIfCarClassIndex_Type())
fsCBQoSIfCarClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarClassIndex.setStatus(_A)
_FsCBQoSIfCarConformedPackets_Type=Counter64
_FsCBQoSIfCarConformedPackets_Object=MibTableColumn
fsCBQoSIfCarConformedPackets=_FsCBQoSIfCarConformedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,4),_FsCBQoSIfCarConformedPackets_Type())
fsCBQoSIfCarConformedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarConformedPackets.setStatus(_A)
_FsCBQoSIfCarConformedBytes_Type=Counter64
_FsCBQoSIfCarConformedBytes_Object=MibTableColumn
fsCBQoSIfCarConformedBytes=_FsCBQoSIfCarConformedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,5),_FsCBQoSIfCarConformedBytes_Type())
fsCBQoSIfCarConformedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarConformedBytes.setStatus(_A)
_FsCBQoSIfCarExceededPackets_Type=Counter64
_FsCBQoSIfCarExceededPackets_Object=MibTableColumn
fsCBQoSIfCarExceededPackets=_FsCBQoSIfCarExceededPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,6),_FsCBQoSIfCarExceededPackets_Type())
fsCBQoSIfCarExceededPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarExceededPackets.setStatus(_A)
_FsCBQoSIfCarExceededBytes_Type=Counter64
_FsCBQoSIfCarExceededBytes_Object=MibTableColumn
fsCBQoSIfCarExceededBytes=_FsCBQoSIfCarExceededBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,7),_FsCBQoSIfCarExceededBytes_Type())
fsCBQoSIfCarExceededBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarExceededBytes.setStatus(_A)
_FsCBQoSIfCarViolatedPackets_Type=Counter64
_FsCBQoSIfCarViolatedPackets_Object=MibTableColumn
fsCBQoSIfCarViolatedPackets=_FsCBQoSIfCarViolatedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,8),_FsCBQoSIfCarViolatedPackets_Type())
fsCBQoSIfCarViolatedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarViolatedPackets.setStatus(_A)
_FsCBQoSIfCarViolatedBytes_Type=Counter64
_FsCBQoSIfCarViolatedBytes_Object=MibTableColumn
fsCBQoSIfCarViolatedBytes=_FsCBQoSIfCarViolatedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,3,1,9),_FsCBQoSIfCarViolatedBytes_Type())
fsCBQoSIfCarViolatedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfCarViolatedBytes.setStatus(_A)
_FsCBQoSIfRemarkRunInfoTable_Object=MibTable
fsCBQoSIfRemarkRunInfoTable=_FsCBQoSIfRemarkRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4))
if mibBuilder.loadTexts:fsCBQoSIfRemarkRunInfoTable.setStatus(_A)
_FsCBQoSIfRemarkRunInfoEntry_Object=MibTableRow
fsCBQoSIfRemarkRunInfoEntry=_FsCBQoSIfRemarkRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4,1))
fsCBQoSIfRemarkRunInfoEntry.setIndexNames((0,_E,_h),(0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:fsCBQoSIfRemarkRunInfoEntry.setStatus(_A)
_FsCBQoSIfRemarkIfIndex_Type=Integer32
_FsCBQoSIfRemarkIfIndex_Object=MibTableColumn
fsCBQoSIfRemarkIfIndex=_FsCBQoSIfRemarkIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4,1,1),_FsCBQoSIfRemarkIfIndex_Type())
fsCBQoSIfRemarkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfRemarkIfIndex.setStatus(_A)
class _FsCBQoSIfRemarkPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_FsCBQoSIfRemarkPolicyDirection_Type.__name__=_D
_FsCBQoSIfRemarkPolicyDirection_Object=MibTableColumn
fsCBQoSIfRemarkPolicyDirection=_FsCBQoSIfRemarkPolicyDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4,1,2),_FsCBQoSIfRemarkPolicyDirection_Type())
fsCBQoSIfRemarkPolicyDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfRemarkPolicyDirection.setStatus(_A)
_FsCBQoSIfRemarkClassIndex_Type=Integer32
_FsCBQoSIfRemarkClassIndex_Object=MibTableColumn
fsCBQoSIfRemarkClassIndex=_FsCBQoSIfRemarkClassIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4,1,3),_FsCBQoSIfRemarkClassIndex_Type())
fsCBQoSIfRemarkClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfRemarkClassIndex.setStatus(_A)
_FsCBQoSIfRemarkedPackets_Type=Counter64
_FsCBQoSIfRemarkedPackets_Object=MibTableColumn
fsCBQoSIfRemarkedPackets=_FsCBQoSIfRemarkedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4,1,4),_FsCBQoSIfRemarkedPackets_Type())
fsCBQoSIfRemarkedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfRemarkedPackets.setStatus(_A)
_FsCBQoSIfRemarkedBytes_Type=Counter64
_FsCBQoSIfRemarkedBytes_Object=MibTableColumn
fsCBQoSIfRemarkedBytes=_FsCBQoSIfRemarkedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,4,1,5),_FsCBQoSIfRemarkedBytes_Type())
fsCBQoSIfRemarkedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfRemarkedBytes.setStatus(_A)
_FsCBQoSIfQueueRunInfoTable_Object=MibTable
fsCBQoSIfQueueRunInfoTable=_FsCBQoSIfQueueRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5))
if mibBuilder.loadTexts:fsCBQoSIfQueueRunInfoTable.setStatus(_A)
_FsCBQoSIfQueueRunInfoEntry_Object=MibTableRow
fsCBQoSIfQueueRunInfoEntry=_FsCBQoSIfQueueRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1))
fsCBQoSIfQueueRunInfoEntry.setIndexNames((0,_E,_k),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:fsCBQoSIfQueueRunInfoEntry.setStatus(_A)
_FsCBQoSIfQueueIfIndex_Type=Integer32
_FsCBQoSIfQueueIfIndex_Object=MibTableColumn
fsCBQoSIfQueueIfIndex=_FsCBQoSIfQueueIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,1),_FsCBQoSIfQueueIfIndex_Type())
fsCBQoSIfQueueIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueIfIndex.setStatus(_A)
class _FsCBQoSIfQueuePolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_FsCBQoSIfQueuePolicyDirection_Type.__name__=_D
_FsCBQoSIfQueuePolicyDirection_Object=MibTableColumn
fsCBQoSIfQueuePolicyDirection=_FsCBQoSIfQueuePolicyDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,2),_FsCBQoSIfQueuePolicyDirection_Type())
fsCBQoSIfQueuePolicyDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueuePolicyDirection.setStatus(_A)
_FsCBQoSIfQueueClassIndex_Type=Integer32
_FsCBQoSIfQueueClassIndex_Object=MibTableColumn
fsCBQoSIfQueueClassIndex=_FsCBQoSIfQueueClassIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,3),_FsCBQoSIfQueueClassIndex_Type())
fsCBQoSIfQueueClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueClassIndex.setStatus(_A)
_FsCBQoSIfQueueMatchedPackets_Type=Counter64
_FsCBQoSIfQueueMatchedPackets_Object=MibTableColumn
fsCBQoSIfQueueMatchedPackets=_FsCBQoSIfQueueMatchedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,4),_FsCBQoSIfQueueMatchedPackets_Type())
fsCBQoSIfQueueMatchedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueMatchedPackets.setStatus(_A)
_FsCBQoSIfQueueMatchedBytes_Type=Counter64
_FsCBQoSIfQueueMatchedBytes_Object=MibTableColumn
fsCBQoSIfQueueMatchedBytes=_FsCBQoSIfQueueMatchedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,5),_FsCBQoSIfQueueMatchedBytes_Type())
fsCBQoSIfQueueMatchedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueMatchedBytes.setStatus(_A)
_FsCBQoSIfQueueEnqueuedPackets_Type=Counter64
_FsCBQoSIfQueueEnqueuedPackets_Object=MibTableColumn
fsCBQoSIfQueueEnqueuedPackets=_FsCBQoSIfQueueEnqueuedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,6),_FsCBQoSIfQueueEnqueuedPackets_Type())
fsCBQoSIfQueueEnqueuedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueEnqueuedPackets.setStatus(_A)
_FsCBQoSIfQueueEnqueuedBytes_Type=Counter64
_FsCBQoSIfQueueEnqueuedBytes_Object=MibTableColumn
fsCBQoSIfQueueEnqueuedBytes=_FsCBQoSIfQueueEnqueuedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,7),_FsCBQoSIfQueueEnqueuedBytes_Type())
fsCBQoSIfQueueEnqueuedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueEnqueuedBytes.setStatus(_A)
_FsCBQoSIfQueueDiscardedPackets_Type=Counter64
_FsCBQoSIfQueueDiscardedPackets_Object=MibTableColumn
fsCBQoSIfQueueDiscardedPackets=_FsCBQoSIfQueueDiscardedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,8),_FsCBQoSIfQueueDiscardedPackets_Type())
fsCBQoSIfQueueDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueDiscardedPackets.setStatus(_A)
_FsCBQoSIfQueueDiscardedBytes_Type=Counter64
_FsCBQoSIfQueueDiscardedBytes_Object=MibTableColumn
fsCBQoSIfQueueDiscardedBytes=_FsCBQoSIfQueueDiscardedBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,5,1,9),_FsCBQoSIfQueueDiscardedBytes_Type())
fsCBQoSIfQueueDiscardedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfQueueDiscardedBytes.setStatus(_A)
_FsCBQoSIfWredRunInfoTable_Object=MibTable
fsCBQoSIfWredRunInfoTable=_FsCBQoSIfWredRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6))
if mibBuilder.loadTexts:fsCBQoSIfWredRunInfoTable.setStatus(_A)
_FsCBQoSIfWredRunInfoEntry_Object=MibTableRow
fsCBQoSIfWredRunInfoEntry=_FsCBQoSIfWredRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6,1))
fsCBQoSIfWredRunInfoEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:fsCBQoSIfWredRunInfoEntry.setStatus(_A)
_FsCBQoSIfWredIfIndex_Type=Integer32
_FsCBQoSIfWredIfIndex_Object=MibTableColumn
fsCBQoSIfWredIfIndex=_FsCBQoSIfWredIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6,1,1),_FsCBQoSIfWredIfIndex_Type())
fsCBQoSIfWredIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfWredIfIndex.setStatus(_A)
_FsCBQoSIfWredClassIndex_Type=Integer32
_FsCBQoSIfWredClassIndex_Object=MibTableColumn
fsCBQoSIfWredClassIndex=_FsCBQoSIfWredClassIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6,1,2),_FsCBQoSIfWredClassIndex_Type())
fsCBQoSIfWredClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfWredClassIndex.setStatus(_A)
_FsCBQoSIfWredClassValue_Type=Integer32
_FsCBQoSIfWredClassValue_Object=MibTableColumn
fsCBQoSIfWredClassValue=_FsCBQoSIfWredClassValue_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6,1,3),_FsCBQoSIfWredClassValue_Type())
fsCBQoSIfWredClassValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfWredClassValue.setStatus(_A)
_FsCBQoSIfWredRandomDiscardedPackets_Type=Counter64
_FsCBQoSIfWredRandomDiscardedPackets_Object=MibTableColumn
fsCBQoSIfWredRandomDiscardedPackets=_FsCBQoSIfWredRandomDiscardedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6,1,4),_FsCBQoSIfWredRandomDiscardedPackets_Type())
fsCBQoSIfWredRandomDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfWredRandomDiscardedPackets.setStatus(_A)
_FsCBQoSIfWredTailDiscardedPackets_Type=Counter64
_FsCBQoSIfWredTailDiscardedPackets_Object=MibTableColumn
fsCBQoSIfWredTailDiscardedPackets=_FsCBQoSIfWredTailDiscardedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,1,1,6,1,5),_FsCBQoSIfWredTailDiscardedPackets_Type())
fsCBQoSIfWredTailDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCBQoSIfWredTailDiscardedPackets.setStatus(_A)
_FsIfQoSMIBObjects_ObjectIdentity=ObjectIdentity
fsIfQoSMIBObjects=_FsIfQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,2))
_FsIfQosPQRunInfoTable_Object=MibTable
fsIfQosPQRunInfoTable=_FsIfQosPQRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1))
if mibBuilder.loadTexts:fsIfQosPQRunInfoTable.setStatus(_A)
_FsIfQosPQRunInfoEntry_Object=MibTableRow
fsIfQosPQRunInfoEntry=_FsIfQosPQRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1))
fsIfQosPQRunInfoEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:fsIfQosPQRunInfoEntry.setStatus(_A)
_FsIfQosPQIfIndex_Type=Integer32
_FsIfQosPQIfIndex_Object=MibTableColumn
fsIfQosPQIfIndex=_FsIfQosPQIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,1),_FsIfQosPQIfIndex_Type())
fsIfQosPQIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQIfIndex.setStatus(_A)
class _FsIfQosPQListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsIfQosPQListNum_Type.__name__=_D
_FsIfQosPQListNum_Object=MibTableColumn
fsIfQosPQListNum=_FsIfQosPQListNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,2),_FsIfQosPQListNum_Type())
fsIfQosPQListNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQListNum.setStatus(_A)
_FsIfQosPQIfName_Type=OctetString
_FsIfQosPQIfName_Object=MibTableColumn
fsIfQosPQIfName=_FsIfQosPQIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,3),_FsIfQosPQIfName_Type())
fsIfQosPQIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQIfName.setStatus(_A)
class _FsIfQosPQHighPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosPQHighPkt_Type.__name__=_D
_FsIfQosPQHighPkt_Object=MibTableColumn
fsIfQosPQHighPkt=_FsIfQosPQHighPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,4),_FsIfQosPQHighPkt_Type())
fsIfQosPQHighPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQHighPkt.setStatus(_A)
_FsIfQosPQHighDiscard_Type=Counter32
_FsIfQosPQHighDiscard_Object=MibTableColumn
fsIfQosPQHighDiscard=_FsIfQosPQHighDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,5),_FsIfQosPQHighDiscard_Type())
fsIfQosPQHighDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQHighDiscard.setStatus(_A)
class _FsIfQosPQHighMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosPQHighMaxQueLen_Type.__name__=_D
_FsIfQosPQHighMaxQueLen_Object=MibTableColumn
fsIfQosPQHighMaxQueLen=_FsIfQosPQHighMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,6),_FsIfQosPQHighMaxQueLen_Type())
fsIfQosPQHighMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQHighMaxQueLen.setStatus(_A)
class _FsIfQosPQMiddlePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosPQMiddlePkt_Type.__name__=_D
_FsIfQosPQMiddlePkt_Object=MibTableColumn
fsIfQosPQMiddlePkt=_FsIfQosPQMiddlePkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,7),_FsIfQosPQMiddlePkt_Type())
fsIfQosPQMiddlePkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQMiddlePkt.setStatus(_A)
_FsIfQosPQMiddleDiscard_Type=Counter32
_FsIfQosPQMiddleDiscard_Object=MibTableColumn
fsIfQosPQMiddleDiscard=_FsIfQosPQMiddleDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,8),_FsIfQosPQMiddleDiscard_Type())
fsIfQosPQMiddleDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQMiddleDiscard.setStatus(_A)
class _FsIfQosPQMiddleMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosPQMiddleMaxQueLen_Type.__name__=_D
_FsIfQosPQMiddleMaxQueLen_Object=MibTableColumn
fsIfQosPQMiddleMaxQueLen=_FsIfQosPQMiddleMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,9),_FsIfQosPQMiddleMaxQueLen_Type())
fsIfQosPQMiddleMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQMiddleMaxQueLen.setStatus(_A)
class _FsIfQosPQNormalPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosPQNormalPkt_Type.__name__=_D
_FsIfQosPQNormalPkt_Object=MibTableColumn
fsIfQosPQNormalPkt=_FsIfQosPQNormalPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,10),_FsIfQosPQNormalPkt_Type())
fsIfQosPQNormalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQNormalPkt.setStatus(_A)
_FsIfQosPQNormalDiscard_Type=Counter32
_FsIfQosPQNormalDiscard_Object=MibTableColumn
fsIfQosPQNormalDiscard=_FsIfQosPQNormalDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,11),_FsIfQosPQNormalDiscard_Type())
fsIfQosPQNormalDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQNormalDiscard.setStatus(_A)
class _FsIfQosPQNormalMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosPQNormalMaxQueLen_Type.__name__=_D
_FsIfQosPQNormalMaxQueLen_Object=MibTableColumn
fsIfQosPQNormalMaxQueLen=_FsIfQosPQNormalMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,12),_FsIfQosPQNormalMaxQueLen_Type())
fsIfQosPQNormalMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQNormalMaxQueLen.setStatus(_A)
class _FsIfQosPQLowPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosPQLowPkt_Type.__name__=_D
_FsIfQosPQLowPkt_Object=MibTableColumn
fsIfQosPQLowPkt=_FsIfQosPQLowPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,13),_FsIfQosPQLowPkt_Type())
fsIfQosPQLowPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQLowPkt.setStatus(_A)
_FsIfQosPQLowDiscard_Type=Counter32
_FsIfQosPQLowDiscard_Object=MibTableColumn
fsIfQosPQLowDiscard=_FsIfQosPQLowDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,14),_FsIfQosPQLowDiscard_Type())
fsIfQosPQLowDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQLowDiscard.setStatus(_A)
class _FsIfQosPQLowMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosPQLowMaxQueLen_Type.__name__=_D
_FsIfQosPQLowMaxQueLen_Object=MibTableColumn
fsIfQosPQLowMaxQueLen=_FsIfQosPQLowMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,1,1,15),_FsIfQosPQLowMaxQueLen_Type())
fsIfQosPQLowMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosPQLowMaxQueLen.setStatus(_A)
_FsIfQosCQRunInfoTable_Object=MibTable
fsIfQosCQRunInfoTable=_FsIfQosCQRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2))
if mibBuilder.loadTexts:fsIfQosCQRunInfoTable.setStatus(_A)
_FsIfQosCQRunInfoEntry_Object=MibTableRow
fsIfQosCQRunInfoEntry=_FsIfQosCQRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1))
fsIfQosCQRunInfoEntry.setIndexNames((0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:fsIfQosCQRunInfoEntry.setStatus(_A)
_FsIfQosCQRunInfoIfIndex_Type=Integer32
_FsIfQosCQRunInfoIfIndex_Object=MibTableColumn
fsIfQosCQRunInfoIfIndex=_FsIfQosCQRunInfoIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1,1),_FsIfQosCQRunInfoIfIndex_Type())
fsIfQosCQRunInfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCQRunInfoIfIndex.setStatus(_A)
class _FsIfQosCQRunInfoQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsIfQosCQRunInfoQueNum_Type.__name__=_D
_FsIfQosCQRunInfoQueNum_Object=MibTableColumn
fsIfQosCQRunInfoQueNum=_FsIfQosCQRunInfoQueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1,2),_FsIfQosCQRunInfoQueNum_Type())
fsIfQosCQRunInfoQueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCQRunInfoQueNum.setStatus(_A)
_FsIfQosCQRunInfoIfName_Type=OctetString
_FsIfQosCQRunInfoIfName_Object=MibTableColumn
fsIfQosCQRunInfoIfName=_FsIfQosCQRunInfoIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1,3),_FsIfQosCQRunInfoIfName_Type())
fsIfQosCQRunInfoIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCQRunInfoIfName.setStatus(_A)
class _FsIfQosCQRunInfoQuePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosCQRunInfoQuePkt_Type.__name__=_D
_FsIfQosCQRunInfoQuePkt_Object=MibTableColumn
fsIfQosCQRunInfoQuePkt=_FsIfQosCQRunInfoQuePkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1,4),_FsIfQosCQRunInfoQuePkt_Type())
fsIfQosCQRunInfoQuePkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCQRunInfoQuePkt.setStatus(_A)
_FsIfQosCQRunInfoQueDiscard_Type=Counter32
_FsIfQosCQRunInfoQueDiscard_Object=MibTableColumn
fsIfQosCQRunInfoQueDiscard=_FsIfQosCQRunInfoQueDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1,5),_FsIfQosCQRunInfoQueDiscard_Type())
fsIfQosCQRunInfoQueDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCQRunInfoQueDiscard.setStatus(_A)
class _FsIfQosCQRunInfoMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosCQRunInfoMaxQueLen_Type.__name__=_D
_FsIfQosCQRunInfoMaxQueLen_Object=MibTableColumn
fsIfQosCQRunInfoMaxQueLen=_FsIfQosCQRunInfoMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,2,1,6),_FsIfQosCQRunInfoMaxQueLen_Type())
fsIfQosCQRunInfoMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCQRunInfoMaxQueLen.setStatus(_A)
_FsIfQosWFQRunInfoTable_Object=MibTable
fsIfQosWFQRunInfoTable=_FsIfQosWFQRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3))
if mibBuilder.loadTexts:fsIfQosWFQRunInfoTable.setStatus(_A)
_FsIfQosWFQRunInfoEntry_Object=MibTableRow
fsIfQosWFQRunInfoEntry=_FsIfQosWFQRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1))
fsIfQosWFQRunInfoEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:fsIfQosWFQRunInfoEntry.setStatus(_A)
_FsIfQosWFQIfIndex_Type=Integer32
_FsIfQosWFQIfIndex_Object=MibTableColumn
fsIfQosWFQIfIndex=_FsIfQosWFQIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,1),_FsIfQosWFQIfIndex_Type())
fsIfQosWFQIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQIfIndex.setStatus(_A)
_FsIfQosWFQIfName_Type=OctetString
_FsIfQosWFQIfName_Object=MibTableColumn
fsIfQosWFQIfName=_FsIfQosWFQIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,2),_FsIfQosWFQIfName_Type())
fsIfQosWFQIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQIfName.setStatus(_A)
class _FsIfQosWFQMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosWFQMaxQueLen_Type.__name__=_D
_FsIfQosWFQMaxQueLen_Object=MibTableColumn
fsIfQosWFQMaxQueLen=_FsIfQosWFQMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,3),_FsIfQosWFQMaxQueLen_Type())
fsIfQosWFQMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQMaxQueLen.setStatus(_A)
class _FsIfQosWFQTotalQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*(('a16',16),('a32',32),('a64',64),('a128',128),('a256',256),('a512',512),('a1024',1024),('a2048',2048),('a4096',4096)))
_FsIfQosWFQTotalQueNum_Type.__name__=_D
_FsIfQosWFQTotalQueNum_Object=MibTableColumn
fsIfQosWFQTotalQueNum=_FsIfQosWFQTotalQueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,4),_FsIfQosWFQTotalQueNum_Type())
fsIfQosWFQTotalQueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQTotalQueNum.setStatus(_A)
_FsIfQosWFQCurQueLen_Type=Integer32
_FsIfQosWFQCurQueLen_Object=MibTableColumn
fsIfQosWFQCurQueLen=_FsIfQosWFQCurQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,5),_FsIfQosWFQCurQueLen_Type())
fsIfQosWFQCurQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQCurQueLen.setStatus(_A)
_FsIfQosWFQTotalDiscard_Type=Counter32
_FsIfQosWFQTotalDiscard_Object=MibTableColumn
fsIfQosWFQTotalDiscard=_FsIfQosWFQTotalDiscard_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,6),_FsIfQosWFQTotalDiscard_Type())
fsIfQosWFQTotalDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQTotalDiscard.setStatus(_A)
class _FsIfQosWFQActiveQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosWFQActiveQueNum_Type.__name__=_D
_FsIfQosWFQActiveQueNum_Object=MibTableColumn
fsIfQosWFQActiveQueNum=_FsIfQosWFQActiveQueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,7),_FsIfQosWFQActiveQueNum_Type())
fsIfQosWFQActiveQueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQActiveQueNum.setStatus(_A)
class _FsIfQosWFQMaxActiveQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FsIfQosWFQMaxActiveQueNum_Type.__name__=_D
_FsIfQosWFQMaxActiveQueNum_Object=MibTableColumn
fsIfQosWFQMaxActiveQueNum=_FsIfQosWFQMaxActiveQueNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,3,1,8),_FsIfQosWFQMaxActiveQueNum_Type())
fsIfQosWFQMaxActiveQueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWFQMaxActiveQueNum.setStatus(_A)
_FsIfQosWredRunInfoTable_Object=MibTable
fsIfQosWredRunInfoTable=_FsIfQosWredRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,4))
if mibBuilder.loadTexts:fsIfQosWredRunInfoTable.setStatus(_A)
_FsIfQosWredRunInfoEntry_Object=MibTableRow
fsIfQosWredRunInfoEntry=_FsIfQosWredRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,4,1))
fsIfQosWredRunInfoEntry.setIndexNames((0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:fsIfQosWredRunInfoEntry.setStatus(_A)
_FsIfQosWredIfIndex_Type=Integer32
_FsIfQosWredIfIndex_Object=MibTableColumn
fsIfQosWredIfIndex=_FsIfQosWredIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,4,1,1),_FsIfQosWredIfIndex_Type())
fsIfQosWredIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWredIfIndex.setStatus(_A)
_FsIfQosWredValue_Type=Integer32
_FsIfQosWredValue_Object=MibTableColumn
fsIfQosWredValue=_FsIfQosWredValue_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,4,1,2),_FsIfQosWredValue_Type())
fsIfQosWredValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWredValue.setStatus(_A)
_FsIfQosWredRandomDiscardedPackets_Type=Counter64
_FsIfQosWredRandomDiscardedPackets_Object=MibTableColumn
fsIfQosWredRandomDiscardedPackets=_FsIfQosWredRandomDiscardedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,4,1,3),_FsIfQosWredRandomDiscardedPackets_Type())
fsIfQosWredRandomDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWredRandomDiscardedPackets.setStatus(_A)
_FsIfQosWredTailDiscardedPackets_Type=Counter64
_FsIfQosWredTailDiscardedPackets_Object=MibTableColumn
fsIfQosWredTailDiscardedPackets=_FsIfQosWredTailDiscardedPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,4,1,4),_FsIfQosWredTailDiscardedPackets_Type())
fsIfQosWredTailDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosWredTailDiscardedPackets.setStatus(_A)
_FsIfQosCARTable_Object=MibTable
fsIfQosCARTable=_FsIfQosCARTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5))
if mibBuilder.loadTexts:fsIfQosCARTable.setStatus(_A)
_FsIfQosCAREntry_Object=MibTableRow
fsIfQosCAREntry=_FsIfQosCAREntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1))
fsIfQosCAREntry.setIndexNames((0,_E,_w),(0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:fsIfQosCAREntry.setStatus(_A)
_FsIfQosCARIfIndex_Type=Integer32
_FsIfQosCARIfIndex_Object=MibTableColumn
fsIfQosCARIfIndex=_FsIfQosCARIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,1),_FsIfQosCARIfIndex_Type())
fsIfQosCARIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARIfIndex.setStatus(_A)
_FsIfQosCARIfName_Type=OctetString
_FsIfQosCARIfName_Object=MibTableColumn
fsIfQosCARIfName=_FsIfQosCARIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,2),_FsIfQosCARIfName_Type())
fsIfQosCARIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARIfName.setStatus(_A)
class _FsIfQosCARPktDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('outout',2)))
_FsIfQosCARPktDirection_Type.__name__=_D
_FsIfQosCARPktDirection_Object=MibTableColumn
fsIfQosCARPktDirection=_FsIfQosCARPktDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,3),_FsIfQosCARPktDirection_Type())
fsIfQosCARPktDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARPktDirection.setStatus(_A)
class _FsIfQosCARType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acl',1),('dscp',2),('qos-group',3),('default',4)))
_FsIfQosCARType_Type.__name__=_D
_FsIfQosCARType_Object=MibTableColumn
fsIfQosCARType=_FsIfQosCARType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,4),_FsIfQosCARType_Type())
fsIfQosCARType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARType.setStatus(_A)
_FsIfQosCARListNum_Type=Integer32
_FsIfQosCARListNum_Object=MibTableColumn
fsIfQosCARListNum=_FsIfQosCARListNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,5),_FsIfQosCARListNum_Type())
fsIfQosCARListNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARListNum.setStatus(_A)
_FsIfQosCARindex_Type=Integer32
_FsIfQosCARindex_Object=MibTableColumn
fsIfQosCARindex=_FsIfQosCARindex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,6),_FsIfQosCARindex_Type())
fsIfQosCARindex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARindex.setStatus(_A)
class _FsIfQosCARCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_FsIfQosCARCIR_Type.__name__=_D
_FsIfQosCARCIR_Object=MibTableColumn
fsIfQosCARCIR=_FsIfQosCARCIR_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,7),_FsIfQosCARCIR_Type())
fsIfQosCARCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARCIR.setStatus(_A)
class _FsIfQosCARBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_FsIfQosCARBurstSize_Type.__name__=_D
_FsIfQosCARBurstSize_Object=MibTableColumn
fsIfQosCARBurstSize=_FsIfQosCARBurstSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,8),_FsIfQosCARBurstSize_Type())
fsIfQosCARBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARBurstSize.setStatus(_A)
class _FsIfQosCARExcessBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_FsIfQosCARExcessBurstSize_Type.__name__=_D
_FsIfQosCARExcessBurstSize_Object=MibTableColumn
fsIfQosCARExcessBurstSize=_FsIfQosCARExcessBurstSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,9),_FsIfQosCARExcessBurstSize_Type())
fsIfQosCARExcessBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARExcessBurstSize.setStatus(_A)
class _FsIfQosCARConformAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_FsIfQosCARConformAction_Type.__name__=_D
_FsIfQosCARConformAction_Object=MibTableColumn
fsIfQosCARConformAction=_FsIfQosCARConformAction_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,10),_FsIfQosCARConformAction_Type())
fsIfQosCARConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARConformAction.setStatus(_A)
class _FsIfQosCARExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_FsIfQosCARExceedAction_Type.__name__=_D
_FsIfQosCARExceedAction_Object=MibTableColumn
fsIfQosCARExceedAction=_FsIfQosCARExceedAction_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,11),_FsIfQosCARExceedAction_Type())
fsIfQosCARExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARExceedAction.setStatus(_A)
class _FsIfQosCARConformNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsIfQosCARConformNewPrec_Type.__name__=_D
_FsIfQosCARConformNewPrec_Object=MibTableColumn
fsIfQosCARConformNewPrec=_FsIfQosCARConformNewPrec_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,12),_FsIfQosCARConformNewPrec_Type())
fsIfQosCARConformNewPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARConformNewPrec.setStatus(_A)
class _FsIfQosCARExceedNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsIfQosCARExceedNewPrec_Type.__name__=_D
_FsIfQosCARExceedNewPrec_Object=MibTableColumn
fsIfQosCARExceedNewPrec=_FsIfQosCARExceedNewPrec_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,13),_FsIfQosCARExceedNewPrec_Type())
fsIfQosCARExceedNewPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARExceedNewPrec.setStatus(_A)
_FsIfQosCARConformPkt_Type=Counter32
_FsIfQosCARConformPkt_Object=MibTableColumn
fsIfQosCARConformPkt=_FsIfQosCARConformPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,14),_FsIfQosCARConformPkt_Type())
fsIfQosCARConformPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARConformPkt.setStatus(_A)
_FsIfQosCARConformByte_Type=Counter32
_FsIfQosCARConformByte_Object=MibTableColumn
fsIfQosCARConformByte=_FsIfQosCARConformByte_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,15),_FsIfQosCARConformByte_Type())
fsIfQosCARConformByte.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARConformByte.setStatus(_A)
_FsIfQosCARExceedPkt_Type=Counter32
_FsIfQosCARExceedPkt_Object=MibTableColumn
fsIfQosCARExceedPkt=_FsIfQosCARExceedPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,16),_FsIfQosCARExceedPkt_Type())
fsIfQosCARExceedPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARExceedPkt.setStatus(_A)
_FsIfQosCARExceedByte_Type=Counter32
_FsIfQosCARExceedByte_Object=MibTableColumn
fsIfQosCARExceedByte=_FsIfQosCARExceedByte_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,5,1,17),_FsIfQosCARExceedByte_Type())
fsIfQosCARExceedByte.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosCARExceedByte.setStatus(_A)
_FsIfQosGTSTable_Object=MibTable
fsIfQosGTSTable=_FsIfQosGTSTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6))
if mibBuilder.loadTexts:fsIfQosGTSTable.setStatus(_A)
_FsIfQosGTSEntry_Object=MibTableRow
fsIfQosGTSEntry=_FsIfQosGTSEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1))
fsIfQosGTSEntry.setIndexNames((0,_E,_z),(0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:fsIfQosGTSEntry.setStatus(_A)
_FsIfQosGTSIfIndex_Type=Integer32
_FsIfQosGTSIfIndex_Object=MibTableColumn
fsIfQosGTSIfIndex=_FsIfQosGTSIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,1),_FsIfQosGTSIfIndex_Type())
fsIfQosGTSIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSIfIndex.setStatus(_A)
_FsIfQosGTSIfName_Type=OctetString
_FsIfQosGTSIfName_Object=MibTableColumn
fsIfQosGTSIfName=_FsIfQosGTSIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,2),_FsIfQosGTSIfName_Type())
fsIfQosGTSIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSIfName.setStatus(_A)
class _FsIfQosGTSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('acl',1),('all',2)))
_FsIfQosGTSType_Type.__name__=_D
_FsIfQosGTSType_Object=MibTableColumn
fsIfQosGTSType=_FsIfQosGTSType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,3),_FsIfQosGTSType_Type())
fsIfQosGTSType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSType.setStatus(_A)
class _FsIfQosGTSACLNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_FsIfQosGTSACLNum_Type.__name__=_D
_FsIfQosGTSACLNum_Object=MibTableColumn
fsIfQosGTSACLNum=_FsIfQosGTSACLNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,4),_FsIfQosGTSACLNum_Type())
fsIfQosGTSACLNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSACLNum.setStatus(_A)
class _FsIfQosGTSCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_FsIfQosGTSCIR_Type.__name__=_D
_FsIfQosGTSCIR_Object=MibTableColumn
fsIfQosGTSCIR=_FsIfQosGTSCIR_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,5),_FsIfQosGTSCIR_Type())
fsIfQosGTSCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSCIR.setStatus(_A)
class _FsIfQosGTSBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_FsIfQosGTSBurstSize_Type.__name__=_D
_FsIfQosGTSBurstSize_Object=MibTableColumn
fsIfQosGTSBurstSize=_FsIfQosGTSBurstSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,6),_FsIfQosGTSBurstSize_Type())
fsIfQosGTSBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSBurstSize.setStatus(_A)
class _FsIfQosGTSExcessBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_FsIfQosGTSExcessBurstSize_Type.__name__=_D
_FsIfQosGTSExcessBurstSize_Object=MibTableColumn
fsIfQosGTSExcessBurstSize=_FsIfQosGTSExcessBurstSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,7),_FsIfQosGTSExcessBurstSize_Type())
fsIfQosGTSExcessBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSExcessBurstSize.setStatus(_A)
class _FsIfQosGTSMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsIfQosGTSMaxQueLen_Type.__name__=_D
_FsIfQosGTSMaxQueLen_Object=MibTableColumn
fsIfQosGTSMaxQueLen=_FsIfQosGTSMaxQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,8),_FsIfQosGTSMaxQueLen_Type())
fsIfQosGTSMaxQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSMaxQueLen.setStatus(_A)
_FsIfQosGTSCurQueLen_Type=Integer32
_FsIfQosGTSCurQueLen_Object=MibTableColumn
fsIfQosGTSCurQueLen=_FsIfQosGTSCurQueLen_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,9),_FsIfQosGTSCurQueLen_Type())
fsIfQosGTSCurQueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSCurQueLen.setStatus(_A)
_FsIfQosGTSPassPkt_Type=Counter32
_FsIfQosGTSPassPkt_Object=MibTableColumn
fsIfQosGTSPassPkt=_FsIfQosGTSPassPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,10),_FsIfQosGTSPassPkt_Type())
fsIfQosGTSPassPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSPassPkt.setStatus(_A)
_FsIfQosGTSPassByte_Type=Counter32
_FsIfQosGTSPassByte_Object=MibTableColumn
fsIfQosGTSPassByte=_FsIfQosGTSPassByte_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,11),_FsIfQosGTSPassByte_Type())
fsIfQosGTSPassByte.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSPassByte.setStatus(_A)
_FsIfQosGTSDiscardPkt_Type=Counter32
_FsIfQosGTSDiscardPkt_Object=MibTableColumn
fsIfQosGTSDiscardPkt=_FsIfQosGTSDiscardPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,12),_FsIfQosGTSDiscardPkt_Type())
fsIfQosGTSDiscardPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSDiscardPkt.setStatus(_A)
_FsIfQosGTSDiscardByte_Type=Counter32
_FsIfQosGTSDiscardByte_Object=MibTableColumn
fsIfQosGTSDiscardByte=_FsIfQosGTSDiscardByte_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,6,1,13),_FsIfQosGTSDiscardByte_Type())
fsIfQosGTSDiscardByte.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosGTSDiscardByte.setStatus(_A)
_FsIfQosRTPIfQueueRunInfoTable_Object=MibTable
fsIfQosRTPIfQueueRunInfoTable=_FsIfQosRTPIfQueueRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7))
if mibBuilder.loadTexts:fsIfQosRTPIfQueueRunInfoTable.setStatus(_A)
_FsIfQosRTPIfQueueRunInfoEntry_Object=MibTableRow
fsIfQosRTPIfQueueRunInfoEntry=_FsIfQosRTPIfQueueRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7,1))
fsIfQosRTPIfQueueRunInfoEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:fsIfQosRTPIfQueueRunInfoEntry.setStatus(_A)
_FsIfQosRTPIfApplyIfIndex_Type=Integer32
_FsIfQosRTPIfApplyIfIndex_Object=MibTableColumn
fsIfQosRTPIfApplyIfIndex=_FsIfQosRTPIfApplyIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7,1,1),_FsIfQosRTPIfApplyIfIndex_Type())
fsIfQosRTPIfApplyIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosRTPIfApplyIfIndex.setStatus(_A)
_FsIfQosRTPIfQueueSize_Type=Counter32
_FsIfQosRTPIfQueueSize_Object=MibTableColumn
fsIfQosRTPIfQueueSize=_FsIfQosRTPIfQueueSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7,1,2),_FsIfQosRTPIfQueueSize_Type())
fsIfQosRTPIfQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosRTPIfQueueSize.setStatus(_A)
_FsIfQosRTPIfQueueMaxSize_Type=Counter32
_FsIfQosRTPIfQueueMaxSize_Object=MibTableColumn
fsIfQosRTPIfQueueMaxSize=_FsIfQosRTPIfQueueMaxSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7,1,3),_FsIfQosRTPIfQueueMaxSize_Type())
fsIfQosRTPIfQueueMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosRTPIfQueueMaxSize.setStatus(_A)
_FsIfQosRTPIfQueueOutputs_Type=Counter32
_FsIfQosRTPIfQueueOutputs_Object=MibTableColumn
fsIfQosRTPIfQueueOutputs=_FsIfQosRTPIfQueueOutputs_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7,1,4),_FsIfQosRTPIfQueueOutputs_Type())
fsIfQosRTPIfQueueOutputs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosRTPIfQueueOutputs.setStatus(_A)
_FsIfQosRTPIfQueueDiscards_Type=Counter32
_FsIfQosRTPIfQueueDiscards_Object=MibTableColumn
fsIfQosRTPIfQueueDiscards=_FsIfQosRTPIfQueueDiscards_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,7,1,5),_FsIfQosRTPIfQueueDiscards_Type())
fsIfQosRTPIfQueueDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosRTPIfQueueDiscards.setStatus(_A)
_FsIfQosFlowLimitRunInfoTable_Object=MibTable
fsIfQosFlowLimitRunInfoTable=_FsIfQosFlowLimitRunInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8))
if mibBuilder.loadTexts:fsIfQosFlowLimitRunInfoTable.setStatus(_A)
_FsIfQosFlowLimitRunInfoEntry_Object=MibTableRow
fsIfQosFlowLimitRunInfoEntry=_FsIfQosFlowLimitRunInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1))
fsIfQosFlowLimitRunInfoEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:fsIfQosFlowLimitRunInfoEntry.setStatus(_A)
class _FsIfQosFlowLimitLabelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsIfQosFlowLimitLabelNum_Type.__name__=_D
_FsIfQosFlowLimitLabelNum_Object=MibTableColumn
fsIfQosFlowLimitLabelNum=_FsIfQosFlowLimitLabelNum_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,1),_FsIfQosFlowLimitLabelNum_Type())
fsIfQosFlowLimitLabelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitLabelNum.setStatus(_A)
class _FsIfQosFlowLimitPktDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_FsIfQosFlowLimitPktDirection_Type.__name__=_D
_FsIfQosFlowLimitPktDirection_Object=MibTableColumn
fsIfQosFlowLimitPktDirection=_FsIfQosFlowLimitPktDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,2),_FsIfQosFlowLimitPktDirection_Type())
fsIfQosFlowLimitPktDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitPktDirection.setStatus(_A)
class _FsIfQosFlowLimitCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_FsIfQosFlowLimitCIR_Type.__name__=_D
_FsIfQosFlowLimitCIR_Object=MibTableColumn
fsIfQosFlowLimitCIR=_FsIfQosFlowLimitCIR_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,3),_FsIfQosFlowLimitCIR_Type())
fsIfQosFlowLimitCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitCIR.setStatus(_A)
class _FsIfQosFlowLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_FsIfQosFlowLimitBurstSize_Type.__name__=_D
_FsIfQosFlowLimitBurstSize_Object=MibTableColumn
fsIfQosFlowLimitBurstSize=_FsIfQosFlowLimitBurstSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,4),_FsIfQosFlowLimitBurstSize_Type())
fsIfQosFlowLimitBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitBurstSize.setStatus(_A)
class _FsIfQosFlowLimitExcessBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_FsIfQosFlowLimitExcessBurstSize_Type.__name__=_D
_FsIfQosFlowLimitExcessBurstSize_Object=MibTableColumn
fsIfQosFlowLimitExcessBurstSize=_FsIfQosFlowLimitExcessBurstSize_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,5),_FsIfQosFlowLimitExcessBurstSize_Type())
fsIfQosFlowLimitExcessBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitExcessBurstSize.setStatus(_A)
class _FsIfQosFlowLimitConformAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_FsIfQosFlowLimitConformAction_Type.__name__=_D
_FsIfQosFlowLimitConformAction_Object=MibTableColumn
fsIfQosFlowLimitConformAction=_FsIfQosFlowLimitConformAction_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,6),_FsIfQosFlowLimitConformAction_Type())
fsIfQosFlowLimitConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitConformAction.setStatus(_A)
class _FsIfQosFlowLimitExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_FsIfQosFlowLimitExceedAction_Type.__name__=_D
_FsIfQosFlowLimitExceedAction_Object=MibTableColumn
fsIfQosFlowLimitExceedAction=_FsIfQosFlowLimitExceedAction_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,7),_FsIfQosFlowLimitExceedAction_Type())
fsIfQosFlowLimitExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitExceedAction.setStatus(_A)
class _FsIfQosFlowLimitConformNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsIfQosFlowLimitConformNewPrec_Type.__name__=_D
_FsIfQosFlowLimitConformNewPrec_Object=MibTableColumn
fsIfQosFlowLimitConformNewPrec=_FsIfQosFlowLimitConformNewPrec_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,8),_FsIfQosFlowLimitConformNewPrec_Type())
fsIfQosFlowLimitConformNewPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitConformNewPrec.setStatus(_A)
class _FsIfQosFlowLimitExceedNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsIfQosFlowLimitExceedNewPrec_Type.__name__=_D
_FsIfQosFlowLimitExceedNewPrec_Object=MibTableColumn
fsIfQosFlowLimitExceedNewPrec=_FsIfQosFlowLimitExceedNewPrec_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,9),_FsIfQosFlowLimitExceedNewPrec_Type())
fsIfQosFlowLimitExceedNewPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitExceedNewPrec.setStatus(_A)
_FsIfQosFlowLimitConformPkt_Type=Counter32
_FsIfQosFlowLimitConformPkt_Object=MibTableColumn
fsIfQosFlowLimitConformPkt=_FsIfQosFlowLimitConformPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,10),_FsIfQosFlowLimitConformPkt_Type())
fsIfQosFlowLimitConformPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitConformPkt.setStatus(_A)
_FsIfQosFlowLimitConformByte_Type=Counter32
_FsIfQosFlowLimitConformByte_Object=MibTableColumn
fsIfQosFlowLimitConformByte=_FsIfQosFlowLimitConformByte_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,11),_FsIfQosFlowLimitConformByte_Type())
fsIfQosFlowLimitConformByte.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitConformByte.setStatus(_A)
_FsIfQosFlowLimitExceedPkt_Type=Counter32
_FsIfQosFlowLimitExceedPkt_Object=MibTableColumn
fsIfQosFlowLimitExceedPkt=_FsIfQosFlowLimitExceedPkt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,12),_FsIfQosFlowLimitExceedPkt_Type())
fsIfQosFlowLimitExceedPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitExceedPkt.setStatus(_A)
_FsIfQosFlowLimitExceedByte_Type=Counter32
_FsIfQosFlowLimitExceedByte_Object=MibTableColumn
fsIfQosFlowLimitExceedByte=_FsIfQosFlowLimitExceedByte_Object((1,3,6,1,4,1,52642,1,1,10,2,106,2,8,1,13),_FsIfQosFlowLimitExceedByte_Type())
fsIfQosFlowLimitExceedByte.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIfQosFlowLimitExceedByte.setStatus(_A)
_FsHQoSMIBObjects_ObjectIdentity=ObjectIdentity
fsHQoSMIBObjects=_FsHQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3))
_FsHQoSScalarObjects_ObjectIdentity=ObjectIdentity
fsHQoSScalarObjects=_FsHQoSScalarObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,1))
class _FsHQoSNameType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknownName',0),('userQNameIn',1),('userQNameOut',2),('userGroupQInName',3),('userGroupQOutName',4),('flowQName',5),('flowMapName',6),('trafficClassifierName',7),('trafficBehaviorName',8),('trafficPolicyName',9),('portQName',10)))
_FsHQoSNameType_Type.__name__=_D
_FsHQoSNameType_Object=MibScalar
fsHQoSNameType=_FsHQoSNameType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,1,1),_FsHQoSNameType_Type())
fsHQoSNameType.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSNameType.setStatus(_A)
class _FsHQoSNameFind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSNameFind_Type.__name__=_F
_FsHQoSNameFind_Object=MibScalar
fsHQoSNameFind=_FsHQoSNameFind_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,1,2),_FsHQoSNameFind_Type())
fsHQoSNameFind.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSNameFind.setStatus(_A)
class _FsHQoSNameIndex_Type(Integer32):defaultValue=0
_FsHQoSNameIndex_Type.__name__=_D
_FsHQoSNameIndex_Object=MibScalar
fsHQoSNameIndex=_FsHQoSNameIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,1,3),_FsHQoSNameIndex_Type())
fsHQoSNameIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSNameIndex.setStatus(_A)
_FsHQoSUserQObjects_ObjectIdentity=ObjectIdentity
fsHQoSUserQObjects=_FsHQoSUserQObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,2))
_FsHQoSUserQInIndexNext_Type=Integer32
_FsHQoSUserQInIndexNext_Object=MibScalar
fsHQoSUserQInIndexNext=_FsHQoSUserQInIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,1),_FsHQoSUserQInIndexNext_Type())
fsHQoSUserQInIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserQInIndexNext.setStatus(_A)
_FsHQoSUserQOutIndexNext_Type=Integer32
_FsHQoSUserQOutIndexNext_Object=MibScalar
fsHQoSUserQOutIndexNext=_FsHQoSUserQOutIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,2),_FsHQoSUserQOutIndexNext_Type())
fsHQoSUserQOutIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserQOutIndexNext.setStatus(_A)
_FsHQoSUserQTable_Object=MibTable
fsHQoSUserQTable=_FsHQoSUserQTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3))
if mibBuilder.loadTexts:fsHQoSUserQTable.setStatus(_A)
_FsHQoSUserQEntry_Object=MibTableRow
fsHQoSUserQEntry=_FsHQoSUserQEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1))
fsHQoSUserQEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:fsHQoSUserQEntry.setStatus(_A)
_FsHQoSUserQIndex_Type=Unsigned32
_FsHQoSUserQIndex_Object=MibTableColumn
fsHQoSUserQIndex=_FsHQoSUserQIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,1),_FsHQoSUserQIndex_Type())
fsHQoSUserQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSUserQIndex.setStatus(_A)
class _FsHQoSUserQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSUserQName_Type.__name__=_F
_FsHQoSUserQName_Object=MibTableColumn
fsHQoSUserQName=_FsHQoSUserQName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,2),_FsHQoSUserQName_Type())
fsHQoSUserQName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQName.setStatus(_A)
_FsHQoSUserQDirection_Type=FSQDirectionType
_FsHQoSUserQDirection_Object=MibTableColumn
fsHQoSUserQDirection=_FsHQoSUserQDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,3),_FsHQoSUserQDirection_Type())
fsHQoSUserQDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQDirection.setStatus(_A)
_FsHQoSUserQRowStatus_Type=RowStatus
_FsHQoSUserQRowStatus_Object=MibTableColumn
fsHQoSUserQRowStatus=_FsHQoSUserQRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,4),_FsHQoSUserQRowStatus_Type())
fsHQoSUserQRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQRowStatus.setStatus(_A)
class _FsHQoSUserQFlowQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSUserQFlowQName_Type.__name__=_F
_FsHQoSUserQFlowQName_Object=MibTableColumn
fsHQoSUserQFlowQName=_FsHQoSUserQFlowQName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,5),_FsHQoSUserQFlowQName_Type())
fsHQoSUserQFlowQName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQFlowQName.setStatus(_A)
_FsHQoSUserQFlowQIndex_Type=Unsigned32
_FsHQoSUserQFlowQIndex_Object=MibTableColumn
fsHQoSUserQFlowQIndex=_FsHQoSUserQFlowQIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,6),_FsHQoSUserQFlowQIndex_Type())
fsHQoSUserQFlowQIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserQFlowQIndex.setStatus(_A)
class _FsHQoSUserQGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSUserQGroupName_Type.__name__=_F
_FsHQoSUserQGroupName_Object=MibTableColumn
fsHQoSUserQGroupName=_FsHQoSUserQGroupName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,7),_FsHQoSUserQGroupName_Type())
fsHQoSUserQGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQGroupName.setStatus(_A)
_FsHQoSUserQGroupIndex_Type=Unsigned32
_FsHQoSUserQGroupIndex_Object=MibTableColumn
fsHQoSUserQGroupIndex=_FsHQoSUserQGroupIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,8),_FsHQoSUserQGroupIndex_Type())
fsHQoSUserQGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserQGroupIndex.setStatus(_A)
class _FsHQoSUserQFlowMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSUserQFlowMapName_Type.__name__=_F
_FsHQoSUserQFlowMapName_Object=MibTableColumn
fsHQoSUserQFlowMapName=_FsHQoSUserQFlowMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,9),_FsHQoSUserQFlowMapName_Type())
fsHQoSUserQFlowMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQFlowMapName.setStatus(_A)
_FsHQoSUserQFlowMapIndex_Type=Unsigned32
_FsHQoSUserQFlowMapIndex_Object=MibTableColumn
fsHQoSUserQFlowMapIndex=_FsHQoSUserQFlowMapIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,10),_FsHQoSUserQFlowMapIndex_Type())
fsHQoSUserQFlowMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserQFlowMapIndex.setStatus(_A)
class _FsHQoSUserQCIR_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSUserQCIR_Type.__name__=_M
_FsHQoSUserQCIR_Object=MibTableColumn
fsHQoSUserQCIR=_FsHQoSUserQCIR_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,11),_FsHQoSUserQCIR_Type())
fsHQoSUserQCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQCIR.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSUserQCIR.setUnits(_G)
class _FsHQoSUserQPIR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_FsHQoSUserQPIR_Type.__name__=_M
_FsHQoSUserQPIR_Object=MibTableColumn
fsHQoSUserQPIR=_FsHQoSUserQPIR_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,2,3,1,12),_FsHQoSUserQPIR_Type())
fsHQoSUserQPIR.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserQPIR.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSUserQPIR.setUnits(_G)
_FsHQoSUserGroupQObjects_ObjectIdentity=ObjectIdentity
fsHQoSUserGroupQObjects=_FsHQoSUserGroupQObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,3))
_FsHQoSUserGroupQInIndexNext_Type=Integer32
_FsHQoSUserGroupQInIndexNext_Object=MibScalar
fsHQoSUserGroupQInIndexNext=_FsHQoSUserGroupQInIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,1),_FsHQoSUserGroupQInIndexNext_Type())
fsHQoSUserGroupQInIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserGroupQInIndexNext.setStatus(_A)
_FsHQoSUserGroupQOutIndexNext_Type=Integer32
_FsHQoSUserGroupQOutIndexNext_Object=MibScalar
fsHQoSUserGroupQOutIndexNext=_FsHQoSUserGroupQOutIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,2),_FsHQoSUserGroupQOutIndexNext_Type())
fsHQoSUserGroupQOutIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSUserGroupQOutIndexNext.setStatus(_A)
_FsHQoSUserGroupQTable_Object=MibTable
fsHQoSUserGroupQTable=_FsHQoSUserGroupQTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3))
if mibBuilder.loadTexts:fsHQoSUserGroupQTable.setStatus(_A)
_FsHQoSUserGroupQEntry_Object=MibTableRow
fsHQoSUserGroupQEntry=_FsHQoSUserGroupQEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3,1))
fsHQoSUserGroupQEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:fsHQoSUserGroupQEntry.setStatus(_A)
_FsHQoSUserGroupQIndex_Type=Unsigned32
_FsHQoSUserGroupQIndex_Object=MibTableColumn
fsHQoSUserGroupQIndex=_FsHQoSUserGroupQIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3,1,1),_FsHQoSUserGroupQIndex_Type())
fsHQoSUserGroupQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSUserGroupQIndex.setStatus(_A)
class _FsHQoSUserGroupQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSUserGroupQName_Type.__name__=_F
_FsHQoSUserGroupQName_Object=MibTableColumn
fsHQoSUserGroupQName=_FsHQoSUserGroupQName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3,1,2),_FsHQoSUserGroupQName_Type())
fsHQoSUserGroupQName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserGroupQName.setStatus(_A)
_FsHQoSUserGroupQDirection_Type=FSQDirectionType
_FsHQoSUserGroupQDirection_Object=MibTableColumn
fsHQoSUserGroupQDirection=_FsHQoSUserGroupQDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3,1,3),_FsHQoSUserGroupQDirection_Type())
fsHQoSUserGroupQDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserGroupQDirection.setStatus(_A)
_FsHQoSUserGroupQRowStatus_Type=RowStatus
_FsHQoSUserGroupQRowStatus_Object=MibTableColumn
fsHQoSUserGroupQRowStatus=_FsHQoSUserGroupQRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3,1,4),_FsHQoSUserGroupQRowStatus_Type())
fsHQoSUserGroupQRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserGroupQRowStatus.setStatus(_A)
class _FsHQoSUserGroupQShaping_Type(Unsigned32):defaultValue=10000000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSUserGroupQShaping_Type.__name__=_M
_FsHQoSUserGroupQShaping_Object=MibTableColumn
fsHQoSUserGroupQShaping=_FsHQoSUserGroupQShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,3,3,1,5),_FsHQoSUserGroupQShaping_Type())
fsHQoSUserGroupQShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSUserGroupQShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSUserGroupQShaping.setUnits(_G)
_FsHQoSFlowQObjects_ObjectIdentity=ObjectIdentity
fsHQoSFlowQObjects=_FsHQoSFlowQObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,4))
_FsHQoSFlowQIndexNext_Type=Integer32
_FsHQoSFlowQIndexNext_Object=MibScalar
fsHQoSFlowQIndexNext=_FsHQoSFlowQIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,1),_FsHQoSFlowQIndexNext_Type())
fsHQoSFlowQIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSFlowQIndexNext.setStatus(_A)
_FsHQoSFlowQTable_Object=MibTable
fsHQoSFlowQTable=_FsHQoSFlowQTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2))
if mibBuilder.loadTexts:fsHQoSFlowQTable.setStatus(_A)
_FsHQoSFlowQEntry_Object=MibTableRow
fsHQoSFlowQEntry=_FsHQoSFlowQEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1))
fsHQoSFlowQEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:fsHQoSFlowQEntry.setStatus(_A)
_FsHQoSFlowQIndex_Type=Unsigned32
_FsHQoSFlowQIndex_Object=MibTableColumn
fsHQoSFlowQIndex=_FsHQoSFlowQIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,1),_FsHQoSFlowQIndex_Type())
fsHQoSFlowQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSFlowQIndex.setStatus(_A)
class _FsHQoSFlowQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQName_Type.__name__=_F
_FsHQoSFlowQName_Object=MibTableColumn
fsHQoSFlowQName=_FsHQoSFlowQName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,2),_FsHQoSFlowQName_Type())
fsHQoSFlowQName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQName.setStatus(_A)
_FsHQoSFlowQRowStatus_Type=RowStatus
_FsHQoSFlowQRowStatus_Object=MibTableColumn
fsHQoSFlowQRowStatus=_FsHQoSFlowQRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,3),_FsHQoSFlowQRowStatus_Type())
fsHQoSFlowQRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQRowStatus.setStatus(_A)
class _FsHQoSFlowQBEQType_Type(FSQType):defaultValue=2
_FsHQoSFlowQBEQType_Type.__name__=_H
_FsHQoSFlowQBEQType_Object=MibTableColumn
fsHQoSFlowQBEQType=_FsHQoSFlowQBEQType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,4),_FsHQoSFlowQBEQType_Type())
fsHQoSFlowQBEQType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQBEQType.setStatus(_A)
class _FsHQoSFlowQBEQWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQBEQWredWeight_Type.__name__=_D
_FsHQoSFlowQBEQWredWeight_Object=MibTableColumn
fsHQoSFlowQBEQWredWeight=_FsHQoSFlowQBEQWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,5),_FsHQoSFlowQBEQWredWeight_Type())
fsHQoSFlowQBEQWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQBEQWredWeight.setStatus(_A)
class _FsHQoSFlowQBEQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQBEQWredName_Type.__name__=_F
_FsHQoSFlowQBEQWredName_Object=MibTableColumn
fsHQoSFlowQBEQWredName=_FsHQoSFlowQBEQWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,6),_FsHQoSFlowQBEQWredName_Type())
fsHQoSFlowQBEQWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQBEQWredName.setStatus(_A)
class _FsHQoSFlowQBEQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQBEQDepth_Type.__name__=_D
_FsHQoSFlowQBEQDepth_Object=MibTableColumn
fsHQoSFlowQBEQDepth=_FsHQoSFlowQBEQDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,7),_FsHQoSFlowQBEQDepth_Type())
fsHQoSFlowQBEQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQBEQDepth.setStatus(_A)
class _FsHQoSFlowQBEQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQBEQShaping_Type.__name__=_D
_FsHQoSFlowQBEQShaping_Object=MibTableColumn
fsHQoSFlowQBEQShaping=_FsHQoSFlowQBEQShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,8),_FsHQoSFlowQBEQShaping_Type())
fsHQoSFlowQBEQShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQBEQShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQBEQShaping.setUnits(_G)
class _FsHQoSFlowQAF1QType_Type(FSQType):defaultValue=2
_FsHQoSFlowQAF1QType_Type.__name__=_H
_FsHQoSFlowQAF1QType_Object=MibTableColumn
fsHQoSFlowQAF1QType=_FsHQoSFlowQAF1QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,9),_FsHQoSFlowQAF1QType_Type())
fsHQoSFlowQAF1QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF1QType.setStatus(_A)
class _FsHQoSFlowQAF1QWredWeight_Type(Integer32):defaultValue=10
_FsHQoSFlowQAF1QWredWeight_Type.__name__=_D
_FsHQoSFlowQAF1QWredWeight_Object=MibTableColumn
fsHQoSFlowQAF1QWredWeight=_FsHQoSFlowQAF1QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,10),_FsHQoSFlowQAF1QWredWeight_Type())
fsHQoSFlowQAF1QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF1QWredWeight.setStatus(_A)
class _FsHQoSFlowQAF1QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQAF1QWredName_Type.__name__=_F
_FsHQoSFlowQAF1QWredName_Object=MibTableColumn
fsHQoSFlowQAF1QWredName=_FsHQoSFlowQAF1QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,11),_FsHQoSFlowQAF1QWredName_Type())
fsHQoSFlowQAF1QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF1QWredName.setStatus(_A)
class _FsHQoSFlowQAF1QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQAF1QDepth_Type.__name__=_D
_FsHQoSFlowQAF1QDepth_Object=MibTableColumn
fsHQoSFlowQAF1QDepth=_FsHQoSFlowQAF1QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,12),_FsHQoSFlowQAF1QDepth_Type())
fsHQoSFlowQAF1QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF1QDepth.setStatus(_A)
class _FsHQoSFlowQAF1QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQAF1QShaping_Type.__name__=_D
_FsHQoSFlowQAF1QShaping_Object=MibTableColumn
fsHQoSFlowQAF1QShaping=_FsHQoSFlowQAF1QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,13),_FsHQoSFlowQAF1QShaping_Type())
fsHQoSFlowQAF1QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF1QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQAF1QShaping.setUnits(_G)
class _FsHQoSFlowQAF2QType_Type(FSQType):defaultValue=2
_FsHQoSFlowQAF2QType_Type.__name__=_H
_FsHQoSFlowQAF2QType_Object=MibTableColumn
fsHQoSFlowQAF2QType=_FsHQoSFlowQAF2QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,14),_FsHQoSFlowQAF2QType_Type())
fsHQoSFlowQAF2QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF2QType.setStatus(_A)
class _FsHQoSFlowQAF2QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQAF2QWredWeight_Type.__name__=_D
_FsHQoSFlowQAF2QWredWeight_Object=MibTableColumn
fsHQoSFlowQAF2QWredWeight=_FsHQoSFlowQAF2QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,15),_FsHQoSFlowQAF2QWredWeight_Type())
fsHQoSFlowQAF2QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF2QWredWeight.setStatus(_A)
class _FsHQoSFlowQAF2QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQAF2QWredName_Type.__name__=_F
_FsHQoSFlowQAF2QWredName_Object=MibTableColumn
fsHQoSFlowQAF2QWredName=_FsHQoSFlowQAF2QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,16),_FsHQoSFlowQAF2QWredName_Type())
fsHQoSFlowQAF2QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF2QWredName.setStatus(_A)
class _FsHQoSFlowQAF2QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQAF2QDepth_Type.__name__=_D
_FsHQoSFlowQAF2QDepth_Object=MibTableColumn
fsHQoSFlowQAF2QDepth=_FsHQoSFlowQAF2QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,17),_FsHQoSFlowQAF2QDepth_Type())
fsHQoSFlowQAF2QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF2QDepth.setStatus(_A)
class _FsHQoSFlowQAF2QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQAF2QShaping_Type.__name__=_D
_FsHQoSFlowQAF2QShaping_Object=MibTableColumn
fsHQoSFlowQAF2QShaping=_FsHQoSFlowQAF2QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,18),_FsHQoSFlowQAF2QShaping_Type())
fsHQoSFlowQAF2QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF2QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQAF2QShaping.setUnits(_G)
class _FsHQoSFlowQAF3QType_Type(FSQType):defaultValue=2
_FsHQoSFlowQAF3QType_Type.__name__=_H
_FsHQoSFlowQAF3QType_Object=MibTableColumn
fsHQoSFlowQAF3QType=_FsHQoSFlowQAF3QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,19),_FsHQoSFlowQAF3QType_Type())
fsHQoSFlowQAF3QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QType.setStatus(_A)
class _FsHQoSFlowQAF3QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQAF3QWredWeight_Type.__name__=_D
_FsHQoSFlowQAF3QWredWeight_Object=MibTableColumn
fsHQoSFlowQAF3QWredWeight=_FsHQoSFlowQAF3QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,20),_FsHQoSFlowQAF3QWredWeight_Type())
fsHQoSFlowQAF3QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QWredWeight.setStatus(_A)
class _FsHQoSFlowQAF3QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQAF3QWredName_Type.__name__=_F
_FsHQoSFlowQAF3QWredName_Object=MibTableColumn
fsHQoSFlowQAF3QWredName=_FsHQoSFlowQAF3QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,21),_FsHQoSFlowQAF3QWredName_Type())
fsHQoSFlowQAF3QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QWredName.setStatus(_A)
class _FsHQoSFlowQAF3QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQAF3QDepth_Type.__name__=_D
_FsHQoSFlowQAF3QDepth_Object=MibTableColumn
fsHQoSFlowQAF3QDepth=_FsHQoSFlowQAF3QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,22),_FsHQoSFlowQAF3QDepth_Type())
fsHQoSFlowQAF3QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QDepth.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QDepth.setUnits(_G)
class _FsHQoSFlowQAF3QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQAF3QShaping_Type.__name__=_D
_FsHQoSFlowQAF3QShaping_Object=MibTableColumn
fsHQoSFlowQAF3QShaping=_FsHQoSFlowQAF3QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,23),_FsHQoSFlowQAF3QShaping_Type())
fsHQoSFlowQAF3QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQAF3QShaping.setUnits(_G)
class _FsHQoSFlowQAF4QType_Type(FSQType):defaultValue=2
_FsHQoSFlowQAF4QType_Type.__name__=_H
_FsHQoSFlowQAF4QType_Object=MibTableColumn
fsHQoSFlowQAF4QType=_FsHQoSFlowQAF4QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,24),_FsHQoSFlowQAF4QType_Type())
fsHQoSFlowQAF4QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF4QType.setStatus(_A)
class _FsHQoSFlowQAF4QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQAF4QWredWeight_Type.__name__=_D
_FsHQoSFlowQAF4QWredWeight_Object=MibTableColumn
fsHQoSFlowQAF4QWredWeight=_FsHQoSFlowQAF4QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,25),_FsHQoSFlowQAF4QWredWeight_Type())
fsHQoSFlowQAF4QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF4QWredWeight.setStatus(_A)
class _FsHQoSFlowQAF4QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQAF4QWredName_Type.__name__=_F
_FsHQoSFlowQAF4QWredName_Object=MibTableColumn
fsHQoSFlowQAF4QWredName=_FsHQoSFlowQAF4QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,26),_FsHQoSFlowQAF4QWredName_Type())
fsHQoSFlowQAF4QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF4QWredName.setStatus(_A)
class _FsHQoSFlowQAF4QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQAF4QDepth_Type.__name__=_D
_FsHQoSFlowQAF4QDepth_Object=MibTableColumn
fsHQoSFlowQAF4QDepth=_FsHQoSFlowQAF4QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,27),_FsHQoSFlowQAF4QDepth_Type())
fsHQoSFlowQAF4QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF4QDepth.setStatus(_A)
class _FsHQoSFlowQAF4QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_FsHQoSFlowQAF4QShaping_Type.__name__=_D
_FsHQoSFlowQAF4QShaping_Object=MibTableColumn
fsHQoSFlowQAF4QShaping=_FsHQoSFlowQAF4QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,28),_FsHQoSFlowQAF4QShaping_Type())
fsHQoSFlowQAF4QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQAF4QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQAF4QShaping.setUnits(_G)
class _FsHQoSFlowQEFQType_Type(FSQType):defaultValue=3
_FsHQoSFlowQEFQType_Type.__name__=_H
_FsHQoSFlowQEFQType_Object=MibTableColumn
fsHQoSFlowQEFQType=_FsHQoSFlowQEFQType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,29),_FsHQoSFlowQEFQType_Type())
fsHQoSFlowQEFQType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQEFQType.setStatus(_A)
class _FsHQoSFlowQEFQWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQEFQWredWeight_Type.__name__=_D
_FsHQoSFlowQEFQWredWeight_Object=MibTableColumn
fsHQoSFlowQEFQWredWeight=_FsHQoSFlowQEFQWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,30),_FsHQoSFlowQEFQWredWeight_Type())
fsHQoSFlowQEFQWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQEFQWredWeight.setStatus(_A)
class _FsHQoSFlowQEFQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQEFQWredName_Type.__name__=_F
_FsHQoSFlowQEFQWredName_Object=MibTableColumn
fsHQoSFlowQEFQWredName=_FsHQoSFlowQEFQWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,31),_FsHQoSFlowQEFQWredName_Type())
fsHQoSFlowQEFQWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQEFQWredName.setStatus(_A)
class _FsHQoSFlowQEFQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQEFQDepth_Type.__name__=_D
_FsHQoSFlowQEFQDepth_Object=MibTableColumn
fsHQoSFlowQEFQDepth=_FsHQoSFlowQEFQDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,32),_FsHQoSFlowQEFQDepth_Type())
fsHQoSFlowQEFQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQEFQDepth.setStatus(_A)
class _FsHQoSFlowQEFQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQEFQShaping_Type.__name__=_D
_FsHQoSFlowQEFQShaping_Object=MibTableColumn
fsHQoSFlowQEFQShaping=_FsHQoSFlowQEFQShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,33),_FsHQoSFlowQEFQShaping_Type())
fsHQoSFlowQEFQShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQEFQShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQEFQShaping.setUnits(_G)
class _FsHQoSFlowQCS6QType_Type(FSQType):defaultValue=3
_FsHQoSFlowQCS6QType_Type.__name__=_H
_FsHQoSFlowQCS6QType_Object=MibTableColumn
fsHQoSFlowQCS6QType=_FsHQoSFlowQCS6QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,34),_FsHQoSFlowQCS6QType_Type())
fsHQoSFlowQCS6QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS6QType.setStatus(_A)
class _FsHQoSFlowQCS6QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQCS6QWredWeight_Type.__name__=_D
_FsHQoSFlowQCS6QWredWeight_Object=MibTableColumn
fsHQoSFlowQCS6QWredWeight=_FsHQoSFlowQCS6QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,35),_FsHQoSFlowQCS6QWredWeight_Type())
fsHQoSFlowQCS6QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS6QWredWeight.setStatus(_A)
class _FsHQoSFlowQCS6QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQCS6QWredName_Type.__name__=_F
_FsHQoSFlowQCS6QWredName_Object=MibTableColumn
fsHQoSFlowQCS6QWredName=_FsHQoSFlowQCS6QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,36),_FsHQoSFlowQCS6QWredName_Type())
fsHQoSFlowQCS6QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS6QWredName.setStatus(_A)
class _FsHQoSFlowQCS6QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQCS6QDepth_Type.__name__=_D
_FsHQoSFlowQCS6QDepth_Object=MibTableColumn
fsHQoSFlowQCS6QDepth=_FsHQoSFlowQCS6QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,37),_FsHQoSFlowQCS6QDepth_Type())
fsHQoSFlowQCS6QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS6QDepth.setStatus(_A)
class _FsHQoSFlowQCS6QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQCS6QShaping_Type.__name__=_D
_FsHQoSFlowQCS6QShaping_Object=MibTableColumn
fsHQoSFlowQCS6QShaping=_FsHQoSFlowQCS6QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,38),_FsHQoSFlowQCS6QShaping_Type())
fsHQoSFlowQCS6QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS6QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQCS6QShaping.setUnits(_G)
class _FsHQoSFlowQCS7QType_Type(FSQType):defaultValue=3
_FsHQoSFlowQCS7QType_Type.__name__=_H
_FsHQoSFlowQCS7QType_Object=MibTableColumn
fsHQoSFlowQCS7QType=_FsHQoSFlowQCS7QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,39),_FsHQoSFlowQCS7QType_Type())
fsHQoSFlowQCS7QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS7QType.setStatus(_A)
class _FsHQoSFlowQCS7QWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSFlowQCS7QWredWeight_Type.__name__=_D
_FsHQoSFlowQCS7QWredWeight_Object=MibTableColumn
fsHQoSFlowQCS7QWredWeight=_FsHQoSFlowQCS7QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,40),_FsHQoSFlowQCS7QWredWeight_Type())
fsHQoSFlowQCS7QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS7QWredWeight.setStatus(_A)
class _FsHQoSFlowQCS7QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowQCS7QWredName_Type.__name__=_F
_FsHQoSFlowQCS7QWredName_Object=MibTableColumn
fsHQoSFlowQCS7QWredName=_FsHQoSFlowQCS7QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,41),_FsHQoSFlowQCS7QWredName_Type())
fsHQoSFlowQCS7QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS7QWredName.setStatus(_A)
class _FsHQoSFlowQCS7QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSFlowQCS7QDepth_Type.__name__=_D
_FsHQoSFlowQCS7QDepth_Object=MibTableColumn
fsHQoSFlowQCS7QDepth=_FsHQoSFlowQCS7QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,42),_FsHQoSFlowQCS7QDepth_Type())
fsHQoSFlowQCS7QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS7QDepth.setStatus(_A)
class _FsHQoSFlowQCS7QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSFlowQCS7QShaping_Type.__name__=_D
_FsHQoSFlowQCS7QShaping_Object=MibTableColumn
fsHQoSFlowQCS7QShaping=_FsHQoSFlowQCS7QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,4,2,1,43),_FsHQoSFlowQCS7QShaping_Type())
fsHQoSFlowQCS7QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowQCS7QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSFlowQCS7QShaping.setUnits(_G)
_FsHQoSFlowMapObjects_ObjectIdentity=ObjectIdentity
fsHQoSFlowMapObjects=_FsHQoSFlowMapObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,5))
_FsHQoSFlowMapIndexNext_Type=Integer32
_FsHQoSFlowMapIndexNext_Object=MibScalar
fsHQoSFlowMapIndexNext=_FsHQoSFlowMapIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,1),_FsHQoSFlowMapIndexNext_Type())
fsHQoSFlowMapIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSFlowMapIndexNext.setStatus(_A)
_FsHQoSFlowMapTable_Object=MibTable
fsHQoSFlowMapTable=_FsHQoSFlowMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2))
if mibBuilder.loadTexts:fsHQoSFlowMapTable.setStatus(_A)
_FsHQoSFlowMapEntry_Object=MibTableRow
fsHQoSFlowMapEntry=_FsHQoSFlowMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1))
fsHQoSFlowMapEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:fsHQoSFlowMapEntry.setStatus(_A)
_FsHQoSFlowMapIndex_Type=Unsigned32
_FsHQoSFlowMapIndex_Object=MibTableColumn
fsHQoSFlowMapIndex=_FsHQoSFlowMapIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,1),_FsHQoSFlowMapIndex_Type())
fsHQoSFlowMapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSFlowMapIndex.setStatus(_A)
class _FsHQoSFlowMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSFlowMapName_Type.__name__=_F
_FsHQoSFlowMapName_Object=MibTableColumn
fsHQoSFlowMapName=_FsHQoSFlowMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,2),_FsHQoSFlowMapName_Type())
fsHQoSFlowMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapName.setStatus(_A)
_FsHQoSFlowMapRowStatus_Type=RowStatus
_FsHQoSFlowMapRowStatus_Object=MibTableColumn
fsHQoSFlowMapRowStatus=_FsHQoSFlowMapRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,3),_FsHQoSFlowMapRowStatus_Type())
fsHQoSFlowMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapRowStatus.setStatus(_A)
class _FsHQoSFlowMapBEQ2PortQ_Type(FSCosType):defaultValue=1
_FsHQoSFlowMapBEQ2PortQ_Type.__name__=_K
_FsHQoSFlowMapBEQ2PortQ_Object=MibTableColumn
fsHQoSFlowMapBEQ2PortQ=_FsHQoSFlowMapBEQ2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,4),_FsHQoSFlowMapBEQ2PortQ_Type())
fsHQoSFlowMapBEQ2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapBEQ2PortQ.setStatus(_A)
class _FsHQoSFlowMapAF1Q2PortQ_Type(FSCosType):defaultValue=2
_FsHQoSFlowMapAF1Q2PortQ_Type.__name__=_K
_FsHQoSFlowMapAF1Q2PortQ_Object=MibTableColumn
fsHQoSFlowMapAF1Q2PortQ=_FsHQoSFlowMapAF1Q2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,5),_FsHQoSFlowMapAF1Q2PortQ_Type())
fsHQoSFlowMapAF1Q2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapAF1Q2PortQ.setStatus(_A)
class _FsHQoSFlowMapAF2Q2PortQ_Type(FSCosType):defaultValue=3
_FsHQoSFlowMapAF2Q2PortQ_Type.__name__=_K
_FsHQoSFlowMapAF2Q2PortQ_Object=MibTableColumn
fsHQoSFlowMapAF2Q2PortQ=_FsHQoSFlowMapAF2Q2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,6),_FsHQoSFlowMapAF2Q2PortQ_Type())
fsHQoSFlowMapAF2Q2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapAF2Q2PortQ.setStatus(_A)
class _FsHQoSFlowMapAF3Q2PortQ_Type(FSCosType):defaultValue=4
_FsHQoSFlowMapAF3Q2PortQ_Type.__name__=_K
_FsHQoSFlowMapAF3Q2PortQ_Object=MibTableColumn
fsHQoSFlowMapAF3Q2PortQ=_FsHQoSFlowMapAF3Q2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,7),_FsHQoSFlowMapAF3Q2PortQ_Type())
fsHQoSFlowMapAF3Q2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapAF3Q2PortQ.setStatus(_A)
class _FsHQoSFlowMapAF4Q2PortQ_Type(FSCosType):defaultValue=5
_FsHQoSFlowMapAF4Q2PortQ_Type.__name__=_K
_FsHQoSFlowMapAF4Q2PortQ_Object=MibTableColumn
fsHQoSFlowMapAF4Q2PortQ=_FsHQoSFlowMapAF4Q2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,8),_FsHQoSFlowMapAF4Q2PortQ_Type())
fsHQoSFlowMapAF4Q2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapAF4Q2PortQ.setStatus(_A)
class _FsHQoSFlowMapEFQ2PortQ_Type(FSCosType):defaultValue=6
_FsHQoSFlowMapEFQ2PortQ_Type.__name__=_K
_FsHQoSFlowMapEFQ2PortQ_Object=MibTableColumn
fsHQoSFlowMapEFQ2PortQ=_FsHQoSFlowMapEFQ2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,9),_FsHQoSFlowMapEFQ2PortQ_Type())
fsHQoSFlowMapEFQ2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapEFQ2PortQ.setStatus(_A)
class _FsHQoSFlowMapCS6Q2PortQ_Type(FSCosType):defaultValue=7
_FsHQoSFlowMapCS6Q2PortQ_Type.__name__=_K
_FsHQoSFlowMapCS6Q2PortQ_Object=MibTableColumn
fsHQoSFlowMapCS6Q2PortQ=_FsHQoSFlowMapCS6Q2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,10),_FsHQoSFlowMapCS6Q2PortQ_Type())
fsHQoSFlowMapCS6Q2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapCS6Q2PortQ.setStatus(_A)
class _FsHQoSFlowMapCS7Q2PortQ_Type(FSCosType):defaultValue=8
_FsHQoSFlowMapCS7Q2PortQ_Type.__name__=_K
_FsHQoSFlowMapCS7Q2PortQ_Object=MibTableColumn
fsHQoSFlowMapCS7Q2PortQ=_FsHQoSFlowMapCS7Q2PortQ_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,5,2,1,11),_FsHQoSFlowMapCS7Q2PortQ_Type())
fsHQoSFlowMapCS7Q2PortQ.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSFlowMapCS7Q2PortQ.setStatus(_A)
_FsHQoSTClassifierObjects_ObjectIdentity=ObjectIdentity
fsHQoSTClassifierObjects=_FsHQoSTClassifierObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,6))
_FsHQoSTClassifierIndexNext_Type=Integer32
_FsHQoSTClassifierIndexNext_Object=MibScalar
fsHQoSTClassifierIndexNext=_FsHQoSTClassifierIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,1),_FsHQoSTClassifierIndexNext_Type())
fsHQoSTClassifierIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSTClassifierIndexNext.setStatus(_A)
_FsHQoSTClassifierTable_Object=MibTable
fsHQoSTClassifierTable=_FsHQoSTClassifierTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2))
if mibBuilder.loadTexts:fsHQoSTClassifierTable.setStatus(_A)
_FsHQoSTClassifierEntry_Object=MibTableRow
fsHQoSTClassifierEntry=_FsHQoSTClassifierEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1))
fsHQoSTClassifierEntry.setIndexNames((0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:fsHQoSTClassifierEntry.setStatus(_A)
_FsHQoSTClassifierIndex_Type=Unsigned32
_FsHQoSTClassifierIndex_Object=MibTableColumn
fsHQoSTClassifierIndex=_FsHQoSTClassifierIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,1),_FsHQoSTClassifierIndex_Type())
fsHQoSTClassifierIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSTClassifierIndex.setStatus(_A)
_FsHQoSTClassifierInstance_Type=Unsigned32
_FsHQoSTClassifierInstance_Object=MibTableColumn
fsHQoSTClassifierInstance=_FsHQoSTClassifierInstance_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,2),_FsHQoSTClassifierInstance_Type())
fsHQoSTClassifierInstance.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSTClassifierInstance.setStatus(_A)
class _FsHQoSTClassifierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTClassifierName_Type.__name__=_F
_FsHQoSTClassifierName_Object=MibTableColumn
fsHQoSTClassifierName=_FsHQoSTClassifierName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,3),_FsHQoSTClassifierName_Type())
fsHQoSTClassifierName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierName.setStatus(_A)
class _FsHQoSTClassifierType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tc-or',1),('tc-and',2)))
_FsHQoSTClassifierType_Type.__name__=_D
_FsHQoSTClassifierType_Object=MibTableColumn
fsHQoSTClassifierType=_FsHQoSTClassifierType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,4),_FsHQoSTClassifierType_Type())
fsHQoSTClassifierType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierType.setStatus(_A)
_FsHQoSTClassifierRowStatus_Type=RowStatus
_FsHQoSTClassifierRowStatus_Object=MibTableColumn
fsHQoSTClassifierRowStatus=_FsHQoSTClassifierRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,5),_FsHQoSTClassifierRowStatus_Type())
fsHQoSTClassifierRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierRowStatus.setStatus(_A)
class _FsHQoSTClassifierMatchMask_Type(Bits):namedValues=NamedValues(*(('tc-v4-any',0),('tc-v4-aclID',1),('tc-v4-aclName',2),('tc-v4-dscp',3),('tc-v4-tos',4),('tc-v6-any',5),('tc-v6-aclID',6),('tc-v6-aclName',7),('tc-v6-dscp',8),('tc-vlan-cos',9),('tc-exp',10),('tc-srcmac',11),('tc-dstmac',12)))
_FsHQoSTClassifierMatchMask_Type.__name__=_Y
_FsHQoSTClassifierMatchMask_Object=MibTableColumn
fsHQoSTClassifierMatchMask=_FsHQoSTClassifierMatchMask_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,6),_FsHQoSTClassifierMatchMask_Type())
fsHQoSTClassifierMatchMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchMask.setStatus(_A)
class _FsHQoSTClassifierMatchV4Any_Type(TruthValue):defaultValue=2
_FsHQoSTClassifierMatchV4Any_Type.__name__=_O
_FsHQoSTClassifierMatchV4Any_Object=MibTableColumn
fsHQoSTClassifierMatchV4Any=_FsHQoSTClassifierMatchV4Any_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,7),_FsHQoSTClassifierMatchV4Any_Type())
fsHQoSTClassifierMatchV4Any.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV4Any.setStatus(_A)
class _FsHQoSTClassifierMatchV4AclID_Type(Integer32):defaultValue=0
_FsHQoSTClassifierMatchV4AclID_Type.__name__=_D
_FsHQoSTClassifierMatchV4AclID_Object=MibTableColumn
fsHQoSTClassifierMatchV4AclID=_FsHQoSTClassifierMatchV4AclID_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,8),_FsHQoSTClassifierMatchV4AclID_Type())
fsHQoSTClassifierMatchV4AclID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV4AclID.setStatus(_A)
class _FsHQoSTClassifierV4AclName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTClassifierV4AclName_Type.__name__=_F
_FsHQoSTClassifierV4AclName_Object=MibTableColumn
fsHQoSTClassifierV4AclName=_FsHQoSTClassifierV4AclName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,9),_FsHQoSTClassifierV4AclName_Type())
fsHQoSTClassifierV4AclName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierV4AclName.setStatus(_A)
class _FsHQoSTClassifierMatchV4Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsHQoSTClassifierMatchV4Dscp_Type.__name__=_D
_FsHQoSTClassifierMatchV4Dscp_Object=MibTableColumn
fsHQoSTClassifierMatchV4Dscp=_FsHQoSTClassifierMatchV4Dscp_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,10),_FsHQoSTClassifierMatchV4Dscp_Type())
fsHQoSTClassifierMatchV4Dscp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV4Dscp.setStatus(_A)
class _FsHQoSTClassifierMatchV4Tos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsHQoSTClassifierMatchV4Tos_Type.__name__=_D
_FsHQoSTClassifierMatchV4Tos_Object=MibTableColumn
fsHQoSTClassifierMatchV4Tos=_FsHQoSTClassifierMatchV4Tos_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,11),_FsHQoSTClassifierMatchV4Tos_Type())
fsHQoSTClassifierMatchV4Tos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV4Tos.setStatus(_A)
class _FsHQoSTClassifierMatchV6Any_Type(TruthValue):defaultValue=2
_FsHQoSTClassifierMatchV6Any_Type.__name__=_O
_FsHQoSTClassifierMatchV6Any_Object=MibTableColumn
fsHQoSTClassifierMatchV6Any=_FsHQoSTClassifierMatchV6Any_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,12),_FsHQoSTClassifierMatchV6Any_Type())
fsHQoSTClassifierMatchV6Any.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV6Any.setStatus(_A)
_FsHQoSTClassifierMatchV6AclID_Type=Integer32
_FsHQoSTClassifierMatchV6AclID_Object=MibTableColumn
fsHQoSTClassifierMatchV6AclID=_FsHQoSTClassifierMatchV6AclID_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,13),_FsHQoSTClassifierMatchV6AclID_Type())
fsHQoSTClassifierMatchV6AclID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV6AclID.setStatus(_A)
class _FsHQoSTClassifierV6AclName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTClassifierV6AclName_Type.__name__=_F
_FsHQoSTClassifierV6AclName_Object=MibTableColumn
fsHQoSTClassifierV6AclName=_FsHQoSTClassifierV6AclName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,14),_FsHQoSTClassifierV6AclName_Type())
fsHQoSTClassifierV6AclName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierV6AclName.setStatus(_A)
class _FsHQoSTClassifierMatchV6Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsHQoSTClassifierMatchV6Dscp_Type.__name__=_D
_FsHQoSTClassifierMatchV6Dscp_Object=MibTableColumn
fsHQoSTClassifierMatchV6Dscp=_FsHQoSTClassifierMatchV6Dscp_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,15),_FsHQoSTClassifierMatchV6Dscp_Type())
fsHQoSTClassifierMatchV6Dscp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchV6Dscp.setStatus(_A)
class _FsHQoSTClassifierMatchCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsHQoSTClassifierMatchCos_Type.__name__=_D
_FsHQoSTClassifierMatchCos_Object=MibTableColumn
fsHQoSTClassifierMatchCos=_FsHQoSTClassifierMatchCos_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,16),_FsHQoSTClassifierMatchCos_Type())
fsHQoSTClassifierMatchCos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchCos.setStatus(_A)
class _FsHQoSTClassifierMatchExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsHQoSTClassifierMatchExp_Type.__name__=_D
_FsHQoSTClassifierMatchExp_Object=MibTableColumn
fsHQoSTClassifierMatchExp=_FsHQoSTClassifierMatchExp_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,17),_FsHQoSTClassifierMatchExp_Type())
fsHQoSTClassifierMatchExp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchExp.setStatus(_A)
_FsHQoSTClassifierMatchSrcMac_Type=MacAddress
_FsHQoSTClassifierMatchSrcMac_Object=MibTableColumn
fsHQoSTClassifierMatchSrcMac=_FsHQoSTClassifierMatchSrcMac_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,18),_FsHQoSTClassifierMatchSrcMac_Type())
fsHQoSTClassifierMatchSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchSrcMac.setStatus(_A)
_FsHQoSTClassifierMatchDstMac_Type=MacAddress
_FsHQoSTClassifierMatchDstMac_Object=MibTableColumn
fsHQoSTClassifierMatchDstMac=_FsHQoSTClassifierMatchDstMac_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,6,2,1,19),_FsHQoSTClassifierMatchDstMac_Type())
fsHQoSTClassifierMatchDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTClassifierMatchDstMac.setStatus(_A)
_FsHQoSTBehaviorObjects_ObjectIdentity=ObjectIdentity
fsHQoSTBehaviorObjects=_FsHQoSTBehaviorObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,7))
_FsHQoSTBehaviorIndexNext_Type=Integer32
_FsHQoSTBehaviorIndexNext_Object=MibScalar
fsHQoSTBehaviorIndexNext=_FsHQoSTBehaviorIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,1),_FsHQoSTBehaviorIndexNext_Type())
fsHQoSTBehaviorIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSTBehaviorIndexNext.setStatus(_A)
_FsHQoSTBehaviorTable_Object=MibTable
fsHQoSTBehaviorTable=_FsHQoSTBehaviorTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2))
if mibBuilder.loadTexts:fsHQoSTBehaviorTable.setStatus(_A)
_FsHQoSTBehaviorEntry_Object=MibTableRow
fsHQoSTBehaviorEntry=_FsHQoSTBehaviorEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1))
fsHQoSTBehaviorEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:fsHQoSTBehaviorEntry.setStatus(_A)
_FsHQoSTBehaviorIndex_Type=Unsigned32
_FsHQoSTBehaviorIndex_Object=MibTableColumn
fsHQoSTBehaviorIndex=_FsHQoSTBehaviorIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,1),_FsHQoSTBehaviorIndex_Type())
fsHQoSTBehaviorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSTBehaviorIndex.setStatus(_A)
class _FsHQoSTBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTBehaviorName_Type.__name__=_F
_FsHQoSTBehaviorName_Object=MibTableColumn
fsHQoSTBehaviorName=_FsHQoSTBehaviorName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,2),_FsHQoSTBehaviorName_Type())
fsHQoSTBehaviorName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorName.setStatus(_A)
_FsHQoSTBehaviorRowStatus_Type=RowStatus
_FsHQoSTBehaviorRowStatus_Object=MibTableColumn
fsHQoSTBehaviorRowStatus=_FsHQoSTBehaviorRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,3),_FsHQoSTBehaviorRowStatus_Type())
fsHQoSTBehaviorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorRowStatus.setStatus(_A)
class _FsHQoSTBehaviorMask_Type(Bits):namedValues=NamedValues(*(('user-queue',0),('set-cos',1),('set-color',2),('remark-v4-dscp',3),('remark-v4-tos',4),('remark-v6-dscp',5),('remark-vlan-cos',6),('remark-exp',7),('sub-policy',8)))
_FsHQoSTBehaviorMask_Type.__name__=_Y
_FsHQoSTBehaviorMask_Object=MibTableColumn
fsHQoSTBehaviorMask=_FsHQoSTBehaviorMask_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,4),_FsHQoSTBehaviorMask_Type())
fsHQoSTBehaviorMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorMask.setStatus(_A)
class _FsHQoSTBehaviorUserQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTBehaviorUserQName_Type.__name__=_F
_FsHQoSTBehaviorUserQName_Object=MibTableColumn
fsHQoSTBehaviorUserQName=_FsHQoSTBehaviorUserQName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,5),_FsHQoSTBehaviorUserQName_Type())
fsHQoSTBehaviorUserQName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorUserQName.setStatus(_A)
_FsHQoSTBehaviorUserQDir_Type=FSQDirectionType
_FsHQoSTBehaviorUserQDir_Object=MibTableColumn
fsHQoSTBehaviorUserQDir=_FsHQoSTBehaviorUserQDir_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,6),_FsHQoSTBehaviorUserQDir_Type())
fsHQoSTBehaviorUserQDir.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorUserQDir.setStatus(_A)
class _FsHQoSTBehaviorTCos_Type(FSCosType):defaultValue=1
_FsHQoSTBehaviorTCos_Type.__name__=_K
_FsHQoSTBehaviorTCos_Object=MibTableColumn
fsHQoSTBehaviorTCos=_FsHQoSTBehaviorTCos_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,7),_FsHQoSTBehaviorTCos_Type())
fsHQoSTBehaviorTCos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorTCos.setStatus(_A)
class _FsHQoSTBehaviorTColor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3)))
_FsHQoSTBehaviorTColor_Type.__name__=_D
_FsHQoSTBehaviorTColor_Object=MibTableColumn
fsHQoSTBehaviorTColor=_FsHQoSTBehaviorTColor_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,8),_FsHQoSTBehaviorTColor_Type())
fsHQoSTBehaviorTColor.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorTColor.setStatus(_A)
class _FsHQoSTBehaviorRV4Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsHQoSTBehaviorRV4Dscp_Type.__name__=_D
_FsHQoSTBehaviorRV4Dscp_Object=MibTableColumn
fsHQoSTBehaviorRV4Dscp=_FsHQoSTBehaviorRV4Dscp_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,9),_FsHQoSTBehaviorRV4Dscp_Type())
fsHQoSTBehaviorRV4Dscp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorRV4Dscp.setStatus(_A)
class _FsHQoSTBehaviorRV4Tos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsHQoSTBehaviorRV4Tos_Type.__name__=_D
_FsHQoSTBehaviorRV4Tos_Object=MibTableColumn
fsHQoSTBehaviorRV4Tos=_FsHQoSTBehaviorRV4Tos_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,10),_FsHQoSTBehaviorRV4Tos_Type())
fsHQoSTBehaviorRV4Tos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorRV4Tos.setStatus(_A)
class _FsHQoSTBehaviorRV6Dscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsHQoSTBehaviorRV6Dscp_Type.__name__=_D
_FsHQoSTBehaviorRV6Dscp_Object=MibTableColumn
fsHQoSTBehaviorRV6Dscp=_FsHQoSTBehaviorRV6Dscp_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,11),_FsHQoSTBehaviorRV6Dscp_Type())
fsHQoSTBehaviorRV6Dscp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorRV6Dscp.setStatus(_A)
class _FsHQoSTBehaviorRVlanCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsHQoSTBehaviorRVlanCos_Type.__name__=_D
_FsHQoSTBehaviorRVlanCos_Object=MibTableColumn
fsHQoSTBehaviorRVlanCos=_FsHQoSTBehaviorRVlanCos_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,12),_FsHQoSTBehaviorRVlanCos_Type())
fsHQoSTBehaviorRVlanCos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorRVlanCos.setStatus(_A)
class _FsHQoSTBehaviorRExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsHQoSTBehaviorRExp_Type.__name__=_D
_FsHQoSTBehaviorRExp_Object=MibTableColumn
fsHQoSTBehaviorRExp=_FsHQoSTBehaviorRExp_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,13),_FsHQoSTBehaviorRExp_Type())
fsHQoSTBehaviorRExp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorRExp.setStatus(_A)
class _FsHQoSTBehaviorSubPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTBehaviorSubPolicyName_Type.__name__=_F
_FsHQoSTBehaviorSubPolicyName_Object=MibTableColumn
fsHQoSTBehaviorSubPolicyName=_FsHQoSTBehaviorSubPolicyName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,7,2,1,14),_FsHQoSTBehaviorSubPolicyName_Type())
fsHQoSTBehaviorSubPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTBehaviorSubPolicyName.setStatus(_A)
_FsHQoSTPolicyObjects_ObjectIdentity=ObjectIdentity
fsHQoSTPolicyObjects=_FsHQoSTPolicyObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,8))
_FsHQoSTPolicyIndexNext_Type=Integer32
_FsHQoSTPolicyIndexNext_Object=MibScalar
fsHQoSTPolicyIndexNext=_FsHQoSTPolicyIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,1),_FsHQoSTPolicyIndexNext_Type())
fsHQoSTPolicyIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSTPolicyIndexNext.setStatus(_A)
_FsHQoSTPolicyTable_Object=MibTable
fsHQoSTPolicyTable=_FsHQoSTPolicyTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,2))
if mibBuilder.loadTexts:fsHQoSTPolicyTable.setStatus(_A)
_FsHQoSTPolicyEntry_Object=MibTableRow
fsHQoSTPolicyEntry=_FsHQoSTPolicyEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,2,1))
fsHQoSTPolicyEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:fsHQoSTPolicyEntry.setStatus(_A)
_FsHQoSTPolicyIndex_Type=Unsigned32
_FsHQoSTPolicyIndex_Object=MibTableColumn
fsHQoSTPolicyIndex=_FsHQoSTPolicyIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,2,1,1),_FsHQoSTPolicyIndex_Type())
fsHQoSTPolicyIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSTPolicyIndex.setStatus(_A)
class _FsHQoSTPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTPolicyName_Type.__name__=_F
_FsHQoSTPolicyName_Object=MibTableColumn
fsHQoSTPolicyName=_FsHQoSTPolicyName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,2,1,2),_FsHQoSTPolicyName_Type())
fsHQoSTPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyName.setStatus(_A)
_FsHQoSTPolicyRowStatus_Type=RowStatus
_FsHQoSTPolicyRowStatus_Object=MibTableColumn
fsHQoSTPolicyRowStatus=_FsHQoSTPolicyRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,2,1,3),_FsHQoSTPolicyRowStatus_Type())
fsHQoSTPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyRowStatus.setStatus(_A)
_FsHQoSTPolicyMapIndexNext_Type=Integer32
_FsHQoSTPolicyMapIndexNext_Object=MibScalar
fsHQoSTPolicyMapIndexNext=_FsHQoSTPolicyMapIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,3),_FsHQoSTPolicyMapIndexNext_Type())
fsHQoSTPolicyMapIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSTPolicyMapIndexNext.setStatus(_A)
_FsHQoSTPolicyMapTable_Object=MibTable
fsHQoSTPolicyMapTable=_FsHQoSTPolicyMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4))
if mibBuilder.loadTexts:fsHQoSTPolicyMapTable.setStatus(_A)
_FsHQoSTPolicyMapEntry_Object=MibTableRow
fsHQoSTPolicyMapEntry=_FsHQoSTPolicyMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1))
fsHQoSTPolicyMapEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:fsHQoSTPolicyMapEntry.setStatus(_A)
_FsHQoSTPolicyMapIndex_Type=Unsigned32
_FsHQoSTPolicyMapIndex_Object=MibTableColumn
fsHQoSTPolicyMapIndex=_FsHQoSTPolicyMapIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,1),_FsHQoSTPolicyMapIndex_Type())
fsHQoSTPolicyMapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSTPolicyMapIndex.setStatus(_A)
class _FsHQoSTPolicyMapPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTPolicyMapPolicyName_Type.__name__=_F
_FsHQoSTPolicyMapPolicyName_Object=MibTableColumn
fsHQoSTPolicyMapPolicyName=_FsHQoSTPolicyMapPolicyName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,2),_FsHQoSTPolicyMapPolicyName_Type())
fsHQoSTPolicyMapPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapPolicyName.setStatus(_A)
_FsHQoSTPolicyMapPolicyIndex_Type=Unsigned32
_FsHQoSTPolicyMapPolicyIndex_Object=MibTableColumn
fsHQoSTPolicyMapPolicyIndex=_FsHQoSTPolicyMapPolicyIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,3),_FsHQoSTPolicyMapPolicyIndex_Type())
fsHQoSTPolicyMapPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapPolicyIndex.setStatus(_A)
class _FsHQoSTPolicyMapTClassfierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTPolicyMapTClassfierName_Type.__name__=_F
_FsHQoSTPolicyMapTClassfierName_Object=MibTableColumn
fsHQoSTPolicyMapTClassfierName=_FsHQoSTPolicyMapTClassfierName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,4),_FsHQoSTPolicyMapTClassfierName_Type())
fsHQoSTPolicyMapTClassfierName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapTClassfierName.setStatus(_A)
_FsHQoSTPolicyMapTClassfierIndex_Type=Unsigned32
_FsHQoSTPolicyMapTClassfierIndex_Object=MibTableColumn
fsHQoSTPolicyMapTClassfierIndex=_FsHQoSTPolicyMapTClassfierIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,5),_FsHQoSTPolicyMapTClassfierIndex_Type())
fsHQoSTPolicyMapTClassfierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapTClassfierIndex.setStatus(_A)
class _FsHQoSTPolicyMapTBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSTPolicyMapTBehaviorName_Type.__name__=_F
_FsHQoSTPolicyMapTBehaviorName_Object=MibTableColumn
fsHQoSTPolicyMapTBehaviorName=_FsHQoSTPolicyMapTBehaviorName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,6),_FsHQoSTPolicyMapTBehaviorName_Type())
fsHQoSTPolicyMapTBehaviorName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapTBehaviorName.setStatus(_A)
_FsHQoSTPolicyMapTBehaviorIndex_Type=Unsigned32
_FsHQoSTPolicyMapTBehaviorIndex_Object=MibTableColumn
fsHQoSTPolicyMapTBehaviorIndex=_FsHQoSTPolicyMapTBehaviorIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,7),_FsHQoSTPolicyMapTBehaviorIndex_Type())
fsHQoSTPolicyMapTBehaviorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapTBehaviorIndex.setStatus(_A)
class _FsHQoSTPolicyMapPrecedence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_FsHQoSTPolicyMapPrecedence_Type.__name__=_M
_FsHQoSTPolicyMapPrecedence_Object=MibTableColumn
fsHQoSTPolicyMapPrecedence=_FsHQoSTPolicyMapPrecedence_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,8),_FsHQoSTPolicyMapPrecedence_Type())
fsHQoSTPolicyMapPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapPrecedence.setStatus(_A)
_FsHQoSTPolicyMapRowStatus_Type=RowStatus
_FsHQoSTPolicyMapRowStatus_Object=MibTableColumn
fsHQoSTPolicyMapRowStatus=_FsHQoSTPolicyMapRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,8,4,1,9),_FsHQoSTPolicyMapRowStatus_Type())
fsHQoSTPolicyMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSTPolicyMapRowStatus.setStatus(_A)
_FsHQoSVoQObjects_ObjectIdentity=ObjectIdentity
fsHQoSVoQObjects=_FsHQoSVoQObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,9))
class _FsHQoSVoQEnable_Type(TruthValue):defaultValue=2
_FsHQoSVoQEnable_Type.__name__=_O
_FsHQoSVoQEnable_Object=MibScalar
fsHQoSVoQEnable=_FsHQoSVoQEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,9,1),_FsHQoSVoQEnable_Type())
fsHQoSVoQEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSVoQEnable.setStatus(_A)
_FsHQoSVoQDeviceTable_Object=MibTable
fsHQoSVoQDeviceTable=_FsHQoSVoQDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,9,2))
if mibBuilder.loadTexts:fsHQoSVoQDeviceTable.setStatus(_A)
_FsHQoSVoQDeviceEntry_Object=MibTableRow
fsHQoSVoQDeviceEntry=_FsHQoSVoQDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,9,2,1))
fsHQoSVoQDeviceEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:fsHQoSVoQDeviceEntry.setStatus(_A)
_FsHQoSVoQDeviceId_Type=Unsigned32
_FsHQoSVoQDeviceId_Object=MibTableColumn
fsHQoSVoQDeviceId=_FsHQoSVoQDeviceId_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,9,2,1,1),_FsHQoSVoQDeviceId_Type())
fsHQoSVoQDeviceId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSVoQDeviceId.setStatus(_A)
_FsHQoSVoQDeviceCredit_Type=Unsigned32
_FsHQoSVoQDeviceCredit_Object=MibTableColumn
fsHQoSVoQDeviceCredit=_FsHQoSVoQDeviceCredit_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,9,2,1,2),_FsHQoSVoQDeviceCredit_Type())
fsHQoSVoQDeviceCredit.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSVoQDeviceCredit.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSVoQDeviceCredit.setUnits('Mbit/s')
_FsHQoSPortQObjects_ObjectIdentity=ObjectIdentity
fsHQoSPortQObjects=_FsHQoSPortQObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,10))
_FsHQoSPortQIndexNext_Type=Integer32
_FsHQoSPortQIndexNext_Object=MibScalar
fsHQoSPortQIndexNext=_FsHQoSPortQIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,1),_FsHQoSPortQIndexNext_Type())
fsHQoSPortQIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSPortQIndexNext.setStatus(_A)
_FsHQoSPortQTable_Object=MibTable
fsHQoSPortQTable=_FsHQoSPortQTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2))
if mibBuilder.loadTexts:fsHQoSPortQTable.setStatus(_A)
_FsHQoSPortQEntry_Object=MibTableRow
fsHQoSPortQEntry=_FsHQoSPortQEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1))
fsHQoSPortQEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:fsHQoSPortQEntry.setStatus(_A)
_FsHQoSPortQIndex_Type=Unsigned32
_FsHQoSPortQIndex_Object=MibTableColumn
fsHQoSPortQIndex=_FsHQoSPortQIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,1),_FsHQoSPortQIndex_Type())
fsHQoSPortQIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSPortQIndex.setStatus(_A)
class _FsHQoSPortQName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQName_Type.__name__=_F
_FsHQoSPortQName_Object=MibTableColumn
fsHQoSPortQName=_FsHQoSPortQName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,2),_FsHQoSPortQName_Type())
fsHQoSPortQName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQName.setStatus(_A)
_FsHQoSPortQRowStatus_Type=RowStatus
_FsHQoSPortQRowStatus_Object=MibTableColumn
fsHQoSPortQRowStatus=_FsHQoSPortQRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,3),_FsHQoSPortQRowStatus_Type())
fsHQoSPortQRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQRowStatus.setStatus(_A)
class _FsHQoSPortQBEQType_Type(FSQType):defaultValue=2
_FsHQoSPortQBEQType_Type.__name__=_H
_FsHQoSPortQBEQType_Object=MibTableColumn
fsHQoSPortQBEQType=_FsHQoSPortQBEQType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,4),_FsHQoSPortQBEQType_Type())
fsHQoSPortQBEQType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQBEQType.setStatus(_A)
class _FsHQoSPortQBEQWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQBEQWredWeight_Type.__name__=_D
_FsHQoSPortQBEQWredWeight_Object=MibTableColumn
fsHQoSPortQBEQWredWeight=_FsHQoSPortQBEQWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,5),_FsHQoSPortQBEQWredWeight_Type())
fsHQoSPortQBEQWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQBEQWredWeight.setStatus(_A)
class _FsHQoSPortQBEQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQBEQWredName_Type.__name__=_F
_FsHQoSPortQBEQWredName_Object=MibTableColumn
fsHQoSPortQBEQWredName=_FsHQoSPortQBEQWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,6),_FsHQoSPortQBEQWredName_Type())
fsHQoSPortQBEQWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQBEQWredName.setStatus(_A)
class _FsHQoSPortQBEQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQBEQDepth_Type.__name__=_D
_FsHQoSPortQBEQDepth_Object=MibTableColumn
fsHQoSPortQBEQDepth=_FsHQoSPortQBEQDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,7),_FsHQoSPortQBEQDepth_Type())
fsHQoSPortQBEQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQBEQDepth.setStatus(_A)
class _FsHQoSPortQBEQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQBEQShaping_Type.__name__=_D
_FsHQoSPortQBEQShaping_Object=MibTableColumn
fsHQoSPortQBEQShaping=_FsHQoSPortQBEQShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,8),_FsHQoSPortQBEQShaping_Type())
fsHQoSPortQBEQShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQBEQShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQBEQShaping.setUnits(_G)
class _FsHQoSPortQAF1QType_Type(FSQType):defaultValue=2
_FsHQoSPortQAF1QType_Type.__name__=_H
_FsHQoSPortQAF1QType_Object=MibTableColumn
fsHQoSPortQAF1QType=_FsHQoSPortQAF1QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,9),_FsHQoSPortQAF1QType_Type())
fsHQoSPortQAF1QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF1QType.setStatus(_A)
class _FsHQoSPortQAF1QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQAF1QWredWeight_Type.__name__=_D
_FsHQoSPortQAF1QWredWeight_Object=MibTableColumn
fsHQoSPortQAF1QWredWeight=_FsHQoSPortQAF1QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,10),_FsHQoSPortQAF1QWredWeight_Type())
fsHQoSPortQAF1QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF1QWredWeight.setStatus(_A)
class _FsHQoSPortQAF1QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQAF1QWredName_Type.__name__=_F
_FsHQoSPortQAF1QWredName_Object=MibTableColumn
fsHQoSPortQAF1QWredName=_FsHQoSPortQAF1QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,11),_FsHQoSPortQAF1QWredName_Type())
fsHQoSPortQAF1QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF1QWredName.setStatus(_A)
class _FsHQoSPortQAF1QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQAF1QDepth_Type.__name__=_D
_FsHQoSPortQAF1QDepth_Object=MibTableColumn
fsHQoSPortQAF1QDepth=_FsHQoSPortQAF1QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,12),_FsHQoSPortQAF1QDepth_Type())
fsHQoSPortQAF1QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF1QDepth.setStatus(_A)
class _FsHQoSPortQAF1QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQAF1QShaping_Type.__name__=_D
_FsHQoSPortQAF1QShaping_Object=MibTableColumn
fsHQoSPortQAF1QShaping=_FsHQoSPortQAF1QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,13),_FsHQoSPortQAF1QShaping_Type())
fsHQoSPortQAF1QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF1QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQAF1QShaping.setUnits(_G)
class _FsHQoSPortQAF2QType_Type(FSQType):defaultValue=2
_FsHQoSPortQAF2QType_Type.__name__=_H
_FsHQoSPortQAF2QType_Object=MibTableColumn
fsHQoSPortQAF2QType=_FsHQoSPortQAF2QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,14),_FsHQoSPortQAF2QType_Type())
fsHQoSPortQAF2QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF2QType.setStatus(_A)
class _FsHQoSPortQAF2QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_FsHQoSPortQAF2QWredWeight_Type.__name__=_D
_FsHQoSPortQAF2QWredWeight_Object=MibTableColumn
fsHQoSPortQAF2QWredWeight=_FsHQoSPortQAF2QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,15),_FsHQoSPortQAF2QWredWeight_Type())
fsHQoSPortQAF2QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF2QWredWeight.setStatus(_A)
class _FsHQoSPortQAF2QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQAF2QWredName_Type.__name__=_F
_FsHQoSPortQAF2QWredName_Object=MibTableColumn
fsHQoSPortQAF2QWredName=_FsHQoSPortQAF2QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,16),_FsHQoSPortQAF2QWredName_Type())
fsHQoSPortQAF2QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF2QWredName.setStatus(_A)
class _FsHQoSPortQAF2QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQAF2QDepth_Type.__name__=_D
_FsHQoSPortQAF2QDepth_Object=MibTableColumn
fsHQoSPortQAF2QDepth=_FsHQoSPortQAF2QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,17),_FsHQoSPortQAF2QDepth_Type())
fsHQoSPortQAF2QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF2QDepth.setStatus(_A)
class _FsHQoSPortQAF2QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQAF2QShaping_Type.__name__=_D
_FsHQoSPortQAF2QShaping_Object=MibTableColumn
fsHQoSPortQAF2QShaping=_FsHQoSPortQAF2QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,18),_FsHQoSPortQAF2QShaping_Type())
fsHQoSPortQAF2QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF2QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQAF2QShaping.setUnits(_G)
class _FsHQoSPortQAF3QType_Type(FSQType):defaultValue=2
_FsHQoSPortQAF3QType_Type.__name__=_H
_FsHQoSPortQAF3QType_Object=MibTableColumn
fsHQoSPortQAF3QType=_FsHQoSPortQAF3QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,19),_FsHQoSPortQAF3QType_Type())
fsHQoSPortQAF3QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF3QType.setStatus(_A)
class _FsHQoSPortQAF3QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQAF3QWredWeight_Type.__name__=_D
_FsHQoSPortQAF3QWredWeight_Object=MibTableColumn
fsHQoSPortQAF3QWredWeight=_FsHQoSPortQAF3QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,20),_FsHQoSPortQAF3QWredWeight_Type())
fsHQoSPortQAF3QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF3QWredWeight.setStatus(_A)
class _FsHQoSPortQAF3QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQAF3QWredName_Type.__name__=_F
_FsHQoSPortQAF3QWredName_Object=MibTableColumn
fsHQoSPortQAF3QWredName=_FsHQoSPortQAF3QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,21),_FsHQoSPortQAF3QWredName_Type())
fsHQoSPortQAF3QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF3QWredName.setStatus(_A)
class _FsHQoSPortQAF3QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQAF3QDepth_Type.__name__=_D
_FsHQoSPortQAF3QDepth_Object=MibTableColumn
fsHQoSPortQAF3QDepth=_FsHQoSPortQAF3QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,22),_FsHQoSPortQAF3QDepth_Type())
fsHQoSPortQAF3QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF3QDepth.setStatus(_A)
class _FsHQoSPortQAF3QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQAF3QShaping_Type.__name__=_D
_FsHQoSPortQAF3QShaping_Object=MibTableColumn
fsHQoSPortQAF3QShaping=_FsHQoSPortQAF3QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,23),_FsHQoSPortQAF3QShaping_Type())
fsHQoSPortQAF3QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF3QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQAF3QShaping.setUnits(_G)
class _FsHQoSPortQAF4QType_Type(FSQType):defaultValue=2
_FsHQoSPortQAF4QType_Type.__name__=_H
_FsHQoSPortQAF4QType_Object=MibTableColumn
fsHQoSPortQAF4QType=_FsHQoSPortQAF4QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,24),_FsHQoSPortQAF4QType_Type())
fsHQoSPortQAF4QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF4QType.setStatus(_A)
class _FsHQoSPortQAF4QWredWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQAF4QWredWeight_Type.__name__=_D
_FsHQoSPortQAF4QWredWeight_Object=MibTableColumn
fsHQoSPortQAF4QWredWeight=_FsHQoSPortQAF4QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,25),_FsHQoSPortQAF4QWredWeight_Type())
fsHQoSPortQAF4QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF4QWredWeight.setStatus(_A)
class _FsHQoSPortQAF4QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQAF4QWredName_Type.__name__=_F
_FsHQoSPortQAF4QWredName_Object=MibTableColumn
fsHQoSPortQAF4QWredName=_FsHQoSPortQAF4QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,26),_FsHQoSPortQAF4QWredName_Type())
fsHQoSPortQAF4QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF4QWredName.setStatus(_A)
class _FsHQoSPortQAF4QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQAF4QDepth_Type.__name__=_D
_FsHQoSPortQAF4QDepth_Object=MibTableColumn
fsHQoSPortQAF4QDepth=_FsHQoSPortQAF4QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,27),_FsHQoSPortQAF4QDepth_Type())
fsHQoSPortQAF4QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF4QDepth.setStatus(_A)
class _FsHQoSPortQAF4QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQAF4QShaping_Type.__name__=_D
_FsHQoSPortQAF4QShaping_Object=MibTableColumn
fsHQoSPortQAF4QShaping=_FsHQoSPortQAF4QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,28),_FsHQoSPortQAF4QShaping_Type())
fsHQoSPortQAF4QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQAF4QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQAF4QShaping.setUnits(_G)
class _FsHQoSPortQEFQType_Type(FSQType):defaultValue=3
_FsHQoSPortQEFQType_Type.__name__=_H
_FsHQoSPortQEFQType_Object=MibTableColumn
fsHQoSPortQEFQType=_FsHQoSPortQEFQType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,29),_FsHQoSPortQEFQType_Type())
fsHQoSPortQEFQType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQEFQType.setStatus(_A)
class _FsHQoSPortQEFQWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQEFQWredWeight_Type.__name__=_D
_FsHQoSPortQEFQWredWeight_Object=MibTableColumn
fsHQoSPortQEFQWredWeight=_FsHQoSPortQEFQWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,30),_FsHQoSPortQEFQWredWeight_Type())
fsHQoSPortQEFQWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQEFQWredWeight.setStatus(_A)
class _FsHQoSPortQEFQWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQEFQWredName_Type.__name__=_F
_FsHQoSPortQEFQWredName_Object=MibTableColumn
fsHQoSPortQEFQWredName=_FsHQoSPortQEFQWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,31),_FsHQoSPortQEFQWredName_Type())
fsHQoSPortQEFQWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQEFQWredName.setStatus(_A)
class _FsHQoSPortQEFQDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQEFQDepth_Type.__name__=_D
_FsHQoSPortQEFQDepth_Object=MibTableColumn
fsHQoSPortQEFQDepth=_FsHQoSPortQEFQDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,32),_FsHQoSPortQEFQDepth_Type())
fsHQoSPortQEFQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQEFQDepth.setStatus(_A)
class _FsHQoSPortQEFQShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQEFQShaping_Type.__name__=_D
_FsHQoSPortQEFQShaping_Object=MibTableColumn
fsHQoSPortQEFQShaping=_FsHQoSPortQEFQShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,33),_FsHQoSPortQEFQShaping_Type())
fsHQoSPortQEFQShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQEFQShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQEFQShaping.setUnits(_G)
class _FsHQoSPortQCS6QType_Type(FSQType):defaultValue=3
_FsHQoSPortQCS6QType_Type.__name__=_H
_FsHQoSPortQCS6QType_Object=MibTableColumn
fsHQoSPortQCS6QType=_FsHQoSPortQCS6QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,34),_FsHQoSPortQCS6QType_Type())
fsHQoSPortQCS6QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS6QType.setStatus(_A)
class _FsHQoSPortQCS6QWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQCS6QWredWeight_Type.__name__=_D
_FsHQoSPortQCS6QWredWeight_Object=MibTableColumn
fsHQoSPortQCS6QWredWeight=_FsHQoSPortQCS6QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,35),_FsHQoSPortQCS6QWredWeight_Type())
fsHQoSPortQCS6QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS6QWredWeight.setStatus(_A)
class _FsHQoSPortQCS6QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQCS6QWredName_Type.__name__=_F
_FsHQoSPortQCS6QWredName_Object=MibTableColumn
fsHQoSPortQCS6QWredName=_FsHQoSPortQCS6QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,36),_FsHQoSPortQCS6QWredName_Type())
fsHQoSPortQCS6QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS6QWredName.setStatus(_A)
class _FsHQoSPortQCS6QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQCS6QDepth_Type.__name__=_D
_FsHQoSPortQCS6QDepth_Object=MibTableColumn
fsHQoSPortQCS6QDepth=_FsHQoSPortQCS6QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,37),_FsHQoSPortQCS6QDepth_Type())
fsHQoSPortQCS6QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS6QDepth.setStatus(_A)
class _FsHQoSPortQCS6QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQCS6QShaping_Type.__name__=_D
_FsHQoSPortQCS6QShaping_Object=MibTableColumn
fsHQoSPortQCS6QShaping=_FsHQoSPortQCS6QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,38),_FsHQoSPortQCS6QShaping_Type())
fsHQoSPortQCS6QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS6QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQCS6QShaping.setUnits(_G)
class _FsHQoSPortQCS7QType_Type(FSQType):defaultValue=3
_FsHQoSPortQCS7QType_Type.__name__=_H
_FsHQoSPortQCS7QType_Object=MibTableColumn
fsHQoSPortQCS7QType=_FsHQoSPortQCS7QType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,39),_FsHQoSPortQCS7QType_Type())
fsHQoSPortQCS7QType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS7QType.setStatus(_A)
class _FsHQoSPortQCS7QWredWeight_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_FsHQoSPortQCS7QWredWeight_Type.__name__=_D
_FsHQoSPortQCS7QWredWeight_Object=MibTableColumn
fsHQoSPortQCS7QWredWeight=_FsHQoSPortQCS7QWredWeight_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,40),_FsHQoSPortQCS7QWredWeight_Type())
fsHQoSPortQCS7QWredWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS7QWredWeight.setStatus(_A)
class _FsHQoSPortQCS7QWredName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSPortQCS7QWredName_Type.__name__=_F
_FsHQoSPortQCS7QWredName_Object=MibTableColumn
fsHQoSPortQCS7QWredName=_FsHQoSPortQCS7QWredName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,41),_FsHQoSPortQCS7QWredName_Type())
fsHQoSPortQCS7QWredName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS7QWredName.setStatus(_A)
class _FsHQoSPortQCS7QDepth_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsHQoSPortQCS7QDepth_Type.__name__=_D
_FsHQoSPortQCS7QDepth_Object=MibTableColumn
fsHQoSPortQCS7QDepth=_FsHQoSPortQCS7QDepth_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,42),_FsHQoSPortQCS7QDepth_Type())
fsHQoSPortQCS7QDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS7QDepth.setStatus(_A)
class _FsHQoSPortQCS7QShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSPortQCS7QShaping_Type.__name__=_D
_FsHQoSPortQCS7QShaping_Object=MibTableColumn
fsHQoSPortQCS7QShaping=_FsHQoSPortQCS7QShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,10,2,1,43),_FsHQoSPortQCS7QShaping_Type())
fsHQoSPortQCS7QShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHQoSPortQCS7QShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSPortQCS7QShaping.setUnits(_G)
_FsHQoSIfAppObjects_ObjectIdentity=ObjectIdentity
fsHQoSIfAppObjects=_FsHQoSIfAppObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,3,11))
_FsHQoSIfAppTable_Object=MibTable
fsHQoSIfAppTable=_FsHQoSIfAppTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1))
if mibBuilder.loadTexts:fsHQoSIfAppTable.setStatus(_A)
_FsHQoSIfAppEntry_Object=MibTableRow
fsHQoSIfAppEntry=_FsHQoSIfAppEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1))
fsHQoSIfAppEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:fsHQoSIfAppEntry.setStatus(_A)
_FsHQoSIfAppIndex_Type=InterfaceIndex
_FsHQoSIfAppIndex_Object=MibTableColumn
fsHQoSIfAppIndex=_FsHQoSIfAppIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,1),_FsHQoSIfAppIndex_Type())
fsHQoSIfAppIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsHQoSIfAppIndex.setStatus(_A)
class _FsHQoSIfAppInPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSIfAppInPolicyName_Type.__name__=_F
_FsHQoSIfAppInPolicyName_Object=MibTableColumn
fsHQoSIfAppInPolicyName=_FsHQoSIfAppInPolicyName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,2),_FsHQoSIfAppInPolicyName_Type())
fsHQoSIfAppInPolicyName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSIfAppInPolicyName.setStatus(_A)
_FsHQoSIfAppInPolicyIndex_Type=Unsigned32
_FsHQoSIfAppInPolicyIndex_Object=MibTableColumn
fsHQoSIfAppInPolicyIndex=_FsHQoSIfAppInPolicyIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,3),_FsHQoSIfAppInPolicyIndex_Type())
fsHQoSIfAppInPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSIfAppInPolicyIndex.setStatus(_A)
class _FsHQoSIfAppInPolicyLayer_Type(FSLayerType):defaultValue=0
_FsHQoSIfAppInPolicyLayer_Type.__name__=_Z
_FsHQoSIfAppInPolicyLayer_Object=MibTableColumn
fsHQoSIfAppInPolicyLayer=_FsHQoSIfAppInPolicyLayer_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,4),_FsHQoSIfAppInPolicyLayer_Type())
fsHQoSIfAppInPolicyLayer.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSIfAppInPolicyLayer.setStatus(_A)
class _FsHQoSIfAppOutPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSIfAppOutPolicyName_Type.__name__=_F
_FsHQoSIfAppOutPolicyName_Object=MibTableColumn
fsHQoSIfAppOutPolicyName=_FsHQoSIfAppOutPolicyName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,5),_FsHQoSIfAppOutPolicyName_Type())
fsHQoSIfAppOutPolicyName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSIfAppOutPolicyName.setStatus(_A)
_FsHQoSIfAppOutPolicyIndex_Type=Unsigned32
_FsHQoSIfAppOutPolicyIndex_Object=MibTableColumn
fsHQoSIfAppOutPolicyIndex=_FsHQoSIfAppOutPolicyIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,6),_FsHQoSIfAppOutPolicyIndex_Type())
fsHQoSIfAppOutPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSIfAppOutPolicyIndex.setStatus(_A)
class _FsHQoSIfAppOutPolicyLayer_Type(FSLayerType):defaultValue=0
_FsHQoSIfAppOutPolicyLayer_Type.__name__=_Z
_FsHQoSIfAppOutPolicyLayer_Object=MibTableColumn
fsHQoSIfAppOutPolicyLayer=_FsHQoSIfAppOutPolicyLayer_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,7),_FsHQoSIfAppOutPolicyLayer_Type())
fsHQoSIfAppOutPolicyLayer.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSIfAppOutPolicyLayer.setStatus(_A)
class _FsHQoSIfAppPortQueueName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsHQoSIfAppPortQueueName_Type.__name__=_F
_FsHQoSIfAppPortQueueName_Object=MibTableColumn
fsHQoSIfAppPortQueueName=_FsHQoSIfAppPortQueueName_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,8),_FsHQoSIfAppPortQueueName_Type())
fsHQoSIfAppPortQueueName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSIfAppPortQueueName.setStatus(_A)
_FsHQoSIfAppPortQueueIndex_Type=Unsigned32
_FsHQoSIfAppPortQueueIndex_Object=MibTableColumn
fsHQoSIfAppPortQueueIndex=_FsHQoSIfAppPortQueueIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,9),_FsHQoSIfAppPortQueueIndex_Type())
fsHQoSIfAppPortQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHQoSIfAppPortQueueIndex.setStatus(_A)
class _FsHQoSIfAppPortQueueShaping_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FsHQoSIfAppPortQueueShaping_Type.__name__=_D
_FsHQoSIfAppPortQueueShaping_Object=MibTableColumn
fsHQoSIfAppPortQueueShaping=_FsHQoSIfAppPortQueueShaping_Object((1,3,6,1,4,1,52642,1,1,10,2,106,3,11,1,1,10),_FsHQoSIfAppPortQueueShaping_Type())
fsHQoSIfAppPortQueueShaping.setMaxAccess(_J)
if mibBuilder.loadTexts:fsHQoSIfAppPortQueueShaping.setStatus(_A)
if mibBuilder.loadTexts:fsHQoSIfAppPortQueueShaping.setUnits(_G)
mibBuilder.exportSymbols(_E,**{_K:FSCosType,_H:FSQType,'FSQDirectionType':FSQDirectionType,_Z:FSLayerType,'fsRouterQoSMIB':fsRouterQoSMIB,'fsCBQoSMIBObjects':fsCBQoSMIBObjects,'fsCBQoSIfStaticsObjects':fsCBQoSIfStaticsObjects,'fsCBQoSIfCbwfqRunInfoTable':fsCBQoSIfCbwfqRunInfoTable,'fsCBQoSIfCbwfqRunInfoEntry':fsCBQoSIfCbwfqRunInfoEntry,_a:fsCBQoSIfCbwfqPolicyIfIndex,'fsCBQoSIfCbwfqQueueSize':fsCBQoSIfCbwfqQueueSize,'fsCBQoSIfCbwfqDiscard':fsCBQoSIfCbwfqDiscard,'fsCBQoSIfCbwfqEfQueueSize':fsCBQoSIfCbwfqEfQueueSize,'fsCBQoSIfCbwfqAfQueueSize':fsCBQoSIfCbwfqAfQueueSize,'fsCBQoSIfCbwfqBeQueueSize':fsCBQoSIfCbwfqBeQueueSize,'fsCBQoSIfCbwfqBeActiveQueueNum':fsCBQoSIfCbwfqBeActiveQueueNum,'fsCBQoSIfCbwfqBeMaxActiveQueueNum':fsCBQoSIfCbwfqBeMaxActiveQueueNum,'fsCBQoSIfCbwfqBeTotalQueueNum':fsCBQoSIfCbwfqBeTotalQueueNum,'fsCBQoSIfCbwfqAfAllocatedQueueNum':fsCBQoSIfCbwfqAfAllocatedQueueNum,'fsCBQoSIfCbwfqPass':fsCBQoSIfCbwfqPass,'fsCBQoSIfCbwfqDroppedRateIn5Min':fsCBQoSIfCbwfqDroppedRateIn5Min,'fsCBQoSIfCbwfqPassBytes':fsCBQoSIfCbwfqPassBytes,'fsCBQoSIfCbwfqDiscardBytes':fsCBQoSIfCbwfqDiscardBytes,'fsCBQoSIfClassMatchRunInfoTable':fsCBQoSIfClassMatchRunInfoTable,'fsCBQoSIfClassMatchRunInfoEntry':fsCBQoSIfClassMatchRunInfoEntry,_b:fsCBQoSIfClassMatchIfIndex,_c:fsCBQoSIfClassMatchPolicyDirection,_d:fsCBQoSIfClassMatchClassIndex,'fsCBQoSIfClassMatchedPackets':fsCBQoSIfClassMatchedPackets,'fsCBQoSIfClassMatchedBytes':fsCBQoSIfClassMatchedBytes,'fsCBQosIfClassPassedPackets':fsCBQosIfClassPassedPackets,'fsCBQosIfClassDroppedPackets':fsCBQosIfClassDroppedPackets,'fsCBQoSIfPolicyName':fsCBQoSIfPolicyName,'fsCBQoSIfClassName':fsCBQoSIfClassName,'fsCBQoSIfClassPassBytes':fsCBQoSIfClassPassBytes,'fsCBQoSIfClassDiscardBytes':fsCBQoSIfClassDiscardBytes,'fsCBQoSIfCarRunInfoTable':fsCBQoSIfCarRunInfoTable,'fsCBQoSIfCarRunInfoEntry':fsCBQoSIfCarRunInfoEntry,_e:fsCBQoSIfCarIfIndex,_f:fsCBQoSIfCarPolicyDirection,_g:fsCBQoSIfCarClassIndex,'fsCBQoSIfCarConformedPackets':fsCBQoSIfCarConformedPackets,'fsCBQoSIfCarConformedBytes':fsCBQoSIfCarConformedBytes,'fsCBQoSIfCarExceededPackets':fsCBQoSIfCarExceededPackets,'fsCBQoSIfCarExceededBytes':fsCBQoSIfCarExceededBytes,'fsCBQoSIfCarViolatedPackets':fsCBQoSIfCarViolatedPackets,'fsCBQoSIfCarViolatedBytes':fsCBQoSIfCarViolatedBytes,'fsCBQoSIfRemarkRunInfoTable':fsCBQoSIfRemarkRunInfoTable,'fsCBQoSIfRemarkRunInfoEntry':fsCBQoSIfRemarkRunInfoEntry,_h:fsCBQoSIfRemarkIfIndex,_i:fsCBQoSIfRemarkPolicyDirection,_j:fsCBQoSIfRemarkClassIndex,'fsCBQoSIfRemarkedPackets':fsCBQoSIfRemarkedPackets,'fsCBQoSIfRemarkedBytes':fsCBQoSIfRemarkedBytes,'fsCBQoSIfQueueRunInfoTable':fsCBQoSIfQueueRunInfoTable,'fsCBQoSIfQueueRunInfoEntry':fsCBQoSIfQueueRunInfoEntry,_k:fsCBQoSIfQueueIfIndex,_l:fsCBQoSIfQueuePolicyDirection,_m:fsCBQoSIfQueueClassIndex,'fsCBQoSIfQueueMatchedPackets':fsCBQoSIfQueueMatchedPackets,'fsCBQoSIfQueueMatchedBytes':fsCBQoSIfQueueMatchedBytes,'fsCBQoSIfQueueEnqueuedPackets':fsCBQoSIfQueueEnqueuedPackets,'fsCBQoSIfQueueEnqueuedBytes':fsCBQoSIfQueueEnqueuedBytes,'fsCBQoSIfQueueDiscardedPackets':fsCBQoSIfQueueDiscardedPackets,'fsCBQoSIfQueueDiscardedBytes':fsCBQoSIfQueueDiscardedBytes,'fsCBQoSIfWredRunInfoTable':fsCBQoSIfWredRunInfoTable,'fsCBQoSIfWredRunInfoEntry':fsCBQoSIfWredRunInfoEntry,_n:fsCBQoSIfWredIfIndex,_o:fsCBQoSIfWredClassIndex,_p:fsCBQoSIfWredClassValue,'fsCBQoSIfWredRandomDiscardedPackets':fsCBQoSIfWredRandomDiscardedPackets,'fsCBQoSIfWredTailDiscardedPackets':fsCBQoSIfWredTailDiscardedPackets,'fsIfQoSMIBObjects':fsIfQoSMIBObjects,'fsIfQosPQRunInfoTable':fsIfQosPQRunInfoTable,'fsIfQosPQRunInfoEntry':fsIfQosPQRunInfoEntry,_q:fsIfQosPQIfIndex,'fsIfQosPQListNum':fsIfQosPQListNum,'fsIfQosPQIfName':fsIfQosPQIfName,'fsIfQosPQHighPkt':fsIfQosPQHighPkt,'fsIfQosPQHighDiscard':fsIfQosPQHighDiscard,'fsIfQosPQHighMaxQueLen':fsIfQosPQHighMaxQueLen,'fsIfQosPQMiddlePkt':fsIfQosPQMiddlePkt,'fsIfQosPQMiddleDiscard':fsIfQosPQMiddleDiscard,'fsIfQosPQMiddleMaxQueLen':fsIfQosPQMiddleMaxQueLen,'fsIfQosPQNormalPkt':fsIfQosPQNormalPkt,'fsIfQosPQNormalDiscard':fsIfQosPQNormalDiscard,'fsIfQosPQNormalMaxQueLen':fsIfQosPQNormalMaxQueLen,'fsIfQosPQLowPkt':fsIfQosPQLowPkt,'fsIfQosPQLowDiscard':fsIfQosPQLowDiscard,'fsIfQosPQLowMaxQueLen':fsIfQosPQLowMaxQueLen,'fsIfQosCQRunInfoTable':fsIfQosCQRunInfoTable,'fsIfQosCQRunInfoEntry':fsIfQosCQRunInfoEntry,_r:fsIfQosCQRunInfoIfIndex,_s:fsIfQosCQRunInfoQueNum,'fsIfQosCQRunInfoIfName':fsIfQosCQRunInfoIfName,'fsIfQosCQRunInfoQuePkt':fsIfQosCQRunInfoQuePkt,'fsIfQosCQRunInfoQueDiscard':fsIfQosCQRunInfoQueDiscard,'fsIfQosCQRunInfoMaxQueLen':fsIfQosCQRunInfoMaxQueLen,'fsIfQosWFQRunInfoTable':fsIfQosWFQRunInfoTable,'fsIfQosWFQRunInfoEntry':fsIfQosWFQRunInfoEntry,_t:fsIfQosWFQIfIndex,'fsIfQosWFQIfName':fsIfQosWFQIfName,'fsIfQosWFQMaxQueLen':fsIfQosWFQMaxQueLen,'fsIfQosWFQTotalQueNum':fsIfQosWFQTotalQueNum,'fsIfQosWFQCurQueLen':fsIfQosWFQCurQueLen,'fsIfQosWFQTotalDiscard':fsIfQosWFQTotalDiscard,'fsIfQosWFQActiveQueNum':fsIfQosWFQActiveQueNum,'fsIfQosWFQMaxActiveQueNum':fsIfQosWFQMaxActiveQueNum,'fsIfQosWredRunInfoTable':fsIfQosWredRunInfoTable,'fsIfQosWredRunInfoEntry':fsIfQosWredRunInfoEntry,_u:fsIfQosWredIfIndex,_v:fsIfQosWredValue,'fsIfQosWredRandomDiscardedPackets':fsIfQosWredRandomDiscardedPackets,'fsIfQosWredTailDiscardedPackets':fsIfQosWredTailDiscardedPackets,'fsIfQosCARTable':fsIfQosCARTable,'fsIfQosCAREntry':fsIfQosCAREntry,_w:fsIfQosCARIfIndex,'fsIfQosCARIfName':fsIfQosCARIfName,_x:fsIfQosCARPktDirection,'fsIfQosCARType':fsIfQosCARType,'fsIfQosCARListNum':fsIfQosCARListNum,_y:fsIfQosCARindex,'fsIfQosCARCIR':fsIfQosCARCIR,'fsIfQosCARBurstSize':fsIfQosCARBurstSize,'fsIfQosCARExcessBurstSize':fsIfQosCARExcessBurstSize,'fsIfQosCARConformAction':fsIfQosCARConformAction,'fsIfQosCARExceedAction':fsIfQosCARExceedAction,'fsIfQosCARConformNewPrec':fsIfQosCARConformNewPrec,'fsIfQosCARExceedNewPrec':fsIfQosCARExceedNewPrec,'fsIfQosCARConformPkt':fsIfQosCARConformPkt,'fsIfQosCARConformByte':fsIfQosCARConformByte,'fsIfQosCARExceedPkt':fsIfQosCARExceedPkt,'fsIfQosCARExceedByte':fsIfQosCARExceedByte,'fsIfQosGTSTable':fsIfQosGTSTable,'fsIfQosGTSEntry':fsIfQosGTSEntry,_z:fsIfQosGTSIfIndex,'fsIfQosGTSIfName':fsIfQosGTSIfName,_A0:fsIfQosGTSType,_A1:fsIfQosGTSACLNum,'fsIfQosGTSCIR':fsIfQosGTSCIR,'fsIfQosGTSBurstSize':fsIfQosGTSBurstSize,'fsIfQosGTSExcessBurstSize':fsIfQosGTSExcessBurstSize,'fsIfQosGTSMaxQueLen':fsIfQosGTSMaxQueLen,'fsIfQosGTSCurQueLen':fsIfQosGTSCurQueLen,'fsIfQosGTSPassPkt':fsIfQosGTSPassPkt,'fsIfQosGTSPassByte':fsIfQosGTSPassByte,'fsIfQosGTSDiscardPkt':fsIfQosGTSDiscardPkt,'fsIfQosGTSDiscardByte':fsIfQosGTSDiscardByte,'fsIfQosRTPIfQueueRunInfoTable':fsIfQosRTPIfQueueRunInfoTable,'fsIfQosRTPIfQueueRunInfoEntry':fsIfQosRTPIfQueueRunInfoEntry,_A2:fsIfQosRTPIfApplyIfIndex,'fsIfQosRTPIfQueueSize':fsIfQosRTPIfQueueSize,'fsIfQosRTPIfQueueMaxSize':fsIfQosRTPIfQueueMaxSize,'fsIfQosRTPIfQueueOutputs':fsIfQosRTPIfQueueOutputs,'fsIfQosRTPIfQueueDiscards':fsIfQosRTPIfQueueDiscards,'fsIfQosFlowLimitRunInfoTable':fsIfQosFlowLimitRunInfoTable,'fsIfQosFlowLimitRunInfoEntry':fsIfQosFlowLimitRunInfoEntry,_A3:fsIfQosFlowLimitLabelNum,_A4:fsIfQosFlowLimitPktDirection,'fsIfQosFlowLimitCIR':fsIfQosFlowLimitCIR,'fsIfQosFlowLimitBurstSize':fsIfQosFlowLimitBurstSize,'fsIfQosFlowLimitExcessBurstSize':fsIfQosFlowLimitExcessBurstSize,'fsIfQosFlowLimitConformAction':fsIfQosFlowLimitConformAction,'fsIfQosFlowLimitExceedAction':fsIfQosFlowLimitExceedAction,'fsIfQosFlowLimitConformNewPrec':fsIfQosFlowLimitConformNewPrec,'fsIfQosFlowLimitExceedNewPrec':fsIfQosFlowLimitExceedNewPrec,'fsIfQosFlowLimitConformPkt':fsIfQosFlowLimitConformPkt,'fsIfQosFlowLimitConformByte':fsIfQosFlowLimitConformByte,'fsIfQosFlowLimitExceedPkt':fsIfQosFlowLimitExceedPkt,'fsIfQosFlowLimitExceedByte':fsIfQosFlowLimitExceedByte,'fsHQoSMIBObjects':fsHQoSMIBObjects,'fsHQoSScalarObjects':fsHQoSScalarObjects,'fsHQoSNameType':fsHQoSNameType,'fsHQoSNameFind':fsHQoSNameFind,'fsHQoSNameIndex':fsHQoSNameIndex,'fsHQoSUserQObjects':fsHQoSUserQObjects,'fsHQoSUserQInIndexNext':fsHQoSUserQInIndexNext,'fsHQoSUserQOutIndexNext':fsHQoSUserQOutIndexNext,'fsHQoSUserQTable':fsHQoSUserQTable,'fsHQoSUserQEntry':fsHQoSUserQEntry,_A5:fsHQoSUserQIndex,'fsHQoSUserQName':fsHQoSUserQName,'fsHQoSUserQDirection':fsHQoSUserQDirection,'fsHQoSUserQRowStatus':fsHQoSUserQRowStatus,'fsHQoSUserQFlowQName':fsHQoSUserQFlowQName,'fsHQoSUserQFlowQIndex':fsHQoSUserQFlowQIndex,'fsHQoSUserQGroupName':fsHQoSUserQGroupName,'fsHQoSUserQGroupIndex':fsHQoSUserQGroupIndex,'fsHQoSUserQFlowMapName':fsHQoSUserQFlowMapName,'fsHQoSUserQFlowMapIndex':fsHQoSUserQFlowMapIndex,'fsHQoSUserQCIR':fsHQoSUserQCIR,'fsHQoSUserQPIR':fsHQoSUserQPIR,'fsHQoSUserGroupQObjects':fsHQoSUserGroupQObjects,'fsHQoSUserGroupQInIndexNext':fsHQoSUserGroupQInIndexNext,'fsHQoSUserGroupQOutIndexNext':fsHQoSUserGroupQOutIndexNext,'fsHQoSUserGroupQTable':fsHQoSUserGroupQTable,'fsHQoSUserGroupQEntry':fsHQoSUserGroupQEntry,_A6:fsHQoSUserGroupQIndex,'fsHQoSUserGroupQName':fsHQoSUserGroupQName,'fsHQoSUserGroupQDirection':fsHQoSUserGroupQDirection,'fsHQoSUserGroupQRowStatus':fsHQoSUserGroupQRowStatus,'fsHQoSUserGroupQShaping':fsHQoSUserGroupQShaping,'fsHQoSFlowQObjects':fsHQoSFlowQObjects,'fsHQoSFlowQIndexNext':fsHQoSFlowQIndexNext,'fsHQoSFlowQTable':fsHQoSFlowQTable,'fsHQoSFlowQEntry':fsHQoSFlowQEntry,_A7:fsHQoSFlowQIndex,'fsHQoSFlowQName':fsHQoSFlowQName,'fsHQoSFlowQRowStatus':fsHQoSFlowQRowStatus,'fsHQoSFlowQBEQType':fsHQoSFlowQBEQType,'fsHQoSFlowQBEQWredWeight':fsHQoSFlowQBEQWredWeight,'fsHQoSFlowQBEQWredName':fsHQoSFlowQBEQWredName,'fsHQoSFlowQBEQDepth':fsHQoSFlowQBEQDepth,'fsHQoSFlowQBEQShaping':fsHQoSFlowQBEQShaping,'fsHQoSFlowQAF1QType':fsHQoSFlowQAF1QType,'fsHQoSFlowQAF1QWredWeight':fsHQoSFlowQAF1QWredWeight,'fsHQoSFlowQAF1QWredName':fsHQoSFlowQAF1QWredName,'fsHQoSFlowQAF1QDepth':fsHQoSFlowQAF1QDepth,'fsHQoSFlowQAF1QShaping':fsHQoSFlowQAF1QShaping,'fsHQoSFlowQAF2QType':fsHQoSFlowQAF2QType,'fsHQoSFlowQAF2QWredWeight':fsHQoSFlowQAF2QWredWeight,'fsHQoSFlowQAF2QWredName':fsHQoSFlowQAF2QWredName,'fsHQoSFlowQAF2QDepth':fsHQoSFlowQAF2QDepth,'fsHQoSFlowQAF2QShaping':fsHQoSFlowQAF2QShaping,'fsHQoSFlowQAF3QType':fsHQoSFlowQAF3QType,'fsHQoSFlowQAF3QWredWeight':fsHQoSFlowQAF3QWredWeight,'fsHQoSFlowQAF3QWredName':fsHQoSFlowQAF3QWredName,'fsHQoSFlowQAF3QDepth':fsHQoSFlowQAF3QDepth,'fsHQoSFlowQAF3QShaping':fsHQoSFlowQAF3QShaping,'fsHQoSFlowQAF4QType':fsHQoSFlowQAF4QType,'fsHQoSFlowQAF4QWredWeight':fsHQoSFlowQAF4QWredWeight,'fsHQoSFlowQAF4QWredName':fsHQoSFlowQAF4QWredName,'fsHQoSFlowQAF4QDepth':fsHQoSFlowQAF4QDepth,'fsHQoSFlowQAF4QShaping':fsHQoSFlowQAF4QShaping,'fsHQoSFlowQEFQType':fsHQoSFlowQEFQType,'fsHQoSFlowQEFQWredWeight':fsHQoSFlowQEFQWredWeight,'fsHQoSFlowQEFQWredName':fsHQoSFlowQEFQWredName,'fsHQoSFlowQEFQDepth':fsHQoSFlowQEFQDepth,'fsHQoSFlowQEFQShaping':fsHQoSFlowQEFQShaping,'fsHQoSFlowQCS6QType':fsHQoSFlowQCS6QType,'fsHQoSFlowQCS6QWredWeight':fsHQoSFlowQCS6QWredWeight,'fsHQoSFlowQCS6QWredName':fsHQoSFlowQCS6QWredName,'fsHQoSFlowQCS6QDepth':fsHQoSFlowQCS6QDepth,'fsHQoSFlowQCS6QShaping':fsHQoSFlowQCS6QShaping,'fsHQoSFlowQCS7QType':fsHQoSFlowQCS7QType,'fsHQoSFlowQCS7QWredWeight':fsHQoSFlowQCS7QWredWeight,'fsHQoSFlowQCS7QWredName':fsHQoSFlowQCS7QWredName,'fsHQoSFlowQCS7QDepth':fsHQoSFlowQCS7QDepth,'fsHQoSFlowQCS7QShaping':fsHQoSFlowQCS7QShaping,'fsHQoSFlowMapObjects':fsHQoSFlowMapObjects,'fsHQoSFlowMapIndexNext':fsHQoSFlowMapIndexNext,'fsHQoSFlowMapTable':fsHQoSFlowMapTable,'fsHQoSFlowMapEntry':fsHQoSFlowMapEntry,_A8:fsHQoSFlowMapIndex,'fsHQoSFlowMapName':fsHQoSFlowMapName,'fsHQoSFlowMapRowStatus':fsHQoSFlowMapRowStatus,'fsHQoSFlowMapBEQ2PortQ':fsHQoSFlowMapBEQ2PortQ,'fsHQoSFlowMapAF1Q2PortQ':fsHQoSFlowMapAF1Q2PortQ,'fsHQoSFlowMapAF2Q2PortQ':fsHQoSFlowMapAF2Q2PortQ,'fsHQoSFlowMapAF3Q2PortQ':fsHQoSFlowMapAF3Q2PortQ,'fsHQoSFlowMapAF4Q2PortQ':fsHQoSFlowMapAF4Q2PortQ,'fsHQoSFlowMapEFQ2PortQ':fsHQoSFlowMapEFQ2PortQ,'fsHQoSFlowMapCS6Q2PortQ':fsHQoSFlowMapCS6Q2PortQ,'fsHQoSFlowMapCS7Q2PortQ':fsHQoSFlowMapCS7Q2PortQ,'fsHQoSTClassifierObjects':fsHQoSTClassifierObjects,'fsHQoSTClassifierIndexNext':fsHQoSTClassifierIndexNext,'fsHQoSTClassifierTable':fsHQoSTClassifierTable,'fsHQoSTClassifierEntry':fsHQoSTClassifierEntry,_A9:fsHQoSTClassifierIndex,_AA:fsHQoSTClassifierInstance,'fsHQoSTClassifierName':fsHQoSTClassifierName,'fsHQoSTClassifierType':fsHQoSTClassifierType,'fsHQoSTClassifierRowStatus':fsHQoSTClassifierRowStatus,'fsHQoSTClassifierMatchMask':fsHQoSTClassifierMatchMask,'fsHQoSTClassifierMatchV4Any':fsHQoSTClassifierMatchV4Any,'fsHQoSTClassifierMatchV4AclID':fsHQoSTClassifierMatchV4AclID,'fsHQoSTClassifierV4AclName':fsHQoSTClassifierV4AclName,'fsHQoSTClassifierMatchV4Dscp':fsHQoSTClassifierMatchV4Dscp,'fsHQoSTClassifierMatchV4Tos':fsHQoSTClassifierMatchV4Tos,'fsHQoSTClassifierMatchV6Any':fsHQoSTClassifierMatchV6Any,'fsHQoSTClassifierMatchV6AclID':fsHQoSTClassifierMatchV6AclID,'fsHQoSTClassifierV6AclName':fsHQoSTClassifierV6AclName,'fsHQoSTClassifierMatchV6Dscp':fsHQoSTClassifierMatchV6Dscp,'fsHQoSTClassifierMatchCos':fsHQoSTClassifierMatchCos,'fsHQoSTClassifierMatchExp':fsHQoSTClassifierMatchExp,'fsHQoSTClassifierMatchSrcMac':fsHQoSTClassifierMatchSrcMac,'fsHQoSTClassifierMatchDstMac':fsHQoSTClassifierMatchDstMac,'fsHQoSTBehaviorObjects':fsHQoSTBehaviorObjects,'fsHQoSTBehaviorIndexNext':fsHQoSTBehaviorIndexNext,'fsHQoSTBehaviorTable':fsHQoSTBehaviorTable,'fsHQoSTBehaviorEntry':fsHQoSTBehaviorEntry,_AB:fsHQoSTBehaviorIndex,'fsHQoSTBehaviorName':fsHQoSTBehaviorName,'fsHQoSTBehaviorRowStatus':fsHQoSTBehaviorRowStatus,'fsHQoSTBehaviorMask':fsHQoSTBehaviorMask,'fsHQoSTBehaviorUserQName':fsHQoSTBehaviorUserQName,'fsHQoSTBehaviorUserQDir':fsHQoSTBehaviorUserQDir,'fsHQoSTBehaviorTCos':fsHQoSTBehaviorTCos,'fsHQoSTBehaviorTColor':fsHQoSTBehaviorTColor,'fsHQoSTBehaviorRV4Dscp':fsHQoSTBehaviorRV4Dscp,'fsHQoSTBehaviorRV4Tos':fsHQoSTBehaviorRV4Tos,'fsHQoSTBehaviorRV6Dscp':fsHQoSTBehaviorRV6Dscp,'fsHQoSTBehaviorRVlanCos':fsHQoSTBehaviorRVlanCos,'fsHQoSTBehaviorRExp':fsHQoSTBehaviorRExp,'fsHQoSTBehaviorSubPolicyName':fsHQoSTBehaviorSubPolicyName,'fsHQoSTPolicyObjects':fsHQoSTPolicyObjects,'fsHQoSTPolicyIndexNext':fsHQoSTPolicyIndexNext,'fsHQoSTPolicyTable':fsHQoSTPolicyTable,'fsHQoSTPolicyEntry':fsHQoSTPolicyEntry,_AC:fsHQoSTPolicyIndex,'fsHQoSTPolicyName':fsHQoSTPolicyName,'fsHQoSTPolicyRowStatus':fsHQoSTPolicyRowStatus,'fsHQoSTPolicyMapIndexNext':fsHQoSTPolicyMapIndexNext,'fsHQoSTPolicyMapTable':fsHQoSTPolicyMapTable,'fsHQoSTPolicyMapEntry':fsHQoSTPolicyMapEntry,_AD:fsHQoSTPolicyMapIndex,'fsHQoSTPolicyMapPolicyName':fsHQoSTPolicyMapPolicyName,'fsHQoSTPolicyMapPolicyIndex':fsHQoSTPolicyMapPolicyIndex,'fsHQoSTPolicyMapTClassfierName':fsHQoSTPolicyMapTClassfierName,'fsHQoSTPolicyMapTClassfierIndex':fsHQoSTPolicyMapTClassfierIndex,'fsHQoSTPolicyMapTBehaviorName':fsHQoSTPolicyMapTBehaviorName,'fsHQoSTPolicyMapTBehaviorIndex':fsHQoSTPolicyMapTBehaviorIndex,'fsHQoSTPolicyMapPrecedence':fsHQoSTPolicyMapPrecedence,'fsHQoSTPolicyMapRowStatus':fsHQoSTPolicyMapRowStatus,'fsHQoSVoQObjects':fsHQoSVoQObjects,'fsHQoSVoQEnable':fsHQoSVoQEnable,'fsHQoSVoQDeviceTable':fsHQoSVoQDeviceTable,'fsHQoSVoQDeviceEntry':fsHQoSVoQDeviceEntry,_AE:fsHQoSVoQDeviceId,'fsHQoSVoQDeviceCredit':fsHQoSVoQDeviceCredit,'fsHQoSPortQObjects':fsHQoSPortQObjects,'fsHQoSPortQIndexNext':fsHQoSPortQIndexNext,'fsHQoSPortQTable':fsHQoSPortQTable,'fsHQoSPortQEntry':fsHQoSPortQEntry,_AF:fsHQoSPortQIndex,'fsHQoSPortQName':fsHQoSPortQName,'fsHQoSPortQRowStatus':fsHQoSPortQRowStatus,'fsHQoSPortQBEQType':fsHQoSPortQBEQType,'fsHQoSPortQBEQWredWeight':fsHQoSPortQBEQWredWeight,'fsHQoSPortQBEQWredName':fsHQoSPortQBEQWredName,'fsHQoSPortQBEQDepth':fsHQoSPortQBEQDepth,'fsHQoSPortQBEQShaping':fsHQoSPortQBEQShaping,'fsHQoSPortQAF1QType':fsHQoSPortQAF1QType,'fsHQoSPortQAF1QWredWeight':fsHQoSPortQAF1QWredWeight,'fsHQoSPortQAF1QWredName':fsHQoSPortQAF1QWredName,'fsHQoSPortQAF1QDepth':fsHQoSPortQAF1QDepth,'fsHQoSPortQAF1QShaping':fsHQoSPortQAF1QShaping,'fsHQoSPortQAF2QType':fsHQoSPortQAF2QType,'fsHQoSPortQAF2QWredWeight':fsHQoSPortQAF2QWredWeight,'fsHQoSPortQAF2QWredName':fsHQoSPortQAF2QWredName,'fsHQoSPortQAF2QDepth':fsHQoSPortQAF2QDepth,'fsHQoSPortQAF2QShaping':fsHQoSPortQAF2QShaping,'fsHQoSPortQAF3QType':fsHQoSPortQAF3QType,'fsHQoSPortQAF3QWredWeight':fsHQoSPortQAF3QWredWeight,'fsHQoSPortQAF3QWredName':fsHQoSPortQAF3QWredName,'fsHQoSPortQAF3QDepth':fsHQoSPortQAF3QDepth,'fsHQoSPortQAF3QShaping':fsHQoSPortQAF3QShaping,'fsHQoSPortQAF4QType':fsHQoSPortQAF4QType,'fsHQoSPortQAF4QWredWeight':fsHQoSPortQAF4QWredWeight,'fsHQoSPortQAF4QWredName':fsHQoSPortQAF4QWredName,'fsHQoSPortQAF4QDepth':fsHQoSPortQAF4QDepth,'fsHQoSPortQAF4QShaping':fsHQoSPortQAF4QShaping,'fsHQoSPortQEFQType':fsHQoSPortQEFQType,'fsHQoSPortQEFQWredWeight':fsHQoSPortQEFQWredWeight,'fsHQoSPortQEFQWredName':fsHQoSPortQEFQWredName,'fsHQoSPortQEFQDepth':fsHQoSPortQEFQDepth,'fsHQoSPortQEFQShaping':fsHQoSPortQEFQShaping,'fsHQoSPortQCS6QType':fsHQoSPortQCS6QType,'fsHQoSPortQCS6QWredWeight':fsHQoSPortQCS6QWredWeight,'fsHQoSPortQCS6QWredName':fsHQoSPortQCS6QWredName,'fsHQoSPortQCS6QDepth':fsHQoSPortQCS6QDepth,'fsHQoSPortQCS6QShaping':fsHQoSPortQCS6QShaping,'fsHQoSPortQCS7QType':fsHQoSPortQCS7QType,'fsHQoSPortQCS7QWredWeight':fsHQoSPortQCS7QWredWeight,'fsHQoSPortQCS7QWredName':fsHQoSPortQCS7QWredName,'fsHQoSPortQCS7QDepth':fsHQoSPortQCS7QDepth,'fsHQoSPortQCS7QShaping':fsHQoSPortQCS7QShaping,'fsHQoSIfAppObjects':fsHQoSIfAppObjects,'fsHQoSIfAppTable':fsHQoSIfAppTable,'fsHQoSIfAppEntry':fsHQoSIfAppEntry,_AG:fsHQoSIfAppIndex,'fsHQoSIfAppInPolicyName':fsHQoSIfAppInPolicyName,'fsHQoSIfAppInPolicyIndex':fsHQoSIfAppInPolicyIndex,'fsHQoSIfAppInPolicyLayer':fsHQoSIfAppInPolicyLayer,'fsHQoSIfAppOutPolicyName':fsHQoSIfAppOutPolicyName,'fsHQoSIfAppOutPolicyIndex':fsHQoSIfAppOutPolicyIndex,'fsHQoSIfAppOutPolicyLayer':fsHQoSIfAppOutPolicyLayer,'fsHQoSIfAppPortQueueName':fsHQoSIfAppPortQueueName,'fsHQoSIfAppPortQueueIndex':fsHQoSIfAppPortQueueIndex,'fsHQoSIfAppPortQueueShaping':fsHQoSIfAppPortQueueShaping})