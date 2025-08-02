_Ar='rlOspfBrRouterOutIf'
_Aq='rlOspfBrRouterNextHopIp'
_Ap='rlOspfBrRouterRouterId'
_Ao='rlOspfBrRouterAreaId'
_An='rlOspfBrRouterProcessId'
_Am='rlOspfVirtLocalLsdbRouterId'
_Al='rlOspfVirtLocalLsdbLsid'
_Ak='rlOspfVirtLocalLsdbType'
_Aj='rlOspfVirtLocalLsdbNeighbor'
_Ai='rlOspfVirtLocalLsdbTransitArea'
_Ah='rlOspfVirtLocalLsdbProcessId'
_Ag='localOpaqueLink'
_Af='rlOspfLocalLsdbRouterId'
_Ae='rlOspfLocalLsdbLsid'
_Ad='rlOspfLocalLsdbType'
_Ac='rlOspfLocalLsdbAddressLessIf'
_Ab='rlOspfLocalLsdbIpAddress'
_Aa='rlOspfLocalLsdbProcessId'
_AZ='rlOspfAreaAggregateMask'
_AY='rlOspfAreaAggregateNet'
_AX='rlOspfAreaAggregateLsdbType'
_AW='rlOspfAreaAggregateAreaID'
_AV='rlOspfAreaAggregateProcessId'
_AU='rlOspfExtLsdbRouterId'
_AT='rlOspfExtLsdbLsid'
_AS='rlOspfExtLsdbType'
_AR='rlOspfExtLsdbProcessId'
_AQ='rlOspfVirtNbrRtrId'
_AP='rlOspfVirtNbrArea'
_AO='rlOspfVirtNbrProcessId'
_AN='exchangeStart'
_AM='rlOspfNbrAddressLessIndex'
_AL='rlOspfNbrIpAddr'
_AK='rlOspfNbrProcessId'
_AJ='rlOspfVirtIfNeighbor'
_AI='rlOspfVirtIfAreaId'
_AH='rlOspfVirtIfProcessId'
_AG='rlOspfIfMetricTOS'
_AF='rlOspfIfMetricAddressLessIf'
_AE='rlOspfIfMetricIpAddress'
_AD='rlOspfIfMetricProcessId'
_AC='RlOspfFastHelloMultiplierRange'
_AB='0000000000000000'
_AA='rlOspfAddressLessIf'
_A9='rlOspfIfIpAddress'
_A8='rlOspfIfProcessId'
_A7='rlOspfHostTOS'
_A6='rlOspfHostIpAddress'
_A5='rlOspfHostProcessId'
_A4='doNotAdvertiseMatching'
_A3='advertiseMatching'
_A2='rlOspfAreaRangeNet'
_A1='rlOspfAreaRangeAreaId'
_A0='rlOspfAreaRangeProcessId'
_z='nssaExternalLink'
_y='asExternalLink'
_x='summaryLink'
_w='rlOspfLsdbRouterId'
_v='rlOspfLsdbLsid'
_u='rlOspfLsdbType'
_t='rlOspfLsdbAreaId'
_s='rlOspfLsdbProcessId'
_r='rlOspfStubTOS'
_q='rlOspfStubAreaId'
_p='rlOspfStubProcessId'
_o='rlOspfAreaId'
_n='rlOspfAreaProcessId'
_m='rlOspfProcessId'
_l='RouterID'
_k='AreaID'
_j='RlOspfDeadIntervalRangeTC'
_i='pointToPoint'
_h='helping'
_g='notHelping'
_f='DisplayString'
_e='IpAddress'
_d='HelloRange'
_c='DesignatedRouterPriority'
_b='00000000'
_a='RlOspfAuthenticationType'
_Z='actFailed'
_Y='goingDown'
_X='goingUp'
_W='up'
_V='topologyChanged'
_U='timedOut'
_T='completed'
_S='inProgress'
_R='Unsigned32'
_Q='Status'
_P='PositiveInteger'
_O='RlOspfUpToRefreshIntervalTC'
_N='TruthValue'
_M='none'
_L='obsolete'
_K='down'
_J='OctetString'
_I='deprecated'
_H='not-accessible'
_G='seconds'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='RADLAN-OSPF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
AreaID,BigMetric,DesignatedRouterPriority,HelloRange,Metric,PositiveInteger,RouterID,Status,TOSType,UpToMaxAge=mibBuilder.importSymbols('OSPF-MIB',_k,'BigMetric',_c,_d,'Metric',_P,_l,_Q,'TOSType','UpToMaxAge')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_e,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_f,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_N)
rlOspf=ModuleIdentity((1,3,6,1,4,1,89,210))
if mibBuilder.loadTexts:rlOspf.setRevisions(('2011-05-04 17:00',))
class RlOspfProcessID(TextualConvention,Integer32):status=_A
class RlOspfFastHelloMultiplierRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
class RlOspfRestartHelperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
class RlOspfRestartExitReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_S,2),(_T,3),(_U,4),(_V,5)))
class RlOspfRouterIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('manual',2)))
class RlOspfAuthenticationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,9)));namedValues=NamedValues(*((_M,0),('simplePassword',1),('md5',2),('null',9)))
class RlOspfUpToRefreshIntervalTC(TextualConvention,Unsigned32):status=_A;displayHint='d-0';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class RlOspfDeadIntervalRangeTC(TextualConvention,Unsigned32):status=_A;displayHint='d-0';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlOspfInstance_Type=RlOspfProcessID
_RlOspfInstance_Object=MibScalar
rlOspfInstance=_RlOspfInstance_Object((1,3,6,1,4,1,89,210,1),_RlOspfInstance_Type())
rlOspfInstance.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfInstance.setStatus(_A)
_RlOspfGeneralGroupTable_Object=MibTable
rlOspfGeneralGroupTable=_RlOspfGeneralGroupTable_Object((1,3,6,1,4,1,89,210,2))
if mibBuilder.loadTexts:rlOspfGeneralGroupTable.setStatus(_A)
_RlOspfGeneralGroupEntry_Object=MibTableRow
rlOspfGeneralGroupEntry=_RlOspfGeneralGroupEntry_Object((1,3,6,1,4,1,89,210,2,1))
rlOspfGeneralGroupEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:rlOspfGeneralGroupEntry.setStatus(_A)
_RlOspfProcessId_Type=RlOspfProcessID
_RlOspfProcessId_Object=MibTableColumn
rlOspfProcessId=_RlOspfProcessId_Object((1,3,6,1,4,1,89,210,2,1,1),_RlOspfProcessId_Type())
rlOspfProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfProcessId.setStatus(_A)
_RlOspfRouterId_Type=RouterID
_RlOspfRouterId_Object=MibTableColumn
rlOspfRouterId=_RlOspfRouterId_Object((1,3,6,1,4,1,89,210,2,1,2),_RlOspfRouterId_Type())
rlOspfRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfRouterId.setStatus(_A)
_RlOspfAdminStat_Type=Status
_RlOspfAdminStat_Object=MibTableColumn
rlOspfAdminStat=_RlOspfAdminStat_Object((1,3,6,1,4,1,89,210,2,1,3),_RlOspfAdminStat_Type())
rlOspfAdminStat.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfAdminStat.setStatus(_A)
class _RlOspfVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('version2',2))
_RlOspfVersionNumber_Type.__name__=_E
_RlOspfVersionNumber_Object=MibTableColumn
rlOspfVersionNumber=_RlOspfVersionNumber_Object((1,3,6,1,4,1,89,210,2,1,4),_RlOspfVersionNumber_Type())
rlOspfVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVersionNumber.setStatus(_A)
_RlOspfAreaBdrRtrStatus_Type=TruthValue
_RlOspfAreaBdrRtrStatus_Object=MibTableColumn
rlOspfAreaBdrRtrStatus=_RlOspfAreaBdrRtrStatus_Object((1,3,6,1,4,1,89,210,2,1,5),_RlOspfAreaBdrRtrStatus_Type())
rlOspfAreaBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaBdrRtrStatus.setStatus(_A)
_RlOspfASBdrRtrStatus_Type=TruthValue
_RlOspfASBdrRtrStatus_Object=MibTableColumn
rlOspfASBdrRtrStatus=_RlOspfASBdrRtrStatus_Object((1,3,6,1,4,1,89,210,2,1,6),_RlOspfASBdrRtrStatus_Type())
rlOspfASBdrRtrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfASBdrRtrStatus.setStatus(_A)
_RlOspfExternLsaCount_Type=Gauge32
_RlOspfExternLsaCount_Object=MibTableColumn
rlOspfExternLsaCount=_RlOspfExternLsaCount_Object((1,3,6,1,4,1,89,210,2,1,7),_RlOspfExternLsaCount_Type())
rlOspfExternLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExternLsaCount.setStatus(_A)
_RlOspfExternLsaCksumSum_Type=Integer32
_RlOspfExternLsaCksumSum_Object=MibTableColumn
rlOspfExternLsaCksumSum=_RlOspfExternLsaCksumSum_Object((1,3,6,1,4,1,89,210,2,1,8),_RlOspfExternLsaCksumSum_Type())
rlOspfExternLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExternLsaCksumSum.setStatus(_A)
_RlOspfTOSSupport_Type=TruthValue
_RlOspfTOSSupport_Object=MibTableColumn
rlOspfTOSSupport=_RlOspfTOSSupport_Object((1,3,6,1,4,1,89,210,2,1,9),_RlOspfTOSSupport_Type())
rlOspfTOSSupport.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfTOSSupport.setStatus(_A)
_RlOspfOriginateNewLsas_Type=Counter32
_RlOspfOriginateNewLsas_Object=MibTableColumn
rlOspfOriginateNewLsas=_RlOspfOriginateNewLsas_Object((1,3,6,1,4,1,89,210,2,1,10),_RlOspfOriginateNewLsas_Type())
rlOspfOriginateNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfOriginateNewLsas.setStatus(_A)
_RlOspfRxNewLsas_Type=Counter32
_RlOspfRxNewLsas_Object=MibTableColumn
rlOspfRxNewLsas=_RlOspfRxNewLsas_Object((1,3,6,1,4,1,89,210,2,1,11),_RlOspfRxNewLsas_Type())
rlOspfRxNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfRxNewLsas.setStatus(_A)
class _RlOspfExtLsdbLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_RlOspfExtLsdbLimit_Type.__name__=_E
_RlOspfExtLsdbLimit_Object=MibTableColumn
rlOspfExtLsdbLimit=_RlOspfExtLsdbLimit_Object((1,3,6,1,4,1,89,210,2,1,12),_RlOspfExtLsdbLimit_Type())
rlOspfExtLsdbLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfExtLsdbLimit.setStatus(_A)
class _RlOspfMulticastExtensions_Type(Integer32):defaultValue=0
_RlOspfMulticastExtensions_Type.__name__=_E
_RlOspfMulticastExtensions_Object=MibTableColumn
rlOspfMulticastExtensions=_RlOspfMulticastExtensions_Object((1,3,6,1,4,1,89,210,2,1,13),_RlOspfMulticastExtensions_Type())
rlOspfMulticastExtensions.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfMulticastExtensions.setStatus(_A)
class _RlOspfExitOverflowInterval_Type(PositiveInteger):defaultValue=0
_RlOspfExitOverflowInterval_Type.__name__=_P
_RlOspfExitOverflowInterval_Object=MibTableColumn
rlOspfExitOverflowInterval=_RlOspfExitOverflowInterval_Object((1,3,6,1,4,1,89,210,2,1,14),_RlOspfExitOverflowInterval_Type())
rlOspfExitOverflowInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfExitOverflowInterval.setStatus(_A)
_RlOspfDemandExtensions_Type=TruthValue
_RlOspfDemandExtensions_Object=MibTableColumn
rlOspfDemandExtensions=_RlOspfDemandExtensions_Object((1,3,6,1,4,1,89,210,2,1,15),_RlOspfDemandExtensions_Type())
rlOspfDemandExtensions.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfDemandExtensions.setStatus(_A)
_RlOspfRFC1583Compatibility_Type=TruthValue
_RlOspfRFC1583Compatibility_Object=MibTableColumn
rlOspfRFC1583Compatibility=_RlOspfRFC1583Compatibility_Object((1,3,6,1,4,1,89,210,2,1,16),_RlOspfRFC1583Compatibility_Type())
rlOspfRFC1583Compatibility.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfRFC1583Compatibility.setStatus(_A)
_RlOspfOpaqueLsaSupport_Type=TruthValue
_RlOspfOpaqueLsaSupport_Object=MibTableColumn
rlOspfOpaqueLsaSupport=_RlOspfOpaqueLsaSupport_Object((1,3,6,1,4,1,89,210,2,1,17),_RlOspfOpaqueLsaSupport_Type())
rlOspfOpaqueLsaSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfOpaqueLsaSupport.setStatus(_A)
_RlOspfReferenceBandwidth_Type=Unsigned32
_RlOspfReferenceBandwidth_Object=MibTableColumn
rlOspfReferenceBandwidth=_RlOspfReferenceBandwidth_Object((1,3,6,1,4,1,89,210,2,1,18),_RlOspfReferenceBandwidth_Type())
rlOspfReferenceBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfReferenceBandwidth.setStatus(_A)
if mibBuilder.loadTexts:rlOspfReferenceBandwidth.setUnits('kilobits per second')
class _RlOspfRestartSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('plannedOnly',2),('plannedAndUnplanned',3)))
_RlOspfRestartSupport_Type.__name__=_E
_RlOspfRestartSupport_Object=MibTableColumn
rlOspfRestartSupport=_RlOspfRestartSupport_Object((1,3,6,1,4,1,89,210,2,1,19),_RlOspfRestartSupport_Type())
rlOspfRestartSupport.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfRestartSupport.setStatus(_A)
class _RlOspfRestartInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_RlOspfRestartInterval_Type.__name__=_E
_RlOspfRestartInterval_Object=MibTableColumn
rlOspfRestartInterval=_RlOspfRestartInterval_Object((1,3,6,1,4,1,89,210,2,1,20),_RlOspfRestartInterval_Type())
rlOspfRestartInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfRestartInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfRestartInterval.setUnits(_G)
_RlOspfRestartStrictLsaChecking_Type=TruthValue
_RlOspfRestartStrictLsaChecking_Object=MibTableColumn
rlOspfRestartStrictLsaChecking=_RlOspfRestartStrictLsaChecking_Object((1,3,6,1,4,1,89,210,2,1,21),_RlOspfRestartStrictLsaChecking_Type())
rlOspfRestartStrictLsaChecking.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfRestartStrictLsaChecking.setStatus(_A)
class _RlOspfRestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRestarting',1),('plannedRestart',2),('unplannedRestart',3)))
_RlOspfRestartStatus_Type.__name__=_E
_RlOspfRestartStatus_Object=MibTableColumn
rlOspfRestartStatus=_RlOspfRestartStatus_Object((1,3,6,1,4,1,89,210,2,1,22),_RlOspfRestartStatus_Type())
rlOspfRestartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfRestartStatus.setStatus(_A)
_RlOspfRestartAge_Type=Unsigned32
_RlOspfRestartAge_Object=MibTableColumn
rlOspfRestartAge=_RlOspfRestartAge_Object((1,3,6,1,4,1,89,210,2,1,23),_RlOspfRestartAge_Type())
rlOspfRestartAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfRestartAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfRestartAge.setUnits(_G)
class _RlOspfRestartExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_RlOspfRestartExitReason_Type.__name__=_E
_RlOspfRestartExitReason_Object=MibTableColumn
rlOspfRestartExitReason=_RlOspfRestartExitReason_Object((1,3,6,1,4,1,89,210,2,1,24),_RlOspfRestartExitReason_Type())
rlOspfRestartExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfRestartExitReason.setStatus(_A)
_RlOspfAsLsaCount_Type=Gauge32
_RlOspfAsLsaCount_Object=MibTableColumn
rlOspfAsLsaCount=_RlOspfAsLsaCount_Object((1,3,6,1,4,1,89,210,2,1,25),_RlOspfAsLsaCount_Type())
rlOspfAsLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAsLsaCount.setStatus(_A)
_RlOspfAsLsaCksumSum_Type=Unsigned32
_RlOspfAsLsaCksumSum_Object=MibTableColumn
rlOspfAsLsaCksumSum=_RlOspfAsLsaCksumSum_Object((1,3,6,1,4,1,89,210,2,1,26),_RlOspfAsLsaCksumSum_Type())
rlOspfAsLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAsLsaCksumSum.setStatus(_A)
_RlOspfStubRouterSupport_Type=TruthValue
_RlOspfStubRouterSupport_Object=MibTableColumn
rlOspfStubRouterSupport=_RlOspfStubRouterSupport_Object((1,3,6,1,4,1,89,210,2,1,27),_RlOspfStubRouterSupport_Type())
rlOspfStubRouterSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfStubRouterSupport.setStatus(_A)
class _RlOspfStubRouterAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNotAdvertise',1),('advertise',2)))
_RlOspfStubRouterAdvertisement_Type.__name__=_E
_RlOspfStubRouterAdvertisement_Object=MibTableColumn
rlOspfStubRouterAdvertisement=_RlOspfStubRouterAdvertisement_Object((1,3,6,1,4,1,89,210,2,1,28),_RlOspfStubRouterAdvertisement_Type())
rlOspfStubRouterAdvertisement.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfStubRouterAdvertisement.setStatus(_A)
_RlOspfDiscontinuityTime_Type=TimeStamp
_RlOspfDiscontinuityTime_Object=MibTableColumn
rlOspfDiscontinuityTime=_RlOspfDiscontinuityTime_Object((1,3,6,1,4,1,89,210,2,1,29),_RlOspfDiscontinuityTime_Type())
rlOspfDiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfDiscontinuityTime.setStatus(_A)
_RlOspfGeneralGroupStatus_Type=RowStatus
_RlOspfGeneralGroupStatus_Object=MibTableColumn
rlOspfGeneralGroupStatus=_RlOspfGeneralGroupStatus_Object((1,3,6,1,4,1,89,210,2,1,30),_RlOspfGeneralGroupStatus_Type())
rlOspfGeneralGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfGeneralGroupStatus.setStatus(_A)
class _RlOspfLogAdjacencyChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('detail',2),('disable',3)))
_RlOspfLogAdjacencyChanges_Type.__name__=_E
_RlOspfLogAdjacencyChanges_Object=MibTableColumn
rlOspfLogAdjacencyChanges=_RlOspfLogAdjacencyChanges_Object((1,3,6,1,4,1,89,210,2,1,31),_RlOspfLogAdjacencyChanges_Type())
rlOspfLogAdjacencyChanges.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfLogAdjacencyChanges.setStatus(_A)
_RlOspfPassiveInterface_Type=TruthValue
_RlOspfPassiveInterface_Object=MibTableColumn
rlOspfPassiveInterface=_RlOspfPassiveInterface_Object((1,3,6,1,4,1,89,210,2,1,32),_RlOspfPassiveInterface_Type())
rlOspfPassiveInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfPassiveInterface.setStatus(_A)
class _RlOspfDefaultMetric_Type(Integer32):defaultValue=0
_RlOspfDefaultMetric_Type.__name__=_E
_RlOspfDefaultMetric_Object=MibTableColumn
rlOspfDefaultMetric=_RlOspfDefaultMetric_Object((1,3,6,1,4,1,89,210,2,1,33),_RlOspfDefaultMetric_Type())
rlOspfDefaultMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfDefaultMetric.setStatus(_A)
class _RlOspfMaximumRedistPrefixNum_Type(Integer32):defaultValue=0
_RlOspfMaximumRedistPrefixNum_Type.__name__=_E
_RlOspfMaximumRedistPrefixNum_Object=MibTableColumn
rlOspfMaximumRedistPrefixNum=_RlOspfMaximumRedistPrefixNum_Object((1,3,6,1,4,1,89,210,2,1,34),_RlOspfMaximumRedistPrefixNum_Type())
rlOspfMaximumRedistPrefixNum.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfMaximumRedistPrefixNum.setStatus(_A)
class _RlOspfMaximumRedistPrefixThreshold_Type(Integer32):defaultValue=75
_RlOspfMaximumRedistPrefixThreshold_Type.__name__=_E
_RlOspfMaximumRedistPrefixThreshold_Object=MibTableColumn
rlOspfMaximumRedistPrefixThreshold=_RlOspfMaximumRedistPrefixThreshold_Object((1,3,6,1,4,1,89,210,2,1,35),_RlOspfMaximumRedistPrefixThreshold_Type())
rlOspfMaximumRedistPrefixThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfMaximumRedistPrefixThreshold.setStatus(_A)
class _RlOspfMaximumRedistPrefixWarningOnly_Type(TruthValue):defaultValue=2
_RlOspfMaximumRedistPrefixWarningOnly_Type.__name__=_N
_RlOspfMaximumRedistPrefixWarningOnly_Object=MibTableColumn
rlOspfMaximumRedistPrefixWarningOnly=_RlOspfMaximumRedistPrefixWarningOnly_Object((1,3,6,1,4,1,89,210,2,1,36),_RlOspfMaximumRedistPrefixWarningOnly_Type())
rlOspfMaximumRedistPrefixWarningOnly.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfMaximumRedistPrefixWarningOnly.setStatus(_A)
class _RlOspfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_K,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfOperStatus_Type.__name__=_E
_RlOspfOperStatus_Object=MibTableColumn
rlOspfOperStatus=_RlOspfOperStatus_Object((1,3,6,1,4,1,89,210,2,1,37),_RlOspfOperStatus_Type())
rlOspfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfOperStatus.setStatus(_A)
_RlOspfNextRouterId_Type=RouterID
_RlOspfNextRouterId_Object=MibTableColumn
rlOspfNextRouterId=_RlOspfNextRouterId_Object((1,3,6,1,4,1,89,210,2,1,38),_RlOspfNextRouterId_Type())
rlOspfNextRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNextRouterId.setStatus(_A)
_RlOspfRouterIdType_Type=RlOspfRouterIdType
_RlOspfRouterIdType_Object=MibTableColumn
rlOspfRouterIdType=_RlOspfRouterIdType_Object((1,3,6,1,4,1,89,210,2,1,39),_RlOspfRouterIdType_Type())
rlOspfRouterIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfRouterIdType.setStatus(_A)
_RlOspfNextRouterIdType_Type=RlOspfRouterIdType
_RlOspfNextRouterIdType_Object=MibTableColumn
rlOspfNextRouterIdType=_RlOspfNextRouterIdType_Object((1,3,6,1,4,1,89,210,2,1,40),_RlOspfNextRouterIdType_Type())
rlOspfNextRouterIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNextRouterIdType.setStatus(_A)
_RlOspfASBdrRtrActualStatus_Type=TruthValue
_RlOspfASBdrRtrActualStatus_Object=MibTableColumn
rlOspfASBdrRtrActualStatus=_RlOspfASBdrRtrActualStatus_Object((1,3,6,1,4,1,89,210,2,1,41),_RlOspfASBdrRtrActualStatus_Type())
rlOspfASBdrRtrActualStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfASBdrRtrActualStatus.setStatus(_A)
class _RlOspfCalcMaxDelay_Type(Unsigned32):defaultValue=5000
_RlOspfCalcMaxDelay_Type.__name__=_R
_RlOspfCalcMaxDelay_Object=MibTableColumn
rlOspfCalcMaxDelay=_RlOspfCalcMaxDelay_Object((1,3,6,1,4,1,89,210,2,1,42),_RlOspfCalcMaxDelay_Type())
rlOspfCalcMaxDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfCalcMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:rlOspfCalcMaxDelay.setUnits('milliseconds')
class _RlOspfRteMaxEqCostPaths_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlOspfRteMaxEqCostPaths_Type.__name__=_R
_RlOspfRteMaxEqCostPaths_Object=MibTableColumn
rlOspfRteMaxEqCostPaths=_RlOspfRteMaxEqCostPaths_Object((1,3,6,1,4,1,89,210,2,1,43),_RlOspfRteMaxEqCostPaths_Type())
rlOspfRteMaxEqCostPaths.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfRteMaxEqCostPaths.setStatus(_A)
_RlOspfAreaTable_Object=MibTable
rlOspfAreaTable=_RlOspfAreaTable_Object((1,3,6,1,4,1,89,210,3))
if mibBuilder.loadTexts:rlOspfAreaTable.setStatus(_A)
_RlOspfAreaEntry_Object=MibTableRow
rlOspfAreaEntry=_RlOspfAreaEntry_Object((1,3,6,1,4,1,89,210,3,1))
rlOspfAreaEntry.setIndexNames((0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:rlOspfAreaEntry.setStatus(_A)
_RlOspfAreaProcessId_Type=RlOspfProcessID
_RlOspfAreaProcessId_Object=MibTableColumn
rlOspfAreaProcessId=_RlOspfAreaProcessId_Object((1,3,6,1,4,1,89,210,3,1,1),_RlOspfAreaProcessId_Type())
rlOspfAreaProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaProcessId.setStatus(_A)
_RlOspfAreaId_Type=AreaID
_RlOspfAreaId_Object=MibTableColumn
rlOspfAreaId=_RlOspfAreaId_Object((1,3,6,1,4,1,89,210,3,1,2),_RlOspfAreaId_Type())
rlOspfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaId.setStatus(_A)
class _RlOspfAuthType_Type(RlOspfAuthenticationType):defaultValue=0
_RlOspfAuthType_Type.__name__=_a
_RlOspfAuthType_Object=MibTableColumn
rlOspfAuthType=_RlOspfAuthType_Object((1,3,6,1,4,1,89,210,3,1,3),_RlOspfAuthType_Type())
rlOspfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAuthType.setStatus(_A)
class _RlOspfImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_RlOspfImportAsExtern_Type.__name__=_E
_RlOspfImportAsExtern_Object=MibTableColumn
rlOspfImportAsExtern=_RlOspfImportAsExtern_Object((1,3,6,1,4,1,89,210,3,1,4),_RlOspfImportAsExtern_Type())
rlOspfImportAsExtern.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfImportAsExtern.setStatus(_A)
_RlOspfSpfRuns_Type=Counter32
_RlOspfSpfRuns_Object=MibTableColumn
rlOspfSpfRuns=_RlOspfSpfRuns_Object((1,3,6,1,4,1,89,210,3,1,5),_RlOspfSpfRuns_Type())
rlOspfSpfRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfSpfRuns.setStatus(_A)
_RlOspfAreaBdrRtrCount_Type=Gauge32
_RlOspfAreaBdrRtrCount_Object=MibTableColumn
rlOspfAreaBdrRtrCount=_RlOspfAreaBdrRtrCount_Object((1,3,6,1,4,1,89,210,3,1,6),_RlOspfAreaBdrRtrCount_Type())
rlOspfAreaBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaBdrRtrCount.setStatus(_A)
_RlOspfAsBdrRtrCount_Type=Gauge32
_RlOspfAsBdrRtrCount_Object=MibTableColumn
rlOspfAsBdrRtrCount=_RlOspfAsBdrRtrCount_Object((1,3,6,1,4,1,89,210,3,1,7),_RlOspfAsBdrRtrCount_Type())
rlOspfAsBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAsBdrRtrCount.setStatus(_A)
_RlOspfAreaLsaCount_Type=Gauge32
_RlOspfAreaLsaCount_Object=MibTableColumn
rlOspfAreaLsaCount=_RlOspfAreaLsaCount_Object((1,3,6,1,4,1,89,210,3,1,8),_RlOspfAreaLsaCount_Type())
rlOspfAreaLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaLsaCount.setStatus(_A)
class _RlOspfAreaLsaCksumSum_Type(Integer32):defaultValue=0
_RlOspfAreaLsaCksumSum_Type.__name__=_E
_RlOspfAreaLsaCksumSum_Object=MibTableColumn
rlOspfAreaLsaCksumSum=_RlOspfAreaLsaCksumSum_Object((1,3,6,1,4,1,89,210,3,1,9),_RlOspfAreaLsaCksumSum_Type())
rlOspfAreaLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaLsaCksumSum.setStatus(_A)
class _RlOspfAreaSummary_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_RlOspfAreaSummary_Type.__name__=_E
_RlOspfAreaSummary_Object=MibTableColumn
rlOspfAreaSummary=_RlOspfAreaSummary_Object((1,3,6,1,4,1,89,210,3,1,10),_RlOspfAreaSummary_Type())
rlOspfAreaSummary.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaSummary.setStatus(_A)
_RlOspfAreaStatus_Type=RowStatus
_RlOspfAreaStatus_Object=MibTableColumn
rlOspfAreaStatus=_RlOspfAreaStatus_Object((1,3,6,1,4,1,89,210,3,1,11),_RlOspfAreaStatus_Type())
rlOspfAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaStatus.setStatus(_A)
class _RlOspfAreaNssaTranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_RlOspfAreaNssaTranslatorRole_Type.__name__=_E
_RlOspfAreaNssaTranslatorRole_Object=MibTableColumn
rlOspfAreaNssaTranslatorRole=_RlOspfAreaNssaTranslatorRole_Object((1,3,6,1,4,1,89,210,3,1,12),_RlOspfAreaNssaTranslatorRole_Type())
rlOspfAreaNssaTranslatorRole.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaNssaTranslatorRole.setStatus(_A)
class _RlOspfAreaNssaTranslatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('elected',2),('disabled',3)))
_RlOspfAreaNssaTranslatorState_Type.__name__=_E
_RlOspfAreaNssaTranslatorState_Object=MibTableColumn
rlOspfAreaNssaTranslatorState=_RlOspfAreaNssaTranslatorState_Object((1,3,6,1,4,1,89,210,3,1,13),_RlOspfAreaNssaTranslatorState_Type())
rlOspfAreaNssaTranslatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaNssaTranslatorState.setStatus(_A)
class _RlOspfAreaNssaTranslatorStabilityInterval_Type(PositiveInteger):defaultValue=40
_RlOspfAreaNssaTranslatorStabilityInterval_Type.__name__=_P
_RlOspfAreaNssaTranslatorStabilityInterval_Object=MibTableColumn
rlOspfAreaNssaTranslatorStabilityInterval=_RlOspfAreaNssaTranslatorStabilityInterval_Object((1,3,6,1,4,1,89,210,3,1,14),_RlOspfAreaNssaTranslatorStabilityInterval_Type())
rlOspfAreaNssaTranslatorStabilityInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaNssaTranslatorStabilityInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfAreaNssaTranslatorStabilityInterval.setUnits(_G)
_RlOspfAreaNssaTranslatorEvents_Type=Counter32
_RlOspfAreaNssaTranslatorEvents_Object=MibTableColumn
rlOspfAreaNssaTranslatorEvents=_RlOspfAreaNssaTranslatorEvents_Object((1,3,6,1,4,1,89,210,3,1,15),_RlOspfAreaNssaTranslatorEvents_Type())
rlOspfAreaNssaTranslatorEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaNssaTranslatorEvents.setStatus(_A)
class _RlOspfAreaAdminStat_Type(Status):defaultValue=1
_RlOspfAreaAdminStat_Type.__name__=_Q
_RlOspfAreaAdminStat_Object=MibTableColumn
rlOspfAreaAdminStat=_RlOspfAreaAdminStat_Object((1,3,6,1,4,1,89,210,3,1,16),_RlOspfAreaAdminStat_Type())
rlOspfAreaAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaAdminStat.setStatus(_A)
class _RlOspfAreaOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_K,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfAreaOperStatus_Type.__name__=_E
_RlOspfAreaOperStatus_Object=MibTableColumn
rlOspfAreaOperStatus=_RlOspfAreaOperStatus_Object((1,3,6,1,4,1,89,210,3,1,17),_RlOspfAreaOperStatus_Type())
rlOspfAreaOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaOperStatus.setStatus(_A)
class _RlOspfAreaFilterPrefixListIn_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlOspfAreaFilterPrefixListIn_Type.__name__=_f
_RlOspfAreaFilterPrefixListIn_Object=MibTableColumn
rlOspfAreaFilterPrefixListIn=_RlOspfAreaFilterPrefixListIn_Object((1,3,6,1,4,1,89,210,3,1,18),_RlOspfAreaFilterPrefixListIn_Type())
rlOspfAreaFilterPrefixListIn.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaFilterPrefixListIn.setStatus(_A)
class _RlOspfAreaFilterPrefixListOut_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlOspfAreaFilterPrefixListOut_Type.__name__=_f
_RlOspfAreaFilterPrefixListOut_Object=MibTableColumn
rlOspfAreaFilterPrefixListOut=_RlOspfAreaFilterPrefixListOut_Object((1,3,6,1,4,1,89,210,3,1,19),_RlOspfAreaFilterPrefixListOut_Type())
rlOspfAreaFilterPrefixListOut.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaFilterPrefixListOut.setStatus(_A)
_RlOspfStubAreaTable_Object=MibTable
rlOspfStubAreaTable=_RlOspfStubAreaTable_Object((1,3,6,1,4,1,89,210,4))
if mibBuilder.loadTexts:rlOspfStubAreaTable.setStatus(_A)
_RlOspfStubAreaEntry_Object=MibTableRow
rlOspfStubAreaEntry=_RlOspfStubAreaEntry_Object((1,3,6,1,4,1,89,210,4,1))
rlOspfStubAreaEntry.setIndexNames((0,_C,_p),(0,_C,_q),(0,_C,_r))
if mibBuilder.loadTexts:rlOspfStubAreaEntry.setStatus(_A)
_RlOspfStubProcessId_Type=RlOspfProcessID
_RlOspfStubProcessId_Object=MibTableColumn
rlOspfStubProcessId=_RlOspfStubProcessId_Object((1,3,6,1,4,1,89,210,4,1,1),_RlOspfStubProcessId_Type())
rlOspfStubProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfStubProcessId.setStatus(_A)
_RlOspfStubAreaId_Type=AreaID
_RlOspfStubAreaId_Object=MibTableColumn
rlOspfStubAreaId=_RlOspfStubAreaId_Object((1,3,6,1,4,1,89,210,4,1,2),_RlOspfStubAreaId_Type())
rlOspfStubAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfStubAreaId.setStatus(_A)
_RlOspfStubTOS_Type=TOSType
_RlOspfStubTOS_Object=MibTableColumn
rlOspfStubTOS=_RlOspfStubTOS_Object((1,3,6,1,4,1,89,210,4,1,3),_RlOspfStubTOS_Type())
rlOspfStubTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfStubTOS.setStatus(_A)
_RlOspfStubMetric_Type=BigMetric
_RlOspfStubMetric_Object=MibTableColumn
rlOspfStubMetric=_RlOspfStubMetric_Object((1,3,6,1,4,1,89,210,4,1,4),_RlOspfStubMetric_Type())
rlOspfStubMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfStubMetric.setStatus(_A)
_RlOspfStubStatus_Type=RowStatus
_RlOspfStubStatus_Object=MibTableColumn
rlOspfStubStatus=_RlOspfStubStatus_Object((1,3,6,1,4,1,89,210,4,1,5),_RlOspfStubStatus_Type())
rlOspfStubStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfStubStatus.setStatus(_A)
class _RlOspfStubMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ospfMetric',1),('comparableCost',2),('nonComparable',3)))
_RlOspfStubMetricType_Type.__name__=_E
_RlOspfStubMetricType_Object=MibTableColumn
rlOspfStubMetricType=_RlOspfStubMetricType_Object((1,3,6,1,4,1,89,210,4,1,6),_RlOspfStubMetricType_Type())
rlOspfStubMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfStubMetricType.setStatus(_A)
_RlOspfLsdbTable_Object=MibTable
rlOspfLsdbTable=_RlOspfLsdbTable_Object((1,3,6,1,4,1,89,210,5))
if mibBuilder.loadTexts:rlOspfLsdbTable.setStatus(_A)
_RlOspfLsdbEntry_Object=MibTableRow
rlOspfLsdbEntry=_RlOspfLsdbEntry_Object((1,3,6,1,4,1,89,210,5,1))
rlOspfLsdbEntry.setIndexNames((0,_C,_s),(0,_C,_t),(0,_C,_u),(0,_C,_v),(0,_C,_w))
if mibBuilder.loadTexts:rlOspfLsdbEntry.setStatus(_A)
_RlOspfLsdbProcessId_Type=RlOspfProcessID
_RlOspfLsdbProcessId_Object=MibTableColumn
rlOspfLsdbProcessId=_RlOspfLsdbProcessId_Object((1,3,6,1,4,1,89,210,5,1,1),_RlOspfLsdbProcessId_Type())
rlOspfLsdbProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbProcessId.setStatus(_A)
_RlOspfLsdbAreaId_Type=AreaID
_RlOspfLsdbAreaId_Object=MibTableColumn
rlOspfLsdbAreaId=_RlOspfLsdbAreaId_Object((1,3,6,1,4,1,89,210,5,1,2),_RlOspfLsdbAreaId_Type())
rlOspfLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbAreaId.setStatus(_A)
class _RlOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,10)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),(_x,3),('asSummaryLink',4),(_y,5),('multicastLink',6),(_z,7),('areaOpaqueLink',10)))
_RlOspfLsdbType_Type.__name__=_E
_RlOspfLsdbType_Object=MibTableColumn
rlOspfLsdbType=_RlOspfLsdbType_Object((1,3,6,1,4,1,89,210,5,1,3),_RlOspfLsdbType_Type())
rlOspfLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbType.setStatus(_A)
_RlOspfLsdbLsid_Type=IpAddress
_RlOspfLsdbLsid_Object=MibTableColumn
rlOspfLsdbLsid=_RlOspfLsdbLsid_Object((1,3,6,1,4,1,89,210,5,1,4),_RlOspfLsdbLsid_Type())
rlOspfLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbLsid.setStatus(_A)
_RlOspfLsdbRouterId_Type=RouterID
_RlOspfLsdbRouterId_Object=MibTableColumn
rlOspfLsdbRouterId=_RlOspfLsdbRouterId_Object((1,3,6,1,4,1,89,210,5,1,5),_RlOspfLsdbRouterId_Type())
rlOspfLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbRouterId.setStatus(_A)
_RlOspfLsdbSequence_Type=Integer32
_RlOspfLsdbSequence_Object=MibTableColumn
rlOspfLsdbSequence=_RlOspfLsdbSequence_Object((1,3,6,1,4,1,89,210,5,1,6),_RlOspfLsdbSequence_Type())
rlOspfLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbSequence.setStatus(_A)
_RlOspfLsdbAge_Type=Integer32
_RlOspfLsdbAge_Object=MibTableColumn
rlOspfLsdbAge=_RlOspfLsdbAge_Object((1,3,6,1,4,1,89,210,5,1,7),_RlOspfLsdbAge_Type())
rlOspfLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfLsdbAge.setUnits(_G)
_RlOspfLsdbChecksum_Type=Integer32
_RlOspfLsdbChecksum_Object=MibTableColumn
rlOspfLsdbChecksum=_RlOspfLsdbChecksum_Object((1,3,6,1,4,1,89,210,5,1,8),_RlOspfLsdbChecksum_Type())
rlOspfLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbChecksum.setStatus(_A)
class _RlOspfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfLsdbAdvertisement_Type.__name__=_J
_RlOspfLsdbAdvertisement_Object=MibTableColumn
rlOspfLsdbAdvertisement=_RlOspfLsdbAdvertisement_Object((1,3,6,1,4,1,89,210,5,1,9),_RlOspfLsdbAdvertisement_Type())
rlOspfLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLsdbAdvertisement.setStatus(_A)
_RlOspfAreaRangeTable_Object=MibTable
rlOspfAreaRangeTable=_RlOspfAreaRangeTable_Object((1,3,6,1,4,1,89,210,6))
if mibBuilder.loadTexts:rlOspfAreaRangeTable.setStatus(_L)
_RlOspfAreaRangeEntry_Object=MibTableRow
rlOspfAreaRangeEntry=_RlOspfAreaRangeEntry_Object((1,3,6,1,4,1,89,210,6,1))
rlOspfAreaRangeEntry.setIndexNames((0,_C,_A0),(0,_C,_A1),(0,_C,_A2))
if mibBuilder.loadTexts:rlOspfAreaRangeEntry.setStatus(_L)
_RlOspfAreaRangeProcessId_Type=RlOspfProcessID
_RlOspfAreaRangeProcessId_Object=MibTableColumn
rlOspfAreaRangeProcessId=_RlOspfAreaRangeProcessId_Object((1,3,6,1,4,1,89,210,6,1,1),_RlOspfAreaRangeProcessId_Type())
rlOspfAreaRangeProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaRangeProcessId.setStatus(_L)
_RlOspfAreaRangeAreaId_Type=AreaID
_RlOspfAreaRangeAreaId_Object=MibTableColumn
rlOspfAreaRangeAreaId=_RlOspfAreaRangeAreaId_Object((1,3,6,1,4,1,89,210,6,1,2),_RlOspfAreaRangeAreaId_Type())
rlOspfAreaRangeAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaRangeAreaId.setStatus(_L)
_RlOspfAreaRangeNet_Type=IpAddress
_RlOspfAreaRangeNet_Object=MibTableColumn
rlOspfAreaRangeNet=_RlOspfAreaRangeNet_Object((1,3,6,1,4,1,89,210,6,1,3),_RlOspfAreaRangeNet_Type())
rlOspfAreaRangeNet.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaRangeNet.setStatus(_L)
_RlOspfAreaRangeMask_Type=IpAddress
_RlOspfAreaRangeMask_Object=MibTableColumn
rlOspfAreaRangeMask=_RlOspfAreaRangeMask_Object((1,3,6,1,4,1,89,210,6,1,4),_RlOspfAreaRangeMask_Type())
rlOspfAreaRangeMask.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaRangeMask.setStatus(_L)
_RlOspfAreaRangeStatus_Type=RowStatus
_RlOspfAreaRangeStatus_Object=MibTableColumn
rlOspfAreaRangeStatus=_RlOspfAreaRangeStatus_Object((1,3,6,1,4,1,89,210,6,1,5),_RlOspfAreaRangeStatus_Type())
rlOspfAreaRangeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaRangeStatus.setStatus(_L)
class _RlOspfAreaRangeEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A3,1),(_A4,2)))
_RlOspfAreaRangeEffect_Type.__name__=_E
_RlOspfAreaRangeEffect_Object=MibTableColumn
rlOspfAreaRangeEffect=_RlOspfAreaRangeEffect_Object((1,3,6,1,4,1,89,210,6,1,6),_RlOspfAreaRangeEffect_Type())
rlOspfAreaRangeEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaRangeEffect.setStatus(_L)
_RlOspfHostTable_Object=MibTable
rlOspfHostTable=_RlOspfHostTable_Object((1,3,6,1,4,1,89,210,7))
if mibBuilder.loadTexts:rlOspfHostTable.setStatus(_A)
_RlOspfHostEntry_Object=MibTableRow
rlOspfHostEntry=_RlOspfHostEntry_Object((1,3,6,1,4,1,89,210,7,1))
rlOspfHostEntry.setIndexNames((0,_C,_A5),(0,_C,_A6),(0,_C,_A7))
if mibBuilder.loadTexts:rlOspfHostEntry.setStatus(_A)
_RlOspfHostProcessId_Type=RlOspfProcessID
_RlOspfHostProcessId_Object=MibTableColumn
rlOspfHostProcessId=_RlOspfHostProcessId_Object((1,3,6,1,4,1,89,210,7,1,1),_RlOspfHostProcessId_Type())
rlOspfHostProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfHostProcessId.setStatus(_A)
_RlOspfHostIpAddress_Type=IpAddress
_RlOspfHostIpAddress_Object=MibTableColumn
rlOspfHostIpAddress=_RlOspfHostIpAddress_Object((1,3,6,1,4,1,89,210,7,1,2),_RlOspfHostIpAddress_Type())
rlOspfHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfHostIpAddress.setStatus(_A)
_RlOspfHostTOS_Type=TOSType
_RlOspfHostTOS_Object=MibTableColumn
rlOspfHostTOS=_RlOspfHostTOS_Object((1,3,6,1,4,1,89,210,7,1,3),_RlOspfHostTOS_Type())
rlOspfHostTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfHostTOS.setStatus(_A)
_RlOspfHostMetric_Type=Metric
_RlOspfHostMetric_Object=MibTableColumn
rlOspfHostMetric=_RlOspfHostMetric_Object((1,3,6,1,4,1,89,210,7,1,4),_RlOspfHostMetric_Type())
rlOspfHostMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfHostMetric.setStatus(_A)
_RlOspfHostStatus_Type=RowStatus
_RlOspfHostStatus_Object=MibTableColumn
rlOspfHostStatus=_RlOspfHostStatus_Object((1,3,6,1,4,1,89,210,7,1,5),_RlOspfHostStatus_Type())
rlOspfHostStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfHostStatus.setStatus(_A)
_RlOspfHostAreaID_Type=AreaID
_RlOspfHostAreaID_Object=MibTableColumn
rlOspfHostAreaID=_RlOspfHostAreaID_Object((1,3,6,1,4,1,89,210,7,1,6),_RlOspfHostAreaID_Type())
rlOspfHostAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfHostAreaID.setStatus(_I)
_RlOspfHostCfgAreaID_Type=AreaID
_RlOspfHostCfgAreaID_Object=MibTableColumn
rlOspfHostCfgAreaID=_RlOspfHostCfgAreaID_Object((1,3,6,1,4,1,89,210,7,1,7),_RlOspfHostCfgAreaID_Type())
rlOspfHostCfgAreaID.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfHostCfgAreaID.setStatus(_A)
_RlOspfIfTable_Object=MibTable
rlOspfIfTable=_RlOspfIfTable_Object((1,3,6,1,4,1,89,210,8))
if mibBuilder.loadTexts:rlOspfIfTable.setStatus(_A)
_RlOspfIfEntry_Object=MibTableRow
rlOspfIfEntry=_RlOspfIfEntry_Object((1,3,6,1,4,1,89,210,8,1))
rlOspfIfEntry.setIndexNames((0,_C,_A8),(0,_C,_A9),(0,_C,_AA))
if mibBuilder.loadTexts:rlOspfIfEntry.setStatus(_A)
_RlOspfIfProcessId_Type=RlOspfProcessID
_RlOspfIfProcessId_Object=MibTableColumn
rlOspfIfProcessId=_RlOspfIfProcessId_Object((1,3,6,1,4,1,89,210,8,1,1),_RlOspfIfProcessId_Type())
rlOspfIfProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfProcessId.setStatus(_A)
_RlOspfIfIpAddress_Type=IpAddress
_RlOspfIfIpAddress_Object=MibTableColumn
rlOspfIfIpAddress=_RlOspfIfIpAddress_Object((1,3,6,1,4,1,89,210,8,1,2),_RlOspfIfIpAddress_Type())
rlOspfIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfIpAddress.setStatus(_A)
_RlOspfAddressLessIf_Type=InterfaceIndexOrZero
_RlOspfAddressLessIf_Object=MibTableColumn
rlOspfAddressLessIf=_RlOspfAddressLessIf_Object((1,3,6,1,4,1,89,210,8,1,3),_RlOspfAddressLessIf_Type())
rlOspfAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAddressLessIf.setStatus(_A)
class _RlOspfIfAreaId_Type(AreaID):defaultHexValue=_b
_RlOspfIfAreaId_Type.__name__=_k
_RlOspfIfAreaId_Object=MibTableColumn
rlOspfIfAreaId=_RlOspfIfAreaId_Object((1,3,6,1,4,1,89,210,8,1,4),_RlOspfIfAreaId_Type())
rlOspfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfAreaId.setStatus(_A)
class _RlOspfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_i,3),('pointToMultipoint',5)))
_RlOspfIfType_Type.__name__=_E
_RlOspfIfType_Object=MibTableColumn
rlOspfIfType=_RlOspfIfType_Object((1,3,6,1,4,1,89,210,8,1,5),_RlOspfIfType_Type())
rlOspfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfType.setStatus(_A)
class _RlOspfIfAdminStat_Type(Status):defaultValue=1
_RlOspfIfAdminStat_Type.__name__=_Q
_RlOspfIfAdminStat_Object=MibTableColumn
rlOspfIfAdminStat=_RlOspfIfAdminStat_Object((1,3,6,1,4,1,89,210,8,1,6),_RlOspfIfAdminStat_Type())
rlOspfIfAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfAdminStat.setStatus(_A)
class _RlOspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RlOspfIfRtrPriority_Type.__name__=_c
_RlOspfIfRtrPriority_Object=MibTableColumn
rlOspfIfRtrPriority=_RlOspfIfRtrPriority_Object((1,3,6,1,4,1,89,210,8,1,7),_RlOspfIfRtrPriority_Type())
rlOspfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfRtrPriority.setStatus(_A)
class _RlOspfIfTransitDelay_Type(RlOspfUpToRefreshIntervalTC):defaultValue=1
_RlOspfIfTransitDelay_Type.__name__=_O
_RlOspfIfTransitDelay_Object=MibTableColumn
rlOspfIfTransitDelay=_RlOspfIfTransitDelay_Object((1,3,6,1,4,1,89,210,8,1,8),_RlOspfIfTransitDelay_Type())
rlOspfIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:rlOspfIfTransitDelay.setUnits(_G)
class _RlOspfIfRetransInterval_Type(RlOspfUpToRefreshIntervalTC):defaultValue=5
_RlOspfIfRetransInterval_Type.__name__=_O
_RlOspfIfRetransInterval_Object=MibTableColumn
rlOspfIfRetransInterval=_RlOspfIfRetransInterval_Object((1,3,6,1,4,1,89,210,8,1,9),_RlOspfIfRetransInterval_Type())
rlOspfIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfIfRetransInterval.setUnits(_G)
class _RlOspfIfHelloInterval_Type(HelloRange):defaultValue=10
_RlOspfIfHelloInterval_Type.__name__=_d
_RlOspfIfHelloInterval_Object=MibTableColumn
rlOspfIfHelloInterval=_RlOspfIfHelloInterval_Object((1,3,6,1,4,1,89,210,8,1,10),_RlOspfIfHelloInterval_Type())
rlOspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfIfHelloInterval.setUnits(_G)
class _RlOspfIfRtrDeadInterval_Type(RlOspfDeadIntervalRangeTC):defaultValue=40
_RlOspfIfRtrDeadInterval_Type.__name__=_j
_RlOspfIfRtrDeadInterval_Object=MibTableColumn
rlOspfIfRtrDeadInterval=_RlOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,89,210,8,1,11),_RlOspfIfRtrDeadInterval_Type())
rlOspfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfIfRtrDeadInterval.setUnits(_G)
class _RlOspfIfPollInterval_Type(PositiveInteger):defaultValue=120
_RlOspfIfPollInterval_Type.__name__=_P
_RlOspfIfPollInterval_Object=MibTableColumn
rlOspfIfPollInterval=_RlOspfIfPollInterval_Object((1,3,6,1,4,1,89,210,8,1,12),_RlOspfIfPollInterval_Type())
rlOspfIfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfPollInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfIfPollInterval.setUnits(_G)
class _RlOspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),('loopback',2),('waiting',3),(_i,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_RlOspfIfState_Type.__name__=_E
_RlOspfIfState_Object=MibTableColumn
rlOspfIfState=_RlOspfIfState_Object((1,3,6,1,4,1,89,210,8,1,13),_RlOspfIfState_Type())
rlOspfIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfState.setStatus(_A)
class _RlOspfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_b
_RlOspfIfDesignatedRouter_Type.__name__=_e
_RlOspfIfDesignatedRouter_Object=MibTableColumn
rlOspfIfDesignatedRouter=_RlOspfIfDesignatedRouter_Object((1,3,6,1,4,1,89,210,8,1,14),_RlOspfIfDesignatedRouter_Type())
rlOspfIfDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfDesignatedRouter.setStatus(_A)
class _RlOspfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_b
_RlOspfIfBackupDesignatedRouter_Type.__name__=_e
_RlOspfIfBackupDesignatedRouter_Object=MibTableColumn
rlOspfIfBackupDesignatedRouter=_RlOspfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,89,210,8,1,15),_RlOspfIfBackupDesignatedRouter_Type())
rlOspfIfBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfBackupDesignatedRouter.setStatus(_A)
_RlOspfIfEvents_Type=Counter32
_RlOspfIfEvents_Object=MibTableColumn
rlOspfIfEvents=_RlOspfIfEvents_Object((1,3,6,1,4,1,89,210,8,1,16),_RlOspfIfEvents_Type())
rlOspfIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfEvents.setStatus(_A)
class _RlOspfIfAuthKey_Type(OctetString):defaultHexValue=_AB;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RlOspfIfAuthKey_Type.__name__=_J
_RlOspfIfAuthKey_Object=MibTableColumn
rlOspfIfAuthKey=_RlOspfIfAuthKey_Object((1,3,6,1,4,1,89,210,8,1,17),_RlOspfIfAuthKey_Type())
rlOspfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfAuthKey.setStatus(_A)
_RlOspfIfStatus_Type=RowStatus
_RlOspfIfStatus_Object=MibTableColumn
rlOspfIfStatus=_RlOspfIfStatus_Object((1,3,6,1,4,1,89,210,8,1,18),_RlOspfIfStatus_Type())
rlOspfIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfStatus.setStatus(_A)
class _RlOspfIfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_RlOspfIfMulticastForwarding_Type.__name__=_E
_RlOspfIfMulticastForwarding_Object=MibTableColumn
rlOspfIfMulticastForwarding=_RlOspfIfMulticastForwarding_Object((1,3,6,1,4,1,89,210,8,1,19),_RlOspfIfMulticastForwarding_Type())
rlOspfIfMulticastForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfMulticastForwarding.setStatus(_A)
class _RlOspfIfDemand_Type(TruthValue):defaultValue=2
_RlOspfIfDemand_Type.__name__=_N
_RlOspfIfDemand_Object=MibTableColumn
rlOspfIfDemand=_RlOspfIfDemand_Object((1,3,6,1,4,1,89,210,8,1,20),_RlOspfIfDemand_Type())
rlOspfIfDemand.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfDemand.setStatus(_A)
class _RlOspfIfAuthType_Type(RlOspfAuthenticationType):defaultValue=0
_RlOspfIfAuthType_Type.__name__=_a
_RlOspfIfAuthType_Object=MibTableColumn
rlOspfIfAuthType=_RlOspfIfAuthType_Object((1,3,6,1,4,1,89,210,8,1,21),_RlOspfIfAuthType_Type())
rlOspfIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfAuthType.setStatus(_A)
_RlOspfIfLsaCount_Type=Gauge32
_RlOspfIfLsaCount_Object=MibTableColumn
rlOspfIfLsaCount=_RlOspfIfLsaCount_Object((1,3,6,1,4,1,89,210,8,1,22),_RlOspfIfLsaCount_Type())
rlOspfIfLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfLsaCount.setStatus(_A)
_RlOspfIfLsaCksumSum_Type=Unsigned32
_RlOspfIfLsaCksumSum_Object=MibTableColumn
rlOspfIfLsaCksumSum=_RlOspfIfLsaCksumSum_Object((1,3,6,1,4,1,89,210,8,1,23),_RlOspfIfLsaCksumSum_Type())
rlOspfIfLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfLsaCksumSum.setStatus(_A)
_RlOspfIfDesignatedRouterId_Type=RouterID
_RlOspfIfDesignatedRouterId_Object=MibTableColumn
rlOspfIfDesignatedRouterId=_RlOspfIfDesignatedRouterId_Object((1,3,6,1,4,1,89,210,8,1,24),_RlOspfIfDesignatedRouterId_Type())
rlOspfIfDesignatedRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfDesignatedRouterId.setStatus(_A)
_RlOspfIfBackupDesignatedRouterId_Type=RouterID
_RlOspfIfBackupDesignatedRouterId_Object=MibTableColumn
rlOspfIfBackupDesignatedRouterId=_RlOspfIfBackupDesignatedRouterId_Object((1,3,6,1,4,1,89,210,8,1,25),_RlOspfIfBackupDesignatedRouterId_Type())
rlOspfIfBackupDesignatedRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfBackupDesignatedRouterId.setStatus(_A)
class _RlOspfIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_K,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfIfOperStatus_Type.__name__=_E
_RlOspfIfOperStatus_Object=MibTableColumn
rlOspfIfOperStatus=_RlOspfIfOperStatus_Object((1,3,6,1,4,1,89,210,8,1,26),_RlOspfIfOperStatus_Type())
rlOspfIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfOperStatus.setStatus(_A)
class _RlOspfIfAuthKeyChain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RlOspfIfAuthKeyChain_Type.__name__=_J
_RlOspfIfAuthKeyChain_Object=MibTableColumn
rlOspfIfAuthKeyChain=_RlOspfIfAuthKeyChain_Object((1,3,6,1,4,1,89,210,8,1,27),_RlOspfIfAuthKeyChain_Type())
rlOspfIfAuthKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfAuthKeyChain.setStatus(_A)
class _RlOspfIfPassive_Type(TruthValue):defaultValue=2
_RlOspfIfPassive_Type.__name__=_N
_RlOspfIfPassive_Object=MibTableColumn
rlOspfIfPassive=_RlOspfIfPassive_Object((1,3,6,1,4,1,89,210,8,1,28),_RlOspfIfPassive_Type())
rlOspfIfPassive.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfIfPassive.setStatus(_A)
class _RlOspfIfLsaRefreshIntvl_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3599))
_RlOspfIfLsaRefreshIntvl_Type.__name__=_E
_RlOspfIfLsaRefreshIntvl_Object=MibTableColumn
rlOspfIfLsaRefreshIntvl=_RlOspfIfLsaRefreshIntvl_Object((1,3,6,1,4,1,89,210,8,1,29),_RlOspfIfLsaRefreshIntvl_Type())
rlOspfIfLsaRefreshIntvl.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfIfLsaRefreshIntvl.setStatus(_A)
if mibBuilder.loadTexts:rlOspfIfLsaRefreshIntvl.setUnits(_G)
class _RlOspfIfFastHelloMultiplier_Type(RlOspfFastHelloMultiplierRange):defaultValue=5
_RlOspfIfFastHelloMultiplier_Type.__name__=_AC
_RlOspfIfFastHelloMultiplier_Object=MibTableColumn
rlOspfIfFastHelloMultiplier=_RlOspfIfFastHelloMultiplier_Object((1,3,6,1,4,1,89,210,8,1,30),_RlOspfIfFastHelloMultiplier_Type())
rlOspfIfFastHelloMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfFastHelloMultiplier.setStatus(_A)
class _RlOspfIfMtuIgnore_Type(TruthValue):defaultValue=2
_RlOspfIfMtuIgnore_Type.__name__=_N
_RlOspfIfMtuIgnore_Object=MibTableColumn
rlOspfIfMtuIgnore=_RlOspfIfMtuIgnore_Object((1,3,6,1,4,1,89,210,8,1,31),_RlOspfIfMtuIgnore_Type())
rlOspfIfMtuIgnore.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfIfMtuIgnore.setStatus(_A)
_RlOspfIfNameLookup_Type=TruthValue
_RlOspfIfNameLookup_Object=MibTableColumn
rlOspfIfNameLookup=_RlOspfIfNameLookup_Object((1,3,6,1,4,1,89,210,8,1,32),_RlOspfIfNameLookup_Type())
rlOspfIfNameLookup.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfIfNameLookup.setStatus(_A)
_RlOspfIfIfIndex_Type=Integer32
_RlOspfIfIfIndex_Object=MibTableColumn
rlOspfIfIfIndex=_RlOspfIfIfIndex_Object((1,3,6,1,4,1,89,210,8,1,33),_RlOspfIfIfIndex_Type())
rlOspfIfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfIfIndex.setStatus(_A)
_RlOspfIfActualAuthType_Type=RlOspfAuthenticationType
_RlOspfIfActualAuthType_Object=MibTableColumn
rlOspfIfActualAuthType=_RlOspfIfActualAuthType_Object((1,3,6,1,4,1,89,210,8,1,34),_RlOspfIfActualAuthType_Type())
rlOspfIfActualAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfActualAuthType.setStatus(_A)
_RlOspfIfMetricTable_Object=MibTable
rlOspfIfMetricTable=_RlOspfIfMetricTable_Object((1,3,6,1,4,1,89,210,9))
if mibBuilder.loadTexts:rlOspfIfMetricTable.setStatus(_A)
_RlOspfIfMetricEntry_Object=MibTableRow
rlOspfIfMetricEntry=_RlOspfIfMetricEntry_Object((1,3,6,1,4,1,89,210,9,1))
rlOspfIfMetricEntry.setIndexNames((0,_C,_AD),(0,_C,_AE),(0,_C,_AF),(0,_C,_AG))
if mibBuilder.loadTexts:rlOspfIfMetricEntry.setStatus(_A)
_RlOspfIfMetricProcessId_Type=RlOspfProcessID
_RlOspfIfMetricProcessId_Object=MibTableColumn
rlOspfIfMetricProcessId=_RlOspfIfMetricProcessId_Object((1,3,6,1,4,1,89,210,9,1,1),_RlOspfIfMetricProcessId_Type())
rlOspfIfMetricProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfMetricProcessId.setStatus(_A)
_RlOspfIfMetricIpAddress_Type=IpAddress
_RlOspfIfMetricIpAddress_Object=MibTableColumn
rlOspfIfMetricIpAddress=_RlOspfIfMetricIpAddress_Object((1,3,6,1,4,1,89,210,9,1,2),_RlOspfIfMetricIpAddress_Type())
rlOspfIfMetricIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfMetricIpAddress.setStatus(_A)
_RlOspfIfMetricAddressLessIf_Type=InterfaceIndexOrZero
_RlOspfIfMetricAddressLessIf_Object=MibTableColumn
rlOspfIfMetricAddressLessIf=_RlOspfIfMetricAddressLessIf_Object((1,3,6,1,4,1,89,210,9,1,3),_RlOspfIfMetricAddressLessIf_Type())
rlOspfIfMetricAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfMetricAddressLessIf.setStatus(_A)
_RlOspfIfMetricTOS_Type=TOSType
_RlOspfIfMetricTOS_Object=MibTableColumn
rlOspfIfMetricTOS=_RlOspfIfMetricTOS_Object((1,3,6,1,4,1,89,210,9,1,4),_RlOspfIfMetricTOS_Type())
rlOspfIfMetricTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfIfMetricTOS.setStatus(_A)
_RlOspfIfMetricValue_Type=Metric
_RlOspfIfMetricValue_Object=MibTableColumn
rlOspfIfMetricValue=_RlOspfIfMetricValue_Object((1,3,6,1,4,1,89,210,9,1,5),_RlOspfIfMetricValue_Type())
rlOspfIfMetricValue.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfMetricValue.setStatus(_A)
_RlOspfIfMetricStatus_Type=RowStatus
_RlOspfIfMetricStatus_Object=MibTableColumn
rlOspfIfMetricStatus=_RlOspfIfMetricStatus_Object((1,3,6,1,4,1,89,210,9,1,6),_RlOspfIfMetricStatus_Type())
rlOspfIfMetricStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfIfMetricStatus.setStatus(_A)
_RlOspfVirtIfTable_Object=MibTable
rlOspfVirtIfTable=_RlOspfVirtIfTable_Object((1,3,6,1,4,1,89,210,10))
if mibBuilder.loadTexts:rlOspfVirtIfTable.setStatus(_A)
_RlOspfVirtIfEntry_Object=MibTableRow
rlOspfVirtIfEntry=_RlOspfVirtIfEntry_Object((1,3,6,1,4,1,89,210,10,1))
rlOspfVirtIfEntry.setIndexNames((0,_C,_AH),(0,_C,_AI),(0,_C,_AJ))
if mibBuilder.loadTexts:rlOspfVirtIfEntry.setStatus(_A)
_RlOspfVirtIfProcessId_Type=RlOspfProcessID
_RlOspfVirtIfProcessId_Object=MibTableColumn
rlOspfVirtIfProcessId=_RlOspfVirtIfProcessId_Object((1,3,6,1,4,1,89,210,10,1,1),_RlOspfVirtIfProcessId_Type())
rlOspfVirtIfProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfProcessId.setStatus(_A)
_RlOspfVirtIfAreaId_Type=AreaID
_RlOspfVirtIfAreaId_Object=MibTableColumn
rlOspfVirtIfAreaId=_RlOspfVirtIfAreaId_Object((1,3,6,1,4,1,89,210,10,1,2),_RlOspfVirtIfAreaId_Type())
rlOspfVirtIfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfAreaId.setStatus(_A)
_RlOspfVirtIfNeighbor_Type=RouterID
_RlOspfVirtIfNeighbor_Object=MibTableColumn
rlOspfVirtIfNeighbor=_RlOspfVirtIfNeighbor_Object((1,3,6,1,4,1,89,210,10,1,3),_RlOspfVirtIfNeighbor_Type())
rlOspfVirtIfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfNeighbor.setStatus(_A)
class _RlOspfVirtIfTransitDelay_Type(RlOspfUpToRefreshIntervalTC):defaultValue=1
_RlOspfVirtIfTransitDelay_Type.__name__=_O
_RlOspfVirtIfTransitDelay_Object=MibTableColumn
rlOspfVirtIfTransitDelay=_RlOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,89,210,10,1,4),_RlOspfVirtIfTransitDelay_Type())
rlOspfVirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:rlOspfVirtIfTransitDelay.setUnits(_G)
class _RlOspfVirtIfRetransInterval_Type(RlOspfUpToRefreshIntervalTC):defaultValue=5
_RlOspfVirtIfRetransInterval_Type.__name__=_O
_RlOspfVirtIfRetransInterval_Object=MibTableColumn
rlOspfVirtIfRetransInterval=_RlOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,89,210,10,1,5),_RlOspfVirtIfRetransInterval_Type())
rlOspfVirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfVirtIfRetransInterval.setUnits(_G)
class _RlOspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_RlOspfVirtIfHelloInterval_Type.__name__=_d
_RlOspfVirtIfHelloInterval_Object=MibTableColumn
rlOspfVirtIfHelloInterval=_RlOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,89,210,10,1,6),_RlOspfVirtIfHelloInterval_Type())
rlOspfVirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfVirtIfHelloInterval.setUnits(_G)
class _RlOspfVirtIfRtrDeadInterval_Type(RlOspfDeadIntervalRangeTC):defaultValue=60
_RlOspfVirtIfRtrDeadInterval_Type.__name__=_j
_RlOspfVirtIfRtrDeadInterval_Object=MibTableColumn
rlOspfVirtIfRtrDeadInterval=_RlOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,89,210,10,1,7),_RlOspfVirtIfRtrDeadInterval_Type())
rlOspfVirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:rlOspfVirtIfRtrDeadInterval.setUnits(_G)
class _RlOspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_K,1),(_i,4)))
_RlOspfVirtIfState_Type.__name__=_E
_RlOspfVirtIfState_Object=MibTableColumn
rlOspfVirtIfState=_RlOspfVirtIfState_Object((1,3,6,1,4,1,89,210,10,1,8),_RlOspfVirtIfState_Type())
rlOspfVirtIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfState.setStatus(_A)
_RlOspfVirtIfEvents_Type=Counter32
_RlOspfVirtIfEvents_Object=MibTableColumn
rlOspfVirtIfEvents=_RlOspfVirtIfEvents_Object((1,3,6,1,4,1,89,210,10,1,9),_RlOspfVirtIfEvents_Type())
rlOspfVirtIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfEvents.setStatus(_A)
class _RlOspfVirtIfAuthKey_Type(OctetString):defaultHexValue=_AB;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RlOspfVirtIfAuthKey_Type.__name__=_J
_RlOspfVirtIfAuthKey_Object=MibTableColumn
rlOspfVirtIfAuthKey=_RlOspfVirtIfAuthKey_Object((1,3,6,1,4,1,89,210,10,1,10),_RlOspfVirtIfAuthKey_Type())
rlOspfVirtIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfAuthKey.setStatus(_A)
_RlOspfVirtIfStatus_Type=RowStatus
_RlOspfVirtIfStatus_Object=MibTableColumn
rlOspfVirtIfStatus=_RlOspfVirtIfStatus_Object((1,3,6,1,4,1,89,210,10,1,11),_RlOspfVirtIfStatus_Type())
rlOspfVirtIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfStatus.setStatus(_A)
class _RlOspfVirtIfAuthType_Type(RlOspfAuthenticationType):defaultValue=0
_RlOspfVirtIfAuthType_Type.__name__=_a
_RlOspfVirtIfAuthType_Object=MibTableColumn
rlOspfVirtIfAuthType=_RlOspfVirtIfAuthType_Object((1,3,6,1,4,1,89,210,10,1,12),_RlOspfVirtIfAuthType_Type())
rlOspfVirtIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfAuthType.setStatus(_A)
_RlOspfVirtIfLsaCount_Type=Gauge32
_RlOspfVirtIfLsaCount_Object=MibTableColumn
rlOspfVirtIfLsaCount=_RlOspfVirtIfLsaCount_Object((1,3,6,1,4,1,89,210,10,1,13),_RlOspfVirtIfLsaCount_Type())
rlOspfVirtIfLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfLsaCount.setStatus(_A)
_RlOspfVirtIfLsaCksumSum_Type=Unsigned32
_RlOspfVirtIfLsaCksumSum_Object=MibTableColumn
rlOspfVirtIfLsaCksumSum=_RlOspfVirtIfLsaCksumSum_Object((1,3,6,1,4,1,89,210,10,1,14),_RlOspfVirtIfLsaCksumSum_Type())
rlOspfVirtIfLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfLsaCksumSum.setStatus(_A)
class _RlOspfVirtIfAuthKeyChain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RlOspfVirtIfAuthKeyChain_Type.__name__=_J
_RlOspfVirtIfAuthKeyChain_Object=MibTableColumn
rlOspfVirtIfAuthKeyChain=_RlOspfVirtIfAuthKeyChain_Object((1,3,6,1,4,1,89,210,10,1,15),_RlOspfVirtIfAuthKeyChain_Type())
rlOspfVirtIfAuthKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfAuthKeyChain.setStatus(_A)
class _RlOspfVirtIfAdminStatus_Type(Status):defaultValue=1
_RlOspfVirtIfAdminStatus_Type.__name__=_Q
_RlOspfVirtIfAdminStatus_Object=MibTableColumn
rlOspfVirtIfAdminStatus=_RlOspfVirtIfAdminStatus_Object((1,3,6,1,4,1,89,210,10,1,16),_RlOspfVirtIfAdminStatus_Type())
rlOspfVirtIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfVirtIfAdminStatus.setStatus(_A)
class _RlOspfVirtIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_K,2),(_X,3),(_Y,4),(_Z,5)))
_RlOspfVirtIfOperStatus_Type.__name__=_E
_RlOspfVirtIfOperStatus_Object=MibTableColumn
rlOspfVirtIfOperStatus=_RlOspfVirtIfOperStatus_Object((1,3,6,1,4,1,89,210,10,1,17),_RlOspfVirtIfOperStatus_Type())
rlOspfVirtIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfOperStatus.setStatus(_A)
_RlOspfVirtIfIndex_Type=Integer32
_RlOspfVirtIfIndex_Object=MibTableColumn
rlOspfVirtIfIndex=_RlOspfVirtIfIndex_Object((1,3,6,1,4,1,89,210,10,1,18),_RlOspfVirtIfIndex_Type())
rlOspfVirtIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfIndex.setStatus(_A)
_RlOspfVirtIfActualAuthType_Type=RlOspfAuthenticationType
_RlOspfVirtIfActualAuthType_Object=MibTableColumn
rlOspfVirtIfActualAuthType=_RlOspfVirtIfActualAuthType_Object((1,3,6,1,4,1,89,210,10,1,19),_RlOspfVirtIfActualAuthType_Type())
rlOspfVirtIfActualAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtIfActualAuthType.setStatus(_A)
_RlOspfNbrTable_Object=MibTable
rlOspfNbrTable=_RlOspfNbrTable_Object((1,3,6,1,4,1,89,210,11))
if mibBuilder.loadTexts:rlOspfNbrTable.setStatus(_A)
_RlOspfNbrEntry_Object=MibTableRow
rlOspfNbrEntry=_RlOspfNbrEntry_Object((1,3,6,1,4,1,89,210,11,1))
rlOspfNbrEntry.setIndexNames((0,_C,_AK),(0,_C,_AL),(0,_C,_AM))
if mibBuilder.loadTexts:rlOspfNbrEntry.setStatus(_A)
_RlOspfNbrProcessId_Type=RlOspfProcessID
_RlOspfNbrProcessId_Object=MibTableColumn
rlOspfNbrProcessId=_RlOspfNbrProcessId_Object((1,3,6,1,4,1,89,210,11,1,1),_RlOspfNbrProcessId_Type())
rlOspfNbrProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrProcessId.setStatus(_A)
_RlOspfNbrIpAddr_Type=IpAddress
_RlOspfNbrIpAddr_Object=MibTableColumn
rlOspfNbrIpAddr=_RlOspfNbrIpAddr_Object((1,3,6,1,4,1,89,210,11,1,2),_RlOspfNbrIpAddr_Type())
rlOspfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrIpAddr.setStatus(_A)
_RlOspfNbrAddressLessIndex_Type=InterfaceIndexOrZero
_RlOspfNbrAddressLessIndex_Object=MibTableColumn
rlOspfNbrAddressLessIndex=_RlOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,89,210,11,1,3),_RlOspfNbrAddressLessIndex_Type())
rlOspfNbrAddressLessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrAddressLessIndex.setStatus(_A)
class _RlOspfNbrRtrId_Type(RouterID):defaultHexValue=_b
_RlOspfNbrRtrId_Type.__name__=_l
_RlOspfNbrRtrId_Object=MibTableColumn
rlOspfNbrRtrId=_RlOspfNbrRtrId_Object((1,3,6,1,4,1,89,210,11,1,4),_RlOspfNbrRtrId_Type())
rlOspfNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrRtrId.setStatus(_A)
class _RlOspfNbrOptions_Type(Integer32):defaultValue=0
_RlOspfNbrOptions_Type.__name__=_E
_RlOspfNbrOptions_Object=MibTableColumn
rlOspfNbrOptions=_RlOspfNbrOptions_Object((1,3,6,1,4,1,89,210,11,1,5),_RlOspfNbrOptions_Type())
rlOspfNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrOptions.setStatus(_A)
class _RlOspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RlOspfNbrPriority_Type.__name__=_c
_RlOspfNbrPriority_Object=MibTableColumn
rlOspfNbrPriority=_RlOspfNbrPriority_Object((1,3,6,1,4,1,89,210,11,1,6),_RlOspfNbrPriority_Type())
rlOspfNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfNbrPriority.setStatus(_A)
class _RlOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('attempt',2),('init',3),('twoWay',4),(_AN,5),('exchange',6),('loading',7),('full',8)))
_RlOspfNbrState_Type.__name__=_E
_RlOspfNbrState_Object=MibTableColumn
rlOspfNbrState=_RlOspfNbrState_Object((1,3,6,1,4,1,89,210,11,1,7),_RlOspfNbrState_Type())
rlOspfNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrState.setStatus(_A)
_RlOspfNbrEvents_Type=Counter32
_RlOspfNbrEvents_Object=MibTableColumn
rlOspfNbrEvents=_RlOspfNbrEvents_Object((1,3,6,1,4,1,89,210,11,1,8),_RlOspfNbrEvents_Type())
rlOspfNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrEvents.setStatus(_A)
_RlOspfNbrLsRetransQLen_Type=Gauge32
_RlOspfNbrLsRetransQLen_Object=MibTableColumn
rlOspfNbrLsRetransQLen=_RlOspfNbrLsRetransQLen_Object((1,3,6,1,4,1,89,210,11,1,9),_RlOspfNbrLsRetransQLen_Type())
rlOspfNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrLsRetransQLen.setStatus(_A)
_RlOspfNbmaNbrStatus_Type=RowStatus
_RlOspfNbmaNbrStatus_Object=MibTableColumn
rlOspfNbmaNbrStatus=_RlOspfNbmaNbrStatus_Object((1,3,6,1,4,1,89,210,11,1,10),_RlOspfNbmaNbrStatus_Type())
rlOspfNbmaNbrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfNbmaNbrStatus.setStatus(_A)
class _RlOspfNbmaNbrPermanence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_RlOspfNbmaNbrPermanence_Type.__name__=_E
_RlOspfNbmaNbrPermanence_Object=MibTableColumn
rlOspfNbmaNbrPermanence=_RlOspfNbmaNbrPermanence_Object((1,3,6,1,4,1,89,210,11,1,11),_RlOspfNbmaNbrPermanence_Type())
rlOspfNbmaNbrPermanence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbmaNbrPermanence.setStatus(_A)
_RlOspfNbrHelloSuppressed_Type=TruthValue
_RlOspfNbrHelloSuppressed_Object=MibTableColumn
rlOspfNbrHelloSuppressed=_RlOspfNbrHelloSuppressed_Object((1,3,6,1,4,1,89,210,11,1,12),_RlOspfNbrHelloSuppressed_Type())
rlOspfNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrHelloSuppressed.setStatus(_A)
class _RlOspfNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_RlOspfNbrRestartHelperStatus_Type.__name__=_E
_RlOspfNbrRestartHelperStatus_Object=MibTableColumn
rlOspfNbrRestartHelperStatus=_RlOspfNbrRestartHelperStatus_Object((1,3,6,1,4,1,89,210,11,1,13),_RlOspfNbrRestartHelperStatus_Type())
rlOspfNbrRestartHelperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrRestartHelperStatus.setStatus(_A)
_RlOspfNbrRestartHelperAge_Type=Unsigned32
_RlOspfNbrRestartHelperAge_Object=MibTableColumn
rlOspfNbrRestartHelperAge=_RlOspfNbrRestartHelperAge_Object((1,3,6,1,4,1,89,210,11,1,14),_RlOspfNbrRestartHelperAge_Type())
rlOspfNbrRestartHelperAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfNbrRestartHelperAge.setUnits(_G)
class _RlOspfNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_RlOspfNbrRestartHelperExitReason_Type.__name__=_E
_RlOspfNbrRestartHelperExitReason_Object=MibTableColumn
rlOspfNbrRestartHelperExitReason=_RlOspfNbrRestartHelperExitReason_Object((1,3,6,1,4,1,89,210,11,1,15),_RlOspfNbrRestartHelperExitReason_Type())
rlOspfNbrRestartHelperExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrRestartHelperExitReason.setStatus(_A)
_RlOspfNbrDeadTime_Type=PositiveInteger
_RlOspfNbrDeadTime_Object=MibTableColumn
rlOspfNbrDeadTime=_RlOspfNbrDeadTime_Object((1,3,6,1,4,1,89,210,11,1,16),_RlOspfNbrDeadTime_Type())
rlOspfNbrDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrDeadTime.setStatus(_A)
_RlOspfNbrAreaId_Type=AreaID
_RlOspfNbrAreaId_Object=MibTableColumn
rlOspfNbrAreaId=_RlOspfNbrAreaId_Object((1,3,6,1,4,1,89,210,11,1,17),_RlOspfNbrAreaId_Type())
rlOspfNbrAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrAreaId.setStatus(_A)
_RlOspfNbrIfIndex_Type=Integer32
_RlOspfNbrIfIndex_Object=MibTableColumn
rlOspfNbrIfIndex=_RlOspfNbrIfIndex_Object((1,3,6,1,4,1,89,210,11,1,18),_RlOspfNbrIfIndex_Type())
rlOspfNbrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrIfIndex.setStatus(_A)
_RlOspfNbrIfIpAddr_Type=IpAddress
_RlOspfNbrIfIpAddr_Object=MibTableColumn
rlOspfNbrIfIpAddr=_RlOspfNbrIfIpAddr_Object((1,3,6,1,4,1,89,210,11,1,19),_RlOspfNbrIfIpAddr_Type())
rlOspfNbrIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfNbrIfIpAddr.setStatus(_A)
_RlOspfVirtNbrTable_Object=MibTable
rlOspfVirtNbrTable=_RlOspfVirtNbrTable_Object((1,3,6,1,4,1,89,210,12))
if mibBuilder.loadTexts:rlOspfVirtNbrTable.setStatus(_A)
_RlOspfVirtNbrEntry_Object=MibTableRow
rlOspfVirtNbrEntry=_RlOspfVirtNbrEntry_Object((1,3,6,1,4,1,89,210,12,1))
rlOspfVirtNbrEntry.setIndexNames((0,_C,_AO),(0,_C,_AP),(0,_C,_AQ))
if mibBuilder.loadTexts:rlOspfVirtNbrEntry.setStatus(_A)
_RlOspfVirtNbrProcessId_Type=RlOspfProcessID
_RlOspfVirtNbrProcessId_Object=MibTableColumn
rlOspfVirtNbrProcessId=_RlOspfVirtNbrProcessId_Object((1,3,6,1,4,1,89,210,12,1,1),_RlOspfVirtNbrProcessId_Type())
rlOspfVirtNbrProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrProcessId.setStatus(_A)
_RlOspfVirtNbrArea_Type=AreaID
_RlOspfVirtNbrArea_Object=MibTableColumn
rlOspfVirtNbrArea=_RlOspfVirtNbrArea_Object((1,3,6,1,4,1,89,210,12,1,2),_RlOspfVirtNbrArea_Type())
rlOspfVirtNbrArea.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrArea.setStatus(_A)
_RlOspfVirtNbrRtrId_Type=RouterID
_RlOspfVirtNbrRtrId_Object=MibTableColumn
rlOspfVirtNbrRtrId=_RlOspfVirtNbrRtrId_Object((1,3,6,1,4,1,89,210,12,1,3),_RlOspfVirtNbrRtrId_Type())
rlOspfVirtNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrRtrId.setStatus(_A)
_RlOspfVirtNbrIpAddr_Type=IpAddress
_RlOspfVirtNbrIpAddr_Object=MibTableColumn
rlOspfVirtNbrIpAddr=_RlOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,89,210,12,1,4),_RlOspfVirtNbrIpAddr_Type())
rlOspfVirtNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrIpAddr.setStatus(_A)
_RlOspfVirtNbrOptions_Type=Integer32
_RlOspfVirtNbrOptions_Object=MibTableColumn
rlOspfVirtNbrOptions=_RlOspfVirtNbrOptions_Object((1,3,6,1,4,1,89,210,12,1,5),_RlOspfVirtNbrOptions_Type())
rlOspfVirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrOptions.setStatus(_A)
class _RlOspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('attempt',2),('init',3),('twoWay',4),(_AN,5),('exchange',6),('loading',7),('full',8)))
_RlOspfVirtNbrState_Type.__name__=_E
_RlOspfVirtNbrState_Object=MibTableColumn
rlOspfVirtNbrState=_RlOspfVirtNbrState_Object((1,3,6,1,4,1,89,210,12,1,6),_RlOspfVirtNbrState_Type())
rlOspfVirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrState.setStatus(_A)
_RlOspfVirtNbrEvents_Type=Counter32
_RlOspfVirtNbrEvents_Object=MibTableColumn
rlOspfVirtNbrEvents=_RlOspfVirtNbrEvents_Object((1,3,6,1,4,1,89,210,12,1,7),_RlOspfVirtNbrEvents_Type())
rlOspfVirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrEvents.setStatus(_A)
_RlOspfVirtNbrLsRetransQLen_Type=Gauge32
_RlOspfVirtNbrLsRetransQLen_Object=MibTableColumn
rlOspfVirtNbrLsRetransQLen=_RlOspfVirtNbrLsRetransQLen_Object((1,3,6,1,4,1,89,210,12,1,8),_RlOspfVirtNbrLsRetransQLen_Type())
rlOspfVirtNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrLsRetransQLen.setStatus(_A)
_RlOspfVirtNbrHelloSuppressed_Type=TruthValue
_RlOspfVirtNbrHelloSuppressed_Object=MibTableColumn
rlOspfVirtNbrHelloSuppressed=_RlOspfVirtNbrHelloSuppressed_Object((1,3,6,1,4,1,89,210,12,1,9),_RlOspfVirtNbrHelloSuppressed_Type())
rlOspfVirtNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrHelloSuppressed.setStatus(_A)
class _RlOspfVirtNbrRestartHelperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_RlOspfVirtNbrRestartHelperStatus_Type.__name__=_E
_RlOspfVirtNbrRestartHelperStatus_Object=MibTableColumn
rlOspfVirtNbrRestartHelperStatus=_RlOspfVirtNbrRestartHelperStatus_Object((1,3,6,1,4,1,89,210,12,1,10),_RlOspfVirtNbrRestartHelperStatus_Type())
rlOspfVirtNbrRestartHelperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrRestartHelperStatus.setStatus(_A)
_RlOspfVirtNbrRestartHelperAge_Type=Unsigned32
_RlOspfVirtNbrRestartHelperAge_Object=MibTableColumn
rlOspfVirtNbrRestartHelperAge=_RlOspfVirtNbrRestartHelperAge_Object((1,3,6,1,4,1,89,210,12,1,11),_RlOspfVirtNbrRestartHelperAge_Type())
rlOspfVirtNbrRestartHelperAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrRestartHelperAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfVirtNbrRestartHelperAge.setUnits(_G)
class _RlOspfVirtNbrRestartHelperExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_RlOspfVirtNbrRestartHelperExitReason_Type.__name__=_E
_RlOspfVirtNbrRestartHelperExitReason_Object=MibTableColumn
rlOspfVirtNbrRestartHelperExitReason=_RlOspfVirtNbrRestartHelperExitReason_Object((1,3,6,1,4,1,89,210,12,1,12),_RlOspfVirtNbrRestartHelperExitReason_Type())
rlOspfVirtNbrRestartHelperExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrRestartHelperExitReason.setStatus(_A)
_RlOspfVirtNbrDeadTime_Type=PositiveInteger
_RlOspfVirtNbrDeadTime_Object=MibTableColumn
rlOspfVirtNbrDeadTime=_RlOspfVirtNbrDeadTime_Object((1,3,6,1,4,1,89,210,12,1,13),_RlOspfVirtNbrDeadTime_Type())
rlOspfVirtNbrDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtNbrDeadTime.setStatus(_A)
_RlOspfExtLsdbTable_Object=MibTable
rlOspfExtLsdbTable=_RlOspfExtLsdbTable_Object((1,3,6,1,4,1,89,210,13))
if mibBuilder.loadTexts:rlOspfExtLsdbTable.setStatus(_I)
_RlOspfExtLsdbEntry_Object=MibTableRow
rlOspfExtLsdbEntry=_RlOspfExtLsdbEntry_Object((1,3,6,1,4,1,89,210,13,1))
rlOspfExtLsdbEntry.setIndexNames((0,_C,_AR),(0,_C,_AS),(0,_C,_AT),(0,_C,_AU))
if mibBuilder.loadTexts:rlOspfExtLsdbEntry.setStatus(_I)
_RlOspfExtLsdbProcessId_Type=RlOspfProcessID
_RlOspfExtLsdbProcessId_Object=MibTableColumn
rlOspfExtLsdbProcessId=_RlOspfExtLsdbProcessId_Object((1,3,6,1,4,1,89,210,13,1,1),_RlOspfExtLsdbProcessId_Type())
rlOspfExtLsdbProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbProcessId.setStatus(_A)
class _RlOspfExtLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_y,5))
_RlOspfExtLsdbType_Type.__name__=_E
_RlOspfExtLsdbType_Object=MibTableColumn
rlOspfExtLsdbType=_RlOspfExtLsdbType_Object((1,3,6,1,4,1,89,210,13,1,2),_RlOspfExtLsdbType_Type())
rlOspfExtLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbType.setStatus(_I)
_RlOspfExtLsdbLsid_Type=IpAddress
_RlOspfExtLsdbLsid_Object=MibTableColumn
rlOspfExtLsdbLsid=_RlOspfExtLsdbLsid_Object((1,3,6,1,4,1,89,210,13,1,3),_RlOspfExtLsdbLsid_Type())
rlOspfExtLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbLsid.setStatus(_I)
_RlOspfExtLsdbRouterId_Type=RouterID
_RlOspfExtLsdbRouterId_Object=MibTableColumn
rlOspfExtLsdbRouterId=_RlOspfExtLsdbRouterId_Object((1,3,6,1,4,1,89,210,13,1,4),_RlOspfExtLsdbRouterId_Type())
rlOspfExtLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbRouterId.setStatus(_I)
_RlOspfExtLsdbSequence_Type=Integer32
_RlOspfExtLsdbSequence_Object=MibTableColumn
rlOspfExtLsdbSequence=_RlOspfExtLsdbSequence_Object((1,3,6,1,4,1,89,210,13,1,5),_RlOspfExtLsdbSequence_Type())
rlOspfExtLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbSequence.setStatus(_I)
_RlOspfExtLsdbAge_Type=Integer32
_RlOspfExtLsdbAge_Object=MibTableColumn
rlOspfExtLsdbAge=_RlOspfExtLsdbAge_Object((1,3,6,1,4,1,89,210,13,1,6),_RlOspfExtLsdbAge_Type())
rlOspfExtLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbAge.setStatus(_I)
if mibBuilder.loadTexts:rlOspfExtLsdbAge.setUnits(_G)
_RlOspfExtLsdbChecksum_Type=Integer32
_RlOspfExtLsdbChecksum_Object=MibTableColumn
rlOspfExtLsdbChecksum=_RlOspfExtLsdbChecksum_Object((1,3,6,1,4,1,89,210,13,1,7),_RlOspfExtLsdbChecksum_Type())
rlOspfExtLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbChecksum.setStatus(_I)
class _RlOspfExtLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_RlOspfExtLsdbAdvertisement_Type.__name__=_J
_RlOspfExtLsdbAdvertisement_Object=MibTableColumn
rlOspfExtLsdbAdvertisement=_RlOspfExtLsdbAdvertisement_Object((1,3,6,1,4,1,89,210,13,1,8),_RlOspfExtLsdbAdvertisement_Type())
rlOspfExtLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfExtLsdbAdvertisement.setStatus(_I)
_RlOspfAreaAggregateTable_Object=MibTable
rlOspfAreaAggregateTable=_RlOspfAreaAggregateTable_Object((1,3,6,1,4,1,89,210,14))
if mibBuilder.loadTexts:rlOspfAreaAggregateTable.setStatus(_A)
_RlOspfAreaAggregateEntry_Object=MibTableRow
rlOspfAreaAggregateEntry=_RlOspfAreaAggregateEntry_Object((1,3,6,1,4,1,89,210,14,1))
rlOspfAreaAggregateEntry.setIndexNames((0,_C,_AV),(0,_C,_AW),(0,_C,_AX),(0,_C,_AY),(0,_C,_AZ))
if mibBuilder.loadTexts:rlOspfAreaAggregateEntry.setStatus(_A)
_RlOspfAreaAggregateProcessId_Type=RlOspfProcessID
_RlOspfAreaAggregateProcessId_Object=MibTableColumn
rlOspfAreaAggregateProcessId=_RlOspfAreaAggregateProcessId_Object((1,3,6,1,4,1,89,210,14,1,1),_RlOspfAreaAggregateProcessId_Type())
rlOspfAreaAggregateProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaAggregateProcessId.setStatus(_A)
_RlOspfAreaAggregateAreaID_Type=AreaID
_RlOspfAreaAggregateAreaID_Object=MibTableColumn
rlOspfAreaAggregateAreaID=_RlOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,89,210,14,1,2),_RlOspfAreaAggregateAreaID_Type())
rlOspfAreaAggregateAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaAggregateAreaID.setStatus(_A)
class _RlOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*((_x,3),(_z,7)))
_RlOspfAreaAggregateLsdbType_Type.__name__=_E
_RlOspfAreaAggregateLsdbType_Object=MibTableColumn
rlOspfAreaAggregateLsdbType=_RlOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,89,210,14,1,3),_RlOspfAreaAggregateLsdbType_Type())
rlOspfAreaAggregateLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaAggregateLsdbType.setStatus(_A)
_RlOspfAreaAggregateNet_Type=IpAddress
_RlOspfAreaAggregateNet_Object=MibTableColumn
rlOspfAreaAggregateNet=_RlOspfAreaAggregateNet_Object((1,3,6,1,4,1,89,210,14,1,4),_RlOspfAreaAggregateNet_Type())
rlOspfAreaAggregateNet.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaAggregateNet.setStatus(_A)
_RlOspfAreaAggregateMask_Type=IpAddress
_RlOspfAreaAggregateMask_Object=MibTableColumn
rlOspfAreaAggregateMask=_RlOspfAreaAggregateMask_Object((1,3,6,1,4,1,89,210,14,1,5),_RlOspfAreaAggregateMask_Type())
rlOspfAreaAggregateMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfAreaAggregateMask.setStatus(_A)
_RlOspfAreaAggregateStatus_Type=RowStatus
_RlOspfAreaAggregateStatus_Object=MibTableColumn
rlOspfAreaAggregateStatus=_RlOspfAreaAggregateStatus_Object((1,3,6,1,4,1,89,210,14,1,6),_RlOspfAreaAggregateStatus_Type())
rlOspfAreaAggregateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaAggregateStatus.setStatus(_A)
class _RlOspfAreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A3,1),(_A4,2)))
_RlOspfAreaAggregateEffect_Type.__name__=_E
_RlOspfAreaAggregateEffect_Object=MibTableColumn
rlOspfAreaAggregateEffect=_RlOspfAreaAggregateEffect_Object((1,3,6,1,4,1,89,210,14,1,7),_RlOspfAreaAggregateEffect_Type())
rlOspfAreaAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaAggregateEffect.setStatus(_A)
class _RlOspfAreaAggregateExtRouteTag_Type(Unsigned32):defaultValue=0
_RlOspfAreaAggregateExtRouteTag_Type.__name__=_R
_RlOspfAreaAggregateExtRouteTag_Object=MibTableColumn
rlOspfAreaAggregateExtRouteTag=_RlOspfAreaAggregateExtRouteTag_Object((1,3,6,1,4,1,89,210,14,1,8),_RlOspfAreaAggregateExtRouteTag_Type())
rlOspfAreaAggregateExtRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:rlOspfAreaAggregateExtRouteTag.setStatus(_A)
_RlOspfLocalLsdbTable_Object=MibTable
rlOspfLocalLsdbTable=_RlOspfLocalLsdbTable_Object((1,3,6,1,4,1,89,210,18))
if mibBuilder.loadTexts:rlOspfLocalLsdbTable.setStatus(_A)
_RlOspfLocalLsdbEntry_Object=MibTableRow
rlOspfLocalLsdbEntry=_RlOspfLocalLsdbEntry_Object((1,3,6,1,4,1,89,210,18,1))
rlOspfLocalLsdbEntry.setIndexNames((0,_C,_Aa),(0,_C,_Ab),(0,_C,_Ac),(0,_C,_Ad),(0,_C,_Ae),(0,_C,_Af))
if mibBuilder.loadTexts:rlOspfLocalLsdbEntry.setStatus(_A)
_RlOspfLocalLsdbProcessId_Type=Unsigned32
_RlOspfLocalLsdbProcessId_Object=MibTableColumn
rlOspfLocalLsdbProcessId=_RlOspfLocalLsdbProcessId_Object((1,3,6,1,4,1,89,210,18,1,1),_RlOspfLocalLsdbProcessId_Type())
rlOspfLocalLsdbProcessId.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfLocalLsdbProcessId.setStatus(_A)
_RlOspfLocalLsdbIpAddress_Type=IpAddress
_RlOspfLocalLsdbIpAddress_Object=MibTableColumn
rlOspfLocalLsdbIpAddress=_RlOspfLocalLsdbIpAddress_Object((1,3,6,1,4,1,89,210,18,1,2),_RlOspfLocalLsdbIpAddress_Type())
rlOspfLocalLsdbIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfLocalLsdbIpAddress.setStatus(_A)
_RlOspfLocalLsdbAddressLessIf_Type=InterfaceIndexOrZero
_RlOspfLocalLsdbAddressLessIf_Object=MibTableColumn
rlOspfLocalLsdbAddressLessIf=_RlOspfLocalLsdbAddressLessIf_Object((1,3,6,1,4,1,89,210,18,1,3),_RlOspfLocalLsdbAddressLessIf_Type())
rlOspfLocalLsdbAddressLessIf.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfLocalLsdbAddressLessIf.setStatus(_A)
class _RlOspfLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues((_Ag,9))
_RlOspfLocalLsdbType_Type.__name__=_E
_RlOspfLocalLsdbType_Object=MibTableColumn
rlOspfLocalLsdbType=_RlOspfLocalLsdbType_Object((1,3,6,1,4,1,89,210,18,1,4),_RlOspfLocalLsdbType_Type())
rlOspfLocalLsdbType.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfLocalLsdbType.setStatus(_A)
_RlOspfLocalLsdbLsid_Type=IpAddress
_RlOspfLocalLsdbLsid_Object=MibTableColumn
rlOspfLocalLsdbLsid=_RlOspfLocalLsdbLsid_Object((1,3,6,1,4,1,89,210,18,1,5),_RlOspfLocalLsdbLsid_Type())
rlOspfLocalLsdbLsid.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfLocalLsdbLsid.setStatus(_A)
_RlOspfLocalLsdbRouterId_Type=RouterID
_RlOspfLocalLsdbRouterId_Object=MibTableColumn
rlOspfLocalLsdbRouterId=_RlOspfLocalLsdbRouterId_Object((1,3,6,1,4,1,89,210,18,1,6),_RlOspfLocalLsdbRouterId_Type())
rlOspfLocalLsdbRouterId.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfLocalLsdbRouterId.setStatus(_A)
_RlOspfLocalLsdbSequence_Type=Integer32
_RlOspfLocalLsdbSequence_Object=MibTableColumn
rlOspfLocalLsdbSequence=_RlOspfLocalLsdbSequence_Object((1,3,6,1,4,1,89,210,18,1,7),_RlOspfLocalLsdbSequence_Type())
rlOspfLocalLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLocalLsdbSequence.setStatus(_A)
_RlOspfLocalLsdbAge_Type=Integer32
_RlOspfLocalLsdbAge_Object=MibTableColumn
rlOspfLocalLsdbAge=_RlOspfLocalLsdbAge_Object((1,3,6,1,4,1,89,210,18,1,8),_RlOspfLocalLsdbAge_Type())
rlOspfLocalLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLocalLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfLocalLsdbAge.setUnits(_G)
_RlOspfLocalLsdbChecksum_Type=Integer32
_RlOspfLocalLsdbChecksum_Object=MibTableColumn
rlOspfLocalLsdbChecksum=_RlOspfLocalLsdbChecksum_Object((1,3,6,1,4,1,89,210,18,1,9),_RlOspfLocalLsdbChecksum_Type())
rlOspfLocalLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLocalLsdbChecksum.setStatus(_A)
class _RlOspfLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfLocalLsdbAdvertisement_Type.__name__=_J
_RlOspfLocalLsdbAdvertisement_Object=MibTableColumn
rlOspfLocalLsdbAdvertisement=_RlOspfLocalLsdbAdvertisement_Object((1,3,6,1,4,1,89,210,18,1,10),_RlOspfLocalLsdbAdvertisement_Type())
rlOspfLocalLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLocalLsdbAdvertisement.setStatus(_A)
_RlOspfLocalLsdbAreaId_Type=AreaID
_RlOspfLocalLsdbAreaId_Object=MibTableColumn
rlOspfLocalLsdbAreaId=_RlOspfLocalLsdbAreaId_Object((1,3,6,1,4,1,89,210,18,1,11),_RlOspfLocalLsdbAreaId_Type())
rlOspfLocalLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfLocalLsdbAreaId.setStatus(_A)
_RlOspfVirtLocalLsdbTable_Object=MibTable
rlOspfVirtLocalLsdbTable=_RlOspfVirtLocalLsdbTable_Object((1,3,6,1,4,1,89,210,19))
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbTable.setStatus(_A)
_RlOspfVirtLocalLsdbEntry_Object=MibTableRow
rlOspfVirtLocalLsdbEntry=_RlOspfVirtLocalLsdbEntry_Object((1,3,6,1,4,1,89,210,19,1))
rlOspfVirtLocalLsdbEntry.setIndexNames((0,_C,_Ah),(0,_C,_Ai),(0,_C,_Aj),(0,_C,_Ak),(0,_C,_Al),(0,_C,_Am))
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbEntry.setStatus(_A)
_RlOspfVirtLocalLsdbProcessId_Type=Unsigned32
_RlOspfVirtLocalLsdbProcessId_Object=MibTableColumn
rlOspfVirtLocalLsdbProcessId=_RlOspfVirtLocalLsdbProcessId_Object((1,3,6,1,4,1,89,210,19,1,1),_RlOspfVirtLocalLsdbProcessId_Type())
rlOspfVirtLocalLsdbProcessId.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbProcessId.setStatus(_A)
_RlOspfVirtLocalLsdbTransitArea_Type=AreaID
_RlOspfVirtLocalLsdbTransitArea_Object=MibTableColumn
rlOspfVirtLocalLsdbTransitArea=_RlOspfVirtLocalLsdbTransitArea_Object((1,3,6,1,4,1,89,210,19,1,2),_RlOspfVirtLocalLsdbTransitArea_Type())
rlOspfVirtLocalLsdbTransitArea.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbTransitArea.setStatus(_A)
_RlOspfVirtLocalLsdbNeighbor_Type=RouterID
_RlOspfVirtLocalLsdbNeighbor_Object=MibTableColumn
rlOspfVirtLocalLsdbNeighbor=_RlOspfVirtLocalLsdbNeighbor_Object((1,3,6,1,4,1,89,210,19,1,3),_RlOspfVirtLocalLsdbNeighbor_Type())
rlOspfVirtLocalLsdbNeighbor.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbNeighbor.setStatus(_A)
class _RlOspfVirtLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues((_Ag,9))
_RlOspfVirtLocalLsdbType_Type.__name__=_E
_RlOspfVirtLocalLsdbType_Object=MibTableColumn
rlOspfVirtLocalLsdbType=_RlOspfVirtLocalLsdbType_Object((1,3,6,1,4,1,89,210,19,1,4),_RlOspfVirtLocalLsdbType_Type())
rlOspfVirtLocalLsdbType.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbType.setStatus(_A)
_RlOspfVirtLocalLsdbLsid_Type=IpAddress
_RlOspfVirtLocalLsdbLsid_Object=MibTableColumn
rlOspfVirtLocalLsdbLsid=_RlOspfVirtLocalLsdbLsid_Object((1,3,6,1,4,1,89,210,19,1,5),_RlOspfVirtLocalLsdbLsid_Type())
rlOspfVirtLocalLsdbLsid.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbLsid.setStatus(_A)
_RlOspfVirtLocalLsdbRouterId_Type=RouterID
_RlOspfVirtLocalLsdbRouterId_Object=MibTableColumn
rlOspfVirtLocalLsdbRouterId=_RlOspfVirtLocalLsdbRouterId_Object((1,3,6,1,4,1,89,210,19,1,6),_RlOspfVirtLocalLsdbRouterId_Type())
rlOspfVirtLocalLsdbRouterId.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbRouterId.setStatus(_A)
_RlOspfVirtLocalLsdbSequence_Type=Integer32
_RlOspfVirtLocalLsdbSequence_Object=MibTableColumn
rlOspfVirtLocalLsdbSequence=_RlOspfVirtLocalLsdbSequence_Object((1,3,6,1,4,1,89,210,19,1,7),_RlOspfVirtLocalLsdbSequence_Type())
rlOspfVirtLocalLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbSequence.setStatus(_A)
_RlOspfVirtLocalLsdbAge_Type=Integer32
_RlOspfVirtLocalLsdbAge_Object=MibTableColumn
rlOspfVirtLocalLsdbAge=_RlOspfVirtLocalLsdbAge_Object((1,3,6,1,4,1,89,210,19,1,8),_RlOspfVirtLocalLsdbAge_Type())
rlOspfVirtLocalLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbAge.setUnits(_G)
_RlOspfVirtLocalLsdbChecksum_Type=Integer32
_RlOspfVirtLocalLsdbChecksum_Object=MibTableColumn
rlOspfVirtLocalLsdbChecksum=_RlOspfVirtLocalLsdbChecksum_Object((1,3,6,1,4,1,89,210,19,1,9),_RlOspfVirtLocalLsdbChecksum_Type())
rlOspfVirtLocalLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbChecksum.setStatus(_A)
class _RlOspfVirtLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RlOspfVirtLocalLsdbAdvertisement_Type.__name__=_J
_RlOspfVirtLocalLsdbAdvertisement_Object=MibTableColumn
rlOspfVirtLocalLsdbAdvertisement=_RlOspfVirtLocalLsdbAdvertisement_Object((1,3,6,1,4,1,89,210,19,1,10),_RlOspfVirtLocalLsdbAdvertisement_Type())
rlOspfVirtLocalLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfVirtLocalLsdbAdvertisement.setStatus(_A)
_RlOspfEnableTrapsOspfErrors_Type=Integer32
_RlOspfEnableTrapsOspfErrors_Object=MibScalar
rlOspfEnableTrapsOspfErrors=_RlOspfEnableTrapsOspfErrors_Object((1,3,6,1,4,1,89,210,20),_RlOspfEnableTrapsOspfErrors_Type())
rlOspfEnableTrapsOspfErrors.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfEnableTrapsOspfErrors.setStatus(_A)
_RlOspfEnableTrapsOspfLsa_Type=Integer32
_RlOspfEnableTrapsOspfLsa_Object=MibScalar
rlOspfEnableTrapsOspfLsa=_RlOspfEnableTrapsOspfLsa_Object((1,3,6,1,4,1,89,210,21),_RlOspfEnableTrapsOspfLsa_Type())
rlOspfEnableTrapsOspfLsa.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfEnableTrapsOspfLsa.setStatus(_A)
class _RlOspfEnableTrapsOspfRateLimitSeconds_Type(Integer32):defaultValue=10
_RlOspfEnableTrapsOspfRateLimitSeconds_Type.__name__=_E
_RlOspfEnableTrapsOspfRateLimitSeconds_Object=MibScalar
rlOspfEnableTrapsOspfRateLimitSeconds=_RlOspfEnableTrapsOspfRateLimitSeconds_Object((1,3,6,1,4,1,89,210,22),_RlOspfEnableTrapsOspfRateLimitSeconds_Type())
rlOspfEnableTrapsOspfRateLimitSeconds.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfEnableTrapsOspfRateLimitSeconds.setStatus(_A)
class _RlOspfEnableTrapsOspfRateLimitTrapNumber_Type(Integer32):defaultValue=7
_RlOspfEnableTrapsOspfRateLimitTrapNumber_Type.__name__=_E
_RlOspfEnableTrapsOspfRateLimitTrapNumber_Object=MibScalar
rlOspfEnableTrapsOspfRateLimitTrapNumber=_RlOspfEnableTrapsOspfRateLimitTrapNumber_Object((1,3,6,1,4,1,89,210,23),_RlOspfEnableTrapsOspfRateLimitTrapNumber_Type())
rlOspfEnableTrapsOspfRateLimitTrapNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfEnableTrapsOspfRateLimitTrapNumber.setStatus(_A)
_RlOspfEnableTrapsOspfTransmit_Type=Integer32
_RlOspfEnableTrapsOspfTransmit_Object=MibScalar
rlOspfEnableTrapsOspfTransmit=_RlOspfEnableTrapsOspfTransmit_Object((1,3,6,1,4,1,89,210,24),_RlOspfEnableTrapsOspfTransmit_Type())
rlOspfEnableTrapsOspfTransmit.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfEnableTrapsOspfTransmit.setStatus(_A)
_RlOspfEnableTrapsOspfStateChange_Type=Integer32
_RlOspfEnableTrapsOspfStateChange_Object=MibScalar
rlOspfEnableTrapsOspfStateChange=_RlOspfEnableTrapsOspfStateChange_Object((1,3,6,1,4,1,89,210,25),_RlOspfEnableTrapsOspfStateChange_Type())
rlOspfEnableTrapsOspfStateChange.setMaxAccess(_F)
if mibBuilder.loadTexts:rlOspfEnableTrapsOspfStateChange.setStatus(_A)
_RlOspfExt_ObjectIdentity=ObjectIdentity
rlOspfExt=_RlOspfExt_ObjectIdentity((1,3,6,1,4,1,89,210,26))
_RlOspfBrRouterTable_Object=MibTable
rlOspfBrRouterTable=_RlOspfBrRouterTable_Object((1,3,6,1,4,1,89,210,26,1))
if mibBuilder.loadTexts:rlOspfBrRouterTable.setStatus(_A)
_RlOspfBrRouterEntry_Object=MibTableRow
rlOspfBrRouterEntry=_RlOspfBrRouterEntry_Object((1,3,6,1,4,1,89,210,26,1,1))
rlOspfBrRouterEntry.setIndexNames((0,_C,_An),(0,_C,_Ao),(0,_C,_Ap),(0,_C,_Aq),(0,_C,_Ar))
if mibBuilder.loadTexts:rlOspfBrRouterEntry.setStatus(_A)
_RlOspfBrRouterProcessId_Type=RlOspfProcessID
_RlOspfBrRouterProcessId_Object=MibTableColumn
rlOspfBrRouterProcessId=_RlOspfBrRouterProcessId_Object((1,3,6,1,4,1,89,210,26,1,1,1),_RlOspfBrRouterProcessId_Type())
rlOspfBrRouterProcessId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterProcessId.setStatus(_A)
_RlOspfBrRouterAreaId_Type=AreaID
_RlOspfBrRouterAreaId_Object=MibTableColumn
rlOspfBrRouterAreaId=_RlOspfBrRouterAreaId_Object((1,3,6,1,4,1,89,210,26,1,1,2),_RlOspfBrRouterAreaId_Type())
rlOspfBrRouterAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterAreaId.setStatus(_A)
_RlOspfBrRouterRouterId_Type=RouterID
_RlOspfBrRouterRouterId_Object=MibTableColumn
rlOspfBrRouterRouterId=_RlOspfBrRouterRouterId_Object((1,3,6,1,4,1,89,210,26,1,1,3),_RlOspfBrRouterRouterId_Type())
rlOspfBrRouterRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterRouterId.setStatus(_A)
_RlOspfBrRouterNextHopIp_Type=IpAddress
_RlOspfBrRouterNextHopIp_Object=MibTableColumn
rlOspfBrRouterNextHopIp=_RlOspfBrRouterNextHopIp_Object((1,3,6,1,4,1,89,210,26,1,1,4),_RlOspfBrRouterNextHopIp_Type())
rlOspfBrRouterNextHopIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterNextHopIp.setStatus(_A)
_RlOspfBrRouterOutIf_Type=InterfaceIndexOrZero
_RlOspfBrRouterOutIf_Object=MibTableColumn
rlOspfBrRouterOutIf=_RlOspfBrRouterOutIf_Object((1,3,6,1,4,1,89,210,26,1,1,5),_RlOspfBrRouterOutIf_Type())
rlOspfBrRouterOutIf.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterOutIf.setStatus(_A)
class _RlOspfBrRouterRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('intra',1),('inter',2)))
_RlOspfBrRouterRouteType_Type.__name__=_E
_RlOspfBrRouterRouteType_Object=MibTableColumn
rlOspfBrRouterRouteType=_RlOspfBrRouterRouteType_Object((1,3,6,1,4,1,89,210,26,1,1,6),_RlOspfBrRouterRouteType_Type())
rlOspfBrRouterRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterRouteType.setStatus(_A)
_RlOspfBrRouterRouteCost_Type=Unsigned32
_RlOspfBrRouterRouteCost_Object=MibTableColumn
rlOspfBrRouterRouteCost=_RlOspfBrRouterRouteCost_Object((1,3,6,1,4,1,89,210,26,1,1,7),_RlOspfBrRouterRouteCost_Type())
rlOspfBrRouterRouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterRouteCost.setStatus(_A)
class _RlOspfBrRouterRouterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abr',1),('asbr',2),('both',3)))
_RlOspfBrRouterRouterType_Type.__name__=_E
_RlOspfBrRouterRouterType_Object=MibTableColumn
rlOspfBrRouterRouterType=_RlOspfBrRouterRouterType_Object((1,3,6,1,4,1,89,210,26,1,1,8),_RlOspfBrRouterRouterType_Type())
rlOspfBrRouterRouterType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOspfBrRouterRouterType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlOspfProcessID':RlOspfProcessID,_AC:RlOspfFastHelloMultiplierRange,'RlOspfRestartHelperStatus':RlOspfRestartHelperStatus,'RlOspfRestartExitReason':RlOspfRestartExitReason,'RlOspfRouterIdType':RlOspfRouterIdType,_a:RlOspfAuthenticationType,_O:RlOspfUpToRefreshIntervalTC,_j:RlOspfDeadIntervalRangeTC,'rlOspf':rlOspf,'rlOspfInstance':rlOspfInstance,'rlOspfGeneralGroupTable':rlOspfGeneralGroupTable,'rlOspfGeneralGroupEntry':rlOspfGeneralGroupEntry,_m:rlOspfProcessId,'rlOspfRouterId':rlOspfRouterId,'rlOspfAdminStat':rlOspfAdminStat,'rlOspfVersionNumber':rlOspfVersionNumber,'rlOspfAreaBdrRtrStatus':rlOspfAreaBdrRtrStatus,'rlOspfASBdrRtrStatus':rlOspfASBdrRtrStatus,'rlOspfExternLsaCount':rlOspfExternLsaCount,'rlOspfExternLsaCksumSum':rlOspfExternLsaCksumSum,'rlOspfTOSSupport':rlOspfTOSSupport,'rlOspfOriginateNewLsas':rlOspfOriginateNewLsas,'rlOspfRxNewLsas':rlOspfRxNewLsas,'rlOspfExtLsdbLimit':rlOspfExtLsdbLimit,'rlOspfMulticastExtensions':rlOspfMulticastExtensions,'rlOspfExitOverflowInterval':rlOspfExitOverflowInterval,'rlOspfDemandExtensions':rlOspfDemandExtensions,'rlOspfRFC1583Compatibility':rlOspfRFC1583Compatibility,'rlOspfOpaqueLsaSupport':rlOspfOpaqueLsaSupport,'rlOspfReferenceBandwidth':rlOspfReferenceBandwidth,'rlOspfRestartSupport':rlOspfRestartSupport,'rlOspfRestartInterval':rlOspfRestartInterval,'rlOspfRestartStrictLsaChecking':rlOspfRestartStrictLsaChecking,'rlOspfRestartStatus':rlOspfRestartStatus,'rlOspfRestartAge':rlOspfRestartAge,'rlOspfRestartExitReason':rlOspfRestartExitReason,'rlOspfAsLsaCount':rlOspfAsLsaCount,'rlOspfAsLsaCksumSum':rlOspfAsLsaCksumSum,'rlOspfStubRouterSupport':rlOspfStubRouterSupport,'rlOspfStubRouterAdvertisement':rlOspfStubRouterAdvertisement,'rlOspfDiscontinuityTime':rlOspfDiscontinuityTime,'rlOspfGeneralGroupStatus':rlOspfGeneralGroupStatus,'rlOspfLogAdjacencyChanges':rlOspfLogAdjacencyChanges,'rlOspfPassiveInterface':rlOspfPassiveInterface,'rlOspfDefaultMetric':rlOspfDefaultMetric,'rlOspfMaximumRedistPrefixNum':rlOspfMaximumRedistPrefixNum,'rlOspfMaximumRedistPrefixThreshold':rlOspfMaximumRedistPrefixThreshold,'rlOspfMaximumRedistPrefixWarningOnly':rlOspfMaximumRedistPrefixWarningOnly,'rlOspfOperStatus':rlOspfOperStatus,'rlOspfNextRouterId':rlOspfNextRouterId,'rlOspfRouterIdType':rlOspfRouterIdType,'rlOspfNextRouterIdType':rlOspfNextRouterIdType,'rlOspfASBdrRtrActualStatus':rlOspfASBdrRtrActualStatus,'rlOspfCalcMaxDelay':rlOspfCalcMaxDelay,'rlOspfRteMaxEqCostPaths':rlOspfRteMaxEqCostPaths,'rlOspfAreaTable':rlOspfAreaTable,'rlOspfAreaEntry':rlOspfAreaEntry,_n:rlOspfAreaProcessId,_o:rlOspfAreaId,'rlOspfAuthType':rlOspfAuthType,'rlOspfImportAsExtern':rlOspfImportAsExtern,'rlOspfSpfRuns':rlOspfSpfRuns,'rlOspfAreaBdrRtrCount':rlOspfAreaBdrRtrCount,'rlOspfAsBdrRtrCount':rlOspfAsBdrRtrCount,'rlOspfAreaLsaCount':rlOspfAreaLsaCount,'rlOspfAreaLsaCksumSum':rlOspfAreaLsaCksumSum,'rlOspfAreaSummary':rlOspfAreaSummary,'rlOspfAreaStatus':rlOspfAreaStatus,'rlOspfAreaNssaTranslatorRole':rlOspfAreaNssaTranslatorRole,'rlOspfAreaNssaTranslatorState':rlOspfAreaNssaTranslatorState,'rlOspfAreaNssaTranslatorStabilityInterval':rlOspfAreaNssaTranslatorStabilityInterval,'rlOspfAreaNssaTranslatorEvents':rlOspfAreaNssaTranslatorEvents,'rlOspfAreaAdminStat':rlOspfAreaAdminStat,'rlOspfAreaOperStatus':rlOspfAreaOperStatus,'rlOspfAreaFilterPrefixListIn':rlOspfAreaFilterPrefixListIn,'rlOspfAreaFilterPrefixListOut':rlOspfAreaFilterPrefixListOut,'rlOspfStubAreaTable':rlOspfStubAreaTable,'rlOspfStubAreaEntry':rlOspfStubAreaEntry,_p:rlOspfStubProcessId,_q:rlOspfStubAreaId,_r:rlOspfStubTOS,'rlOspfStubMetric':rlOspfStubMetric,'rlOspfStubStatus':rlOspfStubStatus,'rlOspfStubMetricType':rlOspfStubMetricType,'rlOspfLsdbTable':rlOspfLsdbTable,'rlOspfLsdbEntry':rlOspfLsdbEntry,_s:rlOspfLsdbProcessId,_t:rlOspfLsdbAreaId,_u:rlOspfLsdbType,_v:rlOspfLsdbLsid,_w:rlOspfLsdbRouterId,'rlOspfLsdbSequence':rlOspfLsdbSequence,'rlOspfLsdbAge':rlOspfLsdbAge,'rlOspfLsdbChecksum':rlOspfLsdbChecksum,'rlOspfLsdbAdvertisement':rlOspfLsdbAdvertisement,'rlOspfAreaRangeTable':rlOspfAreaRangeTable,'rlOspfAreaRangeEntry':rlOspfAreaRangeEntry,_A0:rlOspfAreaRangeProcessId,_A1:rlOspfAreaRangeAreaId,_A2:rlOspfAreaRangeNet,'rlOspfAreaRangeMask':rlOspfAreaRangeMask,'rlOspfAreaRangeStatus':rlOspfAreaRangeStatus,'rlOspfAreaRangeEffect':rlOspfAreaRangeEffect,'rlOspfHostTable':rlOspfHostTable,'rlOspfHostEntry':rlOspfHostEntry,_A5:rlOspfHostProcessId,_A6:rlOspfHostIpAddress,_A7:rlOspfHostTOS,'rlOspfHostMetric':rlOspfHostMetric,'rlOspfHostStatus':rlOspfHostStatus,'rlOspfHostAreaID':rlOspfHostAreaID,'rlOspfHostCfgAreaID':rlOspfHostCfgAreaID,'rlOspfIfTable':rlOspfIfTable,'rlOspfIfEntry':rlOspfIfEntry,_A8:rlOspfIfProcessId,_A9:rlOspfIfIpAddress,_AA:rlOspfAddressLessIf,'rlOspfIfAreaId':rlOspfIfAreaId,'rlOspfIfType':rlOspfIfType,'rlOspfIfAdminStat':rlOspfIfAdminStat,'rlOspfIfRtrPriority':rlOspfIfRtrPriority,'rlOspfIfTransitDelay':rlOspfIfTransitDelay,'rlOspfIfRetransInterval':rlOspfIfRetransInterval,'rlOspfIfHelloInterval':rlOspfIfHelloInterval,'rlOspfIfRtrDeadInterval':rlOspfIfRtrDeadInterval,'rlOspfIfPollInterval':rlOspfIfPollInterval,'rlOspfIfState':rlOspfIfState,'rlOspfIfDesignatedRouter':rlOspfIfDesignatedRouter,'rlOspfIfBackupDesignatedRouter':rlOspfIfBackupDesignatedRouter,'rlOspfIfEvents':rlOspfIfEvents,'rlOspfIfAuthKey':rlOspfIfAuthKey,'rlOspfIfStatus':rlOspfIfStatus,'rlOspfIfMulticastForwarding':rlOspfIfMulticastForwarding,'rlOspfIfDemand':rlOspfIfDemand,'rlOspfIfAuthType':rlOspfIfAuthType,'rlOspfIfLsaCount':rlOspfIfLsaCount,'rlOspfIfLsaCksumSum':rlOspfIfLsaCksumSum,'rlOspfIfDesignatedRouterId':rlOspfIfDesignatedRouterId,'rlOspfIfBackupDesignatedRouterId':rlOspfIfBackupDesignatedRouterId,'rlOspfIfOperStatus':rlOspfIfOperStatus,'rlOspfIfAuthKeyChain':rlOspfIfAuthKeyChain,'rlOspfIfPassive':rlOspfIfPassive,'rlOspfIfLsaRefreshIntvl':rlOspfIfLsaRefreshIntvl,'rlOspfIfFastHelloMultiplier':rlOspfIfFastHelloMultiplier,'rlOspfIfMtuIgnore':rlOspfIfMtuIgnore,'rlOspfIfNameLookup':rlOspfIfNameLookup,'rlOspfIfIfIndex':rlOspfIfIfIndex,'rlOspfIfActualAuthType':rlOspfIfActualAuthType,'rlOspfIfMetricTable':rlOspfIfMetricTable,'rlOspfIfMetricEntry':rlOspfIfMetricEntry,_AD:rlOspfIfMetricProcessId,_AE:rlOspfIfMetricIpAddress,_AF:rlOspfIfMetricAddressLessIf,_AG:rlOspfIfMetricTOS,'rlOspfIfMetricValue':rlOspfIfMetricValue,'rlOspfIfMetricStatus':rlOspfIfMetricStatus,'rlOspfVirtIfTable':rlOspfVirtIfTable,'rlOspfVirtIfEntry':rlOspfVirtIfEntry,_AH:rlOspfVirtIfProcessId,_AI:rlOspfVirtIfAreaId,_AJ:rlOspfVirtIfNeighbor,'rlOspfVirtIfTransitDelay':rlOspfVirtIfTransitDelay,'rlOspfVirtIfRetransInterval':rlOspfVirtIfRetransInterval,'rlOspfVirtIfHelloInterval':rlOspfVirtIfHelloInterval,'rlOspfVirtIfRtrDeadInterval':rlOspfVirtIfRtrDeadInterval,'rlOspfVirtIfState':rlOspfVirtIfState,'rlOspfVirtIfEvents':rlOspfVirtIfEvents,'rlOspfVirtIfAuthKey':rlOspfVirtIfAuthKey,'rlOspfVirtIfStatus':rlOspfVirtIfStatus,'rlOspfVirtIfAuthType':rlOspfVirtIfAuthType,'rlOspfVirtIfLsaCount':rlOspfVirtIfLsaCount,'rlOspfVirtIfLsaCksumSum':rlOspfVirtIfLsaCksumSum,'rlOspfVirtIfAuthKeyChain':rlOspfVirtIfAuthKeyChain,'rlOspfVirtIfAdminStatus':rlOspfVirtIfAdminStatus,'rlOspfVirtIfOperStatus':rlOspfVirtIfOperStatus,'rlOspfVirtIfIndex':rlOspfVirtIfIndex,'rlOspfVirtIfActualAuthType':rlOspfVirtIfActualAuthType,'rlOspfNbrTable':rlOspfNbrTable,'rlOspfNbrEntry':rlOspfNbrEntry,_AK:rlOspfNbrProcessId,_AL:rlOspfNbrIpAddr,_AM:rlOspfNbrAddressLessIndex,'rlOspfNbrRtrId':rlOspfNbrRtrId,'rlOspfNbrOptions':rlOspfNbrOptions,'rlOspfNbrPriority':rlOspfNbrPriority,'rlOspfNbrState':rlOspfNbrState,'rlOspfNbrEvents':rlOspfNbrEvents,'rlOspfNbrLsRetransQLen':rlOspfNbrLsRetransQLen,'rlOspfNbmaNbrStatus':rlOspfNbmaNbrStatus,'rlOspfNbmaNbrPermanence':rlOspfNbmaNbrPermanence,'rlOspfNbrHelloSuppressed':rlOspfNbrHelloSuppressed,'rlOspfNbrRestartHelperStatus':rlOspfNbrRestartHelperStatus,'rlOspfNbrRestartHelperAge':rlOspfNbrRestartHelperAge,'rlOspfNbrRestartHelperExitReason':rlOspfNbrRestartHelperExitReason,'rlOspfNbrDeadTime':rlOspfNbrDeadTime,'rlOspfNbrAreaId':rlOspfNbrAreaId,'rlOspfNbrIfIndex':rlOspfNbrIfIndex,'rlOspfNbrIfIpAddr':rlOspfNbrIfIpAddr,'rlOspfVirtNbrTable':rlOspfVirtNbrTable,'rlOspfVirtNbrEntry':rlOspfVirtNbrEntry,_AO:rlOspfVirtNbrProcessId,_AP:rlOspfVirtNbrArea,_AQ:rlOspfVirtNbrRtrId,'rlOspfVirtNbrIpAddr':rlOspfVirtNbrIpAddr,'rlOspfVirtNbrOptions':rlOspfVirtNbrOptions,'rlOspfVirtNbrState':rlOspfVirtNbrState,'rlOspfVirtNbrEvents':rlOspfVirtNbrEvents,'rlOspfVirtNbrLsRetransQLen':rlOspfVirtNbrLsRetransQLen,'rlOspfVirtNbrHelloSuppressed':rlOspfVirtNbrHelloSuppressed,'rlOspfVirtNbrRestartHelperStatus':rlOspfVirtNbrRestartHelperStatus,'rlOspfVirtNbrRestartHelperAge':rlOspfVirtNbrRestartHelperAge,'rlOspfVirtNbrRestartHelperExitReason':rlOspfVirtNbrRestartHelperExitReason,'rlOspfVirtNbrDeadTime':rlOspfVirtNbrDeadTime,'rlOspfExtLsdbTable':rlOspfExtLsdbTable,'rlOspfExtLsdbEntry':rlOspfExtLsdbEntry,_AR:rlOspfExtLsdbProcessId,_AS:rlOspfExtLsdbType,_AT:rlOspfExtLsdbLsid,_AU:rlOspfExtLsdbRouterId,'rlOspfExtLsdbSequence':rlOspfExtLsdbSequence,'rlOspfExtLsdbAge':rlOspfExtLsdbAge,'rlOspfExtLsdbChecksum':rlOspfExtLsdbChecksum,'rlOspfExtLsdbAdvertisement':rlOspfExtLsdbAdvertisement,'rlOspfAreaAggregateTable':rlOspfAreaAggregateTable,'rlOspfAreaAggregateEntry':rlOspfAreaAggregateEntry,_AV:rlOspfAreaAggregateProcessId,_AW:rlOspfAreaAggregateAreaID,_AX:rlOspfAreaAggregateLsdbType,_AY:rlOspfAreaAggregateNet,_AZ:rlOspfAreaAggregateMask,'rlOspfAreaAggregateStatus':rlOspfAreaAggregateStatus,'rlOspfAreaAggregateEffect':rlOspfAreaAggregateEffect,'rlOspfAreaAggregateExtRouteTag':rlOspfAreaAggregateExtRouteTag,'rlOspfLocalLsdbTable':rlOspfLocalLsdbTable,'rlOspfLocalLsdbEntry':rlOspfLocalLsdbEntry,_Aa:rlOspfLocalLsdbProcessId,_Ab:rlOspfLocalLsdbIpAddress,_Ac:rlOspfLocalLsdbAddressLessIf,_Ad:rlOspfLocalLsdbType,_Ae:rlOspfLocalLsdbLsid,_Af:rlOspfLocalLsdbRouterId,'rlOspfLocalLsdbSequence':rlOspfLocalLsdbSequence,'rlOspfLocalLsdbAge':rlOspfLocalLsdbAge,'rlOspfLocalLsdbChecksum':rlOspfLocalLsdbChecksum,'rlOspfLocalLsdbAdvertisement':rlOspfLocalLsdbAdvertisement,'rlOspfLocalLsdbAreaId':rlOspfLocalLsdbAreaId,'rlOspfVirtLocalLsdbTable':rlOspfVirtLocalLsdbTable,'rlOspfVirtLocalLsdbEntry':rlOspfVirtLocalLsdbEntry,_Ah:rlOspfVirtLocalLsdbProcessId,_Ai:rlOspfVirtLocalLsdbTransitArea,_Aj:rlOspfVirtLocalLsdbNeighbor,_Ak:rlOspfVirtLocalLsdbType,_Al:rlOspfVirtLocalLsdbLsid,_Am:rlOspfVirtLocalLsdbRouterId,'rlOspfVirtLocalLsdbSequence':rlOspfVirtLocalLsdbSequence,'rlOspfVirtLocalLsdbAge':rlOspfVirtLocalLsdbAge,'rlOspfVirtLocalLsdbChecksum':rlOspfVirtLocalLsdbChecksum,'rlOspfVirtLocalLsdbAdvertisement':rlOspfVirtLocalLsdbAdvertisement,'rlOspfEnableTrapsOspfErrors':rlOspfEnableTrapsOspfErrors,'rlOspfEnableTrapsOspfLsa':rlOspfEnableTrapsOspfLsa,'rlOspfEnableTrapsOspfRateLimitSeconds':rlOspfEnableTrapsOspfRateLimitSeconds,'rlOspfEnableTrapsOspfRateLimitTrapNumber':rlOspfEnableTrapsOspfRateLimitTrapNumber,'rlOspfEnableTrapsOspfTransmit':rlOspfEnableTrapsOspfTransmit,'rlOspfEnableTrapsOspfStateChange':rlOspfEnableTrapsOspfStateChange,'rlOspfExt':rlOspfExt,'rlOspfBrRouterTable':rlOspfBrRouterTable,'rlOspfBrRouterEntry':rlOspfBrRouterEntry,_An:rlOspfBrRouterProcessId,_Ao:rlOspfBrRouterAreaId,_Ap:rlOspfBrRouterRouterId,_Aq:rlOspfBrRouterNextHopIp,_Ar:rlOspfBrRouterOutIf,'rlOspfBrRouterRouteType':rlOspfBrRouterRouteType,'rlOspfBrRouterRouteCost':rlOspfBrRouterRouteCost,'rlOspfBrRouterRouterType':rlOspfBrRouterRouterType})