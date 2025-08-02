_M='staticRouteType'
_L='staticRouteIfNumber'
_K='staticRouteNextHop'
_J='staticRouteNetMask'
_I='staticRouteDest'
_H='rdIndex'
_G='ZHONE-COM-IP-RD-MIB'
_F='Unsigned32'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='ZHONE-COM-IP-STATIC-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdIndex,=mibBuilder.importSymbols(_G,_H)
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
comIpStaticRoute=ModuleIdentity((1,3,6,1,4,1,5504,6,63))
if mibBuilder.loadTexts:comIpStaticRoute.setRevisions(('2006-07-14 15:50','2005-04-29 14:10','2000-09-12 10:23','2000-09-29 16:34'))
_StaticRoute_ObjectIdentity=ObjectIdentity
staticRoute=_StaticRoute_ObjectIdentity((1,3,6,1,4,1,5504,4,1,13))
if mibBuilder.loadTexts:staticRoute.setStatus(_A)
_StaticRouteTable_Object=MibTable
staticRouteTable=_StaticRouteTable_Object((1,3,6,1,4,1,5504,4,1,13,1))
if mibBuilder.loadTexts:staticRouteTable.setStatus(_A)
_StaticRouteEntry_Object=MibTableRow
staticRouteEntry=_StaticRouteEntry_Object((1,3,6,1,4,1,5504,4,1,13,1,1))
staticRouteEntry.setIndexNames((0,_G,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:staticRouteEntry.setStatus(_A)
_StaticRouteDest_Type=IpAddress
_StaticRouteDest_Object=MibTableColumn
staticRouteDest=_StaticRouteDest_Object((1,3,6,1,4,1,5504,4,1,13,1,1,1),_StaticRouteDest_Type())
staticRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:staticRouteDest.setStatus(_A)
_StaticRouteNetMask_Type=IpAddress
_StaticRouteNetMask_Object=MibTableColumn
staticRouteNetMask=_StaticRouteNetMask_Object((1,3,6,1,4,1,5504,4,1,13,1,1,2),_StaticRouteNetMask_Type())
staticRouteNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:staticRouteNetMask.setStatus(_A)
_StaticRouteNextHop_Type=IpAddress
_StaticRouteNextHop_Object=MibTableColumn
staticRouteNextHop=_StaticRouteNextHop_Object((1,3,6,1,4,1,5504,4,1,13,1,1,3),_StaticRouteNextHop_Type())
staticRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:staticRouteNextHop.setStatus(_A)
_StaticRouteIfNumber_Type=InterfaceIndexOrZero
_StaticRouteIfNumber_Object=MibTableColumn
staticRouteIfNumber=_StaticRouteIfNumber_Object((1,3,6,1,4,1,5504,4,1,13,1,1,4),_StaticRouteIfNumber_Type())
staticRouteIfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:staticRouteIfNumber.setStatus(_A)
class _StaticRouteMetric_Type(Unsigned32):defaultValue=2147483647
_StaticRouteMetric_Type.__name__=_F
_StaticRouteMetric_Object=MibTableColumn
staticRouteMetric=_StaticRouteMetric_Object((1,3,6,1,4,1,5504,4,1,13,1,1,5),_StaticRouteMetric_Type())
staticRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRouteMetric.setStatus(_A)
class _StaticRouteEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_StaticRouteEnable_Type.__name__=_D
_StaticRouteEnable_Object=MibTableColumn
staticRouteEnable=_StaticRouteEnable_Object((1,3,6,1,4,1,5504,4,1,13,1,1,6),_StaticRouteEnable_Type())
staticRouteEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRouteEnable.setStatus(_A)
_StaticRouteRowStatus_Type=ZhoneRowStatus
_StaticRouteRowStatus_Object=MibTableColumn
staticRouteRowStatus=_StaticRouteRowStatus_Object((1,3,6,1,4,1,5504,4,1,13,1,1,7),_StaticRouteRowStatus_Type())
staticRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRouteRowStatus.setStatus(_A)
class _StaticRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('destinationRoute',1),('sourceRoute',2)))
_StaticRouteType_Type.__name__=_D
_StaticRouteType_Object=MibTableColumn
staticRouteType=_StaticRouteType_Object((1,3,6,1,4,1,5504,4,1,13,1,1,8),_StaticRouteType_Type())
staticRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:staticRouteType.setStatus(_A)
class _StaticRouteFallbackMetric_Type(Integer32):defaultValue=0
_StaticRouteFallbackMetric_Type.__name__=_D
_StaticRouteFallbackMetric_Object=MibTableColumn
staticRouteFallbackMetric=_StaticRouteFallbackMetric_Object((1,3,6,1,4,1,5504,4,1,13,1,1,9),_StaticRouteFallbackMetric_Type())
staticRouteFallbackMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRouteFallbackMetric.setStatus(_A)
class _StaticRoutePingInterval_Type(Unsigned32):defaultValue=0
_StaticRoutePingInterval_Type.__name__=_F
_StaticRoutePingInterval_Object=MibTableColumn
staticRoutePingInterval=_StaticRoutePingInterval_Object((1,3,6,1,4,1,5504,4,1,13,1,1,10),_StaticRoutePingInterval_Type())
staticRoutePingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRoutePingInterval.setStatus(_A)
class _StaticRoutePingFailMax_Type(Integer32):defaultValue=0
_StaticRoutePingFailMax_Type.__name__=_D
_StaticRoutePingFailMax_Object=MibTableColumn
staticRoutePingFailMax=_StaticRoutePingFailMax_Object((1,3,6,1,4,1,5504,4,1,13,1,1,11),_StaticRoutePingFailMax_Type())
staticRoutePingFailMax.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRoutePingFailMax.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'staticRoute':staticRoute,'staticRouteTable':staticRouteTable,'staticRouteEntry':staticRouteEntry,_I:staticRouteDest,_J:staticRouteNetMask,_K:staticRouteNextHop,_L:staticRouteIfNumber,'staticRouteMetric':staticRouteMetric,'staticRouteEnable':staticRouteEnable,'staticRouteRowStatus':staticRouteRowStatus,_M:staticRouteType,'staticRouteFallbackMetric':staticRouteFallbackMetric,'staticRoutePingInterval':staticRoutePingInterval,'staticRoutePingFailMax':staticRoutePingFailMax,'comIpStaticRoute':comIpStaticRoute})