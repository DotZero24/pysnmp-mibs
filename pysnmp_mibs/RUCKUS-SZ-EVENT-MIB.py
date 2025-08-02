_AU='ruckusSZUECaleaRx'
_AT='ruckusSZUECaleaTx'
_AS='ruckusSZEventAuthType'
_AR='ruckusSZHDDHealthDegradationStatus'
_AQ='ruckusSZDestSyslogServerAddress'
_AP='ruckusSZSrcSyslogServerAddress'
_AO='ruckusSZAccSrvrIp'
_AN='ruckusSZFileName'
_AM='ruckusSZFtpPort'
_AL='ruckusSZFtpIp'
_AK='ruckusSZSwitchStatus'
_AJ='ruckusSZSoftGREGWAddress'
_AI='ruckusSoftGREGatewayList'
_AH='ruckusSZEventRogueType'
_AG='ruckusSZEventRogueRuleName'
_AF='ruckusSZEventRoguePolicyName'
_AE='ruckusSZEventZoneName'
_AD='ruckusSZLicenseUsagePerc'
_AC='ruckusSZLicenseType'
_AB='ruckusSZDNATIp'
_AA='ruckusSZSoftwareName'
_A9='ruckusSZADSrvrIp'
_A8='ruckusSZLDAPSrvrIp'
_A7='ruckusSZSyslogServerAddress'
_A6='ruckusSZLicenseServerName'
_A5='ruckusSZRadProxyIp'
_A4='ruckusSZProcessorId'
_A3='ruckusSZNetworkPortID'
_A2='ruckusSZDPConfigID'
_A1='ruckusSecondaryGRE'
_A0='ruckusPrimaryGRE'
_z='ruckusSZConfigAPModel'
_y='ruckusSZAPModel'
_x='ruckusSZAPConfigID'
_w='ruckusSZDiskPerc'
_v='ruckusSZMemoryPerc'
_u='ruckusSZCPUPerc'
_t='ruckusSZIPSecGWAddress'
_s='ruckusSZAuthSrvrIp'
_r='ruckusSZEventClientMacAddr'
_q='ruckusSZEventUpgradedFirmwareVersion'
_p='ruckusSZEventFirmwareVersion'
_o='ruckusSZEventDescription'
_n='ruckusSZRadSrvrIp'
_m='ruckusSZUserName'
_l='ruckusSZFanStatus'
_k='ruckusSZFanId'
_j='ruckusSZTemperatureStatus'
_i='ruckusSZNetworkInterface'
_h='ruckusSZUEMsisdn'
_g='ruckusSZUEImsi'
_f='ruckusSZProcessName'
_e='ruckusSZEventRogueMac'
_d='ruckusSZSrcProcess'
_c='ruckusSZEventSSID'
_b='ruckusSZLBSPort'
_a='ruckusSZLBSURL'
_Z='ruckusSZDPIP'
_Y='ruckusSZEventCtrlIP'
_X='ruckusSZEventSwitchMacAddr'
_W='ruckusSZEventSwitchName'
_V='ruckusSZEventSwitchGroupLevelTwoName'
_U='ruckusSZEventSwitchGroupLevelOneName'
_T='ruckusSZDomainName'
_S='ruckusSZEventReason'
_R='ruckusSZDPKey'
_Q='ruckusSZClusterName'
_P='ruckusSZEventNodeMgmtIp'
_O='ruckusSZEventNodeName'
_N='ruckusSZEventAPIPv6'
_M='ruckusSZEventAPGPSCoordinates'
_L='ruckusSZEventAPDescription'
_K='ruckusSZEventAPLocation'
_J='ruckusSZEventMacAddr'
_I='ruckusSZEventAPIP'
_H='ruckusSZEventAPName'
_G='ruckusSZEventAPMacAddr'
_F='accessible-for-notify'
_E='ruckusSZEventType'
_D='ruckusSZEventCode'
_C='ruckusSZEventSeverity'
_B='current'
_A='RUCKUS-SZ-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusEvents,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusEvents')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ruckusSZEventMIB=ModuleIdentity((1,3,6,1,4,1,25053,2,11))
_RuckusSZEventTraps_ObjectIdentity=ObjectIdentity
ruckusSZEventTraps=_RuckusSZEventTraps_ObjectIdentity((1,3,6,1,4,1,25053,2,11,1))
_RuckusSZEventObjects_ObjectIdentity=ObjectIdentity
ruckusSZEventObjects=_RuckusSZEventObjects_ObjectIdentity((1,3,6,1,4,1,25053,2,11,2))
_RuckusSZEventDescription_Type=OctetString
_RuckusSZEventDescription_Object=MibScalar
ruckusSZEventDescription=_RuckusSZEventDescription_Object((1,3,6,1,4,1,25053,2,11,2,1),_RuckusSZEventDescription_Type())
ruckusSZEventDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventDescription.setStatus(_B)
_RuckusSZClusterName_Type=OctetString
_RuckusSZClusterName_Object=MibScalar
ruckusSZClusterName=_RuckusSZClusterName_Object((1,3,6,1,4,1,25053,2,11,2,2),_RuckusSZClusterName_Type())
ruckusSZClusterName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZClusterName.setStatus(_B)
_RuckusSZEventCode_Type=OctetString
_RuckusSZEventCode_Object=MibScalar
ruckusSZEventCode=_RuckusSZEventCode_Object((1,3,6,1,4,1,25053,2,11,2,10),_RuckusSZEventCode_Type())
ruckusSZEventCode.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventCode.setStatus(_B)
_RuckusSZProcessName_Type=OctetString
_RuckusSZProcessName_Object=MibScalar
ruckusSZProcessName=_RuckusSZProcessName_Object((1,3,6,1,4,1,25053,2,11,2,11),_RuckusSZProcessName_Type())
ruckusSZProcessName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZProcessName.setStatus(_B)
_RuckusSZEventCtrlIP_Type=OctetString
_RuckusSZEventCtrlIP_Object=MibScalar
ruckusSZEventCtrlIP=_RuckusSZEventCtrlIP_Object((1,3,6,1,4,1,25053,2,11,2,12),_RuckusSZEventCtrlIP_Type())
ruckusSZEventCtrlIP.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventCtrlIP.setStatus(_B)
_RuckusSZEventSeverity_Type=OctetString
_RuckusSZEventSeverity_Object=MibScalar
ruckusSZEventSeverity=_RuckusSZEventSeverity_Object((1,3,6,1,4,1,25053,2,11,2,13),_RuckusSZEventSeverity_Type())
ruckusSZEventSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventSeverity.setStatus(_B)
_RuckusSZEventType_Type=OctetString
_RuckusSZEventType_Object=MibScalar
ruckusSZEventType=_RuckusSZEventType_Object((1,3,6,1,4,1,25053,2,11,2,14),_RuckusSZEventType_Type())
ruckusSZEventType.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventType.setStatus(_B)
_RuckusSZEventNodeMgmtIp_Type=OctetString
_RuckusSZEventNodeMgmtIp_Object=MibScalar
ruckusSZEventNodeMgmtIp=_RuckusSZEventNodeMgmtIp_Object((1,3,6,1,4,1,25053,2,11,2,15),_RuckusSZEventNodeMgmtIp_Type())
ruckusSZEventNodeMgmtIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventNodeMgmtIp.setStatus(_B)
_RuckusSZEventNodeName_Type=OctetString
_RuckusSZEventNodeName_Object=MibScalar
ruckusSZEventNodeName=_RuckusSZEventNodeName_Object((1,3,6,1,4,1,25053,2,11,2,16),_RuckusSZEventNodeName_Type())
ruckusSZEventNodeName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventNodeName.setStatus(_B)
_RuckusSZCPUPerc_Type=OctetString
_RuckusSZCPUPerc_Object=MibScalar
ruckusSZCPUPerc=_RuckusSZCPUPerc_Object((1,3,6,1,4,1,25053,2,11,2,17),_RuckusSZCPUPerc_Type())
ruckusSZCPUPerc.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZCPUPerc.setStatus(_B)
_RuckusSZMemoryPerc_Type=OctetString
_RuckusSZMemoryPerc_Object=MibScalar
ruckusSZMemoryPerc=_RuckusSZMemoryPerc_Object((1,3,6,1,4,1,25053,2,11,2,18),_RuckusSZMemoryPerc_Type())
ruckusSZMemoryPerc.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZMemoryPerc.setStatus(_B)
_RuckusSZDiskPerc_Type=OctetString
_RuckusSZDiskPerc_Object=MibScalar
ruckusSZDiskPerc=_RuckusSZDiskPerc_Object((1,3,6,1,4,1,25053,2,11,2,19),_RuckusSZDiskPerc_Type())
ruckusSZDiskPerc.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDiskPerc.setStatus(_B)
_RuckusSZEventMacAddr_Type=OctetString
_RuckusSZEventMacAddr_Object=MibScalar
ruckusSZEventMacAddr=_RuckusSZEventMacAddr_Object((1,3,6,1,4,1,25053,2,11,2,20),_RuckusSZEventMacAddr_Type())
ruckusSZEventMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventMacAddr.setStatus(_B)
_RuckusSZEventFirmwareVersion_Type=OctetString
_RuckusSZEventFirmwareVersion_Object=MibScalar
ruckusSZEventFirmwareVersion=_RuckusSZEventFirmwareVersion_Object((1,3,6,1,4,1,25053,2,11,2,21),_RuckusSZEventFirmwareVersion_Type())
ruckusSZEventFirmwareVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventFirmwareVersion.setStatus(_B)
_RuckusSZEventUpgradedFirmwareVersion_Type=OctetString
_RuckusSZEventUpgradedFirmwareVersion_Object=MibScalar
ruckusSZEventUpgradedFirmwareVersion=_RuckusSZEventUpgradedFirmwareVersion_Object((1,3,6,1,4,1,25053,2,11,2,22),_RuckusSZEventUpgradedFirmwareVersion_Type())
ruckusSZEventUpgradedFirmwareVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventUpgradedFirmwareVersion.setStatus(_B)
_RuckusSZEventAPMacAddr_Type=OctetString
_RuckusSZEventAPMacAddr_Object=MibScalar
ruckusSZEventAPMacAddr=_RuckusSZEventAPMacAddr_Object((1,3,6,1,4,1,25053,2,11,2,23),_RuckusSZEventAPMacAddr_Type())
ruckusSZEventAPMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPMacAddr.setStatus(_B)
_RuckusSZEventReason_Type=OctetString
_RuckusSZEventReason_Object=MibScalar
ruckusSZEventReason=_RuckusSZEventReason_Object((1,3,6,1,4,1,25053,2,11,2,24),_RuckusSZEventReason_Type())
ruckusSZEventReason.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventReason.setStatus(_B)
_RuckusSZEventAPName_Type=OctetString
_RuckusSZEventAPName_Object=MibScalar
ruckusSZEventAPName=_RuckusSZEventAPName_Object((1,3,6,1,4,1,25053,2,11,2,25),_RuckusSZEventAPName_Type())
ruckusSZEventAPName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPName.setStatus(_B)
_RuckusSZEventAPIP_Type=OctetString
_RuckusSZEventAPIP_Object=MibScalar
ruckusSZEventAPIP=_RuckusSZEventAPIP_Object((1,3,6,1,4,1,25053,2,11,2,26),_RuckusSZEventAPIP_Type())
ruckusSZEventAPIP.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPIP.setStatus(_B)
_RuckusSZEventAPLocation_Type=OctetString
_RuckusSZEventAPLocation_Object=MibScalar
ruckusSZEventAPLocation=_RuckusSZEventAPLocation_Object((1,3,6,1,4,1,25053,2,11,2,27),_RuckusSZEventAPLocation_Type())
ruckusSZEventAPLocation.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPLocation.setStatus(_B)
_RuckusSZEventAPGPSCoordinates_Type=OctetString
_RuckusSZEventAPGPSCoordinates_Object=MibScalar
ruckusSZEventAPGPSCoordinates=_RuckusSZEventAPGPSCoordinates_Object((1,3,6,1,4,1,25053,2,11,2,28),_RuckusSZEventAPGPSCoordinates_Type())
ruckusSZEventAPGPSCoordinates.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPGPSCoordinates.setStatus(_B)
_RuckusSZEventAPDescription_Type=OctetString
_RuckusSZEventAPDescription_Object=MibScalar
ruckusSZEventAPDescription=_RuckusSZEventAPDescription_Object((1,3,6,1,4,1,25053,2,11,2,29),_RuckusSZEventAPDescription_Type())
ruckusSZEventAPDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPDescription.setStatus(_B)
_RuckusSZEventZoneName_Type=OctetString
_RuckusSZEventZoneName_Object=MibScalar
ruckusSZEventZoneName=_RuckusSZEventZoneName_Object((1,3,6,1,4,1,25053,2,11,2,30),_RuckusSZEventZoneName_Type())
ruckusSZEventZoneName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventZoneName.setStatus(_B)
_RuckusSZAPModel_Type=OctetString
_RuckusSZAPModel_Object=MibScalar
ruckusSZAPModel=_RuckusSZAPModel_Object((1,3,6,1,4,1,25053,2,11,2,31),_RuckusSZAPModel_Type())
ruckusSZAPModel.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZAPModel.setStatus(_B)
_RuckusSZConfigAPModel_Type=OctetString
_RuckusSZConfigAPModel_Object=MibScalar
ruckusSZConfigAPModel=_RuckusSZConfigAPModel_Object((1,3,6,1,4,1,25053,2,11,2,32),_RuckusSZConfigAPModel_Type())
ruckusSZConfigAPModel.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZConfigAPModel.setStatus(_B)
_RuckusSZAPConfigID_Type=OctetString
_RuckusSZAPConfigID_Object=MibScalar
ruckusSZAPConfigID=_RuckusSZAPConfigID_Object((1,3,6,1,4,1,25053,2,11,2,33),_RuckusSZAPConfigID_Type())
ruckusSZAPConfigID.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZAPConfigID.setStatus(_B)
_RuckusSZEventAPIPv6_Type=OctetString
_RuckusSZEventAPIPv6_Object=MibScalar
ruckusSZEventAPIPv6=_RuckusSZEventAPIPv6_Object((1,3,6,1,4,1,25053,2,11,2,35),_RuckusSZEventAPIPv6_Type())
ruckusSZEventAPIPv6.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAPIPv6.setStatus(_B)
_RuckusSZLBSURL_Type=OctetString
_RuckusSZLBSURL_Object=MibScalar
ruckusSZLBSURL=_RuckusSZLBSURL_Object((1,3,6,1,4,1,25053,2,11,2,38),_RuckusSZLBSURL_Type())
ruckusSZLBSURL.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZLBSURL.setStatus(_B)
_RuckusSZLBSPort_Type=OctetString
_RuckusSZLBSPort_Object=MibScalar
ruckusSZLBSPort=_RuckusSZLBSPort_Object((1,3,6,1,4,1,25053,2,11,2,39),_RuckusSZLBSPort_Type())
ruckusSZLBSPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZLBSPort.setStatus(_B)
_RuckusSZEventSSID_Type=OctetString
_RuckusSZEventSSID_Object=MibScalar
ruckusSZEventSSID=_RuckusSZEventSSID_Object((1,3,6,1,4,1,25053,2,11,2,40),_RuckusSZEventSSID_Type())
ruckusSZEventSSID.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventSSID.setStatus(_B)
_RuckusSZEventAuthType_Type=OctetString
_RuckusSZEventAuthType_Object=MibScalar
ruckusSZEventAuthType=_RuckusSZEventAuthType_Object((1,3,6,1,4,1,25053,2,11,2,41),_RuckusSZEventAuthType_Type())
ruckusSZEventAuthType.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventAuthType.setStatus(_B)
_RuckusSZEventRogueMac_Type=OctetString
_RuckusSZEventRogueMac_Object=MibScalar
ruckusSZEventRogueMac=_RuckusSZEventRogueMac_Object((1,3,6,1,4,1,25053,2,11,2,45),_RuckusSZEventRogueMac_Type())
ruckusSZEventRogueMac.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventRogueMac.setStatus(_B)
_RuckusPrimaryGRE_Type=OctetString
_RuckusPrimaryGRE_Object=MibScalar
ruckusPrimaryGRE=_RuckusPrimaryGRE_Object((1,3,6,1,4,1,25053,2,11,2,46),_RuckusPrimaryGRE_Type())
ruckusPrimaryGRE.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusPrimaryGRE.setStatus(_B)
_RuckusSecondaryGRE_Type=OctetString
_RuckusSecondaryGRE_Object=MibScalar
ruckusSecondaryGRE=_RuckusSecondaryGRE_Object((1,3,6,1,4,1,25053,2,11,2,47),_RuckusSecondaryGRE_Type())
ruckusSecondaryGRE.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSecondaryGRE.setStatus(_B)
_RuckusSoftGREGatewayList_Type=OctetString
_RuckusSoftGREGatewayList_Object=MibScalar
ruckusSoftGREGatewayList=_RuckusSoftGREGatewayList_Object((1,3,6,1,4,1,25053,2,11,2,48),_RuckusSoftGREGatewayList_Type())
ruckusSoftGREGatewayList.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSoftGREGatewayList.setStatus(_B)
_RuckusSZSoftGREGWAddress_Type=OctetString
_RuckusSZSoftGREGWAddress_Object=MibScalar
ruckusSZSoftGREGWAddress=_RuckusSZSoftGREGWAddress_Object((1,3,6,1,4,1,25053,2,11,2,49),_RuckusSZSoftGREGWAddress_Type())
ruckusSZSoftGREGWAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZSoftGREGWAddress.setStatus(_B)
_RuckusSZEventClientMacAddr_Type=OctetString
_RuckusSZEventClientMacAddr_Object=MibScalar
ruckusSZEventClientMacAddr=_RuckusSZEventClientMacAddr_Object((1,3,6,1,4,1,25053,2,11,2,50),_RuckusSZEventClientMacAddr_Type())
ruckusSZEventClientMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventClientMacAddr.setStatus(_B)
_RuckusSZDPKey_Type=OctetString
_RuckusSZDPKey_Object=MibScalar
ruckusSZDPKey=_RuckusSZDPKey_Object((1,3,6,1,4,1,25053,2,11,2,80),_RuckusSZDPKey_Type())
ruckusSZDPKey.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDPKey.setStatus(_B)
_RuckusSZDPConfigID_Type=OctetString
_RuckusSZDPConfigID_Object=MibScalar
ruckusSZDPConfigID=_RuckusSZDPConfigID_Object((1,3,6,1,4,1,25053,2,11,2,81),_RuckusSZDPConfigID_Type())
ruckusSZDPConfigID.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDPConfigID.setStatus(_B)
_RuckusSZDPIP_Type=OctetString
_RuckusSZDPIP_Object=MibScalar
ruckusSZDPIP=_RuckusSZDPIP_Object((1,3,6,1,4,1,25053,2,11,2,82),_RuckusSZDPIP_Type())
ruckusSZDPIP.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDPIP.setStatus(_B)
_RuckusSZNetworkPortID_Type=OctetString
_RuckusSZNetworkPortID_Object=MibScalar
ruckusSZNetworkPortID=_RuckusSZNetworkPortID_Object((1,3,6,1,4,1,25053,2,11,2,100),_RuckusSZNetworkPortID_Type())
ruckusSZNetworkPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZNetworkPortID.setStatus(_B)
_RuckusSZNetworkInterface_Type=OctetString
_RuckusSZNetworkInterface_Object=MibScalar
ruckusSZNetworkInterface=_RuckusSZNetworkInterface_Object((1,3,6,1,4,1,25053,2,11,2,101),_RuckusSZNetworkInterface_Type())
ruckusSZNetworkInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZNetworkInterface.setStatus(_B)
_RuckusSZSwitchStatus_Type=OctetString
_RuckusSZSwitchStatus_Object=MibScalar
ruckusSZSwitchStatus=_RuckusSZSwitchStatus_Object((1,3,6,1,4,1,25053,2,11,2,102),_RuckusSZSwitchStatus_Type())
ruckusSZSwitchStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZSwitchStatus.setStatus(_B)
_RuckusSZTemperatureStatus_Type=OctetString
_RuckusSZTemperatureStatus_Object=MibScalar
ruckusSZTemperatureStatus=_RuckusSZTemperatureStatus_Object((1,3,6,1,4,1,25053,2,11,2,120),_RuckusSZTemperatureStatus_Type())
ruckusSZTemperatureStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZTemperatureStatus.setStatus(_B)
_RuckusSZProcessorId_Type=OctetString
_RuckusSZProcessorId_Object=MibScalar
ruckusSZProcessorId=_RuckusSZProcessorId_Object((1,3,6,1,4,1,25053,2,11,2,121),_RuckusSZProcessorId_Type())
ruckusSZProcessorId.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZProcessorId.setStatus(_B)
_RuckusSZFanId_Type=OctetString
_RuckusSZFanId_Object=MibScalar
ruckusSZFanId=_RuckusSZFanId_Object((1,3,6,1,4,1,25053,2,11,2,122),_RuckusSZFanId_Type())
ruckusSZFanId.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZFanId.setStatus(_B)
_RuckusSZFanStatus_Type=OctetString
_RuckusSZFanStatus_Object=MibScalar
ruckusSZFanStatus=_RuckusSZFanStatus_Object((1,3,6,1,4,1,25053,2,11,2,123),_RuckusSZFanStatus_Type())
ruckusSZFanStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZFanStatus.setStatus(_B)
_RuckusSZLicenseType_Type=OctetString
_RuckusSZLicenseType_Object=MibScalar
ruckusSZLicenseType=_RuckusSZLicenseType_Object((1,3,6,1,4,1,25053,2,11,2,150),_RuckusSZLicenseType_Type())
ruckusSZLicenseType.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZLicenseType.setStatus(_B)
_RuckusSZLicenseUsagePerc_Type=OctetString
_RuckusSZLicenseUsagePerc_Object=MibScalar
ruckusSZLicenseUsagePerc=_RuckusSZLicenseUsagePerc_Object((1,3,6,1,4,1,25053,2,11,2,151),_RuckusSZLicenseUsagePerc_Type())
ruckusSZLicenseUsagePerc.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZLicenseUsagePerc.setStatus(_B)
_RuckusSZLicenseServerName_Type=OctetString
_RuckusSZLicenseServerName_Object=MibScalar
ruckusSZLicenseServerName=_RuckusSZLicenseServerName_Object((1,3,6,1,4,1,25053,2,11,2,152),_RuckusSZLicenseServerName_Type())
ruckusSZLicenseServerName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZLicenseServerName.setStatus(_B)
_RuckusSZIPSecGWAddress_Type=OctetString
_RuckusSZIPSecGWAddress_Object=MibScalar
ruckusSZIPSecGWAddress=_RuckusSZIPSecGWAddress_Object((1,3,6,1,4,1,25053,2,11,2,153),_RuckusSZIPSecGWAddress_Type())
ruckusSZIPSecGWAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZIPSecGWAddress.setStatus(_B)
_RuckusSZSyslogServerAddress_Type=OctetString
_RuckusSZSyslogServerAddress_Object=MibScalar
ruckusSZSyslogServerAddress=_RuckusSZSyslogServerAddress_Object((1,3,6,1,4,1,25053,2,11,2,154),_RuckusSZSyslogServerAddress_Type())
ruckusSZSyslogServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZSyslogServerAddress.setStatus(_B)
_RuckusSZSrcSyslogServerAddress_Type=OctetString
_RuckusSZSrcSyslogServerAddress_Object=MibScalar
ruckusSZSrcSyslogServerAddress=_RuckusSZSrcSyslogServerAddress_Object((1,3,6,1,4,1,25053,2,11,2,155),_RuckusSZSrcSyslogServerAddress_Type())
ruckusSZSrcSyslogServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZSrcSyslogServerAddress.setStatus(_B)
_RuckusSZDestSyslogServerAddress_Type=OctetString
_RuckusSZDestSyslogServerAddress_Object=MibScalar
ruckusSZDestSyslogServerAddress=_RuckusSZDestSyslogServerAddress_Object((1,3,6,1,4,1,25053,2,11,2,156),_RuckusSZDestSyslogServerAddress_Type())
ruckusSZDestSyslogServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDestSyslogServerAddress.setStatus(_B)
_RuckusSZFtpIp_Type=OctetString
_RuckusSZFtpIp_Object=MibScalar
ruckusSZFtpIp=_RuckusSZFtpIp_Object((1,3,6,1,4,1,25053,2,11,2,200),_RuckusSZFtpIp_Type())
ruckusSZFtpIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZFtpIp.setStatus(_B)
_RuckusSZFtpPort_Type=OctetString
_RuckusSZFtpPort_Object=MibScalar
ruckusSZFtpPort=_RuckusSZFtpPort_Object((1,3,6,1,4,1,25053,2,11,2,201),_RuckusSZFtpPort_Type())
ruckusSZFtpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZFtpPort.setStatus(_B)
_RuckusSZSrcProcess_Type=OctetString
_RuckusSZSrcProcess_Object=MibScalar
ruckusSZSrcProcess=_RuckusSZSrcProcess_Object((1,3,6,1,4,1,25053,2,11,2,301),_RuckusSZSrcProcess_Type())
ruckusSZSrcProcess.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZSrcProcess.setStatus(_B)
_RuckusSZUEImsi_Type=OctetString
_RuckusSZUEImsi_Object=MibScalar
ruckusSZUEImsi=_RuckusSZUEImsi_Object((1,3,6,1,4,1,25053,2,11,2,305),_RuckusSZUEImsi_Type())
ruckusSZUEImsi.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZUEImsi.setStatus(_B)
_RuckusSZUEMsisdn_Type=OctetString
_RuckusSZUEMsisdn_Object=MibScalar
ruckusSZUEMsisdn=_RuckusSZUEMsisdn_Object((1,3,6,1,4,1,25053,2,11,2,306),_RuckusSZUEMsisdn_Type())
ruckusSZUEMsisdn.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZUEMsisdn.setStatus(_B)
_RuckusSZAuthSrvrIp_Type=OctetString
_RuckusSZAuthSrvrIp_Object=MibScalar
ruckusSZAuthSrvrIp=_RuckusSZAuthSrvrIp_Object((1,3,6,1,4,1,25053,2,11,2,307),_RuckusSZAuthSrvrIp_Type())
ruckusSZAuthSrvrIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZAuthSrvrIp.setStatus(_B)
_RuckusSZRadProxyIp_Type=OctetString
_RuckusSZRadProxyIp_Object=MibScalar
ruckusSZRadProxyIp=_RuckusSZRadProxyIp_Object((1,3,6,1,4,1,25053,2,11,2,308),_RuckusSZRadProxyIp_Type())
ruckusSZRadProxyIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZRadProxyIp.setStatus(_B)
_RuckusSZAccSrvrIp_Type=OctetString
_RuckusSZAccSrvrIp_Object=MibScalar
ruckusSZAccSrvrIp=_RuckusSZAccSrvrIp_Object((1,3,6,1,4,1,25053,2,11,2,309),_RuckusSZAccSrvrIp_Type())
ruckusSZAccSrvrIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZAccSrvrIp.setStatus(_B)
_RuckusSZRadSrvrIp_Type=OctetString
_RuckusSZRadSrvrIp_Object=MibScalar
ruckusSZRadSrvrIp=_RuckusSZRadSrvrIp_Object((1,3,6,1,4,1,25053,2,11,2,312),_RuckusSZRadSrvrIp_Type())
ruckusSZRadSrvrIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZRadSrvrIp.setStatus(_B)
_RuckusSZUserName_Type=OctetString
_RuckusSZUserName_Object=MibScalar
ruckusSZUserName=_RuckusSZUserName_Object((1,3,6,1,4,1,25053,2,11,2,324),_RuckusSZUserName_Type())
ruckusSZUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZUserName.setStatus(_B)
_RuckusSZFileName_Type=OctetString
_RuckusSZFileName_Object=MibScalar
ruckusSZFileName=_RuckusSZFileName_Object((1,3,6,1,4,1,25053,2,11,2,326),_RuckusSZFileName_Type())
ruckusSZFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZFileName.setStatus(_B)
_RuckusSZLDAPSrvrIp_Type=OctetString
_RuckusSZLDAPSrvrIp_Object=MibScalar
ruckusSZLDAPSrvrIp=_RuckusSZLDAPSrvrIp_Object((1,3,6,1,4,1,25053,2,11,2,327),_RuckusSZLDAPSrvrIp_Type())
ruckusSZLDAPSrvrIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZLDAPSrvrIp.setStatus(_B)
_RuckusSZADSrvrIp_Type=OctetString
_RuckusSZADSrvrIp_Object=MibScalar
ruckusSZADSrvrIp=_RuckusSZADSrvrIp_Object((1,3,6,1,4,1,25053,2,11,2,328),_RuckusSZADSrvrIp_Type())
ruckusSZADSrvrIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZADSrvrIp.setStatus(_B)
_RuckusSZSoftwareName_Type=OctetString
_RuckusSZSoftwareName_Object=MibScalar
ruckusSZSoftwareName=_RuckusSZSoftwareName_Object((1,3,6,1,4,1,25053,2,11,2,329),_RuckusSZSoftwareName_Type())
ruckusSZSoftwareName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZSoftwareName.setStatus(_B)
_RuckusSZDomainName_Type=OctetString
_RuckusSZDomainName_Object=MibScalar
ruckusSZDomainName=_RuckusSZDomainName_Object((1,3,6,1,4,1,25053,2,11,2,330),_RuckusSZDomainName_Type())
ruckusSZDomainName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDomainName.setStatus(_B)
_RuckusSZDNATIp_Type=OctetString
_RuckusSZDNATIp_Object=MibScalar
ruckusSZDNATIp=_RuckusSZDNATIp_Object((1,3,6,1,4,1,25053,2,11,2,331),_RuckusSZDNATIp_Type())
ruckusSZDNATIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZDNATIp.setStatus(_B)
_RuckusSZHDDHealthDegradationStatus_Type=OctetString
_RuckusSZHDDHealthDegradationStatus_Object=MibScalar
ruckusSZHDDHealthDegradationStatus=_RuckusSZHDDHealthDegradationStatus_Object((1,3,6,1,4,1,25053,2,11,2,335),_RuckusSZHDDHealthDegradationStatus_Type())
ruckusSZHDDHealthDegradationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZHDDHealthDegradationStatus.setStatus(_B)
_RuckusSZUECaleaTx_Type=OctetString
_RuckusSZUECaleaTx_Object=MibScalar
ruckusSZUECaleaTx=_RuckusSZUECaleaTx_Object((1,3,6,1,4,1,25053,2,11,2,401),_RuckusSZUECaleaTx_Type())
ruckusSZUECaleaTx.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZUECaleaTx.setStatus(_B)
_RuckusSZUECaleaRx_Type=OctetString
_RuckusSZUECaleaRx_Object=MibScalar
ruckusSZUECaleaRx=_RuckusSZUECaleaRx_Object((1,3,6,1,4,1,25053,2,11,2,402),_RuckusSZUECaleaRx_Type())
ruckusSZUECaleaRx.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZUECaleaRx.setStatus(_B)
_RuckusSZEventRoguePolicyName_Type=OctetString
_RuckusSZEventRoguePolicyName_Object=MibScalar
ruckusSZEventRoguePolicyName=_RuckusSZEventRoguePolicyName_Object((1,3,6,1,4,1,25053,2,11,2,416),_RuckusSZEventRoguePolicyName_Type())
ruckusSZEventRoguePolicyName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventRoguePolicyName.setStatus(_B)
_RuckusSZEventRogueRuleName_Type=OctetString
_RuckusSZEventRogueRuleName_Object=MibScalar
ruckusSZEventRogueRuleName=_RuckusSZEventRogueRuleName_Object((1,3,6,1,4,1,25053,2,11,2,417),_RuckusSZEventRogueRuleName_Type())
ruckusSZEventRogueRuleName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventRogueRuleName.setStatus(_B)
_RuckusSZEventRogueType_Type=OctetString
_RuckusSZEventRogueType_Object=MibScalar
ruckusSZEventRogueType=_RuckusSZEventRogueType_Object((1,3,6,1,4,1,25053,2,11,2,418),_RuckusSZEventRogueType_Type())
ruckusSZEventRogueType.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventRogueType.setStatus(_B)
_RuckusSZEventSwitchGroupLevelOneName_Type=OctetString
_RuckusSZEventSwitchGroupLevelOneName_Object=MibScalar
ruckusSZEventSwitchGroupLevelOneName=_RuckusSZEventSwitchGroupLevelOneName_Object((1,3,6,1,4,1,25053,2,11,2,500),_RuckusSZEventSwitchGroupLevelOneName_Type())
ruckusSZEventSwitchGroupLevelOneName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventSwitchGroupLevelOneName.setStatus(_B)
_RuckusSZEventSwitchGroupLevelTwoName_Type=OctetString
_RuckusSZEventSwitchGroupLevelTwoName_Object=MibScalar
ruckusSZEventSwitchGroupLevelTwoName=_RuckusSZEventSwitchGroupLevelTwoName_Object((1,3,6,1,4,1,25053,2,11,2,501),_RuckusSZEventSwitchGroupLevelTwoName_Type())
ruckusSZEventSwitchGroupLevelTwoName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventSwitchGroupLevelTwoName.setStatus(_B)
_RuckusSZEventSwitchName_Type=OctetString
_RuckusSZEventSwitchName_Object=MibScalar
ruckusSZEventSwitchName=_RuckusSZEventSwitchName_Object((1,3,6,1,4,1,25053,2,11,2,510),_RuckusSZEventSwitchName_Type())
ruckusSZEventSwitchName.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventSwitchName.setStatus(_B)
_RuckusSZEventSwitchMacAddr_Type=OctetString
_RuckusSZEventSwitchMacAddr_Object=MibScalar
ruckusSZEventSwitchMacAddr=_RuckusSZEventSwitchMacAddr_Object((1,3,6,1,4,1,25053,2,11,2,511),_RuckusSZEventSwitchMacAddr_Type())
ruckusSZEventSwitchMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusSZEventSwitchMacAddr.setStatus(_B)
ruckusSZSystemMiscEventTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,1))
ruckusSZSystemMiscEventTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_o)))
if mibBuilder.loadTexts:ruckusSZSystemMiscEventTrap.setStatus(_B)
ruckusSZUpgradeSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,2))
ruckusSZUpgradeSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_P),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ruckusSZUpgradeSuccessTrap.setStatus(_B)
ruckusSZUpgradeFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,3))
ruckusSZUpgradeFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ruckusSZUpgradeFailedTrap.setStatus(_B)
ruckusSZNodeRestartedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,4))
ruckusSZNodeRestartedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZNodeRestartedTrap.setStatus(_B)
ruckusSZNodeShutdownTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,5))
ruckusSZNodeShutdownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZNodeShutdownTrap.setStatus(_B)
ruckusSZCPUUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,6))
ruckusSZCPUUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_u)))
if mibBuilder.loadTexts:ruckusSZCPUUsageThresholdExceededTrap.setStatus(_B)
ruckusSZMemoryUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,7))
ruckusSZMemoryUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_v)))
if mibBuilder.loadTexts:ruckusSZMemoryUsageThresholdExceededTrap.setStatus(_B)
ruckusSZDiskUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,8))
ruckusSZDiskUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_w)))
if mibBuilder.loadTexts:ruckusSZDiskUsageThresholdExceededTrap.setStatus(_B)
ruckusSZLicenseUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,19))
ruckusSZLicenseUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ruckusSZLicenseUsageThresholdExceededTrap.setStatus(_B)
ruckusSZAPMiscEventTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,20))
ruckusSZAPMiscEventTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_o),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPMiscEventTrap.setStatus(_B)
ruckusSZAPConnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,21))
ruckusSZAPConnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPConnectedTrap.setStatus(_B)
ruckusSZAPDeletedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22))
ruckusSZAPDeletedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPDeletedTrap.setStatus(_B)
ruckusSZAPDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,23))
ruckusSZAPDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPDisconnectedTrap.setStatus(_B)
ruckusSZAPLostHeartbeatTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,24))
ruckusSZAPLostHeartbeatTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLostHeartbeatTrap.setStatus(_B)
ruckusSZAPRebootTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,25))
ruckusSZAPRebootTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPRebootTrap.setStatus(_B)
ruckusSZCriticalAPConnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,26))
ruckusSZCriticalAPConnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCriticalAPConnectedTrap.setStatus(_B)
ruckusSZCriticalAPDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,27))
ruckusSZCriticalAPDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCriticalAPDisconnectedTrap.setStatus(_B)
ruckusSZAPRejectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,28))
ruckusSZAPRejectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Y),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPRejectedTrap.setStatus(_B)
ruckusSZAPConfUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,29))
ruckusSZAPConfUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_x),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPConfUpdateFailedTrap.setStatus(_B)
ruckusSZAPConfUpdatedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,30))
ruckusSZAPConfUpdatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_x),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPConfUpdatedTrap.setStatus(_B)
ruckusSZAPSwapOutModelDiffTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,31))
ruckusSZAPSwapOutModelDiffTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_y),(_A,_z),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPSwapOutModelDiffTrap.setStatus(_B)
ruckusSZAPPreProvisionModelDiffTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,32))
ruckusSZAPPreProvisionModelDiffTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_y),(_A,_z),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPPreProvisionModelDiffTrap.setStatus(_B)
ruckusSZAPFirmwareUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,34))
ruckusSZAPFirmwareUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPFirmwareUpdateFailedTrap.setStatus(_B)
ruckusSZAPFirmwareUpdatedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,35))
ruckusSZAPFirmwareUpdatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPFirmwareUpdatedTrap.setStatus(_B)
ruckusSZAPWlanOversubscribedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,36))
ruckusSZAPWlanOversubscribedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ruckusSZAPWlanOversubscribedTrap.setStatus(_B)
ruckusSZAPFactoryResetTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,37))
ruckusSZAPFactoryResetTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPFactoryResetTrap.setStatus(_B)
ruckusSZCableModemDownTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,38))
ruckusSZCableModemDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCableModemDownTrap.setStatus(_B)
ruckusSZCableModemRebootTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,39))
ruckusSZCableModemRebootTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCableModemRebootTrap.setStatus(_B)
ruckusSZAPManagedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,41))
ruckusSZAPManagedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Y)))
if mibBuilder.loadTexts:ruckusSZAPManagedTrap.setStatus(_B)
ruckusSZCPUUsageThresholdBackToNormalTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,42))
ruckusSZCPUUsageThresholdBackToNormalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_u)))
if mibBuilder.loadTexts:ruckusSZCPUUsageThresholdBackToNormalTrap.setStatus(_B)
ruckusSZMemoryUsageThresholdBackToNormalTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,43))
ruckusSZMemoryUsageThresholdBackToNormalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_v)))
if mibBuilder.loadTexts:ruckusSZMemoryUsageThresholdBackToNormalTrap.setStatus(_B)
ruckusSZDiskUsageThresholdBackToNormalTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,44))
ruckusSZDiskUsageThresholdBackToNormalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_w)))
if mibBuilder.loadTexts:ruckusSZDiskUsageThresholdBackToNormalTrap.setStatus(_B)
ruckusSZCableModemUpTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,45))
ruckusSZCableModemUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCableModemUpTrap.setStatus(_B)
ruckusSZAPDiscoverySuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,46))
ruckusSZAPDiscoverySuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Y),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPDiscoverySuccessTrap.setStatus(_B)
ruckusSZCMResetByUserTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,47))
ruckusSZCMResetByUserTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCMResetByUserTrap.setStatus(_B)
ruckusSZCMResetFactoryByUserTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,48))
ruckusSZCMResetFactoryByUserTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZCMResetFactoryByUserTrap.setStatus(_B)
ruckusSZSSIDSpoofingRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,50))
ruckusSZSSIDSpoofingRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_e),(_A,_c),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZSSIDSpoofingRogueAPDetectedTrap.setStatus(_B)
ruckusSZMacSpoofingRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,51))
ruckusSZMacSpoofingRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_e),(_A,_c),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZMacSpoofingRogueAPDetectedTrap.setStatus(_B)
ruckusSZSameNetworkRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,52))
ruckusSZSameNetworkRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_e),(_A,_c),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZSameNetworkRogueAPDetectedTrap.setStatus(_B)
ruckusSZADHocNetworkRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,53))
ruckusSZADHocNetworkRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_e),(_A,_c),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZADHocNetworkRogueAPDetectedTrap.setStatus(_B)
ruckusSZMaliciousRogueAPTimeoutTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,54))
ruckusSZMaliciousRogueAPTimeoutTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_e),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZMaliciousRogueAPTimeoutTrap.setStatus(_B)
ruckusSZAPLBSConnectSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,55))
ruckusSZAPLBSConnectSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLBSConnectSuccessTrap.setStatus(_B)
ruckusSZAPLBSNoResponsesTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,56))
ruckusSZAPLBSNoResponsesTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLBSNoResponsesTrap.setStatus(_B)
ruckusSZAPLBSAuthFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,57))
ruckusSZAPLBSAuthFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLBSAuthFailedTrap.setStatus(_B)
ruckusSZAPLBSConnectFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,58))
ruckusSZAPLBSConnectFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLBSConnectFailedTrap.setStatus(_B)
ruckusSZGeneralRogueAPTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,59))
ruckusSZGeneralRogueAPTrap.setObjects(*((_A,_C),(_A,_E),(_A,_e),(_A,_c),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AE),(_A,_D),(_A,_N),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ruckusSZGeneralRogueAPTrap.setStatus(_B)
ruckusSZAPTunnelBuildFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,60))
ruckusSZAPTunnelBuildFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Z),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPTunnelBuildFailedTrap.setStatus(_B)
ruckusSZAPTunnelBuildSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,61))
ruckusSZAPTunnelBuildSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Z),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPTunnelBuildSuccessTrap.setStatus(_B)
ruckusSZAPTunnelDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,62))
ruckusSZAPTunnelDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_Z),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPTunnelDisconnectedTrap.setStatus(_B)
ruckusSZAPSoftGRETunnelFailoverPtoSTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,65))
ruckusSZAPSoftGRETunnelFailoverPtoSTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_A0),(_A,_A1),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPSoftGRETunnelFailoverPtoSTrap.setStatus(_B)
ruckusSZAPSoftGRETunnelFailoverStoPTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,66))
ruckusSZAPSoftGRETunnelFailoverStoPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_A0),(_A,_A1),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPSoftGRETunnelFailoverStoPTrap.setStatus(_B)
ruckusSZAPSoftGREGatewayNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,67))
ruckusSZAPSoftGREGatewayNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AI),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPSoftGREGatewayNotReachableTrap.setStatus(_B)
ruckusSZAPSoftGREGatewayReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,68))
ruckusSZAPSoftGREGatewayReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AJ)))
if mibBuilder.loadTexts:ruckusSZAPSoftGREGatewayReachableTrap.setStatus(_B)
ruckusSZDPConfUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,70))
ruckusSZDPConfUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_A2)))
if mibBuilder.loadTexts:ruckusSZDPConfUpdateFailedTrap.setStatus(_B)
ruckusSZDPLostHeartbeatTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,71))
ruckusSZDPLostHeartbeatTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPLostHeartbeatTrap.setStatus(_B)
ruckusSZDPDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,72))
ruckusSZDPDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_Y)))
if mibBuilder.loadTexts:ruckusSZDPDisconnectedTrap.setStatus(_B)
ruckusSZDPPhyInterfaceDownTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,73))
ruckusSZDPPhyInterfaceDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_A3)))
if mibBuilder.loadTexts:ruckusSZDPPhyInterfaceDownTrap.setStatus(_B)
ruckusSZDPStatusUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,74))
ruckusSZDPStatusUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPStatusUpdateFailedTrap.setStatus(_B)
ruckusSZDPStatisticUpdateFaliedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,75))
ruckusSZDPStatisticUpdateFaliedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPStatisticUpdateFaliedTrap.setStatus(_B)
ruckusSZDPConnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,76))
ruckusSZDPConnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_Y)))
if mibBuilder.loadTexts:ruckusSZDPConnectedTrap.setStatus(_B)
ruckusSZDPPhyInterfaceUpTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,77))
ruckusSZDPPhyInterfaceUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_A3)))
if mibBuilder.loadTexts:ruckusSZDPPhyInterfaceUpTrap.setStatus(_B)
ruckusSZDPConfUpdatedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,78))
ruckusSZDPConfUpdatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_A2)))
if mibBuilder.loadTexts:ruckusSZDPConfUpdatedTrap.setStatus(_B)
ruckusSZDPTunnelTearDownTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,79))
ruckusSZDPTunnelTearDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZDPTunnelTearDownTrap.setStatus(_B)
ruckusSZDPAcceptTunnelRequestTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,81))
ruckusSZDPAcceptTunnelRequestTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_G)))
if mibBuilder.loadTexts:ruckusSZDPAcceptTunnelRequestTrap.setStatus(_B)
ruckusSZDPRejectTunnelRequestTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,82))
ruckusSZDPRejectTunnelRequestTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZDPRejectTunnelRequestTrap.setStatus(_B)
ruckusSZDPTunnelSetUpTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,85))
ruckusSZDPTunnelSetUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_G)))
if mibBuilder.loadTexts:ruckusSZDPTunnelSetUpTrap.setStatus(_B)
ruckusSZDPDiscoverySuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,86))
ruckusSZDPDiscoverySuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_Y)))
if mibBuilder.loadTexts:ruckusSZDPDiscoverySuccessTrap.setStatus(_B)
ruckusSZDPDiscoveryFailTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,87))
ruckusSZDPDiscoveryFailTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_Y)))
if mibBuilder.loadTexts:ruckusSZDPDiscoveryFailTrap.setStatus(_B)
ruckusSZDPDeletedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,94))
ruckusSZDPDeletedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPDeletedTrap.setStatus(_B)
ruckusSZDPUpgradeStartTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,95))
ruckusSZDPUpgradeStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPUpgradeStartTrap.setStatus(_B)
ruckusSZDPUpgradingTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,96))
ruckusSZDPUpgradingTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPUpgradingTrap.setStatus(_B)
ruckusSZDPUpgradeSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,97))
ruckusSZDPUpgradeSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPUpgradeSuccessTrap.setStatus(_B)
ruckusSZDPUpgradeFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,98))
ruckusSZDPUpgradeFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_R)))
if mibBuilder.loadTexts:ruckusSZDPUpgradeFailedTrap.setStatus(_B)
ruckusSZClientMiscEventTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,100))
ruckusSZClientMiscEventTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_r),(_A,_o)))
if mibBuilder.loadTexts:ruckusSZClientMiscEventTrap.setStatus(_B)
ruckusSZNodeJoinFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,200))
ruckusSZNodeJoinFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZNodeJoinFailedTrap.setStatus(_B)
ruckusSZNodeRemoveFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,201))
ruckusSZNodeRemoveFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZNodeRemoveFailedTrap.setStatus(_B)
ruckusSZNodeOutOfServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,202))
ruckusSZNodeOutOfServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZNodeOutOfServiceTrap.setStatus(_B)
ruckusSZClusterInMaintenanceStateTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,203))
ruckusSZClusterInMaintenanceStateTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterInMaintenanceStateTrap.setStatus(_B)
ruckusSZClusterBackupFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,204))
ruckusSZClusterBackupFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterBackupFailedTrap.setStatus(_B)
ruckusSZClusterRestoreFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,205))
ruckusSZClusterRestoreFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterRestoreFailedTrap.setStatus(_B)
ruckusSZClusterAppStoppedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,206))
ruckusSZClusterAppStoppedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_f),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZClusterAppStoppedTrap.setStatus(_B)
ruckusSZNodeBondInterfaceDownTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,207))
ruckusSZNodeBondInterfaceDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_i),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZNodeBondInterfaceDownTrap.setStatus(_B)
ruckusSZNodePhyInterfaceDownTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,208))
ruckusSZNodePhyInterfaceDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_i),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZNodePhyInterfaceDownTrap.setStatus(_B)
ruckusSZClusterLeaderChangedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,209))
ruckusSZClusterLeaderChangedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterLeaderChangedTrap.setStatus(_B)
ruckusSZClusterUpgradeSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,210))
ruckusSZClusterUpgradeSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ruckusSZClusterUpgradeSuccessTrap.setStatus(_B)
ruckusSZNodeBondInterfaceUpTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,211))
ruckusSZNodeBondInterfaceUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_i),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZNodeBondInterfaceUpTrap.setStatus(_B)
ruckusSZNodePhyInterfaceUpTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,212))
ruckusSZNodePhyInterfaceUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_i),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZNodePhyInterfaceUpTrap.setStatus(_B)
ruckusSZClusterBackToInServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,216))
ruckusSZClusterBackToInServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterBackToInServiceTrap.setStatus(_B)
ruckusSZBackupClusterSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,217))
ruckusSZBackupClusterSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZBackupClusterSuccessTrap.setStatus(_B)
ruckusSZNodeJoinSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,218))
ruckusSZNodeJoinSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZNodeJoinSuccessTrap.setStatus(_B)
ruckusSZClusterAppStartTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,219))
ruckusSZClusterAppStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_f),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZClusterAppStartTrap.setStatus(_B)
ruckusSZNodeRemoveSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,220))
ruckusSZNodeRemoveSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZNodeRemoveSuccessTrap.setStatus(_B)
ruckusSZClusterRestoreSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,221))
ruckusSZClusterRestoreSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterRestoreSuccessTrap.setStatus(_B)
ruckusSZNodeBackToInServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,222))
ruckusSZNodeBackToInServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZNodeBackToInServiceTrap.setStatus(_B)
ruckusSZSshTunnelSwitchedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,223))
ruckusSZSshTunnelSwitchedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_J),(_A,_Q),(_A,_AK)))
if mibBuilder.loadTexts:ruckusSZSshTunnelSwitchedTrap.setStatus(_B)
ruckusSZClusterCfgBackupStartTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,224))
ruckusSZClusterCfgBackupStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterCfgBackupStartTrap.setStatus(_B)
ruckusSZClusterCfgBackupSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,225))
ruckusSZClusterCfgBackupSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterCfgBackupSuccessTrap.setStatus(_B)
ruckusSZClusterCfgBackupFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,226))
ruckusSZClusterCfgBackupFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterCfgBackupFailedTrap.setStatus(_B)
ruckusSZClusterCfgRestoreSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,227))
ruckusSZClusterCfgRestoreSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterCfgRestoreSuccessTrap.setStatus(_B)
ruckusSZClusterCfgRestoreFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,228))
ruckusSZClusterCfgRestoreFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterCfgRestoreFailedTrap.setStatus(_B)
ruckusSZClusterUploadSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,229))
ruckusSZClusterUploadSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterUploadSuccessTrap.setStatus(_B)
ruckusSZClusterUploadFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,230))
ruckusSZClusterUploadFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZClusterUploadFailedTrap.setStatus(_B)
ruckusSZClusterOutOfServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,231))
ruckusSZClusterOutOfServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterOutOfServiceTrap.setStatus(_B)
ruckusSZClusterUploadVDPFirmwareStartTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,232))
ruckusSZClusterUploadVDPFirmwareStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterUploadVDPFirmwareStartTrap.setStatus(_B)
ruckusSZClusterUploadVDPFirmwareSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,233))
ruckusSZClusterUploadVDPFirmwareSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:ruckusSZClusterUploadVDPFirmwareSuccessTrap.setStatus(_B)
ruckusSZClusterUploadVDPFirmwareFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,234))
ruckusSZClusterUploadVDPFirmwareFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Q),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZClusterUploadVDPFirmwareFailedTrap.setStatus(_B)
ruckusSZIpmiTempBBTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,251))
ruckusSZIpmiTempBBTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_j),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiTempBBTrap.setStatus(_B)
ruckusSZIpmiTempPTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,256))
ruckusSZIpmiTempPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_A4),(_A,_j),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiTempPTrap.setStatus(_B)
ruckusSZIpmiFanTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,258))
ruckusSZIpmiFanTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_k),(_A,_l),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiFanTrap.setStatus(_B)
ruckusSZIpmiFanStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,261))
ruckusSZIpmiFanStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_k),(_A,_l),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiFanStatusTrap.setStatus(_B)
ruckusSZIpmiRETempBBTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,265))
ruckusSZIpmiRETempBBTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_j),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiRETempBBTrap.setStatus(_B)
ruckusSZIpmiRETempPTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,270))
ruckusSZIpmiRETempPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_A4),(_A,_j),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiRETempPTrap.setStatus(_B)
ruckusSZIpmiREFanTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,272))
ruckusSZIpmiREFanTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_k),(_A,_l),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiREFanTrap.setStatus(_B)
ruckusSZIpmiREFanStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,275))
ruckusSZIpmiREFanStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_k),(_A,_l),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZIpmiREFanStatusTrap.setStatus(_B)
ruckusSZFtpTransferErrorTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,280))
ruckusSZFtpTransferErrorTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZFtpTransferErrorTrap.setStatus(_B)
ruckusSZSystemLBSConnectSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,290))
ruckusSZSystemLBSConnectSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J),(_A,_P),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ruckusSZSystemLBSConnectSuccessTrap.setStatus(_B)
ruckusSZSystemLBSNoResponseTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,291))
ruckusSZSystemLBSNoResponseTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J),(_A,_P),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ruckusSZSystemLBSNoResponseTrap.setStatus(_B)
ruckusSZSystemLBSAuthFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,292))
ruckusSZSystemLBSAuthFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J),(_A,_P),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ruckusSZSystemLBSAuthFailedTrap.setStatus(_B)
ruckusSZSystemLBSConnectFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,293))
ruckusSZSystemLBSConnectFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J),(_A,_P),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ruckusSZSystemLBSConnectFailedTrap.setStatus(_B)
ruckusSZUnsyncNTPTimeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,294))
ruckusSZUnsyncNTPTimeTrap.setObjects(*((_A,_C),(_A,_E),(_A,_Q),(_A,_S),(_A,_D)))
if mibBuilder.loadTexts:ruckusSZUnsyncNTPTimeTrap.setStatus(_B)
ruckusSZProcessRestartTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,300))
ruckusSZProcessRestartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_f),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZProcessRestartTrap.setStatus(_B)
ruckusSZServiceUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,301))
ruckusSZServiceUnavailableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_f),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZServiceUnavailableTrap.setStatus(_B)
ruckusSZKeepAliveFailureTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,302))
ruckusSZKeepAliveFailureTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_f),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZKeepAliveFailureTrap.setStatus(_B)
ruckusSZResourceUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,304))
ruckusSZResourceUnavailableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_J),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZResourceUnavailableTrap.setStatus(_B)
ruckusSZSmfRegFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,305))
ruckusSZSmfRegFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZSmfRegFailedTrap.setStatus(_B)
ruckusSZHipFailoverTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,306))
ruckusSZHipFailoverTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZHipFailoverTrap.setStatus(_B)
ruckusSZConfUpdFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,307))
ruckusSZConfUpdFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_f),(_A,_J),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZConfUpdFailedTrap.setStatus(_B)
ruckusSZConfRcvFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,308))
ruckusSZConfRcvFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZConfRcvFailedTrap.setStatus(_B)
ruckusSZLostCnxnToDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,309))
ruckusSZLostCnxnToDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Y),(_A,_Z),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZLostCnxnToDbladeTrap.setStatus(_B)
ruckusSZAuthSrvrNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,314))
ruckusSZAuthSrvrNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_s),(_A,_A5),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZAuthSrvrNotReachableTrap.setStatus(_B)
ruckusSZAccSrvrNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,315))
ruckusSZAccSrvrNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_AO),(_A,_A5),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZAccSrvrNotReachableTrap.setStatus(_B)
ruckusSZAuthFailedNonPermanentIDTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,317))
ruckusSZAuthFailedNonPermanentIDTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_g),(_A,_h),(_A,_J),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:ruckusSZAuthFailedNonPermanentIDTrap.setStatus(_B)
ruckusSZAPAcctRespWhileInvalidConfigTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,347))
ruckusSZAPAcctRespWhileInvalidConfigTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_I),(_A,_m),(_A,_J),(_A,_P),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPAcctRespWhileInvalidConfigTrap.setStatus(_B)
ruckusSZAPAcctMsgDropNoAcctStartMsgTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,348))
ruckusSZAPAcctMsgDropNoAcctStartMsgTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_I),(_A,_m),(_A,_J),(_A,_P),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPAcctMsgDropNoAcctStartMsgTrap.setStatus(_B)
ruckusSZUnauthorizedCoaDmMessageDroppedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,349))
ruckusSZUnauthorizedCoaDmMessageDroppedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_d),(_A,_n),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZUnauthorizedCoaDmMessageDroppedTrap.setStatus(_B)
ruckusSZConnectedToDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,350))
ruckusSZConnectedToDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Y),(_A,_Z),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZConnectedToDbladeTrap.setStatus(_B)
ruckusSZSessUpdatedAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,354))
ruckusSZSessUpdatedAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Y),(_A,_Z),(_A,_g),(_A,_h),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZSessUpdatedAtDbladeTrap.setStatus(_B)
ruckusSZSessUpdateErrAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,355))
ruckusSZSessUpdateErrAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Y),(_A,_Z),(_A,_g),(_A,_h),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZSessUpdateErrAtDbladeTrap.setStatus(_B)
ruckusSZSessDeletedAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,356))
ruckusSZSessDeletedAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Y),(_A,_Z),(_A,_g),(_A,_h),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZSessDeletedAtDbladeTrap.setStatus(_B)
ruckusSZSessDeleteErrAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,357))
ruckusSZSessDeleteErrAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_Y),(_A,_Z),(_A,_g),(_A,_h),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ruckusSZSessDeleteErrAtDbladeTrap.setStatus(_B)
ruckusSZLicenseSyncSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,358))
ruckusSZLicenseSyncSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_A6)))
if mibBuilder.loadTexts:ruckusSZLicenseSyncSuccessTrap.setStatus(_B)
ruckusSZLicenseSyncFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,359))
ruckusSZLicenseSyncFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O),(_A,_A6)))
if mibBuilder.loadTexts:ruckusSZLicenseSyncFailedTrap.setStatus(_B)
ruckusSZLicenseImportSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,360))
ruckusSZLicenseImportSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O)))
if mibBuilder.loadTexts:ruckusSZLicenseImportSuccessTrap.setStatus(_B)
ruckusSZLicenseImportFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,361))
ruckusSZLicenseImportFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_O)))
if mibBuilder.loadTexts:ruckusSZLicenseImportFailedTrap.setStatus(_B)
ruckusSZSyslogServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,370))
ruckusSZSyslogServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_A7),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZSyslogServerReachableTrap.setStatus(_B)
ruckusSZSyslogServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,371))
ruckusSZSyslogServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_A7),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZSyslogServerUnreachableTrap.setStatus(_B)
ruckusSZSyslogServerSwitchedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,372))
ruckusSZSyslogServerSwitchedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_AP),(_A,_AQ),(_A,_J)))
if mibBuilder.loadTexts:ruckusSZSyslogServerSwitchedTrap.setStatus(_B)
ruckusSZAPRadiusServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,400))
ruckusSZAPRadiusServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_n),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPRadiusServerReachableTrap.setStatus(_B)
ruckusSZAPRadiusServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,401))
ruckusSZAPRadiusServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_n),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPRadiusServerUnreachableTrap.setStatus(_B)
ruckusSZAPLDAPServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,402))
ruckusSZAPLDAPServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_A8),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLDAPServerReachableTrap.setStatus(_B)
ruckusSZAPLDAPServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,403))
ruckusSZAPLDAPServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_A8),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPLDAPServerUnreachableTrap.setStatus(_B)
ruckusSZAPADServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,404))
ruckusSZAPADServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_A9),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPADServerReachableTrap.setStatus(_B)
ruckusSZAPADServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,405))
ruckusSZAPADServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_A9),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPADServerUnreachableTrap.setStatus(_B)
ruckusSZAPUsbSoftwarePackageDownloadedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,406))
ruckusSZAPUsbSoftwarePackageDownloadedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AA),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPUsbSoftwarePackageDownloadedTrap.setStatus(_B)
ruckusSZAPUsbSoftwarePackageDownloadFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,407))
ruckusSZAPUsbSoftwarePackageDownloadFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AA),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZAPUsbSoftwarePackageDownloadFailedTrap.setStatus(_B)
ruckusSZEspAuthServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,408))
ruckusSZEspAuthServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_s),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspAuthServerReachableTrap.setStatus(_B)
ruckusSZEspAuthServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,409))
ruckusSZEspAuthServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_s),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspAuthServerUnreachableTrap.setStatus(_B)
ruckusSZEspAuthServerResolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,410))
ruckusSZEspAuthServerResolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_T),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspAuthServerResolvableTrap.setStatus(_B)
ruckusSZEspAuthServerUnResolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,411))
ruckusSZEspAuthServerUnResolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_T),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspAuthServerUnResolvableTrap.setStatus(_B)
ruckusSZEspDNATServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,412))
ruckusSZEspDNATServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AB),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspDNATServerReachableTrap.setStatus(_B)
ruckusSZEspDNATServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,413))
ruckusSZEspDNATServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_AB),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspDNATServerUnreachableTrap.setStatus(_B)
ruckusSZEspDNATServerResolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,414))
ruckusSZEspDNATServerResolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_T),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspDNATServerResolvableTrap.setStatus(_B)
ruckusSZEspDNATServerUnresolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,415))
ruckusSZEspDNATServerUnresolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_T),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZEspDNATServerUnresolvableTrap.setStatus(_B)
ruckusSZHDDHealthDegradationTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,416))
ruckusSZHDDHealthDegradationTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_AR),(_A,_O)))
if mibBuilder.loadTexts:ruckusSZHDDHealthDegradationTrap.setStatus(_B)
ruckusRateLimitTORSurpassedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,500))
ruckusRateLimitTORSurpassedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_n)))
if mibBuilder.loadTexts:ruckusRateLimitTORSurpassedTrap.setStatus(_B)
ruckusSZIPSecTunnelAssociatedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,600))
ruckusSZIPSecTunnelAssociatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_t),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZIPSecTunnelAssociatedTrap.setStatus(_B)
ruckusSZIPSecTunnelDisassociatedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,601))
ruckusSZIPSecTunnelDisassociatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_t),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZIPSecTunnelDisassociatedTrap.setStatus(_B)
ruckusSZIPSecTunnelAssociateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,602))
ruckusSZIPSecTunnelAssociateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H),(_A,_G),(_A,_I),(_A,_K),(_A,_L),(_A,_M),(_A,_t),(_A,_N)))
if mibBuilder.loadTexts:ruckusSZIPSecTunnelAssociateFailedTrap.setStatus(_B)
ruckusSZCaleaMirroringStartTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,712))
ruckusSZCaleaMirroringStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_m),(_A,_H),(_A,_G),(_A,_c),(_A,_r)))
if mibBuilder.loadTexts:ruckusSZCaleaMirroringStartTrap.setStatus(_B)
ruckusSZCaleaMirroringStopTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,713))
ruckusSZCaleaMirroringStopTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_m),(_A,_H),(_A,_G),(_A,_c),(_A,_r),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:ruckusSZCaleaMirroringStopTrap.setStatus(_B)
ruckusSZSwitchCriticalMessageTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,20000))
ruckusSZSwitchCriticalMessageTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchCriticalMessageTrap.setStatus(_B)
ruckusSZSwitchAlertMessageTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,20001))
ruckusSZSwitchAlertMessageTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchAlertMessageTrap.setStatus(_B)
ruckusSZSwitchWarningMessageTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,20002))
ruckusSZSwitchWarningMessageTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchWarningMessageTrap.setStatus(_B)
ruckusSZSwitchOfflineTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,21000))
ruckusSZSwitchOfflineTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchOfflineTrap.setStatus(_B)
ruckusSZOverSwitchMaxCapacityTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,21001))
ruckusSZOverSwitchMaxCapacityTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:ruckusSZOverSwitchMaxCapacityTrap.setStatus(_B)
ruckusSZSwitchDuplicatedTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,21002))
ruckusSZSwitchDuplicatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchDuplicatedTrap.setStatus(_B)
ruckusSZSwitchWarningCpuThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22010))
ruckusSZSwitchWarningCpuThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchWarningCpuThresholdExceededTrap.setStatus(_B)
ruckusSZSwitchMajorCpuThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22011))
ruckusSZSwitchMajorCpuThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchMajorCpuThresholdExceededTrap.setStatus(_B)
ruckusSZSwitchCriticalCpuThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22012))
ruckusSZSwitchCriticalCpuThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchCriticalCpuThresholdExceededTrap.setStatus(_B)
ruckusSZSwitchWarningMemoryThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22020))
ruckusSZSwitchWarningMemoryThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchWarningMemoryThresholdExceededTrap.setStatus(_B)
ruckusSZSwitchMajorMemoryThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22021))
ruckusSZSwitchMajorMemoryThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchMajorMemoryThresholdExceededTrap.setStatus(_B)
ruckusSZSwitchCriticalMemoryThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22022))
ruckusSZSwitchCriticalMemoryThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchCriticalMemoryThresholdExceededTrap.setStatus(_B)
ruckusSZSwitchWarningTextPatternTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22030))
ruckusSZSwitchWarningTextPatternTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchWarningTextPatternTrap.setStatus(_B)
ruckusSZSwitchMajorTextPatternTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22031))
ruckusSZSwitchMajorTextPatternTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchMajorTextPatternTrap.setStatus(_B)
ruckusSZSwitchCriticalTextPatternTrap=NotificationType((1,3,6,1,4,1,25053,2,11,1,22032))
ruckusSZSwitchCriticalTextPatternTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ruckusSZSwitchCriticalTextPatternTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ruckusSZEventMIB':ruckusSZEventMIB,'ruckusSZEventTraps':ruckusSZEventTraps,'ruckusSZSystemMiscEventTrap':ruckusSZSystemMiscEventTrap,'ruckusSZUpgradeSuccessTrap':ruckusSZUpgradeSuccessTrap,'ruckusSZUpgradeFailedTrap':ruckusSZUpgradeFailedTrap,'ruckusSZNodeRestartedTrap':ruckusSZNodeRestartedTrap,'ruckusSZNodeShutdownTrap':ruckusSZNodeShutdownTrap,'ruckusSZCPUUsageThresholdExceededTrap':ruckusSZCPUUsageThresholdExceededTrap,'ruckusSZMemoryUsageThresholdExceededTrap':ruckusSZMemoryUsageThresholdExceededTrap,'ruckusSZDiskUsageThresholdExceededTrap':ruckusSZDiskUsageThresholdExceededTrap,'ruckusSZLicenseUsageThresholdExceededTrap':ruckusSZLicenseUsageThresholdExceededTrap,'ruckusSZAPMiscEventTrap':ruckusSZAPMiscEventTrap,'ruckusSZAPConnectedTrap':ruckusSZAPConnectedTrap,'ruckusSZAPDeletedTrap':ruckusSZAPDeletedTrap,'ruckusSZAPDisconnectedTrap':ruckusSZAPDisconnectedTrap,'ruckusSZAPLostHeartbeatTrap':ruckusSZAPLostHeartbeatTrap,'ruckusSZAPRebootTrap':ruckusSZAPRebootTrap,'ruckusSZCriticalAPConnectedTrap':ruckusSZCriticalAPConnectedTrap,'ruckusSZCriticalAPDisconnectedTrap':ruckusSZCriticalAPDisconnectedTrap,'ruckusSZAPRejectedTrap':ruckusSZAPRejectedTrap,'ruckusSZAPConfUpdateFailedTrap':ruckusSZAPConfUpdateFailedTrap,'ruckusSZAPConfUpdatedTrap':ruckusSZAPConfUpdatedTrap,'ruckusSZAPSwapOutModelDiffTrap':ruckusSZAPSwapOutModelDiffTrap,'ruckusSZAPPreProvisionModelDiffTrap':ruckusSZAPPreProvisionModelDiffTrap,'ruckusSZAPFirmwareUpdateFailedTrap':ruckusSZAPFirmwareUpdateFailedTrap,'ruckusSZAPFirmwareUpdatedTrap':ruckusSZAPFirmwareUpdatedTrap,'ruckusSZAPWlanOversubscribedTrap':ruckusSZAPWlanOversubscribedTrap,'ruckusSZAPFactoryResetTrap':ruckusSZAPFactoryResetTrap,'ruckusSZCableModemDownTrap':ruckusSZCableModemDownTrap,'ruckusSZCableModemRebootTrap':ruckusSZCableModemRebootTrap,'ruckusSZAPManagedTrap':ruckusSZAPManagedTrap,'ruckusSZCPUUsageThresholdBackToNormalTrap':ruckusSZCPUUsageThresholdBackToNormalTrap,'ruckusSZMemoryUsageThresholdBackToNormalTrap':ruckusSZMemoryUsageThresholdBackToNormalTrap,'ruckusSZDiskUsageThresholdBackToNormalTrap':ruckusSZDiskUsageThresholdBackToNormalTrap,'ruckusSZCableModemUpTrap':ruckusSZCableModemUpTrap,'ruckusSZAPDiscoverySuccessTrap':ruckusSZAPDiscoverySuccessTrap,'ruckusSZCMResetByUserTrap':ruckusSZCMResetByUserTrap,'ruckusSZCMResetFactoryByUserTrap':ruckusSZCMResetFactoryByUserTrap,'ruckusSZSSIDSpoofingRogueAPDetectedTrap':ruckusSZSSIDSpoofingRogueAPDetectedTrap,'ruckusSZMacSpoofingRogueAPDetectedTrap':ruckusSZMacSpoofingRogueAPDetectedTrap,'ruckusSZSameNetworkRogueAPDetectedTrap':ruckusSZSameNetworkRogueAPDetectedTrap,'ruckusSZADHocNetworkRogueAPDetectedTrap':ruckusSZADHocNetworkRogueAPDetectedTrap,'ruckusSZMaliciousRogueAPTimeoutTrap':ruckusSZMaliciousRogueAPTimeoutTrap,'ruckusSZAPLBSConnectSuccessTrap':ruckusSZAPLBSConnectSuccessTrap,'ruckusSZAPLBSNoResponsesTrap':ruckusSZAPLBSNoResponsesTrap,'ruckusSZAPLBSAuthFailedTrap':ruckusSZAPLBSAuthFailedTrap,'ruckusSZAPLBSConnectFailedTrap':ruckusSZAPLBSConnectFailedTrap,'ruckusSZGeneralRogueAPTrap':ruckusSZGeneralRogueAPTrap,'ruckusSZAPTunnelBuildFailedTrap':ruckusSZAPTunnelBuildFailedTrap,'ruckusSZAPTunnelBuildSuccessTrap':ruckusSZAPTunnelBuildSuccessTrap,'ruckusSZAPTunnelDisconnectedTrap':ruckusSZAPTunnelDisconnectedTrap,'ruckusSZAPSoftGRETunnelFailoverPtoSTrap':ruckusSZAPSoftGRETunnelFailoverPtoSTrap,'ruckusSZAPSoftGRETunnelFailoverStoPTrap':ruckusSZAPSoftGRETunnelFailoverStoPTrap,'ruckusSZAPSoftGREGatewayNotReachableTrap':ruckusSZAPSoftGREGatewayNotReachableTrap,'ruckusSZAPSoftGREGatewayReachableTrap':ruckusSZAPSoftGREGatewayReachableTrap,'ruckusSZDPConfUpdateFailedTrap':ruckusSZDPConfUpdateFailedTrap,'ruckusSZDPLostHeartbeatTrap':ruckusSZDPLostHeartbeatTrap,'ruckusSZDPDisconnectedTrap':ruckusSZDPDisconnectedTrap,'ruckusSZDPPhyInterfaceDownTrap':ruckusSZDPPhyInterfaceDownTrap,'ruckusSZDPStatusUpdateFailedTrap':ruckusSZDPStatusUpdateFailedTrap,'ruckusSZDPStatisticUpdateFaliedTrap':ruckusSZDPStatisticUpdateFaliedTrap,'ruckusSZDPConnectedTrap':ruckusSZDPConnectedTrap,'ruckusSZDPPhyInterfaceUpTrap':ruckusSZDPPhyInterfaceUpTrap,'ruckusSZDPConfUpdatedTrap':ruckusSZDPConfUpdatedTrap,'ruckusSZDPTunnelTearDownTrap':ruckusSZDPTunnelTearDownTrap,'ruckusSZDPAcceptTunnelRequestTrap':ruckusSZDPAcceptTunnelRequestTrap,'ruckusSZDPRejectTunnelRequestTrap':ruckusSZDPRejectTunnelRequestTrap,'ruckusSZDPTunnelSetUpTrap':ruckusSZDPTunnelSetUpTrap,'ruckusSZDPDiscoverySuccessTrap':ruckusSZDPDiscoverySuccessTrap,'ruckusSZDPDiscoveryFailTrap':ruckusSZDPDiscoveryFailTrap,'ruckusSZDPDeletedTrap':ruckusSZDPDeletedTrap,'ruckusSZDPUpgradeStartTrap':ruckusSZDPUpgradeStartTrap,'ruckusSZDPUpgradingTrap':ruckusSZDPUpgradingTrap,'ruckusSZDPUpgradeSuccessTrap':ruckusSZDPUpgradeSuccessTrap,'ruckusSZDPUpgradeFailedTrap':ruckusSZDPUpgradeFailedTrap,'ruckusSZClientMiscEventTrap':ruckusSZClientMiscEventTrap,'ruckusSZNodeJoinFailedTrap':ruckusSZNodeJoinFailedTrap,'ruckusSZNodeRemoveFailedTrap':ruckusSZNodeRemoveFailedTrap,'ruckusSZNodeOutOfServiceTrap':ruckusSZNodeOutOfServiceTrap,'ruckusSZClusterInMaintenanceStateTrap':ruckusSZClusterInMaintenanceStateTrap,'ruckusSZClusterBackupFailedTrap':ruckusSZClusterBackupFailedTrap,'ruckusSZClusterRestoreFailedTrap':ruckusSZClusterRestoreFailedTrap,'ruckusSZClusterAppStoppedTrap':ruckusSZClusterAppStoppedTrap,'ruckusSZNodeBondInterfaceDownTrap':ruckusSZNodeBondInterfaceDownTrap,'ruckusSZNodePhyInterfaceDownTrap':ruckusSZNodePhyInterfaceDownTrap,'ruckusSZClusterLeaderChangedTrap':ruckusSZClusterLeaderChangedTrap,'ruckusSZClusterUpgradeSuccessTrap':ruckusSZClusterUpgradeSuccessTrap,'ruckusSZNodeBondInterfaceUpTrap':ruckusSZNodeBondInterfaceUpTrap,'ruckusSZNodePhyInterfaceUpTrap':ruckusSZNodePhyInterfaceUpTrap,'ruckusSZClusterBackToInServiceTrap':ruckusSZClusterBackToInServiceTrap,'ruckusSZBackupClusterSuccessTrap':ruckusSZBackupClusterSuccessTrap,'ruckusSZNodeJoinSuccessTrap':ruckusSZNodeJoinSuccessTrap,'ruckusSZClusterAppStartTrap':ruckusSZClusterAppStartTrap,'ruckusSZNodeRemoveSuccessTrap':ruckusSZNodeRemoveSuccessTrap,'ruckusSZClusterRestoreSuccessTrap':ruckusSZClusterRestoreSuccessTrap,'ruckusSZNodeBackToInServiceTrap':ruckusSZNodeBackToInServiceTrap,'ruckusSZSshTunnelSwitchedTrap':ruckusSZSshTunnelSwitchedTrap,'ruckusSZClusterCfgBackupStartTrap':ruckusSZClusterCfgBackupStartTrap,'ruckusSZClusterCfgBackupSuccessTrap':ruckusSZClusterCfgBackupSuccessTrap,'ruckusSZClusterCfgBackupFailedTrap':ruckusSZClusterCfgBackupFailedTrap,'ruckusSZClusterCfgRestoreSuccessTrap':ruckusSZClusterCfgRestoreSuccessTrap,'ruckusSZClusterCfgRestoreFailedTrap':ruckusSZClusterCfgRestoreFailedTrap,'ruckusSZClusterUploadSuccessTrap':ruckusSZClusterUploadSuccessTrap,'ruckusSZClusterUploadFailedTrap':ruckusSZClusterUploadFailedTrap,'ruckusSZClusterOutOfServiceTrap':ruckusSZClusterOutOfServiceTrap,'ruckusSZClusterUploadVDPFirmwareStartTrap':ruckusSZClusterUploadVDPFirmwareStartTrap,'ruckusSZClusterUploadVDPFirmwareSuccessTrap':ruckusSZClusterUploadVDPFirmwareSuccessTrap,'ruckusSZClusterUploadVDPFirmwareFailedTrap':ruckusSZClusterUploadVDPFirmwareFailedTrap,'ruckusSZIpmiTempBBTrap':ruckusSZIpmiTempBBTrap,'ruckusSZIpmiTempPTrap':ruckusSZIpmiTempPTrap,'ruckusSZIpmiFanTrap':ruckusSZIpmiFanTrap,'ruckusSZIpmiFanStatusTrap':ruckusSZIpmiFanStatusTrap,'ruckusSZIpmiRETempBBTrap':ruckusSZIpmiRETempBBTrap,'ruckusSZIpmiRETempPTrap':ruckusSZIpmiRETempPTrap,'ruckusSZIpmiREFanTrap':ruckusSZIpmiREFanTrap,'ruckusSZIpmiREFanStatusTrap':ruckusSZIpmiREFanStatusTrap,'ruckusSZFtpTransferErrorTrap':ruckusSZFtpTransferErrorTrap,'ruckusSZSystemLBSConnectSuccessTrap':ruckusSZSystemLBSConnectSuccessTrap,'ruckusSZSystemLBSNoResponseTrap':ruckusSZSystemLBSNoResponseTrap,'ruckusSZSystemLBSAuthFailedTrap':ruckusSZSystemLBSAuthFailedTrap,'ruckusSZSystemLBSConnectFailedTrap':ruckusSZSystemLBSConnectFailedTrap,'ruckusSZUnsyncNTPTimeTrap':ruckusSZUnsyncNTPTimeTrap,'ruckusSZProcessRestartTrap':ruckusSZProcessRestartTrap,'ruckusSZServiceUnavailableTrap':ruckusSZServiceUnavailableTrap,'ruckusSZKeepAliveFailureTrap':ruckusSZKeepAliveFailureTrap,'ruckusSZResourceUnavailableTrap':ruckusSZResourceUnavailableTrap,'ruckusSZSmfRegFailedTrap':ruckusSZSmfRegFailedTrap,'ruckusSZHipFailoverTrap':ruckusSZHipFailoverTrap,'ruckusSZConfUpdFailedTrap':ruckusSZConfUpdFailedTrap,'ruckusSZConfRcvFailedTrap':ruckusSZConfRcvFailedTrap,'ruckusSZLostCnxnToDbladeTrap':ruckusSZLostCnxnToDbladeTrap,'ruckusSZAuthSrvrNotReachableTrap':ruckusSZAuthSrvrNotReachableTrap,'ruckusSZAccSrvrNotReachableTrap':ruckusSZAccSrvrNotReachableTrap,'ruckusSZAuthFailedNonPermanentIDTrap':ruckusSZAuthFailedNonPermanentIDTrap,'ruckusSZAPAcctRespWhileInvalidConfigTrap':ruckusSZAPAcctRespWhileInvalidConfigTrap,'ruckusSZAPAcctMsgDropNoAcctStartMsgTrap':ruckusSZAPAcctMsgDropNoAcctStartMsgTrap,'ruckusSZUnauthorizedCoaDmMessageDroppedTrap':ruckusSZUnauthorizedCoaDmMessageDroppedTrap,'ruckusSZConnectedToDbladeTrap':ruckusSZConnectedToDbladeTrap,'ruckusSZSessUpdatedAtDbladeTrap':ruckusSZSessUpdatedAtDbladeTrap,'ruckusSZSessUpdateErrAtDbladeTrap':ruckusSZSessUpdateErrAtDbladeTrap,'ruckusSZSessDeletedAtDbladeTrap':ruckusSZSessDeletedAtDbladeTrap,'ruckusSZSessDeleteErrAtDbladeTrap':ruckusSZSessDeleteErrAtDbladeTrap,'ruckusSZLicenseSyncSuccessTrap':ruckusSZLicenseSyncSuccessTrap,'ruckusSZLicenseSyncFailedTrap':ruckusSZLicenseSyncFailedTrap,'ruckusSZLicenseImportSuccessTrap':ruckusSZLicenseImportSuccessTrap,'ruckusSZLicenseImportFailedTrap':ruckusSZLicenseImportFailedTrap,'ruckusSZSyslogServerReachableTrap':ruckusSZSyslogServerReachableTrap,'ruckusSZSyslogServerUnreachableTrap':ruckusSZSyslogServerUnreachableTrap,'ruckusSZSyslogServerSwitchedTrap':ruckusSZSyslogServerSwitchedTrap,'ruckusSZAPRadiusServerReachableTrap':ruckusSZAPRadiusServerReachableTrap,'ruckusSZAPRadiusServerUnreachableTrap':ruckusSZAPRadiusServerUnreachableTrap,'ruckusSZAPLDAPServerReachableTrap':ruckusSZAPLDAPServerReachableTrap,'ruckusSZAPLDAPServerUnreachableTrap':ruckusSZAPLDAPServerUnreachableTrap,'ruckusSZAPADServerReachableTrap':ruckusSZAPADServerReachableTrap,'ruckusSZAPADServerUnreachableTrap':ruckusSZAPADServerUnreachableTrap,'ruckusSZAPUsbSoftwarePackageDownloadedTrap':ruckusSZAPUsbSoftwarePackageDownloadedTrap,'ruckusSZAPUsbSoftwarePackageDownloadFailedTrap':ruckusSZAPUsbSoftwarePackageDownloadFailedTrap,'ruckusSZEspAuthServerReachableTrap':ruckusSZEspAuthServerReachableTrap,'ruckusSZEspAuthServerUnreachableTrap':ruckusSZEspAuthServerUnreachableTrap,'ruckusSZEspAuthServerResolvableTrap':ruckusSZEspAuthServerResolvableTrap,'ruckusSZEspAuthServerUnResolvableTrap':ruckusSZEspAuthServerUnResolvableTrap,'ruckusSZEspDNATServerReachableTrap':ruckusSZEspDNATServerReachableTrap,'ruckusSZEspDNATServerUnreachableTrap':ruckusSZEspDNATServerUnreachableTrap,'ruckusSZEspDNATServerResolvableTrap':ruckusSZEspDNATServerResolvableTrap,'ruckusSZEspDNATServerUnresolvableTrap':ruckusSZEspDNATServerUnresolvableTrap,'ruckusSZHDDHealthDegradationTrap':ruckusSZHDDHealthDegradationTrap,'ruckusRateLimitTORSurpassedTrap':ruckusRateLimitTORSurpassedTrap,'ruckusSZIPSecTunnelAssociatedTrap':ruckusSZIPSecTunnelAssociatedTrap,'ruckusSZIPSecTunnelDisassociatedTrap':ruckusSZIPSecTunnelDisassociatedTrap,'ruckusSZIPSecTunnelAssociateFailedTrap':ruckusSZIPSecTunnelAssociateFailedTrap,'ruckusSZCaleaMirroringStartTrap':ruckusSZCaleaMirroringStartTrap,'ruckusSZCaleaMirroringStopTrap':ruckusSZCaleaMirroringStopTrap,'ruckusSZSwitchCriticalMessageTrap':ruckusSZSwitchCriticalMessageTrap,'ruckusSZSwitchAlertMessageTrap':ruckusSZSwitchAlertMessageTrap,'ruckusSZSwitchWarningMessageTrap':ruckusSZSwitchWarningMessageTrap,'ruckusSZSwitchOfflineTrap':ruckusSZSwitchOfflineTrap,'ruckusSZOverSwitchMaxCapacityTrap':ruckusSZOverSwitchMaxCapacityTrap,'ruckusSZSwitchDuplicatedTrap':ruckusSZSwitchDuplicatedTrap,'ruckusSZSwitchWarningCpuThresholdExceededTrap':ruckusSZSwitchWarningCpuThresholdExceededTrap,'ruckusSZSwitchMajorCpuThresholdExceededTrap':ruckusSZSwitchMajorCpuThresholdExceededTrap,'ruckusSZSwitchCriticalCpuThresholdExceededTrap':ruckusSZSwitchCriticalCpuThresholdExceededTrap,'ruckusSZSwitchWarningMemoryThresholdExceededTrap':ruckusSZSwitchWarningMemoryThresholdExceededTrap,'ruckusSZSwitchMajorMemoryThresholdExceededTrap':ruckusSZSwitchMajorMemoryThresholdExceededTrap,'ruckusSZSwitchCriticalMemoryThresholdExceededTrap':ruckusSZSwitchCriticalMemoryThresholdExceededTrap,'ruckusSZSwitchWarningTextPatternTrap':ruckusSZSwitchWarningTextPatternTrap,'ruckusSZSwitchMajorTextPatternTrap':ruckusSZSwitchMajorTextPatternTrap,'ruckusSZSwitchCriticalTextPatternTrap':ruckusSZSwitchCriticalTextPatternTrap,'ruckusSZEventObjects':ruckusSZEventObjects,_o:ruckusSZEventDescription,_Q:ruckusSZClusterName,_D:ruckusSZEventCode,_f:ruckusSZProcessName,_Y:ruckusSZEventCtrlIP,_C:ruckusSZEventSeverity,_E:ruckusSZEventType,_P:ruckusSZEventNodeMgmtIp,_O:ruckusSZEventNodeName,_u:ruckusSZCPUPerc,_v:ruckusSZMemoryPerc,_w:ruckusSZDiskPerc,_J:ruckusSZEventMacAddr,_p:ruckusSZEventFirmwareVersion,_q:ruckusSZEventUpgradedFirmwareVersion,_G:ruckusSZEventAPMacAddr,_S:ruckusSZEventReason,_H:ruckusSZEventAPName,_I:ruckusSZEventAPIP,_K:ruckusSZEventAPLocation,_M:ruckusSZEventAPGPSCoordinates,_L:ruckusSZEventAPDescription,_AE:ruckusSZEventZoneName,_y:ruckusSZAPModel,_z:ruckusSZConfigAPModel,_x:ruckusSZAPConfigID,_N:ruckusSZEventAPIPv6,_a:ruckusSZLBSURL,_b:ruckusSZLBSPort,_c:ruckusSZEventSSID,_AS:ruckusSZEventAuthType,_e:ruckusSZEventRogueMac,_A0:ruckusPrimaryGRE,_A1:ruckusSecondaryGRE,_AI:ruckusSoftGREGatewayList,_AJ:ruckusSZSoftGREGWAddress,_r:ruckusSZEventClientMacAddr,_R:ruckusSZDPKey,_A2:ruckusSZDPConfigID,_Z:ruckusSZDPIP,_A3:ruckusSZNetworkPortID,_i:ruckusSZNetworkInterface,_AK:ruckusSZSwitchStatus,_j:ruckusSZTemperatureStatus,_A4:ruckusSZProcessorId,_k:ruckusSZFanId,_l:ruckusSZFanStatus,_AC:ruckusSZLicenseType,_AD:ruckusSZLicenseUsagePerc,_A6:ruckusSZLicenseServerName,_t:ruckusSZIPSecGWAddress,_A7:ruckusSZSyslogServerAddress,_AP:ruckusSZSrcSyslogServerAddress,_AQ:ruckusSZDestSyslogServerAddress,_AL:ruckusSZFtpIp,_AM:ruckusSZFtpPort,_d:ruckusSZSrcProcess,_g:ruckusSZUEImsi,_h:ruckusSZUEMsisdn,_s:ruckusSZAuthSrvrIp,_A5:ruckusSZRadProxyIp,_AO:ruckusSZAccSrvrIp,_n:ruckusSZRadSrvrIp,_m:ruckusSZUserName,_AN:ruckusSZFileName,_A8:ruckusSZLDAPSrvrIp,_A9:ruckusSZADSrvrIp,_AA:ruckusSZSoftwareName,_T:ruckusSZDomainName,_AB:ruckusSZDNATIp,_AR:ruckusSZHDDHealthDegradationStatus,_AT:ruckusSZUECaleaTx,_AU:ruckusSZUECaleaRx,_AF:ruckusSZEventRoguePolicyName,_AG:ruckusSZEventRogueRuleName,_AH:ruckusSZEventRogueType,_U:ruckusSZEventSwitchGroupLevelOneName,_V:ruckusSZEventSwitchGroupLevelTwoName,_W:ruckusSZEventSwitchName,_X:ruckusSZEventSwitchMacAddr})