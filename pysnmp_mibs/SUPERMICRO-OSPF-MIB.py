_Ai='futOspfDynamicBulkUpdStatus'
_Ah='futOspfHotStandbyState'
_Ag='futOspfVirtNbrRestartHelperExitReason'
_Af='futOspfVirtNbrRestartHelperAge'
_Ae='futOspfVirtNbrRestartHelperStatus'
_Ad='futOspfNbrRestartHelperExitReason'
_Ac='futOspfNbrRestartHelperAge'
_Ab='futOspfNbrRestartHelperStatus'
_Aa='futOspfRestartExitReason'
_AZ='futOspfRestartInterval'
_AY='futOspfRestartStatus'
_AX='futOspfVirtIfCryptoAuthEntry'
_AW='futOspfIfCryptoAuthEntry'
_AV='futOspfVirtNbrEntry'
_AU='futOspfOpaqueInterfaceEntry'
_AT='futOspfVirtIfAuthKeyId'
_AS='futOspfVirtIfAuthNeighbor'
_AR='futOspfVirtIfAuthAreaId'
_AQ='futOspfIfAuthKeyId'
_AP='futOspfIfAuthAddressLessIf'
_AO='futOspfIfAuthIpAddress'
_AN='futOspfDistInOutRouteMapType'
_AM='futOspfDistInOutRouteMapName'
_AL='futOspfRRDRouteMask'
_AK='futOspfRRDRouteDest'
_AJ='futOspfAppInfoDbAppid'
_AI='futOspfType11LsdbRouterId'
_AH='futOspfType11LsdbLsid'
_AG='futOspfType11LsdbOpaqueType'
_AF='futOspfType9LsdbRouterId'
_AE='futOspfType9LsdbLsid'
_AD='futOspfType9LsdbOpaqueType'
_AC='futOspfType9LsdbIfIpAddress'
_AB='futOspfAsExternalAggregationAreaId'
_AA='futOspfAsExternalAggregationMask'
_A9='futOspfAsExternalAggregationNet'
_A8='futOspfAreaAggregateMask'
_A7='futOspfAreaAggregateNet'
_A6='futOspfAreaAggregateLsdbType'
_A5='futOspfAreaAggregateAreaID'
_A4='futOspfSecIpAddrMask'
_A3='futOspfSecIpAddr'
_A2='futOspfPrimAddresslessIf'
_A1='futOspfPrimIpAddr'
_A0='futOspfRouteIpNextHop'
_z='futOspfRouteIpTos'
_y='futOspfRouteIpAddrMask'
_x='futOspfRouteIpAddr'
_w='helping'
_v='notHelping'
_u='futOspfNbrAddressLessIndex'
_t='futOspfNbrIpAddr'
_s='futOspfVirtIfMD5AuthKeyId'
_r='futOspfVirtIfMD5AuthNeighbor'
_q='futOspfVirtIfMD5AuthAreaId'
_p='futOspfIfMD5AuthKeyId'
_o='futOspfIfMD5AuthAddressLessIf'
_n='futOspfIfMD5AuthIpAddress'
_m='futOspfAddressLessIf'
_l='futOspfIfIpAddress'
_k='futOspfHostTOS'
_j='futOspfHostIpAddress'
_i='futOspfAreaId'
_h='switchToRedundant'
_g='swReloadUpgrade'
_f='softwareRestart'
_e='unknown'
_d='Unsigned32'
_c='TimeTicks'
_b='ospfNbrRtrId'
_a='PositiveInteger'
_Z='BigMetric'
_Y='topologyChanged'
_X='timedOut'
_W='seconds'
_V='DisplayString'
_U='Status'
_T='delete'
_S='valid'
_R='completed'
_Q='inProgress'
_P='none'
_O='ospfRouterId'
_N='deprecated'
_M='TruthValue'
_L='OSPF-MIB'
_K='InterfaceIndex'
_J='OctetString'
_I='read-create'
_H='disabled'
_G='enabled'
_F='not-accessible'
_E='SUPERMICRO-OSPF-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_K)
AreaID,BigMetric,PositiveInteger,RouterID,Status,TOSType,ospfIfEntry,ospfNbrRtrId,ospfRouterId,ospfVirtIfEntry,ospfVirtNbrEntry=mibBuilder.importSymbols(_L,'AreaID',_Z,_a,'RouterID',_U,'TOSType','ospfIfEntry',_b,_O,'ospfVirtIfEntry','ospfVirtNbrEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_c,_d,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_V,'PhysAddress','RowStatus','TextualConvention',_M)
futospf=ModuleIdentity((1,3,6,1,4,1,10876,101,1,10))
if mibBuilder.loadTexts:futospf.setRevisions(('2012-09-05 00:00',))
_FutospfGeneralGroup_ObjectIdentity=ObjectIdentity
futospfGeneralGroup=_FutospfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,1))
class _FutOspfOverFlowState_Type(TruthValue):defaultValue=2
_FutOspfOverFlowState_Type.__name__=_M
_FutOspfOverFlowState_Object=MibScalar
futOspfOverFlowState=_FutOspfOverFlowState_Object((1,3,6,1,4,1,10876,101,1,10,1,1),_FutOspfOverFlowState_Type())
futOspfOverFlowState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfOverFlowState.setStatus(_A)
_FutOspfPktsRcvd_Type=Counter32
_FutOspfPktsRcvd_Object=MibScalar
futOspfPktsRcvd=_FutOspfPktsRcvd_Object((1,3,6,1,4,1,10876,101,1,10,1,2),_FutOspfPktsRcvd_Type())
futOspfPktsRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfPktsRcvd.setStatus(_A)
_FutOspfPktsTxed_Type=Counter32
_FutOspfPktsTxed_Object=MibScalar
futOspfPktsTxed=_FutOspfPktsTxed_Object((1,3,6,1,4,1,10876,101,1,10,1,3),_FutOspfPktsTxed_Type())
futOspfPktsTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfPktsTxed.setStatus(_A)
_FutOspfPktsDisd_Type=Counter32
_FutOspfPktsDisd_Object=MibScalar
futOspfPktsDisd=_FutOspfPktsDisd_Object((1,3,6,1,4,1,10876,101,1,10,1,4),_FutOspfPktsDisd_Type())
futOspfPktsDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfPktsDisd.setStatus(_A)
class _FutOspfRFC1583Compatibility_Type(Status):defaultValue=1
_FutOspfRFC1583Compatibility_Type.__name__=_U
_FutOspfRFC1583Compatibility_Object=MibScalar
futOspfRFC1583Compatibility=_FutOspfRFC1583Compatibility_Object((1,3,6,1,4,1,10876,101,1,10,1,5),_FutOspfRFC1583Compatibility_Type())
futOspfRFC1583Compatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRFC1583Compatibility.setStatus(_A)
class _FutOspfMaxAreas_Type(Integer32):defaultValue=4
_FutOspfMaxAreas_Type.__name__=_B
_FutOspfMaxAreas_Object=MibScalar
futOspfMaxAreas=_FutOspfMaxAreas_Object((1,3,6,1,4,1,10876,101,1,10,1,6),_FutOspfMaxAreas_Type())
futOspfMaxAreas.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMaxAreas.setStatus(_N)
class _FutOspfMaxLSAperArea_Type(Integer32):defaultValue=128
_FutOspfMaxLSAperArea_Type.__name__=_B
_FutOspfMaxLSAperArea_Object=MibScalar
futOspfMaxLSAperArea=_FutOspfMaxLSAperArea_Object((1,3,6,1,4,1,10876,101,1,10,1,7),_FutOspfMaxLSAperArea_Type())
futOspfMaxLSAperArea.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMaxLSAperArea.setStatus(_N)
class _FutOspfMaxExtLSAs_Type(Integer32):defaultValue=512
_FutOspfMaxExtLSAs_Type.__name__=_B
_FutOspfMaxExtLSAs_Object=MibScalar
futOspfMaxExtLSAs=_FutOspfMaxExtLSAs_Object((1,3,6,1,4,1,10876,101,1,10,1,8),_FutOspfMaxExtLSAs_Type())
futOspfMaxExtLSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMaxExtLSAs.setStatus(_N)
class _FutOspfMaxSelfOrgLSAs_Type(Integer32):defaultValue=128
_FutOspfMaxSelfOrgLSAs_Type.__name__=_B
_FutOspfMaxSelfOrgLSAs_Object=MibScalar
futOspfMaxSelfOrgLSAs=_FutOspfMaxSelfOrgLSAs_Object((1,3,6,1,4,1,10876,101,1,10,1,9),_FutOspfMaxSelfOrgLSAs_Type())
futOspfMaxSelfOrgLSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMaxSelfOrgLSAs.setStatus(_N)
class _FutOspfMaxRoutes_Type(Integer32):defaultValue=256
_FutOspfMaxRoutes_Type.__name__=_B
_FutOspfMaxRoutes_Object=MibScalar
futOspfMaxRoutes=_FutOspfMaxRoutes_Object((1,3,6,1,4,1,10876,101,1,10,1,10),_FutOspfMaxRoutes_Type())
futOspfMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMaxRoutes.setStatus(_N)
class _FutOspfMaxLsaSize_Type(Integer32):defaultValue=128
_FutOspfMaxLsaSize_Type.__name__=_B
_FutOspfMaxLsaSize_Object=MibScalar
futOspfMaxLsaSize=_FutOspfMaxLsaSize_Object((1,3,6,1,4,1,10876,101,1,10,1,11),_FutOspfMaxLsaSize_Type())
futOspfMaxLsaSize.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMaxLsaSize.setStatus(_N)
class _FutOspfTraceLevel_Type(Integer32):defaultValue=2048
_FutOspfTraceLevel_Type.__name__=_B
_FutOspfTraceLevel_Object=MibScalar
futOspfTraceLevel=_FutOspfTraceLevel_Object((1,3,6,1,4,1,10876,101,1,10,1,12),_FutOspfTraceLevel_Type())
futOspfTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfTraceLevel.setStatus(_A)
class _FutOspfMinLsaInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FutOspfMinLsaInterval_Type.__name__=_B
_FutOspfMinLsaInterval_Object=MibScalar
futOspfMinLsaInterval=_FutOspfMinLsaInterval_Object((1,3,6,1,4,1,10876,101,1,10,1,13),_FutOspfMinLsaInterval_Type())
futOspfMinLsaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfMinLsaInterval.setStatus(_A)
class _FutOspfABRType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardABR',1),('ciscoABR',2),('ibmABR',3)))
_FutOspfABRType_Type.__name__=_B
_FutOspfABRType_Object=MibScalar
futOspfABRType=_FutOspfABRType_Object((1,3,6,1,4,1,10876,101,1,10,1,14),_FutOspfABRType_Type())
futOspfABRType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfABRType.setStatus(_A)
class _FutOspfNssaAsbrDefRtTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfNssaAsbrDefRtTrans_Type.__name__=_B
_FutOspfNssaAsbrDefRtTrans_Object=MibScalar
futOspfNssaAsbrDefRtTrans=_FutOspfNssaAsbrDefRtTrans_Object((1,3,6,1,4,1,10876,101,1,10,1,15),_FutOspfNssaAsbrDefRtTrans_Type())
futOspfNssaAsbrDefRtTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfNssaAsbrDefRtTrans.setStatus(_A)
class _FutOspfDefaultPassiveInterface_Type(TruthValue):defaultValue=2
_FutOspfDefaultPassiveInterface_Type.__name__=_M
_FutOspfDefaultPassiveInterface_Object=MibScalar
futOspfDefaultPassiveInterface=_FutOspfDefaultPassiveInterface_Object((1,3,6,1,4,1,10876,101,1,10,1,16),_FutOspfDefaultPassiveInterface_Type())
futOspfDefaultPassiveInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfDefaultPassiveInterface.setStatus(_A)
class _FutOspfSpfHoldtime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfSpfHoldtime_Type.__name__=_B
_FutOspfSpfHoldtime_Object=MibScalar
futOspfSpfHoldtime=_FutOspfSpfHoldtime_Object((1,3,6,1,4,1,10876,101,1,10,1,17),_FutOspfSpfHoldtime_Type())
futOspfSpfHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfSpfHoldtime.setStatus(_A)
class _FutOspfSpfDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfSpfDelay_Type.__name__=_B
_FutOspfSpfDelay_Object=MibScalar
futOspfSpfDelay=_FutOspfSpfDelay_Object((1,3,6,1,4,1,10876,101,1,10,1,18),_FutOspfSpfDelay_Type())
futOspfSpfDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfSpfDelay.setStatus(_A)
class _FutOspfRestartSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('plannedOnly',2),('plannedAndUnplanned',3)))
_FutOspfRestartSupport_Type.__name__=_B
_FutOspfRestartSupport_Object=MibScalar
futOspfRestartSupport=_FutOspfRestartSupport_Object((1,3,6,1,4,1,10876,101,1,10,1,19),_FutOspfRestartSupport_Type())
futOspfRestartSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRestartSupport.setStatus(_A)
class _FutOspfRestartInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_FutOspfRestartInterval_Type.__name__=_B
_FutOspfRestartInterval_Object=MibScalar
futOspfRestartInterval=_FutOspfRestartInterval_Object((1,3,6,1,4,1,10876,101,1,10,1,20),_FutOspfRestartInterval_Type())
futOspfRestartInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRestartInterval.setStatus(_A)
class _FutOspfRestartStrictLsaChecking_Type(TruthValue):defaultValue=2
_FutOspfRestartStrictLsaChecking_Type.__name__=_M
_FutOspfRestartStrictLsaChecking_Object=MibScalar
futOspfRestartStrictLsaChecking=_FutOspfRestartStrictLsaChecking_Object((1,3,6,1,4,1,10876,101,1,10,1,21),_FutOspfRestartStrictLsaChecking_Type())
futOspfRestartStrictLsaChecking.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRestartStrictLsaChecking.setStatus(_A)
class _FutOspfRestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRestarting',1),('plannedRestart',2),('unplannedRestart',3)))
_FutOspfRestartStatus_Type.__name__=_B
_FutOspfRestartStatus_Object=MibScalar
futOspfRestartStatus=_FutOspfRestartStatus_Object((1,3,6,1,4,1,10876,101,1,10,1,22),_FutOspfRestartStatus_Type())
futOspfRestartStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRestartStatus.setStatus(_A)
_FutOspfRestartAge_Type=Unsigned32
_FutOspfRestartAge_Object=MibScalar
futOspfRestartAge=_FutOspfRestartAge_Object((1,3,6,1,4,1,10876,101,1,10,1,23),_FutOspfRestartAge_Type())
futOspfRestartAge.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRestartAge.setStatus(_A)
if mibBuilder.loadTexts:futOspfRestartAge.setUnits(_W)
class _FutOspfRestartExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_X,4),(_Y,5)))
_FutOspfRestartExitReason_Type.__name__=_B
_FutOspfRestartExitReason_Object=MibScalar
futOspfRestartExitReason=_FutOspfRestartExitReason_Object((1,3,6,1,4,1,10876,101,1,10,1,24),_FutOspfRestartExitReason_Type())
futOspfRestartExitReason.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRestartExitReason.setStatus(_A)
class _FutOspfHelperSupport_Type(Bits):namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3)))
_FutOspfHelperSupport_Type.__name__='Bits'
_FutOspfHelperSupport_Object=MibScalar
futOspfHelperSupport=_FutOspfHelperSupport_Object((1,3,6,1,4,1,10876,101,1,10,1,25),_FutOspfHelperSupport_Type())
futOspfHelperSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfHelperSupport.setStatus(_A)
class _FutOspfHelperGraceTimeLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_FutOspfHelperGraceTimeLimit_Type.__name__=_B
_FutOspfHelperGraceTimeLimit_Object=MibScalar
futOspfHelperGraceTimeLimit=_FutOspfHelperGraceTimeLimit_Object((1,3,6,1,4,1,10876,101,1,10,1,26),_FutOspfHelperGraceTimeLimit_Type())
futOspfHelperGraceTimeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfHelperGraceTimeLimit.setStatus(_A)
class _FutOspfRestartAckState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfRestartAckState_Type.__name__=_B
_FutOspfRestartAckState_Object=MibScalar
futOspfRestartAckState=_FutOspfRestartAckState_Object((1,3,6,1,4,1,10876,101,1,10,1,27),_FutOspfRestartAckState_Type())
futOspfRestartAckState.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRestartAckState.setStatus(_A)
class _FutOspfGraceLsaRetransmitCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FutOspfGraceLsaRetransmitCount_Type.__name__=_B
_FutOspfGraceLsaRetransmitCount_Object=MibScalar
futOspfGraceLsaRetransmitCount=_FutOspfGraceLsaRetransmitCount_Object((1,3,6,1,4,1,10876,101,1,10,1,28),_FutOspfGraceLsaRetransmitCount_Type())
futOspfGraceLsaRetransmitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfGraceLsaRetransmitCount.setStatus(_A)
class _FutOspfRestartReason_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3)))
_FutOspfRestartReason_Type.__name__=_B
_FutOspfRestartReason_Object=MibScalar
futOspfRestartReason=_FutOspfRestartReason_Object((1,3,6,1,4,1,10876,101,1,10,1,29),_FutOspfRestartReason_Type())
futOspfRestartReason.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRestartReason.setStatus(_A)
class _FutOspfRTStaggeringInterval_Type(TimeTicks):defaultValue=10000
_FutOspfRTStaggeringInterval_Type.__name__=_c
_FutOspfRTStaggeringInterval_Object=MibScalar
futOspfRTStaggeringInterval=_FutOspfRTStaggeringInterval_Object((1,3,6,1,4,1,10876,101,1,10,1,30),_FutOspfRTStaggeringInterval_Type())
futOspfRTStaggeringInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRTStaggeringInterval.setStatus(_A)
class _FutOspfRTStaggeringStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfRTStaggeringStatus_Type.__name__=_B
_FutOspfRTStaggeringStatus_Object=MibScalar
futOspfRTStaggeringStatus=_FutOspfRTStaggeringStatus_Object((1,3,6,1,4,1,10876,101,1,10,1,31),_FutOspfRTStaggeringStatus_Type())
futOspfRTStaggeringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRTStaggeringStatus.setStatus(_A)
class _FutOspfHotStandbyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfHotStandbyAdminStatus_Type.__name__=_B
_FutOspfHotStandbyAdminStatus_Object=MibScalar
futOspfHotStandbyAdminStatus=_FutOspfHotStandbyAdminStatus_Object((1,3,6,1,4,1,10876,101,1,10,1,32),_FutOspfHotStandbyAdminStatus_Type())
futOspfHotStandbyAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfHotStandbyAdminStatus.setStatus(_A)
class _FutOspfHotStandbyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FutOspfHotStandbyState_Type.__name__=_B
_FutOspfHotStandbyState_Object=MibScalar
futOspfHotStandbyState=_FutOspfHotStandbyState_Object((1,3,6,1,4,1,10876,101,1,10,1,33),_FutOspfHotStandbyState_Type())
futOspfHotStandbyState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfHotStandbyState.setStatus(_A)
class _FutOspfDynamicBulkUpdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),(_Q,2),(_R,3),('aborted',4)))
_FutOspfDynamicBulkUpdStatus_Type.__name__=_B
_FutOspfDynamicBulkUpdStatus_Object=MibScalar
futOspfDynamicBulkUpdStatus=_FutOspfDynamicBulkUpdStatus_Object((1,3,6,1,4,1,10876,101,1,10,1,34),_FutOspfDynamicBulkUpdStatus_Type())
futOspfDynamicBulkUpdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfDynamicBulkUpdStatus.setStatus(_A)
_FutOspfStanbyHelloSyncCount_Type=Counter32
_FutOspfStanbyHelloSyncCount_Object=MibScalar
futOspfStanbyHelloSyncCount=_FutOspfStanbyHelloSyncCount_Object((1,3,6,1,4,1,10876,101,1,10,1,35),_FutOspfStanbyHelloSyncCount_Type())
futOspfStanbyHelloSyncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfStanbyHelloSyncCount.setStatus(_A)
_FutOspfStanbyLsaSyncCount_Type=Counter32
_FutOspfStanbyLsaSyncCount_Object=MibScalar
futOspfStanbyLsaSyncCount=_FutOspfStanbyLsaSyncCount_Object((1,3,6,1,4,1,10876,101,1,10,1,36),_FutOspfStanbyLsaSyncCount_Type())
futOspfStanbyLsaSyncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfStanbyLsaSyncCount.setStatus(_A)
_FutOspfExtTraceLevel_Type=Integer32
_FutOspfExtTraceLevel_Object=MibScalar
futOspfExtTraceLevel=_FutOspfExtTraceLevel_Object((1,3,6,1,4,1,10876,101,1,10,1,37),_FutOspfExtTraceLevel_Type())
futOspfExtTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfExtTraceLevel.setStatus(_A)
class _FutospfRouterIdPermanence_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_FutospfRouterIdPermanence_Type.__name__=_B
_FutospfRouterIdPermanence_Object=MibScalar
futospfRouterIdPermanence=_FutospfRouterIdPermanence_Object((1,3,6,1,4,1,10876,101,1,10,1,38),_FutospfRouterIdPermanence_Type())
futospfRouterIdPermanence.setMaxAccess(_C)
if mibBuilder.loadTexts:futospfRouterIdPermanence.setStatus(_A)
class _FutOspfBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfBfdStatus_Type.__name__=_B
_FutOspfBfdStatus_Object=MibScalar
futOspfBfdStatus=_FutOspfBfdStatus_Object((1,3,6,1,4,1,10876,101,1,10,1,39),_FutOspfBfdStatus_Type())
futOspfBfdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBfdStatus.setStatus(_A)
class _FutOspfBfdAllIfState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfBfdAllIfState_Type.__name__=_B
_FutOspfBfdAllIfState_Object=MibScalar
futOspfBfdAllIfState=_FutOspfBfdAllIfState_Object((1,3,6,1,4,1,10876,101,1,10,1,40),_FutOspfBfdAllIfState_Type())
futOspfBfdAllIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBfdAllIfState.setStatus(_A)
_FutOspfAreaTable_Object=MibTable
futOspfAreaTable=_FutOspfAreaTable_Object((1,3,6,1,4,1,10876,101,1,10,2))
if mibBuilder.loadTexts:futOspfAreaTable.setStatus(_A)
_FutOspfAreaEntry_Object=MibTableRow
futOspfAreaEntry=_FutOspfAreaEntry_Object((1,3,6,1,4,1,10876,101,1,10,2,1))
futOspfAreaEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:futOspfAreaEntry.setStatus(_A)
_FutOspfAreaId_Type=AreaID
_FutOspfAreaId_Object=MibTableColumn
futOspfAreaId=_FutOspfAreaId_Object((1,3,6,1,4,1,10876,101,1,10,2,1,1),_FutOspfAreaId_Type())
futOspfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAreaId.setStatus(_A)
_FutOspfAreaIfCount_Type=Gauge32
_FutOspfAreaIfCount_Object=MibTableColumn
futOspfAreaIfCount=_FutOspfAreaIfCount_Object((1,3,6,1,4,1,10876,101,1,10,2,1,2),_FutOspfAreaIfCount_Type())
futOspfAreaIfCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAreaIfCount.setStatus(_A)
_FutOspfAreaNetCount_Type=Gauge32
_FutOspfAreaNetCount_Object=MibTableColumn
futOspfAreaNetCount=_FutOspfAreaNetCount_Object((1,3,6,1,4,1,10876,101,1,10,2,1,3),_FutOspfAreaNetCount_Type())
futOspfAreaNetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAreaNetCount.setStatus(_A)
_FutOspfAreaRtrCount_Type=Gauge32
_FutOspfAreaRtrCount_Object=MibTableColumn
futOspfAreaRtrCount=_FutOspfAreaRtrCount_Object((1,3,6,1,4,1,10876,101,1,10,2,1,4),_FutOspfAreaRtrCount_Type())
futOspfAreaRtrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAreaRtrCount.setStatus(_A)
class _FutOspfAreaNSSATranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_FutOspfAreaNSSATranslatorRole_Type.__name__=_B
_FutOspfAreaNSSATranslatorRole_Object=MibTableColumn
futOspfAreaNSSATranslatorRole=_FutOspfAreaNSSATranslatorRole_Object((1,3,6,1,4,1,10876,101,1,10,2,1,5),_FutOspfAreaNSSATranslatorRole_Type())
futOspfAreaNSSATranslatorRole.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAreaNSSATranslatorRole.setStatus(_A)
class _FutOspfAreaNSSATranslatorState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('elected',2),(_H,3)))
_FutOspfAreaNSSATranslatorState_Type.__name__=_B
_FutOspfAreaNSSATranslatorState_Object=MibTableColumn
futOspfAreaNSSATranslatorState=_FutOspfAreaNSSATranslatorState_Object((1,3,6,1,4,1,10876,101,1,10,2,1,6),_FutOspfAreaNSSATranslatorState_Type())
futOspfAreaNSSATranslatorState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAreaNSSATranslatorState.setStatus(_A)
class _FutOspfAreaNSSATranslatorStabilityInterval_Type(PositiveInteger):defaultValue=40
_FutOspfAreaNSSATranslatorStabilityInterval_Type.__name__=_a
_FutOspfAreaNSSATranslatorStabilityInterval_Object=MibTableColumn
futOspfAreaNSSATranslatorStabilityInterval=_FutOspfAreaNSSATranslatorStabilityInterval_Object((1,3,6,1,4,1,10876,101,1,10,2,1,7),_FutOspfAreaNSSATranslatorStabilityInterval_Type())
futOspfAreaNSSATranslatorStabilityInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAreaNSSATranslatorStabilityInterval.setStatus(_A)
_FutOspfAreaNSSATranslatorEvents_Type=Counter32
_FutOspfAreaNSSATranslatorEvents_Object=MibTableColumn
futOspfAreaNSSATranslatorEvents=_FutOspfAreaNSSATranslatorEvents_Object((1,3,6,1,4,1,10876,101,1,10,2,1,8),_FutOspfAreaNSSATranslatorEvents_Type())
futOspfAreaNSSATranslatorEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAreaNSSATranslatorEvents.setStatus(_A)
class _FutOspfAreaDfInfOriginate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfAreaDfInfOriginate_Type.__name__=_B
_FutOspfAreaDfInfOriginate_Object=MibTableColumn
futOspfAreaDfInfOriginate=_FutOspfAreaDfInfOriginate_Object((1,3,6,1,4,1,10876,101,1,10,2,1,9),_FutOspfAreaDfInfOriginate_Type())
futOspfAreaDfInfOriginate.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAreaDfInfOriginate.setStatus(_A)
_FutOspfHostTable_Object=MibTable
futOspfHostTable=_FutOspfHostTable_Object((1,3,6,1,4,1,10876,101,1,10,3))
if mibBuilder.loadTexts:futOspfHostTable.setStatus(_A)
_FutOspfHostEntry_Object=MibTableRow
futOspfHostEntry=_FutOspfHostEntry_Object((1,3,6,1,4,1,10876,101,1,10,3,1))
futOspfHostEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:futOspfHostEntry.setStatus(_A)
_FutOspfHostIpAddress_Type=IpAddress
_FutOspfHostIpAddress_Object=MibTableColumn
futOspfHostIpAddress=_FutOspfHostIpAddress_Object((1,3,6,1,4,1,10876,101,1,10,3,1,1),_FutOspfHostIpAddress_Type())
futOspfHostIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfHostIpAddress.setStatus(_A)
_FutOspfHostTOS_Type=TOSType
_FutOspfHostTOS_Object=MibTableColumn
futOspfHostTOS=_FutOspfHostTOS_Object((1,3,6,1,4,1,10876,101,1,10,3,1,2),_FutOspfHostTOS_Type())
futOspfHostTOS.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfHostTOS.setStatus(_A)
class _FutOspfHostRouteIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfHostRouteIfIndex_Type.__name__=_B
_FutOspfHostRouteIfIndex_Object=MibTableColumn
futOspfHostRouteIfIndex=_FutOspfHostRouteIfIndex_Object((1,3,6,1,4,1,10876,101,1,10,3,1,3),_FutOspfHostRouteIfIndex_Type())
futOspfHostRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfHostRouteIfIndex.setStatus(_A)
_FutOspfIfTable_Object=MibTable
futOspfIfTable=_FutOspfIfTable_Object((1,3,6,1,4,1,10876,101,1,10,4))
if mibBuilder.loadTexts:futOspfIfTable.setStatus(_A)
_FutOspfIfEntry_Object=MibTableRow
futOspfIfEntry=_FutOspfIfEntry_Object((1,3,6,1,4,1,10876,101,1,10,4,1))
futOspfIfEntry.setIndexNames((0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:futOspfIfEntry.setStatus(_A)
_FutOspfIfIpAddress_Type=IpAddress
_FutOspfIfIpAddress_Object=MibTableColumn
futOspfIfIpAddress=_FutOspfIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,10,4,1,1),_FutOspfIfIpAddress_Type())
futOspfIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfIpAddress.setStatus(_A)
class _FutOspfAddressLessIf_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfAddressLessIf_Type.__name__=_K
_FutOspfAddressLessIf_Object=MibTableColumn
futOspfAddressLessIf=_FutOspfAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,10,4,1,2),_FutOspfAddressLessIf_Type())
futOspfAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAddressLessIf.setStatus(_A)
class _FutOspfIfOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operup',1),('operdown',2),('loopback',3),('unloop',4)))
_FutOspfIfOperState_Type.__name__=_B
_FutOspfIfOperState_Object=MibTableColumn
futOspfIfOperState=_FutOspfIfOperState_Object((1,3,6,1,4,1,10876,101,1,10,4,1,3),_FutOspfIfOperState_Type())
futOspfIfOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfOperState.setStatus(_A)
class _FutOspfIfPassive_Type(TruthValue):defaultValue=2
_FutOspfIfPassive_Type.__name__=_M
_FutOspfIfPassive_Object=MibTableColumn
futOspfIfPassive=_FutOspfIfPassive_Object((1,3,6,1,4,1,10876,101,1,10,4,1,4),_FutOspfIfPassive_Type())
futOspfIfPassive.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfPassive.setStatus(_A)
_FutOspfIfNbrCount_Type=Gauge32
_FutOspfIfNbrCount_Object=MibTableColumn
futOspfIfNbrCount=_FutOspfIfNbrCount_Object((1,3,6,1,4,1,10876,101,1,10,4,1,5),_FutOspfIfNbrCount_Type())
futOspfIfNbrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfNbrCount.setStatus(_A)
_FutOspfIfAdjCount_Type=Gauge32
_FutOspfIfAdjCount_Object=MibTableColumn
futOspfIfAdjCount=_FutOspfIfAdjCount_Object((1,3,6,1,4,1,10876,101,1,10,4,1,6),_FutOspfIfAdjCount_Type())
futOspfIfAdjCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfAdjCount.setStatus(_A)
_FutOspfIfHelloRcvd_Type=Counter32
_FutOspfIfHelloRcvd_Object=MibTableColumn
futOspfIfHelloRcvd=_FutOspfIfHelloRcvd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,7),_FutOspfIfHelloRcvd_Type())
futOspfIfHelloRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfHelloRcvd.setStatus(_A)
_FutOspfIfHelloTxed_Type=Counter32
_FutOspfIfHelloTxed_Object=MibTableColumn
futOspfIfHelloTxed=_FutOspfIfHelloTxed_Object((1,3,6,1,4,1,10876,101,1,10,4,1,8),_FutOspfIfHelloTxed_Type())
futOspfIfHelloTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfHelloTxed.setStatus(_A)
_FutOspfIfHelloDisd_Type=Counter32
_FutOspfIfHelloDisd_Object=MibTableColumn
futOspfIfHelloDisd=_FutOspfIfHelloDisd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,9),_FutOspfIfHelloDisd_Type())
futOspfIfHelloDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfHelloDisd.setStatus(_A)
_FutOspfIfDdpRcvd_Type=Counter32
_FutOspfIfDdpRcvd_Object=MibTableColumn
futOspfIfDdpRcvd=_FutOspfIfDdpRcvd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,10),_FutOspfIfDdpRcvd_Type())
futOspfIfDdpRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfDdpRcvd.setStatus(_A)
_FutOspfIfDdpTxed_Type=Counter32
_FutOspfIfDdpTxed_Object=MibTableColumn
futOspfIfDdpTxed=_FutOspfIfDdpTxed_Object((1,3,6,1,4,1,10876,101,1,10,4,1,11),_FutOspfIfDdpTxed_Type())
futOspfIfDdpTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfDdpTxed.setStatus(_A)
_FutOspfIfDdpDisd_Type=Counter32
_FutOspfIfDdpDisd_Object=MibTableColumn
futOspfIfDdpDisd=_FutOspfIfDdpDisd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,12),_FutOspfIfDdpDisd_Type())
futOspfIfDdpDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfDdpDisd.setStatus(_A)
_FutOspfIfLrqRcvd_Type=Counter32
_FutOspfIfLrqRcvd_Object=MibTableColumn
futOspfIfLrqRcvd=_FutOspfIfLrqRcvd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,13),_FutOspfIfLrqRcvd_Type())
futOspfIfLrqRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLrqRcvd.setStatus(_A)
_FutOspfIfLrqTxed_Type=Counter32
_FutOspfIfLrqTxed_Object=MibTableColumn
futOspfIfLrqTxed=_FutOspfIfLrqTxed_Object((1,3,6,1,4,1,10876,101,1,10,4,1,14),_FutOspfIfLrqTxed_Type())
futOspfIfLrqTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLrqTxed.setStatus(_A)
_FutOspfIfLrqDisd_Type=Counter32
_FutOspfIfLrqDisd_Object=MibTableColumn
futOspfIfLrqDisd=_FutOspfIfLrqDisd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,15),_FutOspfIfLrqDisd_Type())
futOspfIfLrqDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLrqDisd.setStatus(_A)
_FutOspfIfLsuRcvd_Type=Counter32
_FutOspfIfLsuRcvd_Object=MibTableColumn
futOspfIfLsuRcvd=_FutOspfIfLsuRcvd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,16),_FutOspfIfLsuRcvd_Type())
futOspfIfLsuRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLsuRcvd.setStatus(_A)
_FutOspfIfLsuTxed_Type=Counter32
_FutOspfIfLsuTxed_Object=MibTableColumn
futOspfIfLsuTxed=_FutOspfIfLsuTxed_Object((1,3,6,1,4,1,10876,101,1,10,4,1,17),_FutOspfIfLsuTxed_Type())
futOspfIfLsuTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLsuTxed.setStatus(_A)
_FutOspfIfLsuDisd_Type=Counter32
_FutOspfIfLsuDisd_Object=MibTableColumn
futOspfIfLsuDisd=_FutOspfIfLsuDisd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,18),_FutOspfIfLsuDisd_Type())
futOspfIfLsuDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLsuDisd.setStatus(_A)
_FutOspfIfLakRcvd_Type=Counter32
_FutOspfIfLakRcvd_Object=MibTableColumn
futOspfIfLakRcvd=_FutOspfIfLakRcvd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,19),_FutOspfIfLakRcvd_Type())
futOspfIfLakRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLakRcvd.setStatus(_A)
_FutOspfIfLakTxed_Type=Counter32
_FutOspfIfLakTxed_Object=MibTableColumn
futOspfIfLakTxed=_FutOspfIfLakTxed_Object((1,3,6,1,4,1,10876,101,1,10,4,1,20),_FutOspfIfLakTxed_Type())
futOspfIfLakTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLakTxed.setStatus(_A)
_FutOspfIfLakDisd_Type=Counter32
_FutOspfIfLakDisd_Object=MibTableColumn
futOspfIfLakDisd=_FutOspfIfLakDisd_Object((1,3,6,1,4,1,10876,101,1,10,4,1,21),_FutOspfIfLakDisd_Type())
futOspfIfLakDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfIfLakDisd.setStatus(_A)
class _FutOspfIfBfdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfIfBfdState_Type.__name__=_B
_FutOspfIfBfdState_Object=MibTableColumn
futOspfIfBfdState=_FutOspfIfBfdState_Object((1,3,6,1,4,1,10876,101,1,10,4,1,22),_FutOspfIfBfdState_Type())
futOspfIfBfdState.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfBfdState.setStatus(_A)
_FutOspfIfMD5AuthTable_Object=MibTable
futOspfIfMD5AuthTable=_FutOspfIfMD5AuthTable_Object((1,3,6,1,4,1,10876,101,1,10,5))
if mibBuilder.loadTexts:futOspfIfMD5AuthTable.setStatus(_A)
_FutOspfIfMD5AuthEntry_Object=MibTableRow
futOspfIfMD5AuthEntry=_FutOspfIfMD5AuthEntry_Object((1,3,6,1,4,1,10876,101,1,10,5,1))
futOspfIfMD5AuthEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:futOspfIfMD5AuthEntry.setStatus(_A)
_FutOspfIfMD5AuthIpAddress_Type=IpAddress
_FutOspfIfMD5AuthIpAddress_Object=MibTableColumn
futOspfIfMD5AuthIpAddress=_FutOspfIfMD5AuthIpAddress_Object((1,3,6,1,4,1,10876,101,1,10,5,1,1),_FutOspfIfMD5AuthIpAddress_Type())
futOspfIfMD5AuthIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfMD5AuthIpAddress.setStatus(_A)
class _FutOspfIfMD5AuthAddressLessIf_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfIfMD5AuthAddressLessIf_Type.__name__=_K
_FutOspfIfMD5AuthAddressLessIf_Object=MibTableColumn
futOspfIfMD5AuthAddressLessIf=_FutOspfIfMD5AuthAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,10,5,1,2),_FutOspfIfMD5AuthAddressLessIf_Type())
futOspfIfMD5AuthAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfMD5AuthAddressLessIf.setStatus(_A)
class _FutOspfIfMD5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspfIfMD5AuthKeyId_Type.__name__=_B
_FutOspfIfMD5AuthKeyId_Object=MibTableColumn
futOspfIfMD5AuthKeyId=_FutOspfIfMD5AuthKeyId_Object((1,3,6,1,4,1,10876,101,1,10,5,1,3),_FutOspfIfMD5AuthKeyId_Type())
futOspfIfMD5AuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfMD5AuthKeyId.setStatus(_A)
class _FutOspfIfMD5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FutOspfIfMD5AuthKey_Type.__name__=_J
_FutOspfIfMD5AuthKey_Object=MibTableColumn
futOspfIfMD5AuthKey=_FutOspfIfMD5AuthKey_Object((1,3,6,1,4,1,10876,101,1,10,5,1,4),_FutOspfIfMD5AuthKey_Type())
futOspfIfMD5AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfMD5AuthKey.setStatus(_A)
class _FutOspfIfMD5AuthKeyStartAccept_Type(Integer32):defaultValue=0
_FutOspfIfMD5AuthKeyStartAccept_Type.__name__=_B
_FutOspfIfMD5AuthKeyStartAccept_Object=MibTableColumn
futOspfIfMD5AuthKeyStartAccept=_FutOspfIfMD5AuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,10,5,1,5),_FutOspfIfMD5AuthKeyStartAccept_Type())
futOspfIfMD5AuthKeyStartAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfMD5AuthKeyStartAccept.setStatus(_A)
class _FutOspfIfMD5AuthKeyStartGenerate_Type(Integer32):defaultValue=0
_FutOspfIfMD5AuthKeyStartGenerate_Type.__name__=_B
_FutOspfIfMD5AuthKeyStartGenerate_Object=MibTableColumn
futOspfIfMD5AuthKeyStartGenerate=_FutOspfIfMD5AuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,10,5,1,6),_FutOspfIfMD5AuthKeyStartGenerate_Type())
futOspfIfMD5AuthKeyStartGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfMD5AuthKeyStartGenerate.setStatus(_A)
class _FutOspfIfMD5AuthKeyStopGenerate_Type(Integer32):defaultValue=-1
_FutOspfIfMD5AuthKeyStopGenerate_Type.__name__=_B
_FutOspfIfMD5AuthKeyStopGenerate_Object=MibTableColumn
futOspfIfMD5AuthKeyStopGenerate=_FutOspfIfMD5AuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,10,5,1,7),_FutOspfIfMD5AuthKeyStopGenerate_Type())
futOspfIfMD5AuthKeyStopGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfMD5AuthKeyStopGenerate.setStatus(_A)
class _FutOspfIfMD5AuthKeyStopAccept_Type(Integer32):defaultValue=-1
_FutOspfIfMD5AuthKeyStopAccept_Type.__name__=_B
_FutOspfIfMD5AuthKeyStopAccept_Object=MibTableColumn
futOspfIfMD5AuthKeyStopAccept=_FutOspfIfMD5AuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,10,5,1,8),_FutOspfIfMD5AuthKeyStopAccept_Type())
futOspfIfMD5AuthKeyStopAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfMD5AuthKeyStopAccept.setStatus(_A)
class _FutOspfIfMD5AuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_S,1),(_T,3)))
_FutOspfIfMD5AuthKeyStatus_Type.__name__=_B
_FutOspfIfMD5AuthKeyStatus_Object=MibTableColumn
futOspfIfMD5AuthKeyStatus=_FutOspfIfMD5AuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,10,5,1,9),_FutOspfIfMD5AuthKeyStatus_Type())
futOspfIfMD5AuthKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfMD5AuthKeyStatus.setStatus(_A)
_FutOspfVirtIfMD5AuthTable_Object=MibTable
futOspfVirtIfMD5AuthTable=_FutOspfVirtIfMD5AuthTable_Object((1,3,6,1,4,1,10876,101,1,10,6))
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthTable.setStatus(_A)
_FutOspfVirtIfMD5AuthEntry_Object=MibTableRow
futOspfVirtIfMD5AuthEntry=_FutOspfVirtIfMD5AuthEntry_Object((1,3,6,1,4,1,10876,101,1,10,6,1))
futOspfVirtIfMD5AuthEntry.setIndexNames((0,_E,_q),(0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthEntry.setStatus(_A)
_FutOspfVirtIfMD5AuthAreaId_Type=AreaID
_FutOspfVirtIfMD5AuthAreaId_Object=MibTableColumn
futOspfVirtIfMD5AuthAreaId=_FutOspfVirtIfMD5AuthAreaId_Object((1,3,6,1,4,1,10876,101,1,10,6,1,1),_FutOspfVirtIfMD5AuthAreaId_Type())
futOspfVirtIfMD5AuthAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthAreaId.setStatus(_A)
_FutOspfVirtIfMD5AuthNeighbor_Type=RouterID
_FutOspfVirtIfMD5AuthNeighbor_Object=MibTableColumn
futOspfVirtIfMD5AuthNeighbor=_FutOspfVirtIfMD5AuthNeighbor_Object((1,3,6,1,4,1,10876,101,1,10,6,1,2),_FutOspfVirtIfMD5AuthNeighbor_Type())
futOspfVirtIfMD5AuthNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthNeighbor.setStatus(_A)
class _FutOspfVirtIfMD5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspfVirtIfMD5AuthKeyId_Type.__name__=_B
_FutOspfVirtIfMD5AuthKeyId_Object=MibTableColumn
futOspfVirtIfMD5AuthKeyId=_FutOspfVirtIfMD5AuthKeyId_Object((1,3,6,1,4,1,10876,101,1,10,6,1,3),_FutOspfVirtIfMD5AuthKeyId_Type())
futOspfVirtIfMD5AuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKeyId.setStatus(_A)
class _FutOspfVirtIfMD5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FutOspfVirtIfMD5AuthKey_Type.__name__=_J
_FutOspfVirtIfMD5AuthKey_Object=MibTableColumn
futOspfVirtIfMD5AuthKey=_FutOspfVirtIfMD5AuthKey_Object((1,3,6,1,4,1,10876,101,1,10,6,1,4),_FutOspfVirtIfMD5AuthKey_Type())
futOspfVirtIfMD5AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKey.setStatus(_A)
class _FutOspfVirtIfMD5AuthKeyStartAccept_Type(Integer32):defaultValue=0
_FutOspfVirtIfMD5AuthKeyStartAccept_Type.__name__=_B
_FutOspfVirtIfMD5AuthKeyStartAccept_Object=MibTableColumn
futOspfVirtIfMD5AuthKeyStartAccept=_FutOspfVirtIfMD5AuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,10,6,1,5),_FutOspfVirtIfMD5AuthKeyStartAccept_Type())
futOspfVirtIfMD5AuthKeyStartAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKeyStartAccept.setStatus(_A)
class _FutOspfVirtIfMD5AuthKeyStartGenerate_Type(Integer32):defaultValue=0
_FutOspfVirtIfMD5AuthKeyStartGenerate_Type.__name__=_B
_FutOspfVirtIfMD5AuthKeyStartGenerate_Object=MibTableColumn
futOspfVirtIfMD5AuthKeyStartGenerate=_FutOspfVirtIfMD5AuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,10,6,1,6),_FutOspfVirtIfMD5AuthKeyStartGenerate_Type())
futOspfVirtIfMD5AuthKeyStartGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKeyStartGenerate.setStatus(_A)
class _FutOspfVirtIfMD5AuthKeyStopGenerate_Type(Integer32):defaultValue=-1
_FutOspfVirtIfMD5AuthKeyStopGenerate_Type.__name__=_B
_FutOspfVirtIfMD5AuthKeyStopGenerate_Object=MibTableColumn
futOspfVirtIfMD5AuthKeyStopGenerate=_FutOspfVirtIfMD5AuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,10,6,1,7),_FutOspfVirtIfMD5AuthKeyStopGenerate_Type())
futOspfVirtIfMD5AuthKeyStopGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKeyStopGenerate.setStatus(_A)
class _FutOspfVirtIfMD5AuthKeyStopAccept_Type(Integer32):defaultValue=-1
_FutOspfVirtIfMD5AuthKeyStopAccept_Type.__name__=_B
_FutOspfVirtIfMD5AuthKeyStopAccept_Object=MibTableColumn
futOspfVirtIfMD5AuthKeyStopAccept=_FutOspfVirtIfMD5AuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,10,6,1,8),_FutOspfVirtIfMD5AuthKeyStopAccept_Type())
futOspfVirtIfMD5AuthKeyStopAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKeyStopAccept.setStatus(_A)
class _FutOspfVirtIfMD5AuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_S,1),(_T,3)))
_FutOspfVirtIfMD5AuthKeyStatus_Type.__name__=_B
_FutOspfVirtIfMD5AuthKeyStatus_Object=MibTableColumn
futOspfVirtIfMD5AuthKeyStatus=_FutOspfVirtIfMD5AuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,10,6,1,9),_FutOspfVirtIfMD5AuthKeyStatus_Type())
futOspfVirtIfMD5AuthKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfMD5AuthKeyStatus.setStatus(_A)
_FutOspfNbrTable_Object=MibTable
futOspfNbrTable=_FutOspfNbrTable_Object((1,3,6,1,4,1,10876,101,1,10,7))
if mibBuilder.loadTexts:futOspfNbrTable.setStatus(_A)
_FutOspfNbrEntry_Object=MibTableRow
futOspfNbrEntry=_FutOspfNbrEntry_Object((1,3,6,1,4,1,10876,101,1,10,7,1))
futOspfNbrEntry.setIndexNames((0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:futOspfNbrEntry.setStatus(_A)
_FutOspfNbrIpAddr_Type=IpAddress
_FutOspfNbrIpAddr_Object=MibTableColumn
futOspfNbrIpAddr=_FutOspfNbrIpAddr_Object((1,3,6,1,4,1,10876,101,1,10,7,1,1),_FutOspfNbrIpAddr_Type())
futOspfNbrIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfNbrIpAddr.setStatus(_A)
class _FutOspfNbrAddressLessIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfNbrAddressLessIndex_Type.__name__=_K
_FutOspfNbrAddressLessIndex_Object=MibTableColumn
futOspfNbrAddressLessIndex=_FutOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,10876,101,1,10,7,1,2),_FutOspfNbrAddressLessIndex_Type())
futOspfNbrAddressLessIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfNbrAddressLessIndex.setStatus(_A)
_FutOspfNbrDBSummaryQLen_Type=Gauge32
_FutOspfNbrDBSummaryQLen_Object=MibTableColumn
futOspfNbrDBSummaryQLen=_FutOspfNbrDBSummaryQLen_Object((1,3,6,1,4,1,10876,101,1,10,7,1,3),_FutOspfNbrDBSummaryQLen_Type())
futOspfNbrDBSummaryQLen.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfNbrDBSummaryQLen.setStatus(_A)
_FutOspfNbrLSReqQLen_Type=Gauge32
_FutOspfNbrLSReqQLen_Object=MibTableColumn
futOspfNbrLSReqQLen=_FutOspfNbrLSReqQLen_Object((1,3,6,1,4,1,10876,101,1,10,7,1,4),_FutOspfNbrLSReqQLen_Type())
futOspfNbrLSReqQLen.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfNbrLSReqQLen.setStatus(_A)
class _FutOspfNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_FutOspfNbrRestartHelperStatus_Type.__name__=_B
_FutOspfNbrRestartHelperStatus_Object=MibTableColumn
futOspfNbrRestartHelperStatus=_FutOspfNbrRestartHelperStatus_Object((1,3,6,1,4,1,10876,101,1,10,7,1,5),_FutOspfNbrRestartHelperStatus_Type())
futOspfNbrRestartHelperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfNbrRestartHelperStatus.setStatus(_A)
_FutOspfNbrRestartHelperAge_Type=Unsigned32
_FutOspfNbrRestartHelperAge_Object=MibTableColumn
futOspfNbrRestartHelperAge=_FutOspfNbrRestartHelperAge_Object((1,3,6,1,4,1,10876,101,1,10,7,1,6),_FutOspfNbrRestartHelperAge_Type())
futOspfNbrRestartHelperAge.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:futOspfNbrRestartHelperAge.setUnits(_W)
class _FutOspfNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_X,4),(_Y,5)))
_FutOspfNbrRestartHelperExitReason_Type.__name__=_B
_FutOspfNbrRestartHelperExitReason_Object=MibTableColumn
futOspfNbrRestartHelperExitReason=_FutOspfNbrRestartHelperExitReason_Object((1,3,6,1,4,1,10876,101,1,10,7,1,7),_FutOspfNbrRestartHelperExitReason_Type())
futOspfNbrRestartHelperExitReason.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfNbrRestartHelperExitReason.setStatus(_A)
class _FutOspfNbrBfdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfNbrBfdState_Type.__name__=_B
_FutOspfNbrBfdState_Object=MibTableColumn
futOspfNbrBfdState=_FutOspfNbrBfdState_Object((1,3,6,1,4,1,10876,101,1,10,7,1,8),_FutOspfNbrBfdState_Type())
futOspfNbrBfdState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfNbrBfdState.setStatus(_A)
_FutOspfRoutingTable_Object=MibTable
futOspfRoutingTable=_FutOspfRoutingTable_Object((1,3,6,1,4,1,10876,101,1,10,8))
if mibBuilder.loadTexts:futOspfRoutingTable.setStatus(_A)
_FutOspfRoutingEntry_Object=MibTableRow
futOspfRoutingEntry=_FutOspfRoutingEntry_Object((1,3,6,1,4,1,10876,101,1,10,8,1))
futOspfRoutingEntry.setIndexNames((0,_E,_x),(0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:futOspfRoutingEntry.setStatus(_A)
_FutOspfRouteIpAddr_Type=IpAddress
_FutOspfRouteIpAddr_Object=MibTableColumn
futOspfRouteIpAddr=_FutOspfRouteIpAddr_Object((1,3,6,1,4,1,10876,101,1,10,8,1,1),_FutOspfRouteIpAddr_Type())
futOspfRouteIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfRouteIpAddr.setStatus(_A)
_FutOspfRouteIpAddrMask_Type=IpAddress
_FutOspfRouteIpAddrMask_Object=MibTableColumn
futOspfRouteIpAddrMask=_FutOspfRouteIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,10,8,1,2),_FutOspfRouteIpAddrMask_Type())
futOspfRouteIpAddrMask.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfRouteIpAddrMask.setStatus(_A)
_FutOspfRouteIpTos_Type=TOSType
_FutOspfRouteIpTos_Object=MibTableColumn
futOspfRouteIpTos=_FutOspfRouteIpTos_Object((1,3,6,1,4,1,10876,101,1,10,8,1,3),_FutOspfRouteIpTos_Type())
futOspfRouteIpTos.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfRouteIpTos.setStatus(_A)
_FutOspfRouteIpNextHop_Type=IpAddress
_FutOspfRouteIpNextHop_Object=MibTableColumn
futOspfRouteIpNextHop=_FutOspfRouteIpNextHop_Object((1,3,6,1,4,1,10876,101,1,10,8,1,4),_FutOspfRouteIpNextHop_Type())
futOspfRouteIpNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfRouteIpNextHop.setStatus(_A)
class _FutOspfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('intraArea',1),('interArea',2),('type1External',3),('type2External',4)))
_FutOspfRouteType_Type.__name__=_B
_FutOspfRouteType_Object=MibTableColumn
futOspfRouteType=_FutOspfRouteType_Object((1,3,6,1,4,1,10876,101,1,10,8,1,5),_FutOspfRouteType_Type())
futOspfRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRouteType.setStatus(_A)
_FutOspfRouteAreaId_Type=IpAddress
_FutOspfRouteAreaId_Object=MibTableColumn
futOspfRouteAreaId=_FutOspfRouteAreaId_Object((1,3,6,1,4,1,10876,101,1,10,8,1,6),_FutOspfRouteAreaId_Type())
futOspfRouteAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRouteAreaId.setStatus(_A)
_FutOspfRouteCost_Type=BigMetric
_FutOspfRouteCost_Object=MibTableColumn
futOspfRouteCost=_FutOspfRouteCost_Object((1,3,6,1,4,1,10876,101,1,10,8,1,7),_FutOspfRouteCost_Type())
futOspfRouteCost.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRouteCost.setStatus(_A)
_FutOspfRouteType2Cost_Type=BigMetric
_FutOspfRouteType2Cost_Object=MibTableColumn
futOspfRouteType2Cost=_FutOspfRouteType2Cost_Object((1,3,6,1,4,1,10876,101,1,10,8,1,8),_FutOspfRouteType2Cost_Type())
futOspfRouteType2Cost.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRouteType2Cost.setStatus(_A)
_FutOspfRouteInterfaceIndex_Type=InterfaceIndex
_FutOspfRouteInterfaceIndex_Object=MibTableColumn
futOspfRouteInterfaceIndex=_FutOspfRouteInterfaceIndex_Object((1,3,6,1,4,1,10876,101,1,10,8,1,9),_FutOspfRouteInterfaceIndex_Type())
futOspfRouteInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfRouteInterfaceIndex.setStatus(_A)
_FutOspfSecIfTable_Object=MibTable
futOspfSecIfTable=_FutOspfSecIfTable_Object((1,3,6,1,4,1,10876,101,1,10,9))
if mibBuilder.loadTexts:futOspfSecIfTable.setStatus(_A)
_FutOspfSecIfEntry_Object=MibTableRow
futOspfSecIfEntry=_FutOspfSecIfEntry_Object((1,3,6,1,4,1,10876,101,1,10,9,1))
futOspfSecIfEntry.setIndexNames((0,_E,_A1),(0,_E,_A2),(0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:futOspfSecIfEntry.setStatus(_A)
_FutOspfPrimIpAddr_Type=IpAddress
_FutOspfPrimIpAddr_Object=MibTableColumn
futOspfPrimIpAddr=_FutOspfPrimIpAddr_Object((1,3,6,1,4,1,10876,101,1,10,9,1,1),_FutOspfPrimIpAddr_Type())
futOspfPrimIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfPrimIpAddr.setStatus(_A)
class _FutOspfPrimAddresslessIf_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfPrimAddresslessIf_Type.__name__=_K
_FutOspfPrimAddresslessIf_Object=MibTableColumn
futOspfPrimAddresslessIf=_FutOspfPrimAddresslessIf_Object((1,3,6,1,4,1,10876,101,1,10,9,1,2),_FutOspfPrimAddresslessIf_Type())
futOspfPrimAddresslessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfPrimAddresslessIf.setStatus(_A)
_FutOspfSecIpAddr_Type=IpAddress
_FutOspfSecIpAddr_Object=MibTableColumn
futOspfSecIpAddr=_FutOspfSecIpAddr_Object((1,3,6,1,4,1,10876,101,1,10,9,1,3),_FutOspfSecIpAddr_Type())
futOspfSecIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfSecIpAddr.setStatus(_A)
_FutOspfSecIpAddrMask_Type=IpAddress
_FutOspfSecIpAddrMask_Object=MibTableColumn
futOspfSecIpAddrMask=_FutOspfSecIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,10,9,1,4),_FutOspfSecIpAddrMask_Type())
futOspfSecIpAddrMask.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfSecIpAddrMask.setStatus(_A)
_FutOspfSecIfStatus_Type=RowStatus
_FutOspfSecIfStatus_Object=MibTableColumn
futOspfSecIfStatus=_FutOspfSecIfStatus_Object((1,3,6,1,4,1,10876,101,1,10,9,1,5),_FutOspfSecIfStatus_Type())
futOspfSecIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfSecIfStatus.setStatus(_A)
_FutOspfAreaAggregateTable_Object=MibTable
futOspfAreaAggregateTable=_FutOspfAreaAggregateTable_Object((1,3,6,1,4,1,10876,101,1,10,10))
if mibBuilder.loadTexts:futOspfAreaAggregateTable.setStatus(_A)
_FutOspfAreaAggregateEntry_Object=MibTableRow
futOspfAreaAggregateEntry=_FutOspfAreaAggregateEntry_Object((1,3,6,1,4,1,10876,101,1,10,10,1))
futOspfAreaAggregateEntry.setIndexNames((0,_E,_A5),(0,_E,_A6),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:futOspfAreaAggregateEntry.setStatus(_A)
_FutOspfAreaAggregateAreaID_Type=AreaID
_FutOspfAreaAggregateAreaID_Object=MibTableColumn
futOspfAreaAggregateAreaID=_FutOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,10876,101,1,10,10,1,1),_FutOspfAreaAggregateAreaID_Type())
futOspfAreaAggregateAreaID.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAreaAggregateAreaID.setStatus(_A)
class _FutOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*(('summaryLink',3),('nssaExternalLink',7)))
_FutOspfAreaAggregateLsdbType_Type.__name__=_B
_FutOspfAreaAggregateLsdbType_Object=MibTableColumn
futOspfAreaAggregateLsdbType=_FutOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,10876,101,1,10,10,1,2),_FutOspfAreaAggregateLsdbType_Type())
futOspfAreaAggregateLsdbType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAreaAggregateLsdbType.setStatus(_A)
_FutOspfAreaAggregateNet_Type=IpAddress
_FutOspfAreaAggregateNet_Object=MibTableColumn
futOspfAreaAggregateNet=_FutOspfAreaAggregateNet_Object((1,3,6,1,4,1,10876,101,1,10,10,1,3),_FutOspfAreaAggregateNet_Type())
futOspfAreaAggregateNet.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAreaAggregateNet.setStatus(_A)
_FutOspfAreaAggregateMask_Type=IpAddress
_FutOspfAreaAggregateMask_Object=MibTableColumn
futOspfAreaAggregateMask=_FutOspfAreaAggregateMask_Object((1,3,6,1,4,1,10876,101,1,10,10,1,4),_FutOspfAreaAggregateMask_Type())
futOspfAreaAggregateMask.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAreaAggregateMask.setStatus(_A)
_FutOspfAreaAggregateExternalTag_Type=Integer32
_FutOspfAreaAggregateExternalTag_Object=MibTableColumn
futOspfAreaAggregateExternalTag=_FutOspfAreaAggregateExternalTag_Object((1,3,6,1,4,1,10876,101,1,10,10,1,5),_FutOspfAreaAggregateExternalTag_Type())
futOspfAreaAggregateExternalTag.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAreaAggregateExternalTag.setStatus(_A)
_FutOspfAsExternalAggregationTable_Object=MibTable
futOspfAsExternalAggregationTable=_FutOspfAsExternalAggregationTable_Object((1,3,6,1,4,1,10876,101,1,10,11))
if mibBuilder.loadTexts:futOspfAsExternalAggregationTable.setStatus(_A)
_FutOspfAsExternalAggregationEntry_Object=MibTableRow
futOspfAsExternalAggregationEntry=_FutOspfAsExternalAggregationEntry_Object((1,3,6,1,4,1,10876,101,1,10,11,1))
futOspfAsExternalAggregationEntry.setIndexNames((0,_E,_A9),(0,_E,_AA),(0,_E,_AB))
if mibBuilder.loadTexts:futOspfAsExternalAggregationEntry.setStatus(_A)
_FutOspfAsExternalAggregationNet_Type=IpAddress
_FutOspfAsExternalAggregationNet_Object=MibTableColumn
futOspfAsExternalAggregationNet=_FutOspfAsExternalAggregationNet_Object((1,3,6,1,4,1,10876,101,1,10,11,1,1),_FutOspfAsExternalAggregationNet_Type())
futOspfAsExternalAggregationNet.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAsExternalAggregationNet.setStatus(_A)
_FutOspfAsExternalAggregationMask_Type=IpAddress
_FutOspfAsExternalAggregationMask_Object=MibTableColumn
futOspfAsExternalAggregationMask=_FutOspfAsExternalAggregationMask_Object((1,3,6,1,4,1,10876,101,1,10,11,1,2),_FutOspfAsExternalAggregationMask_Type())
futOspfAsExternalAggregationMask.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAsExternalAggregationMask.setStatus(_A)
_FutOspfAsExternalAggregationAreaId_Type=AreaID
_FutOspfAsExternalAggregationAreaId_Object=MibTableColumn
futOspfAsExternalAggregationAreaId=_FutOspfAsExternalAggregationAreaId_Object((1,3,6,1,4,1,10876,101,1,10,11,1,3),_FutOspfAsExternalAggregationAreaId_Type())
futOspfAsExternalAggregationAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAsExternalAggregationAreaId.setStatus(_A)
class _FutOspfAsExternalAggregationEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertise',1),('doNotAdvertise',2),('allowAll',3),('denyAll',4)))
_FutOspfAsExternalAggregationEffect_Type.__name__=_B
_FutOspfAsExternalAggregationEffect_Object=MibTableColumn
futOspfAsExternalAggregationEffect=_FutOspfAsExternalAggregationEffect_Object((1,3,6,1,4,1,10876,101,1,10,11,1,4),_FutOspfAsExternalAggregationEffect_Type())
futOspfAsExternalAggregationEffect.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAsExternalAggregationEffect.setStatus(_A)
class _FutOspfAsExternalAggregationTranslation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfAsExternalAggregationTranslation_Type.__name__=_B
_FutOspfAsExternalAggregationTranslation_Object=MibTableColumn
futOspfAsExternalAggregationTranslation=_FutOspfAsExternalAggregationTranslation_Object((1,3,6,1,4,1,10876,101,1,10,11,1,5),_FutOspfAsExternalAggregationTranslation_Type())
futOspfAsExternalAggregationTranslation.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAsExternalAggregationTranslation.setStatus(_A)
_FutOspfAsExternalAggregationStatus_Type=RowStatus
_FutOspfAsExternalAggregationStatus_Object=MibTableColumn
futOspfAsExternalAggregationStatus=_FutOspfAsExternalAggregationStatus_Object((1,3,6,1,4,1,10876,101,1,10,11,1,6),_FutOspfAsExternalAggregationStatus_Type())
futOspfAsExternalAggregationStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfAsExternalAggregationStatus.setStatus(_A)
_FutOspfOpaqueLSAGroup_ObjectIdentity=ObjectIdentity
futOspfOpaqueLSAGroup=_FutOspfOpaqueLSAGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,12))
_FutOspfOpaqueLSAGeneralGroup_ObjectIdentity=ObjectIdentity
futOspfOpaqueLSAGeneralGroup=_FutOspfOpaqueLSAGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,12,1))
class _FutOspfOpaqueOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FutOspfOpaqueOption_Type.__name__=_B
_FutOspfOpaqueOption_Object=MibScalar
futOspfOpaqueOption=_FutOspfOpaqueOption_Object((1,3,6,1,4,1,10876,101,1,10,12,1,1),_FutOspfOpaqueOption_Type())
futOspfOpaqueOption.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfOpaqueOption.setStatus(_A)
_FutOspfType11LsaCount_Type=Gauge32
_FutOspfType11LsaCount_Object=MibScalar
futOspfType11LsaCount=_FutOspfType11LsaCount_Object((1,3,6,1,4,1,10876,101,1,10,12,1,2),_FutOspfType11LsaCount_Type())
futOspfType11LsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType11LsaCount.setStatus(_A)
_FutOspfType11LsaCksumSum_Type=Integer32
_FutOspfType11LsaCksumSum_Object=MibScalar
futOspfType11LsaCksumSum=_FutOspfType11LsaCksumSum_Object((1,3,6,1,4,1,10876,101,1,10,12,1,3),_FutOspfType11LsaCksumSum_Type())
futOspfType11LsaCksumSum.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType11LsaCksumSum.setStatus(_A)
class _FutOspfAreaIDValid_Type(TruthValue):defaultValue=2
_FutOspfAreaIDValid_Type.__name__=_M
_FutOspfAreaIDValid_Object=MibScalar
futOspfAreaIDValid=_FutOspfAreaIDValid_Object((1,3,6,1,4,1,10876,101,1,10,12,1,4),_FutOspfAreaIDValid_Type())
futOspfAreaIDValid.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfAreaIDValid.setStatus(_A)
_FutOspfOpaqueInterfaceTable_Object=MibTable
futOspfOpaqueInterfaceTable=_FutOspfOpaqueInterfaceTable_Object((1,3,6,1,4,1,10876,101,1,10,12,2))
if mibBuilder.loadTexts:futOspfOpaqueInterfaceTable.setStatus(_A)
_FutOspfOpaqueInterfaceEntry_Object=MibTableRow
futOspfOpaqueInterfaceEntry=_FutOspfOpaqueInterfaceEntry_Object((1,3,6,1,4,1,10876,101,1,10,12,2,1))
if mibBuilder.loadTexts:futOspfOpaqueInterfaceEntry.setStatus(_A)
_FutOspfOpaqueType9LsaCount_Type=Gauge32
_FutOspfOpaqueType9LsaCount_Object=MibTableColumn
futOspfOpaqueType9LsaCount=_FutOspfOpaqueType9LsaCount_Object((1,3,6,1,4,1,10876,101,1,10,12,2,1,1),_FutOspfOpaqueType9LsaCount_Type())
futOspfOpaqueType9LsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfOpaqueType9LsaCount.setStatus(_A)
class _FutOspfOpaqueType9LsaCksumSum_Type(Integer32):defaultValue=0
_FutOspfOpaqueType9LsaCksumSum_Type.__name__=_B
_FutOspfOpaqueType9LsaCksumSum_Object=MibTableColumn
futOspfOpaqueType9LsaCksumSum=_FutOspfOpaqueType9LsaCksumSum_Object((1,3,6,1,4,1,10876,101,1,10,12,2,1,2),_FutOspfOpaqueType9LsaCksumSum_Type())
futOspfOpaqueType9LsaCksumSum.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfOpaqueType9LsaCksumSum.setStatus(_A)
_FutOspfType9LsdbTable_Object=MibTable
futOspfType9LsdbTable=_FutOspfType9LsdbTable_Object((1,3,6,1,4,1,10876,101,1,10,12,3))
if mibBuilder.loadTexts:futOspfType9LsdbTable.setStatus(_A)
_FutOspfType9LsdbEntry_Object=MibTableRow
futOspfType9LsdbEntry=_FutOspfType9LsdbEntry_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1))
futOspfType9LsdbEntry.setIndexNames((0,_E,_AC),(0,_E,_AD),(0,_E,_AE),(0,_E,_AF))
if mibBuilder.loadTexts:futOspfType9LsdbEntry.setStatus(_A)
_FutOspfType9LsdbIfIpAddress_Type=IpAddress
_FutOspfType9LsdbIfIpAddress_Object=MibTableColumn
futOspfType9LsdbIfIpAddress=_FutOspfType9LsdbIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,1),_FutOspfType9LsdbIfIpAddress_Type())
futOspfType9LsdbIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType9LsdbIfIpAddress.setStatus(_A)
class _FutOspfType9LsdbOpaqueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,11))
_FutOspfType9LsdbOpaqueType_Type.__name__=_B
_FutOspfType9LsdbOpaqueType_Object=MibTableColumn
futOspfType9LsdbOpaqueType=_FutOspfType9LsdbOpaqueType_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,2),_FutOspfType9LsdbOpaqueType_Type())
futOspfType9LsdbOpaqueType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType9LsdbOpaqueType.setStatus(_A)
_FutOspfType9LsdbLsid_Type=IpAddress
_FutOspfType9LsdbLsid_Object=MibTableColumn
futOspfType9LsdbLsid=_FutOspfType9LsdbLsid_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,3),_FutOspfType9LsdbLsid_Type())
futOspfType9LsdbLsid.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType9LsdbLsid.setStatus(_A)
_FutOspfType9LsdbRouterId_Type=RouterID
_FutOspfType9LsdbRouterId_Object=MibTableColumn
futOspfType9LsdbRouterId=_FutOspfType9LsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,4),_FutOspfType9LsdbRouterId_Type())
futOspfType9LsdbRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType9LsdbRouterId.setStatus(_A)
_FutOspfType9LsdbSequence_Type=Integer32
_FutOspfType9LsdbSequence_Object=MibTableColumn
futOspfType9LsdbSequence=_FutOspfType9LsdbSequence_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,5),_FutOspfType9LsdbSequence_Type())
futOspfType9LsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType9LsdbSequence.setStatus(_A)
_FutOspfType9LsdbAge_Type=Integer32
_FutOspfType9LsdbAge_Object=MibTableColumn
futOspfType9LsdbAge=_FutOspfType9LsdbAge_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,6),_FutOspfType9LsdbAge_Type())
futOspfType9LsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType9LsdbAge.setStatus(_A)
_FutOspfType9LsdbChecksum_Type=Integer32
_FutOspfType9LsdbChecksum_Object=MibTableColumn
futOspfType9LsdbChecksum=_FutOspfType9LsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,7),_FutOspfType9LsdbChecksum_Type())
futOspfType9LsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType9LsdbChecksum.setStatus(_A)
class _FutOspfType9LsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FutOspfType9LsdbAdvertisement_Type.__name__=_J
_FutOspfType9LsdbAdvertisement_Object=MibTableColumn
futOspfType9LsdbAdvertisement=_FutOspfType9LsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,10,12,3,1,8),_FutOspfType9LsdbAdvertisement_Type())
futOspfType9LsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType9LsdbAdvertisement.setStatus(_A)
_FutOspfType11LsdbTable_Object=MibTable
futOspfType11LsdbTable=_FutOspfType11LsdbTable_Object((1,3,6,1,4,1,10876,101,1,10,12,4))
if mibBuilder.loadTexts:futOspfType11LsdbTable.setStatus(_A)
_FutOspfType11LsdbEntry_Object=MibTableRow
futOspfType11LsdbEntry=_FutOspfType11LsdbEntry_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1))
futOspfType11LsdbEntry.setIndexNames((0,_E,_AG),(0,_E,_AH),(0,_E,_AI))
if mibBuilder.loadTexts:futOspfType11LsdbEntry.setStatus(_A)
class _FutOspfType11LsdbOpaqueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,11))
_FutOspfType11LsdbOpaqueType_Type.__name__=_B
_FutOspfType11LsdbOpaqueType_Object=MibTableColumn
futOspfType11LsdbOpaqueType=_FutOspfType11LsdbOpaqueType_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,1),_FutOspfType11LsdbOpaqueType_Type())
futOspfType11LsdbOpaqueType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType11LsdbOpaqueType.setStatus(_A)
_FutOspfType11LsdbLsid_Type=IpAddress
_FutOspfType11LsdbLsid_Object=MibTableColumn
futOspfType11LsdbLsid=_FutOspfType11LsdbLsid_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,2),_FutOspfType11LsdbLsid_Type())
futOspfType11LsdbLsid.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType11LsdbLsid.setStatus(_A)
_FutOspfType11LsdbRouterId_Type=RouterID
_FutOspfType11LsdbRouterId_Object=MibTableColumn
futOspfType11LsdbRouterId=_FutOspfType11LsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,3),_FutOspfType11LsdbRouterId_Type())
futOspfType11LsdbRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfType11LsdbRouterId.setStatus(_A)
_FutOspfType11LsdbSequence_Type=Integer32
_FutOspfType11LsdbSequence_Object=MibTableColumn
futOspfType11LsdbSequence=_FutOspfType11LsdbSequence_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,4),_FutOspfType11LsdbSequence_Type())
futOspfType11LsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType11LsdbSequence.setStatus(_A)
_FutOspfType11LsdbAge_Type=Integer32
_FutOspfType11LsdbAge_Object=MibTableColumn
futOspfType11LsdbAge=_FutOspfType11LsdbAge_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,5),_FutOspfType11LsdbAge_Type())
futOspfType11LsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType11LsdbAge.setStatus(_A)
_FutOspfType11LsdbChecksum_Type=Integer32
_FutOspfType11LsdbChecksum_Object=MibTableColumn
futOspfType11LsdbChecksum=_FutOspfType11LsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,6),_FutOspfType11LsdbChecksum_Type())
futOspfType11LsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType11LsdbChecksum.setStatus(_A)
class _FutOspfType11LsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FutOspfType11LsdbAdvertisement_Type.__name__=_J
_FutOspfType11LsdbAdvertisement_Object=MibTableColumn
futOspfType11LsdbAdvertisement=_FutOspfType11LsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,10,12,4,1,7),_FutOspfType11LsdbAdvertisement_Type())
futOspfType11LsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfType11LsdbAdvertisement.setStatus(_A)
_FutOspfAppInfoDbTable_Object=MibTable
futOspfAppInfoDbTable=_FutOspfAppInfoDbTable_Object((1,3,6,1,4,1,10876,101,1,10,12,5))
if mibBuilder.loadTexts:futOspfAppInfoDbTable.setStatus(_A)
_FutOspfAppInfoDbEntry_Object=MibTableRow
futOspfAppInfoDbEntry=_FutOspfAppInfoDbEntry_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1))
futOspfAppInfoDbEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:futOspfAppInfoDbEntry.setStatus(_A)
class _FutOspfAppInfoDbAppid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FutOspfAppInfoDbAppid_Type.__name__=_B
_FutOspfAppInfoDbAppid_Object=MibTableColumn
futOspfAppInfoDbAppid=_FutOspfAppInfoDbAppid_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,1),_FutOspfAppInfoDbAppid_Type())
futOspfAppInfoDbAppid.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfAppInfoDbAppid.setStatus(_A)
class _FutOspfAppInfoDbOpaqueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspfAppInfoDbOpaqueType_Type.__name__=_B
_FutOspfAppInfoDbOpaqueType_Object=MibTableColumn
futOspfAppInfoDbOpaqueType=_FutOspfAppInfoDbOpaqueType_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,2),_FutOspfAppInfoDbOpaqueType_Type())
futOspfAppInfoDbOpaqueType.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbOpaqueType.setStatus(_A)
class _FutOspfAppInfoDbLsaTypesSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FutOspfAppInfoDbLsaTypesSupported_Type.__name__=_B
_FutOspfAppInfoDbLsaTypesSupported_Object=MibTableColumn
futOspfAppInfoDbLsaTypesSupported=_FutOspfAppInfoDbLsaTypesSupported_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,3),_FutOspfAppInfoDbLsaTypesSupported_Type())
futOspfAppInfoDbLsaTypesSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbLsaTypesSupported.setStatus(_A)
_FutOspfAppInfoDbType9Gen_Type=Counter32
_FutOspfAppInfoDbType9Gen_Object=MibTableColumn
futOspfAppInfoDbType9Gen=_FutOspfAppInfoDbType9Gen_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,4),_FutOspfAppInfoDbType9Gen_Type())
futOspfAppInfoDbType9Gen.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbType9Gen.setStatus(_A)
_FutOspfAppInfoDbType9Rcvd_Type=Counter32
_FutOspfAppInfoDbType9Rcvd_Object=MibTableColumn
futOspfAppInfoDbType9Rcvd=_FutOspfAppInfoDbType9Rcvd_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,5),_FutOspfAppInfoDbType9Rcvd_Type())
futOspfAppInfoDbType9Rcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbType9Rcvd.setStatus(_A)
_FutOspfAppInfoDbType10Gen_Type=Counter32
_FutOspfAppInfoDbType10Gen_Object=MibTableColumn
futOspfAppInfoDbType10Gen=_FutOspfAppInfoDbType10Gen_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,6),_FutOspfAppInfoDbType10Gen_Type())
futOspfAppInfoDbType10Gen.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbType10Gen.setStatus(_A)
_FutOspfAppInfoDbType10Rcvd_Type=Counter32
_FutOspfAppInfoDbType10Rcvd_Object=MibTableColumn
futOspfAppInfoDbType10Rcvd=_FutOspfAppInfoDbType10Rcvd_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,7),_FutOspfAppInfoDbType10Rcvd_Type())
futOspfAppInfoDbType10Rcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbType10Rcvd.setStatus(_A)
_FutOspfAppInfoDbType11Gen_Type=Counter32
_FutOspfAppInfoDbType11Gen_Object=MibTableColumn
futOspfAppInfoDbType11Gen=_FutOspfAppInfoDbType11Gen_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,8),_FutOspfAppInfoDbType11Gen_Type())
futOspfAppInfoDbType11Gen.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbType11Gen.setStatus(_A)
_FutOspfAppInfoDbType11Rcvd_Type=Counter32
_FutOspfAppInfoDbType11Rcvd_Object=MibTableColumn
futOspfAppInfoDbType11Rcvd=_FutOspfAppInfoDbType11Rcvd_Object((1,3,6,1,4,1,10876,101,1,10,12,5,1,9),_FutOspfAppInfoDbType11Rcvd_Type())
futOspfAppInfoDbType11Rcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfAppInfoDbType11Rcvd.setStatus(_A)
_FutospfRRDGroup_ObjectIdentity=ObjectIdentity
futospfRRDGroup=_FutospfRRDGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,13))
_FutospfRRDGeneralGroup_ObjectIdentity=ObjectIdentity
futospfRRDGeneralGroup=_FutospfRRDGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,13,1))
class _FutOspfRRDStatus_Type(Status):defaultValue=2
_FutOspfRRDStatus_Type.__name__=_U
_FutOspfRRDStatus_Object=MibScalar
futOspfRRDStatus=_FutOspfRRDStatus_Object((1,3,6,1,4,1,10876,101,1,10,13,1,1),_FutOspfRRDStatus_Type())
futOspfRRDStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDStatus.setStatus(_A)
class _FutOspfRRDSrcProtoMaskEnable_Type(Integer32):defaultValue=0
_FutOspfRRDSrcProtoMaskEnable_Type.__name__=_B
_FutOspfRRDSrcProtoMaskEnable_Object=MibScalar
futOspfRRDSrcProtoMaskEnable=_FutOspfRRDSrcProtoMaskEnable_Object((1,3,6,1,4,1,10876,101,1,10,13,1,2),_FutOspfRRDSrcProtoMaskEnable_Type())
futOspfRRDSrcProtoMaskEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDSrcProtoMaskEnable.setStatus(_A)
class _FutOspfRRDSrcProtoMaskDisable_Type(Integer32):defaultValue=8326
_FutOspfRRDSrcProtoMaskDisable_Type.__name__=_B
_FutOspfRRDSrcProtoMaskDisable_Object=MibScalar
futOspfRRDSrcProtoMaskDisable=_FutOspfRRDSrcProtoMaskDisable_Object((1,3,6,1,4,1,10876,101,1,10,13,1,3),_FutOspfRRDSrcProtoMaskDisable_Type())
futOspfRRDSrcProtoMaskDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDSrcProtoMaskDisable.setStatus(_A)
class _FutOspfRRDRouteMapEnable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FutOspfRRDRouteMapEnable_Type.__name__=_V
_FutOspfRRDRouteMapEnable_Object=MibScalar
futOspfRRDRouteMapEnable=_FutOspfRRDRouteMapEnable_Object((1,3,6,1,4,1,10876,101,1,10,13,1,4),_FutOspfRRDRouteMapEnable_Type())
futOspfRRDRouteMapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDRouteMapEnable.setStatus(_A)
_FutOspfRRDRouteConfigTable_Object=MibTable
futOspfRRDRouteConfigTable=_FutOspfRRDRouteConfigTable_Object((1,3,6,1,4,1,10876,101,1,10,13,2))
if mibBuilder.loadTexts:futOspfRRDRouteConfigTable.setStatus(_A)
_FutOspfRRDRouteConfigEntry_Object=MibTableRow
futOspfRRDRouteConfigEntry=_FutOspfRRDRouteConfigEntry_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1))
futOspfRRDRouteConfigEntry.setIndexNames((0,_E,_AK),(0,_E,_AL))
if mibBuilder.loadTexts:futOspfRRDRouteConfigEntry.setStatus(_A)
_FutOspfRRDRouteDest_Type=IpAddress
_FutOspfRRDRouteDest_Object=MibTableColumn
futOspfRRDRouteDest=_FutOspfRRDRouteDest_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,1),_FutOspfRRDRouteDest_Type())
futOspfRRDRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfRRDRouteDest.setStatus(_A)
_FutOspfRRDRouteMask_Type=IpAddress
_FutOspfRRDRouteMask_Object=MibTableColumn
futOspfRRDRouteMask=_FutOspfRRDRouteMask_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,2),_FutOspfRRDRouteMask_Type())
futOspfRRDRouteMask.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfRRDRouteMask.setStatus(_A)
class _FutOspfRRDRouteMetric_Type(BigMetric):defaultValue=10
_FutOspfRRDRouteMetric_Type.__name__=_Z
_FutOspfRRDRouteMetric_Object=MibTableColumn
futOspfRRDRouteMetric=_FutOspfRRDRouteMetric_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,3),_FutOspfRRDRouteMetric_Type())
futOspfRRDRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDRouteMetric.setStatus(_A)
class _FutOspfRRDRouteMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asexttype1',1),('asexttype2',2)))
_FutOspfRRDRouteMetricType_Type.__name__=_B
_FutOspfRRDRouteMetricType_Object=MibTableColumn
futOspfRRDRouteMetricType=_FutOspfRRDRouteMetricType_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,4),_FutOspfRRDRouteMetricType_Type())
futOspfRRDRouteMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDRouteMetricType.setStatus(_A)
class _FutOspfRRDRouteTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_FutOspfRRDRouteTagType_Type.__name__=_B
_FutOspfRRDRouteTagType_Object=MibTableColumn
futOspfRRDRouteTagType=_FutOspfRRDRouteTagType_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,5),_FutOspfRRDRouteTagType_Type())
futOspfRRDRouteTagType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDRouteTagType.setStatus(_A)
class _FutOspfRRDRouteTag_Type(Unsigned32):defaultValue=0
_FutOspfRRDRouteTag_Type.__name__=_d
_FutOspfRRDRouteTag_Object=MibTableColumn
futOspfRRDRouteTag=_FutOspfRRDRouteTag_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,6),_FutOspfRRDRouteTag_Type())
futOspfRRDRouteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfRRDRouteTag.setStatus(_A)
_FutOspfRRDRouteStatus_Type=RowStatus
_FutOspfRRDRouteStatus_Object=MibTableColumn
futOspfRRDRouteStatus=_FutOspfRRDRouteStatus_Object((1,3,6,1,4,1,10876,101,1,10,13,2,1,7),_FutOspfRRDRouteStatus_Type())
futOspfRRDRouteStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:futOspfRRDRouteStatus.setStatus(_A)
_FutOspfVirtNbrTable_Object=MibTable
futOspfVirtNbrTable=_FutOspfVirtNbrTable_Object((1,3,6,1,4,1,10876,101,1,10,14))
if mibBuilder.loadTexts:futOspfVirtNbrTable.setStatus(_A)
_FutOspfVirtNbrEntry_Object=MibTableRow
futOspfVirtNbrEntry=_FutOspfVirtNbrEntry_Object((1,3,6,1,4,1,10876,101,1,10,14,1))
if mibBuilder.loadTexts:futOspfVirtNbrEntry.setStatus(_A)
class _FutOspfVirtNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_FutOspfVirtNbrRestartHelperStatus_Type.__name__=_B
_FutOspfVirtNbrRestartHelperStatus_Object=MibTableColumn
futOspfVirtNbrRestartHelperStatus=_FutOspfVirtNbrRestartHelperStatus_Object((1,3,6,1,4,1,10876,101,1,10,14,1,1),_FutOspfVirtNbrRestartHelperStatus_Type())
futOspfVirtNbrRestartHelperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfVirtNbrRestartHelperStatus.setStatus(_A)
_FutOspfVirtNbrRestartHelperAge_Type=Unsigned32
_FutOspfVirtNbrRestartHelperAge_Object=MibTableColumn
futOspfVirtNbrRestartHelperAge=_FutOspfVirtNbrRestartHelperAge_Object((1,3,6,1,4,1,10876,101,1,10,14,1,2),_FutOspfVirtNbrRestartHelperAge_Type())
futOspfVirtNbrRestartHelperAge.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfVirtNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:futOspfVirtNbrRestartHelperAge.setUnits(_W)
class _FutOspfVirtNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_X,4),(_Y,5)))
_FutOspfVirtNbrRestartHelperExitReason_Type.__name__=_B
_FutOspfVirtNbrRestartHelperExitReason_Object=MibTableColumn
futOspfVirtNbrRestartHelperExitReason=_FutOspfVirtNbrRestartHelperExitReason_Object((1,3,6,1,4,1,10876,101,1,10,14,1,3),_FutOspfVirtNbrRestartHelperExitReason_Type())
futOspfVirtNbrRestartHelperExitReason.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfVirtNbrRestartHelperExitReason.setStatus(_A)
_FutospfDistInOutRouteMap_ObjectIdentity=ObjectIdentity
futospfDistInOutRouteMap=_FutospfDistInOutRouteMap_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,15))
_FutOspfDistInOutRouteMapTable_Object=MibTable
futOspfDistInOutRouteMapTable=_FutOspfDistInOutRouteMapTable_Object((1,3,6,1,4,1,10876,101,1,10,15,1))
if mibBuilder.loadTexts:futOspfDistInOutRouteMapTable.setStatus(_A)
_FutOspfDistInOutRouteMapEntry_Object=MibTableRow
futOspfDistInOutRouteMapEntry=_FutOspfDistInOutRouteMapEntry_Object((1,3,6,1,4,1,10876,101,1,10,15,1,1))
futOspfDistInOutRouteMapEntry.setIndexNames((0,_E,_AM),(0,_E,_AN))
if mibBuilder.loadTexts:futOspfDistInOutRouteMapEntry.setStatus(_A)
class _FutOspfDistInOutRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FutOspfDistInOutRouteMapName_Type.__name__=_V
_FutOspfDistInOutRouteMapName_Object=MibTableColumn
futOspfDistInOutRouteMapName=_FutOspfDistInOutRouteMapName_Object((1,3,6,1,4,1,10876,101,1,10,15,1,1,1),_FutOspfDistInOutRouteMapName_Type())
futOspfDistInOutRouteMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfDistInOutRouteMapName.setStatus(_A)
class _FutOspfDistInOutRouteMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FutOspfDistInOutRouteMapType_Type.__name__=_B
_FutOspfDistInOutRouteMapType_Object=MibTableColumn
futOspfDistInOutRouteMapType=_FutOspfDistInOutRouteMapType_Object((1,3,6,1,4,1,10876,101,1,10,15,1,1,3),_FutOspfDistInOutRouteMapType_Type())
futOspfDistInOutRouteMapType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfDistInOutRouteMapType.setStatus(_A)
class _FutOspfDistInOutRouteMapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FutOspfDistInOutRouteMapValue_Type.__name__=_B
_FutOspfDistInOutRouteMapValue_Object=MibTableColumn
futOspfDistInOutRouteMapValue=_FutOspfDistInOutRouteMapValue_Object((1,3,6,1,4,1,10876,101,1,10,15,1,1,4),_FutOspfDistInOutRouteMapValue_Type())
futOspfDistInOutRouteMapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfDistInOutRouteMapValue.setStatus(_A)
_FutOspfDistInOutRouteMapRowStatus_Type=RowStatus
_FutOspfDistInOutRouteMapRowStatus_Object=MibTableColumn
futOspfDistInOutRouteMapRowStatus=_FutOspfDistInOutRouteMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,10,15,1,1,5),_FutOspfDistInOutRouteMapRowStatus_Type())
futOspfDistInOutRouteMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfDistInOutRouteMapRowStatus.setStatus(_A)
_FutospfPreferenceGroup_ObjectIdentity=ObjectIdentity
futospfPreferenceGroup=_FutospfPreferenceGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,16))
class _FutOspfPreferenceValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspfPreferenceValue_Type.__name__=_B
_FutOspfPreferenceValue_Object=MibScalar
futOspfPreferenceValue=_FutOspfPreferenceValue_Object((1,3,6,1,4,1,10876,101,1,10,16,1),_FutOspfPreferenceValue_Type())
futOspfPreferenceValue.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfPreferenceValue.setStatus(_A)
_FutOspfIfAuthTable_Object=MibTable
futOspfIfAuthTable=_FutOspfIfAuthTable_Object((1,3,6,1,4,1,10876,101,1,10,17))
if mibBuilder.loadTexts:futOspfIfAuthTable.setStatus(_A)
_FutOspfIfAuthEntry_Object=MibTableRow
futOspfIfAuthEntry=_FutOspfIfAuthEntry_Object((1,3,6,1,4,1,10876,101,1,10,17,1))
futOspfIfAuthEntry.setIndexNames((0,_E,_AO),(0,_E,_AP),(0,_E,_AQ))
if mibBuilder.loadTexts:futOspfIfAuthEntry.setStatus(_A)
_FutOspfIfAuthIpAddress_Type=IpAddress
_FutOspfIfAuthIpAddress_Object=MibTableColumn
futOspfIfAuthIpAddress=_FutOspfIfAuthIpAddress_Object((1,3,6,1,4,1,10876,101,1,10,17,1,1),_FutOspfIfAuthIpAddress_Type())
futOspfIfAuthIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfAuthIpAddress.setStatus(_A)
class _FutOspfIfAuthAddressLessIf_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfIfAuthAddressLessIf_Type.__name__=_K
_FutOspfIfAuthAddressLessIf_Object=MibTableColumn
futOspfIfAuthAddressLessIf=_FutOspfIfAuthAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,10,17,1,2),_FutOspfIfAuthAddressLessIf_Type())
futOspfIfAuthAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfAuthAddressLessIf.setStatus(_A)
class _FutOspfIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspfIfAuthKeyId_Type.__name__=_B
_FutOspfIfAuthKeyId_Object=MibTableColumn
futOspfIfAuthKeyId=_FutOspfIfAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,10,17,1,3),_FutOspfIfAuthKeyId_Type())
futOspfIfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfIfAuthKeyId.setStatus(_A)
class _FutOspfIfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FutOspfIfAuthKey_Type.__name__=_J
_FutOspfIfAuthKey_Object=MibTableColumn
futOspfIfAuthKey=_FutOspfIfAuthKey_Object((1,3,6,1,4,1,10876,101,1,10,17,1,4),_FutOspfIfAuthKey_Type())
futOspfIfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfAuthKey.setStatus(_A)
_FutOspfIfAuthKeyStartAccept_Type=DateAndTime
_FutOspfIfAuthKeyStartAccept_Object=MibTableColumn
futOspfIfAuthKeyStartAccept=_FutOspfIfAuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,10,17,1,5),_FutOspfIfAuthKeyStartAccept_Type())
futOspfIfAuthKeyStartAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfAuthKeyStartAccept.setStatus(_A)
_FutOspfIfAuthKeyStartGenerate_Type=DateAndTime
_FutOspfIfAuthKeyStartGenerate_Object=MibTableColumn
futOspfIfAuthKeyStartGenerate=_FutOspfIfAuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,10,17,1,6),_FutOspfIfAuthKeyStartGenerate_Type())
futOspfIfAuthKeyStartGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfAuthKeyStartGenerate.setStatus(_A)
_FutOspfIfAuthKeyStopGenerate_Type=DateAndTime
_FutOspfIfAuthKeyStopGenerate_Object=MibTableColumn
futOspfIfAuthKeyStopGenerate=_FutOspfIfAuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,10,17,1,7),_FutOspfIfAuthKeyStopGenerate_Type())
futOspfIfAuthKeyStopGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfAuthKeyStopGenerate.setStatus(_A)
_FutOspfIfAuthKeyStopAccept_Type=DateAndTime
_FutOspfIfAuthKeyStopAccept_Object=MibTableColumn
futOspfIfAuthKeyStopAccept=_FutOspfIfAuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,10,17,1,8),_FutOspfIfAuthKeyStopAccept_Type())
futOspfIfAuthKeyStopAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfAuthKeyStopAccept.setStatus(_A)
class _FutOspfIfAuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_S,1),(_T,3)))
_FutOspfIfAuthKeyStatus_Type.__name__=_B
_FutOspfIfAuthKeyStatus_Object=MibTableColumn
futOspfIfAuthKeyStatus=_FutOspfIfAuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,10,17,1,9),_FutOspfIfAuthKeyStatus_Type())
futOspfIfAuthKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfAuthKeyStatus.setStatus(_A)
_FutOspfVirtIfAuthTable_Object=MibTable
futOspfVirtIfAuthTable=_FutOspfVirtIfAuthTable_Object((1,3,6,1,4,1,10876,101,1,10,18))
if mibBuilder.loadTexts:futOspfVirtIfAuthTable.setStatus(_A)
_FutOspfVirtIfAuthEntry_Object=MibTableRow
futOspfVirtIfAuthEntry=_FutOspfVirtIfAuthEntry_Object((1,3,6,1,4,1,10876,101,1,10,18,1))
futOspfVirtIfAuthEntry.setIndexNames((0,_E,_AR),(0,_E,_AS),(0,_E,_AT))
if mibBuilder.loadTexts:futOspfVirtIfAuthEntry.setStatus(_A)
_FutOspfVirtIfAuthAreaId_Type=AreaID
_FutOspfVirtIfAuthAreaId_Object=MibTableColumn
futOspfVirtIfAuthAreaId=_FutOspfVirtIfAuthAreaId_Object((1,3,6,1,4,1,10876,101,1,10,18,1,1),_FutOspfVirtIfAuthAreaId_Type())
futOspfVirtIfAuthAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfVirtIfAuthAreaId.setStatus(_A)
_FutOspfVirtIfAuthNeighbor_Type=RouterID
_FutOspfVirtIfAuthNeighbor_Object=MibTableColumn
futOspfVirtIfAuthNeighbor=_FutOspfVirtIfAuthNeighbor_Object((1,3,6,1,4,1,10876,101,1,10,18,1,2),_FutOspfVirtIfAuthNeighbor_Type())
futOspfVirtIfAuthNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfVirtIfAuthNeighbor.setStatus(_A)
class _FutOspfVirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspfVirtIfAuthKeyId_Type.__name__=_B
_FutOspfVirtIfAuthKeyId_Object=MibTableColumn
futOspfVirtIfAuthKeyId=_FutOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,10,18,1,3),_FutOspfVirtIfAuthKeyId_Type())
futOspfVirtIfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfVirtIfAuthKeyId.setStatus(_A)
class _FutOspfVirtIfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FutOspfVirtIfAuthKey_Type.__name__=_J
_FutOspfVirtIfAuthKey_Object=MibTableColumn
futOspfVirtIfAuthKey=_FutOspfVirtIfAuthKey_Object((1,3,6,1,4,1,10876,101,1,10,18,1,4),_FutOspfVirtIfAuthKey_Type())
futOspfVirtIfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfAuthKey.setStatus(_A)
_FutOspfVirtIfAuthKeyStartAccept_Type=DateAndTime
_FutOspfVirtIfAuthKeyStartAccept_Object=MibTableColumn
futOspfVirtIfAuthKeyStartAccept=_FutOspfVirtIfAuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,10,18,1,5),_FutOspfVirtIfAuthKeyStartAccept_Type())
futOspfVirtIfAuthKeyStartAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfAuthKeyStartAccept.setStatus(_A)
_FutOspfVirtIfAuthKeyStartGenerate_Type=DateAndTime
_FutOspfVirtIfAuthKeyStartGenerate_Object=MibTableColumn
futOspfVirtIfAuthKeyStartGenerate=_FutOspfVirtIfAuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,10,18,1,6),_FutOspfVirtIfAuthKeyStartGenerate_Type())
futOspfVirtIfAuthKeyStartGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfAuthKeyStartGenerate.setStatus(_A)
_FutOspfVirtIfAuthKeyStopGenerate_Type=DateAndTime
_FutOspfVirtIfAuthKeyStopGenerate_Object=MibTableColumn
futOspfVirtIfAuthKeyStopGenerate=_FutOspfVirtIfAuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,10,18,1,7),_FutOspfVirtIfAuthKeyStopGenerate_Type())
futOspfVirtIfAuthKeyStopGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfAuthKeyStopGenerate.setStatus(_A)
_FutOspfVirtIfAuthKeyStopAccept_Type=DateAndTime
_FutOspfVirtIfAuthKeyStopAccept_Object=MibTableColumn
futOspfVirtIfAuthKeyStopAccept=_FutOspfVirtIfAuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,10,18,1,8),_FutOspfVirtIfAuthKeyStopAccept_Type())
futOspfVirtIfAuthKeyStopAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfAuthKeyStopAccept.setStatus(_A)
class _FutOspfVirtIfAuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_S,1),(_T,3)))
_FutOspfVirtIfAuthKeyStatus_Type.__name__=_B
_FutOspfVirtIfAuthKeyStatus_Object=MibTableColumn
futOspfVirtIfAuthKeyStatus=_FutOspfVirtIfAuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,10,18,1,9),_FutOspfVirtIfAuthKeyStatus_Type())
futOspfVirtIfAuthKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfAuthKeyStatus.setStatus(_A)
_FutOspfIfCryptoAuthTable_Object=MibTable
futOspfIfCryptoAuthTable=_FutOspfIfCryptoAuthTable_Object((1,3,6,1,4,1,10876,101,1,10,19))
if mibBuilder.loadTexts:futOspfIfCryptoAuthTable.setStatus(_A)
_FutOspfIfCryptoAuthEntry_Object=MibTableRow
futOspfIfCryptoAuthEntry=_FutOspfIfCryptoAuthEntry_Object((1,3,6,1,4,1,10876,101,1,10,19,1))
if mibBuilder.loadTexts:futOspfIfCryptoAuthEntry.setStatus(_A)
class _FutOspfIfCryptoAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('md5',1),('sha1',2),('sha224',3),('sha256',4),('sha384',5),('sha512',6)))
_FutOspfIfCryptoAuthType_Type.__name__=_B
_FutOspfIfCryptoAuthType_Object=MibTableColumn
futOspfIfCryptoAuthType=_FutOspfIfCryptoAuthType_Object((1,3,6,1,4,1,10876,101,1,10,19,1,1),_FutOspfIfCryptoAuthType_Type())
futOspfIfCryptoAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfIfCryptoAuthType.setStatus(_A)
_FutOspfVirtIfCryptoAuthTable_Object=MibTable
futOspfVirtIfCryptoAuthTable=_FutOspfVirtIfCryptoAuthTable_Object((1,3,6,1,4,1,10876,101,1,10,20))
if mibBuilder.loadTexts:futOspfVirtIfCryptoAuthTable.setStatus(_A)
_FutOspfVirtIfCryptoAuthEntry_Object=MibTableRow
futOspfVirtIfCryptoAuthEntry=_FutOspfVirtIfCryptoAuthEntry_Object((1,3,6,1,4,1,10876,101,1,10,20,1))
if mibBuilder.loadTexts:futOspfVirtIfCryptoAuthEntry.setStatus(_A)
class _FutOspfVirtIfCryptoAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('md5',1),('sha1',2),('sha224',3),('sha256',4),('sha384',5),('sha512',6)))
_FutOspfVirtIfCryptoAuthType_Type.__name__=_B
_FutOspfVirtIfCryptoAuthType_Object=MibTableColumn
futOspfVirtIfCryptoAuthType=_FutOspfVirtIfCryptoAuthType_Object((1,3,6,1,4,1,10876,101,1,10,20,1,1),_FutOspfVirtIfCryptoAuthType_Type())
futOspfVirtIfCryptoAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfVirtIfCryptoAuthType.setStatus(_A)
_FutOspfTestGroup_ObjectIdentity=ObjectIdentity
futOspfTestGroup=_FutOspfTestGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,100))
_FutOspfNotification_ObjectIdentity=ObjectIdentity
futOspfNotification=_FutOspfNotification_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,101))
_FutOspfTraps_ObjectIdentity=ObjectIdentity
futOspfTraps=_FutOspfTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,101,0))
_FutOspfOasGroup_ObjectIdentity=ObjectIdentity
futOspfOasGroup=_FutOspfOasGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,102))
futOspfIfEntry.registerAugmentions((_E,_AU))
futOspfOpaqueInterfaceEntry.setIndexNames(*futOspfIfEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions((_E,_AV))
futOspfVirtNbrEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_E,_AW))
futOspfIfCryptoAuthEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_E,_AX))
futOspfVirtIfCryptoAuthEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
futOspfRestartStatusChange=NotificationType((1,3,6,1,4,1,10876,101,1,10,101,0,1))
futOspfRestartStatusChange.setObjects(*((_L,_O),(_E,_AY),(_E,_AZ),(_E,_Aa)))
if mibBuilder.loadTexts:futOspfRestartStatusChange.setStatus(_A)
futOspfNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,1,10,101,0,2))
futOspfNbrRestartHelperStatusChange.setObjects(*((_L,_O),(_L,_b),(_E,_Ab),(_E,_Ac),(_E,_Ad)))
if mibBuilder.loadTexts:futOspfNbrRestartHelperStatusChange.setStatus(_A)
futOspfVirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,1,10,101,0,3))
futOspfVirtNbrRestartHelperStatusChange.setObjects(*((_L,_O),(_E,_Ae),(_E,_Af),(_E,_Ag)))
if mibBuilder.loadTexts:futOspfVirtNbrRestartHelperStatusChange.setStatus(_A)
futOspfHotStandbyEventTrap=NotificationType((1,3,6,1,4,1,10876,101,1,10,101,0,4))
futOspfHotStandbyEventTrap.setObjects(*((_L,_O),(_E,_Ah),(_E,_Ai)))
if mibBuilder.loadTexts:futOspfHotStandbyEventTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'futospf':futospf,'futospfGeneralGroup':futospfGeneralGroup,'futOspfOverFlowState':futOspfOverFlowState,'futOspfPktsRcvd':futOspfPktsRcvd,'futOspfPktsTxed':futOspfPktsTxed,'futOspfPktsDisd':futOspfPktsDisd,'futOspfRFC1583Compatibility':futOspfRFC1583Compatibility,'futOspfMaxAreas':futOspfMaxAreas,'futOspfMaxLSAperArea':futOspfMaxLSAperArea,'futOspfMaxExtLSAs':futOspfMaxExtLSAs,'futOspfMaxSelfOrgLSAs':futOspfMaxSelfOrgLSAs,'futOspfMaxRoutes':futOspfMaxRoutes,'futOspfMaxLsaSize':futOspfMaxLsaSize,'futOspfTraceLevel':futOspfTraceLevel,'futOspfMinLsaInterval':futOspfMinLsaInterval,'futOspfABRType':futOspfABRType,'futOspfNssaAsbrDefRtTrans':futOspfNssaAsbrDefRtTrans,'futOspfDefaultPassiveInterface':futOspfDefaultPassiveInterface,'futOspfSpfHoldtime':futOspfSpfHoldtime,'futOspfSpfDelay':futOspfSpfDelay,'futOspfRestartSupport':futOspfRestartSupport,_AZ:futOspfRestartInterval,'futOspfRestartStrictLsaChecking':futOspfRestartStrictLsaChecking,_AY:futOspfRestartStatus,'futOspfRestartAge':futOspfRestartAge,_Aa:futOspfRestartExitReason,'futOspfHelperSupport':futOspfHelperSupport,'futOspfHelperGraceTimeLimit':futOspfHelperGraceTimeLimit,'futOspfRestartAckState':futOspfRestartAckState,'futOspfGraceLsaRetransmitCount':futOspfGraceLsaRetransmitCount,'futOspfRestartReason':futOspfRestartReason,'futOspfRTStaggeringInterval':futOspfRTStaggeringInterval,'futOspfRTStaggeringStatus':futOspfRTStaggeringStatus,'futOspfHotStandbyAdminStatus':futOspfHotStandbyAdminStatus,_Ah:futOspfHotStandbyState,_Ai:futOspfDynamicBulkUpdStatus,'futOspfStanbyHelloSyncCount':futOspfStanbyHelloSyncCount,'futOspfStanbyLsaSyncCount':futOspfStanbyLsaSyncCount,'futOspfExtTraceLevel':futOspfExtTraceLevel,'futospfRouterIdPermanence':futospfRouterIdPermanence,'futOspfBfdStatus':futOspfBfdStatus,'futOspfBfdAllIfState':futOspfBfdAllIfState,'futOspfAreaTable':futOspfAreaTable,'futOspfAreaEntry':futOspfAreaEntry,_i:futOspfAreaId,'futOspfAreaIfCount':futOspfAreaIfCount,'futOspfAreaNetCount':futOspfAreaNetCount,'futOspfAreaRtrCount':futOspfAreaRtrCount,'futOspfAreaNSSATranslatorRole':futOspfAreaNSSATranslatorRole,'futOspfAreaNSSATranslatorState':futOspfAreaNSSATranslatorState,'futOspfAreaNSSATranslatorStabilityInterval':futOspfAreaNSSATranslatorStabilityInterval,'futOspfAreaNSSATranslatorEvents':futOspfAreaNSSATranslatorEvents,'futOspfAreaDfInfOriginate':futOspfAreaDfInfOriginate,'futOspfHostTable':futOspfHostTable,'futOspfHostEntry':futOspfHostEntry,_j:futOspfHostIpAddress,_k:futOspfHostTOS,'futOspfHostRouteIfIndex':futOspfHostRouteIfIndex,'futOspfIfTable':futOspfIfTable,'futOspfIfEntry':futOspfIfEntry,_l:futOspfIfIpAddress,_m:futOspfAddressLessIf,'futOspfIfOperState':futOspfIfOperState,'futOspfIfPassive':futOspfIfPassive,'futOspfIfNbrCount':futOspfIfNbrCount,'futOspfIfAdjCount':futOspfIfAdjCount,'futOspfIfHelloRcvd':futOspfIfHelloRcvd,'futOspfIfHelloTxed':futOspfIfHelloTxed,'futOspfIfHelloDisd':futOspfIfHelloDisd,'futOspfIfDdpRcvd':futOspfIfDdpRcvd,'futOspfIfDdpTxed':futOspfIfDdpTxed,'futOspfIfDdpDisd':futOspfIfDdpDisd,'futOspfIfLrqRcvd':futOspfIfLrqRcvd,'futOspfIfLrqTxed':futOspfIfLrqTxed,'futOspfIfLrqDisd':futOspfIfLrqDisd,'futOspfIfLsuRcvd':futOspfIfLsuRcvd,'futOspfIfLsuTxed':futOspfIfLsuTxed,'futOspfIfLsuDisd':futOspfIfLsuDisd,'futOspfIfLakRcvd':futOspfIfLakRcvd,'futOspfIfLakTxed':futOspfIfLakTxed,'futOspfIfLakDisd':futOspfIfLakDisd,'futOspfIfBfdState':futOspfIfBfdState,'futOspfIfMD5AuthTable':futOspfIfMD5AuthTable,'futOspfIfMD5AuthEntry':futOspfIfMD5AuthEntry,_n:futOspfIfMD5AuthIpAddress,_o:futOspfIfMD5AuthAddressLessIf,_p:futOspfIfMD5AuthKeyId,'futOspfIfMD5AuthKey':futOspfIfMD5AuthKey,'futOspfIfMD5AuthKeyStartAccept':futOspfIfMD5AuthKeyStartAccept,'futOspfIfMD5AuthKeyStartGenerate':futOspfIfMD5AuthKeyStartGenerate,'futOspfIfMD5AuthKeyStopGenerate':futOspfIfMD5AuthKeyStopGenerate,'futOspfIfMD5AuthKeyStopAccept':futOspfIfMD5AuthKeyStopAccept,'futOspfIfMD5AuthKeyStatus':futOspfIfMD5AuthKeyStatus,'futOspfVirtIfMD5AuthTable':futOspfVirtIfMD5AuthTable,'futOspfVirtIfMD5AuthEntry':futOspfVirtIfMD5AuthEntry,_q:futOspfVirtIfMD5AuthAreaId,_r:futOspfVirtIfMD5AuthNeighbor,_s:futOspfVirtIfMD5AuthKeyId,'futOspfVirtIfMD5AuthKey':futOspfVirtIfMD5AuthKey,'futOspfVirtIfMD5AuthKeyStartAccept':futOspfVirtIfMD5AuthKeyStartAccept,'futOspfVirtIfMD5AuthKeyStartGenerate':futOspfVirtIfMD5AuthKeyStartGenerate,'futOspfVirtIfMD5AuthKeyStopGenerate':futOspfVirtIfMD5AuthKeyStopGenerate,'futOspfVirtIfMD5AuthKeyStopAccept':futOspfVirtIfMD5AuthKeyStopAccept,'futOspfVirtIfMD5AuthKeyStatus':futOspfVirtIfMD5AuthKeyStatus,'futOspfNbrTable':futOspfNbrTable,'futOspfNbrEntry':futOspfNbrEntry,_t:futOspfNbrIpAddr,_u:futOspfNbrAddressLessIndex,'futOspfNbrDBSummaryQLen':futOspfNbrDBSummaryQLen,'futOspfNbrLSReqQLen':futOspfNbrLSReqQLen,_Ab:futOspfNbrRestartHelperStatus,_Ac:futOspfNbrRestartHelperAge,_Ad:futOspfNbrRestartHelperExitReason,'futOspfNbrBfdState':futOspfNbrBfdState,'futOspfRoutingTable':futOspfRoutingTable,'futOspfRoutingEntry':futOspfRoutingEntry,_x:futOspfRouteIpAddr,_y:futOspfRouteIpAddrMask,_z:futOspfRouteIpTos,_A0:futOspfRouteIpNextHop,'futOspfRouteType':futOspfRouteType,'futOspfRouteAreaId':futOspfRouteAreaId,'futOspfRouteCost':futOspfRouteCost,'futOspfRouteType2Cost':futOspfRouteType2Cost,'futOspfRouteInterfaceIndex':futOspfRouteInterfaceIndex,'futOspfSecIfTable':futOspfSecIfTable,'futOspfSecIfEntry':futOspfSecIfEntry,_A1:futOspfPrimIpAddr,_A2:futOspfPrimAddresslessIf,_A3:futOspfSecIpAddr,_A4:futOspfSecIpAddrMask,'futOspfSecIfStatus':futOspfSecIfStatus,'futOspfAreaAggregateTable':futOspfAreaAggregateTable,'futOspfAreaAggregateEntry':futOspfAreaAggregateEntry,_A5:futOspfAreaAggregateAreaID,_A6:futOspfAreaAggregateLsdbType,_A7:futOspfAreaAggregateNet,_A8:futOspfAreaAggregateMask,'futOspfAreaAggregateExternalTag':futOspfAreaAggregateExternalTag,'futOspfAsExternalAggregationTable':futOspfAsExternalAggregationTable,'futOspfAsExternalAggregationEntry':futOspfAsExternalAggregationEntry,_A9:futOspfAsExternalAggregationNet,_AA:futOspfAsExternalAggregationMask,_AB:futOspfAsExternalAggregationAreaId,'futOspfAsExternalAggregationEffect':futOspfAsExternalAggregationEffect,'futOspfAsExternalAggregationTranslation':futOspfAsExternalAggregationTranslation,'futOspfAsExternalAggregationStatus':futOspfAsExternalAggregationStatus,'futOspfOpaqueLSAGroup':futOspfOpaqueLSAGroup,'futOspfOpaqueLSAGeneralGroup':futOspfOpaqueLSAGeneralGroup,'futOspfOpaqueOption':futOspfOpaqueOption,'futOspfType11LsaCount':futOspfType11LsaCount,'futOspfType11LsaCksumSum':futOspfType11LsaCksumSum,'futOspfAreaIDValid':futOspfAreaIDValid,'futOspfOpaqueInterfaceTable':futOspfOpaqueInterfaceTable,_AU:futOspfOpaqueInterfaceEntry,'futOspfOpaqueType9LsaCount':futOspfOpaqueType9LsaCount,'futOspfOpaqueType9LsaCksumSum':futOspfOpaqueType9LsaCksumSum,'futOspfType9LsdbTable':futOspfType9LsdbTable,'futOspfType9LsdbEntry':futOspfType9LsdbEntry,_AC:futOspfType9LsdbIfIpAddress,_AD:futOspfType9LsdbOpaqueType,_AE:futOspfType9LsdbLsid,_AF:futOspfType9LsdbRouterId,'futOspfType9LsdbSequence':futOspfType9LsdbSequence,'futOspfType9LsdbAge':futOspfType9LsdbAge,'futOspfType9LsdbChecksum':futOspfType9LsdbChecksum,'futOspfType9LsdbAdvertisement':futOspfType9LsdbAdvertisement,'futOspfType11LsdbTable':futOspfType11LsdbTable,'futOspfType11LsdbEntry':futOspfType11LsdbEntry,_AG:futOspfType11LsdbOpaqueType,_AH:futOspfType11LsdbLsid,_AI:futOspfType11LsdbRouterId,'futOspfType11LsdbSequence':futOspfType11LsdbSequence,'futOspfType11LsdbAge':futOspfType11LsdbAge,'futOspfType11LsdbChecksum':futOspfType11LsdbChecksum,'futOspfType11LsdbAdvertisement':futOspfType11LsdbAdvertisement,'futOspfAppInfoDbTable':futOspfAppInfoDbTable,'futOspfAppInfoDbEntry':futOspfAppInfoDbEntry,_AJ:futOspfAppInfoDbAppid,'futOspfAppInfoDbOpaqueType':futOspfAppInfoDbOpaqueType,'futOspfAppInfoDbLsaTypesSupported':futOspfAppInfoDbLsaTypesSupported,'futOspfAppInfoDbType9Gen':futOspfAppInfoDbType9Gen,'futOspfAppInfoDbType9Rcvd':futOspfAppInfoDbType9Rcvd,'futOspfAppInfoDbType10Gen':futOspfAppInfoDbType10Gen,'futOspfAppInfoDbType10Rcvd':futOspfAppInfoDbType10Rcvd,'futOspfAppInfoDbType11Gen':futOspfAppInfoDbType11Gen,'futOspfAppInfoDbType11Rcvd':futOspfAppInfoDbType11Rcvd,'futospfRRDGroup':futospfRRDGroup,'futospfRRDGeneralGroup':futospfRRDGeneralGroup,'futOspfRRDStatus':futOspfRRDStatus,'futOspfRRDSrcProtoMaskEnable':futOspfRRDSrcProtoMaskEnable,'futOspfRRDSrcProtoMaskDisable':futOspfRRDSrcProtoMaskDisable,'futOspfRRDRouteMapEnable':futOspfRRDRouteMapEnable,'futOspfRRDRouteConfigTable':futOspfRRDRouteConfigTable,'futOspfRRDRouteConfigEntry':futOspfRRDRouteConfigEntry,_AK:futOspfRRDRouteDest,_AL:futOspfRRDRouteMask,'futOspfRRDRouteMetric':futOspfRRDRouteMetric,'futOspfRRDRouteMetricType':futOspfRRDRouteMetricType,'futOspfRRDRouteTagType':futOspfRRDRouteTagType,'futOspfRRDRouteTag':futOspfRRDRouteTag,'futOspfRRDRouteStatus':futOspfRRDRouteStatus,'futOspfVirtNbrTable':futOspfVirtNbrTable,_AV:futOspfVirtNbrEntry,_Ae:futOspfVirtNbrRestartHelperStatus,_Af:futOspfVirtNbrRestartHelperAge,_Ag:futOspfVirtNbrRestartHelperExitReason,'futospfDistInOutRouteMap':futospfDistInOutRouteMap,'futOspfDistInOutRouteMapTable':futOspfDistInOutRouteMapTable,'futOspfDistInOutRouteMapEntry':futOspfDistInOutRouteMapEntry,_AM:futOspfDistInOutRouteMapName,_AN:futOspfDistInOutRouteMapType,'futOspfDistInOutRouteMapValue':futOspfDistInOutRouteMapValue,'futOspfDistInOutRouteMapRowStatus':futOspfDistInOutRouteMapRowStatus,'futospfPreferenceGroup':futospfPreferenceGroup,'futOspfPreferenceValue':futOspfPreferenceValue,'futOspfIfAuthTable':futOspfIfAuthTable,'futOspfIfAuthEntry':futOspfIfAuthEntry,_AO:futOspfIfAuthIpAddress,_AP:futOspfIfAuthAddressLessIf,_AQ:futOspfIfAuthKeyId,'futOspfIfAuthKey':futOspfIfAuthKey,'futOspfIfAuthKeyStartAccept':futOspfIfAuthKeyStartAccept,'futOspfIfAuthKeyStartGenerate':futOspfIfAuthKeyStartGenerate,'futOspfIfAuthKeyStopGenerate':futOspfIfAuthKeyStopGenerate,'futOspfIfAuthKeyStopAccept':futOspfIfAuthKeyStopAccept,'futOspfIfAuthKeyStatus':futOspfIfAuthKeyStatus,'futOspfVirtIfAuthTable':futOspfVirtIfAuthTable,'futOspfVirtIfAuthEntry':futOspfVirtIfAuthEntry,_AR:futOspfVirtIfAuthAreaId,_AS:futOspfVirtIfAuthNeighbor,_AT:futOspfVirtIfAuthKeyId,'futOspfVirtIfAuthKey':futOspfVirtIfAuthKey,'futOspfVirtIfAuthKeyStartAccept':futOspfVirtIfAuthKeyStartAccept,'futOspfVirtIfAuthKeyStartGenerate':futOspfVirtIfAuthKeyStartGenerate,'futOspfVirtIfAuthKeyStopGenerate':futOspfVirtIfAuthKeyStopGenerate,'futOspfVirtIfAuthKeyStopAccept':futOspfVirtIfAuthKeyStopAccept,'futOspfVirtIfAuthKeyStatus':futOspfVirtIfAuthKeyStatus,'futOspfIfCryptoAuthTable':futOspfIfCryptoAuthTable,_AW:futOspfIfCryptoAuthEntry,'futOspfIfCryptoAuthType':futOspfIfCryptoAuthType,'futOspfVirtIfCryptoAuthTable':futOspfVirtIfCryptoAuthTable,_AX:futOspfVirtIfCryptoAuthEntry,'futOspfVirtIfCryptoAuthType':futOspfVirtIfCryptoAuthType,'futOspfTestGroup':futOspfTestGroup,'futOspfNotification':futOspfNotification,'futOspfTraps':futOspfTraps,'futOspfRestartStatusChange':futOspfRestartStatusChange,'futOspfNbrRestartHelperStatusChange':futOspfNbrRestartHelperStatusChange,'futOspfVirtNbrRestartHelperStatusChange':futOspfVirtNbrRestartHelperStatusChange,'futOspfHotStandbyEventTrap':futOspfHotStandbyEventTrap,'futOspfOasGroup':futOspfOasGroup})