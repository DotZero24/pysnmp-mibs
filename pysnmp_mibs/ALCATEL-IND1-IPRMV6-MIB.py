_e='alaIprmV6ConfigMIBGroup'
_d='alaIprmV6StaticRouteName'
_c='alaIprmV6StaticRouteTag'
_b='alaIprmV6RtPrefIbgp'
_a='alaIprmV6RtPrefEbgp'
_Z='alaIprmV6RtPrefRip'
_Y='alaIprmV6RtPrefOspf'
_X='alaIprmV6RtPrefStatic'
_W='alaIprmV6RtPrefLocal'
_V='alaIprmV6StaticRouteStatus'
_U='alaIprmV6StaticRouteMetric'
_T='alaIprmV6RouteValid'
_S='alaIprmV6RouteMetric'
_R='alaIprmV6StaticRouteIfIndex'
_Q='alaIprmV6StaticRouteNextHop'
_P='alaIprmV6StaticRoutePfxLength'
_O='alaIprmV6StaticRouteDest'
_N='alaIprmV6RouteIfIndex'
_M='alaIprmV6RouteProtocol'
_L='alaIprmV6RouteNextHop'
_K='alaIprmV6RoutePfxLength'
_J='alaIprmV6RouteDest'
_I='Unsigned32'
_H='SnmpAdminString'
_G='read-only'
_F='read-create'
_E='read-write'
_D='not-accessible'
_C='Integer32'
_B='ALCATEL-IND1-IPRMV6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Iprm,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Iprm')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
Ipv6Address,Ipv6IfIndex=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6IfIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1IPRMV6MIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,2))
if mibBuilder.loadTexts:alcatelIND1IPRMV6MIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1IPRMV6MIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBObjects=_AlcatelIND1IPRMV6MIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1))
_AlaIprmV6Config_ObjectIdentity=ObjectIdentity
alaIprmV6Config=_AlaIprmV6Config_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1))
_AlaIprmV6RouteTable_Object=MibTable
alaIprmV6RouteTable=_AlaIprmV6RouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1))
if mibBuilder.loadTexts:alaIprmV6RouteTable.setStatus(_A)
_AlaIprmV6RouteEntry_Object=MibTableRow
alaIprmV6RouteEntry=_AlaIprmV6RouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1))
alaIprmV6RouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaIprmV6RouteEntry.setStatus(_A)
_AlaIprmV6RouteDest_Type=Ipv6Address
_AlaIprmV6RouteDest_Object=MibTableColumn
alaIprmV6RouteDest=_AlaIprmV6RouteDest_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,1),_AlaIprmV6RouteDest_Type())
alaIprmV6RouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6RouteDest.setStatus(_A)
class _AlaIprmV6RoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaIprmV6RoutePfxLength_Type.__name__=_C
_AlaIprmV6RoutePfxLength_Object=MibTableColumn
alaIprmV6RoutePfxLength=_AlaIprmV6RoutePfxLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,2),_AlaIprmV6RoutePfxLength_Type())
alaIprmV6RoutePfxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6RoutePfxLength.setStatus(_A)
if mibBuilder.loadTexts:alaIprmV6RoutePfxLength.setUnits('bits')
_AlaIprmV6RouteNextHop_Type=Ipv6Address
_AlaIprmV6RouteNextHop_Object=MibTableColumn
alaIprmV6RouteNextHop=_AlaIprmV6RouteNextHop_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,3),_AlaIprmV6RouteNextHop_Type())
alaIprmV6RouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6RouteNextHop.setStatus(_A)
_AlaIprmV6RouteProtocol_Type=IANAipRouteProtocol
_AlaIprmV6RouteProtocol_Object=MibTableColumn
alaIprmV6RouteProtocol=_AlaIprmV6RouteProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,4),_AlaIprmV6RouteProtocol_Type())
alaIprmV6RouteProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6RouteProtocol.setStatus(_A)
_AlaIprmV6RouteIfIndex_Type=Ipv6IfIndex
_AlaIprmV6RouteIfIndex_Object=MibTableColumn
alaIprmV6RouteIfIndex=_AlaIprmV6RouteIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,5),_AlaIprmV6RouteIfIndex_Type())
alaIprmV6RouteIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6RouteIfIndex.setStatus(_A)
_AlaIprmV6RouteMetric_Type=Unsigned32
_AlaIprmV6RouteMetric_Object=MibTableColumn
alaIprmV6RouteMetric=_AlaIprmV6RouteMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,6),_AlaIprmV6RouteMetric_Type())
alaIprmV6RouteMetric.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmV6RouteMetric.setStatus(_A)
_AlaIprmV6RouteValid_Type=TruthValue
_AlaIprmV6RouteValid_Object=MibTableColumn
alaIprmV6RouteValid=_AlaIprmV6RouteValid_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,1,1,7),_AlaIprmV6RouteValid_Type())
alaIprmV6RouteValid.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmV6RouteValid.setStatus(_A)
_AlaIprmV6StaticRouteTable_Object=MibTable
alaIprmV6StaticRouteTable=_AlaIprmV6StaticRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2))
if mibBuilder.loadTexts:alaIprmV6StaticRouteTable.setStatus(_A)
_AlaIprmV6StaticRouteEntry_Object=MibTableRow
alaIprmV6StaticRouteEntry=_AlaIprmV6StaticRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1))
alaIprmV6StaticRouteEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:alaIprmV6StaticRouteEntry.setStatus(_A)
_AlaIprmV6StaticRouteDest_Type=Ipv6Address
_AlaIprmV6StaticRouteDest_Object=MibTableColumn
alaIprmV6StaticRouteDest=_AlaIprmV6StaticRouteDest_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,1),_AlaIprmV6StaticRouteDest_Type())
alaIprmV6StaticRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteDest.setStatus(_A)
class _AlaIprmV6StaticRoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaIprmV6StaticRoutePfxLength_Type.__name__=_C
_AlaIprmV6StaticRoutePfxLength_Object=MibTableColumn
alaIprmV6StaticRoutePfxLength=_AlaIprmV6StaticRoutePfxLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,2),_AlaIprmV6StaticRoutePfxLength_Type())
alaIprmV6StaticRoutePfxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRoutePfxLength.setStatus(_A)
_AlaIprmV6StaticRouteNextHop_Type=Ipv6Address
_AlaIprmV6StaticRouteNextHop_Object=MibTableColumn
alaIprmV6StaticRouteNextHop=_AlaIprmV6StaticRouteNextHop_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,3),_AlaIprmV6StaticRouteNextHop_Type())
alaIprmV6StaticRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteNextHop.setStatus(_A)
_AlaIprmV6StaticRouteIfIndex_Type=Ipv6IfIndex
_AlaIprmV6StaticRouteIfIndex_Object=MibTableColumn
alaIprmV6StaticRouteIfIndex=_AlaIprmV6StaticRouteIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,4),_AlaIprmV6StaticRouteIfIndex_Type())
alaIprmV6StaticRouteIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteIfIndex.setStatus(_A)
class _AlaIprmV6StaticRouteMetric_Type(Unsigned32):defaultValue=1
_AlaIprmV6StaticRouteMetric_Type.__name__=_I
_AlaIprmV6StaticRouteMetric_Object=MibTableColumn
alaIprmV6StaticRouteMetric=_AlaIprmV6StaticRouteMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,5),_AlaIprmV6StaticRouteMetric_Type())
alaIprmV6StaticRouteMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6StaticRouteMetric.setStatus(_A)
_AlaIprmV6StaticRouteStatus_Type=RowStatus
_AlaIprmV6StaticRouteStatus_Object=MibTableColumn
alaIprmV6StaticRouteStatus=_AlaIprmV6StaticRouteStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,6),_AlaIprmV6StaticRouteStatus_Type())
alaIprmV6StaticRouteStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6StaticRouteStatus.setStatus(_A)
_AlaIprmV6StaticRouteTag_Type=Unsigned32
_AlaIprmV6StaticRouteTag_Object=MibTableColumn
alaIprmV6StaticRouteTag=_AlaIprmV6StaticRouteTag_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,7),_AlaIprmV6StaticRouteTag_Type())
alaIprmV6StaticRouteTag.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6StaticRouteTag.setStatus(_A)
class _AlaIprmV6StaticRouteName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaIprmV6StaticRouteName_Type.__name__=_H
_AlaIprmV6StaticRouteName_Object=MibTableColumn
alaIprmV6StaticRouteName=_AlaIprmV6StaticRouteName_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,2,1,8),_AlaIprmV6StaticRouteName_Type())
alaIprmV6StaticRouteName.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6StaticRouteName.setStatus(_A)
class _AlaIprmV6RtPrefLocal_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefLocal_Type.__name__=_C
_AlaIprmV6RtPrefLocal_Object=MibScalar
alaIprmV6RtPrefLocal=_AlaIprmV6RtPrefLocal_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,3),_AlaIprmV6RtPrefLocal_Type())
alaIprmV6RtPrefLocal.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmV6RtPrefLocal.setStatus(_A)
class _AlaIprmV6RtPrefStatic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefStatic_Type.__name__=_C
_AlaIprmV6RtPrefStatic_Object=MibScalar
alaIprmV6RtPrefStatic=_AlaIprmV6RtPrefStatic_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,4),_AlaIprmV6RtPrefStatic_Type())
alaIprmV6RtPrefStatic.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmV6RtPrefStatic.setStatus(_A)
class _AlaIprmV6RtPrefOspf_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefOspf_Type.__name__=_C
_AlaIprmV6RtPrefOspf_Object=MibScalar
alaIprmV6RtPrefOspf=_AlaIprmV6RtPrefOspf_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,5),_AlaIprmV6RtPrefOspf_Type())
alaIprmV6RtPrefOspf.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmV6RtPrefOspf.setStatus(_A)
class _AlaIprmV6RtPrefRip_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefRip_Type.__name__=_C
_AlaIprmV6RtPrefRip_Object=MibScalar
alaIprmV6RtPrefRip=_AlaIprmV6RtPrefRip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,6),_AlaIprmV6RtPrefRip_Type())
alaIprmV6RtPrefRip.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmV6RtPrefRip.setStatus(_A)
class _AlaIprmV6RtPrefEbgp_Type(Integer32):defaultValue=190;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefEbgp_Type.__name__=_C
_AlaIprmV6RtPrefEbgp_Object=MibScalar
alaIprmV6RtPrefEbgp=_AlaIprmV6RtPrefEbgp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,7),_AlaIprmV6RtPrefEbgp_Type())
alaIprmV6RtPrefEbgp.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmV6RtPrefEbgp.setStatus(_A)
class _AlaIprmV6RtPrefIbgp_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefIbgp_Type.__name__=_C
_AlaIprmV6RtPrefIbgp_Object=MibScalar
alaIprmV6RtPrefIbgp=_AlaIprmV6RtPrefIbgp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,1,1,8),_AlaIprmV6RtPrefIbgp_Type())
alaIprmV6RtPrefIbgp.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmV6RtPrefIbgp.setStatus(_A)
_AlcatelIND1IPRMV6MIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBConformance=_AlcatelIND1IPRMV6MIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,2))
_AlcatelIND1IPRMV6MIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBCompliances=_AlcatelIND1IPRMV6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,2,1))
_AlcatelIND1IPRMV6MIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBGroups=_AlcatelIND1IPRMV6MIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,2,2))
alaIprmV6ConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,2,2,1))
alaIprmV6ConfigMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:alaIprmV6ConfigMIBGroup.setStatus(_A)
alaIprmV6Compliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,2,2,2,1,1))
alaIprmV6Compliance.setObjects((_B,_e))
if mibBuilder.loadTexts:alaIprmV6Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1IPRMV6MIB':alcatelIND1IPRMV6MIB,'alcatelIND1IPRMV6MIBObjects':alcatelIND1IPRMV6MIBObjects,'alaIprmV6Config':alaIprmV6Config,'alaIprmV6RouteTable':alaIprmV6RouteTable,'alaIprmV6RouteEntry':alaIprmV6RouteEntry,_J:alaIprmV6RouteDest,_K:alaIprmV6RoutePfxLength,_L:alaIprmV6RouteNextHop,_M:alaIprmV6RouteProtocol,_N:alaIprmV6RouteIfIndex,_S:alaIprmV6RouteMetric,_T:alaIprmV6RouteValid,'alaIprmV6StaticRouteTable':alaIprmV6StaticRouteTable,'alaIprmV6StaticRouteEntry':alaIprmV6StaticRouteEntry,_O:alaIprmV6StaticRouteDest,_P:alaIprmV6StaticRoutePfxLength,_Q:alaIprmV6StaticRouteNextHop,_R:alaIprmV6StaticRouteIfIndex,_U:alaIprmV6StaticRouteMetric,_V:alaIprmV6StaticRouteStatus,_c:alaIprmV6StaticRouteTag,_d:alaIprmV6StaticRouteName,_W:alaIprmV6RtPrefLocal,_X:alaIprmV6RtPrefStatic,_Y:alaIprmV6RtPrefOspf,_Z:alaIprmV6RtPrefRip,_a:alaIprmV6RtPrefEbgp,_b:alaIprmV6RtPrefIbgp,'alcatelIND1IPRMV6MIBConformance':alcatelIND1IPRMV6MIBConformance,'alcatelIND1IPRMV6MIBCompliances':alcatelIND1IPRMV6MIBCompliances,'alaIprmV6Compliance':alaIprmV6Compliance,'alcatelIND1IPRMV6MIBGroups':alcatelIND1IPRMV6MIBGroups,_e:alaIprmV6ConfigMIBGroup})