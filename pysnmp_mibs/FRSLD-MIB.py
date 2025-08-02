_B2='frsldPvcSampleGeneralGroup'
_B1='frsldPvcSampleAvailGroup'
_B0='frsldPvcSampleHCDataGroup'
_A_='frsldPvcSampleHCFrameGroup'
_Az='frsldPvcSampleDataGroup'
_Ay='frsldPvcSampleDelayGroup'
_Ax='frsldPvcDelayDataGroup'
_Aw='frsldPvcSampleCtrlGroup'
_Av='frsldPvcDelayCtrlGroup'
_Au='frsldPvcPacketGroup'
_At='frsldPvcHCOctetDataGroup'
_As='frsldPvcHCFrameDataGroup'
_Ar='frsldCapabilitiesGroup'
_Aq='frsldPvcReqDataGroup'
_Ap='frsldPvcReqCtrlGroup'
_Ao='frsldNumSmplCtrls'
_An='frsldMaxSmplCtrls'
_Am='frsldNumPvcCtrls'
_Al='frsldMaxPvcCtrls'
_Ak='frsldRPCaps'
_Aj='frsldSmplCtrlWriteCaps'
_Ai='frsldPvcCtrlWriteCaps'
_Ah='frsldPvcSmplEndTime'
_Ag='frsldPvcSmplStartTime'
_Af='frsldPvcSmplUnavailables'
_Ae='frsldPvcSmplUnavailableTime'
_Ad='frsldPvcSmplHCDataOfferedE'
_Ac='frsldPvcSmplHCDataOfferedC'
_Ab='frsldPvcSmplHCDataDeliveredE'
_Aa='frsldPvcSmplHCDataDeliveredC'
_AZ='frsldPvcSmplHCFrOfferedE'
_AY='frsldPvcSmplHCFrOfferedC'
_AX='frsldPvcSmplHCFrDeliveredE'
_AW='frsldPvcSmplHCFrDeliveredC'
_AV='frsldPvcSmplDataOfferedE'
_AU='frsldPvcSmplDataOfferedC'
_AT='frsldPvcSmplDataDeliveredE'
_AS='frsldPvcSmplDataDeliveredC'
_AR='frsldPvcSmplFrOfferedE'
_AQ='frsldPvcSmplFrOfferedC'
_AP='frsldPvcSmplFrDeliveredE'
_AO='frsldPvcSmplFrDeliveredC'
_AN='frsldPvcSmplMissedPolls'
_AM='frsldPvcSmplDelayAvg'
_AL='frsldPvcSmplDelayMax'
_AK='frsldPvcSmplDelayMin'
_AJ='frsldPvcDataHCDataOfferedE'
_AI='frsldPvcDataHCDataOfferedC'
_AH='frsldPvcDataHCDataDeliveredE'
_AG='frsldPvcDataHCDataDeliveredC'
_AF='frsldPvcDataHCFrOfferedE'
_AE='frsldPvcDataHCFrOfferedC'
_AD='frsldPvcDataHCFrDeliveredE'
_AC='frsldPvcDataHCFrDeliveredC'
_AB='frsldPvcDataMissedPolls'
_AA='frsldPvcDataUnavailables'
_A9='frsldPvcDataUnavailableTime'
_A8='frsldPvcDataDataOfferedE'
_A7='frsldPvcDataDataOfferedC'
_A6='frsldPvcDataDataDeliveredE'
_A5='frsldPvcDataDataDeliveredC'
_A4='frsldPvcDataFrOfferedE'
_A3='frsldPvcDataFrOfferedC'
_A2='frsldPvcDataFrDeliveredE'
_A1='frsldPvcDataFrDeliveredC'
_A0='frsldSmplCtrlBucketsGranted'
_z='frsldSmplCtrlColPeriod'
_y='frsldPvcCtrlLastPurgeTime'
_x='read-write'
_w='frsldPvcSmplIdx'
_v='otherRxRemoteRP'
_u='eqoRxRemoteRP'
_t='eqiRxRemoteRP'
_s='tpRxRemoteRP'
_r='ingRxRemoteRP'
_q='desRemoteRP'
_p='otherRxLocalRP'
_o='eqoRxLocalRP'
_n='eqiRxLocalRP'
_m='tpRxLocalRP'
_l='ingRxLocalRP'
_k='desLocalRP'
_j='otherTxRemoteRP'
_i='eqoTxRemoteRP'
_h='eqiTxRemoteRP'
_g='tpTxRemoteRP'
_f='ingTxRemoteRP'
_e='srcRemoteRP'
_d='otherTxLocalRP'
_c='eqoTxLocalRP'
_b='eqiTxLocalRP'
_a='tpTxLocalRP'
_Z='ingTxLocalRP'
_Y='srcLocalRP'
_X='frsldSmplCtrlBuckets'
_W='frsldSmplCtrlStatus'
_V='frsldPvcCtrlDeleteOnPurge'
_U='frsldPvcCtrlPurge'
_T='frsldPvcCtrlDelayTimeOut'
_S='frsldPvcCtrlDelayType'
_R='frsldPvcCtrlDelayFrSize'
_Q='frsldPvcCtrlPacketFreq'
_P='frsldPvcCtrlStatus'
_O='microseconds'
_N='frsldSmplCtrlIdx'
_M='seconds'
_L='Bits'
_K='not-accessible'
_J='frsldPvcCtrlReceiveRP'
_I='frsldPvcCtrlTransmitRP'
_H='frsldPvcCtrlDlci'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='FRSLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DLCI,=mibBuilder.importSymbols('FRAME-RELAY-DTE-MIB','DLCI')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
frsldMIB=ModuleIdentity((1,3,6,1,2,1,95))
if mibBuilder.loadTexts:frsldMIB.setRevisions(('2002-01-03 00:00',))
class FrsldTxRP(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6),(_e,7),(_f,8),(_g,9),(_h,10),(_i,11),(_j,12)))
class FrsldRxRP(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7),(_r,8),(_s,9),(_t,10),(_u,11),(_v,12)))
_FrsldObjects_ObjectIdentity=ObjectIdentity
frsldObjects=_FrsldObjects_ObjectIdentity((1,3,6,1,2,1,95,1))
_FrsldPvcCtrlTable_Object=MibTable
frsldPvcCtrlTable=_FrsldPvcCtrlTable_Object((1,3,6,1,2,1,95,1,1))
if mibBuilder.loadTexts:frsldPvcCtrlTable.setStatus(_A)
_FrsldPvcCtrlEntry_Object=MibTableRow
frsldPvcCtrlEntry=_FrsldPvcCtrlEntry_Object((1,3,6,1,2,1,95,1,1,1))
frsldPvcCtrlEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:frsldPvcCtrlEntry.setStatus(_A)
_FrsldPvcCtrlDlci_Type=DLCI
_FrsldPvcCtrlDlci_Object=MibTableColumn
frsldPvcCtrlDlci=_FrsldPvcCtrlDlci_Object((1,3,6,1,2,1,95,1,1,1,1),_FrsldPvcCtrlDlci_Type())
frsldPvcCtrlDlci.setMaxAccess(_K)
if mibBuilder.loadTexts:frsldPvcCtrlDlci.setStatus(_A)
_FrsldPvcCtrlTransmitRP_Type=FrsldTxRP
_FrsldPvcCtrlTransmitRP_Object=MibTableColumn
frsldPvcCtrlTransmitRP=_FrsldPvcCtrlTransmitRP_Object((1,3,6,1,2,1,95,1,1,1,2),_FrsldPvcCtrlTransmitRP_Type())
frsldPvcCtrlTransmitRP.setMaxAccess(_K)
if mibBuilder.loadTexts:frsldPvcCtrlTransmitRP.setStatus(_A)
_FrsldPvcCtrlReceiveRP_Type=FrsldRxRP
_FrsldPvcCtrlReceiveRP_Object=MibTableColumn
frsldPvcCtrlReceiveRP=_FrsldPvcCtrlReceiveRP_Object((1,3,6,1,2,1,95,1,1,1,3),_FrsldPvcCtrlReceiveRP_Type())
frsldPvcCtrlReceiveRP.setMaxAccess(_K)
if mibBuilder.loadTexts:frsldPvcCtrlReceiveRP.setStatus(_A)
_FrsldPvcCtrlStatus_Type=RowStatus
_FrsldPvcCtrlStatus_Object=MibTableColumn
frsldPvcCtrlStatus=_FrsldPvcCtrlStatus_Object((1,3,6,1,2,1,95,1,1,1,4),_FrsldPvcCtrlStatus_Type())
frsldPvcCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlStatus.setStatus(_A)
class _FrsldPvcCtrlPacketFreq_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrsldPvcCtrlPacketFreq_Type.__name__=_D
_FrsldPvcCtrlPacketFreq_Object=MibTableColumn
frsldPvcCtrlPacketFreq=_FrsldPvcCtrlPacketFreq_Object((1,3,6,1,2,1,95,1,1,1,5),_FrsldPvcCtrlPacketFreq_Type())
frsldPvcCtrlPacketFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlPacketFreq.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcCtrlPacketFreq.setUnits(_M)
class _FrsldPvcCtrlDelayFrSize_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8188))
_FrsldPvcCtrlDelayFrSize_Type.__name__=_D
_FrsldPvcCtrlDelayFrSize_Object=MibTableColumn
frsldPvcCtrlDelayFrSize=_FrsldPvcCtrlDelayFrSize_Object((1,3,6,1,2,1,95,1,1,1,6),_FrsldPvcCtrlDelayFrSize_Type())
frsldPvcCtrlDelayFrSize.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlDelayFrSize.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcCtrlDelayFrSize.setUnits('octets')
class _FrsldPvcCtrlDelayType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneWay',1),('roundTrip',2)))
_FrsldPvcCtrlDelayType_Type.__name__=_D
_FrsldPvcCtrlDelayType_Object=MibTableColumn
frsldPvcCtrlDelayType=_FrsldPvcCtrlDelayType_Object((1,3,6,1,2,1,95,1,1,1,7),_FrsldPvcCtrlDelayType_Type())
frsldPvcCtrlDelayType.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlDelayType.setStatus(_A)
class _FrsldPvcCtrlDelayTimeOut_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_FrsldPvcCtrlDelayTimeOut_Type.__name__=_D
_FrsldPvcCtrlDelayTimeOut_Object=MibTableColumn
frsldPvcCtrlDelayTimeOut=_FrsldPvcCtrlDelayTimeOut_Object((1,3,6,1,2,1,95,1,1,1,8),_FrsldPvcCtrlDelayTimeOut_Type())
frsldPvcCtrlDelayTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlDelayTimeOut.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcCtrlDelayTimeOut.setUnits(_M)
class _FrsldPvcCtrlPurge_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,172800))
_FrsldPvcCtrlPurge_Type.__name__=_D
_FrsldPvcCtrlPurge_Object=MibTableColumn
frsldPvcCtrlPurge=_FrsldPvcCtrlPurge_Object((1,3,6,1,2,1,95,1,1,1,9),_FrsldPvcCtrlPurge_Type())
frsldPvcCtrlPurge.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlPurge.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcCtrlPurge.setUnits(_M)
class _FrsldPvcCtrlDeleteOnPurge_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('sampleContols',2),('all',3)))
_FrsldPvcCtrlDeleteOnPurge_Type.__name__=_D
_FrsldPvcCtrlDeleteOnPurge_Object=MibTableColumn
frsldPvcCtrlDeleteOnPurge=_FrsldPvcCtrlDeleteOnPurge_Object((1,3,6,1,2,1,95,1,1,1,10),_FrsldPvcCtrlDeleteOnPurge_Type())
frsldPvcCtrlDeleteOnPurge.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldPvcCtrlDeleteOnPurge.setStatus(_A)
_FrsldPvcCtrlLastPurgeTime_Type=TimeStamp
_FrsldPvcCtrlLastPurgeTime_Object=MibTableColumn
frsldPvcCtrlLastPurgeTime=_FrsldPvcCtrlLastPurgeTime_Object((1,3,6,1,2,1,95,1,1,1,11),_FrsldPvcCtrlLastPurgeTime_Type())
frsldPvcCtrlLastPurgeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcCtrlLastPurgeTime.setStatus(_A)
_FrsldSmplCtrlTable_Object=MibTable
frsldSmplCtrlTable=_FrsldSmplCtrlTable_Object((1,3,6,1,2,1,95,1,2))
if mibBuilder.loadTexts:frsldSmplCtrlTable.setStatus(_A)
_FrsldSmplCtrlEntry_Object=MibTableRow
frsldSmplCtrlEntry=_FrsldSmplCtrlEntry_Object((1,3,6,1,2,1,95,1,2,1))
frsldSmplCtrlEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_N))
if mibBuilder.loadTexts:frsldSmplCtrlEntry.setStatus(_A)
class _FrsldSmplCtrlIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FrsldSmplCtrlIdx_Type.__name__=_D
_FrsldSmplCtrlIdx_Object=MibTableColumn
frsldSmplCtrlIdx=_FrsldSmplCtrlIdx_Object((1,3,6,1,2,1,95,1,2,1,1),_FrsldSmplCtrlIdx_Type())
frsldSmplCtrlIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:frsldSmplCtrlIdx.setStatus(_A)
_FrsldSmplCtrlStatus_Type=RowStatus
_FrsldSmplCtrlStatus_Object=MibTableColumn
frsldSmplCtrlStatus=_FrsldSmplCtrlStatus_Object((1,3,6,1,2,1,95,1,2,1,2),_FrsldSmplCtrlStatus_Type())
frsldSmplCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldSmplCtrlStatus.setStatus(_A)
class _FrsldSmplCtrlColPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrsldSmplCtrlColPeriod_Type.__name__=_D
_FrsldSmplCtrlColPeriod_Object=MibTableColumn
frsldSmplCtrlColPeriod=_FrsldSmplCtrlColPeriod_Object((1,3,6,1,2,1,95,1,2,1,3),_FrsldSmplCtrlColPeriod_Type())
frsldSmplCtrlColPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldSmplCtrlColPeriod.setStatus(_A)
if mibBuilder.loadTexts:frsldSmplCtrlColPeriod.setUnits(_M)
class _FrsldSmplCtrlBuckets_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FrsldSmplCtrlBuckets_Type.__name__=_D
_FrsldSmplCtrlBuckets_Object=MibTableColumn
frsldSmplCtrlBuckets=_FrsldSmplCtrlBuckets_Object((1,3,6,1,2,1,95,1,2,1,4),_FrsldSmplCtrlBuckets_Type())
frsldSmplCtrlBuckets.setMaxAccess(_E)
if mibBuilder.loadTexts:frsldSmplCtrlBuckets.setStatus(_A)
class _FrsldSmplCtrlBucketsGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrsldSmplCtrlBucketsGranted_Type.__name__=_D
_FrsldSmplCtrlBucketsGranted_Object=MibTableColumn
frsldSmplCtrlBucketsGranted=_FrsldSmplCtrlBucketsGranted_Object((1,3,6,1,2,1,95,1,2,1,5),_FrsldSmplCtrlBucketsGranted_Type())
frsldSmplCtrlBucketsGranted.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldSmplCtrlBucketsGranted.setStatus(_A)
_FrsldPvcDataTable_Object=MibTable
frsldPvcDataTable=_FrsldPvcDataTable_Object((1,3,6,1,2,1,95,1,3))
if mibBuilder.loadTexts:frsldPvcDataTable.setStatus(_A)
_FrsldPvcDataEntry_Object=MibTableRow
frsldPvcDataEntry=_FrsldPvcDataEntry_Object((1,3,6,1,2,1,95,1,3,1))
frsldPvcDataEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:frsldPvcDataEntry.setStatus(_A)
_FrsldPvcDataMissedPolls_Type=Counter32
_FrsldPvcDataMissedPolls_Object=MibTableColumn
frsldPvcDataMissedPolls=_FrsldPvcDataMissedPolls_Object((1,3,6,1,2,1,95,1,3,1,1),_FrsldPvcDataMissedPolls_Type())
frsldPvcDataMissedPolls.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataMissedPolls.setStatus(_A)
_FrsldPvcDataFrDeliveredC_Type=Counter32
_FrsldPvcDataFrDeliveredC_Object=MibTableColumn
frsldPvcDataFrDeliveredC=_FrsldPvcDataFrDeliveredC_Object((1,3,6,1,2,1,95,1,3,1,2),_FrsldPvcDataFrDeliveredC_Type())
frsldPvcDataFrDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataFrDeliveredC.setStatus(_A)
_FrsldPvcDataFrDeliveredE_Type=Counter32
_FrsldPvcDataFrDeliveredE_Object=MibTableColumn
frsldPvcDataFrDeliveredE=_FrsldPvcDataFrDeliveredE_Object((1,3,6,1,2,1,95,1,3,1,3),_FrsldPvcDataFrDeliveredE_Type())
frsldPvcDataFrDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataFrDeliveredE.setStatus(_A)
_FrsldPvcDataFrOfferedC_Type=Counter32
_FrsldPvcDataFrOfferedC_Object=MibTableColumn
frsldPvcDataFrOfferedC=_FrsldPvcDataFrOfferedC_Object((1,3,6,1,2,1,95,1,3,1,4),_FrsldPvcDataFrOfferedC_Type())
frsldPvcDataFrOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataFrOfferedC.setStatus(_A)
_FrsldPvcDataFrOfferedE_Type=Counter32
_FrsldPvcDataFrOfferedE_Object=MibTableColumn
frsldPvcDataFrOfferedE=_FrsldPvcDataFrOfferedE_Object((1,3,6,1,2,1,95,1,3,1,5),_FrsldPvcDataFrOfferedE_Type())
frsldPvcDataFrOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataFrOfferedE.setStatus(_A)
_FrsldPvcDataDataDeliveredC_Type=Counter32
_FrsldPvcDataDataDeliveredC_Object=MibTableColumn
frsldPvcDataDataDeliveredC=_FrsldPvcDataDataDeliveredC_Object((1,3,6,1,2,1,95,1,3,1,6),_FrsldPvcDataDataDeliveredC_Type())
frsldPvcDataDataDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataDataDeliveredC.setStatus(_A)
_FrsldPvcDataDataDeliveredE_Type=Counter32
_FrsldPvcDataDataDeliveredE_Object=MibTableColumn
frsldPvcDataDataDeliveredE=_FrsldPvcDataDataDeliveredE_Object((1,3,6,1,2,1,95,1,3,1,7),_FrsldPvcDataDataDeliveredE_Type())
frsldPvcDataDataDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataDataDeliveredE.setStatus(_A)
_FrsldPvcDataDataOfferedC_Type=Counter32
_FrsldPvcDataDataOfferedC_Object=MibTableColumn
frsldPvcDataDataOfferedC=_FrsldPvcDataDataOfferedC_Object((1,3,6,1,2,1,95,1,3,1,8),_FrsldPvcDataDataOfferedC_Type())
frsldPvcDataDataOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataDataOfferedC.setStatus(_A)
_FrsldPvcDataDataOfferedE_Type=Counter32
_FrsldPvcDataDataOfferedE_Object=MibTableColumn
frsldPvcDataDataOfferedE=_FrsldPvcDataDataOfferedE_Object((1,3,6,1,2,1,95,1,3,1,9),_FrsldPvcDataDataOfferedE_Type())
frsldPvcDataDataOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataDataOfferedE.setStatus(_A)
_FrsldPvcDataHCFrDeliveredC_Type=Counter64
_FrsldPvcDataHCFrDeliveredC_Object=MibTableColumn
frsldPvcDataHCFrDeliveredC=_FrsldPvcDataHCFrDeliveredC_Object((1,3,6,1,2,1,95,1,3,1,10),_FrsldPvcDataHCFrDeliveredC_Type())
frsldPvcDataHCFrDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCFrDeliveredC.setStatus(_A)
_FrsldPvcDataHCFrDeliveredE_Type=Counter64
_FrsldPvcDataHCFrDeliveredE_Object=MibTableColumn
frsldPvcDataHCFrDeliveredE=_FrsldPvcDataHCFrDeliveredE_Object((1,3,6,1,2,1,95,1,3,1,11),_FrsldPvcDataHCFrDeliveredE_Type())
frsldPvcDataHCFrDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCFrDeliveredE.setStatus(_A)
_FrsldPvcDataHCFrOfferedC_Type=Counter64
_FrsldPvcDataHCFrOfferedC_Object=MibTableColumn
frsldPvcDataHCFrOfferedC=_FrsldPvcDataHCFrOfferedC_Object((1,3,6,1,2,1,95,1,3,1,12),_FrsldPvcDataHCFrOfferedC_Type())
frsldPvcDataHCFrOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCFrOfferedC.setStatus(_A)
_FrsldPvcDataHCFrOfferedE_Type=Counter64
_FrsldPvcDataHCFrOfferedE_Object=MibTableColumn
frsldPvcDataHCFrOfferedE=_FrsldPvcDataHCFrOfferedE_Object((1,3,6,1,2,1,95,1,3,1,13),_FrsldPvcDataHCFrOfferedE_Type())
frsldPvcDataHCFrOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCFrOfferedE.setStatus(_A)
_FrsldPvcDataHCDataDeliveredC_Type=Counter64
_FrsldPvcDataHCDataDeliveredC_Object=MibTableColumn
frsldPvcDataHCDataDeliveredC=_FrsldPvcDataHCDataDeliveredC_Object((1,3,6,1,2,1,95,1,3,1,14),_FrsldPvcDataHCDataDeliveredC_Type())
frsldPvcDataHCDataDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCDataDeliveredC.setStatus(_A)
_FrsldPvcDataHCDataDeliveredE_Type=Counter64
_FrsldPvcDataHCDataDeliveredE_Object=MibTableColumn
frsldPvcDataHCDataDeliveredE=_FrsldPvcDataHCDataDeliveredE_Object((1,3,6,1,2,1,95,1,3,1,15),_FrsldPvcDataHCDataDeliveredE_Type())
frsldPvcDataHCDataDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCDataDeliveredE.setStatus(_A)
_FrsldPvcDataHCDataOfferedC_Type=Counter64
_FrsldPvcDataHCDataOfferedC_Object=MibTableColumn
frsldPvcDataHCDataOfferedC=_FrsldPvcDataHCDataOfferedC_Object((1,3,6,1,2,1,95,1,3,1,16),_FrsldPvcDataHCDataOfferedC_Type())
frsldPvcDataHCDataOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCDataOfferedC.setStatus(_A)
_FrsldPvcDataHCDataOfferedE_Type=Counter64
_FrsldPvcDataHCDataOfferedE_Object=MibTableColumn
frsldPvcDataHCDataOfferedE=_FrsldPvcDataHCDataOfferedE_Object((1,3,6,1,2,1,95,1,3,1,17),_FrsldPvcDataHCDataOfferedE_Type())
frsldPvcDataHCDataOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataHCDataOfferedE.setStatus(_A)
_FrsldPvcDataUnavailableTime_Type=TimeTicks
_FrsldPvcDataUnavailableTime_Object=MibTableColumn
frsldPvcDataUnavailableTime=_FrsldPvcDataUnavailableTime_Object((1,3,6,1,2,1,95,1,3,1,18),_FrsldPvcDataUnavailableTime_Type())
frsldPvcDataUnavailableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataUnavailableTime.setStatus(_A)
_FrsldPvcDataUnavailables_Type=Counter32
_FrsldPvcDataUnavailables_Object=MibTableColumn
frsldPvcDataUnavailables=_FrsldPvcDataUnavailables_Object((1,3,6,1,2,1,95,1,3,1,19),_FrsldPvcDataUnavailables_Type())
frsldPvcDataUnavailables.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcDataUnavailables.setStatus(_A)
_FrsldPvcSampleTable_Object=MibTable
frsldPvcSampleTable=_FrsldPvcSampleTable_Object((1,3,6,1,2,1,95,1,4))
if mibBuilder.loadTexts:frsldPvcSampleTable.setStatus(_A)
_FrsldPvcSampleEntry_Object=MibTableRow
frsldPvcSampleEntry=_FrsldPvcSampleEntry_Object((1,3,6,1,2,1,95,1,4,1))
frsldPvcSampleEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_N),(0,_B,_w))
if mibBuilder.loadTexts:frsldPvcSampleEntry.setStatus(_A)
class _FrsldPvcSmplIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrsldPvcSmplIdx_Type.__name__=_D
_FrsldPvcSmplIdx_Object=MibTableColumn
frsldPvcSmplIdx=_FrsldPvcSmplIdx_Object((1,3,6,1,2,1,95,1,4,1,1),_FrsldPvcSmplIdx_Type())
frsldPvcSmplIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:frsldPvcSmplIdx.setStatus(_A)
_FrsldPvcSmplDelayMin_Type=Gauge32
_FrsldPvcSmplDelayMin_Object=MibTableColumn
frsldPvcSmplDelayMin=_FrsldPvcSmplDelayMin_Object((1,3,6,1,2,1,95,1,4,1,2),_FrsldPvcSmplDelayMin_Type())
frsldPvcSmplDelayMin.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDelayMin.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcSmplDelayMin.setUnits(_O)
_FrsldPvcSmplDelayMax_Type=Gauge32
_FrsldPvcSmplDelayMax_Object=MibTableColumn
frsldPvcSmplDelayMax=_FrsldPvcSmplDelayMax_Object((1,3,6,1,2,1,95,1,4,1,3),_FrsldPvcSmplDelayMax_Type())
frsldPvcSmplDelayMax.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDelayMax.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcSmplDelayMax.setUnits(_O)
_FrsldPvcSmplDelayAvg_Type=Gauge32
_FrsldPvcSmplDelayAvg_Object=MibTableColumn
frsldPvcSmplDelayAvg=_FrsldPvcSmplDelayAvg_Object((1,3,6,1,2,1,95,1,4,1,4),_FrsldPvcSmplDelayAvg_Type())
frsldPvcSmplDelayAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDelayAvg.setStatus(_A)
if mibBuilder.loadTexts:frsldPvcSmplDelayAvg.setUnits(_O)
_FrsldPvcSmplMissedPolls_Type=Gauge32
_FrsldPvcSmplMissedPolls_Object=MibTableColumn
frsldPvcSmplMissedPolls=_FrsldPvcSmplMissedPolls_Object((1,3,6,1,2,1,95,1,4,1,5),_FrsldPvcSmplMissedPolls_Type())
frsldPvcSmplMissedPolls.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplMissedPolls.setStatus(_A)
_FrsldPvcSmplFrDeliveredC_Type=Gauge32
_FrsldPvcSmplFrDeliveredC_Object=MibTableColumn
frsldPvcSmplFrDeliveredC=_FrsldPvcSmplFrDeliveredC_Object((1,3,6,1,2,1,95,1,4,1,6),_FrsldPvcSmplFrDeliveredC_Type())
frsldPvcSmplFrDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplFrDeliveredC.setStatus(_A)
_FrsldPvcSmplFrDeliveredE_Type=Gauge32
_FrsldPvcSmplFrDeliveredE_Object=MibTableColumn
frsldPvcSmplFrDeliveredE=_FrsldPvcSmplFrDeliveredE_Object((1,3,6,1,2,1,95,1,4,1,7),_FrsldPvcSmplFrDeliveredE_Type())
frsldPvcSmplFrDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplFrDeliveredE.setStatus(_A)
_FrsldPvcSmplFrOfferedC_Type=Gauge32
_FrsldPvcSmplFrOfferedC_Object=MibTableColumn
frsldPvcSmplFrOfferedC=_FrsldPvcSmplFrOfferedC_Object((1,3,6,1,2,1,95,1,4,1,8),_FrsldPvcSmplFrOfferedC_Type())
frsldPvcSmplFrOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplFrOfferedC.setStatus(_A)
_FrsldPvcSmplFrOfferedE_Type=Gauge32
_FrsldPvcSmplFrOfferedE_Object=MibTableColumn
frsldPvcSmplFrOfferedE=_FrsldPvcSmplFrOfferedE_Object((1,3,6,1,2,1,95,1,4,1,9),_FrsldPvcSmplFrOfferedE_Type())
frsldPvcSmplFrOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplFrOfferedE.setStatus(_A)
_FrsldPvcSmplDataDeliveredC_Type=Gauge32
_FrsldPvcSmplDataDeliveredC_Object=MibTableColumn
frsldPvcSmplDataDeliveredC=_FrsldPvcSmplDataDeliveredC_Object((1,3,6,1,2,1,95,1,4,1,10),_FrsldPvcSmplDataDeliveredC_Type())
frsldPvcSmplDataDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDataDeliveredC.setStatus(_A)
_FrsldPvcSmplDataDeliveredE_Type=Gauge32
_FrsldPvcSmplDataDeliveredE_Object=MibTableColumn
frsldPvcSmplDataDeliveredE=_FrsldPvcSmplDataDeliveredE_Object((1,3,6,1,2,1,95,1,4,1,11),_FrsldPvcSmplDataDeliveredE_Type())
frsldPvcSmplDataDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDataDeliveredE.setStatus(_A)
_FrsldPvcSmplDataOfferedC_Type=Gauge32
_FrsldPvcSmplDataOfferedC_Object=MibTableColumn
frsldPvcSmplDataOfferedC=_FrsldPvcSmplDataOfferedC_Object((1,3,6,1,2,1,95,1,4,1,12),_FrsldPvcSmplDataOfferedC_Type())
frsldPvcSmplDataOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDataOfferedC.setStatus(_A)
_FrsldPvcSmplDataOfferedE_Type=Gauge32
_FrsldPvcSmplDataOfferedE_Object=MibTableColumn
frsldPvcSmplDataOfferedE=_FrsldPvcSmplDataOfferedE_Object((1,3,6,1,2,1,95,1,4,1,13),_FrsldPvcSmplDataOfferedE_Type())
frsldPvcSmplDataOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplDataOfferedE.setStatus(_A)
_FrsldPvcSmplHCFrDeliveredC_Type=CounterBasedGauge64
_FrsldPvcSmplHCFrDeliveredC_Object=MibTableColumn
frsldPvcSmplHCFrDeliveredC=_FrsldPvcSmplHCFrDeliveredC_Object((1,3,6,1,2,1,95,1,4,1,14),_FrsldPvcSmplHCFrDeliveredC_Type())
frsldPvcSmplHCFrDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCFrDeliveredC.setStatus(_A)
_FrsldPvcSmplHCFrDeliveredE_Type=CounterBasedGauge64
_FrsldPvcSmplHCFrDeliveredE_Object=MibTableColumn
frsldPvcSmplHCFrDeliveredE=_FrsldPvcSmplHCFrDeliveredE_Object((1,3,6,1,2,1,95,1,4,1,15),_FrsldPvcSmplHCFrDeliveredE_Type())
frsldPvcSmplHCFrDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCFrDeliveredE.setStatus(_A)
_FrsldPvcSmplHCFrOfferedC_Type=CounterBasedGauge64
_FrsldPvcSmplHCFrOfferedC_Object=MibTableColumn
frsldPvcSmplHCFrOfferedC=_FrsldPvcSmplHCFrOfferedC_Object((1,3,6,1,2,1,95,1,4,1,16),_FrsldPvcSmplHCFrOfferedC_Type())
frsldPvcSmplHCFrOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCFrOfferedC.setStatus(_A)
_FrsldPvcSmplHCFrOfferedE_Type=CounterBasedGauge64
_FrsldPvcSmplHCFrOfferedE_Object=MibTableColumn
frsldPvcSmplHCFrOfferedE=_FrsldPvcSmplHCFrOfferedE_Object((1,3,6,1,2,1,95,1,4,1,17),_FrsldPvcSmplHCFrOfferedE_Type())
frsldPvcSmplHCFrOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCFrOfferedE.setStatus(_A)
_FrsldPvcSmplHCDataDeliveredC_Type=CounterBasedGauge64
_FrsldPvcSmplHCDataDeliveredC_Object=MibTableColumn
frsldPvcSmplHCDataDeliveredC=_FrsldPvcSmplHCDataDeliveredC_Object((1,3,6,1,2,1,95,1,4,1,18),_FrsldPvcSmplHCDataDeliveredC_Type())
frsldPvcSmplHCDataDeliveredC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCDataDeliveredC.setStatus(_A)
_FrsldPvcSmplHCDataDeliveredE_Type=CounterBasedGauge64
_FrsldPvcSmplHCDataDeliveredE_Object=MibTableColumn
frsldPvcSmplHCDataDeliveredE=_FrsldPvcSmplHCDataDeliveredE_Object((1,3,6,1,2,1,95,1,4,1,19),_FrsldPvcSmplHCDataDeliveredE_Type())
frsldPvcSmplHCDataDeliveredE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCDataDeliveredE.setStatus(_A)
_FrsldPvcSmplHCDataOfferedC_Type=CounterBasedGauge64
_FrsldPvcSmplHCDataOfferedC_Object=MibTableColumn
frsldPvcSmplHCDataOfferedC=_FrsldPvcSmplHCDataOfferedC_Object((1,3,6,1,2,1,95,1,4,1,20),_FrsldPvcSmplHCDataOfferedC_Type())
frsldPvcSmplHCDataOfferedC.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCDataOfferedC.setStatus(_A)
_FrsldPvcSmplHCDataOfferedE_Type=CounterBasedGauge64
_FrsldPvcSmplHCDataOfferedE_Object=MibTableColumn
frsldPvcSmplHCDataOfferedE=_FrsldPvcSmplHCDataOfferedE_Object((1,3,6,1,2,1,95,1,4,1,21),_FrsldPvcSmplHCDataOfferedE_Type())
frsldPvcSmplHCDataOfferedE.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplHCDataOfferedE.setStatus(_A)
_FrsldPvcSmplUnavailableTime_Type=TimeTicks
_FrsldPvcSmplUnavailableTime_Object=MibTableColumn
frsldPvcSmplUnavailableTime=_FrsldPvcSmplUnavailableTime_Object((1,3,6,1,2,1,95,1,4,1,22),_FrsldPvcSmplUnavailableTime_Type())
frsldPvcSmplUnavailableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplUnavailableTime.setStatus(_A)
_FrsldPvcSmplUnavailables_Type=Gauge32
_FrsldPvcSmplUnavailables_Object=MibTableColumn
frsldPvcSmplUnavailables=_FrsldPvcSmplUnavailables_Object((1,3,6,1,2,1,95,1,4,1,23),_FrsldPvcSmplUnavailables_Type())
frsldPvcSmplUnavailables.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplUnavailables.setStatus(_A)
_FrsldPvcSmplStartTime_Type=TimeStamp
_FrsldPvcSmplStartTime_Object=MibTableColumn
frsldPvcSmplStartTime=_FrsldPvcSmplStartTime_Object((1,3,6,1,2,1,95,1,4,1,24),_FrsldPvcSmplStartTime_Type())
frsldPvcSmplStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplStartTime.setStatus(_A)
_FrsldPvcSmplEndTime_Type=TimeStamp
_FrsldPvcSmplEndTime_Object=MibTableColumn
frsldPvcSmplEndTime=_FrsldPvcSmplEndTime_Object((1,3,6,1,2,1,95,1,4,1,25),_FrsldPvcSmplEndTime_Type())
frsldPvcSmplEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcSmplEndTime.setStatus(_A)
_FrsldCapabilities_ObjectIdentity=ObjectIdentity
frsldCapabilities=_FrsldCapabilities_ObjectIdentity((1,3,6,1,2,1,95,2))
class _FrsldPvcCtrlWriteCaps_Type(Bits):namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6)))
_FrsldPvcCtrlWriteCaps_Type.__name__=_L
_FrsldPvcCtrlWriteCaps_Object=MibScalar
frsldPvcCtrlWriteCaps=_FrsldPvcCtrlWriteCaps_Object((1,3,6,1,2,1,95,2,1),_FrsldPvcCtrlWriteCaps_Type())
frsldPvcCtrlWriteCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldPvcCtrlWriteCaps.setStatus(_A)
class _FrsldSmplCtrlWriteCaps_Type(Bits):namedValues=NamedValues(*((_W,0),(_X,1)))
_FrsldSmplCtrlWriteCaps_Type.__name__=_L
_FrsldSmplCtrlWriteCaps_Object=MibScalar
frsldSmplCtrlWriteCaps=_FrsldSmplCtrlWriteCaps_Object((1,3,6,1,2,1,95,2,2),_FrsldSmplCtrlWriteCaps_Type())
frsldSmplCtrlWriteCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldSmplCtrlWriteCaps.setStatus(_A)
class _FrsldRPCaps_Type(Bits):namedValues=NamedValues(*((_Y,0),(_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_i,10),(_j,11),(_k,12),(_l,13),(_m,14),(_n,15),(_o,16),(_p,17),(_q,18),(_r,19),(_s,20),(_t,21),(_u,22),(_v,23)))
_FrsldRPCaps_Type.__name__=_L
_FrsldRPCaps_Object=MibScalar
frsldRPCaps=_FrsldRPCaps_Object((1,3,6,1,2,1,95,2,3),_FrsldRPCaps_Type())
frsldRPCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldRPCaps.setStatus(_A)
class _FrsldMaxPvcCtrls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrsldMaxPvcCtrls_Type.__name__=_D
_FrsldMaxPvcCtrls_Object=MibScalar
frsldMaxPvcCtrls=_FrsldMaxPvcCtrls_Object((1,3,6,1,2,1,95,2,4),_FrsldMaxPvcCtrls_Type())
frsldMaxPvcCtrls.setMaxAccess(_x)
if mibBuilder.loadTexts:frsldMaxPvcCtrls.setStatus(_A)
_FrsldNumPvcCtrls_Type=Gauge32
_FrsldNumPvcCtrls_Object=MibScalar
frsldNumPvcCtrls=_FrsldNumPvcCtrls_Object((1,3,6,1,2,1,95,2,5),_FrsldNumPvcCtrls_Type())
frsldNumPvcCtrls.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldNumPvcCtrls.setStatus(_A)
class _FrsldMaxSmplCtrls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrsldMaxSmplCtrls_Type.__name__=_D
_FrsldMaxSmplCtrls_Object=MibScalar
frsldMaxSmplCtrls=_FrsldMaxSmplCtrls_Object((1,3,6,1,2,1,95,2,6),_FrsldMaxSmplCtrls_Type())
frsldMaxSmplCtrls.setMaxAccess(_x)
if mibBuilder.loadTexts:frsldMaxSmplCtrls.setStatus(_A)
_FrsldNumSmplCtrls_Type=Gauge32
_FrsldNumSmplCtrls_Object=MibScalar
frsldNumSmplCtrls=_FrsldNumSmplCtrls_Object((1,3,6,1,2,1,95,2,7),_FrsldNumSmplCtrls_Type())
frsldNumSmplCtrls.setMaxAccess(_C)
if mibBuilder.loadTexts:frsldNumSmplCtrls.setStatus(_A)
_FrsldConformance_ObjectIdentity=ObjectIdentity
frsldConformance=_FrsldConformance_ObjectIdentity((1,3,6,1,2,1,95,3))
_FrsldMIBGroups_ObjectIdentity=ObjectIdentity
frsldMIBGroups=_FrsldMIBGroups_ObjectIdentity((1,3,6,1,2,1,95,3,1))
_FrsldMIBCompliances_ObjectIdentity=ObjectIdentity
frsldMIBCompliances=_FrsldMIBCompliances_ObjectIdentity((1,3,6,1,2,1,95,3,2))
frsldPvcReqCtrlGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,1))
frsldPvcReqCtrlGroup.setObjects(*((_B,_P),(_B,_U),(_B,_V),(_B,_y)))
if mibBuilder.loadTexts:frsldPvcReqCtrlGroup.setStatus(_A)
frsldPvcPacketGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,2))
frsldPvcPacketGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:frsldPvcPacketGroup.setStatus(_A)
frsldPvcDelayCtrlGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,3))
frsldPvcDelayCtrlGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:frsldPvcDelayCtrlGroup.setStatus(_A)
frsldPvcSampleCtrlGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,4))
frsldPvcSampleCtrlGroup.setObjects(*((_B,_W),(_B,_z),(_B,_X),(_B,_A0)))
if mibBuilder.loadTexts:frsldPvcSampleCtrlGroup.setStatus(_A)
frsldPvcReqDataGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,5))
frsldPvcReqDataGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:frsldPvcReqDataGroup.setStatus(_A)
frsldPvcDelayDataGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,6))
frsldPvcDelayDataGroup.setObjects((_B,_AB))
if mibBuilder.loadTexts:frsldPvcDelayDataGroup.setStatus(_A)
frsldPvcHCFrameDataGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,7))
frsldPvcHCFrameDataGroup.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:frsldPvcHCFrameDataGroup.setStatus(_A)
frsldPvcHCOctetDataGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,8))
frsldPvcHCOctetDataGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:frsldPvcHCOctetDataGroup.setStatus(_A)
frsldPvcSampleDelayGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,9))
frsldPvcSampleDelayGroup.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:frsldPvcSampleDelayGroup.setStatus(_A)
frsldPvcSampleDataGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,10))
frsldPvcSampleDataGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:frsldPvcSampleDataGroup.setStatus(_A)
frsldPvcSampleHCFrameGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,11))
frsldPvcSampleHCFrameGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:frsldPvcSampleHCFrameGroup.setStatus(_A)
frsldPvcSampleHCDataGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,12))
frsldPvcSampleHCDataGroup.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:frsldPvcSampleHCDataGroup.setStatus(_A)
frsldPvcSampleAvailGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,13))
frsldPvcSampleAvailGroup.setObjects(*((_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:frsldPvcSampleAvailGroup.setStatus(_A)
frsldPvcSampleGeneralGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,14))
frsldPvcSampleGeneralGroup.setObjects(*((_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:frsldPvcSampleGeneralGroup.setStatus(_A)
frsldCapabilitiesGroup=ObjectGroup((1,3,6,1,2,1,95,3,1,15))
frsldCapabilitiesGroup.setObjects(*((_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao)))
if mibBuilder.loadTexts:frsldCapabilitiesGroup.setStatus(_A)
frsldCompliance=ModuleCompliance((1,3,6,1,2,1,95,3,2,1))
frsldCompliance.setObjects(*((_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:frsldCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FrsldTxRP':FrsldTxRP,'FrsldRxRP':FrsldRxRP,'frsldMIB':frsldMIB,'frsldObjects':frsldObjects,'frsldPvcCtrlTable':frsldPvcCtrlTable,'frsldPvcCtrlEntry':frsldPvcCtrlEntry,_H:frsldPvcCtrlDlci,_I:frsldPvcCtrlTransmitRP,_J:frsldPvcCtrlReceiveRP,_P:frsldPvcCtrlStatus,_Q:frsldPvcCtrlPacketFreq,_R:frsldPvcCtrlDelayFrSize,_S:frsldPvcCtrlDelayType,_T:frsldPvcCtrlDelayTimeOut,_U:frsldPvcCtrlPurge,_V:frsldPvcCtrlDeleteOnPurge,_y:frsldPvcCtrlLastPurgeTime,'frsldSmplCtrlTable':frsldSmplCtrlTable,'frsldSmplCtrlEntry':frsldSmplCtrlEntry,_N:frsldSmplCtrlIdx,_W:frsldSmplCtrlStatus,_z:frsldSmplCtrlColPeriod,_X:frsldSmplCtrlBuckets,_A0:frsldSmplCtrlBucketsGranted,'frsldPvcDataTable':frsldPvcDataTable,'frsldPvcDataEntry':frsldPvcDataEntry,_AB:frsldPvcDataMissedPolls,_A1:frsldPvcDataFrDeliveredC,_A2:frsldPvcDataFrDeliveredE,_A3:frsldPvcDataFrOfferedC,_A4:frsldPvcDataFrOfferedE,_A5:frsldPvcDataDataDeliveredC,_A6:frsldPvcDataDataDeliveredE,_A7:frsldPvcDataDataOfferedC,_A8:frsldPvcDataDataOfferedE,_AC:frsldPvcDataHCFrDeliveredC,_AD:frsldPvcDataHCFrDeliveredE,_AE:frsldPvcDataHCFrOfferedC,_AF:frsldPvcDataHCFrOfferedE,_AG:frsldPvcDataHCDataDeliveredC,_AH:frsldPvcDataHCDataDeliveredE,_AI:frsldPvcDataHCDataOfferedC,_AJ:frsldPvcDataHCDataOfferedE,_A9:frsldPvcDataUnavailableTime,_AA:frsldPvcDataUnavailables,'frsldPvcSampleTable':frsldPvcSampleTable,'frsldPvcSampleEntry':frsldPvcSampleEntry,_w:frsldPvcSmplIdx,_AK:frsldPvcSmplDelayMin,_AL:frsldPvcSmplDelayMax,_AM:frsldPvcSmplDelayAvg,_AN:frsldPvcSmplMissedPolls,_AO:frsldPvcSmplFrDeliveredC,_AP:frsldPvcSmplFrDeliveredE,_AQ:frsldPvcSmplFrOfferedC,_AR:frsldPvcSmplFrOfferedE,_AS:frsldPvcSmplDataDeliveredC,_AT:frsldPvcSmplDataDeliveredE,_AU:frsldPvcSmplDataOfferedC,_AV:frsldPvcSmplDataOfferedE,_AW:frsldPvcSmplHCFrDeliveredC,_AX:frsldPvcSmplHCFrDeliveredE,_AY:frsldPvcSmplHCFrOfferedC,_AZ:frsldPvcSmplHCFrOfferedE,_Aa:frsldPvcSmplHCDataDeliveredC,_Ab:frsldPvcSmplHCDataDeliveredE,_Ac:frsldPvcSmplHCDataOfferedC,_Ad:frsldPvcSmplHCDataOfferedE,_Ae:frsldPvcSmplUnavailableTime,_Af:frsldPvcSmplUnavailables,_Ag:frsldPvcSmplStartTime,_Ah:frsldPvcSmplEndTime,'frsldCapabilities':frsldCapabilities,_Ai:frsldPvcCtrlWriteCaps,_Aj:frsldSmplCtrlWriteCaps,_Ak:frsldRPCaps,_Al:frsldMaxPvcCtrls,_Am:frsldNumPvcCtrls,_An:frsldMaxSmplCtrls,_Ao:frsldNumSmplCtrls,'frsldConformance':frsldConformance,'frsldMIBGroups':frsldMIBGroups,_Ap:frsldPvcReqCtrlGroup,_Au:frsldPvcPacketGroup,_Av:frsldPvcDelayCtrlGroup,_Aw:frsldPvcSampleCtrlGroup,_Aq:frsldPvcReqDataGroup,_Ax:frsldPvcDelayDataGroup,_As:frsldPvcHCFrameDataGroup,_At:frsldPvcHCOctetDataGroup,_Ay:frsldPvcSampleDelayGroup,_Az:frsldPvcSampleDataGroup,_A_:frsldPvcSampleHCFrameGroup,_B0:frsldPvcSampleHCDataGroup,_B1:frsldPvcSampleAvailGroup,_B2:frsldPvcSampleGeneralGroup,_Ar:frsldCapabilitiesGroup,'frsldMIBCompliances':frsldMIBCompliances,'frsldCompliance':frsldCompliance})