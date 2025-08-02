_AL='futOspfv3TrapBulkUpdAbortReason'
_AK='futOspfv3DynamicBulkUpdStatus'
_AJ='futOspfv3HotStandbyState'
_AI='futOspfv3TrapVirtNbrRtrId'
_AH='futOspfv3TrapVirtNbrArea'
_AG='futOspfv3TrapNbrRtrId'
_AF='futOspfv3TrapNbrIfIndex'
_AE='futOspfv3VirtIfCryptoAuthEntry'
_AD='futOspfv3NeighborBfdEntry'
_AC='futOspfv3VirtIfAuthKeyId'
_AB='futOspfv3VirtIfAuthNeighbor'
_AA='futOspfv3VirtIfAuthAreaId'
_A9='futOspfv3IfAuthKeyId'
_A8='futOspfv3IfAuthIfIndex'
_A7='futOspfv3DistInOutRouteMapType'
_A6='futOspfv3DistInOutRouteMapName'
_A5='futOspfv3RedistRoutePfxLength'
_A4='futOspfv3RedistRouteDest'
_A3='futOspfv3RedistRouteDestType'
_A2='futOspfv3BRRouteDestType'
_A1='futOspfv3BRRouteNextHop'
_A0='futOspfv3BRRouteNextHopType'
_z='futOspfv3BRRouteDest'
_y='futOspfv3AsExternalAggregationAreaId'
_x='futOspfv3AsExternalAggregationPfxLength'
_w='futOspfv3AsExternalAggregationNet'
_v='futOspfv3AsExternalAggregationNetType'
_u='type2External'
_t='type1External'
_s='interArea'
_r='intraArea'
_q='futOspfv3RouteNextHop'
_p='futOspfv3RouteNextHopType'
_o='futOspfv3RoutePfxLength'
_n='futOspfv3RouteDest'
_m='futOspfv3RouteDestType'
_l='transition'
_k='sha512'
_j='sha384'
_i='sha256'
_h='futOspfv3IfIndex'
_g='switchToRedundant'
_f='swReloadUpgrade'
_e='softwareRestart'
_d='unknown'
_c='DisplayString'
_b='ospfv3VirtNbrRestartHelperStatus'
_a='ospfv3VirtNbrRestartHelperExitReason'
_Z='ospfv3VirtNbrRestartHelperAge'
_Y='ospfv3RestartStatus'
_X='ospfv3RestartInterval'
_W='ospfv3RestartExitReason'
_V='ospfv3NbrRestartHelperStatus'
_U='ospfv3NbrRestartHelperExitReason'
_T='ospfv3NbrRestartHelperAge'
_S='Status'
_R='BigMetric'
_Q='InterfaceIndex'
_P='read-create'
_O='OctetString'
_N='accessible-for-notify'
_M='none'
_L='TruthValue'
_K='InetAddress'
_J='ospfv3RouterId'
_I='disabled'
_H='enabled'
_G='OSPFV3-MIB'
_F='not-accessible'
_E='ARICENT-OSPFV3-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_Q)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,'InetAddressPrefixLength','InetAddressType')
AreaID,BigMetric,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB','AreaID',_R,'RouterID',_S)
ospfv3NbrEntry,ospfv3NbrRestartHelperAge,ospfv3NbrRestartHelperExitReason,ospfv3NbrRestartHelperStatus,ospfv3RestartExitReason,ospfv3RestartInterval,ospfv3RestartStatus,ospfv3RouterId,ospfv3VirtIfEntry,ospfv3VirtNbrRestartHelperAge,ospfv3VirtNbrRestartHelperExitReason,ospfv3VirtNbrRestartHelperStatus=mibBuilder.importSymbols(_G,'ospfv3NbrEntry',_T,_U,_V,_W,_X,_Y,_J,'ospfv3VirtIfEntry',_Z,_a,_b)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_c,'PhysAddress','RowStatus','TextualConvention',_L)
futospfv3=ModuleIdentity((1,3,6,1,4,1,2076,90))
if mibBuilder.loadTexts:futospfv3.setRevisions(('2012-09-05 00:00',))
_Futospfv3GeneralGroup_ObjectIdentity=ObjectIdentity
futospfv3GeneralGroup=_Futospfv3GeneralGroup_ObjectIdentity((1,3,6,1,4,1,2076,90,1))
class _FutOspfv3OverFlowState_Type(TruthValue):defaultValue=2
_FutOspfv3OverFlowState_Type.__name__=_L
_FutOspfv3OverFlowState_Object=MibScalar
futOspfv3OverFlowState=_FutOspfv3OverFlowState_Object((1,3,6,1,4,1,2076,90,1,1),_FutOspfv3OverFlowState_Type())
futOspfv3OverFlowState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3OverFlowState.setStatus(_A)
class _FutOspfv3TraceLevel_Type(Integer32):defaultValue=2048
_FutOspfv3TraceLevel_Type.__name__=_C
_FutOspfv3TraceLevel_Object=MibScalar
futOspfv3TraceLevel=_FutOspfv3TraceLevel_Object((1,3,6,1,4,1,2076,90,1,2),_FutOspfv3TraceLevel_Type())
futOspfv3TraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3TraceLevel.setStatus(_A)
class _FutOspfv3ABRType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardABR',1),('ciscoABR',2),('ibmABR',3)))
_FutOspfv3ABRType_Type.__name__=_C
_FutOspfv3ABRType_Object=MibScalar
futOspfv3ABRType=_FutOspfv3ABRType_Object((1,3,6,1,4,1,2076,90,1,3),_FutOspfv3ABRType_Type())
futOspfv3ABRType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3ABRType.setStatus(_A)
class _FutOspfv3NssaAsbrDefRtTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3NssaAsbrDefRtTrans_Type.__name__=_C
_FutOspfv3NssaAsbrDefRtTrans_Object=MibScalar
futOspfv3NssaAsbrDefRtTrans=_FutOspfv3NssaAsbrDefRtTrans_Object((1,3,6,1,4,1,2076,90,1,4),_FutOspfv3NssaAsbrDefRtTrans_Type())
futOspfv3NssaAsbrDefRtTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3NssaAsbrDefRtTrans.setStatus(_A)
class _FutOspfv3DefaultPassiveInterface_Type(TruthValue):defaultValue=2
_FutOspfv3DefaultPassiveInterface_Type.__name__=_L
_FutOspfv3DefaultPassiveInterface_Object=MibScalar
futOspfv3DefaultPassiveInterface=_FutOspfv3DefaultPassiveInterface_Object((1,3,6,1,4,1,2076,90,1,5),_FutOspfv3DefaultPassiveInterface_Type())
futOspfv3DefaultPassiveInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3DefaultPassiveInterface.setStatus(_A)
class _FutOspfv3SpfDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfv3SpfDelay_Type.__name__=_C
_FutOspfv3SpfDelay_Object=MibScalar
futOspfv3SpfDelay=_FutOspfv3SpfDelay_Object((1,3,6,1,4,1,2076,90,1,6),_FutOspfv3SpfDelay_Type())
futOspfv3SpfDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3SpfDelay.setStatus(_A)
class _FutOspfv3SpfHoldTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfv3SpfHoldTime_Type.__name__=_C
_FutOspfv3SpfHoldTime_Object=MibScalar
futOspfv3SpfHoldTime=_FutOspfv3SpfHoldTime_Object((1,3,6,1,4,1,2076,90,1,7),_FutOspfv3SpfHoldTime_Type())
futOspfv3SpfHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3SpfHoldTime.setStatus(_A)
class _FutOspfv3RTStaggeringInterval_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,2147483647))
_FutOspfv3RTStaggeringInterval_Type.__name__=_C
_FutOspfv3RTStaggeringInterval_Object=MibScalar
futOspfv3RTStaggeringInterval=_FutOspfv3RTStaggeringInterval_Object((1,3,6,1,4,1,2076,90,1,8),_FutOspfv3RTStaggeringInterval_Type())
futOspfv3RTStaggeringInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RTStaggeringInterval.setStatus(_A)
class _FutOspfv3RTStaggeringStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FutOspfv3RTStaggeringStatus_Type.__name__=_C
_FutOspfv3RTStaggeringStatus_Object=MibScalar
futOspfv3RTStaggeringStatus=_FutOspfv3RTStaggeringStatus_Object((1,3,6,1,4,1,2076,90,1,9),_FutOspfv3RTStaggeringStatus_Type())
futOspfv3RTStaggeringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RTStaggeringStatus.setStatus(_A)
class _FutOspfv3RestartStrictLsaChecking_Type(TruthValue):defaultValue=2
_FutOspfv3RestartStrictLsaChecking_Type.__name__=_L
_FutOspfv3RestartStrictLsaChecking_Object=MibScalar
futOspfv3RestartStrictLsaChecking=_FutOspfv3RestartStrictLsaChecking_Object((1,3,6,1,4,1,2076,90,1,10),_FutOspfv3RestartStrictLsaChecking_Type())
futOspfv3RestartStrictLsaChecking.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RestartStrictLsaChecking.setStatus(_A)
class _FutOspfv3HelperSupport_Type(Bits):namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3)))
_FutOspfv3HelperSupport_Type.__name__='Bits'
_FutOspfv3HelperSupport_Object=MibScalar
futOspfv3HelperSupport=_FutOspfv3HelperSupport_Object((1,3,6,1,4,1,2076,90,1,11),_FutOspfv3HelperSupport_Type())
futOspfv3HelperSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3HelperSupport.setStatus(_A)
class _FutOspfv3HelperGraceTimeLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_FutOspfv3HelperGraceTimeLimit_Type.__name__=_C
_FutOspfv3HelperGraceTimeLimit_Object=MibScalar
futOspfv3HelperGraceTimeLimit=_FutOspfv3HelperGraceTimeLimit_Object((1,3,6,1,4,1,2076,90,1,12),_FutOspfv3HelperGraceTimeLimit_Type())
futOspfv3HelperGraceTimeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3HelperGraceTimeLimit.setStatus(_A)
class _FutOspfv3RestartAckState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3RestartAckState_Type.__name__=_C
_FutOspfv3RestartAckState_Object=MibScalar
futOspfv3RestartAckState=_FutOspfv3RestartAckState_Object((1,3,6,1,4,1,2076,90,1,13),_FutOspfv3RestartAckState_Type())
futOspfv3RestartAckState.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RestartAckState.setStatus(_A)
class _FutOspfv3GraceLsaRetransmitCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FutOspfv3GraceLsaRetransmitCount_Type.__name__=_C
_FutOspfv3GraceLsaRetransmitCount_Object=MibScalar
futOspfv3GraceLsaRetransmitCount=_FutOspfv3GraceLsaRetransmitCount_Object((1,3,6,1,4,1,2076,90,1,14),_FutOspfv3GraceLsaRetransmitCount_Type())
futOspfv3GraceLsaRetransmitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3GraceLsaRetransmitCount.setStatus(_A)
class _FutOspfv3RestartReason_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3)))
_FutOspfv3RestartReason_Type.__name__=_C
_FutOspfv3RestartReason_Object=MibScalar
futOspfv3RestartReason=_FutOspfv3RestartReason_Object((1,3,6,1,4,1,2076,90,1,15),_FutOspfv3RestartReason_Type())
futOspfv3RestartReason.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RestartReason.setStatus(_A)
_FutOspfv3ExtTraceLevel_Type=Integer32
_FutOspfv3ExtTraceLevel_Object=MibScalar
futOspfv3ExtTraceLevel=_FutOspfv3ExtTraceLevel_Object((1,3,6,1,4,1,2076,90,1,16),_FutOspfv3ExtTraceLevel_Type())
futOspfv3ExtTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3ExtTraceLevel.setStatus(_A)
_FutOspfv3SetTraps_Type=Integer32
_FutOspfv3SetTraps_Object=MibScalar
futOspfv3SetTraps=_FutOspfv3SetTraps_Object((1,3,6,1,4,1,2076,90,1,17),_FutOspfv3SetTraps_Type())
futOspfv3SetTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3SetTraps.setStatus(_A)
class _FutOspfv3HotStandbyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3HotStandbyAdminStatus_Type.__name__=_C
_FutOspfv3HotStandbyAdminStatus_Object=MibScalar
futOspfv3HotStandbyAdminStatus=_FutOspfv3HotStandbyAdminStatus_Object((1,3,6,1,4,1,2076,90,1,18),_FutOspfv3HotStandbyAdminStatus_Type())
futOspfv3HotStandbyAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3HotStandbyAdminStatus.setStatus(_A)
class _FutOspfv3HotStandbyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FutOspfv3HotStandbyState_Type.__name__=_C
_FutOspfv3HotStandbyState_Object=MibScalar
futOspfv3HotStandbyState=_FutOspfv3HotStandbyState_Object((1,3,6,1,4,1,2076,90,1,19),_FutOspfv3HotStandbyState_Type())
futOspfv3HotStandbyState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3HotStandbyState.setStatus(_A)
class _FutOspfv3DynamicBulkUpdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('completed',3),('aborted',4)))
_FutOspfv3DynamicBulkUpdStatus_Type.__name__=_C
_FutOspfv3DynamicBulkUpdStatus_Object=MibScalar
futOspfv3DynamicBulkUpdStatus=_FutOspfv3DynamicBulkUpdStatus_Object((1,3,6,1,4,1,2076,90,1,20),_FutOspfv3DynamicBulkUpdStatus_Type())
futOspfv3DynamicBulkUpdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3DynamicBulkUpdStatus.setStatus(_A)
_FutOspfv3StandbyHelloSyncCount_Type=Counter32
_FutOspfv3StandbyHelloSyncCount_Object=MibScalar
futOspfv3StandbyHelloSyncCount=_FutOspfv3StandbyHelloSyncCount_Object((1,3,6,1,4,1,2076,90,1,21),_FutOspfv3StandbyHelloSyncCount_Type())
futOspfv3StandbyHelloSyncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3StandbyHelloSyncCount.setStatus(_A)
_FutOspfv3StandbyLsaSyncCount_Type=Counter32
_FutOspfv3StandbyLsaSyncCount_Object=MibScalar
futOspfv3StandbyLsaSyncCount=_FutOspfv3StandbyLsaSyncCount_Object((1,3,6,1,4,1,2076,90,1,22),_FutOspfv3StandbyLsaSyncCount_Type())
futOspfv3StandbyLsaSyncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3StandbyLsaSyncCount.setStatus(_A)
class _FutOspfv3BfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3BfdStatus_Type.__name__=_C
_FutOspfv3BfdStatus_Object=MibScalar
futOspfv3BfdStatus=_FutOspfv3BfdStatus_Object((1,3,6,1,4,1,2076,90,1,23),_FutOspfv3BfdStatus_Type())
futOspfv3BfdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3BfdStatus.setStatus(_A)
class _FutOspfv3BfdAllIfState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3BfdAllIfState_Type.__name__=_C
_FutOspfv3BfdAllIfState_Object=MibScalar
futOspfv3BfdAllIfState=_FutOspfv3BfdAllIfState_Object((1,3,6,1,4,1,2076,90,1,24),_FutOspfv3BfdAllIfState_Type())
futOspfv3BfdAllIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3BfdAllIfState.setStatus(_A)
_FutOspfv3IfTable_Object=MibTable
futOspfv3IfTable=_FutOspfv3IfTable_Object((1,3,6,1,4,1,2076,90,2))
if mibBuilder.loadTexts:futOspfv3IfTable.setStatus(_A)
_FutOspfv3IfEntry_Object=MibTableRow
futOspfv3IfEntry=_FutOspfv3IfEntry_Object((1,3,6,1,4,1,2076,90,2,1))
futOspfv3IfEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:futOspfv3IfEntry.setStatus(_A)
_FutOspfv3IfIndex_Type=InterfaceIndex
_FutOspfv3IfIndex_Object=MibTableColumn
futOspfv3IfIndex=_FutOspfv3IfIndex_Object((1,3,6,1,4,1,2076,90,2,1,1),_FutOspfv3IfIndex_Type())
futOspfv3IfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3IfIndex.setStatus(_A)
class _FutOspfv3IfOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operup',1),('operdown',2),('loopback',3),('unloop',4)))
_FutOspfv3IfOperState_Type.__name__=_C
_FutOspfv3IfOperState_Object=MibTableColumn
futOspfv3IfOperState=_FutOspfv3IfOperState_Object((1,3,6,1,4,1,2076,90,2,1,2),_FutOspfv3IfOperState_Type())
futOspfv3IfOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfOperState.setStatus(_A)
class _FutOspfv3IfPassive_Type(TruthValue):defaultValue=2
_FutOspfv3IfPassive_Type.__name__=_L
_FutOspfv3IfPassive_Object=MibTableColumn
futOspfv3IfPassive=_FutOspfv3IfPassive_Object((1,3,6,1,4,1,2076,90,2,1,3),_FutOspfv3IfPassive_Type())
futOspfv3IfPassive.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfPassive.setStatus(_A)
_FutOspfv3IfNbrCount_Type=Gauge32
_FutOspfv3IfNbrCount_Object=MibTableColumn
futOspfv3IfNbrCount=_FutOspfv3IfNbrCount_Object((1,3,6,1,4,1,2076,90,2,1,4),_FutOspfv3IfNbrCount_Type())
futOspfv3IfNbrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfNbrCount.setStatus(_A)
_FutOspfv3IfAdjCount_Type=Gauge32
_FutOspfv3IfAdjCount_Object=MibTableColumn
futOspfv3IfAdjCount=_FutOspfv3IfAdjCount_Object((1,3,6,1,4,1,2076,90,2,1,5),_FutOspfv3IfAdjCount_Type())
futOspfv3IfAdjCount.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfAdjCount.setStatus(_A)
_FutOspfv3IfHelloRcvd_Type=Counter32
_FutOspfv3IfHelloRcvd_Object=MibTableColumn
futOspfv3IfHelloRcvd=_FutOspfv3IfHelloRcvd_Object((1,3,6,1,4,1,2076,90,2,1,6),_FutOspfv3IfHelloRcvd_Type())
futOspfv3IfHelloRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfHelloRcvd.setStatus(_A)
_FutOspfv3IfHelloTxed_Type=Counter32
_FutOspfv3IfHelloTxed_Object=MibTableColumn
futOspfv3IfHelloTxed=_FutOspfv3IfHelloTxed_Object((1,3,6,1,4,1,2076,90,2,1,7),_FutOspfv3IfHelloTxed_Type())
futOspfv3IfHelloTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfHelloTxed.setStatus(_A)
_FutOspfv3IfHelloDisd_Type=Counter32
_FutOspfv3IfHelloDisd_Object=MibTableColumn
futOspfv3IfHelloDisd=_FutOspfv3IfHelloDisd_Object((1,3,6,1,4,1,2076,90,2,1,8),_FutOspfv3IfHelloDisd_Type())
futOspfv3IfHelloDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfHelloDisd.setStatus(_A)
_FutOspfv3IfDdpRcvd_Type=Counter32
_FutOspfv3IfDdpRcvd_Object=MibTableColumn
futOspfv3IfDdpRcvd=_FutOspfv3IfDdpRcvd_Object((1,3,6,1,4,1,2076,90,2,1,9),_FutOspfv3IfDdpRcvd_Type())
futOspfv3IfDdpRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfDdpRcvd.setStatus(_A)
_FutOspfv3IfDdpTxed_Type=Counter32
_FutOspfv3IfDdpTxed_Object=MibTableColumn
futOspfv3IfDdpTxed=_FutOspfv3IfDdpTxed_Object((1,3,6,1,4,1,2076,90,2,1,10),_FutOspfv3IfDdpTxed_Type())
futOspfv3IfDdpTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfDdpTxed.setStatus(_A)
_FutOspfv3IfDdpDisd_Type=Counter32
_FutOspfv3IfDdpDisd_Object=MibTableColumn
futOspfv3IfDdpDisd=_FutOspfv3IfDdpDisd_Object((1,3,6,1,4,1,2076,90,2,1,11),_FutOspfv3IfDdpDisd_Type())
futOspfv3IfDdpDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfDdpDisd.setStatus(_A)
_FutOspfv3IfLrqRcvd_Type=Counter32
_FutOspfv3IfLrqRcvd_Object=MibTableColumn
futOspfv3IfLrqRcvd=_FutOspfv3IfLrqRcvd_Object((1,3,6,1,4,1,2076,90,2,1,12),_FutOspfv3IfLrqRcvd_Type())
futOspfv3IfLrqRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLrqRcvd.setStatus(_A)
_FutOspfv3IfLrqTxed_Type=Counter32
_FutOspfv3IfLrqTxed_Object=MibTableColumn
futOspfv3IfLrqTxed=_FutOspfv3IfLrqTxed_Object((1,3,6,1,4,1,2076,90,2,1,13),_FutOspfv3IfLrqTxed_Type())
futOspfv3IfLrqTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLrqTxed.setStatus(_A)
_FutOspfv3IfLrqDisd_Type=Counter32
_FutOspfv3IfLrqDisd_Object=MibTableColumn
futOspfv3IfLrqDisd=_FutOspfv3IfLrqDisd_Object((1,3,6,1,4,1,2076,90,2,1,14),_FutOspfv3IfLrqDisd_Type())
futOspfv3IfLrqDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLrqDisd.setStatus(_A)
_FutOspfv3IfLsuRcvd_Type=Counter32
_FutOspfv3IfLsuRcvd_Object=MibTableColumn
futOspfv3IfLsuRcvd=_FutOspfv3IfLsuRcvd_Object((1,3,6,1,4,1,2076,90,2,1,15),_FutOspfv3IfLsuRcvd_Type())
futOspfv3IfLsuRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLsuRcvd.setStatus(_A)
_FutOspfv3IfLsuTxed_Type=Counter32
_FutOspfv3IfLsuTxed_Object=MibTableColumn
futOspfv3IfLsuTxed=_FutOspfv3IfLsuTxed_Object((1,3,6,1,4,1,2076,90,2,1,16),_FutOspfv3IfLsuTxed_Type())
futOspfv3IfLsuTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLsuTxed.setStatus(_A)
_FutOspfv3IfLsuDisd_Type=Counter32
_FutOspfv3IfLsuDisd_Object=MibTableColumn
futOspfv3IfLsuDisd=_FutOspfv3IfLsuDisd_Object((1,3,6,1,4,1,2076,90,2,1,17),_FutOspfv3IfLsuDisd_Type())
futOspfv3IfLsuDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLsuDisd.setStatus(_A)
_FutOspfv3IfLakRcvd_Type=Counter32
_FutOspfv3IfLakRcvd_Object=MibTableColumn
futOspfv3IfLakRcvd=_FutOspfv3IfLakRcvd_Object((1,3,6,1,4,1,2076,90,2,1,18),_FutOspfv3IfLakRcvd_Type())
futOspfv3IfLakRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLakRcvd.setStatus(_A)
_FutOspfv3IfLakTxed_Type=Counter32
_FutOspfv3IfLakTxed_Object=MibTableColumn
futOspfv3IfLakTxed=_FutOspfv3IfLakTxed_Object((1,3,6,1,4,1,2076,90,2,1,19),_FutOspfv3IfLakTxed_Type())
futOspfv3IfLakTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLakTxed.setStatus(_A)
_FutOspfv3IfLakDisd_Type=Counter32
_FutOspfv3IfLakDisd_Object=MibTableColumn
futOspfv3IfLakDisd=_FutOspfv3IfLakDisd_Object((1,3,6,1,4,1,2076,90,2,1,20),_FutOspfv3IfLakDisd_Type())
futOspfv3IfLakDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfLakDisd.setStatus(_A)
class _FutOspfv3IfLinkLSASuppression_Type(TruthValue):defaultValue=2
_FutOspfv3IfLinkLSASuppression_Type.__name__=_L
_FutOspfv3IfLinkLSASuppression_Object=MibTableColumn
futOspfv3IfLinkLSASuppression=_FutOspfv3IfLinkLSASuppression_Object((1,3,6,1,4,1,2076,90,2,1,21),_FutOspfv3IfLinkLSASuppression_Type())
futOspfv3IfLinkLSASuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfLinkLSASuppression.setStatus(_A)
class _FutOspfv3IfBfdState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3IfBfdState_Type.__name__=_C
_FutOspfv3IfBfdState_Object=MibTableColumn
futOspfv3IfBfdState=_FutOspfv3IfBfdState_Object((1,3,6,1,4,1,2076,90,2,1,22),_FutOspfv3IfBfdState_Type())
futOspfv3IfBfdState.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfBfdState.setStatus(_A)
class _FutOspfv3IfCryptoAuthType_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6)));namedValues=NamedValues(*(('sha1',1),(_i,3),(_j,4),(_k,5),(_M,6)))
_FutOspfv3IfCryptoAuthType_Type.__name__=_C
_FutOspfv3IfCryptoAuthType_Object=MibTableColumn
futOspfv3IfCryptoAuthType=_FutOspfv3IfCryptoAuthType_Object((1,3,6,1,4,1,2076,90,2,1,23),_FutOspfv3IfCryptoAuthType_Type())
futOspfv3IfCryptoAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfCryptoAuthType.setStatus(_A)
class _FutOspfv3IfCryptoAuthMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),(_l,2),(_M,3)))
_FutOspfv3IfCryptoAuthMode_Type.__name__=_C
_FutOspfv3IfCryptoAuthMode_Object=MibTableColumn
futOspfv3IfCryptoAuthMode=_FutOspfv3IfCryptoAuthMode_Object((1,3,6,1,4,1,2076,90,2,1,24),_FutOspfv3IfCryptoAuthMode_Type())
futOspfv3IfCryptoAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfCryptoAuthMode.setStatus(_A)
_FutOspfv3IfAuthTxed_Type=Counter32
_FutOspfv3IfAuthTxed_Object=MibTableColumn
futOspfv3IfAuthTxed=_FutOspfv3IfAuthTxed_Object((1,3,6,1,4,1,2076,90,2,1,25),_FutOspfv3IfAuthTxed_Type())
futOspfv3IfAuthTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfAuthTxed.setStatus(_A)
_FutOspfv3IfAuthRcvd_Type=Counter32
_FutOspfv3IfAuthRcvd_Object=MibTableColumn
futOspfv3IfAuthRcvd=_FutOspfv3IfAuthRcvd_Object((1,3,6,1,4,1,2076,90,2,1,26),_FutOspfv3IfAuthRcvd_Type())
futOspfv3IfAuthRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfAuthRcvd.setStatus(_A)
_FutOspfv3IfAuthDisd_Type=Counter32
_FutOspfv3IfAuthDisd_Object=MibTableColumn
futOspfv3IfAuthDisd=_FutOspfv3IfAuthDisd_Object((1,3,6,1,4,1,2076,90,2,1,27),_FutOspfv3IfAuthDisd_Type())
futOspfv3IfAuthDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3IfAuthDisd.setStatus(_A)
_FutOspfv3RoutingTable_Object=MibTable
futOspfv3RoutingTable=_FutOspfv3RoutingTable_Object((1,3,6,1,4,1,2076,90,3))
if mibBuilder.loadTexts:futOspfv3RoutingTable.setStatus(_A)
_FutOspfv3RoutingEntry_Object=MibTableRow
futOspfv3RoutingEntry=_FutOspfv3RoutingEntry_Object((1,3,6,1,4,1,2076,90,3,1))
futOspfv3RoutingEntry.setIndexNames((0,_E,_m),(0,_E,_n),(0,_E,_o),(0,_E,_p),(0,_E,_q))
if mibBuilder.loadTexts:futOspfv3RoutingEntry.setStatus(_A)
_FutOspfv3RouteDestType_Type=InetAddressType
_FutOspfv3RouteDestType_Object=MibTableColumn
futOspfv3RouteDestType=_FutOspfv3RouteDestType_Object((1,3,6,1,4,1,2076,90,3,1,1),_FutOspfv3RouteDestType_Type())
futOspfv3RouteDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RouteDestType.setStatus(_A)
class _FutOspfv3RouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3RouteDest_Type.__name__=_K
_FutOspfv3RouteDest_Object=MibTableColumn
futOspfv3RouteDest=_FutOspfv3RouteDest_Object((1,3,6,1,4,1,2076,90,3,1,2),_FutOspfv3RouteDest_Type())
futOspfv3RouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RouteDest.setStatus(_A)
_FutOspfv3RoutePfxLength_Type=InetAddressPrefixLength
_FutOspfv3RoutePfxLength_Object=MibTableColumn
futOspfv3RoutePfxLength=_FutOspfv3RoutePfxLength_Object((1,3,6,1,4,1,2076,90,3,1,3),_FutOspfv3RoutePfxLength_Type())
futOspfv3RoutePfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RoutePfxLength.setStatus(_A)
_FutOspfv3RouteNextHopType_Type=InetAddressType
_FutOspfv3RouteNextHopType_Object=MibTableColumn
futOspfv3RouteNextHopType=_FutOspfv3RouteNextHopType_Object((1,3,6,1,4,1,2076,90,3,1,4),_FutOspfv3RouteNextHopType_Type())
futOspfv3RouteNextHopType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RouteNextHopType.setStatus(_A)
class _FutOspfv3RouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3RouteNextHop_Type.__name__=_K
_FutOspfv3RouteNextHop_Object=MibTableColumn
futOspfv3RouteNextHop=_FutOspfv3RouteNextHop_Object((1,3,6,1,4,1,2076,90,3,1,5),_FutOspfv3RouteNextHop_Type())
futOspfv3RouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RouteNextHop.setStatus(_A)
class _FutOspfv3RouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4),('type1ExternalNssa',6)))
_FutOspfv3RouteType_Type.__name__=_C
_FutOspfv3RouteType_Object=MibTableColumn
futOspfv3RouteType=_FutOspfv3RouteType_Object((1,3,6,1,4,1,2076,90,3,1,6),_FutOspfv3RouteType_Type())
futOspfv3RouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3RouteType.setStatus(_A)
_FutOspfv3RouteAreaId_Type=AreaID
_FutOspfv3RouteAreaId_Object=MibTableColumn
futOspfv3RouteAreaId=_FutOspfv3RouteAreaId_Object((1,3,6,1,4,1,2076,90,3,1,7),_FutOspfv3RouteAreaId_Type())
futOspfv3RouteAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3RouteAreaId.setStatus(_A)
_FutOspfv3RouteCost_Type=BigMetric
_FutOspfv3RouteCost_Object=MibTableColumn
futOspfv3RouteCost=_FutOspfv3RouteCost_Object((1,3,6,1,4,1,2076,90,3,1,8),_FutOspfv3RouteCost_Type())
futOspfv3RouteCost.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3RouteCost.setStatus(_A)
_FutOspfv3RouteType2Cost_Type=BigMetric
_FutOspfv3RouteType2Cost_Object=MibTableColumn
futOspfv3RouteType2Cost=_FutOspfv3RouteType2Cost_Object((1,3,6,1,4,1,2076,90,3,1,9),_FutOspfv3RouteType2Cost_Type())
futOspfv3RouteType2Cost.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3RouteType2Cost.setStatus(_A)
class _FutOspfv3RouteInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FutOspfv3RouteInterfaceIndex_Type.__name__=_C
_FutOspfv3RouteInterfaceIndex_Object=MibTableColumn
futOspfv3RouteInterfaceIndex=_FutOspfv3RouteInterfaceIndex_Object((1,3,6,1,4,1,2076,90,3,1,10),_FutOspfv3RouteInterfaceIndex_Type())
futOspfv3RouteInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3RouteInterfaceIndex.setStatus(_A)
_FutOspfv3AsExternalAggregationTable_Object=MibTable
futOspfv3AsExternalAggregationTable=_FutOspfv3AsExternalAggregationTable_Object((1,3,6,1,4,1,2076,90,4))
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationTable.setStatus(_A)
_FutOspfv3AsExternalAggregationEntry_Object=MibTableRow
futOspfv3AsExternalAggregationEntry=_FutOspfv3AsExternalAggregationEntry_Object((1,3,6,1,4,1,2076,90,4,1))
futOspfv3AsExternalAggregationEntry.setIndexNames((0,_E,_v),(0,_E,_w),(0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationEntry.setStatus(_A)
_FutOspfv3AsExternalAggregationNetType_Type=InetAddressType
_FutOspfv3AsExternalAggregationNetType_Object=MibTableColumn
futOspfv3AsExternalAggregationNetType=_FutOspfv3AsExternalAggregationNetType_Object((1,3,6,1,4,1,2076,90,4,1,1),_FutOspfv3AsExternalAggregationNetType_Type())
futOspfv3AsExternalAggregationNetType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationNetType.setStatus(_A)
class _FutOspfv3AsExternalAggregationNet_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3AsExternalAggregationNet_Type.__name__=_K
_FutOspfv3AsExternalAggregationNet_Object=MibTableColumn
futOspfv3AsExternalAggregationNet=_FutOspfv3AsExternalAggregationNet_Object((1,3,6,1,4,1,2076,90,4,1,2),_FutOspfv3AsExternalAggregationNet_Type())
futOspfv3AsExternalAggregationNet.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationNet.setStatus(_A)
_FutOspfv3AsExternalAggregationPfxLength_Type=InetAddressPrefixLength
_FutOspfv3AsExternalAggregationPfxLength_Object=MibTableColumn
futOspfv3AsExternalAggregationPfxLength=_FutOspfv3AsExternalAggregationPfxLength_Object((1,3,6,1,4,1,2076,90,4,1,3),_FutOspfv3AsExternalAggregationPfxLength_Type())
futOspfv3AsExternalAggregationPfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationPfxLength.setStatus(_A)
_FutOspfv3AsExternalAggregationAreaId_Type=AreaID
_FutOspfv3AsExternalAggregationAreaId_Object=MibTableColumn
futOspfv3AsExternalAggregationAreaId=_FutOspfv3AsExternalAggregationAreaId_Object((1,3,6,1,4,1,2076,90,4,1,4),_FutOspfv3AsExternalAggregationAreaId_Type())
futOspfv3AsExternalAggregationAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationAreaId.setStatus(_A)
class _FutOspfv3AsExternalAggregationEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertise',1),('doNotAdvertise',2),('allowAll',3),('denyAll',4)))
_FutOspfv3AsExternalAggregationEffect_Type.__name__=_C
_FutOspfv3AsExternalAggregationEffect_Object=MibTableColumn
futOspfv3AsExternalAggregationEffect=_FutOspfv3AsExternalAggregationEffect_Object((1,3,6,1,4,1,2076,90,4,1,5),_FutOspfv3AsExternalAggregationEffect_Type())
futOspfv3AsExternalAggregationEffect.setMaxAccess(_P)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationEffect.setStatus(_A)
class _FutOspfv3AsExternalAggregationTranslation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3AsExternalAggregationTranslation_Type.__name__=_C
_FutOspfv3AsExternalAggregationTranslation_Object=MibTableColumn
futOspfv3AsExternalAggregationTranslation=_FutOspfv3AsExternalAggregationTranslation_Object((1,3,6,1,4,1,2076,90,4,1,6),_FutOspfv3AsExternalAggregationTranslation_Type())
futOspfv3AsExternalAggregationTranslation.setMaxAccess(_P)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationTranslation.setStatus(_A)
_FutOspfv3AsExternalAggregationStatus_Type=RowStatus
_FutOspfv3AsExternalAggregationStatus_Object=MibTableColumn
futOspfv3AsExternalAggregationStatus=_FutOspfv3AsExternalAggregationStatus_Object((1,3,6,1,4,1,2076,90,4,1,7),_FutOspfv3AsExternalAggregationStatus_Type())
futOspfv3AsExternalAggregationStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:futOspfv3AsExternalAggregationStatus.setStatus(_A)
_FutOspfv3BRRouteTable_Object=MibTable
futOspfv3BRRouteTable=_FutOspfv3BRRouteTable_Object((1,3,6,1,4,1,2076,90,5))
if mibBuilder.loadTexts:futOspfv3BRRouteTable.setStatus(_A)
_FutOspfv3BRRouteEntry_Object=MibTableRow
futOspfv3BRRouteEntry=_FutOspfv3BRRouteEntry_Object((1,3,6,1,4,1,2076,90,5,1))
futOspfv3BRRouteEntry.setIndexNames((0,_E,_z),(0,_E,_A0),(0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:futOspfv3BRRouteEntry.setStatus(_A)
_FutOspfv3BRRouteDest_Type=IpAddress
_FutOspfv3BRRouteDest_Object=MibTableColumn
futOspfv3BRRouteDest=_FutOspfv3BRRouteDest_Object((1,3,6,1,4,1,2076,90,5,1,1),_FutOspfv3BRRouteDest_Type())
futOspfv3BRRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3BRRouteDest.setStatus(_A)
_FutOspfv3BRRouteNextHopType_Type=InetAddressType
_FutOspfv3BRRouteNextHopType_Object=MibTableColumn
futOspfv3BRRouteNextHopType=_FutOspfv3BRRouteNextHopType_Object((1,3,6,1,4,1,2076,90,5,1,2),_FutOspfv3BRRouteNextHopType_Type())
futOspfv3BRRouteNextHopType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3BRRouteNextHopType.setStatus(_A)
class _FutOspfv3BRRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3BRRouteNextHop_Type.__name__=_K
_FutOspfv3BRRouteNextHop_Object=MibTableColumn
futOspfv3BRRouteNextHop=_FutOspfv3BRRouteNextHop_Object((1,3,6,1,4,1,2076,90,5,1,3),_FutOspfv3BRRouteNextHop_Type())
futOspfv3BRRouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3BRRouteNextHop.setStatus(_A)
class _FutOspfv3BRRouteDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('areaBorder',2),('asBoundary',3)))
_FutOspfv3BRRouteDestType_Type.__name__=_C
_FutOspfv3BRRouteDestType_Object=MibTableColumn
futOspfv3BRRouteDestType=_FutOspfv3BRRouteDestType_Object((1,3,6,1,4,1,2076,90,5,1,4),_FutOspfv3BRRouteDestType_Type())
futOspfv3BRRouteDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3BRRouteDestType.setStatus(_A)
class _FutOspfv3BRRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_r,1),(_s,2)))
_FutOspfv3BRRouteType_Type.__name__=_C
_FutOspfv3BRRouteType_Object=MibTableColumn
futOspfv3BRRouteType=_FutOspfv3BRRouteType_Object((1,3,6,1,4,1,2076,90,5,1,5),_FutOspfv3BRRouteType_Type())
futOspfv3BRRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3BRRouteType.setStatus(_A)
_FutOspfv3BRRouteAreaId_Type=AreaID
_FutOspfv3BRRouteAreaId_Object=MibTableColumn
futOspfv3BRRouteAreaId=_FutOspfv3BRRouteAreaId_Object((1,3,6,1,4,1,2076,90,5,1,6),_FutOspfv3BRRouteAreaId_Type())
futOspfv3BRRouteAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3BRRouteAreaId.setStatus(_A)
_FutOspfv3BRRouteCost_Type=BigMetric
_FutOspfv3BRRouteCost_Object=MibTableColumn
futOspfv3BRRouteCost=_FutOspfv3BRRouteCost_Object((1,3,6,1,4,1,2076,90,5,1,7),_FutOspfv3BRRouteCost_Type())
futOspfv3BRRouteCost.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3BRRouteCost.setStatus(_A)
_FutOspfv3BRRouteInterfaceIndex_Type=InterfaceIndex
_FutOspfv3BRRouteInterfaceIndex_Object=MibTableColumn
futOspfv3BRRouteInterfaceIndex=_FutOspfv3BRRouteInterfaceIndex_Object((1,3,6,1,4,1,2076,90,5,1,8),_FutOspfv3BRRouteInterfaceIndex_Type())
futOspfv3BRRouteInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3BRRouteInterfaceIndex.setStatus(_A)
_FutOspfv3RedistRouteCfgTable_Object=MibTable
futOspfv3RedistRouteCfgTable=_FutOspfv3RedistRouteCfgTable_Object((1,3,6,1,4,1,2076,90,6))
if mibBuilder.loadTexts:futOspfv3RedistRouteCfgTable.setStatus(_A)
_FutOspfv3RedistRouteCfgEntry_Object=MibTableRow
futOspfv3RedistRouteCfgEntry=_FutOspfv3RedistRouteCfgEntry_Object((1,3,6,1,4,1,2076,90,6,1))
futOspfv3RedistRouteCfgEntry.setIndexNames((0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:futOspfv3RedistRouteCfgEntry.setStatus(_A)
_FutOspfv3RedistRouteDestType_Type=InetAddressType
_FutOspfv3RedistRouteDestType_Object=MibTableColumn
futOspfv3RedistRouteDestType=_FutOspfv3RedistRouteDestType_Object((1,3,6,1,4,1,2076,90,6,1,1),_FutOspfv3RedistRouteDestType_Type())
futOspfv3RedistRouteDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RedistRouteDestType.setStatus(_A)
class _FutOspfv3RedistRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3RedistRouteDest_Type.__name__=_K
_FutOspfv3RedistRouteDest_Object=MibTableColumn
futOspfv3RedistRouteDest=_FutOspfv3RedistRouteDest_Object((1,3,6,1,4,1,2076,90,6,1,2),_FutOspfv3RedistRouteDest_Type())
futOspfv3RedistRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RedistRouteDest.setStatus(_A)
_FutOspfv3RedistRoutePfxLength_Type=InetAddressPrefixLength
_FutOspfv3RedistRoutePfxLength_Object=MibTableColumn
futOspfv3RedistRoutePfxLength=_FutOspfv3RedistRoutePfxLength_Object((1,3,6,1,4,1,2076,90,6,1,3),_FutOspfv3RedistRoutePfxLength_Type())
futOspfv3RedistRoutePfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3RedistRoutePfxLength.setStatus(_A)
class _FutOspfv3RedistRouteMetric_Type(BigMetric):defaultValue=10
_FutOspfv3RedistRouteMetric_Type.__name__=_R
_FutOspfv3RedistRouteMetric_Object=MibTableColumn
futOspfv3RedistRouteMetric=_FutOspfv3RedistRouteMetric_Object((1,3,6,1,4,1,2076,90,6,1,4),_FutOspfv3RedistRouteMetric_Type())
futOspfv3RedistRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RedistRouteMetric.setStatus(_A)
class _FutOspfv3RedistRouteMetricType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_t,3),(_u,4)))
_FutOspfv3RedistRouteMetricType_Type.__name__=_C
_FutOspfv3RedistRouteMetricType_Object=MibTableColumn
futOspfv3RedistRouteMetricType=_FutOspfv3RedistRouteMetricType_Object((1,3,6,1,4,1,2076,90,6,1,5),_FutOspfv3RedistRouteMetricType_Type())
futOspfv3RedistRouteMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RedistRouteMetricType.setStatus(_A)
class _FutOspfv3RedistRouteTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_FutOspfv3RedistRouteTagType_Type.__name__=_C
_FutOspfv3RedistRouteTagType_Object=MibTableColumn
futOspfv3RedistRouteTagType=_FutOspfv3RedistRouteTagType_Object((1,3,6,1,4,1,2076,90,6,1,6),_FutOspfv3RedistRouteTagType_Type())
futOspfv3RedistRouteTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RedistRouteTagType.setStatus(_A)
class _FutOspfv3RedistRouteTag_Type(Integer32):defaultValue=0
_FutOspfv3RedistRouteTag_Type.__name__=_C
_FutOspfv3RedistRouteTag_Object=MibTableColumn
futOspfv3RedistRouteTag=_FutOspfv3RedistRouteTag_Object((1,3,6,1,4,1,2076,90,6,1,7),_FutOspfv3RedistRouteTag_Type())
futOspfv3RedistRouteTag.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RedistRouteTag.setStatus(_A)
_FutOspfv3RedistRouteStatus_Type=RowStatus
_FutOspfv3RedistRouteStatus_Object=MibTableColumn
futOspfv3RedistRouteStatus=_FutOspfv3RedistRouteStatus_Object((1,3,6,1,4,1,2076,90,6,1,8),_FutOspfv3RedistRouteStatus_Type())
futOspfv3RedistRouteStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:futOspfv3RedistRouteStatus.setStatus(_A)
_Futospfv3RRDGroup_ObjectIdentity=ObjectIdentity
futospfv3RRDGroup=_Futospfv3RRDGroup_ObjectIdentity((1,3,6,1,4,1,2076,90,7))
_FutOspfv3RRDGeneralGroup_ObjectIdentity=ObjectIdentity
futOspfv3RRDGeneralGroup=_FutOspfv3RRDGeneralGroup_ObjectIdentity((1,3,6,1,4,1,2076,90,7,1))
class _FutOspfv3RRDStatus_Type(Status):defaultValue=2
_FutOspfv3RRDStatus_Type.__name__=_S
_FutOspfv3RRDStatus_Object=MibScalar
futOspfv3RRDStatus=_FutOspfv3RRDStatus_Object((1,3,6,1,4,1,2076,90,7,1,1),_FutOspfv3RRDStatus_Type())
futOspfv3RRDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RRDStatus.setStatus(_A)
class _FutOspfv3RRDSrcProtoMask_Type(Integer32):defaultValue=0
_FutOspfv3RRDSrcProtoMask_Type.__name__=_C
_FutOspfv3RRDSrcProtoMask_Object=MibScalar
futOspfv3RRDSrcProtoMask=_FutOspfv3RRDSrcProtoMask_Object((1,3,6,1,4,1,2076,90,7,1,2),_FutOspfv3RRDSrcProtoMask_Type())
futOspfv3RRDSrcProtoMask.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RRDSrcProtoMask.setStatus(_A)
class _FutOspfv3RRDRouteMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FutOspfv3RRDRouteMapName_Type.__name__=_O
_FutOspfv3RRDRouteMapName_Object=MibScalar
futOspfv3RRDRouteMapName=_FutOspfv3RRDRouteMapName_Object((1,3,6,1,4,1,2076,90,7,1,3),_FutOspfv3RRDRouteMapName_Type())
futOspfv3RRDRouteMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3RRDRouteMapName.setStatus(_A)
_Futospfv3DistInOutRouteMap_ObjectIdentity=ObjectIdentity
futospfv3DistInOutRouteMap=_Futospfv3DistInOutRouteMap_ObjectIdentity((1,3,6,1,4,1,2076,90,8))
_FutOspfv3DistInOutRouteMapTable_Object=MibTable
futOspfv3DistInOutRouteMapTable=_FutOspfv3DistInOutRouteMapTable_Object((1,3,6,1,4,1,2076,90,8,1))
if mibBuilder.loadTexts:futOspfv3DistInOutRouteMapTable.setStatus(_A)
_FutOspfv3DistInOutRouteMapEntry_Object=MibTableRow
futOspfv3DistInOutRouteMapEntry=_FutOspfv3DistInOutRouteMapEntry_Object((1,3,6,1,4,1,2076,90,8,1,1))
futOspfv3DistInOutRouteMapEntry.setIndexNames((0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:futOspfv3DistInOutRouteMapEntry.setStatus(_A)
class _FutOspfv3DistInOutRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FutOspfv3DistInOutRouteMapName_Type.__name__=_c
_FutOspfv3DistInOutRouteMapName_Object=MibTableColumn
futOspfv3DistInOutRouteMapName=_FutOspfv3DistInOutRouteMapName_Object((1,3,6,1,4,1,2076,90,8,1,1,1),_FutOspfv3DistInOutRouteMapName_Type())
futOspfv3DistInOutRouteMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3DistInOutRouteMapName.setStatus(_A)
class _FutOspfv3DistInOutRouteMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FutOspfv3DistInOutRouteMapType_Type.__name__=_C
_FutOspfv3DistInOutRouteMapType_Object=MibTableColumn
futOspfv3DistInOutRouteMapType=_FutOspfv3DistInOutRouteMapType_Object((1,3,6,1,4,1,2076,90,8,1,1,2),_FutOspfv3DistInOutRouteMapType_Type())
futOspfv3DistInOutRouteMapType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3DistInOutRouteMapType.setStatus(_A)
class _FutOspfv3DistInOutRouteMapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FutOspfv3DistInOutRouteMapValue_Type.__name__=_C
_FutOspfv3DistInOutRouteMapValue_Object=MibTableColumn
futOspfv3DistInOutRouteMapValue=_FutOspfv3DistInOutRouteMapValue_Object((1,3,6,1,4,1,2076,90,8,1,1,3),_FutOspfv3DistInOutRouteMapValue_Type())
futOspfv3DistInOutRouteMapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3DistInOutRouteMapValue.setStatus(_A)
_FutOspfv3DistInOutRouteMapRowStatus_Type=RowStatus
_FutOspfv3DistInOutRouteMapRowStatus_Object=MibTableColumn
futOspfv3DistInOutRouteMapRowStatus=_FutOspfv3DistInOutRouteMapRowStatus_Object((1,3,6,1,4,1,2076,90,8,1,1,4),_FutOspfv3DistInOutRouteMapRowStatus_Type())
futOspfv3DistInOutRouteMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3DistInOutRouteMapRowStatus.setStatus(_A)
_Futospf3PreferenceGroup_ObjectIdentity=ObjectIdentity
futospf3PreferenceGroup=_Futospf3PreferenceGroup_ObjectIdentity((1,3,6,1,4,1,2076,90,9))
class _FutOspf3PreferenceValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FutOspf3PreferenceValue_Type.__name__=_C
_FutOspf3PreferenceValue_Object=MibScalar
futOspf3PreferenceValue=_FutOspf3PreferenceValue_Object((1,3,6,1,4,1,2076,90,9,1),_FutOspf3PreferenceValue_Type())
futOspf3PreferenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspf3PreferenceValue.setStatus(_A)
_FutOspfv3NeighborBfdGroup_ObjectIdentity=ObjectIdentity
futOspfv3NeighborBfdGroup=_FutOspfv3NeighborBfdGroup_ObjectIdentity((1,3,6,1,4,1,2076,90,11))
_FutOspfv3NeighborBfdTable_Object=MibTable
futOspfv3NeighborBfdTable=_FutOspfv3NeighborBfdTable_Object((1,3,6,1,4,1,2076,90,11,1))
if mibBuilder.loadTexts:futOspfv3NeighborBfdTable.setStatus(_A)
_FutOspfv3NeighborBfdEntry_Object=MibTableRow
futOspfv3NeighborBfdEntry=_FutOspfv3NeighborBfdEntry_Object((1,3,6,1,4,1,2076,90,11,1,1))
if mibBuilder.loadTexts:futOspfv3NeighborBfdEntry.setStatus(_A)
class _FutOspfv3NbrBfdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FutOspfv3NbrBfdState_Type.__name__=_C
_FutOspfv3NbrBfdState_Object=MibTableColumn
futOspfv3NbrBfdState=_FutOspfv3NbrBfdState_Object((1,3,6,1,4,1,2076,90,11,1,1,1),_FutOspfv3NbrBfdState_Type())
futOspfv3NbrBfdState.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfv3NbrBfdState.setStatus(_A)
_FutOspfv3IfAuthTable_Object=MibTable
futOspfv3IfAuthTable=_FutOspfv3IfAuthTable_Object((1,3,6,1,4,1,2076,90,12))
if mibBuilder.loadTexts:futOspfv3IfAuthTable.setStatus(_A)
_FutOspfv3IfAuthEntry_Object=MibTableRow
futOspfv3IfAuthEntry=_FutOspfv3IfAuthEntry_Object((1,3,6,1,4,1,2076,90,12,1))
futOspfv3IfAuthEntry.setIndexNames((0,_E,_A8),(0,_E,_A9))
if mibBuilder.loadTexts:futOspfv3IfAuthEntry.setStatus(_A)
class _FutOspfv3IfAuthIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfv3IfAuthIfIndex_Type.__name__=_Q
_FutOspfv3IfAuthIfIndex_Object=MibTableColumn
futOspfv3IfAuthIfIndex=_FutOspfv3IfAuthIfIndex_Object((1,3,6,1,4,1,2076,90,12,1,1),_FutOspfv3IfAuthIfIndex_Type())
futOspfv3IfAuthIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3IfAuthIfIndex.setStatus(_A)
class _FutOspfv3IfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfv3IfAuthKeyId_Type.__name__=_C
_FutOspfv3IfAuthKeyId_Object=MibTableColumn
futOspfv3IfAuthKeyId=_FutOspfv3IfAuthKeyId_Object((1,3,6,1,4,1,2076,90,12,1,2),_FutOspfv3IfAuthKeyId_Type())
futOspfv3IfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3IfAuthKeyId.setStatus(_A)
class _FutOspfv3IfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FutOspfv3IfAuthKey_Type.__name__=_O
_FutOspfv3IfAuthKey_Object=MibTableColumn
futOspfv3IfAuthKey=_FutOspfv3IfAuthKey_Object((1,3,6,1,4,1,2076,90,12,1,3),_FutOspfv3IfAuthKey_Type())
futOspfv3IfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfAuthKey.setStatus(_A)
_FutOspfv3IfAuthKeyStartAccept_Type=DateAndTime
_FutOspfv3IfAuthKeyStartAccept_Object=MibTableColumn
futOspfv3IfAuthKeyStartAccept=_FutOspfv3IfAuthKeyStartAccept_Object((1,3,6,1,4,1,2076,90,12,1,4),_FutOspfv3IfAuthKeyStartAccept_Type())
futOspfv3IfAuthKeyStartAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfAuthKeyStartAccept.setStatus(_A)
_FutOspfv3IfAuthKeyStartGenerate_Type=DateAndTime
_FutOspfv3IfAuthKeyStartGenerate_Object=MibTableColumn
futOspfv3IfAuthKeyStartGenerate=_FutOspfv3IfAuthKeyStartGenerate_Object((1,3,6,1,4,1,2076,90,12,1,5),_FutOspfv3IfAuthKeyStartGenerate_Type())
futOspfv3IfAuthKeyStartGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfAuthKeyStartGenerate.setStatus(_A)
_FutOspfv3IfAuthKeyStopGenerate_Type=DateAndTime
_FutOspfv3IfAuthKeyStopGenerate_Object=MibTableColumn
futOspfv3IfAuthKeyStopGenerate=_FutOspfv3IfAuthKeyStopGenerate_Object((1,3,6,1,4,1,2076,90,12,1,6),_FutOspfv3IfAuthKeyStopGenerate_Type())
futOspfv3IfAuthKeyStopGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfAuthKeyStopGenerate.setStatus(_A)
_FutOspfv3IfAuthKeyStopAccept_Type=DateAndTime
_FutOspfv3IfAuthKeyStopAccept_Object=MibTableColumn
futOspfv3IfAuthKeyStopAccept=_FutOspfv3IfAuthKeyStopAccept_Object((1,3,6,1,4,1,2076,90,12,1,7),_FutOspfv3IfAuthKeyStopAccept_Type())
futOspfv3IfAuthKeyStopAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfAuthKeyStopAccept.setStatus(_A)
_FutOspfv3IfAuthKeyStatus_Type=RowStatus
_FutOspfv3IfAuthKeyStatus_Object=MibTableColumn
futOspfv3IfAuthKeyStatus=_FutOspfv3IfAuthKeyStatus_Object((1,3,6,1,4,1,2076,90,12,1,8),_FutOspfv3IfAuthKeyStatus_Type())
futOspfv3IfAuthKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3IfAuthKeyStatus.setStatus(_A)
_FutOspfv3VirtIfAuthTable_Object=MibTable
futOspfv3VirtIfAuthTable=_FutOspfv3VirtIfAuthTable_Object((1,3,6,1,4,1,2076,90,13))
if mibBuilder.loadTexts:futOspfv3VirtIfAuthTable.setStatus(_A)
_FutOspfv3VirtIfAuthEntry_Object=MibTableRow
futOspfv3VirtIfAuthEntry=_FutOspfv3VirtIfAuthEntry_Object((1,3,6,1,4,1,2076,90,13,1))
futOspfv3VirtIfAuthEntry.setIndexNames((0,_E,_AA),(0,_E,_AB),(0,_E,_AC))
if mibBuilder.loadTexts:futOspfv3VirtIfAuthEntry.setStatus(_A)
_FutOspfv3VirtIfAuthAreaId_Type=AreaID
_FutOspfv3VirtIfAuthAreaId_Object=MibTableColumn
futOspfv3VirtIfAuthAreaId=_FutOspfv3VirtIfAuthAreaId_Object((1,3,6,1,4,1,2076,90,13,1,1),_FutOspfv3VirtIfAuthAreaId_Type())
futOspfv3VirtIfAuthAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthAreaId.setStatus(_A)
_FutOspfv3VirtIfAuthNeighbor_Type=RouterID
_FutOspfv3VirtIfAuthNeighbor_Object=MibTableColumn
futOspfv3VirtIfAuthNeighbor=_FutOspfv3VirtIfAuthNeighbor_Object((1,3,6,1,4,1,2076,90,13,1,2),_FutOspfv3VirtIfAuthNeighbor_Type())
futOspfv3VirtIfAuthNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthNeighbor.setStatus(_A)
class _FutOspfv3VirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfv3VirtIfAuthKeyId_Type.__name__=_C
_FutOspfv3VirtIfAuthKeyId_Object=MibTableColumn
futOspfv3VirtIfAuthKeyId=_FutOspfv3VirtIfAuthKeyId_Object((1,3,6,1,4,1,2076,90,13,1,3),_FutOspfv3VirtIfAuthKeyId_Type())
futOspfv3VirtIfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKeyId.setStatus(_A)
class _FutOspfv3VirtIfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FutOspfv3VirtIfAuthKey_Type.__name__=_O
_FutOspfv3VirtIfAuthKey_Object=MibTableColumn
futOspfv3VirtIfAuthKey=_FutOspfv3VirtIfAuthKey_Object((1,3,6,1,4,1,2076,90,13,1,4),_FutOspfv3VirtIfAuthKey_Type())
futOspfv3VirtIfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKey.setStatus(_A)
_FutOspfv3VirtIfAuthKeyStartAccept_Type=DateAndTime
_FutOspfv3VirtIfAuthKeyStartAccept_Object=MibTableColumn
futOspfv3VirtIfAuthKeyStartAccept=_FutOspfv3VirtIfAuthKeyStartAccept_Object((1,3,6,1,4,1,2076,90,13,1,5),_FutOspfv3VirtIfAuthKeyStartAccept_Type())
futOspfv3VirtIfAuthKeyStartAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKeyStartAccept.setStatus(_A)
_FutOspfv3VirtIfAuthKeyStartGenerate_Type=DateAndTime
_FutOspfv3VirtIfAuthKeyStartGenerate_Object=MibTableColumn
futOspfv3VirtIfAuthKeyStartGenerate=_FutOspfv3VirtIfAuthKeyStartGenerate_Object((1,3,6,1,4,1,2076,90,13,1,6),_FutOspfv3VirtIfAuthKeyStartGenerate_Type())
futOspfv3VirtIfAuthKeyStartGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKeyStartGenerate.setStatus(_A)
_FutOspfv3VirtIfAuthKeyStopGenerate_Type=DateAndTime
_FutOspfv3VirtIfAuthKeyStopGenerate_Object=MibTableColumn
futOspfv3VirtIfAuthKeyStopGenerate=_FutOspfv3VirtIfAuthKeyStopGenerate_Object((1,3,6,1,4,1,2076,90,13,1,7),_FutOspfv3VirtIfAuthKeyStopGenerate_Type())
futOspfv3VirtIfAuthKeyStopGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKeyStopGenerate.setStatus(_A)
_FutOspfv3VirtIfAuthKeyStopAccept_Type=DateAndTime
_FutOspfv3VirtIfAuthKeyStopAccept_Object=MibTableColumn
futOspfv3VirtIfAuthKeyStopAccept=_FutOspfv3VirtIfAuthKeyStopAccept_Object((1,3,6,1,4,1,2076,90,13,1,8),_FutOspfv3VirtIfAuthKeyStopAccept_Type())
futOspfv3VirtIfAuthKeyStopAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKeyStopAccept.setStatus(_A)
_FutOspfv3VirtIfAuthKeyStatus_Type=RowStatus
_FutOspfv3VirtIfAuthKeyStatus_Object=MibTableColumn
futOspfv3VirtIfAuthKeyStatus=_FutOspfv3VirtIfAuthKeyStatus_Object((1,3,6,1,4,1,2076,90,13,1,9),_FutOspfv3VirtIfAuthKeyStatus_Type())
futOspfv3VirtIfAuthKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfAuthKeyStatus.setStatus(_A)
_FutOspfv3VirtIfCryptoAuthTable_Object=MibTable
futOspfv3VirtIfCryptoAuthTable=_FutOspfv3VirtIfCryptoAuthTable_Object((1,3,6,1,4,1,2076,90,14))
if mibBuilder.loadTexts:futOspfv3VirtIfCryptoAuthTable.setStatus(_A)
_FutOspfv3VirtIfCryptoAuthEntry_Object=MibTableRow
futOspfv3VirtIfCryptoAuthEntry=_FutOspfv3VirtIfCryptoAuthEntry_Object((1,3,6,1,4,1,2076,90,14,1))
if mibBuilder.loadTexts:futOspfv3VirtIfCryptoAuthEntry.setStatus(_A)
class _FutOspfv3VirtIfCryptoAuthType_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6)));namedValues=NamedValues(*(('sha1',1),(_i,3),(_j,4),(_k,5),(_M,6)))
_FutOspfv3VirtIfCryptoAuthType_Type.__name__=_C
_FutOspfv3VirtIfCryptoAuthType_Object=MibTableColumn
futOspfv3VirtIfCryptoAuthType=_FutOspfv3VirtIfCryptoAuthType_Object((1,3,6,1,4,1,2076,90,14,1,1),_FutOspfv3VirtIfCryptoAuthType_Type())
futOspfv3VirtIfCryptoAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfCryptoAuthType.setStatus(_A)
class _FutOspfv3VirtIfCryptoAuthMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),(_l,2),(_M,3)))
_FutOspfv3VirtIfCryptoAuthMode_Type.__name__=_C
_FutOspfv3VirtIfCryptoAuthMode_Object=MibTableColumn
futOspfv3VirtIfCryptoAuthMode=_FutOspfv3VirtIfCryptoAuthMode_Object((1,3,6,1,4,1,2076,90,14,1,2),_FutOspfv3VirtIfCryptoAuthMode_Type())
futOspfv3VirtIfCryptoAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfv3VirtIfCryptoAuthMode.setStatus(_A)
_FutOspfv3Notification_ObjectIdentity=ObjectIdentity
futOspfv3Notification=_FutOspfv3Notification_ObjectIdentity((1,3,6,1,4,1,2076,90,101))
_FutOspfv3Traps_ObjectIdentity=ObjectIdentity
futOspfv3Traps=_FutOspfv3Traps_ObjectIdentity((1,3,6,1,4,1,2076,90,101,0))
_FutOspfv3TrapObject_ObjectIdentity=ObjectIdentity
futOspfv3TrapObject=_FutOspfv3TrapObject_ObjectIdentity((1,3,6,1,4,1,2076,90,101,1))
_FutOspfv3TrapNbrIfIndex_Type=InterfaceIndex
_FutOspfv3TrapNbrIfIndex_Object=MibScalar
futOspfv3TrapNbrIfIndex=_FutOspfv3TrapNbrIfIndex_Object((1,3,6,1,4,1,2076,90,101,1,1),_FutOspfv3TrapNbrIfIndex_Type())
futOspfv3TrapNbrIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:futOspfv3TrapNbrIfIndex.setStatus(_A)
_FutOspfv3TrapVirtNbrRtrId_Type=RouterID
_FutOspfv3TrapVirtNbrRtrId_Object=MibScalar
futOspfv3TrapVirtNbrRtrId=_FutOspfv3TrapVirtNbrRtrId_Object((1,3,6,1,4,1,2076,90,101,1,2),_FutOspfv3TrapVirtNbrRtrId_Type())
futOspfv3TrapVirtNbrRtrId.setMaxAccess(_N)
if mibBuilder.loadTexts:futOspfv3TrapVirtNbrRtrId.setStatus(_A)
_FutOspfv3TrapNbrRtrId_Type=RouterID
_FutOspfv3TrapNbrRtrId_Object=MibScalar
futOspfv3TrapNbrRtrId=_FutOspfv3TrapNbrRtrId_Object((1,3,6,1,4,1,2076,90,101,1,3),_FutOspfv3TrapNbrRtrId_Type())
futOspfv3TrapNbrRtrId.setMaxAccess(_N)
if mibBuilder.loadTexts:futOspfv3TrapNbrRtrId.setStatus(_A)
_FutOspfv3TrapVirtNbrArea_Type=AreaID
_FutOspfv3TrapVirtNbrArea_Object=MibScalar
futOspfv3TrapVirtNbrArea=_FutOspfv3TrapVirtNbrArea_Object((1,3,6,1,4,1,2076,90,101,1,4),_FutOspfv3TrapVirtNbrArea_Type())
futOspfv3TrapVirtNbrArea.setMaxAccess(_N)
if mibBuilder.loadTexts:futOspfv3TrapVirtNbrArea.setStatus(_A)
class _FutOspfv3TrapBulkUpdAbortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('memAllocFailed',2),('sendFailed',3),('processFailed',4)))
_FutOspfv3TrapBulkUpdAbortReason_Type.__name__=_C
_FutOspfv3TrapBulkUpdAbortReason_Object=MibScalar
futOspfv3TrapBulkUpdAbortReason=_FutOspfv3TrapBulkUpdAbortReason_Object((1,3,6,1,4,1,2076,90,101,1,5),_FutOspfv3TrapBulkUpdAbortReason_Type())
futOspfv3TrapBulkUpdAbortReason.setMaxAccess(_N)
if mibBuilder.loadTexts:futOspfv3TrapBulkUpdAbortReason.setStatus(_A)
ospfv3NbrEntry.registerAugmentions((_E,_AD))
futOspfv3NeighborBfdEntry.setIndexNames(*ospfv3NbrEntry.getIndexNames())
ospfv3VirtIfEntry.registerAugmentions((_E,_AE))
futOspfv3VirtIfCryptoAuthEntry.setIndexNames(*ospfv3VirtIfEntry.getIndexNames())
futOspfv3RestartStatusChange=NotificationType((1,3,6,1,4,1,2076,90,101,0,1))
futOspfv3RestartStatusChange.setObjects(*((_G,_J),(_G,_Y),(_G,_X),(_G,_W)))
if mibBuilder.loadTexts:futOspfv3RestartStatusChange.setStatus(_A)
futOspfv3NbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,2076,90,101,0,2))
futOspfv3NbrRestartHelperStatusChange.setObjects(*((_G,_J),(_E,_AF),(_E,_AG),(_G,_V),(_G,_T),(_G,_U)))
if mibBuilder.loadTexts:futOspfv3NbrRestartHelperStatusChange.setStatus(_A)
futOspfv3VirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,2076,90,101,0,3))
futOspfv3VirtNbrRestartHelperStatusChange.setObjects(*((_G,_J),(_E,_AH),(_E,_AI),(_G,_b),(_G,_Z),(_G,_a)))
if mibBuilder.loadTexts:futOspfv3VirtNbrRestartHelperStatusChange.setStatus(_A)
futOspfv3HotStandbyStateChgTrap=NotificationType((1,3,6,1,4,1,2076,90,101,0,4))
futOspfv3HotStandbyStateChgTrap.setObjects(*((_G,_J),(_E,_AJ)))
if mibBuilder.loadTexts:futOspfv3HotStandbyStateChgTrap.setStatus(_A)
futOspfv3HotStandbyBulkUpdAbortTrap=NotificationType((1,3,6,1,4,1,2076,90,101,0,5))
futOspfv3HotStandbyBulkUpdAbortTrap.setObjects(*((_G,_J),(_E,_AK),(_E,_AL)))
if mibBuilder.loadTexts:futOspfv3HotStandbyBulkUpdAbortTrap.setStatus(_A)
futOspfv3AuthSequenceNumWrap=NotificationType((1,3,6,1,4,1,2076,90,101,0,6))
futOspfv3AuthSequenceNumWrap.setObjects((_G,_J))
if mibBuilder.loadTexts:futOspfv3AuthSequenceNumWrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'futospfv3':futospfv3,'futospfv3GeneralGroup':futospfv3GeneralGroup,'futOspfv3OverFlowState':futOspfv3OverFlowState,'futOspfv3TraceLevel':futOspfv3TraceLevel,'futOspfv3ABRType':futOspfv3ABRType,'futOspfv3NssaAsbrDefRtTrans':futOspfv3NssaAsbrDefRtTrans,'futOspfv3DefaultPassiveInterface':futOspfv3DefaultPassiveInterface,'futOspfv3SpfDelay':futOspfv3SpfDelay,'futOspfv3SpfHoldTime':futOspfv3SpfHoldTime,'futOspfv3RTStaggeringInterval':futOspfv3RTStaggeringInterval,'futOspfv3RTStaggeringStatus':futOspfv3RTStaggeringStatus,'futOspfv3RestartStrictLsaChecking':futOspfv3RestartStrictLsaChecking,'futOspfv3HelperSupport':futOspfv3HelperSupport,'futOspfv3HelperGraceTimeLimit':futOspfv3HelperGraceTimeLimit,'futOspfv3RestartAckState':futOspfv3RestartAckState,'futOspfv3GraceLsaRetransmitCount':futOspfv3GraceLsaRetransmitCount,'futOspfv3RestartReason':futOspfv3RestartReason,'futOspfv3ExtTraceLevel':futOspfv3ExtTraceLevel,'futOspfv3SetTraps':futOspfv3SetTraps,'futOspfv3HotStandbyAdminStatus':futOspfv3HotStandbyAdminStatus,_AJ:futOspfv3HotStandbyState,_AK:futOspfv3DynamicBulkUpdStatus,'futOspfv3StandbyHelloSyncCount':futOspfv3StandbyHelloSyncCount,'futOspfv3StandbyLsaSyncCount':futOspfv3StandbyLsaSyncCount,'futOspfv3BfdStatus':futOspfv3BfdStatus,'futOspfv3BfdAllIfState':futOspfv3BfdAllIfState,'futOspfv3IfTable':futOspfv3IfTable,'futOspfv3IfEntry':futOspfv3IfEntry,_h:futOspfv3IfIndex,'futOspfv3IfOperState':futOspfv3IfOperState,'futOspfv3IfPassive':futOspfv3IfPassive,'futOspfv3IfNbrCount':futOspfv3IfNbrCount,'futOspfv3IfAdjCount':futOspfv3IfAdjCount,'futOspfv3IfHelloRcvd':futOspfv3IfHelloRcvd,'futOspfv3IfHelloTxed':futOspfv3IfHelloTxed,'futOspfv3IfHelloDisd':futOspfv3IfHelloDisd,'futOspfv3IfDdpRcvd':futOspfv3IfDdpRcvd,'futOspfv3IfDdpTxed':futOspfv3IfDdpTxed,'futOspfv3IfDdpDisd':futOspfv3IfDdpDisd,'futOspfv3IfLrqRcvd':futOspfv3IfLrqRcvd,'futOspfv3IfLrqTxed':futOspfv3IfLrqTxed,'futOspfv3IfLrqDisd':futOspfv3IfLrqDisd,'futOspfv3IfLsuRcvd':futOspfv3IfLsuRcvd,'futOspfv3IfLsuTxed':futOspfv3IfLsuTxed,'futOspfv3IfLsuDisd':futOspfv3IfLsuDisd,'futOspfv3IfLakRcvd':futOspfv3IfLakRcvd,'futOspfv3IfLakTxed':futOspfv3IfLakTxed,'futOspfv3IfLakDisd':futOspfv3IfLakDisd,'futOspfv3IfLinkLSASuppression':futOspfv3IfLinkLSASuppression,'futOspfv3IfBfdState':futOspfv3IfBfdState,'futOspfv3IfCryptoAuthType':futOspfv3IfCryptoAuthType,'futOspfv3IfCryptoAuthMode':futOspfv3IfCryptoAuthMode,'futOspfv3IfAuthTxed':futOspfv3IfAuthTxed,'futOspfv3IfAuthRcvd':futOspfv3IfAuthRcvd,'futOspfv3IfAuthDisd':futOspfv3IfAuthDisd,'futOspfv3RoutingTable':futOspfv3RoutingTable,'futOspfv3RoutingEntry':futOspfv3RoutingEntry,_m:futOspfv3RouteDestType,_n:futOspfv3RouteDest,_o:futOspfv3RoutePfxLength,_p:futOspfv3RouteNextHopType,_q:futOspfv3RouteNextHop,'futOspfv3RouteType':futOspfv3RouteType,'futOspfv3RouteAreaId':futOspfv3RouteAreaId,'futOspfv3RouteCost':futOspfv3RouteCost,'futOspfv3RouteType2Cost':futOspfv3RouteType2Cost,'futOspfv3RouteInterfaceIndex':futOspfv3RouteInterfaceIndex,'futOspfv3AsExternalAggregationTable':futOspfv3AsExternalAggregationTable,'futOspfv3AsExternalAggregationEntry':futOspfv3AsExternalAggregationEntry,_v:futOspfv3AsExternalAggregationNetType,_w:futOspfv3AsExternalAggregationNet,_x:futOspfv3AsExternalAggregationPfxLength,_y:futOspfv3AsExternalAggregationAreaId,'futOspfv3AsExternalAggregationEffect':futOspfv3AsExternalAggregationEffect,'futOspfv3AsExternalAggregationTranslation':futOspfv3AsExternalAggregationTranslation,'futOspfv3AsExternalAggregationStatus':futOspfv3AsExternalAggregationStatus,'futOspfv3BRRouteTable':futOspfv3BRRouteTable,'futOspfv3BRRouteEntry':futOspfv3BRRouteEntry,_z:futOspfv3BRRouteDest,_A0:futOspfv3BRRouteNextHopType,_A1:futOspfv3BRRouteNextHop,_A2:futOspfv3BRRouteDestType,'futOspfv3BRRouteType':futOspfv3BRRouteType,'futOspfv3BRRouteAreaId':futOspfv3BRRouteAreaId,'futOspfv3BRRouteCost':futOspfv3BRRouteCost,'futOspfv3BRRouteInterfaceIndex':futOspfv3BRRouteInterfaceIndex,'futOspfv3RedistRouteCfgTable':futOspfv3RedistRouteCfgTable,'futOspfv3RedistRouteCfgEntry':futOspfv3RedistRouteCfgEntry,_A3:futOspfv3RedistRouteDestType,_A4:futOspfv3RedistRouteDest,_A5:futOspfv3RedistRoutePfxLength,'futOspfv3RedistRouteMetric':futOspfv3RedistRouteMetric,'futOspfv3RedistRouteMetricType':futOspfv3RedistRouteMetricType,'futOspfv3RedistRouteTagType':futOspfv3RedistRouteTagType,'futOspfv3RedistRouteTag':futOspfv3RedistRouteTag,'futOspfv3RedistRouteStatus':futOspfv3RedistRouteStatus,'futospfv3RRDGroup':futospfv3RRDGroup,'futOspfv3RRDGeneralGroup':futOspfv3RRDGeneralGroup,'futOspfv3RRDStatus':futOspfv3RRDStatus,'futOspfv3RRDSrcProtoMask':futOspfv3RRDSrcProtoMask,'futOspfv3RRDRouteMapName':futOspfv3RRDRouteMapName,'futospfv3DistInOutRouteMap':futospfv3DistInOutRouteMap,'futOspfv3DistInOutRouteMapTable':futOspfv3DistInOutRouteMapTable,'futOspfv3DistInOutRouteMapEntry':futOspfv3DistInOutRouteMapEntry,_A6:futOspfv3DistInOutRouteMapName,_A7:futOspfv3DistInOutRouteMapType,'futOspfv3DistInOutRouteMapValue':futOspfv3DistInOutRouteMapValue,'futOspfv3DistInOutRouteMapRowStatus':futOspfv3DistInOutRouteMapRowStatus,'futospf3PreferenceGroup':futospf3PreferenceGroup,'futOspf3PreferenceValue':futOspf3PreferenceValue,'futOspfv3NeighborBfdGroup':futOspfv3NeighborBfdGroup,'futOspfv3NeighborBfdTable':futOspfv3NeighborBfdTable,_AD:futOspfv3NeighborBfdEntry,'futOspfv3NbrBfdState':futOspfv3NbrBfdState,'futOspfv3IfAuthTable':futOspfv3IfAuthTable,'futOspfv3IfAuthEntry':futOspfv3IfAuthEntry,_A8:futOspfv3IfAuthIfIndex,_A9:futOspfv3IfAuthKeyId,'futOspfv3IfAuthKey':futOspfv3IfAuthKey,'futOspfv3IfAuthKeyStartAccept':futOspfv3IfAuthKeyStartAccept,'futOspfv3IfAuthKeyStartGenerate':futOspfv3IfAuthKeyStartGenerate,'futOspfv3IfAuthKeyStopGenerate':futOspfv3IfAuthKeyStopGenerate,'futOspfv3IfAuthKeyStopAccept':futOspfv3IfAuthKeyStopAccept,'futOspfv3IfAuthKeyStatus':futOspfv3IfAuthKeyStatus,'futOspfv3VirtIfAuthTable':futOspfv3VirtIfAuthTable,'futOspfv3VirtIfAuthEntry':futOspfv3VirtIfAuthEntry,_AA:futOspfv3VirtIfAuthAreaId,_AB:futOspfv3VirtIfAuthNeighbor,_AC:futOspfv3VirtIfAuthKeyId,'futOspfv3VirtIfAuthKey':futOspfv3VirtIfAuthKey,'futOspfv3VirtIfAuthKeyStartAccept':futOspfv3VirtIfAuthKeyStartAccept,'futOspfv3VirtIfAuthKeyStartGenerate':futOspfv3VirtIfAuthKeyStartGenerate,'futOspfv3VirtIfAuthKeyStopGenerate':futOspfv3VirtIfAuthKeyStopGenerate,'futOspfv3VirtIfAuthKeyStopAccept':futOspfv3VirtIfAuthKeyStopAccept,'futOspfv3VirtIfAuthKeyStatus':futOspfv3VirtIfAuthKeyStatus,'futOspfv3VirtIfCryptoAuthTable':futOspfv3VirtIfCryptoAuthTable,_AE:futOspfv3VirtIfCryptoAuthEntry,'futOspfv3VirtIfCryptoAuthType':futOspfv3VirtIfCryptoAuthType,'futOspfv3VirtIfCryptoAuthMode':futOspfv3VirtIfCryptoAuthMode,'futOspfv3Notification':futOspfv3Notification,'futOspfv3Traps':futOspfv3Traps,'futOspfv3RestartStatusChange':futOspfv3RestartStatusChange,'futOspfv3NbrRestartHelperStatusChange':futOspfv3NbrRestartHelperStatusChange,'futOspfv3VirtNbrRestartHelperStatusChange':futOspfv3VirtNbrRestartHelperStatusChange,'futOspfv3HotStandbyStateChgTrap':futOspfv3HotStandbyStateChgTrap,'futOspfv3HotStandbyBulkUpdAbortTrap':futOspfv3HotStandbyBulkUpdAbortTrap,'futOspfv3AuthSequenceNumWrap':futOspfv3AuthSequenceNumWrap,'futOspfv3TrapObject':futOspfv3TrapObject,_AF:futOspfv3TrapNbrIfIndex,_AI:futOspfv3TrapVirtNbrRtrId,_AG:futOspfv3TrapNbrRtrId,_AH:futOspfv3TrapVirtNbrArea,_AL:futOspfv3TrapBulkUpdAbortReason})