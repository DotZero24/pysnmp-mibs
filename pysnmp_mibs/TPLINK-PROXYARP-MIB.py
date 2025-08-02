_F='tpProxyArpInterface'
_E='TPLINK-PROXYARP-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkProxyArpMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,37))
if mibBuilder.loadTexts:tplinkProxyArpMIB.setRevisions(('2012-12-13 09:30',))
_TplinkProxyArpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkProxyArpMIBObjects=_TplinkProxyArpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,37,1))
_TpProxyArpConfig_ObjectIdentity=ObjectIdentity
tpProxyArpConfig=_TpProxyArpConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,37,1))
_TpProxyArpTable_Object=MibTable
tpProxyArpTable=_TpProxyArpTable_Object((1,3,6,1,4,1,11863,6,37,1,1))
if mibBuilder.loadTexts:tpProxyArpTable.setStatus(_A)
_TpProxyArpEntry_Object=MibTableRow
tpProxyArpEntry=_TpProxyArpEntry_Object((1,3,6,1,4,1,11863,6,37,1,1,1))
tpProxyArpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpProxyArpEntry.setStatus(_A)
class _TpProxyArpInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpProxyArpInterface_Type.__name__=_C
_TpProxyArpInterface_Object=MibTableColumn
tpProxyArpInterface=_TpProxyArpInterface_Object((1,3,6,1,4,1,11863,6,37,1,1,1,1),_TpProxyArpInterface_Type())
tpProxyArpInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpProxyArpInterface.setStatus(_A)
_TpProxyArpIpAddr_Type=IpAddress
_TpProxyArpIpAddr_Object=MibTableColumn
tpProxyArpIpAddr=_TpProxyArpIpAddr_Object((1,3,6,1,4,1,11863,6,37,1,1,1,2),_TpProxyArpIpAddr_Type())
tpProxyArpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpProxyArpIpAddr.setStatus(_A)
_TpProxyArpIpMask_Type=IpAddress
_TpProxyArpIpMask_Object=MibTableColumn
tpProxyArpIpMask=_TpProxyArpIpMask_Object((1,3,6,1,4,1,11863,6,37,1,1,1,3),_TpProxyArpIpMask_Type())
tpProxyArpIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpProxyArpIpMask.setStatus(_A)
class _TpProxyArpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpProxyArpEnable_Type.__name__=_D
_TpProxyArpEnable_Object=MibTableColumn
tpProxyArpEnable=_TpProxyArpEnable_Object((1,3,6,1,4,1,11863,6,37,1,1,1,4),_TpProxyArpEnable_Type())
tpProxyArpEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:tpProxyArpEnable.setStatus(_A)
_TplinkProxyArpNotifications_ObjectIdentity=ObjectIdentity
tplinkProxyArpNotifications=_TplinkProxyArpNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,37,2))
mibBuilder.exportSymbols(_E,**{'tplinkProxyArpMIB':tplinkProxyArpMIB,'tplinkProxyArpMIBObjects':tplinkProxyArpMIBObjects,'tpProxyArpConfig':tpProxyArpConfig,'tpProxyArpTable':tpProxyArpTable,'tpProxyArpEntry':tpProxyArpEntry,_F:tpProxyArpInterface,'tpProxyArpIpAddr':tpProxyArpIpAddr,'tpProxyArpIpMask':tpProxyArpIpMask,'tpProxyArpEnable':tpProxyArpEnable,'tplinkProxyArpNotifications':tplinkProxyArpNotifications})