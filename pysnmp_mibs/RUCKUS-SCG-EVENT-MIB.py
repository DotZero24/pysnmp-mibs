_Ai='ruckusSCGDestSyslogServerAddress'
_Ah='ruckusSCGSrcSyslogServerAddress'
_Ag='ruckusSCGHlrInstance'
_Af='ruckusSCGOperation'
_Ae='ruckusSCGAccSrvrIp'
_Ad='ruckusSCGFileName'
_Ac='ruckusSCGFtpPort'
_Ab='ruckusSCGFtpIp'
_Aa='ruckusSCGSwitchStatus'
_AZ='ruckusSoftGREGatewayList'
_AY='ruckusSCGEventRogueType'
_AX='ruckusSCGEventRogueRuleName'
_AW='ruckusSCGEventRoguePolicyName'
_AV='ruckusSCGEventTargetZoneName'
_AU='ruckusSCGLicenseUsagePerc'
_AT='ruckusSCGLicenseType'
_AS='ruckusSCGDNATIp'
_AR='ruckusSCGSoftwareName'
_AQ='ruckusSCGADSrvrIp'
_AP='ruckusSCGLDAPSrvrIp'
_AO='ruckusSCGSyslogServerAddress'
_AN='ruckusSCGLicenseServerName'
_AM='ruckusSCGRadProxyIp'
_AL='ruckusSCGApn'
_AK='ruckusSCGGtpcIp'
_AJ='ruckusSCGDrvStatus'
_AI='ruckusSCGDrvId'
_AH='ruckusSCGEventClientMacAddr'
_AG='ruckusSCGNetworkPortID'
_AF='ruckusSCGDPConfigID'
_AE='ruckusSecondaryGRE'
_AD='ruckusPrimaryGRE'
_AC='ruckusSCGConfigAPModel'
_AB='ruckusSCGAPModel'
_AA='ruckusSCGAPConfigID'
_A9='ruckusSCGDiskPerc'
_A8='ruckusSCGMemoryPerc'
_A7='ruckusSCGCPUPerc'
_A6='ruckusSCGLMAIp'
_A5='ruckusSCGIPSecGWAddress'
_A4='ruckusSCGDestPort'
_A3='ruckusSCGDestIP'
_A2='ruckusSCGSrcPort'
_A1='ruckusSCGSrcIP'
_A0='ruckusSCGSSN'
_z='ruckusSCGRoutingContext'
_y='ruckusSCGCgfSrvrIp'
_x='ruckusSCGAuthSrvrIp'
_w='ruckusSCGGgsnIp'
_v='ruckusSCGDPPacketPoolID'
_u='ruckusSCGEventUpgradedFirmwareVersion'
_t='ruckusSCGEventFirmwareVersion'
_s='ruckusSCGEventDescription'
_r='ruckusSCGDomainName'
_q='ruckusSCGUserName'
_p='ruckusSCGFanStatus'
_o='ruckusSCGFanId'
_n='ruckusSCGProcessorId'
_m='ruckusSCGNetworkInterface'
_l='ruckusSCGPointCode'
_k='ruckusSCGSoftGREGWAddress'
_j='ruckusSCGEventSSID'
_i='ruckusSCGRealm'
_h='ruckusSCGPsStatus'
_g='ruckusSCGProcessName'
_f='ruckusSCGEventRogueMac'
_e='ruckusSCGRadSrvrIp'
_d='ruckusSCGPgwIp'
_c='ruckusSCGUEMsisdn'
_b='ruckusSCGPsId'
_a='ruckusSCGLBSPort'
_Z='ruckusSCGLBSURL'
_Y='ruckusSCGDPIP'
_X='ruckusSCGUEImsi'
_W='ruckusSCGEventCtrlIP'
_V='ruckusSCGTemperatureStatus'
_U='ruckusSCGSrcProcess'
_T='ruckusSCGEventReason'
_S='ruckusSCGClusterName'
_R='ruckusSCGEventNodeName'
_Q='ruckusSCGDPKey'
_P='ruckusSCGEventNodeMgmtIp'
_O='ruckusSCGEventZoneName'
_N='ruckusSCGEventAPGPSCoordinates'
_M='ruckusSCGEventAPDescription'
_L='ruckusSCGEventAPLocation'
_K='ruckusSCGEventAPName'
_J='ruckusSCGEventAPIPv6'
_I='ruckusSCGEventAPMacAddr'
_H='ruckusSCGEventAPIP'
_G='accessible-for-notify'
_F='ruckusSCGEventMacAddr'
_E='ruckusSCGEventCode'
_D='ruckusSCGEventType'
_C='ruckusSCGEventSeverity'
_B='current'
_A='RUCKUS-SCG-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusEvents,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusEvents')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ruckusSCGEventMIB=ModuleIdentity((1,3,6,1,4,1,25053,2,10))
_RuckusSCGEventTraps_ObjectIdentity=ObjectIdentity
ruckusSCGEventTraps=_RuckusSCGEventTraps_ObjectIdentity((1,3,6,1,4,1,25053,2,10,1))
_RuckusSCGEventObjects_ObjectIdentity=ObjectIdentity
ruckusSCGEventObjects=_RuckusSCGEventObjects_ObjectIdentity((1,3,6,1,4,1,25053,2,10,2))
_RuckusSCGEventDescription_Type=OctetString
_RuckusSCGEventDescription_Object=MibScalar
ruckusSCGEventDescription=_RuckusSCGEventDescription_Object((1,3,6,1,4,1,25053,2,10,2,1),_RuckusSCGEventDescription_Type())
ruckusSCGEventDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventDescription.setStatus(_B)
_RuckusSCGClusterName_Type=OctetString
_RuckusSCGClusterName_Object=MibScalar
ruckusSCGClusterName=_RuckusSCGClusterName_Object((1,3,6,1,4,1,25053,2,10,2,2),_RuckusSCGClusterName_Type())
ruckusSCGClusterName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGClusterName.setStatus(_B)
_RuckusSCGEventCode_Type=OctetString
_RuckusSCGEventCode_Object=MibScalar
ruckusSCGEventCode=_RuckusSCGEventCode_Object((1,3,6,1,4,1,25053,2,10,2,10),_RuckusSCGEventCode_Type())
ruckusSCGEventCode.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventCode.setStatus(_B)
_RuckusSCGProcessName_Type=OctetString
_RuckusSCGProcessName_Object=MibScalar
ruckusSCGProcessName=_RuckusSCGProcessName_Object((1,3,6,1,4,1,25053,2,10,2,11),_RuckusSCGProcessName_Type())
ruckusSCGProcessName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGProcessName.setStatus(_B)
_RuckusSCGEventCtrlIP_Type=OctetString
_RuckusSCGEventCtrlIP_Object=MibScalar
ruckusSCGEventCtrlIP=_RuckusSCGEventCtrlIP_Object((1,3,6,1,4,1,25053,2,10,2,12),_RuckusSCGEventCtrlIP_Type())
ruckusSCGEventCtrlIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventCtrlIP.setStatus(_B)
_RuckusSCGEventSeverity_Type=OctetString
_RuckusSCGEventSeverity_Object=MibScalar
ruckusSCGEventSeverity=_RuckusSCGEventSeverity_Object((1,3,6,1,4,1,25053,2,10,2,13),_RuckusSCGEventSeverity_Type())
ruckusSCGEventSeverity.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventSeverity.setStatus(_B)
_RuckusSCGEventType_Type=OctetString
_RuckusSCGEventType_Object=MibScalar
ruckusSCGEventType=_RuckusSCGEventType_Object((1,3,6,1,4,1,25053,2,10,2,14),_RuckusSCGEventType_Type())
ruckusSCGEventType.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventType.setStatus(_B)
_RuckusSCGEventNodeMgmtIp_Type=OctetString
_RuckusSCGEventNodeMgmtIp_Object=MibScalar
ruckusSCGEventNodeMgmtIp=_RuckusSCGEventNodeMgmtIp_Object((1,3,6,1,4,1,25053,2,10,2,15),_RuckusSCGEventNodeMgmtIp_Type())
ruckusSCGEventNodeMgmtIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventNodeMgmtIp.setStatus(_B)
_RuckusSCGEventNodeName_Type=OctetString
_RuckusSCGEventNodeName_Object=MibScalar
ruckusSCGEventNodeName=_RuckusSCGEventNodeName_Object((1,3,6,1,4,1,25053,2,10,2,16),_RuckusSCGEventNodeName_Type())
ruckusSCGEventNodeName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventNodeName.setStatus(_B)
_RuckusSCGCPUPerc_Type=OctetString
_RuckusSCGCPUPerc_Object=MibScalar
ruckusSCGCPUPerc=_RuckusSCGCPUPerc_Object((1,3,6,1,4,1,25053,2,10,2,17),_RuckusSCGCPUPerc_Type())
ruckusSCGCPUPerc.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGCPUPerc.setStatus(_B)
_RuckusSCGMemoryPerc_Type=OctetString
_RuckusSCGMemoryPerc_Object=MibScalar
ruckusSCGMemoryPerc=_RuckusSCGMemoryPerc_Object((1,3,6,1,4,1,25053,2,10,2,18),_RuckusSCGMemoryPerc_Type())
ruckusSCGMemoryPerc.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGMemoryPerc.setStatus(_B)
_RuckusSCGDiskPerc_Type=OctetString
_RuckusSCGDiskPerc_Object=MibScalar
ruckusSCGDiskPerc=_RuckusSCGDiskPerc_Object((1,3,6,1,4,1,25053,2,10,2,19),_RuckusSCGDiskPerc_Type())
ruckusSCGDiskPerc.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDiskPerc.setStatus(_B)
_RuckusSCGEventMacAddr_Type=OctetString
_RuckusSCGEventMacAddr_Object=MibScalar
ruckusSCGEventMacAddr=_RuckusSCGEventMacAddr_Object((1,3,6,1,4,1,25053,2,10,2,20),_RuckusSCGEventMacAddr_Type())
ruckusSCGEventMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventMacAddr.setStatus(_B)
_RuckusSCGEventFirmwareVersion_Type=OctetString
_RuckusSCGEventFirmwareVersion_Object=MibScalar
ruckusSCGEventFirmwareVersion=_RuckusSCGEventFirmwareVersion_Object((1,3,6,1,4,1,25053,2,10,2,21),_RuckusSCGEventFirmwareVersion_Type())
ruckusSCGEventFirmwareVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventFirmwareVersion.setStatus(_B)
_RuckusSCGEventUpgradedFirmwareVersion_Type=OctetString
_RuckusSCGEventUpgradedFirmwareVersion_Object=MibScalar
ruckusSCGEventUpgradedFirmwareVersion=_RuckusSCGEventUpgradedFirmwareVersion_Object((1,3,6,1,4,1,25053,2,10,2,22),_RuckusSCGEventUpgradedFirmwareVersion_Type())
ruckusSCGEventUpgradedFirmwareVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventUpgradedFirmwareVersion.setStatus(_B)
_RuckusSCGEventAPMacAddr_Type=OctetString
_RuckusSCGEventAPMacAddr_Object=MibScalar
ruckusSCGEventAPMacAddr=_RuckusSCGEventAPMacAddr_Object((1,3,6,1,4,1,25053,2,10,2,23),_RuckusSCGEventAPMacAddr_Type())
ruckusSCGEventAPMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPMacAddr.setStatus(_B)
_RuckusSCGEventReason_Type=OctetString
_RuckusSCGEventReason_Object=MibScalar
ruckusSCGEventReason=_RuckusSCGEventReason_Object((1,3,6,1,4,1,25053,2,10,2,24),_RuckusSCGEventReason_Type())
ruckusSCGEventReason.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventReason.setStatus(_B)
_RuckusSCGEventAPName_Type=OctetString
_RuckusSCGEventAPName_Object=MibScalar
ruckusSCGEventAPName=_RuckusSCGEventAPName_Object((1,3,6,1,4,1,25053,2,10,2,25),_RuckusSCGEventAPName_Type())
ruckusSCGEventAPName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPName.setStatus(_B)
_RuckusSCGEventAPIP_Type=OctetString
_RuckusSCGEventAPIP_Object=MibScalar
ruckusSCGEventAPIP=_RuckusSCGEventAPIP_Object((1,3,6,1,4,1,25053,2,10,2,26),_RuckusSCGEventAPIP_Type())
ruckusSCGEventAPIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPIP.setStatus(_B)
_RuckusSCGEventAPLocation_Type=OctetString
_RuckusSCGEventAPLocation_Object=MibScalar
ruckusSCGEventAPLocation=_RuckusSCGEventAPLocation_Object((1,3,6,1,4,1,25053,2,10,2,27),_RuckusSCGEventAPLocation_Type())
ruckusSCGEventAPLocation.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPLocation.setStatus(_B)
_RuckusSCGEventAPGPSCoordinates_Type=OctetString
_RuckusSCGEventAPGPSCoordinates_Object=MibScalar
ruckusSCGEventAPGPSCoordinates=_RuckusSCGEventAPGPSCoordinates_Object((1,3,6,1,4,1,25053,2,10,2,28),_RuckusSCGEventAPGPSCoordinates_Type())
ruckusSCGEventAPGPSCoordinates.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPGPSCoordinates.setStatus(_B)
_RuckusSCGEventAPDescription_Type=OctetString
_RuckusSCGEventAPDescription_Object=MibScalar
ruckusSCGEventAPDescription=_RuckusSCGEventAPDescription_Object((1,3,6,1,4,1,25053,2,10,2,29),_RuckusSCGEventAPDescription_Type())
ruckusSCGEventAPDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPDescription.setStatus(_B)
_RuckusSCGEventZoneName_Type=OctetString
_RuckusSCGEventZoneName_Object=MibScalar
ruckusSCGEventZoneName=_RuckusSCGEventZoneName_Object((1,3,6,1,4,1,25053,2,10,2,30),_RuckusSCGEventZoneName_Type())
ruckusSCGEventZoneName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventZoneName.setStatus(_B)
_RuckusSCGAPModel_Type=OctetString
_RuckusSCGAPModel_Object=MibScalar
ruckusSCGAPModel=_RuckusSCGAPModel_Object((1,3,6,1,4,1,25053,2,10,2,31),_RuckusSCGAPModel_Type())
ruckusSCGAPModel.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGAPModel.setStatus(_B)
_RuckusSCGConfigAPModel_Type=OctetString
_RuckusSCGConfigAPModel_Object=MibScalar
ruckusSCGConfigAPModel=_RuckusSCGConfigAPModel_Object((1,3,6,1,4,1,25053,2,10,2,32),_RuckusSCGConfigAPModel_Type())
ruckusSCGConfigAPModel.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGConfigAPModel.setStatus(_B)
_RuckusSCGAPConfigID_Type=OctetString
_RuckusSCGAPConfigID_Object=MibScalar
ruckusSCGAPConfigID=_RuckusSCGAPConfigID_Object((1,3,6,1,4,1,25053,2,10,2,33),_RuckusSCGAPConfigID_Type())
ruckusSCGAPConfigID.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGAPConfigID.setStatus(_B)
_RuckusSCGEventTargetZoneName_Type=OctetString
_RuckusSCGEventTargetZoneName_Object=MibScalar
ruckusSCGEventTargetZoneName=_RuckusSCGEventTargetZoneName_Object((1,3,6,1,4,1,25053,2,10,2,34),_RuckusSCGEventTargetZoneName_Type())
ruckusSCGEventTargetZoneName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventTargetZoneName.setStatus(_B)
_RuckusSCGEventAPIPv6_Type=OctetString
_RuckusSCGEventAPIPv6_Object=MibScalar
ruckusSCGEventAPIPv6=_RuckusSCGEventAPIPv6_Object((1,3,6,1,4,1,25053,2,10,2,35),_RuckusSCGEventAPIPv6_Type())
ruckusSCGEventAPIPv6.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventAPIPv6.setStatus(_B)
_RuckusSCGLBSURL_Type=OctetString
_RuckusSCGLBSURL_Object=MibScalar
ruckusSCGLBSURL=_RuckusSCGLBSURL_Object((1,3,6,1,4,1,25053,2,10,2,38),_RuckusSCGLBSURL_Type())
ruckusSCGLBSURL.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLBSURL.setStatus(_B)
_RuckusSCGLBSPort_Type=OctetString
_RuckusSCGLBSPort_Object=MibScalar
ruckusSCGLBSPort=_RuckusSCGLBSPort_Object((1,3,6,1,4,1,25053,2,10,2,39),_RuckusSCGLBSPort_Type())
ruckusSCGLBSPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLBSPort.setStatus(_B)
_RuckusSCGEventSSID_Type=OctetString
_RuckusSCGEventSSID_Object=MibScalar
ruckusSCGEventSSID=_RuckusSCGEventSSID_Object((1,3,6,1,4,1,25053,2,10,2,40),_RuckusSCGEventSSID_Type())
ruckusSCGEventSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventSSID.setStatus(_B)
_RuckusSCGEventRogueMac_Type=OctetString
_RuckusSCGEventRogueMac_Object=MibScalar
ruckusSCGEventRogueMac=_RuckusSCGEventRogueMac_Object((1,3,6,1,4,1,25053,2,10,2,45),_RuckusSCGEventRogueMac_Type())
ruckusSCGEventRogueMac.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventRogueMac.setStatus(_B)
_RuckusPrimaryGRE_Type=OctetString
_RuckusPrimaryGRE_Object=MibScalar
ruckusPrimaryGRE=_RuckusPrimaryGRE_Object((1,3,6,1,4,1,25053,2,10,2,46),_RuckusPrimaryGRE_Type())
ruckusPrimaryGRE.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusPrimaryGRE.setStatus(_B)
_RuckusSecondaryGRE_Type=OctetString
_RuckusSecondaryGRE_Object=MibScalar
ruckusSecondaryGRE=_RuckusSecondaryGRE_Object((1,3,6,1,4,1,25053,2,10,2,47),_RuckusSecondaryGRE_Type())
ruckusSecondaryGRE.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSecondaryGRE.setStatus(_B)
_RuckusSoftGREGatewayList_Type=OctetString
_RuckusSoftGREGatewayList_Object=MibScalar
ruckusSoftGREGatewayList=_RuckusSoftGREGatewayList_Object((1,3,6,1,4,1,25053,2,10,2,48),_RuckusSoftGREGatewayList_Type())
ruckusSoftGREGatewayList.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSoftGREGatewayList.setStatus(_B)
_RuckusSCGSoftGREGWAddress_Type=OctetString
_RuckusSCGSoftGREGWAddress_Object=MibScalar
ruckusSCGSoftGREGWAddress=_RuckusSCGSoftGREGWAddress_Object((1,3,6,1,4,1,25053,2,10,2,49),_RuckusSCGSoftGREGWAddress_Type())
ruckusSCGSoftGREGWAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSoftGREGWAddress.setStatus(_B)
_RuckusSCGEventClientMacAddr_Type=OctetString
_RuckusSCGEventClientMacAddr_Object=MibScalar
ruckusSCGEventClientMacAddr=_RuckusSCGEventClientMacAddr_Object((1,3,6,1,4,1,25053,2,10,2,50),_RuckusSCGEventClientMacAddr_Type())
ruckusSCGEventClientMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventClientMacAddr.setStatus(_B)
_RuckusSCGDPKey_Type=OctetString
_RuckusSCGDPKey_Object=MibScalar
ruckusSCGDPKey=_RuckusSCGDPKey_Object((1,3,6,1,4,1,25053,2,10,2,80),_RuckusSCGDPKey_Type())
ruckusSCGDPKey.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDPKey.setStatus(_B)
_RuckusSCGDPConfigID_Type=OctetString
_RuckusSCGDPConfigID_Object=MibScalar
ruckusSCGDPConfigID=_RuckusSCGDPConfigID_Object((1,3,6,1,4,1,25053,2,10,2,81),_RuckusSCGDPConfigID_Type())
ruckusSCGDPConfigID.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDPConfigID.setStatus(_B)
_RuckusSCGDPIP_Type=OctetString
_RuckusSCGDPIP_Object=MibScalar
ruckusSCGDPIP=_RuckusSCGDPIP_Object((1,3,6,1,4,1,25053,2,10,2,82),_RuckusSCGDPIP_Type())
ruckusSCGDPIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDPIP.setStatus(_B)
_RuckusSCGDPPacketPoolID_Type=OctetString
_RuckusSCGDPPacketPoolID_Object=MibScalar
ruckusSCGDPPacketPoolID=_RuckusSCGDPPacketPoolID_Object((1,3,6,1,4,1,25053,2,10,2,83),_RuckusSCGDPPacketPoolID_Type())
ruckusSCGDPPacketPoolID.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDPPacketPoolID.setStatus(_B)
_RuckusSCGNetworkPortID_Type=OctetString
_RuckusSCGNetworkPortID_Object=MibScalar
ruckusSCGNetworkPortID=_RuckusSCGNetworkPortID_Object((1,3,6,1,4,1,25053,2,10,2,100),_RuckusSCGNetworkPortID_Type())
ruckusSCGNetworkPortID.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGNetworkPortID.setStatus(_B)
_RuckusSCGNetworkInterface_Type=OctetString
_RuckusSCGNetworkInterface_Object=MibScalar
ruckusSCGNetworkInterface=_RuckusSCGNetworkInterface_Object((1,3,6,1,4,1,25053,2,10,2,101),_RuckusSCGNetworkInterface_Type())
ruckusSCGNetworkInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGNetworkInterface.setStatus(_B)
_RuckusSCGSwitchStatus_Type=OctetString
_RuckusSCGSwitchStatus_Object=MibScalar
ruckusSCGSwitchStatus=_RuckusSCGSwitchStatus_Object((1,3,6,1,4,1,25053,2,10,2,102),_RuckusSCGSwitchStatus_Type())
ruckusSCGSwitchStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSwitchStatus.setStatus(_B)
_RuckusSCGTemperatureStatus_Type=OctetString
_RuckusSCGTemperatureStatus_Object=MibScalar
ruckusSCGTemperatureStatus=_RuckusSCGTemperatureStatus_Object((1,3,6,1,4,1,25053,2,10,2,120),_RuckusSCGTemperatureStatus_Type())
ruckusSCGTemperatureStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGTemperatureStatus.setStatus(_B)
_RuckusSCGProcessorId_Type=OctetString
_RuckusSCGProcessorId_Object=MibScalar
ruckusSCGProcessorId=_RuckusSCGProcessorId_Object((1,3,6,1,4,1,25053,2,10,2,121),_RuckusSCGProcessorId_Type())
ruckusSCGProcessorId.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGProcessorId.setStatus(_B)
_RuckusSCGFanId_Type=OctetString
_RuckusSCGFanId_Object=MibScalar
ruckusSCGFanId=_RuckusSCGFanId_Object((1,3,6,1,4,1,25053,2,10,2,122),_RuckusSCGFanId_Type())
ruckusSCGFanId.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGFanId.setStatus(_B)
_RuckusSCGFanStatus_Type=OctetString
_RuckusSCGFanStatus_Object=MibScalar
ruckusSCGFanStatus=_RuckusSCGFanStatus_Object((1,3,6,1,4,1,25053,2,10,2,123),_RuckusSCGFanStatus_Type())
ruckusSCGFanStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGFanStatus.setStatus(_B)
_RuckusSCGPsId_Type=OctetString
_RuckusSCGPsId_Object=MibScalar
ruckusSCGPsId=_RuckusSCGPsId_Object((1,3,6,1,4,1,25053,2,10,2,124),_RuckusSCGPsId_Type())
ruckusSCGPsId.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGPsId.setStatus(_B)
_RuckusSCGPsStatus_Type=OctetString
_RuckusSCGPsStatus_Object=MibScalar
ruckusSCGPsStatus=_RuckusSCGPsStatus_Object((1,3,6,1,4,1,25053,2,10,2,125),_RuckusSCGPsStatus_Type())
ruckusSCGPsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGPsStatus.setStatus(_B)
_RuckusSCGDrvId_Type=OctetString
_RuckusSCGDrvId_Object=MibScalar
ruckusSCGDrvId=_RuckusSCGDrvId_Object((1,3,6,1,4,1,25053,2,10,2,126),_RuckusSCGDrvId_Type())
ruckusSCGDrvId.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDrvId.setStatus(_B)
_RuckusSCGDrvStatus_Type=OctetString
_RuckusSCGDrvStatus_Object=MibScalar
ruckusSCGDrvStatus=_RuckusSCGDrvStatus_Object((1,3,6,1,4,1,25053,2,10,2,127),_RuckusSCGDrvStatus_Type())
ruckusSCGDrvStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDrvStatus.setStatus(_B)
_RuckusSCGLicenseType_Type=OctetString
_RuckusSCGLicenseType_Object=MibScalar
ruckusSCGLicenseType=_RuckusSCGLicenseType_Object((1,3,6,1,4,1,25053,2,10,2,150),_RuckusSCGLicenseType_Type())
ruckusSCGLicenseType.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLicenseType.setStatus(_B)
_RuckusSCGLicenseUsagePerc_Type=OctetString
_RuckusSCGLicenseUsagePerc_Object=MibScalar
ruckusSCGLicenseUsagePerc=_RuckusSCGLicenseUsagePerc_Object((1,3,6,1,4,1,25053,2,10,2,151),_RuckusSCGLicenseUsagePerc_Type())
ruckusSCGLicenseUsagePerc.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLicenseUsagePerc.setStatus(_B)
_RuckusSCGLicenseServerName_Type=OctetString
_RuckusSCGLicenseServerName_Object=MibScalar
ruckusSCGLicenseServerName=_RuckusSCGLicenseServerName_Object((1,3,6,1,4,1,25053,2,10,2,152),_RuckusSCGLicenseServerName_Type())
ruckusSCGLicenseServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLicenseServerName.setStatus(_B)
_RuckusSCGIPSecGWAddress_Type=OctetString
_RuckusSCGIPSecGWAddress_Object=MibScalar
ruckusSCGIPSecGWAddress=_RuckusSCGIPSecGWAddress_Object((1,3,6,1,4,1,25053,2,10,2,153),_RuckusSCGIPSecGWAddress_Type())
ruckusSCGIPSecGWAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGIPSecGWAddress.setStatus(_B)
_RuckusSCGSyslogServerAddress_Type=OctetString
_RuckusSCGSyslogServerAddress_Object=MibScalar
ruckusSCGSyslogServerAddress=_RuckusSCGSyslogServerAddress_Object((1,3,6,1,4,1,25053,2,10,2,154),_RuckusSCGSyslogServerAddress_Type())
ruckusSCGSyslogServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSyslogServerAddress.setStatus(_B)
_RuckusSCGSrcSyslogServerAddress_Type=OctetString
_RuckusSCGSrcSyslogServerAddress_Object=MibScalar
ruckusSCGSrcSyslogServerAddress=_RuckusSCGSrcSyslogServerAddress_Object((1,3,6,1,4,1,25053,2,10,2,155),_RuckusSCGSrcSyslogServerAddress_Type())
ruckusSCGSrcSyslogServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSrcSyslogServerAddress.setStatus(_B)
_RuckusSCGDestSyslogServerAddress_Type=OctetString
_RuckusSCGDestSyslogServerAddress_Object=MibScalar
ruckusSCGDestSyslogServerAddress=_RuckusSCGDestSyslogServerAddress_Object((1,3,6,1,4,1,25053,2,10,2,156),_RuckusSCGDestSyslogServerAddress_Type())
ruckusSCGDestSyslogServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDestSyslogServerAddress.setStatus(_B)
_RuckusSCGFtpIp_Type=OctetString
_RuckusSCGFtpIp_Object=MibScalar
ruckusSCGFtpIp=_RuckusSCGFtpIp_Object((1,3,6,1,4,1,25053,2,10,2,200),_RuckusSCGFtpIp_Type())
ruckusSCGFtpIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGFtpIp.setStatus(_B)
_RuckusSCGFtpPort_Type=OctetString
_RuckusSCGFtpPort_Object=MibScalar
ruckusSCGFtpPort=_RuckusSCGFtpPort_Object((1,3,6,1,4,1,25053,2,10,2,201),_RuckusSCGFtpPort_Type())
ruckusSCGFtpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGFtpPort.setStatus(_B)
_RuckusSCGSrcProcess_Type=OctetString
_RuckusSCGSrcProcess_Object=MibScalar
ruckusSCGSrcProcess=_RuckusSCGSrcProcess_Object((1,3,6,1,4,1,25053,2,10,2,301),_RuckusSCGSrcProcess_Type())
ruckusSCGSrcProcess.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSrcProcess.setStatus(_B)
_RuckusSCGGgsnIp_Type=OctetString
_RuckusSCGGgsnIp_Object=MibScalar
ruckusSCGGgsnIp=_RuckusSCGGgsnIp_Object((1,3,6,1,4,1,25053,2,10,2,302),_RuckusSCGGgsnIp_Type())
ruckusSCGGgsnIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGGgsnIp.setStatus(_B)
_RuckusSCGGtpcIp_Type=OctetString
_RuckusSCGGtpcIp_Object=MibScalar
ruckusSCGGtpcIp=_RuckusSCGGtpcIp_Object((1,3,6,1,4,1,25053,2,10,2,303),_RuckusSCGGtpcIp_Type())
ruckusSCGGtpcIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGGtpcIp.setStatus(_B)
_RuckusSCGApn_Type=OctetString
_RuckusSCGApn_Object=MibScalar
ruckusSCGApn=_RuckusSCGApn_Object((1,3,6,1,4,1,25053,2,10,2,304),_RuckusSCGApn_Type())
ruckusSCGApn.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGApn.setStatus(_B)
_RuckusSCGUEImsi_Type=OctetString
_RuckusSCGUEImsi_Object=MibScalar
ruckusSCGUEImsi=_RuckusSCGUEImsi_Object((1,3,6,1,4,1,25053,2,10,2,305),_RuckusSCGUEImsi_Type())
ruckusSCGUEImsi.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGUEImsi.setStatus(_B)
_RuckusSCGUEMsisdn_Type=OctetString
_RuckusSCGUEMsisdn_Object=MibScalar
ruckusSCGUEMsisdn=_RuckusSCGUEMsisdn_Object((1,3,6,1,4,1,25053,2,10,2,306),_RuckusSCGUEMsisdn_Type())
ruckusSCGUEMsisdn.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGUEMsisdn.setStatus(_B)
_RuckusSCGAuthSrvrIp_Type=OctetString
_RuckusSCGAuthSrvrIp_Object=MibScalar
ruckusSCGAuthSrvrIp=_RuckusSCGAuthSrvrIp_Object((1,3,6,1,4,1,25053,2,10,2,307),_RuckusSCGAuthSrvrIp_Type())
ruckusSCGAuthSrvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGAuthSrvrIp.setStatus(_B)
_RuckusSCGRadProxyIp_Type=OctetString
_RuckusSCGRadProxyIp_Object=MibScalar
ruckusSCGRadProxyIp=_RuckusSCGRadProxyIp_Object((1,3,6,1,4,1,25053,2,10,2,308),_RuckusSCGRadProxyIp_Type())
ruckusSCGRadProxyIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGRadProxyIp.setStatus(_B)
_RuckusSCGAccSrvrIp_Type=OctetString
_RuckusSCGAccSrvrIp_Object=MibScalar
ruckusSCGAccSrvrIp=_RuckusSCGAccSrvrIp_Object((1,3,6,1,4,1,25053,2,10,2,309),_RuckusSCGAccSrvrIp_Type())
ruckusSCGAccSrvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGAccSrvrIp.setStatus(_B)
_RuckusSCGRealm_Type=OctetString
_RuckusSCGRealm_Object=MibScalar
ruckusSCGRealm=_RuckusSCGRealm_Object((1,3,6,1,4,1,25053,2,10,2,310),_RuckusSCGRealm_Type())
ruckusSCGRealm.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGRealm.setStatus(_B)
_RuckusSCGCgfSrvrIp_Type=OctetString
_RuckusSCGCgfSrvrIp_Object=MibScalar
ruckusSCGCgfSrvrIp=_RuckusSCGCgfSrvrIp_Object((1,3,6,1,4,1,25053,2,10,2,311),_RuckusSCGCgfSrvrIp_Type())
ruckusSCGCgfSrvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGCgfSrvrIp.setStatus(_B)
_RuckusSCGRadSrvrIp_Type=OctetString
_RuckusSCGRadSrvrIp_Object=MibScalar
ruckusSCGRadSrvrIp=_RuckusSCGRadSrvrIp_Object((1,3,6,1,4,1,25053,2,10,2,312),_RuckusSCGRadSrvrIp_Type())
ruckusSCGRadSrvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGRadSrvrIp.setStatus(_B)
_RuckusSCGCipIp_Type=OctetString
_RuckusSCGCipIp_Object=MibScalar
ruckusSCGCipIp=_RuckusSCGCipIp_Object((1,3,6,1,4,1,25053,2,10,2,313),_RuckusSCGCipIp_Type())
ruckusSCGCipIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGCipIp.setStatus(_B)
_RuckusSCGPointCode_Type=OctetString
_RuckusSCGPointCode_Object=MibScalar
ruckusSCGPointCode=_RuckusSCGPointCode_Object((1,3,6,1,4,1,25053,2,10,2,314),_RuckusSCGPointCode_Type())
ruckusSCGPointCode.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGPointCode.setStatus(_B)
_RuckusSCGCongLevel_Type=OctetString
_RuckusSCGCongLevel_Object=MibScalar
ruckusSCGCongLevel=_RuckusSCGCongLevel_Object((1,3,6,1,4,1,25053,2,10,2,315),_RuckusSCGCongLevel_Type())
ruckusSCGCongLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGCongLevel.setStatus(_B)
_RuckusSCGSSN_Type=OctetString
_RuckusSCGSSN_Object=MibScalar
ruckusSCGSSN=_RuckusSCGSSN_Object((1,3,6,1,4,1,25053,2,10,2,316),_RuckusSCGSSN_Type())
ruckusSCGSSN.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSSN.setStatus(_B)
_RuckusSCGRoutingContext_Type=OctetString
_RuckusSCGRoutingContext_Object=MibScalar
ruckusSCGRoutingContext=_RuckusSCGRoutingContext_Object((1,3,6,1,4,1,25053,2,10,2,317),_RuckusSCGRoutingContext_Type())
ruckusSCGRoutingContext.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGRoutingContext.setStatus(_B)
_RuckusSCGSrcIP_Type=OctetString
_RuckusSCGSrcIP_Object=MibScalar
ruckusSCGSrcIP=_RuckusSCGSrcIP_Object((1,3,6,1,4,1,25053,2,10,2,318),_RuckusSCGSrcIP_Type())
ruckusSCGSrcIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSrcIP.setStatus(_B)
_RuckusSCGSrcPort_Type=OctetString
_RuckusSCGSrcPort_Object=MibScalar
ruckusSCGSrcPort=_RuckusSCGSrcPort_Object((1,3,6,1,4,1,25053,2,10,2,319),_RuckusSCGSrcPort_Type())
ruckusSCGSrcPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSrcPort.setStatus(_B)
_RuckusSCGDestIP_Type=OctetString
_RuckusSCGDestIP_Object=MibScalar
ruckusSCGDestIP=_RuckusSCGDestIP_Object((1,3,6,1,4,1,25053,2,10,2,320),_RuckusSCGDestIP_Type())
ruckusSCGDestIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDestIP.setStatus(_B)
_RuckusSCGDestPort_Type=OctetString
_RuckusSCGDestPort_Object=MibScalar
ruckusSCGDestPort=_RuckusSCGDestPort_Object((1,3,6,1,4,1,25053,2,10,2,321),_RuckusSCGDestPort_Type())
ruckusSCGDestPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDestPort.setStatus(_B)
_RuckusSCGOperation_Type=OctetString
_RuckusSCGOperation_Object=MibScalar
ruckusSCGOperation=_RuckusSCGOperation_Object((1,3,6,1,4,1,25053,2,10,2,322),_RuckusSCGOperation_Type())
ruckusSCGOperation.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGOperation.setStatus(_B)
_RuckusSCGHlrInstance_Type=OctetString
_RuckusSCGHlrInstance_Object=MibScalar
ruckusSCGHlrInstance=_RuckusSCGHlrInstance_Object((1,3,6,1,4,1,25053,2,10,2,323),_RuckusSCGHlrInstance_Type())
ruckusSCGHlrInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGHlrInstance.setStatus(_B)
_RuckusSCGUserName_Type=OctetString
_RuckusSCGUserName_Object=MibScalar
ruckusSCGUserName=_RuckusSCGUserName_Object((1,3,6,1,4,1,25053,2,10,2,324),_RuckusSCGUserName_Type())
ruckusSCGUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGUserName.setStatus(_B)
_RuckusSCGPgwIp_Type=OctetString
_RuckusSCGPgwIp_Object=MibScalar
ruckusSCGPgwIp=_RuckusSCGPgwIp_Object((1,3,6,1,4,1,25053,2,10,2,325),_RuckusSCGPgwIp_Type())
ruckusSCGPgwIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGPgwIp.setStatus(_B)
_RuckusSCGFileName_Type=OctetString
_RuckusSCGFileName_Object=MibScalar
ruckusSCGFileName=_RuckusSCGFileName_Object((1,3,6,1,4,1,25053,2,10,2,326),_RuckusSCGFileName_Type())
ruckusSCGFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGFileName.setStatus(_B)
_RuckusSCGLDAPSrvrIp_Type=OctetString
_RuckusSCGLDAPSrvrIp_Object=MibScalar
ruckusSCGLDAPSrvrIp=_RuckusSCGLDAPSrvrIp_Object((1,3,6,1,4,1,25053,2,10,2,327),_RuckusSCGLDAPSrvrIp_Type())
ruckusSCGLDAPSrvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLDAPSrvrIp.setStatus(_B)
_RuckusSCGADSrvrIp_Type=OctetString
_RuckusSCGADSrvrIp_Object=MibScalar
ruckusSCGADSrvrIp=_RuckusSCGADSrvrIp_Object((1,3,6,1,4,1,25053,2,10,2,328),_RuckusSCGADSrvrIp_Type())
ruckusSCGADSrvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGADSrvrIp.setStatus(_B)
_RuckusSCGSoftwareName_Type=OctetString
_RuckusSCGSoftwareName_Object=MibScalar
ruckusSCGSoftwareName=_RuckusSCGSoftwareName_Object((1,3,6,1,4,1,25053,2,10,2,329),_RuckusSCGSoftwareName_Type())
ruckusSCGSoftwareName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGSoftwareName.setStatus(_B)
_RuckusSCGDomainName_Type=OctetString
_RuckusSCGDomainName_Object=MibScalar
ruckusSCGDomainName=_RuckusSCGDomainName_Object((1,3,6,1,4,1,25053,2,10,2,330),_RuckusSCGDomainName_Type())
ruckusSCGDomainName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDomainName.setStatus(_B)
_RuckusSCGDNATIp_Type=OctetString
_RuckusSCGDNATIp_Object=MibScalar
ruckusSCGDNATIp=_RuckusSCGDNATIp_Object((1,3,6,1,4,1,25053,2,10,2,331),_RuckusSCGDNATIp_Type())
ruckusSCGDNATIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGDNATIp.setStatus(_B)
_RuckusSCGLMAIp_Type=OctetString
_RuckusSCGLMAIp_Object=MibScalar
ruckusSCGLMAIp=_RuckusSCGLMAIp_Object((1,3,6,1,4,1,25053,2,10,2,400),_RuckusSCGLMAIp_Type())
ruckusSCGLMAIp.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGLMAIp.setStatus(_B)
_RuckusSCGEventRoguePolicyName_Type=OctetString
_RuckusSCGEventRoguePolicyName_Object=MibScalar
ruckusSCGEventRoguePolicyName=_RuckusSCGEventRoguePolicyName_Object((1,3,6,1,4,1,25053,2,10,2,401),_RuckusSCGEventRoguePolicyName_Type())
ruckusSCGEventRoguePolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventRoguePolicyName.setStatus(_B)
_RuckusSCGEventRogueRuleName_Type=OctetString
_RuckusSCGEventRogueRuleName_Object=MibScalar
ruckusSCGEventRogueRuleName=_RuckusSCGEventRogueRuleName_Object((1,3,6,1,4,1,25053,2,10,2,402),_RuckusSCGEventRogueRuleName_Type())
ruckusSCGEventRogueRuleName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventRogueRuleName.setStatus(_B)
_RuckusSCGEventRogueType_Type=OctetString
_RuckusSCGEventRogueType_Object=MibScalar
ruckusSCGEventRogueType=_RuckusSCGEventRogueType_Object((1,3,6,1,4,1,25053,2,10,2,403),_RuckusSCGEventRogueType_Type())
ruckusSCGEventRogueType.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusSCGEventRogueType.setStatus(_B)
ruckusSCGSystemMiscEventTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,1))
ruckusSCGSystemMiscEventTrap.setObjects(*((_A,_C),(_A,_D),(_A,_s),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSystemMiscEventTrap.setStatus(_B)
ruckusSCGUpgradeSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,2))
ruckusSCGUpgradeSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_P),(_A,_t),(_A,_u),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGUpgradeSuccessTrap.setStatus(_B)
ruckusSCGUpgradeFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,3))
ruckusSCGUpgradeFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_t),(_A,_u),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGUpgradeFailedTrap.setStatus(_B)
ruckusSCGNodeRestartedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,4))
ruckusSCGNodeRestartedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeRestartedTrap.setStatus(_B)
ruckusSCGNodeShutdownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,5))
ruckusSCGNodeShutdownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeShutdownTrap.setStatus(_B)
ruckusSCGCPUUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,6))
ruckusSCGCPUUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_A7),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCPUUsageThresholdExceededTrap.setStatus(_B)
ruckusSCGMemoryUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,7))
ruckusSCGMemoryUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_A8),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGMemoryUsageThresholdExceededTrap.setStatus(_B)
ruckusSCGDiskUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,8))
ruckusSCGDiskUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_A9),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDiskUsageThresholdExceededTrap.setStatus(_B)
ruckusSCGLicenseUsageThresholdExceededTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,19))
ruckusSCGLicenseUsageThresholdExceededTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AT),(_A,_AU),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGLicenseUsageThresholdExceededTrap.setStatus(_B)
ruckusSCGAPMiscEventTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,20))
ruckusSCGAPMiscEventTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_s),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPMiscEventTrap.setStatus(_B)
ruckusSCGAPConnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,21))
ruckusSCGAPConnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPConnectedTrap.setStatus(_B)
ruckusSCGAPDeletedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,22))
ruckusSCGAPDeletedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPDeletedTrap.setStatus(_B)
ruckusSCGAPDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,23))
ruckusSCGAPDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPDisconnectedTrap.setStatus(_B)
ruckusSCGAPLostHeartbeatTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,24))
ruckusSCGAPLostHeartbeatTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLostHeartbeatTrap.setStatus(_B)
ruckusSCGAPRebootTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,25))
ruckusSCGAPRebootTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPRebootTrap.setStatus(_B)
ruckusSCGCriticalAPConnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,26))
ruckusSCGCriticalAPConnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCriticalAPConnectedTrap.setStatus(_B)
ruckusSCGCriticalAPDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,27))
ruckusSCGCriticalAPDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCriticalAPDisconnectedTrap.setStatus(_B)
ruckusSCGAPRejectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,28))
ruckusSCGAPRejectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_W),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPRejectedTrap.setStatus(_B)
ruckusSCGAPConfUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,29))
ruckusSCGAPConfUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AA),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPConfUpdateFailedTrap.setStatus(_B)
ruckusSCGAPConfUpdatedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,30))
ruckusSCGAPConfUpdatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AA),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPConfUpdatedTrap.setStatus(_B)
ruckusSCGAPSwapOutModelDiffTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,31))
ruckusSCGAPSwapOutModelDiffTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AB),(_A,_AC),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPSwapOutModelDiffTrap.setStatus(_B)
ruckusSCGAPPreProvisionModelDiffTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,32))
ruckusSCGAPPreProvisionModelDiffTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AB),(_A,_AC),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPPreProvisionModelDiffTrap.setStatus(_B)
ruckusSCGAPDiscoveryFailTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,33))
ruckusSCGAPDiscoveryFailTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_W),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPDiscoveryFailTrap.setStatus(_B)
ruckusSCGAPFirmwareUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,34))
ruckusSCGAPFirmwareUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPFirmwareUpdateFailedTrap.setStatus(_B)
ruckusSCGAPFirmwareUpdatedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,35))
ruckusSCGAPFirmwareUpdatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPFirmwareUpdatedTrap.setStatus(_B)
ruckusSCGAPWlanOversubscribedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,36))
ruckusSCGAPWlanOversubscribedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAPWlanOversubscribedTrap.setStatus(_B)
ruckusSCGAPFactoryResetTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,37))
ruckusSCGAPFactoryResetTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPFactoryResetTrap.setStatus(_B)
ruckusSCGCableModemDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,38))
ruckusSCGCableModemDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCableModemDownTrap.setStatus(_B)
ruckusSCGCableModemRebootTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,39))
ruckusSCGCableModemRebootTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCableModemRebootTrap.setStatus(_B)
ruckusSCGAPJoinZoneFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,40))
ruckusSCGAPJoinZoneFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AV),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPJoinZoneFailedTrap.setStatus(_B)
ruckusSCGAPManagedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,41))
ruckusSCGAPManagedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_W),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAPManagedTrap.setStatus(_B)
ruckusSCGCPUUsageThresholdBackToNormalTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,42))
ruckusSCGCPUUsageThresholdBackToNormalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_A7),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCPUUsageThresholdBackToNormalTrap.setStatus(_B)
ruckusSCGMemoryUsageThresholdBackToNormalTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,43))
ruckusSCGMemoryUsageThresholdBackToNormalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_A8),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGMemoryUsageThresholdBackToNormalTrap.setStatus(_B)
ruckusSCGDiskUsageThresholdBackToNormalTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,44))
ruckusSCGDiskUsageThresholdBackToNormalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_A9),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDiskUsageThresholdBackToNormalTrap.setStatus(_B)
ruckusSCGCableModemUpTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,45))
ruckusSCGCableModemUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCableModemUpTrap.setStatus(_B)
ruckusSCGAPDiscoverySuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,46))
ruckusSCGAPDiscoverySuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_W),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPDiscoverySuccessTrap.setStatus(_B)
ruckusSCGCMResetByUserTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,47))
ruckusSCGCMResetByUserTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCMResetByUserTrap.setStatus(_B)
ruckusSCGCMResetFactoryByUserTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,48))
ruckusSCGCMResetFactoryByUserTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGCMResetFactoryByUserTrap.setStatus(_B)
ruckusSCGSSIDSpoofingRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,50))
ruckusSCGSSIDSpoofingRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_f),(_A,_j),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGSSIDSpoofingRogueAPDetectedTrap.setStatus(_B)
ruckusSCGMacSpoofingRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,51))
ruckusSCGMacSpoofingRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_f),(_A,_j),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGMacSpoofingRogueAPDetectedTrap.setStatus(_B)
ruckusSCGSameNetworkRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,52))
ruckusSCGSameNetworkRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_f),(_A,_j),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGSameNetworkRogueAPDetectedTrap.setStatus(_B)
ruckusSCGADHocNetworkRogueAPDetectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,53))
ruckusSCGADHocNetworkRogueAPDetectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_f),(_A,_j),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGADHocNetworkRogueAPDetectedTrap.setStatus(_B)
ruckusSCGMaliciousRogueAPTimeoutTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,54))
ruckusSCGMaliciousRogueAPTimeoutTrap.setObjects(*((_A,_C),(_A,_D),(_A,_f),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGMaliciousRogueAPTimeoutTrap.setStatus(_B)
ruckusSCGAPLBSConnectSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,55))
ruckusSCGAPLBSConnectSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLBSConnectSuccessTrap.setStatus(_B)
ruckusSCGAPLBSNoResponsesTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,56))
ruckusSCGAPLBSNoResponsesTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLBSNoResponsesTrap.setStatus(_B)
ruckusSCGAPLBSAuthFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,57))
ruckusSCGAPLBSAuthFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLBSAuthFailedTrap.setStatus(_B)
ruckusSCGAPLBSConnectFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,58))
ruckusSCGAPLBSConnectFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLBSConnectFailedTrap.setStatus(_B)
ruckusSCGGeneralRogueAPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,59))
ruckusSCGGeneralRogueAPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_f),(_A,_j),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_J),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:ruckusSCGGeneralRogueAPTrap.setStatus(_B)
ruckusSCGAPTunnelBuildFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,60))
ruckusSCGAPTunnelBuildFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Y),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPTunnelBuildFailedTrap.setStatus(_B)
ruckusSCGAPTunnelBuildSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,61))
ruckusSCGAPTunnelBuildSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Y),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPTunnelBuildSuccessTrap.setStatus(_B)
ruckusSCGAPTunnelDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,62))
ruckusSCGAPTunnelDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Y),(_A,_T),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPTunnelDisconnectedTrap.setStatus(_B)
ruckusSCGAPSoftGRETunnelFailoverPtoSTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,65))
ruckusSCGAPSoftGRETunnelFailoverPtoSTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AD),(_A,_AE),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPSoftGRETunnelFailoverPtoSTrap.setStatus(_B)
ruckusSCGAPSoftGRETunnelFailoverStoPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,66))
ruckusSCGAPSoftGRETunnelFailoverStoPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AD),(_A,_AE),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPSoftGRETunnelFailoverStoPTrap.setStatus(_B)
ruckusSCGAPSoftGREGatewayNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,67))
ruckusSCGAPSoftGREGatewayNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AZ),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPSoftGREGatewayNotReachableTrap.setStatus(_B)
ruckusSCGAPSoftGREGatewayReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,68))
ruckusSCGAPSoftGREGatewayReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_k),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAPSoftGREGatewayReachableTrap.setStatus(_B)
ruckusSCGDPConfUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,70))
ruckusSCGDPConfUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_AF),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPConfUpdateFailedTrap.setStatus(_B)
ruckusSCGDPLostHeartbeatTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,71))
ruckusSCGDPLostHeartbeatTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPLostHeartbeatTrap.setStatus(_B)
ruckusSCGDPDisconnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,72))
ruckusSCGDPDisconnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_W),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPDisconnectedTrap.setStatus(_B)
ruckusSCGDPPhyInterfaceDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,73))
ruckusSCGDPPhyInterfaceDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_AG),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPPhyInterfaceDownTrap.setStatus(_B)
ruckusSCGDPStatusUpdateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,74))
ruckusSCGDPStatusUpdateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPStatusUpdateFailedTrap.setStatus(_B)
ruckusSCGDPStatisticUpdateFaliedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,75))
ruckusSCGDPStatisticUpdateFaliedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPStatisticUpdateFaliedTrap.setStatus(_B)
ruckusSCGDPConnectedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,76))
ruckusSCGDPConnectedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_W),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPConnectedTrap.setStatus(_B)
ruckusSCGDPPhyInterfaceUpTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,77))
ruckusSCGDPPhyInterfaceUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_AG),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPPhyInterfaceUpTrap.setStatus(_B)
ruckusSCGDPConfUpdatedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,78))
ruckusSCGDPConfUpdatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_AF),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPConfUpdatedTrap.setStatus(_B)
ruckusSCGDPTunnelTearDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,79))
ruckusSCGDPTunnelTearDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_I),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPTunnelTearDownTrap.setStatus(_B)
ruckusSCGDPRebootTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,80))
ruckusSCGDPRebootTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPRebootTrap.setStatus(_B)
ruckusSCGDPAcceptTunnelRequestTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,81))
ruckusSCGDPAcceptTunnelRequestTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPAcceptTunnelRequestTrap.setStatus(_B)
ruckusSCGDPRejectTunnelRequestTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,82))
ruckusSCGDPRejectTunnelRequestTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_I),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPRejectTunnelRequestTrap.setStatus(_B)
ruckusSCGDPSgreGWUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,83))
ruckusSCGDPSgreGWUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_k),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPSgreGWUnreachableTrap.setStatus(_B)
ruckusSCGDPSgreGWReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,84))
ruckusSCGDPSgreGWReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_k),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPSgreGWReachableTrap.setStatus(_B)
ruckusSCGDPTunnelSetUpTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,85))
ruckusSCGDPTunnelSetUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPTunnelSetUpTrap.setStatus(_B)
ruckusSCGDPDiscoverySuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,86))
ruckusSCGDPDiscoverySuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_W),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPDiscoverySuccessTrap.setStatus(_B)
ruckusSCGDPDiscoveryFailTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,87))
ruckusSCGDPDiscoveryFailTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_W),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPDiscoveryFailTrap.setStatus(_B)
ruckusSCGDPSgreGWInactTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,88))
ruckusSCGDPSgreGWInactTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_k),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPSgreGWInactTrap.setStatus(_B)
ruckusSCGDPSgreGWActTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,89))
ruckusSCGDPSgreGWActTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_k),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPSgreGWActTrap.setStatus(_B)
ruckusSCGDPPktPoolLowTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,90))
ruckusSCGDPPktPoolLowTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_v),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPPktPoolLowTrap.setStatus(_B)
ruckusSCGDPPktPoolCriticalLowTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,91))
ruckusSCGDPPktPoolCriticalLowTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_v),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPPktPoolCriticalLowTrap.setStatus(_B)
ruckusSCGDPPktPoolRecoverTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,92))
ruckusSCGDPPktPoolRecoverTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_v),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPPktPoolRecoverTrap.setStatus(_B)
ruckusSCGDPCoreDeadTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,93))
ruckusSCGDPCoreDeadTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPCoreDeadTrap.setStatus(_B)
ruckusSCGDPDeletedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,94))
ruckusSCGDPDeletedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPDeletedTrap.setStatus(_B)
ruckusSCGDPUpgradeStartTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,95))
ruckusSCGDPUpgradeStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPUpgradeStartTrap.setStatus(_B)
ruckusSCGDPUpgradingTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,96))
ruckusSCGDPUpgradingTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPUpgradingTrap.setStatus(_B)
ruckusSCGDPUpgradeSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,97))
ruckusSCGDPUpgradeSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPUpgradeSuccessTrap.setStatus(_B)
ruckusSCGDPUpgradeFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,98))
ruckusSCGDPUpgradeFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDPUpgradeFailedTrap.setStatus(_B)
ruckusSCGClientMiscEventTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,100))
ruckusSCGClientMiscEventTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AH),(_A,_s),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClientMiscEventTrap.setStatus(_B)
ruckusSCGNodeJoinFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,200))
ruckusSCGNodeJoinFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeJoinFailedTrap.setStatus(_B)
ruckusSCGNodeRemoveFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,201))
ruckusSCGNodeRemoveFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeRemoveFailedTrap.setStatus(_B)
ruckusSCGNodeOutOfServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,202))
ruckusSCGNodeOutOfServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeOutOfServiceTrap.setStatus(_B)
ruckusSCGClusterInMaintenanceStateTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,203))
ruckusSCGClusterInMaintenanceStateTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterInMaintenanceStateTrap.setStatus(_B)
ruckusSCGClusterBackupFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,204))
ruckusSCGClusterBackupFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterBackupFailedTrap.setStatus(_B)
ruckusSCGClusterRestoreFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,205))
ruckusSCGClusterRestoreFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterRestoreFailedTrap.setStatus(_B)
ruckusSCGClusterAppStoppedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,206))
ruckusSCGClusterAppStoppedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_g),(_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterAppStoppedTrap.setStatus(_B)
ruckusSCGNodeBondInterfaceDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,207))
ruckusSCGNodeBondInterfaceDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_m),(_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeBondInterfaceDownTrap.setStatus(_B)
ruckusSCGNodePhyInterfaceDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,208))
ruckusSCGNodePhyInterfaceDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_m),(_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodePhyInterfaceDownTrap.setStatus(_B)
ruckusSCGClusterLeaderChangedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,209))
ruckusSCGClusterLeaderChangedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterLeaderChangedTrap.setStatus(_B)
ruckusSCGClusterUpgradeSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,210))
ruckusSCGClusterUpgradeSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_t),(_A,_u),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterUpgradeSuccessTrap.setStatus(_B)
ruckusSCGNodeBondInterfaceUpTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,211))
ruckusSCGNodeBondInterfaceUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_m),(_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeBondInterfaceUpTrap.setStatus(_B)
ruckusSCGNodePhyInterfaceUpTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,212))
ruckusSCGNodePhyInterfaceUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_m),(_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodePhyInterfaceUpTrap.setStatus(_B)
ruckusSCGClusterBackToInServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,216))
ruckusSCGClusterBackToInServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterBackToInServiceTrap.setStatus(_B)
ruckusSCGBackupClusterSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,217))
ruckusSCGBackupClusterSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGBackupClusterSuccessTrap.setStatus(_B)
ruckusSCGNodeJoinSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,218))
ruckusSCGNodeJoinSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeJoinSuccessTrap.setStatus(_B)
ruckusSCGClusterAppStartTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,219))
ruckusSCGClusterAppStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_g),(_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterAppStartTrap.setStatus(_B)
ruckusSCGNodeRemoveSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,220))
ruckusSCGNodeRemoveSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeRemoveSuccessTrap.setStatus(_B)
ruckusSCGClusterRestoreSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,221))
ruckusSCGClusterRestoreSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterRestoreSuccessTrap.setStatus(_B)
ruckusSCGNodeBackToInServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,222))
ruckusSCGNodeBackToInServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGNodeBackToInServiceTrap.setStatus(_B)
ruckusSCGSshTunnelSwitchedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,223))
ruckusSCGSshTunnelSwitchedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_F),(_A,_S),(_A,_Aa),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSshTunnelSwitchedTrap.setStatus(_B)
ruckusSCGClusterCfgBackupStartTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,224))
ruckusSCGClusterCfgBackupStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterCfgBackupStartTrap.setStatus(_B)
ruckusSCGClusterCfgBackupSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,225))
ruckusSCGClusterCfgBackupSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterCfgBackupSuccessTrap.setStatus(_B)
ruckusSCGClusterCfgBackupFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,226))
ruckusSCGClusterCfgBackupFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterCfgBackupFailedTrap.setStatus(_B)
ruckusSCGClusterCfgRestoreSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,227))
ruckusSCGClusterCfgRestoreSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterCfgRestoreSuccessTrap.setStatus(_B)
ruckusSCGClusterCfgRestoreFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,228))
ruckusSCGClusterCfgRestoreFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterCfgRestoreFailedTrap.setStatus(_B)
ruckusSCGClusterUploadSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,229))
ruckusSCGClusterUploadSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterUploadSuccessTrap.setStatus(_B)
ruckusSCGClusterUploadFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,230))
ruckusSCGClusterUploadFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterUploadFailedTrap.setStatus(_B)
ruckusSCGClusterOutOfServiceTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,231))
ruckusSCGClusterOutOfServiceTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterOutOfServiceTrap.setStatus(_B)
ruckusSCGClusterUploadVDPFirmwareStartTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,232))
ruckusSCGClusterUploadVDPFirmwareStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterUploadVDPFirmwareStartTrap.setStatus(_B)
ruckusSCGClusterUploadVDPFirmwareSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,233))
ruckusSCGClusterUploadVDPFirmwareSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterUploadVDPFirmwareSuccessTrap.setStatus(_B)
ruckusSCGClusterUploadVDPFirmwareFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,234))
ruckusSCGClusterUploadVDPFirmwareFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGClusterUploadVDPFirmwareFailedTrap.setStatus(_B)
ruckusSCGIpmiVotageTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,250))
ruckusSCGIpmiVotageTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiVotageTrap.setStatus(_B)
ruckusSCGIpmiTempBBTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,251))
ruckusSCGIpmiTempBBTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempBBTrap.setStatus(_B)
ruckusSCGIpmiTempFPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,252))
ruckusSCGIpmiTempFPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempFPTrap.setStatus(_B)
ruckusSCGIpmiTempIOHTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,253))
ruckusSCGIpmiTempIOHTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempIOHTrap.setStatus(_B)
ruckusSCGIpmiTempMemPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,254))
ruckusSCGIpmiTempMemPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_n),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempMemPTrap.setStatus(_B)
ruckusSCGIpmiTempPSTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,255))
ruckusSCGIpmiTempPSTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempPSTrap.setStatus(_B)
ruckusSCGIpmiTempPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,256))
ruckusSCGIpmiTempPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_n),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempPTrap.setStatus(_B)
ruckusSCGIpmiTempHSBPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,257))
ruckusSCGIpmiTempHSBPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiTempHSBPTrap.setStatus(_B)
ruckusSCGIpmiFanTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,258))
ruckusSCGIpmiFanTrap.setObjects(*((_A,_C),(_A,_D),(_A,_o),(_A,_p),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiFanTrap.setStatus(_B)
ruckusSCGIpmiPowerTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,259))
ruckusSCGIpmiPowerTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_h),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiPowerTrap.setStatus(_B)
ruckusSCGIpmiCurrentTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,260))
ruckusSCGIpmiCurrentTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_h),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiCurrentTrap.setStatus(_B)
ruckusSCGIpmiFanStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,261))
ruckusSCGIpmiFanStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_o),(_A,_p),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiFanStatusTrap.setStatus(_B)
ruckusSCGIpmiPsStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,262))
ruckusSCGIpmiPsStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_h),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiPsStatusTrap.setStatus(_B)
ruckusSCGIpmiDrvStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,263))
ruckusSCGIpmiDrvStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AI),(_A,_AJ),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiDrvStatusTrap.setStatus(_B)
ruckusSCGIpmiREVotageTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,264))
ruckusSCGIpmiREVotageTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiREVotageTrap.setStatus(_B)
ruckusSCGIpmiRETempBBTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,265))
ruckusSCGIpmiRETempBBTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempBBTrap.setStatus(_B)
ruckusSCGIpmiRETempFPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,266))
ruckusSCGIpmiRETempFPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempFPTrap.setStatus(_B)
ruckusSCGIpmiRETempIOHTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,267))
ruckusSCGIpmiRETempIOHTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempIOHTrap.setStatus(_B)
ruckusSCGIpmiRETempMemPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,268))
ruckusSCGIpmiRETempMemPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_n),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempMemPTrap.setStatus(_B)
ruckusSCGIpmiRETempPSTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,269))
ruckusSCGIpmiRETempPSTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempPSTrap.setStatus(_B)
ruckusSCGIpmiRETempPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,270))
ruckusSCGIpmiRETempPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_n),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempPTrap.setStatus(_B)
ruckusSCGIpmiRETempHSBPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,271))
ruckusSCGIpmiRETempHSBPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_V),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRETempHSBPTrap.setStatus(_B)
ruckusSCGIpmiREFanTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,272))
ruckusSCGIpmiREFanTrap.setObjects(*((_A,_C),(_A,_D),(_A,_o),(_A,_p),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiREFanTrap.setStatus(_B)
ruckusSCGIpmiREPowerTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,273))
ruckusSCGIpmiREPowerTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_h),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiREPowerTrap.setStatus(_B)
ruckusSCGIpmiRECurrentTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,274))
ruckusSCGIpmiRECurrentTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_h),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiRECurrentTrap.setStatus(_B)
ruckusSCGIpmiREFanStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,275))
ruckusSCGIpmiREFanStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_o),(_A,_p),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiREFanStatusTrap.setStatus(_B)
ruckusSCGIpmiREPsStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,276))
ruckusSCGIpmiREPsStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_b),(_A,_h),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiREPsStatusTrap.setStatus(_B)
ruckusSCGIpmiREDrvStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,277))
ruckusSCGIpmiREDrvStatusTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AI),(_A,_AJ),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGIpmiREDrvStatusTrap.setStatus(_B)
ruckusSCGFtpTransferErrorTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,280))
ruckusSCGFtpTransferErrorTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGFtpTransferErrorTrap.setStatus(_B)
ruckusSCGSystemLBSConnectSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,290))
ruckusSCGSystemLBSConnectSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_Z),(_A,_a),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSystemLBSConnectSuccessTrap.setStatus(_B)
ruckusSCGSystemLBSNoResponseTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,291))
ruckusSCGSystemLBSNoResponseTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_Z),(_A,_a),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSystemLBSNoResponseTrap.setStatus(_B)
ruckusSCGSystemLBSAuthFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,292))
ruckusSCGSystemLBSAuthFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_Z),(_A,_a),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSystemLBSAuthFailedTrap.setStatus(_B)
ruckusSCGSystemLBSConnectFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,293))
ruckusSCGSystemLBSConnectFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_Z),(_A,_a),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSystemLBSConnectFailedTrap.setStatus(_B)
ruckusSCGProcessRestartTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,300))
ruckusSCGProcessRestartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_g),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGProcessRestartTrap.setStatus(_B)
ruckusSCGServiceUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,301))
ruckusSCGServiceUnavailableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_g),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGServiceUnavailableTrap.setStatus(_B)
ruckusSCGKeepAliveFailureTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,302))
ruckusSCGKeepAliveFailureTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_g),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGKeepAliveFailureTrap.setStatus(_B)
ruckusSCGResourceUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,304))
ruckusSCGResourceUnavailableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGResourceUnavailableTrap.setStatus(_B)
ruckusSCGSmfRegFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,305))
ruckusSCGSmfRegFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSmfRegFailedTrap.setStatus(_B)
ruckusSCGHipFailoverTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,306))
ruckusSCGHipFailoverTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGHipFailoverTrap.setStatus(_B)
ruckusSCGConfUpdFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,307))
ruckusSCGConfUpdFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_g),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGConfUpdFailedTrap.setStatus(_B)
ruckusSCGConfRcvFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,308))
ruckusSCGConfRcvFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGConfRcvFailedTrap.setStatus(_B)
ruckusSCGLostCnxnToDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,309))
ruckusSCGLostCnxnToDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_W),(_A,_Y),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGLostCnxnToDbladeTrap.setStatus(_B)
ruckusSCGGgsnRestartedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,310))
ruckusSCGGgsnRestartedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_w),(_A,_AK),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGGgsnRestartedTrap.setStatus(_B)
ruckusSCGGgsnNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,311))
ruckusSCGGgsnNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_w),(_A,_AK),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGGgsnNotReachableTrap.setStatus(_B)
ruckusSCGGgsnNotResolvedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,312))
ruckusSCGGgsnNotResolvedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AL),(_A,_X),(_A,_c),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGGgsnNotResolvedTrap.setStatus(_B)
ruckusSCGUnknownUETrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,313))
ruckusSCGUnknownUETrap.setObjects(*((_A,_C),(_A,_D),(_A,_AH),(_A,_c),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGUnknownUETrap.setStatus(_B)
ruckusSCGAuthSrvrNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,314))
ruckusSCGAuthSrvrNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_x),(_A,_AM),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAuthSrvrNotReachableTrap.setStatus(_B)
ruckusSCGAccSrvrNotReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,315))
ruckusSCGAccSrvrNotReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Ae),(_A,_AM),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAccSrvrNotReachableTrap.setStatus(_B)
ruckusSCGUnknownRealmTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,316))
ruckusSCGUnknownRealmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_i),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGUnknownRealmTrap.setStatus(_B)
ruckusSCGAuthFailedNonPermanentIDTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,317))
ruckusSCGAuthFailedNonPermanentIDTrap.setObjects(*((_A,_C),(_A,_D),(_A,_X),(_A,_c),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAuthFailedNonPermanentIDTrap.setStatus(_B)
ruckusSCGCnxnToCgfFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,318))
ruckusSCGCnxnToCgfFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_y),(_A,_e),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCnxnToCgfFailedTrap.setStatus(_B)
ruckusSCGCdrTransferFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,319))
ruckusSCGCdrTransferFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_y),(_A,_e),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCdrTransferFailedTrap.setStatus(_B)
ruckusSCGCdrGenerateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,320))
ruckusSCGCdrGenerateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_e),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCdrGenerateFailedTrap.setStatus(_B)
ruckusSCGDestNotRecheableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,321))
ruckusSCGDestNotRecheableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_l),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDestNotRecheableTrap.setStatus(_B)
ruckusSCGAppServerDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,324))
ruckusSCGAppServerDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_z),(_A,_l),(_A,_A0),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAppServerDownTrap.setStatus(_B)
ruckusSCGAppServerInactiveTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,325))
ruckusSCGAppServerInactiveTrap.setObjects(*((_A,_C),(_A,_D),(_A,_z),(_A,_l),(_A,_A0),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAppServerInactiveTrap.setStatus(_B)
ruckusSCGAssocCantStartTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,326))
ruckusSCGAssocCantStartTrap.setObjects(*((_A,_C),(_A,_D),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAssocCantStartTrap.setStatus(_B)
ruckusSCGAssocDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,327))
ruckusSCGAssocDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAssocDownTrap.setStatus(_B)
ruckusSCGOutboundRoutingFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,328))
ruckusSCGOutboundRoutingFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Af),(_A,_X),(_A,_Ag),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGOutboundRoutingFailedTrap.setStatus(_B)
ruckusSCGDidAllocationFailureTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,329))
ruckusSCGDidAllocationFailureTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDidAllocationFailureTrap.setStatus(_B)
ruckusSCGPdnGwUnresolvedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,331))
ruckusSCGPdnGwUnresolvedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_AL),(_A,_X),(_A,_c),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPdnGwUnresolvedTrap.setStatus(_B)
ruckusSCGPdnGwVersionUnsupportedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,332))
ruckusSCGPdnGwVersionUnsupportedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPdnGwVersionUnsupportedTrap.setStatus(_B)
ruckusSCGPdnGwAssociationDownTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,333))
ruckusSCGPdnGwAssociationDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPdnGwAssociationDownTrap.setStatus(_B)
ruckusSCGCreateSessionResponseFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,334))
ruckusSCGCreateSessionResponseFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_X),(_A,_i),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCreateSessionResponseFailedTrap.setStatus(_B)
ruckusSCGDecodeFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,335))
ruckusSCGDecodeFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDecodeFailedTrap.setStatus(_B)
ruckusSCGModifyBearerResponseFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,336))
ruckusSCGModifyBearerResponseFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_X),(_A,_i),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGModifyBearerResponseFailedTrap.setStatus(_B)
ruckusSCGDeleteSessionResponseFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,337))
ruckusSCGDeleteSessionResponseFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_X),(_A,_i),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDeleteSessionResponseFailedTrap.setStatus(_B)
ruckusSCGDeleteBearerRequestFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,338))
ruckusSCGDeleteBearerRequestFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_i),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDeleteBearerRequestFailedTrap.setStatus(_B)
ruckusSCGUpdateBearerRequestFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,339))
ruckusSCGUpdateBearerRequestFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_d),(_A,_i),(_A,_F),(_A,_P),(_A,_T),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGUpdateBearerRequestFailedTrap.setStatus(_B)
ruckusSCGCgfServerNotConfiguredTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,340))
ruckusSCGCgfServerNotConfiguredTrap.setObjects(*((_A,_C),(_A,_D),(_A,_y),(_A,_w),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGCgfServerNotConfiguredTrap.setStatus(_B)
ruckusSCGTtgSessionCriticalThresholdTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,342))
ruckusSCGTtgSessionCriticalThresholdTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGTtgSessionCriticalThresholdTrap.setStatus(_B)
ruckusSCGTtgSessionLicenseInsufficientTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,343))
ruckusSCGTtgSessionLicenseInsufficientTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGTtgSessionLicenseInsufficientTrap.setStatus(_B)
ruckusSCGAPAcctMsgMandatoryPrmMissingTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,344))
ruckusSCGAPAcctMsgMandatoryPrmMissingTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_H),(_A,_q),(_A,_F),(_A,_P),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPAcctMsgMandatoryPrmMissingTrap.setStatus(_B)
ruckusSCGAcctUnknownRealmTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,345))
ruckusSCGAcctUnknownRealmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_H),(_A,_q),(_A,_F),(_A,_P),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAcctUnknownRealmTrap.setStatus(_B)
ruckusSCGAPAcctMsgDecodeFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,346))
ruckusSCGAPAcctMsgDecodeFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_H),(_A,_F),(_A,_P),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPAcctMsgDecodeFailedTrap.setStatus(_B)
ruckusSCGAPAcctRespWhileInvalidConfigTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,347))
ruckusSCGAPAcctRespWhileInvalidConfigTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_H),(_A,_q),(_A,_F),(_A,_P),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPAcctRespWhileInvalidConfigTrap.setStatus(_B)
ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,348))
ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_H),(_A,_q),(_A,_F),(_A,_P),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap.setStatus(_B)
ruckusSCGUnauthorizedCoaDmMessageDroppedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,349))
ruckusSCGUnauthorizedCoaDmMessageDroppedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_U),(_A,_e),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGUnauthorizedCoaDmMessageDroppedTrap.setStatus(_B)
ruckusSCGConnectedToDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,350))
ruckusSCGConnectedToDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_W),(_A,_Y),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGConnectedToDbladeTrap.setStatus(_B)
ruckusSCGDestAvailableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,351))
ruckusSCGDestAvailableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_l),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGDestAvailableTrap.setStatus(_B)
ruckusSCGAppServerActiveTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,352))
ruckusSCGAppServerActiveTrap.setObjects(*((_A,_C),(_A,_D),(_A,_z),(_A,_l),(_A,_A0),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAppServerActiveTrap.setStatus(_B)
ruckusSCGAssocUpTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,353))
ruckusSCGAssocUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGAssocUpTrap.setStatus(_B)
ruckusSCGSessUpdatedAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,354))
ruckusSCGSessUpdatedAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_W),(_A,_Y),(_A,_X),(_A,_c),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSessUpdatedAtDbladeTrap.setStatus(_B)
ruckusSCGSessUpdateErrAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,355))
ruckusSCGSessUpdateErrAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_W),(_A,_Y),(_A,_X),(_A,_c),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSessUpdateErrAtDbladeTrap.setStatus(_B)
ruckusSCGSessDeletedAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,356))
ruckusSCGSessDeletedAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_W),(_A,_Y),(_A,_X),(_A,_c),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSessDeletedAtDbladeTrap.setStatus(_B)
ruckusSCGSessDeleteErrAtDbladeTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,357))
ruckusSCGSessDeleteErrAtDbladeTrap.setObjects(*((_A,_C),(_A,_D),(_A,_W),(_A,_Y),(_A,_X),(_A,_c),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSessDeleteErrAtDbladeTrap.setStatus(_B)
ruckusSCGLicenseSyncSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,358))
ruckusSCGLicenseSyncSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_AN),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGLicenseSyncSuccessTrap.setStatus(_B)
ruckusSCGLicenseSyncFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,359))
ruckusSCGLicenseSyncFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_AN),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGLicenseSyncFailedTrap.setStatus(_B)
ruckusSCGLicenseImportSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,360))
ruckusSCGLicenseImportSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGLicenseImportSuccessTrap.setStatus(_B)
ruckusSCGLicenseImportFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,361))
ruckusSCGLicenseImportFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_R),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGLicenseImportFailedTrap.setStatus(_B)
ruckusSCGSyslogServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,370))
ruckusSCGSyslogServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AO),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSyslogServerReachableTrap.setStatus(_B)
ruckusSCGSyslogServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,371))
ruckusSCGSyslogServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_AO),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSyslogServerUnreachableTrap.setStatus(_B)
ruckusSCGSyslogServerSwitchedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,372))
ruckusSCGSyslogServerSwitchedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_Ah),(_A,_Ai),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGSyslogServerSwitchedTrap.setStatus(_B)
ruckusSCGAPRadiusServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,400))
ruckusSCGAPRadiusServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_e),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPRadiusServerReachableTrap.setStatus(_B)
ruckusSCGAPRadiusServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,401))
ruckusSCGAPRadiusServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_e),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPRadiusServerUnreachableTrap.setStatus(_B)
ruckusSCGAPLDAPServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,402))
ruckusSCGAPLDAPServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AP),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLDAPServerReachableTrap.setStatus(_B)
ruckusSCGAPLDAPServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,403))
ruckusSCGAPLDAPServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AP),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPLDAPServerUnreachableTrap.setStatus(_B)
ruckusSCGAPADServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,404))
ruckusSCGAPADServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AQ),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPADServerReachableTrap.setStatus(_B)
ruckusSCGAPADServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,405))
ruckusSCGAPADServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AQ),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPADServerUnreachableTrap.setStatus(_B)
ruckusSCGAPUsbSoftwarePackageDownloadedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,406))
ruckusSCGAPUsbSoftwarePackageDownloadedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AR),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPUsbSoftwarePackageDownloadedTrap.setStatus(_B)
ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,407))
ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AR),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap.setStatus(_B)
ruckusSCGEspAuthServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,408))
ruckusSCGEspAuthServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_x),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspAuthServerReachableTrap.setStatus(_B)
ruckusSCGEspAuthServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,409))
ruckusSCGEspAuthServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_x),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspAuthServerUnreachableTrap.setStatus(_B)
ruckusSCGEspAuthServerResolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,410))
ruckusSCGEspAuthServerResolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_r),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspAuthServerResolvableTrap.setStatus(_B)
ruckusSCGEspAuthServerUnResolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,411))
ruckusSCGEspAuthServerUnResolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_r),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspAuthServerUnResolvableTrap.setStatus(_B)
ruckusSCGEspDNATServerReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,412))
ruckusSCGEspDNATServerReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AS),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspDNATServerReachableTrap.setStatus(_B)
ruckusSCGEspDNATServerUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,413))
ruckusSCGEspDNATServerUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AS),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspDNATServerUnreachableTrap.setStatus(_B)
ruckusSCGEspDNATServerResolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,414))
ruckusSCGEspDNATServerResolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_r),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspDNATServerResolvableTrap.setStatus(_B)
ruckusSCGEspDNATServerUnresolvableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,415))
ruckusSCGEspDNATServerUnresolvableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_r),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGEspDNATServerUnresolvableTrap.setStatus(_B)
ruckusRateLimitTORSurpassedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,500))
ruckusRateLimitTORSurpassedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_e),(_A,_E)))
if mibBuilder.loadTexts:ruckusRateLimitTORSurpassedTrap.setStatus(_B)
ruckusSCGIPSecTunnelAssociatedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,600))
ruckusSCGIPSecTunnelAssociatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_A5),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGIPSecTunnelAssociatedTrap.setStatus(_B)
ruckusSCGIPSecTunnelDisassociatedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,601))
ruckusSCGIPSecTunnelDisassociatedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_A5),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGIPSecTunnelDisassociatedTrap.setStatus(_B)
ruckusSCGIPSecTunnelAssociateFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,602))
ruckusSCGIPSecTunnelAssociateFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_I),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_A5),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:ruckusSCGIPSecTunnelAssociateFailedTrap.setStatus(_B)
ruckusSCGPmipProcessInitTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,700))
ruckusSCGPmipProcessInitTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipProcessInitTrap.setStatus(_B)
ruckusSCGPmipUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,701))
ruckusSCGPmipUnavailableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipUnavailableTrap.setStatus(_B)
ruckusSCGPmipUnallocatedMemoryTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,702))
ruckusSCGPmipUnallocatedMemoryTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipUnallocatedMemoryTrap.setStatus(_B)
ruckusSCGPmipUpdateCgfFailedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,703))
ruckusSCGPmipUpdateCgfFailedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipUpdateCgfFailedTrap.setStatus(_B)
ruckusSCGPmipLMAIcmpUnreachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,704))
ruckusSCGPmipLMAIcmpUnreachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_A6),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipLMAIcmpUnreachableTrap.setStatus(_B)
ruckusSCGPmipLMAFailOverTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,705))
ruckusSCGPmipLMAFailOverTrap.setObjects(*((_A,_C),(_A,_D),(_A,_A6),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipLMAFailOverTrap.setStatus(_B)
ruckusSCGPmipBindingFailureTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,706))
ruckusSCGPmipBindingFailureTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipBindingFailureTrap.setStatus(_B)
ruckusSCGPmiplostCnxnToDHCPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,707))
ruckusSCGPmiplostCnxnToDHCPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmiplostCnxnToDHCPTrap.setStatus(_B)
ruckusSCGPmipLMAIcmpReachableTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,708))
ruckusSCGPmipLMAIcmpReachableTrap.setObjects(*((_A,_C),(_A,_D),(_A,_A6),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipLMAIcmpReachableTrap.setStatus(_B)
ruckusSCGPmipBindingSuccessTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,709))
ruckusSCGPmipBindingSuccessTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipBindingSuccessTrap.setStatus(_B)
ruckusSCGPmipConnectedToDHCPTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,710))
ruckusSCGPmipConnectedToDHCPTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipConnectedToDHCPTrap.setStatus(_B)
ruckusSCGPmipProcessStoppedTrap=NotificationType((1,3,6,1,4,1,25053,2,10,1,711))
ruckusSCGPmipProcessStoppedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_P),(_A,_E)))
if mibBuilder.loadTexts:ruckusSCGPmipProcessStoppedTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ruckusSCGEventMIB':ruckusSCGEventMIB,'ruckusSCGEventTraps':ruckusSCGEventTraps,'ruckusSCGSystemMiscEventTrap':ruckusSCGSystemMiscEventTrap,'ruckusSCGUpgradeSuccessTrap':ruckusSCGUpgradeSuccessTrap,'ruckusSCGUpgradeFailedTrap':ruckusSCGUpgradeFailedTrap,'ruckusSCGNodeRestartedTrap':ruckusSCGNodeRestartedTrap,'ruckusSCGNodeShutdownTrap':ruckusSCGNodeShutdownTrap,'ruckusSCGCPUUsageThresholdExceededTrap':ruckusSCGCPUUsageThresholdExceededTrap,'ruckusSCGMemoryUsageThresholdExceededTrap':ruckusSCGMemoryUsageThresholdExceededTrap,'ruckusSCGDiskUsageThresholdExceededTrap':ruckusSCGDiskUsageThresholdExceededTrap,'ruckusSCGLicenseUsageThresholdExceededTrap':ruckusSCGLicenseUsageThresholdExceededTrap,'ruckusSCGAPMiscEventTrap':ruckusSCGAPMiscEventTrap,'ruckusSCGAPConnectedTrap':ruckusSCGAPConnectedTrap,'ruckusSCGAPDeletedTrap':ruckusSCGAPDeletedTrap,'ruckusSCGAPDisconnectedTrap':ruckusSCGAPDisconnectedTrap,'ruckusSCGAPLostHeartbeatTrap':ruckusSCGAPLostHeartbeatTrap,'ruckusSCGAPRebootTrap':ruckusSCGAPRebootTrap,'ruckusSCGCriticalAPConnectedTrap':ruckusSCGCriticalAPConnectedTrap,'ruckusSCGCriticalAPDisconnectedTrap':ruckusSCGCriticalAPDisconnectedTrap,'ruckusSCGAPRejectedTrap':ruckusSCGAPRejectedTrap,'ruckusSCGAPConfUpdateFailedTrap':ruckusSCGAPConfUpdateFailedTrap,'ruckusSCGAPConfUpdatedTrap':ruckusSCGAPConfUpdatedTrap,'ruckusSCGAPSwapOutModelDiffTrap':ruckusSCGAPSwapOutModelDiffTrap,'ruckusSCGAPPreProvisionModelDiffTrap':ruckusSCGAPPreProvisionModelDiffTrap,'ruckusSCGAPDiscoveryFailTrap':ruckusSCGAPDiscoveryFailTrap,'ruckusSCGAPFirmwareUpdateFailedTrap':ruckusSCGAPFirmwareUpdateFailedTrap,'ruckusSCGAPFirmwareUpdatedTrap':ruckusSCGAPFirmwareUpdatedTrap,'ruckusSCGAPWlanOversubscribedTrap':ruckusSCGAPWlanOversubscribedTrap,'ruckusSCGAPFactoryResetTrap':ruckusSCGAPFactoryResetTrap,'ruckusSCGCableModemDownTrap':ruckusSCGCableModemDownTrap,'ruckusSCGCableModemRebootTrap':ruckusSCGCableModemRebootTrap,'ruckusSCGAPJoinZoneFailedTrap':ruckusSCGAPJoinZoneFailedTrap,'ruckusSCGAPManagedTrap':ruckusSCGAPManagedTrap,'ruckusSCGCPUUsageThresholdBackToNormalTrap':ruckusSCGCPUUsageThresholdBackToNormalTrap,'ruckusSCGMemoryUsageThresholdBackToNormalTrap':ruckusSCGMemoryUsageThresholdBackToNormalTrap,'ruckusSCGDiskUsageThresholdBackToNormalTrap':ruckusSCGDiskUsageThresholdBackToNormalTrap,'ruckusSCGCableModemUpTrap':ruckusSCGCableModemUpTrap,'ruckusSCGAPDiscoverySuccessTrap':ruckusSCGAPDiscoverySuccessTrap,'ruckusSCGCMResetByUserTrap':ruckusSCGCMResetByUserTrap,'ruckusSCGCMResetFactoryByUserTrap':ruckusSCGCMResetFactoryByUserTrap,'ruckusSCGSSIDSpoofingRogueAPDetectedTrap':ruckusSCGSSIDSpoofingRogueAPDetectedTrap,'ruckusSCGMacSpoofingRogueAPDetectedTrap':ruckusSCGMacSpoofingRogueAPDetectedTrap,'ruckusSCGSameNetworkRogueAPDetectedTrap':ruckusSCGSameNetworkRogueAPDetectedTrap,'ruckusSCGADHocNetworkRogueAPDetectedTrap':ruckusSCGADHocNetworkRogueAPDetectedTrap,'ruckusSCGMaliciousRogueAPTimeoutTrap':ruckusSCGMaliciousRogueAPTimeoutTrap,'ruckusSCGAPLBSConnectSuccessTrap':ruckusSCGAPLBSConnectSuccessTrap,'ruckusSCGAPLBSNoResponsesTrap':ruckusSCGAPLBSNoResponsesTrap,'ruckusSCGAPLBSAuthFailedTrap':ruckusSCGAPLBSAuthFailedTrap,'ruckusSCGAPLBSConnectFailedTrap':ruckusSCGAPLBSConnectFailedTrap,'ruckusSCGGeneralRogueAPTrap':ruckusSCGGeneralRogueAPTrap,'ruckusSCGAPTunnelBuildFailedTrap':ruckusSCGAPTunnelBuildFailedTrap,'ruckusSCGAPTunnelBuildSuccessTrap':ruckusSCGAPTunnelBuildSuccessTrap,'ruckusSCGAPTunnelDisconnectedTrap':ruckusSCGAPTunnelDisconnectedTrap,'ruckusSCGAPSoftGRETunnelFailoverPtoSTrap':ruckusSCGAPSoftGRETunnelFailoverPtoSTrap,'ruckusSCGAPSoftGRETunnelFailoverStoPTrap':ruckusSCGAPSoftGRETunnelFailoverStoPTrap,'ruckusSCGAPSoftGREGatewayNotReachableTrap':ruckusSCGAPSoftGREGatewayNotReachableTrap,'ruckusSCGAPSoftGREGatewayReachableTrap':ruckusSCGAPSoftGREGatewayReachableTrap,'ruckusSCGDPConfUpdateFailedTrap':ruckusSCGDPConfUpdateFailedTrap,'ruckusSCGDPLostHeartbeatTrap':ruckusSCGDPLostHeartbeatTrap,'ruckusSCGDPDisconnectedTrap':ruckusSCGDPDisconnectedTrap,'ruckusSCGDPPhyInterfaceDownTrap':ruckusSCGDPPhyInterfaceDownTrap,'ruckusSCGDPStatusUpdateFailedTrap':ruckusSCGDPStatusUpdateFailedTrap,'ruckusSCGDPStatisticUpdateFaliedTrap':ruckusSCGDPStatisticUpdateFaliedTrap,'ruckusSCGDPConnectedTrap':ruckusSCGDPConnectedTrap,'ruckusSCGDPPhyInterfaceUpTrap':ruckusSCGDPPhyInterfaceUpTrap,'ruckusSCGDPConfUpdatedTrap':ruckusSCGDPConfUpdatedTrap,'ruckusSCGDPTunnelTearDownTrap':ruckusSCGDPTunnelTearDownTrap,'ruckusSCGDPRebootTrap':ruckusSCGDPRebootTrap,'ruckusSCGDPAcceptTunnelRequestTrap':ruckusSCGDPAcceptTunnelRequestTrap,'ruckusSCGDPRejectTunnelRequestTrap':ruckusSCGDPRejectTunnelRequestTrap,'ruckusSCGDPSgreGWUnreachableTrap':ruckusSCGDPSgreGWUnreachableTrap,'ruckusSCGDPSgreGWReachableTrap':ruckusSCGDPSgreGWReachableTrap,'ruckusSCGDPTunnelSetUpTrap':ruckusSCGDPTunnelSetUpTrap,'ruckusSCGDPDiscoverySuccessTrap':ruckusSCGDPDiscoverySuccessTrap,'ruckusSCGDPDiscoveryFailTrap':ruckusSCGDPDiscoveryFailTrap,'ruckusSCGDPSgreGWInactTrap':ruckusSCGDPSgreGWInactTrap,'ruckusSCGDPSgreGWActTrap':ruckusSCGDPSgreGWActTrap,'ruckusSCGDPPktPoolLowTrap':ruckusSCGDPPktPoolLowTrap,'ruckusSCGDPPktPoolCriticalLowTrap':ruckusSCGDPPktPoolCriticalLowTrap,'ruckusSCGDPPktPoolRecoverTrap':ruckusSCGDPPktPoolRecoverTrap,'ruckusSCGDPCoreDeadTrap':ruckusSCGDPCoreDeadTrap,'ruckusSCGDPDeletedTrap':ruckusSCGDPDeletedTrap,'ruckusSCGDPUpgradeStartTrap':ruckusSCGDPUpgradeStartTrap,'ruckusSCGDPUpgradingTrap':ruckusSCGDPUpgradingTrap,'ruckusSCGDPUpgradeSuccessTrap':ruckusSCGDPUpgradeSuccessTrap,'ruckusSCGDPUpgradeFailedTrap':ruckusSCGDPUpgradeFailedTrap,'ruckusSCGClientMiscEventTrap':ruckusSCGClientMiscEventTrap,'ruckusSCGNodeJoinFailedTrap':ruckusSCGNodeJoinFailedTrap,'ruckusSCGNodeRemoveFailedTrap':ruckusSCGNodeRemoveFailedTrap,'ruckusSCGNodeOutOfServiceTrap':ruckusSCGNodeOutOfServiceTrap,'ruckusSCGClusterInMaintenanceStateTrap':ruckusSCGClusterInMaintenanceStateTrap,'ruckusSCGClusterBackupFailedTrap':ruckusSCGClusterBackupFailedTrap,'ruckusSCGClusterRestoreFailedTrap':ruckusSCGClusterRestoreFailedTrap,'ruckusSCGClusterAppStoppedTrap':ruckusSCGClusterAppStoppedTrap,'ruckusSCGNodeBondInterfaceDownTrap':ruckusSCGNodeBondInterfaceDownTrap,'ruckusSCGNodePhyInterfaceDownTrap':ruckusSCGNodePhyInterfaceDownTrap,'ruckusSCGClusterLeaderChangedTrap':ruckusSCGClusterLeaderChangedTrap,'ruckusSCGClusterUpgradeSuccessTrap':ruckusSCGClusterUpgradeSuccessTrap,'ruckusSCGNodeBondInterfaceUpTrap':ruckusSCGNodeBondInterfaceUpTrap,'ruckusSCGNodePhyInterfaceUpTrap':ruckusSCGNodePhyInterfaceUpTrap,'ruckusSCGClusterBackToInServiceTrap':ruckusSCGClusterBackToInServiceTrap,'ruckusSCGBackupClusterSuccessTrap':ruckusSCGBackupClusterSuccessTrap,'ruckusSCGNodeJoinSuccessTrap':ruckusSCGNodeJoinSuccessTrap,'ruckusSCGClusterAppStartTrap':ruckusSCGClusterAppStartTrap,'ruckusSCGNodeRemoveSuccessTrap':ruckusSCGNodeRemoveSuccessTrap,'ruckusSCGClusterRestoreSuccessTrap':ruckusSCGClusterRestoreSuccessTrap,'ruckusSCGNodeBackToInServiceTrap':ruckusSCGNodeBackToInServiceTrap,'ruckusSCGSshTunnelSwitchedTrap':ruckusSCGSshTunnelSwitchedTrap,'ruckusSCGClusterCfgBackupStartTrap':ruckusSCGClusterCfgBackupStartTrap,'ruckusSCGClusterCfgBackupSuccessTrap':ruckusSCGClusterCfgBackupSuccessTrap,'ruckusSCGClusterCfgBackupFailedTrap':ruckusSCGClusterCfgBackupFailedTrap,'ruckusSCGClusterCfgRestoreSuccessTrap':ruckusSCGClusterCfgRestoreSuccessTrap,'ruckusSCGClusterCfgRestoreFailedTrap':ruckusSCGClusterCfgRestoreFailedTrap,'ruckusSCGClusterUploadSuccessTrap':ruckusSCGClusterUploadSuccessTrap,'ruckusSCGClusterUploadFailedTrap':ruckusSCGClusterUploadFailedTrap,'ruckusSCGClusterOutOfServiceTrap':ruckusSCGClusterOutOfServiceTrap,'ruckusSCGClusterUploadVDPFirmwareStartTrap':ruckusSCGClusterUploadVDPFirmwareStartTrap,'ruckusSCGClusterUploadVDPFirmwareSuccessTrap':ruckusSCGClusterUploadVDPFirmwareSuccessTrap,'ruckusSCGClusterUploadVDPFirmwareFailedTrap':ruckusSCGClusterUploadVDPFirmwareFailedTrap,'ruckusSCGIpmiVotageTrap':ruckusSCGIpmiVotageTrap,'ruckusSCGIpmiTempBBTrap':ruckusSCGIpmiTempBBTrap,'ruckusSCGIpmiTempFPTrap':ruckusSCGIpmiTempFPTrap,'ruckusSCGIpmiTempIOHTrap':ruckusSCGIpmiTempIOHTrap,'ruckusSCGIpmiTempMemPTrap':ruckusSCGIpmiTempMemPTrap,'ruckusSCGIpmiTempPSTrap':ruckusSCGIpmiTempPSTrap,'ruckusSCGIpmiTempPTrap':ruckusSCGIpmiTempPTrap,'ruckusSCGIpmiTempHSBPTrap':ruckusSCGIpmiTempHSBPTrap,'ruckusSCGIpmiFanTrap':ruckusSCGIpmiFanTrap,'ruckusSCGIpmiPowerTrap':ruckusSCGIpmiPowerTrap,'ruckusSCGIpmiCurrentTrap':ruckusSCGIpmiCurrentTrap,'ruckusSCGIpmiFanStatusTrap':ruckusSCGIpmiFanStatusTrap,'ruckusSCGIpmiPsStatusTrap':ruckusSCGIpmiPsStatusTrap,'ruckusSCGIpmiDrvStatusTrap':ruckusSCGIpmiDrvStatusTrap,'ruckusSCGIpmiREVotageTrap':ruckusSCGIpmiREVotageTrap,'ruckusSCGIpmiRETempBBTrap':ruckusSCGIpmiRETempBBTrap,'ruckusSCGIpmiRETempFPTrap':ruckusSCGIpmiRETempFPTrap,'ruckusSCGIpmiRETempIOHTrap':ruckusSCGIpmiRETempIOHTrap,'ruckusSCGIpmiRETempMemPTrap':ruckusSCGIpmiRETempMemPTrap,'ruckusSCGIpmiRETempPSTrap':ruckusSCGIpmiRETempPSTrap,'ruckusSCGIpmiRETempPTrap':ruckusSCGIpmiRETempPTrap,'ruckusSCGIpmiRETempHSBPTrap':ruckusSCGIpmiRETempHSBPTrap,'ruckusSCGIpmiREFanTrap':ruckusSCGIpmiREFanTrap,'ruckusSCGIpmiREPowerTrap':ruckusSCGIpmiREPowerTrap,'ruckusSCGIpmiRECurrentTrap':ruckusSCGIpmiRECurrentTrap,'ruckusSCGIpmiREFanStatusTrap':ruckusSCGIpmiREFanStatusTrap,'ruckusSCGIpmiREPsStatusTrap':ruckusSCGIpmiREPsStatusTrap,'ruckusSCGIpmiREDrvStatusTrap':ruckusSCGIpmiREDrvStatusTrap,'ruckusSCGFtpTransferErrorTrap':ruckusSCGFtpTransferErrorTrap,'ruckusSCGSystemLBSConnectSuccessTrap':ruckusSCGSystemLBSConnectSuccessTrap,'ruckusSCGSystemLBSNoResponseTrap':ruckusSCGSystemLBSNoResponseTrap,'ruckusSCGSystemLBSAuthFailedTrap':ruckusSCGSystemLBSAuthFailedTrap,'ruckusSCGSystemLBSConnectFailedTrap':ruckusSCGSystemLBSConnectFailedTrap,'ruckusSCGProcessRestartTrap':ruckusSCGProcessRestartTrap,'ruckusSCGServiceUnavailableTrap':ruckusSCGServiceUnavailableTrap,'ruckusSCGKeepAliveFailureTrap':ruckusSCGKeepAliveFailureTrap,'ruckusSCGResourceUnavailableTrap':ruckusSCGResourceUnavailableTrap,'ruckusSCGSmfRegFailedTrap':ruckusSCGSmfRegFailedTrap,'ruckusSCGHipFailoverTrap':ruckusSCGHipFailoverTrap,'ruckusSCGConfUpdFailedTrap':ruckusSCGConfUpdFailedTrap,'ruckusSCGConfRcvFailedTrap':ruckusSCGConfRcvFailedTrap,'ruckusSCGLostCnxnToDbladeTrap':ruckusSCGLostCnxnToDbladeTrap,'ruckusSCGGgsnRestartedTrap':ruckusSCGGgsnRestartedTrap,'ruckusSCGGgsnNotReachableTrap':ruckusSCGGgsnNotReachableTrap,'ruckusSCGGgsnNotResolvedTrap':ruckusSCGGgsnNotResolvedTrap,'ruckusSCGUnknownUETrap':ruckusSCGUnknownUETrap,'ruckusSCGAuthSrvrNotReachableTrap':ruckusSCGAuthSrvrNotReachableTrap,'ruckusSCGAccSrvrNotReachableTrap':ruckusSCGAccSrvrNotReachableTrap,'ruckusSCGUnknownRealmTrap':ruckusSCGUnknownRealmTrap,'ruckusSCGAuthFailedNonPermanentIDTrap':ruckusSCGAuthFailedNonPermanentIDTrap,'ruckusSCGCnxnToCgfFailedTrap':ruckusSCGCnxnToCgfFailedTrap,'ruckusSCGCdrTransferFailedTrap':ruckusSCGCdrTransferFailedTrap,'ruckusSCGCdrGenerateFailedTrap':ruckusSCGCdrGenerateFailedTrap,'ruckusSCGDestNotRecheableTrap':ruckusSCGDestNotRecheableTrap,'ruckusSCGAppServerDownTrap':ruckusSCGAppServerDownTrap,'ruckusSCGAppServerInactiveTrap':ruckusSCGAppServerInactiveTrap,'ruckusSCGAssocCantStartTrap':ruckusSCGAssocCantStartTrap,'ruckusSCGAssocDownTrap':ruckusSCGAssocDownTrap,'ruckusSCGOutboundRoutingFailedTrap':ruckusSCGOutboundRoutingFailedTrap,'ruckusSCGDidAllocationFailureTrap':ruckusSCGDidAllocationFailureTrap,'ruckusSCGPdnGwUnresolvedTrap':ruckusSCGPdnGwUnresolvedTrap,'ruckusSCGPdnGwVersionUnsupportedTrap':ruckusSCGPdnGwVersionUnsupportedTrap,'ruckusSCGPdnGwAssociationDownTrap':ruckusSCGPdnGwAssociationDownTrap,'ruckusSCGCreateSessionResponseFailedTrap':ruckusSCGCreateSessionResponseFailedTrap,'ruckusSCGDecodeFailedTrap':ruckusSCGDecodeFailedTrap,'ruckusSCGModifyBearerResponseFailedTrap':ruckusSCGModifyBearerResponseFailedTrap,'ruckusSCGDeleteSessionResponseFailedTrap':ruckusSCGDeleteSessionResponseFailedTrap,'ruckusSCGDeleteBearerRequestFailedTrap':ruckusSCGDeleteBearerRequestFailedTrap,'ruckusSCGUpdateBearerRequestFailedTrap':ruckusSCGUpdateBearerRequestFailedTrap,'ruckusSCGCgfServerNotConfiguredTrap':ruckusSCGCgfServerNotConfiguredTrap,'ruckusSCGTtgSessionCriticalThresholdTrap':ruckusSCGTtgSessionCriticalThresholdTrap,'ruckusSCGTtgSessionLicenseInsufficientTrap':ruckusSCGTtgSessionLicenseInsufficientTrap,'ruckusSCGAPAcctMsgMandatoryPrmMissingTrap':ruckusSCGAPAcctMsgMandatoryPrmMissingTrap,'ruckusSCGAcctUnknownRealmTrap':ruckusSCGAcctUnknownRealmTrap,'ruckusSCGAPAcctMsgDecodeFailedTrap':ruckusSCGAPAcctMsgDecodeFailedTrap,'ruckusSCGAPAcctRespWhileInvalidConfigTrap':ruckusSCGAPAcctRespWhileInvalidConfigTrap,'ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap':ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap,'ruckusSCGUnauthorizedCoaDmMessageDroppedTrap':ruckusSCGUnauthorizedCoaDmMessageDroppedTrap,'ruckusSCGConnectedToDbladeTrap':ruckusSCGConnectedToDbladeTrap,'ruckusSCGDestAvailableTrap':ruckusSCGDestAvailableTrap,'ruckusSCGAppServerActiveTrap':ruckusSCGAppServerActiveTrap,'ruckusSCGAssocUpTrap':ruckusSCGAssocUpTrap,'ruckusSCGSessUpdatedAtDbladeTrap':ruckusSCGSessUpdatedAtDbladeTrap,'ruckusSCGSessUpdateErrAtDbladeTrap':ruckusSCGSessUpdateErrAtDbladeTrap,'ruckusSCGSessDeletedAtDbladeTrap':ruckusSCGSessDeletedAtDbladeTrap,'ruckusSCGSessDeleteErrAtDbladeTrap':ruckusSCGSessDeleteErrAtDbladeTrap,'ruckusSCGLicenseSyncSuccessTrap':ruckusSCGLicenseSyncSuccessTrap,'ruckusSCGLicenseSyncFailedTrap':ruckusSCGLicenseSyncFailedTrap,'ruckusSCGLicenseImportSuccessTrap':ruckusSCGLicenseImportSuccessTrap,'ruckusSCGLicenseImportFailedTrap':ruckusSCGLicenseImportFailedTrap,'ruckusSCGSyslogServerReachableTrap':ruckusSCGSyslogServerReachableTrap,'ruckusSCGSyslogServerUnreachableTrap':ruckusSCGSyslogServerUnreachableTrap,'ruckusSCGSyslogServerSwitchedTrap':ruckusSCGSyslogServerSwitchedTrap,'ruckusSCGAPRadiusServerReachableTrap':ruckusSCGAPRadiusServerReachableTrap,'ruckusSCGAPRadiusServerUnreachableTrap':ruckusSCGAPRadiusServerUnreachableTrap,'ruckusSCGAPLDAPServerReachableTrap':ruckusSCGAPLDAPServerReachableTrap,'ruckusSCGAPLDAPServerUnreachableTrap':ruckusSCGAPLDAPServerUnreachableTrap,'ruckusSCGAPADServerReachableTrap':ruckusSCGAPADServerReachableTrap,'ruckusSCGAPADServerUnreachableTrap':ruckusSCGAPADServerUnreachableTrap,'ruckusSCGAPUsbSoftwarePackageDownloadedTrap':ruckusSCGAPUsbSoftwarePackageDownloadedTrap,'ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap':ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap,'ruckusSCGEspAuthServerReachableTrap':ruckusSCGEspAuthServerReachableTrap,'ruckusSCGEspAuthServerUnreachableTrap':ruckusSCGEspAuthServerUnreachableTrap,'ruckusSCGEspAuthServerResolvableTrap':ruckusSCGEspAuthServerResolvableTrap,'ruckusSCGEspAuthServerUnResolvableTrap':ruckusSCGEspAuthServerUnResolvableTrap,'ruckusSCGEspDNATServerReachableTrap':ruckusSCGEspDNATServerReachableTrap,'ruckusSCGEspDNATServerUnreachableTrap':ruckusSCGEspDNATServerUnreachableTrap,'ruckusSCGEspDNATServerResolvableTrap':ruckusSCGEspDNATServerResolvableTrap,'ruckusSCGEspDNATServerUnresolvableTrap':ruckusSCGEspDNATServerUnresolvableTrap,'ruckusRateLimitTORSurpassedTrap':ruckusRateLimitTORSurpassedTrap,'ruckusSCGIPSecTunnelAssociatedTrap':ruckusSCGIPSecTunnelAssociatedTrap,'ruckusSCGIPSecTunnelDisassociatedTrap':ruckusSCGIPSecTunnelDisassociatedTrap,'ruckusSCGIPSecTunnelAssociateFailedTrap':ruckusSCGIPSecTunnelAssociateFailedTrap,'ruckusSCGPmipProcessInitTrap':ruckusSCGPmipProcessInitTrap,'ruckusSCGPmipUnavailableTrap':ruckusSCGPmipUnavailableTrap,'ruckusSCGPmipUnallocatedMemoryTrap':ruckusSCGPmipUnallocatedMemoryTrap,'ruckusSCGPmipUpdateCgfFailedTrap':ruckusSCGPmipUpdateCgfFailedTrap,'ruckusSCGPmipLMAIcmpUnreachableTrap':ruckusSCGPmipLMAIcmpUnreachableTrap,'ruckusSCGPmipLMAFailOverTrap':ruckusSCGPmipLMAFailOverTrap,'ruckusSCGPmipBindingFailureTrap':ruckusSCGPmipBindingFailureTrap,'ruckusSCGPmiplostCnxnToDHCPTrap':ruckusSCGPmiplostCnxnToDHCPTrap,'ruckusSCGPmipLMAIcmpReachableTrap':ruckusSCGPmipLMAIcmpReachableTrap,'ruckusSCGPmipBindingSuccessTrap':ruckusSCGPmipBindingSuccessTrap,'ruckusSCGPmipConnectedToDHCPTrap':ruckusSCGPmipConnectedToDHCPTrap,'ruckusSCGPmipProcessStoppedTrap':ruckusSCGPmipProcessStoppedTrap,'ruckusSCGEventObjects':ruckusSCGEventObjects,_s:ruckusSCGEventDescription,_S:ruckusSCGClusterName,_E:ruckusSCGEventCode,_g:ruckusSCGProcessName,_W:ruckusSCGEventCtrlIP,_C:ruckusSCGEventSeverity,_D:ruckusSCGEventType,_P:ruckusSCGEventNodeMgmtIp,_R:ruckusSCGEventNodeName,_A7:ruckusSCGCPUPerc,_A8:ruckusSCGMemoryPerc,_A9:ruckusSCGDiskPerc,_F:ruckusSCGEventMacAddr,_t:ruckusSCGEventFirmwareVersion,_u:ruckusSCGEventUpgradedFirmwareVersion,_I:ruckusSCGEventAPMacAddr,_T:ruckusSCGEventReason,_K:ruckusSCGEventAPName,_H:ruckusSCGEventAPIP,_L:ruckusSCGEventAPLocation,_N:ruckusSCGEventAPGPSCoordinates,_M:ruckusSCGEventAPDescription,_O:ruckusSCGEventZoneName,_AB:ruckusSCGAPModel,_AC:ruckusSCGConfigAPModel,_AA:ruckusSCGAPConfigID,_AV:ruckusSCGEventTargetZoneName,_J:ruckusSCGEventAPIPv6,_Z:ruckusSCGLBSURL,_a:ruckusSCGLBSPort,_j:ruckusSCGEventSSID,_f:ruckusSCGEventRogueMac,_AD:ruckusPrimaryGRE,_AE:ruckusSecondaryGRE,_AZ:ruckusSoftGREGatewayList,_k:ruckusSCGSoftGREGWAddress,_AH:ruckusSCGEventClientMacAddr,_Q:ruckusSCGDPKey,_AF:ruckusSCGDPConfigID,_Y:ruckusSCGDPIP,_v:ruckusSCGDPPacketPoolID,_AG:ruckusSCGNetworkPortID,_m:ruckusSCGNetworkInterface,_Aa:ruckusSCGSwitchStatus,_V:ruckusSCGTemperatureStatus,_n:ruckusSCGProcessorId,_o:ruckusSCGFanId,_p:ruckusSCGFanStatus,_b:ruckusSCGPsId,_h:ruckusSCGPsStatus,_AI:ruckusSCGDrvId,_AJ:ruckusSCGDrvStatus,_AT:ruckusSCGLicenseType,_AU:ruckusSCGLicenseUsagePerc,_AN:ruckusSCGLicenseServerName,_A5:ruckusSCGIPSecGWAddress,_AO:ruckusSCGSyslogServerAddress,_Ah:ruckusSCGSrcSyslogServerAddress,_Ai:ruckusSCGDestSyslogServerAddress,_Ab:ruckusSCGFtpIp,_Ac:ruckusSCGFtpPort,_U:ruckusSCGSrcProcess,_w:ruckusSCGGgsnIp,_AK:ruckusSCGGtpcIp,_AL:ruckusSCGApn,_X:ruckusSCGUEImsi,_c:ruckusSCGUEMsisdn,_x:ruckusSCGAuthSrvrIp,_AM:ruckusSCGRadProxyIp,_Ae:ruckusSCGAccSrvrIp,_i:ruckusSCGRealm,_y:ruckusSCGCgfSrvrIp,_e:ruckusSCGRadSrvrIp,'ruckusSCGCipIp':ruckusSCGCipIp,_l:ruckusSCGPointCode,'ruckusSCGCongLevel':ruckusSCGCongLevel,_A0:ruckusSCGSSN,_z:ruckusSCGRoutingContext,_A1:ruckusSCGSrcIP,_A2:ruckusSCGSrcPort,_A3:ruckusSCGDestIP,_A4:ruckusSCGDestPort,_Af:ruckusSCGOperation,_Ag:ruckusSCGHlrInstance,_q:ruckusSCGUserName,_d:ruckusSCGPgwIp,_Ad:ruckusSCGFileName,_AP:ruckusSCGLDAPSrvrIp,_AQ:ruckusSCGADSrvrIp,_AR:ruckusSCGSoftwareName,_r:ruckusSCGDomainName,_AS:ruckusSCGDNATIp,_A6:ruckusSCGLMAIp,_AW:ruckusSCGEventRoguePolicyName,_AX:ruckusSCGEventRogueRuleName,_AY:ruckusSCGEventRogueType})