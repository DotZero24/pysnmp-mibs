_a='clientMacAddr'
_Z='bridgeNatPortForwardingListId'
_Y='static'
_X='bridgeAPFilteringListId'
_W='PhysAddress'
_V='apClientFilteringListId'
_U='true'
_T='false'
_S='a-only'
_R='mixed-b-g'
_Q='g-only'
_P='b-only'
_O='powerOn'
_N='powerOff'
_M='on'
_L='off'
_K='DisplayString'
_J='ACKSYS-WLG-MIB'
_I='ack'
_H='obsolete'
_G='OctetString'
_F='read-only'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,_W,'TextualConvention')
acksysMIB=ModuleIdentity((1,3,6,1,4,1,28097,2))
class DisplayString(OctetString):0
class PhysAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Acksys_ObjectIdentity=ObjectIdentity
acksys=_Acksys_ObjectIdentity((1,3,6,1,4,1,28097))
_Network_product_ObjectIdentity=ObjectIdentity
network_product=_Network_product_ObjectIdentity((1,3,6,1,4,1,28097,1))
_WifiInterface_ObjectIdentity=ObjectIdentity
wifiInterface=_WifiInterface_ObjectIdentity((1,3,6,1,4,1,28097,1,1))
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1))
class _SettingInterfaceSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SettingInterfaceSsid_Type.__name__=_K
_SettingInterfaceSsid_Object=MibScalar
settingInterfaceSsid=_SettingInterfaceSsid_Object((1,3,6,1,4,1,28097,1,1,1,1),_SettingInterfaceSsid_Type())
settingInterfaceSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceSsid.setStatus(_A)
class _SettingInterfaceWifiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('access-point',2)))
_SettingInterfaceWifiMode_Type.__name__=_C
_SettingInterfaceWifiMode_Object=MibScalar
settingInterfaceWifiMode=_SettingInterfaceWifiMode_Object((1,3,6,1,4,1,28097,1,1,1,2),_SettingInterfaceWifiMode_Type())
settingInterfaceWifiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceWifiMode.setStatus(_A)
_SettingInterfaceChannel_Type=Integer32
_SettingInterfaceChannel_Object=MibScalar
settingInterfaceChannel=_SettingInterfaceChannel_Object((1,3,6,1,4,1,28097,1,1,1,3),_SettingInterfaceChannel_Type())
settingInterfaceChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceChannel.setStatus(_A)
class _SettingInterface80211Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_SettingInterface80211Mode_Type.__name__=_C
_SettingInterface80211Mode_Object=MibScalar
settingInterface80211Mode=_SettingInterface80211Mode_Object((1,3,6,1,4,1,28097,1,1,1,4),_SettingInterface80211Mode_Type())
settingInterface80211Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterface80211Mode.setStatus(_A)
class _SettingInterfaceSuper_a_g_Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('super-g-without-turbo',2),('super-g-with-static-turbo',3),('super-g-with-dynamic-turbo',4)))
_SettingInterfaceSuper_a_g_Mode_Type.__name__=_C
_SettingInterfaceSuper_a_g_Mode_Object=MibScalar
settingInterfaceSuper_a_g_Mode=_SettingInterfaceSuper_a_g_Mode_Object((1,3,6,1,4,1,28097,1,1,1,5),_SettingInterfaceSuper_a_g_Mode_Type())
settingInterfaceSuper_a_g_Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:settingInterfaceSuper_a_g_Mode.setStatus(_A)
class _SettingEnableRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SettingEnableRadio_Type.__name__=_C
_SettingEnableRadio_Object=MibScalar
settingEnableRadio=_SettingEnableRadio_Object((1,3,6,1,4,1,28097,1,1,1,6),_SettingEnableRadio_Type())
settingEnableRadio.setMaxAccess(_B)
if mibBuilder.loadTexts:settingEnableRadio.setStatus(_A)
class _SettingTxPoxer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3)))
_SettingTxPoxer_Type.__name__=_C
_SettingTxPoxer_Object=MibScalar
settingTxPoxer=_SettingTxPoxer_Object((1,3,6,1,4,1,28097,1,1,1,7),_SettingTxPoxer_Type())
settingTxPoxer.setMaxAccess(_B)
if mibBuilder.loadTexts:settingTxPoxer.setStatus(_A)
class _SettingRegion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,5,6,7,10,14,17,18,20,21,22,23,27,28,29,30,31)));namedValues=NamedValues(*(('israel',2),('usa',4),('hong-kong',5),('canada',6),('australia',7),('franceoutdoor',10),('europe',14),('japan',17),('singapore',18),('korea',20),('mexico',21),('indonesia',22),('china',23),('russia',27),('brazil',28),('chile',29),('thailand',30),('peru',31)))
_SettingRegion_Type.__name__=_C
_SettingRegion_Object=MibScalar
settingRegion=_SettingRegion_Object((1,3,6,1,4,1,28097,1,1,1,8),_SettingRegion_Type())
settingRegion.setMaxAccess(_B)
if mibBuilder.loadTexts:settingRegion.setStatus(_A)
_SecuritySettings_ObjectIdentity=ObjectIdentity
securitySettings=_SecuritySettings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9))
class _SecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('wep',2),('wpa-wpa2-psk',3),('wpa-wpa2',4)))
_SecurityMode_Type.__name__=_C
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
class _SecurityModeWepKey_1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,26))
_SecurityModeWepKey_1_Type.__name__=_G
_SecurityModeWepKey_1_Object=MibScalar
securityModeWepKey_1=_SecurityModeWepKey_1_Object((1,3,6,1,4,1,28097,1,1,1,9,2,2),_SecurityModeWepKey_1_Type())
securityModeWepKey_1.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_1.setStatus(_A)
class _SecurityModeWepKey_2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,26))
_SecurityModeWepKey_2_Type.__name__=_G
_SecurityModeWepKey_2_Object=MibScalar
securityModeWepKey_2=_SecurityModeWepKey_2_Object((1,3,6,1,4,1,28097,1,1,1,9,2,3),_SecurityModeWepKey_2_Type())
securityModeWepKey_2.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_2.setStatus(_A)
class _SecurityModeWepKey_3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,26))
_SecurityModeWepKey_3_Type.__name__=_G
_SecurityModeWepKey_3_Object=MibScalar
securityModeWepKey_3=_SecurityModeWepKey_3_Object((1,3,6,1,4,1,28097,1,1,1,9,2,4),_SecurityModeWepKey_3_Type())
securityModeWepKey_3.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepKey_3.setStatus(_A)
class _SecurityModeWepKey_4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,26))
_SecurityModeWepKey_4_Type.__name__=_G
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
_SecurityModeWepAuthentication_Type.__name__=_C
_SecurityModeWepAuthentication_Object=MibScalar
securityModeWepAuthentication=_SecurityModeWepAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,2,7),_SecurityModeWepAuthentication_Type())
securityModeWepAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWepAuthentication.setStatus(_A)
_SecurityWPA_WPA2_ObjectIdentity=ObjectIdentity
securityWPA_WPA2=_SecurityWPA_WPA2_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3))
_SecurityPresharedKey_ObjectIdentity=ObjectIdentity
securityPresharedKey=_SecurityPresharedKey_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,1))
class _SecurityModeWpaPresharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_SecurityModeWpaPresharedKey_Type.__name__=_G
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
if mibBuilder.loadTexts:securityModeWPARadiusAuthenticationTimeout.setStatus(_H)
_SecurityModeWPARadiusIP_Type=IpAddress
_SecurityModeWPARadiusIP_Object=MibScalar
securityModeWPARadiusIP=_SecurityModeWPARadiusIP_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,2),_SecurityModeWPARadiusIP_Type())
securityModeWPARadiusIP.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusIP.setStatus(_H)
_SecurityModeWPARadiusPort_Type=Integer32
_SecurityModeWPARadiusPort_Object=MibScalar
securityModeWPARadiusPort=_SecurityModeWPARadiusPort_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,3),_SecurityModeWPARadiusPort_Type())
securityModeWPARadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusPort.setStatus(_H)
class _SecurityModeWPARadiusSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusSecret_Type.__name__=_G
_SecurityModeWPARadiusSecret_Object=MibScalar
securityModeWPARadiusSecret=_SecurityModeWPARadiusSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,4),_SecurityModeWPARadiusSecret_Type())
securityModeWPARadiusSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusSecret.setStatus(_H)
class _SecurityModeWPARadiusMacAddressAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SecurityModeWPARadiusMacAddressAuthentication_Type.__name__=_C
_SecurityModeWPARadiusMacAddressAuthentication_Object=MibScalar
securityModeWPARadiusMacAddressAuthentication=_SecurityModeWPARadiusMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,5),_SecurityModeWPARadiusMacAddressAuthentication_Type())
securityModeWPARadiusMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusMacAddressAuthentication.setStatus(_H)
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
_SecurityModeWPARadiusAPSecret_Type.__name__=_G
_SecurityModeWPARadiusAPSecret_Object=MibScalar
securityModeWPARadiusAPSecret=_SecurityModeWPARadiusAPSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,4),_SecurityModeWPARadiusAPSecret_Type())
securityModeWPARadiusAPSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusAPSecret.setStatus(_A)
class _SecurityModeWPARadiusAPMacAddressAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SecurityModeWPARadiusAPMacAddressAuthentication_Type.__name__=_C
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
_SecurityModeWPARadiusBackupAPSecret_Type.__name__=_G
_SecurityModeWPARadiusBackupAPSecret_Object=MibScalar
securityModeWPARadiusBackupAPSecret=_SecurityModeWPARadiusBackupAPSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6,3),_SecurityModeWPARadiusBackupAPSecret_Type())
securityModeWPARadiusBackupAPSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupAPSecret.setStatus(_A)
class _SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type.__name__=_C
_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Object=MibScalar
securityModeWPABackupRadiusAPMacAddressAuthentication=_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,6,6,4),_SecurityModeWPABackupRadiusAPMacAddressAuthentication_Type())
securityModeWPABackupRadiusAPMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPABackupRadiusAPMacAddressAuthentication.setStatus(_A)
_SecurityRadiusBridge_ObjectIdentity=ObjectIdentity
securityRadiusBridge=_SecurityRadiusBridge_ObjectIdentity((1,3,6,1,4,1,28097,1,1,1,9,3,2,7))
class _SecurityModeWPARadiusLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusLogin_Type.__name__=_G
_SecurityModeWPARadiusLogin_Object=MibScalar
securityModeWPARadiusLogin=_SecurityModeWPARadiusLogin_Object((1,3,6,1,4,1,28097,1,1,1,9,3,2,7,1),_SecurityModeWPARadiusLogin_Type())
securityModeWPARadiusLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusLogin.setStatus(_A)
class _SecurityModeWPARadiusPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusPassword_Type.__name__=_G
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
if mibBuilder.loadTexts:securityModeWPABackupRadiusIP.setStatus(_H)
_SecurityModeWPARadiusBackupPort_Type=Integer32
_SecurityModeWPARadiusBackupPort_Object=MibScalar
securityModeWPARadiusBackupPort=_SecurityModeWPARadiusBackupPort_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,2),_SecurityModeWPARadiusBackupPort_Type())
securityModeWPARadiusBackupPort.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupPort.setStatus(_H)
class _SecurityModeWPARadiusBackupSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SecurityModeWPARadiusBackupSecret_Type.__name__=_G
_SecurityModeWPARadiusBackupSecret_Object=MibScalar
securityModeWPARadiusBackupSecret=_SecurityModeWPARadiusBackupSecret_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,3),_SecurityModeWPARadiusBackupSecret_Type())
securityModeWPARadiusBackupSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPARadiusBackupSecret.setStatus(_H)
class _SecurityModeWPABackupRadiusMacAddressAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SecurityModeWPABackupRadiusMacAddressAuthentication_Type.__name__=_C
_SecurityModeWPABackupRadiusMacAddressAuthentication_Object=MibScalar
securityModeWPABackupRadiusMacAddressAuthentication=_SecurityModeWPABackupRadiusMacAddressAuthentication_Object((1,3,6,1,4,1,28097,1,1,1,9,3,3,4),_SecurityModeWPABackupRadiusMacAddressAuthentication_Type())
securityModeWPABackupRadiusMacAddressAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWPABackupRadiusMacAddressAuthentication.setStatus(_H)
class _SecurityModeWpaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wpa',1),('wpa2',2)))
_SecurityModeWpaMode_Type.__name__=_C
_SecurityModeWpaMode_Object=MibScalar
securityModeWpaMode=_SecurityModeWpaMode_Object((1,3,6,1,4,1,28097,1,1,1,9,3,4),_SecurityModeWpaMode_Type())
securityModeWpaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:securityModeWpaMode.setStatus(_A)
class _SecurityModeWpaCipherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tkip',1),('aes',2)))
_SecurityModeWpaCipherType_Type.__name__=_C
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
_SettingAntennaChoice_Type.__name__=_C
_SettingAntennaChoice_Object=MibScalar
settingAntennaChoice=_SettingAntennaChoice_Object((1,3,6,1,4,1,28097,1,1,1,10),_SettingAntennaChoice_Type())
settingAntennaChoice.setMaxAccess(_B)
if mibBuilder.loadTexts:settingAntennaChoice.setStatus(_A)
_SettingTransmisionRate_Type=Integer32
_SettingTransmisionRate_Object=MibScalar
settingTransmisionRate=_SettingTransmisionRate_Object((1,3,6,1,4,1,28097,1,1,1,11),_SettingTransmisionRate_Type())
settingTransmisionRate.setMaxAccess(_B)
if mibBuilder.loadTexts:settingTransmisionRate.setStatus(_A)
class _SettingFlagUdapnopassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_SettingFlagUdapnopassword_Type.__name__=_C
_SettingFlagUdapnopassword_Object=MibScalar
settingFlagUdapnopassword=_SettingFlagUdapnopassword_Object((1,3,6,1,4,1,28097,1,1,1,12),_SettingFlagUdapnopassword_Type())
settingFlagUdapnopassword.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFlagUdapnopassword.setStatus(_A)
class _SettingFlagFiltersamenet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('different-subnet-filter',2),('custom-subnet-filter',3)))
_SettingFlagFiltersamenet_Type.__name__=_C
_SettingFlagFiltersamenet_Object=MibScalar
settingFlagFiltersamenet=_SettingFlagFiltersamenet_Object((1,3,6,1,4,1,28097,1,1,1,13),_SettingFlagFiltersamenet_Type())
settingFlagFiltersamenet.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFlagFiltersamenet.setStatus(_A)
class _SettingFlagFilterframecosom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_SettingFlagFilterframecosom_Type.__name__=_C
_SettingFlagFilterframecosom_Object=MibScalar
settingFlagFilterframecosom=_SettingFlagFilterframecosom_Object((1,3,6,1,4,1,28097,1,1,1,14),_SettingFlagFilterframecosom_Type())
settingFlagFilterframecosom.setMaxAccess(_B)
if mibBuilder.loadTexts:settingFlagFilterframecosom.setStatus(_A)
class _SettingDFSsupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_SettingDFSsupport_Type.__name__=_C
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
_Bridge_modeLinkStatus_Type.__name__=_C
_Bridge_modeLinkStatus_Object=MibScalar
bridge_modeLinkStatus=_Bridge_modeLinkStatus_Object((1,3,6,1,4,1,28097,1,1,2,1),_Bridge_modeLinkStatus_Type())
bridge_modeLinkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:bridge_modeLinkStatus.setStatus(_A)
_Bridge_modeMacAP_Type=PhysAddress
_Bridge_modeMacAP_Object=MibScalar
bridge_modeMacAP=_Bridge_modeMacAP_Object((1,3,6,1,4,1,28097,1,1,2,2),_Bridge_modeMacAP_Type())
bridge_modeMacAP.setMaxAccess(_F)
if mibBuilder.loadTexts:bridge_modeMacAP.setStatus(_A)
_Bridge_modeRSSI_Type=Gauge32
_Bridge_modeRSSI_Object=MibScalar
bridge_modeRSSI=_Bridge_modeRSSI_Object((1,3,6,1,4,1,28097,1,1,2,3),_Bridge_modeRSSI_Type())
bridge_modeRSSI.setMaxAccess(_F)
if mibBuilder.loadTexts:bridge_modeRSSI.setStatus(_A)
_Bridge_modeRSSIdBm_Type=Gauge32
_Bridge_modeRSSIdBm_Object=MibScalar
bridge_modeRSSIdBm=_Bridge_modeRSSIdBm_Object((1,3,6,1,4,1,28097,1,1,2,4),_Bridge_modeRSSIdBm_Type())
bridge_modeRSSIdBm.setMaxAccess(_F)
if mibBuilder.loadTexts:bridge_modeRSSIdBm.setStatus(_A)
_Bridge_modeRSSIPercent_Type=Gauge32
_Bridge_modeRSSIPercent_Object=MibScalar
bridge_modeRSSIPercent=_Bridge_modeRSSIPercent_Object((1,3,6,1,4,1,28097,1,1,2,5),_Bridge_modeRSSIPercent_Type())
bridge_modeRSSIPercent.setMaxAccess(_F)
if mibBuilder.loadTexts:bridge_modeRSSIPercent.setStatus(_A)
_Bridge_modeCurrentTxRate_Type=Integer32
_Bridge_modeCurrentTxRate_Object=MibScalar
bridge_modeCurrentTxRate=_Bridge_modeCurrentTxRate_Object((1,3,6,1,4,1,28097,1,1,2,6),_Bridge_modeCurrentTxRate_Type())
bridge_modeCurrentTxRate.setMaxAccess(_F)
if mibBuilder.loadTexts:bridge_modeCurrentTxRate.setStatus(_A)
class _Bridge_WirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('infrastructure',1),('ad-hoc',2)))
_Bridge_WirelessMode_Type.__name__=_C
_Bridge_WirelessMode_Object=MibScalar
bridge_WirelessMode=_Bridge_WirelessMode_Object((1,3,6,1,4,1,28097,1,1,2,7),_Bridge_WirelessMode_Type())
bridge_WirelessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bridge_WirelessMode.setStatus(_A)
_BridgeAPFiltering_ObjectIdentity=ObjectIdentity
bridgeAPFiltering=_BridgeAPFiltering_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,8))
class _BridgeAPFilteringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_BridgeAPFilteringEnable_Type.__name__=_C
_BridgeAPFilteringEnable_Object=MibScalar
bridgeAPFilteringEnable=_BridgeAPFilteringEnable_Object((1,3,6,1,4,1,28097,1,1,2,8,1),_BridgeAPFilteringEnable_Type())
bridgeAPFilteringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeAPFilteringEnable.setStatus(_A)
class _BridgeAPFilteringMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_BridgeAPFilteringMode_Type.__name__=_C
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
_BridgeAPFilteringName_Type.__name__=_G
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
bridgeAPFilteringEntry.setIndexNames((0,_J,_X))
if mibBuilder.loadTexts:bridgeAPFilteringEntry.setStatus(_A)
_BridgeAPFilteringListId_Type=Integer32
_BridgeAPFilteringListId_Object=MibTableColumn
bridgeAPFilteringListId=_BridgeAPFilteringListId_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,1),_BridgeAPFilteringListId_Type())
bridgeAPFilteringListId.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeAPFilteringListId.setStatus(_A)
class _BridgeAPFilteringListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BridgeAPFilteringListName_Type.__name__=_G
_BridgeAPFilteringListName_Object=MibTableColumn
bridgeAPFilteringListName=_BridgeAPFilteringListName_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,2),_BridgeAPFilteringListName_Type())
bridgeAPFilteringListName.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeAPFilteringListName.setStatus(_A)
_BridgeAPFilteringListMAC_Type=PhysAddress
_BridgeAPFilteringListMAC_Object=MibTableColumn
bridgeAPFilteringListMAC=_BridgeAPFilteringListMAC_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,3),_BridgeAPFilteringListMAC_Type())
bridgeAPFilteringListMAC.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeAPFilteringListMAC.setStatus(_A)
class _BridgeAPFilteringListEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BridgeAPFilteringListEnable_Type.__name__=_C
_BridgeAPFilteringListEnable_Object=MibTableColumn
bridgeAPFilteringListEnable=_BridgeAPFilteringListEnable_Object((1,3,6,1,4,1,28097,1,1,2,8,9,1,4),_BridgeAPFilteringListEnable_Type())
bridgeAPFilteringListEnable.setMaxAccess(_F)
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
class _BridgeRoamingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BridgeRoamingEnable_Type.__name__=_C
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
_BridgeChannelList_Type.__name__=_G
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
bridgeWirelessScanEntry.setIndexNames((0,_J,_V))
if mibBuilder.loadTexts:bridgeWirelessScanEntry.setStatus(_A)
_BridgeWirelessScanAPMac_Type=PhysAddress
_BridgeWirelessScanAPMac_Object=MibTableColumn
bridgeWirelessScanAPMac=_BridgeWirelessScanAPMac_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,1),_BridgeWirelessScanAPMac_Type())
bridgeWirelessScanAPMac.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeWirelessScanAPMac.setStatus(_A)
class _BridgeWirelessScanSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_BridgeWirelessScanSSID_Type.__name__=_K
_BridgeWirelessScanSSID_Object=MibTableColumn
bridgeWirelessScanSSID=_BridgeWirelessScanSSID_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,2),_BridgeWirelessScanSSID_Type())
bridgeWirelessScanSSID.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeWirelessScanSSID.setStatus(_A)
_BridgeWirelessScanChannel_Type=Integer32
_BridgeWirelessScanChannel_Object=MibTableColumn
bridgeWirelessScanChannel=_BridgeWirelessScanChannel_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,3),_BridgeWirelessScanChannel_Type())
bridgeWirelessScanChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeWirelessScanChannel.setStatus(_A)
class _BridgeWirelessScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_BridgeWirelessScanMode_Type.__name__=_C
_BridgeWirelessScanMode_Object=MibTableColumn
bridgeWirelessScanMode=_BridgeWirelessScanMode_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,4),_BridgeWirelessScanMode_Type())
bridgeWirelessScanMode.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeWirelessScanMode.setStatus(_A)
class _BridgeWirelessScanSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('wep',1),('wpa',2)))
_BridgeWirelessScanSecurity_Type.__name__=_C
_BridgeWirelessScanSecurity_Object=MibTableColumn
bridgeWirelessScanSecurity=_BridgeWirelessScanSecurity_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,5),_BridgeWirelessScanSecurity_Type())
bridgeWirelessScanSecurity.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeWirelessScanSecurity.setStatus(_A)
_BridgeWirelessScanRssi_Type=Integer32
_BridgeWirelessScanRssi_Object=MibTableColumn
bridgeWirelessScanRssi=_BridgeWirelessScanRssi_Object((1,3,6,1,4,1,28097,1,1,2,11,1,1,6),_BridgeWirelessScanRssi_Type())
bridgeWirelessScanRssi.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeWirelessScanRssi.setStatus(_A)
_BridgeNAT_ObjectIdentity=ObjectIdentity
bridgeNAT=_BridgeNAT_ObjectIdentity((1,3,6,1,4,1,28097,1,1,2,12))
class _BrigeNATStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BrigeNATStatus_Type.__name__=_C
_BrigeNATStatus_Object=MibScalar
brigeNATStatus=_BrigeNATStatus_Object((1,3,6,1,4,1,28097,1,1,2,12,1),_BrigeNATStatus_Type())
brigeNATStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATStatus.setStatus(_A)
class _BrigeNATEnablePing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BrigeNATEnablePing_Type.__name__=_C
_BrigeNATEnablePing_Object=MibScalar
brigeNATEnablePing=_BrigeNATEnablePing_Object((1,3,6,1,4,1,28097,1,1,2,12,2),_BrigeNATEnablePing_Type())
brigeNATEnablePing.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATEnablePing.setStatus(_A)
class _BrigeNATEnableProductWebServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BrigeNATEnableProductWebServer_Type.__name__=_C
_BrigeNATEnableProductWebServer_Object=MibScalar
brigeNATEnableProductWebServer=_BrigeNATEnableProductWebServer_Object((1,3,6,1,4,1,28097,1,1,2,12,3),_BrigeNATEnableProductWebServer_Type())
brigeNATEnableProductWebServer.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATEnableProductWebServer.setStatus(_A)
_BrigeNATInternalWebServerPort_Type=Integer32
_BrigeNATInternalWebServerPort_Object=MibScalar
brigeNATInternalWebServerPort=_BrigeNATInternalWebServerPort_Object((1,3,6,1,4,1,28097,1,1,2,12,4),_BrigeNATInternalWebServerPort_Type())
brigeNATInternalWebServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATInternalWebServerPort.setStatus(_A)
class _BrigeNATEnableProductSnmpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BrigeNATEnableProductSnmpServer_Type.__name__=_C
_BrigeNATEnableProductSnmpServer_Object=MibScalar
brigeNATEnableProductSnmpServer=_BrigeNATEnableProductSnmpServer_Object((1,3,6,1,4,1,28097,1,1,2,12,5),_BrigeNATEnableProductSnmpServer_Type())
brigeNATEnableProductSnmpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATEnableProductSnmpServer.setStatus(_A)
_BrigeNATInternalWebSnmpPort_Type=Integer32
_BrigeNATInternalWebSnmpPort_Object=MibScalar
brigeNATInternalWebSnmpPort=_BrigeNATInternalWebSnmpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,6),_BrigeNATInternalWebSnmpPort_Type())
brigeNATInternalWebSnmpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brigeNATInternalWebSnmpPort.setStatus(_A)
class _BrigeNATWanIpAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),('dhcp',2)))
_BrigeNATWanIpAddrMode_Type.__name__=_C
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
bridgeNatPortForwardingEntry.setIndexNames((0,_J,_Z))
if mibBuilder.loadTexts:bridgeNatPortForwardingEntry.setStatus(_A)
_BridgeNatPortForwardingListId_Type=Integer32
_BridgeNatPortForwardingListId_Object=MibTableColumn
bridgeNatPortForwardingListId=_BridgeNatPortForwardingListId_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,1),_BridgeNatPortForwardingListId_Type())
bridgeNatPortForwardingListId.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListId.setStatus(_A)
class _BridgeNatPortForwardingListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListName_Type.__name__=_G
_BridgeNatPortForwardingListName_Object=MibTableColumn
bridgeNatPortForwardingListName=_BridgeNatPortForwardingListName_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,2),_BridgeNatPortForwardingListName_Type())
bridgeNatPortForwardingListName.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListName.setStatus(_A)
_BridgeNatPortForwardingListIpAddr_Type=IpAddress
_BridgeNatPortForwardingListIpAddr_Object=MibTableColumn
bridgeNatPortForwardingListIpAddr=_BridgeNatPortForwardingListIpAddr_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,3),_BridgeNatPortForwardingListIpAddr_Type())
bridgeNatPortForwardingListIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListIpAddr.setStatus(_A)
class _BridgeNatPortForwardingListPublicTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPublicTcpPort_Type.__name__=_G
_BridgeNatPortForwardingListPublicTcpPort_Object=MibTableColumn
bridgeNatPortForwardingListPublicTcpPort=_BridgeNatPortForwardingListPublicTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,4),_BridgeNatPortForwardingListPublicTcpPort_Type())
bridgeNatPortForwardingListPublicTcpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPublicTcpPort.setStatus(_A)
class _BridgeNatPortForwardingListPrivateTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPrivateTcpPort_Type.__name__=_G
_BridgeNatPortForwardingListPrivateTcpPort_Object=MibTableColumn
bridgeNatPortForwardingListPrivateTcpPort=_BridgeNatPortForwardingListPrivateTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,5),_BridgeNatPortForwardingListPrivateTcpPort_Type())
bridgeNatPortForwardingListPrivateTcpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPrivateTcpPort.setStatus(_A)
class _BridgeNatPortForwardingListPublicUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPublicUdpPort_Type.__name__=_G
_BridgeNatPortForwardingListPublicUdpPort_Object=MibTableColumn
bridgeNatPortForwardingListPublicUdpPort=_BridgeNatPortForwardingListPublicUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,6),_BridgeNatPortForwardingListPublicUdpPort_Type())
bridgeNatPortForwardingListPublicUdpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPublicUdpPort.setStatus(_A)
class _BridgeNatPortForwardingListPrivateUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingListPrivateUdpPort_Type.__name__=_G
_BridgeNatPortForwardingListPrivateUdpPort_Object=MibTableColumn
bridgeNatPortForwardingListPrivateUdpPort=_BridgeNatPortForwardingListPrivateUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,7),_BridgeNatPortForwardingListPrivateUdpPort_Type())
bridgeNatPortForwardingListPrivateUdpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListPrivateUdpPort.setStatus(_A)
class _BridgeNatPortForwardingListEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_BridgeNatPortForwardingListEnable_Type.__name__=_C
_BridgeNatPortForwardingListEnable_Object=MibTableColumn
bridgeNatPortForwardingListEnable=_BridgeNatPortForwardingListEnable_Object((1,3,6,1,4,1,28097,1,1,2,12,11,1,1,8),_BridgeNatPortForwardingListEnable_Type())
bridgeNatPortForwardingListEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:bridgeNatPortForwardingListEnable.setStatus(_A)
class _BridgeNatPortForwardingName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingName_Type.__name__=_G
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
_BridgeNatPortForwardingPublicTcpPort_Type.__name__=_G
_BridgeNatPortForwardingPublicTcpPort_Object=MibScalar
bridgeNatPortForwardingPublicTcpPort=_BridgeNatPortForwardingPublicTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,4),_BridgeNatPortForwardingPublicTcpPort_Type())
bridgeNatPortForwardingPublicTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPublicTcpPort.setStatus(_A)
class _BridgeNatPortForwardingPrivateTcpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPrivateTcpPort_Type.__name__=_G
_BridgeNatPortForwardingPrivateTcpPort_Object=MibScalar
bridgeNatPortForwardingPrivateTcpPort=_BridgeNatPortForwardingPrivateTcpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,5),_BridgeNatPortForwardingPrivateTcpPort_Type())
bridgeNatPortForwardingPrivateTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPrivateTcpPort.setStatus(_A)
class _BridgeNatPortForwardingPublicUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPublicUdpPort_Type.__name__=_G
_BridgeNatPortForwardingPublicUdpPort_Object=MibScalar
bridgeNatPortForwardingPublicUdpPort=_BridgeNatPortForwardingPublicUdpPort_Object((1,3,6,1,4,1,28097,1,1,2,12,11,6),_BridgeNatPortForwardingPublicUdpPort_Type())
bridgeNatPortForwardingPublicUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bridgeNatPortForwardingPublicUdpPort.setStatus(_A)
class _BridgeNatPortForwardingPrivateUdpPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BridgeNatPortForwardingPrivateUdpPort_Type.__name__=_G
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
apClientEntry.setIndexNames((0,_J,_a))
if mibBuilder.loadTexts:apClientEntry.setStatus(_A)
_ClientMacAddr_Type=PhysAddress
_ClientMacAddr_Object=MibTableColumn
clientMacAddr=_ClientMacAddr_Object((1,3,6,1,4,1,28097,1,1,3,1,1,1),_ClientMacAddr_Type())
clientMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:clientMacAddr.setStatus(_A)
class _Client80211Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_Client80211Mode_Type.__name__=_C
_Client80211Mode_Object=MibTableColumn
client80211Mode=_Client80211Mode_Object((1,3,6,1,4,1,28097,1,1,3,1,1,2),_Client80211Mode_Type())
client80211Mode.setMaxAccess(_F)
if mibBuilder.loadTexts:client80211Mode.setStatus(_A)
_ClientTxRate_Type=Integer32
_ClientTxRate_Object=MibTableColumn
clientTxRate=_ClientTxRate_Object((1,3,6,1,4,1,28097,1,1,3,1,1,3),_ClientTxRate_Type())
clientTxRate.setMaxAccess(_F)
if mibBuilder.loadTexts:clientTxRate.setStatus(_A)
_ClientRssiPercent_Type=Gauge32
_ClientRssiPercent_Object=MibTableColumn
clientRssiPercent=_ClientRssiPercent_Object((1,3,6,1,4,1,28097,1,1,3,1,1,4),_ClientRssiPercent_Type())
clientRssiPercent.setMaxAccess(_F)
if mibBuilder.loadTexts:clientRssiPercent.setStatus(_A)
class _ApAutomaticChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ApAutomaticChannel_Type.__name__=_C
_ApAutomaticChannel_Object=MibScalar
apAutomaticChannel=_ApAutomaticChannel_Object((1,3,6,1,4,1,28097,1,1,3,2),_ApAutomaticChannel_Type())
apAutomaticChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apAutomaticChannel.setStatus(_A)
_ApClientCount_Type=Integer32
_ApClientCount_Object=MibScalar
apClientCount=_ApClientCount_Object((1,3,6,1,4,1,28097,1,1,3,3),_ApClientCount_Type())
apClientCount.setMaxAccess(_F)
if mibBuilder.loadTexts:apClientCount.setStatus(_A)
_ApClientFiltering_ObjectIdentity=ObjectIdentity
apClientFiltering=_ApClientFiltering_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3,4))
class _ApClientFilteringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ApClientFilteringEnable_Type.__name__=_C
_ApClientFilteringEnable_Object=MibScalar
apClientFilteringEnable=_ApClientFilteringEnable_Object((1,3,6,1,4,1,28097,1,1,3,4,1),_ApClientFilteringEnable_Type())
apClientFilteringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringEnable.setStatus(_A)
class _ApClientFilteringMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_ApClientFilteringMode_Type.__name__=_C
_ApClientFilteringMode_Object=MibScalar
apClientFilteringMode=_ApClientFilteringMode_Object((1,3,6,1,4,1,28097,1,1,3,4,2),_ApClientFilteringMode_Type())
apClientFilteringMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientFilteringMode.setStatus(_A)
class _ApClientWirelessFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ApClientWirelessFiltering_Type.__name__=_C
_ApClientWirelessFiltering_Object=MibScalar
apClientWirelessFiltering=_ApClientWirelessFiltering_Object((1,3,6,1,4,1,28097,1,1,3,4,3),_ApClientWirelessFiltering_Type())
apClientWirelessFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:apClientWirelessFiltering.setStatus(_A)
class _ApClientWiredFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ApClientWiredFiltering_Type.__name__=_C
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
_ApClientFilteringName_Type.__name__=_G
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
apClientFilteringEntry.setIndexNames((0,_J,_V))
if mibBuilder.loadTexts:apClientFilteringEntry.setStatus(_A)
_ApClientFilteringListId_Type=Integer32
_ApClientFilteringListId_Object=MibTableColumn
apClientFilteringListId=_ApClientFilteringListId_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,1),_ApClientFilteringListId_Type())
apClientFilteringListId.setMaxAccess(_F)
if mibBuilder.loadTexts:apClientFilteringListId.setStatus(_A)
class _ApClientFilteringListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ApClientFilteringListName_Type.__name__=_G
_ApClientFilteringListName_Object=MibTableColumn
apClientFilteringListName=_ApClientFilteringListName_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,2),_ApClientFilteringListName_Type())
apClientFilteringListName.setMaxAccess(_F)
if mibBuilder.loadTexts:apClientFilteringListName.setStatus(_A)
_ApClientFilteringListMAC_Type=PhysAddress
_ApClientFilteringListMAC_Object=MibTableColumn
apClientFilteringListMAC=_ApClientFilteringListMAC_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,3),_ApClientFilteringListMAC_Type())
apClientFilteringListMAC.setMaxAccess(_F)
if mibBuilder.loadTexts:apClientFilteringListMAC.setStatus(_A)
class _ApClientFilteringListEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ApClientFilteringListEnable_Type.__name__=_C
_ApClientFilteringListEnable_Object=MibTableColumn
apClientFilteringListEnable=_ApClientFilteringListEnable_Object((1,3,6,1,4,1,28097,1,1,3,4,11,1,4),_ApClientFilteringListEnable_Type())
apClientFilteringListEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:apClientFilteringListEnable.setStatus(_A)
_Wds_ObjectIdentity=ObjectIdentity
wds=_Wds_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3,5))
class _ApWDSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ApWDSEnable_Type.__name__=_C
_ApWDSEnable_Object=MibScalar
apWDSEnable=_ApWDSEnable_Object((1,3,6,1,4,1,28097,1,1,3,5,1),_ApWDSEnable_Type())
apWDSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:apWDSEnable.setStatus(_A)
class _ApWDSEnableSTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ApWDSEnableSTP_Type.__name__=_C
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
_SettingSSIDVisibility_Type.__name__=_C
_SettingSSIDVisibility_Object=MibScalar
settingSSIDVisibility=_SettingSSIDVisibility_Object((1,3,6,1,4,1,28097,1,1,3,6),_SettingSSIDVisibility_Type())
settingSSIDVisibility.setMaxAccess(_B)
if mibBuilder.loadTexts:settingSSIDVisibility.setStatus(_A)
class _EnableSTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnableSTP_Type.__name__=_C
_EnableSTP_Object=MibScalar
enableSTP=_EnableSTP_Object((1,3,6,1,4,1,28097,1,1,3,7),_EnableSTP_Type())
enableSTP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableSTP.setStatus(_A)
_LanTimeOutSettings_ObjectIdentity=ObjectIdentity
lanTimeOutSettings=_LanTimeOutSettings_ObjectIdentity((1,3,6,1,4,1,28097,1,1,3,8))
class _EnableLanTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnableLanTimeout_Type.__name__=_C
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
class _EnableLongDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnableLongDistance_Type.__name__=_C
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
class _Enable802_11d_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Enable802_11d_Type.__name__=_C
_Enable802_11d_Object=MibScalar
enable802_11d=_Enable802_11d_Object((1,3,6,1,4,1,28097,1,1,4,2),_Enable802_11d_Type())
enable802_11d.setMaxAccess(_B)
if mibBuilder.loadTexts:enable802_11d.setStatus(_A)
class _EnableIsolateSTA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnableIsolateSTA_Type.__name__=_C
_EnableIsolateSTA_Object=MibScalar
enableIsolateSTA=_EnableIsolateSTA_Object((1,3,6,1,4,1,28097,1,1,4,3),_EnableIsolateSTA_Type())
enableIsolateSTA.setMaxAccess(_B)
if mibBuilder.loadTexts:enableIsolateSTA.setStatus(_A)
_Administration_ObjectIdentity=ObjectIdentity
administration=_Administration_ObjectIdentity((1,3,6,1,4,1,28097,1,2))
class _AdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdminReset_Type.__name__=_C
_AdminReset_Object=MibScalar
adminReset=_AdminReset_Object((1,3,6,1,4,1,28097,1,2,1),_AdminReset_Type())
adminReset.setMaxAccess(_B)
if mibBuilder.loadTexts:adminReset.setStatus(_A)
class _AdminResetFactory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('resetfactory',1))
_AdminResetFactory_Type.__name__=_C
_AdminResetFactory_Object=MibScalar
adminResetFactory=_AdminResetFactory_Object((1,3,6,1,4,1,28097,1,2,2),_AdminResetFactory_Type())
adminResetFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:adminResetFactory.setStatus(_A)
class _AdminEnableWebServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdminEnableWebServer_Type.__name__=_C
_AdminEnableWebServer_Object=MibScalar
adminEnableWebServer=_AdminEnableWebServer_Object((1,3,6,1,4,1,28097,1,2,3),_AdminEnableWebServer_Type())
adminEnableWebServer.setMaxAccess(_B)
if mibBuilder.loadTexts:adminEnableWebServer.setStatus(_A)
class _AdminAutoSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdminAutoSave_Type.__name__=_C
_AdminAutoSave_Object=MibScalar
adminAutoSave=_AdminAutoSave_Object((1,3,6,1,4,1,28097,1,2,4),_AdminAutoSave_Type())
adminAutoSave.setMaxAccess(_B)
if mibBuilder.loadTexts:adminAutoSave.setStatus(_A)
class _AdminSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('saveRequire',2),('saveNotRequire',3)))
_AdminSave_Type.__name__=_C
_AdminSave_Object=MibScalar
adminSave=_AdminSave_Object((1,3,6,1,4,1,28097,1,2,5),_AdminSave_Type())
adminSave.setMaxAccess(_B)
if mibBuilder.loadTexts:adminSave.setStatus(_A)
_Os_stat_ObjectIdentity=ObjectIdentity
os_stat=_Os_stat_ObjectIdentity((1,3,6,1,4,1,28097,1,3))
_Os_statFreeHeap_Type=Integer32
_Os_statFreeHeap_Object=MibScalar
os_statFreeHeap=_Os_statFreeHeap_Object((1,3,6,1,4,1,28097,1,3,1),_Os_statFreeHeap_Type())
os_statFreeHeap.setMaxAccess(_F)
if mibBuilder.loadTexts:os_statFreeHeap.setStatus(_A)
_Os_statTotalHeap_Type=Integer32
_Os_statTotalHeap_Object=MibScalar
os_statTotalHeap=_Os_statTotalHeap_Object((1,3,6,1,4,1,28097,1,3,2),_Os_statTotalHeap_Type())
os_statTotalHeap.setMaxAccess(_F)
if mibBuilder.loadTexts:os_statTotalHeap.setStatus(_A)
_Os_statHeapLowWater_Type=Integer32
_Os_statHeapLowWater_Object=MibScalar
os_statHeapLowWater=_Os_statHeapLowWater_Object((1,3,6,1,4,1,28097,1,3,3),_Os_statHeapLowWater_Type())
os_statHeapLowWater.setMaxAccess(_F)
if mibBuilder.loadTexts:os_statHeapLowWater.setStatus(_A)
_Os_statNetpageFree_Type=Integer32
_Os_statNetpageFree_Object=MibScalar
os_statNetpageFree=_Os_statNetpageFree_Object((1,3,6,1,4,1,28097,1,3,4),_Os_statNetpageFree_Type())
os_statNetpageFree.setMaxAccess(_F)
if mibBuilder.loadTexts:os_statNetpageFree.setStatus(_A)
_Os_statNetpageLowWater_Type=Integer32
_Os_statNetpageLowWater_Object=MibScalar
os_statNetpageLowWater=_Os_statNetpageLowWater_Object((1,3,6,1,4,1,28097,1,3,5),_Os_statNetpageLowWater_Type())
os_statNetpageLowWater.setMaxAccess(_F)
if mibBuilder.loadTexts:os_statNetpageLowWater.setStatus(_A)
_ProductSpecific_ObjectIdentity=ObjectIdentity
productSpecific=_ProductSpecific_ObjectIdentity((1,3,6,1,4,1,28097,1,4))
_Wlg_aboard_ObjectIdentity=ObjectIdentity
wlg_aboard=_Wlg_aboard_ObjectIdentity((1,3,6,1,4,1,28097,1,4,1))
class _Wlg_aboard_PW1_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Wlg_aboard_PW1_state_Type.__name__=_C
_Wlg_aboard_PW1_state_Object=MibScalar
wlg_aboard_PW1_state=_Wlg_aboard_PW1_state_Object((1,3,6,1,4,1,28097,1,4,1,1),_Wlg_aboard_PW1_state_Type())
wlg_aboard_PW1_state.setMaxAccess(_F)
if mibBuilder.loadTexts:wlg_aboard_PW1_state.setStatus(_H)
class _Wlg_aboard_PW2_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Wlg_aboard_PW2_state_Type.__name__=_C
_Wlg_aboard_PW2_state_Object=MibScalar
wlg_aboard_PW2_state=_Wlg_aboard_PW2_state_Object((1,3,6,1,4,1,28097,1,4,1,2),_Wlg_aboard_PW2_state_Type())
wlg_aboard_PW2_state.setMaxAccess(_F)
if mibBuilder.loadTexts:wlg_aboard_PW2_state.setStatus(_H)
_LanInterface_ObjectIdentity=ObjectIdentity
lanInterface=_LanInterface_ObjectIdentity((1,3,6,1,4,1,28097,1,5))
class _LanInterfaceIpAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),('dhcp',2)))
_LanInterfaceIpAddrMode_Type.__name__=_C
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
_LanInterfaceHostName_Type.__name__=_G
_LanInterfaceHostName_Object=MibScalar
lanInterfaceHostName=_LanInterfaceHostName_Object((1,3,6,1,4,1,28097,1,5,5),_LanInterfaceHostName_Type())
lanInterfaceHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceHostName.setStatus(_A)
class _LanInterfaceLocalDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,33))
_LanInterfaceLocalDomainName_Type.__name__=_G
_LanInterfaceLocalDomainName_Object=MibScalar
lanInterfaceLocalDomainName=_LanInterfaceLocalDomainName_Object((1,3,6,1,4,1,28097,1,5,6),_LanInterfaceLocalDomainName_Type())
lanInterfaceLocalDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:lanInterfaceLocalDomainName.setStatus(_A)
class _AcksysProductID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wlg-link',1),('wlg-aboard-n',2),('wlg-link-v2',3),('wlg-aboard-n-v2',4)))
_AcksysProductID_Type.__name__=_C
_AcksysProductID_Object=MibScalar
acksysProductID=_AcksysProductID_Object((1,3,6,1,4,1,28097,3),_AcksysProductID_Type())
acksysProductID.setMaxAccess(_F)
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
_AlarmSettings_ObjectIdentity=ObjectIdentity
alarmSettings=_AlarmSettings_ObjectIdentity((1,3,6,1,4,1,28097,5))
class _AlarmSettingsTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('clear',2)))
_AlarmSettingsTest_Type.__name__=_C
_AlarmSettingsTest_Object=MibScalar
alarmSettingsTest=_AlarmSettingsTest_Object((1,3,6,1,4,1,28097,5,1),_AlarmSettingsTest_Type())
alarmSettingsTest.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsTest.setStatus(_A)
_AlarmSettingsPower1Down_ObjectIdentity=ObjectIdentity
alarmSettingsPower1Down=_AlarmSettingsPower1Down_ObjectIdentity((1,3,6,1,4,1,28097,5,2))
class _AlarmSettingsPower1DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsPower1DownEnable_Type.__name__=_C
_AlarmSettingsPower1DownEnable_Object=MibScalar
alarmSettingsPower1DownEnable=_AlarmSettingsPower1DownEnable_Object((1,3,6,1,4,1,28097,5,2,1),_AlarmSettingsPower1DownEnable_Type())
alarmSettingsPower1DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower1DownEnable.setStatus(_A)
class _AlarmSettingsPower1DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsPower1DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsPower1DownEnableAutomaticReset_Object=MibScalar
alarmSettingsPower1DownEnableAutomaticReset=_AlarmSettingsPower1DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,2,2),_AlarmSettingsPower1DownEnableAutomaticReset_Type())
alarmSettingsPower1DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower1DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsPower1DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsPower1DownStatus_Type.__name__=_C
_AlarmSettingsPower1DownStatus_Object=MibScalar
alarmSettingsPower1DownStatus=_AlarmSettingsPower1DownStatus_Object((1,3,6,1,4,1,28097,5,2,3),_AlarmSettingsPower1DownStatus_Type())
alarmSettingsPower1DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower1DownStatus.setStatus(_A)
_AlarmSettingsPower2Down_ObjectIdentity=ObjectIdentity
alarmSettingsPower2Down=_AlarmSettingsPower2Down_ObjectIdentity((1,3,6,1,4,1,28097,5,3))
class _AlarmSettingsPower2DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsPower2DownEnable_Type.__name__=_C
_AlarmSettingsPower2DownEnable_Object=MibScalar
alarmSettingsPower2DownEnable=_AlarmSettingsPower2DownEnable_Object((1,3,6,1,4,1,28097,5,3,1),_AlarmSettingsPower2DownEnable_Type())
alarmSettingsPower2DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower2DownEnable.setStatus(_A)
class _AlarmSettingsPower2DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsPower2DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsPower2DownEnableAutomaticReset_Object=MibScalar
alarmSettingsPower2DownEnableAutomaticReset=_AlarmSettingsPower2DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,3,2),_AlarmSettingsPower2DownEnableAutomaticReset_Type())
alarmSettingsPower2DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower2DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsPower2DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsPower2DownStatus_Type.__name__=_C
_AlarmSettingsPower2DownStatus_Object=MibScalar
alarmSettingsPower2DownStatus=_AlarmSettingsPower2DownStatus_Object((1,3,6,1,4,1,28097,5,3,3),_AlarmSettingsPower2DownStatus_Type())
alarmSettingsPower2DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsPower2DownStatus.setStatus(_A)
_AlarmSettingsLan1Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan1Down=_AlarmSettingsLan1Down_ObjectIdentity((1,3,6,1,4,1,28097,5,4))
class _AlarmSettingsLan1DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan1DownEnable_Type.__name__=_C
_AlarmSettingsLan1DownEnable_Object=MibScalar
alarmSettingsLan1DownEnable=_AlarmSettingsLan1DownEnable_Object((1,3,6,1,4,1,28097,5,4,1),_AlarmSettingsLan1DownEnable_Type())
alarmSettingsLan1DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan1DownEnable.setStatus(_A)
class _AlarmSettingsLan1DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan1DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan1DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan1DownEnableAutomaticReset=_AlarmSettingsLan1DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,4,2),_AlarmSettingsLan1DownEnableAutomaticReset_Type())
alarmSettingsLan1DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan1DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan1DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan1DownStatus_Type.__name__=_C
_AlarmSettingsLan1DownStatus_Object=MibScalar
alarmSettingsLan1DownStatus=_AlarmSettingsLan1DownStatus_Object((1,3,6,1,4,1,28097,5,4,3),_AlarmSettingsLan1DownStatus_Type())
alarmSettingsLan1DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan1DownStatus.setStatus(_A)
_AlarmSettingsLan2Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan2Down=_AlarmSettingsLan2Down_ObjectIdentity((1,3,6,1,4,1,28097,5,5))
class _AlarmSettingsLan2DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan2DownEnable_Type.__name__=_C
_AlarmSettingsLan2DownEnable_Object=MibScalar
alarmSettingsLan2DownEnable=_AlarmSettingsLan2DownEnable_Object((1,3,6,1,4,1,28097,5,5,1),_AlarmSettingsLan2DownEnable_Type())
alarmSettingsLan2DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan2DownEnable.setStatus(_A)
class _AlarmSettingsLan2DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan2DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan2DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan2DownEnableAutomaticReset=_AlarmSettingsLan2DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,5,2),_AlarmSettingsLan2DownEnableAutomaticReset_Type())
alarmSettingsLan2DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan2DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan2DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan2DownStatus_Type.__name__=_C
_AlarmSettingsLan2DownStatus_Object=MibScalar
alarmSettingsLan2DownStatus=_AlarmSettingsLan2DownStatus_Object((1,3,6,1,4,1,28097,5,5,3),_AlarmSettingsLan2DownStatus_Type())
alarmSettingsLan2DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan2DownStatus.setStatus(_A)
_AlarmSettingsLan3Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan3Down=_AlarmSettingsLan3Down_ObjectIdentity((1,3,6,1,4,1,28097,5,6))
class _AlarmSettingsLan3DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan3DownEnable_Type.__name__=_C
_AlarmSettingsLan3DownEnable_Object=MibScalar
alarmSettingsLan3DownEnable=_AlarmSettingsLan3DownEnable_Object((1,3,6,1,4,1,28097,5,6,1),_AlarmSettingsLan3DownEnable_Type())
alarmSettingsLan3DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan3DownEnable.setStatus(_A)
class _AlarmSettingsLan3DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan3DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan3DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan3DownEnableAutomaticReset=_AlarmSettingsLan3DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,6,2),_AlarmSettingsLan3DownEnableAutomaticReset_Type())
alarmSettingsLan3DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan3DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan3DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan3DownStatus_Type.__name__=_C
_AlarmSettingsLan3DownStatus_Object=MibScalar
alarmSettingsLan3DownStatus=_AlarmSettingsLan3DownStatus_Object((1,3,6,1,4,1,28097,5,6,3),_AlarmSettingsLan3DownStatus_Type())
alarmSettingsLan3DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan3DownStatus.setStatus(_A)
_AlarmSettingsLan4Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan4Down=_AlarmSettingsLan4Down_ObjectIdentity((1,3,6,1,4,1,28097,5,7))
class _AlarmSettingsLan4DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan4DownEnable_Type.__name__=_C
_AlarmSettingsLan4DownEnable_Object=MibScalar
alarmSettingsLan4DownEnable=_AlarmSettingsLan4DownEnable_Object((1,3,6,1,4,1,28097,5,7,1),_AlarmSettingsLan4DownEnable_Type())
alarmSettingsLan4DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan4DownEnable.setStatus(_A)
class _AlarmSettingsLan4DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan4DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan4DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan4DownEnableAutomaticReset=_AlarmSettingsLan4DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,7,2),_AlarmSettingsLan4DownEnableAutomaticReset_Type())
alarmSettingsLan4DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan4DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan4DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan4DownStatus_Type.__name__=_C
_AlarmSettingsLan4DownStatus_Object=MibScalar
alarmSettingsLan4DownStatus=_AlarmSettingsLan4DownStatus_Object((1,3,6,1,4,1,28097,5,7,3),_AlarmSettingsLan4DownStatus_Type())
alarmSettingsLan4DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan4DownStatus.setStatus(_A)
_AlarmSettingsLan5Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan5Down=_AlarmSettingsLan5Down_ObjectIdentity((1,3,6,1,4,1,28097,5,8))
class _AlarmSettingsLan5DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan5DownEnable_Type.__name__=_C
_AlarmSettingsLan5DownEnable_Object=MibScalar
alarmSettingsLan5DownEnable=_AlarmSettingsLan5DownEnable_Object((1,3,6,1,4,1,28097,5,8,1),_AlarmSettingsLan5DownEnable_Type())
alarmSettingsLan5DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan5DownEnable.setStatus(_A)
class _AlarmSettingsLan5DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan5DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan5DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan5DownEnableAutomaticReset=_AlarmSettingsLan5DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,8,2),_AlarmSettingsLan5DownEnableAutomaticReset_Type())
alarmSettingsLan5DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan5DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan5DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan5DownStatus_Type.__name__=_C
_AlarmSettingsLan5DownStatus_Object=MibScalar
alarmSettingsLan5DownStatus=_AlarmSettingsLan5DownStatus_Object((1,3,6,1,4,1,28097,5,8,3),_AlarmSettingsLan5DownStatus_Type())
alarmSettingsLan5DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan5DownStatus.setStatus(_A)
_AlarmSettingsLan6Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan6Down=_AlarmSettingsLan6Down_ObjectIdentity((1,3,6,1,4,1,28097,5,9))
class _AlarmSettingsLan6DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan6DownEnable_Type.__name__=_C
_AlarmSettingsLan6DownEnable_Object=MibScalar
alarmSettingsLan6DownEnable=_AlarmSettingsLan6DownEnable_Object((1,3,6,1,4,1,28097,5,9,1),_AlarmSettingsLan6DownEnable_Type())
alarmSettingsLan6DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan6DownEnable.setStatus(_A)
class _AlarmSettingsLan6DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan6DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan6DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan6DownEnableAutomaticReset=_AlarmSettingsLan6DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,9,2),_AlarmSettingsLan6DownEnableAutomaticReset_Type())
alarmSettingsLan6DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan6DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan6DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan6DownStatus_Type.__name__=_C
_AlarmSettingsLan6DownStatus_Object=MibScalar
alarmSettingsLan6DownStatus=_AlarmSettingsLan6DownStatus_Object((1,3,6,1,4,1,28097,5,9,3),_AlarmSettingsLan6DownStatus_Type())
alarmSettingsLan6DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan6DownStatus.setStatus(_A)
_AlarmSettingsLan7Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan7Down=_AlarmSettingsLan7Down_ObjectIdentity((1,3,6,1,4,1,28097,5,10))
class _AlarmSettingsLan7DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan7DownEnable_Type.__name__=_C
_AlarmSettingsLan7DownEnable_Object=MibScalar
alarmSettingsLan7DownEnable=_AlarmSettingsLan7DownEnable_Object((1,3,6,1,4,1,28097,5,10,1),_AlarmSettingsLan7DownEnable_Type())
alarmSettingsLan7DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan7DownEnable.setStatus(_A)
class _AlarmSettingsLan7DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan7DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan7DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan7DownEnableAutomaticReset=_AlarmSettingsLan7DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,10,2),_AlarmSettingsLan7DownEnableAutomaticReset_Type())
alarmSettingsLan7DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan7DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan7DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan7DownStatus_Type.__name__=_C
_AlarmSettingsLan7DownStatus_Object=MibScalar
alarmSettingsLan7DownStatus=_AlarmSettingsLan7DownStatus_Object((1,3,6,1,4,1,28097,5,10,3),_AlarmSettingsLan7DownStatus_Type())
alarmSettingsLan7DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan7DownStatus.setStatus(_A)
_AlarmSettingsLan8Down_ObjectIdentity=ObjectIdentity
alarmSettingsLan8Down=_AlarmSettingsLan8Down_ObjectIdentity((1,3,6,1,4,1,28097,5,11))
class _AlarmSettingsLan8DownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan8DownEnable_Type.__name__=_C
_AlarmSettingsLan8DownEnable_Object=MibScalar
alarmSettingsLan8DownEnable=_AlarmSettingsLan8DownEnable_Object((1,3,6,1,4,1,28097,5,11,1),_AlarmSettingsLan8DownEnable_Type())
alarmSettingsLan8DownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan8DownEnable.setStatus(_A)
class _AlarmSettingsLan8DownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsLan8DownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsLan8DownEnableAutomaticReset_Object=MibScalar
alarmSettingsLan8DownEnableAutomaticReset=_AlarmSettingsLan8DownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,11,2),_AlarmSettingsLan8DownEnableAutomaticReset_Type())
alarmSettingsLan8DownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan8DownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsLan8DownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsLan8DownStatus_Type.__name__=_C
_AlarmSettingsLan8DownStatus_Object=MibScalar
alarmSettingsLan8DownStatus=_AlarmSettingsLan8DownStatus_Object((1,3,6,1,4,1,28097,5,11,3),_AlarmSettingsLan8DownStatus_Type())
alarmSettingsLan8DownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsLan8DownStatus.setStatus(_A)
_AlarmSettingsWLANDown_ObjectIdentity=ObjectIdentity
alarmSettingsWLANDown=_AlarmSettingsWLANDown_ObjectIdentity((1,3,6,1,4,1,28097,5,12))
class _AlarmSettingsWLANDownEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsWLANDownEnable_Type.__name__=_C
_AlarmSettingsWLANDownEnable_Object=MibScalar
alarmSettingsWLANDownEnable=_AlarmSettingsWLANDownEnable_Object((1,3,6,1,4,1,28097,5,12,1),_AlarmSettingsWLANDownEnable_Type())
alarmSettingsWLANDownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsWLANDownEnable.setStatus(_A)
class _AlarmSettingsWLANDownEnableAutomaticReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AlarmSettingsWLANDownEnableAutomaticReset_Type.__name__=_C
_AlarmSettingsWLANDownEnableAutomaticReset_Object=MibScalar
alarmSettingsWLANDownEnableAutomaticReset=_AlarmSettingsWLANDownEnableAutomaticReset_Object((1,3,6,1,4,1,28097,5,12,2),_AlarmSettingsWLANDownEnableAutomaticReset_Type())
alarmSettingsWLANDownEnableAutomaticReset.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsWLANDownEnableAutomaticReset.setStatus(_A)
class _AlarmSettingsWLANDownStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,3)))
_AlarmSettingsWLANDownStatus_Type.__name__=_C
_AlarmSettingsWLANDownStatus_Object=MibScalar
alarmSettingsWLANDownStatus=_AlarmSettingsWLANDownStatus_Object((1,3,6,1,4,1,28097,5,12,3),_AlarmSettingsWLANDownStatus_Type())
alarmSettingsWLANDownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmSettingsWLANDownStatus.setStatus(_A)
_PowerStatus_ObjectIdentity=ObjectIdentity
powerStatus=_PowerStatus_ObjectIdentity((1,3,6,1,4,1,28097,6))
class _PowerStatus_PW1_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_PowerStatus_PW1_state_Type.__name__=_C
_PowerStatus_PW1_state_Object=MibScalar
powerStatus_PW1_state=_PowerStatus_PW1_state_Object((1,3,6,1,4,1,28097,6,1),_PowerStatus_PW1_state_Type())
powerStatus_PW1_state.setMaxAccess(_F)
if mibBuilder.loadTexts:powerStatus_PW1_state.setStatus(_A)
class _PowerStatus_PW2_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_PowerStatus_PW2_state_Type.__name__=_C
_PowerStatus_PW2_state_Object=MibScalar
powerStatus_PW2_state=_PowerStatus_PW2_state_Object((1,3,6,1,4,1,28097,6,2),_PowerStatus_PW2_state_Type())
powerStatus_PW2_state.setMaxAccess(_F)
if mibBuilder.loadTexts:powerStatus_PW2_state.setStatus(_A)
mibBuilder.exportSymbols(_J,**{_K:DisplayString,_W:PhysAddress,'acksys':acksys,'network-product':network_product,'wifiInterface':wifiInterface,'settings':settings,'settingInterfaceSsid':settingInterfaceSsid,'settingInterfaceWifiMode':settingInterfaceWifiMode,'settingInterfaceChannel':settingInterfaceChannel,'settingInterface80211Mode':settingInterface80211Mode,'settingInterfaceSuper-a-g-Mode':settingInterfaceSuper_a_g_Mode,'settingEnableRadio':settingEnableRadio,'settingTxPoxer':settingTxPoxer,'settingRegion':settingRegion,'securitySettings':securitySettings,'securityMode':securityMode,'securityWEP':securityWEP,'securityModeWepKeyLen':securityModeWepKeyLen,'securityModeWepKey-1':securityModeWepKey_1,'securityModeWepKey-2':securityModeWepKey_2,'securityModeWepKey-3':securityModeWepKey_3,'securityModeWepKey-4':securityModeWepKey_4,'securityModeDefaultWepKey':securityModeDefaultWepKey,'securityModeWepAuthentication':securityModeWepAuthentication,'securityWPA-WPA2':securityWPA_WPA2,'securityPresharedKey':securityPresharedKey,'securityModeWpaPresharedKey':securityModeWpaPresharedKey,'securityRadius':securityRadius,'securityModeWPARadiusAuthenticationTimeout':securityModeWPARadiusAuthenticationTimeout,'securityModeWPARadiusIP':securityModeWPARadiusIP,'securityModeWPARadiusPort':securityModeWPARadiusPort,'securityModeWPARadiusSecret':securityModeWPARadiusSecret,'securityModeWPARadiusMacAddressAuthentication':securityModeWPARadiusMacAddressAuthentication,'securityRadiusAP':securityRadiusAP,'securityModeWPARadiusAPAuthenticationTimeout':securityModeWPARadiusAPAuthenticationTimeout,'securityModeWPARadiusAPIP':securityModeWPARadiusAPIP,'securityModeWPARadiusAPPort':securityModeWPARadiusAPPort,'securityModeWPARadiusAPSecret':securityModeWPARadiusAPSecret,'securityModeWPARadiusAPMacAddressAuthentication':securityModeWPARadiusAPMacAddressAuthentication,'securityRadiusAPBackup':securityRadiusAPBackup,'securityModeWPABackupRadiusAPIP':securityModeWPABackupRadiusAPIP,'securityModeWPARadiusBackupAPPort':securityModeWPARadiusBackupAPPort,'securityModeWPARadiusBackupAPSecret':securityModeWPARadiusBackupAPSecret,'securityModeWPABackupRadiusAPMacAddressAuthentication':securityModeWPABackupRadiusAPMacAddressAuthentication,'securityRadiusBridge':securityRadiusBridge,'securityModeWPARadiusLogin':securityModeWPARadiusLogin,'securityModeWPARadiusPassword':securityModeWPARadiusPassword,'securityBackupRadius':securityBackupRadius,'securityModeWPABackupRadiusIP':securityModeWPABackupRadiusIP,'securityModeWPARadiusBackupPort':securityModeWPARadiusBackupPort,'securityModeWPARadiusBackupSecret':securityModeWPARadiusBackupSecret,'securityModeWPABackupRadiusMacAddressAuthentication':securityModeWPABackupRadiusMacAddressAuthentication,'securityModeWpaMode':securityModeWpaMode,'securityModeWpaCipherType':securityModeWpaCipherType,'securityModeWpaKeyUpdateInterval':securityModeWpaKeyUpdateInterval,'settingAntennaChoice':settingAntennaChoice,'settingTransmisionRate':settingTransmisionRate,'settingFlagUdapnopassword':settingFlagUdapnopassword,'settingFlagFiltersamenet':settingFlagFiltersamenet,'settingFlagFilterframecosom':settingFlagFilterframecosom,'settingDFSsupport':settingDFSsupport,'settingFilterCustomIpAddr':settingFilterCustomIpAddr,'settingFilterCustomSubnetMask':settingFilterCustomSubnetMask,'bridge-mode':bridge_mode,'bridge-modeLinkStatus':bridge_modeLinkStatus,'bridge-modeMacAP':bridge_modeMacAP,'bridge-modeRSSI':bridge_modeRSSI,'bridge-modeRSSIdBm':bridge_modeRSSIdBm,'bridge-modeRSSIPercent':bridge_modeRSSIPercent,'bridge-modeCurrentTxRate':bridge_modeCurrentTxRate,'bridge-WirelessMode':bridge_WirelessMode,'bridgeAPFiltering':bridgeAPFiltering,'bridgeAPFilteringEnable':bridgeAPFilteringEnable,'bridgeAPFilteringMode':bridgeAPFilteringMode,'bridgeAPFilteringMACAddress':bridgeAPFilteringMACAddress,'bridgeAPFilteringName':bridgeAPFilteringName,'bridgeAPFilteringSave':bridgeAPFilteringSave,'bridgeAPFilteringDelete':bridgeAPFilteringDelete,'bridgeAPFilteringEnableRule':bridgeAPFilteringEnableRule,'bridgeAPFilteringDisableRule':bridgeAPFilteringDisableRule,'bridgeAPFilteringTable':bridgeAPFilteringTable,'bridgeAPFilteringEntry':bridgeAPFilteringEntry,_X:bridgeAPFilteringListId,'bridgeAPFilteringListName':bridgeAPFilteringListName,'bridgeAPFilteringListMAC':bridgeAPFilteringListMAC,'bridgeAPFilteringListEnable':bridgeAPFilteringListEnable,'bridgeRoaming':bridgeRoaming,'bridgeRoamingAdvanced':bridgeRoamingAdvanced,'bridgeRoamingAdvancedScanThreshold-dbm':bridgeRoamingAdvancedScanThreshold_dbm,'bridgeRoamingAdvancedScanThreshold-percent':bridgeRoamingAdvancedScanThreshold_percent,'bridgeRoamingAdvancedScanPeriod':bridgeRoamingAdvancedScanPeriod,'bridgeRoamingAdvancedScanDuration':bridgeRoamingAdvancedScanDuration,'bridgeRoamingAdvancedAPLossDetection':bridgeRoamingAdvancedAPLossDetection,'bridgeRoamingEnable':bridgeRoamingEnable,'bridgeRoamingRSSIThreshold-dBm':bridgeRoamingRSSIThreshold_dBm,'bridgeRoamingRSSIThreshold-percent':bridgeRoamingRSSIThreshold_percent,'bridgeChannelList':bridgeChannelList,'bridgeWirelessScan':bridgeWirelessScan,'bridgeWileressScanTable':bridgeWileressScanTable,'bridgeWirelessScanEntry':bridgeWirelessScanEntry,'bridgeWirelessScanAPMac':bridgeWirelessScanAPMac,'bridgeWirelessScanSSID':bridgeWirelessScanSSID,'bridgeWirelessScanChannel':bridgeWirelessScanChannel,'bridgeWirelessScanMode':bridgeWirelessScanMode,'bridgeWirelessScanSecurity':bridgeWirelessScanSecurity,'bridgeWirelessScanRssi':bridgeWirelessScanRssi,'bridgeNAT':bridgeNAT,'brigeNATStatus':brigeNATStatus,'brigeNATEnablePing':brigeNATEnablePing,'brigeNATEnableProductWebServer':brigeNATEnableProductWebServer,'brigeNATInternalWebServerPort':brigeNATInternalWebServerPort,'brigeNATEnableProductSnmpServer':brigeNATEnableProductSnmpServer,'brigeNATInternalWebSnmpPort':brigeNATInternalWebSnmpPort,'brigeNATWanIpAddrMode':brigeNATWanIpAddrMode,'brigeNATWanIpAddr':brigeNATWanIpAddr,'brigeNATWanSubnetMask':brigeNATWanSubnetMask,'brigeNATWanGateway':brigeNATWanGateway,'bridgeNatPortForwarding':bridgeNatPortForwarding,'bridgeNatPortForwardingTable':bridgeNatPortForwardingTable,'bridgeNatPortForwardingEntry':bridgeNatPortForwardingEntry,_Z:bridgeNatPortForwardingListId,'bridgeNatPortForwardingListName':bridgeNatPortForwardingListName,'bridgeNatPortForwardingListIpAddr':bridgeNatPortForwardingListIpAddr,'bridgeNatPortForwardingListPublicTcpPort':bridgeNatPortForwardingListPublicTcpPort,'bridgeNatPortForwardingListPrivateTcpPort':bridgeNatPortForwardingListPrivateTcpPort,'bridgeNatPortForwardingListPublicUdpPort':bridgeNatPortForwardingListPublicUdpPort,'bridgeNatPortForwardingListPrivateUdpPort':bridgeNatPortForwardingListPrivateUdpPort,'bridgeNatPortForwardingListEnable':bridgeNatPortForwardingListEnable,'bridgeNatPortForwardingName':bridgeNatPortForwardingName,'bridgeNatPortForwardingIpAddr':bridgeNatPortForwardingIpAddr,'bridgeNatPortForwardingPublicTcpPort':bridgeNatPortForwardingPublicTcpPort,'bridgeNatPortForwardingPrivateTcpPort':bridgeNatPortForwardingPrivateTcpPort,'bridgeNatPortForwardingPublicUdpPort':bridgeNatPortForwardingPublicUdpPort,'bridgeNatPortForwardingPrivateUdpPort':bridgeNatPortForwardingPrivateUdpPort,'bridgeNatPortForwardingEnableRule':bridgeNatPortForwardingEnableRule,'bridgeNatPortForwardingDisableRule':bridgeNatPortForwardingDisableRule,'bridgeNatPortForwardingSaveRule':bridgeNatPortForwardingSaveRule,'bridgeNatPortForwardingDeleteRule':bridgeNatPortForwardingDeleteRule,'access-point-mode':access_point_mode,'apClientTable':apClientTable,'apClientEntry':apClientEntry,_a:clientMacAddr,'client80211Mode':client80211Mode,'clientTxRate':clientTxRate,'clientRssiPercent':clientRssiPercent,'apAutomaticChannel':apAutomaticChannel,'apClientCount':apClientCount,'apClientFiltering':apClientFiltering,'apClientFilteringEnable':apClientFilteringEnable,'apClientFilteringMode':apClientFilteringMode,'apClientWirelessFiltering':apClientWirelessFiltering,'apClientWiredFiltering':apClientWiredFiltering,'apClientFilteringMACAddress':apClientFilteringMACAddress,'apClientFilteringName':apClientFilteringName,'apClientFilteringSave':apClientFilteringSave,'apClientFilteringDelete':apClientFilteringDelete,'apClientFilteringEnableRule':apClientFilteringEnableRule,'apClientFilteringDisableRule':apClientFilteringDisableRule,'apClientFilteringTable':apClientFilteringTable,'apClientFilteringEntry':apClientFilteringEntry,_V:apClientFilteringListId,'apClientFilteringListName':apClientFilteringListName,'apClientFilteringListMAC':apClientFilteringListMAC,'apClientFilteringListEnable':apClientFilteringListEnable,'wds':wds,'apWDSEnable':apWDSEnable,'apWDSEnableSTP':apWDSEnableSTP,'apWDSMAC1':apWDSMAC1,'apWDSMAC2':apWDSMAC2,'apWDSMAC3':apWDSMAC3,'apWDSMAC4':apWDSMAC4,'apWDSMAC5':apWDSMAC5,'apWDSMAC6':apWDSMAC6,'settingSSIDVisibility':settingSSIDVisibility,'enableSTP':enableSTP,'lanTimeOutSettings':lanTimeOutSettings,'enableLanTimeout':enableLanTimeout,'lanTimeoutIPSurvey':lanTimeoutIPSurvey,'lanTimeoutMaxProbe':lanTimeoutMaxProbe,'lanTimeoutProbeTimeout':lanTimeoutProbeTimeout,'lanTimeoutProbeInterval':lanTimeoutProbeInterval,'advancedSettings':advancedSettings,'longDistanceSettings':longDistanceSettings,'enableLongDistance':enableLongDistance,'distanceAntennaMeter':distanceAntennaMeter,'distanceSlotTime':distanceSlotTime,'distanceAckTimeout':distanceAckTimeout,'distanceCtsTimeout':distanceCtsTimeout,'enable802-11d':enable802_11d,'enableIsolateSTA':enableIsolateSTA,'administration':administration,'adminReset':adminReset,'adminResetFactory':adminResetFactory,'adminEnableWebServer':adminEnableWebServer,'adminAutoSave':adminAutoSave,'adminSave':adminSave,'os-stat':os_stat,'os-statFreeHeap':os_statFreeHeap,'os-statTotalHeap':os_statTotalHeap,'os-statHeapLowWater':os_statHeapLowWater,'os-statNetpageFree':os_statNetpageFree,'os-statNetpageLowWater':os_statNetpageLowWater,'productSpecific':productSpecific,'wlg-aboard':wlg_aboard,'wlg-aboard-PW1-state':wlg_aboard_PW1_state,'wlg-aboard-PW2-state':wlg_aboard_PW2_state,'lanInterface':lanInterface,'lanInterfaceIpAddrMode':lanInterfaceIpAddrMode,'lanInterfaceIpAddr':lanInterfaceIpAddr,'lanInterfaceSubNetMask':lanInterfaceSubNetMask,'lanInterfaceGatewayIp':lanInterfaceGatewayIp,'lanInterfaceHostName':lanInterfaceHostName,'lanInterfaceLocalDomainName':lanInterfaceLocalDomainName,'acksysMIB':acksysMIB,'acksysProductID':acksysProductID,'c-key-management':c_key_management,'ckeyManagementCopySettingTo':ckeyManagementCopySettingTo,'ckeyManagementCopySettingFrom':ckeyManagementCopySettingFrom,'alarmSettings':alarmSettings,'alarmSettingsTest':alarmSettingsTest,'alarmSettingsPower1Down':alarmSettingsPower1Down,'alarmSettingsPower1DownEnable':alarmSettingsPower1DownEnable,'alarmSettingsPower1DownEnableAutomaticReset':alarmSettingsPower1DownEnableAutomaticReset,'alarmSettingsPower1DownStatus':alarmSettingsPower1DownStatus,'alarmSettingsPower2Down':alarmSettingsPower2Down,'alarmSettingsPower2DownEnable':alarmSettingsPower2DownEnable,'alarmSettingsPower2DownEnableAutomaticReset':alarmSettingsPower2DownEnableAutomaticReset,'alarmSettingsPower2DownStatus':alarmSettingsPower2DownStatus,'alarmSettingsLan1Down':alarmSettingsLan1Down,'alarmSettingsLan1DownEnable':alarmSettingsLan1DownEnable,'alarmSettingsLan1DownEnableAutomaticReset':alarmSettingsLan1DownEnableAutomaticReset,'alarmSettingsLan1DownStatus':alarmSettingsLan1DownStatus,'alarmSettingsLan2Down':alarmSettingsLan2Down,'alarmSettingsLan2DownEnable':alarmSettingsLan2DownEnable,'alarmSettingsLan2DownEnableAutomaticReset':alarmSettingsLan2DownEnableAutomaticReset,'alarmSettingsLan2DownStatus':alarmSettingsLan2DownStatus,'alarmSettingsLan3Down':alarmSettingsLan3Down,'alarmSettingsLan3DownEnable':alarmSettingsLan3DownEnable,'alarmSettingsLan3DownEnableAutomaticReset':alarmSettingsLan3DownEnableAutomaticReset,'alarmSettingsLan3DownStatus':alarmSettingsLan3DownStatus,'alarmSettingsLan4Down':alarmSettingsLan4Down,'alarmSettingsLan4DownEnable':alarmSettingsLan4DownEnable,'alarmSettingsLan4DownEnableAutomaticReset':alarmSettingsLan4DownEnableAutomaticReset,'alarmSettingsLan4DownStatus':alarmSettingsLan4DownStatus,'alarmSettingsLan5Down':alarmSettingsLan5Down,'alarmSettingsLan5DownEnable':alarmSettingsLan5DownEnable,'alarmSettingsLan5DownEnableAutomaticReset':alarmSettingsLan5DownEnableAutomaticReset,'alarmSettingsLan5DownStatus':alarmSettingsLan5DownStatus,'alarmSettingsLan6Down':alarmSettingsLan6Down,'alarmSettingsLan6DownEnable':alarmSettingsLan6DownEnable,'alarmSettingsLan6DownEnableAutomaticReset':alarmSettingsLan6DownEnableAutomaticReset,'alarmSettingsLan6DownStatus':alarmSettingsLan6DownStatus,'alarmSettingsLan7Down':alarmSettingsLan7Down,'alarmSettingsLan7DownEnable':alarmSettingsLan7DownEnable,'alarmSettingsLan7DownEnableAutomaticReset':alarmSettingsLan7DownEnableAutomaticReset,'alarmSettingsLan7DownStatus':alarmSettingsLan7DownStatus,'alarmSettingsLan8Down':alarmSettingsLan8Down,'alarmSettingsLan8DownEnable':alarmSettingsLan8DownEnable,'alarmSettingsLan8DownEnableAutomaticReset':alarmSettingsLan8DownEnableAutomaticReset,'alarmSettingsLan8DownStatus':alarmSettingsLan8DownStatus,'alarmSettingsWLANDown':alarmSettingsWLANDown,'alarmSettingsWLANDownEnable':alarmSettingsWLANDownEnable,'alarmSettingsWLANDownEnableAutomaticReset':alarmSettingsWLANDownEnableAutomaticReset,'alarmSettingsWLANDownStatus':alarmSettingsWLANDownStatus,'powerStatus':powerStatus,'powerStatus-PW1-state':powerStatus_PW1_state,'powerStatus-PW2-state':powerStatus_PW2_state})