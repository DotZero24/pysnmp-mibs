_AX='mplsMpCvTrCntrBadSeqRepsRcvd'
_AW='mplsMpCvTrCntrTmoRepsRcvd'
_AV='mplsMpCvTrCntrIllRepsRcvd'
_AU='mplsMpCvTrCntrBadRepsRcvd'
_AT='mplsMpCvTrCntrIllRepsSent'
_AS='mplsMpCvTrCntrBadRepsSent'
_AR='mplsMpCvTrCntrOKRepsRcvd'
_AQ='mplsMpCvTrCntrOKRepsSent'
_AP='mplsMpCvTrCntrTotalRepsRcvd'
_AO='mplsMpCvTrCntrTotalRepsSent'
_AN='mplsMpCvTrCntrReqsRcvd'
_AM='mplsMpCvTrCntrReqsSent'
_AL='mplsMpCvTrCntrLastRcvdRetCode'
_AK='mplsMpCvTrCntrNextSeqToSend'
_AJ='mplsCvTrSysCounterBadSeqRepsRcvd'
_AI='mplsCvTrSysCounterTmoRepsRcvd'
_AH='mplsCvTrSysCounterIllRepsRcvd'
_AG='mplsCvTrSysCounterBadRepsRcvd'
_AF='mplsCvTrSysCounterIllRepsSent'
_AE='mplsCvTrSysCounterBadRepsSent'
_AD='mplsCvTrSysCounterOKRepsRcvd'
_AC='mplsCvTrSysCounterOKRepsSent'
_AB='mplsCvTrSysCounterTotalRepsRcvd'
_AA='mplsCvTrSysCounterTotalRepsSent'
_A9='mplsCvTrSysCounterReqsRcvd'
_A8='mplsCvTrSysCounterReqsSent'
_A7='mplsTrHopMpDownstreamIfIndex'
_A6='mplsTrHopMpDownstreamIfAddr'
_A5='mplsTrHopMpDownstreamIfAddrType'
_A4='mplsTrHopMpMtu'
_A3='mplsTrHopMpRoundTrip'
_A2='mplsTrHopMpLabel'
_A1='mplsTrHopMpNextHopAddress'
_A0='mplsTrHopMpNextHopAddressType'
_z='mplsTrHopMpReturnCode'
_y='mplsCvTrMpTrReturnCode'
_x='mplsCvTrMpTimeout'
_w='mplsCvTrMpTrStatus'
_v='mplsCvTrMpCvRoundTripMax'
_u='mplsCvTrMpCvRoundTripAve'
_t='mplsCvTrMpCvRoundTripMin'
_s='mplsCvTrMpCvRepliesRcvd'
_r='mplsCvTrMpCvRvsReturnCode'
_q='mplsCvTrMpCvReturnCode'
_p='mplsCvTrMpCvTtl'
_o='mplsCvTrMpCvVerifyReverse'
_n='mplsCvTrMpCvInterval'
_m='mplsCvTrMpCvMessages'
_l='mplsCvTrMpCvStatus'
_k='mplsCvTrMpPhb'
_j='mplsCvTrMpRowStatus'
_i='mplsTrHopNumber'
_h='not-accessible'
_g='Counter32'
_f='mplsMpIndex'
_e='DC-OAM-MPLS-MP-MIB'
_d='lsppGeneralGroup'
_c='mplsCvTrMpIndex'
_b='TruthValue'
_a='ttlLimitReached'
_Z='badReplyReceived'
_Y='resourceFailure'
_X='requestNotSent'
_W='timeout'
_V='singleLabel'
_U='unknownFec'
_T='noLabel'
_S='wrongLabel'
_R='noForwarding'
_Q='labelSwitch'
_P='interfaceUnknown'
_O='mappingMismatch'
_N='noMapping'
_M='egress'
_L='unrecognizedTlv'
_K='badRequestSent'
_J='noRC'
_I='oammEntApplIndex'
_H='DC-OAMM-MIB'
_G='milliseconds'
_F='Integer32'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='DC-OAM-LSP-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NumericIndex,=mibBuilder.importSymbols('DC-MASTER-TC','NumericIndex')
mplsMpEntry,mplsMpIndex=mibBuilder.importSymbols(_e,'mplsMpEntry',_f)
oammEntApplIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
MplsLabel,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLabel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_g,'Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_b)
lspPingMib=ModuleIdentity((1,3,6,1,4,1,629,10,12))
if mibBuilder.loadTexts:lspPingMib.setRevisions(('2014-12-21 00:00',))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Opx_ObjectIdentity=ObjectIdentity
opx=_Opx_ObjectIdentity((1,3,6,1,4,1,629,10))
_LsppObjects_ObjectIdentity=ObjectIdentity
lsppObjects=_LsppObjects_ObjectIdentity((1,3,6,1,4,1,629,10,12,1))
_MplsCvTrMpTable_Object=MibTable
mplsCvTrMpTable=_MplsCvTrMpTable_Object((1,3,6,1,4,1,629,10,12,1,1))
if mibBuilder.loadTexts:mplsCvTrMpTable.setStatus(_A)
_MplsCvTrMpEntry_Object=MibTableRow
mplsCvTrMpEntry=_MplsCvTrMpEntry_Object((1,3,6,1,4,1,629,10,12,1,1,1))
mplsCvTrMpEntry.setIndexNames((0,_H,_I),(0,_B,_c))
if mibBuilder.loadTexts:mplsCvTrMpEntry.setStatus(_A)
_MplsCvTrMpIndex_Type=NumericIndex
_MplsCvTrMpIndex_Object=MibTableColumn
mplsCvTrMpIndex=_MplsCvTrMpIndex_Object((1,3,6,1,4,1,629,10,12,1,1,1,1),_MplsCvTrMpIndex_Type())
mplsCvTrMpIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:mplsCvTrMpIndex.setStatus(_A)
_MplsCvTrMpRowStatus_Type=RowStatus
_MplsCvTrMpRowStatus_Object=MibTableColumn
mplsCvTrMpRowStatus=_MplsCvTrMpRowStatus_Object((1,3,6,1,4,1,629,10,12,1,1,1,2),_MplsCvTrMpRowStatus_Type())
mplsCvTrMpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpRowStatus.setStatus(_A)
class _MplsCvTrMpPhb_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsCvTrMpPhb_Type.__name__=_F
_MplsCvTrMpPhb_Object=MibTableColumn
mplsCvTrMpPhb=_MplsCvTrMpPhb_Object((1,3,6,1,4,1,629,10,12,1,1,1,3),_MplsCvTrMpPhb_Type())
mplsCvTrMpPhb.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpPhb.setStatus(_A)
class _MplsCvTrMpCvStatus_Type(TruthValue):defaultValue=2
_MplsCvTrMpCvStatus_Type.__name__=_b
_MplsCvTrMpCvStatus_Object=MibTableColumn
mplsCvTrMpCvStatus=_MplsCvTrMpCvStatus_Object((1,3,6,1,4,1,629,10,12,1,1,1,4),_MplsCvTrMpCvStatus_Type())
mplsCvTrMpCvStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpCvStatus.setStatus(_A)
class _MplsCvTrMpCvMessages_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_MplsCvTrMpCvMessages_Type.__name__=_D
_MplsCvTrMpCvMessages_Object=MibTableColumn
mplsCvTrMpCvMessages=_MplsCvTrMpCvMessages_Object((1,3,6,1,4,1,629,10,12,1,1,1,5),_MplsCvTrMpCvMessages_Type())
mplsCvTrMpCvMessages.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpCvMessages.setStatus(_A)
class _MplsCvTrMpCvInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_MplsCvTrMpCvInterval_Type.__name__=_D
_MplsCvTrMpCvInterval_Object=MibTableColumn
mplsCvTrMpCvInterval=_MplsCvTrMpCvInterval_Object((1,3,6,1,4,1,629,10,12,1,1,1,6),_MplsCvTrMpCvInterval_Type())
mplsCvTrMpCvInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpCvInterval.setStatus(_A)
if mibBuilder.loadTexts:mplsCvTrMpCvInterval.setUnits(_G)
class _MplsCvTrMpCvVerifyReverse_Type(TruthValue):defaultValue=2
_MplsCvTrMpCvVerifyReverse_Type.__name__=_b
_MplsCvTrMpCvVerifyReverse_Object=MibTableColumn
mplsCvTrMpCvVerifyReverse=_MplsCvTrMpCvVerifyReverse_Object((1,3,6,1,4,1,629,10,12,1,1,1,7),_MplsCvTrMpCvVerifyReverse_Type())
mplsCvTrMpCvVerifyReverse.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpCvVerifyReverse.setStatus(_A)
class _MplsCvTrMpCvTtl_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_MplsCvTrMpCvTtl_Type.__name__=_D
_MplsCvTrMpCvTtl_Object=MibTableColumn
mplsCvTrMpCvTtl=_MplsCvTrMpCvTtl_Object((1,3,6,1,4,1,629,10,12,1,1,1,8),_MplsCvTrMpCvTtl_Type())
mplsCvTrMpCvTtl.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpCvTtl.setStatus(_A)
class _MplsCvTrMpCvReturnCode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12,13,256,257,258,259,260)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,256),(_X,257),(_Y,258),(_Z,259),(_a,260)))
_MplsCvTrMpCvReturnCode_Type.__name__=_F
_MplsCvTrMpCvReturnCode_Object=MibTableColumn
mplsCvTrMpCvReturnCode=_MplsCvTrMpCvReturnCode_Object((1,3,6,1,4,1,629,10,12,1,1,1,9),_MplsCvTrMpCvReturnCode_Type())
mplsCvTrMpCvReturnCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpCvReturnCode.setStatus(_A)
class _MplsCvTrMpCvRvsReturnCode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12,13,256,257,258,259,260)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,256),(_X,257),(_Y,258),(_Z,259),(_a,260)))
_MplsCvTrMpCvRvsReturnCode_Type.__name__=_F
_MplsCvTrMpCvRvsReturnCode_Object=MibTableColumn
mplsCvTrMpCvRvsReturnCode=_MplsCvTrMpCvRvsReturnCode_Object((1,3,6,1,4,1,629,10,12,1,1,1,10),_MplsCvTrMpCvRvsReturnCode_Type())
mplsCvTrMpCvRvsReturnCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpCvRvsReturnCode.setStatus(_A)
class _MplsCvTrMpCvRepliesRcvd_Type(Counter32):defaultValue=0
_MplsCvTrMpCvRepliesRcvd_Type.__name__=_g
_MplsCvTrMpCvRepliesRcvd_Object=MibTableColumn
mplsCvTrMpCvRepliesRcvd=_MplsCvTrMpCvRepliesRcvd_Object((1,3,6,1,4,1,629,10,12,1,1,1,11),_MplsCvTrMpCvRepliesRcvd_Type())
mplsCvTrMpCvRepliesRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpCvRepliesRcvd.setStatus(_A)
class _MplsCvTrMpCvRoundTripMin_Type(Unsigned32):defaultValue=0
_MplsCvTrMpCvRoundTripMin_Type.__name__=_D
_MplsCvTrMpCvRoundTripMin_Object=MibTableColumn
mplsCvTrMpCvRoundTripMin=_MplsCvTrMpCvRoundTripMin_Object((1,3,6,1,4,1,629,10,12,1,1,1,12),_MplsCvTrMpCvRoundTripMin_Type())
mplsCvTrMpCvRoundTripMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpCvRoundTripMin.setStatus(_A)
if mibBuilder.loadTexts:mplsCvTrMpCvRoundTripMin.setUnits(_G)
class _MplsCvTrMpCvRoundTripAve_Type(Unsigned32):defaultValue=0
_MplsCvTrMpCvRoundTripAve_Type.__name__=_D
_MplsCvTrMpCvRoundTripAve_Object=MibTableColumn
mplsCvTrMpCvRoundTripAve=_MplsCvTrMpCvRoundTripAve_Object((1,3,6,1,4,1,629,10,12,1,1,1,13),_MplsCvTrMpCvRoundTripAve_Type())
mplsCvTrMpCvRoundTripAve.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpCvRoundTripAve.setStatus(_A)
if mibBuilder.loadTexts:mplsCvTrMpCvRoundTripAve.setUnits(_G)
class _MplsCvTrMpCvRoundTripMax_Type(Unsigned32):defaultValue=0
_MplsCvTrMpCvRoundTripMax_Type.__name__=_D
_MplsCvTrMpCvRoundTripMax_Object=MibTableColumn
mplsCvTrMpCvRoundTripMax=_MplsCvTrMpCvRoundTripMax_Object((1,3,6,1,4,1,629,10,12,1,1,1,14),_MplsCvTrMpCvRoundTripMax_Type())
mplsCvTrMpCvRoundTripMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpCvRoundTripMax.setStatus(_A)
if mibBuilder.loadTexts:mplsCvTrMpCvRoundTripMax.setUnits(_G)
class _MplsCvTrMpTrStatus_Type(TruthValue):defaultValue=2
_MplsCvTrMpTrStatus_Type.__name__=_b
_MplsCvTrMpTrStatus_Object=MibTableColumn
mplsCvTrMpTrStatus=_MplsCvTrMpTrStatus_Object((1,3,6,1,4,1,629,10,12,1,1,1,15),_MplsCvTrMpTrStatus_Type())
mplsCvTrMpTrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpTrStatus.setStatus(_A)
class _MplsCvTrMpTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_MplsCvTrMpTimeout_Type.__name__=_D
_MplsCvTrMpTimeout_Object=MibTableColumn
mplsCvTrMpTimeout=_MplsCvTrMpTimeout_Object((1,3,6,1,4,1,629,10,12,1,1,1,16),_MplsCvTrMpTimeout_Type())
mplsCvTrMpTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsCvTrMpTimeout.setStatus(_A)
if mibBuilder.loadTexts:mplsCvTrMpTimeout.setUnits(_G)
class _MplsCvTrMpTrReturnCode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12,13,256,257,258,259,260)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,256),(_X,257),(_Y,258),(_Z,259),(_a,260)))
_MplsCvTrMpTrReturnCode_Type.__name__=_F
_MplsCvTrMpTrReturnCode_Object=MibTableColumn
mplsCvTrMpTrReturnCode=_MplsCvTrMpTrReturnCode_Object((1,3,6,1,4,1,629,10,12,1,1,1,17),_MplsCvTrMpTrReturnCode_Type())
mplsCvTrMpTrReturnCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrMpTrReturnCode.setStatus(_A)
_MplsTrHopMpTable_Object=MibTable
mplsTrHopMpTable=_MplsTrHopMpTable_Object((1,3,6,1,4,1,629,10,12,1,2))
if mibBuilder.loadTexts:mplsTrHopMpTable.setStatus(_A)
_MplsTrHopMpEntry_Object=MibTableRow
mplsTrHopMpEntry=_MplsTrHopMpEntry_Object((1,3,6,1,4,1,629,10,12,1,2,1))
mplsTrHopMpEntry.setIndexNames((0,_H,_I),(0,_B,_c),(0,_B,_i))
if mibBuilder.loadTexts:mplsTrHopMpEntry.setStatus(_A)
_MplsTrHopNumber_Type=Unsigned32
_MplsTrHopNumber_Object=MibTableColumn
mplsTrHopNumber=_MplsTrHopNumber_Object((1,3,6,1,4,1,629,10,12,1,2,1,1),_MplsTrHopNumber_Type())
mplsTrHopNumber.setMaxAccess(_h)
if mibBuilder.loadTexts:mplsTrHopNumber.setStatus(_A)
class _MplsTrHopMpReturnCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12,13,256,257,258,259,260)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,256),(_X,257),(_Y,258),(_Z,259),(_a,260)))
_MplsTrHopMpReturnCode_Type.__name__=_F
_MplsTrHopMpReturnCode_Object=MibTableColumn
mplsTrHopMpReturnCode=_MplsTrHopMpReturnCode_Object((1,3,6,1,4,1,629,10,12,1,2,1,2),_MplsTrHopMpReturnCode_Type())
mplsTrHopMpReturnCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpReturnCode.setStatus(_A)
_MplsTrHopMpNextHopAddressType_Type=InetAddressType
_MplsTrHopMpNextHopAddressType_Object=MibTableColumn
mplsTrHopMpNextHopAddressType=_MplsTrHopMpNextHopAddressType_Object((1,3,6,1,4,1,629,10,12,1,2,1,3),_MplsTrHopMpNextHopAddressType_Type())
mplsTrHopMpNextHopAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpNextHopAddressType.setStatus(_A)
_MplsTrHopMpNextHopAddress_Type=InetAddress
_MplsTrHopMpNextHopAddress_Object=MibTableColumn
mplsTrHopMpNextHopAddress=_MplsTrHopMpNextHopAddress_Object((1,3,6,1,4,1,629,10,12,1,2,1,4),_MplsTrHopMpNextHopAddress_Type())
mplsTrHopMpNextHopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpNextHopAddress.setStatus(_A)
_MplsTrHopMpLabel_Type=MplsLabel
_MplsTrHopMpLabel_Object=MibTableColumn
mplsTrHopMpLabel=_MplsTrHopMpLabel_Object((1,3,6,1,4,1,629,10,12,1,2,1,5),_MplsTrHopMpLabel_Type())
mplsTrHopMpLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpLabel.setStatus(_A)
_MplsTrHopMpRoundTrip_Type=Unsigned32
_MplsTrHopMpRoundTrip_Object=MibTableColumn
mplsTrHopMpRoundTrip=_MplsTrHopMpRoundTrip_Object((1,3,6,1,4,1,629,10,12,1,2,1,6),_MplsTrHopMpRoundTrip_Type())
mplsTrHopMpRoundTrip.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpRoundTrip.setStatus(_A)
if mibBuilder.loadTexts:mplsTrHopMpRoundTrip.setUnits(_G)
class _MplsTrHopMpMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MplsTrHopMpMtu_Type.__name__=_D
_MplsTrHopMpMtu_Object=MibTableColumn
mplsTrHopMpMtu=_MplsTrHopMpMtu_Object((1,3,6,1,4,1,629,10,12,1,2,1,7),_MplsTrHopMpMtu_Type())
mplsTrHopMpMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpMtu.setStatus(_A)
_MplsTrHopMpDownstreamIfAddrType_Type=InetAddressType
_MplsTrHopMpDownstreamIfAddrType_Object=MibTableColumn
mplsTrHopMpDownstreamIfAddrType=_MplsTrHopMpDownstreamIfAddrType_Object((1,3,6,1,4,1,629,10,12,1,2,1,100),_MplsTrHopMpDownstreamIfAddrType_Type())
mplsTrHopMpDownstreamIfAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpDownstreamIfAddrType.setStatus(_A)
_MplsTrHopMpDownstreamIfAddr_Type=InetAddress
_MplsTrHopMpDownstreamIfAddr_Object=MibTableColumn
mplsTrHopMpDownstreamIfAddr=_MplsTrHopMpDownstreamIfAddr_Object((1,3,6,1,4,1,629,10,12,1,2,1,101),_MplsTrHopMpDownstreamIfAddr_Type())
mplsTrHopMpDownstreamIfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpDownstreamIfAddr.setStatus(_A)
_MplsTrHopMpDownstreamIfIndex_Type=Unsigned32
_MplsTrHopMpDownstreamIfIndex_Object=MibTableColumn
mplsTrHopMpDownstreamIfIndex=_MplsTrHopMpDownstreamIfIndex_Object((1,3,6,1,4,1,629,10,12,1,2,1,102),_MplsTrHopMpDownstreamIfIndex_Type())
mplsTrHopMpDownstreamIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrHopMpDownstreamIfIndex.setStatus(_A)
_MplsCvTrSysCounterTable_Object=MibTable
mplsCvTrSysCounterTable=_MplsCvTrSysCounterTable_Object((1,3,6,1,4,1,629,10,12,1,3))
if mibBuilder.loadTexts:mplsCvTrSysCounterTable.setStatus(_A)
_MplsCvTrSysCounterEntry_Object=MibTableRow
mplsCvTrSysCounterEntry=_MplsCvTrSysCounterEntry_Object((1,3,6,1,4,1,629,10,12,1,3,1))
mplsCvTrSysCounterEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mplsCvTrSysCounterEntry.setStatus(_A)
_MplsCvTrSysCounterReqsSent_Type=Counter32
_MplsCvTrSysCounterReqsSent_Object=MibTableColumn
mplsCvTrSysCounterReqsSent=_MplsCvTrSysCounterReqsSent_Object((1,3,6,1,4,1,629,10,12,1,3,1,1),_MplsCvTrSysCounterReqsSent_Type())
mplsCvTrSysCounterReqsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterReqsSent.setStatus(_A)
_MplsCvTrSysCounterReqsRcvd_Type=Counter32
_MplsCvTrSysCounterReqsRcvd_Object=MibTableColumn
mplsCvTrSysCounterReqsRcvd=_MplsCvTrSysCounterReqsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,2),_MplsCvTrSysCounterReqsRcvd_Type())
mplsCvTrSysCounterReqsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterReqsRcvd.setStatus(_A)
_MplsCvTrSysCounterTotalRepsSent_Type=Counter32
_MplsCvTrSysCounterTotalRepsSent_Object=MibTableColumn
mplsCvTrSysCounterTotalRepsSent=_MplsCvTrSysCounterTotalRepsSent_Object((1,3,6,1,4,1,629,10,12,1,3,1,3),_MplsCvTrSysCounterTotalRepsSent_Type())
mplsCvTrSysCounterTotalRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterTotalRepsSent.setStatus(_A)
_MplsCvTrSysCounterTotalRepsRcvd_Type=Counter32
_MplsCvTrSysCounterTotalRepsRcvd_Object=MibTableColumn
mplsCvTrSysCounterTotalRepsRcvd=_MplsCvTrSysCounterTotalRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,4),_MplsCvTrSysCounterTotalRepsRcvd_Type())
mplsCvTrSysCounterTotalRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterTotalRepsRcvd.setStatus(_A)
_MplsCvTrSysCounterOKRepsSent_Type=Counter32
_MplsCvTrSysCounterOKRepsSent_Object=MibTableColumn
mplsCvTrSysCounterOKRepsSent=_MplsCvTrSysCounterOKRepsSent_Object((1,3,6,1,4,1,629,10,12,1,3,1,5),_MplsCvTrSysCounterOKRepsSent_Type())
mplsCvTrSysCounterOKRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterOKRepsSent.setStatus(_A)
_MplsCvTrSysCounterOKRepsRcvd_Type=Counter32
_MplsCvTrSysCounterOKRepsRcvd_Object=MibTableColumn
mplsCvTrSysCounterOKRepsRcvd=_MplsCvTrSysCounterOKRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,6),_MplsCvTrSysCounterOKRepsRcvd_Type())
mplsCvTrSysCounterOKRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterOKRepsRcvd.setStatus(_A)
_MplsCvTrSysCounterBadRepsSent_Type=Counter32
_MplsCvTrSysCounterBadRepsSent_Object=MibTableColumn
mplsCvTrSysCounterBadRepsSent=_MplsCvTrSysCounterBadRepsSent_Object((1,3,6,1,4,1,629,10,12,1,3,1,7),_MplsCvTrSysCounterBadRepsSent_Type())
mplsCvTrSysCounterBadRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterBadRepsSent.setStatus(_A)
_MplsCvTrSysCounterIllRepsSent_Type=Counter32
_MplsCvTrSysCounterIllRepsSent_Object=MibTableColumn
mplsCvTrSysCounterIllRepsSent=_MplsCvTrSysCounterIllRepsSent_Object((1,3,6,1,4,1,629,10,12,1,3,1,8),_MplsCvTrSysCounterIllRepsSent_Type())
mplsCvTrSysCounterIllRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterIllRepsSent.setStatus(_A)
_MplsCvTrSysCounterBadRepsRcvd_Type=Counter32
_MplsCvTrSysCounterBadRepsRcvd_Object=MibTableColumn
mplsCvTrSysCounterBadRepsRcvd=_MplsCvTrSysCounterBadRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,9),_MplsCvTrSysCounterBadRepsRcvd_Type())
mplsCvTrSysCounterBadRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterBadRepsRcvd.setStatus(_A)
_MplsCvTrSysCounterIllRepsRcvd_Type=Counter32
_MplsCvTrSysCounterIllRepsRcvd_Object=MibTableColumn
mplsCvTrSysCounterIllRepsRcvd=_MplsCvTrSysCounterIllRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,10),_MplsCvTrSysCounterIllRepsRcvd_Type())
mplsCvTrSysCounterIllRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterIllRepsRcvd.setStatus(_A)
_MplsCvTrSysCounterTmoRepsRcvd_Type=Counter32
_MplsCvTrSysCounterTmoRepsRcvd_Object=MibTableColumn
mplsCvTrSysCounterTmoRepsRcvd=_MplsCvTrSysCounterTmoRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,11),_MplsCvTrSysCounterTmoRepsRcvd_Type())
mplsCvTrSysCounterTmoRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterTmoRepsRcvd.setStatus(_A)
_MplsCvTrSysCounterBadSeqRepsRcvd_Type=Counter32
_MplsCvTrSysCounterBadSeqRepsRcvd_Object=MibTableColumn
mplsCvTrSysCounterBadSeqRepsRcvd=_MplsCvTrSysCounterBadSeqRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,3,1,12),_MplsCvTrSysCounterBadSeqRepsRcvd_Type())
mplsCvTrSysCounterBadSeqRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsCvTrSysCounterBadSeqRepsRcvd.setStatus(_A)
_MplsMpCvTrCntrTable_Object=MibTable
mplsMpCvTrCntrTable=_MplsMpCvTrCntrTable_Object((1,3,6,1,4,1,629,10,12,1,4))
if mibBuilder.loadTexts:mplsMpCvTrCntrTable.setStatus(_A)
_MplsMpCvTrCntrEntry_Object=MibTableRow
mplsMpCvTrCntrEntry=_MplsMpCvTrCntrEntry_Object((1,3,6,1,4,1,629,10,12,1,4,1))
mplsMpCvTrCntrEntry.setIndexNames((0,_H,_I),(0,_e,_f))
if mibBuilder.loadTexts:mplsMpCvTrCntrEntry.setStatus(_A)
_MplsMpCvTrCntrNextSeqToSend_Type=Unsigned32
_MplsMpCvTrCntrNextSeqToSend_Object=MibTableColumn
mplsMpCvTrCntrNextSeqToSend=_MplsMpCvTrCntrNextSeqToSend_Object((1,3,6,1,4,1,629,10,12,1,4,1,1),_MplsMpCvTrCntrNextSeqToSend_Type())
mplsMpCvTrCntrNextSeqToSend.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrNextSeqToSend.setStatus(_A)
class _MplsMpCvTrCntrLastRcvdRetCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12,13,256,257,258,259,260)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,256),(_X,257),(_Y,258),(_Z,259),(_a,260)))
_MplsMpCvTrCntrLastRcvdRetCode_Type.__name__=_F
_MplsMpCvTrCntrLastRcvdRetCode_Object=MibTableColumn
mplsMpCvTrCntrLastRcvdRetCode=_MplsMpCvTrCntrLastRcvdRetCode_Object((1,3,6,1,4,1,629,10,12,1,4,1,2),_MplsMpCvTrCntrLastRcvdRetCode_Type())
mplsMpCvTrCntrLastRcvdRetCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrLastRcvdRetCode.setStatus(_A)
_MplsMpCvTrCntrReqsSent_Type=Counter32
_MplsMpCvTrCntrReqsSent_Object=MibTableColumn
mplsMpCvTrCntrReqsSent=_MplsMpCvTrCntrReqsSent_Object((1,3,6,1,4,1,629,10,12,1,4,1,3),_MplsMpCvTrCntrReqsSent_Type())
mplsMpCvTrCntrReqsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrReqsSent.setStatus(_A)
_MplsMpCvTrCntrReqsRcvd_Type=Counter32
_MplsMpCvTrCntrReqsRcvd_Object=MibTableColumn
mplsMpCvTrCntrReqsRcvd=_MplsMpCvTrCntrReqsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,4),_MplsMpCvTrCntrReqsRcvd_Type())
mplsMpCvTrCntrReqsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrReqsRcvd.setStatus(_A)
_MplsMpCvTrCntrTotalRepsSent_Type=Counter32
_MplsMpCvTrCntrTotalRepsSent_Object=MibTableColumn
mplsMpCvTrCntrTotalRepsSent=_MplsMpCvTrCntrTotalRepsSent_Object((1,3,6,1,4,1,629,10,12,1,4,1,5),_MplsMpCvTrCntrTotalRepsSent_Type())
mplsMpCvTrCntrTotalRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrTotalRepsSent.setStatus(_A)
_MplsMpCvTrCntrTotalRepsRcvd_Type=Counter32
_MplsMpCvTrCntrTotalRepsRcvd_Object=MibTableColumn
mplsMpCvTrCntrTotalRepsRcvd=_MplsMpCvTrCntrTotalRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,6),_MplsMpCvTrCntrTotalRepsRcvd_Type())
mplsMpCvTrCntrTotalRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrTotalRepsRcvd.setStatus(_A)
_MplsMpCvTrCntrOKRepsSent_Type=Counter32
_MplsMpCvTrCntrOKRepsSent_Object=MibTableColumn
mplsMpCvTrCntrOKRepsSent=_MplsMpCvTrCntrOKRepsSent_Object((1,3,6,1,4,1,629,10,12,1,4,1,7),_MplsMpCvTrCntrOKRepsSent_Type())
mplsMpCvTrCntrOKRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrOKRepsSent.setStatus(_A)
_MplsMpCvTrCntrOKRepsRcvd_Type=Counter32
_MplsMpCvTrCntrOKRepsRcvd_Object=MibTableColumn
mplsMpCvTrCntrOKRepsRcvd=_MplsMpCvTrCntrOKRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,8),_MplsMpCvTrCntrOKRepsRcvd_Type())
mplsMpCvTrCntrOKRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrOKRepsRcvd.setStatus(_A)
_MplsMpCvTrCntrBadRepsSent_Type=Counter32
_MplsMpCvTrCntrBadRepsSent_Object=MibTableColumn
mplsMpCvTrCntrBadRepsSent=_MplsMpCvTrCntrBadRepsSent_Object((1,3,6,1,4,1,629,10,12,1,4,1,9),_MplsMpCvTrCntrBadRepsSent_Type())
mplsMpCvTrCntrBadRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrBadRepsSent.setStatus(_A)
_MplsMpCvTrCntrIllRepsSent_Type=Counter32
_MplsMpCvTrCntrIllRepsSent_Object=MibTableColumn
mplsMpCvTrCntrIllRepsSent=_MplsMpCvTrCntrIllRepsSent_Object((1,3,6,1,4,1,629,10,12,1,4,1,10),_MplsMpCvTrCntrIllRepsSent_Type())
mplsMpCvTrCntrIllRepsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrIllRepsSent.setStatus(_A)
_MplsMpCvTrCntrBadRepsRcvd_Type=Counter32
_MplsMpCvTrCntrBadRepsRcvd_Object=MibTableColumn
mplsMpCvTrCntrBadRepsRcvd=_MplsMpCvTrCntrBadRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,11),_MplsMpCvTrCntrBadRepsRcvd_Type())
mplsMpCvTrCntrBadRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrBadRepsRcvd.setStatus(_A)
_MplsMpCvTrCntrIllRepsRcvd_Type=Counter32
_MplsMpCvTrCntrIllRepsRcvd_Object=MibTableColumn
mplsMpCvTrCntrIllRepsRcvd=_MplsMpCvTrCntrIllRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,12),_MplsMpCvTrCntrIllRepsRcvd_Type())
mplsMpCvTrCntrIllRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrIllRepsRcvd.setStatus(_A)
_MplsMpCvTrCntrTmoRepsRcvd_Type=Counter32
_MplsMpCvTrCntrTmoRepsRcvd_Object=MibTableColumn
mplsMpCvTrCntrTmoRepsRcvd=_MplsMpCvTrCntrTmoRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,13),_MplsMpCvTrCntrTmoRepsRcvd_Type())
mplsMpCvTrCntrTmoRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrTmoRepsRcvd.setStatus(_A)
_MplsMpCvTrCntrBadSeqRepsRcvd_Type=Counter32
_MplsMpCvTrCntrBadSeqRepsRcvd_Object=MibTableColumn
mplsMpCvTrCntrBadSeqRepsRcvd=_MplsMpCvTrCntrBadSeqRepsRcvd_Object((1,3,6,1,4,1,629,10,12,1,4,1,14),_MplsMpCvTrCntrBadSeqRepsRcvd_Type())
mplsMpCvTrCntrBadSeqRepsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpCvTrCntrBadSeqRepsRcvd.setStatus(_A)
_LsppConformance_ObjectIdentity=ObjectIdentity
lsppConformance=_LsppConformance_ObjectIdentity((1,3,6,1,4,1,629,10,12,2))
_LsppGroups_ObjectIdentity=ObjectIdentity
lsppGroups=_LsppGroups_ObjectIdentity((1,3,6,1,4,1,629,10,12,2,1))
_LsppCompliances_ObjectIdentity=ObjectIdentity
lsppCompliances=_LsppCompliances_ObjectIdentity((1,3,6,1,4,1,629,10,12,2,2))
lsppGeneralGroup=ObjectGroup((1,3,6,1,4,1,629,10,12,2,1,1))
lsppGeneralGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:lsppGeneralGroup.setStatus(_A)
lsppModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,12,2,2,1))
lsppModuleFullCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:lsppModuleFullCompliance.setStatus(_A)
lsppModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,12,2,2,2))
lsppModuleReadOnlyCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:lsppModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbase':nbase,'opx':opx,'lspPingMib':lspPingMib,'lsppObjects':lsppObjects,'mplsCvTrMpTable':mplsCvTrMpTable,'mplsCvTrMpEntry':mplsCvTrMpEntry,_c:mplsCvTrMpIndex,_j:mplsCvTrMpRowStatus,_k:mplsCvTrMpPhb,_l:mplsCvTrMpCvStatus,_m:mplsCvTrMpCvMessages,_n:mplsCvTrMpCvInterval,_o:mplsCvTrMpCvVerifyReverse,_p:mplsCvTrMpCvTtl,_q:mplsCvTrMpCvReturnCode,_r:mplsCvTrMpCvRvsReturnCode,_s:mplsCvTrMpCvRepliesRcvd,_t:mplsCvTrMpCvRoundTripMin,_u:mplsCvTrMpCvRoundTripAve,_v:mplsCvTrMpCvRoundTripMax,_w:mplsCvTrMpTrStatus,_x:mplsCvTrMpTimeout,_y:mplsCvTrMpTrReturnCode,'mplsTrHopMpTable':mplsTrHopMpTable,'mplsTrHopMpEntry':mplsTrHopMpEntry,_i:mplsTrHopNumber,_z:mplsTrHopMpReturnCode,_A0:mplsTrHopMpNextHopAddressType,_A1:mplsTrHopMpNextHopAddress,_A2:mplsTrHopMpLabel,_A3:mplsTrHopMpRoundTrip,_A4:mplsTrHopMpMtu,_A5:mplsTrHopMpDownstreamIfAddrType,_A6:mplsTrHopMpDownstreamIfAddr,_A7:mplsTrHopMpDownstreamIfIndex,'mplsCvTrSysCounterTable':mplsCvTrSysCounterTable,'mplsCvTrSysCounterEntry':mplsCvTrSysCounterEntry,_A8:mplsCvTrSysCounterReqsSent,_A9:mplsCvTrSysCounterReqsRcvd,_AA:mplsCvTrSysCounterTotalRepsSent,_AB:mplsCvTrSysCounterTotalRepsRcvd,_AC:mplsCvTrSysCounterOKRepsSent,_AD:mplsCvTrSysCounterOKRepsRcvd,_AE:mplsCvTrSysCounterBadRepsSent,_AF:mplsCvTrSysCounterIllRepsSent,_AG:mplsCvTrSysCounterBadRepsRcvd,_AH:mplsCvTrSysCounterIllRepsRcvd,_AI:mplsCvTrSysCounterTmoRepsRcvd,_AJ:mplsCvTrSysCounterBadSeqRepsRcvd,'mplsMpCvTrCntrTable':mplsMpCvTrCntrTable,'mplsMpCvTrCntrEntry':mplsMpCvTrCntrEntry,_AK:mplsMpCvTrCntrNextSeqToSend,_AL:mplsMpCvTrCntrLastRcvdRetCode,_AM:mplsMpCvTrCntrReqsSent,_AN:mplsMpCvTrCntrReqsRcvd,_AO:mplsMpCvTrCntrTotalRepsSent,_AP:mplsMpCvTrCntrTotalRepsRcvd,_AQ:mplsMpCvTrCntrOKRepsSent,_AR:mplsMpCvTrCntrOKRepsRcvd,_AS:mplsMpCvTrCntrBadRepsSent,_AT:mplsMpCvTrCntrIllRepsSent,_AU:mplsMpCvTrCntrBadRepsRcvd,_AV:mplsMpCvTrCntrIllRepsRcvd,_AW:mplsMpCvTrCntrTmoRepsRcvd,_AX:mplsMpCvTrCntrBadSeqRepsRcvd,'lsppConformance':lsppConformance,'lsppGroups':lsppGroups,_d:lsppGeneralGroup,'lsppCompliances':lsppCompliances,'lsppModuleFullCompliance':lsppModuleFullCompliance,'lsppModuleReadOnlyCompliance':lsppModuleReadOnlyCompliance})