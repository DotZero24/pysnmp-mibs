_V='alaGrtConfigMIBGroup'
_U='alaGrt6RouteVrfName'
_T='alaGrt6RouteTag'
_S='alaGrt6RouteMetric'
_R='alaGrtRouteIsid'
_Q='alaGrtRouteVrfName'
_P='alaGrtRouteTag'
_O='alaGrtRouteMetric'
_N='alaGrt6RouteIfIndex'
_M='alaGrt6RouteNextHop'
_L='alaGrt6RouteMaskLen'
_K='alaGrt6RouteDest'
_J='alaGrt6RouteDistinguisher'
_I='alaGrtRouteNextHop'
_H='alaGrtRouteMaskLen'
_G='alaGrtRouteDest'
_F='alaGrtRouteDistinguisher'
_E='OctetString'
_D='read-only'
_C='not-accessible'
_B='ALCATEL-ENT1-GLOBALROUTETABLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1GlobalRouteTable,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1GlobalRouteTable')
Ipv6Address,Ipv6IfIndex=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1GRTMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16,1))
if mibBuilder.loadTexts:alcatelIND1GRTMIB.setRevisions(('2014-02-07 00:00',))
class AlaGrtRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AlcatelIND1GRTMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBObjects=_AlcatelIND1GRTMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1))
_AlaGrtConfig_ObjectIdentity=ObjectIdentity
alaGrtConfig=_AlaGrtConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1))
_AlaGrtRouteTable_Object=MibTable
alaGrtRouteTable=_AlaGrtRouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1))
if mibBuilder.loadTexts:alaGrtRouteTable.setStatus(_A)
_AlaGrtRouteEntry_Object=MibTableRow
alaGrtRouteEntry=_AlaGrtRouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1))
alaGrtRouteEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:alaGrtRouteEntry.setStatus(_A)
_AlaGrtRouteDistinguisher_Type=AlaGrtRouteDistinguisher
_AlaGrtRouteDistinguisher_Object=MibTableColumn
alaGrtRouteDistinguisher=_AlaGrtRouteDistinguisher_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,1),_AlaGrtRouteDistinguisher_Type())
alaGrtRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteDistinguisher.setStatus(_A)
_AlaGrtRouteDest_Type=IpAddress
_AlaGrtRouteDest_Object=MibTableColumn
alaGrtRouteDest=_AlaGrtRouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,2),_AlaGrtRouteDest_Type())
alaGrtRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteDest.setStatus(_A)
_AlaGrtRouteMaskLen_Type=Unsigned32
_AlaGrtRouteMaskLen_Object=MibTableColumn
alaGrtRouteMaskLen=_AlaGrtRouteMaskLen_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,3),_AlaGrtRouteMaskLen_Type())
alaGrtRouteMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteMaskLen.setStatus(_A)
_AlaGrtRouteNextHop_Type=IpAddress
_AlaGrtRouteNextHop_Object=MibTableColumn
alaGrtRouteNextHop=_AlaGrtRouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,4),_AlaGrtRouteNextHop_Type())
alaGrtRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrtRouteNextHop.setStatus(_A)
_AlaGrtRouteMetric_Type=Unsigned32
_AlaGrtRouteMetric_Object=MibTableColumn
alaGrtRouteMetric=_AlaGrtRouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,5),_AlaGrtRouteMetric_Type())
alaGrtRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrtRouteMetric.setStatus(_A)
_AlaGrtRouteTag_Type=Unsigned32
_AlaGrtRouteTag_Object=MibTableColumn
alaGrtRouteTag=_AlaGrtRouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,6),_AlaGrtRouteTag_Type())
alaGrtRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrtRouteTag.setStatus(_A)
class _AlaGrtRouteVrfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AlaGrtRouteVrfName_Type.__name__=_E
_AlaGrtRouteVrfName_Object=MibTableColumn
alaGrtRouteVrfName=_AlaGrtRouteVrfName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,7),_AlaGrtRouteVrfName_Type())
alaGrtRouteVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrtRouteVrfName.setStatus(_A)
_AlaGrtRouteIsid_Type=Unsigned32
_AlaGrtRouteIsid_Object=MibTableColumn
alaGrtRouteIsid=_AlaGrtRouteIsid_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,1,1,8),_AlaGrtRouteIsid_Type())
alaGrtRouteIsid.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrtRouteIsid.setStatus(_A)
_AlaGrt6RouteTable_Object=MibTable
alaGrt6RouteTable=_AlaGrt6RouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2))
if mibBuilder.loadTexts:alaGrt6RouteTable.setStatus(_A)
_AlaGrt6RouteEntry_Object=MibTableRow
alaGrt6RouteEntry=_AlaGrt6RouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1))
alaGrt6RouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaGrt6RouteEntry.setStatus(_A)
_AlaGrt6RouteDistinguisher_Type=AlaGrtRouteDistinguisher
_AlaGrt6RouteDistinguisher_Object=MibTableColumn
alaGrt6RouteDistinguisher=_AlaGrt6RouteDistinguisher_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,1),_AlaGrt6RouteDistinguisher_Type())
alaGrt6RouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrt6RouteDistinguisher.setStatus(_A)
_AlaGrt6RouteDest_Type=Ipv6Address
_AlaGrt6RouteDest_Object=MibTableColumn
alaGrt6RouteDest=_AlaGrt6RouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,2),_AlaGrt6RouteDest_Type())
alaGrt6RouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrt6RouteDest.setStatus(_A)
_AlaGrt6RouteMaskLen_Type=Unsigned32
_AlaGrt6RouteMaskLen_Object=MibTableColumn
alaGrt6RouteMaskLen=_AlaGrt6RouteMaskLen_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,3),_AlaGrt6RouteMaskLen_Type())
alaGrt6RouteMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrt6RouteMaskLen.setStatus(_A)
_AlaGrt6RouteNextHop_Type=Ipv6Address
_AlaGrt6RouteNextHop_Object=MibTableColumn
alaGrt6RouteNextHop=_AlaGrt6RouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,4),_AlaGrt6RouteNextHop_Type())
alaGrt6RouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrt6RouteNextHop.setStatus(_A)
_AlaGrt6RouteIfIndex_Type=Ipv6IfIndex
_AlaGrt6RouteIfIndex_Object=MibTableColumn
alaGrt6RouteIfIndex=_AlaGrt6RouteIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,5),_AlaGrt6RouteIfIndex_Type())
alaGrt6RouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaGrt6RouteIfIndex.setStatus(_A)
_AlaGrt6RouteMetric_Type=Unsigned32
_AlaGrt6RouteMetric_Object=MibTableColumn
alaGrt6RouteMetric=_AlaGrt6RouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,6),_AlaGrt6RouteMetric_Type())
alaGrt6RouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrt6RouteMetric.setStatus(_A)
_AlaGrt6RouteTag_Type=Unsigned32
_AlaGrt6RouteTag_Object=MibTableColumn
alaGrt6RouteTag=_AlaGrt6RouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,7),_AlaGrt6RouteTag_Type())
alaGrt6RouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrt6RouteTag.setStatus(_A)
class _AlaGrt6RouteVrfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AlaGrt6RouteVrfName_Type.__name__=_E
_AlaGrt6RouteVrfName_Object=MibTableColumn
alaGrt6RouteVrfName=_AlaGrt6RouteVrfName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,1,1,2,1,8),_AlaGrt6RouteVrfName_Type())
alaGrt6RouteVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaGrt6RouteVrfName.setStatus(_A)
_AlcatelIND1GRTMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBConformance=_AlcatelIND1GRTMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,2))
_AlcatelIND1GRTMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBCompliances=_AlcatelIND1GRTMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,2,1))
_AlcatelIND1GRTMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1GRTMIBGroups=_AlcatelIND1GRTMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,2,2))
alaGrtConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,2,2,1))
alaGrtConfigMIBGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alaGrtConfigMIBGroup.setStatus(_A)
alaGrtCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,16,1,2,1,1))
alaGrtCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:alaGrtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaGrtRouteDistinguisher':AlaGrtRouteDistinguisher,'alcatelIND1GRTMIB':alcatelIND1GRTMIB,'alcatelIND1GRTMIBObjects':alcatelIND1GRTMIBObjects,'alaGrtConfig':alaGrtConfig,'alaGrtRouteTable':alaGrtRouteTable,'alaGrtRouteEntry':alaGrtRouteEntry,_F:alaGrtRouteDistinguisher,_G:alaGrtRouteDest,_H:alaGrtRouteMaskLen,_I:alaGrtRouteNextHop,_O:alaGrtRouteMetric,_P:alaGrtRouteTag,_Q:alaGrtRouteVrfName,_R:alaGrtRouteIsid,'alaGrt6RouteTable':alaGrt6RouteTable,'alaGrt6RouteEntry':alaGrt6RouteEntry,_J:alaGrt6RouteDistinguisher,_K:alaGrt6RouteDest,_L:alaGrt6RouteMaskLen,_M:alaGrt6RouteNextHop,_N:alaGrt6RouteIfIndex,_S:alaGrt6RouteMetric,_T:alaGrt6RouteTag,_U:alaGrt6RouteVrfName,'alcatelIND1GRTMIBConformance':alcatelIND1GRTMIBConformance,'alcatelIND1GRTMIBCompliances':alcatelIND1GRTMIBCompliances,'alaGrtCompliance':alaGrtCompliance,'alcatelIND1GRTMIBGroups':alcatelIND1GRTMIBGroups,_V:alaGrtConfigMIBGroup})