_G='tpBindingIp'
_F='TPLINK-IPMACBINDING-MIB'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkIpMacBindingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,68))
if mibBuilder.loadTexts:tplinkIpMacBindingMIB.setRevisions(('2012-12-17 10:14',))
_TplinkIpMacBindingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpMacBindingMIBObjects=_TplinkIpMacBindingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,68,1))
_TpIpMacBindigConfigure_ObjectIdentity=ObjectIdentity
tpIpMacBindigConfigure=_TpIpMacBindigConfigure_ObjectIdentity((1,3,6,1,4,1,11863,6,68,1,1))
_TpIpMacBindingTable_Object=MibTable
tpIpMacBindingTable=_TpIpMacBindingTable_Object((1,3,6,1,4,1,11863,6,68,1,1,1))
if mibBuilder.loadTexts:tpIpMacBindingTable.setStatus(_A)
_TpIpMacBindingEntry_Object=MibTableRow
tpIpMacBindingEntry=_TpIpMacBindingEntry_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1))
tpIpMacBindingEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpIpMacBindingEntry.setStatus(_A)
class _TpBindingHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TpBindingHostName_Type.__name__=_B
_TpBindingHostName_Object=MibTableColumn
tpBindingHostName=_TpBindingHostName_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,1),_TpBindingHostName_Type())
tpBindingHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:tpBindingHostName.setStatus(_A)
_TpBindingIp_Type=IpAddress
_TpBindingIp_Object=MibTableColumn
tpBindingIp=_TpBindingIp_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,2),_TpBindingIp_Type())
tpBindingIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tpBindingIp.setStatus(_A)
class _TpBindingMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_TpBindingMac_Type.__name__=_B
_TpBindingMac_Object=MibTableColumn
tpBindingMac=_TpBindingMac_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,3),_TpBindingMac_Type())
tpBindingMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tpBindingMac.setStatus(_A)
_TpBindingVlanId_Type=Integer32
_TpBindingVlanId_Object=MibTableColumn
tpBindingVlanId=_TpBindingVlanId_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,4),_TpBindingVlanId_Type())
tpBindingVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpBindingVlanId.setStatus(_A)
class _TpBindingPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TpBindingPort_Type.__name__=_B
_TpBindingPort_Object=MibTableColumn
tpBindingPort=_TpBindingPort_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,5),_TpBindingPort_Type())
tpBindingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tpBindingPort.setStatus(_A)
class _TpBindingProtectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('arp-detection',1),('ip-source-guard',2),('both',3)))
_TpBindingProtectType_Type.__name__=_D
_TpBindingProtectType_Object=MibTableColumn
tpBindingProtectType=_TpBindingProtectType_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,6),_TpBindingProtectType_Type())
tpBindingProtectType.setMaxAccess(_E)
if mibBuilder.loadTexts:tpBindingProtectType.setStatus(_A)
class _TpBindingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('arp-scanning',2),('dhcp-snooping',3)))
_TpBindingSource_Type.__name__=_D
_TpBindingSource_Object=MibTableColumn
tpBindingSource=_TpBindingSource_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,7),_TpBindingSource_Type())
tpBindingSource.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpBindingSource.setStatus(_A)
_TpBindingRowStatus_Type=TPRowStatus
_TpBindingRowStatus_Object=MibTableColumn
tpBindingRowStatus=_TpBindingRowStatus_Object((1,3,6,1,4,1,11863,6,68,1,1,1,1,8),_TpBindingRowStatus_Type())
tpBindingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpBindingRowStatus.setStatus(_A)
_TplinkIpMacBindingNotifications_ObjectIdentity=ObjectIdentity
tplinkIpMacBindingNotifications=_TplinkIpMacBindingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,68,2))
mibBuilder.exportSymbols(_F,**{'tplinkIpMacBindingMIB':tplinkIpMacBindingMIB,'tplinkIpMacBindingMIBObjects':tplinkIpMacBindingMIBObjects,'tpIpMacBindigConfigure':tpIpMacBindigConfigure,'tpIpMacBindingTable':tpIpMacBindingTable,'tpIpMacBindingEntry':tpIpMacBindingEntry,'tpBindingHostName':tpBindingHostName,_G:tpBindingIp,'tpBindingMac':tpBindingMac,'tpBindingVlanId':tpBindingVlanId,'tpBindingPort':tpBindingPort,'tpBindingProtectType':tpBindingProtectType,'tpBindingSource':tpBindingSource,'tpBindingRowStatus':tpBindingRowStatus,'tplinkIpMacBindingNotifications':tplinkIpMacBindingNotifications})