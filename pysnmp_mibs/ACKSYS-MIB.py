_Aw='nbEventState'
_Av='nbClientMacAddress'
_Au='configProfileIconName'
_At='configProfileOsuProviderName'
_As='configProfileOperClassName'
_Ar='configProfileWanMetricsName'
_Aq='configProfileConnCapName'
_Ap='configProfileOperFriendlyNameName'
_Ao='configProfileOverrideElementName'
_An='configProfileNaiRealmName'
_Am='configProfile3gppCellNetName'
_Al='configProfileDomainNameName'
_Ak='configProfileIpAddrTypeAvailName'
_Aj='configProfileNetworkAuthTypeName'
_Ai='configProfileRoamingConsortiumName'
_Ah='configProfileVenueName'
_Ag='configPasspointConfigName'
_Af='configDhcpSubnet'
_Ae='gpioOutIndex'
_Ad='gpioInIndex'
_Ac='snmpAgentOIDIndex'
_Ab='configIfSrccName'
_Aa='configIfVlanIndex'
_AZ='configIfBridgeName'
_AY='configIfMeshName'
_AX='configIfAPName'
_AW='configIfStaName'
_AV='configInterfaceName'
_AU='configFilterGroupRuleIndex'
_AT='configFilterGroupIndex'
_AS='configRadiusIndex'
_AR='configPhyCellName'
_AQ='configPhyWifiName'
_AP='configIpDscpTaggingIndex'
_AO='configIpZoneForwardIndex'
_AN='configIpRoutesIndex'
_AM='configIpFirewallIndex'
_AL='configIpNatIpForwardIndex'
_AK='configIpZoneIndex'
_AJ='configIpSubnetName'
_AI='statusPhyCellIndex'
_AH='statusMeshSurveyIndex'
_AG='statusPhyLanIndex'
_AF='statusAssociationIndex'
_AE='statusSpanningTreePortName'
_AD='statusSpanningTreePortBridgeName'
_AC='statusSpanningTreeBridgeName'
_AB='statusPhyWifiScanTableIndex'
_AA='statusPhyWifiIndex'
_A9='undefined'
_A8='statusIfWlanIndex'
_A7='statusIpSubnetIndex'
_A6='millisecond'
_A5='apClientFilteringListId'
_A4='clientMacAddr'
_A3='bridgeNatPortForwardingListId'
_A2='bridgeWirelessScanAPMac'
_A1='bridgeAPFilteringListId'
_A0='infrastructure'
_z='access-point'
_y='PhysAddress'
_x='DisplayString'
_w='destination'
_v='source'
_u='nofilter'
_t='all'
_s='disabled'
_r='connected'
_q='not-connected'
_p='flowControl'
_o='outputFlow'
_n='modem'
_m='wpa'
_l='wpa3'
_k='icmp'
_j='udp'
_i='tcp'
_h='inputFlow'
_g='powerOn'
_f='powerOff'
_e='dhcp'
_d='static'
_c='on'
_b='a-only'
_a='mixed-b-g'
_Z='g-only'
_Y='b-only'
_X='off'
_W='invalid'
_V='low'
_U='high'
_T='ignore'
_S='variable'
_R='fixed'
_Q='true'
_P='false'
_O='default'
_N='none'
_M='nbEventName'
_L='ack'
_K='obsolete'
_J='enable'
_I='accessible-for-notify'
_H='disable'
_G='read-create'
_F='OctetString'
_E='ACKSYS-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_x,_y,'RowStatus','TextualConvention','TruthValue')
acksys=ModuleIdentity((1,3,6,1,4,1,28097))
if mibBuilder.loadTexts:acksys.setRevisions(('2022-02-18 15:05','2021-07-02 11:13'))
class PhysAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class WifiFlavor(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,10,11,12,16)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),('n-g',10),('n-bg',11),('n-a',12),('ac',16)))
class NetifName(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class SecurityModes(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),('wep',2),('wpa-wpa2-psk',3),('wpa-wpa2',4),('sae-wpa3-psk',5),(_l,6),('owe',7)))
class CellSecurityProtocol(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('pap',1),('chap',2)))
class PeapSecurityProtocol(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('peap-pap',1),('peap-chap',2),('peap-mschap',3),('peap-mschapv2',4)))
class WpaVersions(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_m,1),('wpa2',2),('wpa-wpa2-mixed',3),(_l,4),('wpa2-wpa3-mixed',5)))
class CipherTypes(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tkip',1),('aes',2),('aestkip',3)))
class WepKeys(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,26))
class WifiLevel(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,0))
class DisableEnable(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
class TriState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_H,1),(_J,2)))
class AsyncSetStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('set-init',0),('set-more',1),('set-wait',2),('set-ok',3),('set-fail',4)))
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class PortId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class CellAttachMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('reg-hung',0),('reg-home',1),('reg-searching',2),('reg-denied',3),('reg-noCell',4),('reg-roaming',5),('reg-homeSMS',6),('reg-roamingSMS',7),('reg-emgOnly',8),('reg-homeNoCSFB',9),('reg-roamingNoCSFB',10)))
class CellAccessTech(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('at-gsm',0),('at-gsmCompact',1),('at-UTRAN',2),('at-EGPRS',3),('at-HSDPA',4),('at-HSUPA',5),('at-HSPA',6),('at-EUTRAN',7),('at-GSM-IoT',8),('at-EUTRAN-NB-S1',9)))
_Network_product_ObjectIdentity=ObjectIdentity
network_product=_Network_product_ObjectIdentity((1,3,6,1,4,1,28097,1))
_WifiInterface_ObjectIdentity=ObjectIdentity
wifiInterface=_WifiInterface_ObjectIdentity((1,3,6,1,4,1,28097,1,1))
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1))
class _SettingInterfaceSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SettingInterfaceSsid_Type.__name__=_x
_SettingInterfaceSsid_Object=MibScalar
settingInterfaceSsid=_SettingInterfaceSsid_Object((1,3,6,1,4,1,28097,1,1,1,1),_SettingInterfaceSsid_Type())
settingInterfaceSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceSsid.setStatus(_A)
class _SettingInterfaceWifiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),(_z,2)))
_SettingInterfaceWifiMode_Type.__name__=_D
_SettingInterfaceWifiMode_Object=MibScalar
settingInterfaceWifiMode=_SettingInterfaceWifiMode_Object((1,3,6,1,4,1,28097,1,1,1,2),_SettingInterfaceWifiMode_Type())
settingInterfaceWifiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceWifiMode.setStatus(_A)
_SettingInterfaceChannel_Type=Integer32
_SettingInterfaceChannel_Object=MibScalar
settingInterfaceChannel=_SettingInterfaceChannel_Object((1,3,6,1,4,1,28097,1,1,1,3),_SettingInterfaceChannel_Type())
settingInterfaceChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceChannel.setStatus(_A)
class _SettingInterface80211Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,10,11,12)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),('n-g',10),('n-bg',11),('n-a',12)))
_SettingInterface80211Mode_Type.__name__=_D
_SettingInterface80211Mode_Object=MibScalar
settingInterface80211Mode=_SettingInterface80211Mode_Object((1,3,6,1,4,1,28097,1,1,1,4),_SettingInterface80211Mode_Type())
settingInterface80211Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterface80211Mode.setStatus(_A)
class _SettingInterfaceSuper_a_g_Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('super-g-without-turbo',2),('super-g-with-static-turbo',3),('super-g-with-dynamic-turbo',4)))
_SettingInterfaceSuper_a_g_Mode_Type.__name__=_D
_SettingInterfaceSuper_a_g_Mode_Object=MibScalar
settingInterfaceSuper_a_g_Mode=_SettingInterfaceSuper_a_g_Mode_Object((1,3,6,1,4,1,28097,1,1,1,5),_SettingInterfaceSuper_a_g_Mode_Type())
settingInterfaceSuper_a_g_Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceSuper_a_g_Mode.setStatus(_A)
class _SettingEnableRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_c,2)))
_SettingEnableRadio_Type.__name__=_D
_SettingEnableRadio_Object=MibScalar
settingEnableRadio=_SettingEnableRadio_Object((1,3,6,1,4,1,28097,1,1,1,6),_SettingEnableRadio_Type())
settingEnableRadio.setMaxAccess(_B)
if mibBuilder.loadTexts:settingEnableRadio.setStatus(_A)
class _SettingTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('medium',2),(_V,3)))
_SettingTxPower_Type.__name__=_D
_SettingTxPower_Object=MibScalar
settingTxPower=_SettingTxPower_Object((1,3,6,1,4,1,28097,1,1,1,7),_SettingTxPower_Type())
settingTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:settingTxPower.setStatus(_A)
class _SettingRegion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,5,6,7,10,14,17,18,20,21,22,23,27,28,29,30,31)));namedValues=NamedValues(*(('israel',2),('usa',4),('hong-kong',5),('canada',6),('australia',7),('franceoutdoor',10),('europe',14),('japan',17),('singapore',18),('korea',20),('mexico',21),('indonesia',22),('china',23),('russia',27),('brazil',28),('chile',29),('thailand',30),('peru',31)))
_SettingRegion_Type.__name__=_D
_SettingRegion_Object=MibScalar
settingRegion=_SettingRegion_Object((1,3,6,1,4,1,28097,1,1,1,8),_SettingRegion_Type())
settingRegion.setMaxAccess(_B)
if mibBuilder.loadTexts:settingRegion.setStatus(_A)
_SecuritySettings_ObjectIdentity=ObjectIdentity
securitySettings=_SecuritySettings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9))
_SecurityMode_Type=SecurityModes
_SecurityMode_Object=MibScalar
securityMode=_SecurityMode_Object((1,3,6,1,4,1,28097,1,1,1,9,1),_SecurityMode_Type())
securityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:securityMode.setStatus(_A)
_SecurityWEP_ObjectIdentity=ObjectIdentity
securityWEP=_SecurityWEP_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,2))
_SecurityModeWepKeyLen_Type=Integer32
_SecurityModeWepKeyLen_Object=MibScalar
securityModeWepKeyLen=_SecurityModeWepKeyLen_Object((1,3,6,1,4,1,28097,1,1,1,9,2,1),_SecurityModeWepKeyLen_Type())
securityModeWepKeyLen.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKeyLen.setStatus(_A)
_SecurityModeWepKey_1_Type=WepKeys
_SecurityModeWepKey_1_Object=MibScalar
securityModeWepKey_1=_SecurityModeWepKey_1_Object((1,3,6,1,4,1,28097,1,1,1,9,2,2),_SecurityModeWepKey_1_Type())
securityModeWepKey_1.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_1.setStatus(_A)
_SecurityModeWepKey_2_Type=WepKeys
_SecurityModeWepKey_2_Object=MibScalar
securityModeWepKey_2=_SecurityModeWepKey_2_Object((1,3,6,1,4,1,28097,1,1,1,9,2,3),_SecurityModeWepKey_2_Type())
securityModeWepKey_2.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_2.setStatus(_A)
_SecurityModeWepKey_3_Type=WepKeys
_SecurityModeWepKey_3_Object=MibScalar
securityModeWepKey_3=_SecurityModeWepKey_3_Object((1,3,6,1,4,1,28097,1,1,1,9,2,4),_SecurityModeWepKey_3_Type())
securityModeWepKey_3.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_3.setStatus(_A)
_SecurityModeWepKey_4_Type=WepKeys
_SecurityModeWepKey_4_Object=MibScalar
securityModeWepKey_4=_SecurityModeWepKey_4_Object((1,3,6,1,4,1,28097,1,1,1,9,2,5),_SecurityModeWepKey_4_Type())
securityModeWepKey_4.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_4.setStatus(_A)
_SecurityModeDefaultWepKey_Type=Integer32
_SecurityModeDefaultWepKey_Object=MibScalar
securityModeDefaultWepKey=_SecurityModeDefaultWepKey_Object((1,3,6,1,4,1,28097,1,1,1,9,2,6),_SecurityModeDefaultWepKey_Type())
securityModeDefaultWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeDefaultWepKey.setStatus(_A)
class _SecurityModeWepAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('shared',2)))
_SecurityModeWepAuthentication_Type.__name__=_D
_SecurityModeWepAuthentication_Object=MibScalar
securityModeWepAuthentication=_SecurityModeWepAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,2,7),_SecurityModeWepAuthentication_Type())
securityModeWepAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepAuthentication.setStatus(_A)
_SecurityWPA_WPA2_ObjectIdentity=ObjectIdentity
securityWPA_WPA2=_SecurityWPA_WPA2_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3))
_SecurityPresharedKey_ObjectIdentity=ObjectIdentity
securityPresharedKey=_SecurityPresharedKey_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,1))
class _SecurityModeWpaPresharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_SecurityModeWpaPresharedKey_Type.__name__=_F
_SecurityModeWpaPresharedKey_Object=MibScalar
securityModeWpaPresharedKey=_SecurityModeWpaPresharedKey_Object((1,3,6,1,4,1,28097,1,1,1,9,3,1,1),_SecurityModeWpaPresharedKey_Type())
securityModeWpaPresharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWpaPresharedKey.setStatus(_A)
_SecurityRadius_ObjectIdentity=ObjectIdentity
securityRadius=_SecurityRadius_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,2))
_SecurityModeWPARadiusAuthenticationTimeout_Type=Integer32
_SecurityModeWPARadiusAuthenticationTimeout_Object=MibScalar
securityModeWPARadiusAuthenticationTimeout=_SecurityModeWPARadiusAuthenticationTimeout_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,1),_SecurityModeWPARadiusAuthenticationTimeout_Type())
securityModeWPARadiusAuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAuthenticationTimeout.setStatus(_K)
_SecurityModeWPARadiusIP_Type=IpAddress
_SecurityModeWPARadiusIP_Object=MibScalar
securityModeWPARadiusIP=_SecurityModeWPARadiusIP_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,2),_SecurityModeWPARadiusIP_Type())
securityModeWPARadiusIP.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusIP.setStatus(_K)
_SecurityModeWPARadiusPort_Type=Integer32
_SecurityModeWPARadiusPort_Object=MibScalar
securityModeWPARadiusPort=_SecurityModeWPARadiusPort_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,3),_SecurityModeWPARadiusPort_Type())
securityModeWPARadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusPort.setStatus(_K)
class _SecurityModeWPARadiusSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusSecret_Type.__name__=_F
_SecurityModeWPARadiusSecret_Object=MibScalar
securityModeWPARadiusSecret=_SecurityModeWPARadiusSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,4),_SecurityModeWPARadiusSecret_Type())
securityModeWPARadiusSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusSecret.setStatus(_K)
_SecurityModeWPARadiusMacAddressAuthentication_Type=DisableEnable
_SecurityModeWPARadiusMacAddressAuthentication_Object=MibScalar
securityModeWPARadiusMacAddressAuthentication=_SecurityModeWPARadiusMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,5),_SecurityModeWPARadiusMacAddressAuthentication_Type())
securityModeWPARadiusMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusMacAddressAuthentication.setStatus(_K)
_SecurityRadiusAP_ObjectIdentity=ObjectIdentity
securityRadiusAP=_SecurityRadiusAP_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,2,6))
_SecurityModeWPARadiusAPAuthenticationTimeout_Type=Integer32
_SecurityModeWPARadiusAPAuthenticationTimeout_Object=MibScalar
securityModeWPARadiusAPAuthenticationTimeout=_SecurityModeWPARadiusAPAuthenticationTimeout_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,1),_SecurityModeWPARadiusAPAuthenticationTimeout_Type())
securityModeWPARadiusAPAuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAPAuthenticationTimeout.setStatus(_A)
_SecurityModeWPARadiusAPIP_Type=IpAddress
_SecurityModeWPARadiusAPIP_Object=MibScalar
securityModeWPARadiusAPIP=_SecurityModeWPARadiusAPIP_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,2),_SecurityModeWPARadiusAPIP_Type())
securityModeWPARadiusAPIP.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAPIP.setStatus(_A)
_SecurityModeWPARadiusAPPort_Type=Integer32
_SecurityModeWPARadiusAPPort_Object=MibScalar
securityModeWPARadiusAPPort=_SecurityModeWPARadiusAPPort_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,3),_SecurityModeWPARadiusAPPort_Type())
securityModeWPARadiusAPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAPPort.setStatus(_A)
class _SecurityModeWPARadiusAPSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusAPSecret_Type.__name__=_F
_SecurityModeWPARadiusAPSecret_Object=MibScalar
securityModeWPARadiusAPSecret=_SecurityModeWPARadiusAPSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,4),_SecurityModeWPARadiusAPSecret_Type())
securityModeWPARadiusAPSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAPSecret.setStatus(_A)
_SecurityModeWPARadiusAPMacAddressAuthentication_Type=DisableEnable
_SecurityModeWPARadiusAPMacAddressAuthentication_Object=MibScalar
securityModeWPARadiusAPMacAddressAuthentication=_SecurityModeWPARadiusAPMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,5),_SecurityModeWPARadiusAPMacAddressAuthentication_Type())
securityModeWPARadiusAPMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAPMacAddressAuthentication.setStatus(_A)
_SecurityRadiusAPBackup_ObjectIdentity=ObjectIdentity
securityRadiusAPBackup=_SecurityRadiusAPBackup_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6))
_SecurityModeWPABackupRadiusAPIP_Type=IpAddress
_SecurityModeWPABackupRadiusAPIP_Object=MibScalar
securityModeWPABackupRadiusAPIP=_SecurityModeWPABackupRadiusAPIP_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6,1),_SecurityModeWPABackupRadiusAPIP_Type())
securityModeWPABackupRadiusAPIP.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPABackupRadiusAPIP.setStatus(_A)
_SecurityModeWPARadiusBackupAPPort_Type=Integer32
_SecurityModeWPARadiusBackupAPPort_Object=MibScalar
securityModeWPARadiusBackupAPPort=_SecurityModeWPARadiusBackupAPPort_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6,2),_SecurityModeWPARadiusBackupAPPort_Type())
securityModeWPARadiusBackupAPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupAPPort.setStatus(_A)
class _SecurityModeWPARadiusBackupAPSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusBackupAPSecret_Type.__name__=_F
_SecurityModeWPARadiusBackupAPSecret_Object=MibScalar
securityModeWPARadiusBackupAPSecret=_SecurityModeWPARadiusBackupAPSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6,3),_SecurityModeWPARadiusBackupAPSecret_Type())
securityModeWPARadiusBackupAPSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupAPSecret.setStatus(_A)
_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type=DisableEnable
_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Object=MibScalar
securityModeWPABackupRadiusAPMacAddressAuthentication=_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6,4),_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type())
securityModeWPABackupRadiusAPMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPABackupRadiusAPMacAddressAuthentication.setStatus(_A)
_SecurityRadiusBridge_ObjectIdentity=ObjectIdentity
securityRadiusBridge=_SecurityRadiusBridge_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,2,7))
class _SecurityModeWPARadiusLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusLogin_Type.__name__=_F
_SecurityModeWPARadiusLogin_Object=MibScalar
securityModeWPARadiusLogin=_SecurityModeWPARadiusLogin_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,7,1),_SecurityModeWPARadiusLogin_Type())
securityModeWPARadiusLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusLogin.setStatus(_A)
class _SecurityModeWPARadiusPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusPassword_Type.__name__=_F
_SecurityModeWPARadiusPassword_Object=MibScalar
securityModeWPARadiusPassword=_SecurityModeWPARadiusPassword_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,7,2),_SecurityModeWPARadiusPassword_Type())
securityModeWPARadiusPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusPassword.setStatus(_A)
_SecurityBackupRadius_ObjectIdentity=ObjectIdentity
securityBackupRadius=_SecurityBackupRadius_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,3))
_SecurityModeWPABackupRadiusIP_Type=IpAddress
_SecurityModeWPABackupRadiusIP_Object=MibScalar
securityModeWPABackupRadiusIP=_SecurityModeWPABackupRadiusIP_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,1),_SecurityModeWPABackupRadiusIP_Type())
securityModeWPABackupRadiusIP.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPABackupRadiusIP.setStatus(_K)
_SecurityModeWPARadiusBackupPort_Type=Integer32
_SecurityModeWPARadiusBackupPort_Object=MibScalar
securityModeWPARadiusBackupPort=_SecurityModeWPARadiusBackupPort_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,2),_SecurityModeWPARadiusBackupPort_Type())
securityModeWPARadiusBackupPort.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupPort.setStatus(_K)
class _SecurityModeWPARadiusBackupSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusBackupSecret_Type.__name__=_F
_SecurityModeWPARadiusBackupSecret_Object=MibScalar
securityModeWPARadiusBackupSecret=_SecurityModeWPARadiusBackupSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,3),_SecurityModeWPARadiusBackupSecret_Type())
securityModeWPARadiusBackupSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupSecret.setStatus(_K)
_SecurityModeWPABackupRadiusMacAddressAuthentication_Type=DisableEnable
_SecurityModeWPABackupRadiusMacAddressAuthentication_Object=MibScalar
securityModeWPABackupRadiusMacAddressAuthentication=_SecurityModeWPABackupRadiusMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,4),_SecurityModeWPABackupRadiusMacAddressAuthentication_Type())
securityModeWPABackupRadiusMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPABackupRadiusMacAddressAuthentication.setStatus(_K)
class _SecurityModeWpaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),('wpa2',2),(_l,3)))
_SecurityModeWpaMode_Type.__name__=_D
_SecurityModeWpaMode_Object=MibScalar
securityModeWpaMode=_SecurityModeWpaMode_Object((1,3,6,1,4,1,28097,1,1,1,9,3,4),_SecurityModeWpaMode_Type())
securityModeWpaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWpaMode.setStatus(_A)
_SecurityModeWpaCipherType_Type=CipherTypes
_SecurityModeWpaCipherType_Object=MibScalar
securityModeWpaCipherType=_SecurityModeWpaCipherType_Object((1,3,6,1,4,1,28097,1,1,1,9,3,5),_SecurityModeWpaCipherType_Type())
securityModeWpaCipherType.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWpaCipherType.setStatus(_A)
_SecurityModeWpaKeyUpdateInterval_Type=Integer32
_SecurityModeWpaKeyUpdateInterval_Object=MibScalar
securityModeWpaKeyUpdateInterval=_SecurityModeWpaKeyUpdateInterval_Object((1,3,6,1,4,1,28097,1,1,1,9,3,6),_SecurityModeWpaKeyUpdateInterval_Type())
securityModeWpaKeyUpdateInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWpaKeyUpdateInterval.setStatus(_A)
class _SettingAntennaChoice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('diversity',1),('main',2),('aux',3)))
_SettingAntennaChoice_Type.__name__=_D
_SettingAntennaChoice_Object=MibScalar
settingAntennaChoice=_SettingAntennaChoice_Object((1,3,6,1,4,1,28097,1,1,1,10),_SettingAntennaChoice_Type())
settingAntennaChoice.setMaxAccess(_B)
if mibBuilder.loadTexts:settingAntennaChoice.setStatus(_A)
_SettingTransmisionRate_Type=Integer32
_SettingTransmisionRate_Object=MibScalar
settingTransmisionRate=_SettingTransmisionRate_Object((1,3,6,1,4,1,28097,1,1,1,11),_SettingTransmisionRate_Type())
settingTransmisionRate.setMaxAccess(_B)
if mibBuilder.loadTexts:settingTransmisionRate.setStatus(_A)
class _SettingFlagUdapnopassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SettingFlagUdapnopassword_Type.__name__=_D
_SettingFlagUdapnopassword_Object=MibScalar
settingFlagUdapnopassword=_SettingFlagUdapnopassword_Object((1,3,6,1,4,1,28097,1,1,1,12),_SettingFlagUdapnopassword_Type())
settingFlagUdapnopassword.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFlagUdapnopassword.setStatus(_A)
class _SettingFlagFiltersamenet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('different-subnet-filtre',2),('custom-subnet-filtre',3)))
_SettingFlagFiltersamenet_Type.__name__=_D
_SettingFlagFiltersamenet_Object=MibScalar
settingFlagFiltersamenet=_SettingFlagFiltersamenet_Object((1,3,6,1,4,1,28097,1,1,1,13),_SettingFlagFiltersamenet_Type())
settingFlagFiltersamenet.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFlagFiltersamenet.setStatus(_A)
class _SettingFlagFilterframecosom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SettingFlagFilterframecosom_Type.__name__=_D
_SettingFlagFilterframecosom_Object=MibScalar
settingFlagFilterframecosom=_SettingFlagFilterframecosom_Object((1,3,6,1,4,1,28097,1,1,1,14),_SettingFlagFilterframecosom_Type())
settingFlagFilterframecosom.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFlagFilterframecosom.setStatus(_A)
class _SettingDFSsupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SettingDFSsupport_Type.__name__=_D
_SettingDFSsupport_Object=MibScalar
settingDFSsupport=_SettingDFSsupport_Object((1,3,6,1,4,1,28097,1,1,1,15),_SettingDFSsupport_Type())
settingDFSsupport.setMaxAccess(_B)
if mibBuilder.loadTexts:settingDFSsupport.setStatus(_A)
_SettingFilterCustomIpAddr_Type=IpAddress
_SettingFilterCustomIpAddr_Object=MibScalar
settingFilterCustomIpAddr=_SettingFilterCustomIpAddr_Object((1,3,6,1,4,1,28097,1,1,1,16),_SettingFilterCustomIpAddr_Type())
settingFilterCustomIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFilterCustomIpAddr.setStatus(_A)
_SettingFilterCustomSubnetMask_Type=IpAddress
_SettingFilterCustomSubnetMask_Object=MibScalar
settingFilterCustomSubnetMask=_SettingFilterCustomSubnetMask_Object((1,3,6,1,4,1,28097,1,1,1,17),_SettingFilterCustomSubnetMask_Type())
settingFilterCustomSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFilterCustomSubnetMask.setStatus(_A)
_Bridge_mode_ObjectIdentity=ObjectIdentity
bridge_mode=_Bridge_mode_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2))
class _Bridge_modeLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_Bridge_modeLinkStatus_Type.__name__=_D
_Bridge_modeLinkStatus_Object=MibScalar
bridge_modeLinkStatus=_Bridge_modeLinkStatus_Object((1,3,6,1,4,1,28097,1,1,2,1),_Bridge_modeLinkStatus_Type())
bridge_modeLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bridge_modeLinkStatus.setStatus(_A)
_Bridge_modeMacAP_Type=PhysAddress
_Bridge_modeMacAP_Object=MibScalar
bridge_modeMacAP=_Bridge_modeMacAP_Object((1,3,6,1,4,1,28097,1,1,2,2),_Bridge_modeMacAP_Type())
bridge_modeMacAP.setMaxAccess(_C)
if mibBuilder.loadTexts:bridge_modeMacAP.setStatus(_A)
_Bridge_modeRSSI_Type=Gauge32
_Bridge_modeRSSI_Object=MibScalar
bridge_modeRSSI=_Bridge_modeRSSI_Object((1,3,6,1,4,1,28097,1,1,2,3),_Bridge_modeRSSI_Type())
bridge_modeRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:bridge_modeRSSI.setStatus(_A)
_Bridge_modeRSSIdBm_Type=Gauge32
_Bridge_modeRSSIdBm_Object=MibScalar
bridge_modeRSSIdBm=_Bridge_modeRSSIdBm_Object((1,3,6,1,4,1,28097,1,1,2,4),_Bridge_modeRSSIdBm_Type())
bridge_modeRSSIdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:bridge_modeRSSIdBm.setStatus(_A)
_Bridge_modeRSSIPercent_Type=Gauge32
_Bridge_modeRSSIPercent_Object=MibScalar
bridge_modeRSSIPercent=_Bridge_modeRSSIPercent_Object((1,3,6,1,4,1,28097,1,1,2,5),_Bridge_modeRSSIPercent_Type())
bridge_modeRSSIPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:bridge_modeRSSIPercent.setStatus(_A)
_Bridge_modeCurrentTxRate_Type=Integer32
_Bridge_modeCurrentTxRate_Object=MibScalar
bridge_modeCurrentTxRate=_Bridge_modeCurrentTxRate_Object((1,3,6,1,4,1,28097,1,1,2,6),_Bridge_modeCurrentTxRate_Type())
bridge_modeCurrentTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bridge_modeCurrentTxRate.setStatus(_A)
class _Bridge_WirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),('ad-hoc',2)))
_Bridge_WirelessMode_Type.__name__=_D
_Bridge_WirelessMode_Object=MibScalar
bridge_WirelessMode=_Bridge_WirelessMode_Object((1,3,6,1,4,1,28097,1,1,2,7),_Bridge_WirelessMode_Type())
bridge_WirelessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bridge_WirelessMode.setStatus(_A)
_BridgeAPFiltering_ObjectIdentity=ObjectIdentity
bridgeAPFiltering=_BridgeAPFiltering_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,8))
class _BridgeAPFilteringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_c,2)))
_BridgeAPFilteringEnable_Type.__name__=_D
_BridgeAPFilteringEnable_Object=MibScalar
bridgeAPFilteringEnable=_BridgeAPFilteringEnable_Object((1,3,6,1,4,1,28097,1,1,2,8,1),_BridgeAPFilteringEnable_Type())
bridgeAPFilteringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringEnable.setStatus(_A)
class _BridgeAPFilteringMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_BridgeAPFilteringMode_Type.__name__=_D
_BridgeAPFilteringMode_Object=MibScalar
bridgeAPFilteringMode=_BridgeAPFilteringMode_Object((1,3,6,1,4,1,28097,1,1,2,8,2),_BridgeAPFilteringMode_Type())
bridgeAPFilteringMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringMode.setStatus(_A)
_BridgeAPFilteringMACAddress_Type=PhysAddress
_BridgeAPFilteringMACAddress_Object=MibScalar
bridgeAPFilteringMACAddress=_BridgeAPFilteringMACAddress_Object((1,3,6,1,4,1,28097,1,1,2,8,3),_BridgeAPFilteringMACAddress_Type())
bridgeAPFilteringMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringMACAddress.setStatus(_A)
class _BridgeAPFilteringName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BridgeAPFilteringName_Type.__name__=_F
_BridgeAPFilteringName_Object=MibScalar
bridgeAPFilteringName=_BridgeAPFilteringName_Object((1,3,6,1,4,1,28097,1,1,2,8,4),_BridgeAPFilteringName_Type())
bridgeAPFilteringName.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringName.setStatus(_A)
_BridgeAPFilteringSave_Type=Integer32
_BridgeAPFilteringSave_Object=MibScalar
bridgeAPFilteringSave=_BridgeAPFilteringSave_Object((1,3,6,1,4,1,28097,1,1,2,8,5),_BridgeAPFilteringSave_Type())
bridgeAPFilteringSave.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringSave.setStatus(_A)
_BridgeAPFilteringDelete_Type=Integer32
_BridgeAPFilteringDelete_Object=MibScalar
bridgeAPFilteringDelete=_BridgeAPFilteringDelete_Object((1,3,6,1,4,1,28097,1,1,2,8,6),_BridgeAPFilteringDelete_Type())
bridgeAPFilteringDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringDelete.setStatus(_A)
_BridgeAPFilteringEnableRule_Type=Integer32
_BridgeAPFilteringEnableRule_Object=MibScalar
bridgeAPFilteringEnableRule=_BridgeAPFilteringEnableRule_Object((1,3,6,1,4,1,28097,1,1,2,8,7),_BridgeAPFilteringEnableRule_Type())
bridgeAPFilteringEnableRule.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringEnableRule.setStatus(_A)
_BridgeAPFilteringDisableRule_Type=Integer32
_BridgeAPFilteringDisableRule_Object=MibScalar
bridgeAPFilteringDisableRule=_BridgeAPFilteringDisableRule_Object((1,3,6,1,4,1,28097,1,1,2,8,8),_BridgeAPFilteringDisableRule_Type())
bridgeAPFilteringDisableRule.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringDisableRule.setStatus(_A)
_BridgeAPFilteringTable_Object=MibTable
bridgeAPFilteringTable=_BridgeAPFilteringTable_Object((1,3,6,1,4,1,28097,1,1,2,8,9))
if mibBuilder.loadTexts:bridgeAPFilteringTable.setStatus(_A)
_BridgeAPFilteringEntry_Object=MibTableRow
bridgeAPFilteringEntry=_BridgeAPFilteringEntry_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1))
bridgeAPFilteringEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:bridgeAPFilteringEntry.setStatus(_A)
_BridgeAPFilteringListId_Type=Integer32
_BridgeAPFilteringListId_Object=MibTableColumn
bridgeAPFilteringListId=_BridgeAPFilteringListId_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,1),_BridgeAPFilteringListId_Type())
bridgeAPFilteringListId.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeAPFilteringListId.setStatus(_A)
class _BridgeAPFilteringListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BridgeAPFilteringListName_Type.__name__=_F
_BridgeAPFilteringListName_Object=MibTableColumn
bridgeAPFilteringListName=_BridgeAPFilteringListName_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,2),_BridgeAPFilteringListName_Type())
bridgeAPFilteringListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeAPFilteringListName.setStatus(_A)
_BridgeAPFilteringListMAC_Type=PhysAddress
_BridgeAPFilteringListMAC_Object=MibTableColumn
bridgeAPFilteringListMAC=_BridgeAPFilteringListMAC_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,3),_BridgeAPFilteringListMAC_Type())
bridgeAPFilteringListMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeAPFilteringListMAC.setStatus(_A)
_BridgeAPFilteringListEnable_Type=DisableEnable
_BridgeAPFilteringListEnable_Object=MibTableColumn
bridgeAPFilteringListEnable=_BridgeAPFilteringListEnable_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,4),_BridgeAPFilteringListEnable_Type())
bridgeAPFilteringListEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeAPFilteringListEnable.setStatus(_A)
_BridgeRoaming_ObjectIdentity=ObjectIdentity
bridgeRoaming=_BridgeRoaming_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,9))
_BridgeRoamingAdvanced_ObjectIdentity=ObjectIdentity
bridgeRoamingAdvanced=_BridgeRoamingAdvanced_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,9,1))
_BridgeRoamingAdvancedScanThreshold_dbm_Type=Integer32
_BridgeRoamingAdvancedScanThreshold_dbm_Object=MibScalar
bridgeRoamingAdvancedScanThreshold_dbm=_BridgeRoamingAdvancedScanThreshold_dbm_Object((1,3,6,1,4,1,28097,1,1,2,9,1,1),_BridgeRoamingAdvancedScanThreshold_dbm_Type())
bridgeRoamingAdvancedScanThreshold_dbm.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingAdvancedScanThreshold_dbm.setStatus(_A)
_BridgeRoamingAdvancedScanThreshold_percent_Type=Integer32
_BridgeRoamingAdvancedScanThreshold_percent_Object=MibScalar
bridgeRoamingAdvancedScanThreshold_percent=_BridgeRoamingAdvancedScanThreshold_percent_Object((1,3,6,1,4,1,28097,1,1,2,9,1,2),_BridgeRoamingAdvancedScanThreshold_percent_Type())
bridgeRoamingAdvancedScanThreshold_percent.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingAdvancedScanThreshold_percent.setStatus(_A)
_BridgeRoamingAdvancedScanPeriod_Type=Integer32
_BridgeRoamingAdvancedScanPeriod_Object=MibScalar
bridgeRoamingAdvancedScanPeriod=_BridgeRoamingAdvancedScanPeriod_Object((1,3,6,1,4,1,28097,1,1,2,9,1,3),_BridgeRoamingAdvancedScanPeriod_Type())
bridgeRoamingAdvancedScanPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingAdvancedScanPeriod.setStatus(_A)
_BridgeRoamingAdvancedScanDuration_Type=Integer32
_BridgeRoamingAdvancedScanDuration_Object=MibScalar
bridgeRoamingAdvancedScanDuration=_BridgeRoamingAdvancedScanDuration_Object((1,3,6,1,4,1,28097,1,1,2,9,1,4),_BridgeRoamingAdvancedScanDuration_Type())
bridgeRoamingAdvancedScanDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingAdvancedScanDuration.setStatus(_A)
_BridgeRoamingAdvancedAPLossDetection_Type=Integer32
_BridgeRoamingAdvancedAPLossDetection_Object=MibScalar
bridgeRoamingAdvancedAPLossDetection=_BridgeRoamingAdvancedAPLossDetection_Object((1,3,6,1,4,1,28097,1,1,2,9,1,5),_BridgeRoamingAdvancedAPLossDetection_Type())
bridgeRoamingAdvancedAPLossDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingAdvancedAPLossDetection.setStatus(_A)
_BridgeRoamingEnable_Type=DisableEnable
_BridgeRoamingEnable_Object=MibScalar
bridgeRoamingEnable=_BridgeRoamingEnable_Object((1,3,6,1,4,1,28097,1,1,2,9,2),_BridgeRoamingEnable_Type())
bridgeRoamingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingEnable.setStatus(_A)
_BridgeRoamingRSSIThreshold_dBm_Type=Integer32
_BridgeRoamingRSSIThreshold_dBm_Object=MibScalar
bridgeRoamingRSSIThreshold_dBm=_BridgeRoamingRSSIThreshold_dBm_Object((1,3,6,1,4,1,28097,1,1,2,9,3),_BridgeRoamingRSSIThreshold_dBm_Type())
bridgeRoamingRSSIThreshold_dBm.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingRSSIThreshold_dBm.setStatus(_A)
_BridgeRoamingRSSIThreshold_percent_Type=Integer32
_BridgeRoamingRSSIThreshold_percent_Object=MibScalar
bridgeRoamingRSSIThreshold_percent=_BridgeRoamingRSSIThreshold_percent_Object((1,3,6,1,4,1,28097,1,1,2,9,4),_BridgeRoamingRSSIThreshold_percent_Type())
bridgeRoamingRSSIThreshold_percent.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeRoamingRSSIThreshold_percent.setStatus(_A)
class _BridgeChannelList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_BridgeChannelList_Type.__name__=_F
_BridgeChannelList_Object=MibScalar
bridgeChannelList=_BridgeChannelList_Object((1,3,6,1,4,1,28097,1,1,2,10),_BridgeChannelList_Type())
bridgeChannelList.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeChannelList.setStatus(_A)
_BridgeWirelessScan_ObjectIdentity=ObjectIdentity
bridgeWirelessScan=_BridgeWirelessScan_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,11))
_BridgeWileressScanTable_Object=MibTable
bridgeWileressScanTable=_BridgeWileressScanTable_Object((1,3,6,1,4,1,28097,1,1,2,11,1))
if mibBuilder.loadTexts:bridgeWileressScanTable.setStatus(_A)
_BridgeWirelessScanEntry_Object=MibTableRow
bridgeWirelessScanEntry=_BridgeWirelessScanEntry_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1))
bridgeWirelessScanEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:bridgeWirelessScanEntry.setStatus(_A)
_BridgeWirelessScanAPMac_Type=PhysAddress
_BridgeWirelessScanAPMac_Object=MibTableColumn
bridgeWirelessScanAPMac=_BridgeWirelessScanAPMac_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,1),_BridgeWirelessScanAPMac_Type())
bridgeWirelessScanAPMac.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeWirelessScanAPMac.setStatus(_A)
class _BridgeWirelessScanSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_BridgeWirelessScanSSID_Type.__name__=_F
_BridgeWirelessScanSSID_Object=MibTableColumn
bridgeWirelessScanSSID=_BridgeWirelessScanSSID_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,2),_BridgeWirelessScanSSID_Type())
bridgeWirelessScanSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeWirelessScanSSID.setStatus(_A)
_BridgeWirelessScanChannel_Type=Integer32
_BridgeWirelessScanChannel_Object=MibTableColumn
bridgeWirelessScanChannel=_BridgeWirelessScanChannel_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,3),_BridgeWirelessScanChannel_Type())
bridgeWirelessScanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeWirelessScanChannel.setStatus(_A)
class _BridgeWirelessScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4)))
_BridgeWirelessScanMode_Type.__name__=_D
_BridgeWirelessScanMode_Object=MibTableColumn
bridgeWirelessScanMode=_BridgeWirelessScanMode_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,4),_BridgeWirelessScanMode_Type())
bridgeWirelessScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeWirelessScanMode.setStatus(_A)
class _BridgeWirelessScanSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('wep',1),(_m,2)))
_BridgeWirelessScanSecurity_Type.__name__=_D
_BridgeWirelessScanSecurity_Object=MibTableColumn
bridgeWirelessScanSecurity=_BridgeWirelessScanSecurity_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,5),_BridgeWirelessScanSecurity_Type())
bridgeWirelessScanSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeWirelessScanSecurity.setStatus(_A)
_BridgeWirelessScanRssi_Type=Integer32
_BridgeWirelessScanRssi_Object=MibTableColumn
bridgeWirelessScanRssi=_BridgeWirelessScanRssi_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,6),_BridgeWirelessScanRssi_Type())
bridgeWirelessScanRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeWirelessScanRssi.setStatus(_A)
_BridgeNAT_ObjectIdentity=ObjectIdentity
bridgeNAT=_BridgeNAT_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,12))
class _BrigeNATStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_BrigeNATStatus_Type.__name__=_D
_BrigeNATStatus_Object=MibScalar
brigeNATStatus=_BrigeNATStatus_Object((1,3,6,1,4,1,28097,1,1,2,12,1),_BrigeNATStatus_Type())
brigeNATStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATStatus.setStatus(_A)
class _BrigeNATEnablePing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_BrigeNATEnablePing_Type.__name__=_D
_BrigeNATEnablePing_Object=MibScalar
brigeNATEnablePing=_BrigeNATEnablePing_Object((1,3,6,1,4,1,28097,1,1,2,12,2),_BrigeNATEnablePing_Type())
brigeNATEnablePing.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATEnablePing.setStatus(_A)
class _BrigeNATEnableProductWebServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_BrigeNATEnableProductWebServer_Type.__name__=_D
_BrigeNATEnableProductWebServer_Object=MibScalar
brigeNATEnableProductWebServer=_BrigeNATEnableProductWebServer_Object((1,3,6,1,4,1,28097,1,1,2,12,3),_BrigeNATEnableProductWebServer_Type())
brigeNATEnableProductWebServer.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATEnableProductWebServer.setStatus(_A)
_BrigeNATInternalWebServerPort_Type=Integer32
_BrigeNATInternalWebServerPort_Object=MibScalar
brigeNATInternalWebServerPort=_BrigeNATInternalWebServerPort_Object((1,3,6,1,4,1,28097,1,1,2,12,4),_BrigeNATInternalWebServerPort_Type())
brigeNATInternalWebServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATInternalWebServerPort.setStatus(_A)
class _BrigeNATEnableProductSnmpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_BrigeNATEnableProductSnmpServer_Type.__name__=_D
_BrigeNATEnableProductSnmpServer_Object=MibScalar
brigeNATEnableProductSnmpServer=_BrigeNATEnableProductSnmpServer_Object((1,3,6,1,4,1,28097,1,1,2,12,5),_BrigeNATEnableProductSnmpServer_Type())
brigeNATEnableProductSnmpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATEnableProductSnmpServer.setStatus(_A)
_BrigeNATInternalWebSnmpPort_Type=Integer32
_BrigeNATInternalWebSnmpPort_Object=MibScalar
brigeNATInternalWebSnmpPort=_BrigeNATInternalWebSnmpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,6),_BrigeNATInternalWebSnmpPort_Type())
brigeNATInternalWebSnmpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATInternalWebSnmpPort.setStatus(_A)
class _BrigeNATWanIpAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_BrigeNATWanIpAddrMode_Type.__name__=_D
_BrigeNATWanIpAddrMode_Object=MibScalar
brigeNATWanIpAddrMode=_BrigeNATWanIpAddrMode_Object((1,3,6,1,4,1,28097,1,1,2,12,7),_BrigeNATWanIpAddrMode_Type())
brigeNATWanIpAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATWanIpAddrMode.setStatus(_A)
_BrigeNATWanIpAddr_Type=IpAddress
_BrigeNATWanIpAddr_Object=MibScalar
brigeNATWanIpAddr=_BrigeNATWanIpAddr_Object((1,3,6,1,4,1,28097,1,1,2,12,8),_BrigeNATWanIpAddr_Type())
brigeNATWanIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATWanIpAddr.setStatus(_A)
_BrigeNATWanSubnetMask_Type=IpAddress
_BrigeNATWanSubnetMask_Object=MibScalar
brigeNATWanSubnetMask=_BrigeNATWanSubnetMask_Object((1,3,6,1,4,1,28097,1,1,2,12,9),_BrigeNATWanSubnetMask_Type())
brigeNATWanSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATWanSubnetMask.setStatus(_A)
_BrigeNATWanGateway_Type=IpAddress
_BrigeNATWanGateway_Object=MibScalar
brigeNATWanGateway=_BrigeNATWanGateway_Object((1,3,6,1,4,1,28097,1,1,2,12,10),_BrigeNATWanGateway_Type())
brigeNATWanGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATWanGateway.setStatus(_A)
_BridgeNatPortForwarding_ObjectIdentity=ObjectIdentity
bridgeNatPortForwarding=_BridgeNatPortForwarding_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,12,11))
_BridgeNatPortForwardingTable_Object=MibTable
bridgeNatPortForwardingTable=_BridgeNatPortForwardingTable_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1))
if mibBuilder.loadTexts:bridgeNatPortForwardingTable.setStatus(_A)
_BridgeNatPortForwardingEntry_Object=MibTableRow
bridgeNatPortForwardingEntry=_BridgeNatPortForwardingEntry_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1))
bridgeNatPortForwardingEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:bridgeNatPortForwardingEntry.setStatus(_A)
_BridgeNatPortForwardingListId_Type=Integer32
_BridgeNatPortForwardingListId_Object=MibTableColumn
bridgeNatPortForwardingListId=_BridgeNatPortForwardingListId_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,1),_BridgeNatPortForwardingListId_Type())
bridgeNatPortForwardingListId.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListId.setStatus(_A)
class _BridgeNatPortForwardingListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListName_Type.__name__=_F
_BridgeNatPortForwardingListName_Object=MibTableColumn
bridgeNatPortForwardingListName=_BridgeNatPortForwardingListName_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,2),_BridgeNatPortForwardingListName_Type())
bridgeNatPortForwardingListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListName.setStatus(_A)
_BridgeNatPortForwardingListIpAddr_Type=IpAddress
_BridgeNatPortForwardingListIpAddr_Object=MibTableColumn
bridgeNatPortForwardingListIpAddr=_BridgeNatPortForwardingListIpAddr_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,3),_BridgeNatPortForwardingListIpAddr_Type())
bridgeNatPortForwardingListIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListIpAddr.setStatus(_A)
class _BridgeNatPortForwardingListPublicTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPublicTcpPort_Type.__name__=_F
_BridgeNatPortForwardingListPublicTcpPort_Object=MibTableColumn
bridgeNatPortForwardingListPublicTcpPort=_BridgeNatPortForwardingListPublicTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,4),_BridgeNatPortForwardingListPublicTcpPort_Type())
bridgeNatPortForwardingListPublicTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPublicTcpPort.setStatus(_A)
class _BridgeNatPortForwardingListPrivateTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPrivateTcpPort_Type.__name__=_F
_BridgeNatPortForwardingListPrivateTcpPort_Object=MibTableColumn
bridgeNatPortForwardingListPrivateTcpPort=_BridgeNatPortForwardingListPrivateTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,5),_BridgeNatPortForwardingListPrivateTcpPort_Type())
bridgeNatPortForwardingListPrivateTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPrivateTcpPort.setStatus(_A)
class _BridgeNatPortForwardingListPublicUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPublicUdpPort_Type.__name__=_F
_BridgeNatPortForwardingListPublicUdpPort_Object=MibTableColumn
bridgeNatPortForwardingListPublicUdpPort=_BridgeNatPortForwardingListPublicUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,6),_BridgeNatPortForwardingListPublicUdpPort_Type())
bridgeNatPortForwardingListPublicUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPublicUdpPort.setStatus(_A)
class _BridgeNatPortForwardingListPrivateUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPrivateUdpPort_Type.__name__=_F
_BridgeNatPortForwardingListPrivateUdpPort_Object=MibTableColumn
bridgeNatPortForwardingListPrivateUdpPort=_BridgeNatPortForwardingListPrivateUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,7),_BridgeNatPortForwardingListPrivateUdpPort_Type())
bridgeNatPortForwardingListPrivateUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPrivateUdpPort.setStatus(_A)
class _BridgeNatPortForwardingListEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_BridgeNatPortForwardingListEnable_Type.__name__=_D
_BridgeNatPortForwardingListEnable_Object=MibTableColumn
bridgeNatPortForwardingListEnable=_BridgeNatPortForwardingListEnable_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,8),_BridgeNatPortForwardingListEnable_Type())
bridgeNatPortForwardingListEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeNatPortForwardingListEnable.setStatus(_A)
class _BridgeNatPortForwardingName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingName_Type.__name__=_F
_BridgeNatPortForwardingName_Object=MibScalar
bridgeNatPortForwardingName=_BridgeNatPortForwardingName_Object((1,3,6,1,4,1,28097,1,1,2,12,11,2),_BridgeNatPortForwardingName_Type())
bridgeNatPortForwardingName.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingName.setStatus(_A)
_BridgeNatPortForwardingIpAddr_Type=IpAddress
_BridgeNatPortForwardingIpAddr_Object=MibScalar
bridgeNatPortForwardingIpAddr=_BridgeNatPortForwardingIpAddr_Object((1,3,6,1,4,1,28097,1,1,2,12,11,3),_BridgeNatPortForwardingIpAddr_Type())
bridgeNatPortForwardingIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingIpAddr.setStatus(_A)
class _BridgeNatPortForwardingPublicTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPublicTcpPort_Type.__name__=_F
_BridgeNatPortForwardingPublicTcpPort_Object=MibScalar
bridgeNatPortForwardingPublicTcpPort=_BridgeNatPortForwardingPublicTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,4),_BridgeNatPortForwardingPublicTcpPort_Type())
bridgeNatPortForwardingPublicTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPublicTcpPort.setStatus(_A)
class _BridgeNatPortForwardingPrivateTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPrivateTcpPort_Type.__name__=_F
_BridgeNatPortForwardingPrivateTcpPort_Object=MibScalar
bridgeNatPortForwardingPrivateTcpPort=_BridgeNatPortForwardingPrivateTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,5),_BridgeNatPortForwardingPrivateTcpPort_Type())
bridgeNatPortForwardingPrivateTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPrivateTcpPort.setStatus(_A)
class _BridgeNatPortForwardingPublicUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPublicUdpPort_Type.__name__=_F
_BridgeNatPortForwardingPublicUdpPort_Object=MibScalar
bridgeNatPortForwardingPublicUdpPort=_BridgeNatPortForwardingPublicUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,6),_BridgeNatPortForwardingPublicUdpPort_Type())
bridgeNatPortForwardingPublicUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPublicUdpPort.setStatus(_A)
class _BridgeNatPortForwardingPrivateUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPrivateUdpPort_Type.__name__=_F
_BridgeNatPortForwardingPrivateUdpPort_Object=MibScalar
bridgeNatPortForwardingPrivateUdpPort=_BridgeNatPortForwardingPrivateUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,7),_BridgeNatPortForwardingPrivateUdpPort_Type())
bridgeNatPortForwardingPrivateUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPrivateUdpPort.setStatus(_A)
_BridgeNatPortForwardingEnableRule_Type=Integer32
_BridgeNatPortForwardingEnableRule_Object=MibScalar
bridgeNatPortForwardingEnableRule=_BridgeNatPortForwardingEnableRule_Object((1,3,6,1,4,1,28097,1,1,2,12,11,8),_BridgeNatPortForwardingEnableRule_Type())
bridgeNatPortForwardingEnableRule.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingEnableRule.setStatus(_A)
_BridgeNatPortForwardingDisableRule_Type=Integer32
_BridgeNatPortForwardingDisableRule_Object=MibScalar
bridgeNatPortForwardingDisableRule=_BridgeNatPortForwardingDisableRule_Object((1,3,6,1,4,1,28097,1,1,2,12,11,9),_BridgeNatPortForwardingDisableRule_Type())
bridgeNatPortForwardingDisableRule.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingDisableRule.setStatus(_A)
_BridgeNatPortForwardingSaveRule_Type=Integer32
_BridgeNatPortForwardingSaveRule_Object=MibScalar
bridgeNatPortForwardingSaveRule=_BridgeNatPortForwardingSaveRule_Object((1,3,6,1,4,1,28097,1,1,2,12,11,10),_BridgeNatPortForwardingSaveRule_Type())
bridgeNatPortForwardingSaveRule.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingSaveRule.setStatus(_A)
_BridgeNatPortForwardingDeleteRule_Type=Integer32
_BridgeNatPortForwardingDeleteRule_Object=MibScalar
bridgeNatPortForwardingDeleteRule=_BridgeNatPortForwardingDeleteRule_Object((1,3,6,1,4,1,28097,1,1,2,12,11,11),_BridgeNatPortForwardingDeleteRule_Type())
bridgeNatPortForwardingDeleteRule.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingDeleteRule.setStatus(_A)
_Access_point_mode_ObjectIdentity=ObjectIdentity
access_point_mode=_Access_point_mode_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3))
_ApClientTable_Object=MibTable
apClientTable=_ApClientTable_Object((1,3,6,1,4,1,28097,1,1,3,1))
if mibBuilder.loadTexts:apClientTable.setStatus(_A)
_ApClientEntry_Object=MibTableRow
apClientEntry=_ApClientEntry_Object((1,3,6,1,4,1,28097,1,1,3,1,1))
apClientEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:apClientEntry.setStatus(_A)
_ClientMacAddr_Type=PhysAddress
_ClientMacAddr_Object=MibTableColumn
clientMacAddr=_ClientMacAddr_Object((1,3,6,1,4,1,28097,1,1,3,1,1,1),_ClientMacAddr_Type())
clientMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:clientMacAddr.setStatus(_A)
class _Client80211Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4)))
_Client80211Mode_Type.__name__=_D
_Client80211Mode_Object=MibTableColumn
client80211Mode=_Client80211Mode_Object((1,3,6,1,4,1,28097,1,1,3,1,1,2),_Client80211Mode_Type())
client80211Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:client80211Mode.setStatus(_A)
_ClientTxRate_Type=Integer32
_ClientTxRate_Object=MibTableColumn
clientTxRate=_ClientTxRate_Object((1,3,6,1,4,1,28097,1,1,3,1,1,3),_ClientTxRate_Type())
clientTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:clientTxRate.setStatus(_A)
_ClientRssiPercent_Type=Gauge32
_ClientRssiPercent_Object=MibTableColumn
clientRssiPercent=_ClientRssiPercent_Object((1,3,6,1,4,1,28097,1,1,3,1,1,4),_ClientRssiPercent_Type())
clientRssiPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:clientRssiPercent.setStatus(_A)
class _ApAutomaticChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_c,2)))
_ApAutomaticChannel_Type.__name__=_D
_ApAutomaticChannel_Object=MibScalar
apAutomaticChannel=_ApAutomaticChannel_Object((1,3,6,1,4,1,28097,1,1,3,2),_ApAutomaticChannel_Type())
apAutomaticChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apAutomaticChannel.setStatus(_A)
_ApClientCount_Type=Integer32
_ApClientCount_Object=MibScalar
apClientCount=_ApClientCount_Object((1,3,6,1,4,1,28097,1,1,3,3),_ApClientCount_Type())
apClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apClientCount.setStatus(_A)
_ApClientFiltering_ObjectIdentity=ObjectIdentity
apClientFiltering=_ApClientFiltering_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3,4))
class _ApClientFilteringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_c,2)))
_ApClientFilteringEnable_Type.__name__=_D
_ApClientFilteringEnable_Object=MibScalar
apClientFilteringEnable=_ApClientFilteringEnable_Object((1,3,6,1,4,1,28097,1,1,3,4,1),_ApClientFilteringEnable_Type())
apClientFilteringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringEnable.setStatus(_A)
class _ApClientFilteringMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_ApClientFilteringMode_Type.__name__=_D
_ApClientFilteringMode_Object=MibScalar
apClientFilteringMode=_ApClientFilteringMode_Object((1,3,6,1,4,1,28097,1,1,3,4,2),_ApClientFilteringMode_Type())
apClientFilteringMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringMode.setStatus(_A)
_ApClientWirelessFiltering_Type=DisableEnable
_ApClientWirelessFiltering_Object=MibScalar
apClientWirelessFiltering=_ApClientWirelessFiltering_Object((1,3,6,1,4,1,28097,1,1,3,4,3),_ApClientWirelessFiltering_Type())
apClientWirelessFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientWirelessFiltering.setStatus(_A)
_ApClientWiredFiltering_Type=DisableEnable
_ApClientWiredFiltering_Object=MibScalar
apClientWiredFiltering=_ApClientWiredFiltering_Object((1,3,6,1,4,1,28097,1,1,3,4,4),_ApClientWiredFiltering_Type())
apClientWiredFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientWiredFiltering.setStatus(_A)
_ApClientFilteringMACAddress_Type=PhysAddress
_ApClientFilteringMACAddress_Object=MibScalar
apClientFilteringMACAddress=_ApClientFilteringMACAddress_Object((1,3,6,1,4,1,28097,1,1,3,4,5),_ApClientFilteringMACAddress_Type())
apClientFilteringMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringMACAddress.setStatus(_A)
class _ApClientFilteringName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ApClientFilteringName_Type.__name__=_F
_ApClientFilteringName_Object=MibScalar
apClientFilteringName=_ApClientFilteringName_Object((1,3,6,1,4,1,28097,1,1,3,4,6),_ApClientFilteringName_Type())
apClientFilteringName.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringName.setStatus(_A)
_ApClientFilteringSave_Type=Integer32
_ApClientFilteringSave_Object=MibScalar
apClientFilteringSave=_ApClientFilteringSave_Object((1,3,6,1,4,1,28097,1,1,3,4,7),_ApClientFilteringSave_Type())
apClientFilteringSave.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringSave.setStatus(_A)
_ApClientFilteringDelete_Type=Integer32
_ApClientFilteringDelete_Object=MibScalar
apClientFilteringDelete=_ApClientFilteringDelete_Object((1,3,6,1,4,1,28097,1,1,3,4,8),_ApClientFilteringDelete_Type())
apClientFilteringDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringDelete.setStatus(_A)
_ApClientFilteringEnableRule_Type=Integer32
_ApClientFilteringEnableRule_Object=MibScalar
apClientFilteringEnableRule=_ApClientFilteringEnableRule_Object((1,3,6,1,4,1,28097,1,1,3,4,9),_ApClientFilteringEnableRule_Type())
apClientFilteringEnableRule.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringEnableRule.setStatus(_A)
_ApClientFilteringDisableRule_Type=Integer32
_ApClientFilteringDisableRule_Object=MibScalar
apClientFilteringDisableRule=_ApClientFilteringDisableRule_Object((1,3,6,1,4,1,28097,1,1,3,4,10),_ApClientFilteringDisableRule_Type())
apClientFilteringDisableRule.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringDisableRule.setStatus(_A)
_ApClientFilteringTable_Object=MibTable
apClientFilteringTable=_ApClientFilteringTable_Object((1,3,6,1,4,1,28097,1,1,3,4,11))
if mibBuilder.loadTexts:apClientFilteringTable.setStatus(_A)
_ApClientFilteringEntry_Object=MibTableRow
apClientFilteringEntry=_ApClientFilteringEntry_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1))
apClientFilteringEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:apClientFilteringEntry.setStatus(_A)
_ApClientFilteringListId_Type=Integer32
_ApClientFilteringListId_Object=MibTableColumn
apClientFilteringListId=_ApClientFilteringListId_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,1),_ApClientFilteringListId_Type())
apClientFilteringListId.setMaxAccess(_C)
if mibBuilder.loadTexts:apClientFilteringListId.setStatus(_A)
class _ApClientFilteringListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ApClientFilteringListName_Type.__name__=_F
_ApClientFilteringListName_Object=MibTableColumn
apClientFilteringListName=_ApClientFilteringListName_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,2),_ApClientFilteringListName_Type())
apClientFilteringListName.setMaxAccess(_C)
if mibBuilder.loadTexts:apClientFilteringListName.setStatus(_A)
_ApClientFilteringListMAC_Type=PhysAddress
_ApClientFilteringListMAC_Object=MibTableColumn
apClientFilteringListMAC=_ApClientFilteringListMAC_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,3),_ApClientFilteringListMAC_Type())
apClientFilteringListMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:apClientFilteringListMAC.setStatus(_A)
_ApClientFilteringListEnable_Type=DisableEnable
_ApClientFilteringListEnable_Object=MibTableColumn
apClientFilteringListEnable=_ApClientFilteringListEnable_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,4),_ApClientFilteringListEnable_Type())
apClientFilteringListEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apClientFilteringListEnable.setStatus(_A)
_Wds_ObjectIdentity=ObjectIdentity
wds=_Wds_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3,5))
_ApWDSEnable_Type=DisableEnable
_ApWDSEnable_Object=MibScalar
apWDSEnable=_ApWDSEnable_Object((1,3,6,1,4,1,28097,1,1,3,5,1),_ApWDSEnable_Type())
apWDSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSEnable.setStatus(_A)
_ApWDSEnableSTP_Type=DisableEnable
_ApWDSEnableSTP_Object=MibScalar
apWDSEnableSTP=_ApWDSEnableSTP_Object((1,3,6,1,4,1,28097,1,1,3,5,2),_ApWDSEnableSTP_Type())
apWDSEnableSTP.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSEnableSTP.setStatus(_A)
_ApWDSMAC1_Type=PhysAddress
_ApWDSMAC1_Object=MibScalar
apWDSMAC1=_ApWDSMAC1_Object((1,3,6,1,4,1,28097,1,1,3,5,3),_ApWDSMAC1_Type())
apWDSMAC1.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSMAC1.setStatus(_A)
_ApWDSMAC2_Type=PhysAddress
_ApWDSMAC2_Object=MibScalar
apWDSMAC2=_ApWDSMAC2_Object((1,3,6,1,4,1,28097,1,1,3,5,4),_ApWDSMAC2_Type())
apWDSMAC2.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSMAC2.setStatus(_A)
_ApWDSMAC3_Type=PhysAddress
_ApWDSMAC3_Object=MibScalar
apWDSMAC3=_ApWDSMAC3_Object((1,3,6,1,4,1,28097,1,1,3,5,5),_ApWDSMAC3_Type())
apWDSMAC3.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSMAC3.setStatus(_A)
_ApWDSMAC4_Type=PhysAddress
_ApWDSMAC4_Object=MibScalar
apWDSMAC4=_ApWDSMAC4_Object((1,3,6,1,4,1,28097,1,1,3,5,6),_ApWDSMAC4_Type())
apWDSMAC4.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSMAC4.setStatus(_A)
_ApWDSMAC5_Type=PhysAddress
_ApWDSMAC5_Object=MibScalar
apWDSMAC5=_ApWDSMAC5_Object((1,3,6,1,4,1,28097,1,1,3,5,7),_ApWDSMAC5_Type())
apWDSMAC5.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSMAC5.setStatus(_A)
_ApWDSMAC6_Type=PhysAddress
_ApWDSMAC6_Object=MibScalar
apWDSMAC6=_ApWDSMAC6_Object((1,3,6,1,4,1,28097,1,1,3,5,8),_ApWDSMAC6_Type())
apWDSMAC6.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSMAC6.setStatus(_A)
class _SettingSSIDVisibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('invisible',1),('visible',2)))
_SettingSSIDVisibility_Type.__name__=_D
_SettingSSIDVisibility_Object=MibScalar
settingSSIDVisibility=_SettingSSIDVisibility_Object((1,3,6,1,4,1,28097,1,1,3,6),_SettingSSIDVisibility_Type())
settingSSIDVisibility.setMaxAccess(_B)
if mibBuilder.loadTexts:settingSSIDVisibility.setStatus(_A)
_EnableSTP_Type=DisableEnable
_EnableSTP_Object=MibScalar
enableSTP=_EnableSTP_Object((1,3,6,1,4,1,28097,1,1,3,7),_EnableSTP_Type())
enableSTP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableSTP.setStatus(_A)
_LanTimeOutSettings_ObjectIdentity=ObjectIdentity
lanTimeOutSettings=_LanTimeOutSettings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3,8))
_EnableLanTimeout_Type=DisableEnable
_EnableLanTimeout_Object=MibScalar
enableLanTimeout=_EnableLanTimeout_Object((1,3,6,1,4,1,28097,1,1,3,8,1),_EnableLanTimeout_Type())
enableLanTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:enableLanTimeout.setStatus(_A)
_LanTimeoutIPSurvey_Type=Integer32
_LanTimeoutIPSurvey_Object=MibScalar
lanTimeoutIPSurvey=_LanTimeoutIPSurvey_Object((1,3,6,1,4,1,28097,1,1,3,8,2),_LanTimeoutIPSurvey_Type())
lanTimeoutIPSurvey.setMaxAccess(_B)
if mibBuilder.loadTexts:lanTimeoutIPSurvey.setStatus(_A)
_LanTimeoutMaxProbe_Type=Integer32
_LanTimeoutMaxProbe_Object=MibScalar
lanTimeoutMaxProbe=_LanTimeoutMaxProbe_Object((1,3,6,1,4,1,28097,1,1,3,8,3),_LanTimeoutMaxProbe_Type())
lanTimeoutMaxProbe.setMaxAccess(_B)
if mibBuilder.loadTexts:lanTimeoutMaxProbe.setStatus(_A)
_LanTimeoutProbeTimeout_Type=Integer32
_LanTimeoutProbeTimeout_Object=MibScalar
lanTimeoutProbeTimeout=_LanTimeoutProbeTimeout_Object((1,3,6,1,4,1,28097,1,1,3,8,4),_LanTimeoutProbeTimeout_Type())
lanTimeoutProbeTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:lanTimeoutProbeTimeout.setStatus(_A)
_LanTimeoutProbeInterval_Type=Integer32
_LanTimeoutProbeInterval_Object=MibScalar
lanTimeoutProbeInterval=_LanTimeoutProbeInterval_Object((1,3,6,1,4,1,28097,1,1,3,8,5),_LanTimeoutProbeInterval_Type())
lanTimeoutProbeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lanTimeoutProbeInterval.setStatus(_A)
_AdvancedSettings_ObjectIdentity=ObjectIdentity
advancedSettings=_AdvancedSettings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,4))
_LongDistanceSettings_ObjectIdentity=ObjectIdentity
longDistanceSettings=_LongDistanceSettings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,4,1))
_EnableLongDistance_Type=DisableEnable
_EnableLongDistance_Object=MibScalar
enableLongDistance=_EnableLongDistance_Object((1,3,6,1,4,1,28097,1,1,4,1,1),_EnableLongDistance_Type())
enableLongDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:enableLongDistance.setStatus(_A)
_DistanceAntennaMeter_Type=Integer32
_DistanceAntennaMeter_Object=MibScalar
distanceAntennaMeter=_DistanceAntennaMeter_Object((1,3,6,1,4,1,28097,1,1,4,1,2),_DistanceAntennaMeter_Type())
distanceAntennaMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:distanceAntennaMeter.setStatus(_A)
_DistanceSlotTime_Type=Integer32
_DistanceSlotTime_Object=MibScalar
distanceSlotTime=_DistanceSlotTime_Object((1,3,6,1,4,1,28097,1,1,4,1,3),_DistanceSlotTime_Type())
distanceSlotTime.setMaxAccess(_B)
if mibBuilder.loadTexts:distanceSlotTime.setStatus(_A)
_DistanceAckTimeout_Type=Integer32
_DistanceAckTimeout_Object=MibScalar
distanceAckTimeout=_DistanceAckTimeout_Object((1,3,6,1,4,1,28097,1,1,4,1,4),_DistanceAckTimeout_Type())
distanceAckTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:distanceAckTimeout.setStatus(_A)
_DistanceCtsTimeout_Type=Integer32
_DistanceCtsTimeout_Object=MibScalar
distanceCtsTimeout=_DistanceCtsTimeout_Object((1,3,6,1,4,1,28097,1,1,4,1,5),_DistanceCtsTimeout_Type())
distanceCtsTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:distanceCtsTimeout.setStatus(_A)
_Enable802_11d_Type=DisableEnable
_Enable802_11d_Object=MibScalar
enable802_11d=_Enable802_11d_Object((1,3,6,1,4,1,28097,1,1,4,2),_Enable802_11d_Type())
enable802_11d.setMaxAccess(_B)
if mibBuilder.loadTexts:enable802_11d.setStatus(_A)
class _EnableIsolateSTA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_EnableIsolateSTA_Type.__name__=_D
_EnableIsolateSTA_Object=MibScalar
enableIsolateSTA=_EnableIsolateSTA_Object((1,3,6,1,4,1,28097,1,1,4,3),_EnableIsolateSTA_Type())
enableIsolateSTA.setMaxAccess(_B)
if mibBuilder.loadTexts:enableIsolateSTA.setStatus(_A)
_Administration_ObjectIdentity=ObjectIdentity
administration=_Administration_ObjectIdentity((1,3,6,1,4,1,28097,1,2))
class _AdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdminReset_Type.__name__=_D
_AdminReset_Object=MibScalar
adminReset=_AdminReset_Object((1,3,6,1,4,1,28097,1,2,1),_AdminReset_Type())
adminReset.setMaxAccess(_B)
if mibBuilder.loadTexts:adminReset.setStatus(_A)
class _AdminResetFactory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('resetfactory',1))
_AdminResetFactory_Type.__name__=_D
_AdminResetFactory_Object=MibScalar
adminResetFactory=_AdminResetFactory_Object((1,3,6,1,4,1,28097,1,2,2),_AdminResetFactory_Type())
adminResetFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:adminResetFactory.setStatus(_A)
_AdminEnableWebServer_Type=DisableEnable
_AdminEnableWebServer_Object=MibScalar
adminEnableWebServer=_AdminEnableWebServer_Object((1,3,6,1,4,1,28097,1,2,3),_AdminEnableWebServer_Type())
adminEnableWebServer.setMaxAccess(_B)
if mibBuilder.loadTexts:adminEnableWebServer.setStatus(_A)
_AdminAutoSave_Type=DisableEnable
_AdminAutoSave_Object=MibScalar
adminAutoSave=_AdminAutoSave_Object((1,3,6,1,4,1,28097,1,2,4),_AdminAutoSave_Type())
adminAutoSave.setMaxAccess(_B)
if mibBuilder.loadTexts:adminAutoSave.setStatus(_A)
class _AdminSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('save',1),('saveRequired',2),('saveNotRequired',3)))
_AdminSave_Type.__name__=_D
_AdminSave_Object=MibScalar
adminSave=_AdminSave_Object((1,3,6,1,4,1,28097,1,2,5),_AdminSave_Type())
adminSave.setMaxAccess(_B)
if mibBuilder.loadTexts:adminSave.setStatus(_A)
class _AdminApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),('applyRequire',3)))
_AdminApply_Type.__name__=_D
_AdminApply_Object=MibScalar
adminApply=_AdminApply_Object((1,3,6,1,4,1,28097,1,2,6),_AdminApply_Type())
adminApply.setMaxAccess(_B)
if mibBuilder.loadTexts:adminApply.setStatus(_A)
class _AdminConfigHash_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminConfigHash_Type.__name__=_F
_AdminConfigHash_Object=MibScalar
adminConfigHash=_AdminConfigHash_Object((1,3,6,1,4,1,28097,1,2,7),_AdminConfigHash_Type())
adminConfigHash.setMaxAccess(_C)
if mibBuilder.loadTexts:adminConfigHash.setStatus(_A)
_FileTransfer_ObjectIdentity=ObjectIdentity
fileTransfer=_FileTransfer_ObjectIdentity((1,3,6,1,4,1,28097,1,2,8))
class _FileTransferAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upload',1),('download',2)))
_FileTransferAction_Type.__name__=_D
_FileTransferAction_Object=MibScalar
fileTransferAction=_FileTransferAction_Object((1,3,6,1,4,1,28097,1,2,8,1),_FileTransferAction_Type())
fileTransferAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferAction.setStatus(_A)
class _FileTransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('config',1),('firmware',2),('lte-firmware',3),('wids-config',4),('ssh-auth-keys',5)))
_FileTransferType_Type.__name__=_D
_FileTransferType_Object=MibScalar
fileTransferType=_FileTransferType_Object((1,3,6,1,4,1,28097,1,2,8,2),_FileTransferType_Type())
fileTransferType.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferType.setStatus(_A)
_FileTransferSize_Type=Integer32
_FileTransferSize_Object=MibScalar
fileTransferSize=_FileTransferSize_Object((1,3,6,1,4,1,28097,1,2,8,3),_FileTransferSize_Type())
fileTransferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferSize.setStatus(_A)
_FileTransferIndex_Type=Integer32
_FileTransferIndex_Object=MibScalar
fileTransferIndex=_FileTransferIndex_Object((1,3,6,1,4,1,28097,1,2,8,4),_FileTransferIndex_Type())
fileTransferIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferIndex.setStatus(_A)
_FileTransferHash_Type=OctetString
_FileTransferHash_Object=MibScalar
fileTransferHash=_FileTransferHash_Object((1,3,6,1,4,1,28097,1,2,8,5),_FileTransferHash_Type())
fileTransferHash.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferHash.setStatus(_A)
_FileTransferChunk_Type=OctetString
_FileTransferChunk_Object=MibScalar
fileTransferChunk=_FileTransferChunk_Object((1,3,6,1,4,1,28097,1,2,8,6),_FileTransferChunk_Type())
fileTransferChunk.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferChunk.setStatus(_A)
class _FileTransferResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('available',1),('in-progress',2),('nok',3)))
_FileTransferResult_Type.__name__=_D
_FileTransferResult_Object=MibScalar
fileTransferResult=_FileTransferResult_Object((1,3,6,1,4,1,28097,1,2,8,7),_FileTransferResult_Type())
fileTransferResult.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferResult.setStatus(_A)
_FileTransferSession_Type=Integer32
_FileTransferSession_Object=MibScalar
fileTransferSession=_FileTransferSession_Object((1,3,6,1,4,1,28097,1,2,8,8),_FileTransferSession_Type())
fileTransferSession.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferSession.setStatus(_A)
_AdminIdentify_Type=Integer32
_AdminIdentify_Object=MibScalar
adminIdentify=_AdminIdentify_Object((1,3,6,1,4,1,28097,1,2,9),_AdminIdentify_Type())
adminIdentify.setMaxAccess(_B)
if mibBuilder.loadTexts:adminIdentify.setStatus(_A)
_AdminEvents_ObjectIdentity=ObjectIdentity
adminEvents=_AdminEvents_ObjectIdentity((1,3,6,1,4,1,28097,1,2,10))
_AdminEventDisable_Type=OctetString
_AdminEventDisable_Object=MibScalar
adminEventDisable=_AdminEventDisable_Object((1,3,6,1,4,1,28097,1,2,10,1),_AdminEventDisable_Type())
adminEventDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:adminEventDisable.setStatus(_A)
_AdminEventEnable_Type=OctetString
_AdminEventEnable_Object=MibScalar
adminEventEnable=_AdminEventEnable_Object((1,3,6,1,4,1,28097,1,2,10,2),_AdminEventEnable_Type())
adminEventEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:adminEventEnable.setStatus(_A)
_AdminEventTrigger_Type=OctetString
_AdminEventTrigger_Object=MibScalar
adminEventTrigger=_AdminEventTrigger_Object((1,3,6,1,4,1,28097,1,2,10,3),_AdminEventTrigger_Type())
adminEventTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:adminEventTrigger.setStatus(_A)
_AdminTimeZone_ObjectIdentity=ObjectIdentity
adminTimeZone=_AdminTimeZone_ObjectIdentity((1,3,6,1,4,1,28097,1,2,11))
_AdminTimeZoneDBVersion_Type=DisplayString
_AdminTimeZoneDBVersion_Object=MibScalar
adminTimeZoneDBVersion=_AdminTimeZoneDBVersion_Object((1,3,6,1,4,1,28097,1,2,11,1),_AdminTimeZoneDBVersion_Type())
adminTimeZoneDBVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adminTimeZoneDBVersion.setStatus(_A)
class _AdminTimeZoneName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AdminTimeZoneName_Type.__name__=_F
_AdminTimeZoneName_Object=MibScalar
adminTimeZoneName=_AdminTimeZoneName_Object((1,3,6,1,4,1,28097,1,2,11,2),_AdminTimeZoneName_Type())
adminTimeZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:adminTimeZoneName.setStatus(_A)
_AdminSystemDateAndTime_ObjectIdentity=ObjectIdentity
adminSystemDateAndTime=_AdminSystemDateAndTime_ObjectIdentity((1,3,6,1,4,1,28097,1,2,12))
_AdminSystemDateAndTimeLocal_Type=DateAndTime
_AdminSystemDateAndTimeLocal_Object=MibScalar
adminSystemDateAndTimeLocal=_AdminSystemDateAndTimeLocal_Object((1,3,6,1,4,1,28097,1,2,12,1),_AdminSystemDateAndTimeLocal_Type())
adminSystemDateAndTimeLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:adminSystemDateAndTimeLocal.setStatus(_A)
_AdminSystemDateAndTimeUTC_Type=DateAndTime
_AdminSystemDateAndTimeUTC_Object=MibScalar
adminSystemDateAndTimeUTC=_AdminSystemDateAndTimeUTC_Object((1,3,6,1,4,1,28097,1,2,12,2),_AdminSystemDateAndTimeUTC_Type())
adminSystemDateAndTimeUTC.setMaxAccess(_B)
if mibBuilder.loadTexts:adminSystemDateAndTimeUTC.setStatus(_A)
_Os_stat_ObjectIdentity=ObjectIdentity
os_stat=_Os_stat_ObjectIdentity((1,3,6,1,4,1,28097,1,3))
_Os_statFreeHeap_Type=Integer32
_Os_statFreeHeap_Object=MibScalar
os_statFreeHeap=_Os_statFreeHeap_Object((1,3,6,1,4,1,28097,1,3,1),_Os_statFreeHeap_Type())
os_statFreeHeap.setMaxAccess(_C)
if mibBuilder.loadTexts:os_statFreeHeap.setStatus(_A)
_Os_statTotalHeap_Type=Integer32
_Os_statTotalHeap_Object=MibScalar
os_statTotalHeap=_Os_statTotalHeap_Object((1,3,6,1,4,1,28097,1,3,2),_Os_statTotalHeap_Type())
os_statTotalHeap.setMaxAccess(_C)
if mibBuilder.loadTexts:os_statTotalHeap.setStatus(_A)
_Os_statHeapLowWater_Type=Integer32
_Os_statHeapLowWater_Object=MibScalar
os_statHeapLowWater=_Os_statHeapLowWater_Object((1,3,6,1,4,1,28097,1,3,3),_Os_statHeapLowWater_Type())
os_statHeapLowWater.setMaxAccess(_C)
if mibBuilder.loadTexts:os_statHeapLowWater.setStatus(_A)
_Os_statNetpageFree_Type=Integer32
_Os_statNetpageFree_Object=MibScalar
os_statNetpageFree=_Os_statNetpageFree_Object((1,3,6,1,4,1,28097,1,3,4),_Os_statNetpageFree_Type())
os_statNetpageFree.setMaxAccess(_C)
if mibBuilder.loadTexts:os_statNetpageFree.setStatus(_A)
_Os_statNetpageLowWater_Type=Integer32
_Os_statNetpageLowWater_Object=MibScalar
os_statNetpageLowWater=_Os_statNetpageLowWater_Object((1,3,6,1,4,1,28097,1,3,5),_Os_statNetpageLowWater_Type())
os_statNetpageLowWater.setMaxAccess(_C)
if mibBuilder.loadTexts:os_statNetpageLowWater.setStatus(_A)
_ProductSpecific_ObjectIdentity=ObjectIdentity
productSpecific=_ProductSpecific_ObjectIdentity((1,3,6,1,4,1,28097,1,4))
_Wlg_aboard_ObjectIdentity=ObjectIdentity
wlg_aboard=_Wlg_aboard_ObjectIdentity((1,3,6,1,4,1,28097,1,4,1))
class _Wlg_aboard_PW1_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_Wlg_aboard_PW1_state_Type.__name__=_D
_Wlg_aboard_PW1_state_Object=MibScalar
wlg_aboard_PW1_state=_Wlg_aboard_PW1_state_Object((1,3,6,1,4,1,28097,1,4,1,1),_Wlg_aboard_PW1_state_Type())
wlg_aboard_PW1_state.setMaxAccess(_C)
if mibBuilder.loadTexts:wlg_aboard_PW1_state.setStatus(_K)
class _Wlg_aboard_PW2_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_Wlg_aboard_PW2_state_Type.__name__=_D
_Wlg_aboard_PW2_state_Object=MibScalar
wlg_aboard_PW2_state=_Wlg_aboard_PW2_state_Object((1,3,6,1,4,1,28097,1,4,1,2),_Wlg_aboard_PW2_state_Type())
wlg_aboard_PW2_state.setMaxAccess(_C)
if mibBuilder.loadTexts:wlg_aboard_PW2_state.setStatus(_K)
_LanInterface_ObjectIdentity=ObjectIdentity
lanInterface=_LanInterface_ObjectIdentity((1,3,6,1,4,1,28097,1,5))
class _LanInterfaceIpAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_LanInterfaceIpAddrMode_Type.__name__=_D
_LanInterfaceIpAddrMode_Object=MibScalar
lanInterfaceIpAddrMode=_LanInterfaceIpAddrMode_Object((1,3,6,1,4,1,28097,1,5,1),_LanInterfaceIpAddrMode_Type())
lanInterfaceIpAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceIpAddrMode.setStatus(_A)
_LanInterfaceIpAddr_Type=IpAddress
_LanInterfaceIpAddr_Object=MibScalar
lanInterfaceIpAddr=_LanInterfaceIpAddr_Object((1,3,6,1,4,1,28097,1,5,2),_LanInterfaceIpAddr_Type())
lanInterfaceIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceIpAddr.setStatus(_A)
_LanInterfaceSubNetMask_Type=IpAddress
_LanInterfaceSubNetMask_Object=MibScalar
lanInterfaceSubNetMask=_LanInterfaceSubNetMask_Object((1,3,6,1,4,1,28097,1,5,3),_LanInterfaceSubNetMask_Type())
lanInterfaceSubNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceSubNetMask.setStatus(_A)
_LanInterfaceGatewayIp_Type=IpAddress
_LanInterfaceGatewayIp_Object=MibScalar
lanInterfaceGatewayIp=_LanInterfaceGatewayIp_Object((1,3,6,1,4,1,28097,1,5,4),_LanInterfaceGatewayIp_Type())
lanInterfaceGatewayIp.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceGatewayIp.setStatus(_A)
class _LanInterfaceHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_LanInterfaceHostName_Type.__name__=_F
_LanInterfaceHostName_Object=MibScalar
lanInterfaceHostName=_LanInterfaceHostName_Object((1,3,6,1,4,1,28097,1,5,5),_LanInterfaceHostName_Type())
lanInterfaceHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceHostName.setStatus(_A)
class _LanInterfaceLocalDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,33))
_LanInterfaceLocalDomainName_Type.__name__=_F
_LanInterfaceLocalDomainName_Object=MibScalar
lanInterfaceLocalDomainName=_LanInterfaceLocalDomainName_Object((1,3,6,1,4,1,28097,1,5,6),_LanInterfaceLocalDomainName_Type())
lanInterfaceLocalDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceLocalDomainName.setStatus(_A)
_SerialInterface_ObjectIdentity=ObjectIdentity
serialInterface=_SerialInterface_ObjectIdentity((1,3,6,1,4,1,28097,1,6))
class _SerialServicetype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('virtualcom',1),('modbusTcpSlave',2),('modbusTcpMaster',3),('tcpRawPortServer',4),('tcpRawPortClient',5),('udpRawPortServer',6),('serialServiceInvalid',7)))
_SerialServicetype_Type.__name__=_D
_SerialServicetype_Object=MibScalar
serialServicetype=_SerialServicetype_Object((1,3,6,1,4,1,28097,1,6,1),_SerialServicetype_Type())
serialServicetype.setMaxAccess(_B)
if mibBuilder.loadTexts:serialServicetype.setStatus(_A)
_SerialFormat_ObjectIdentity=ObjectIdentity
serialFormat=_SerialFormat_ObjectIdentity((1,3,6,1,4,1,28097,1,6,2))
_SerialFormatBaudRate_Type=Integer32
_SerialFormatBaudRate_Object=MibScalar
serialFormatBaudRate=_SerialFormatBaudRate_Object((1,3,6,1,4,1,28097,1,6,2,1),_SerialFormatBaudRate_Type())
serialFormatBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:serialFormatBaudRate.setStatus(_A)
_SerialFormatDataBit_Type=Integer32
_SerialFormatDataBit_Object=MibScalar
serialFormatDataBit=_SerialFormatDataBit_Object((1,3,6,1,4,1,28097,1,6,2,2),_SerialFormatDataBit_Type())
serialFormatDataBit.setMaxAccess(_B)
if mibBuilder.loadTexts:serialFormatDataBit.setStatus(_A)
class _SerialFormatParityBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('odd',2),('even',3),('mark',4),('space',5)))
_SerialFormatParityBit_Type.__name__=_D
_SerialFormatParityBit_Object=MibScalar
serialFormatParityBit=_SerialFormatParityBit_Object((1,3,6,1,4,1,28097,1,6,2,3),_SerialFormatParityBit_Type())
serialFormatParityBit.setMaxAccess(_B)
if mibBuilder.loadTexts:serialFormatParityBit.setStatus(_A)
_SerialFormatStopBit_Type=Integer32
_SerialFormatStopBit_Object=MibScalar
serialFormatStopBit=_SerialFormatStopBit_Object((1,3,6,1,4,1,28097,1,6,2,4),_SerialFormatStopBit_Type())
serialFormatStopBit.setMaxAccess(_B)
if mibBuilder.loadTexts:serialFormatStopBit.setStatus(_A)
class _SerialElectricalInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rs232',1),('rs422Master',2),('rs422Slave',3),('rs485NoEcho',4),('rs485echo',5)))
_SerialElectricalInterface_Type.__name__=_D
_SerialElectricalInterface_Object=MibScalar
serialElectricalInterface=_SerialElectricalInterface_Object((1,3,6,1,4,1,28097,1,6,2,5),_SerialElectricalInterface_Type())
serialElectricalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:serialElectricalInterface.setStatus(_A)
_SerialSendTriggers_ObjectIdentity=ObjectIdentity
serialSendTriggers=_SerialSendTriggers_ObjectIdentity((1,3,6,1,4,1,28097,1,6,3))
_SerialSendTriggerCharcount_ObjectIdentity=ObjectIdentity
serialSendTriggerCharcount=_SerialSendTriggerCharcount_ObjectIdentity((1,3,6,1,4,1,28097,1,6,3,1))
class _SendTriggerCharCountEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_SendTriggerCharCountEnable_Type.__name__=_D
_SendTriggerCharCountEnable_Object=MibScalar
sendTriggerCharCountEnable=_SendTriggerCharCountEnable_Object((1,3,6,1,4,1,28097,1,6,3,1,1),_SendTriggerCharCountEnable_Type())
sendTriggerCharCountEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerCharCountEnable.setStatus(_A)
_SendTriggerCharCountValue_Type=Integer32
_SendTriggerCharCountValue_Object=MibScalar
sendTriggerCharCountValue=_SendTriggerCharCountValue_Object((1,3,6,1,4,1,28097,1,6,3,1,2),_SendTriggerCharCountValue_Type())
sendTriggerCharCountValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerCharCountValue.setStatus(_A)
_SerialSendTriggerIdleDelay_ObjectIdentity=ObjectIdentity
serialSendTriggerIdleDelay=_SerialSendTriggerIdleDelay_ObjectIdentity((1,3,6,1,4,1,28097,1,6,3,2))
class _SendTriggerIdleDelayEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_SendTriggerIdleDelayEnable_Type.__name__=_D
_SendTriggerIdleDelayEnable_Object=MibScalar
sendTriggerIdleDelayEnable=_SendTriggerIdleDelayEnable_Object((1,3,6,1,4,1,28097,1,6,3,2,1),_SendTriggerIdleDelayEnable_Type())
sendTriggerIdleDelayEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerIdleDelayEnable.setStatus(_A)
_SendTriggerIdleDelayValue_Type=Integer32
_SendTriggerIdleDelayValue_Object=MibScalar
sendTriggerIdleDelayValue=_SendTriggerIdleDelayValue_Object((1,3,6,1,4,1,28097,1,6,3,2,2),_SendTriggerIdleDelayValue_Type())
sendTriggerIdleDelayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerIdleDelayValue.setStatus(_A)
class _SendTriggerIdleDelayUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('charTime',1),(_A6,2)))
_SendTriggerIdleDelayUnit_Type.__name__=_D
_SendTriggerIdleDelayUnit_Object=MibScalar
sendTriggerIdleDelayUnit=_SendTriggerIdleDelayUnit_Object((1,3,6,1,4,1,28097,1,6,3,2,3),_SendTriggerIdleDelayUnit_Type())
sendTriggerIdleDelayUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerIdleDelayUnit.setStatus(_A)
_SerialSendTriggerFrameDelay_ObjectIdentity=ObjectIdentity
serialSendTriggerFrameDelay=_SerialSendTriggerFrameDelay_ObjectIdentity((1,3,6,1,4,1,28097,1,6,3,3))
class _SendTriggerFrameDelayEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_SendTriggerFrameDelayEnable_Type.__name__=_D
_SendTriggerFrameDelayEnable_Object=MibScalar
sendTriggerFrameDelayEnable=_SendTriggerFrameDelayEnable_Object((1,3,6,1,4,1,28097,1,6,3,3,1),_SendTriggerFrameDelayEnable_Type())
sendTriggerFrameDelayEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerFrameDelayEnable.setStatus(_A)
_SendTriggerFrameDelayValue_Type=Integer32
_SendTriggerFrameDelayValue_Object=MibScalar
sendTriggerFrameDelayValue=_SendTriggerFrameDelayValue_Object((1,3,6,1,4,1,28097,1,6,3,3,2),_SendTriggerFrameDelayValue_Type())
sendTriggerFrameDelayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerFrameDelayValue.setStatus(_A)
class _SendTriggerFrameDelayUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('charTime',1),(_A6,2)))
_SendTriggerFrameDelayUnit_Type.__name__=_D
_SendTriggerFrameDelayUnit_Object=MibScalar
sendTriggerFrameDelayUnit=_SendTriggerFrameDelayUnit_Object((1,3,6,1,4,1,28097,1,6,3,3,3),_SendTriggerFrameDelayUnit_Type())
sendTriggerFrameDelayUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:sendTriggerFrameDelayUnit.setStatus(_A)
_SerialServiceVirtualCom_ObjectIdentity=ObjectIdentity
serialServiceVirtualCom=_SerialServiceVirtualCom_ObjectIdentity((1,3,6,1,4,1,28097,1,6,4))
_SerialServiceModbusSlave_ObjectIdentity=ObjectIdentity
serialServiceModbusSlave=_SerialServiceModbusSlave_ObjectIdentity((1,3,6,1,4,1,28097,1,6,5))
class _ModbusSlaveFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('rtu',2)))
_ModbusSlaveFormat_Type.__name__=_D
_ModbusSlaveFormat_Object=MibScalar
modbusSlaveFormat=_ModbusSlaveFormat_Object((1,3,6,1,4,1,28097,1,6,5,1),_ModbusSlaveFormat_Type())
modbusSlaveFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusSlaveFormat.setStatus(_A)
_ModbusSlaveSerialTransactionTimeout_Type=Integer32
_ModbusSlaveSerialTransactionTimeout_Object=MibScalar
modbusSlaveSerialTransactionTimeout=_ModbusSlaveSerialTransactionTimeout_Object((1,3,6,1,4,1,28097,1,6,5,2),_ModbusSlaveSerialTransactionTimeout_Type())
modbusSlaveSerialTransactionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusSlaveSerialTransactionTimeout.setStatus(_A)
_SerialServiceModbusMaster_ObjectIdentity=ObjectIdentity
serialServiceModbusMaster=_SerialServiceModbusMaster_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6))
class _ModbusMasterFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('rtu',2)))
_ModbusMasterFormat_Type.__name__=_D
_ModbusMasterFormat_Object=MibScalar
modbusMasterFormat=_ModbusMasterFormat_Object((1,3,6,1,4,1,28097,1,6,6,1),_ModbusMasterFormat_Type())
modbusMasterFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusMasterFormat.setStatus(_A)
_ModbusMasterTransactionTimeout_Type=Integer32
_ModbusMasterTransactionTimeout_Object=MibScalar
modbusMasterTransactionTimeout=_ModbusMasterTransactionTimeout_Object((1,3,6,1,4,1,28097,1,6,6,2),_ModbusMasterTransactionTimeout_Type())
modbusMasterTransactionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusMasterTransactionTimeout.setStatus(_A)
_ModbusMasterForwardingTable_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable=_ModbusMasterForwardingTable_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3))
_ModbusMasterForwardingTable_Rule1_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule1=_ModbusMasterForwardingTable_Rule1_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,1))
_MmForwardingTable_Rule1_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule1_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule1_FirstLocalAddr=_MmForwardingTable_Rule1_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,1,1),_MmForwardingTable_Rule1_FirstLocalAddr_Type())
mmForwardingTable_Rule1_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule1_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule1_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule1_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule1_LastLocalAddr=_MmForwardingTable_Rule1_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,1,2),_MmForwardingTable_Rule1_LastLocalAddr_Type())
mmForwardingTable_Rule1_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule1_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule1_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule1_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule1_FirstRemoteAddr=_MmForwardingTable_Rule1_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,1,3),_MmForwardingTable_Rule1_FirstRemoteAddr_Type())
mmForwardingTable_Rule1_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule1_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule1_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule1_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule1_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule1_SlaveIpAddrIncrement=_MmForwardingTable_Rule1_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,1,4),_MmForwardingTable_Rule1_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule1_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule1_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule1_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule1_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule1_SlaveIpAddr=_MmForwardingTable_Rule1_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,1,5),_MmForwardingTable_Rule1_SlaveIpAddr_Type())
mmForwardingTable_Rule1_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule1_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule2_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule2=_ModbusMasterForwardingTable_Rule2_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,2))
_MmForwardingTable_Rule2_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule2_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule2_FirstLocalAddr=_MmForwardingTable_Rule2_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,2,1),_MmForwardingTable_Rule2_FirstLocalAddr_Type())
mmForwardingTable_Rule2_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule2_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule2_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule2_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule2_LastLocalAddr=_MmForwardingTable_Rule2_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,2,2),_MmForwardingTable_Rule2_LastLocalAddr_Type())
mmForwardingTable_Rule2_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule2_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule2_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule2_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule2_FirstRemoteAddr=_MmForwardingTable_Rule2_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,2,3),_MmForwardingTable_Rule2_FirstRemoteAddr_Type())
mmForwardingTable_Rule2_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule2_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule2_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule2_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule2_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule2_SlaveIpAddrIncrement=_MmForwardingTable_Rule2_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,2,4),_MmForwardingTable_Rule2_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule2_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule2_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule2_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule2_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule2_SlaveIpAddr=_MmForwardingTable_Rule2_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,2,5),_MmForwardingTable_Rule2_SlaveIpAddr_Type())
mmForwardingTable_Rule2_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule2_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule3_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule3=_ModbusMasterForwardingTable_Rule3_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,3))
_MmForwardingTable_Rule3_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule3_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule3_FirstLocalAddr=_MmForwardingTable_Rule3_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,3,1),_MmForwardingTable_Rule3_FirstLocalAddr_Type())
mmForwardingTable_Rule3_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule3_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule3_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule3_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule3_LastLocalAddr=_MmForwardingTable_Rule3_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,3,2),_MmForwardingTable_Rule3_LastLocalAddr_Type())
mmForwardingTable_Rule3_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule3_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule3_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule3_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule3_FirstRemoteAddr=_MmForwardingTable_Rule3_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,3,3),_MmForwardingTable_Rule3_FirstRemoteAddr_Type())
mmForwardingTable_Rule3_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule3_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule3_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule3_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule3_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule3_SlaveIpAddrIncrement=_MmForwardingTable_Rule3_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,3,4),_MmForwardingTable_Rule3_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule3_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule3_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule3_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule3_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule3_SlaveIpAddr=_MmForwardingTable_Rule3_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,3,5),_MmForwardingTable_Rule3_SlaveIpAddr_Type())
mmForwardingTable_Rule3_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule3_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule4_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule4=_ModbusMasterForwardingTable_Rule4_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,4))
_MmForwardingTable_Rule4_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule4_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule4_FirstLocalAddr=_MmForwardingTable_Rule4_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,4,1),_MmForwardingTable_Rule4_FirstLocalAddr_Type())
mmForwardingTable_Rule4_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule4_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule4_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule4_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule4_LastLocalAddr=_MmForwardingTable_Rule4_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,4,2),_MmForwardingTable_Rule4_LastLocalAddr_Type())
mmForwardingTable_Rule4_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule4_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule4_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule4_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule4_FirstRemoteAddr=_MmForwardingTable_Rule4_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,4,3),_MmForwardingTable_Rule4_FirstRemoteAddr_Type())
mmForwardingTable_Rule4_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule4_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule4_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule4_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule4_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule4_SlaveIpAddrIncrement=_MmForwardingTable_Rule4_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,4,4),_MmForwardingTable_Rule4_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule4_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule4_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule4_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule4_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule4_SlaveIpAddr=_MmForwardingTable_Rule4_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,4,5),_MmForwardingTable_Rule4_SlaveIpAddr_Type())
mmForwardingTable_Rule4_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule4_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule5_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule5=_ModbusMasterForwardingTable_Rule5_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,5))
_MmForwardingTable_Rule5_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule5_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule5_FirstLocalAddr=_MmForwardingTable_Rule5_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,5,1),_MmForwardingTable_Rule5_FirstLocalAddr_Type())
mmForwardingTable_Rule5_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule5_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule5_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule5_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule5_LastLocalAddr=_MmForwardingTable_Rule5_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,5,2),_MmForwardingTable_Rule5_LastLocalAddr_Type())
mmForwardingTable_Rule5_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule5_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule5_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule5_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule5_FirstRemoteAddr=_MmForwardingTable_Rule5_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,5,3),_MmForwardingTable_Rule5_FirstRemoteAddr_Type())
mmForwardingTable_Rule5_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule5_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule5_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule5_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule5_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule5_SlaveIpAddrIncrement=_MmForwardingTable_Rule5_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,5,4),_MmForwardingTable_Rule5_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule5_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule5_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule5_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule5_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule5_SlaveIpAddr=_MmForwardingTable_Rule5_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,5,5),_MmForwardingTable_Rule5_SlaveIpAddr_Type())
mmForwardingTable_Rule5_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule5_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule6_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule6=_ModbusMasterForwardingTable_Rule6_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,6))
_MmForwardingTable_Rule6_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule6_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule6_FirstLocalAddr=_MmForwardingTable_Rule6_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,6,1),_MmForwardingTable_Rule6_FirstLocalAddr_Type())
mmForwardingTable_Rule6_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule6_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule6_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule6_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule6_LastLocalAddr=_MmForwardingTable_Rule6_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,6,2),_MmForwardingTable_Rule6_LastLocalAddr_Type())
mmForwardingTable_Rule6_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule6_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule6_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule6_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule6_FirstRemoteAddr=_MmForwardingTable_Rule6_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,6,3),_MmForwardingTable_Rule6_FirstRemoteAddr_Type())
mmForwardingTable_Rule6_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule6_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule6_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule6_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule6_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule6_SlaveIpAddrIncrement=_MmForwardingTable_Rule6_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,6,4),_MmForwardingTable_Rule6_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule6_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule6_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule6_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule6_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule6_SlaveIpAddr=_MmForwardingTable_Rule6_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,6,5),_MmForwardingTable_Rule6_SlaveIpAddr_Type())
mmForwardingTable_Rule6_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule6_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule7_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule7=_ModbusMasterForwardingTable_Rule7_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,7))
_MmForwardingTable_Rule7_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule7_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule7_FirstLocalAddr=_MmForwardingTable_Rule7_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,7,1),_MmForwardingTable_Rule7_FirstLocalAddr_Type())
mmForwardingTable_Rule7_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule7_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule7_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule7_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule7_LastLocalAddr=_MmForwardingTable_Rule7_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,7,2),_MmForwardingTable_Rule7_LastLocalAddr_Type())
mmForwardingTable_Rule7_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule7_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule7_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule7_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule7_FirstRemoteAddr=_MmForwardingTable_Rule7_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,7,3),_MmForwardingTable_Rule7_FirstRemoteAddr_Type())
mmForwardingTable_Rule7_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule7_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule7_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule7_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule7_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule7_SlaveIpAddrIncrement=_MmForwardingTable_Rule7_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,7,4),_MmForwardingTable_Rule7_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule7_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule7_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule7_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule7_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule7_SlaveIpAddr=_MmForwardingTable_Rule7_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,7,5),_MmForwardingTable_Rule7_SlaveIpAddr_Type())
mmForwardingTable_Rule7_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule7_SlaveIpAddr.setStatus(_A)
_ModbusMasterForwardingTable_Rule8_ObjectIdentity=ObjectIdentity
modbusMasterForwardingTable_Rule8=_ModbusMasterForwardingTable_Rule8_ObjectIdentity((1,3,6,1,4,1,28097,1,6,6,3,8))
_MmForwardingTable_Rule8_FirstLocalAddr_Type=Integer32
_MmForwardingTable_Rule8_FirstLocalAddr_Object=MibScalar
mmForwardingTable_Rule8_FirstLocalAddr=_MmForwardingTable_Rule8_FirstLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,8,1),_MmForwardingTable_Rule8_FirstLocalAddr_Type())
mmForwardingTable_Rule8_FirstLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule8_FirstLocalAddr.setStatus(_A)
_MmForwardingTable_Rule8_LastLocalAddr_Type=Integer32
_MmForwardingTable_Rule8_LastLocalAddr_Object=MibScalar
mmForwardingTable_Rule8_LastLocalAddr=_MmForwardingTable_Rule8_LastLocalAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,8,2),_MmForwardingTable_Rule8_LastLocalAddr_Type())
mmForwardingTable_Rule8_LastLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule8_LastLocalAddr.setStatus(_A)
_MmForwardingTable_Rule8_FirstRemoteAddr_Type=Integer32
_MmForwardingTable_Rule8_FirstRemoteAddr_Object=MibScalar
mmForwardingTable_Rule8_FirstRemoteAddr=_MmForwardingTable_Rule8_FirstRemoteAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,8,3),_MmForwardingTable_Rule8_FirstRemoteAddr_Type())
mmForwardingTable_Rule8_FirstRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule8_FirstRemoteAddr.setStatus(_A)
class _MmForwardingTable_Rule8_SlaveIpAddrIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_MmForwardingTable_Rule8_SlaveIpAddrIncrement_Type.__name__=_D
_MmForwardingTable_Rule8_SlaveIpAddrIncrement_Object=MibScalar
mmForwardingTable_Rule8_SlaveIpAddrIncrement=_MmForwardingTable_Rule8_SlaveIpAddrIncrement_Object((1,3,6,1,4,1,28097,1,6,6,3,8,4),_MmForwardingTable_Rule8_SlaveIpAddrIncrement_Type())
mmForwardingTable_Rule8_SlaveIpAddrIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule8_SlaveIpAddrIncrement.setStatus(_A)
_MmForwardingTable_Rule8_SlaveIpAddr_Type=IpAddress
_MmForwardingTable_Rule8_SlaveIpAddr_Object=MibScalar
mmForwardingTable_Rule8_SlaveIpAddr=_MmForwardingTable_Rule8_SlaveIpAddr_Object((1,3,6,1,4,1,28097,1,6,6,3,8,5),_MmForwardingTable_Rule8_SlaveIpAddr_Type())
mmForwardingTable_Rule8_SlaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mmForwardingTable_Rule8_SlaveIpAddr.setStatus(_A)
_SerialServiceTcpRawPortServer_ObjectIdentity=ObjectIdentity
serialServiceTcpRawPortServer=_SerialServiceTcpRawPortServer_ObjectIdentity((1,3,6,1,4,1,28097,1,6,7))
_TcpRawServerSerialExtraConfig_ObjectIdentity=ObjectIdentity
tcpRawServerSerialExtraConfig=_TcpRawServerSerialExtraConfig_ObjectIdentity((1,3,6,1,4,1,28097,1,6,7,1))
class _TrsExtraConfigDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_O,1),('tcpConnected',2),(_h,4),(_V,5),(_U,6)))
_TrsExtraConfigDTR_Type.__name__=_D
_TrsExtraConfigDTR_Object=MibScalar
trsExtraConfigDTR=_TrsExtraConfigDTR_Object((1,3,6,1,4,1,28097,1,6,7,1,1),_TrsExtraConfigDTR_Type())
trsExtraConfigDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:trsExtraConfigDTR.setStatus(_A)
class _TrsExtraConfigRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_O,1),(_n,2),(_h,4),(_V,5),(_U,6)))
_TrsExtraConfigRTS_Type.__name__=_D
_TrsExtraConfigRTS_Object=MibScalar
trsExtraConfigRTS=_TrsExtraConfigRTS_Object((1,3,6,1,4,1,28097,1,6,7,1,2),_TrsExtraConfigRTS_Type())
trsExtraConfigRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:trsExtraConfigRTS.setStatus(_A)
class _TrsExtraConfigDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('acceptCall',2)))
_TrsExtraConfigDSR_Type.__name__=_D
_TrsExtraConfigDSR_Object=MibScalar
trsExtraConfigDSR=_TrsExtraConfigDSR_Object((1,3,6,1,4,1,28097,1,6,7,1,3),_TrsExtraConfigDSR_Type())
trsExtraConfigDSR.setMaxAccess(_B)
if mibBuilder.loadTexts:trsExtraConfigDSR.setStatus(_A)
class _TrsExtraConfigCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_T,1),(_o,4)))
_TrsExtraConfigCTS_Type.__name__=_D
_TrsExtraConfigCTS_Object=MibScalar
trsExtraConfigCTS=_TrsExtraConfigCTS_Object((1,3,6,1,4,1,28097,1,6,7,1,4),_TrsExtraConfigCTS_Type())
trsExtraConfigCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:trsExtraConfigCTS.setStatus(_A)
class _TrsExtraConfigDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('rxData',2)))
_TrsExtraConfigDCD_Type.__name__=_D
_TrsExtraConfigDCD_Object=MibScalar
trsExtraConfigDCD=_TrsExtraConfigDCD_Object((1,3,6,1,4,1,28097,1,6,7,1,5),_TrsExtraConfigDCD_Type())
trsExtraConfigDCD.setMaxAccess(_B)
if mibBuilder.loadTexts:trsExtraConfigDCD.setStatus(_A)
class _TrsExtraConfigXonXoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7)));namedValues=NamedValues(*((_T,1),(_p,7)))
_TrsExtraConfigXonXoff_Type.__name__=_D
_TrsExtraConfigXonXoff_Object=MibScalar
trsExtraConfigXonXoff=_TrsExtraConfigXonXoff_Object((1,3,6,1,4,1,28097,1,6,7,1,6),_TrsExtraConfigXonXoff_Type())
trsExtraConfigXonXoff.setMaxAccess(_B)
if mibBuilder.loadTexts:trsExtraConfigXonXoff.setStatus(_A)
_SerialServiceTcpRawPortClient_ObjectIdentity=ObjectIdentity
serialServiceTcpRawPortClient=_SerialServiceTcpRawPortClient_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8))
_TcpRawClientSerialExtraConfig_ObjectIdentity=ObjectIdentity
tcpRawClientSerialExtraConfig=_TcpRawClientSerialExtraConfig_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,1))
class _TrcExtraConfigDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,6)));namedValues=NamedValues(*((_O,1),(_V,5),(_U,6)))
_TrcExtraConfigDTR_Type.__name__=_D
_TrcExtraConfigDTR_Object=MibScalar
trcExtraConfigDTR=_TrcExtraConfigDTR_Object((1,3,6,1,4,1,28097,1,6,8,1,1),_TrcExtraConfigDTR_Type())
trcExtraConfigDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:trcExtraConfigDTR.setStatus(_A)
class _TrcExtraConfigRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_O,1),(_n,2),(_h,4),(_V,5),(_U,6)))
_TrcExtraConfigRTS_Type.__name__=_D
_TrcExtraConfigRTS_Object=MibScalar
trcExtraConfigRTS=_TrcExtraConfigRTS_Object((1,3,6,1,4,1,28097,1,6,8,1,2),_TrcExtraConfigRTS_Type())
trcExtraConfigRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:trcExtraConfigRTS.setStatus(_A)
class _TrcExtraConfigCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_T,1),(_o,4)))
_TrcExtraConfigCTS_Type.__name__=_D
_TrcExtraConfigCTS_Object=MibScalar
trcExtraConfigCTS=_TrcExtraConfigCTS_Object((1,3,6,1,4,1,28097,1,6,8,1,4),_TrcExtraConfigCTS_Type())
trcExtraConfigCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:trcExtraConfigCTS.setStatus(_A)
class _TrcExtraConfigDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('rxData',2)))
_TrcExtraConfigDCD_Type.__name__=_D
_TrcExtraConfigDCD_Object=MibScalar
trcExtraConfigDCD=_TrcExtraConfigDCD_Object((1,3,6,1,4,1,28097,1,6,8,1,5),_TrcExtraConfigDCD_Type())
trcExtraConfigDCD.setMaxAccess(_B)
if mibBuilder.loadTexts:trcExtraConfigDCD.setStatus(_A)
class _TrcExtraConfigXonXoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7)));namedValues=NamedValues(*((_T,1),(_p,7)))
_TrcExtraConfigXonXoff_Type.__name__=_D
_TrcExtraConfigXonXoff_Object=MibScalar
trcExtraConfigXonXoff=_TrcExtraConfigXonXoff_Object((1,3,6,1,4,1,28097,1,6,8,1,6),_TrcExtraConfigXonXoff_Type())
trcExtraConfigXonXoff.setMaxAccess(_B)
if mibBuilder.loadTexts:trcExtraConfigXonXoff.setStatus(_A)
_TcpRawClientConnectionTimeout_Type=Integer32
_TcpRawClientConnectionTimeout_Object=MibScalar
tcpRawClientConnectionTimeout=_TcpRawClientConnectionTimeout_Object((1,3,6,1,4,1,28097,1,6,8,4),_TcpRawClientConnectionTimeout_Type())
tcpRawClientConnectionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawClientConnectionTimeout.setStatus(_A)
_TcpRawClientPollPeriode_Type=Integer32
_TcpRawClientPollPeriode_Object=MibScalar
tcpRawClientPollPeriode=_TcpRawClientPollPeriode_Object((1,3,6,1,4,1,28097,1,6,8,5),_TcpRawClientPollPeriode_Type())
tcpRawClientPollPeriode.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawClientPollPeriode.setStatus(_A)
class _TcpRawClientDSRUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notUsed',1),('graceful',2),('fast',3)))
_TcpRawClientDSRUse_Type.__name__=_D
_TcpRawClientDSRUse_Object=MibScalar
tcpRawClientDSRUse=_TcpRawClientDSRUse_Object((1,3,6,1,4,1,28097,1,6,8,6),_TcpRawClientDSRUse_Type())
tcpRawClientDSRUse.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawClientDSRUse.setStatus(_A)
_TcpRawClientRemoteServers_ObjectIdentity=ObjectIdentity
tcpRawClientRemoteServers=_TcpRawClientRemoteServers_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7))
_TcpRawClientServer1_ObjectIdentity=ObjectIdentity
tcpRawClientServer1=_TcpRawClientServer1_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,1))
_TcpRawClienServer1_IpAddress_Type=IpAddress
_TcpRawClienServer1_IpAddress_Object=MibScalar
tcpRawClienServer1_IpAddress=_TcpRawClienServer1_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,1,1),_TcpRawClienServer1_IpAddress_Type())
tcpRawClienServer1_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawClienServer1_IpAddress.setStatus(_A)
_TcpRawclientServer1_TcpPort_Type=Integer32
_TcpRawclientServer1_TcpPort_Object=MibScalar
tcpRawclientServer1_TcpPort=_TcpRawclientServer1_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,1,2),_TcpRawclientServer1_TcpPort_Type())
tcpRawclientServer1_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer1_TcpPort.setStatus(_A)
_TcpRawClientServer2_ObjectIdentity=ObjectIdentity
tcpRawClientServer2=_TcpRawClientServer2_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,2))
_TcpRawclientServer2_IpAddress_Type=IpAddress
_TcpRawclientServer2_IpAddress_Object=MibScalar
tcpRawclientServer2_IpAddress=_TcpRawclientServer2_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,2,1),_TcpRawclientServer2_IpAddress_Type())
tcpRawclientServer2_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer2_IpAddress.setStatus(_A)
_TcpRawclientServer2_TcpPort_Type=Integer32
_TcpRawclientServer2_TcpPort_Object=MibScalar
tcpRawclientServer2_TcpPort=_TcpRawclientServer2_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,2,2),_TcpRawclientServer2_TcpPort_Type())
tcpRawclientServer2_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer2_TcpPort.setStatus(_A)
_TcpRawClientServer3_ObjectIdentity=ObjectIdentity
tcpRawClientServer3=_TcpRawClientServer3_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,3))
_TcpRawclientServer3_IpAddress_Type=IpAddress
_TcpRawclientServer3_IpAddress_Object=MibScalar
tcpRawclientServer3_IpAddress=_TcpRawclientServer3_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,3,1),_TcpRawclientServer3_IpAddress_Type())
tcpRawclientServer3_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer3_IpAddress.setStatus(_A)
_TcpRawclientServer3_TcpPort_Type=Integer32
_TcpRawclientServer3_TcpPort_Object=MibScalar
tcpRawclientServer3_TcpPort=_TcpRawclientServer3_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,3,2),_TcpRawclientServer3_TcpPort_Type())
tcpRawclientServer3_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer3_TcpPort.setStatus(_A)
_TcpRawClientServer4_ObjectIdentity=ObjectIdentity
tcpRawClientServer4=_TcpRawClientServer4_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,4))
_TcpRawclientServer4_IpAddress_Type=IpAddress
_TcpRawclientServer4_IpAddress_Object=MibScalar
tcpRawclientServer4_IpAddress=_TcpRawclientServer4_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,4,1),_TcpRawclientServer4_IpAddress_Type())
tcpRawclientServer4_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer4_IpAddress.setStatus(_A)
_TcpRawclientServer4_TcpPort_Type=Integer32
_TcpRawclientServer4_TcpPort_Object=MibScalar
tcpRawclientServer4_TcpPort=_TcpRawclientServer4_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,4,2),_TcpRawclientServer4_TcpPort_Type())
tcpRawclientServer4_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer4_TcpPort.setStatus(_A)
_TcpRawClientServer5_ObjectIdentity=ObjectIdentity
tcpRawClientServer5=_TcpRawClientServer5_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,5))
_TcpRawclientServer5_IpAddress_Type=IpAddress
_TcpRawclientServer5_IpAddress_Object=MibScalar
tcpRawclientServer5_IpAddress=_TcpRawclientServer5_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,5,1),_TcpRawclientServer5_IpAddress_Type())
tcpRawclientServer5_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer5_IpAddress.setStatus(_A)
_TcpRawclientServer5_TcpPort_Type=Integer32
_TcpRawclientServer5_TcpPort_Object=MibScalar
tcpRawclientServer5_TcpPort=_TcpRawclientServer5_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,5,2),_TcpRawclientServer5_TcpPort_Type())
tcpRawclientServer5_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer5_TcpPort.setStatus(_A)
_TcpRawClientServer6_ObjectIdentity=ObjectIdentity
tcpRawClientServer6=_TcpRawClientServer6_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,6))
_TcpRawclientServer6_IpAddress_Type=IpAddress
_TcpRawclientServer6_IpAddress_Object=MibScalar
tcpRawclientServer6_IpAddress=_TcpRawclientServer6_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,6,1),_TcpRawclientServer6_IpAddress_Type())
tcpRawclientServer6_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer6_IpAddress.setStatus(_A)
_TcpRawclientServer6_TcpPort_Type=Integer32
_TcpRawclientServer6_TcpPort_Object=MibScalar
tcpRawclientServer6_TcpPort=_TcpRawclientServer6_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,6,2),_TcpRawclientServer6_TcpPort_Type())
tcpRawclientServer6_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer6_TcpPort.setStatus(_A)
_TcpRawClientServer7_ObjectIdentity=ObjectIdentity
tcpRawClientServer7=_TcpRawClientServer7_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,7))
_TcpRawclientServer7_IpAddress_Type=IpAddress
_TcpRawclientServer7_IpAddress_Object=MibScalar
tcpRawclientServer7_IpAddress=_TcpRawclientServer7_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,7,1),_TcpRawclientServer7_IpAddress_Type())
tcpRawclientServer7_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer7_IpAddress.setStatus(_A)
_TcpRawclientServer7_TcpPort_Type=Integer32
_TcpRawclientServer7_TcpPort_Object=MibScalar
tcpRawclientServer7_TcpPort=_TcpRawclientServer7_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,7,2),_TcpRawclientServer7_TcpPort_Type())
tcpRawclientServer7_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer7_TcpPort.setStatus(_A)
_TcpRawClientServer8_ObjectIdentity=ObjectIdentity
tcpRawClientServer8=_TcpRawClientServer8_ObjectIdentity((1,3,6,1,4,1,28097,1,6,8,7,8))
_TcpRawclientServer8_IpAddress_Type=IpAddress
_TcpRawclientServer8_IpAddress_Object=MibScalar
tcpRawclientServer8_IpAddress=_TcpRawclientServer8_IpAddress_Object((1,3,6,1,4,1,28097,1,6,8,7,8,1),_TcpRawclientServer8_IpAddress_Type())
tcpRawclientServer8_IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer8_IpAddress.setStatus(_A)
_TcpRawclientServer8_TcpPort_Type=Integer32
_TcpRawclientServer8_TcpPort_Object=MibScalar
tcpRawclientServer8_TcpPort=_TcpRawclientServer8_TcpPort_Object((1,3,6,1,4,1,28097,1,6,8,7,8,2),_TcpRawclientServer8_TcpPort_Type())
tcpRawclientServer8_TcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpRawclientServer8_TcpPort.setStatus(_A)
_SerialServiceUdpRawPortServer_ObjectIdentity=ObjectIdentity
serialServiceUdpRawPortServer=_SerialServiceUdpRawPortServer_ObjectIdentity((1,3,6,1,4,1,28097,1,6,9))
_UdpRawServerSerialExtraConfig_ObjectIdentity=ObjectIdentity
udpRawServerSerialExtraConfig=_UdpRawServerSerialExtraConfig_ObjectIdentity((1,3,6,1,4,1,28097,1,6,9,1))
class _UrsExtraConfigDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,6)));namedValues=NamedValues(*((_O,1),(_V,5),(_U,6)))
_UrsExtraConfigDTR_Type.__name__=_D
_UrsExtraConfigDTR_Object=MibScalar
ursExtraConfigDTR=_UrsExtraConfigDTR_Object((1,3,6,1,4,1,28097,1,6,9,1,1),_UrsExtraConfigDTR_Type())
ursExtraConfigDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:ursExtraConfigDTR.setStatus(_A)
class _UrsExtraConfigRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_O,1),(_n,2),(_h,4),(_V,5),(_U,6)))
_UrsExtraConfigRTS_Type.__name__=_D
_UrsExtraConfigRTS_Object=MibScalar
ursExtraConfigRTS=_UrsExtraConfigRTS_Object((1,3,6,1,4,1,28097,1,6,9,1,2),_UrsExtraConfigRTS_Type())
ursExtraConfigRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:ursExtraConfigRTS.setStatus(_A)
class _UrsExtraConfigCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_T,1),(_o,4)))
_UrsExtraConfigCTS_Type.__name__=_D
_UrsExtraConfigCTS_Object=MibScalar
ursExtraConfigCTS=_UrsExtraConfigCTS_Object((1,3,6,1,4,1,28097,1,6,9,1,3),_UrsExtraConfigCTS_Type())
ursExtraConfigCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:ursExtraConfigCTS.setStatus(_A)
class _UrsExtraConfigXonXoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7)));namedValues=NamedValues(*((_T,1),(_p,7)))
_UrsExtraConfigXonXoff_Type.__name__=_D
_UrsExtraConfigXonXoff_Object=MibScalar
ursExtraConfigXonXoff=_UrsExtraConfigXonXoff_Object((1,3,6,1,4,1,28097,1,6,9,1,4),_UrsExtraConfigXonXoff_Type())
ursExtraConfigXonXoff.setMaxAccess(_B)
if mibBuilder.loadTexts:ursExtraConfigXonXoff.setStatus(_A)
_UdpRawServerRemoteIP_Type=IpAddress
_UdpRawServerRemoteIP_Object=MibScalar
udpRawServerRemoteIP=_UdpRawServerRemoteIP_Object((1,3,6,1,4,1,28097,1,6,9,2),_UdpRawServerRemoteIP_Type())
udpRawServerRemoteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:udpRawServerRemoteIP.setStatus(_A)
_UdpRawServerRemotePort_Type=Integer32
_UdpRawServerRemotePort_Object=MibScalar
udpRawServerRemotePort=_UdpRawServerRemotePort_Object((1,3,6,1,4,1,28097,1,6,9,3),_UdpRawServerRemotePort_Type())
udpRawServerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:udpRawServerRemotePort.setStatus(_A)
_UdpRawServerLocalPort_Type=Integer32
_UdpRawServerLocalPort_Object=MibScalar
udpRawServerLocalPort=_UdpRawServerLocalPort_Object((1,3,6,1,4,1,28097,1,6,9,4),_UdpRawServerLocalPort_Type())
udpRawServerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:udpRawServerLocalPort.setStatus(_A)
_AcksysInternals_ObjectIdentity=ObjectIdentity
acksysInternals=_AcksysInternals_ObjectIdentity((1,3,6,1,4,1,28097,2))
_InternalUniqueID_Type=PhysAddress
_InternalUniqueID_Object=MibScalar
internalUniqueID=_InternalUniqueID_Object((1,3,6,1,4,1,28097,2,1),_InternalUniqueID_Type())
internalUniqueID.setMaxAccess(_C)
if mibBuilder.loadTexts:internalUniqueID.setStatus(_A)
_InternalSerial_Type=Integer32
_InternalSerial_Object=MibScalar
internalSerial=_InternalSerial_Object((1,3,6,1,4,1,28097,2,2),_InternalSerial_Type())
internalSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSerial.setStatus(_A)
_InternalWlanChange_Type=Integer32
_InternalWlanChange_Object=MibScalar
internalWlanChange=_InternalWlanChange_Object((1,3,6,1,4,1,28097,2,3),_InternalWlanChange_Type())
internalWlanChange.setMaxAccess(_C)
if mibBuilder.loadTexts:internalWlanChange.setStatus(_A)
_InternalRadioChange_Type=Integer32
_InternalRadioChange_Object=MibScalar
internalRadioChange=_InternalRadioChange_Object((1,3,6,1,4,1,28097,2,4),_InternalRadioChange_Type())
internalRadioChange.setMaxAccess(_C)
if mibBuilder.loadTexts:internalRadioChange.setStatus(_A)
_InternalSerialTest_Type=Integer32
_InternalSerialTest_Object=MibScalar
internalSerialTest=_InternalSerialTest_Object((1,3,6,1,4,1,28097,2,5),_InternalSerialTest_Type())
internalSerialTest.setMaxAccess(_B)
if mibBuilder.loadTexts:internalSerialTest.setStatus(_A)
_InternalSerialTestResult_Type=Integer32
_InternalSerialTestResult_Object=MibScalar
internalSerialTestResult=_InternalSerialTestResult_Object((1,3,6,1,4,1,28097,2,6),_InternalSerialTestResult_Type())
internalSerialTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSerialTestResult.setStatus(_A)
_InternalAlarmSwitch_Type=Integer32
_InternalAlarmSwitch_Object=MibScalar
internalAlarmSwitch=_InternalAlarmSwitch_Object((1,3,6,1,4,1,28097,2,7),_InternalAlarmSwitch_Type())
internalAlarmSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:internalAlarmSwitch.setStatus(_A)
_InternalDigitalInput_Type=Integer32
_InternalDigitalInput_Object=MibScalar
internalDigitalInput=_InternalDigitalInput_Object((1,3,6,1,4,1,28097,2,8),_InternalDigitalInput_Type())
internalDigitalInput.setMaxAccess(_C)
if mibBuilder.loadTexts:internalDigitalInput.setStatus(_A)
class _AcksysProductID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,19,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,45)));namedValues=NamedValues(*(('wlg-link',1),('wlg-aboard-n',2),('wlg-link-v2',3),('wlg-aboard-n-v2',4),('wlg-switch',5),('wlg-dongle-oem',6),('wlg-dongle',7),('msw-aboard',8),('wlg-xroad-n',9),('wlg-xroad-s',10),('wlg-ida-n',11),('wlg-ida-s',12),('wlg-xroad-np',13),('wlg-ida-np',14),('m340-wc',18),('wlg-aboard-npi-v3',19),('wln-aboard',22),('wln-aboard-n',23),('wln-aboard-24',24),('wln-aboard-48',25),('wln-aboard-72',26),('wln-aboard-110',27),('wln-link-oem-rj',28),('wln-link-oem-ttl',29),('wln-xroad',30),('wln-xroad-v2',31),('wlg-link-v3',32),('wlg-4lan',33),('wln-railbox-1',35),('wln-railbox-1p',36),('wln-railbox-2',37),('wln-railbox-2p',38),('wln-link-oem-ttl-v2',45)))
_AcksysProductID_Type.__name__=_D
_AcksysProductID_Object=MibScalar
acksysProductID=_AcksysProductID_Object((1,3,6,1,4,1,28097,3),_AcksysProductID_Type())
acksysProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:acksysProductID.setStatus(_A)
_C_key_management_ObjectIdentity=ObjectIdentity
c_key_management=_C_key_management_ObjectIdentity((1,3,6,1,4,1,28097,4))
_CkeyManagementCopySettingTo_Type=Integer32
_CkeyManagementCopySettingTo_Object=MibScalar
ckeyManagementCopySettingTo=_CkeyManagementCopySettingTo_Object((1,3,6,1,4,1,28097,4,1),_CkeyManagementCopySettingTo_Type())
ckeyManagementCopySettingTo.setMaxAccess(_B)
if mibBuilder.loadTexts:ckeyManagementCopySettingTo.setStatus(_A)
_CkeyManagementCopySettingFrom_Type=Integer32
_CkeyManagementCopySettingFrom_Object=MibScalar
ckeyManagementCopySettingFrom=_CkeyManagementCopySettingFrom_Object((1,3,6,1,4,1,28097,4,2),_CkeyManagementCopySettingFrom_Type())
ckeyManagementCopySettingFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:ckeyManagementCopySettingFrom.setStatus(_A)
_CkeyManagementErase_Type=Integer32
_CkeyManagementErase_Object=MibScalar
ckeyManagementErase=_CkeyManagementErase_Object((1,3,6,1,4,1,28097,4,3),_CkeyManagementErase_Type())
ckeyManagementErase.setMaxAccess(_B)
if mibBuilder.loadTexts:ckeyManagementErase.setStatus(_A)
class _CkeyManagementStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ckeyStatusNotDetected',1),('ckeyStatusNotValid',2),('ckeyStatusValidAndApplied',3),('ckeyStatusValidAndBackup',4),('ckeyStatusValidAndIgnored',5),('ckeyStatusContainsWlg',6),('ckeyStatusTooSmall',7),('ckeyStatusWrongProduct',8),('ckeyStatusIgnored',9),('ckeyStatusBusy',10)))
_CkeyManagementStatus_Type.__name__=_D
_CkeyManagementStatus_Object=MibScalar
ckeyManagementStatus=_CkeyManagementStatus_Object((1,3,6,1,4,1,28097,4,4),_CkeyManagementStatus_Type())
ckeyManagementStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ckeyManagementStatus.setStatus(_A)
_CkeyManagementIgnoreSetting_Type=DisableEnable
_CkeyManagementIgnoreSetting_Object=MibScalar
ckeyManagementIgnoreSetting=_CkeyManagementIgnoreSetting_Object((1,3,6,1,4,1,28097,4,5),_CkeyManagementIgnoreSetting_Type())
ckeyManagementIgnoreSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:ckeyManagementIgnoreSetting.setStatus(_A)
_CkeyManagementDisableLed_Type=DisableEnable
_CkeyManagementDisableLed_Object=MibScalar
ckeyManagementDisableLed=_CkeyManagementDisableLed_Object((1,3,6,1,4,1,28097,4,6),_CkeyManagementDisableLed_Type())
ckeyManagementDisableLed.setMaxAccess(_B)
if mibBuilder.loadTexts:ckeyManagementDisableLed.setStatus(_A)
_CkeyManagementTest_Type=Integer32
_CkeyManagementTest_Object=MibScalar
ckeyManagementTest=_CkeyManagementTest_Object((1,3,6,1,4,1,28097,4,7),_CkeyManagementTest_Type())
ckeyManagementTest.setMaxAccess(_B)
if mibBuilder.loadTexts:ckeyManagementTest.setStatus(_A)
class _CkeyManagementTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ckeyTestInternalError',1),('ckeyTestNotAvailAble',2),('ckeyTestInProgress',3),('ckeyTestNotOk',4),('ckeyTestOk',5)))
_CkeyManagementTestResult_Type.__name__=_D
_CkeyManagementTestResult_Object=MibScalar
ckeyManagementTestResult=_CkeyManagementTestResult_Object((1,3,6,1,4,1,28097,4,8),_CkeyManagementTestResult_Type())
ckeyManagementTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:ckeyManagementTestResult.setStatus(_A)
_AlarmSettings_ObjectIdentity=ObjectIdentity
alarmSettings=_AlarmSettings_ObjectIdentity((1,3,6,1,4,1,28097,5))
class _AlarmSettingsTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('clear',2)))
_AlarmSettingsTest_Type.__name__=_D
_AlarmSettingsTest_Object=MibScalar
alarmSettingsTest=_AlarmSettingsTest_Object((1,3,6,1,4,1,28097,5,1),_AlarmSettingsTest_Type())
alarmSettingsTest.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsTest.setStatus(_A)
_AlarmSettingsPower1Down_ObjectIdentity=ObjectIdentity
alarmSettingsPower1Down=_AlarmSettingsPower1Down_ObjectIdentity((1,3,6,1,4,1,28097,5,2))
_AlarmSettingsPower1DownEnable_Type=DisableEnable
_AlarmSettingsPower1DownEnable_Object=MibScalar
alarmSettingsPower1DownEnable=_AlarmSettingsPower1DownEnable_Object((1,3,6,1,4,1,28097,5,2,1),_AlarmSettingsPower1DownEnable_Type())
alarmSettingsPower1DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower1DownEnable.setStatus(_A)
_AlarmSettingsPower1DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsPower1DownEnableAutomaticReset_Object=MibScalar
alarmSettingsPower1DownEnableAutomaticReset=_AlarmSettingsPower1DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,2,2),_AlarmSettingsPower1DownEnableAutomaticReset_Type())
alarmSettingsPower1DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower1DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsPower1DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsPower1DownStatus_Type.__name__=_D
_AlarmSettingsPower1DownStatus_Object=MibScalar
alarmSettingsPower1DownStatus=_AlarmSettingsPower1DownStatus_Object((1,3,6,1,4,1,28097,5,2,3),_AlarmSettingsPower1DownStatus_Type())
alarmSettingsPower1DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower1DownStatus.setStatus(_A)
_AlarmSettingsPower2Down_ObjectIdentity=ObjectIdentity
alarmSettingsPower2Down=_AlarmSettingsPower2Down_ObjectIdentity((1,3,6,1,4,1,28097,5,3))
_AlarmSettingsPower2DownEnable_Type=DisableEnable
_AlarmSettingsPower2DownEnable_Object=MibScalar
alarmSettingsPower2DownEnable=_AlarmSettingsPower2DownEnable_Object((1,3,6,1,4,1,28097,5,3,1),_AlarmSettingsPower2DownEnable_Type())
alarmSettingsPower2DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower2DownEnable.setStatus(_A)
_AlarmSettingsPower2DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsPower2DownEnableAutomaticReset_Object=MibScalar
alarmSettingsPower2DownEnableAutomaticReset=_AlarmSettingsPower2DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,3,2),_AlarmSettingsPower2DownEnableAutomaticReset_Type())
alarmSettingsPower2DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower2DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsPower2DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsPower2DownStatus_Type.__name__=_D
_AlarmSettingsPower2DownStatus_Object=MibScalar
alarmSettingsPower2DownStatus=_AlarmSettingsPower2DownStatus_Object((1,3,6,1,4,1,28097,5,3,3),_AlarmSettingsPower2DownStatus_Type())
alarmSettingsPower2DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower2DownStatus.setStatus(_A)
_AlarmSettingsLan1Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan1Down=_AlarmSettingsLan1Down_ObjectIdentity((1,3,6,1,4,1,28097,5,4))
_AlarmSettingsLan1DownEnable_Type=DisableEnable
_AlarmSettingsLan1DownEnable_Object=MibScalar
alarmSettingsLan1DownEnable=_AlarmSettingsLan1DownEnable_Object((1,3,6,1,4,1,28097,5,4,1),_AlarmSettingsLan1DownEnable_Type())
alarmSettingsLan1DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan1DownEnable.setStatus(_A)
_AlarmSettingsLan1DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan1DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan1DownEnableAutomaticReset=_AlarmSettingsLan1DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,4,2),_AlarmSettingsLan1DownEnableAutomaticReset_Type())
alarmSettingsLan1DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan1DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan1DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan1DownStatus_Type.__name__=_D
_AlarmSettingsLan1DownStatus_Object=MibScalar
alarmSettingsLan1DownStatus=_AlarmSettingsLan1DownStatus_Object((1,3,6,1,4,1,28097,5,4,3),_AlarmSettingsLan1DownStatus_Type())
alarmSettingsLan1DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan1DownStatus.setStatus(_A)
_AlarmSettingsLan2Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan2Down=_AlarmSettingsLan2Down_ObjectIdentity((1,3,6,1,4,1,28097,5,5))
_AlarmSettingsLan2DownEnable_Type=DisableEnable
_AlarmSettingsLan2DownEnable_Object=MibScalar
alarmSettingsLan2DownEnable=_AlarmSettingsLan2DownEnable_Object((1,3,6,1,4,1,28097,5,5,1),_AlarmSettingsLan2DownEnable_Type())
alarmSettingsLan2DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan2DownEnable.setStatus(_A)
_AlarmSettingsLan2DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan2DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan2DownEnableAutomaticReset=_AlarmSettingsLan2DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,5,2),_AlarmSettingsLan2DownEnableAutomaticReset_Type())
alarmSettingsLan2DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan2DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan2DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan2DownStatus_Type.__name__=_D
_AlarmSettingsLan2DownStatus_Object=MibScalar
alarmSettingsLan2DownStatus=_AlarmSettingsLan2DownStatus_Object((1,3,6,1,4,1,28097,5,5,3),_AlarmSettingsLan2DownStatus_Type())
alarmSettingsLan2DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan2DownStatus.setStatus(_A)
_AlarmSettingsLan3Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan3Down=_AlarmSettingsLan3Down_ObjectIdentity((1,3,6,1,4,1,28097,5,6))
_AlarmSettingsLan3DownEnable_Type=DisableEnable
_AlarmSettingsLan3DownEnable_Object=MibScalar
alarmSettingsLan3DownEnable=_AlarmSettingsLan3DownEnable_Object((1,3,6,1,4,1,28097,5,6,1),_AlarmSettingsLan3DownEnable_Type())
alarmSettingsLan3DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan3DownEnable.setStatus(_A)
_AlarmSettingsLan3DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan3DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan3DownEnableAutomaticReset=_AlarmSettingsLan3DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,6,2),_AlarmSettingsLan3DownEnableAutomaticReset_Type())
alarmSettingsLan3DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan3DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan3DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan3DownStatus_Type.__name__=_D
_AlarmSettingsLan3DownStatus_Object=MibScalar
alarmSettingsLan3DownStatus=_AlarmSettingsLan3DownStatus_Object((1,3,6,1,4,1,28097,5,6,3),_AlarmSettingsLan3DownStatus_Type())
alarmSettingsLan3DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan3DownStatus.setStatus(_A)
_AlarmSettingsLan4Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan4Down=_AlarmSettingsLan4Down_ObjectIdentity((1,3,6,1,4,1,28097,5,7))
_AlarmSettingsLan4DownEnable_Type=DisableEnable
_AlarmSettingsLan4DownEnable_Object=MibScalar
alarmSettingsLan4DownEnable=_AlarmSettingsLan4DownEnable_Object((1,3,6,1,4,1,28097,5,7,1),_AlarmSettingsLan4DownEnable_Type())
alarmSettingsLan4DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan4DownEnable.setStatus(_A)
_AlarmSettingsLan4DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan4DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan4DownEnableAutomaticReset=_AlarmSettingsLan4DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,7,2),_AlarmSettingsLan4DownEnableAutomaticReset_Type())
alarmSettingsLan4DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan4DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan4DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan4DownStatus_Type.__name__=_D
_AlarmSettingsLan4DownStatus_Object=MibScalar
alarmSettingsLan4DownStatus=_AlarmSettingsLan4DownStatus_Object((1,3,6,1,4,1,28097,5,7,3),_AlarmSettingsLan4DownStatus_Type())
alarmSettingsLan4DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan4DownStatus.setStatus(_A)
_AlarmSettingsLan5Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan5Down=_AlarmSettingsLan5Down_ObjectIdentity((1,3,6,1,4,1,28097,5,8))
_AlarmSettingsLan5DownEnable_Type=DisableEnable
_AlarmSettingsLan5DownEnable_Object=MibScalar
alarmSettingsLan5DownEnable=_AlarmSettingsLan5DownEnable_Object((1,3,6,1,4,1,28097,5,8,1),_AlarmSettingsLan5DownEnable_Type())
alarmSettingsLan5DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan5DownEnable.setStatus(_A)
_AlarmSettingsLan5DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan5DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan5DownEnableAutomaticReset=_AlarmSettingsLan5DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,8,2),_AlarmSettingsLan5DownEnableAutomaticReset_Type())
alarmSettingsLan5DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan5DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan5DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan5DownStatus_Type.__name__=_D
_AlarmSettingsLan5DownStatus_Object=MibScalar
alarmSettingsLan5DownStatus=_AlarmSettingsLan5DownStatus_Object((1,3,6,1,4,1,28097,5,8,3),_AlarmSettingsLan5DownStatus_Type())
alarmSettingsLan5DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan5DownStatus.setStatus(_A)
_AlarmSettingsLan6Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan6Down=_AlarmSettingsLan6Down_ObjectIdentity((1,3,6,1,4,1,28097,5,9))
_AlarmSettingsLan6DownEnable_Type=DisableEnable
_AlarmSettingsLan6DownEnable_Object=MibScalar
alarmSettingsLan6DownEnable=_AlarmSettingsLan6DownEnable_Object((1,3,6,1,4,1,28097,5,9,1),_AlarmSettingsLan6DownEnable_Type())
alarmSettingsLan6DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan6DownEnable.setStatus(_A)
_AlarmSettingsLan6DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan6DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan6DownEnableAutomaticReset=_AlarmSettingsLan6DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,9,2),_AlarmSettingsLan6DownEnableAutomaticReset_Type())
alarmSettingsLan6DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan6DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan6DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan6DownStatus_Type.__name__=_D
_AlarmSettingsLan6DownStatus_Object=MibScalar
alarmSettingsLan6DownStatus=_AlarmSettingsLan6DownStatus_Object((1,3,6,1,4,1,28097,5,9,3),_AlarmSettingsLan6DownStatus_Type())
alarmSettingsLan6DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan6DownStatus.setStatus(_A)
_AlarmSettingsLan7Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan7Down=_AlarmSettingsLan7Down_ObjectIdentity((1,3,6,1,4,1,28097,5,10))
_AlarmSettingsLan7DownEnable_Type=DisableEnable
_AlarmSettingsLan7DownEnable_Object=MibScalar
alarmSettingsLan7DownEnable=_AlarmSettingsLan7DownEnable_Object((1,3,6,1,4,1,28097,5,10,1),_AlarmSettingsLan7DownEnable_Type())
alarmSettingsLan7DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan7DownEnable.setStatus(_A)
_AlarmSettingsLan7DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan7DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan7DownEnableAutomaticReset=_AlarmSettingsLan7DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,10,2),_AlarmSettingsLan7DownEnableAutomaticReset_Type())
alarmSettingsLan7DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan7DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan7DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan7DownStatus_Type.__name__=_D
_AlarmSettingsLan7DownStatus_Object=MibScalar
alarmSettingsLan7DownStatus=_AlarmSettingsLan7DownStatus_Object((1,3,6,1,4,1,28097,5,10,3),_AlarmSettingsLan7DownStatus_Type())
alarmSettingsLan7DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan7DownStatus.setStatus(_A)
_AlarmSettingsLan8Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan8Down=_AlarmSettingsLan8Down_ObjectIdentity((1,3,6,1,4,1,28097,5,11))
_AlarmSettingsLan8DownEnable_Type=DisableEnable
_AlarmSettingsLan8DownEnable_Object=MibScalar
alarmSettingsLan8DownEnable=_AlarmSettingsLan8DownEnable_Object((1,3,6,1,4,1,28097,5,11,1),_AlarmSettingsLan8DownEnable_Type())
alarmSettingsLan8DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan8DownEnable.setStatus(_A)
_AlarmSettingsLan8DownEnableAutomaticReset_Type=DisableEnable
_AlarmSettingsLan8DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan8DownEnableAutomaticReset=_AlarmSettingsLan8DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,11,2),_AlarmSettingsLan8DownEnableAutomaticReset_Type())
alarmSettingsLan8DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan8DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan8DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsLan8DownStatus_Type.__name__=_D
_AlarmSettingsLan8DownStatus_Object=MibScalar
alarmSettingsLan8DownStatus=_AlarmSettingsLan8DownStatus_Object((1,3,6,1,4,1,28097,5,11,3),_AlarmSettingsLan8DownStatus_Type())
alarmSettingsLan8DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan8DownStatus.setStatus(_A)
_AlarmSettingsWLANDown_ObjectIdentity=ObjectIdentity
alarmSettingsWLANDown=_AlarmSettingsWLANDown_ObjectIdentity((1,3,6,1,4,1,28097,5,12))
class _AlarmSettingsWLANDownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_AlarmSettingsWLANDownEnable_Type.__name__=_D
_AlarmSettingsWLANDownEnable_Object=MibScalar
alarmSettingsWLANDownEnable=_AlarmSettingsWLANDownEnable_Object((1,3,6,1,4,1,28097,5,12,1),_AlarmSettingsWLANDownEnable_Type())
alarmSettingsWLANDownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsWLANDownEnable.setStatus(_A)
class _AlarmSettingsWLANDownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_J,2)))
_AlarmSettingsWLANDownEnableAutomaticReset_Type.__name__=_D
_AlarmSettingsWLANDownEnableAutomaticReset_Object=MibScalar
alarmSettingsWLANDownEnableAutomaticReset=_AlarmSettingsWLANDownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,12,2),_AlarmSettingsWLANDownEnableAutomaticReset_Type())
alarmSettingsWLANDownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsWLANDownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsWLANDownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_L,3)))
_AlarmSettingsWLANDownStatus_Type.__name__=_D
_AlarmSettingsWLANDownStatus_Object=MibScalar
alarmSettingsWLANDownStatus=_AlarmSettingsWLANDownStatus_Object((1,3,6,1,4,1,28097,5,12,3),_AlarmSettingsWLANDownStatus_Type())
alarmSettingsWLANDownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsWLANDownStatus.setStatus(_A)
_PowerStatus_ObjectIdentity=ObjectIdentity
powerStatus=_PowerStatus_ObjectIdentity((1,3,6,1,4,1,28097,6))
class _PowerStatus_PW1_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_PowerStatus_PW1_state_Type.__name__=_D
_PowerStatus_PW1_state_Object=MibScalar
powerStatus_PW1_state=_PowerStatus_PW1_state_Object((1,3,6,1,4,1,28097,6,1),_PowerStatus_PW1_state_Type())
powerStatus_PW1_state.setMaxAccess(_C)
if mibBuilder.loadTexts:powerStatus_PW1_state.setStatus(_A)
class _PowerStatus_PW2_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_PowerStatus_PW2_state_Type.__name__=_D
_PowerStatus_PW2_state_Object=MibScalar
powerStatus_PW2_state=_PowerStatus_PW2_state_Object((1,3,6,1,4,1,28097,6,2),_PowerStatus_PW2_state_Type())
powerStatus_PW2_state.setMaxAccess(_C)
if mibBuilder.loadTexts:powerStatus_PW2_state.setStatus(_A)
_NetworkStatus_ObjectIdentity=ObjectIdentity
networkStatus=_NetworkStatus_ObjectIdentity((1,3,6,1,4,1,28097,7))
_StatusIpSubnetTable_Object=MibTable
statusIpSubnetTable=_StatusIpSubnetTable_Object((1,3,6,1,4,1,28097,7,1))
if mibBuilder.loadTexts:statusIpSubnetTable.setStatus(_A)
_StatusIpSubnetEntry_Object=MibTableRow
statusIpSubnetEntry=_StatusIpSubnetEntry_Object((1,3,6,1,4,1,28097,7,1,1))
statusIpSubnetEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:statusIpSubnetEntry.setStatus(_A)
_StatusIpSubnetIndex_Type=Integer32
_StatusIpSubnetIndex_Object=MibTableColumn
statusIpSubnetIndex=_StatusIpSubnetIndex_Object((1,3,6,1,4,1,28097,7,1,1,1),_StatusIpSubnetIndex_Type())
statusIpSubnetIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetIndex.setStatus(_A)
_StatusIpSubnetName_Type=NetifName
_StatusIpSubnetName_Object=MibTableColumn
statusIpSubnetName=_StatusIpSubnetName_Object((1,3,6,1,4,1,28097,7,1,1,2),_StatusIpSubnetName_Type())
statusIpSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetName.setStatus(_A)
_StatusIpSubnetLabel_Type=DisplayString
_StatusIpSubnetLabel_Object=MibTableColumn
statusIpSubnetLabel=_StatusIpSubnetLabel_Object((1,3,6,1,4,1,28097,7,1,1,3),_StatusIpSubnetLabel_Type())
statusIpSubnetLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetLabel.setStatus(_A)
_StatusIpSubnetIfIndex_Type=Integer32
_StatusIpSubnetIfIndex_Object=MibTableColumn
statusIpSubnetIfIndex=_StatusIpSubnetIfIndex_Object((1,3,6,1,4,1,28097,7,1,1,4),_StatusIpSubnetIfIndex_Type())
statusIpSubnetIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetIfIndex.setStatus(_A)
class _StatusIpSubnetAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_d,1),(_e,2),(_N,3),('vrrp',4)))
_StatusIpSubnetAddrMode_Type.__name__=_D
_StatusIpSubnetAddrMode_Object=MibTableColumn
statusIpSubnetAddrMode=_StatusIpSubnetAddrMode_Object((1,3,6,1,4,1,28097,7,1,1,5),_StatusIpSubnetAddrMode_Type())
statusIpSubnetAddrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetAddrMode.setStatus(_A)
_StatusIpSubnetIPv4Addr_Type=IpAddress
_StatusIpSubnetIPv4Addr_Object=MibTableColumn
statusIpSubnetIPv4Addr=_StatusIpSubnetIPv4Addr_Object((1,3,6,1,4,1,28097,7,1,1,6),_StatusIpSubnetIPv4Addr_Type())
statusIpSubnetIPv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetIPv4Addr.setStatus(_A)
_StatusIpSubnetIPv4Mask_Type=IpAddress
_StatusIpSubnetIPv4Mask_Object=MibTableColumn
statusIpSubnetIPv4Mask=_StatusIpSubnetIPv4Mask_Object((1,3,6,1,4,1,28097,7,1,1,7),_StatusIpSubnetIPv4Mask_Type())
statusIpSubnetIPv4Mask.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetIPv4Mask.setStatus(_A)
_StatusIpSubnetDNS_Type=DisplayString
_StatusIpSubnetDNS_Object=MibTableColumn
statusIpSubnetDNS=_StatusIpSubnetDNS_Object((1,3,6,1,4,1,28097,7,1,1,8),_StatusIpSubnetDNS_Type())
statusIpSubnetDNS.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetDNS.setStatus(_A)
_StatusIpSubnetMember_Type=DisplayString
_StatusIpSubnetMember_Object=MibTableColumn
statusIpSubnetMember=_StatusIpSubnetMember_Object((1,3,6,1,4,1,28097,7,1,1,9),_StatusIpSubnetMember_Type())
statusIpSubnetMember.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetMember.setStatus(_A)
_StatusIpSubnetMemberIndex_Type=DisplayString
_StatusIpSubnetMemberIndex_Object=MibTableColumn
statusIpSubnetMemberIndex=_StatusIpSubnetMemberIndex_Object((1,3,6,1,4,1,28097,7,1,1,10),_StatusIpSubnetMemberIndex_Type())
statusIpSubnetMemberIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIpSubnetMemberIndex.setStatus(_A)
_StatusIfWlanTable_Object=MibTable
statusIfWlanTable=_StatusIfWlanTable_Object((1,3,6,1,4,1,28097,7,2))
if mibBuilder.loadTexts:statusIfWlanTable.setStatus(_A)
_StatusIfWlanEntry_Object=MibTableRow
statusIfWlanEntry=_StatusIfWlanEntry_Object((1,3,6,1,4,1,28097,7,2,1))
statusIfWlanEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:statusIfWlanEntry.setStatus(_A)
_StatusIfWlanIndex_Type=Integer32
_StatusIfWlanIndex_Object=MibTableColumn
statusIfWlanIndex=_StatusIfWlanIndex_Object((1,3,6,1,4,1,28097,7,2,1,1),_StatusIfWlanIndex_Type())
statusIfWlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanIndex.setStatus(_A)
class _StatusIfWlanSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StatusIfWlanSSID_Type.__name__=_F
_StatusIfWlanSSID_Object=MibTableColumn
statusIfWlanSSID=_StatusIfWlanSSID_Object((1,3,6,1,4,1,28097,7,2,1,2),_StatusIfWlanSSID_Type())
statusIfWlanSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanSSID.setStatus(_A)
class _StatusIfWlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7,8)));namedValues=NamedValues(*((_A9,0),('infra-client',1),(_z,2),('ad-hoc',3),('monitor',5),('ieee80211s',6),('repeater',7),('isolating-access-point',8)))
_StatusIfWlanMode_Type.__name__=_D
_StatusIfWlanMode_Object=MibTableColumn
statusIfWlanMode=_StatusIfWlanMode_Object((1,3,6,1,4,1,28097,7,2,1,3),_StatusIfWlanMode_Type())
statusIfWlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanMode.setStatus(_A)
_StatusIfWlanBand_Type=WifiFlavor
_StatusIfWlanBand_Object=MibTableColumn
statusIfWlanBand=_StatusIfWlanBand_Object((1,3,6,1,4,1,28097,7,2,1,4),_StatusIfWlanBand_Type())
statusIfWlanBand.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanBand.setStatus(_A)
_StatusIfWlanChannel_Type=Integer32
_StatusIfWlanChannel_Object=MibTableColumn
statusIfWlanChannel=_StatusIfWlanChannel_Object((1,3,6,1,4,1,28097,7,2,1,5),_StatusIfWlanChannel_Type())
statusIfWlanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanChannel.setStatus(_A)
_StatusIfWlanFrequency_Type=Integer32
_StatusIfWlanFrequency_Object=MibTableColumn
statusIfWlanFrequency=_StatusIfWlanFrequency_Object((1,3,6,1,4,1,28097,7,2,1,6),_StatusIfWlanFrequency_Type())
statusIfWlanFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanFrequency.setStatus(_A)
_StatusIfWlanEnable_Type=DisableEnable
_StatusIfWlanEnable_Object=MibTableColumn
statusIfWlanEnable=_StatusIfWlanEnable_Object((1,3,6,1,4,1,28097,7,2,1,7),_StatusIfWlanEnable_Type())
statusIfWlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanEnable.setStatus(_A)
_StatusIfWlanPhy_Type=Integer32
_StatusIfWlanPhy_Object=MibTableColumn
statusIfWlanPhy=_StatusIfWlanPhy_Object((1,3,6,1,4,1,28097,7,2,1,8),_StatusIfWlanPhy_Type())
statusIfWlanPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanPhy.setStatus(_A)
_StatusIfWlanSecurityMode_Type=SecurityModes
_StatusIfWlanSecurityMode_Object=MibTableColumn
statusIfWlanSecurityMode=_StatusIfWlanSecurityMode_Object((1,3,6,1,4,1,28097,7,2,1,9),_StatusIfWlanSecurityMode_Type())
statusIfWlanSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanSecurityMode.setStatus(_A)
_StatusIfWlanWpaVersion_Type=Integer32
_StatusIfWlanWpaVersion_Object=MibTableColumn
statusIfWlanWpaVersion=_StatusIfWlanWpaVersion_Object((1,3,6,1,4,1,28097,7,2,1,10),_StatusIfWlanWpaVersion_Type())
statusIfWlanWpaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanWpaVersion.setStatus(_A)
_StatusIfWlanNPeers_Type=Integer32
_StatusIfWlanNPeers_Object=MibTableColumn
statusIfWlanNPeers=_StatusIfWlanNPeers_Object((1,3,6,1,4,1,28097,7,2,1,11),_StatusIfWlanNPeers_Type())
statusIfWlanNPeers.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanNPeers.setStatus(_A)
_StatusIfWlanQuality_Type=Integer32
_StatusIfWlanQuality_Object=MibTableColumn
statusIfWlanQuality=_StatusIfWlanQuality_Object((1,3,6,1,4,1,28097,7,2,1,12),_StatusIfWlanQuality_Type())
statusIfWlanQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanQuality.setStatus(_A)
_StatusIfWlanBssid_Type=PhysAddress
_StatusIfWlanBssid_Object=MibTableColumn
statusIfWlanBssid=_StatusIfWlanBssid_Object((1,3,6,1,4,1,28097,7,2,1,13),_StatusIfWlanBssid_Type())
statusIfWlanBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanBssid.setStatus(_A)
class _StatusIfWlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,9)));namedValues=NamedValues(*((_q,0),(_r,9)))
_StatusIfWlanState_Type.__name__=_D
_StatusIfWlanState_Object=MibTableColumn
statusIfWlanState=_StatusIfWlanState_Object((1,3,6,1,4,1,28097,7,2,1,14),_StatusIfWlanState_Type())
statusIfWlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanState.setStatus(_A)
_StatusIfStaFastBSSTransitionActivated_Type=DisableEnable
_StatusIfStaFastBSSTransitionActivated_Object=MibTableColumn
statusIfStaFastBSSTransitionActivated=_StatusIfStaFastBSSTransitionActivated_Object((1,3,6,1,4,1,28097,7,2,1,15),_StatusIfStaFastBSSTransitionActivated_Type())
statusIfStaFastBSSTransitionActivated.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfStaFastBSSTransitionActivated.setStatus(_A)
_StatusIfWlanBeaconSignalAvg_Type=Integer32
_StatusIfWlanBeaconSignalAvg_Object=MibTableColumn
statusIfWlanBeaconSignalAvg=_StatusIfWlanBeaconSignalAvg_Object((1,3,6,1,4,1,28097,7,2,1,16),_StatusIfWlanBeaconSignalAvg_Type())
statusIfWlanBeaconSignalAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanBeaconSignalAvg.setStatus(_A)
_StatusIfWlanNoise_Type=Integer32
_StatusIfWlanNoise_Object=MibTableColumn
statusIfWlanNoise=_StatusIfWlanNoise_Object((1,3,6,1,4,1,28097,7,2,1,17),_StatusIfWlanNoise_Type())
statusIfWlanNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanNoise.setStatus(_A)
_StatusIfWlanWpaCipher_Type=CipherTypes
_StatusIfWlanWpaCipher_Object=MibTableColumn
statusIfWlanWpaCipher=_StatusIfWlanWpaCipher_Object((1,3,6,1,4,1,28097,7,2,1,18),_StatusIfWlanWpaCipher_Type())
statusIfWlanWpaCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanWpaCipher.setStatus(_A)
_StatusIfWlanWpaPreSharedKey_Type=OctetString
_StatusIfWlanWpaPreSharedKey_Object=MibTableColumn
statusIfWlanWpaPreSharedKey=_StatusIfWlanWpaPreSharedKey_Object((1,3,6,1,4,1,28097,7,2,1,19),_StatusIfWlanWpaPreSharedKey_Type())
statusIfWlanWpaPreSharedKey.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanWpaPreSharedKey.setStatus(_A)
_StatusIfWlanName_Type=DisplayString
_StatusIfWlanName_Object=MibTableColumn
statusIfWlanName=_StatusIfWlanName_Object((1,3,6,1,4,1,28097,7,2,1,20),_StatusIfWlanName_Type())
statusIfWlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanName.setStatus(_A)
_StatusIfWlanIfIndex_Type=Integer32
_StatusIfWlanIfIndex_Object=MibTableColumn
statusIfWlanIfIndex=_StatusIfWlanIfIndex_Object((1,3,6,1,4,1,28097,7,2,1,21),_StatusIfWlanIfIndex_Type())
statusIfWlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusIfWlanIfIndex.setStatus(_A)
_StatusPhyWifiTable_Object=MibTable
statusPhyWifiTable=_StatusPhyWifiTable_Object((1,3,6,1,4,1,28097,7,3))
if mibBuilder.loadTexts:statusPhyWifiTable.setStatus(_A)
_StatusPhyWifiEntry_Object=MibTableRow
statusPhyWifiEntry=_StatusPhyWifiEntry_Object((1,3,6,1,4,1,28097,7,3,1))
statusPhyWifiEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:statusPhyWifiEntry.setStatus(_A)
_StatusPhyWifiIndex_Type=Integer32
_StatusPhyWifiIndex_Object=MibTableColumn
statusPhyWifiIndex=_StatusPhyWifiIndex_Object((1,3,6,1,4,1,28097,7,3,1,1),_StatusPhyWifiIndex_Type())
statusPhyWifiIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiIndex.setStatus(_A)
_StatusPhyWifiLabel_Type=DisplayString
_StatusPhyWifiLabel_Object=MibTableColumn
statusPhyWifiLabel=_StatusPhyWifiLabel_Object((1,3,6,1,4,1,28097,7,3,1,2),_StatusPhyWifiLabel_Type())
statusPhyWifiLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiLabel.setStatus(_A)
_StatusPhyWifiEnable_Type=DisableEnable
_StatusPhyWifiEnable_Object=MibTableColumn
statusPhyWifiEnable=_StatusPhyWifiEnable_Object((1,3,6,1,4,1,28097,7,3,1,3),_StatusPhyWifiEnable_Type())
statusPhyWifiEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiEnable.setStatus(_A)
_StatusPhyWifiName_Type=NetifName
_StatusPhyWifiName_Object=MibTableColumn
statusPhyWifiName=_StatusPhyWifiName_Object((1,3,6,1,4,1,28097,7,3,1,4),_StatusPhyWifiName_Type())
statusPhyWifiName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiName.setStatus(_A)
class _StatusPhyWifiClusterMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_StatusPhyWifiClusterMode_Type.__name__=_F
_StatusPhyWifiClusterMode_Object=MibTableColumn
statusPhyWifiClusterMode=_StatusPhyWifiClusterMode_Object((1,3,6,1,4,1,28097,7,3,1,5),_StatusPhyWifiClusterMode_Type())
statusPhyWifiClusterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiClusterMode.setStatus(_A)
class _StatusPhyWifiClusterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_StatusPhyWifiClusterList_Type.__name__=_F
_StatusPhyWifiClusterList_Object=MibTableColumn
statusPhyWifiClusterList=_StatusPhyWifiClusterList_Object((1,3,6,1,4,1,28097,7,3,1,6),_StatusPhyWifiClusterList_Type())
statusPhyWifiClusterList.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiClusterList.setStatus(_A)
class _StatusPhyWifiClusterArgs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_StatusPhyWifiClusterArgs_Type.__name__=_F
_StatusPhyWifiClusterArgs_Object=MibTableColumn
statusPhyWifiClusterArgs=_StatusPhyWifiClusterArgs_Object((1,3,6,1,4,1,28097,7,3,1,7),_StatusPhyWifiClusterArgs_Type())
statusPhyWifiClusterArgs.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiClusterArgs.setStatus(_A)
_StatusPhyWifiMAC_Type=PhysAddress
_StatusPhyWifiMAC_Object=MibTableColumn
statusPhyWifiMAC=_StatusPhyWifiMAC_Object((1,3,6,1,4,1,28097,7,3,1,8),_StatusPhyWifiMAC_Type())
statusPhyWifiMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiMAC.setStatus(_A)
_StatusPhyWifiWids_Type=Integer32
_StatusPhyWifiWids_Object=MibTableColumn
statusPhyWifiWids=_StatusPhyWifiWids_Object((1,3,6,1,4,1,28097,7,3,1,9),_StatusPhyWifiWids_Type())
statusPhyWifiWids.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiWids.setStatus(_A)
_StatusPhyWifiScanTable_Object=MibTable
statusPhyWifiScanTable=_StatusPhyWifiScanTable_Object((1,3,6,1,4,1,28097,7,4))
if mibBuilder.loadTexts:statusPhyWifiScanTable.setStatus(_A)
_StatusPhyWifiScanEntry_Object=MibTableRow
statusPhyWifiScanEntry=_StatusPhyWifiScanEntry_Object((1,3,6,1,4,1,28097,7,4,1))
statusPhyWifiScanEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:statusPhyWifiScanEntry.setStatus(_A)
_StatusPhyWifiScanTableIndex_Type=Integer32
_StatusPhyWifiScanTableIndex_Object=MibTableColumn
statusPhyWifiScanTableIndex=_StatusPhyWifiScanTableIndex_Object((1,3,6,1,4,1,28097,7,4,1,1),_StatusPhyWifiScanTableIndex_Type())
statusPhyWifiScanTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanTableIndex.setStatus(_A)
class _StatusPhyWifiScanSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StatusPhyWifiScanSSID_Type.__name__=_F
_StatusPhyWifiScanSSID_Object=MibTableColumn
statusPhyWifiScanSSID=_StatusPhyWifiScanSSID_Object((1,3,6,1,4,1,28097,7,4,1,2),_StatusPhyWifiScanSSID_Type())
statusPhyWifiScanSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanSSID.setStatus(_A)
_StatusPhyWifiScanSignal_Type=Integer32
_StatusPhyWifiScanSignal_Object=MibTableColumn
statusPhyWifiScanSignal=_StatusPhyWifiScanSignal_Object((1,3,6,1,4,1,28097,7,4,1,3),_StatusPhyWifiScanSignal_Type())
statusPhyWifiScanSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanSignal.setStatus(_A)
_StatusPhyWifiScanFreq_Type=Integer32
_StatusPhyWifiScanFreq_Object=MibTableColumn
statusPhyWifiScanFreq=_StatusPhyWifiScanFreq_Object((1,3,6,1,4,1,28097,7,4,1,4),_StatusPhyWifiScanFreq_Type())
statusPhyWifiScanFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanFreq.setStatus(_A)
class _StatusPhyWifiScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),(_A0,2),('adhoc',3),('mesh',4)))
_StatusPhyWifiScanMode_Type.__name__=_D
_StatusPhyWifiScanMode_Object=MibTableColumn
statusPhyWifiScanMode=_StatusPhyWifiScanMode_Object((1,3,6,1,4,1,28097,7,4,1,5),_StatusPhyWifiScanMode_Type())
statusPhyWifiScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanMode.setStatus(_A)
_StatusPhyWifiScanSecurity_Type=SecurityModes
_StatusPhyWifiScanSecurity_Object=MibTableColumn
statusPhyWifiScanSecurity=_StatusPhyWifiScanSecurity_Object((1,3,6,1,4,1,28097,7,4,1,6),_StatusPhyWifiScanSecurity_Type())
statusPhyWifiScanSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanSecurity.setStatus(_A)
_StatusPhyWifiScanBssid_Type=PhysAddress
_StatusPhyWifiScanBssid_Object=MibTableColumn
statusPhyWifiScanBssid=_StatusPhyWifiScanBssid_Object((1,3,6,1,4,1,28097,7,4,1,7),_StatusPhyWifiScanBssid_Type())
statusPhyWifiScanBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanBssid.setStatus(_A)
_StatusPhyWifiScanPhyNum_Type=Integer32
_StatusPhyWifiScanPhyNum_Object=MibTableColumn
statusPhyWifiScanPhyNum=_StatusPhyWifiScanPhyNum_Object((1,3,6,1,4,1,28097,7,4,1,8),_StatusPhyWifiScanPhyNum_Type())
statusPhyWifiScanPhyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanPhyNum.setStatus(_A)
_StatusPhyWifiScanChWidth_Type=Integer32
_StatusPhyWifiScanChWidth_Object=MibTableColumn
statusPhyWifiScanChWidth=_StatusPhyWifiScanChWidth_Object((1,3,6,1,4,1,28097,7,4,1,9),_StatusPhyWifiScanChWidth_Type())
statusPhyWifiScanChWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyWifiScanChWidth.setStatus(_A)
_StatusPhyWifiScanTableStart_Type=Integer32
_StatusPhyWifiScanTableStart_Object=MibScalar
statusPhyWifiScanTableStart=_StatusPhyWifiScanTableStart_Object((1,3,6,1,4,1,28097,7,5),_StatusPhyWifiScanTableStart_Type())
statusPhyWifiScanTableStart.setMaxAccess(_B)
if mibBuilder.loadTexts:statusPhyWifiScanTableStart.setStatus(_A)
class _StatusPhyWifiScanUpdateTbl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StatusPhyWifiScanUpdateTbl_Type.__name__=_F
_StatusPhyWifiScanUpdateTbl_Object=MibScalar
statusPhyWifiScanUpdateTbl=_StatusPhyWifiScanUpdateTbl_Object((1,3,6,1,4,1,28097,7,6),_StatusPhyWifiScanUpdateTbl_Type())
statusPhyWifiScanUpdateTbl.setMaxAccess(_B)
if mibBuilder.loadTexts:statusPhyWifiScanUpdateTbl.setStatus(_A)
_StatusSpanningTreeTable_Object=MibTable
statusSpanningTreeTable=_StatusSpanningTreeTable_Object((1,3,6,1,4,1,28097,7,7))
if mibBuilder.loadTexts:statusSpanningTreeTable.setStatus(_A)
_StatusSpanningTreeEntry_Object=MibTableRow
statusSpanningTreeEntry=_StatusSpanningTreeEntry_Object((1,3,6,1,4,1,28097,7,7,1))
statusSpanningTreeEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:statusSpanningTreeEntry.setStatus(_A)
_StatusSpanningTreeBridgeName_Type=NetifName
_StatusSpanningTreeBridgeName_Object=MibTableColumn
statusSpanningTreeBridgeName=_StatusSpanningTreeBridgeName_Object((1,3,6,1,4,1,28097,7,7,1,1),_StatusSpanningTreeBridgeName_Type())
statusSpanningTreeBridgeName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreeBridgeName.setStatus(_A)
_StatusSpanningTreeNetworkLabel_Type=DisplayString
_StatusSpanningTreeNetworkLabel_Object=MibTableColumn
statusSpanningTreeNetworkLabel=_StatusSpanningTreeNetworkLabel_Object((1,3,6,1,4,1,28097,7,7,1,2),_StatusSpanningTreeNetworkLabel_Type())
statusSpanningTreeNetworkLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreeNetworkLabel.setStatus(_A)
_StatusSpanningTreeBridgeId_Type=BridgeId
_StatusSpanningTreeBridgeId_Object=MibTableColumn
statusSpanningTreeBridgeId=_StatusSpanningTreeBridgeId_Object((1,3,6,1,4,1,28097,7,7,1,3),_StatusSpanningTreeBridgeId_Type())
statusSpanningTreeBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreeBridgeId.setStatus(_A)
_StatusSpanningTreeDesignatedRoot_Type=BridgeId
_StatusSpanningTreeDesignatedRoot_Object=MibTableColumn
statusSpanningTreeDesignatedRoot=_StatusSpanningTreeDesignatedRoot_Object((1,3,6,1,4,1,28097,7,7,1,4),_StatusSpanningTreeDesignatedRoot_Type())
statusSpanningTreeDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreeDesignatedRoot.setStatus(_A)
_StatusSpanningTreeRootPort_Type=NetifName
_StatusSpanningTreeRootPort_Object=MibTableColumn
statusSpanningTreeRootPort=_StatusSpanningTreeRootPort_Object((1,3,6,1,4,1,28097,7,7,1,5),_StatusSpanningTreeRootPort_Type())
statusSpanningTreeRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreeRootPort.setStatus(_A)
_StatusSpanningTreePortTable_Object=MibTable
statusSpanningTreePortTable=_StatusSpanningTreePortTable_Object((1,3,6,1,4,1,28097,7,8))
if mibBuilder.loadTexts:statusSpanningTreePortTable.setStatus(_A)
_StatusSpanningTreePortEntry_Object=MibTableRow
statusSpanningTreePortEntry=_StatusSpanningTreePortEntry_Object((1,3,6,1,4,1,28097,7,8,1))
statusSpanningTreePortEntry.setIndexNames((0,_E,_AD),(0,_E,_AE))
if mibBuilder.loadTexts:statusSpanningTreePortEntry.setStatus(_A)
_StatusSpanningTreePortBridgeName_Type=NetifName
_StatusSpanningTreePortBridgeName_Object=MibTableColumn
statusSpanningTreePortBridgeName=_StatusSpanningTreePortBridgeName_Object((1,3,6,1,4,1,28097,7,8,1,1),_StatusSpanningTreePortBridgeName_Type())
statusSpanningTreePortBridgeName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortBridgeName.setStatus(_A)
_StatusSpanningTreePortNetworkLabel_Type=DisplayString
_StatusSpanningTreePortNetworkLabel_Object=MibTableColumn
statusSpanningTreePortNetworkLabel=_StatusSpanningTreePortNetworkLabel_Object((1,3,6,1,4,1,28097,7,8,1,2),_StatusSpanningTreePortNetworkLabel_Type())
statusSpanningTreePortNetworkLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortNetworkLabel.setStatus(_A)
_StatusSpanningTreePortName_Type=NetifName
_StatusSpanningTreePortName_Object=MibTableColumn
statusSpanningTreePortName=_StatusSpanningTreePortName_Object((1,3,6,1,4,1,28097,7,8,1,3),_StatusSpanningTreePortName_Type())
statusSpanningTreePortName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortName.setStatus(_A)
_StatusSpanningTreePortLabel_Type=DisplayString
_StatusSpanningTreePortLabel_Object=MibTableColumn
statusSpanningTreePortLabel=_StatusSpanningTreePortLabel_Object((1,3,6,1,4,1,28097,7,8,1,4),_StatusSpanningTreePortLabel_Type())
statusSpanningTreePortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortLabel.setStatus(_A)
_StatusSpanningTreePortId_Type=PortId
_StatusSpanningTreePortId_Object=MibTableColumn
statusSpanningTreePortId=_StatusSpanningTreePortId_Object((1,3,6,1,4,1,28097,7,8,1,5),_StatusSpanningTreePortId_Type())
statusSpanningTreePortId.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortId.setStatus(_A)
class _StatusSpanningTreePortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_s,0),('root',1),('designated',2),('alternate',3),('backup',4),('master',5)))
_StatusSpanningTreePortRole_Type.__name__=_D
_StatusSpanningTreePortRole_Object=MibTableColumn
statusSpanningTreePortRole=_StatusSpanningTreePortRole_Object((1,3,6,1,4,1,28097,7,8,1,6),_StatusSpanningTreePortRole_Type())
statusSpanningTreePortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortRole.setStatus(_A)
class _StatusSpanningTreePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discarding',0),('learning',1),('forwarding',2)))
_StatusSpanningTreePortState_Type.__name__=_D
_StatusSpanningTreePortState_Object=MibTableColumn
statusSpanningTreePortState=_StatusSpanningTreePortState_Object((1,3,6,1,4,1,28097,7,8,1,7),_StatusSpanningTreePortState_Type())
statusSpanningTreePortState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortState.setStatus(_A)
class _StatusSpanningTreePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_StatusSpanningTreePortPathCost_Type.__name__=_D
_StatusSpanningTreePortPathCost_Object=MibTableColumn
statusSpanningTreePortPathCost=_StatusSpanningTreePortPathCost_Object((1,3,6,1,4,1,28097,7,8,1,8),_StatusSpanningTreePortPathCost_Type())
statusSpanningTreePortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortPathCost.setStatus(_A)
_StatusSpanningTreePortDesignatedRoot_Type=BridgeId
_StatusSpanningTreePortDesignatedRoot_Object=MibTableColumn
statusSpanningTreePortDesignatedRoot=_StatusSpanningTreePortDesignatedRoot_Object((1,3,6,1,4,1,28097,7,8,1,9),_StatusSpanningTreePortDesignatedRoot_Type())
statusSpanningTreePortDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortDesignatedRoot.setStatus(_A)
_StatusSpanningTreePortDesignatedCost_Type=Integer32
_StatusSpanningTreePortDesignatedCost_Object=MibTableColumn
statusSpanningTreePortDesignatedCost=_StatusSpanningTreePortDesignatedCost_Object((1,3,6,1,4,1,28097,7,8,1,10),_StatusSpanningTreePortDesignatedCost_Type())
statusSpanningTreePortDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortDesignatedCost.setStatus(_A)
_StatusSpanningTreePortDesignatedBridge_Type=BridgeId
_StatusSpanningTreePortDesignatedBridge_Object=MibTableColumn
statusSpanningTreePortDesignatedBridge=_StatusSpanningTreePortDesignatedBridge_Object((1,3,6,1,4,1,28097,7,8,1,11),_StatusSpanningTreePortDesignatedBridge_Type())
statusSpanningTreePortDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortDesignatedBridge.setStatus(_A)
_StatusSpanningTreePortDesignatedPort_Type=PortId
_StatusSpanningTreePortDesignatedPort_Object=MibTableColumn
statusSpanningTreePortDesignatedPort=_StatusSpanningTreePortDesignatedPort_Object((1,3,6,1,4,1,28097,7,8,1,12),_StatusSpanningTreePortDesignatedPort_Type())
statusSpanningTreePortDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortDesignatedPort.setStatus(_A)
_StatusSpanningTreePortOperEdgePort_Type=TruthValue
_StatusSpanningTreePortOperEdgePort_Object=MibTableColumn
statusSpanningTreePortOperEdgePort=_StatusSpanningTreePortOperEdgePort_Object((1,3,6,1,4,1,28097,7,8,1,13),_StatusSpanningTreePortOperEdgePort_Type())
statusSpanningTreePortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortOperEdgePort.setStatus(_A)
_StatusSpanningTreePortOperPointToPoint_Type=TruthValue
_StatusSpanningTreePortOperPointToPoint_Object=MibTableColumn
statusSpanningTreePortOperPointToPoint=_StatusSpanningTreePortOperPointToPoint_Object((1,3,6,1,4,1,28097,7,8,1,14),_StatusSpanningTreePortOperPointToPoint_Type())
statusSpanningTreePortOperPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpanningTreePortOperPointToPoint.setStatus(_A)
_StatusAssociationTable_Object=MibTable
statusAssociationTable=_StatusAssociationTable_Object((1,3,6,1,4,1,28097,7,9))
if mibBuilder.loadTexts:statusAssociationTable.setStatus(_A)
_StatusAssociationEntry_Object=MibTableRow
statusAssociationEntry=_StatusAssociationEntry_Object((1,3,6,1,4,1,28097,7,9,1))
statusAssociationEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:statusAssociationEntry.setStatus(_A)
_StatusAssociationIndex_Type=Integer32
_StatusAssociationIndex_Object=MibTableColumn
statusAssociationIndex=_StatusAssociationIndex_Object((1,3,6,1,4,1,28097,7,9,1,1),_StatusAssociationIndex_Type())
statusAssociationIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationIndex.setStatus(_A)
_StatusAssociationMacAddr_Type=PhysAddress
_StatusAssociationMacAddr_Object=MibTableColumn
statusAssociationMacAddr=_StatusAssociationMacAddr_Object((1,3,6,1,4,1,28097,7,9,1,2),_StatusAssociationMacAddr_Type())
statusAssociationMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationMacAddr.setStatus(_A)
_StatusAssociationSSID_Type=DisplayString
_StatusAssociationSSID_Object=MibTableColumn
statusAssociationSSID=_StatusAssociationSSID_Object((1,3,6,1,4,1,28097,7,9,1,3),_StatusAssociationSSID_Type())
statusAssociationSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationSSID.setStatus(_A)
_StatusAssociationBSSID_Type=PhysAddress
_StatusAssociationBSSID_Object=MibTableColumn
statusAssociationBSSID=_StatusAssociationBSSID_Object((1,3,6,1,4,1,28097,7,9,1,4),_StatusAssociationBSSID_Type())
statusAssociationBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationBSSID.setStatus(_A)
_StatusAssociationPhy_Type=DisplayString
_StatusAssociationPhy_Object=MibTableColumn
statusAssociationPhy=_StatusAssociationPhy_Object((1,3,6,1,4,1,28097,7,9,1,5),_StatusAssociationPhy_Type())
statusAssociationPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationPhy.setStatus(_A)
_StatusAssociationSignaldBm_Type=Integer32
_StatusAssociationSignaldBm_Object=MibTableColumn
statusAssociationSignaldBm=_StatusAssociationSignaldBm_Object((1,3,6,1,4,1,28097,7,9,1,6),_StatusAssociationSignaldBm_Type())
statusAssociationSignaldBm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationSignaldBm.setStatus(_A)
_StatusAssociationNoisedBm_Type=Integer32
_StatusAssociationNoisedBm_Object=MibTableColumn
statusAssociationNoisedBm=_StatusAssociationNoisedBm_Object((1,3,6,1,4,1,28097,7,9,1,7),_StatusAssociationNoisedBm_Type())
statusAssociationNoisedBm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationNoisedBm.setStatus(_A)
_StatusAssociationSNR_Type=Integer32
_StatusAssociationSNR_Object=MibTableColumn
statusAssociationSNR=_StatusAssociationSNR_Object((1,3,6,1,4,1,28097,7,9,1,8),_StatusAssociationSNR_Type())
statusAssociationSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationSNR.setStatus(_A)
_StatusAssociationWlanIndex_Type=Integer32
_StatusAssociationWlanIndex_Object=MibTableColumn
statusAssociationWlanIndex=_StatusAssociationWlanIndex_Object((1,3,6,1,4,1,28097,7,9,1,9),_StatusAssociationWlanIndex_Type())
statusAssociationWlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationWlanIndex.setStatus(_A)
_StatusAssociationSecurityMode_Type=SecurityModes
_StatusAssociationSecurityMode_Object=MibTableColumn
statusAssociationSecurityMode=_StatusAssociationSecurityMode_Object((1,3,6,1,4,1,28097,7,9,1,10),_StatusAssociationSecurityMode_Type())
statusAssociationSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusAssociationSecurityMode.setStatus(_A)
_StatusPhyLanTable_Object=MibTable
statusPhyLanTable=_StatusPhyLanTable_Object((1,3,6,1,4,1,28097,7,10))
if mibBuilder.loadTexts:statusPhyLanTable.setStatus(_A)
_StatusPhyLanEntry_Object=MibTableRow
statusPhyLanEntry=_StatusPhyLanEntry_Object((1,3,6,1,4,1,28097,7,10,1))
statusPhyLanEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:statusPhyLanEntry.setStatus(_A)
_StatusPhyLanIndex_Type=Integer32
_StatusPhyLanIndex_Object=MibTableColumn
statusPhyLanIndex=_StatusPhyLanIndex_Object((1,3,6,1,4,1,28097,7,10,1,1),_StatusPhyLanIndex_Type())
statusPhyLanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyLanIndex.setStatus(_A)
_StatusPhyLanName_Type=DisplayString
_StatusPhyLanName_Object=MibTableColumn
statusPhyLanName=_StatusPhyLanName_Object((1,3,6,1,4,1,28097,7,10,1,2),_StatusPhyLanName_Type())
statusPhyLanName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyLanName.setStatus(_A)
_StatusPhyLanLabel_Type=DisplayString
_StatusPhyLanLabel_Object=MibTableColumn
statusPhyLanLabel=_StatusPhyLanLabel_Object((1,3,6,1,4,1,28097,7,10,1,3),_StatusPhyLanLabel_Type())
statusPhyLanLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyLanLabel.setStatus(_A)
_StatusPhyLanIfIndex_Type=Integer32
_StatusPhyLanIfIndex_Object=MibTableColumn
statusPhyLanIfIndex=_StatusPhyLanIfIndex_Object((1,3,6,1,4,1,28097,7,10,1,4),_StatusPhyLanIfIndex_Type())
statusPhyLanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyLanIfIndex.setStatus(_A)
_StatusMeshSurveyTable_Object=MibTable
statusMeshSurveyTable=_StatusMeshSurveyTable_Object((1,3,6,1,4,1,28097,7,11))
if mibBuilder.loadTexts:statusMeshSurveyTable.setStatus(_A)
_StatusMeshSurveyEntry_Object=MibTableRow
statusMeshSurveyEntry=_StatusMeshSurveyEntry_Object((1,3,6,1,4,1,28097,7,11,1))
statusMeshSurveyEntry.setIndexNames((0,_E,_AH))
if mibBuilder.loadTexts:statusMeshSurveyEntry.setStatus(_A)
_StatusMeshSurveyIndex_Type=Integer32
_StatusMeshSurveyIndex_Object=MibTableColumn
statusMeshSurveyIndex=_StatusMeshSurveyIndex_Object((1,3,6,1,4,1,28097,7,11,1,1),_StatusMeshSurveyIndex_Type())
statusMeshSurveyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyIndex.setStatus(_A)
_StatusMeshSurveyDstMacAddr_Type=PhysAddress
_StatusMeshSurveyDstMacAddr_Object=MibTableColumn
statusMeshSurveyDstMacAddr=_StatusMeshSurveyDstMacAddr_Object((1,3,6,1,4,1,28097,7,11,1,2),_StatusMeshSurveyDstMacAddr_Type())
statusMeshSurveyDstMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyDstMacAddr.setStatus(_A)
_StatusMeshSurveyNextHopMacAddr_Type=PhysAddress
_StatusMeshSurveyNextHopMacAddr_Object=MibTableColumn
statusMeshSurveyNextHopMacAddr=_StatusMeshSurveyNextHopMacAddr_Object((1,3,6,1,4,1,28097,7,11,1,3),_StatusMeshSurveyNextHopMacAddr_Type())
statusMeshSurveyNextHopMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyNextHopMacAddr.setStatus(_A)
_StatusMeshSurveyPhy_Type=DisplayString
_StatusMeshSurveyPhy_Object=MibTableColumn
statusMeshSurveyPhy=_StatusMeshSurveyPhy_Object((1,3,6,1,4,1,28097,7,11,1,4),_StatusMeshSurveyPhy_Type())
statusMeshSurveyPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyPhy.setStatus(_A)
_StatusMeshSurveyMetric_Type=Integer32
_StatusMeshSurveyMetric_Object=MibTableColumn
statusMeshSurveyMetric=_StatusMeshSurveyMetric_Object((1,3,6,1,4,1,28097,7,11,1,5),_StatusMeshSurveyMetric_Type())
statusMeshSurveyMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyMetric.setStatus(_A)
_StatusMeshSurveyDiscoveryTimeout_Type=Integer32
_StatusMeshSurveyDiscoveryTimeout_Object=MibTableColumn
statusMeshSurveyDiscoveryTimeout=_StatusMeshSurveyDiscoveryTimeout_Object((1,3,6,1,4,1,28097,7,11,1,6),_StatusMeshSurveyDiscoveryTimeout_Type())
statusMeshSurveyDiscoveryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyDiscoveryTimeout.setStatus(_A)
_StatusMeshSurveyDiscoveryRetries_Type=Integer32
_StatusMeshSurveyDiscoveryRetries_Object=MibTableColumn
statusMeshSurveyDiscoveryRetries=_StatusMeshSurveyDiscoveryRetries_Object((1,3,6,1,4,1,28097,7,11,1,7),_StatusMeshSurveyDiscoveryRetries_Type())
statusMeshSurveyDiscoveryRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyDiscoveryRetries.setStatus(_A)
_StatusMeshSurveyStateActive_Type=TruthValue
_StatusMeshSurveyStateActive_Object=MibTableColumn
statusMeshSurveyStateActive=_StatusMeshSurveyStateActive_Object((1,3,6,1,4,1,28097,7,11,1,8),_StatusMeshSurveyStateActive_Type())
statusMeshSurveyStateActive.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyStateActive.setStatus(_A)
_StatusMeshSurveyStateResolving_Type=TruthValue
_StatusMeshSurveyStateResolving_Object=MibTableColumn
statusMeshSurveyStateResolving=_StatusMeshSurveyStateResolving_Object((1,3,6,1,4,1,28097,7,11,1,9),_StatusMeshSurveyStateResolving_Type())
statusMeshSurveyStateResolving.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyStateResolving.setStatus(_A)
_StatusMeshSurveyStateDSNValid_Type=TruthValue
_StatusMeshSurveyStateDSNValid_Object=MibTableColumn
statusMeshSurveyStateDSNValid=_StatusMeshSurveyStateDSNValid_Object((1,3,6,1,4,1,28097,7,11,1,10),_StatusMeshSurveyStateDSNValid_Type())
statusMeshSurveyStateDSNValid.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyStateDSNValid.setStatus(_A)
_StatusMeshSurveyStateFixed_Type=TruthValue
_StatusMeshSurveyStateFixed_Object=MibTableColumn
statusMeshSurveyStateFixed=_StatusMeshSurveyStateFixed_Object((1,3,6,1,4,1,28097,7,11,1,11),_StatusMeshSurveyStateFixed_Type())
statusMeshSurveyStateFixed.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyStateFixed.setStatus(_A)
_StatusMeshSurveyStateResolved_Type=TruthValue
_StatusMeshSurveyStateResolved_Object=MibTableColumn
statusMeshSurveyStateResolved=_StatusMeshSurveyStateResolved_Object((1,3,6,1,4,1,28097,7,11,1,12),_StatusMeshSurveyStateResolved_Type())
statusMeshSurveyStateResolved.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyStateResolved.setStatus(_A)
_StatusMeshSurveyMeshId_Type=DisplayString
_StatusMeshSurveyMeshId_Object=MibTableColumn
statusMeshSurveyMeshId=_StatusMeshSurveyMeshId_Object((1,3,6,1,4,1,28097,7,11,1,13),_StatusMeshSurveyMeshId_Type())
statusMeshSurveyMeshId.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyMeshId.setStatus(_A)
_StatusMeshSurveyWlanIndex_Type=Integer32
_StatusMeshSurveyWlanIndex_Object=MibTableColumn
statusMeshSurveyWlanIndex=_StatusMeshSurveyWlanIndex_Object((1,3,6,1,4,1,28097,7,11,1,14),_StatusMeshSurveyWlanIndex_Type())
statusMeshSurveyWlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMeshSurveyWlanIndex.setStatus(_A)
_StatusPhyCellTable_Object=MibTable
statusPhyCellTable=_StatusPhyCellTable_Object((1,3,6,1,4,1,28097,7,12))
if mibBuilder.loadTexts:statusPhyCellTable.setStatus(_A)
_StatusPhyCellEntry_Object=MibTableRow
statusPhyCellEntry=_StatusPhyCellEntry_Object((1,3,6,1,4,1,28097,7,12,1))
statusPhyCellEntry.setIndexNames((0,_E,_AI))
if mibBuilder.loadTexts:statusPhyCellEntry.setStatus(_A)
_StatusPhyCellIndex_Type=Integer32
_StatusPhyCellIndex_Object=MibTableColumn
statusPhyCellIndex=_StatusPhyCellIndex_Object((1,3,6,1,4,1,28097,7,12,1,1),_StatusPhyCellIndex_Type())
statusPhyCellIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellIndex.setStatus(_A)
_StatusPhyCellLabel_Type=DisplayString
_StatusPhyCellLabel_Object=MibTableColumn
statusPhyCellLabel=_StatusPhyCellLabel_Object((1,3,6,1,4,1,28097,7,12,1,2),_StatusPhyCellLabel_Type())
statusPhyCellLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellLabel.setStatus(_A)
_StatusPhyCellFriendlyName_Type=OctetString
_StatusPhyCellFriendlyName_Object=MibTableColumn
statusPhyCellFriendlyName=_StatusPhyCellFriendlyName_Object((1,3,6,1,4,1,28097,7,12,1,3),_StatusPhyCellFriendlyName_Type())
statusPhyCellFriendlyName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellFriendlyName.setStatus(_A)
_StatusPhyCellEnable_Type=DisableEnable
_StatusPhyCellEnable_Object=MibTableColumn
statusPhyCellEnable=_StatusPhyCellEnable_Object((1,3,6,1,4,1,28097,7,12,1,4),_StatusPhyCellEnable_Type())
statusPhyCellEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellEnable.setStatus(_A)
_StatusPhyCellIMEI_Type=DisplayString
_StatusPhyCellIMEI_Object=MibTableColumn
statusPhyCellIMEI=_StatusPhyCellIMEI_Object((1,3,6,1,4,1,28097,7,12,1,5),_StatusPhyCellIMEI_Type())
statusPhyCellIMEI.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellIMEI.setStatus(_A)
_StatusPhyCellModel_Type=DisplayString
_StatusPhyCellModel_Object=MibTableColumn
statusPhyCellModel=_StatusPhyCellModel_Object((1,3,6,1,4,1,28097,7,12,1,6),_StatusPhyCellModel_Type())
statusPhyCellModel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellModel.setStatus(_A)
_StatusPhyCellName_Type=NetifName
_StatusPhyCellName_Object=MibTableColumn
statusPhyCellName=_StatusPhyCellName_Object((1,3,6,1,4,1,28097,7,12,1,7),_StatusPhyCellName_Type())
statusPhyCellName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellName.setStatus(_A)
_StatusPhyCellSimSelected_Type=Integer32
_StatusPhyCellSimSelected_Object=MibTableColumn
statusPhyCellSimSelected=_StatusPhyCellSimSelected_Object((1,3,6,1,4,1,28097,7,12,1,8),_StatusPhyCellSimSelected_Type())
statusPhyCellSimSelected.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellSimSelected.setStatus(_A)
_StatusPhyCellSimState_Type=DisplayString
_StatusPhyCellSimState_Object=MibTableColumn
statusPhyCellSimState=_StatusPhyCellSimState_Object((1,3,6,1,4,1,28097,7,12,1,9),_StatusPhyCellSimState_Type())
statusPhyCellSimState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellSimState.setStatus(_A)
_StatusPhyCellSimIMSI_Type=DisplayString
_StatusPhyCellSimIMSI_Object=MibTableColumn
statusPhyCellSimIMSI=_StatusPhyCellSimIMSI_Object((1,3,6,1,4,1,28097,7,12,1,10),_StatusPhyCellSimIMSI_Type())
statusPhyCellSimIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellSimIMSI.setStatus(_A)
_StatusPhyCellAttachMode_Type=CellAttachMode
_StatusPhyCellAttachMode_Object=MibTableColumn
statusPhyCellAttachMode=_StatusPhyCellAttachMode_Object((1,3,6,1,4,1,28097,7,12,1,11),_StatusPhyCellAttachMode_Type())
statusPhyCellAttachMode.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellAttachMode.setStatus(_A)
_StatusPhyCellOperator_Type=DisplayString
_StatusPhyCellOperator_Object=MibTableColumn
statusPhyCellOperator=_StatusPhyCellOperator_Object((1,3,6,1,4,1,28097,7,12,1,12),_StatusPhyCellOperator_Type())
statusPhyCellOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellOperator.setStatus(_A)
_StatusPhyCellMcc_Type=Integer32
_StatusPhyCellMcc_Object=MibTableColumn
statusPhyCellMcc=_StatusPhyCellMcc_Object((1,3,6,1,4,1,28097,7,12,1,13),_StatusPhyCellMcc_Type())
statusPhyCellMcc.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellMcc.setStatus(_A)
_StatusPhyCellMnc_Type=Integer32
_StatusPhyCellMnc_Object=MibTableColumn
statusPhyCellMnc=_StatusPhyCellMnc_Object((1,3,6,1,4,1,28097,7,12,1,14),_StatusPhyCellMnc_Type())
statusPhyCellMnc.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellMnc.setStatus(_A)
_StatusPhyCellBaseLAC_Type=Integer32
_StatusPhyCellBaseLAC_Object=MibTableColumn
statusPhyCellBaseLAC=_StatusPhyCellBaseLAC_Object((1,3,6,1,4,1,28097,7,12,1,15),_StatusPhyCellBaseLAC_Type())
statusPhyCellBaseLAC.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellBaseLAC.setStatus(_A)
_StatusPhyCellBaseCID_Type=Integer32
_StatusPhyCellBaseCID_Object=MibTableColumn
statusPhyCellBaseCID=_StatusPhyCellBaseCID_Object((1,3,6,1,4,1,28097,7,12,1,16),_StatusPhyCellBaseCID_Type())
statusPhyCellBaseCID.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellBaseCID.setStatus(_A)
_StatusPhyCellRegistrationClass_Type=DisplayString
_StatusPhyCellRegistrationClass_Object=MibTableColumn
statusPhyCellRegistrationClass=_StatusPhyCellRegistrationClass_Object((1,3,6,1,4,1,28097,7,12,1,17),_StatusPhyCellRegistrationClass_Type())
statusPhyCellRegistrationClass.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellRegistrationClass.setStatus(_A)
_StatusPhyCellAccessTech_Type=CellAccessTech
_StatusPhyCellAccessTech_Object=MibTableColumn
statusPhyCellAccessTech=_StatusPhyCellAccessTech_Object((1,3,6,1,4,1,28097,7,12,1,18),_StatusPhyCellAccessTech_Type())
statusPhyCellAccessTech.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellAccessTech.setStatus(_A)
_StatusPhyCellBandName_Type=DisplayString
_StatusPhyCellBandName_Object=MibTableColumn
statusPhyCellBandName=_StatusPhyCellBandName_Object((1,3,6,1,4,1,28097,7,12,1,19),_StatusPhyCellBandName_Type())
statusPhyCellBandName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellBandName.setStatus(_A)
_StatusPhyCellARFCN_Type=Integer32
_StatusPhyCellARFCN_Object=MibTableColumn
statusPhyCellARFCN=_StatusPhyCellARFCN_Object((1,3,6,1,4,1,28097,7,12,1,20),_StatusPhyCellARFCN_Type())
statusPhyCellARFCN.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellARFCN.setStatus(_A)
_StatusPhyCellRSSI_Type=Integer32
_StatusPhyCellRSSI_Object=MibTableColumn
statusPhyCellRSSI=_StatusPhyCellRSSI_Object((1,3,6,1,4,1,28097,7,12,1,21),_StatusPhyCellRSSI_Type())
statusPhyCellRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellRSSI.setStatus(_A)
_StatusPhyCellBER_Type=Integer32
_StatusPhyCellBER_Object=MibTableColumn
statusPhyCellBER=_StatusPhyCellBER_Object((1,3,6,1,4,1,28097,7,12,1,22),_StatusPhyCellBER_Type())
statusPhyCellBER.setMaxAccess(_C)
if mibBuilder.loadTexts:statusPhyCellBER.setStatus(_A)
_StatusRoaming_ObjectIdentity=ObjectIdentity
statusRoaming=_StatusRoaming_ObjectIdentity((1,3,6,1,4,1,28097,7,13))
_StatusRoamingLeaveLvlMax_Type=Integer32
_StatusRoamingLeaveLvlMax_Object=MibScalar
statusRoamingLeaveLvlMax=_StatusRoamingLeaveLvlMax_Object((1,3,6,1,4,1,28097,7,13,1),_StatusRoamingLeaveLvlMax_Type())
statusRoamingLeaveLvlMax.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingLeaveLvlMax.setStatus(_A)
_StatusRoamingLeaveLvlMin_Type=Integer32
_StatusRoamingLeaveLvlMin_Object=MibScalar
statusRoamingLeaveLvlMin=_StatusRoamingLeaveLvlMin_Object((1,3,6,1,4,1,28097,7,13,2),_StatusRoamingLeaveLvlMin_Type())
statusRoamingLeaveLvlMin.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingLeaveLvlMin.setStatus(_A)
_StatusRoamingRoamLvlMax_Type=Integer32
_StatusRoamingRoamLvlMax_Object=MibScalar
statusRoamingRoamLvlMax=_StatusRoamingRoamLvlMax_Object((1,3,6,1,4,1,28097,7,13,3),_StatusRoamingRoamLvlMax_Type())
statusRoamingRoamLvlMax.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingRoamLvlMax.setStatus(_A)
_StatusRoamingRoamLvlMin_Type=Integer32
_StatusRoamingRoamLvlMin_Object=MibScalar
statusRoamingRoamLvlMin=_StatusRoamingRoamLvlMin_Object((1,3,6,1,4,1,28097,7,13,4),_StatusRoamingRoamLvlMin_Type())
statusRoamingRoamLvlMin.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingRoamLvlMin.setStatus(_A)
_StatusRoamingThresHyst_Type=Integer32
_StatusRoamingThresHyst_Object=MibScalar
statusRoamingThresHyst=_StatusRoamingThresHyst_Object((1,3,6,1,4,1,28097,7,13,5),_StatusRoamingThresHyst_Type())
statusRoamingThresHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingThresHyst.setStatus(_A)
_StatusRoamingLeaveBoost_Type=Integer32
_StatusRoamingLeaveBoost_Object=MibScalar
statusRoamingLeaveBoost=_StatusRoamingLeaveBoost_Object((1,3,6,1,4,1,28097,7,13,6),_StatusRoamingLeaveBoost_Type())
statusRoamingLeaveBoost.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingLeaveBoost.setStatus(_A)
_StatusRoamingActiveIf_ObjectIdentity=ObjectIdentity
statusRoamingActiveIf=_StatusRoamingActiveIf_ObjectIdentity((1,3,6,1,4,1,28097,7,13,7))
_StatusRoamingActiveIfName_Type=OctetString
_StatusRoamingActiveIfName_Object=MibScalar
statusRoamingActiveIfName=_StatusRoamingActiveIfName_Object((1,3,6,1,4,1,28097,7,13,7,1),_StatusRoamingActiveIfName_Type())
statusRoamingActiveIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfName.setStatus(_A)
_StatusRoamingActiveIfBssid_Type=PhysAddress
_StatusRoamingActiveIfBssid_Object=MibScalar
statusRoamingActiveIfBssid=_StatusRoamingActiveIfBssid_Object((1,3,6,1,4,1,28097,7,13,7,2),_StatusRoamingActiveIfBssid_Type())
statusRoamingActiveIfBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfBssid.setStatus(_A)
_StatusRoamingActiveIfBeaconSignalAvg_Type=Integer32
_StatusRoamingActiveIfBeaconSignalAvg_Object=MibScalar
statusRoamingActiveIfBeaconSignalAvg=_StatusRoamingActiveIfBeaconSignalAvg_Object((1,3,6,1,4,1,28097,7,13,7,3),_StatusRoamingActiveIfBeaconSignalAvg_Type())
statusRoamingActiveIfBeaconSignalAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfBeaconSignalAvg.setStatus(_A)
_StatusRoamingActiveIfNoise_Type=Integer32
_StatusRoamingActiveIfNoise_Object=MibScalar
statusRoamingActiveIfNoise=_StatusRoamingActiveIfNoise_Object((1,3,6,1,4,1,28097,7,13,7,4),_StatusRoamingActiveIfNoise_Type())
statusRoamingActiveIfNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfNoise.setStatus(_A)
class _StatusRoamingActiveIfSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_StatusRoamingActiveIfSwitching_Type.__name__=_D
_StatusRoamingActiveIfSwitching_Object=MibScalar
statusRoamingActiveIfSwitching=_StatusRoamingActiveIfSwitching_Object((1,3,6,1,4,1,28097,7,13,7,5),_StatusRoamingActiveIfSwitching_Type())
statusRoamingActiveIfSwitching.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfSwitching.setStatus(_A)
_StatusRoamingActiveIfChannel_Type=Integer32
_StatusRoamingActiveIfChannel_Object=MibScalar
statusRoamingActiveIfChannel=_StatusRoamingActiveIfChannel_Object((1,3,6,1,4,1,28097,7,13,7,6),_StatusRoamingActiveIfChannel_Type())
statusRoamingActiveIfChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfChannel.setStatus(_A)
class _StatusRoamingActiveIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,9)));namedValues=NamedValues(*((_q,0),(_r,9)))
_StatusRoamingActiveIfState_Type.__name__=_D
_StatusRoamingActiveIfState_Object=MibScalar
statusRoamingActiveIfState=_StatusRoamingActiveIfState_Object((1,3,6,1,4,1,28097,7,13,7,7),_StatusRoamingActiveIfState_Type())
statusRoamingActiveIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingActiveIfState.setStatus(_A)
_StatusRoamingPassiveIf_ObjectIdentity=ObjectIdentity
statusRoamingPassiveIf=_StatusRoamingPassiveIf_ObjectIdentity((1,3,6,1,4,1,28097,7,13,8))
_StatusRoamingPassiveIfName_Type=OctetString
_StatusRoamingPassiveIfName_Object=MibScalar
statusRoamingPassiveIfName=_StatusRoamingPassiveIfName_Object((1,3,6,1,4,1,28097,7,13,8,1),_StatusRoamingPassiveIfName_Type())
statusRoamingPassiveIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfName.setStatus(_A)
_StatusRoamingPassiveIfBssid_Type=PhysAddress
_StatusRoamingPassiveIfBssid_Object=MibScalar
statusRoamingPassiveIfBssid=_StatusRoamingPassiveIfBssid_Object((1,3,6,1,4,1,28097,7,13,8,2),_StatusRoamingPassiveIfBssid_Type())
statusRoamingPassiveIfBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfBssid.setStatus(_A)
_StatusRoamingPassiveIfBeaconSignalAvg_Type=Integer32
_StatusRoamingPassiveIfBeaconSignalAvg_Object=MibScalar
statusRoamingPassiveIfBeaconSignalAvg=_StatusRoamingPassiveIfBeaconSignalAvg_Object((1,3,6,1,4,1,28097,7,13,8,3),_StatusRoamingPassiveIfBeaconSignalAvg_Type())
statusRoamingPassiveIfBeaconSignalAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfBeaconSignalAvg.setStatus(_A)
_StatusRoamingPassiveIfNoise_Type=Integer32
_StatusRoamingPassiveIfNoise_Object=MibScalar
statusRoamingPassiveIfNoise=_StatusRoamingPassiveIfNoise_Object((1,3,6,1,4,1,28097,7,13,8,4),_StatusRoamingPassiveIfNoise_Type())
statusRoamingPassiveIfNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfNoise.setStatus(_A)
class _StatusRoamingPassiveIfSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_StatusRoamingPassiveIfSwitching_Type.__name__=_D
_StatusRoamingPassiveIfSwitching_Object=MibScalar
statusRoamingPassiveIfSwitching=_StatusRoamingPassiveIfSwitching_Object((1,3,6,1,4,1,28097,7,13,8,5),_StatusRoamingPassiveIfSwitching_Type())
statusRoamingPassiveIfSwitching.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfSwitching.setStatus(_A)
_StatusRoamingPassiveIfChannel_Type=Integer32
_StatusRoamingPassiveIfChannel_Object=MibScalar
statusRoamingPassiveIfChannel=_StatusRoamingPassiveIfChannel_Object((1,3,6,1,4,1,28097,7,13,8,6),_StatusRoamingPassiveIfChannel_Type())
statusRoamingPassiveIfChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfChannel.setStatus(_A)
class _StatusRoamingPassiveIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,9)));namedValues=NamedValues(*((_q,0),(_r,9)))
_StatusRoamingPassiveIfState_Type.__name__=_D
_StatusRoamingPassiveIfState_Object=MibScalar
statusRoamingPassiveIfState=_StatusRoamingPassiveIfState_Object((1,3,6,1,4,1,28097,7,13,8,7),_StatusRoamingPassiveIfState_Type())
statusRoamingPassiveIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingPassiveIfState.setStatus(_A)
_StatusRoamingUrgent_Type=DisableEnable
_StatusRoamingUrgent_Object=MibScalar
statusRoamingUrgent=_StatusRoamingUrgent_Object((1,3,6,1,4,1,28097,7,13,9),_StatusRoamingUrgent_Type())
statusRoamingUrgent.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRoamingUrgent.setStatus(_A)
_NetworkConfiguration_ObjectIdentity=ObjectIdentity
networkConfiguration=_NetworkConfiguration_ObjectIdentity((1,3,6,1,4,1,28097,8))
_Tcpip_ObjectIdentity=ObjectIdentity
tcpip=_Tcpip_ObjectIdentity((1,3,6,1,4,1,28097,8,1))
_ConfigIpSubnetTable_Object=MibTable
configIpSubnetTable=_ConfigIpSubnetTable_Object((1,3,6,1,4,1,28097,8,1,1))
if mibBuilder.loadTexts:configIpSubnetTable.setStatus(_A)
_ConfigIpSubnetEntry_Object=MibTableRow
configIpSubnetEntry=_ConfigIpSubnetEntry_Object((1,3,6,1,4,1,28097,8,1,1,1))
configIpSubnetEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:configIpSubnetEntry.setStatus(_A)
_ConfigIpSubnetName_Type=NetifName
_ConfigIpSubnetName_Object=MibTableColumn
configIpSubnetName=_ConfigIpSubnetName_Object((1,3,6,1,4,1,28097,8,1,1,1,1),_ConfigIpSubnetName_Type())
configIpSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:configIpSubnetName.setStatus(_A)
_ConfigIpSubnetRowStatus_Type=RowStatus
_ConfigIpSubnetRowStatus_Object=MibTableColumn
configIpSubnetRowStatus=_ConfigIpSubnetRowStatus_Object((1,3,6,1,4,1,28097,8,1,1,1,2),_ConfigIpSubnetRowStatus_Type())
configIpSubnetRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpSubnetRowStatus.setStatus(_A)
class _ConfigIpAddressMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_d,1),(_e,2),(_N,3),('vrrp',4)))
_ConfigIpAddressMode_Type.__name__=_D
_ConfigIpAddressMode_Object=MibTableColumn
configIpAddressMode=_ConfigIpAddressMode_Object((1,3,6,1,4,1,28097,8,1,1,1,3),_ConfigIpAddressMode_Type())
configIpAddressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpAddressMode.setStatus(_A)
_ConfigIpSubnetIPv4Addr_Type=IpAddress
_ConfigIpSubnetIPv4Addr_Object=MibTableColumn
configIpSubnetIPv4Addr=_ConfigIpSubnetIPv4Addr_Object((1,3,6,1,4,1,28097,8,1,1,1,4),_ConfigIpSubnetIPv4Addr_Type())
configIpSubnetIPv4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetIPv4Addr.setStatus(_A)
_ConfigIpSubnetIPv4Mask_Type=IpAddress
_ConfigIpSubnetIPv4Mask_Object=MibTableColumn
configIpSubnetIPv4Mask=_ConfigIpSubnetIPv4Mask_Object((1,3,6,1,4,1,28097,8,1,1,1,5),_ConfigIpSubnetIPv4Mask_Type())
configIpSubnetIPv4Mask.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetIPv4Mask.setStatus(_A)
_ConfigIpSubnetMetric_Type=Integer32
_ConfigIpSubnetMetric_Object=MibTableColumn
configIpSubnetMetric=_ConfigIpSubnetMetric_Object((1,3,6,1,4,1,28097,8,1,1,1,6),_ConfigIpSubnetMetric_Type())
configIpSubnetMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetMetric.setStatus(_A)
_ConfigIpSubnetDnsList_Type=OctetString
_ConfigIpSubnetDnsList_Object=MibTableColumn
configIpSubnetDnsList=_ConfigIpSubnetDnsList_Object((1,3,6,1,4,1,28097,8,1,1,1,7),_ConfigIpSubnetDnsList_Type())
configIpSubnetDnsList.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetDnsList.setStatus(_A)
_ConfigIpSubnetInterface_Type=OctetString
_ConfigIpSubnetInterface_Object=MibTableColumn
configIpSubnetInterface=_ConfigIpSubnetInterface_Object((1,3,6,1,4,1,28097,8,1,1,1,8),_ConfigIpSubnetInterface_Type())
configIpSubnetInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetInterface.setStatus(_A)
_ConfigIpSubnetIPv4Gateway_Type=IpAddress
_ConfigIpSubnetIPv4Gateway_Object=MibTableColumn
configIpSubnetIPv4Gateway=_ConfigIpSubnetIPv4Gateway_Object((1,3,6,1,4,1,28097,8,1,1,1,9),_ConfigIpSubnetIPv4Gateway_Type())
configIpSubnetIPv4Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetIPv4Gateway.setStatus(_A)
_ConfigIpSubnetFriendlyName_Type=OctetString
_ConfigIpSubnetFriendlyName_Object=MibTableColumn
configIpSubnetFriendlyName=_ConfigIpSubnetFriendlyName_Object((1,3,6,1,4,1,28097,8,1,1,1,10),_ConfigIpSubnetFriendlyName_Type())
configIpSubnetFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetFriendlyName.setStatus(_A)
_ConfigIpSubnetBridgeEnable_Type=DisableEnable
_ConfigIpSubnetBridgeEnable_Object=MibTableColumn
configIpSubnetBridgeEnable=_ConfigIpSubnetBridgeEnable_Object((1,3,6,1,4,1,28097,8,1,1,1,11),_ConfigIpSubnetBridgeEnable_Type())
configIpSubnetBridgeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetBridgeEnable.setStatus(_A)
_ConfigIpSubnetPersistence_Type=TriState
_ConfigIpSubnetPersistence_Object=MibTableColumn
configIpSubnetPersistence=_ConfigIpSubnetPersistence_Object((1,3,6,1,4,1,28097,8,1,1,1,12),_ConfigIpSubnetPersistence_Type())
configIpSubnetPersistence.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetPersistence.setStatus(_A)
_ConfigIpSubnetEnable_Type=DisableEnable
_ConfigIpSubnetEnable_Object=MibTableColumn
configIpSubnetEnable=_ConfigIpSubnetEnable_Object((1,3,6,1,4,1,28097,8,1,1,1,13),_ConfigIpSubnetEnable_Type())
configIpSubnetEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetEnable.setStatus(_A)
_ConfigIpSubnetAutoStart_Type=TriState
_ConfigIpSubnetAutoStart_Object=MibTableColumn
configIpSubnetAutoStart=_ConfigIpSubnetAutoStart_Object((1,3,6,1,4,1,28097,8,1,1,1,14),_ConfigIpSubnetAutoStart_Type())
configIpSubnetAutoStart.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetAutoStart.setStatus(_A)
_ConfigIpSubnetPeerDns_Type=DisableEnable
_ConfigIpSubnetPeerDns_Object=MibTableColumn
configIpSubnetPeerDns=_ConfigIpSubnetPeerDns_Object((1,3,6,1,4,1,28097,8,1,1,1,15),_ConfigIpSubnetPeerDns_Type())
configIpSubnetPeerDns.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetPeerDns.setStatus(_A)
_ConfigIpSubnetDefaultRoute_Type=DisableEnable
_ConfigIpSubnetDefaultRoute_Object=MibTableColumn
configIpSubnetDefaultRoute=_ConfigIpSubnetDefaultRoute_Object((1,3,6,1,4,1,28097,8,1,1,1,16),_ConfigIpSubnetDefaultRoute_Type())
configIpSubnetDefaultRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpSubnetDefaultRoute.setStatus(_A)
_IpFactory_ObjectIdentity=ObjectIdentity
ipFactory=_IpFactory_ObjectIdentity((1,3,6,1,4,1,28097,8,1,2))
_Synfloodprotection_Type=DisableEnable
_Synfloodprotection_Object=MibScalar
synfloodprotection=_Synfloodprotection_Object((1,3,6,1,4,1,28097,8,1,2,1),_Synfloodprotection_Type())
synfloodprotection.setMaxAccess(_B)
if mibBuilder.loadTexts:synfloodprotection.setStatus(_A)
_Dropinvalidpacket_Type=DisableEnable
_Dropinvalidpacket_Object=MibScalar
dropinvalidpacket=_Dropinvalidpacket_Object((1,3,6,1,4,1,28097,8,1,2,2),_Dropinvalidpacket_Type())
dropinvalidpacket.setMaxAccess(_B)
if mibBuilder.loadTexts:dropinvalidpacket.setStatus(_A)
_ConfigIpZonesTable_Object=MibTable
configIpZonesTable=_ConfigIpZonesTable_Object((1,3,6,1,4,1,28097,8,1,2,3))
if mibBuilder.loadTexts:configIpZonesTable.setStatus(_A)
_ConfigIpZonesEntry_Object=MibTableRow
configIpZonesEntry=_ConfigIpZonesEntry_Object((1,3,6,1,4,1,28097,8,1,2,3,1))
configIpZonesEntry.setIndexNames((0,_E,_AK))
if mibBuilder.loadTexts:configIpZonesEntry.setStatus(_A)
_ConfigIpZoneIndex_Type=OctetString
_ConfigIpZoneIndex_Object=MibTableColumn
configIpZoneIndex=_ConfigIpZoneIndex_Object((1,3,6,1,4,1,28097,8,1,2,3,1,1),_ConfigIpZoneIndex_Type())
configIpZoneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneIndex.setStatus(_A)
_ConfigIpZoneRowStatus_Type=RowStatus
_ConfigIpZoneRowStatus_Object=MibTableColumn
configIpZoneRowStatus=_ConfigIpZoneRowStatus_Object((1,3,6,1,4,1,28097,8,1,2,3,1,2),_ConfigIpZoneRowStatus_Type())
configIpZoneRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpZoneRowStatus.setStatus(_A)
_ConfigIpZoneFriendlyName_Type=OctetString
_ConfigIpZoneFriendlyName_Object=MibTableColumn
configIpZoneFriendlyName=_ConfigIpZoneFriendlyName_Object((1,3,6,1,4,1,28097,8,1,2,3,1,3),_ConfigIpZoneFriendlyName_Type())
configIpZoneFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneFriendlyName.setStatus(_A)
_ConfigIpZoneNAT_Type=DisableEnable
_ConfigIpZoneNAT_Object=MibTableColumn
configIpZoneNAT=_ConfigIpZoneNAT_Object((1,3,6,1,4,1,28097,8,1,2,3,1,4),_ConfigIpZoneNAT_Type())
configIpZoneNAT.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneNAT.setStatus(_A)
_ConfigIpZoneMSSClamping_Type=DisableEnable
_ConfigIpZoneMSSClamping_Object=MibTableColumn
configIpZoneMSSClamping=_ConfigIpZoneMSSClamping_Object((1,3,6,1,4,1,28097,8,1,2,3,1,5),_ConfigIpZoneMSSClamping_Type())
configIpZoneMSSClamping.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneMSSClamping.setStatus(_A)
class _ConfigIpZoneDefaultAcceptancePolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allenable',1),('alldisable',2)))
_ConfigIpZoneDefaultAcceptancePolicy_Type.__name__=_D
_ConfigIpZoneDefaultAcceptancePolicy_Object=MibTableColumn
configIpZoneDefaultAcceptancePolicy=_ConfigIpZoneDefaultAcceptancePolicy_Object((1,3,6,1,4,1,28097,8,1,2,3,1,6),_ConfigIpZoneDefaultAcceptancePolicy_Type())
configIpZoneDefaultAcceptancePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneDefaultAcceptancePolicy.setStatus(_A)
class _ConfigIpZoneRestrictedAddressFamily_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4ipv6',1),('ipv4',2),('ipv6',3)))
_ConfigIpZoneRestrictedAddressFamily_Type.__name__=_D
_ConfigIpZoneRestrictedAddressFamily_Object=MibTableColumn
configIpZoneRestrictedAddressFamily=_ConfigIpZoneRestrictedAddressFamily_Object((1,3,6,1,4,1,28097,8,1,2,3,1,7),_ConfigIpZoneRestrictedAddressFamily_Type())
configIpZoneRestrictedAddressFamily.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneRestrictedAddressFamily.setStatus(_A)
_ConfigIpZoneConnectionTracking_Type=DisableEnable
_ConfigIpZoneConnectionTracking_Object=MibTableColumn
configIpZoneConnectionTracking=_ConfigIpZoneConnectionTracking_Object((1,3,6,1,4,1,28097,8,1,2,3,1,8),_ConfigIpZoneConnectionTracking_Type())
configIpZoneConnectionTracking.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneConnectionTracking.setStatus(_A)
_ConfigIpZoneLogging_Type=DisableEnable
_ConfigIpZoneLogging_Object=MibTableColumn
configIpZoneLogging=_ConfigIpZoneLogging_Object((1,3,6,1,4,1,28097,8,1,2,3,1,9),_ConfigIpZoneLogging_Type())
configIpZoneLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneLogging.setStatus(_A)
_ConfigIpZoneLoggingLimit_Type=OctetString
_ConfigIpZoneLoggingLimit_Object=MibTableColumn
configIpZoneLoggingLimit=_ConfigIpZoneLoggingLimit_Object((1,3,6,1,4,1,28097,8,1,2,3,1,10),_ConfigIpZoneLoggingLimit_Type())
configIpZoneLoggingLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneLoggingLimit.setStatus(_A)
_ConfigIpZoneInterfaces_Type=OctetString
_ConfigIpZoneInterfaces_Object=MibTableColumn
configIpZoneInterfaces=_ConfigIpZoneInterfaces_Object((1,3,6,1,4,1,28097,8,1,2,3,1,11),_ConfigIpZoneInterfaces_Type())
configIpZoneInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneInterfaces.setStatus(_A)
_ConfigIpNatIpForwardTable_Object=MibTable
configIpNatIpForwardTable=_ConfigIpNatIpForwardTable_Object((1,3,6,1,4,1,28097,8,1,2,4))
if mibBuilder.loadTexts:configIpNatIpForwardTable.setStatus(_A)
_ConfigIpNatIpForwardEntry_Object=MibTableRow
configIpNatIpForwardEntry=_ConfigIpNatIpForwardEntry_Object((1,3,6,1,4,1,28097,8,1,2,4,1))
configIpNatIpForwardEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:configIpNatIpForwardEntry.setStatus(_A)
_ConfigIpNatIpForwardIndex_Type=OctetString
_ConfigIpNatIpForwardIndex_Object=MibTableColumn
configIpNatIpForwardIndex=_ConfigIpNatIpForwardIndex_Object((1,3,6,1,4,1,28097,8,1,2,4,1,1),_ConfigIpNatIpForwardIndex_Type())
configIpNatIpForwardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardIndex.setStatus(_A)
_ConfigIpNatIpForwardRowStatus_Type=RowStatus
_ConfigIpNatIpForwardRowStatus_Object=MibTableColumn
configIpNatIpForwardRowStatus=_ConfigIpNatIpForwardRowStatus_Object((1,3,6,1,4,1,28097,8,1,2,4,1,2),_ConfigIpNatIpForwardRowStatus_Type())
configIpNatIpForwardRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpNatIpForwardRowStatus.setStatus(_A)
_ConfigIpNatIpForwardFriendlyName_Type=OctetString
_ConfigIpNatIpForwardFriendlyName_Object=MibTableColumn
configIpNatIpForwardFriendlyName=_ConfigIpNatIpForwardFriendlyName_Object((1,3,6,1,4,1,28097,8,1,2,4,1,3),_ConfigIpNatIpForwardFriendlyName_Type())
configIpNatIpForwardFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardFriendlyName.setStatus(_A)
_ConfigIpNatIpForwardZoneName_Type=OctetString
_ConfigIpNatIpForwardZoneName_Object=MibTableColumn
configIpNatIpForwardZoneName=_ConfigIpNatIpForwardZoneName_Object((1,3,6,1,4,1,28097,8,1,2,4,1,4),_ConfigIpNatIpForwardZoneName_Type())
configIpNatIpForwardZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardZoneName.setStatus(_A)
_ConfigIpNatIpForwardSrcIp_Type=IpAddress
_ConfigIpNatIpForwardSrcIp_Object=MibTableColumn
configIpNatIpForwardSrcIp=_ConfigIpNatIpForwardSrcIp_Object((1,3,6,1,4,1,28097,8,1,2,4,1,5),_ConfigIpNatIpForwardSrcIp_Type())
configIpNatIpForwardSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardSrcIp.setStatus(_A)
class _ConfigIpNatIpForwardProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_t,1),(_i,2),(_j,3),('tcpudp',4),(_k,5)))
_ConfigIpNatIpForwardProtocol_Type.__name__=_D
_ConfigIpNatIpForwardProtocol_Object=MibTableColumn
configIpNatIpForwardProtocol=_ConfigIpNatIpForwardProtocol_Object((1,3,6,1,4,1,28097,8,1,2,4,1,6),_ConfigIpNatIpForwardProtocol_Type())
configIpNatIpForwardProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardProtocol.setStatus(_A)
_ConfigIpNatIpForwardPublicPort_Type=OctetString
_ConfigIpNatIpForwardPublicPort_Object=MibTableColumn
configIpNatIpForwardPublicPort=_ConfigIpNatIpForwardPublicPort_Object((1,3,6,1,4,1,28097,8,1,2,4,1,7),_ConfigIpNatIpForwardPublicPort_Type())
configIpNatIpForwardPublicPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardPublicPort.setStatus(_A)
_ConfigIpNatIpForwardPrivatePort_Type=OctetString
_ConfigIpNatIpForwardPrivatePort_Object=MibTableColumn
configIpNatIpForwardPrivatePort=_ConfigIpNatIpForwardPrivatePort_Object((1,3,6,1,4,1,28097,8,1,2,4,1,8),_ConfigIpNatIpForwardPrivatePort_Type())
configIpNatIpForwardPrivatePort.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardPrivatePort.setStatus(_A)
_ConfigIpNatIpForwardTargetIp_Type=IpAddress
_ConfigIpNatIpForwardTargetIp_Object=MibTableColumn
configIpNatIpForwardTargetIp=_ConfigIpNatIpForwardTargetIp_Object((1,3,6,1,4,1,28097,8,1,2,4,1,9),_ConfigIpNatIpForwardTargetIp_Type())
configIpNatIpForwardTargetIp.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpNatIpForwardTargetIp.setStatus(_A)
_ConfigIpFirewallTable_Object=MibTable
configIpFirewallTable=_ConfigIpFirewallTable_Object((1,3,6,1,4,1,28097,8,1,2,5))
if mibBuilder.loadTexts:configIpFirewallTable.setStatus(_A)
_ConfigIpFirewallEntry_Object=MibTableRow
configIpFirewallEntry=_ConfigIpFirewallEntry_Object((1,3,6,1,4,1,28097,8,1,2,5,1))
configIpFirewallEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:configIpFirewallEntry.setStatus(_A)
_ConfigIpFirewallIndex_Type=OctetString
_ConfigIpFirewallIndex_Object=MibTableColumn
configIpFirewallIndex=_ConfigIpFirewallIndex_Object((1,3,6,1,4,1,28097,8,1,2,5,1,1),_ConfigIpFirewallIndex_Type())
configIpFirewallIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallIndex.setStatus(_A)
_ConfigIpFirewallRowStatus_Type=RowStatus
_ConfigIpFirewallRowStatus_Object=MibTableColumn
configIpFirewallRowStatus=_ConfigIpFirewallRowStatus_Object((1,3,6,1,4,1,28097,8,1,2,5,1,2),_ConfigIpFirewallRowStatus_Type())
configIpFirewallRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpFirewallRowStatus.setStatus(_A)
_ConfigIpFirewallZoneName_Type=OctetString
_ConfigIpFirewallZoneName_Object=MibTableColumn
configIpFirewallZoneName=_ConfigIpFirewallZoneName_Object((1,3,6,1,4,1,28097,8,1,2,5,1,3),_ConfigIpFirewallZoneName_Type())
configIpFirewallZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallZoneName.setStatus(_A)
class _ConfigIpFirewallProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_t,1),(_i,2),(_j,3),('tcpudp',4),(_k,5),('gre',6)))
_ConfigIpFirewallProtocol_Type.__name__=_D
_ConfigIpFirewallProtocol_Object=MibTableColumn
configIpFirewallProtocol=_ConfigIpFirewallProtocol_Object((1,3,6,1,4,1,28097,8,1,2,5,1,4),_ConfigIpFirewallProtocol_Type())
configIpFirewallProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallProtocol.setStatus(_A)
_ConfigIpFirewallPort_Type=OctetString
_ConfigIpFirewallPort_Object=MibTableColumn
configIpFirewallPort=_ConfigIpFirewallPort_Object((1,3,6,1,4,1,28097,8,1,2,5,1,5),_ConfigIpFirewallPort_Type())
configIpFirewallPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallPort.setStatus(_A)
class _ConfigIpFirewallAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward',1),('reject',2),('drop',3)))
_ConfigIpFirewallAction_Type.__name__=_D
_ConfigIpFirewallAction_Object=MibTableColumn
configIpFirewallAction=_ConfigIpFirewallAction_Object((1,3,6,1,4,1,28097,8,1,2,5,1,6),_ConfigIpFirewallAction_Type())
configIpFirewallAction.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallAction.setStatus(_A)
_ConfigIpFirewallDestZone_Type=OctetString
_ConfigIpFirewallDestZone_Object=MibTableColumn
configIpFirewallDestZone=_ConfigIpFirewallDestZone_Object((1,3,6,1,4,1,28097,8,1,2,5,1,7),_ConfigIpFirewallDestZone_Type())
configIpFirewallDestZone.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallDestZone.setStatus(_A)
_ConfigIpFirewallSrcIP_Type=IpAddress
_ConfigIpFirewallSrcIP_Object=MibTableColumn
configIpFirewallSrcIP=_ConfigIpFirewallSrcIP_Object((1,3,6,1,4,1,28097,8,1,2,5,1,8),_ConfigIpFirewallSrcIP_Type())
configIpFirewallSrcIP.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallSrcIP.setStatus(_A)
_ConfigIpFirewallTargetIP_Type=IpAddress
_ConfigIpFirewallTargetIP_Object=MibTableColumn
configIpFirewallTargetIP=_ConfigIpFirewallTargetIP_Object((1,3,6,1,4,1,28097,8,1,2,5,1,9),_ConfigIpFirewallTargetIP_Type())
configIpFirewallTargetIP.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpFirewallTargetIP.setStatus(_A)
_ConfigIpRoutesTable_Object=MibTable
configIpRoutesTable=_ConfigIpRoutesTable_Object((1,3,6,1,4,1,28097,8,1,2,6))
if mibBuilder.loadTexts:configIpRoutesTable.setStatus(_A)
_ConfigIpRoutesEntry_Object=MibTableRow
configIpRoutesEntry=_ConfigIpRoutesEntry_Object((1,3,6,1,4,1,28097,8,1,2,6,1))
configIpRoutesEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:configIpRoutesEntry.setStatus(_A)
_ConfigIpRoutesIndex_Type=Integer32
_ConfigIpRoutesIndex_Object=MibTableColumn
configIpRoutesIndex=_ConfigIpRoutesIndex_Object((1,3,6,1,4,1,28097,8,1,2,6,1,1),_ConfigIpRoutesIndex_Type())
configIpRoutesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesIndex.setStatus(_A)
_ConfigIpRoutesRowStatus_Type=RowStatus
_ConfigIpRoutesRowStatus_Object=MibTableColumn
configIpRoutesRowStatus=_ConfigIpRoutesRowStatus_Object((1,3,6,1,4,1,28097,8,1,2,6,1,2),_ConfigIpRoutesRowStatus_Type())
configIpRoutesRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpRoutesRowStatus.setStatus(_A)
_ConfigIpRoutesNetwork_Type=OctetString
_ConfigIpRoutesNetwork_Object=MibTableColumn
configIpRoutesNetwork=_ConfigIpRoutesNetwork_Object((1,3,6,1,4,1,28097,8,1,2,6,1,3),_ConfigIpRoutesNetwork_Type())
configIpRoutesNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesNetwork.setStatus(_A)
_ConfigIpRoutesTarget_Type=IpAddress
_ConfigIpRoutesTarget_Object=MibTableColumn
configIpRoutesTarget=_ConfigIpRoutesTarget_Object((1,3,6,1,4,1,28097,8,1,2,6,1,4),_ConfigIpRoutesTarget_Type())
configIpRoutesTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesTarget.setStatus(_A)
_ConfigIpRoutesNetmask_Type=IpAddress
_ConfigIpRoutesNetmask_Object=MibTableColumn
configIpRoutesNetmask=_ConfigIpRoutesNetmask_Object((1,3,6,1,4,1,28097,8,1,2,6,1,5),_ConfigIpRoutesNetmask_Type())
configIpRoutesNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesNetmask.setStatus(_A)
_ConfigIpRoutesGateway_Type=IpAddress
_ConfigIpRoutesGateway_Object=MibTableColumn
configIpRoutesGateway=_ConfigIpRoutesGateway_Object((1,3,6,1,4,1,28097,8,1,2,6,1,6),_ConfigIpRoutesGateway_Type())
configIpRoutesGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesGateway.setStatus(_A)
_ConfigIpRoutesMetric_Type=Integer32
_ConfigIpRoutesMetric_Object=MibTableColumn
configIpRoutesMetric=_ConfigIpRoutesMetric_Object((1,3,6,1,4,1,28097,8,1,2,6,1,7),_ConfigIpRoutesMetric_Type())
configIpRoutesMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesMetric.setStatus(_A)
_ConfigIpRoutesMTU_Type=Integer32
_ConfigIpRoutesMTU_Object=MibTableColumn
configIpRoutesMTU=_ConfigIpRoutesMTU_Object((1,3,6,1,4,1,28097,8,1,2,6,1,8),_ConfigIpRoutesMTU_Type())
configIpRoutesMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpRoutesMTU.setStatus(_A)
_ConfigIpZoneForwardTable_Object=MibTable
configIpZoneForwardTable=_ConfigIpZoneForwardTable_Object((1,3,6,1,4,1,28097,8,1,2,7))
if mibBuilder.loadTexts:configIpZoneForwardTable.setStatus(_A)
_ConfigIpZoneForwardEntry_Object=MibTableRow
configIpZoneForwardEntry=_ConfigIpZoneForwardEntry_Object((1,3,6,1,4,1,28097,8,1,2,7,1))
configIpZoneForwardEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:configIpZoneForwardEntry.setStatus(_A)
_ConfigIpZoneForwardIndex_Type=Integer32
_ConfigIpZoneForwardIndex_Object=MibTableColumn
configIpZoneForwardIndex=_ConfigIpZoneForwardIndex_Object((1,3,6,1,4,1,28097,8,1,2,7,1,1),_ConfigIpZoneForwardIndex_Type())
configIpZoneForwardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneForwardIndex.setStatus(_A)
_ConfigIpZoneForwardRowStatus_Type=RowStatus
_ConfigIpZoneForwardRowStatus_Object=MibTableColumn
configIpZoneForwardRowStatus=_ConfigIpZoneForwardRowStatus_Object((1,3,6,1,4,1,28097,8,1,2,7,1,2),_ConfigIpZoneForwardRowStatus_Type())
configIpZoneForwardRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpZoneForwardRowStatus.setStatus(_A)
_ConfigIpZoneForwardSrc_Type=OctetString
_ConfigIpZoneForwardSrc_Object=MibTableColumn
configIpZoneForwardSrc=_ConfigIpZoneForwardSrc_Object((1,3,6,1,4,1,28097,8,1,2,7,1,3),_ConfigIpZoneForwardSrc_Type())
configIpZoneForwardSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneForwardSrc.setStatus(_A)
_ConfigIpZoneForwardDst_Type=OctetString
_ConfigIpZoneForwardDst_Object=MibTableColumn
configIpZoneForwardDst=_ConfigIpZoneForwardDst_Object((1,3,6,1,4,1,28097,8,1,2,7,1,4),_ConfigIpZoneForwardDst_Type())
configIpZoneForwardDst.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpZoneForwardDst.setStatus(_A)
_ConfigIpDscpTaggingTable_Object=MibTable
configIpDscpTaggingTable=_ConfigIpDscpTaggingTable_Object((1,3,6,1,4,1,28097,8,1,2,8))
if mibBuilder.loadTexts:configIpDscpTaggingTable.setStatus(_A)
_ConfigIpDscpTaggingEntry_Object=MibTableRow
configIpDscpTaggingEntry=_ConfigIpDscpTaggingEntry_Object((1,3,6,1,4,1,28097,8,1,2,8,1))
configIpDscpTaggingEntry.setIndexNames((0,_E,_AP))
if mibBuilder.loadTexts:configIpDscpTaggingEntry.setStatus(_A)
_ConfigIpDscpTaggingIndex_Type=OctetString
_ConfigIpDscpTaggingIndex_Object=MibTableColumn
configIpDscpTaggingIndex=_ConfigIpDscpTaggingIndex_Object((1,3,6,1,4,1,28097,8,1,2,8,1,1),_ConfigIpDscpTaggingIndex_Type())
configIpDscpTaggingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingIndex.setStatus(_A)
_ConfigIpDscpTaggingRowStatus_Type=RowStatus
_ConfigIpDscpTaggingRowStatus_Object=MibTableColumn
configIpDscpTaggingRowStatus=_ConfigIpDscpTaggingRowStatus_Object((1,3,6,1,4,1,28097,8,1,2,8,1,2),_ConfigIpDscpTaggingRowStatus_Type())
configIpDscpTaggingRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIpDscpTaggingRowStatus.setStatus(_A)
_ConfigIpDscpTaggingFriendlyName_Type=OctetString
_ConfigIpDscpTaggingFriendlyName_Object=MibTableColumn
configIpDscpTaggingFriendlyName=_ConfigIpDscpTaggingFriendlyName_Object((1,3,6,1,4,1,28097,8,1,2,8,1,3),_ConfigIpDscpTaggingFriendlyName_Type())
configIpDscpTaggingFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingFriendlyName.setStatus(_A)
class _ConfigIpDscpTaggingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_t,1),(_i,2),(_j,3),(_k,4)))
_ConfigIpDscpTaggingProtocol_Type.__name__=_D
_ConfigIpDscpTaggingProtocol_Object=MibTableColumn
configIpDscpTaggingProtocol=_ConfigIpDscpTaggingProtocol_Object((1,3,6,1,4,1,28097,8,1,2,8,1,4),_ConfigIpDscpTaggingProtocol_Type())
configIpDscpTaggingProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingProtocol.setStatus(_A)
_ConfigIpDscpTaggingSrcIP_Type=IpAddress
_ConfigIpDscpTaggingSrcIP_Object=MibTableColumn
configIpDscpTaggingSrcIP=_ConfigIpDscpTaggingSrcIP_Object((1,3,6,1,4,1,28097,8,1,2,8,1,5),_ConfigIpDscpTaggingSrcIP_Type())
configIpDscpTaggingSrcIP.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingSrcIP.setStatus(_A)
_ConfigIpDscpTaggingDstIP_Type=IpAddress
_ConfigIpDscpTaggingDstIP_Object=MibTableColumn
configIpDscpTaggingDstIP=_ConfigIpDscpTaggingDstIP_Object((1,3,6,1,4,1,28097,8,1,2,8,1,6),_ConfigIpDscpTaggingDstIP_Type())
configIpDscpTaggingDstIP.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingDstIP.setStatus(_A)
_ConfigIpDscpTaggingSrcPort_Type=OctetString
_ConfigIpDscpTaggingSrcPort_Object=MibTableColumn
configIpDscpTaggingSrcPort=_ConfigIpDscpTaggingSrcPort_Object((1,3,6,1,4,1,28097,8,1,2,8,1,7),_ConfigIpDscpTaggingSrcPort_Type())
configIpDscpTaggingSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingSrcPort.setStatus(_A)
_ConfigIpDscpTaggingDstPort_Type=OctetString
_ConfigIpDscpTaggingDstPort_Object=MibTableColumn
configIpDscpTaggingDstPort=_ConfigIpDscpTaggingDstPort_Object((1,3,6,1,4,1,28097,8,1,2,8,1,8),_ConfigIpDscpTaggingDstPort_Type())
configIpDscpTaggingDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingDstPort.setStatus(_A)
_ConfigIpDscpTaggingDscpValue_Type=Integer32
_ConfigIpDscpTaggingDscpValue_Object=MibTableColumn
configIpDscpTaggingDscpValue=_ConfigIpDscpTaggingDscpValue_Object((1,3,6,1,4,1,28097,8,1,2,8,1,9),_ConfigIpDscpTaggingDscpValue_Type())
configIpDscpTaggingDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpDscpTaggingDscpValue.setStatus(_A)
_Netphy_ObjectIdentity=ObjectIdentity
netphy=_Netphy_ObjectIdentity((1,3,6,1,4,1,28097,8,2))
_ConfigPhyWifiTable_Object=MibTable
configPhyWifiTable=_ConfigPhyWifiTable_Object((1,3,6,1,4,1,28097,8,2,1))
if mibBuilder.loadTexts:configPhyWifiTable.setStatus(_A)
_ConfigPhyWifiEntry_Object=MibTableRow
configPhyWifiEntry=_ConfigPhyWifiEntry_Object((1,3,6,1,4,1,28097,8,2,1,1))
configPhyWifiEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:configPhyWifiEntry.setStatus(_A)
_ConfigPhyWifiName_Type=NetifName
_ConfigPhyWifiName_Object=MibTableColumn
configPhyWifiName=_ConfigPhyWifiName_Object((1,3,6,1,4,1,28097,8,2,1,1,2),_ConfigPhyWifiName_Type())
configPhyWifiName.setMaxAccess(_C)
if mibBuilder.loadTexts:configPhyWifiName.setStatus(_A)
_ConfigPhyWifiLabel_Type=DisplayString
_ConfigPhyWifiLabel_Object=MibTableColumn
configPhyWifiLabel=_ConfigPhyWifiLabel_Object((1,3,6,1,4,1,28097,8,2,1,1,3),_ConfigPhyWifiLabel_Type())
configPhyWifiLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:configPhyWifiLabel.setStatus(_A)
_ConfigPhyWifiMAC_Type=PhysAddress
_ConfigPhyWifiMAC_Object=MibTableColumn
configPhyWifiMAC=_ConfigPhyWifiMAC_Object((1,3,6,1,4,1,28097,8,2,1,1,4),_ConfigPhyWifiMAC_Type())
configPhyWifiMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:configPhyWifiMAC.setStatus(_A)
_ConfigPhyWifiEnable_Type=DisableEnable
_ConfigPhyWifiEnable_Object=MibTableColumn
configPhyWifiEnable=_ConfigPhyWifiEnable_Object((1,3,6,1,4,1,28097,8,2,1,1,5),_ConfigPhyWifiEnable_Type())
configPhyWifiEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiEnable.setStatus(_A)
_ConfigPhyWifiMode_Type=WifiFlavor
_ConfigPhyWifiMode_Object=MibTableColumn
configPhyWifiMode=_ConfigPhyWifiMode_Object((1,3,6,1,4,1,28097,8,2,1,1,6),_ConfigPhyWifiMode_Type())
configPhyWifiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiMode.setStatus(_A)
class _ConfigPhyWifiCountry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_ConfigPhyWifiCountry_Type.__name__=_F
_ConfigPhyWifiCountry_Object=MibTableColumn
configPhyWifiCountry=_ConfigPhyWifiCountry_Object((1,3,6,1,4,1,28097,8,2,1,1,7),_ConfigPhyWifiCountry_Type())
configPhyWifiCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiCountry.setStatus(_A)
_ConfigPhyWifiChannel_Type=Integer32
_ConfigPhyWifiChannel_Object=MibTableColumn
configPhyWifiChannel=_ConfigPhyWifiChannel_Object((1,3,6,1,4,1,28097,8,2,1,1,8),_ConfigPhyWifiChannel_Type())
configPhyWifiChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiChannel.setStatus(_A)
class _ConfigPhyWifiHTMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ht20',1),('ht40-below',2),('ht40-above',3),('ht40-auto',4),('vht20',5),('vht40',6),('vht80',7)))
_ConfigPhyWifiHTMode_Type.__name__=_D
_ConfigPhyWifiHTMode_Object=MibTableColumn
configPhyWifiHTMode=_ConfigPhyWifiHTMode_Object((1,3,6,1,4,1,28097,8,2,1,1,9),_ConfigPhyWifiHTMode_Type())
configPhyWifiHTMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiHTMode.setStatus(_A)
_ConfigPhyWifiTxPowerDBM_Type=Integer32
_ConfigPhyWifiTxPowerDBM_Object=MibTableColumn
configPhyWifiTxPowerDBM=_ConfigPhyWifiTxPowerDBM_Object((1,3,6,1,4,1,28097,8,2,1,1,10),_ConfigPhyWifiTxPowerDBM_Type())
configPhyWifiTxPowerDBM.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiTxPowerDBM.setStatus(_A)
_ConfigPhyWifiDistance_Type=Integer32
_ConfigPhyWifiDistance_Object=MibTableColumn
configPhyWifiDistance=_ConfigPhyWifiDistance_Object((1,3,6,1,4,1,28097,8,2,1,1,11),_ConfigPhyWifiDistance_Type())
configPhyWifiDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiDistance.setStatus(_A)
class _ConfigPhyWifiClusterMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ConfigPhyWifiClusterMode_Type.__name__=_F
_ConfigPhyWifiClusterMode_Object=MibTableColumn
configPhyWifiClusterMode=_ConfigPhyWifiClusterMode_Object((1,3,6,1,4,1,28097,8,2,1,1,12),_ConfigPhyWifiClusterMode_Type())
configPhyWifiClusterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiClusterMode.setStatus(_A)
class _ConfigPhyWifiClusterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ConfigPhyWifiClusterList_Type.__name__=_F
_ConfigPhyWifiClusterList_Object=MibTableColumn
configPhyWifiClusterList=_ConfigPhyWifiClusterList_Object((1,3,6,1,4,1,28097,8,2,1,1,13),_ConfigPhyWifiClusterList_Type())
configPhyWifiClusterList.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiClusterList.setStatus(_A)
class _ConfigPhyWifiClusterArgs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ConfigPhyWifiClusterArgs_Type.__name__=_F
_ConfigPhyWifiClusterArgs_Object=MibTableColumn
configPhyWifiClusterArgs=_ConfigPhyWifiClusterArgs_Object((1,3,6,1,4,1,28097,8,2,1,1,14),_ConfigPhyWifiClusterArgs_Type())
configPhyWifiClusterArgs.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiClusterArgs.setStatus(_A)
class _ConfigPhyWifiAntennaPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,7)));namedValues=NamedValues(*(('port1',1),('ports12',3),('ports123',7)))
_ConfigPhyWifiAntennaPorts_Type.__name__=_D
_ConfigPhyWifiAntennaPorts_Object=MibTableColumn
configPhyWifiAntennaPorts=_ConfigPhyWifiAntennaPorts_Object((1,3,6,1,4,1,28097,8,2,1,1,15),_ConfigPhyWifiAntennaPorts_Type())
configPhyWifiAntennaPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiAntennaPorts.setStatus(_A)
class _ConfigPhyWifiABGBasicRates_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,66))
_ConfigPhyWifiABGBasicRates_Type.__name__=_F
_ConfigPhyWifiABGBasicRates_Object=MibTableColumn
configPhyWifiABGBasicRates=_ConfigPhyWifiABGBasicRates_Object((1,3,6,1,4,1,28097,8,2,1,1,16),_ConfigPhyWifiABGBasicRates_Type())
configPhyWifiABGBasicRates.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiABGBasicRates.setStatus(_A)
class _ConfigPhyWifiABGSupportedRates_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,66))
_ConfigPhyWifiABGSupportedRates_Type.__name__=_F
_ConfigPhyWifiABGSupportedRates_Object=MibTableColumn
configPhyWifiABGSupportedRates=_ConfigPhyWifiABGSupportedRates_Object((1,3,6,1,4,1,28097,8,2,1,1,17),_ConfigPhyWifiABGSupportedRates_Type())
configPhyWifiABGSupportedRates.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiABGSupportedRates.setStatus(_A)
_ConfigPhyWifiChannelList_Type=OctetString
_ConfigPhyWifiChannelList_Object=MibTableColumn
configPhyWifiChannelList=_ConfigPhyWifiChannelList_Object((1,3,6,1,4,1,28097,8,2,1,1,18),_ConfigPhyWifiChannelList_Type())
configPhyWifiChannelList.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiChannelList.setStatus(_A)
_ConfigPhyWifiWids_Type=Integer32
_ConfigPhyWifiWids_Object=MibTableColumn
configPhyWifiWids=_ConfigPhyWifiWids_Object((1,3,6,1,4,1,28097,8,2,1,1,19),_ConfigPhyWifiWids_Type())
configPhyWifiWids.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyWifiWids.setStatus(_A)
_ConfigPhyCellTable_Object=MibTable
configPhyCellTable=_ConfigPhyCellTable_Object((1,3,6,1,4,1,28097,8,2,2))
if mibBuilder.loadTexts:configPhyCellTable.setStatus(_A)
_ConfigPhyCellEntry_Object=MibTableRow
configPhyCellEntry=_ConfigPhyCellEntry_Object((1,3,6,1,4,1,28097,8,2,2,1))
configPhyCellEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:configPhyCellEntry.setStatus(_A)
_ConfigPhyCellName_Type=NetifName
_ConfigPhyCellName_Object=MibTableColumn
configPhyCellName=_ConfigPhyCellName_Object((1,3,6,1,4,1,28097,8,2,2,1,1),_ConfigPhyCellName_Type())
configPhyCellName.setMaxAccess(_C)
if mibBuilder.loadTexts:configPhyCellName.setStatus(_A)
_ConfigPhyCellLabel_Type=DisplayString
_ConfigPhyCellLabel_Object=MibTableColumn
configPhyCellLabel=_ConfigPhyCellLabel_Object((1,3,6,1,4,1,28097,8,2,2,1,2),_ConfigPhyCellLabel_Type())
configPhyCellLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:configPhyCellLabel.setStatus(_A)
_ConfigPhyCellDisableAtBoot_Type=DisableEnable
_ConfigPhyCellDisableAtBoot_Object=MibTableColumn
configPhyCellDisableAtBoot=_ConfigPhyCellDisableAtBoot_Object((1,3,6,1,4,1,28097,8,2,2,1,3),_ConfigPhyCellDisableAtBoot_Type())
configPhyCellDisableAtBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellDisableAtBoot.setStatus(_A)
_ConfigPhyCellLogAT_Type=DisableEnable
_ConfigPhyCellLogAT_Object=MibTableColumn
configPhyCellLogAT=_ConfigPhyCellLogAT_Object((1,3,6,1,4,1,28097,8,2,2,1,4),_ConfigPhyCellLogAT_Type())
configPhyCellLogAT.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellLogAT.setStatus(_A)
class _ConfigPhyCellSIM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sim1',1),('sim2',2)))
_ConfigPhyCellSIM_Type.__name__=_D
_ConfigPhyCellSIM_Object=MibTableColumn
configPhyCellSIM=_ConfigPhyCellSIM_Object((1,3,6,1,4,1,28097,8,2,2,1,5),_ConfigPhyCellSIM_Type())
configPhyCellSIM.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSIM.setStatus(_A)
_ConfigPhyCellSetPIN_Type=DisplayString
_ConfigPhyCellSetPIN_Object=MibTableColumn
configPhyCellSetPIN=_ConfigPhyCellSetPIN_Object((1,3,6,1,4,1,28097,8,2,2,1,6),_ConfigPhyCellSetPIN_Type())
configPhyCellSetPIN.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSetPIN.setStatus(_A)
_ConfigPhyCellSetPUK_Type=DisplayString
_ConfigPhyCellSetPUK_Object=MibTableColumn
configPhyCellSetPUK=_ConfigPhyCellSetPUK_Object((1,3,6,1,4,1,28097,8,2,2,1,7),_ConfigPhyCellSetPUK_Type())
configPhyCellSetPUK.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSetPUK.setStatus(_A)
_ConfigPhyCellSetPINStatus_Type=AsyncSetStatus
_ConfigPhyCellSetPINStatus_Object=MibTableColumn
configPhyCellSetPINStatus=_ConfigPhyCellSetPINStatus_Object((1,3,6,1,4,1,28097,8,2,2,1,8),_ConfigPhyCellSetPINStatus_Type())
configPhyCellSetPINStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:configPhyCellSetPINStatus.setStatus(_A)
_ConfigPhyCellSim1Pin_Type=DisplayString
_ConfigPhyCellSim1Pin_Object=MibTableColumn
configPhyCellSim1Pin=_ConfigPhyCellSim1Pin_Object((1,3,6,1,4,1,28097,8,2,2,1,9),_ConfigPhyCellSim1Pin_Type())
configPhyCellSim1Pin.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim1Pin.setStatus(_A)
_ConfigPhyCellSim1Apn_Type=DisplayString
_ConfigPhyCellSim1Apn_Object=MibTableColumn
configPhyCellSim1Apn=_ConfigPhyCellSim1Apn_Object((1,3,6,1,4,1,28097,8,2,2,1,10),_ConfigPhyCellSim1Apn_Type())
configPhyCellSim1Apn.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim1Apn.setStatus(_A)
_ConfigPhyCellSim1Authentication_Type=CellSecurityProtocol
_ConfigPhyCellSim1Authentication_Object=MibTableColumn
configPhyCellSim1Authentication=_ConfigPhyCellSim1Authentication_Object((1,3,6,1,4,1,28097,8,2,2,1,11),_ConfigPhyCellSim1Authentication_Type())
configPhyCellSim1Authentication.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim1Authentication.setStatus(_A)
_ConfigPhyCellSim1Identity_Type=DisplayString
_ConfigPhyCellSim1Identity_Object=MibTableColumn
configPhyCellSim1Identity=_ConfigPhyCellSim1Identity_Object((1,3,6,1,4,1,28097,8,2,2,1,12),_ConfigPhyCellSim1Identity_Type())
configPhyCellSim1Identity.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim1Identity.setStatus(_A)
_ConfigPhyCellSim1Password_Type=DisplayString
_ConfigPhyCellSim1Password_Object=MibTableColumn
configPhyCellSim1Password=_ConfigPhyCellSim1Password_Object((1,3,6,1,4,1,28097,8,2,2,1,13),_ConfigPhyCellSim1Password_Type())
configPhyCellSim1Password.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim1Password.setStatus(_A)
_ConfigPhyCellSim2Pin_Type=DisplayString
_ConfigPhyCellSim2Pin_Object=MibTableColumn
configPhyCellSim2Pin=_ConfigPhyCellSim2Pin_Object((1,3,6,1,4,1,28097,8,2,2,1,14),_ConfigPhyCellSim2Pin_Type())
configPhyCellSim2Pin.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim2Pin.setStatus(_A)
_ConfigPhyCellSim2Apn_Type=DisplayString
_ConfigPhyCellSim2Apn_Object=MibTableColumn
configPhyCellSim2Apn=_ConfigPhyCellSim2Apn_Object((1,3,6,1,4,1,28097,8,2,2,1,15),_ConfigPhyCellSim2Apn_Type())
configPhyCellSim2Apn.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim2Apn.setStatus(_A)
_ConfigPhyCellSim2Authentication_Type=CellSecurityProtocol
_ConfigPhyCellSim2Authentication_Object=MibTableColumn
configPhyCellSim2Authentication=_ConfigPhyCellSim2Authentication_Object((1,3,6,1,4,1,28097,8,2,2,1,16),_ConfigPhyCellSim2Authentication_Type())
configPhyCellSim2Authentication.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim2Authentication.setStatus(_A)
_ConfigPhyCellSim2Identity_Type=DisplayString
_ConfigPhyCellSim2Identity_Object=MibTableColumn
configPhyCellSim2Identity=_ConfigPhyCellSim2Identity_Object((1,3,6,1,4,1,28097,8,2,2,1,17),_ConfigPhyCellSim2Identity_Type())
configPhyCellSim2Identity.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim2Identity.setStatus(_A)
_ConfigPhyCellSim2Password_Type=DisplayString
_ConfigPhyCellSim2Password_Object=MibTableColumn
configPhyCellSim2Password=_ConfigPhyCellSim2Password_Object((1,3,6,1,4,1,28097,8,2,2,1,18),_ConfigPhyCellSim2Password_Type())
configPhyCellSim2Password.setMaxAccess(_B)
if mibBuilder.loadTexts:configPhyCellSim2Password.setStatus(_A)
_Netif_ObjectIdentity=ObjectIdentity
netif=_Netif_ObjectIdentity((1,3,6,1,4,1,28097,8,3))
_Netdetails_ObjectIdentity=ObjectIdentity
netdetails=_Netdetails_ObjectIdentity((1,3,6,1,4,1,28097,8,3,1))
_ConfigRadiusTable_Object=MibTable
configRadiusTable=_ConfigRadiusTable_Object((1,3,6,1,4,1,28097,8,3,1,1))
if mibBuilder.loadTexts:configRadiusTable.setStatus(_A)
_ConfigRadiusEntry_Object=MibTableRow
configRadiusEntry=_ConfigRadiusEntry_Object((1,3,6,1,4,1,28097,8,3,1,1,1))
configRadiusEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:configRadiusEntry.setStatus(_A)
_ConfigRadiusIndex_Type=Integer32
_ConfigRadiusIndex_Object=MibTableColumn
configRadiusIndex=_ConfigRadiusIndex_Object((1,3,6,1,4,1,28097,8,3,1,1,1,1),_ConfigRadiusIndex_Type())
configRadiusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:configRadiusIndex.setStatus(_A)
_ConfigRadiusRowStatus_Type=RowStatus
_ConfigRadiusRowStatus_Object=MibTableColumn
configRadiusRowStatus=_ConfigRadiusRowStatus_Object((1,3,6,1,4,1,28097,8,3,1,1,1,2),_ConfigRadiusRowStatus_Type())
configRadiusRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configRadiusRowStatus.setStatus(_A)
_ConfigRadiusIpAddress_Type=OctetString
_ConfigRadiusIpAddress_Object=MibTableColumn
configRadiusIpAddress=_ConfigRadiusIpAddress_Object((1,3,6,1,4,1,28097,8,3,1,1,1,3),_ConfigRadiusIpAddress_Type())
configRadiusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configRadiusIpAddress.setStatus(_A)
_ConfigRadiusPort_Type=Integer32
_ConfigRadiusPort_Object=MibTableColumn
configRadiusPort=_ConfigRadiusPort_Object((1,3,6,1,4,1,28097,8,3,1,1,1,4),_ConfigRadiusPort_Type())
configRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configRadiusPort.setStatus(_A)
_ConfigRadiusSecret_Type=OctetString
_ConfigRadiusSecret_Object=MibTableColumn
configRadiusSecret=_ConfigRadiusSecret_Object((1,3,6,1,4,1,28097,8,3,1,1,1,5),_ConfigRadiusSecret_Type())
configRadiusSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:configRadiusSecret.setStatus(_A)
class _ConfigDetailsNasId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_ConfigDetailsNasId_Type.__name__=_F
_ConfigDetailsNasId_Object=MibScalar
configDetailsNasId=_ConfigDetailsNasId_Object((1,3,6,1,4,1,28097,8,3,1,2),_ConfigDetailsNasId_Type())
configDetailsNasId.setMaxAccess(_B)
if mibBuilder.loadTexts:configDetailsNasId.setStatus(_A)
_ConfigFilterGroupTable_Object=MibTable
configFilterGroupTable=_ConfigFilterGroupTable_Object((1,3,6,1,4,1,28097,8,3,1,3))
if mibBuilder.loadTexts:configFilterGroupTable.setStatus(_A)
_ConfigFilterGroupEntry_Object=MibTableRow
configFilterGroupEntry=_ConfigFilterGroupEntry_Object((1,3,6,1,4,1,28097,8,3,1,3,1))
configFilterGroupEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:configFilterGroupEntry.setStatus(_A)
_ConfigFilterGroupIndex_Type=OctetString
_ConfigFilterGroupIndex_Object=MibTableColumn
configFilterGroupIndex=_ConfigFilterGroupIndex_Object((1,3,6,1,4,1,28097,8,3,1,3,1,1),_ConfigFilterGroupIndex_Type())
configFilterGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupIndex.setStatus(_A)
_ConfigFilterGroupRowStatus_Type=RowStatus
_ConfigFilterGroupRowStatus_Object=MibTableColumn
configFilterGroupRowStatus=_ConfigFilterGroupRowStatus_Object((1,3,6,1,4,1,28097,8,3,1,3,1,2),_ConfigFilterGroupRowStatus_Type())
configFilterGroupRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configFilterGroupRowStatus.setStatus(_A)
_ConfigFilterGroupFriendlyName_Type=OctetString
_ConfigFilterGroupFriendlyName_Object=MibTableColumn
configFilterGroupFriendlyName=_ConfigFilterGroupFriendlyName_Object((1,3,6,1,4,1,28097,8,3,1,3,1,3),_ConfigFilterGroupFriendlyName_Type())
configFilterGroupFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupFriendlyName.setStatus(_A)
_ConfigFilterGroupRuleTable_Object=MibTable
configFilterGroupRuleTable=_ConfigFilterGroupRuleTable_Object((1,3,6,1,4,1,28097,8,3,1,4))
if mibBuilder.loadTexts:configFilterGroupRuleTable.setStatus(_A)
_ConfigFilterGroupRuleEntry_Object=MibTableRow
configFilterGroupRuleEntry=_ConfigFilterGroupRuleEntry_Object((1,3,6,1,4,1,28097,8,3,1,4,1))
configFilterGroupRuleEntry.setIndexNames((0,_E,_AU))
if mibBuilder.loadTexts:configFilterGroupRuleEntry.setStatus(_A)
_ConfigFilterGroupRuleIndex_Type=OctetString
_ConfigFilterGroupRuleIndex_Object=MibTableColumn
configFilterGroupRuleIndex=_ConfigFilterGroupRuleIndex_Object((1,3,6,1,4,1,28097,8,3,1,4,1,1),_ConfigFilterGroupRuleIndex_Type())
configFilterGroupRuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleIndex.setStatus(_A)
_ConfigFilterGroupRuleRowStatus_Type=RowStatus
_ConfigFilterGroupRuleRowStatus_Object=MibTableColumn
configFilterGroupRuleRowStatus=_ConfigFilterGroupRuleRowStatus_Object((1,3,6,1,4,1,28097,8,3,1,4,1,2),_ConfigFilterGroupRuleRowStatus_Type())
configFilterGroupRuleRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configFilterGroupRuleRowStatus.setStatus(_A)
_ConfigFilterGroupGroupIndex_Type=OctetString
_ConfigFilterGroupGroupIndex_Object=MibTableColumn
configFilterGroupGroupIndex=_ConfigFilterGroupGroupIndex_Object((1,3,6,1,4,1,28097,8,3,1,4,1,3),_ConfigFilterGroupGroupIndex_Type())
configFilterGroupGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupGroupIndex.setStatus(_A)
class _ConfigFilterGroupRuleMACFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,1,2,3,4)));namedValues=NamedValues(*((_W,-255),(_u,1),('unicast',2),('broadcast',3),('multicast',4)))
_ConfigFilterGroupRuleMACFrameType_Type.__name__=_D
_ConfigFilterGroupRuleMACFrameType_Object=MibTableColumn
configFilterGroupRuleMACFrameType=_ConfigFilterGroupRuleMACFrameType_Object((1,3,6,1,4,1,28097,8,3,1,4,1,4),_ConfigFilterGroupRuleMACFrameType_Type())
configFilterGroupRuleMACFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleMACFrameType.setStatus(_A)
class _ConfigFilterGroupRuleCheckMAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,1,2)));namedValues=NamedValues(*((_W,-255),(_v,1),(_w,2)))
_ConfigFilterGroupRuleCheckMAC_Type.__name__=_D
_ConfigFilterGroupRuleCheckMAC_Object=MibTableColumn
configFilterGroupRuleCheckMAC=_ConfigFilterGroupRuleCheckMAC_Object((1,3,6,1,4,1,28097,8,3,1,4,1,5),_ConfigFilterGroupRuleCheckMAC_Type())
configFilterGroupRuleCheckMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleCheckMAC.setStatus(_A)
class _ConfigFilterGroupRuleNetworkProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,-3,-2,-1)));namedValues=NamedValues(*((_W,-255),('arp',-3),('ip',-2),(_u,-1)))
_ConfigFilterGroupRuleNetworkProtocol_Type.__name__=_D
_ConfigFilterGroupRuleNetworkProtocol_Object=MibTableColumn
configFilterGroupRuleNetworkProtocol=_ConfigFilterGroupRuleNetworkProtocol_Object((1,3,6,1,4,1,28097,8,3,1,4,1,6),_ConfigFilterGroupRuleNetworkProtocol_Type())
configFilterGroupRuleNetworkProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleNetworkProtocol.setStatus(_A)
_ConfigFilterGroupRuleIpAddress_Type=IpAddress
_ConfigFilterGroupRuleIpAddress_Object=MibTableColumn
configFilterGroupRuleIpAddress=_ConfigFilterGroupRuleIpAddress_Object((1,3,6,1,4,1,28097,8,3,1,4,1,7),_ConfigFilterGroupRuleIpAddress_Type())
configFilterGroupRuleIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleIpAddress.setStatus(_A)
_ConfigFilterGroupRuleNetmask_Type=IpAddress
_ConfigFilterGroupRuleNetmask_Object=MibTableColumn
configFilterGroupRuleNetmask=_ConfigFilterGroupRuleNetmask_Object((1,3,6,1,4,1,28097,8,3,1,4,1,8),_ConfigFilterGroupRuleNetmask_Type())
configFilterGroupRuleNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleNetmask.setStatus(_A)
class _ConfigFilterGroupRuleCheckIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,1,2)));namedValues=NamedValues(*((_W,-255),(_v,1),(_w,2)))
_ConfigFilterGroupRuleCheckIP_Type.__name__=_D
_ConfigFilterGroupRuleCheckIP_Object=MibTableColumn
configFilterGroupRuleCheckIP=_ConfigFilterGroupRuleCheckIP_Object((1,3,6,1,4,1,28097,8,3,1,4,1,9),_ConfigFilterGroupRuleCheckIP_Type())
configFilterGroupRuleCheckIP.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleCheckIP.setStatus(_A)
class _ConfigFilterGroupRuleTransportProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,1,2,3,4)));namedValues=NamedValues(*((_W,-255),(_u,1),(_j,2),(_i,3),(_k,4)))
_ConfigFilterGroupRuleTransportProtocol_Type.__name__=_D
_ConfigFilterGroupRuleTransportProtocol_Object=MibTableColumn
configFilterGroupRuleTransportProtocol=_ConfigFilterGroupRuleTransportProtocol_Object((1,3,6,1,4,1,28097,8,3,1,4,1,10),_ConfigFilterGroupRuleTransportProtocol_Type())
configFilterGroupRuleTransportProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleTransportProtocol.setStatus(_A)
class _ConfigFilterGroupRuleFirstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigFilterGroupRuleFirstPort_Type.__name__=_D
_ConfigFilterGroupRuleFirstPort_Object=MibTableColumn
configFilterGroupRuleFirstPort=_ConfigFilterGroupRuleFirstPort_Object((1,3,6,1,4,1,28097,8,3,1,4,1,11),_ConfigFilterGroupRuleFirstPort_Type())
configFilterGroupRuleFirstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleFirstPort.setStatus(_A)
class _ConfigFilterGroupRuleLastPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigFilterGroupRuleLastPort_Type.__name__=_D
_ConfigFilterGroupRuleLastPort_Object=MibTableColumn
configFilterGroupRuleLastPort=_ConfigFilterGroupRuleLastPort_Object((1,3,6,1,4,1,28097,8,3,1,4,1,12),_ConfigFilterGroupRuleLastPort_Type())
configFilterGroupRuleLastPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleLastPort.setStatus(_A)
class _ConfigFilterGroupRuleCheckPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,1,2)));namedValues=NamedValues(*((_W,-255),(_v,1),(_w,2)))
_ConfigFilterGroupRuleCheckPort_Type.__name__=_D
_ConfigFilterGroupRuleCheckPort_Object=MibTableColumn
configFilterGroupRuleCheckPort=_ConfigFilterGroupRuleCheckPort_Object((1,3,6,1,4,1,28097,8,3,1,4,1,13),_ConfigFilterGroupRuleCheckPort_Type())
configFilterGroupRuleCheckPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configFilterGroupRuleCheckPort.setStatus(_A)
_ConfigInterfaceTable_Object=MibTable
configInterfaceTable=_ConfigInterfaceTable_Object((1,3,6,1,4,1,28097,8,3,2))
if mibBuilder.loadTexts:configInterfaceTable.setStatus(_A)
_ConfigInterfaceEntry_Object=MibTableRow
configInterfaceEntry=_ConfigInterfaceEntry_Object((1,3,6,1,4,1,28097,8,3,2,1))
configInterfaceEntry.setIndexNames((0,_E,_AV))
if mibBuilder.loadTexts:configInterfaceEntry.setStatus(_A)
_ConfigInterfaceName_Type=NetifName
_ConfigInterfaceName_Object=MibTableColumn
configInterfaceName=_ConfigInterfaceName_Object((1,3,6,1,4,1,28097,8,3,2,1,1),_ConfigInterfaceName_Type())
configInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:configInterfaceName.setStatus(_A)
_ConfigInterfaceRowStatus_Type=RowStatus
_ConfigInterfaceRowStatus_Object=MibTableColumn
configInterfaceRowStatus=_ConfigInterfaceRowStatus_Object((1,3,6,1,4,1,28097,8,3,2,1,2),_ConfigInterfaceRowStatus_Type())
configInterfaceRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configInterfaceRowStatus.setStatus(_A)
class _ConfigInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('ethernet',1),('mac-bridge',2),('wifi-sta',3),('wifi-ap',4),('wifi-11s',5),('wifi-rept',6),('wifi-adhoc',7),('vlan8021q',8),('l2tunnel-gre',9),('wifi-srcc',10),('cellular',11),('mac-bond',12),('wifi-monitor',13)))
_ConfigInterfaceType_Type.__name__=_D
_ConfigInterfaceType_Object=MibTableColumn
configInterfaceType=_ConfigInterfaceType_Object((1,3,6,1,4,1,28097,8,3,2,1,3),_ConfigInterfaceType_Type())
configInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:configInterfaceType.setStatus(_A)
_ConfigInterfaceDepends_Type=NetifName
_ConfigInterfaceDepends_Object=MibTableColumn
configInterfaceDepends=_ConfigInterfaceDepends_Object((1,3,6,1,4,1,28097,8,3,2,1,4),_ConfigInterfaceDepends_Type())
configInterfaceDepends.setMaxAccess(_B)
if mibBuilder.loadTexts:configInterfaceDepends.setStatus(_A)
_ConfigInterfaceOutputFilterGroup_Type=OctetString
_ConfigInterfaceOutputFilterGroup_Object=MibTableColumn
configInterfaceOutputFilterGroup=_ConfigInterfaceOutputFilterGroup_Object((1,3,6,1,4,1,28097,8,3,2,1,5),_ConfigInterfaceOutputFilterGroup_Type())
configInterfaceOutputFilterGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:configInterfaceOutputFilterGroup.setStatus(_A)
class _ConfigInterfaceFilterGroupDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('in',1),('out',2),('inout',3)))
_ConfigInterfaceFilterGroupDir_Type.__name__=_D
_ConfigInterfaceFilterGroupDir_Object=MibTableColumn
configInterfaceFilterGroupDir=_ConfigInterfaceFilterGroupDir_Object((1,3,6,1,4,1,28097,8,3,2,1,6),_ConfigInterfaceFilterGroupDir_Type())
configInterfaceFilterGroupDir.setMaxAccess(_B)
if mibBuilder.loadTexts:configInterfaceFilterGroupDir.setStatus(_K)
_ConfigInterfaceInputFilterGroup_Type=OctetString
_ConfigInterfaceInputFilterGroup_Object=MibTableColumn
configInterfaceInputFilterGroup=_ConfigInterfaceInputFilterGroup_Object((1,3,6,1,4,1,28097,8,3,2,1,7),_ConfigInterfaceInputFilterGroup_Type())
configInterfaceInputFilterGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:configInterfaceInputFilterGroup.setStatus(_A)
_ConfigIfStaTable_Object=MibTable
configIfStaTable=_ConfigIfStaTable_Object((1,3,6,1,4,1,28097,8,3,3))
if mibBuilder.loadTexts:configIfStaTable.setStatus(_A)
_ConfigIfStaEntry_Object=MibTableRow
configIfStaEntry=_ConfigIfStaEntry_Object((1,3,6,1,4,1,28097,8,3,3,1))
configIfStaEntry.setIndexNames((0,_E,_AW))
if mibBuilder.loadTexts:configIfStaEntry.setStatus(_A)
_ConfigIfStaName_Type=NetifName
_ConfigIfStaName_Object=MibTableColumn
configIfStaName=_ConfigIfStaName_Object((1,3,6,1,4,1,28097,8,3,3,1,1),_ConfigIfStaName_Type())
configIfStaName.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfStaName.setStatus(_A)
_ConfigIfStaRowStatus_Type=RowStatus
_ConfigIfStaRowStatus_Object=MibTableColumn
configIfStaRowStatus=_ConfigIfStaRowStatus_Object((1,3,6,1,4,1,28097,8,3,3,1,2),_ConfigIfStaRowStatus_Type())
configIfStaRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIfStaRowStatus.setStatus(_A)
_ConfigIfStaPhy_Type=NetifName
_ConfigIfStaPhy_Object=MibTableColumn
configIfStaPhy=_ConfigIfStaPhy_Object((1,3,6,1,4,1,28097,8,3,3,1,3),_ConfigIfStaPhy_Type())
configIfStaPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfStaPhy.setStatus(_A)
class _ConfigIfStaSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ConfigIfStaSsid_Type.__name__=_F
_ConfigIfStaSsid_Object=MibTableColumn
configIfStaSsid=_ConfigIfStaSsid_Object((1,3,6,1,4,1,28097,8,3,3,1,4),_ConfigIfStaSsid_Type())
configIfStaSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaSsid.setStatus(_A)
_ConfigIfStaBssid_Type=PhysAddress
_ConfigIfStaBssid_Object=MibTableColumn
configIfStaBssid=_ConfigIfStaBssid_Object((1,3,6,1,4,1,28097,8,3,3,1,5),_ConfigIfStaBssid_Type())
configIfStaBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaBssid.setStatus(_A)
class _ConfigIfStaBridgingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('arpnat',1),('four-addresses',2),('mono-eth-cloning',3),('mono-profinet-clonning',4),('multi-eth-cloning',5)))
_ConfigIfStaBridgingMode_Type.__name__=_D
_ConfigIfStaBridgingMode_Object=MibTableColumn
configIfStaBridgingMode=_ConfigIfStaBridgingMode_Object((1,3,6,1,4,1,28097,8,3,3,1,6),_ConfigIfStaBridgingMode_Type())
configIfStaBridgingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaBridgingMode.setStatus(_A)
_ConfigIfStaScanChannels_Type=OctetString
_ConfigIfStaScanChannels_Object=MibTableColumn
configIfStaScanChannels=_ConfigIfStaScanChannels_Object((1,3,6,1,4,1,28097,8,3,3,1,7),_ConfigIfStaScanChannels_Type())
configIfStaScanChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaScanChannels.setStatus(_A)
_ConfigIfStaScanPassive_Type=DisableEnable
_ConfigIfStaScanPassive_Object=MibTableColumn
configIfStaScanPassive=_ConfigIfStaScanPassive_Object((1,3,6,1,4,1,28097,8,3,3,1,8),_ConfigIfStaScanPassive_Type())
configIfStaScanPassive.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaScanPassive.setStatus(_A)
_ConfigIfStaRoamingEnable_Type=DisableEnable
_ConfigIfStaRoamingEnable_Object=MibTableColumn
configIfStaRoamingEnable=_ConfigIfStaRoamingEnable_Object((1,3,6,1,4,1,28097,8,3,3,1,9),_ConfigIfStaRoamingEnable_Type())
configIfStaRoamingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingEnable.setStatus(_A)
_ConfigIfStaRoamingEnableDBM_Type=Integer32
_ConfigIfStaRoamingEnableDBM_Object=MibTableColumn
configIfStaRoamingEnableDBM=_ConfigIfStaRoamingEnableDBM_Object((1,3,6,1,4,1,28097,8,3,3,1,10),_ConfigIfStaRoamingEnableDBM_Type())
configIfStaRoamingEnableDBM.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingEnableDBM.setStatus(_A)
_ConfigIfStaRoamingRequiredBoost_Type=Integer32
_ConfigIfStaRoamingRequiredBoost_Object=MibTableColumn
configIfStaRoamingRequiredBoost=_ConfigIfStaRoamingRequiredBoost_Object((1,3,6,1,4,1,28097,8,3,3,1,11),_ConfigIfStaRoamingRequiredBoost_Type())
configIfStaRoamingRequiredBoost.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingRequiredBoost.setStatus(_A)
_ConfigIfStaRoamingScanPeriod_Type=Integer32
_ConfigIfStaRoamingScanPeriod_Object=MibTableColumn
configIfStaRoamingScanPeriod=_ConfigIfStaRoamingScanPeriod_Object((1,3,6,1,4,1,28097,8,3,3,1,12),_ConfigIfStaRoamingScanPeriod_Type())
configIfStaRoamingScanPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingScanPeriod.setStatus(_A)
_ConfigIfStaSecurityMode_Type=SecurityModes
_ConfigIfStaSecurityMode_Object=MibTableColumn
configIfStaSecurityMode=_ConfigIfStaSecurityMode_Object((1,3,6,1,4,1,28097,8,3,3,1,13),_ConfigIfStaSecurityMode_Type())
configIfStaSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaSecurityMode.setStatus(_A)
_ConfigIfStaWepKey1_Type=WepKeys
_ConfigIfStaWepKey1_Object=MibTableColumn
configIfStaWepKey1=_ConfigIfStaWepKey1_Object((1,3,6,1,4,1,28097,8,3,3,1,14),_ConfigIfStaWepKey1_Type())
configIfStaWepKey1.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWepKey1.setStatus(_A)
_ConfigIfStaWepKey2_Type=WepKeys
_ConfigIfStaWepKey2_Object=MibTableColumn
configIfStaWepKey2=_ConfigIfStaWepKey2_Object((1,3,6,1,4,1,28097,8,3,3,1,15),_ConfigIfStaWepKey2_Type())
configIfStaWepKey2.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWepKey2.setStatus(_A)
_ConfigIfStaWepKey3_Type=WepKeys
_ConfigIfStaWepKey3_Object=MibTableColumn
configIfStaWepKey3=_ConfigIfStaWepKey3_Object((1,3,6,1,4,1,28097,8,3,3,1,16),_ConfigIfStaWepKey3_Type())
configIfStaWepKey3.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWepKey3.setStatus(_A)
_ConfigIfStaWepKey4_Type=WepKeys
_ConfigIfStaWepKey4_Object=MibTableColumn
configIfStaWepKey4=_ConfigIfStaWepKey4_Object((1,3,6,1,4,1,28097,8,3,3,1,17),_ConfigIfStaWepKey4_Type())
configIfStaWepKey4.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWepKey4.setStatus(_A)
_ConfigIfStaWepKey_Type=Integer32
_ConfigIfStaWepKey_Object=MibTableColumn
configIfStaWepKey=_ConfigIfStaWepKey_Object((1,3,6,1,4,1,28097,8,3,3,1,18),_ConfigIfStaWepKey_Type())
configIfStaWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWepKey.setStatus(_A)
_ConfigIfStaWpaVersion_Type=WpaVersions
_ConfigIfStaWpaVersion_Object=MibTableColumn
configIfStaWpaVersion=_ConfigIfStaWpaVersion_Object((1,3,6,1,4,1,28097,8,3,3,1,19),_ConfigIfStaWpaVersion_Type())
configIfStaWpaVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWpaVersion.setStatus(_A)
_ConfigIfStaWpaCipher_Type=CipherTypes
_ConfigIfStaWpaCipher_Object=MibTableColumn
configIfStaWpaCipher=_ConfigIfStaWpaCipher_Object((1,3,6,1,4,1,28097,8,3,3,1,20),_ConfigIfStaWpaCipher_Type())
configIfStaWpaCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfStaWpaCipher.setStatus(_A)
_ConfigIfStaIdentity_Type=OctetString
_ConfigIfStaIdentity_Object=MibTableColumn
configIfStaIdentity=_ConfigIfStaIdentity_Object((1,3,6,1,4,1,28097,8,3,3,1,21),_ConfigIfStaIdentity_Type())
configIfStaIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaIdentity.setStatus(_A)
_ConfigIfStaKey_Type=OctetString
_ConfigIfStaKey_Object=MibTableColumn
configIfStaKey=_ConfigIfStaKey_Object((1,3,6,1,4,1,28097,8,3,3,1,22),_ConfigIfStaKey_Type())
configIfStaKey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaKey.setStatus(_A)
_ConfigIfStaPrivateKey_Type=OctetString
_ConfigIfStaPrivateKey_Object=MibTableColumn
configIfStaPrivateKey=_ConfigIfStaPrivateKey_Object((1,3,6,1,4,1,28097,8,3,3,1,23),_ConfigIfStaPrivateKey_Type())
configIfStaPrivateKey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaPrivateKey.setStatus(_A)
_ConfigIfStaCACert_Type=OctetString
_ConfigIfStaCACert_Object=MibTableColumn
configIfStaCACert=_ConfigIfStaCACert_Object((1,3,6,1,4,1,28097,8,3,3,1,24),_ConfigIfStaCACert_Type())
configIfStaCACert.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaCACert.setStatus(_A)
class _ConfigIfStaEapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eap-tls',1),('eap-peap',2),('eap-leap',3)))
_ConfigIfStaEapType_Type.__name__=_D
_ConfigIfStaEapType_Object=MibTableColumn
configIfStaEapType=_ConfigIfStaEapType_Object((1,3,6,1,4,1,28097,8,3,3,1,25),_ConfigIfStaEapType_Type())
configIfStaEapType.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaEapType.setStatus(_A)
_ConfigIfStaAuthentication_Type=PeapSecurityProtocol
_ConfigIfStaAuthentication_Object=MibTableColumn
configIfStaAuthentication=_ConfigIfStaAuthentication_Object((1,3,6,1,4,1,28097,8,3,3,1,26),_ConfigIfStaAuthentication_Type())
configIfStaAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaAuthentication.setStatus(_A)
_ConfigIfStaFastBSSTransitionActivated_Type=DisableEnable
_ConfigIfStaFastBSSTransitionActivated_Object=MibTableColumn
configIfStaFastBSSTransitionActivated=_ConfigIfStaFastBSSTransitionActivated_Object((1,3,6,1,4,1,28097,8,3,3,1,27),_ConfigIfStaFastBSSTransitionActivated_Type())
configIfStaFastBSSTransitionActivated.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaFastBSSTransitionActivated.setStatus(_A)
_ConfigIfStaIgnorePreviousScansResults_Type=DisableEnable
_ConfigIfStaIgnorePreviousScansResults_Object=MibTableColumn
configIfStaIgnorePreviousScansResults=_ConfigIfStaIgnorePreviousScansResults_Object((1,3,6,1,4,1,28097,8,3,3,1,28),_ConfigIfStaIgnorePreviousScansResults_Type())
configIfStaIgnorePreviousScansResults.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaIgnorePreviousScansResults.setStatus(_A)
_ConfigIfStaRoamingRssiSmoothingFactor_Type=Integer32
_ConfigIfStaRoamingRssiSmoothingFactor_Object=MibTableColumn
configIfStaRoamingRssiSmoothingFactor=_ConfigIfStaRoamingRssiSmoothingFactor_Object((1,3,6,1,4,1,28097,8,3,3,1,29),_ConfigIfStaRoamingRssiSmoothingFactor_Type())
configIfStaRoamingRssiSmoothingFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingRssiSmoothingFactor.setStatus(_A)
_ConfigIfStaRoamingBeaconTimeout_Type=Integer32
_ConfigIfStaRoamingBeaconTimeout_Object=MibTableColumn
configIfStaRoamingBeaconTimeout=_ConfigIfStaRoamingBeaconTimeout_Object((1,3,6,1,4,1,28097,8,3,3,1,30),_ConfigIfStaRoamingBeaconTimeout_Type())
configIfStaRoamingBeaconTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingBeaconTimeout.setStatus(_A)
_ConfigIfStaWpaKeyCacheLifetime_Type=Integer32
_ConfigIfStaWpaKeyCacheLifetime_Object=MibTableColumn
configIfStaWpaKeyCacheLifetime=_ConfigIfStaWpaKeyCacheLifetime_Object((1,3,6,1,4,1,28097,8,3,3,1,31),_ConfigIfStaWpaKeyCacheLifetime_Type())
configIfStaWpaKeyCacheLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaWpaKeyCacheLifetime.setStatus(_A)
_ConfigIfStaRoamingCurrentApScanThreshold_Type=Integer32
_ConfigIfStaRoamingCurrentApScanThreshold_Object=MibTableColumn
configIfStaRoamingCurrentApScanThreshold=_ConfigIfStaRoamingCurrentApScanThreshold_Object((1,3,6,1,4,1,28097,8,3,3,1,32),_ConfigIfStaRoamingCurrentApScanThreshold_Type())
configIfStaRoamingCurrentApScanThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingCurrentApScanThreshold.setStatus(_A)
_ConfigIfStaRoamingMinimumStaLevel_Type=Integer32
_ConfigIfStaRoamingMinimumStaLevel_Object=MibTableColumn
configIfStaRoamingMinimumStaLevel=_ConfigIfStaRoamingMinimumStaLevel_Object((1,3,6,1,4,1,28097,8,3,3,1,33),_ConfigIfStaRoamingMinimumStaLevel_Type())
configIfStaRoamingMinimumStaLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingMinimumStaLevel.setStatus(_A)
_ConfigIfStaRoamingAboveLevelThreshold_Type=Integer32
_ConfigIfStaRoamingAboveLevelThreshold_Object=MibTableColumn
configIfStaRoamingAboveLevelThreshold=_ConfigIfStaRoamingAboveLevelThreshold_Object((1,3,6,1,4,1,28097,8,3,3,1,34),_ConfigIfStaRoamingAboveLevelThreshold_Type())
configIfStaRoamingAboveLevelThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingAboveLevelThreshold.setStatus(_A)
_ConfigIfStaRoamingMaxSignalLevel_Type=Integer32
_ConfigIfStaRoamingMaxSignalLevel_Object=MibTableColumn
configIfStaRoamingMaxSignalLevel=_ConfigIfStaRoamingMaxSignalLevel_Object((1,3,6,1,4,1,28097,8,3,3,1,35),_ConfigIfStaRoamingMaxSignalLevel_Type())
configIfStaRoamingMaxSignalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingMaxSignalLevel.setStatus(_A)
_ConfigIfStaRoamingMinRoamDelay_Type=Integer32
_ConfigIfStaRoamingMinRoamDelay_Object=MibTableColumn
configIfStaRoamingMinRoamDelay=_ConfigIfStaRoamingMinRoamDelay_Object((1,3,6,1,4,1,28097,8,3,3,1,36),_ConfigIfStaRoamingMinRoamDelay_Type())
configIfStaRoamingMinRoamDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingMinRoamDelay.setStatus(_A)
_ConfigIfStaRoamingNoReturnDelay_Type=Integer32
_ConfigIfStaRoamingNoReturnDelay_Object=MibTableColumn
configIfStaRoamingNoReturnDelay=_ConfigIfStaRoamingNoReturnDelay_Object((1,3,6,1,4,1,28097,8,3,3,1,37),_ConfigIfStaRoamingNoReturnDelay_Type())
configIfStaRoamingNoReturnDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingNoReturnDelay.setStatus(_A)
_ConfigIfStaRoamingThresholdHysteresis_Type=Integer32
_ConfigIfStaRoamingThresholdHysteresis_Object=MibTableColumn
configIfStaRoamingThresholdHysteresis=_ConfigIfStaRoamingThresholdHysteresis_Object((1,3,6,1,4,1,28097,8,3,3,1,38),_ConfigIfStaRoamingThresholdHysteresis_Type())
configIfStaRoamingThresholdHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingThresholdHysteresis.setStatus(_A)
_ConfigIfStaRoamingOffChanMaxDelay_Type=Integer32
_ConfigIfStaRoamingOffChanMaxDelay_Object=MibTableColumn
configIfStaRoamingOffChanMaxDelay=_ConfigIfStaRoamingOffChanMaxDelay_Object((1,3,6,1,4,1,28097,8,3,3,1,39),_ConfigIfStaRoamingOffChanMaxDelay_Type())
configIfStaRoamingOffChanMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingOffChanMaxDelay.setStatus(_A)
_ConfigIfStaRoamingOffChanProbeDelay_Type=Integer32
_ConfigIfStaRoamingOffChanProbeDelay_Object=MibTableColumn
configIfStaRoamingOffChanProbeDelay=_ConfigIfStaRoamingOffChanProbeDelay_Object((1,3,6,1,4,1,28097,8,3,3,1,40),_ConfigIfStaRoamingOffChanProbeDelay_Type())
configIfStaRoamingOffChanProbeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingOffChanProbeDelay.setStatus(_A)
_ConfigIfStaRoamingPerChanProbeDelay_Type=Integer32
_ConfigIfStaRoamingPerChanProbeDelay_Object=MibTableColumn
configIfStaRoamingPerChanProbeDelay=_ConfigIfStaRoamingPerChanProbeDelay_Object((1,3,6,1,4,1,28097,8,3,3,1,41),_ConfigIfStaRoamingPerChanProbeDelay_Type())
configIfStaRoamingPerChanProbeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaRoamingPerChanProbeDelay.setStatus(_A)
_ConfigIfStaUserCert_Type=OctetString
_ConfigIfStaUserCert_Object=MibTableColumn
configIfStaUserCert=_ConfigIfStaUserCert_Object((1,3,6,1,4,1,28097,8,3,3,1,42),_ConfigIfStaUserCert_Type())
configIfStaUserCert.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaUserCert.setStatus(_A)
_ConfigIfStaDeauthBeforeRoamingtoNextAP_Type=DisableEnable
_ConfigIfStaDeauthBeforeRoamingtoNextAP_Object=MibTableColumn
configIfStaDeauthBeforeRoamingtoNextAP=_ConfigIfStaDeauthBeforeRoamingtoNextAP_Object((1,3,6,1,4,1,28097,8,3,3,1,43),_ConfigIfStaDeauthBeforeRoamingtoNextAP_Type())
configIfStaDeauthBeforeRoamingtoNextAP.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfStaDeauthBeforeRoamingtoNextAP.setStatus(_A)
_ConfigIfAPTable_Object=MibTable
configIfAPTable=_ConfigIfAPTable_Object((1,3,6,1,4,1,28097,8,3,4))
if mibBuilder.loadTexts:configIfAPTable.setStatus(_A)
_ConfigIfAPEntry_Object=MibTableRow
configIfAPEntry=_ConfigIfAPEntry_Object((1,3,6,1,4,1,28097,8,3,4,1))
configIfAPEntry.setIndexNames((0,_E,_AX))
if mibBuilder.loadTexts:configIfAPEntry.setStatus(_A)
_ConfigIfAPName_Type=NetifName
_ConfigIfAPName_Object=MibTableColumn
configIfAPName=_ConfigIfAPName_Object((1,3,6,1,4,1,28097,8,3,4,1,1),_ConfigIfAPName_Type())
configIfAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfAPName.setStatus(_A)
_ConfigIfAPRowStatus_Type=RowStatus
_ConfigIfAPRowStatus_Object=MibTableColumn
configIfAPRowStatus=_ConfigIfAPRowStatus_Object((1,3,6,1,4,1,28097,8,3,4,1,2),_ConfigIfAPRowStatus_Type())
configIfAPRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIfAPRowStatus.setStatus(_A)
_ConfigIfAPPhy_Type=NetifName
_ConfigIfAPPhy_Object=MibTableColumn
configIfAPPhy=_ConfigIfAPPhy_Object((1,3,6,1,4,1,28097,8,3,4,1,3),_ConfigIfAPPhy_Type())
configIfAPPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfAPPhy.setStatus(_A)
class _ConfigIfAPSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ConfigIfAPSsid_Type.__name__=_F
_ConfigIfAPSsid_Object=MibTableColumn
configIfAPSsid=_ConfigIfAPSsid_Object((1,3,6,1,4,1,28097,8,3,4,1,4),_ConfigIfAPSsid_Type())
configIfAPSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPSsid.setStatus(_A)
_ConfigIfAPHidden_Type=DisableEnable
_ConfigIfAPHidden_Object=MibTableColumn
configIfAPHidden=_ConfigIfAPHidden_Object((1,3,6,1,4,1,28097,8,3,4,1,5),_ConfigIfAPHidden_Type())
configIfAPHidden.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPHidden.setStatus(_A)
_ConfigIfAPWds_Type=DisableEnable
_ConfigIfAPWds_Object=MibTableColumn
configIfAPWds=_ConfigIfAPWds_Object((1,3,6,1,4,1,28097,8,3,4,1,6),_ConfigIfAPWds_Type())
configIfAPWds.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWds.setStatus(_A)
_ConfigIfAPIsolate_Type=DisableEnable
_ConfigIfAPIsolate_Object=MibTableColumn
configIfAPIsolate=_ConfigIfAPIsolate_Object((1,3,6,1,4,1,28097,8,3,4,1,7),_ConfigIfAPIsolate_Type())
configIfAPIsolate.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPIsolate.setStatus(_A)
_ConfigIfAPSecurityMode_Type=SecurityModes
_ConfigIfAPSecurityMode_Object=MibTableColumn
configIfAPSecurityMode=_ConfigIfAPSecurityMode_Object((1,3,6,1,4,1,28097,8,3,4,1,8),_ConfigIfAPSecurityMode_Type())
configIfAPSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPSecurityMode.setStatus(_A)
_ConfigIfAPWepKey1_Type=WepKeys
_ConfigIfAPWepKey1_Object=MibTableColumn
configIfAPWepKey1=_ConfigIfAPWepKey1_Object((1,3,6,1,4,1,28097,8,3,4,1,9),_ConfigIfAPWepKey1_Type())
configIfAPWepKey1.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWepKey1.setStatus(_A)
_ConfigIfAPWepKey2_Type=WepKeys
_ConfigIfAPWepKey2_Object=MibTableColumn
configIfAPWepKey2=_ConfigIfAPWepKey2_Object((1,3,6,1,4,1,28097,8,3,4,1,10),_ConfigIfAPWepKey2_Type())
configIfAPWepKey2.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWepKey2.setStatus(_A)
_ConfigIfAPWepKey3_Type=WepKeys
_ConfigIfAPWepKey3_Object=MibTableColumn
configIfAPWepKey3=_ConfigIfAPWepKey3_Object((1,3,6,1,4,1,28097,8,3,4,1,11),_ConfigIfAPWepKey3_Type())
configIfAPWepKey3.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWepKey3.setStatus(_A)
_ConfigIfAPWepKey4_Type=WepKeys
_ConfigIfAPWepKey4_Object=MibTableColumn
configIfAPWepKey4=_ConfigIfAPWepKey4_Object((1,3,6,1,4,1,28097,8,3,4,1,12),_ConfigIfAPWepKey4_Type())
configIfAPWepKey4.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWepKey4.setStatus(_A)
_ConfigIfAPWepKey_Type=Integer32
_ConfigIfAPWepKey_Object=MibTableColumn
configIfAPWepKey=_ConfigIfAPWepKey_Object((1,3,6,1,4,1,28097,8,3,4,1,13),_ConfigIfAPWepKey_Type())
configIfAPWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWepKey.setStatus(_A)
class _ConfigIfAPWepAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('shared',2)))
_ConfigIfAPWepAuthentication_Type.__name__=_D
_ConfigIfAPWepAuthentication_Object=MibTableColumn
configIfAPWepAuthentication=_ConfigIfAPWepAuthentication_Object((1,3,6,1,4,1,28097,8,3,4,1,14),_ConfigIfAPWepAuthentication_Type())
configIfAPWepAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWepAuthentication.setStatus(_A)
_ConfigIfAPWpaVersion_Type=WpaVersions
_ConfigIfAPWpaVersion_Object=MibTableColumn
configIfAPWpaVersion=_ConfigIfAPWpaVersion_Object((1,3,6,1,4,1,28097,8,3,4,1,15),_ConfigIfAPWpaVersion_Type())
configIfAPWpaVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWpaVersion.setStatus(_A)
_ConfigIfAPWpaCipher_Type=CipherTypes
_ConfigIfAPWpaCipher_Object=MibTableColumn
configIfAPWpaCipher=_ConfigIfAPWpaCipher_Object((1,3,6,1,4,1,28097,8,3,4,1,16),_ConfigIfAPWpaCipher_Type())
configIfAPWpaCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfAPWpaCipher.setStatus(_A)
class _ConfigIfAPKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_ConfigIfAPKey_Type.__name__=_F
_ConfigIfAPKey_Object=MibTableColumn
configIfAPKey=_ConfigIfAPKey_Object((1,3,6,1,4,1,28097,8,3,4,1,17),_ConfigIfAPKey_Type())
configIfAPKey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPKey.setStatus(_A)
_ConfigIfAPRadiusIndex_Type=Integer32
_ConfigIfAPRadiusIndex_Object=MibTableColumn
configIfAPRadiusIndex=_ConfigIfAPRadiusIndex_Object((1,3,6,1,4,1,28097,8,3,4,1,18),_ConfigIfAPRadiusIndex_Type())
configIfAPRadiusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPRadiusIndex.setStatus(_A)
_ConfigIfAPPreAuthentication_Type=DisableEnable
_ConfigIfAPPreAuthentication_Object=MibTableColumn
configIfAPPreAuthentication=_ConfigIfAPPreAuthentication_Object((1,3,6,1,4,1,28097,8,3,4,1,19),_ConfigIfAPPreAuthentication_Type())
configIfAPPreAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPPreAuthentication.setStatus(_A)
class _ConfigIfAPMACFilterBehaviour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_s,1),('denyMAC',2),('allowMAC',3)))
_ConfigIfAPMACFilterBehaviour_Type.__name__=_D
_ConfigIfAPMACFilterBehaviour_Object=MibTableColumn
configIfAPMACFilterBehaviour=_ConfigIfAPMACFilterBehaviour_Object((1,3,6,1,4,1,28097,8,3,4,1,20),_ConfigIfAPMACFilterBehaviour_Type())
configIfAPMACFilterBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPMACFilterBehaviour.setStatus(_A)
_ConfigIfAPMACFilterAddresses_Type=OctetString
_ConfigIfAPMACFilterAddresses_Object=MibTableColumn
configIfAPMACFilterAddresses=_ConfigIfAPMACFilterAddresses_Object((1,3,6,1,4,1,28097,8,3,4,1,21),_ConfigIfAPMACFilterAddresses_Type())
configIfAPMACFilterAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPMACFilterAddresses.setStatus(_A)
_ConfigIfAPWpaGroupRekey_Type=Integer32
_ConfigIfAPWpaGroupRekey_Object=MibTableColumn
configIfAPWpaGroupRekey=_ConfigIfAPWpaGroupRekey_Object((1,3,6,1,4,1,28097,8,3,4,1,22),_ConfigIfAPWpaGroupRekey_Type())
configIfAPWpaGroupRekey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWpaGroupRekey.setStatus(_A)
_ConfigIfAPWpaPairRekey_Type=Integer32
_ConfigIfAPWpaPairRekey_Object=MibTableColumn
configIfAPWpaPairRekey=_ConfigIfAPWpaPairRekey_Object((1,3,6,1,4,1,28097,8,3,4,1,23),_ConfigIfAPWpaPairRekey_Type())
configIfAPWpaPairRekey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWpaPairRekey.setStatus(_A)
_ConfigIfAPWpaMasterRekey_Type=Integer32
_ConfigIfAPWpaMasterRekey_Object=MibTableColumn
configIfAPWpaMasterRekey=_ConfigIfAPWpaMasterRekey_Object((1,3,6,1,4,1,28097,8,3,4,1,24),_ConfigIfAPWpaMasterRekey_Type())
configIfAPWpaMasterRekey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWpaMasterRekey.setStatus(_A)
class _ConfigIfAPWpaProtectedFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_s,1),('enable-optional',2),('enable-required',3)))
_ConfigIfAPWpaProtectedFrame_Type.__name__=_D
_ConfigIfAPWpaProtectedFrame_Object=MibTableColumn
configIfAPWpaProtectedFrame=_ConfigIfAPWpaProtectedFrame_Object((1,3,6,1,4,1,28097,8,3,4,1,25),_ConfigIfAPWpaProtectedFrame_Type())
configIfAPWpaProtectedFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPWpaProtectedFrame.setStatus(_A)
_ConfigIfAPMaxSimultaneousAssoc_Type=Integer32
_ConfigIfAPMaxSimultaneousAssoc_Object=MibTableColumn
configIfAPMaxSimultaneousAssoc=_ConfigIfAPMaxSimultaneousAssoc_Object((1,3,6,1,4,1,28097,8,3,4,1,26),_ConfigIfAPMaxSimultaneousAssoc_Type())
configIfAPMaxSimultaneousAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPMaxSimultaneousAssoc.setStatus(_A)
_ConfigIfAPPasspointConfigName_Type=OctetString
_ConfigIfAPPasspointConfigName_Object=MibTableColumn
configIfAPPasspointConfigName=_ConfigIfAPPasspointConfigName_Object((1,3,6,1,4,1,28097,8,3,4,1,27),_ConfigIfAPPasspointConfigName_Type())
configIfAPPasspointConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfAPPasspointConfigName.setStatus(_A)
_ConfigIfMeshTable_Object=MibTable
configIfMeshTable=_ConfigIfMeshTable_Object((1,3,6,1,4,1,28097,8,3,5))
if mibBuilder.loadTexts:configIfMeshTable.setStatus(_A)
_ConfigIfMeshEntry_Object=MibTableRow
configIfMeshEntry=_ConfigIfMeshEntry_Object((1,3,6,1,4,1,28097,8,3,5,1))
configIfMeshEntry.setIndexNames((0,_E,_AY))
if mibBuilder.loadTexts:configIfMeshEntry.setStatus(_A)
_ConfigIfMeshName_Type=NetifName
_ConfigIfMeshName_Object=MibTableColumn
configIfMeshName=_ConfigIfMeshName_Object((1,3,6,1,4,1,28097,8,3,5,1,1),_ConfigIfMeshName_Type())
configIfMeshName.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfMeshName.setStatus(_A)
_ConfigIfMeshRowStatus_Type=RowStatus
_ConfigIfMeshRowStatus_Object=MibTableColumn
configIfMeshRowStatus=_ConfigIfMeshRowStatus_Object((1,3,6,1,4,1,28097,8,3,5,1,2),_ConfigIfMeshRowStatus_Type())
configIfMeshRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIfMeshRowStatus.setStatus(_A)
_ConfigIfMeshPhy_Type=NetifName
_ConfigIfMeshPhy_Object=MibTableColumn
configIfMeshPhy=_ConfigIfMeshPhy_Object((1,3,6,1,4,1,28097,8,3,5,1,3),_ConfigIfMeshPhy_Type())
configIfMeshPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfMeshPhy.setStatus(_A)
class _ConfigIfMeshId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ConfigIfMeshId_Type.__name__=_F
_ConfigIfMeshId_Object=MibTableColumn
configIfMeshId=_ConfigIfMeshId_Object((1,3,6,1,4,1,28097,8,3,5,1,4),_ConfigIfMeshId_Type())
configIfMeshId.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshId.setStatus(_A)
class _ConfigIfMeshSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*((_N,1),('sae',5)))
_ConfigIfMeshSecurityMode_Type.__name__=_D
_ConfigIfMeshSecurityMode_Object=MibTableColumn
configIfMeshSecurityMode=_ConfigIfMeshSecurityMode_Object((1,3,6,1,4,1,28097,8,3,5,1,5),_ConfigIfMeshSecurityMode_Type())
configIfMeshSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshSecurityMode.setStatus(_A)
class _ConfigIfMeshPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_ConfigIfMeshPreSharedKey_Type.__name__=_F
_ConfigIfMeshPreSharedKey_Object=MibTableColumn
configIfMeshPreSharedKey=_ConfigIfMeshPreSharedKey_Object((1,3,6,1,4,1,28097,8,3,5,1,6),_ConfigIfMeshPreSharedKey_Type())
configIfMeshPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshPreSharedKey.setStatus(_A)
_ConfigIfMeshPathRefreshTime_Type=Integer32
_ConfigIfMeshPathRefreshTime_Object=MibTableColumn
configIfMeshPathRefreshTime=_ConfigIfMeshPathRefreshTime_Object((1,3,6,1,4,1,28097,8,3,5,1,7),_ConfigIfMeshPathRefreshTime_Type())
configIfMeshPathRefreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshPathRefreshTime.setStatus(_A)
_ConfigIfMeshMinDiscoveryTimeout_Type=Integer32
_ConfigIfMeshMinDiscoveryTimeout_Object=MibTableColumn
configIfMeshMinDiscoveryTimeout=_ConfigIfMeshMinDiscoveryTimeout_Object((1,3,6,1,4,1,28097,8,3,5,1,8),_ConfigIfMeshMinDiscoveryTimeout_Type())
configIfMeshMinDiscoveryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshMinDiscoveryTimeout.setStatus(_A)
_ConfigIfMeshActivePathTimeout_Type=Integer32
_ConfigIfMeshActivePathTimeout_Object=MibTableColumn
configIfMeshActivePathTimeout=_ConfigIfMeshActivePathTimeout_Object((1,3,6,1,4,1,28097,8,3,5,1,9),_ConfigIfMeshActivePathTimeout_Type())
configIfMeshActivePathTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshActivePathTimeout.setStatus(_A)
_ConfigIfMeshNetworkDiameterTraversalTime_Type=Integer32
_ConfigIfMeshNetworkDiameterTraversalTime_Object=MibTableColumn
configIfMeshNetworkDiameterTraversalTime=_ConfigIfMeshNetworkDiameterTraversalTime_Object((1,3,6,1,4,1,28097,8,3,5,1,10),_ConfigIfMeshNetworkDiameterTraversalTime_Type())
configIfMeshNetworkDiameterTraversalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshNetworkDiameterTraversalTime.setStatus(_A)
class _ConfigIfMeshRootMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notroot',1),('proactivepreq',2),('proactivepreqprep',3),('proactiverann',4)))
_ConfigIfMeshRootMode_Type.__name__=_D
_ConfigIfMeshRootMode_Object=MibTableColumn
configIfMeshRootMode=_ConfigIfMeshRootMode_Object((1,3,6,1,4,1,28097,8,3,5,1,11),_ConfigIfMeshRootMode_Type())
configIfMeshRootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshRootMode.setStatus(_A)
_ConfigIfMeshGatesAnnouncement_Type=DisableEnable
_ConfigIfMeshGatesAnnouncement_Object=MibTableColumn
configIfMeshGatesAnnouncement=_ConfigIfMeshGatesAnnouncement_Object((1,3,6,1,4,1,28097,8,3,5,1,12),_ConfigIfMeshGatesAnnouncement_Type())
configIfMeshGatesAnnouncement.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshGatesAnnouncement.setStatus(_A)
_ConfigIfMeshActivePathToRootTimeout_Type=Integer32
_ConfigIfMeshActivePathToRootTimeout_Object=MibTableColumn
configIfMeshActivePathToRootTimeout=_ConfigIfMeshActivePathToRootTimeout_Object((1,3,6,1,4,1,28097,8,3,5,1,13),_ConfigIfMeshActivePathToRootTimeout_Type())
configIfMeshActivePathToRootTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshActivePathToRootTimeout.setStatus(_A)
_ConfigIfMeshPreqRootInterval_Type=Integer32
_ConfigIfMeshPreqRootInterval_Object=MibTableColumn
configIfMeshPreqRootInterval=_ConfigIfMeshPreqRootInterval_Object((1,3,6,1,4,1,28097,8,3,5,1,14),_ConfigIfMeshPreqRootInterval_Type())
configIfMeshPreqRootInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshPreqRootInterval.setStatus(_A)
_ConfigIfMeshRannRootInterval_Type=Integer32
_ConfigIfMeshRannRootInterval_Object=MibTableColumn
configIfMeshRannRootInterval=_ConfigIfMeshRannRootInterval_Object((1,3,6,1,4,1,28097,8,3,5,1,15),_ConfigIfMeshRannRootInterval_Type())
configIfMeshRannRootInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfMeshRannRootInterval.setStatus(_A)
_ConfigIfBridgeTable_Object=MibTable
configIfBridgeTable=_ConfigIfBridgeTable_Object((1,3,6,1,4,1,28097,8,3,6))
if mibBuilder.loadTexts:configIfBridgeTable.setStatus(_A)
_ConfigIfBridgeEntry_Object=MibTableRow
configIfBridgeEntry=_ConfigIfBridgeEntry_Object((1,3,6,1,4,1,28097,8,3,6,1))
configIfBridgeEntry.setIndexNames((0,_E,_AZ))
if mibBuilder.loadTexts:configIfBridgeEntry.setStatus(_A)
_ConfigIfBridgeName_Type=NetifName
_ConfigIfBridgeName_Object=MibTableColumn
configIfBridgeName=_ConfigIfBridgeName_Object((1,3,6,1,4,1,28097,8,3,6,1,1),_ConfigIfBridgeName_Type())
configIfBridgeName.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfBridgeName.setStatus(_A)
_ConfigIfBridgeRowStatus_Type=RowStatus
_ConfigIfBridgeRowStatus_Object=MibTableColumn
configIfBridgeRowStatus=_ConfigIfBridgeRowStatus_Object((1,3,6,1,4,1,28097,8,3,6,1,2),_ConfigIfBridgeRowStatus_Type())
configIfBridgeRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIfBridgeRowStatus.setStatus(_A)
class _ConfigIfBridgeStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),('rstp',2),('stp-only',3)))
_ConfigIfBridgeStp_Type.__name__=_D
_ConfigIfBridgeStp_Object=MibTableColumn
configIfBridgeStp=_ConfigIfBridgeStp_Object((1,3,6,1,4,1,28097,8,3,6,1,3),_ConfigIfBridgeStp_Type())
configIfBridgeStp.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfBridgeStp.setStatus(_A)
_ConfigIfBridgePriority_Type=Integer32
_ConfigIfBridgePriority_Object=MibTableColumn
configIfBridgePriority=_ConfigIfBridgePriority_Object((1,3,6,1,4,1,28097,8,3,6,1,4),_ConfigIfBridgePriority_Type())
configIfBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfBridgePriority.setStatus(_A)
_ConfigIfBridgeHello_Type=Integer32
_ConfigIfBridgeHello_Object=MibTableColumn
configIfBridgeHello=_ConfigIfBridgeHello_Object((1,3,6,1,4,1,28097,8,3,6,1,5),_ConfigIfBridgeHello_Type())
configIfBridgeHello.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfBridgeHello.setStatus(_A)
_ConfigIfBridgeMaxAge_Type=Integer32
_ConfigIfBridgeMaxAge_Object=MibTableColumn
configIfBridgeMaxAge=_ConfigIfBridgeMaxAge_Object((1,3,6,1,4,1,28097,8,3,6,1,6),_ConfigIfBridgeMaxAge_Type())
configIfBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfBridgeMaxAge.setStatus(_A)
_ConfigIfBridgeForwardDelay_Type=Integer32
_ConfigIfBridgeForwardDelay_Object=MibTableColumn
configIfBridgeForwardDelay=_ConfigIfBridgeForwardDelay_Object((1,3,6,1,4,1,28097,8,3,6,1,7),_ConfigIfBridgeForwardDelay_Type())
configIfBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfBridgeForwardDelay.setStatus(_A)
_ConfigIfBridgeLldpForward_Type=DisableEnable
_ConfigIfBridgeLldpForward_Object=MibTableColumn
configIfBridgeLldpForward=_ConfigIfBridgeLldpForward_Object((1,3,6,1,4,1,28097,8,3,6,1,8),_ConfigIfBridgeLldpForward_Type())
configIfBridgeLldpForward.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfBridgeLldpForward.setStatus(_A)
_ConfigIfVlanTable_Object=MibTable
configIfVlanTable=_ConfigIfVlanTable_Object((1,3,6,1,4,1,28097,8,3,7))
if mibBuilder.loadTexts:configIfVlanTable.setStatus(_A)
_ConfigIfVlanEntry_Object=MibTableRow
configIfVlanEntry=_ConfigIfVlanEntry_Object((1,3,6,1,4,1,28097,8,3,7,1))
configIfVlanEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:configIfVlanEntry.setStatus(_A)
_ConfigIfVlanIndex_Type=OctetString
_ConfigIfVlanIndex_Object=MibTableColumn
configIfVlanIndex=_ConfigIfVlanIndex_Object((1,3,6,1,4,1,28097,8,3,7,1,1),_ConfigIfVlanIndex_Type())
configIfVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfVlanIndex.setStatus(_A)
_ConfigIfVlanRowStatus_Type=RowStatus
_ConfigIfVlanRowStatus_Object=MibTableColumn
configIfVlanRowStatus=_ConfigIfVlanRowStatus_Object((1,3,6,1,4,1,28097,8,3,7,1,2),_ConfigIfVlanRowStatus_Type())
configIfVlanRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIfVlanRowStatus.setStatus(_A)
_ConfigIfVlanFriendlyName_Type=OctetString
_ConfigIfVlanFriendlyName_Object=MibTableColumn
configIfVlanFriendlyName=_ConfigIfVlanFriendlyName_Object((1,3,6,1,4,1,28097,8,3,7,1,3),_ConfigIfVlanFriendlyName_Type())
configIfVlanFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfVlanFriendlyName.setStatus(_A)
_ConfigIfVlanHostIfName_Type=NetifName
_ConfigIfVlanHostIfName_Object=MibTableColumn
configIfVlanHostIfName=_ConfigIfVlanHostIfName_Object((1,3,6,1,4,1,28097,8,3,7,1,4),_ConfigIfVlanHostIfName_Type())
configIfVlanHostIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfVlanHostIfName.setStatus(_A)
_ConfigIfVlanId_Type=Integer32
_ConfigIfVlanId_Object=MibTableColumn
configIfVlanId=_ConfigIfVlanId_Object((1,3,6,1,4,1,28097,8,3,7,1,5),_ConfigIfVlanId_Type())
configIfVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfVlanId.setStatus(_A)
_ConfigIfSrccTable_Object=MibTable
configIfSrccTable=_ConfigIfSrccTable_Object((1,3,6,1,4,1,28097,8,3,8))
if mibBuilder.loadTexts:configIfSrccTable.setStatus(_A)
_ConfigIfSrccEntry_Object=MibTableRow
configIfSrccEntry=_ConfigIfSrccEntry_Object((1,3,6,1,4,1,28097,8,3,8,1))
configIfSrccEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:configIfSrccEntry.setStatus(_A)
_ConfigIfSrccName_Type=NetifName
_ConfigIfSrccName_Object=MibTableColumn
configIfSrccName=_ConfigIfSrccName_Object((1,3,6,1,4,1,28097,8,3,8,1,1),_ConfigIfSrccName_Type())
configIfSrccName.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfSrccName.setStatus(_A)
_ConfigIfSrccRowStatus_Type=RowStatus
_ConfigIfSrccRowStatus_Object=MibTableColumn
configIfSrccRowStatus=_ConfigIfSrccRowStatus_Object((1,3,6,1,4,1,28097,8,3,8,1,2),_ConfigIfSrccRowStatus_Type())
configIfSrccRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configIfSrccRowStatus.setStatus(_A)
_ConfigIfSrccPhy_Type=NetifName
_ConfigIfSrccPhy_Object=MibTableColumn
configIfSrccPhy=_ConfigIfSrccPhy_Object((1,3,6,1,4,1,28097,8,3,8,1,3),_ConfigIfSrccPhy_Type())
configIfSrccPhy.setMaxAccess(_C)
if mibBuilder.loadTexts:configIfSrccPhy.setStatus(_A)
class _ConfigIfSrccDiscoverApSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ConfigIfSrccDiscoverApSsid_Type.__name__=_F
_ConfigIfSrccDiscoverApSsid_Object=MibTableColumn
configIfSrccDiscoverApSsid=_ConfigIfSrccDiscoverApSsid_Object((1,3,6,1,4,1,28097,8,3,8,1,4),_ConfigIfSrccDiscoverApSsid_Type())
configIfSrccDiscoverApSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccDiscoverApSsid.setStatus(_A)
class _ConfigIfSrccProductType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('typeA',1),('typeB',2)))
_ConfigIfSrccProductType_Type.__name__=_D
_ConfigIfSrccProductType_Object=MibTableColumn
configIfSrccProductType=_ConfigIfSrccProductType_Object((1,3,6,1,4,1,28097,8,3,8,1,5),_ConfigIfSrccProductType_Type())
configIfSrccProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccProductType.setStatus(_A)
_ConfigIfSrccDiscSigThreshold_Type=Integer32
_ConfigIfSrccDiscSigThreshold_Object=MibTableColumn
configIfSrccDiscSigThreshold=_ConfigIfSrccDiscSigThreshold_Object((1,3,6,1,4,1,28097,8,3,8,1,6),_ConfigIfSrccDiscSigThreshold_Type())
configIfSrccDiscSigThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccDiscSigThreshold.setStatus(_A)
_ConfigIfSrccDiscDuration_Type=Integer32
_ConfigIfSrccDiscDuration_Object=MibTableColumn
configIfSrccDiscDuration=_ConfigIfSrccDiscDuration_Object((1,3,6,1,4,1,28097,8,3,8,1,7),_ConfigIfSrccDiscDuration_Type())
configIfSrccDiscDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccDiscDuration.setStatus(_A)
_ConfigIfSrccBrokenThreshold_Type=Integer32
_ConfigIfSrccBrokenThreshold_Object=MibTableColumn
configIfSrccBrokenThreshold=_ConfigIfSrccBrokenThreshold_Object((1,3,6,1,4,1,28097,8,3,8,1,8),_ConfigIfSrccBrokenThreshold_Type())
configIfSrccBrokenThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccBrokenThreshold.setStatus(_A)
_ConfigIfSrccBrokenDuration_Type=Integer32
_ConfigIfSrccBrokenDuration_Object=MibTableColumn
configIfSrccBrokenDuration=_ConfigIfSrccBrokenDuration_Object((1,3,6,1,4,1,28097,8,3,8,1,9),_ConfigIfSrccBrokenDuration_Type())
configIfSrccBrokenDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccBrokenDuration.setStatus(_A)
class _ConfigIfSrccWifiBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('band-5g',1),('band-24',2)))
_ConfigIfSrccWifiBand_Type.__name__=_D
_ConfigIfSrccWifiBand_Object=MibTableColumn
configIfSrccWifiBand=_ConfigIfSrccWifiBand_Object((1,3,6,1,4,1,28097,8,3,8,1,10),_ConfigIfSrccWifiBand_Type())
configIfSrccWifiBand.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccWifiBand.setStatus(_A)
_ConfigIfSrccFirstChannel_Type=Integer32
_ConfigIfSrccFirstChannel_Object=MibTableColumn
configIfSrccFirstChannel=_ConfigIfSrccFirstChannel_Object((1,3,6,1,4,1,28097,8,3,8,1,11),_ConfigIfSrccFirstChannel_Type())
configIfSrccFirstChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccFirstChannel.setStatus(_A)
_ConfigIfSrccSecondChannel_Type=Integer32
_ConfigIfSrccSecondChannel_Object=MibTableColumn
configIfSrccSecondChannel=_ConfigIfSrccSecondChannel_Object((1,3,6,1,4,1,28097,8,3,8,1,12),_ConfigIfSrccSecondChannel_Type())
configIfSrccSecondChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccSecondChannel.setStatus(_A)
_ConfigIfSrccDiscScanDuration_Type=Integer32
_ConfigIfSrccDiscScanDuration_Object=MibTableColumn
configIfSrccDiscScanDuration=_ConfigIfSrccDiscScanDuration_Object((1,3,6,1,4,1,28097,8,3,8,1,13),_ConfigIfSrccDiscScanDuration_Type())
configIfSrccDiscScanDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccDiscScanDuration.setStatus(_A)
class _ConfigIfSrccMixRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('wifi',1),('ethernet',2),(_N,3)))
_ConfigIfSrccMixRedundancy_Type.__name__=_D
_ConfigIfSrccMixRedundancy_Object=MibTableColumn
configIfSrccMixRedundancy=_ConfigIfSrccMixRedundancy_Object((1,3,6,1,4,1,28097,8,3,8,1,14),_ConfigIfSrccMixRedundancy_Type())
configIfSrccMixRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccMixRedundancy.setStatus(_A)
_ConfigIfSrccMixRedundancyBoost_Type=Integer32
_ConfigIfSrccMixRedundancyBoost_Object=MibTableColumn
configIfSrccMixRedundancyBoost=_ConfigIfSrccMixRedundancyBoost_Object((1,3,6,1,4,1,28097,8,3,8,1,15),_ConfigIfSrccMixRedundancyBoost_Type())
configIfSrccMixRedundancyBoost.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccMixRedundancyBoost.setStatus(_A)
_ConfigIfSrccPeerTableTimeout_Type=Integer32
_ConfigIfSrccPeerTableTimeout_Object=MibTableColumn
configIfSrccPeerTableTimeout=_ConfigIfSrccPeerTableTimeout_Object((1,3,6,1,4,1,28097,8,3,8,1,16),_ConfigIfSrccPeerTableTimeout_Type())
configIfSrccPeerTableTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccPeerTableTimeout.setStatus(_A)
_ConfigIfSrccTargetTableTimeout_Type=Integer32
_ConfigIfSrccTargetTableTimeout_Object=MibTableColumn
configIfSrccTargetTableTimeout=_ConfigIfSrccTargetTableTimeout_Object((1,3,6,1,4,1,28097,8,3,8,1,17),_ConfigIfSrccTargetTableTimeout_Type())
configIfSrccTargetTableTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccTargetTableTimeout.setStatus(_A)
_ConfigIfSrccPeerAcknowTimeout_Type=Integer32
_ConfigIfSrccPeerAcknowTimeout_Object=MibTableColumn
configIfSrccPeerAcknowTimeout=_ConfigIfSrccPeerAcknowTimeout_Object((1,3,6,1,4,1,28097,8,3,8,1,18),_ConfigIfSrccPeerAcknowTimeout_Type())
configIfSrccPeerAcknowTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccPeerAcknowTimeout.setStatus(_A)
_ConfigIfSrccPeerReconfigTimeout_Type=Integer32
_ConfigIfSrccPeerReconfigTimeout_Object=MibTableColumn
configIfSrccPeerReconfigTimeout=_ConfigIfSrccPeerReconfigTimeout_Object((1,3,6,1,4,1,28097,8,3,8,1,19),_ConfigIfSrccPeerReconfigTimeout_Type())
configIfSrccPeerReconfigTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccPeerReconfigTimeout.setStatus(_A)
_ConfigIfSrccGreBridgeIpAddr_Type=IpAddress
_ConfigIfSrccGreBridgeIpAddr_Object=MibTableColumn
configIfSrccGreBridgeIpAddr=_ConfigIfSrccGreBridgeIpAddr_Object((1,3,6,1,4,1,28097,8,3,8,1,20),_ConfigIfSrccGreBridgeIpAddr_Type())
configIfSrccGreBridgeIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:configIfSrccGreBridgeIpAddr.setStatus(_A)
_Roaming_ObjectIdentity=ObjectIdentity
roaming=_Roaming_ObjectIdentity((1,3,6,1,4,1,28097,8,4))
class _RoamingAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('scan',1),('cbb',2),('plh',3)))
_RoamingAlgorithm_Type.__name__=_D
_RoamingAlgorithm_Object=MibScalar
roamingAlgorithm=_RoamingAlgorithm_Object((1,3,6,1,4,1,28097,8,4,1),_RoamingAlgorithm_Type())
roamingAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingAlgorithm.setStatus(_A)
class _RoamingPLHposition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('front',1),('rear',2)))
_RoamingPLHposition_Type.__name__=_D
_RoamingPLHposition_Object=MibScalar
roamingPLHposition=_RoamingPLHposition_Object((1,3,6,1,4,1,28097,8,4,2),_RoamingPLHposition_Type())
roamingPLHposition.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHposition.setStatus(_A)
class _RoamingPLHjitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_RoamingPLHjitter_Type.__name__=_D
_RoamingPLHjitter_Object=MibScalar
roamingPLHjitter=_RoamingPLHjitter_Object((1,3,6,1,4,1,28097,8,4,3),_RoamingPLHjitter_Type())
roamingPLHjitter.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHjitter.setStatus(_A)
_RoamingPLHurgent_Type=WifiLevel
_RoamingPLHurgent_Object=MibScalar
roamingPLHurgent=_RoamingPLHurgent_Object((1,3,6,1,4,1,28097,8,4,4),_RoamingPLHurgent_Type())
roamingPLHurgent.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHurgent.setStatus(_A)
_RoamingPLHfront_ObjectIdentity=ObjectIdentity
roamingPLHfront=_RoamingPLHfront_ObjectIdentity((1,3,6,1,4,1,28097,8,4,5))
_RoamingPLHfrontCandMin_Type=WifiLevel
_RoamingPLHfrontCandMin_Object=MibScalar
roamingPLHfrontCandMin=_RoamingPLHfrontCandMin_Object((1,3,6,1,4,1,28097,8,4,5,1),_RoamingPLHfrontCandMin_Type())
roamingPLHfrontCandMin.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHfrontCandMin.setStatus(_A)
_RoamingPLHfrontCandMax_Type=WifiLevel
_RoamingPLHfrontCandMax_Object=MibScalar
roamingPLHfrontCandMax=_RoamingPLHfrontCandMax_Object((1,3,6,1,4,1,28097,8,4,5,2),_RoamingPLHfrontCandMax_Type())
roamingPLHfrontCandMax.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHfrontCandMax.setStatus(_A)
_RoamingPLHfrontCurrentLow_Type=WifiLevel
_RoamingPLHfrontCurrentLow_Object=MibScalar
roamingPLHfrontCurrentLow=_RoamingPLHfrontCurrentLow_Object((1,3,6,1,4,1,28097,8,4,5,3),_RoamingPLHfrontCurrentLow_Type())
roamingPLHfrontCurrentLow.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHfrontCurrentLow.setStatus(_A)
_RoamingPLHfrontCurrentHigh_Type=WifiLevel
_RoamingPLHfrontCurrentHigh_Object=MibScalar
roamingPLHfrontCurrentHigh=_RoamingPLHfrontCurrentHigh_Object((1,3,6,1,4,1,28097,8,4,5,4),_RoamingPLHfrontCurrentHigh_Type())
roamingPLHfrontCurrentHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHfrontCurrentHigh.setStatus(_A)
_RoamingPLHrear_ObjectIdentity=ObjectIdentity
roamingPLHrear=_RoamingPLHrear_ObjectIdentity((1,3,6,1,4,1,28097,8,4,6))
_RoamingPLHrearCandMin_Type=WifiLevel
_RoamingPLHrearCandMin_Object=MibScalar
roamingPLHrearCandMin=_RoamingPLHrearCandMin_Object((1,3,6,1,4,1,28097,8,4,6,1),_RoamingPLHrearCandMin_Type())
roamingPLHrearCandMin.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHrearCandMin.setStatus(_A)
_RoamingPLHrearCandMax_Type=WifiLevel
_RoamingPLHrearCandMax_Object=MibScalar
roamingPLHrearCandMax=_RoamingPLHrearCandMax_Object((1,3,6,1,4,1,28097,8,4,6,2),_RoamingPLHrearCandMax_Type())
roamingPLHrearCandMax.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHrearCandMax.setStatus(_A)
_RoamingPLHrearCurrentLow_Type=WifiLevel
_RoamingPLHrearCurrentLow_Object=MibScalar
roamingPLHrearCurrentLow=_RoamingPLHrearCurrentLow_Object((1,3,6,1,4,1,28097,8,4,6,3),_RoamingPLHrearCurrentLow_Type())
roamingPLHrearCurrentLow.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHrearCurrentLow.setStatus(_A)
_RoamingPLHrearCurrentHigh_Type=WifiLevel
_RoamingPLHrearCurrentHigh_Object=MibScalar
roamingPLHrearCurrentHigh=_RoamingPLHrearCurrentHigh_Object((1,3,6,1,4,1,28097,8,4,6,4),_RoamingPLHrearCurrentHigh_Type())
roamingPLHrearCurrentHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:roamingPLHrearCurrentHigh.setStatus(_A)
_ServiceStatus_ObjectIdentity=ObjectIdentity
serviceStatus=_ServiceStatus_ObjectIdentity((1,3,6,1,4,1,28097,9))
_Ss_webserver_ObjectIdentity=ObjectIdentity
ss_webserver=_Ss_webserver_ObjectIdentity((1,3,6,1,4,1,28097,9,1))
_Ss_dhcp_ObjectIdentity=ObjectIdentity
ss_dhcp=_Ss_dhcp_ObjectIdentity((1,3,6,1,4,1,28097,9,2))
_Ss_ntp_ObjectIdentity=ObjectIdentity
ss_ntp=_Ss_ntp_ObjectIdentity((1,3,6,1,4,1,28097,9,3))
_Ss_radius_ObjectIdentity=ObjectIdentity
ss_radius=_Ss_radius_ObjectIdentity((1,3,6,1,4,1,28097,9,4))
_Ss_snmp_ObjectIdentity=ObjectIdentity
ss_snmp=_Ss_snmp_ObjectIdentity((1,3,6,1,4,1,28097,9,5))
_SnmpAgentOIDTable_Object=MibTable
snmpAgentOIDTable=_SnmpAgentOIDTable_Object((1,3,6,1,4,1,28097,9,5,1))
if mibBuilder.loadTexts:snmpAgentOIDTable.setStatus(_A)
_SnmpAgentOIDEntry_Object=MibTableRow
snmpAgentOIDEntry=_SnmpAgentOIDEntry_Object((1,3,6,1,4,1,28097,9,5,1,1))
snmpAgentOIDEntry.setIndexNames((0,_E,_Ac))
if mibBuilder.loadTexts:snmpAgentOIDEntry.setStatus(_A)
_SnmpAgentOIDIndex_Type=Integer32
_SnmpAgentOIDIndex_Object=MibTableColumn
snmpAgentOIDIndex=_SnmpAgentOIDIndex_Object((1,3,6,1,4,1,28097,9,5,1,1,1),_SnmpAgentOIDIndex_Type())
snmpAgentOIDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpAgentOIDIndex.setStatus(_A)
_SnmpAgentOIDProductID_Type=Integer32
_SnmpAgentOIDProductID_Object=MibTableColumn
snmpAgentOIDProductID=_SnmpAgentOIDProductID_Object((1,3,6,1,4,1,28097,9,5,1,1,2),_SnmpAgentOIDProductID_Type())
snmpAgentOIDProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpAgentOIDProductID.setStatus(_A)
_Ss_dns_ObjectIdentity=ObjectIdentity
ss_dns=_Ss_dns_ObjectIdentity((1,3,6,1,4,1,28097,9,6))
_Ss_system_ObjectIdentity=ObjectIdentity
ss_system=_Ss_system_ObjectIdentity((1,3,6,1,4,1,28097,9,7))
class _SystemReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-ready',1),('ready',2)))
_SystemReady_Type.__name__=_D
_SystemReady_Object=MibScalar
systemReady=_SystemReady_Object((1,3,6,1,4,1,28097,9,7,1),_SystemReady_Type())
systemReady.setMaxAccess(_C)
if mibBuilder.loadTexts:systemReady.setStatus(_A)
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,28097,9,7,2))
_TempSensors_ObjectIdentity=ObjectIdentity
tempSensors=_TempSensors_ObjectIdentity((1,3,6,1,4,1,28097,9,7,2,1))
_MotherBoard0_Type=Integer32
_MotherBoard0_Object=MibScalar
motherBoard0=_MotherBoard0_Object((1,3,6,1,4,1,28097,9,7,2,1,1),_MotherBoard0_Type())
motherBoard0.setMaxAccess(_C)
if mibBuilder.loadTexts:motherBoard0.setStatus(_A)
_GpioInTable_Object=MibTable
gpioInTable=_GpioInTable_Object((1,3,6,1,4,1,28097,9,7,2,2))
if mibBuilder.loadTexts:gpioInTable.setStatus(_A)
_GpioInEntry_Object=MibTableRow
gpioInEntry=_GpioInEntry_Object((1,3,6,1,4,1,28097,9,7,2,2,1))
gpioInEntry.setIndexNames((0,_E,_Ad))
if mibBuilder.loadTexts:gpioInEntry.setStatus(_A)
_GpioInIndex_Type=Integer32
_GpioInIndex_Object=MibTableColumn
gpioInIndex=_GpioInIndex_Object((1,3,6,1,4,1,28097,9,7,2,2,1,1),_GpioInIndex_Type())
gpioInIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:gpioInIndex.setStatus(_A)
_GpioInState_Type=Integer32
_GpioInState_Object=MibTableColumn
gpioInState=_GpioInState_Object((1,3,6,1,4,1,28097,9,7,2,2,1,2),_GpioInState_Type())
gpioInState.setMaxAccess(_C)
if mibBuilder.loadTexts:gpioInState.setStatus(_A)
_GpioOutTable_Object=MibTable
gpioOutTable=_GpioOutTable_Object((1,3,6,1,4,1,28097,9,7,2,3))
if mibBuilder.loadTexts:gpioOutTable.setStatus(_A)
_GpioOutEntry_Object=MibTableRow
gpioOutEntry=_GpioOutEntry_Object((1,3,6,1,4,1,28097,9,7,2,3,1))
gpioOutEntry.setIndexNames((0,_E,_Ae))
if mibBuilder.loadTexts:gpioOutEntry.setStatus(_A)
_GpioOutIndex_Type=Integer32
_GpioOutIndex_Object=MibTableColumn
gpioOutIndex=_GpioOutIndex_Object((1,3,6,1,4,1,28097,9,7,2,3,1,1),_GpioOutIndex_Type())
gpioOutIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:gpioOutIndex.setStatus(_A)
_GpioOutState_Type=Integer32
_GpioOutState_Object=MibTableColumn
gpioOutState=_GpioOutState_Object((1,3,6,1,4,1,28097,9,7,2,3,1,2),_GpioOutState_Type())
gpioOutState.setMaxAccess(_B)
if mibBuilder.loadTexts:gpioOutState.setStatus(_A)
_Ss_gnss_ObjectIdentity=ObjectIdentity
ss_gnss=_Ss_gnss_ObjectIdentity((1,3,6,1,4,1,28097,9,8))
_Gnss_current_position_ObjectIdentity=ObjectIdentity
gnss_current_position=_Gnss_current_position_ObjectIdentity((1,3,6,1,4,1,28097,9,8,1))
class _PositionValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_PositionValid_Type.__name__=_D
_PositionValid_Object=MibScalar
positionValid=_PositionValid_Object((1,3,6,1,4,1,28097,9,8,1,1),_PositionValid_Type())
positionValid.setMaxAccess(_C)
if mibBuilder.loadTexts:positionValid.setStatus(_A)
_Fixdate_Type=OctetString
_Fixdate_Object=MibScalar
fixdate=_Fixdate_Object((1,3,6,1,4,1,28097,9,8,1,2),_Fixdate_Type())
fixdate.setMaxAccess(_C)
if mibBuilder.loadTexts:fixdate.setStatus(_A)
_Fixtime_Type=OctetString
_Fixtime_Object=MibScalar
fixtime=_Fixtime_Object((1,3,6,1,4,1,28097,9,8,1,3),_Fixtime_Type())
fixtime.setMaxAccess(_C)
if mibBuilder.loadTexts:fixtime.setStatus(_A)
_Latitude_Type=OctetString
_Latitude_Object=MibScalar
latitude=_Latitude_Object((1,3,6,1,4,1,28097,9,8,1,4),_Latitude_Type())
latitude.setMaxAccess(_C)
if mibBuilder.loadTexts:latitude.setStatus(_A)
_Longitude_Type=OctetString
_Longitude_Object=MibScalar
longitude=_Longitude_Object((1,3,6,1,4,1,28097,9,8,1,5),_Longitude_Type())
longitude.setMaxAccess(_C)
if mibBuilder.loadTexts:longitude.setStatus(_A)
_Altitude_Type=OctetString
_Altitude_Object=MibScalar
altitude=_Altitude_Object((1,3,6,1,4,1,28097,9,8,1,6),_Altitude_Type())
altitude.setMaxAccess(_C)
if mibBuilder.loadTexts:altitude.setStatus(_A)
_Speedkmh_Type=OctetString
_Speedkmh_Object=MibScalar
speedkmh=_Speedkmh_Object((1,3,6,1,4,1,28097,9,8,1,7),_Speedkmh_Type())
speedkmh.setMaxAccess(_C)
if mibBuilder.loadTexts:speedkmh.setStatus(_A)
_CourseDegrees_Type=OctetString
_CourseDegrees_Object=MibScalar
courseDegrees=_CourseDegrees_Object((1,3,6,1,4,1,28097,9,8,1,8),_CourseDegrees_Type())
courseDegrees.setMaxAccess(_C)
if mibBuilder.loadTexts:courseDegrees.setStatus(_A)
_Fixdimension_Type=Integer32
_Fixdimension_Object=MibScalar
fixdimension=_Fixdimension_Object((1,3,6,1,4,1,28097,9,8,1,9),_Fixdimension_Type())
fixdimension.setMaxAccess(_C)
if mibBuilder.loadTexts:fixdimension.setStatus(_A)
_GnssAllPositions_Type=OctetString
_GnssAllPositions_Object=MibScalar
gnssAllPositions=_GnssAllPositions_Object((1,3,6,1,4,1,28097,9,8,1,10),_GnssAllPositions_Type())
gnssAllPositions.setMaxAccess(_C)
if mibBuilder.loadTexts:gnssAllPositions.setStatus(_A)
_Ss_tcn_ObjectIdentity=ObjectIdentity
ss_tcn=_Ss_tcn_ObjectIdentity((1,3,6,1,4,1,28097,9,9))
_Ss_async_sysupgrade_ObjectIdentity=ObjectIdentity
ss_async_sysupgrade=_Ss_async_sysupgrade_ObjectIdentity((1,3,6,1,4,1,28097,9,10))
class _FirmwareExists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_FirmwareExists_Type.__name__=_D
_FirmwareExists_Object=MibScalar
firmwareExists=_FirmwareExists_Object((1,3,6,1,4,1,28097,9,10,1),_FirmwareExists_Type())
firmwareExists.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareExists.setStatus(_A)
_FirmwareInfo_Type=OctetString
_FirmwareInfo_Object=MibScalar
firmwareInfo=_FirmwareInfo_Object((1,3,6,1,4,1,28097,9,10,2),_FirmwareInfo_Type())
firmwareInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareInfo.setStatus(_A)
class _SysupgradeMissed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SysupgradeMissed_Type.__name__=_D
_SysupgradeMissed_Object=MibScalar
sysupgradeMissed=_SysupgradeMissed_Object((1,3,6,1,4,1,28097,9,10,3),_SysupgradeMissed_Type())
sysupgradeMissed.setMaxAccess(_C)
if mibBuilder.loadTexts:sysupgradeMissed.setStatus(_A)
_ServiceConfiguration_ObjectIdentity=ObjectIdentity
serviceConfiguration=_ServiceConfiguration_ObjectIdentity((1,3,6,1,4,1,28097,10))
_Sc_webserver_ObjectIdentity=ObjectIdentity
sc_webserver=_Sc_webserver_ObjectIdentity((1,3,6,1,4,1,28097,10,1))
_ConfigHttpServer_Type=DisableEnable
_ConfigHttpServer_Object=MibScalar
configHttpServer=_ConfigHttpServer_Object((1,3,6,1,4,1,28097,10,1,1),_ConfigHttpServer_Type())
configHttpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:configHttpServer.setStatus(_A)
class _ConfigHttpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigHttpServerPort_Type.__name__=_D
_ConfigHttpServerPort_Object=MibScalar
configHttpServerPort=_ConfigHttpServerPort_Object((1,3,6,1,4,1,28097,10,1,2),_ConfigHttpServerPort_Type())
configHttpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configHttpServerPort.setStatus(_A)
_ConfigHttpsServer_Type=DisableEnable
_ConfigHttpsServer_Object=MibScalar
configHttpsServer=_ConfigHttpsServer_Object((1,3,6,1,4,1,28097,10,1,3),_ConfigHttpsServer_Type())
configHttpsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:configHttpsServer.setStatus(_A)
class _ConfigHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigHttpsPort_Type.__name__=_D
_ConfigHttpsPort_Object=MibScalar
configHttpsPort=_ConfigHttpsPort_Object((1,3,6,1,4,1,28097,10,1,4),_ConfigHttpsPort_Type())
configHttpsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configHttpsPort.setStatus(_A)
_ConfigHttpsCertificate_Type=OctetString
_ConfigHttpsCertificate_Object=MibScalar
configHttpsCertificate=_ConfigHttpsCertificate_Object((1,3,6,1,4,1,28097,10,1,5),_ConfigHttpsCertificate_Type())
configHttpsCertificate.setMaxAccess(_B)
if mibBuilder.loadTexts:configHttpsCertificate.setStatus(_A)
_Sc_dhcp_ObjectIdentity=ObjectIdentity
sc_dhcp=_Sc_dhcp_ObjectIdentity((1,3,6,1,4,1,28097,10,2))
_ConfigDhcpTable_Object=MibTable
configDhcpTable=_ConfigDhcpTable_Object((1,3,6,1,4,1,28097,10,2,1))
if mibBuilder.loadTexts:configDhcpTable.setStatus(_A)
_ConfigDhcpEntry_Object=MibTableRow
configDhcpEntry=_ConfigDhcpEntry_Object((1,3,6,1,4,1,28097,10,2,1,1))
configDhcpEntry.setIndexNames((0,_E,_Af))
if mibBuilder.loadTexts:configDhcpEntry.setStatus(_A)
_ConfigDhcpSubnet_Type=NetifName
_ConfigDhcpSubnet_Object=MibTableColumn
configDhcpSubnet=_ConfigDhcpSubnet_Object((1,3,6,1,4,1,28097,10,2,1,1,1),_ConfigDhcpSubnet_Type())
configDhcpSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:configDhcpSubnet.setStatus(_A)
_ConfigDhcpRowStatus_Type=RowStatus
_ConfigDhcpRowStatus_Object=MibTableColumn
configDhcpRowStatus=_ConfigDhcpRowStatus_Object((1,3,6,1,4,1,28097,10,2,1,1,2),_ConfigDhcpRowStatus_Type())
configDhcpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configDhcpRowStatus.setStatus(_A)
_ConfigDhcpEnable_Type=DisableEnable
_ConfigDhcpEnable_Object=MibTableColumn
configDhcpEnable=_ConfigDhcpEnable_Object((1,3,6,1,4,1,28097,10,2,1,1,3),_ConfigDhcpEnable_Type())
configDhcpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configDhcpEnable.setStatus(_A)
_ConfigDhcpPoolStart_Type=Integer32
_ConfigDhcpPoolStart_Object=MibTableColumn
configDhcpPoolStart=_ConfigDhcpPoolStart_Object((1,3,6,1,4,1,28097,10,2,1,1,4),_ConfigDhcpPoolStart_Type())
configDhcpPoolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:configDhcpPoolStart.setStatus(_A)
_ConfigDhcpPoolCount_Type=Integer32
_ConfigDhcpPoolCount_Object=MibTableColumn
configDhcpPoolCount=_ConfigDhcpPoolCount_Object((1,3,6,1,4,1,28097,10,2,1,1,5),_ConfigDhcpPoolCount_Type())
configDhcpPoolCount.setMaxAccess(_B)
if mibBuilder.loadTexts:configDhcpPoolCount.setStatus(_A)
_ConfigDhcpLeaseDuration_Type=Integer32
_ConfigDhcpLeaseDuration_Object=MibTableColumn
configDhcpLeaseDuration=_ConfigDhcpLeaseDuration_Object((1,3,6,1,4,1,28097,10,2,1,1,6),_ConfigDhcpLeaseDuration_Type())
configDhcpLeaseDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:configDhcpLeaseDuration.setStatus(_A)
_Sc_ntp_ObjectIdentity=ObjectIdentity
sc_ntp=_Sc_ntp_ObjectIdentity((1,3,6,1,4,1,28097,10,3))
_ConfigNtp_Type=Integer32
_ConfigNtp_Object=MibScalar
configNtp=_ConfigNtp_Object((1,3,6,1,4,1,28097,10,3,1),_ConfigNtp_Type())
configNtp.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:configNtp.setStatus(_A)
_Sc_radius_ObjectIdentity=ObjectIdentity
sc_radius=_Sc_radius_ObjectIdentity((1,3,6,1,4,1,28097,10,4))
_Sc_snmp_ObjectIdentity=ObjectIdentity
sc_snmp=_Sc_snmp_ObjectIdentity((1,3,6,1,4,1,28097,10,5))
_Sc_dns_ObjectIdentity=ObjectIdentity
sc_dns=_Sc_dns_ObjectIdentity((1,3,6,1,4,1,28097,10,6))
_ConfigRelay_ObjectIdentity=ObjectIdentity
configRelay=_ConfigRelay_ObjectIdentity((1,3,6,1,4,1,28097,10,6,1))
_ConfigDnsRebindProtection_Type=DisableEnable
_ConfigDnsRebindProtection_Object=MibScalar
configDnsRebindProtection=_ConfigDnsRebindProtection_Object((1,3,6,1,4,1,28097,10,6,1,1),_ConfigDnsRebindProtection_Type())
configDnsRebindProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:configDnsRebindProtection.setStatus(_A)
_ConfigDnsRebindLocalhost_Type=DisableEnable
_ConfigDnsRebindLocalhost_Object=MibScalar
configDnsRebindLocalhost=_ConfigDnsRebindLocalhost_Object((1,3,6,1,4,1,28097,10,6,1,2),_ConfigDnsRebindLocalhost_Type())
configDnsRebindLocalhost.setMaxAccess(_B)
if mibBuilder.loadTexts:configDnsRebindLocalhost.setStatus(_A)
_Sc_ssh_ObjectIdentity=ObjectIdentity
sc_ssh=_Sc_ssh_ObjectIdentity((1,3,6,1,4,1,28097,10,7))
_ConfigSshEnable_Type=DisableEnable
_ConfigSshEnable_Object=MibScalar
configSshEnable=_ConfigSshEnable_Object((1,3,6,1,4,1,28097,10,7,1),_ConfigSshEnable_Type())
configSshEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configSshEnable.setStatus(_A)
_ConfigSshEnablePwd_Type=DisableEnable
_ConfigSshEnablePwd_Object=MibScalar
configSshEnablePwd=_ConfigSshEnablePwd_Object((1,3,6,1,4,1,28097,10,7,2),_ConfigSshEnablePwd_Type())
configSshEnablePwd.setMaxAccess(_B)
if mibBuilder.loadTexts:configSshEnablePwd.setStatus(_A)
_Sc_tcn_ObjectIdentity=ObjectIdentity
sc_tcn=_Sc_tcn_ObjectIdentity((1,3,6,1,4,1,28097,10,8))
_Sc_collectd_ObjectIdentity=ObjectIdentity
sc_collectd=_Sc_collectd_ObjectIdentity((1,3,6,1,4,1,28097,10,9))
_ConfigCollectdEnable_Type=DisableEnable
_ConfigCollectdEnable_Object=MibScalar
configCollectdEnable=_ConfigCollectdEnable_Object((1,3,6,1,4,1,28097,10,9,1),_ConfigCollectdEnable_Type())
configCollectdEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdEnable.setStatus(_A)
class _ConfigCollectdSamplingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ConfigCollectdSamplingInterval_Type.__name__=_D
_ConfigCollectdSamplingInterval_Object=MibScalar
configCollectdSamplingInterval=_ConfigCollectdSamplingInterval_Object((1,3,6,1,4,1,28097,10,9,2),_ConfigCollectdSamplingInterval_Type())
configCollectdSamplingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdSamplingInterval.setStatus(_A)
_Plugin_GPS_ObjectIdentity=ObjectIdentity
plugin_GPS=_Plugin_GPS_ObjectIdentity((1,3,6,1,4,1,28097,10,9,3))
_ConfigCollectdGPSEnable_Type=DisableEnable
_ConfigCollectdGPSEnable_Object=MibScalar
configCollectdGPSEnable=_ConfigCollectdGPSEnable_Object((1,3,6,1,4,1,28097,10,9,3,1),_ConfigCollectdGPSEnable_Type())
configCollectdGPSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdGPSEnable.setStatus(_A)
_ConfigCollectdGPSServerAddr_Type=IpAddress
_ConfigCollectdGPSServerAddr_Object=MibScalar
configCollectdGPSServerAddr=_ConfigCollectdGPSServerAddr_Object((1,3,6,1,4,1,28097,10,9,3,2),_ConfigCollectdGPSServerAddr_Type())
configCollectdGPSServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdGPSServerAddr.setStatus(_A)
class _ConfigCollectdGPSServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigCollectdGPSServerPort_Type.__name__=_D
_ConfigCollectdGPSServerPort_Object=MibScalar
configCollectdGPSServerPort=_ConfigCollectdGPSServerPort_Object((1,3,6,1,4,1,28097,10,9,3,3),_ConfigCollectdGPSServerPort_Type())
configCollectdGPSServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdGPSServerPort.setStatus(_A)
class _ConfigCollectdGPSConnTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ConfigCollectdGPSConnTimeout_Type.__name__=_D
_ConfigCollectdGPSConnTimeout_Object=MibScalar
configCollectdGPSConnTimeout=_ConfigCollectdGPSConnTimeout_Object((1,3,6,1,4,1,28097,10,9,3,4),_ConfigCollectdGPSConnTimeout_Type())
configCollectdGPSConnTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdGPSConnTimeout.setStatus(_A)
class _ConfigCollectdGPSReqInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ConfigCollectdGPSReqInterval_Type.__name__=_D
_ConfigCollectdGPSReqInterval_Object=MibScalar
configCollectdGPSReqInterval=_ConfigCollectdGPSReqInterval_Object((1,3,6,1,4,1,28097,10,9,3,5),_ConfigCollectdGPSReqInterval_Type())
configCollectdGPSReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdGPSReqInterval.setStatus(_A)
_Plugin_AcksysScanResult_ObjectIdentity=ObjectIdentity
plugin_AcksysScanResult=_Plugin_AcksysScanResult_ObjectIdentity((1,3,6,1,4,1,28097,10,9,4))
_ConfigCollectdWirelessScanResult_Type=DisableEnable
_ConfigCollectdWirelessScanResult_Object=MibScalar
configCollectdWirelessScanResult=_ConfigCollectdWirelessScanResult_Object((1,3,6,1,4,1,28097,10,9,4,1),_ConfigCollectdWirelessScanResult_Type())
configCollectdWirelessScanResult.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdWirelessScanResult.setStatus(_A)
_Plugin_iwinfo_ObjectIdentity=ObjectIdentity
plugin_iwinfo=_Plugin_iwinfo_ObjectIdentity((1,3,6,1,4,1,28097,10,9,5))
_ConfigCollectdIwinfo_Type=DisableEnable
_ConfigCollectdIwinfo_Object=MibScalar
configCollectdIwinfo=_ConfigCollectdIwinfo_Object((1,3,6,1,4,1,28097,10,9,5,1),_ConfigCollectdIwinfo_Type())
configCollectdIwinfo.setMaxAccess(_B)
if mibBuilder.loadTexts:configCollectdIwinfo.setStatus(_A)
_Plugin_AcksysTelemetry_ObjectIdentity=ObjectIdentity
plugin_AcksysTelemetry=_Plugin_AcksysTelemetry_ObjectIdentity((1,3,6,1,4,1,28097,10,9,6))
_ConfigAcksysTelemetryEnable_Type=DisableEnable
_ConfigAcksysTelemetryEnable_Object=MibScalar
configAcksysTelemetryEnable=_ConfigAcksysTelemetryEnable_Object((1,3,6,1,4,1,28097,10,9,6,1),_ConfigAcksysTelemetryEnable_Type())
configAcksysTelemetryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configAcksysTelemetryEnable.setStatus(_A)
class _ConfigAcksysTelemetryServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigAcksysTelemetryServerPort_Type.__name__=_D
_ConfigAcksysTelemetryServerPort_Object=MibScalar
configAcksysTelemetryServerPort=_ConfigAcksysTelemetryServerPort_Object((1,3,6,1,4,1,28097,10,9,6,2),_ConfigAcksysTelemetryServerPort_Type())
configAcksysTelemetryServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:configAcksysTelemetryServerPort.setStatus(_A)
class _ConfigAcksysTelemetryOutputInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ConfigAcksysTelemetryOutputInterval_Type.__name__=_D
_ConfigAcksysTelemetryOutputInterval_Object=MibScalar
configAcksysTelemetryOutputInterval=_ConfigAcksysTelemetryOutputInterval_Object((1,3,6,1,4,1,28097,10,9,6,3),_ConfigAcksysTelemetryOutputInterval_Type())
configAcksysTelemetryOutputInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configAcksysTelemetryOutputInterval.setStatus(_A)
class _ConfigAcksysTelemetryMaxBufferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ConfigAcksysTelemetryMaxBufferSize_Type.__name__=_D
_ConfigAcksysTelemetryMaxBufferSize_Object=MibScalar
configAcksysTelemetryMaxBufferSize=_ConfigAcksysTelemetryMaxBufferSize_Object((1,3,6,1,4,1,28097,10,9,6,4),_ConfigAcksysTelemetryMaxBufferSize_Type())
configAcksysTelemetryMaxBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:configAcksysTelemetryMaxBufferSize.setStatus(_A)
_Sc_passpoint_ObjectIdentity=ObjectIdentity
sc_passpoint=_Sc_passpoint_ObjectIdentity((1,3,6,1,4,1,28097,10,10))
_ConfigPasspointConfigTable_Object=MibTable
configPasspointConfigTable=_ConfigPasspointConfigTable_Object((1,3,6,1,4,1,28097,10,10,1))
if mibBuilder.loadTexts:configPasspointConfigTable.setStatus(_A)
_ConfigPasspointConfigEntry_Object=MibTableRow
configPasspointConfigEntry=_ConfigPasspointConfigEntry_Object((1,3,6,1,4,1,28097,10,10,1,1))
configPasspointConfigEntry.setIndexNames((0,_E,_Ag))
if mibBuilder.loadTexts:configPasspointConfigEntry.setStatus(_A)
_ConfigPasspointConfigName_Type=OctetString
_ConfigPasspointConfigName_Object=MibTableColumn
configPasspointConfigName=_ConfigPasspointConfigName_Object((1,3,6,1,4,1,28097,10,10,1,1,1),_ConfigPasspointConfigName_Type())
configPasspointConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigName.setStatus(_A)
_ConfigPasspointConfigRowStatus_Type=RowStatus
_ConfigPasspointConfigRowStatus_Object=MibTableColumn
configPasspointConfigRowStatus=_ConfigPasspointConfigRowStatus_Object((1,3,6,1,4,1,28097,10,10,1,1,2),_ConfigPasspointConfigRowStatus_Type())
configPasspointConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configPasspointConfigRowStatus.setStatus(_A)
_ConfigPasspointConfigAnqpAccessNetworkType_Type=Integer32
_ConfigPasspointConfigAnqpAccessNetworkType_Object=MibTableColumn
configPasspointConfigAnqpAccessNetworkType=_ConfigPasspointConfigAnqpAccessNetworkType_Object((1,3,6,1,4,1,28097,10,10,1,1,3),_ConfigPasspointConfigAnqpAccessNetworkType_Type())
configPasspointConfigAnqpAccessNetworkType.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpAccessNetworkType.setStatus(_A)
_ConfigPasspointConfigAnqpInternet_Type=DisableEnable
_ConfigPasspointConfigAnqpInternet_Object=MibTableColumn
configPasspointConfigAnqpInternet=_ConfigPasspointConfigAnqpInternet_Object((1,3,6,1,4,1,28097,10,10,1,1,4),_ConfigPasspointConfigAnqpInternet_Type())
configPasspointConfigAnqpInternet.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpInternet.setStatus(_A)
_ConfigPasspointConfigAnqpAsra_Type=DisableEnable
_ConfigPasspointConfigAnqpAsra_Object=MibTableColumn
configPasspointConfigAnqpAsra=_ConfigPasspointConfigAnqpAsra_Object((1,3,6,1,4,1,28097,10,10,1,1,5),_ConfigPasspointConfigAnqpAsra_Type())
configPasspointConfigAnqpAsra.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpAsra.setStatus(_A)
_ConfigPasspointConfigAnqpEsr_Type=DisableEnable
_ConfigPasspointConfigAnqpEsr_Object=MibTableColumn
configPasspointConfigAnqpEsr=_ConfigPasspointConfigAnqpEsr_Object((1,3,6,1,4,1,28097,10,10,1,1,6),_ConfigPasspointConfigAnqpEsr_Type())
configPasspointConfigAnqpEsr.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpEsr.setStatus(_A)
_ConfigPasspointConfigAnqpUesa_Type=DisableEnable
_ConfigPasspointConfigAnqpUesa_Object=MibTableColumn
configPasspointConfigAnqpUesa=_ConfigPasspointConfigAnqpUesa_Object((1,3,6,1,4,1,28097,10,10,1,1,7),_ConfigPasspointConfigAnqpUesa_Type())
configPasspointConfigAnqpUesa.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpUesa.setStatus(_A)
_ConfigPasspointConfigAnqpHessid_Type=OctetString
_ConfigPasspointConfigAnqpHessid_Object=MibTableColumn
configPasspointConfigAnqpHessid=_ConfigPasspointConfigAnqpHessid_Object((1,3,6,1,4,1,28097,10,10,1,1,8),_ConfigPasspointConfigAnqpHessid_Type())
configPasspointConfigAnqpHessid.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpHessid.setStatus(_A)
class _ConfigPasspointConfigAnqpGasAddress3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('p2p',0),('ieee80211-std',1),('non-compliant',2)))
_ConfigPasspointConfigAnqpGasAddress3_Type.__name__=_D
_ConfigPasspointConfigAnqpGasAddress3_Object=MibTableColumn
configPasspointConfigAnqpGasAddress3=_ConfigPasspointConfigAnqpGasAddress3_Object((1,3,6,1,4,1,28097,10,10,1,1,9),_ConfigPasspointConfigAnqpGasAddress3_Type())
configPasspointConfigAnqpGasAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpGasAddress3.setStatus(_A)
_ConfigPasspointConfigAnqpVenueProfile_Type=OctetString
_ConfigPasspointConfigAnqpVenueProfile_Object=MibTableColumn
configPasspointConfigAnqpVenueProfile=_ConfigPasspointConfigAnqpVenueProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,10),_ConfigPasspointConfigAnqpVenueProfile_Type())
configPasspointConfigAnqpVenueProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpVenueProfile.setStatus(_A)
_ConfigPasspointConfigAnqpRoamingConsortiumProfile_Type=OctetString
_ConfigPasspointConfigAnqpRoamingConsortiumProfile_Object=MibTableColumn
configPasspointConfigAnqpRoamingConsortiumProfile=_ConfigPasspointConfigAnqpRoamingConsortiumProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,11),_ConfigPasspointConfigAnqpRoamingConsortiumProfile_Type())
configPasspointConfigAnqpRoamingConsortiumProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpRoamingConsortiumProfile.setStatus(_A)
_ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Type=OctetString
_ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Object=MibTableColumn
configPasspointConfigAnqpNetworkAuthTypeProfile=_ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,12),_ConfigPasspointConfigAnqpNetworkAuthTypeProfile_Type())
configPasspointConfigAnqpNetworkAuthTypeProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpNetworkAuthTypeProfile.setStatus(_A)
_ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Type=OctetString
_ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Object=MibTableColumn
configPasspointConfigAnqpIpAddrTypeAvailProfile=_ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,13),_ConfigPasspointConfigAnqpIpAddrTypeAvailProfile_Type())
configPasspointConfigAnqpIpAddrTypeAvailProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpIpAddrTypeAvailProfile.setStatus(_A)
_ConfigPasspointConfigAnqpDomainNameProfile_Type=OctetString
_ConfigPasspointConfigAnqpDomainNameProfile_Object=MibTableColumn
configPasspointConfigAnqpDomainNameProfile=_ConfigPasspointConfigAnqpDomainNameProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,14),_ConfigPasspointConfigAnqpDomainNameProfile_Type())
configPasspointConfigAnqpDomainNameProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpDomainNameProfile.setStatus(_A)
_ConfigPasspointConfigAnqp3gppCellNetProfile_Type=OctetString
_ConfigPasspointConfigAnqp3gppCellNetProfile_Object=MibTableColumn
configPasspointConfigAnqp3gppCellNetProfile=_ConfigPasspointConfigAnqp3gppCellNetProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,15),_ConfigPasspointConfigAnqp3gppCellNetProfile_Type())
configPasspointConfigAnqp3gppCellNetProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqp3gppCellNetProfile.setStatus(_A)
_ConfigPasspointConfigAnqpNaiRealmProfile_Type=OctetString
_ConfigPasspointConfigAnqpNaiRealmProfile_Object=MibTableColumn
configPasspointConfigAnqpNaiRealmProfile=_ConfigPasspointConfigAnqpNaiRealmProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,16),_ConfigPasspointConfigAnqpNaiRealmProfile_Type())
configPasspointConfigAnqpNaiRealmProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpNaiRealmProfile.setStatus(_A)
_ConfigPasspointConfigAnqpOverrideElementProfile_Type=OctetString
_ConfigPasspointConfigAnqpOverrideElementProfile_Object=MibTableColumn
configPasspointConfigAnqpOverrideElementProfile=_ConfigPasspointConfigAnqpOverrideElementProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,17),_ConfigPasspointConfigAnqpOverrideElementProfile_Type())
configPasspointConfigAnqpOverrideElementProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigAnqpOverrideElementProfile.setStatus(_A)
_ConfigPasspointConfigHS20DisableDgaf_Type=DisableEnable
_ConfigPasspointConfigHS20DisableDgaf_Object=MibTableColumn
configPasspointConfigHS20DisableDgaf=_ConfigPasspointConfigHS20DisableDgaf_Object((1,3,6,1,4,1,28097,10,10,1,1,18),_ConfigPasspointConfigHS20DisableDgaf_Type())
configPasspointConfigHS20DisableDgaf.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20DisableDgaf.setStatus(_A)
_ConfigPasspointConfigHS20DomainId_Type=Integer32
_ConfigPasspointConfigHS20DomainId_Object=MibTableColumn
configPasspointConfigHS20DomainId=_ConfigPasspointConfigHS20DomainId_Object((1,3,6,1,4,1,28097,10,10,1,1,19),_ConfigPasspointConfigHS20DomainId_Type())
configPasspointConfigHS20DomainId.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20DomainId.setStatus(_A)
_ConfigPasspointConfigHS20DeauthReqTimeout_Type=Integer32
_ConfigPasspointConfigHS20DeauthReqTimeout_Object=MibTableColumn
configPasspointConfigHS20DeauthReqTimeout=_ConfigPasspointConfigHS20DeauthReqTimeout_Object((1,3,6,1,4,1,28097,10,10,1,1,20),_ConfigPasspointConfigHS20DeauthReqTimeout_Type())
configPasspointConfigHS20DeauthReqTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20DeauthReqTimeout.setStatus(_A)
_ConfigPasspointConfigHS20OsuSsid_Type=OctetString
_ConfigPasspointConfigHS20OsuSsid_Object=MibTableColumn
configPasspointConfigHS20OsuSsid=_ConfigPasspointConfigHS20OsuSsid_Object((1,3,6,1,4,1,28097,10,10,1,1,21),_ConfigPasspointConfigHS20OsuSsid_Type())
configPasspointConfigHS20OsuSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20OsuSsid.setStatus(_A)
_ConfigPasspointConfigHS20OperFriendlyNameProfile_Type=OctetString
_ConfigPasspointConfigHS20OperFriendlyNameProfile_Object=MibTableColumn
configPasspointConfigHS20OperFriendlyNameProfile=_ConfigPasspointConfigHS20OperFriendlyNameProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,22),_ConfigPasspointConfigHS20OperFriendlyNameProfile_Type())
configPasspointConfigHS20OperFriendlyNameProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20OperFriendlyNameProfile.setStatus(_A)
_ConfigPasspointConfigHS20ConnCapProfile_Type=OctetString
_ConfigPasspointConfigHS20ConnCapProfile_Object=MibTableColumn
configPasspointConfigHS20ConnCapProfile=_ConfigPasspointConfigHS20ConnCapProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,23),_ConfigPasspointConfigHS20ConnCapProfile_Type())
configPasspointConfigHS20ConnCapProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20ConnCapProfile.setStatus(_A)
_ConfigPasspointConfigHS20WanMetricsProfile_Type=OctetString
_ConfigPasspointConfigHS20WanMetricsProfile_Object=MibTableColumn
configPasspointConfigHS20WanMetricsProfile=_ConfigPasspointConfigHS20WanMetricsProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,24),_ConfigPasspointConfigHS20WanMetricsProfile_Type())
configPasspointConfigHS20WanMetricsProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20WanMetricsProfile.setStatus(_A)
_ConfigPasspointConfigHS20OperClassProfile_Type=OctetString
_ConfigPasspointConfigHS20OperClassProfile_Object=MibTableColumn
configPasspointConfigHS20OperClassProfile=_ConfigPasspointConfigHS20OperClassProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,25),_ConfigPasspointConfigHS20OperClassProfile_Type())
configPasspointConfigHS20OperClassProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20OperClassProfile.setStatus(_A)
_ConfigPasspointConfigHS20OsuProviderProfile_Type=OctetString
_ConfigPasspointConfigHS20OsuProviderProfile_Object=MibTableColumn
configPasspointConfigHS20OsuProviderProfile=_ConfigPasspointConfigHS20OsuProviderProfile_Object((1,3,6,1,4,1,28097,10,10,1,1,26),_ConfigPasspointConfigHS20OsuProviderProfile_Type())
configPasspointConfigHS20OsuProviderProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:configPasspointConfigHS20OsuProviderProfile.setStatus(_A)
_ConfigAnqpProfileVenueTable_Object=MibTable
configAnqpProfileVenueTable=_ConfigAnqpProfileVenueTable_Object((1,3,6,1,4,1,28097,10,10,2))
if mibBuilder.loadTexts:configAnqpProfileVenueTable.setStatus(_A)
_ConfigAnqpProfileVenueEntry_Object=MibTableRow
configAnqpProfileVenueEntry=_ConfigAnqpProfileVenueEntry_Object((1,3,6,1,4,1,28097,10,10,2,1))
configAnqpProfileVenueEntry.setIndexNames((0,_E,_Ah))
if mibBuilder.loadTexts:configAnqpProfileVenueEntry.setStatus(_A)
_ConfigProfileVenueName_Type=OctetString
_ConfigProfileVenueName_Object=MibTableColumn
configProfileVenueName=_ConfigProfileVenueName_Object((1,3,6,1,4,1,28097,10,10,2,1,1),_ConfigProfileVenueName_Type())
configProfileVenueName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileVenueName.setStatus(_A)
_ConfigProfileVenueRowStatus_Type=RowStatus
_ConfigProfileVenueRowStatus_Object=MibTableColumn
configProfileVenueRowStatus=_ConfigProfileVenueRowStatus_Object((1,3,6,1,4,1,28097,10,10,2,1,2),_ConfigProfileVenueRowStatus_Type())
configProfileVenueRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileVenueRowStatus.setStatus(_A)
_ConfigProfileVenueDesc_Type=OctetString
_ConfigProfileVenueDesc_Object=MibTableColumn
configProfileVenueDesc=_ConfigProfileVenueDesc_Object((1,3,6,1,4,1,28097,10,10,2,1,3),_ConfigProfileVenueDesc_Type())
configProfileVenueDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileVenueDesc.setStatus(_A)
_ConfigVenueGroup_Type=Integer32
_ConfigVenueGroup_Object=MibTableColumn
configVenueGroup=_ConfigVenueGroup_Object((1,3,6,1,4,1,28097,10,10,2,1,4),_ConfigVenueGroup_Type())
configVenueGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:configVenueGroup.setStatus(_A)
_ConfigVenueType_Type=Integer32
_ConfigVenueType_Object=MibTableColumn
configVenueType=_ConfigVenueType_Object((1,3,6,1,4,1,28097,10,10,2,1,5),_ConfigVenueType_Type())
configVenueType.setMaxAccess(_B)
if mibBuilder.loadTexts:configVenueType.setStatus(_A)
_ConfigVenueNameList_Type=OctetString
_ConfigVenueNameList_Object=MibTableColumn
configVenueNameList=_ConfigVenueNameList_Object((1,3,6,1,4,1,28097,10,10,2,1,6),_ConfigVenueNameList_Type())
configVenueNameList.setMaxAccess(_B)
if mibBuilder.loadTexts:configVenueNameList.setStatus(_A)
_ConfigAnqpProfileRoamingConsortiumTable_Object=MibTable
configAnqpProfileRoamingConsortiumTable=_ConfigAnqpProfileRoamingConsortiumTable_Object((1,3,6,1,4,1,28097,10,10,3))
if mibBuilder.loadTexts:configAnqpProfileRoamingConsortiumTable.setStatus(_A)
_ConfigAnqpProfileRoamingConsortiumEntry_Object=MibTableRow
configAnqpProfileRoamingConsortiumEntry=_ConfigAnqpProfileRoamingConsortiumEntry_Object((1,3,6,1,4,1,28097,10,10,3,1))
configAnqpProfileRoamingConsortiumEntry.setIndexNames((0,_E,_Ai))
if mibBuilder.loadTexts:configAnqpProfileRoamingConsortiumEntry.setStatus(_A)
_ConfigProfileRoamingConsortiumName_Type=OctetString
_ConfigProfileRoamingConsortiumName_Object=MibTableColumn
configProfileRoamingConsortiumName=_ConfigProfileRoamingConsortiumName_Object((1,3,6,1,4,1,28097,10,10,3,1,1),_ConfigProfileRoamingConsortiumName_Type())
configProfileRoamingConsortiumName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileRoamingConsortiumName.setStatus(_A)
_ConfigProfileRoamingConsortiumRowStatus_Type=RowStatus
_ConfigProfileRoamingConsortiumRowStatus_Object=MibTableColumn
configProfileRoamingConsortiumRowStatus=_ConfigProfileRoamingConsortiumRowStatus_Object((1,3,6,1,4,1,28097,10,10,3,1,2),_ConfigProfileRoamingConsortiumRowStatus_Type())
configProfileRoamingConsortiumRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileRoamingConsortiumRowStatus.setStatus(_A)
_ConfigProfileRoamingConsortiumDesc_Type=OctetString
_ConfigProfileRoamingConsortiumDesc_Object=MibTableColumn
configProfileRoamingConsortiumDesc=_ConfigProfileRoamingConsortiumDesc_Object((1,3,6,1,4,1,28097,10,10,3,1,3),_ConfigProfileRoamingConsortiumDesc_Type())
configProfileRoamingConsortiumDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileRoamingConsortiumDesc.setStatus(_A)
_ConfigRoamingConsortiumList_Type=OctetString
_ConfigRoamingConsortiumList_Object=MibTableColumn
configRoamingConsortiumList=_ConfigRoamingConsortiumList_Object((1,3,6,1,4,1,28097,10,10,3,1,4),_ConfigRoamingConsortiumList_Type())
configRoamingConsortiumList.setMaxAccess(_B)
if mibBuilder.loadTexts:configRoamingConsortiumList.setStatus(_A)
_ConfigAnqpProfileNetworkAuthTypeTable_Object=MibTable
configAnqpProfileNetworkAuthTypeTable=_ConfigAnqpProfileNetworkAuthTypeTable_Object((1,3,6,1,4,1,28097,10,10,4))
if mibBuilder.loadTexts:configAnqpProfileNetworkAuthTypeTable.setStatus(_A)
_ConfigAnqpProfileNetworkAuthTypeEntry_Object=MibTableRow
configAnqpProfileNetworkAuthTypeEntry=_ConfigAnqpProfileNetworkAuthTypeEntry_Object((1,3,6,1,4,1,28097,10,10,4,1))
configAnqpProfileNetworkAuthTypeEntry.setIndexNames((0,_E,_Aj))
if mibBuilder.loadTexts:configAnqpProfileNetworkAuthTypeEntry.setStatus(_A)
_ConfigProfileNetworkAuthTypeName_Type=OctetString
_ConfigProfileNetworkAuthTypeName_Object=MibTableColumn
configProfileNetworkAuthTypeName=_ConfigProfileNetworkAuthTypeName_Object((1,3,6,1,4,1,28097,10,10,4,1,1),_ConfigProfileNetworkAuthTypeName_Type())
configProfileNetworkAuthTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileNetworkAuthTypeName.setStatus(_A)
_ConfigProfileNetworkAuthTypeRowStatus_Type=RowStatus
_ConfigProfileNetworkAuthTypeRowStatus_Object=MibTableColumn
configProfileNetworkAuthTypeRowStatus=_ConfigProfileNetworkAuthTypeRowStatus_Object((1,3,6,1,4,1,28097,10,10,4,1,2),_ConfigProfileNetworkAuthTypeRowStatus_Type())
configProfileNetworkAuthTypeRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileNetworkAuthTypeRowStatus.setStatus(_A)
_ConfigProfileNetworkAuthTypeDesc_Type=OctetString
_ConfigProfileNetworkAuthTypeDesc_Object=MibTableColumn
configProfileNetworkAuthTypeDesc=_ConfigProfileNetworkAuthTypeDesc_Object((1,3,6,1,4,1,28097,10,10,4,1,3),_ConfigProfileNetworkAuthTypeDesc_Type())
configProfileNetworkAuthTypeDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileNetworkAuthTypeDesc.setStatus(_A)
_ConfigNetworkAuthType_Type=OctetString
_ConfigNetworkAuthType_Object=MibTableColumn
configNetworkAuthType=_ConfigNetworkAuthType_Object((1,3,6,1,4,1,28097,10,10,4,1,4),_ConfigNetworkAuthType_Type())
configNetworkAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:configNetworkAuthType.setStatus(_A)
_ConfigAnqpProfileIpAddrTypeAvailTable_Object=MibTable
configAnqpProfileIpAddrTypeAvailTable=_ConfigAnqpProfileIpAddrTypeAvailTable_Object((1,3,6,1,4,1,28097,10,10,5))
if mibBuilder.loadTexts:configAnqpProfileIpAddrTypeAvailTable.setStatus(_A)
_ConfigAnqpProfileIpAddrTypeAvailEntry_Object=MibTableRow
configAnqpProfileIpAddrTypeAvailEntry=_ConfigAnqpProfileIpAddrTypeAvailEntry_Object((1,3,6,1,4,1,28097,10,10,5,1))
configAnqpProfileIpAddrTypeAvailEntry.setIndexNames((0,_E,_Ak))
if mibBuilder.loadTexts:configAnqpProfileIpAddrTypeAvailEntry.setStatus(_A)
_ConfigProfileIpAddrTypeAvailName_Type=OctetString
_ConfigProfileIpAddrTypeAvailName_Object=MibTableColumn
configProfileIpAddrTypeAvailName=_ConfigProfileIpAddrTypeAvailName_Object((1,3,6,1,4,1,28097,10,10,5,1,1),_ConfigProfileIpAddrTypeAvailName_Type())
configProfileIpAddrTypeAvailName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileIpAddrTypeAvailName.setStatus(_A)
_ConfigProfileIpAddrTypeAvailRowStatus_Type=RowStatus
_ConfigProfileIpAddrTypeAvailRowStatus_Object=MibTableColumn
configProfileIpAddrTypeAvailRowStatus=_ConfigProfileIpAddrTypeAvailRowStatus_Object((1,3,6,1,4,1,28097,10,10,5,1,2),_ConfigProfileIpAddrTypeAvailRowStatus_Type())
configProfileIpAddrTypeAvailRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileIpAddrTypeAvailRowStatus.setStatus(_A)
_ConfigProfileIpAddrTypeAvailDesc_Type=OctetString
_ConfigProfileIpAddrTypeAvailDesc_Object=MibTableColumn
configProfileIpAddrTypeAvailDesc=_ConfigProfileIpAddrTypeAvailDesc_Object((1,3,6,1,4,1,28097,10,10,5,1,3),_ConfigProfileIpAddrTypeAvailDesc_Type())
configProfileIpAddrTypeAvailDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileIpAddrTypeAvailDesc.setStatus(_A)
_ConfigIpv4Type_Type=Integer32
_ConfigIpv4Type_Object=MibTableColumn
configIpv4Type=_ConfigIpv4Type_Object((1,3,6,1,4,1,28097,10,10,5,1,4),_ConfigIpv4Type_Type())
configIpv4Type.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpv4Type.setStatus(_A)
_ConfigIpv6Type_Type=Integer32
_ConfigIpv6Type_Object=MibTableColumn
configIpv6Type=_ConfigIpv6Type_Object((1,3,6,1,4,1,28097,10,10,5,1,5),_ConfigIpv6Type_Type())
configIpv6Type.setMaxAccess(_B)
if mibBuilder.loadTexts:configIpv6Type.setStatus(_A)
_ConfigAnqpProfileDomainNameTable_Object=MibTable
configAnqpProfileDomainNameTable=_ConfigAnqpProfileDomainNameTable_Object((1,3,6,1,4,1,28097,10,10,6))
if mibBuilder.loadTexts:configAnqpProfileDomainNameTable.setStatus(_A)
_ConfigAnqpProfileDomainNameEntry_Object=MibTableRow
configAnqpProfileDomainNameEntry=_ConfigAnqpProfileDomainNameEntry_Object((1,3,6,1,4,1,28097,10,10,6,1))
configAnqpProfileDomainNameEntry.setIndexNames((0,_E,_Al))
if mibBuilder.loadTexts:configAnqpProfileDomainNameEntry.setStatus(_A)
_ConfigProfileDomainNameName_Type=OctetString
_ConfigProfileDomainNameName_Object=MibTableColumn
configProfileDomainNameName=_ConfigProfileDomainNameName_Object((1,3,6,1,4,1,28097,10,10,6,1,1),_ConfigProfileDomainNameName_Type())
configProfileDomainNameName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileDomainNameName.setStatus(_A)
_ConfigProfileDomainNameRowStatus_Type=RowStatus
_ConfigProfileDomainNameRowStatus_Object=MibTableColumn
configProfileDomainNameRowStatus=_ConfigProfileDomainNameRowStatus_Object((1,3,6,1,4,1,28097,10,10,6,1,2),_ConfigProfileDomainNameRowStatus_Type())
configProfileDomainNameRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileDomainNameRowStatus.setStatus(_A)
_ConfigProfileDomainNameDesc_Type=OctetString
_ConfigProfileDomainNameDesc_Object=MibTableColumn
configProfileDomainNameDesc=_ConfigProfileDomainNameDesc_Object((1,3,6,1,4,1,28097,10,10,6,1,3),_ConfigProfileDomainNameDesc_Type())
configProfileDomainNameDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileDomainNameDesc.setStatus(_A)
_ConfigDomainNameList_Type=OctetString
_ConfigDomainNameList_Object=MibTableColumn
configDomainNameList=_ConfigDomainNameList_Object((1,3,6,1,4,1,28097,10,10,6,1,4),_ConfigDomainNameList_Type())
configDomainNameList.setMaxAccess(_B)
if mibBuilder.loadTexts:configDomainNameList.setStatus(_A)
_ConfigAnqpProfile3gppCellNetTable_Object=MibTable
configAnqpProfile3gppCellNetTable=_ConfigAnqpProfile3gppCellNetTable_Object((1,3,6,1,4,1,28097,10,10,7))
if mibBuilder.loadTexts:configAnqpProfile3gppCellNetTable.setStatus(_A)
_ConfigAnqpProfile3gppCellNetEntry_Object=MibTableRow
configAnqpProfile3gppCellNetEntry=_ConfigAnqpProfile3gppCellNetEntry_Object((1,3,6,1,4,1,28097,10,10,7,1))
configAnqpProfile3gppCellNetEntry.setIndexNames((0,_E,_Am))
if mibBuilder.loadTexts:configAnqpProfile3gppCellNetEntry.setStatus(_A)
_ConfigProfile3gppCellNetName_Type=OctetString
_ConfigProfile3gppCellNetName_Object=MibTableColumn
configProfile3gppCellNetName=_ConfigProfile3gppCellNetName_Object((1,3,6,1,4,1,28097,10,10,7,1,1),_ConfigProfile3gppCellNetName_Type())
configProfile3gppCellNetName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfile3gppCellNetName.setStatus(_A)
_ConfigProfile3gppCellNetRowStatus_Type=RowStatus
_ConfigProfile3gppCellNetRowStatus_Object=MibTableColumn
configProfile3gppCellNetRowStatus=_ConfigProfile3gppCellNetRowStatus_Object((1,3,6,1,4,1,28097,10,10,7,1,2),_ConfigProfile3gppCellNetRowStatus_Type())
configProfile3gppCellNetRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfile3gppCellNetRowStatus.setStatus(_A)
_ConfigProfile3gppCellNetDesc_Type=OctetString
_ConfigProfile3gppCellNetDesc_Object=MibTableColumn
configProfile3gppCellNetDesc=_ConfigProfile3gppCellNetDesc_Object((1,3,6,1,4,1,28097,10,10,7,1,3),_ConfigProfile3gppCellNetDesc_Type())
configProfile3gppCellNetDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfile3gppCellNetDesc.setStatus(_A)
_Config3gppCellNetList_Type=OctetString
_Config3gppCellNetList_Object=MibTableColumn
config3gppCellNetList=_Config3gppCellNetList_Object((1,3,6,1,4,1,28097,10,10,7,1,4),_Config3gppCellNetList_Type())
config3gppCellNetList.setMaxAccess(_B)
if mibBuilder.loadTexts:config3gppCellNetList.setStatus(_A)
_ConfigAnqpProfileNaiRealmTable_Object=MibTable
configAnqpProfileNaiRealmTable=_ConfigAnqpProfileNaiRealmTable_Object((1,3,6,1,4,1,28097,10,10,8))
if mibBuilder.loadTexts:configAnqpProfileNaiRealmTable.setStatus(_A)
_ConfigAnqpProfileNaiRealmEntry_Object=MibTableRow
configAnqpProfileNaiRealmEntry=_ConfigAnqpProfileNaiRealmEntry_Object((1,3,6,1,4,1,28097,10,10,8,1))
configAnqpProfileNaiRealmEntry.setIndexNames((0,_E,_An))
if mibBuilder.loadTexts:configAnqpProfileNaiRealmEntry.setStatus(_A)
_ConfigProfileNaiRealmName_Type=OctetString
_ConfigProfileNaiRealmName_Object=MibTableColumn
configProfileNaiRealmName=_ConfigProfileNaiRealmName_Object((1,3,6,1,4,1,28097,10,10,8,1,1),_ConfigProfileNaiRealmName_Type())
configProfileNaiRealmName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileNaiRealmName.setStatus(_A)
_ConfigProfileNaiRealmRowStatus_Type=RowStatus
_ConfigProfileNaiRealmRowStatus_Object=MibTableColumn
configProfileNaiRealmRowStatus=_ConfigProfileNaiRealmRowStatus_Object((1,3,6,1,4,1,28097,10,10,8,1,2),_ConfigProfileNaiRealmRowStatus_Type())
configProfileNaiRealmRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileNaiRealmRowStatus.setStatus(_A)
_ConfigProfileNaiRealmDesc_Type=OctetString
_ConfigProfileNaiRealmDesc_Object=MibTableColumn
configProfileNaiRealmDesc=_ConfigProfileNaiRealmDesc_Object((1,3,6,1,4,1,28097,10,10,8,1,3),_ConfigProfileNaiRealmDesc_Type())
configProfileNaiRealmDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileNaiRealmDesc.setStatus(_A)
_ConfigNaiRealmEncode_Type=DisableEnable
_ConfigNaiRealmEncode_Object=MibTableColumn
configNaiRealmEncode=_ConfigNaiRealmEncode_Object((1,3,6,1,4,1,28097,10,10,8,1,4),_ConfigNaiRealmEncode_Type())
configNaiRealmEncode.setMaxAccess(_B)
if mibBuilder.loadTexts:configNaiRealmEncode.setStatus(_A)
_ConfigNaiRealmRealmList_Type=OctetString
_ConfigNaiRealmRealmList_Object=MibTableColumn
configNaiRealmRealmList=_ConfigNaiRealmRealmList_Object((1,3,6,1,4,1,28097,10,10,8,1,5),_ConfigNaiRealmRealmList_Type())
configNaiRealmRealmList.setMaxAccess(_B)
if mibBuilder.loadTexts:configNaiRealmRealmList.setStatus(_A)
_ConfigNaiRealmEap_Type=OctetString
_ConfigNaiRealmEap_Object=MibTableColumn
configNaiRealmEap=_ConfigNaiRealmEap_Object((1,3,6,1,4,1,28097,10,10,8,1,6),_ConfigNaiRealmEap_Type())
configNaiRealmEap.setMaxAccess(_B)
if mibBuilder.loadTexts:configNaiRealmEap.setStatus(_A)
_ConfigAnqpProfileOverrideElementTable_Object=MibTable
configAnqpProfileOverrideElementTable=_ConfigAnqpProfileOverrideElementTable_Object((1,3,6,1,4,1,28097,10,10,9))
if mibBuilder.loadTexts:configAnqpProfileOverrideElementTable.setStatus(_A)
_ConfigAnqpProfileOverrideElementEntry_Object=MibTableRow
configAnqpProfileOverrideElementEntry=_ConfigAnqpProfileOverrideElementEntry_Object((1,3,6,1,4,1,28097,10,10,9,1))
configAnqpProfileOverrideElementEntry.setIndexNames((0,_E,_Ao))
if mibBuilder.loadTexts:configAnqpProfileOverrideElementEntry.setStatus(_A)
_ConfigProfileOverrideElementName_Type=OctetString
_ConfigProfileOverrideElementName_Object=MibTableColumn
configProfileOverrideElementName=_ConfigProfileOverrideElementName_Object((1,3,6,1,4,1,28097,10,10,9,1,1),_ConfigProfileOverrideElementName_Type())
configProfileOverrideElementName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileOverrideElementName.setStatus(_A)
_ConfigProfileOverrideElementRowStatus_Type=RowStatus
_ConfigProfileOverrideElementRowStatus_Object=MibTableColumn
configProfileOverrideElementRowStatus=_ConfigProfileOverrideElementRowStatus_Object((1,3,6,1,4,1,28097,10,10,9,1,2),_ConfigProfileOverrideElementRowStatus_Type())
configProfileOverrideElementRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileOverrideElementRowStatus.setStatus(_A)
_ConfigProfileOverrideElementDesc_Type=OctetString
_ConfigProfileOverrideElementDesc_Object=MibTableColumn
configProfileOverrideElementDesc=_ConfigProfileOverrideElementDesc_Object((1,3,6,1,4,1,28097,10,10,9,1,3),_ConfigProfileOverrideElementDesc_Type())
configProfileOverrideElementDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileOverrideElementDesc.setStatus(_A)
_ConfigAnqpOverrideList_Type=OctetString
_ConfigAnqpOverrideList_Object=MibTableColumn
configAnqpOverrideList=_ConfigAnqpOverrideList_Object((1,3,6,1,4,1,28097,10,10,9,1,4),_ConfigAnqpOverrideList_Type())
configAnqpOverrideList.setMaxAccess(_B)
if mibBuilder.loadTexts:configAnqpOverrideList.setStatus(_A)
_ConfigHS20ProfileOperFriendlyNameTable_Object=MibTable
configHS20ProfileOperFriendlyNameTable=_ConfigHS20ProfileOperFriendlyNameTable_Object((1,3,6,1,4,1,28097,10,10,10))
if mibBuilder.loadTexts:configHS20ProfileOperFriendlyNameTable.setStatus(_A)
_ConfigHS20ProfileOperFriendlyNameEntry_Object=MibTableRow
configHS20ProfileOperFriendlyNameEntry=_ConfigHS20ProfileOperFriendlyNameEntry_Object((1,3,6,1,4,1,28097,10,10,10,1))
configHS20ProfileOperFriendlyNameEntry.setIndexNames((0,_E,_Ap))
if mibBuilder.loadTexts:configHS20ProfileOperFriendlyNameEntry.setStatus(_A)
_ConfigProfileOperFriendlyNameName_Type=OctetString
_ConfigProfileOperFriendlyNameName_Object=MibTableColumn
configProfileOperFriendlyNameName=_ConfigProfileOperFriendlyNameName_Object((1,3,6,1,4,1,28097,10,10,10,1,1),_ConfigProfileOperFriendlyNameName_Type())
configProfileOperFriendlyNameName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileOperFriendlyNameName.setStatus(_A)
_ConfigProfileOperFriendlyNameRowStatus_Type=RowStatus
_ConfigProfileOperFriendlyNameRowStatus_Object=MibTableColumn
configProfileOperFriendlyNameRowStatus=_ConfigProfileOperFriendlyNameRowStatus_Object((1,3,6,1,4,1,28097,10,10,10,1,2),_ConfigProfileOperFriendlyNameRowStatus_Type())
configProfileOperFriendlyNameRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileOperFriendlyNameRowStatus.setStatus(_A)
_ConfigProfileOperFriendlyNameDesc_Type=OctetString
_ConfigProfileOperFriendlyNameDesc_Object=MibTableColumn
configProfileOperFriendlyNameDesc=_ConfigProfileOperFriendlyNameDesc_Object((1,3,6,1,4,1,28097,10,10,10,1,3),_ConfigProfileOperFriendlyNameDesc_Type())
configProfileOperFriendlyNameDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileOperFriendlyNameDesc.setStatus(_A)
_ConfigFriendlyNameList_Type=OctetString
_ConfigFriendlyNameList_Object=MibTableColumn
configFriendlyNameList=_ConfigFriendlyNameList_Object((1,3,6,1,4,1,28097,10,10,10,1,4),_ConfigFriendlyNameList_Type())
configFriendlyNameList.setMaxAccess(_B)
if mibBuilder.loadTexts:configFriendlyNameList.setStatus(_A)
_ConfigHS20ProfileConnCapTable_Object=MibTable
configHS20ProfileConnCapTable=_ConfigHS20ProfileConnCapTable_Object((1,3,6,1,4,1,28097,10,10,11))
if mibBuilder.loadTexts:configHS20ProfileConnCapTable.setStatus(_A)
_ConfigHS20ProfileConnCapEntry_Object=MibTableRow
configHS20ProfileConnCapEntry=_ConfigHS20ProfileConnCapEntry_Object((1,3,6,1,4,1,28097,10,10,11,1))
configHS20ProfileConnCapEntry.setIndexNames((0,_E,_Aq))
if mibBuilder.loadTexts:configHS20ProfileConnCapEntry.setStatus(_A)
_ConfigProfileConnCapName_Type=OctetString
_ConfigProfileConnCapName_Object=MibTableColumn
configProfileConnCapName=_ConfigProfileConnCapName_Object((1,3,6,1,4,1,28097,10,10,11,1,1),_ConfigProfileConnCapName_Type())
configProfileConnCapName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileConnCapName.setStatus(_A)
_ConfigProfileConnCapRowStatus_Type=RowStatus
_ConfigProfileConnCapRowStatus_Object=MibTableColumn
configProfileConnCapRowStatus=_ConfigProfileConnCapRowStatus_Object((1,3,6,1,4,1,28097,10,10,11,1,2),_ConfigProfileConnCapRowStatus_Type())
configProfileConnCapRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileConnCapRowStatus.setStatus(_A)
_ConfigProfileConnCapDesc_Type=OctetString
_ConfigProfileConnCapDesc_Object=MibTableColumn
configProfileConnCapDesc=_ConfigProfileConnCapDesc_Object((1,3,6,1,4,1,28097,10,10,11,1,3),_ConfigProfileConnCapDesc_Type())
configProfileConnCapDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileConnCapDesc.setStatus(_A)
_ConfigConnCapabList_Type=OctetString
_ConfigConnCapabList_Object=MibTableColumn
configConnCapabList=_ConfigConnCapabList_Object((1,3,6,1,4,1,28097,10,10,11,1,4),_ConfigConnCapabList_Type())
configConnCapabList.setMaxAccess(_B)
if mibBuilder.loadTexts:configConnCapabList.setStatus(_A)
_ConfigHS20ProfileWanMetricsTable_Object=MibTable
configHS20ProfileWanMetricsTable=_ConfigHS20ProfileWanMetricsTable_Object((1,3,6,1,4,1,28097,10,10,12))
if mibBuilder.loadTexts:configHS20ProfileWanMetricsTable.setStatus(_A)
_ConfigHS20ProfileWanMetricsEntry_Object=MibTableRow
configHS20ProfileWanMetricsEntry=_ConfigHS20ProfileWanMetricsEntry_Object((1,3,6,1,4,1,28097,10,10,12,1))
configHS20ProfileWanMetricsEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:configHS20ProfileWanMetricsEntry.setStatus(_A)
_ConfigProfileWanMetricsName_Type=OctetString
_ConfigProfileWanMetricsName_Object=MibTableColumn
configProfileWanMetricsName=_ConfigProfileWanMetricsName_Object((1,3,6,1,4,1,28097,10,10,12,1,1),_ConfigProfileWanMetricsName_Type())
configProfileWanMetricsName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileWanMetricsName.setStatus(_A)
_ConfigProfileWanMetricsRowStatus_Type=RowStatus
_ConfigProfileWanMetricsRowStatus_Object=MibTableColumn
configProfileWanMetricsRowStatus=_ConfigProfileWanMetricsRowStatus_Object((1,3,6,1,4,1,28097,10,10,12,1,2),_ConfigProfileWanMetricsRowStatus_Type())
configProfileWanMetricsRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileWanMetricsRowStatus.setStatus(_A)
_ConfigProfileWanMetricsDesc_Type=OctetString
_ConfigProfileWanMetricsDesc_Object=MibTableColumn
configProfileWanMetricsDesc=_ConfigProfileWanMetricsDesc_Object((1,3,6,1,4,1,28097,10,10,12,1,3),_ConfigProfileWanMetricsDesc_Type())
configProfileWanMetricsDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileWanMetricsDesc.setStatus(_A)
_ConfigLinkStatus_Type=Integer32
_ConfigLinkStatus_Object=MibTableColumn
configLinkStatus=_ConfigLinkStatus_Object((1,3,6,1,4,1,28097,10,10,12,1,4),_ConfigLinkStatus_Type())
configLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configLinkStatus.setStatus(_A)
_ConfigSymmetric_Type=DisableEnable
_ConfigSymmetric_Object=MibTableColumn
configSymmetric=_ConfigSymmetric_Object((1,3,6,1,4,1,28097,10,10,12,1,5),_ConfigSymmetric_Type())
configSymmetric.setMaxAccess(_B)
if mibBuilder.loadTexts:configSymmetric.setStatus(_A)
_ConfigAtCapacity_Type=DisableEnable
_ConfigAtCapacity_Object=MibTableColumn
configAtCapacity=_ConfigAtCapacity_Object((1,3,6,1,4,1,28097,10,10,12,1,6),_ConfigAtCapacity_Type())
configAtCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:configAtCapacity.setStatus(_A)
_ConfigDownSpeed_Type=Integer32
_ConfigDownSpeed_Object=MibTableColumn
configDownSpeed=_ConfigDownSpeed_Object((1,3,6,1,4,1,28097,10,10,12,1,7),_ConfigDownSpeed_Type())
configDownSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:configDownSpeed.setStatus(_A)
_ConfigUpSpeed_Type=Integer32
_ConfigUpSpeed_Object=MibTableColumn
configUpSpeed=_ConfigUpSpeed_Object((1,3,6,1,4,1,28097,10,10,12,1,8),_ConfigUpSpeed_Type())
configUpSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:configUpSpeed.setStatus(_A)
_ConfigDownLoad_Type=Integer32
_ConfigDownLoad_Object=MibTableColumn
configDownLoad=_ConfigDownLoad_Object((1,3,6,1,4,1,28097,10,10,12,1,9),_ConfigDownLoad_Type())
configDownLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:configDownLoad.setStatus(_A)
_ConfigUpLoad_Type=Integer32
_ConfigUpLoad_Object=MibTableColumn
configUpLoad=_ConfigUpLoad_Object((1,3,6,1,4,1,28097,10,10,12,1,10),_ConfigUpLoad_Type())
configUpLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:configUpLoad.setStatus(_A)
_ConfigLMD_Type=Integer32
_ConfigLMD_Object=MibTableColumn
configLMD=_ConfigLMD_Object((1,3,6,1,4,1,28097,10,10,12,1,11),_ConfigLMD_Type())
configLMD.setMaxAccess(_B)
if mibBuilder.loadTexts:configLMD.setStatus(_A)
_ConfigHS20ProfileOperClassTable_Object=MibTable
configHS20ProfileOperClassTable=_ConfigHS20ProfileOperClassTable_Object((1,3,6,1,4,1,28097,10,10,13))
if mibBuilder.loadTexts:configHS20ProfileOperClassTable.setStatus(_A)
_ConfigHS20ProfileOperClassEntry_Object=MibTableRow
configHS20ProfileOperClassEntry=_ConfigHS20ProfileOperClassEntry_Object((1,3,6,1,4,1,28097,10,10,13,1))
configHS20ProfileOperClassEntry.setIndexNames((0,_E,_As))
if mibBuilder.loadTexts:configHS20ProfileOperClassEntry.setStatus(_A)
_ConfigProfileOperClassName_Type=OctetString
_ConfigProfileOperClassName_Object=MibTableColumn
configProfileOperClassName=_ConfigProfileOperClassName_Object((1,3,6,1,4,1,28097,10,10,13,1,1),_ConfigProfileOperClassName_Type())
configProfileOperClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileOperClassName.setStatus(_A)
_ConfigProfileOperClassRowStatus_Type=RowStatus
_ConfigProfileOperClassRowStatus_Object=MibTableColumn
configProfileOperClassRowStatus=_ConfigProfileOperClassRowStatus_Object((1,3,6,1,4,1,28097,10,10,13,1,2),_ConfigProfileOperClassRowStatus_Type())
configProfileOperClassRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileOperClassRowStatus.setStatus(_A)
_ConfigProfileOperClassDesc_Type=OctetString
_ConfigProfileOperClassDesc_Object=MibTableColumn
configProfileOperClassDesc=_ConfigProfileOperClassDesc_Object((1,3,6,1,4,1,28097,10,10,13,1,3),_ConfigProfileOperClassDesc_Type())
configProfileOperClassDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileOperClassDesc.setStatus(_A)
_ConfigOperClassList_Type=OctetString
_ConfigOperClassList_Object=MibTableColumn
configOperClassList=_ConfigOperClassList_Object((1,3,6,1,4,1,28097,10,10,13,1,4),_ConfigOperClassList_Type())
configOperClassList.setMaxAccess(_B)
if mibBuilder.loadTexts:configOperClassList.setStatus(_A)
_ConfigHS20ProfileOsuProviderTable_Object=MibTable
configHS20ProfileOsuProviderTable=_ConfigHS20ProfileOsuProviderTable_Object((1,3,6,1,4,1,28097,10,10,14))
if mibBuilder.loadTexts:configHS20ProfileOsuProviderTable.setStatus(_A)
_ConfigHS20ProfileOsuProviderEntry_Object=MibTableRow
configHS20ProfileOsuProviderEntry=_ConfigHS20ProfileOsuProviderEntry_Object((1,3,6,1,4,1,28097,10,10,14,1))
configHS20ProfileOsuProviderEntry.setIndexNames((0,_E,_At))
if mibBuilder.loadTexts:configHS20ProfileOsuProviderEntry.setStatus(_A)
_ConfigProfileOsuProviderName_Type=OctetString
_ConfigProfileOsuProviderName_Object=MibTableColumn
configProfileOsuProviderName=_ConfigProfileOsuProviderName_Object((1,3,6,1,4,1,28097,10,10,14,1,1),_ConfigProfileOsuProviderName_Type())
configProfileOsuProviderName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileOsuProviderName.setStatus(_A)
_ConfigProfileOsuProviderRowStatus_Type=RowStatus
_ConfigProfileOsuProviderRowStatus_Object=MibTableColumn
configProfileOsuProviderRowStatus=_ConfigProfileOsuProviderRowStatus_Object((1,3,6,1,4,1,28097,10,10,14,1,2),_ConfigProfileOsuProviderRowStatus_Type())
configProfileOsuProviderRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileOsuProviderRowStatus.setStatus(_A)
_ConfigProfileOsuProviderDesc_Type=OctetString
_ConfigProfileOsuProviderDesc_Object=MibTableColumn
configProfileOsuProviderDesc=_ConfigProfileOsuProviderDesc_Object((1,3,6,1,4,1,28097,10,10,14,1,3),_ConfigProfileOsuProviderDesc_Type())
configProfileOsuProviderDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileOsuProviderDesc.setStatus(_A)
_ConfigOsuServerUri_Type=OctetString
_ConfigOsuServerUri_Object=MibTableColumn
configOsuServerUri=_ConfigOsuServerUri_Object((1,3,6,1,4,1,28097,10,10,14,1,4),_ConfigOsuServerUri_Type())
configOsuServerUri.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuServerUri.setStatus(_A)
_ConfigOsuFriendlyNameList_Type=OctetString
_ConfigOsuFriendlyNameList_Object=MibTableColumn
configOsuFriendlyNameList=_ConfigOsuFriendlyNameList_Object((1,3,6,1,4,1,28097,10,10,14,1,5),_ConfigOsuFriendlyNameList_Type())
configOsuFriendlyNameList.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuFriendlyNameList.setStatus(_A)
_ConfigOsuNai_Type=OctetString
_ConfigOsuNai_Object=MibTableColumn
configOsuNai=_ConfigOsuNai_Object((1,3,6,1,4,1,28097,10,10,14,1,6),_ConfigOsuNai_Type())
configOsuNai.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuNai.setStatus(_A)
_ConfigOsuOmaDm_Type=DisableEnable
_ConfigOsuOmaDm_Object=MibTableColumn
configOsuOmaDm=_ConfigOsuOmaDm_Object((1,3,6,1,4,1,28097,10,10,14,1,7),_ConfigOsuOmaDm_Type())
configOsuOmaDm.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuOmaDm.setStatus(_A)
_ConfigOsuSoapXml_Type=DisableEnable
_ConfigOsuSoapXml_Object=MibTableColumn
configOsuSoapXml=_ConfigOsuSoapXml_Object((1,3,6,1,4,1,28097,10,10,14,1,8),_ConfigOsuSoapXml_Type())
configOsuSoapXml.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuSoapXml.setStatus(_A)
_ConfigOsuIconProfileList_Type=OctetString
_ConfigOsuIconProfileList_Object=MibTableColumn
configOsuIconProfileList=_ConfigOsuIconProfileList_Object((1,3,6,1,4,1,28097,10,10,14,1,9),_ConfigOsuIconProfileList_Type())
configOsuIconProfileList.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuIconProfileList.setStatus(_A)
_ConfigOsuServiceDescList_Type=OctetString
_ConfigOsuServiceDescList_Object=MibTableColumn
configOsuServiceDescList=_ConfigOsuServiceDescList_Object((1,3,6,1,4,1,28097,10,10,14,1,10),_ConfigOsuServiceDescList_Type())
configOsuServiceDescList.setMaxAccess(_B)
if mibBuilder.loadTexts:configOsuServiceDescList.setStatus(_A)
_ConfigProfileIconTable_Object=MibTable
configProfileIconTable=_ConfigProfileIconTable_Object((1,3,6,1,4,1,28097,10,10,15))
if mibBuilder.loadTexts:configProfileIconTable.setStatus(_A)
_ConfigProfileIconEntry_Object=MibTableRow
configProfileIconEntry=_ConfigProfileIconEntry_Object((1,3,6,1,4,1,28097,10,10,15,1))
configProfileIconEntry.setIndexNames((0,_E,_Au))
if mibBuilder.loadTexts:configProfileIconEntry.setStatus(_A)
_ConfigProfileIconName_Type=OctetString
_ConfigProfileIconName_Object=MibTableColumn
configProfileIconName=_ConfigProfileIconName_Object((1,3,6,1,4,1,28097,10,10,15,1,1),_ConfigProfileIconName_Type())
configProfileIconName.setMaxAccess(_C)
if mibBuilder.loadTexts:configProfileIconName.setStatus(_A)
_ConfigProfileIconRowStatus_Type=RowStatus
_ConfigProfileIconRowStatus_Object=MibTableColumn
configProfileIconRowStatus=_ConfigProfileIconRowStatus_Object((1,3,6,1,4,1,28097,10,10,15,1,2),_ConfigProfileIconRowStatus_Type())
configProfileIconRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configProfileIconRowStatus.setStatus(_A)
_ConfigProfileIconDesc_Type=OctetString
_ConfigProfileIconDesc_Object=MibTableColumn
configProfileIconDesc=_ConfigProfileIconDesc_Object((1,3,6,1,4,1,28097,10,10,15,1,3),_ConfigProfileIconDesc_Type())
configProfileIconDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:configProfileIconDesc.setStatus(_A)
_ConfigIconLang_Type=OctetString
_ConfigIconLang_Object=MibTableColumn
configIconLang=_ConfigIconLang_Object((1,3,6,1,4,1,28097,10,10,15,1,4),_ConfigIconLang_Type())
configIconLang.setMaxAccess(_B)
if mibBuilder.loadTexts:configIconLang.setStatus(_A)
_ConfigIconSize_Type=OctetString
_ConfigIconSize_Object=MibTableColumn
configIconSize=_ConfigIconSize_Object((1,3,6,1,4,1,28097,10,10,15,1,5),_ConfigIconSize_Type())
configIconSize.setMaxAccess(_B)
if mibBuilder.loadTexts:configIconSize.setStatus(_A)
_ConfigIconType_Type=OctetString
_ConfigIconType_Object=MibTableColumn
configIconType=_ConfigIconType_Object((1,3,6,1,4,1,28097,10,10,15,1,6),_ConfigIconType_Type())
configIconType.setMaxAccess(_B)
if mibBuilder.loadTexts:configIconType.setStatus(_A)
_ConfigIconPath_Type=OctetString
_ConfigIconPath_Object=MibTableColumn
configIconPath=_ConfigIconPath_Object((1,3,6,1,4,1,28097,10,10,15,1,7),_ConfigIconPath_Type())
configIconPath.setMaxAccess(_C)
if mibBuilder.loadTexts:configIconPath.setStatus(_A)
_ConfigIconFileContent_Type=OctetString
_ConfigIconFileContent_Object=MibTableColumn
configIconFileContent=_ConfigIconFileContent_Object((1,3,6,1,4,1,28097,10,10,15,1,8),_ConfigIconFileContent_Type())
configIconFileContent.setMaxAccess(_B)
if mibBuilder.loadTexts:configIconFileContent.setStatus(_A)
_Sc_async_sysupgrade_ObjectIdentity=ObjectIdentity
sc_async_sysupgrade=_Sc_async_sysupgrade_ObjectIdentity((1,3,6,1,4,1,28097,10,11))
class _ConfigAsyncUpgradeDoUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('execute',2))
_ConfigAsyncUpgradeDoUpgrade_Type.__name__=_D
_ConfigAsyncUpgradeDoUpgrade_Object=MibScalar
configAsyncUpgradeDoUpgrade=_ConfigAsyncUpgradeDoUpgrade_Object((1,3,6,1,4,1,28097,10,11,1),_ConfigAsyncUpgradeDoUpgrade_Type())
configAsyncUpgradeDoUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:configAsyncUpgradeDoUpgrade.setStatus(_A)
_ConfigAsyncUpgradeTimerEnable_Type=DisableEnable
_ConfigAsyncUpgradeTimerEnable_Object=MibScalar
configAsyncUpgradeTimerEnable=_ConfigAsyncUpgradeTimerEnable_Object((1,3,6,1,4,1,28097,10,11,2),_ConfigAsyncUpgradeTimerEnable_Type())
configAsyncUpgradeTimerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:configAsyncUpgradeTimerEnable.setStatus(_A)
class _ConfigAsyncUpgradeTimerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,100)));namedValues=NamedValues(*(('no-retry',1),('retry-immediately',2),('retry-after-24h',3),('missed-upgrade-retry-after-24h',100)))
_ConfigAsyncUpgradeTimerMode_Type.__name__=_D
_ConfigAsyncUpgradeTimerMode_Object=MibScalar
configAsyncUpgradeTimerMode=_ConfigAsyncUpgradeTimerMode_Object((1,3,6,1,4,1,28097,10,11,3),_ConfigAsyncUpgradeTimerMode_Type())
configAsyncUpgradeTimerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:configAsyncUpgradeTimerMode.setStatus(_A)
_ConfigAsyncUpgradeTimerMinute_Type=Integer32
_ConfigAsyncUpgradeTimerMinute_Object=MibScalar
configAsyncUpgradeTimerMinute=_ConfigAsyncUpgradeTimerMinute_Object((1,3,6,1,4,1,28097,10,11,4),_ConfigAsyncUpgradeTimerMinute_Type())
configAsyncUpgradeTimerMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:configAsyncUpgradeTimerMinute.setStatus(_A)
_Sc_md5sum_ObjectIdentity=ObjectIdentity
sc_md5sum=_Sc_md5sum_ObjectIdentity((1,3,6,1,4,1,28097,10,12))
_ConfigMD5SUMstatus_Type=Integer32
_ConfigMD5SUMstatus_Object=MibScalar
configMD5SUMstatus=_ConfigMD5SUMstatus_Object((1,3,6,1,4,1,28097,10,12,1),_ConfigMD5SUMstatus_Type())
configMD5SUMstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configMD5SUMstatus.setStatus(_A)
_ConfigMD5SUMfiles_Type=DisplayString
_ConfigMD5SUMfiles_Object=MibScalar
configMD5SUMfiles=_ConfigMD5SUMfiles_Object((1,3,6,1,4,1,28097,10,12,2),_ConfigMD5SUMfiles_Type())
configMD5SUMfiles.setMaxAccess(_C)
if mibBuilder.loadTexts:configMD5SUMfiles.setStatus(_A)
_Notification_ObjectIdentity=ObjectIdentity
notification=_Notification_ObjectIdentity((1,3,6,1,4,1,28097,11))
_NotificationBindings_ObjectIdentity=ObjectIdentity
notificationBindings=_NotificationBindings_ObjectIdentity((1,3,6,1,4,1,28097,11,255))
_NbClientMacAddress_Type=PhysAddress
_NbClientMacAddress_Object=MibScalar
nbClientMacAddress=_NbClientMacAddress_Object((1,3,6,1,4,1,28097,11,255,1),_NbClientMacAddress_Type())
nbClientMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:nbClientMacAddress.setStatus(_A)
class _NbSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_NbSsid_Type.__name__=_F
_NbSsid_Object=MibScalar
nbSsid=_NbSsid_Object((1,3,6,1,4,1,28097,11,255,2),_NbSsid_Type())
nbSsid.setMaxAccess(_I)
if mibBuilder.loadTexts:nbSsid.setStatus(_A)
_NbBssid_Type=PhysAddress
_NbBssid_Object=MibScalar
nbBssid=_NbBssid_Object((1,3,6,1,4,1,28097,11,255,3),_NbBssid_Type())
nbBssid.setMaxAccess(_I)
if mibBuilder.loadTexts:nbBssid.setStatus(_A)
_NbEventState_Type=DisplayString
_NbEventState_Object=MibScalar
nbEventState=_NbEventState_Object((1,3,6,1,4,1,28097,11,255,4),_NbEventState_Type())
nbEventState.setMaxAccess(_I)
if mibBuilder.loadTexts:nbEventState.setStatus(_A)
_NbEventName_Type=DisplayString
_NbEventName_Object=MibScalar
nbEventName=_NbEventName_Object((1,3,6,1,4,1,28097,11,255,5),_NbEventName_Type())
nbEventName.setMaxAccess(_I)
if mibBuilder.loadTexts:nbEventName.setStatus(_A)
_NbRadioName_Type=DisplayString
_NbRadioName_Object=MibScalar
nbRadioName=_NbRadioName_Object((1,3,6,1,4,1,28097,11,255,6),_NbRadioName_Type())
nbRadioName.setMaxAccess(_I)
if mibBuilder.loadTexts:nbRadioName.setStatus(_A)
_NbRadioMacAddress_Type=PhysAddress
_NbRadioMacAddress_Object=MibScalar
nbRadioMacAddress=_NbRadioMacAddress_Object((1,3,6,1,4,1,28097,11,255,7),_NbRadioMacAddress_Type())
nbRadioMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:nbRadioMacAddress.setStatus(_A)
_NbRadioChannel_Type=Unsigned32
_NbRadioChannel_Object=MibScalar
nbRadioChannel=_NbRadioChannel_Object((1,3,6,1,4,1,28097,11,255,8),_NbRadioChannel_Type())
nbRadioChannel.setMaxAccess(_I)
if mibBuilder.loadTexts:nbRadioChannel.setStatus(_A)
_NbRadioChannelWidth_Type=Unsigned32
_NbRadioChannelWidth_Object=MibScalar
nbRadioChannelWidth=_NbRadioChannelWidth_Object((1,3,6,1,4,1,28097,11,255,9),_NbRadioChannelWidth_Type())
nbRadioChannelWidth.setMaxAccess(_I)
if mibBuilder.loadTexts:nbRadioChannelWidth.setStatus(_A)
_NbRadarChannel_Type=Unsigned32
_NbRadarChannel_Object=MibScalar
nbRadarChannel=_NbRadarChannel_Object((1,3,6,1,4,1,28097,11,255,10),_NbRadarChannel_Type())
nbRadarChannel.setMaxAccess(_I)
if mibBuilder.loadTexts:nbRadarChannel.setStatus(_A)
_NbRadarChannelWidth_Type=Unsigned32
_NbRadarChannelWidth_Object=MibScalar
nbRadarChannelWidth=_NbRadarChannelWidth_Object((1,3,6,1,4,1,28097,11,255,11),_NbRadarChannelWidth_Type())
nbRadarChannelWidth.setMaxAccess(_I)
if mibBuilder.loadTexts:nbRadarChannelWidth.setStatus(_A)
_NbHostName_Type=DisplayString
_NbHostName_Object=MibScalar
nbHostName=_NbHostName_Object((1,3,6,1,4,1,28097,11,255,12),_NbHostName_Type())
nbHostName.setMaxAccess(_I)
if mibBuilder.loadTexts:nbHostName.setStatus(_A)
_NbDigitalInName_Type=DisplayString
_NbDigitalInName_Object=MibScalar
nbDigitalInName=_NbDigitalInName_Object((1,3,6,1,4,1,28097,11,255,13),_NbDigitalInName_Type())
nbDigitalInName.setMaxAccess(_I)
if mibBuilder.loadTexts:nbDigitalInName.setStatus(_A)
_NbTcnTaiIp_Type=IpAddress
_NbTcnTaiIp_Object=MibScalar
nbTcnTaiIp=_NbTcnTaiIp_Object((1,3,6,1,4,1,28097,11,255,14),_NbTcnTaiIp_Type())
nbTcnTaiIp.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnTaiIp.setStatus(_A)
class _NbTcnEtbnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('initConfig',3),('notInaugurated',4),('readyForInauguration',5),('tndValidated',6),('inaugurating',7),('initServices',8),('inaugurated',9),('interConsistOperational',10),('tndPendingRemoval',11)))
_NbTcnEtbnStatus_Type.__name__=_D
_NbTcnEtbnStatus_Object=MibScalar
nbTcnEtbnStatus=_NbTcnEtbnStatus_Object((1,3,6,1,4,1,28097,11,255,15),_NbTcnEtbnStatus_Type())
nbTcnEtbnStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnEtbnStatus.setStatus(_A)
class _NbTcnEtbnRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_A9,0),('master',1),('backup',2),('notRedundant',3)))
_NbTcnEtbnRole_Type.__name__=_D
_NbTcnEtbnRole_Object=MibScalar
nbTcnEtbnRole=_NbTcnEtbnRole_Object((1,3,6,1,4,1,28097,11,255,16),_NbTcnEtbnRole_Type())
nbTcnEtbnRole.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnEtbnRole.setStatus(_A)
_NbTcnEtbnTopoCnt_Type=Unsigned32
_NbTcnEtbnTopoCnt_Object=MibScalar
nbTcnEtbnTopoCnt=_NbTcnEtbnTopoCnt_Object((1,3,6,1,4,1,28097,11,255,17),_NbTcnEtbnTopoCnt_Type())
nbTcnEtbnTopoCnt.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnEtbnTopoCnt.setStatus(_A)
class _NbTcnEtbTopoCntState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_W,2)))
_NbTcnEtbTopoCntState_Type.__name__=_D
_NbTcnEtbTopoCntState_Object=MibScalar
nbTcnEtbTopoCntState=_NbTcnEtbTopoCntState_Object((1,3,6,1,4,1,28097,11,255,18),_NbTcnEtbTopoCntState_Type())
nbTcnEtbTopoCntState.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnEtbTopoCntState.setStatus(_A)
_NbTcnLengtheningFlag_Type=TruthValue
_NbTcnLengtheningFlag_Object=MibScalar
nbTcnLengtheningFlag=_NbTcnLengtheningFlag_Object((1,3,6,1,4,1,28097,11,255,19),_NbTcnLengtheningFlag_Type())
nbTcnLengtheningFlag.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnLengtheningFlag.setStatus(_A)
class _NbTcnShorteningState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_NbTcnShorteningState_Type.__name__=_F
_NbTcnShorteningState_Object=MibScalar
nbTcnShorteningState=_NbTcnShorteningState_Object((1,3,6,1,4,1,28097,11,255,20),_NbTcnShorteningState_Type())
nbTcnShorteningState.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnShorteningState.setStatus(_A)
class _NbTcnRadio1CouplingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('stopped',0),('scanning',1),('signalgood',2),('signalbad',3)))
_NbTcnRadio1CouplingState_Type.__name__=_D
_NbTcnRadio1CouplingState_Object=MibScalar
nbTcnRadio1CouplingState=_NbTcnRadio1CouplingState_Object((1,3,6,1,4,1,28097,11,255,21),_NbTcnRadio1CouplingState_Type())
nbTcnRadio1CouplingState.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnRadio1CouplingState.setStatus(_A)
class _NbTcnConsistCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_NbTcnConsistCount_Type.__name__=_D
_NbTcnConsistCount_Object=MibScalar
nbTcnConsistCount=_NbTcnConsistCount_Object((1,3,6,1,4,1,28097,11,255,22),_NbTcnConsistCount_Type())
nbTcnConsistCount.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnConsistCount.setStatus(_A)
class _NbTcnConsistPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_NbTcnConsistPosition_Type.__name__=_D
_NbTcnConsistPosition_Object=MibScalar
nbTcnConsistPosition=_NbTcnConsistPosition_Object((1,3,6,1,4,1,28097,11,255,23),_NbTcnConsistPosition_Type())
nbTcnConsistPosition.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTcnConsistPosition.setStatus(_A)
_NbDescription_Type=DisplayString
_NbDescription_Object=MibScalar
nbDescription=_NbDescription_Object((1,3,6,1,4,1,28097,11,255,24),_NbDescription_Type())
nbDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:nbDescription.setStatus(_A)
_NbTimestamp_Type=Unsigned32
_NbTimestamp_Object=MibScalar
nbTimestamp=_NbTimestamp_Object((1,3,6,1,4,1,28097,11,255,25),_NbTimestamp_Type())
nbTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:nbTimestamp.setStatus(_A)
_NbMacAddr_Type=PhysAddress
_NbMacAddr_Object=MibScalar
nbMacAddr=_NbMacAddr_Object((1,3,6,1,4,1,28097,11,255,26),_NbMacAddr_Type())
nbMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:nbMacAddr.setStatus(_A)
_NbSource_Type=DisplayString
_NbSource_Object=MibScalar
nbSource=_NbSource_Object((1,3,6,1,4,1,28097,11,255,27),_NbSource_Type())
nbSource.setMaxAccess(_I)
if mibBuilder.loadTexts:nbSource.setStatus(_A)
_AcksysProductSerialNumber_Type=DisplayString
_AcksysProductSerialNumber_Object=MibScalar
acksysProductSerialNumber=_AcksysProductSerialNumber_Object((1,3,6,1,4,1,28097,12),_AcksysProductSerialNumber_Type())
acksysProductSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:acksysProductSerialNumber.setStatus(_A)
linkAlarm=NotificationType((1,3,6,1,4,1,28097,11,1))
linkAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:linkAlarm.setStatus(_A)
powerAlarm=NotificationType((1,3,6,1,4,1,28097,11,3))
powerAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:powerAlarm.setStatus(_A)
digitalInputAlarm=NotificationType((1,3,6,1,4,1,28097,11,4))
digitalInputAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:digitalInputAlarm.setStatus(_A)
tempExceededAlarm=NotificationType((1,3,6,1,4,1,28097,11,5))
tempExceededAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:tempExceededAlarm.setStatus(_A)
clientLinkAlarm=NotificationType((1,3,6,1,4,1,28097,11,6))
clientLinkAlarm.setObjects(*((_E,_Av),(_E,'nbSsid'),(_E,'nbBssid'),(_E,_Aw),(_E,_M)))
if mibBuilder.loadTexts:clientLinkAlarm.setStatus(_A)
vrrpAlarm=NotificationType((1,3,6,1,4,1,28097,11,7))
vrrpAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:vrrpAlarm.setStatus(_A)
dfsAlarm=NotificationType((1,3,6,1,4,1,28097,11,8))
dfsAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:dfsAlarm.setStatus(_A)
pingerAlarm=NotificationType((1,3,6,1,4,1,28097,11,9))
pingerAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:pingerAlarm.setStatus(_A)
tcnAlarm=NotificationType((1,3,6,1,4,1,28097,11,11))
tcnAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:tcnAlarm.setStatus(_A)
securityAlarm=NotificationType((1,3,6,1,4,1,28097,11,12))
securityAlarm.setObjects((_E,_M))
if mibBuilder.loadTexts:securityAlarm.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_y:PhysAddress,'WifiFlavor':WifiFlavor,'NetifName':NetifName,'SecurityModes':SecurityModes,'CellSecurityProtocol':CellSecurityProtocol,'PeapSecurityProtocol':PeapSecurityProtocol,'WpaVersions':WpaVersions,'CipherTypes':CipherTypes,'WepKeys':WepKeys,'WifiLevel':WifiLevel,'DisableEnable':DisableEnable,'TriState':TriState,'AsyncSetStatus':AsyncSetStatus,'BridgeId':BridgeId,'PortId':PortId,'CellAttachMode':CellAttachMode,'CellAccessTech':CellAccessTech,'acksys':acksys,'network-product':network_product,'wifiInterface':wifiInterface,'settings':settings,'settingInterfaceSsid':settingInterfaceSsid,'settingInterfaceWifiMode':settingInterfaceWifiMode,'settingInterfaceChannel':settingInterfaceChannel,'settingInterface80211Mode':settingInterface80211Mode,'settingInterfaceSuper-a-g-Mode':settingInterfaceSuper_a_g_Mode,'settingEnableRadio':settingEnableRadio,'settingTxPower':settingTxPower,'settingRegion':settingRegion,'securitySettings':securitySettings,'securityMode':securityMode,'securityWEP':securityWEP,'securityModeWepKeyLen':securityModeWepKeyLen,'securityModeWepKey-1':securityModeWepKey_1,'securityModeWepKey-2':securityModeWepKey_2,'securityModeWepKey-3':securityModeWepKey_3,'securityModeWepKey-4':securityModeWepKey_4,'securityModeDefaultWepKey':securityModeDefaultWepKey,'securityModeWepAuthentication':securityModeWepAuthentication,'securityWPA-WPA2':securityWPA_WPA2,'securityPresharedKey':securityPresharedKey,'securityModeWpaPresharedKey':securityModeWpaPresharedKey,'securityRadius':securityRadius,'securityModeWPARadiusAuthenticationTimeout':securityModeWPARadiusAuthenticationTimeout,'securityModeWPARadiusIP':securityModeWPARadiusIP,'securityModeWPARadiusPort':securityModeWPARadiusPort,'securityModeWPARadiusSecret':securityModeWPARadiusSecret,'securityModeWPARadiusMacAddressAuthentication':securityModeWPARadiusMacAddressAuthentication,'securityRadiusAP':securityRadiusAP,'securityModeWPARadiusAPAuthenticationTimeout':securityModeWPARadiusAPAuthenticationTimeout,'securityModeWPARadiusAPIP':securityModeWPARadiusAPIP,'securityModeWPARadiusAPPort':securityModeWPARadiusAPPort,'securityModeWPARadiusAPSecret':securityModeWPARadiusAPSecret,'securityModeWPARadiusAPMacAddressAuthentication':securityModeWPARadiusAPMacAddressAuthentication,'securityRadiusAPBackup':securityRadiusAPBackup,'securityModeWPABackupRadiusAPIP':securityModeWPABackupRadiusAPIP,'securityModeWPARadiusBackupAPPort':securityModeWPARadiusBackupAPPort,'securityModeWPARadiusBackupAPSecret':securityModeWPARadiusBackupAPSecret,'securityModeWPABackupRadiusAPMacAddressAuthentication':securityModeWPABackupRadiusAPMacAddressAuthentication,'securityRadiusBridge':securityRadiusBridge,'securityModeWPARadiusLogin':securityModeWPARadiusLogin,'securityModeWPARadiusPassword':securityModeWPARadiusPassword,'securityBackupRadius':securityBackupRadius,'securityModeWPABackupRadiusIP':securityModeWPABackupRadiusIP,'securityModeWPARadiusBackupPort':securityModeWPARadiusBackupPort,'securityModeWPARadiusBackupSecret':securityModeWPARadiusBackupSecret,'securityModeWPABackupRadiusMacAddressAuthentication':securityModeWPABackupRadiusMacAddressAuthentication,'securityModeWpaMode':securityModeWpaMode,'securityModeWpaCipherType':securityModeWpaCipherType,'securityModeWpaKeyUpdateInterval':securityModeWpaKeyUpdateInterval,'settingAntennaChoice':settingAntennaChoice,'settingTransmisionRate':settingTransmisionRate,'settingFlagUdapnopassword':settingFlagUdapnopassword,'settingFlagFiltersamenet':settingFlagFiltersamenet,'settingFlagFilterframecosom':settingFlagFilterframecosom,'settingDFSsupport':settingDFSsupport,'settingFilterCustomIpAddr':settingFilterCustomIpAddr,'settingFilterCustomSubnetMask':settingFilterCustomSubnetMask,'bridge-mode':bridge_mode,'bridge-modeLinkStatus':bridge_modeLinkStatus,'bridge-modeMacAP':bridge_modeMacAP,'bridge-modeRSSI':bridge_modeRSSI,'bridge-modeRSSIdBm':bridge_modeRSSIdBm,'bridge-modeRSSIPercent':bridge_modeRSSIPercent,'bridge-modeCurrentTxRate':bridge_modeCurrentTxRate,'bridge-WirelessMode':bridge_WirelessMode,'bridgeAPFiltering':bridgeAPFiltering,'bridgeAPFilteringEnable':bridgeAPFilteringEnable,'bridgeAPFilteringMode':bridgeAPFilteringMode,'bridgeAPFilteringMACAddress':bridgeAPFilteringMACAddress,'bridgeAPFilteringName':bridgeAPFilteringName,'bridgeAPFilteringSave':bridgeAPFilteringSave,'bridgeAPFilteringDelete':bridgeAPFilteringDelete,'bridgeAPFilteringEnableRule':bridgeAPFilteringEnableRule,'bridgeAPFilteringDisableRule':bridgeAPFilteringDisableRule,'bridgeAPFilteringTable':bridgeAPFilteringTable,'bridgeAPFilteringEntry':bridgeAPFilteringEntry,_A1:bridgeAPFilteringListId,'bridgeAPFilteringListName':bridgeAPFilteringListName,'bridgeAPFilteringListMAC':bridgeAPFilteringListMAC,'bridgeAPFilteringListEnable':bridgeAPFilteringListEnable,'bridgeRoaming':bridgeRoaming,'bridgeRoamingAdvanced':bridgeRoamingAdvanced,'bridgeRoamingAdvancedScanThreshold-dbm':bridgeRoamingAdvancedScanThreshold_dbm,'bridgeRoamingAdvancedScanThreshold-percent':bridgeRoamingAdvancedScanThreshold_percent,'bridgeRoamingAdvancedScanPeriod':bridgeRoamingAdvancedScanPeriod,'bridgeRoamingAdvancedScanDuration':bridgeRoamingAdvancedScanDuration,'bridgeRoamingAdvancedAPLossDetection':bridgeRoamingAdvancedAPLossDetection,'bridgeRoamingEnable':bridgeRoamingEnable,'bridgeRoamingRSSIThreshold-dBm':bridgeRoamingRSSIThreshold_dBm,'bridgeRoamingRSSIThreshold-percent':bridgeRoamingRSSIThreshold_percent,'bridgeChannelList':bridgeChannelList,'bridgeWirelessScan':bridgeWirelessScan,'bridgeWileressScanTable':bridgeWileressScanTable,'bridgeWirelessScanEntry':bridgeWirelessScanEntry,_A2:bridgeWirelessScanAPMac,'bridgeWirelessScanSSID':bridgeWirelessScanSSID,'bridgeWirelessScanChannel':bridgeWirelessScanChannel,'bridgeWirelessScanMode':bridgeWirelessScanMode,'bridgeWirelessScanSecurity':bridgeWirelessScanSecurity,'bridgeWirelessScanRssi':bridgeWirelessScanRssi,'bridgeNAT':bridgeNAT,'brigeNATStatus':brigeNATStatus,'brigeNATEnablePing':brigeNATEnablePing,'brigeNATEnableProductWebServer':brigeNATEnableProductWebServer,'brigeNATInternalWebServerPort':brigeNATInternalWebServerPort,'brigeNATEnableProductSnmpServer':brigeNATEnableProductSnmpServer,'brigeNATInternalWebSnmpPort':brigeNATInternalWebSnmpPort,'brigeNATWanIpAddrMode':brigeNATWanIpAddrMode,'brigeNATWanIpAddr':brigeNATWanIpAddr,'brigeNATWanSubnetMask':brigeNATWanSubnetMask,'brigeNATWanGateway':brigeNATWanGateway,'bridgeNatPortForwarding':bridgeNatPortForwarding,'bridgeNatPortForwardingTable':bridgeNatPortForwardingTable,'bridgeNatPortForwardingEntry':bridgeNatPortForwardingEntry,_A3:bridgeNatPortForwardingListId,'bridgeNatPortForwardingListName':bridgeNatPortForwardingListName,'bridgeNatPortForwardingListIpAddr':bridgeNatPortForwardingListIpAddr,'bridgeNatPortForwardingListPublicTcpPort':bridgeNatPortForwardingListPublicTcpPort,'bridgeNatPortForwardingListPrivateTcpPort':bridgeNatPortForwardingListPrivateTcpPort,'bridgeNatPortForwardingListPublicUdpPort':bridgeNatPortForwardingListPublicUdpPort,'bridgeNatPortForwardingListPrivateUdpPort':bridgeNatPortForwardingListPrivateUdpPort,'bridgeNatPortForwardingListEnable':bridgeNatPortForwardingListEnable,'bridgeNatPortForwardingName':bridgeNatPortForwardingName,'bridgeNatPortForwardingIpAddr':bridgeNatPortForwardingIpAddr,'bridgeNatPortForwardingPublicTcpPort':bridgeNatPortForwardingPublicTcpPort,'bridgeNatPortForwardingPrivateTcpPort':bridgeNatPortForwardingPrivateTcpPort,'bridgeNatPortForwardingPublicUdpPort':bridgeNatPortForwardingPublicUdpPort,'bridgeNatPortForwardingPrivateUdpPort':bridgeNatPortForwardingPrivateUdpPort,'bridgeNatPortForwardingEnableRule':bridgeNatPortForwardingEnableRule,'bridgeNatPortForwardingDisableRule':bridgeNatPortForwardingDisableRule,'bridgeNatPortForwardingSaveRule':bridgeNatPortForwardingSaveRule,'bridgeNatPortForwardingDeleteRule':bridgeNatPortForwardingDeleteRule,'access-point-mode':access_point_mode,'apClientTable':apClientTable,'apClientEntry':apClientEntry,_A4:clientMacAddr,'client80211Mode':client80211Mode,'clientTxRate':clientTxRate,'clientRssiPercent':clientRssiPercent,'apAutomaticChannel':apAutomaticChannel,'apClientCount':apClientCount,'apClientFiltering':apClientFiltering,'apClientFilteringEnable':apClientFilteringEnable,'apClientFilteringMode':apClientFilteringMode,'apClientWirelessFiltering':apClientWirelessFiltering,'apClientWiredFiltering':apClientWiredFiltering,'apClientFilteringMACAddress':apClientFilteringMACAddress,'apClientFilteringName':apClientFilteringName,'apClientFilteringSave':apClientFilteringSave,'apClientFilteringDelete':apClientFilteringDelete,'apClientFilteringEnableRule':apClientFilteringEnableRule,'apClientFilteringDisableRule':apClientFilteringDisableRule,'apClientFilteringTable':apClientFilteringTable,'apClientFilteringEntry':apClientFilteringEntry,_A5:apClientFilteringListId,'apClientFilteringListName':apClientFilteringListName,'apClientFilteringListMAC':apClientFilteringListMAC,'apClientFilteringListEnable':apClientFilteringListEnable,'wds':wds,'apWDSEnable':apWDSEnable,'apWDSEnableSTP':apWDSEnableSTP,'apWDSMAC1':apWDSMAC1,'apWDSMAC2':apWDSMAC2,'apWDSMAC3':apWDSMAC3,'apWDSMAC4':apWDSMAC4,'apWDSMAC5':apWDSMAC5,'apWDSMAC6':apWDSMAC6,'settingSSIDVisibility':settingSSIDVisibility,'enableSTP':enableSTP,'lanTimeOutSettings':lanTimeOutSettings,'enableLanTimeout':enableLanTimeout,'lanTimeoutIPSurvey':lanTimeoutIPSurvey,'lanTimeoutMaxProbe':lanTimeoutMaxProbe,'lanTimeoutProbeTimeout':lanTimeoutProbeTimeout,'lanTimeoutProbeInterval':lanTimeoutProbeInterval,'advancedSettings':advancedSettings,'longDistanceSettings':longDistanceSettings,'enableLongDistance':enableLongDistance,'distanceAntennaMeter':distanceAntennaMeter,'distanceSlotTime':distanceSlotTime,'distanceAckTimeout':distanceAckTimeout,'distanceCtsTimeout':distanceCtsTimeout,'enable802-11d':enable802_11d,'enableIsolateSTA':enableIsolateSTA,'administration':administration,'adminReset':adminReset,'adminResetFactory':adminResetFactory,'adminEnableWebServer':adminEnableWebServer,'adminAutoSave':adminAutoSave,'adminSave':adminSave,'adminApply':adminApply,'adminConfigHash':adminConfigHash,'fileTransfer':fileTransfer,'fileTransferAction':fileTransferAction,'fileTransferType':fileTransferType,'fileTransferSize':fileTransferSize,'fileTransferIndex':fileTransferIndex,'fileTransferHash':fileTransferHash,'fileTransferChunk':fileTransferChunk,'fileTransferResult':fileTransferResult,'fileTransferSession':fileTransferSession,'adminIdentify':adminIdentify,'adminEvents':adminEvents,'adminEventDisable':adminEventDisable,'adminEventEnable':adminEventEnable,'adminEventTrigger':adminEventTrigger,'adminTimeZone':adminTimeZone,'adminTimeZoneDBVersion':adminTimeZoneDBVersion,'adminTimeZoneName':adminTimeZoneName,'adminSystemDateAndTime':adminSystemDateAndTime,'adminSystemDateAndTimeLocal':adminSystemDateAndTimeLocal,'adminSystemDateAndTimeUTC':adminSystemDateAndTimeUTC,'os-stat':os_stat,'os-statFreeHeap':os_statFreeHeap,'os-statTotalHeap':os_statTotalHeap,'os-statHeapLowWater':os_statHeapLowWater,'os-statNetpageFree':os_statNetpageFree,'os-statNetpageLowWater':os_statNetpageLowWater,'productSpecific':productSpecific,'wlg-aboard':wlg_aboard,'wlg-aboard-PW1-state':wlg_aboard_PW1_state,'wlg-aboard-PW2-state':wlg_aboard_PW2_state,'lanInterface':lanInterface,'lanInterfaceIpAddrMode':lanInterfaceIpAddrMode,'lanInterfaceIpAddr':lanInterfaceIpAddr,'lanInterfaceSubNetMask':lanInterfaceSubNetMask,'lanInterfaceGatewayIp':lanInterfaceGatewayIp,'lanInterfaceHostName':lanInterfaceHostName,'lanInterfaceLocalDomainName':lanInterfaceLocalDomainName,'serialInterface':serialInterface,'serialServicetype':serialServicetype,'serialFormat':serialFormat,'serialFormatBaudRate':serialFormatBaudRate,'serialFormatDataBit':serialFormatDataBit,'serialFormatParityBit':serialFormatParityBit,'serialFormatStopBit':serialFormatStopBit,'serialElectricalInterface':serialElectricalInterface,'serialSendTriggers':serialSendTriggers,'serialSendTriggerCharcount':serialSendTriggerCharcount,'sendTriggerCharCountEnable':sendTriggerCharCountEnable,'sendTriggerCharCountValue':sendTriggerCharCountValue,'serialSendTriggerIdleDelay':serialSendTriggerIdleDelay,'sendTriggerIdleDelayEnable':sendTriggerIdleDelayEnable,'sendTriggerIdleDelayValue':sendTriggerIdleDelayValue,'sendTriggerIdleDelayUnit':sendTriggerIdleDelayUnit,'serialSendTriggerFrameDelay':serialSendTriggerFrameDelay,'sendTriggerFrameDelayEnable':sendTriggerFrameDelayEnable,'sendTriggerFrameDelayValue':sendTriggerFrameDelayValue,'sendTriggerFrameDelayUnit':sendTriggerFrameDelayUnit,'serialServiceVirtualCom':serialServiceVirtualCom,'serialServiceModbusSlave':serialServiceModbusSlave,'modbusSlaveFormat':modbusSlaveFormat,'modbusSlaveSerialTransactionTimeout':modbusSlaveSerialTransactionTimeout,'serialServiceModbusMaster':serialServiceModbusMaster,'modbusMasterFormat':modbusMasterFormat,'modbusMasterTransactionTimeout':modbusMasterTransactionTimeout,'modbusMasterForwardingTable':modbusMasterForwardingTable,'modbusMasterForwardingTable-Rule1':modbusMasterForwardingTable_Rule1,'mmForwardingTable-Rule1-FirstLocalAddr':mmForwardingTable_Rule1_FirstLocalAddr,'mmForwardingTable-Rule1-LastLocalAddr':mmForwardingTable_Rule1_LastLocalAddr,'mmForwardingTable-Rule1-FirstRemoteAddr':mmForwardingTable_Rule1_FirstRemoteAddr,'mmForwardingTable-Rule1-SlaveIpAddrIncrement':mmForwardingTable_Rule1_SlaveIpAddrIncrement,'mmForwardingTable-Rule1-SlaveIpAddr':mmForwardingTable_Rule1_SlaveIpAddr,'modbusMasterForwardingTable-Rule2':modbusMasterForwardingTable_Rule2,'mmForwardingTable-Rule2-FirstLocalAddr':mmForwardingTable_Rule2_FirstLocalAddr,'mmForwardingTable-Rule2-LastLocalAddr':mmForwardingTable_Rule2_LastLocalAddr,'mmForwardingTable-Rule2-FirstRemoteAddr':mmForwardingTable_Rule2_FirstRemoteAddr,'mmForwardingTable-Rule2-SlaveIpAddrIncrement':mmForwardingTable_Rule2_SlaveIpAddrIncrement,'mmForwardingTable-Rule2-SlaveIpAddr':mmForwardingTable_Rule2_SlaveIpAddr,'modbusMasterForwardingTable-Rule3':modbusMasterForwardingTable_Rule3,'mmForwardingTable-Rule3-FirstLocalAddr':mmForwardingTable_Rule3_FirstLocalAddr,'mmForwardingTable-Rule3-LastLocalAddr':mmForwardingTable_Rule3_LastLocalAddr,'mmForwardingTable-Rule3-FirstRemoteAddr':mmForwardingTable_Rule3_FirstRemoteAddr,'mmForwardingTable-Rule3-SlaveIpAddrIncrement':mmForwardingTable_Rule3_SlaveIpAddrIncrement,'mmForwardingTable-Rule3-SlaveIpAddr':mmForwardingTable_Rule3_SlaveIpAddr,'modbusMasterForwardingTable-Rule4':modbusMasterForwardingTable_Rule4,'mmForwardingTable-Rule4-FirstLocalAddr':mmForwardingTable_Rule4_FirstLocalAddr,'mmForwardingTable-Rule4-LastLocalAddr':mmForwardingTable_Rule4_LastLocalAddr,'mmForwardingTable-Rule4-FirstRemoteAddr':mmForwardingTable_Rule4_FirstRemoteAddr,'mmForwardingTable-Rule4-SlaveIpAddrIncrement':mmForwardingTable_Rule4_SlaveIpAddrIncrement,'mmForwardingTable-Rule4-SlaveIpAddr':mmForwardingTable_Rule4_SlaveIpAddr,'modbusMasterForwardingTable-Rule5':modbusMasterForwardingTable_Rule5,'mmForwardingTable-Rule5-FirstLocalAddr':mmForwardingTable_Rule5_FirstLocalAddr,'mmForwardingTable-Rule5-LastLocalAddr':mmForwardingTable_Rule5_LastLocalAddr,'mmForwardingTable-Rule5-FirstRemoteAddr':mmForwardingTable_Rule5_FirstRemoteAddr,'mmForwardingTable-Rule5-SlaveIpAddrIncrement':mmForwardingTable_Rule5_SlaveIpAddrIncrement,'mmForwardingTable-Rule5-SlaveIpAddr':mmForwardingTable_Rule5_SlaveIpAddr,'modbusMasterForwardingTable-Rule6':modbusMasterForwardingTable_Rule6,'mmForwardingTable-Rule6-FirstLocalAddr':mmForwardingTable_Rule6_FirstLocalAddr,'mmForwardingTable-Rule6-LastLocalAddr':mmForwardingTable_Rule6_LastLocalAddr,'mmForwardingTable-Rule6-FirstRemoteAddr':mmForwardingTable_Rule6_FirstRemoteAddr,'mmForwardingTable-Rule6-SlaveIpAddrIncrement':mmForwardingTable_Rule6_SlaveIpAddrIncrement,'mmForwardingTable-Rule6-SlaveIpAddr':mmForwardingTable_Rule6_SlaveIpAddr,'modbusMasterForwardingTable-Rule7':modbusMasterForwardingTable_Rule7,'mmForwardingTable-Rule7-FirstLocalAddr':mmForwardingTable_Rule7_FirstLocalAddr,'mmForwardingTable-Rule7-LastLocalAddr':mmForwardingTable_Rule7_LastLocalAddr,'mmForwardingTable-Rule7-FirstRemoteAddr':mmForwardingTable_Rule7_FirstRemoteAddr,'mmForwardingTable-Rule7-SlaveIpAddrIncrement':mmForwardingTable_Rule7_SlaveIpAddrIncrement,'mmForwardingTable-Rule7-SlaveIpAddr':mmForwardingTable_Rule7_SlaveIpAddr,'modbusMasterForwardingTable-Rule8':modbusMasterForwardingTable_Rule8,'mmForwardingTable-Rule8-FirstLocalAddr':mmForwardingTable_Rule8_FirstLocalAddr,'mmForwardingTable-Rule8-LastLocalAddr':mmForwardingTable_Rule8_LastLocalAddr,'mmForwardingTable-Rule8-FirstRemoteAddr':mmForwardingTable_Rule8_FirstRemoteAddr,'mmForwardingTable-Rule8-SlaveIpAddrIncrement':mmForwardingTable_Rule8_SlaveIpAddrIncrement,'mmForwardingTable-Rule8-SlaveIpAddr':mmForwardingTable_Rule8_SlaveIpAddr,'serialServiceTcpRawPortServer':serialServiceTcpRawPortServer,'tcpRawServerSerialExtraConfig':tcpRawServerSerialExtraConfig,'trsExtraConfigDTR':trsExtraConfigDTR,'trsExtraConfigRTS':trsExtraConfigRTS,'trsExtraConfigDSR':trsExtraConfigDSR,'trsExtraConfigCTS':trsExtraConfigCTS,'trsExtraConfigDCD':trsExtraConfigDCD,'trsExtraConfigXonXoff':trsExtraConfigXonXoff,'serialServiceTcpRawPortClient':serialServiceTcpRawPortClient,'tcpRawClientSerialExtraConfig':tcpRawClientSerialExtraConfig,'trcExtraConfigDTR':trcExtraConfigDTR,'trcExtraConfigRTS':trcExtraConfigRTS,'trcExtraConfigCTS':trcExtraConfigCTS,'trcExtraConfigDCD':trcExtraConfigDCD,'trcExtraConfigXonXoff':trcExtraConfigXonXoff,'tcpRawClientConnectionTimeout':tcpRawClientConnectionTimeout,'tcpRawClientPollPeriode':tcpRawClientPollPeriode,'tcpRawClientDSRUse':tcpRawClientDSRUse,'tcpRawClientRemoteServers':tcpRawClientRemoteServers,'tcpRawClientServer1':tcpRawClientServer1,'tcpRawClienServer1-IpAddress':tcpRawClienServer1_IpAddress,'tcpRawclientServer1-TcpPort':tcpRawclientServer1_TcpPort,'tcpRawClientServer2':tcpRawClientServer2,'tcpRawclientServer2-IpAddress':tcpRawclientServer2_IpAddress,'tcpRawclientServer2-TcpPort':tcpRawclientServer2_TcpPort,'tcpRawClientServer3':tcpRawClientServer3,'tcpRawclientServer3-IpAddress':tcpRawclientServer3_IpAddress,'tcpRawclientServer3-TcpPort':tcpRawclientServer3_TcpPort,'tcpRawClientServer4':tcpRawClientServer4,'tcpRawclientServer4-IpAddress':tcpRawclientServer4_IpAddress,'tcpRawclientServer4-TcpPort':tcpRawclientServer4_TcpPort,'tcpRawClientServer5':tcpRawClientServer5,'tcpRawclientServer5-IpAddress':tcpRawclientServer5_IpAddress,'tcpRawclientServer5-TcpPort':tcpRawclientServer5_TcpPort,'tcpRawClientServer6':tcpRawClientServer6,'tcpRawclientServer6-IpAddress':tcpRawclientServer6_IpAddress,'tcpRawclientServer6-TcpPort':tcpRawclientServer6_TcpPort,'tcpRawClientServer7':tcpRawClientServer7,'tcpRawclientServer7-IpAddress':tcpRawclientServer7_IpAddress,'tcpRawclientServer7-TcpPort':tcpRawclientServer7_TcpPort,'tcpRawClientServer8':tcpRawClientServer8,'tcpRawclientServer8-IpAddress':tcpRawclientServer8_IpAddress,'tcpRawclientServer8-TcpPort':tcpRawclientServer8_TcpPort,'serialServiceUdpRawPortServer':serialServiceUdpRawPortServer,'udpRawServerSerialExtraConfig':udpRawServerSerialExtraConfig,'ursExtraConfigDTR':ursExtraConfigDTR,'ursExtraConfigRTS':ursExtraConfigRTS,'ursExtraConfigCTS':ursExtraConfigCTS,'ursExtraConfigXonXoff':ursExtraConfigXonXoff,'udpRawServerRemoteIP':udpRawServerRemoteIP,'udpRawServerRemotePort':udpRawServerRemotePort,'udpRawServerLocalPort':udpRawServerLocalPort,'acksysInternals':acksysInternals,'internalUniqueID':internalUniqueID,'internalSerial':internalSerial,'internalWlanChange':internalWlanChange,'internalRadioChange':internalRadioChange,'internalSerialTest':internalSerialTest,'internalSerialTestResult':internalSerialTestResult,'internalAlarmSwitch':internalAlarmSwitch,'internalDigitalInput':internalDigitalInput,'acksysProductID':acksysProductID,'c-key-management':c_key_management,'ckeyManagementCopySettingTo':ckeyManagementCopySettingTo,'ckeyManagementCopySettingFrom':ckeyManagementCopySettingFrom,'ckeyManagementErase':ckeyManagementErase,'ckeyManagementStatus':ckeyManagementStatus,'ckeyManagementIgnoreSetting':ckeyManagementIgnoreSetting,'ckeyManagementDisableLed':ckeyManagementDisableLed,'ckeyManagementTest':ckeyManagementTest,'ckeyManagementTestResult':ckeyManagementTestResult,'alarmSettings':alarmSettings,'alarmSettingsTest':alarmSettingsTest,'alarmSettingsPower1Down':alarmSettingsPower1Down,'alarmSettingsPower1DownEnable':alarmSettingsPower1DownEnable,'alarmSettingsPower1DownEnableAutomaticReset':alarmSettingsPower1DownEnableAutomaticReset,'alarmSettingsPower1DownStatus':alarmSettingsPower1DownStatus,'alarmSettingsPower2Down':alarmSettingsPower2Down,'alarmSettingsPower2DownEnable':alarmSettingsPower2DownEnable,'alarmSettingsPower2DownEnableAutomaticReset':alarmSettingsPower2DownEnableAutomaticReset,'alarmSettingsPower2DownStatus':alarmSettingsPower2DownStatus,'alarmSettingsLan1Down':alarmSettingsLan1Down,'alarmSettingsLan1DownEnable':alarmSettingsLan1DownEnable,'alarmSettingsLan1DownEnableAutomaticReset':alarmSettingsLan1DownEnableAutomaticReset,'alarmSettingsLan1DownStatus':alarmSettingsLan1DownStatus,'alarmSettingsLan2Down':alarmSettingsLan2Down,'alarmSettingsLan2DownEnable':alarmSettingsLan2DownEnable,'alarmSettingsLan2DownEnableAutomaticReset':alarmSettingsLan2DownEnableAutomaticReset,'alarmSettingsLan2DownStatus':alarmSettingsLan2DownStatus,'alarmSettingsLan3Down':alarmSettingsLan3Down,'alarmSettingsLan3DownEnable':alarmSettingsLan3DownEnable,'alarmSettingsLan3DownEnableAutomaticReset':alarmSettingsLan3DownEnableAutomaticReset,'alarmSettingsLan3DownStatus':alarmSettingsLan3DownStatus,'alarmSettingsLan4Down':alarmSettingsLan4Down,'alarmSettingsLan4DownEnable':alarmSettingsLan4DownEnable,'alarmSettingsLan4DownEnableAutomaticReset':alarmSettingsLan4DownEnableAutomaticReset,'alarmSettingsLan4DownStatus':alarmSettingsLan4DownStatus,'alarmSettingsLan5Down':alarmSettingsLan5Down,'alarmSettingsLan5DownEnable':alarmSettingsLan5DownEnable,'alarmSettingsLan5DownEnableAutomaticReset':alarmSettingsLan5DownEnableAutomaticReset,'alarmSettingsLan5DownStatus':alarmSettingsLan5DownStatus,'alarmSettingsLan6Down':alarmSettingsLan6Down,'alarmSettingsLan6DownEnable':alarmSettingsLan6DownEnable,'alarmSettingsLan6DownEnableAutomaticReset':alarmSettingsLan6DownEnableAutomaticReset,'alarmSettingsLan6DownStatus':alarmSettingsLan6DownStatus,'alarmSettingsLan7Down':alarmSettingsLan7Down,'alarmSettingsLan7DownEnable':alarmSettingsLan7DownEnable,'alarmSettingsLan7DownEnableAutomaticReset':alarmSettingsLan7DownEnableAutomaticReset,'alarmSettingsLan7DownStatus':alarmSettingsLan7DownStatus,'alarmSettingsLan8Down':alarmSettingsLan8Down,'alarmSettingsLan8DownEnable':alarmSettingsLan8DownEnable,'alarmSettingsLan8DownEnableAutomaticReset':alarmSettingsLan8DownEnableAutomaticReset,'alarmSettingsLan8DownStatus':alarmSettingsLan8DownStatus,'alarmSettingsWLANDown':alarmSettingsWLANDown,'alarmSettingsWLANDownEnable':alarmSettingsWLANDownEnable,'alarmSettingsWLANDownEnableAutomaticReset':alarmSettingsWLANDownEnableAutomaticReset,'alarmSettingsWLANDownStatus':alarmSettingsWLANDownStatus,'powerStatus':powerStatus,'powerStatus-PW1-state':powerStatus_PW1_state,'powerStatus-PW2-state':powerStatus_PW2_state,'networkStatus':networkStatus,'statusIpSubnetTable':statusIpSubnetTable,'statusIpSubnetEntry':statusIpSubnetEntry,_A7:statusIpSubnetIndex,'statusIpSubnetName':statusIpSubnetName,'statusIpSubnetLabel':statusIpSubnetLabel,'statusIpSubnetIfIndex':statusIpSubnetIfIndex,'statusIpSubnetAddrMode':statusIpSubnetAddrMode,'statusIpSubnetIPv4Addr':statusIpSubnetIPv4Addr,'statusIpSubnetIPv4Mask':statusIpSubnetIPv4Mask,'statusIpSubnetDNS':statusIpSubnetDNS,'statusIpSubnetMember':statusIpSubnetMember,'statusIpSubnetMemberIndex':statusIpSubnetMemberIndex,'statusIfWlanTable':statusIfWlanTable,'statusIfWlanEntry':statusIfWlanEntry,_A8:statusIfWlanIndex,'statusIfWlanSSID':statusIfWlanSSID,'statusIfWlanMode':statusIfWlanMode,'statusIfWlanBand':statusIfWlanBand,'statusIfWlanChannel':statusIfWlanChannel,'statusIfWlanFrequency':statusIfWlanFrequency,'statusIfWlanEnable':statusIfWlanEnable,'statusIfWlanPhy':statusIfWlanPhy,'statusIfWlanSecurityMode':statusIfWlanSecurityMode,'statusIfWlanWpaVersion':statusIfWlanWpaVersion,'statusIfWlanNPeers':statusIfWlanNPeers,'statusIfWlanQuality':statusIfWlanQuality,'statusIfWlanBssid':statusIfWlanBssid,'statusIfWlanState':statusIfWlanState,'statusIfStaFastBSSTransitionActivated':statusIfStaFastBSSTransitionActivated,'statusIfWlanBeaconSignalAvg':statusIfWlanBeaconSignalAvg,'statusIfWlanNoise':statusIfWlanNoise,'statusIfWlanWpaCipher':statusIfWlanWpaCipher,'statusIfWlanWpaPreSharedKey':statusIfWlanWpaPreSharedKey,'statusIfWlanName':statusIfWlanName,'statusIfWlanIfIndex':statusIfWlanIfIndex,'statusPhyWifiTable':statusPhyWifiTable,'statusPhyWifiEntry':statusPhyWifiEntry,_AA:statusPhyWifiIndex,'statusPhyWifiLabel':statusPhyWifiLabel,'statusPhyWifiEnable':statusPhyWifiEnable,'statusPhyWifiName':statusPhyWifiName,'statusPhyWifiClusterMode':statusPhyWifiClusterMode,'statusPhyWifiClusterList':statusPhyWifiClusterList,'statusPhyWifiClusterArgs':statusPhyWifiClusterArgs,'statusPhyWifiMAC':statusPhyWifiMAC,'statusPhyWifiWids':statusPhyWifiWids,'statusPhyWifiScanTable':statusPhyWifiScanTable,'statusPhyWifiScanEntry':statusPhyWifiScanEntry,_AB:statusPhyWifiScanTableIndex,'statusPhyWifiScanSSID':statusPhyWifiScanSSID,'statusPhyWifiScanSignal':statusPhyWifiScanSignal,'statusPhyWifiScanFreq':statusPhyWifiScanFreq,'statusPhyWifiScanMode':statusPhyWifiScanMode,'statusPhyWifiScanSecurity':statusPhyWifiScanSecurity,'statusPhyWifiScanBssid':statusPhyWifiScanBssid,'statusPhyWifiScanPhyNum':statusPhyWifiScanPhyNum,'statusPhyWifiScanChWidth':statusPhyWifiScanChWidth,'statusPhyWifiScanTableStart':statusPhyWifiScanTableStart,'statusPhyWifiScanUpdateTbl':statusPhyWifiScanUpdateTbl,'statusSpanningTreeTable':statusSpanningTreeTable,'statusSpanningTreeEntry':statusSpanningTreeEntry,_AC:statusSpanningTreeBridgeName,'statusSpanningTreeNetworkLabel':statusSpanningTreeNetworkLabel,'statusSpanningTreeBridgeId':statusSpanningTreeBridgeId,'statusSpanningTreeDesignatedRoot':statusSpanningTreeDesignatedRoot,'statusSpanningTreeRootPort':statusSpanningTreeRootPort,'statusSpanningTreePortTable':statusSpanningTreePortTable,'statusSpanningTreePortEntry':statusSpanningTreePortEntry,_AD:statusSpanningTreePortBridgeName,'statusSpanningTreePortNetworkLabel':statusSpanningTreePortNetworkLabel,_AE:statusSpanningTreePortName,'statusSpanningTreePortLabel':statusSpanningTreePortLabel,'statusSpanningTreePortId':statusSpanningTreePortId,'statusSpanningTreePortRole':statusSpanningTreePortRole,'statusSpanningTreePortState':statusSpanningTreePortState,'statusSpanningTreePortPathCost':statusSpanningTreePortPathCost,'statusSpanningTreePortDesignatedRoot':statusSpanningTreePortDesignatedRoot,'statusSpanningTreePortDesignatedCost':statusSpanningTreePortDesignatedCost,'statusSpanningTreePortDesignatedBridge':statusSpanningTreePortDesignatedBridge,'statusSpanningTreePortDesignatedPort':statusSpanningTreePortDesignatedPort,'statusSpanningTreePortOperEdgePort':statusSpanningTreePortOperEdgePort,'statusSpanningTreePortOperPointToPoint':statusSpanningTreePortOperPointToPoint,'statusAssociationTable':statusAssociationTable,'statusAssociationEntry':statusAssociationEntry,_AF:statusAssociationIndex,'statusAssociationMacAddr':statusAssociationMacAddr,'statusAssociationSSID':statusAssociationSSID,'statusAssociationBSSID':statusAssociationBSSID,'statusAssociationPhy':statusAssociationPhy,'statusAssociationSignaldBm':statusAssociationSignaldBm,'statusAssociationNoisedBm':statusAssociationNoisedBm,'statusAssociationSNR':statusAssociationSNR,'statusAssociationWlanIndex':statusAssociationWlanIndex,'statusAssociationSecurityMode':statusAssociationSecurityMode,'statusPhyLanTable':statusPhyLanTable,'statusPhyLanEntry':statusPhyLanEntry,_AG:statusPhyLanIndex,'statusPhyLanName':statusPhyLanName,'statusPhyLanLabel':statusPhyLanLabel,'statusPhyLanIfIndex':statusPhyLanIfIndex,'statusMeshSurveyTable':statusMeshSurveyTable,'statusMeshSurveyEntry':statusMeshSurveyEntry,_AH:statusMeshSurveyIndex,'statusMeshSurveyDstMacAddr':statusMeshSurveyDstMacAddr,'statusMeshSurveyNextHopMacAddr':statusMeshSurveyNextHopMacAddr,'statusMeshSurveyPhy':statusMeshSurveyPhy,'statusMeshSurveyMetric':statusMeshSurveyMetric,'statusMeshSurveyDiscoveryTimeout':statusMeshSurveyDiscoveryTimeout,'statusMeshSurveyDiscoveryRetries':statusMeshSurveyDiscoveryRetries,'statusMeshSurveyStateActive':statusMeshSurveyStateActive,'statusMeshSurveyStateResolving':statusMeshSurveyStateResolving,'statusMeshSurveyStateDSNValid':statusMeshSurveyStateDSNValid,'statusMeshSurveyStateFixed':statusMeshSurveyStateFixed,'statusMeshSurveyStateResolved':statusMeshSurveyStateResolved,'statusMeshSurveyMeshId':statusMeshSurveyMeshId,'statusMeshSurveyWlanIndex':statusMeshSurveyWlanIndex,'statusPhyCellTable':statusPhyCellTable,'statusPhyCellEntry':statusPhyCellEntry,_AI:statusPhyCellIndex,'statusPhyCellLabel':statusPhyCellLabel,'statusPhyCellFriendlyName':statusPhyCellFriendlyName,'statusPhyCellEnable':statusPhyCellEnable,'statusPhyCellIMEI':statusPhyCellIMEI,'statusPhyCellModel':statusPhyCellModel,'statusPhyCellName':statusPhyCellName,'statusPhyCellSimSelected':statusPhyCellSimSelected,'statusPhyCellSimState':statusPhyCellSimState,'statusPhyCellSimIMSI':statusPhyCellSimIMSI,'statusPhyCellAttachMode':statusPhyCellAttachMode,'statusPhyCellOperator':statusPhyCellOperator,'statusPhyCellMcc':statusPhyCellMcc,'statusPhyCellMnc':statusPhyCellMnc,'statusPhyCellBaseLAC':statusPhyCellBaseLAC,'statusPhyCellBaseCID':statusPhyCellBaseCID,'statusPhyCellRegistrationClass':statusPhyCellRegistrationClass,'statusPhyCellAccessTech':statusPhyCellAccessTech,'statusPhyCellBandName':statusPhyCellBandName,'statusPhyCellARFCN':statusPhyCellARFCN,'statusPhyCellRSSI':statusPhyCellRSSI,'statusPhyCellBER':statusPhyCellBER,'statusRoaming':statusRoaming,'statusRoamingLeaveLvlMax':statusRoamingLeaveLvlMax,'statusRoamingLeaveLvlMin':statusRoamingLeaveLvlMin,'statusRoamingRoamLvlMax':statusRoamingRoamLvlMax,'statusRoamingRoamLvlMin':statusRoamingRoamLvlMin,'statusRoamingThresHyst':statusRoamingThresHyst,'statusRoamingLeaveBoost':statusRoamingLeaveBoost,'statusRoamingActiveIf':statusRoamingActiveIf,'statusRoamingActiveIfName':statusRoamingActiveIfName,'statusRoamingActiveIfBssid':statusRoamingActiveIfBssid,'statusRoamingActiveIfBeaconSignalAvg':statusRoamingActiveIfBeaconSignalAvg,'statusRoamingActiveIfNoise':statusRoamingActiveIfNoise,'statusRoamingActiveIfSwitching':statusRoamingActiveIfSwitching,'statusRoamingActiveIfChannel':statusRoamingActiveIfChannel,'statusRoamingActiveIfState':statusRoamingActiveIfState,'statusRoamingPassiveIf':statusRoamingPassiveIf,'statusRoamingPassiveIfName':statusRoamingPassiveIfName,'statusRoamingPassiveIfBssid':statusRoamingPassiveIfBssid,'statusRoamingPassiveIfBeaconSignalAvg':statusRoamingPassiveIfBeaconSignalAvg,'statusRoamingPassiveIfNoise':statusRoamingPassiveIfNoise,'statusRoamingPassiveIfSwitching':statusRoamingPassiveIfSwitching,'statusRoamingPassiveIfChannel':statusRoamingPassiveIfChannel,'statusRoamingPassiveIfState':statusRoamingPassiveIfState,'statusRoamingUrgent':statusRoamingUrgent,'networkConfiguration':networkConfiguration,'tcpip':tcpip,'configIpSubnetTable':configIpSubnetTable,'configIpSubnetEntry':configIpSubnetEntry,_AJ:configIpSubnetName,'configIpSubnetRowStatus':configIpSubnetRowStatus,'configIpAddressMode':configIpAddressMode,'configIpSubnetIPv4Addr':configIpSubnetIPv4Addr,'configIpSubnetIPv4Mask':configIpSubnetIPv4Mask,'configIpSubnetMetric':configIpSubnetMetric,'configIpSubnetDnsList':configIpSubnetDnsList,'configIpSubnetInterface':configIpSubnetInterface,'configIpSubnetIPv4Gateway':configIpSubnetIPv4Gateway,'configIpSubnetFriendlyName':configIpSubnetFriendlyName,'configIpSubnetBridgeEnable':configIpSubnetBridgeEnable,'configIpSubnetPersistence':configIpSubnetPersistence,'configIpSubnetEnable':configIpSubnetEnable,'configIpSubnetAutoStart':configIpSubnetAutoStart,'configIpSubnetPeerDns':configIpSubnetPeerDns,'configIpSubnetDefaultRoute':configIpSubnetDefaultRoute,'ipFactory':ipFactory,'synfloodprotection':synfloodprotection,'dropinvalidpacket':dropinvalidpacket,'configIpZonesTable':configIpZonesTable,'configIpZonesEntry':configIpZonesEntry,_AK:configIpZoneIndex,'configIpZoneRowStatus':configIpZoneRowStatus,'configIpZoneFriendlyName':configIpZoneFriendlyName,'configIpZoneNAT':configIpZoneNAT,'configIpZoneMSSClamping':configIpZoneMSSClamping,'configIpZoneDefaultAcceptancePolicy':configIpZoneDefaultAcceptancePolicy,'configIpZoneRestrictedAddressFamily':configIpZoneRestrictedAddressFamily,'configIpZoneConnectionTracking':configIpZoneConnectionTracking,'configIpZoneLogging':configIpZoneLogging,'configIpZoneLoggingLimit':configIpZoneLoggingLimit,'configIpZoneInterfaces':configIpZoneInterfaces,'configIpNatIpForwardTable':configIpNatIpForwardTable,'configIpNatIpForwardEntry':configIpNatIpForwardEntry,_AL:configIpNatIpForwardIndex,'configIpNatIpForwardRowStatus':configIpNatIpForwardRowStatus,'configIpNatIpForwardFriendlyName':configIpNatIpForwardFriendlyName,'configIpNatIpForwardZoneName':configIpNatIpForwardZoneName,'configIpNatIpForwardSrcIp':configIpNatIpForwardSrcIp,'configIpNatIpForwardProtocol':configIpNatIpForwardProtocol,'configIpNatIpForwardPublicPort':configIpNatIpForwardPublicPort,'configIpNatIpForwardPrivatePort':configIpNatIpForwardPrivatePort,'configIpNatIpForwardTargetIp':configIpNatIpForwardTargetIp,'configIpFirewallTable':configIpFirewallTable,'configIpFirewallEntry':configIpFirewallEntry,_AM:configIpFirewallIndex,'configIpFirewallRowStatus':configIpFirewallRowStatus,'configIpFirewallZoneName':configIpFirewallZoneName,'configIpFirewallProtocol':configIpFirewallProtocol,'configIpFirewallPort':configIpFirewallPort,'configIpFirewallAction':configIpFirewallAction,'configIpFirewallDestZone':configIpFirewallDestZone,'configIpFirewallSrcIP':configIpFirewallSrcIP,'configIpFirewallTargetIP':configIpFirewallTargetIP,'configIpRoutesTable':configIpRoutesTable,'configIpRoutesEntry':configIpRoutesEntry,_AN:configIpRoutesIndex,'configIpRoutesRowStatus':configIpRoutesRowStatus,'configIpRoutesNetwork':configIpRoutesNetwork,'configIpRoutesTarget':configIpRoutesTarget,'configIpRoutesNetmask':configIpRoutesNetmask,'configIpRoutesGateway':configIpRoutesGateway,'configIpRoutesMetric':configIpRoutesMetric,'configIpRoutesMTU':configIpRoutesMTU,'configIpZoneForwardTable':configIpZoneForwardTable,'configIpZoneForwardEntry':configIpZoneForwardEntry,_AO:configIpZoneForwardIndex,'configIpZoneForwardRowStatus':configIpZoneForwardRowStatus,'configIpZoneForwardSrc':configIpZoneForwardSrc,'configIpZoneForwardDst':configIpZoneForwardDst,'configIpDscpTaggingTable':configIpDscpTaggingTable,'configIpDscpTaggingEntry':configIpDscpTaggingEntry,_AP:configIpDscpTaggingIndex,'configIpDscpTaggingRowStatus':configIpDscpTaggingRowStatus,'configIpDscpTaggingFriendlyName':configIpDscpTaggingFriendlyName,'configIpDscpTaggingProtocol':configIpDscpTaggingProtocol,'configIpDscpTaggingSrcIP':configIpDscpTaggingSrcIP,'configIpDscpTaggingDstIP':configIpDscpTaggingDstIP,'configIpDscpTaggingSrcPort':configIpDscpTaggingSrcPort,'configIpDscpTaggingDstPort':configIpDscpTaggingDstPort,'configIpDscpTaggingDscpValue':configIpDscpTaggingDscpValue,'netphy':netphy,'configPhyWifiTable':configPhyWifiTable,'configPhyWifiEntry':configPhyWifiEntry,_AQ:configPhyWifiName,'configPhyWifiLabel':configPhyWifiLabel,'configPhyWifiMAC':configPhyWifiMAC,'configPhyWifiEnable':configPhyWifiEnable,'configPhyWifiMode':configPhyWifiMode,'configPhyWifiCountry':configPhyWifiCountry,'configPhyWifiChannel':configPhyWifiChannel,'configPhyWifiHTMode':configPhyWifiHTMode,'configPhyWifiTxPowerDBM':configPhyWifiTxPowerDBM,'configPhyWifiDistance':configPhyWifiDistance,'configPhyWifiClusterMode':configPhyWifiClusterMode,'configPhyWifiClusterList':configPhyWifiClusterList,'configPhyWifiClusterArgs':configPhyWifiClusterArgs,'configPhyWifiAntennaPorts':configPhyWifiAntennaPorts,'configPhyWifiABGBasicRates':configPhyWifiABGBasicRates,'configPhyWifiABGSupportedRates':configPhyWifiABGSupportedRates,'configPhyWifiChannelList':configPhyWifiChannelList,'configPhyWifiWids':configPhyWifiWids,'configPhyCellTable':configPhyCellTable,'configPhyCellEntry':configPhyCellEntry,_AR:configPhyCellName,'configPhyCellLabel':configPhyCellLabel,'configPhyCellDisableAtBoot':configPhyCellDisableAtBoot,'configPhyCellLogAT':configPhyCellLogAT,'configPhyCellSIM':configPhyCellSIM,'configPhyCellSetPIN':configPhyCellSetPIN,'configPhyCellSetPUK':configPhyCellSetPUK,'configPhyCellSetPINStatus':configPhyCellSetPINStatus,'configPhyCellSim1Pin':configPhyCellSim1Pin,'configPhyCellSim1Apn':configPhyCellSim1Apn,'configPhyCellSim1Authentication':configPhyCellSim1Authentication,'configPhyCellSim1Identity':configPhyCellSim1Identity,'configPhyCellSim1Password':configPhyCellSim1Password,'configPhyCellSim2Pin':configPhyCellSim2Pin,'configPhyCellSim2Apn':configPhyCellSim2Apn,'configPhyCellSim2Authentication':configPhyCellSim2Authentication,'configPhyCellSim2Identity':configPhyCellSim2Identity,'configPhyCellSim2Password':configPhyCellSim2Password,'netif':netif,'netdetails':netdetails,'configRadiusTable':configRadiusTable,'configRadiusEntry':configRadiusEntry,_AS:configRadiusIndex,'configRadiusRowStatus':configRadiusRowStatus,'configRadiusIpAddress':configRadiusIpAddress,'configRadiusPort':configRadiusPort,'configRadiusSecret':configRadiusSecret,'configDetailsNasId':configDetailsNasId,'configFilterGroupTable':configFilterGroupTable,'configFilterGroupEntry':configFilterGroupEntry,_AT:configFilterGroupIndex,'configFilterGroupRowStatus':configFilterGroupRowStatus,'configFilterGroupFriendlyName':configFilterGroupFriendlyName,'configFilterGroupRuleTable':configFilterGroupRuleTable,'configFilterGroupRuleEntry':configFilterGroupRuleEntry,_AU:configFilterGroupRuleIndex,'configFilterGroupRuleRowStatus':configFilterGroupRuleRowStatus,'configFilterGroupGroupIndex':configFilterGroupGroupIndex,'configFilterGroupRuleMACFrameType':configFilterGroupRuleMACFrameType,'configFilterGroupRuleCheckMAC':configFilterGroupRuleCheckMAC,'configFilterGroupRuleNetworkProtocol':configFilterGroupRuleNetworkProtocol,'configFilterGroupRuleIpAddress':configFilterGroupRuleIpAddress,'configFilterGroupRuleNetmask':configFilterGroupRuleNetmask,'configFilterGroupRuleCheckIP':configFilterGroupRuleCheckIP,'configFilterGroupRuleTransportProtocol':configFilterGroupRuleTransportProtocol,'configFilterGroupRuleFirstPort':configFilterGroupRuleFirstPort,'configFilterGroupRuleLastPort':configFilterGroupRuleLastPort,'configFilterGroupRuleCheckPort':configFilterGroupRuleCheckPort,'configInterfaceTable':configInterfaceTable,'configInterfaceEntry':configInterfaceEntry,_AV:configInterfaceName,'configInterfaceRowStatus':configInterfaceRowStatus,'configInterfaceType':configInterfaceType,'configInterfaceDepends':configInterfaceDepends,'configInterfaceOutputFilterGroup':configInterfaceOutputFilterGroup,'configInterfaceFilterGroupDir':configInterfaceFilterGroupDir,'configInterfaceInputFilterGroup':configInterfaceInputFilterGroup,'configIfStaTable':configIfStaTable,'configIfStaEntry':configIfStaEntry,_AW:configIfStaName,'configIfStaRowStatus':configIfStaRowStatus,'configIfStaPhy':configIfStaPhy,'configIfStaSsid':configIfStaSsid,'configIfStaBssid':configIfStaBssid,'configIfStaBridgingMode':configIfStaBridgingMode,'configIfStaScanChannels':configIfStaScanChannels,'configIfStaScanPassive':configIfStaScanPassive,'configIfStaRoamingEnable':configIfStaRoamingEnable,'configIfStaRoamingEnableDBM':configIfStaRoamingEnableDBM,'configIfStaRoamingRequiredBoost':configIfStaRoamingRequiredBoost,'configIfStaRoamingScanPeriod':configIfStaRoamingScanPeriod,'configIfStaSecurityMode':configIfStaSecurityMode,'configIfStaWepKey1':configIfStaWepKey1,'configIfStaWepKey2':configIfStaWepKey2,'configIfStaWepKey3':configIfStaWepKey3,'configIfStaWepKey4':configIfStaWepKey4,'configIfStaWepKey':configIfStaWepKey,'configIfStaWpaVersion':configIfStaWpaVersion,'configIfStaWpaCipher':configIfStaWpaCipher,'configIfStaIdentity':configIfStaIdentity,'configIfStaKey':configIfStaKey,'configIfStaPrivateKey':configIfStaPrivateKey,'configIfStaCACert':configIfStaCACert,'configIfStaEapType':configIfStaEapType,'configIfStaAuthentication':configIfStaAuthentication,'configIfStaFastBSSTransitionActivated':configIfStaFastBSSTransitionActivated,'configIfStaIgnorePreviousScansResults':configIfStaIgnorePreviousScansResults,'configIfStaRoamingRssiSmoothingFactor':configIfStaRoamingRssiSmoothingFactor,'configIfStaRoamingBeaconTimeout':configIfStaRoamingBeaconTimeout,'configIfStaWpaKeyCacheLifetime':configIfStaWpaKeyCacheLifetime,'configIfStaRoamingCurrentApScanThreshold':configIfStaRoamingCurrentApScanThreshold,'configIfStaRoamingMinimumStaLevel':configIfStaRoamingMinimumStaLevel,'configIfStaRoamingAboveLevelThreshold':configIfStaRoamingAboveLevelThreshold,'configIfStaRoamingMaxSignalLevel':configIfStaRoamingMaxSignalLevel,'configIfStaRoamingMinRoamDelay':configIfStaRoamingMinRoamDelay,'configIfStaRoamingNoReturnDelay':configIfStaRoamingNoReturnDelay,'configIfStaRoamingThresholdHysteresis':configIfStaRoamingThresholdHysteresis,'configIfStaRoamingOffChanMaxDelay':configIfStaRoamingOffChanMaxDelay,'configIfStaRoamingOffChanProbeDelay':configIfStaRoamingOffChanProbeDelay,'configIfStaRoamingPerChanProbeDelay':configIfStaRoamingPerChanProbeDelay,'configIfStaUserCert':configIfStaUserCert,'configIfStaDeauthBeforeRoamingtoNextAP':configIfStaDeauthBeforeRoamingtoNextAP,'configIfAPTable':configIfAPTable,'configIfAPEntry':configIfAPEntry,_AX:configIfAPName,'configIfAPRowStatus':configIfAPRowStatus,'configIfAPPhy':configIfAPPhy,'configIfAPSsid':configIfAPSsid,'configIfAPHidden':configIfAPHidden,'configIfAPWds':configIfAPWds,'configIfAPIsolate':configIfAPIsolate,'configIfAPSecurityMode':configIfAPSecurityMode,'configIfAPWepKey1':configIfAPWepKey1,'configIfAPWepKey2':configIfAPWepKey2,'configIfAPWepKey3':configIfAPWepKey3,'configIfAPWepKey4':configIfAPWepKey4,'configIfAPWepKey':configIfAPWepKey,'configIfAPWepAuthentication':configIfAPWepAuthentication,'configIfAPWpaVersion':configIfAPWpaVersion,'configIfAPWpaCipher':configIfAPWpaCipher,'configIfAPKey':configIfAPKey,'configIfAPRadiusIndex':configIfAPRadiusIndex,'configIfAPPreAuthentication':configIfAPPreAuthentication,'configIfAPMACFilterBehaviour':configIfAPMACFilterBehaviour,'configIfAPMACFilterAddresses':configIfAPMACFilterAddresses,'configIfAPWpaGroupRekey':configIfAPWpaGroupRekey,'configIfAPWpaPairRekey':configIfAPWpaPairRekey,'configIfAPWpaMasterRekey':configIfAPWpaMasterRekey,'configIfAPWpaProtectedFrame':configIfAPWpaProtectedFrame,'configIfAPMaxSimultaneousAssoc':configIfAPMaxSimultaneousAssoc,'configIfAPPasspointConfigName':configIfAPPasspointConfigName,'configIfMeshTable':configIfMeshTable,'configIfMeshEntry':configIfMeshEntry,_AY:configIfMeshName,'configIfMeshRowStatus':configIfMeshRowStatus,'configIfMeshPhy':configIfMeshPhy,'configIfMeshId':configIfMeshId,'configIfMeshSecurityMode':configIfMeshSecurityMode,'configIfMeshPreSharedKey':configIfMeshPreSharedKey,'configIfMeshPathRefreshTime':configIfMeshPathRefreshTime,'configIfMeshMinDiscoveryTimeout':configIfMeshMinDiscoveryTimeout,'configIfMeshActivePathTimeout':configIfMeshActivePathTimeout,'configIfMeshNetworkDiameterTraversalTime':configIfMeshNetworkDiameterTraversalTime,'configIfMeshRootMode':configIfMeshRootMode,'configIfMeshGatesAnnouncement':configIfMeshGatesAnnouncement,'configIfMeshActivePathToRootTimeout':configIfMeshActivePathToRootTimeout,'configIfMeshPreqRootInterval':configIfMeshPreqRootInterval,'configIfMeshRannRootInterval':configIfMeshRannRootInterval,'configIfBridgeTable':configIfBridgeTable,'configIfBridgeEntry':configIfBridgeEntry,_AZ:configIfBridgeName,'configIfBridgeRowStatus':configIfBridgeRowStatus,'configIfBridgeStp':configIfBridgeStp,'configIfBridgePriority':configIfBridgePriority,'configIfBridgeHello':configIfBridgeHello,'configIfBridgeMaxAge':configIfBridgeMaxAge,'configIfBridgeForwardDelay':configIfBridgeForwardDelay,'configIfBridgeLldpForward':configIfBridgeLldpForward,'configIfVlanTable':configIfVlanTable,'configIfVlanEntry':configIfVlanEntry,_Aa:configIfVlanIndex,'configIfVlanRowStatus':configIfVlanRowStatus,'configIfVlanFriendlyName':configIfVlanFriendlyName,'configIfVlanHostIfName':configIfVlanHostIfName,'configIfVlanId':configIfVlanId,'configIfSrccTable':configIfSrccTable,'configIfSrccEntry':configIfSrccEntry,_Ab:configIfSrccName,'configIfSrccRowStatus':configIfSrccRowStatus,'configIfSrccPhy':configIfSrccPhy,'configIfSrccDiscoverApSsid':configIfSrccDiscoverApSsid,'configIfSrccProductType':configIfSrccProductType,'configIfSrccDiscSigThreshold':configIfSrccDiscSigThreshold,'configIfSrccDiscDuration':configIfSrccDiscDuration,'configIfSrccBrokenThreshold':configIfSrccBrokenThreshold,'configIfSrccBrokenDuration':configIfSrccBrokenDuration,'configIfSrccWifiBand':configIfSrccWifiBand,'configIfSrccFirstChannel':configIfSrccFirstChannel,'configIfSrccSecondChannel':configIfSrccSecondChannel,'configIfSrccDiscScanDuration':configIfSrccDiscScanDuration,'configIfSrccMixRedundancy':configIfSrccMixRedundancy,'configIfSrccMixRedundancyBoost':configIfSrccMixRedundancyBoost,'configIfSrccPeerTableTimeout':configIfSrccPeerTableTimeout,'configIfSrccTargetTableTimeout':configIfSrccTargetTableTimeout,'configIfSrccPeerAcknowTimeout':configIfSrccPeerAcknowTimeout,'configIfSrccPeerReconfigTimeout':configIfSrccPeerReconfigTimeout,'configIfSrccGreBridgeIpAddr':configIfSrccGreBridgeIpAddr,'roaming':roaming,'roamingAlgorithm':roamingAlgorithm,'roamingPLHposition':roamingPLHposition,'roamingPLHjitter':roamingPLHjitter,'roamingPLHurgent':roamingPLHurgent,'roamingPLHfront':roamingPLHfront,'roamingPLHfrontCandMin':roamingPLHfrontCandMin,'roamingPLHfrontCandMax':roamingPLHfrontCandMax,'roamingPLHfrontCurrentLow':roamingPLHfrontCurrentLow,'roamingPLHfrontCurrentHigh':roamingPLHfrontCurrentHigh,'roamingPLHrear':roamingPLHrear,'roamingPLHrearCandMin':roamingPLHrearCandMin,'roamingPLHrearCandMax':roamingPLHrearCandMax,'roamingPLHrearCurrentLow':roamingPLHrearCurrentLow,'roamingPLHrearCurrentHigh':roamingPLHrearCurrentHigh,'serviceStatus':serviceStatus,'ss-webserver':ss_webserver,'ss-dhcp':ss_dhcp,'ss-ntp':ss_ntp,'ss-radius':ss_radius,'ss-snmp':ss_snmp,'snmpAgentOIDTable':snmpAgentOIDTable,'snmpAgentOIDEntry':snmpAgentOIDEntry,_Ac:snmpAgentOIDIndex,'snmpAgentOIDProductID':snmpAgentOIDProductID,'ss-dns':ss_dns,'ss-system':ss_system,'systemReady':systemReady,'sensors':sensors,'tempSensors':tempSensors,'motherBoard0':motherBoard0,'gpioInTable':gpioInTable,'gpioInEntry':gpioInEntry,_Ad:gpioInIndex,'gpioInState':gpioInState,'gpioOutTable':gpioOutTable,'gpioOutEntry':gpioOutEntry,_Ae:gpioOutIndex,'gpioOutState':gpioOutState,'ss-gnss':ss_gnss,'gnss-current-position':gnss_current_position,'positionValid':positionValid,'fixdate':fixdate,'fixtime':fixtime,'latitude':latitude,'longitude':longitude,'altitude':altitude,'speedkmh':speedkmh,'courseDegrees':courseDegrees,'fixdimension':fixdimension,'gnssAllPositions':gnssAllPositions,'ss-tcn':ss_tcn,'ss-async-sysupgrade':ss_async_sysupgrade,'firmwareExists':firmwareExists,'firmwareInfo':firmwareInfo,'sysupgradeMissed':sysupgradeMissed,'serviceConfiguration':serviceConfiguration,'sc-webserver':sc_webserver,'configHttpServer':configHttpServer,'configHttpServerPort':configHttpServerPort,'configHttpsServer':configHttpsServer,'configHttpsPort':configHttpsPort,'configHttpsCertificate':configHttpsCertificate,'sc-dhcp':sc_dhcp,'configDhcpTable':configDhcpTable,'configDhcpEntry':configDhcpEntry,_Af:configDhcpSubnet,'configDhcpRowStatus':configDhcpRowStatus,'configDhcpEnable':configDhcpEnable,'configDhcpPoolStart':configDhcpPoolStart,'configDhcpPoolCount':configDhcpPoolCount,'configDhcpLeaseDuration':configDhcpLeaseDuration,'sc-ntp':sc_ntp,'configNtp':configNtp,'sc-radius':sc_radius,'sc-snmp':sc_snmp,'sc-dns':sc_dns,'configRelay':configRelay,'configDnsRebindProtection':configDnsRebindProtection,'configDnsRebindLocalhost':configDnsRebindLocalhost,'sc-ssh':sc_ssh,'configSshEnable':configSshEnable,'configSshEnablePwd':configSshEnablePwd,'sc-tcn':sc_tcn,'sc-collectd':sc_collectd,'configCollectdEnable':configCollectdEnable,'configCollectdSamplingInterval':configCollectdSamplingInterval,'plugin-GPS':plugin_GPS,'configCollectdGPSEnable':configCollectdGPSEnable,'configCollectdGPSServerAddr':configCollectdGPSServerAddr,'configCollectdGPSServerPort':configCollectdGPSServerPort,'configCollectdGPSConnTimeout':configCollectdGPSConnTimeout,'configCollectdGPSReqInterval':configCollectdGPSReqInterval,'plugin-AcksysScanResult':plugin_AcksysScanResult,'configCollectdWirelessScanResult':configCollectdWirelessScanResult,'plugin-iwinfo':plugin_iwinfo,'configCollectdIwinfo':configCollectdIwinfo,'plugin-AcksysTelemetry':plugin_AcksysTelemetry,'configAcksysTelemetryEnable':configAcksysTelemetryEnable,'configAcksysTelemetryServerPort':configAcksysTelemetryServerPort,'configAcksysTelemetryOutputInterval':configAcksysTelemetryOutputInterval,'configAcksysTelemetryMaxBufferSize':configAcksysTelemetryMaxBufferSize,'sc-passpoint':sc_passpoint,'configPasspointConfigTable':configPasspointConfigTable,'configPasspointConfigEntry':configPasspointConfigEntry,_Ag:configPasspointConfigName,'configPasspointConfigRowStatus':configPasspointConfigRowStatus,'configPasspointConfigAnqpAccessNetworkType':configPasspointConfigAnqpAccessNetworkType,'configPasspointConfigAnqpInternet':configPasspointConfigAnqpInternet,'configPasspointConfigAnqpAsra':configPasspointConfigAnqpAsra,'configPasspointConfigAnqpEsr':configPasspointConfigAnqpEsr,'configPasspointConfigAnqpUesa':configPasspointConfigAnqpUesa,'configPasspointConfigAnqpHessid':configPasspointConfigAnqpHessid,'configPasspointConfigAnqpGasAddress3':configPasspointConfigAnqpGasAddress3,'configPasspointConfigAnqpVenueProfile':configPasspointConfigAnqpVenueProfile,'configPasspointConfigAnqpRoamingConsortiumProfile':configPasspointConfigAnqpRoamingConsortiumProfile,'configPasspointConfigAnqpNetworkAuthTypeProfile':configPasspointConfigAnqpNetworkAuthTypeProfile,'configPasspointConfigAnqpIpAddrTypeAvailProfile':configPasspointConfigAnqpIpAddrTypeAvailProfile,'configPasspointConfigAnqpDomainNameProfile':configPasspointConfigAnqpDomainNameProfile,'configPasspointConfigAnqp3gppCellNetProfile':configPasspointConfigAnqp3gppCellNetProfile,'configPasspointConfigAnqpNaiRealmProfile':configPasspointConfigAnqpNaiRealmProfile,'configPasspointConfigAnqpOverrideElementProfile':configPasspointConfigAnqpOverrideElementProfile,'configPasspointConfigHS20DisableDgaf':configPasspointConfigHS20DisableDgaf,'configPasspointConfigHS20DomainId':configPasspointConfigHS20DomainId,'configPasspointConfigHS20DeauthReqTimeout':configPasspointConfigHS20DeauthReqTimeout,'configPasspointConfigHS20OsuSsid':configPasspointConfigHS20OsuSsid,'configPasspointConfigHS20OperFriendlyNameProfile':configPasspointConfigHS20OperFriendlyNameProfile,'configPasspointConfigHS20ConnCapProfile':configPasspointConfigHS20ConnCapProfile,'configPasspointConfigHS20WanMetricsProfile':configPasspointConfigHS20WanMetricsProfile,'configPasspointConfigHS20OperClassProfile':configPasspointConfigHS20OperClassProfile,'configPasspointConfigHS20OsuProviderProfile':configPasspointConfigHS20OsuProviderProfile,'configAnqpProfileVenueTable':configAnqpProfileVenueTable,'configAnqpProfileVenueEntry':configAnqpProfileVenueEntry,_Ah:configProfileVenueName,'configProfileVenueRowStatus':configProfileVenueRowStatus,'configProfileVenueDesc':configProfileVenueDesc,'configVenueGroup':configVenueGroup,'configVenueType':configVenueType,'configVenueNameList':configVenueNameList,'configAnqpProfileRoamingConsortiumTable':configAnqpProfileRoamingConsortiumTable,'configAnqpProfileRoamingConsortiumEntry':configAnqpProfileRoamingConsortiumEntry,_Ai:configProfileRoamingConsortiumName,'configProfileRoamingConsortiumRowStatus':configProfileRoamingConsortiumRowStatus,'configProfileRoamingConsortiumDesc':configProfileRoamingConsortiumDesc,'configRoamingConsortiumList':configRoamingConsortiumList,'configAnqpProfileNetworkAuthTypeTable':configAnqpProfileNetworkAuthTypeTable,'configAnqpProfileNetworkAuthTypeEntry':configAnqpProfileNetworkAuthTypeEntry,_Aj:configProfileNetworkAuthTypeName,'configProfileNetworkAuthTypeRowStatus':configProfileNetworkAuthTypeRowStatus,'configProfileNetworkAuthTypeDesc':configProfileNetworkAuthTypeDesc,'configNetworkAuthType':configNetworkAuthType,'configAnqpProfileIpAddrTypeAvailTable':configAnqpProfileIpAddrTypeAvailTable,'configAnqpProfileIpAddrTypeAvailEntry':configAnqpProfileIpAddrTypeAvailEntry,_Ak:configProfileIpAddrTypeAvailName,'configProfileIpAddrTypeAvailRowStatus':configProfileIpAddrTypeAvailRowStatus,'configProfileIpAddrTypeAvailDesc':configProfileIpAddrTypeAvailDesc,'configIpv4Type':configIpv4Type,'configIpv6Type':configIpv6Type,'configAnqpProfileDomainNameTable':configAnqpProfileDomainNameTable,'configAnqpProfileDomainNameEntry':configAnqpProfileDomainNameEntry,_Al:configProfileDomainNameName,'configProfileDomainNameRowStatus':configProfileDomainNameRowStatus,'configProfileDomainNameDesc':configProfileDomainNameDesc,'configDomainNameList':configDomainNameList,'configAnqpProfile3gppCellNetTable':configAnqpProfile3gppCellNetTable,'configAnqpProfile3gppCellNetEntry':configAnqpProfile3gppCellNetEntry,_Am:configProfile3gppCellNetName,'configProfile3gppCellNetRowStatus':configProfile3gppCellNetRowStatus,'configProfile3gppCellNetDesc':configProfile3gppCellNetDesc,'config3gppCellNetList':config3gppCellNetList,'configAnqpProfileNaiRealmTable':configAnqpProfileNaiRealmTable,'configAnqpProfileNaiRealmEntry':configAnqpProfileNaiRealmEntry,_An:configProfileNaiRealmName,'configProfileNaiRealmRowStatus':configProfileNaiRealmRowStatus,'configProfileNaiRealmDesc':configProfileNaiRealmDesc,'configNaiRealmEncode':configNaiRealmEncode,'configNaiRealmRealmList':configNaiRealmRealmList,'configNaiRealmEap':configNaiRealmEap,'configAnqpProfileOverrideElementTable':configAnqpProfileOverrideElementTable,'configAnqpProfileOverrideElementEntry':configAnqpProfileOverrideElementEntry,_Ao:configProfileOverrideElementName,'configProfileOverrideElementRowStatus':configProfileOverrideElementRowStatus,'configProfileOverrideElementDesc':configProfileOverrideElementDesc,'configAnqpOverrideList':configAnqpOverrideList,'configHS20ProfileOperFriendlyNameTable':configHS20ProfileOperFriendlyNameTable,'configHS20ProfileOperFriendlyNameEntry':configHS20ProfileOperFriendlyNameEntry,_Ap:configProfileOperFriendlyNameName,'configProfileOperFriendlyNameRowStatus':configProfileOperFriendlyNameRowStatus,'configProfileOperFriendlyNameDesc':configProfileOperFriendlyNameDesc,'configFriendlyNameList':configFriendlyNameList,'configHS20ProfileConnCapTable':configHS20ProfileConnCapTable,'configHS20ProfileConnCapEntry':configHS20ProfileConnCapEntry,_Aq:configProfileConnCapName,'configProfileConnCapRowStatus':configProfileConnCapRowStatus,'configProfileConnCapDesc':configProfileConnCapDesc,'configConnCapabList':configConnCapabList,'configHS20ProfileWanMetricsTable':configHS20ProfileWanMetricsTable,'configHS20ProfileWanMetricsEntry':configHS20ProfileWanMetricsEntry,_Ar:configProfileWanMetricsName,'configProfileWanMetricsRowStatus':configProfileWanMetricsRowStatus,'configProfileWanMetricsDesc':configProfileWanMetricsDesc,'configLinkStatus':configLinkStatus,'configSymmetric':configSymmetric,'configAtCapacity':configAtCapacity,'configDownSpeed':configDownSpeed,'configUpSpeed':configUpSpeed,'configDownLoad':configDownLoad,'configUpLoad':configUpLoad,'configLMD':configLMD,'configHS20ProfileOperClassTable':configHS20ProfileOperClassTable,'configHS20ProfileOperClassEntry':configHS20ProfileOperClassEntry,_As:configProfileOperClassName,'configProfileOperClassRowStatus':configProfileOperClassRowStatus,'configProfileOperClassDesc':configProfileOperClassDesc,'configOperClassList':configOperClassList,'configHS20ProfileOsuProviderTable':configHS20ProfileOsuProviderTable,'configHS20ProfileOsuProviderEntry':configHS20ProfileOsuProviderEntry,_At:configProfileOsuProviderName,'configProfileOsuProviderRowStatus':configProfileOsuProviderRowStatus,'configProfileOsuProviderDesc':configProfileOsuProviderDesc,'configOsuServerUri':configOsuServerUri,'configOsuFriendlyNameList':configOsuFriendlyNameList,'configOsuNai':configOsuNai,'configOsuOmaDm':configOsuOmaDm,'configOsuSoapXml':configOsuSoapXml,'configOsuIconProfileList':configOsuIconProfileList,'configOsuServiceDescList':configOsuServiceDescList,'configProfileIconTable':configProfileIconTable,'configProfileIconEntry':configProfileIconEntry,_Au:configProfileIconName,'configProfileIconRowStatus':configProfileIconRowStatus,'configProfileIconDesc':configProfileIconDesc,'configIconLang':configIconLang,'configIconSize':configIconSize,'configIconType':configIconType,'configIconPath':configIconPath,'configIconFileContent':configIconFileContent,'sc-async-sysupgrade':sc_async_sysupgrade,'configAsyncUpgradeDoUpgrade':configAsyncUpgradeDoUpgrade,'configAsyncUpgradeTimerEnable':configAsyncUpgradeTimerEnable,'configAsyncUpgradeTimerMode':configAsyncUpgradeTimerMode,'configAsyncUpgradeTimerMinute':configAsyncUpgradeTimerMinute,'sc-md5sum':sc_md5sum,'configMD5SUMstatus':configMD5SUMstatus,'configMD5SUMfiles':configMD5SUMfiles,'notification':notification,'linkAlarm':linkAlarm,'powerAlarm':powerAlarm,'digitalInputAlarm':digitalInputAlarm,'tempExceededAlarm':tempExceededAlarm,'clientLinkAlarm':clientLinkAlarm,'vrrpAlarm':vrrpAlarm,'dfsAlarm':dfsAlarm,'pingerAlarm':pingerAlarm,'tcnAlarm':tcnAlarm,'securityAlarm':securityAlarm,'notificationBindings':notificationBindings,_Av:nbClientMacAddress,'nbSsid':nbSsid,'nbBssid':nbBssid,_Aw:nbEventState,_M:nbEventName,'nbRadioName':nbRadioName,'nbRadioMacAddress':nbRadioMacAddress,'nbRadioChannel':nbRadioChannel,'nbRadioChannelWidth':nbRadioChannelWidth,'nbRadarChannel':nbRadarChannel,'nbRadarChannelWidth':nbRadarChannelWidth,'nbHostName':nbHostName,'nbDigitalInName':nbDigitalInName,'nbTcnTaiIp':nbTcnTaiIp,'nbTcnEtbnStatus':nbTcnEtbnStatus,'nbTcnEtbnRole':nbTcnEtbnRole,'nbTcnEtbnTopoCnt':nbTcnEtbnTopoCnt,'nbTcnEtbTopoCntState':nbTcnEtbTopoCntState,'nbTcnLengtheningFlag':nbTcnLengtheningFlag,'nbTcnShorteningState':nbTcnShorteningState,'nbTcnRadio1CouplingState':nbTcnRadio1CouplingState,'nbTcnConsistCount':nbTcnConsistCount,'nbTcnConsistPosition':nbTcnConsistPosition,'nbDescription':nbDescription,'nbTimestamp':nbTimestamp,'nbMacAddr':nbMacAddr,'nbSource':nbSource,'acksysProductSerialNumber':acksysProductSerialNumber})