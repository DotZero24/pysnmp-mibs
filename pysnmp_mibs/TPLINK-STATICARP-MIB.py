_F='read-create'
_E='read-only'
_D='tpStaticARPItemIp'
_C='TPLINK-STATICARP-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkStaticARPMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,54))
if mibBuilder.loadTexts:tplinkStaticARPMIB.setRevisions(('2014-11-24 14:42',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TplinkStaticARPMIBObjects_ObjectIdentity=ObjectIdentity
tplinkStaticARPMIBObjects=_TplinkStaticARPMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,54,1))
_TpStaticARPConfig_ObjectIdentity=ObjectIdentity
tpStaticARPConfig=_TpStaticARPConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,54,1,1))
_TpStaticARPConfigTable_Object=MibTable
tpStaticARPConfigTable=_TpStaticARPConfigTable_Object((1,3,6,1,4,1,11863,6,54,1,1,1))
if mibBuilder.loadTexts:tpStaticARPConfigTable.setStatus(_A)
_TpStaticARPConfigEntry_Object=MibTableRow
tpStaticARPConfigEntry=_TpStaticARPConfigEntry_Object((1,3,6,1,4,1,11863,6,54,1,1,1,1))
tpStaticARPConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:tpStaticARPConfigEntry.setStatus(_A)
_TpStaticARPItemIp_Type=IpAddress
_TpStaticARPItemIp_Object=MibTableColumn
tpStaticARPItemIp=_TpStaticARPItemIp_Object((1,3,6,1,4,1,11863,6,54,1,1,1,1,1),_TpStaticARPItemIp_Type())
tpStaticARPItemIp.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStaticARPItemIp.setStatus(_A)
class _TpStaticARPItemMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TpStaticARPItemMac_Type.__name__=_B
_TpStaticARPItemMac_Object=MibTableColumn
tpStaticARPItemMac=_TpStaticARPItemMac_Object((1,3,6,1,4,1,11863,6,54,1,1,1,1,2),_TpStaticARPItemMac_Type())
tpStaticARPItemMac.setMaxAccess(_F)
if mibBuilder.loadTexts:tpStaticARPItemMac.setStatus(_A)
class _TpStaticArpItemInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStaticArpItemInterfaceName_Type.__name__=_B
_TpStaticArpItemInterfaceName_Object=MibTableColumn
tpStaticArpItemInterfaceName=_TpStaticArpItemInterfaceName_Object((1,3,6,1,4,1,11863,6,54,1,1,1,1,3),_TpStaticArpItemInterfaceName_Type())
tpStaticArpItemInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStaticArpItemInterfaceName.setStatus(_A)
_TpStaticARPItemStatus_Type=TPRowStatus
_TpStaticARPItemStatus_Object=MibTableColumn
tpStaticARPItemStatus=_TpStaticARPItemStatus_Object((1,3,6,1,4,1,11863,6,54,1,1,1,1,4),_TpStaticARPItemStatus_Type())
tpStaticARPItemStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tpStaticARPItemStatus.setStatus(_A)
_TplinkStaticARPNotifications_ObjectIdentity=ObjectIdentity
tplinkStaticARPNotifications=_TplinkStaticARPNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,54,2))
mibBuilder.exportSymbols(_C,**{'MacAddress':MacAddress,'tplinkStaticARPMIB':tplinkStaticARPMIB,'tplinkStaticARPMIBObjects':tplinkStaticARPMIBObjects,'tpStaticARPConfig':tpStaticARPConfig,'tpStaticARPConfigTable':tpStaticARPConfigTable,'tpStaticARPConfigEntry':tpStaticARPConfigEntry,_D:tpStaticARPItemIp,'tpStaticARPItemMac':tpStaticARPItemMac,'tpStaticArpItemInterfaceName':tpStaticArpItemInterfaceName,'tpStaticARPItemStatus':tpStaticARPItemStatus,'tplinkStaticARPNotifications':tplinkStaticARPNotifications})