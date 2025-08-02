_AC='remoteIpIndex'
_AB='accessibleIpListIndex'
_AA='key-128-bits'
_A9='key-64-bits'
_A8='open-system'
_A7='w802_11b_g'
_A6='channel_165'
_A5='channel_161'
_A4='channel_157'
_A3='channel_153'
_A2='channel_149'
_A1='channel_140'
_A0='channel_136'
_z='channel_132'
_y='channel_128'
_x='channel_124'
_w='channel_120'
_v='channel_116'
_u='channel_112'
_t='channel_108'
_s='channel_104'
_r='channel_100'
_q='channel_64'
_p='channel_60'
_o='channel_56'
_n='channel_52'
_m='channel_48'
_l='channel_44'
_k='channel_40'
_j='channel_36'
_i='channel_13'
_h='channel_12'
_g='channel_11'
_f='channel_10'
_e='channel_9'
_d='channel_8'
_c='channel_7'
_b='channel_6'
_a='channel_5'
_Z='channel_4'
_Y='channel_3'
_X='channel_2'
_W='channel_1'
_V='n_a'
_U='installed'
_T='not-installed'
_S='profileIndex'
_R='bootp'
_Q='dhcp'
_P='static'
_O='none'
_N='always-low'
_M='always-high'
_L='write-only'
_K='on'
_J='off'
_I='DisplayString'
_H='portIndex'
_G='MOXA-W2x50A-MIB'
_F='enable'
_E='disable'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'MacAddress','PhysAddress','TextualConvention')
w2x50A=ModuleIdentity((1,3,6,1,4,1,8691,2,13))
class PortList(TextualConvention,OctetString):status=_A
_Moxa_ObjectIdentity=ObjectIdentity
moxa=_Moxa_ObjectIdentity((1,3,6,1,4,1,8691))
_Nport_ObjectIdentity=ObjectIdentity
nport=_Nport_ObjectIdentity((1,3,6,1,4,1,8691,2))
_SwMgmt_ObjectIdentity=ObjectIdentity
swMgmt=_SwMgmt_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1))
_Overview_ObjectIdentity=ObjectIdentity
overview=_Overview_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,1))
_ModelName_Type=DisplayString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,8691,2,13,1,1,1),_ModelName_Type())
modelName.setMaxAccess(_D)
if mibBuilder.loadTexts:modelName.setStatus(_A)
_SerialNumber_Type=Integer32
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,8691,2,13,1,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,8691,2,13,1,1,3),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
_EthIPAddress_Type=DisplayString
_EthIPAddress_Object=MibScalar
ethIPAddress=_EthIPAddress_Object((1,3,6,1,4,1,8691,2,13,1,1,4),_EthIPAddress_Type())
ethIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIPAddress.setStatus(_A)
_EthMacAddress_Type=MacAddress
_EthMacAddress_Object=MibScalar
ethMacAddress=_EthMacAddress_Object((1,3,6,1,4,1,8691,2,13,1,1,5),_EthMacAddress_Type())
ethMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ethMacAddress.setStatus(_A)
_WlanIPAddress_Type=DisplayString
_WlanIPAddress_Object=MibScalar
wlanIPAddress=_WlanIPAddress_Object((1,3,6,1,4,1,8691,2,13,1,1,6),_WlanIPAddress_Type())
wlanIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIPAddress.setStatus(_A)
_WlanMacAddress_Type=MacAddress
_WlanMacAddress_Object=MibScalar
wlanMacAddress=_WlanMacAddress_Object((1,3,6,1,4,1,8691,2,13,1,1,7),_WlanMacAddress_Type())
wlanMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMacAddress.setStatus(_A)
_WlanSSID_Type=DisplayString
_WlanSSID_Object=MibScalar
wlanSSID=_WlanSSID_Object((1,3,6,1,4,1,8691,2,13,1,1,8),_WlanSSID_Type())
wlanSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanSSID.setStatus(_A)
_WlanNetworkType_Type=DisplayString
_WlanNetworkType_Object=MibScalar
wlanNetworkType=_WlanNetworkType_Object((1,3,6,1,4,1,8691,2,13,1,1,9),_WlanNetworkType_Type())
wlanNetworkType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanNetworkType.setStatus(_A)
_WlanSecurityMode_Type=DisplayString
_WlanSecurityMode_Object=MibScalar
wlanSecurityMode=_WlanSecurityMode_Object((1,3,6,1,4,1,8691,2,13,1,1,10),_WlanSecurityMode_Type())
wlanSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanSecurityMode.setStatus(_A)
_WlanRFType_Type=DisplayString
_WlanRFType_Object=MibScalar
wlanRFType=_WlanRFType_Object((1,3,6,1,4,1,8691,2,13,1,1,11),_WlanRFType_Type())
wlanRFType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanRFType.setStatus(_A)
_WlanCountryCode_Type=DisplayString
_WlanCountryCode_Object=MibScalar
wlanCountryCode=_WlanCountryCode_Object((1,3,6,1,4,1,8691,2,13,1,1,12),_WlanCountryCode_Type())
wlanCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanCountryCode.setStatus(_A)
_WlanFastRoaming_Type=DisplayString
_WlanFastRoaming_Object=MibScalar
wlanFastRoaming=_WlanFastRoaming_Object((1,3,6,1,4,1,8691,2,13,1,1,13),_WlanFastRoaming_Type())
wlanFastRoaming.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanFastRoaming.setStatus(_A)
_ActiveNetworkPort_Type=DisplayString
_ActiveNetworkPort_Object=MibScalar
activeNetworkPort=_ActiveNetworkPort_Object((1,3,6,1,4,1,8691,2,13,1,1,14),_ActiveNetworkPort_Type())
activeNetworkPort.setMaxAccess(_D)
if mibBuilder.loadTexts:activeNetworkPort.setStatus(_A)
_UpTime_Type=DisplayString
_UpTime_Object=MibScalar
upTime=_UpTime_Object((1,3,6,1,4,1,8691,2,13,1,1,15),_UpTime_Type())
upTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upTime.setStatus(_A)
_SerialPort1_Type=DisplayString
_SerialPort1_Object=MibScalar
serialPort1=_SerialPort1_Object((1,3,6,1,4,1,8691,2,13,1,1,16),_SerialPort1_Type())
serialPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:serialPort1.setStatus(_A)
_SerialPort2_Type=DisplayString
_SerialPort2_Object=MibScalar
serialPort2=_SerialPort2_Object((1,3,6,1,4,1,8691,2,13,1,1,17),_SerialPort2_Type())
serialPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:serialPort2.setStatus(_A)
_BasicSetting_ObjectIdentity=ObjectIdentity
basicSetting=_BasicSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,2))
_ServerSetting_ObjectIdentity=ObjectIdentity
serverSetting=_ServerSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,2,1))
_ServerName_Type=DisplayString
_ServerName_Object=MibScalar
serverName=_ServerName_Object((1,3,6,1,4,1,8691,2,13,1,2,1,1),_ServerName_Type())
serverName.setMaxAccess(_B)
if mibBuilder.loadTexts:serverName.setStatus(_A)
_ServerLocation_Type=DisplayString
_ServerLocation_Object=MibScalar
serverLocation=_ServerLocation_Object((1,3,6,1,4,1,8691,2,13,1,2,1,2),_ServerLocation_Type())
serverLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:serverLocation.setStatus(_A)
_TimeSetting_ObjectIdentity=ObjectIdentity
timeSetting=_TimeSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,2,2))
class _TimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63)));namedValues=NamedValues(*(('GMT-1200_Eniwetok-Kwajalein',0),('GMT-1100_Midway-Island-Samoa',1),('GMT-1000_Hawaii',2),('GMT-0900_Alaska',3),('GMT-0800_Pacific-Time-US_Canada-Tijuana',4),('GMT-0700_Arizona',5),('GMT-0700_Mountain-Time-US_Canada',6),('GMT-0600_Central-Time-US_Canada',7),('GMT-0600_Mexico-City-Tegucigalpa',8),('GMT-0600_Saskatchewan',9),('GMT-0500_Bogota-Lima-Quito',10),('GMT-0500_Eastern-Time-US_Canada',11),('GMT-0500_Indiana-East',12),('GMT-0430_Caracas',13),('GMT-0400_Atlantic-Time-Canada',14),('GMT-0400_Georgetown-La-Paz',15),('GMT-0400_Santiago',16),('GMT-0330_Newfoundland',17),('GMT-0300_Brasilia',18),('GMT-0300_Buenos-Aires',19),('GMT-0200_Mid-Atlantic',20),('GMT-0100_Azores-Cape-Verde-Is',21),('GMT_Casabanca-Monrovia',22),('GMT_Greenich-Mean-Time_Dublin-Edinburgh-Lisbon-London',23),('GMT_0100_Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna',24),('GMT_0100_Belgrade-Bratislava-Budapest-Ljubljana-Prague',25),('GMT_0100_Brussels-Copenhagen-Madrid-Paris-Vilnius',26),('GMT_0100_Sarajevo-Skopje-Warsaw-Zagreb',27),('GMT_0200_Athens-Istanbul-Minsk',28),('GMT_0200_Bucharest',29),('GMT_0200_Cairo',30),('GMT_0200_Harare-Pretoria',31),('GMT_0200_Helsinki-Riga-Sofia-Tallinn',32),('GMT_0200_Jerusalem',33),('GMT_0300_Baghdad-Kuwait-Riyadh',34),('GMT_0300_Moscow-St-Petersburg-Volgograd',35),('GMT_0300_Mairobi',36),('GMT_0330_Tehran',37),('GMT_0400_Abu-Dhabi-Muscat',38),('GMT_0400_Baku-Tbilisi',39),('GMT_0430_Kabul',40),('GMT_0500_Ekaterinburg',41),('GMT_0500_Islamabad-Karachi-Tashkent',42),('GMT_0530_Bombay-Calcutta-Madras-New-Delhi',43),('GMT_0600_Astana-Almaty-Dhaka',44),('GMT_0600_Colombo',45),('GMT_0700_Bangkok-Hanoi-Jakarta',46),('GMT_0800_Beijing-Chongqing-Hong-Kong-Urumqi',47),('GMT_0800_Perth',48),('GMT_0800_Singapore',49),('GMT_0800_Taipei',50),('GMT_0900_Osaka-Sapporo-Tokyo',51),('GMT_0900_Seoul',52),('GMT_0900_Yakutsk',53),('GMT_0930_Adelaide',54),('GMT_0930_Darwin',55),('GMT_1000_Brisbane',56),('GMT_1000_Canberra-Melbourne-Sydney',57),('GMT_1000_Guam-Port-Moresby',58),('GMT_1000_Hobart',59),('GMT_1000_Vladivostok',60),('GMT_1100_Magadan-Solomon-Is-New-Caledonia',61),('GMT_1200_Auckland-Wllington',62),('GMT_1200_Fiji-Kamchatka-Marshall-Is',63)))
_TimeZone_Type.__name__=_C
_TimeZone_Object=MibScalar
timeZone=_TimeZone_Object((1,3,6,1,4,1,8691,2,13,1,2,2,1),_TimeZone_Type())
timeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:timeZone.setStatus(_A)
class _LocalTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_LocalTime_Type.__name__=_I
_LocalTime_Object=MibScalar
localTime=_LocalTime_Object((1,3,6,1,4,1,8691,2,13,1,2,2,2),_LocalTime_Type())
localTime.setMaxAccess(_B)
if mibBuilder.loadTexts:localTime.setStatus(_A)
_TimeServer_Type=DisplayString
_TimeServer_Object=MibScalar
timeServer=_TimeServer_Object((1,3,6,1,4,1,8691,2,13,1,2,2,3),_TimeServer_Type())
timeServer.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer.setStatus(_A)
_NetworkSetting_ObjectIdentity=ObjectIdentity
networkSetting=_NetworkSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3))
_GeneralSetting_ObjectIdentity=ObjectIdentity
generalSetting=_GeneralSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,1))
_DnsServer1IpAddr_Type=IpAddress
_DnsServer1IpAddr_Object=MibScalar
dnsServer1IpAddr=_DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,2,13,1,3,1,1),_DnsServer1IpAddr_Type())
dnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer1IpAddr.setStatus(_A)
_DnsServer2IpAddr_Type=IpAddress
_DnsServer2IpAddr_Object=MibScalar
dnsServer2IpAddr=_DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,2,13,1,3,1,2),_DnsServer2IpAddr_Type())
dnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer2IpAddr.setStatus(_A)
_EthernetSetting_ObjectIdentity=ObjectIdentity
ethernetSetting=_EthernetSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,2))
class _EthIpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2)))
_EthIpConfiguration_Type.__name__=_C
_EthIpConfiguration_Object=MibScalar
ethIpConfiguration=_EthIpConfiguration_Object((1,3,6,1,4,1,8691,2,13,1,3,2,1),_EthIpConfiguration_Type())
ethIpConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIpConfiguration.setStatus(_A)
_EthIpAddress_Type=IpAddress
_EthIpAddress_Object=MibScalar
ethIpAddress=_EthIpAddress_Object((1,3,6,1,4,1,8691,2,13,1,3,2,2),_EthIpAddress_Type())
ethIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIpAddress.setStatus(_A)
_EthNetMask_Type=IpAddress
_EthNetMask_Object=MibScalar
ethNetMask=_EthNetMask_Object((1,3,6,1,4,1,8691,2,13,1,3,2,3),_EthNetMask_Type())
ethNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ethNetMask.setStatus(_A)
_EthDefaultGateway_Type=IpAddress
_EthDefaultGateway_Object=MibScalar
ethDefaultGateway=_EthDefaultGateway_Object((1,3,6,1,4,1,8691,2,13,1,3,2,4),_EthDefaultGateway_Type())
ethDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDefaultGateway.setStatus(_A)
class _EthBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EthBridgeMode_Type.__name__=_C
_EthBridgeMode_Object=MibScalar
ethBridgeMode=_EthBridgeMode_Object((1,3,6,1,4,1,8691,2,13,1,3,2,5),_EthBridgeMode_Type())
ethBridgeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBridgeMode.setStatus(_A)
_WlanSetting_ObjectIdentity=ObjectIdentity
wlanSetting=_WlanSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,3))
class _WlanIpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2)))
_WlanIpConfiguration_Type.__name__=_C
_WlanIpConfiguration_Object=MibScalar
wlanIpConfiguration=_WlanIpConfiguration_Object((1,3,6,1,4,1,8691,2,13,1,3,3,1),_WlanIpConfiguration_Type())
wlanIpConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIpConfiguration.setStatus(_A)
_WlanIpAddress_Type=IpAddress
_WlanIpAddress_Object=MibScalar
wlanIpAddress=_WlanIpAddress_Object((1,3,6,1,4,1,8691,2,13,1,3,3,2),_WlanIpAddress_Type())
wlanIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIpAddress.setStatus(_A)
_WlanNetMask_Type=IpAddress
_WlanNetMask_Object=MibScalar
wlanNetMask=_WlanNetMask_Object((1,3,6,1,4,1,8691,2,13,1,3,3,3),_WlanNetMask_Type())
wlanNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanNetMask.setStatus(_A)
_WlanDefaultGateway_Type=IpAddress
_WlanDefaultGateway_Object=MibScalar
wlanDefaultGateway=_WlanDefaultGateway_Object((1,3,6,1,4,1,8691,2,13,1,3,3,4),_WlanDefaultGateway_Type())
wlanDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanDefaultGateway.setStatus(_A)
_ProfileSetting_ObjectIdentity=ObjectIdentity
profileSetting=_ProfileSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4))
class _NetworkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ad-hoc',0),('infrastructure',1)))
_NetworkType_Type.__name__=_C
_NetworkType_Object=MibScalar
networkType=_NetworkType_Object((1,3,6,1,4,1,8691,2,13,1,3,4,1),_NetworkType_Type())
networkType.setMaxAccess(_B)
if mibBuilder.loadTexts:networkType.setStatus(_A)
_AdhocProfile_ObjectIdentity=ObjectIdentity
adhocProfile=_AdhocProfile_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4,2))
_AdhocGeneralSetting_ObjectIdentity=ObjectIdentity
adhocGeneralSetting=_AdhocGeneralSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4,2,1))
class _AdhocProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdhocProfileName_Type.__name__=_I
_AdhocProfileName_Object=MibScalar
adhocProfileName=_AdhocProfileName_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,1,1),_AdhocProfileName_Type())
adhocProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocProfileName.setStatus(_A)
class _AdhocRFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_A7,2))
_AdhocRFType_Type.__name__=_C
_AdhocRFType_Object=MibScalar
adhocRFType=_AdhocRFType_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,1,2),_AdhocRFType_Type())
adhocRFType.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocRFType.setStatus(_A)
class _AdhocWlanSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdhocWlanSSID_Type.__name__=_I
_AdhocWlanSSID_Object=MibScalar
adhocWlanSSID=_AdhocWlanSSID_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,1,3),_AdhocWlanSSID_Type())
adhocWlanSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWlanSSID.setStatus(_A)
_AdhocChannel_Type=Integer32
_AdhocChannel_Object=MibScalar
adhocChannel=_AdhocChannel_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,1,4),_AdhocChannel_Type())
adhocChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocChannel.setStatus(_A)
_AdhocSecuritySetting_ObjectIdentity=ObjectIdentity
adhocSecuritySetting=_AdhocSecuritySetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4,2,2))
class _AdhocAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_A8,0))
_AdhocAuthentication_Type.__name__=_C
_AdhocAuthentication_Object=MibScalar
adhocAuthentication=_AdhocAuthentication_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,2,1),_AdhocAuthentication_Type())
adhocAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:adhocAuthentication.setStatus(_A)
class _AdhocEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('wep',1)))
_AdhocEncryption_Type.__name__=_C
_AdhocEncryption_Object=MibScalar
adhocEncryption=_AdhocEncryption_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,2,2),_AdhocEncryption_Type())
adhocEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocEncryption.setStatus(_A)
class _AdhocWepKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_A9,0),(_AA,1)))
_AdhocWepKeyLength_Type.__name__=_C
_AdhocWepKeyLength_Object=MibScalar
adhocWepKeyLength=_AdhocWepKeyLength_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,2,3),_AdhocWepKeyLength_Type())
adhocWepKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyLength.setStatus(_A)
class _AdhocWepKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AdhocWepKeyIndex_Type.__name__=_C
_AdhocWepKeyIndex_Object=MibScalar
adhocWepKeyIndex=_AdhocWepKeyIndex_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,2,4),_AdhocWepKeyIndex_Type())
adhocWepKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyIndex.setStatus(_A)
class _AdhocWepKeyPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_AdhocWepKeyPassphrase_Type.__name__=_I
_AdhocWepKeyPassphrase_Object=MibScalar
adhocWepKeyPassphrase=_AdhocWepKeyPassphrase_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,2,5),_AdhocWepKeyPassphrase_Type())
adhocWepKeyPassphrase.setMaxAccess(_L)
if mibBuilder.loadTexts:adhocWepKeyPassphrase.setStatus(_A)
class _AdhocWepKeyFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascii',0),('hex',1)))
_AdhocWepKeyFormat_Type.__name__=_C
_AdhocWepKeyFormat_Object=MibScalar
adhocWepKeyFormat=_AdhocWepKeyFormat_Object((1,3,6,1,4,1,8691,2,13,1,3,4,2,2,6),_AdhocWepKeyFormat_Type())
adhocWepKeyFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyFormat.setStatus(_A)
_InfrastructureProfile_ObjectIdentity=ObjectIdentity
infrastructureProfile=_InfrastructureProfile_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4,3))
_InfraGeneralSetting_ObjectIdentity=ObjectIdentity
infraGeneralSetting=_InfraGeneralSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4,3,1))
_InfraGeneralSettingTable_Object=MibTable
infraGeneralSettingTable=_InfraGeneralSettingTable_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,1,1))
if mibBuilder.loadTexts:infraGeneralSettingTable.setStatus(_A)
_InfraGeneralSettingEntry_Object=MibTableRow
infraGeneralSettingEntry=_InfraGeneralSettingEntry_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,1,1,1))
infraGeneralSettingEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:infraGeneralSettingEntry.setStatus(_A)
class _ProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('profile1',1))
_ProfileIndex_Type.__name__=_C
_ProfileIndex_Object=MibTableColumn
profileIndex=_ProfileIndex_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,1,1,1,1),_ProfileIndex_Type())
profileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:profileIndex.setStatus(_A)
class _ProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProfileName_Type.__name__=_I
_ProfileName_Object=MibTableColumn
profileName=_ProfileName_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,1,1,1,2),_ProfileName_Type())
profileName.setMaxAccess(_B)
if mibBuilder.loadTexts:profileName.setStatus(_A)
class _ProfileRFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('auto',0),('w802_11a',1),(_A7,2),('w802_11a_n',3),('w802_11b_g_n',4)))
_ProfileRFType_Type.__name__=_C
_ProfileRFType_Object=MibTableColumn
profileRFType=_ProfileRFType_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,1,1,1,3),_ProfileRFType_Type())
profileRFType.setMaxAccess(_B)
if mibBuilder.loadTexts:profileRFType.setStatus(_A)
class _ProfileWlanSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProfileWlanSSID_Type.__name__=_I
_ProfileWlanSSID_Object=MibTableColumn
profileWlanSSID=_ProfileWlanSSID_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,1,1,1,4),_ProfileWlanSSID_Type())
profileWlanSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:profileWlanSSID.setStatus(_A)
_SecuritySetting_ObjectIdentity=ObjectIdentity
securitySetting=_SecuritySetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,4,3,2))
_SecuritySettingTable_Object=MibTable
securitySettingTable=_SecuritySettingTable_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1))
if mibBuilder.loadTexts:securitySettingTable.setStatus(_A)
_SecuritySettingEntry_Object=MibTableRow
securitySettingEntry=_SecuritySettingEntry_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1))
securitySettingEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:securitySettingEntry.setStatus(_A)
class _Authentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A8,0),('shared-key',1),('wpa',2),('wpa-psk',3),('wpa2',4),('wpa2-psk',5)))
_Authentication_Type.__name__=_C
_Authentication_Object=MibTableColumn
authentication=_Authentication_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,1),_Authentication_Type())
authentication.setMaxAccess(_B)
if mibBuilder.loadTexts:authentication.setStatus(_A)
class _Encryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('wep',1),('tkip',2),('aes-ccmp',3)))
_Encryption_Type.__name__=_C
_Encryption_Object=MibTableColumn
encryption=_Encryption_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,2),_Encryption_Type())
encryption.setMaxAccess(_B)
if mibBuilder.loadTexts:encryption.setStatus(_A)
class _WepKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_A9,0),(_AA,1)))
_WepKeyLength_Type.__name__=_C
_WepKeyLength_Object=MibTableColumn
wepKeyLength=_WepKeyLength_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,3),_WepKeyLength_Type())
wepKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyLength.setStatus(_A)
class _WepKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WepKeyIndex_Type.__name__=_C
_WepKeyIndex_Object=MibTableColumn
wepKeyIndex=_WepKeyIndex_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,4),_WepKeyIndex_Type())
wepKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyIndex.setStatus(_A)
class _WepKeyPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_WepKeyPassphrase_Type.__name__=_I
_WepKeyPassphrase_Object=MibTableColumn
wepKeyPassphrase=_WepKeyPassphrase_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,5),_WepKeyPassphrase_Type())
wepKeyPassphrase.setMaxAccess(_L)
if mibBuilder.loadTexts:wepKeyPassphrase.setStatus(_A)
class _WepKeyFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascii',0),('hex',1)))
_WepKeyFormat_Type.__name__=_C
_WepKeyFormat_Object=MibTableColumn
wepKeyFormat=_WepKeyFormat_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,6),_WepKeyFormat_Type())
wepKeyFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyFormat.setStatus(_A)
class _EapMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('tls',0),('peap',1),('ttls',2),('leap',3)))
_EapMethod_Type.__name__=_C
_EapMethod_Object=MibTableColumn
eapMethod=_EapMethod_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,12),_EapMethod_Type())
eapMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:eapMethod.setStatus(_A)
class _TunneledAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('gtc',0),('md5',1),('pap',2),('chap',3),('mschap',4),('mschapv2',5),('tls',6),('eap-tls',7),('eap-mschapv2',8),('eap-gtc',9),('eap-md5',10)))
_TunneledAuth_Type.__name__=_C
_TunneledAuth_Object=MibTableColumn
tunneledAuth=_TunneledAuth_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,13),_TunneledAuth_Type())
tunneledAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:tunneledAuth.setStatus(_A)
class _WpaUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_WpaUsername_Type.__name__=_I
_WpaUsername_Object=MibTableColumn
wpaUsername=_WpaUsername_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,14),_WpaUsername_Type())
wpaUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:wpaUsername.setStatus(_A)
class _WpaAnonymousUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_WpaAnonymousUsername_Type.__name__=_I
_WpaAnonymousUsername_Object=MibTableColumn
wpaAnonymousUsername=_WpaAnonymousUsername_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,16),_WpaAnonymousUsername_Type())
wpaAnonymousUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:wpaAnonymousUsername.setStatus(_A)
class _VerifyServerCert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VerifyServerCert_Type.__name__=_C
_VerifyServerCert_Object=MibTableColumn
verifyServerCert=_VerifyServerCert_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,17),_VerifyServerCert_Type())
verifyServerCert.setMaxAccess(_B)
if mibBuilder.loadTexts:verifyServerCert.setStatus(_A)
class _TrustedServerCert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_TrustedServerCert_Type.__name__=_C
_TrustedServerCert_Object=MibTableColumn
trustedServerCert=_TrustedServerCert_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,18),_TrustedServerCert_Type())
trustedServerCert.setMaxAccess(_D)
if mibBuilder.loadTexts:trustedServerCert.setStatus(_A)
class _UserCert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_UserCert_Type.__name__=_C
_UserCert_Object=MibTableColumn
userCert=_UserCert_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,19),_UserCert_Type())
userCert.setMaxAccess(_D)
if mibBuilder.loadTexts:userCert.setStatus(_A)
class _UserPrivateKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_UserPrivateKey_Type.__name__=_C
_UserPrivateKey_Object=MibTableColumn
userPrivateKey=_UserPrivateKey_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,2,1,1,20),_UserPrivateKey_Type())
userPrivateKey.setMaxAccess(_D)
if mibBuilder.loadTexts:userPrivateKey.setStatus(_A)
class _FastRoamingSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FastRoamingSetting_Type.__name__=_C
_FastRoamingSetting_Object=MibScalar
fastRoamingSetting=_FastRoamingSetting_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,3),_FastRoamingSetting_Type())
fastRoamingSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingSetting.setStatus(_A)
class _FastRoamingScanChannels1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7),(_d,8),(_e,9),(_f,10),(_g,11),(_h,12),(_i,13),(_j,15),(_k,16),(_l,17),(_m,18),(_n,19),(_o,20),(_p,21),(_q,22),(_r,23),(_s,24),(_t,25),(_u,26),(_v,27),(_w,28),(_x,29),(_y,30),(_z,31),(_A0,32),(_A1,33),(_A2,34),(_A3,35),(_A4,36),(_A5,37),(_A6,38)))
_FastRoamingScanChannels1_Type.__name__=_C
_FastRoamingScanChannels1_Object=MibScalar
fastRoamingScanChannels1=_FastRoamingScanChannels1_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,4),_FastRoamingScanChannels1_Type())
fastRoamingScanChannels1.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingScanChannels1.setStatus(_A)
class _FastRoamingScanChannels2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7),(_d,8),(_e,9),(_f,10),(_g,11),(_h,12),(_i,13),(_j,15),(_k,16),(_l,17),(_m,18),(_n,19),(_o,20),(_p,21),(_q,22),(_r,23),(_s,24),(_t,25),(_u,26),(_v,27),(_w,28),(_x,29),(_y,30),(_z,31),(_A0,32),(_A1,33),(_A2,34),(_A3,35),(_A4,36),(_A5,37),(_A6,38)))
_FastRoamingScanChannels2_Type.__name__=_C
_FastRoamingScanChannels2_Object=MibScalar
fastRoamingScanChannels2=_FastRoamingScanChannels2_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,5),_FastRoamingScanChannels2_Type())
fastRoamingScanChannels2.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingScanChannels2.setStatus(_A)
class _FastRoamingScanChannels3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7),(_d,8),(_e,9),(_f,10),(_g,11),(_h,12),(_i,13),(_j,15),(_k,16),(_l,17),(_m,18),(_n,19),(_o,20),(_p,21),(_q,22),(_r,23),(_s,24),(_t,25),(_u,26),(_v,27),(_w,28),(_x,29),(_y,30),(_z,31),(_A0,32),(_A1,33),(_A2,34),(_A3,35),(_A4,36),(_A5,37),(_A6,38)))
_FastRoamingScanChannels3_Type.__name__=_C
_FastRoamingScanChannels3_Object=MibScalar
fastRoamingScanChannels3=_FastRoamingScanChannels3_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,6),_FastRoamingScanChannels3_Type())
fastRoamingScanChannels3.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingScanChannels3.setStatus(_A)
class _FastRoamingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-70,-40))
_FastRoamingThreshold_Type.__name__=_C
_FastRoamingThreshold_Object=MibScalar
fastRoamingThreshold=_FastRoamingThreshold_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,7),_FastRoamingThreshold_Type())
fastRoamingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingThreshold.setStatus(_A)
class _FastRoamingDifference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_FastRoamingDifference_Type.__name__=_C
_FastRoamingDifference_Object=MibScalar
fastRoamingDifference=_FastRoamingDifference_Object((1,3,6,1,4,1,8691,2,13,1,3,4,3,8),_FastRoamingDifference_Type())
fastRoamingDifference.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingDifference.setStatus(_A)
_WlanLogSetting_ObjectIdentity=ObjectIdentity
wlanLogSetting=_WlanLogSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,5))
class _WlanLogEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WlanLogEnable_Type.__name__=_C
_WlanLogEnable_Object=MibScalar
wlanLogEnable=_WlanLogEnable_Object((1,3,6,1,4,1,8691,2,13,1,3,5,1),_WlanLogEnable_Type())
wlanLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanLogEnable.setStatus(_A)
_AdvancedSetting_ObjectIdentity=ObjectIdentity
advancedSetting=_AdvancedSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,3,6))
class _GratuitousArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_GratuitousArp_Type.__name__=_C
_GratuitousArp_Object=MibScalar
gratuitousArp=_GratuitousArp_Object((1,3,6,1,4,1,8691,2,13,1,3,6,1),_GratuitousArp_Type())
gratuitousArp.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArp.setStatus(_A)
class _GratuitousArpSendPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_GratuitousArpSendPeriod_Type.__name__=_C
_GratuitousArpSendPeriod_Object=MibScalar
gratuitousArpSendPeriod=_GratuitousArpSendPeriod_Object((1,3,6,1,4,1,8691,2,13,1,3,6,2),_GratuitousArpSendPeriod_Type())
gratuitousArpSendPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpSendPeriod.setStatus(_A)
_GratuitousArpIpAddress1_Type=DisplayString
_GratuitousArpIpAddress1_Object=MibScalar
gratuitousArpIpAddress1=_GratuitousArpIpAddress1_Object((1,3,6,1,4,1,8691,2,13,1,3,6,3),_GratuitousArpIpAddress1_Type())
gratuitousArpIpAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress1.setStatus(_A)
_GratuitousArpMacAddress1_Type=DisplayString
_GratuitousArpMacAddress1_Object=MibScalar
gratuitousArpMacAddress1=_GratuitousArpMacAddress1_Object((1,3,6,1,4,1,8691,2,13,1,3,6,4),_GratuitousArpMacAddress1_Type())
gratuitousArpMacAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress1.setStatus(_A)
_GratuitousArpIpAddress2_Type=DisplayString
_GratuitousArpIpAddress2_Object=MibScalar
gratuitousArpIpAddress2=_GratuitousArpIpAddress2_Object((1,3,6,1,4,1,8691,2,13,1,3,6,5),_GratuitousArpIpAddress2_Type())
gratuitousArpIpAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress2.setStatus(_A)
_GratuitousArpMacAddress2_Type=DisplayString
_GratuitousArpMacAddress2_Object=MibScalar
gratuitousArpMacAddress2=_GratuitousArpMacAddress2_Object((1,3,6,1,4,1,8691,2,13,1,3,6,6),_GratuitousArpMacAddress2_Type())
gratuitousArpMacAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress2.setStatus(_A)
_GratuitousArpIpAddress3_Type=DisplayString
_GratuitousArpIpAddress3_Object=MibScalar
gratuitousArpIpAddress3=_GratuitousArpIpAddress3_Object((1,3,6,1,4,1,8691,2,13,1,3,6,7),_GratuitousArpIpAddress3_Type())
gratuitousArpIpAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress3.setStatus(_A)
_GratuitousArpMacAddress3_Type=DisplayString
_GratuitousArpMacAddress3_Object=MibScalar
gratuitousArpMacAddress3=_GratuitousArpMacAddress3_Object((1,3,6,1,4,1,8691,2,13,1,3,6,8),_GratuitousArpMacAddress3_Type())
gratuitousArpMacAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress3.setStatus(_A)
_GratuitousArpIpAddress4_Type=DisplayString
_GratuitousArpIpAddress4_Object=MibScalar
gratuitousArpIpAddress4=_GratuitousArpIpAddress4_Object((1,3,6,1,4,1,8691,2,13,1,3,6,9),_GratuitousArpIpAddress4_Type())
gratuitousArpIpAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress4.setStatus(_A)
_GratuitousArpMacAddress4_Type=DisplayString
_GratuitousArpMacAddress4_Object=MibScalar
gratuitousArpMacAddress4=_GratuitousArpMacAddress4_Object((1,3,6,1,4,1,8691,2,13,1,3,6,10),_GratuitousArpMacAddress4_Type())
gratuitousArpMacAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress4.setStatus(_A)
_PortSetting_ObjectIdentity=ObjectIdentity
portSetting=_PortSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4))
_OpModeSetting_ObjectIdentity=ObjectIdentity
opModeSetting=_OpModeSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1))
_OpMode_ObjectIdentity=ObjectIdentity
opMode=_OpMode_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,1))
_OpModePortTable_Object=MibTable
opModePortTable=_OpModePortTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,1,1))
if mibBuilder.loadTexts:opModePortTable.setStatus(_A)
_OpModePortEntry_Object=MibTableRow
opModePortEntry=_OpModePortEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,1,1,1))
opModePortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:opModePortEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PortIndex_Type.__name__=_C
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,8691,2,13,1,4,1,1,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,7,10,12,13,14,20,21)));namedValues=NamedValues(*(('pair-connection-slave',0),('pair-connection-master',1),('real-Com',2),(_E,7),('tcp-Server',10),('ethernet-modem',12),('tcp-Client',13),('udp',14),('rfc-2217',20),('reverse-Terminal',21)))
_PortMode_Type.__name__=_C
_PortMode_Object=MibTableColumn
portMode=_PortMode_Object((1,3,6,1,4,1,8691,2,13,1,4,1,1,1,1,2),_PortMode_Type())
portMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portMode.setStatus(_A)
_OpModeParam_ObjectIdentity=ObjectIdentity
opModeParam=_OpModeParam_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2))
_RealCOM_ObjectIdentity=ObjectIdentity
realCOM=_RealCOM_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,1))
_RealCOMTable_Object=MibTable
realCOMTable=_RealCOMTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1))
if mibBuilder.loadTexts:realCOMTable.setStatus(_A)
_RealCOMEntry_Object=MibTableRow
realCOMEntry=_RealCOMEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1))
realCOMEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:realCOMEntry.setStatus(_A)
_RealCOMTcpAliveCheck_Type=Integer32
_RealCOMTcpAliveCheck_Object=MibTableColumn
realCOMTcpAliveCheck=_RealCOMTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1,1),_RealCOMTcpAliveCheck_Type())
realCOMTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMTcpAliveCheck.setStatus(_A)
_RealCOMMaxConnection_Type=Integer32
_RealCOMMaxConnection_Object=MibTableColumn
realCOMMaxConnection=_RealCOMMaxConnection_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1,2),_RealCOMMaxConnection_Type())
realCOMMaxConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMMaxConnection.setStatus(_A)
class _RealCOMIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RealCOMIgnoreJammedIp_Type.__name__=_C
_RealCOMIgnoreJammedIp_Object=MibTableColumn
realCOMIgnoreJammedIp=_RealCOMIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1,3),_RealCOMIgnoreJammedIp_Type())
realCOMIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMIgnoreJammedIp.setStatus(_A)
class _RealCOMAllowDriverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RealCOMAllowDriverControl_Type.__name__=_C
_RealCOMAllowDriverControl_Object=MibTableColumn
realCOMAllowDriverControl=_RealCOMAllowDriverControl_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1,4),_RealCOMAllowDriverControl_Type())
realCOMAllowDriverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMAllowDriverControl.setStatus(_A)
class _RealCOMConnectionDownRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_RealCOMConnectionDownRTS_Type.__name__=_C
_RealCOMConnectionDownRTS_Object=MibTableColumn
realCOMConnectionDownRTS=_RealCOMConnectionDownRTS_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1,5),_RealCOMConnectionDownRTS_Type())
realCOMConnectionDownRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMConnectionDownRTS.setStatus(_A)
class _RealCOMConnectionDownDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_RealCOMConnectionDownDTR_Type.__name__=_C
_RealCOMConnectionDownDTR_Object=MibTableColumn
realCOMConnectionDownDTR=_RealCOMConnectionDownDTR_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,1,1,1,6),_RealCOMConnectionDownDTR_Type())
realCOMConnectionDownDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMConnectionDownDTR.setStatus(_A)
_Rfc2217_ObjectIdentity=ObjectIdentity
rfc2217=_Rfc2217_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,2))
_Rfc2217Table_Object=MibTable
rfc2217Table=_Rfc2217Table_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,2,1))
if mibBuilder.loadTexts:rfc2217Table.setStatus(_A)
_Rfc2217Entry_Object=MibTableRow
rfc2217Entry=_Rfc2217Entry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,2,1,1))
rfc2217Entry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rfc2217Entry.setStatus(_A)
_Rfc2217TcpAliveCheck_Type=Integer32
_Rfc2217TcpAliveCheck_Object=MibTableColumn
rfc2217TcpAliveCheck=_Rfc2217TcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,2,1,1,1),_Rfc2217TcpAliveCheck_Type())
rfc2217TcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:rfc2217TcpAliveCheck.setStatus(_A)
_Rfc2217TcpPort_Type=Integer32
_Rfc2217TcpPort_Object=MibTableColumn
rfc2217TcpPort=_Rfc2217TcpPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,2,1,1,2),_Rfc2217TcpPort_Type())
rfc2217TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rfc2217TcpPort.setStatus(_A)
_TcpServer_ObjectIdentity=ObjectIdentity
tcpServer=_TcpServer_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,3))
_TcpServerTable_Object=MibTable
tcpServerTable=_TcpServerTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1))
if mibBuilder.loadTexts:tcpServerTable.setStatus(_A)
_TcpServerEntry_Object=MibTableRow
tcpServerEntry=_TcpServerEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1))
tcpServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tcpServerEntry.setStatus(_A)
_TcpServerTcpAliveCheck_Type=Integer32
_TcpServerTcpAliveCheck_Object=MibTableColumn
tcpServerTcpAliveCheck=_TcpServerTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,1),_TcpServerTcpAliveCheck_Type())
tcpServerTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerTcpAliveCheck.setStatus(_A)
_TcpServerInactivityTime_Type=Integer32
_TcpServerInactivityTime_Object=MibTableColumn
tcpServerInactivityTime=_TcpServerInactivityTime_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,2),_TcpServerInactivityTime_Type())
tcpServerInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerInactivityTime.setStatus(_A)
_TcpServerMaxConnection_Type=Integer32
_TcpServerMaxConnection_Object=MibTableColumn
tcpServerMaxConnection=_TcpServerMaxConnection_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,3),_TcpServerMaxConnection_Type())
tcpServerMaxConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerMaxConnection.setStatus(_A)
class _TcpServerIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcpServerIgnoreJammedIp_Type.__name__=_C
_TcpServerIgnoreJammedIp_Object=MibTableColumn
tcpServerIgnoreJammedIp=_TcpServerIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,4),_TcpServerIgnoreJammedIp_Type())
tcpServerIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerIgnoreJammedIp.setStatus(_A)
class _TcpServerAllowDriverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcpServerAllowDriverControl_Type.__name__=_C
_TcpServerAllowDriverControl_Object=MibTableColumn
tcpServerAllowDriverControl=_TcpServerAllowDriverControl_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,5),_TcpServerAllowDriverControl_Type())
tcpServerAllowDriverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerAllowDriverControl.setStatus(_A)
_TcpServerTcpPort_Type=Integer32
_TcpServerTcpPort_Object=MibTableColumn
tcpServerTcpPort=_TcpServerTcpPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,6),_TcpServerTcpPort_Type())
tcpServerTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerTcpPort.setStatus(_A)
_TcpServerCmdPort_Type=Integer32
_TcpServerCmdPort_Object=MibTableColumn
tcpServerCmdPort=_TcpServerCmdPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,7),_TcpServerCmdPort_Type())
tcpServerCmdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerCmdPort.setStatus(_A)
class _TcpServerConnectionDownRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_TcpServerConnectionDownRTS_Type.__name__=_C
_TcpServerConnectionDownRTS_Object=MibTableColumn
tcpServerConnectionDownRTS=_TcpServerConnectionDownRTS_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,8),_TcpServerConnectionDownRTS_Type())
tcpServerConnectionDownRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerConnectionDownRTS.setStatus(_A)
class _TcpServerConnectionDownDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_TcpServerConnectionDownDTR_Type.__name__=_C
_TcpServerConnectionDownDTR_Object=MibTableColumn
tcpServerConnectionDownDTR=_TcpServerConnectionDownDTR_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,3,1,1,9),_TcpServerConnectionDownDTR_Type())
tcpServerConnectionDownDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerConnectionDownDTR.setStatus(_A)
_TcpClient_ObjectIdentity=ObjectIdentity
tcpClient=_TcpClient_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,4))
_TcpClientTable_Object=MibTable
tcpClientTable=_TcpClientTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1))
if mibBuilder.loadTexts:tcpClientTable.setStatus(_A)
_TcpClientEntry_Object=MibTableRow
tcpClientEntry=_TcpClientEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1))
tcpClientEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tcpClientEntry.setStatus(_A)
_TcpClientTcpAliveCheck_Type=Integer32
_TcpClientTcpAliveCheck_Object=MibTableColumn
tcpClientTcpAliveCheck=_TcpClientTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,1),_TcpClientTcpAliveCheck_Type())
tcpClientTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientTcpAliveCheck.setStatus(_A)
_TcpClientInactivityTime_Type=Integer32
_TcpClientInactivityTime_Object=MibTableColumn
tcpClientInactivityTime=_TcpClientInactivityTime_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,2),_TcpClientInactivityTime_Type())
tcpClientInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientInactivityTime.setStatus(_A)
class _TcpClientIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcpClientIgnoreJammedIp_Type.__name__=_C
_TcpClientIgnoreJammedIp_Object=MibTableColumn
tcpClientIgnoreJammedIp=_TcpClientIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,3),_TcpClientIgnoreJammedIp_Type())
tcpClientIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientIgnoreJammedIp.setStatus(_A)
_TcpClientDestinationAddress1_Type=DisplayString
_TcpClientDestinationAddress1_Object=MibTableColumn
tcpClientDestinationAddress1=_TcpClientDestinationAddress1_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,4),_TcpClientDestinationAddress1_Type())
tcpClientDestinationAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress1.setStatus(_A)
_TcpClientDestinationPort1_Type=Integer32
_TcpClientDestinationPort1_Object=MibTableColumn
tcpClientDestinationPort1=_TcpClientDestinationPort1_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,5),_TcpClientDestinationPort1_Type())
tcpClientDestinationPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort1.setStatus(_A)
_TcpClientDestinationAddress2_Type=DisplayString
_TcpClientDestinationAddress2_Object=MibTableColumn
tcpClientDestinationAddress2=_TcpClientDestinationAddress2_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,6),_TcpClientDestinationAddress2_Type())
tcpClientDestinationAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress2.setStatus(_A)
_TcpClientDestinationPort2_Type=Integer32
_TcpClientDestinationPort2_Object=MibTableColumn
tcpClientDestinationPort2=_TcpClientDestinationPort2_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,7),_TcpClientDestinationPort2_Type())
tcpClientDestinationPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort2.setStatus(_A)
_TcpClientDestinationAddress3_Type=DisplayString
_TcpClientDestinationAddress3_Object=MibTableColumn
tcpClientDestinationAddress3=_TcpClientDestinationAddress3_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,8),_TcpClientDestinationAddress3_Type())
tcpClientDestinationAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress3.setStatus(_A)
_TcpClientDestinationPort3_Type=Integer32
_TcpClientDestinationPort3_Object=MibTableColumn
tcpClientDestinationPort3=_TcpClientDestinationPort3_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,9),_TcpClientDestinationPort3_Type())
tcpClientDestinationPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort3.setStatus(_A)
_TcpClientDestinationAddress4_Type=DisplayString
_TcpClientDestinationAddress4_Object=MibTableColumn
tcpClientDestinationAddress4=_TcpClientDestinationAddress4_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,10),_TcpClientDestinationAddress4_Type())
tcpClientDestinationAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress4.setStatus(_A)
_TcpClientDestinationPort4_Type=Integer32
_TcpClientDestinationPort4_Object=MibTableColumn
tcpClientDestinationPort4=_TcpClientDestinationPort4_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,11),_TcpClientDestinationPort4_Type())
tcpClientDestinationPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort4.setStatus(_A)
_TcpClientDesignatedLocalPort1_Type=Integer32
_TcpClientDesignatedLocalPort1_Object=MibTableColumn
tcpClientDesignatedLocalPort1=_TcpClientDesignatedLocalPort1_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,12),_TcpClientDesignatedLocalPort1_Type())
tcpClientDesignatedLocalPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort1.setStatus(_A)
_TcpClientDesignatedLocalPort2_Type=Integer32
_TcpClientDesignatedLocalPort2_Object=MibTableColumn
tcpClientDesignatedLocalPort2=_TcpClientDesignatedLocalPort2_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,13),_TcpClientDesignatedLocalPort2_Type())
tcpClientDesignatedLocalPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort2.setStatus(_A)
_TcpClientDesignatedLocalPort3_Type=Integer32
_TcpClientDesignatedLocalPort3_Object=MibTableColumn
tcpClientDesignatedLocalPort3=_TcpClientDesignatedLocalPort3_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,14),_TcpClientDesignatedLocalPort3_Type())
tcpClientDesignatedLocalPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort3.setStatus(_A)
_TcpClientDesignatedLocalPort4_Type=Integer32
_TcpClientDesignatedLocalPort4_Object=MibTableColumn
tcpClientDesignatedLocalPort4=_TcpClientDesignatedLocalPort4_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,15),_TcpClientDesignatedLocalPort4_Type())
tcpClientDesignatedLocalPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort4.setStatus(_A)
class _TcpClientConnectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(257,258,260,264,514,1028,2056)));namedValues=NamedValues(*(('startup-None',257),('anyCharacter-None',258),('dsrOn-None',260),('dcdOn-None',264),('anyCharacter-InactivityTime',514),('dsrOn-DSR-Off',1028),('dcdOn-DCD-Off',2056)))
_TcpClientConnectionControl_Type.__name__=_C
_TcpClientConnectionControl_Object=MibTableColumn
tcpClientConnectionControl=_TcpClientConnectionControl_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,4,1,1,16),_TcpClientConnectionControl_Type())
tcpClientConnectionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientConnectionControl.setStatus(_A)
_Udp_ObjectIdentity=ObjectIdentity
udp=_Udp_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,5))
_UdpTable_Object=MibTable
udpTable=_UdpTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1))
if mibBuilder.loadTexts:udpTable.setStatus(_A)
_UdpEntry_Object=MibTableRow
udpEntry=_UdpEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1))
udpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:udpEntry.setStatus(_A)
_UdpDestinationAddress1Begin_Type=IpAddress
_UdpDestinationAddress1Begin_Object=MibTableColumn
udpDestinationAddress1Begin=_UdpDestinationAddress1Begin_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,1),_UdpDestinationAddress1Begin_Type())
udpDestinationAddress1Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress1Begin.setStatus(_A)
_UdpDestinationAddress1End_Type=IpAddress
_UdpDestinationAddress1End_Object=MibTableColumn
udpDestinationAddress1End=_UdpDestinationAddress1End_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,2),_UdpDestinationAddress1End_Type())
udpDestinationAddress1End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress1End.setStatus(_A)
_UdpDestinationPort1_Type=Integer32
_UdpDestinationPort1_Object=MibTableColumn
udpDestinationPort1=_UdpDestinationPort1_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,3),_UdpDestinationPort1_Type())
udpDestinationPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort1.setStatus(_A)
_UdpDestinationAddress2Begin_Type=IpAddress
_UdpDestinationAddress2Begin_Object=MibTableColumn
udpDestinationAddress2Begin=_UdpDestinationAddress2Begin_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,4),_UdpDestinationAddress2Begin_Type())
udpDestinationAddress2Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress2Begin.setStatus(_A)
_UdpDestinationAddress2End_Type=IpAddress
_UdpDestinationAddress2End_Object=MibTableColumn
udpDestinationAddress2End=_UdpDestinationAddress2End_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,5),_UdpDestinationAddress2End_Type())
udpDestinationAddress2End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress2End.setStatus(_A)
_UdpDestinationPort2_Type=Integer32
_UdpDestinationPort2_Object=MibTableColumn
udpDestinationPort2=_UdpDestinationPort2_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,6),_UdpDestinationPort2_Type())
udpDestinationPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort2.setStatus(_A)
_UdpDestinationAddress3Begin_Type=IpAddress
_UdpDestinationAddress3Begin_Object=MibTableColumn
udpDestinationAddress3Begin=_UdpDestinationAddress3Begin_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,7),_UdpDestinationAddress3Begin_Type())
udpDestinationAddress3Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress3Begin.setStatus(_A)
_UdpDestinationAddress3End_Type=IpAddress
_UdpDestinationAddress3End_Object=MibTableColumn
udpDestinationAddress3End=_UdpDestinationAddress3End_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,8),_UdpDestinationAddress3End_Type())
udpDestinationAddress3End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress3End.setStatus(_A)
_UdpDestinationPort3_Type=Integer32
_UdpDestinationPort3_Object=MibTableColumn
udpDestinationPort3=_UdpDestinationPort3_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,9),_UdpDestinationPort3_Type())
udpDestinationPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort3.setStatus(_A)
_UdpDestinationAddress4Begin_Type=IpAddress
_UdpDestinationAddress4Begin_Object=MibTableColumn
udpDestinationAddress4Begin=_UdpDestinationAddress4Begin_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,10),_UdpDestinationAddress4Begin_Type())
udpDestinationAddress4Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress4Begin.setStatus(_A)
_UdpDestinationAddress4End_Type=IpAddress
_UdpDestinationAddress4End_Object=MibTableColumn
udpDestinationAddress4End=_UdpDestinationAddress4End_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,11),_UdpDestinationAddress4End_Type())
udpDestinationAddress4End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress4End.setStatus(_A)
_UdpDestinationPort4_Type=Integer32
_UdpDestinationPort4_Object=MibTableColumn
udpDestinationPort4=_UdpDestinationPort4_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,12),_UdpDestinationPort4_Type())
udpDestinationPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort4.setStatus(_A)
_UdpLocalListenPort_Type=Integer32
_UdpLocalListenPort_Object=MibTableColumn
udpLocalListenPort=_UdpLocalListenPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,5,1,1,13),_UdpLocalListenPort_Type())
udpLocalListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:udpLocalListenPort.setStatus(_A)
_PairConnectionMaster_ObjectIdentity=ObjectIdentity
pairConnectionMaster=_PairConnectionMaster_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,6))
_PairConnectionMasterTable_Object=MibTable
pairConnectionMasterTable=_PairConnectionMasterTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,6,1))
if mibBuilder.loadTexts:pairConnectionMasterTable.setStatus(_A)
_PairConnectionMasterEntry_Object=MibTableRow
pairConnectionMasterEntry=_PairConnectionMasterEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,6,1,1))
pairConnectionMasterEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pairConnectionMasterEntry.setStatus(_A)
_PairConnectionMasterTcpAliveCheck_Type=Integer32
_PairConnectionMasterTcpAliveCheck_Object=MibTableColumn
pairConnectionMasterTcpAliveCheck=_PairConnectionMasterTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,6,1,1,1),_PairConnectionMasterTcpAliveCheck_Type())
pairConnectionMasterTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionMasterTcpAliveCheck.setStatus(_A)
_PairConnectionMasterDestnationAddress_Type=DisplayString
_PairConnectionMasterDestnationAddress_Object=MibTableColumn
pairConnectionMasterDestnationAddress=_PairConnectionMasterDestnationAddress_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,6,1,1,2),_PairConnectionMasterDestnationAddress_Type())
pairConnectionMasterDestnationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionMasterDestnationAddress.setStatus(_A)
_PairConnectionMasterDestnationTcpPort_Type=Integer32
_PairConnectionMasterDestnationTcpPort_Object=MibTableColumn
pairConnectionMasterDestnationTcpPort=_PairConnectionMasterDestnationTcpPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,6,1,1,3),_PairConnectionMasterDestnationTcpPort_Type())
pairConnectionMasterDestnationTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionMasterDestnationTcpPort.setStatus(_A)
_PairConnectionSlave_ObjectIdentity=ObjectIdentity
pairConnectionSlave=_PairConnectionSlave_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,7))
_PairConnectionSlaveTable_Object=MibTable
pairConnectionSlaveTable=_PairConnectionSlaveTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,7,1))
if mibBuilder.loadTexts:pairConnectionSlaveTable.setStatus(_A)
_PairConnectionSlaveEntry_Object=MibTableRow
pairConnectionSlaveEntry=_PairConnectionSlaveEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,7,1,1))
pairConnectionSlaveEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pairConnectionSlaveEntry.setStatus(_A)
_PairConnectionSlaveTcpAliveCheck_Type=Integer32
_PairConnectionSlaveTcpAliveCheck_Object=MibTableColumn
pairConnectionSlaveTcpAliveCheck=_PairConnectionSlaveTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,7,1,1,1),_PairConnectionSlaveTcpAliveCheck_Type())
pairConnectionSlaveTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionSlaveTcpAliveCheck.setStatus(_A)
_PairConnectionSlaveLocalTcpPort_Type=Integer32
_PairConnectionSlaveLocalTcpPort_Object=MibTableColumn
pairConnectionSlaveLocalTcpPort=_PairConnectionSlaveLocalTcpPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,7,1,1,2),_PairConnectionSlaveLocalTcpPort_Type())
pairConnectionSlaveLocalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionSlaveLocalTcpPort.setStatus(_A)
_EthernetModem_ObjectIdentity=ObjectIdentity
ethernetModem=_EthernetModem_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,8))
_EthernetModemTable_Object=MibTable
ethernetModemTable=_EthernetModemTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,8,1))
if mibBuilder.loadTexts:ethernetModemTable.setStatus(_A)
_EthernetModemEntry_Object=MibTableRow
ethernetModemEntry=_EthernetModemEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,8,1,1))
ethernetModemEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ethernetModemEntry.setStatus(_A)
_EthernetModemTcpAliveCheck_Type=Integer32
_EthernetModemTcpAliveCheck_Object=MibTableColumn
ethernetModemTcpAliveCheck=_EthernetModemTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,8,1,1,1),_EthernetModemTcpAliveCheck_Type())
ethernetModemTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetModemTcpAliveCheck.setStatus(_A)
_EthernetModemLocalTcpPort_Type=Integer32
_EthernetModemLocalTcpPort_Object=MibTableColumn
ethernetModemLocalTcpPort=_EthernetModemLocalTcpPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,8,1,1,2),_EthernetModemLocalTcpPort_Type())
ethernetModemLocalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetModemLocalTcpPort.setStatus(_A)
_ReverseTerminal_ObjectIdentity=ObjectIdentity
reverseTerminal=_ReverseTerminal_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,2,9))
_ReverseTerminalTable_Object=MibTable
reverseTerminalTable=_ReverseTerminalTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1))
if mibBuilder.loadTexts:reverseTerminalTable.setStatus(_A)
_ReverseTerminalEntry_Object=MibTableRow
reverseTerminalEntry=_ReverseTerminalEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1,1))
reverseTerminalEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:reverseTerminalEntry.setStatus(_A)
_ReverseTerminalTcpAliveCheck_Type=Integer32
_ReverseTerminalTcpAliveCheck_Object=MibTableColumn
reverseTerminalTcpAliveCheck=_ReverseTerminalTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1,1,1),_ReverseTerminalTcpAliveCheck_Type())
reverseTerminalTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTcpAliveCheck.setStatus(_A)
_ReverseTerminalInactivityTime_Type=Integer32
_ReverseTerminalInactivityTime_Object=MibTableColumn
reverseTerminalInactivityTime=_ReverseTerminalInactivityTime_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1,1,2),_ReverseTerminalInactivityTime_Type())
reverseTerminalInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalInactivityTime.setStatus(_A)
_ReverseTerminalTcpPort_Type=Integer32
_ReverseTerminalTcpPort_Object=MibTableColumn
reverseTerminalTcpPort=_ReverseTerminalTcpPort_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1,1,3),_ReverseTerminalTcpPort_Type())
reverseTerminalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTcpPort.setStatus(_A)
class _ReverseTerminalAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('local',1),('radius',2)))
_ReverseTerminalAuthenticationType_Type.__name__=_C
_ReverseTerminalAuthenticationType_Object=MibTableColumn
reverseTerminalAuthenticationType=_ReverseTerminalAuthenticationType_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1,1,4),_ReverseTerminalAuthenticationType_Type())
reverseTerminalAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalAuthenticationType.setStatus(_A)
class _ReverseTerminalMapKeys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('cr-lf',0),('cr',1),('lf',2)))
_ReverseTerminalMapKeys_Type.__name__=_C
_ReverseTerminalMapKeys_Object=MibTableColumn
reverseTerminalMapKeys=_ReverseTerminalMapKeys_Object((1,3,6,1,4,1,8691,2,13,1,4,1,2,9,1,1,5),_ReverseTerminalMapKeys_Type())
reverseTerminalMapKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalMapKeys.setStatus(_A)
_DataPacking_ObjectIdentity=ObjectIdentity
dataPacking=_DataPacking_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,1,3))
_DataPackingPortTable_Object=MibTable
dataPackingPortTable=_DataPackingPortTable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1))
if mibBuilder.loadTexts:dataPackingPortTable.setStatus(_A)
_DataPackingPortEntry_Object=MibTableRow
dataPackingPortEntry=_DataPackingPortEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1))
dataPackingPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dataPackingPortEntry.setStatus(_A)
_PortPacketLength_Type=Integer32
_PortPacketLength_Object=MibTableColumn
portPacketLength=_PortPacketLength_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,1),_PortPacketLength_Type())
portPacketLength.setMaxAccess(_B)
if mibBuilder.loadTexts:portPacketLength.setStatus(_A)
class _PortDelimiter1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortDelimiter1Enable_Type.__name__=_C
_PortDelimiter1Enable_Object=MibTableColumn
portDelimiter1Enable=_PortDelimiter1Enable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,2),_PortDelimiter1Enable_Type())
portDelimiter1Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter1Enable.setStatus(_A)
class _PortDelimiter1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_PortDelimiter1_Type.__name__=_I
_PortDelimiter1_Object=MibTableColumn
portDelimiter1=_PortDelimiter1_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,3),_PortDelimiter1_Type())
portDelimiter1.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter1.setStatus(_A)
class _PortDelimiter2Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortDelimiter2Enable_Type.__name__=_C
_PortDelimiter2Enable_Object=MibTableColumn
portDelimiter2Enable=_PortDelimiter2Enable_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,4),_PortDelimiter2Enable_Type())
portDelimiter2Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter2Enable.setStatus(_A)
class _PortDelimiter2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_PortDelimiter2_Type.__name__=_I
_PortDelimiter2_Object=MibTableColumn
portDelimiter2=_PortDelimiter2_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,5),_PortDelimiter2_Type())
portDelimiter2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter2.setStatus(_A)
class _PortDelimiterProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*(('doNothing',1),('delimiterAddOne',2),('delimiterAddTwo',4),('stripDelimiter',8)))
_PortDelimiterProcess_Type.__name__=_C
_PortDelimiterProcess_Object=MibTableColumn
portDelimiterProcess=_PortDelimiterProcess_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,6),_PortDelimiterProcess_Type())
portDelimiterProcess.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiterProcess.setStatus(_A)
_PortForceTransmit_Type=Integer32
_PortForceTransmit_Object=MibTableColumn
portForceTransmit=_PortForceTransmit_Object((1,3,6,1,4,1,8691,2,13,1,4,1,3,1,1,7),_PortForceTransmit_Type())
portForceTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:portForceTransmit.setStatus(_A)
_ComParamSetting_ObjectIdentity=ObjectIdentity
comParamSetting=_ComParamSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,2))
_ComParamPortTable_Object=MibTable
comParamPortTable=_ComParamPortTable_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1))
if mibBuilder.loadTexts:comParamPortTable.setStatus(_A)
_ComParamPortEntry_Object=MibTableRow
comParamPortEntry=_ComParamPortEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1))
comParamPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:comParamPortEntry.setStatus(_A)
class _PortAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortAlias_Type.__name__=_I
_PortAlias_Object=MibTableColumn
portAlias=_PortAlias_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,1),_PortAlias_Type())
portAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:portAlias.setStatus(_A)
class _PortInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rs-232',0),('rs-422',1),('rs-485-2wire',2),('rs-485-4wire',3)))
_PortInterface_Type.__name__=_C
_PortInterface_Object=MibTableColumn
portInterface=_PortInterface_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,2),_PortInterface_Type())
portInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:portInterface.setStatus(_A)
class _PortBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('b50',0),('b75',1),('b110',2),('b134',3),('b150',4),('b300',5),('b600',6),('b1200',7),('b1800',8),('b2400',9),('b4800',10),('b9600',12),('b19200',13),('b38400',14),('b57600',15),('b115200',16),('b230400',17),('b460800',18),('b921600',19)))
_PortBaudRate_Type.__name__=_C
_PortBaudRate_Object=MibTableColumn
portBaudRate=_PortBaudRate_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,3),_PortBaudRate_Type())
portBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:portBaudRate.setStatus(_A)
class _PortDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('bits-5',0),('bits-6',1),('bits-7',2),('bits-8',3)))
_PortDataBits_Type.__name__=_C
_PortDataBits_Object=MibTableColumn
portDataBits=_PortDataBits_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,4),_PortDataBits_Type())
portDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:portDataBits.setStatus(_A)
class _PortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('bits-1',0),('bits-1dot5',1),('bits-2',2)))
_PortStopBits_Type.__name__=_C
_PortStopBits_Object=MibTableColumn
portStopBits=_PortStopBits_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,5),_PortStopBits_Type())
portStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:portStopBits.setStatus(_A)
class _PortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,5,7)));namedValues=NamedValues(*((_O,0),('odd',1),('even',3),('mark',5),('space',7)))
_PortParity_Type.__name__=_C
_PortParity_Object=MibTableColumn
portParity=_PortParity_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,6),_PortParity_Type())
portParity.setMaxAccess(_B)
if mibBuilder.loadTexts:portParity.setStatus(_A)
class _PortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('rts-cts',1),('xon-xoff',2)))
_PortFlowControl_Type.__name__=_C
_PortFlowControl_Object=MibTableColumn
portFlowControl=_PortFlowControl_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,7),_PortFlowControl_Type())
portFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowControl.setStatus(_A)
class _PortFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortFIFO_Type.__name__=_C
_PortFIFO_Object=MibTableColumn
portFIFO=_PortFIFO_Object((1,3,6,1,4,1,8691,2,13,1,4,2,1,1,8),_PortFIFO_Type())
portFIFO.setMaxAccess(_B)
if mibBuilder.loadTexts:portFIFO.setStatus(_A)
_DataBuffering_ObjectIdentity=ObjectIdentity
dataBuffering=_DataBuffering_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,4,3))
_DataBufferingPortTable_Object=MibTable
dataBufferingPortTable=_DataBufferingPortTable_Object((1,3,6,1,4,1,8691,2,13,1,4,3,1))
if mibBuilder.loadTexts:dataBufferingPortTable.setStatus(_A)
_DataBufferingPortEntry_Object=MibTableRow
dataBufferingPortEntry=_DataBufferingPortEntry_Object((1,3,6,1,4,1,8691,2,13,1,4,3,1,1))
dataBufferingPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dataBufferingPortEntry.setStatus(_A)
class _PortBufferingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortBufferingEnable_Type.__name__=_C
_PortBufferingEnable_Object=MibTableColumn
portBufferingEnable=_PortBufferingEnable_Object((1,3,6,1,4,1,8691,2,13,1,4,3,1,1,1),_PortBufferingEnable_Type())
portBufferingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portBufferingEnable.setStatus(_A)
class _PortSerialDataLoggingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortSerialDataLoggingEnable_Type.__name__=_C
_PortSerialDataLoggingEnable_Object=MibTableColumn
portSerialDataLoggingEnable=_PortSerialDataLoggingEnable_Object((1,3,6,1,4,1,8691,2,13,1,4,3,1,1,2),_PortSerialDataLoggingEnable_Type())
portSerialDataLoggingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portSerialDataLoggingEnable.setStatus(_A)
_SysManagement_ObjectIdentity=ObjectIdentity
sysManagement=_SysManagement_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5))
_MiscNetworkSettings_ObjectIdentity=ObjectIdentity
miscNetworkSettings=_MiscNetworkSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,1))
_AccessibleIp_ObjectIdentity=ObjectIdentity
accessibleIp=_AccessibleIp_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,1,1))
class _EnableAccessibleIpList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableAccessibleIpList_Type.__name__=_C
_EnableAccessibleIpList_Object=MibScalar
enableAccessibleIpList=_EnableAccessibleIpList_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,1),_EnableAccessibleIpList_Type())
enableAccessibleIpList.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAccessibleIpList.setStatus(_A)
_AccessibleIpListTable_Object=MibTable
accessibleIpListTable=_AccessibleIpListTable_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,2))
if mibBuilder.loadTexts:accessibleIpListTable.setStatus(_A)
_AccessibleIpListEntry_Object=MibTableRow
accessibleIpListEntry=_AccessibleIpListEntry_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,2,1))
accessibleIpListEntry.setIndexNames((0,_G,_AB))
if mibBuilder.loadTexts:accessibleIpListEntry.setStatus(_A)
class _AccessibleIpListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AccessibleIpListIndex_Type.__name__=_C
_AccessibleIpListIndex_Object=MibTableColumn
accessibleIpListIndex=_AccessibleIpListIndex_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,2,1,1),_AccessibleIpListIndex_Type())
accessibleIpListIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:accessibleIpListIndex.setStatus(_A)
class _ActiveAccessibleIpList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ActiveAccessibleIpList_Type.__name__=_C
_ActiveAccessibleIpList_Object=MibTableColumn
activeAccessibleIpList=_ActiveAccessibleIpList_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,2,1,2),_ActiveAccessibleIpList_Type())
activeAccessibleIpList.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAccessibleIpList.setStatus(_A)
_AccessibleIpListAddress_Type=IpAddress
_AccessibleIpListAddress_Object=MibTableColumn
accessibleIpListAddress=_AccessibleIpListAddress_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,2,1,3),_AccessibleIpListAddress_Type())
accessibleIpListAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:accessibleIpListAddress.setStatus(_A)
_AccessibleIpListNetmask_Type=IpAddress
_AccessibleIpListNetmask_Object=MibTableColumn
accessibleIpListNetmask=_AccessibleIpListNetmask_Object((1,3,6,1,4,1,8691,2,13,1,5,1,1,2,1,4),_AccessibleIpListNetmask_Type())
accessibleIpListNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:accessibleIpListNetmask.setStatus(_A)
_SnmpAgentSettings_ObjectIdentity=ObjectIdentity
snmpAgentSettings=_SnmpAgentSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,1,2))
class _SnmpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnmpEnable_Type.__name__=_C
_SnmpEnable_Object=MibScalar
snmpEnable=_SnmpEnable_Object((1,3,6,1,4,1,8691,2,13,1,5,1,2,1),_SnmpEnable_Type())
snmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEnable.setStatus(_A)
class _SnmpContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SnmpContactName_Type.__name__=_I
_SnmpContactName_Object=MibScalar
snmpContactName=_SnmpContactName_Object((1,3,6,1,4,1,8691,2,13,1,5,1,2,2),_SnmpContactName_Type())
snmpContactName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpContactName.setStatus(_A)
class _SnmpLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SnmpLocation_Type.__name__=_I
_SnmpLocation_Object=MibScalar
snmpLocation=_SnmpLocation_Object((1,3,6,1,4,1,8691,2,13,1,5,1,2,3),_SnmpLocation_Type())
snmpLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpLocation.setStatus(_A)
_AuthenticationServer_ObjectIdentity=ObjectIdentity
authenticationServer=_AuthenticationServer_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,1,4))
class _RadiusServerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RadiusServerIp_Type.__name__=_I
_RadiusServerIp_Object=MibScalar
radiusServerIp=_RadiusServerIp_Object((1,3,6,1,4,1,8691,2,13,1,5,1,4,1),_RadiusServerIp_Type())
radiusServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServerIp.setStatus(_A)
class _UdpPortAuthenticationServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1645,1812)));namedValues=NamedValues(*(('port1645',1645),('port1812',1812)))
_UdpPortAuthenticationServer_Type.__name__=_C
_UdpPortAuthenticationServer_Object=MibScalar
udpPortAuthenticationServer=_UdpPortAuthenticationServer_Object((1,3,6,1,4,1,8691,2,13,1,5,1,4,3),_UdpPortAuthenticationServer_Type())
udpPortAuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:udpPortAuthenticationServer.setStatus(_A)
class _RadiusAccounting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RadiusAccounting_Type.__name__=_C
_RadiusAccounting_Object=MibScalar
radiusAccounting=_RadiusAccounting_Object((1,3,6,1,4,1,8691,2,13,1,5,1,4,4),_RadiusAccounting_Type())
radiusAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccounting.setStatus(_A)
_SysLogSettings_ObjectIdentity=ObjectIdentity
sysLogSettings=_SysLogSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,1,5))
class _SysLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SysLocalLog_Type.__name__=_C
_SysLocalLog_Object=MibScalar
sysLocalLog=_SysLocalLog_Object((1,3,6,1,4,1,8691,2,13,1,5,1,5,1),_SysLocalLog_Type())
sysLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:sysLocalLog.setStatus(_A)
class _NetworkLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NetworkLocalLog_Type.__name__=_C
_NetworkLocalLog_Object=MibScalar
networkLocalLog=_NetworkLocalLog_Object((1,3,6,1,4,1,8691,2,13,1,5,1,5,2),_NetworkLocalLog_Type())
networkLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:networkLocalLog.setStatus(_A)
class _ConfigLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigLocalLog_Type.__name__=_C
_ConfigLocalLog_Object=MibScalar
configLocalLog=_ConfigLocalLog_Object((1,3,6,1,4,1,8691,2,13,1,5,1,5,3),_ConfigLocalLog_Type())
configLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalLog.setStatus(_A)
class _OpModeLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_OpModeLocalLog_Type.__name__=_C
_OpModeLocalLog_Object=MibScalar
opModeLocalLog=_OpModeLocalLog_Object((1,3,6,1,4,1,8691,2,13,1,5,1,5,4),_OpModeLocalLog_Type())
opModeLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:opModeLocalLog.setStatus(_A)
_AutoWarningSettings_ObjectIdentity=ObjectIdentity
autoWarningSettings=_AutoWarningSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,2))
_EventSettings_ObjectIdentity=ObjectIdentity
eventSettings=_EventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,2,1))
class _MailWarningColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningColdStart_Type.__name__=_C
_MailWarningColdStart_Object=MibScalar
mailWarningColdStart=_MailWarningColdStart_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,1),_MailWarningColdStart_Type())
mailWarningColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningColdStart.setStatus(_A)
class _MailWarningWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningWarmStart_Type.__name__=_C
_MailWarningWarmStart_Object=MibScalar
mailWarningWarmStart=_MailWarningWarmStart_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,2),_MailWarningWarmStart_Type())
mailWarningWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningWarmStart.setStatus(_A)
class _MailWarningAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningAuthFailure_Type.__name__=_C
_MailWarningAuthFailure_Object=MibScalar
mailWarningAuthFailure=_MailWarningAuthFailure_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,3),_MailWarningAuthFailure_Type())
mailWarningAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningAuthFailure.setStatus(_A)
class _MailWarningIpChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningIpChanged_Type.__name__=_C
_MailWarningIpChanged_Object=MibScalar
mailWarningIpChanged=_MailWarningIpChanged_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,4),_MailWarningIpChanged_Type())
mailWarningIpChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningIpChanged.setStatus(_A)
class _MailWarningPasswordChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningPasswordChanged_Type.__name__=_C
_MailWarningPasswordChanged_Object=MibScalar
mailWarningPasswordChanged=_MailWarningPasswordChanged_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,5),_MailWarningPasswordChanged_Type())
mailWarningPasswordChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningPasswordChanged.setStatus(_A)
class _TrapServerColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapServerColdStart_Type.__name__=_C
_TrapServerColdStart_Object=MibScalar
trapServerColdStart=_TrapServerColdStart_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,6),_TrapServerColdStart_Type())
trapServerColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerColdStart.setStatus(_A)
class _TrapServerWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapServerWarmStart_Type.__name__=_C
_TrapServerWarmStart_Object=MibScalar
trapServerWarmStart=_TrapServerWarmStart_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,7),_TrapServerWarmStart_Type())
trapServerWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerWarmStart.setStatus(_A)
class _TrapServerAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapServerAuthFailure_Type.__name__=_C
_TrapServerAuthFailure_Object=MibScalar
trapServerAuthFailure=_TrapServerAuthFailure_Object((1,3,6,1,4,1,8691,2,13,1,5,2,1,8),_TrapServerAuthFailure_Type())
trapServerAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerAuthFailure.setStatus(_A)
_SerialEventSettings_ObjectIdentity=ObjectIdentity
serialEventSettings=_SerialEventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,2,2))
_PortEventSettingsTable_Object=MibTable
portEventSettingsTable=_PortEventSettingsTable_Object((1,3,6,1,4,1,8691,2,13,1,5,2,2,1))
if mibBuilder.loadTexts:portEventSettingsTable.setStatus(_A)
_PortEventSettingsEntry_Object=MibTableRow
portEventSettingsEntry=_PortEventSettingsEntry_Object((1,3,6,1,4,1,8691,2,13,1,5,2,2,1,1))
portEventSettingsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:portEventSettingsEntry.setStatus(_A)
class _MailDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailDCDchange_Type.__name__=_C
_MailDCDchange_Object=MibTableColumn
mailDCDchange=_MailDCDchange_Object((1,3,6,1,4,1,8691,2,13,1,5,2,2,1,1,1),_MailDCDchange_Type())
mailDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:mailDCDchange.setStatus(_A)
class _TrapDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapDCDchange_Type.__name__=_C
_TrapDCDchange_Object=MibTableColumn
trapDCDchange=_TrapDCDchange_Object((1,3,6,1,4,1,8691,2,13,1,5,2,2,1,1,2),_TrapDCDchange_Type())
trapDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDCDchange.setStatus(_A)
class _MailDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailDSRchange_Type.__name__=_C
_MailDSRchange_Object=MibTableColumn
mailDSRchange=_MailDSRchange_Object((1,3,6,1,4,1,8691,2,13,1,5,2,2,1,1,3),_MailDSRchange_Type())
mailDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:mailDSRchange.setStatus(_A)
class _TrapDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapDSRchange_Type.__name__=_C
_TrapDSRchange_Object=MibTableColumn
trapDSRchange=_TrapDSRchange_Object((1,3,6,1,4,1,8691,2,13,1,5,2,2,1,1,4),_TrapDSRchange_Type())
trapDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDSRchange.setStatus(_A)
_EmailAlert_ObjectIdentity=ObjectIdentity
emailAlert=_EmailAlert_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,2,3))
_EmailWarningMailServer_Type=DisplayString
_EmailWarningMailServer_Object=MibScalar
emailWarningMailServer=_EmailWarningMailServer_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,1),_EmailWarningMailServer_Type())
emailWarningMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningMailServer.setStatus(_A)
class _EmailRequiresAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('non-require',0),('require',1)))
_EmailRequiresAuthentication_Type.__name__=_C
_EmailRequiresAuthentication_Object=MibScalar
emailRequiresAuthentication=_EmailRequiresAuthentication_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,2),_EmailRequiresAuthentication_Type())
emailRequiresAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:emailRequiresAuthentication.setStatus(_A)
_EmailWarningUserName_Type=DisplayString
_EmailWarningUserName_Object=MibScalar
emailWarningUserName=_EmailWarningUserName_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,3),_EmailWarningUserName_Type())
emailWarningUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningUserName.setStatus(_A)
_EmailWarningFromEmail_Type=DisplayString
_EmailWarningFromEmail_Object=MibScalar
emailWarningFromEmail=_EmailWarningFromEmail_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,5),_EmailWarningFromEmail_Type())
emailWarningFromEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFromEmail.setStatus(_A)
_EmailWarningFirstEmailAddr_Type=DisplayString
_EmailWarningFirstEmailAddr_Object=MibScalar
emailWarningFirstEmailAddr=_EmailWarningFirstEmailAddr_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,6),_EmailWarningFirstEmailAddr_Type())
emailWarningFirstEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFirstEmailAddr.setStatus(_A)
_EmailWarningSecondEmailAddr_Type=DisplayString
_EmailWarningSecondEmailAddr_Object=MibScalar
emailWarningSecondEmailAddr=_EmailWarningSecondEmailAddr_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,7),_EmailWarningSecondEmailAddr_Type())
emailWarningSecondEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSecondEmailAddr.setStatus(_A)
_EmailWarningThirdEmailAddr_Type=DisplayString
_EmailWarningThirdEmailAddr_Object=MibScalar
emailWarningThirdEmailAddr=_EmailWarningThirdEmailAddr_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,8),_EmailWarningThirdEmailAddr_Type())
emailWarningThirdEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningThirdEmailAddr.setStatus(_A)
_EmailWarningFourthEmailAddr_Type=DisplayString
_EmailWarningFourthEmailAddr_Object=MibScalar
emailWarningFourthEmailAddr=_EmailWarningFourthEmailAddr_Object((1,3,6,1,4,1,8691,2,13,1,5,2,3,9),_EmailWarningFourthEmailAddr_Type())
emailWarningFourthEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFourthEmailAddr.setStatus(_A)
_SnmpTrap_ObjectIdentity=ObjectIdentity
snmpTrap=_SnmpTrap_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,2,4))
_SnmpTrapReceiverIp_Type=DisplayString
_SnmpTrapReceiverIp_Object=MibScalar
snmpTrapReceiverIp=_SnmpTrapReceiverIp_Object((1,3,6,1,4,1,8691,2,13,1,5,2,4,1),_SnmpTrapReceiverIp_Type())
snmpTrapReceiverIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapReceiverIp.setStatus(_A)
class _TrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v1',0),('v2c',1)))
_TrapVersion_Type.__name__=_C
_TrapVersion_Object=MibScalar
trapVersion=_TrapVersion_Object((1,3,6,1,4,1,8691,2,13,1,5,2,4,2),_TrapVersion_Type())
trapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:trapVersion.setStatus(_A)
_Maintenance_ObjectIdentity=ObjectIdentity
maintenance=_Maintenance_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,3))
_ConsoleSettings_ObjectIdentity=ObjectIdentity
consoleSettings=_ConsoleSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,3,1))
class _HttpConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_HttpConsole_Type.__name__=_C
_HttpConsole_Object=MibScalar
httpConsole=_HttpConsole_Object((1,3,6,1,4,1,8691,2,13,1,5,3,1,1),_HttpConsole_Type())
httpConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:httpConsole.setStatus(_A)
class _HttpsConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_HttpsConsole_Type.__name__=_C
_HttpsConsole_Object=MibScalar
httpsConsole=_HttpsConsole_Object((1,3,6,1,4,1,8691,2,13,1,5,3,1,2),_HttpsConsole_Type())
httpsConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:httpsConsole.setStatus(_A)
class _TelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TelnetConsole_Type.__name__=_C
_TelnetConsole_Object=MibScalar
telnetConsole=_TelnetConsole_Object((1,3,6,1,4,1,8691,2,13,1,5,3,1,3),_TelnetConsole_Type())
telnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetConsole.setStatus(_A)
class _SshConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SshConsole_Type.__name__=_C
_SshConsole_Object=MibScalar
sshConsole=_SshConsole_Object((1,3,6,1,4,1,8691,2,13,1,5,3,1,4),_SshConsole_Type())
sshConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConsole.setStatus(_A)
class _SerialConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SerialConsole_Type.__name__=_C
_SerialConsole_Object=MibScalar
serialConsole=_SerialConsole_Object((1,3,6,1,4,1,8691,2,13,1,5,3,1,5),_SerialConsole_Type())
serialConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:serialConsole.setStatus(_A)
class _ResetButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('Disable_after_60_sec',0),('Always_enable',1)))
_ResetButton_Type.__name__=_C
_ResetButton_Object=MibScalar
resetButton=_ResetButton_Object((1,3,6,1,4,1,8691,2,13,1,5,3,1,6),_ResetButton_Type())
resetButton.setMaxAccess(_B)
if mibBuilder.loadTexts:resetButton.setStatus(_A)
_LoadFactoryDefault_ObjectIdentity=ObjectIdentity
loadFactoryDefault=_LoadFactoryDefault_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,5,3,2))
class _LoadFactoryDefaultSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('resetToFactoryDefault-ExcludingIpConfiguration',0),('resetToFactoryDefault',1)))
_LoadFactoryDefaultSetting_Type.__name__=_C
_LoadFactoryDefaultSetting_Object=MibScalar
loadFactoryDefaultSetting=_LoadFactoryDefaultSetting_Object((1,3,6,1,4,1,8691,2,13,1,5,3,2,1),_LoadFactoryDefaultSetting_Type())
loadFactoryDefaultSetting.setMaxAccess(_L)
if mibBuilder.loadTexts:loadFactoryDefaultSetting.setStatus(_A)
_SysStatus_ObjectIdentity=ObjectIdentity
sysStatus=_SysStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6))
_S2eConnections_ObjectIdentity=ObjectIdentity
s2eConnections=_S2eConnections_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6,1))
_MonitorRemoteIpTable_Object=MibTable
monitorRemoteIpTable=_MonitorRemoteIpTable_Object((1,3,6,1,4,1,8691,2,13,1,6,1,1))
if mibBuilder.loadTexts:monitorRemoteIpTable.setStatus(_A)
_MonitorRemoteIpEntry_Object=MibTableRow
monitorRemoteIpEntry=_MonitorRemoteIpEntry_Object((1,3,6,1,4,1,8691,2,13,1,6,1,1,1))
monitorRemoteIpEntry.setIndexNames((0,_G,_H),(0,_G,_AC))
if mibBuilder.loadTexts:monitorRemoteIpEntry.setStatus(_A)
class _RemoteIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RemoteIpIndex_Type.__name__=_C
_RemoteIpIndex_Object=MibTableColumn
remoteIpIndex=_RemoteIpIndex_Object((1,3,6,1,4,1,8691,2,13,1,6,1,1,1,1),_RemoteIpIndex_Type())
remoteIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteIpIndex.setStatus(_A)
_MonitorRemoteIp_Type=IpAddress
_MonitorRemoteIp_Object=MibTableColumn
monitorRemoteIp=_MonitorRemoteIp_Object((1,3,6,1,4,1,8691,2,13,1,6,1,1,1,2),_MonitorRemoteIp_Type())
monitorRemoteIp.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRemoteIp.setStatus(_A)
_SerialPortStatus_ObjectIdentity=ObjectIdentity
serialPortStatus=_SerialPortStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6,2))
_MonitorSerialPortStatusTable_Object=MibTable
monitorSerialPortStatusTable=_MonitorSerialPortStatusTable_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1))
if mibBuilder.loadTexts:monitorSerialPortStatusTable.setStatus(_A)
_MonitorSerialPortStatusEntry_Object=MibTableRow
monitorSerialPortStatusEntry=_MonitorSerialPortStatusEntry_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1))
monitorSerialPortStatusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortStatusEntry.setStatus(_A)
_MonitorTxCount_Type=Integer32
_MonitorTxCount_Object=MibTableColumn
monitorTxCount=_MonitorTxCount_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,1),_MonitorTxCount_Type())
monitorTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTxCount.setStatus(_A)
_MonitorRxCount_Type=Integer32
_MonitorRxCount_Object=MibTableColumn
monitorRxCount=_MonitorRxCount_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,2),_MonitorRxCount_Type())
monitorRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRxCount.setStatus(_A)
_MonitorTxTotalCount_Type=Integer32
_MonitorTxTotalCount_Object=MibTableColumn
monitorTxTotalCount=_MonitorTxTotalCount_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,3),_MonitorTxTotalCount_Type())
monitorTxTotalCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTxTotalCount.setStatus(_A)
_MonitorRxTotalCount_Type=Integer32
_MonitorRxTotalCount_Object=MibTableColumn
monitorRxTotalCount=_MonitorRxTotalCount_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,4),_MonitorRxTotalCount_Type())
monitorRxTotalCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRxTotalCount.setStatus(_A)
class _MonitorDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorDSR_Type.__name__=_C
_MonitorDSR_Object=MibTableColumn
monitorDSR=_MonitorDSR_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,5),_MonitorDSR_Type())
monitorDSR.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDSR.setStatus(_A)
class _MonitorDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorDTR_Type.__name__=_C
_MonitorDTR_Object=MibTableColumn
monitorDTR=_MonitorDTR_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,6),_MonitorDTR_Type())
monitorDTR.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDTR.setStatus(_A)
class _MonitorRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorRTS_Type.__name__=_C
_MonitorRTS_Object=MibTableColumn
monitorRTS=_MonitorRTS_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,7),_MonitorRTS_Type())
monitorRTS.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRTS.setStatus(_A)
class _MonitorCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorCTS_Type.__name__=_C
_MonitorCTS_Object=MibTableColumn
monitorCTS=_MonitorCTS_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,8),_MonitorCTS_Type())
monitorCTS.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorCTS.setStatus(_A)
class _MonitorDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorDCD_Type.__name__=_C
_MonitorDCD_Object=MibTableColumn
monitorDCD=_MonitorDCD_Object((1,3,6,1,4,1,8691,2,13,1,6,2,1,1,9),_MonitorDCD_Type())
monitorDCD.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDCD.setStatus(_A)
_SerialPortErrorCount_ObjectIdentity=ObjectIdentity
serialPortErrorCount=_SerialPortErrorCount_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6,3))
_MonitorSerialPortErrorCountTable_Object=MibTable
monitorSerialPortErrorCountTable=_MonitorSerialPortErrorCountTable_Object((1,3,6,1,4,1,8691,2,13,1,6,3,1))
if mibBuilder.loadTexts:monitorSerialPortErrorCountTable.setStatus(_A)
_MonitorSerialPortErrorCountEntry_Object=MibTableRow
monitorSerialPortErrorCountEntry=_MonitorSerialPortErrorCountEntry_Object((1,3,6,1,4,1,8691,2,13,1,6,3,1,1))
monitorSerialPortErrorCountEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortErrorCountEntry.setStatus(_A)
_MonitorErrorCountFrame_Type=Integer32
_MonitorErrorCountFrame_Object=MibTableColumn
monitorErrorCountFrame=_MonitorErrorCountFrame_Object((1,3,6,1,4,1,8691,2,13,1,6,3,1,1,1),_MonitorErrorCountFrame_Type())
monitorErrorCountFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountFrame.setStatus(_A)
_MonitorErrorCountParity_Type=Integer32
_MonitorErrorCountParity_Object=MibTableColumn
monitorErrorCountParity=_MonitorErrorCountParity_Object((1,3,6,1,4,1,8691,2,13,1,6,3,1,1,2),_MonitorErrorCountParity_Type())
monitorErrorCountParity.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountParity.setStatus(_A)
_MonitorErrorCountOverrun_Type=Integer32
_MonitorErrorCountOverrun_Object=MibTableColumn
monitorErrorCountOverrun=_MonitorErrorCountOverrun_Object((1,3,6,1,4,1,8691,2,13,1,6,3,1,1,3),_MonitorErrorCountOverrun_Type())
monitorErrorCountOverrun.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountOverrun.setStatus(_A)
_MonitorErrorCountBreak_Type=Integer32
_MonitorErrorCountBreak_Object=MibTableColumn
monitorErrorCountBreak=_MonitorErrorCountBreak_Object((1,3,6,1,4,1,8691,2,13,1,6,3,1,1,4),_MonitorErrorCountBreak_Type())
monitorErrorCountBreak.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountBreak.setStatus(_A)
_SerialPortSettings_ObjectIdentity=ObjectIdentity
serialPortSettings=_SerialPortSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6,4))
_MonitorSerialPortSettingsTable_Object=MibTable
monitorSerialPortSettingsTable=_MonitorSerialPortSettingsTable_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1))
if mibBuilder.loadTexts:monitorSerialPortSettingsTable.setStatus(_A)
_MonitorSerialPortSettingsEntry_Object=MibTableRow
monitorSerialPortSettingsEntry=_MonitorSerialPortSettingsEntry_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1))
monitorSerialPortSettingsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortSettingsEntry.setStatus(_A)
_MonitorBaudRate_Type=Integer32
_MonitorBaudRate_Object=MibTableColumn
monitorBaudRate=_MonitorBaudRate_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,1),_MonitorBaudRate_Type())
monitorBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorBaudRate.setStatus(_A)
class _MonitorDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8)));namedValues=NamedValues(*(('bits-5',5),('bits-6',6),('bits-7',7),('bits-8',8)))
_MonitorDataBits_Type.__name__=_C
_MonitorDataBits_Object=MibTableColumn
monitorDataBits=_MonitorDataBits_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,2),_MonitorDataBits_Type())
monitorDataBits.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDataBits.setStatus(_A)
_MonitorStopBits_Type=DisplayString
_MonitorStopBits_Object=MibTableColumn
monitorStopBits=_MonitorStopBits_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,3),_MonitorStopBits_Type())
monitorStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorStopBits.setStatus(_A)
class _MonitorParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8,24,40,56)));namedValues=NamedValues(*((_O,0),('odd',8),('even',24),('mark',40),('space',56)))
_MonitorParity_Type.__name__=_C
_MonitorParity_Object=MibTableColumn
monitorParity=_MonitorParity_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,4),_MonitorParity_Type())
monitorParity.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorParity.setStatus(_A)
class _MonitorRTSCTSFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorRTSCTSFlowControl_Type.__name__=_C
_MonitorRTSCTSFlowControl_Object=MibTableColumn
monitorRTSCTSFlowControl=_MonitorRTSCTSFlowControl_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,5),_MonitorRTSCTSFlowControl_Type())
monitorRTSCTSFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRTSCTSFlowControl.setStatus(_A)
class _MonitorXONXOFFFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_MonitorXONXOFFFlowControl_Type.__name__=_C
_MonitorXONXOFFFlowControl_Object=MibTableColumn
monitorXONXOFFFlowControl=_MonitorXONXOFFFlowControl_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,6),_MonitorXONXOFFFlowControl_Type())
monitorXONXOFFFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorXONXOFFFlowControl.setStatus(_A)
class _MonitorFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MonitorFIFO_Type.__name__=_C
_MonitorFIFO_Object=MibTableColumn
monitorFIFO=_MonitorFIFO_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,7),_MonitorFIFO_Type())
monitorFIFO.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFIFO.setStatus(_A)
class _MonitorInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rs-232',0),('rs-422',1),('rs-485-2-wire',2),('rs-485-4-wire',3)))
_MonitorInterface_Type.__name__=_C
_MonitorInterface_Object=MibTableColumn
monitorInterface=_MonitorInterface_Object((1,3,6,1,4,1,8691,2,13,1,6,4,1,1,8),_MonitorInterface_Type())
monitorInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorInterface.setStatus(_A)
_SerialPortBuffering_ObjectIdentity=ObjectIdentity
serialPortBuffering=_SerialPortBuffering_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6,5))
_MonitorSerialPortBufferingTable_Object=MibTable
monitorSerialPortBufferingTable=_MonitorSerialPortBufferingTable_Object((1,3,6,1,4,1,8691,2,13,1,6,5,1))
if mibBuilder.loadTexts:monitorSerialPortBufferingTable.setStatus(_A)
_MonitorSerialPortBufferingEntry_Object=MibTableRow
monitorSerialPortBufferingEntry=_MonitorSerialPortBufferingEntry_Object((1,3,6,1,4,1,8691,2,13,1,6,5,1,1))
monitorSerialPortBufferingEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortBufferingEntry.setStatus(_A)
_MonitorBuffering_Type=Integer32
_MonitorBuffering_Object=MibTableColumn
monitorBuffering=_MonitorBuffering_Object((1,3,6,1,4,1,8691,2,13,1,6,5,1,1,1),_MonitorBuffering_Type())
monitorBuffering.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorBuffering.setStatus(_A)
_SysWlanStatus_ObjectIdentity=ObjectIdentity
sysWlanStatus=_SysWlanStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,6,6))
_WlanStatusActiveProfileName_Type=DisplayString
_WlanStatusActiveProfileName_Object=MibScalar
wlanStatusActiveProfileName=_WlanStatusActiveProfileName_Object((1,3,6,1,4,1,8691,2,13,1,6,6,1),_WlanStatusActiveProfileName_Type())
wlanStatusActiveProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusActiveProfileName.setStatus(_A)
class _WlanStatusIpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2)))
_WlanStatusIpConfiguration_Type.__name__=_C
_WlanStatusIpConfiguration_Object=MibScalar
wlanStatusIpConfiguration=_WlanStatusIpConfiguration_Object((1,3,6,1,4,1,8691,2,13,1,6,6,2),_WlanStatusIpConfiguration_Type())
wlanStatusIpConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusIpConfiguration.setStatus(_A)
_WlanStatusIpAddress_Type=IpAddress
_WlanStatusIpAddress_Object=MibScalar
wlanStatusIpAddress=_WlanStatusIpAddress_Object((1,3,6,1,4,1,8691,2,13,1,6,6,3),_WlanStatusIpAddress_Type())
wlanStatusIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusIpAddress.setStatus(_A)
_WlanStatusNetMask_Type=IpAddress
_WlanStatusNetMask_Object=MibScalar
wlanStatusNetMask=_WlanStatusNetMask_Object((1,3,6,1,4,1,8691,2,13,1,6,6,4),_WlanStatusNetMask_Type())
wlanStatusNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusNetMask.setStatus(_A)
_WlanStatusDefaultGateway_Type=IpAddress
_WlanStatusDefaultGateway_Object=MibScalar
wlanStatusDefaultGateway=_WlanStatusDefaultGateway_Object((1,3,6,1,4,1,8691,2,13,1,6,6,5),_WlanStatusDefaultGateway_Type())
wlanStatusDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusDefaultGateway.setStatus(_A)
_WlanStatusNetworkType_Type=DisplayString
_WlanStatusNetworkType_Object=MibScalar
wlanStatusNetworkType=_WlanStatusNetworkType_Object((1,3,6,1,4,1,8691,2,13,1,6,6,6),_WlanStatusNetworkType_Type())
wlanStatusNetworkType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusNetworkType.setStatus(_A)
_WlanStatusRFType_Type=DisplayString
_WlanStatusRFType_Object=MibScalar
wlanStatusRFType=_WlanStatusRFType_Object((1,3,6,1,4,1,8691,2,13,1,6,6,7),_WlanStatusRFType_Type())
wlanStatusRFType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusRFType.setStatus(_A)
_WlanStatusSSID_Type=DisplayString
_WlanStatusSSID_Object=MibScalar
wlanStatusSSID=_WlanStatusSSID_Object((1,3,6,1,4,1,8691,2,13,1,6,6,8),_WlanStatusSSID_Type())
wlanStatusSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusSSID.setStatus(_A)
_WlanStatusChannel_Type=DisplayString
_WlanStatusChannel_Object=MibScalar
wlanStatusChannel=_WlanStatusChannel_Object((1,3,6,1,4,1,8691,2,13,1,6,6,9),_WlanStatusChannel_Type())
wlanStatusChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusChannel.setStatus(_A)
_WlanStatusAuthentication_Type=DisplayString
_WlanStatusAuthentication_Object=MibScalar
wlanStatusAuthentication=_WlanStatusAuthentication_Object((1,3,6,1,4,1,8691,2,13,1,6,6,10),_WlanStatusAuthentication_Type())
wlanStatusAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusAuthentication.setStatus(_A)
_WlanStatusEncryption_Type=DisplayString
_WlanStatusEncryption_Object=MibScalar
wlanStatusEncryption=_WlanStatusEncryption_Object((1,3,6,1,4,1,8691,2,13,1,6,6,11),_WlanStatusEncryption_Type())
wlanStatusEncryption.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusEncryption.setStatus(_A)
_WlanStatusRegion_Type=DisplayString
_WlanStatusRegion_Object=MibScalar
wlanStatusRegion=_WlanStatusRegion_Object((1,3,6,1,4,1,8691,2,13,1,6,6,12),_WlanStatusRegion_Type())
wlanStatusRegion.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusRegion.setStatus(_A)
_WlanStatusSignalStrength_Type=DisplayString
_WlanStatusSignalStrength_Object=MibScalar
wlanStatusSignalStrength=_WlanStatusSignalStrength_Object((1,3,6,1,4,1,8691,2,13,1,6,6,13),_WlanStatusSignalStrength_Type())
wlanStatusSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusSignalStrength.setStatus(_A)
_WlanStatusConnectionSpeed_Type=DisplayString
_WlanStatusConnectionSpeed_Object=MibScalar
wlanStatusConnectionSpeed=_WlanStatusConnectionSpeed_Object((1,3,6,1,4,1,8691,2,13,1,6,6,14),_WlanStatusConnectionSpeed_Type())
wlanStatusConnectionSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusConnectionSpeed.setStatus(_A)
_WlanStatusCurrentBSSID_Type=DisplayString
_WlanStatusCurrentBSSID_Object=MibScalar
wlanStatusCurrentBSSID=_WlanStatusCurrentBSSID_Object((1,3,6,1,4,1,8691,2,13,1,6,6,15),_WlanStatusCurrentBSSID_Type())
wlanStatusCurrentBSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusCurrentBSSID.setStatus(_A)
_ActivateSettings_ObjectIdentity=ObjectIdentity
activateSettings=_ActivateSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,7))
class _DoActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('activate',1))
_DoActivate_Type.__name__=_C
_DoActivate_Object=MibScalar
doActivate=_DoActivate_Object((1,3,6,1,4,1,8691,2,13,1,7,1),_DoActivate_Type())
doActivate.setMaxAccess(_L)
if mibBuilder.loadTexts:doActivate.setStatus(_A)
_Restart_ObjectIdentity=ObjectIdentity
restart=_Restart_ObjectIdentity((1,3,6,1,4,1,8691,2,13,1,8))
class _RestartPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('port1',0),('port2',1)))
_RestartPorts_Type.__name__=_C
_RestartPorts_Object=MibScalar
restartPorts=_RestartPorts_Object((1,3,6,1,4,1,8691,2,13,1,8,1),_RestartPorts_Type())
restartPorts.setMaxAccess(_L)
if mibBuilder.loadTexts:restartPorts.setStatus(_A)
class _RestartSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_RestartSystem_Type.__name__=_C
_RestartSystem_Object=MibScalar
restartSystem=_RestartSystem_Object((1,3,6,1,4,1,8691,2,13,1,8,2),_RestartSystem_Type())
restartSystem.setMaxAccess(_L)
if mibBuilder.loadTexts:restartSystem.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'PortList':PortList,'moxa':moxa,'nport':nport,'w2x50A':w2x50A,'swMgmt':swMgmt,'overview':overview,'modelName':modelName,'serialNumber':serialNumber,'firmwareVersion':firmwareVersion,'ethIPAddress':ethIPAddress,'ethMacAddress':ethMacAddress,'wlanIPAddress':wlanIPAddress,'wlanMacAddress':wlanMacAddress,'wlanSSID':wlanSSID,'wlanNetworkType':wlanNetworkType,'wlanSecurityMode':wlanSecurityMode,'wlanRFType':wlanRFType,'wlanCountryCode':wlanCountryCode,'wlanFastRoaming':wlanFastRoaming,'activeNetworkPort':activeNetworkPort,'upTime':upTime,'serialPort1':serialPort1,'serialPort2':serialPort2,'basicSetting':basicSetting,'serverSetting':serverSetting,'serverName':serverName,'serverLocation':serverLocation,'timeSetting':timeSetting,'timeZone':timeZone,'localTime':localTime,'timeServer':timeServer,'networkSetting':networkSetting,'generalSetting':generalSetting,'dnsServer1IpAddr':dnsServer1IpAddr,'dnsServer2IpAddr':dnsServer2IpAddr,'ethernetSetting':ethernetSetting,'ethIpConfiguration':ethIpConfiguration,'ethIpAddress':ethIpAddress,'ethNetMask':ethNetMask,'ethDefaultGateway':ethDefaultGateway,'ethBridgeMode':ethBridgeMode,'wlanSetting':wlanSetting,'wlanIpConfiguration':wlanIpConfiguration,'wlanIpAddress':wlanIpAddress,'wlanNetMask':wlanNetMask,'wlanDefaultGateway':wlanDefaultGateway,'profileSetting':profileSetting,'networkType':networkType,'adhocProfile':adhocProfile,'adhocGeneralSetting':adhocGeneralSetting,'adhocProfileName':adhocProfileName,'adhocRFType':adhocRFType,'adhocWlanSSID':adhocWlanSSID,'adhocChannel':adhocChannel,'adhocSecuritySetting':adhocSecuritySetting,'adhocAuthentication':adhocAuthentication,'adhocEncryption':adhocEncryption,'adhocWepKeyLength':adhocWepKeyLength,'adhocWepKeyIndex':adhocWepKeyIndex,'adhocWepKeyPassphrase':adhocWepKeyPassphrase,'adhocWepKeyFormat':adhocWepKeyFormat,'infrastructureProfile':infrastructureProfile,'infraGeneralSetting':infraGeneralSetting,'infraGeneralSettingTable':infraGeneralSettingTable,'infraGeneralSettingEntry':infraGeneralSettingEntry,_S:profileIndex,'profileName':profileName,'profileRFType':profileRFType,'profileWlanSSID':profileWlanSSID,'securitySetting':securitySetting,'securitySettingTable':securitySettingTable,'securitySettingEntry':securitySettingEntry,'authentication':authentication,'encryption':encryption,'wepKeyLength':wepKeyLength,'wepKeyIndex':wepKeyIndex,'wepKeyPassphrase':wepKeyPassphrase,'wepKeyFormat':wepKeyFormat,'eapMethod':eapMethod,'tunneledAuth':tunneledAuth,'wpaUsername':wpaUsername,'wpaAnonymousUsername':wpaAnonymousUsername,'verifyServerCert':verifyServerCert,'trustedServerCert':trustedServerCert,'userCert':userCert,'userPrivateKey':userPrivateKey,'fastRoamingSetting':fastRoamingSetting,'fastRoamingScanChannels1':fastRoamingScanChannels1,'fastRoamingScanChannels2':fastRoamingScanChannels2,'fastRoamingScanChannels3':fastRoamingScanChannels3,'fastRoamingThreshold':fastRoamingThreshold,'fastRoamingDifference':fastRoamingDifference,'wlanLogSetting':wlanLogSetting,'wlanLogEnable':wlanLogEnable,'advancedSetting':advancedSetting,'gratuitousArp':gratuitousArp,'gratuitousArpSendPeriod':gratuitousArpSendPeriod,'gratuitousArpIpAddress1':gratuitousArpIpAddress1,'gratuitousArpMacAddress1':gratuitousArpMacAddress1,'gratuitousArpIpAddress2':gratuitousArpIpAddress2,'gratuitousArpMacAddress2':gratuitousArpMacAddress2,'gratuitousArpIpAddress3':gratuitousArpIpAddress3,'gratuitousArpMacAddress3':gratuitousArpMacAddress3,'gratuitousArpIpAddress4':gratuitousArpIpAddress4,'gratuitousArpMacAddress4':gratuitousArpMacAddress4,'portSetting':portSetting,'opModeSetting':opModeSetting,'opMode':opMode,'opModePortTable':opModePortTable,'opModePortEntry':opModePortEntry,_H:portIndex,'portMode':portMode,'opModeParam':opModeParam,'realCOM':realCOM,'realCOMTable':realCOMTable,'realCOMEntry':realCOMEntry,'realCOMTcpAliveCheck':realCOMTcpAliveCheck,'realCOMMaxConnection':realCOMMaxConnection,'realCOMIgnoreJammedIp':realCOMIgnoreJammedIp,'realCOMAllowDriverControl':realCOMAllowDriverControl,'realCOMConnectionDownRTS':realCOMConnectionDownRTS,'realCOMConnectionDownDTR':realCOMConnectionDownDTR,'rfc2217':rfc2217,'rfc2217Table':rfc2217Table,'rfc2217Entry':rfc2217Entry,'rfc2217TcpAliveCheck':rfc2217TcpAliveCheck,'rfc2217TcpPort':rfc2217TcpPort,'tcpServer':tcpServer,'tcpServerTable':tcpServerTable,'tcpServerEntry':tcpServerEntry,'tcpServerTcpAliveCheck':tcpServerTcpAliveCheck,'tcpServerInactivityTime':tcpServerInactivityTime,'tcpServerMaxConnection':tcpServerMaxConnection,'tcpServerIgnoreJammedIp':tcpServerIgnoreJammedIp,'tcpServerAllowDriverControl':tcpServerAllowDriverControl,'tcpServerTcpPort':tcpServerTcpPort,'tcpServerCmdPort':tcpServerCmdPort,'tcpServerConnectionDownRTS':tcpServerConnectionDownRTS,'tcpServerConnectionDownDTR':tcpServerConnectionDownDTR,'tcpClient':tcpClient,'tcpClientTable':tcpClientTable,'tcpClientEntry':tcpClientEntry,'tcpClientTcpAliveCheck':tcpClientTcpAliveCheck,'tcpClientInactivityTime':tcpClientInactivityTime,'tcpClientIgnoreJammedIp':tcpClientIgnoreJammedIp,'tcpClientDestinationAddress1':tcpClientDestinationAddress1,'tcpClientDestinationPort1':tcpClientDestinationPort1,'tcpClientDestinationAddress2':tcpClientDestinationAddress2,'tcpClientDestinationPort2':tcpClientDestinationPort2,'tcpClientDestinationAddress3':tcpClientDestinationAddress3,'tcpClientDestinationPort3':tcpClientDestinationPort3,'tcpClientDestinationAddress4':tcpClientDestinationAddress4,'tcpClientDestinationPort4':tcpClientDestinationPort4,'tcpClientDesignatedLocalPort1':tcpClientDesignatedLocalPort1,'tcpClientDesignatedLocalPort2':tcpClientDesignatedLocalPort2,'tcpClientDesignatedLocalPort3':tcpClientDesignatedLocalPort3,'tcpClientDesignatedLocalPort4':tcpClientDesignatedLocalPort4,'tcpClientConnectionControl':tcpClientConnectionControl,'udp':udp,'udpTable':udpTable,'udpEntry':udpEntry,'udpDestinationAddress1Begin':udpDestinationAddress1Begin,'udpDestinationAddress1End':udpDestinationAddress1End,'udpDestinationPort1':udpDestinationPort1,'udpDestinationAddress2Begin':udpDestinationAddress2Begin,'udpDestinationAddress2End':udpDestinationAddress2End,'udpDestinationPort2':udpDestinationPort2,'udpDestinationAddress3Begin':udpDestinationAddress3Begin,'udpDestinationAddress3End':udpDestinationAddress3End,'udpDestinationPort3':udpDestinationPort3,'udpDestinationAddress4Begin':udpDestinationAddress4Begin,'udpDestinationAddress4End':udpDestinationAddress4End,'udpDestinationPort4':udpDestinationPort4,'udpLocalListenPort':udpLocalListenPort,'pairConnectionMaster':pairConnectionMaster,'pairConnectionMasterTable':pairConnectionMasterTable,'pairConnectionMasterEntry':pairConnectionMasterEntry,'pairConnectionMasterTcpAliveCheck':pairConnectionMasterTcpAliveCheck,'pairConnectionMasterDestnationAddress':pairConnectionMasterDestnationAddress,'pairConnectionMasterDestnationTcpPort':pairConnectionMasterDestnationTcpPort,'pairConnectionSlave':pairConnectionSlave,'pairConnectionSlaveTable':pairConnectionSlaveTable,'pairConnectionSlaveEntry':pairConnectionSlaveEntry,'pairConnectionSlaveTcpAliveCheck':pairConnectionSlaveTcpAliveCheck,'pairConnectionSlaveLocalTcpPort':pairConnectionSlaveLocalTcpPort,'ethernetModem':ethernetModem,'ethernetModemTable':ethernetModemTable,'ethernetModemEntry':ethernetModemEntry,'ethernetModemTcpAliveCheck':ethernetModemTcpAliveCheck,'ethernetModemLocalTcpPort':ethernetModemLocalTcpPort,'reverseTerminal':reverseTerminal,'reverseTerminalTable':reverseTerminalTable,'reverseTerminalEntry':reverseTerminalEntry,'reverseTerminalTcpAliveCheck':reverseTerminalTcpAliveCheck,'reverseTerminalInactivityTime':reverseTerminalInactivityTime,'reverseTerminalTcpPort':reverseTerminalTcpPort,'reverseTerminalAuthenticationType':reverseTerminalAuthenticationType,'reverseTerminalMapKeys':reverseTerminalMapKeys,'dataPacking':dataPacking,'dataPackingPortTable':dataPackingPortTable,'dataPackingPortEntry':dataPackingPortEntry,'portPacketLength':portPacketLength,'portDelimiter1Enable':portDelimiter1Enable,'portDelimiter1':portDelimiter1,'portDelimiter2Enable':portDelimiter2Enable,'portDelimiter2':portDelimiter2,'portDelimiterProcess':portDelimiterProcess,'portForceTransmit':portForceTransmit,'comParamSetting':comParamSetting,'comParamPortTable':comParamPortTable,'comParamPortEntry':comParamPortEntry,'portAlias':portAlias,'portInterface':portInterface,'portBaudRate':portBaudRate,'portDataBits':portDataBits,'portStopBits':portStopBits,'portParity':portParity,'portFlowControl':portFlowControl,'portFIFO':portFIFO,'dataBuffering':dataBuffering,'dataBufferingPortTable':dataBufferingPortTable,'dataBufferingPortEntry':dataBufferingPortEntry,'portBufferingEnable':portBufferingEnable,'portSerialDataLoggingEnable':portSerialDataLoggingEnable,'sysManagement':sysManagement,'miscNetworkSettings':miscNetworkSettings,'accessibleIp':accessibleIp,'enableAccessibleIpList':enableAccessibleIpList,'accessibleIpListTable':accessibleIpListTable,'accessibleIpListEntry':accessibleIpListEntry,_AB:accessibleIpListIndex,'activeAccessibleIpList':activeAccessibleIpList,'accessibleIpListAddress':accessibleIpListAddress,'accessibleIpListNetmask':accessibleIpListNetmask,'snmpAgentSettings':snmpAgentSettings,'snmpEnable':snmpEnable,'snmpContactName':snmpContactName,'snmpLocation':snmpLocation,'authenticationServer':authenticationServer,'radiusServerIp':radiusServerIp,'udpPortAuthenticationServer':udpPortAuthenticationServer,'radiusAccounting':radiusAccounting,'sysLogSettings':sysLogSettings,'sysLocalLog':sysLocalLog,'networkLocalLog':networkLocalLog,'configLocalLog':configLocalLog,'opModeLocalLog':opModeLocalLog,'autoWarningSettings':autoWarningSettings,'eventSettings':eventSettings,'mailWarningColdStart':mailWarningColdStart,'mailWarningWarmStart':mailWarningWarmStart,'mailWarningAuthFailure':mailWarningAuthFailure,'mailWarningIpChanged':mailWarningIpChanged,'mailWarningPasswordChanged':mailWarningPasswordChanged,'trapServerColdStart':trapServerColdStart,'trapServerWarmStart':trapServerWarmStart,'trapServerAuthFailure':trapServerAuthFailure,'serialEventSettings':serialEventSettings,'portEventSettingsTable':portEventSettingsTable,'portEventSettingsEntry':portEventSettingsEntry,'mailDCDchange':mailDCDchange,'trapDCDchange':trapDCDchange,'mailDSRchange':mailDSRchange,'trapDSRchange':trapDSRchange,'emailAlert':emailAlert,'emailWarningMailServer':emailWarningMailServer,'emailRequiresAuthentication':emailRequiresAuthentication,'emailWarningUserName':emailWarningUserName,'emailWarningFromEmail':emailWarningFromEmail,'emailWarningFirstEmailAddr':emailWarningFirstEmailAddr,'emailWarningSecondEmailAddr':emailWarningSecondEmailAddr,'emailWarningThirdEmailAddr':emailWarningThirdEmailAddr,'emailWarningFourthEmailAddr':emailWarningFourthEmailAddr,'snmpTrap':snmpTrap,'snmpTrapReceiverIp':snmpTrapReceiverIp,'trapVersion':trapVersion,'maintenance':maintenance,'consoleSettings':consoleSettings,'httpConsole':httpConsole,'httpsConsole':httpsConsole,'telnetConsole':telnetConsole,'sshConsole':sshConsole,'serialConsole':serialConsole,'resetButton':resetButton,'loadFactoryDefault':loadFactoryDefault,'loadFactoryDefaultSetting':loadFactoryDefaultSetting,'sysStatus':sysStatus,'s2eConnections':s2eConnections,'monitorRemoteIpTable':monitorRemoteIpTable,'monitorRemoteIpEntry':monitorRemoteIpEntry,_AC:remoteIpIndex,'monitorRemoteIp':monitorRemoteIp,'serialPortStatus':serialPortStatus,'monitorSerialPortStatusTable':monitorSerialPortStatusTable,'monitorSerialPortStatusEntry':monitorSerialPortStatusEntry,'monitorTxCount':monitorTxCount,'monitorRxCount':monitorRxCount,'monitorTxTotalCount':monitorTxTotalCount,'monitorRxTotalCount':monitorRxTotalCount,'monitorDSR':monitorDSR,'monitorDTR':monitorDTR,'monitorRTS':monitorRTS,'monitorCTS':monitorCTS,'monitorDCD':monitorDCD,'serialPortErrorCount':serialPortErrorCount,'monitorSerialPortErrorCountTable':monitorSerialPortErrorCountTable,'monitorSerialPortErrorCountEntry':monitorSerialPortErrorCountEntry,'monitorErrorCountFrame':monitorErrorCountFrame,'monitorErrorCountParity':monitorErrorCountParity,'monitorErrorCountOverrun':monitorErrorCountOverrun,'monitorErrorCountBreak':monitorErrorCountBreak,'serialPortSettings':serialPortSettings,'monitorSerialPortSettingsTable':monitorSerialPortSettingsTable,'monitorSerialPortSettingsEntry':monitorSerialPortSettingsEntry,'monitorBaudRate':monitorBaudRate,'monitorDataBits':monitorDataBits,'monitorStopBits':monitorStopBits,'monitorParity':monitorParity,'monitorRTSCTSFlowControl':monitorRTSCTSFlowControl,'monitorXONXOFFFlowControl':monitorXONXOFFFlowControl,'monitorFIFO':monitorFIFO,'monitorInterface':monitorInterface,'serialPortBuffering':serialPortBuffering,'monitorSerialPortBufferingTable':monitorSerialPortBufferingTable,'monitorSerialPortBufferingEntry':monitorSerialPortBufferingEntry,'monitorBuffering':monitorBuffering,'sysWlanStatus':sysWlanStatus,'wlanStatusActiveProfileName':wlanStatusActiveProfileName,'wlanStatusIpConfiguration':wlanStatusIpConfiguration,'wlanStatusIpAddress':wlanStatusIpAddress,'wlanStatusNetMask':wlanStatusNetMask,'wlanStatusDefaultGateway':wlanStatusDefaultGateway,'wlanStatusNetworkType':wlanStatusNetworkType,'wlanStatusRFType':wlanStatusRFType,'wlanStatusSSID':wlanStatusSSID,'wlanStatusChannel':wlanStatusChannel,'wlanStatusAuthentication':wlanStatusAuthentication,'wlanStatusEncryption':wlanStatusEncryption,'wlanStatusRegion':wlanStatusRegion,'wlanStatusSignalStrength':wlanStatusSignalStrength,'wlanStatusConnectionSpeed':wlanStatusConnectionSpeed,'wlanStatusCurrentBSSID':wlanStatusCurrentBSSID,'activateSettings':activateSettings,'doActivate':doActivate,'restart':restart,'restartPorts':restartPorts,'restartSystem':restartSystem})