_BA='notificationsGroup'
_B9='pubStatsGroup'
_B8='versionsGroup'
_B7='snmpControlGroup'
_B6='smtpGroup'
_B5='alarmsGroup'
_B4='phyStatusGroup'
_B3='managementGroup'
_B2='licenceGroup'
_B1='ethernetGroup'
_B0='configurationGroup'
_A_='radarDetectTrap'
_Az='linkStatusTrap'
_Ay='noWirelessChannelAvailableTrap'
_Ax='installArmStateTrap'
_Aw='dataPortStatusTrap'
_Av='aggregateDataRate'
_Au='transmitDataRate'
_At='receiveDataRate'
_As='bootVersion'
_Ar='hardwareVersion'
_Aq='softwareVersion'
_Ap='nTPServerPortNumber'
_Ao='nTPServerIp'
_An='systemClock'
_Am='nTPLastSync'
_Al='nTPPollInterval'
_Ak='sNMPTrapVersion'
_Aj='sNMPTrapCommunity'
_Ai='sNMPCommunityOid'
_Ah='sNMPCommunityAccess'
_Ag='sNMPCommunityString'
_Af='sNMPTrapPortNumber'
_Ae='sNMPTrapIPAddress'
_Ad='sNMPEnabledTraps'
_Ac='sNMPTrapTableNumber'
_Ab='sNMPCommunityTableNumber'
_Aa='sMTPEnabledMessages'
_AZ='sMTPDestinationEmailAddress'
_AY='sMTPSourceEmailAddress'
_AX='sMTPServerPortNumber'
_AW='sMTPServerIPAddress'
_AV='measuredRange'
_AU='noiseFloor'
_AT='searchState'
_AS='signalStrengthRatio'
_AR='extendedFreqMHz'
_AQ='currentFreqMHz'
_AP='transmitModulationMode'
_AO='receiveModulationMode'
_AN='extendedChannel'
_AM='currentChannel'
_AL='transmitPower'
_AK='vectorError'
_AJ='receivePower'
_AI='tFTPSoftwareUpgradeStatusAdditionalText'
_AH='tFTPSoftwareUpgradeStatusText'
_AG='tFTPSoftwareUpgradeStatus'
_AF='tFTPSoftwareUpgradeFileName'
_AE='tFTPServerPortNumber'
_AD='tFTPServerIPAddress'
_AC='productName'
_AB='productVariant'
_AA='regionCode'
_A9='dataPortSpeedAndDuplex'
_A8='dataPortAutoNegAdvertisement'
_A7='dataPortAutoNegotiation'
_A6='dualPayload'
_A5='fixedModMode'
_A4='vlanPriority'
_A3='vlanTagging'
_A2='channelSelection'
_A1='configuredRange'
_A0='configuredModulationMode'
_z='siteName'
_y='linkName'
_x='remoteMACAddress'
_w='remoteIPAddress'
_v='channelBandwidth'
_u='cableLoss'
_t='antennaGain'
_s='maximumTransmitPower'
_r='masterSlaveMode'
_q='gatewayIPAddress'
_p='subnetMask'
_o='iPAddress'
_n='sNMPTrapTableIndex'
_m='not-accessible'
_l='sNMPCommunityTableIndex'
_k='noChannelAvailable'
_j='radarDetect'
_i='coldStart'
_h='wirelessLinkUpDown'
_g='dataPortUpDown'
_f='mod64QamFiveSixthsDual'
_e='mod64QamThreeQuartersDual'
_d='mod64QamTwoThirdsDual'
_c='mod16QamThreeQuartersDual'
_b='mod16QamHalfDual'
_a='modQpskThreeQuartersDual'
_Z='modQpskHalfDual'
_Y='modBpskHalfDual'
_X='mod64QamFiveSixthsSingle'
_W='mod64QamThreeQuartersSingle'
_V='mod64QamTwoThirdsSingle'
_U='mod16QamThreeQuartersSingle'
_T='mod16QamHalfSingle'
_S='modQpskThreeQuartersSingle'
_R='modQpskHalfSingle'
_Q='modBpskHalfSingle'
_P='acquisition'
_O='ptp250'
_N='OctetString'
_M='wirelessLinkStatus'
_L='radarDetectChannel'
_K='dataPortStatus'
_J='noWirelessChannelAvailable'
_I='installArmState'
_H='enabled'
_G='disabled'
_F='Bits'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='CAMBIUM-PTP250-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
cambium=ModuleIdentity((1,3,6,1,4,1,17713))
if mibBuilder.loadTexts:cambium.setRevisions(('2012-12-07 09:35','2011-10-18 10:47'))
_Ptp_ObjectIdentity=ObjectIdentity
ptp=_Ptp_ObjectIdentity((1,3,6,1,4,1,17713,1))
_Ptmp_ObjectIdentity=ObjectIdentity
ptmp=_Ptmp_ObjectIdentity((1,3,6,1,4,1,17713,2))
_Ptp250_ObjectIdentity=ObjectIdentity
ptp250=_Ptp250_ObjectIdentity((1,3,6,1,4,1,17713,250))
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,17713,250,1))
_IPAddress_Type=IpAddress
_IPAddress_Object=MibScalar
iPAddress=_IPAddress_Object((1,3,6,1,4,1,17713,250,1,1),_IPAddress_Type())
iPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:iPAddress.setStatus(_B)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,17713,250,1,2),_SubnetMask_Type())
subnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetMask.setStatus(_B)
_GatewayIPAddress_Type=IpAddress
_GatewayIPAddress_Object=MibScalar
gatewayIPAddress=_GatewayIPAddress_Object((1,3,6,1,4,1,17713,250,1,3),_GatewayIPAddress_Type())
gatewayIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:gatewayIPAddress.setStatus(_B)
class _RemoteMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RemoteMACAddress_Type.__name__=_N
_RemoteMACAddress_Object=MibScalar
remoteMACAddress=_RemoteMACAddress_Object((1,3,6,1,4,1,17713,250,1,4),_RemoteMACAddress_Type())
remoteMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMACAddress.setStatus(_B)
class _MasterSlaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('slave',0),('master',1)))
_MasterSlaveMode_Type.__name__=_D
_MasterSlaveMode_Object=MibScalar
masterSlaveMode=_MasterSlaveMode_Object((1,3,6,1,4,1,17713,250,1,5),_MasterSlaveMode_Type())
masterSlaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:masterSlaveMode.setStatus(_B)
class _MaximumTransmitPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,27))
_MaximumTransmitPower_Type.__name__=_D
_MaximumTransmitPower_Object=MibScalar
maximumTransmitPower=_MaximumTransmitPower_Object((1,3,6,1,4,1,17713,250,1,6),_MaximumTransmitPower_Type())
maximumTransmitPower.setMaxAccess(_C)
if mibBuilder.loadTexts:maximumTransmitPower.setStatus(_B)
class _AntennaGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,610))
_AntennaGain_Type.__name__=_D
_AntennaGain_Object=MibScalar
antennaGain=_AntennaGain_Object((1,3,6,1,4,1,17713,250,1,7),_AntennaGain_Type())
antennaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:antennaGain.setStatus(_B)
class _CableLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CableLoss_Type.__name__=_D
_CableLoss_Object=MibScalar
cableLoss=_CableLoss_Object((1,3,6,1,4,1,17713,250,1,8),_CableLoss_Type())
cableLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:cableLoss.setStatus(_B)
class _ChannelBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bw20MHz',0),('bw40MHz',1)))
_ChannelBandwidth_Type.__name__=_D
_ChannelBandwidth_Object=MibScalar
channelBandwidth=_ChannelBandwidth_Object((1,3,6,1,4,1,17713,250,1,9),_ChannelBandwidth_Type())
channelBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:channelBandwidth.setStatus(_B)
_RemoteIPAddress_Type=IpAddress
_RemoteIPAddress_Object=MibScalar
remoteIPAddress=_RemoteIPAddress_Object((1,3,6,1,4,1,17713,250,1,10),_RemoteIPAddress_Type())
remoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteIPAddress.setStatus(_B)
class _LinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_LinkName_Type.__name__=_E
_LinkName_Object=MibScalar
linkName=_LinkName_Object((1,3,6,1,4,1,17713,250,1,11),_LinkName_Type())
linkName.setMaxAccess(_C)
if mibBuilder.loadTexts:linkName.setStatus(_B)
class _SiteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SiteName_Type.__name__=_E
_SiteName_Object=MibScalar
siteName=_SiteName_Object((1,3,6,1,4,1,17713,250,1,12),_SiteName_Type())
siteName.setMaxAccess(_C)
if mibBuilder.loadTexts:siteName.setStatus(_B)
class _ConfiguredModulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('modBpskHalf',0),('modQpskHalf',1),('modQpskThreeQuarters',2),('mod16QamHalf',3),('mod16QamThreeQuarters',4),('mod64QamTwoThirds',5),('mod64QamThreeQuarters',6),('mod64QamFiveSixths',7)))
_ConfiguredModulationMode_Type.__name__=_D
_ConfiguredModulationMode_Object=MibScalar
configuredModulationMode=_ConfiguredModulationMode_Object((1,3,6,1,4,1,17713,250,1,13),_ConfiguredModulationMode_Type())
configuredModulationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:configuredModulationMode.setStatus(_B)
class _Band_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unset',0),('freq5400MHz',1),('freq5800MHz',2)))
_Band_Type.__name__=_D
_Band_Object=MibScalar
band=_Band_Object((1,3,6,1,4,1,17713,250,1,14),_Band_Type())
band.setMaxAccess(_C)
if mibBuilder.loadTexts:band.setStatus(_B)
class _ConfiguredRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5400))
_ConfiguredRange_Type.__name__=_D
_ConfiguredRange_Object=MibScalar
configuredRange=_ConfiguredRange_Object((1,3,6,1,4,1,17713,250,1,15),_ConfiguredRange_Type())
configuredRange.setMaxAccess(_C)
if mibBuilder.loadTexts:configuredRange.setStatus(_B)
class _ChannelSelection_Type(Bits):namedValues=NamedValues(*(('channum100',0),('channum104',1),('channum108',2),('channum112',3),('channum116',4),('channum120',5),('channum124',6),('channum128',7),('channum132',8),('channum136',9),('channum140',10),('channum149',11),('channum153',12),('channum157',13),('channum161',14),('channum165',15)))
_ChannelSelection_Type.__name__=_F
_ChannelSelection_Object=MibScalar
channelSelection=_ChannelSelection_Object((1,3,6,1,4,1,17713,250,1,16),_ChannelSelection_Type())
channelSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:channelSelection.setStatus(_B)
class _VlanTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_VlanTagging_Type.__name__=_D
_VlanTagging_Object=MibScalar
vlanTagging=_VlanTagging_Object((1,3,6,1,4,1,17713,250,1,17),_VlanTagging_Type())
vlanTagging.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanTagging.setStatus(_B)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanId_Type.__name__=_D
_VlanId_Object=MibScalar
vlanId=_VlanId_Object((1,3,6,1,4,1,17713,250,1,18),_VlanId_Type())
vlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanId.setStatus(_B)
class _VlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanPriority_Type.__name__=_D
_VlanPriority_Object=MibScalar
vlanPriority=_VlanPriority_Object((1,3,6,1,4,1,17713,250,1,19),_VlanPriority_Type())
vlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPriority.setStatus(_B)
class _FixedModMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_FixedModMode_Type.__name__=_D
_FixedModMode_Object=MibScalar
fixedModMode=_FixedModMode_Object((1,3,6,1,4,1,17713,250,1,22),_FixedModMode_Type())
fixedModMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fixedModMode.setStatus(_B)
class _DualPayload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DualPayload_Type.__name__=_D
_DualPayload_Object=MibScalar
dualPayload=_DualPayload_Object((1,3,6,1,4,1,17713,250,1,23),_DualPayload_Type())
dualPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:dualPayload.setStatus(_B)
_Ethernet_ObjectIdentity=ObjectIdentity
ethernet=_Ethernet_ObjectIdentity((1,3,6,1,4,1,17713,250,2))
class _DataPortAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DataPortAutoNegotiation_Type.__name__=_D
_DataPortAutoNegotiation_Object=MibScalar
dataPortAutoNegotiation=_DataPortAutoNegotiation_Object((1,3,6,1,4,1,17713,250,2,1),_DataPortAutoNegotiation_Type())
dataPortAutoNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:dataPortAutoNegotiation.setStatus(_B)
class _DataPortAutoNegAdvertisement_Type(Bits):namedValues=NamedValues(*(('negInvalid',0),('neg10MbpsHalfDuplex',1),('neg10MbpsFullDuplex',2),('neg100MbpsHalfDuplex',3),('neg100MbpsFullDuplex',4),('neg1000MbpsFullDuplex',5)))
_DataPortAutoNegAdvertisement_Type.__name__=_F
_DataPortAutoNegAdvertisement_Object=MibScalar
dataPortAutoNegAdvertisement=_DataPortAutoNegAdvertisement_Object((1,3,6,1,4,1,17713,250,2,2),_DataPortAutoNegAdvertisement_Type())
dataPortAutoNegAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:dataPortAutoNegAdvertisement.setStatus(_B)
class _DataPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_DataPortStatus_Type.__name__=_D
_DataPortStatus_Object=MibScalar
dataPortStatus=_DataPortStatus_Object((1,3,6,1,4,1,17713,250,2,3),_DataPortStatus_Type())
dataPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dataPortStatus.setStatus(_B)
class _DataPortSpeedAndDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('speed1000MbpsFullDuplex',0),('speed100MbpsFullDuplex',1),('speed100MbpsHalfDuplex',2),('speed10MbpsFullDuplex',3),('speed10MbpsHalfDuplex',4),('speedUnknown6',5)))
_DataPortSpeedAndDuplex_Type.__name__=_D
_DataPortSpeedAndDuplex_Object=MibScalar
dataPortSpeedAndDuplex=_DataPortSpeedAndDuplex_Object((1,3,6,1,4,1,17713,250,2,4),_DataPortSpeedAndDuplex_Type())
dataPortSpeedAndDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:dataPortSpeedAndDuplex.setStatus(_B)
_Licence_ObjectIdentity=ObjectIdentity
licence=_Licence_ObjectIdentity((1,3,6,1,4,1,17713,250,3))
class _RegionCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RegionCode_Type.__name__=_E
_RegionCode_Object=MibScalar
regionCode=_RegionCode_Object((1,3,6,1,4,1,17713,250,3,1),_RegionCode_Type())
regionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:regionCode.setStatus(_B)
class _ProductVariant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('ptpXX400Full',0),('ptpXX400Deprecated1',1),('ptpXX400Deprecated2',2),('ptpXX400Lite',3),('spare1',4),('ptpXX300',5),('spare2',6),('spare3',7),('ptpXX500FullDeprecated',8),('ptpXX500LiteDeprecated',9),('ptpXX500',10),('ptpXX600Lite',11),('ptpXX600Full',12),('spare5',13),('spare6',14),('ptp800',15),(_O,16)))
_ProductVariant_Type.__name__=_D
_ProductVariant_Object=MibScalar
productVariant=_ProductVariant_Object((1,3,6,1,4,1,17713,250,3,2),_ProductVariant_Type())
productVariant.setMaxAccess(_C)
if mibBuilder.loadTexts:productVariant.setStatus(_B)
class _ProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ProductName_Type.__name__=_E
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,17713,250,3,3),_ProductName_Type())
productName.setMaxAccess(_C)
if mibBuilder.loadTexts:productName.setStatus(_B)
_Management_ObjectIdentity=ObjectIdentity
management=_Management_ObjectIdentity((1,3,6,1,4,1,17713,250,4))
class _InstallArmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disarmed',0),('armed',1)))
_InstallArmState_Type.__name__=_D
_InstallArmState_Object=MibScalar
installArmState=_InstallArmState_Object((1,3,6,1,4,1,17713,250,4,1),_InstallArmState_Type())
installArmState.setMaxAccess(_C)
if mibBuilder.loadTexts:installArmState.setStatus(_B)
_TFTPServerIPAddress_Type=IpAddress
_TFTPServerIPAddress_Object=MibScalar
tFTPServerIPAddress=_TFTPServerIPAddress_Object((1,3,6,1,4,1,17713,250,4,2),_TFTPServerIPAddress_Type())
tFTPServerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tFTPServerIPAddress.setStatus(_B)
class _TFTPServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TFTPServerPortNumber_Type.__name__=_D
_TFTPServerPortNumber_Object=MibScalar
tFTPServerPortNumber=_TFTPServerPortNumber_Object((1,3,6,1,4,1,17713,250,4,3),_TFTPServerPortNumber_Type())
tFTPServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tFTPServerPortNumber.setStatus(_B)
class _TFTPSoftwareUpgradeFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TFTPSoftwareUpgradeFileName_Type.__name__=_E
_TFTPSoftwareUpgradeFileName_Object=MibScalar
tFTPSoftwareUpgradeFileName=_TFTPSoftwareUpgradeFileName_Object((1,3,6,1,4,1,17713,250,4,4),_TFTPSoftwareUpgradeFileName_Type())
tFTPSoftwareUpgradeFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tFTPSoftwareUpgradeFileName.setStatus(_B)
class _TFTPSoftwareUpgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('idle',0),('uploadinprogress',1),('uploadsuccessfulprogrammingFLASH',2),('upgradesuccessfulreboottorunthenewsoftwareimage',3),('upgradefailed',4)))
_TFTPSoftwareUpgradeStatus_Type.__name__=_D
_TFTPSoftwareUpgradeStatus_Object=MibScalar
tFTPSoftwareUpgradeStatus=_TFTPSoftwareUpgradeStatus_Object((1,3,6,1,4,1,17713,250,4,5),_TFTPSoftwareUpgradeStatus_Type())
tFTPSoftwareUpgradeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tFTPSoftwareUpgradeStatus.setStatus(_B)
class _TFTPSoftwareUpgradeStatusText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TFTPSoftwareUpgradeStatusText_Type.__name__=_E
_TFTPSoftwareUpgradeStatusText_Object=MibScalar
tFTPSoftwareUpgradeStatusText=_TFTPSoftwareUpgradeStatusText_Object((1,3,6,1,4,1,17713,250,4,6),_TFTPSoftwareUpgradeStatusText_Type())
tFTPSoftwareUpgradeStatusText.setMaxAccess(_C)
if mibBuilder.loadTexts:tFTPSoftwareUpgradeStatusText.setStatus(_B)
class _TFTPSoftwareUpgradeStatusAdditionalText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TFTPSoftwareUpgradeStatusAdditionalText_Type.__name__=_E
_TFTPSoftwareUpgradeStatusAdditionalText_Object=MibScalar
tFTPSoftwareUpgradeStatusAdditionalText=_TFTPSoftwareUpgradeStatusAdditionalText_Object((1,3,6,1,4,1,17713,250,4,7),_TFTPSoftwareUpgradeStatusAdditionalText_Type())
tFTPSoftwareUpgradeStatusAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:tFTPSoftwareUpgradeStatusAdditionalText.setStatus(_B)
_PhyStatus_ObjectIdentity=ObjectIdentity
phyStatus=_PhyStatus_ObjectIdentity((1,3,6,1,4,1,17713,250,5))
_ReceivePower_Type=Integer32
_ReceivePower_Object=MibScalar
receivePower=_ReceivePower_Object((1,3,6,1,4,1,17713,250,5,1),_ReceivePower_Type())
receivePower.setMaxAccess(_C)
if mibBuilder.loadTexts:receivePower.setStatus(_B)
_VectorError_Type=Integer32
_VectorError_Object=MibScalar
vectorError=_VectorError_Object((1,3,6,1,4,1,17713,250,5,2),_VectorError_Type())
vectorError.setMaxAccess(_C)
if mibBuilder.loadTexts:vectorError.setStatus(_B)
_TransmitPower_Type=Integer32
_TransmitPower_Object=MibScalar
transmitPower=_TransmitPower_Object((1,3,6,1,4,1,17713,250,5,3),_TransmitPower_Type())
transmitPower.setMaxAccess(_C)
if mibBuilder.loadTexts:transmitPower.setStatus(_B)
class _LinkLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_LinkLoss_Type.__name__=_D
_LinkLoss_Object=MibScalar
linkLoss=_LinkLoss_Object((1,3,6,1,4,1,17713,250,5,5),_LinkLoss_Type())
linkLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLoss.setStatus(_B)
class _CurrentChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CurrentChannel_Type.__name__=_D
_CurrentChannel_Object=MibScalar
currentChannel=_CurrentChannel_Object((1,3,6,1,4,1,17713,250,5,6),_CurrentChannel_Type())
currentChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:currentChannel.setStatus(_B)
class _ExtendedChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ExtendedChannel_Type.__name__=_D
_ExtendedChannel_Object=MibScalar
extendedChannel=_ExtendedChannel_Object((1,3,6,1,4,1,17713,250,5,7),_ExtendedChannel_Type())
extendedChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:extendedChannel.setStatus(_B)
class _ReceiveModulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9),(_Z,10),(_a,11),(_b,12),(_c,13),(_d,14),(_e,15),(_f,16)))
_ReceiveModulationMode_Type.__name__=_D
_ReceiveModulationMode_Object=MibScalar
receiveModulationMode=_ReceiveModulationMode_Object((1,3,6,1,4,1,17713,250,5,8),_ReceiveModulationMode_Type())
receiveModulationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:receiveModulationMode.setStatus(_B)
class _TransmitModulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9),(_Z,10),(_a,11),(_b,12),(_c,13),(_d,14),(_e,15),(_f,16)))
_TransmitModulationMode_Type.__name__=_D
_TransmitModulationMode_Object=MibScalar
transmitModulationMode=_TransmitModulationMode_Object((1,3,6,1,4,1,17713,250,5,9),_TransmitModulationMode_Type())
transmitModulationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:transmitModulationMode.setStatus(_B)
_CurrentFreqMHz_Type=Integer32
_CurrentFreqMHz_Object=MibScalar
currentFreqMHz=_CurrentFreqMHz_Object((1,3,6,1,4,1,17713,250,5,11),_CurrentFreqMHz_Type())
currentFreqMHz.setMaxAccess(_C)
if mibBuilder.loadTexts:currentFreqMHz.setStatus(_B)
_ExtendedFreqMHz_Type=Integer32
_ExtendedFreqMHz_Object=MibScalar
extendedFreqMHz=_ExtendedFreqMHz_Object((1,3,6,1,4,1,17713,250,5,12),_ExtendedFreqMHz_Type())
extendedFreqMHz.setMaxAccess(_C)
if mibBuilder.loadTexts:extendedFreqMHz.setStatus(_B)
_SignalStrengthRatio_Type=Integer32
_SignalStrengthRatio_Object=MibScalar
signalStrengthRatio=_SignalStrengthRatio_Object((1,3,6,1,4,1,17713,250,5,13),_SignalStrengthRatio_Type())
signalStrengthRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:signalStrengthRatio.setStatus(_B)
class _SearchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('up',0),('registering',1),('acquiring',2),('searching',3),('radarCAC',4),('initialising',5),('noChannels',6)))
_SearchState_Type.__name__=_D
_SearchState_Object=MibScalar
searchState=_SearchState_Object((1,3,6,1,4,1,17713,250,5,14),_SearchState_Type())
searchState.setMaxAccess(_C)
if mibBuilder.loadTexts:searchState.setStatus(_B)
_NoiseFloor_Type=Integer32
_NoiseFloor_Object=MibScalar
noiseFloor=_NoiseFloor_Object((1,3,6,1,4,1,17713,250,5,15),_NoiseFloor_Type())
noiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:noiseFloor.setStatus(_B)
class _RadarDetectChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RadarDetectChannel_Type.__name__=_D
_RadarDetectChannel_Object=MibScalar
radarDetectChannel=_RadarDetectChannel_Object((1,3,6,1,4,1,17713,250,5,16),_RadarDetectChannel_Type())
radarDetectChannel.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:radarDetectChannel.setStatus(_B)
_MeasuredRange_Type=Integer32
_MeasuredRange_Object=MibScalar
measuredRange=_MeasuredRange_Object((1,3,6,1,4,1,17713,250,5,17),_MeasuredRange_Type())
measuredRange.setMaxAccess(_C)
if mibBuilder.loadTexts:measuredRange.setStatus(_B)
_Alarms_ObjectIdentity=ObjectIdentity
alarms=_Alarms_ObjectIdentity((1,3,6,1,4,1,17713,250,6))
class _NoWirelessChannelAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),(_J,1)))
_NoWirelessChannelAvailable_Type.__name__=_D
_NoWirelessChannelAvailable_Object=MibScalar
noWirelessChannelAvailable=_NoWirelessChannelAvailable_Object((1,3,6,1,4,1,17713,250,6,1),_NoWirelessChannelAvailable_Type())
noWirelessChannelAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:noWirelessChannelAvailable.setStatus(_B)
_Smtp_ObjectIdentity=ObjectIdentity
smtp=_Smtp_ObjectIdentity((1,3,6,1,4,1,17713,250,7))
_SMTPServerIPAddress_Type=IpAddress
_SMTPServerIPAddress_Object=MibScalar
sMTPServerIPAddress=_SMTPServerIPAddress_Object((1,3,6,1,4,1,17713,250,7,1),_SMTPServerIPAddress_Type())
sMTPServerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sMTPServerIPAddress.setStatus(_B)
class _SMTPServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SMTPServerPortNumber_Type.__name__=_D
_SMTPServerPortNumber_Object=MibScalar
sMTPServerPortNumber=_SMTPServerPortNumber_Object((1,3,6,1,4,1,17713,250,7,2),_SMTPServerPortNumber_Type())
sMTPServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sMTPServerPortNumber.setStatus(_B)
class _SMTPSourceEmailAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SMTPSourceEmailAddress_Type.__name__=_E
_SMTPSourceEmailAddress_Object=MibScalar
sMTPSourceEmailAddress=_SMTPSourceEmailAddress_Object((1,3,6,1,4,1,17713,250,7,3),_SMTPSourceEmailAddress_Type())
sMTPSourceEmailAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sMTPSourceEmailAddress.setStatus(_B)
class _SMTPDestinationEmailAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SMTPDestinationEmailAddress_Type.__name__=_E
_SMTPDestinationEmailAddress_Object=MibScalar
sMTPDestinationEmailAddress=_SMTPDestinationEmailAddress_Object((1,3,6,1,4,1,17713,250,7,4),_SMTPDestinationEmailAddress_Type())
sMTPDestinationEmailAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sMTPDestinationEmailAddress.setStatus(_B)
class _SMTPEnabledMessages_Type(Bits):namedValues=NamedValues(*((_g,0),(_h,1),(_i,2),(_j,3),(_I,4),(_k,5)))
_SMTPEnabledMessages_Type.__name__=_F
_SMTPEnabledMessages_Object=MibScalar
sMTPEnabledMessages=_SMTPEnabledMessages_Object((1,3,6,1,4,1,17713,250,7,5),_SMTPEnabledMessages_Type())
sMTPEnabledMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:sMTPEnabledMessages.setStatus(_B)
_SnmpControl_ObjectIdentity=ObjectIdentity
snmpControl=_SnmpControl_ObjectIdentity((1,3,6,1,4,1,17713,250,8))
class _SNMPCommunityTableNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2))
_SNMPCommunityTableNumber_Type.__name__=_D
_SNMPCommunityTableNumber_Object=MibScalar
sNMPCommunityTableNumber=_SNMPCommunityTableNumber_Object((1,3,6,1,4,1,17713,250,8,1),_SNMPCommunityTableNumber_Type())
sNMPCommunityTableNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPCommunityTableNumber.setStatus(_B)
_SNMPCommunityTable_Object=MibTable
sNMPCommunityTable=_SNMPCommunityTable_Object((1,3,6,1,4,1,17713,250,8,2))
if mibBuilder.loadTexts:sNMPCommunityTable.setStatus(_B)
_SNMPCommunityTableEntry_Object=MibTableRow
sNMPCommunityTableEntry=_SNMPCommunityTableEntry_Object((1,3,6,1,4,1,17713,250,8,2,1))
sNMPCommunityTableEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:sNMPCommunityTableEntry.setStatus(_B)
class _SNMPCommunityTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SNMPCommunityTableIndex_Type.__name__=_D
_SNMPCommunityTableIndex_Object=MibTableColumn
sNMPCommunityTableIndex=_SNMPCommunityTableIndex_Object((1,3,6,1,4,1,17713,250,8,2,1,1),_SNMPCommunityTableIndex_Type())
sNMPCommunityTableIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:sNMPCommunityTableIndex.setStatus(_B)
_SNMPCommunityString_Type=OctetString
_SNMPCommunityString_Object=MibTableColumn
sNMPCommunityString=_SNMPCommunityString_Object((1,3,6,1,4,1,17713,250,8,2,1,2),_SNMPCommunityString_Type())
sNMPCommunityString.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPCommunityString.setStatus(_B)
class _SNMPCommunityAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('readOnly',0),('readWrite',1)))
_SNMPCommunityAccess_Type.__name__=_D
_SNMPCommunityAccess_Object=MibTableColumn
sNMPCommunityAccess=_SNMPCommunityAccess_Object((1,3,6,1,4,1,17713,250,8,2,1,3),_SNMPCommunityAccess_Type())
sNMPCommunityAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPCommunityAccess.setStatus(_B)
_SNMPCommunityOid_Type=ObjectIdentifier
_SNMPCommunityOid_Object=MibTableColumn
sNMPCommunityOid=_SNMPCommunityOid_Object((1,3,6,1,4,1,17713,250,8,2,1,4),_SNMPCommunityOid_Type())
sNMPCommunityOid.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPCommunityOid.setStatus(_B)
class _SNMPTrapTableNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2))
_SNMPTrapTableNumber_Type.__name__=_D
_SNMPTrapTableNumber_Object=MibScalar
sNMPTrapTableNumber=_SNMPTrapTableNumber_Object((1,3,6,1,4,1,17713,250,8,3),_SNMPTrapTableNumber_Type())
sNMPTrapTableNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPTrapTableNumber.setStatus(_B)
_SNMPTrapTable_Object=MibTable
sNMPTrapTable=_SNMPTrapTable_Object((1,3,6,1,4,1,17713,250,8,4))
if mibBuilder.loadTexts:sNMPTrapTable.setStatus(_B)
_SNMPTrapTableEntry_Object=MibTableRow
sNMPTrapTableEntry=_SNMPTrapTableEntry_Object((1,3,6,1,4,1,17713,250,8,4,1))
sNMPTrapTableEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:sNMPTrapTableEntry.setStatus(_B)
class _SNMPTrapTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SNMPTrapTableIndex_Type.__name__=_D
_SNMPTrapTableIndex_Object=MibTableColumn
sNMPTrapTableIndex=_SNMPTrapTableIndex_Object((1,3,6,1,4,1,17713,250,8,4,1,1),_SNMPTrapTableIndex_Type())
sNMPTrapTableIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:sNMPTrapTableIndex.setStatus(_B)
_SNMPTrapIPAddress_Type=IpAddress
_SNMPTrapIPAddress_Object=MibTableColumn
sNMPTrapIPAddress=_SNMPTrapIPAddress_Object((1,3,6,1,4,1,17713,250,8,4,1,2),_SNMPTrapIPAddress_Type())
sNMPTrapIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPTrapIPAddress.setStatus(_B)
class _SNMPTrapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SNMPTrapPortNumber_Type.__name__=_D
_SNMPTrapPortNumber_Object=MibTableColumn
sNMPTrapPortNumber=_SNMPTrapPortNumber_Object((1,3,6,1,4,1,17713,250,8,4,1,3),_SNMPTrapPortNumber_Type())
sNMPTrapPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPTrapPortNumber.setStatus(_B)
_SNMPTrapCommunity_Type=OctetString
_SNMPTrapCommunity_Object=MibTableColumn
sNMPTrapCommunity=_SNMPTrapCommunity_Object((1,3,6,1,4,1,17713,250,8,4,1,4),_SNMPTrapCommunity_Type())
sNMPTrapCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPTrapCommunity.setStatus(_B)
class _SNMPTrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v1',0),('v2c',1)))
_SNMPTrapVersion_Type.__name__=_D
_SNMPTrapVersion_Object=MibTableColumn
sNMPTrapVersion=_SNMPTrapVersion_Object((1,3,6,1,4,1,17713,250,8,4,1,5),_SNMPTrapVersion_Type())
sNMPTrapVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPTrapVersion.setStatus(_B)
class _SNMPEnabledTraps_Type(Bits):namedValues=NamedValues(*((_g,0),(_h,1),(_i,2),(_j,3),(_I,4),(_k,5)))
_SNMPEnabledTraps_Type.__name__=_F
_SNMPEnabledTraps_Object=MibScalar
sNMPEnabledTraps=_SNMPEnabledTraps_Object((1,3,6,1,4,1,17713,250,8,6),_SNMPEnabledTraps_Type())
sNMPEnabledTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:sNMPEnabledTraps.setStatus(_B)
_Ntp_ObjectIdentity=ObjectIdentity
ntp=_Ntp_ObjectIdentity((1,3,6,1,4,1,17713,250,9))
class _NTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NTPState_Type.__name__=_D
_NTPState_Object=MibScalar
nTPState=_NTPState_Object((1,3,6,1,4,1,17713,250,9,1),_NTPState_Type())
nTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:nTPState.setStatus(_B)
class _NTPPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,43200))
_NTPPollInterval_Type.__name__=_D
_NTPPollInterval_Object=MibScalar
nTPPollInterval=_NTPPollInterval_Object((1,3,6,1,4,1,17713,250,9,2),_NTPPollInterval_Type())
nTPPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:nTPPollInterval.setStatus(_B)
class _NTPSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noSync',0),('inSync',1)))
_NTPSync_Type.__name__=_D
_NTPSync_Object=MibScalar
nTPSync=_NTPSync_Object((1,3,6,1,4,1,17713,250,9,3),_NTPSync_Type())
nTPSync.setMaxAccess(_C)
if mibBuilder.loadTexts:nTPSync.setStatus(_B)
_NTPLastSync_Type=Integer32
_NTPLastSync_Object=MibScalar
nTPLastSync=_NTPLastSync_Object((1,3,6,1,4,1,17713,250,9,4),_NTPLastSync_Type())
nTPLastSync.setMaxAccess(_C)
if mibBuilder.loadTexts:nTPLastSync.setStatus(_B)
_SystemClock_Type=Integer32
_SystemClock_Object=MibScalar
systemClock=_SystemClock_Object((1,3,6,1,4,1,17713,250,9,5),_SystemClock_Type())
systemClock.setMaxAccess(_C)
if mibBuilder.loadTexts:systemClock.setStatus(_B)
class _TimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)));namedValues=NamedValues(*(('gmtMinus1200',0),('gmtMinus1130',1),('gmtMinus1100',2),('gmtMinus1030',3),('gmtMinus1000',4),('gmtMinus0930',5),('gmtMinus0900',6),('gmtMinus0830',7),('gmtMinus0800',8),('gmtMinus0730',9),('gmtMinus0700',10),('gmtMinus0630',11),('gmtMinus0600',12),('gmtMinus0530',13),('gmtMinus0500',14),('gmtMinus0430',15),('gmtMinus0400',16),('gmtMinus0330',17),('gmtMinus0300',18),('gmtMinus0230',19),('gmtMinus0200',20),('gmtMinus0130',21),('gmtMinus0100',22),('gmtMinus0030',23),('gmtZero',24),('gmtPlus0030',25),('gmtPlus0100',26),('gmtPlus0130',27),('gmtPlus0200',28),('gmtPlus0230',29),('gmtPlus0300',30),('gmtPlus0330',31),('gmtPlus0400',32),('gmtPlus0430',33),('gmtPlus0500',34),('gmtPlus0530',35),('gmtPlus0600',36),('gmtPlus0630',37),('gmtPlus0700',38),('gmtPlus0730',39),('gmtPlus0800',40),('gmtPlus0830',41),('gmtPlus0900',42),('gmtPlus0930',43),('gmtPlus1000',44),('gmtPlus1030',45),('gmtPlus1100',46),('gmtPlus1130',47),('gmtPlus1200',48),('gmtPlus1230',49),('gmtPlus1300',50)))
_TimeZone_Type.__name__=_D
_TimeZone_Object=MibScalar
timeZone=_TimeZone_Object((1,3,6,1,4,1,17713,250,9,6),_TimeZone_Type())
timeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:timeZone.setStatus(_B)
_NTPServerIp_Type=IpAddress
_NTPServerIp_Object=MibScalar
nTPServerIp=_NTPServerIp_Object((1,3,6,1,4,1,17713,250,9,7),_NTPServerIp_Type())
nTPServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:nTPServerIp.setStatus(_B)
class _NTPServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NTPServerPortNumber_Type.__name__=_D
_NTPServerPortNumber_Object=MibScalar
nTPServerPortNumber=_NTPServerPortNumber_Object((1,3,6,1,4,1,17713,250,9,8),_NTPServerPortNumber_Type())
nTPServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nTPServerPortNumber.setStatus(_B)
_Versions_ObjectIdentity=ObjectIdentity
versions=_Versions_ObjectIdentity((1,3,6,1,4,1,17713,250,10))
class _SoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SoftwareVersion_Type.__name__=_E
_SoftwareVersion_Object=MibScalar
softwareVersion=_SoftwareVersion_Object((1,3,6,1,4,1,17713,250,10,1),_SoftwareVersion_Type())
softwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersion.setStatus(_B)
class _HardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HardwareVersion_Type.__name__=_E
_HardwareVersion_Object=MibScalar
hardwareVersion=_HardwareVersion_Object((1,3,6,1,4,1,17713,250,10,2),_HardwareVersion_Type())
hardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareVersion.setStatus(_B)
class _BootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_BootVersion_Type.__name__=_E
_BootVersion_Object=MibScalar
bootVersion=_BootVersion_Object((1,3,6,1,4,1,17713,250,10,3),_BootVersion_Type())
bootVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:bootVersion.setStatus(_B)
_PubStats_ObjectIdentity=ObjectIdentity
pubStats=_PubStats_ObjectIdentity((1,3,6,1,4,1,17713,250,11))
_ReceiveDataRate_Type=Integer32
_ReceiveDataRate_Object=MibScalar
receiveDataRate=_ReceiveDataRate_Object((1,3,6,1,4,1,17713,250,11,1),_ReceiveDataRate_Type())
receiveDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:receiveDataRate.setStatus(_B)
_TransmitDataRate_Type=Integer32
_TransmitDataRate_Object=MibScalar
transmitDataRate=_TransmitDataRate_Object((1,3,6,1,4,1,17713,250,11,2),_TransmitDataRate_Type())
transmitDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:transmitDataRate.setStatus(_B)
_AggregateDataRate_Type=Integer32
_AggregateDataRate_Object=MibScalar
aggregateDataRate=_AggregateDataRate_Object((1,3,6,1,4,1,17713,250,11,3),_AggregateDataRate_Type())
aggregateDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aggregateDataRate.setStatus(_B)
class _WirelessLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_WirelessLinkStatus_Type.__name__=_D
_WirelessLinkStatus_Object=MibScalar
wirelessLinkStatus=_WirelessLinkStatus_Object((1,3,6,1,4,1,17713,250,11,4),_WirelessLinkStatus_Type())
wirelessLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wirelessLinkStatus.setStatus(_B)
_PtpGroups_ObjectIdentity=ObjectIdentity
ptpGroups=_PtpGroups_ObjectIdentity((1,3,6,1,4,1,17713,250,98))
_PtpTraps_ObjectIdentity=ObjectIdentity
ptpTraps=_PtpTraps_ObjectIdentity((1,3,6,1,4,1,17713,250,99))
_PtpTrapPrefix_ObjectIdentity=ObjectIdentity
ptpTrapPrefix=_PtpTrapPrefix_ObjectIdentity((1,3,6,1,4,1,17713,250,99,0))
configurationGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,5))
configurationGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,'band'),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,'vlanId'),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:configurationGroup.setStatus(_B)
ethernetGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,6))
ethernetGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_K),(_A,_A9)))
if mibBuilder.loadTexts:ethernetGroup.setStatus(_B)
licenceGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,8))
licenceGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:licenceGroup.setStatus(_B)
managementGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,9))
managementGroup.setObjects(*((_A,_I),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:managementGroup.setStatus(_B)
phyStatusGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,12))
phyStatusGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,'linkLoss'),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_L),(_A,_AV)))
if mibBuilder.loadTexts:phyStatusGroup.setStatus(_B)
alarmsGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,13))
alarmsGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:alarmsGroup.setStatus(_B)
smtpGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,15))
smtpGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:smtpGroup.setStatus(_B)
snmpControlGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,16))
snmpControlGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:snmpControlGroup.setStatus(_B)
ntpGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,17))
ntpGroup.setObjects(*((_A,'nTPState'),(_A,_Al),(_A,'nTPSync'),(_A,_Am),(_A,_An),(_A,'timeZone'),(_A,_Ao),(_A,_Ap)))
if mibBuilder.loadTexts:ntpGroup.setStatus(_B)
versionsGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,19))
versionsGroup.setObjects(*((_A,_Aq),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:versionsGroup.setStatus(_B)
pubStatsGroup=ObjectGroup((1,3,6,1,4,1,17713,250,98,20))
pubStatsGroup.setObjects(*((_A,_At),(_A,_Au),(_A,_Av),(_A,_M)))
if mibBuilder.loadTexts:pubStatsGroup.setStatus(_B)
dataPortStatusTrap=NotificationType((1,3,6,1,4,1,17713,250,99,0,1))
dataPortStatusTrap.setObjects((_A,_K))
if mibBuilder.loadTexts:dataPortStatusTrap.setStatus(_B)
installArmStateTrap=NotificationType((1,3,6,1,4,1,17713,250,99,0,2))
installArmStateTrap.setObjects((_A,_I))
if mibBuilder.loadTexts:installArmStateTrap.setStatus(_B)
noWirelessChannelAvailableTrap=NotificationType((1,3,6,1,4,1,17713,250,99,0,3))
noWirelessChannelAvailableTrap.setObjects((_A,_J))
if mibBuilder.loadTexts:noWirelessChannelAvailableTrap.setStatus(_B)
linkStatusTrap=NotificationType((1,3,6,1,4,1,17713,250,99,0,4))
linkStatusTrap.setObjects((_A,_M))
if mibBuilder.loadTexts:linkStatusTrap.setStatus(_B)
radarDetectTrap=NotificationType((1,3,6,1,4,1,17713,250,99,0,5))
radarDetectTrap.setObjects((_A,_L))
if mibBuilder.loadTexts:radarDetectTrap.setStatus(_B)
notificationsGroup=NotificationGroup((1,3,6,1,4,1,17713,250,98,99))
notificationsGroup.setObjects(*((_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:notificationsGroup.setStatus(_B)
ptpCompliance=ModuleCompliance((1,3,6,1,4,1,17713,250,97))
ptpCompliance.setObjects(*((_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,'ntpGroup'),(_A,_B8),(_A,_B9),(_A,_BA)))
if mibBuilder.loadTexts:ptpCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cambium':cambium,'ptp':ptp,'ptmp':ptmp,_O:ptp250,'configuration':configuration,_o:iPAddress,_p:subnetMask,_q:gatewayIPAddress,_x:remoteMACAddress,_r:masterSlaveMode,_s:maximumTransmitPower,_t:antennaGain,_u:cableLoss,_v:channelBandwidth,_w:remoteIPAddress,_y:linkName,_z:siteName,_A0:configuredModulationMode,'band':band,_A1:configuredRange,_A2:channelSelection,_A3:vlanTagging,'vlanId':vlanId,_A4:vlanPriority,_A5:fixedModMode,_A6:dualPayload,'ethernet':ethernet,_A7:dataPortAutoNegotiation,_A8:dataPortAutoNegAdvertisement,_K:dataPortStatus,_A9:dataPortSpeedAndDuplex,'licence':licence,_AA:regionCode,_AB:productVariant,_AC:productName,'management':management,_I:installArmState,_AD:tFTPServerIPAddress,_AE:tFTPServerPortNumber,_AF:tFTPSoftwareUpgradeFileName,_AG:tFTPSoftwareUpgradeStatus,_AH:tFTPSoftwareUpgradeStatusText,_AI:tFTPSoftwareUpgradeStatusAdditionalText,'phyStatus':phyStatus,_AJ:receivePower,_AK:vectorError,_AL:transmitPower,'linkLoss':linkLoss,_AM:currentChannel,_AN:extendedChannel,_AO:receiveModulationMode,_AP:transmitModulationMode,_AQ:currentFreqMHz,_AR:extendedFreqMHz,_AS:signalStrengthRatio,_AT:searchState,_AU:noiseFloor,_L:radarDetectChannel,_AV:measuredRange,'alarms':alarms,_J:noWirelessChannelAvailable,'smtp':smtp,_AW:sMTPServerIPAddress,_AX:sMTPServerPortNumber,_AY:sMTPSourceEmailAddress,_AZ:sMTPDestinationEmailAddress,_Aa:sMTPEnabledMessages,'snmpControl':snmpControl,_Ab:sNMPCommunityTableNumber,'sNMPCommunityTable':sNMPCommunityTable,'sNMPCommunityTableEntry':sNMPCommunityTableEntry,_l:sNMPCommunityTableIndex,_Ag:sNMPCommunityString,_Ah:sNMPCommunityAccess,_Ai:sNMPCommunityOid,_Ac:sNMPTrapTableNumber,'sNMPTrapTable':sNMPTrapTable,'sNMPTrapTableEntry':sNMPTrapTableEntry,_n:sNMPTrapTableIndex,_Ae:sNMPTrapIPAddress,_Af:sNMPTrapPortNumber,_Aj:sNMPTrapCommunity,_Ak:sNMPTrapVersion,_Ad:sNMPEnabledTraps,'ntp':ntp,'nTPState':nTPState,_Al:nTPPollInterval,'nTPSync':nTPSync,_Am:nTPLastSync,_An:systemClock,'timeZone':timeZone,_Ao:nTPServerIp,_Ap:nTPServerPortNumber,'versions':versions,_Aq:softwareVersion,_Ar:hardwareVersion,_As:bootVersion,'pubStats':pubStats,_At:receiveDataRate,_Au:transmitDataRate,_Av:aggregateDataRate,_M:wirelessLinkStatus,'ptpCompliance':ptpCompliance,'ptpGroups':ptpGroups,_B0:configurationGroup,_B1:ethernetGroup,_B2:licenceGroup,_B3:managementGroup,_B4:phyStatusGroup,_B5:alarmsGroup,_B6:smtpGroup,_B7:snmpControlGroup,'ntpGroup':ntpGroup,_B8:versionsGroup,_B9:pubStatsGroup,_BA:notificationsGroup,'ptpTraps':ptpTraps,'ptpTrapPrefix':ptpTrapPrefix,_Aw:dataPortStatusTrap,_Ax:installArmStateTrap,_Ay:noWirelessChannelAvailableTrap,_Az:linkStatusTrap,_A_:radarDetectTrap})