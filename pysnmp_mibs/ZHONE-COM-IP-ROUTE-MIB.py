_L='zhoneRouteInfoEntry'
_K='zhIpCidrRouteNextHop'
_J='zhIpCidrRouteMask'
_I='zhIpCidrRouteDest'
_H='rdIndex'
_G='ZHONE-COM-IP-RD-MIB'
_F='not-accessible'
_E='read-only'
_D='ZHONE-COM-IP-ROUTE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdEntry,rdIndex=mibBuilder.importSymbols(_G,'rdEntry',_H)
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
comIpRoute=ModuleIdentity((1,3,6,1,4,1,5504,6,57))
if mibBuilder.loadTexts:comIpRoute.setRevisions(('2000-09-11 16:33',))
_Route_ObjectIdentity=ObjectIdentity
route=_Route_ObjectIdentity((1,3,6,1,4,1,5504,4,1,7))
if mibBuilder.loadTexts:route.setStatus(_A)
_ZhoneRouteInfoTable_Object=MibTable
zhoneRouteInfoTable=_ZhoneRouteInfoTable_Object((1,3,6,1,4,1,5504,4,1,7,1))
if mibBuilder.loadTexts:zhoneRouteInfoTable.setStatus(_A)
_ZhoneRouteInfoEntry_Object=MibTableRow
zhoneRouteInfoEntry=_ZhoneRouteInfoEntry_Object((1,3,6,1,4,1,5504,4,1,7,1,1))
if mibBuilder.loadTexts:zhoneRouteInfoEntry.setStatus(_A)
_ZhIpCidrRouteNumber_Type=Gauge32
_ZhIpCidrRouteNumber_Object=MibTableColumn
zhIpCidrRouteNumber=_ZhIpCidrRouteNumber_Object((1,3,6,1,4,1,5504,4,1,7,1,1,1),_ZhIpCidrRouteNumber_Type())
zhIpCidrRouteNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:zhIpCidrRouteNumber.setStatus(_A)
_ZhoneIpCidrRouteTable_Object=MibTable
zhoneIpCidrRouteTable=_ZhoneIpCidrRouteTable_Object((1,3,6,1,4,1,5504,4,1,7,3))
if mibBuilder.loadTexts:zhoneIpCidrRouteTable.setStatus(_A)
_ZhoneIpCidrRouteEntry_Object=MibTableRow
zhoneIpCidrRouteEntry=_ZhoneIpCidrRouteEntry_Object((1,3,6,1,4,1,5504,4,1,7,3,1))
zhoneIpCidrRouteEntry.setIndexNames((0,_G,_H),(0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:zhoneIpCidrRouteEntry.setStatus(_A)
_ZhIpCidrRouteDest_Type=IpAddress
_ZhIpCidrRouteDest_Object=MibTableColumn
zhIpCidrRouteDest=_ZhIpCidrRouteDest_Object((1,3,6,1,4,1,5504,4,1,7,3,1,1),_ZhIpCidrRouteDest_Type())
zhIpCidrRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:zhIpCidrRouteDest.setStatus(_A)
_ZhIpCidrRouteMask_Type=IpAddress
_ZhIpCidrRouteMask_Object=MibTableColumn
zhIpCidrRouteMask=_ZhIpCidrRouteMask_Object((1,3,6,1,4,1,5504,4,1,7,3,1,2),_ZhIpCidrRouteMask_Type())
zhIpCidrRouteMask.setMaxAccess(_F)
if mibBuilder.loadTexts:zhIpCidrRouteMask.setStatus(_A)
_ZhIpCidrRouteNextHop_Type=IpAddress
_ZhIpCidrRouteNextHop_Object=MibTableColumn
zhIpCidrRouteNextHop=_ZhIpCidrRouteNextHop_Object((1,3,6,1,4,1,5504,4,1,7,3,1,3),_ZhIpCidrRouteNextHop_Type())
zhIpCidrRouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:zhIpCidrRouteNextHop.setStatus(_A)
_ZhIpCidrRouteIfIndex_Type=InterfaceIndexOrZero
_ZhIpCidrRouteIfIndex_Object=MibTableColumn
zhIpCidrRouteIfIndex=_ZhIpCidrRouteIfIndex_Object((1,3,6,1,4,1,5504,4,1,7,3,1,4),_ZhIpCidrRouteIfIndex_Type())
zhIpCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteIfIndex.setStatus(_A)
class _ZhIpCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('reject',2),('local',3),('remote',4)))
_ZhIpCidrRouteType_Type.__name__=_B
_ZhIpCidrRouteType_Object=MibTableColumn
zhIpCidrRouteType=_ZhIpCidrRouteType_Object((1,3,6,1,4,1,5504,4,1,7,3,1,5),_ZhIpCidrRouteType_Type())
zhIpCidrRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteType.setStatus(_A)
class _ZhIpCidrRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8,9,13,14,15)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('icmp',4),('rip',8),('isIs',9),('ospf',13),('bgp',14),('idpr',15)))
_ZhIpCidrRouteProto_Type.__name__=_B
_ZhIpCidrRouteProto_Object=MibTableColumn
zhIpCidrRouteProto=_ZhIpCidrRouteProto_Object((1,3,6,1,4,1,5504,4,1,7,3,1,6),_ZhIpCidrRouteProto_Type())
zhIpCidrRouteProto.setMaxAccess(_E)
if mibBuilder.loadTexts:zhIpCidrRouteProto.setStatus(_A)
_ZhIpCidrRouteAge_Type=Unsigned32
_ZhIpCidrRouteAge_Object=MibTableColumn
zhIpCidrRouteAge=_ZhIpCidrRouteAge_Object((1,3,6,1,4,1,5504,4,1,7,3,1,7),_ZhIpCidrRouteAge_Type())
zhIpCidrRouteAge.setMaxAccess(_E)
if mibBuilder.loadTexts:zhIpCidrRouteAge.setStatus(_A)
if mibBuilder.loadTexts:zhIpCidrRouteAge.setUnits('seconds')
_ZhIpCidrRouteInfo_Type=ObjectIdentifier
_ZhIpCidrRouteInfo_Object=MibTableColumn
zhIpCidrRouteInfo=_ZhIpCidrRouteInfo_Object((1,3,6,1,4,1,5504,4,1,7,3,1,8),_ZhIpCidrRouteInfo_Type())
zhIpCidrRouteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteInfo.setStatus(_A)
class _ZhIpCidrRouteNextHopAS_Type(Integer32):defaultValue=0
_ZhIpCidrRouteNextHopAS_Type.__name__=_B
_ZhIpCidrRouteNextHopAS_Object=MibTableColumn
zhIpCidrRouteNextHopAS=_ZhIpCidrRouteNextHopAS_Object((1,3,6,1,4,1,5504,4,1,7,3,1,9),_ZhIpCidrRouteNextHopAS_Type())
zhIpCidrRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteNextHopAS.setStatus(_A)
class _ZhIpCidrRouteMetric1_Type(Integer32):defaultValue=-1
_ZhIpCidrRouteMetric1_Type.__name__=_B
_ZhIpCidrRouteMetric1_Object=MibTableColumn
zhIpCidrRouteMetric1=_ZhIpCidrRouteMetric1_Object((1,3,6,1,4,1,5504,4,1,7,3,1,10),_ZhIpCidrRouteMetric1_Type())
zhIpCidrRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteMetric1.setStatus(_A)
class _ZhIpCidrRouteMetric2_Type(Integer32):defaultValue=-1
_ZhIpCidrRouteMetric2_Type.__name__=_B
_ZhIpCidrRouteMetric2_Object=MibTableColumn
zhIpCidrRouteMetric2=_ZhIpCidrRouteMetric2_Object((1,3,6,1,4,1,5504,4,1,7,3,1,11),_ZhIpCidrRouteMetric2_Type())
zhIpCidrRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteMetric2.setStatus(_A)
class _ZhIpCidrRouteMetric3_Type(Integer32):defaultValue=-1
_ZhIpCidrRouteMetric3_Type.__name__=_B
_ZhIpCidrRouteMetric3_Object=MibTableColumn
zhIpCidrRouteMetric3=_ZhIpCidrRouteMetric3_Object((1,3,6,1,4,1,5504,4,1,7,3,1,12),_ZhIpCidrRouteMetric3_Type())
zhIpCidrRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteMetric3.setStatus(_A)
class _ZhIpCidrRouteMetric4_Type(Integer32):defaultValue=-1
_ZhIpCidrRouteMetric4_Type.__name__=_B
_ZhIpCidrRouteMetric4_Object=MibTableColumn
zhIpCidrRouteMetric4=_ZhIpCidrRouteMetric4_Object((1,3,6,1,4,1,5504,4,1,7,3,1,13),_ZhIpCidrRouteMetric4_Type())
zhIpCidrRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteMetric4.setStatus(_A)
class _ZhIpCidrRouteMetric5_Type(Integer32):defaultValue=-1
_ZhIpCidrRouteMetric5_Type.__name__=_B
_ZhIpCidrRouteMetric5_Object=MibTableColumn
zhIpCidrRouteMetric5=_ZhIpCidrRouteMetric5_Object((1,3,6,1,4,1,5504,4,1,7,3,1,14),_ZhIpCidrRouteMetric5_Type())
zhIpCidrRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:zhIpCidrRouteMetric5.setStatus(_A)
rdEntry.registerAugmentions((_D,_L))
zhoneRouteInfoEntry.setIndexNames(*rdEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'route':route,'zhoneRouteInfoTable':zhoneRouteInfoTable,_L:zhoneRouteInfoEntry,'zhIpCidrRouteNumber':zhIpCidrRouteNumber,'zhoneIpCidrRouteTable':zhoneIpCidrRouteTable,'zhoneIpCidrRouteEntry':zhoneIpCidrRouteEntry,_I:zhIpCidrRouteDest,_J:zhIpCidrRouteMask,_K:zhIpCidrRouteNextHop,'zhIpCidrRouteIfIndex':zhIpCidrRouteIfIndex,'zhIpCidrRouteType':zhIpCidrRouteType,'zhIpCidrRouteProto':zhIpCidrRouteProto,'zhIpCidrRouteAge':zhIpCidrRouteAge,'zhIpCidrRouteInfo':zhIpCidrRouteInfo,'zhIpCidrRouteNextHopAS':zhIpCidrRouteNextHopAS,'zhIpCidrRouteMetric1':zhIpCidrRouteMetric1,'zhIpCidrRouteMetric2':zhIpCidrRouteMetric2,'zhIpCidrRouteMetric3':zhIpCidrRouteMetric3,'zhIpCidrRouteMetric4':zhIpCidrRouteMetric4,'zhIpCidrRouteMetric5':zhIpCidrRouteMetric5,'comIpRoute':comIpRoute})