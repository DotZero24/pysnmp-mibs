_G='tpIpv6BindingIp'
_F='TPLINK-IPV6MACBINDING-MIB'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkIpv6MacBindingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,69))
if mibBuilder.loadTexts:tplinkIpv6MacBindingMIB.setRevisions(('2012-12-17 10:14',))
_TplinkIpv6MacBindingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpv6MacBindingMIBObjects=_TplinkIpv6MacBindingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,69,1))
_TpIpv6MacBindigConfigure_ObjectIdentity=ObjectIdentity
tpIpv6MacBindigConfigure=_TpIpv6MacBindigConfigure_ObjectIdentity((1,3,6,1,4,1,11863,6,69,1,1))
_TpIpv6MacBindingTable_Object=MibTable
tpIpv6MacBindingTable=_TpIpv6MacBindingTable_Object((1,3,6,1,4,1,11863,6,69,1,1,1))
if mibBuilder.loadTexts:tpIpv6MacBindingTable.setStatus(_A)
_TpIpv6MacBindingEntry_Object=MibTableRow
tpIpv6MacBindingEntry=_TpIpv6MacBindingEntry_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1))
tpIpv6MacBindingEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpIpv6MacBindingEntry.setStatus(_A)
class _TpIpv6BindingHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TpIpv6BindingHostName_Type.__name__=_B
_TpIpv6BindingHostName_Object=MibTableColumn
tpIpv6BindingHostName=_TpIpv6BindingHostName_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,1),_TpIpv6BindingHostName_Type())
tpIpv6BindingHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIpv6BindingHostName.setStatus(_A)
_TpIpv6BindingIp_Type=InetAddress
_TpIpv6BindingIp_Object=MibTableColumn
tpIpv6BindingIp=_TpIpv6BindingIp_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,2),_TpIpv6BindingIp_Type())
tpIpv6BindingIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIpv6BindingIp.setStatus(_A)
class _TpIpv6BindingMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_TpIpv6BindingMac_Type.__name__=_B
_TpIpv6BindingMac_Object=MibTableColumn
tpIpv6BindingMac=_TpIpv6BindingMac_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,3),_TpIpv6BindingMac_Type())
tpIpv6BindingMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIpv6BindingMac.setStatus(_A)
_TpIpv6BindingVlanId_Type=Integer32
_TpIpv6BindingVlanId_Object=MibTableColumn
tpIpv6BindingVlanId=_TpIpv6BindingVlanId_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,4),_TpIpv6BindingVlanId_Type())
tpIpv6BindingVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIpv6BindingVlanId.setStatus(_A)
class _TpIpv6BindingPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TpIpv6BindingPort_Type.__name__=_B
_TpIpv6BindingPort_Object=MibTableColumn
tpIpv6BindingPort=_TpIpv6BindingPort_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,5),_TpIpv6BindingPort_Type())
tpIpv6BindingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIpv6BindingPort.setStatus(_A)
class _TpIpv6BindingProtectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('nd-detection',1),('ipv6-source-guard',2),('both',3)))
_TpIpv6BindingProtectType_Type.__name__=_D
_TpIpv6BindingProtectType_Object=MibTableColumn
tpIpv6BindingProtectType=_TpIpv6BindingProtectType_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,6),_TpIpv6BindingProtectType_Type())
tpIpv6BindingProtectType.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIpv6BindingProtectType.setStatus(_A)
class _TpIpv6BindingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcp-snooping',2),('nd-snooping',3)))
_TpIpv6BindingSource_Type.__name__=_D
_TpIpv6BindingSource_Object=MibTableColumn
tpIpv6BindingSource=_TpIpv6BindingSource_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,7),_TpIpv6BindingSource_Type())
tpIpv6BindingSource.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpIpv6BindingSource.setStatus(_A)
_TpIpv6BindingRowStatus_Type=TPRowStatus
_TpIpv6BindingRowStatus_Object=MibTableColumn
tpIpv6BindingRowStatus=_TpIpv6BindingRowStatus_Object((1,3,6,1,4,1,11863,6,69,1,1,1,1,8),_TpIpv6BindingRowStatus_Type())
tpIpv6BindingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIpv6BindingRowStatus.setStatus(_A)
_TplinkIpv6MacBindingNotifications_ObjectIdentity=ObjectIdentity
tplinkIpv6MacBindingNotifications=_TplinkIpv6MacBindingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,69,2))
mibBuilder.exportSymbols(_F,**{'tplinkIpv6MacBindingMIB':tplinkIpv6MacBindingMIB,'tplinkIpv6MacBindingMIBObjects':tplinkIpv6MacBindingMIBObjects,'tpIpv6MacBindigConfigure':tpIpv6MacBindigConfigure,'tpIpv6MacBindingTable':tpIpv6MacBindingTable,'tpIpv6MacBindingEntry':tpIpv6MacBindingEntry,'tpIpv6BindingHostName':tpIpv6BindingHostName,_G:tpIpv6BindingIp,'tpIpv6BindingMac':tpIpv6BindingMac,'tpIpv6BindingVlanId':tpIpv6BindingVlanId,'tpIpv6BindingPort':tpIpv6BindingPort,'tpIpv6BindingProtectType':tpIpv6BindingProtectType,'tpIpv6BindingSource':tpIpv6BindingSource,'tpIpv6BindingRowStatus':tpIpv6BindingRowStatus,'tplinkIpv6MacBindingNotifications':tplinkIpv6MacBindingNotifications})