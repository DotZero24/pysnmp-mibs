_AC='fsMIStdOspfv3AreaAggregatePrefixLength'
_AB='fsMIStdOspfv3AreaAggregatePrefix'
_AA='fsMIStdOspfv3AreaAggregatePrefixType'
_A9='fsMIStdOspfv3AreaAggregateAreaLsdbType'
_A8='fsMIStdOspfv3AreaAggregateAreaID'
_A7='fsMIStdOspfv3VirtNbrRtrId'
_A6='fsMIStdOspfv3VirtNbrArea'
_A5='fsMIStdOspfv3NbmaNbrAddress'
_A4='fsMIStdOspfv3NbmaNbrAddressType'
_A3='fsMIStdOspfv3NbmaNbrIfIndex'
_A2='notHelping'
_A1='fsMIStdOspfv3NbrRtrId'
_A0='fsMIStdOspfv3NbrIfIndex'
_z='fsMIStdOspfv3VirtIfNeighbor'
_y='fsMIStdOspfv3VirtIfAreaId'
_x='fsMIStdOspfv3IfIndex'
_w='fsMIStdOspfv3HostAddress'
_v='fsMIStdOspfv3HostAddressType'
_u='fsMIStdOspfv3LinkLsdbLsid'
_t='fsMIStdOspfv3LinkLsdbRouterId'
_s='fsMIStdOspfv3LinkLsdbType'
_r='fsMIStdOspfv3LinkLsdbIfIndex'
_q='fsMIStdOspfv3AreaLsdbLsid'
_p='fsMIStdOspfv3AreaLsdbRouterId'
_o='fsMIStdOspfv3AreaLsdbType'
_n='fsMIStdOspfv3AreaLsdbAreaId'
_m='fsMIStdOspfv3AsLsdbLsid'
_l='fsMIStdOspfv3AsLsdbRouterId'
_k='fsMIStdOspfv3AsLsdbType'
_j='fsMIStdOspfv3AreaId'
_i='StorageType'
_h='Status'
_g='AreaID'
_f='InetAddressPrefixLength'
_e='full'
_d='loading'
_c='exchange'
_b='exchangeStart'
_a='twoWay'
_Z='init'
_Y='attempt'
_X='RouterDeadRange'
_W='pointToPoint'
_V='topologyChanged'
_U='timedOut'
_T='completed'
_S='inProgress'
_R='TruthValue'
_Q='HelloRange'
_P='DesignatedRouterPriority'
_O='none'
_N='OctetString'
_M='down'
_L='UpToRefreshInterval'
_K='InetAddress'
_J='Unsigned32'
_I='fsMIStdOspfv3ContextId'
_H='read-write'
_G='seconds'
_F='Integer32'
_E='not-accessible'
_D='ARICENT-MISTDOSPFV3-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,_f,'InetAddressType')
AreaID,BigMetric,DesignatedRouterPriority,HelloRange,Metric,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB',_g,'BigMetric',_P,_Q,'Metric','RouterID',_h)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_i,'TextualConvention',_R)
fsMIStdOspfv3=ModuleIdentity((1,3,6,1,4,1,29601,2,23))
if mibBuilder.loadTexts:fsMIStdOspfv3.setRevisions(('2012-09-05 00:00',))
class UpToRefreshInterval(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
class RouterDeadRange(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIStdOspfv3Objects_ObjectIdentity=ObjectIdentity
fsMIStdOspfv3Objects=_FsMIStdOspfv3Objects_ObjectIdentity((1,3,6,1,4,1,29601,2,23,1))
_FsMIStdOspfv3Table_Object=MibTable
fsMIStdOspfv3Table=_FsMIStdOspfv3Table_Object((1,3,6,1,4,1,29601,2,23,1,1))
if mibBuilder.loadTexts:fsMIStdOspfv3Table.setStatus(_A)
_FsMIStdOspfv3Entry_Object=MibTableRow
fsMIStdOspfv3Entry=_FsMIStdOspfv3Entry_Object((1,3,6,1,4,1,29601,2,23,1,1,1))
fsMIStdOspfv3Entry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:fsMIStdOspfv3Entry.setStatus(_A)
class _FsMIStdOspfv3ContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIStdOspfv3ContextId_Type.__name__=_F
_FsMIStdOspfv3ContextId_Object=MibTableColumn
fsMIStdOspfv3ContextId=_FsMIStdOspfv3ContextId_Object((1,3,6,1,4,1,29601,2,23,1,1,1,1),_FsMIStdOspfv3ContextId_Type())
fsMIStdOspfv3ContextId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3ContextId.setStatus(_A)
_FsMIStdOspfv3RouterId_Type=RouterID
_FsMIStdOspfv3RouterId_Object=MibTableColumn
fsMIStdOspfv3RouterId=_FsMIStdOspfv3RouterId_Object((1,3,6,1,4,1,29601,2,23,1,1,1,2),_FsMIStdOspfv3RouterId_Type())
fsMIStdOspfv3RouterId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3RouterId.setStatus(_A)
_FsMIStdOspfv3AdminStat_Type=Status
_FsMIStdOspfv3AdminStat_Object=MibTableColumn
fsMIStdOspfv3AdminStat=_FsMIStdOspfv3AdminStat_Object((1,3,6,1,4,1,29601,2,23,1,1,1,3),_FsMIStdOspfv3AdminStat_Type())
fsMIStdOspfv3AdminStat.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3AdminStat.setStatus(_A)
class _FsMIStdOspfv3VersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('version3',3))
_FsMIStdOspfv3VersionNumber_Type.__name__=_F
_FsMIStdOspfv3VersionNumber_Object=MibTableColumn
fsMIStdOspfv3VersionNumber=_FsMIStdOspfv3VersionNumber_Object((1,3,6,1,4,1,29601,2,23,1,1,1,4),_FsMIStdOspfv3VersionNumber_Type())
fsMIStdOspfv3VersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VersionNumber.setStatus(_A)
_FsMIStdOspfv3AreaBdrRtrStatus_Type=TruthValue
_FsMIStdOspfv3AreaBdrRtrStatus_Object=MibTableColumn
fsMIStdOspfv3AreaBdrRtrStatus=_FsMIStdOspfv3AreaBdrRtrStatus_Object((1,3,6,1,4,1,29601,2,23,1,1,1,5),_FsMIStdOspfv3AreaBdrRtrStatus_Type())
fsMIStdOspfv3AreaBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaBdrRtrStatus.setStatus(_A)
_FsMIStdOspfv3ASBdrRtrStatus_Type=TruthValue
_FsMIStdOspfv3ASBdrRtrStatus_Object=MibTableColumn
fsMIStdOspfv3ASBdrRtrStatus=_FsMIStdOspfv3ASBdrRtrStatus_Object((1,3,6,1,4,1,29601,2,23,1,1,1,6),_FsMIStdOspfv3ASBdrRtrStatus_Type())
fsMIStdOspfv3ASBdrRtrStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3ASBdrRtrStatus.setStatus(_A)
_FsMIStdOspfv3AsScopeLsaCount_Type=Gauge32
_FsMIStdOspfv3AsScopeLsaCount_Object=MibTableColumn
fsMIStdOspfv3AsScopeLsaCount=_FsMIStdOspfv3AsScopeLsaCount_Object((1,3,6,1,4,1,29601,2,23,1,1,1,7),_FsMIStdOspfv3AsScopeLsaCount_Type())
fsMIStdOspfv3AsScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsScopeLsaCount.setStatus(_A)
_FsMIStdOspfv3AsScopeLsaCksumSum_Type=Integer32
_FsMIStdOspfv3AsScopeLsaCksumSum_Object=MibTableColumn
fsMIStdOspfv3AsScopeLsaCksumSum=_FsMIStdOspfv3AsScopeLsaCksumSum_Object((1,3,6,1,4,1,29601,2,23,1,1,1,8),_FsMIStdOspfv3AsScopeLsaCksumSum_Type())
fsMIStdOspfv3AsScopeLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsScopeLsaCksumSum.setStatus(_A)
_FsMIStdOspfv3OriginateNewLsas_Type=Counter32
_FsMIStdOspfv3OriginateNewLsas_Object=MibTableColumn
fsMIStdOspfv3OriginateNewLsas=_FsMIStdOspfv3OriginateNewLsas_Object((1,3,6,1,4,1,29601,2,23,1,1,1,9),_FsMIStdOspfv3OriginateNewLsas_Type())
fsMIStdOspfv3OriginateNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3OriginateNewLsas.setStatus(_A)
_FsMIStdOspfv3RxNewLsas_Type=Counter32
_FsMIStdOspfv3RxNewLsas_Object=MibTableColumn
fsMIStdOspfv3RxNewLsas=_FsMIStdOspfv3RxNewLsas_Object((1,3,6,1,4,1,29601,2,23,1,1,1,10),_FsMIStdOspfv3RxNewLsas_Type())
fsMIStdOspfv3RxNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3RxNewLsas.setStatus(_A)
_FsMIStdOspfv3ExtLsaCount_Type=Gauge32
_FsMIStdOspfv3ExtLsaCount_Object=MibTableColumn
fsMIStdOspfv3ExtLsaCount=_FsMIStdOspfv3ExtLsaCount_Object((1,3,6,1,4,1,29601,2,23,1,1,1,11),_FsMIStdOspfv3ExtLsaCount_Type())
fsMIStdOspfv3ExtLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3ExtLsaCount.setStatus(_A)
class _FsMIStdOspfv3ExtAreaLsdbLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_FsMIStdOspfv3ExtAreaLsdbLimit_Type.__name__=_F
_FsMIStdOspfv3ExtAreaLsdbLimit_Object=MibTableColumn
fsMIStdOspfv3ExtAreaLsdbLimit=_FsMIStdOspfv3ExtAreaLsdbLimit_Object((1,3,6,1,4,1,29601,2,23,1,1,1,12),_FsMIStdOspfv3ExtAreaLsdbLimit_Type())
fsMIStdOspfv3ExtAreaLsdbLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3ExtAreaLsdbLimit.setStatus(_A)
class _FsMIStdOspfv3MulticastExtensions_Type(Bits):namedValues=NamedValues(*(('intraAreaMulticast',0),('interAreaMulticast',1),('interAsMulticast',2)))
_FsMIStdOspfv3MulticastExtensions_Type.__name__='Bits'
_FsMIStdOspfv3MulticastExtensions_Object=MibTableColumn
fsMIStdOspfv3MulticastExtensions=_FsMIStdOspfv3MulticastExtensions_Object((1,3,6,1,4,1,29601,2,23,1,1,1,13),_FsMIStdOspfv3MulticastExtensions_Type())
fsMIStdOspfv3MulticastExtensions.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3MulticastExtensions.setStatus(_A)
_FsMIStdOspfv3ExitOverflowInterval_Type=Unsigned32
_FsMIStdOspfv3ExitOverflowInterval_Object=MibTableColumn
fsMIStdOspfv3ExitOverflowInterval=_FsMIStdOspfv3ExitOverflowInterval_Object((1,3,6,1,4,1,29601,2,23,1,1,1,14),_FsMIStdOspfv3ExitOverflowInterval_Type())
fsMIStdOspfv3ExitOverflowInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3ExitOverflowInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3ExitOverflowInterval.setUnits(_G)
_FsMIStdOspfv3DemandExtensions_Type=TruthValue
_FsMIStdOspfv3DemandExtensions_Object=MibTableColumn
fsMIStdOspfv3DemandExtensions=_FsMIStdOspfv3DemandExtensions_Object((1,3,6,1,4,1,29601,2,23,1,1,1,15),_FsMIStdOspfv3DemandExtensions_Type())
fsMIStdOspfv3DemandExtensions.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3DemandExtensions.setStatus(_A)
_FsMIStdOspfv3TrafficEngineeringSupport_Type=TruthValue
_FsMIStdOspfv3TrafficEngineeringSupport_Object=MibTableColumn
fsMIStdOspfv3TrafficEngineeringSupport=_FsMIStdOspfv3TrafficEngineeringSupport_Object((1,3,6,1,4,1,29601,2,23,1,1,1,16),_FsMIStdOspfv3TrafficEngineeringSupport_Type())
fsMIStdOspfv3TrafficEngineeringSupport.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3TrafficEngineeringSupport.setStatus(_A)
_FsMIStdOspfv3ReferenceBandwidth_Type=Unsigned32
_FsMIStdOspfv3ReferenceBandwidth_Object=MibTableColumn
fsMIStdOspfv3ReferenceBandwidth=_FsMIStdOspfv3ReferenceBandwidth_Object((1,3,6,1,4,1,29601,2,23,1,1,1,17),_FsMIStdOspfv3ReferenceBandwidth_Type())
fsMIStdOspfv3ReferenceBandwidth.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3ReferenceBandwidth.setStatus(_A)
class _FsMIStdOspfv3RestartSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('plannedOnly',2),('plannedAndUnplanned',3)))
_FsMIStdOspfv3RestartSupport_Type.__name__=_F
_FsMIStdOspfv3RestartSupport_Object=MibTableColumn
fsMIStdOspfv3RestartSupport=_FsMIStdOspfv3RestartSupport_Object((1,3,6,1,4,1,29601,2,23,1,1,1,18),_FsMIStdOspfv3RestartSupport_Type())
fsMIStdOspfv3RestartSupport.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartSupport.setStatus(_A)
_FsMIStdOspfv3RestartInterval_Type=UpToRefreshInterval
_FsMIStdOspfv3RestartInterval_Object=MibTableColumn
fsMIStdOspfv3RestartInterval=_FsMIStdOspfv3RestartInterval_Object((1,3,6,1,4,1,29601,2,23,1,1,1,19),_FsMIStdOspfv3RestartInterval_Type())
fsMIStdOspfv3RestartInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartInterval.setUnits(_G)
class _FsMIStdOspfv3RestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRestarting',1),('plannedRestart',2),('unplannedRestart',3)))
_FsMIStdOspfv3RestartStatus_Type.__name__=_F
_FsMIStdOspfv3RestartStatus_Object=MibTableColumn
fsMIStdOspfv3RestartStatus=_FsMIStdOspfv3RestartStatus_Object((1,3,6,1,4,1,29601,2,23,1,1,1,20),_FsMIStdOspfv3RestartStatus_Type())
fsMIStdOspfv3RestartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartStatus.setStatus(_A)
_FsMIStdOspfv3RestartAge_Type=UpToRefreshInterval
_FsMIStdOspfv3RestartAge_Object=MibTableColumn
fsMIStdOspfv3RestartAge=_FsMIStdOspfv3RestartAge_Object((1,3,6,1,4,1,29601,2,23,1,1,1,21),_FsMIStdOspfv3RestartAge_Type())
fsMIStdOspfv3RestartAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartAge.setUnits(_G)
class _FsMIStdOspfv3RestartExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_FsMIStdOspfv3RestartExitReason_Type.__name__=_F
_FsMIStdOspfv3RestartExitReason_Object=MibTableColumn
fsMIStdOspfv3RestartExitReason=_FsMIStdOspfv3RestartExitReason_Object((1,3,6,1,4,1,29601,2,23,1,1,1,22),_FsMIStdOspfv3RestartExitReason_Type())
fsMIStdOspfv3RestartExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3RestartExitReason.setStatus(_A)
_FsMIStdOspfv3Status_Type=RowStatus
_FsMIStdOspfv3Status_Object=MibTableColumn
fsMIStdOspfv3Status=_FsMIStdOspfv3Status_Object((1,3,6,1,4,1,29601,2,23,1,1,1,23),_FsMIStdOspfv3Status_Type())
fsMIStdOspfv3Status.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfv3Status.setStatus(_A)
_FsMIStdOspfv3AreaTable_Object=MibTable
fsMIStdOspfv3AreaTable=_FsMIStdOspfv3AreaTable_Object((1,3,6,1,4,1,29601,2,23,1,2))
if mibBuilder.loadTexts:fsMIStdOspfv3AreaTable.setStatus(_A)
_FsMIStdOspfv3AreaEntry_Object=MibTableRow
fsMIStdOspfv3AreaEntry=_FsMIStdOspfv3AreaEntry_Object((1,3,6,1,4,1,29601,2,23,1,2,1))
fsMIStdOspfv3AreaEntry.setIndexNames((0,_D,_I),(0,_D,_j))
if mibBuilder.loadTexts:fsMIStdOspfv3AreaEntry.setStatus(_A)
_FsMIStdOspfv3AreaId_Type=AreaID
_FsMIStdOspfv3AreaId_Object=MibTableColumn
fsMIStdOspfv3AreaId=_FsMIStdOspfv3AreaId_Object((1,3,6,1,4,1,29601,2,23,1,2,1,1),_FsMIStdOspfv3AreaId_Type())
fsMIStdOspfv3AreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaId.setStatus(_A)
class _FsMIStdOspfv3ImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_FsMIStdOspfv3ImportAsExtern_Type.__name__=_F
_FsMIStdOspfv3ImportAsExtern_Object=MibTableColumn
fsMIStdOspfv3ImportAsExtern=_FsMIStdOspfv3ImportAsExtern_Object((1,3,6,1,4,1,29601,2,23,1,2,1,2),_FsMIStdOspfv3ImportAsExtern_Type())
fsMIStdOspfv3ImportAsExtern.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3ImportAsExtern.setStatus(_A)
_FsMIStdOspfv3AreaSpfRuns_Type=Counter32
_FsMIStdOspfv3AreaSpfRuns_Object=MibTableColumn
fsMIStdOspfv3AreaSpfRuns=_FsMIStdOspfv3AreaSpfRuns_Object((1,3,6,1,4,1,29601,2,23,1,2,1,3),_FsMIStdOspfv3AreaSpfRuns_Type())
fsMIStdOspfv3AreaSpfRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaSpfRuns.setStatus(_A)
_FsMIStdOspfv3AreaBdrRtrCount_Type=Gauge32
_FsMIStdOspfv3AreaBdrRtrCount_Object=MibTableColumn
fsMIStdOspfv3AreaBdrRtrCount=_FsMIStdOspfv3AreaBdrRtrCount_Object((1,3,6,1,4,1,29601,2,23,1,2,1,4),_FsMIStdOspfv3AreaBdrRtrCount_Type())
fsMIStdOspfv3AreaBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaBdrRtrCount.setStatus(_A)
_FsMIStdOspfv3AreaAsBdrRtrCount_Type=Gauge32
_FsMIStdOspfv3AreaAsBdrRtrCount_Object=MibTableColumn
fsMIStdOspfv3AreaAsBdrRtrCount=_FsMIStdOspfv3AreaAsBdrRtrCount_Object((1,3,6,1,4,1,29601,2,23,1,2,1,5),_FsMIStdOspfv3AreaAsBdrRtrCount_Type())
fsMIStdOspfv3AreaAsBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAsBdrRtrCount.setStatus(_A)
_FsMIStdOspfv3AreaScopeLsaCount_Type=Gauge32
_FsMIStdOspfv3AreaScopeLsaCount_Object=MibTableColumn
fsMIStdOspfv3AreaScopeLsaCount=_FsMIStdOspfv3AreaScopeLsaCount_Object((1,3,6,1,4,1,29601,2,23,1,2,1,6),_FsMIStdOspfv3AreaScopeLsaCount_Type())
fsMIStdOspfv3AreaScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaScopeLsaCount.setStatus(_A)
_FsMIStdOspfv3AreaScopeLsaCksumSum_Type=Integer32
_FsMIStdOspfv3AreaScopeLsaCksumSum_Object=MibTableColumn
fsMIStdOspfv3AreaScopeLsaCksumSum=_FsMIStdOspfv3AreaScopeLsaCksumSum_Object((1,3,6,1,4,1,29601,2,23,1,2,1,7),_FsMIStdOspfv3AreaScopeLsaCksumSum_Type())
fsMIStdOspfv3AreaScopeLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaScopeLsaCksumSum.setStatus(_A)
class _FsMIStdOspfv3AreaSummary_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_FsMIStdOspfv3AreaSummary_Type.__name__=_F
_FsMIStdOspfv3AreaSummary_Object=MibTableColumn
fsMIStdOspfv3AreaSummary=_FsMIStdOspfv3AreaSummary_Object((1,3,6,1,4,1,29601,2,23,1,2,1,8),_FsMIStdOspfv3AreaSummary_Type())
fsMIStdOspfv3AreaSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaSummary.setStatus(_A)
_FsMIStdOspfv3StubMetric_Type=BigMetric
_FsMIStdOspfv3StubMetric_Object=MibTableColumn
fsMIStdOspfv3StubMetric=_FsMIStdOspfv3StubMetric_Object((1,3,6,1,4,1,29601,2,23,1,2,1,9),_FsMIStdOspfv3StubMetric_Type())
fsMIStdOspfv3StubMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3StubMetric.setStatus(_A)
class _FsMIStdOspfv3AreaNssaTranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_FsMIStdOspfv3AreaNssaTranslatorRole_Type.__name__=_F
_FsMIStdOspfv3AreaNssaTranslatorRole_Object=MibTableColumn
fsMIStdOspfv3AreaNssaTranslatorRole=_FsMIStdOspfv3AreaNssaTranslatorRole_Object((1,3,6,1,4,1,29601,2,23,1,2,1,10),_FsMIStdOspfv3AreaNssaTranslatorRole_Type())
fsMIStdOspfv3AreaNssaTranslatorRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaNssaTranslatorRole.setStatus(_A)
class _FsMIStdOspfv3AreaNssaTranslatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('elected',2),('disabled',3)))
_FsMIStdOspfv3AreaNssaTranslatorState_Type.__name__=_F
_FsMIStdOspfv3AreaNssaTranslatorState_Object=MibTableColumn
fsMIStdOspfv3AreaNssaTranslatorState=_FsMIStdOspfv3AreaNssaTranslatorState_Object((1,3,6,1,4,1,29601,2,23,1,2,1,11),_FsMIStdOspfv3AreaNssaTranslatorState_Type())
fsMIStdOspfv3AreaNssaTranslatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaNssaTranslatorState.setStatus(_A)
class _FsMIStdOspfv3AreaNssaTranslatorStabilityInterval_Type(Unsigned32):defaultValue=40
_FsMIStdOspfv3AreaNssaTranslatorStabilityInterval_Type.__name__=_J
_FsMIStdOspfv3AreaNssaTranslatorStabilityInterval_Object=MibTableColumn
fsMIStdOspfv3AreaNssaTranslatorStabilityInterval=_FsMIStdOspfv3AreaNssaTranslatorStabilityInterval_Object((1,3,6,1,4,1,29601,2,23,1,2,1,12),_FsMIStdOspfv3AreaNssaTranslatorStabilityInterval_Type())
fsMIStdOspfv3AreaNssaTranslatorStabilityInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaNssaTranslatorStabilityInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaNssaTranslatorStabilityInterval.setUnits(_G)
_FsMIStdOspfv3AreaNssaTranslatorEvents_Type=Counter32
_FsMIStdOspfv3AreaNssaTranslatorEvents_Object=MibTableColumn
fsMIStdOspfv3AreaNssaTranslatorEvents=_FsMIStdOspfv3AreaNssaTranslatorEvents_Object((1,3,6,1,4,1,29601,2,23,1,2,1,13),_FsMIStdOspfv3AreaNssaTranslatorEvents_Type())
fsMIStdOspfv3AreaNssaTranslatorEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaNssaTranslatorEvents.setStatus(_A)
class _FsMIStdOspfv3AreaStubMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ospfMetric',1),('comparableCost',2),('nonComparable',3)))
_FsMIStdOspfv3AreaStubMetricType_Type.__name__=_F
_FsMIStdOspfv3AreaStubMetricType_Object=MibTableColumn
fsMIStdOspfv3AreaStubMetricType=_FsMIStdOspfv3AreaStubMetricType_Object((1,3,6,1,4,1,29601,2,23,1,2,1,14),_FsMIStdOspfv3AreaStubMetricType_Type())
fsMIStdOspfv3AreaStubMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaStubMetricType.setStatus(_A)
_FsMIStdOspfv3AreaStatus_Type=RowStatus
_FsMIStdOspfv3AreaStatus_Object=MibTableColumn
fsMIStdOspfv3AreaStatus=_FsMIStdOspfv3AreaStatus_Object((1,3,6,1,4,1,29601,2,23,1,2,1,15),_FsMIStdOspfv3AreaStatus_Type())
fsMIStdOspfv3AreaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaStatus.setStatus(_A)
_FsMIStdOspfv3AsLsdbTable_Object=MibTable
fsMIStdOspfv3AsLsdbTable=_FsMIStdOspfv3AsLsdbTable_Object((1,3,6,1,4,1,29601,2,23,1,3))
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbTable.setStatus(_A)
_FsMIStdOspfv3AsLsdbEntry_Object=MibTableRow
fsMIStdOspfv3AsLsdbEntry=_FsMIStdOspfv3AsLsdbEntry_Object((1,3,6,1,4,1,29601,2,23,1,3,1))
fsMIStdOspfv3AsLsdbEntry.setIndexNames((0,_D,_I),(0,_D,_k),(0,_D,_l),(0,_D,_m))
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbEntry.setStatus(_A)
class _FsMIStdOspfv3AsLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIStdOspfv3AsLsdbType_Type.__name__=_J
_FsMIStdOspfv3AsLsdbType_Object=MibTableColumn
fsMIStdOspfv3AsLsdbType=_FsMIStdOspfv3AsLsdbType_Object((1,3,6,1,4,1,29601,2,23,1,3,1,1),_FsMIStdOspfv3AsLsdbType_Type())
fsMIStdOspfv3AsLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbType.setStatus(_A)
_FsMIStdOspfv3AsLsdbRouterId_Type=RouterID
_FsMIStdOspfv3AsLsdbRouterId_Object=MibTableColumn
fsMIStdOspfv3AsLsdbRouterId=_FsMIStdOspfv3AsLsdbRouterId_Object((1,3,6,1,4,1,29601,2,23,1,3,1,2),_FsMIStdOspfv3AsLsdbRouterId_Type())
fsMIStdOspfv3AsLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbRouterId.setStatus(_A)
_FsMIStdOspfv3AsLsdbLsid_Type=IpAddress
_FsMIStdOspfv3AsLsdbLsid_Object=MibTableColumn
fsMIStdOspfv3AsLsdbLsid=_FsMIStdOspfv3AsLsdbLsid_Object((1,3,6,1,4,1,29601,2,23,1,3,1,3),_FsMIStdOspfv3AsLsdbLsid_Type())
fsMIStdOspfv3AsLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbLsid.setStatus(_A)
_FsMIStdOspfv3AsLsdbSequence_Type=Integer32
_FsMIStdOspfv3AsLsdbSequence_Object=MibTableColumn
fsMIStdOspfv3AsLsdbSequence=_FsMIStdOspfv3AsLsdbSequence_Object((1,3,6,1,4,1,29601,2,23,1,3,1,4),_FsMIStdOspfv3AsLsdbSequence_Type())
fsMIStdOspfv3AsLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbSequence.setStatus(_A)
_FsMIStdOspfv3AsLsdbAge_Type=Integer32
_FsMIStdOspfv3AsLsdbAge_Object=MibTableColumn
fsMIStdOspfv3AsLsdbAge=_FsMIStdOspfv3AsLsdbAge_Object((1,3,6,1,4,1,29601,2,23,1,3,1,5),_FsMIStdOspfv3AsLsdbAge_Type())
fsMIStdOspfv3AsLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbAge.setUnits(_G)
_FsMIStdOspfv3AsLsdbChecksum_Type=Integer32
_FsMIStdOspfv3AsLsdbChecksum_Object=MibTableColumn
fsMIStdOspfv3AsLsdbChecksum=_FsMIStdOspfv3AsLsdbChecksum_Object((1,3,6,1,4,1,29601,2,23,1,3,1,6),_FsMIStdOspfv3AsLsdbChecksum_Type())
fsMIStdOspfv3AsLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbChecksum.setStatus(_A)
class _FsMIStdOspfv3AsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FsMIStdOspfv3AsLsdbAdvertisement_Type.__name__=_N
_FsMIStdOspfv3AsLsdbAdvertisement_Object=MibTableColumn
fsMIStdOspfv3AsLsdbAdvertisement=_FsMIStdOspfv3AsLsdbAdvertisement_Object((1,3,6,1,4,1,29601,2,23,1,3,1,7),_FsMIStdOspfv3AsLsdbAdvertisement_Type())
fsMIStdOspfv3AsLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbAdvertisement.setStatus(_A)
_FsMIStdOspfv3AsLsdbTypeKnown_Type=TruthValue
_FsMIStdOspfv3AsLsdbTypeKnown_Object=MibTableColumn
fsMIStdOspfv3AsLsdbTypeKnown=_FsMIStdOspfv3AsLsdbTypeKnown_Object((1,3,6,1,4,1,29601,2,23,1,3,1,8),_FsMIStdOspfv3AsLsdbTypeKnown_Type())
fsMIStdOspfv3AsLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AsLsdbTypeKnown.setStatus(_A)
_FsMIStdOspfv3AreaLsdbTable_Object=MibTable
fsMIStdOspfv3AreaLsdbTable=_FsMIStdOspfv3AreaLsdbTable_Object((1,3,6,1,4,1,29601,2,23,1,4))
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbTable.setStatus(_A)
_FsMIStdOspfv3AreaLsdbEntry_Object=MibTableRow
fsMIStdOspfv3AreaLsdbEntry=_FsMIStdOspfv3AreaLsdbEntry_Object((1,3,6,1,4,1,29601,2,23,1,4,1))
fsMIStdOspfv3AreaLsdbEntry.setIndexNames((0,_D,_I),(0,_D,_n),(0,_D,_o),(0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbEntry.setStatus(_A)
_FsMIStdOspfv3AreaLsdbAreaId_Type=AreaID
_FsMIStdOspfv3AreaLsdbAreaId_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbAreaId=_FsMIStdOspfv3AreaLsdbAreaId_Object((1,3,6,1,4,1,29601,2,23,1,4,1,1),_FsMIStdOspfv3AreaLsdbAreaId_Type())
fsMIStdOspfv3AreaLsdbAreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbAreaId.setStatus(_A)
class _FsMIStdOspfv3AreaLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIStdOspfv3AreaLsdbType_Type.__name__=_J
_FsMIStdOspfv3AreaLsdbType_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbType=_FsMIStdOspfv3AreaLsdbType_Object((1,3,6,1,4,1,29601,2,23,1,4,1,2),_FsMIStdOspfv3AreaLsdbType_Type())
fsMIStdOspfv3AreaLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbType.setStatus(_A)
_FsMIStdOspfv3AreaLsdbRouterId_Type=RouterID
_FsMIStdOspfv3AreaLsdbRouterId_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbRouterId=_FsMIStdOspfv3AreaLsdbRouterId_Object((1,3,6,1,4,1,29601,2,23,1,4,1,3),_FsMIStdOspfv3AreaLsdbRouterId_Type())
fsMIStdOspfv3AreaLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbRouterId.setStatus(_A)
_FsMIStdOspfv3AreaLsdbLsid_Type=IpAddress
_FsMIStdOspfv3AreaLsdbLsid_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbLsid=_FsMIStdOspfv3AreaLsdbLsid_Object((1,3,6,1,4,1,29601,2,23,1,4,1,4),_FsMIStdOspfv3AreaLsdbLsid_Type())
fsMIStdOspfv3AreaLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbLsid.setStatus(_A)
_FsMIStdOspfv3AreaLsdbSequence_Type=Integer32
_FsMIStdOspfv3AreaLsdbSequence_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbSequence=_FsMIStdOspfv3AreaLsdbSequence_Object((1,3,6,1,4,1,29601,2,23,1,4,1,5),_FsMIStdOspfv3AreaLsdbSequence_Type())
fsMIStdOspfv3AreaLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbSequence.setStatus(_A)
_FsMIStdOspfv3AreaLsdbAge_Type=Integer32
_FsMIStdOspfv3AreaLsdbAge_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbAge=_FsMIStdOspfv3AreaLsdbAge_Object((1,3,6,1,4,1,29601,2,23,1,4,1,6),_FsMIStdOspfv3AreaLsdbAge_Type())
fsMIStdOspfv3AreaLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbAge.setUnits(_G)
_FsMIStdOspfv3AreaLsdbChecksum_Type=Integer32
_FsMIStdOspfv3AreaLsdbChecksum_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbChecksum=_FsMIStdOspfv3AreaLsdbChecksum_Object((1,3,6,1,4,1,29601,2,23,1,4,1,7),_FsMIStdOspfv3AreaLsdbChecksum_Type())
fsMIStdOspfv3AreaLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbChecksum.setStatus(_A)
class _FsMIStdOspfv3AreaLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FsMIStdOspfv3AreaLsdbAdvertisement_Type.__name__=_N
_FsMIStdOspfv3AreaLsdbAdvertisement_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbAdvertisement=_FsMIStdOspfv3AreaLsdbAdvertisement_Object((1,3,6,1,4,1,29601,2,23,1,4,1,8),_FsMIStdOspfv3AreaLsdbAdvertisement_Type())
fsMIStdOspfv3AreaLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbAdvertisement.setStatus(_A)
_FsMIStdOspfv3AreaLsdbTypeKnown_Type=TruthValue
_FsMIStdOspfv3AreaLsdbTypeKnown_Object=MibTableColumn
fsMIStdOspfv3AreaLsdbTypeKnown=_FsMIStdOspfv3AreaLsdbTypeKnown_Object((1,3,6,1,4,1,29601,2,23,1,4,1,9),_FsMIStdOspfv3AreaLsdbTypeKnown_Type())
fsMIStdOspfv3AreaLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaLsdbTypeKnown.setStatus(_A)
_FsMIStdOspfv3LinkLsdbTable_Object=MibTable
fsMIStdOspfv3LinkLsdbTable=_FsMIStdOspfv3LinkLsdbTable_Object((1,3,6,1,4,1,29601,2,23,1,5))
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbTable.setStatus(_A)
_FsMIStdOspfv3LinkLsdbEntry_Object=MibTableRow
fsMIStdOspfv3LinkLsdbEntry=_FsMIStdOspfv3LinkLsdbEntry_Object((1,3,6,1,4,1,29601,2,23,1,5,1))
fsMIStdOspfv3LinkLsdbEntry.setIndexNames((0,_D,_r),(0,_D,_s),(0,_D,_t),(0,_D,_u))
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbEntry.setStatus(_A)
_FsMIStdOspfv3LinkLsdbIfIndex_Type=InterfaceIndex
_FsMIStdOspfv3LinkLsdbIfIndex_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbIfIndex=_FsMIStdOspfv3LinkLsdbIfIndex_Object((1,3,6,1,4,1,29601,2,23,1,5,1,1),_FsMIStdOspfv3LinkLsdbIfIndex_Type())
fsMIStdOspfv3LinkLsdbIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbIfIndex.setStatus(_A)
class _FsMIStdOspfv3LinkLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIStdOspfv3LinkLsdbType_Type.__name__=_J
_FsMIStdOspfv3LinkLsdbType_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbType=_FsMIStdOspfv3LinkLsdbType_Object((1,3,6,1,4,1,29601,2,23,1,5,1,2),_FsMIStdOspfv3LinkLsdbType_Type())
fsMIStdOspfv3LinkLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbType.setStatus(_A)
_FsMIStdOspfv3LinkLsdbRouterId_Type=RouterID
_FsMIStdOspfv3LinkLsdbRouterId_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbRouterId=_FsMIStdOspfv3LinkLsdbRouterId_Object((1,3,6,1,4,1,29601,2,23,1,5,1,3),_FsMIStdOspfv3LinkLsdbRouterId_Type())
fsMIStdOspfv3LinkLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbRouterId.setStatus(_A)
_FsMIStdOspfv3LinkLsdbLsid_Type=IpAddress
_FsMIStdOspfv3LinkLsdbLsid_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbLsid=_FsMIStdOspfv3LinkLsdbLsid_Object((1,3,6,1,4,1,29601,2,23,1,5,1,4),_FsMIStdOspfv3LinkLsdbLsid_Type())
fsMIStdOspfv3LinkLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbLsid.setStatus(_A)
_FsMIStdOspfv3LinkLsdbSequence_Type=Integer32
_FsMIStdOspfv3LinkLsdbSequence_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbSequence=_FsMIStdOspfv3LinkLsdbSequence_Object((1,3,6,1,4,1,29601,2,23,1,5,1,5),_FsMIStdOspfv3LinkLsdbSequence_Type())
fsMIStdOspfv3LinkLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbSequence.setStatus(_A)
_FsMIStdOspfv3LinkLsdbAge_Type=Integer32
_FsMIStdOspfv3LinkLsdbAge_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbAge=_FsMIStdOspfv3LinkLsdbAge_Object((1,3,6,1,4,1,29601,2,23,1,5,1,6),_FsMIStdOspfv3LinkLsdbAge_Type())
fsMIStdOspfv3LinkLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbAge.setUnits(_G)
_FsMIStdOspfv3LinkLsdbChecksum_Type=Integer32
_FsMIStdOspfv3LinkLsdbChecksum_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbChecksum=_FsMIStdOspfv3LinkLsdbChecksum_Object((1,3,6,1,4,1,29601,2,23,1,5,1,7),_FsMIStdOspfv3LinkLsdbChecksum_Type())
fsMIStdOspfv3LinkLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbChecksum.setStatus(_A)
class _FsMIStdOspfv3LinkLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FsMIStdOspfv3LinkLsdbAdvertisement_Type.__name__=_N
_FsMIStdOspfv3LinkLsdbAdvertisement_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbAdvertisement=_FsMIStdOspfv3LinkLsdbAdvertisement_Object((1,3,6,1,4,1,29601,2,23,1,5,1,8),_FsMIStdOspfv3LinkLsdbAdvertisement_Type())
fsMIStdOspfv3LinkLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbAdvertisement.setStatus(_A)
_FsMIStdOspfv3LinkLsdbTypeKnown_Type=TruthValue
_FsMIStdOspfv3LinkLsdbTypeKnown_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbTypeKnown=_FsMIStdOspfv3LinkLsdbTypeKnown_Object((1,3,6,1,4,1,29601,2,23,1,5,1,9),_FsMIStdOspfv3LinkLsdbTypeKnown_Type())
fsMIStdOspfv3LinkLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbTypeKnown.setStatus(_A)
_FsMIStdOspfv3LinkLsdbContextId_Type=Integer32
_FsMIStdOspfv3LinkLsdbContextId_Object=MibTableColumn
fsMIStdOspfv3LinkLsdbContextId=_FsMIStdOspfv3LinkLsdbContextId_Object((1,3,6,1,4,1,29601,2,23,1,5,1,10),_FsMIStdOspfv3LinkLsdbContextId_Type())
fsMIStdOspfv3LinkLsdbContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3LinkLsdbContextId.setStatus(_A)
_FsMIStdOspfv3HostTable_Object=MibTable
fsMIStdOspfv3HostTable=_FsMIStdOspfv3HostTable_Object((1,3,6,1,4,1,29601,2,23,1,6))
if mibBuilder.loadTexts:fsMIStdOspfv3HostTable.setStatus(_A)
_FsMIStdOspfv3HostEntry_Object=MibTableRow
fsMIStdOspfv3HostEntry=_FsMIStdOspfv3HostEntry_Object((1,3,6,1,4,1,29601,2,23,1,6,1))
fsMIStdOspfv3HostEntry.setIndexNames((0,_D,_I),(0,_D,_v),(0,_D,_w))
if mibBuilder.loadTexts:fsMIStdOspfv3HostEntry.setStatus(_A)
_FsMIStdOspfv3HostAddressType_Type=InetAddressType
_FsMIStdOspfv3HostAddressType_Object=MibTableColumn
fsMIStdOspfv3HostAddressType=_FsMIStdOspfv3HostAddressType_Object((1,3,6,1,4,1,29601,2,23,1,6,1,1),_FsMIStdOspfv3HostAddressType_Type())
fsMIStdOspfv3HostAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3HostAddressType.setStatus(_A)
class _FsMIStdOspfv3HostAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdOspfv3HostAddress_Type.__name__=_K
_FsMIStdOspfv3HostAddress_Object=MibTableColumn
fsMIStdOspfv3HostAddress=_FsMIStdOspfv3HostAddress_Object((1,3,6,1,4,1,29601,2,23,1,6,1,2),_FsMIStdOspfv3HostAddress_Type())
fsMIStdOspfv3HostAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3HostAddress.setStatus(_A)
_FsMIStdOspfv3HostMetric_Type=Metric
_FsMIStdOspfv3HostMetric_Object=MibTableColumn
fsMIStdOspfv3HostMetric=_FsMIStdOspfv3HostMetric_Object((1,3,6,1,4,1,29601,2,23,1,6,1,3),_FsMIStdOspfv3HostMetric_Type())
fsMIStdOspfv3HostMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3HostMetric.setStatus(_A)
_FsMIStdOspfv3HostAreaID_Type=AreaID
_FsMIStdOspfv3HostAreaID_Object=MibTableColumn
fsMIStdOspfv3HostAreaID=_FsMIStdOspfv3HostAreaID_Object((1,3,6,1,4,1,29601,2,23,1,6,1,4),_FsMIStdOspfv3HostAreaID_Type())
fsMIStdOspfv3HostAreaID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3HostAreaID.setStatus(_A)
_FsMIStdOspfv3HostStatus_Type=RowStatus
_FsMIStdOspfv3HostStatus_Object=MibTableColumn
fsMIStdOspfv3HostStatus=_FsMIStdOspfv3HostStatus_Object((1,3,6,1,4,1,29601,2,23,1,6,1,5),_FsMIStdOspfv3HostStatus_Type())
fsMIStdOspfv3HostStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3HostStatus.setStatus(_A)
_FsMIStdOspfv3IfTable_Object=MibTable
fsMIStdOspfv3IfTable=_FsMIStdOspfv3IfTable_Object((1,3,6,1,4,1,29601,2,23,1,7))
if mibBuilder.loadTexts:fsMIStdOspfv3IfTable.setStatus(_A)
_FsMIStdOspfv3IfEntry_Object=MibTableRow
fsMIStdOspfv3IfEntry=_FsMIStdOspfv3IfEntry_Object((1,3,6,1,4,1,29601,2,23,1,7,1))
fsMIStdOspfv3IfEntry.setIndexNames((0,_D,_x))
if mibBuilder.loadTexts:fsMIStdOspfv3IfEntry.setStatus(_A)
_FsMIStdOspfv3IfIndex_Type=InterfaceIndex
_FsMIStdOspfv3IfIndex_Object=MibTableColumn
fsMIStdOspfv3IfIndex=_FsMIStdOspfv3IfIndex_Object((1,3,6,1,4,1,29601,2,23,1,7,1,1),_FsMIStdOspfv3IfIndex_Type())
fsMIStdOspfv3IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3IfIndex.setStatus(_A)
class _FsMIStdOspfv3IfAreaId_Type(AreaID):defaultHexValue='00000000'
_FsMIStdOspfv3IfAreaId_Type.__name__=_g
_FsMIStdOspfv3IfAreaId_Object=MibTableColumn
fsMIStdOspfv3IfAreaId=_FsMIStdOspfv3IfAreaId_Object((1,3,6,1,4,1,29601,2,23,1,7,1,2),_FsMIStdOspfv3IfAreaId_Type())
fsMIStdOspfv3IfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfAreaId.setStatus(_A)
class _FsMIStdOspfv3IfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_W,3),('pointToMultipoint',5)))
_FsMIStdOspfv3IfType_Type.__name__=_F
_FsMIStdOspfv3IfType_Object=MibTableColumn
fsMIStdOspfv3IfType=_FsMIStdOspfv3IfType_Object((1,3,6,1,4,1,29601,2,23,1,7,1,3),_FsMIStdOspfv3IfType_Type())
fsMIStdOspfv3IfType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfType.setStatus(_A)
class _FsMIStdOspfv3IfAdminStat_Type(Status):defaultValue=1
_FsMIStdOspfv3IfAdminStat_Type.__name__=_h
_FsMIStdOspfv3IfAdminStat_Object=MibTableColumn
fsMIStdOspfv3IfAdminStat=_FsMIStdOspfv3IfAdminStat_Object((1,3,6,1,4,1,29601,2,23,1,7,1,4),_FsMIStdOspfv3IfAdminStat_Type())
fsMIStdOspfv3IfAdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfAdminStat.setStatus(_A)
class _FsMIStdOspfv3IfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_FsMIStdOspfv3IfRtrPriority_Type.__name__=_P
_FsMIStdOspfv3IfRtrPriority_Object=MibTableColumn
fsMIStdOspfv3IfRtrPriority=_FsMIStdOspfv3IfRtrPriority_Object((1,3,6,1,4,1,29601,2,23,1,7,1,5),_FsMIStdOspfv3IfRtrPriority_Type())
fsMIStdOspfv3IfRtrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfRtrPriority.setStatus(_A)
class _FsMIStdOspfv3IfTransitDelay_Type(UpToRefreshInterval):defaultValue=1
_FsMIStdOspfv3IfTransitDelay_Type.__name__=_L
_FsMIStdOspfv3IfTransitDelay_Object=MibTableColumn
fsMIStdOspfv3IfTransitDelay=_FsMIStdOspfv3IfTransitDelay_Object((1,3,6,1,4,1,29601,2,23,1,7,1,6),_FsMIStdOspfv3IfTransitDelay_Type())
fsMIStdOspfv3IfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfTransitDelay.setUnits(_G)
class _FsMIStdOspfv3IfRetransInterval_Type(UpToRefreshInterval):defaultValue=5
_FsMIStdOspfv3IfRetransInterval_Type.__name__=_L
_FsMIStdOspfv3IfRetransInterval_Object=MibTableColumn
fsMIStdOspfv3IfRetransInterval=_FsMIStdOspfv3IfRetransInterval_Object((1,3,6,1,4,1,29601,2,23,1,7,1,7),_FsMIStdOspfv3IfRetransInterval_Type())
fsMIStdOspfv3IfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfRetransInterval.setUnits(_G)
class _FsMIStdOspfv3IfHelloInterval_Type(HelloRange):defaultValue=10
_FsMIStdOspfv3IfHelloInterval_Type.__name__=_Q
_FsMIStdOspfv3IfHelloInterval_Object=MibTableColumn
fsMIStdOspfv3IfHelloInterval=_FsMIStdOspfv3IfHelloInterval_Object((1,3,6,1,4,1,29601,2,23,1,7,1,8),_FsMIStdOspfv3IfHelloInterval_Type())
fsMIStdOspfv3IfHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfHelloInterval.setUnits(_G)
class _FsMIStdOspfv3IfRtrDeadInterval_Type(RouterDeadRange):defaultValue=40
_FsMIStdOspfv3IfRtrDeadInterval_Type.__name__=_X
_FsMIStdOspfv3IfRtrDeadInterval_Object=MibTableColumn
fsMIStdOspfv3IfRtrDeadInterval=_FsMIStdOspfv3IfRtrDeadInterval_Object((1,3,6,1,4,1,29601,2,23,1,7,1,9),_FsMIStdOspfv3IfRtrDeadInterval_Type())
fsMIStdOspfv3IfRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfRtrDeadInterval.setUnits(_G)
class _FsMIStdOspfv3IfPollInterval_Type(Unsigned32):defaultValue=120
_FsMIStdOspfv3IfPollInterval_Type.__name__=_J
_FsMIStdOspfv3IfPollInterval_Object=MibTableColumn
fsMIStdOspfv3IfPollInterval=_FsMIStdOspfv3IfPollInterval_Object((1,3,6,1,4,1,29601,2,23,1,7,1,10),_FsMIStdOspfv3IfPollInterval_Type())
fsMIStdOspfv3IfPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfPollInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfPollInterval.setUnits(_G)
class _FsMIStdOspfv3IfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('loopback',2),('waiting',3),(_W,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7),('standbyOnLink',8)))
_FsMIStdOspfv3IfState_Type.__name__=_F
_FsMIStdOspfv3IfState_Object=MibTableColumn
fsMIStdOspfv3IfState=_FsMIStdOspfv3IfState_Object((1,3,6,1,4,1,29601,2,23,1,7,1,11),_FsMIStdOspfv3IfState_Type())
fsMIStdOspfv3IfState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfState.setStatus(_A)
_FsMIStdOspfv3IfDesignatedRouter_Type=RouterID
_FsMIStdOspfv3IfDesignatedRouter_Object=MibTableColumn
fsMIStdOspfv3IfDesignatedRouter=_FsMIStdOspfv3IfDesignatedRouter_Object((1,3,6,1,4,1,29601,2,23,1,7,1,12),_FsMIStdOspfv3IfDesignatedRouter_Type())
fsMIStdOspfv3IfDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDesignatedRouter.setStatus(_A)
_FsMIStdOspfv3IfBackupDesignatedRouter_Type=RouterID
_FsMIStdOspfv3IfBackupDesignatedRouter_Object=MibTableColumn
fsMIStdOspfv3IfBackupDesignatedRouter=_FsMIStdOspfv3IfBackupDesignatedRouter_Object((1,3,6,1,4,1,29601,2,23,1,7,1,13),_FsMIStdOspfv3IfBackupDesignatedRouter_Type())
fsMIStdOspfv3IfBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfBackupDesignatedRouter.setStatus(_A)
_FsMIStdOspfv3IfEvents_Type=Counter32
_FsMIStdOspfv3IfEvents_Object=MibTableColumn
fsMIStdOspfv3IfEvents=_FsMIStdOspfv3IfEvents_Object((1,3,6,1,4,1,29601,2,23,1,7,1,14),_FsMIStdOspfv3IfEvents_Type())
fsMIStdOspfv3IfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfEvents.setStatus(_A)
class _FsMIStdOspfv3IfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_FsMIStdOspfv3IfMulticastForwarding_Type.__name__=_F
_FsMIStdOspfv3IfMulticastForwarding_Object=MibTableColumn
fsMIStdOspfv3IfMulticastForwarding=_FsMIStdOspfv3IfMulticastForwarding_Object((1,3,6,1,4,1,29601,2,23,1,7,1,15),_FsMIStdOspfv3IfMulticastForwarding_Type())
fsMIStdOspfv3IfMulticastForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfMulticastForwarding.setStatus(_A)
class _FsMIStdOspfv3IfDemand_Type(TruthValue):defaultValue=2
_FsMIStdOspfv3IfDemand_Type.__name__=_R
_FsMIStdOspfv3IfDemand_Object=MibTableColumn
fsMIStdOspfv3IfDemand=_FsMIStdOspfv3IfDemand_Object((1,3,6,1,4,1,29601,2,23,1,7,1,16),_FsMIStdOspfv3IfDemand_Type())
fsMIStdOspfv3IfDemand.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDemand.setStatus(_A)
_FsMIStdOspfv3IfMetricValue_Type=Metric
_FsMIStdOspfv3IfMetricValue_Object=MibTableColumn
fsMIStdOspfv3IfMetricValue=_FsMIStdOspfv3IfMetricValue_Object((1,3,6,1,4,1,29601,2,23,1,7,1,17),_FsMIStdOspfv3IfMetricValue_Type())
fsMIStdOspfv3IfMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfMetricValue.setStatus(_A)
_FsMIStdOspfv3IfLinkScopeLsaCount_Type=Gauge32
_FsMIStdOspfv3IfLinkScopeLsaCount_Object=MibTableColumn
fsMIStdOspfv3IfLinkScopeLsaCount=_FsMIStdOspfv3IfLinkScopeLsaCount_Object((1,3,6,1,4,1,29601,2,23,1,7,1,18),_FsMIStdOspfv3IfLinkScopeLsaCount_Type())
fsMIStdOspfv3IfLinkScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfLinkScopeLsaCount.setStatus(_A)
_FsMIStdOspfv3IfLinkLsaCksumSum_Type=Integer32
_FsMIStdOspfv3IfLinkLsaCksumSum_Object=MibTableColumn
fsMIStdOspfv3IfLinkLsaCksumSum=_FsMIStdOspfv3IfLinkLsaCksumSum_Object((1,3,6,1,4,1,29601,2,23,1,7,1,19),_FsMIStdOspfv3IfLinkLsaCksumSum_Type())
fsMIStdOspfv3IfLinkLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfLinkLsaCksumSum.setStatus(_A)
class _FsMIStdOspfv3IfInstId_Type(Integer32):defaultValue=0
_FsMIStdOspfv3IfInstId_Type.__name__=_F
_FsMIStdOspfv3IfInstId_Object=MibTableColumn
fsMIStdOspfv3IfInstId=_FsMIStdOspfv3IfInstId_Object((1,3,6,1,4,1,29601,2,23,1,7,1,20),_FsMIStdOspfv3IfInstId_Type())
fsMIStdOspfv3IfInstId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfInstId.setStatus(_A)
class _FsMIStdOspfv3IfDemandNbrProbe_Type(TruthValue):defaultValue=2
_FsMIStdOspfv3IfDemandNbrProbe_Type.__name__=_R
_FsMIStdOspfv3IfDemandNbrProbe_Object=MibTableColumn
fsMIStdOspfv3IfDemandNbrProbe=_FsMIStdOspfv3IfDemandNbrProbe_Object((1,3,6,1,4,1,29601,2,23,1,7,1,21),_FsMIStdOspfv3IfDemandNbrProbe_Type())
fsMIStdOspfv3IfDemandNbrProbe.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDemandNbrProbe.setStatus(_A)
class _FsMIStdOspfv3IfDemandNbrProbeRetxLimit_Type(Unsigned32):defaultValue=10
_FsMIStdOspfv3IfDemandNbrProbeRetxLimit_Type.__name__=_J
_FsMIStdOspfv3IfDemandNbrProbeRetxLimit_Object=MibTableColumn
fsMIStdOspfv3IfDemandNbrProbeRetxLimit=_FsMIStdOspfv3IfDemandNbrProbeRetxLimit_Object((1,3,6,1,4,1,29601,2,23,1,7,1,22),_FsMIStdOspfv3IfDemandNbrProbeRetxLimit_Type())
fsMIStdOspfv3IfDemandNbrProbeRetxLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDemandNbrProbeRetxLimit.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDemandNbrProbeRetxLimit.setUnits(_G)
class _FsMIStdOspfv3IfDemandNbrProbeInterval_Type(Unsigned32):defaultValue=120
_FsMIStdOspfv3IfDemandNbrProbeInterval_Type.__name__=_J
_FsMIStdOspfv3IfDemandNbrProbeInterval_Object=MibTableColumn
fsMIStdOspfv3IfDemandNbrProbeInterval=_FsMIStdOspfv3IfDemandNbrProbeInterval_Object((1,3,6,1,4,1,29601,2,23,1,7,1,23),_FsMIStdOspfv3IfDemandNbrProbeInterval_Type())
fsMIStdOspfv3IfDemandNbrProbeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDemandNbrProbeInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3IfDemandNbrProbeInterval.setUnits(_G)
_FsMIStdOspfv3IfContextId_Type=Integer32
_FsMIStdOspfv3IfContextId_Object=MibTableColumn
fsMIStdOspfv3IfContextId=_FsMIStdOspfv3IfContextId_Object((1,3,6,1,4,1,29601,2,23,1,7,1,24),_FsMIStdOspfv3IfContextId_Type())
fsMIStdOspfv3IfContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3IfContextId.setStatus(_A)
_FsMIStdOspfv3IfStatus_Type=RowStatus
_FsMIStdOspfv3IfStatus_Object=MibTableColumn
fsMIStdOspfv3IfStatus=_FsMIStdOspfv3IfStatus_Object((1,3,6,1,4,1,29601,2,23,1,7,1,25),_FsMIStdOspfv3IfStatus_Type())
fsMIStdOspfv3IfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3IfStatus.setStatus(_A)
_FsMIStdOspfv3VirtIfTable_Object=MibTable
fsMIStdOspfv3VirtIfTable=_FsMIStdOspfv3VirtIfTable_Object((1,3,6,1,4,1,29601,2,23,1,8))
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfTable.setStatus(_A)
_FsMIStdOspfv3VirtIfEntry_Object=MibTableRow
fsMIStdOspfv3VirtIfEntry=_FsMIStdOspfv3VirtIfEntry_Object((1,3,6,1,4,1,29601,2,23,1,8,1))
fsMIStdOspfv3VirtIfEntry.setIndexNames((0,_D,_I),(0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfEntry.setStatus(_A)
_FsMIStdOspfv3VirtIfAreaId_Type=AreaID
_FsMIStdOspfv3VirtIfAreaId_Object=MibTableColumn
fsMIStdOspfv3VirtIfAreaId=_FsMIStdOspfv3VirtIfAreaId_Object((1,3,6,1,4,1,29601,2,23,1,8,1,1),_FsMIStdOspfv3VirtIfAreaId_Type())
fsMIStdOspfv3VirtIfAreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfAreaId.setStatus(_A)
_FsMIStdOspfv3VirtIfNeighbor_Type=RouterID
_FsMIStdOspfv3VirtIfNeighbor_Object=MibTableColumn
fsMIStdOspfv3VirtIfNeighbor=_FsMIStdOspfv3VirtIfNeighbor_Object((1,3,6,1,4,1,29601,2,23,1,8,1,2),_FsMIStdOspfv3VirtIfNeighbor_Type())
fsMIStdOspfv3VirtIfNeighbor.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfNeighbor.setStatus(_A)
_FsMIStdOspfv3VirtIfIndex_Type=InterfaceIndex
_FsMIStdOspfv3VirtIfIndex_Object=MibTableColumn
fsMIStdOspfv3VirtIfIndex=_FsMIStdOspfv3VirtIfIndex_Object((1,3,6,1,4,1,29601,2,23,1,8,1,3),_FsMIStdOspfv3VirtIfIndex_Type())
fsMIStdOspfv3VirtIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfIndex.setStatus(_A)
class _FsMIStdOspfv3VirtIfTransitDelay_Type(UpToRefreshInterval):defaultValue=1
_FsMIStdOspfv3VirtIfTransitDelay_Type.__name__=_L
_FsMIStdOspfv3VirtIfTransitDelay_Object=MibTableColumn
fsMIStdOspfv3VirtIfTransitDelay=_FsMIStdOspfv3VirtIfTransitDelay_Object((1,3,6,1,4,1,29601,2,23,1,8,1,4),_FsMIStdOspfv3VirtIfTransitDelay_Type())
fsMIStdOspfv3VirtIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfTransitDelay.setUnits(_G)
class _FsMIStdOspfv3VirtIfRetransInterval_Type(UpToRefreshInterval):defaultValue=5
_FsMIStdOspfv3VirtIfRetransInterval_Type.__name__=_L
_FsMIStdOspfv3VirtIfRetransInterval_Object=MibTableColumn
fsMIStdOspfv3VirtIfRetransInterval=_FsMIStdOspfv3VirtIfRetransInterval_Object((1,3,6,1,4,1,29601,2,23,1,8,1,5),_FsMIStdOspfv3VirtIfRetransInterval_Type())
fsMIStdOspfv3VirtIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfRetransInterval.setUnits(_G)
class _FsMIStdOspfv3VirtIfHelloInterval_Type(HelloRange):defaultValue=10
_FsMIStdOspfv3VirtIfHelloInterval_Type.__name__=_Q
_FsMIStdOspfv3VirtIfHelloInterval_Object=MibTableColumn
fsMIStdOspfv3VirtIfHelloInterval=_FsMIStdOspfv3VirtIfHelloInterval_Object((1,3,6,1,4,1,29601,2,23,1,8,1,6),_FsMIStdOspfv3VirtIfHelloInterval_Type())
fsMIStdOspfv3VirtIfHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfHelloInterval.setUnits(_G)
class _FsMIStdOspfv3VirtIfRtrDeadInterval_Type(RouterDeadRange):defaultValue=60
_FsMIStdOspfv3VirtIfRtrDeadInterval_Type.__name__=_X
_FsMIStdOspfv3VirtIfRtrDeadInterval_Object=MibTableColumn
fsMIStdOspfv3VirtIfRtrDeadInterval=_FsMIStdOspfv3VirtIfRtrDeadInterval_Object((1,3,6,1,4,1,29601,2,23,1,8,1,7),_FsMIStdOspfv3VirtIfRtrDeadInterval_Type())
fsMIStdOspfv3VirtIfRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfRtrDeadInterval.setUnits(_G)
class _FsMIStdOspfv3VirtIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_M,1),(_W,4)))
_FsMIStdOspfv3VirtIfState_Type.__name__=_F
_FsMIStdOspfv3VirtIfState_Object=MibTableColumn
fsMIStdOspfv3VirtIfState=_FsMIStdOspfv3VirtIfState_Object((1,3,6,1,4,1,29601,2,23,1,8,1,8),_FsMIStdOspfv3VirtIfState_Type())
fsMIStdOspfv3VirtIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfState.setStatus(_A)
_FsMIStdOspfv3VirtIfEvents_Type=Counter32
_FsMIStdOspfv3VirtIfEvents_Object=MibTableColumn
fsMIStdOspfv3VirtIfEvents=_FsMIStdOspfv3VirtIfEvents_Object((1,3,6,1,4,1,29601,2,23,1,8,1,9),_FsMIStdOspfv3VirtIfEvents_Type())
fsMIStdOspfv3VirtIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfEvents.setStatus(_A)
_FsMIStdOspfv3VirtIfLinkScopeLsaCount_Type=Gauge32
_FsMIStdOspfv3VirtIfLinkScopeLsaCount_Object=MibTableColumn
fsMIStdOspfv3VirtIfLinkScopeLsaCount=_FsMIStdOspfv3VirtIfLinkScopeLsaCount_Object((1,3,6,1,4,1,29601,2,23,1,8,1,10),_FsMIStdOspfv3VirtIfLinkScopeLsaCount_Type())
fsMIStdOspfv3VirtIfLinkScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfLinkScopeLsaCount.setStatus(_A)
_FsMIStdOspfv3VirtIfLinkLsaCksumSum_Type=Integer32
_FsMIStdOspfv3VirtIfLinkLsaCksumSum_Object=MibTableColumn
fsMIStdOspfv3VirtIfLinkLsaCksumSum=_FsMIStdOspfv3VirtIfLinkLsaCksumSum_Object((1,3,6,1,4,1,29601,2,23,1,8,1,11),_FsMIStdOspfv3VirtIfLinkLsaCksumSum_Type())
fsMIStdOspfv3VirtIfLinkLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfLinkLsaCksumSum.setStatus(_A)
_FsMIStdOspfv3VirtIfStatus_Type=RowStatus
_FsMIStdOspfv3VirtIfStatus_Object=MibTableColumn
fsMIStdOspfv3VirtIfStatus=_FsMIStdOspfv3VirtIfStatus_Object((1,3,6,1,4,1,29601,2,23,1,8,1,12),_FsMIStdOspfv3VirtIfStatus_Type())
fsMIStdOspfv3VirtIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtIfStatus.setStatus(_A)
_FsMIStdOspfv3NbrTable_Object=MibTable
fsMIStdOspfv3NbrTable=_FsMIStdOspfv3NbrTable_Object((1,3,6,1,4,1,29601,2,23,1,9))
if mibBuilder.loadTexts:fsMIStdOspfv3NbrTable.setStatus(_A)
_FsMIStdOspfv3NbrEntry_Object=MibTableRow
fsMIStdOspfv3NbrEntry=_FsMIStdOspfv3NbrEntry_Object((1,3,6,1,4,1,29601,2,23,1,9,1))
fsMIStdOspfv3NbrEntry.setIndexNames((0,_D,_A0),(0,_D,_A1))
if mibBuilder.loadTexts:fsMIStdOspfv3NbrEntry.setStatus(_A)
_FsMIStdOspfv3NbrIfIndex_Type=InterfaceIndex
_FsMIStdOspfv3NbrIfIndex_Object=MibTableColumn
fsMIStdOspfv3NbrIfIndex=_FsMIStdOspfv3NbrIfIndex_Object((1,3,6,1,4,1,29601,2,23,1,9,1,1),_FsMIStdOspfv3NbrIfIndex_Type())
fsMIStdOspfv3NbrIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrIfIndex.setStatus(_A)
_FsMIStdOspfv3NbrRtrId_Type=RouterID
_FsMIStdOspfv3NbrRtrId_Object=MibTableColumn
fsMIStdOspfv3NbrRtrId=_FsMIStdOspfv3NbrRtrId_Object((1,3,6,1,4,1,29601,2,23,1,9,1,2),_FsMIStdOspfv3NbrRtrId_Type())
fsMIStdOspfv3NbrRtrId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrRtrId.setStatus(_A)
_FsMIStdOspfv3NbrAddressType_Type=InetAddressType
_FsMIStdOspfv3NbrAddressType_Object=MibTableColumn
fsMIStdOspfv3NbrAddressType=_FsMIStdOspfv3NbrAddressType_Object((1,3,6,1,4,1,29601,2,23,1,9,1,3),_FsMIStdOspfv3NbrAddressType_Type())
fsMIStdOspfv3NbrAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrAddressType.setStatus(_A)
class _FsMIStdOspfv3NbrAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdOspfv3NbrAddress_Type.__name__=_K
_FsMIStdOspfv3NbrAddress_Object=MibTableColumn
fsMIStdOspfv3NbrAddress=_FsMIStdOspfv3NbrAddress_Object((1,3,6,1,4,1,29601,2,23,1,9,1,4),_FsMIStdOspfv3NbrAddress_Type())
fsMIStdOspfv3NbrAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrAddress.setStatus(_A)
_FsMIStdOspfv3NbrOptions_Type=Integer32
_FsMIStdOspfv3NbrOptions_Object=MibTableColumn
fsMIStdOspfv3NbrOptions=_FsMIStdOspfv3NbrOptions_Object((1,3,6,1,4,1,29601,2,23,1,9,1,5),_FsMIStdOspfv3NbrOptions_Type())
fsMIStdOspfv3NbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrOptions.setStatus(_A)
_FsMIStdOspfv3NbrPriority_Type=DesignatedRouterPriority
_FsMIStdOspfv3NbrPriority_Object=MibTableColumn
fsMIStdOspfv3NbrPriority=_FsMIStdOspfv3NbrPriority_Object((1,3,6,1,4,1,29601,2,23,1,9,1,6),_FsMIStdOspfv3NbrPriority_Type())
fsMIStdOspfv3NbrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrPriority.setStatus(_A)
class _FsMIStdOspfv3NbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_c,6),(_d,7),(_e,8)))
_FsMIStdOspfv3NbrState_Type.__name__=_F
_FsMIStdOspfv3NbrState_Object=MibTableColumn
fsMIStdOspfv3NbrState=_FsMIStdOspfv3NbrState_Object((1,3,6,1,4,1,29601,2,23,1,9,1,7),_FsMIStdOspfv3NbrState_Type())
fsMIStdOspfv3NbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrState.setStatus(_A)
_FsMIStdOspfv3NbrEvents_Type=Counter32
_FsMIStdOspfv3NbrEvents_Object=MibTableColumn
fsMIStdOspfv3NbrEvents=_FsMIStdOspfv3NbrEvents_Object((1,3,6,1,4,1,29601,2,23,1,9,1,8),_FsMIStdOspfv3NbrEvents_Type())
fsMIStdOspfv3NbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrEvents.setStatus(_A)
_FsMIStdOspfv3NbrLsRetransQLen_Type=Gauge32
_FsMIStdOspfv3NbrLsRetransQLen_Object=MibTableColumn
fsMIStdOspfv3NbrLsRetransQLen=_FsMIStdOspfv3NbrLsRetransQLen_Object((1,3,6,1,4,1,29601,2,23,1,9,1,9),_FsMIStdOspfv3NbrLsRetransQLen_Type())
fsMIStdOspfv3NbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrLsRetransQLen.setStatus(_A)
_FsMIStdOspfv3NbrHelloSuppressed_Type=TruthValue
_FsMIStdOspfv3NbrHelloSuppressed_Object=MibTableColumn
fsMIStdOspfv3NbrHelloSuppressed=_FsMIStdOspfv3NbrHelloSuppressed_Object((1,3,6,1,4,1,29601,2,23,1,9,1,10),_FsMIStdOspfv3NbrHelloSuppressed_Type())
fsMIStdOspfv3NbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrHelloSuppressed.setStatus(_A)
_FsMIStdOspfv3NbrIfId_Type=InterfaceIndex
_FsMIStdOspfv3NbrIfId_Object=MibTableColumn
fsMIStdOspfv3NbrIfId=_FsMIStdOspfv3NbrIfId_Object((1,3,6,1,4,1,29601,2,23,1,9,1,11),_FsMIStdOspfv3NbrIfId_Type())
fsMIStdOspfv3NbrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrIfId.setStatus(_A)
class _FsMIStdOspfv3NbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),('helping',2)))
_FsMIStdOspfv3NbrRestartHelperStatus_Type.__name__=_F
_FsMIStdOspfv3NbrRestartHelperStatus_Object=MibTableColumn
fsMIStdOspfv3NbrRestartHelperStatus=_FsMIStdOspfv3NbrRestartHelperStatus_Object((1,3,6,1,4,1,29601,2,23,1,9,1,12),_FsMIStdOspfv3NbrRestartHelperStatus_Type())
fsMIStdOspfv3NbrRestartHelperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrRestartHelperStatus.setStatus(_A)
_FsMIStdOspfv3NbrRestartHelperAge_Type=UpToRefreshInterval
_FsMIStdOspfv3NbrRestartHelperAge_Object=MibTableColumn
fsMIStdOspfv3NbrRestartHelperAge=_FsMIStdOspfv3NbrRestartHelperAge_Object((1,3,6,1,4,1,29601,2,23,1,9,1,13),_FsMIStdOspfv3NbrRestartHelperAge_Type())
fsMIStdOspfv3NbrRestartHelperAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrRestartHelperAge.setUnits(_G)
class _FsMIStdOspfv3NbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_FsMIStdOspfv3NbrRestartHelperExitReason_Type.__name__=_F
_FsMIStdOspfv3NbrRestartHelperExitReason_Object=MibTableColumn
fsMIStdOspfv3NbrRestartHelperExitReason=_FsMIStdOspfv3NbrRestartHelperExitReason_Object((1,3,6,1,4,1,29601,2,23,1,9,1,14),_FsMIStdOspfv3NbrRestartHelperExitReason_Type())
fsMIStdOspfv3NbrRestartHelperExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrRestartHelperExitReason.setStatus(_A)
_FsMIStdOspfv3NbrContextId_Type=Integer32
_FsMIStdOspfv3NbrContextId_Object=MibTableColumn
fsMIStdOspfv3NbrContextId=_FsMIStdOspfv3NbrContextId_Object((1,3,6,1,4,1,29601,2,23,1,9,1,15),_FsMIStdOspfv3NbrContextId_Type())
fsMIStdOspfv3NbrContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbrContextId.setStatus(_A)
_FsMIStdOspfv3NbmaNbrTable_Object=MibTable
fsMIStdOspfv3NbmaNbrTable=_FsMIStdOspfv3NbmaNbrTable_Object((1,3,6,1,4,1,29601,2,23,1,10))
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrTable.setStatus(_A)
_FsMIStdOspfv3NbmaNbrEntry_Object=MibTableRow
fsMIStdOspfv3NbmaNbrEntry=_FsMIStdOspfv3NbmaNbrEntry_Object((1,3,6,1,4,1,29601,2,23,1,10,1))
fsMIStdOspfv3NbmaNbrEntry.setIndexNames((0,_D,_A3),(0,_D,_A4),(0,_D,_A5))
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrEntry.setStatus(_A)
_FsMIStdOspfv3NbmaNbrIfIndex_Type=InterfaceIndex
_FsMIStdOspfv3NbmaNbrIfIndex_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrIfIndex=_FsMIStdOspfv3NbmaNbrIfIndex_Object((1,3,6,1,4,1,29601,2,23,1,10,1,1),_FsMIStdOspfv3NbmaNbrIfIndex_Type())
fsMIStdOspfv3NbmaNbrIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrIfIndex.setStatus(_A)
_FsMIStdOspfv3NbmaNbrAddressType_Type=InetAddressType
_FsMIStdOspfv3NbmaNbrAddressType_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrAddressType=_FsMIStdOspfv3NbmaNbrAddressType_Object((1,3,6,1,4,1,29601,2,23,1,10,1,2),_FsMIStdOspfv3NbmaNbrAddressType_Type())
fsMIStdOspfv3NbmaNbrAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrAddressType.setStatus(_A)
class _FsMIStdOspfv3NbmaNbrAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdOspfv3NbmaNbrAddress_Type.__name__=_K
_FsMIStdOspfv3NbmaNbrAddress_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrAddress=_FsMIStdOspfv3NbmaNbrAddress_Object((1,3,6,1,4,1,29601,2,23,1,10,1,3),_FsMIStdOspfv3NbmaNbrAddress_Type())
fsMIStdOspfv3NbmaNbrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrAddress.setStatus(_A)
class _FsMIStdOspfv3NbmaNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_FsMIStdOspfv3NbmaNbrPriority_Type.__name__=_P
_FsMIStdOspfv3NbmaNbrPriority_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrPriority=_FsMIStdOspfv3NbmaNbrPriority_Object((1,3,6,1,4,1,29601,2,23,1,10,1,4),_FsMIStdOspfv3NbmaNbrPriority_Type())
fsMIStdOspfv3NbmaNbrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrPriority.setStatus(_A)
_FsMIStdOspfv3NbmaNbrRtrId_Type=RouterID
_FsMIStdOspfv3NbmaNbrRtrId_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrRtrId=_FsMIStdOspfv3NbmaNbrRtrId_Object((1,3,6,1,4,1,29601,2,23,1,10,1,5),_FsMIStdOspfv3NbmaNbrRtrId_Type())
fsMIStdOspfv3NbmaNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrRtrId.setStatus(_A)
class _FsMIStdOspfv3NbmaNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_c,6),(_d,7),(_e,8)))
_FsMIStdOspfv3NbmaNbrState_Type.__name__=_F
_FsMIStdOspfv3NbmaNbrState_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrState=_FsMIStdOspfv3NbmaNbrState_Object((1,3,6,1,4,1,29601,2,23,1,10,1,6),_FsMIStdOspfv3NbmaNbrState_Type())
fsMIStdOspfv3NbmaNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrState.setStatus(_A)
class _FsMIStdOspfv3NbmaNbrStorageType_Type(StorageType):defaultValue=3
_FsMIStdOspfv3NbmaNbrStorageType_Type.__name__=_i
_FsMIStdOspfv3NbmaNbrStorageType_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrStorageType=_FsMIStdOspfv3NbmaNbrStorageType_Object((1,3,6,1,4,1,29601,2,23,1,10,1,7),_FsMIStdOspfv3NbmaNbrStorageType_Type())
fsMIStdOspfv3NbmaNbrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrStorageType.setStatus(_A)
_FsMIStdOspfv3NbmaNbrContextId_Type=Integer32
_FsMIStdOspfv3NbmaNbrContextId_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrContextId=_FsMIStdOspfv3NbmaNbrContextId_Object((1,3,6,1,4,1,29601,2,23,1,10,1,8),_FsMIStdOspfv3NbmaNbrContextId_Type())
fsMIStdOspfv3NbmaNbrContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrContextId.setStatus(_A)
_FsMIStdOspfv3NbmaNbrStatus_Type=RowStatus
_FsMIStdOspfv3NbmaNbrStatus_Object=MibTableColumn
fsMIStdOspfv3NbmaNbrStatus=_FsMIStdOspfv3NbmaNbrStatus_Object((1,3,6,1,4,1,29601,2,23,1,10,1,9),_FsMIStdOspfv3NbmaNbrStatus_Type())
fsMIStdOspfv3NbmaNbrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3NbmaNbrStatus.setStatus(_A)
_FsMIStdOspfv3VirtNbrTable_Object=MibTable
fsMIStdOspfv3VirtNbrTable=_FsMIStdOspfv3VirtNbrTable_Object((1,3,6,1,4,1,29601,2,23,1,11))
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrTable.setStatus(_A)
_FsMIStdOspfv3VirtNbrEntry_Object=MibTableRow
fsMIStdOspfv3VirtNbrEntry=_FsMIStdOspfv3VirtNbrEntry_Object((1,3,6,1,4,1,29601,2,23,1,11,1))
fsMIStdOspfv3VirtNbrEntry.setIndexNames((0,_D,_I),(0,_D,_A6),(0,_D,_A7))
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrEntry.setStatus(_A)
_FsMIStdOspfv3VirtNbrArea_Type=AreaID
_FsMIStdOspfv3VirtNbrArea_Object=MibTableColumn
fsMIStdOspfv3VirtNbrArea=_FsMIStdOspfv3VirtNbrArea_Object((1,3,6,1,4,1,29601,2,23,1,11,1,1),_FsMIStdOspfv3VirtNbrArea_Type())
fsMIStdOspfv3VirtNbrArea.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrArea.setStatus(_A)
_FsMIStdOspfv3VirtNbrRtrId_Type=RouterID
_FsMIStdOspfv3VirtNbrRtrId_Object=MibTableColumn
fsMIStdOspfv3VirtNbrRtrId=_FsMIStdOspfv3VirtNbrRtrId_Object((1,3,6,1,4,1,29601,2,23,1,11,1,2),_FsMIStdOspfv3VirtNbrRtrId_Type())
fsMIStdOspfv3VirtNbrRtrId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrRtrId.setStatus(_A)
_FsMIStdOspfv3VirtNbrIfIndex_Type=InterfaceIndex
_FsMIStdOspfv3VirtNbrIfIndex_Object=MibTableColumn
fsMIStdOspfv3VirtNbrIfIndex=_FsMIStdOspfv3VirtNbrIfIndex_Object((1,3,6,1,4,1,29601,2,23,1,11,1,3),_FsMIStdOspfv3VirtNbrIfIndex_Type())
fsMIStdOspfv3VirtNbrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrIfIndex.setStatus(_A)
_FsMIStdOspfv3VirtNbrAddressType_Type=InetAddressType
_FsMIStdOspfv3VirtNbrAddressType_Object=MibTableColumn
fsMIStdOspfv3VirtNbrAddressType=_FsMIStdOspfv3VirtNbrAddressType_Object((1,3,6,1,4,1,29601,2,23,1,11,1,4),_FsMIStdOspfv3VirtNbrAddressType_Type())
fsMIStdOspfv3VirtNbrAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrAddressType.setStatus(_A)
class _FsMIStdOspfv3VirtNbrAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdOspfv3VirtNbrAddress_Type.__name__=_K
_FsMIStdOspfv3VirtNbrAddress_Object=MibTableColumn
fsMIStdOspfv3VirtNbrAddress=_FsMIStdOspfv3VirtNbrAddress_Object((1,3,6,1,4,1,29601,2,23,1,11,1,5),_FsMIStdOspfv3VirtNbrAddress_Type())
fsMIStdOspfv3VirtNbrAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrAddress.setStatus(_A)
_FsMIStdOspfv3VirtNbrOptions_Type=Integer32
_FsMIStdOspfv3VirtNbrOptions_Object=MibTableColumn
fsMIStdOspfv3VirtNbrOptions=_FsMIStdOspfv3VirtNbrOptions_Object((1,3,6,1,4,1,29601,2,23,1,11,1,6),_FsMIStdOspfv3VirtNbrOptions_Type())
fsMIStdOspfv3VirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrOptions.setStatus(_A)
class _FsMIStdOspfv3VirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_c,6),(_d,7),(_e,8)))
_FsMIStdOspfv3VirtNbrState_Type.__name__=_F
_FsMIStdOspfv3VirtNbrState_Object=MibTableColumn
fsMIStdOspfv3VirtNbrState=_FsMIStdOspfv3VirtNbrState_Object((1,3,6,1,4,1,29601,2,23,1,11,1,7),_FsMIStdOspfv3VirtNbrState_Type())
fsMIStdOspfv3VirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrState.setStatus(_A)
_FsMIStdOspfv3VirtNbrEvents_Type=Counter32
_FsMIStdOspfv3VirtNbrEvents_Object=MibTableColumn
fsMIStdOspfv3VirtNbrEvents=_FsMIStdOspfv3VirtNbrEvents_Object((1,3,6,1,4,1,29601,2,23,1,11,1,8),_FsMIStdOspfv3VirtNbrEvents_Type())
fsMIStdOspfv3VirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrEvents.setStatus(_A)
_FsMIStdOspfv3VirtNbrLsRetransQLen_Type=Gauge32
_FsMIStdOspfv3VirtNbrLsRetransQLen_Object=MibTableColumn
fsMIStdOspfv3VirtNbrLsRetransQLen=_FsMIStdOspfv3VirtNbrLsRetransQLen_Object((1,3,6,1,4,1,29601,2,23,1,11,1,9),_FsMIStdOspfv3VirtNbrLsRetransQLen_Type())
fsMIStdOspfv3VirtNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrLsRetransQLen.setStatus(_A)
_FsMIStdOspfv3VirtNbrHelloSuppressed_Type=TruthValue
_FsMIStdOspfv3VirtNbrHelloSuppressed_Object=MibTableColumn
fsMIStdOspfv3VirtNbrHelloSuppressed=_FsMIStdOspfv3VirtNbrHelloSuppressed_Object((1,3,6,1,4,1,29601,2,23,1,11,1,10),_FsMIStdOspfv3VirtNbrHelloSuppressed_Type())
fsMIStdOspfv3VirtNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrHelloSuppressed.setStatus(_A)
_FsMIStdOspfv3VirtNbrIfId_Type=InterfaceIndex
_FsMIStdOspfv3VirtNbrIfId_Object=MibTableColumn
fsMIStdOspfv3VirtNbrIfId=_FsMIStdOspfv3VirtNbrIfId_Object((1,3,6,1,4,1,29601,2,23,1,11,1,11),_FsMIStdOspfv3VirtNbrIfId_Type())
fsMIStdOspfv3VirtNbrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrIfId.setStatus(_A)
class _FsMIStdOspfv3VirtNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),('helping',2)))
_FsMIStdOspfv3VirtNbrRestartHelperStatus_Type.__name__=_F
_FsMIStdOspfv3VirtNbrRestartHelperStatus_Object=MibTableColumn
fsMIStdOspfv3VirtNbrRestartHelperStatus=_FsMIStdOspfv3VirtNbrRestartHelperStatus_Object((1,3,6,1,4,1,29601,2,23,1,11,1,12),_FsMIStdOspfv3VirtNbrRestartHelperStatus_Type())
fsMIStdOspfv3VirtNbrRestartHelperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrRestartHelperStatus.setStatus(_A)
_FsMIStdOspfv3VirtNbrRestartHelperAge_Type=UpToRefreshInterval
_FsMIStdOspfv3VirtNbrRestartHelperAge_Object=MibTableColumn
fsMIStdOspfv3VirtNbrRestartHelperAge=_FsMIStdOspfv3VirtNbrRestartHelperAge_Object((1,3,6,1,4,1,29601,2,23,1,11,1,13),_FsMIStdOspfv3VirtNbrRestartHelperAge_Type())
fsMIStdOspfv3VirtNbrRestartHelperAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrRestartHelperAge.setUnits(_G)
class _FsMIStdOspfv3VirtNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_FsMIStdOspfv3VirtNbrRestartHelperExitReason_Type.__name__=_F
_FsMIStdOspfv3VirtNbrRestartHelperExitReason_Object=MibTableColumn
fsMIStdOspfv3VirtNbrRestartHelperExitReason=_FsMIStdOspfv3VirtNbrRestartHelperExitReason_Object((1,3,6,1,4,1,29601,2,23,1,11,1,14),_FsMIStdOspfv3VirtNbrRestartHelperExitReason_Type())
fsMIStdOspfv3VirtNbrRestartHelperExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdOspfv3VirtNbrRestartHelperExitReason.setStatus(_A)
_FsMIStdOspfv3AreaAggregateTable_Object=MibTable
fsMIStdOspfv3AreaAggregateTable=_FsMIStdOspfv3AreaAggregateTable_Object((1,3,6,1,4,1,29601,2,23,1,12))
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateTable.setStatus(_A)
_FsMIStdOspfv3AreaAggregateEntry_Object=MibTableRow
fsMIStdOspfv3AreaAggregateEntry=_FsMIStdOspfv3AreaAggregateEntry_Object((1,3,6,1,4,1,29601,2,23,1,12,1))
fsMIStdOspfv3AreaAggregateEntry.setIndexNames((0,_D,_I),(0,_D,_A8),(0,_D,_A9),(0,_D,_AA),(0,_D,_AB),(0,_D,_AC))
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateEntry.setStatus(_A)
_FsMIStdOspfv3AreaAggregateAreaID_Type=AreaID
_FsMIStdOspfv3AreaAggregateAreaID_Object=MibTableColumn
fsMIStdOspfv3AreaAggregateAreaID=_FsMIStdOspfv3AreaAggregateAreaID_Object((1,3,6,1,4,1,29601,2,23,1,12,1,1),_FsMIStdOspfv3AreaAggregateAreaID_Type())
fsMIStdOspfv3AreaAggregateAreaID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateAreaID.setStatus(_A)
class _FsMIStdOspfv3AreaAggregateAreaLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8195,8199)));namedValues=NamedValues(*(('interAreaPrefixLsa',8195),('nssaExternalLsa',8199)))
_FsMIStdOspfv3AreaAggregateAreaLsdbType_Type.__name__=_F
_FsMIStdOspfv3AreaAggregateAreaLsdbType_Object=MibTableColumn
fsMIStdOspfv3AreaAggregateAreaLsdbType=_FsMIStdOspfv3AreaAggregateAreaLsdbType_Object((1,3,6,1,4,1,29601,2,23,1,12,1,2),_FsMIStdOspfv3AreaAggregateAreaLsdbType_Type())
fsMIStdOspfv3AreaAggregateAreaLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateAreaLsdbType.setStatus(_A)
_FsMIStdOspfv3AreaAggregatePrefixType_Type=InetAddressType
_FsMIStdOspfv3AreaAggregatePrefixType_Object=MibTableColumn
fsMIStdOspfv3AreaAggregatePrefixType=_FsMIStdOspfv3AreaAggregatePrefixType_Object((1,3,6,1,4,1,29601,2,23,1,12,1,4),_FsMIStdOspfv3AreaAggregatePrefixType_Type())
fsMIStdOspfv3AreaAggregatePrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregatePrefixType.setStatus(_A)
class _FsMIStdOspfv3AreaAggregatePrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIStdOspfv3AreaAggregatePrefix_Type.__name__=_K
_FsMIStdOspfv3AreaAggregatePrefix_Object=MibTableColumn
fsMIStdOspfv3AreaAggregatePrefix=_FsMIStdOspfv3AreaAggregatePrefix_Object((1,3,6,1,4,1,29601,2,23,1,12,1,5),_FsMIStdOspfv3AreaAggregatePrefix_Type())
fsMIStdOspfv3AreaAggregatePrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregatePrefix.setStatus(_A)
class _FsMIStdOspfv3AreaAggregatePrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,128))
_FsMIStdOspfv3AreaAggregatePrefixLength_Type.__name__=_f
_FsMIStdOspfv3AreaAggregatePrefixLength_Object=MibTableColumn
fsMIStdOspfv3AreaAggregatePrefixLength=_FsMIStdOspfv3AreaAggregatePrefixLength_Object((1,3,6,1,4,1,29601,2,23,1,12,1,6),_FsMIStdOspfv3AreaAggregatePrefixLength_Type())
fsMIStdOspfv3AreaAggregatePrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregatePrefixLength.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregatePrefixLength.setUnits('bits')
class _FsMIStdOspfv3AreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('advertiseMatching',1),('doNotAdvertiseMatching',2)))
_FsMIStdOspfv3AreaAggregateEffect_Type.__name__=_F
_FsMIStdOspfv3AreaAggregateEffect_Object=MibTableColumn
fsMIStdOspfv3AreaAggregateEffect=_FsMIStdOspfv3AreaAggregateEffect_Object((1,3,6,1,4,1,29601,2,23,1,12,1,7),_FsMIStdOspfv3AreaAggregateEffect_Type())
fsMIStdOspfv3AreaAggregateEffect.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateEffect.setStatus(_A)
class _FsMIStdOspfv3AreaAggregateRouteTag_Type(Integer32):defaultValue=0
_FsMIStdOspfv3AreaAggregateRouteTag_Type.__name__=_F
_FsMIStdOspfv3AreaAggregateRouteTag_Object=MibTableColumn
fsMIStdOspfv3AreaAggregateRouteTag=_FsMIStdOspfv3AreaAggregateRouteTag_Object((1,3,6,1,4,1,29601,2,23,1,12,1,8),_FsMIStdOspfv3AreaAggregateRouteTag_Type())
fsMIStdOspfv3AreaAggregateRouteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateRouteTag.setStatus(_A)
_FsMIStdOspfv3AreaAggregateStatus_Type=RowStatus
_FsMIStdOspfv3AreaAggregateStatus_Object=MibTableColumn
fsMIStdOspfv3AreaAggregateStatus=_FsMIStdOspfv3AreaAggregateStatus_Object((1,3,6,1,4,1,29601,2,23,1,12,1,9),_FsMIStdOspfv3AreaAggregateStatus_Type())
fsMIStdOspfv3AreaAggregateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfv3AreaAggregateStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_L:UpToRefreshInterval,_X:RouterDeadRange,'fsMIStdOspfv3':fsMIStdOspfv3,'fsMIStdOspfv3Objects':fsMIStdOspfv3Objects,'fsMIStdOspfv3Table':fsMIStdOspfv3Table,'fsMIStdOspfv3Entry':fsMIStdOspfv3Entry,_I:fsMIStdOspfv3ContextId,'fsMIStdOspfv3RouterId':fsMIStdOspfv3RouterId,'fsMIStdOspfv3AdminStat':fsMIStdOspfv3AdminStat,'fsMIStdOspfv3VersionNumber':fsMIStdOspfv3VersionNumber,'fsMIStdOspfv3AreaBdrRtrStatus':fsMIStdOspfv3AreaBdrRtrStatus,'fsMIStdOspfv3ASBdrRtrStatus':fsMIStdOspfv3ASBdrRtrStatus,'fsMIStdOspfv3AsScopeLsaCount':fsMIStdOspfv3AsScopeLsaCount,'fsMIStdOspfv3AsScopeLsaCksumSum':fsMIStdOspfv3AsScopeLsaCksumSum,'fsMIStdOspfv3OriginateNewLsas':fsMIStdOspfv3OriginateNewLsas,'fsMIStdOspfv3RxNewLsas':fsMIStdOspfv3RxNewLsas,'fsMIStdOspfv3ExtLsaCount':fsMIStdOspfv3ExtLsaCount,'fsMIStdOspfv3ExtAreaLsdbLimit':fsMIStdOspfv3ExtAreaLsdbLimit,'fsMIStdOspfv3MulticastExtensions':fsMIStdOspfv3MulticastExtensions,'fsMIStdOspfv3ExitOverflowInterval':fsMIStdOspfv3ExitOverflowInterval,'fsMIStdOspfv3DemandExtensions':fsMIStdOspfv3DemandExtensions,'fsMIStdOspfv3TrafficEngineeringSupport':fsMIStdOspfv3TrafficEngineeringSupport,'fsMIStdOspfv3ReferenceBandwidth':fsMIStdOspfv3ReferenceBandwidth,'fsMIStdOspfv3RestartSupport':fsMIStdOspfv3RestartSupport,'fsMIStdOspfv3RestartInterval':fsMIStdOspfv3RestartInterval,'fsMIStdOspfv3RestartStatus':fsMIStdOspfv3RestartStatus,'fsMIStdOspfv3RestartAge':fsMIStdOspfv3RestartAge,'fsMIStdOspfv3RestartExitReason':fsMIStdOspfv3RestartExitReason,'fsMIStdOspfv3Status':fsMIStdOspfv3Status,'fsMIStdOspfv3AreaTable':fsMIStdOspfv3AreaTable,'fsMIStdOspfv3AreaEntry':fsMIStdOspfv3AreaEntry,_j:fsMIStdOspfv3AreaId,'fsMIStdOspfv3ImportAsExtern':fsMIStdOspfv3ImportAsExtern,'fsMIStdOspfv3AreaSpfRuns':fsMIStdOspfv3AreaSpfRuns,'fsMIStdOspfv3AreaBdrRtrCount':fsMIStdOspfv3AreaBdrRtrCount,'fsMIStdOspfv3AreaAsBdrRtrCount':fsMIStdOspfv3AreaAsBdrRtrCount,'fsMIStdOspfv3AreaScopeLsaCount':fsMIStdOspfv3AreaScopeLsaCount,'fsMIStdOspfv3AreaScopeLsaCksumSum':fsMIStdOspfv3AreaScopeLsaCksumSum,'fsMIStdOspfv3AreaSummary':fsMIStdOspfv3AreaSummary,'fsMIStdOspfv3StubMetric':fsMIStdOspfv3StubMetric,'fsMIStdOspfv3AreaNssaTranslatorRole':fsMIStdOspfv3AreaNssaTranslatorRole,'fsMIStdOspfv3AreaNssaTranslatorState':fsMIStdOspfv3AreaNssaTranslatorState,'fsMIStdOspfv3AreaNssaTranslatorStabilityInterval':fsMIStdOspfv3AreaNssaTranslatorStabilityInterval,'fsMIStdOspfv3AreaNssaTranslatorEvents':fsMIStdOspfv3AreaNssaTranslatorEvents,'fsMIStdOspfv3AreaStubMetricType':fsMIStdOspfv3AreaStubMetricType,'fsMIStdOspfv3AreaStatus':fsMIStdOspfv3AreaStatus,'fsMIStdOspfv3AsLsdbTable':fsMIStdOspfv3AsLsdbTable,'fsMIStdOspfv3AsLsdbEntry':fsMIStdOspfv3AsLsdbEntry,_k:fsMIStdOspfv3AsLsdbType,_l:fsMIStdOspfv3AsLsdbRouterId,_m:fsMIStdOspfv3AsLsdbLsid,'fsMIStdOspfv3AsLsdbSequence':fsMIStdOspfv3AsLsdbSequence,'fsMIStdOspfv3AsLsdbAge':fsMIStdOspfv3AsLsdbAge,'fsMIStdOspfv3AsLsdbChecksum':fsMIStdOspfv3AsLsdbChecksum,'fsMIStdOspfv3AsLsdbAdvertisement':fsMIStdOspfv3AsLsdbAdvertisement,'fsMIStdOspfv3AsLsdbTypeKnown':fsMIStdOspfv3AsLsdbTypeKnown,'fsMIStdOspfv3AreaLsdbTable':fsMIStdOspfv3AreaLsdbTable,'fsMIStdOspfv3AreaLsdbEntry':fsMIStdOspfv3AreaLsdbEntry,_n:fsMIStdOspfv3AreaLsdbAreaId,_o:fsMIStdOspfv3AreaLsdbType,_p:fsMIStdOspfv3AreaLsdbRouterId,_q:fsMIStdOspfv3AreaLsdbLsid,'fsMIStdOspfv3AreaLsdbSequence':fsMIStdOspfv3AreaLsdbSequence,'fsMIStdOspfv3AreaLsdbAge':fsMIStdOspfv3AreaLsdbAge,'fsMIStdOspfv3AreaLsdbChecksum':fsMIStdOspfv3AreaLsdbChecksum,'fsMIStdOspfv3AreaLsdbAdvertisement':fsMIStdOspfv3AreaLsdbAdvertisement,'fsMIStdOspfv3AreaLsdbTypeKnown':fsMIStdOspfv3AreaLsdbTypeKnown,'fsMIStdOspfv3LinkLsdbTable':fsMIStdOspfv3LinkLsdbTable,'fsMIStdOspfv3LinkLsdbEntry':fsMIStdOspfv3LinkLsdbEntry,_r:fsMIStdOspfv3LinkLsdbIfIndex,_s:fsMIStdOspfv3LinkLsdbType,_t:fsMIStdOspfv3LinkLsdbRouterId,_u:fsMIStdOspfv3LinkLsdbLsid,'fsMIStdOspfv3LinkLsdbSequence':fsMIStdOspfv3LinkLsdbSequence,'fsMIStdOspfv3LinkLsdbAge':fsMIStdOspfv3LinkLsdbAge,'fsMIStdOspfv3LinkLsdbChecksum':fsMIStdOspfv3LinkLsdbChecksum,'fsMIStdOspfv3LinkLsdbAdvertisement':fsMIStdOspfv3LinkLsdbAdvertisement,'fsMIStdOspfv3LinkLsdbTypeKnown':fsMIStdOspfv3LinkLsdbTypeKnown,'fsMIStdOspfv3LinkLsdbContextId':fsMIStdOspfv3LinkLsdbContextId,'fsMIStdOspfv3HostTable':fsMIStdOspfv3HostTable,'fsMIStdOspfv3HostEntry':fsMIStdOspfv3HostEntry,_v:fsMIStdOspfv3HostAddressType,_w:fsMIStdOspfv3HostAddress,'fsMIStdOspfv3HostMetric':fsMIStdOspfv3HostMetric,'fsMIStdOspfv3HostAreaID':fsMIStdOspfv3HostAreaID,'fsMIStdOspfv3HostStatus':fsMIStdOspfv3HostStatus,'fsMIStdOspfv3IfTable':fsMIStdOspfv3IfTable,'fsMIStdOspfv3IfEntry':fsMIStdOspfv3IfEntry,_x:fsMIStdOspfv3IfIndex,'fsMIStdOspfv3IfAreaId':fsMIStdOspfv3IfAreaId,'fsMIStdOspfv3IfType':fsMIStdOspfv3IfType,'fsMIStdOspfv3IfAdminStat':fsMIStdOspfv3IfAdminStat,'fsMIStdOspfv3IfRtrPriority':fsMIStdOspfv3IfRtrPriority,'fsMIStdOspfv3IfTransitDelay':fsMIStdOspfv3IfTransitDelay,'fsMIStdOspfv3IfRetransInterval':fsMIStdOspfv3IfRetransInterval,'fsMIStdOspfv3IfHelloInterval':fsMIStdOspfv3IfHelloInterval,'fsMIStdOspfv3IfRtrDeadInterval':fsMIStdOspfv3IfRtrDeadInterval,'fsMIStdOspfv3IfPollInterval':fsMIStdOspfv3IfPollInterval,'fsMIStdOspfv3IfState':fsMIStdOspfv3IfState,'fsMIStdOspfv3IfDesignatedRouter':fsMIStdOspfv3IfDesignatedRouter,'fsMIStdOspfv3IfBackupDesignatedRouter':fsMIStdOspfv3IfBackupDesignatedRouter,'fsMIStdOspfv3IfEvents':fsMIStdOspfv3IfEvents,'fsMIStdOspfv3IfMulticastForwarding':fsMIStdOspfv3IfMulticastForwarding,'fsMIStdOspfv3IfDemand':fsMIStdOspfv3IfDemand,'fsMIStdOspfv3IfMetricValue':fsMIStdOspfv3IfMetricValue,'fsMIStdOspfv3IfLinkScopeLsaCount':fsMIStdOspfv3IfLinkScopeLsaCount,'fsMIStdOspfv3IfLinkLsaCksumSum':fsMIStdOspfv3IfLinkLsaCksumSum,'fsMIStdOspfv3IfInstId':fsMIStdOspfv3IfInstId,'fsMIStdOspfv3IfDemandNbrProbe':fsMIStdOspfv3IfDemandNbrProbe,'fsMIStdOspfv3IfDemandNbrProbeRetxLimit':fsMIStdOspfv3IfDemandNbrProbeRetxLimit,'fsMIStdOspfv3IfDemandNbrProbeInterval':fsMIStdOspfv3IfDemandNbrProbeInterval,'fsMIStdOspfv3IfContextId':fsMIStdOspfv3IfContextId,'fsMIStdOspfv3IfStatus':fsMIStdOspfv3IfStatus,'fsMIStdOspfv3VirtIfTable':fsMIStdOspfv3VirtIfTable,'fsMIStdOspfv3VirtIfEntry':fsMIStdOspfv3VirtIfEntry,_y:fsMIStdOspfv3VirtIfAreaId,_z:fsMIStdOspfv3VirtIfNeighbor,'fsMIStdOspfv3VirtIfIndex':fsMIStdOspfv3VirtIfIndex,'fsMIStdOspfv3VirtIfTransitDelay':fsMIStdOspfv3VirtIfTransitDelay,'fsMIStdOspfv3VirtIfRetransInterval':fsMIStdOspfv3VirtIfRetransInterval,'fsMIStdOspfv3VirtIfHelloInterval':fsMIStdOspfv3VirtIfHelloInterval,'fsMIStdOspfv3VirtIfRtrDeadInterval':fsMIStdOspfv3VirtIfRtrDeadInterval,'fsMIStdOspfv3VirtIfState':fsMIStdOspfv3VirtIfState,'fsMIStdOspfv3VirtIfEvents':fsMIStdOspfv3VirtIfEvents,'fsMIStdOspfv3VirtIfLinkScopeLsaCount':fsMIStdOspfv3VirtIfLinkScopeLsaCount,'fsMIStdOspfv3VirtIfLinkLsaCksumSum':fsMIStdOspfv3VirtIfLinkLsaCksumSum,'fsMIStdOspfv3VirtIfStatus':fsMIStdOspfv3VirtIfStatus,'fsMIStdOspfv3NbrTable':fsMIStdOspfv3NbrTable,'fsMIStdOspfv3NbrEntry':fsMIStdOspfv3NbrEntry,_A0:fsMIStdOspfv3NbrIfIndex,_A1:fsMIStdOspfv3NbrRtrId,'fsMIStdOspfv3NbrAddressType':fsMIStdOspfv3NbrAddressType,'fsMIStdOspfv3NbrAddress':fsMIStdOspfv3NbrAddress,'fsMIStdOspfv3NbrOptions':fsMIStdOspfv3NbrOptions,'fsMIStdOspfv3NbrPriority':fsMIStdOspfv3NbrPriority,'fsMIStdOspfv3NbrState':fsMIStdOspfv3NbrState,'fsMIStdOspfv3NbrEvents':fsMIStdOspfv3NbrEvents,'fsMIStdOspfv3NbrLsRetransQLen':fsMIStdOspfv3NbrLsRetransQLen,'fsMIStdOspfv3NbrHelloSuppressed':fsMIStdOspfv3NbrHelloSuppressed,'fsMIStdOspfv3NbrIfId':fsMIStdOspfv3NbrIfId,'fsMIStdOspfv3NbrRestartHelperStatus':fsMIStdOspfv3NbrRestartHelperStatus,'fsMIStdOspfv3NbrRestartHelperAge':fsMIStdOspfv3NbrRestartHelperAge,'fsMIStdOspfv3NbrRestartHelperExitReason':fsMIStdOspfv3NbrRestartHelperExitReason,'fsMIStdOspfv3NbrContextId':fsMIStdOspfv3NbrContextId,'fsMIStdOspfv3NbmaNbrTable':fsMIStdOspfv3NbmaNbrTable,'fsMIStdOspfv3NbmaNbrEntry':fsMIStdOspfv3NbmaNbrEntry,_A3:fsMIStdOspfv3NbmaNbrIfIndex,_A4:fsMIStdOspfv3NbmaNbrAddressType,_A5:fsMIStdOspfv3NbmaNbrAddress,'fsMIStdOspfv3NbmaNbrPriority':fsMIStdOspfv3NbmaNbrPriority,'fsMIStdOspfv3NbmaNbrRtrId':fsMIStdOspfv3NbmaNbrRtrId,'fsMIStdOspfv3NbmaNbrState':fsMIStdOspfv3NbmaNbrState,'fsMIStdOspfv3NbmaNbrStorageType':fsMIStdOspfv3NbmaNbrStorageType,'fsMIStdOspfv3NbmaNbrContextId':fsMIStdOspfv3NbmaNbrContextId,'fsMIStdOspfv3NbmaNbrStatus':fsMIStdOspfv3NbmaNbrStatus,'fsMIStdOspfv3VirtNbrTable':fsMIStdOspfv3VirtNbrTable,'fsMIStdOspfv3VirtNbrEntry':fsMIStdOspfv3VirtNbrEntry,_A6:fsMIStdOspfv3VirtNbrArea,_A7:fsMIStdOspfv3VirtNbrRtrId,'fsMIStdOspfv3VirtNbrIfIndex':fsMIStdOspfv3VirtNbrIfIndex,'fsMIStdOspfv3VirtNbrAddressType':fsMIStdOspfv3VirtNbrAddressType,'fsMIStdOspfv3VirtNbrAddress':fsMIStdOspfv3VirtNbrAddress,'fsMIStdOspfv3VirtNbrOptions':fsMIStdOspfv3VirtNbrOptions,'fsMIStdOspfv3VirtNbrState':fsMIStdOspfv3VirtNbrState,'fsMIStdOspfv3VirtNbrEvents':fsMIStdOspfv3VirtNbrEvents,'fsMIStdOspfv3VirtNbrLsRetransQLen':fsMIStdOspfv3VirtNbrLsRetransQLen,'fsMIStdOspfv3VirtNbrHelloSuppressed':fsMIStdOspfv3VirtNbrHelloSuppressed,'fsMIStdOspfv3VirtNbrIfId':fsMIStdOspfv3VirtNbrIfId,'fsMIStdOspfv3VirtNbrRestartHelperStatus':fsMIStdOspfv3VirtNbrRestartHelperStatus,'fsMIStdOspfv3VirtNbrRestartHelperAge':fsMIStdOspfv3VirtNbrRestartHelperAge,'fsMIStdOspfv3VirtNbrRestartHelperExitReason':fsMIStdOspfv3VirtNbrRestartHelperExitReason,'fsMIStdOspfv3AreaAggregateTable':fsMIStdOspfv3AreaAggregateTable,'fsMIStdOspfv3AreaAggregateEntry':fsMIStdOspfv3AreaAggregateEntry,_A8:fsMIStdOspfv3AreaAggregateAreaID,_A9:fsMIStdOspfv3AreaAggregateAreaLsdbType,_AA:fsMIStdOspfv3AreaAggregatePrefixType,_AB:fsMIStdOspfv3AreaAggregatePrefix,_AC:fsMIStdOspfv3AreaAggregatePrefixLength,'fsMIStdOspfv3AreaAggregateEffect':fsMIStdOspfv3AreaAggregateEffect,'fsMIStdOspfv3AreaAggregateRouteTag':fsMIStdOspfv3AreaAggregateRouteTag,'fsMIStdOspfv3AreaAggregateStatus':fsMIStdOspfv3AreaAggregateStatus})