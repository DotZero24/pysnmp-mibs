_Ap='juniOspfIfBFDGroup'
_Ao='juniOspfBasicGroup'
_An='juniOspfIfBfdMultiplier'
_Am='juniOspfIfBfdMinTxInterval'
_Al='juniOspfIfBfdMinRxInterval'
_Ak='juniOspfIfBfdEnable'
_Aj='juniOspfMplsTeRtrIdIfIndex'
_Ai='juniOspfDomainId'
_Ah='juniOspfVpnRouteTag'
_Ag='juniOspfNetRangeRowStatus'
_Af='juniOspfMd5VirtIntfRowStatus'
_Ae='juniOspfMd5VirtIntfAuthKey'
_Ad='juniOspfMd5VirtIntfKeyActive'
_Ac='juniOspfMd5IntfRowStatus'
_Ab='juniOspfMd5IntfAuthKey'
_Aa='juniOspfMd5IntfKeyActive'
_AZ='juniOspfSummRowStatus'
_AY='juniOspfSummAdminStat'
_AX='juniOspfNbrBDR'
_AW='juniOspfNbrDR'
_AV='juniOspfNbrLocalIpAddr'
_AU='juniOspfVirtIfMd5AuthKeyId'
_AT='juniOspfVirtIfMd5AuthKey'
_AS='juniOspfAreaTeCapable'
_AR='juniOspfAreaType'
_AQ='juniOspfIfMd5AuthKeyId'
_AP='juniOspfIfMd5AuthKey'
_AO='juniOspfIfAdjNbrCount'
_AN='juniOspfIfNbrCount'
_AM='juniOspfIfPassiveFlag'
_AL='juniOspfIfMask'
_AK='juniOspfIfCost'
_AJ='juniOspfNbrEntry'
_AI='juniOspfVirtIfEntry'
_AH='juniOspfIfBFDEntry'
_AG='juniOspfIfEntry'
_AF='juniOspfAreaEntry'
_AE='deprecated'
_AD='TruthValue'
_AC='ospfIfIpAddress'
_AB='ospfAddressLessIf'
_AA='juniOspfBasicGroup2'
_A9='obsolete'
_A8='juniOspfOperState'
_A7='juniOspfAllocFailPkt'
_A6='juniOspfAllocFailCirc'
_A5='juniOspfAllocFailDbPkt'
_A4='juniOspfAllocFailAck'
_A3='juniOspfAllocFailRtx'
_A2='juniOspfAllocFailDbRequest'
_A1='juniOspfAllocFailLsd'
_A0='juniOspfAllocFailLsa'
_z='juniOspfAllocFailNbr'
_y='juniOspfCsumErrPkts'
_x='juniOspfTotalSent'
_w='juniOspfErrPktsSent'
_v='juniOspfLsAckPktsSent'
_u='juniOspfLsuPktsSent'
_t='juniOspfLsrPktsSent'
_s='juniOspfDDPktsSent'
_r='juniOspfHelloPktsSent'
_q='juniOspfLsaDiscardCnt'
_p='juniOspfTotalRcv'
_o='juniOspfLsAckPktsRcv'
_n='juniOspfLsuPktsRcv'
_m='juniOspfLsrPktsRcv'
_l='juniOspfDDPktsRcv'
_k='juniOspfHelloPktsRcv'
_j='juniOspfExtDistance'
_i='juniOspfInterDistance'
_h='juniOspfIntraDistance'
_g='juniOspfAutoVlink'
_f='juniOspfRefBw'
_e='juniOspfSpfTime'
_d='juniOspfNumActiveAreas'
_c='juniOspfSpfHoldInterval'
_b='juniOspfMaxPathSplits'
_a='juniOspfProcessId'
_Z='juniOspfNetRangeAreaId'
_Y='juniOspfNetRangeMask'
_X='juniOspfNetRangeNet'
_W='juniOspfMd5VirtIntfKeyId'
_V='juniOspfMd5VirtIntfNeighbor'
_U='juniOspfMd5VirtIntfAreaId'
_T='juniOspfMd5IntfKeyId'
_S='juniOspfSummAggMask'
_R='juniOspfSummAggNet'
_Q='OSPF-MIB'
_P='juniOspfNetRangeGroup'
_O='juniOspfMd5VirtIntfGroup'
_N='juniOspfMd5IntfGroup'
_M='juniOspfSummImportGroup'
_L='juniOspfNbrGroup'
_K='juniOspfVirtIfGroup'
_J='juniOspfIfGroup'
_I='juniOspfAreaGroup'
_H='Unsigned32'
_G='OctetString'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='Juniper-OSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ospfAddressLessIf,ospfAreaEntry,ospfIfEntry,ospfIfIpAddress,ospfNbrEntry,ospfVirtIfEntry=mibBuilder.importSymbols(_Q,_AB,'ospfAreaEntry','ospfIfEntry',_AC,'ospfNbrEntry','ospfVirtIfEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_AD)
juniOspfMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,14))
if mibBuilder.loadTexts:juniOspfMIB.setRevisions(('2002-09-16 21:44','2002-04-05 21:20','2000-05-23 00:00','1999-09-28 00:00'))
_JuniOspfObjects_ObjectIdentity=ObjectIdentity
juniOspfObjects=_JuniOspfObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,14,1))
_JuniOspfGeneralGroup_ObjectIdentity=ObjectIdentity
juniOspfGeneralGroup=_JuniOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,14,1,1))
class _JuniOspfProcessId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniOspfProcessId_Type.__name__=_E
_JuniOspfProcessId_Object=MibScalar
juniOspfProcessId=_JuniOspfProcessId_Object((1,3,6,1,4,1,4874,2,2,14,1,1,1),_JuniOspfProcessId_Type())
juniOspfProcessId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfProcessId.setStatus(_B)
class _JuniOspfMaxPathSplits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_JuniOspfMaxPathSplits_Type.__name__=_E
_JuniOspfMaxPathSplits_Object=MibScalar
juniOspfMaxPathSplits=_JuniOspfMaxPathSplits_Object((1,3,6,1,4,1,4874,2,2,14,1,1,2),_JuniOspfMaxPathSplits_Type())
juniOspfMaxPathSplits.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfMaxPathSplits.setStatus(_B)
class _JuniOspfSpfHoldInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_JuniOspfSpfHoldInterval_Type.__name__=_E
_JuniOspfSpfHoldInterval_Object=MibScalar
juniOspfSpfHoldInterval=_JuniOspfSpfHoldInterval_Object((1,3,6,1,4,1,4874,2,2,14,1,1,3),_JuniOspfSpfHoldInterval_Type())
juniOspfSpfHoldInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfSpfHoldInterval.setStatus(_B)
if mibBuilder.loadTexts:juniOspfSpfHoldInterval.setUnits('seconds')
_JuniOspfNumActiveAreas_Type=Counter32
_JuniOspfNumActiveAreas_Object=MibScalar
juniOspfNumActiveAreas=_JuniOspfNumActiveAreas_Object((1,3,6,1,4,1,4874,2,2,14,1,1,4),_JuniOspfNumActiveAreas_Type())
juniOspfNumActiveAreas.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNumActiveAreas.setStatus(_B)
_JuniOspfSpfTime_Type=Counter32
_JuniOspfSpfTime_Object=MibScalar
juniOspfSpfTime=_JuniOspfSpfTime_Object((1,3,6,1,4,1,4874,2,2,14,1,1,5),_JuniOspfSpfTime_Type())
juniOspfSpfTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfSpfTime.setStatus(_B)
class _JuniOspfRefBw_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JuniOspfRefBw_Type.__name__=_H
_JuniOspfRefBw_Object=MibScalar
juniOspfRefBw=_JuniOspfRefBw_Object((1,3,6,1,4,1,4874,2,2,14,1,1,6),_JuniOspfRefBw_Type())
juniOspfRefBw.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfRefBw.setStatus(_B)
if mibBuilder.loadTexts:juniOspfRefBw.setUnits('bits per second')
_JuniOspfAutoVlink_Type=TruthValue
_JuniOspfAutoVlink_Object=MibScalar
juniOspfAutoVlink=_JuniOspfAutoVlink_Object((1,3,6,1,4,1,4874,2,2,14,1,1,7),_JuniOspfAutoVlink_Type())
juniOspfAutoVlink.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfAutoVlink.setStatus(_B)
class _JuniOspfIntraDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniOspfIntraDistance_Type.__name__=_E
_JuniOspfIntraDistance_Object=MibScalar
juniOspfIntraDistance=_JuniOspfIntraDistance_Object((1,3,6,1,4,1,4874,2,2,14,1,1,8),_JuniOspfIntraDistance_Type())
juniOspfIntraDistance.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfIntraDistance.setStatus(_B)
class _JuniOspfInterDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniOspfInterDistance_Type.__name__=_E
_JuniOspfInterDistance_Object=MibScalar
juniOspfInterDistance=_JuniOspfInterDistance_Object((1,3,6,1,4,1,4874,2,2,14,1,1,9),_JuniOspfInterDistance_Type())
juniOspfInterDistance.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfInterDistance.setStatus(_B)
class _JuniOspfExtDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniOspfExtDistance_Type.__name__=_E
_JuniOspfExtDistance_Object=MibScalar
juniOspfExtDistance=_JuniOspfExtDistance_Object((1,3,6,1,4,1,4874,2,2,14,1,1,10),_JuniOspfExtDistance_Type())
juniOspfExtDistance.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfExtDistance.setStatus(_B)
_JuniOspfHelloPktsRcv_Type=Counter32
_JuniOspfHelloPktsRcv_Object=MibScalar
juniOspfHelloPktsRcv=_JuniOspfHelloPktsRcv_Object((1,3,6,1,4,1,4874,2,2,14,1,1,11),_JuniOspfHelloPktsRcv_Type())
juniOspfHelloPktsRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfHelloPktsRcv.setStatus(_B)
_JuniOspfDDPktsRcv_Type=Counter32
_JuniOspfDDPktsRcv_Object=MibScalar
juniOspfDDPktsRcv=_JuniOspfDDPktsRcv_Object((1,3,6,1,4,1,4874,2,2,14,1,1,12),_JuniOspfDDPktsRcv_Type())
juniOspfDDPktsRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfDDPktsRcv.setStatus(_B)
_JuniOspfLsrPktsRcv_Type=Counter32
_JuniOspfLsrPktsRcv_Object=MibScalar
juniOspfLsrPktsRcv=_JuniOspfLsrPktsRcv_Object((1,3,6,1,4,1,4874,2,2,14,1,1,13),_JuniOspfLsrPktsRcv_Type())
juniOspfLsrPktsRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsrPktsRcv.setStatus(_B)
_JuniOspfLsuPktsRcv_Type=Counter32
_JuniOspfLsuPktsRcv_Object=MibScalar
juniOspfLsuPktsRcv=_JuniOspfLsuPktsRcv_Object((1,3,6,1,4,1,4874,2,2,14,1,1,14),_JuniOspfLsuPktsRcv_Type())
juniOspfLsuPktsRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsuPktsRcv.setStatus(_B)
_JuniOspfLsAckPktsRcv_Type=Counter32
_JuniOspfLsAckPktsRcv_Object=MibScalar
juniOspfLsAckPktsRcv=_JuniOspfLsAckPktsRcv_Object((1,3,6,1,4,1,4874,2,2,14,1,1,15),_JuniOspfLsAckPktsRcv_Type())
juniOspfLsAckPktsRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsAckPktsRcv.setStatus(_B)
_JuniOspfTotalRcv_Type=Counter32
_JuniOspfTotalRcv_Object=MibScalar
juniOspfTotalRcv=_JuniOspfTotalRcv_Object((1,3,6,1,4,1,4874,2,2,14,1,1,16),_JuniOspfTotalRcv_Type())
juniOspfTotalRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfTotalRcv.setStatus(_B)
_JuniOspfLsaDiscardCnt_Type=Counter32
_JuniOspfLsaDiscardCnt_Object=MibScalar
juniOspfLsaDiscardCnt=_JuniOspfLsaDiscardCnt_Object((1,3,6,1,4,1,4874,2,2,14,1,1,17),_JuniOspfLsaDiscardCnt_Type())
juniOspfLsaDiscardCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsaDiscardCnt.setStatus(_B)
_JuniOspfHelloPktsSent_Type=Counter32
_JuniOspfHelloPktsSent_Object=MibScalar
juniOspfHelloPktsSent=_JuniOspfHelloPktsSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,18),_JuniOspfHelloPktsSent_Type())
juniOspfHelloPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfHelloPktsSent.setStatus(_B)
_JuniOspfDDPktsSent_Type=Counter32
_JuniOspfDDPktsSent_Object=MibScalar
juniOspfDDPktsSent=_JuniOspfDDPktsSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,19),_JuniOspfDDPktsSent_Type())
juniOspfDDPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfDDPktsSent.setStatus(_B)
_JuniOspfLsrPktsSent_Type=Counter32
_JuniOspfLsrPktsSent_Object=MibScalar
juniOspfLsrPktsSent=_JuniOspfLsrPktsSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,20),_JuniOspfLsrPktsSent_Type())
juniOspfLsrPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsrPktsSent.setStatus(_B)
_JuniOspfLsuPktsSent_Type=Counter32
_JuniOspfLsuPktsSent_Object=MibScalar
juniOspfLsuPktsSent=_JuniOspfLsuPktsSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,21),_JuniOspfLsuPktsSent_Type())
juniOspfLsuPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsuPktsSent.setStatus(_B)
_JuniOspfLsAckPktsSent_Type=Counter32
_JuniOspfLsAckPktsSent_Object=MibScalar
juniOspfLsAckPktsSent=_JuniOspfLsAckPktsSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,22),_JuniOspfLsAckPktsSent_Type())
juniOspfLsAckPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfLsAckPktsSent.setStatus(_B)
_JuniOspfErrPktsSent_Type=Counter32
_JuniOspfErrPktsSent_Object=MibScalar
juniOspfErrPktsSent=_JuniOspfErrPktsSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,23),_JuniOspfErrPktsSent_Type())
juniOspfErrPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfErrPktsSent.setStatus(_B)
_JuniOspfTotalSent_Type=Counter32
_JuniOspfTotalSent_Object=MibScalar
juniOspfTotalSent=_JuniOspfTotalSent_Object((1,3,6,1,4,1,4874,2,2,14,1,1,24),_JuniOspfTotalSent_Type())
juniOspfTotalSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfTotalSent.setStatus(_B)
_JuniOspfCsumErrPkts_Type=Counter32
_JuniOspfCsumErrPkts_Object=MibScalar
juniOspfCsumErrPkts=_JuniOspfCsumErrPkts_Object((1,3,6,1,4,1,4874,2,2,14,1,1,25),_JuniOspfCsumErrPkts_Type())
juniOspfCsumErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfCsumErrPkts.setStatus(_B)
_JuniOspfAllocFailNbr_Type=Counter32
_JuniOspfAllocFailNbr_Object=MibScalar
juniOspfAllocFailNbr=_JuniOspfAllocFailNbr_Object((1,3,6,1,4,1,4874,2,2,14,1,1,26),_JuniOspfAllocFailNbr_Type())
juniOspfAllocFailNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailNbr.setStatus(_B)
_JuniOspfAllocFailLsa_Type=Counter32
_JuniOspfAllocFailLsa_Object=MibScalar
juniOspfAllocFailLsa=_JuniOspfAllocFailLsa_Object((1,3,6,1,4,1,4874,2,2,14,1,1,27),_JuniOspfAllocFailLsa_Type())
juniOspfAllocFailLsa.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailLsa.setStatus(_B)
_JuniOspfAllocFailLsd_Type=Counter32
_JuniOspfAllocFailLsd_Object=MibScalar
juniOspfAllocFailLsd=_JuniOspfAllocFailLsd_Object((1,3,6,1,4,1,4874,2,2,14,1,1,28),_JuniOspfAllocFailLsd_Type())
juniOspfAllocFailLsd.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailLsd.setStatus(_B)
_JuniOspfAllocFailDbRequest_Type=Counter32
_JuniOspfAllocFailDbRequest_Object=MibScalar
juniOspfAllocFailDbRequest=_JuniOspfAllocFailDbRequest_Object((1,3,6,1,4,1,4874,2,2,14,1,1,29),_JuniOspfAllocFailDbRequest_Type())
juniOspfAllocFailDbRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailDbRequest.setStatus(_B)
_JuniOspfAllocFailRtx_Type=Counter32
_JuniOspfAllocFailRtx_Object=MibScalar
juniOspfAllocFailRtx=_JuniOspfAllocFailRtx_Object((1,3,6,1,4,1,4874,2,2,14,1,1,30),_JuniOspfAllocFailRtx_Type())
juniOspfAllocFailRtx.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailRtx.setStatus(_B)
_JuniOspfAllocFailAck_Type=Counter32
_JuniOspfAllocFailAck_Object=MibScalar
juniOspfAllocFailAck=_JuniOspfAllocFailAck_Object((1,3,6,1,4,1,4874,2,2,14,1,1,31),_JuniOspfAllocFailAck_Type())
juniOspfAllocFailAck.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailAck.setStatus(_B)
_JuniOspfAllocFailDbPkt_Type=Counter32
_JuniOspfAllocFailDbPkt_Object=MibScalar
juniOspfAllocFailDbPkt=_JuniOspfAllocFailDbPkt_Object((1,3,6,1,4,1,4874,2,2,14,1,1,32),_JuniOspfAllocFailDbPkt_Type())
juniOspfAllocFailDbPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailDbPkt.setStatus(_B)
_JuniOspfAllocFailCirc_Type=Counter32
_JuniOspfAllocFailCirc_Object=MibScalar
juniOspfAllocFailCirc=_JuniOspfAllocFailCirc_Object((1,3,6,1,4,1,4874,2,2,14,1,1,33),_JuniOspfAllocFailCirc_Type())
juniOspfAllocFailCirc.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailCirc.setStatus(_B)
_JuniOspfAllocFailPkt_Type=Counter32
_JuniOspfAllocFailPkt_Object=MibScalar
juniOspfAllocFailPkt=_JuniOspfAllocFailPkt_Object((1,3,6,1,4,1,4874,2,2,14,1,1,34),_JuniOspfAllocFailPkt_Type())
juniOspfAllocFailPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAllocFailPkt.setStatus(_B)
_JuniOspfOperState_Type=TruthValue
_JuniOspfOperState_Object=MibScalar
juniOspfOperState=_JuniOspfOperState_Object((1,3,6,1,4,1,4874,2,2,14,1,1,35),_JuniOspfOperState_Type())
juniOspfOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfOperState.setStatus(_B)
class _JuniOspfVpnRouteTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JuniOspfVpnRouteTag_Type.__name__=_H
_JuniOspfVpnRouteTag_Object=MibScalar
juniOspfVpnRouteTag=_JuniOspfVpnRouteTag_Object((1,3,6,1,4,1,4874,2,2,14,1,1,36),_JuniOspfVpnRouteTag_Type())
juniOspfVpnRouteTag.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfVpnRouteTag.setStatus(_B)
class _JuniOspfDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JuniOspfDomainId_Type.__name__=_H
_JuniOspfDomainId_Object=MibScalar
juniOspfDomainId=_JuniOspfDomainId_Object((1,3,6,1,4,1,4874,2,2,14,1,1,37),_JuniOspfDomainId_Type())
juniOspfDomainId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfDomainId.setStatus(_B)
_JuniOspfMplsTeRtrIdIfIndex_Type=InterfaceIndexOrZero
_JuniOspfMplsTeRtrIdIfIndex_Object=MibScalar
juniOspfMplsTeRtrIdIfIndex=_JuniOspfMplsTeRtrIdIfIndex_Object((1,3,6,1,4,1,4874,2,2,14,1,1,38),_JuniOspfMplsTeRtrIdIfIndex_Type())
juniOspfMplsTeRtrIdIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfMplsTeRtrIdIfIndex.setStatus(_B)
_JuniOspfAreaTable_Object=MibTable
juniOspfAreaTable=_JuniOspfAreaTable_Object((1,3,6,1,4,1,4874,2,2,14,1,2))
if mibBuilder.loadTexts:juniOspfAreaTable.setStatus(_B)
_JuniOspfAreaEntry_Object=MibTableRow
juniOspfAreaEntry=_JuniOspfAreaEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,2,1))
if mibBuilder.loadTexts:juniOspfAreaEntry.setStatus(_B)
class _JuniOspfAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transitArea',1),('stubArea',2),('nssaArea',3)))
_JuniOspfAreaType_Type.__name__=_E
_JuniOspfAreaType_Object=MibTableColumn
juniOspfAreaType=_JuniOspfAreaType_Object((1,3,6,1,4,1,4874,2,2,14,1,2,1,1),_JuniOspfAreaType_Type())
juniOspfAreaType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfAreaType.setStatus(_B)
_JuniOspfAreaTeCapable_Type=TruthValue
_JuniOspfAreaTeCapable_Object=MibTableColumn
juniOspfAreaTeCapable=_JuniOspfAreaTeCapable_Object((1,3,6,1,4,1,4874,2,2,14,1,2,1,2),_JuniOspfAreaTeCapable_Type())
juniOspfAreaTeCapable.setMaxAccess(_F)
if mibBuilder.loadTexts:juniOspfAreaTeCapable.setStatus(_B)
_JuniOspfIfTable_Object=MibTable
juniOspfIfTable=_JuniOspfIfTable_Object((1,3,6,1,4,1,4874,2,2,14,1,7))
if mibBuilder.loadTexts:juniOspfIfTable.setStatus(_B)
_JuniOspfIfEntry_Object=MibTableRow
juniOspfIfEntry=_JuniOspfIfEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1))
if mibBuilder.loadTexts:juniOspfIfEntry.setStatus(_B)
class _JuniOspfIfCost_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniOspfIfCost_Type.__name__=_E
_JuniOspfIfCost_Object=MibTableColumn
juniOspfIfCost=_JuniOspfIfCost_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,1),_JuniOspfIfCost_Type())
juniOspfIfCost.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfCost.setStatus(_B)
_JuniOspfIfMask_Type=IpAddress
_JuniOspfIfMask_Object=MibTableColumn
juniOspfIfMask=_JuniOspfIfMask_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,2),_JuniOspfIfMask_Type())
juniOspfIfMask.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfMask.setStatus(_B)
class _JuniOspfIfPassiveFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_JuniOspfIfPassiveFlag_Type.__name__=_E
_JuniOspfIfPassiveFlag_Object=MibTableColumn
juniOspfIfPassiveFlag=_JuniOspfIfPassiveFlag_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,3),_JuniOspfIfPassiveFlag_Type())
juniOspfIfPassiveFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfPassiveFlag.setStatus(_B)
_JuniOspfIfNbrCount_Type=Counter32
_JuniOspfIfNbrCount_Object=MibTableColumn
juniOspfIfNbrCount=_JuniOspfIfNbrCount_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,4),_JuniOspfIfNbrCount_Type())
juniOspfIfNbrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfIfNbrCount.setStatus(_B)
_JuniOspfIfAdjNbrCount_Type=Counter32
_JuniOspfIfAdjNbrCount_Object=MibTableColumn
juniOspfIfAdjNbrCount=_JuniOspfIfAdjNbrCount_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,5),_JuniOspfIfAdjNbrCount_Type())
juniOspfIfAdjNbrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfIfAdjNbrCount.setStatus(_B)
class _JuniOspfIfMd5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_JuniOspfIfMd5AuthKey_Type.__name__=_G
_JuniOspfIfMd5AuthKey_Object=MibTableColumn
juniOspfIfMd5AuthKey=_JuniOspfIfMd5AuthKey_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,6),_JuniOspfIfMd5AuthKey_Type())
juniOspfIfMd5AuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfMd5AuthKey.setStatus(_B)
class _JuniOspfIfMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniOspfIfMd5AuthKeyId_Type.__name__=_E
_JuniOspfIfMd5AuthKeyId_Object=MibTableColumn
juniOspfIfMd5AuthKeyId=_JuniOspfIfMd5AuthKeyId_Object((1,3,6,1,4,1,4874,2,2,14,1,7,1,7),_JuniOspfIfMd5AuthKeyId_Type())
juniOspfIfMd5AuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfMd5AuthKeyId.setStatus(_B)
_JuniOspfIfBFDTable_Object=MibTable
juniOspfIfBFDTable=_JuniOspfIfBFDTable_Object((1,3,6,1,4,1,4874,2,2,14,1,8))
if mibBuilder.loadTexts:juniOspfIfBFDTable.setStatus(_B)
_JuniOspfIfBFDEntry_Object=MibTableRow
juniOspfIfBFDEntry=_JuniOspfIfBFDEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,8,1))
if mibBuilder.loadTexts:juniOspfIfBFDEntry.setStatus(_B)
class _JuniOspfIfBfdEnable_Type(TruthValue):defaultValue=2
_JuniOspfIfBfdEnable_Type.__name__=_AD
_JuniOspfIfBfdEnable_Object=MibTableColumn
juniOspfIfBfdEnable=_JuniOspfIfBfdEnable_Object((1,3,6,1,4,1,4874,2,2,14,1,8,1,1),_JuniOspfIfBfdEnable_Type())
juniOspfIfBfdEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfBfdEnable.setStatus(_B)
class _JuniOspfIfBfdMinRxInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_JuniOspfIfBfdMinRxInterval_Type.__name__=_E
_JuniOspfIfBfdMinRxInterval_Object=MibTableColumn
juniOspfIfBfdMinRxInterval=_JuniOspfIfBfdMinRxInterval_Object((1,3,6,1,4,1,4874,2,2,14,1,8,1,2),_JuniOspfIfBfdMinRxInterval_Type())
juniOspfIfBfdMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfBfdMinRxInterval.setStatus(_B)
class _JuniOspfIfBfdMinTxInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_JuniOspfIfBfdMinTxInterval_Type.__name__=_E
_JuniOspfIfBfdMinTxInterval_Object=MibTableColumn
juniOspfIfBfdMinTxInterval=_JuniOspfIfBfdMinTxInterval_Object((1,3,6,1,4,1,4874,2,2,14,1,8,1,3),_JuniOspfIfBfdMinTxInterval_Type())
juniOspfIfBfdMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfBfdMinTxInterval.setStatus(_B)
class _JuniOspfIfBfdMultiplier_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniOspfIfBfdMultiplier_Type.__name__=_E
_JuniOspfIfBfdMultiplier_Object=MibTableColumn
juniOspfIfBfdMultiplier=_JuniOspfIfBfdMultiplier_Object((1,3,6,1,4,1,4874,2,2,14,1,8,1,4),_JuniOspfIfBfdMultiplier_Type())
juniOspfIfBfdMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfIfBfdMultiplier.setStatus(_B)
_JuniOspfVirtIfTable_Object=MibTable
juniOspfVirtIfTable=_JuniOspfVirtIfTable_Object((1,3,6,1,4,1,4874,2,2,14,1,9))
if mibBuilder.loadTexts:juniOspfVirtIfTable.setStatus(_B)
_JuniOspfVirtIfEntry_Object=MibTableRow
juniOspfVirtIfEntry=_JuniOspfVirtIfEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,9,1))
if mibBuilder.loadTexts:juniOspfVirtIfEntry.setStatus(_B)
class _JuniOspfVirtIfMd5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_JuniOspfVirtIfMd5AuthKey_Type.__name__=_G
_JuniOspfVirtIfMd5AuthKey_Object=MibTableColumn
juniOspfVirtIfMd5AuthKey=_JuniOspfVirtIfMd5AuthKey_Object((1,3,6,1,4,1,4874,2,2,14,1,9,1,1),_JuniOspfVirtIfMd5AuthKey_Type())
juniOspfVirtIfMd5AuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfVirtIfMd5AuthKey.setStatus(_B)
class _JuniOspfVirtIfMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniOspfVirtIfMd5AuthKeyId_Type.__name__=_E
_JuniOspfVirtIfMd5AuthKeyId_Object=MibTableColumn
juniOspfVirtIfMd5AuthKeyId=_JuniOspfVirtIfMd5AuthKeyId_Object((1,3,6,1,4,1,4874,2,2,14,1,9,1,2),_JuniOspfVirtIfMd5AuthKeyId_Type())
juniOspfVirtIfMd5AuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfVirtIfMd5AuthKeyId.setStatus(_B)
_JuniOspfNbrTable_Object=MibTable
juniOspfNbrTable=_JuniOspfNbrTable_Object((1,3,6,1,4,1,4874,2,2,14,1,10))
if mibBuilder.loadTexts:juniOspfNbrTable.setStatus(_B)
_JuniOspfNbrEntry_Object=MibTableRow
juniOspfNbrEntry=_JuniOspfNbrEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,10,1))
if mibBuilder.loadTexts:juniOspfNbrEntry.setStatus(_B)
_JuniOspfNbrLocalIpAddr_Type=IpAddress
_JuniOspfNbrLocalIpAddr_Object=MibTableColumn
juniOspfNbrLocalIpAddr=_JuniOspfNbrLocalIpAddr_Object((1,3,6,1,4,1,4874,2,2,14,1,10,1,1),_JuniOspfNbrLocalIpAddr_Type())
juniOspfNbrLocalIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNbrLocalIpAddr.setStatus(_B)
_JuniOspfNbrDR_Type=IpAddress
_JuniOspfNbrDR_Object=MibTableColumn
juniOspfNbrDR=_JuniOspfNbrDR_Object((1,3,6,1,4,1,4874,2,2,14,1,10,1,2),_JuniOspfNbrDR_Type())
juniOspfNbrDR.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNbrDR.setStatus(_B)
_JuniOspfNbrBDR_Type=IpAddress
_JuniOspfNbrBDR_Object=MibTableColumn
juniOspfNbrBDR=_JuniOspfNbrBDR_Object((1,3,6,1,4,1,4874,2,2,14,1,10,1,3),_JuniOspfNbrBDR_Type())
juniOspfNbrBDR.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNbrBDR.setStatus(_B)
_JuniOspfSummImportTable_Object=MibTable
juniOspfSummImportTable=_JuniOspfSummImportTable_Object((1,3,6,1,4,1,4874,2,2,14,1,15))
if mibBuilder.loadTexts:juniOspfSummImportTable.setStatus(_B)
_JuniOspfSummImportEntry_Object=MibTableRow
juniOspfSummImportEntry=_JuniOspfSummImportEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,15,1))
juniOspfSummImportEntry.setIndexNames((0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:juniOspfSummImportEntry.setStatus(_B)
_JuniOspfSummAggNet_Type=IpAddress
_JuniOspfSummAggNet_Object=MibTableColumn
juniOspfSummAggNet=_JuniOspfSummAggNet_Object((1,3,6,1,4,1,4874,2,2,14,1,15,1,1),_JuniOspfSummAggNet_Type())
juniOspfSummAggNet.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfSummAggNet.setStatus(_B)
_JuniOspfSummAggMask_Type=IpAddress
_JuniOspfSummAggMask_Object=MibTableColumn
juniOspfSummAggMask=_JuniOspfSummAggMask_Object((1,3,6,1,4,1,4874,2,2,14,1,15,1,2),_JuniOspfSummAggMask_Type())
juniOspfSummAggMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfSummAggMask.setStatus(_B)
class _JuniOspfSummAdminStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_JuniOspfSummAdminStat_Type.__name__=_E
_JuniOspfSummAdminStat_Object=MibTableColumn
juniOspfSummAdminStat=_JuniOspfSummAdminStat_Object((1,3,6,1,4,1,4874,2,2,14,1,15,1,3),_JuniOspfSummAdminStat_Type())
juniOspfSummAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfSummAdminStat.setStatus(_B)
_JuniOspfSummRowStatus_Type=RowStatus
_JuniOspfSummRowStatus_Object=MibTableColumn
juniOspfSummRowStatus=_JuniOspfSummRowStatus_Object((1,3,6,1,4,1,4874,2,2,14,1,15,1,4),_JuniOspfSummRowStatus_Type())
juniOspfSummRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfSummRowStatus.setStatus(_B)
_JuniOspfMd5IntfTable_Object=MibTable
juniOspfMd5IntfTable=_JuniOspfMd5IntfTable_Object((1,3,6,1,4,1,4874,2,2,14,1,16))
if mibBuilder.loadTexts:juniOspfMd5IntfTable.setStatus(_B)
_JuniOspfMd5IntfEntry_Object=MibTableRow
juniOspfMd5IntfEntry=_JuniOspfMd5IntfEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,16,1))
juniOspfMd5IntfEntry.setIndexNames((0,_Q,_AC),(0,_Q,_AB),(0,_A,_T))
if mibBuilder.loadTexts:juniOspfMd5IntfEntry.setStatus(_B)
class _JuniOspfMd5IntfKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniOspfMd5IntfKeyId_Type.__name__=_E
_JuniOspfMd5IntfKeyId_Object=MibTableColumn
juniOspfMd5IntfKeyId=_JuniOspfMd5IntfKeyId_Object((1,3,6,1,4,1,4874,2,2,14,1,16,1,1),_JuniOspfMd5IntfKeyId_Type())
juniOspfMd5IntfKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfMd5IntfKeyId.setStatus(_B)
_JuniOspfMd5IntfKeyActive_Type=TruthValue
_JuniOspfMd5IntfKeyActive_Object=MibTableColumn
juniOspfMd5IntfKeyActive=_JuniOspfMd5IntfKeyActive_Object((1,3,6,1,4,1,4874,2,2,14,1,16,1,2),_JuniOspfMd5IntfKeyActive_Type())
juniOspfMd5IntfKeyActive.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfMd5IntfKeyActive.setStatus(_AE)
class _JuniOspfMd5IntfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_JuniOspfMd5IntfAuthKey_Type.__name__=_G
_JuniOspfMd5IntfAuthKey_Object=MibTableColumn
juniOspfMd5IntfAuthKey=_JuniOspfMd5IntfAuthKey_Object((1,3,6,1,4,1,4874,2,2,14,1,16,1,3),_JuniOspfMd5IntfAuthKey_Type())
juniOspfMd5IntfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfMd5IntfAuthKey.setStatus(_B)
_JuniOspfMd5IntfRowStatus_Type=RowStatus
_JuniOspfMd5IntfRowStatus_Object=MibTableColumn
juniOspfMd5IntfRowStatus=_JuniOspfMd5IntfRowStatus_Object((1,3,6,1,4,1,4874,2,2,14,1,16,1,4),_JuniOspfMd5IntfRowStatus_Type())
juniOspfMd5IntfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfMd5IntfRowStatus.setStatus(_B)
_JuniOspfMd5VirtIntfTable_Object=MibTable
juniOspfMd5VirtIntfTable=_JuniOspfMd5VirtIntfTable_Object((1,3,6,1,4,1,4874,2,2,14,1,17))
if mibBuilder.loadTexts:juniOspfMd5VirtIntfTable.setStatus(_B)
_JuniOspfMd5VirtIntfEntry_Object=MibTableRow
juniOspfMd5VirtIntfEntry=_JuniOspfMd5VirtIntfEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1))
juniOspfMd5VirtIntfEntry.setIndexNames((0,_A,_U),(0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:juniOspfMd5VirtIntfEntry.setStatus(_B)
_JuniOspfMd5VirtIntfAreaId_Type=IpAddress
_JuniOspfMd5VirtIntfAreaId_Object=MibTableColumn
juniOspfMd5VirtIntfAreaId=_JuniOspfMd5VirtIntfAreaId_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1,1),_JuniOspfMd5VirtIntfAreaId_Type())
juniOspfMd5VirtIntfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfMd5VirtIntfAreaId.setStatus(_B)
_JuniOspfMd5VirtIntfNeighbor_Type=IpAddress
_JuniOspfMd5VirtIntfNeighbor_Object=MibTableColumn
juniOspfMd5VirtIntfNeighbor=_JuniOspfMd5VirtIntfNeighbor_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1,2),_JuniOspfMd5VirtIntfNeighbor_Type())
juniOspfMd5VirtIntfNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfMd5VirtIntfNeighbor.setStatus(_B)
class _JuniOspfMd5VirtIntfKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniOspfMd5VirtIntfKeyId_Type.__name__=_E
_JuniOspfMd5VirtIntfKeyId_Object=MibTableColumn
juniOspfMd5VirtIntfKeyId=_JuniOspfMd5VirtIntfKeyId_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1,3),_JuniOspfMd5VirtIntfKeyId_Type())
juniOspfMd5VirtIntfKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfMd5VirtIntfKeyId.setStatus(_B)
_JuniOspfMd5VirtIntfKeyActive_Type=TruthValue
_JuniOspfMd5VirtIntfKeyActive_Object=MibTableColumn
juniOspfMd5VirtIntfKeyActive=_JuniOspfMd5VirtIntfKeyActive_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1,4),_JuniOspfMd5VirtIntfKeyActive_Type())
juniOspfMd5VirtIntfKeyActive.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfMd5VirtIntfKeyActive.setStatus(_AE)
class _JuniOspfMd5VirtIntfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_JuniOspfMd5VirtIntfAuthKey_Type.__name__=_G
_JuniOspfMd5VirtIntfAuthKey_Object=MibTableColumn
juniOspfMd5VirtIntfAuthKey=_JuniOspfMd5VirtIntfAuthKey_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1,5),_JuniOspfMd5VirtIntfAuthKey_Type())
juniOspfMd5VirtIntfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfMd5VirtIntfAuthKey.setStatus(_B)
_JuniOspfMd5VirtIntfRowStatus_Type=RowStatus
_JuniOspfMd5VirtIntfRowStatus_Object=MibTableColumn
juniOspfMd5VirtIntfRowStatus=_JuniOspfMd5VirtIntfRowStatus_Object((1,3,6,1,4,1,4874,2,2,14,1,17,1,6),_JuniOspfMd5VirtIntfRowStatus_Type())
juniOspfMd5VirtIntfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfMd5VirtIntfRowStatus.setStatus(_B)
_JuniOspfNetworkRangeTable_Object=MibTable
juniOspfNetworkRangeTable=_JuniOspfNetworkRangeTable_Object((1,3,6,1,4,1,4874,2,2,14,1,18))
if mibBuilder.loadTexts:juniOspfNetworkRangeTable.setStatus(_B)
_JuniOspfNetworkRangeEntry_Object=MibTableRow
juniOspfNetworkRangeEntry=_JuniOspfNetworkRangeEntry_Object((1,3,6,1,4,1,4874,2,2,14,1,18,1))
juniOspfNetworkRangeEntry.setIndexNames((0,_A,_X),(0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:juniOspfNetworkRangeEntry.setStatus(_B)
_JuniOspfNetRangeNet_Type=IpAddress
_JuniOspfNetRangeNet_Object=MibTableColumn
juniOspfNetRangeNet=_JuniOspfNetRangeNet_Object((1,3,6,1,4,1,4874,2,2,14,1,18,1,1),_JuniOspfNetRangeNet_Type())
juniOspfNetRangeNet.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNetRangeNet.setStatus(_B)
_JuniOspfNetRangeMask_Type=IpAddress
_JuniOspfNetRangeMask_Object=MibTableColumn
juniOspfNetRangeMask=_JuniOspfNetRangeMask_Object((1,3,6,1,4,1,4874,2,2,14,1,18,1,2),_JuniOspfNetRangeMask_Type())
juniOspfNetRangeMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNetRangeMask.setStatus(_B)
_JuniOspfNetRangeAreaId_Type=IpAddress
_JuniOspfNetRangeAreaId_Object=MibTableColumn
juniOspfNetRangeAreaId=_JuniOspfNetRangeAreaId_Object((1,3,6,1,4,1,4874,2,2,14,1,18,1,3),_JuniOspfNetRangeAreaId_Type())
juniOspfNetRangeAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniOspfNetRangeAreaId.setStatus(_B)
_JuniOspfNetRangeRowStatus_Type=RowStatus
_JuniOspfNetRangeRowStatus_Object=MibTableColumn
juniOspfNetRangeRowStatus=_JuniOspfNetRangeRowStatus_Object((1,3,6,1,4,1,4874,2,2,14,1,18,1,4),_JuniOspfNetRangeRowStatus_Type())
juniOspfNetRangeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniOspfNetRangeRowStatus.setStatus(_B)
_JuniOspfConformance_ObjectIdentity=ObjectIdentity
juniOspfConformance=_JuniOspfConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,14,4))
_JuniOspfCompliances_ObjectIdentity=ObjectIdentity
juniOspfCompliances=_JuniOspfCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,14,4,1))
_JuniOspfGroups_ObjectIdentity=ObjectIdentity
juniOspfGroups=_JuniOspfGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,14,4,2))
ospfAreaEntry.registerAugmentions((_A,_AF))
juniOspfAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_A,_AG))
juniOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_A,_AH))
juniOspfIfBFDEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_A,_AI))
juniOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions((_A,_AJ))
juniOspfNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
juniOspfBasicGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,1))
juniOspfBasicGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:juniOspfBasicGroup.setStatus(_A9)
juniOspfIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,2))
juniOspfIfGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:juniOspfIfGroup.setStatus(_B)
juniOspfAreaGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,3))
juniOspfAreaGroup.setObjects(*((_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:juniOspfAreaGroup.setStatus(_B)
juniOspfVirtIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,4))
juniOspfVirtIfGroup.setObjects(*((_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:juniOspfVirtIfGroup.setStatus(_B)
juniOspfNbrGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,5))
juniOspfNbrGroup.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:juniOspfNbrGroup.setStatus(_B)
juniOspfSummImportGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,6))
juniOspfSummImportGroup.setObjects(*((_A,_R),(_A,_S),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:juniOspfSummImportGroup.setStatus(_B)
juniOspfMd5IntfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,7))
juniOspfMd5IntfGroup.setObjects(*((_A,_T),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:juniOspfMd5IntfGroup.setStatus(_B)
juniOspfMd5VirtIntfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,8))
juniOspfMd5VirtIntfGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:juniOspfMd5VirtIntfGroup.setStatus(_B)
juniOspfNetRangeGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,9))
juniOspfNetRangeGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_Ag)))
if mibBuilder.loadTexts:juniOspfNetRangeGroup.setStatus(_B)
juniOspfBasicGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,10))
juniOspfBasicGroup2.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:juniOspfBasicGroup2.setStatus(_B)
juniOspfIfBFDGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,14,4,2,11))
juniOspfIfBFDGroup.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An)))
if mibBuilder.loadTexts:juniOspfIfBFDGroup.setStatus(_B)
juniOspfCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,14,4,1,1))
juniOspfCompliance.setObjects(*((_A,_Ao),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:juniOspfCompliance.setStatus(_A9)
juniOspfCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,14,4,1,2))
juniOspfCompliance2.setObjects(*((_A,_AA),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:juniOspfCompliance2.setStatus(_A9)
juniOspfCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,14,4,1,3))
juniOspfCompliance3.setObjects(*((_A,_AA),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Ap)))
if mibBuilder.loadTexts:juniOspfCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniOspfMIB':juniOspfMIB,'juniOspfObjects':juniOspfObjects,'juniOspfGeneralGroup':juniOspfGeneralGroup,_a:juniOspfProcessId,_b:juniOspfMaxPathSplits,_c:juniOspfSpfHoldInterval,_d:juniOspfNumActiveAreas,_e:juniOspfSpfTime,_f:juniOspfRefBw,_g:juniOspfAutoVlink,_h:juniOspfIntraDistance,_i:juniOspfInterDistance,_j:juniOspfExtDistance,_k:juniOspfHelloPktsRcv,_l:juniOspfDDPktsRcv,_m:juniOspfLsrPktsRcv,_n:juniOspfLsuPktsRcv,_o:juniOspfLsAckPktsRcv,_p:juniOspfTotalRcv,_q:juniOspfLsaDiscardCnt,_r:juniOspfHelloPktsSent,_s:juniOspfDDPktsSent,_t:juniOspfLsrPktsSent,_u:juniOspfLsuPktsSent,_v:juniOspfLsAckPktsSent,_w:juniOspfErrPktsSent,_x:juniOspfTotalSent,_y:juniOspfCsumErrPkts,_z:juniOspfAllocFailNbr,_A0:juniOspfAllocFailLsa,_A1:juniOspfAllocFailLsd,_A2:juniOspfAllocFailDbRequest,_A3:juniOspfAllocFailRtx,_A4:juniOspfAllocFailAck,_A5:juniOspfAllocFailDbPkt,_A6:juniOspfAllocFailCirc,_A7:juniOspfAllocFailPkt,_A8:juniOspfOperState,_Ah:juniOspfVpnRouteTag,_Ai:juniOspfDomainId,_Aj:juniOspfMplsTeRtrIdIfIndex,'juniOspfAreaTable':juniOspfAreaTable,_AF:juniOspfAreaEntry,_AR:juniOspfAreaType,_AS:juniOspfAreaTeCapable,'juniOspfIfTable':juniOspfIfTable,_AG:juniOspfIfEntry,_AK:juniOspfIfCost,_AL:juniOspfIfMask,_AM:juniOspfIfPassiveFlag,_AN:juniOspfIfNbrCount,_AO:juniOspfIfAdjNbrCount,_AP:juniOspfIfMd5AuthKey,_AQ:juniOspfIfMd5AuthKeyId,'juniOspfIfBFDTable':juniOspfIfBFDTable,_AH:juniOspfIfBFDEntry,_Ak:juniOspfIfBfdEnable,_Al:juniOspfIfBfdMinRxInterval,_Am:juniOspfIfBfdMinTxInterval,_An:juniOspfIfBfdMultiplier,'juniOspfVirtIfTable':juniOspfVirtIfTable,_AI:juniOspfVirtIfEntry,_AT:juniOspfVirtIfMd5AuthKey,_AU:juniOspfVirtIfMd5AuthKeyId,'juniOspfNbrTable':juniOspfNbrTable,_AJ:juniOspfNbrEntry,_AV:juniOspfNbrLocalIpAddr,_AW:juniOspfNbrDR,_AX:juniOspfNbrBDR,'juniOspfSummImportTable':juniOspfSummImportTable,'juniOspfSummImportEntry':juniOspfSummImportEntry,_R:juniOspfSummAggNet,_S:juniOspfSummAggMask,_AY:juniOspfSummAdminStat,_AZ:juniOspfSummRowStatus,'juniOspfMd5IntfTable':juniOspfMd5IntfTable,'juniOspfMd5IntfEntry':juniOspfMd5IntfEntry,_T:juniOspfMd5IntfKeyId,_Aa:juniOspfMd5IntfKeyActive,_Ab:juniOspfMd5IntfAuthKey,_Ac:juniOspfMd5IntfRowStatus,'juniOspfMd5VirtIntfTable':juniOspfMd5VirtIntfTable,'juniOspfMd5VirtIntfEntry':juniOspfMd5VirtIntfEntry,_U:juniOspfMd5VirtIntfAreaId,_V:juniOspfMd5VirtIntfNeighbor,_W:juniOspfMd5VirtIntfKeyId,_Ad:juniOspfMd5VirtIntfKeyActive,_Ae:juniOspfMd5VirtIntfAuthKey,_Af:juniOspfMd5VirtIntfRowStatus,'juniOspfNetworkRangeTable':juniOspfNetworkRangeTable,'juniOspfNetworkRangeEntry':juniOspfNetworkRangeEntry,_X:juniOspfNetRangeNet,_Y:juniOspfNetRangeMask,_Z:juniOspfNetRangeAreaId,_Ag:juniOspfNetRangeRowStatus,'juniOspfConformance':juniOspfConformance,'juniOspfCompliances':juniOspfCompliances,'juniOspfCompliance':juniOspfCompliance,'juniOspfCompliance2':juniOspfCompliance2,'juniOspfCompliance3':juniOspfCompliance3,'juniOspfGroups':juniOspfGroups,_Ao:juniOspfBasicGroup,_J:juniOspfIfGroup,_I:juniOspfAreaGroup,_K:juniOspfVirtIfGroup,_L:juniOspfNbrGroup,_M:juniOspfSummImportGroup,_N:juniOspfMd5IntfGroup,_O:juniOspfMd5VirtIntfGroup,_P:juniOspfNetRangeGroup,_AA:juniOspfBasicGroup2,_Ap:juniOspfIfBFDGroup})