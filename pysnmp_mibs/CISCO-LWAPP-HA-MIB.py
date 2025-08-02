_Am='ciscoLwappMcRmiConfigGroup'
_Al='cLHaPeerHotStandbyTrap'
_Ak='cLHaBulkSyncCompleteTrap'
_Aj='cLHaRFSwapInfoTrap'
_Ai='cLHaSecondaryControllerUsageTrap'
_Ah='cLMcRmiGatewayFailoverInterval'
_Ag='cLMcRmiGatewayFailover'
_Af='cLMcRmiChassisBIp'
_Ae='cLMcRmiChassisBIpAddrType'
_Ad='cLMcRmiChassisBNum'
_Ac='cLMcRmiChassisAIp'
_Ab='cLMcRmiChassisAIpAddrType'
_Aa='cLMcRmiChassisANum'
_AZ='cLMcRmiInterface'
_AY='cLMcRmiConfigAction'
_AX='cLMcHaKeepAliveRetryCount'
_AW='cLMcHaClearConfig'
_AV='cLMcHaChassisPriority'
_AU='cLMcHaKeepAliveTimeOut'
_AT='cLMcHaPortRemIp'
_AS='cLMcHaPortRemoteIpAddrType'
_AR='cLMcHaPortMask'
_AQ='cLMcHaPortLocIp'
_AP='cLMcHaPortLocIpAddrType'
_AO='cLMcHaPortName'
_AN='cLHaPowerSupply2Operational'
_AM='cLHaPowerSupply2Present'
_AL='cLHaPowerSupply1Operational'
_AK='cLHaPowerSupply1Present'
_AJ='cLHaAllCpuUsage'
_AI='cLHaTotalFreeInclMmap'
_AH='cLHaTotalUsedMmap'
_AG='cLHaTotalAllocatedInclMmap'
_AF='cLHaTopMostReleasableSpace'
_AE='cLHaTotalNotInUseSpace'
_AD='cLHaTotalAllocatedSpace'
_AC='cLHaSpaceInMmappedRegions'
_AB='cLHaMmappedRegions'
_AA='cLHaChunksFree'
_A9='cLHaAllocatedFromRtos'
_A8='cLHaUsedSystemMemory'
_A7='cLHaFreeSystemMemory'
_A6='cLHaTotalSystemMemory'
_A5='cLHaBulkSyncStatus'
_A4='cLHaAvgGwReachLatency'
_A3='cLHaAvgPeerReachLatency'
_A2='cLHaNetworkRoutePeerRowStatus'
_A1='cLHaNetworkRoutePeerTransferStatus'
_A0='cLHaNetworkRoutePeerGateway'
_z='cLHaNetworkRoutePeerGatewayType'
_y='cLHaNetworkRoutePeerIPNetmask'
_x='cLHaNetworkRoutePeerIPNetmaskType'
_w='cLHaPeerSearchTimeout'
_v='cLHaGwRetryCount'
_u='cLHaKARetryCount'
_t='cLHaKATimeout'
_s='cLHaRFStatusUnitIpType'
_r='cLHaNetworkFailOver'
_q='cLHaLinkEncryption'
_p='cLHaPrimaryUnit'
_o='cLHaVirtualMacAddress'
_n='cLHaPeerMacAddress'
_m='cLHaRedundancyIpAddress'
_l='cLHaRedundancyIpAddressType'
_k='cLHaServicePortPeerIpNetMask'
_j='cLHaServicePortPeerIpNetMaskType'
_i='cLHaServicePortPeerIpAddress'
_h='cLHaServicePortPeerIpAddressType'
_g='cLHaPeerIpAddressType'
_f='cLHaApSsoConfig'
_e='Microseconds'
_d='not-accessible'
_c='cLHaNetworkRoutePeerIPAddress'
_b='cLHaNetworkRoutePeerIPAddressType'
_a='sysName'
_Z='SNMPv2-MIB'
_Y='cRFStatusUnitState'
_X='cRFStatusPeerUnitState'
_W='ciscoLwappMcHaConfigGroup'
_V='ciscoLwappHaMIBNotificationGroup'
_U='ciscoLwappHaMIBNotificationVariableGroup'
_T='ciscoLwappHaStatisticsGroup'
_S='ciscoLwappHaNetworkConfigGroup'
_R='ciscoLwappHaGlobalConfigGroup'
_Q='cLHaPeerHotStandbyEvent'
_P='cLHaBulkSyncCompleteEvent'
_O='cLHaSecondaryControllerUsageDayCounter'
_N='cLHaSecondaryControllerUsageTrapType'
_M='cLHaRFStatusUnitIp'
_L='cLHaPeerIpAddress'
_K='SnmpAdminString'
_J='CISCO-RF-MIB'
_I='read-create'
_H='KBytes'
_G='TruthValue'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='current'
_A='CISCO-LWAPP-HA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cRFStatusPeerUnitState,cRFStatusUnitState=mibBuilder.importSymbols(_J,_X,_Y)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_Z,_a)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
ciscoLwappHaMIB=ModuleIdentity((1,3,6,1,4,1,9,9,843))
if mibBuilder.loadTexts:ciscoLwappHaMIB.setRevisions(('2020-06-07 00:00','2019-07-08 00:00','2017-11-08 00:00','2017-03-14 00:00'))
_CiscoLwappHaMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappHaMIBNotifs=_CiscoLwappHaMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,843,0))
_CiscoLwappHaMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappHaMIBObjects=_CiscoLwappHaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,843,1))
_CiscoLwappHaGlobalConfig_ObjectIdentity=ObjectIdentity
ciscoLwappHaGlobalConfig=_CiscoLwappHaGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,1))
class _CLHaApSsoConfig_Type(TruthValue):defaultValue=2
_CLHaApSsoConfig_Type.__name__=_G
_CLHaApSsoConfig_Object=MibScalar
cLHaApSsoConfig=_CLHaApSsoConfig_Object((1,3,6,1,4,1,9,9,843,1,1,1),_CLHaApSsoConfig_Type())
cLHaApSsoConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaApSsoConfig.setStatus(_B)
_CLHaPeerIpAddressType_Type=InetAddressType
_CLHaPeerIpAddressType_Object=MibScalar
cLHaPeerIpAddressType=_CLHaPeerIpAddressType_Object((1,3,6,1,4,1,9,9,843,1,1,2),_CLHaPeerIpAddressType_Type())
cLHaPeerIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaPeerIpAddressType.setStatus(_B)
_CLHaPeerIpAddress_Type=InetAddress
_CLHaPeerIpAddress_Object=MibScalar
cLHaPeerIpAddress=_CLHaPeerIpAddress_Object((1,3,6,1,4,1,9,9,843,1,1,3),_CLHaPeerIpAddress_Type())
cLHaPeerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaPeerIpAddress.setStatus(_B)
_CLHaServicePortPeerIpAddressType_Type=InetAddressType
_CLHaServicePortPeerIpAddressType_Object=MibScalar
cLHaServicePortPeerIpAddressType=_CLHaServicePortPeerIpAddressType_Object((1,3,6,1,4,1,9,9,843,1,1,4),_CLHaServicePortPeerIpAddressType_Type())
cLHaServicePortPeerIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaServicePortPeerIpAddressType.setStatus(_B)
_CLHaServicePortPeerIpAddress_Type=InetAddress
_CLHaServicePortPeerIpAddress_Object=MibScalar
cLHaServicePortPeerIpAddress=_CLHaServicePortPeerIpAddress_Object((1,3,6,1,4,1,9,9,843,1,1,5),_CLHaServicePortPeerIpAddress_Type())
cLHaServicePortPeerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaServicePortPeerIpAddress.setStatus(_B)
_CLHaServicePortPeerIpNetMaskType_Type=InetAddressType
_CLHaServicePortPeerIpNetMaskType_Object=MibScalar
cLHaServicePortPeerIpNetMaskType=_CLHaServicePortPeerIpNetMaskType_Object((1,3,6,1,4,1,9,9,843,1,1,6),_CLHaServicePortPeerIpNetMaskType_Type())
cLHaServicePortPeerIpNetMaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaServicePortPeerIpNetMaskType.setStatus(_B)
_CLHaServicePortPeerIpNetMask_Type=InetAddress
_CLHaServicePortPeerIpNetMask_Object=MibScalar
cLHaServicePortPeerIpNetMask=_CLHaServicePortPeerIpNetMask_Object((1,3,6,1,4,1,9,9,843,1,1,7),_CLHaServicePortPeerIpNetMask_Type())
cLHaServicePortPeerIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaServicePortPeerIpNetMask.setStatus(_B)
_CLHaRedundancyIpAddressType_Type=InetAddressType
_CLHaRedundancyIpAddressType_Object=MibScalar
cLHaRedundancyIpAddressType=_CLHaRedundancyIpAddressType_Object((1,3,6,1,4,1,9,9,843,1,1,8),_CLHaRedundancyIpAddressType_Type())
cLHaRedundancyIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaRedundancyIpAddressType.setStatus(_B)
_CLHaRedundancyIpAddress_Type=InetAddress
_CLHaRedundancyIpAddress_Object=MibScalar
cLHaRedundancyIpAddress=_CLHaRedundancyIpAddress_Object((1,3,6,1,4,1,9,9,843,1,1,9),_CLHaRedundancyIpAddress_Type())
cLHaRedundancyIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaRedundancyIpAddress.setStatus(_B)
_CLHaPeerMacAddress_Type=MacAddress
_CLHaPeerMacAddress_Object=MibScalar
cLHaPeerMacAddress=_CLHaPeerMacAddress_Object((1,3,6,1,4,1,9,9,843,1,1,10),_CLHaPeerMacAddress_Type())
cLHaPeerMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaPeerMacAddress.setStatus(_B)
_CLHaVirtualMacAddress_Type=MacAddress
_CLHaVirtualMacAddress_Object=MibScalar
cLHaVirtualMacAddress=_CLHaVirtualMacAddress_Object((1,3,6,1,4,1,9,9,843,1,1,11),_CLHaVirtualMacAddress_Type())
cLHaVirtualMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaVirtualMacAddress.setStatus(_B)
class _CLHaPrimaryUnit_Type(TruthValue):defaultValue=2
_CLHaPrimaryUnit_Type.__name__=_G
_CLHaPrimaryUnit_Object=MibScalar
cLHaPrimaryUnit=_CLHaPrimaryUnit_Object((1,3,6,1,4,1,9,9,843,1,1,12),_CLHaPrimaryUnit_Type())
cLHaPrimaryUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaPrimaryUnit.setStatus(_B)
class _CLHaLinkEncryption_Type(TruthValue):defaultValue=2
_CLHaLinkEncryption_Type.__name__=_G
_CLHaLinkEncryption_Object=MibScalar
cLHaLinkEncryption=_CLHaLinkEncryption_Object((1,3,6,1,4,1,9,9,843,1,1,13),_CLHaLinkEncryption_Type())
cLHaLinkEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaLinkEncryption.setStatus(_B)
class _CLHaNetworkFailOver_Type(TruthValue):defaultValue=2
_CLHaNetworkFailOver_Type.__name__=_G
_CLHaNetworkFailOver_Object=MibScalar
cLHaNetworkFailOver=_CLHaNetworkFailOver_Object((1,3,6,1,4,1,9,9,843,1,1,14),_CLHaNetworkFailOver_Type())
cLHaNetworkFailOver.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaNetworkFailOver.setStatus(_B)
_CLHaRFStatusUnitIp_Type=InetAddress
_CLHaRFStatusUnitIp_Object=MibScalar
cLHaRFStatusUnitIp=_CLHaRFStatusUnitIp_Object((1,3,6,1,4,1,9,9,843,1,1,15),_CLHaRFStatusUnitIp_Type())
cLHaRFStatusUnitIp.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaRFStatusUnitIp.setStatus(_B)
class _CLHaKATimeout_Type(Unsigned32):defaultValue=100
_CLHaKATimeout_Type.__name__=_F
_CLHaKATimeout_Object=MibScalar
cLHaKATimeout=_CLHaKATimeout_Object((1,3,6,1,4,1,9,9,843,1,1,16),_CLHaKATimeout_Type())
cLHaKATimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaKATimeout.setStatus(_B)
if mibBuilder.loadTexts:cLHaKATimeout.setUnits('milliseconds')
class _CLHaKARetryCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_CLHaKARetryCount_Type.__name__=_F
_CLHaKARetryCount_Object=MibScalar
cLHaKARetryCount=_CLHaKARetryCount_Object((1,3,6,1,4,1,9,9,843,1,1,17),_CLHaKARetryCount_Type())
cLHaKARetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaKARetryCount.setStatus(_B)
class _CLHaGwRetryCount_Type(Unsigned32):defaultValue=12;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,12))
_CLHaGwRetryCount_Type.__name__=_F
_CLHaGwRetryCount_Object=MibScalar
cLHaGwRetryCount=_CLHaGwRetryCount_Object((1,3,6,1,4,1,9,9,843,1,1,18),_CLHaGwRetryCount_Type())
cLHaGwRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaGwRetryCount.setStatus(_B)
class _CLHaPeerSearchTimeout_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_CLHaPeerSearchTimeout_Type.__name__=_F
_CLHaPeerSearchTimeout_Object=MibScalar
cLHaPeerSearchTimeout=_CLHaPeerSearchTimeout_Object((1,3,6,1,4,1,9,9,843,1,1,19),_CLHaPeerSearchTimeout_Type())
cLHaPeerSearchTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHaPeerSearchTimeout.setStatus(_B)
if mibBuilder.loadTexts:cLHaPeerSearchTimeout.setUnits('seconds')
_CLHaRFStatusUnitIpType_Type=InetAddressType
_CLHaRFStatusUnitIpType_Object=MibScalar
cLHaRFStatusUnitIpType=_CLHaRFStatusUnitIpType_Object((1,3,6,1,4,1,9,9,843,1,1,20),_CLHaRFStatusUnitIpType_Type())
cLHaRFStatusUnitIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaRFStatusUnitIpType.setStatus(_B)
_CiscoLwappHaNetworkConfig_ObjectIdentity=ObjectIdentity
ciscoLwappHaNetworkConfig=_CiscoLwappHaNetworkConfig_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,2))
_CLHaNetworkRoutePeerConfigTable_Object=MibTable
cLHaNetworkRoutePeerConfigTable=_CLHaNetworkRoutePeerConfigTable_Object((1,3,6,1,4,1,9,9,843,1,2,1))
if mibBuilder.loadTexts:cLHaNetworkRoutePeerConfigTable.setStatus(_B)
_CLHaNetworkRoutePeerConfigEntry_Object=MibTableRow
cLHaNetworkRoutePeerConfigEntry=_CLHaNetworkRoutePeerConfigEntry_Object((1,3,6,1,4,1,9,9,843,1,2,1,1))
cLHaNetworkRoutePeerConfigEntry.setIndexNames((0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:cLHaNetworkRoutePeerConfigEntry.setStatus(_B)
_CLHaNetworkRoutePeerIPAddressType_Type=InetAddressType
_CLHaNetworkRoutePeerIPAddressType_Object=MibTableColumn
cLHaNetworkRoutePeerIPAddressType=_CLHaNetworkRoutePeerIPAddressType_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,1),_CLHaNetworkRoutePeerIPAddressType_Type())
cLHaNetworkRoutePeerIPAddressType.setMaxAccess(_d)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerIPAddressType.setStatus(_B)
_CLHaNetworkRoutePeerIPAddress_Type=InetAddress
_CLHaNetworkRoutePeerIPAddress_Object=MibTableColumn
cLHaNetworkRoutePeerIPAddress=_CLHaNetworkRoutePeerIPAddress_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,2),_CLHaNetworkRoutePeerIPAddress_Type())
cLHaNetworkRoutePeerIPAddress.setMaxAccess(_d)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerIPAddress.setStatus(_B)
_CLHaNetworkRoutePeerIPNetmaskType_Type=InetAddressType
_CLHaNetworkRoutePeerIPNetmaskType_Object=MibTableColumn
cLHaNetworkRoutePeerIPNetmaskType=_CLHaNetworkRoutePeerIPNetmaskType_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,3),_CLHaNetworkRoutePeerIPNetmaskType_Type())
cLHaNetworkRoutePeerIPNetmaskType.setMaxAccess(_I)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerIPNetmaskType.setStatus(_B)
_CLHaNetworkRoutePeerIPNetmask_Type=InetAddress
_CLHaNetworkRoutePeerIPNetmask_Object=MibTableColumn
cLHaNetworkRoutePeerIPNetmask=_CLHaNetworkRoutePeerIPNetmask_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,4),_CLHaNetworkRoutePeerIPNetmask_Type())
cLHaNetworkRoutePeerIPNetmask.setMaxAccess(_I)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerIPNetmask.setStatus(_B)
_CLHaNetworkRoutePeerGatewayType_Type=InetAddressType
_CLHaNetworkRoutePeerGatewayType_Object=MibTableColumn
cLHaNetworkRoutePeerGatewayType=_CLHaNetworkRoutePeerGatewayType_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,5),_CLHaNetworkRoutePeerGatewayType_Type())
cLHaNetworkRoutePeerGatewayType.setMaxAccess(_I)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerGatewayType.setStatus(_B)
_CLHaNetworkRoutePeerGateway_Type=InetAddress
_CLHaNetworkRoutePeerGateway_Object=MibTableColumn
cLHaNetworkRoutePeerGateway=_CLHaNetworkRoutePeerGateway_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,6),_CLHaNetworkRoutePeerGateway_Type())
cLHaNetworkRoutePeerGateway.setMaxAccess(_I)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerGateway.setStatus(_B)
class _CLHaNetworkRoutePeerTransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('initiate',1),('inProgress',2),('success',3),('failure',4),('timeout',5)))
_CLHaNetworkRoutePeerTransferStatus_Type.__name__=_E
_CLHaNetworkRoutePeerTransferStatus_Object=MibTableColumn
cLHaNetworkRoutePeerTransferStatus=_CLHaNetworkRoutePeerTransferStatus_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,7),_CLHaNetworkRoutePeerTransferStatus_Type())
cLHaNetworkRoutePeerTransferStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerTransferStatus.setStatus(_B)
_CLHaNetworkRoutePeerRowStatus_Type=RowStatus
_CLHaNetworkRoutePeerRowStatus_Object=MibTableColumn
cLHaNetworkRoutePeerRowStatus=_CLHaNetworkRoutePeerRowStatus_Object((1,3,6,1,4,1,9,9,843,1,2,1,1,8),_CLHaNetworkRoutePeerRowStatus_Type())
cLHaNetworkRoutePeerRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:cLHaNetworkRoutePeerRowStatus.setStatus(_B)
_CiscoLwappHaNotificationVariable_ObjectIdentity=ObjectIdentity
ciscoLwappHaNotificationVariable=_CiscoLwappHaNotificationVariable_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,3))
class _CLHaSecondaryControllerUsageTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('usageStart',1),('usageComplete',2),('overUsage',3)))
_CLHaSecondaryControllerUsageTrapType_Type.__name__=_E
_CLHaSecondaryControllerUsageTrapType_Object=MibScalar
cLHaSecondaryControllerUsageTrapType=_CLHaSecondaryControllerUsageTrapType_Object((1,3,6,1,4,1,9,9,843,1,3,1),_CLHaSecondaryControllerUsageTrapType_Type())
cLHaSecondaryControllerUsageTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaSecondaryControllerUsageTrapType.setStatus(_B)
_CLHaSecondaryControllerUsageDayCounter_Type=Counter32
_CLHaSecondaryControllerUsageDayCounter_Object=MibScalar
cLHaSecondaryControllerUsageDayCounter=_CLHaSecondaryControllerUsageDayCounter_Object((1,3,6,1,4,1,9,9,843,1,3,2),_CLHaSecondaryControllerUsageDayCounter_Type())
cLHaSecondaryControllerUsageDayCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaSecondaryControllerUsageDayCounter.setStatus(_B)
class _CLHaBulkSyncCompleteEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('bulkSyncComplete',1))
_CLHaBulkSyncCompleteEvent_Type.__name__=_E
_CLHaBulkSyncCompleteEvent_Object=MibScalar
cLHaBulkSyncCompleteEvent=_CLHaBulkSyncCompleteEvent_Object((1,3,6,1,4,1,9,9,843,1,3,3),_CLHaBulkSyncCompleteEvent_Type())
cLHaBulkSyncCompleteEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaBulkSyncCompleteEvent.setStatus(_B)
class _CLHaPeerHotStandbyEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('haPeerHotstandby',1))
_CLHaPeerHotStandbyEvent_Type.__name__=_E
_CLHaPeerHotStandbyEvent_Object=MibScalar
cLHaPeerHotStandbyEvent=_CLHaPeerHotStandbyEvent_Object((1,3,6,1,4,1,9,9,843,1,3,4),_CLHaPeerHotStandbyEvent_Type())
cLHaPeerHotStandbyEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaPeerHotStandbyEvent.setStatus(_B)
_CiscoLwappHaPeerStatisticsVariable_ObjectIdentity=ObjectIdentity
ciscoLwappHaPeerStatisticsVariable=_CiscoLwappHaPeerStatisticsVariable_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,4))
_CiscoLwappHaSystemStatistics_ObjectIdentity=ObjectIdentity
ciscoLwappHaSystemStatistics=_CiscoLwappHaSystemStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,4,1))
_CiscoLwappHaCpuStatistics_ObjectIdentity=ObjectIdentity
ciscoLwappHaCpuStatistics=_CiscoLwappHaCpuStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,4,1,1))
class _CLHaAllCpuUsage_Type(SnmpAdminString):defaultValue=OctetString('')
_CLHaAllCpuUsage_Type.__name__=_K
_CLHaAllCpuUsage_Object=MibScalar
cLHaAllCpuUsage=_CLHaAllCpuUsage_Object((1,3,6,1,4,1,9,9,843,1,4,1,1,1),_CLHaAllCpuUsage_Type())
cLHaAllCpuUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaAllCpuUsage.setStatus(_B)
_CiscoLwappHaPowerSupplyStatistics_ObjectIdentity=ObjectIdentity
ciscoLwappHaPowerSupplyStatistics=_CiscoLwappHaPowerSupplyStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,4,1,2))
class _CLHaPowerSupply1Present_Type(TruthValue):defaultValue=2
_CLHaPowerSupply1Present_Type.__name__=_G
_CLHaPowerSupply1Present_Object=MibScalar
cLHaPowerSupply1Present=_CLHaPowerSupply1Present_Object((1,3,6,1,4,1,9,9,843,1,4,1,2,1),_CLHaPowerSupply1Present_Type())
cLHaPowerSupply1Present.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaPowerSupply1Present.setStatus(_B)
class _CLHaPowerSupply1Operational_Type(TruthValue):defaultValue=2
_CLHaPowerSupply1Operational_Type.__name__=_G
_CLHaPowerSupply1Operational_Object=MibScalar
cLHaPowerSupply1Operational=_CLHaPowerSupply1Operational_Object((1,3,6,1,4,1,9,9,843,1,4,1,2,2),_CLHaPowerSupply1Operational_Type())
cLHaPowerSupply1Operational.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaPowerSupply1Operational.setStatus(_B)
class _CLHaPowerSupply2Present_Type(TruthValue):defaultValue=2
_CLHaPowerSupply2Present_Type.__name__=_G
_CLHaPowerSupply2Present_Object=MibScalar
cLHaPowerSupply2Present=_CLHaPowerSupply2Present_Object((1,3,6,1,4,1,9,9,843,1,4,1,2,3),_CLHaPowerSupply2Present_Type())
cLHaPowerSupply2Present.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaPowerSupply2Present.setStatus(_B)
class _CLHaPowerSupply2Operational_Type(TruthValue):defaultValue=2
_CLHaPowerSupply2Operational_Type.__name__=_G
_CLHaPowerSupply2Operational_Object=MibScalar
cLHaPowerSupply2Operational=_CLHaPowerSupply2Operational_Object((1,3,6,1,4,1,9,9,843,1,4,1,2,4),_CLHaPowerSupply2Operational_Type())
cLHaPowerSupply2Operational.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaPowerSupply2Operational.setStatus(_B)
_CiscoLwappHaMemoryStatistics_ObjectIdentity=ObjectIdentity
ciscoLwappHaMemoryStatistics=_CiscoLwappHaMemoryStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,4,1,3))
class _CLHaTotalSystemMemory_Type(Integer32):defaultValue=0
_CLHaTotalSystemMemory_Type.__name__=_E
_CLHaTotalSystemMemory_Object=MibScalar
cLHaTotalSystemMemory=_CLHaTotalSystemMemory_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,1),_CLHaTotalSystemMemory_Type())
cLHaTotalSystemMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTotalSystemMemory.setStatus(_B)
if mibBuilder.loadTexts:cLHaTotalSystemMemory.setUnits(_H)
class _CLHaFreeSystemMemory_Type(Integer32):defaultValue=0
_CLHaFreeSystemMemory_Type.__name__=_E
_CLHaFreeSystemMemory_Object=MibScalar
cLHaFreeSystemMemory=_CLHaFreeSystemMemory_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,2),_CLHaFreeSystemMemory_Type())
cLHaFreeSystemMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaFreeSystemMemory.setStatus(_B)
if mibBuilder.loadTexts:cLHaFreeSystemMemory.setUnits(_H)
class _CLHaUsedSystemMemory_Type(Integer32):defaultValue=0
_CLHaUsedSystemMemory_Type.__name__=_E
_CLHaUsedSystemMemory_Object=MibScalar
cLHaUsedSystemMemory=_CLHaUsedSystemMemory_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,3),_CLHaUsedSystemMemory_Type())
cLHaUsedSystemMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaUsedSystemMemory.setStatus(_B)
if mibBuilder.loadTexts:cLHaUsedSystemMemory.setUnits(_H)
class _CLHaAllocatedFromRtos_Type(Integer32):defaultValue=0
_CLHaAllocatedFromRtos_Type.__name__=_E
_CLHaAllocatedFromRtos_Object=MibScalar
cLHaAllocatedFromRtos=_CLHaAllocatedFromRtos_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,4),_CLHaAllocatedFromRtos_Type())
cLHaAllocatedFromRtos.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaAllocatedFromRtos.setStatus(_B)
if mibBuilder.loadTexts:cLHaAllocatedFromRtos.setUnits(_H)
class _CLHaChunksFree_Type(Integer32):defaultValue=0
_CLHaChunksFree_Type.__name__=_E
_CLHaChunksFree_Object=MibScalar
cLHaChunksFree=_CLHaChunksFree_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,5),_CLHaChunksFree_Type())
cLHaChunksFree.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaChunksFree.setStatus(_B)
class _CLHaMmappedRegions_Type(Integer32):defaultValue=0
_CLHaMmappedRegions_Type.__name__=_E
_CLHaMmappedRegions_Object=MibScalar
cLHaMmappedRegions=_CLHaMmappedRegions_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,6),_CLHaMmappedRegions_Type())
cLHaMmappedRegions.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaMmappedRegions.setStatus(_B)
class _CLHaSpaceInMmappedRegions_Type(Integer32):defaultValue=0
_CLHaSpaceInMmappedRegions_Type.__name__=_E
_CLHaSpaceInMmappedRegions_Object=MibScalar
cLHaSpaceInMmappedRegions=_CLHaSpaceInMmappedRegions_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,7),_CLHaSpaceInMmappedRegions_Type())
cLHaSpaceInMmappedRegions.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaSpaceInMmappedRegions.setStatus(_B)
if mibBuilder.loadTexts:cLHaSpaceInMmappedRegions.setUnits(_H)
class _CLHaTotalAllocatedSpace_Type(Integer32):defaultValue=0
_CLHaTotalAllocatedSpace_Type.__name__=_E
_CLHaTotalAllocatedSpace_Object=MibScalar
cLHaTotalAllocatedSpace=_CLHaTotalAllocatedSpace_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,8),_CLHaTotalAllocatedSpace_Type())
cLHaTotalAllocatedSpace.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTotalAllocatedSpace.setStatus(_B)
if mibBuilder.loadTexts:cLHaTotalAllocatedSpace.setUnits(_H)
class _CLHaTotalNotInUseSpace_Type(Integer32):defaultValue=0
_CLHaTotalNotInUseSpace_Type.__name__=_E
_CLHaTotalNotInUseSpace_Object=MibScalar
cLHaTotalNotInUseSpace=_CLHaTotalNotInUseSpace_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,9),_CLHaTotalNotInUseSpace_Type())
cLHaTotalNotInUseSpace.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTotalNotInUseSpace.setStatus(_B)
if mibBuilder.loadTexts:cLHaTotalNotInUseSpace.setUnits(_H)
class _CLHaTopMostReleasableSpace_Type(Integer32):defaultValue=0
_CLHaTopMostReleasableSpace_Type.__name__=_E
_CLHaTopMostReleasableSpace_Object=MibScalar
cLHaTopMostReleasableSpace=_CLHaTopMostReleasableSpace_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,10),_CLHaTopMostReleasableSpace_Type())
cLHaTopMostReleasableSpace.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTopMostReleasableSpace.setStatus(_B)
if mibBuilder.loadTexts:cLHaTopMostReleasableSpace.setUnits(_H)
class _CLHaTotalAllocatedInclMmap_Type(Integer32):defaultValue=0
_CLHaTotalAllocatedInclMmap_Type.__name__=_E
_CLHaTotalAllocatedInclMmap_Object=MibScalar
cLHaTotalAllocatedInclMmap=_CLHaTotalAllocatedInclMmap_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,11),_CLHaTotalAllocatedInclMmap_Type())
cLHaTotalAllocatedInclMmap.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTotalAllocatedInclMmap.setStatus(_B)
if mibBuilder.loadTexts:cLHaTotalAllocatedInclMmap.setUnits(_H)
class _CLHaTotalUsedMmap_Type(Integer32):defaultValue=0
_CLHaTotalUsedMmap_Type.__name__=_E
_CLHaTotalUsedMmap_Object=MibScalar
cLHaTotalUsedMmap=_CLHaTotalUsedMmap_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,12),_CLHaTotalUsedMmap_Type())
cLHaTotalUsedMmap.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTotalUsedMmap.setStatus(_B)
if mibBuilder.loadTexts:cLHaTotalUsedMmap.setUnits(_H)
class _CLHaTotalFreeInclMmap_Type(Integer32):defaultValue=0
_CLHaTotalFreeInclMmap_Type.__name__=_E
_CLHaTotalFreeInclMmap_Object=MibScalar
cLHaTotalFreeInclMmap=_CLHaTotalFreeInclMmap_Object((1,3,6,1,4,1,9,9,843,1,4,1,3,13),_CLHaTotalFreeInclMmap_Type())
cLHaTotalFreeInclMmap.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaTotalFreeInclMmap.setStatus(_B)
if mibBuilder.loadTexts:cLHaTotalFreeInclMmap.setUnits(_H)
_CiscoLwappHaStatisticsVariable_ObjectIdentity=ObjectIdentity
ciscoLwappHaStatisticsVariable=_CiscoLwappHaStatisticsVariable_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,5))
class _CLHaAvgPeerReachLatency_Type(Integer32):defaultValue=0
_CLHaAvgPeerReachLatency_Type.__name__=_E
_CLHaAvgPeerReachLatency_Object=MibScalar
cLHaAvgPeerReachLatency=_CLHaAvgPeerReachLatency_Object((1,3,6,1,4,1,9,9,843,1,5,1),_CLHaAvgPeerReachLatency_Type())
cLHaAvgPeerReachLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaAvgPeerReachLatency.setStatus(_B)
if mibBuilder.loadTexts:cLHaAvgPeerReachLatency.setUnits(_e)
class _CLHaAvgGwReachLatency_Type(Integer32):defaultValue=0
_CLHaAvgGwReachLatency_Type.__name__=_E
_CLHaAvgGwReachLatency_Object=MibScalar
cLHaAvgGwReachLatency=_CLHaAvgGwReachLatency_Object((1,3,6,1,4,1,9,9,843,1,5,2),_CLHaAvgGwReachLatency_Type())
cLHaAvgGwReachLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaAvgGwReachLatency.setStatus(_B)
if mibBuilder.loadTexts:cLHaAvgGwReachLatency.setUnits(_e)
class _CLHaBulkSyncStatus_Type(SnmpAdminString):defaultValue=OctetString('')
_CLHaBulkSyncStatus_Type.__name__=_K
_CLHaBulkSyncStatus_Object=MibScalar
cLHaBulkSyncStatus=_CLHaBulkSyncStatus_Object((1,3,6,1,4,1,9,9,843,1,5,3),_CLHaBulkSyncStatus_Type())
cLHaBulkSyncStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cLHaBulkSyncStatus.setStatus(_B)
_CiscoLwappMcHaConfig_ObjectIdentity=ObjectIdentity
ciscoLwappMcHaConfig=_CiscoLwappMcHaConfig_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,6))
_CLMcHaPortName_Type=DisplayString
_CLMcHaPortName_Object=MibScalar
cLMcHaPortName=_CLMcHaPortName_Object((1,3,6,1,4,1,9,9,843,1,6,1),_CLMcHaPortName_Type())
cLMcHaPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaPortName.setStatus(_B)
_CLMcHaPortLocIpAddrType_Type=InetAddressType
_CLMcHaPortLocIpAddrType_Object=MibScalar
cLMcHaPortLocIpAddrType=_CLMcHaPortLocIpAddrType_Object((1,3,6,1,4,1,9,9,843,1,6,2),_CLMcHaPortLocIpAddrType_Type())
cLMcHaPortLocIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaPortLocIpAddrType.setStatus(_B)
_CLMcHaPortLocIp_Type=InetAddress
_CLMcHaPortLocIp_Object=MibScalar
cLMcHaPortLocIp=_CLMcHaPortLocIp_Object((1,3,6,1,4,1,9,9,843,1,6,3),_CLMcHaPortLocIp_Type())
cLMcHaPortLocIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaPortLocIp.setStatus(_B)
_CLMcHaPortMask_Type=InetAddress
_CLMcHaPortMask_Object=MibScalar
cLMcHaPortMask=_CLMcHaPortMask_Object((1,3,6,1,4,1,9,9,843,1,6,4),_CLMcHaPortMask_Type())
cLMcHaPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaPortMask.setStatus(_B)
_CLMcHaPortRemoteIpAddrType_Type=InetAddressType
_CLMcHaPortRemoteIpAddrType_Object=MibScalar
cLMcHaPortRemoteIpAddrType=_CLMcHaPortRemoteIpAddrType_Object((1,3,6,1,4,1,9,9,843,1,6,5),_CLMcHaPortRemoteIpAddrType_Type())
cLMcHaPortRemoteIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaPortRemoteIpAddrType.setStatus(_B)
_CLMcHaPortRemIp_Type=InetAddress
_CLMcHaPortRemIp_Object=MibScalar
cLMcHaPortRemIp=_CLMcHaPortRemIp_Object((1,3,6,1,4,1,9,9,843,1,6,6),_CLMcHaPortRemIp_Type())
cLMcHaPortRemIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaPortRemIp.setStatus(_B)
class _CLMcHaKeepAliveTimeOut_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CLMcHaKeepAliveTimeOut_Type.__name__=_F
_CLMcHaKeepAliveTimeOut_Object=MibScalar
cLMcHaKeepAliveTimeOut=_CLMcHaKeepAliveTimeOut_Object((1,3,6,1,4,1,9,9,843,1,6,7),_CLMcHaKeepAliveTimeOut_Type())
cLMcHaKeepAliveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaKeepAliveTimeOut.setStatus(_B)
class _CLMcHaChassisPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CLMcHaChassisPriority_Type.__name__=_F
_CLMcHaChassisPriority_Object=MibScalar
cLMcHaChassisPriority=_CLMcHaChassisPriority_Object((1,3,6,1,4,1,9,9,843,1,6,8),_CLMcHaChassisPriority_Type())
cLMcHaChassisPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaChassisPriority.setStatus(_B)
class _CLMcHaClearConfig_Type(TruthValue):defaultValue=2
_CLMcHaClearConfig_Type.__name__=_G
_CLMcHaClearConfig_Object=MibScalar
cLMcHaClearConfig=_CLMcHaClearConfig_Object((1,3,6,1,4,1,9,9,843,1,6,9),_CLMcHaClearConfig_Type())
cLMcHaClearConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaClearConfig.setStatus(_B)
class _CLMcHaKeepAliveRetryCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_CLMcHaKeepAliveRetryCount_Type.__name__=_F
_CLMcHaKeepAliveRetryCount_Object=MibScalar
cLMcHaKeepAliveRetryCount=_CLMcHaKeepAliveRetryCount_Object((1,3,6,1,4,1,9,9,843,1,6,10),_CLMcHaKeepAliveRetryCount_Type())
cLMcHaKeepAliveRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcHaKeepAliveRetryCount.setStatus(_B)
_CiscoLwappMcRmiConfig_ObjectIdentity=ObjectIdentity
ciscoLwappMcRmiConfig=_CiscoLwappMcRmiConfig_ObjectIdentity((1,3,6,1,4,1,9,9,843,1,7))
class _CLMcRmiConfigAction_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CLMcRmiConfigAction_Type.__name__=_F
_CLMcRmiConfigAction_Object=MibScalar
cLMcRmiConfigAction=_CLMcRmiConfigAction_Object((1,3,6,1,4,1,9,9,843,1,7,1),_CLMcRmiConfigAction_Type())
cLMcRmiConfigAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiConfigAction.setStatus(_B)
_CLMcRmiInterface_Type=SnmpAdminString
_CLMcRmiInterface_Object=MibScalar
cLMcRmiInterface=_CLMcRmiInterface_Object((1,3,6,1,4,1,9,9,843,1,7,2),_CLMcRmiInterface_Type())
cLMcRmiInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiInterface.setStatus(_B)
class _CLMcRmiChassisANum_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CLMcRmiChassisANum_Type.__name__=_F
_CLMcRmiChassisANum_Object=MibScalar
cLMcRmiChassisANum=_CLMcRmiChassisANum_Object((1,3,6,1,4,1,9,9,843,1,7,3),_CLMcRmiChassisANum_Type())
cLMcRmiChassisANum.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiChassisANum.setStatus(_B)
_CLMcRmiChassisAIpAddrType_Type=InetAddressType
_CLMcRmiChassisAIpAddrType_Object=MibScalar
cLMcRmiChassisAIpAddrType=_CLMcRmiChassisAIpAddrType_Object((1,3,6,1,4,1,9,9,843,1,7,4),_CLMcRmiChassisAIpAddrType_Type())
cLMcRmiChassisAIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiChassisAIpAddrType.setStatus(_B)
_CLMcRmiChassisAIp_Type=InetAddress
_CLMcRmiChassisAIp_Object=MibScalar
cLMcRmiChassisAIp=_CLMcRmiChassisAIp_Object((1,3,6,1,4,1,9,9,843,1,7,5),_CLMcRmiChassisAIp_Type())
cLMcRmiChassisAIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiChassisAIp.setStatus(_B)
class _CLMcRmiChassisBNum_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CLMcRmiChassisBNum_Type.__name__=_F
_CLMcRmiChassisBNum_Object=MibScalar
cLMcRmiChassisBNum=_CLMcRmiChassisBNum_Object((1,3,6,1,4,1,9,9,843,1,7,6),_CLMcRmiChassisBNum_Type())
cLMcRmiChassisBNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiChassisBNum.setStatus(_B)
_CLMcRmiChassisBIpAddrType_Type=InetAddressType
_CLMcRmiChassisBIpAddrType_Object=MibScalar
cLMcRmiChassisBIpAddrType=_CLMcRmiChassisBIpAddrType_Object((1,3,6,1,4,1,9,9,843,1,7,7),_CLMcRmiChassisBIpAddrType_Type())
cLMcRmiChassisBIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiChassisBIpAddrType.setStatus(_B)
_CLMcRmiChassisBIp_Type=InetAddress
_CLMcRmiChassisBIp_Object=MibScalar
cLMcRmiChassisBIp=_CLMcRmiChassisBIp_Object((1,3,6,1,4,1,9,9,843,1,7,8),_CLMcRmiChassisBIp_Type())
cLMcRmiChassisBIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiChassisBIp.setStatus(_B)
class _CLMcRmiGatewayFailover_Type(TruthValue):defaultValue=1
_CLMcRmiGatewayFailover_Type.__name__=_G
_CLMcRmiGatewayFailover_Object=MibScalar
cLMcRmiGatewayFailover=_CLMcRmiGatewayFailover_Object((1,3,6,1,4,1,9,9,843,1,7,9),_CLMcRmiGatewayFailover_Type())
cLMcRmiGatewayFailover.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiGatewayFailover.setStatus(_B)
class _CLMcRmiGatewayFailoverInterval_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,12))
_CLMcRmiGatewayFailoverInterval_Type.__name__=_F
_CLMcRmiGatewayFailoverInterval_Object=MibScalar
cLMcRmiGatewayFailoverInterval=_CLMcRmiGatewayFailoverInterval_Object((1,3,6,1,4,1,9,9,843,1,7,10),_CLMcRmiGatewayFailoverInterval_Type())
cLMcRmiGatewayFailoverInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cLMcRmiGatewayFailoverInterval.setStatus(_B)
_CiscoLwappHaMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappHaMIBConform=_CiscoLwappHaMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,843,2))
_CiscoLwappHaMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappHaMIBCompliances=_CiscoLwappHaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,843,2,1))
_CiscoLwappHaMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappHaMIBGroups=_CiscoLwappHaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,843,2,2))
ciscoLwappHaGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,843,2,2,1))
ciscoLwappHaGlobalConfigGroup.setObjects(*((_A,_f),(_A,_g),(_A,_L),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_M),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ciscoLwappHaGlobalConfigGroup.setStatus(_B)
ciscoLwappHaNetworkConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,843,2,2,2))
ciscoLwappHaNetworkConfigGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoLwappHaNetworkConfigGroup.setStatus(_B)
ciscoLwappHaStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,843,2,2,3))
ciscoLwappHaStatisticsGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:ciscoLwappHaStatisticsGroup.setStatus(_B)
ciscoLwappHaMIBNotificationVariableGroup=ObjectGroup((1,3,6,1,4,1,9,9,843,2,2,4))
ciscoLwappHaMIBNotificationVariableGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoLwappHaMIBNotificationVariableGroup.setStatus(_B)
ciscoLwappMcHaConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,843,2,2,6))
ciscoLwappMcHaConfigGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:ciscoLwappMcHaConfigGroup.setStatus(_B)
ciscoLwappMcRmiConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,843,2,2,7))
ciscoLwappMcRmiConfigGroup.setObjects(*((_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoLwappMcRmiConfigGroup.setStatus(_B)
cLHaSecondaryControllerUsageTrap=NotificationType((1,3,6,1,4,1,9,9,843,0,1))
cLHaSecondaryControllerUsageTrap.setObjects(*((_A,_N),(_A,_O),(_Z,_a)))
if mibBuilder.loadTexts:cLHaSecondaryControllerUsageTrap.setStatus(_B)
cLHaRFSwapInfoTrap=NotificationType((1,3,6,1,4,1,9,9,843,0,2))
cLHaRFSwapInfoTrap.setObjects(*((_A,_M),(_J,_Y),(_A,_L),(_J,_X)))
if mibBuilder.loadTexts:cLHaRFSwapInfoTrap.setStatus(_B)
cLHaBulkSyncCompleteTrap=NotificationType((1,3,6,1,4,1,9,9,843,0,3))
cLHaBulkSyncCompleteTrap.setObjects((_A,_P))
if mibBuilder.loadTexts:cLHaBulkSyncCompleteTrap.setStatus(_B)
cLHaPeerHotStandbyTrap=NotificationType((1,3,6,1,4,1,9,9,843,0,4))
cLHaPeerHotStandbyTrap.setObjects((_A,_Q))
if mibBuilder.loadTexts:cLHaPeerHotStandbyTrap.setStatus(_B)
ciscoLwappHaMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,843,2,2,5))
ciscoLwappHaMIBNotificationGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:ciscoLwappHaMIBNotificationGroup.setStatus(_B)
ciscoLwappHaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,843,2,1,1))
ciscoLwappHaMIBCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoLwappHaMIBCompliance.setStatus('deprecated')
ciscoLwappHaMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,843,2,1,2))
ciscoLwappHaMIBComplianceRev1.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_Am)))
if mibBuilder.loadTexts:ciscoLwappHaMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoLwappHaMIB':ciscoLwappHaMIB,'ciscoLwappHaMIBNotifs':ciscoLwappHaMIBNotifs,_Ai:cLHaSecondaryControllerUsageTrap,_Aj:cLHaRFSwapInfoTrap,_Ak:cLHaBulkSyncCompleteTrap,_Al:cLHaPeerHotStandbyTrap,'ciscoLwappHaMIBObjects':ciscoLwappHaMIBObjects,'ciscoLwappHaGlobalConfig':ciscoLwappHaGlobalConfig,_f:cLHaApSsoConfig,_g:cLHaPeerIpAddressType,_L:cLHaPeerIpAddress,_h:cLHaServicePortPeerIpAddressType,_i:cLHaServicePortPeerIpAddress,_j:cLHaServicePortPeerIpNetMaskType,_k:cLHaServicePortPeerIpNetMask,_l:cLHaRedundancyIpAddressType,_m:cLHaRedundancyIpAddress,_n:cLHaPeerMacAddress,_o:cLHaVirtualMacAddress,_p:cLHaPrimaryUnit,_q:cLHaLinkEncryption,_r:cLHaNetworkFailOver,_M:cLHaRFStatusUnitIp,_t:cLHaKATimeout,_u:cLHaKARetryCount,_v:cLHaGwRetryCount,_w:cLHaPeerSearchTimeout,_s:cLHaRFStatusUnitIpType,'ciscoLwappHaNetworkConfig':ciscoLwappHaNetworkConfig,'cLHaNetworkRoutePeerConfigTable':cLHaNetworkRoutePeerConfigTable,'cLHaNetworkRoutePeerConfigEntry':cLHaNetworkRoutePeerConfigEntry,_b:cLHaNetworkRoutePeerIPAddressType,_c:cLHaNetworkRoutePeerIPAddress,_x:cLHaNetworkRoutePeerIPNetmaskType,_y:cLHaNetworkRoutePeerIPNetmask,_z:cLHaNetworkRoutePeerGatewayType,_A0:cLHaNetworkRoutePeerGateway,_A1:cLHaNetworkRoutePeerTransferStatus,_A2:cLHaNetworkRoutePeerRowStatus,'ciscoLwappHaNotificationVariable':ciscoLwappHaNotificationVariable,_N:cLHaSecondaryControllerUsageTrapType,_O:cLHaSecondaryControllerUsageDayCounter,_P:cLHaBulkSyncCompleteEvent,_Q:cLHaPeerHotStandbyEvent,'ciscoLwappHaPeerStatisticsVariable':ciscoLwappHaPeerStatisticsVariable,'ciscoLwappHaSystemStatistics':ciscoLwappHaSystemStatistics,'ciscoLwappHaCpuStatistics':ciscoLwappHaCpuStatistics,_AJ:cLHaAllCpuUsage,'ciscoLwappHaPowerSupplyStatistics':ciscoLwappHaPowerSupplyStatistics,_AK:cLHaPowerSupply1Present,_AL:cLHaPowerSupply1Operational,_AM:cLHaPowerSupply2Present,_AN:cLHaPowerSupply2Operational,'ciscoLwappHaMemoryStatistics':ciscoLwappHaMemoryStatistics,_A6:cLHaTotalSystemMemory,_A7:cLHaFreeSystemMemory,_A8:cLHaUsedSystemMemory,_A9:cLHaAllocatedFromRtos,_AA:cLHaChunksFree,_AB:cLHaMmappedRegions,_AC:cLHaSpaceInMmappedRegions,_AD:cLHaTotalAllocatedSpace,_AE:cLHaTotalNotInUseSpace,_AF:cLHaTopMostReleasableSpace,_AG:cLHaTotalAllocatedInclMmap,_AH:cLHaTotalUsedMmap,_AI:cLHaTotalFreeInclMmap,'ciscoLwappHaStatisticsVariable':ciscoLwappHaStatisticsVariable,_A3:cLHaAvgPeerReachLatency,_A4:cLHaAvgGwReachLatency,_A5:cLHaBulkSyncStatus,'ciscoLwappMcHaConfig':ciscoLwappMcHaConfig,_AO:cLMcHaPortName,_AP:cLMcHaPortLocIpAddrType,_AQ:cLMcHaPortLocIp,_AR:cLMcHaPortMask,_AS:cLMcHaPortRemoteIpAddrType,_AT:cLMcHaPortRemIp,_AU:cLMcHaKeepAliveTimeOut,_AV:cLMcHaChassisPriority,_AW:cLMcHaClearConfig,_AX:cLMcHaKeepAliveRetryCount,'ciscoLwappMcRmiConfig':ciscoLwappMcRmiConfig,_AY:cLMcRmiConfigAction,_AZ:cLMcRmiInterface,_Aa:cLMcRmiChassisANum,_Ab:cLMcRmiChassisAIpAddrType,_Ac:cLMcRmiChassisAIp,_Ad:cLMcRmiChassisBNum,_Ae:cLMcRmiChassisBIpAddrType,_Af:cLMcRmiChassisBIp,_Ag:cLMcRmiGatewayFailover,_Ah:cLMcRmiGatewayFailoverInterval,'ciscoLwappHaMIBConform':ciscoLwappHaMIBConform,'ciscoLwappHaMIBCompliances':ciscoLwappHaMIBCompliances,'ciscoLwappHaMIBCompliance':ciscoLwappHaMIBCompliance,'ciscoLwappHaMIBComplianceRev1':ciscoLwappHaMIBComplianceRev1,'ciscoLwappHaMIBGroups':ciscoLwappHaMIBGroups,_R:ciscoLwappHaGlobalConfigGroup,_S:ciscoLwappHaNetworkConfigGroup,_T:ciscoLwappHaStatisticsGroup,_U:ciscoLwappHaMIBNotificationVariableGroup,_V:ciscoLwappHaMIBNotificationGroup,_W:ciscoLwappMcHaConfigGroup,_Am:ciscoLwappMcRmiConfigGroup})