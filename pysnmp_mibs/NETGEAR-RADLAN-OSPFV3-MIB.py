_As='rlOspfv3VirtNbrRestartHelperExitReason'
_Ar='rlOspfv3VirtNbrRestartHelperAge'
_Aq='rlOspfv3VirtNbrRestartHelperStatus'
_Ap='rlOspfv3NbrRestartHelperExitReason'
_Ao='rlOspfv3NbrRestartHelperAge'
_An='rlOspfv3NbrRestartHelperStatus'
_Am='rlOspfv3RestartExitReason'
_Al='rlOspfv3RestartInterval'
_Ak='rlOspfv3RestartStatus'
_Aj='rlOspfv3AreaNssaTranslatorState'
_Ai='rlOspfv3VirtNbrState'
_Ah='rlOspfv3NbrState'
_Ag='rlOspfv3VirtLinkLsdbLsid'
_Af='rlOspfv3VirtLinkLsdbRouterId'
_Ae='rlOspfv3VirtLinkLsdbType'
_Ad='rlOspfv3VirtLinkLsdbIfNeighbor'
_Ac='rlOspfv3VirtLinkLsdbIfAreaId'
_Ab='rlOspfv3VirtLinkLsdbProcessId'
_Aa='rlOspfv3AreaAggregatePrefixLength'
_AZ='rlOspfv3AreaAggregatePrefix'
_AY='rlOspfv3AreaAggregatePrefixType'
_AX='rlOspfv3AreaAggregateAreaLsdbType'
_AW='rlOspfv3AreaAggregateAreaID'
_AV='rlOspfv3AreaAggregateProcessId'
_AU='rlOspfv3VirtNbrRtrId'
_AT='rlOspfv3VirtNbrArea'
_AS='rlOspfv3VirtNbrProcessId'
_AR='rlOspfv3CfgNbrAddress'
_AQ='rlOspfv3CfgNbrAddressType'
_AP='rlOspfv3CfgNbrIfInstId'
_AO='rlOspfv3CfgNbrIfIndex'
_AN='rlOspf3CfgNbrProcessId'
_AM='exchangeStart'
_AL='rlOspfv3NbrRtrId'
_AK='rlOspfv3NbrIfInstId'
_AJ='rlOspfv3NbrIfIndex'
_AI='rlOspfv3NbrProcessId'
_AH='rlOspfv3VirtIfNeighbor'
_AG='rlOspfv3VirtIfAreaId'
_AF='rlOspfv3VirtIfProcessId'
_AE='RlOspfv3FastHelloMultiplierRange'
_AD='rlOspfv3IfInstId'
_AC='rlOspfv3IfIndex'
_AB='rlOspfv3IfProcessId'
_AA='rlOspfv3HostAddress'
_A9='rlOspfv3HostAddressType'
_A8='rlOspfv3HostProcessId'
_A7='rlOspfv3LinkLsdbLsid'
_A6='rlOspfv3LinkLsdbRouterId'
_A5='rlOspfv3LinkLsdbType'
_A4='rlOspfv3LinkLsdbIfInstId'
_A3='rlOspfv3LinkLsdbIfIndex'
_A2='rlOspfv3LinkLsdbProcessId'
_A1='rlOspfv3AreaLsdbLsid'
_A0='rlOspfv3AreaLsdbRouterId'
_z='rlOspfv3AreaLsdbType'
_y='rlOspfv3AreaLsdbAreaId'
_x='rlOspfv3AreaLsdbProcessId'
_w='rlOspfv3AsLsdbLsid'
_v='rlOspfv3AsLsdbRouterId'
_u='rlOspfv3AsLsdbType'
_t='rlOspfv3AsLsdbProcessId'
_s='rlOspfv3AreaId'
_r='rlOspfv3AreaProcessId'
_q='rlOspfv3ProcessId'
_p='Ospfv3UpToRefreshIntervalTC'
_o='InetAddressPrefixLength'
_n='InetAddress'
_m='rlOspfv3ExtAreaLsdbLimit'
_l='rlOspfv3ConfigErrorType'
_k='rlOspfv3PacketSrc'
_j='accessible-for-notify'
_i='pointToPoint'
_h='helping'
_g='notHelping'
_f='DisplayString'
_e='Ospfv3DeadIntervalRangeTC'
_d='HelloRange'
_c='DesignatedRouterPriority'
_b='rlOspfv3IfState'
_a='rlOspfv3VirtIfState'
_Z='actFailed'
_Y='goingDown'
_X='goingUp'
_W='up'
_V='topologyChanged'
_U='timedOut'
_T='completed'
_S='inProgress'
_R='Gauge32'
_Q='Status'
_P='rlOspfv3PacketType'
_O='RlOspfv3UpToRefreshIntervalTC'
_N='none'
_M='OctetString'
_L='down'
_K='TruthValue'
_J='Unsigned32'
_I='rlOspfv3RouterId'
_H='seconds'
_G='read-write'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='NETGEAR-RADLAN-OSPFV3-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressIPv6,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_n,'InetAddressIPv6',_o,'InetAddressType')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
RlOspfFastHelloMultiplierRange,RlOspfProcessID,RlOspfRestartExitReason,RlOspfRestartHelperStatus,RlOspfRouterIdType=mibBuilder.importSymbols('NETGEAR-RADLAN-OSPF-MIB','RlOspfFastHelloMultiplierRange','RlOspfProcessID','RlOspfRestartExitReason','RlOspfRestartHelperStatus','RlOspfRouterIdType')
AreaID,BigMetric,DesignatedRouterPriority,HelloRange,Metric,OspfAuthenticationType,PositiveInteger,RouterID,Status,TOSType,UpToMaxAge=mibBuilder.importSymbols('OSPF-MIB','AreaID','BigMetric',_c,_d,'Metric','OspfAuthenticationType','PositiveInteger','RouterID',_Q,'TOSType','UpToMaxAge')
Ospfv3AreaIdTC,Ospfv3DeadIntervalRangeTC,Ospfv3IfInstIdTC,Ospfv3LsIdTC,Ospfv3LsaAgeTC,Ospfv3LsaSequenceTC,Ospfv3RouterIdTC,Ospfv3UpToRefreshIntervalTC=mibBuilder.importSymbols('OSPFV3-MIB','Ospfv3AreaIdTC',_e,'Ospfv3IfInstIdTC','Ospfv3LsIdTC','Ospfv3LsaAgeTC','Ospfv3LsaSequenceTC','Ospfv3RouterIdTC',_p)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_R,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_f,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_K)
rlOspfv3=ModuleIdentity((1,3,6,1,4,1,4526,17,216))
if mibBuilder.loadTexts:rlOspfv3.setRevisions(('2011-05-04 17:00',))
class RlRouterID(TextualConvention,Unsigned32):status=_A;displayHint='d'
class RlLsID(TextualConvention,Unsigned32):status=_A;displayHint='d'
class RlOspfv3FastHelloMultiplierRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
class RlOspfv3UpToRefreshInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
class RlOspfv3RestartHelperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
class RlOspfv3RestartExitReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_S,2),(_T,3),(_U,4),(_V,5)))
class RlOspfv3UpToRefreshIntervalTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlOspfv3Instance_Type=RlOspfProcessID
_RlOspfv3Instance_Object=MibScalar
rlOspfv3Instance=_RlOspfv3Instance_Object((1,3,6,1,4,1,4526,17,216,1),_RlOspfv3Instance_Type())
rlOspfv3Instance.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3Instance.setStatus(_A)
_RlOspfv3GeneralGroupTable_Object=MibTable
rlOspfv3GeneralGroupTable=_RlOspfv3GeneralGroupTable_Object((1,3,6,1,4,1,4526,17,216,2))
if mibBuilder.loadTexts:rlOspfv3GeneralGroupTable.setStatus(_A)
_RlOspfv3GeneralGroupEntry_Object=MibTableRow
rlOspfv3GeneralGroupEntry=_RlOspfv3GeneralGroupEntry_Object((1,3,6,1,4,1,4526,17,216,2,1))
rlOspfv3GeneralGroupEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:rlOspfv3GeneralGroupEntry.setStatus(_A)
_RlOspfv3ProcessId_Type=RlOspfProcessID
_RlOspfv3ProcessId_Object=MibTableColumn
rlOspfv3ProcessId=_RlOspfv3ProcessId_Object((1,3,6,1,4,1,4526,17,216,2,1,1),_RlOspfv3ProcessId_Type())
rlOspfv3ProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3ProcessId.setStatus(_A)
_RlOspfv3RouterId_Type=RouterID
_RlOspfv3RouterId_Object=MibTableColumn
rlOspfv3RouterId=_RlOspfv3RouterId_Object((1,3,6,1,4,1,4526,17,216,2,1,2),_RlOspfv3RouterId_Type())
rlOspfv3RouterId.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3RouterId.setStatus(_A)
_RlOspfv3AdminStatus_Type=Status
_RlOspfv3AdminStatus_Object=MibTableColumn
rlOspfv3AdminStatus=_RlOspfv3AdminStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,3),_RlOspfv3AdminStatus_Type())
rlOspfv3AdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3AdminStatus.setStatus(_A)
class _RlOspfv3VersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('version3',3))
_RlOspfv3VersionNumber_Type.__name__=_F
_RlOspfv3VersionNumber_Object=MibTableColumn
rlOspfv3VersionNumber=_RlOspfv3VersionNumber_Object((1,3,6,1,4,1,4526,17,216,2,1,4),_RlOspfv3VersionNumber_Type())
rlOspfv3VersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VersionNumber.setStatus(_A)
_RlOspfv3AreaBdrRtrStatus_Type=TruthValue
_RlOspfv3AreaBdrRtrStatus_Object=MibTableColumn
rlOspfv3AreaBdrRtrStatus=_RlOspfv3AreaBdrRtrStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,5),_RlOspfv3AreaBdrRtrStatus_Type())
rlOspfv3AreaBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaBdrRtrStatus.setStatus(_A)
_RlOspfv3ASBdrRtrStatus_Type=TruthValue
_RlOspfv3ASBdrRtrStatus_Object=MibTableColumn
rlOspfv3ASBdrRtrStatus=_RlOspfv3ASBdrRtrStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,6),_RlOspfv3ASBdrRtrStatus_Type())
rlOspfv3ASBdrRtrStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3ASBdrRtrStatus.setStatus(_A)
_RlOspfv3AsScopeLsaCount_Type=Gauge32
_RlOspfv3AsScopeLsaCount_Object=MibTableColumn
rlOspfv3AsScopeLsaCount=_RlOspfv3AsScopeLsaCount_Object((1,3,6,1,4,1,4526,17,216,2,1,7),_RlOspfv3AsScopeLsaCount_Type())
rlOspfv3AsScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsScopeLsaCount.setStatus(_A)
_RlOspfv3AsScopeLsaCksumSum_Type=Unsigned32
_RlOspfv3AsScopeLsaCksumSum_Object=MibTableColumn
rlOspfv3AsScopeLsaCksumSum=_RlOspfv3AsScopeLsaCksumSum_Object((1,3,6,1,4,1,4526,17,216,2,1,8),_RlOspfv3AsScopeLsaCksumSum_Type())
rlOspfv3AsScopeLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsScopeLsaCksumSum.setStatus(_A)
_RlOspfv3OriginateNewLsas_Type=Counter32
_RlOspfv3OriginateNewLsas_Object=MibTableColumn
rlOspfv3OriginateNewLsas=_RlOspfv3OriginateNewLsas_Object((1,3,6,1,4,1,4526,17,216,2,1,9),_RlOspfv3OriginateNewLsas_Type())
rlOspfv3OriginateNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3OriginateNewLsas.setStatus(_A)
_RlOspfv3RxNewLsas_Type=Counter32
_RlOspfv3RxNewLsas_Object=MibTableColumn
rlOspfv3RxNewLsas=_RlOspfv3RxNewLsas_Object((1,3,6,1,4,1,4526,17,216,2,1,10),_RlOspfv3RxNewLsas_Type())
rlOspfv3RxNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3RxNewLsas.setStatus(_A)
_RlOspfv3ExtLsaCount_Type=Gauge32
_RlOspfv3ExtLsaCount_Object=MibTableColumn
rlOspfv3ExtLsaCount=_RlOspfv3ExtLsaCount_Object((1,3,6,1,4,1,4526,17,216,2,1,11),_RlOspfv3ExtLsaCount_Type())
rlOspfv3ExtLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3ExtLsaCount.setStatus(_A)
class _RlOspfv3ExtAreaLsdbLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_RlOspfv3ExtAreaLsdbLimit_Type.__name__=_F
_RlOspfv3ExtAreaLsdbLimit_Object=MibTableColumn
rlOspfv3ExtAreaLsdbLimit=_RlOspfv3ExtAreaLsdbLimit_Object((1,3,6,1,4,1,4526,17,216,2,1,12),_RlOspfv3ExtAreaLsdbLimit_Type())
rlOspfv3ExtAreaLsdbLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3ExtAreaLsdbLimit.setStatus(_A)
_RlOspfv3ExitOverflowInterval_Type=Unsigned32
_RlOspfv3ExitOverflowInterval_Object=MibTableColumn
rlOspfv3ExitOverflowInterval=_RlOspfv3ExitOverflowInterval_Object((1,3,6,1,4,1,4526,17,216,2,1,13),_RlOspfv3ExitOverflowInterval_Type())
rlOspfv3ExitOverflowInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3ExitOverflowInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3ExitOverflowInterval.setUnits(_H)
_RlOspfv3DemandExtensions_Type=TruthValue
_RlOspfv3DemandExtensions_Object=MibTableColumn
rlOspfv3DemandExtensions=_RlOspfv3DemandExtensions_Object((1,3,6,1,4,1,4526,17,216,2,1,14),_RlOspfv3DemandExtensions_Type())
rlOspfv3DemandExtensions.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3DemandExtensions.setStatus(_A)
class _RlOspfv3ReferenceBandwidth_Type(Unsigned32):defaultValue=100000
_RlOspfv3ReferenceBandwidth_Type.__name__=_J
_RlOspfv3ReferenceBandwidth_Object=MibTableColumn
rlOspfv3ReferenceBandwidth=_RlOspfv3ReferenceBandwidth_Object((1,3,6,1,4,1,4526,17,216,2,1,15),_RlOspfv3ReferenceBandwidth_Type())
rlOspfv3ReferenceBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3ReferenceBandwidth.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3ReferenceBandwidth.setUnits('kilobits per second')
class _RlOspfv3RestartSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('plannedOnly',2),('plannedAndUnplanned',3)))
_RlOspfv3RestartSupport_Type.__name__=_F
_RlOspfv3RestartSupport_Object=MibTableColumn
rlOspfv3RestartSupport=_RlOspfv3RestartSupport_Object((1,3,6,1,4,1,4526,17,216,2,1,16),_RlOspfv3RestartSupport_Type())
rlOspfv3RestartSupport.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3RestartSupport.setStatus(_A)
class _RlOspfv3RestartInterval_Type(Ospfv3UpToRefreshIntervalTC):defaultValue=120
_RlOspfv3RestartInterval_Type.__name__=_p
_RlOspfv3RestartInterval_Object=MibTableColumn
rlOspfv3RestartInterval=_RlOspfv3RestartInterval_Object((1,3,6,1,4,1,4526,17,216,2,1,17),_RlOspfv3RestartInterval_Type())
rlOspfv3RestartInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3RestartInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3RestartInterval.setUnits(_H)
class _RlOspfv3RestartStrictLsaChecking_Type(TruthValue):defaultValue=1
_RlOspfv3RestartStrictLsaChecking_Type.__name__=_K
_RlOspfv3RestartStrictLsaChecking_Object=MibTableColumn
rlOspfv3RestartStrictLsaChecking=_RlOspfv3RestartStrictLsaChecking_Object((1,3,6,1,4,1,4526,17,216,2,1,18),_RlOspfv3RestartStrictLsaChecking_Type())
rlOspfv3RestartStrictLsaChecking.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3RestartStrictLsaChecking.setStatus(_A)
class _RlOspfv3RestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRestarting',1),('plannedRestart',2),('unplannedRestart',3)))
_RlOspfv3RestartStatus_Type.__name__=_F
_RlOspfv3RestartStatus_Object=MibTableColumn
rlOspfv3RestartStatus=_RlOspfv3RestartStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,19),_RlOspfv3RestartStatus_Type())
rlOspfv3RestartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3RestartStatus.setStatus(_A)
_RlOspfv3RestartAge_Type=Ospfv3UpToRefreshIntervalTC
_RlOspfv3RestartAge_Object=MibTableColumn
rlOspfv3RestartAge=_RlOspfv3RestartAge_Object((1,3,6,1,4,1,4526,17,216,2,1,20),_RlOspfv3RestartAge_Type())
rlOspfv3RestartAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3RestartAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3RestartAge.setUnits(_H)
class _RlOspfv3RestartExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_RlOspfv3RestartExitReason_Type.__name__=_F
_RlOspfv3RestartExitReason_Object=MibTableColumn
rlOspfv3RestartExitReason=_RlOspfv3RestartExitReason_Object((1,3,6,1,4,1,4526,17,216,2,1,21),_RlOspfv3RestartExitReason_Type())
rlOspfv3RestartExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3RestartExitReason.setStatus(_A)
_RlOspfv3NotificationEnable_Type=TruthValue
_RlOspfv3NotificationEnable_Object=MibTableColumn
rlOspfv3NotificationEnable=_RlOspfv3NotificationEnable_Object((1,3,6,1,4,1,4526,17,216,2,1,22),_RlOspfv3NotificationEnable_Type())
rlOspfv3NotificationEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3NotificationEnable.setStatus(_A)
_RlOspfv3StubRouterSupport_Type=TruthValue
_RlOspfv3StubRouterSupport_Object=MibTableColumn
rlOspfv3StubRouterSupport=_RlOspfv3StubRouterSupport_Object((1,3,6,1,4,1,4526,17,216,2,1,23),_RlOspfv3StubRouterSupport_Type())
rlOspfv3StubRouterSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3StubRouterSupport.setStatus(_A)
class _RlOspfv3StubRouterAdvertisement_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNotAdvertise',1),('advertise',2)))
_RlOspfv3StubRouterAdvertisement_Type.__name__=_F
_RlOspfv3StubRouterAdvertisement_Object=MibTableColumn
rlOspfv3StubRouterAdvertisement=_RlOspfv3StubRouterAdvertisement_Object((1,3,6,1,4,1,4526,17,216,2,1,24),_RlOspfv3StubRouterAdvertisement_Type())
rlOspfv3StubRouterAdvertisement.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3StubRouterAdvertisement.setStatus(_A)
_RlOspfv3DiscontinuityTime_Type=TimeStamp
_RlOspfv3DiscontinuityTime_Object=MibTableColumn
rlOspfv3DiscontinuityTime=_RlOspfv3DiscontinuityTime_Object((1,3,6,1,4,1,4526,17,216,2,1,25),_RlOspfv3DiscontinuityTime_Type())
rlOspfv3DiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3DiscontinuityTime.setStatus(_A)
_RlOspfv3RestartTime_Type=TimeStamp
_RlOspfv3RestartTime_Object=MibTableColumn
rlOspfv3RestartTime=_RlOspfv3RestartTime_Object((1,3,6,1,4,1,4526,17,216,2,1,26),_RlOspfv3RestartTime_Type())
rlOspfv3RestartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3RestartTime.setStatus(_A)
class _RlOspfv3OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_L,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfv3OperStatus_Type.__name__=_F
_RlOspfv3OperStatus_Object=MibTableColumn
rlOspfv3OperStatus=_RlOspfv3OperStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,27),_RlOspfv3OperStatus_Type())
rlOspfv3OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3OperStatus.setStatus(_A)
_RlOspfv3RowStatus_Type=RowStatus
_RlOspfv3RowStatus_Object=MibTableColumn
rlOspfv3RowStatus=_RlOspfv3RowStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,28),_RlOspfv3RowStatus_Type())
rlOspfv3RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3RowStatus.setStatus(_A)
class _RlOspfv3LogAdjacencyChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('detail',2),('disable',3)))
_RlOspfv3LogAdjacencyChanges_Type.__name__=_F
_RlOspfv3LogAdjacencyChanges_Object=MibTableColumn
rlOspfv3LogAdjacencyChanges=_RlOspfv3LogAdjacencyChanges_Object((1,3,6,1,4,1,4526,17,216,2,1,29),_RlOspfv3LogAdjacencyChanges_Type())
rlOspfv3LogAdjacencyChanges.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3LogAdjacencyChanges.setStatus(_A)
_RlOspfv3PassiveInterface_Type=TruthValue
_RlOspfv3PassiveInterface_Object=MibTableColumn
rlOspfv3PassiveInterface=_RlOspfv3PassiveInterface_Object((1,3,6,1,4,1,4526,17,216,2,1,30),_RlOspfv3PassiveInterface_Type())
rlOspfv3PassiveInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3PassiveInterface.setStatus(_A)
class _RlOspfv3DefaultMetric_Type(Integer32):defaultValue=0
_RlOspfv3DefaultMetric_Type.__name__=_F
_RlOspfv3DefaultMetric_Object=MibTableColumn
rlOspfv3DefaultMetric=_RlOspfv3DefaultMetric_Object((1,3,6,1,4,1,4526,17,216,2,1,31),_RlOspfv3DefaultMetric_Type())
rlOspfv3DefaultMetric.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3DefaultMetric.setStatus(_A)
class _RlOspfv3MaximumRedistPrefixNum_Type(Integer32):defaultValue=0
_RlOspfv3MaximumRedistPrefixNum_Type.__name__=_F
_RlOspfv3MaximumRedistPrefixNum_Object=MibTableColumn
rlOspfv3MaximumRedistPrefixNum=_RlOspfv3MaximumRedistPrefixNum_Object((1,3,6,1,4,1,4526,17,216,2,1,32),_RlOspfv3MaximumRedistPrefixNum_Type())
rlOspfv3MaximumRedistPrefixNum.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3MaximumRedistPrefixNum.setStatus(_A)
class _RlOspfv3MaximumRedistPrefixThreshold_Type(Integer32):defaultValue=75
_RlOspfv3MaximumRedistPrefixThreshold_Type.__name__=_F
_RlOspfv3MaximumRedistPrefixThreshold_Object=MibTableColumn
rlOspfv3MaximumRedistPrefixThreshold=_RlOspfv3MaximumRedistPrefixThreshold_Object((1,3,6,1,4,1,4526,17,216,2,1,33),_RlOspfv3MaximumRedistPrefixThreshold_Type())
rlOspfv3MaximumRedistPrefixThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3MaximumRedistPrefixThreshold.setStatus(_A)
class _RlOspfv3MaximumRedistPrefixWarningOnly_Type(TruthValue):defaultValue=2
_RlOspfv3MaximumRedistPrefixWarningOnly_Type.__name__=_K
_RlOspfv3MaximumRedistPrefixWarningOnly_Object=MibTableColumn
rlOspfv3MaximumRedistPrefixWarningOnly=_RlOspfv3MaximumRedistPrefixWarningOnly_Object((1,3,6,1,4,1,4526,17,216,2,1,34),_RlOspfv3MaximumRedistPrefixWarningOnly_Type())
rlOspfv3MaximumRedistPrefixWarningOnly.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3MaximumRedistPrefixWarningOnly.setStatus(_A)
_RlOspfv3NextRouterId_Type=RouterID
_RlOspfv3NextRouterId_Object=MibTableColumn
rlOspfv3NextRouterId=_RlOspfv3NextRouterId_Object((1,3,6,1,4,1,4526,17,216,2,1,35),_RlOspfv3NextRouterId_Type())
rlOspfv3NextRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NextRouterId.setStatus(_A)
_RlOspfv3RouterIdType_Type=RlOspfRouterIdType
_RlOspfv3RouterIdType_Object=MibTableColumn
rlOspfv3RouterIdType=_RlOspfv3RouterIdType_Object((1,3,6,1,4,1,4526,17,216,2,1,36),_RlOspfv3RouterIdType_Type())
rlOspfv3RouterIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3RouterIdType.setStatus(_A)
_RlOspfv3NextRouterIdType_Type=RlOspfRouterIdType
_RlOspfv3NextRouterIdType_Object=MibTableColumn
rlOspfv3NextRouterIdType=_RlOspfv3NextRouterIdType_Object((1,3,6,1,4,1,4526,17,216,2,1,37),_RlOspfv3NextRouterIdType_Type())
rlOspfv3NextRouterIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NextRouterIdType.setStatus(_A)
_RlOspfv3ASBdrRtrActualStatus_Type=TruthValue
_RlOspfv3ASBdrRtrActualStatus_Object=MibTableColumn
rlOspfv3ASBdrRtrActualStatus=_RlOspfv3ASBdrRtrActualStatus_Object((1,3,6,1,4,1,4526,17,216,2,1,38),_RlOspfv3ASBdrRtrActualStatus_Type())
rlOspfv3ASBdrRtrActualStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3ASBdrRtrActualStatus.setStatus(_A)
class _RlOspfv3CalcMaxDelay_Type(Unsigned32):defaultValue=5000
_RlOspfv3CalcMaxDelay_Type.__name__=_J
_RlOspfv3CalcMaxDelay_Object=MibTableColumn
rlOspfv3CalcMaxDelay=_RlOspfv3CalcMaxDelay_Object((1,3,6,1,4,1,4526,17,216,2,1,39),_RlOspfv3CalcMaxDelay_Type())
rlOspfv3CalcMaxDelay.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3CalcMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3CalcMaxDelay.setUnits('milliseconds')
class _RlOspfv3RteMaxEqCostPaths_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlOspfv3RteMaxEqCostPaths_Type.__name__=_J
_RlOspfv3RteMaxEqCostPaths_Object=MibTableColumn
rlOspfv3RteMaxEqCostPaths=_RlOspfv3RteMaxEqCostPaths_Object((1,3,6,1,4,1,4526,17,216,2,1,40),_RlOspfv3RteMaxEqCostPaths_Type())
rlOspfv3RteMaxEqCostPaths.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3RteMaxEqCostPaths.setStatus(_A)
_RlOspfv3AreaTable_Object=MibTable
rlOspfv3AreaTable=_RlOspfv3AreaTable_Object((1,3,6,1,4,1,4526,17,216,3))
if mibBuilder.loadTexts:rlOspfv3AreaTable.setStatus(_A)
_RlOspfv3AreaEntry_Object=MibTableRow
rlOspfv3AreaEntry=_RlOspfv3AreaEntry_Object((1,3,6,1,4,1,4526,17,216,3,1))
rlOspfv3AreaEntry.setIndexNames((0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:rlOspfv3AreaEntry.setStatus(_A)
_RlOspfv3AreaProcessId_Type=RlOspfProcessID
_RlOspfv3AreaProcessId_Object=MibTableColumn
rlOspfv3AreaProcessId=_RlOspfv3AreaProcessId_Object((1,3,6,1,4,1,4526,17,216,3,1,1),_RlOspfv3AreaProcessId_Type())
rlOspfv3AreaProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaProcessId.setStatus(_A)
_RlOspfv3AreaId_Type=AreaID
_RlOspfv3AreaId_Object=MibTableColumn
rlOspfv3AreaId=_RlOspfv3AreaId_Object((1,3,6,1,4,1,4526,17,216,3,1,2),_RlOspfv3AreaId_Type())
rlOspfv3AreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaId.setStatus(_A)
class _RlOspfv3AreaImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_RlOspfv3AreaImportAsExtern_Type.__name__=_F
_RlOspfv3AreaImportAsExtern_Object=MibTableColumn
rlOspfv3AreaImportAsExtern=_RlOspfv3AreaImportAsExtern_Object((1,3,6,1,4,1,4526,17,216,3,1,3),_RlOspfv3AreaImportAsExtern_Type())
rlOspfv3AreaImportAsExtern.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaImportAsExtern.setStatus(_A)
_RlOspfv3AreaSpfRuns_Type=Counter32
_RlOspfv3AreaSpfRuns_Object=MibTableColumn
rlOspfv3AreaSpfRuns=_RlOspfv3AreaSpfRuns_Object((1,3,6,1,4,1,4526,17,216,3,1,4),_RlOspfv3AreaSpfRuns_Type())
rlOspfv3AreaSpfRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaSpfRuns.setStatus(_A)
class _RlOspfv3AreaBdrRtrCount_Type(Gauge32):defaultValue=0
_RlOspfv3AreaBdrRtrCount_Type.__name__=_R
_RlOspfv3AreaBdrRtrCount_Object=MibTableColumn
rlOspfv3AreaBdrRtrCount=_RlOspfv3AreaBdrRtrCount_Object((1,3,6,1,4,1,4526,17,216,3,1,5),_RlOspfv3AreaBdrRtrCount_Type())
rlOspfv3AreaBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaBdrRtrCount.setStatus(_A)
class _RlOspfv3AreaAsBdrRtrCount_Type(Gauge32):defaultValue=0
_RlOspfv3AreaAsBdrRtrCount_Type.__name__=_R
_RlOspfv3AreaAsBdrRtrCount_Object=MibTableColumn
rlOspfv3AreaAsBdrRtrCount=_RlOspfv3AreaAsBdrRtrCount_Object((1,3,6,1,4,1,4526,17,216,3,1,6),_RlOspfv3AreaAsBdrRtrCount_Type())
rlOspfv3AreaAsBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaAsBdrRtrCount.setStatus(_A)
class _RlOspfv3AreaScopeLsaCount_Type(Gauge32):defaultValue=0
_RlOspfv3AreaScopeLsaCount_Type.__name__=_R
_RlOspfv3AreaScopeLsaCount_Object=MibTableColumn
rlOspfv3AreaScopeLsaCount=_RlOspfv3AreaScopeLsaCount_Object((1,3,6,1,4,1,4526,17,216,3,1,7),_RlOspfv3AreaScopeLsaCount_Type())
rlOspfv3AreaScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaScopeLsaCount.setStatus(_A)
_RlOspfv3AreaScopeLsaCksumSum_Type=Unsigned32
_RlOspfv3AreaScopeLsaCksumSum_Object=MibTableColumn
rlOspfv3AreaScopeLsaCksumSum=_RlOspfv3AreaScopeLsaCksumSum_Object((1,3,6,1,4,1,4526,17,216,3,1,8),_RlOspfv3AreaScopeLsaCksumSum_Type())
rlOspfv3AreaScopeLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaScopeLsaCksumSum.setStatus(_A)
class _RlOspfv3AreaSummary_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_RlOspfv3AreaSummary_Type.__name__=_F
_RlOspfv3AreaSummary_Object=MibTableColumn
rlOspfv3AreaSummary=_RlOspfv3AreaSummary_Object((1,3,6,1,4,1,4526,17,216,3,1,9),_RlOspfv3AreaSummary_Type())
rlOspfv3AreaSummary.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaSummary.setStatus(_A)
_RlOspfv3AreaRowStatus_Type=RowStatus
_RlOspfv3AreaRowStatus_Object=MibTableColumn
rlOspfv3AreaRowStatus=_RlOspfv3AreaRowStatus_Object((1,3,6,1,4,1,4526,17,216,3,1,10),_RlOspfv3AreaRowStatus_Type())
rlOspfv3AreaRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaRowStatus.setStatus(_A)
_RlOspfv3AreaStubMetric_Type=BigMetric
_RlOspfv3AreaStubMetric_Object=MibTableColumn
rlOspfv3AreaStubMetric=_RlOspfv3AreaStubMetric_Object((1,3,6,1,4,1,4526,17,216,3,1,11),_RlOspfv3AreaStubMetric_Type())
rlOspfv3AreaStubMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaStubMetric.setStatus(_A)
class _RlOspfv3AreaNssaTranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_RlOspfv3AreaNssaTranslatorRole_Type.__name__=_F
_RlOspfv3AreaNssaTranslatorRole_Object=MibTableColumn
rlOspfv3AreaNssaTranslatorRole=_RlOspfv3AreaNssaTranslatorRole_Object((1,3,6,1,4,1,4526,17,216,3,1,12),_RlOspfv3AreaNssaTranslatorRole_Type())
rlOspfv3AreaNssaTranslatorRole.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaNssaTranslatorRole.setStatus(_A)
class _RlOspfv3AreaNssaTranslatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('elected',2),('disabled',3)))
_RlOspfv3AreaNssaTranslatorState_Type.__name__=_F
_RlOspfv3AreaNssaTranslatorState_Object=MibTableColumn
rlOspfv3AreaNssaTranslatorState=_RlOspfv3AreaNssaTranslatorState_Object((1,3,6,1,4,1,4526,17,216,3,1,13),_RlOspfv3AreaNssaTranslatorState_Type())
rlOspfv3AreaNssaTranslatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaNssaTranslatorState.setStatus(_A)
class _RlOspfv3AreaNssaTranslatorStabInterval_Type(Unsigned32):defaultValue=40
_RlOspfv3AreaNssaTranslatorStabInterval_Type.__name__=_J
_RlOspfv3AreaNssaTranslatorStabInterval_Object=MibTableColumn
rlOspfv3AreaNssaTranslatorStabInterval=_RlOspfv3AreaNssaTranslatorStabInterval_Object((1,3,6,1,4,1,4526,17,216,3,1,14),_RlOspfv3AreaNssaTranslatorStabInterval_Type())
rlOspfv3AreaNssaTranslatorStabInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaNssaTranslatorStabInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3AreaNssaTranslatorStabInterval.setUnits(_H)
_RlOspfv3AreaNssaTranslatorEvents_Type=Counter32
_RlOspfv3AreaNssaTranslatorEvents_Object=MibTableColumn
rlOspfv3AreaNssaTranslatorEvents=_RlOspfv3AreaNssaTranslatorEvents_Object((1,3,6,1,4,1,4526,17,216,3,1,15),_RlOspfv3AreaNssaTranslatorEvents_Type())
rlOspfv3AreaNssaTranslatorEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaNssaTranslatorEvents.setStatus(_A)
class _RlOspfv3AreaStubMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rlOspfv3Metric',1),('comparableCost',2),('nonComparable',3)))
_RlOspfv3AreaStubMetricType_Type.__name__=_F
_RlOspfv3AreaStubMetricType_Object=MibTableColumn
rlOspfv3AreaStubMetricType=_RlOspfv3AreaStubMetricType_Object((1,3,6,1,4,1,4526,17,216,3,1,16),_RlOspfv3AreaStubMetricType_Type())
rlOspfv3AreaStubMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaStubMetricType.setStatus(_A)
class _RlOspfv3AreaTEEnabled_Type(TruthValue):defaultValue=2
_RlOspfv3AreaTEEnabled_Type.__name__=_K
_RlOspfv3AreaTEEnabled_Object=MibTableColumn
rlOspfv3AreaTEEnabled=_RlOspfv3AreaTEEnabled_Object((1,3,6,1,4,1,4526,17,216,3,1,17),_RlOspfv3AreaTEEnabled_Type())
rlOspfv3AreaTEEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaTEEnabled.setStatus(_A)
class _RlOspfv3AreaAdminStat_Type(Status):defaultValue=1
_RlOspfv3AreaAdminStat_Type.__name__=_Q
_RlOspfv3AreaAdminStat_Object=MibTableColumn
rlOspfv3AreaAdminStat=_RlOspfv3AreaAdminStat_Object((1,3,6,1,4,1,4526,17,216,3,1,18),_RlOspfv3AreaAdminStat_Type())
rlOspfv3AreaAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaAdminStat.setStatus(_A)
class _RlOspfv3AreaOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_L,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfv3AreaOperStatus_Type.__name__=_F
_RlOspfv3AreaOperStatus_Object=MibTableColumn
rlOspfv3AreaOperStatus=_RlOspfv3AreaOperStatus_Object((1,3,6,1,4,1,4526,17,216,3,1,19),_RlOspfv3AreaOperStatus_Type())
rlOspfv3AreaOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaOperStatus.setStatus(_A)
class _RlOspfv3AreaFilterPrefixListIn_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlOspfv3AreaFilterPrefixListIn_Type.__name__=_f
_RlOspfv3AreaFilterPrefixListIn_Object=MibTableColumn
rlOspfv3AreaFilterPrefixListIn=_RlOspfv3AreaFilterPrefixListIn_Object((1,3,6,1,4,1,4526,17,216,3,1,20),_RlOspfv3AreaFilterPrefixListIn_Type())
rlOspfv3AreaFilterPrefixListIn.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3AreaFilterPrefixListIn.setStatus(_A)
class _RlOspfv3AreaFilterPrefixListOut_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlOspfv3AreaFilterPrefixListOut_Type.__name__=_f
_RlOspfv3AreaFilterPrefixListOut_Object=MibTableColumn
rlOspfv3AreaFilterPrefixListOut=_RlOspfv3AreaFilterPrefixListOut_Object((1,3,6,1,4,1,4526,17,216,3,1,21),_RlOspfv3AreaFilterPrefixListOut_Type())
rlOspfv3AreaFilterPrefixListOut.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3AreaFilterPrefixListOut.setStatus(_A)
_RlOspfv3AsLsdbTable_Object=MibTable
rlOspfv3AsLsdbTable=_RlOspfv3AsLsdbTable_Object((1,3,6,1,4,1,4526,17,216,4))
if mibBuilder.loadTexts:rlOspfv3AsLsdbTable.setStatus(_A)
_RlOspfv3AsLsdbEntry_Object=MibTableRow
rlOspfv3AsLsdbEntry=_RlOspfv3AsLsdbEntry_Object((1,3,6,1,4,1,4526,17,216,4,1))
rlOspfv3AsLsdbEntry.setIndexNames((0,_C,_t),(0,_C,_u),(0,_C,_v),(0,_C,_w))
if mibBuilder.loadTexts:rlOspfv3AsLsdbEntry.setStatus(_A)
_RlOspfv3AsLsdbProcessId_Type=RlOspfProcessID
_RlOspfv3AsLsdbProcessId_Object=MibTableColumn
rlOspfv3AsLsdbProcessId=_RlOspfv3AsLsdbProcessId_Object((1,3,6,1,4,1,4526,17,216,4,1,1),_RlOspfv3AsLsdbProcessId_Type())
rlOspfv3AsLsdbProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsLsdbProcessId.setStatus(_A)
class _RlOspfv3AsLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RlOspfv3AsLsdbType_Type.__name__=_J
_RlOspfv3AsLsdbType_Object=MibTableColumn
rlOspfv3AsLsdbType=_RlOspfv3AsLsdbType_Object((1,3,6,1,4,1,4526,17,216,4,1,2),_RlOspfv3AsLsdbType_Type())
rlOspfv3AsLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AsLsdbType.setStatus(_A)
_RlOspfv3AsLsdbRouterId_Type=RouterID
_RlOspfv3AsLsdbRouterId_Object=MibTableColumn
rlOspfv3AsLsdbRouterId=_RlOspfv3AsLsdbRouterId_Object((1,3,6,1,4,1,4526,17,216,4,1,3),_RlOspfv3AsLsdbRouterId_Type())
rlOspfv3AsLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AsLsdbRouterId.setStatus(_A)
_RlOspfv3AsLsdbLsid_Type=RlLsID
_RlOspfv3AsLsdbLsid_Object=MibTableColumn
rlOspfv3AsLsdbLsid=_RlOspfv3AsLsdbLsid_Object((1,3,6,1,4,1,4526,17,216,4,1,4),_RlOspfv3AsLsdbLsid_Type())
rlOspfv3AsLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AsLsdbLsid.setStatus(_A)
_RlOspfv3AsLsdbSequence_Type=Ospfv3LsaSequenceTC
_RlOspfv3AsLsdbSequence_Object=MibTableColumn
rlOspfv3AsLsdbSequence=_RlOspfv3AsLsdbSequence_Object((1,3,6,1,4,1,4526,17,216,4,1,5),_RlOspfv3AsLsdbSequence_Type())
rlOspfv3AsLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsLsdbSequence.setStatus(_A)
_RlOspfv3AsLsdbAge_Type=Ospfv3LsaAgeTC
_RlOspfv3AsLsdbAge_Object=MibTableColumn
rlOspfv3AsLsdbAge=_RlOspfv3AsLsdbAge_Object((1,3,6,1,4,1,4526,17,216,4,1,6),_RlOspfv3AsLsdbAge_Type())
rlOspfv3AsLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3AsLsdbAge.setUnits(_H)
_RlOspfv3AsLsdbChecksum_Type=Integer32
_RlOspfv3AsLsdbChecksum_Object=MibTableColumn
rlOspfv3AsLsdbChecksum=_RlOspfv3AsLsdbChecksum_Object((1,3,6,1,4,1,4526,17,216,4,1,7),_RlOspfv3AsLsdbChecksum_Type())
rlOspfv3AsLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsLsdbChecksum.setStatus(_A)
class _RlOspfv3AsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfv3AsLsdbAdvertisement_Type.__name__=_M
_RlOspfv3AsLsdbAdvertisement_Object=MibTableColumn
rlOspfv3AsLsdbAdvertisement=_RlOspfv3AsLsdbAdvertisement_Object((1,3,6,1,4,1,4526,17,216,4,1,8),_RlOspfv3AsLsdbAdvertisement_Type())
rlOspfv3AsLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsLsdbAdvertisement.setStatus(_A)
_RlOspfv3AsLsdbTypeKnown_Type=TruthValue
_RlOspfv3AsLsdbTypeKnown_Object=MibTableColumn
rlOspfv3AsLsdbTypeKnown=_RlOspfv3AsLsdbTypeKnown_Object((1,3,6,1,4,1,4526,17,216,4,1,9),_RlOspfv3AsLsdbTypeKnown_Type())
rlOspfv3AsLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AsLsdbTypeKnown.setStatus(_A)
_RlOspfv3AreaLsdbTable_Object=MibTable
rlOspfv3AreaLsdbTable=_RlOspfv3AreaLsdbTable_Object((1,3,6,1,4,1,4526,17,216,5))
if mibBuilder.loadTexts:rlOspfv3AreaLsdbTable.setStatus(_A)
_RlOspfv3AreaLsdbEntry_Object=MibTableRow
rlOspfv3AreaLsdbEntry=_RlOspfv3AreaLsdbEntry_Object((1,3,6,1,4,1,4526,17,216,5,1))
rlOspfv3AreaLsdbEntry.setIndexNames((0,_C,_x),(0,_C,_y),(0,_C,_z),(0,_C,_A0),(0,_C,_A1))
if mibBuilder.loadTexts:rlOspfv3AreaLsdbEntry.setStatus(_A)
_RlOspfv3AreaLsdbProcessId_Type=RlOspfProcessID
_RlOspfv3AreaLsdbProcessId_Object=MibTableColumn
rlOspfv3AreaLsdbProcessId=_RlOspfv3AreaLsdbProcessId_Object((1,3,6,1,4,1,4526,17,216,5,1,1),_RlOspfv3AreaLsdbProcessId_Type())
rlOspfv3AreaLsdbProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbProcessId.setStatus(_A)
_RlOspfv3AreaLsdbAreaId_Type=AreaID
_RlOspfv3AreaLsdbAreaId_Object=MibTableColumn
rlOspfv3AreaLsdbAreaId=_RlOspfv3AreaLsdbAreaId_Object((1,3,6,1,4,1,4526,17,216,5,1,2),_RlOspfv3AreaLsdbAreaId_Type())
rlOspfv3AreaLsdbAreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbAreaId.setStatus(_A)
class _RlOspfv3AreaLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RlOspfv3AreaLsdbType_Type.__name__=_J
_RlOspfv3AreaLsdbType_Object=MibTableColumn
rlOspfv3AreaLsdbType=_RlOspfv3AreaLsdbType_Object((1,3,6,1,4,1,4526,17,216,5,1,3),_RlOspfv3AreaLsdbType_Type())
rlOspfv3AreaLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbType.setStatus(_A)
_RlOspfv3AreaLsdbRouterId_Type=RouterID
_RlOspfv3AreaLsdbRouterId_Object=MibTableColumn
rlOspfv3AreaLsdbRouterId=_RlOspfv3AreaLsdbRouterId_Object((1,3,6,1,4,1,4526,17,216,5,1,4),_RlOspfv3AreaLsdbRouterId_Type())
rlOspfv3AreaLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbRouterId.setStatus(_A)
_RlOspfv3AreaLsdbLsid_Type=RlLsID
_RlOspfv3AreaLsdbLsid_Object=MibTableColumn
rlOspfv3AreaLsdbLsid=_RlOspfv3AreaLsdbLsid_Object((1,3,6,1,4,1,4526,17,216,5,1,5),_RlOspfv3AreaLsdbLsid_Type())
rlOspfv3AreaLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbLsid.setStatus(_A)
_RlOspfv3AreaLsdbSequence_Type=Ospfv3LsaSequenceTC
_RlOspfv3AreaLsdbSequence_Object=MibTableColumn
rlOspfv3AreaLsdbSequence=_RlOspfv3AreaLsdbSequence_Object((1,3,6,1,4,1,4526,17,216,5,1,6),_RlOspfv3AreaLsdbSequence_Type())
rlOspfv3AreaLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbSequence.setStatus(_A)
_RlOspfv3AreaLsdbAge_Type=Ospfv3LsaAgeTC
_RlOspfv3AreaLsdbAge_Object=MibTableColumn
rlOspfv3AreaLsdbAge=_RlOspfv3AreaLsdbAge_Object((1,3,6,1,4,1,4526,17,216,5,1,7),_RlOspfv3AreaLsdbAge_Type())
rlOspfv3AreaLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbAge.setUnits(_H)
_RlOspfv3AreaLsdbChecksum_Type=Integer32
_RlOspfv3AreaLsdbChecksum_Object=MibTableColumn
rlOspfv3AreaLsdbChecksum=_RlOspfv3AreaLsdbChecksum_Object((1,3,6,1,4,1,4526,17,216,5,1,8),_RlOspfv3AreaLsdbChecksum_Type())
rlOspfv3AreaLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbChecksum.setStatus(_A)
class _RlOspfv3AreaLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfv3AreaLsdbAdvertisement_Type.__name__=_M
_RlOspfv3AreaLsdbAdvertisement_Object=MibTableColumn
rlOspfv3AreaLsdbAdvertisement=_RlOspfv3AreaLsdbAdvertisement_Object((1,3,6,1,4,1,4526,17,216,5,1,9),_RlOspfv3AreaLsdbAdvertisement_Type())
rlOspfv3AreaLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbAdvertisement.setStatus(_A)
_RlOspfv3AreaLsdbTypeKnown_Type=TruthValue
_RlOspfv3AreaLsdbTypeKnown_Object=MibTableColumn
rlOspfv3AreaLsdbTypeKnown=_RlOspfv3AreaLsdbTypeKnown_Object((1,3,6,1,4,1,4526,17,216,5,1,10),_RlOspfv3AreaLsdbTypeKnown_Type())
rlOspfv3AreaLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaLsdbTypeKnown.setStatus(_A)
_RlOspfv3LinkLsdbTable_Object=MibTable
rlOspfv3LinkLsdbTable=_RlOspfv3LinkLsdbTable_Object((1,3,6,1,4,1,4526,17,216,6))
if mibBuilder.loadTexts:rlOspfv3LinkLsdbTable.setStatus(_A)
_RlOspfv3LinkLsdbEntry_Object=MibTableRow
rlOspfv3LinkLsdbEntry=_RlOspfv3LinkLsdbEntry_Object((1,3,6,1,4,1,4526,17,216,6,1))
rlOspfv3LinkLsdbEntry.setIndexNames((0,_C,_A2),(0,_C,_A3),(0,_C,_A4),(0,_C,_A5),(0,_C,_A6),(0,_C,_A7))
if mibBuilder.loadTexts:rlOspfv3LinkLsdbEntry.setStatus(_A)
_RlOspfv3LinkLsdbProcessId_Type=RlOspfProcessID
_RlOspfv3LinkLsdbProcessId_Object=MibTableColumn
rlOspfv3LinkLsdbProcessId=_RlOspfv3LinkLsdbProcessId_Object((1,3,6,1,4,1,4526,17,216,6,1,1),_RlOspfv3LinkLsdbProcessId_Type())
rlOspfv3LinkLsdbProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbProcessId.setStatus(_A)
_RlOspfv3LinkLsdbIfIndex_Type=InterfaceIndex
_RlOspfv3LinkLsdbIfIndex_Object=MibTableColumn
rlOspfv3LinkLsdbIfIndex=_RlOspfv3LinkLsdbIfIndex_Object((1,3,6,1,4,1,4526,17,216,6,1,2),_RlOspfv3LinkLsdbIfIndex_Type())
rlOspfv3LinkLsdbIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbIfIndex.setStatus(_A)
_RlOspfv3LinkLsdbIfInstId_Type=Ospfv3IfInstIdTC
_RlOspfv3LinkLsdbIfInstId_Object=MibTableColumn
rlOspfv3LinkLsdbIfInstId=_RlOspfv3LinkLsdbIfInstId_Object((1,3,6,1,4,1,4526,17,216,6,1,3),_RlOspfv3LinkLsdbIfInstId_Type())
rlOspfv3LinkLsdbIfInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbIfInstId.setStatus(_A)
class _RlOspfv3LinkLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RlOspfv3LinkLsdbType_Type.__name__=_J
_RlOspfv3LinkLsdbType_Object=MibTableColumn
rlOspfv3LinkLsdbType=_RlOspfv3LinkLsdbType_Object((1,3,6,1,4,1,4526,17,216,6,1,4),_RlOspfv3LinkLsdbType_Type())
rlOspfv3LinkLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbType.setStatus(_A)
_RlOspfv3LinkLsdbRouterId_Type=RouterID
_RlOspfv3LinkLsdbRouterId_Object=MibTableColumn
rlOspfv3LinkLsdbRouterId=_RlOspfv3LinkLsdbRouterId_Object((1,3,6,1,4,1,4526,17,216,6,1,5),_RlOspfv3LinkLsdbRouterId_Type())
rlOspfv3LinkLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbRouterId.setStatus(_A)
_RlOspfv3LinkLsdbLsid_Type=RlLsID
_RlOspfv3LinkLsdbLsid_Object=MibTableColumn
rlOspfv3LinkLsdbLsid=_RlOspfv3LinkLsdbLsid_Object((1,3,6,1,4,1,4526,17,216,6,1,6),_RlOspfv3LinkLsdbLsid_Type())
rlOspfv3LinkLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbLsid.setStatus(_A)
_RlOspfv3LinkLsdbSequence_Type=Ospfv3LsaSequenceTC
_RlOspfv3LinkLsdbSequence_Object=MibTableColumn
rlOspfv3LinkLsdbSequence=_RlOspfv3LinkLsdbSequence_Object((1,3,6,1,4,1,4526,17,216,6,1,7),_RlOspfv3LinkLsdbSequence_Type())
rlOspfv3LinkLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbSequence.setStatus(_A)
_RlOspfv3LinkLsdbAge_Type=Ospfv3LsaAgeTC
_RlOspfv3LinkLsdbAge_Object=MibTableColumn
rlOspfv3LinkLsdbAge=_RlOspfv3LinkLsdbAge_Object((1,3,6,1,4,1,4526,17,216,6,1,8),_RlOspfv3LinkLsdbAge_Type())
rlOspfv3LinkLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbAge.setUnits(_H)
_RlOspfv3LinkLsdbChecksum_Type=Integer32
_RlOspfv3LinkLsdbChecksum_Object=MibTableColumn
rlOspfv3LinkLsdbChecksum=_RlOspfv3LinkLsdbChecksum_Object((1,3,6,1,4,1,4526,17,216,6,1,9),_RlOspfv3LinkLsdbChecksum_Type())
rlOspfv3LinkLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbChecksum.setStatus(_A)
class _RlOspfv3LinkLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfv3LinkLsdbAdvertisement_Type.__name__=_M
_RlOspfv3LinkLsdbAdvertisement_Object=MibTableColumn
rlOspfv3LinkLsdbAdvertisement=_RlOspfv3LinkLsdbAdvertisement_Object((1,3,6,1,4,1,4526,17,216,6,1,10),_RlOspfv3LinkLsdbAdvertisement_Type())
rlOspfv3LinkLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbAdvertisement.setStatus(_A)
_RlOspfv3LinkLsdbTypeKnown_Type=TruthValue
_RlOspfv3LinkLsdbTypeKnown_Object=MibTableColumn
rlOspfv3LinkLsdbTypeKnown=_RlOspfv3LinkLsdbTypeKnown_Object((1,3,6,1,4,1,4526,17,216,6,1,11),_RlOspfv3LinkLsdbTypeKnown_Type())
rlOspfv3LinkLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3LinkLsdbTypeKnown.setStatus(_A)
_RlOspfv3HostTable_Object=MibTable
rlOspfv3HostTable=_RlOspfv3HostTable_Object((1,3,6,1,4,1,4526,17,216,7))
if mibBuilder.loadTexts:rlOspfv3HostTable.setStatus(_A)
_RlOspfv3HostEntry_Object=MibTableRow
rlOspfv3HostEntry=_RlOspfv3HostEntry_Object((1,3,6,1,4,1,4526,17,216,7,1))
rlOspfv3HostEntry.setIndexNames((0,_C,_A8),(0,_C,_A9),(0,_C,_AA))
if mibBuilder.loadTexts:rlOspfv3HostEntry.setStatus(_A)
_RlOspfv3HostProcessId_Type=RlOspfProcessID
_RlOspfv3HostProcessId_Object=MibTableColumn
rlOspfv3HostProcessId=_RlOspfv3HostProcessId_Object((1,3,6,1,4,1,4526,17,216,7,1,1),_RlOspfv3HostProcessId_Type())
rlOspfv3HostProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3HostProcessId.setStatus(_A)
_RlOspfv3HostAddressType_Type=InetAddressType
_RlOspfv3HostAddressType_Object=MibTableColumn
rlOspfv3HostAddressType=_RlOspfv3HostAddressType_Object((1,3,6,1,4,1,4526,17,216,7,1,2),_RlOspfv3HostAddressType_Type())
rlOspfv3HostAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3HostAddressType.setStatus(_A)
_RlOspfv3HostAddress_Type=InetAddress
_RlOspfv3HostAddress_Object=MibTableColumn
rlOspfv3HostAddress=_RlOspfv3HostAddress_Object((1,3,6,1,4,1,4526,17,216,7,1,3),_RlOspfv3HostAddress_Type())
rlOspfv3HostAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3HostAddress.setStatus(_A)
_RlOspfv3HostMetric_Type=Metric
_RlOspfv3HostMetric_Object=MibTableColumn
rlOspfv3HostMetric=_RlOspfv3HostMetric_Object((1,3,6,1,4,1,4526,17,216,7,1,4),_RlOspfv3HostMetric_Type())
rlOspfv3HostMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3HostMetric.setStatus(_A)
_RlOspfv3HostRowStatus_Type=RowStatus
_RlOspfv3HostRowStatus_Object=MibTableColumn
rlOspfv3HostRowStatus=_RlOspfv3HostRowStatus_Object((1,3,6,1,4,1,4526,17,216,7,1,5),_RlOspfv3HostRowStatus_Type())
rlOspfv3HostRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3HostRowStatus.setStatus(_A)
_RlOspfv3HostAreaID_Type=AreaID
_RlOspfv3HostAreaID_Object=MibTableColumn
rlOspfv3HostAreaID=_RlOspfv3HostAreaID_Object((1,3,6,1,4,1,4526,17,216,7,1,6),_RlOspfv3HostAreaID_Type())
rlOspfv3HostAreaID.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3HostAreaID.setStatus(_A)
_RlOspfv3IfTable_Object=MibTable
rlOspfv3IfTable=_RlOspfv3IfTable_Object((1,3,6,1,4,1,4526,17,216,8))
if mibBuilder.loadTexts:rlOspfv3IfTable.setStatus(_A)
_RlOspfv3IfEntry_Object=MibTableRow
rlOspfv3IfEntry=_RlOspfv3IfEntry_Object((1,3,6,1,4,1,4526,17,216,8,1))
rlOspfv3IfEntry.setIndexNames((0,_C,_AB),(0,_C,_AC),(0,_C,_AD))
if mibBuilder.loadTexts:rlOspfv3IfEntry.setStatus(_A)
_RlOspfv3IfProcessId_Type=RlOspfProcessID
_RlOspfv3IfProcessId_Object=MibTableColumn
rlOspfv3IfProcessId=_RlOspfv3IfProcessId_Object((1,3,6,1,4,1,4526,17,216,8,1,1),_RlOspfv3IfProcessId_Type())
rlOspfv3IfProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfProcessId.setStatus(_A)
_RlOspfv3IfIndex_Type=InterfaceIndex
_RlOspfv3IfIndex_Object=MibTableColumn
rlOspfv3IfIndex=_RlOspfv3IfIndex_Object((1,3,6,1,4,1,4526,17,216,8,1,2),_RlOspfv3IfIndex_Type())
rlOspfv3IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3IfIndex.setStatus(_A)
_RlOspfv3IfInstId_Type=Ospfv3IfInstIdTC
_RlOspfv3IfInstId_Object=MibTableColumn
rlOspfv3IfInstId=_RlOspfv3IfInstId_Object((1,3,6,1,4,1,4526,17,216,8,1,3),_RlOspfv3IfInstId_Type())
rlOspfv3IfInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3IfInstId.setStatus(_A)
_RlOspfv3IfAreaId_Type=AreaID
_RlOspfv3IfAreaId_Object=MibTableColumn
rlOspfv3IfAreaId=_RlOspfv3IfAreaId_Object((1,3,6,1,4,1,4526,17,216,8,1,4),_RlOspfv3IfAreaId_Type())
rlOspfv3IfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfAreaId.setStatus(_A)
class _RlOspfv3IfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_i,3),('pointToMultipoint',5)))
_RlOspfv3IfType_Type.__name__=_F
_RlOspfv3IfType_Object=MibTableColumn
rlOspfv3IfType=_RlOspfv3IfType_Object((1,3,6,1,4,1,4526,17,216,8,1,5),_RlOspfv3IfType_Type())
rlOspfv3IfType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfType.setStatus(_A)
class _RlOspfv3IfAdminStatus_Type(Status):defaultValue=1
_RlOspfv3IfAdminStatus_Type.__name__=_Q
_RlOspfv3IfAdminStatus_Object=MibTableColumn
rlOspfv3IfAdminStatus=_RlOspfv3IfAdminStatus_Object((1,3,6,1,4,1,4526,17,216,8,1,6),_RlOspfv3IfAdminStatus_Type())
rlOspfv3IfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfAdminStatus.setStatus(_A)
class _RlOspfv3IfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RlOspfv3IfRtrPriority_Type.__name__=_c
_RlOspfv3IfRtrPriority_Object=MibTableColumn
rlOspfv3IfRtrPriority=_RlOspfv3IfRtrPriority_Object((1,3,6,1,4,1,4526,17,216,8,1,7),_RlOspfv3IfRtrPriority_Type())
rlOspfv3IfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfRtrPriority.setStatus(_A)
class _RlOspfv3IfTransitDelay_Type(RlOspfv3UpToRefreshIntervalTC):defaultValue=1
_RlOspfv3IfTransitDelay_Type.__name__=_O
_RlOspfv3IfTransitDelay_Object=MibTableColumn
rlOspfv3IfTransitDelay=_RlOspfv3IfTransitDelay_Object((1,3,6,1,4,1,4526,17,216,8,1,8),_RlOspfv3IfTransitDelay_Type())
rlOspfv3IfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfTransitDelay.setUnits(_H)
class _RlOspfv3IfRetransInterval_Type(RlOspfv3UpToRefreshIntervalTC):defaultValue=5
_RlOspfv3IfRetransInterval_Type.__name__=_O
_RlOspfv3IfRetransInterval_Object=MibTableColumn
rlOspfv3IfRetransInterval=_RlOspfv3IfRetransInterval_Object((1,3,6,1,4,1,4526,17,216,8,1,9),_RlOspfv3IfRetransInterval_Type())
rlOspfv3IfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfRetransInterval.setUnits(_H)
class _RlOspfv3IfHelloInterval_Type(HelloRange):defaultValue=10
_RlOspfv3IfHelloInterval_Type.__name__=_d
_RlOspfv3IfHelloInterval_Object=MibTableColumn
rlOspfv3IfHelloInterval=_RlOspfv3IfHelloInterval_Object((1,3,6,1,4,1,4526,17,216,8,1,10),_RlOspfv3IfHelloInterval_Type())
rlOspfv3IfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfHelloInterval.setUnits(_H)
class _RlOspfv3IfRtrDeadInterval_Type(Ospfv3DeadIntervalRangeTC):defaultValue=40
_RlOspfv3IfRtrDeadInterval_Type.__name__=_e
_RlOspfv3IfRtrDeadInterval_Object=MibTableColumn
rlOspfv3IfRtrDeadInterval=_RlOspfv3IfRtrDeadInterval_Object((1,3,6,1,4,1,4526,17,216,8,1,11),_RlOspfv3IfRtrDeadInterval_Type())
rlOspfv3IfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfRtrDeadInterval.setUnits(_H)
class _RlOspfv3IfPollInterval_Type(Unsigned32):defaultValue=120
_RlOspfv3IfPollInterval_Type.__name__=_J
_RlOspfv3IfPollInterval_Object=MibTableColumn
rlOspfv3IfPollInterval=_RlOspfv3IfPollInterval_Object((1,3,6,1,4,1,4526,17,216,8,1,12),_RlOspfv3IfPollInterval_Type())
rlOspfv3IfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfPollInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfPollInterval.setUnits(_H)
class _RlOspfv3IfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),('loopback',2),('waiting',3),(_i,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7),('standby',8)))
_RlOspfv3IfState_Type.__name__=_F
_RlOspfv3IfState_Object=MibTableColumn
rlOspfv3IfState=_RlOspfv3IfState_Object((1,3,6,1,4,1,4526,17,216,8,1,13),_RlOspfv3IfState_Type())
rlOspfv3IfState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfState.setStatus(_A)
_RlOspfv3IfDesignatedRouter_Type=RouterID
_RlOspfv3IfDesignatedRouter_Object=MibTableColumn
rlOspfv3IfDesignatedRouter=_RlOspfv3IfDesignatedRouter_Object((1,3,6,1,4,1,4526,17,216,8,1,14),_RlOspfv3IfDesignatedRouter_Type())
rlOspfv3IfDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfDesignatedRouter.setStatus(_A)
_RlOspfv3IfBackupDesignatedRouter_Type=RouterID
_RlOspfv3IfBackupDesignatedRouter_Object=MibTableColumn
rlOspfv3IfBackupDesignatedRouter=_RlOspfv3IfBackupDesignatedRouter_Object((1,3,6,1,4,1,4526,17,216,8,1,15),_RlOspfv3IfBackupDesignatedRouter_Type())
rlOspfv3IfBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfBackupDesignatedRouter.setStatus(_A)
_RlOspfv3IfEvents_Type=Counter32
_RlOspfv3IfEvents_Object=MibTableColumn
rlOspfv3IfEvents=_RlOspfv3IfEvents_Object((1,3,6,1,4,1,4526,17,216,8,1,16),_RlOspfv3IfEvents_Type())
rlOspfv3IfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfEvents.setStatus(_A)
_RlOspfv3IfRowStatus_Type=RowStatus
_RlOspfv3IfRowStatus_Object=MibTableColumn
rlOspfv3IfRowStatus=_RlOspfv3IfRowStatus_Object((1,3,6,1,4,1,4526,17,216,8,1,17),_RlOspfv3IfRowStatus_Type())
rlOspfv3IfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfRowStatus.setStatus(_A)
class _RlOspfv3IfDemand_Type(TruthValue):defaultValue=2
_RlOspfv3IfDemand_Type.__name__=_K
_RlOspfv3IfDemand_Object=MibTableColumn
rlOspfv3IfDemand=_RlOspfv3IfDemand_Object((1,3,6,1,4,1,4526,17,216,8,1,18),_RlOspfv3IfDemand_Type())
rlOspfv3IfDemand.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfDemand.setStatus(_A)
_RlOspfv3IfMetricValue_Type=Metric
_RlOspfv3IfMetricValue_Object=MibTableColumn
rlOspfv3IfMetricValue=_RlOspfv3IfMetricValue_Object((1,3,6,1,4,1,4526,17,216,8,1,19),_RlOspfv3IfMetricValue_Type())
rlOspfv3IfMetricValue.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfMetricValue.setStatus(_A)
_RlOspfv3IfLinkScopeLsaCount_Type=Gauge32
_RlOspfv3IfLinkScopeLsaCount_Object=MibTableColumn
rlOspfv3IfLinkScopeLsaCount=_RlOspfv3IfLinkScopeLsaCount_Object((1,3,6,1,4,1,4526,17,216,8,1,20),_RlOspfv3IfLinkScopeLsaCount_Type())
rlOspfv3IfLinkScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfLinkScopeLsaCount.setStatus(_A)
_RlOspfv3IfLinkLsaCksumSum_Type=Unsigned32
_RlOspfv3IfLinkLsaCksumSum_Object=MibTableColumn
rlOspfv3IfLinkLsaCksumSum=_RlOspfv3IfLinkLsaCksumSum_Object((1,3,6,1,4,1,4526,17,216,8,1,21),_RlOspfv3IfLinkLsaCksumSum_Type())
rlOspfv3IfLinkLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfLinkLsaCksumSum.setStatus(_A)
class _RlOspfv3IfDemandNbrProbe_Type(TruthValue):defaultValue=2
_RlOspfv3IfDemandNbrProbe_Type.__name__=_K
_RlOspfv3IfDemandNbrProbe_Object=MibTableColumn
rlOspfv3IfDemandNbrProbe=_RlOspfv3IfDemandNbrProbe_Object((1,3,6,1,4,1,4526,17,216,8,1,22),_RlOspfv3IfDemandNbrProbe_Type())
rlOspfv3IfDemandNbrProbe.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfDemandNbrProbe.setStatus(_A)
class _RlOspfv3IfDemandNbrProbeRetransLimit_Type(Unsigned32):defaultValue=10
_RlOspfv3IfDemandNbrProbeRetransLimit_Type.__name__=_J
_RlOspfv3IfDemandNbrProbeRetransLimit_Object=MibTableColumn
rlOspfv3IfDemandNbrProbeRetransLimit=_RlOspfv3IfDemandNbrProbeRetransLimit_Object((1,3,6,1,4,1,4526,17,216,8,1,23),_RlOspfv3IfDemandNbrProbeRetransLimit_Type())
rlOspfv3IfDemandNbrProbeRetransLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfDemandNbrProbeRetransLimit.setStatus(_A)
class _RlOspfv3IfDemandNbrProbeInterval_Type(Unsigned32):defaultValue=120
_RlOspfv3IfDemandNbrProbeInterval_Type.__name__=_J
_RlOspfv3IfDemandNbrProbeInterval_Object=MibTableColumn
rlOspfv3IfDemandNbrProbeInterval=_RlOspfv3IfDemandNbrProbeInterval_Object((1,3,6,1,4,1,4526,17,216,8,1,24),_RlOspfv3IfDemandNbrProbeInterval_Type())
rlOspfv3IfDemandNbrProbeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfDemandNbrProbeInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfDemandNbrProbeInterval.setUnits(_H)
class _RlOspfv3IfTEDisabled_Type(TruthValue):defaultValue=2
_RlOspfv3IfTEDisabled_Type.__name__=_K
_RlOspfv3IfTEDisabled_Object=MibTableColumn
rlOspfv3IfTEDisabled=_RlOspfv3IfTEDisabled_Object((1,3,6,1,4,1,4526,17,216,8,1,25),_RlOspfv3IfTEDisabled_Type())
rlOspfv3IfTEDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfTEDisabled.setStatus(_A)
class _RlOspfv3IfLinkLSASuppression_Type(TruthValue):defaultValue=2
_RlOspfv3IfLinkLSASuppression_Type.__name__=_K
_RlOspfv3IfLinkLSASuppression_Object=MibTableColumn
rlOspfv3IfLinkLSASuppression=_RlOspfv3IfLinkLSASuppression_Object((1,3,6,1,4,1,4526,17,216,8,1,26),_RlOspfv3IfLinkLSASuppression_Type())
rlOspfv3IfLinkLSASuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfLinkLSASuppression.setStatus(_A)
class _RlOspfv3IfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_L,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfv3IfOperStatus_Type.__name__=_F
_RlOspfv3IfOperStatus_Object=MibTableColumn
rlOspfv3IfOperStatus=_RlOspfv3IfOperStatus_Object((1,3,6,1,4,1,4526,17,216,8,1,27),_RlOspfv3IfOperStatus_Type())
rlOspfv3IfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3IfOperStatus.setStatus(_A)
class _RlOspfv3IfPassive_Type(TruthValue):defaultValue=2
_RlOspfv3IfPassive_Type.__name__=_K
_RlOspfv3IfPassive_Object=MibTableColumn
rlOspfv3IfPassive=_RlOspfv3IfPassive_Object((1,3,6,1,4,1,4526,17,216,8,1,28),_RlOspfv3IfPassive_Type())
rlOspfv3IfPassive.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3IfPassive.setStatus(_A)
class _RlOspfv3IfLsaRefreshIntvl_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3599))
_RlOspfv3IfLsaRefreshIntvl_Type.__name__=_F
_RlOspfv3IfLsaRefreshIntvl_Object=MibTableColumn
rlOspfv3IfLsaRefreshIntvl=_RlOspfv3IfLsaRefreshIntvl_Object((1,3,6,1,4,1,4526,17,216,8,1,29),_RlOspfv3IfLsaRefreshIntvl_Type())
rlOspfv3IfLsaRefreshIntvl.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3IfLsaRefreshIntvl.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3IfLsaRefreshIntvl.setUnits(_H)
class _RlOspfv3IfFastHelloMultiplier_Type(RlOspfv3FastHelloMultiplierRange):defaultValue=5
_RlOspfv3IfFastHelloMultiplier_Type.__name__=_AE
_RlOspfv3IfFastHelloMultiplier_Object=MibTableColumn
rlOspfv3IfFastHelloMultiplier=_RlOspfv3IfFastHelloMultiplier_Object((1,3,6,1,4,1,4526,17,216,8,1,30),_RlOspfv3IfFastHelloMultiplier_Type())
rlOspfv3IfFastHelloMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3IfFastHelloMultiplier.setStatus(_A)
class _RlOspfv3IfMtuIgnore_Type(TruthValue):defaultValue=2
_RlOspfv3IfMtuIgnore_Type.__name__=_K
_RlOspfv3IfMtuIgnore_Object=MibTableColumn
rlOspfv3IfMtuIgnore=_RlOspfv3IfMtuIgnore_Object((1,3,6,1,4,1,4526,17,216,8,1,31),_RlOspfv3IfMtuIgnore_Type())
rlOspfv3IfMtuIgnore.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3IfMtuIgnore.setStatus(_A)
_RlOspfv3IfNameLookup_Type=TruthValue
_RlOspfv3IfNameLookup_Object=MibTableColumn
rlOspfv3IfNameLookup=_RlOspfv3IfNameLookup_Object((1,3,6,1,4,1,4526,17,216,8,1,32),_RlOspfv3IfNameLookup_Type())
rlOspfv3IfNameLookup.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3IfNameLookup.setStatus(_A)
_RlOspfv3VirtIfTable_Object=MibTable
rlOspfv3VirtIfTable=_RlOspfv3VirtIfTable_Object((1,3,6,1,4,1,4526,17,216,9))
if mibBuilder.loadTexts:rlOspfv3VirtIfTable.setStatus(_A)
_RlOspfv3VirtIfEntry_Object=MibTableRow
rlOspfv3VirtIfEntry=_RlOspfv3VirtIfEntry_Object((1,3,6,1,4,1,4526,17,216,9,1))
rlOspfv3VirtIfEntry.setIndexNames((0,_C,_AF),(0,_C,_AG),(0,_C,_AH))
if mibBuilder.loadTexts:rlOspfv3VirtIfEntry.setStatus(_A)
_RlOspfv3VirtIfProcessId_Type=RlOspfProcessID
_RlOspfv3VirtIfProcessId_Object=MibTableColumn
rlOspfv3VirtIfProcessId=_RlOspfv3VirtIfProcessId_Object((1,3,6,1,4,1,4526,17,216,9,1,1),_RlOspfv3VirtIfProcessId_Type())
rlOspfv3VirtIfProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfProcessId.setStatus(_A)
_RlOspfv3VirtIfAreaId_Type=AreaID
_RlOspfv3VirtIfAreaId_Object=MibTableColumn
rlOspfv3VirtIfAreaId=_RlOspfv3VirtIfAreaId_Object((1,3,6,1,4,1,4526,17,216,9,1,2),_RlOspfv3VirtIfAreaId_Type())
rlOspfv3VirtIfAreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtIfAreaId.setStatus(_A)
_RlOspfv3VirtIfNeighbor_Type=RouterID
_RlOspfv3VirtIfNeighbor_Object=MibTableColumn
rlOspfv3VirtIfNeighbor=_RlOspfv3VirtIfNeighbor_Object((1,3,6,1,4,1,4526,17,216,9,1,3),_RlOspfv3VirtIfNeighbor_Type())
rlOspfv3VirtIfNeighbor.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtIfNeighbor.setStatus(_A)
_RlOspfv3VirtIfIndex_Type=InterfaceIndex
_RlOspfv3VirtIfIndex_Object=MibTableColumn
rlOspfv3VirtIfIndex=_RlOspfv3VirtIfIndex_Object((1,3,6,1,4,1,4526,17,216,9,1,4),_RlOspfv3VirtIfIndex_Type())
rlOspfv3VirtIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfIndex.setStatus(_A)
_RlOspfv3VirtIfInstId_Type=Ospfv3IfInstIdTC
_RlOspfv3VirtIfInstId_Object=MibTableColumn
rlOspfv3VirtIfInstId=_RlOspfv3VirtIfInstId_Object((1,3,6,1,4,1,4526,17,216,9,1,5),_RlOspfv3VirtIfInstId_Type())
rlOspfv3VirtIfInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfInstId.setStatus(_A)
class _RlOspfv3VirtIfTransitDelay_Type(RlOspfv3UpToRefreshIntervalTC):defaultValue=1
_RlOspfv3VirtIfTransitDelay_Type.__name__=_O
_RlOspfv3VirtIfTransitDelay_Object=MibTableColumn
rlOspfv3VirtIfTransitDelay=_RlOspfv3VirtIfTransitDelay_Object((1,3,6,1,4,1,4526,17,216,9,1,6),_RlOspfv3VirtIfTransitDelay_Type())
rlOspfv3VirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3VirtIfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3VirtIfTransitDelay.setUnits(_H)
class _RlOspfv3VirtIfRetransInterval_Type(RlOspfv3UpToRefreshIntervalTC):defaultValue=5
_RlOspfv3VirtIfRetransInterval_Type.__name__=_O
_RlOspfv3VirtIfRetransInterval_Object=MibTableColumn
rlOspfv3VirtIfRetransInterval=_RlOspfv3VirtIfRetransInterval_Object((1,3,6,1,4,1,4526,17,216,9,1,7),_RlOspfv3VirtIfRetransInterval_Type())
rlOspfv3VirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3VirtIfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3VirtIfRetransInterval.setUnits(_H)
class _RlOspfv3VirtIfHelloInterval_Type(HelloRange):defaultValue=10
_RlOspfv3VirtIfHelloInterval_Type.__name__=_d
_RlOspfv3VirtIfHelloInterval_Object=MibTableColumn
rlOspfv3VirtIfHelloInterval=_RlOspfv3VirtIfHelloInterval_Object((1,3,6,1,4,1,4526,17,216,9,1,8),_RlOspfv3VirtIfHelloInterval_Type())
rlOspfv3VirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3VirtIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3VirtIfHelloInterval.setUnits(_H)
class _RlOspfv3VirtIfRtrDeadInterval_Type(Ospfv3DeadIntervalRangeTC):defaultValue=60
_RlOspfv3VirtIfRtrDeadInterval_Type.__name__=_e
_RlOspfv3VirtIfRtrDeadInterval_Object=MibTableColumn
rlOspfv3VirtIfRtrDeadInterval=_RlOspfv3VirtIfRtrDeadInterval_Object((1,3,6,1,4,1,4526,17,216,9,1,9),_RlOspfv3VirtIfRtrDeadInterval_Type())
rlOspfv3VirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3VirtIfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3VirtIfRtrDeadInterval.setUnits(_H)
class _RlOspfv3VirtIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_L,1),(_i,4)))
_RlOspfv3VirtIfState_Type.__name__=_F
_RlOspfv3VirtIfState_Object=MibTableColumn
rlOspfv3VirtIfState=_RlOspfv3VirtIfState_Object((1,3,6,1,4,1,4526,17,216,9,1,10),_RlOspfv3VirtIfState_Type())
rlOspfv3VirtIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfState.setStatus(_A)
_RlOspfv3VirtIfEvents_Type=Counter32
_RlOspfv3VirtIfEvents_Object=MibTableColumn
rlOspfv3VirtIfEvents=_RlOspfv3VirtIfEvents_Object((1,3,6,1,4,1,4526,17,216,9,1,11),_RlOspfv3VirtIfEvents_Type())
rlOspfv3VirtIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfEvents.setStatus(_A)
_RlOspfv3VirtIfRowStatus_Type=RowStatus
_RlOspfv3VirtIfRowStatus_Object=MibTableColumn
rlOspfv3VirtIfRowStatus=_RlOspfv3VirtIfRowStatus_Object((1,3,6,1,4,1,4526,17,216,9,1,12),_RlOspfv3VirtIfRowStatus_Type())
rlOspfv3VirtIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3VirtIfRowStatus.setStatus(_A)
_RlOspfv3VirtIfLinkScopeLsaCount_Type=Gauge32
_RlOspfv3VirtIfLinkScopeLsaCount_Object=MibTableColumn
rlOspfv3VirtIfLinkScopeLsaCount=_RlOspfv3VirtIfLinkScopeLsaCount_Object((1,3,6,1,4,1,4526,17,216,9,1,13),_RlOspfv3VirtIfLinkScopeLsaCount_Type())
rlOspfv3VirtIfLinkScopeLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfLinkScopeLsaCount.setStatus(_A)
_RlOspfv3VirtIfLinkLsaCksumSum_Type=Unsigned32
_RlOspfv3VirtIfLinkLsaCksumSum_Object=MibTableColumn
rlOspfv3VirtIfLinkLsaCksumSum=_RlOspfv3VirtIfLinkLsaCksumSum_Object((1,3,6,1,4,1,4526,17,216,9,1,14),_RlOspfv3VirtIfLinkLsaCksumSum_Type())
rlOspfv3VirtIfLinkLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfLinkLsaCksumSum.setStatus(_A)
class _RlOspfv3VirtIfAdminStatus_Type(Status):defaultValue=1
_RlOspfv3VirtIfAdminStatus_Type.__name__=_Q
_RlOspfv3VirtIfAdminStatus_Object=MibTableColumn
rlOspfv3VirtIfAdminStatus=_RlOspfv3VirtIfAdminStatus_Object((1,3,6,1,4,1,4526,17,216,9,1,15),_RlOspfv3VirtIfAdminStatus_Type())
rlOspfv3VirtIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3VirtIfAdminStatus.setStatus(_A)
class _RlOspfv3VirtIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_L,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfv3VirtIfOperStatus_Type.__name__=_F
_RlOspfv3VirtIfOperStatus_Object=MibTableColumn
rlOspfv3VirtIfOperStatus=_RlOspfv3VirtIfOperStatus_Object((1,3,6,1,4,1,4526,17,216,9,1,16),_RlOspfv3VirtIfOperStatus_Type())
rlOspfv3VirtIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtIfOperStatus.setStatus(_A)
_RlOspfv3NbrTable_Object=MibTable
rlOspfv3NbrTable=_RlOspfv3NbrTable_Object((1,3,6,1,4,1,4526,17,216,10))
if mibBuilder.loadTexts:rlOspfv3NbrTable.setStatus(_A)
_RlOspfv3NbrEntry_Object=MibTableRow
rlOspfv3NbrEntry=_RlOspfv3NbrEntry_Object((1,3,6,1,4,1,4526,17,216,10,1))
rlOspfv3NbrEntry.setIndexNames((0,_C,_AI),(0,_C,_AJ),(0,_C,_AK),(0,_C,_AL))
if mibBuilder.loadTexts:rlOspfv3NbrEntry.setStatus(_A)
_RlOspfv3NbrProcessId_Type=RlOspfProcessID
_RlOspfv3NbrProcessId_Object=MibTableColumn
rlOspfv3NbrProcessId=_RlOspfv3NbrProcessId_Object((1,3,6,1,4,1,4526,17,216,10,1,1),_RlOspfv3NbrProcessId_Type())
rlOspfv3NbrProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrProcessId.setStatus(_A)
_RlOspfv3NbrIfIndex_Type=InterfaceIndex
_RlOspfv3NbrIfIndex_Object=MibTableColumn
rlOspfv3NbrIfIndex=_RlOspfv3NbrIfIndex_Object((1,3,6,1,4,1,4526,17,216,10,1,2),_RlOspfv3NbrIfIndex_Type())
rlOspfv3NbrIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3NbrIfIndex.setStatus(_A)
_RlOspfv3NbrIfInstId_Type=Ospfv3IfInstIdTC
_RlOspfv3NbrIfInstId_Object=MibTableColumn
rlOspfv3NbrIfInstId=_RlOspfv3NbrIfInstId_Object((1,3,6,1,4,1,4526,17,216,10,1,3),_RlOspfv3NbrIfInstId_Type())
rlOspfv3NbrIfInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3NbrIfInstId.setStatus(_A)
_RlOspfv3NbrRtrId_Type=RouterID
_RlOspfv3NbrRtrId_Object=MibTableColumn
rlOspfv3NbrRtrId=_RlOspfv3NbrRtrId_Object((1,3,6,1,4,1,4526,17,216,10,1,4),_RlOspfv3NbrRtrId_Type())
rlOspfv3NbrRtrId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3NbrRtrId.setStatus(_A)
_RlOspfv3NbrAddressType_Type=InetAddressType
_RlOspfv3NbrAddressType_Object=MibTableColumn
rlOspfv3NbrAddressType=_RlOspfv3NbrAddressType_Object((1,3,6,1,4,1,4526,17,216,10,1,5),_RlOspfv3NbrAddressType_Type())
rlOspfv3NbrAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrAddressType.setStatus(_A)
_RlOspfv3NbrAddress_Type=InetAddress
_RlOspfv3NbrAddress_Object=MibTableColumn
rlOspfv3NbrAddress=_RlOspfv3NbrAddress_Object((1,3,6,1,4,1,4526,17,216,10,1,6),_RlOspfv3NbrAddress_Type())
rlOspfv3NbrAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrAddress.setStatus(_A)
_RlOspfv3NbrOptions_Type=Integer32
_RlOspfv3NbrOptions_Object=MibTableColumn
rlOspfv3NbrOptions=_RlOspfv3NbrOptions_Object((1,3,6,1,4,1,4526,17,216,10,1,7),_RlOspfv3NbrOptions_Type())
rlOspfv3NbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrOptions.setStatus(_A)
_RlOspfv3NbrPriority_Type=DesignatedRouterPriority
_RlOspfv3NbrPriority_Object=MibTableColumn
rlOspfv3NbrPriority=_RlOspfv3NbrPriority_Object((1,3,6,1,4,1,4526,17,216,10,1,8),_RlOspfv3NbrPriority_Type())
rlOspfv3NbrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrPriority.setStatus(_A)
class _RlOspfv3NbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),('attempt',2),('init',3),('twoWay',4),(_AM,5),('exchange',6),('loading',7),('full',8)))
_RlOspfv3NbrState_Type.__name__=_F
_RlOspfv3NbrState_Object=MibTableColumn
rlOspfv3NbrState=_RlOspfv3NbrState_Object((1,3,6,1,4,1,4526,17,216,10,1,9),_RlOspfv3NbrState_Type())
rlOspfv3NbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrState.setStatus(_A)
_RlOspfv3NbrEvents_Type=Counter32
_RlOspfv3NbrEvents_Object=MibTableColumn
rlOspfv3NbrEvents=_RlOspfv3NbrEvents_Object((1,3,6,1,4,1,4526,17,216,10,1,10),_RlOspfv3NbrEvents_Type())
rlOspfv3NbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrEvents.setStatus(_A)
_RlOspfv3NbrLsRetransQLen_Type=Gauge32
_RlOspfv3NbrLsRetransQLen_Object=MibTableColumn
rlOspfv3NbrLsRetransQLen=_RlOspfv3NbrLsRetransQLen_Object((1,3,6,1,4,1,4526,17,216,10,1,11),_RlOspfv3NbrLsRetransQLen_Type())
rlOspfv3NbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrLsRetransQLen.setStatus(_A)
_RlOspfv3NbrHelloSuppressed_Type=TruthValue
_RlOspfv3NbrHelloSuppressed_Object=MibTableColumn
rlOspfv3NbrHelloSuppressed=_RlOspfv3NbrHelloSuppressed_Object((1,3,6,1,4,1,4526,17,216,10,1,12),_RlOspfv3NbrHelloSuppressed_Type())
rlOspfv3NbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrHelloSuppressed.setStatus(_A)
_RlOspfv3NbrIfId_Type=InterfaceIndex
_RlOspfv3NbrIfId_Object=MibTableColumn
rlOspfv3NbrIfId=_RlOspfv3NbrIfId_Object((1,3,6,1,4,1,4526,17,216,10,1,13),_RlOspfv3NbrIfId_Type())
rlOspfv3NbrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrIfId.setStatus(_A)
class _RlOspfv3NbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_RlOspfv3NbrRestartHelperStatus_Type.__name__=_F
_RlOspfv3NbrRestartHelperStatus_Object=MibTableColumn
rlOspfv3NbrRestartHelperStatus=_RlOspfv3NbrRestartHelperStatus_Object((1,3,6,1,4,1,4526,17,216,10,1,14),_RlOspfv3NbrRestartHelperStatus_Type())
rlOspfv3NbrRestartHelperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrRestartHelperStatus.setStatus(_A)
_RlOspfv3NbrRestartHelperAge_Type=Ospfv3UpToRefreshIntervalTC
_RlOspfv3NbrRestartHelperAge_Object=MibTableColumn
rlOspfv3NbrRestartHelperAge=_RlOspfv3NbrRestartHelperAge_Object((1,3,6,1,4,1,4526,17,216,10,1,15),_RlOspfv3NbrRestartHelperAge_Type())
rlOspfv3NbrRestartHelperAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3NbrRestartHelperAge.setUnits(_H)
class _RlOspfv3NbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_RlOspfv3NbrRestartHelperExitReason_Type.__name__=_F
_RlOspfv3NbrRestartHelperExitReason_Object=MibTableColumn
rlOspfv3NbrRestartHelperExitReason=_RlOspfv3NbrRestartHelperExitReason_Object((1,3,6,1,4,1,4526,17,216,10,1,16),_RlOspfv3NbrRestartHelperExitReason_Type())
rlOspfv3NbrRestartHelperExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrRestartHelperExitReason.setStatus(_A)
_RlOspfv3NbrDeadTime_Type=PositiveInteger
_RlOspfv3NbrDeadTime_Object=MibTableColumn
rlOspfv3NbrDeadTime=_RlOspfv3NbrDeadTime_Object((1,3,6,1,4,1,4526,17,216,10,1,17),_RlOspfv3NbrDeadTime_Type())
rlOspfv3NbrDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrDeadTime.setStatus(_A)
_RlOspfv3NbrAreaId_Type=AreaID
_RlOspfv3NbrAreaId_Object=MibTableColumn
rlOspfv3NbrAreaId=_RlOspfv3NbrAreaId_Object((1,3,6,1,4,1,4526,17,216,10,1,18),_RlOspfv3NbrAreaId_Type())
rlOspfv3NbrAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3NbrAreaId.setStatus(_A)
_RlOspfv3CfgNbrTable_Object=MibTable
rlOspfv3CfgNbrTable=_RlOspfv3CfgNbrTable_Object((1,3,6,1,4,1,4526,17,216,11))
if mibBuilder.loadTexts:rlOspfv3CfgNbrTable.setStatus(_A)
_RlOspfv3CfgNbrEntry_Object=MibTableRow
rlOspfv3CfgNbrEntry=_RlOspfv3CfgNbrEntry_Object((1,3,6,1,4,1,4526,17,216,11,1))
rlOspfv3CfgNbrEntry.setIndexNames((0,_C,_AN),(0,_C,_AO),(0,_C,_AP),(0,_C,_AQ),(0,_C,_AR))
if mibBuilder.loadTexts:rlOspfv3CfgNbrEntry.setStatus(_A)
_RlOspf3CfgNbrProcessId_Type=RlOspfProcessID
_RlOspf3CfgNbrProcessId_Object=MibTableColumn
rlOspf3CfgNbrProcessId=_RlOspf3CfgNbrProcessId_Object((1,3,6,1,4,1,4526,17,216,11,1,1),_RlOspf3CfgNbrProcessId_Type())
rlOspf3CfgNbrProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspf3CfgNbrProcessId.setStatus(_A)
_RlOspfv3CfgNbrIfIndex_Type=InterfaceIndex
_RlOspfv3CfgNbrIfIndex_Object=MibTableColumn
rlOspfv3CfgNbrIfIndex=_RlOspfv3CfgNbrIfIndex_Object((1,3,6,1,4,1,4526,17,216,11,1,2),_RlOspfv3CfgNbrIfIndex_Type())
rlOspfv3CfgNbrIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3CfgNbrIfIndex.setStatus(_A)
_RlOspfv3CfgNbrIfInstId_Type=Ospfv3IfInstIdTC
_RlOspfv3CfgNbrIfInstId_Object=MibTableColumn
rlOspfv3CfgNbrIfInstId=_RlOspfv3CfgNbrIfInstId_Object((1,3,6,1,4,1,4526,17,216,11,1,3),_RlOspfv3CfgNbrIfInstId_Type())
rlOspfv3CfgNbrIfInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3CfgNbrIfInstId.setStatus(_A)
_RlOspfv3CfgNbrAddressType_Type=InetAddressType
_RlOspfv3CfgNbrAddressType_Object=MibTableColumn
rlOspfv3CfgNbrAddressType=_RlOspfv3CfgNbrAddressType_Object((1,3,6,1,4,1,4526,17,216,11,1,4),_RlOspfv3CfgNbrAddressType_Type())
rlOspfv3CfgNbrAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3CfgNbrAddressType.setStatus(_A)
_RlOspfv3CfgNbrAddress_Type=InetAddress
_RlOspfv3CfgNbrAddress_Object=MibTableColumn
rlOspfv3CfgNbrAddress=_RlOspfv3CfgNbrAddress_Object((1,3,6,1,4,1,4526,17,216,11,1,5),_RlOspfv3CfgNbrAddress_Type())
rlOspfv3CfgNbrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3CfgNbrAddress.setStatus(_A)
class _RlOspfv3CfgNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RlOspfv3CfgNbrPriority_Type.__name__=_c
_RlOspfv3CfgNbrPriority_Object=MibTableColumn
rlOspfv3CfgNbrPriority=_RlOspfv3CfgNbrPriority_Object((1,3,6,1,4,1,4526,17,216,11,1,6),_RlOspfv3CfgNbrPriority_Type())
rlOspfv3CfgNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3CfgNbrPriority.setStatus(_A)
_RlOspfv3CfgNbrRowStatus_Type=RowStatus
_RlOspfv3CfgNbrRowStatus_Object=MibTableColumn
rlOspfv3CfgNbrRowStatus=_RlOspfv3CfgNbrRowStatus_Object((1,3,6,1,4,1,4526,17,216,11,1,7),_RlOspfv3CfgNbrRowStatus_Type())
rlOspfv3CfgNbrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3CfgNbrRowStatus.setStatus(_A)
_RlOspfv3VirtNbrTable_Object=MibTable
rlOspfv3VirtNbrTable=_RlOspfv3VirtNbrTable_Object((1,3,6,1,4,1,4526,17,216,12))
if mibBuilder.loadTexts:rlOspfv3VirtNbrTable.setStatus(_A)
_RlOspfv3VirtNbrEntry_Object=MibTableRow
rlOspfv3VirtNbrEntry=_RlOspfv3VirtNbrEntry_Object((1,3,6,1,4,1,4526,17,216,12,1))
rlOspfv3VirtNbrEntry.setIndexNames((0,_C,_AS),(0,_C,_AT),(0,_C,_AU))
if mibBuilder.loadTexts:rlOspfv3VirtNbrEntry.setStatus(_A)
_RlOspfv3VirtNbrProcessId_Type=RlOspfProcessID
_RlOspfv3VirtNbrProcessId_Object=MibTableColumn
rlOspfv3VirtNbrProcessId=_RlOspfv3VirtNbrProcessId_Object((1,3,6,1,4,1,4526,17,216,12,1,1),_RlOspfv3VirtNbrProcessId_Type())
rlOspfv3VirtNbrProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrProcessId.setStatus(_A)
_RlOspfv3VirtNbrArea_Type=AreaID
_RlOspfv3VirtNbrArea_Object=MibTableColumn
rlOspfv3VirtNbrArea=_RlOspfv3VirtNbrArea_Object((1,3,6,1,4,1,4526,17,216,12,1,2),_RlOspfv3VirtNbrArea_Type())
rlOspfv3VirtNbrArea.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtNbrArea.setStatus(_A)
_RlOspfv3VirtNbrRtrId_Type=RouterID
_RlOspfv3VirtNbrRtrId_Object=MibTableColumn
rlOspfv3VirtNbrRtrId=_RlOspfv3VirtNbrRtrId_Object((1,3,6,1,4,1,4526,17,216,12,1,3),_RlOspfv3VirtNbrRtrId_Type())
rlOspfv3VirtNbrRtrId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtNbrRtrId.setStatus(_A)
_RlOspfv3VirtNbrIfIndex_Type=InterfaceIndex
_RlOspfv3VirtNbrIfIndex_Object=MibTableColumn
rlOspfv3VirtNbrIfIndex=_RlOspfv3VirtNbrIfIndex_Object((1,3,6,1,4,1,4526,17,216,12,1,4),_RlOspfv3VirtNbrIfIndex_Type())
rlOspfv3VirtNbrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrIfIndex.setStatus(_A)
_RlOspfv3VirtNbrIfInstId_Type=Ospfv3IfInstIdTC
_RlOspfv3VirtNbrIfInstId_Object=MibTableColumn
rlOspfv3VirtNbrIfInstId=_RlOspfv3VirtNbrIfInstId_Object((1,3,6,1,4,1,4526,17,216,12,1,5),_RlOspfv3VirtNbrIfInstId_Type())
rlOspfv3VirtNbrIfInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrIfInstId.setStatus(_A)
_RlOspfv3VirtNbrAddressType_Type=InetAddressType
_RlOspfv3VirtNbrAddressType_Object=MibTableColumn
rlOspfv3VirtNbrAddressType=_RlOspfv3VirtNbrAddressType_Object((1,3,6,1,4,1,4526,17,216,12,1,6),_RlOspfv3VirtNbrAddressType_Type())
rlOspfv3VirtNbrAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrAddressType.setStatus(_A)
_RlOspfv3VirtNbrAddress_Type=InetAddress
_RlOspfv3VirtNbrAddress_Object=MibTableColumn
rlOspfv3VirtNbrAddress=_RlOspfv3VirtNbrAddress_Object((1,3,6,1,4,1,4526,17,216,12,1,7),_RlOspfv3VirtNbrAddress_Type())
rlOspfv3VirtNbrAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrAddress.setStatus(_A)
_RlOspfv3VirtNbrOptions_Type=Integer32
_RlOspfv3VirtNbrOptions_Object=MibTableColumn
rlOspfv3VirtNbrOptions=_RlOspfv3VirtNbrOptions_Object((1,3,6,1,4,1,4526,17,216,12,1,8),_RlOspfv3VirtNbrOptions_Type())
rlOspfv3VirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrOptions.setStatus(_A)
class _RlOspfv3VirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),('attempt',2),('init',3),('twoWay',4),(_AM,5),('exchange',6),('loading',7),('full',8)))
_RlOspfv3VirtNbrState_Type.__name__=_F
_RlOspfv3VirtNbrState_Object=MibTableColumn
rlOspfv3VirtNbrState=_RlOspfv3VirtNbrState_Object((1,3,6,1,4,1,4526,17,216,12,1,9),_RlOspfv3VirtNbrState_Type())
rlOspfv3VirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrState.setStatus(_A)
_RlOspfv3VirtNbrEvents_Type=Counter32
_RlOspfv3VirtNbrEvents_Object=MibTableColumn
rlOspfv3VirtNbrEvents=_RlOspfv3VirtNbrEvents_Object((1,3,6,1,4,1,4526,17,216,12,1,10),_RlOspfv3VirtNbrEvents_Type())
rlOspfv3VirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrEvents.setStatus(_A)
_RlOspfv3VirtNbrLsRetransQLen_Type=Gauge32
_RlOspfv3VirtNbrLsRetransQLen_Object=MibTableColumn
rlOspfv3VirtNbrLsRetransQLen=_RlOspfv3VirtNbrLsRetransQLen_Object((1,3,6,1,4,1,4526,17,216,12,1,11),_RlOspfv3VirtNbrLsRetransQLen_Type())
rlOspfv3VirtNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrLsRetransQLen.setStatus(_A)
_RlOspfv3VirtNbrHelloSuppressed_Type=TruthValue
_RlOspfv3VirtNbrHelloSuppressed_Object=MibTableColumn
rlOspfv3VirtNbrHelloSuppressed=_RlOspfv3VirtNbrHelloSuppressed_Object((1,3,6,1,4,1,4526,17,216,12,1,12),_RlOspfv3VirtNbrHelloSuppressed_Type())
rlOspfv3VirtNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrHelloSuppressed.setStatus(_A)
_RlOspfv3VirtNbrIfId_Type=InterfaceIndex
_RlOspfv3VirtNbrIfId_Object=MibTableColumn
rlOspfv3VirtNbrIfId=_RlOspfv3VirtNbrIfId_Object((1,3,6,1,4,1,4526,17,216,12,1,13),_RlOspfv3VirtNbrIfId_Type())
rlOspfv3VirtNbrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrIfId.setStatus(_A)
class _RlOspfv3VirtNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_RlOspfv3VirtNbrRestartHelperStatus_Type.__name__=_F
_RlOspfv3VirtNbrRestartHelperStatus_Object=MibTableColumn
rlOspfv3VirtNbrRestartHelperStatus=_RlOspfv3VirtNbrRestartHelperStatus_Object((1,3,6,1,4,1,4526,17,216,12,1,14),_RlOspfv3VirtNbrRestartHelperStatus_Type())
rlOspfv3VirtNbrRestartHelperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrRestartHelperStatus.setStatus(_A)
_RlOspfv3VirtNbrRestartHelperAge_Type=Ospfv3UpToRefreshIntervalTC
_RlOspfv3VirtNbrRestartHelperAge_Object=MibTableColumn
rlOspfv3VirtNbrRestartHelperAge=_RlOspfv3VirtNbrRestartHelperAge_Object((1,3,6,1,4,1,4526,17,216,12,1,15),_RlOspfv3VirtNbrRestartHelperAge_Type())
rlOspfv3VirtNbrRestartHelperAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3VirtNbrRestartHelperAge.setUnits(_H)
class _RlOspfv3VirtNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_RlOspfv3VirtNbrRestartHelperExitReason_Type.__name__=_F
_RlOspfv3VirtNbrRestartHelperExitReason_Object=MibTableColumn
rlOspfv3VirtNbrRestartHelperExitReason=_RlOspfv3VirtNbrRestartHelperExitReason_Object((1,3,6,1,4,1,4526,17,216,12,1,16),_RlOspfv3VirtNbrRestartHelperExitReason_Type())
rlOspfv3VirtNbrRestartHelperExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrRestartHelperExitReason.setStatus(_A)
_RlOspfv3VirtNbrDeadTime_Type=PositiveInteger
_RlOspfv3VirtNbrDeadTime_Object=MibTableColumn
rlOspfv3VirtNbrDeadTime=_RlOspfv3VirtNbrDeadTime_Object((1,3,6,1,4,1,4526,17,216,12,1,17),_RlOspfv3VirtNbrDeadTime_Type())
rlOspfv3VirtNbrDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtNbrDeadTime.setStatus(_A)
_RlOspfv3AreaAggregateTable_Object=MibTable
rlOspfv3AreaAggregateTable=_RlOspfv3AreaAggregateTable_Object((1,3,6,1,4,1,4526,17,216,13))
if mibBuilder.loadTexts:rlOspfv3AreaAggregateTable.setStatus(_A)
_RlOspfv3AreaAggregateEntry_Object=MibTableRow
rlOspfv3AreaAggregateEntry=_RlOspfv3AreaAggregateEntry_Object((1,3,6,1,4,1,4526,17,216,13,1))
rlOspfv3AreaAggregateEntry.setIndexNames((0,_C,_AV),(0,_C,_AW),(0,_C,_AX),(0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa))
if mibBuilder.loadTexts:rlOspfv3AreaAggregateEntry.setStatus(_A)
_RlOspfv3AreaAggregateProcessId_Type=RlOspfProcessID
_RlOspfv3AreaAggregateProcessId_Object=MibTableColumn
rlOspfv3AreaAggregateProcessId=_RlOspfv3AreaAggregateProcessId_Object((1,3,6,1,4,1,4526,17,216,13,1,1),_RlOspfv3AreaAggregateProcessId_Type())
rlOspfv3AreaAggregateProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3AreaAggregateProcessId.setStatus(_A)
_RlOspfv3AreaAggregateAreaID_Type=AreaID
_RlOspfv3AreaAggregateAreaID_Object=MibTableColumn
rlOspfv3AreaAggregateAreaID=_RlOspfv3AreaAggregateAreaID_Object((1,3,6,1,4,1,4526,17,216,13,1,2),_RlOspfv3AreaAggregateAreaID_Type())
rlOspfv3AreaAggregateAreaID.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaAggregateAreaID.setStatus(_A)
class _RlOspfv3AreaAggregateAreaLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8195,8199)));namedValues=NamedValues(*(('interAreaPrefixLsa',8195),('nssaExternalLsa',8199)))
_RlOspfv3AreaAggregateAreaLsdbType_Type.__name__=_F
_RlOspfv3AreaAggregateAreaLsdbType_Object=MibTableColumn
rlOspfv3AreaAggregateAreaLsdbType=_RlOspfv3AreaAggregateAreaLsdbType_Object((1,3,6,1,4,1,4526,17,216,13,1,3),_RlOspfv3AreaAggregateAreaLsdbType_Type())
rlOspfv3AreaAggregateAreaLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaAggregateAreaLsdbType.setStatus(_A)
_RlOspfv3AreaAggregatePrefixType_Type=InetAddressType
_RlOspfv3AreaAggregatePrefixType_Object=MibTableColumn
rlOspfv3AreaAggregatePrefixType=_RlOspfv3AreaAggregatePrefixType_Object((1,3,6,1,4,1,4526,17,216,13,1,4),_RlOspfv3AreaAggregatePrefixType_Type())
rlOspfv3AreaAggregatePrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaAggregatePrefixType.setStatus(_A)
class _RlOspfv3AreaAggregatePrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlOspfv3AreaAggregatePrefix_Type.__name__=_n
_RlOspfv3AreaAggregatePrefix_Object=MibTableColumn
rlOspfv3AreaAggregatePrefix=_RlOspfv3AreaAggregatePrefix_Object((1,3,6,1,4,1,4526,17,216,13,1,5),_RlOspfv3AreaAggregatePrefix_Type())
rlOspfv3AreaAggregatePrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaAggregatePrefix.setStatus(_A)
class _RlOspfv3AreaAggregatePrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,128))
_RlOspfv3AreaAggregatePrefixLength_Type.__name__=_o
_RlOspfv3AreaAggregatePrefixLength_Object=MibTableColumn
rlOspfv3AreaAggregatePrefixLength=_RlOspfv3AreaAggregatePrefixLength_Object((1,3,6,1,4,1,4526,17,216,13,1,6),_RlOspfv3AreaAggregatePrefixLength_Type())
rlOspfv3AreaAggregatePrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3AreaAggregatePrefixLength.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3AreaAggregatePrefixLength.setUnits('bits')
_RlOspfv3AreaAggregateRowStatus_Type=RowStatus
_RlOspfv3AreaAggregateRowStatus_Object=MibTableColumn
rlOspfv3AreaAggregateRowStatus=_RlOspfv3AreaAggregateRowStatus_Object((1,3,6,1,4,1,4526,17,216,13,1,7),_RlOspfv3AreaAggregateRowStatus_Type())
rlOspfv3AreaAggregateRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaAggregateRowStatus.setStatus(_A)
class _RlOspfv3AreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('advertiseMatching',1),('doNotAdvertiseMatching',2)))
_RlOspfv3AreaAggregateEffect_Type.__name__=_F
_RlOspfv3AreaAggregateEffect_Object=MibTableColumn
rlOspfv3AreaAggregateEffect=_RlOspfv3AreaAggregateEffect_Object((1,3,6,1,4,1,4526,17,216,13,1,8),_RlOspfv3AreaAggregateEffect_Type())
rlOspfv3AreaAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaAggregateEffect.setStatus(_A)
class _RlOspfv3AreaAggregateRouteTag_Type(Unsigned32):defaultValue=0
_RlOspfv3AreaAggregateRouteTag_Type.__name__=_J
_RlOspfv3AreaAggregateRouteTag_Object=MibTableColumn
rlOspfv3AreaAggregateRouteTag=_RlOspfv3AreaAggregateRouteTag_Object((1,3,6,1,4,1,4526,17,216,13,1,9),_RlOspfv3AreaAggregateRouteTag_Type())
rlOspfv3AreaAggregateRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfv3AreaAggregateRouteTag.setStatus(_A)
_RlOspfv3VirtLinkLsdbTable_Object=MibTable
rlOspfv3VirtLinkLsdbTable=_RlOspfv3VirtLinkLsdbTable_Object((1,3,6,1,4,1,4526,17,216,14))
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbTable.setStatus(_A)
_RlOspfv3VirtLinkLsdbEntry_Object=MibTableRow
rlOspfv3VirtLinkLsdbEntry=_RlOspfv3VirtLinkLsdbEntry_Object((1,3,6,1,4,1,4526,17,216,14,1))
rlOspfv3VirtLinkLsdbEntry.setIndexNames((0,_C,_Ab),(0,_C,_Ac),(0,_C,_Ad),(0,_C,_Ae),(0,_C,_Af),(0,_C,_Ag))
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbEntry.setStatus(_A)
_RlOspfv3VirtLinkLsdbProcessId_Type=RlOspfProcessID
_RlOspfv3VirtLinkLsdbProcessId_Object=MibTableColumn
rlOspfv3VirtLinkLsdbProcessId=_RlOspfv3VirtLinkLsdbProcessId_Object((1,3,6,1,4,1,4526,17,216,14,1,1),_RlOspfv3VirtLinkLsdbProcessId_Type())
rlOspfv3VirtLinkLsdbProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbProcessId.setStatus(_A)
_RlOspfv3VirtLinkLsdbIfAreaId_Type=AreaID
_RlOspfv3VirtLinkLsdbIfAreaId_Object=MibTableColumn
rlOspfv3VirtLinkLsdbIfAreaId=_RlOspfv3VirtLinkLsdbIfAreaId_Object((1,3,6,1,4,1,4526,17,216,14,1,2),_RlOspfv3VirtLinkLsdbIfAreaId_Type())
rlOspfv3VirtLinkLsdbIfAreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbIfAreaId.setStatus(_A)
_RlOspfv3VirtLinkLsdbIfNeighbor_Type=RouterID
_RlOspfv3VirtLinkLsdbIfNeighbor_Object=MibTableColumn
rlOspfv3VirtLinkLsdbIfNeighbor=_RlOspfv3VirtLinkLsdbIfNeighbor_Object((1,3,6,1,4,1,4526,17,216,14,1,3),_RlOspfv3VirtLinkLsdbIfNeighbor_Type())
rlOspfv3VirtLinkLsdbIfNeighbor.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbIfNeighbor.setStatus(_A)
class _RlOspfv3VirtLinkLsdbType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RlOspfv3VirtLinkLsdbType_Type.__name__=_J
_RlOspfv3VirtLinkLsdbType_Object=MibTableColumn
rlOspfv3VirtLinkLsdbType=_RlOspfv3VirtLinkLsdbType_Object((1,3,6,1,4,1,4526,17,216,14,1,4),_RlOspfv3VirtLinkLsdbType_Type())
rlOspfv3VirtLinkLsdbType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbType.setStatus(_A)
_RlOspfv3VirtLinkLsdbRouterId_Type=RouterID
_RlOspfv3VirtLinkLsdbRouterId_Object=MibTableColumn
rlOspfv3VirtLinkLsdbRouterId=_RlOspfv3VirtLinkLsdbRouterId_Object((1,3,6,1,4,1,4526,17,216,14,1,5),_RlOspfv3VirtLinkLsdbRouterId_Type())
rlOspfv3VirtLinkLsdbRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbRouterId.setStatus(_A)
_RlOspfv3VirtLinkLsdbLsid_Type=RlLsID
_RlOspfv3VirtLinkLsdbLsid_Object=MibTableColumn
rlOspfv3VirtLinkLsdbLsid=_RlOspfv3VirtLinkLsdbLsid_Object((1,3,6,1,4,1,4526,17,216,14,1,6),_RlOspfv3VirtLinkLsdbLsid_Type())
rlOspfv3VirtLinkLsdbLsid.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbLsid.setStatus(_A)
_RlOspfv3VirtLinkLsdbSequence_Type=Ospfv3LsaSequenceTC
_RlOspfv3VirtLinkLsdbSequence_Object=MibTableColumn
rlOspfv3VirtLinkLsdbSequence=_RlOspfv3VirtLinkLsdbSequence_Object((1,3,6,1,4,1,4526,17,216,14,1,7),_RlOspfv3VirtLinkLsdbSequence_Type())
rlOspfv3VirtLinkLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbSequence.setStatus(_A)
_RlOspfv3VirtLinkLsdbAge_Type=Ospfv3LsaAgeTC
_RlOspfv3VirtLinkLsdbAge_Object=MibTableColumn
rlOspfv3VirtLinkLsdbAge=_RlOspfv3VirtLinkLsdbAge_Object((1,3,6,1,4,1,4526,17,216,14,1,8),_RlOspfv3VirtLinkLsdbAge_Type())
rlOspfv3VirtLinkLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbAge.setUnits(_H)
_RlOspfv3VirtLinkLsdbChecksum_Type=Integer32
_RlOspfv3VirtLinkLsdbChecksum_Object=MibTableColumn
rlOspfv3VirtLinkLsdbChecksum=_RlOspfv3VirtLinkLsdbChecksum_Object((1,3,6,1,4,1,4526,17,216,14,1,9),_RlOspfv3VirtLinkLsdbChecksum_Type())
rlOspfv3VirtLinkLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbChecksum.setStatus(_A)
class _RlOspfv3VirtLinkLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfv3VirtLinkLsdbAdvertisement_Type.__name__=_M
_RlOspfv3VirtLinkLsdbAdvertisement_Object=MibTableColumn
rlOspfv3VirtLinkLsdbAdvertisement=_RlOspfv3VirtLinkLsdbAdvertisement_Object((1,3,6,1,4,1,4526,17,216,14,1,10),_RlOspfv3VirtLinkLsdbAdvertisement_Type())
rlOspfv3VirtLinkLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbAdvertisement.setStatus(_A)
_RlOspfv3VirtLinkLsdbTypeKnown_Type=TruthValue
_RlOspfv3VirtLinkLsdbTypeKnown_Object=MibTableColumn
rlOspfv3VirtLinkLsdbTypeKnown=_RlOspfv3VirtLinkLsdbTypeKnown_Object((1,3,6,1,4,1,4526,17,216,14,1,11),_RlOspfv3VirtLinkLsdbTypeKnown_Type())
rlOspfv3VirtLinkLsdbTypeKnown.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfv3VirtLinkLsdbTypeKnown.setStatus(_A)
_RlOspfv3NotificationEntry_ObjectIdentity=ObjectIdentity
rlOspfv3NotificationEntry=_RlOspfv3NotificationEntry_ObjectIdentity((1,3,6,1,4,1,4526,17,216,15))
class _RlOspfv3ConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('helloIntervalMismatch',5),('deadIntervalMismatch',6),('optionMismatch',7),('mtuMismatch',8),('duplicateRouterId',9),('noError',10)))
_RlOspfv3ConfigErrorType_Type.__name__=_F
_RlOspfv3ConfigErrorType_Object=MibScalar
rlOspfv3ConfigErrorType=_RlOspfv3ConfigErrorType_Object((1,3,6,1,4,1,4526,17,216,15,1),_RlOspfv3ConfigErrorType_Type())
rlOspfv3ConfigErrorType.setMaxAccess(_j)
if mibBuilder.loadTexts:rlOspfv3ConfigErrorType.setStatus(_A)
class _RlOspfv3PacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hello',1),('dbDescript',2),('lsReq',3),('lsUpdate',4),('lsAck',5),('nullPacket',6)))
_RlOspfv3PacketType_Type.__name__=_F
_RlOspfv3PacketType_Object=MibScalar
rlOspfv3PacketType=_RlOspfv3PacketType_Object((1,3,6,1,4,1,4526,17,216,15,2),_RlOspfv3PacketType_Type())
rlOspfv3PacketType.setMaxAccess(_j)
if mibBuilder.loadTexts:rlOspfv3PacketType.setStatus(_A)
_RlOspfv3PacketSrc_Type=InetAddressIPv6
_RlOspfv3PacketSrc_Object=MibScalar
rlOspfv3PacketSrc=_RlOspfv3PacketSrc_Object((1,3,6,1,4,1,4526,17,216,15,3),_RlOspfv3PacketSrc_Type())
rlOspfv3PacketSrc.setMaxAccess(_j)
if mibBuilder.loadTexts:rlOspfv3PacketSrc.setStatus(_A)
_RlOspfv3Notifications_ObjectIdentity=ObjectIdentity
rlOspfv3Notifications=_RlOspfv3Notifications_ObjectIdentity((1,3,6,1,4,1,4526,17,216,16))
_RlOspfv3EnableNotificationsOspfEvents_Type=Integer32
_RlOspfv3EnableNotificationsOspfEvents_Object=MibScalar
rlOspfv3EnableNotificationsOspfEvents=_RlOspfv3EnableNotificationsOspfEvents_Object((1,3,6,1,4,1,4526,17,216,17),_RlOspfv3EnableNotificationsOspfEvents_Type())
rlOspfv3EnableNotificationsOspfEvents.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3EnableNotificationsOspfEvents.setStatus(_A)
class _RlOspfv3EnableNotificationsOspfRateLimitSeconds_Type(Integer32):defaultValue=10
_RlOspfv3EnableNotificationsOspfRateLimitSeconds_Type.__name__=_F
_RlOspfv3EnableNotificationsOspfRateLimitSeconds_Object=MibScalar
rlOspfv3EnableNotificationsOspfRateLimitSeconds=_RlOspfv3EnableNotificationsOspfRateLimitSeconds_Object((1,3,6,1,4,1,4526,17,216,18),_RlOspfv3EnableNotificationsOspfRateLimitSeconds_Type())
rlOspfv3EnableNotificationsOspfRateLimitSeconds.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3EnableNotificationsOspfRateLimitSeconds.setStatus(_A)
class _RlOspfv3EnableNotificationsOspfRateLimitTrapNumber_Type(Integer32):defaultValue=7
_RlOspfv3EnableNotificationsOspfRateLimitTrapNumber_Type.__name__=_F
_RlOspfv3EnableNotificationsOspfRateLimitTrapNumber_Object=MibScalar
rlOspfv3EnableNotificationsOspfRateLimitTrapNumber=_RlOspfv3EnableNotificationsOspfRateLimitTrapNumber_Object((1,3,6,1,4,1,4526,17,216,19),_RlOspfv3EnableNotificationsOspfRateLimitTrapNumber_Type())
rlOspfv3EnableNotificationsOspfRateLimitTrapNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:rlOspfv3EnableNotificationsOspfRateLimitTrapNumber.setStatus(_A)
rlOspfv3VirtIfStateChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,1))
rlOspfv3VirtIfStateChange.setObjects(*((_C,_I),(_C,_a)))
if mibBuilder.loadTexts:rlOspfv3VirtIfStateChange.setStatus(_A)
rlOspfv3NbrStateChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,2))
rlOspfv3NbrStateChange.setObjects(*((_C,_I),(_C,_Ah)))
if mibBuilder.loadTexts:rlOspfv3NbrStateChange.setStatus(_A)
rlOspfv3VirtNbrStateChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,3))
rlOspfv3VirtNbrStateChange.setObjects(*((_C,_I),(_C,_Ai)))
if mibBuilder.loadTexts:rlOspfv3VirtNbrStateChange.setStatus(_A)
rlOspfv3IfConfigError=NotificationType((1,3,6,1,4,1,4526,17,216,16,4))
rlOspfv3IfConfigError.setObjects(*((_C,_I),(_C,_b),(_C,_k),(_C,_l),(_C,_P)))
if mibBuilder.loadTexts:rlOspfv3IfConfigError.setStatus(_A)
rlOspfv3VirtIfConfigError=NotificationType((1,3,6,1,4,1,4526,17,216,16,5))
rlOspfv3VirtIfConfigError.setObjects(*((_C,_I),(_C,_a),(_C,_l),(_C,_P)))
if mibBuilder.loadTexts:rlOspfv3VirtIfConfigError.setStatus(_A)
rlOspfv3IfRxBadPacket=NotificationType((1,3,6,1,4,1,4526,17,216,16,6))
rlOspfv3IfRxBadPacket.setObjects(*((_C,_I),(_C,_b),(_C,_k),(_C,_P)))
if mibBuilder.loadTexts:rlOspfv3IfRxBadPacket.setStatus(_A)
rlOspfv3VirtIfRxBadPacket=NotificationType((1,3,6,1,4,1,4526,17,216,16,7))
rlOspfv3VirtIfRxBadPacket.setObjects(*((_C,_I),(_C,_a),(_C,_P)))
if mibBuilder.loadTexts:rlOspfv3VirtIfRxBadPacket.setStatus(_A)
rlOspfv3LsdbOverflow=NotificationType((1,3,6,1,4,1,4526,17,216,16,8))
rlOspfv3LsdbOverflow.setObjects(*((_C,_I),(_C,_m)))
if mibBuilder.loadTexts:rlOspfv3LsdbOverflow.setStatus(_A)
rlOspfv3LsdbApproachingOverflow=NotificationType((1,3,6,1,4,1,4526,17,216,16,9))
rlOspfv3LsdbApproachingOverflow.setObjects(*((_C,_I),(_C,_m)))
if mibBuilder.loadTexts:rlOspfv3LsdbApproachingOverflow.setStatus(_A)
rlOspfv3IfStateChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,10))
rlOspfv3IfStateChange.setObjects(*((_C,_I),(_C,_b)))
if mibBuilder.loadTexts:rlOspfv3IfStateChange.setStatus(_A)
rlOspfv3NssaTranslatorStatusChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,11))
rlOspfv3NssaTranslatorStatusChange.setObjects(*((_C,_I),(_C,_Aj)))
if mibBuilder.loadTexts:rlOspfv3NssaTranslatorStatusChange.setStatus(_A)
rlOspfv3RestartStatusChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,12))
rlOspfv3RestartStatusChange.setObjects(*((_C,_I),(_C,_Ak),(_C,_Al),(_C,_Am)))
if mibBuilder.loadTexts:rlOspfv3RestartStatusChange.setStatus(_A)
rlOspfv3NbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,13))
rlOspfv3NbrRestartHelperStatusChange.setObjects(*((_C,_I),(_C,_An),(_C,_Ao),(_C,_Ap)))
if mibBuilder.loadTexts:rlOspfv3NbrRestartHelperStatusChange.setStatus(_A)
rlOspfv3VirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,4,1,4526,17,216,16,14))
rlOspfv3VirtNbrRestartHelperStatusChange.setObjects(*((_C,_I),(_C,_Aq),(_C,_Ar),(_C,_As)))
if mibBuilder.loadTexts:rlOspfv3VirtNbrRestartHelperStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlRouterID':RlRouterID,'RlLsID':RlLsID,_AE:RlOspfv3FastHelloMultiplierRange,'RlOspfv3UpToRefreshInterval':RlOspfv3UpToRefreshInterval,'RlOspfv3RestartHelperStatus':RlOspfv3RestartHelperStatus,'RlOspfv3RestartExitReason':RlOspfv3RestartExitReason,_O:RlOspfv3UpToRefreshIntervalTC,'rlOspfv3':rlOspfv3,'rlOspfv3Instance':rlOspfv3Instance,'rlOspfv3GeneralGroupTable':rlOspfv3GeneralGroupTable,'rlOspfv3GeneralGroupEntry':rlOspfv3GeneralGroupEntry,_q:rlOspfv3ProcessId,_I:rlOspfv3RouterId,'rlOspfv3AdminStatus':rlOspfv3AdminStatus,'rlOspfv3VersionNumber':rlOspfv3VersionNumber,'rlOspfv3AreaBdrRtrStatus':rlOspfv3AreaBdrRtrStatus,'rlOspfv3ASBdrRtrStatus':rlOspfv3ASBdrRtrStatus,'rlOspfv3AsScopeLsaCount':rlOspfv3AsScopeLsaCount,'rlOspfv3AsScopeLsaCksumSum':rlOspfv3AsScopeLsaCksumSum,'rlOspfv3OriginateNewLsas':rlOspfv3OriginateNewLsas,'rlOspfv3RxNewLsas':rlOspfv3RxNewLsas,'rlOspfv3ExtLsaCount':rlOspfv3ExtLsaCount,_m:rlOspfv3ExtAreaLsdbLimit,'rlOspfv3ExitOverflowInterval':rlOspfv3ExitOverflowInterval,'rlOspfv3DemandExtensions':rlOspfv3DemandExtensions,'rlOspfv3ReferenceBandwidth':rlOspfv3ReferenceBandwidth,'rlOspfv3RestartSupport':rlOspfv3RestartSupport,_Al:rlOspfv3RestartInterval,'rlOspfv3RestartStrictLsaChecking':rlOspfv3RestartStrictLsaChecking,_Ak:rlOspfv3RestartStatus,'rlOspfv3RestartAge':rlOspfv3RestartAge,_Am:rlOspfv3RestartExitReason,'rlOspfv3NotificationEnable':rlOspfv3NotificationEnable,'rlOspfv3StubRouterSupport':rlOspfv3StubRouterSupport,'rlOspfv3StubRouterAdvertisement':rlOspfv3StubRouterAdvertisement,'rlOspfv3DiscontinuityTime':rlOspfv3DiscontinuityTime,'rlOspfv3RestartTime':rlOspfv3RestartTime,'rlOspfv3OperStatus':rlOspfv3OperStatus,'rlOspfv3RowStatus':rlOspfv3RowStatus,'rlOspfv3LogAdjacencyChanges':rlOspfv3LogAdjacencyChanges,'rlOspfv3PassiveInterface':rlOspfv3PassiveInterface,'rlOspfv3DefaultMetric':rlOspfv3DefaultMetric,'rlOspfv3MaximumRedistPrefixNum':rlOspfv3MaximumRedistPrefixNum,'rlOspfv3MaximumRedistPrefixThreshold':rlOspfv3MaximumRedistPrefixThreshold,'rlOspfv3MaximumRedistPrefixWarningOnly':rlOspfv3MaximumRedistPrefixWarningOnly,'rlOspfv3NextRouterId':rlOspfv3NextRouterId,'rlOspfv3RouterIdType':rlOspfv3RouterIdType,'rlOspfv3NextRouterIdType':rlOspfv3NextRouterIdType,'rlOspfv3ASBdrRtrActualStatus':rlOspfv3ASBdrRtrActualStatus,'rlOspfv3CalcMaxDelay':rlOspfv3CalcMaxDelay,'rlOspfv3RteMaxEqCostPaths':rlOspfv3RteMaxEqCostPaths,'rlOspfv3AreaTable':rlOspfv3AreaTable,'rlOspfv3AreaEntry':rlOspfv3AreaEntry,_r:rlOspfv3AreaProcessId,_s:rlOspfv3AreaId,'rlOspfv3AreaImportAsExtern':rlOspfv3AreaImportAsExtern,'rlOspfv3AreaSpfRuns':rlOspfv3AreaSpfRuns,'rlOspfv3AreaBdrRtrCount':rlOspfv3AreaBdrRtrCount,'rlOspfv3AreaAsBdrRtrCount':rlOspfv3AreaAsBdrRtrCount,'rlOspfv3AreaScopeLsaCount':rlOspfv3AreaScopeLsaCount,'rlOspfv3AreaScopeLsaCksumSum':rlOspfv3AreaScopeLsaCksumSum,'rlOspfv3AreaSummary':rlOspfv3AreaSummary,'rlOspfv3AreaRowStatus':rlOspfv3AreaRowStatus,'rlOspfv3AreaStubMetric':rlOspfv3AreaStubMetric,'rlOspfv3AreaNssaTranslatorRole':rlOspfv3AreaNssaTranslatorRole,_Aj:rlOspfv3AreaNssaTranslatorState,'rlOspfv3AreaNssaTranslatorStabInterval':rlOspfv3AreaNssaTranslatorStabInterval,'rlOspfv3AreaNssaTranslatorEvents':rlOspfv3AreaNssaTranslatorEvents,'rlOspfv3AreaStubMetricType':rlOspfv3AreaStubMetricType,'rlOspfv3AreaTEEnabled':rlOspfv3AreaTEEnabled,'rlOspfv3AreaAdminStat':rlOspfv3AreaAdminStat,'rlOspfv3AreaOperStatus':rlOspfv3AreaOperStatus,'rlOspfv3AreaFilterPrefixListIn':rlOspfv3AreaFilterPrefixListIn,'rlOspfv3AreaFilterPrefixListOut':rlOspfv3AreaFilterPrefixListOut,'rlOspfv3AsLsdbTable':rlOspfv3AsLsdbTable,'rlOspfv3AsLsdbEntry':rlOspfv3AsLsdbEntry,_t:rlOspfv3AsLsdbProcessId,_u:rlOspfv3AsLsdbType,_v:rlOspfv3AsLsdbRouterId,_w:rlOspfv3AsLsdbLsid,'rlOspfv3AsLsdbSequence':rlOspfv3AsLsdbSequence,'rlOspfv3AsLsdbAge':rlOspfv3AsLsdbAge,'rlOspfv3AsLsdbChecksum':rlOspfv3AsLsdbChecksum,'rlOspfv3AsLsdbAdvertisement':rlOspfv3AsLsdbAdvertisement,'rlOspfv3AsLsdbTypeKnown':rlOspfv3AsLsdbTypeKnown,'rlOspfv3AreaLsdbTable':rlOspfv3AreaLsdbTable,'rlOspfv3AreaLsdbEntry':rlOspfv3AreaLsdbEntry,_x:rlOspfv3AreaLsdbProcessId,_y:rlOspfv3AreaLsdbAreaId,_z:rlOspfv3AreaLsdbType,_A0:rlOspfv3AreaLsdbRouterId,_A1:rlOspfv3AreaLsdbLsid,'rlOspfv3AreaLsdbSequence':rlOspfv3AreaLsdbSequence,'rlOspfv3AreaLsdbAge':rlOspfv3AreaLsdbAge,'rlOspfv3AreaLsdbChecksum':rlOspfv3AreaLsdbChecksum,'rlOspfv3AreaLsdbAdvertisement':rlOspfv3AreaLsdbAdvertisement,'rlOspfv3AreaLsdbTypeKnown':rlOspfv3AreaLsdbTypeKnown,'rlOspfv3LinkLsdbTable':rlOspfv3LinkLsdbTable,'rlOspfv3LinkLsdbEntry':rlOspfv3LinkLsdbEntry,_A2:rlOspfv3LinkLsdbProcessId,_A3:rlOspfv3LinkLsdbIfIndex,_A4:rlOspfv3LinkLsdbIfInstId,_A5:rlOspfv3LinkLsdbType,_A6:rlOspfv3LinkLsdbRouterId,_A7:rlOspfv3LinkLsdbLsid,'rlOspfv3LinkLsdbSequence':rlOspfv3LinkLsdbSequence,'rlOspfv3LinkLsdbAge':rlOspfv3LinkLsdbAge,'rlOspfv3LinkLsdbChecksum':rlOspfv3LinkLsdbChecksum,'rlOspfv3LinkLsdbAdvertisement':rlOspfv3LinkLsdbAdvertisement,'rlOspfv3LinkLsdbTypeKnown':rlOspfv3LinkLsdbTypeKnown,'rlOspfv3HostTable':rlOspfv3HostTable,'rlOspfv3HostEntry':rlOspfv3HostEntry,_A8:rlOspfv3HostProcessId,_A9:rlOspfv3HostAddressType,_AA:rlOspfv3HostAddress,'rlOspfv3HostMetric':rlOspfv3HostMetric,'rlOspfv3HostRowStatus':rlOspfv3HostRowStatus,'rlOspfv3HostAreaID':rlOspfv3HostAreaID,'rlOspfv3IfTable':rlOspfv3IfTable,'rlOspfv3IfEntry':rlOspfv3IfEntry,_AB:rlOspfv3IfProcessId,_AC:rlOspfv3IfIndex,_AD:rlOspfv3IfInstId,'rlOspfv3IfAreaId':rlOspfv3IfAreaId,'rlOspfv3IfType':rlOspfv3IfType,'rlOspfv3IfAdminStatus':rlOspfv3IfAdminStatus,'rlOspfv3IfRtrPriority':rlOspfv3IfRtrPriority,'rlOspfv3IfTransitDelay':rlOspfv3IfTransitDelay,'rlOspfv3IfRetransInterval':rlOspfv3IfRetransInterval,'rlOspfv3IfHelloInterval':rlOspfv3IfHelloInterval,'rlOspfv3IfRtrDeadInterval':rlOspfv3IfRtrDeadInterval,'rlOspfv3IfPollInterval':rlOspfv3IfPollInterval,_b:rlOspfv3IfState,'rlOspfv3IfDesignatedRouter':rlOspfv3IfDesignatedRouter,'rlOspfv3IfBackupDesignatedRouter':rlOspfv3IfBackupDesignatedRouter,'rlOspfv3IfEvents':rlOspfv3IfEvents,'rlOspfv3IfRowStatus':rlOspfv3IfRowStatus,'rlOspfv3IfDemand':rlOspfv3IfDemand,'rlOspfv3IfMetricValue':rlOspfv3IfMetricValue,'rlOspfv3IfLinkScopeLsaCount':rlOspfv3IfLinkScopeLsaCount,'rlOspfv3IfLinkLsaCksumSum':rlOspfv3IfLinkLsaCksumSum,'rlOspfv3IfDemandNbrProbe':rlOspfv3IfDemandNbrProbe,'rlOspfv3IfDemandNbrProbeRetransLimit':rlOspfv3IfDemandNbrProbeRetransLimit,'rlOspfv3IfDemandNbrProbeInterval':rlOspfv3IfDemandNbrProbeInterval,'rlOspfv3IfTEDisabled':rlOspfv3IfTEDisabled,'rlOspfv3IfLinkLSASuppression':rlOspfv3IfLinkLSASuppression,'rlOspfv3IfOperStatus':rlOspfv3IfOperStatus,'rlOspfv3IfPassive':rlOspfv3IfPassive,'rlOspfv3IfLsaRefreshIntvl':rlOspfv3IfLsaRefreshIntvl,'rlOspfv3IfFastHelloMultiplier':rlOspfv3IfFastHelloMultiplier,'rlOspfv3IfMtuIgnore':rlOspfv3IfMtuIgnore,'rlOspfv3IfNameLookup':rlOspfv3IfNameLookup,'rlOspfv3VirtIfTable':rlOspfv3VirtIfTable,'rlOspfv3VirtIfEntry':rlOspfv3VirtIfEntry,_AF:rlOspfv3VirtIfProcessId,_AG:rlOspfv3VirtIfAreaId,_AH:rlOspfv3VirtIfNeighbor,'rlOspfv3VirtIfIndex':rlOspfv3VirtIfIndex,'rlOspfv3VirtIfInstId':rlOspfv3VirtIfInstId,'rlOspfv3VirtIfTransitDelay':rlOspfv3VirtIfTransitDelay,'rlOspfv3VirtIfRetransInterval':rlOspfv3VirtIfRetransInterval,'rlOspfv3VirtIfHelloInterval':rlOspfv3VirtIfHelloInterval,'rlOspfv3VirtIfRtrDeadInterval':rlOspfv3VirtIfRtrDeadInterval,_a:rlOspfv3VirtIfState,'rlOspfv3VirtIfEvents':rlOspfv3VirtIfEvents,'rlOspfv3VirtIfRowStatus':rlOspfv3VirtIfRowStatus,'rlOspfv3VirtIfLinkScopeLsaCount':rlOspfv3VirtIfLinkScopeLsaCount,'rlOspfv3VirtIfLinkLsaCksumSum':rlOspfv3VirtIfLinkLsaCksumSum,'rlOspfv3VirtIfAdminStatus':rlOspfv3VirtIfAdminStatus,'rlOspfv3VirtIfOperStatus':rlOspfv3VirtIfOperStatus,'rlOspfv3NbrTable':rlOspfv3NbrTable,'rlOspfv3NbrEntry':rlOspfv3NbrEntry,_AI:rlOspfv3NbrProcessId,_AJ:rlOspfv3NbrIfIndex,_AK:rlOspfv3NbrIfInstId,_AL:rlOspfv3NbrRtrId,'rlOspfv3NbrAddressType':rlOspfv3NbrAddressType,'rlOspfv3NbrAddress':rlOspfv3NbrAddress,'rlOspfv3NbrOptions':rlOspfv3NbrOptions,'rlOspfv3NbrPriority':rlOspfv3NbrPriority,_Ah:rlOspfv3NbrState,'rlOspfv3NbrEvents':rlOspfv3NbrEvents,'rlOspfv3NbrLsRetransQLen':rlOspfv3NbrLsRetransQLen,'rlOspfv3NbrHelloSuppressed':rlOspfv3NbrHelloSuppressed,'rlOspfv3NbrIfId':rlOspfv3NbrIfId,_An:rlOspfv3NbrRestartHelperStatus,_Ao:rlOspfv3NbrRestartHelperAge,_Ap:rlOspfv3NbrRestartHelperExitReason,'rlOspfv3NbrDeadTime':rlOspfv3NbrDeadTime,'rlOspfv3NbrAreaId':rlOspfv3NbrAreaId,'rlOspfv3CfgNbrTable':rlOspfv3CfgNbrTable,'rlOspfv3CfgNbrEntry':rlOspfv3CfgNbrEntry,_AN:rlOspf3CfgNbrProcessId,_AO:rlOspfv3CfgNbrIfIndex,_AP:rlOspfv3CfgNbrIfInstId,_AQ:rlOspfv3CfgNbrAddressType,_AR:rlOspfv3CfgNbrAddress,'rlOspfv3CfgNbrPriority':rlOspfv3CfgNbrPriority,'rlOspfv3CfgNbrRowStatus':rlOspfv3CfgNbrRowStatus,'rlOspfv3VirtNbrTable':rlOspfv3VirtNbrTable,'rlOspfv3VirtNbrEntry':rlOspfv3VirtNbrEntry,_AS:rlOspfv3VirtNbrProcessId,_AT:rlOspfv3VirtNbrArea,_AU:rlOspfv3VirtNbrRtrId,'rlOspfv3VirtNbrIfIndex':rlOspfv3VirtNbrIfIndex,'rlOspfv3VirtNbrIfInstId':rlOspfv3VirtNbrIfInstId,'rlOspfv3VirtNbrAddressType':rlOspfv3VirtNbrAddressType,'rlOspfv3VirtNbrAddress':rlOspfv3VirtNbrAddress,'rlOspfv3VirtNbrOptions':rlOspfv3VirtNbrOptions,_Ai:rlOspfv3VirtNbrState,'rlOspfv3VirtNbrEvents':rlOspfv3VirtNbrEvents,'rlOspfv3VirtNbrLsRetransQLen':rlOspfv3VirtNbrLsRetransQLen,'rlOspfv3VirtNbrHelloSuppressed':rlOspfv3VirtNbrHelloSuppressed,'rlOspfv3VirtNbrIfId':rlOspfv3VirtNbrIfId,_Aq:rlOspfv3VirtNbrRestartHelperStatus,_Ar:rlOspfv3VirtNbrRestartHelperAge,_As:rlOspfv3VirtNbrRestartHelperExitReason,'rlOspfv3VirtNbrDeadTime':rlOspfv3VirtNbrDeadTime,'rlOspfv3AreaAggregateTable':rlOspfv3AreaAggregateTable,'rlOspfv3AreaAggregateEntry':rlOspfv3AreaAggregateEntry,_AV:rlOspfv3AreaAggregateProcessId,_AW:rlOspfv3AreaAggregateAreaID,_AX:rlOspfv3AreaAggregateAreaLsdbType,_AY:rlOspfv3AreaAggregatePrefixType,_AZ:rlOspfv3AreaAggregatePrefix,_Aa:rlOspfv3AreaAggregatePrefixLength,'rlOspfv3AreaAggregateRowStatus':rlOspfv3AreaAggregateRowStatus,'rlOspfv3AreaAggregateEffect':rlOspfv3AreaAggregateEffect,'rlOspfv3AreaAggregateRouteTag':rlOspfv3AreaAggregateRouteTag,'rlOspfv3VirtLinkLsdbTable':rlOspfv3VirtLinkLsdbTable,'rlOspfv3VirtLinkLsdbEntry':rlOspfv3VirtLinkLsdbEntry,_Ab:rlOspfv3VirtLinkLsdbProcessId,_Ac:rlOspfv3VirtLinkLsdbIfAreaId,_Ad:rlOspfv3VirtLinkLsdbIfNeighbor,_Ae:rlOspfv3VirtLinkLsdbType,_Af:rlOspfv3VirtLinkLsdbRouterId,_Ag:rlOspfv3VirtLinkLsdbLsid,'rlOspfv3VirtLinkLsdbSequence':rlOspfv3VirtLinkLsdbSequence,'rlOspfv3VirtLinkLsdbAge':rlOspfv3VirtLinkLsdbAge,'rlOspfv3VirtLinkLsdbChecksum':rlOspfv3VirtLinkLsdbChecksum,'rlOspfv3VirtLinkLsdbAdvertisement':rlOspfv3VirtLinkLsdbAdvertisement,'rlOspfv3VirtLinkLsdbTypeKnown':rlOspfv3VirtLinkLsdbTypeKnown,'rlOspfv3NotificationEntry':rlOspfv3NotificationEntry,_l:rlOspfv3ConfigErrorType,_P:rlOspfv3PacketType,_k:rlOspfv3PacketSrc,'rlOspfv3Notifications':rlOspfv3Notifications,'rlOspfv3VirtIfStateChange':rlOspfv3VirtIfStateChange,'rlOspfv3NbrStateChange':rlOspfv3NbrStateChange,'rlOspfv3VirtNbrStateChange':rlOspfv3VirtNbrStateChange,'rlOspfv3IfConfigError':rlOspfv3IfConfigError,'rlOspfv3VirtIfConfigError':rlOspfv3VirtIfConfigError,'rlOspfv3IfRxBadPacket':rlOspfv3IfRxBadPacket,'rlOspfv3VirtIfRxBadPacket':rlOspfv3VirtIfRxBadPacket,'rlOspfv3LsdbOverflow':rlOspfv3LsdbOverflow,'rlOspfv3LsdbApproachingOverflow':rlOspfv3LsdbApproachingOverflow,'rlOspfv3IfStateChange':rlOspfv3IfStateChange,'rlOspfv3NssaTranslatorStatusChange':rlOspfv3NssaTranslatorStatusChange,'rlOspfv3RestartStatusChange':rlOspfv3RestartStatusChange,'rlOspfv3NbrRestartHelperStatusChange':rlOspfv3NbrRestartHelperStatusChange,'rlOspfv3VirtNbrRestartHelperStatusChange':rlOspfv3VirtNbrRestartHelperStatusChange,'rlOspfv3EnableNotificationsOspfEvents':rlOspfv3EnableNotificationsOspfEvents,'rlOspfv3EnableNotificationsOspfRateLimitSeconds':rlOspfv3EnableNotificationsOspfRateLimitSeconds,'rlOspfv3EnableNotificationsOspfRateLimitTrapNumber':rlOspfv3EnableNotificationsOspfRateLimitTrapNumber})