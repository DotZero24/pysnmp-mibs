_AA='qosIfBandwidthIfIndex'
_A9='qosLRIfIndex'
_A8='qosGTSACLNum'
_A7='qosGTSType'
_A6='qosGTSIfIndex'
_A5='remark-mplsexp-pass'
_A4='remark-mplsexp-continue'
_A3='remark-prec-pass'
_A2='remark-prec-continue'
_A1='qosCARExcessBurstSize'
_A0='qosCARBurstSize'
_z='qosCARCIR'
_y='qosCARListNum'
_x='qosCARType'
_w='qosCARPktDirection'
_v='qosCARIfIndex'
_u='qosCarlListNum'
_t='qosWREDPrecedence'
_s='qosWREDPreIfIndex'
_r='qosWREDIfIndex'
_q='qosWFQIfIndex'
_p='qosCQRunInfoQueNum'
_o='qosCQRunInfoIfIndex'
_n='qosCQIfIndex'
_m='qosCqlQueParaMaxQueLen'
_l='qosCqlQueParaServing'
_k='qosCqlQueParaQueNum'
_j='qosCqlQueParaListNum'
_i='qosCqlProQueKeyValue'
_h='qosCqlProQueKey'
_g='qosCqlProName'
_f='qosCqlProListNum'
_e='qosCqlIfIndex'
_d='qosCqlIfListNum'
_c='qosCqlListNum'
_b='qosPQIfIndex'
_a='exp-mask'
_Z='greater-than'
_Y='less-than'
_X='fragment'
_W='qosPqlProQueKeyValue'
_V='qosPqlProQueKey'
_U='qosPqlProName'
_T='qosPqlProListNum'
_S='qosPqlIfIndex'
_R='qosPqlIfListNum'
_Q='qosPqlQueLenQueueType'
_P='qosPqlQueLenListNum'
_O='qosPqlDefaultListNum'
_N='qosFIFOIfIndex'
_M='qosRTPIfApplyIfIndex'
_L='acl'
_K='bottom'
_J='normal'
_I='middle'
_H='top'
_G='read-create'
_F='not-accessible'
_E='A3COM-HUAWEI-QOS-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huawei,hwInternetProtocol,hwLocal,vrpProtocol=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huawei','hwInternetProtocol','hwLocal','vrpProtocol')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hwIfQoSMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,1,3,3,2))
_QosFIFOTable_Object=MibTable
qosFIFOTable=_QosFIFOTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1))
if mibBuilder.loadTexts:qosFIFOTable.setStatus(_A)
_QosFIFOEntry_Object=MibTableRow
qosFIFOEntry=_QosFIFOEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1))
qosFIFOEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:qosFIFOEntry.setStatus(_A)
_QosFIFOIfIndex_Type=Integer32
_QosFIFOIfIndex_Object=MibTableColumn
qosFIFOIfIndex=_QosFIFOIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1,1),_QosFIFOIfIndex_Type())
qosFIFOIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosFIFOIfIndex.setStatus(_A)
_QosFIFOIfName_Type=OctetString
_QosFIFOIfName_Object=MibTableColumn
qosFIFOIfName=_QosFIFOIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1,2),_QosFIFOIfName_Type())
qosFIFOIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosFIFOIfName.setStatus(_A)
class _QosFIFOMaxQueueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosFIFOMaxQueueLen_Type.__name__=_B
_QosFIFOMaxQueueLen_Object=MibTableColumn
qosFIFOMaxQueueLen=_QosFIFOMaxQueueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1,3),_QosFIFOMaxQueueLen_Type())
qosFIFOMaxQueueLen.setMaxAccess(_D)
if mibBuilder.loadTexts:qosFIFOMaxQueueLen.setStatus(_A)
_QosFIFOCurQueueLen_Type=Integer32
_QosFIFOCurQueueLen_Object=MibTableColumn
qosFIFOCurQueueLen=_QosFIFOCurQueueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1,4),_QosFIFOCurQueueLen_Type())
qosFIFOCurQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosFIFOCurQueueLen.setStatus(_A)
_QosFIFODiscardPkt_Type=Counter32
_QosFIFODiscardPkt_Object=MibTableColumn
qosFIFODiscardPkt=_QosFIFODiscardPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1,5),_QosFIFODiscardPkt_Type())
qosFIFODiscardPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosFIFODiscardPkt.setStatus(_A)
class _QosUndoFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosFIFO',0),('qosNoFIFO',1)))
_QosUndoFIFO_Type.__name__=_B
_QosUndoFIFO_Object=MibTableColumn
qosUndoFIFO=_QosUndoFIFO_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,1,1,6),_QosUndoFIFO_Type())
qosUndoFIFO.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoFIFO.setStatus(_A)
_QosPqlDefaultTable_Object=MibTable
qosPqlDefaultTable=_QosPqlDefaultTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,2))
if mibBuilder.loadTexts:qosPqlDefaultTable.setStatus(_A)
_QosPqlDefaultEntry_Object=MibTableRow
qosPqlDefaultEntry=_QosPqlDefaultEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,2,1))
qosPqlDefaultEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:qosPqlDefaultEntry.setStatus(_A)
class _QosPqlDefaultListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosPqlDefaultListNum_Type.__name__=_B
_QosPqlDefaultListNum_Object=MibTableColumn
qosPqlDefaultListNum=_QosPqlDefaultListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,2,1,1),_QosPqlDefaultListNum_Type())
qosPqlDefaultListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlDefaultListNum.setStatus(_A)
class _QosPqlDefaultQueueType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3)))
_QosPqlDefaultQueueType_Type.__name__=_B
_QosPqlDefaultQueueType_Object=MibTableColumn
qosPqlDefaultQueueType=_QosPqlDefaultQueueType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,2,1,2),_QosPqlDefaultQueueType_Type())
qosPqlDefaultQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:qosPqlDefaultQueueType.setStatus(_A)
class _QosUndoPqlDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosPqlDefault',0),('qosNoPqlDefault',1)))
_QosUndoPqlDefault_Type.__name__=_B
_QosUndoPqlDefault_Object=MibTableColumn
qosUndoPqlDefault=_QosUndoPqlDefault_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,2,1,3),_QosUndoPqlDefault_Type())
qosUndoPqlDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoPqlDefault.setStatus(_A)
_QosPqlQueueLenTable_Object=MibTable
qosPqlQueueLenTable=_QosPqlQueueLenTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,3))
if mibBuilder.loadTexts:qosPqlQueueLenTable.setStatus(_A)
_QosPqlQueueLenEntry_Object=MibTableRow
qosPqlQueueLenEntry=_QosPqlQueueLenEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,3,1))
qosPqlQueueLenEntry.setIndexNames((0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:qosPqlQueueLenEntry.setStatus(_A)
class _QosPqlQueLenListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosPqlQueLenListNum_Type.__name__=_B
_QosPqlQueLenListNum_Object=MibTableColumn
qosPqlQueLenListNum=_QosPqlQueLenListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,3,1,1),_QosPqlQueLenListNum_Type())
qosPqlQueLenListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlQueLenListNum.setStatus(_A)
class _QosPqlQueLenQueueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3)))
_QosPqlQueLenQueueType_Type.__name__=_B
_QosPqlQueLenQueueType_Object=MibTableColumn
qosPqlQueLenQueueType=_QosPqlQueLenQueueType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,3,1,2),_QosPqlQueLenQueueType_Type())
qosPqlQueLenQueueType.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlQueLenQueueType.setStatus(_A)
class _QosPqlQueLenValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosPqlQueLenValue_Type.__name__=_B
_QosPqlQueLenValue_Object=MibTableColumn
qosPqlQueLenValue=_QosPqlQueLenValue_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,3,1,3),_QosPqlQueLenValue_Type())
qosPqlQueLenValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qosPqlQueLenValue.setStatus(_A)
class _QosUndoPqlQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosPqlQueLen',0),('qosNoPqlQueLen',1)))
_QosUndoPqlQueLen_Type.__name__=_B
_QosUndoPqlQueLen_Object=MibTableColumn
qosUndoPqlQueLen=_QosUndoPqlQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,3,1,4),_QosUndoPqlQueLen_Type())
qosUndoPqlQueLen.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoPqlQueLen.setStatus(_A)
_QosPqlIfTable_Object=MibTable
qosPqlIfTable=_QosPqlIfTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4))
if mibBuilder.loadTexts:qosPqlIfTable.setStatus(_A)
_QosPqlIfEntry_Object=MibTableRow
qosPqlIfEntry=_QosPqlIfEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4,1))
qosPqlIfEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:qosPqlIfEntry.setStatus(_A)
_QosPqlIfListNum_Type=Integer32
_QosPqlIfListNum_Object=MibTableColumn
qosPqlIfListNum=_QosPqlIfListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4,1,1),_QosPqlIfListNum_Type())
qosPqlIfListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlIfListNum.setStatus(_A)
_QosPqlIfIndex_Type=Integer32
_QosPqlIfIndex_Object=MibTableColumn
qosPqlIfIndex=_QosPqlIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4,1,2),_QosPqlIfIndex_Type())
qosPqlIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlIfIndex.setStatus(_A)
_QosPqlIfName_Type=OctetString
_QosPqlIfName_Object=MibTableColumn
qosPqlIfName=_QosPqlIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4,1,3),_QosPqlIfName_Type())
qosPqlIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPqlIfName.setStatus(_A)
class _QosPqlIfQueueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3)))
_QosPqlIfQueueType_Type.__name__=_B
_QosPqlIfQueueType_Object=MibTableColumn
qosPqlIfQueueType=_QosPqlIfQueueType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4,1,4),_QosPqlIfQueueType_Type())
qosPqlIfQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:qosPqlIfQueueType.setStatus(_A)
class _QosUndoPqlIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosPqlIF',0),('qosNoPqlIF',1)))
_QosUndoPqlIf_Type.__name__=_B
_QosUndoPqlIf_Object=MibTableColumn
qosUndoPqlIf=_QosUndoPqlIf_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,4,1,5),_QosUndoPqlIf_Type())
qosUndoPqlIf.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoPqlIf.setStatus(_A)
_QosPqlProtocolTable_Object=MibTable
qosPqlProtocolTable=_QosPqlProtocolTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5))
if mibBuilder.loadTexts:qosPqlProtocolTable.setStatus(_A)
_QosPqlProtocolEntry_Object=MibTableRow
qosPqlProtocolEntry=_QosPqlProtocolEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1))
qosPqlProtocolEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:qosPqlProtocolEntry.setStatus(_A)
_QosPqlProListNum_Type=Integer32
_QosPqlProListNum_Object=MibTableColumn
qosPqlProListNum=_QosPqlProListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1,1),_QosPqlProListNum_Type())
qosPqlProListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlProListNum.setStatus(_A)
class _QosPqlProName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('mpls',2)))
_QosPqlProName_Type.__name__=_B
_QosPqlProName_Object=MibTableColumn
qosPqlProName=_QosPqlProName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1,2),_QosPqlProName_Type())
qosPqlProName.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlProName.setStatus(_A)
class _QosPqlProQueKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('null',1),(_X,2),(_L,3),(_Y,4),(_Z,5),('tcp',6),('udp',7),(_a,8)))
_QosPqlProQueKey_Type.__name__=_B
_QosPqlProQueKey_Object=MibTableColumn
qosPqlProQueKey=_QosPqlProQueKey_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1,3),_QosPqlProQueKey_Type())
qosPqlProQueKey.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlProQueKey.setStatus(_A)
class _QosPqlProQueKeyValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosPqlProQueKeyValue_Type.__name__=_B
_QosPqlProQueKeyValue_Object=MibTableColumn
qosPqlProQueKeyValue=_QosPqlProQueKeyValue_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1,4),_QosPqlProQueKeyValue_Type())
qosPqlProQueKeyValue.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPqlProQueKeyValue.setStatus(_A)
class _QosPqlProQueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3)))
_QosPqlProQueType_Type.__name__=_B
_QosPqlProQueType_Object=MibTableColumn
qosPqlProQueType=_QosPqlProQueType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1,5),_QosPqlProQueType_Type())
qosPqlProQueType.setMaxAccess(_D)
if mibBuilder.loadTexts:qosPqlProQueType.setStatus(_A)
class _QosUndoPqlProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosPqlProtocol',0),('qosNoPqlProtocol',1)))
_QosUndoPqlProtocol_Type.__name__=_B
_QosUndoPqlProtocol_Object=MibTableColumn
qosUndoPqlProtocol=_QosUndoPqlProtocol_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,5,1,6),_QosUndoPqlProtocol_Type())
qosUndoPqlProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoPqlProtocol.setStatus(_A)
_QosPQTable_Object=MibTable
qosPQTable=_QosPQTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6))
if mibBuilder.loadTexts:qosPQTable.setStatus(_A)
_QosPQEntry_Object=MibTableRow
qosPQEntry=_QosPQEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1))
qosPQEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:qosPQEntry.setStatus(_A)
_QosPQIfIndex_Type=Integer32
_QosPQIfIndex_Object=MibTableColumn
qosPQIfIndex=_QosPQIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,1),_QosPQIfIndex_Type())
qosPQIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosPQIfIndex.setStatus(_A)
class _QosPQListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosPQListNum_Type.__name__=_B
_QosPQListNum_Object=MibTableColumn
qosPQListNum=_QosPQListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,2),_QosPQListNum_Type())
qosPQListNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qosPQListNum.setStatus(_A)
_QosPQIfName_Type=OctetString
_QosPQIfName_Object=MibTableColumn
qosPQIfName=_QosPQIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,3),_QosPQIfName_Type())
qosPQIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQIfName.setStatus(_A)
class _QosPQTopPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosPQTopPkt_Type.__name__=_B
_QosPQTopPkt_Object=MibTableColumn
qosPQTopPkt=_QosPQTopPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,4),_QosPQTopPkt_Type())
qosPQTopPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQTopPkt.setStatus(_A)
_QosPQTopDiscard_Type=Counter32
_QosPQTopDiscard_Object=MibTableColumn
qosPQTopDiscard=_QosPQTopDiscard_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,5),_QosPQTopDiscard_Type())
qosPQTopDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQTopDiscard.setStatus(_A)
class _QosPQTopMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosPQTopMaxQueLen_Type.__name__=_B
_QosPQTopMaxQueLen_Object=MibTableColumn
qosPQTopMaxQueLen=_QosPQTopMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,6),_QosPQTopMaxQueLen_Type())
qosPQTopMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQTopMaxQueLen.setStatus(_A)
class _QosPQMiddlePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosPQMiddlePkt_Type.__name__=_B
_QosPQMiddlePkt_Object=MibTableColumn
qosPQMiddlePkt=_QosPQMiddlePkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,7),_QosPQMiddlePkt_Type())
qosPQMiddlePkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQMiddlePkt.setStatus(_A)
_QosPQMiddleDiscard_Type=Counter32
_QosPQMiddleDiscard_Object=MibTableColumn
qosPQMiddleDiscard=_QosPQMiddleDiscard_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,8),_QosPQMiddleDiscard_Type())
qosPQMiddleDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQMiddleDiscard.setStatus(_A)
class _QosPQMiddleMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosPQMiddleMaxQueLen_Type.__name__=_B
_QosPQMiddleMaxQueLen_Object=MibTableColumn
qosPQMiddleMaxQueLen=_QosPQMiddleMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,9),_QosPQMiddleMaxQueLen_Type())
qosPQMiddleMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQMiddleMaxQueLen.setStatus(_A)
class _QosPQNormalPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosPQNormalPkt_Type.__name__=_B
_QosPQNormalPkt_Object=MibTableColumn
qosPQNormalPkt=_QosPQNormalPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,10),_QosPQNormalPkt_Type())
qosPQNormalPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQNormalPkt.setStatus(_A)
_QosPQNormalDiscard_Type=Counter32
_QosPQNormalDiscard_Object=MibTableColumn
qosPQNormalDiscard=_QosPQNormalDiscard_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,11),_QosPQNormalDiscard_Type())
qosPQNormalDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQNormalDiscard.setStatus(_A)
class _QosPQNormalMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosPQNormalMaxQueLen_Type.__name__=_B
_QosPQNormalMaxQueLen_Object=MibTableColumn
qosPQNormalMaxQueLen=_QosPQNormalMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,12),_QosPQNormalMaxQueLen_Type())
qosPQNormalMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQNormalMaxQueLen.setStatus(_A)
class _QosPQBottomPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosPQBottomPkt_Type.__name__=_B
_QosPQBottomPkt_Object=MibTableColumn
qosPQBottomPkt=_QosPQBottomPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,13),_QosPQBottomPkt_Type())
qosPQBottomPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQBottomPkt.setStatus(_A)
_QosPQBottomDiscard_Type=Counter32
_QosPQBottomDiscard_Object=MibTableColumn
qosPQBottomDiscard=_QosPQBottomDiscard_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,14),_QosPQBottomDiscard_Type())
qosPQBottomDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQBottomDiscard.setStatus(_A)
class _QosPQBottomMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosPQBottomMaxQueLen_Type.__name__=_B
_QosPQBottomMaxQueLen_Object=MibTableColumn
qosPQBottomMaxQueLen=_QosPQBottomMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,15),_QosPQBottomMaxQueLen_Type())
qosPQBottomMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPQBottomMaxQueLen.setStatus(_A)
class _QosUndoPQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosPQ',0),('qosNoPQ',1)))
_QosUndoPQ_Type.__name__=_B
_QosUndoPQ_Object=MibTableColumn
qosUndoPQ=_QosUndoPQ_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,6,1,16),_QosUndoPQ_Type())
qosUndoPQ.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoPQ.setStatus(_A)
_QosCqlDefaultTable_Object=MibTable
qosCqlDefaultTable=_QosCqlDefaultTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,7))
if mibBuilder.loadTexts:qosCqlDefaultTable.setStatus(_A)
_QosCqlDefaultEntry_Object=MibTableRow
qosCqlDefaultEntry=_QosCqlDefaultEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,7,1))
qosCqlDefaultEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:qosCqlDefaultEntry.setStatus(_A)
class _QosCqlListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosCqlListNum_Type.__name__=_B
_QosCqlListNum_Object=MibTableColumn
qosCqlListNum=_QosCqlListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,7,1,1),_QosCqlListNum_Type())
qosCqlListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlListNum.setStatus(_A)
class _QosCqlQueueNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosCqlQueueNum_Type.__name__=_B
_QosCqlQueueNum_Object=MibTableColumn
qosCqlQueueNum=_QosCqlQueueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,7,1,2),_QosCqlQueueNum_Type())
qosCqlQueueNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCqlQueueNum.setStatus(_A)
class _QosUndoCqlDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosCqlDefault',0),('qosNoCqlDefault',1)))
_QosUndoCqlDefault_Type.__name__=_B
_QosUndoCqlDefault_Object=MibTableColumn
qosUndoCqlDefault=_QosUndoCqlDefault_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,7,1,3),_QosUndoCqlDefault_Type())
qosUndoCqlDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCqlDefault.setStatus(_A)
_QosCqlIfTable_Object=MibTable
qosCqlIfTable=_QosCqlIfTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8))
if mibBuilder.loadTexts:qosCqlIfTable.setStatus(_A)
_QosCqlIfEntry_Object=MibTableRow
qosCqlIfEntry=_QosCqlIfEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8,1))
qosCqlIfEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:qosCqlIfEntry.setStatus(_A)
_QosCqlIfListNum_Type=Integer32
_QosCqlIfListNum_Object=MibTableColumn
qosCqlIfListNum=_QosCqlIfListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8,1,1),_QosCqlIfListNum_Type())
qosCqlIfListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlIfListNum.setStatus(_A)
_QosCqlIfIndex_Type=Integer32
_QosCqlIfIndex_Object=MibTableColumn
qosCqlIfIndex=_QosCqlIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8,1,2),_QosCqlIfIndex_Type())
qosCqlIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlIfIndex.setStatus(_A)
_QosCqlIfName_Type=OctetString
_QosCqlIfName_Object=MibTableColumn
qosCqlIfName=_QosCqlIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8,1,3),_QosCqlIfName_Type())
qosCqlIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCqlIfName.setStatus(_A)
class _QosCqlIfQueueNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosCqlIfQueueNum_Type.__name__=_B
_QosCqlIfQueueNum_Object=MibTableColumn
qosCqlIfQueueNum=_QosCqlIfQueueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8,1,4),_QosCqlIfQueueNum_Type())
qosCqlIfQueueNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCqlIfQueueNum.setStatus(_A)
class _QosUndoCqlIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosCqlIf',0),('qosNoCqlIf',1)))
_QosUndoCqlIf_Type.__name__=_B
_QosUndoCqlIf_Object=MibTableColumn
qosUndoCqlIf=_QosUndoCqlIf_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,8,1,5),_QosUndoCqlIf_Type())
qosUndoCqlIf.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCqlIf.setStatus(_A)
_QosCqlProtocolTable_Object=MibTable
qosCqlProtocolTable=_QosCqlProtocolTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9))
if mibBuilder.loadTexts:qosCqlProtocolTable.setStatus(_A)
_QosCqlProtocolEntry_Object=MibTableRow
qosCqlProtocolEntry=_QosCqlProtocolEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1))
qosCqlProtocolEntry.setIndexNames((0,_E,_f),(0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:qosCqlProtocolEntry.setStatus(_A)
_QosCqlProListNum_Type=Integer32
_QosCqlProListNum_Object=MibTableColumn
qosCqlProListNum=_QosCqlProListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1,1),_QosCqlProListNum_Type())
qosCqlProListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlProListNum.setStatus(_A)
class _QosCqlProName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('mpls',2)))
_QosCqlProName_Type.__name__=_B
_QosCqlProName_Object=MibTableColumn
qosCqlProName=_QosCqlProName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1,2),_QosCqlProName_Type())
qosCqlProName.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlProName.setStatus(_A)
class _QosCqlProQueKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('null',1),(_X,2),(_L,3),(_Y,4),(_Z,5),('tcp',6),('udp',7),(_a,8)))
_QosCqlProQueKey_Type.__name__=_B
_QosCqlProQueKey_Object=MibTableColumn
qosCqlProQueKey=_QosCqlProQueKey_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1,3),_QosCqlProQueKey_Type())
qosCqlProQueKey.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlProQueKey.setStatus(_A)
class _QosCqlProQueKeyValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosCqlProQueKeyValue_Type.__name__=_B
_QosCqlProQueKeyValue_Object=MibTableColumn
qosCqlProQueKeyValue=_QosCqlProQueKeyValue_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1,4),_QosCqlProQueKeyValue_Type())
qosCqlProQueKeyValue.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlProQueKeyValue.setStatus(_A)
class _QosCqlProQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosCqlProQueNum_Type.__name__=_B
_QosCqlProQueNum_Object=MibTableColumn
qosCqlProQueNum=_QosCqlProQueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1,5),_QosCqlProQueNum_Type())
qosCqlProQueNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCqlProQueNum.setStatus(_A)
class _QosUndoCqlProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosCqlProtocol',0),('qosNoCqlProtocol',1)))
_QosUndoCqlProtocol_Type.__name__=_B
_QosUndoCqlProtocol_Object=MibTableColumn
qosUndoCqlProtocol=_QosUndoCqlProtocol_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,9,1,6),_QosUndoCqlProtocol_Type())
qosUndoCqlProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCqlProtocol.setStatus(_A)
_QosCqlQueParaTable_Object=MibTable
qosCqlQueParaTable=_QosCqlQueParaTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10))
if mibBuilder.loadTexts:qosCqlQueParaTable.setStatus(_A)
_QosCqlQueParaEntry_Object=MibTableRow
qosCqlQueParaEntry=_QosCqlQueParaEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1))
qosCqlQueParaEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:qosCqlQueParaEntry.setStatus(_A)
_QosCqlQueParaListNum_Type=Integer32
_QosCqlQueParaListNum_Object=MibTableColumn
qosCqlQueParaListNum=_QosCqlQueParaListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1,1),_QosCqlQueParaListNum_Type())
qosCqlQueParaListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlQueParaListNum.setStatus(_A)
class _QosCqlQueParaQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosCqlQueParaQueNum_Type.__name__=_B
_QosCqlQueParaQueNum_Object=MibTableColumn
qosCqlQueParaQueNum=_QosCqlQueParaQueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1,2),_QosCqlQueParaQueNum_Type())
qosCqlQueParaQueNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCqlQueParaQueNum.setStatus(_A)
class _QosCqlQueParaServing_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_QosCqlQueParaServing_Type.__name__=_B
_QosCqlQueParaServing_Object=MibTableColumn
qosCqlQueParaServing=_QosCqlQueParaServing_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1,3),_QosCqlQueParaServing_Type())
qosCqlQueParaServing.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCqlQueParaServing.setStatus(_A)
class _QosCqlQueParaMaxQueLen_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosCqlQueParaMaxQueLen_Type.__name__=_B
_QosCqlQueParaMaxQueLen_Object=MibTableColumn
qosCqlQueParaMaxQueLen=_QosCqlQueParaMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1,4),_QosCqlQueParaMaxQueLen_Type())
qosCqlQueParaMaxQueLen.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCqlQueParaMaxQueLen.setStatus(_A)
class _QosUndoCqlQueParaServing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_l,0),('qosNoCqlQueParaServing',1)))
_QosUndoCqlQueParaServing_Type.__name__=_B
_QosUndoCqlQueParaServing_Object=MibTableColumn
qosUndoCqlQueParaServing=_QosUndoCqlQueParaServing_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1,5),_QosUndoCqlQueParaServing_Type())
qosUndoCqlQueParaServing.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCqlQueParaServing.setStatus(_A)
class _QosUndoCqlQueParaMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_m,0),('qosNoCqlQueParaMaxQueLen',1)))
_QosUndoCqlQueParaMaxQueLen_Type.__name__=_B
_QosUndoCqlQueParaMaxQueLen_Object=MibTableColumn
qosUndoCqlQueParaMaxQueLen=_QosUndoCqlQueParaMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,10,1,6),_QosUndoCqlQueParaMaxQueLen_Type())
qosUndoCqlQueParaMaxQueLen.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCqlQueParaMaxQueLen.setStatus(_A)
_QosCQTable_Object=MibTable
qosCQTable=_QosCQTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,11))
if mibBuilder.loadTexts:qosCQTable.setStatus(_A)
_QosCQEntry_Object=MibTableRow
qosCQEntry=_QosCQEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,11,1))
qosCQEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:qosCQEntry.setStatus(_A)
_QosCQIfIndex_Type=Integer32
_QosCQIfIndex_Object=MibTableColumn
qosCQIfIndex=_QosCQIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,11,1,1),_QosCQIfIndex_Type())
qosCQIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCQIfIndex.setStatus(_A)
class _QosCQListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosCQListNum_Type.__name__=_B
_QosCQListNum_Object=MibTableColumn
qosCQListNum=_QosCQListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,11,1,2),_QosCQListNum_Type())
qosCQListNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCQListNum.setStatus(_A)
_QosCQIfName_Type=OctetString
_QosCQIfName_Object=MibTableColumn
qosCQIfName=_QosCQIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,11,1,3),_QosCQIfName_Type())
qosCQIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCQIfName.setStatus(_A)
class _QosUndoCQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosCQ',0),('qosNoCQ',1)))
_QosUndoCQ_Type.__name__=_B
_QosUndoCQ_Object=MibTableColumn
qosUndoCQ=_QosUndoCQ_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,11,1,4),_QosUndoCQ_Type())
qosUndoCQ.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCQ.setStatus(_A)
_QosCQRunInfoTable_Object=MibTable
qosCQRunInfoTable=_QosCQRunInfoTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12))
if mibBuilder.loadTexts:qosCQRunInfoTable.setStatus(_A)
_QosCQRunInfoEntry_Object=MibTableRow
qosCQRunInfoEntry=_QosCQRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1))
qosCQRunInfoEntry.setIndexNames((0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:qosCQRunInfoEntry.setStatus(_A)
_QosCQRunInfoIfIndex_Type=Integer32
_QosCQRunInfoIfIndex_Object=MibTableColumn
qosCQRunInfoIfIndex=_QosCQRunInfoIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1,1),_QosCQRunInfoIfIndex_Type())
qosCQRunInfoIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCQRunInfoIfIndex.setStatus(_A)
class _QosCQRunInfoQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QosCQRunInfoQueNum_Type.__name__=_B
_QosCQRunInfoQueNum_Object=MibTableColumn
qosCQRunInfoQueNum=_QosCQRunInfoQueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1,2),_QosCQRunInfoQueNum_Type())
qosCQRunInfoQueNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCQRunInfoQueNum.setStatus(_A)
_QosCQRunInfoIfName_Type=OctetString
_QosCQRunInfoIfName_Object=MibTableColumn
qosCQRunInfoIfName=_QosCQRunInfoIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1,3),_QosCQRunInfoIfName_Type())
qosCQRunInfoIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCQRunInfoIfName.setStatus(_A)
class _QosCQRunInfoQuePkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosCQRunInfoQuePkt_Type.__name__=_B
_QosCQRunInfoQuePkt_Object=MibTableColumn
qosCQRunInfoQuePkt=_QosCQRunInfoQuePkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1,4),_QosCQRunInfoQuePkt_Type())
qosCQRunInfoQuePkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCQRunInfoQuePkt.setStatus(_A)
_QosCQRunInfoQueDiscard_Type=Counter32
_QosCQRunInfoQueDiscard_Object=MibTableColumn
qosCQRunInfoQueDiscard=_QosCQRunInfoQueDiscard_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1,5),_QosCQRunInfoQueDiscard_Type())
qosCQRunInfoQueDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCQRunInfoQueDiscard.setStatus(_A)
class _QosCQRunInfoMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosCQRunInfoMaxQueLen_Type.__name__=_B
_QosCQRunInfoMaxQueLen_Object=MibTableColumn
qosCQRunInfoMaxQueLen=_QosCQRunInfoMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,12,1,6),_QosCQRunInfoMaxQueLen_Type())
qosCQRunInfoMaxQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCQRunInfoMaxQueLen.setStatus(_A)
_QosWFQTable_Object=MibTable
qosWFQTable=_QosWFQTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13))
if mibBuilder.loadTexts:qosWFQTable.setStatus(_A)
_QosWFQEntry_Object=MibTableRow
qosWFQEntry=_QosWFQEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1))
qosWFQEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:qosWFQEntry.setStatus(_A)
_QosWFQIfIndex_Type=Integer32
_QosWFQIfIndex_Object=MibTableColumn
qosWFQIfIndex=_QosWFQIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,1),_QosWFQIfIndex_Type())
qosWFQIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosWFQIfIndex.setStatus(_A)
_QosWFQIfName_Type=OctetString
_QosWFQIfName_Object=MibTableColumn
qosWFQIfName=_QosWFQIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,2),_QosWFQIfName_Type())
qosWFQIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWFQIfName.setStatus(_A)
class _QosWFQMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosWFQMaxQueLen_Type.__name__=_B
_QosWFQMaxQueLen_Object=MibTableColumn
qosWFQMaxQueLen=_QosWFQMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,3),_QosWFQMaxQueLen_Type())
qosWFQMaxQueLen.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWFQMaxQueLen.setStatus(_A)
class _QosWFQTotalQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*(('a16',16),('a32',32),('a64',64),('a128',128),('a256',256),('a512',512),('a1024',1024),('a2048',2048),('a4096',4096)))
_QosWFQTotalQueNum_Type.__name__=_B
_QosWFQTotalQueNum_Object=MibTableColumn
qosWFQTotalQueNum=_QosWFQTotalQueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,4),_QosWFQTotalQueNum_Type())
qosWFQTotalQueNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWFQTotalQueNum.setStatus(_A)
_QosWFQCurQueLen_Type=Integer32
_QosWFQCurQueLen_Object=MibTableColumn
qosWFQCurQueLen=_QosWFQCurQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,5),_QosWFQCurQueLen_Type())
qosWFQCurQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWFQCurQueLen.setStatus(_A)
_QosWFQTotalDiscard_Type=Counter32
_QosWFQTotalDiscard_Object=MibTableColumn
qosWFQTotalDiscard=_QosWFQTotalDiscard_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,6),_QosWFQTotalDiscard_Type())
qosWFQTotalDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWFQTotalDiscard.setStatus(_A)
class _QosWFQActiveQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosWFQActiveQueNum_Type.__name__=_B
_QosWFQActiveQueNum_Object=MibTableColumn
qosWFQActiveQueNum=_QosWFQActiveQueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,7),_QosWFQActiveQueNum_Type())
qosWFQActiveQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWFQActiveQueNum.setStatus(_A)
class _QosWFQMaxActiveQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QosWFQMaxActiveQueNum_Type.__name__=_B
_QosWFQMaxActiveQueNum_Object=MibTableColumn
qosWFQMaxActiveQueNum=_QosWFQMaxActiveQueNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,8),_QosWFQMaxActiveQueNum_Type())
qosWFQMaxActiveQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWFQMaxActiveQueNum.setStatus(_A)
class _QosUndoWFQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosWFQ',0),('qosNoWFQ',1)))
_QosUndoWFQ_Type.__name__=_B
_QosUndoWFQ_Object=MibTableColumn
qosUndoWFQ=_QosUndoWFQ_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,9),_QosUndoWFQ_Type())
qosUndoWFQ.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoWFQ.setStatus(_A)
class _QosWFQQueueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip-precedence',1),('dscp',2)))
_QosWFQQueueType_Type.__name__=_B
_QosWFQQueueType_Object=MibTableColumn
qosWFQQueueType=_QosWFQQueueType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,13,1,10),_QosWFQQueueType_Type())
qosWFQQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWFQQueueType.setStatus(_A)
_QosWREDTable_Object=MibTable
qosWREDTable=_QosWREDTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14))
if mibBuilder.loadTexts:qosWREDTable.setStatus(_A)
_QosWREDEntry_Object=MibTableRow
qosWREDEntry=_QosWREDEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14,1))
qosWREDEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:qosWREDEntry.setStatus(_A)
_QosWREDIfIndex_Type=Integer32
_QosWREDIfIndex_Object=MibTableColumn
qosWREDIfIndex=_QosWREDIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14,1,1),_QosWREDIfIndex_Type())
qosWREDIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosWREDIfIndex.setStatus(_A)
_QosWREDIfName_Type=OctetString
_QosWREDIfName_Object=MibTableColumn
qosWREDIfName=_QosWREDIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14,1,2),_QosWREDIfName_Type())
qosWREDIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWREDIfName.setStatus(_A)
class _QosWREDWeightConstant_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosWREDWeightConstant_Type.__name__=_B
_QosWREDWeightConstant_Object=MibTableColumn
qosWREDWeightConstant=_QosWREDWeightConstant_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14,1,3),_QosWREDWeightConstant_Type())
qosWREDWeightConstant.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWREDWeightConstant.setStatus(_A)
class _QosWREDEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_QosWREDEnable_Type.__name__=_B
_QosWREDEnable_Object=MibTableColumn
qosWREDEnable=_QosWREDEnable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14,1,4),_QosWREDEnable_Type())
qosWREDEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWREDEnable.setStatus(_A)
class _QosUndoWREDWeightConstant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosWREDExponent',0),('qosNoWREDExponent',1)))
_QosUndoWREDWeightConstant_Type.__name__=_B
_QosUndoWREDWeightConstant_Object=MibTableColumn
qosUndoWREDWeightConstant=_QosUndoWREDWeightConstant_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,14,1,5),_QosUndoWREDWeightConstant_Type())
qosUndoWREDWeightConstant.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoWREDWeightConstant.setStatus(_A)
_QosWREDPreTable_Object=MibTable
qosWREDPreTable=_QosWREDPreTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15))
if mibBuilder.loadTexts:qosWREDPreTable.setStatus(_A)
_QosWREDPreEntry_Object=MibTableRow
qosWREDPreEntry=_QosWREDPreEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1))
qosWREDPreEntry.setIndexNames((0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:qosWREDPreEntry.setStatus(_A)
_QosWREDPreIfIndex_Type=Integer32
_QosWREDPreIfIndex_Object=MibTableColumn
qosWREDPreIfIndex=_QosWREDPreIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,1),_QosWREDPreIfIndex_Type())
qosWREDPreIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosWREDPreIfIndex.setStatus(_A)
class _QosWREDPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosWREDPrecedence_Type.__name__=_B
_QosWREDPrecedence_Object=MibTableColumn
qosWREDPrecedence=_QosWREDPrecedence_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,2),_QosWREDPrecedence_Type())
qosWREDPrecedence.setMaxAccess(_F)
if mibBuilder.loadTexts:qosWREDPrecedence.setStatus(_A)
_QosWREDPreIfName_Type=OctetString
_QosWREDPreIfName_Object=MibTableColumn
qosWREDPreIfName=_QosWREDPreIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,3),_QosWREDPreIfName_Type())
qosWREDPreIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWREDPreIfName.setStatus(_A)
class _QosWREDPreLowLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosWREDPreLowLimit_Type.__name__=_B
_QosWREDPreLowLimit_Object=MibTableColumn
qosWREDPreLowLimit=_QosWREDPreLowLimit_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,4),_QosWREDPreLowLimit_Type())
qosWREDPreLowLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWREDPreLowLimit.setStatus(_A)
class _QosWREDPreHighLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosWREDPreHighLimit_Type.__name__=_B
_QosWREDPreHighLimit_Object=MibTableColumn
qosWREDPreHighLimit=_QosWREDPreHighLimit_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,5),_QosWREDPreHighLimit_Type())
qosWREDPreHighLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWREDPreHighLimit.setStatus(_A)
class _QosWREDPreDiscardProbability_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QosWREDPreDiscardProbability_Type.__name__=_B
_QosWREDPreDiscardProbability_Object=MibTableColumn
qosWREDPreDiscardProbability=_QosWREDPreDiscardProbability_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,6),_QosWREDPreDiscardProbability_Type())
qosWREDPreDiscardProbability.setMaxAccess(_D)
if mibBuilder.loadTexts:qosWREDPreDiscardProbability.setStatus(_A)
_QosWREDPreRandomDropNum_Type=Counter32
_QosWREDPreRandomDropNum_Object=MibTableColumn
qosWREDPreRandomDropNum=_QosWREDPreRandomDropNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,7),_QosWREDPreRandomDropNum_Type())
qosWREDPreRandomDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWREDPreRandomDropNum.setStatus(_A)
_QosWREDPreTailDropNum_Type=Counter32
_QosWREDPreTailDropNum_Object=MibTableColumn
qosWREDPreTailDropNum=_QosWREDPreTailDropNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,8),_QosWREDPreTailDropNum_Type())
qosWREDPreTailDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qosWREDPreTailDropNum.setStatus(_A)
class _QosUndoWREDPre_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosWREDPre',0),('qosNoWREDPre',1)))
_QosUndoWREDPre_Type.__name__=_B
_QosUndoWREDPre_Object=MibTableColumn
qosUndoWREDPre=_QosUndoWREDPre_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,15,1,9),_QosUndoWREDPre_Type())
qosUndoWREDPre.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoWREDPre.setStatus(_A)
_QosCarlTable_Object=MibTable
qosCarlTable=_QosCarlTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,16))
if mibBuilder.loadTexts:qosCarlTable.setStatus(_A)
_QosCarlEntry_Object=MibTableRow
qosCarlEntry=_QosCarlEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,16,1))
qosCarlEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:qosCarlEntry.setStatus(_A)
_QosCarlListNum_Type=Integer32
_QosCarlListNum_Object=MibTableColumn
qosCarlListNum=_QosCarlListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,16,1,1),_QosCarlListNum_Type())
qosCarlListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCarlListNum.setStatus(_A)
class _QosCarlParaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mac-address',1),('prec-mask',2),('dscp-mask',3)))
_QosCarlParaType_Type.__name__=_B
_QosCarlParaType_Object=MibTableColumn
qosCarlParaType=_QosCarlParaType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,16,1,2),_QosCarlParaType_Type())
qosCarlParaType.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarlParaType.setStatus(_A)
_QosCarlParaValue_Type=OctetString
_QosCarlParaValue_Object=MibTableColumn
qosCarlParaValue=_QosCarlParaValue_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,16,1,3),_QosCarlParaValue_Type())
qosCarlParaValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCarlParaValue.setStatus(_A)
class _QosUndoCarl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosCARL',0),('qosNoCARL',1)))
_QosUndoCarl_Type.__name__=_B
_QosUndoCarl_Object=MibTableColumn
qosUndoCarl=_QosUndoCarl_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,16,1,4),_QosUndoCarl_Type())
qosUndoCarl.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCarl.setStatus(_A)
_QosCARTable_Object=MibTable
qosCARTable=_QosCARTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17))
if mibBuilder.loadTexts:qosCARTable.setStatus(_A)
_QosCAREntry_Object=MibTableRow
qosCAREntry=_QosCAREntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1))
qosCAREntry.setIndexNames((0,_E,_v),(0,_E,_w),(0,_E,_x),(0,_E,_y),(0,_E,_z),(0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:qosCAREntry.setStatus(_A)
_QosCARIfIndex_Type=Integer32
_QosCARIfIndex_Object=MibTableColumn
qosCARIfIndex=_QosCARIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,1),_QosCARIfIndex_Type())
qosCARIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARIfIndex.setStatus(_A)
_QosCARIfName_Type=OctetString
_QosCARIfName_Object=MibTableColumn
qosCARIfName=_QosCARIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,2),_QosCARIfName_Type())
qosCARIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCARIfName.setStatus(_A)
class _QosCARPktDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_QosCARPktDirection_Type.__name__=_B
_QosCARPktDirection_Object=MibTableColumn
qosCARPktDirection=_QosCARPktDirection_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,3),_QosCARPktDirection_Type())
qosCARPktDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARPktDirection.setStatus(_A)
class _QosCARType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('carl',2),('all',3)))
_QosCARType_Type.__name__=_B
_QosCARType_Object=MibTableColumn
qosCARType=_QosCARType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,4),_QosCARType_Type())
qosCARType.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARType.setStatus(_A)
class _QosCARListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199),ValueRangeConstraint(2000,3999))
_QosCARListNum_Type.__name__=_B
_QosCARListNum_Object=MibTableColumn
qosCARListNum=_QosCARListNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,5),_QosCARListNum_Type())
qosCARListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARListNum.setStatus(_A)
_QosCARCIR_Type=Integer32
_QosCARCIR_Object=MibTableColumn
qosCARCIR=_QosCARCIR_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,6),_QosCARCIR_Type())
qosCARCIR.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARCIR.setStatus(_A)
_QosCARBurstSize_Type=Integer32
_QosCARBurstSize_Object=MibTableColumn
qosCARBurstSize=_QosCARBurstSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,7),_QosCARBurstSize_Type())
qosCARBurstSize.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARBurstSize.setStatus(_A)
_QosCARExcessBurstSize_Type=Integer32
_QosCARExcessBurstSize_Object=MibTableColumn
qosCARExcessBurstSize=_QosCARExcessBurstSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,8),_QosCARExcessBurstSize_Type())
qosCARExcessBurstSize.setMaxAccess(_F)
if mibBuilder.loadTexts:qosCARExcessBurstSize.setStatus(_A)
class _QosCARConformAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('continue',1),('discard',2),(_A2,3),(_A3,4),('pass',5),(_A4,6),(_A5,7)))
_QosCARConformAction_Type.__name__=_B
_QosCARConformAction_Object=MibTableColumn
qosCARConformAction=_QosCARConformAction_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,9),_QosCARConformAction_Type())
qosCARConformAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCARConformAction.setStatus(_A)
class _QosCARExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('continue',1),('discard',2),(_A2,3),(_A3,4),('pass',5),(_A4,6),(_A5,7)))
_QosCARExceedAction_Type.__name__=_B
_QosCARExceedAction_Object=MibTableColumn
qosCARExceedAction=_QosCARExceedAction_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,10),_QosCARExceedAction_Type())
qosCARExceedAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCARExceedAction.setStatus(_A)
class _QosCARConformNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosCARConformNewPrec_Type.__name__=_B
_QosCARConformNewPrec_Object=MibTableColumn
qosCARConformNewPrec=_QosCARConformNewPrec_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,11),_QosCARConformNewPrec_Type())
qosCARConformNewPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCARConformNewPrec.setStatus(_A)
class _QosCARExceedNewPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosCARExceedNewPrec_Type.__name__=_B
_QosCARExceedNewPrec_Object=MibTableColumn
qosCARExceedNewPrec=_QosCARExceedNewPrec_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,12),_QosCARExceedNewPrec_Type())
qosCARExceedNewPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:qosCARExceedNewPrec.setStatus(_A)
_QosCARConformPkt_Type=Counter32
_QosCARConformPkt_Object=MibTableColumn
qosCARConformPkt=_QosCARConformPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,13),_QosCARConformPkt_Type())
qosCARConformPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCARConformPkt.setStatus(_A)
_QosCARConformByte_Type=Counter32
_QosCARConformByte_Object=MibTableColumn
qosCARConformByte=_QosCARConformByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,14),_QosCARConformByte_Type())
qosCARConformByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCARConformByte.setStatus(_A)
_QosCARExceedPkt_Type=Counter32
_QosCARExceedPkt_Object=MibTableColumn
qosCARExceedPkt=_QosCARExceedPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,15),_QosCARExceedPkt_Type())
qosCARExceedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCARExceedPkt.setStatus(_A)
_QosCARExceedByte_Type=Counter32
_QosCARExceedByte_Object=MibTableColumn
qosCARExceedByte=_QosCARExceedByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,16),_QosCARExceedByte_Type())
qosCARExceedByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCARExceedByte.setStatus(_A)
class _QosUndoCAR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosCAR',0),('qosNoCAR',1)))
_QosUndoCAR_Type.__name__=_B
_QosUndoCAR_Object=MibTableColumn
qosUndoCAR=_QosUndoCAR_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,17,1,17),_QosUndoCAR_Type())
qosUndoCAR.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoCAR.setStatus(_A)
_QosGTSTable_Object=MibTable
qosGTSTable=_QosGTSTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18))
if mibBuilder.loadTexts:qosGTSTable.setStatus(_A)
_QosGTSEntry_Object=MibTableRow
qosGTSEntry=_QosGTSEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1))
qosGTSEntry.setIndexNames((0,_E,_A6),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:qosGTSEntry.setStatus(_A)
_QosGTSIfIndex_Type=Integer32
_QosGTSIfIndex_Object=MibTableColumn
qosGTSIfIndex=_QosGTSIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,1),_QosGTSIfIndex_Type())
qosGTSIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosGTSIfIndex.setStatus(_A)
_QosGTSIfName_Type=OctetString
_QosGTSIfName_Object=MibTableColumn
qosGTSIfName=_QosGTSIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,2),_QosGTSIfName_Type())
qosGTSIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSIfName.setStatus(_A)
class _QosGTSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('all',2)))
_QosGTSType_Type.__name__=_B
_QosGTSType_Object=MibTableColumn
qosGTSType=_QosGTSType_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,3),_QosGTSType_Type())
qosGTSType.setMaxAccess(_F)
if mibBuilder.loadTexts:qosGTSType.setStatus(_A)
class _QosGTSACLNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_QosGTSACLNum_Type.__name__=_B
_QosGTSACLNum_Object=MibTableColumn
qosGTSACLNum=_QosGTSACLNum_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,4),_QosGTSACLNum_Type())
qosGTSACLNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSACLNum.setStatus(_A)
_QosGTSCIR_Type=Integer32
_QosGTSCIR_Object=MibTableColumn
qosGTSCIR=_QosGTSCIR_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,5),_QosGTSCIR_Type())
qosGTSCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:qosGTSCIR.setStatus(_A)
_QosGTSBurstSize_Type=Integer32
_QosGTSBurstSize_Object=MibTableColumn
qosGTSBurstSize=_QosGTSBurstSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,6),_QosGTSBurstSize_Type())
qosGTSBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:qosGTSBurstSize.setStatus(_A)
_QosGTSExcessBurstSize_Type=Integer32
_QosGTSExcessBurstSize_Object=MibTableColumn
qosGTSExcessBurstSize=_QosGTSExcessBurstSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,7),_QosGTSExcessBurstSize_Type())
qosGTSExcessBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:qosGTSExcessBurstSize.setStatus(_A)
class _QosGTSMaxQueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosGTSMaxQueLen_Type.__name__=_B
_QosGTSMaxQueLen_Object=MibTableColumn
qosGTSMaxQueLen=_QosGTSMaxQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,8),_QosGTSMaxQueLen_Type())
qosGTSMaxQueLen.setMaxAccess(_D)
if mibBuilder.loadTexts:qosGTSMaxQueLen.setStatus(_A)
_QosGTSCurQueLen_Type=Integer32
_QosGTSCurQueLen_Object=MibTableColumn
qosGTSCurQueLen=_QosGTSCurQueLen_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,9),_QosGTSCurQueLen_Type())
qosGTSCurQueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSCurQueLen.setStatus(_A)
_QosGTSPassPkt_Type=Counter32
_QosGTSPassPkt_Object=MibTableColumn
qosGTSPassPkt=_QosGTSPassPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,10),_QosGTSPassPkt_Type())
qosGTSPassPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSPassPkt.setStatus(_A)
_QosGTSPassByte_Type=Counter32
_QosGTSPassByte_Object=MibTableColumn
qosGTSPassByte=_QosGTSPassByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,11),_QosGTSPassByte_Type())
qosGTSPassByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSPassByte.setStatus(_A)
_QosGTSDelayPkt_Type=Counter32
_QosGTSDelayPkt_Object=MibTableColumn
qosGTSDelayPkt=_QosGTSDelayPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,12),_QosGTSDelayPkt_Type())
qosGTSDelayPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSDelayPkt.setStatus(_A)
_QosGTSDelayByte_Type=Counter32
_QosGTSDelayByte_Object=MibTableColumn
qosGTSDelayByte=_QosGTSDelayByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,13),_QosGTSDelayByte_Type())
qosGTSDelayByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSDelayByte.setStatus(_A)
_QosGTSDiscardPkt_Type=Counter32
_QosGTSDiscardPkt_Object=MibTableColumn
qosGTSDiscardPkt=_QosGTSDiscardPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,14),_QosGTSDiscardPkt_Type())
qosGTSDiscardPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSDiscardPkt.setStatus(_A)
_QosGTSDiscardByte_Type=Counter32
_QosGTSDiscardByte_Object=MibTableColumn
qosGTSDiscardByte=_QosGTSDiscardByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,15),_QosGTSDiscardByte_Type())
qosGTSDiscardByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGTSDiscardByte.setStatus(_A)
class _QosUndoGTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosGTS',0),('qosNoGTS',1)))
_QosUndoGTS_Type.__name__=_B
_QosUndoGTS_Object=MibTableColumn
qosUndoGTS=_QosUndoGTS_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,18,1,16),_QosUndoGTS_Type())
qosUndoGTS.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoGTS.setStatus(_A)
_QosLRTable_Object=MibTable
qosLRTable=_QosLRTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19))
if mibBuilder.loadTexts:qosLRTable.setStatus(_A)
_QosLREntry_Object=MibTableRow
qosLREntry=_QosLREntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1))
qosLREntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:qosLREntry.setStatus(_A)
_QosLRIfIndex_Type=Integer32
_QosLRIfIndex_Object=MibTableColumn
qosLRIfIndex=_QosLRIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,1),_QosLRIfIndex_Type())
qosLRIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosLRIfIndex.setStatus(_A)
_QosLRIfName_Type=OctetString
_QosLRIfName_Object=MibTableColumn
qosLRIfName=_QosLRIfName_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,2),_QosLRIfName_Type())
qosLRIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosLRIfName.setStatus(_A)
_QosLRCIR_Type=Integer32
_QosLRCIR_Object=MibTableColumn
qosLRCIR=_QosLRCIR_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,3),_QosLRCIR_Type())
qosLRCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:qosLRCIR.setStatus(_A)
_QosLRBurstSize_Type=Integer32
_QosLRBurstSize_Object=MibTableColumn
qosLRBurstSize=_QosLRBurstSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,4),_QosLRBurstSize_Type())
qosLRBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:qosLRBurstSize.setStatus(_A)
_QosLRExcessBurstSize_Type=Integer32
_QosLRExcessBurstSize_Object=MibTableColumn
qosLRExcessBurstSize=_QosLRExcessBurstSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,5),_QosLRExcessBurstSize_Type())
qosLRExcessBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:qosLRExcessBurstSize.setStatus(_A)
_QosLRPassPkt_Type=Counter32
_QosLRPassPkt_Object=MibTableColumn
qosLRPassPkt=_QosLRPassPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,6),_QosLRPassPkt_Type())
qosLRPassPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosLRPassPkt.setStatus(_A)
_QosLRPassByte_Type=Counter32
_QosLRPassByte_Object=MibTableColumn
qosLRPassByte=_QosLRPassByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,7),_QosLRPassByte_Type())
qosLRPassByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosLRPassByte.setStatus(_A)
_QosLRDelayPkt_Type=Counter32
_QosLRDelayPkt_Object=MibTableColumn
qosLRDelayPkt=_QosLRDelayPkt_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,8),_QosLRDelayPkt_Type())
qosLRDelayPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:qosLRDelayPkt.setStatus(_A)
_QosLRDelayByte_Type=Counter32
_QosLRDelayByte_Object=MibTableColumn
qosLRDelayByte=_QosLRDelayByte_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,9),_QosLRDelayByte_Type())
qosLRDelayByte.setMaxAccess(_C)
if mibBuilder.loadTexts:qosLRDelayByte.setStatus(_A)
class _QosUndoLR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('qosLR',0),('qosNoLR',1)))
_QosUndoLR_Type.__name__=_B
_QosUndoLR_Object=MibTableColumn
qosUndoLR=_QosUndoLR_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,19,1,10),_QosUndoLR_Type())
qosUndoLR.setMaxAccess(_D)
if mibBuilder.loadTexts:qosUndoLR.setStatus(_A)
_QosIfBandwidthTable_Object=MibTable
qosIfBandwidthTable=_QosIfBandwidthTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20))
if mibBuilder.loadTexts:qosIfBandwidthTable.setStatus(_A)
_QosIfBandwidthEntry_Object=MibTableRow
qosIfBandwidthEntry=_QosIfBandwidthEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1))
qosIfBandwidthEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:qosIfBandwidthEntry.setStatus(_A)
_QosIfBandwidthIfIndex_Type=Integer32
_QosIfBandwidthIfIndex_Object=MibTableColumn
qosIfBandwidthIfIndex=_QosIfBandwidthIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1,1),_QosIfBandwidthIfIndex_Type())
qosIfBandwidthIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosIfBandwidthIfIndex.setStatus(_A)
class _QosIFBandwidthMaxBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_QosIFBandwidthMaxBW_Type.__name__=_B
_QosIFBandwidthMaxBW_Object=MibTableColumn
qosIFBandwidthMaxBW=_QosIFBandwidthMaxBW_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1,2),_QosIFBandwidthMaxBW_Type())
qosIFBandwidthMaxBW.setMaxAccess(_G)
if mibBuilder.loadTexts:qosIFBandwidthMaxBW.setStatus(_A)
class _QosIFBandwidthMaxReservedBWPct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QosIFBandwidthMaxReservedBWPct_Type.__name__=_B
_QosIFBandwidthMaxReservedBWPct_Object=MibTableColumn
qosIFBandwidthMaxReservedBWPct=_QosIFBandwidthMaxReservedBWPct_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1,3),_QosIFBandwidthMaxReservedBWPct_Type())
qosIFBandwidthMaxReservedBWPct.setMaxAccess(_G)
if mibBuilder.loadTexts:qosIFBandwidthMaxReservedBWPct.setStatus(_A)
_QosIFBandwidthMaxReservedBW_Type=Integer32
_QosIFBandwidthMaxReservedBW_Object=MibTableColumn
qosIFBandwidthMaxReservedBW=_QosIFBandwidthMaxReservedBW_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1,4),_QosIFBandwidthMaxReservedBW_Type())
qosIFBandwidthMaxReservedBW.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIFBandwidthMaxReservedBW.setStatus(_A)
_QosIFBandwidthAvailable_Type=Integer32
_QosIFBandwidthAvailable_Object=MibTableColumn
qosIFBandwidthAvailable=_QosIFBandwidthAvailable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1,5),_QosIFBandwidthAvailable_Type())
qosIFBandwidthAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIFBandwidthAvailable.setStatus(_A)
_QosIFBandwidthRowStatus_Type=RowStatus
_QosIFBandwidthRowStatus_Object=MibTableColumn
qosIFBandwidthRowStatus=_QosIFBandwidthRowStatus_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,20,1,6),_QosIFBandwidthRowStatus_Type())
qosIFBandwidthRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosIFBandwidthRowStatus.setStatus(_A)
_QosRTPIfApplyTable_Object=MibTable
qosRTPIfApplyTable=_QosRTPIfApplyTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21))
if mibBuilder.loadTexts:qosRTPIfApplyTable.setStatus(_A)
_QosRTPIfApplyEntry_Object=MibTableRow
qosRTPIfApplyEntry=_QosRTPIfApplyEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1))
qosRTPIfApplyEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:qosRTPIfApplyEntry.setStatus(_A)
_QosRTPIfApplyIfIndex_Type=Integer32
_QosRTPIfApplyIfIndex_Object=MibTableColumn
qosRTPIfApplyIfIndex=_QosRTPIfApplyIfIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1,1),_QosRTPIfApplyIfIndex_Type())
qosRTPIfApplyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosRTPIfApplyIfIndex.setStatus(_A)
class _QosRTPIfApplyStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_QosRTPIfApplyStartPort_Type.__name__=_B
_QosRTPIfApplyStartPort_Object=MibTableColumn
qosRTPIfApplyStartPort=_QosRTPIfApplyStartPort_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1,2),_QosRTPIfApplyStartPort_Type())
qosRTPIfApplyStartPort.setMaxAccess(_G)
if mibBuilder.loadTexts:qosRTPIfApplyStartPort.setStatus(_A)
class _QosRTPIfApplyEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_QosRTPIfApplyEndPort_Type.__name__=_B
_QosRTPIfApplyEndPort_Object=MibTableColumn
qosRTPIfApplyEndPort=_QosRTPIfApplyEndPort_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1,3),_QosRTPIfApplyEndPort_Type())
qosRTPIfApplyEndPort.setMaxAccess(_G)
if mibBuilder.loadTexts:qosRTPIfApplyEndPort.setStatus(_A)
class _QosRTPIfApplyBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,1000000))
_QosRTPIfApplyBandWidth_Type.__name__=_B
_QosRTPIfApplyBandWidth_Object=MibTableColumn
qosRTPIfApplyBandWidth=_QosRTPIfApplyBandWidth_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1,4),_QosRTPIfApplyBandWidth_Type())
qosRTPIfApplyBandWidth.setMaxAccess(_G)
if mibBuilder.loadTexts:qosRTPIfApplyBandWidth.setStatus(_A)
_QosRTPIfApplyCbs_Type=Integer32
_QosRTPIfApplyCbs_Object=MibTableColumn
qosRTPIfApplyCbs=_QosRTPIfApplyCbs_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1,5),_QosRTPIfApplyCbs_Type())
qosRTPIfApplyCbs.setMaxAccess(_G)
if mibBuilder.loadTexts:qosRTPIfApplyCbs.setStatus(_A)
_QosRTPIfApplyRowStatus_Type=RowStatus
_QosRTPIfApplyRowStatus_Object=MibTableColumn
qosRTPIfApplyRowStatus=_QosRTPIfApplyRowStatus_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,21,1,6),_QosRTPIfApplyRowStatus_Type())
qosRTPIfApplyRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qosRTPIfApplyRowStatus.setStatus(_A)
_QosRTPIfQueueRunInfoTable_Object=MibTable
qosRTPIfQueueRunInfoTable=_QosRTPIfQueueRunInfoTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,22))
if mibBuilder.loadTexts:qosRTPIfQueueRunInfoTable.setStatus(_A)
_QosRTPIfQueueRunInfoEntry_Object=MibTableRow
qosRTPIfQueueRunInfoEntry=_QosRTPIfQueueRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,22,1))
qosRTPIfQueueRunInfoEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:qosRTPIfQueueRunInfoEntry.setStatus(_A)
_QosRTPIfQueueSize_Type=Counter32
_QosRTPIfQueueSize_Object=MibTableColumn
qosRTPIfQueueSize=_QosRTPIfQueueSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,22,1,1),_QosRTPIfQueueSize_Type())
qosRTPIfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRTPIfQueueSize.setStatus(_A)
_QosRTPIfQueueMaxSize_Type=Counter32
_QosRTPIfQueueMaxSize_Object=MibTableColumn
qosRTPIfQueueMaxSize=_QosRTPIfQueueMaxSize_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,22,1,2),_QosRTPIfQueueMaxSize_Type())
qosRTPIfQueueMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRTPIfQueueMaxSize.setStatus(_A)
_QosRTPIfQueueOutputs_Type=Counter32
_QosRTPIfQueueOutputs_Object=MibTableColumn
qosRTPIfQueueOutputs=_QosRTPIfQueueOutputs_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,22,1,3),_QosRTPIfQueueOutputs_Type())
qosRTPIfQueueOutputs.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRTPIfQueueOutputs.setStatus(_A)
_QosRTPIfQueueDiscards_Type=Counter32
_QosRTPIfQueueDiscards_Object=MibTableColumn
qosRTPIfQueueDiscards=_QosRTPIfQueueDiscards_Object((1,3,6,1,4,1,43,45,1,1,3,3,2,22,1,4),_QosRTPIfQueueDiscards_Type())
qosRTPIfQueueDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRTPIfQueueDiscards.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hwIfQoSMib':hwIfQoSMib,'qosFIFOTable':qosFIFOTable,'qosFIFOEntry':qosFIFOEntry,_N:qosFIFOIfIndex,'qosFIFOIfName':qosFIFOIfName,'qosFIFOMaxQueueLen':qosFIFOMaxQueueLen,'qosFIFOCurQueueLen':qosFIFOCurQueueLen,'qosFIFODiscardPkt':qosFIFODiscardPkt,'qosUndoFIFO':qosUndoFIFO,'qosPqlDefaultTable':qosPqlDefaultTable,'qosPqlDefaultEntry':qosPqlDefaultEntry,_O:qosPqlDefaultListNum,'qosPqlDefaultQueueType':qosPqlDefaultQueueType,'qosUndoPqlDefault':qosUndoPqlDefault,'qosPqlQueueLenTable':qosPqlQueueLenTable,'qosPqlQueueLenEntry':qosPqlQueueLenEntry,_P:qosPqlQueLenListNum,_Q:qosPqlQueLenQueueType,'qosPqlQueLenValue':qosPqlQueLenValue,'qosUndoPqlQueLen':qosUndoPqlQueLen,'qosPqlIfTable':qosPqlIfTable,'qosPqlIfEntry':qosPqlIfEntry,_R:qosPqlIfListNum,_S:qosPqlIfIndex,'qosPqlIfName':qosPqlIfName,'qosPqlIfQueueType':qosPqlIfQueueType,'qosUndoPqlIf':qosUndoPqlIf,'qosPqlProtocolTable':qosPqlProtocolTable,'qosPqlProtocolEntry':qosPqlProtocolEntry,_T:qosPqlProListNum,_U:qosPqlProName,_V:qosPqlProQueKey,_W:qosPqlProQueKeyValue,'qosPqlProQueType':qosPqlProQueType,'qosUndoPqlProtocol':qosUndoPqlProtocol,'qosPQTable':qosPQTable,'qosPQEntry':qosPQEntry,_b:qosPQIfIndex,'qosPQListNum':qosPQListNum,'qosPQIfName':qosPQIfName,'qosPQTopPkt':qosPQTopPkt,'qosPQTopDiscard':qosPQTopDiscard,'qosPQTopMaxQueLen':qosPQTopMaxQueLen,'qosPQMiddlePkt':qosPQMiddlePkt,'qosPQMiddleDiscard':qosPQMiddleDiscard,'qosPQMiddleMaxQueLen':qosPQMiddleMaxQueLen,'qosPQNormalPkt':qosPQNormalPkt,'qosPQNormalDiscard':qosPQNormalDiscard,'qosPQNormalMaxQueLen':qosPQNormalMaxQueLen,'qosPQBottomPkt':qosPQBottomPkt,'qosPQBottomDiscard':qosPQBottomDiscard,'qosPQBottomMaxQueLen':qosPQBottomMaxQueLen,'qosUndoPQ':qosUndoPQ,'qosCqlDefaultTable':qosCqlDefaultTable,'qosCqlDefaultEntry':qosCqlDefaultEntry,_c:qosCqlListNum,'qosCqlQueueNum':qosCqlQueueNum,'qosUndoCqlDefault':qosUndoCqlDefault,'qosCqlIfTable':qosCqlIfTable,'qosCqlIfEntry':qosCqlIfEntry,_d:qosCqlIfListNum,_e:qosCqlIfIndex,'qosCqlIfName':qosCqlIfName,'qosCqlIfQueueNum':qosCqlIfQueueNum,'qosUndoCqlIf':qosUndoCqlIf,'qosCqlProtocolTable':qosCqlProtocolTable,'qosCqlProtocolEntry':qosCqlProtocolEntry,_f:qosCqlProListNum,_g:qosCqlProName,_h:qosCqlProQueKey,_i:qosCqlProQueKeyValue,'qosCqlProQueNum':qosCqlProQueNum,'qosUndoCqlProtocol':qosUndoCqlProtocol,'qosCqlQueParaTable':qosCqlQueParaTable,'qosCqlQueParaEntry':qosCqlQueParaEntry,_j:qosCqlQueParaListNum,_k:qosCqlQueParaQueNum,_l:qosCqlQueParaServing,_m:qosCqlQueParaMaxQueLen,'qosUndoCqlQueParaServing':qosUndoCqlQueParaServing,'qosUndoCqlQueParaMaxQueLen':qosUndoCqlQueParaMaxQueLen,'qosCQTable':qosCQTable,'qosCQEntry':qosCQEntry,_n:qosCQIfIndex,'qosCQListNum':qosCQListNum,'qosCQIfName':qosCQIfName,'qosUndoCQ':qosUndoCQ,'qosCQRunInfoTable':qosCQRunInfoTable,'qosCQRunInfoEntry':qosCQRunInfoEntry,_o:qosCQRunInfoIfIndex,_p:qosCQRunInfoQueNum,'qosCQRunInfoIfName':qosCQRunInfoIfName,'qosCQRunInfoQuePkt':qosCQRunInfoQuePkt,'qosCQRunInfoQueDiscard':qosCQRunInfoQueDiscard,'qosCQRunInfoMaxQueLen':qosCQRunInfoMaxQueLen,'qosWFQTable':qosWFQTable,'qosWFQEntry':qosWFQEntry,_q:qosWFQIfIndex,'qosWFQIfName':qosWFQIfName,'qosWFQMaxQueLen':qosWFQMaxQueLen,'qosWFQTotalQueNum':qosWFQTotalQueNum,'qosWFQCurQueLen':qosWFQCurQueLen,'qosWFQTotalDiscard':qosWFQTotalDiscard,'qosWFQActiveQueNum':qosWFQActiveQueNum,'qosWFQMaxActiveQueNum':qosWFQMaxActiveQueNum,'qosUndoWFQ':qosUndoWFQ,'qosWFQQueueType':qosWFQQueueType,'qosWREDTable':qosWREDTable,'qosWREDEntry':qosWREDEntry,_r:qosWREDIfIndex,'qosWREDIfName':qosWREDIfName,'qosWREDWeightConstant':qosWREDWeightConstant,'qosWREDEnable':qosWREDEnable,'qosUndoWREDWeightConstant':qosUndoWREDWeightConstant,'qosWREDPreTable':qosWREDPreTable,'qosWREDPreEntry':qosWREDPreEntry,_s:qosWREDPreIfIndex,_t:qosWREDPrecedence,'qosWREDPreIfName':qosWREDPreIfName,'qosWREDPreLowLimit':qosWREDPreLowLimit,'qosWREDPreHighLimit':qosWREDPreHighLimit,'qosWREDPreDiscardProbability':qosWREDPreDiscardProbability,'qosWREDPreRandomDropNum':qosWREDPreRandomDropNum,'qosWREDPreTailDropNum':qosWREDPreTailDropNum,'qosUndoWREDPre':qosUndoWREDPre,'qosCarlTable':qosCarlTable,'qosCarlEntry':qosCarlEntry,_u:qosCarlListNum,'qosCarlParaType':qosCarlParaType,'qosCarlParaValue':qosCarlParaValue,'qosUndoCarl':qosUndoCarl,'qosCARTable':qosCARTable,'qosCAREntry':qosCAREntry,_v:qosCARIfIndex,'qosCARIfName':qosCARIfName,_w:qosCARPktDirection,_x:qosCARType,_y:qosCARListNum,_z:qosCARCIR,_A0:qosCARBurstSize,_A1:qosCARExcessBurstSize,'qosCARConformAction':qosCARConformAction,'qosCARExceedAction':qosCARExceedAction,'qosCARConformNewPrec':qosCARConformNewPrec,'qosCARExceedNewPrec':qosCARExceedNewPrec,'qosCARConformPkt':qosCARConformPkt,'qosCARConformByte':qosCARConformByte,'qosCARExceedPkt':qosCARExceedPkt,'qosCARExceedByte':qosCARExceedByte,'qosUndoCAR':qosUndoCAR,'qosGTSTable':qosGTSTable,'qosGTSEntry':qosGTSEntry,_A6:qosGTSIfIndex,'qosGTSIfName':qosGTSIfName,_A7:qosGTSType,_A8:qosGTSACLNum,'qosGTSCIR':qosGTSCIR,'qosGTSBurstSize':qosGTSBurstSize,'qosGTSExcessBurstSize':qosGTSExcessBurstSize,'qosGTSMaxQueLen':qosGTSMaxQueLen,'qosGTSCurQueLen':qosGTSCurQueLen,'qosGTSPassPkt':qosGTSPassPkt,'qosGTSPassByte':qosGTSPassByte,'qosGTSDelayPkt':qosGTSDelayPkt,'qosGTSDelayByte':qosGTSDelayByte,'qosGTSDiscardPkt':qosGTSDiscardPkt,'qosGTSDiscardByte':qosGTSDiscardByte,'qosUndoGTS':qosUndoGTS,'qosLRTable':qosLRTable,'qosLREntry':qosLREntry,_A9:qosLRIfIndex,'qosLRIfName':qosLRIfName,'qosLRCIR':qosLRCIR,'qosLRBurstSize':qosLRBurstSize,'qosLRExcessBurstSize':qosLRExcessBurstSize,'qosLRPassPkt':qosLRPassPkt,'qosLRPassByte':qosLRPassByte,'qosLRDelayPkt':qosLRDelayPkt,'qosLRDelayByte':qosLRDelayByte,'qosUndoLR':qosUndoLR,'qosIfBandwidthTable':qosIfBandwidthTable,'qosIfBandwidthEntry':qosIfBandwidthEntry,_AA:qosIfBandwidthIfIndex,'qosIFBandwidthMaxBW':qosIFBandwidthMaxBW,'qosIFBandwidthMaxReservedBWPct':qosIFBandwidthMaxReservedBWPct,'qosIFBandwidthMaxReservedBW':qosIFBandwidthMaxReservedBW,'qosIFBandwidthAvailable':qosIFBandwidthAvailable,'qosIFBandwidthRowStatus':qosIFBandwidthRowStatus,'qosRTPIfApplyTable':qosRTPIfApplyTable,'qosRTPIfApplyEntry':qosRTPIfApplyEntry,_M:qosRTPIfApplyIfIndex,'qosRTPIfApplyStartPort':qosRTPIfApplyStartPort,'qosRTPIfApplyEndPort':qosRTPIfApplyEndPort,'qosRTPIfApplyBandWidth':qosRTPIfApplyBandWidth,'qosRTPIfApplyCbs':qosRTPIfApplyCbs,'qosRTPIfApplyRowStatus':qosRTPIfApplyRowStatus,'qosRTPIfQueueRunInfoTable':qosRTPIfQueueRunInfoTable,'qosRTPIfQueueRunInfoEntry':qosRTPIfQueueRunInfoEntry,'qosRTPIfQueueSize':qosRTPIfQueueSize,'qosRTPIfQueueMaxSize':qosRTPIfQueueMaxSize,'qosRTPIfQueueOutputs':qosRTPIfQueueOutputs,'qosRTPIfQueueDiscards':qosRTPIfQueueDiscards})