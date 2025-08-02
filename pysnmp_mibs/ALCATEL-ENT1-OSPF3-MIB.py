_n='alaOSPF3ConfigMIBGroup'
_m='alaOspf3AreaSummarizationRangeCount'
_l='alaOspf3AreaInterfaceCount'
_k='alaOspf3AreaHostCount'
_j='alaOspf3AreaInterAreaRouterLsaCount'
_i='alaOspf3AreaInterAreaPrefixLsaCount'
_h='alaOspf3AreaIntraAreaPrefixLsaCount'
_g='alaOspf3AreaNetworkLsaCount'
_f='alaOspf3AreaRouterLsaCount'
_e='alaOspf3IfBfdStatus'
_d='alaOspf3IfBfdDrsOnly'
_c='alaOspf3BfdAllInterfaceStatus'
_b='alaOspf3BfdStatus'
_a='alaOspf3RouteMetric2'
_Z='alaOspf3RouteMetric1'
_Y='alaOspf3RoutePathType'
_X='alaOspf3RouteType'
_W='alaOspf3MTUCheck'
_V='alaOspf3RestartInitiate'
_U='alaOspf3RestartStrictLsaChecking'
_T='alaOspf3RestartHelperSupport'
_S='alaOspf3TimerSpfHold'
_R='alaOspf3TimerSpfDelay'
_Q='alaOspf3OrigRouteTag'
_P='alaOspf3AreaAugEntry'
_O='alaOspf3IfAugEntry'
_N='read-create'
_M='alaOspf3RouteIfIndex'
_L='alaOspf3RouteNextHop'
_K='alaOspf3RoutePfxLength'
_J='alaOspf3RouteDest'
_I='Unsigned32'
_H='not-accessible'
_G='disable'
_F='enable'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALCATEL-ENT1-OSPF3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ospf3,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Ospf3')
Ipv6Address,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6IfIndexOrZero')
ospfv3AreaEntry,ospfv3IfEntry=mibBuilder.importSymbols('OSPFV3-MIB','ospfv3AreaEntry','ospfv3IfEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1OSPF3MIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13,1))
if mibBuilder.loadTexts:alcatelIND1OSPF3MIB.setRevisions(('2014-10-06 00:00','2007-04-03 00:00'))
_AlcatelIND1OSPF3MIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBObjects=_AlcatelIND1OSPF3MIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1))
_AlaProtocolOspf3_ObjectIdentity=ObjectIdentity
alaProtocolOspf3=_AlaProtocolOspf3_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1))
class _AlaOspf3OrigRouteTag_Type(Unsigned32):defaultValue=0
_AlaOspf3OrigRouteTag_Type.__name__=_I
_AlaOspf3OrigRouteTag_Object=MibScalar
alaOspf3OrigRouteTag=_AlaOspf3OrigRouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,1),_AlaOspf3OrigRouteTag_Type())
alaOspf3OrigRouteTag.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3OrigRouteTag.setStatus(_A)
class _AlaOspf3TimerSpfDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaOspf3TimerSpfDelay_Type.__name__=_C
_AlaOspf3TimerSpfDelay_Object=MibScalar
alaOspf3TimerSpfDelay=_AlaOspf3TimerSpfDelay_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,2),_AlaOspf3TimerSpfDelay_Type())
alaOspf3TimerSpfDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3TimerSpfDelay.setStatus(_A)
class _AlaOspf3TimerSpfHold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaOspf3TimerSpfHold_Type.__name__=_C
_AlaOspf3TimerSpfHold_Object=MibScalar
alaOspf3TimerSpfHold=_AlaOspf3TimerSpfHold_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,3),_AlaOspf3TimerSpfHold_Type())
alaOspf3TimerSpfHold.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3TimerSpfHold.setStatus(_A)
class _AlaOspf3RestartHelperSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3RestartHelperSupport_Type.__name__=_C
_AlaOspf3RestartHelperSupport_Object=MibScalar
alaOspf3RestartHelperSupport=_AlaOspf3RestartHelperSupport_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,4),_AlaOspf3RestartHelperSupport_Type())
alaOspf3RestartHelperSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3RestartHelperSupport.setStatus(_A)
class _AlaOspf3RestartStrictLsaChecking_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3RestartStrictLsaChecking_Type.__name__=_C
_AlaOspf3RestartStrictLsaChecking_Object=MibScalar
alaOspf3RestartStrictLsaChecking=_AlaOspf3RestartStrictLsaChecking_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,5),_AlaOspf3RestartStrictLsaChecking_Type())
alaOspf3RestartStrictLsaChecking.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3RestartStrictLsaChecking.setStatus(_A)
class _AlaOspf3RestartInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3RestartInitiate_Type.__name__=_C
_AlaOspf3RestartInitiate_Object=MibScalar
alaOspf3RestartInitiate=_AlaOspf3RestartInitiate_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,6),_AlaOspf3RestartInitiate_Type())
alaOspf3RestartInitiate.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3RestartInitiate.setStatus(_A)
class _AlaOspf3MTUCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3MTUCheck_Type.__name__=_C
_AlaOspf3MTUCheck_Object=MibScalar
alaOspf3MTUCheck=_AlaOspf3MTUCheck_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,7),_AlaOspf3MTUCheck_Type())
alaOspf3MTUCheck.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3MTUCheck.setStatus(_A)
_AlaOspf3RouteTable_Object=MibTable
alaOspf3RouteTable=_AlaOspf3RouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8))
if mibBuilder.loadTexts:alaOspf3RouteTable.setStatus(_A)
_AlaOspf3RouteEntry_Object=MibTableRow
alaOspf3RouteEntry=_AlaOspf3RouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1))
alaOspf3RouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:alaOspf3RouteEntry.setStatus(_A)
_AlaOspf3RouteDest_Type=Ipv6Address
_AlaOspf3RouteDest_Object=MibTableColumn
alaOspf3RouteDest=_AlaOspf3RouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,1),_AlaOspf3RouteDest_Type())
alaOspf3RouteDest.setMaxAccess(_H)
if mibBuilder.loadTexts:alaOspf3RouteDest.setStatus(_A)
class _AlaOspf3RoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaOspf3RoutePfxLength_Type.__name__=_C
_AlaOspf3RoutePfxLength_Object=MibTableColumn
alaOspf3RoutePfxLength=_AlaOspf3RoutePfxLength_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,2),_AlaOspf3RoutePfxLength_Type())
alaOspf3RoutePfxLength.setMaxAccess(_H)
if mibBuilder.loadTexts:alaOspf3RoutePfxLength.setStatus(_A)
if mibBuilder.loadTexts:alaOspf3RoutePfxLength.setUnits('bits')
_AlaOspf3RouteNextHop_Type=Ipv6Address
_AlaOspf3RouteNextHop_Object=MibTableColumn
alaOspf3RouteNextHop=_AlaOspf3RouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,3),_AlaOspf3RouteNextHop_Type())
alaOspf3RouteNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:alaOspf3RouteNextHop.setStatus(_A)
_AlaOspf3RouteIfIndex_Type=Ipv6IfIndexOrZero
_AlaOspf3RouteIfIndex_Object=MibTableColumn
alaOspf3RouteIfIndex=_AlaOspf3RouteIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,4),_AlaOspf3RouteIfIndex_Type())
alaOspf3RouteIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaOspf3RouteIfIndex.setStatus(_A)
class _AlaOspf3RouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('host',1),('other',2)))
_AlaOspf3RouteType_Type.__name__=_C
_AlaOspf3RouteType_Object=MibTableColumn
alaOspf3RouteType=_AlaOspf3RouteType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,5),_AlaOspf3RouteType_Type())
alaOspf3RouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RouteType.setStatus(_A)
class _AlaOspf3RoutePathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('intraArea',1),('interArea',2),('externalType1',3),('externalType2',4)))
_AlaOspf3RoutePathType_Type.__name__=_C
_AlaOspf3RoutePathType_Object=MibTableColumn
alaOspf3RoutePathType=_AlaOspf3RoutePathType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,6),_AlaOspf3RoutePathType_Type())
alaOspf3RoutePathType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RoutePathType.setStatus(_A)
_AlaOspf3RouteMetric1_Type=Unsigned32
_AlaOspf3RouteMetric1_Object=MibTableColumn
alaOspf3RouteMetric1=_AlaOspf3RouteMetric1_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,7),_AlaOspf3RouteMetric1_Type())
alaOspf3RouteMetric1.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RouteMetric1.setStatus(_A)
_AlaOspf3RouteMetric2_Type=Unsigned32
_AlaOspf3RouteMetric2_Object=MibTableColumn
alaOspf3RouteMetric2=_AlaOspf3RouteMetric2_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,8,1,8),_AlaOspf3RouteMetric2_Type())
alaOspf3RouteMetric2.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3RouteMetric2.setStatus(_A)
class _AlaOspf3BfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3BfdStatus_Type.__name__=_C
_AlaOspf3BfdStatus_Object=MibScalar
alaOspf3BfdStatus=_AlaOspf3BfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,9),_AlaOspf3BfdStatus_Type())
alaOspf3BfdStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3BfdStatus.setStatus(_A)
class _AlaOspf3BfdAllInterfaceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3BfdAllInterfaceStatus_Type.__name__=_C
_AlaOspf3BfdAllInterfaceStatus_Object=MibScalar
alaOspf3BfdAllInterfaceStatus=_AlaOspf3BfdAllInterfaceStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,10),_AlaOspf3BfdAllInterfaceStatus_Type())
alaOspf3BfdAllInterfaceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOspf3BfdAllInterfaceStatus.setStatus(_A)
_AlaOspf3IfAugTable_Object=MibTable
alaOspf3IfAugTable=_AlaOspf3IfAugTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,11))
if mibBuilder.loadTexts:alaOspf3IfAugTable.setStatus(_A)
_AlaOspf3IfAugEntry_Object=MibTableRow
alaOspf3IfAugEntry=_AlaOspf3IfAugEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,11,1))
if mibBuilder.loadTexts:alaOspf3IfAugEntry.setStatus(_A)
class _AlaOspf3IfBfdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3IfBfdStatus_Type.__name__=_C
_AlaOspf3IfBfdStatus_Object=MibTableColumn
alaOspf3IfBfdStatus=_AlaOspf3IfBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,11,1,1),_AlaOspf3IfBfdStatus_Type())
alaOspf3IfBfdStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:alaOspf3IfBfdStatus.setStatus(_A)
class _AlaOspf3IfBfdDrsOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaOspf3IfBfdDrsOnly_Type.__name__=_C
_AlaOspf3IfBfdDrsOnly_Object=MibTableColumn
alaOspf3IfBfdDrsOnly=_AlaOspf3IfBfdDrsOnly_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,11,1,2),_AlaOspf3IfBfdDrsOnly_Type())
alaOspf3IfBfdDrsOnly.setMaxAccess(_N)
if mibBuilder.loadTexts:alaOspf3IfBfdDrsOnly.setStatus(_A)
_AlaOspf3AreaAugTable_Object=MibTable
alaOspf3AreaAugTable=_AlaOspf3AreaAugTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12))
if mibBuilder.loadTexts:alaOspf3AreaAugTable.setStatus(_A)
_AlaOspf3AreaAugEntry_Object=MibTableRow
alaOspf3AreaAugEntry=_AlaOspf3AreaAugEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1))
if mibBuilder.loadTexts:alaOspf3AreaAugEntry.setStatus(_A)
_AlaOspf3AreaRouterLsaCount_Type=Gauge32
_AlaOspf3AreaRouterLsaCount_Object=MibTableColumn
alaOspf3AreaRouterLsaCount=_AlaOspf3AreaRouterLsaCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,1),_AlaOspf3AreaRouterLsaCount_Type())
alaOspf3AreaRouterLsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaRouterLsaCount.setStatus(_A)
_AlaOspf3AreaNetworkLsaCount_Type=Gauge32
_AlaOspf3AreaNetworkLsaCount_Object=MibTableColumn
alaOspf3AreaNetworkLsaCount=_AlaOspf3AreaNetworkLsaCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,2),_AlaOspf3AreaNetworkLsaCount_Type())
alaOspf3AreaNetworkLsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaNetworkLsaCount.setStatus(_A)
_AlaOspf3AreaIntraAreaPrefixLsaCount_Type=Gauge32
_AlaOspf3AreaIntraAreaPrefixLsaCount_Object=MibTableColumn
alaOspf3AreaIntraAreaPrefixLsaCount=_AlaOspf3AreaIntraAreaPrefixLsaCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,3),_AlaOspf3AreaIntraAreaPrefixLsaCount_Type())
alaOspf3AreaIntraAreaPrefixLsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaIntraAreaPrefixLsaCount.setStatus(_A)
_AlaOspf3AreaInterAreaPrefixLsaCount_Type=Gauge32
_AlaOspf3AreaInterAreaPrefixLsaCount_Object=MibTableColumn
alaOspf3AreaInterAreaPrefixLsaCount=_AlaOspf3AreaInterAreaPrefixLsaCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,4),_AlaOspf3AreaInterAreaPrefixLsaCount_Type())
alaOspf3AreaInterAreaPrefixLsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaInterAreaPrefixLsaCount.setStatus(_A)
_AlaOspf3AreaInterAreaRouterLsaCount_Type=Gauge32
_AlaOspf3AreaInterAreaRouterLsaCount_Object=MibTableColumn
alaOspf3AreaInterAreaRouterLsaCount=_AlaOspf3AreaInterAreaRouterLsaCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,5),_AlaOspf3AreaInterAreaRouterLsaCount_Type())
alaOspf3AreaInterAreaRouterLsaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaInterAreaRouterLsaCount.setStatus(_A)
_AlaOspf3AreaHostCount_Type=Gauge32
_AlaOspf3AreaHostCount_Object=MibTableColumn
alaOspf3AreaHostCount=_AlaOspf3AreaHostCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,6),_AlaOspf3AreaHostCount_Type())
alaOspf3AreaHostCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaHostCount.setStatus(_A)
_AlaOspf3AreaInterfaceCount_Type=Gauge32
_AlaOspf3AreaInterfaceCount_Object=MibTableColumn
alaOspf3AreaInterfaceCount=_AlaOspf3AreaInterfaceCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,7),_AlaOspf3AreaInterfaceCount_Type())
alaOspf3AreaInterfaceCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaInterfaceCount.setStatus(_A)
_AlaOspf3AreaSummarizationRangeCount_Type=Gauge32
_AlaOspf3AreaSummarizationRangeCount_Object=MibTableColumn
alaOspf3AreaSummarizationRangeCount=_AlaOspf3AreaSummarizationRangeCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,1,1,12,1,8),_AlaOspf3AreaSummarizationRangeCount_Type())
alaOspf3AreaSummarizationRangeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOspf3AreaSummarizationRangeCount.setStatus(_A)
_AlcatelIND1OSPF3MIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBConformance=_AlcatelIND1OSPF3MIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2))
_AlcatelIND1OSPF3MIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBCompliances=_AlcatelIND1OSPF3MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2,1))
_AlcatelIND1OSPF3MIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1OSPF3MIBGroups=_AlcatelIND1OSPF3MIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2,2))
ospfv3IfEntry.registerAugmentions((_B,_O))
alaOspf3IfAugEntry.setIndexNames(*ospfv3IfEntry.getIndexNames())
ospfv3AreaEntry.registerAugmentions((_B,_P))
alaOspf3AreaAugEntry.setIndexNames(*ospfv3AreaEntry.getIndexNames())
alaOSPF3ConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2,2,1))
alaOSPF3ConfigMIBGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:alaOSPF3ConfigMIBGroup.setStatus(_A)
alaOspf3RouteGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2,2,2))
alaOspf3RouteGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:alaOspf3RouteGroup.setStatus(_A)
alaOspf3AreaGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2,2,3))
alaOspf3AreaGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:alaOspf3AreaGroup.setStatus(_A)
alcatelIND1OSPF3MIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,13,1,2,1,1))
alcatelIND1OSPF3MIBCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:alcatelIND1OSPF3MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1OSPF3MIB':alcatelIND1OSPF3MIB,'alcatelIND1OSPF3MIBObjects':alcatelIND1OSPF3MIBObjects,'alaProtocolOspf3':alaProtocolOspf3,_Q:alaOspf3OrigRouteTag,_R:alaOspf3TimerSpfDelay,_S:alaOspf3TimerSpfHold,_T:alaOspf3RestartHelperSupport,_U:alaOspf3RestartStrictLsaChecking,_V:alaOspf3RestartInitiate,_W:alaOspf3MTUCheck,'alaOspf3RouteTable':alaOspf3RouteTable,'alaOspf3RouteEntry':alaOspf3RouteEntry,_J:alaOspf3RouteDest,_K:alaOspf3RoutePfxLength,_L:alaOspf3RouteNextHop,_M:alaOspf3RouteIfIndex,_X:alaOspf3RouteType,_Y:alaOspf3RoutePathType,_Z:alaOspf3RouteMetric1,_a:alaOspf3RouteMetric2,_b:alaOspf3BfdStatus,_c:alaOspf3BfdAllInterfaceStatus,'alaOspf3IfAugTable':alaOspf3IfAugTable,_O:alaOspf3IfAugEntry,_e:alaOspf3IfBfdStatus,_d:alaOspf3IfBfdDrsOnly,'alaOspf3AreaAugTable':alaOspf3AreaAugTable,_P:alaOspf3AreaAugEntry,_f:alaOspf3AreaRouterLsaCount,_g:alaOspf3AreaNetworkLsaCount,_h:alaOspf3AreaIntraAreaPrefixLsaCount,_i:alaOspf3AreaInterAreaPrefixLsaCount,_j:alaOspf3AreaInterAreaRouterLsaCount,_k:alaOspf3AreaHostCount,_l:alaOspf3AreaInterfaceCount,_m:alaOspf3AreaSummarizationRangeCount,'alcatelIND1OSPF3MIBConformance':alcatelIND1OSPF3MIBConformance,'alcatelIND1OSPF3MIBCompliances':alcatelIND1OSPF3MIBCompliances,'alcatelIND1OSPF3MIBCompliance':alcatelIND1OSPF3MIBCompliance,'alcatelIND1OSPF3MIBGroups':alcatelIND1OSPF3MIBGroups,_n:alaOSPF3ConfigMIBGroup,'alaOspf3RouteGroup':alaOspf3RouteGroup,'alaOspf3AreaGroup':alaOspf3AreaGroup})