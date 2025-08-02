_I='tpStaticRouteItemNextIp'
_H='tpStaticRouteItemMask'
_G='tpStaticRouteItemDesIp'
_F='Integer32'
_E='OctetString'
_D='read-create'
_C='read-only'
_B='TPLINK-STATICROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkStaticRouteMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,36))
if mibBuilder.loadTexts:tplinkStaticRouteMIB.setRevisions(('2012-12-13 09:30',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TplinkStaticRouteMIBObjects_ObjectIdentity=ObjectIdentity
tplinkStaticRouteMIBObjects=_TplinkStaticRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,36,1))
_TpStaticRouteConfig_ObjectIdentity=ObjectIdentity
tpStaticRouteConfig=_TpStaticRouteConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,36,1,1))
_TpStaticRouteConfigTable_Object=MibTable
tpStaticRouteConfigTable=_TpStaticRouteConfigTable_Object((1,3,6,1,4,1,11863,6,36,1,1,1))
if mibBuilder.loadTexts:tpStaticRouteConfigTable.setStatus(_A)
_TpStaticRouteConfigEntry_Object=MibTableRow
tpStaticRouteConfigEntry=_TpStaticRouteConfigEntry_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1))
tpStaticRouteConfigEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:tpStaticRouteConfigEntry.setStatus(_A)
_TpStaticRouteItemDesIp_Type=IpAddress
_TpStaticRouteItemDesIp_Object=MibTableColumn
tpStaticRouteItemDesIp=_TpStaticRouteItemDesIp_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1,1),_TpStaticRouteItemDesIp_Type())
tpStaticRouteItemDesIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStaticRouteItemDesIp.setStatus(_A)
_TpStaticRouteItemMask_Type=IpAddress
_TpStaticRouteItemMask_Object=MibTableColumn
tpStaticRouteItemMask=_TpStaticRouteItemMask_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1,2),_TpStaticRouteItemMask_Type())
tpStaticRouteItemMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStaticRouteItemMask.setStatus(_A)
_TpStaticRouteItemNextIp_Type=IpAddress
_TpStaticRouteItemNextIp_Object=MibTableColumn
tpStaticRouteItemNextIp=_TpStaticRouteItemNextIp_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1,3),_TpStaticRouteItemNextIp_Type())
tpStaticRouteItemNextIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStaticRouteItemNextIp.setStatus(_A)
class _TpStaticRouteItemDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpStaticRouteItemDistance_Type.__name__=_F
_TpStaticRouteItemDistance_Object=MibTableColumn
tpStaticRouteItemDistance=_TpStaticRouteItemDistance_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1,4),_TpStaticRouteItemDistance_Type())
tpStaticRouteItemDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStaticRouteItemDistance.setStatus(_A)
class _TpStaticRouteItemInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStaticRouteItemInterfaceName_Type.__name__=_E
_TpStaticRouteItemInterfaceName_Object=MibTableColumn
tpStaticRouteItemInterfaceName=_TpStaticRouteItemInterfaceName_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1,5),_TpStaticRouteItemInterfaceName_Type())
tpStaticRouteItemInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStaticRouteItemInterfaceName.setStatus(_A)
_TpStaticRouteItemStatus_Type=TPRowStatus
_TpStaticRouteItemStatus_Object=MibTableColumn
tpStaticRouteItemStatus=_TpStaticRouteItemStatus_Object((1,3,6,1,4,1,11863,6,36,1,1,1,1,6),_TpStaticRouteItemStatus_Type())
tpStaticRouteItemStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStaticRouteItemStatus.setStatus(_A)
_TplinkStaticRouteNotifications_ObjectIdentity=ObjectIdentity
tplinkStaticRouteNotifications=_TplinkStaticRouteNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,36,2))
mibBuilder.exportSymbols(_B,**{'MacAddress':MacAddress,'tplinkStaticRouteMIB':tplinkStaticRouteMIB,'tplinkStaticRouteMIBObjects':tplinkStaticRouteMIBObjects,'tpStaticRouteConfig':tpStaticRouteConfig,'tpStaticRouteConfigTable':tpStaticRouteConfigTable,'tpStaticRouteConfigEntry':tpStaticRouteConfigEntry,_G:tpStaticRouteItemDesIp,_H:tpStaticRouteItemMask,_I:tpStaticRouteItemNextIp,'tpStaticRouteItemDistance':tpStaticRouteItemDistance,'tpStaticRouteItemInterfaceName':tpStaticRouteItemInterfaceName,'tpStaticRouteItemStatus':tpStaticRouteItemStatus,'tplinkStaticRouteNotifications':tplinkStaticRouteNotifications})