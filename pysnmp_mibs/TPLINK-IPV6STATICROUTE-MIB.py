_I='tpIPv6StaticRouteItemNexthop'
_H='tpIPv6StaticRouteItemPrefixLen'
_G='tpIPv6StaticRouteItemDesIp'
_F='OctetString'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='TPLINK-IPV6STATICROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkIPv6StaticRouteMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,53))
if mibBuilder.loadTexts:tplinkIPv6StaticRouteMIB.setRevisions(('2012-12-13 09:30',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TplinkIPv6StaticRouteMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIPv6StaticRouteMIBObjects=_TplinkIPv6StaticRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,53,1))
_TpIPv6StaticRouteConfig_ObjectIdentity=ObjectIdentity
tpIPv6StaticRouteConfig=_TpIPv6StaticRouteConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,53,1,1))
_TpIPv6StaticRouteConfigTable_Object=MibTable
tpIPv6StaticRouteConfigTable=_TpIPv6StaticRouteConfigTable_Object((1,3,6,1,4,1,11863,6,53,1,1,1))
if mibBuilder.loadTexts:tpIPv6StaticRouteConfigTable.setStatus(_A)
_TpIPv6StaticRouteConfigEntry_Object=MibTableRow
tpIPv6StaticRouteConfigEntry=_TpIPv6StaticRouteConfigEntry_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1))
tpIPv6StaticRouteConfigEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:tpIPv6StaticRouteConfigEntry.setStatus(_A)
_TpIPv6StaticRouteItemDesIp_Type=InetAddress
_TpIPv6StaticRouteItemDesIp_Object=MibTableColumn
tpIPv6StaticRouteItemDesIp=_TpIPv6StaticRouteItemDesIp_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1,1),_TpIPv6StaticRouteItemDesIp_Type())
tpIPv6StaticRouteItemDesIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIPv6StaticRouteItemDesIp.setStatus(_A)
class _TpIPv6StaticRouteItemPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_TpIPv6StaticRouteItemPrefixLen_Type.__name__=_C
_TpIPv6StaticRouteItemPrefixLen_Object=MibTableColumn
tpIPv6StaticRouteItemPrefixLen=_TpIPv6StaticRouteItemPrefixLen_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1,2),_TpIPv6StaticRouteItemPrefixLen_Type())
tpIPv6StaticRouteItemPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIPv6StaticRouteItemPrefixLen.setStatus(_A)
_TpIPv6StaticRouteItemNexthop_Type=InetAddress
_TpIPv6StaticRouteItemNexthop_Object=MibTableColumn
tpIPv6StaticRouteItemNexthop=_TpIPv6StaticRouteItemNexthop_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1,3),_TpIPv6StaticRouteItemNexthop_Type())
tpIPv6StaticRouteItemNexthop.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIPv6StaticRouteItemNexthop.setStatus(_A)
class _TpIPv6StaticRouteItemDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpIPv6StaticRouteItemDistance_Type.__name__=_C
_TpIPv6StaticRouteItemDistance_Object=MibTableColumn
tpIPv6StaticRouteItemDistance=_TpIPv6StaticRouteItemDistance_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1,4),_TpIPv6StaticRouteItemDistance_Type())
tpIPv6StaticRouteItemDistance.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIPv6StaticRouteItemDistance.setStatus(_A)
class _TpIPv6StaticRouteItemInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpIPv6StaticRouteItemInterfaceName_Type.__name__=_F
_TpIPv6StaticRouteItemInterfaceName_Object=MibTableColumn
tpIPv6StaticRouteItemInterfaceName=_TpIPv6StaticRouteItemInterfaceName_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1,5),_TpIPv6StaticRouteItemInterfaceName_Type())
tpIPv6StaticRouteItemInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIPv6StaticRouteItemInterfaceName.setStatus(_A)
_TpIPv6StaticRouteItemStatus_Type=TPRowStatus
_TpIPv6StaticRouteItemStatus_Object=MibTableColumn
tpIPv6StaticRouteItemStatus=_TpIPv6StaticRouteItemStatus_Object((1,3,6,1,4,1,11863,6,53,1,1,1,1,6),_TpIPv6StaticRouteItemStatus_Type())
tpIPv6StaticRouteItemStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIPv6StaticRouteItemStatus.setStatus(_A)
_TplinkIPv6StaticRouteNotifications_ObjectIdentity=ObjectIdentity
tplinkIPv6StaticRouteNotifications=_TplinkIPv6StaticRouteNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,53,2))
mibBuilder.exportSymbols(_B,**{'MacAddress':MacAddress,'tplinkIPv6StaticRouteMIB':tplinkIPv6StaticRouteMIB,'tplinkIPv6StaticRouteMIBObjects':tplinkIPv6StaticRouteMIBObjects,'tpIPv6StaticRouteConfig':tpIPv6StaticRouteConfig,'tpIPv6StaticRouteConfigTable':tpIPv6StaticRouteConfigTable,'tpIPv6StaticRouteConfigEntry':tpIPv6StaticRouteConfigEntry,_G:tpIPv6StaticRouteItemDesIp,_H:tpIPv6StaticRouteItemPrefixLen,_I:tpIPv6StaticRouteItemNexthop,'tpIPv6StaticRouteItemDistance':tpIPv6StaticRouteItemDistance,'tpIPv6StaticRouteItemInterfaceName':tpIPv6StaticRouteItemInterfaceName,'tpIPv6StaticRouteItemStatus':tpIPv6StaticRouteItemStatus,'tplinkIPv6StaticRouteNotifications':tplinkIPv6StaticRouteNotifications})