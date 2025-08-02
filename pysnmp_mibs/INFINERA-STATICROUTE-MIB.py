_L='staticRouteGroup'
_K='blackHoleRoute'
_J='staticRouteAction'
_I='nextHopIntf'
_H='prefixLength'
_G='nextHop'
_F='destinationIP'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-STATICROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
infnNE,=mibBuilder.importSymbols('INFINERA-REG-MIB','infnNE')
InfnBlackHoleRouteStatus,InfnStaticRouteAction=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnBlackHoleRouteStatus','InfnStaticRouteAction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
staticRouteMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,8,5))
if mibBuilder.loadTexts:staticRouteMIB.setRevisions(('2017-07-18 00:00',))
_StaticRouteTable_Object=MibTable
staticRouteTable=_StaticRouteTable_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1))
if mibBuilder.loadTexts:staticRouteTable.setStatus(_A)
_StaticRouteEntry_Object=MibTableRow
staticRouteEntry=_StaticRouteEntry_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1))
staticRouteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:staticRouteEntry.setStatus(_A)
_MoID_Type=DisplayString
_MoID_Object=MibTableColumn
moID=_MoID_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,1),_MoID_Type())
moID.setMaxAccess(_C)
if mibBuilder.loadTexts:moID.setStatus(_A)
_DestinationIP_Type=DisplayString
_DestinationIP_Object=MibTableColumn
destinationIP=_DestinationIP_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,2),_DestinationIP_Type())
destinationIP.setMaxAccess(_C)
if mibBuilder.loadTexts:destinationIP.setStatus(_A)
_NextHop_Type=DisplayString
_NextHop_Object=MibTableColumn
nextHop=_NextHop_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,3),_NextHop_Type())
nextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:nextHop.setStatus(_A)
_PrefixLength_Type=Unsigned32
_PrefixLength_Object=MibTableColumn
prefixLength=_PrefixLength_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,4),_PrefixLength_Type())
prefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixLength.setStatus(_A)
_NextHopIntf_Type=DisplayString
_NextHopIntf_Object=MibTableColumn
nextHopIntf=_NextHopIntf_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,5),_NextHopIntf_Type())
nextHopIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:nextHopIntf.setStatus(_A)
_Cost_Type=Unsigned32
_Cost_Object=MibTableColumn
cost=_Cost_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,6),_Cost_Type())
cost.setMaxAccess(_C)
if mibBuilder.loadTexts:cost.setStatus(_A)
_StaticRouteAction_Type=InfnStaticRouteAction
_StaticRouteAction_Object=MibTableColumn
staticRouteAction=_StaticRouteAction_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,7),_StaticRouteAction_Type())
staticRouteAction.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRouteAction.setStatus(_A)
_BlackHoleRoute_Type=InfnBlackHoleRouteStatus
_BlackHoleRoute_Object=MibTableColumn
blackHoleRoute=_BlackHoleRoute_Object((1,3,6,1,4,1,21296,2,2,1,8,5,1,1,8),_BlackHoleRoute_Type())
blackHoleRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:blackHoleRoute.setStatus(_A)
_StaticRouteConformance_ObjectIdentity=ObjectIdentity
staticRouteConformance=_StaticRouteConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8,5,2))
_StaticRouteCompliances_ObjectIdentity=ObjectIdentity
staticRouteCompliances=_StaticRouteCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8,5,2,1))
_StaticRouteGroups_ObjectIdentity=ObjectIdentity
staticRouteGroups=_StaticRouteGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8,5,2,2))
staticRouteGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,8,5,2,2,1))
staticRouteGroup.setObjects(*((_B,'moID'),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,'cost'),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:staticRouteGroup.setStatus(_A)
staticRouteCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,8,5,2,1,1))
staticRouteCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:staticRouteCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'staticRouteMIB':staticRouteMIB,'staticRouteTable':staticRouteTable,'staticRouteEntry':staticRouteEntry,'moID':moID,_F:destinationIP,_G:nextHop,_H:prefixLength,_I:nextHopIntf,'cost':cost,_J:staticRouteAction,_K:blackHoleRoute,'staticRouteConformance':staticRouteConformance,'staticRouteCompliances':staticRouteCompliances,'staticRouteCompliance':staticRouteCompliance,'staticRouteGroups':staticRouteGroups,_L:staticRouteGroup})