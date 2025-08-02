_AQ='alarmAcked'
_AP='doMonIndex'
_AO='diMonIndex'
_AN='remoteIpIndex'
_AM='accessibleIpListIndex'
_AL='highToLow'
_AK='key-128-bits'
_AJ='key-64-bits'
_AI='open-system'
_AH='w802_11b_g'
_AG='alarm'
_AF='channel_165'
_AE='channel_161'
_AD='channel_157'
_AC='channel_153'
_AB='channel_149'
_AA='channel_140'
_A9='channel_136'
_A8='channel_132'
_A7='channel_128'
_A6='channel_124'
_A5='channel_120'
_A4='channel_116'
_A3='channel_112'
_A2='channel_108'
_A1='channel_104'
_A0='channel_100'
_z='channel_64'
_y='channel_60'
_x='channel_56'
_w='channel_52'
_v='channel_48'
_u='channel_44'
_t='channel_40'
_s='channel_36'
_r='channel_13'
_q='channel_12'
_p='channel_11'
_o='channel_10'
_n='channel_9'
_m='channel_8'
_l='channel_7'
_k='channel_6'
_j='channel_5'
_i='channel_4'
_h='channel_3'
_g='channel_2'
_f='channel_1'
_e='n_a'
_d='installed'
_c='not-installed'
_b='profileIndex'
_a='bootp'
_Z='dhcp'
_Y='static'
_X='not-accessible'
_W='none'
_V='always-low'
_U='always-high'
_T='on'
_S='off'
_R='fc01_CoilStatus'
_Q='fc03_HoldingRegister'
_P='fc02_InputStatus'
_O='dt_2_word'
_N='dt_1_word'
_M='dt_1_bit'
_L='rw'
_K='r'
_J='fc04_InputRegister'
_I='DisplayString'
_H='portIndex'
_G='MOXA-IAW5x50A_IO-MIB'
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
iaw5x50AIO=ModuleIdentity((1,3,6,1,4,1,8691,2,21))
class PortList(TextualConvention,OctetString):status=_A
_Moxa_ObjectIdentity=ObjectIdentity
moxa=_Moxa_ObjectIdentity((1,3,6,1,4,1,8691))
_Nport_ObjectIdentity=ObjectIdentity
nport=_Nport_ObjectIdentity((1,3,6,1,4,1,8691,2))
_SwMgmt_ObjectIdentity=ObjectIdentity
swMgmt=_SwMgmt_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1))
_Overview_ObjectIdentity=ObjectIdentity
overview=_Overview_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,1))
_ModelName_Type=DisplayString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,8691,2,21,1,1,1),_ModelName_Type())
modelName.setMaxAccess(_D)
if mibBuilder.loadTexts:modelName.setStatus(_A)
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,8691,2,21,1,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,8691,2,21,1,1,3),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
_EthIPAddress_Type=DisplayString
_EthIPAddress_Object=MibScalar
ethIPAddress=_EthIPAddress_Object((1,3,6,1,4,1,8691,2,21,1,1,4),_EthIPAddress_Type())
ethIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIPAddress.setStatus(_A)
_EthMacAddress_Type=MacAddress
_EthMacAddress_Object=MibScalar
ethMacAddress=_EthMacAddress_Object((1,3,6,1,4,1,8691,2,21,1,1,5),_EthMacAddress_Type())
ethMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ethMacAddress.setStatus(_A)
_WlanIPAddress_Type=DisplayString
_WlanIPAddress_Object=MibScalar
wlanIPAddress=_WlanIPAddress_Object((1,3,6,1,4,1,8691,2,21,1,1,6),_WlanIPAddress_Type())
wlanIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIPAddress.setStatus(_A)
_WlanMacAddress_Type=MacAddress
_WlanMacAddress_Object=MibScalar
wlanMacAddress=_WlanMacAddress_Object((1,3,6,1,4,1,8691,2,21,1,1,7),_WlanMacAddress_Type())
wlanMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMacAddress.setStatus(_A)
_WlanSSID_Type=DisplayString
_WlanSSID_Object=MibScalar
wlanSSID=_WlanSSID_Object((1,3,6,1,4,1,8691,2,21,1,1,8),_WlanSSID_Type())
wlanSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanSSID.setStatus(_A)
_WlanNetworkType_Type=DisplayString
_WlanNetworkType_Object=MibScalar
wlanNetworkType=_WlanNetworkType_Object((1,3,6,1,4,1,8691,2,21,1,1,9),_WlanNetworkType_Type())
wlanNetworkType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanNetworkType.setStatus(_A)
_WlanSecurityMode_Type=DisplayString
_WlanSecurityMode_Object=MibScalar
wlanSecurityMode=_WlanSecurityMode_Object((1,3,6,1,4,1,8691,2,21,1,1,10),_WlanSecurityMode_Type())
wlanSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanSecurityMode.setStatus(_A)
_WlanRFType_Type=DisplayString
_WlanRFType_Object=MibScalar
wlanRFType=_WlanRFType_Object((1,3,6,1,4,1,8691,2,21,1,1,11),_WlanRFType_Type())
wlanRFType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanRFType.setStatus(_A)
_WlanCountryCode_Type=DisplayString
_WlanCountryCode_Object=MibScalar
wlanCountryCode=_WlanCountryCode_Object((1,3,6,1,4,1,8691,2,21,1,1,12),_WlanCountryCode_Type())
wlanCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanCountryCode.setStatus(_A)
_WlanFastRoaming_Type=DisplayString
_WlanFastRoaming_Object=MibScalar
wlanFastRoaming=_WlanFastRoaming_Object((1,3,6,1,4,1,8691,2,21,1,1,13),_WlanFastRoaming_Type())
wlanFastRoaming.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanFastRoaming.setStatus(_A)
_ActiveNetworkPort_Type=DisplayString
_ActiveNetworkPort_Object=MibScalar
activeNetworkPort=_ActiveNetworkPort_Object((1,3,6,1,4,1,8691,2,21,1,1,14),_ActiveNetworkPort_Type())
activeNetworkPort.setMaxAccess(_D)
if mibBuilder.loadTexts:activeNetworkPort.setStatus(_A)
_UpTime_Type=DisplayString
_UpTime_Object=MibScalar
upTime=_UpTime_Object((1,3,6,1,4,1,8691,2,21,1,1,15),_UpTime_Type())
upTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upTime.setStatus(_A)
_SerialPort1_Type=DisplayString
_SerialPort1_Object=MibScalar
serialPort1=_SerialPort1_Object((1,3,6,1,4,1,8691,2,21,1,1,16),_SerialPort1_Type())
serialPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:serialPort1.setStatus(_A)
_SerialPort2_Type=DisplayString
_SerialPort2_Object=MibScalar
serialPort2=_SerialPort2_Object((1,3,6,1,4,1,8691,2,21,1,1,17),_SerialPort2_Type())
serialPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:serialPort2.setStatus(_A)
_BasicSetting_ObjectIdentity=ObjectIdentity
basicSetting=_BasicSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,2))
_ServerSetting_ObjectIdentity=ObjectIdentity
serverSetting=_ServerSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,2,1))
_ServerName_Type=DisplayString
_ServerName_Object=MibScalar
serverName=_ServerName_Object((1,3,6,1,4,1,8691,2,21,1,2,1,1),_ServerName_Type())
serverName.setMaxAccess(_B)
if mibBuilder.loadTexts:serverName.setStatus(_A)
_ServerLocation_Type=DisplayString
_ServerLocation_Object=MibScalar
serverLocation=_ServerLocation_Object((1,3,6,1,4,1,8691,2,21,1,2,1,2),_ServerLocation_Type())
serverLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:serverLocation.setStatus(_A)
class _EnableServerSocketIdleConnectionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableServerSocketIdleConnectionTimeout_Type.__name__=_C
_EnableServerSocketIdleConnectionTimeout_Object=MibScalar
enableServerSocketIdleConnectionTimeout=_EnableServerSocketIdleConnectionTimeout_Object((1,3,6,1,4,1,8691,2,21,1,2,1,3),_EnableServerSocketIdleConnectionTimeout_Type())
enableServerSocketIdleConnectionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:enableServerSocketIdleConnectionTimeout.setStatus(_A)
class _ServerSocketIdleConnectionTimeoutInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ServerSocketIdleConnectionTimeoutInterval_Type.__name__=_C
_ServerSocketIdleConnectionTimeoutInterval_Object=MibScalar
serverSocketIdleConnectionTimeoutInterval=_ServerSocketIdleConnectionTimeoutInterval_Object((1,3,6,1,4,1,8691,2,21,1,2,1,4),_ServerSocketIdleConnectionTimeoutInterval_Type())
serverSocketIdleConnectionTimeoutInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:serverSocketIdleConnectionTimeoutInterval.setStatus(_A)
class _EnableCommunicationWatchdogTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableCommunicationWatchdogTimeout_Type.__name__=_C
_EnableCommunicationWatchdogTimeout_Object=MibScalar
enableCommunicationWatchdogTimeout=_EnableCommunicationWatchdogTimeout_Object((1,3,6,1,4,1,8691,2,21,1,2,1,5),_EnableCommunicationWatchdogTimeout_Type())
enableCommunicationWatchdogTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:enableCommunicationWatchdogTimeout.setStatus(_A)
class _CommunicationWatchdogTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CommunicationWatchdogTimeout_Type.__name__=_C
_CommunicationWatchdogTimeout_Object=MibScalar
communicationWatchdogTimeout=_CommunicationWatchdogTimeout_Object((1,3,6,1,4,1,8691,2,21,1,2,1,6),_CommunicationWatchdogTimeout_Type())
communicationWatchdogTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:communicationWatchdogTimeout.setStatus(_A)
_TimeSetting_ObjectIdentity=ObjectIdentity
timeSetting=_TimeSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,2,2))
class _TimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63)));namedValues=NamedValues(*(('gmt-1200_Eniwetok-Kwajalein',0),('gmt-1100_Midway-Island-Samoa',1),('gmt-1000_Hawaii',2),('gmt-0900_Alaska',3),('gmt-0800_Pacific-Time-US_Canada-Tijuana',4),('gmt-0700_Arizona',5),('gmt-0700_Mountain-Time-US_Canada',6),('gmt-0600_Central-Time-US_Canada',7),('gmt-0600_Mexico-City-Tegucigalpa',8),('gmt-0600_Saskatchewan',9),('gmt-0500_Bogota-Lima-Quito',10),('gmt-0500_Eastern-Time-US_Canada',11),('gmt-0500_Indiana-East',12),('gmt-0430_Caracas',13),('gmt-0400_Atlantic-Time-Canada',14),('gmt-0400_Georgetown-La-Paz',15),('gmt-0400_Santiago',16),('gmt-0330_Newfoundland',17),('gmt-0300_Brasilia',18),('gmt-0300_Buenos-Aires',19),('gmt-0200_Mid-Atlantic',20),('gmt-0100_Azores-Cape-Verde-Is',21),('gmt_Casabanca-Monrovia',22),('gmt_Greenich-Mean-Time_Dublin-Edinburgh-Lisbon-London',23),('gmt_0100_Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna',24),('gmt_0100_Belgrade-Bratislava-Budapest-Ljubljana-Prague',25),('gmt_0100_Brussels-Copenhagen-Madrid-Paris-Vilnius',26),('gmt_0100_Sarajevo-Skopje-Warsaw-Zagreb',27),('gmt_0200_Athens-Istanbul-Minsk',28),('gmt_0200_Bucharest',29),('gmt_0200_Cairo',30),('gmt_0200_Harare-Pretoria',31),('gmt_0200_Helsinki-Riga-Sofia-Tallinn',32),('gmt_0200_Jerusalem',33),('gmt_0300_Baghdad-Kuwait-Riyadh',34),('gmt_0300_Moscow-St-Petersburg-Volgograd',35),('gmt_0300_Mairobi',36),('gmt_0330_Tehran',37),('gmt_0400_Abu-Dhabi-Muscat',38),('gmt_0400_Baku-Tbilisi',39),('gmt_0430_Kabul',40),('gmt_0500_Ekaterinburg',41),('gmt_0500_Islamabad-Karachi-Tashkent',42),('gmt_0530_Bombay-Calcutta-Madras-New-Delhi',43),('gmt_0600_Astana-Almaty-Dhaka',44),('gmt_0600_Colombo',45),('gmt_0700_Bangkok-Hanoi-Jakarta',46),('gmt_0800_Beijing-Chongqing-Hong-Kong-Urumqi',47),('gmt_0800_Perth',48),('gmt_0800_Singapore',49),('gmt_0800_Taipei',50),('gmt_0900_Osaka-Sapporo-Tokyo',51),('gmt_0900_Seoul',52),('gmt_0900_Yakutsk',53),('gmt_0930_Adelaide',54),('gmt_0930_Darwin',55),('gmt_1000_Brisbane',56),('gmt_1000_Canberra-Melbourne-Sydney',57),('gmt_1000_Guam-Port-Moresby',58),('gmt_1000_Hobart',59),('gmt_1000_Vladivostok',60),('gmt_1100_Magadan-Solomon-Is-New-Caledonia',61),('gmt_1200_Auckland-Wllington',62),('gmt_1200_Fiji-Kamchatka-Marshall-Is',63)))
_TimeZone_Type.__name__=_C
_TimeZone_Object=MibScalar
timeZone=_TimeZone_Object((1,3,6,1,4,1,8691,2,21,1,2,2,1),_TimeZone_Type())
timeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:timeZone.setStatus(_A)
class _LocalTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_LocalTime_Type.__name__=_I
_LocalTime_Object=MibScalar
localTime=_LocalTime_Object((1,3,6,1,4,1,8691,2,21,1,2,2,2),_LocalTime_Type())
localTime.setMaxAccess(_B)
if mibBuilder.loadTexts:localTime.setStatus(_A)
_TimeServer_Type=DisplayString
_TimeServer_Object=MibScalar
timeServer=_TimeServer_Object((1,3,6,1,4,1,8691,2,21,1,2,2,3),_TimeServer_Type())
timeServer.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer.setStatus(_A)
_NetworkSetting_ObjectIdentity=ObjectIdentity
networkSetting=_NetworkSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3))
_GeneralSetting_ObjectIdentity=ObjectIdentity
generalSetting=_GeneralSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,1))
_DnsServer1IpAddr_Type=IpAddress
_DnsServer1IpAddr_Object=MibScalar
dnsServer1IpAddr=_DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,2,21,1,3,1,1),_DnsServer1IpAddr_Type())
dnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer1IpAddr.setStatus(_A)
_DnsServer2IpAddr_Type=IpAddress
_DnsServer2IpAddr_Object=MibScalar
dnsServer2IpAddr=_DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,2,21,1,3,1,2),_DnsServer2IpAddr_Type())
dnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer2IpAddr.setStatus(_A)
_EthernetSetting_ObjectIdentity=ObjectIdentity
ethernetSetting=_EthernetSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,2))
class _EthIpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Y,0),(_Z,1),(_a,2)))
_EthIpConfiguration_Type.__name__=_C
_EthIpConfiguration_Object=MibScalar
ethIpConfiguration=_EthIpConfiguration_Object((1,3,6,1,4,1,8691,2,21,1,3,2,1),_EthIpConfiguration_Type())
ethIpConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIpConfiguration.setStatus(_A)
_EthIpAddress_Type=IpAddress
_EthIpAddress_Object=MibScalar
ethIpAddress=_EthIpAddress_Object((1,3,6,1,4,1,8691,2,21,1,3,2,2),_EthIpAddress_Type())
ethIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIpAddress.setStatus(_A)
_EthNetMask_Type=IpAddress
_EthNetMask_Object=MibScalar
ethNetMask=_EthNetMask_Object((1,3,6,1,4,1,8691,2,21,1,3,2,3),_EthNetMask_Type())
ethNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ethNetMask.setStatus(_A)
_EthDefaultGateway_Type=IpAddress
_EthDefaultGateway_Object=MibScalar
ethDefaultGateway=_EthDefaultGateway_Object((1,3,6,1,4,1,8691,2,21,1,3,2,4),_EthDefaultGateway_Type())
ethDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDefaultGateway.setStatus(_A)
class _EthBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EthBridgeMode_Type.__name__=_C
_EthBridgeMode_Object=MibScalar
ethBridgeMode=_EthBridgeMode_Object((1,3,6,1,4,1,8691,2,21,1,3,2,5),_EthBridgeMode_Type())
ethBridgeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBridgeMode.setStatus(_A)
_WlanSetting_ObjectIdentity=ObjectIdentity
wlanSetting=_WlanSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,3))
class _WlanIpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Y,0),(_Z,1),(_a,2)))
_WlanIpConfiguration_Type.__name__=_C
_WlanIpConfiguration_Object=MibScalar
wlanIpConfiguration=_WlanIpConfiguration_Object((1,3,6,1,4,1,8691,2,21,1,3,3,1),_WlanIpConfiguration_Type())
wlanIpConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIpConfiguration.setStatus(_A)
_WlanIpAddress_Type=IpAddress
_WlanIpAddress_Object=MibScalar
wlanIpAddress=_WlanIpAddress_Object((1,3,6,1,4,1,8691,2,21,1,3,3,2),_WlanIpAddress_Type())
wlanIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIpAddress.setStatus(_A)
_WlanNetMask_Type=IpAddress
_WlanNetMask_Object=MibScalar
wlanNetMask=_WlanNetMask_Object((1,3,6,1,4,1,8691,2,21,1,3,3,3),_WlanNetMask_Type())
wlanNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanNetMask.setStatus(_A)
_WlanDefaultGateway_Type=IpAddress
_WlanDefaultGateway_Object=MibScalar
wlanDefaultGateway=_WlanDefaultGateway_Object((1,3,6,1,4,1,8691,2,21,1,3,3,4),_WlanDefaultGateway_Type())
wlanDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanDefaultGateway.setStatus(_A)
_ProfileSetting_ObjectIdentity=ObjectIdentity
profileSetting=_ProfileSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4))
class _NetworkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ad-hoc',0),('infrastructure',1)))
_NetworkType_Type.__name__=_C
_NetworkType_Object=MibScalar
networkType=_NetworkType_Object((1,3,6,1,4,1,8691,2,21,1,3,4,1),_NetworkType_Type())
networkType.setMaxAccess(_B)
if mibBuilder.loadTexts:networkType.setStatus(_A)
_AdhocProfile_ObjectIdentity=ObjectIdentity
adhocProfile=_AdhocProfile_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4,2))
_AdhocGeneralSetting_ObjectIdentity=ObjectIdentity
adhocGeneralSetting=_AdhocGeneralSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4,2,1))
class _AdhocProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdhocProfileName_Type.__name__=_I
_AdhocProfileName_Object=MibScalar
adhocProfileName=_AdhocProfileName_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,1,1),_AdhocProfileName_Type())
adhocProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocProfileName.setStatus(_A)
class _AdhocRFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_AH,2))
_AdhocRFType_Type.__name__=_C
_AdhocRFType_Object=MibScalar
adhocRFType=_AdhocRFType_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,1,2),_AdhocRFType_Type())
adhocRFType.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocRFType.setStatus(_A)
class _AdhocWlanSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdhocWlanSSID_Type.__name__=_I
_AdhocWlanSSID_Object=MibScalar
adhocWlanSSID=_AdhocWlanSSID_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,1,3),_AdhocWlanSSID_Type())
adhocWlanSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWlanSSID.setStatus(_A)
_AdhocChannel_Type=Integer32
_AdhocChannel_Object=MibScalar
adhocChannel=_AdhocChannel_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,1,4),_AdhocChannel_Type())
adhocChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocChannel.setStatus(_A)
_AdhocSecuritySetting_ObjectIdentity=ObjectIdentity
adhocSecuritySetting=_AdhocSecuritySetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4,2,2))
class _AdhocAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_AI,0))
_AdhocAuthentication_Type.__name__=_C
_AdhocAuthentication_Object=MibScalar
adhocAuthentication=_AdhocAuthentication_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,2,1),_AdhocAuthentication_Type())
adhocAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:adhocAuthentication.setStatus(_A)
class _AdhocEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('wep',1)))
_AdhocEncryption_Type.__name__=_C
_AdhocEncryption_Object=MibScalar
adhocEncryption=_AdhocEncryption_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,2,2),_AdhocEncryption_Type())
adhocEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocEncryption.setStatus(_A)
class _AdhocWepKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AJ,0),(_AK,1)))
_AdhocWepKeyLength_Type.__name__=_C
_AdhocWepKeyLength_Object=MibScalar
adhocWepKeyLength=_AdhocWepKeyLength_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,2,3),_AdhocWepKeyLength_Type())
adhocWepKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyLength.setStatus(_A)
class _AdhocWepKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AdhocWepKeyIndex_Type.__name__=_C
_AdhocWepKeyIndex_Object=MibScalar
adhocWepKeyIndex=_AdhocWepKeyIndex_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,2,4),_AdhocWepKeyIndex_Type())
adhocWepKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyIndex.setStatus(_A)
class _AdhocWepKeyPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_AdhocWepKeyPassphrase_Type.__name__=_I
_AdhocWepKeyPassphrase_Object=MibScalar
adhocWepKeyPassphrase=_AdhocWepKeyPassphrase_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,2,5),_AdhocWepKeyPassphrase_Type())
adhocWepKeyPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyPassphrase.setStatus(_A)
class _AdhocWepKeyFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascii',0),('hex',1)))
_AdhocWepKeyFormat_Type.__name__=_C
_AdhocWepKeyFormat_Object=MibScalar
adhocWepKeyFormat=_AdhocWepKeyFormat_Object((1,3,6,1,4,1,8691,2,21,1,3,4,2,2,6),_AdhocWepKeyFormat_Type())
adhocWepKeyFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adhocWepKeyFormat.setStatus(_A)
_InfrastructureProfile_ObjectIdentity=ObjectIdentity
infrastructureProfile=_InfrastructureProfile_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4,3))
_InfraGeneralSetting_ObjectIdentity=ObjectIdentity
infraGeneralSetting=_InfraGeneralSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4,3,1))
_InfraGeneralSettingTable_Object=MibTable
infraGeneralSettingTable=_InfraGeneralSettingTable_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,1,1))
if mibBuilder.loadTexts:infraGeneralSettingTable.setStatus(_A)
_InfraGeneralSettingEntry_Object=MibTableRow
infraGeneralSettingEntry=_InfraGeneralSettingEntry_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,1,1,1))
infraGeneralSettingEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:infraGeneralSettingEntry.setStatus(_A)
class _ProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('profile1',1))
_ProfileIndex_Type.__name__=_C
_ProfileIndex_Object=MibTableColumn
profileIndex=_ProfileIndex_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,1,1,1,1),_ProfileIndex_Type())
profileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:profileIndex.setStatus(_A)
class _ProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProfileName_Type.__name__=_I
_ProfileName_Object=MibTableColumn
profileName=_ProfileName_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,1,1,1,2),_ProfileName_Type())
profileName.setMaxAccess(_B)
if mibBuilder.loadTexts:profileName.setStatus(_A)
class _ProfileRFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('auto',0),('w802_11a',1),(_AH,2),('w802_11a_n',3),('w802_11b_g_n',4)))
_ProfileRFType_Type.__name__=_C
_ProfileRFType_Object=MibTableColumn
profileRFType=_ProfileRFType_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,1,1,1,3),_ProfileRFType_Type())
profileRFType.setMaxAccess(_B)
if mibBuilder.loadTexts:profileRFType.setStatus(_A)
class _ProfileWlanSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProfileWlanSSID_Type.__name__=_I
_ProfileWlanSSID_Object=MibTableColumn
profileWlanSSID=_ProfileWlanSSID_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,1,1,1,4),_ProfileWlanSSID_Type())
profileWlanSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:profileWlanSSID.setStatus(_A)
_SecuritySetting_ObjectIdentity=ObjectIdentity
securitySetting=_SecuritySetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,4,3,2))
_SecuritySettingTable_Object=MibTable
securitySettingTable=_SecuritySettingTable_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1))
if mibBuilder.loadTexts:securitySettingTable.setStatus(_A)
_SecuritySettingEntry_Object=MibTableRow
securitySettingEntry=_SecuritySettingEntry_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1))
securitySettingEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:securitySettingEntry.setStatus(_A)
class _Authentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AI,0),('shared-key',1),('wpa',2),('wpa-psk',3),('wpa2',4),('wpa2-psk',5)))
_Authentication_Type.__name__=_C
_Authentication_Object=MibTableColumn
authentication=_Authentication_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,1),_Authentication_Type())
authentication.setMaxAccess(_B)
if mibBuilder.loadTexts:authentication.setStatus(_A)
class _Encryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('wep',1),('tkip',2),('aes-ccmp',3)))
_Encryption_Type.__name__=_C
_Encryption_Object=MibTableColumn
encryption=_Encryption_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,2),_Encryption_Type())
encryption.setMaxAccess(_B)
if mibBuilder.loadTexts:encryption.setStatus(_A)
class _WepKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AJ,0),(_AK,1)))
_WepKeyLength_Type.__name__=_C
_WepKeyLength_Object=MibTableColumn
wepKeyLength=_WepKeyLength_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,3),_WepKeyLength_Type())
wepKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyLength.setStatus(_A)
class _WepKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WepKeyIndex_Type.__name__=_C
_WepKeyIndex_Object=MibTableColumn
wepKeyIndex=_WepKeyIndex_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,4),_WepKeyIndex_Type())
wepKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyIndex.setStatus(_A)
class _WepKeyPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_WepKeyPassphrase_Type.__name__=_I
_WepKeyPassphrase_Object=MibTableColumn
wepKeyPassphrase=_WepKeyPassphrase_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,5),_WepKeyPassphrase_Type())
wepKeyPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyPassphrase.setStatus(_A)
class _WepKeyFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascii',0),('hex',1)))
_WepKeyFormat_Type.__name__=_C
_WepKeyFormat_Object=MibTableColumn
wepKeyFormat=_WepKeyFormat_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,6),_WepKeyFormat_Type())
wepKeyFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyFormat.setStatus(_A)
class _EapMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('tls',0),('peap',1),('ttls',2),('leap',3)))
_EapMethod_Type.__name__=_C
_EapMethod_Object=MibTableColumn
eapMethod=_EapMethod_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,12),_EapMethod_Type())
eapMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:eapMethod.setStatus(_A)
class _TunneledAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('gtc',0),('md5',1),('pap',2),('chap',3),('mschap',4),('mschapv2',5),('tls',6),('eap-tls',7),('eap-mschapv2',8),('eap-gtc',9),('eap-md5',10)))
_TunneledAuth_Type.__name__=_C
_TunneledAuth_Object=MibTableColumn
tunneledAuth=_TunneledAuth_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,13),_TunneledAuth_Type())
tunneledAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:tunneledAuth.setStatus(_A)
class _WpaUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_WpaUsername_Type.__name__=_I
_WpaUsername_Object=MibTableColumn
wpaUsername=_WpaUsername_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,14),_WpaUsername_Type())
wpaUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:wpaUsername.setStatus(_A)
class _WpaAnonymousUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_WpaAnonymousUsername_Type.__name__=_I
_WpaAnonymousUsername_Object=MibTableColumn
wpaAnonymousUsername=_WpaAnonymousUsername_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,16),_WpaAnonymousUsername_Type())
wpaAnonymousUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:wpaAnonymousUsername.setStatus(_A)
class _VerifyServerCert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VerifyServerCert_Type.__name__=_C
_VerifyServerCert_Object=MibTableColumn
verifyServerCert=_VerifyServerCert_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,17),_VerifyServerCert_Type())
verifyServerCert.setMaxAccess(_B)
if mibBuilder.loadTexts:verifyServerCert.setStatus(_A)
class _TrustedServerCert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_TrustedServerCert_Type.__name__=_C
_TrustedServerCert_Object=MibTableColumn
trustedServerCert=_TrustedServerCert_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,18),_TrustedServerCert_Type())
trustedServerCert.setMaxAccess(_D)
if mibBuilder.loadTexts:trustedServerCert.setStatus(_A)
class _UserCert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_UserCert_Type.__name__=_C
_UserCert_Object=MibTableColumn
userCert=_UserCert_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,19),_UserCert_Type())
userCert.setMaxAccess(_D)
if mibBuilder.loadTexts:userCert.setStatus(_A)
class _UserPrivateKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_UserPrivateKey_Type.__name__=_C
_UserPrivateKey_Object=MibTableColumn
userPrivateKey=_UserPrivateKey_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,2,1,1,20),_UserPrivateKey_Type())
userPrivateKey.setMaxAccess(_D)
if mibBuilder.loadTexts:userPrivateKey.setStatus(_A)
class _FastRoamingSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FastRoamingSetting_Type.__name__=_C
_FastRoamingSetting_Object=MibScalar
fastRoamingSetting=_FastRoamingSetting_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,3),_FastRoamingSetting_Type())
fastRoamingSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingSetting.setStatus(_A)
class _FastRoamingScanChannels1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_m,8),(_n,9),(_o,10),(_p,11),(_q,12),(_r,13),(_s,15),(_t,16),(_u,17),(_v,18),(_w,19),(_x,20),(_y,21),(_z,22),(_A0,23),(_A1,24),(_A2,25),(_A3,26),(_A4,27),(_A5,28),(_A6,29),(_A7,30),(_A8,31),(_A9,32),(_AA,33),(_AB,34),(_AC,35),(_AD,36),(_AE,37),(_AF,38)))
_FastRoamingScanChannels1_Type.__name__=_C
_FastRoamingScanChannels1_Object=MibScalar
fastRoamingScanChannels1=_FastRoamingScanChannels1_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,4),_FastRoamingScanChannels1_Type())
fastRoamingScanChannels1.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingScanChannels1.setStatus(_A)
class _FastRoamingScanChannels2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_m,8),(_n,9),(_o,10),(_p,11),(_q,12),(_r,13),(_s,15),(_t,16),(_u,17),(_v,18),(_w,19),(_x,20),(_y,21),(_z,22),(_A0,23),(_A1,24),(_A2,25),(_A3,26),(_A4,27),(_A5,28),(_A6,29),(_A7,30),(_A8,31),(_A9,32),(_AA,33),(_AB,34),(_AC,35),(_AD,36),(_AE,37),(_AF,38)))
_FastRoamingScanChannels2_Type.__name__=_C
_FastRoamingScanChannels2_Object=MibScalar
fastRoamingScanChannels2=_FastRoamingScanChannels2_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,5),_FastRoamingScanChannels2_Type())
fastRoamingScanChannels2.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingScanChannels2.setStatus(_A)
class _FastRoamingScanChannels3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_m,8),(_n,9),(_o,10),(_p,11),(_q,12),(_r,13),(_s,15),(_t,16),(_u,17),(_v,18),(_w,19),(_x,20),(_y,21),(_z,22),(_A0,23),(_A1,24),(_A2,25),(_A3,26),(_A4,27),(_A5,28),(_A6,29),(_A7,30),(_A8,31),(_A9,32),(_AA,33),(_AB,34),(_AC,35),(_AD,36),(_AE,37),(_AF,38)))
_FastRoamingScanChannels3_Type.__name__=_C
_FastRoamingScanChannels3_Object=MibScalar
fastRoamingScanChannels3=_FastRoamingScanChannels3_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,6),_FastRoamingScanChannels3_Type())
fastRoamingScanChannels3.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingScanChannels3.setStatus(_A)
class _FastRoamingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-70,-40))
_FastRoamingThreshold_Type.__name__=_C
_FastRoamingThreshold_Object=MibScalar
fastRoamingThreshold=_FastRoamingThreshold_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,7),_FastRoamingThreshold_Type())
fastRoamingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingThreshold.setStatus(_A)
class _FastRoamingDifference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_FastRoamingDifference_Type.__name__=_C
_FastRoamingDifference_Object=MibScalar
fastRoamingDifference=_FastRoamingDifference_Object((1,3,6,1,4,1,8691,2,21,1,3,4,3,8),_FastRoamingDifference_Type())
fastRoamingDifference.setMaxAccess(_B)
if mibBuilder.loadTexts:fastRoamingDifference.setStatus(_A)
_WlanLogSetting_ObjectIdentity=ObjectIdentity
wlanLogSetting=_WlanLogSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,5))
class _WlanLogEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WlanLogEnable_Type.__name__=_C
_WlanLogEnable_Object=MibScalar
wlanLogEnable=_WlanLogEnable_Object((1,3,6,1,4,1,8691,2,21,1,3,5,1),_WlanLogEnable_Type())
wlanLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanLogEnable.setStatus(_A)
_AdvancedSetting_ObjectIdentity=ObjectIdentity
advancedSetting=_AdvancedSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,3,6))
class _GratuitousArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_GratuitousArp_Type.__name__=_C
_GratuitousArp_Object=MibScalar
gratuitousArp=_GratuitousArp_Object((1,3,6,1,4,1,8691,2,21,1,3,6,1),_GratuitousArp_Type())
gratuitousArp.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArp.setStatus(_A)
class _GratuitousArpSendPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_GratuitousArpSendPeriod_Type.__name__=_C
_GratuitousArpSendPeriod_Object=MibScalar
gratuitousArpSendPeriod=_GratuitousArpSendPeriod_Object((1,3,6,1,4,1,8691,2,21,1,3,6,2),_GratuitousArpSendPeriod_Type())
gratuitousArpSendPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpSendPeriod.setStatus(_A)
_GratuitousArpIpAddress1_Type=DisplayString
_GratuitousArpIpAddress1_Object=MibScalar
gratuitousArpIpAddress1=_GratuitousArpIpAddress1_Object((1,3,6,1,4,1,8691,2,21,1,3,6,3),_GratuitousArpIpAddress1_Type())
gratuitousArpIpAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress1.setStatus(_A)
_GratuitousArpMacAddress1_Type=DisplayString
_GratuitousArpMacAddress1_Object=MibScalar
gratuitousArpMacAddress1=_GratuitousArpMacAddress1_Object((1,3,6,1,4,1,8691,2,21,1,3,6,4),_GratuitousArpMacAddress1_Type())
gratuitousArpMacAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress1.setStatus(_A)
_GratuitousArpIpAddress2_Type=DisplayString
_GratuitousArpIpAddress2_Object=MibScalar
gratuitousArpIpAddress2=_GratuitousArpIpAddress2_Object((1,3,6,1,4,1,8691,2,21,1,3,6,5),_GratuitousArpIpAddress2_Type())
gratuitousArpIpAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress2.setStatus(_A)
_GratuitousArpMacAddress2_Type=DisplayString
_GratuitousArpMacAddress2_Object=MibScalar
gratuitousArpMacAddress2=_GratuitousArpMacAddress2_Object((1,3,6,1,4,1,8691,2,21,1,3,6,6),_GratuitousArpMacAddress2_Type())
gratuitousArpMacAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress2.setStatus(_A)
_GratuitousArpIpAddress3_Type=DisplayString
_GratuitousArpIpAddress3_Object=MibScalar
gratuitousArpIpAddress3=_GratuitousArpIpAddress3_Object((1,3,6,1,4,1,8691,2,21,1,3,6,7),_GratuitousArpIpAddress3_Type())
gratuitousArpIpAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress3.setStatus(_A)
_GratuitousArpMacAddress3_Type=DisplayString
_GratuitousArpMacAddress3_Object=MibScalar
gratuitousArpMacAddress3=_GratuitousArpMacAddress3_Object((1,3,6,1,4,1,8691,2,21,1,3,6,8),_GratuitousArpMacAddress3_Type())
gratuitousArpMacAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress3.setStatus(_A)
_GratuitousArpIpAddress4_Type=DisplayString
_GratuitousArpIpAddress4_Object=MibScalar
gratuitousArpIpAddress4=_GratuitousArpIpAddress4_Object((1,3,6,1,4,1,8691,2,21,1,3,6,9),_GratuitousArpIpAddress4_Type())
gratuitousArpIpAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpIpAddress4.setStatus(_A)
_GratuitousArpMacAddress4_Type=DisplayString
_GratuitousArpMacAddress4_Object=MibScalar
gratuitousArpMacAddress4=_GratuitousArpMacAddress4_Object((1,3,6,1,4,1,8691,2,21,1,3,6,10),_GratuitousArpMacAddress4_Type())
gratuitousArpMacAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpMacAddress4.setStatus(_A)
_PortSetting_ObjectIdentity=ObjectIdentity
portSetting=_PortSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4))
_OpModeSetting_ObjectIdentity=ObjectIdentity
opModeSetting=_OpModeSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1))
_OpMode_ObjectIdentity=ObjectIdentity
opMode=_OpMode_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,1))
_OpModePortTable_Object=MibTable
opModePortTable=_OpModePortTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,1,1))
if mibBuilder.loadTexts:opModePortTable.setStatus(_A)
_OpModePortEntry_Object=MibTableRow
opModePortEntry=_OpModePortEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,1,1,1))
opModePortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:opModePortEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PortIndex_Type.__name__=_C
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,8691,2,21,1,4,1,1,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,7,10,12,13,14,20,21)));namedValues=NamedValues(*(('pair-connection-slave',0),('pair-connection-master',1),('real-Com',2),(_E,7),('tcp-Server',10),('ethernet-modem',12),('tcp-Client',13),('udp',14),('rfc-2217',20),('reverse-Terminal',21)))
_PortMode_Type.__name__=_C
_PortMode_Object=MibTableColumn
portMode=_PortMode_Object((1,3,6,1,4,1,8691,2,21,1,4,1,1,1,1,2),_PortMode_Type())
portMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portMode.setStatus(_A)
_OpModeParam_ObjectIdentity=ObjectIdentity
opModeParam=_OpModeParam_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2))
_RealCOM_ObjectIdentity=ObjectIdentity
realCOM=_RealCOM_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,1))
_RealCOMTable_Object=MibTable
realCOMTable=_RealCOMTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1))
if mibBuilder.loadTexts:realCOMTable.setStatus(_A)
_RealCOMEntry_Object=MibTableRow
realCOMEntry=_RealCOMEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1))
realCOMEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:realCOMEntry.setStatus(_A)
_RealCOMTcpAliveCheck_Type=Integer32
_RealCOMTcpAliveCheck_Object=MibTableColumn
realCOMTcpAliveCheck=_RealCOMTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1,1),_RealCOMTcpAliveCheck_Type())
realCOMTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMTcpAliveCheck.setStatus(_A)
_RealCOMMaxConnection_Type=Integer32
_RealCOMMaxConnection_Object=MibTableColumn
realCOMMaxConnection=_RealCOMMaxConnection_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1,2),_RealCOMMaxConnection_Type())
realCOMMaxConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMMaxConnection.setStatus(_A)
class _RealCOMIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RealCOMIgnoreJammedIp_Type.__name__=_C
_RealCOMIgnoreJammedIp_Object=MibTableColumn
realCOMIgnoreJammedIp=_RealCOMIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1,3),_RealCOMIgnoreJammedIp_Type())
realCOMIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMIgnoreJammedIp.setStatus(_A)
class _RealCOMAllowDriverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RealCOMAllowDriverControl_Type.__name__=_C
_RealCOMAllowDriverControl_Object=MibTableColumn
realCOMAllowDriverControl=_RealCOMAllowDriverControl_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1,4),_RealCOMAllowDriverControl_Type())
realCOMAllowDriverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMAllowDriverControl.setStatus(_A)
class _RealCOMConnectionDownRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_RealCOMConnectionDownRTS_Type.__name__=_C
_RealCOMConnectionDownRTS_Object=MibTableColumn
realCOMConnectionDownRTS=_RealCOMConnectionDownRTS_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1,5),_RealCOMConnectionDownRTS_Type())
realCOMConnectionDownRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMConnectionDownRTS.setStatus(_A)
class _RealCOMConnectionDownDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_RealCOMConnectionDownDTR_Type.__name__=_C
_RealCOMConnectionDownDTR_Object=MibTableColumn
realCOMConnectionDownDTR=_RealCOMConnectionDownDTR_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,1,1,1,6),_RealCOMConnectionDownDTR_Type())
realCOMConnectionDownDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:realCOMConnectionDownDTR.setStatus(_A)
_Rfc2217_ObjectIdentity=ObjectIdentity
rfc2217=_Rfc2217_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,2))
_Rfc2217Table_Object=MibTable
rfc2217Table=_Rfc2217Table_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,2,1))
if mibBuilder.loadTexts:rfc2217Table.setStatus(_A)
_Rfc2217Entry_Object=MibTableRow
rfc2217Entry=_Rfc2217Entry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,2,1,1))
rfc2217Entry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rfc2217Entry.setStatus(_A)
_Rfc2217TcpAliveCheck_Type=Integer32
_Rfc2217TcpAliveCheck_Object=MibTableColumn
rfc2217TcpAliveCheck=_Rfc2217TcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,2,1,1,1),_Rfc2217TcpAliveCheck_Type())
rfc2217TcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:rfc2217TcpAliveCheck.setStatus(_A)
_Rfc2217TcpPort_Type=Integer32
_Rfc2217TcpPort_Object=MibTableColumn
rfc2217TcpPort=_Rfc2217TcpPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,2,1,1,2),_Rfc2217TcpPort_Type())
rfc2217TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rfc2217TcpPort.setStatus(_A)
_TcpServer_ObjectIdentity=ObjectIdentity
tcpServer=_TcpServer_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,3))
_TcpServerTable_Object=MibTable
tcpServerTable=_TcpServerTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1))
if mibBuilder.loadTexts:tcpServerTable.setStatus(_A)
_TcpServerEntry_Object=MibTableRow
tcpServerEntry=_TcpServerEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1))
tcpServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tcpServerEntry.setStatus(_A)
_TcpServerTcpAliveCheck_Type=Integer32
_TcpServerTcpAliveCheck_Object=MibTableColumn
tcpServerTcpAliveCheck=_TcpServerTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,1),_TcpServerTcpAliveCheck_Type())
tcpServerTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerTcpAliveCheck.setStatus(_A)
_TcpServerInactivityTime_Type=Integer32
_TcpServerInactivityTime_Object=MibTableColumn
tcpServerInactivityTime=_TcpServerInactivityTime_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,2),_TcpServerInactivityTime_Type())
tcpServerInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerInactivityTime.setStatus(_A)
_TcpServerMaxConnection_Type=Integer32
_TcpServerMaxConnection_Object=MibTableColumn
tcpServerMaxConnection=_TcpServerMaxConnection_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,3),_TcpServerMaxConnection_Type())
tcpServerMaxConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerMaxConnection.setStatus(_A)
class _TcpServerIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcpServerIgnoreJammedIp_Type.__name__=_C
_TcpServerIgnoreJammedIp_Object=MibTableColumn
tcpServerIgnoreJammedIp=_TcpServerIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,4),_TcpServerIgnoreJammedIp_Type())
tcpServerIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerIgnoreJammedIp.setStatus(_A)
class _TcpServerAllowDriverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcpServerAllowDriverControl_Type.__name__=_C
_TcpServerAllowDriverControl_Object=MibTableColumn
tcpServerAllowDriverControl=_TcpServerAllowDriverControl_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,5),_TcpServerAllowDriverControl_Type())
tcpServerAllowDriverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerAllowDriverControl.setStatus(_A)
_TcpServerTcpPort_Type=Integer32
_TcpServerTcpPort_Object=MibTableColumn
tcpServerTcpPort=_TcpServerTcpPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,6),_TcpServerTcpPort_Type())
tcpServerTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerTcpPort.setStatus(_A)
_TcpServerCmdPort_Type=Integer32
_TcpServerCmdPort_Object=MibTableColumn
tcpServerCmdPort=_TcpServerCmdPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,7),_TcpServerCmdPort_Type())
tcpServerCmdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerCmdPort.setStatus(_A)
class _TcpServerConnectionDownRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_TcpServerConnectionDownRTS_Type.__name__=_C
_TcpServerConnectionDownRTS_Object=MibTableColumn
tcpServerConnectionDownRTS=_TcpServerConnectionDownRTS_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,8),_TcpServerConnectionDownRTS_Type())
tcpServerConnectionDownRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerConnectionDownRTS.setStatus(_A)
class _TcpServerConnectionDownDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_TcpServerConnectionDownDTR_Type.__name__=_C
_TcpServerConnectionDownDTR_Object=MibTableColumn
tcpServerConnectionDownDTR=_TcpServerConnectionDownDTR_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,3,1,1,9),_TcpServerConnectionDownDTR_Type())
tcpServerConnectionDownDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpServerConnectionDownDTR.setStatus(_A)
_TcpClient_ObjectIdentity=ObjectIdentity
tcpClient=_TcpClient_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,4))
_TcpClientTable_Object=MibTable
tcpClientTable=_TcpClientTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1))
if mibBuilder.loadTexts:tcpClientTable.setStatus(_A)
_TcpClientEntry_Object=MibTableRow
tcpClientEntry=_TcpClientEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1))
tcpClientEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tcpClientEntry.setStatus(_A)
_TcpClientTcpAliveCheck_Type=Integer32
_TcpClientTcpAliveCheck_Object=MibTableColumn
tcpClientTcpAliveCheck=_TcpClientTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,1),_TcpClientTcpAliveCheck_Type())
tcpClientTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientTcpAliveCheck.setStatus(_A)
_TcpClientInactivityTime_Type=Integer32
_TcpClientInactivityTime_Object=MibTableColumn
tcpClientInactivityTime=_TcpClientInactivityTime_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,2),_TcpClientInactivityTime_Type())
tcpClientInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientInactivityTime.setStatus(_A)
class _TcpClientIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TcpClientIgnoreJammedIp_Type.__name__=_C
_TcpClientIgnoreJammedIp_Object=MibTableColumn
tcpClientIgnoreJammedIp=_TcpClientIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,3),_TcpClientIgnoreJammedIp_Type())
tcpClientIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientIgnoreJammedIp.setStatus(_A)
_TcpClientDestinationAddress1_Type=DisplayString
_TcpClientDestinationAddress1_Object=MibTableColumn
tcpClientDestinationAddress1=_TcpClientDestinationAddress1_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,4),_TcpClientDestinationAddress1_Type())
tcpClientDestinationAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress1.setStatus(_A)
_TcpClientDestinationPort1_Type=Integer32
_TcpClientDestinationPort1_Object=MibTableColumn
tcpClientDestinationPort1=_TcpClientDestinationPort1_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,5),_TcpClientDestinationPort1_Type())
tcpClientDestinationPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort1.setStatus(_A)
_TcpClientDestinationAddress2_Type=DisplayString
_TcpClientDestinationAddress2_Object=MibTableColumn
tcpClientDestinationAddress2=_TcpClientDestinationAddress2_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,6),_TcpClientDestinationAddress2_Type())
tcpClientDestinationAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress2.setStatus(_A)
_TcpClientDestinationPort2_Type=Integer32
_TcpClientDestinationPort2_Object=MibTableColumn
tcpClientDestinationPort2=_TcpClientDestinationPort2_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,7),_TcpClientDestinationPort2_Type())
tcpClientDestinationPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort2.setStatus(_A)
_TcpClientDestinationAddress3_Type=DisplayString
_TcpClientDestinationAddress3_Object=MibTableColumn
tcpClientDestinationAddress3=_TcpClientDestinationAddress3_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,8),_TcpClientDestinationAddress3_Type())
tcpClientDestinationAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress3.setStatus(_A)
_TcpClientDestinationPort3_Type=Integer32
_TcpClientDestinationPort3_Object=MibTableColumn
tcpClientDestinationPort3=_TcpClientDestinationPort3_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,9),_TcpClientDestinationPort3_Type())
tcpClientDestinationPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort3.setStatus(_A)
_TcpClientDestinationAddress4_Type=DisplayString
_TcpClientDestinationAddress4_Object=MibTableColumn
tcpClientDestinationAddress4=_TcpClientDestinationAddress4_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,10),_TcpClientDestinationAddress4_Type())
tcpClientDestinationAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationAddress4.setStatus(_A)
_TcpClientDestinationPort4_Type=Integer32
_TcpClientDestinationPort4_Object=MibTableColumn
tcpClientDestinationPort4=_TcpClientDestinationPort4_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,11),_TcpClientDestinationPort4_Type())
tcpClientDestinationPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDestinationPort4.setStatus(_A)
_TcpClientDesignatedLocalPort1_Type=Integer32
_TcpClientDesignatedLocalPort1_Object=MibTableColumn
tcpClientDesignatedLocalPort1=_TcpClientDesignatedLocalPort1_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,12),_TcpClientDesignatedLocalPort1_Type())
tcpClientDesignatedLocalPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort1.setStatus(_A)
_TcpClientDesignatedLocalPort2_Type=Integer32
_TcpClientDesignatedLocalPort2_Object=MibTableColumn
tcpClientDesignatedLocalPort2=_TcpClientDesignatedLocalPort2_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,13),_TcpClientDesignatedLocalPort2_Type())
tcpClientDesignatedLocalPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort2.setStatus(_A)
_TcpClientDesignatedLocalPort3_Type=Integer32
_TcpClientDesignatedLocalPort3_Object=MibTableColumn
tcpClientDesignatedLocalPort3=_TcpClientDesignatedLocalPort3_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,14),_TcpClientDesignatedLocalPort3_Type())
tcpClientDesignatedLocalPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort3.setStatus(_A)
_TcpClientDesignatedLocalPort4_Type=Integer32
_TcpClientDesignatedLocalPort4_Object=MibTableColumn
tcpClientDesignatedLocalPort4=_TcpClientDesignatedLocalPort4_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,15),_TcpClientDesignatedLocalPort4_Type())
tcpClientDesignatedLocalPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientDesignatedLocalPort4.setStatus(_A)
class _TcpClientConnectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(257,258,260,264,514,1028,2056)));namedValues=NamedValues(*(('startup-None',257),('anyCharacter-None',258),('dsrOn-None',260),('dcdOn-None',264),('anyCharacter-InactivityTime',514),('dsrOn-DSR-Off',1028),('dcdOn-DCD-Off',2056)))
_TcpClientConnectionControl_Type.__name__=_C
_TcpClientConnectionControl_Object=MibTableColumn
tcpClientConnectionControl=_TcpClientConnectionControl_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,4,1,1,16),_TcpClientConnectionControl_Type())
tcpClientConnectionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpClientConnectionControl.setStatus(_A)
_Udp_ObjectIdentity=ObjectIdentity
udp=_Udp_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,5))
_UdpTable_Object=MibTable
udpTable=_UdpTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1))
if mibBuilder.loadTexts:udpTable.setStatus(_A)
_UdpEntry_Object=MibTableRow
udpEntry=_UdpEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1))
udpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:udpEntry.setStatus(_A)
_UdpDestinationAddress1Begin_Type=IpAddress
_UdpDestinationAddress1Begin_Object=MibTableColumn
udpDestinationAddress1Begin=_UdpDestinationAddress1Begin_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,1),_UdpDestinationAddress1Begin_Type())
udpDestinationAddress1Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress1Begin.setStatus(_A)
_UdpDestinationAddress1End_Type=IpAddress
_UdpDestinationAddress1End_Object=MibTableColumn
udpDestinationAddress1End=_UdpDestinationAddress1End_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,2),_UdpDestinationAddress1End_Type())
udpDestinationAddress1End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress1End.setStatus(_A)
_UdpDestinationPort1_Type=Integer32
_UdpDestinationPort1_Object=MibTableColumn
udpDestinationPort1=_UdpDestinationPort1_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,3),_UdpDestinationPort1_Type())
udpDestinationPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort1.setStatus(_A)
_UdpDestinationAddress2Begin_Type=IpAddress
_UdpDestinationAddress2Begin_Object=MibTableColumn
udpDestinationAddress2Begin=_UdpDestinationAddress2Begin_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,4),_UdpDestinationAddress2Begin_Type())
udpDestinationAddress2Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress2Begin.setStatus(_A)
_UdpDestinationAddress2End_Type=IpAddress
_UdpDestinationAddress2End_Object=MibTableColumn
udpDestinationAddress2End=_UdpDestinationAddress2End_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,5),_UdpDestinationAddress2End_Type())
udpDestinationAddress2End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress2End.setStatus(_A)
_UdpDestinationPort2_Type=Integer32
_UdpDestinationPort2_Object=MibTableColumn
udpDestinationPort2=_UdpDestinationPort2_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,6),_UdpDestinationPort2_Type())
udpDestinationPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort2.setStatus(_A)
_UdpDestinationAddress3Begin_Type=IpAddress
_UdpDestinationAddress3Begin_Object=MibTableColumn
udpDestinationAddress3Begin=_UdpDestinationAddress3Begin_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,7),_UdpDestinationAddress3Begin_Type())
udpDestinationAddress3Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress3Begin.setStatus(_A)
_UdpDestinationAddress3End_Type=IpAddress
_UdpDestinationAddress3End_Object=MibTableColumn
udpDestinationAddress3End=_UdpDestinationAddress3End_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,8),_UdpDestinationAddress3End_Type())
udpDestinationAddress3End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress3End.setStatus(_A)
_UdpDestinationPort3_Type=Integer32
_UdpDestinationPort3_Object=MibTableColumn
udpDestinationPort3=_UdpDestinationPort3_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,9),_UdpDestinationPort3_Type())
udpDestinationPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort3.setStatus(_A)
_UdpDestinationAddress4Begin_Type=IpAddress
_UdpDestinationAddress4Begin_Object=MibTableColumn
udpDestinationAddress4Begin=_UdpDestinationAddress4Begin_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,10),_UdpDestinationAddress4Begin_Type())
udpDestinationAddress4Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress4Begin.setStatus(_A)
_UdpDestinationAddress4End_Type=IpAddress
_UdpDestinationAddress4End_Object=MibTableColumn
udpDestinationAddress4End=_UdpDestinationAddress4End_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,11),_UdpDestinationAddress4End_Type())
udpDestinationAddress4End.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationAddress4End.setStatus(_A)
_UdpDestinationPort4_Type=Integer32
_UdpDestinationPort4_Object=MibTableColumn
udpDestinationPort4=_UdpDestinationPort4_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,12),_UdpDestinationPort4_Type())
udpDestinationPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:udpDestinationPort4.setStatus(_A)
_UdpLocalListenPort_Type=Integer32
_UdpLocalListenPort_Object=MibTableColumn
udpLocalListenPort=_UdpLocalListenPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,5,1,1,13),_UdpLocalListenPort_Type())
udpLocalListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:udpLocalListenPort.setStatus(_A)
_PairConnectionMaster_ObjectIdentity=ObjectIdentity
pairConnectionMaster=_PairConnectionMaster_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,6))
_PairConnectionMasterTable_Object=MibTable
pairConnectionMasterTable=_PairConnectionMasterTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,6,1))
if mibBuilder.loadTexts:pairConnectionMasterTable.setStatus(_A)
_PairConnectionMasterEntry_Object=MibTableRow
pairConnectionMasterEntry=_PairConnectionMasterEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,6,1,1))
pairConnectionMasterEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pairConnectionMasterEntry.setStatus(_A)
_PairConnectionMasterTcpAliveCheck_Type=Integer32
_PairConnectionMasterTcpAliveCheck_Object=MibTableColumn
pairConnectionMasterTcpAliveCheck=_PairConnectionMasterTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,6,1,1,1),_PairConnectionMasterTcpAliveCheck_Type())
pairConnectionMasterTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionMasterTcpAliveCheck.setStatus(_A)
_PairConnectionMasterDestnationAddress_Type=DisplayString
_PairConnectionMasterDestnationAddress_Object=MibTableColumn
pairConnectionMasterDestnationAddress=_PairConnectionMasterDestnationAddress_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,6,1,1,2),_PairConnectionMasterDestnationAddress_Type())
pairConnectionMasterDestnationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionMasterDestnationAddress.setStatus(_A)
_PairConnectionMasterDestnationTcpPort_Type=Integer32
_PairConnectionMasterDestnationTcpPort_Object=MibTableColumn
pairConnectionMasterDestnationTcpPort=_PairConnectionMasterDestnationTcpPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,6,1,1,3),_PairConnectionMasterDestnationTcpPort_Type())
pairConnectionMasterDestnationTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionMasterDestnationTcpPort.setStatus(_A)
_PairConnectionSlave_ObjectIdentity=ObjectIdentity
pairConnectionSlave=_PairConnectionSlave_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,7))
_PairConnectionSlaveTable_Object=MibTable
pairConnectionSlaveTable=_PairConnectionSlaveTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,7,1))
if mibBuilder.loadTexts:pairConnectionSlaveTable.setStatus(_A)
_PairConnectionSlaveEntry_Object=MibTableRow
pairConnectionSlaveEntry=_PairConnectionSlaveEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,7,1,1))
pairConnectionSlaveEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pairConnectionSlaveEntry.setStatus(_A)
_PairConnectionSlaveTcpAliveCheck_Type=Integer32
_PairConnectionSlaveTcpAliveCheck_Object=MibTableColumn
pairConnectionSlaveTcpAliveCheck=_PairConnectionSlaveTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,7,1,1,1),_PairConnectionSlaveTcpAliveCheck_Type())
pairConnectionSlaveTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionSlaveTcpAliveCheck.setStatus(_A)
_PairConnectionSlaveLocalTcpPort_Type=Integer32
_PairConnectionSlaveLocalTcpPort_Object=MibTableColumn
pairConnectionSlaveLocalTcpPort=_PairConnectionSlaveLocalTcpPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,7,1,1,2),_PairConnectionSlaveLocalTcpPort_Type())
pairConnectionSlaveLocalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionSlaveLocalTcpPort.setStatus(_A)
_EthernetModem_ObjectIdentity=ObjectIdentity
ethernetModem=_EthernetModem_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,8))
_EthernetModemTable_Object=MibTable
ethernetModemTable=_EthernetModemTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,8,1))
if mibBuilder.loadTexts:ethernetModemTable.setStatus(_A)
_EthernetModemEntry_Object=MibTableRow
ethernetModemEntry=_EthernetModemEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,8,1,1))
ethernetModemEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ethernetModemEntry.setStatus(_A)
_EthernetModemTcpAliveCheck_Type=Integer32
_EthernetModemTcpAliveCheck_Object=MibTableColumn
ethernetModemTcpAliveCheck=_EthernetModemTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,8,1,1,1),_EthernetModemTcpAliveCheck_Type())
ethernetModemTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetModemTcpAliveCheck.setStatus(_A)
_EthernetModemLocalTcpPort_Type=Integer32
_EthernetModemLocalTcpPort_Object=MibTableColumn
ethernetModemLocalTcpPort=_EthernetModemLocalTcpPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,8,1,1,2),_EthernetModemLocalTcpPort_Type())
ethernetModemLocalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetModemLocalTcpPort.setStatus(_A)
_ReverseTerminal_ObjectIdentity=ObjectIdentity
reverseTerminal=_ReverseTerminal_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,2,9))
_ReverseTerminalTable_Object=MibTable
reverseTerminalTable=_ReverseTerminalTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1))
if mibBuilder.loadTexts:reverseTerminalTable.setStatus(_A)
_ReverseTerminalEntry_Object=MibTableRow
reverseTerminalEntry=_ReverseTerminalEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1,1))
reverseTerminalEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:reverseTerminalEntry.setStatus(_A)
_ReverseTerminalTcpAliveCheck_Type=Integer32
_ReverseTerminalTcpAliveCheck_Object=MibTableColumn
reverseTerminalTcpAliveCheck=_ReverseTerminalTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1,1,1),_ReverseTerminalTcpAliveCheck_Type())
reverseTerminalTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTcpAliveCheck.setStatus(_A)
_ReverseTerminalInactivityTime_Type=Integer32
_ReverseTerminalInactivityTime_Object=MibTableColumn
reverseTerminalInactivityTime=_ReverseTerminalInactivityTime_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1,1,2),_ReverseTerminalInactivityTime_Type())
reverseTerminalInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalInactivityTime.setStatus(_A)
_ReverseTerminalTcpPort_Type=Integer32
_ReverseTerminalTcpPort_Object=MibTableColumn
reverseTerminalTcpPort=_ReverseTerminalTcpPort_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1,1,3),_ReverseTerminalTcpPort_Type())
reverseTerminalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTcpPort.setStatus(_A)
class _ReverseTerminalAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),('local',1),('radius',2)))
_ReverseTerminalAuthenticationType_Type.__name__=_C
_ReverseTerminalAuthenticationType_Object=MibTableColumn
reverseTerminalAuthenticationType=_ReverseTerminalAuthenticationType_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1,1,4),_ReverseTerminalAuthenticationType_Type())
reverseTerminalAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalAuthenticationType.setStatus(_A)
class _ReverseTerminalMapKeys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('cr-lf',0),('cr',1),('lf',2)))
_ReverseTerminalMapKeys_Type.__name__=_C
_ReverseTerminalMapKeys_Object=MibTableColumn
reverseTerminalMapKeys=_ReverseTerminalMapKeys_Object((1,3,6,1,4,1,8691,2,21,1,4,1,2,9,1,1,5),_ReverseTerminalMapKeys_Type())
reverseTerminalMapKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalMapKeys.setStatus(_A)
_DataPacking_ObjectIdentity=ObjectIdentity
dataPacking=_DataPacking_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,1,3))
_DataPackingPortTable_Object=MibTable
dataPackingPortTable=_DataPackingPortTable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1))
if mibBuilder.loadTexts:dataPackingPortTable.setStatus(_A)
_DataPackingPortEntry_Object=MibTableRow
dataPackingPortEntry=_DataPackingPortEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1))
dataPackingPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dataPackingPortEntry.setStatus(_A)
_PortPacketLength_Type=Integer32
_PortPacketLength_Object=MibTableColumn
portPacketLength=_PortPacketLength_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,1),_PortPacketLength_Type())
portPacketLength.setMaxAccess(_B)
if mibBuilder.loadTexts:portPacketLength.setStatus(_A)
class _PortDelimiter1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortDelimiter1Enable_Type.__name__=_C
_PortDelimiter1Enable_Object=MibTableColumn
portDelimiter1Enable=_PortDelimiter1Enable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,2),_PortDelimiter1Enable_Type())
portDelimiter1Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter1Enable.setStatus(_A)
class _PortDelimiter1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_PortDelimiter1_Type.__name__=_I
_PortDelimiter1_Object=MibTableColumn
portDelimiter1=_PortDelimiter1_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,3),_PortDelimiter1_Type())
portDelimiter1.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter1.setStatus(_A)
class _PortDelimiter2Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortDelimiter2Enable_Type.__name__=_C
_PortDelimiter2Enable_Object=MibTableColumn
portDelimiter2Enable=_PortDelimiter2Enable_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,4),_PortDelimiter2Enable_Type())
portDelimiter2Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter2Enable.setStatus(_A)
class _PortDelimiter2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_PortDelimiter2_Type.__name__=_I
_PortDelimiter2_Object=MibTableColumn
portDelimiter2=_PortDelimiter2_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,5),_PortDelimiter2_Type())
portDelimiter2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter2.setStatus(_A)
class _PortDelimiterProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*(('doNothing',1),('delimiterAddOne',2),('delimiterAddTwo',4),('stripDelimiter',8)))
_PortDelimiterProcess_Type.__name__=_C
_PortDelimiterProcess_Object=MibTableColumn
portDelimiterProcess=_PortDelimiterProcess_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,6),_PortDelimiterProcess_Type())
portDelimiterProcess.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiterProcess.setStatus(_A)
_PortForceTransmit_Type=Integer32
_PortForceTransmit_Object=MibTableColumn
portForceTransmit=_PortForceTransmit_Object((1,3,6,1,4,1,8691,2,21,1,4,1,3,1,1,7),_PortForceTransmit_Type())
portForceTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:portForceTransmit.setStatus(_A)
_ComParamSetting_ObjectIdentity=ObjectIdentity
comParamSetting=_ComParamSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,2))
_ComParamPortTable_Object=MibTable
comParamPortTable=_ComParamPortTable_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1))
if mibBuilder.loadTexts:comParamPortTable.setStatus(_A)
_ComParamPortEntry_Object=MibTableRow
comParamPortEntry=_ComParamPortEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1))
comParamPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:comParamPortEntry.setStatus(_A)
class _PortAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortAlias_Type.__name__=_I
_PortAlias_Object=MibTableColumn
portAlias=_PortAlias_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,1),_PortAlias_Type())
portAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:portAlias.setStatus(_A)
class _PortInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rs-232',0),('rs-422',1),('rs-485-2wire',2),('rs-485-4wire',3)))
_PortInterface_Type.__name__=_C
_PortInterface_Object=MibTableColumn
portInterface=_PortInterface_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,2),_PortInterface_Type())
portInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:portInterface.setStatus(_A)
class _PortBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('b50',0),('b75',1),('b110',2),('b134',3),('b150',4),('b300',5),('b600',6),('b1200',7),('b1800',8),('b2400',9),('b4800',10),('b9600',12),('b19200',13),('b38400',14),('b57600',15),('b115200',16),('b230400',17),('b460800',18),('b921600',19)))
_PortBaudRate_Type.__name__=_C
_PortBaudRate_Object=MibTableColumn
portBaudRate=_PortBaudRate_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,3),_PortBaudRate_Type())
portBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:portBaudRate.setStatus(_A)
class _PortDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('bits-5',0),('bits-6',1),('bits-7',2),('bits-8',3)))
_PortDataBits_Type.__name__=_C
_PortDataBits_Object=MibTableColumn
portDataBits=_PortDataBits_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,4),_PortDataBits_Type())
portDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:portDataBits.setStatus(_A)
class _PortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('bits-1',0),('bits-1dot5',1),('bits-2',2)))
_PortStopBits_Type.__name__=_C
_PortStopBits_Object=MibTableColumn
portStopBits=_PortStopBits_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,5),_PortStopBits_Type())
portStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:portStopBits.setStatus(_A)
class _PortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,5,7)));namedValues=NamedValues(*((_W,0),('odd',1),('even',3),('mark',5),('space',7)))
_PortParity_Type.__name__=_C
_PortParity_Object=MibTableColumn
portParity=_PortParity_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,6),_PortParity_Type())
portParity.setMaxAccess(_B)
if mibBuilder.loadTexts:portParity.setStatus(_A)
class _PortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),('rts-cts',1),('xon-xoff',2)))
_PortFlowControl_Type.__name__=_C
_PortFlowControl_Object=MibTableColumn
portFlowControl=_PortFlowControl_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,7),_PortFlowControl_Type())
portFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowControl.setStatus(_A)
class _PortFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortFIFO_Type.__name__=_C
_PortFIFO_Object=MibTableColumn
portFIFO=_PortFIFO_Object((1,3,6,1,4,1,8691,2,21,1,4,2,1,1,8),_PortFIFO_Type())
portFIFO.setMaxAccess(_B)
if mibBuilder.loadTexts:portFIFO.setStatus(_A)
_DataBuffering_ObjectIdentity=ObjectIdentity
dataBuffering=_DataBuffering_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,4,3))
_DataBufferingPortTable_Object=MibTable
dataBufferingPortTable=_DataBufferingPortTable_Object((1,3,6,1,4,1,8691,2,21,1,4,3,1))
if mibBuilder.loadTexts:dataBufferingPortTable.setStatus(_A)
_DataBufferingPortEntry_Object=MibTableRow
dataBufferingPortEntry=_DataBufferingPortEntry_Object((1,3,6,1,4,1,8691,2,21,1,4,3,1,1))
dataBufferingPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dataBufferingPortEntry.setStatus(_A)
class _PortBufferingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortBufferingEnable_Type.__name__=_C
_PortBufferingEnable_Object=MibTableColumn
portBufferingEnable=_PortBufferingEnable_Object((1,3,6,1,4,1,8691,2,21,1,4,3,1,1,1),_PortBufferingEnable_Type())
portBufferingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portBufferingEnable.setStatus(_A)
class _PortSerialDataLoggingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortSerialDataLoggingEnable_Type.__name__=_C
_PortSerialDataLoggingEnable_Object=MibTableColumn
portSerialDataLoggingEnable=_PortSerialDataLoggingEnable_Object((1,3,6,1,4,1,8691,2,21,1,4,3,1,1,2),_PortSerialDataLoggingEnable_Type())
portSerialDataLoggingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portSerialDataLoggingEnable.setStatus(_A)
_ModbusAddressMapping_ObjectIdentity=ObjectIdentity
modbusAddressMapping=_ModbusAddressMapping_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,5))
_UserDefinedModbusAddress_ObjectIdentity=ObjectIdentity
userDefinedModbusAddress=_UserDefinedModbusAddress_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,5,1))
class _EnableUserDefinedModbus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableUserDefinedModbus_Type.__name__=_C
_EnableUserDefinedModbus_Object=MibScalar
enableUserDefinedModbus=_EnableUserDefinedModbus_Object((1,3,6,1,4,1,8691,2,21,1,5,1,1),_EnableUserDefinedModbus_Type())
enableUserDefinedModbus.setMaxAccess(_B)
if mibBuilder.loadTexts:enableUserDefinedModbus.setStatus(_A)
class _DoValueStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DoValueStartAddress_Type.__name__=_C
_DoValueStartAddress_Object=MibScalar
doValueStartAddress=_DoValueStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,2),_DoValueStartAddress_Type())
doValueStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:doValueStartAddress.setStatus(_A)
class _DoValueFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DoValueFunctionCode_Type.__name__=_C
_DoValueFunctionCode_Object=MibScalar
doValueFunctionCode=_DoValueFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,3),_DoValueFunctionCode_Type())
doValueFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:doValueFunctionCode.setStatus(_A)
class _DoValueReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DoValueReadWrite_Type.__name__=_C
_DoValueReadWrite_Object=MibScalar
doValueReadWrite=_DoValueReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,4),_DoValueReadWrite_Type())
doValueReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueReadWrite.setStatus(_A)
class _DoValueReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DoValueReferenceAddress_Type.__name__=_C
_DoValueReferenceAddress_Object=MibScalar
doValueReferenceAddress=_DoValueReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,5),_DoValueReferenceAddress_Type())
doValueReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueReferenceAddress.setStatus(_A)
_DoValueTotalchannels_Type=Integer32
_DoValueTotalchannels_Object=MibScalar
doValueTotalchannels=_DoValueTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,6),_DoValueTotalchannels_Type())
doValueTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueTotalchannels.setStatus(_A)
class _DoValueDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DoValueDatatype_Type.__name__=_C
_DoValueDatatype_Object=MibScalar
doValueDatatype=_DoValueDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,7),_DoValueDatatype_Type())
doValueDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueDatatype.setStatus(_A)
class _DoPulseStatusStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DoPulseStatusStartAddress_Type.__name__=_C
_DoPulseStatusStartAddress_Object=MibScalar
doPulseStatusStartAddress=_DoPulseStatusStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,8),_DoPulseStatusStartAddress_Type())
doPulseStatusStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:doPulseStatusStartAddress.setStatus(_A)
class _DoPulseStatusFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DoPulseStatusFunctionCode_Type.__name__=_C
_DoPulseStatusFunctionCode_Object=MibScalar
doPulseStatusFunctionCode=_DoPulseStatusFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,9),_DoPulseStatusFunctionCode_Type())
doPulseStatusFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:doPulseStatusFunctionCode.setStatus(_A)
class _DoPulseStatusReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DoPulseStatusReadWrite_Type.__name__=_C
_DoPulseStatusReadWrite_Object=MibScalar
doPulseStatusReadWrite=_DoPulseStatusReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,10),_DoPulseStatusReadWrite_Type())
doPulseStatusReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:doPulseStatusReadWrite.setStatus(_A)
class _DoPulseStatusReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DoPulseStatusReferenceAddress_Type.__name__=_C
_DoPulseStatusReferenceAddress_Object=MibScalar
doPulseStatusReferenceAddress=_DoPulseStatusReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,11),_DoPulseStatusReferenceAddress_Type())
doPulseStatusReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:doPulseStatusReferenceAddress.setStatus(_A)
_DoPulseStatusTotalchannels_Type=Integer32
_DoPulseStatusTotalchannels_Object=MibScalar
doPulseStatusTotalchannels=_DoPulseStatusTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,12),_DoPulseStatusTotalchannels_Type())
doPulseStatusTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:doPulseStatusTotalchannels.setStatus(_A)
class _DoPulseStatusDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DoPulseStatusDatatype_Type.__name__=_C
_DoPulseStatusDatatype_Object=MibScalar
doPulseStatusDatatype=_DoPulseStatusDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,13),_DoPulseStatusDatatype_Type())
doPulseStatusDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:doPulseStatusDatatype.setStatus(_A)
class _DoValueAllChannelStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DoValueAllChannelStartAddress_Type.__name__=_C
_DoValueAllChannelStartAddress_Object=MibScalar
doValueAllChannelStartAddress=_DoValueAllChannelStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,14),_DoValueAllChannelStartAddress_Type())
doValueAllChannelStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:doValueAllChannelStartAddress.setStatus(_A)
class _DoValueAllChannelFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Q,2),(_J,3)))
_DoValueAllChannelFunctionCode_Type.__name__=_C
_DoValueAllChannelFunctionCode_Object=MibScalar
doValueAllChannelFunctionCode=_DoValueAllChannelFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,15),_DoValueAllChannelFunctionCode_Type())
doValueAllChannelFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:doValueAllChannelFunctionCode.setStatus(_A)
class _DoValueAllChannelReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DoValueAllChannelReadWrite_Type.__name__=_C
_DoValueAllChannelReadWrite_Object=MibScalar
doValueAllChannelReadWrite=_DoValueAllChannelReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,16),_DoValueAllChannelReadWrite_Type())
doValueAllChannelReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueAllChannelReadWrite.setStatus(_A)
class _DoValueAllChannelReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DoValueAllChannelReferenceAddress_Type.__name__=_C
_DoValueAllChannelReferenceAddress_Object=MibScalar
doValueAllChannelReferenceAddress=_DoValueAllChannelReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,17),_DoValueAllChannelReferenceAddress_Type())
doValueAllChannelReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueAllChannelReferenceAddress.setStatus(_A)
_DoValueAllChannelTotalchannels_Type=Integer32
_DoValueAllChannelTotalchannels_Object=MibScalar
doValueAllChannelTotalchannels=_DoValueAllChannelTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,18),_DoValueAllChannelTotalchannels_Type())
doValueAllChannelTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueAllChannelTotalchannels.setStatus(_A)
class _DoValueAllChannelDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DoValueAllChannelDatatype_Type.__name__=_C
_DoValueAllChannelDatatype_Object=MibScalar
doValueAllChannelDatatype=_DoValueAllChannelDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,19),_DoValueAllChannelDatatype_Type())
doValueAllChannelDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:doValueAllChannelDatatype.setStatus(_A)
class _DiValueStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiValueStartAddress_Type.__name__=_C
_DiValueStartAddress_Object=MibScalar
diValueStartAddress=_DiValueStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,20),_DiValueStartAddress_Type())
diValueStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:diValueStartAddress.setStatus(_A)
class _DiValueFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_P,1),(_J,3)))
_DiValueFunctionCode_Type.__name__=_C
_DiValueFunctionCode_Object=MibScalar
diValueFunctionCode=_DiValueFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,21),_DiValueFunctionCode_Type())
diValueFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:diValueFunctionCode.setStatus(_A)
class _DiValueReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DiValueReadWrite_Type.__name__=_C
_DiValueReadWrite_Object=MibScalar
diValueReadWrite=_DiValueReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,22),_DiValueReadWrite_Type())
diValueReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueReadWrite.setStatus(_A)
class _DiValueReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DiValueReferenceAddress_Type.__name__=_C
_DiValueReferenceAddress_Object=MibScalar
diValueReferenceAddress=_DiValueReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,23),_DiValueReferenceAddress_Type())
diValueReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueReferenceAddress.setStatus(_A)
_DiValueTotalchannels_Type=Integer32
_DiValueTotalchannels_Object=MibScalar
diValueTotalchannels=_DiValueTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,24),_DiValueTotalchannels_Type())
diValueTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueTotalchannels.setStatus(_A)
class _DiValueDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DiValueDatatype_Type.__name__=_C
_DiValueDatatype_Object=MibScalar
diValueDatatype=_DiValueDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,25),_DiValueDatatype_Type())
diValueDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueDatatype.setStatus(_A)
class _DiCounterValueStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiCounterValueStartAddress_Type.__name__=_C
_DiCounterValueStartAddress_Object=MibScalar
diCounterValueStartAddress=_DiCounterValueStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,26),_DiCounterValueStartAddress_Type())
diCounterValueStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:diCounterValueStartAddress.setStatus(_A)
class _DiCounterValueFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_J,3))
_DiCounterValueFunctionCode_Type.__name__=_C
_DiCounterValueFunctionCode_Object=MibScalar
diCounterValueFunctionCode=_DiCounterValueFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,27),_DiCounterValueFunctionCode_Type())
diCounterValueFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:diCounterValueFunctionCode.setStatus(_A)
class _DiCounterValueReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DiCounterValueReadWrite_Type.__name__=_C
_DiCounterValueReadWrite_Object=MibScalar
diCounterValueReadWrite=_DiCounterValueReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,28),_DiCounterValueReadWrite_Type())
diCounterValueReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterValueReadWrite.setStatus(_A)
class _DiCounterValueReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DiCounterValueReferenceAddress_Type.__name__=_C
_DiCounterValueReferenceAddress_Object=MibScalar
diCounterValueReferenceAddress=_DiCounterValueReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,29),_DiCounterValueReferenceAddress_Type())
diCounterValueReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterValueReferenceAddress.setStatus(_A)
_DiCounterValueTotalchannels_Type=Integer32
_DiCounterValueTotalchannels_Object=MibScalar
diCounterValueTotalchannels=_DiCounterValueTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,30),_DiCounterValueTotalchannels_Type())
diCounterValueTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterValueTotalchannels.setStatus(_A)
class _DiCounterValueDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DiCounterValueDatatype_Type.__name__=_C
_DiCounterValueDatatype_Object=MibScalar
diCounterValueDatatype=_DiCounterValueDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,31),_DiCounterValueDatatype_Type())
diCounterValueDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterValueDatatype.setStatus(_A)
class _DiValueAllChannelStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiValueAllChannelStartAddress_Type.__name__=_C
_DiValueAllChannelStartAddress_Object=MibScalar
diValueAllChannelStartAddress=_DiValueAllChannelStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,32),_DiValueAllChannelStartAddress_Type())
diValueAllChannelStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:diValueAllChannelStartAddress.setStatus(_A)
class _DiValueAllChannelFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_J,3))
_DiValueAllChannelFunctionCode_Type.__name__=_C
_DiValueAllChannelFunctionCode_Object=MibScalar
diValueAllChannelFunctionCode=_DiValueAllChannelFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,33),_DiValueAllChannelFunctionCode_Type())
diValueAllChannelFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:diValueAllChannelFunctionCode.setStatus(_A)
class _DiValueAllChannelReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DiValueAllChannelReadWrite_Type.__name__=_C
_DiValueAllChannelReadWrite_Object=MibScalar
diValueAllChannelReadWrite=_DiValueAllChannelReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,34),_DiValueAllChannelReadWrite_Type())
diValueAllChannelReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueAllChannelReadWrite.setStatus(_A)
class _DiValueAllChannelReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DiValueAllChannelReferenceAddress_Type.__name__=_C
_DiValueAllChannelReferenceAddress_Object=MibScalar
diValueAllChannelReferenceAddress=_DiValueAllChannelReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,35),_DiValueAllChannelReferenceAddress_Type())
diValueAllChannelReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueAllChannelReferenceAddress.setStatus(_A)
_DiValueAllChannelTotalchannels_Type=Integer32
_DiValueAllChannelTotalchannels_Object=MibScalar
diValueAllChannelTotalchannels=_DiValueAllChannelTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,36),_DiValueAllChannelTotalchannels_Type())
diValueAllChannelTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueAllChannelTotalchannels.setStatus(_A)
class _DiValueAllChannelDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DiValueAllChannelDatatype_Type.__name__=_C
_DiValueAllChannelDatatype_Object=MibScalar
diValueAllChannelDatatype=_DiValueAllChannelDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,37),_DiValueAllChannelDatatype_Type())
diValueAllChannelDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:diValueAllChannelDatatype.setStatus(_A)
class _DiCounterStartStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiCounterStartStartAddress_Type.__name__=_C
_DiCounterStartStartAddress_Object=MibScalar
diCounterStartStartAddress=_DiCounterStartStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,38),_DiCounterStartStartAddress_Type())
diCounterStartStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:diCounterStartStartAddress.setStatus(_A)
class _DiCounterStartFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DiCounterStartFunctionCode_Type.__name__=_C
_DiCounterStartFunctionCode_Object=MibScalar
diCounterStartFunctionCode=_DiCounterStartFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,39),_DiCounterStartFunctionCode_Type())
diCounterStartFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:diCounterStartFunctionCode.setStatus(_A)
class _DiCounterStartReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DiCounterStartReadWrite_Type.__name__=_C
_DiCounterStartReadWrite_Object=MibScalar
diCounterStartReadWrite=_DiCounterStartReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,40),_DiCounterStartReadWrite_Type())
diCounterStartReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterStartReadWrite.setStatus(_A)
class _DiCounterStartReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DiCounterStartReferenceAddress_Type.__name__=_C
_DiCounterStartReferenceAddress_Object=MibScalar
diCounterStartReferenceAddress=_DiCounterStartReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,41),_DiCounterStartReferenceAddress_Type())
diCounterStartReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterStartReferenceAddress.setStatus(_A)
_DiCounterStartTotalchannels_Type=Integer32
_DiCounterStartTotalchannels_Object=MibScalar
diCounterStartTotalchannels=_DiCounterStartTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,42),_DiCounterStartTotalchannels_Type())
diCounterStartTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterStartTotalchannels.setStatus(_A)
class _DiCounterStartDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DiCounterStartDatatype_Type.__name__=_C
_DiCounterStartDatatype_Object=MibScalar
diCounterStartDatatype=_DiCounterStartDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,43),_DiCounterStartDatatype_Type())
diCounterStartDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterStartDatatype.setStatus(_A)
class _DiCounterClearStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiCounterClearStartAddress_Type.__name__=_C
_DiCounterClearStartAddress_Object=MibScalar
diCounterClearStartAddress=_DiCounterClearStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,44),_DiCounterClearStartAddress_Type())
diCounterClearStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:diCounterClearStartAddress.setStatus(_A)
class _DiCounterClearFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DiCounterClearFunctionCode_Type.__name__=_C
_DiCounterClearFunctionCode_Object=MibScalar
diCounterClearFunctionCode=_DiCounterClearFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,1,45),_DiCounterClearFunctionCode_Type())
diCounterClearFunctionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:diCounterClearFunctionCode.setStatus(_A)
class _DiCounterClearReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DiCounterClearReadWrite_Type.__name__=_C
_DiCounterClearReadWrite_Object=MibScalar
diCounterClearReadWrite=_DiCounterClearReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,1,46),_DiCounterClearReadWrite_Type())
diCounterClearReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterClearReadWrite.setStatus(_A)
class _DiCounterClearReferenceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,465536))
_DiCounterClearReferenceAddress_Type.__name__=_C
_DiCounterClearReferenceAddress_Object=MibScalar
diCounterClearReferenceAddress=_DiCounterClearReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,1,47),_DiCounterClearReferenceAddress_Type())
diCounterClearReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterClearReferenceAddress.setStatus(_A)
_DiCounterClearTotalchannels_Type=Integer32
_DiCounterClearTotalchannels_Object=MibScalar
diCounterClearTotalchannels=_DiCounterClearTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,1,48),_DiCounterClearTotalchannels_Type())
diCounterClearTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterClearTotalchannels.setStatus(_A)
class _DiCounterClearDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DiCounterClearDatatype_Type.__name__=_C
_DiCounterClearDatatype_Object=MibScalar
diCounterClearDatatype=_DiCounterClearDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,1,49),_DiCounterClearDatatype_Type())
diCounterClearDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:diCounterClearDatatype.setStatus(_A)
class _UserDefModbusLoadDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('userDefinedModbusLoadDefault',1))
_UserDefModbusLoadDefault_Type.__name__=_C
_UserDefModbusLoadDefault_Object=MibScalar
userDefModbusLoadDefault=_UserDefModbusLoadDefault_Object((1,3,6,1,4,1,8691,2,21,1,5,1,50),_UserDefModbusLoadDefault_Type())
userDefModbusLoadDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:userDefModbusLoadDefault.setStatus(_A)
_DefaultModbusAddress_ObjectIdentity=ObjectIdentity
defaultModbusAddress=_DefaultModbusAddress_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,5,2))
_DefaultDOValueStartAddress_Type=Integer32
_DefaultDOValueStartAddress_Object=MibScalar
defaultDOValueStartAddress=_DefaultDOValueStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,1),_DefaultDOValueStartAddress_Type())
defaultDOValueStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueStartAddress.setStatus(_A)
class _DefaultDOValueFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DefaultDOValueFunctionCode_Type.__name__=_C
_DefaultDOValueFunctionCode_Object=MibScalar
defaultDOValueFunctionCode=_DefaultDOValueFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,2),_DefaultDOValueFunctionCode_Type())
defaultDOValueFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueFunctionCode.setStatus(_A)
class _DefaultDOValueReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDOValueReadWrite_Type.__name__=_C
_DefaultDOValueReadWrite_Object=MibScalar
defaultDOValueReadWrite=_DefaultDOValueReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,3),_DefaultDOValueReadWrite_Type())
defaultDOValueReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueReadWrite.setStatus(_A)
_DefaultDOValueReferenceAddress_Type=Integer32
_DefaultDOValueReferenceAddress_Object=MibScalar
defaultDOValueReferenceAddress=_DefaultDOValueReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,4),_DefaultDOValueReferenceAddress_Type())
defaultDOValueReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueReferenceAddress.setStatus(_A)
_DefaultDOValueTotalchannels_Type=Integer32
_DefaultDOValueTotalchannels_Object=MibScalar
defaultDOValueTotalchannels=_DefaultDOValueTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,5),_DefaultDOValueTotalchannels_Type())
defaultDOValueTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueTotalchannels.setStatus(_A)
class _DefaultDOValueDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDOValueDatatype_Type.__name__=_C
_DefaultDOValueDatatype_Object=MibScalar
defaultDOValueDatatype=_DefaultDOValueDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,6),_DefaultDOValueDatatype_Type())
defaultDOValueDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueDatatype.setStatus(_A)
_DefaultDOPulseStatusStartAddress_Type=Integer32
_DefaultDOPulseStatusStartAddress_Object=MibScalar
defaultDOPulseStatusStartAddress=_DefaultDOPulseStatusStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,7),_DefaultDOPulseStatusStartAddress_Type())
defaultDOPulseStatusStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOPulseStatusStartAddress.setStatus(_A)
class _DefaultDOPulseStatusFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DefaultDOPulseStatusFunctionCode_Type.__name__=_C
_DefaultDOPulseStatusFunctionCode_Object=MibScalar
defaultDOPulseStatusFunctionCode=_DefaultDOPulseStatusFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,8),_DefaultDOPulseStatusFunctionCode_Type())
defaultDOPulseStatusFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOPulseStatusFunctionCode.setStatus(_A)
class _DefaultDOPulseStatusReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDOPulseStatusReadWrite_Type.__name__=_C
_DefaultDOPulseStatusReadWrite_Object=MibScalar
defaultDOPulseStatusReadWrite=_DefaultDOPulseStatusReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,9),_DefaultDOPulseStatusReadWrite_Type())
defaultDOPulseStatusReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOPulseStatusReadWrite.setStatus(_A)
_DefaultDOPulseStatusReferenceAddress_Type=Integer32
_DefaultDOPulseStatusReferenceAddress_Object=MibScalar
defaultDOPulseStatusReferenceAddress=_DefaultDOPulseStatusReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,10),_DefaultDOPulseStatusReferenceAddress_Type())
defaultDOPulseStatusReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOPulseStatusReferenceAddress.setStatus(_A)
_DefaultDOPulseStatusTotalchannels_Type=Integer32
_DefaultDOPulseStatusTotalchannels_Object=MibScalar
defaultDOPulseStatusTotalchannels=_DefaultDOPulseStatusTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,11),_DefaultDOPulseStatusTotalchannels_Type())
defaultDOPulseStatusTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOPulseStatusTotalchannels.setStatus(_A)
class _DefaultDOPulseStatusDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDOPulseStatusDatatype_Type.__name__=_C
_DefaultDOPulseStatusDatatype_Object=MibScalar
defaultDOPulseStatusDatatype=_DefaultDOPulseStatusDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,12),_DefaultDOPulseStatusDatatype_Type())
defaultDOPulseStatusDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOPulseStatusDatatype.setStatus(_A)
_DefaultDOValueAllChannelStartAddress_Type=Integer32
_DefaultDOValueAllChannelStartAddress_Object=MibScalar
defaultDOValueAllChannelStartAddress=_DefaultDOValueAllChannelStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,13),_DefaultDOValueAllChannelStartAddress_Type())
defaultDOValueAllChannelStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueAllChannelStartAddress.setStatus(_A)
class _DefaultDOValueAllChannelFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Q,2),(_J,3)))
_DefaultDOValueAllChannelFunctionCode_Type.__name__=_C
_DefaultDOValueAllChannelFunctionCode_Object=MibScalar
defaultDOValueAllChannelFunctionCode=_DefaultDOValueAllChannelFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,14),_DefaultDOValueAllChannelFunctionCode_Type())
defaultDOValueAllChannelFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueAllChannelFunctionCode.setStatus(_A)
class _DefaultDOValueAllChannelReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDOValueAllChannelReadWrite_Type.__name__=_C
_DefaultDOValueAllChannelReadWrite_Object=MibScalar
defaultDOValueAllChannelReadWrite=_DefaultDOValueAllChannelReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,15),_DefaultDOValueAllChannelReadWrite_Type())
defaultDOValueAllChannelReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueAllChannelReadWrite.setStatus(_A)
_DefaultDOValueAllChannelReferenceAddress_Type=Integer32
_DefaultDOValueAllChannelReferenceAddress_Object=MibScalar
defaultDOValueAllChannelReferenceAddress=_DefaultDOValueAllChannelReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,16),_DefaultDOValueAllChannelReferenceAddress_Type())
defaultDOValueAllChannelReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueAllChannelReferenceAddress.setStatus(_A)
_DefaultDOValueAllChannelTotalchannels_Type=Integer32
_DefaultDOValueAllChannelTotalchannels_Object=MibScalar
defaultDOValueAllChannelTotalchannels=_DefaultDOValueAllChannelTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,17),_DefaultDOValueAllChannelTotalchannels_Type())
defaultDOValueAllChannelTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueAllChannelTotalchannels.setStatus(_A)
class _DefaultDOValueAllChannelDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDOValueAllChannelDatatype_Type.__name__=_C
_DefaultDOValueAllChannelDatatype_Object=MibScalar
defaultDOValueAllChannelDatatype=_DefaultDOValueAllChannelDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,18),_DefaultDOValueAllChannelDatatype_Type())
defaultDOValueAllChannelDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDOValueAllChannelDatatype.setStatus(_A)
_DefaultDIValueStartAddress_Type=Integer32
_DefaultDIValueStartAddress_Object=MibScalar
defaultDIValueStartAddress=_DefaultDIValueStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,19),_DefaultDIValueStartAddress_Type())
defaultDIValueStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueStartAddress.setStatus(_A)
class _DefaultDIValueFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_P,1),(_J,3)))
_DefaultDIValueFunctionCode_Type.__name__=_C
_DefaultDIValueFunctionCode_Object=MibScalar
defaultDIValueFunctionCode=_DefaultDIValueFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,20),_DefaultDIValueFunctionCode_Type())
defaultDIValueFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueFunctionCode.setStatus(_A)
class _DefaultDIValueReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDIValueReadWrite_Type.__name__=_C
_DefaultDIValueReadWrite_Object=MibScalar
defaultDIValueReadWrite=_DefaultDIValueReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,21),_DefaultDIValueReadWrite_Type())
defaultDIValueReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueReadWrite.setStatus(_A)
_DefaultDIValueReferenceAddress_Type=Integer32
_DefaultDIValueReferenceAddress_Object=MibScalar
defaultDIValueReferenceAddress=_DefaultDIValueReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,22),_DefaultDIValueReferenceAddress_Type())
defaultDIValueReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueReferenceAddress.setStatus(_A)
_DefaultDIValueTotalchannels_Type=Integer32
_DefaultDIValueTotalchannels_Object=MibScalar
defaultDIValueTotalchannels=_DefaultDIValueTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,23),_DefaultDIValueTotalchannels_Type())
defaultDIValueTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueTotalchannels.setStatus(_A)
class _DefaultDIValueDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDIValueDatatype_Type.__name__=_C
_DefaultDIValueDatatype_Object=MibScalar
defaultDIValueDatatype=_DefaultDIValueDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,24),_DefaultDIValueDatatype_Type())
defaultDIValueDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueDatatype.setStatus(_A)
_DefaultDICounterValueStartAddress_Type=Integer32
_DefaultDICounterValueStartAddress_Object=MibScalar
defaultDICounterValueStartAddress=_DefaultDICounterValueStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,25),_DefaultDICounterValueStartAddress_Type())
defaultDICounterValueStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterValueStartAddress.setStatus(_A)
class _DefaultDICounterValueFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_J,3))
_DefaultDICounterValueFunctionCode_Type.__name__=_C
_DefaultDICounterValueFunctionCode_Object=MibScalar
defaultDICounterValueFunctionCode=_DefaultDICounterValueFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,26),_DefaultDICounterValueFunctionCode_Type())
defaultDICounterValueFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterValueFunctionCode.setStatus(_A)
class _DefaultDICounterValueReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDICounterValueReadWrite_Type.__name__=_C
_DefaultDICounterValueReadWrite_Object=MibScalar
defaultDICounterValueReadWrite=_DefaultDICounterValueReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,27),_DefaultDICounterValueReadWrite_Type())
defaultDICounterValueReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterValueReadWrite.setStatus(_A)
_DefaultDICounterValueReferenceAddress_Type=Integer32
_DefaultDICounterValueReferenceAddress_Object=MibScalar
defaultDICounterValueReferenceAddress=_DefaultDICounterValueReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,28),_DefaultDICounterValueReferenceAddress_Type())
defaultDICounterValueReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterValueReferenceAddress.setStatus(_A)
_DefaultDICounterValueTotalchannels_Type=Integer32
_DefaultDICounterValueTotalchannels_Object=MibScalar
defaultDICounterValueTotalchannels=_DefaultDICounterValueTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,29),_DefaultDICounterValueTotalchannels_Type())
defaultDICounterValueTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterValueTotalchannels.setStatus(_A)
class _DefaultDICounterValueDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDICounterValueDatatype_Type.__name__=_C
_DefaultDICounterValueDatatype_Object=MibScalar
defaultDICounterValueDatatype=_DefaultDICounterValueDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,30),_DefaultDICounterValueDatatype_Type())
defaultDICounterValueDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterValueDatatype.setStatus(_A)
_DefaultDIValueAllChannelStartAddress_Type=Integer32
_DefaultDIValueAllChannelStartAddress_Object=MibScalar
defaultDIValueAllChannelStartAddress=_DefaultDIValueAllChannelStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,31),_DefaultDIValueAllChannelStartAddress_Type())
defaultDIValueAllChannelStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueAllChannelStartAddress.setStatus(_A)
class _DefaultDIValueAllChannelFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_J,3))
_DefaultDIValueAllChannelFunctionCode_Type.__name__=_C
_DefaultDIValueAllChannelFunctionCode_Object=MibScalar
defaultDIValueAllChannelFunctionCode=_DefaultDIValueAllChannelFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,32),_DefaultDIValueAllChannelFunctionCode_Type())
defaultDIValueAllChannelFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueAllChannelFunctionCode.setStatus(_A)
class _DefaultDIValueAllChannelReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDIValueAllChannelReadWrite_Type.__name__=_C
_DefaultDIValueAllChannelReadWrite_Object=MibScalar
defaultDIValueAllChannelReadWrite=_DefaultDIValueAllChannelReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,33),_DefaultDIValueAllChannelReadWrite_Type())
defaultDIValueAllChannelReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueAllChannelReadWrite.setStatus(_A)
_DefaultDIValueAllChannelReferenceAddress_Type=Integer32
_DefaultDIValueAllChannelReferenceAddress_Object=MibScalar
defaultDIValueAllChannelReferenceAddress=_DefaultDIValueAllChannelReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,34),_DefaultDIValueAllChannelReferenceAddress_Type())
defaultDIValueAllChannelReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueAllChannelReferenceAddress.setStatus(_A)
_DefaultDIValueAllChannelTotalchannels_Type=Integer32
_DefaultDIValueAllChannelTotalchannels_Object=MibScalar
defaultDIValueAllChannelTotalchannels=_DefaultDIValueAllChannelTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,35),_DefaultDIValueAllChannelTotalchannels_Type())
defaultDIValueAllChannelTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueAllChannelTotalchannels.setStatus(_A)
class _DefaultDIValueAllChannelDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDIValueAllChannelDatatype_Type.__name__=_C
_DefaultDIValueAllChannelDatatype_Object=MibScalar
defaultDIValueAllChannelDatatype=_DefaultDIValueAllChannelDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,36),_DefaultDIValueAllChannelDatatype_Type())
defaultDIValueAllChannelDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDIValueAllChannelDatatype.setStatus(_A)
_DefaultDICounterStartStartAddress_Type=Integer32
_DefaultDICounterStartStartAddress_Object=MibScalar
defaultDICounterStartStartAddress=_DefaultDICounterStartStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,37),_DefaultDICounterStartStartAddress_Type())
defaultDICounterStartStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterStartStartAddress.setStatus(_A)
class _DefaultDICounterStartFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DefaultDICounterStartFunctionCode_Type.__name__=_C
_DefaultDICounterStartFunctionCode_Object=MibScalar
defaultDICounterStartFunctionCode=_DefaultDICounterStartFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,38),_DefaultDICounterStartFunctionCode_Type())
defaultDICounterStartFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterStartFunctionCode.setStatus(_A)
class _DefaultDICounterStartReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDICounterStartReadWrite_Type.__name__=_C
_DefaultDICounterStartReadWrite_Object=MibScalar
defaultDICounterStartReadWrite=_DefaultDICounterStartReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,39),_DefaultDICounterStartReadWrite_Type())
defaultDICounterStartReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterStartReadWrite.setStatus(_A)
_DefaultDICounterStartReferenceAddress_Type=Integer32
_DefaultDICounterStartReferenceAddress_Object=MibScalar
defaultDICounterStartReferenceAddress=_DefaultDICounterStartReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,40),_DefaultDICounterStartReferenceAddress_Type())
defaultDICounterStartReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterStartReferenceAddress.setStatus(_A)
_DefaultDICounterStartTotalchannels_Type=Integer32
_DefaultDICounterStartTotalchannels_Object=MibScalar
defaultDICounterStartTotalchannels=_DefaultDICounterStartTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,41),_DefaultDICounterStartTotalchannels_Type())
defaultDICounterStartTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterStartTotalchannels.setStatus(_A)
class _DefaultDICounterStartDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDICounterStartDatatype_Type.__name__=_C
_DefaultDICounterStartDatatype_Object=MibScalar
defaultDICounterStartDatatype=_DefaultDICounterStartDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,42),_DefaultDICounterStartDatatype_Type())
defaultDICounterStartDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterStartDatatype.setStatus(_A)
_DefaultDICounterClearStartAddress_Type=Integer32
_DefaultDICounterClearStartAddress_Object=MibScalar
defaultDICounterClearStartAddress=_DefaultDICounterClearStartAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,43),_DefaultDICounterClearStartAddress_Type())
defaultDICounterClearStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterClearStartAddress.setStatus(_A)
class _DefaultDICounterClearFunctionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_P,1),(_Q,2),(_J,3)))
_DefaultDICounterClearFunctionCode_Type.__name__=_C
_DefaultDICounterClearFunctionCode_Object=MibScalar
defaultDICounterClearFunctionCode=_DefaultDICounterClearFunctionCode_Object((1,3,6,1,4,1,8691,2,21,1,5,2,44),_DefaultDICounterClearFunctionCode_Type())
defaultDICounterClearFunctionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterClearFunctionCode.setStatus(_A)
class _DefaultDICounterClearReadWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DefaultDICounterClearReadWrite_Type.__name__=_C
_DefaultDICounterClearReadWrite_Object=MibScalar
defaultDICounterClearReadWrite=_DefaultDICounterClearReadWrite_Object((1,3,6,1,4,1,8691,2,21,1,5,2,45),_DefaultDICounterClearReadWrite_Type())
defaultDICounterClearReadWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterClearReadWrite.setStatus(_A)
_DefaultDICounterClearReferenceAddress_Type=Integer32
_DefaultDICounterClearReferenceAddress_Object=MibScalar
defaultDICounterClearReferenceAddress=_DefaultDICounterClearReferenceAddress_Object((1,3,6,1,4,1,8691,2,21,1,5,2,46),_DefaultDICounterClearReferenceAddress_Type())
defaultDICounterClearReferenceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterClearReferenceAddress.setStatus(_A)
_DefaultDICounterClearTotalchannels_Type=Integer32
_DefaultDICounterClearTotalchannels_Object=MibScalar
defaultDICounterClearTotalchannels=_DefaultDICounterClearTotalchannels_Object((1,3,6,1,4,1,8691,2,21,1,5,2,47),_DefaultDICounterClearTotalchannels_Type())
defaultDICounterClearTotalchannels.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterClearTotalchannels.setStatus(_A)
class _DefaultDICounterClearDatatype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_DefaultDICounterClearDatatype_Type.__name__=_C
_DefaultDICounterClearDatatype_Object=MibScalar
defaultDICounterClearDatatype=_DefaultDICounterClearDatatype_Object((1,3,6,1,4,1,8691,2,21,1,5,2,48),_DefaultDICounterClearDatatype_Type())
defaultDICounterClearDatatype.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultDICounterClearDatatype.setStatus(_A)
_IoSetting_ObjectIdentity=ObjectIdentity
ioSetting=_IoSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,6))
_DiSetting_ObjectIdentity=ObjectIdentity
diSetting=_DiSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,6,1))
_DiTable_Object=MibTable
diTable=_DiTable_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1))
if mibBuilder.loadTexts:diTable.setStatus(_A)
_DiEntry_Object=MibTableRow
diEntry=_DiEntry_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1))
diEntry.setIndexNames((0,_G,'diIndex'))
if mibBuilder.loadTexts:diEntry.setStatus(_A)
class _DiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DiIndex_Type.__name__=_C
_DiIndex_Object=MibTableColumn
diIndex=_DiIndex_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1,1),_DiIndex_Type())
diIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:diIndex.setStatus(_A)
class _DiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_DiMode_Type.__name__=_C
_DiMode_Object=MibTableColumn
diMode=_DiMode_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1,2),_DiMode_Type())
diMode.setMaxAccess(_B)
if mibBuilder.loadTexts:diMode.setStatus(_A)
class _DiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiStatus_Type.__name__=_C
_DiStatus_Object=MibTableColumn
diStatus=_DiStatus_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1,3),_DiStatus_Type())
diStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:diStatus.setStatus(_A)
class _DiFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DiFilter_Type.__name__=_C
_DiFilter_Object=MibTableColumn
diFilter=_DiFilter_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1,4),_DiFilter_Type())
diFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:diFilter.setStatus(_A)
class _DiTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('loToHigh',0),(_AL,1),('both',2)))
_DiTrigger_Type.__name__=_C
_DiTrigger_Object=MibTableColumn
diTrigger=_DiTrigger_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1,5),_DiTrigger_Type())
diTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:diTrigger.setStatus(_A)
class _DiCntStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_DiCntStart_Type.__name__=_C
_DiCntStart_Object=MibTableColumn
diCntStart=_DiCntStart_Object((1,3,6,1,4,1,8691,2,21,1,6,1,1,1,6),_DiCntStart_Type())
diCntStart.setMaxAccess(_B)
if mibBuilder.loadTexts:diCntStart.setStatus(_A)
_DoSetting_ObjectIdentity=ObjectIdentity
doSetting=_DoSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,6,2))
_DoTable_Object=MibTable
doTable=_DoTable_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1))
if mibBuilder.loadTexts:doTable.setStatus(_A)
_DoEntry_Object=MibTableRow
doEntry=_DoEntry_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1))
doEntry.setIndexNames((0,_G,'doIndex'))
if mibBuilder.loadTexts:doEntry.setStatus(_A)
class _DoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_DoIndex_Type.__name__=_C
_DoIndex_Object=MibTableColumn
doIndex=_DoIndex_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1,1),_DoIndex_Type())
doIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:doIndex.setStatus(_A)
class _DoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_DoMode_Type.__name__=_C
_DoMode_Object=MibTableColumn
doMode=_DoMode_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1,2),_DoMode_Type())
doMode.setMaxAccess(_B)
if mibBuilder.loadTexts:doMode.setStatus(_A)
class _DoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DoStatus_Type.__name__=_C
_DoStatus_Object=MibTableColumn
doStatus=_DoStatus_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1,3),_DoStatus_Type())
doStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:doStatus.setStatus(_A)
class _DoPulseOnWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DoPulseOnWidth_Type.__name__=_C
_DoPulseOnWidth_Object=MibTableColumn
doPulseOnWidth=_DoPulseOnWidth_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1,4),_DoPulseOnWidth_Type())
doPulseOnWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:doPulseOnWidth.setStatus(_A)
class _DoPulseOffWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DoPulseOffWidth_Type.__name__=_C
_DoPulseOffWidth_Object=MibTableColumn
doPulseOffWidth=_DoPulseOffWidth_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1,5),_DoPulseOffWidth_Type())
doPulseOffWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:doPulseOffWidth.setStatus(_A)
class _DoPulseStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_DoPulseStart_Type.__name__=_C
_DoPulseStart_Object=MibTableColumn
doPulseStart=_DoPulseStart_Object((1,3,6,1,4,1,8691,2,21,1,6,2,1,1,6),_DoPulseStart_Type())
doPulseStart.setMaxAccess(_B)
if mibBuilder.loadTexts:doPulseStart.setStatus(_A)
_SysManagement_ObjectIdentity=ObjectIdentity
sysManagement=_SysManagement_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7))
_MiscNetworkSettings_ObjectIdentity=ObjectIdentity
miscNetworkSettings=_MiscNetworkSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,1))
_AccessibleIp_ObjectIdentity=ObjectIdentity
accessibleIp=_AccessibleIp_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,1,1))
class _EnableAccessibleIpList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableAccessibleIpList_Type.__name__=_C
_EnableAccessibleIpList_Object=MibScalar
enableAccessibleIpList=_EnableAccessibleIpList_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,1),_EnableAccessibleIpList_Type())
enableAccessibleIpList.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAccessibleIpList.setStatus(_A)
_AccessibleIpListTable_Object=MibTable
accessibleIpListTable=_AccessibleIpListTable_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,2))
if mibBuilder.loadTexts:accessibleIpListTable.setStatus(_A)
_AccessibleIpListEntry_Object=MibTableRow
accessibleIpListEntry=_AccessibleIpListEntry_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,2,1))
accessibleIpListEntry.setIndexNames((0,_G,_AM))
if mibBuilder.loadTexts:accessibleIpListEntry.setStatus(_A)
class _AccessibleIpListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AccessibleIpListIndex_Type.__name__=_C
_AccessibleIpListIndex_Object=MibTableColumn
accessibleIpListIndex=_AccessibleIpListIndex_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,2,1,1),_AccessibleIpListIndex_Type())
accessibleIpListIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:accessibleIpListIndex.setStatus(_A)
class _ActiveAccessibleIpList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ActiveAccessibleIpList_Type.__name__=_C
_ActiveAccessibleIpList_Object=MibTableColumn
activeAccessibleIpList=_ActiveAccessibleIpList_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,2,1,2),_ActiveAccessibleIpList_Type())
activeAccessibleIpList.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAccessibleIpList.setStatus(_A)
_AccessibleIpListAddress_Type=IpAddress
_AccessibleIpListAddress_Object=MibTableColumn
accessibleIpListAddress=_AccessibleIpListAddress_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,2,1,3),_AccessibleIpListAddress_Type())
accessibleIpListAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:accessibleIpListAddress.setStatus(_A)
_AccessibleIpListNetmask_Type=IpAddress
_AccessibleIpListNetmask_Object=MibTableColumn
accessibleIpListNetmask=_AccessibleIpListNetmask_Object((1,3,6,1,4,1,8691,2,21,1,7,1,1,2,1,4),_AccessibleIpListNetmask_Type())
accessibleIpListNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:accessibleIpListNetmask.setStatus(_A)
_SnmpAgentSettings_ObjectIdentity=ObjectIdentity
snmpAgentSettings=_SnmpAgentSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,1,2))
class _SnmpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnmpEnable_Type.__name__=_C
_SnmpEnable_Object=MibScalar
snmpEnable=_SnmpEnable_Object((1,3,6,1,4,1,8691,2,21,1,7,1,2,1),_SnmpEnable_Type())
snmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEnable.setStatus(_A)
class _SnmpContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SnmpContactName_Type.__name__=_I
_SnmpContactName_Object=MibScalar
snmpContactName=_SnmpContactName_Object((1,3,6,1,4,1,8691,2,21,1,7,1,2,2),_SnmpContactName_Type())
snmpContactName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpContactName.setStatus(_A)
class _SnmpLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SnmpLocation_Type.__name__=_I
_SnmpLocation_Object=MibScalar
snmpLocation=_SnmpLocation_Object((1,3,6,1,4,1,8691,2,21,1,7,1,2,3),_SnmpLocation_Type())
snmpLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpLocation.setStatus(_A)
_AuthenticationServer_ObjectIdentity=ObjectIdentity
authenticationServer=_AuthenticationServer_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,1,4))
class _RadiusServerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RadiusServerIp_Type.__name__=_I
_RadiusServerIp_Object=MibScalar
radiusServerIp=_RadiusServerIp_Object((1,3,6,1,4,1,8691,2,21,1,7,1,4,1),_RadiusServerIp_Type())
radiusServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServerIp.setStatus(_A)
class _UdpPortAuthenticationServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1645,1812)));namedValues=NamedValues(*(('port1645',1645),('port1812',1812)))
_UdpPortAuthenticationServer_Type.__name__=_C
_UdpPortAuthenticationServer_Object=MibScalar
udpPortAuthenticationServer=_UdpPortAuthenticationServer_Object((1,3,6,1,4,1,8691,2,21,1,7,1,4,3),_UdpPortAuthenticationServer_Type())
udpPortAuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:udpPortAuthenticationServer.setStatus(_A)
class _RadiusAccounting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RadiusAccounting_Type.__name__=_C
_RadiusAccounting_Object=MibScalar
radiusAccounting=_RadiusAccounting_Object((1,3,6,1,4,1,8691,2,21,1,7,1,4,4),_RadiusAccounting_Type())
radiusAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccounting.setStatus(_A)
_SysLogSettings_ObjectIdentity=ObjectIdentity
sysLogSettings=_SysLogSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,1,5))
class _SysLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SysLocalLog_Type.__name__=_C
_SysLocalLog_Object=MibScalar
sysLocalLog=_SysLocalLog_Object((1,3,6,1,4,1,8691,2,21,1,7,1,5,1),_SysLocalLog_Type())
sysLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:sysLocalLog.setStatus(_A)
class _NetworkLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NetworkLocalLog_Type.__name__=_C
_NetworkLocalLog_Object=MibScalar
networkLocalLog=_NetworkLocalLog_Object((1,3,6,1,4,1,8691,2,21,1,7,1,5,2),_NetworkLocalLog_Type())
networkLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:networkLocalLog.setStatus(_A)
class _ConfigLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigLocalLog_Type.__name__=_C
_ConfigLocalLog_Object=MibScalar
configLocalLog=_ConfigLocalLog_Object((1,3,6,1,4,1,8691,2,21,1,7,1,5,3),_ConfigLocalLog_Type())
configLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalLog.setStatus(_A)
class _OpModeLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_OpModeLocalLog_Type.__name__=_C
_OpModeLocalLog_Object=MibScalar
opModeLocalLog=_OpModeLocalLog_Object((1,3,6,1,4,1,8691,2,21,1,7,1,5,4),_OpModeLocalLog_Type())
opModeLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:opModeLocalLog.setStatus(_A)
_AutoWarningSettings_ObjectIdentity=ObjectIdentity
autoWarningSettings=_AutoWarningSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,2))
_EventSettings_ObjectIdentity=ObjectIdentity
eventSettings=_EventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,2,1))
class _MailWarningColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningColdStart_Type.__name__=_C
_MailWarningColdStart_Object=MibScalar
mailWarningColdStart=_MailWarningColdStart_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,1),_MailWarningColdStart_Type())
mailWarningColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningColdStart.setStatus(_A)
class _MailWarningWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningWarmStart_Type.__name__=_C
_MailWarningWarmStart_Object=MibScalar
mailWarningWarmStart=_MailWarningWarmStart_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,2),_MailWarningWarmStart_Type())
mailWarningWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningWarmStart.setStatus(_A)
class _MailWarningPower1InputFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningPower1InputFailure_Type.__name__=_C
_MailWarningPower1InputFailure_Object=MibScalar
mailWarningPower1InputFailure=_MailWarningPower1InputFailure_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,3),_MailWarningPower1InputFailure_Type())
mailWarningPower1InputFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningPower1InputFailure.setStatus(_A)
class _MailWarningPower2InputFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningPower2InputFailure_Type.__name__=_C
_MailWarningPower2InputFailure_Object=MibScalar
mailWarningPower2InputFailure=_MailWarningPower2InputFailure_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,4),_MailWarningPower2InputFailure_Type())
mailWarningPower2InputFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningPower2InputFailure.setStatus(_A)
class _MailWarningAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningAuthFailure_Type.__name__=_C
_MailWarningAuthFailure_Object=MibScalar
mailWarningAuthFailure=_MailWarningAuthFailure_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,5),_MailWarningAuthFailure_Type())
mailWarningAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningAuthFailure.setStatus(_A)
class _MailWarningIpChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningIpChanged_Type.__name__=_C
_MailWarningIpChanged_Object=MibScalar
mailWarningIpChanged=_MailWarningIpChanged_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,6),_MailWarningIpChanged_Type())
mailWarningIpChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningIpChanged.setStatus(_A)
class _MailWarningPasswordChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailWarningPasswordChanged_Type.__name__=_C
_MailWarningPasswordChanged_Object=MibScalar
mailWarningPasswordChanged=_MailWarningPasswordChanged_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,7),_MailWarningPasswordChanged_Type())
mailWarningPasswordChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningPasswordChanged.setStatus(_A)
class _TrapServerColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapServerColdStart_Type.__name__=_C
_TrapServerColdStart_Object=MibScalar
trapServerColdStart=_TrapServerColdStart_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,8),_TrapServerColdStart_Type())
trapServerColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerColdStart.setStatus(_A)
class _TrapServerWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapServerWarmStart_Type.__name__=_C
_TrapServerWarmStart_Object=MibScalar
trapServerWarmStart=_TrapServerWarmStart_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,9),_TrapServerWarmStart_Type())
trapServerWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerWarmStart.setStatus(_A)
class _TrapServerAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapServerAuthFailure_Type.__name__=_C
_TrapServerAuthFailure_Object=MibScalar
trapServerAuthFailure=_TrapServerAuthFailure_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,10),_TrapServerAuthFailure_Type())
trapServerAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerAuthFailure.setStatus(_A)
class _RelayOutputPower1InputFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayOutputPower1InputFailure_Type.__name__=_C
_RelayOutputPower1InputFailure_Object=MibScalar
relayOutputPower1InputFailure=_RelayOutputPower1InputFailure_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,11),_RelayOutputPower1InputFailure_Type())
relayOutputPower1InputFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:relayOutputPower1InputFailure.setStatus(_A)
class _RelayOutputPower2InputFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayOutputPower2InputFailure_Type.__name__=_C
_RelayOutputPower2InputFailure_Object=MibScalar
relayOutputPower2InputFailure=_RelayOutputPower2InputFailure_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,12),_RelayOutputPower2InputFailure_Type())
relayOutputPower2InputFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:relayOutputPower2InputFailure.setStatus(_A)
class _RelayOutputEthernetLinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayOutputEthernetLinkDown_Type.__name__=_C
_RelayOutputEthernetLinkDown_Object=MibScalar
relayOutputEthernetLinkDown=_RelayOutputEthernetLinkDown_Object((1,3,6,1,4,1,8691,2,21,1,7,2,1,13),_RelayOutputEthernetLinkDown_Type())
relayOutputEthernetLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:relayOutputEthernetLinkDown.setStatus(_A)
_SerialEventSettings_ObjectIdentity=ObjectIdentity
serialEventSettings=_SerialEventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,2,2))
_PortEventSettingsTable_Object=MibTable
portEventSettingsTable=_PortEventSettingsTable_Object((1,3,6,1,4,1,8691,2,21,1,7,2,2,1))
if mibBuilder.loadTexts:portEventSettingsTable.setStatus(_A)
_PortEventSettingsEntry_Object=MibTableRow
portEventSettingsEntry=_PortEventSettingsEntry_Object((1,3,6,1,4,1,8691,2,21,1,7,2,2,1,1))
portEventSettingsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:portEventSettingsEntry.setStatus(_A)
class _MailDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailDCDchange_Type.__name__=_C
_MailDCDchange_Object=MibTableColumn
mailDCDchange=_MailDCDchange_Object((1,3,6,1,4,1,8691,2,21,1,7,2,2,1,1,1),_MailDCDchange_Type())
mailDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:mailDCDchange.setStatus(_A)
class _TrapDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapDCDchange_Type.__name__=_C
_TrapDCDchange_Object=MibTableColumn
trapDCDchange=_TrapDCDchange_Object((1,3,6,1,4,1,8691,2,21,1,7,2,2,1,1,2),_TrapDCDchange_Type())
trapDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDCDchange.setStatus(_A)
class _MailDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MailDSRchange_Type.__name__=_C
_MailDSRchange_Object=MibTableColumn
mailDSRchange=_MailDSRchange_Object((1,3,6,1,4,1,8691,2,21,1,7,2,2,1,1,3),_MailDSRchange_Type())
mailDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:mailDSRchange.setStatus(_A)
class _TrapDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TrapDSRchange_Type.__name__=_C
_TrapDSRchange_Object=MibTableColumn
trapDSRchange=_TrapDSRchange_Object((1,3,6,1,4,1,8691,2,21,1,7,2,2,1,1,4),_TrapDSRchange_Type())
trapDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDSRchange.setStatus(_A)
_IoEventSettings_ObjectIdentity=ObjectIdentity
ioEventSettings=_IoEventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,2,3))
_DiEventSettingsTable_Object=MibTable
diEventSettingsTable=_DiEventSettingsTable_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,1))
if mibBuilder.loadTexts:diEventSettingsTable.setStatus(_A)
_DiEventSettingsEntry_Object=MibTableRow
diEventSettingsEntry=_DiEventSettingsEntry_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,1,1))
diEventSettingsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:diEventSettingsEntry.setStatus(_A)
class _DiEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DiEventIndex_Type.__name__=_C
_DiEventIndex_Object=MibTableColumn
diEventIndex=_DiEventIndex_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,1,1,1),_DiEventIndex_Type())
diEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:diEventIndex.setStatus(_A)
class _DiEventTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DiEventTrap_Type.__name__=_C
_DiEventTrap_Object=MibTableColumn
diEventTrap=_DiEventTrap_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,1,1,2),_DiEventTrap_Type())
diEventTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:diEventTrap.setStatus(_A)
_DoEventSettingsTable_Object=MibTable
doEventSettingsTable=_DoEventSettingsTable_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,2))
if mibBuilder.loadTexts:doEventSettingsTable.setStatus(_A)
_DoEventSettingsEntry_Object=MibTableRow
doEventSettingsEntry=_DoEventSettingsEntry_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,2,1))
doEventSettingsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:doEventSettingsEntry.setStatus(_A)
class _DoEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_DoEventIndex_Type.__name__=_C
_DoEventIndex_Object=MibTableColumn
doEventIndex=_DoEventIndex_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,2,1,1),_DoEventIndex_Type())
doEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:doEventIndex.setStatus(_A)
class _DoEventTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DoEventTrap_Type.__name__=_C
_DoEventTrap_Object=MibTableColumn
doEventTrap=_DoEventTrap_Object((1,3,6,1,4,1,8691,2,21,1,7,2,3,2,1,2),_DoEventTrap_Type())
doEventTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:doEventTrap.setStatus(_A)
_EmailAlert_ObjectIdentity=ObjectIdentity
emailAlert=_EmailAlert_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,2,4))
_EmailWarningMailServer_Type=DisplayString
_EmailWarningMailServer_Object=MibScalar
emailWarningMailServer=_EmailWarningMailServer_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,1),_EmailWarningMailServer_Type())
emailWarningMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningMailServer.setStatus(_A)
class _EmailRequiresAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('non-require',0),('require',1)))
_EmailRequiresAuthentication_Type.__name__=_C
_EmailRequiresAuthentication_Object=MibScalar
emailRequiresAuthentication=_EmailRequiresAuthentication_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,2),_EmailRequiresAuthentication_Type())
emailRequiresAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:emailRequiresAuthentication.setStatus(_A)
_EmailWarningUserName_Type=DisplayString
_EmailWarningUserName_Object=MibScalar
emailWarningUserName=_EmailWarningUserName_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,3),_EmailWarningUserName_Type())
emailWarningUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningUserName.setStatus(_A)
_EmailWarningFromEmail_Type=DisplayString
_EmailWarningFromEmail_Object=MibScalar
emailWarningFromEmail=_EmailWarningFromEmail_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,5),_EmailWarningFromEmail_Type())
emailWarningFromEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFromEmail.setStatus(_A)
_EmailWarningFirstEmailAddr_Type=DisplayString
_EmailWarningFirstEmailAddr_Object=MibScalar
emailWarningFirstEmailAddr=_EmailWarningFirstEmailAddr_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,6),_EmailWarningFirstEmailAddr_Type())
emailWarningFirstEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFirstEmailAddr.setStatus(_A)
_EmailWarningSecondEmailAddr_Type=DisplayString
_EmailWarningSecondEmailAddr_Object=MibScalar
emailWarningSecondEmailAddr=_EmailWarningSecondEmailAddr_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,7),_EmailWarningSecondEmailAddr_Type())
emailWarningSecondEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSecondEmailAddr.setStatus(_A)
_EmailWarningThirdEmailAddr_Type=DisplayString
_EmailWarningThirdEmailAddr_Object=MibScalar
emailWarningThirdEmailAddr=_EmailWarningThirdEmailAddr_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,8),_EmailWarningThirdEmailAddr_Type())
emailWarningThirdEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningThirdEmailAddr.setStatus(_A)
_EmailWarningFourthEmailAddr_Type=DisplayString
_EmailWarningFourthEmailAddr_Object=MibScalar
emailWarningFourthEmailAddr=_EmailWarningFourthEmailAddr_Object((1,3,6,1,4,1,8691,2,21,1,7,2,4,9),_EmailWarningFourthEmailAddr_Type())
emailWarningFourthEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFourthEmailAddr.setStatus(_A)
_SnmpTrap_ObjectIdentity=ObjectIdentity
snmpTrap=_SnmpTrap_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,2,5))
_SnmpTrapReceiverIp_Type=DisplayString
_SnmpTrapReceiverIp_Object=MibScalar
snmpTrapReceiverIp=_SnmpTrapReceiverIp_Object((1,3,6,1,4,1,8691,2,21,1,7,2,5,1),_SnmpTrapReceiverIp_Type())
snmpTrapReceiverIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapReceiverIp.setStatus(_A)
class _TrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v1',0),('v2c',1)))
_TrapVersion_Type.__name__=_C
_TrapVersion_Object=MibScalar
trapVersion=_TrapVersion_Object((1,3,6,1,4,1,8691,2,21,1,7,2,5,2),_TrapVersion_Type())
trapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:trapVersion.setStatus(_A)
_Maintenance_ObjectIdentity=ObjectIdentity
maintenance=_Maintenance_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,3))
_ConsoleSettings_ObjectIdentity=ObjectIdentity
consoleSettings=_ConsoleSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,3,1))
class _HttpConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_HttpConsole_Type.__name__=_C
_HttpConsole_Object=MibScalar
httpConsole=_HttpConsole_Object((1,3,6,1,4,1,8691,2,21,1,7,3,1,1),_HttpConsole_Type())
httpConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:httpConsole.setStatus(_A)
class _HttpsConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_HttpsConsole_Type.__name__=_C
_HttpsConsole_Object=MibScalar
httpsConsole=_HttpsConsole_Object((1,3,6,1,4,1,8691,2,21,1,7,3,1,2),_HttpsConsole_Type())
httpsConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:httpsConsole.setStatus(_A)
class _TelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TelnetConsole_Type.__name__=_C
_TelnetConsole_Object=MibScalar
telnetConsole=_TelnetConsole_Object((1,3,6,1,4,1,8691,2,21,1,7,3,1,3),_TelnetConsole_Type())
telnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetConsole.setStatus(_A)
class _SshConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SshConsole_Type.__name__=_C
_SshConsole_Object=MibScalar
sshConsole=_SshConsole_Object((1,3,6,1,4,1,8691,2,21,1,7,3,1,4),_SshConsole_Type())
sshConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConsole.setStatus(_A)
class _SerialConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SerialConsole_Type.__name__=_C
_SerialConsole_Object=MibScalar
serialConsole=_SerialConsole_Object((1,3,6,1,4,1,8691,2,21,1,7,3,1,5),_SerialConsole_Type())
serialConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:serialConsole.setStatus(_A)
class _ResetButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable_after_60_sec',0),('always_enable',1)))
_ResetButton_Type.__name__=_C
_ResetButton_Object=MibScalar
resetButton=_ResetButton_Object((1,3,6,1,4,1,8691,2,21,1,7,3,1,6),_ResetButton_Type())
resetButton.setMaxAccess(_B)
if mibBuilder.loadTexts:resetButton.setStatus(_A)
_LoadFactoryDefault_ObjectIdentity=ObjectIdentity
loadFactoryDefault=_LoadFactoryDefault_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,3,2))
class _LoadFactoryDefaultSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('resetToFactoryDefault-ExcludingIpConfiguration',0),('resetToFactoryDefault',1)))
_LoadFactoryDefaultSetting_Type.__name__=_C
_LoadFactoryDefaultSetting_Object=MibScalar
loadFactoryDefaultSetting=_LoadFactoryDefaultSetting_Object((1,3,6,1,4,1,8691,2,21,1,7,3,2,1),_LoadFactoryDefaultSetting_Type())
loadFactoryDefaultSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:loadFactoryDefaultSetting.setStatus(_A)
_SdBackup_ObjectIdentity=ObjectIdentity
sdBackup=_SdBackup_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,7,3,3))
class _AutoLoadSdConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_AutoLoadSdConfiguration_Type.__name__=_C
_AutoLoadSdConfiguration_Object=MibScalar
autoLoadSdConfiguration=_AutoLoadSdConfiguration_Object((1,3,6,1,4,1,8691,2,21,1,7,3,3,1),_AutoLoadSdConfiguration_Type())
autoLoadSdConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:autoLoadSdConfiguration.setStatus(_A)
_SysStatus_ObjectIdentity=ObjectIdentity
sysStatus=_SysStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8))
_S2eConnections_ObjectIdentity=ObjectIdentity
s2eConnections=_S2eConnections_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,1))
_MonitorRemoteIpTable_Object=MibTable
monitorRemoteIpTable=_MonitorRemoteIpTable_Object((1,3,6,1,4,1,8691,2,21,1,8,1,1))
if mibBuilder.loadTexts:monitorRemoteIpTable.setStatus(_A)
_MonitorRemoteIpEntry_Object=MibTableRow
monitorRemoteIpEntry=_MonitorRemoteIpEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,1,1,1))
monitorRemoteIpEntry.setIndexNames((0,_G,_H),(0,_G,_AN))
if mibBuilder.loadTexts:monitorRemoteIpEntry.setStatus(_A)
class _RemoteIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RemoteIpIndex_Type.__name__=_C
_RemoteIpIndex_Object=MibTableColumn
remoteIpIndex=_RemoteIpIndex_Object((1,3,6,1,4,1,8691,2,21,1,8,1,1,1,1),_RemoteIpIndex_Type())
remoteIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteIpIndex.setStatus(_A)
_MonitorRemoteIp_Type=IpAddress
_MonitorRemoteIp_Object=MibTableColumn
monitorRemoteIp=_MonitorRemoteIp_Object((1,3,6,1,4,1,8691,2,21,1,8,1,1,1,2),_MonitorRemoteIp_Type())
monitorRemoteIp.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRemoteIp.setStatus(_A)
_SerialPortStatus_ObjectIdentity=ObjectIdentity
serialPortStatus=_SerialPortStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,2))
_MonitorSerialPortStatusTable_Object=MibTable
monitorSerialPortStatusTable=_MonitorSerialPortStatusTable_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1))
if mibBuilder.loadTexts:monitorSerialPortStatusTable.setStatus(_A)
_MonitorSerialPortStatusEntry_Object=MibTableRow
monitorSerialPortStatusEntry=_MonitorSerialPortStatusEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1))
monitorSerialPortStatusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortStatusEntry.setStatus(_A)
_MonitorTxCount_Type=Integer32
_MonitorTxCount_Object=MibTableColumn
monitorTxCount=_MonitorTxCount_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,1),_MonitorTxCount_Type())
monitorTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTxCount.setStatus(_A)
_MonitorRxCount_Type=Integer32
_MonitorRxCount_Object=MibTableColumn
monitorRxCount=_MonitorRxCount_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,2),_MonitorRxCount_Type())
monitorRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRxCount.setStatus(_A)
_MonitorTxTotalCount_Type=Integer32
_MonitorTxTotalCount_Object=MibTableColumn
monitorTxTotalCount=_MonitorTxTotalCount_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,3),_MonitorTxTotalCount_Type())
monitorTxTotalCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTxTotalCount.setStatus(_A)
_MonitorRxTotalCount_Type=Integer32
_MonitorRxTotalCount_Object=MibTableColumn
monitorRxTotalCount=_MonitorRxTotalCount_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,4),_MonitorRxTotalCount_Type())
monitorRxTotalCount.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRxTotalCount.setStatus(_A)
class _MonitorDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorDSR_Type.__name__=_C
_MonitorDSR_Object=MibTableColumn
monitorDSR=_MonitorDSR_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,5),_MonitorDSR_Type())
monitorDSR.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDSR.setStatus(_A)
class _MonitorDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorDTR_Type.__name__=_C
_MonitorDTR_Object=MibTableColumn
monitorDTR=_MonitorDTR_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,6),_MonitorDTR_Type())
monitorDTR.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDTR.setStatus(_A)
class _MonitorRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorRTS_Type.__name__=_C
_MonitorRTS_Object=MibTableColumn
monitorRTS=_MonitorRTS_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,7),_MonitorRTS_Type())
monitorRTS.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRTS.setStatus(_A)
class _MonitorCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorCTS_Type.__name__=_C
_MonitorCTS_Object=MibTableColumn
monitorCTS=_MonitorCTS_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,8),_MonitorCTS_Type())
monitorCTS.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorCTS.setStatus(_A)
class _MonitorDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorDCD_Type.__name__=_C
_MonitorDCD_Object=MibTableColumn
monitorDCD=_MonitorDCD_Object((1,3,6,1,4,1,8691,2,21,1,8,2,1,1,9),_MonitorDCD_Type())
monitorDCD.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDCD.setStatus(_A)
_SerialPortErrorCount_ObjectIdentity=ObjectIdentity
serialPortErrorCount=_SerialPortErrorCount_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,3))
_MonitorSerialPortErrorCountTable_Object=MibTable
monitorSerialPortErrorCountTable=_MonitorSerialPortErrorCountTable_Object((1,3,6,1,4,1,8691,2,21,1,8,3,1))
if mibBuilder.loadTexts:monitorSerialPortErrorCountTable.setStatus(_A)
_MonitorSerialPortErrorCountEntry_Object=MibTableRow
monitorSerialPortErrorCountEntry=_MonitorSerialPortErrorCountEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,3,1,1))
monitorSerialPortErrorCountEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortErrorCountEntry.setStatus(_A)
_MonitorErrorCountFrame_Type=Integer32
_MonitorErrorCountFrame_Object=MibTableColumn
monitorErrorCountFrame=_MonitorErrorCountFrame_Object((1,3,6,1,4,1,8691,2,21,1,8,3,1,1,1),_MonitorErrorCountFrame_Type())
monitorErrorCountFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountFrame.setStatus(_A)
_MonitorErrorCountParity_Type=Integer32
_MonitorErrorCountParity_Object=MibTableColumn
monitorErrorCountParity=_MonitorErrorCountParity_Object((1,3,6,1,4,1,8691,2,21,1,8,3,1,1,2),_MonitorErrorCountParity_Type())
monitorErrorCountParity.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountParity.setStatus(_A)
_MonitorErrorCountOverrun_Type=Integer32
_MonitorErrorCountOverrun_Object=MibTableColumn
monitorErrorCountOverrun=_MonitorErrorCountOverrun_Object((1,3,6,1,4,1,8691,2,21,1,8,3,1,1,3),_MonitorErrorCountOverrun_Type())
monitorErrorCountOverrun.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountOverrun.setStatus(_A)
_MonitorErrorCountBreak_Type=Integer32
_MonitorErrorCountBreak_Object=MibTableColumn
monitorErrorCountBreak=_MonitorErrorCountBreak_Object((1,3,6,1,4,1,8691,2,21,1,8,3,1,1,4),_MonitorErrorCountBreak_Type())
monitorErrorCountBreak.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorErrorCountBreak.setStatus(_A)
_SerialPortSettings_ObjectIdentity=ObjectIdentity
serialPortSettings=_SerialPortSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,4))
_MonitorSerialPortSettingsTable_Object=MibTable
monitorSerialPortSettingsTable=_MonitorSerialPortSettingsTable_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1))
if mibBuilder.loadTexts:monitorSerialPortSettingsTable.setStatus(_A)
_MonitorSerialPortSettingsEntry_Object=MibTableRow
monitorSerialPortSettingsEntry=_MonitorSerialPortSettingsEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1))
monitorSerialPortSettingsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortSettingsEntry.setStatus(_A)
_MonitorBaudRate_Type=Integer32
_MonitorBaudRate_Object=MibTableColumn
monitorBaudRate=_MonitorBaudRate_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,1),_MonitorBaudRate_Type())
monitorBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorBaudRate.setStatus(_A)
class _MonitorDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8)));namedValues=NamedValues(*(('bits-5',5),('bits-6',6),('bits-7',7),('bits-8',8)))
_MonitorDataBits_Type.__name__=_C
_MonitorDataBits_Object=MibTableColumn
monitorDataBits=_MonitorDataBits_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,2),_MonitorDataBits_Type())
monitorDataBits.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDataBits.setStatus(_A)
_MonitorStopBits_Type=DisplayString
_MonitorStopBits_Object=MibTableColumn
monitorStopBits=_MonitorStopBits_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,3),_MonitorStopBits_Type())
monitorStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorStopBits.setStatus(_A)
class _MonitorParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8,24,40,56)));namedValues=NamedValues(*((_W,0),('odd',8),('even',24),('mark',40),('space',56)))
_MonitorParity_Type.__name__=_C
_MonitorParity_Object=MibTableColumn
monitorParity=_MonitorParity_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,4),_MonitorParity_Type())
monitorParity.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorParity.setStatus(_A)
class _MonitorRTSCTSFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorRTSCTSFlowControl_Type.__name__=_C
_MonitorRTSCTSFlowControl_Object=MibTableColumn
monitorRTSCTSFlowControl=_MonitorRTSCTSFlowControl_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,5),_MonitorRTSCTSFlowControl_Type())
monitorRTSCTSFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRTSCTSFlowControl.setStatus(_A)
class _MonitorXONXOFFFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MonitorXONXOFFFlowControl_Type.__name__=_C
_MonitorXONXOFFFlowControl_Object=MibTableColumn
monitorXONXOFFFlowControl=_MonitorXONXOFFFlowControl_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,6),_MonitorXONXOFFFlowControl_Type())
monitorXONXOFFFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorXONXOFFFlowControl.setStatus(_A)
class _MonitorFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MonitorFIFO_Type.__name__=_C
_MonitorFIFO_Object=MibTableColumn
monitorFIFO=_MonitorFIFO_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,7),_MonitorFIFO_Type())
monitorFIFO.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFIFO.setStatus(_A)
class _MonitorInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rs-232',0),('rs-422',1),('rs-485-2-wire',2),('rs-485-4-wire',3)))
_MonitorInterface_Type.__name__=_C
_MonitorInterface_Object=MibTableColumn
monitorInterface=_MonitorInterface_Object((1,3,6,1,4,1,8691,2,21,1,8,4,1,1,8),_MonitorInterface_Type())
monitorInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorInterface.setStatus(_A)
_SerialPortBuffering_ObjectIdentity=ObjectIdentity
serialPortBuffering=_SerialPortBuffering_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,5))
_MonitorSerialPortBufferingTable_Object=MibTable
monitorSerialPortBufferingTable=_MonitorSerialPortBufferingTable_Object((1,3,6,1,4,1,8691,2,21,1,8,5,1))
if mibBuilder.loadTexts:monitorSerialPortBufferingTable.setStatus(_A)
_MonitorSerialPortBufferingEntry_Object=MibTableRow
monitorSerialPortBufferingEntry=_MonitorSerialPortBufferingEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,5,1,1))
monitorSerialPortBufferingEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:monitorSerialPortBufferingEntry.setStatus(_A)
_MonitorBuffering_Type=Integer32
_MonitorBuffering_Object=MibTableColumn
monitorBuffering=_MonitorBuffering_Object((1,3,6,1,4,1,8691,2,21,1,8,5,1,1,1),_MonitorBuffering_Type())
monitorBuffering.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorBuffering.setStatus(_A)
_SysWlanStatus_ObjectIdentity=ObjectIdentity
sysWlanStatus=_SysWlanStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,6))
_WlanStatusActiveProfileName_Type=DisplayString
_WlanStatusActiveProfileName_Object=MibScalar
wlanStatusActiveProfileName=_WlanStatusActiveProfileName_Object((1,3,6,1,4,1,8691,2,21,1,8,6,1),_WlanStatusActiveProfileName_Type())
wlanStatusActiveProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusActiveProfileName.setStatus(_A)
class _WlanStatusIpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Y,0),(_Z,1),(_a,2)))
_WlanStatusIpConfiguration_Type.__name__=_C
_WlanStatusIpConfiguration_Object=MibScalar
wlanStatusIpConfiguration=_WlanStatusIpConfiguration_Object((1,3,6,1,4,1,8691,2,21,1,8,6,2),_WlanStatusIpConfiguration_Type())
wlanStatusIpConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusIpConfiguration.setStatus(_A)
_WlanStatusIpAddress_Type=IpAddress
_WlanStatusIpAddress_Object=MibScalar
wlanStatusIpAddress=_WlanStatusIpAddress_Object((1,3,6,1,4,1,8691,2,21,1,8,6,3),_WlanStatusIpAddress_Type())
wlanStatusIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusIpAddress.setStatus(_A)
_WlanStatusNetMask_Type=IpAddress
_WlanStatusNetMask_Object=MibScalar
wlanStatusNetMask=_WlanStatusNetMask_Object((1,3,6,1,4,1,8691,2,21,1,8,6,4),_WlanStatusNetMask_Type())
wlanStatusNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusNetMask.setStatus(_A)
_WlanStatusDefaultGateway_Type=IpAddress
_WlanStatusDefaultGateway_Object=MibScalar
wlanStatusDefaultGateway=_WlanStatusDefaultGateway_Object((1,3,6,1,4,1,8691,2,21,1,8,6,5),_WlanStatusDefaultGateway_Type())
wlanStatusDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusDefaultGateway.setStatus(_A)
_WlanStatusNetworkType_Type=DisplayString
_WlanStatusNetworkType_Object=MibScalar
wlanStatusNetworkType=_WlanStatusNetworkType_Object((1,3,6,1,4,1,8691,2,21,1,8,6,6),_WlanStatusNetworkType_Type())
wlanStatusNetworkType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusNetworkType.setStatus(_A)
_WlanStatusRFType_Type=DisplayString
_WlanStatusRFType_Object=MibScalar
wlanStatusRFType=_WlanStatusRFType_Object((1,3,6,1,4,1,8691,2,21,1,8,6,7),_WlanStatusRFType_Type())
wlanStatusRFType.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusRFType.setStatus(_A)
_WlanStatusSSID_Type=DisplayString
_WlanStatusSSID_Object=MibScalar
wlanStatusSSID=_WlanStatusSSID_Object((1,3,6,1,4,1,8691,2,21,1,8,6,8),_WlanStatusSSID_Type())
wlanStatusSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusSSID.setStatus(_A)
_WlanStatusChannel_Type=DisplayString
_WlanStatusChannel_Object=MibScalar
wlanStatusChannel=_WlanStatusChannel_Object((1,3,6,1,4,1,8691,2,21,1,8,6,9),_WlanStatusChannel_Type())
wlanStatusChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusChannel.setStatus(_A)
_WlanStatusAuthentication_Type=DisplayString
_WlanStatusAuthentication_Object=MibScalar
wlanStatusAuthentication=_WlanStatusAuthentication_Object((1,3,6,1,4,1,8691,2,21,1,8,6,10),_WlanStatusAuthentication_Type())
wlanStatusAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusAuthentication.setStatus(_A)
_WlanStatusEncryption_Type=DisplayString
_WlanStatusEncryption_Object=MibScalar
wlanStatusEncryption=_WlanStatusEncryption_Object((1,3,6,1,4,1,8691,2,21,1,8,6,11),_WlanStatusEncryption_Type())
wlanStatusEncryption.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusEncryption.setStatus(_A)
_WlanStatusRegion_Type=DisplayString
_WlanStatusRegion_Object=MibScalar
wlanStatusRegion=_WlanStatusRegion_Object((1,3,6,1,4,1,8691,2,21,1,8,6,12),_WlanStatusRegion_Type())
wlanStatusRegion.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusRegion.setStatus(_A)
_WlanStatusSignalStrength_Type=DisplayString
_WlanStatusSignalStrength_Object=MibScalar
wlanStatusSignalStrength=_WlanStatusSignalStrength_Object((1,3,6,1,4,1,8691,2,21,1,8,6,13),_WlanStatusSignalStrength_Type())
wlanStatusSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusSignalStrength.setStatus(_A)
_WlanStatusConnectionSpeed_Type=DisplayString
_WlanStatusConnectionSpeed_Object=MibScalar
wlanStatusConnectionSpeed=_WlanStatusConnectionSpeed_Object((1,3,6,1,4,1,8691,2,21,1,8,6,14),_WlanStatusConnectionSpeed_Type())
wlanStatusConnectionSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusConnectionSpeed.setStatus(_A)
_WlanStatusCurrentBSSID_Type=DisplayString
_WlanStatusCurrentBSSID_Object=MibScalar
wlanStatusCurrentBSSID=_WlanStatusCurrentBSSID_Object((1,3,6,1,4,1,8691,2,21,1,8,6,15),_WlanStatusCurrentBSSID_Type())
wlanStatusCurrentBSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatusCurrentBSSID.setStatus(_A)
_IoStatus_ObjectIdentity=ObjectIdentity
ioStatus=_IoStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,7))
_DiIoStatus_ObjectIdentity=ObjectIdentity
diIoStatus=_DiIoStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,7,1))
_DiMonTable_Object=MibTable
diMonTable=_DiMonTable_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1))
if mibBuilder.loadTexts:diMonTable.setStatus(_A)
_DiMonEntry_Object=MibTableRow
diMonEntry=_DiMonEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1))
diMonEntry.setIndexNames((0,_G,_AO))
if mibBuilder.loadTexts:diMonEntry.setStatus(_A)
_DiMonIndex_Type=Integer32
_DiMonIndex_Object=MibTableColumn
diMonIndex=_DiMonIndex_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1,1),_DiMonIndex_Type())
diMonIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:diMonIndex.setStatus(_A)
_DiMonMode_Type=Integer32
_DiMonMode_Object=MibTableColumn
diMonMode=_DiMonMode_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1,2),_DiMonMode_Type())
diMonMode.setMaxAccess(_D)
if mibBuilder.loadTexts:diMonMode.setStatus(_A)
_DiMonStatus_Type=Integer32
_DiMonStatus_Object=MibTableColumn
diMonStatus=_DiMonStatus_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1,3),_DiMonStatus_Type())
diMonStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:diMonStatus.setStatus(_A)
_DiMonFilter_Type=Integer32
_DiMonFilter_Object=MibTableColumn
diMonFilter=_DiMonFilter_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1,4),_DiMonFilter_Type())
diMonFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:diMonFilter.setStatus(_A)
class _DiMonTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('loToHigh',0),(_AL,1),('both',2)))
_DiMonTrigger_Type.__name__=_C
_DiMonTrigger_Object=MibTableColumn
diMonTrigger=_DiMonTrigger_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1,5),_DiMonTrigger_Type())
diMonTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:diMonTrigger.setStatus(_A)
_DiMonCntStart_Type=Integer32
_DiMonCntStart_Object=MibTableColumn
diMonCntStart=_DiMonCntStart_Object((1,3,6,1,4,1,8691,2,21,1,8,7,1,1,1,6),_DiMonCntStart_Type())
diMonCntStart.setMaxAccess(_D)
if mibBuilder.loadTexts:diMonCntStart.setStatus(_A)
_DoIoStatus_ObjectIdentity=ObjectIdentity
doIoStatus=_DoIoStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,7,2))
_DoMonTable_Object=MibTable
doMonTable=_DoMonTable_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1))
if mibBuilder.loadTexts:doMonTable.setStatus(_A)
_DoMonEntry_Object=MibTableRow
doMonEntry=_DoMonEntry_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1))
doMonEntry.setIndexNames((0,_G,_AP))
if mibBuilder.loadTexts:doMonEntry.setStatus(_A)
_DoMonIndex_Type=Integer32
_DoMonIndex_Object=MibTableColumn
doMonIndex=_DoMonIndex_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1,1),_DoMonIndex_Type())
doMonIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:doMonIndex.setStatus(_A)
_DoMonMode_Type=Integer32
_DoMonMode_Object=MibTableColumn
doMonMode=_DoMonMode_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1,2),_DoMonMode_Type())
doMonMode.setMaxAccess(_D)
if mibBuilder.loadTexts:doMonMode.setStatus(_A)
_DoMonStatus_Type=Integer32
_DoMonStatus_Object=MibTableColumn
doMonStatus=_DoMonStatus_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1,3),_DoMonStatus_Type())
doMonStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:doMonStatus.setStatus(_A)
_DoMonPulseOnWidth_Type=Integer32
_DoMonPulseOnWidth_Object=MibTableColumn
doMonPulseOnWidth=_DoMonPulseOnWidth_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1,4),_DoMonPulseOnWidth_Type())
doMonPulseOnWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:doMonPulseOnWidth.setStatus(_A)
_DoMonPulseOffWidth_Type=Integer32
_DoMonPulseOffWidth_Object=MibTableColumn
doMonPulseOffWidth=_DoMonPulseOffWidth_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1,5),_DoMonPulseOffWidth_Type())
doMonPulseOffWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:doMonPulseOffWidth.setStatus(_A)
_DoMonPulseStart_Type=Integer32
_DoMonPulseStart_Object=MibTableColumn
doMonPulseStart=_DoMonPulseStart_Object((1,3,6,1,4,1,8691,2,21,1,8,7,2,1,1,6),_DoMonPulseStart_Type())
doMonPulseStart.setMaxAccess(_D)
if mibBuilder.loadTexts:doMonPulseStart.setStatus(_A)
_SysAlertStatus_ObjectIdentity=ObjectIdentity
sysAlertStatus=_SysAlertStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,8,8))
class _Power1FailureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('na',0),('non',1),(_AG,2),(_AQ,3)))
_Power1FailureStatus_Type.__name__=_C
_Power1FailureStatus_Object=MibScalar
power1FailureStatus=_Power1FailureStatus_Object((1,3,6,1,4,1,8691,2,21,1,8,8,1),_Power1FailureStatus_Type())
power1FailureStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power1FailureStatus.setStatus(_A)
class _Power1FailureAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ack',1))
_Power1FailureAck_Type.__name__=_C
_Power1FailureAck_Object=MibScalar
power1FailureAck=_Power1FailureAck_Object((1,3,6,1,4,1,8691,2,21,1,8,8,2),_Power1FailureAck_Type())
power1FailureAck.setMaxAccess(_B)
if mibBuilder.loadTexts:power1FailureAck.setStatus(_A)
class _Power2FailureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('na',0),('non',1),(_AG,2),(_AQ,3)))
_Power2FailureStatus_Type.__name__=_C
_Power2FailureStatus_Object=MibScalar
power2FailureStatus=_Power2FailureStatus_Object((1,3,6,1,4,1,8691,2,21,1,8,8,3),_Power2FailureStatus_Type())
power2FailureStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power2FailureStatus.setStatus(_A)
class _Power2FailureAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ack',1))
_Power2FailureAck_Type.__name__=_C
_Power2FailureAck_Object=MibScalar
power2FailureAck=_Power2FailureAck_Object((1,3,6,1,4,1,8691,2,21,1,8,8,4),_Power2FailureAck_Type())
power2FailureAck.setMaxAccess(_B)
if mibBuilder.loadTexts:power2FailureAck.setStatus(_A)
class _HostConnectionLostAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('na',0),('non',1),(_AG,2)))
_HostConnectionLostAlarmStatus_Type.__name__=_C
_HostConnectionLostAlarmStatus_Object=MibScalar
hostConnectionLostAlarmStatus=_HostConnectionLostAlarmStatus_Object((1,3,6,1,4,1,8691,2,21,1,8,8,5),_HostConnectionLostAlarmStatus_Type())
hostConnectionLostAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hostConnectionLostAlarmStatus.setStatus(_A)
class _HostConnectionLostAlarmClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_HostConnectionLostAlarmClear_Type.__name__=_C
_HostConnectionLostAlarmClear_Object=MibScalar
hostConnectionLostAlarmClear=_HostConnectionLostAlarmClear_Object((1,3,6,1,4,1,8691,2,21,1,8,8,6),_HostConnectionLostAlarmClear_Type())
hostConnectionLostAlarmClear.setMaxAccess(_B)
if mibBuilder.loadTexts:hostConnectionLostAlarmClear.setStatus(_A)
_ActivateSettings_ObjectIdentity=ObjectIdentity
activateSettings=_ActivateSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,9))
class _DoActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('activate',1))
_DoActivate_Type.__name__=_C
_DoActivate_Object=MibScalar
doActivate=_DoActivate_Object((1,3,6,1,4,1,8691,2,21,1,9,1),_DoActivate_Type())
doActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:doActivate.setStatus(_A)
_Restart_ObjectIdentity=ObjectIdentity
restart=_Restart_ObjectIdentity((1,3,6,1,4,1,8691,2,21,1,10))
class _RestartPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('port1',0),('port2',1)))
_RestartPorts_Type.__name__=_C
_RestartPorts_Object=MibScalar
restartPorts=_RestartPorts_Object((1,3,6,1,4,1,8691,2,21,1,10,1),_RestartPorts_Type())
restartPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:restartPorts.setStatus(_A)
class _RestartSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_RestartSystem_Type.__name__=_C
_RestartSystem_Object=MibScalar
restartSystem=_RestartSystem_Object((1,3,6,1,4,1,8691,2,21,1,10,2),_RestartSystem_Type())
restartSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:restartSystem.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'PortList':PortList,'moxa':moxa,'nport':nport,'iaw5x50AIO':iaw5x50AIO,'swMgmt':swMgmt,'overview':overview,'modelName':modelName,'serialNumber':serialNumber,'firmwareVersion':firmwareVersion,'ethIPAddress':ethIPAddress,'ethMacAddress':ethMacAddress,'wlanIPAddress':wlanIPAddress,'wlanMacAddress':wlanMacAddress,'wlanSSID':wlanSSID,'wlanNetworkType':wlanNetworkType,'wlanSecurityMode':wlanSecurityMode,'wlanRFType':wlanRFType,'wlanCountryCode':wlanCountryCode,'wlanFastRoaming':wlanFastRoaming,'activeNetworkPort':activeNetworkPort,'upTime':upTime,'serialPort1':serialPort1,'serialPort2':serialPort2,'basicSetting':basicSetting,'serverSetting':serverSetting,'serverName':serverName,'serverLocation':serverLocation,'enableServerSocketIdleConnectionTimeout':enableServerSocketIdleConnectionTimeout,'serverSocketIdleConnectionTimeoutInterval':serverSocketIdleConnectionTimeoutInterval,'enableCommunicationWatchdogTimeout':enableCommunicationWatchdogTimeout,'communicationWatchdogTimeout':communicationWatchdogTimeout,'timeSetting':timeSetting,'timeZone':timeZone,'localTime':localTime,'timeServer':timeServer,'networkSetting':networkSetting,'generalSetting':generalSetting,'dnsServer1IpAddr':dnsServer1IpAddr,'dnsServer2IpAddr':dnsServer2IpAddr,'ethernetSetting':ethernetSetting,'ethIpConfiguration':ethIpConfiguration,'ethIpAddress':ethIpAddress,'ethNetMask':ethNetMask,'ethDefaultGateway':ethDefaultGateway,'ethBridgeMode':ethBridgeMode,'wlanSetting':wlanSetting,'wlanIpConfiguration':wlanIpConfiguration,'wlanIpAddress':wlanIpAddress,'wlanNetMask':wlanNetMask,'wlanDefaultGateway':wlanDefaultGateway,'profileSetting':profileSetting,'networkType':networkType,'adhocProfile':adhocProfile,'adhocGeneralSetting':adhocGeneralSetting,'adhocProfileName':adhocProfileName,'adhocRFType':adhocRFType,'adhocWlanSSID':adhocWlanSSID,'adhocChannel':adhocChannel,'adhocSecuritySetting':adhocSecuritySetting,'adhocAuthentication':adhocAuthentication,'adhocEncryption':adhocEncryption,'adhocWepKeyLength':adhocWepKeyLength,'adhocWepKeyIndex':adhocWepKeyIndex,'adhocWepKeyPassphrase':adhocWepKeyPassphrase,'adhocWepKeyFormat':adhocWepKeyFormat,'infrastructureProfile':infrastructureProfile,'infraGeneralSetting':infraGeneralSetting,'infraGeneralSettingTable':infraGeneralSettingTable,'infraGeneralSettingEntry':infraGeneralSettingEntry,_b:profileIndex,'profileName':profileName,'profileRFType':profileRFType,'profileWlanSSID':profileWlanSSID,'securitySetting':securitySetting,'securitySettingTable':securitySettingTable,'securitySettingEntry':securitySettingEntry,'authentication':authentication,'encryption':encryption,'wepKeyLength':wepKeyLength,'wepKeyIndex':wepKeyIndex,'wepKeyPassphrase':wepKeyPassphrase,'wepKeyFormat':wepKeyFormat,'eapMethod':eapMethod,'tunneledAuth':tunneledAuth,'wpaUsername':wpaUsername,'wpaAnonymousUsername':wpaAnonymousUsername,'verifyServerCert':verifyServerCert,'trustedServerCert':trustedServerCert,'userCert':userCert,'userPrivateKey':userPrivateKey,'fastRoamingSetting':fastRoamingSetting,'fastRoamingScanChannels1':fastRoamingScanChannels1,'fastRoamingScanChannels2':fastRoamingScanChannels2,'fastRoamingScanChannels3':fastRoamingScanChannels3,'fastRoamingThreshold':fastRoamingThreshold,'fastRoamingDifference':fastRoamingDifference,'wlanLogSetting':wlanLogSetting,'wlanLogEnable':wlanLogEnable,'advancedSetting':advancedSetting,'gratuitousArp':gratuitousArp,'gratuitousArpSendPeriod':gratuitousArpSendPeriod,'gratuitousArpIpAddress1':gratuitousArpIpAddress1,'gratuitousArpMacAddress1':gratuitousArpMacAddress1,'gratuitousArpIpAddress2':gratuitousArpIpAddress2,'gratuitousArpMacAddress2':gratuitousArpMacAddress2,'gratuitousArpIpAddress3':gratuitousArpIpAddress3,'gratuitousArpMacAddress3':gratuitousArpMacAddress3,'gratuitousArpIpAddress4':gratuitousArpIpAddress4,'gratuitousArpMacAddress4':gratuitousArpMacAddress4,'portSetting':portSetting,'opModeSetting':opModeSetting,'opMode':opMode,'opModePortTable':opModePortTable,'opModePortEntry':opModePortEntry,_H:portIndex,'portMode':portMode,'opModeParam':opModeParam,'realCOM':realCOM,'realCOMTable':realCOMTable,'realCOMEntry':realCOMEntry,'realCOMTcpAliveCheck':realCOMTcpAliveCheck,'realCOMMaxConnection':realCOMMaxConnection,'realCOMIgnoreJammedIp':realCOMIgnoreJammedIp,'realCOMAllowDriverControl':realCOMAllowDriverControl,'realCOMConnectionDownRTS':realCOMConnectionDownRTS,'realCOMConnectionDownDTR':realCOMConnectionDownDTR,'rfc2217':rfc2217,'rfc2217Table':rfc2217Table,'rfc2217Entry':rfc2217Entry,'rfc2217TcpAliveCheck':rfc2217TcpAliveCheck,'rfc2217TcpPort':rfc2217TcpPort,'tcpServer':tcpServer,'tcpServerTable':tcpServerTable,'tcpServerEntry':tcpServerEntry,'tcpServerTcpAliveCheck':tcpServerTcpAliveCheck,'tcpServerInactivityTime':tcpServerInactivityTime,'tcpServerMaxConnection':tcpServerMaxConnection,'tcpServerIgnoreJammedIp':tcpServerIgnoreJammedIp,'tcpServerAllowDriverControl':tcpServerAllowDriverControl,'tcpServerTcpPort':tcpServerTcpPort,'tcpServerCmdPort':tcpServerCmdPort,'tcpServerConnectionDownRTS':tcpServerConnectionDownRTS,'tcpServerConnectionDownDTR':tcpServerConnectionDownDTR,'tcpClient':tcpClient,'tcpClientTable':tcpClientTable,'tcpClientEntry':tcpClientEntry,'tcpClientTcpAliveCheck':tcpClientTcpAliveCheck,'tcpClientInactivityTime':tcpClientInactivityTime,'tcpClientIgnoreJammedIp':tcpClientIgnoreJammedIp,'tcpClientDestinationAddress1':tcpClientDestinationAddress1,'tcpClientDestinationPort1':tcpClientDestinationPort1,'tcpClientDestinationAddress2':tcpClientDestinationAddress2,'tcpClientDestinationPort2':tcpClientDestinationPort2,'tcpClientDestinationAddress3':tcpClientDestinationAddress3,'tcpClientDestinationPort3':tcpClientDestinationPort3,'tcpClientDestinationAddress4':tcpClientDestinationAddress4,'tcpClientDestinationPort4':tcpClientDestinationPort4,'tcpClientDesignatedLocalPort1':tcpClientDesignatedLocalPort1,'tcpClientDesignatedLocalPort2':tcpClientDesignatedLocalPort2,'tcpClientDesignatedLocalPort3':tcpClientDesignatedLocalPort3,'tcpClientDesignatedLocalPort4':tcpClientDesignatedLocalPort4,'tcpClientConnectionControl':tcpClientConnectionControl,'udp':udp,'udpTable':udpTable,'udpEntry':udpEntry,'udpDestinationAddress1Begin':udpDestinationAddress1Begin,'udpDestinationAddress1End':udpDestinationAddress1End,'udpDestinationPort1':udpDestinationPort1,'udpDestinationAddress2Begin':udpDestinationAddress2Begin,'udpDestinationAddress2End':udpDestinationAddress2End,'udpDestinationPort2':udpDestinationPort2,'udpDestinationAddress3Begin':udpDestinationAddress3Begin,'udpDestinationAddress3End':udpDestinationAddress3End,'udpDestinationPort3':udpDestinationPort3,'udpDestinationAddress4Begin':udpDestinationAddress4Begin,'udpDestinationAddress4End':udpDestinationAddress4End,'udpDestinationPort4':udpDestinationPort4,'udpLocalListenPort':udpLocalListenPort,'pairConnectionMaster':pairConnectionMaster,'pairConnectionMasterTable':pairConnectionMasterTable,'pairConnectionMasterEntry':pairConnectionMasterEntry,'pairConnectionMasterTcpAliveCheck':pairConnectionMasterTcpAliveCheck,'pairConnectionMasterDestnationAddress':pairConnectionMasterDestnationAddress,'pairConnectionMasterDestnationTcpPort':pairConnectionMasterDestnationTcpPort,'pairConnectionSlave':pairConnectionSlave,'pairConnectionSlaveTable':pairConnectionSlaveTable,'pairConnectionSlaveEntry':pairConnectionSlaveEntry,'pairConnectionSlaveTcpAliveCheck':pairConnectionSlaveTcpAliveCheck,'pairConnectionSlaveLocalTcpPort':pairConnectionSlaveLocalTcpPort,'ethernetModem':ethernetModem,'ethernetModemTable':ethernetModemTable,'ethernetModemEntry':ethernetModemEntry,'ethernetModemTcpAliveCheck':ethernetModemTcpAliveCheck,'ethernetModemLocalTcpPort':ethernetModemLocalTcpPort,'reverseTerminal':reverseTerminal,'reverseTerminalTable':reverseTerminalTable,'reverseTerminalEntry':reverseTerminalEntry,'reverseTerminalTcpAliveCheck':reverseTerminalTcpAliveCheck,'reverseTerminalInactivityTime':reverseTerminalInactivityTime,'reverseTerminalTcpPort':reverseTerminalTcpPort,'reverseTerminalAuthenticationType':reverseTerminalAuthenticationType,'reverseTerminalMapKeys':reverseTerminalMapKeys,'dataPacking':dataPacking,'dataPackingPortTable':dataPackingPortTable,'dataPackingPortEntry':dataPackingPortEntry,'portPacketLength':portPacketLength,'portDelimiter1Enable':portDelimiter1Enable,'portDelimiter1':portDelimiter1,'portDelimiter2Enable':portDelimiter2Enable,'portDelimiter2':portDelimiter2,'portDelimiterProcess':portDelimiterProcess,'portForceTransmit':portForceTransmit,'comParamSetting':comParamSetting,'comParamPortTable':comParamPortTable,'comParamPortEntry':comParamPortEntry,'portAlias':portAlias,'portInterface':portInterface,'portBaudRate':portBaudRate,'portDataBits':portDataBits,'portStopBits':portStopBits,'portParity':portParity,'portFlowControl':portFlowControl,'portFIFO':portFIFO,'dataBuffering':dataBuffering,'dataBufferingPortTable':dataBufferingPortTable,'dataBufferingPortEntry':dataBufferingPortEntry,'portBufferingEnable':portBufferingEnable,'portSerialDataLoggingEnable':portSerialDataLoggingEnable,'modbusAddressMapping':modbusAddressMapping,'userDefinedModbusAddress':userDefinedModbusAddress,'enableUserDefinedModbus':enableUserDefinedModbus,'doValueStartAddress':doValueStartAddress,'doValueFunctionCode':doValueFunctionCode,'doValueReadWrite':doValueReadWrite,'doValueReferenceAddress':doValueReferenceAddress,'doValueTotalchannels':doValueTotalchannels,'doValueDatatype':doValueDatatype,'doPulseStatusStartAddress':doPulseStatusStartAddress,'doPulseStatusFunctionCode':doPulseStatusFunctionCode,'doPulseStatusReadWrite':doPulseStatusReadWrite,'doPulseStatusReferenceAddress':doPulseStatusReferenceAddress,'doPulseStatusTotalchannels':doPulseStatusTotalchannels,'doPulseStatusDatatype':doPulseStatusDatatype,'doValueAllChannelStartAddress':doValueAllChannelStartAddress,'doValueAllChannelFunctionCode':doValueAllChannelFunctionCode,'doValueAllChannelReadWrite':doValueAllChannelReadWrite,'doValueAllChannelReferenceAddress':doValueAllChannelReferenceAddress,'doValueAllChannelTotalchannels':doValueAllChannelTotalchannels,'doValueAllChannelDatatype':doValueAllChannelDatatype,'diValueStartAddress':diValueStartAddress,'diValueFunctionCode':diValueFunctionCode,'diValueReadWrite':diValueReadWrite,'diValueReferenceAddress':diValueReferenceAddress,'diValueTotalchannels':diValueTotalchannels,'diValueDatatype':diValueDatatype,'diCounterValueStartAddress':diCounterValueStartAddress,'diCounterValueFunctionCode':diCounterValueFunctionCode,'diCounterValueReadWrite':diCounterValueReadWrite,'diCounterValueReferenceAddress':diCounterValueReferenceAddress,'diCounterValueTotalchannels':diCounterValueTotalchannels,'diCounterValueDatatype':diCounterValueDatatype,'diValueAllChannelStartAddress':diValueAllChannelStartAddress,'diValueAllChannelFunctionCode':diValueAllChannelFunctionCode,'diValueAllChannelReadWrite':diValueAllChannelReadWrite,'diValueAllChannelReferenceAddress':diValueAllChannelReferenceAddress,'diValueAllChannelTotalchannels':diValueAllChannelTotalchannels,'diValueAllChannelDatatype':diValueAllChannelDatatype,'diCounterStartStartAddress':diCounterStartStartAddress,'diCounterStartFunctionCode':diCounterStartFunctionCode,'diCounterStartReadWrite':diCounterStartReadWrite,'diCounterStartReferenceAddress':diCounterStartReferenceAddress,'diCounterStartTotalchannels':diCounterStartTotalchannels,'diCounterStartDatatype':diCounterStartDatatype,'diCounterClearStartAddress':diCounterClearStartAddress,'diCounterClearFunctionCode':diCounterClearFunctionCode,'diCounterClearReadWrite':diCounterClearReadWrite,'diCounterClearReferenceAddress':diCounterClearReferenceAddress,'diCounterClearTotalchannels':diCounterClearTotalchannels,'diCounterClearDatatype':diCounterClearDatatype,'userDefModbusLoadDefault':userDefModbusLoadDefault,'defaultModbusAddress':defaultModbusAddress,'defaultDOValueStartAddress':defaultDOValueStartAddress,'defaultDOValueFunctionCode':defaultDOValueFunctionCode,'defaultDOValueReadWrite':defaultDOValueReadWrite,'defaultDOValueReferenceAddress':defaultDOValueReferenceAddress,'defaultDOValueTotalchannels':defaultDOValueTotalchannels,'defaultDOValueDatatype':defaultDOValueDatatype,'defaultDOPulseStatusStartAddress':defaultDOPulseStatusStartAddress,'defaultDOPulseStatusFunctionCode':defaultDOPulseStatusFunctionCode,'defaultDOPulseStatusReadWrite':defaultDOPulseStatusReadWrite,'defaultDOPulseStatusReferenceAddress':defaultDOPulseStatusReferenceAddress,'defaultDOPulseStatusTotalchannels':defaultDOPulseStatusTotalchannels,'defaultDOPulseStatusDatatype':defaultDOPulseStatusDatatype,'defaultDOValueAllChannelStartAddress':defaultDOValueAllChannelStartAddress,'defaultDOValueAllChannelFunctionCode':defaultDOValueAllChannelFunctionCode,'defaultDOValueAllChannelReadWrite':defaultDOValueAllChannelReadWrite,'defaultDOValueAllChannelReferenceAddress':defaultDOValueAllChannelReferenceAddress,'defaultDOValueAllChannelTotalchannels':defaultDOValueAllChannelTotalchannels,'defaultDOValueAllChannelDatatype':defaultDOValueAllChannelDatatype,'defaultDIValueStartAddress':defaultDIValueStartAddress,'defaultDIValueFunctionCode':defaultDIValueFunctionCode,'defaultDIValueReadWrite':defaultDIValueReadWrite,'defaultDIValueReferenceAddress':defaultDIValueReferenceAddress,'defaultDIValueTotalchannels':defaultDIValueTotalchannels,'defaultDIValueDatatype':defaultDIValueDatatype,'defaultDICounterValueStartAddress':defaultDICounterValueStartAddress,'defaultDICounterValueFunctionCode':defaultDICounterValueFunctionCode,'defaultDICounterValueReadWrite':defaultDICounterValueReadWrite,'defaultDICounterValueReferenceAddress':defaultDICounterValueReferenceAddress,'defaultDICounterValueTotalchannels':defaultDICounterValueTotalchannels,'defaultDICounterValueDatatype':defaultDICounterValueDatatype,'defaultDIValueAllChannelStartAddress':defaultDIValueAllChannelStartAddress,'defaultDIValueAllChannelFunctionCode':defaultDIValueAllChannelFunctionCode,'defaultDIValueAllChannelReadWrite':defaultDIValueAllChannelReadWrite,'defaultDIValueAllChannelReferenceAddress':defaultDIValueAllChannelReferenceAddress,'defaultDIValueAllChannelTotalchannels':defaultDIValueAllChannelTotalchannels,'defaultDIValueAllChannelDatatype':defaultDIValueAllChannelDatatype,'defaultDICounterStartStartAddress':defaultDICounterStartStartAddress,'defaultDICounterStartFunctionCode':defaultDICounterStartFunctionCode,'defaultDICounterStartReadWrite':defaultDICounterStartReadWrite,'defaultDICounterStartReferenceAddress':defaultDICounterStartReferenceAddress,'defaultDICounterStartTotalchannels':defaultDICounterStartTotalchannels,'defaultDICounterStartDatatype':defaultDICounterStartDatatype,'defaultDICounterClearStartAddress':defaultDICounterClearStartAddress,'defaultDICounterClearFunctionCode':defaultDICounterClearFunctionCode,'defaultDICounterClearReadWrite':defaultDICounterClearReadWrite,'defaultDICounterClearReferenceAddress':defaultDICounterClearReferenceAddress,'defaultDICounterClearTotalchannels':defaultDICounterClearTotalchannels,'defaultDICounterClearDatatype':defaultDICounterClearDatatype,'ioSetting':ioSetting,'diSetting':diSetting,'diTable':diTable,'diEntry':diEntry,'diIndex':diIndex,'diMode':diMode,'diStatus':diStatus,'diFilter':diFilter,'diTrigger':diTrigger,'diCntStart':diCntStart,'doSetting':doSetting,'doTable':doTable,'doEntry':doEntry,'doIndex':doIndex,'doMode':doMode,'doStatus':doStatus,'doPulseOnWidth':doPulseOnWidth,'doPulseOffWidth':doPulseOffWidth,'doPulseStart':doPulseStart,'sysManagement':sysManagement,'miscNetworkSettings':miscNetworkSettings,'accessibleIp':accessibleIp,'enableAccessibleIpList':enableAccessibleIpList,'accessibleIpListTable':accessibleIpListTable,'accessibleIpListEntry':accessibleIpListEntry,_AM:accessibleIpListIndex,'activeAccessibleIpList':activeAccessibleIpList,'accessibleIpListAddress':accessibleIpListAddress,'accessibleIpListNetmask':accessibleIpListNetmask,'snmpAgentSettings':snmpAgentSettings,'snmpEnable':snmpEnable,'snmpContactName':snmpContactName,'snmpLocation':snmpLocation,'authenticationServer':authenticationServer,'radiusServerIp':radiusServerIp,'udpPortAuthenticationServer':udpPortAuthenticationServer,'radiusAccounting':radiusAccounting,'sysLogSettings':sysLogSettings,'sysLocalLog':sysLocalLog,'networkLocalLog':networkLocalLog,'configLocalLog':configLocalLog,'opModeLocalLog':opModeLocalLog,'autoWarningSettings':autoWarningSettings,'eventSettings':eventSettings,'mailWarningColdStart':mailWarningColdStart,'mailWarningWarmStart':mailWarningWarmStart,'mailWarningPower1InputFailure':mailWarningPower1InputFailure,'mailWarningPower2InputFailure':mailWarningPower2InputFailure,'mailWarningAuthFailure':mailWarningAuthFailure,'mailWarningIpChanged':mailWarningIpChanged,'mailWarningPasswordChanged':mailWarningPasswordChanged,'trapServerColdStart':trapServerColdStart,'trapServerWarmStart':trapServerWarmStart,'trapServerAuthFailure':trapServerAuthFailure,'relayOutputPower1InputFailure':relayOutputPower1InputFailure,'relayOutputPower2InputFailure':relayOutputPower2InputFailure,'relayOutputEthernetLinkDown':relayOutputEthernetLinkDown,'serialEventSettings':serialEventSettings,'portEventSettingsTable':portEventSettingsTable,'portEventSettingsEntry':portEventSettingsEntry,'mailDCDchange':mailDCDchange,'trapDCDchange':trapDCDchange,'mailDSRchange':mailDSRchange,'trapDSRchange':trapDSRchange,'ioEventSettings':ioEventSettings,'diEventSettingsTable':diEventSettingsTable,'diEventSettingsEntry':diEventSettingsEntry,'diEventIndex':diEventIndex,'diEventTrap':diEventTrap,'doEventSettingsTable':doEventSettingsTable,'doEventSettingsEntry':doEventSettingsEntry,'doEventIndex':doEventIndex,'doEventTrap':doEventTrap,'emailAlert':emailAlert,'emailWarningMailServer':emailWarningMailServer,'emailRequiresAuthentication':emailRequiresAuthentication,'emailWarningUserName':emailWarningUserName,'emailWarningFromEmail':emailWarningFromEmail,'emailWarningFirstEmailAddr':emailWarningFirstEmailAddr,'emailWarningSecondEmailAddr':emailWarningSecondEmailAddr,'emailWarningThirdEmailAddr':emailWarningThirdEmailAddr,'emailWarningFourthEmailAddr':emailWarningFourthEmailAddr,'snmpTrap':snmpTrap,'snmpTrapReceiverIp':snmpTrapReceiverIp,'trapVersion':trapVersion,'maintenance':maintenance,'consoleSettings':consoleSettings,'httpConsole':httpConsole,'httpsConsole':httpsConsole,'telnetConsole':telnetConsole,'sshConsole':sshConsole,'serialConsole':serialConsole,'resetButton':resetButton,'loadFactoryDefault':loadFactoryDefault,'loadFactoryDefaultSetting':loadFactoryDefaultSetting,'sdBackup':sdBackup,'autoLoadSdConfiguration':autoLoadSdConfiguration,'sysStatus':sysStatus,'s2eConnections':s2eConnections,'monitorRemoteIpTable':monitorRemoteIpTable,'monitorRemoteIpEntry':monitorRemoteIpEntry,_AN:remoteIpIndex,'monitorRemoteIp':monitorRemoteIp,'serialPortStatus':serialPortStatus,'monitorSerialPortStatusTable':monitorSerialPortStatusTable,'monitorSerialPortStatusEntry':monitorSerialPortStatusEntry,'monitorTxCount':monitorTxCount,'monitorRxCount':monitorRxCount,'monitorTxTotalCount':monitorTxTotalCount,'monitorRxTotalCount':monitorRxTotalCount,'monitorDSR':monitorDSR,'monitorDTR':monitorDTR,'monitorRTS':monitorRTS,'monitorCTS':monitorCTS,'monitorDCD':monitorDCD,'serialPortErrorCount':serialPortErrorCount,'monitorSerialPortErrorCountTable':monitorSerialPortErrorCountTable,'monitorSerialPortErrorCountEntry':monitorSerialPortErrorCountEntry,'monitorErrorCountFrame':monitorErrorCountFrame,'monitorErrorCountParity':monitorErrorCountParity,'monitorErrorCountOverrun':monitorErrorCountOverrun,'monitorErrorCountBreak':monitorErrorCountBreak,'serialPortSettings':serialPortSettings,'monitorSerialPortSettingsTable':monitorSerialPortSettingsTable,'monitorSerialPortSettingsEntry':monitorSerialPortSettingsEntry,'monitorBaudRate':monitorBaudRate,'monitorDataBits':monitorDataBits,'monitorStopBits':monitorStopBits,'monitorParity':monitorParity,'monitorRTSCTSFlowControl':monitorRTSCTSFlowControl,'monitorXONXOFFFlowControl':monitorXONXOFFFlowControl,'monitorFIFO':monitorFIFO,'monitorInterface':monitorInterface,'serialPortBuffering':serialPortBuffering,'monitorSerialPortBufferingTable':monitorSerialPortBufferingTable,'monitorSerialPortBufferingEntry':monitorSerialPortBufferingEntry,'monitorBuffering':monitorBuffering,'sysWlanStatus':sysWlanStatus,'wlanStatusActiveProfileName':wlanStatusActiveProfileName,'wlanStatusIpConfiguration':wlanStatusIpConfiguration,'wlanStatusIpAddress':wlanStatusIpAddress,'wlanStatusNetMask':wlanStatusNetMask,'wlanStatusDefaultGateway':wlanStatusDefaultGateway,'wlanStatusNetworkType':wlanStatusNetworkType,'wlanStatusRFType':wlanStatusRFType,'wlanStatusSSID':wlanStatusSSID,'wlanStatusChannel':wlanStatusChannel,'wlanStatusAuthentication':wlanStatusAuthentication,'wlanStatusEncryption':wlanStatusEncryption,'wlanStatusRegion':wlanStatusRegion,'wlanStatusSignalStrength':wlanStatusSignalStrength,'wlanStatusConnectionSpeed':wlanStatusConnectionSpeed,'wlanStatusCurrentBSSID':wlanStatusCurrentBSSID,'ioStatus':ioStatus,'diIoStatus':diIoStatus,'diMonTable':diMonTable,'diMonEntry':diMonEntry,_AO:diMonIndex,'diMonMode':diMonMode,'diMonStatus':diMonStatus,'diMonFilter':diMonFilter,'diMonTrigger':diMonTrigger,'diMonCntStart':diMonCntStart,'doIoStatus':doIoStatus,'doMonTable':doMonTable,'doMonEntry':doMonEntry,_AP:doMonIndex,'doMonMode':doMonMode,'doMonStatus':doMonStatus,'doMonPulseOnWidth':doMonPulseOnWidth,'doMonPulseOffWidth':doMonPulseOffWidth,'doMonPulseStart':doMonPulseStart,'sysAlertStatus':sysAlertStatus,'power1FailureStatus':power1FailureStatus,'power1FailureAck':power1FailureAck,'power2FailureStatus':power2FailureStatus,'power2FailureAck':power2FailureAck,'hostConnectionLostAlarmStatus':hostConnectionLostAlarmStatus,'hostConnectionLostAlarmClear':hostConnectionLostAlarmClear,'activateSettings':activateSettings,'doActivate':doActivate,'restart':restart,'restartPorts':restartPorts,'restartSystem':restartSystem})