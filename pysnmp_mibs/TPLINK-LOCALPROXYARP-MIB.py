_F='tpLocalProxyArpInterface'
_E='TPLINK-LOCALPROXYARP-MIB'
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
tplinkLocalProxyArpMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,46))
if mibBuilder.loadTexts:tplinkLocalProxyArpMIB.setRevisions(('2012-12-13 09:30',))
_TplinkLocalProxyArpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkLocalProxyArpMIBObjects=_TplinkLocalProxyArpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,46,1))
_TpLocalProxyArpConfig_ObjectIdentity=ObjectIdentity
tpLocalProxyArpConfig=_TpLocalProxyArpConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,46,1))
_TpLocalProxyArpTable_Object=MibTable
tpLocalProxyArpTable=_TpLocalProxyArpTable_Object((1,3,6,1,4,1,11863,6,46,1,1))
if mibBuilder.loadTexts:tpLocalProxyArpTable.setStatus(_A)
_TpLocalProxyArpEntry_Object=MibTableRow
tpLocalProxyArpEntry=_TpLocalProxyArpEntry_Object((1,3,6,1,4,1,11863,6,46,1,1,1))
tpLocalProxyArpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpLocalProxyArpEntry.setStatus(_A)
class _TpLocalProxyArpInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpLocalProxyArpInterface_Type.__name__=_C
_TpLocalProxyArpInterface_Object=MibTableColumn
tpLocalProxyArpInterface=_TpLocalProxyArpInterface_Object((1,3,6,1,4,1,11863,6,46,1,1,1,1),_TpLocalProxyArpInterface_Type())
tpLocalProxyArpInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLocalProxyArpInterface.setStatus(_A)
_TpLocalProxyArpIpAddr_Type=IpAddress
_TpLocalProxyArpIpAddr_Object=MibTableColumn
tpLocalProxyArpIpAddr=_TpLocalProxyArpIpAddr_Object((1,3,6,1,4,1,11863,6,46,1,1,1,2),_TpLocalProxyArpIpAddr_Type())
tpLocalProxyArpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLocalProxyArpIpAddr.setStatus(_A)
_TpLocalProxyArpIpMask_Type=IpAddress
_TpLocalProxyArpIpMask_Object=MibTableColumn
tpLocalProxyArpIpMask=_TpLocalProxyArpIpMask_Object((1,3,6,1,4,1,11863,6,46,1,1,1,3),_TpLocalProxyArpIpMask_Type())
tpLocalProxyArpIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLocalProxyArpIpMask.setStatus(_A)
class _TpLocalProxyArpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpLocalProxyArpEnable_Type.__name__=_D
_TpLocalProxyArpEnable_Object=MibTableColumn
tpLocalProxyArpEnable=_TpLocalProxyArpEnable_Object((1,3,6,1,4,1,11863,6,46,1,1,1,4),_TpLocalProxyArpEnable_Type())
tpLocalProxyArpEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:tpLocalProxyArpEnable.setStatus(_A)
_TplinkLocalProxyArpNotifications_ObjectIdentity=ObjectIdentity
tplinkLocalProxyArpNotifications=_TplinkLocalProxyArpNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,46,2))
mibBuilder.exportSymbols(_E,**{'tplinkLocalProxyArpMIB':tplinkLocalProxyArpMIB,'tplinkLocalProxyArpMIBObjects':tplinkLocalProxyArpMIBObjects,'tpLocalProxyArpConfig':tpLocalProxyArpConfig,'tpLocalProxyArpTable':tpLocalProxyArpTable,'tpLocalProxyArpEntry':tpLocalProxyArpEntry,_F:tpLocalProxyArpInterface,'tpLocalProxyArpIpAddr':tpLocalProxyArpIpAddr,'tpLocalProxyArpIpMask':tpLocalProxyArpIpMask,'tpLocalProxyArpEnable':tpLocalProxyArpEnable,'tplinkLocalProxyArpNotifications':tplinkLocalProxyArpNotifications})