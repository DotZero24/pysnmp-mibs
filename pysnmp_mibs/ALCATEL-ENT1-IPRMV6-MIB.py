_j='alaIprmV6ConfigMIBGroup'
_i='alaIprmV6StaticAllBfd'
_h='alaIprmV6ImportVrfRowStatus'
_g='alaIprmV6ImportVrfRouteMap'
_f='alaIprmV6ExportToAllVrfsRouteMap'
_e='alaIprmV6ExportRouteMap'
_d='alaIprmV6RtPrefEntryValue'
_c='alaIprmV6StaticRouteType'
_b='alaIprmV6StaticRouteBfdStatus'
_a='alaIprmV6StaticRouteName'
_Z='alaIprmV6StaticRouteTag'
_Y='alaIprmV6StaticRouteStatus'
_X='alaIprmV6StaticRouteMetric'
_W='alaIprmV6RouteValid'
_V='alaIprmV6RouteMetric'
_U='alaIprmV6ImportVrfName'
_T='alaIprmV6RtPrefEntryType'
_S='alaIprmV6StaticRouteIfIndex'
_R='alaIprmV6StaticRouteNextHop'
_Q='alaIprmV6StaticRoutePfxLength'
_P='alaIprmV6StaticRouteDest'
_O='read-only'
_N='alaIprmV6RouteIfIndex'
_M='alaIprmV6RouteProtocol'
_L='alaIprmV6RouteNextHop'
_K='alaIprmV6RoutePfxLength'
_J='alaIprmV6RouteDest'
_I='Unsigned32'
_H='AlaIprmAdminStatus'
_G='SnmpAdminString'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='not-accessible'
_B='ALCATEL-ENT1-IPRMV6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Iprm,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Iprm')
AlaIprmAdminStatus,AlaIprmStaticRouteTypes=mibBuilder.importSymbols('ALCATEL-ENT1-IPRM-MIB',_H,'AlaIprmStaticRouteTypes')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
Ipv6Address,Ipv6IfIndex,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6IfIndex','Ipv6IfIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1IPRMV6MIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,2))
if mibBuilder.loadTexts:alcatelIND1IPRMV6MIB.setRevisions(('2010-02-22 00:00',))
class AlaIprmV6RtPrefType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('local',1),('static',2),('ospf',3),('rip',4),('bgpExternal',5),('bgpInternal',6),('isisl1',7),('isisl2',8),('import',9)))
_AlcatelIND1IPRMV6MIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBObjects=_AlcatelIND1IPRMV6MIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1))
_AlaIprmV6Config_ObjectIdentity=ObjectIdentity
alaIprmV6Config=_AlaIprmV6Config_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1))
_AlaIprmV6RouteTable_Object=MibTable
alaIprmV6RouteTable=_AlaIprmV6RouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1))
if mibBuilder.loadTexts:alaIprmV6RouteTable.setStatus(_A)
_AlaIprmV6RouteEntry_Object=MibTableRow
alaIprmV6RouteEntry=_AlaIprmV6RouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1))
alaIprmV6RouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaIprmV6RouteEntry.setStatus(_A)
_AlaIprmV6RouteDest_Type=Ipv6Address
_AlaIprmV6RouteDest_Object=MibTableColumn
alaIprmV6RouteDest=_AlaIprmV6RouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,1),_AlaIprmV6RouteDest_Type())
alaIprmV6RouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6RouteDest.setStatus(_A)
class _AlaIprmV6RoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaIprmV6RoutePfxLength_Type.__name__=_E
_AlaIprmV6RoutePfxLength_Object=MibTableColumn
alaIprmV6RoutePfxLength=_AlaIprmV6RoutePfxLength_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,2),_AlaIprmV6RoutePfxLength_Type())
alaIprmV6RoutePfxLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6RoutePfxLength.setStatus(_A)
if mibBuilder.loadTexts:alaIprmV6RoutePfxLength.setUnits('bits')
_AlaIprmV6RouteNextHop_Type=Ipv6Address
_AlaIprmV6RouteNextHop_Object=MibTableColumn
alaIprmV6RouteNextHop=_AlaIprmV6RouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,3),_AlaIprmV6RouteNextHop_Type())
alaIprmV6RouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6RouteNextHop.setStatus(_A)
_AlaIprmV6RouteProtocol_Type=IANAipRouteProtocol
_AlaIprmV6RouteProtocol_Object=MibTableColumn
alaIprmV6RouteProtocol=_AlaIprmV6RouteProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,4),_AlaIprmV6RouteProtocol_Type())
alaIprmV6RouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6RouteProtocol.setStatus(_A)
_AlaIprmV6RouteIfIndex_Type=Ipv6IfIndex
_AlaIprmV6RouteIfIndex_Object=MibTableColumn
alaIprmV6RouteIfIndex=_AlaIprmV6RouteIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,5),_AlaIprmV6RouteIfIndex_Type())
alaIprmV6RouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6RouteIfIndex.setStatus(_A)
_AlaIprmV6RouteMetric_Type=Unsigned32
_AlaIprmV6RouteMetric_Object=MibTableColumn
alaIprmV6RouteMetric=_AlaIprmV6RouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,6),_AlaIprmV6RouteMetric_Type())
alaIprmV6RouteMetric.setMaxAccess(_O)
if mibBuilder.loadTexts:alaIprmV6RouteMetric.setStatus(_A)
_AlaIprmV6RouteValid_Type=TruthValue
_AlaIprmV6RouteValid_Object=MibTableColumn
alaIprmV6RouteValid=_AlaIprmV6RouteValid_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,1,1,7),_AlaIprmV6RouteValid_Type())
alaIprmV6RouteValid.setMaxAccess(_O)
if mibBuilder.loadTexts:alaIprmV6RouteValid.setStatus(_A)
_AlaIprmV6StaticRouteTable_Object=MibTable
alaIprmV6StaticRouteTable=_AlaIprmV6StaticRouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2))
if mibBuilder.loadTexts:alaIprmV6StaticRouteTable.setStatus(_A)
_AlaIprmV6StaticRouteEntry_Object=MibTableRow
alaIprmV6StaticRouteEntry=_AlaIprmV6StaticRouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1))
alaIprmV6StaticRouteEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:alaIprmV6StaticRouteEntry.setStatus(_A)
_AlaIprmV6StaticRouteDest_Type=Ipv6Address
_AlaIprmV6StaticRouteDest_Object=MibTableColumn
alaIprmV6StaticRouteDest=_AlaIprmV6StaticRouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,1),_AlaIprmV6StaticRouteDest_Type())
alaIprmV6StaticRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6StaticRouteDest.setStatus(_A)
class _AlaIprmV6StaticRoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaIprmV6StaticRoutePfxLength_Type.__name__=_E
_AlaIprmV6StaticRoutePfxLength_Object=MibTableColumn
alaIprmV6StaticRoutePfxLength=_AlaIprmV6StaticRoutePfxLength_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,2),_AlaIprmV6StaticRoutePfxLength_Type())
alaIprmV6StaticRoutePfxLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6StaticRoutePfxLength.setStatus(_A)
_AlaIprmV6StaticRouteNextHop_Type=Ipv6Address
_AlaIprmV6StaticRouteNextHop_Object=MibTableColumn
alaIprmV6StaticRouteNextHop=_AlaIprmV6StaticRouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,3),_AlaIprmV6StaticRouteNextHop_Type())
alaIprmV6StaticRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6StaticRouteNextHop.setStatus(_A)
_AlaIprmV6StaticRouteIfIndex_Type=Ipv6IfIndexOrZero
_AlaIprmV6StaticRouteIfIndex_Object=MibTableColumn
alaIprmV6StaticRouteIfIndex=_AlaIprmV6StaticRouteIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,4),_AlaIprmV6StaticRouteIfIndex_Type())
alaIprmV6StaticRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6StaticRouteIfIndex.setStatus(_A)
class _AlaIprmV6StaticRouteMetric_Type(Unsigned32):defaultValue=1
_AlaIprmV6StaticRouteMetric_Type.__name__=_I
_AlaIprmV6StaticRouteMetric_Object=MibTableColumn
alaIprmV6StaticRouteMetric=_AlaIprmV6StaticRouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,5),_AlaIprmV6StaticRouteMetric_Type())
alaIprmV6StaticRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteMetric.setStatus(_A)
_AlaIprmV6StaticRouteStatus_Type=RowStatus
_AlaIprmV6StaticRouteStatus_Object=MibTableColumn
alaIprmV6StaticRouteStatus=_AlaIprmV6StaticRouteStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,6),_AlaIprmV6StaticRouteStatus_Type())
alaIprmV6StaticRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteStatus.setStatus(_A)
_AlaIprmV6StaticRouteTag_Type=Unsigned32
_AlaIprmV6StaticRouteTag_Object=MibTableColumn
alaIprmV6StaticRouteTag=_AlaIprmV6StaticRouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,7),_AlaIprmV6StaticRouteTag_Type())
alaIprmV6StaticRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteTag.setStatus(_A)
class _AlaIprmV6StaticRouteName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaIprmV6StaticRouteName_Type.__name__=_G
_AlaIprmV6StaticRouteName_Object=MibTableColumn
alaIprmV6StaticRouteName=_AlaIprmV6StaticRouteName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,8),_AlaIprmV6StaticRouteName_Type())
alaIprmV6StaticRouteName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteName.setStatus(_A)
_AlaIprmV6StaticRouteBfdStatus_Type=AlaIprmAdminStatus
_AlaIprmV6StaticRouteBfdStatus_Object=MibTableColumn
alaIprmV6StaticRouteBfdStatus=_AlaIprmV6StaticRouteBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,9),_AlaIprmV6StaticRouteBfdStatus_Type())
alaIprmV6StaticRouteBfdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteBfdStatus.setStatus(_A)
_AlaIprmV6StaticRouteType_Type=AlaIprmStaticRouteTypes
_AlaIprmV6StaticRouteType_Object=MibTableColumn
alaIprmV6StaticRouteType=_AlaIprmV6StaticRouteType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,2,1,10),_AlaIprmV6StaticRouteType_Type())
alaIprmV6StaticRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6StaticRouteType.setStatus(_A)
_AlaIprmV6RtPrefTable_Object=MibTable
alaIprmV6RtPrefTable=_AlaIprmV6RtPrefTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,3))
if mibBuilder.loadTexts:alaIprmV6RtPrefTable.setStatus(_A)
_AlaIprmV6RtPrefTableEntry_Object=MibTableRow
alaIprmV6RtPrefTableEntry=_AlaIprmV6RtPrefTableEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,3,1))
alaIprmV6RtPrefTableEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaIprmV6RtPrefTableEntry.setStatus(_A)
_AlaIprmV6RtPrefEntryType_Type=AlaIprmV6RtPrefType
_AlaIprmV6RtPrefEntryType_Object=MibTableColumn
alaIprmV6RtPrefEntryType=_AlaIprmV6RtPrefEntryType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,3,1,1),_AlaIprmV6RtPrefEntryType_Type())
alaIprmV6RtPrefEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6RtPrefEntryType.setStatus(_A)
class _AlaIprmV6RtPrefEntryValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmV6RtPrefEntryValue_Type.__name__=_E
_AlaIprmV6RtPrefEntryValue_Object=MibTableColumn
alaIprmV6RtPrefEntryValue=_AlaIprmV6RtPrefEntryValue_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,3,1,2),_AlaIprmV6RtPrefEntryValue_Type())
alaIprmV6RtPrefEntryValue.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6RtPrefEntryValue.setStatus(_A)
_AlaIprmV6ExportRouteMap_Type=Integer32
_AlaIprmV6ExportRouteMap_Object=MibScalar
alaIprmV6ExportRouteMap=_AlaIprmV6ExportRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,4),_AlaIprmV6ExportRouteMap_Type())
alaIprmV6ExportRouteMap.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6ExportRouteMap.setStatus(_A)
_AlaIprmV6ExportToAllVrfsRouteMap_Type=Integer32
_AlaIprmV6ExportToAllVrfsRouteMap_Object=MibScalar
alaIprmV6ExportToAllVrfsRouteMap=_AlaIprmV6ExportToAllVrfsRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,5),_AlaIprmV6ExportToAllVrfsRouteMap_Type())
alaIprmV6ExportToAllVrfsRouteMap.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6ExportToAllVrfsRouteMap.setStatus(_A)
_AlaIprmV6ImportVrfTable_Object=MibTable
alaIprmV6ImportVrfTable=_AlaIprmV6ImportVrfTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,6))
if mibBuilder.loadTexts:alaIprmV6ImportVrfTable.setStatus(_A)
_AlaIprmV6ImportVrfEntry_Object=MibTableRow
alaIprmV6ImportVrfEntry=_AlaIprmV6ImportVrfEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,6,1))
alaIprmV6ImportVrfEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:alaIprmV6ImportVrfEntry.setStatus(_A)
class _AlaIprmV6ImportVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AlaIprmV6ImportVrfName_Type.__name__=_G
_AlaIprmV6ImportVrfName_Object=MibTableColumn
alaIprmV6ImportVrfName=_AlaIprmV6ImportVrfName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,6,1,1),_AlaIprmV6ImportVrfName_Type())
alaIprmV6ImportVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmV6ImportVrfName.setStatus(_A)
_AlaIprmV6ImportVrfRouteMap_Type=Integer32
_AlaIprmV6ImportVrfRouteMap_Object=MibTableColumn
alaIprmV6ImportVrfRouteMap=_AlaIprmV6ImportVrfRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,6,1,2),_AlaIprmV6ImportVrfRouteMap_Type())
alaIprmV6ImportVrfRouteMap.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6ImportVrfRouteMap.setStatus(_A)
_AlaIprmV6ImportVrfRowStatus_Type=RowStatus
_AlaIprmV6ImportVrfRowStatus_Object=MibTableColumn
alaIprmV6ImportVrfRowStatus=_AlaIprmV6ImportVrfRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,6,1,3),_AlaIprmV6ImportVrfRowStatus_Type())
alaIprmV6ImportVrfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmV6ImportVrfRowStatus.setStatus(_A)
class _AlaIprmV6StaticAllBfd_Type(AlaIprmAdminStatus):defaultValue=2
_AlaIprmV6StaticAllBfd_Type.__name__=_H
_AlaIprmV6StaticAllBfd_Object=MibScalar
alaIprmV6StaticAllBfd=_AlaIprmV6StaticAllBfd_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,1,1,7),_AlaIprmV6StaticAllBfd_Type())
alaIprmV6StaticAllBfd.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmV6StaticAllBfd.setStatus(_A)
_AlcatelIND1IPRMV6MIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBConformance=_AlcatelIND1IPRMV6MIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,2))
_AlcatelIND1IPRMV6MIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBCompliances=_AlcatelIND1IPRMV6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,2,1))
_AlcatelIND1IPRMV6MIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMV6MIBGroups=_AlcatelIND1IPRMV6MIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,2,2))
alaIprmV6ConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,2,2,1))
alaIprmV6ConfigMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:alaIprmV6ConfigMIBGroup.setStatus(_A)
alaIprmV6Compliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,2,2,2,1,1))
alaIprmV6Compliance.setObjects((_B,_j))
if mibBuilder.loadTexts:alaIprmV6Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaIprmV6RtPrefType':AlaIprmV6RtPrefType,'alcatelIND1IPRMV6MIB':alcatelIND1IPRMV6MIB,'alcatelIND1IPRMV6MIBObjects':alcatelIND1IPRMV6MIBObjects,'alaIprmV6Config':alaIprmV6Config,'alaIprmV6RouteTable':alaIprmV6RouteTable,'alaIprmV6RouteEntry':alaIprmV6RouteEntry,_J:alaIprmV6RouteDest,_K:alaIprmV6RoutePfxLength,_L:alaIprmV6RouteNextHop,_M:alaIprmV6RouteProtocol,_N:alaIprmV6RouteIfIndex,_V:alaIprmV6RouteMetric,_W:alaIprmV6RouteValid,'alaIprmV6StaticRouteTable':alaIprmV6StaticRouteTable,'alaIprmV6StaticRouteEntry':alaIprmV6StaticRouteEntry,_P:alaIprmV6StaticRouteDest,_Q:alaIprmV6StaticRoutePfxLength,_R:alaIprmV6StaticRouteNextHop,_S:alaIprmV6StaticRouteIfIndex,_X:alaIprmV6StaticRouteMetric,_Y:alaIprmV6StaticRouteStatus,_Z:alaIprmV6StaticRouteTag,_a:alaIprmV6StaticRouteName,_b:alaIprmV6StaticRouteBfdStatus,_c:alaIprmV6StaticRouteType,'alaIprmV6RtPrefTable':alaIprmV6RtPrefTable,'alaIprmV6RtPrefTableEntry':alaIprmV6RtPrefTableEntry,_T:alaIprmV6RtPrefEntryType,_d:alaIprmV6RtPrefEntryValue,_e:alaIprmV6ExportRouteMap,_f:alaIprmV6ExportToAllVrfsRouteMap,'alaIprmV6ImportVrfTable':alaIprmV6ImportVrfTable,'alaIprmV6ImportVrfEntry':alaIprmV6ImportVrfEntry,_U:alaIprmV6ImportVrfName,_g:alaIprmV6ImportVrfRouteMap,_h:alaIprmV6ImportVrfRowStatus,_i:alaIprmV6StaticAllBfd,'alcatelIND1IPRMV6MIBConformance':alcatelIND1IPRMV6MIBConformance,'alcatelIND1IPRMV6MIBCompliances':alcatelIND1IPRMV6MIBCompliances,'alaIprmV6Compliance':alaIprmV6Compliance,'alcatelIND1IPRMV6MIBGroups':alcatelIND1IPRMV6MIBGroups,_j:alaIprmV6ConfigMIBGroup})