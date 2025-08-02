_A7='rcDot11AssociationSecurity'
_A6='rcDot11AssociationRxSeq'
_A5='rcDot11AssociationTxSeq'
_A4='rcDot11AssociationRssi'
_A3='rcDot11AssociationRate'
_A2='rcDot11AssociationChannel'
_A1='rcDot11RowStatus'
_A0='rcDot11MacFilteringControl'
_z='rcDot11DhcpLeaseTime'
_y='rcDot11DhcpDnsIpAddress'
_x='rcDot11DhcpGateway'
_w='rcDot11DhcpSubnet'
_v='rcDot11DhcpIpPoolSize'
_u='rcDot11DhcpStartOfPool'
_t='rcDot11DhcpServerEnable'
_s='rcDot11SecurityRadiusSecret'
_r='rcDot11SecurityRadiusPort'
_q='rcDot11SecurityRadiusIpAddress'
_p='rcDot11SecurityKeyRenewal'
_o='rcDot11SecurityWepKey'
_n='rcDot11SecurityPassPhrase'
_m='rcDot11SecurityEncrypType'
_l='rcDot11SecurityAuthMode'
_k='rcDot11NetworkDistance'
_j='rcDot11NetworkTxShortPreamble'
_i='rcDot11NetworkWmmEnable'
_h='rcDot11NetworkWdsEnable'
_g='rcDot11NetworkTxPower'
_f='rcDot11NetworkRate'
_e='rcDot11NetworkRfTxEnable'
_d='rcDot11NetworkAssociatedStations'
_c='rcDot11NetworkSsidTxSuppress'
_b='rcDot11NetworkRfChannel'
_a='rcDot11NetworkSecondary2Ssid'
_Z='rcDot11NetworkSecondary1Ssid'
_Y='rcDot11NetworkPrimarySsid'
_X='rcDot11NetworkDesiredSsid'
_W='rcDot11NetworkPhyMode'
_V='rcDot11WlanReset'
_U='rcDot11SwUpgradeStatus'
_T='rcDot11SwUpgrade'
_S='rcDot11TftpServerIpAddress'
_R='rcDot11Version'
_Q='rcDot11UpTime'
_P='rcDot11Status'
_O='rcDot11DefaultGateway'
_N='rcDot11IpSubnet'
_M='rcDot11IpAddress'
_L='rcDot11RFMAC'
_K='rcDot11OpMode'
_J='rcDot11AssociationMac'
_I='not-accessible'
_H='rcDot11FilterMacAddress'
_G='Unsigned32'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='RUGGEDCOM-DOT11-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
rcDot11=ModuleIdentity((1,3,6,1,4,1,15004,4,4))
_RcDot11GlobalParams_ObjectIdentity=ObjectIdentity
rcDot11GlobalParams=_RcDot11GlobalParams_ObjectIdentity((1,3,6,1,4,1,15004,4,4,1))
if mibBuilder.loadTexts:rcDot11GlobalParams.setStatus(_A)
class _RcDot11OpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ap',1),('clientBridge',2),('clientIpBridge',3)))
_RcDot11OpMode_Type.__name__=_D
_RcDot11OpMode_Object=MibScalar
rcDot11OpMode=_RcDot11OpMode_Object((1,3,6,1,4,1,15004,4,4,1,1),_RcDot11OpMode_Type())
rcDot11OpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11OpMode.setStatus(_A)
_RcDot11RFMAC_Type=MacAddress
_RcDot11RFMAC_Object=MibScalar
rcDot11RFMAC=_RcDot11RFMAC_Object((1,3,6,1,4,1,15004,4,4,1,2),_RcDot11RFMAC_Type())
rcDot11RFMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11RFMAC.setStatus(_A)
_RcDot11IpAddress_Type=IpAddress
_RcDot11IpAddress_Object=MibScalar
rcDot11IpAddress=_RcDot11IpAddress_Object((1,3,6,1,4,1,15004,4,4,1,3),_RcDot11IpAddress_Type())
rcDot11IpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11IpAddress.setStatus(_A)
_RcDot11IpSubnet_Type=IpAddress
_RcDot11IpSubnet_Object=MibScalar
rcDot11IpSubnet=_RcDot11IpSubnet_Object((1,3,6,1,4,1,15004,4,4,1,4),_RcDot11IpSubnet_Type())
rcDot11IpSubnet.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11IpSubnet.setStatus(_A)
_RcDot11DefaultGateway_Type=IpAddress
_RcDot11DefaultGateway_Object=MibScalar
rcDot11DefaultGateway=_RcDot11DefaultGateway_Object((1,3,6,1,4,1,15004,4,4,1,5),_RcDot11DefaultGateway_Type())
rcDot11DefaultGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11DefaultGateway.setStatus(_A)
class _RcDot11Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('booting',2),('running',3),('cmdProcessing',4),('softwareUpgrade',5)))
_RcDot11Status_Type.__name__=_D
_RcDot11Status_Object=MibScalar
rcDot11Status=_RcDot11Status_Object((1,3,6,1,4,1,15004,4,4,1,6),_RcDot11Status_Type())
rcDot11Status.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11Status.setStatus(_A)
_RcDot11UpTime_Type=DisplayString
_RcDot11UpTime_Object=MibScalar
rcDot11UpTime=_RcDot11UpTime_Object((1,3,6,1,4,1,15004,4,4,1,7),_RcDot11UpTime_Type())
rcDot11UpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11UpTime.setStatus(_A)
_RcDot11Version_Type=DisplayString
_RcDot11Version_Object=MibScalar
rcDot11Version=_RcDot11Version_Object((1,3,6,1,4,1,15004,4,4,1,8),_RcDot11Version_Type())
rcDot11Version.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11Version.setStatus(_A)
_RcDot11TftpServerIpAddress_Type=IpAddress
_RcDot11TftpServerIpAddress_Object=MibScalar
rcDot11TftpServerIpAddress=_RcDot11TftpServerIpAddress_Object((1,3,6,1,4,1,15004,4,4,1,9),_RcDot11TftpServerIpAddress_Type())
rcDot11TftpServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11TftpServerIpAddress.setStatus(_A)
_RcDot11SwUpgrade_Type=TruthValue
_RcDot11SwUpgrade_Object=MibScalar
rcDot11SwUpgrade=_RcDot11SwUpgrade_Object((1,3,6,1,4,1,15004,4,4,1,10),_RcDot11SwUpgrade_Type())
rcDot11SwUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SwUpgrade.setStatus(_A)
_RcDot11SwUpgradeStatus_Type=DisplayString
_RcDot11SwUpgradeStatus_Object=MibScalar
rcDot11SwUpgradeStatus=_RcDot11SwUpgradeStatus_Object((1,3,6,1,4,1,15004,4,4,1,11),_RcDot11SwUpgradeStatus_Type())
rcDot11SwUpgradeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11SwUpgradeStatus.setStatus(_A)
class _RcDot11WlanReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('fullReset',2),('quickReset',3)))
_RcDot11WlanReset_Type.__name__=_D
_RcDot11WlanReset_Object=MibScalar
rcDot11WlanReset=_RcDot11WlanReset_Object((1,3,6,1,4,1,15004,4,4,1,12),_RcDot11WlanReset_Type())
rcDot11WlanReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11WlanReset.setStatus(_A)
_RcDot11NetworkParams_ObjectIdentity=ObjectIdentity
rcDot11NetworkParams=_RcDot11NetworkParams_ObjectIdentity((1,3,6,1,4,1,15004,4,4,2))
if mibBuilder.loadTexts:rcDot11NetworkParams.setStatus(_A)
class _RcDot11NetworkPhyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('dot11b',2),('dot11g',3)))
_RcDot11NetworkPhyMode_Type.__name__=_D
_RcDot11NetworkPhyMode_Object=MibScalar
rcDot11NetworkPhyMode=_RcDot11NetworkPhyMode_Object((1,3,6,1,4,1,15004,4,4,2,1),_RcDot11NetworkPhyMode_Type())
rcDot11NetworkPhyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkPhyMode.setStatus(_A)
class _RcDot11NetworkDesiredSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,32))
_RcDot11NetworkDesiredSsid_Type.__name__=_F
_RcDot11NetworkDesiredSsid_Object=MibScalar
rcDot11NetworkDesiredSsid=_RcDot11NetworkDesiredSsid_Object((1,3,6,1,4,1,15004,4,4,2,2),_RcDot11NetworkDesiredSsid_Type())
rcDot11NetworkDesiredSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkDesiredSsid.setStatus(_A)
class _RcDot11NetworkPrimarySsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,32))
_RcDot11NetworkPrimarySsid_Type.__name__=_F
_RcDot11NetworkPrimarySsid_Object=MibScalar
rcDot11NetworkPrimarySsid=_RcDot11NetworkPrimarySsid_Object((1,3,6,1,4,1,15004,4,4,2,3),_RcDot11NetworkPrimarySsid_Type())
rcDot11NetworkPrimarySsid.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkPrimarySsid.setStatus(_A)
class _RcDot11NetworkSecondary1Ssid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,32))
_RcDot11NetworkSecondary1Ssid_Type.__name__=_F
_RcDot11NetworkSecondary1Ssid_Object=MibScalar
rcDot11NetworkSecondary1Ssid=_RcDot11NetworkSecondary1Ssid_Object((1,3,6,1,4,1,15004,4,4,2,4),_RcDot11NetworkSecondary1Ssid_Type())
rcDot11NetworkSecondary1Ssid.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkSecondary1Ssid.setStatus(_A)
class _RcDot11NetworkSecondary2Ssid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,32))
_RcDot11NetworkSecondary2Ssid_Type.__name__=_F
_RcDot11NetworkSecondary2Ssid_Object=MibScalar
rcDot11NetworkSecondary2Ssid=_RcDot11NetworkSecondary2Ssid_Object((1,3,6,1,4,1,15004,4,4,2,5),_RcDot11NetworkSecondary2Ssid_Type())
rcDot11NetworkSecondary2Ssid.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkSecondary2Ssid.setStatus(_A)
class _RcDot11NetworkRfChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,13))
_RcDot11NetworkRfChannel_Type.__name__=_D
_RcDot11NetworkRfChannel_Object=MibScalar
rcDot11NetworkRfChannel=_RcDot11NetworkRfChannel_Object((1,3,6,1,4,1,15004,4,4,2,6),_RcDot11NetworkRfChannel_Type())
rcDot11NetworkRfChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkRfChannel.setStatus(_A)
_RcDot11NetworkSsidTxSuppress_Type=TruthValue
_RcDot11NetworkSsidTxSuppress_Object=MibScalar
rcDot11NetworkSsidTxSuppress=_RcDot11NetworkSsidTxSuppress_Object((1,3,6,1,4,1,15004,4,4,2,7),_RcDot11NetworkSsidTxSuppress_Type())
rcDot11NetworkSsidTxSuppress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkSsidTxSuppress.setStatus(_A)
_RcDot11NetworkRfTxEnable_Type=TruthValue
_RcDot11NetworkRfTxEnable_Object=MibScalar
rcDot11NetworkRfTxEnable=_RcDot11NetworkRfTxEnable_Object((1,3,6,1,4,1,15004,4,4,2,8),_RcDot11NetworkRfTxEnable_Type())
rcDot11NetworkRfTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkRfTxEnable.setStatus(_A)
class _RcDot11NetworkRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('best',1),('mbps1',2),('mbps2',3),('mbps11',4),('mbps12',5),('mbps18',6),('mbps24',7),('mbps36',8),('mbps48',9),('mbps54',10)))
_RcDot11NetworkRate_Type.__name__=_D
_RcDot11NetworkRate_Object=MibScalar
rcDot11NetworkRate=_RcDot11NetworkRate_Object((1,3,6,1,4,1,15004,4,4,2,9),_RcDot11NetworkRate_Type())
rcDot11NetworkRate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkRate.setStatus(_A)
class _RcDot11NetworkTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RcDot11NetworkTxPower_Type.__name__=_D
_RcDot11NetworkTxPower_Object=MibScalar
rcDot11NetworkTxPower=_RcDot11NetworkTxPower_Object((1,3,6,1,4,1,15004,4,4,2,10),_RcDot11NetworkTxPower_Type())
rcDot11NetworkTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkTxPower.setStatus(_A)
_RcDot11NetworkWdsEnable_Type=TruthValue
_RcDot11NetworkWdsEnable_Object=MibScalar
rcDot11NetworkWdsEnable=_RcDot11NetworkWdsEnable_Object((1,3,6,1,4,1,15004,4,4,2,11),_RcDot11NetworkWdsEnable_Type())
rcDot11NetworkWdsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkWdsEnable.setStatus(_A)
_RcDot11NetworkWmmEnable_Type=TruthValue
_RcDot11NetworkWmmEnable_Object=MibScalar
rcDot11NetworkWmmEnable=_RcDot11NetworkWmmEnable_Object((1,3,6,1,4,1,15004,4,4,2,12),_RcDot11NetworkWmmEnable_Type())
rcDot11NetworkWmmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkWmmEnable.setStatus(_A)
_RcDot11NetworkTxShortPreamble_Type=TruthValue
_RcDot11NetworkTxShortPreamble_Object=MibScalar
rcDot11NetworkTxShortPreamble=_RcDot11NetworkTxShortPreamble_Object((1,3,6,1,4,1,15004,4,4,2,13),_RcDot11NetworkTxShortPreamble_Type())
rcDot11NetworkTxShortPreamble.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkTxShortPreamble.setStatus(_A)
class _RcDot11NetworkDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,15000))
_RcDot11NetworkDistance_Type.__name__=_D
_RcDot11NetworkDistance_Object=MibScalar
rcDot11NetworkDistance=_RcDot11NetworkDistance_Object((1,3,6,1,4,1,15004,4,4,2,14),_RcDot11NetworkDistance_Type())
rcDot11NetworkDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11NetworkDistance.setStatus(_A)
class _RcDot11NetworkAssociatedStations_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_RcDot11NetworkAssociatedStations_Type.__name__=_G
_RcDot11NetworkAssociatedStations_Object=MibScalar
rcDot11NetworkAssociatedStations=_RcDot11NetworkAssociatedStations_Object((1,3,6,1,4,1,15004,4,4,2,15),_RcDot11NetworkAssociatedStations_Type())
rcDot11NetworkAssociatedStations.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11NetworkAssociatedStations.setStatus(_A)
_RcDot11SecurityParams_ObjectIdentity=ObjectIdentity
rcDot11SecurityParams=_RcDot11SecurityParams_ObjectIdentity((1,3,6,1,4,1,15004,4,4,3))
if mibBuilder.loadTexts:rcDot11SecurityParams.setStatus(_A)
class _RcDot11SecurityAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',1),('wep',2),('dot1x',3),('wpa',4),('wpaPsk',5),('wpa2',6),('wpa2psk',7),('wpaAuto',8),('wpaAutoPsk',9)))
_RcDot11SecurityAuthMode_Type.__name__=_D
_RcDot11SecurityAuthMode_Object=MibScalar
rcDot11SecurityAuthMode=_RcDot11SecurityAuthMode_Object((1,3,6,1,4,1,15004,4,4,3,1),_RcDot11SecurityAuthMode_Type())
rcDot11SecurityAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityAuthMode.setStatus(_A)
class _RcDot11SecurityEncrypType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('wep',2),('tkip',3),('aes',4)))
_RcDot11SecurityEncrypType_Type.__name__=_D
_RcDot11SecurityEncrypType_Object=MibScalar
rcDot11SecurityEncrypType=_RcDot11SecurityEncrypType_Object((1,3,6,1,4,1,15004,4,4,3,2),_RcDot11SecurityEncrypType_Type())
rcDot11SecurityEncrypType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityEncrypType.setStatus(_A)
class _RcDot11SecurityPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RcDot11SecurityPassPhrase_Type.__name__=_F
_RcDot11SecurityPassPhrase_Object=MibScalar
rcDot11SecurityPassPhrase=_RcDot11SecurityPassPhrase_Object((1,3,6,1,4,1,15004,4,4,3,3),_RcDot11SecurityPassPhrase_Type())
rcDot11SecurityPassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityPassPhrase.setStatus(_A)
class _RcDot11SecurityWepKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10),ValueSizeConstraint(26,26))
_RcDot11SecurityWepKey_Type.__name__=_F
_RcDot11SecurityWepKey_Object=MibScalar
rcDot11SecurityWepKey=_RcDot11SecurityWepKey_Object((1,3,6,1,4,1,15004,4,4,3,4),_RcDot11SecurityWepKey_Type())
rcDot11SecurityWepKey.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityWepKey.setStatus(_A)
_RcDot11SecurityKeyRenewal_Type=TimeTicks
_RcDot11SecurityKeyRenewal_Object=MibScalar
rcDot11SecurityKeyRenewal=_RcDot11SecurityKeyRenewal_Object((1,3,6,1,4,1,15004,4,4,3,5),_RcDot11SecurityKeyRenewal_Type())
rcDot11SecurityKeyRenewal.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityKeyRenewal.setStatus(_A)
_RcDot11SecurityRadiusIpAddress_Type=IpAddress
_RcDot11SecurityRadiusIpAddress_Object=MibScalar
rcDot11SecurityRadiusIpAddress=_RcDot11SecurityRadiusIpAddress_Object((1,3,6,1,4,1,15004,4,4,3,6),_RcDot11SecurityRadiusIpAddress_Type())
rcDot11SecurityRadiusIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityRadiusIpAddress.setStatus(_A)
class _RcDot11SecurityRadiusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcDot11SecurityRadiusPort_Type.__name__=_D
_RcDot11SecurityRadiusPort_Object=MibScalar
rcDot11SecurityRadiusPort=_RcDot11SecurityRadiusPort_Object((1,3,6,1,4,1,15004,4,4,3,7),_RcDot11SecurityRadiusPort_Type())
rcDot11SecurityRadiusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityRadiusPort.setStatus(_A)
class _RcDot11SecurityRadiusSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,48))
_RcDot11SecurityRadiusSecret_Type.__name__=_F
_RcDot11SecurityRadiusSecret_Object=MibScalar
rcDot11SecurityRadiusSecret=_RcDot11SecurityRadiusSecret_Object((1,3,6,1,4,1,15004,4,4,3,8),_RcDot11SecurityRadiusSecret_Type())
rcDot11SecurityRadiusSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11SecurityRadiusSecret.setStatus(_A)
_RcDot11MacFiltering_ObjectIdentity=ObjectIdentity
rcDot11MacFiltering=_RcDot11MacFiltering_ObjectIdentity((1,3,6,1,4,1,15004,4,4,4))
if mibBuilder.loadTexts:rcDot11MacFiltering.setStatus(_A)
class _RcDot11MacFilteringControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),('allow',2),('deny',3)))
_RcDot11MacFilteringControl_Type.__name__=_D
_RcDot11MacFilteringControl_Object=MibScalar
rcDot11MacFilteringControl=_RcDot11MacFilteringControl_Object((1,3,6,1,4,1,15004,4,4,4,1),_RcDot11MacFilteringControl_Type())
rcDot11MacFilteringControl.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11MacFilteringControl.setStatus(_A)
_RcDot11MacFilteringTable_Object=MibTable
rcDot11MacFilteringTable=_RcDot11MacFilteringTable_Object((1,3,6,1,4,1,15004,4,4,4,2))
if mibBuilder.loadTexts:rcDot11MacFilteringTable.setStatus(_A)
_RcDot11MacFilteringEntry_Object=MibTableRow
rcDot11MacFilteringEntry=_RcDot11MacFilteringEntry_Object((1,3,6,1,4,1,15004,4,4,4,2,1))
rcDot11MacFilteringEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:rcDot11MacFilteringEntry.setStatus(_A)
_RcDot11FilterMacAddress_Type=MacAddress
_RcDot11FilterMacAddress_Object=MibTableColumn
rcDot11FilterMacAddress=_RcDot11FilterMacAddress_Object((1,3,6,1,4,1,15004,4,4,4,2,1,1),_RcDot11FilterMacAddress_Type())
rcDot11FilterMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:rcDot11FilterMacAddress.setStatus(_A)
class _RcDot11RowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*(('active',1),('createAndGo',4),('delete',6)))
_RcDot11RowStatus_Type.__name__=_D
_RcDot11RowStatus_Object=MibTableColumn
rcDot11RowStatus=_RcDot11RowStatus_Object((1,3,6,1,4,1,15004,4,4,4,2,1,2),_RcDot11RowStatus_Type())
rcDot11RowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rcDot11RowStatus.setStatus(_A)
_RcDot11DhcpParams_ObjectIdentity=ObjectIdentity
rcDot11DhcpParams=_RcDot11DhcpParams_ObjectIdentity((1,3,6,1,4,1,15004,4,4,5))
if mibBuilder.loadTexts:rcDot11DhcpParams.setStatus(_A)
_RcDot11DhcpServerEnable_Type=TruthValue
_RcDot11DhcpServerEnable_Object=MibScalar
rcDot11DhcpServerEnable=_RcDot11DhcpServerEnable_Object((1,3,6,1,4,1,15004,4,4,5,1),_RcDot11DhcpServerEnable_Type())
rcDot11DhcpServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpServerEnable.setStatus(_A)
_RcDot11DhcpStartOfPool_Type=IpAddress
_RcDot11DhcpStartOfPool_Object=MibScalar
rcDot11DhcpStartOfPool=_RcDot11DhcpStartOfPool_Object((1,3,6,1,4,1,15004,4,4,5,2),_RcDot11DhcpStartOfPool_Type())
rcDot11DhcpStartOfPool.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpStartOfPool.setStatus(_A)
class _RcDot11DhcpIpPoolSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_RcDot11DhcpIpPoolSize_Type.__name__=_D
_RcDot11DhcpIpPoolSize_Object=MibScalar
rcDot11DhcpIpPoolSize=_RcDot11DhcpIpPoolSize_Object((1,3,6,1,4,1,15004,4,4,5,3),_RcDot11DhcpIpPoolSize_Type())
rcDot11DhcpIpPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpIpPoolSize.setStatus(_A)
_RcDot11DhcpSubnet_Type=IpAddress
_RcDot11DhcpSubnet_Object=MibScalar
rcDot11DhcpSubnet=_RcDot11DhcpSubnet_Object((1,3,6,1,4,1,15004,4,4,5,4),_RcDot11DhcpSubnet_Type())
rcDot11DhcpSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpSubnet.setStatus(_A)
_RcDot11DhcpGateway_Type=IpAddress
_RcDot11DhcpGateway_Object=MibScalar
rcDot11DhcpGateway=_RcDot11DhcpGateway_Object((1,3,6,1,4,1,15004,4,4,5,5),_RcDot11DhcpGateway_Type())
rcDot11DhcpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpGateway.setStatus(_A)
_RcDot11DhcpDnsIpAddress_Type=IpAddress
_RcDot11DhcpDnsIpAddress_Object=MibScalar
rcDot11DhcpDnsIpAddress=_RcDot11DhcpDnsIpAddress_Object((1,3,6,1,4,1,15004,4,4,5,6),_RcDot11DhcpDnsIpAddress_Type())
rcDot11DhcpDnsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpDnsIpAddress.setStatus(_A)
_RcDot11DhcpLeaseTime_Type=TimeTicks
_RcDot11DhcpLeaseTime_Object=MibScalar
rcDot11DhcpLeaseTime=_RcDot11DhcpLeaseTime_Object((1,3,6,1,4,1,15004,4,4,5,7),_RcDot11DhcpLeaseTime_Type())
rcDot11DhcpLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDot11DhcpLeaseTime.setStatus(_A)
_RcDot11AssociationInfo_ObjectIdentity=ObjectIdentity
rcDot11AssociationInfo=_RcDot11AssociationInfo_ObjectIdentity((1,3,6,1,4,1,15004,4,4,6))
if mibBuilder.loadTexts:rcDot11AssociationInfo.setStatus(_A)
_RcDot11AssociationTable_Object=MibTable
rcDot11AssociationTable=_RcDot11AssociationTable_Object((1,3,6,1,4,1,15004,4,4,6,1))
if mibBuilder.loadTexts:rcDot11AssociationTable.setStatus(_A)
_RcDot11AssociationEntry_Object=MibTableRow
rcDot11AssociationEntry=_RcDot11AssociationEntry_Object((1,3,6,1,4,1,15004,4,4,6,1,1))
rcDot11AssociationEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:rcDot11AssociationEntry.setStatus(_A)
_RcDot11AssociationMac_Type=MacAddress
_RcDot11AssociationMac_Object=MibTableColumn
rcDot11AssociationMac=_RcDot11AssociationMac_Object((1,3,6,1,4,1,15004,4,4,6,1,1,1),_RcDot11AssociationMac_Type())
rcDot11AssociationMac.setMaxAccess(_I)
if mibBuilder.loadTexts:rcDot11AssociationMac.setStatus(_A)
_RcDot11AssociationChannel_Type=Unsigned32
_RcDot11AssociationChannel_Object=MibTableColumn
rcDot11AssociationChannel=_RcDot11AssociationChannel_Object((1,3,6,1,4,1,15004,4,4,6,1,1,2),_RcDot11AssociationChannel_Type())
rcDot11AssociationChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11AssociationChannel.setStatus(_A)
_RcDot11AssociationRate_Type=Unsigned32
_RcDot11AssociationRate_Object=MibTableColumn
rcDot11AssociationRate=_RcDot11AssociationRate_Object((1,3,6,1,4,1,15004,4,4,6,1,1,3),_RcDot11AssociationRate_Type())
rcDot11AssociationRate.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11AssociationRate.setStatus(_A)
_RcDot11AssociationRssi_Type=Unsigned32
_RcDot11AssociationRssi_Object=MibTableColumn
rcDot11AssociationRssi=_RcDot11AssociationRssi_Object((1,3,6,1,4,1,15004,4,4,6,1,1,4),_RcDot11AssociationRssi_Type())
rcDot11AssociationRssi.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11AssociationRssi.setStatus(_A)
_RcDot11AssociationTxSeq_Type=Unsigned32
_RcDot11AssociationTxSeq_Object=MibTableColumn
rcDot11AssociationTxSeq=_RcDot11AssociationTxSeq_Object((1,3,6,1,4,1,15004,4,4,6,1,1,5),_RcDot11AssociationTxSeq_Type())
rcDot11AssociationTxSeq.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11AssociationTxSeq.setStatus(_A)
_RcDot11AssociationRxSeq_Type=Unsigned32
_RcDot11AssociationRxSeq_Object=MibTableColumn
rcDot11AssociationRxSeq=_RcDot11AssociationRxSeq_Object((1,3,6,1,4,1,15004,4,4,6,1,1,6),_RcDot11AssociationRxSeq_Type())
rcDot11AssociationRxSeq.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11AssociationRxSeq.setStatus(_A)
_RcDot11AssociationSecurity_Type=OctetString
_RcDot11AssociationSecurity_Object=MibTableColumn
rcDot11AssociationSecurity=_RcDot11AssociationSecurity_Object((1,3,6,1,4,1,15004,4,4,6,1,1,7),_RcDot11AssociationSecurity_Type())
rcDot11AssociationSecurity.setMaxAccess(_E)
if mibBuilder.loadTexts:rcDot11AssociationSecurity.setStatus(_A)
_RcDot11Conformance_ObjectIdentity=ObjectIdentity
rcDot11Conformance=_RcDot11Conformance_ObjectIdentity((1,3,6,1,4,1,15004,4,4,10))
_RcDot11Groups_ObjectIdentity=ObjectIdentity
rcDot11Groups=_RcDot11Groups_ObjectIdentity((1,3,6,1,4,1,15004,4,4,10,2))
rcDot11GlobalParamsGroup=ObjectGroup((1,3,6,1,4,1,15004,4,4,10,2,1))
rcDot11GlobalParamsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:rcDot11GlobalParamsGroup.setStatus(_A)
rcDot11NetworkParamsGroup=ObjectGroup((1,3,6,1,4,1,15004,4,4,10,2,2))
rcDot11NetworkParamsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:rcDot11NetworkParamsGroup.setStatus(_A)
rcDot11SecurityParamsGroup=ObjectGroup((1,3,6,1,4,1,15004,4,4,10,2,3))
rcDot11SecurityParamsGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:rcDot11SecurityParamsGroup.setStatus(_A)
rcDot11DhcpParamsGroup=ObjectGroup((1,3,6,1,4,1,15004,4,4,10,2,4))
rcDot11DhcpParamsGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:rcDot11DhcpParamsGroup.setStatus(_A)
rcDot11MacFilteringTableGroup=ObjectGroup((1,3,6,1,4,1,15004,4,4,10,2,5))
rcDot11MacFilteringTableGroup.setObjects(*((_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:rcDot11MacFilteringTableGroup.setStatus(_A)
rcDot11AssociationTableGroup=ObjectGroup((1,3,6,1,4,1,15004,4,4,10,2,6))
rcDot11AssociationTableGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:rcDot11AssociationTableGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcDot11':rcDot11,'rcDot11GlobalParams':rcDot11GlobalParams,_K:rcDot11OpMode,_L:rcDot11RFMAC,_M:rcDot11IpAddress,_N:rcDot11IpSubnet,_O:rcDot11DefaultGateway,_P:rcDot11Status,_Q:rcDot11UpTime,_R:rcDot11Version,_S:rcDot11TftpServerIpAddress,_T:rcDot11SwUpgrade,_U:rcDot11SwUpgradeStatus,_V:rcDot11WlanReset,'rcDot11NetworkParams':rcDot11NetworkParams,_W:rcDot11NetworkPhyMode,_X:rcDot11NetworkDesiredSsid,_Y:rcDot11NetworkPrimarySsid,_Z:rcDot11NetworkSecondary1Ssid,_a:rcDot11NetworkSecondary2Ssid,_b:rcDot11NetworkRfChannel,_c:rcDot11NetworkSsidTxSuppress,_e:rcDot11NetworkRfTxEnable,_f:rcDot11NetworkRate,_g:rcDot11NetworkTxPower,_h:rcDot11NetworkWdsEnable,_i:rcDot11NetworkWmmEnable,_j:rcDot11NetworkTxShortPreamble,_k:rcDot11NetworkDistance,_d:rcDot11NetworkAssociatedStations,'rcDot11SecurityParams':rcDot11SecurityParams,_l:rcDot11SecurityAuthMode,_m:rcDot11SecurityEncrypType,_n:rcDot11SecurityPassPhrase,_o:rcDot11SecurityWepKey,_p:rcDot11SecurityKeyRenewal,_q:rcDot11SecurityRadiusIpAddress,_r:rcDot11SecurityRadiusPort,_s:rcDot11SecurityRadiusSecret,'rcDot11MacFiltering':rcDot11MacFiltering,_A0:rcDot11MacFilteringControl,'rcDot11MacFilteringTable':rcDot11MacFilteringTable,'rcDot11MacFilteringEntry':rcDot11MacFilteringEntry,_H:rcDot11FilterMacAddress,_A1:rcDot11RowStatus,'rcDot11DhcpParams':rcDot11DhcpParams,_t:rcDot11DhcpServerEnable,_u:rcDot11DhcpStartOfPool,_v:rcDot11DhcpIpPoolSize,_w:rcDot11DhcpSubnet,_x:rcDot11DhcpGateway,_y:rcDot11DhcpDnsIpAddress,_z:rcDot11DhcpLeaseTime,'rcDot11AssociationInfo':rcDot11AssociationInfo,'rcDot11AssociationTable':rcDot11AssociationTable,'rcDot11AssociationEntry':rcDot11AssociationEntry,_J:rcDot11AssociationMac,_A2:rcDot11AssociationChannel,_A3:rcDot11AssociationRate,_A4:rcDot11AssociationRssi,_A5:rcDot11AssociationTxSeq,_A6:rcDot11AssociationRxSeq,_A7:rcDot11AssociationSecurity,'rcDot11Conformance':rcDot11Conformance,'rcDot11Groups':rcDot11Groups,'rcDot11GlobalParamsGroup':rcDot11GlobalParamsGroup,'rcDot11NetworkParamsGroup':rcDot11NetworkParamsGroup,'rcDot11SecurityParamsGroup':rcDot11SecurityParamsGroup,'rcDot11DhcpParamsGroup':rcDot11DhcpParamsGroup,'rcDot11MacFilteringTableGroup':rcDot11MacFilteringTableGroup,'rcDot11AssociationTableGroup':rcDot11AssociationTableGroup})