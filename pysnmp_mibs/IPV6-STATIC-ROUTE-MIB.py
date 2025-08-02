_N='static'
_M='swIPv6NeighborCacheInterfaceName'
_L='swIPv6NeighborCacheMacAddress'
_K='swIPv6NeighborCacheIPv6Address'
_J='swIPv6StaticRouteNextHop'
_I='swIPv6StaticRouteInterfaceName'
_H='swIPv6StaticRoutePrefixLen'
_G='swIPv6StaticRouteDest'
_F='DisplayString'
_E='read-create'
_D='Integer32'
_C='IPV6-STATIC-ROUTE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swIPv6StaticRouteMIB=ModuleIdentity((1,3,6,1,4,1,171,12,26))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwIPv6StaticRouteCtrl_ObjectIdentity=ObjectIdentity
swIPv6StaticRouteCtrl=_SwIPv6StaticRouteCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,26,1))
_SwIPv6StaticRouteInfo_ObjectIdentity=ObjectIdentity
swIPv6StaticRouteInfo=_SwIPv6StaticRouteInfo_ObjectIdentity((1,3,6,1,4,1,171,12,26,2))
_SwIPv6StaticRouteMgmt_ObjectIdentity=ObjectIdentity
swIPv6StaticRouteMgmt=_SwIPv6StaticRouteMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,26,3))
_SwIPv6StaticRouteTable_Object=MibTable
swIPv6StaticRouteTable=_SwIPv6StaticRouteTable_Object((1,3,6,1,4,1,171,12,26,3,1))
if mibBuilder.loadTexts:swIPv6StaticRouteTable.setStatus(_A)
_SwIPv6StaticRouteEntry_Object=MibTableRow
swIPv6StaticRouteEntry=_SwIPv6StaticRouteEntry_Object((1,3,6,1,4,1,171,12,26,3,1,1))
swIPv6StaticRouteEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:swIPv6StaticRouteEntry.setStatus(_A)
_SwIPv6StaticRouteDest_Type=Ipv6Address
_SwIPv6StaticRouteDest_Object=MibTableColumn
swIPv6StaticRouteDest=_SwIPv6StaticRouteDest_Object((1,3,6,1,4,1,171,12,26,3,1,1,1),_SwIPv6StaticRouteDest_Type())
swIPv6StaticRouteDest.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6StaticRouteDest.setStatus(_A)
class _SwIPv6StaticRoutePrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_SwIPv6StaticRoutePrefixLen_Type.__name__=_D
_SwIPv6StaticRoutePrefixLen_Object=MibTableColumn
swIPv6StaticRoutePrefixLen=_SwIPv6StaticRoutePrefixLen_Object((1,3,6,1,4,1,171,12,26,3,1,1,2),_SwIPv6StaticRoutePrefixLen_Type())
swIPv6StaticRoutePrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6StaticRoutePrefixLen.setStatus(_A)
class _SwIPv6StaticRouteInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwIPv6StaticRouteInterfaceName_Type.__name__=_F
_SwIPv6StaticRouteInterfaceName_Object=MibTableColumn
swIPv6StaticRouteInterfaceName=_SwIPv6StaticRouteInterfaceName_Object((1,3,6,1,4,1,171,12,26,3,1,1,3),_SwIPv6StaticRouteInterfaceName_Type())
swIPv6StaticRouteInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6StaticRouteInterfaceName.setStatus(_A)
_SwIPv6StaticRouteNextHop_Type=Ipv6Address
_SwIPv6StaticRouteNextHop_Object=MibTableColumn
swIPv6StaticRouteNextHop=_SwIPv6StaticRouteNextHop_Object((1,3,6,1,4,1,171,12,26,3,1,1,4),_SwIPv6StaticRouteNextHop_Type())
swIPv6StaticRouteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6StaticRouteNextHop.setStatus(_A)
class _SwIPv6StaticRouteMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwIPv6StaticRouteMetric_Type.__name__=_D
_SwIPv6StaticRouteMetric_Object=MibTableColumn
swIPv6StaticRouteMetric=_SwIPv6StaticRouteMetric_Object((1,3,6,1,4,1,171,12,26,3,1,1,5),_SwIPv6StaticRouteMetric_Type())
swIPv6StaticRouteMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:swIPv6StaticRouteMetric.setStatus(_A)
class _SwIPv6StaticRouteWeight_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SwIPv6StaticRouteWeight_Type.__name__=_D
_SwIPv6StaticRouteWeight_Object=MibTableColumn
swIPv6StaticRouteWeight=_SwIPv6StaticRouteWeight_Object((1,3,6,1,4,1,171,12,26,3,1,1,6),_SwIPv6StaticRouteWeight_Type())
swIPv6StaticRouteWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:swIPv6StaticRouteWeight.setStatus(_A)
_SwIPv6StaticProtocol_Type=DisplayString
_SwIPv6StaticProtocol_Object=MibTableColumn
swIPv6StaticProtocol=_SwIPv6StaticProtocol_Object((1,3,6,1,4,1,171,12,26,3,1,1,7),_SwIPv6StaticProtocol_Type())
swIPv6StaticProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6StaticProtocol.setStatus(_A)
_SwIPv6StaticRouteStatus_Type=RowStatus
_SwIPv6StaticRouteStatus_Object=MibTableColumn
swIPv6StaticRouteStatus=_SwIPv6StaticRouteStatus_Object((1,3,6,1,4,1,171,12,26,3,1,1,8),_SwIPv6StaticRouteStatus_Type())
swIPv6StaticRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swIPv6StaticRouteStatus.setStatus(_A)
class _SwIPv6StaticRouteBkupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('backup',2),('none',3)))
_SwIPv6StaticRouteBkupState_Type.__name__=_D
_SwIPv6StaticRouteBkupState_Object=MibTableColumn
swIPv6StaticRouteBkupState=_SwIPv6StaticRouteBkupState_Object((1,3,6,1,4,1,171,12,26,3,1,1,9),_SwIPv6StaticRouteBkupState_Type())
swIPv6StaticRouteBkupState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIPv6StaticRouteBkupState.setStatus(_A)
_SwIPv6NeighborCacheMgmt_ObjectIdentity=ObjectIdentity
swIPv6NeighborCacheMgmt=_SwIPv6NeighborCacheMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,26,4))
_SwIPv6NeighborCacheTable_Object=MibTable
swIPv6NeighborCacheTable=_SwIPv6NeighborCacheTable_Object((1,3,6,1,4,1,171,12,26,4,1))
if mibBuilder.loadTexts:swIPv6NeighborCacheTable.setStatus(_A)
_SwIPv6NeighborCacheEntry_Object=MibTableRow
swIPv6NeighborCacheEntry=_SwIPv6NeighborCacheEntry_Object((1,3,6,1,4,1,171,12,26,4,1,1))
swIPv6NeighborCacheEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:swIPv6NeighborCacheEntry.setStatus(_A)
_SwIPv6NeighborCacheIPv6Address_Type=Ipv6Address
_SwIPv6NeighborCacheIPv6Address_Object=MibTableColumn
swIPv6NeighborCacheIPv6Address=_SwIPv6NeighborCacheIPv6Address_Object((1,3,6,1,4,1,171,12,26,4,1,1,1),_SwIPv6NeighborCacheIPv6Address_Type())
swIPv6NeighborCacheIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6NeighborCacheIPv6Address.setStatus(_A)
_SwIPv6NeighborCacheMacAddress_Type=MacAddress
_SwIPv6NeighborCacheMacAddress_Object=MibTableColumn
swIPv6NeighborCacheMacAddress=_SwIPv6NeighborCacheMacAddress_Object((1,3,6,1,4,1,171,12,26,4,1,1,2),_SwIPv6NeighborCacheMacAddress_Type())
swIPv6NeighborCacheMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6NeighborCacheMacAddress.setStatus(_A)
class _SwIPv6NeighborCacheInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwIPv6NeighborCacheInterfaceName_Type.__name__=_F
_SwIPv6NeighborCacheInterfaceName_Object=MibTableColumn
swIPv6NeighborCacheInterfaceName=_SwIPv6NeighborCacheInterfaceName_Object((1,3,6,1,4,1,171,12,26,4,1,1,3),_SwIPv6NeighborCacheInterfaceName_Type())
swIPv6NeighborCacheInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6NeighborCacheInterfaceName.setStatus(_A)
class _SwIPv6NeighborCacheReachState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('incomplete',1),('reachable',2),('stale',3),('delay',4),('probe',5),(_N,6)))
_SwIPv6NeighborCacheReachState_Type.__name__=_D
_SwIPv6NeighborCacheReachState_Object=MibTableColumn
swIPv6NeighborCacheReachState=_SwIPv6NeighborCacheReachState_Object((1,3,6,1,4,1,171,12,26,4,1,1,4),_SwIPv6NeighborCacheReachState_Type())
swIPv6NeighborCacheReachState.setMaxAccess(_B)
if mibBuilder.loadTexts:swIPv6NeighborCacheReachState.setStatus(_A)
_SwIPv6NeighborCacheRouteStatus_Type=RowStatus
_SwIPv6NeighborCacheRouteStatus_Object=MibTableColumn
swIPv6NeighborCacheRouteStatus=_SwIPv6NeighborCacheRouteStatus_Object((1,3,6,1,4,1,171,12,26,4,1,1,5),_SwIPv6NeighborCacheRouteStatus_Type())
swIPv6NeighborCacheRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swIPv6NeighborCacheRouteStatus.setStatus(_A)
class _SwIPv6NeighborCacheDeleteAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),(_N,2),('dynamic',3),('other',4)))
_SwIPv6NeighborCacheDeleteAction_Type.__name__=_D
_SwIPv6NeighborCacheDeleteAction_Object=MibScalar
swIPv6NeighborCacheDeleteAction=_SwIPv6NeighborCacheDeleteAction_Object((1,3,6,1,4,1,171,12,26,4,2),_SwIPv6NeighborCacheDeleteAction_Type())
swIPv6NeighborCacheDeleteAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:swIPv6NeighborCacheDeleteAction.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Ipv6Address':Ipv6Address,'swIPv6StaticRouteMIB':swIPv6StaticRouteMIB,'swIPv6StaticRouteCtrl':swIPv6StaticRouteCtrl,'swIPv6StaticRouteInfo':swIPv6StaticRouteInfo,'swIPv6StaticRouteMgmt':swIPv6StaticRouteMgmt,'swIPv6StaticRouteTable':swIPv6StaticRouteTable,'swIPv6StaticRouteEntry':swIPv6StaticRouteEntry,_G:swIPv6StaticRouteDest,_H:swIPv6StaticRoutePrefixLen,_I:swIPv6StaticRouteInterfaceName,_J:swIPv6StaticRouteNextHop,'swIPv6StaticRouteMetric':swIPv6StaticRouteMetric,'swIPv6StaticRouteWeight':swIPv6StaticRouteWeight,'swIPv6StaticProtocol':swIPv6StaticProtocol,'swIPv6StaticRouteStatus':swIPv6StaticRouteStatus,'swIPv6StaticRouteBkupState':swIPv6StaticRouteBkupState,'swIPv6NeighborCacheMgmt':swIPv6NeighborCacheMgmt,'swIPv6NeighborCacheTable':swIPv6NeighborCacheTable,'swIPv6NeighborCacheEntry':swIPv6NeighborCacheEntry,_K:swIPv6NeighborCacheIPv6Address,_L:swIPv6NeighborCacheMacAddress,_M:swIPv6NeighborCacheInterfaceName,'swIPv6NeighborCacheReachState':swIPv6NeighborCacheReachState,'swIPv6NeighborCacheRouteStatus':swIPv6NeighborCacheRouteStatus,'swIPv6NeighborCacheDeleteAction':swIPv6NeighborCacheDeleteAction})