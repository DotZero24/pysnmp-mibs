_T='ifIndex'
_S='entSNMPCommunityIndex'
_R='entCLInfoIndex'
_Q='entWlan802dot1xESSIDIndex'
_P='entWlanWPAESSIDIndex'
_O='entWlanESSIDIndex'
_N='entWlanESSIDInfoIndex'
_M='entMacAddressIndex'
_L='wds-bridge'
_K='client-bridge'
_J='repeater'
_I='OctetString'
_H='DisplayString'
_G='write-only'
_F='SENAO-ENTERPRISE-INDOOR-AP-CB-MIB'
_E='read-only'
_D='Integer32'
_C='mandatory'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','TextualConvention','TruthValue')
senao=ModuleIdentity((1,3,6,1,4,1,14125))
_IndoorWirelessDevice_ObjectIdentity=ObjectIdentity
indoorWirelessDevice=_IndoorWirelessDevice_ObjectIdentity((1,3,6,1,4,1,14125,100))
_EntSystem_ObjectIdentity=ObjectIdentity
entSystem=_EntSystem_ObjectIdentity((1,3,6,1,4,1,14125,100,1))
class _EntPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EntPassword_Type.__name__=_H
_EntPassword_Object=MibScalar
entPassword=_EntPassword_Object((1,3,6,1,4,1,14125,100,1,2),_EntPassword_Type())
entPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:entPassword.setStatus(_C)
_EntSysModel_Type=DisplayString
_EntSysModel_Object=MibScalar
entSysModel=_EntSysModel_Object((1,3,6,1,4,1,14125,100,1,3),_EntSysModel_Type())
entSysModel.setMaxAccess(_E)
if mibBuilder.loadTexts:entSysModel.setStatus(_C)
class _EntSysMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ap-router',0),(_J,1),('ap-bridge',2),(_K,3),('client-router',4),(_L,5)))
_EntSysMode_Type.__name__=_D
_EntSysMode_Object=MibScalar
entSysMode=_EntSysMode_Object((1,3,6,1,4,1,14125,100,1,4),_EntSysMode_Type())
entSysMode.setMaxAccess(_E)
if mibBuilder.loadTexts:entSysMode.setStatus(_C)
_EntSysUpTime_Type=TimeTicks
_EntSysUpTime_Object=MibScalar
entSysUpTime=_EntSysUpTime_Object((1,3,6,1,4,1,14125,100,1,5),_EntSysUpTime_Type())
entSysUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:entSysUpTime.setStatus(_C)
_EntHwVersion_Type=DisplayString
_EntHwVersion_Object=MibScalar
entHwVersion=_EntHwVersion_Object((1,3,6,1,4,1,14125,100,1,6),_EntHwVersion_Type())
entHwVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:entHwVersion.setStatus(_C)
_EntSN_Type=DisplayString
_EntSN_Object=MibScalar
entSN=_EntSN_Object((1,3,6,1,4,1,14125,100,1,7),_EntSN_Type())
entSN.setMaxAccess(_E)
if mibBuilder.loadTexts:entSN.setStatus(_C)
_EntKenelVersion_Type=DisplayString
_EntKenelVersion_Object=MibScalar
entKenelVersion=_EntKenelVersion_Object((1,3,6,1,4,1,14125,100,1,8),_EntKenelVersion_Type())
entKenelVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:entKenelVersion.setStatus(_C)
_EntAppVersion_Type=DisplayString
_EntAppVersion_Object=MibScalar
entAppVersion=_EntAppVersion_Object((1,3,6,1,4,1,14125,100,1,9),_EntAppVersion_Type())
entAppVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:entAppVersion.setStatus(_C)
_EntReset_Type=TruthValue
_EntReset_Object=MibScalar
entReset=_EntReset_Object((1,3,6,1,4,1,14125,100,1,10),_EntReset_Type())
entReset.setMaxAccess(_G)
if mibBuilder.loadTexts:entReset.setStatus(_C)
_EntResetToDefault_Type=TruthValue
_EntResetToDefault_Object=MibScalar
entResetToDefault=_EntResetToDefault_Object((1,3,6,1,4,1,14125,100,1,11),_EntResetToDefault_Type())
entResetToDefault.setMaxAccess(_G)
if mibBuilder.loadTexts:entResetToDefault.setStatus(_C)
_EntApplyModules_Type=TruthValue
_EntApplyModules_Object=MibScalar
entApplyModules=_EntApplyModules_Object((1,3,6,1,4,1,14125,100,1,12),_EntApplyModules_Type())
entApplyModules.setMaxAccess(_G)
if mibBuilder.loadTexts:entApplyModules.setStatus(_C)
_EntLAN_ObjectIdentity=ObjectIdentity
entLAN=_EntLAN_ObjectIdentity((1,3,6,1,4,1,14125,100,2))
_EntLANIP_Type=IpAddress
_EntLANIP_Object=MibScalar
entLANIP=_EntLANIP_Object((1,3,6,1,4,1,14125,100,2,1),_EntLANIP_Type())
entLANIP.setMaxAccess(_A)
if mibBuilder.loadTexts:entLANIP.setStatus(_C)
_EntLANSubnetMask_Type=IpAddress
_EntLANSubnetMask_Object=MibScalar
entLANSubnetMask=_EntLANSubnetMask_Object((1,3,6,1,4,1,14125,100,2,2),_EntLANSubnetMask_Type())
entLANSubnetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:entLANSubnetMask.setStatus(_C)
_EntSTPEnable_Type=TruthValue
_EntSTPEnable_Object=MibScalar
entSTPEnable=_EntSTPEnable_Object((1,3,6,1,4,1,14125,100,2,3),_EntSTPEnable_Type())
entSTPEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:entSTPEnable.setStatus(_C)
_EntDHCPEnable_Type=TruthValue
_EntDHCPEnable_Object=MibScalar
entDHCPEnable=_EntDHCPEnable_Object((1,3,6,1,4,1,14125,100,2,4),_EntDHCPEnable_Type())
entDHCPEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:entDHCPEnable.setStatus(_C)
_EntIPPoolStart_Type=IpAddress
_EntIPPoolStart_Object=MibScalar
entIPPoolStart=_EntIPPoolStart_Object((1,3,6,1,4,1,14125,100,2,5),_EntIPPoolStart_Type())
entIPPoolStart.setMaxAccess(_A)
if mibBuilder.loadTexts:entIPPoolStart.setStatus(_C)
_EntIPPoolEnd_Type=IpAddress
_EntIPPoolEnd_Object=MibScalar
entIPPoolEnd=_EntIPPoolEnd_Object((1,3,6,1,4,1,14125,100,2,6),_EntIPPoolEnd_Type())
entIPPoolEnd.setMaxAccess(_A)
if mibBuilder.loadTexts:entIPPoolEnd.setStatus(_C)
class _EntIPLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('half-hour',0),('one-hour',1),('two-hours',2),('half-day',3),('one-day',4),('two-days',5),('one-week',6),('two-weeks',7),('forever',8)))
_EntIPLeaseTime_Type.__name__=_D
_EntIPLeaseTime_Object=MibScalar
entIPLeaseTime=_EntIPLeaseTime_Object((1,3,6,1,4,1,14125,100,2,7),_EntIPLeaseTime_Type())
entIPLeaseTime.setMaxAccess(_A)
if mibBuilder.loadTexts:entIPLeaseTime.setStatus(_C)
_EntWAN_ObjectIdentity=ObjectIdentity
entWAN=_EntWAN_ObjectIdentity((1,3,6,1,4,1,14125,100,3))
_EntRouterEnable_Type=TruthValue
_EntRouterEnable_Object=MibScalar
entRouterEnable=_EntRouterEnable_Object((1,3,6,1,4,1,14125,100,3,1),_EntRouterEnable_Type())
entRouterEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:entRouterEnable.setStatus(_C)
_EntMacFilter_ObjectIdentity=ObjectIdentity
entMacFilter=_EntMacFilter_ObjectIdentity((1,3,6,1,4,1,14125,100,4))
_EntLanMacFilteringEnable_Type=TruthValue
_EntLanMacFilteringEnable_Object=MibScalar
entLanMacFilteringEnable=_EntLanMacFilteringEnable_Object((1,3,6,1,4,1,14125,100,4,1),_EntLanMacFilteringEnable_Type())
entLanMacFilteringEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:entLanMacFilteringEnable.setStatus(_C)
class _EntLanMacFilteringMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('white-list',0),('black-list',1)))
_EntLanMacFilteringMode_Type.__name__=_D
_EntLanMacFilteringMode_Object=MibScalar
entLanMacFilteringMode=_EntLanMacFilteringMode_Object((1,3,6,1,4,1,14125,100,4,2),_EntLanMacFilteringMode_Type())
entLanMacFilteringMode.setMaxAccess(_A)
if mibBuilder.loadTexts:entLanMacFilteringMode.setStatus(_C)
_EntLanMacFilterTable_Object=MibTable
entLanMacFilterTable=_EntLanMacFilterTable_Object((1,3,6,1,4,1,14125,100,4,3))
if mibBuilder.loadTexts:entLanMacFilterTable.setStatus(_B)
_EntLanMacFilterEntry_Object=MibTableRow
entLanMacFilterEntry=_EntLanMacFilterEntry_Object((1,3,6,1,4,1,14125,100,4,3,1))
entLanMacFilterEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:entLanMacFilterEntry.setStatus(_B)
_EntMacAddressIndex_Type=Integer32
_EntMacAddressIndex_Object=MibTableColumn
entMacAddressIndex=_EntMacAddressIndex_Object((1,3,6,1,4,1,14125,100,4,3,1,1),_EntMacAddressIndex_Type())
entMacAddressIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entMacAddressIndex.setStatus(_B)
_EntMacAddress_Type=DisplayString
_EntMacAddress_Object=MibTableColumn
entMacAddress=_EntMacAddress_Object((1,3,6,1,4,1,14125,100,4,3,1,2),_EntMacAddress_Type())
entMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:entMacAddress.setStatus(_B)
_EntMacFilteringValid_Type=TruthValue
_EntMacFilteringValid_Object=MibTableColumn
entMacFilteringValid=_EntMacFilteringValid_Object((1,3,6,1,4,1,14125,100,4,3,1,3),_EntMacFilteringValid_Type())
entMacFilteringValid.setMaxAccess(_E)
if mibBuilder.loadTexts:entMacFilteringValid.setStatus(_B)
_EntWlan_ObjectIdentity=ObjectIdentity
entWlan=_EntWlan_ObjectIdentity((1,3,6,1,4,1,14125,100,5))
_EntWlanCommonInfo_ObjectIdentity=ObjectIdentity
entWlanCommonInfo=_EntWlanCommonInfo_ObjectIdentity((1,3,6,1,4,1,14125,100,5,1))
class _EntOpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ap',0),(_K,1),(_L,2),(_J,3)))
_EntOpMode_Type.__name__=_D
_EntOpMode_Object=MibScalar
entOpMode=_EntOpMode_Object((1,3,6,1,4,1,14125,100,5,1,1),_EntOpMode_Type())
entOpMode.setMaxAccess(_A)
if mibBuilder.loadTexts:entOpMode.setStatus(_C)
_EntRadio_Type=TruthValue
_EntRadio_Object=MibScalar
entRadio=_EntRadio_Object((1,3,6,1,4,1,14125,100,5,1,2),_EntRadio_Type())
entRadio.setMaxAccess(_A)
if mibBuilder.loadTexts:entRadio.setStatus(_C)
class _EntAPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ap',0),('wds',1)))
_EntAPMode_Type.__name__=_D
_EntAPMode_Object=MibScalar
entAPMode=_EntAPMode_Object((1,3,6,1,4,1,14125,100,5,1,3),_EntAPMode_Type())
entAPMode.setMaxAccess(_A)
if mibBuilder.loadTexts:entAPMode.setStatus(_C)
class _EntBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,7,8,9)));namedValues=NamedValues(*(('ieee802dot11-b-g',0),('ieee802dot11-b',1),('ieee802dot11-a',2),('ieee802dot11-g',4),('ieee802dot11-n',6),('ieee802dot11-g-n',7),('ieee802dot11-a-n',8),('ieee802dot11-b-g-n',9)))
_EntBand_Type.__name__=_D
_EntBand_Object=MibScalar
entBand=_EntBand_Object((1,3,6,1,4,1,14125,100,5,1,4),_EntBand_Type())
entBand.setMaxAccess(_A)
if mibBuilder.loadTexts:entBand.setStatus(_C)
class _EntESSIDNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EntESSIDNum_Type.__name__=_D
_EntESSIDNum_Object=MibScalar
entESSIDNum=_EntESSIDNum_Object((1,3,6,1,4,1,14125,100,5,1,5),_EntESSIDNum_Type())
entESSIDNum.setMaxAccess(_A)
if mibBuilder.loadTexts:entESSIDNum.setStatus(_C)
class _EntChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_EntChannel_Type.__name__=_D
_EntChannel_Object=MibScalar
entChannel=_EntChannel_Object((1,3,6,1,4,1,14125,100,5,1,6),_EntChannel_Type())
entChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:entChannel.setStatus(_C)
class _EntDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5,6,9,11,12,18,24,36,48,54)));namedValues=NamedValues(*(('auto',0),('oneMbps',1),('twoMbps',2),('fiveNhalfMbps',5),('sixMbps',6),('nineMbps',9),('elevenMbps',11),('twelveMbps',12),('eighteenMbps',18),('twentytwoMbps',24),('thirtysixMbps',36),('fortyeightMbps',48),('fiftyfourMbps',54)))
_EntDataRate_Type.__name__=_D
_EntDataRate_Object=MibScalar
entDataRate=_EntDataRate_Object((1,3,6,1,4,1,14125,100,5,1,7),_EntDataRate_Type())
entDataRate.setMaxAccess(_A)
if mibBuilder.loadTexts:entDataRate.setStatus(_C)
_EntNDataRate_Type=Integer32
_EntNDataRate_Object=MibScalar
entNDataRate=_EntNDataRate_Object((1,3,6,1,4,1,14125,100,5,1,8),_EntNDataRate_Type())
entNDataRate.setMaxAccess(_A)
if mibBuilder.loadTexts:entNDataRate.setStatus(_C)
_EntTxPower_Type=Integer32
_EntTxPower_Object=MibScalar
entTxPower=_EntTxPower_Object((1,3,6,1,4,1,14125,100,5,1,9),_EntTxPower_Type())
entTxPower.setMaxAccess(_A)
if mibBuilder.loadTexts:entTxPower.setStatus(_C)
class _EntBeaconInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1024))
_EntBeaconInterval_Type.__name__=_D
_EntBeaconInterval_Object=MibScalar
entBeaconInterval=_EntBeaconInterval_Object((1,3,6,1,4,1,14125,100,5,1,10),_EntBeaconInterval_Type())
entBeaconInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:entBeaconInterval.setStatus(_C)
class _EntDTIMPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EntDTIMPeriod_Type.__name__=_D
_EntDTIMPeriod_Object=MibScalar
entDTIMPeriod=_EntDTIMPeriod_Object((1,3,6,1,4,1,14125,100,5,1,11),_EntDTIMPeriod_Type())
entDTIMPeriod.setMaxAccess(_A)
if mibBuilder.loadTexts:entDTIMPeriod.setStatus(_C)
class _EntFragmentationThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_EntFragmentationThreshold_Type.__name__=_D
_EntFragmentationThreshold_Object=MibScalar
entFragmentationThreshold=_EntFragmentationThreshold_Object((1,3,6,1,4,1,14125,100,5,1,12),_EntFragmentationThreshold_Type())
entFragmentationThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:entFragmentationThreshold.setStatus(_C)
class _EntRTSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_EntRTSThreshold_Type.__name__=_D
_EntRTSThreshold_Object=MibScalar
entRTSThreshold=_EntRTSThreshold_Object((1,3,6,1,4,1,14125,100,5,1,13),_EntRTSThreshold_Type())
entRTSThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:entRTSThreshold.setStatus(_C)
class _EntChannelBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_EntChannelBandwidth_Type.__name__=_D
_EntChannelBandwidth_Object=MibScalar
entChannelBandwidth=_EntChannelBandwidth_Object((1,3,6,1,4,1,14125,100,5,1,14),_EntChannelBandwidth_Type())
entChannelBandwidth.setMaxAccess(_A)
if mibBuilder.loadTexts:entChannelBandwidth.setStatus(_C)
class _EntPreambleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_EntPreambleType_Type.__name__=_D
_EntPreambleType_Object=MibScalar
entPreambleType=_EntPreambleType_Object((1,3,6,1,4,1,14125,100,5,1,15),_EntPreambleType_Type())
entPreambleType.setMaxAccess(_A)
if mibBuilder.loadTexts:entPreambleType.setStatus(_C)
class _EntCTSProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('always',1),('none',2)))
_EntCTSProtection_Type.__name__=_D
_EntCTSProtection_Object=MibScalar
entCTSProtection=_EntCTSProtection_Object((1,3,6,1,4,1,14125,100,5,1,16),_EntCTSProtection_Type())
entCTSProtection.setMaxAccess(_A)
if mibBuilder.loadTexts:entCTSProtection.setStatus(_C)
_EntWlanESSIDInfoTable_Object=MibTable
entWlanESSIDInfoTable=_EntWlanESSIDInfoTable_Object((1,3,6,1,4,1,14125,100,5,2))
if mibBuilder.loadTexts:entWlanESSIDInfoTable.setStatus(_B)
_EntWlanESSIDInfoEntry_Object=MibTableRow
entWlanESSIDInfoEntry=_EntWlanESSIDInfoEntry_Object((1,3,6,1,4,1,14125,100,5,2,1))
entWlanESSIDInfoEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:entWlanESSIDInfoEntry.setStatus(_B)
_EntWlanESSIDInfoIndex_Type=Integer32
_EntWlanESSIDInfoIndex_Object=MibTableColumn
entWlanESSIDInfoIndex=_EntWlanESSIDInfoIndex_Object((1,3,6,1,4,1,14125,100,5,2,1,1),_EntWlanESSIDInfoIndex_Type())
entWlanESSIDInfoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entWlanESSIDInfoIndex.setStatus(_B)
class _EntESSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EntESSID_Type.__name__=_I
_EntESSID_Object=MibTableColumn
entESSID=_EntESSID_Object((1,3,6,1,4,1,14125,100,5,2,1,2),_EntESSID_Type())
entESSID.setMaxAccess(_A)
if mibBuilder.loadTexts:entESSID.setStatus(_B)
_EntBroadcastESSID_Type=TruthValue
_EntBroadcastESSID_Object=MibTableColumn
entBroadcastESSID=_EntBroadcastESSID_Object((1,3,6,1,4,1,14125,100,5,2,1,3),_EntBroadcastESSID_Type())
entBroadcastESSID.setMaxAccess(_A)
if mibBuilder.loadTexts:entBroadcastESSID.setStatus(_C)
_EntWMM_Type=TruthValue
_EntWMM_Object=MibTableColumn
entWMM=_EntWMM_Object((1,3,6,1,4,1,14125,100,5,2,1,4),_EntWMM_Type())
entWMM.setMaxAccess(_A)
if mibBuilder.loadTexts:entWMM.setStatus(_C)
class _EntEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_EntEncryption_Type.__name__=_D
_EntEncryption_Object=MibTableColumn
entEncryption=_EntEncryption_Object((1,3,6,1,4,1,14125,100,5,2,1,5),_EntEncryption_Type())
entEncryption.setMaxAccess(_A)
if mibBuilder.loadTexts:entEncryption.setStatus(_B)
class _EntWlanAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_EntWlanAuthenticationType_Type.__name__=_D
_EntWlanAuthenticationType_Object=MibTableColumn
entWlanAuthenticationType=_EntWlanAuthenticationType_Object((1,3,6,1,4,1,14125,100,5,2,1,6),_EntWlanAuthenticationType_Type())
entWlanAuthenticationType.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlanAuthenticationType.setStatus(_B)
_EntWlanWepInfoTable_Object=MibTable
entWlanWepInfoTable=_EntWlanWepInfoTable_Object((1,3,6,1,4,1,14125,100,5,3))
if mibBuilder.loadTexts:entWlanWepInfoTable.setStatus(_B)
_EntWlanWepInfoEntry_Object=MibTableRow
entWlanWepInfoEntry=_EntWlanWepInfoEntry_Object((1,3,6,1,4,1,14125,100,5,3,1))
entWlanWepInfoEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:entWlanWepInfoEntry.setStatus(_B)
_EntWlanESSIDIndex_Type=Integer32
_EntWlanESSIDIndex_Object=MibTableColumn
entWlanESSIDIndex=_EntWlanESSIDIndex_Object((1,3,6,1,4,1,14125,100,5,3,1,1),_EntWlanESSIDIndex_Type())
entWlanESSIDIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entWlanESSIDIndex.setStatus(_B)
class _EntWlanWepKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EntWlanWepKeyID_Type.__name__=_D
_EntWlanWepKeyID_Object=MibTableColumn
entWlanWepKeyID=_EntWlanWepKeyID_Object((1,3,6,1,4,1,14125,100,5,3,1,2),_EntWlanWepKeyID_Type())
entWlanWepKeyID.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlanWepKeyID.setStatus(_B)
_EntWlanWepKey1Value_Type=OctetString
_EntWlanWepKey1Value_Object=MibTableColumn
entWlanWepKey1Value=_EntWlanWepKey1Value_Object((1,3,6,1,4,1,14125,100,5,3,1,3),_EntWlanWepKey1Value_Type())
entWlanWepKey1Value.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlanWepKey1Value.setStatus(_B)
_EntWlanWepKey2Value_Type=OctetString
_EntWlanWepKey2Value_Object=MibTableColumn
entWlanWepKey2Value=_EntWlanWepKey2Value_Object((1,3,6,1,4,1,14125,100,5,3,1,4),_EntWlanWepKey2Value_Type())
entWlanWepKey2Value.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlanWepKey2Value.setStatus(_B)
_EntWlanWepKey3Value_Type=OctetString
_EntWlanWepKey3Value_Object=MibTableColumn
entWlanWepKey3Value=_EntWlanWepKey3Value_Object((1,3,6,1,4,1,14125,100,5,3,1,5),_EntWlanWepKey3Value_Type())
entWlanWepKey3Value.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlanWepKey3Value.setStatus(_B)
_EntWlanWepKey4Value_Type=OctetString
_EntWlanWepKey4Value_Object=MibTableColumn
entWlanWepKey4Value=_EntWlanWepKey4Value_Object((1,3,6,1,4,1,14125,100,5,3,1,6),_EntWlanWepKey4Value_Type())
entWlanWepKey4Value.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlanWepKey4Value.setStatus(_B)
_EntWlanWPAInfoTable_Object=MibTable
entWlanWPAInfoTable=_EntWlanWPAInfoTable_Object((1,3,6,1,4,1,14125,100,5,4))
if mibBuilder.loadTexts:entWlanWPAInfoTable.setStatus(_B)
_EntWlanWPAInfoEntry_Object=MibTableRow
entWlanWPAInfoEntry=_EntWlanWPAInfoEntry_Object((1,3,6,1,4,1,14125,100,5,4,1))
entWlanWPAInfoEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:entWlanWPAInfoEntry.setStatus(_B)
_EntWlanWPAESSIDIndex_Type=Integer32
_EntWlanWPAESSIDIndex_Object=MibTableColumn
entWlanWPAESSIDIndex=_EntWlanWPAESSIDIndex_Object((1,3,6,1,4,1,14125,100,5,4,1,1),_EntWlanWPAESSIDIndex_Type())
entWlanWPAESSIDIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entWlanWPAESSIDIndex.setStatus(_B)
_EntPresharedKey_Type=DisplayString
_EntPresharedKey_Object=MibTableColumn
entPresharedKey=_EntPresharedKey_Object((1,3,6,1,4,1,14125,100,5,4,1,2),_EntPresharedKey_Type())
entPresharedKey.setMaxAccess(_G)
if mibBuilder.loadTexts:entPresharedKey.setStatus(_B)
_Ent802dot1xInfoTable_Object=MibTable
ent802dot1xInfoTable=_Ent802dot1xInfoTable_Object((1,3,6,1,4,1,14125,100,5,5))
if mibBuilder.loadTexts:ent802dot1xInfoTable.setStatus(_B)
_Ent802dot1xInfoEntry_Object=MibTableRow
ent802dot1xInfoEntry=_Ent802dot1xInfoEntry_Object((1,3,6,1,4,1,14125,100,5,5,1))
ent802dot1xInfoEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:ent802dot1xInfoEntry.setStatus(_B)
_EntWlan802dot1xESSIDIndex_Type=Integer32
_EntWlan802dot1xESSIDIndex_Object=MibTableColumn
entWlan802dot1xESSIDIndex=_EntWlan802dot1xESSIDIndex_Object((1,3,6,1,4,1,14125,100,5,5,1,1),_EntWlan802dot1xESSIDIndex_Type())
entWlan802dot1xESSIDIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entWlan802dot1xESSIDIndex.setStatus(_B)
_EntRADIUSServerIPAddress_Type=IpAddress
_EntRADIUSServerIPAddress_Object=MibTableColumn
entRADIUSServerIPAddress=_EntRADIUSServerIPAddress_Object((1,3,6,1,4,1,14125,100,5,5,1,2),_EntRADIUSServerIPAddress_Type())
entRADIUSServerIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:entRADIUSServerIPAddress.setStatus(_B)
class _EntRADIUSServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EntRADIUSServerPort_Type.__name__=_D
_EntRADIUSServerPort_Object=MibTableColumn
entRADIUSServerPort=_EntRADIUSServerPort_Object((1,3,6,1,4,1,14125,100,5,5,1,3),_EntRADIUSServerPort_Type())
entRADIUSServerPort.setMaxAccess(_A)
if mibBuilder.loadTexts:entRADIUSServerPort.setStatus(_B)
_EntRADIUSServerPassword_Type=DisplayString
_EntRADIUSServerPassword_Object=MibTableColumn
entRADIUSServerPassword=_EntRADIUSServerPassword_Object((1,3,6,1,4,1,14125,100,5,5,1,4),_EntRADIUSServerPassword_Type())
entRADIUSServerPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:entRADIUSServerPassword.setStatus(_B)
_EntWlan802dot1xEnable_Type=TruthValue
_EntWlan802dot1xEnable_Object=MibTableColumn
entWlan802dot1xEnable=_EntWlan802dot1xEnable_Object((1,3,6,1,4,1,14125,100,5,5,1,5),_EntWlan802dot1xEnable_Type())
entWlan802dot1xEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:entWlan802dot1xEnable.setStatus(_B)
_EntWlanClientListInfoTable_Object=MibTable
entWlanClientListInfoTable=_EntWlanClientListInfoTable_Object((1,3,6,1,4,1,14125,100,5,6))
if mibBuilder.loadTexts:entWlanClientListInfoTable.setStatus(_B)
_EntWlanClientListInfoEntry_Object=MibTableRow
entWlanClientListInfoEntry=_EntWlanClientListInfoEntry_Object((1,3,6,1,4,1,14125,100,5,6,1))
entWlanClientListInfoEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:entWlanClientListInfoEntry.setStatus(_B)
_EntCLInfoIndex_Type=Integer32
_EntCLInfoIndex_Object=MibTableColumn
entCLInfoIndex=_EntCLInfoIndex_Object((1,3,6,1,4,1,14125,100,5,6,1,1),_EntCLInfoIndex_Type())
entCLInfoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entCLInfoIndex.setStatus(_B)
_EntCLInterface_Type=OctetString
_EntCLInterface_Object=MibTableColumn
entCLInterface=_EntCLInterface_Object((1,3,6,1,4,1,14125,100,5,6,1,2),_EntCLInterface_Type())
entCLInterface.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLInterface.setStatus(_B)
_EntCLMAC_Type=OctetString
_EntCLMAC_Object=MibTableColumn
entCLMAC=_EntCLMAC_Object((1,3,6,1,4,1,14125,100,5,6,1,3),_EntCLMAC_Type())
entCLMAC.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLMAC.setStatus(_B)
_EntCLRx_Type=OctetString
_EntCLRx_Object=MibTableColumn
entCLRx=_EntCLRx_Object((1,3,6,1,4,1,14125,100,5,6,1,4),_EntCLRx_Type())
entCLRx.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLRx.setStatus(_B)
_EntCLTx_Type=OctetString
_EntCLTx_Object=MibTableColumn
entCLTx=_EntCLTx_Object((1,3,6,1,4,1,14125,100,5,6,1,5),_EntCLTx_Type())
entCLTx.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLTx.setStatus(_B)
_EntCLSignal_Type=Integer32
_EntCLSignal_Object=MibTableColumn
entCLSignal=_EntCLSignal_Object((1,3,6,1,4,1,14125,100,5,6,1,6),_EntCLSignal_Type())
entCLSignal.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLSignal.setStatus(_B)
_EntCLConnectedTime_Type=OctetString
_EntCLConnectedTime_Object=MibTableColumn
entCLConnectedTime=_EntCLConnectedTime_Object((1,3,6,1,4,1,14125,100,5,6,1,7),_EntCLConnectedTime_Type())
entCLConnectedTime.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLConnectedTime.setStatus(_B)
_EntCLIdleTime_Type=OctetString
_EntCLIdleTime_Object=MibTableColumn
entCLIdleTime=_EntCLIdleTime_Object((1,3,6,1,4,1,14125,100,5,6,1,8),_EntCLIdleTime_Type())
entCLIdleTime.setMaxAccess(_A)
if mibBuilder.loadTexts:entCLIdleTime.setStatus(_B)
_EntSNMP_ObjectIdentity=ObjectIdentity
entSNMP=_EntSNMP_ObjectIdentity((1,3,6,1,4,1,14125,100,6))
_EntSNMPStatus_Type=TruthValue
_EntSNMPStatus_Object=MibScalar
entSNMPStatus=_EntSNMPStatus_Object((1,3,6,1,4,1,14125,100,6,1),_EntSNMPStatus_Type())
entSNMPStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:entSNMPStatus.setStatus(_C)
class _EntSNMPVerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('v1',1),('v2c',2),('v3',3)))
_EntSNMPVerType_Type.__name__=_D
_EntSNMPVerType_Object=MibScalar
entSNMPVerType=_EntSNMPVerType_Object((1,3,6,1,4,1,14125,100,6,2),_EntSNMPVerType_Type())
entSNMPVerType.setMaxAccess(_A)
if mibBuilder.loadTexts:entSNMPVerType.setStatus(_C)
_EntSNMPCommunityTable_Object=MibTable
entSNMPCommunityTable=_EntSNMPCommunityTable_Object((1,3,6,1,4,1,14125,100,6,3))
if mibBuilder.loadTexts:entSNMPCommunityTable.setStatus(_B)
_EntSNMPCommunityEntry_Object=MibTableRow
entSNMPCommunityEntry=_EntSNMPCommunityEntry_Object((1,3,6,1,4,1,14125,100,6,3,1))
entSNMPCommunityEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:entSNMPCommunityEntry.setStatus(_B)
class _EntSNMPCommunityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_EntSNMPCommunityIndex_Type.__name__=_D
_EntSNMPCommunityIndex_Object=MibTableColumn
entSNMPCommunityIndex=_EntSNMPCommunityIndex_Object((1,3,6,1,4,1,14125,100,6,3,1,1),_EntSNMPCommunityIndex_Type())
entSNMPCommunityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entSNMPCommunityIndex.setStatus(_B)
class _EntSNMPCommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EntSNMPCommunityName_Type.__name__=_H
_EntSNMPCommunityName_Object=MibTableColumn
entSNMPCommunityName=_EntSNMPCommunityName_Object((1,3,6,1,4,1,14125,100,6,3,1,2),_EntSNMPCommunityName_Type())
entSNMPCommunityName.setMaxAccess(_A)
if mibBuilder.loadTexts:entSNMPCommunityName.setStatus(_B)
class _EntSNMPCommunityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('read',1),('write',2)))
_EntSNMPCommunityType_Type.__name__=_D
_EntSNMPCommunityType_Object=MibTableColumn
entSNMPCommunityType=_EntSNMPCommunityType_Object((1,3,6,1,4,1,14125,100,6,3,1,3),_EntSNMPCommunityType_Type())
entSNMPCommunityType.setMaxAccess(_E)
if mibBuilder.loadTexts:entSNMPCommunityType.setStatus(_B)
_EntSNMPCommunityValid_Type=TruthValue
_EntSNMPCommunityValid_Object=MibTableColumn
entSNMPCommunityValid=_EntSNMPCommunityValid_Object((1,3,6,1,4,1,14125,100,6,3,1,4),_EntSNMPCommunityValid_Type())
entSNMPCommunityValid.setMaxAccess(_E)
if mibBuilder.loadTexts:entSNMPCommunityValid.setStatus(_B)
_EntSNMPTrap_ObjectIdentity=ObjectIdentity
entSNMPTrap=_EntSNMPTrap_ObjectIdentity((1,3,6,1,4,1,14125,100,6,4))
_EntTrapStatus_Type=TruthValue
_EntTrapStatus_Object=MibScalar
entTrapStatus=_EntTrapStatus_Object((1,3,6,1,4,1,14125,100,6,4,1),_EntTrapStatus_Type())
entTrapStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:entTrapStatus.setStatus(_C)
class _EntTrapVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('v1',1),('v2c',2),('v3',3)))
_EntTrapVer_Type.__name__=_D
_EntTrapVer_Object=MibScalar
entTrapVer=_EntTrapVer_Object((1,3,6,1,4,1,14125,100,6,4,2),_EntTrapVer_Type())
entTrapVer.setMaxAccess(_A)
if mibBuilder.loadTexts:entTrapVer.setStatus(_C)
_EntTrapReceiverIPAddress_Type=IpAddress
_EntTrapReceiverIPAddress_Object=MibScalar
entTrapReceiverIPAddress=_EntTrapReceiverIPAddress_Object((1,3,6,1,4,1,14125,100,6,4,3),_EntTrapReceiverIPAddress_Type())
entTrapReceiverIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:entTrapReceiverIPAddress.setStatus(_C)
_EntTrapReceiverCommunityName_Type=DisplayString
_EntTrapReceiverCommunityName_Object=MibScalar
entTrapReceiverCommunityName=_EntTrapReceiverCommunityName_Object((1,3,6,1,4,1,14125,100,6,4,4),_EntTrapReceiverCommunityName_Type())
entTrapReceiverCommunityName.setMaxAccess(_A)
if mibBuilder.loadTexts:entTrapReceiverCommunityName.setStatus(_C)
_EntTraps_ObjectIdentity=ObjectIdentity
entTraps=_EntTraps_ObjectIdentity((1,3,6,1,4,1,14125,100,20))
_EntSystemTraps_ObjectIdentity=ObjectIdentity
entSystemTraps=_EntSystemTraps_ObjectIdentity((1,3,6,1,4,1,14125,100,20,1))
_EntWanTraps_ObjectIdentity=ObjectIdentity
entWanTraps=_EntWanTraps_ObjectIdentity((1,3,6,1,4,1,14125,100,20,2))
entSystemTrapsReboot=NotificationType((1,3,6,1,4,1,14125,100,20,1,1))
if mibBuilder.loadTexts:entSystemTrapsReboot.setStatus(_B)
entSystemTrapsRestoreToDefault=NotificationType((1,3,6,1,4,1,14125,100,20,1,2))
if mibBuilder.loadTexts:entSystemTrapsRestoreToDefault.setStatus(_B)
entSystemTrapsReloadModules=NotificationType((1,3,6,1,4,1,14125,100,20,1,3))
if mibBuilder.loadTexts:entSystemTrapsReloadModules.setStatus(_B)
entWanTrapsLinkDisconnect=NotificationType((1,3,6,1,4,1,14125,100,20,2,1))
entWanTrapsLinkDisconnect.setObjects((_F,_T))
if mibBuilder.loadTexts:entWanTrapsLinkDisconnect.setStatus(_B)
entWanTrapsLinkRecover=NotificationType((1,3,6,1,4,1,14125,100,20,2,2))
entWanTrapsLinkRecover.setObjects((_F,_T))
if mibBuilder.loadTexts:entWanTrapsLinkRecover.setStatus(_B)
mibBuilder.exportSymbols(_F,**{'senao':senao,'indoorWirelessDevice':indoorWirelessDevice,'entSystem':entSystem,'entPassword':entPassword,'entSysModel':entSysModel,'entSysMode':entSysMode,'entSysUpTime':entSysUpTime,'entHwVersion':entHwVersion,'entSN':entSN,'entKenelVersion':entKenelVersion,'entAppVersion':entAppVersion,'entReset':entReset,'entResetToDefault':entResetToDefault,'entApplyModules':entApplyModules,'entLAN':entLAN,'entLANIP':entLANIP,'entLANSubnetMask':entLANSubnetMask,'entSTPEnable':entSTPEnable,'entDHCPEnable':entDHCPEnable,'entIPPoolStart':entIPPoolStart,'entIPPoolEnd':entIPPoolEnd,'entIPLeaseTime':entIPLeaseTime,'entWAN':entWAN,'entRouterEnable':entRouterEnable,'entMacFilter':entMacFilter,'entLanMacFilteringEnable':entLanMacFilteringEnable,'entLanMacFilteringMode':entLanMacFilteringMode,'entLanMacFilterTable':entLanMacFilterTable,'entLanMacFilterEntry':entLanMacFilterEntry,_M:entMacAddressIndex,'entMacAddress':entMacAddress,'entMacFilteringValid':entMacFilteringValid,'entWlan':entWlan,'entWlanCommonInfo':entWlanCommonInfo,'entOpMode':entOpMode,'entRadio':entRadio,'entAPMode':entAPMode,'entBand':entBand,'entESSIDNum':entESSIDNum,'entChannel':entChannel,'entDataRate':entDataRate,'entNDataRate':entNDataRate,'entTxPower':entTxPower,'entBeaconInterval':entBeaconInterval,'entDTIMPeriod':entDTIMPeriod,'entFragmentationThreshold':entFragmentationThreshold,'entRTSThreshold':entRTSThreshold,'entChannelBandwidth':entChannelBandwidth,'entPreambleType':entPreambleType,'entCTSProtection':entCTSProtection,'entWlanESSIDInfoTable':entWlanESSIDInfoTable,'entWlanESSIDInfoEntry':entWlanESSIDInfoEntry,_N:entWlanESSIDInfoIndex,'entESSID':entESSID,'entBroadcastESSID':entBroadcastESSID,'entWMM':entWMM,'entEncryption':entEncryption,'entWlanAuthenticationType':entWlanAuthenticationType,'entWlanWepInfoTable':entWlanWepInfoTable,'entWlanWepInfoEntry':entWlanWepInfoEntry,_O:entWlanESSIDIndex,'entWlanWepKeyID':entWlanWepKeyID,'entWlanWepKey1Value':entWlanWepKey1Value,'entWlanWepKey2Value':entWlanWepKey2Value,'entWlanWepKey3Value':entWlanWepKey3Value,'entWlanWepKey4Value':entWlanWepKey4Value,'entWlanWPAInfoTable':entWlanWPAInfoTable,'entWlanWPAInfoEntry':entWlanWPAInfoEntry,_P:entWlanWPAESSIDIndex,'entPresharedKey':entPresharedKey,'ent802dot1xInfoTable':ent802dot1xInfoTable,'ent802dot1xInfoEntry':ent802dot1xInfoEntry,_Q:entWlan802dot1xESSIDIndex,'entRADIUSServerIPAddress':entRADIUSServerIPAddress,'entRADIUSServerPort':entRADIUSServerPort,'entRADIUSServerPassword':entRADIUSServerPassword,'entWlan802dot1xEnable':entWlan802dot1xEnable,'entWlanClientListInfoTable':entWlanClientListInfoTable,'entWlanClientListInfoEntry':entWlanClientListInfoEntry,_R:entCLInfoIndex,'entCLInterface':entCLInterface,'entCLMAC':entCLMAC,'entCLRx':entCLRx,'entCLTx':entCLTx,'entCLSignal':entCLSignal,'entCLConnectedTime':entCLConnectedTime,'entCLIdleTime':entCLIdleTime,'entSNMP':entSNMP,'entSNMPStatus':entSNMPStatus,'entSNMPVerType':entSNMPVerType,'entSNMPCommunityTable':entSNMPCommunityTable,'entSNMPCommunityEntry':entSNMPCommunityEntry,_S:entSNMPCommunityIndex,'entSNMPCommunityName':entSNMPCommunityName,'entSNMPCommunityType':entSNMPCommunityType,'entSNMPCommunityValid':entSNMPCommunityValid,'entSNMPTrap':entSNMPTrap,'entTrapStatus':entTrapStatus,'entTrapVer':entTrapVer,'entTrapReceiverIPAddress':entTrapReceiverIPAddress,'entTrapReceiverCommunityName':entTrapReceiverCommunityName,'entTraps':entTraps,'entSystemTraps':entSystemTraps,'entSystemTrapsReboot':entSystemTrapsReboot,'entSystemTrapsRestoreToDefault':entSystemTrapsRestoreToDefault,'entSystemTrapsReloadModules':entSystemTrapsReloadModules,'entWanTraps':entWanTraps,'entWanTrapsLinkDisconnect':entWanTrapsLinkDisconnect,'entWanTrapsLinkRecover':entWanTrapsLinkRecover})