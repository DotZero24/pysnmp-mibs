_I='userSecurityUserAuthIndex'
_H='OctetString'
_G='TPLINK-USERSECURITY-MIB'
_F='read-only'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkUserSecurity=ModuleIdentity((1,3,6,1,4,1,11863,6,41))
if mibBuilder.loadTexts:tplinkUserSecurity.setRevisions(('1920-09-07 09:00',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TplinkUserSecurityMIBObjects_ObjectIdentity=ObjectIdentity
tplinkUserSecurityMIBObjects=_TplinkUserSecurityMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,41,1))
_UserSecurityUserAuth_ObjectIdentity=ObjectIdentity
userSecurityUserAuth=_UserSecurityUserAuth_ObjectIdentity((1,3,6,1,4,1,11863,6,41,1,1))
class _UserSecurityUserAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('ip',1),('mac',2),('port',3)))
_UserSecurityUserAuthType_Type.__name__=_C
_UserSecurityUserAuthType_Object=MibScalar
userSecurityUserAuthType=_UserSecurityUserAuthType_Object((1,3,6,1,4,1,11863,6,41,1,1,1),_UserSecurityUserAuthType_Type())
userSecurityUserAuthType.setMaxAccess(_F)
if mibBuilder.loadTexts:userSecurityUserAuthType.setStatus(_A)
_UserSecurityUserAuthPort_ObjectIdentity=ObjectIdentity
userSecurityUserAuthPort=_UserSecurityUserAuthPort_ObjectIdentity((1,3,6,1,4,1,11863,6,41,1,1,2))
class _UserSecurityUserAuthPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortEnable_Type.__name__=_C
_UserSecurityUserAuthPortEnable_Object=MibScalar
userSecurityUserAuthPortEnable=_UserSecurityUserAuthPortEnable_Object((1,3,6,1,4,1,11863,6,41,1,1,2,1),_UserSecurityUserAuthPortEnable_Type())
userSecurityUserAuthPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortEnable.setStatus(_A)
_UserSecurityUserAuthPortTable_Object=MibTable
userSecurityUserAuthPortTable=_UserSecurityUserAuthPortTable_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2))
if mibBuilder.loadTexts:userSecurityUserAuthPortTable.setStatus(_A)
_UserSecurityUserAuthPortEntry_Object=MibTableRow
userSecurityUserAuthPortEntry=_UserSecurityUserAuthPortEntry_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1))
userSecurityUserAuthPortEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:userSecurityUserAuthPortEntry.setStatus(_A)
_UserSecurityUserAuthPortIndex_Type=Integer32
_UserSecurityUserAuthPortIndex_Object=MibTableColumn
userSecurityUserAuthPortIndex=_UserSecurityUserAuthPortIndex_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,1),_UserSecurityUserAuthPortIndex_Type())
userSecurityUserAuthPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:userSecurityUserAuthPortIndex.setStatus(_A)
class _UserSecurityUserAuthPortAccessSnmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortAccessSnmp_Type.__name__=_C
_UserSecurityUserAuthPortAccessSnmp_Object=MibTableColumn
userSecurityUserAuthPortAccessSnmp=_UserSecurityUserAuthPortAccessSnmp_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,2),_UserSecurityUserAuthPortAccessSnmp_Type())
userSecurityUserAuthPortAccessSnmp.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortAccessSnmp.setStatus(_A)
class _UserSecurityUserAuthPortAccessTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortAccessTelnet_Type.__name__=_C
_UserSecurityUserAuthPortAccessTelnet_Object=MibTableColumn
userSecurityUserAuthPortAccessTelnet=_UserSecurityUserAuthPortAccessTelnet_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,3),_UserSecurityUserAuthPortAccessTelnet_Type())
userSecurityUserAuthPortAccessTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortAccessTelnet.setStatus(_A)
class _UserSecurityUserAuthPortAccessSsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortAccessSsh_Type.__name__=_C
_UserSecurityUserAuthPortAccessSsh_Object=MibTableColumn
userSecurityUserAuthPortAccessSsh=_UserSecurityUserAuthPortAccessSsh_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,4),_UserSecurityUserAuthPortAccessSsh_Type())
userSecurityUserAuthPortAccessSsh.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortAccessSsh.setStatus(_A)
class _UserSecurityUserAuthPortAccessHttp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortAccessHttp_Type.__name__=_C
_UserSecurityUserAuthPortAccessHttp_Object=MibTableColumn
userSecurityUserAuthPortAccessHttp=_UserSecurityUserAuthPortAccessHttp_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,5),_UserSecurityUserAuthPortAccessHttp_Type())
userSecurityUserAuthPortAccessHttp.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortAccessHttp.setStatus(_A)
class _UserSecurityUserAuthPortAccessHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortAccessHttps_Type.__name__=_C
_UserSecurityUserAuthPortAccessHttps_Object=MibTableColumn
userSecurityUserAuthPortAccessHttps=_UserSecurityUserAuthPortAccessHttps_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,6),_UserSecurityUserAuthPortAccessHttps_Type())
userSecurityUserAuthPortAccessHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortAccessHttps.setStatus(_A)
class _UserSecurityUserAuthPortAccessPing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthPortAccessPing_Type.__name__=_C
_UserSecurityUserAuthPortAccessPing_Object=MibTableColumn
userSecurityUserAuthPortAccessPing=_UserSecurityUserAuthPortAccessPing_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,7),_UserSecurityUserAuthPortAccessPing_Type())
userSecurityUserAuthPortAccessPing.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortAccessPing.setStatus(_A)
class _UserSecurityUserAuthPortConf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UserSecurityUserAuthPortConf_Type.__name__=_H
_UserSecurityUserAuthPortConf_Object=MibTableColumn
userSecurityUserAuthPortConf=_UserSecurityUserAuthPortConf_Object((1,3,6,1,4,1,11863,6,41,1,1,2,2,1,8),_UserSecurityUserAuthPortConf_Type())
userSecurityUserAuthPortConf.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthPortConf.setStatus(_A)
_UserSecurityUserAuthIp_ObjectIdentity=ObjectIdentity
userSecurityUserAuthIp=_UserSecurityUserAuthIp_ObjectIdentity((1,3,6,1,4,1,11863,6,41,1,1,3))
class _UserSecurityUserAuthIpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpEnable_Type.__name__=_C
_UserSecurityUserAuthIpEnable_Object=MibScalar
userSecurityUserAuthIpEnable=_UserSecurityUserAuthIpEnable_Object((1,3,6,1,4,1,11863,6,41,1,1,3,1),_UserSecurityUserAuthIpEnable_Type())
userSecurityUserAuthIpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpEnable.setStatus(_A)
_UserSecurityUserAuthIpTable_Object=MibTable
userSecurityUserAuthIpTable=_UserSecurityUserAuthIpTable_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2))
if mibBuilder.loadTexts:userSecurityUserAuthIpTable.setStatus(_A)
_UserSecurityUserAuthIpEntry_Object=MibTableRow
userSecurityUserAuthIpEntry=_UserSecurityUserAuthIpEntry_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1))
userSecurityUserAuthIpEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:userSecurityUserAuthIpEntry.setStatus(_A)
_UserSecurityUserAuthIpIndex_Type=Integer32
_UserSecurityUserAuthIpIndex_Object=MibTableColumn
userSecurityUserAuthIpIndex=_UserSecurityUserAuthIpIndex_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,1),_UserSecurityUserAuthIpIndex_Type())
userSecurityUserAuthIpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:userSecurityUserAuthIpIndex.setStatus(_A)
class _UserSecurityUserAuthIpAccessSnmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpAccessSnmp_Type.__name__=_C
_UserSecurityUserAuthIpAccessSnmp_Object=MibTableColumn
userSecurityUserAuthIpAccessSnmp=_UserSecurityUserAuthIpAccessSnmp_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,2),_UserSecurityUserAuthIpAccessSnmp_Type())
userSecurityUserAuthIpAccessSnmp.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAccessSnmp.setStatus(_A)
class _UserSecurityUserAuthIpAccessTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpAccessTelnet_Type.__name__=_C
_UserSecurityUserAuthIpAccessTelnet_Object=MibTableColumn
userSecurityUserAuthIpAccessTelnet=_UserSecurityUserAuthIpAccessTelnet_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,3),_UserSecurityUserAuthIpAccessTelnet_Type())
userSecurityUserAuthIpAccessTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAccessTelnet.setStatus(_A)
class _UserSecurityUserAuthIpAccessSsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpAccessSsh_Type.__name__=_C
_UserSecurityUserAuthIpAccessSsh_Object=MibTableColumn
userSecurityUserAuthIpAccessSsh=_UserSecurityUserAuthIpAccessSsh_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,4),_UserSecurityUserAuthIpAccessSsh_Type())
userSecurityUserAuthIpAccessSsh.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAccessSsh.setStatus(_A)
class _UserSecurityUserAuthIpAccessHttp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpAccessHttp_Type.__name__=_C
_UserSecurityUserAuthIpAccessHttp_Object=MibTableColumn
userSecurityUserAuthIpAccessHttp=_UserSecurityUserAuthIpAccessHttp_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,5),_UserSecurityUserAuthIpAccessHttp_Type())
userSecurityUserAuthIpAccessHttp.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAccessHttp.setStatus(_A)
class _UserSecurityUserAuthIpAccessHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpAccessHttps_Type.__name__=_C
_UserSecurityUserAuthIpAccessHttps_Object=MibTableColumn
userSecurityUserAuthIpAccessHttps=_UserSecurityUserAuthIpAccessHttps_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,6),_UserSecurityUserAuthIpAccessHttps_Type())
userSecurityUserAuthIpAccessHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAccessHttps.setStatus(_A)
class _UserSecurityUserAuthIpAccessPing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthIpAccessPing_Type.__name__=_C
_UserSecurityUserAuthIpAccessPing_Object=MibTableColumn
userSecurityUserAuthIpAccessPing=_UserSecurityUserAuthIpAccessPing_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,7),_UserSecurityUserAuthIpAccessPing_Type())
userSecurityUserAuthIpAccessPing.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAccessPing.setStatus(_A)
_UserSecurityUserAuthIpAddress_Type=IpAddress
_UserSecurityUserAuthIpAddress_Object=MibTableColumn
userSecurityUserAuthIpAddress=_UserSecurityUserAuthIpAddress_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,8),_UserSecurityUserAuthIpAddress_Type())
userSecurityUserAuthIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpAddress.setStatus(_A)
_UserSecurityUserAuthIpMask_Type=IpAddress
_UserSecurityUserAuthIpMask_Object=MibTableColumn
userSecurityUserAuthIpMask=_UserSecurityUserAuthIpMask_Object((1,3,6,1,4,1,11863,6,41,1,1,3,2,1,9),_UserSecurityUserAuthIpMask_Type())
userSecurityUserAuthIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthIpMask.setStatus(_A)
_UserSecurityUserAuthMac_ObjectIdentity=ObjectIdentity
userSecurityUserAuthMac=_UserSecurityUserAuthMac_ObjectIdentity((1,3,6,1,4,1,11863,6,41,1,1,4))
class _UserSecurityUserAuthMacEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacEnable_Type.__name__=_C
_UserSecurityUserAuthMacEnable_Object=MibScalar
userSecurityUserAuthMacEnable=_UserSecurityUserAuthMacEnable_Object((1,3,6,1,4,1,11863,6,41,1,1,4,1),_UserSecurityUserAuthMacEnable_Type())
userSecurityUserAuthMacEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacEnable.setStatus(_A)
_UserSecurityUserAuthMacTable_Object=MibTable
userSecurityUserAuthMacTable=_UserSecurityUserAuthMacTable_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2))
if mibBuilder.loadTexts:userSecurityUserAuthMacTable.setStatus(_A)
_UserSecurityUserAuthMacEntry_Object=MibTableRow
userSecurityUserAuthMacEntry=_UserSecurityUserAuthMacEntry_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1))
userSecurityUserAuthMacEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:userSecurityUserAuthMacEntry.setStatus(_A)
_UserSecurityUserAuthMacIndex_Type=Integer32
_UserSecurityUserAuthMacIndex_Object=MibTableColumn
userSecurityUserAuthMacIndex=_UserSecurityUserAuthMacIndex_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,1),_UserSecurityUserAuthMacIndex_Type())
userSecurityUserAuthMacIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:userSecurityUserAuthMacIndex.setStatus(_A)
class _UserSecurityUserAuthMacAccessSnmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacAccessSnmp_Type.__name__=_C
_UserSecurityUserAuthMacAccessSnmp_Object=MibTableColumn
userSecurityUserAuthMacAccessSnmp=_UserSecurityUserAuthMacAccessSnmp_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,2),_UserSecurityUserAuthMacAccessSnmp_Type())
userSecurityUserAuthMacAccessSnmp.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAccessSnmp.setStatus(_A)
class _UserSecurityUserAuthMacAccessTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacAccessTelnet_Type.__name__=_C
_UserSecurityUserAuthMacAccessTelnet_Object=MibTableColumn
userSecurityUserAuthMacAccessTelnet=_UserSecurityUserAuthMacAccessTelnet_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,3),_UserSecurityUserAuthMacAccessTelnet_Type())
userSecurityUserAuthMacAccessTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAccessTelnet.setStatus(_A)
class _UserSecurityUserAuthMacAccessSsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacAccessSsh_Type.__name__=_C
_UserSecurityUserAuthMacAccessSsh_Object=MibTableColumn
userSecurityUserAuthMacAccessSsh=_UserSecurityUserAuthMacAccessSsh_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,4),_UserSecurityUserAuthMacAccessSsh_Type())
userSecurityUserAuthMacAccessSsh.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAccessSsh.setStatus(_A)
class _UserSecurityUserAuthMacAccessHttp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacAccessHttp_Type.__name__=_C
_UserSecurityUserAuthMacAccessHttp_Object=MibTableColumn
userSecurityUserAuthMacAccessHttp=_UserSecurityUserAuthMacAccessHttp_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,5),_UserSecurityUserAuthMacAccessHttp_Type())
userSecurityUserAuthMacAccessHttp.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAccessHttp.setStatus(_A)
class _UserSecurityUserAuthMacAccessHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacAccessHttps_Type.__name__=_C
_UserSecurityUserAuthMacAccessHttps_Object=MibTableColumn
userSecurityUserAuthMacAccessHttps=_UserSecurityUserAuthMacAccessHttps_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,6),_UserSecurityUserAuthMacAccessHttps_Type())
userSecurityUserAuthMacAccessHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAccessHttps.setStatus(_A)
class _UserSecurityUserAuthMacAccessPing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_UserSecurityUserAuthMacAccessPing_Type.__name__=_C
_UserSecurityUserAuthMacAccessPing_Object=MibTableColumn
userSecurityUserAuthMacAccessPing=_UserSecurityUserAuthMacAccessPing_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,7),_UserSecurityUserAuthMacAccessPing_Type())
userSecurityUserAuthMacAccessPing.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAccessPing.setStatus(_A)
class _UserSecurityUserAuthMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UserSecurityUserAuthMacAddress_Type.__name__=_H
_UserSecurityUserAuthMacAddress_Object=MibTableColumn
userSecurityUserAuthMacAddress=_UserSecurityUserAuthMacAddress_Object((1,3,6,1,4,1,11863,6,41,1,1,4,2,1,8),_UserSecurityUserAuthMacAddress_Type())
userSecurityUserAuthMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:userSecurityUserAuthMacAddress.setStatus(_A)
_TplinkUserSecurityMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkUserSecurityMIBNotifications=_TplinkUserSecurityMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,41,2))
mibBuilder.exportSymbols(_G,**{'MacAddress':MacAddress,'tplinkUserSecurity':tplinkUserSecurity,'tplinkUserSecurityMIBObjects':tplinkUserSecurityMIBObjects,'userSecurityUserAuth':userSecurityUserAuth,'userSecurityUserAuthType':userSecurityUserAuthType,'userSecurityUserAuthPort':userSecurityUserAuthPort,'userSecurityUserAuthPortEnable':userSecurityUserAuthPortEnable,'userSecurityUserAuthPortTable':userSecurityUserAuthPortTable,'userSecurityUserAuthPortEntry':userSecurityUserAuthPortEntry,'userSecurityUserAuthPortIndex':userSecurityUserAuthPortIndex,'userSecurityUserAuthPortAccessSnmp':userSecurityUserAuthPortAccessSnmp,'userSecurityUserAuthPortAccessTelnet':userSecurityUserAuthPortAccessTelnet,'userSecurityUserAuthPortAccessSsh':userSecurityUserAuthPortAccessSsh,'userSecurityUserAuthPortAccessHttp':userSecurityUserAuthPortAccessHttp,'userSecurityUserAuthPortAccessHttps':userSecurityUserAuthPortAccessHttps,'userSecurityUserAuthPortAccessPing':userSecurityUserAuthPortAccessPing,'userSecurityUserAuthPortConf':userSecurityUserAuthPortConf,'userSecurityUserAuthIp':userSecurityUserAuthIp,'userSecurityUserAuthIpEnable':userSecurityUserAuthIpEnable,'userSecurityUserAuthIpTable':userSecurityUserAuthIpTable,'userSecurityUserAuthIpEntry':userSecurityUserAuthIpEntry,'userSecurityUserAuthIpIndex':userSecurityUserAuthIpIndex,'userSecurityUserAuthIpAccessSnmp':userSecurityUserAuthIpAccessSnmp,'userSecurityUserAuthIpAccessTelnet':userSecurityUserAuthIpAccessTelnet,'userSecurityUserAuthIpAccessSsh':userSecurityUserAuthIpAccessSsh,'userSecurityUserAuthIpAccessHttp':userSecurityUserAuthIpAccessHttp,'userSecurityUserAuthIpAccessHttps':userSecurityUserAuthIpAccessHttps,'userSecurityUserAuthIpAccessPing':userSecurityUserAuthIpAccessPing,'userSecurityUserAuthIpAddress':userSecurityUserAuthIpAddress,'userSecurityUserAuthIpMask':userSecurityUserAuthIpMask,'userSecurityUserAuthMac':userSecurityUserAuthMac,'userSecurityUserAuthMacEnable':userSecurityUserAuthMacEnable,'userSecurityUserAuthMacTable':userSecurityUserAuthMacTable,'userSecurityUserAuthMacEntry':userSecurityUserAuthMacEntry,'userSecurityUserAuthMacIndex':userSecurityUserAuthMacIndex,'userSecurityUserAuthMacAccessSnmp':userSecurityUserAuthMacAccessSnmp,'userSecurityUserAuthMacAccessTelnet':userSecurityUserAuthMacAccessTelnet,'userSecurityUserAuthMacAccessSsh':userSecurityUserAuthMacAccessSsh,'userSecurityUserAuthMacAccessHttp':userSecurityUserAuthMacAccessHttp,'userSecurityUserAuthMacAccessHttps':userSecurityUserAuthMacAccessHttps,'userSecurityUserAuthMacAccessPing':userSecurityUserAuthMacAccessPing,'userSecurityUserAuthMacAddress':userSecurityUserAuthMacAddress,'tplinkUserSecurityMIBNotifications':tplinkUserSecurityMIBNotifications})