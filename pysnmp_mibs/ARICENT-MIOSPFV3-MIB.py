_AP='fsMIOspfv3TrapBulkUpdAbortReason'
_AO='fsMIOspfv3DynamicBulkUpdStatus'
_AN='fsMIOspfv3HotStandbyState'
_AM='fsMIOspfv3TrapVirtNbrRtrId'
_AL='fsMIOspfv3TrapVirtNbrArea'
_AK='fsMIOspfv3TrapNbrRtrId'
_AJ='fsMIOspfv3TrapNbrIfIndex'
_AI='fsMIOspfv3VirtIfCryptoAuthEntry'
_AH='fsMIOspfv3NeighborBfdEntry'
_AG='fsMIOspfv3PreferenceEntry'
_AF='fsMIOspfv3RRDRouteEntry'
_AE='fsMIOspfv3Entry'
_AD='fsMIOspfv3VirtIfAuthKeyId'
_AC='fsMIOspfv3VirtIfAuthNeighbor'
_AB='fsMIOspfv3VirtIfAuthAreaId'
_AA='fsMIOspfv3IfAuthKeyId'
_A9='fsMIOspfv3IfAuthIfIndex'
_A8='fsMIOspfv3DistInOutRouteMapType'
_A7='fsMIOspfv3DistInOutRouteMapName'
_A6='fsMIOspfv3RedistRoutePfxLength'
_A5='fsMIOspfv3RedistRouteDest'
_A4='fsMIOspfv3RedistRouteDestType'
_A3='fsMIOspfv3BRRouteDestType'
_A2='fsMIOspfv3BRRouteNextHop'
_A1='fsMIOspfv3BRRouteNextHopType'
_A0='fsMIOspfv3BRRouteDest'
_z='fsMIOspfv3AsExternalAggregationAreaId'
_y='fsMIOspfv3AsExternalAggregationPfxLength'
_x='fsMIOspfv3AsExternalAggregationNet'
_w='fsMIOspfv3AsExternalAggregationNetType'
_v='type2External'
_u='type1External'
_t='interArea'
_s='intraArea'
_r='fsMIOspfv3RouteNextHop'
_q='fsMIOspfv3RouteNextHopType'
_p='fsMIOspfv3RoutePfxLength'
_o='fsMIOspfv3RouteDest'
_n='fsMIOspfv3RouteDestType'
_m='transition'
_l='sha512'
_k='sha384'
_j='sha256'
_i='fsMIOspfv3IfIndex'
_h='switchToRedundant'
_g='swReloadUpgrade'
_f='softwareRestart'
_e='unknown'
_d='DisplayString'
_c='Status'
_b='BigMetric'
_a='InterfaceIndex'
_Z='fsMIStdOspfv3VirtNbrRestartHelperStatus'
_Y='fsMIStdOspfv3VirtNbrRestartHelperExitReason'
_X='fsMIStdOspfv3VirtNbrRestartHelperAge'
_W='fsMIStdOspfv3RestartStatus'
_V='fsMIStdOspfv3RestartInterval'
_U='fsMIStdOspfv3RestartExitReason'
_T='fsMIStdOspfv3NbrRestartHelperStatus'
_S='fsMIStdOspfv3NbrRestartHelperExitReason'
_R='fsMIStdOspfv3NbrRestartHelperAge'
_Q='read-create'
_P='OctetString'
_O='accessible-for-notify'
_N='none'
_M='TruthValue'
_L='InetAddress'
_K='fsMIStdOspfv3RouterId'
_J='disabled'
_I='enabled'
_H='fsMIStdOspfv3ContextId'
_G='ARICENT-MISTDOSPFV3-MIB'
_F='not-accessible'
_E='ARICENT-MIOSPFV3-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMIStdOspfv3ContextId,fsMIStdOspfv3Entry,fsMIStdOspfv3NbrEntry,fsMIStdOspfv3NbrRestartHelperAge,fsMIStdOspfv3NbrRestartHelperExitReason,fsMIStdOspfv3NbrRestartHelperStatus,fsMIStdOspfv3RestartExitReason,fsMIStdOspfv3RestartInterval,fsMIStdOspfv3RestartStatus,fsMIStdOspfv3RouterId,fsMIStdOspfv3VirtIfEntry,fsMIStdOspfv3VirtNbrRestartHelperAge,fsMIStdOspfv3VirtNbrRestartHelperExitReason,fsMIStdOspfv3VirtNbrRestartHelperStatus=mibBuilder.importSymbols(_G,_H,'fsMIStdOspfv3Entry','fsMIStdOspfv3NbrEntry',_R,_S,_T,_U,_V,_W,_K,'fsMIStdOspfv3VirtIfEntry',_X,_Y,_Z)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_a)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,'InetAddressPrefixLength','InetAddressType')
AreaID,BigMetric,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB','AreaID',_b,'RouterID',_c)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_d,'PhysAddress','RowStatus','TextualConvention',_M)
fsMIOspfv3=ModuleIdentity((1,3,6,1,4,1,29601,2,24))
if mibBuilder.loadTexts:fsMIOspfv3.setRevisions(('2012-09-05 00:00',))
_FsMIOspfv3GeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3GeneralGroup=_FsMIOspfv3GeneralGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,24,1))
_FsMIOspfv3GlobalTraceLevel_Type=Integer32
_FsMIOspfv3GlobalTraceLevel_Object=MibScalar
fsMIOspfv3GlobalTraceLevel=_FsMIOspfv3GlobalTraceLevel_Object((1,3,6,1,4,1,29601,2,24,1,1),_FsMIOspfv3GlobalTraceLevel_Type())
fsMIOspfv3GlobalTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3GlobalTraceLevel.setStatus(_A)
class _FsMIOspfv3VrfSpfInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_FsMIOspfv3VrfSpfInterval_Type.__name__=_C
_FsMIOspfv3VrfSpfInterval_Object=MibScalar
fsMIOspfv3VrfSpfInterval=_FsMIOspfv3VrfSpfInterval_Object((1,3,6,1,4,1,29601,2,24,1,2),_FsMIOspfv3VrfSpfInterval_Type())
fsMIOspfv3VrfSpfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VrfSpfInterval.setStatus(_A)
class _FsMIOspfv3RTStaggeringStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsMIOspfv3RTStaggeringStatus_Type.__name__=_C
_FsMIOspfv3RTStaggeringStatus_Object=MibScalar
fsMIOspfv3RTStaggeringStatus=_FsMIOspfv3RTStaggeringStatus_Object((1,3,6,1,4,1,29601,2,24,1,3),_FsMIOspfv3RTStaggeringStatus_Type())
fsMIOspfv3RTStaggeringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RTStaggeringStatus.setStatus(_A)
class _FsMIOspfv3HotStandbyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3HotStandbyAdminStatus_Type.__name__=_C
_FsMIOspfv3HotStandbyAdminStatus_Object=MibScalar
fsMIOspfv3HotStandbyAdminStatus=_FsMIOspfv3HotStandbyAdminStatus_Object((1,3,6,1,4,1,29601,2,24,1,4),_FsMIOspfv3HotStandbyAdminStatus_Type())
fsMIOspfv3HotStandbyAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyAdminStatus.setStatus(_A)
class _FsMIOspfv3HotStandbyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FsMIOspfv3HotStandbyState_Type.__name__=_C
_FsMIOspfv3HotStandbyState_Object=MibScalar
fsMIOspfv3HotStandbyState=_FsMIOspfv3HotStandbyState_Object((1,3,6,1,4,1,29601,2,24,1,5),_FsMIOspfv3HotStandbyState_Type())
fsMIOspfv3HotStandbyState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyState.setStatus(_A)
class _FsMIOspfv3DynamicBulkUpdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('completed',3),('aborted',4)))
_FsMIOspfv3DynamicBulkUpdStatus_Type.__name__=_C
_FsMIOspfv3DynamicBulkUpdStatus_Object=MibScalar
fsMIOspfv3DynamicBulkUpdStatus=_FsMIOspfv3DynamicBulkUpdStatus_Object((1,3,6,1,4,1,29601,2,24,1,6),_FsMIOspfv3DynamicBulkUpdStatus_Type())
fsMIOspfv3DynamicBulkUpdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3DynamicBulkUpdStatus.setStatus(_A)
_FsMIOspfv3StandbyHelloSyncCount_Type=Counter32
_FsMIOspfv3StandbyHelloSyncCount_Object=MibScalar
fsMIOspfv3StandbyHelloSyncCount=_FsMIOspfv3StandbyHelloSyncCount_Object((1,3,6,1,4,1,29601,2,24,1,7),_FsMIOspfv3StandbyHelloSyncCount_Type())
fsMIOspfv3StandbyHelloSyncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3StandbyHelloSyncCount.setStatus(_A)
_FsMIOspfv3StandbyLsaSyncCount_Type=Counter32
_FsMIOspfv3StandbyLsaSyncCount_Object=MibScalar
fsMIOspfv3StandbyLsaSyncCount=_FsMIOspfv3StandbyLsaSyncCount_Object((1,3,6,1,4,1,29601,2,24,1,8),_FsMIOspfv3StandbyLsaSyncCount_Type())
fsMIOspfv3StandbyLsaSyncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3StandbyLsaSyncCount.setStatus(_A)
_FsMIOspfv3Table_Object=MibTable
fsMIOspfv3Table=_FsMIOspfv3Table_Object((1,3,6,1,4,1,29601,2,24,2))
if mibBuilder.loadTexts:fsMIOspfv3Table.setStatus(_A)
_FsMIOspfv3Entry_Object=MibTableRow
fsMIOspfv3Entry=_FsMIOspfv3Entry_Object((1,3,6,1,4,1,29601,2,24,2,1))
if mibBuilder.loadTexts:fsMIOspfv3Entry.setStatus(_A)
class _FsMIOspfv3OverFlowState_Type(TruthValue):defaultValue=2
_FsMIOspfv3OverFlowState_Type.__name__=_M
_FsMIOspfv3OverFlowState_Object=MibTableColumn
fsMIOspfv3OverFlowState=_FsMIOspfv3OverFlowState_Object((1,3,6,1,4,1,29601,2,24,2,1,1),_FsMIOspfv3OverFlowState_Type())
fsMIOspfv3OverFlowState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3OverFlowState.setStatus(_A)
class _FsMIOspfv3TraceLevel_Type(Integer32):defaultValue=2048
_FsMIOspfv3TraceLevel_Type.__name__=_C
_FsMIOspfv3TraceLevel_Object=MibTableColumn
fsMIOspfv3TraceLevel=_FsMIOspfv3TraceLevel_Object((1,3,6,1,4,1,29601,2,24,2,1,2),_FsMIOspfv3TraceLevel_Type())
fsMIOspfv3TraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3TraceLevel.setStatus(_A)
class _FsMIOspfv3ABRType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardABR',1),('ciscoABR',2),('ibmABR',3)))
_FsMIOspfv3ABRType_Type.__name__=_C
_FsMIOspfv3ABRType_Object=MibTableColumn
fsMIOspfv3ABRType=_FsMIOspfv3ABRType_Object((1,3,6,1,4,1,29601,2,24,2,1,3),_FsMIOspfv3ABRType_Type())
fsMIOspfv3ABRType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3ABRType.setStatus(_A)
class _FsMIOspfv3NssaAsbrDefRtTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3NssaAsbrDefRtTrans_Type.__name__=_C
_FsMIOspfv3NssaAsbrDefRtTrans_Object=MibTableColumn
fsMIOspfv3NssaAsbrDefRtTrans=_FsMIOspfv3NssaAsbrDefRtTrans_Object((1,3,6,1,4,1,29601,2,24,2,1,4),_FsMIOspfv3NssaAsbrDefRtTrans_Type())
fsMIOspfv3NssaAsbrDefRtTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3NssaAsbrDefRtTrans.setStatus(_A)
class _FsMIOspfv3DefaultPassiveInterface_Type(TruthValue):defaultValue=2
_FsMIOspfv3DefaultPassiveInterface_Type.__name__=_M
_FsMIOspfv3DefaultPassiveInterface_Object=MibTableColumn
fsMIOspfv3DefaultPassiveInterface=_FsMIOspfv3DefaultPassiveInterface_Object((1,3,6,1,4,1,29601,2,24,2,1,5),_FsMIOspfv3DefaultPassiveInterface_Type())
fsMIOspfv3DefaultPassiveInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3DefaultPassiveInterface.setStatus(_A)
class _FsMIOspfv3SpfDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3SpfDelay_Type.__name__=_C
_FsMIOspfv3SpfDelay_Object=MibTableColumn
fsMIOspfv3SpfDelay=_FsMIOspfv3SpfDelay_Object((1,3,6,1,4,1,29601,2,24,2,1,6),_FsMIOspfv3SpfDelay_Type())
fsMIOspfv3SpfDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3SpfDelay.setStatus(_A)
class _FsMIOspfv3SpfHoldTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3SpfHoldTime_Type.__name__=_C
_FsMIOspfv3SpfHoldTime_Object=MibTableColumn
fsMIOspfv3SpfHoldTime=_FsMIOspfv3SpfHoldTime_Object((1,3,6,1,4,1,29601,2,24,2,1,7),_FsMIOspfv3SpfHoldTime_Type())
fsMIOspfv3SpfHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3SpfHoldTime.setStatus(_A)
class _FsMIOspfv3RTStaggeringInterval_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,2147483647))
_FsMIOspfv3RTStaggeringInterval_Type.__name__=_C
_FsMIOspfv3RTStaggeringInterval_Object=MibTableColumn
fsMIOspfv3RTStaggeringInterval=_FsMIOspfv3RTStaggeringInterval_Object((1,3,6,1,4,1,29601,2,24,2,1,8),_FsMIOspfv3RTStaggeringInterval_Type())
fsMIOspfv3RTStaggeringInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RTStaggeringInterval.setStatus(_A)
class _FsMIOspfv3RestartStrictLsaChecking_Type(TruthValue):defaultValue=2
_FsMIOspfv3RestartStrictLsaChecking_Type.__name__=_M
_FsMIOspfv3RestartStrictLsaChecking_Object=MibTableColumn
fsMIOspfv3RestartStrictLsaChecking=_FsMIOspfv3RestartStrictLsaChecking_Object((1,3,6,1,4,1,29601,2,24,2,1,9),_FsMIOspfv3RestartStrictLsaChecking_Type())
fsMIOspfv3RestartStrictLsaChecking.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RestartStrictLsaChecking.setStatus(_A)
class _FsMIOspfv3HelperSupport_Type(Bits):namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3)))
_FsMIOspfv3HelperSupport_Type.__name__='Bits'
_FsMIOspfv3HelperSupport_Object=MibTableColumn
fsMIOspfv3HelperSupport=_FsMIOspfv3HelperSupport_Object((1,3,6,1,4,1,29601,2,24,2,1,10),_FsMIOspfv3HelperSupport_Type())
fsMIOspfv3HelperSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3HelperSupport.setStatus(_A)
class _FsMIOspfv3HelperGraceTimeLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_FsMIOspfv3HelperGraceTimeLimit_Type.__name__=_C
_FsMIOspfv3HelperGraceTimeLimit_Object=MibTableColumn
fsMIOspfv3HelperGraceTimeLimit=_FsMIOspfv3HelperGraceTimeLimit_Object((1,3,6,1,4,1,29601,2,24,2,1,11),_FsMIOspfv3HelperGraceTimeLimit_Type())
fsMIOspfv3HelperGraceTimeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3HelperGraceTimeLimit.setStatus(_A)
class _FsMIOspfv3RestartAckState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3RestartAckState_Type.__name__=_C
_FsMIOspfv3RestartAckState_Object=MibTableColumn
fsMIOspfv3RestartAckState=_FsMIOspfv3RestartAckState_Object((1,3,6,1,4,1,29601,2,24,2,1,12),_FsMIOspfv3RestartAckState_Type())
fsMIOspfv3RestartAckState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RestartAckState.setStatus(_A)
class _FsMIOspfv3GraceLsaRetransmitCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FsMIOspfv3GraceLsaRetransmitCount_Type.__name__=_C
_FsMIOspfv3GraceLsaRetransmitCount_Object=MibTableColumn
fsMIOspfv3GraceLsaRetransmitCount=_FsMIOspfv3GraceLsaRetransmitCount_Object((1,3,6,1,4,1,29601,2,24,2,1,13),_FsMIOspfv3GraceLsaRetransmitCount_Type())
fsMIOspfv3GraceLsaRetransmitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3GraceLsaRetransmitCount.setStatus(_A)
class _FsMIOspfv3RestartReason_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3)))
_FsMIOspfv3RestartReason_Type.__name__=_C
_FsMIOspfv3RestartReason_Object=MibTableColumn
fsMIOspfv3RestartReason=_FsMIOspfv3RestartReason_Object((1,3,6,1,4,1,29601,2,24,2,1,14),_FsMIOspfv3RestartReason_Type())
fsMIOspfv3RestartReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RestartReason.setStatus(_A)
_FsMIOspfv3ExtTraceLevel_Type=Integer32
_FsMIOspfv3ExtTraceLevel_Object=MibTableColumn
fsMIOspfv3ExtTraceLevel=_FsMIOspfv3ExtTraceLevel_Object((1,3,6,1,4,1,29601,2,24,2,1,15),_FsMIOspfv3ExtTraceLevel_Type())
fsMIOspfv3ExtTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3ExtTraceLevel.setStatus(_A)
_FsMIOspfv3SetTraps_Type=Integer32
_FsMIOspfv3SetTraps_Object=MibTableColumn
fsMIOspfv3SetTraps=_FsMIOspfv3SetTraps_Object((1,3,6,1,4,1,29601,2,24,2,1,16),_FsMIOspfv3SetTraps_Type())
fsMIOspfv3SetTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3SetTraps.setStatus(_A)
class _FsMIOspfv3BfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3BfdStatus_Type.__name__=_C
_FsMIOspfv3BfdStatus_Object=MibTableColumn
fsMIOspfv3BfdStatus=_FsMIOspfv3BfdStatus_Object((1,3,6,1,4,1,29601,2,24,2,1,17),_FsMIOspfv3BfdStatus_Type())
fsMIOspfv3BfdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3BfdStatus.setStatus(_A)
class _FsMIOspfv3BfdAllIfState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3BfdAllIfState_Type.__name__=_C
_FsMIOspfv3BfdAllIfState_Object=MibTableColumn
fsMIOspfv3BfdAllIfState=_FsMIOspfv3BfdAllIfState_Object((1,3,6,1,4,1,29601,2,24,2,1,18),_FsMIOspfv3BfdAllIfState_Type())
fsMIOspfv3BfdAllIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3BfdAllIfState.setStatus(_A)
_FsMIOspfv3IfTable_Object=MibTable
fsMIOspfv3IfTable=_FsMIOspfv3IfTable_Object((1,3,6,1,4,1,29601,2,24,3))
if mibBuilder.loadTexts:fsMIOspfv3IfTable.setStatus(_A)
_FsMIOspfv3IfEntry_Object=MibTableRow
fsMIOspfv3IfEntry=_FsMIOspfv3IfEntry_Object((1,3,6,1,4,1,29601,2,24,3,1))
fsMIOspfv3IfEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:fsMIOspfv3IfEntry.setStatus(_A)
_FsMIOspfv3IfIndex_Type=InterfaceIndex
_FsMIOspfv3IfIndex_Object=MibTableColumn
fsMIOspfv3IfIndex=_FsMIOspfv3IfIndex_Object((1,3,6,1,4,1,29601,2,24,3,1,1),_FsMIOspfv3IfIndex_Type())
fsMIOspfv3IfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3IfIndex.setStatus(_A)
class _FsMIOspfv3IfOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operup',1),('operdown',2),('loopback',3),('unloop',4)))
_FsMIOspfv3IfOperState_Type.__name__=_C
_FsMIOspfv3IfOperState_Object=MibTableColumn
fsMIOspfv3IfOperState=_FsMIOspfv3IfOperState_Object((1,3,6,1,4,1,29601,2,24,3,1,2),_FsMIOspfv3IfOperState_Type())
fsMIOspfv3IfOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfOperState.setStatus(_A)
class _FsMIOspfv3IfPassive_Type(TruthValue):defaultValue=2
_FsMIOspfv3IfPassive_Type.__name__=_M
_FsMIOspfv3IfPassive_Object=MibTableColumn
fsMIOspfv3IfPassive=_FsMIOspfv3IfPassive_Object((1,3,6,1,4,1,29601,2,24,3,1,3),_FsMIOspfv3IfPassive_Type())
fsMIOspfv3IfPassive.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfPassive.setStatus(_A)
_FsMIOspfv3IfNbrCount_Type=Gauge32
_FsMIOspfv3IfNbrCount_Object=MibTableColumn
fsMIOspfv3IfNbrCount=_FsMIOspfv3IfNbrCount_Object((1,3,6,1,4,1,29601,2,24,3,1,4),_FsMIOspfv3IfNbrCount_Type())
fsMIOspfv3IfNbrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfNbrCount.setStatus(_A)
_FsMIOspfv3IfAdjCount_Type=Gauge32
_FsMIOspfv3IfAdjCount_Object=MibTableColumn
fsMIOspfv3IfAdjCount=_FsMIOspfv3IfAdjCount_Object((1,3,6,1,4,1,29601,2,24,3,1,5),_FsMIOspfv3IfAdjCount_Type())
fsMIOspfv3IfAdjCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfAdjCount.setStatus(_A)
_FsMIOspfv3IfHelloRcvd_Type=Counter32
_FsMIOspfv3IfHelloRcvd_Object=MibTableColumn
fsMIOspfv3IfHelloRcvd=_FsMIOspfv3IfHelloRcvd_Object((1,3,6,1,4,1,29601,2,24,3,1,6),_FsMIOspfv3IfHelloRcvd_Type())
fsMIOspfv3IfHelloRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfHelloRcvd.setStatus(_A)
_FsMIOspfv3IfHelloTxed_Type=Counter32
_FsMIOspfv3IfHelloTxed_Object=MibTableColumn
fsMIOspfv3IfHelloTxed=_FsMIOspfv3IfHelloTxed_Object((1,3,6,1,4,1,29601,2,24,3,1,7),_FsMIOspfv3IfHelloTxed_Type())
fsMIOspfv3IfHelloTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfHelloTxed.setStatus(_A)
_FsMIOspfv3IfHelloDisd_Type=Counter32
_FsMIOspfv3IfHelloDisd_Object=MibTableColumn
fsMIOspfv3IfHelloDisd=_FsMIOspfv3IfHelloDisd_Object((1,3,6,1,4,1,29601,2,24,3,1,8),_FsMIOspfv3IfHelloDisd_Type())
fsMIOspfv3IfHelloDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfHelloDisd.setStatus(_A)
_FsMIOspfv3IfDdpRcvd_Type=Counter32
_FsMIOspfv3IfDdpRcvd_Object=MibTableColumn
fsMIOspfv3IfDdpRcvd=_FsMIOspfv3IfDdpRcvd_Object((1,3,6,1,4,1,29601,2,24,3,1,9),_FsMIOspfv3IfDdpRcvd_Type())
fsMIOspfv3IfDdpRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfDdpRcvd.setStatus(_A)
_FsMIOspfv3IfDdpTxed_Type=Counter32
_FsMIOspfv3IfDdpTxed_Object=MibTableColumn
fsMIOspfv3IfDdpTxed=_FsMIOspfv3IfDdpTxed_Object((1,3,6,1,4,1,29601,2,24,3,1,10),_FsMIOspfv3IfDdpTxed_Type())
fsMIOspfv3IfDdpTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfDdpTxed.setStatus(_A)
_FsMIOspfv3IfDdpDisd_Type=Counter32
_FsMIOspfv3IfDdpDisd_Object=MibTableColumn
fsMIOspfv3IfDdpDisd=_FsMIOspfv3IfDdpDisd_Object((1,3,6,1,4,1,29601,2,24,3,1,11),_FsMIOspfv3IfDdpDisd_Type())
fsMIOspfv3IfDdpDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfDdpDisd.setStatus(_A)
_FsMIOspfv3IfLrqRcvd_Type=Counter32
_FsMIOspfv3IfLrqRcvd_Object=MibTableColumn
fsMIOspfv3IfLrqRcvd=_FsMIOspfv3IfLrqRcvd_Object((1,3,6,1,4,1,29601,2,24,3,1,12),_FsMIOspfv3IfLrqRcvd_Type())
fsMIOspfv3IfLrqRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLrqRcvd.setStatus(_A)
_FsMIOspfv3IfLrqTxed_Type=Counter32
_FsMIOspfv3IfLrqTxed_Object=MibTableColumn
fsMIOspfv3IfLrqTxed=_FsMIOspfv3IfLrqTxed_Object((1,3,6,1,4,1,29601,2,24,3,1,13),_FsMIOspfv3IfLrqTxed_Type())
fsMIOspfv3IfLrqTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLrqTxed.setStatus(_A)
_FsMIOspfv3IfLrqDisd_Type=Counter32
_FsMIOspfv3IfLrqDisd_Object=MibTableColumn
fsMIOspfv3IfLrqDisd=_FsMIOspfv3IfLrqDisd_Object((1,3,6,1,4,1,29601,2,24,3,1,14),_FsMIOspfv3IfLrqDisd_Type())
fsMIOspfv3IfLrqDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLrqDisd.setStatus(_A)
_FsMIOspfv3IfLsuRcvd_Type=Counter32
_FsMIOspfv3IfLsuRcvd_Object=MibTableColumn
fsMIOspfv3IfLsuRcvd=_FsMIOspfv3IfLsuRcvd_Object((1,3,6,1,4,1,29601,2,24,3,1,15),_FsMIOspfv3IfLsuRcvd_Type())
fsMIOspfv3IfLsuRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLsuRcvd.setStatus(_A)
_FsMIOspfv3IfLsuTxed_Type=Counter32
_FsMIOspfv3IfLsuTxed_Object=MibTableColumn
fsMIOspfv3IfLsuTxed=_FsMIOspfv3IfLsuTxed_Object((1,3,6,1,4,1,29601,2,24,3,1,16),_FsMIOspfv3IfLsuTxed_Type())
fsMIOspfv3IfLsuTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLsuTxed.setStatus(_A)
_FsMIOspfv3IfLsuDisd_Type=Counter32
_FsMIOspfv3IfLsuDisd_Object=MibTableColumn
fsMIOspfv3IfLsuDisd=_FsMIOspfv3IfLsuDisd_Object((1,3,6,1,4,1,29601,2,24,3,1,17),_FsMIOspfv3IfLsuDisd_Type())
fsMIOspfv3IfLsuDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLsuDisd.setStatus(_A)
_FsMIOspfv3IfLakRcvd_Type=Counter32
_FsMIOspfv3IfLakRcvd_Object=MibTableColumn
fsMIOspfv3IfLakRcvd=_FsMIOspfv3IfLakRcvd_Object((1,3,6,1,4,1,29601,2,24,3,1,18),_FsMIOspfv3IfLakRcvd_Type())
fsMIOspfv3IfLakRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLakRcvd.setStatus(_A)
_FsMIOspfv3IfLakTxed_Type=Counter32
_FsMIOspfv3IfLakTxed_Object=MibTableColumn
fsMIOspfv3IfLakTxed=_FsMIOspfv3IfLakTxed_Object((1,3,6,1,4,1,29601,2,24,3,1,19),_FsMIOspfv3IfLakTxed_Type())
fsMIOspfv3IfLakTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLakTxed.setStatus(_A)
_FsMIOspfv3IfLakDisd_Type=Counter32
_FsMIOspfv3IfLakDisd_Object=MibTableColumn
fsMIOspfv3IfLakDisd=_FsMIOspfv3IfLakDisd_Object((1,3,6,1,4,1,29601,2,24,3,1,20),_FsMIOspfv3IfLakDisd_Type())
fsMIOspfv3IfLakDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLakDisd.setStatus(_A)
_FsMIOspfv3IfContextId_Type=Integer32
_FsMIOspfv3IfContextId_Object=MibTableColumn
fsMIOspfv3IfContextId=_FsMIOspfv3IfContextId_Object((1,3,6,1,4,1,29601,2,24,3,1,21),_FsMIOspfv3IfContextId_Type())
fsMIOspfv3IfContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfContextId.setStatus(_A)
class _FsMIOspfv3IfLinkLSASuppression_Type(TruthValue):defaultValue=2
_FsMIOspfv3IfLinkLSASuppression_Type.__name__=_M
_FsMIOspfv3IfLinkLSASuppression_Object=MibTableColumn
fsMIOspfv3IfLinkLSASuppression=_FsMIOspfv3IfLinkLSASuppression_Object((1,3,6,1,4,1,29601,2,24,3,1,22),_FsMIOspfv3IfLinkLSASuppression_Type())
fsMIOspfv3IfLinkLSASuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLinkLSASuppression.setStatus(_A)
class _FsMIOspfv3IfBfdState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3IfBfdState_Type.__name__=_C
_FsMIOspfv3IfBfdState_Object=MibTableColumn
fsMIOspfv3IfBfdState=_FsMIOspfv3IfBfdState_Object((1,3,6,1,4,1,29601,2,24,3,1,23),_FsMIOspfv3IfBfdState_Type())
fsMIOspfv3IfBfdState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfBfdState.setStatus(_A)
class _FsMIOspfv3IfCryptoAuthType_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6)));namedValues=NamedValues(*(('sha1',1),(_j,3),(_k,4),(_l,5),(_N,6)))
_FsMIOspfv3IfCryptoAuthType_Type.__name__=_C
_FsMIOspfv3IfCryptoAuthType_Object=MibTableColumn
fsMIOspfv3IfCryptoAuthType=_FsMIOspfv3IfCryptoAuthType_Object((1,3,6,1,4,1,29601,2,24,3,1,24),_FsMIOspfv3IfCryptoAuthType_Type())
fsMIOspfv3IfCryptoAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfCryptoAuthType.setStatus(_A)
class _FsMIOspfv3IfCryptoAuthMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),(_m,2),(_N,3)))
_FsMIOspfv3IfCryptoAuthMode_Type.__name__=_C
_FsMIOspfv3IfCryptoAuthMode_Object=MibTableColumn
fsMIOspfv3IfCryptoAuthMode=_FsMIOspfv3IfCryptoAuthMode_Object((1,3,6,1,4,1,29601,2,24,3,1,25),_FsMIOspfv3IfCryptoAuthMode_Type())
fsMIOspfv3IfCryptoAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfCryptoAuthMode.setStatus(_A)
_FsMIOspfv3IfAuthTxed_Type=Counter32
_FsMIOspfv3IfAuthTxed_Object=MibTableColumn
fsMIOspfv3IfAuthTxed=_FsMIOspfv3IfAuthTxed_Object((1,3,6,1,4,1,29601,2,24,3,1,26),_FsMIOspfv3IfAuthTxed_Type())
fsMIOspfv3IfAuthTxed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthTxed.setStatus(_A)
_FsMIOspfv3IfAuthRcvd_Type=Counter32
_FsMIOspfv3IfAuthRcvd_Object=MibTableColumn
fsMIOspfv3IfAuthRcvd=_FsMIOspfv3IfAuthRcvd_Object((1,3,6,1,4,1,29601,2,24,3,1,27),_FsMIOspfv3IfAuthRcvd_Type())
fsMIOspfv3IfAuthRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthRcvd.setStatus(_A)
_FsMIOspfv3IfAuthDisd_Type=Counter32
_FsMIOspfv3IfAuthDisd_Object=MibTableColumn
fsMIOspfv3IfAuthDisd=_FsMIOspfv3IfAuthDisd_Object((1,3,6,1,4,1,29601,2,24,3,1,28),_FsMIOspfv3IfAuthDisd_Type())
fsMIOspfv3IfAuthDisd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthDisd.setStatus(_A)
_FsMIOspfv3RoutingTable_Object=MibTable
fsMIOspfv3RoutingTable=_FsMIOspfv3RoutingTable_Object((1,3,6,1,4,1,29601,2,24,4))
if mibBuilder.loadTexts:fsMIOspfv3RoutingTable.setStatus(_A)
_FsMIOspfv3RoutingEntry_Object=MibTableRow
fsMIOspfv3RoutingEntry=_FsMIOspfv3RoutingEntry_Object((1,3,6,1,4,1,29601,2,24,4,1))
fsMIOspfv3RoutingEntry.setIndexNames((0,_G,_H),(0,_E,_n),(0,_E,_o),(0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:fsMIOspfv3RoutingEntry.setStatus(_A)
_FsMIOspfv3RouteDestType_Type=InetAddressType
_FsMIOspfv3RouteDestType_Object=MibTableColumn
fsMIOspfv3RouteDestType=_FsMIOspfv3RouteDestType_Object((1,3,6,1,4,1,29601,2,24,4,1,1),_FsMIOspfv3RouteDestType_Type())
fsMIOspfv3RouteDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RouteDestType.setStatus(_A)
class _FsMIOspfv3RouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3RouteDest_Type.__name__=_L
_FsMIOspfv3RouteDest_Object=MibTableColumn
fsMIOspfv3RouteDest=_FsMIOspfv3RouteDest_Object((1,3,6,1,4,1,29601,2,24,4,1,2),_FsMIOspfv3RouteDest_Type())
fsMIOspfv3RouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RouteDest.setStatus(_A)
_FsMIOspfv3RoutePfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3RoutePfxLength_Object=MibTableColumn
fsMIOspfv3RoutePfxLength=_FsMIOspfv3RoutePfxLength_Object((1,3,6,1,4,1,29601,2,24,4,1,3),_FsMIOspfv3RoutePfxLength_Type())
fsMIOspfv3RoutePfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RoutePfxLength.setStatus(_A)
_FsMIOspfv3RouteNextHopType_Type=InetAddressType
_FsMIOspfv3RouteNextHopType_Object=MibTableColumn
fsMIOspfv3RouteNextHopType=_FsMIOspfv3RouteNextHopType_Object((1,3,6,1,4,1,29601,2,24,4,1,4),_FsMIOspfv3RouteNextHopType_Type())
fsMIOspfv3RouteNextHopType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RouteNextHopType.setStatus(_A)
class _FsMIOspfv3RouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3RouteNextHop_Type.__name__=_L
_FsMIOspfv3RouteNextHop_Object=MibTableColumn
fsMIOspfv3RouteNextHop=_FsMIOspfv3RouteNextHop_Object((1,3,6,1,4,1,29601,2,24,4,1,5),_FsMIOspfv3RouteNextHop_Type())
fsMIOspfv3RouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RouteNextHop.setStatus(_A)
class _FsMIOspfv3RouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_s,1),(_t,2),(_u,3),(_v,4)))
_FsMIOspfv3RouteType_Type.__name__=_C
_FsMIOspfv3RouteType_Object=MibTableColumn
fsMIOspfv3RouteType=_FsMIOspfv3RouteType_Object((1,3,6,1,4,1,29601,2,24,4,1,6),_FsMIOspfv3RouteType_Type())
fsMIOspfv3RouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RouteType.setStatus(_A)
_FsMIOspfv3RouteAreaId_Type=AreaID
_FsMIOspfv3RouteAreaId_Object=MibTableColumn
fsMIOspfv3RouteAreaId=_FsMIOspfv3RouteAreaId_Object((1,3,6,1,4,1,29601,2,24,4,1,7),_FsMIOspfv3RouteAreaId_Type())
fsMIOspfv3RouteAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RouteAreaId.setStatus(_A)
_FsMIOspfv3RouteCost_Type=BigMetric
_FsMIOspfv3RouteCost_Object=MibTableColumn
fsMIOspfv3RouteCost=_FsMIOspfv3RouteCost_Object((1,3,6,1,4,1,29601,2,24,4,1,8),_FsMIOspfv3RouteCost_Type())
fsMIOspfv3RouteCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RouteCost.setStatus(_A)
_FsMIOspfv3RouteType2Cost_Type=BigMetric
_FsMIOspfv3RouteType2Cost_Object=MibTableColumn
fsMIOspfv3RouteType2Cost=_FsMIOspfv3RouteType2Cost_Object((1,3,6,1,4,1,29601,2,24,4,1,9),_FsMIOspfv3RouteType2Cost_Type())
fsMIOspfv3RouteType2Cost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RouteType2Cost.setStatus(_A)
class _FsMIOspfv3RouteInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIOspfv3RouteInterfaceIndex_Type.__name__=_C
_FsMIOspfv3RouteInterfaceIndex_Object=MibTableColumn
fsMIOspfv3RouteInterfaceIndex=_FsMIOspfv3RouteInterfaceIndex_Object((1,3,6,1,4,1,29601,2,24,4,1,10),_FsMIOspfv3RouteInterfaceIndex_Type())
fsMIOspfv3RouteInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RouteInterfaceIndex.setStatus(_A)
_FsMIOspfv3AsExternalAggregationTable_Object=MibTable
fsMIOspfv3AsExternalAggregationTable=_FsMIOspfv3AsExternalAggregationTable_Object((1,3,6,1,4,1,29601,2,24,5))
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationTable.setStatus(_A)
_FsMIOspfv3AsExternalAggregationEntry_Object=MibTableRow
fsMIOspfv3AsExternalAggregationEntry=_FsMIOspfv3AsExternalAggregationEntry_Object((1,3,6,1,4,1,29601,2,24,5,1))
fsMIOspfv3AsExternalAggregationEntry.setIndexNames((0,_G,_H),(0,_E,_w),(0,_E,_x),(0,_E,_y),(0,_E,_z))
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationEntry.setStatus(_A)
_FsMIOspfv3AsExternalAggregationNetType_Type=InetAddressType
_FsMIOspfv3AsExternalAggregationNetType_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationNetType=_FsMIOspfv3AsExternalAggregationNetType_Object((1,3,6,1,4,1,29601,2,24,5,1,1),_FsMIOspfv3AsExternalAggregationNetType_Type())
fsMIOspfv3AsExternalAggregationNetType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationNetType.setStatus(_A)
class _FsMIOspfv3AsExternalAggregationNet_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3AsExternalAggregationNet_Type.__name__=_L
_FsMIOspfv3AsExternalAggregationNet_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationNet=_FsMIOspfv3AsExternalAggregationNet_Object((1,3,6,1,4,1,29601,2,24,5,1,2),_FsMIOspfv3AsExternalAggregationNet_Type())
fsMIOspfv3AsExternalAggregationNet.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationNet.setStatus(_A)
_FsMIOspfv3AsExternalAggregationPfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3AsExternalAggregationPfxLength_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationPfxLength=_FsMIOspfv3AsExternalAggregationPfxLength_Object((1,3,6,1,4,1,29601,2,24,5,1,3),_FsMIOspfv3AsExternalAggregationPfxLength_Type())
fsMIOspfv3AsExternalAggregationPfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationPfxLength.setStatus(_A)
_FsMIOspfv3AsExternalAggregationAreaId_Type=AreaID
_FsMIOspfv3AsExternalAggregationAreaId_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationAreaId=_FsMIOspfv3AsExternalAggregationAreaId_Object((1,3,6,1,4,1,29601,2,24,5,1,4),_FsMIOspfv3AsExternalAggregationAreaId_Type())
fsMIOspfv3AsExternalAggregationAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationAreaId.setStatus(_A)
class _FsMIOspfv3AsExternalAggregationEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertise',1),('doNotAdvertise',2),('allowAll',3),('denyAll',4)))
_FsMIOspfv3AsExternalAggregationEffect_Type.__name__=_C
_FsMIOspfv3AsExternalAggregationEffect_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationEffect=_FsMIOspfv3AsExternalAggregationEffect_Object((1,3,6,1,4,1,29601,2,24,5,1,5),_FsMIOspfv3AsExternalAggregationEffect_Type())
fsMIOspfv3AsExternalAggregationEffect.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationEffect.setStatus(_A)
class _FsMIOspfv3AsExternalAggregationTranslation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3AsExternalAggregationTranslation_Type.__name__=_C
_FsMIOspfv3AsExternalAggregationTranslation_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationTranslation=_FsMIOspfv3AsExternalAggregationTranslation_Object((1,3,6,1,4,1,29601,2,24,5,1,6),_FsMIOspfv3AsExternalAggregationTranslation_Type())
fsMIOspfv3AsExternalAggregationTranslation.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationTranslation.setStatus(_A)
_FsMIOspfv3AsExternalAggregationStatus_Type=RowStatus
_FsMIOspfv3AsExternalAggregationStatus_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationStatus=_FsMIOspfv3AsExternalAggregationStatus_Object((1,3,6,1,4,1,29601,2,24,5,1,7),_FsMIOspfv3AsExternalAggregationStatus_Type())
fsMIOspfv3AsExternalAggregationStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationStatus.setStatus(_A)
_FsMIOspfv3BRRouteTable_Object=MibTable
fsMIOspfv3BRRouteTable=_FsMIOspfv3BRRouteTable_Object((1,3,6,1,4,1,29601,2,24,6))
if mibBuilder.loadTexts:fsMIOspfv3BRRouteTable.setStatus(_A)
_FsMIOspfv3BRRouteEntry_Object=MibTableRow
fsMIOspfv3BRRouteEntry=_FsMIOspfv3BRRouteEntry_Object((1,3,6,1,4,1,29601,2,24,6,1))
fsMIOspfv3BRRouteEntry.setIndexNames((0,_G,_H),(0,_E,_A0),(0,_E,_A1),(0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:fsMIOspfv3BRRouteEntry.setStatus(_A)
_FsMIOspfv3BRRouteDest_Type=IpAddress
_FsMIOspfv3BRRouteDest_Object=MibTableColumn
fsMIOspfv3BRRouteDest=_FsMIOspfv3BRRouteDest_Object((1,3,6,1,4,1,29601,2,24,6,1,1),_FsMIOspfv3BRRouteDest_Type())
fsMIOspfv3BRRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteDest.setStatus(_A)
_FsMIOspfv3BRRouteNextHopType_Type=InetAddressType
_FsMIOspfv3BRRouteNextHopType_Object=MibTableColumn
fsMIOspfv3BRRouteNextHopType=_FsMIOspfv3BRRouteNextHopType_Object((1,3,6,1,4,1,29601,2,24,6,1,2),_FsMIOspfv3BRRouteNextHopType_Type())
fsMIOspfv3BRRouteNextHopType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteNextHopType.setStatus(_A)
class _FsMIOspfv3BRRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3BRRouteNextHop_Type.__name__=_L
_FsMIOspfv3BRRouteNextHop_Object=MibTableColumn
fsMIOspfv3BRRouteNextHop=_FsMIOspfv3BRRouteNextHop_Object((1,3,6,1,4,1,29601,2,24,6,1,3),_FsMIOspfv3BRRouteNextHop_Type())
fsMIOspfv3BRRouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteNextHop.setStatus(_A)
class _FsMIOspfv3BRRouteDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('areaBorder',2),('asBoundary',3)))
_FsMIOspfv3BRRouteDestType_Type.__name__=_C
_FsMIOspfv3BRRouteDestType_Object=MibTableColumn
fsMIOspfv3BRRouteDestType=_FsMIOspfv3BRRouteDestType_Object((1,3,6,1,4,1,29601,2,24,6,1,4),_FsMIOspfv3BRRouteDestType_Type())
fsMIOspfv3BRRouteDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteDestType.setStatus(_A)
class _FsMIOspfv3BRRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_FsMIOspfv3BRRouteType_Type.__name__=_C
_FsMIOspfv3BRRouteType_Object=MibTableColumn
fsMIOspfv3BRRouteType=_FsMIOspfv3BRRouteType_Object((1,3,6,1,4,1,29601,2,24,6,1,5),_FsMIOspfv3BRRouteType_Type())
fsMIOspfv3BRRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteType.setStatus(_A)
_FsMIOspfv3BRRouteAreaId_Type=AreaID
_FsMIOspfv3BRRouteAreaId_Object=MibTableColumn
fsMIOspfv3BRRouteAreaId=_FsMIOspfv3BRRouteAreaId_Object((1,3,6,1,4,1,29601,2,24,6,1,6),_FsMIOspfv3BRRouteAreaId_Type())
fsMIOspfv3BRRouteAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteAreaId.setStatus(_A)
_FsMIOspfv3BRRouteCost_Type=BigMetric
_FsMIOspfv3BRRouteCost_Object=MibTableColumn
fsMIOspfv3BRRouteCost=_FsMIOspfv3BRRouteCost_Object((1,3,6,1,4,1,29601,2,24,6,1,7),_FsMIOspfv3BRRouteCost_Type())
fsMIOspfv3BRRouteCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteCost.setStatus(_A)
_FsMIOspfv3BRRouteInterfaceIndex_Type=InterfaceIndex
_FsMIOspfv3BRRouteInterfaceIndex_Object=MibTableColumn
fsMIOspfv3BRRouteInterfaceIndex=_FsMIOspfv3BRRouteInterfaceIndex_Object((1,3,6,1,4,1,29601,2,24,6,1,8),_FsMIOspfv3BRRouteInterfaceIndex_Type())
fsMIOspfv3BRRouteInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteInterfaceIndex.setStatus(_A)
_FsMIOspfv3RedistRouteCfgTable_Object=MibTable
fsMIOspfv3RedistRouteCfgTable=_FsMIOspfv3RedistRouteCfgTable_Object((1,3,6,1,4,1,29601,2,24,7))
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteCfgTable.setStatus(_A)
_FsMIOspfv3RedistRouteCfgEntry_Object=MibTableRow
fsMIOspfv3RedistRouteCfgEntry=_FsMIOspfv3RedistRouteCfgEntry_Object((1,3,6,1,4,1,29601,2,24,7,1))
fsMIOspfv3RedistRouteCfgEntry.setIndexNames((0,_G,_H),(0,_E,_A4),(0,_E,_A5),(0,_E,_A6))
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteCfgEntry.setStatus(_A)
_FsMIOspfv3RedistRouteDestType_Type=InetAddressType
_FsMIOspfv3RedistRouteDestType_Object=MibTableColumn
fsMIOspfv3RedistRouteDestType=_FsMIOspfv3RedistRouteDestType_Object((1,3,6,1,4,1,29601,2,24,7,1,1),_FsMIOspfv3RedistRouteDestType_Type())
fsMIOspfv3RedistRouteDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteDestType.setStatus(_A)
class _FsMIOspfv3RedistRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3RedistRouteDest_Type.__name__=_L
_FsMIOspfv3RedistRouteDest_Object=MibTableColumn
fsMIOspfv3RedistRouteDest=_FsMIOspfv3RedistRouteDest_Object((1,3,6,1,4,1,29601,2,24,7,1,2),_FsMIOspfv3RedistRouteDest_Type())
fsMIOspfv3RedistRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteDest.setStatus(_A)
_FsMIOspfv3RedistRoutePfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3RedistRoutePfxLength_Object=MibTableColumn
fsMIOspfv3RedistRoutePfxLength=_FsMIOspfv3RedistRoutePfxLength_Object((1,3,6,1,4,1,29601,2,24,7,1,3),_FsMIOspfv3RedistRoutePfxLength_Type())
fsMIOspfv3RedistRoutePfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3RedistRoutePfxLength.setStatus(_A)
class _FsMIOspfv3RedistRouteMetric_Type(BigMetric):defaultValue=10
_FsMIOspfv3RedistRouteMetric_Type.__name__=_b
_FsMIOspfv3RedistRouteMetric_Object=MibTableColumn
fsMIOspfv3RedistRouteMetric=_FsMIOspfv3RedistRouteMetric_Object((1,3,6,1,4,1,29601,2,24,7,1,4),_FsMIOspfv3RedistRouteMetric_Type())
fsMIOspfv3RedistRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteMetric.setStatus(_A)
class _FsMIOspfv3RedistRouteMetricType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_u,3),(_v,4)))
_FsMIOspfv3RedistRouteMetricType_Type.__name__=_C
_FsMIOspfv3RedistRouteMetricType_Object=MibTableColumn
fsMIOspfv3RedistRouteMetricType=_FsMIOspfv3RedistRouteMetricType_Object((1,3,6,1,4,1,29601,2,24,7,1,5),_FsMIOspfv3RedistRouteMetricType_Type())
fsMIOspfv3RedistRouteMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteMetricType.setStatus(_A)
class _FsMIOspfv3RedistRouteTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_FsMIOspfv3RedistRouteTagType_Type.__name__=_C
_FsMIOspfv3RedistRouteTagType_Object=MibTableColumn
fsMIOspfv3RedistRouteTagType=_FsMIOspfv3RedistRouteTagType_Object((1,3,6,1,4,1,29601,2,24,7,1,6),_FsMIOspfv3RedistRouteTagType_Type())
fsMIOspfv3RedistRouteTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteTagType.setStatus(_A)
class _FsMIOspfv3RedistRouteTag_Type(Integer32):defaultValue=0
_FsMIOspfv3RedistRouteTag_Type.__name__=_C
_FsMIOspfv3RedistRouteTag_Object=MibTableColumn
fsMIOspfv3RedistRouteTag=_FsMIOspfv3RedistRouteTag_Object((1,3,6,1,4,1,29601,2,24,7,1,7),_FsMIOspfv3RedistRouteTag_Type())
fsMIOspfv3RedistRouteTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteTag.setStatus(_A)
_FsMIOspfv3RedistRouteStatus_Type=RowStatus
_FsMIOspfv3RedistRouteStatus_Object=MibTableColumn
fsMIOspfv3RedistRouteStatus=_FsMIOspfv3RedistRouteStatus_Object((1,3,6,1,4,1,29601,2,24,7,1,8),_FsMIOspfv3RedistRouteStatus_Type())
fsMIOspfv3RedistRouteStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteStatus.setStatus(_A)
_FsMIOspfv3RRDGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3RRDGroup=_FsMIOspfv3RRDGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,24,8))
_FsMIOspfv3RRDGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3RRDGeneralGroup=_FsMIOspfv3RRDGeneralGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,24,8,1))
_FsMIOspfv3RRDRouteTable_Object=MibTable
fsMIOspfv3RRDRouteTable=_FsMIOspfv3RRDRouteTable_Object((1,3,6,1,4,1,29601,2,24,8,1,1))
if mibBuilder.loadTexts:fsMIOspfv3RRDRouteTable.setStatus(_A)
_FsMIOspfv3RRDRouteEntry_Object=MibTableRow
fsMIOspfv3RRDRouteEntry=_FsMIOspfv3RRDRouteEntry_Object((1,3,6,1,4,1,29601,2,24,8,1,1,1))
if mibBuilder.loadTexts:fsMIOspfv3RRDRouteEntry.setStatus(_A)
class _FsMIOspfv3RRDStatus_Type(Status):defaultValue=2
_FsMIOspfv3RRDStatus_Type.__name__=_c
_FsMIOspfv3RRDStatus_Object=MibTableColumn
fsMIOspfv3RRDStatus=_FsMIOspfv3RRDStatus_Object((1,3,6,1,4,1,29601,2,24,8,1,1,1,1),_FsMIOspfv3RRDStatus_Type())
fsMIOspfv3RRDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RRDStatus.setStatus(_A)
class _FsMIOspfv3RRDSrcProtoMask_Type(Integer32):defaultValue=0
_FsMIOspfv3RRDSrcProtoMask_Type.__name__=_C
_FsMIOspfv3RRDSrcProtoMask_Object=MibTableColumn
fsMIOspfv3RRDSrcProtoMask=_FsMIOspfv3RRDSrcProtoMask_Object((1,3,6,1,4,1,29601,2,24,8,1,1,1,2),_FsMIOspfv3RRDSrcProtoMask_Type())
fsMIOspfv3RRDSrcProtoMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RRDSrcProtoMask.setStatus(_A)
class _FsMIOspfv3RRDRouteMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsMIOspfv3RRDRouteMapName_Type.__name__=_P
_FsMIOspfv3RRDRouteMapName_Object=MibTableColumn
fsMIOspfv3RRDRouteMapName=_FsMIOspfv3RRDRouteMapName_Object((1,3,6,1,4,1,29601,2,24,8,1,1,1,3),_FsMIOspfv3RRDRouteMapName_Type())
fsMIOspfv3RRDRouteMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RRDRouteMapName.setStatus(_A)
_FsMIOspfv3DistInOutRouteMap_ObjectIdentity=ObjectIdentity
fsMIOspfv3DistInOutRouteMap=_FsMIOspfv3DistInOutRouteMap_ObjectIdentity((1,3,6,1,4,1,29601,2,24,9))
_FsMIOspfv3DistInOutRouteMapTable_Object=MibTable
fsMIOspfv3DistInOutRouteMapTable=_FsMIOspfv3DistInOutRouteMapTable_Object((1,3,6,1,4,1,29601,2,24,9,1))
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapTable.setStatus(_A)
_FsMIOspfv3DistInOutRouteMapEntry_Object=MibTableRow
fsMIOspfv3DistInOutRouteMapEntry=_FsMIOspfv3DistInOutRouteMapEntry_Object((1,3,6,1,4,1,29601,2,24,9,1,1))
fsMIOspfv3DistInOutRouteMapEntry.setIndexNames((0,_G,_H),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapEntry.setStatus(_A)
class _FsMIOspfv3DistInOutRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsMIOspfv3DistInOutRouteMapName_Type.__name__=_d
_FsMIOspfv3DistInOutRouteMapName_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapName=_FsMIOspfv3DistInOutRouteMapName_Object((1,3,6,1,4,1,29601,2,24,9,1,1,1),_FsMIOspfv3DistInOutRouteMapName_Type())
fsMIOspfv3DistInOutRouteMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapName.setStatus(_A)
class _FsMIOspfv3DistInOutRouteMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FsMIOspfv3DistInOutRouteMapType_Type.__name__=_C
_FsMIOspfv3DistInOutRouteMapType_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapType=_FsMIOspfv3DistInOutRouteMapType_Object((1,3,6,1,4,1,29601,2,24,9,1,1,2),_FsMIOspfv3DistInOutRouteMapType_Type())
fsMIOspfv3DistInOutRouteMapType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapType.setStatus(_A)
class _FsMIOspfv3DistInOutRouteMapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIOspfv3DistInOutRouteMapValue_Type.__name__=_C
_FsMIOspfv3DistInOutRouteMapValue_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapValue=_FsMIOspfv3DistInOutRouteMapValue_Object((1,3,6,1,4,1,29601,2,24,9,1,1,3),_FsMIOspfv3DistInOutRouteMapValue_Type())
fsMIOspfv3DistInOutRouteMapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapValue.setStatus(_A)
_FsMIOspfv3DistInOutRouteMapRowStatus_Type=RowStatus
_FsMIOspfv3DistInOutRouteMapRowStatus_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapRowStatus=_FsMIOspfv3DistInOutRouteMapRowStatus_Object((1,3,6,1,4,1,29601,2,24,9,1,1,4),_FsMIOspfv3DistInOutRouteMapRowStatus_Type())
fsMIOspfv3DistInOutRouteMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapRowStatus.setStatus(_A)
_FsMIOspfv3PreferenceGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3PreferenceGroup=_FsMIOspfv3PreferenceGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,24,10))
_FsMIOspfv3PreferenceTable_Object=MibTable
fsMIOspfv3PreferenceTable=_FsMIOspfv3PreferenceTable_Object((1,3,6,1,4,1,29601,2,24,10,1))
if mibBuilder.loadTexts:fsMIOspfv3PreferenceTable.setStatus(_A)
_FsMIOspfv3PreferenceEntry_Object=MibTableRow
fsMIOspfv3PreferenceEntry=_FsMIOspfv3PreferenceEntry_Object((1,3,6,1,4,1,29601,2,24,10,1,1))
if mibBuilder.loadTexts:fsMIOspfv3PreferenceEntry.setStatus(_A)
class _FsMIOspfv3PreferenceValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfv3PreferenceValue_Type.__name__=_C
_FsMIOspfv3PreferenceValue_Object=MibTableColumn
fsMIOspfv3PreferenceValue=_FsMIOspfv3PreferenceValue_Object((1,3,6,1,4,1,29601,2,24,10,1,1,1),_FsMIOspfv3PreferenceValue_Type())
fsMIOspfv3PreferenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3PreferenceValue.setStatus(_A)
_FsMIOspfv3NeighborBfdGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3NeighborBfdGroup=_FsMIOspfv3NeighborBfdGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,24,11))
_FsMIOspfv3NeighborBfdTable_Object=MibTable
fsMIOspfv3NeighborBfdTable=_FsMIOspfv3NeighborBfdTable_Object((1,3,6,1,4,1,29601,2,24,11,1))
if mibBuilder.loadTexts:fsMIOspfv3NeighborBfdTable.setStatus(_A)
_FsMIOspfv3NeighborBfdEntry_Object=MibTableRow
fsMIOspfv3NeighborBfdEntry=_FsMIOspfv3NeighborBfdEntry_Object((1,3,6,1,4,1,29601,2,24,11,1,1))
if mibBuilder.loadTexts:fsMIOspfv3NeighborBfdEntry.setStatus(_A)
class _FsMIOspfv3NbrBfdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsMIOspfv3NbrBfdState_Type.__name__=_C
_FsMIOspfv3NbrBfdState_Object=MibTableColumn
fsMIOspfv3NbrBfdState=_FsMIOspfv3NbrBfdState_Object((1,3,6,1,4,1,29601,2,24,11,1,1,1),_FsMIOspfv3NbrBfdState_Type())
fsMIOspfv3NbrBfdState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3NbrBfdState.setStatus(_A)
_FsMIOspfv3IfAuthTable_Object=MibTable
fsMIOspfv3IfAuthTable=_FsMIOspfv3IfAuthTable_Object((1,3,6,1,4,1,29601,2,24,12))
if mibBuilder.loadTexts:fsMIOspfv3IfAuthTable.setStatus(_A)
_FsMIOspfv3IfAuthEntry_Object=MibTableRow
fsMIOspfv3IfAuthEntry=_FsMIOspfv3IfAuthEntry_Object((1,3,6,1,4,1,29601,2,24,12,1))
fsMIOspfv3IfAuthEntry.setIndexNames((0,_G,_H),(0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:fsMIOspfv3IfAuthEntry.setStatus(_A)
class _FsMIOspfv3IfAuthIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3IfAuthIfIndex_Type.__name__=_a
_FsMIOspfv3IfAuthIfIndex_Object=MibTableColumn
fsMIOspfv3IfAuthIfIndex=_FsMIOspfv3IfAuthIfIndex_Object((1,3,6,1,4,1,29601,2,24,12,1,1),_FsMIOspfv3IfAuthIfIndex_Type())
fsMIOspfv3IfAuthIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthIfIndex.setStatus(_A)
class _FsMIOspfv3IfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3IfAuthKeyId_Type.__name__=_C
_FsMIOspfv3IfAuthKeyId_Object=MibTableColumn
fsMIOspfv3IfAuthKeyId=_FsMIOspfv3IfAuthKeyId_Object((1,3,6,1,4,1,29601,2,24,12,1,2),_FsMIOspfv3IfAuthKeyId_Type())
fsMIOspfv3IfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKeyId.setStatus(_A)
class _FsMIOspfv3IfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIOspfv3IfAuthKey_Type.__name__=_P
_FsMIOspfv3IfAuthKey_Object=MibTableColumn
fsMIOspfv3IfAuthKey=_FsMIOspfv3IfAuthKey_Object((1,3,6,1,4,1,29601,2,24,12,1,3),_FsMIOspfv3IfAuthKey_Type())
fsMIOspfv3IfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKey.setStatus(_A)
_FsMIOspfv3IfAuthKeyStartAccept_Type=DateAndTime
_FsMIOspfv3IfAuthKeyStartAccept_Object=MibTableColumn
fsMIOspfv3IfAuthKeyStartAccept=_FsMIOspfv3IfAuthKeyStartAccept_Object((1,3,6,1,4,1,29601,2,24,12,1,4),_FsMIOspfv3IfAuthKeyStartAccept_Type())
fsMIOspfv3IfAuthKeyStartAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKeyStartAccept.setStatus(_A)
_FsMIOspfv3IfAuthKeyStartGenerate_Type=DateAndTime
_FsMIOspfv3IfAuthKeyStartGenerate_Object=MibTableColumn
fsMIOspfv3IfAuthKeyStartGenerate=_FsMIOspfv3IfAuthKeyStartGenerate_Object((1,3,6,1,4,1,29601,2,24,12,1,5),_FsMIOspfv3IfAuthKeyStartGenerate_Type())
fsMIOspfv3IfAuthKeyStartGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKeyStartGenerate.setStatus(_A)
_FsMIOspfv3IfAuthKeyStopGenerate_Type=DateAndTime
_FsMIOspfv3IfAuthKeyStopGenerate_Object=MibTableColumn
fsMIOspfv3IfAuthKeyStopGenerate=_FsMIOspfv3IfAuthKeyStopGenerate_Object((1,3,6,1,4,1,29601,2,24,12,1,6),_FsMIOspfv3IfAuthKeyStopGenerate_Type())
fsMIOspfv3IfAuthKeyStopGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKeyStopGenerate.setStatus(_A)
_FsMIOspfv3IfAuthKeyStopAccept_Type=DateAndTime
_FsMIOspfv3IfAuthKeyStopAccept_Object=MibTableColumn
fsMIOspfv3IfAuthKeyStopAccept=_FsMIOspfv3IfAuthKeyStopAccept_Object((1,3,6,1,4,1,29601,2,24,12,1,7),_FsMIOspfv3IfAuthKeyStopAccept_Type())
fsMIOspfv3IfAuthKeyStopAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKeyStopAccept.setStatus(_A)
_FsMIOspfv3IfAuthKeyStatus_Type=RowStatus
_FsMIOspfv3IfAuthKeyStatus_Object=MibTableColumn
fsMIOspfv3IfAuthKeyStatus=_FsMIOspfv3IfAuthKeyStatus_Object((1,3,6,1,4,1,29601,2,24,12,1,8),_FsMIOspfv3IfAuthKeyStatus_Type())
fsMIOspfv3IfAuthKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAuthKeyStatus.setStatus(_A)
_FsMIOspfv3VirtIfAuthTable_Object=MibTable
fsMIOspfv3VirtIfAuthTable=_FsMIOspfv3VirtIfAuthTable_Object((1,3,6,1,4,1,29601,2,24,13))
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthTable.setStatus(_A)
_FsMIOspfv3VirtIfAuthEntry_Object=MibTableRow
fsMIOspfv3VirtIfAuthEntry=_FsMIOspfv3VirtIfAuthEntry_Object((1,3,6,1,4,1,29601,2,24,13,1))
fsMIOspfv3VirtIfAuthEntry.setIndexNames((0,_G,_H),(0,_E,_AB),(0,_E,_AC),(0,_E,_AD))
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthEntry.setStatus(_A)
_FsMIOspfv3VirtIfAuthAreaId_Type=AreaID
_FsMIOspfv3VirtIfAuthAreaId_Object=MibTableColumn
fsMIOspfv3VirtIfAuthAreaId=_FsMIOspfv3VirtIfAuthAreaId_Object((1,3,6,1,4,1,29601,2,24,13,1,1),_FsMIOspfv3VirtIfAuthAreaId_Type())
fsMIOspfv3VirtIfAuthAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthAreaId.setStatus(_A)
_FsMIOspfv3VirtIfAuthNeighbor_Type=RouterID
_FsMIOspfv3VirtIfAuthNeighbor_Object=MibTableColumn
fsMIOspfv3VirtIfAuthNeighbor=_FsMIOspfv3VirtIfAuthNeighbor_Object((1,3,6,1,4,1,29601,2,24,13,1,2),_FsMIOspfv3VirtIfAuthNeighbor_Type())
fsMIOspfv3VirtIfAuthNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthNeighbor.setStatus(_A)
class _FsMIOspfv3VirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3VirtIfAuthKeyId_Type.__name__=_C
_FsMIOspfv3VirtIfAuthKeyId_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKeyId=_FsMIOspfv3VirtIfAuthKeyId_Object((1,3,6,1,4,1,29601,2,24,13,1,3),_FsMIOspfv3VirtIfAuthKeyId_Type())
fsMIOspfv3VirtIfAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKeyId.setStatus(_A)
class _FsMIOspfv3VirtIfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIOspfv3VirtIfAuthKey_Type.__name__=_P
_FsMIOspfv3VirtIfAuthKey_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKey=_FsMIOspfv3VirtIfAuthKey_Object((1,3,6,1,4,1,29601,2,24,13,1,4),_FsMIOspfv3VirtIfAuthKey_Type())
fsMIOspfv3VirtIfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKey.setStatus(_A)
_FsMIOspfv3VirtIfAuthKeyStartAccept_Type=DateAndTime
_FsMIOspfv3VirtIfAuthKeyStartAccept_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKeyStartAccept=_FsMIOspfv3VirtIfAuthKeyStartAccept_Object((1,3,6,1,4,1,29601,2,24,13,1,5),_FsMIOspfv3VirtIfAuthKeyStartAccept_Type())
fsMIOspfv3VirtIfAuthKeyStartAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKeyStartAccept.setStatus(_A)
_FsMIOspfv3VirtIfAuthKeyStartGenerate_Type=DateAndTime
_FsMIOspfv3VirtIfAuthKeyStartGenerate_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKeyStartGenerate=_FsMIOspfv3VirtIfAuthKeyStartGenerate_Object((1,3,6,1,4,1,29601,2,24,13,1,6),_FsMIOspfv3VirtIfAuthKeyStartGenerate_Type())
fsMIOspfv3VirtIfAuthKeyStartGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKeyStartGenerate.setStatus(_A)
_FsMIOspfv3VirtIfAuthKeyStopGenerate_Type=DateAndTime
_FsMIOspfv3VirtIfAuthKeyStopGenerate_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKeyStopGenerate=_FsMIOspfv3VirtIfAuthKeyStopGenerate_Object((1,3,6,1,4,1,29601,2,24,13,1,7),_FsMIOspfv3VirtIfAuthKeyStopGenerate_Type())
fsMIOspfv3VirtIfAuthKeyStopGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKeyStopGenerate.setStatus(_A)
_FsMIOspfv3VirtIfAuthKeyStopAccept_Type=DateAndTime
_FsMIOspfv3VirtIfAuthKeyStopAccept_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKeyStopAccept=_FsMIOspfv3VirtIfAuthKeyStopAccept_Object((1,3,6,1,4,1,29601,2,24,13,1,8),_FsMIOspfv3VirtIfAuthKeyStopAccept_Type())
fsMIOspfv3VirtIfAuthKeyStopAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKeyStopAccept.setStatus(_A)
_FsMIOspfv3VirtIfAuthKeyStatus_Type=RowStatus
_FsMIOspfv3VirtIfAuthKeyStatus_Object=MibTableColumn
fsMIOspfv3VirtIfAuthKeyStatus=_FsMIOspfv3VirtIfAuthKeyStatus_Object((1,3,6,1,4,1,29601,2,24,13,1,9),_FsMIOspfv3VirtIfAuthKeyStatus_Type())
fsMIOspfv3VirtIfAuthKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfAuthKeyStatus.setStatus(_A)
_FsMIOspfv3VirtIfCryptoAuthTable_Object=MibTable
fsMIOspfv3VirtIfCryptoAuthTable=_FsMIOspfv3VirtIfCryptoAuthTable_Object((1,3,6,1,4,1,29601,2,24,14))
if mibBuilder.loadTexts:fsMIOspfv3VirtIfCryptoAuthTable.setStatus(_A)
_FsMIOspfv3VirtIfCryptoAuthEntry_Object=MibTableRow
fsMIOspfv3VirtIfCryptoAuthEntry=_FsMIOspfv3VirtIfCryptoAuthEntry_Object((1,3,6,1,4,1,29601,2,24,14,1))
if mibBuilder.loadTexts:fsMIOspfv3VirtIfCryptoAuthEntry.setStatus(_A)
class _FsMIOspfv3VirtIfCryptoAuthType_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6)));namedValues=NamedValues(*(('sha1',1),(_j,3),(_k,4),(_l,5),(_N,6)))
_FsMIOspfv3VirtIfCryptoAuthType_Type.__name__=_C
_FsMIOspfv3VirtIfCryptoAuthType_Object=MibTableColumn
fsMIOspfv3VirtIfCryptoAuthType=_FsMIOspfv3VirtIfCryptoAuthType_Object((1,3,6,1,4,1,29601,2,24,14,1,1),_FsMIOspfv3VirtIfCryptoAuthType_Type())
fsMIOspfv3VirtIfCryptoAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfCryptoAuthType.setStatus(_A)
class _FsMIOspfv3VirtIfCryptoAuthMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),(_m,2),(_N,3)))
_FsMIOspfv3VirtIfCryptoAuthMode_Type.__name__=_C
_FsMIOspfv3VirtIfCryptoAuthMode_Object=MibTableColumn
fsMIOspfv3VirtIfCryptoAuthMode=_FsMIOspfv3VirtIfCryptoAuthMode_Object((1,3,6,1,4,1,29601,2,24,14,1,2),_FsMIOspfv3VirtIfCryptoAuthMode_Type())
fsMIOspfv3VirtIfCryptoAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3VirtIfCryptoAuthMode.setStatus(_A)
_FsMIOspfv3Notification_ObjectIdentity=ObjectIdentity
fsMIOspfv3Notification=_FsMIOspfv3Notification_ObjectIdentity((1,3,6,1,4,1,29601,2,24,101))
_FsMIOspfv3Traps_ObjectIdentity=ObjectIdentity
fsMIOspfv3Traps=_FsMIOspfv3Traps_ObjectIdentity((1,3,6,1,4,1,29601,2,24,101,0))
_FsMIOspfv3TrapObject_ObjectIdentity=ObjectIdentity
fsMIOspfv3TrapObject=_FsMIOspfv3TrapObject_ObjectIdentity((1,3,6,1,4,1,29601,2,24,101,1))
_FsMIOspfv3TrapNbrIfIndex_Type=InterfaceIndex
_FsMIOspfv3TrapNbrIfIndex_Object=MibScalar
fsMIOspfv3TrapNbrIfIndex=_FsMIOspfv3TrapNbrIfIndex_Object((1,3,6,1,4,1,29601,2,24,101,1,1),_FsMIOspfv3TrapNbrIfIndex_Type())
fsMIOspfv3TrapNbrIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3TrapNbrIfIndex.setStatus(_A)
_FsMIOspfv3TrapVirtNbrRtrId_Type=RouterID
_FsMIOspfv3TrapVirtNbrRtrId_Object=MibScalar
fsMIOspfv3TrapVirtNbrRtrId=_FsMIOspfv3TrapVirtNbrRtrId_Object((1,3,6,1,4,1,29601,2,24,101,1,2),_FsMIOspfv3TrapVirtNbrRtrId_Type())
fsMIOspfv3TrapVirtNbrRtrId.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3TrapVirtNbrRtrId.setStatus(_A)
_FsMIOspfv3TrapNbrRtrId_Type=RouterID
_FsMIOspfv3TrapNbrRtrId_Object=MibScalar
fsMIOspfv3TrapNbrRtrId=_FsMIOspfv3TrapNbrRtrId_Object((1,3,6,1,4,1,29601,2,24,101,1,3),_FsMIOspfv3TrapNbrRtrId_Type())
fsMIOspfv3TrapNbrRtrId.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3TrapNbrRtrId.setStatus(_A)
_FsMIOspfv3TrapVirtNbrArea_Type=AreaID
_FsMIOspfv3TrapVirtNbrArea_Object=MibScalar
fsMIOspfv3TrapVirtNbrArea=_FsMIOspfv3TrapVirtNbrArea_Object((1,3,6,1,4,1,29601,2,24,101,1,4),_FsMIOspfv3TrapVirtNbrArea_Type())
fsMIOspfv3TrapVirtNbrArea.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3TrapVirtNbrArea.setStatus(_A)
class _FsMIOspfv3TrapBulkUpdAbortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('memAllocFailed',2),('sendFailed',3),('processFailed',4)))
_FsMIOspfv3TrapBulkUpdAbortReason_Type.__name__=_C
_FsMIOspfv3TrapBulkUpdAbortReason_Object=MibScalar
fsMIOspfv3TrapBulkUpdAbortReason=_FsMIOspfv3TrapBulkUpdAbortReason_Object((1,3,6,1,4,1,29601,2,24,101,1,5),_FsMIOspfv3TrapBulkUpdAbortReason_Type())
fsMIOspfv3TrapBulkUpdAbortReason.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3TrapBulkUpdAbortReason.setStatus(_A)
fsMIStdOspfv3Entry.registerAugmentions((_E,_AE))
fsMIOspfv3Entry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3Entry.registerAugmentions((_E,_AF))
fsMIOspfv3RRDRouteEntry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3Entry.registerAugmentions((_E,_AG))
fsMIOspfv3PreferenceEntry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3NbrEntry.registerAugmentions((_E,_AH))
fsMIOspfv3NeighborBfdEntry.setIndexNames(*fsMIStdOspfv3NbrEntry.getIndexNames())
fsMIStdOspfv3VirtIfEntry.registerAugmentions((_E,_AI))
fsMIOspfv3VirtIfCryptoAuthEntry.setIndexNames(*fsMIStdOspfv3VirtIfEntry.getIndexNames())
fsMIOspfv3RestartStatusChange=NotificationType((1,3,6,1,4,1,29601,2,24,101,0,1))
fsMIOspfv3RestartStatusChange.setObjects(*((_G,_K),(_G,_W),(_G,_V),(_G,_U)))
if mibBuilder.loadTexts:fsMIOspfv3RestartStatusChange.setStatus(_A)
fsMIOspfv3NbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,29601,2,24,101,0,2))
fsMIOspfv3NbrRestartHelperStatusChange.setObjects(*((_G,_K),(_E,_AJ),(_E,_AK),(_G,_T),(_G,_R),(_G,_S)))
if mibBuilder.loadTexts:fsMIOspfv3NbrRestartHelperStatusChange.setStatus(_A)
fsMIOspfv3VirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,29601,2,24,101,0,3))
fsMIOspfv3VirtNbrRestartHelperStatusChange.setObjects(*((_G,_K),(_E,_AL),(_E,_AM),(_G,_Z),(_G,_X),(_G,_Y)))
if mibBuilder.loadTexts:fsMIOspfv3VirtNbrRestartHelperStatusChange.setStatus(_A)
fsMIOspfv3HotStandbyStateChgTrap=NotificationType((1,3,6,1,4,1,29601,2,24,101,0,4))
fsMIOspfv3HotStandbyStateChgTrap.setObjects(*((_G,_K),(_E,_AN)))
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyStateChgTrap.setStatus(_A)
fsMIOspfv3HotStandbyBulkUpdAbortTrap=NotificationType((1,3,6,1,4,1,29601,2,24,101,0,5))
fsMIOspfv3HotStandbyBulkUpdAbortTrap.setObjects(*((_G,_K),(_E,_AO),(_E,_AP)))
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyBulkUpdAbortTrap.setStatus(_A)
fsMIOspfv3AuthSequenceNumWrap=NotificationType((1,3,6,1,4,1,29601,2,24,101,0,6))
fsMIOspfv3AuthSequenceNumWrap.setObjects((_G,_K))
if mibBuilder.loadTexts:fsMIOspfv3AuthSequenceNumWrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsMIOspfv3':fsMIOspfv3,'fsMIOspfv3GeneralGroup':fsMIOspfv3GeneralGroup,'fsMIOspfv3GlobalTraceLevel':fsMIOspfv3GlobalTraceLevel,'fsMIOspfv3VrfSpfInterval':fsMIOspfv3VrfSpfInterval,'fsMIOspfv3RTStaggeringStatus':fsMIOspfv3RTStaggeringStatus,'fsMIOspfv3HotStandbyAdminStatus':fsMIOspfv3HotStandbyAdminStatus,_AN:fsMIOspfv3HotStandbyState,_AO:fsMIOspfv3DynamicBulkUpdStatus,'fsMIOspfv3StandbyHelloSyncCount':fsMIOspfv3StandbyHelloSyncCount,'fsMIOspfv3StandbyLsaSyncCount':fsMIOspfv3StandbyLsaSyncCount,'fsMIOspfv3Table':fsMIOspfv3Table,_AE:fsMIOspfv3Entry,'fsMIOspfv3OverFlowState':fsMIOspfv3OverFlowState,'fsMIOspfv3TraceLevel':fsMIOspfv3TraceLevel,'fsMIOspfv3ABRType':fsMIOspfv3ABRType,'fsMIOspfv3NssaAsbrDefRtTrans':fsMIOspfv3NssaAsbrDefRtTrans,'fsMIOspfv3DefaultPassiveInterface':fsMIOspfv3DefaultPassiveInterface,'fsMIOspfv3SpfDelay':fsMIOspfv3SpfDelay,'fsMIOspfv3SpfHoldTime':fsMIOspfv3SpfHoldTime,'fsMIOspfv3RTStaggeringInterval':fsMIOspfv3RTStaggeringInterval,'fsMIOspfv3RestartStrictLsaChecking':fsMIOspfv3RestartStrictLsaChecking,'fsMIOspfv3HelperSupport':fsMIOspfv3HelperSupport,'fsMIOspfv3HelperGraceTimeLimit':fsMIOspfv3HelperGraceTimeLimit,'fsMIOspfv3RestartAckState':fsMIOspfv3RestartAckState,'fsMIOspfv3GraceLsaRetransmitCount':fsMIOspfv3GraceLsaRetransmitCount,'fsMIOspfv3RestartReason':fsMIOspfv3RestartReason,'fsMIOspfv3ExtTraceLevel':fsMIOspfv3ExtTraceLevel,'fsMIOspfv3SetTraps':fsMIOspfv3SetTraps,'fsMIOspfv3BfdStatus':fsMIOspfv3BfdStatus,'fsMIOspfv3BfdAllIfState':fsMIOspfv3BfdAllIfState,'fsMIOspfv3IfTable':fsMIOspfv3IfTable,'fsMIOspfv3IfEntry':fsMIOspfv3IfEntry,_i:fsMIOspfv3IfIndex,'fsMIOspfv3IfOperState':fsMIOspfv3IfOperState,'fsMIOspfv3IfPassive':fsMIOspfv3IfPassive,'fsMIOspfv3IfNbrCount':fsMIOspfv3IfNbrCount,'fsMIOspfv3IfAdjCount':fsMIOspfv3IfAdjCount,'fsMIOspfv3IfHelloRcvd':fsMIOspfv3IfHelloRcvd,'fsMIOspfv3IfHelloTxed':fsMIOspfv3IfHelloTxed,'fsMIOspfv3IfHelloDisd':fsMIOspfv3IfHelloDisd,'fsMIOspfv3IfDdpRcvd':fsMIOspfv3IfDdpRcvd,'fsMIOspfv3IfDdpTxed':fsMIOspfv3IfDdpTxed,'fsMIOspfv3IfDdpDisd':fsMIOspfv3IfDdpDisd,'fsMIOspfv3IfLrqRcvd':fsMIOspfv3IfLrqRcvd,'fsMIOspfv3IfLrqTxed':fsMIOspfv3IfLrqTxed,'fsMIOspfv3IfLrqDisd':fsMIOspfv3IfLrqDisd,'fsMIOspfv3IfLsuRcvd':fsMIOspfv3IfLsuRcvd,'fsMIOspfv3IfLsuTxed':fsMIOspfv3IfLsuTxed,'fsMIOspfv3IfLsuDisd':fsMIOspfv3IfLsuDisd,'fsMIOspfv3IfLakRcvd':fsMIOspfv3IfLakRcvd,'fsMIOspfv3IfLakTxed':fsMIOspfv3IfLakTxed,'fsMIOspfv3IfLakDisd':fsMIOspfv3IfLakDisd,'fsMIOspfv3IfContextId':fsMIOspfv3IfContextId,'fsMIOspfv3IfLinkLSASuppression':fsMIOspfv3IfLinkLSASuppression,'fsMIOspfv3IfBfdState':fsMIOspfv3IfBfdState,'fsMIOspfv3IfCryptoAuthType':fsMIOspfv3IfCryptoAuthType,'fsMIOspfv3IfCryptoAuthMode':fsMIOspfv3IfCryptoAuthMode,'fsMIOspfv3IfAuthTxed':fsMIOspfv3IfAuthTxed,'fsMIOspfv3IfAuthRcvd':fsMIOspfv3IfAuthRcvd,'fsMIOspfv3IfAuthDisd':fsMIOspfv3IfAuthDisd,'fsMIOspfv3RoutingTable':fsMIOspfv3RoutingTable,'fsMIOspfv3RoutingEntry':fsMIOspfv3RoutingEntry,_n:fsMIOspfv3RouteDestType,_o:fsMIOspfv3RouteDest,_p:fsMIOspfv3RoutePfxLength,_q:fsMIOspfv3RouteNextHopType,_r:fsMIOspfv3RouteNextHop,'fsMIOspfv3RouteType':fsMIOspfv3RouteType,'fsMIOspfv3RouteAreaId':fsMIOspfv3RouteAreaId,'fsMIOspfv3RouteCost':fsMIOspfv3RouteCost,'fsMIOspfv3RouteType2Cost':fsMIOspfv3RouteType2Cost,'fsMIOspfv3RouteInterfaceIndex':fsMIOspfv3RouteInterfaceIndex,'fsMIOspfv3AsExternalAggregationTable':fsMIOspfv3AsExternalAggregationTable,'fsMIOspfv3AsExternalAggregationEntry':fsMIOspfv3AsExternalAggregationEntry,_w:fsMIOspfv3AsExternalAggregationNetType,_x:fsMIOspfv3AsExternalAggregationNet,_y:fsMIOspfv3AsExternalAggregationPfxLength,_z:fsMIOspfv3AsExternalAggregationAreaId,'fsMIOspfv3AsExternalAggregationEffect':fsMIOspfv3AsExternalAggregationEffect,'fsMIOspfv3AsExternalAggregationTranslation':fsMIOspfv3AsExternalAggregationTranslation,'fsMIOspfv3AsExternalAggregationStatus':fsMIOspfv3AsExternalAggregationStatus,'fsMIOspfv3BRRouteTable':fsMIOspfv3BRRouteTable,'fsMIOspfv3BRRouteEntry':fsMIOspfv3BRRouteEntry,_A0:fsMIOspfv3BRRouteDest,_A1:fsMIOspfv3BRRouteNextHopType,_A2:fsMIOspfv3BRRouteNextHop,_A3:fsMIOspfv3BRRouteDestType,'fsMIOspfv3BRRouteType':fsMIOspfv3BRRouteType,'fsMIOspfv3BRRouteAreaId':fsMIOspfv3BRRouteAreaId,'fsMIOspfv3BRRouteCost':fsMIOspfv3BRRouteCost,'fsMIOspfv3BRRouteInterfaceIndex':fsMIOspfv3BRRouteInterfaceIndex,'fsMIOspfv3RedistRouteCfgTable':fsMIOspfv3RedistRouteCfgTable,'fsMIOspfv3RedistRouteCfgEntry':fsMIOspfv3RedistRouteCfgEntry,_A4:fsMIOspfv3RedistRouteDestType,_A5:fsMIOspfv3RedistRouteDest,_A6:fsMIOspfv3RedistRoutePfxLength,'fsMIOspfv3RedistRouteMetric':fsMIOspfv3RedistRouteMetric,'fsMIOspfv3RedistRouteMetricType':fsMIOspfv3RedistRouteMetricType,'fsMIOspfv3RedistRouteTagType':fsMIOspfv3RedistRouteTagType,'fsMIOspfv3RedistRouteTag':fsMIOspfv3RedistRouteTag,'fsMIOspfv3RedistRouteStatus':fsMIOspfv3RedistRouteStatus,'fsMIOspfv3RRDGroup':fsMIOspfv3RRDGroup,'fsMIOspfv3RRDGeneralGroup':fsMIOspfv3RRDGeneralGroup,'fsMIOspfv3RRDRouteTable':fsMIOspfv3RRDRouteTable,_AF:fsMIOspfv3RRDRouteEntry,'fsMIOspfv3RRDStatus':fsMIOspfv3RRDStatus,'fsMIOspfv3RRDSrcProtoMask':fsMIOspfv3RRDSrcProtoMask,'fsMIOspfv3RRDRouteMapName':fsMIOspfv3RRDRouteMapName,'fsMIOspfv3DistInOutRouteMap':fsMIOspfv3DistInOutRouteMap,'fsMIOspfv3DistInOutRouteMapTable':fsMIOspfv3DistInOutRouteMapTable,'fsMIOspfv3DistInOutRouteMapEntry':fsMIOspfv3DistInOutRouteMapEntry,_A7:fsMIOspfv3DistInOutRouteMapName,_A8:fsMIOspfv3DistInOutRouteMapType,'fsMIOspfv3DistInOutRouteMapValue':fsMIOspfv3DistInOutRouteMapValue,'fsMIOspfv3DistInOutRouteMapRowStatus':fsMIOspfv3DistInOutRouteMapRowStatus,'fsMIOspfv3PreferenceGroup':fsMIOspfv3PreferenceGroup,'fsMIOspfv3PreferenceTable':fsMIOspfv3PreferenceTable,_AG:fsMIOspfv3PreferenceEntry,'fsMIOspfv3PreferenceValue':fsMIOspfv3PreferenceValue,'fsMIOspfv3NeighborBfdGroup':fsMIOspfv3NeighborBfdGroup,'fsMIOspfv3NeighborBfdTable':fsMIOspfv3NeighborBfdTable,_AH:fsMIOspfv3NeighborBfdEntry,'fsMIOspfv3NbrBfdState':fsMIOspfv3NbrBfdState,'fsMIOspfv3IfAuthTable':fsMIOspfv3IfAuthTable,'fsMIOspfv3IfAuthEntry':fsMIOspfv3IfAuthEntry,_A9:fsMIOspfv3IfAuthIfIndex,_AA:fsMIOspfv3IfAuthKeyId,'fsMIOspfv3IfAuthKey':fsMIOspfv3IfAuthKey,'fsMIOspfv3IfAuthKeyStartAccept':fsMIOspfv3IfAuthKeyStartAccept,'fsMIOspfv3IfAuthKeyStartGenerate':fsMIOspfv3IfAuthKeyStartGenerate,'fsMIOspfv3IfAuthKeyStopGenerate':fsMIOspfv3IfAuthKeyStopGenerate,'fsMIOspfv3IfAuthKeyStopAccept':fsMIOspfv3IfAuthKeyStopAccept,'fsMIOspfv3IfAuthKeyStatus':fsMIOspfv3IfAuthKeyStatus,'fsMIOspfv3VirtIfAuthTable':fsMIOspfv3VirtIfAuthTable,'fsMIOspfv3VirtIfAuthEntry':fsMIOspfv3VirtIfAuthEntry,_AB:fsMIOspfv3VirtIfAuthAreaId,_AC:fsMIOspfv3VirtIfAuthNeighbor,_AD:fsMIOspfv3VirtIfAuthKeyId,'fsMIOspfv3VirtIfAuthKey':fsMIOspfv3VirtIfAuthKey,'fsMIOspfv3VirtIfAuthKeyStartAccept':fsMIOspfv3VirtIfAuthKeyStartAccept,'fsMIOspfv3VirtIfAuthKeyStartGenerate':fsMIOspfv3VirtIfAuthKeyStartGenerate,'fsMIOspfv3VirtIfAuthKeyStopGenerate':fsMIOspfv3VirtIfAuthKeyStopGenerate,'fsMIOspfv3VirtIfAuthKeyStopAccept':fsMIOspfv3VirtIfAuthKeyStopAccept,'fsMIOspfv3VirtIfAuthKeyStatus':fsMIOspfv3VirtIfAuthKeyStatus,'fsMIOspfv3VirtIfCryptoAuthTable':fsMIOspfv3VirtIfCryptoAuthTable,_AI:fsMIOspfv3VirtIfCryptoAuthEntry,'fsMIOspfv3VirtIfCryptoAuthType':fsMIOspfv3VirtIfCryptoAuthType,'fsMIOspfv3VirtIfCryptoAuthMode':fsMIOspfv3VirtIfCryptoAuthMode,'fsMIOspfv3Notification':fsMIOspfv3Notification,'fsMIOspfv3Traps':fsMIOspfv3Traps,'fsMIOspfv3RestartStatusChange':fsMIOspfv3RestartStatusChange,'fsMIOspfv3NbrRestartHelperStatusChange':fsMIOspfv3NbrRestartHelperStatusChange,'fsMIOspfv3VirtNbrRestartHelperStatusChange':fsMIOspfv3VirtNbrRestartHelperStatusChange,'fsMIOspfv3HotStandbyStateChgTrap':fsMIOspfv3HotStandbyStateChgTrap,'fsMIOspfv3HotStandbyBulkUpdAbortTrap':fsMIOspfv3HotStandbyBulkUpdAbortTrap,'fsMIOspfv3AuthSequenceNumWrap':fsMIOspfv3AuthSequenceNumWrap,'fsMIOspfv3TrapObject':fsMIOspfv3TrapObject,_AJ:fsMIOspfv3TrapNbrIfIndex,_AM:fsMIOspfv3TrapVirtNbrRtrId,_AK:fsMIOspfv3TrapNbrRtrId,_AL:fsMIOspfv3TrapVirtNbrArea,_AP:fsMIOspfv3TrapBulkUpdAbortReason})