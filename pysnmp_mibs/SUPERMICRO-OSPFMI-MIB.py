_Al='fsMIOspfDynamicBulkUpdStatus'
_Ak='fsMIOspfHotStandbyState'
_Aj='fsMIOspfVirtNbrRestartHelperExitReason'
_Ai='fsMIOspfVirtNbrRestartHelperAge'
_Ah='fsMIOspfVirtNbrRestartHelperStatus'
_Ag='fsMIOspfNbrRestartHelperExitReason'
_Af='fsMIOspfNbrRestartHelperAge'
_Ae='fsMIOspfNbrRestartHelperStatus'
_Ad='fsMIOspfRestartExitReason'
_Ac='fsMIOspfRestartInterval'
_Ab='fsMIOspfRestartStatus'
_Aa='fsMIOspfVirtNbrEntry'
_AZ='fsMIOspfRRDRouteEntry'
_AY='fsMIOspfOpaqueInterfaceEntry'
_AX='fsMIOspfOpaqueEntry'
_AW='fsMIOspfEntry'
_AV='fsMIOspfVirtIfAuthKeyId'
_AU='fsMIOspfVirtIfAuthNeighbor'
_AT='fsMIOspfVirtIfAuthAreaId'
_AS='fsMIOspfIfAuthKeyId'
_AR='fsMIOspfIfAuthAddressLessIf'
_AQ='fsMIOspfIfAuthIpAddress'
_AP='fsMIOspfDistInOutRouteMapType'
_AO='fsMIOspfDistInOutRouteMapName'
_AN='fsMIOspfRRDProtocolId'
_AM='fsMIOspfRRDRouteMask'
_AL='fsMIOspfRRDRouteDest'
_AK='fsMIOspfAppInfoDbAppid'
_AJ='fsMIOspfType11LsdbRouterId'
_AI='fsMIOspfType11LsdbLsid'
_AH='fsMIOspfType11LsdbOpaqueType'
_AG='fsMIOspfType9LsdbRouterId'
_AF='fsMIOspfType9LsdbLsid'
_AE='fsMIOspfType9LsdbOpaqueType'
_AD='fsMIOspfType9LsdbIfIpAddress'
_AC='fsMIOspfAsExternalAggregationAreaId'
_AB='fsMIOspfAsExternalAggregationMask'
_AA='fsMIOspfAsExternalAggregationNet'
_A9='fsMIOspfAreaAggregateMask'
_A8='fsMIOspfAreaAggregateNet'
_A7='fsMIOspfAreaAggregateLsdbType'
_A6='fsMIOspfAreaAggregateAreaID'
_A5='fsMIOspfSecIpAddrMask'
_A4='fsMIOspfSecIpAddr'
_A3='fsMIOspfPrimAddresslessIf'
_A2='fsMIOspfPrimIpAddr'
_A1='type2External'
_A0='type1External'
_z='fsMIOspfRouteIpNextHop'
_y='fsMIOspfRouteIpTos'
_x='fsMIOspfRouteIpAddrMask'
_w='fsMIOspfRouteIpAddr'
_v='helping'
_u='notHelping'
_t='fsMIOspfNbrAddressLessIndex'
_s='fsMIOspfNbrIpAddr'
_r='fsMIOspfVirtIfMD5AuthKeyId'
_q='fsMIOspfVirtIfMD5AuthNeighbor'
_p='fsMIOspfVirtIfMD5AuthAreaId'
_o='fsMIOspfIfMD5AuthKeyId'
_n='fsMIOspfIfMD5AuthAddressLessIf'
_m='fsMIOspfIfMD5AuthIpAddress'
_l='fsMIOspfAddressLessIf'
_k='fsMIOspfIfIpAddress'
_j='fsMIOspfHostTOS'
_i='fsMIOspfHostIpAddress'
_h='fsMIOspfAreaId'
_g='switchToRedundant'
_f='swReloadUpgrade'
_e='softwareRestart'
_d='unknown'
_c='fsMIStdOspfNbrRtrId'
_b='PositiveInteger'
_a='BigMetric'
_Z='Unsigned32'
_Y='TimeTicks'
_X='topologyChanged'
_W='timedOut'
_V='seconds'
_U='Status'
_T='DisplayString'
_S='delete'
_R='valid'
_Q='completed'
_P='inProgress'
_O='none'
_N='fsMIStdOspfRouterId'
_M='TruthValue'
_L='OctetString'
_K='read-create'
_J='disabled'
_I='enabled'
_H='fsMIStdOspfContextId'
_G='SUPERMICRO-MISTDOSPF-MIB'
_F='not-accessible'
_E='SUPERMICRO-OSPFMI-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Y,_Z,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_T,'PhysAddress','RowStatus','TextualConvention',_M)
AreaID,BigMetric,PositiveInteger,RouterID,Status,TOSType,fsMIStdOspfContextId,fsMIStdOspfEntry,fsMIStdOspfNbrRtrId,fsMIStdOspfRouterId,fsMIStdOspfVirtNbrEntry=mibBuilder.importSymbols(_G,'AreaID',_a,_b,'RouterID',_U,'TOSType',_H,'fsMIStdOspfEntry',_c,_N,'fsMIStdOspfVirtNbrEntry')
fsMIOspf=ModuleIdentity((1,3,6,1,4,1,10876,101,1,145))
if mibBuilder.loadTexts:fsMIOspf.setRevisions(('2012-09-11 00:00',))
_FsMIOspfGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfGeneralGroup=_FsMIOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,1))
_FsMIOspfGlobalTraceLevel_Type=Integer32
_FsMIOspfGlobalTraceLevel_Object=MibScalar
fsMIOspfGlobalTraceLevel=_FsMIOspfGlobalTraceLevel_Object((1,3,6,1,4,1,10876,101,1,145,1,1),_FsMIOspfGlobalTraceLevel_Type())
fsMIOspfGlobalTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfGlobalTraceLevel.setStatus(_A)
class _FsMIOspfVrfSpfInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsMIOspfVrfSpfInterval_Type.__name__=_B
_FsMIOspfVrfSpfInterval_Object=MibScalar
fsMIOspfVrfSpfInterval=_FsMIOspfVrfSpfInterval_Object((1,3,6,1,4,1,10876,101,1,145,1,2),_FsMIOspfVrfSpfInterval_Type())
fsMIOspfVrfSpfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVrfSpfInterval.setStatus(_A)
_FsMIOspfTable_Object=MibTable
fsMIOspfTable=_FsMIOspfTable_Object((1,3,6,1,4,1,10876,101,1,145,1,3))
if mibBuilder.loadTexts:fsMIOspfTable.setStatus(_A)
_FsMIOspfEntry_Object=MibTableRow
fsMIOspfEntry=_FsMIOspfEntry_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1))
if mibBuilder.loadTexts:fsMIOspfEntry.setStatus(_A)
class _FsMIOspfOverFlowState_Type(TruthValue):defaultValue=2
_FsMIOspfOverFlowState_Type.__name__=_M
_FsMIOspfOverFlowState_Object=MibTableColumn
fsMIOspfOverFlowState=_FsMIOspfOverFlowState_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,1),_FsMIOspfOverFlowState_Type())
fsMIOspfOverFlowState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfOverFlowState.setStatus(_A)
_FsMIOspfPktsRcvd_Type=Counter32
_FsMIOspfPktsRcvd_Object=MibTableColumn
fsMIOspfPktsRcvd=_FsMIOspfPktsRcvd_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,2),_FsMIOspfPktsRcvd_Type())
fsMIOspfPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfPktsRcvd.setStatus(_A)
_FsMIOspfPktsTxed_Type=Counter32
_FsMIOspfPktsTxed_Object=MibTableColumn
fsMIOspfPktsTxed=_FsMIOspfPktsTxed_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,3),_FsMIOspfPktsTxed_Type())
fsMIOspfPktsTxed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfPktsTxed.setStatus(_A)
_FsMIOspfPktsDisd_Type=Counter32
_FsMIOspfPktsDisd_Object=MibTableColumn
fsMIOspfPktsDisd=_FsMIOspfPktsDisd_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,4),_FsMIOspfPktsDisd_Type())
fsMIOspfPktsDisd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfPktsDisd.setStatus(_A)
class _FsMIOspfRFC1583Compatibility_Type(Status):defaultValue=1
_FsMIOspfRFC1583Compatibility_Type.__name__=_U
_FsMIOspfRFC1583Compatibility_Object=MibTableColumn
fsMIOspfRFC1583Compatibility=_FsMIOspfRFC1583Compatibility_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,5),_FsMIOspfRFC1583Compatibility_Type())
fsMIOspfRFC1583Compatibility.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRFC1583Compatibility.setStatus(_A)
class _FsMIOspfTraceLevel_Type(Integer32):defaultValue=2048
_FsMIOspfTraceLevel_Type.__name__=_B
_FsMIOspfTraceLevel_Object=MibTableColumn
fsMIOspfTraceLevel=_FsMIOspfTraceLevel_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,12),_FsMIOspfTraceLevel_Type())
fsMIOspfTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfTraceLevel.setStatus(_A)
class _FsMIOspfMinLsaInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIOspfMinLsaInterval_Type.__name__=_B
_FsMIOspfMinLsaInterval_Object=MibTableColumn
fsMIOspfMinLsaInterval=_FsMIOspfMinLsaInterval_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,13),_FsMIOspfMinLsaInterval_Type())
fsMIOspfMinLsaInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfMinLsaInterval.setStatus(_A)
class _FsMIOspfABRType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardABR',1),('ciscoABR',2),('ibmABR',3)))
_FsMIOspfABRType_Type.__name__=_B
_FsMIOspfABRType_Object=MibTableColumn
fsMIOspfABRType=_FsMIOspfABRType_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,14),_FsMIOspfABRType_Type())
fsMIOspfABRType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfABRType.setStatus(_A)
class _FsMIOspfNssaAsbrDefRtTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfNssaAsbrDefRtTrans_Type.__name__=_B
_FsMIOspfNssaAsbrDefRtTrans_Object=MibTableColumn
fsMIOspfNssaAsbrDefRtTrans=_FsMIOspfNssaAsbrDefRtTrans_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,15),_FsMIOspfNssaAsbrDefRtTrans_Type())
fsMIOspfNssaAsbrDefRtTrans.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfNssaAsbrDefRtTrans.setStatus(_A)
class _FsMIOspfDefaultPassiveInterface_Type(TruthValue):defaultValue=2
_FsMIOspfDefaultPassiveInterface_Type.__name__=_M
_FsMIOspfDefaultPassiveInterface_Object=MibTableColumn
fsMIOspfDefaultPassiveInterface=_FsMIOspfDefaultPassiveInterface_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,16),_FsMIOspfDefaultPassiveInterface_Type())
fsMIOspfDefaultPassiveInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfDefaultPassiveInterface.setStatus(_A)
class _FsMIOspfSpfHoldtime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfSpfHoldtime_Type.__name__=_B
_FsMIOspfSpfHoldtime_Object=MibTableColumn
fsMIOspfSpfHoldtime=_FsMIOspfSpfHoldtime_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,17),_FsMIOspfSpfHoldtime_Type())
fsMIOspfSpfHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfSpfHoldtime.setStatus(_A)
class _FsMIOspfSpfDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfSpfDelay_Type.__name__=_B
_FsMIOspfSpfDelay_Object=MibTableColumn
fsMIOspfSpfDelay=_FsMIOspfSpfDelay_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,18),_FsMIOspfSpfDelay_Type())
fsMIOspfSpfDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfSpfDelay.setStatus(_A)
class _FsMIOspfRestartSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('plannedOnly',2),('plannedAndUnplanned',3)))
_FsMIOspfRestartSupport_Type.__name__=_B
_FsMIOspfRestartSupport_Object=MibTableColumn
fsMIOspfRestartSupport=_FsMIOspfRestartSupport_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,19),_FsMIOspfRestartSupport_Type())
fsMIOspfRestartSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRestartSupport.setStatus(_A)
class _FsMIOspfRestartInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_FsMIOspfRestartInterval_Type.__name__=_B
_FsMIOspfRestartInterval_Object=MibTableColumn
fsMIOspfRestartInterval=_FsMIOspfRestartInterval_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,20),_FsMIOspfRestartInterval_Type())
fsMIOspfRestartInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRestartInterval.setStatus(_A)
class _FsMIOspfRestartStrictLsaChecking_Type(TruthValue):defaultValue=2
_FsMIOspfRestartStrictLsaChecking_Type.__name__=_M
_FsMIOspfRestartStrictLsaChecking_Object=MibTableColumn
fsMIOspfRestartStrictLsaChecking=_FsMIOspfRestartStrictLsaChecking_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,21),_FsMIOspfRestartStrictLsaChecking_Type())
fsMIOspfRestartStrictLsaChecking.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRestartStrictLsaChecking.setStatus(_A)
class _FsMIOspfRestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRestarting',1),('plannedRestart',2),('unplannedRestart',3)))
_FsMIOspfRestartStatus_Type.__name__=_B
_FsMIOspfRestartStatus_Object=MibTableColumn
fsMIOspfRestartStatus=_FsMIOspfRestartStatus_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,22),_FsMIOspfRestartStatus_Type())
fsMIOspfRestartStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRestartStatus.setStatus(_A)
_FsMIOspfRestartAge_Type=Unsigned32
_FsMIOspfRestartAge_Object=MibTableColumn
fsMIOspfRestartAge=_FsMIOspfRestartAge_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,23),_FsMIOspfRestartAge_Type())
fsMIOspfRestartAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRestartAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIOspfRestartAge.setUnits(_V)
class _FsMIOspfRestartExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_W,4),(_X,5)))
_FsMIOspfRestartExitReason_Type.__name__=_B
_FsMIOspfRestartExitReason_Object=MibTableColumn
fsMIOspfRestartExitReason=_FsMIOspfRestartExitReason_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,24),_FsMIOspfRestartExitReason_Type())
fsMIOspfRestartExitReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRestartExitReason.setStatus(_A)
class _FsMIOspfHelperSupport_Type(Bits):namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3)))
_FsMIOspfHelperSupport_Type.__name__='Bits'
_FsMIOspfHelperSupport_Object=MibTableColumn
fsMIOspfHelperSupport=_FsMIOspfHelperSupport_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,25),_FsMIOspfHelperSupport_Type())
fsMIOspfHelperSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfHelperSupport.setStatus(_A)
_FsMIOspfExtTraceLevel_Type=Integer32
_FsMIOspfExtTraceLevel_Object=MibTableColumn
fsMIOspfExtTraceLevel=_FsMIOspfExtTraceLevel_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,26),_FsMIOspfExtTraceLevel_Type())
fsMIOspfExtTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfExtTraceLevel.setStatus(_A)
class _FsMIOspfHelperGraceTimeLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_FsMIOspfHelperGraceTimeLimit_Type.__name__=_B
_FsMIOspfHelperGraceTimeLimit_Object=MibTableColumn
fsMIOspfHelperGraceTimeLimit=_FsMIOspfHelperGraceTimeLimit_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,27),_FsMIOspfHelperGraceTimeLimit_Type())
fsMIOspfHelperGraceTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfHelperGraceTimeLimit.setStatus(_A)
class _FsMIOspfRestartAckState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfRestartAckState_Type.__name__=_B
_FsMIOspfRestartAckState_Object=MibTableColumn
fsMIOspfRestartAckState=_FsMIOspfRestartAckState_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,28),_FsMIOspfRestartAckState_Type())
fsMIOspfRestartAckState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRestartAckState.setStatus(_A)
class _FsMIOspfGraceLsaRetransmitCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FsMIOspfGraceLsaRetransmitCount_Type.__name__=_B
_FsMIOspfGraceLsaRetransmitCount_Object=MibTableColumn
fsMIOspfGraceLsaRetransmitCount=_FsMIOspfGraceLsaRetransmitCount_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,29),_FsMIOspfGraceLsaRetransmitCount_Type())
fsMIOspfGraceLsaRetransmitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfGraceLsaRetransmitCount.setStatus(_A)
class _FsMIOspfRestartReason_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3)))
_FsMIOspfRestartReason_Type.__name__=_B
_FsMIOspfRestartReason_Object=MibTableColumn
fsMIOspfRestartReason=_FsMIOspfRestartReason_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,30),_FsMIOspfRestartReason_Type())
fsMIOspfRestartReason.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRestartReason.setStatus(_A)
class _FsMIOspfRTStaggeringInterval_Type(TimeTicks):defaultValue=10000
_FsMIOspfRTStaggeringInterval_Type.__name__=_Y
_FsMIOspfRTStaggeringInterval_Object=MibTableColumn
fsMIOspfRTStaggeringInterval=_FsMIOspfRTStaggeringInterval_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,31),_FsMIOspfRTStaggeringInterval_Type())
fsMIOspfRTStaggeringInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRTStaggeringInterval.setStatus(_A)
class _FsMIOspfRouterIdPermanence_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_FsMIOspfRouterIdPermanence_Type.__name__=_B
_FsMIOspfRouterIdPermanence_Object=MibTableColumn
fsMIOspfRouterIdPermanence=_FsMIOspfRouterIdPermanence_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,32),_FsMIOspfRouterIdPermanence_Type())
fsMIOspfRouterIdPermanence.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRouterIdPermanence.setStatus(_A)
class _FsMIOspfBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfBfdStatus_Type.__name__=_B
_FsMIOspfBfdStatus_Object=MibTableColumn
fsMIOspfBfdStatus=_FsMIOspfBfdStatus_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,33),_FsMIOspfBfdStatus_Type())
fsMIOspfBfdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBfdStatus.setStatus(_A)
class _FsMIOspfBfdAllIfState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfBfdAllIfState_Type.__name__=_B
_FsMIOspfBfdAllIfState_Object=MibTableColumn
fsMIOspfBfdAllIfState=_FsMIOspfBfdAllIfState_Object((1,3,6,1,4,1,10876,101,1,145,1,3,1,34),_FsMIOspfBfdAllIfState_Type())
fsMIOspfBfdAllIfState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBfdAllIfState.setStatus(_A)
class _FsMIOspfRTStaggeringStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfRTStaggeringStatus_Type.__name__=_B
_FsMIOspfRTStaggeringStatus_Object=MibScalar
fsMIOspfRTStaggeringStatus=_FsMIOspfRTStaggeringStatus_Object((1,3,6,1,4,1,10876,101,1,145,1,4),_FsMIOspfRTStaggeringStatus_Type())
fsMIOspfRTStaggeringStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRTStaggeringStatus.setStatus(_A)
class _FsMIOspfHotStandbyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfHotStandbyAdminStatus_Type.__name__=_B
_FsMIOspfHotStandbyAdminStatus_Object=MibScalar
fsMIOspfHotStandbyAdminStatus=_FsMIOspfHotStandbyAdminStatus_Object((1,3,6,1,4,1,10876,101,1,145,1,5),_FsMIOspfHotStandbyAdminStatus_Type())
fsMIOspfHotStandbyAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfHotStandbyAdminStatus.setStatus(_A)
class _FsMIOspfHotStandbyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FsMIOspfHotStandbyState_Type.__name__=_B
_FsMIOspfHotStandbyState_Object=MibScalar
fsMIOspfHotStandbyState=_FsMIOspfHotStandbyState_Object((1,3,6,1,4,1,10876,101,1,145,1,6),_FsMIOspfHotStandbyState_Type())
fsMIOspfHotStandbyState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfHotStandbyState.setStatus(_A)
class _FsMIOspfDynamicBulkUpdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),(_P,2),(_Q,3),('aborted',4)))
_FsMIOspfDynamicBulkUpdStatus_Type.__name__=_B
_FsMIOspfDynamicBulkUpdStatus_Object=MibScalar
fsMIOspfDynamicBulkUpdStatus=_FsMIOspfDynamicBulkUpdStatus_Object((1,3,6,1,4,1,10876,101,1,145,1,7),_FsMIOspfDynamicBulkUpdStatus_Type())
fsMIOspfDynamicBulkUpdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfDynamicBulkUpdStatus.setStatus(_A)
_FsMIOspfStanbyHelloSyncCount_Type=Counter32
_FsMIOspfStanbyHelloSyncCount_Object=MibScalar
fsMIOspfStanbyHelloSyncCount=_FsMIOspfStanbyHelloSyncCount_Object((1,3,6,1,4,1,10876,101,1,145,1,8),_FsMIOspfStanbyHelloSyncCount_Type())
fsMIOspfStanbyHelloSyncCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfStanbyHelloSyncCount.setStatus(_A)
_FsMIOspfStanbyLsaSyncCount_Type=Counter32
_FsMIOspfStanbyLsaSyncCount_Object=MibScalar
fsMIOspfStanbyLsaSyncCount=_FsMIOspfStanbyLsaSyncCount_Object((1,3,6,1,4,1,10876,101,1,145,1,9),_FsMIOspfStanbyLsaSyncCount_Type())
fsMIOspfStanbyLsaSyncCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfStanbyLsaSyncCount.setStatus(_A)
_FsMIOspfGlobalExtTraceLevel_Type=Integer32
_FsMIOspfGlobalExtTraceLevel_Object=MibScalar
fsMIOspfGlobalExtTraceLevel=_FsMIOspfGlobalExtTraceLevel_Object((1,3,6,1,4,1,10876,101,1,145,1,10),_FsMIOspfGlobalExtTraceLevel_Type())
fsMIOspfGlobalExtTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfGlobalExtTraceLevel.setStatus(_A)
_FsMIOspfAreaTable_Object=MibTable
fsMIOspfAreaTable=_FsMIOspfAreaTable_Object((1,3,6,1,4,1,10876,101,1,145,2))
if mibBuilder.loadTexts:fsMIOspfAreaTable.setStatus(_A)
_FsMIOspfAreaEntry_Object=MibTableRow
fsMIOspfAreaEntry=_FsMIOspfAreaEntry_Object((1,3,6,1,4,1,10876,101,1,145,2,1))
fsMIOspfAreaEntry.setIndexNames((0,_G,_H),(0,_E,_h))
if mibBuilder.loadTexts:fsMIOspfAreaEntry.setStatus(_A)
_FsMIOspfAreaId_Type=AreaID
_FsMIOspfAreaId_Object=MibTableColumn
fsMIOspfAreaId=_FsMIOspfAreaId_Object((1,3,6,1,4,1,10876,101,1,145,2,1,1),_FsMIOspfAreaId_Type())
fsMIOspfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAreaId.setStatus(_A)
_FsMIOspfAreaIfCount_Type=Gauge32
_FsMIOspfAreaIfCount_Object=MibTableColumn
fsMIOspfAreaIfCount=_FsMIOspfAreaIfCount_Object((1,3,6,1,4,1,10876,101,1,145,2,1,2),_FsMIOspfAreaIfCount_Type())
fsMIOspfAreaIfCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAreaIfCount.setStatus(_A)
_FsMIOspfAreaNetCount_Type=Gauge32
_FsMIOspfAreaNetCount_Object=MibTableColumn
fsMIOspfAreaNetCount=_FsMIOspfAreaNetCount_Object((1,3,6,1,4,1,10876,101,1,145,2,1,3),_FsMIOspfAreaNetCount_Type())
fsMIOspfAreaNetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAreaNetCount.setStatus(_A)
_FsMIOspfAreaRtrCount_Type=Gauge32
_FsMIOspfAreaRtrCount_Object=MibTableColumn
fsMIOspfAreaRtrCount=_FsMIOspfAreaRtrCount_Object((1,3,6,1,4,1,10876,101,1,145,2,1,4),_FsMIOspfAreaRtrCount_Type())
fsMIOspfAreaRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAreaRtrCount.setStatus(_A)
class _FsMIOspfAreaNSSATranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_FsMIOspfAreaNSSATranslatorRole_Type.__name__=_B
_FsMIOspfAreaNSSATranslatorRole_Object=MibTableColumn
fsMIOspfAreaNSSATranslatorRole=_FsMIOspfAreaNSSATranslatorRole_Object((1,3,6,1,4,1,10876,101,1,145,2,1,5),_FsMIOspfAreaNSSATranslatorRole_Type())
fsMIOspfAreaNSSATranslatorRole.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAreaNSSATranslatorRole.setStatus(_A)
class _FsMIOspfAreaNSSATranslatorState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('elected',2),(_J,3)))
_FsMIOspfAreaNSSATranslatorState_Type.__name__=_B
_FsMIOspfAreaNSSATranslatorState_Object=MibTableColumn
fsMIOspfAreaNSSATranslatorState=_FsMIOspfAreaNSSATranslatorState_Object((1,3,6,1,4,1,10876,101,1,145,2,1,6),_FsMIOspfAreaNSSATranslatorState_Type())
fsMIOspfAreaNSSATranslatorState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAreaNSSATranslatorState.setStatus(_A)
class _FsMIOspfAreaNSSATranslatorStabilityInterval_Type(PositiveInteger):defaultValue=40
_FsMIOspfAreaNSSATranslatorStabilityInterval_Type.__name__=_b
_FsMIOspfAreaNSSATranslatorStabilityInterval_Object=MibTableColumn
fsMIOspfAreaNSSATranslatorStabilityInterval=_FsMIOspfAreaNSSATranslatorStabilityInterval_Object((1,3,6,1,4,1,10876,101,1,145,2,1,7),_FsMIOspfAreaNSSATranslatorStabilityInterval_Type())
fsMIOspfAreaNSSATranslatorStabilityInterval.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAreaNSSATranslatorStabilityInterval.setStatus(_A)
_FsMIOspfAreaNSSATranslatorEvents_Type=Counter32
_FsMIOspfAreaNSSATranslatorEvents_Object=MibTableColumn
fsMIOspfAreaNSSATranslatorEvents=_FsMIOspfAreaNSSATranslatorEvents_Object((1,3,6,1,4,1,10876,101,1,145,2,1,8),_FsMIOspfAreaNSSATranslatorEvents_Type())
fsMIOspfAreaNSSATranslatorEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAreaNSSATranslatorEvents.setStatus(_A)
class _FsMIOspfAreaDfInfOriginate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfAreaDfInfOriginate_Type.__name__=_B
_FsMIOspfAreaDfInfOriginate_Object=MibTableColumn
fsMIOspfAreaDfInfOriginate=_FsMIOspfAreaDfInfOriginate_Object((1,3,6,1,4,1,10876,101,1,145,2,1,9),_FsMIOspfAreaDfInfOriginate_Type())
fsMIOspfAreaDfInfOriginate.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAreaDfInfOriginate.setStatus(_A)
_FsMIOspfHostTable_Object=MibTable
fsMIOspfHostTable=_FsMIOspfHostTable_Object((1,3,6,1,4,1,10876,101,1,145,3))
if mibBuilder.loadTexts:fsMIOspfHostTable.setStatus(_A)
_FsMIOspfHostEntry_Object=MibTableRow
fsMIOspfHostEntry=_FsMIOspfHostEntry_Object((1,3,6,1,4,1,10876,101,1,145,3,1))
fsMIOspfHostEntry.setIndexNames((0,_G,_H),(0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:fsMIOspfHostEntry.setStatus(_A)
_FsMIOspfHostIpAddress_Type=IpAddress
_FsMIOspfHostIpAddress_Object=MibTableColumn
fsMIOspfHostIpAddress=_FsMIOspfHostIpAddress_Object((1,3,6,1,4,1,10876,101,1,145,3,1,1),_FsMIOspfHostIpAddress_Type())
fsMIOspfHostIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfHostIpAddress.setStatus(_A)
_FsMIOspfHostTOS_Type=TOSType
_FsMIOspfHostTOS_Object=MibTableColumn
fsMIOspfHostTOS=_FsMIOspfHostTOS_Object((1,3,6,1,4,1,10876,101,1,145,3,1,2),_FsMIOspfHostTOS_Type())
fsMIOspfHostTOS.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfHostTOS.setStatus(_A)
class _FsMIOspfHostRouteIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfHostRouteIfIndex_Type.__name__=_B
_FsMIOspfHostRouteIfIndex_Object=MibTableColumn
fsMIOspfHostRouteIfIndex=_FsMIOspfHostRouteIfIndex_Object((1,3,6,1,4,1,10876,101,1,145,3,1,3),_FsMIOspfHostRouteIfIndex_Type())
fsMIOspfHostRouteIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfHostRouteIfIndex.setStatus(_A)
_FsMIOspfIfTable_Object=MibTable
fsMIOspfIfTable=_FsMIOspfIfTable_Object((1,3,6,1,4,1,10876,101,1,145,4))
if mibBuilder.loadTexts:fsMIOspfIfTable.setStatus(_A)
_FsMIOspfIfEntry_Object=MibTableRow
fsMIOspfIfEntry=_FsMIOspfIfEntry_Object((1,3,6,1,4,1,10876,101,1,145,4,1))
fsMIOspfIfEntry.setIndexNames((0,_G,_H),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:fsMIOspfIfEntry.setStatus(_A)
_FsMIOspfIfIpAddress_Type=IpAddress
_FsMIOspfIfIpAddress_Object=MibTableColumn
fsMIOspfIfIpAddress=_FsMIOspfIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,145,4,1,1),_FsMIOspfIfIpAddress_Type())
fsMIOspfIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfIpAddress.setStatus(_A)
class _FsMIOspfAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfAddressLessIf_Type.__name__=_B
_FsMIOspfAddressLessIf_Object=MibTableColumn
fsMIOspfAddressLessIf=_FsMIOspfAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,145,4,1,2),_FsMIOspfAddressLessIf_Type())
fsMIOspfAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAddressLessIf.setStatus(_A)
class _FsMIOspfIfOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operup',1),('operdown',2),('loopback',3),('unloop',4)))
_FsMIOspfIfOperState_Type.__name__=_B
_FsMIOspfIfOperState_Object=MibTableColumn
fsMIOspfIfOperState=_FsMIOspfIfOperState_Object((1,3,6,1,4,1,10876,101,1,145,4,1,3),_FsMIOspfIfOperState_Type())
fsMIOspfIfOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfOperState.setStatus(_A)
class _FsMIOspfIfPassive_Type(TruthValue):defaultValue=2
_FsMIOspfIfPassive_Type.__name__=_M
_FsMIOspfIfPassive_Object=MibTableColumn
fsMIOspfIfPassive=_FsMIOspfIfPassive_Object((1,3,6,1,4,1,10876,101,1,145,4,1,4),_FsMIOspfIfPassive_Type())
fsMIOspfIfPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfPassive.setStatus(_A)
_FsMIOspfIfNbrCount_Type=Gauge32
_FsMIOspfIfNbrCount_Object=MibTableColumn
fsMIOspfIfNbrCount=_FsMIOspfIfNbrCount_Object((1,3,6,1,4,1,10876,101,1,145,4,1,5),_FsMIOspfIfNbrCount_Type())
fsMIOspfIfNbrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfNbrCount.setStatus(_A)
_FsMIOspfIfAdjCount_Type=Gauge32
_FsMIOspfIfAdjCount_Object=MibTableColumn
fsMIOspfIfAdjCount=_FsMIOspfIfAdjCount_Object((1,3,6,1,4,1,10876,101,1,145,4,1,6),_FsMIOspfIfAdjCount_Type())
fsMIOspfIfAdjCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfAdjCount.setStatus(_A)
_FsMIOspfIfHelloRcvd_Type=Counter32
_FsMIOspfIfHelloRcvd_Object=MibTableColumn
fsMIOspfIfHelloRcvd=_FsMIOspfIfHelloRcvd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,7),_FsMIOspfIfHelloRcvd_Type())
fsMIOspfIfHelloRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfHelloRcvd.setStatus(_A)
_FsMIOspfIfHelloTxed_Type=Counter32
_FsMIOspfIfHelloTxed_Object=MibTableColumn
fsMIOspfIfHelloTxed=_FsMIOspfIfHelloTxed_Object((1,3,6,1,4,1,10876,101,1,145,4,1,8),_FsMIOspfIfHelloTxed_Type())
fsMIOspfIfHelloTxed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfHelloTxed.setStatus(_A)
_FsMIOspfIfHelloDisd_Type=Counter32
_FsMIOspfIfHelloDisd_Object=MibTableColumn
fsMIOspfIfHelloDisd=_FsMIOspfIfHelloDisd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,9),_FsMIOspfIfHelloDisd_Type())
fsMIOspfIfHelloDisd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfHelloDisd.setStatus(_A)
_FsMIOspfIfDdpRcvd_Type=Counter32
_FsMIOspfIfDdpRcvd_Object=MibTableColumn
fsMIOspfIfDdpRcvd=_FsMIOspfIfDdpRcvd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,10),_FsMIOspfIfDdpRcvd_Type())
fsMIOspfIfDdpRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfDdpRcvd.setStatus(_A)
_FsMIOspfIfDdpTxed_Type=Counter32
_FsMIOspfIfDdpTxed_Object=MibTableColumn
fsMIOspfIfDdpTxed=_FsMIOspfIfDdpTxed_Object((1,3,6,1,4,1,10876,101,1,145,4,1,11),_FsMIOspfIfDdpTxed_Type())
fsMIOspfIfDdpTxed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfDdpTxed.setStatus(_A)
_FsMIOspfIfDdpDisd_Type=Counter32
_FsMIOspfIfDdpDisd_Object=MibTableColumn
fsMIOspfIfDdpDisd=_FsMIOspfIfDdpDisd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,12),_FsMIOspfIfDdpDisd_Type())
fsMIOspfIfDdpDisd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfDdpDisd.setStatus(_A)
_FsMIOspfIfLrqRcvd_Type=Counter32
_FsMIOspfIfLrqRcvd_Object=MibTableColumn
fsMIOspfIfLrqRcvd=_FsMIOspfIfLrqRcvd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,13),_FsMIOspfIfLrqRcvd_Type())
fsMIOspfIfLrqRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLrqRcvd.setStatus(_A)
_FsMIOspfIfLrqTxed_Type=Counter32
_FsMIOspfIfLrqTxed_Object=MibTableColumn
fsMIOspfIfLrqTxed=_FsMIOspfIfLrqTxed_Object((1,3,6,1,4,1,10876,101,1,145,4,1,14),_FsMIOspfIfLrqTxed_Type())
fsMIOspfIfLrqTxed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLrqTxed.setStatus(_A)
_FsMIOspfIfLrqDisd_Type=Counter32
_FsMIOspfIfLrqDisd_Object=MibTableColumn
fsMIOspfIfLrqDisd=_FsMIOspfIfLrqDisd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,15),_FsMIOspfIfLrqDisd_Type())
fsMIOspfIfLrqDisd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLrqDisd.setStatus(_A)
_FsMIOspfIfLsuRcvd_Type=Counter32
_FsMIOspfIfLsuRcvd_Object=MibTableColumn
fsMIOspfIfLsuRcvd=_FsMIOspfIfLsuRcvd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,16),_FsMIOspfIfLsuRcvd_Type())
fsMIOspfIfLsuRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLsuRcvd.setStatus(_A)
_FsMIOspfIfLsuTxed_Type=Counter32
_FsMIOspfIfLsuTxed_Object=MibTableColumn
fsMIOspfIfLsuTxed=_FsMIOspfIfLsuTxed_Object((1,3,6,1,4,1,10876,101,1,145,4,1,17),_FsMIOspfIfLsuTxed_Type())
fsMIOspfIfLsuTxed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLsuTxed.setStatus(_A)
_FsMIOspfIfLsuDisd_Type=Counter32
_FsMIOspfIfLsuDisd_Object=MibTableColumn
fsMIOspfIfLsuDisd=_FsMIOspfIfLsuDisd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,18),_FsMIOspfIfLsuDisd_Type())
fsMIOspfIfLsuDisd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLsuDisd.setStatus(_A)
_FsMIOspfIfLakRcvd_Type=Counter32
_FsMIOspfIfLakRcvd_Object=MibTableColumn
fsMIOspfIfLakRcvd=_FsMIOspfIfLakRcvd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,19),_FsMIOspfIfLakRcvd_Type())
fsMIOspfIfLakRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLakRcvd.setStatus(_A)
_FsMIOspfIfLakTxed_Type=Counter32
_FsMIOspfIfLakTxed_Object=MibTableColumn
fsMIOspfIfLakTxed=_FsMIOspfIfLakTxed_Object((1,3,6,1,4,1,10876,101,1,145,4,1,20),_FsMIOspfIfLakTxed_Type())
fsMIOspfIfLakTxed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLakTxed.setStatus(_A)
_FsMIOspfIfLakDisd_Type=Counter32
_FsMIOspfIfLakDisd_Object=MibTableColumn
fsMIOspfIfLakDisd=_FsMIOspfIfLakDisd_Object((1,3,6,1,4,1,10876,101,1,145,4,1,21),_FsMIOspfIfLakDisd_Type())
fsMIOspfIfLakDisd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfIfLakDisd.setStatus(_A)
class _FsMIOspfIfBfdState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfIfBfdState_Type.__name__=_B
_FsMIOspfIfBfdState_Object=MibTableColumn
fsMIOspfIfBfdState=_FsMIOspfIfBfdState_Object((1,3,6,1,4,1,10876,101,1,145,4,1,22),_FsMIOspfIfBfdState_Type())
fsMIOspfIfBfdState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfBfdState.setStatus(_A)
_FsMIOspfIfMD5AuthTable_Object=MibTable
fsMIOspfIfMD5AuthTable=_FsMIOspfIfMD5AuthTable_Object((1,3,6,1,4,1,10876,101,1,145,5))
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthTable.setStatus(_A)
_FsMIOspfIfMD5AuthEntry_Object=MibTableRow
fsMIOspfIfMD5AuthEntry=_FsMIOspfIfMD5AuthEntry_Object((1,3,6,1,4,1,10876,101,1,145,5,1))
fsMIOspfIfMD5AuthEntry.setIndexNames((0,_G,_H),(0,_E,_m),(0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthEntry.setStatus(_A)
_FsMIOspfIfMD5AuthIpAddress_Type=IpAddress
_FsMIOspfIfMD5AuthIpAddress_Object=MibTableColumn
fsMIOspfIfMD5AuthIpAddress=_FsMIOspfIfMD5AuthIpAddress_Object((1,3,6,1,4,1,10876,101,1,145,5,1,1),_FsMIOspfIfMD5AuthIpAddress_Type())
fsMIOspfIfMD5AuthIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthIpAddress.setStatus(_A)
class _FsMIOspfIfMD5AuthAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfIfMD5AuthAddressLessIf_Type.__name__=_B
_FsMIOspfIfMD5AuthAddressLessIf_Object=MibTableColumn
fsMIOspfIfMD5AuthAddressLessIf=_FsMIOspfIfMD5AuthAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,145,5,1,2),_FsMIOspfIfMD5AuthAddressLessIf_Type())
fsMIOspfIfMD5AuthAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthAddressLessIf.setStatus(_A)
class _FsMIOspfIfMD5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfIfMD5AuthKeyId_Type.__name__=_B
_FsMIOspfIfMD5AuthKeyId_Object=MibTableColumn
fsMIOspfIfMD5AuthKeyId=_FsMIOspfIfMD5AuthKeyId_Object((1,3,6,1,4,1,10876,101,1,145,5,1,3),_FsMIOspfIfMD5AuthKeyId_Type())
fsMIOspfIfMD5AuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKeyId.setStatus(_A)
class _FsMIOspfIfMD5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIOspfIfMD5AuthKey_Type.__name__=_L
_FsMIOspfIfMD5AuthKey_Object=MibTableColumn
fsMIOspfIfMD5AuthKey=_FsMIOspfIfMD5AuthKey_Object((1,3,6,1,4,1,10876,101,1,145,5,1,4),_FsMIOspfIfMD5AuthKey_Type())
fsMIOspfIfMD5AuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKey.setStatus(_A)
class _FsMIOspfIfMD5AuthKeyStartAccept_Type(Integer32):defaultValue=0
_FsMIOspfIfMD5AuthKeyStartAccept_Type.__name__=_B
_FsMIOspfIfMD5AuthKeyStartAccept_Object=MibTableColumn
fsMIOspfIfMD5AuthKeyStartAccept=_FsMIOspfIfMD5AuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,145,5,1,5),_FsMIOspfIfMD5AuthKeyStartAccept_Type())
fsMIOspfIfMD5AuthKeyStartAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKeyStartAccept.setStatus(_A)
class _FsMIOspfIfMD5AuthKeyStartGenerate_Type(Integer32):defaultValue=0
_FsMIOspfIfMD5AuthKeyStartGenerate_Type.__name__=_B
_FsMIOspfIfMD5AuthKeyStartGenerate_Object=MibTableColumn
fsMIOspfIfMD5AuthKeyStartGenerate=_FsMIOspfIfMD5AuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,145,5,1,6),_FsMIOspfIfMD5AuthKeyStartGenerate_Type())
fsMIOspfIfMD5AuthKeyStartGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKeyStartGenerate.setStatus(_A)
class _FsMIOspfIfMD5AuthKeyStopGenerate_Type(Integer32):defaultValue=-1
_FsMIOspfIfMD5AuthKeyStopGenerate_Type.__name__=_B
_FsMIOspfIfMD5AuthKeyStopGenerate_Object=MibTableColumn
fsMIOspfIfMD5AuthKeyStopGenerate=_FsMIOspfIfMD5AuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,145,5,1,7),_FsMIOspfIfMD5AuthKeyStopGenerate_Type())
fsMIOspfIfMD5AuthKeyStopGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKeyStopGenerate.setStatus(_A)
class _FsMIOspfIfMD5AuthKeyStopAccept_Type(Integer32):defaultValue=-1
_FsMIOspfIfMD5AuthKeyStopAccept_Type.__name__=_B
_FsMIOspfIfMD5AuthKeyStopAccept_Object=MibTableColumn
fsMIOspfIfMD5AuthKeyStopAccept=_FsMIOspfIfMD5AuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,145,5,1,8),_FsMIOspfIfMD5AuthKeyStopAccept_Type())
fsMIOspfIfMD5AuthKeyStopAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKeyStopAccept.setStatus(_A)
class _FsMIOspfIfMD5AuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_R,1),(_S,3)))
_FsMIOspfIfMD5AuthKeyStatus_Type.__name__=_B
_FsMIOspfIfMD5AuthKeyStatus_Object=MibTableColumn
fsMIOspfIfMD5AuthKeyStatus=_FsMIOspfIfMD5AuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,145,5,1,9),_FsMIOspfIfMD5AuthKeyStatus_Type())
fsMIOspfIfMD5AuthKeyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfMD5AuthKeyStatus.setStatus(_A)
_FsMIOspfVirtIfMD5AuthTable_Object=MibTable
fsMIOspfVirtIfMD5AuthTable=_FsMIOspfVirtIfMD5AuthTable_Object((1,3,6,1,4,1,10876,101,1,145,6))
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthTable.setStatus(_A)
_FsMIOspfVirtIfMD5AuthEntry_Object=MibTableRow
fsMIOspfVirtIfMD5AuthEntry=_FsMIOspfVirtIfMD5AuthEntry_Object((1,3,6,1,4,1,10876,101,1,145,6,1))
fsMIOspfVirtIfMD5AuthEntry.setIndexNames((0,_G,_H),(0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthEntry.setStatus(_A)
_FsMIOspfVirtIfMD5AuthAreaId_Type=AreaID
_FsMIOspfVirtIfMD5AuthAreaId_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthAreaId=_FsMIOspfVirtIfMD5AuthAreaId_Object((1,3,6,1,4,1,10876,101,1,145,6,1,1),_FsMIOspfVirtIfMD5AuthAreaId_Type())
fsMIOspfVirtIfMD5AuthAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthAreaId.setStatus(_A)
_FsMIOspfVirtIfMD5AuthNeighbor_Type=RouterID
_FsMIOspfVirtIfMD5AuthNeighbor_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthNeighbor=_FsMIOspfVirtIfMD5AuthNeighbor_Object((1,3,6,1,4,1,10876,101,1,145,6,1,2),_FsMIOspfVirtIfMD5AuthNeighbor_Type())
fsMIOspfVirtIfMD5AuthNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthNeighbor.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfVirtIfMD5AuthKeyId_Type.__name__=_B
_FsMIOspfVirtIfMD5AuthKeyId_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKeyId=_FsMIOspfVirtIfMD5AuthKeyId_Object((1,3,6,1,4,1,10876,101,1,145,6,1,3),_FsMIOspfVirtIfMD5AuthKeyId_Type())
fsMIOspfVirtIfMD5AuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKeyId.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIOspfVirtIfMD5AuthKey_Type.__name__=_L
_FsMIOspfVirtIfMD5AuthKey_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKey=_FsMIOspfVirtIfMD5AuthKey_Object((1,3,6,1,4,1,10876,101,1,145,6,1,4),_FsMIOspfVirtIfMD5AuthKey_Type())
fsMIOspfVirtIfMD5AuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKey.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKeyStartAccept_Type(Integer32):defaultValue=0
_FsMIOspfVirtIfMD5AuthKeyStartAccept_Type.__name__=_B
_FsMIOspfVirtIfMD5AuthKeyStartAccept_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStartAccept=_FsMIOspfVirtIfMD5AuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,145,6,1,5),_FsMIOspfVirtIfMD5AuthKeyStartAccept_Type())
fsMIOspfVirtIfMD5AuthKeyStartAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKeyStartAccept.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKeyStartGenerate_Type(Integer32):defaultValue=0
_FsMIOspfVirtIfMD5AuthKeyStartGenerate_Type.__name__=_B
_FsMIOspfVirtIfMD5AuthKeyStartGenerate_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStartGenerate=_FsMIOspfVirtIfMD5AuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,145,6,1,6),_FsMIOspfVirtIfMD5AuthKeyStartGenerate_Type())
fsMIOspfVirtIfMD5AuthKeyStartGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKeyStartGenerate.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKeyStopGenerate_Type(Integer32):defaultValue=-1
_FsMIOspfVirtIfMD5AuthKeyStopGenerate_Type.__name__=_B
_FsMIOspfVirtIfMD5AuthKeyStopGenerate_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStopGenerate=_FsMIOspfVirtIfMD5AuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,145,6,1,7),_FsMIOspfVirtIfMD5AuthKeyStopGenerate_Type())
fsMIOspfVirtIfMD5AuthKeyStopGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKeyStopGenerate.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKeyStopAccept_Type(Integer32):defaultValue=-1
_FsMIOspfVirtIfMD5AuthKeyStopAccept_Type.__name__=_B
_FsMIOspfVirtIfMD5AuthKeyStopAccept_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStopAccept=_FsMIOspfVirtIfMD5AuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,145,6,1,8),_FsMIOspfVirtIfMD5AuthKeyStopAccept_Type())
fsMIOspfVirtIfMD5AuthKeyStopAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKeyStopAccept.setStatus(_A)
class _FsMIOspfVirtIfMD5AuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_R,1),(_S,3)))
_FsMIOspfVirtIfMD5AuthKeyStatus_Type.__name__=_B
_FsMIOspfVirtIfMD5AuthKeyStatus_Object=MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStatus=_FsMIOspfVirtIfMD5AuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,145,6,1,9),_FsMIOspfVirtIfMD5AuthKeyStatus_Type())
fsMIOspfVirtIfMD5AuthKeyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfMD5AuthKeyStatus.setStatus(_A)
_FsMIOspfNbrTable_Object=MibTable
fsMIOspfNbrTable=_FsMIOspfNbrTable_Object((1,3,6,1,4,1,10876,101,1,145,7))
if mibBuilder.loadTexts:fsMIOspfNbrTable.setStatus(_A)
_FsMIOspfNbrEntry_Object=MibTableRow
fsMIOspfNbrEntry=_FsMIOspfNbrEntry_Object((1,3,6,1,4,1,10876,101,1,145,7,1))
fsMIOspfNbrEntry.setIndexNames((0,_G,_H),(0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:fsMIOspfNbrEntry.setStatus(_A)
_FsMIOspfNbrIpAddr_Type=IpAddress
_FsMIOspfNbrIpAddr_Object=MibTableColumn
fsMIOspfNbrIpAddr=_FsMIOspfNbrIpAddr_Object((1,3,6,1,4,1,10876,101,1,145,7,1,1),_FsMIOspfNbrIpAddr_Type())
fsMIOspfNbrIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfNbrIpAddr.setStatus(_A)
class _FsMIOspfNbrAddressLessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfNbrAddressLessIndex_Type.__name__=_B
_FsMIOspfNbrAddressLessIndex_Object=MibTableColumn
fsMIOspfNbrAddressLessIndex=_FsMIOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,10876,101,1,145,7,1,2),_FsMIOspfNbrAddressLessIndex_Type())
fsMIOspfNbrAddressLessIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfNbrAddressLessIndex.setStatus(_A)
_FsMIOspfNbrDBSummaryQLen_Type=Gauge32
_FsMIOspfNbrDBSummaryQLen_Object=MibTableColumn
fsMIOspfNbrDBSummaryQLen=_FsMIOspfNbrDBSummaryQLen_Object((1,3,6,1,4,1,10876,101,1,145,7,1,3),_FsMIOspfNbrDBSummaryQLen_Type())
fsMIOspfNbrDBSummaryQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfNbrDBSummaryQLen.setStatus(_A)
_FsMIOspfNbrLSReqQLen_Type=Gauge32
_FsMIOspfNbrLSReqQLen_Object=MibTableColumn
fsMIOspfNbrLSReqQLen=_FsMIOspfNbrLSReqQLen_Object((1,3,6,1,4,1,10876,101,1,145,7,1,4),_FsMIOspfNbrLSReqQLen_Type())
fsMIOspfNbrLSReqQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfNbrLSReqQLen.setStatus(_A)
class _FsMIOspfNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),(_v,2)))
_FsMIOspfNbrRestartHelperStatus_Type.__name__=_B
_FsMIOspfNbrRestartHelperStatus_Object=MibTableColumn
fsMIOspfNbrRestartHelperStatus=_FsMIOspfNbrRestartHelperStatus_Object((1,3,6,1,4,1,10876,101,1,145,7,1,5),_FsMIOspfNbrRestartHelperStatus_Type())
fsMIOspfNbrRestartHelperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfNbrRestartHelperStatus.setStatus(_A)
_FsMIOspfNbrRestartHelperAge_Type=Unsigned32
_FsMIOspfNbrRestartHelperAge_Object=MibTableColumn
fsMIOspfNbrRestartHelperAge=_FsMIOspfNbrRestartHelperAge_Object((1,3,6,1,4,1,10876,101,1,145,7,1,6),_FsMIOspfNbrRestartHelperAge_Type())
fsMIOspfNbrRestartHelperAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIOspfNbrRestartHelperAge.setUnits(_V)
class _FsMIOspfNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_W,4),(_X,5)))
_FsMIOspfNbrRestartHelperExitReason_Type.__name__=_B
_FsMIOspfNbrRestartHelperExitReason_Object=MibTableColumn
fsMIOspfNbrRestartHelperExitReason=_FsMIOspfNbrRestartHelperExitReason_Object((1,3,6,1,4,1,10876,101,1,145,7,1,7),_FsMIOspfNbrRestartHelperExitReason_Type())
fsMIOspfNbrRestartHelperExitReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfNbrRestartHelperExitReason.setStatus(_A)
class _FsMIOspfNbrBfdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfNbrBfdState_Type.__name__=_B
_FsMIOspfNbrBfdState_Object=MibTableColumn
fsMIOspfNbrBfdState=_FsMIOspfNbrBfdState_Object((1,3,6,1,4,1,10876,101,1,145,7,1,8),_FsMIOspfNbrBfdState_Type())
fsMIOspfNbrBfdState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfNbrBfdState.setStatus(_A)
_FsMIOspfRoutingTable_Object=MibTable
fsMIOspfRoutingTable=_FsMIOspfRoutingTable_Object((1,3,6,1,4,1,10876,101,1,145,8))
if mibBuilder.loadTexts:fsMIOspfRoutingTable.setStatus(_A)
_FsMIOspfRoutingEntry_Object=MibTableRow
fsMIOspfRoutingEntry=_FsMIOspfRoutingEntry_Object((1,3,6,1,4,1,10876,101,1,145,8,1))
fsMIOspfRoutingEntry.setIndexNames((0,_G,_H),(0,_E,_w),(0,_E,_x),(0,_E,_y),(0,_E,_z))
if mibBuilder.loadTexts:fsMIOspfRoutingEntry.setStatus(_A)
_FsMIOspfRouteIpAddr_Type=IpAddress
_FsMIOspfRouteIpAddr_Object=MibTableColumn
fsMIOspfRouteIpAddr=_FsMIOspfRouteIpAddr_Object((1,3,6,1,4,1,10876,101,1,145,8,1,1),_FsMIOspfRouteIpAddr_Type())
fsMIOspfRouteIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRouteIpAddr.setStatus(_A)
_FsMIOspfRouteIpAddrMask_Type=IpAddress
_FsMIOspfRouteIpAddrMask_Object=MibTableColumn
fsMIOspfRouteIpAddrMask=_FsMIOspfRouteIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,145,8,1,2),_FsMIOspfRouteIpAddrMask_Type())
fsMIOspfRouteIpAddrMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRouteIpAddrMask.setStatus(_A)
_FsMIOspfRouteIpTos_Type=TOSType
_FsMIOspfRouteIpTos_Object=MibTableColumn
fsMIOspfRouteIpTos=_FsMIOspfRouteIpTos_Object((1,3,6,1,4,1,10876,101,1,145,8,1,3),_FsMIOspfRouteIpTos_Type())
fsMIOspfRouteIpTos.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRouteIpTos.setStatus(_A)
_FsMIOspfRouteIpNextHop_Type=IpAddress
_FsMIOspfRouteIpNextHop_Object=MibTableColumn
fsMIOspfRouteIpNextHop=_FsMIOspfRouteIpNextHop_Object((1,3,6,1,4,1,10876,101,1,145,8,1,4),_FsMIOspfRouteIpNextHop_Type())
fsMIOspfRouteIpNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRouteIpNextHop.setStatus(_A)
class _FsMIOspfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('intraArea',1),('interArea',2),(_A0,3),(_A1,4)))
_FsMIOspfRouteType_Type.__name__=_B
_FsMIOspfRouteType_Object=MibTableColumn
fsMIOspfRouteType=_FsMIOspfRouteType_Object((1,3,6,1,4,1,10876,101,1,145,8,1,5),_FsMIOspfRouteType_Type())
fsMIOspfRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRouteType.setStatus(_A)
_FsMIOspfRouteAreaId_Type=IpAddress
_FsMIOspfRouteAreaId_Object=MibTableColumn
fsMIOspfRouteAreaId=_FsMIOspfRouteAreaId_Object((1,3,6,1,4,1,10876,101,1,145,8,1,6),_FsMIOspfRouteAreaId_Type())
fsMIOspfRouteAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRouteAreaId.setStatus(_A)
_FsMIOspfRouteCost_Type=BigMetric
_FsMIOspfRouteCost_Object=MibTableColumn
fsMIOspfRouteCost=_FsMIOspfRouteCost_Object((1,3,6,1,4,1,10876,101,1,145,8,1,7),_FsMIOspfRouteCost_Type())
fsMIOspfRouteCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRouteCost.setStatus(_A)
_FsMIOspfRouteType2Cost_Type=BigMetric
_FsMIOspfRouteType2Cost_Object=MibTableColumn
fsMIOspfRouteType2Cost=_FsMIOspfRouteType2Cost_Object((1,3,6,1,4,1,10876,101,1,145,8,1,8),_FsMIOspfRouteType2Cost_Type())
fsMIOspfRouteType2Cost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRouteType2Cost.setStatus(_A)
class _FsMIOspfRouteInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfRouteInterfaceIndex_Type.__name__=_B
_FsMIOspfRouteInterfaceIndex_Object=MibTableColumn
fsMIOspfRouteInterfaceIndex=_FsMIOspfRouteInterfaceIndex_Object((1,3,6,1,4,1,10876,101,1,145,8,1,9),_FsMIOspfRouteInterfaceIndex_Type())
fsMIOspfRouteInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfRouteInterfaceIndex.setStatus(_A)
_FsMIOspfSecIfTable_Object=MibTable
fsMIOspfSecIfTable=_FsMIOspfSecIfTable_Object((1,3,6,1,4,1,10876,101,1,145,9))
if mibBuilder.loadTexts:fsMIOspfSecIfTable.setStatus(_A)
_FsMIOspfSecIfEntry_Object=MibTableRow
fsMIOspfSecIfEntry=_FsMIOspfSecIfEntry_Object((1,3,6,1,4,1,10876,101,1,145,9,1))
fsMIOspfSecIfEntry.setIndexNames((0,_G,_H),(0,_E,_A2),(0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:fsMIOspfSecIfEntry.setStatus(_A)
_FsMIOspfPrimIpAddr_Type=IpAddress
_FsMIOspfPrimIpAddr_Object=MibTableColumn
fsMIOspfPrimIpAddr=_FsMIOspfPrimIpAddr_Object((1,3,6,1,4,1,10876,101,1,145,9,1,1),_FsMIOspfPrimIpAddr_Type())
fsMIOspfPrimIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfPrimIpAddr.setStatus(_A)
class _FsMIOspfPrimAddresslessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfPrimAddresslessIf_Type.__name__=_B
_FsMIOspfPrimAddresslessIf_Object=MibTableColumn
fsMIOspfPrimAddresslessIf=_FsMIOspfPrimAddresslessIf_Object((1,3,6,1,4,1,10876,101,1,145,9,1,2),_FsMIOspfPrimAddresslessIf_Type())
fsMIOspfPrimAddresslessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfPrimAddresslessIf.setStatus(_A)
_FsMIOspfSecIpAddr_Type=IpAddress
_FsMIOspfSecIpAddr_Object=MibTableColumn
fsMIOspfSecIpAddr=_FsMIOspfSecIpAddr_Object((1,3,6,1,4,1,10876,101,1,145,9,1,3),_FsMIOspfSecIpAddr_Type())
fsMIOspfSecIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfSecIpAddr.setStatus(_A)
_FsMIOspfSecIpAddrMask_Type=IpAddress
_FsMIOspfSecIpAddrMask_Object=MibTableColumn
fsMIOspfSecIpAddrMask=_FsMIOspfSecIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,145,9,1,4),_FsMIOspfSecIpAddrMask_Type())
fsMIOspfSecIpAddrMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfSecIpAddrMask.setStatus(_A)
_FsMIOspfSecIfStatus_Type=RowStatus
_FsMIOspfSecIfStatus_Object=MibTableColumn
fsMIOspfSecIfStatus=_FsMIOspfSecIfStatus_Object((1,3,6,1,4,1,10876,101,1,145,9,1,5),_FsMIOspfSecIfStatus_Type())
fsMIOspfSecIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfSecIfStatus.setStatus(_A)
_FsMIOspfAreaAggregateTable_Object=MibTable
fsMIOspfAreaAggregateTable=_FsMIOspfAreaAggregateTable_Object((1,3,6,1,4,1,10876,101,1,145,10))
if mibBuilder.loadTexts:fsMIOspfAreaAggregateTable.setStatus(_A)
_FsMIOspfAreaAggregateEntry_Object=MibTableRow
fsMIOspfAreaAggregateEntry=_FsMIOspfAreaAggregateEntry_Object((1,3,6,1,4,1,10876,101,1,145,10,1))
fsMIOspfAreaAggregateEntry.setIndexNames((0,_G,_H),(0,_E,_A6),(0,_E,_A7),(0,_E,_A8),(0,_E,_A9))
if mibBuilder.loadTexts:fsMIOspfAreaAggregateEntry.setStatus(_A)
_FsMIOspfAreaAggregateAreaID_Type=AreaID
_FsMIOspfAreaAggregateAreaID_Object=MibTableColumn
fsMIOspfAreaAggregateAreaID=_FsMIOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,10876,101,1,145,10,1,1),_FsMIOspfAreaAggregateAreaID_Type())
fsMIOspfAreaAggregateAreaID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAreaAggregateAreaID.setStatus(_A)
class _FsMIOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*(('summaryLink',3),('nssaExternalLink',7)))
_FsMIOspfAreaAggregateLsdbType_Type.__name__=_B
_FsMIOspfAreaAggregateLsdbType_Object=MibTableColumn
fsMIOspfAreaAggregateLsdbType=_FsMIOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,10876,101,1,145,10,1,2),_FsMIOspfAreaAggregateLsdbType_Type())
fsMIOspfAreaAggregateLsdbType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAreaAggregateLsdbType.setStatus(_A)
_FsMIOspfAreaAggregateNet_Type=IpAddress
_FsMIOspfAreaAggregateNet_Object=MibTableColumn
fsMIOspfAreaAggregateNet=_FsMIOspfAreaAggregateNet_Object((1,3,6,1,4,1,10876,101,1,145,10,1,3),_FsMIOspfAreaAggregateNet_Type())
fsMIOspfAreaAggregateNet.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAreaAggregateNet.setStatus(_A)
_FsMIOspfAreaAggregateMask_Type=IpAddress
_FsMIOspfAreaAggregateMask_Object=MibTableColumn
fsMIOspfAreaAggregateMask=_FsMIOspfAreaAggregateMask_Object((1,3,6,1,4,1,10876,101,1,145,10,1,4),_FsMIOspfAreaAggregateMask_Type())
fsMIOspfAreaAggregateMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAreaAggregateMask.setStatus(_A)
_FsMIOspfAreaAggregateExternalTag_Type=Integer32
_FsMIOspfAreaAggregateExternalTag_Object=MibTableColumn
fsMIOspfAreaAggregateExternalTag=_FsMIOspfAreaAggregateExternalTag_Object((1,3,6,1,4,1,10876,101,1,145,10,1,5),_FsMIOspfAreaAggregateExternalTag_Type())
fsMIOspfAreaAggregateExternalTag.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAreaAggregateExternalTag.setStatus(_A)
_FsMIOspfAsExternalAggregationTable_Object=MibTable
fsMIOspfAsExternalAggregationTable=_FsMIOspfAsExternalAggregationTable_Object((1,3,6,1,4,1,10876,101,1,145,11))
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationTable.setStatus(_A)
_FsMIOspfAsExternalAggregationEntry_Object=MibTableRow
fsMIOspfAsExternalAggregationEntry=_FsMIOspfAsExternalAggregationEntry_Object((1,3,6,1,4,1,10876,101,1,145,11,1))
fsMIOspfAsExternalAggregationEntry.setIndexNames((0,_G,_H),(0,_E,_AA),(0,_E,_AB),(0,_E,_AC))
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationEntry.setStatus(_A)
_FsMIOspfAsExternalAggregationNet_Type=IpAddress
_FsMIOspfAsExternalAggregationNet_Object=MibTableColumn
fsMIOspfAsExternalAggregationNet=_FsMIOspfAsExternalAggregationNet_Object((1,3,6,1,4,1,10876,101,1,145,11,1,1),_FsMIOspfAsExternalAggregationNet_Type())
fsMIOspfAsExternalAggregationNet.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationNet.setStatus(_A)
_FsMIOspfAsExternalAggregationMask_Type=IpAddress
_FsMIOspfAsExternalAggregationMask_Object=MibTableColumn
fsMIOspfAsExternalAggregationMask=_FsMIOspfAsExternalAggregationMask_Object((1,3,6,1,4,1,10876,101,1,145,11,1,2),_FsMIOspfAsExternalAggregationMask_Type())
fsMIOspfAsExternalAggregationMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationMask.setStatus(_A)
_FsMIOspfAsExternalAggregationAreaId_Type=AreaID
_FsMIOspfAsExternalAggregationAreaId_Object=MibTableColumn
fsMIOspfAsExternalAggregationAreaId=_FsMIOspfAsExternalAggregationAreaId_Object((1,3,6,1,4,1,10876,101,1,145,11,1,3),_FsMIOspfAsExternalAggregationAreaId_Type())
fsMIOspfAsExternalAggregationAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationAreaId.setStatus(_A)
class _FsMIOspfAsExternalAggregationEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertise',1),('doNotAdvertise',2),('allowAll',3),('denyAll',4)))
_FsMIOspfAsExternalAggregationEffect_Type.__name__=_B
_FsMIOspfAsExternalAggregationEffect_Object=MibTableColumn
fsMIOspfAsExternalAggregationEffect=_FsMIOspfAsExternalAggregationEffect_Object((1,3,6,1,4,1,10876,101,1,145,11,1,4),_FsMIOspfAsExternalAggregationEffect_Type())
fsMIOspfAsExternalAggregationEffect.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationEffect.setStatus(_A)
class _FsMIOspfAsExternalAggregationTranslation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfAsExternalAggregationTranslation_Type.__name__=_B
_FsMIOspfAsExternalAggregationTranslation_Object=MibTableColumn
fsMIOspfAsExternalAggregationTranslation=_FsMIOspfAsExternalAggregationTranslation_Object((1,3,6,1,4,1,10876,101,1,145,11,1,5),_FsMIOspfAsExternalAggregationTranslation_Type())
fsMIOspfAsExternalAggregationTranslation.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationTranslation.setStatus(_A)
_FsMIOspfAsExternalAggregationStatus_Type=RowStatus
_FsMIOspfAsExternalAggregationStatus_Object=MibTableColumn
fsMIOspfAsExternalAggregationStatus=_FsMIOspfAsExternalAggregationStatus_Object((1,3,6,1,4,1,10876,101,1,145,11,1,6),_FsMIOspfAsExternalAggregationStatus_Type())
fsMIOspfAsExternalAggregationStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfAsExternalAggregationStatus.setStatus(_A)
_FsMIOspfOpaqueLSAGroup_ObjectIdentity=ObjectIdentity
fsMIOspfOpaqueLSAGroup=_FsMIOspfOpaqueLSAGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,12))
_FsMIOspfOpaqueLSAGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfOpaqueLSAGeneralGroup=_FsMIOspfOpaqueLSAGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,12,1))
_FsMIOspfOpaqueTable_Object=MibTable
fsMIOspfOpaqueTable=_FsMIOspfOpaqueTable_Object((1,3,6,1,4,1,10876,101,1,145,12,1,1))
if mibBuilder.loadTexts:fsMIOspfOpaqueTable.setStatus(_A)
_FsMIOspfOpaqueEntry_Object=MibTableRow
fsMIOspfOpaqueEntry=_FsMIOspfOpaqueEntry_Object((1,3,6,1,4,1,10876,101,1,145,12,1,1,1))
if mibBuilder.loadTexts:fsMIOspfOpaqueEntry.setStatus(_A)
class _FsMIOspfOpaqueOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfOpaqueOption_Type.__name__=_B
_FsMIOspfOpaqueOption_Object=MibTableColumn
fsMIOspfOpaqueOption=_FsMIOspfOpaqueOption_Object((1,3,6,1,4,1,10876,101,1,145,12,1,1,1,1),_FsMIOspfOpaqueOption_Type())
fsMIOspfOpaqueOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfOpaqueOption.setStatus(_A)
_FsMIOspfType11LsaCount_Type=Gauge32
_FsMIOspfType11LsaCount_Object=MibTableColumn
fsMIOspfType11LsaCount=_FsMIOspfType11LsaCount_Object((1,3,6,1,4,1,10876,101,1,145,12,1,1,1,2),_FsMIOspfType11LsaCount_Type())
fsMIOspfType11LsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType11LsaCount.setStatus(_A)
_FsMIOspfType11LsaCksumSum_Type=Integer32
_FsMIOspfType11LsaCksumSum_Object=MibTableColumn
fsMIOspfType11LsaCksumSum=_FsMIOspfType11LsaCksumSum_Object((1,3,6,1,4,1,10876,101,1,145,12,1,1,1,3),_FsMIOspfType11LsaCksumSum_Type())
fsMIOspfType11LsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType11LsaCksumSum.setStatus(_A)
class _FsMIOspfAreaIDValid_Type(TruthValue):defaultValue=2
_FsMIOspfAreaIDValid_Type.__name__=_M
_FsMIOspfAreaIDValid_Object=MibTableColumn
fsMIOspfAreaIDValid=_FsMIOspfAreaIDValid_Object((1,3,6,1,4,1,10876,101,1,145,12,1,1,1,4),_FsMIOspfAreaIDValid_Type())
fsMIOspfAreaIDValid.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfAreaIDValid.setStatus(_A)
_FsMIOspfOpaqueInterfaceTable_Object=MibTable
fsMIOspfOpaqueInterfaceTable=_FsMIOspfOpaqueInterfaceTable_Object((1,3,6,1,4,1,10876,101,1,145,12,2))
if mibBuilder.loadTexts:fsMIOspfOpaqueInterfaceTable.setStatus(_A)
_FsMIOspfOpaqueInterfaceEntry_Object=MibTableRow
fsMIOspfOpaqueInterfaceEntry=_FsMIOspfOpaqueInterfaceEntry_Object((1,3,6,1,4,1,10876,101,1,145,12,2,1))
if mibBuilder.loadTexts:fsMIOspfOpaqueInterfaceEntry.setStatus(_A)
_FsMIOspfOpaqueType9LsaCount_Type=Gauge32
_FsMIOspfOpaqueType9LsaCount_Object=MibTableColumn
fsMIOspfOpaqueType9LsaCount=_FsMIOspfOpaqueType9LsaCount_Object((1,3,6,1,4,1,10876,101,1,145,12,2,1,1),_FsMIOspfOpaqueType9LsaCount_Type())
fsMIOspfOpaqueType9LsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfOpaqueType9LsaCount.setStatus(_A)
class _FsMIOspfOpaqueType9LsaCksumSum_Type(Integer32):defaultValue=0
_FsMIOspfOpaqueType9LsaCksumSum_Type.__name__=_B
_FsMIOspfOpaqueType9LsaCksumSum_Object=MibTableColumn
fsMIOspfOpaqueType9LsaCksumSum=_FsMIOspfOpaqueType9LsaCksumSum_Object((1,3,6,1,4,1,10876,101,1,145,12,2,1,2),_FsMIOspfOpaqueType9LsaCksumSum_Type())
fsMIOspfOpaqueType9LsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfOpaqueType9LsaCksumSum.setStatus(_A)
_FsMIOspfType9LsdbTable_Object=MibTable
fsMIOspfType9LsdbTable=_FsMIOspfType9LsdbTable_Object((1,3,6,1,4,1,10876,101,1,145,12,3))
if mibBuilder.loadTexts:fsMIOspfType9LsdbTable.setStatus(_A)
_FsMIOspfType9LsdbEntry_Object=MibTableRow
fsMIOspfType9LsdbEntry=_FsMIOspfType9LsdbEntry_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1))
fsMIOspfType9LsdbEntry.setIndexNames((0,_G,_H),(0,_E,_AD),(0,_E,_AE),(0,_E,_AF),(0,_E,_AG))
if mibBuilder.loadTexts:fsMIOspfType9LsdbEntry.setStatus(_A)
_FsMIOspfType9LsdbIfIpAddress_Type=IpAddress
_FsMIOspfType9LsdbIfIpAddress_Object=MibTableColumn
fsMIOspfType9LsdbIfIpAddress=_FsMIOspfType9LsdbIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,1),_FsMIOspfType9LsdbIfIpAddress_Type())
fsMIOspfType9LsdbIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType9LsdbIfIpAddress.setStatus(_A)
class _FsMIOspfType9LsdbOpaqueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,11))
_FsMIOspfType9LsdbOpaqueType_Type.__name__=_B
_FsMIOspfType9LsdbOpaqueType_Object=MibTableColumn
fsMIOspfType9LsdbOpaqueType=_FsMIOspfType9LsdbOpaqueType_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,2),_FsMIOspfType9LsdbOpaqueType_Type())
fsMIOspfType9LsdbOpaqueType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType9LsdbOpaqueType.setStatus(_A)
_FsMIOspfType9LsdbLsid_Type=IpAddress
_FsMIOspfType9LsdbLsid_Object=MibTableColumn
fsMIOspfType9LsdbLsid=_FsMIOspfType9LsdbLsid_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,3),_FsMIOspfType9LsdbLsid_Type())
fsMIOspfType9LsdbLsid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType9LsdbLsid.setStatus(_A)
_FsMIOspfType9LsdbRouterId_Type=RouterID
_FsMIOspfType9LsdbRouterId_Object=MibTableColumn
fsMIOspfType9LsdbRouterId=_FsMIOspfType9LsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,4),_FsMIOspfType9LsdbRouterId_Type())
fsMIOspfType9LsdbRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType9LsdbRouterId.setStatus(_A)
_FsMIOspfType9LsdbSequence_Type=Integer32
_FsMIOspfType9LsdbSequence_Object=MibTableColumn
fsMIOspfType9LsdbSequence=_FsMIOspfType9LsdbSequence_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,5),_FsMIOspfType9LsdbSequence_Type())
fsMIOspfType9LsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType9LsdbSequence.setStatus(_A)
_FsMIOspfType9LsdbAge_Type=Integer32
_FsMIOspfType9LsdbAge_Object=MibTableColumn
fsMIOspfType9LsdbAge=_FsMIOspfType9LsdbAge_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,6),_FsMIOspfType9LsdbAge_Type())
fsMIOspfType9LsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType9LsdbAge.setStatus(_A)
_FsMIOspfType9LsdbChecksum_Type=Integer32
_FsMIOspfType9LsdbChecksum_Object=MibTableColumn
fsMIOspfType9LsdbChecksum=_FsMIOspfType9LsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,7),_FsMIOspfType9LsdbChecksum_Type())
fsMIOspfType9LsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType9LsdbChecksum.setStatus(_A)
class _FsMIOspfType9LsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FsMIOspfType9LsdbAdvertisement_Type.__name__=_L
_FsMIOspfType9LsdbAdvertisement_Object=MibTableColumn
fsMIOspfType9LsdbAdvertisement=_FsMIOspfType9LsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,145,12,3,1,8),_FsMIOspfType9LsdbAdvertisement_Type())
fsMIOspfType9LsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType9LsdbAdvertisement.setStatus(_A)
_FsMIOspfType11LsdbTable_Object=MibTable
fsMIOspfType11LsdbTable=_FsMIOspfType11LsdbTable_Object((1,3,6,1,4,1,10876,101,1,145,12,4))
if mibBuilder.loadTexts:fsMIOspfType11LsdbTable.setStatus(_A)
_FsMIOspfType11LsdbEntry_Object=MibTableRow
fsMIOspfType11LsdbEntry=_FsMIOspfType11LsdbEntry_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1))
fsMIOspfType11LsdbEntry.setIndexNames((0,_G,_H),(0,_E,_AH),(0,_E,_AI),(0,_E,_AJ))
if mibBuilder.loadTexts:fsMIOspfType11LsdbEntry.setStatus(_A)
class _FsMIOspfType11LsdbOpaqueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,11))
_FsMIOspfType11LsdbOpaqueType_Type.__name__=_B
_FsMIOspfType11LsdbOpaqueType_Object=MibTableColumn
fsMIOspfType11LsdbOpaqueType=_FsMIOspfType11LsdbOpaqueType_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,1),_FsMIOspfType11LsdbOpaqueType_Type())
fsMIOspfType11LsdbOpaqueType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType11LsdbOpaqueType.setStatus(_A)
_FsMIOspfType11LsdbLsid_Type=IpAddress
_FsMIOspfType11LsdbLsid_Object=MibTableColumn
fsMIOspfType11LsdbLsid=_FsMIOspfType11LsdbLsid_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,2),_FsMIOspfType11LsdbLsid_Type())
fsMIOspfType11LsdbLsid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType11LsdbLsid.setStatus(_A)
_FsMIOspfType11LsdbRouterId_Type=RouterID
_FsMIOspfType11LsdbRouterId_Object=MibTableColumn
fsMIOspfType11LsdbRouterId=_FsMIOspfType11LsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,3),_FsMIOspfType11LsdbRouterId_Type())
fsMIOspfType11LsdbRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfType11LsdbRouterId.setStatus(_A)
_FsMIOspfType11LsdbSequence_Type=Integer32
_FsMIOspfType11LsdbSequence_Object=MibTableColumn
fsMIOspfType11LsdbSequence=_FsMIOspfType11LsdbSequence_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,4),_FsMIOspfType11LsdbSequence_Type())
fsMIOspfType11LsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType11LsdbSequence.setStatus(_A)
_FsMIOspfType11LsdbAge_Type=Integer32
_FsMIOspfType11LsdbAge_Object=MibTableColumn
fsMIOspfType11LsdbAge=_FsMIOspfType11LsdbAge_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,5),_FsMIOspfType11LsdbAge_Type())
fsMIOspfType11LsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType11LsdbAge.setStatus(_A)
_FsMIOspfType11LsdbChecksum_Type=Integer32
_FsMIOspfType11LsdbChecksum_Object=MibTableColumn
fsMIOspfType11LsdbChecksum=_FsMIOspfType11LsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,6),_FsMIOspfType11LsdbChecksum_Type())
fsMIOspfType11LsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType11LsdbChecksum.setStatus(_A)
class _FsMIOspfType11LsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FsMIOspfType11LsdbAdvertisement_Type.__name__=_L
_FsMIOspfType11LsdbAdvertisement_Object=MibTableColumn
fsMIOspfType11LsdbAdvertisement=_FsMIOspfType11LsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,145,12,4,1,7),_FsMIOspfType11LsdbAdvertisement_Type())
fsMIOspfType11LsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfType11LsdbAdvertisement.setStatus(_A)
_FsMIOspfAppInfoDbTable_Object=MibTable
fsMIOspfAppInfoDbTable=_FsMIOspfAppInfoDbTable_Object((1,3,6,1,4,1,10876,101,1,145,12,5))
if mibBuilder.loadTexts:fsMIOspfAppInfoDbTable.setStatus(_A)
_FsMIOspfAppInfoDbEntry_Object=MibTableRow
fsMIOspfAppInfoDbEntry=_FsMIOspfAppInfoDbEntry_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1))
fsMIOspfAppInfoDbEntry.setIndexNames((0,_G,_H),(0,_E,_AK))
if mibBuilder.loadTexts:fsMIOspfAppInfoDbEntry.setStatus(_A)
class _FsMIOspfAppInfoDbAppid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIOspfAppInfoDbAppid_Type.__name__=_B
_FsMIOspfAppInfoDbAppid_Object=MibTableColumn
fsMIOspfAppInfoDbAppid=_FsMIOspfAppInfoDbAppid_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,1),_FsMIOspfAppInfoDbAppid_Type())
fsMIOspfAppInfoDbAppid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbAppid.setStatus(_A)
class _FsMIOspfAppInfoDbOpaqueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfAppInfoDbOpaqueType_Type.__name__=_B
_FsMIOspfAppInfoDbOpaqueType_Object=MibTableColumn
fsMIOspfAppInfoDbOpaqueType=_FsMIOspfAppInfoDbOpaqueType_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,2),_FsMIOspfAppInfoDbOpaqueType_Type())
fsMIOspfAppInfoDbOpaqueType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbOpaqueType.setStatus(_A)
class _FsMIOspfAppInfoDbLsaTypesSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsMIOspfAppInfoDbLsaTypesSupported_Type.__name__=_B
_FsMIOspfAppInfoDbLsaTypesSupported_Object=MibTableColumn
fsMIOspfAppInfoDbLsaTypesSupported=_FsMIOspfAppInfoDbLsaTypesSupported_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,3),_FsMIOspfAppInfoDbLsaTypesSupported_Type())
fsMIOspfAppInfoDbLsaTypesSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbLsaTypesSupported.setStatus(_A)
_FsMIOspfAppInfoDbType9Gen_Type=Counter32
_FsMIOspfAppInfoDbType9Gen_Object=MibTableColumn
fsMIOspfAppInfoDbType9Gen=_FsMIOspfAppInfoDbType9Gen_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,4),_FsMIOspfAppInfoDbType9Gen_Type())
fsMIOspfAppInfoDbType9Gen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbType9Gen.setStatus(_A)
_FsMIOspfAppInfoDbType9Rcvd_Type=Counter32
_FsMIOspfAppInfoDbType9Rcvd_Object=MibTableColumn
fsMIOspfAppInfoDbType9Rcvd=_FsMIOspfAppInfoDbType9Rcvd_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,5),_FsMIOspfAppInfoDbType9Rcvd_Type())
fsMIOspfAppInfoDbType9Rcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbType9Rcvd.setStatus(_A)
_FsMIOspfAppInfoDbType10Gen_Type=Counter32
_FsMIOspfAppInfoDbType10Gen_Object=MibTableColumn
fsMIOspfAppInfoDbType10Gen=_FsMIOspfAppInfoDbType10Gen_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,6),_FsMIOspfAppInfoDbType10Gen_Type())
fsMIOspfAppInfoDbType10Gen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbType10Gen.setStatus(_A)
_FsMIOspfAppInfoDbType10Rcvd_Type=Counter32
_FsMIOspfAppInfoDbType10Rcvd_Object=MibTableColumn
fsMIOspfAppInfoDbType10Rcvd=_FsMIOspfAppInfoDbType10Rcvd_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,7),_FsMIOspfAppInfoDbType10Rcvd_Type())
fsMIOspfAppInfoDbType10Rcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbType10Rcvd.setStatus(_A)
_FsMIOspfAppInfoDbType11Gen_Type=Counter32
_FsMIOspfAppInfoDbType11Gen_Object=MibTableColumn
fsMIOspfAppInfoDbType11Gen=_FsMIOspfAppInfoDbType11Gen_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,8),_FsMIOspfAppInfoDbType11Gen_Type())
fsMIOspfAppInfoDbType11Gen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbType11Gen.setStatus(_A)
_FsMIOspfAppInfoDbType11Rcvd_Type=Counter32
_FsMIOspfAppInfoDbType11Rcvd_Object=MibTableColumn
fsMIOspfAppInfoDbType11Rcvd=_FsMIOspfAppInfoDbType11Rcvd_Object((1,3,6,1,4,1,10876,101,1,145,12,5,1,9),_FsMIOspfAppInfoDbType11Rcvd_Type())
fsMIOspfAppInfoDbType11Rcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfAppInfoDbType11Rcvd.setStatus(_A)
_FsMIOspfRRDGroup_ObjectIdentity=ObjectIdentity
fsMIOspfRRDGroup=_FsMIOspfRRDGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,13))
_FsMIOspfRRDGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfRRDGeneralGroup=_FsMIOspfRRDGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,13,1))
_FsMIOspfRRDRouteTable_Object=MibTable
fsMIOspfRRDRouteTable=_FsMIOspfRRDRouteTable_Object((1,3,6,1,4,1,10876,101,1,145,13,1,1))
if mibBuilder.loadTexts:fsMIOspfRRDRouteTable.setStatus(_A)
_FsMIOspfRRDRouteEntry_Object=MibTableRow
fsMIOspfRRDRouteEntry=_FsMIOspfRRDRouteEntry_Object((1,3,6,1,4,1,10876,101,1,145,13,1,1,1))
if mibBuilder.loadTexts:fsMIOspfRRDRouteEntry.setStatus(_A)
class _FsMIOspfRRDStatus_Type(Status):defaultValue=2
_FsMIOspfRRDStatus_Type.__name__=_U
_FsMIOspfRRDStatus_Object=MibTableColumn
fsMIOspfRRDStatus=_FsMIOspfRRDStatus_Object((1,3,6,1,4,1,10876,101,1,145,13,1,1,1,1),_FsMIOspfRRDStatus_Type())
fsMIOspfRRDStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDStatus.setStatus(_A)
class _FsMIOspfRRDSrcProtoMaskEnable_Type(Integer32):defaultValue=0
_FsMIOspfRRDSrcProtoMaskEnable_Type.__name__=_B
_FsMIOspfRRDSrcProtoMaskEnable_Object=MibTableColumn
fsMIOspfRRDSrcProtoMaskEnable=_FsMIOspfRRDSrcProtoMaskEnable_Object((1,3,6,1,4,1,10876,101,1,145,13,1,1,1,2),_FsMIOspfRRDSrcProtoMaskEnable_Type())
fsMIOspfRRDSrcProtoMaskEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDSrcProtoMaskEnable.setStatus(_A)
class _FsMIOspfRRDSrcProtoMaskDisable_Type(Integer32):defaultValue=8326
_FsMIOspfRRDSrcProtoMaskDisable_Type.__name__=_B
_FsMIOspfRRDSrcProtoMaskDisable_Object=MibTableColumn
fsMIOspfRRDSrcProtoMaskDisable=_FsMIOspfRRDSrcProtoMaskDisable_Object((1,3,6,1,4,1,10876,101,1,145,13,1,1,1,3),_FsMIOspfRRDSrcProtoMaskDisable_Type())
fsMIOspfRRDSrcProtoMaskDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDSrcProtoMaskDisable.setStatus(_A)
class _FsMIOspfRRDRouteMapEnable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsMIOspfRRDRouteMapEnable_Type.__name__=_T
_FsMIOspfRRDRouteMapEnable_Object=MibTableColumn
fsMIOspfRRDRouteMapEnable=_FsMIOspfRRDRouteMapEnable_Object((1,3,6,1,4,1,10876,101,1,145,13,1,1,1,4),_FsMIOspfRRDRouteMapEnable_Type())
fsMIOspfRRDRouteMapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDRouteMapEnable.setStatus(_A)
_FsMIOspfRRDRouteConfigTable_Object=MibTable
fsMIOspfRRDRouteConfigTable=_FsMIOspfRRDRouteConfigTable_Object((1,3,6,1,4,1,10876,101,1,145,13,2))
if mibBuilder.loadTexts:fsMIOspfRRDRouteConfigTable.setStatus(_A)
_FsMIOspfRRDRouteConfigEntry_Object=MibTableRow
fsMIOspfRRDRouteConfigEntry=_FsMIOspfRRDRouteConfigEntry_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1))
fsMIOspfRRDRouteConfigEntry.setIndexNames((0,_G,_H),(0,_E,_AL),(0,_E,_AM))
if mibBuilder.loadTexts:fsMIOspfRRDRouteConfigEntry.setStatus(_A)
_FsMIOspfRRDRouteDest_Type=IpAddress
_FsMIOspfRRDRouteDest_Object=MibTableColumn
fsMIOspfRRDRouteDest=_FsMIOspfRRDRouteDest_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,1),_FsMIOspfRRDRouteDest_Type())
fsMIOspfRRDRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRRDRouteDest.setStatus(_A)
_FsMIOspfRRDRouteMask_Type=IpAddress
_FsMIOspfRRDRouteMask_Object=MibTableColumn
fsMIOspfRRDRouteMask=_FsMIOspfRRDRouteMask_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,2),_FsMIOspfRRDRouteMask_Type())
fsMIOspfRRDRouteMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRRDRouteMask.setStatus(_A)
class _FsMIOspfRRDRouteMetric_Type(BigMetric):defaultValue=10
_FsMIOspfRRDRouteMetric_Type.__name__=_a
_FsMIOspfRRDRouteMetric_Object=MibTableColumn
fsMIOspfRRDRouteMetric=_FsMIOspfRRDRouteMetric_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,3),_FsMIOspfRRDRouteMetric_Type())
fsMIOspfRRDRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDRouteMetric.setStatus(_A)
class _FsMIOspfRRDRouteMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asexttype1',1),('asexttype2',2)))
_FsMIOspfRRDRouteMetricType_Type.__name__=_B
_FsMIOspfRRDRouteMetricType_Object=MibTableColumn
fsMIOspfRRDRouteMetricType=_FsMIOspfRRDRouteMetricType_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,4),_FsMIOspfRRDRouteMetricType_Type())
fsMIOspfRRDRouteMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDRouteMetricType.setStatus(_A)
class _FsMIOspfRRDRouteTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_FsMIOspfRRDRouteTagType_Type.__name__=_B
_FsMIOspfRRDRouteTagType_Object=MibTableColumn
fsMIOspfRRDRouteTagType=_FsMIOspfRRDRouteTagType_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,5),_FsMIOspfRRDRouteTagType_Type())
fsMIOspfRRDRouteTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDRouteTagType.setStatus(_A)
class _FsMIOspfRRDRouteTag_Type(Unsigned32):defaultValue=0
_FsMIOspfRRDRouteTag_Type.__name__=_Z
_FsMIOspfRRDRouteTag_Object=MibTableColumn
fsMIOspfRRDRouteTag=_FsMIOspfRRDRouteTag_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,6),_FsMIOspfRRDRouteTag_Type())
fsMIOspfRRDRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDRouteTag.setStatus(_A)
_FsMIOspfRRDRouteStatus_Type=RowStatus
_FsMIOspfRRDRouteStatus_Object=MibTableColumn
fsMIOspfRRDRouteStatus=_FsMIOspfRRDRouteStatus_Object((1,3,6,1,4,1,10876,101,1,145,13,2,1,7),_FsMIOspfRRDRouteStatus_Type())
fsMIOspfRRDRouteStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIOspfRRDRouteStatus.setStatus(_A)
_FsMIOspfRRDMetricTable_Object=MibTable
fsMIOspfRRDMetricTable=_FsMIOspfRRDMetricTable_Object((1,3,6,1,4,1,10876,101,1,145,13,3))
if mibBuilder.loadTexts:fsMIOspfRRDMetricTable.setStatus(_A)
_FsMIOspfRRDMerticEntry_Object=MibTableRow
fsMIOspfRRDMerticEntry=_FsMIOspfRRDMerticEntry_Object((1,3,6,1,4,1,10876,101,1,145,13,3,1))
fsMIOspfRRDMerticEntry.setIndexNames((0,_G,_H),(0,_E,_AN))
if mibBuilder.loadTexts:fsMIOspfRRDMerticEntry.setStatus(_A)
class _FsMIOspfRRDProtocolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bgp',1),('rip',2),('connected',3),('static',4)))
_FsMIOspfRRDProtocolId_Type.__name__=_B
_FsMIOspfRRDProtocolId_Object=MibTableColumn
fsMIOspfRRDProtocolId=_FsMIOspfRRDProtocolId_Object((1,3,6,1,4,1,10876,101,1,145,13,3,1,1),_FsMIOspfRRDProtocolId_Type())
fsMIOspfRRDProtocolId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfRRDProtocolId.setStatus(_A)
_FsMIOspfRRDMetricValue_Type=Integer32
_FsMIOspfRRDMetricValue_Object=MibTableColumn
fsMIOspfRRDMetricValue=_FsMIOspfRRDMetricValue_Object((1,3,6,1,4,1,10876,101,1,145,13,3,1,2),_FsMIOspfRRDMetricValue_Type())
fsMIOspfRRDMetricValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDMetricValue.setStatus(_A)
class _FsMIOspfRRDMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_FsMIOspfRRDMetricType_Type.__name__=_B
_FsMIOspfRRDMetricType_Object=MibTableColumn
fsMIOspfRRDMetricType=_FsMIOspfRRDMetricType_Object((1,3,6,1,4,1,10876,101,1,145,13,3,1,3),_FsMIOspfRRDMetricType_Type())
fsMIOspfRRDMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfRRDMetricType.setStatus(_A)
_FsMIOspfVirtNbrTable_Object=MibTable
fsMIOspfVirtNbrTable=_FsMIOspfVirtNbrTable_Object((1,3,6,1,4,1,10876,101,1,145,14))
if mibBuilder.loadTexts:fsMIOspfVirtNbrTable.setStatus(_A)
_FsMIOspfVirtNbrEntry_Object=MibTableRow
fsMIOspfVirtNbrEntry=_FsMIOspfVirtNbrEntry_Object((1,3,6,1,4,1,10876,101,1,145,14,1))
if mibBuilder.loadTexts:fsMIOspfVirtNbrEntry.setStatus(_A)
class _FsMIOspfVirtNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),(_v,2)))
_FsMIOspfVirtNbrRestartHelperStatus_Type.__name__=_B
_FsMIOspfVirtNbrRestartHelperStatus_Object=MibTableColumn
fsMIOspfVirtNbrRestartHelperStatus=_FsMIOspfVirtNbrRestartHelperStatus_Object((1,3,6,1,4,1,10876,101,1,145,14,1,1),_FsMIOspfVirtNbrRestartHelperStatus_Type())
fsMIOspfVirtNbrRestartHelperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfVirtNbrRestartHelperStatus.setStatus(_A)
_FsMIOspfVirtNbrRestartHelperAge_Type=Unsigned32
_FsMIOspfVirtNbrRestartHelperAge_Object=MibTableColumn
fsMIOspfVirtNbrRestartHelperAge=_FsMIOspfVirtNbrRestartHelperAge_Object((1,3,6,1,4,1,10876,101,1,145,14,1,2),_FsMIOspfVirtNbrRestartHelperAge_Type())
fsMIOspfVirtNbrRestartHelperAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfVirtNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIOspfVirtNbrRestartHelperAge.setUnits(_V)
class _FsMIOspfVirtNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_W,4),(_X,5)))
_FsMIOspfVirtNbrRestartHelperExitReason_Type.__name__=_B
_FsMIOspfVirtNbrRestartHelperExitReason_Object=MibTableColumn
fsMIOspfVirtNbrRestartHelperExitReason=_FsMIOspfVirtNbrRestartHelperExitReason_Object((1,3,6,1,4,1,10876,101,1,145,14,1,3),_FsMIOspfVirtNbrRestartHelperExitReason_Type())
fsMIOspfVirtNbrRestartHelperExitReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfVirtNbrRestartHelperExitReason.setStatus(_A)
_FsMIospfDistInOutRouteMap_ObjectIdentity=ObjectIdentity
fsMIospfDistInOutRouteMap=_FsMIospfDistInOutRouteMap_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,15))
_FsMIOspfDistInOutRouteMapTable_Object=MibTable
fsMIOspfDistInOutRouteMapTable=_FsMIOspfDistInOutRouteMapTable_Object((1,3,6,1,4,1,10876,101,1,145,15,1))
if mibBuilder.loadTexts:fsMIOspfDistInOutRouteMapTable.setStatus(_A)
_FsMIOspfDistInOutRouteMapEntry_Object=MibTableRow
fsMIOspfDistInOutRouteMapEntry=_FsMIOspfDistInOutRouteMapEntry_Object((1,3,6,1,4,1,10876,101,1,145,15,1,1))
fsMIOspfDistInOutRouteMapEntry.setIndexNames((0,_G,_H),(0,_E,_AO),(0,_E,_AP))
if mibBuilder.loadTexts:fsMIOspfDistInOutRouteMapEntry.setStatus(_A)
class _FsMIOspfDistInOutRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsMIOspfDistInOutRouteMapName_Type.__name__=_T
_FsMIOspfDistInOutRouteMapName_Object=MibTableColumn
fsMIOspfDistInOutRouteMapName=_FsMIOspfDistInOutRouteMapName_Object((1,3,6,1,4,1,10876,101,1,145,15,1,1,1),_FsMIOspfDistInOutRouteMapName_Type())
fsMIOspfDistInOutRouteMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfDistInOutRouteMapName.setStatus(_A)
class _FsMIOspfDistInOutRouteMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FsMIOspfDistInOutRouteMapType_Type.__name__=_B
_FsMIOspfDistInOutRouteMapType_Object=MibTableColumn
fsMIOspfDistInOutRouteMapType=_FsMIOspfDistInOutRouteMapType_Object((1,3,6,1,4,1,10876,101,1,145,15,1,1,3),_FsMIOspfDistInOutRouteMapType_Type())
fsMIOspfDistInOutRouteMapType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfDistInOutRouteMapType.setStatus(_A)
class _FsMIOspfDistInOutRouteMapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIOspfDistInOutRouteMapValue_Type.__name__=_B
_FsMIOspfDistInOutRouteMapValue_Object=MibTableColumn
fsMIOspfDistInOutRouteMapValue=_FsMIOspfDistInOutRouteMapValue_Object((1,3,6,1,4,1,10876,101,1,145,15,1,1,4),_FsMIOspfDistInOutRouteMapValue_Type())
fsMIOspfDistInOutRouteMapValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfDistInOutRouteMapValue.setStatus(_A)
_FsMIOspfDistInOutRouteMapRowStatus_Type=RowStatus
_FsMIOspfDistInOutRouteMapRowStatus_Object=MibTableColumn
fsMIOspfDistInOutRouteMapRowStatus=_FsMIOspfDistInOutRouteMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,145,15,1,1,5),_FsMIOspfDistInOutRouteMapRowStatus_Type())
fsMIOspfDistInOutRouteMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfDistInOutRouteMapRowStatus.setStatus(_A)
_FsMIospfPreferenceGroup_ObjectIdentity=ObjectIdentity
fsMIospfPreferenceGroup=_FsMIospfPreferenceGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,16))
_FsMIOspfPreferenceTable_Object=MibTable
fsMIOspfPreferenceTable=_FsMIOspfPreferenceTable_Object((1,3,6,1,4,1,10876,101,1,145,16,1))
if mibBuilder.loadTexts:fsMIOspfPreferenceTable.setStatus(_A)
_FsMIOspfPreferenceEntry_Object=MibTableRow
fsMIOspfPreferenceEntry=_FsMIOspfPreferenceEntry_Object((1,3,6,1,4,1,10876,101,1,145,16,1,1))
fsMIOspfPreferenceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fsMIOspfPreferenceEntry.setStatus(_A)
class _FsMIOspfPreferenceValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfPreferenceValue_Type.__name__=_B
_FsMIOspfPreferenceValue_Object=MibTableColumn
fsMIOspfPreferenceValue=_FsMIOspfPreferenceValue_Object((1,3,6,1,4,1,10876,101,1,145,16,1,1,1),_FsMIOspfPreferenceValue_Type())
fsMIOspfPreferenceValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfPreferenceValue.setStatus(_A)
_FsMIOspfIfAuthTable_Object=MibTable
fsMIOspfIfAuthTable=_FsMIOspfIfAuthTable_Object((1,3,6,1,4,1,10876,101,1,145,17))
if mibBuilder.loadTexts:fsMIOspfIfAuthTable.setStatus(_A)
_FsMIOspfIfAuthEntry_Object=MibTableRow
fsMIOspfIfAuthEntry=_FsMIOspfIfAuthEntry_Object((1,3,6,1,4,1,10876,101,1,145,17,1))
fsMIOspfIfAuthEntry.setIndexNames((0,_G,_H),(0,_E,_AQ),(0,_E,_AR),(0,_E,_AS))
if mibBuilder.loadTexts:fsMIOspfIfAuthEntry.setStatus(_A)
_FsMIOspfIfAuthIpAddress_Type=IpAddress
_FsMIOspfIfAuthIpAddress_Object=MibTableColumn
fsMIOspfIfAuthIpAddress=_FsMIOspfIfAuthIpAddress_Object((1,3,6,1,4,1,10876,101,1,145,17,1,1),_FsMIOspfIfAuthIpAddress_Type())
fsMIOspfIfAuthIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfAuthIpAddress.setStatus(_A)
class _FsMIOspfIfAuthAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfIfAuthAddressLessIf_Type.__name__=_B
_FsMIOspfIfAuthAddressLessIf_Object=MibTableColumn
fsMIOspfIfAuthAddressLessIf=_FsMIOspfIfAuthAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,145,17,1,2),_FsMIOspfIfAuthAddressLessIf_Type())
fsMIOspfIfAuthAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfAuthAddressLessIf.setStatus(_A)
class _FsMIOspfIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfIfAuthKeyId_Type.__name__=_B
_FsMIOspfIfAuthKeyId_Object=MibTableColumn
fsMIOspfIfAuthKeyId=_FsMIOspfIfAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,145,17,1,3),_FsMIOspfIfAuthKeyId_Type())
fsMIOspfIfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfIfAuthKeyId.setStatus(_A)
class _FsMIOspfIfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIOspfIfAuthKey_Type.__name__=_L
_FsMIOspfIfAuthKey_Object=MibTableColumn
fsMIOspfIfAuthKey=_FsMIOspfIfAuthKey_Object((1,3,6,1,4,1,10876,101,1,145,17,1,4),_FsMIOspfIfAuthKey_Type())
fsMIOspfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfAuthKey.setStatus(_A)
_FsMIOspfIfAuthKeyStartAccept_Type=DateAndTime
_FsMIOspfIfAuthKeyStartAccept_Object=MibTableColumn
fsMIOspfIfAuthKeyStartAccept=_FsMIOspfIfAuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,145,17,1,5),_FsMIOspfIfAuthKeyStartAccept_Type())
fsMIOspfIfAuthKeyStartAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfAuthKeyStartAccept.setStatus(_A)
_FsMIOspfIfAuthKeyStartGenerate_Type=DateAndTime
_FsMIOspfIfAuthKeyStartGenerate_Object=MibTableColumn
fsMIOspfIfAuthKeyStartGenerate=_FsMIOspfIfAuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,145,17,1,6),_FsMIOspfIfAuthKeyStartGenerate_Type())
fsMIOspfIfAuthKeyStartGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfAuthKeyStartGenerate.setStatus(_A)
_FsMIOspfIfAuthKeyStopGenerate_Type=DateAndTime
_FsMIOspfIfAuthKeyStopGenerate_Object=MibTableColumn
fsMIOspfIfAuthKeyStopGenerate=_FsMIOspfIfAuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,145,17,1,7),_FsMIOspfIfAuthKeyStopGenerate_Type())
fsMIOspfIfAuthKeyStopGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfAuthKeyStopGenerate.setStatus(_A)
_FsMIOspfIfAuthKeyStopAccept_Type=DateAndTime
_FsMIOspfIfAuthKeyStopAccept_Object=MibTableColumn
fsMIOspfIfAuthKeyStopAccept=_FsMIOspfIfAuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,145,17,1,8),_FsMIOspfIfAuthKeyStopAccept_Type())
fsMIOspfIfAuthKeyStopAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfAuthKeyStopAccept.setStatus(_A)
class _FsMIOspfIfAuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_R,1),(_S,3)))
_FsMIOspfIfAuthKeyStatus_Type.__name__=_B
_FsMIOspfIfAuthKeyStatus_Object=MibTableColumn
fsMIOspfIfAuthKeyStatus=_FsMIOspfIfAuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,145,17,1,9),_FsMIOspfIfAuthKeyStatus_Type())
fsMIOspfIfAuthKeyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfIfAuthKeyStatus.setStatus(_A)
_FsMIOspfVirtIfAuthTable_Object=MibTable
fsMIOspfVirtIfAuthTable=_FsMIOspfVirtIfAuthTable_Object((1,3,6,1,4,1,10876,101,1,145,18))
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthTable.setStatus(_A)
_FsMIOspfVirtIfAuthEntry_Object=MibTableRow
fsMIOspfVirtIfAuthEntry=_FsMIOspfVirtIfAuthEntry_Object((1,3,6,1,4,1,10876,101,1,145,18,1))
fsMIOspfVirtIfAuthEntry.setIndexNames((0,_G,_H),(0,_E,_AT),(0,_E,_AU),(0,_E,_AV))
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthEntry.setStatus(_A)
_FsMIOspfVirtIfAuthAreaId_Type=AreaID
_FsMIOspfVirtIfAuthAreaId_Object=MibTableColumn
fsMIOspfVirtIfAuthAreaId=_FsMIOspfVirtIfAuthAreaId_Object((1,3,6,1,4,1,10876,101,1,145,18,1,1),_FsMIOspfVirtIfAuthAreaId_Type())
fsMIOspfVirtIfAuthAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthAreaId.setStatus(_A)
_FsMIOspfVirtIfAuthNeighbor_Type=RouterID
_FsMIOspfVirtIfAuthNeighbor_Object=MibTableColumn
fsMIOspfVirtIfAuthNeighbor=_FsMIOspfVirtIfAuthNeighbor_Object((1,3,6,1,4,1,10876,101,1,145,18,1,2),_FsMIOspfVirtIfAuthNeighbor_Type())
fsMIOspfVirtIfAuthNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthNeighbor.setStatus(_A)
class _FsMIOspfVirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfVirtIfAuthKeyId_Type.__name__=_B
_FsMIOspfVirtIfAuthKeyId_Object=MibTableColumn
fsMIOspfVirtIfAuthKeyId=_FsMIOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,145,18,1,3),_FsMIOspfVirtIfAuthKeyId_Type())
fsMIOspfVirtIfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKeyId.setStatus(_A)
class _FsMIOspfVirtIfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIOspfVirtIfAuthKey_Type.__name__=_L
_FsMIOspfVirtIfAuthKey_Object=MibTableColumn
fsMIOspfVirtIfAuthKey=_FsMIOspfVirtIfAuthKey_Object((1,3,6,1,4,1,10876,101,1,145,18,1,4),_FsMIOspfVirtIfAuthKey_Type())
fsMIOspfVirtIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKey.setStatus(_A)
_FsMIOspfVirtIfAuthKeyStartAccept_Type=DateAndTime
_FsMIOspfVirtIfAuthKeyStartAccept_Object=MibTableColumn
fsMIOspfVirtIfAuthKeyStartAccept=_FsMIOspfVirtIfAuthKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,145,18,1,5),_FsMIOspfVirtIfAuthKeyStartAccept_Type())
fsMIOspfVirtIfAuthKeyStartAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKeyStartAccept.setStatus(_A)
_FsMIOspfVirtIfAuthKeyStartGenerate_Type=DateAndTime
_FsMIOspfVirtIfAuthKeyStartGenerate_Object=MibTableColumn
fsMIOspfVirtIfAuthKeyStartGenerate=_FsMIOspfVirtIfAuthKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,145,18,1,6),_FsMIOspfVirtIfAuthKeyStartGenerate_Type())
fsMIOspfVirtIfAuthKeyStartGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKeyStartGenerate.setStatus(_A)
_FsMIOspfVirtIfAuthKeyStopGenerate_Type=DateAndTime
_FsMIOspfVirtIfAuthKeyStopGenerate_Object=MibTableColumn
fsMIOspfVirtIfAuthKeyStopGenerate=_FsMIOspfVirtIfAuthKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,145,18,1,7),_FsMIOspfVirtIfAuthKeyStopGenerate_Type())
fsMIOspfVirtIfAuthKeyStopGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKeyStopGenerate.setStatus(_A)
_FsMIOspfVirtIfAuthKeyStopAccept_Type=DateAndTime
_FsMIOspfVirtIfAuthKeyStopAccept_Object=MibTableColumn
fsMIOspfVirtIfAuthKeyStopAccept=_FsMIOspfVirtIfAuthKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,145,18,1,8),_FsMIOspfVirtIfAuthKeyStopAccept_Type())
fsMIOspfVirtIfAuthKeyStopAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKeyStopAccept.setStatus(_A)
class _FsMIOspfVirtIfAuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_R,1),(_S,3)))
_FsMIOspfVirtIfAuthKeyStatus_Type.__name__=_B
_FsMIOspfVirtIfAuthKeyStatus_Object=MibTableColumn
fsMIOspfVirtIfAuthKeyStatus=_FsMIOspfVirtIfAuthKeyStatus_Object((1,3,6,1,4,1,10876,101,1,145,18,1,9),_FsMIOspfVirtIfAuthKeyStatus_Type())
fsMIOspfVirtIfAuthKeyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfVirtIfAuthKeyStatus.setStatus(_A)
_FsMIOspfTestGroup_ObjectIdentity=ObjectIdentity
fsMIOspfTestGroup=_FsMIOspfTestGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,100))
_FsMIOspfNotification_ObjectIdentity=ObjectIdentity
fsMIOspfNotification=_FsMIOspfNotification_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,101))
_FsMIOspfTraps_ObjectIdentity=ObjectIdentity
fsMIOspfTraps=_FsMIOspfTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,145,101,0))
fsMIStdOspfEntry.registerAugmentions((_E,_AW))
fsMIOspfEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
fsMIStdOspfEntry.registerAugmentions((_E,_AX))
fsMIOspfOpaqueEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
fsMIOspfIfEntry.registerAugmentions((_E,_AY))
fsMIOspfOpaqueInterfaceEntry.setIndexNames(*fsMIOspfIfEntry.getIndexNames())
fsMIStdOspfEntry.registerAugmentions((_E,_AZ))
fsMIOspfRRDRouteEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
fsMIStdOspfVirtNbrEntry.registerAugmentions((_E,_Aa))
fsMIOspfVirtNbrEntry.setIndexNames(*fsMIStdOspfVirtNbrEntry.getIndexNames())
fsMIOspfRestartStatusChange=NotificationType((1,3,6,1,4,1,10876,101,1,145,101,0,1))
fsMIOspfRestartStatusChange.setObjects(*((_G,_N),(_E,_Ab),(_E,_Ac),(_E,_Ad)))
if mibBuilder.loadTexts:fsMIOspfRestartStatusChange.setStatus(_A)
fsMIOspfNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,1,145,101,0,2))
fsMIOspfNbrRestartHelperStatusChange.setObjects(*((_G,_N),(_G,_c),(_E,_Ae),(_E,_Af),(_E,_Ag)))
if mibBuilder.loadTexts:fsMIOspfNbrRestartHelperStatusChange.setStatus(_A)
fsMIOspfVirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,1,145,101,0,3))
fsMIOspfVirtNbrRestartHelperStatusChange.setObjects(*((_G,_N),(_E,_Ah),(_E,_Ai),(_E,_Aj)))
if mibBuilder.loadTexts:fsMIOspfVirtNbrRestartHelperStatusChange.setStatus(_A)
fsMIOspfHotStandbyEventTrap=NotificationType((1,3,6,1,4,1,10876,101,1,145,101,0,4))
fsMIOspfHotStandbyEventTrap.setObjects(*((_G,_N),(_E,_Ak),(_E,_Al)))
if mibBuilder.loadTexts:fsMIOspfHotStandbyEventTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsMIOspf':fsMIOspf,'fsMIOspfGeneralGroup':fsMIOspfGeneralGroup,'fsMIOspfGlobalTraceLevel':fsMIOspfGlobalTraceLevel,'fsMIOspfVrfSpfInterval':fsMIOspfVrfSpfInterval,'fsMIOspfTable':fsMIOspfTable,_AW:fsMIOspfEntry,'fsMIOspfOverFlowState':fsMIOspfOverFlowState,'fsMIOspfPktsRcvd':fsMIOspfPktsRcvd,'fsMIOspfPktsTxed':fsMIOspfPktsTxed,'fsMIOspfPktsDisd':fsMIOspfPktsDisd,'fsMIOspfRFC1583Compatibility':fsMIOspfRFC1583Compatibility,'fsMIOspfTraceLevel':fsMIOspfTraceLevel,'fsMIOspfMinLsaInterval':fsMIOspfMinLsaInterval,'fsMIOspfABRType':fsMIOspfABRType,'fsMIOspfNssaAsbrDefRtTrans':fsMIOspfNssaAsbrDefRtTrans,'fsMIOspfDefaultPassiveInterface':fsMIOspfDefaultPassiveInterface,'fsMIOspfSpfHoldtime':fsMIOspfSpfHoldtime,'fsMIOspfSpfDelay':fsMIOspfSpfDelay,'fsMIOspfRestartSupport':fsMIOspfRestartSupport,_Ac:fsMIOspfRestartInterval,'fsMIOspfRestartStrictLsaChecking':fsMIOspfRestartStrictLsaChecking,_Ab:fsMIOspfRestartStatus,'fsMIOspfRestartAge':fsMIOspfRestartAge,_Ad:fsMIOspfRestartExitReason,'fsMIOspfHelperSupport':fsMIOspfHelperSupport,'fsMIOspfExtTraceLevel':fsMIOspfExtTraceLevel,'fsMIOspfHelperGraceTimeLimit':fsMIOspfHelperGraceTimeLimit,'fsMIOspfRestartAckState':fsMIOspfRestartAckState,'fsMIOspfGraceLsaRetransmitCount':fsMIOspfGraceLsaRetransmitCount,'fsMIOspfRestartReason':fsMIOspfRestartReason,'fsMIOspfRTStaggeringInterval':fsMIOspfRTStaggeringInterval,'fsMIOspfRouterIdPermanence':fsMIOspfRouterIdPermanence,'fsMIOspfBfdStatus':fsMIOspfBfdStatus,'fsMIOspfBfdAllIfState':fsMIOspfBfdAllIfState,'fsMIOspfRTStaggeringStatus':fsMIOspfRTStaggeringStatus,'fsMIOspfHotStandbyAdminStatus':fsMIOspfHotStandbyAdminStatus,_Ak:fsMIOspfHotStandbyState,_Al:fsMIOspfDynamicBulkUpdStatus,'fsMIOspfStanbyHelloSyncCount':fsMIOspfStanbyHelloSyncCount,'fsMIOspfStanbyLsaSyncCount':fsMIOspfStanbyLsaSyncCount,'fsMIOspfGlobalExtTraceLevel':fsMIOspfGlobalExtTraceLevel,'fsMIOspfAreaTable':fsMIOspfAreaTable,'fsMIOspfAreaEntry':fsMIOspfAreaEntry,_h:fsMIOspfAreaId,'fsMIOspfAreaIfCount':fsMIOspfAreaIfCount,'fsMIOspfAreaNetCount':fsMIOspfAreaNetCount,'fsMIOspfAreaRtrCount':fsMIOspfAreaRtrCount,'fsMIOspfAreaNSSATranslatorRole':fsMIOspfAreaNSSATranslatorRole,'fsMIOspfAreaNSSATranslatorState':fsMIOspfAreaNSSATranslatorState,'fsMIOspfAreaNSSATranslatorStabilityInterval':fsMIOspfAreaNSSATranslatorStabilityInterval,'fsMIOspfAreaNSSATranslatorEvents':fsMIOspfAreaNSSATranslatorEvents,'fsMIOspfAreaDfInfOriginate':fsMIOspfAreaDfInfOriginate,'fsMIOspfHostTable':fsMIOspfHostTable,'fsMIOspfHostEntry':fsMIOspfHostEntry,_i:fsMIOspfHostIpAddress,_j:fsMIOspfHostTOS,'fsMIOspfHostRouteIfIndex':fsMIOspfHostRouteIfIndex,'fsMIOspfIfTable':fsMIOspfIfTable,'fsMIOspfIfEntry':fsMIOspfIfEntry,_k:fsMIOspfIfIpAddress,_l:fsMIOspfAddressLessIf,'fsMIOspfIfOperState':fsMIOspfIfOperState,'fsMIOspfIfPassive':fsMIOspfIfPassive,'fsMIOspfIfNbrCount':fsMIOspfIfNbrCount,'fsMIOspfIfAdjCount':fsMIOspfIfAdjCount,'fsMIOspfIfHelloRcvd':fsMIOspfIfHelloRcvd,'fsMIOspfIfHelloTxed':fsMIOspfIfHelloTxed,'fsMIOspfIfHelloDisd':fsMIOspfIfHelloDisd,'fsMIOspfIfDdpRcvd':fsMIOspfIfDdpRcvd,'fsMIOspfIfDdpTxed':fsMIOspfIfDdpTxed,'fsMIOspfIfDdpDisd':fsMIOspfIfDdpDisd,'fsMIOspfIfLrqRcvd':fsMIOspfIfLrqRcvd,'fsMIOspfIfLrqTxed':fsMIOspfIfLrqTxed,'fsMIOspfIfLrqDisd':fsMIOspfIfLrqDisd,'fsMIOspfIfLsuRcvd':fsMIOspfIfLsuRcvd,'fsMIOspfIfLsuTxed':fsMIOspfIfLsuTxed,'fsMIOspfIfLsuDisd':fsMIOspfIfLsuDisd,'fsMIOspfIfLakRcvd':fsMIOspfIfLakRcvd,'fsMIOspfIfLakTxed':fsMIOspfIfLakTxed,'fsMIOspfIfLakDisd':fsMIOspfIfLakDisd,'fsMIOspfIfBfdState':fsMIOspfIfBfdState,'fsMIOspfIfMD5AuthTable':fsMIOspfIfMD5AuthTable,'fsMIOspfIfMD5AuthEntry':fsMIOspfIfMD5AuthEntry,_m:fsMIOspfIfMD5AuthIpAddress,_n:fsMIOspfIfMD5AuthAddressLessIf,_o:fsMIOspfIfMD5AuthKeyId,'fsMIOspfIfMD5AuthKey':fsMIOspfIfMD5AuthKey,'fsMIOspfIfMD5AuthKeyStartAccept':fsMIOspfIfMD5AuthKeyStartAccept,'fsMIOspfIfMD5AuthKeyStartGenerate':fsMIOspfIfMD5AuthKeyStartGenerate,'fsMIOspfIfMD5AuthKeyStopGenerate':fsMIOspfIfMD5AuthKeyStopGenerate,'fsMIOspfIfMD5AuthKeyStopAccept':fsMIOspfIfMD5AuthKeyStopAccept,'fsMIOspfIfMD5AuthKeyStatus':fsMIOspfIfMD5AuthKeyStatus,'fsMIOspfVirtIfMD5AuthTable':fsMIOspfVirtIfMD5AuthTable,'fsMIOspfVirtIfMD5AuthEntry':fsMIOspfVirtIfMD5AuthEntry,_p:fsMIOspfVirtIfMD5AuthAreaId,_q:fsMIOspfVirtIfMD5AuthNeighbor,_r:fsMIOspfVirtIfMD5AuthKeyId,'fsMIOspfVirtIfMD5AuthKey':fsMIOspfVirtIfMD5AuthKey,'fsMIOspfVirtIfMD5AuthKeyStartAccept':fsMIOspfVirtIfMD5AuthKeyStartAccept,'fsMIOspfVirtIfMD5AuthKeyStartGenerate':fsMIOspfVirtIfMD5AuthKeyStartGenerate,'fsMIOspfVirtIfMD5AuthKeyStopGenerate':fsMIOspfVirtIfMD5AuthKeyStopGenerate,'fsMIOspfVirtIfMD5AuthKeyStopAccept':fsMIOspfVirtIfMD5AuthKeyStopAccept,'fsMIOspfVirtIfMD5AuthKeyStatus':fsMIOspfVirtIfMD5AuthKeyStatus,'fsMIOspfNbrTable':fsMIOspfNbrTable,'fsMIOspfNbrEntry':fsMIOspfNbrEntry,_s:fsMIOspfNbrIpAddr,_t:fsMIOspfNbrAddressLessIndex,'fsMIOspfNbrDBSummaryQLen':fsMIOspfNbrDBSummaryQLen,'fsMIOspfNbrLSReqQLen':fsMIOspfNbrLSReqQLen,_Ae:fsMIOspfNbrRestartHelperStatus,_Af:fsMIOspfNbrRestartHelperAge,_Ag:fsMIOspfNbrRestartHelperExitReason,'fsMIOspfNbrBfdState':fsMIOspfNbrBfdState,'fsMIOspfRoutingTable':fsMIOspfRoutingTable,'fsMIOspfRoutingEntry':fsMIOspfRoutingEntry,_w:fsMIOspfRouteIpAddr,_x:fsMIOspfRouteIpAddrMask,_y:fsMIOspfRouteIpTos,_z:fsMIOspfRouteIpNextHop,'fsMIOspfRouteType':fsMIOspfRouteType,'fsMIOspfRouteAreaId':fsMIOspfRouteAreaId,'fsMIOspfRouteCost':fsMIOspfRouteCost,'fsMIOspfRouteType2Cost':fsMIOspfRouteType2Cost,'fsMIOspfRouteInterfaceIndex':fsMIOspfRouteInterfaceIndex,'fsMIOspfSecIfTable':fsMIOspfSecIfTable,'fsMIOspfSecIfEntry':fsMIOspfSecIfEntry,_A2:fsMIOspfPrimIpAddr,_A3:fsMIOspfPrimAddresslessIf,_A4:fsMIOspfSecIpAddr,_A5:fsMIOspfSecIpAddrMask,'fsMIOspfSecIfStatus':fsMIOspfSecIfStatus,'fsMIOspfAreaAggregateTable':fsMIOspfAreaAggregateTable,'fsMIOspfAreaAggregateEntry':fsMIOspfAreaAggregateEntry,_A6:fsMIOspfAreaAggregateAreaID,_A7:fsMIOspfAreaAggregateLsdbType,_A8:fsMIOspfAreaAggregateNet,_A9:fsMIOspfAreaAggregateMask,'fsMIOspfAreaAggregateExternalTag':fsMIOspfAreaAggregateExternalTag,'fsMIOspfAsExternalAggregationTable':fsMIOspfAsExternalAggregationTable,'fsMIOspfAsExternalAggregationEntry':fsMIOspfAsExternalAggregationEntry,_AA:fsMIOspfAsExternalAggregationNet,_AB:fsMIOspfAsExternalAggregationMask,_AC:fsMIOspfAsExternalAggregationAreaId,'fsMIOspfAsExternalAggregationEffect':fsMIOspfAsExternalAggregationEffect,'fsMIOspfAsExternalAggregationTranslation':fsMIOspfAsExternalAggregationTranslation,'fsMIOspfAsExternalAggregationStatus':fsMIOspfAsExternalAggregationStatus,'fsMIOspfOpaqueLSAGroup':fsMIOspfOpaqueLSAGroup,'fsMIOspfOpaqueLSAGeneralGroup':fsMIOspfOpaqueLSAGeneralGroup,'fsMIOspfOpaqueTable':fsMIOspfOpaqueTable,_AX:fsMIOspfOpaqueEntry,'fsMIOspfOpaqueOption':fsMIOspfOpaqueOption,'fsMIOspfType11LsaCount':fsMIOspfType11LsaCount,'fsMIOspfType11LsaCksumSum':fsMIOspfType11LsaCksumSum,'fsMIOspfAreaIDValid':fsMIOspfAreaIDValid,'fsMIOspfOpaqueInterfaceTable':fsMIOspfOpaqueInterfaceTable,_AY:fsMIOspfOpaqueInterfaceEntry,'fsMIOspfOpaqueType9LsaCount':fsMIOspfOpaqueType9LsaCount,'fsMIOspfOpaqueType9LsaCksumSum':fsMIOspfOpaqueType9LsaCksumSum,'fsMIOspfType9LsdbTable':fsMIOspfType9LsdbTable,'fsMIOspfType9LsdbEntry':fsMIOspfType9LsdbEntry,_AD:fsMIOspfType9LsdbIfIpAddress,_AE:fsMIOspfType9LsdbOpaqueType,_AF:fsMIOspfType9LsdbLsid,_AG:fsMIOspfType9LsdbRouterId,'fsMIOspfType9LsdbSequence':fsMIOspfType9LsdbSequence,'fsMIOspfType9LsdbAge':fsMIOspfType9LsdbAge,'fsMIOspfType9LsdbChecksum':fsMIOspfType9LsdbChecksum,'fsMIOspfType9LsdbAdvertisement':fsMIOspfType9LsdbAdvertisement,'fsMIOspfType11LsdbTable':fsMIOspfType11LsdbTable,'fsMIOspfType11LsdbEntry':fsMIOspfType11LsdbEntry,_AH:fsMIOspfType11LsdbOpaqueType,_AI:fsMIOspfType11LsdbLsid,_AJ:fsMIOspfType11LsdbRouterId,'fsMIOspfType11LsdbSequence':fsMIOspfType11LsdbSequence,'fsMIOspfType11LsdbAge':fsMIOspfType11LsdbAge,'fsMIOspfType11LsdbChecksum':fsMIOspfType11LsdbChecksum,'fsMIOspfType11LsdbAdvertisement':fsMIOspfType11LsdbAdvertisement,'fsMIOspfAppInfoDbTable':fsMIOspfAppInfoDbTable,'fsMIOspfAppInfoDbEntry':fsMIOspfAppInfoDbEntry,_AK:fsMIOspfAppInfoDbAppid,'fsMIOspfAppInfoDbOpaqueType':fsMIOspfAppInfoDbOpaqueType,'fsMIOspfAppInfoDbLsaTypesSupported':fsMIOspfAppInfoDbLsaTypesSupported,'fsMIOspfAppInfoDbType9Gen':fsMIOspfAppInfoDbType9Gen,'fsMIOspfAppInfoDbType9Rcvd':fsMIOspfAppInfoDbType9Rcvd,'fsMIOspfAppInfoDbType10Gen':fsMIOspfAppInfoDbType10Gen,'fsMIOspfAppInfoDbType10Rcvd':fsMIOspfAppInfoDbType10Rcvd,'fsMIOspfAppInfoDbType11Gen':fsMIOspfAppInfoDbType11Gen,'fsMIOspfAppInfoDbType11Rcvd':fsMIOspfAppInfoDbType11Rcvd,'fsMIOspfRRDGroup':fsMIOspfRRDGroup,'fsMIOspfRRDGeneralGroup':fsMIOspfRRDGeneralGroup,'fsMIOspfRRDRouteTable':fsMIOspfRRDRouteTable,_AZ:fsMIOspfRRDRouteEntry,'fsMIOspfRRDStatus':fsMIOspfRRDStatus,'fsMIOspfRRDSrcProtoMaskEnable':fsMIOspfRRDSrcProtoMaskEnable,'fsMIOspfRRDSrcProtoMaskDisable':fsMIOspfRRDSrcProtoMaskDisable,'fsMIOspfRRDRouteMapEnable':fsMIOspfRRDRouteMapEnable,'fsMIOspfRRDRouteConfigTable':fsMIOspfRRDRouteConfigTable,'fsMIOspfRRDRouteConfigEntry':fsMIOspfRRDRouteConfigEntry,_AL:fsMIOspfRRDRouteDest,_AM:fsMIOspfRRDRouteMask,'fsMIOspfRRDRouteMetric':fsMIOspfRRDRouteMetric,'fsMIOspfRRDRouteMetricType':fsMIOspfRRDRouteMetricType,'fsMIOspfRRDRouteTagType':fsMIOspfRRDRouteTagType,'fsMIOspfRRDRouteTag':fsMIOspfRRDRouteTag,'fsMIOspfRRDRouteStatus':fsMIOspfRRDRouteStatus,'fsMIOspfRRDMetricTable':fsMIOspfRRDMetricTable,'fsMIOspfRRDMerticEntry':fsMIOspfRRDMerticEntry,_AN:fsMIOspfRRDProtocolId,'fsMIOspfRRDMetricValue':fsMIOspfRRDMetricValue,'fsMIOspfRRDMetricType':fsMIOspfRRDMetricType,'fsMIOspfVirtNbrTable':fsMIOspfVirtNbrTable,_Aa:fsMIOspfVirtNbrEntry,_Ah:fsMIOspfVirtNbrRestartHelperStatus,_Ai:fsMIOspfVirtNbrRestartHelperAge,_Aj:fsMIOspfVirtNbrRestartHelperExitReason,'fsMIospfDistInOutRouteMap':fsMIospfDistInOutRouteMap,'fsMIOspfDistInOutRouteMapTable':fsMIOspfDistInOutRouteMapTable,'fsMIOspfDistInOutRouteMapEntry':fsMIOspfDistInOutRouteMapEntry,_AO:fsMIOspfDistInOutRouteMapName,_AP:fsMIOspfDistInOutRouteMapType,'fsMIOspfDistInOutRouteMapValue':fsMIOspfDistInOutRouteMapValue,'fsMIOspfDistInOutRouteMapRowStatus':fsMIOspfDistInOutRouteMapRowStatus,'fsMIospfPreferenceGroup':fsMIospfPreferenceGroup,'fsMIOspfPreferenceTable':fsMIOspfPreferenceTable,'fsMIOspfPreferenceEntry':fsMIOspfPreferenceEntry,'fsMIOspfPreferenceValue':fsMIOspfPreferenceValue,'fsMIOspfIfAuthTable':fsMIOspfIfAuthTable,'fsMIOspfIfAuthEntry':fsMIOspfIfAuthEntry,_AQ:fsMIOspfIfAuthIpAddress,_AR:fsMIOspfIfAuthAddressLessIf,_AS:fsMIOspfIfAuthKeyId,'fsMIOspfIfAuthKey':fsMIOspfIfAuthKey,'fsMIOspfIfAuthKeyStartAccept':fsMIOspfIfAuthKeyStartAccept,'fsMIOspfIfAuthKeyStartGenerate':fsMIOspfIfAuthKeyStartGenerate,'fsMIOspfIfAuthKeyStopGenerate':fsMIOspfIfAuthKeyStopGenerate,'fsMIOspfIfAuthKeyStopAccept':fsMIOspfIfAuthKeyStopAccept,'fsMIOspfIfAuthKeyStatus':fsMIOspfIfAuthKeyStatus,'fsMIOspfVirtIfAuthTable':fsMIOspfVirtIfAuthTable,'fsMIOspfVirtIfAuthEntry':fsMIOspfVirtIfAuthEntry,_AT:fsMIOspfVirtIfAuthAreaId,_AU:fsMIOspfVirtIfAuthNeighbor,_AV:fsMIOspfVirtIfAuthKeyId,'fsMIOspfVirtIfAuthKey':fsMIOspfVirtIfAuthKey,'fsMIOspfVirtIfAuthKeyStartAccept':fsMIOspfVirtIfAuthKeyStartAccept,'fsMIOspfVirtIfAuthKeyStartGenerate':fsMIOspfVirtIfAuthKeyStartGenerate,'fsMIOspfVirtIfAuthKeyStopGenerate':fsMIOspfVirtIfAuthKeyStopGenerate,'fsMIOspfVirtIfAuthKeyStopAccept':fsMIOspfVirtIfAuthKeyStopAccept,'fsMIOspfVirtIfAuthKeyStatus':fsMIOspfVirtIfAuthKeyStatus,'fsMIOspfTestGroup':fsMIOspfTestGroup,'fsMIOspfNotification':fsMIOspfNotification,'fsMIOspfTraps':fsMIOspfTraps,'fsMIOspfRestartStatusChange':fsMIOspfRestartStatusChange,'fsMIOspfNbrRestartHelperStatusChange':fsMIOspfNbrRestartHelperStatusChange,'fsMIOspfVirtNbrRestartHelperStatusChange':fsMIOspfVirtNbrRestartHelperStatusChange,'fsMIOspfHotStandbyEventTrap':fsMIOspfHotStandbyEventTrap})