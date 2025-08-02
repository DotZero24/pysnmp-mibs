_Y='public'
_X='wpapskmixed'
_W='wpa2psk'
_V='wpapsk'
_U='wlanTableIndex'
_T='ENGENIUS-PRIVATE-MIB'
_S='manual'
_R='key4'
_Q='key3'
_P='key2'
_O='key1'
_N='aes'
_M='wep'
_L='shared'
_K='open'
_J='admin'
_I='none'
_H='auto'
_G='read-only'
_F='enable'
_E='disable'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
engeniusprivate=ModuleIdentity((1,3,6,1,4,1,14125,2))
if mibBuilder.loadTexts:engeniusprivate.setRevisions(('2009-06-11 11:00','2009-06-10 16:00','2009-05-14 10:00'))
_Engenius_ObjectIdentity=ObjectIdentity
engenius=_Engenius_ObjectIdentity((1,3,6,1,4,1,14125))
_Status_ObjectIdentity=ObjectIdentity
status=_Status_ObjectIdentity((1,3,6,1,4,1,14125,2,1))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,14125,2,1,1))
class _SystemName_Type(DisplayString):defaultValue=OctetString('Access Point');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SystemName_Type.__name__=_D
_SystemName_Object=MibScalar
systemName=_SystemName_Object((1,3,6,1,4,1,14125,2,1,1,1),_SystemName_Type())
systemName.setMaxAccess(_G)
if mibBuilder.loadTexts:systemName.setStatus(_A)
class _SysPassword_Type(DisplayString):defaultValue=OctetString(_J);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SysPassword_Type.__name__=_D
_SysPassword_Object=MibScalar
sysPassword=_SysPassword_Object((1,3,6,1,4,1,14125,2,1,1,2),_SysPassword_Type())
sysPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:sysPassword.setStatus(_A)
class _ErrMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ErrMsg_Type.__name__=_D
_ErrMsg_Object=MibScalar
errMsg=_ErrMsg_Object((1,3,6,1,4,1,14125,2,1,1,3),_ErrMsg_Type())
errMsg.setMaxAccess(_G)
if mibBuilder.loadTexts:errMsg.setStatus(_A)
class _StatusWLANSTAAssoc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_StatusWLANSTAAssoc_Type.__name__=_C
_StatusWLANSTAAssoc_Object=MibScalar
statusWLANSTAAssoc=_StatusWLANSTAAssoc_Object((1,3,6,1,4,1,14125,2,1,1,4),_StatusWLANSTAAssoc_Type())
statusWLANSTAAssoc.setMaxAccess(_G)
if mibBuilder.loadTexts:statusWLANSTAAssoc.setStatus(_A)
class _ModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ModelName_Type.__name__=_D
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,14125,2,1,1,5),_ModelName_Type())
modelName.setMaxAccess(_G)
if mibBuilder.loadTexts:modelName.setStatus(_A)
class _WirelessMacAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_WirelessMacAddress_Type.__name__=_D
_WirelessMacAddress_Object=MibScalar
wirelessMacAddress=_WirelessMacAddress_Object((1,3,6,1,4,1,14125,2,1,1,6),_WirelessMacAddress_Type())
wirelessMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:wirelessMacAddress.setStatus(_A)
_WanIPAddress_Type=DisplayString
_WanIPAddress_Object=MibScalar
wanIPAddress=_WanIPAddress_Object((1,3,6,1,4,1,14125,2,1,1,7),_WanIPAddress_Type())
wanIPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:wanIPAddress.setStatus(_A)
_WanSubnetMask_Type=DisplayString
_WanSubnetMask_Object=MibScalar
wanSubnetMask=_WanSubnetMask_Object((1,3,6,1,4,1,14125,2,1,1,8),_WanSubnetMask_Type())
wanSubnetMask.setMaxAccess(_G)
if mibBuilder.loadTexts:wanSubnetMask.setStatus(_A)
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,14125,2,2))
_Wan_ObjectIdentity=ObjectIdentity
wan=_Wan_ObjectIdentity((1,3,6,1,4,1,14125,2,2,1))
class _WanConnectionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dhcp',1),('static',2),('pppoe',3)))
_WanConnectionType_Type.__name__=_C
_WanConnectionType_Object=MibScalar
wanConnectionType=_WanConnectionType_Object((1,3,6,1,4,1,14125,2,2,1,1),_WanConnectionType_Type())
wanConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:wanConnectionType.setStatus(_A)
class _WanGeneralAccount_Type(DisplayString):defaultValue=OctetString(_I);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WanGeneralAccount_Type.__name__=_D
_WanGeneralAccount_Object=MibScalar
wanGeneralAccount=_WanGeneralAccount_Object((1,3,6,1,4,1,14125,2,2,1,2),_WanGeneralAccount_Type())
wanGeneralAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:wanGeneralAccount.setStatus(_A)
class _WanGeneralDomain_Type(DisplayString):defaultValue=OctetString(_I);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WanGeneralDomain_Type.__name__=_D
_WanGeneralDomain_Object=MibScalar
wanGeneralDomain=_WanGeneralDomain_Object((1,3,6,1,4,1,14125,2,2,1,3),_WanGeneralDomain_Type())
wanGeneralDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:wanGeneralDomain.setStatus(_A)
_WanGeneralIP_Type=IpAddress
_WanGeneralIP_Object=MibScalar
wanGeneralIP=_WanGeneralIP_Object((1,3,6,1,4,1,14125,2,2,1,4),_WanGeneralIP_Type())
wanGeneralIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wanGeneralIP.setStatus(_A)
_WanGeneralSubnetMask_Type=IpAddress
_WanGeneralSubnetMask_Object=MibScalar
wanGeneralSubnetMask=_WanGeneralSubnetMask_Object((1,3,6,1,4,1,14125,2,2,1,5),_WanGeneralSubnetMask_Type())
wanGeneralSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wanGeneralSubnetMask.setStatus(_A)
_WanGeneralGateway_Type=IpAddress
_WanGeneralGateway_Object=MibScalar
wanGeneralGateway=_WanGeneralGateway_Object((1,3,6,1,4,1,14125,2,2,1,6),_WanGeneralGateway_Type())
wanGeneralGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wanGeneralGateway.setStatus(_A)
_Pppoe_ObjectIdentity=ObjectIdentity
pppoe=_Pppoe_ObjectIdentity((1,3,6,1,4,1,14125,2,2,2))
class _WanPPPoELoginName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WanPPPoELoginName_Type.__name__=_D
_WanPPPoELoginName_Object=MibScalar
wanPPPoELoginName=_WanPPPoELoginName_Object((1,3,6,1,4,1,14125,2,2,2,1),_WanPPPoELoginName_Type())
wanPPPoELoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPPPoELoginName.setStatus(_A)
class _WanPPPoEPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WanPPPoEPassword_Type.__name__=_D
_WanPPPoEPassword_Object=MibScalar
wanPPPoEPassword=_WanPPPoEPassword_Object((1,3,6,1,4,1,14125,2,2,2,2),_WanPPPoEPassword_Type())
wanPPPoEPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPPPoEPassword.setStatus(_A)
class _WanPPPoEServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WanPPPoEServiceName_Type.__name__=_D
_WanPPPoEServiceName_Object=MibScalar
wanPPPoEServiceName=_WanPPPoEServiceName_Object((1,3,6,1,4,1,14125,2,2,2,3),_WanPPPoEServiceName_Type())
wanPPPoEServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPPPoEServiceName.setStatus(_A)
class _WanPPPoEConnectionType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('keepalive',0),('connectondemand',1)))
_WanPPPoEConnectionType_Type.__name__=_C
_WanPPPoEConnectionType_Object=MibScalar
wanPPPoEConnectionType=_WanPPPoEConnectionType_Object((1,3,6,1,4,1,14125,2,2,2,4),_WanPPPoEConnectionType_Type())
wanPPPoEConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPPPoEConnectionType.setStatus(_A)
class _WanPPPoEMaxIdleTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_WanPPPoEMaxIdleTime_Type.__name__=_C
_WanPPPoEMaxIdleTime_Object=MibScalar
wanPPPoEMaxIdleTime=_WanPPPoEMaxIdleTime_Object((1,3,6,1,4,1,14125,2,2,2,5),_WanPPPoEMaxIdleTime_Type())
wanPPPoEMaxIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPPPoEMaxIdleTime.setStatus(_A)
class _WanPPPoERedialPeriod_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,180))
_WanPPPoERedialPeriod_Type.__name__=_C
_WanPPPoERedialPeriod_Object=MibScalar
wanPPPoERedialPeriod=_WanPPPoERedialPeriod_Object((1,3,6,1,4,1,14125,2,2,2,6),_WanPPPoERedialPeriod_Type())
wanPPPoERedialPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPPPoERedialPeriod.setStatus(_A)
_Dns_ObjectIdentity=ObjectIdentity
dns=_Dns_ObjectIdentity((1,3,6,1,4,1,14125,2,2,3))
class _WanDNSSourc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('isp',0),('specified',1)))
_WanDNSSourc_Type.__name__=_C
_WanDNSSourc_Object=MibScalar
wanDNSSourc=_WanDNSSourc_Object((1,3,6,1,4,1,14125,2,2,3,1),_WanDNSSourc_Type())
wanDNSSourc.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDNSSourc.setStatus(_A)
_WanPrimaryDNSIP_Type=IpAddress
_WanPrimaryDNSIP_Object=MibScalar
wanPrimaryDNSIP=_WanPrimaryDNSIP_Object((1,3,6,1,4,1,14125,2,2,3,2),_WanPrimaryDNSIP_Type())
wanPrimaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPrimaryDNSIP.setStatus(_A)
_WanSecondaryDNSIP_Type=IpAddress
_WanSecondaryDNSIP_Object=MibScalar
wanSecondaryDNSIP=_WanSecondaryDNSIP_Object((1,3,6,1,4,1,14125,2,2,3,3),_WanSecondaryDNSIP_Type())
wanSecondaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wanSecondaryDNSIP.setStatus(_A)
_Mtu_ObjectIdentity=ObjectIdentity
mtu=_Mtu_ObjectIdentity((1,3,6,1,4,1,14125,2,2,4))
class _WanMTUMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_S,1)))
_WanMTUMode_Type.__name__=_C
_WanMTUMode_Object=MibScalar
wanMTUMode=_WanMTUMode_Object((1,3,6,1,4,1,14125,2,2,4,1),_WanMTUMode_Type())
wanMTUMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wanMTUMode.setStatus(_A)
class _WanMTU_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(576,1500))
_WanMTU_Type.__name__=_C
_WanMTU_Object=MibScalar
wanMTU=_WanMTU_Object((1,3,6,1,4,1,14125,2,2,4,2),_WanMTU_Type())
wanMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:wanMTU.setStatus(_A)
class _PppoeMTU_Type(Integer32):defaultValue=1492;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(576,1492))
_PppoeMTU_Type.__name__=_C
_PppoeMTU_Object=MibScalar
pppoeMTU=_PppoeMTU_Object((1,3,6,1,4,1,14125,2,2,4,3),_PppoeMTU_Type())
pppoeMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeMTU.setStatus(_A)
_Landhcp_ObjectIdentity=ObjectIdentity
landhcp=_Landhcp_ObjectIdentity((1,3,6,1,4,1,14125,2,2,5))
class _LanDHCPC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LanDHCPC_Type.__name__=_C
_LanDHCPC_Object=MibScalar
lanDHCPC=_LanDHCPC_Object((1,3,6,1,4,1,14125,2,2,5,1),_LanDHCPC_Type())
lanDHCPC.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDHCPC.setStatus(_A)
_LanIP_Type=IpAddress
_LanIP_Object=MibScalar
lanIP=_LanIP_Object((1,3,6,1,4,1,14125,2,2,5,2),_LanIP_Type())
lanIP.setMaxAccess(_B)
if mibBuilder.loadTexts:lanIP.setStatus(_A)
_LanSubnetmask_Type=IpAddress
_LanSubnetmask_Object=MibScalar
lanSubnetmask=_LanSubnetmask_Object((1,3,6,1,4,1,14125,2,2,5,3),_LanSubnetmask_Type())
lanSubnetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:lanSubnetmask.setStatus(_A)
_LanGatewayIP_Type=IpAddress
_LanGatewayIP_Object=MibScalar
lanGatewayIP=_LanGatewayIP_Object((1,3,6,1,4,1,14125,2,2,5,4),_LanGatewayIP_Type())
lanGatewayIP.setMaxAccess(_B)
if mibBuilder.loadTexts:lanGatewayIP.setStatus(_A)
_LanWINSAddr_Type=IpAddress
_LanWINSAddr_Object=MibScalar
lanWINSAddr=_LanWINSAddr_Object((1,3,6,1,4,1,14125,2,2,5,5),_LanWINSAddr_Type())
lanWINSAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanWINSAddr.setStatus(_A)
class _LanDHCPSrvEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LanDHCPSrvEnable_Type.__name__=_C
_LanDHCPSrvEnable_Object=MibScalar
lanDHCPSrvEnable=_LanDHCPSrvEnable_Object((1,3,6,1,4,1,14125,2,2,5,6),_LanDHCPSrvEnable_Type())
lanDHCPSrvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDHCPSrvEnable.setStatus(_A)
_LanDHCPSrvStartAddr_Type=IpAddress
_LanDHCPSrvStartAddr_Object=MibScalar
lanDHCPSrvStartAddr=_LanDHCPSrvStartAddr_Object((1,3,6,1,4,1,14125,2,2,5,7),_LanDHCPSrvStartAddr_Type())
lanDHCPSrvStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDHCPSrvStartAddr.setStatus(_A)
_LanDHCPSrvStopAddr_Type=IpAddress
_LanDHCPSrvStopAddr_Object=MibScalar
lanDHCPSrvStopAddr=_LanDHCPSrvStopAddr_Object((1,3,6,1,4,1,14125,2,2,5,8),_LanDHCPSrvStopAddr_Type())
lanDHCPSrvStopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDHCPSrvStopAddr.setStatus(_A)
_Ntp_ObjectIdentity=ObjectIdentity
ntp=_Ntp_ObjectIdentity((1,3,6,1,4,1,14125,2,2,6))
class _TimeSettingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_H,1)))
_TimeSettingMode_Type.__name__=_C
_TimeSettingMode_Object=MibScalar
timeSettingMode=_TimeSettingMode_Object((1,3,6,1,4,1,14125,2,2,6,1),_TimeSettingMode_Type())
timeSettingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:timeSettingMode.setStatus(_A)
class _UserNTPSrvMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_UserNTPSrvMode_Type.__name__=_C
_UserNTPSrvMode_Object=MibScalar
userNTPSrvMode=_UserNTPSrvMode_Object((1,3,6,1,4,1,14125,2,2,6,2),_UserNTPSrvMode_Type())
userNTPSrvMode.setMaxAccess(_B)
if mibBuilder.loadTexts:userNTPSrvMode.setStatus(_A)
_UserNTPSrvIP_Type=IpAddress
_UserNTPSrvIP_Object=MibScalar
userNTPSrvIP=_UserNTPSrvIP_Object((1,3,6,1,4,1,14125,2,2,6,3),_UserNTPSrvIP_Type())
userNTPSrvIP.setMaxAccess(_B)
if mibBuilder.loadTexts:userNTPSrvIP.setStatus(_A)
class _TimeZone_Type(DisplayString):defaultValue=OctetString('GMT0');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TimeZone_Type.__name__=_D
_TimeZone_Object=MibScalar
timeZone=_TimeZone_Object((1,3,6,1,4,1,14125,2,2,6,4),_TimeZone_Type())
timeZone.setMaxAccess(_G)
if mibBuilder.loadTexts:timeZone.setStatus(_A)
_Admin_ObjectIdentity=ObjectIdentity
admin=_Admin_ObjectIdentity((1,3,6,1,4,1,14125,2,2,8))
class _Username_Type(DisplayString):defaultValue=OctetString(_J);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_Username_Type.__name__=_D
_Username_Object=MibScalar
username=_Username_Object((1,3,6,1,4,1,14125,2,2,8,1),_Username_Type())
username.setMaxAccess(_B)
if mibBuilder.loadTexts:username.setStatus(_A)
class _RemoteManagementEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RemoteManagementEnable_Type.__name__=_C
_RemoteManagementEnable_Object=MibScalar
remoteManagementEnable=_RemoteManagementEnable_Object((1,3,6,1,4,1,14125,2,2,8,3),_RemoteManagementEnable_Type())
remoteManagementEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteManagementEnable.setStatus(_A)
class _RemoteUpgradeEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RemoteUpgradeEnable_Type.__name__=_C
_RemoteUpgradeEnable_Object=MibScalar
remoteUpgradeEnable=_RemoteUpgradeEnable_Object((1,3,6,1,4,1,14125,2,2,8,4),_RemoteUpgradeEnable_Type())
remoteUpgradeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteUpgradeEnable.setStatus(_A)
class _RemoteManagementPort_Type(Integer32):defaultValue=8080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RemoteManagementPort_Type.__name__=_C
_RemoteManagementPort_Object=MibScalar
remoteManagementPort=_RemoteManagementPort_Object((1,3,6,1,4,1,14125,2,2,8,5),_RemoteManagementPort_Type())
remoteManagementPort.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteManagementPort.setStatus(_A)
class _RemoteManagementVLANID_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_RemoteManagementVLANID_Type.__name__=_C
_RemoteManagementVLANID_Object=MibScalar
remoteManagementVLANID=_RemoteManagementVLANID_Object((1,3,6,1,4,1,14125,2,2,8,6),_RemoteManagementVLANID_Type())
remoteManagementVLANID.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteManagementVLANID.setStatus(_A)
_Wlan_ObjectIdentity=ObjectIdentity
wlan=_Wlan_ObjectIdentity((1,3,6,1,4,1,14125,2,2,9))
class _WlanMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6,7,9)));namedValues=NamedValues(*(('wlan11a',1),('wlan11b',2),('wlan11bg',3),('wlan11astaticturbo',5),('wlan11gdynamicturbo',6),('wlan11gstaticturbo',7),('wlan11gpure',9)))
_WlanMode_Type.__name__=_C
_WlanMode_Object=MibScalar
wlanMode=_WlanMode_Object((1,3,6,1,4,1,14125,2,2,9,1),_WlanMode_Type())
wlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMode.setStatus(_A)
class _ChanBwMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('wlan20MHz',0),('wlan10MHz',1),('wlan5MHz',2)))
_ChanBwMode_Type.__name__=_C
_ChanBwMode_Object=MibScalar
chanBwMode=_ChanBwMode_Object((1,3,6,1,4,1,14125,2,2,9,2),_ChanBwMode_Type())
chanBwMode.setMaxAccess(_B)
if mibBuilder.loadTexts:chanBwMode.setStatus(_A)
class _WlanaSSID_Type(DisplayString):defaultValue=OctetString('EnGenius');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_WlanaSSID_Type.__name__=_D
_WlanaSSID_Object=MibScalar
wlanaSSID=_WlanaSSID_Object((1,3,6,1,4,1,14125,2,2,9,3),_WlanaSSID_Type())
wlanaSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanaSSID.setStatus(_A)
class _WlanOpMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('accesspoint',0),('clientbridge',1),('wdsbridge',2),('repeater',3),('aprouter',4),('clientrouter',5),('mesh',6)))
_WlanOpMode_Type.__name__=_C
_WlanOpMode_Object=MibScalar
wlanOpMode=_WlanOpMode_Object((1,3,6,1,4,1,14125,2,2,9,4),_WlanOpMode_Type())
wlanOpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanOpMode.setStatus(_A)
class _WlanCountryCode_Type(DisplayString):defaultValue=OctetString('0');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_WlanCountryCode_Type.__name__=_D
_WlanCountryCode_Object=MibScalar
wlanCountryCode=_WlanCountryCode_Object((1,3,6,1,4,1,14125,2,2,9,5),_WlanCountryCode_Type())
wlanCountryCode.setMaxAccess(_G)
if mibBuilder.loadTexts:wlanCountryCode.setStatus(_A)
class _WlanCountry_Type(DisplayString):defaultValue=OctetString('N/A');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_WlanCountry_Type.__name__=_D
_WlanCountry_Object=MibScalar
wlanCountry=_WlanCountry_Object((1,3,6,1,4,1,14125,2,2,9,6),_WlanCountry_Type())
wlanCountry.setMaxAccess(_G)
if mibBuilder.loadTexts:wlanCountry.setStatus(_A)
class _WlanChannel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WlanChannel_Type.__name__=_C
_WlanChannel_Object=MibScalar
wlanChannel=_WlanChannel_Object((1,3,6,1,4,1,14125,2,2,9,7),_WlanChannel_Type())
wlanChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanChannel.setStatus(_A)
class _WlanACLMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('allow',1),('deny',2)))
_WlanACLMode_Type.__name__=_C
_WlanACLMode_Object=MibScalar
wlanACLMode=_WlanACLMode_Object((1,3,6,1,4,1,14125,2,2,9,8),_WlanACLMode_Type())
wlanACLMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanACLMode.setStatus(_A)
class _WlanOutdoorDistance_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,30000))
_WlanOutdoorDistance_Type.__name__=_C
_WlanOutdoorDistance_Object=MibScalar
wlanOutdoorDistance=_WlanOutdoorDistance_Object((1,3,6,1,4,1,14125,2,2,9,9),_WlanOutdoorDistance_Type())
wlanOutdoorDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanOutdoorDistance.setStatus(_A)
class _WlanDataRate_Type(DisplayString):defaultValue=OctetString(_H);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_WlanDataRate_Type.__name__=_D
_WlanDataRate_Object=MibScalar
wlanDataRate=_WlanDataRate_Object((1,3,6,1,4,1,14125,2,2,9,10),_WlanDataRate_Type())
wlanDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanDataRate.setStatus(_A)
class _WlanTxPower_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_WlanTxPower_Type.__name__=_C
_WlanTxPower_Object=MibScalar
wlanTxPower=_WlanTxPower_Object((1,3,6,1,4,1,14125,2,2,9,11),_WlanTxPower_Type())
wlanTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanTxPower.setStatus(_A)
class _Antennasel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('diversity',0),('vertical',1),('horizontal',2)))
_Antennasel_Type.__name__=_C
_Antennasel_Object=MibScalar
antennasel=_Antennasel_Object((1,3,6,1,4,1,14125,2,2,9,12),_Antennasel_Type())
antennasel.setMaxAccess(_B)
if mibBuilder.loadTexts:antennasel.setStatus(_A)
class _WlanBeaconInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,500))
_WlanBeaconInterval_Type.__name__=_C
_WlanBeaconInterval_Object=MibScalar
wlanBeaconInterval=_WlanBeaconInterval_Object((1,3,6,1,4,1,14125,2,2,9,13),_WlanBeaconInterval_Type())
wlanBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanBeaconInterval.setStatus(_A)
class _WlanRTSTh_Type(Integer32):defaultValue=2346;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2346))
_WlanRTSTh_Type.__name__=_C
_WlanRTSTh_Object=MibScalar
wlanRTSTh=_WlanRTSTh_Object((1,3,6,1,4,1,14125,2,2,9,15),_WlanRTSTh_Type())
wlanRTSTh.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanRTSTh.setStatus(_A)
class _WlanFragLen_Type(Integer32):defaultValue=2346;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_WlanFragLen_Type.__name__=_C
_WlanFragLen_Object=MibScalar
wlanFragLen=_WlanFragLen_Object((1,3,6,1,4,1,14125,2,2,9,16),_WlanFragLen_Type())
wlanFragLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanFragLen.setStatus(_A)
class _WlanProtmode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('ctsonly',1),('rtscts',2)))
_WlanProtmode_Type.__name__=_C
_WlanProtmode_Object=MibScalar
wlanProtmode=_WlanProtmode_Object((1,3,6,1,4,1,14125,2,2,9,18),_WlanProtmode_Type())
wlanProtmode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanProtmode.setStatus(_A)
_WlanPreferBSSID_Type=DisplayString
_WlanPreferBSSID_Object=MibScalar
wlanPreferBSSID=_WlanPreferBSSID_Object((1,3,6,1,4,1,14125,2,2,9,19),_WlanPreferBSSID_Type())
wlanPreferBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanPreferBSSID.setStatus(_A)
_WlanTable_Object=MibTable
wlanTable=_WlanTable_Object((1,3,6,1,4,1,14125,2,2,9,21))
if mibBuilder.loadTexts:wlanTable.setStatus(_A)
_WlanTableEntry_Object=MibTableRow
wlanTableEntry=_WlanTableEntry_Object((1,3,6,1,4,1,14125,2,2,9,21,1))
wlanTableEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:wlanTableEntry.setStatus(_A)
class _WlanTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_WlanTableIndex_Type.__name__=_C
_WlanTableIndex_Object=MibTableColumn
wlanTableIndex=_WlanTableIndex_Object((1,3,6,1,4,1,14125,2,2,9,21,1,1),_WlanTableIndex_Type())
wlanTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wlanTableIndex.setStatus(_A)
class _WlanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WlanEnable_Type.__name__=_C
_WlanEnable_Object=MibTableColumn
wlanEnable=_WlanEnable_Object((1,3,6,1,4,1,14125,2,2,9,21,1,2),_WlanEnable_Type())
wlanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanEnable.setStatus(_A)
class _WlanSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WlanSSID_Type.__name__=_D
_WlanSSID_Object=MibTableColumn
wlanSSID=_WlanSSID_Object((1,3,6,1,4,1,14125,2,2,9,21,1,3),_WlanSSID_Type())
wlanSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanSSID.setStatus(_A)
class _WlanHideSSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WlanHideSSID_Type.__name__=_C
_WlanHideSSID_Object=MibTableColumn
wlanHideSSID=_WlanHideSSID_Object((1,3,6,1,4,1,14125,2,2,9,21,1,4),_WlanHideSSID_Type())
wlanHideSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanHideSSID.setStatus(_A)
class _WlanStaSeparation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WlanStaSeparation_Type.__name__=_C
_WlanStaSeparation_Object=MibTableColumn
wlanStaSeparation=_WlanStaSeparation_Object((1,3,6,1,4,1,14125,2,2,9,21,1,5),_WlanStaSeparation_Type())
wlanStaSeparation.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStaSeparation.setStatus(_A)
class _WlanVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WlanVLANID_Type.__name__=_C
_WlanVLANID_Object=MibTableColumn
wlanVLANID=_WlanVLANID_Object((1,3,6,1,4,1,14125,2,2,9,21,1,6),_WlanVLANID_Type())
wlanVLANID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanVLANID.setStatus(_A)
class _WlanAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_K,1),(_L,2),(_H,3),('wlan8021x',4),('wpa',5),(_V,6),('wpa2',7),(_W,8),('wpamixed',9),(_X,10)))
_WlanAuth_Type.__name__=_C
_WlanAuth_Object=MibTableColumn
wlanAuth=_WlanAuth_Object((1,3,6,1,4,1,14125,2,2,9,21,1,7),_WlanAuth_Type())
wlanAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanAuth.setStatus(_A)
class _WlanEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_M,1),('tkip',2),(_N,3),(_H,4)))
_WlanEncryption_Type.__name__=_C
_WlanEncryption_Object=MibTableColumn
wlanEncryption=_WlanEncryption_Object((1,3,6,1,4,1,14125,2,2,9,21,1,8),_WlanEncryption_Type())
wlanEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanEncryption.setStatus(_A)
class _WlanWepDefaultKeyIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_WlanWepDefaultKeyIdx_Type.__name__=_C
_WlanWepDefaultKeyIdx_Object=MibTableColumn
wlanWepDefaultKeyIdx=_WlanWepDefaultKeyIdx_Object((1,3,6,1,4,1,14125,2,2,9,21,1,9),_WlanWepDefaultKeyIdx_Type())
wlanWepDefaultKeyIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWepDefaultKeyIdx.setStatus(_A)
class _WlanWepKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5),ValueSizeConstraint(10,10),ValueSizeConstraint(13,13),ValueSizeConstraint(16,16),ValueSizeConstraint(26,26),ValueSizeConstraint(32,32))
_WlanWepKey_Type.__name__=_D
_WlanWepKey_Object=MibTableColumn
wlanWepKey=_WlanWepKey_Object((1,3,6,1,4,1,14125,2,2,9,21,1,10),_WlanWepKey_Type())
wlanWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWepKey.setStatus(_A)
class _WlanWpapskPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlanWpapskPassphrase_Type.__name__=_D
_WlanWpapskPassphrase_Object=MibTableColumn
wlanWpapskPassphrase=_WlanWpapskPassphrase_Object((1,3,6,1,4,1,14125,2,2,9,21,1,11),_WlanWpapskPassphrase_Type())
wlanWpapskPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWpapskPassphrase.setStatus(_A)
_WlanWpaRadiusSrvIP_Type=IpAddress
_WlanWpaRadiusSrvIP_Object=MibTableColumn
wlanWpaRadiusSrvIP=_WlanWpaRadiusSrvIP_Object((1,3,6,1,4,1,14125,2,2,9,21,1,12),_WlanWpaRadiusSrvIP_Type())
wlanWpaRadiusSrvIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWpaRadiusSrvIP.setStatus(_A)
class _WlanWpaRadiusSrvPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WlanWpaRadiusSrvPort_Type.__name__=_C
_WlanWpaRadiusSrvPort_Object=MibTableColumn
wlanWpaRadiusSrvPort=_WlanWpaRadiusSrvPort_Object((1,3,6,1,4,1,14125,2,2,9,21,1,13),_WlanWpaRadiusSrvPort_Type())
wlanWpaRadiusSrvPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWpaRadiusSrvPort.setStatus(_A)
class _WlanWpaRadiusSrvSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlanWpaRadiusSrvSecret_Type.__name__=_D
_WlanWpaRadiusSrvSecret_Object=MibTableColumn
wlanWpaRadiusSrvSecret=_WlanWpaRadiusSrvSecret_Object((1,3,6,1,4,1,14125,2,2,9,21,1,14),_WlanWpaRadiusSrvSecret_Type())
wlanWpaRadiusSrvSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWpaRadiusSrvSecret.setStatus(_A)
class _WlanWpaGroupKeyUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_WlanWpaGroupKeyUpdateInterval_Type.__name__=_C
_WlanWpaGroupKeyUpdateInterval_Object=MibTableColumn
wlanWpaGroupKeyUpdateInterval=_WlanWpaGroupKeyUpdateInterval_Object((1,3,6,1,4,1,14125,2,2,9,21,1,15),_WlanWpaGroupKeyUpdateInterval_Type())
wlanWpaGroupKeyUpdateInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWpaGroupKeyUpdateInterval.setStatus(_A)
_Wlansta_ObjectIdentity=ObjectIdentity
wlansta=_Wlansta_ObjectIdentity((1,3,6,1,4,1,14125,2,2,10))
class _WlanSTAAuth_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6,8,10)));namedValues=NamedValues(*((_K,1),(_L,2),(_V,6),(_W,8),(_X,10)))
_WlanSTAAuth_Type.__name__=_C
_WlanSTAAuth_Object=MibScalar
wlanSTAAuth=_WlanSTAAuth_Object((1,3,6,1,4,1,14125,2,2,10,1),_WlanSTAAuth_Type())
wlanSTAAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanSTAAuth.setStatus(_A)
class _WlanSTAEncryption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_M,1),('tkip',2),(_N,3),(_H,4)))
_WlanSTAEncryption_Type.__name__=_C
_WlanSTAEncryption_Object=MibScalar
wlanSTAEncryption=_WlanSTAEncryption_Object((1,3,6,1,4,1,14125,2,2,10,2),_WlanSTAEncryption_Type())
wlanSTAEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanSTAEncryption.setStatus(_A)
class _WlanSTAWepDefaultKeyIdx_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_WlanSTAWepDefaultKeyIdx_Type.__name__=_C
_WlanSTAWepDefaultKeyIdx_Object=MibScalar
wlanSTAWepDefaultKeyIdx=_WlanSTAWepDefaultKeyIdx_Object((1,3,6,1,4,1,14125,2,2,10,3),_WlanSTAWepDefaultKeyIdx_Type())
wlanSTAWepDefaultKeyIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanSTAWepDefaultKeyIdx.setStatus(_A)
class _WlanSTAWepKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5),ValueSizeConstraint(10,10),ValueSizeConstraint(13,13),ValueSizeConstraint(16,16),ValueSizeConstraint(26,26),ValueSizeConstraint(32,32))
_WlanSTAWepKey_Type.__name__=_D
_WlanSTAWepKey_Object=MibScalar
wlanSTAWepKey=_WlanSTAWepKey_Object((1,3,6,1,4,1,14125,2,2,10,4),_WlanSTAWepKey_Type())
wlanSTAWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanSTAWepKey.setStatus(_A)
class _WlanSTAWpapskPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlanSTAWpapskPassphrase_Type.__name__=_D
_WlanSTAWpapskPassphrase_Object=MibScalar
wlanSTAWpapskPassphrase=_WlanSTAWpapskPassphrase_Object((1,3,6,1,4,1,14125,2,2,10,5),_WlanSTAWpapskPassphrase_Type())
wlanSTAWpapskPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanSTAWpapskPassphrase.setStatus(_A)
_Wlanmesh_ObjectIdentity=ObjectIdentity
wlanmesh=_Wlanmesh_ObjectIdentity((1,3,6,1,4,1,14125,2,2,11))
class _WlanMESHSSID_Type(DisplayString):defaultValue=OctetString('EnGeniusMesh');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_WlanMESHSSID_Type.__name__=_D
_WlanMESHSSID_Object=MibScalar
wlanMESHSSID=_WlanMESHSSID_Object((1,3,6,1,4,1,14125,2,2,11,1),_WlanMESHSSID_Type())
wlanMESHSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHSSID.setStatus(_A)
class _WlanMESHGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WlanMESHGateway_Type.__name__=_C
_WlanMESHGateway_Object=MibScalar
wlanMESHGateway=_WlanMESHGateway_Object((1,3,6,1,4,1,14125,2,2,11,2),_WlanMESHGateway_Type())
wlanMESHGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHGateway.setStatus(_A)
class _WlanMESHAuth_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WlanMESHAuth_Type.__name__=_C
_WlanMESHAuth_Object=MibScalar
wlanMESHAuth=_WlanMESHAuth_Object((1,3,6,1,4,1,14125,2,2,11,4),_WlanMESHAuth_Type())
wlanMESHAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHAuth.setStatus(_A)
class _WlanMESHEncryption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_M,1),(_N,2)))
_WlanMESHEncryption_Type.__name__=_C
_WlanMESHEncryption_Object=MibScalar
wlanMESHEncryption=_WlanMESHEncryption_Object((1,3,6,1,4,1,14125,2,2,11,5),_WlanMESHEncryption_Type())
wlanMESHEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHEncryption.setStatus(_A)
class _WlanMESHWepDefaultKeyIdx_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_WlanMESHWepDefaultKeyIdx_Type.__name__=_C
_WlanMESHWepDefaultKeyIdx_Object=MibScalar
wlanMESHWepDefaultKeyIdx=_WlanMESHWepDefaultKeyIdx_Object((1,3,6,1,4,1,14125,2,2,11,6),_WlanMESHWepDefaultKeyIdx_Type())
wlanMESHWepDefaultKeyIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHWepDefaultKeyIdx.setStatus(_A)
class _WlanMESHWepKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5),ValueSizeConstraint(10,10),ValueSizeConstraint(13,13),ValueSizeConstraint(16,16),ValueSizeConstraint(26,26),ValueSizeConstraint(32,32))
_WlanMESHWepKey_Type.__name__=_D
_WlanMESHWepKey_Object=MibScalar
wlanMESHWepKey=_WlanMESHWepKey_Object((1,3,6,1,4,1,14125,2,2,11,7),_WlanMESHWepKey_Type())
wlanMESHWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHWepKey.setStatus(_A)
class _WlanMESHWpapskPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlanMESHWpapskPassphrase_Type.__name__=_D
_WlanMESHWpapskPassphrase_Object=MibScalar
wlanMESHWpapskPassphrase=_WlanMESHWpapskPassphrase_Object((1,3,6,1,4,1,14125,2,2,11,8),_WlanMESHWpapskPassphrase_Type())
wlanMESHWpapskPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMESHWpapskPassphrase.setStatus(_A)
_Wlanstawds_ObjectIdentity=ObjectIdentity
wlanstawds=_Wlanstawds_ObjectIdentity((1,3,6,1,4,1,14125,2,2,14))
class _StaWDS_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StaWDS_Type.__name__=_C
_StaWDS_Object=MibScalar
staWDS=_StaWDS_Object((1,3,6,1,4,1,14125,2,2,14,1),_StaWDS_Type())
staWDS.setMaxAccess(_B)
if mibBuilder.loadTexts:staWDS.setStatus(_A)
_Stp_ObjectIdentity=ObjectIdentity
stp=_Stp_ObjectIdentity((1,3,6,1,4,1,14125,2,2,15))
class _StpMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StpMode_Type.__name__=_C
_StpMode_Object=MibScalar
stpMode=_StpMode_Object((1,3,6,1,4,1,14125,2,2,15,1),_StpMode_Type())
stpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:stpMode.setStatus(_A)
class _StpHelloTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StpHelloTime_Type.__name__=_C
_StpHelloTime_Object=MibScalar
stpHelloTime=_StpHelloTime_Object((1,3,6,1,4,1,14125,2,2,15,2),_StpHelloTime_Type())
stpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpHelloTime.setStatus(_A)
class _StpMaxAge_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_StpMaxAge_Type.__name__=_C
_StpMaxAge_Object=MibScalar
stpMaxAge=_StpMaxAge_Object((1,3,6,1,4,1,14125,2,2,15,3),_StpMaxAge_Type())
stpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpMaxAge.setStatus(_A)
class _StpForwardDelay_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_StpForwardDelay_Type.__name__=_C
_StpForwardDelay_Object=MibScalar
stpForwardDelay=_StpForwardDelay_Object((1,3,6,1,4,1,14125,2,2,15,4),_StpForwardDelay_Type())
stpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stpForwardDelay.setStatus(_A)
class _StpPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StpPriority_Type.__name__=_C
_StpPriority_Object=MibScalar
stpPriority=_StpPriority_Object((1,3,6,1,4,1,14125,2,2,15,5),_StpPriority_Type())
stpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPriority.setStatus(_A)
_Snmp_ObjectIdentity=ObjectIdentity
snmp=_Snmp_ObjectIdentity((1,3,6,1,4,1,14125,2,2,16))
class _SnmpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnmpEnable_Type.__name__=_C
_SnmpEnable_Object=MibScalar
snmpEnable=_SnmpEnable_Object((1,3,6,1,4,1,14125,2,2,16,1),_SnmpEnable_Type())
snmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEnable.setStatus(_A)
class _SnmpCmntyRO_Type(DisplayString):defaultValue=OctetString(_Y);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SnmpCmntyRO_Type.__name__=_D
_SnmpCmntyRO_Object=MibScalar
snmpCmntyRO=_SnmpCmntyRO_Object((1,3,6,1,4,1,14125,2,2,16,2),_SnmpCmntyRO_Type())
snmpCmntyRO.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpCmntyRO.setStatus(_A)
class _SnmpCmntyRW_Type(DisplayString):defaultValue=OctetString('private');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SnmpCmntyRW_Type.__name__=_D
_SnmpCmntyRW_Object=MibScalar
snmpCmntyRW=_SnmpCmntyRW_Object((1,3,6,1,4,1,14125,2,2,16,3),_SnmpCmntyRW_Type())
snmpCmntyRW.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpCmntyRW.setStatus(_A)
_SnmpTrapDstIP_Type=IpAddress
_SnmpTrapDstIP_Object=MibScalar
snmpTrapDstIP=_SnmpTrapDstIP_Object((1,3,6,1,4,1,14125,2,2,16,4),_SnmpTrapDstIP_Type())
snmpTrapDstIP.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapDstIP.setStatus(_A)
class _SnmpTrapCmnty_Type(DisplayString):defaultValue=OctetString(_Y);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SnmpTrapCmnty_Type.__name__=_D
_SnmpTrapCmnty_Object=MibScalar
snmpTrapCmnty=_SnmpTrapCmnty_Object((1,3,6,1,4,1,14125,2,2,16,5),_SnmpTrapCmnty_Type())
snmpTrapCmnty.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapCmnty.setStatus(_A)
class _SnmpCont_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SnmpCont_Type.__name__=_D
_SnmpCont_Object=MibScalar
snmpCont=_SnmpCont_Object((1,3,6,1,4,1,14125,2,2,16,6),_SnmpCont_Type())
snmpCont.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpCont.setStatus(_A)
class _SnmpLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SnmpLocation_Type.__name__=_D
_SnmpLocation_Object=MibScalar
snmpLocation=_SnmpLocation_Object((1,3,6,1,4,1,14125,2,2,16,7),_SnmpLocation_Type())
snmpLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpLocation.setStatus(_A)
class _SysObjectID_Type(DisplayString):defaultValue=OctetString('1.3.6.1.4.1.14125');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SysObjectID_Type.__name__=_D
_SysObjectID_Object=MibScalar
sysObjectID=_SysObjectID_Object((1,3,6,1,4,1,14125,2,2,16,8),_SysObjectID_Type())
sysObjectID.setMaxAccess(_G)
if mibBuilder.loadTexts:sysObjectID.setStatus(_A)
_Wmm_ObjectIdentity=ObjectIdentity
wmm=_Wmm_ObjectIdentity((1,3,6,1,4,1,14125,2,2,17))
class _WmmEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WmmEnable_Type.__name__=_C
_WmmEnable_Object=MibScalar
wmmEnable=_WmmEnable_Object((1,3,6,1,4,1,14125,2,2,17,1),_WmmEnable_Type())
wmmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wmmEnable.setStatus(_A)
_Logemail_ObjectIdentity=ObjectIdentity
logemail=_Logemail_ObjectIdentity((1,3,6,1,4,1,14125,2,2,20))
class _LogServerEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LogServerEnable_Type.__name__=_C
_LogServerEnable_Object=MibScalar
logServerEnable=_LogServerEnable_Object((1,3,6,1,4,1,14125,2,2,20,1),_LogServerEnable_Type())
logServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:logServerEnable.setStatus(_A)
_LogServerIP_Type=IpAddress
_LogServerIP_Object=MibScalar
logServerIP=_LogServerIP_Object((1,3,6,1,4,1,14125,2,2,20,2),_LogServerIP_Type())
logServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:logServerIP.setStatus(_A)
class _LogLocalEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LogLocalEnable_Type.__name__=_C
_LogLocalEnable_Object=MibScalar
logLocalEnable=_LogLocalEnable_Object((1,3,6,1,4,1,14125,2,2,20,3),_LogLocalEnable_Type())
logLocalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:logLocalEnable.setStatus(_A)
class _LogLevel_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('information',6),('debug',7),('all',8)))
_LogLevel_Type.__name__=_C
_LogLevel_Object=MibScalar
logLevel=_LogLevel_Object((1,3,6,1,4,1,14125,2,2,20,4),_LogLevel_Type())
logLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:logLevel.setStatus(_A)
_Vpn_ObjectIdentity=ObjectIdentity
vpn=_Vpn_ObjectIdentity((1,3,6,1,4,1,14125,2,2,21))
class _VpnPassthroughPPTP_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VpnPassthroughPPTP_Type.__name__=_C
_VpnPassthroughPPTP_Object=MibScalar
vpnPassthroughPPTP=_VpnPassthroughPPTP_Object((1,3,6,1,4,1,14125,2,2,21,1),_VpnPassthroughPPTP_Type())
vpnPassthroughPPTP.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnPassthroughPPTP.setStatus(_A)
class _VpnPassthroughL2TP_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VpnPassthroughL2TP_Type.__name__=_C
_VpnPassthroughL2TP_Object=MibScalar
vpnPassthroughL2TP=_VpnPassthroughL2TP_Object((1,3,6,1,4,1,14125,2,2,21,2),_VpnPassthroughL2TP_Type())
vpnPassthroughL2TP.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnPassthroughL2TP.setStatus(_A)
class _VpnPassthroughIPSec_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VpnPassthroughIPSec_Type.__name__=_C
_VpnPassthroughIPSec_Object=MibScalar
vpnPassthroughIPSec=_VpnPassthroughIPSec_Object((1,3,6,1,4,1,14125,2,2,21,3),_VpnPassthroughIPSec_Type())
vpnPassthroughIPSec.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnPassthroughIPSec.setStatus(_A)
_Traffic_ObjectIdentity=ObjectIdentity
traffic=_Traffic_ObjectIdentity((1,3,6,1,4,1,14125,2,2,22))
class _TcEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcEnable_Type.__name__=_C
_TcEnable_Object=MibScalar
tcEnable=_TcEnable_Object((1,3,6,1,4,1,14125,2,2,22,1),_TcEnable_Type())
tcEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tcEnable.setStatus(_A)
class _TcInRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_TcInRate_Type.__name__=_C
_TcInRate_Object=MibScalar
tcInRate=_TcInRate_Object((1,3,6,1,4,1,14125,2,2,22,2),_TcInRate_Type())
tcInRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tcInRate.setStatus(_A)
class _TcInBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_TcInBurst_Type.__name__=_C
_TcInBurst_Object=MibScalar
tcInBurst=_TcInBurst_Object((1,3,6,1,4,1,14125,2,2,22,3),_TcInBurst_Type())
tcInBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:tcInBurst.setStatus(_A)
class _TcOutRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_TcOutRate_Type.__name__=_C
_TcOutRate_Object=MibScalar
tcOutRate=_TcOutRate_Object((1,3,6,1,4,1,14125,2,2,22,4),_TcOutRate_Type())
tcOutRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tcOutRate.setStatus(_A)
class _TcOutBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_TcOutBurst_Type.__name__=_C
_TcOutBurst_Object=MibScalar
tcOutBurst=_TcOutBurst_Object((1,3,6,1,4,1,14125,2,2,22,5),_TcOutBurst_Type())
tcOutBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:tcOutBurst.setStatus(_A)
_Command_ObjectIdentity=ObjectIdentity
command=_Command_ObjectIdentity((1,3,6,1,4,1,14125,2,3))
_SaveCmd_ObjectIdentity=ObjectIdentity
saveCmd=_SaveCmd_ObjectIdentity((1,3,6,1,4,1,14125,2,3,1))
class _ExecuteSaveCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ExecuteSaveCmd_Type.__name__=_C
_ExecuteSaveCmd_Object=MibScalar
executeSaveCmd=_ExecuteSaveCmd_Object((1,3,6,1,4,1,14125,2,3,1,1),_ExecuteSaveCmd_Type())
executeSaveCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:executeSaveCmd.setStatus(_A)
_ResetCmd_ObjectIdentity=ObjectIdentity
resetCmd=_ResetCmd_ObjectIdentity((1,3,6,1,4,1,14125,2,3,2))
class _ExecuteResetCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ExecuteResetCmd_Type.__name__=_C
_ExecuteResetCmd_Object=MibScalar
executeResetCmd=_ExecuteResetCmd_Object((1,3,6,1,4,1,14125,2,3,2,1),_ExecuteResetCmd_Type())
executeResetCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:executeResetCmd.setStatus(_A)
_RebootCmd_ObjectIdentity=ObjectIdentity
rebootCmd=_RebootCmd_ObjectIdentity((1,3,6,1,4,1,14125,2,3,3))
class _ExecuteRebootCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_ExecuteRebootCmd_Type.__name__=_C
_ExecuteRebootCmd_Object=MibScalar
executeRebootCmd=_ExecuteRebootCmd_Object((1,3,6,1,4,1,14125,2,3,3,1),_ExecuteRebootCmd_Type())
executeRebootCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:executeRebootCmd.setStatus(_A)
mibBuilder.exportSymbols(_T,**{'engenius':engenius,'engeniusprivate':engeniusprivate,'status':status,'system':system,'systemName':systemName,'sysPassword':sysPassword,'errMsg':errMsg,'statusWLANSTAAssoc':statusWLANSTAAssoc,'modelName':modelName,'wirelessMacAddress':wirelessMacAddress,'wanIPAddress':wanIPAddress,'wanSubnetMask':wanSubnetMask,'configuration':configuration,'wan':wan,'wanConnectionType':wanConnectionType,'wanGeneralAccount':wanGeneralAccount,'wanGeneralDomain':wanGeneralDomain,'wanGeneralIP':wanGeneralIP,'wanGeneralSubnetMask':wanGeneralSubnetMask,'wanGeneralGateway':wanGeneralGateway,'pppoe':pppoe,'wanPPPoELoginName':wanPPPoELoginName,'wanPPPoEPassword':wanPPPoEPassword,'wanPPPoEServiceName':wanPPPoEServiceName,'wanPPPoEConnectionType':wanPPPoEConnectionType,'wanPPPoEMaxIdleTime':wanPPPoEMaxIdleTime,'wanPPPoERedialPeriod':wanPPPoERedialPeriod,'dns':dns,'wanDNSSourc':wanDNSSourc,'wanPrimaryDNSIP':wanPrimaryDNSIP,'wanSecondaryDNSIP':wanSecondaryDNSIP,'mtu':mtu,'wanMTUMode':wanMTUMode,'wanMTU':wanMTU,'pppoeMTU':pppoeMTU,'landhcp':landhcp,'lanDHCPC':lanDHCPC,'lanIP':lanIP,'lanSubnetmask':lanSubnetmask,'lanGatewayIP':lanGatewayIP,'lanWINSAddr':lanWINSAddr,'lanDHCPSrvEnable':lanDHCPSrvEnable,'lanDHCPSrvStartAddr':lanDHCPSrvStartAddr,'lanDHCPSrvStopAddr':lanDHCPSrvStopAddr,'ntp':ntp,'timeSettingMode':timeSettingMode,'userNTPSrvMode':userNTPSrvMode,'userNTPSrvIP':userNTPSrvIP,'timeZone':timeZone,_J:admin,'username':username,'remoteManagementEnable':remoteManagementEnable,'remoteUpgradeEnable':remoteUpgradeEnable,'remoteManagementPort':remoteManagementPort,'remoteManagementVLANID':remoteManagementVLANID,'wlan':wlan,'wlanMode':wlanMode,'chanBwMode':chanBwMode,'wlanaSSID':wlanaSSID,'wlanOpMode':wlanOpMode,'wlanCountryCode':wlanCountryCode,'wlanCountry':wlanCountry,'wlanChannel':wlanChannel,'wlanACLMode':wlanACLMode,'wlanOutdoorDistance':wlanOutdoorDistance,'wlanDataRate':wlanDataRate,'wlanTxPower':wlanTxPower,'antennasel':antennasel,'wlanBeaconInterval':wlanBeaconInterval,'wlanRTSTh':wlanRTSTh,'wlanFragLen':wlanFragLen,'wlanProtmode':wlanProtmode,'wlanPreferBSSID':wlanPreferBSSID,'wlanTable':wlanTable,'wlanTableEntry':wlanTableEntry,_U:wlanTableIndex,'wlanEnable':wlanEnable,'wlanSSID':wlanSSID,'wlanHideSSID':wlanHideSSID,'wlanStaSeparation':wlanStaSeparation,'wlanVLANID':wlanVLANID,'wlanAuth':wlanAuth,'wlanEncryption':wlanEncryption,'wlanWepDefaultKeyIdx':wlanWepDefaultKeyIdx,'wlanWepKey':wlanWepKey,'wlanWpapskPassphrase':wlanWpapskPassphrase,'wlanWpaRadiusSrvIP':wlanWpaRadiusSrvIP,'wlanWpaRadiusSrvPort':wlanWpaRadiusSrvPort,'wlanWpaRadiusSrvSecret':wlanWpaRadiusSrvSecret,'wlanWpaGroupKeyUpdateInterval':wlanWpaGroupKeyUpdateInterval,'wlansta':wlansta,'wlanSTAAuth':wlanSTAAuth,'wlanSTAEncryption':wlanSTAEncryption,'wlanSTAWepDefaultKeyIdx':wlanSTAWepDefaultKeyIdx,'wlanSTAWepKey':wlanSTAWepKey,'wlanSTAWpapskPassphrase':wlanSTAWpapskPassphrase,'wlanmesh':wlanmesh,'wlanMESHSSID':wlanMESHSSID,'wlanMESHGateway':wlanMESHGateway,'wlanMESHAuth':wlanMESHAuth,'wlanMESHEncryption':wlanMESHEncryption,'wlanMESHWepDefaultKeyIdx':wlanMESHWepDefaultKeyIdx,'wlanMESHWepKey':wlanMESHWepKey,'wlanMESHWpapskPassphrase':wlanMESHWpapskPassphrase,'wlanstawds':wlanstawds,'staWDS':staWDS,'stp':stp,'stpMode':stpMode,'stpHelloTime':stpHelloTime,'stpMaxAge':stpMaxAge,'stpForwardDelay':stpForwardDelay,'stpPriority':stpPriority,'snmp':snmp,'snmpEnable':snmpEnable,'snmpCmntyRO':snmpCmntyRO,'snmpCmntyRW':snmpCmntyRW,'snmpTrapDstIP':snmpTrapDstIP,'snmpTrapCmnty':snmpTrapCmnty,'snmpCont':snmpCont,'snmpLocation':snmpLocation,'sysObjectID':sysObjectID,'wmm':wmm,'wmmEnable':wmmEnable,'logemail':logemail,'logServerEnable':logServerEnable,'logServerIP':logServerIP,'logLocalEnable':logLocalEnable,'logLevel':logLevel,'vpn':vpn,'vpnPassthroughPPTP':vpnPassthroughPPTP,'vpnPassthroughL2TP':vpnPassthroughL2TP,'vpnPassthroughIPSec':vpnPassthroughIPSec,'traffic':traffic,'tcEnable':tcEnable,'tcInRate':tcInRate,'tcInBurst':tcInBurst,'tcOutRate':tcOutRate,'tcOutBurst':tcOutBurst,'command':command,'saveCmd':saveCmd,'executeSaveCmd':executeSaveCmd,'resetCmd':resetCmd,'executeResetCmd':executeResetCmd,'rebootCmd':rebootCmd,'executeRebootCmd':executeRebootCmd})