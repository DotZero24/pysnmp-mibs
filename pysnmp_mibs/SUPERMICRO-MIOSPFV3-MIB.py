_AC='fsMIOspfv3TrapBulkUpdAbortReason'
_AB='fsMIOspfv3DynamicBulkUpdStatus'
_AA='fsMIOspfv3HotStandbyState'
_A9='fsMIOspfv3TrapVirtNbrRtrId'
_A8='fsMIOspfv3TrapVirtNbrArea'
_A7='fsMIOspfv3TrapNbrRtrId'
_A6='fsMIOspfv3TrapNbrIfIndex'
_A5='fsMIOspfv3PreferenceEntry'
_A4='fsMIOspfv3RRDRouteEntry'
_A3='fsMIOspfv3Entry'
_A2='fsMIOspfv3DistInOutRouteMapType'
_A1='fsMIOspfv3DistInOutRouteMapName'
_A0='fsMIOspfv3RedistRoutePfxLength'
_z='fsMIOspfv3RedistRouteDest'
_y='fsMIOspfv3RedistRouteDestType'
_x='fsMIOspfv3BRRouteDestType'
_w='fsMIOspfv3BRRouteNextHop'
_v='fsMIOspfv3BRRouteNextHopType'
_u='fsMIOspfv3BRRouteDest'
_t='fsMIOspfv3AsExternalAggregationAreaId'
_s='fsMIOspfv3AsExternalAggregationPfxLength'
_r='fsMIOspfv3AsExternalAggregationNet'
_q='fsMIOspfv3AsExternalAggregationNetType'
_p='type2External'
_o='type1External'
_n='interArea'
_m='intraArea'
_l='fsMIOspfv3RouteNextHop'
_k='fsMIOspfv3RouteNextHopType'
_j='fsMIOspfv3RoutePfxLength'
_i='fsMIOspfv3RouteDest'
_h='fsMIOspfv3RouteDestType'
_g='fsMIOspfv3IfIndex'
_f='switchToRedundant'
_e='swReloadUpgrade'
_d='softwareRestart'
_c='unknown'
_b='fsMIStdOspfv3VirtNbrRestartHelperStatus'
_a='fsMIStdOspfv3VirtNbrRestartHelperExitReason'
_Z='fsMIStdOspfv3VirtNbrRestartHelperAge'
_Y='fsMIStdOspfv3RestartStatus'
_X='fsMIStdOspfv3RestartInterval'
_W='fsMIStdOspfv3RestartExitReason'
_V='fsMIStdOspfv3NbrRestartHelperStatus'
_U='fsMIStdOspfv3NbrRestartHelperExitReason'
_T='fsMIStdOspfv3NbrRestartHelperAge'
_S='DisplayString'
_R='Status'
_Q='BigMetric'
_P='OctetString'
_O='read-create'
_N='disabled'
_M='enabled'
_L='accessible-for-notify'
_K='fsMIStdOspfv3RouterId'
_J='fsMIStdOspfv3ContextId'
_I='TruthValue'
_H='InetAddress'
_G='not-accessible'
_F='SUPERMICRO-MISTDOSPFV3-MIB'
_E='SUPERMICRO-MIOSPFV3-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressPrefixLength','InetAddressType')
AreaID,BigMetric,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB','AreaID',_Q,'RouterID',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_S,'PhysAddress','RowStatus','TextualConvention',_I)
fsMIStdOspfv3ContextId,fsMIStdOspfv3Entry,fsMIStdOspfv3NbrRestartHelperAge,fsMIStdOspfv3NbrRestartHelperExitReason,fsMIStdOspfv3NbrRestartHelperStatus,fsMIStdOspfv3RestartExitReason,fsMIStdOspfv3RestartInterval,fsMIStdOspfv3RestartStatus,fsMIStdOspfv3RouterId,fsMIStdOspfv3VirtNbrRestartHelperAge,fsMIStdOspfv3VirtNbrRestartHelperExitReason,fsMIStdOspfv3VirtNbrRestartHelperStatus=mibBuilder.importSymbols(_F,_J,'fsMIStdOspfv3Entry',_T,_U,_V,_W,_X,_Y,_K,_Z,_a,_b)
fsMIOspfv3=ModuleIdentity((1,3,6,1,4,1,10876,101,2,24))
if mibBuilder.loadTexts:fsMIOspfv3.setRevisions(('2012-09-05 00:00',))
_FsMIOspfv3GeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3GeneralGroup=_FsMIOspfv3GeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,1))
_FsMIOspfv3GlobalTraceLevel_Type=Integer32
_FsMIOspfv3GlobalTraceLevel_Object=MibScalar
fsMIOspfv3GlobalTraceLevel=_FsMIOspfv3GlobalTraceLevel_Object((1,3,6,1,4,1,10876,101,2,24,1,1),_FsMIOspfv3GlobalTraceLevel_Type())
fsMIOspfv3GlobalTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3GlobalTraceLevel.setStatus(_A)
class _FsMIOspfv3VrfSpfInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_FsMIOspfv3VrfSpfInterval_Type.__name__=_C
_FsMIOspfv3VrfSpfInterval_Object=MibScalar
fsMIOspfv3VrfSpfInterval=_FsMIOspfv3VrfSpfInterval_Object((1,3,6,1,4,1,10876,101,2,24,1,2),_FsMIOspfv3VrfSpfInterval_Type())
fsMIOspfv3VrfSpfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3VrfSpfInterval.setStatus(_A)
class _FsMIOspfv3RTStaggeringStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsMIOspfv3RTStaggeringStatus_Type.__name__=_C
_FsMIOspfv3RTStaggeringStatus_Object=MibScalar
fsMIOspfv3RTStaggeringStatus=_FsMIOspfv3RTStaggeringStatus_Object((1,3,6,1,4,1,10876,101,2,24,1,3),_FsMIOspfv3RTStaggeringStatus_Type())
fsMIOspfv3RTStaggeringStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RTStaggeringStatus.setStatus(_A)
class _FsMIOspfv3HotStandbyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIOspfv3HotStandbyAdminStatus_Type.__name__=_C
_FsMIOspfv3HotStandbyAdminStatus_Object=MibScalar
fsMIOspfv3HotStandbyAdminStatus=_FsMIOspfv3HotStandbyAdminStatus_Object((1,3,6,1,4,1,10876,101,2,24,1,4),_FsMIOspfv3HotStandbyAdminStatus_Type())
fsMIOspfv3HotStandbyAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyAdminStatus.setStatus(_A)
class _FsMIOspfv3HotStandbyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FsMIOspfv3HotStandbyState_Type.__name__=_C
_FsMIOspfv3HotStandbyState_Object=MibScalar
fsMIOspfv3HotStandbyState=_FsMIOspfv3HotStandbyState_Object((1,3,6,1,4,1,10876,101,2,24,1,5),_FsMIOspfv3HotStandbyState_Type())
fsMIOspfv3HotStandbyState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyState.setStatus(_A)
class _FsMIOspfv3DynamicBulkUpdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('completed',3),('aborted',4)))
_FsMIOspfv3DynamicBulkUpdStatus_Type.__name__=_C
_FsMIOspfv3DynamicBulkUpdStatus_Object=MibScalar
fsMIOspfv3DynamicBulkUpdStatus=_FsMIOspfv3DynamicBulkUpdStatus_Object((1,3,6,1,4,1,10876,101,2,24,1,6),_FsMIOspfv3DynamicBulkUpdStatus_Type())
fsMIOspfv3DynamicBulkUpdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3DynamicBulkUpdStatus.setStatus(_A)
_FsMIOspfv3StandbyHelloSyncCount_Type=Counter32
_FsMIOspfv3StandbyHelloSyncCount_Object=MibScalar
fsMIOspfv3StandbyHelloSyncCount=_FsMIOspfv3StandbyHelloSyncCount_Object((1,3,6,1,4,1,10876,101,2,24,1,7),_FsMIOspfv3StandbyHelloSyncCount_Type())
fsMIOspfv3StandbyHelloSyncCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3StandbyHelloSyncCount.setStatus(_A)
_FsMIOspfv3StandbyLsaSyncCount_Type=Counter32
_FsMIOspfv3StandbyLsaSyncCount_Object=MibScalar
fsMIOspfv3StandbyLsaSyncCount=_FsMIOspfv3StandbyLsaSyncCount_Object((1,3,6,1,4,1,10876,101,2,24,1,8),_FsMIOspfv3StandbyLsaSyncCount_Type())
fsMIOspfv3StandbyLsaSyncCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3StandbyLsaSyncCount.setStatus(_A)
_FsMIOspfv3Table_Object=MibTable
fsMIOspfv3Table=_FsMIOspfv3Table_Object((1,3,6,1,4,1,10876,101,2,24,2))
if mibBuilder.loadTexts:fsMIOspfv3Table.setStatus(_A)
_FsMIOspfv3Entry_Object=MibTableRow
fsMIOspfv3Entry=_FsMIOspfv3Entry_Object((1,3,6,1,4,1,10876,101,2,24,2,1))
if mibBuilder.loadTexts:fsMIOspfv3Entry.setStatus(_A)
class _FsMIOspfv3OverFlowState_Type(TruthValue):defaultValue=2
_FsMIOspfv3OverFlowState_Type.__name__=_I
_FsMIOspfv3OverFlowState_Object=MibTableColumn
fsMIOspfv3OverFlowState=_FsMIOspfv3OverFlowState_Object((1,3,6,1,4,1,10876,101,2,24,2,1,1),_FsMIOspfv3OverFlowState_Type())
fsMIOspfv3OverFlowState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3OverFlowState.setStatus(_A)
class _FsMIOspfv3TraceLevel_Type(Integer32):defaultValue=2048
_FsMIOspfv3TraceLevel_Type.__name__=_C
_FsMIOspfv3TraceLevel_Object=MibTableColumn
fsMIOspfv3TraceLevel=_FsMIOspfv3TraceLevel_Object((1,3,6,1,4,1,10876,101,2,24,2,1,2),_FsMIOspfv3TraceLevel_Type())
fsMIOspfv3TraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3TraceLevel.setStatus(_A)
class _FsMIOspfv3ABRType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardABR',1),('ciscoABR',2),('ibmABR',3)))
_FsMIOspfv3ABRType_Type.__name__=_C
_FsMIOspfv3ABRType_Object=MibTableColumn
fsMIOspfv3ABRType=_FsMIOspfv3ABRType_Object((1,3,6,1,4,1,10876,101,2,24,2,1,3),_FsMIOspfv3ABRType_Type())
fsMIOspfv3ABRType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3ABRType.setStatus(_A)
class _FsMIOspfv3NssaAsbrDefRtTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIOspfv3NssaAsbrDefRtTrans_Type.__name__=_C
_FsMIOspfv3NssaAsbrDefRtTrans_Object=MibTableColumn
fsMIOspfv3NssaAsbrDefRtTrans=_FsMIOspfv3NssaAsbrDefRtTrans_Object((1,3,6,1,4,1,10876,101,2,24,2,1,4),_FsMIOspfv3NssaAsbrDefRtTrans_Type())
fsMIOspfv3NssaAsbrDefRtTrans.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3NssaAsbrDefRtTrans.setStatus(_A)
class _FsMIOspfv3DefaultPassiveInterface_Type(TruthValue):defaultValue=2
_FsMIOspfv3DefaultPassiveInterface_Type.__name__=_I
_FsMIOspfv3DefaultPassiveInterface_Object=MibTableColumn
fsMIOspfv3DefaultPassiveInterface=_FsMIOspfv3DefaultPassiveInterface_Object((1,3,6,1,4,1,10876,101,2,24,2,1,5),_FsMIOspfv3DefaultPassiveInterface_Type())
fsMIOspfv3DefaultPassiveInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3DefaultPassiveInterface.setStatus(_A)
class _FsMIOspfv3SpfDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3SpfDelay_Type.__name__=_C
_FsMIOspfv3SpfDelay_Object=MibTableColumn
fsMIOspfv3SpfDelay=_FsMIOspfv3SpfDelay_Object((1,3,6,1,4,1,10876,101,2,24,2,1,6),_FsMIOspfv3SpfDelay_Type())
fsMIOspfv3SpfDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3SpfDelay.setStatus(_A)
class _FsMIOspfv3SpfHoldTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfv3SpfHoldTime_Type.__name__=_C
_FsMIOspfv3SpfHoldTime_Object=MibTableColumn
fsMIOspfv3SpfHoldTime=_FsMIOspfv3SpfHoldTime_Object((1,3,6,1,4,1,10876,101,2,24,2,1,7),_FsMIOspfv3SpfHoldTime_Type())
fsMIOspfv3SpfHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3SpfHoldTime.setStatus(_A)
class _FsMIOspfv3RTStaggeringInterval_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,2147483647))
_FsMIOspfv3RTStaggeringInterval_Type.__name__=_C
_FsMIOspfv3RTStaggeringInterval_Object=MibTableColumn
fsMIOspfv3RTStaggeringInterval=_FsMIOspfv3RTStaggeringInterval_Object((1,3,6,1,4,1,10876,101,2,24,2,1,8),_FsMIOspfv3RTStaggeringInterval_Type())
fsMIOspfv3RTStaggeringInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RTStaggeringInterval.setStatus(_A)
class _FsMIOspfv3RestartStrictLsaChecking_Type(TruthValue):defaultValue=2
_FsMIOspfv3RestartStrictLsaChecking_Type.__name__=_I
_FsMIOspfv3RestartStrictLsaChecking_Object=MibTableColumn
fsMIOspfv3RestartStrictLsaChecking=_FsMIOspfv3RestartStrictLsaChecking_Object((1,3,6,1,4,1,10876,101,2,24,2,1,9),_FsMIOspfv3RestartStrictLsaChecking_Type())
fsMIOspfv3RestartStrictLsaChecking.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RestartStrictLsaChecking.setStatus(_A)
class _FsMIOspfv3HelperSupport_Type(Bits):namedValues=NamedValues(*((_c,0),(_d,1),(_e,2),(_f,3)))
_FsMIOspfv3HelperSupport_Type.__name__='Bits'
_FsMIOspfv3HelperSupport_Object=MibTableColumn
fsMIOspfv3HelperSupport=_FsMIOspfv3HelperSupport_Object((1,3,6,1,4,1,10876,101,2,24,2,1,10),_FsMIOspfv3HelperSupport_Type())
fsMIOspfv3HelperSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3HelperSupport.setStatus(_A)
class _FsMIOspfv3HelperGraceTimeLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_FsMIOspfv3HelperGraceTimeLimit_Type.__name__=_C
_FsMIOspfv3HelperGraceTimeLimit_Object=MibTableColumn
fsMIOspfv3HelperGraceTimeLimit=_FsMIOspfv3HelperGraceTimeLimit_Object((1,3,6,1,4,1,10876,101,2,24,2,1,11),_FsMIOspfv3HelperGraceTimeLimit_Type())
fsMIOspfv3HelperGraceTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3HelperGraceTimeLimit.setStatus(_A)
class _FsMIOspfv3RestartAckState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIOspfv3RestartAckState_Type.__name__=_C
_FsMIOspfv3RestartAckState_Object=MibTableColumn
fsMIOspfv3RestartAckState=_FsMIOspfv3RestartAckState_Object((1,3,6,1,4,1,10876,101,2,24,2,1,12),_FsMIOspfv3RestartAckState_Type())
fsMIOspfv3RestartAckState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RestartAckState.setStatus(_A)
class _FsMIOspfv3GraceLsaRetransmitCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FsMIOspfv3GraceLsaRetransmitCount_Type.__name__=_C
_FsMIOspfv3GraceLsaRetransmitCount_Object=MibTableColumn
fsMIOspfv3GraceLsaRetransmitCount=_FsMIOspfv3GraceLsaRetransmitCount_Object((1,3,6,1,4,1,10876,101,2,24,2,1,13),_FsMIOspfv3GraceLsaRetransmitCount_Type())
fsMIOspfv3GraceLsaRetransmitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3GraceLsaRetransmitCount.setStatus(_A)
class _FsMIOspfv3RestartReason_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_c,0),(_d,1),(_e,2),(_f,3)))
_FsMIOspfv3RestartReason_Type.__name__=_C
_FsMIOspfv3RestartReason_Object=MibTableColumn
fsMIOspfv3RestartReason=_FsMIOspfv3RestartReason_Object((1,3,6,1,4,1,10876,101,2,24,2,1,14),_FsMIOspfv3RestartReason_Type())
fsMIOspfv3RestartReason.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RestartReason.setStatus(_A)
_FsMIOspfv3ExtTraceLevel_Type=Integer32
_FsMIOspfv3ExtTraceLevel_Object=MibTableColumn
fsMIOspfv3ExtTraceLevel=_FsMIOspfv3ExtTraceLevel_Object((1,3,6,1,4,1,10876,101,2,24,2,1,15),_FsMIOspfv3ExtTraceLevel_Type())
fsMIOspfv3ExtTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3ExtTraceLevel.setStatus(_A)
_FsMIOspfv3SetTraps_Type=Integer32
_FsMIOspfv3SetTraps_Object=MibTableColumn
fsMIOspfv3SetTraps=_FsMIOspfv3SetTraps_Object((1,3,6,1,4,1,10876,101,2,24,2,1,16),_FsMIOspfv3SetTraps_Type())
fsMIOspfv3SetTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3SetTraps.setStatus(_A)
_FsMIOspfv3IfTable_Object=MibTable
fsMIOspfv3IfTable=_FsMIOspfv3IfTable_Object((1,3,6,1,4,1,10876,101,2,24,3))
if mibBuilder.loadTexts:fsMIOspfv3IfTable.setStatus(_A)
_FsMIOspfv3IfEntry_Object=MibTableRow
fsMIOspfv3IfEntry=_FsMIOspfv3IfEntry_Object((1,3,6,1,4,1,10876,101,2,24,3,1))
fsMIOspfv3IfEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:fsMIOspfv3IfEntry.setStatus(_A)
_FsMIOspfv3IfIndex_Type=InterfaceIndex
_FsMIOspfv3IfIndex_Object=MibTableColumn
fsMIOspfv3IfIndex=_FsMIOspfv3IfIndex_Object((1,3,6,1,4,1,10876,101,2,24,3,1,1),_FsMIOspfv3IfIndex_Type())
fsMIOspfv3IfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3IfIndex.setStatus(_A)
class _FsMIOspfv3IfOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operup',1),('operdown',2),('loopback',3),('unloop',4)))
_FsMIOspfv3IfOperState_Type.__name__=_C
_FsMIOspfv3IfOperState_Object=MibTableColumn
fsMIOspfv3IfOperState=_FsMIOspfv3IfOperState_Object((1,3,6,1,4,1,10876,101,2,24,3,1,2),_FsMIOspfv3IfOperState_Type())
fsMIOspfv3IfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfOperState.setStatus(_A)
class _FsMIOspfv3IfPassive_Type(TruthValue):defaultValue=2
_FsMIOspfv3IfPassive_Type.__name__=_I
_FsMIOspfv3IfPassive_Object=MibTableColumn
fsMIOspfv3IfPassive=_FsMIOspfv3IfPassive_Object((1,3,6,1,4,1,10876,101,2,24,3,1,3),_FsMIOspfv3IfPassive_Type())
fsMIOspfv3IfPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfPassive.setStatus(_A)
_FsMIOspfv3IfNbrCount_Type=Gauge32
_FsMIOspfv3IfNbrCount_Object=MibTableColumn
fsMIOspfv3IfNbrCount=_FsMIOspfv3IfNbrCount_Object((1,3,6,1,4,1,10876,101,2,24,3,1,4),_FsMIOspfv3IfNbrCount_Type())
fsMIOspfv3IfNbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfNbrCount.setStatus(_A)
_FsMIOspfv3IfAdjCount_Type=Gauge32
_FsMIOspfv3IfAdjCount_Object=MibTableColumn
fsMIOspfv3IfAdjCount=_FsMIOspfv3IfAdjCount_Object((1,3,6,1,4,1,10876,101,2,24,3,1,5),_FsMIOspfv3IfAdjCount_Type())
fsMIOspfv3IfAdjCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfAdjCount.setStatus(_A)
_FsMIOspfv3IfHelloRcvd_Type=Counter32
_FsMIOspfv3IfHelloRcvd_Object=MibTableColumn
fsMIOspfv3IfHelloRcvd=_FsMIOspfv3IfHelloRcvd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,6),_FsMIOspfv3IfHelloRcvd_Type())
fsMIOspfv3IfHelloRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfHelloRcvd.setStatus(_A)
_FsMIOspfv3IfHelloTxed_Type=Counter32
_FsMIOspfv3IfHelloTxed_Object=MibTableColumn
fsMIOspfv3IfHelloTxed=_FsMIOspfv3IfHelloTxed_Object((1,3,6,1,4,1,10876,101,2,24,3,1,7),_FsMIOspfv3IfHelloTxed_Type())
fsMIOspfv3IfHelloTxed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfHelloTxed.setStatus(_A)
_FsMIOspfv3IfHelloDisd_Type=Counter32
_FsMIOspfv3IfHelloDisd_Object=MibTableColumn
fsMIOspfv3IfHelloDisd=_FsMIOspfv3IfHelloDisd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,8),_FsMIOspfv3IfHelloDisd_Type())
fsMIOspfv3IfHelloDisd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfHelloDisd.setStatus(_A)
_FsMIOspfv3IfDdpRcvd_Type=Counter32
_FsMIOspfv3IfDdpRcvd_Object=MibTableColumn
fsMIOspfv3IfDdpRcvd=_FsMIOspfv3IfDdpRcvd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,9),_FsMIOspfv3IfDdpRcvd_Type())
fsMIOspfv3IfDdpRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfDdpRcvd.setStatus(_A)
_FsMIOspfv3IfDdpTxed_Type=Counter32
_FsMIOspfv3IfDdpTxed_Object=MibTableColumn
fsMIOspfv3IfDdpTxed=_FsMIOspfv3IfDdpTxed_Object((1,3,6,1,4,1,10876,101,2,24,3,1,10),_FsMIOspfv3IfDdpTxed_Type())
fsMIOspfv3IfDdpTxed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfDdpTxed.setStatus(_A)
_FsMIOspfv3IfDdpDisd_Type=Counter32
_FsMIOspfv3IfDdpDisd_Object=MibTableColumn
fsMIOspfv3IfDdpDisd=_FsMIOspfv3IfDdpDisd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,11),_FsMIOspfv3IfDdpDisd_Type())
fsMIOspfv3IfDdpDisd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfDdpDisd.setStatus(_A)
_FsMIOspfv3IfLrqRcvd_Type=Counter32
_FsMIOspfv3IfLrqRcvd_Object=MibTableColumn
fsMIOspfv3IfLrqRcvd=_FsMIOspfv3IfLrqRcvd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,12),_FsMIOspfv3IfLrqRcvd_Type())
fsMIOspfv3IfLrqRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLrqRcvd.setStatus(_A)
_FsMIOspfv3IfLrqTxed_Type=Counter32
_FsMIOspfv3IfLrqTxed_Object=MibTableColumn
fsMIOspfv3IfLrqTxed=_FsMIOspfv3IfLrqTxed_Object((1,3,6,1,4,1,10876,101,2,24,3,1,13),_FsMIOspfv3IfLrqTxed_Type())
fsMIOspfv3IfLrqTxed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLrqTxed.setStatus(_A)
_FsMIOspfv3IfLrqDisd_Type=Counter32
_FsMIOspfv3IfLrqDisd_Object=MibTableColumn
fsMIOspfv3IfLrqDisd=_FsMIOspfv3IfLrqDisd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,14),_FsMIOspfv3IfLrqDisd_Type())
fsMIOspfv3IfLrqDisd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLrqDisd.setStatus(_A)
_FsMIOspfv3IfLsuRcvd_Type=Counter32
_FsMIOspfv3IfLsuRcvd_Object=MibTableColumn
fsMIOspfv3IfLsuRcvd=_FsMIOspfv3IfLsuRcvd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,15),_FsMIOspfv3IfLsuRcvd_Type())
fsMIOspfv3IfLsuRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLsuRcvd.setStatus(_A)
_FsMIOspfv3IfLsuTxed_Type=Counter32
_FsMIOspfv3IfLsuTxed_Object=MibTableColumn
fsMIOspfv3IfLsuTxed=_FsMIOspfv3IfLsuTxed_Object((1,3,6,1,4,1,10876,101,2,24,3,1,16),_FsMIOspfv3IfLsuTxed_Type())
fsMIOspfv3IfLsuTxed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLsuTxed.setStatus(_A)
_FsMIOspfv3IfLsuDisd_Type=Counter32
_FsMIOspfv3IfLsuDisd_Object=MibTableColumn
fsMIOspfv3IfLsuDisd=_FsMIOspfv3IfLsuDisd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,17),_FsMIOspfv3IfLsuDisd_Type())
fsMIOspfv3IfLsuDisd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLsuDisd.setStatus(_A)
_FsMIOspfv3IfLakRcvd_Type=Counter32
_FsMIOspfv3IfLakRcvd_Object=MibTableColumn
fsMIOspfv3IfLakRcvd=_FsMIOspfv3IfLakRcvd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,18),_FsMIOspfv3IfLakRcvd_Type())
fsMIOspfv3IfLakRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLakRcvd.setStatus(_A)
_FsMIOspfv3IfLakTxed_Type=Counter32
_FsMIOspfv3IfLakTxed_Object=MibTableColumn
fsMIOspfv3IfLakTxed=_FsMIOspfv3IfLakTxed_Object((1,3,6,1,4,1,10876,101,2,24,3,1,19),_FsMIOspfv3IfLakTxed_Type())
fsMIOspfv3IfLakTxed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLakTxed.setStatus(_A)
_FsMIOspfv3IfLakDisd_Type=Counter32
_FsMIOspfv3IfLakDisd_Object=MibTableColumn
fsMIOspfv3IfLakDisd=_FsMIOspfv3IfLakDisd_Object((1,3,6,1,4,1,10876,101,2,24,3,1,20),_FsMIOspfv3IfLakDisd_Type())
fsMIOspfv3IfLakDisd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfLakDisd.setStatus(_A)
_FsMIOspfv3IfContextId_Type=Integer32
_FsMIOspfv3IfContextId_Object=MibTableColumn
fsMIOspfv3IfContextId=_FsMIOspfv3IfContextId_Object((1,3,6,1,4,1,10876,101,2,24,3,1,21),_FsMIOspfv3IfContextId_Type())
fsMIOspfv3IfContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3IfContextId.setStatus(_A)
class _FsMIOspfv3IfLinkLSASuppression_Type(TruthValue):defaultValue=2
_FsMIOspfv3IfLinkLSASuppression_Type.__name__=_I
_FsMIOspfv3IfLinkLSASuppression_Object=MibTableColumn
fsMIOspfv3IfLinkLSASuppression=_FsMIOspfv3IfLinkLSASuppression_Object((1,3,6,1,4,1,10876,101,2,24,3,1,22),_FsMIOspfv3IfLinkLSASuppression_Type())
fsMIOspfv3IfLinkLSASuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3IfLinkLSASuppression.setStatus(_A)
_FsMIOspfv3RoutingTable_Object=MibTable
fsMIOspfv3RoutingTable=_FsMIOspfv3RoutingTable_Object((1,3,6,1,4,1,10876,101,2,24,4))
if mibBuilder.loadTexts:fsMIOspfv3RoutingTable.setStatus(_A)
_FsMIOspfv3RoutingEntry_Object=MibTableRow
fsMIOspfv3RoutingEntry=_FsMIOspfv3RoutingEntry_Object((1,3,6,1,4,1,10876,101,2,24,4,1))
fsMIOspfv3RoutingEntry.setIndexNames((0,_F,_J),(0,_E,_h),(0,_E,_i),(0,_E,_j),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:fsMIOspfv3RoutingEntry.setStatus(_A)
_FsMIOspfv3RouteDestType_Type=InetAddressType
_FsMIOspfv3RouteDestType_Object=MibTableColumn
fsMIOspfv3RouteDestType=_FsMIOspfv3RouteDestType_Object((1,3,6,1,4,1,10876,101,2,24,4,1,1),_FsMIOspfv3RouteDestType_Type())
fsMIOspfv3RouteDestType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RouteDestType.setStatus(_A)
class _FsMIOspfv3RouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3RouteDest_Type.__name__=_H
_FsMIOspfv3RouteDest_Object=MibTableColumn
fsMIOspfv3RouteDest=_FsMIOspfv3RouteDest_Object((1,3,6,1,4,1,10876,101,2,24,4,1,2),_FsMIOspfv3RouteDest_Type())
fsMIOspfv3RouteDest.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RouteDest.setStatus(_A)
_FsMIOspfv3RoutePfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3RoutePfxLength_Object=MibTableColumn
fsMIOspfv3RoutePfxLength=_FsMIOspfv3RoutePfxLength_Object((1,3,6,1,4,1,10876,101,2,24,4,1,3),_FsMIOspfv3RoutePfxLength_Type())
fsMIOspfv3RoutePfxLength.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RoutePfxLength.setStatus(_A)
_FsMIOspfv3RouteNextHopType_Type=InetAddressType
_FsMIOspfv3RouteNextHopType_Object=MibTableColumn
fsMIOspfv3RouteNextHopType=_FsMIOspfv3RouteNextHopType_Object((1,3,6,1,4,1,10876,101,2,24,4,1,4),_FsMIOspfv3RouteNextHopType_Type())
fsMIOspfv3RouteNextHopType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RouteNextHopType.setStatus(_A)
class _FsMIOspfv3RouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3RouteNextHop_Type.__name__=_H
_FsMIOspfv3RouteNextHop_Object=MibTableColumn
fsMIOspfv3RouteNextHop=_FsMIOspfv3RouteNextHop_Object((1,3,6,1,4,1,10876,101,2,24,4,1,5),_FsMIOspfv3RouteNextHop_Type())
fsMIOspfv3RouteNextHop.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RouteNextHop.setStatus(_A)
class _FsMIOspfv3RouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_m,1),(_n,2),(_o,3),(_p,4)))
_FsMIOspfv3RouteType_Type.__name__=_C
_FsMIOspfv3RouteType_Object=MibTableColumn
fsMIOspfv3RouteType=_FsMIOspfv3RouteType_Object((1,3,6,1,4,1,10876,101,2,24,4,1,6),_FsMIOspfv3RouteType_Type())
fsMIOspfv3RouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RouteType.setStatus(_A)
_FsMIOspfv3RouteAreaId_Type=AreaID
_FsMIOspfv3RouteAreaId_Object=MibTableColumn
fsMIOspfv3RouteAreaId=_FsMIOspfv3RouteAreaId_Object((1,3,6,1,4,1,10876,101,2,24,4,1,7),_FsMIOspfv3RouteAreaId_Type())
fsMIOspfv3RouteAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RouteAreaId.setStatus(_A)
_FsMIOspfv3RouteCost_Type=BigMetric
_FsMIOspfv3RouteCost_Object=MibTableColumn
fsMIOspfv3RouteCost=_FsMIOspfv3RouteCost_Object((1,3,6,1,4,1,10876,101,2,24,4,1,8),_FsMIOspfv3RouteCost_Type())
fsMIOspfv3RouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RouteCost.setStatus(_A)
_FsMIOspfv3RouteType2Cost_Type=BigMetric
_FsMIOspfv3RouteType2Cost_Object=MibTableColumn
fsMIOspfv3RouteType2Cost=_FsMIOspfv3RouteType2Cost_Object((1,3,6,1,4,1,10876,101,2,24,4,1,9),_FsMIOspfv3RouteType2Cost_Type())
fsMIOspfv3RouteType2Cost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RouteType2Cost.setStatus(_A)
class _FsMIOspfv3RouteInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIOspfv3RouteInterfaceIndex_Type.__name__=_C
_FsMIOspfv3RouteInterfaceIndex_Object=MibTableColumn
fsMIOspfv3RouteInterfaceIndex=_FsMIOspfv3RouteInterfaceIndex_Object((1,3,6,1,4,1,10876,101,2,24,4,1,10),_FsMIOspfv3RouteInterfaceIndex_Type())
fsMIOspfv3RouteInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3RouteInterfaceIndex.setStatus(_A)
_FsMIOspfv3AsExternalAggregationTable_Object=MibTable
fsMIOspfv3AsExternalAggregationTable=_FsMIOspfv3AsExternalAggregationTable_Object((1,3,6,1,4,1,10876,101,2,24,5))
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationTable.setStatus(_A)
_FsMIOspfv3AsExternalAggregationEntry_Object=MibTableRow
fsMIOspfv3AsExternalAggregationEntry=_FsMIOspfv3AsExternalAggregationEntry_Object((1,3,6,1,4,1,10876,101,2,24,5,1))
fsMIOspfv3AsExternalAggregationEntry.setIndexNames((0,_F,_J),(0,_E,_q),(0,_E,_r),(0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationEntry.setStatus(_A)
_FsMIOspfv3AsExternalAggregationNetType_Type=InetAddressType
_FsMIOspfv3AsExternalAggregationNetType_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationNetType=_FsMIOspfv3AsExternalAggregationNetType_Object((1,3,6,1,4,1,10876,101,2,24,5,1,1),_FsMIOspfv3AsExternalAggregationNetType_Type())
fsMIOspfv3AsExternalAggregationNetType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationNetType.setStatus(_A)
class _FsMIOspfv3AsExternalAggregationNet_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3AsExternalAggregationNet_Type.__name__=_H
_FsMIOspfv3AsExternalAggregationNet_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationNet=_FsMIOspfv3AsExternalAggregationNet_Object((1,3,6,1,4,1,10876,101,2,24,5,1,2),_FsMIOspfv3AsExternalAggregationNet_Type())
fsMIOspfv3AsExternalAggregationNet.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationNet.setStatus(_A)
_FsMIOspfv3AsExternalAggregationPfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3AsExternalAggregationPfxLength_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationPfxLength=_FsMIOspfv3AsExternalAggregationPfxLength_Object((1,3,6,1,4,1,10876,101,2,24,5,1,3),_FsMIOspfv3AsExternalAggregationPfxLength_Type())
fsMIOspfv3AsExternalAggregationPfxLength.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationPfxLength.setStatus(_A)
_FsMIOspfv3AsExternalAggregationAreaId_Type=AreaID
_FsMIOspfv3AsExternalAggregationAreaId_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationAreaId=_FsMIOspfv3AsExternalAggregationAreaId_Object((1,3,6,1,4,1,10876,101,2,24,5,1,4),_FsMIOspfv3AsExternalAggregationAreaId_Type())
fsMIOspfv3AsExternalAggregationAreaId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationAreaId.setStatus(_A)
class _FsMIOspfv3AsExternalAggregationEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertise',1),('doNotAdvertise',2),('allowAll',3),('denyAll',4)))
_FsMIOspfv3AsExternalAggregationEffect_Type.__name__=_C
_FsMIOspfv3AsExternalAggregationEffect_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationEffect=_FsMIOspfv3AsExternalAggregationEffect_Object((1,3,6,1,4,1,10876,101,2,24,5,1,5),_FsMIOspfv3AsExternalAggregationEffect_Type())
fsMIOspfv3AsExternalAggregationEffect.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationEffect.setStatus(_A)
class _FsMIOspfv3AsExternalAggregationTranslation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIOspfv3AsExternalAggregationTranslation_Type.__name__=_C
_FsMIOspfv3AsExternalAggregationTranslation_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationTranslation=_FsMIOspfv3AsExternalAggregationTranslation_Object((1,3,6,1,4,1,10876,101,2,24,5,1,6),_FsMIOspfv3AsExternalAggregationTranslation_Type())
fsMIOspfv3AsExternalAggregationTranslation.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationTranslation.setStatus(_A)
_FsMIOspfv3AsExternalAggregationStatus_Type=RowStatus
_FsMIOspfv3AsExternalAggregationStatus_Object=MibTableColumn
fsMIOspfv3AsExternalAggregationStatus=_FsMIOspfv3AsExternalAggregationStatus_Object((1,3,6,1,4,1,10876,101,2,24,5,1,7),_FsMIOspfv3AsExternalAggregationStatus_Type())
fsMIOspfv3AsExternalAggregationStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3AsExternalAggregationStatus.setStatus(_A)
_FsMIOspfv3BRRouteTable_Object=MibTable
fsMIOspfv3BRRouteTable=_FsMIOspfv3BRRouteTable_Object((1,3,6,1,4,1,10876,101,2,24,6))
if mibBuilder.loadTexts:fsMIOspfv3BRRouteTable.setStatus(_A)
_FsMIOspfv3BRRouteEntry_Object=MibTableRow
fsMIOspfv3BRRouteEntry=_FsMIOspfv3BRRouteEntry_Object((1,3,6,1,4,1,10876,101,2,24,6,1))
fsMIOspfv3BRRouteEntry.setIndexNames((0,_F,_J),(0,_E,_u),(0,_E,_v),(0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:fsMIOspfv3BRRouteEntry.setStatus(_A)
_FsMIOspfv3BRRouteDest_Type=IpAddress
_FsMIOspfv3BRRouteDest_Object=MibTableColumn
fsMIOspfv3BRRouteDest=_FsMIOspfv3BRRouteDest_Object((1,3,6,1,4,1,10876,101,2,24,6,1,1),_FsMIOspfv3BRRouteDest_Type())
fsMIOspfv3BRRouteDest.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteDest.setStatus(_A)
_FsMIOspfv3BRRouteNextHopType_Type=InetAddressType
_FsMIOspfv3BRRouteNextHopType_Object=MibTableColumn
fsMIOspfv3BRRouteNextHopType=_FsMIOspfv3BRRouteNextHopType_Object((1,3,6,1,4,1,10876,101,2,24,6,1,2),_FsMIOspfv3BRRouteNextHopType_Type())
fsMIOspfv3BRRouteNextHopType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteNextHopType.setStatus(_A)
class _FsMIOspfv3BRRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3BRRouteNextHop_Type.__name__=_H
_FsMIOspfv3BRRouteNextHop_Object=MibTableColumn
fsMIOspfv3BRRouteNextHop=_FsMIOspfv3BRRouteNextHop_Object((1,3,6,1,4,1,10876,101,2,24,6,1,3),_FsMIOspfv3BRRouteNextHop_Type())
fsMIOspfv3BRRouteNextHop.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteNextHop.setStatus(_A)
class _FsMIOspfv3BRRouteDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('areaBorder',2),('asBoundary',3)))
_FsMIOspfv3BRRouteDestType_Type.__name__=_C
_FsMIOspfv3BRRouteDestType_Object=MibTableColumn
fsMIOspfv3BRRouteDestType=_FsMIOspfv3BRRouteDestType_Object((1,3,6,1,4,1,10876,101,2,24,6,1,4),_FsMIOspfv3BRRouteDestType_Type())
fsMIOspfv3BRRouteDestType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteDestType.setStatus(_A)
class _FsMIOspfv3BRRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_FsMIOspfv3BRRouteType_Type.__name__=_C
_FsMIOspfv3BRRouteType_Object=MibTableColumn
fsMIOspfv3BRRouteType=_FsMIOspfv3BRRouteType_Object((1,3,6,1,4,1,10876,101,2,24,6,1,5),_FsMIOspfv3BRRouteType_Type())
fsMIOspfv3BRRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteType.setStatus(_A)
_FsMIOspfv3BRRouteAreaId_Type=AreaID
_FsMIOspfv3BRRouteAreaId_Object=MibTableColumn
fsMIOspfv3BRRouteAreaId=_FsMIOspfv3BRRouteAreaId_Object((1,3,6,1,4,1,10876,101,2,24,6,1,6),_FsMIOspfv3BRRouteAreaId_Type())
fsMIOspfv3BRRouteAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteAreaId.setStatus(_A)
_FsMIOspfv3BRRouteCost_Type=BigMetric
_FsMIOspfv3BRRouteCost_Object=MibTableColumn
fsMIOspfv3BRRouteCost=_FsMIOspfv3BRRouteCost_Object((1,3,6,1,4,1,10876,101,2,24,6,1,7),_FsMIOspfv3BRRouteCost_Type())
fsMIOspfv3BRRouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteCost.setStatus(_A)
_FsMIOspfv3BRRouteInterfaceIndex_Type=InterfaceIndex
_FsMIOspfv3BRRouteInterfaceIndex_Object=MibTableColumn
fsMIOspfv3BRRouteInterfaceIndex=_FsMIOspfv3BRRouteInterfaceIndex_Object((1,3,6,1,4,1,10876,101,2,24,6,1,8),_FsMIOspfv3BRRouteInterfaceIndex_Type())
fsMIOspfv3BRRouteInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIOspfv3BRRouteInterfaceIndex.setStatus(_A)
_FsMIOspfv3RedistRouteCfgTable_Object=MibTable
fsMIOspfv3RedistRouteCfgTable=_FsMIOspfv3RedistRouteCfgTable_Object((1,3,6,1,4,1,10876,101,2,24,7))
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteCfgTable.setStatus(_A)
_FsMIOspfv3RedistRouteCfgEntry_Object=MibTableRow
fsMIOspfv3RedistRouteCfgEntry=_FsMIOspfv3RedistRouteCfgEntry_Object((1,3,6,1,4,1,10876,101,2,24,7,1))
fsMIOspfv3RedistRouteCfgEntry.setIndexNames((0,_F,_J),(0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteCfgEntry.setStatus(_A)
_FsMIOspfv3RedistRouteDestType_Type=InetAddressType
_FsMIOspfv3RedistRouteDestType_Object=MibTableColumn
fsMIOspfv3RedistRouteDestType=_FsMIOspfv3RedistRouteDestType_Object((1,3,6,1,4,1,10876,101,2,24,7,1,1),_FsMIOspfv3RedistRouteDestType_Type())
fsMIOspfv3RedistRouteDestType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteDestType.setStatus(_A)
class _FsMIOspfv3RedistRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3RedistRouteDest_Type.__name__=_H
_FsMIOspfv3RedistRouteDest_Object=MibTableColumn
fsMIOspfv3RedistRouteDest=_FsMIOspfv3RedistRouteDest_Object((1,3,6,1,4,1,10876,101,2,24,7,1,2),_FsMIOspfv3RedistRouteDest_Type())
fsMIOspfv3RedistRouteDest.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteDest.setStatus(_A)
_FsMIOspfv3RedistRoutePfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3RedistRoutePfxLength_Object=MibTableColumn
fsMIOspfv3RedistRoutePfxLength=_FsMIOspfv3RedistRoutePfxLength_Object((1,3,6,1,4,1,10876,101,2,24,7,1,3),_FsMIOspfv3RedistRoutePfxLength_Type())
fsMIOspfv3RedistRoutePfxLength.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3RedistRoutePfxLength.setStatus(_A)
class _FsMIOspfv3RedistRouteMetric_Type(BigMetric):defaultValue=10
_FsMIOspfv3RedistRouteMetric_Type.__name__=_Q
_FsMIOspfv3RedistRouteMetric_Object=MibTableColumn
fsMIOspfv3RedistRouteMetric=_FsMIOspfv3RedistRouteMetric_Object((1,3,6,1,4,1,10876,101,2,24,7,1,4),_FsMIOspfv3RedistRouteMetric_Type())
fsMIOspfv3RedistRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteMetric.setStatus(_A)
class _FsMIOspfv3RedistRouteMetricType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_o,3),(_p,4)))
_FsMIOspfv3RedistRouteMetricType_Type.__name__=_C
_FsMIOspfv3RedistRouteMetricType_Object=MibTableColumn
fsMIOspfv3RedistRouteMetricType=_FsMIOspfv3RedistRouteMetricType_Object((1,3,6,1,4,1,10876,101,2,24,7,1,5),_FsMIOspfv3RedistRouteMetricType_Type())
fsMIOspfv3RedistRouteMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteMetricType.setStatus(_A)
class _FsMIOspfv3RedistRouteTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_FsMIOspfv3RedistRouteTagType_Type.__name__=_C
_FsMIOspfv3RedistRouteTagType_Object=MibTableColumn
fsMIOspfv3RedistRouteTagType=_FsMIOspfv3RedistRouteTagType_Object((1,3,6,1,4,1,10876,101,2,24,7,1,6),_FsMIOspfv3RedistRouteTagType_Type())
fsMIOspfv3RedistRouteTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteTagType.setStatus(_A)
class _FsMIOspfv3RedistRouteTag_Type(Integer32):defaultValue=0
_FsMIOspfv3RedistRouteTag_Type.__name__=_C
_FsMIOspfv3RedistRouteTag_Object=MibTableColumn
fsMIOspfv3RedistRouteTag=_FsMIOspfv3RedistRouteTag_Object((1,3,6,1,4,1,10876,101,2,24,7,1,7),_FsMIOspfv3RedistRouteTag_Type())
fsMIOspfv3RedistRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteTag.setStatus(_A)
_FsMIOspfv3RedistRouteStatus_Type=RowStatus
_FsMIOspfv3RedistRouteStatus_Object=MibTableColumn
fsMIOspfv3RedistRouteStatus=_FsMIOspfv3RedistRouteStatus_Object((1,3,6,1,4,1,10876,101,2,24,7,1,8),_FsMIOspfv3RedistRouteStatus_Type())
fsMIOspfv3RedistRouteStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMIOspfv3RedistRouteStatus.setStatus(_A)
_FsMIOspfv3RRDGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3RRDGroup=_FsMIOspfv3RRDGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,8))
_FsMIOspfv3RRDGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3RRDGeneralGroup=_FsMIOspfv3RRDGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,8,1))
_FsMIOspfv3RRDRouteTable_Object=MibTable
fsMIOspfv3RRDRouteTable=_FsMIOspfv3RRDRouteTable_Object((1,3,6,1,4,1,10876,101,2,24,8,1,1))
if mibBuilder.loadTexts:fsMIOspfv3RRDRouteTable.setStatus(_A)
_FsMIOspfv3RRDRouteEntry_Object=MibTableRow
fsMIOspfv3RRDRouteEntry=_FsMIOspfv3RRDRouteEntry_Object((1,3,6,1,4,1,10876,101,2,24,8,1,1,1))
if mibBuilder.loadTexts:fsMIOspfv3RRDRouteEntry.setStatus(_A)
class _FsMIOspfv3RRDStatus_Type(Status):defaultValue=2
_FsMIOspfv3RRDStatus_Type.__name__=_R
_FsMIOspfv3RRDStatus_Object=MibTableColumn
fsMIOspfv3RRDStatus=_FsMIOspfv3RRDStatus_Object((1,3,6,1,4,1,10876,101,2,24,8,1,1,1,1),_FsMIOspfv3RRDStatus_Type())
fsMIOspfv3RRDStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RRDStatus.setStatus(_A)
class _FsMIOspfv3RRDSrcProtoMask_Type(Integer32):defaultValue=0
_FsMIOspfv3RRDSrcProtoMask_Type.__name__=_C
_FsMIOspfv3RRDSrcProtoMask_Object=MibTableColumn
fsMIOspfv3RRDSrcProtoMask=_FsMIOspfv3RRDSrcProtoMask_Object((1,3,6,1,4,1,10876,101,2,24,8,1,1,1,2),_FsMIOspfv3RRDSrcProtoMask_Type())
fsMIOspfv3RRDSrcProtoMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RRDSrcProtoMask.setStatus(_A)
class _FsMIOspfv3RRDRouteMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsMIOspfv3RRDRouteMapName_Type.__name__=_P
_FsMIOspfv3RRDRouteMapName_Object=MibTableColumn
fsMIOspfv3RRDRouteMapName=_FsMIOspfv3RRDRouteMapName_Object((1,3,6,1,4,1,10876,101,2,24,8,1,1,1,3),_FsMIOspfv3RRDRouteMapName_Type())
fsMIOspfv3RRDRouteMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3RRDRouteMapName.setStatus(_A)
_FsMIOspfv3DistInOutRouteMap_ObjectIdentity=ObjectIdentity
fsMIOspfv3DistInOutRouteMap=_FsMIOspfv3DistInOutRouteMap_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,9))
_FsMIOspfv3DistInOutRouteMapTable_Object=MibTable
fsMIOspfv3DistInOutRouteMapTable=_FsMIOspfv3DistInOutRouteMapTable_Object((1,3,6,1,4,1,10876,101,2,24,9,1))
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapTable.setStatus(_A)
_FsMIOspfv3DistInOutRouteMapEntry_Object=MibTableRow
fsMIOspfv3DistInOutRouteMapEntry=_FsMIOspfv3DistInOutRouteMapEntry_Object((1,3,6,1,4,1,10876,101,2,24,9,1,1))
fsMIOspfv3DistInOutRouteMapEntry.setIndexNames((0,_F,_J),(0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapEntry.setStatus(_A)
class _FsMIOspfv3DistInOutRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsMIOspfv3DistInOutRouteMapName_Type.__name__=_S
_FsMIOspfv3DistInOutRouteMapName_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapName=_FsMIOspfv3DistInOutRouteMapName_Object((1,3,6,1,4,1,10876,101,2,24,9,1,1,1),_FsMIOspfv3DistInOutRouteMapName_Type())
fsMIOspfv3DistInOutRouteMapName.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapName.setStatus(_A)
class _FsMIOspfv3DistInOutRouteMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FsMIOspfv3DistInOutRouteMapType_Type.__name__=_C
_FsMIOspfv3DistInOutRouteMapType_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapType=_FsMIOspfv3DistInOutRouteMapType_Object((1,3,6,1,4,1,10876,101,2,24,9,1,1,2),_FsMIOspfv3DistInOutRouteMapType_Type())
fsMIOspfv3DistInOutRouteMapType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapType.setStatus(_A)
class _FsMIOspfv3DistInOutRouteMapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIOspfv3DistInOutRouteMapValue_Type.__name__=_C
_FsMIOspfv3DistInOutRouteMapValue_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapValue=_FsMIOspfv3DistInOutRouteMapValue_Object((1,3,6,1,4,1,10876,101,2,24,9,1,1,3),_FsMIOspfv3DistInOutRouteMapValue_Type())
fsMIOspfv3DistInOutRouteMapValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapValue.setStatus(_A)
_FsMIOspfv3DistInOutRouteMapRowStatus_Type=RowStatus
_FsMIOspfv3DistInOutRouteMapRowStatus_Object=MibTableColumn
fsMIOspfv3DistInOutRouteMapRowStatus=_FsMIOspfv3DistInOutRouteMapRowStatus_Object((1,3,6,1,4,1,10876,101,2,24,9,1,1,4),_FsMIOspfv3DistInOutRouteMapRowStatus_Type())
fsMIOspfv3DistInOutRouteMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3DistInOutRouteMapRowStatus.setStatus(_A)
_FsMIOspfv3PreferenceGroup_ObjectIdentity=ObjectIdentity
fsMIOspfv3PreferenceGroup=_FsMIOspfv3PreferenceGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,10))
_FsMIOspfv3PreferenceTable_Object=MibTable
fsMIOspfv3PreferenceTable=_FsMIOspfv3PreferenceTable_Object((1,3,6,1,4,1,10876,101,2,24,10,1))
if mibBuilder.loadTexts:fsMIOspfv3PreferenceTable.setStatus(_A)
_FsMIOspfv3PreferenceEntry_Object=MibTableRow
fsMIOspfv3PreferenceEntry=_FsMIOspfv3PreferenceEntry_Object((1,3,6,1,4,1,10876,101,2,24,10,1,1))
if mibBuilder.loadTexts:fsMIOspfv3PreferenceEntry.setStatus(_A)
class _FsMIOspfv3PreferenceValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIOspfv3PreferenceValue_Type.__name__=_C
_FsMIOspfv3PreferenceValue_Object=MibTableColumn
fsMIOspfv3PreferenceValue=_FsMIOspfv3PreferenceValue_Object((1,3,6,1,4,1,10876,101,2,24,10,1,1,1),_FsMIOspfv3PreferenceValue_Type())
fsMIOspfv3PreferenceValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfv3PreferenceValue.setStatus(_A)
_FsMIOspfv3Notification_ObjectIdentity=ObjectIdentity
fsMIOspfv3Notification=_FsMIOspfv3Notification_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,101))
_FsMIOspfv3Traps_ObjectIdentity=ObjectIdentity
fsMIOspfv3Traps=_FsMIOspfv3Traps_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,101,0))
_FsMIOspfv3TrapObject_ObjectIdentity=ObjectIdentity
fsMIOspfv3TrapObject=_FsMIOspfv3TrapObject_ObjectIdentity((1,3,6,1,4,1,10876,101,2,24,101,1))
_FsMIOspfv3TrapNbrIfIndex_Type=InterfaceIndex
_FsMIOspfv3TrapNbrIfIndex_Object=MibScalar
fsMIOspfv3TrapNbrIfIndex=_FsMIOspfv3TrapNbrIfIndex_Object((1,3,6,1,4,1,10876,101,2,24,101,1,1),_FsMIOspfv3TrapNbrIfIndex_Type())
fsMIOspfv3TrapNbrIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIOspfv3TrapNbrIfIndex.setStatus(_A)
_FsMIOspfv3TrapVirtNbrRtrId_Type=RouterID
_FsMIOspfv3TrapVirtNbrRtrId_Object=MibScalar
fsMIOspfv3TrapVirtNbrRtrId=_FsMIOspfv3TrapVirtNbrRtrId_Object((1,3,6,1,4,1,10876,101,2,24,101,1,2),_FsMIOspfv3TrapVirtNbrRtrId_Type())
fsMIOspfv3TrapVirtNbrRtrId.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIOspfv3TrapVirtNbrRtrId.setStatus(_A)
_FsMIOspfv3TrapNbrRtrId_Type=RouterID
_FsMIOspfv3TrapNbrRtrId_Object=MibScalar
fsMIOspfv3TrapNbrRtrId=_FsMIOspfv3TrapNbrRtrId_Object((1,3,6,1,4,1,10876,101,2,24,101,1,3),_FsMIOspfv3TrapNbrRtrId_Type())
fsMIOspfv3TrapNbrRtrId.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIOspfv3TrapNbrRtrId.setStatus(_A)
_FsMIOspfv3TrapVirtNbrArea_Type=AreaID
_FsMIOspfv3TrapVirtNbrArea_Object=MibScalar
fsMIOspfv3TrapVirtNbrArea=_FsMIOspfv3TrapVirtNbrArea_Object((1,3,6,1,4,1,10876,101,2,24,101,1,4),_FsMIOspfv3TrapVirtNbrArea_Type())
fsMIOspfv3TrapVirtNbrArea.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIOspfv3TrapVirtNbrArea.setStatus(_A)
class _FsMIOspfv3TrapBulkUpdAbortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('memAllocFailed',2),('sendFailed',3),('processFailed',4)))
_FsMIOspfv3TrapBulkUpdAbortReason_Type.__name__=_C
_FsMIOspfv3TrapBulkUpdAbortReason_Object=MibScalar
fsMIOspfv3TrapBulkUpdAbortReason=_FsMIOspfv3TrapBulkUpdAbortReason_Object((1,3,6,1,4,1,10876,101,2,24,101,1,5),_FsMIOspfv3TrapBulkUpdAbortReason_Type())
fsMIOspfv3TrapBulkUpdAbortReason.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIOspfv3TrapBulkUpdAbortReason.setStatus(_A)
fsMIStdOspfv3Entry.registerAugmentions((_E,_A3))
fsMIOspfv3Entry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3Entry.registerAugmentions((_E,_A4))
fsMIOspfv3RRDRouteEntry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3Entry.registerAugmentions((_E,_A5))
fsMIOspfv3PreferenceEntry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIOspfv3RestartStatusChange=NotificationType((1,3,6,1,4,1,10876,101,2,24,101,0,1))
fsMIOspfv3RestartStatusChange.setObjects(*((_F,_K),(_F,_Y),(_F,_X),(_F,_W)))
if mibBuilder.loadTexts:fsMIOspfv3RestartStatusChange.setStatus(_A)
fsMIOspfv3NbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,2,24,101,0,2))
fsMIOspfv3NbrRestartHelperStatusChange.setObjects(*((_F,_K),(_E,_A6),(_E,_A7),(_F,_V),(_F,_T),(_F,_U)))
if mibBuilder.loadTexts:fsMIOspfv3NbrRestartHelperStatusChange.setStatus(_A)
fsMIOspfv3VirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,2,24,101,0,3))
fsMIOspfv3VirtNbrRestartHelperStatusChange.setObjects(*((_F,_K),(_E,_A8),(_E,_A9),(_F,_b),(_F,_Z),(_F,_a)))
if mibBuilder.loadTexts:fsMIOspfv3VirtNbrRestartHelperStatusChange.setStatus(_A)
fsMIOspfv3HotStandbyStateChgTrap=NotificationType((1,3,6,1,4,1,10876,101,2,24,101,0,4))
fsMIOspfv3HotStandbyStateChgTrap.setObjects(*((_F,_K),(_E,_AA)))
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyStateChgTrap.setStatus(_A)
fsMIOspfv3HotStandbyBulkUpdAbortTrap=NotificationType((1,3,6,1,4,1,10876,101,2,24,101,0,5))
fsMIOspfv3HotStandbyBulkUpdAbortTrap.setObjects(*((_F,_K),(_E,_AB),(_E,_AC)))
if mibBuilder.loadTexts:fsMIOspfv3HotStandbyBulkUpdAbortTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsMIOspfv3':fsMIOspfv3,'fsMIOspfv3GeneralGroup':fsMIOspfv3GeneralGroup,'fsMIOspfv3GlobalTraceLevel':fsMIOspfv3GlobalTraceLevel,'fsMIOspfv3VrfSpfInterval':fsMIOspfv3VrfSpfInterval,'fsMIOspfv3RTStaggeringStatus':fsMIOspfv3RTStaggeringStatus,'fsMIOspfv3HotStandbyAdminStatus':fsMIOspfv3HotStandbyAdminStatus,_AA:fsMIOspfv3HotStandbyState,_AB:fsMIOspfv3DynamicBulkUpdStatus,'fsMIOspfv3StandbyHelloSyncCount':fsMIOspfv3StandbyHelloSyncCount,'fsMIOspfv3StandbyLsaSyncCount':fsMIOspfv3StandbyLsaSyncCount,'fsMIOspfv3Table':fsMIOspfv3Table,_A3:fsMIOspfv3Entry,'fsMIOspfv3OverFlowState':fsMIOspfv3OverFlowState,'fsMIOspfv3TraceLevel':fsMIOspfv3TraceLevel,'fsMIOspfv3ABRType':fsMIOspfv3ABRType,'fsMIOspfv3NssaAsbrDefRtTrans':fsMIOspfv3NssaAsbrDefRtTrans,'fsMIOspfv3DefaultPassiveInterface':fsMIOspfv3DefaultPassiveInterface,'fsMIOspfv3SpfDelay':fsMIOspfv3SpfDelay,'fsMIOspfv3SpfHoldTime':fsMIOspfv3SpfHoldTime,'fsMIOspfv3RTStaggeringInterval':fsMIOspfv3RTStaggeringInterval,'fsMIOspfv3RestartStrictLsaChecking':fsMIOspfv3RestartStrictLsaChecking,'fsMIOspfv3HelperSupport':fsMIOspfv3HelperSupport,'fsMIOspfv3HelperGraceTimeLimit':fsMIOspfv3HelperGraceTimeLimit,'fsMIOspfv3RestartAckState':fsMIOspfv3RestartAckState,'fsMIOspfv3GraceLsaRetransmitCount':fsMIOspfv3GraceLsaRetransmitCount,'fsMIOspfv3RestartReason':fsMIOspfv3RestartReason,'fsMIOspfv3ExtTraceLevel':fsMIOspfv3ExtTraceLevel,'fsMIOspfv3SetTraps':fsMIOspfv3SetTraps,'fsMIOspfv3IfTable':fsMIOspfv3IfTable,'fsMIOspfv3IfEntry':fsMIOspfv3IfEntry,_g:fsMIOspfv3IfIndex,'fsMIOspfv3IfOperState':fsMIOspfv3IfOperState,'fsMIOspfv3IfPassive':fsMIOspfv3IfPassive,'fsMIOspfv3IfNbrCount':fsMIOspfv3IfNbrCount,'fsMIOspfv3IfAdjCount':fsMIOspfv3IfAdjCount,'fsMIOspfv3IfHelloRcvd':fsMIOspfv3IfHelloRcvd,'fsMIOspfv3IfHelloTxed':fsMIOspfv3IfHelloTxed,'fsMIOspfv3IfHelloDisd':fsMIOspfv3IfHelloDisd,'fsMIOspfv3IfDdpRcvd':fsMIOspfv3IfDdpRcvd,'fsMIOspfv3IfDdpTxed':fsMIOspfv3IfDdpTxed,'fsMIOspfv3IfDdpDisd':fsMIOspfv3IfDdpDisd,'fsMIOspfv3IfLrqRcvd':fsMIOspfv3IfLrqRcvd,'fsMIOspfv3IfLrqTxed':fsMIOspfv3IfLrqTxed,'fsMIOspfv3IfLrqDisd':fsMIOspfv3IfLrqDisd,'fsMIOspfv3IfLsuRcvd':fsMIOspfv3IfLsuRcvd,'fsMIOspfv3IfLsuTxed':fsMIOspfv3IfLsuTxed,'fsMIOspfv3IfLsuDisd':fsMIOspfv3IfLsuDisd,'fsMIOspfv3IfLakRcvd':fsMIOspfv3IfLakRcvd,'fsMIOspfv3IfLakTxed':fsMIOspfv3IfLakTxed,'fsMIOspfv3IfLakDisd':fsMIOspfv3IfLakDisd,'fsMIOspfv3IfContextId':fsMIOspfv3IfContextId,'fsMIOspfv3IfLinkLSASuppression':fsMIOspfv3IfLinkLSASuppression,'fsMIOspfv3RoutingTable':fsMIOspfv3RoutingTable,'fsMIOspfv3RoutingEntry':fsMIOspfv3RoutingEntry,_h:fsMIOspfv3RouteDestType,_i:fsMIOspfv3RouteDest,_j:fsMIOspfv3RoutePfxLength,_k:fsMIOspfv3RouteNextHopType,_l:fsMIOspfv3RouteNextHop,'fsMIOspfv3RouteType':fsMIOspfv3RouteType,'fsMIOspfv3RouteAreaId':fsMIOspfv3RouteAreaId,'fsMIOspfv3RouteCost':fsMIOspfv3RouteCost,'fsMIOspfv3RouteType2Cost':fsMIOspfv3RouteType2Cost,'fsMIOspfv3RouteInterfaceIndex':fsMIOspfv3RouteInterfaceIndex,'fsMIOspfv3AsExternalAggregationTable':fsMIOspfv3AsExternalAggregationTable,'fsMIOspfv3AsExternalAggregationEntry':fsMIOspfv3AsExternalAggregationEntry,_q:fsMIOspfv3AsExternalAggregationNetType,_r:fsMIOspfv3AsExternalAggregationNet,_s:fsMIOspfv3AsExternalAggregationPfxLength,_t:fsMIOspfv3AsExternalAggregationAreaId,'fsMIOspfv3AsExternalAggregationEffect':fsMIOspfv3AsExternalAggregationEffect,'fsMIOspfv3AsExternalAggregationTranslation':fsMIOspfv3AsExternalAggregationTranslation,'fsMIOspfv3AsExternalAggregationStatus':fsMIOspfv3AsExternalAggregationStatus,'fsMIOspfv3BRRouteTable':fsMIOspfv3BRRouteTable,'fsMIOspfv3BRRouteEntry':fsMIOspfv3BRRouteEntry,_u:fsMIOspfv3BRRouteDest,_v:fsMIOspfv3BRRouteNextHopType,_w:fsMIOspfv3BRRouteNextHop,_x:fsMIOspfv3BRRouteDestType,'fsMIOspfv3BRRouteType':fsMIOspfv3BRRouteType,'fsMIOspfv3BRRouteAreaId':fsMIOspfv3BRRouteAreaId,'fsMIOspfv3BRRouteCost':fsMIOspfv3BRRouteCost,'fsMIOspfv3BRRouteInterfaceIndex':fsMIOspfv3BRRouteInterfaceIndex,'fsMIOspfv3RedistRouteCfgTable':fsMIOspfv3RedistRouteCfgTable,'fsMIOspfv3RedistRouteCfgEntry':fsMIOspfv3RedistRouteCfgEntry,_y:fsMIOspfv3RedistRouteDestType,_z:fsMIOspfv3RedistRouteDest,_A0:fsMIOspfv3RedistRoutePfxLength,'fsMIOspfv3RedistRouteMetric':fsMIOspfv3RedistRouteMetric,'fsMIOspfv3RedistRouteMetricType':fsMIOspfv3RedistRouteMetricType,'fsMIOspfv3RedistRouteTagType':fsMIOspfv3RedistRouteTagType,'fsMIOspfv3RedistRouteTag':fsMIOspfv3RedistRouteTag,'fsMIOspfv3RedistRouteStatus':fsMIOspfv3RedistRouteStatus,'fsMIOspfv3RRDGroup':fsMIOspfv3RRDGroup,'fsMIOspfv3RRDGeneralGroup':fsMIOspfv3RRDGeneralGroup,'fsMIOspfv3RRDRouteTable':fsMIOspfv3RRDRouteTable,_A4:fsMIOspfv3RRDRouteEntry,'fsMIOspfv3RRDStatus':fsMIOspfv3RRDStatus,'fsMIOspfv3RRDSrcProtoMask':fsMIOspfv3RRDSrcProtoMask,'fsMIOspfv3RRDRouteMapName':fsMIOspfv3RRDRouteMapName,'fsMIOspfv3DistInOutRouteMap':fsMIOspfv3DistInOutRouteMap,'fsMIOspfv3DistInOutRouteMapTable':fsMIOspfv3DistInOutRouteMapTable,'fsMIOspfv3DistInOutRouteMapEntry':fsMIOspfv3DistInOutRouteMapEntry,_A1:fsMIOspfv3DistInOutRouteMapName,_A2:fsMIOspfv3DistInOutRouteMapType,'fsMIOspfv3DistInOutRouteMapValue':fsMIOspfv3DistInOutRouteMapValue,'fsMIOspfv3DistInOutRouteMapRowStatus':fsMIOspfv3DistInOutRouteMapRowStatus,'fsMIOspfv3PreferenceGroup':fsMIOspfv3PreferenceGroup,'fsMIOspfv3PreferenceTable':fsMIOspfv3PreferenceTable,_A5:fsMIOspfv3PreferenceEntry,'fsMIOspfv3PreferenceValue':fsMIOspfv3PreferenceValue,'fsMIOspfv3Notification':fsMIOspfv3Notification,'fsMIOspfv3Traps':fsMIOspfv3Traps,'fsMIOspfv3RestartStatusChange':fsMIOspfv3RestartStatusChange,'fsMIOspfv3NbrRestartHelperStatusChange':fsMIOspfv3NbrRestartHelperStatusChange,'fsMIOspfv3VirtNbrRestartHelperStatusChange':fsMIOspfv3VirtNbrRestartHelperStatusChange,'fsMIOspfv3HotStandbyStateChgTrap':fsMIOspfv3HotStandbyStateChgTrap,'fsMIOspfv3HotStandbyBulkUpdAbortTrap':fsMIOspfv3HotStandbyBulkUpdAbortTrap,'fsMIOspfv3TrapObject':fsMIOspfv3TrapObject,_A6:fsMIOspfv3TrapNbrIfIndex,_A9:fsMIOspfv3TrapVirtNbrRtrId,_A7:fsMIOspfv3TrapNbrRtrId,_A8:fsMIOspfv3TrapVirtNbrArea,_AC:fsMIOspfv3TrapBulkUpdAbortReason})