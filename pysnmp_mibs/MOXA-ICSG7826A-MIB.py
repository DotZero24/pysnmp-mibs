_BN='varABC02WarningTrap'
_BM='varLLDPChgTrap'
_BL='varRateLimitedOnTrap'
_BK='varPortLoopDetectedTrap'
_BJ='varturboRingCouplingPortChangedTrap'
_BI='varredundancyTopologyChangedTrap'
_BH='vartrafficOverloadTrap'
_BG='varpower2Trap'
_BF='varpower1Trap'
_BE='varconfigChangeTrap'
_BD='pimdmMRIndex'
_BC='pimdmIfIndex'
_BB='dvmrpMRIndex'
_BA='dvmrpIfIndex'
_B9='ipRoutingIndex'
_B8='ospfAggrIndex'
_B7='ospfVlinkIndex'
_B6='ospfIfIndex'
_B5='ospfAreaId'
_B4='staticRouteIndex'
_B3='portEventIndex'
_B2='information'
_B1='emergency'
_B0='enable-All-SNMPTrap-Email-Syslog-Relay1-Relay2'
_A_='enable-Email-Syslog-Relay1-Relay2'
_Az='enable-Syslog-Relay1-Relay2'
_Ay='enable-SNMPTrap-Relay1-Relay2'
_Ax='enable-Relay1-Relay2'
_Aw='enable-SNMPTrap-Email-Syslog-Relay2'
_Av='enable-Email-Syslog-Relay2'
_Au='enable-SNMPTrap-Syslog-Relay2'
_At='enable-Syslog-Relay2'
_As='enable-SNMPTrap-Email-Relay2'
_Ar='enable-Email-Relay2'
_Aq='enable-SNMPTrap-Relay2'
_Ap='enable-Relay2-only'
_Ao='enable-SNMPTrap-Email-Syslog-Relay1'
_An='enable-Email-Syslog-Relay1'
_Am='enable-SNMPTrap-Syslog-Relay1'
_Al='enable-Syslog-Relay1'
_Ak='enable-SNMPTrap-Email-Relay1'
_Aj='enable-Email-Relay1'
_Ai='enable-SNMPTrap-Relay1'
_Ah='enable-Relay1-only'
_Ag='enable-SNMPTrap-Email-Syslog'
_Af='enable-Email-Syslog'
_Ae='enable-SNMPTrap-Syslog'
_Ad='enable-Syslog-only'
_Ac='enable-SNMPTrap-Email'
_Ab='enable-Email-only'
_Aa='enable-SNMPTrap-only'
_AZ='systemEventIndex'
_AY='aclRuleIndex'
_AX='eventlogIndex'
_AW='ptpPortIndex'
_AV='v2E2E1stepTC'
_AU='v2E2E2stepTC'
_AT='dhcpPortIndex'
_AS='accessibleIpAddress'
_AR='portAccessControlAddress'
_AQ='dot1xReauthPortIndex'
_AP='notlimited'
_AO='gmrpMulticastGroup'
_AN='staticMulticastAddress'
_AM='igmpSnoopingStreamIndex'
_AL='notTurboChainPort'
_AK='spanningTreeIndex'
_AJ='turboRingPortIndex'
_AI='trunkPort'
_AH='trunkIndex'
_AG='trunkSettingIndex'
_AF='setDevIpIndex'
_AE='not-present'
_AD='speed1000M-Half'
_AC='speed1000M-Full'
_AB='speed10M-Half'
_AA='speed10M-Full'
_A9='speed100M-Half'
_A8='speed100M-Full'
_A7='varturboRingMasterChangedTrap'
_A6='t16sec'
_A5='t8sec'
_A4='t4sec'
_A3='vlanId'
_A2='priority7'
_A1='priority6'
_A0='priority5'
_z='priority4'
_y='priority3'
_x='off2on'
_w='on2off'
_v='broken'
_u='inactive'
_t='turboChain'
_s='turboRingV2'
_r='turboRing'
_q='spanningTree'
_p='diIndex'
_o='auto'
_n='ipIfIndex'
_m='t2sec'
_l='t1sec'
_k='true'
_j='priority2'
_i='priority1'
_h='relayAlarmIndex'
_g='portDisabled'
_f='false'
_e='priority0'
_d='normal'
_c='on'
_b='off'
_a='triggered'
_Z='not-triggered'
_Y='linkdown'
_X='notRedundant'
_W='disabled'
_V='blocked'
_U='linkDown'
_T='blocking'
_S='learning'
_R='destroy'
_Q='createAndWait'
_P='createAndGo'
_O='forwarding'
_N='yes'
_M='portIndex'
_L='none'
_K='active'
_J='no'
_I='na'
_H='enable'
_G='disable'
_F='read-create'
_E='MOXA-ICSG7826A-MIB'
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
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
icsg7826a=ModuleIdentity((1,3,6,1,4,1,8691,7,99))
if mibBuilder.loadTexts:icsg7826a.setRevisions(('2016-07-20 00:00','2015-06-26 00:00'))
class PortList(TextualConvention,OctetString):status=_A
_Moxa_ObjectIdentity=ObjectIdentity
moxa=_Moxa_ObjectIdentity((1,3,6,1,4,1,8691))
_IndustrialEthernet_ObjectIdentity=ObjectIdentity
industrialEthernet=_IndustrialEthernet_ObjectIdentity((1,3,6,1,4,1,8691,7))
_MibNotificationsPrefix_ObjectIdentity=ObjectIdentity
mibNotificationsPrefix=_MibNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,8691,7,99,0))
_SwMgmt_ObjectIdentity=ObjectIdentity
swMgmt=_SwMgmt_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1))
_NumberOfPorts_Type=Integer32
_NumberOfPorts_Object=MibScalar
numberOfPorts=_NumberOfPorts_Object((1,3,6,1,4,1,8691,7,99,1,1),_NumberOfPorts_Type())
numberOfPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:numberOfPorts.setStatus(_A)
_SwitchModel_Type=DisplayString
_SwitchModel_Object=MibScalar
switchModel=_SwitchModel_Object((1,3,6,1,4,1,8691,7,99,1,2),_SwitchModel_Type())
switchModel.setMaxAccess(_D)
if mibBuilder.loadTexts:switchModel.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,8691,7,99,1,4),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
class _EnableWebConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('httpOrHttps',1),('httpsOnly',2)))
_EnableWebConfig_Type.__name__=_C
_EnableWebConfig_Object=MibScalar
enableWebConfig=_EnableWebConfig_Object((1,3,6,1,4,1,8691,7,99,1,5),_EnableWebConfig_Type())
enableWebConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:enableWebConfig.setStatus(_A)
class _EnableTelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableTelnetConsole_Type.__name__=_C
_EnableTelnetConsole_Object=MibScalar
enableTelnetConsole=_EnableTelnetConsole_Object((1,3,6,1,4,1,8691,7,99,1,6),_EnableTelnetConsole_Type())
enableTelnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:enableTelnetConsole.setStatus(_A)
class _LineSwapRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_LineSwapRecovery_Type.__name__=_C
_LineSwapRecovery_Object=MibScalar
lineSwapRecovery=_LineSwapRecovery_Object((1,3,6,1,4,1,8691,7,99,1,7),_LineSwapRecovery_Type())
lineSwapRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:lineSwapRecovery.setStatus(_A)
_NetworkSetting_ObjectIdentity=ObjectIdentity
networkSetting=_NetworkSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,8))
_SwitchIpAddr_Type=IpAddress
_SwitchIpAddr_Object=MibScalar
switchIpAddr=_SwitchIpAddr_Object((1,3,6,1,4,1,8691,7,99,1,8,1),_SwitchIpAddr_Type())
switchIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:switchIpAddr.setStatus(_A)
_SwitchIpMask_Type=IpAddress
_SwitchIpMask_Object=MibScalar
switchIpMask=_SwitchIpMask_Object((1,3,6,1,4,1,8691,7,99,1,8,2),_SwitchIpMask_Type())
switchIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:switchIpMask.setStatus(_A)
_DefaultGateway_Type=IpAddress
_DefaultGateway_Object=MibScalar
defaultGateway=_DefaultGateway_Object((1,3,6,1,4,1,8691,7,99,1,8,3),_DefaultGateway_Type())
defaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultGateway.setStatus(_A)
class _EnableAutoIpConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('enableDHCP',1),('enableBOOTP',2)))
_EnableAutoIpConfig_Type.__name__=_C
_EnableAutoIpConfig_Object=MibScalar
enableAutoIpConfig=_EnableAutoIpConfig_Object((1,3,6,1,4,1,8691,7,99,1,8,4),_EnableAutoIpConfig_Type())
enableAutoIpConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAutoIpConfig.setStatus(_A)
_DnsServer1IpAddr_Type=IpAddress
_DnsServer1IpAddr_Object=MibScalar
dnsServer1IpAddr=_DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,7,99,1,8,5),_DnsServer1IpAddr_Type())
dnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer1IpAddr.setStatus(_A)
_SnmpTrapCommunity_Type=DisplayString
_SnmpTrapCommunity_Object=MibScalar
snmpTrapCommunity=_SnmpTrapCommunity_Object((1,3,6,1,4,1,8691,7,99,1,8,6),_SnmpTrapCommunity_Type())
snmpTrapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapCommunity.setStatus(_A)
_TrapServerAddr_Type=DisplayString
_TrapServerAddr_Object=MibScalar
trapServerAddr=_TrapServerAddr_Object((1,3,6,1,4,1,8691,7,99,1,8,7),_TrapServerAddr_Type())
trapServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerAddr.setStatus(_A)
_DnsServer2IpAddr_Type=IpAddress
_DnsServer2IpAddr_Object=MibScalar
dnsServer2IpAddr=_DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,7,99,1,8,8),_DnsServer2IpAddr_Type())
dnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer2IpAddr.setStatus(_A)
_SnmpReadCommunity_Type=DisplayString
_SnmpReadCommunity_Object=MibScalar
snmpReadCommunity=_SnmpReadCommunity_Object((1,3,6,1,4,1,8691,7,99,1,8,9),_SnmpReadCommunity_Type())
snmpReadCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpReadCommunity.setStatus(_A)
_SnmpTrap2Community_Type=DisplayString
_SnmpTrap2Community_Object=MibScalar
snmpTrap2Community=_SnmpTrap2Community_Object((1,3,6,1,4,1,8691,7,99,1,8,11),_SnmpTrap2Community_Type())
snmpTrap2Community.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrap2Community.setStatus(_A)
_Trap2ServerAddr_Type=DisplayString
_Trap2ServerAddr_Object=MibScalar
trap2ServerAddr=_Trap2ServerAddr_Object((1,3,6,1,4,1,8691,7,99,1,8,12),_Trap2ServerAddr_Type())
trap2ServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trap2ServerAddr.setStatus(_A)
class _SnmpInformEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnmpInformEnable_Type.__name__=_C
_SnmpInformEnable_Object=MibScalar
snmpInformEnable=_SnmpInformEnable_Object((1,3,6,1,4,1,8691,7,99,1,8,13),_SnmpInformEnable_Type())
snmpInformEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInformEnable.setStatus(_A)
class _SnmpInformRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_SnmpInformRetries_Type.__name__=_C
_SnmpInformRetries_Object=MibScalar
snmpInformRetries=_SnmpInformRetries_Object((1,3,6,1,4,1,8691,7,99,1,8,14),_SnmpInformRetries_Type())
snmpInformRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInformRetries.setStatus(_A)
class _SnmpInformTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_SnmpInformTimeout_Type.__name__=_C
_SnmpInformTimeout_Object=MibScalar
snmpInformTimeout=_SnmpInformTimeout_Object((1,3,6,1,4,1,8691,7,99,1,8,15),_SnmpInformTimeout_Type())
snmpInformTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInformTimeout.setStatus(_A)
_DhcpRetryPeriods_Type=Integer32
_DhcpRetryPeriods_Object=MibScalar
dhcpRetryPeriods=_DhcpRetryPeriods_Object((1,3,6,1,4,1,8691,7,99,1,8,16),_DhcpRetryPeriods_Type())
dhcpRetryPeriods.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRetryPeriods.setStatus(_A)
_DhcpRetryTimes_Type=Integer32
_DhcpRetryTimes_Object=MibScalar
dhcpRetryTimes=_DhcpRetryTimes_Object((1,3,6,1,4,1,8691,7,99,1,8,17),_DhcpRetryTimes_Type())
dhcpRetryTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRetryTimes.setStatus(_A)
_PortSetting_ObjectIdentity=ObjectIdentity
portSetting=_PortSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,9))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,8691,7,99,1,9,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1))
portEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
_PortDesc_Type=DisplayString
_PortDesc_Object=MibTableColumn
portDesc=_PortDesc_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,2),_PortDesc_Type())
portDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:portDesc.setStatus(_A)
class _PortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_PortEnable_Type.__name__=_C
_PortEnable_Object=MibTableColumn
portEnable=_PortEnable_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,3),_PortEnable_Type())
portEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portEnable.setStatus(_A)
class _PortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_o,0),(_A8,1),(_A9,2),(_AA,3),(_AB,4),(_AC,5),(_AD,6),('speed10G',7)))
_PortSpeed_Type.__name__=_C
_PortSpeed_Object=MibTableColumn
portSpeed=_PortSpeed_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,4),_PortSpeed_Type())
portSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:portSpeed.setStatus(_A)
class _PortMDI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_o,1),('mdi',2),('mdiX',3)))
_PortMDI_Type.__name__=_C
_PortMDI_Object=MibTableColumn
portMDI=_PortMDI_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,5),_PortMDI_Type())
portMDI.setMaxAccess(_B)
if mibBuilder.loadTexts:portMDI.setStatus(_A)
class _PortFDXFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_PortFDXFlowCtrl_Type.__name__=_C
_PortFDXFlowCtrl_Object=MibTableColumn
portFDXFlowCtrl=_PortFDXFlowCtrl_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,6),_PortFDXFlowCtrl_Type())
portFDXFlowCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFDXFlowCtrl.setStatus(_A)
_PortName_Type=DisplayString
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,8691,7,99,1,9,1,1,7),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
_Monitor_ObjectIdentity=ObjectIdentity
monitor=_Monitor_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,10))
class _Power1InputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AE,0),('present',1)))
_Power1InputStatus_Type.__name__=_C
_Power1InputStatus_Object=MibScalar
power1InputStatus=_Power1InputStatus_Object((1,3,6,1,4,1,8691,7,99,1,10,1),_Power1InputStatus_Type())
power1InputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power1InputStatus.setStatus(_A)
class _Power2InputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AE,0),('present',1)))
_Power2InputStatus_Type.__name__=_C
_Power2InputStatus_Object=MibScalar
power2InputStatus=_Power2InputStatus_Object((1,3,6,1,4,1,8691,7,99,1,10,2),_Power2InputStatus_Type())
power2InputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power2InputStatus.setStatus(_A)
_MonitorPortTable_Object=MibTable
monitorPortTable=_MonitorPortTable_Object((1,3,6,1,4,1,8691,7,99,1,10,3))
if mibBuilder.loadTexts:monitorPortTable.setStatus(_A)
_MonitorPortEntry_Object=MibTableRow
monitorPortEntry=_MonitorPortEntry_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1))
monitorPortEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:monitorPortEntry.setStatus(_A)
class _MonitorLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_G,-1),(_b,0),(_c,1)))
_MonitorLinkStatus_Type.__name__=_C
_MonitorLinkStatus_Object=MibTableColumn
monitorLinkStatus=_MonitorLinkStatus_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,2),_MonitorLinkStatus_Type())
monitorLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorLinkStatus.setStatus(_A)
class _MonitorSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,7)));namedValues=NamedValues(*((_I,-1),(_AB,0),(_AA,1),(_A9,2),(_A8,3),(_AD,4),(_AC,5),('speed10G',7)))
_MonitorSpeed_Type.__name__=_C
_MonitorSpeed_Object=MibTableColumn
monitorSpeed=_MonitorSpeed_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,3),_MonitorSpeed_Type())
monitorSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSpeed.setStatus(_A)
class _MonitorAutoMDI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_I,-1),('mdi',0),('mdiX',1)))
_MonitorAutoMDI_Type.__name__=_C
_MonitorAutoMDI_Object=MibTableColumn
monitorAutoMDI=_MonitorAutoMDI_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,4),_MonitorAutoMDI_Type())
monitorAutoMDI.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorAutoMDI.setStatus(_A)
_MonitorTraffic_Type=Integer32
_MonitorTraffic_Object=MibTableColumn
monitorTraffic=_MonitorTraffic_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,5),_MonitorTraffic_Type())
monitorTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTraffic.setStatus(_A)
class _MonitorFDXFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_MonitorFDXFlowCtrl_Type.__name__=_C
_MonitorFDXFlowCtrl_Object=MibTableColumn
monitorFDXFlowCtrl=_MonitorFDXFlowCtrl_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,6),_MonitorFDXFlowCtrl_Type())
monitorFDXFlowCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFDXFlowCtrl.setStatus(_A)
_MonitorTxTraffic_Type=Integer32
_MonitorTxTraffic_Object=MibTableColumn
monitorTxTraffic=_MonitorTxTraffic_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,7),_MonitorTxTraffic_Type())
monitorTxTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTxTraffic.setStatus(_A)
_MonitorRxTraffic_Type=Integer32
_MonitorRxTraffic_Object=MibTableColumn
monitorRxTraffic=_MonitorRxTraffic_Object((1,3,6,1,4,1,8691,7,99,1,10,3,1,8),_MonitorRxTraffic_Type())
monitorRxTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRxTraffic.setStatus(_A)
_MonitorDiTable_Object=MibTable
monitorDiTable=_MonitorDiTable_Object((1,3,6,1,4,1,8691,7,99,1,10,4))
if mibBuilder.loadTexts:monitorDiTable.setStatus(_A)
_MonitorDiEntry_Object=MibTableRow
monitorDiEntry=_MonitorDiEntry_Object((1,3,6,1,4,1,8691,7,99,1,10,4,1))
monitorDiEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:monitorDiEntry.setStatus(_A)
class _DiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DiIndex_Type.__name__=_C
_DiIndex_Object=MibTableColumn
diIndex=_DiIndex_Object((1,3,6,1,4,1,8691,7,99,1,10,4,1,1),_DiIndex_Type())
diIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:diIndex.setStatus(_A)
class _DiInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_DiInputStatus_Type.__name__=_C
_DiInputStatus_Object=MibTableColumn
diInputStatus=_DiInputStatus_Object((1,3,6,1,4,1,8691,7,99,1,10,4,1,2),_DiInputStatus_Type())
diInputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:diInputStatus.setStatus(_A)
_MonitorSFPTable_Object=MibTable
monitorSFPTable=_MonitorSFPTable_Object((1,3,6,1,4,1,8691,7,99,1,10,7))
if mibBuilder.loadTexts:monitorSFPTable.setStatus(_A)
_MonitorSFPEntry_Object=MibTableRow
monitorSFPEntry=_MonitorSFPEntry_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1))
monitorSFPEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:monitorSFPEntry.setStatus(_A)
_SfpPort_Type=DisplayString
_SfpPort_Object=MibTableColumn
sfpPort=_SfpPort_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1,1),_SfpPort_Type())
sfpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpPort.setStatus(_A)
_SfpModelName_Type=DisplayString
_SfpModelName_Object=MibTableColumn
sfpModelName=_SfpModelName_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1,2),_SfpModelName_Type())
sfpModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpModelName.setStatus(_A)
_SfpTemperature_Type=DisplayString
_SfpTemperature_Object=MibTableColumn
sfpTemperature=_SfpTemperature_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1,3),_SfpTemperature_Type())
sfpTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpTemperature.setStatus(_A)
_SfpVoltage_Type=DisplayString
_SfpVoltage_Object=MibTableColumn
sfpVoltage=_SfpVoltage_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1,4),_SfpVoltage_Type())
sfpVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpVoltage.setStatus(_A)
_SfpTxPower_Type=DisplayString
_SfpTxPower_Object=MibTableColumn
sfpTxPower=_SfpTxPower_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1,5),_SfpTxPower_Type())
sfpTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpTxPower.setStatus(_A)
_SfpRxPower_Type=DisplayString
_SfpRxPower_Object=MibTableColumn
sfpRxPower=_SfpRxPower_Object((1,3,6,1,4,1,8691,7,99,1,10,7,1,6),_SfpRxPower_Type())
sfpRxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpRxPower.setStatus(_A)
_PowerConsumption_Type=DisplayString
_PowerConsumption_Object=MibScalar
powerConsumption=_PowerConsumption_Object((1,3,6,1,4,1,8691,7,99,1,10,8),_PowerConsumption_Type())
powerConsumption.setMaxAccess(_D)
if mibBuilder.loadTexts:powerConsumption.setStatus(_A)
_EmailWarning_ObjectIdentity=ObjectIdentity
emailWarning=_EmailWarning_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,11))
_EmailService_ObjectIdentity=ObjectIdentity
emailService=_EmailService_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,11,1))
_EmailWarningMailServer_Type=DisplayString
_EmailWarningMailServer_Object=MibScalar
emailWarningMailServer=_EmailWarningMailServer_Object((1,3,6,1,4,1,8691,7,99,1,11,1,1),_EmailWarningMailServer_Type())
emailWarningMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningMailServer.setStatus(_A)
_EmailWarningFirstEmailAddr_Type=DisplayString
_EmailWarningFirstEmailAddr_Object=MibScalar
emailWarningFirstEmailAddr=_EmailWarningFirstEmailAddr_Object((1,3,6,1,4,1,8691,7,99,1,11,1,2),_EmailWarningFirstEmailAddr_Type())
emailWarningFirstEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFirstEmailAddr.setStatus(_A)
_EmailWarningSecondEmailAddr_Type=DisplayString
_EmailWarningSecondEmailAddr_Object=MibScalar
emailWarningSecondEmailAddr=_EmailWarningSecondEmailAddr_Object((1,3,6,1,4,1,8691,7,99,1,11,1,3),_EmailWarningSecondEmailAddr_Type())
emailWarningSecondEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSecondEmailAddr.setStatus(_A)
_EmailWarningThirdEmailAddr_Type=DisplayString
_EmailWarningThirdEmailAddr_Object=MibScalar
emailWarningThirdEmailAddr=_EmailWarningThirdEmailAddr_Object((1,3,6,1,4,1,8691,7,99,1,11,1,4),_EmailWarningThirdEmailAddr_Type())
emailWarningThirdEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningThirdEmailAddr.setStatus(_A)
_EmailWarningFourthEmailAddr_Type=DisplayString
_EmailWarningFourthEmailAddr_Object=MibScalar
emailWarningFourthEmailAddr=_EmailWarningFourthEmailAddr_Object((1,3,6,1,4,1,8691,7,99,1,11,1,5),_EmailWarningFourthEmailAddr_Type())
emailWarningFourthEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFourthEmailAddr.setStatus(_A)
class _EmailWarningSMTPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EmailWarningSMTPPort_Type.__name__=_C
_EmailWarningSMTPPort_Object=MibScalar
emailWarningSMTPPort=_EmailWarningSMTPPort_Object((1,3,6,1,4,1,8691,7,99,1,11,1,6),_EmailWarningSMTPPort_Type())
emailWarningSMTPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSMTPPort.setStatus(_A)
_SetDeviceIp_ObjectIdentity=ObjectIdentity
setDeviceIp=_SetDeviceIp_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,12))
_SetDevIpTable_Object=MibTable
setDevIpTable=_SetDevIpTable_Object((1,3,6,1,4,1,8691,7,99,1,12,1))
if mibBuilder.loadTexts:setDevIpTable.setStatus(_A)
_SetDevIpEntry_Object=MibTableRow
setDevIpEntry=_SetDevIpEntry_Object((1,3,6,1,4,1,8691,7,99,1,12,1,1))
setDevIpEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:setDevIpEntry.setStatus(_A)
_SetDevIpIndex_Type=Integer32
_SetDevIpIndex_Object=MibTableColumn
setDevIpIndex=_SetDevIpIndex_Object((1,3,6,1,4,1,8691,7,99,1,12,1,1,1),_SetDevIpIndex_Type())
setDevIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpIndex.setStatus(_A)
_SetDevIpCurrentIpofDevice_Type=DisplayString
_SetDevIpCurrentIpofDevice_Object=MibTableColumn
setDevIpCurrentIpofDevice=_SetDevIpCurrentIpofDevice_Object((1,3,6,1,4,1,8691,7,99,1,12,1,1,2),_SetDevIpCurrentIpofDevice_Type())
setDevIpCurrentIpofDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpCurrentIpofDevice.setStatus(_A)
class _SetDevIpPresentBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_J,0),('dhcpClient',1),('rarp',2),('bootp',4)))
_SetDevIpPresentBy_Type.__name__=_C
_SetDevIpPresentBy_Object=MibTableColumn
setDevIpPresentBy=_SetDevIpPresentBy_Object((1,3,6,1,4,1,8691,7,99,1,12,1,1,3),_SetDevIpPresentBy_Type())
setDevIpPresentBy.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpPresentBy.setStatus(_A)
_SetDevIpDedicatedIp_Type=IpAddress
_SetDevIpDedicatedIp_Object=MibTableColumn
setDevIpDedicatedIp=_SetDevIpDedicatedIp_Object((1,3,6,1,4,1,8691,7,99,1,12,1,1,4),_SetDevIpDedicatedIp_Type())
setDevIpDedicatedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:setDevIpDedicatedIp.setStatus(_A)
_Mirroring_ObjectIdentity=ObjectIdentity
mirroring=_Mirroring_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,13))
_TargetPort_Type=PortList
_TargetPort_Object=MibScalar
targetPort=_TargetPort_Object((1,3,6,1,4,1,8691,7,99,1,13,1),_TargetPort_Type())
targetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:targetPort.setStatus(_A)
_MirroringPort_Type=Integer32
_MirroringPort_Object=MibScalar
mirroringPort=_MirroringPort_Object((1,3,6,1,4,1,8691,7,99,1,13,2),_MirroringPort_Type())
mirroringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirroringPort.setStatus(_A)
class _MonitorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inputDataStream',0),('outputDataStream',1),('biDirectional',2)))
_MonitorDirection_Type.__name__=_C
_MonitorDirection_Object=MibScalar
monitorDirection=_MonitorDirection_Object((1,3,6,1,4,1,8691,7,99,1,13,3),_MonitorDirection_Type())
monitorDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:monitorDirection.setStatus(_A)
_PortTrunking_ObjectIdentity=ObjectIdentity
portTrunking=_PortTrunking_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,14))
_TrunkSettingTable_Object=MibTable
trunkSettingTable=_TrunkSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,14,1))
if mibBuilder.loadTexts:trunkSettingTable.setStatus(_A)
_TrunkSettingEntry_Object=MibTableRow
trunkSettingEntry=_TrunkSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,14,1,1))
trunkSettingEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:trunkSettingEntry.setStatus(_A)
_TrunkSettingIndex_Type=Integer32
_TrunkSettingIndex_Object=MibTableColumn
trunkSettingIndex=_TrunkSettingIndex_Object((1,3,6,1,4,1,8691,7,99,1,14,1,1,1),_TrunkSettingIndex_Type())
trunkSettingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkSettingIndex.setStatus(_A)
class _TrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('lacp',2)))
_TrunkType_Type.__name__=_C
_TrunkType_Object=MibTableColumn
trunkType=_TrunkType_Object((1,3,6,1,4,1,8691,7,99,1,14,1,1,2),_TrunkType_Type())
trunkType.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkType.setStatus(_A)
_TrunkMemberPorts_Type=PortList
_TrunkMemberPorts_Object=MibTableColumn
trunkMemberPorts=_TrunkMemberPorts_Object((1,3,6,1,4,1,8691,7,99,1,14,1,1,3),_TrunkMemberPorts_Type())
trunkMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkMemberPorts.setStatus(_A)
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,8691,7,99,1,14,2))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,8691,7,99,1,14,2,1))
trunkEntry.setIndexNames((0,_E,_AH),(0,_E,_AI))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
_TrunkIndex_Type=Integer32
_TrunkIndex_Object=MibTableColumn
trunkIndex=_TrunkIndex_Object((1,3,6,1,4,1,8691,7,99,1,14,2,1,1),_TrunkIndex_Type())
trunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkIndex.setStatus(_A)
_TrunkPort_Type=Integer32
_TrunkPort_Object=MibTableColumn
trunkPort=_TrunkPort_Object((1,3,6,1,4,1,8691,7,99,1,14,2,1,2),_TrunkPort_Type())
trunkPort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkPort.setStatus(_A)
class _TrunkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('success',1),('fail',2),('standby',3)))
_TrunkStatus_Type.__name__=_C
_TrunkStatus_Object=MibTableColumn
trunkStatus=_TrunkStatus_Object((1,3,6,1,4,1,8691,7,99,1,14,2,1,3),_TrunkStatus_Type())
trunkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkStatus.setStatus(_A)
_CommRedundancy_ObjectIdentity=ObjectIdentity
commRedundancy=_CommRedundancy_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16))
class _ProtocolOfRedundancySetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),('mstp',5)))
_ProtocolOfRedundancySetup_Type.__name__=_C
_ProtocolOfRedundancySetup_Object=MibScalar
protocolOfRedundancySetup=_ProtocolOfRedundancySetup_Object((1,3,6,1,4,1,8691,7,99,1,16,1),_ProtocolOfRedundancySetup_Type())
protocolOfRedundancySetup.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolOfRedundancySetup.setStatus(_A)
_TurboRing_ObjectIdentity=ObjectIdentity
turboRing=_TurboRing_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,2))
class _TurboRingMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_TurboRingMaster_Type.__name__=_C
_TurboRingMaster_Object=MibScalar
turboRingMaster=_TurboRingMaster_Object((1,3,6,1,4,1,8691,7,99,1,16,2,1),_TurboRingMaster_Type())
turboRingMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingMaster.setStatus(_A)
class _TurboRingMasterSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_TurboRingMasterSetup_Type.__name__=_C
_TurboRingMasterSetup_Object=MibScalar
turboRingMasterSetup=_TurboRingMasterSetup_Object((1,3,6,1,4,1,8691,7,99,1,16,2,2),_TurboRingMasterSetup_Type())
turboRingMasterSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingMasterSetup.setStatus(_A)
_TurboRingPortTable_Object=MibTable
turboRingPortTable=_TurboRingPortTable_Object((1,3,6,1,4,1,8691,7,99,1,16,2,3))
if mibBuilder.loadTexts:turboRingPortTable.setStatus(_A)
_TurboRingPortEntry_Object=MibTableRow
turboRingPortEntry=_TurboRingPortEntry_Object((1,3,6,1,4,1,8691,7,99,1,16,2,3,1))
turboRingPortEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:turboRingPortEntry.setStatus(_A)
_TurboRingPortIndex_Type=Integer32
_TurboRingPortIndex_Object=MibTableColumn
turboRingPortIndex=_TurboRingPortIndex_Object((1,3,6,1,4,1,8691,7,99,1,16,2,3,1,1),_TurboRingPortIndex_Type())
turboRingPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortIndex.setStatus(_A)
class _TurboRingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_g,0),('notTurboRingPort',1),(_U,2),(_V,3),(_S,4),(_O,5)))
_TurboRingPortStatus_Type.__name__=_C
_TurboRingPortStatus_Object=MibTableColumn
turboRingPortStatus=_TurboRingPortStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,2,3,1,2),_TurboRingPortStatus_Type())
turboRingPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortStatus.setStatus(_A)
_TurboRingPortDesignatedBridge_Type=MacAddress
_TurboRingPortDesignatedBridge_Object=MibTableColumn
turboRingPortDesignatedBridge=_TurboRingPortDesignatedBridge_Object((1,3,6,1,4,1,8691,7,99,1,16,2,3,1,3),_TurboRingPortDesignatedBridge_Type())
turboRingPortDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortDesignatedBridge.setStatus(_A)
_TurboRingPortDesignatedPort_Type=Integer32
_TurboRingPortDesignatedPort_Object=MibTableColumn
turboRingPortDesignatedPort=_TurboRingPortDesignatedPort_Object((1,3,6,1,4,1,8691,7,99,1,16,2,3,1,4),_TurboRingPortDesignatedPort_Type())
turboRingPortDesignatedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortDesignatedPort.setStatus(_A)
_TurboRingDesignatedMaster_Type=MacAddress
_TurboRingDesignatedMaster_Object=MibScalar
turboRingDesignatedMaster=_TurboRingDesignatedMaster_Object((1,3,6,1,4,1,8691,7,99,1,16,2,6),_TurboRingDesignatedMaster_Type())
turboRingDesignatedMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingDesignatedMaster.setStatus(_A)
_TurboRingRdntPort1_Type=Integer32
_TurboRingRdntPort1_Object=MibScalar
turboRingRdntPort1=_TurboRingRdntPort1_Object((1,3,6,1,4,1,8691,7,99,1,16,2,7),_TurboRingRdntPort1_Type())
turboRingRdntPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort1.setStatus(_A)
_TurboRingRdntPort2_Type=Integer32
_TurboRingRdntPort2_Object=MibScalar
turboRingRdntPort2=_TurboRingRdntPort2_Object((1,3,6,1,4,1,8691,7,99,1,16,2,8),_TurboRingRdntPort2_Type())
turboRingRdntPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort2.setStatus(_A)
class _TurboRingEnableCoupling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TurboRingEnableCoupling_Type.__name__=_C
_TurboRingEnableCoupling_Object=MibScalar
turboRingEnableCoupling=_TurboRingEnableCoupling_Object((1,3,6,1,4,1,8691,7,99,1,16,2,9),_TurboRingEnableCoupling_Type())
turboRingEnableCoupling.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingEnableCoupling.setStatus(_A)
_TurboRingCouplingPort_Type=Integer32
_TurboRingCouplingPort_Object=MibScalar
turboRingCouplingPort=_TurboRingCouplingPort_Object((1,3,6,1,4,1,8691,7,99,1,16,2,10),_TurboRingCouplingPort_Type())
turboRingCouplingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingCouplingPort.setStatus(_A)
class _TurboRingCouplingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5)));namedValues=NamedValues(*((_g,0),('notCouplingPort',1),(_U,2),(_V,3),(_O,5)))
_TurboRingCouplingPortStatus_Type.__name__=_C
_TurboRingCouplingPortStatus_Object=MibScalar
turboRingCouplingPortStatus=_TurboRingCouplingPortStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,2,11),_TurboRingCouplingPortStatus_Type())
turboRingCouplingPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingCouplingPortStatus.setStatus(_A)
_TurboRingControlPort_Type=Integer32
_TurboRingControlPort_Object=MibScalar
turboRingControlPort=_TurboRingControlPort_Object((1,3,6,1,4,1,8691,7,99,1,16,2,12),_TurboRingControlPort_Type())
turboRingControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingControlPort.setStatus(_A)
class _TurboRingControlPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7)));namedValues=NamedValues(*((_g,0),('notControlPort',1),(_U,2),(_V,3),(_O,5),(_u,6),(_K,7)))
_TurboRingControlPortStatus_Type.__name__=_C
_TurboRingControlPortStatus_Object=MibScalar
turboRingControlPortStatus=_TurboRingControlPortStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,2,13),_TurboRingControlPortStatus_Type())
turboRingControlPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingControlPortStatus.setStatus(_A)
class _TurboRingBrokenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_d,1),(_v,2)))
_TurboRingBrokenStatus_Type.__name__=_C
_TurboRingBrokenStatus_Object=MibScalar
turboRingBrokenStatus=_TurboRingBrokenStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,2,14),_TurboRingBrokenStatus_Type())
turboRingBrokenStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingBrokenStatus.setStatus(_A)
_SpanningTree_ObjectIdentity=ObjectIdentity
spanningTree=_SpanningTree_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,3))
class _SpanningTreeRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_SpanningTreeRoot_Type.__name__=_C
_SpanningTreeRoot_Object=MibScalar
spanningTreeRoot=_SpanningTreeRoot_Object((1,3,6,1,4,1,8691,7,99,1,16,3,1),_SpanningTreeRoot_Type())
spanningTreeRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreeRoot.setStatus(_A)
class _SpanningTreeBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4096,8192,12288,16384,20480,24576,28672,32768,36864,40960,45056,49152,53248,57344,61440)));namedValues=NamedValues(*((_e,0),('priority4096',4096),('priority8192',8192),('priority12288',12288),('priority16384',16384),('priority20480',20480),('priority24576',24576),('priority28672',28672),('priority32768',32768),('priority36864',36864),('priority40960',40960),('priority45056',45056),('priority49152',49152),('priority53248',53248),('priority57344',57344),('priority61440',61440)))
_SpanningTreeBridgePriority_Type.__name__=_C
_SpanningTreeBridgePriority_Object=MibScalar
spanningTreeBridgePriority=_SpanningTreeBridgePriority_Object((1,3,6,1,4,1,8691,7,99,1,16,3,2),_SpanningTreeBridgePriority_Type())
spanningTreeBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeBridgePriority.setStatus(_A)
_SpanningTreeHelloTime_Type=Integer32
_SpanningTreeHelloTime_Object=MibScalar
spanningTreeHelloTime=_SpanningTreeHelloTime_Object((1,3,6,1,4,1,8691,7,99,1,16,3,3),_SpanningTreeHelloTime_Type())
spanningTreeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeHelloTime.setStatus(_A)
_SpanningTreeMaxAge_Type=Integer32
_SpanningTreeMaxAge_Object=MibScalar
spanningTreeMaxAge=_SpanningTreeMaxAge_Object((1,3,6,1,4,1,8691,7,99,1,16,3,4),_SpanningTreeMaxAge_Type())
spanningTreeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeMaxAge.setStatus(_A)
_SpanningTreeForwardingDelay_Type=Integer32
_SpanningTreeForwardingDelay_Object=MibScalar
spanningTreeForwardingDelay=_SpanningTreeForwardingDelay_Object((1,3,6,1,4,1,8691,7,99,1,16,3,5),_SpanningTreeForwardingDelay_Type())
spanningTreeForwardingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeForwardingDelay.setStatus(_A)
_SpanningTreeTable_Object=MibTable
spanningTreeTable=_SpanningTreeTable_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6))
if mibBuilder.loadTexts:spanningTreeTable.setStatus(_A)
_SpanningTreeEntry_Object=MibTableRow
spanningTreeEntry=_SpanningTreeEntry_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1))
spanningTreeEntry.setIndexNames((0,_E,_AK))
if mibBuilder.loadTexts:spanningTreeEntry.setStatus(_A)
_SpanningTreeIndex_Type=Integer32
_SpanningTreeIndex_Object=MibTableColumn
spanningTreeIndex=_SpanningTreeIndex_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1,1),_SpanningTreeIndex_Type())
spanningTreeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreeIndex.setStatus(_A)
class _EnableSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableSpanningTree_Type.__name__=_C
_EnableSpanningTree_Object=MibTableColumn
enableSpanningTree=_EnableSpanningTree_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1,2),_EnableSpanningTree_Type())
enableSpanningTree.setMaxAccess(_B)
if mibBuilder.loadTexts:enableSpanningTree.setStatus(_A)
class _SpanningTreePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240)));namedValues=NamedValues(*((_e,0),('priority16',16),('priority32',32),('priority48',48),('priority64',64),('priority80',80),('priority96',96),('priority112',112),('priority128',128),('priority144',144),('priority160',160),('priority176',176),('priority192',192),('priority208',208),('priority224',224),('priority240',240)))
_SpanningTreePortPriority_Type.__name__=_C
_SpanningTreePortPriority_Object=MibTableColumn
spanningTreePortPriority=_SpanningTreePortPriority_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1,3),_SpanningTreePortPriority_Type())
spanningTreePortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortPriority.setStatus(_A)
_SpanningTreePortCost_Type=Integer32
_SpanningTreePortCost_Object=MibTableColumn
spanningTreePortCost=_SpanningTreePortCost_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1,4),_SpanningTreePortCost_Type())
spanningTreePortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortCost.setStatus(_A)
class _SpanningTreePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_g,0),('notSpanningTreePort',1),(_U,2),(_V,3),(_S,4),(_O,5)))
_SpanningTreePortStatus_Type.__name__=_C
_SpanningTreePortStatus_Object=MibTableColumn
spanningTreePortStatus=_SpanningTreePortStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1,5),_SpanningTreePortStatus_Type())
spanningTreePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreePortStatus.setStatus(_A)
class _SpanningTreePortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_o,0),('forceEdge',1),(_f,2)))
_SpanningTreePortEdge_Type.__name__=_C
_SpanningTreePortEdge_Object=MibTableColumn
spanningTreePortEdge=_SpanningTreePortEdge_Object((1,3,6,1,4,1,8691,7,99,1,16,3,6,1,6),_SpanningTreePortEdge_Type())
spanningTreePortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortEdge.setStatus(_A)
class _ActiveProtocolOfRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_L,0),(_q,1),(_r,2),(_s,3),(_t,4),('mstp',5)))
_ActiveProtocolOfRedundancy_Type.__name__=_C
_ActiveProtocolOfRedundancy_Object=MibScalar
activeProtocolOfRedundancy=_ActiveProtocolOfRedundancy_Object((1,3,6,1,4,1,8691,7,99,1,16,4),_ActiveProtocolOfRedundancy_Type())
activeProtocolOfRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:activeProtocolOfRedundancy.setStatus(_A)
_TurboRingV2_ObjectIdentity=ObjectIdentity
turboRingV2=_TurboRingV2_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,5))
_TurboRingV2Ring1_ObjectIdentity=ObjectIdentity
turboRingV2Ring1=_TurboRingV2Ring1_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,5,1))
class _RingIndexRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RingIndexRing1_Type.__name__=_C
_RingIndexRing1_Object=MibScalar
ringIndexRing1=_RingIndexRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,1),_RingIndexRing1_Type())
ringIndexRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:ringIndexRing1.setStatus(_A)
class _RingEnableRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RingEnableRing1_Type.__name__=_C
_RingEnableRing1_Object=MibScalar
ringEnableRing1=_RingEnableRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,2),_RingEnableRing1_Type())
ringEnableRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:ringEnableRing1.setStatus(_A)
class _MasterSetupRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_MasterSetupRing1_Type.__name__=_C
_MasterSetupRing1_Object=MibScalar
masterSetupRing1=_MasterSetupRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,3),_MasterSetupRing1_Type())
masterSetupRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:masterSetupRing1.setStatus(_A)
class _MasterStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_MasterStatusRing1_Type.__name__=_C
_MasterStatusRing1_Object=MibScalar
masterStatusRing1=_MasterStatusRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,4),_MasterStatusRing1_Type())
masterStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:masterStatusRing1.setStatus(_A)
_DesignatedMasterRing1_Type=MacAddress
_DesignatedMasterRing1_Object=MibScalar
designatedMasterRing1=_DesignatedMasterRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,5),_DesignatedMasterRing1_Type())
designatedMasterRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:designatedMasterRing1.setStatus(_A)
_Rdnt1stPortRing1_Type=Integer32
_Rdnt1stPortRing1_Object=MibScalar
rdnt1stPortRing1=_Rdnt1stPortRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,6),_Rdnt1stPortRing1_Type())
rdnt1stPortRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt1stPortRing1.setStatus(_A)
class _Rdnt1stPortStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_T,3),(_S,4),(_O,5)))
_Rdnt1stPortStatusRing1_Type.__name__=_C
_Rdnt1stPortStatusRing1_Object=MibScalar
rdnt1stPortStatusRing1=_Rdnt1stPortStatusRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,7),_Rdnt1stPortStatusRing1_Type())
rdnt1stPortStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt1stPortStatusRing1.setStatus(_A)
_Rdnt2ndPortRing1_Type=Integer32
_Rdnt2ndPortRing1_Object=MibScalar
rdnt2ndPortRing1=_Rdnt2ndPortRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,8),_Rdnt2ndPortRing1_Type())
rdnt2ndPortRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt2ndPortRing1.setStatus(_A)
class _Rdnt2ndPortStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_T,3),(_S,4),(_O,5)))
_Rdnt2ndPortStatusRing1_Type.__name__=_C
_Rdnt2ndPortStatusRing1_Object=MibScalar
rdnt2ndPortStatusRing1=_Rdnt2ndPortStatusRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,9),_Rdnt2ndPortStatusRing1_Type())
rdnt2ndPortStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt2ndPortStatusRing1.setStatus(_A)
class _BrokenStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_d,1),(_v,2)))
_BrokenStatusRing1_Type.__name__=_C
_BrokenStatusRing1_Object=MibScalar
brokenStatusRing1=_BrokenStatusRing1_Object((1,3,6,1,4,1,8691,7,99,1,16,5,1,10),_BrokenStatusRing1_Type())
brokenStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:brokenStatusRing1.setStatus(_A)
_TurboRingV2Ring2_ObjectIdentity=ObjectIdentity
turboRingV2Ring2=_TurboRingV2Ring2_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,5,2))
class _RingIndexRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RingIndexRing2_Type.__name__=_C
_RingIndexRing2_Object=MibScalar
ringIndexRing2=_RingIndexRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,1),_RingIndexRing2_Type())
ringIndexRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:ringIndexRing2.setStatus(_A)
class _RingEnableRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RingEnableRing2_Type.__name__=_C
_RingEnableRing2_Object=MibScalar
ringEnableRing2=_RingEnableRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,2),_RingEnableRing2_Type())
ringEnableRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:ringEnableRing2.setStatus(_A)
class _MasterSetupRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_MasterSetupRing2_Type.__name__=_C
_MasterSetupRing2_Object=MibScalar
masterSetupRing2=_MasterSetupRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,3),_MasterSetupRing2_Type())
masterSetupRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:masterSetupRing2.setStatus(_A)
class _MasterStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_MasterStatusRing2_Type.__name__=_C
_MasterStatusRing2_Object=MibScalar
masterStatusRing2=_MasterStatusRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,4),_MasterStatusRing2_Type())
masterStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:masterStatusRing2.setStatus(_A)
_DesignatedMasterRing2_Type=MacAddress
_DesignatedMasterRing2_Object=MibScalar
designatedMasterRing2=_DesignatedMasterRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,5),_DesignatedMasterRing2_Type())
designatedMasterRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:designatedMasterRing2.setStatus(_A)
_Rdnt1stPortRing2_Type=Integer32
_Rdnt1stPortRing2_Object=MibScalar
rdnt1stPortRing2=_Rdnt1stPortRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,6),_Rdnt1stPortRing2_Type())
rdnt1stPortRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt1stPortRing2.setStatus(_A)
class _Rdnt1stPortStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_T,3),(_S,4),(_O,5)))
_Rdnt1stPortStatusRing2_Type.__name__=_C
_Rdnt1stPortStatusRing2_Object=MibScalar
rdnt1stPortStatusRing2=_Rdnt1stPortStatusRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,7),_Rdnt1stPortStatusRing2_Type())
rdnt1stPortStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt1stPortStatusRing2.setStatus(_A)
_Rdnt2ndPortRing2_Type=Integer32
_Rdnt2ndPortRing2_Object=MibScalar
rdnt2ndPortRing2=_Rdnt2ndPortRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,8),_Rdnt2ndPortRing2_Type())
rdnt2ndPortRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt2ndPortRing2.setStatus(_A)
class _Rdnt2ndPortStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_T,3),(_S,4),(_O,5)))
_Rdnt2ndPortStatusRing2_Type.__name__=_C
_Rdnt2ndPortStatusRing2_Object=MibScalar
rdnt2ndPortStatusRing2=_Rdnt2ndPortStatusRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,9),_Rdnt2ndPortStatusRing2_Type())
rdnt2ndPortStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt2ndPortStatusRing2.setStatus(_A)
class _BrokenStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_d,1),(_v,2)))
_BrokenStatusRing2_Type.__name__=_C
_BrokenStatusRing2_Object=MibScalar
brokenStatusRing2=_BrokenStatusRing2_Object((1,3,6,1,4,1,8691,7,99,1,16,5,2,10),_BrokenStatusRing2_Type())
brokenStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:brokenStatusRing2.setStatus(_A)
_TurboRingV2Coupling_ObjectIdentity=ObjectIdentity
turboRingV2Coupling=_TurboRingV2Coupling_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,5,3))
class _CouplingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_CouplingEnable_Type.__name__=_C
_CouplingEnable_Object=MibScalar
couplingEnable=_CouplingEnable_Object((1,3,6,1,4,1,8691,7,99,1,16,5,3,1),_CouplingEnable_Type())
couplingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:couplingEnable.setStatus(_A)
class _CouplingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dualHoming',1),('couplingBackup',2),('couplingPrimary',3)))
_CouplingMode_Type.__name__=_C
_CouplingMode_Object=MibScalar
couplingMode=_CouplingMode_Object((1,3,6,1,4,1,8691,7,99,1,16,5,3,2),_CouplingMode_Type())
couplingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:couplingMode.setStatus(_A)
_Coupling1stPort_Type=Integer32
_Coupling1stPort_Object=MibScalar
coupling1stPort=_Coupling1stPort_Object((1,3,6,1,4,1,8691,7,99,1,16,5,3,3),_Coupling1stPort_Type())
coupling1stPort.setMaxAccess(_B)
if mibBuilder.loadTexts:coupling1stPort.setStatus(_A)
class _Coupling1stPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_T,3),(_S,4),(_O,5)))
_Coupling1stPortStatus_Type.__name__=_C
_Coupling1stPortStatus_Object=MibScalar
coupling1stPortStatus=_Coupling1stPortStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,5,3,4),_Coupling1stPortStatus_Type())
coupling1stPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coupling1stPortStatus.setStatus(_A)
_Coupling2ndPort_Type=Integer32
_Coupling2ndPort_Object=MibScalar
coupling2ndPort=_Coupling2ndPort_Object((1,3,6,1,4,1,8691,7,99,1,16,5,3,5),_Coupling2ndPort_Type())
coupling2ndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:coupling2ndPort.setStatus(_A)
class _Coupling2ndPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_T,3),(_S,4),(_O,5)))
_Coupling2ndPortStatus_Type.__name__=_C
_Coupling2ndPortStatus_Object=MibScalar
coupling2ndPortStatus=_Coupling2ndPortStatus_Object((1,3,6,1,4,1,8691,7,99,1,16,5,3,6),_Coupling2ndPortStatus_Type())
coupling2ndPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coupling2ndPortStatus.setStatus(_A)
_TurboChain_ObjectIdentity=ObjectIdentity
turboChain=_TurboChain_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,16,6))
class _TurboChainRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('head',1),('member',2),('tail',3)))
_TurboChainRole_Type.__name__=_C
_TurboChainRole_Object=MibScalar
turboChainRole=_TurboChainRole_Object((1,3,6,1,4,1,8691,7,99,1,16,6,1),_TurboChainRole_Type())
turboChainRole.setMaxAccess(_B)
if mibBuilder.loadTexts:turboChainRole.setStatus(_A)
_TurboChainPort1_Type=Integer32
_TurboChainPort1_Object=MibScalar
turboChainPort1=_TurboChainPort1_Object((1,3,6,1,4,1,8691,7,99,1,16,6,2),_TurboChainPort1_Type())
turboChainPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboChainPort1.setStatus(_A)
_TurboChainPort2_Type=Integer32
_TurboChainPort2_Object=MibScalar
turboChainPort2=_TurboChainPort2_Object((1,3,6,1,4,1,8691,7,99,1,16,6,3),_TurboChainPort2_Type())
turboChainPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboChainPort2.setStatus(_A)
class _TurboChainPort1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AL,0),(_U,1),(_T,2),(_V,3),(_O,4),(_I,5)))
_TurboChainPort1Status_Type.__name__=_C
_TurboChainPort1Status_Object=MibScalar
turboChainPort1Status=_TurboChainPort1Status_Object((1,3,6,1,4,1,8691,7,99,1,16,6,4),_TurboChainPort1Status_Type())
turboChainPort1Status.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort1Status.setStatus(_A)
class _TurboChainPort2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AL,0),(_U,1),(_T,2),(_V,3),(_O,4),(_I,5)))
_TurboChainPort2Status_Type.__name__=_C
_TurboChainPort2Status_Object=MibScalar
turboChainPort2Status=_TurboChainPort2Status_Object((1,3,6,1,4,1,8691,7,99,1,16,6,5),_TurboChainPort2Status_Type())
turboChainPort2Status.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort2Status.setStatus(_A)
_TurboChainPort1PartnerBridge_Type=MacAddress
_TurboChainPort1PartnerBridge_Object=MibScalar
turboChainPort1PartnerBridge=_TurboChainPort1PartnerBridge_Object((1,3,6,1,4,1,8691,7,99,1,16,6,6),_TurboChainPort1PartnerBridge_Type())
turboChainPort1PartnerBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort1PartnerBridge.setStatus(_A)
_TurboChainPort2PartnerBridge_Type=MacAddress
_TurboChainPort2PartnerBridge_Object=MibScalar
turboChainPort2PartnerBridge=_TurboChainPort2PartnerBridge_Object((1,3,6,1,4,1,8691,7,99,1,16,6,7),_TurboChainPort2PartnerBridge_Type())
turboChainPort2PartnerBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort2PartnerBridge.setStatus(_A)
_RelayWarning_ObjectIdentity=ObjectIdentity
relayWarning=_RelayWarning_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,17))
_RelayWarningTable_Object=MibTable
relayWarningTable=_RelayWarningTable_Object((1,3,6,1,4,1,8691,7,99,1,17,11))
if mibBuilder.loadTexts:relayWarningTable.setStatus(_A)
_RelayWarningEntry_Object=MibTableRow
relayWarningEntry=_RelayWarningEntry_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1))
relayWarningEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:relayWarningEntry.setStatus(_A)
_RelayAlarmIndex_Type=Integer32
_RelayAlarmIndex_Object=MibTableColumn
relayAlarmIndex=_RelayAlarmIndex_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,1),_RelayAlarmIndex_Type())
relayAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:relayAlarmIndex.setStatus(_A)
class _RelayWarningRelayContact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('opened',1)))
_RelayWarningRelayContact_Type.__name__=_C
_RelayWarningRelayContact_Object=MibTableColumn
relayWarningRelayContact=_RelayWarningRelayContact_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,2),_RelayWarningRelayContact_Type())
relayWarningRelayContact.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningRelayContact.setStatus(_A)
class _OverrideRelayWarningSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_OverrideRelayWarningSetting_Type.__name__=_C
_OverrideRelayWarningSetting_Object=MibTableColumn
overrideRelayWarningSetting=_OverrideRelayWarningSetting_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,3),_OverrideRelayWarningSetting_Type())
overrideRelayWarningSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:overrideRelayWarningSetting.setStatus(_A)
class _RelayWarningPower1Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RelayWarningPower1Off_Type.__name__=_C
_RelayWarningPower1Off_Object=MibTableColumn
relayWarningPower1Off=_RelayWarningPower1Off_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,4),_RelayWarningPower1Off_Type())
relayWarningPower1Off.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningPower1Off.setStatus(_A)
class _RelayWarningPower1OffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RelayWarningPower1OffStatus_Type.__name__=_C
_RelayWarningPower1OffStatus_Object=MibTableColumn
relayWarningPower1OffStatus=_RelayWarningPower1OffStatus_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,5),_RelayWarningPower1OffStatus_Type())
relayWarningPower1OffStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningPower1OffStatus.setStatus(_A)
class _RelayWarningPower2Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RelayWarningPower2Off_Type.__name__=_C
_RelayWarningPower2Off_Object=MibTableColumn
relayWarningPower2Off=_RelayWarningPower2Off_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,6),_RelayWarningPower2Off_Type())
relayWarningPower2Off.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningPower2Off.setStatus(_A)
class _RelayWarningPower2OffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RelayWarningPower2OffStatus_Type.__name__=_C
_RelayWarningPower2OffStatus_Object=MibTableColumn
relayWarningPower2OffStatus=_RelayWarningPower2OffStatus_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,7),_RelayWarningPower2OffStatus_Type())
relayWarningPower2OffStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningPower2OffStatus.setStatus(_A)
class _RelayWarningTurboRingBreak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RelayWarningTurboRingBreak_Type.__name__=_C
_RelayWarningTurboRingBreak_Object=MibTableColumn
relayWarningTurboRingBreak=_RelayWarningTurboRingBreak_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,8),_RelayWarningTurboRingBreak_Type())
relayWarningTurboRingBreak.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTurboRingBreak.setStatus(_A)
class _RelayWarningTurboRingBreakStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RelayWarningTurboRingBreakStatus_Type.__name__=_C
_RelayWarningTurboRingBreakStatus_Object=MibTableColumn
relayWarningTurboRingBreakStatus=_RelayWarningTurboRingBreakStatus_Object((1,3,6,1,4,1,8691,7,99,1,17,11,1,9),_RelayWarningTurboRingBreakStatus_Type())
relayWarningTurboRingBreakStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningTurboRingBreakStatus.setStatus(_A)
_PortRelayWarningTable_Object=MibTable
portRelayWarningTable=_PortRelayWarningTable_Object((1,3,6,1,4,1,8691,7,99,1,17,12))
if mibBuilder.loadTexts:portRelayWarningTable.setStatus(_A)
_PortRelayWarningEntry_Object=MibTableRow
portRelayWarningEntry=_PortRelayWarningEntry_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1))
portRelayWarningEntry.setIndexNames((0,_E,_M),(0,_E,_h))
if mibBuilder.loadTexts:portRelayWarningEntry.setStatus(_A)
class _RelayWarningLinkChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ignore',0),(_w,1),(_x,2)))
_RelayWarningLinkChanged_Type.__name__=_C
_RelayWarningLinkChanged_Object=MibTableColumn
relayWarningLinkChanged=_RelayWarningLinkChanged_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1,1),_RelayWarningLinkChanged_Type())
relayWarningLinkChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningLinkChanged.setStatus(_A)
class _RelayWarningLinkChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RelayWarningLinkChangedStatus_Type.__name__=_C
_RelayWarningLinkChangedStatus_Object=MibTableColumn
relayWarningLinkChangedStatus=_RelayWarningLinkChangedStatus_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1,2),_RelayWarningLinkChangedStatus_Type())
relayWarningLinkChangedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningLinkChangedStatus.setStatus(_A)
class _RelayWarningTrafficOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RelayWarningTrafficOverload_Type.__name__=_C
_RelayWarningTrafficOverload_Object=MibTableColumn
relayWarningTrafficOverload=_RelayWarningTrafficOverload_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1,3),_RelayWarningTrafficOverload_Type())
relayWarningTrafficOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficOverload.setStatus(_A)
class _RelayWarningTrafficOverloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RelayWarningTrafficOverloadStatus_Type.__name__=_C
_RelayWarningTrafficOverloadStatus_Object=MibTableColumn
relayWarningTrafficOverloadStatus=_RelayWarningTrafficOverloadStatus_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1,4),_RelayWarningTrafficOverloadStatus_Type())
relayWarningTrafficOverloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningTrafficOverloadStatus.setStatus(_A)
_RelayWarningRxTrafficThreshold_Type=Integer32
_RelayWarningRxTrafficThreshold_Object=MibTableColumn
relayWarningRxTrafficThreshold=_RelayWarningRxTrafficThreshold_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1,5),_RelayWarningRxTrafficThreshold_Type())
relayWarningRxTrafficThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningRxTrafficThreshold.setStatus(_A)
_RelayWarningTrafficDuration_Type=Integer32
_RelayWarningTrafficDuration_Object=MibTableColumn
relayWarningTrafficDuration=_RelayWarningTrafficDuration_Object((1,3,6,1,4,1,8691,7,99,1,17,12,1,6),_RelayWarningTrafficDuration_Type())
relayWarningTrafficDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficDuration.setStatus(_A)
_DiRelayWarningTable_Object=MibTable
diRelayWarningTable=_DiRelayWarningTable_Object((1,3,6,1,4,1,8691,7,99,1,17,13))
if mibBuilder.loadTexts:diRelayWarningTable.setStatus(_A)
_DiRelayWarningEntry_Object=MibTableRow
diRelayWarningEntry=_DiRelayWarningEntry_Object((1,3,6,1,4,1,8691,7,99,1,17,13,1))
diRelayWarningEntry.setIndexNames((0,_E,_p),(0,_E,_h))
if mibBuilder.loadTexts:diRelayWarningEntry.setStatus(_A)
class _RelayWarningDiInputChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_b,1),(_c,2)))
_RelayWarningDiInputChanged_Type.__name__=_C
_RelayWarningDiInputChanged_Object=MibTableColumn
relayWarningDiInputChanged=_RelayWarningDiInputChanged_Object((1,3,6,1,4,1,8691,7,99,1,17,13,1,1),_RelayWarningDiInputChanged_Type())
relayWarningDiInputChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningDiInputChanged.setStatus(_A)
class _RelayWarningDiInputChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RelayWarningDiInputChangedStatus_Type.__name__=_C
_RelayWarningDiInputChangedStatus_Object=MibTableColumn
relayWarningDiInputChangedStatus=_RelayWarningDiInputChangedStatus_Object((1,3,6,1,4,1,8691,7,99,1,17,13,1,2),_RelayWarningDiInputChangedStatus_Type())
relayWarningDiInputChangedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningDiInputChangedStatus.setStatus(_A)
_TrafficPrioritization_ObjectIdentity=ObjectIdentity
trafficPrioritization=_TrafficPrioritization_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,18))
_QosClassification_ObjectIdentity=ObjectIdentity
qosClassification=_QosClassification_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,18,1))
class _QueuingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('schedweightfair',0),('schedstrict',1)))
_QueuingMechanism_Type.__name__=_C
_QueuingMechanism_Object=MibScalar
queuingMechanism=_QueuingMechanism_Object((1,3,6,1,4,1,8691,7,99,1,18,1,1),_QueuingMechanism_Type())
queuingMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:queuingMechanism.setStatus(_A)
_QosPortTable_Object=MibTable
qosPortTable=_QosPortTable_Object((1,3,6,1,4,1,8691,7,99,1,18,1,2))
if mibBuilder.loadTexts:qosPortTable.setStatus(_A)
_QosPortEntry_Object=MibTableRow
qosPortEntry=_QosPortEntry_Object((1,3,6,1,4,1,8691,7,99,1,18,1,2,1))
qosPortEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:qosPortEntry.setStatus(_A)
class _InspectTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_InspectTos_Type.__name__=_C
_InspectTos_Object=MibTableColumn
inspectTos=_InspectTos_Object((1,3,6,1,4,1,8691,7,99,1,18,1,2,1,1),_InspectTos_Type())
inspectTos.setMaxAccess(_B)
if mibBuilder.loadTexts:inspectTos.setStatus(_A)
class _InspectCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_InspectCos_Type.__name__=_C
_InspectCos_Object=MibTableColumn
inspectCos=_InspectCos_Object((1,3,6,1,4,1,8691,7,99,1,18,1,2,1,2),_InspectCos_Type())
inspectCos.setMaxAccess(_B)
if mibBuilder.loadTexts:inspectCos.setStatus(_A)
class _PortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,0),(_i,1),(_j,2),(_y,3),(_z,4),(_A0,5),(_A1,6),(_A2,7)))
_PortPriority_Type.__name__=_C
_PortPriority_Object=MibTableColumn
portPriority=_PortPriority_Object((1,3,6,1,4,1,8691,7,99,1,18,1,2,1,3),_PortPriority_Type())
portPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:portPriority.setStatus(_A)
_CosMapping_ObjectIdentity=ObjectIdentity
cosMapping=_CosMapping_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,18,2))
_CosMappingTable_Object=MibTable
cosMappingTable=_CosMappingTable_Object((1,3,6,1,4,1,8691,7,99,1,18,2,1))
if mibBuilder.loadTexts:cosMappingTable.setStatus(_A)
_CosMappingEntry_Object=MibTableRow
cosMappingEntry=_CosMappingEntry_Object((1,3,6,1,4,1,8691,7,99,1,18,2,1,1))
cosMappingEntry.setIndexNames((0,_E,'cosTag'))
if mibBuilder.loadTexts:cosMappingEntry.setStatus(_A)
class _CosTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CosTag_Type.__name__=_C
_CosTag_Object=MibTableColumn
cosTag=_CosTag_Object((1,3,6,1,4,1,8691,7,99,1,18,2,1,1,1),_CosTag_Type())
cosTag.setMaxAccess(_D)
if mibBuilder.loadTexts:cosTag.setStatus(_A)
class _CosMappedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,0),(_i,1),(_j,2),(_y,3),(_z,4),(_A0,5),(_A1,6),(_A2,7)))
_CosMappedPriority_Type.__name__=_C
_CosMappedPriority_Object=MibTableColumn
cosMappedPriority=_CosMappedPriority_Object((1,3,6,1,4,1,8691,7,99,1,18,2,1,1,2),_CosMappedPriority_Type())
cosMappedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cosMappedPriority.setStatus(_A)
_TosMapping_ObjectIdentity=ObjectIdentity
tosMapping=_TosMapping_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,18,3))
_TosMappingTable_Object=MibTable
tosMappingTable=_TosMappingTable_Object((1,3,6,1,4,1,8691,7,99,1,18,3,1))
if mibBuilder.loadTexts:tosMappingTable.setStatus(_A)
_TosMappingEntry_Object=MibTableRow
tosMappingEntry=_TosMappingEntry_Object((1,3,6,1,4,1,8691,7,99,1,18,3,1,1))
tosMappingEntry.setIndexNames((0,_E,'tosClass'))
if mibBuilder.loadTexts:tosMappingEntry.setStatus(_A)
_TosClass_Type=Integer32
_TosClass_Object=MibTableColumn
tosClass=_TosClass_Object((1,3,6,1,4,1,8691,7,99,1,18,3,1,1,1),_TosClass_Type())
tosClass.setMaxAccess(_D)
if mibBuilder.loadTexts:tosClass.setStatus(_A)
class _TosMappedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,0),(_i,1),(_j,2),(_y,3),(_z,4),(_A0,5),(_A1,6),(_A2,7)))
_TosMappedPriority_Type.__name__=_C
_TosMappedPriority_Object=MibTableColumn
tosMappedPriority=_TosMappedPriority_Object((1,3,6,1,4,1,8691,7,99,1,18,3,1,1,2),_TosMappedPriority_Type())
tosMappedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tosMappedPriority.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,19))
_VlanPortSettingTable_Object=MibTable
vlanPortSettingTable=_VlanPortSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,19,1))
if mibBuilder.loadTexts:vlanPortSettingTable.setStatus(_A)
_VlanPortSettingEntry_Object=MibTableRow
vlanPortSettingEntry=_VlanPortSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,19,1,1))
vlanPortSettingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:vlanPortSettingEntry.setStatus(_A)
class _PortVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('access',0),('trunk',1),('hybrid',2)))
_PortVlanType_Type.__name__=_C
_PortVlanType_Object=MibTableColumn
portVlanType=_PortVlanType_Object((1,3,6,1,4,1,8691,7,99,1,19,1,1,1),_PortVlanType_Type())
portVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:portVlanType.setStatus(_A)
class _PortDefaultVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortDefaultVid_Type.__name__=_C
_PortDefaultVid_Object=MibTableColumn
portDefaultVid=_PortDefaultVid_Object((1,3,6,1,4,1,8691,7,99,1,19,1,1,2),_PortDefaultVid_Type())
portDefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portDefaultVid.setStatus(_A)
_PortFixedVid_Type=DisplayString
_PortFixedVid_Object=MibTableColumn
portFixedVid=_PortFixedVid_Object((1,3,6,1,4,1,8691,7,99,1,19,1,1,3),_PortFixedVid_Type())
portFixedVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portFixedVid.setStatus(_A)
_PortForbiddenVid_Type=DisplayString
_PortForbiddenVid_Object=MibTableColumn
portForbiddenVid=_PortForbiddenVid_Object((1,3,6,1,4,1,8691,7,99,1,19,1,1,4),_PortForbiddenVid_Type())
portForbiddenVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portForbiddenVid.setStatus(_A)
_PortFixedVidUntag_Type=DisplayString
_PortFixedVidUntag_Object=MibTableColumn
portFixedVidUntag=_PortFixedVidUntag_Object((1,3,6,1,4,1,8691,7,99,1,19,1,1,5),_PortFixedVidUntag_Type())
portFixedVidUntag.setMaxAccess(_B)
if mibBuilder.loadTexts:portFixedVidUntag.setStatus(_A)
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,8691,7,99,1,19,2))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,8691,7,99,1,19,2,1))
vlanEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanId_Type.__name__=_C
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,8691,7,99,1,19,2,1,1),_VlanId_Type())
vlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
_JoinedAccessPorts_Type=PortList
_JoinedAccessPorts_Object=MibTableColumn
joinedAccessPorts=_JoinedAccessPorts_Object((1,3,6,1,4,1,8691,7,99,1,19,2,1,2),_JoinedAccessPorts_Type())
joinedAccessPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedAccessPorts.setStatus(_A)
_JoinedTrunkPorts_Type=PortList
_JoinedTrunkPorts_Object=MibTableColumn
joinedTrunkPorts=_JoinedTrunkPorts_Object((1,3,6,1,4,1,8691,7,99,1,19,2,1,3),_JoinedTrunkPorts_Type())
joinedTrunkPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedTrunkPorts.setStatus(_A)
_JoinedHybridPorts_Type=PortList
_JoinedHybridPorts_Object=MibTableColumn
joinedHybridPorts=_JoinedHybridPorts_Object((1,3,6,1,4,1,8691,7,99,1,19,2,1,4),_JoinedHybridPorts_Type())
joinedHybridPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedHybridPorts.setStatus(_A)
_ManagementVlanId_Type=Integer32
_ManagementVlanId_Object=MibScalar
managementVlanId=_ManagementVlanId_Object((1,3,6,1,4,1,8691,7,99,1,19,3),_ManagementVlanId_Type())
managementVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:managementVlanId.setStatus(_A)
class _VlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('tagBased',0))
_VlanType_Type.__name__=_C
_VlanType_Object=MibScalar
vlanType=_VlanType_Object((1,3,6,1,4,1,8691,7,99,1,19,4),_VlanType_Type())
vlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanType.setStatus(_A)
class _EnableGvrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableGvrp_Type.__name__=_C
_EnableGvrp_Object=MibScalar
enableGvrp=_EnableGvrp_Object((1,3,6,1,4,1,8691,7,99,1,19,6),_EnableGvrp_Type())
enableGvrp.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGvrp.setStatus(_A)
_QinqSettingTable_Object=MibTable
qinqSettingTable=_QinqSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,19,7))
if mibBuilder.loadTexts:qinqSettingTable.setStatus(_A)
_QinqSettingEntry_Object=MibTableRow
qinqSettingEntry=_QinqSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,19,7,1))
qinqSettingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:qinqSettingEntry.setStatus(_A)
class _QinqEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_QinqEnable_Type.__name__=_C
_QinqEnable_Object=MibTableColumn
qinqEnable=_QinqEnable_Object((1,3,6,1,4,1,8691,7,99,1,19,7,1,1),_QinqEnable_Type())
qinqEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qinqEnable.setStatus(_A)
_QinqTpid_Type=DisplayString
_QinqTpid_Object=MibTableColumn
qinqTpid=_QinqTpid_Object((1,3,6,1,4,1,8691,7,99,1,19,7,1,2),_QinqTpid_Type())
qinqTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:qinqTpid.setStatus(_A)
_MulticastFiltering_ObjectIdentity=ObjectIdentity
multicastFiltering=_MulticastFiltering_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,20))
_IgmpSnooping_ObjectIdentity=ObjectIdentity
igmpSnooping=_IgmpSnooping_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,20,1))
class _QuerierQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,600))
_QuerierQueryInterval_Type.__name__=_C
_QuerierQueryInterval_Object=MibScalar
querierQueryInterval=_QuerierQueryInterval_Object((1,3,6,1,4,1,8691,7,99,1,20,1,1),_QuerierQueryInterval_Type())
querierQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:querierQueryInterval.setStatus(_A)
_IgmpSnoopingSettingTable_Object=MibTable
igmpSnoopingSettingTable=_IgmpSnoopingSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,20,1,2))
if mibBuilder.loadTexts:igmpSnoopingSettingTable.setStatus(_A)
_IgmpSnoopingSettingEntry_Object=MibTableRow
igmpSnoopingSettingEntry=_IgmpSnoopingSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,20,1,2,1))
igmpSnoopingSettingEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:igmpSnoopingSettingEntry.setStatus(_A)
class _EnableIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableIgmpSnooping_Type.__name__=_C
_EnableIgmpSnooping_Object=MibTableColumn
enableIgmpSnooping=_EnableIgmpSnooping_Object((1,3,6,1,4,1,8691,7,99,1,20,1,2,1,1),_EnableIgmpSnooping_Type())
enableIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:enableIgmpSnooping.setStatus(_A)
class _EnableQuerier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('igmp-v2',1),('igmp-v3',2)))
_EnableQuerier_Type.__name__=_C
_EnableQuerier_Object=MibTableColumn
enableQuerier=_EnableQuerier_Object((1,3,6,1,4,1,8691,7,99,1,20,1,2,1,2),_EnableQuerier_Type())
enableQuerier.setMaxAccess(_B)
if mibBuilder.loadTexts:enableQuerier.setStatus(_A)
_FixedMulticastQuerierPorts_Type=PortList
_FixedMulticastQuerierPorts_Object=MibTableColumn
fixedMulticastQuerierPorts=_FixedMulticastQuerierPorts_Object((1,3,6,1,4,1,8691,7,99,1,20,1,2,1,3),_FixedMulticastQuerierPorts_Type())
fixedMulticastQuerierPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fixedMulticastQuerierPorts.setStatus(_A)
_LearnedMulticastQuerierPorts_Type=PortList
_LearnedMulticastQuerierPorts_Object=MibTableColumn
learnedMulticastQuerierPorts=_LearnedMulticastQuerierPorts_Object((1,3,6,1,4,1,8691,7,99,1,20,1,2,1,4),_LearnedMulticastQuerierPorts_Type())
learnedMulticastQuerierPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:learnedMulticastQuerierPorts.setStatus(_A)
class _EnableGlobalIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableGlobalIgmpSnooping_Type.__name__=_C
_EnableGlobalIgmpSnooping_Object=MibScalar
enableGlobalIgmpSnooping=_EnableGlobalIgmpSnooping_Object((1,3,6,1,4,1,8691,7,99,1,20,1,4),_EnableGlobalIgmpSnooping_Type())
enableGlobalIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGlobalIgmpSnooping.setStatus(_A)
_IgmpSnoopingStreamTable_Object=MibTable
igmpSnoopingStreamTable=_IgmpSnoopingStreamTable_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6))
if mibBuilder.loadTexts:igmpSnoopingStreamTable.setStatus(_A)
_IgmpSnoopingStreamEntry_Object=MibTableRow
igmpSnoopingStreamEntry=_IgmpSnoopingStreamEntry_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6,1))
igmpSnoopingStreamEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:igmpSnoopingStreamEntry.setStatus(_A)
_IgmpSnoopingStreamIndex_Type=Integer32
_IgmpSnoopingStreamIndex_Object=MibTableColumn
igmpSnoopingStreamIndex=_IgmpSnoopingStreamIndex_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6,1,1),_IgmpSnoopingStreamIndex_Type())
igmpSnoopingStreamIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingStreamIndex.setStatus(_A)
_IgmpSnoopingStreamGroup_Type=IpAddress
_IgmpSnoopingStreamGroup_Object=MibTableColumn
igmpSnoopingStreamGroup=_IgmpSnoopingStreamGroup_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6,1,2),_IgmpSnoopingStreamGroup_Type())
igmpSnoopingStreamGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingStreamGroup.setStatus(_A)
_IgmpSnoopingStreamSource_Type=IpAddress
_IgmpSnoopingStreamSource_Object=MibTableColumn
igmpSnoopingStreamSource=_IgmpSnoopingStreamSource_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6,1,3),_IgmpSnoopingStreamSource_Type())
igmpSnoopingStreamSource.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingStreamSource.setStatus(_A)
_IgmpSnoopingStreamPort_Type=Integer32
_IgmpSnoopingStreamPort_Object=MibTableColumn
igmpSnoopingStreamPort=_IgmpSnoopingStreamPort_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6,1,4),_IgmpSnoopingStreamPort_Type())
igmpSnoopingStreamPort.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingStreamPort.setStatus(_A)
_IgmpSnoopingMemberPorts_Type=PortList
_IgmpSnoopingMemberPorts_Object=MibTableColumn
igmpSnoopingMemberPorts=_IgmpSnoopingMemberPorts_Object((1,3,6,1,4,1,8691,7,99,1,20,1,6,1,5),_IgmpSnoopingMemberPorts_Type())
igmpSnoopingMemberPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingMemberPorts.setStatus(_A)
class _MulticastFastForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_MulticastFastForwarding_Type.__name__=_C
_MulticastFastForwarding_Object=MibScalar
multicastFastForwarding=_MulticastFastForwarding_Object((1,3,6,1,4,1,8691,7,99,1,20,1,7),_MulticastFastForwarding_Type())
multicastFastForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:multicastFastForwarding.setStatus(_A)
_StaticMulticast_ObjectIdentity=ObjectIdentity
staticMulticast=_StaticMulticast_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,20,2))
_StaticMulticastTable_Object=MibTable
staticMulticastTable=_StaticMulticastTable_Object((1,3,6,1,4,1,8691,7,99,1,20,2,1))
if mibBuilder.loadTexts:staticMulticastTable.setStatus(_A)
_StaticMulticastEntry_Object=MibTableRow
staticMulticastEntry=_StaticMulticastEntry_Object((1,3,6,1,4,1,8691,7,99,1,20,2,1,1))
staticMulticastEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:staticMulticastEntry.setStatus(_A)
_StaticMulticastAddress_Type=MacAddress
_StaticMulticastAddress_Object=MibTableColumn
staticMulticastAddress=_StaticMulticastAddress_Object((1,3,6,1,4,1,8691,7,99,1,20,2,1,1,1),_StaticMulticastAddress_Type())
staticMulticastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:staticMulticastAddress.setStatus(_A)
_StaticMulticastPorts_Type=PortList
_StaticMulticastPorts_Object=MibTableColumn
staticMulticastPorts=_StaticMulticastPorts_Object((1,3,6,1,4,1,8691,7,99,1,20,2,1,1,2),_StaticMulticastPorts_Type())
staticMulticastPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:staticMulticastPorts.setStatus(_A)
class _StaticMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_StaticMulticastStatus_Type.__name__=_C
_StaticMulticastStatus_Object=MibTableColumn
staticMulticastStatus=_StaticMulticastStatus_Object((1,3,6,1,4,1,8691,7,99,1,20,2,1,1,3),_StaticMulticastStatus_Type())
staticMulticastStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:staticMulticastStatus.setStatus(_A)
_Gmrp_ObjectIdentity=ObjectIdentity
gmrp=_Gmrp_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,20,3))
_GmrpSettingTable_Object=MibTable
gmrpSettingTable=_GmrpSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,20,3,1))
if mibBuilder.loadTexts:gmrpSettingTable.setStatus(_A)
_GmrpSettingEntry_Object=MibTableRow
gmrpSettingEntry=_GmrpSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,20,3,1,1))
gmrpSettingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:gmrpSettingEntry.setStatus(_A)
class _EnableGMRP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableGMRP_Type.__name__=_C
_EnableGMRP_Object=MibTableColumn
enableGMRP=_EnableGMRP_Object((1,3,6,1,4,1,8691,7,99,1,20,3,1,1,1),_EnableGMRP_Type())
enableGMRP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGMRP.setStatus(_A)
_GmrpTable_Object=MibTable
gmrpTable=_GmrpTable_Object((1,3,6,1,4,1,8691,7,99,1,20,3,2))
if mibBuilder.loadTexts:gmrpTable.setStatus(_A)
_GmrpEntry_Object=MibTableRow
gmrpEntry=_GmrpEntry_Object((1,3,6,1,4,1,8691,7,99,1,20,3,2,1))
gmrpEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:gmrpEntry.setStatus(_A)
_GmrpMulticastGroup_Type=MacAddress
_GmrpMulticastGroup_Object=MibTableColumn
gmrpMulticastGroup=_GmrpMulticastGroup_Object((1,3,6,1,4,1,8691,7,99,1,20,3,2,1,1),_GmrpMulticastGroup_Type())
gmrpMulticastGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:gmrpMulticastGroup.setStatus(_A)
_GmrpFixedPorts_Type=PortList
_GmrpFixedPorts_Object=MibTableColumn
gmrpFixedPorts=_GmrpFixedPorts_Object((1,3,6,1,4,1,8691,7,99,1,20,3,2,1,2),_GmrpFixedPorts_Type())
gmrpFixedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:gmrpFixedPorts.setStatus(_A)
_GmrpLearnedPorts_Type=PortList
_GmrpLearnedPorts_Object=MibTableColumn
gmrpLearnedPorts=_GmrpLearnedPorts_Object((1,3,6,1,4,1,8691,7,99,1,20,3,2,1,3),_GmrpLearnedPorts_Type())
gmrpLearnedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:gmrpLearnedPorts.setStatus(_A)
_Mfb_ObjectIdentity=ObjectIdentity
mfb=_Mfb_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,20,4))
_MfbSettingTable_Object=MibTable
mfbSettingTable=_MfbSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,20,4,1))
if mibBuilder.loadTexts:mfbSettingTable.setStatus(_A)
_MfbSettingEntry_Object=MibTableRow
mfbSettingEntry=_MfbSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,20,4,1,1))
mfbSettingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:mfbSettingEntry.setStatus(_A)
class _FilterBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forwardAll',1),('forwardUnknown',2),('filterUnknown',3)))
_FilterBehavior_Type.__name__=_C
_FilterBehavior_Object=MibTableColumn
filterBehavior=_FilterBehavior_Object((1,3,6,1,4,1,8691,7,99,1,20,4,1,1,1),_FilterBehavior_Type())
filterBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:filterBehavior.setStatus(_A)
_RateLimiting_ObjectIdentity=ObjectIdentity
rateLimiting=_RateLimiting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,21))
_NormalModeRateLimitingIngressTable_Object=MibTable
normalModeRateLimitingIngressTable=_NormalModeRateLimitingIngressTable_Object((1,3,6,1,4,1,8691,7,99,1,21,1))
if mibBuilder.loadTexts:normalModeRateLimitingIngressTable.setStatus(_A)
_NormalModeRateLimitingIngressEntry_Object=MibTableRow
normalModeRateLimitingIngressEntry=_NormalModeRateLimitingIngressEntry_Object((1,3,6,1,4,1,8691,7,99,1,21,1,1))
normalModeRateLimitingIngressEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:normalModeRateLimitingIngressEntry.setStatus(_A)
class _LimitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('bmucast',1),('bmcast',2),('bcast',3)))
_LimitMode_Type.__name__=_C
_LimitMode_Object=MibTableColumn
limitMode=_LimitMode_Object((1,3,6,1,4,1,8691,7,99,1,21,1,1,1),_LimitMode_Type())
limitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:limitMode.setStatus(_A)
class _IngressLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notlimit',0),('limit128k',1),('limit256k',2),('limit512k',3),('limit1M',4),('limit2M',5),('limit4M',6),('limit8M',7)))
_IngressLimitRate_Type.__name__=_C
_IngressLimitRate_Object=MibTableColumn
ingressLimitRate=_IngressLimitRate_Object((1,3,6,1,4,1,8691,7,99,1,21,1,1,2),_IngressLimitRate_Type())
ingressLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressLimitRate.setStatus(_A)
class _EgressLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_AP,0),('percentage03',1),('percentage05',2),('percentage10',3),('percentage15',4),('percentage25',5),('percentage35',6),('percentage50',7),('percentage65',8),('percentage85',9)))
_EgressLimit_Type.__name__=_C
_EgressLimit_Object=MibTableColumn
egressLimit=_EgressLimit_Object((1,3,6,1,4,1,8691,7,99,1,21,1,1,3),_EgressLimit_Type())
egressLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:egressLimit.setStatus(_A)
_BroadcastStormProtection_ObjectIdentity=ObjectIdentity
broadcastStormProtection=_BroadcastStormProtection_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,21,2))
_UnicastFilterBehavior_ObjectIdentity=ObjectIdentity
unicastFilterBehavior=_UnicastFilterBehavior_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,21,2,1))
class _UfbIncludeUnkonwnUcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_UfbIncludeUnkonwnUcast_Type.__name__=_C
_UfbIncludeUnkonwnUcast_Object=MibScalar
ufbIncludeUnkonwnUcast=_UfbIncludeUnkonwnUcast_Object((1,3,6,1,4,1,8691,7,99,1,21,2,1,1),_UfbIncludeUnkonwnUcast_Type())
ufbIncludeUnkonwnUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ufbIncludeUnkonwnUcast.setStatus(_A)
_PortDisableMode_ObjectIdentity=ObjectIdentity
portDisableMode=_PortDisableMode_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,21,3))
class _PortDisableModePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PortDisableModePeriod_Type.__name__=_C
_PortDisableModePeriod_Object=MibScalar
portDisableModePeriod=_PortDisableModePeriod_Object((1,3,6,1,4,1,8691,7,99,1,21,3,1),_PortDisableModePeriod_Type())
portDisableModePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:portDisableModePeriod.setStatus(_A)
_PortDisableModeTable_Object=MibTable
portDisableModeTable=_PortDisableModeTable_Object((1,3,6,1,4,1,8691,7,99,1,21,3,2))
if mibBuilder.loadTexts:portDisableModeTable.setStatus(_A)
_PortDisableModeEntry_Object=MibTableRow
portDisableModeEntry=_PortDisableModeEntry_Object((1,3,6,1,4,1,8691,7,99,1,21,3,2,1))
portDisableModeEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:portDisableModeEntry.setStatus(_A)
class _IngressLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_AP,0),('rateMega1Fps4464',1),('rateMega2Fps7441',2),('rateMega3Fps14881',3),('rateMega4Fps22322',4),('rateMega5Fps37203',5),('rateMega6Fps52084',6),('rateMega7Fps74405',7),('rateGiga1Fps44640',8),('rateGiga2Fps74410',9),('rateGiga3Fps148810',10),('rateGiga4Fps223220',11),('rateGiga5Fps372030',12),('rateGiga6Fps520840',13),('rateGiga7Fps744050',14)))
_IngressLimit_Type.__name__=_C
_IngressLimit_Object=MibTableColumn
ingressLimit=_IngressLimit_Object((1,3,6,1,4,1,8691,7,99,1,21,3,2,1,1),_IngressLimit_Type())
ingressLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressLimit.setStatus(_A)
class _RateLimitingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),('portDisable',1)))
_RateLimitingMode_Type.__name__=_C
_RateLimitingMode_Object=MibScalar
rateLimitingMode=_RateLimitingMode_Object((1,3,6,1,4,1,8691,7,99,1,21,4),_RateLimitingMode_Type())
rateLimitingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitingMode.setStatus(_A)
_Security_ObjectIdentity=ObjectIdentity
security=_Security_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22))
_UserLoginSetting_ObjectIdentity=ObjectIdentity
userLoginSetting=_UserLoginSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,1))
class _UserLoginServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tacacs',1),('radius',2)))
_UserLoginServer_Type.__name__=_C
_UserLoginServer_Object=MibScalar
userLoginServer=_UserLoginServer_Object((1,3,6,1,4,1,8691,7,99,1,22,1,1),_UserLoginServer_Type())
userLoginServer.setMaxAccess(_B)
if mibBuilder.loadTexts:userLoginServer.setStatus(_A)
_TacacsServerSetting_ObjectIdentity=ObjectIdentity
tacacsServerSetting=_TacacsServerSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,1,2))
_TacacsLoginAuthServer_Type=DisplayString
_TacacsLoginAuthServer_Object=MibScalar
tacacsLoginAuthServer=_TacacsLoginAuthServer_Object((1,3,6,1,4,1,8691,7,99,1,22,1,2,1),_TacacsLoginAuthServer_Type())
tacacsLoginAuthServer.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsLoginAuthServer.setStatus(_A)
class _TacacsLoginAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacacsLoginAuthPort_Type.__name__=_C
_TacacsLoginAuthPort_Object=MibScalar
tacacsLoginAuthPort=_TacacsLoginAuthPort_Object((1,3,6,1,4,1,8691,7,99,1,22,1,2,2),_TacacsLoginAuthPort_Type())
tacacsLoginAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsLoginAuthPort.setStatus(_A)
_TacacsLoginAuthSharedKey_Type=DisplayString
_TacacsLoginAuthSharedKey_Object=MibScalar
tacacsLoginAuthSharedKey=_TacacsLoginAuthSharedKey_Object((1,3,6,1,4,1,8691,7,99,1,22,1,2,3),_TacacsLoginAuthSharedKey_Type())
tacacsLoginAuthSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsLoginAuthSharedKey.setStatus(_A)
class _TacacsLoginAuthAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ascii',0),('pap',1),('chap',2),('arap',3),('mschap',4)))
_TacacsLoginAuthAuthType_Type.__name__=_C
_TacacsLoginAuthAuthType_Object=MibScalar
tacacsLoginAuthAuthType=_TacacsLoginAuthAuthType_Object((1,3,6,1,4,1,8691,7,99,1,22,1,2,4),_TacacsLoginAuthAuthType_Type())
tacacsLoginAuthAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsLoginAuthAuthType.setStatus(_A)
class _TacacsLoginAuthTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TacacsLoginAuthTimeout_Type.__name__=_C
_TacacsLoginAuthTimeout_Object=MibScalar
tacacsLoginAuthTimeout=_TacacsLoginAuthTimeout_Object((1,3,6,1,4,1,8691,7,99,1,22,1,2,5),_TacacsLoginAuthTimeout_Type())
tacacsLoginAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsLoginAuthTimeout.setStatus(_A)
_RadiusServerSetting_ObjectIdentity=ObjectIdentity
radiusServerSetting=_RadiusServerSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,1,3))
_RadiusLoginAuthServer_Type=DisplayString
_RadiusLoginAuthServer_Object=MibScalar
radiusLoginAuthServer=_RadiusLoginAuthServer_Object((1,3,6,1,4,1,8691,7,99,1,22,1,3,1),_RadiusLoginAuthServer_Type())
radiusLoginAuthServer.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusLoginAuthServer.setStatus(_A)
class _RadiusLoginAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusLoginAuthPort_Type.__name__=_C
_RadiusLoginAuthPort_Object=MibScalar
radiusLoginAuthPort=_RadiusLoginAuthPort_Object((1,3,6,1,4,1,8691,7,99,1,22,1,3,2),_RadiusLoginAuthPort_Type())
radiusLoginAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusLoginAuthPort.setStatus(_A)
_RadiusLoginAuthSharedKey_Type=DisplayString
_RadiusLoginAuthSharedKey_Object=MibScalar
radiusLoginAuthSharedKey=_RadiusLoginAuthSharedKey_Object((1,3,6,1,4,1,8691,7,99,1,22,1,3,3),_RadiusLoginAuthSharedKey_Type())
radiusLoginAuthSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusLoginAuthSharedKey.setStatus(_A)
class _RadiusLoginAuthAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('eap-md5',0))
_RadiusLoginAuthAuthType_Type.__name__=_C
_RadiusLoginAuthAuthType_Object=MibScalar
radiusLoginAuthAuthType=_RadiusLoginAuthAuthType_Object((1,3,6,1,4,1,8691,7,99,1,22,1,3,4),_RadiusLoginAuthAuthType_Type())
radiusLoginAuthAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusLoginAuthAuthType.setStatus(_A)
class _RadiusLoginAuthTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RadiusLoginAuthTimeout_Type.__name__=_C
_RadiusLoginAuthTimeout_Object=MibScalar
radiusLoginAuthTimeout=_RadiusLoginAuthTimeout_Object((1,3,6,1,4,1,8691,7,99,1,22,1,3,5),_RadiusLoginAuthTimeout_Type())
radiusLoginAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusLoginAuthTimeout.setStatus(_A)
_PortAccessControl_ObjectIdentity=ObjectIdentity
portAccessControl=_PortAccessControl_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,2))
_StaticPortLock_ObjectIdentity=ObjectIdentity
staticPortLock=_StaticPortLock_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,2,1))
_StaticPortLockAddress_Type=MacAddress
_StaticPortLockAddress_Object=MibScalar
staticPortLockAddress=_StaticPortLockAddress_Object((1,3,6,1,4,1,8691,7,99,1,22,2,1,1),_StaticPortLockAddress_Type())
staticPortLockAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:staticPortLockAddress.setStatus(_A)
_StaticPortLockPort_Type=Integer32
_StaticPortLockPort_Object=MibScalar
staticPortLockPort=_StaticPortLockPort_Object((1,3,6,1,4,1,8691,7,99,1,22,2,1,2),_StaticPortLockPort_Type())
staticPortLockPort.setMaxAccess(_F)
if mibBuilder.loadTexts:staticPortLockPort.setStatus(_A)
class _StaticPortLockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_K,1),(_P,4)))
_StaticPortLockStatus_Type.__name__=_C
_StaticPortLockStatus_Object=MibScalar
staticPortLockStatus=_StaticPortLockStatus_Object((1,3,6,1,4,1,8691,7,99,1,22,2,1,3),_StaticPortLockStatus_Type())
staticPortLockStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:staticPortLockStatus.setStatus(_A)
_Dot1x_ObjectIdentity=ObjectIdentity
dot1x=_Dot1x_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,2,2))
class _DataBaseOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('radius',2),('radiuslocal',3)))
_DataBaseOption_Type.__name__=_C
_DataBaseOption_Object=MibScalar
dataBaseOption=_DataBaseOption_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,1),_DataBaseOption_Type())
dataBaseOption.setMaxAccess(_B)
if mibBuilder.loadTexts:dataBaseOption.setStatus(_A)
class _Dot1xReauthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Dot1xReauthEnable_Type.__name__=_C
_Dot1xReauthEnable_Object=MibScalar
dot1xReauthEnable=_Dot1xReauthEnable_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,5),_Dot1xReauthEnable_Type())
dot1xReauthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xReauthEnable.setStatus(_A)
class _Dot1xReauthPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_Dot1xReauthPeriod_Type.__name__=_C
_Dot1xReauthPeriod_Object=MibScalar
dot1xReauthPeriod=_Dot1xReauthPeriod_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,6),_Dot1xReauthPeriod_Type())
dot1xReauthPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xReauthPeriod.setStatus(_A)
_Dot1xSettingTable_Object=MibTable
dot1xSettingTable=_Dot1xSettingTable_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,7))
if mibBuilder.loadTexts:dot1xSettingTable.setStatus(_A)
_Dot1xSettingEntry_Object=MibTableRow
dot1xSettingEntry=_Dot1xSettingEntry_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,7,1))
dot1xSettingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:dot1xSettingEntry.setStatus(_A)
class _EnableDot1X_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableDot1X_Type.__name__=_C
_EnableDot1X_Object=MibTableColumn
enableDot1X=_EnableDot1X_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,7,1,1),_EnableDot1X_Type())
enableDot1X.setMaxAccess(_B)
if mibBuilder.loadTexts:enableDot1X.setStatus(_A)
_Dot1xReauthTable_Object=MibTable
dot1xReauthTable=_Dot1xReauthTable_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,8))
if mibBuilder.loadTexts:dot1xReauthTable.setStatus(_A)
_Dot1xReauthEntry_Object=MibTableRow
dot1xReauthEntry=_Dot1xReauthEntry_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,8,1))
dot1xReauthEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:dot1xReauthEntry.setStatus(_A)
_Dot1xReauthPortIndex_Type=Integer32
_Dot1xReauthPortIndex_Object=MibTableColumn
dot1xReauthPortIndex=_Dot1xReauthPortIndex_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,8,1,1),_Dot1xReauthPortIndex_Type())
dot1xReauthPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xReauthPortIndex.setStatus(_A)
class _Dot1xReauth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_Dot1xReauth_Type.__name__=_C
_Dot1xReauth_Object=MibTableColumn
dot1xReauth=_Dot1xReauth_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,8,1,2),_Dot1xReauth_Type())
dot1xReauth.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xReauth.setStatus(_A)
_Dot1xRadius_ObjectIdentity=ObjectIdentity
dot1xRadius=_Dot1xRadius_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,22,2,2,9))
class _Dot1xSameAsAuthServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notSame',0),('same',1)))
_Dot1xSameAsAuthServer_Type.__name__=_C
_Dot1xSameAsAuthServer_Object=MibScalar
dot1xSameAsAuthServer=_Dot1xSameAsAuthServer_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,1),_Dot1xSameAsAuthServer_Type())
dot1xSameAsAuthServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xSameAsAuthServer.setStatus(_A)
_Dot1x1stRadiusServer_Type=DisplayString
_Dot1x1stRadiusServer_Object=MibScalar
dot1x1stRadiusServer=_Dot1x1stRadiusServer_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,2),_Dot1x1stRadiusServer_Type())
dot1x1stRadiusServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1x1stRadiusServer.setStatus(_A)
class _Dot1x1stRadiusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1x1stRadiusPort_Type.__name__=_C
_Dot1x1stRadiusPort_Object=MibScalar
dot1x1stRadiusPort=_Dot1x1stRadiusPort_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,3),_Dot1x1stRadiusPort_Type())
dot1x1stRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1x1stRadiusPort.setStatus(_A)
_Dot1x1stRadiusSharedKey_Type=DisplayString
_Dot1x1stRadiusSharedKey_Object=MibScalar
dot1x1stRadiusSharedKey=_Dot1x1stRadiusSharedKey_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,4),_Dot1x1stRadiusSharedKey_Type())
dot1x1stRadiusSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1x1stRadiusSharedKey.setStatus(_A)
_Dot1x2ndRadiusServer_Type=DisplayString
_Dot1x2ndRadiusServer_Object=MibScalar
dot1x2ndRadiusServer=_Dot1x2ndRadiusServer_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,5),_Dot1x2ndRadiusServer_Type())
dot1x2ndRadiusServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1x2ndRadiusServer.setStatus(_A)
class _Dot1x2ndRadiusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1x2ndRadiusPort_Type.__name__=_C
_Dot1x2ndRadiusPort_Object=MibScalar
dot1x2ndRadiusPort=_Dot1x2ndRadiusPort_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,6),_Dot1x2ndRadiusPort_Type())
dot1x2ndRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1x2ndRadiusPort.setStatus(_A)
_Dot1x2ndRadiusSharedKey_Type=DisplayString
_Dot1x2ndRadiusSharedKey_Object=MibScalar
dot1x2ndRadiusSharedKey=_Dot1x2ndRadiusSharedKey_Object((1,3,6,1,4,1,8691,7,99,1,22,2,2,9,7),_Dot1x2ndRadiusSharedKey_Type())
dot1x2ndRadiusSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1x2ndRadiusSharedKey.setStatus(_A)
_PortAccessControlTable_Object=MibTable
portAccessControlTable=_PortAccessControlTable_Object((1,3,6,1,4,1,8691,7,99,1,22,2,3))
if mibBuilder.loadTexts:portAccessControlTable.setStatus(_A)
_PortAccessControlEntry_Object=MibTableRow
portAccessControlEntry=_PortAccessControlEntry_Object((1,3,6,1,4,1,8691,7,99,1,22,2,3,1))
portAccessControlEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:portAccessControlEntry.setStatus(_A)
_PortAccessControlAddress_Type=MacAddress
_PortAccessControlAddress_Object=MibTableColumn
portAccessControlAddress=_PortAccessControlAddress_Object((1,3,6,1,4,1,8691,7,99,1,22,2,3,1,1),_PortAccessControlAddress_Type())
portAccessControlAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:portAccessControlAddress.setStatus(_A)
_PortAccessControlPortNo_Type=Integer32
_PortAccessControlPortNo_Object=MibTableColumn
portAccessControlPortNo=_PortAccessControlPortNo_Object((1,3,6,1,4,1,8691,7,99,1,22,2,3,1,2),_PortAccessControlPortNo_Type())
portAccessControlPortNo.setMaxAccess(_D)
if mibBuilder.loadTexts:portAccessControlPortNo.setStatus(_A)
class _PortAccessControlAccessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('staticLock',1),('authorized',2),('unAuthorized',3),('authorizing',4)))
_PortAccessControlAccessStatus_Type.__name__=_C
_PortAccessControlAccessStatus_Object=MibTableColumn
portAccessControlAccessStatus=_PortAccessControlAccessStatus_Object((1,3,6,1,4,1,8691,7,99,1,22,2,3,1,3),_PortAccessControlAccessStatus_Type())
portAccessControlAccessStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portAccessControlAccessStatus.setStatus(_A)
class _PortAccessControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_PortAccessControlStatus_Type.__name__=_C
_PortAccessControlStatus_Object=MibTableColumn
portAccessControlStatus=_PortAccessControlStatus_Object((1,3,6,1,4,1,8691,7,99,1,22,2,3,1,4),_PortAccessControlStatus_Type())
portAccessControlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:portAccessControlStatus.setStatus(_A)
_AccessibleIP_ObjectIdentity=ObjectIdentity
accessibleIP=_AccessibleIP_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,30))
class _EnableAccessibleIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableAccessibleIP_Type.__name__=_C
_EnableAccessibleIP_Object=MibScalar
enableAccessibleIP=_EnableAccessibleIP_Object((1,3,6,1,4,1,8691,7,99,1,30,1),_EnableAccessibleIP_Type())
enableAccessibleIP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAccessibleIP.setStatus(_A)
_AccessibleIpTable_Object=MibTable
accessibleIpTable=_AccessibleIpTable_Object((1,3,6,1,4,1,8691,7,99,1,30,2))
if mibBuilder.loadTexts:accessibleIpTable.setStatus(_A)
_AccessibleIpEntry_Object=MibTableRow
accessibleIpEntry=_AccessibleIpEntry_Object((1,3,6,1,4,1,8691,7,99,1,30,2,1))
accessibleIpEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:accessibleIpEntry.setStatus(_A)
_AccessibleIpAddress_Type=IpAddress
_AccessibleIpAddress_Object=MibTableColumn
accessibleIpAddress=_AccessibleIpAddress_Object((1,3,6,1,4,1,8691,7,99,1,30,2,1,1),_AccessibleIpAddress_Type())
accessibleIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:accessibleIpAddress.setStatus(_A)
_AccessibleIpNetMask_Type=IpAddress
_AccessibleIpNetMask_Object=MibTableColumn
accessibleIpNetMask=_AccessibleIpNetMask_Object((1,3,6,1,4,1,8691,7,99,1,30,2,1,2),_AccessibleIpNetMask_Type())
accessibleIpNetMask.setMaxAccess(_F)
if mibBuilder.loadTexts:accessibleIpNetMask.setStatus(_A)
class _AccessibleIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_AccessibleIpStatus_Type.__name__=_C
_AccessibleIpStatus_Object=MibTableColumn
accessibleIpStatus=_AccessibleIpStatus_Object((1,3,6,1,4,1,8691,7,99,1,30,2,1,3),_AccessibleIpStatus_Type())
accessibleIpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:accessibleIpStatus.setStatus(_A)
_SysFileUpdate_ObjectIdentity=ObjectIdentity
sysFileUpdate=_SysFileUpdate_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,31))
_TftpServer_Type=DisplayString
_TftpServer_Object=MibScalar
tftpServer=_TftpServer_Object((1,3,6,1,4,1,8691,7,99,1,31,1),_TftpServer_Type())
tftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpServer.setStatus(_A)
_FirmwarePathName_Type=DisplayString
_FirmwarePathName_Object=MibScalar
firmwarePathName=_FirmwarePathName_Object((1,3,6,1,4,1,8691,7,99,1,31,2),_FirmwarePathName_Type())
firmwarePathName.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwarePathName.setStatus(_A)
_LogPathName_Type=DisplayString
_LogPathName_Object=MibScalar
logPathName=_LogPathName_Object((1,3,6,1,4,1,8691,7,99,1,31,3),_LogPathName_Type())
logPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:logPathName.setStatus(_A)
_ConfPathName_Type=DisplayString
_ConfPathName_Object=MibScalar
confPathName=_ConfPathName_Object((1,3,6,1,4,1,8691,7,99,1,31,4),_ConfPathName_Type())
confPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:confPathName.setStatus(_A)
class _TftpUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('importFirmware',1),('importConfig',2),('exportConfig',3),('exportLog',4)))
_TftpUpdate_Type.__name__=_C
_TftpUpdate_Object=MibScalar
tftpUpdate=_TftpUpdate_Object((1,3,6,1,4,1,8691,7,99,1,31,5),_TftpUpdate_Type())
tftpUpdate.setMaxAccess(_F)
if mibBuilder.loadTexts:tftpUpdate.setStatus(_A)
_TimeSetting_ObjectIdentity=ObjectIdentity
timeSetting=_TimeSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,32))
_SysDateTime_Type=DateAndTime
_SysDateTime_Object=MibScalar
sysDateTime=_SysDateTime_Object((1,3,6,1,4,1,8691,7,99,1,32,1),_SysDateTime_Type())
sysDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDateTime.setStatus(_A)
_CalibratePeriod_Type=Integer32
_CalibratePeriod_Object=MibScalar
calibratePeriod=_CalibratePeriod_Object((1,3,6,1,4,1,8691,7,99,1,32,2),_CalibratePeriod_Type())
calibratePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:calibratePeriod.setStatus(_A)
_TimeServer1_Type=DisplayString
_TimeServer1_Object=MibScalar
timeServer1=_TimeServer1_Object((1,3,6,1,4,1,8691,7,99,1,32,3),_TimeServer1_Type())
timeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer1.setStatus(_A)
_TimeServer2_Type=DisplayString
_TimeServer2_Object=MibScalar
timeServer2=_TimeServer2_Object((1,3,6,1,4,1,8691,7,99,1,32,4),_TimeServer2_Type())
timeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer2.setStatus(_A)
_DaylightSaving_ObjectIdentity=ObjectIdentity
daylightSaving=_DaylightSaving_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,32,5))
class _StartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_I,0),('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_StartMonth_Type.__name__=_C
_StartMonth_Object=MibScalar
startMonth=_StartMonth_Object((1,3,6,1,4,1,8691,7,99,1,32,5,1),_StartMonth_Type())
startMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:startMonth.setStatus(_A)
class _StartWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6)));namedValues=NamedValues(*((_I,0),('week1',1),('week2',2),('week3',3),('week4',4),('weeklast',6)))
_StartWeek_Type.__name__=_C
_StartWeek_Object=MibScalar
startWeek=_StartWeek_Object((1,3,6,1,4,1,8691,7,99,1,32,5,2),_StartWeek_Type())
startWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:startWeek.setStatus(_A)
class _StartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_StartDay_Type.__name__=_C
_StartDay_Object=MibScalar
startDay=_StartDay_Object((1,3,6,1,4,1,8691,7,99,1,32,5,3),_StartDay_Type())
startDay.setMaxAccess(_B)
if mibBuilder.loadTexts:startDay.setStatus(_A)
_StartHour_Type=Integer32
_StartHour_Object=MibScalar
startHour=_StartHour_Object((1,3,6,1,4,1,8691,7,99,1,32,5,4),_StartHour_Type())
startHour.setMaxAccess(_B)
if mibBuilder.loadTexts:startHour.setStatus(_A)
class _EndMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_I,0),('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_EndMonth_Type.__name__=_C
_EndMonth_Object=MibScalar
endMonth=_EndMonth_Object((1,3,6,1,4,1,8691,7,99,1,32,5,5),_EndMonth_Type())
endMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:endMonth.setStatus(_A)
class _EndWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6)));namedValues=NamedValues(*((_I,0),('week1',1),('week2',2),('week3',3),('week4',4),('weeklast',6)))
_EndWeek_Type.__name__=_C
_EndWeek_Object=MibScalar
endWeek=_EndWeek_Object((1,3,6,1,4,1,8691,7,99,1,32,5,6),_EndWeek_Type())
endWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:endWeek.setStatus(_A)
class _EndDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_EndDay_Type.__name__=_C
_EndDay_Object=MibScalar
endDay=_EndDay_Object((1,3,6,1,4,1,8691,7,99,1,32,5,7),_EndDay_Type())
endDay.setMaxAccess(_B)
if mibBuilder.loadTexts:endDay.setStatus(_A)
_EndHour_Type=Integer32
_EndHour_Object=MibScalar
endHour=_EndHour_Object((1,3,6,1,4,1,8691,7,99,1,32,5,8),_EndHour_Type())
endHour.setMaxAccess(_B)
if mibBuilder.loadTexts:endHour.setStatus(_A)
_OffsetHours_Type=Integer32
_OffsetHours_Object=MibScalar
offsetHours=_OffsetHours_Object((1,3,6,1,4,1,8691,7,99,1,32,5,9),_OffsetHours_Type())
offsetHours.setMaxAccess(_B)
if mibBuilder.loadTexts:offsetHours.setStatus(_A)
class _EnableNTPServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableNTPServer_Type.__name__=_C
_EnableNTPServer_Object=MibScalar
enableNTPServer=_EnableNTPServer_Object((1,3,6,1,4,1,8691,7,99,1,32,6),_EnableNTPServer_Type())
enableNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:enableNTPServer.setStatus(_A)
class _TimeProtocolOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('sntp',1),('ntp',2)))
_TimeProtocolOption_Type.__name__=_C
_TimeProtocolOption_Object=MibScalar
timeProtocolOption=_TimeProtocolOption_Object((1,3,6,1,4,1,8691,7,99,1,32,7),_TimeProtocolOption_Type())
timeProtocolOption.setMaxAccess(_B)
if mibBuilder.loadTexts:timeProtocolOption.setStatus(_A)
_BackupMediaSetting_ObjectIdentity=ObjectIdentity
backupMediaSetting=_BackupMediaSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,35))
class _BackupMediaAutoLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_BackupMediaAutoLoad_Type.__name__=_C
_BackupMediaAutoLoad_Object=MibScalar
backupMediaAutoLoad=_BackupMediaAutoLoad_Object((1,3,6,1,4,1,8691,7,99,1,35,1),_BackupMediaAutoLoad_Type())
backupMediaAutoLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:backupMediaAutoLoad.setStatus(_A)
class _EnableWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_N,1)))
_EnableWarmStart_Type.__name__=_C
_EnableWarmStart_Object=MibScalar
enableWarmStart=_EnableWarmStart_Object((1,3,6,1,4,1,8691,7,99,1,36),_EnableWarmStart_Type())
enableWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:enableWarmStart.setStatus(_A)
_SyslogSetting_ObjectIdentity=ObjectIdentity
syslogSetting=_SyslogSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,37))
_SyslogServer1_Type=DisplayString
_SyslogServer1_Object=MibScalar
syslogServer1=_SyslogServer1_Object((1,3,6,1,4,1,8691,7,99,1,37,1),_SyslogServer1_Type())
syslogServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer1.setStatus(_A)
_SyslogServer1port_Type=Integer32
_SyslogServer1port_Object=MibScalar
syslogServer1port=_SyslogServer1port_Object((1,3,6,1,4,1,8691,7,99,1,37,2),_SyslogServer1port_Type())
syslogServer1port.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer1port.setStatus(_A)
_SyslogServer2_Type=DisplayString
_SyslogServer2_Object=MibScalar
syslogServer2=_SyslogServer2_Object((1,3,6,1,4,1,8691,7,99,1,37,3),_SyslogServer2_Type())
syslogServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer2.setStatus(_A)
_SyslogServer2port_Type=Integer32
_SyslogServer2port_Object=MibScalar
syslogServer2port=_SyslogServer2port_Object((1,3,6,1,4,1,8691,7,99,1,37,4),_SyslogServer2port_Type())
syslogServer2port.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer2port.setStatus(_A)
_SyslogServer3_Type=DisplayString
_SyslogServer3_Object=MibScalar
syslogServer3=_SyslogServer3_Object((1,3,6,1,4,1,8691,7,99,1,37,5),_SyslogServer3_Type())
syslogServer3.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer3.setStatus(_A)
_SyslogServer3port_Type=Integer32
_SyslogServer3port_Object=MibScalar
syslogServer3port=_SyslogServer3port_Object((1,3,6,1,4,1,8691,7,99,1,37,6),_SyslogServer3port_Type())
syslogServer3port.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer3port.setStatus(_A)
_DhcpRelayAgentSetting_ObjectIdentity=ObjectIdentity
dhcpRelayAgentSetting=_DhcpRelayAgentSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,39))
_DhcpServer1_Type=DisplayString
_DhcpServer1_Object=MibScalar
dhcpServer1=_DhcpServer1_Object((1,3,6,1,4,1,8691,7,99,1,39,1),_DhcpServer1_Type())
dhcpServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer1.setStatus(_A)
_DhcpServer2_Type=DisplayString
_DhcpServer2_Object=MibScalar
dhcpServer2=_DhcpServer2_Object((1,3,6,1,4,1,8691,7,99,1,39,2),_DhcpServer2_Type())
dhcpServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer2.setStatus(_A)
_DhcpServer3_Type=DisplayString
_DhcpServer3_Object=MibScalar
dhcpServer3=_DhcpServer3_Object((1,3,6,1,4,1,8691,7,99,1,39,3),_DhcpServer3_Type())
dhcpServer3.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer3.setStatus(_A)
_DhcpServer4_Type=DisplayString
_DhcpServer4_Object=MibScalar
dhcpServer4=_DhcpServer4_Object((1,3,6,1,4,1,8691,7,99,1,39,4),_DhcpServer4_Type())
dhcpServer4.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer4.setStatus(_A)
_Option82Setting_ObjectIdentity=ObjectIdentity
option82Setting=_Option82Setting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,39,5))
class _EnableOption82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableOption82_Type.__name__=_C
_EnableOption82_Object=MibScalar
enableOption82=_EnableOption82_Object((1,3,6,1,4,1,8691,7,99,1,39,5,1),_EnableOption82_Type())
enableOption82.setMaxAccess(_B)
if mibBuilder.loadTexts:enableOption82.setStatus(_A)
class _Option82Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ip',0),('mac',1),('client-id',2),('other',3)))
_Option82Type_Type.__name__=_C
_Option82Type_Object=MibScalar
option82Type=_Option82Type_Object((1,3,6,1,4,1,8691,7,99,1,39,5,2),_Option82Type_Type())
option82Type.setMaxAccess(_B)
if mibBuilder.loadTexts:option82Type.setStatus(_A)
_Option82Value_Type=DisplayString
_Option82Value_Object=MibScalar
option82Value=_Option82Value_Object((1,3,6,1,4,1,8691,7,99,1,39,5,3),_Option82Value_Type())
option82Value.setMaxAccess(_B)
if mibBuilder.loadTexts:option82Value.setStatus(_A)
_Option82ValueDisplay_Type=DisplayString
_Option82ValueDisplay_Object=MibScalar
option82ValueDisplay=_Option82ValueDisplay_Object((1,3,6,1,4,1,8691,7,99,1,39,5,4),_Option82ValueDisplay_Type())
option82ValueDisplay.setMaxAccess(_D)
if mibBuilder.loadTexts:option82ValueDisplay.setStatus(_A)
_DhcpFunctionTable_Object=MibTable
dhcpFunctionTable=_DhcpFunctionTable_Object((1,3,6,1,4,1,8691,7,99,1,39,6))
if mibBuilder.loadTexts:dhcpFunctionTable.setStatus(_A)
_DhcpFunctionEntry_Object=MibTableRow
dhcpFunctionEntry=_DhcpFunctionEntry_Object((1,3,6,1,4,1,8691,7,99,1,39,6,1))
dhcpFunctionEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:dhcpFunctionEntry.setStatus(_A)
_DhcpPortIndex_Type=Integer32
_DhcpPortIndex_Object=MibTableColumn
dhcpPortIndex=_DhcpPortIndex_Object((1,3,6,1,4,1,8691,7,99,1,39,6,1,1),_DhcpPortIndex_Type())
dhcpPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpPortIndex.setStatus(_A)
_CircuitID_Type=DisplayString
_CircuitID_Object=MibTableColumn
circuitID=_CircuitID_Object((1,3,6,1,4,1,8691,7,99,1,39,6,1,2),_CircuitID_Type())
circuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:circuitID.setStatus(_A)
class _Option82Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Option82Enable_Type.__name__=_C
_Option82Enable_Object=MibTableColumn
option82Enable=_Option82Enable_Object((1,3,6,1,4,1,8691,7,99,1,39,6,1,3),_Option82Enable_Type())
option82Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:option82Enable.setStatus(_A)
_Ieee1588Setting_ObjectIdentity=ObjectIdentity
ieee1588Setting=_Ieee1588Setting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,41))
_Ptpv1Setting_ObjectIdentity=ObjectIdentity
ptpv1Setting=_Ptpv1Setting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,41,1))
class _EnablePtpv1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnablePtpv1_Type.__name__=_C
_EnablePtpv1_Object=MibScalar
enablePtpv1=_EnablePtpv1_Object((1,3,6,1,4,1,8691,7,99,1,41,1,1),_EnablePtpv1_Type())
enablePtpv1.setMaxAccess(_B)
if mibBuilder.loadTexts:enablePtpv1.setStatus(_A)
class _ClockModev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('v1BC',0),(_AU,1),(_AV,2),('v2P2PTC',3),('v2E2EBC',4),('v2P2PBC',5)))
_ClockModev1_Type.__name__=_C
_ClockModev1_Object=MibScalar
clockModev1=_ClockModev1_Object((1,3,6,1,4,1,8691,7,99,1,41,1,2),_ClockModev1_Type())
clockModev1.setMaxAccess(_B)
if mibBuilder.loadTexts:clockModev1.setStatus(_A)
class _SyncIntervalv1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('oneSec',0),('twoSec',1),('fourSec',2),('eightSec',3),('sixteenSec',4)))
_SyncIntervalv1_Type.__name__=_C
_SyncIntervalv1_Object=MibScalar
syncIntervalv1=_SyncIntervalv1_Object((1,3,6,1,4,1,8691,7,99,1,41,1,3),_SyncIntervalv1_Type())
syncIntervalv1.setMaxAccess(_B)
if mibBuilder.loadTexts:syncIntervalv1.setStatus(_A)
class _SubDomainNamev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('dflt',0),('alt1',1),('alt2',2),('alt3',3)))
_SubDomainNamev1_Type.__name__=_C
_SubDomainNamev1_Object=MibScalar
subDomainNamev1=_SubDomainNamev1_Object((1,3,6,1,4,1,8691,7,99,1,41,1,4),_SubDomainNamev1_Type())
subDomainNamev1.setMaxAccess(_B)
if mibBuilder.loadTexts:subDomainNamev1.setStatus(_A)
class _PreferMasterv1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_k,1)))
_PreferMasterv1_Type.__name__=_C
_PreferMasterv1_Object=MibScalar
preferMasterv1=_PreferMasterv1_Object((1,3,6,1,4,1,8691,7,99,1,41,1,5),_PreferMasterv1_Type())
preferMasterv1.setMaxAccess(_B)
if mibBuilder.loadTexts:preferMasterv1.setStatus(_A)
_Ptpv2Setting_ObjectIdentity=ObjectIdentity
ptpv2Setting=_Ptpv2Setting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,41,2))
class _EnablePtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnablePtp_Type.__name__=_C
_EnablePtp_Object=MibScalar
enablePtp=_EnablePtp_Object((1,3,6,1,4,1,8691,7,99,1,41,2,1),_EnablePtp_Type())
enablePtp.setMaxAccess(_B)
if mibBuilder.loadTexts:enablePtp.setStatus(_A)
class _ClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('v1BC',0),(_AU,1),(_AV,2),('v2P2PTC',3),('v2E2EBC',4),('v2P2PBC',5)))
_ClockMode_Type.__name__=_C
_ClockMode_Object=MibScalar
clockMode=_ClockMode_Object((1,3,6,1,4,1,8691,7,99,1,41,2,2),_ClockMode_Type())
clockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:clockMode.setStatus(_A)
class _Transport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ieee802dot3',0),('ipv4',1)))
_Transport_Type.__name__=_C
_Transport_Object=MibScalar
transport=_Transport_Object((1,3,6,1,4,1,8691,7,99,1,41,2,3),_Transport_Type())
transport.setMaxAccess(_B)
if mibBuilder.loadTexts:transport.setStatus(_A)
class _SyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-3,-2,-1,0,1)));namedValues=NamedValues(*(('t128msec',-3),('t256msec',-2),('t512msec',-1),(_l,0),(_m,1)))
_SyncInterval_Type.__name__=_C
_SyncInterval_Object=MibScalar
syncInterval=_SyncInterval_Object((1,3,6,1,4,1,8691,7,99,1,41,2,4),_SyncInterval_Type())
syncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:syncInterval.setStatus(_A)
class _LogMinDelayReqInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_l,0),(_m,1),(_A4,2),(_A5,3),(_A6,4),('t32sec',5)))
_LogMinDelayReqInterval_Type.__name__=_C
_LogMinDelayReqInterval_Object=MibScalar
logMinDelayReqInterval=_LogMinDelayReqInterval_Object((1,3,6,1,4,1,8691,7,99,1,41,2,5),_LogMinDelayReqInterval_Type())
logMinDelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:logMinDelayReqInterval.setStatus(_A)
class _LogMinPdelayReqInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5)));namedValues=NamedValues(*(('t512msec',-1),(_l,0),(_m,1),(_A4,2),(_A5,3),(_A6,4),('t32sec',5)))
_LogMinPdelayReqInterval_Type.__name__=_C
_LogMinPdelayReqInterval_Object=MibScalar
logMinPdelayReqInterval=_LogMinPdelayReqInterval_Object((1,3,6,1,4,1,8691,7,99,1,41,2,6),_LogMinPdelayReqInterval_Type())
logMinPdelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:logMinPdelayReqInterval.setStatus(_A)
class _LogAnnounceInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_l,0),(_m,1),(_A4,2),(_A5,3),(_A6,4)))
_LogAnnounceInterval_Type.__name__=_C
_LogAnnounceInterval_Object=MibScalar
logAnnounceInterval=_LogAnnounceInterval_Object((1,3,6,1,4,1,8691,7,99,1,41,2,7),_LogAnnounceInterval_Type())
logAnnounceInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:logAnnounceInterval.setStatus(_A)
class _AnnounceReceiptTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_AnnounceReceiptTimeout_Type.__name__=_C
_AnnounceReceiptTimeout_Object=MibScalar
announceReceiptTimeout=_AnnounceReceiptTimeout_Object((1,3,6,1,4,1,8691,7,99,1,41,2,8),_AnnounceReceiptTimeout_Type())
announceReceiptTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:announceReceiptTimeout.setStatus(_A)
_Priority1_Type=Integer32
_Priority1_Object=MibScalar
priority1=_Priority1_Object((1,3,6,1,4,1,8691,7,99,1,41,2,9),_Priority1_Type())
priority1.setMaxAccess(_B)
if mibBuilder.loadTexts:priority1.setStatus(_A)
_Priority2_Type=Integer32
_Priority2_Object=MibScalar
priority2=_Priority2_Object((1,3,6,1,4,1,8691,7,99,1,41,2,10),_Priority2_Type())
priority2.setMaxAccess(_B)
if mibBuilder.loadTexts:priority2.setStatus(_A)
_ClockClass_Type=Integer32
_ClockClass_Object=MibScalar
clockClass=_ClockClass_Object((1,3,6,1,4,1,8691,7,99,1,41,2,11),_ClockClass_Type())
clockClass.setMaxAccess(_B)
if mibBuilder.loadTexts:clockClass.setStatus(_A)
class _DomainNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('dflt',0),('alt1',1),('alt2',2),('alt3',3)))
_DomainNumber_Type.__name__=_C
_DomainNumber_Object=MibScalar
domainNumber=_DomainNumber_Object((1,3,6,1,4,1,8691,7,99,1,41,2,12),_DomainNumber_Type())
domainNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:domainNumber.setStatus(_A)
_LocalUtcOffset_Type=Integer32
_LocalUtcOffset_Object=MibScalar
localUtcOffset=_LocalUtcOffset_Object((1,3,6,1,4,1,8691,7,99,1,41,2,13),_LocalUtcOffset_Type())
localUtcOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:localUtcOffset.setStatus(_A)
class _LocalUtcOffsetValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_k,1)))
_LocalUtcOffsetValid_Type.__name__=_C
_LocalUtcOffsetValid_Object=MibScalar
localUtcOffsetValid=_LocalUtcOffsetValid_Object((1,3,6,1,4,1,8691,7,99,1,41,2,14),_LocalUtcOffsetValid_Type())
localUtcOffsetValid.setMaxAccess(_B)
if mibBuilder.loadTexts:localUtcOffsetValid.setStatus(_A)
class _LocalLeap59_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_k,1)))
_LocalLeap59_Type.__name__=_C
_LocalLeap59_Object=MibScalar
localLeap59=_LocalLeap59_Object((1,3,6,1,4,1,8691,7,99,1,41,2,15),_LocalLeap59_Type())
localLeap59.setMaxAccess(_B)
if mibBuilder.loadTexts:localLeap59.setStatus(_A)
class _LocalLeap61_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_k,1)))
_LocalLeap61_Type.__name__=_C
_LocalLeap61_Object=MibScalar
localLeap61=_LocalLeap61_Object((1,3,6,1,4,1,8691,7,99,1,41,2,16),_LocalLeap61_Type())
localLeap61.setMaxAccess(_B)
if mibBuilder.loadTexts:localLeap61.setStatus(_A)
class _LocalPtpTimescale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('arb',0),('ptp',1)))
_LocalPtpTimescale_Type.__name__=_C
_LocalPtpTimescale_Object=MibScalar
localPtpTimescale=_LocalPtpTimescale_Object((1,3,6,1,4,1,8691,7,99,1,41,2,17),_LocalPtpTimescale_Type())
localPtpTimescale.setMaxAccess(_B)
if mibBuilder.loadTexts:localPtpTimescale.setStatus(_A)
_LocalArbTime_Type=Integer32
_LocalArbTime_Object=MibScalar
localArbTime=_LocalArbTime_Object((1,3,6,1,4,1,8691,7,99,1,41,2,18),_LocalArbTime_Type())
localArbTime.setMaxAccess(_B)
if mibBuilder.loadTexts:localArbTime.setStatus(_A)
_Ptpv1Status_ObjectIdentity=ObjectIdentity
ptpv1Status=_Ptpv1Status_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,41,3))
_OffsetToMasterv1_Type=Integer32
_OffsetToMasterv1_Object=MibScalar
offsetToMasterv1=_OffsetToMasterv1_Object((1,3,6,1,4,1,8691,7,99,1,41,3,1),_OffsetToMasterv1_Type())
offsetToMasterv1.setMaxAccess(_D)
if mibBuilder.loadTexts:offsetToMasterv1.setStatus(_A)
_MeanPathDelayv1_Type=Integer32
_MeanPathDelayv1_Object=MibScalar
meanPathDelayv1=_MeanPathDelayv1_Object((1,3,6,1,4,1,8691,7,99,1,41,3,2),_MeanPathDelayv1_Type())
meanPathDelayv1.setMaxAccess(_D)
if mibBuilder.loadTexts:meanPathDelayv1.setStatus(_A)
_GrandMasterUuidv1_Type=MacAddress
_GrandMasterUuidv1_Object=MibScalar
grandMasterUuidv1=_GrandMasterUuidv1_Object((1,3,6,1,4,1,8691,7,99,1,41,3,3),_GrandMasterUuidv1_Type())
grandMasterUuidv1.setMaxAccess(_D)
if mibBuilder.loadTexts:grandMasterUuidv1.setStatus(_A)
_ParentUuidv1_Type=MacAddress
_ParentUuidv1_Object=MibScalar
parentUuidv1=_ParentUuidv1_Object((1,3,6,1,4,1,8691,7,99,1,41,3,4),_ParentUuidv1_Type())
parentUuidv1.setMaxAccess(_D)
if mibBuilder.loadTexts:parentUuidv1.setStatus(_A)
_ClockStratumv1_Type=Integer32
_ClockStratumv1_Object=MibScalar
clockStratumv1=_ClockStratumv1_Object((1,3,6,1,4,1,8691,7,99,1,41,3,5),_ClockStratumv1_Type())
clockStratumv1.setMaxAccess(_D)
if mibBuilder.loadTexts:clockStratumv1.setStatus(_A)
_ClockIdentifierv1_Type=DisplayString
_ClockIdentifierv1_Object=MibScalar
clockIdentifierv1=_ClockIdentifierv1_Object((1,3,6,1,4,1,8691,7,99,1,41,3,6),_ClockIdentifierv1_Type())
clockIdentifierv1.setMaxAccess(_D)
if mibBuilder.loadTexts:clockIdentifierv1.setStatus(_A)
_Ptpv2Status_ObjectIdentity=ObjectIdentity
ptpv2Status=_Ptpv2Status_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,41,4))
_OffsetToMaster_Type=Integer32
_OffsetToMaster_Object=MibScalar
offsetToMaster=_OffsetToMaster_Object((1,3,6,1,4,1,8691,7,99,1,41,4,1),_OffsetToMaster_Type())
offsetToMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:offsetToMaster.setStatus(_A)
_MeanPathDelay_Type=Integer32
_MeanPathDelay_Object=MibScalar
meanPathDelay=_MeanPathDelay_Object((1,3,6,1,4,1,8691,7,99,1,41,4,2),_MeanPathDelay_Type())
meanPathDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:meanPathDelay.setStatus(_A)
_ParentIdentity_Type=DisplayString
_ParentIdentity_Object=MibScalar
parentIdentity=_ParentIdentity_Object((1,3,6,1,4,1,8691,7,99,1,41,4,3),_ParentIdentity_Type())
parentIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:parentIdentity.setStatus(_A)
_GrandmasterIdentity_Type=DisplayString
_GrandmasterIdentity_Object=MibScalar
grandmasterIdentity=_GrandmasterIdentity_Object((1,3,6,1,4,1,8691,7,99,1,41,4,4),_GrandmasterIdentity_Type())
grandmasterIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:grandmasterIdentity.setStatus(_A)
_GrandmasterClockClass_Type=Integer32
_GrandmasterClockClass_Object=MibScalar
grandmasterClockClass=_GrandmasterClockClass_Object((1,3,6,1,4,1,8691,7,99,1,41,4,5),_GrandmasterClockClass_Type())
grandmasterClockClass.setMaxAccess(_D)
if mibBuilder.loadTexts:grandmasterClockClass.setStatus(_A)
_GrandmasterClockAccuracy_Type=Integer32
_GrandmasterClockAccuracy_Object=MibScalar
grandmasterClockAccuracy=_GrandmasterClockAccuracy_Object((1,3,6,1,4,1,8691,7,99,1,41,4,6),_GrandmasterClockAccuracy_Type())
grandmasterClockAccuracy.setMaxAccess(_D)
if mibBuilder.loadTexts:grandmasterClockAccuracy.setStatus(_A)
_GrandmasterPriority1_Type=Integer32
_GrandmasterPriority1_Object=MibScalar
grandmasterPriority1=_GrandmasterPriority1_Object((1,3,6,1,4,1,8691,7,99,1,41,4,7),_GrandmasterPriority1_Type())
grandmasterPriority1.setMaxAccess(_D)
if mibBuilder.loadTexts:grandmasterPriority1.setStatus(_A)
_GrandmasterPriority2_Type=Integer32
_GrandmasterPriority2_Object=MibScalar
grandmasterPriority2=_GrandmasterPriority2_Object((1,3,6,1,4,1,8691,7,99,1,41,4,8),_GrandmasterPriority2_Type())
grandmasterPriority2.setMaxAccess(_D)
if mibBuilder.loadTexts:grandmasterPriority2.setStatus(_A)
_StepsRemoved_Type=Integer32
_StepsRemoved_Object=MibScalar
stepsRemoved=_StepsRemoved_Object((1,3,6,1,4,1,8691,7,99,1,41,4,9),_StepsRemoved_Type())
stepsRemoved.setMaxAccess(_D)
if mibBuilder.loadTexts:stepsRemoved.setStatus(_A)
_CurrentUtcOffset_Type=Integer32
_CurrentUtcOffset_Object=MibScalar
currentUtcOffset=_CurrentUtcOffset_Object((1,3,6,1,4,1,8691,7,99,1,41,4,10),_CurrentUtcOffset_Type())
currentUtcOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:currentUtcOffset.setStatus(_A)
_CurrentUtcOffsetValid_Type=DisplayString
_CurrentUtcOffsetValid_Object=MibScalar
currentUtcOffsetValid=_CurrentUtcOffsetValid_Object((1,3,6,1,4,1,8691,7,99,1,41,4,11),_CurrentUtcOffsetValid_Type())
currentUtcOffsetValid.setMaxAccess(_D)
if mibBuilder.loadTexts:currentUtcOffsetValid.setStatus(_A)
_Leap59_Type=DisplayString
_Leap59_Object=MibScalar
leap59=_Leap59_Object((1,3,6,1,4,1,8691,7,99,1,41,4,12),_Leap59_Type())
leap59.setMaxAccess(_D)
if mibBuilder.loadTexts:leap59.setStatus(_A)
_Leap61_Type=DisplayString
_Leap61_Object=MibScalar
leap61=_Leap61_Object((1,3,6,1,4,1,8691,7,99,1,41,4,13),_Leap61_Type())
leap61.setMaxAccess(_D)
if mibBuilder.loadTexts:leap61.setStatus(_A)
_PtpTimescale_Type=DisplayString
_PtpTimescale_Object=MibScalar
ptpTimescale=_PtpTimescale_Object((1,3,6,1,4,1,8691,7,99,1,41,4,14),_PtpTimescale_Type())
ptpTimescale.setMaxAccess(_D)
if mibBuilder.loadTexts:ptpTimescale.setStatus(_A)
_Timesource_Type=DisplayString
_Timesource_Object=MibScalar
timesource=_Timesource_Object((1,3,6,1,4,1,8691,7,99,1,41,4,15),_Timesource_Type())
timesource.setMaxAccess(_D)
if mibBuilder.loadTexts:timesource.setStatus(_A)
_PtpPortTable_Object=MibTable
ptpPortTable=_PtpPortTable_Object((1,3,6,1,4,1,8691,7,99,1,41,5))
if mibBuilder.loadTexts:ptpPortTable.setStatus(_A)
_PtpPortEntry_Object=MibTableRow
ptpPortEntry=_PtpPortEntry_Object((1,3,6,1,4,1,8691,7,99,1,41,5,1))
ptpPortEntry.setIndexNames((0,_E,_AW))
if mibBuilder.loadTexts:ptpPortEntry.setStatus(_A)
_PtpPortIndex_Type=Integer32
_PtpPortIndex_Object=MibTableColumn
ptpPortIndex=_PtpPortIndex_Object((1,3,6,1,4,1,8691,7,99,1,41,5,1,1),_PtpPortIndex_Type())
ptpPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ptpPortIndex.setStatus(_A)
class _PtpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_PtpPortEnable_Type.__name__=_C
_PtpPortEnable_Object=MibTableColumn
ptpPortEnable=_PtpPortEnable_Object((1,3,6,1,4,1,8691,7,99,1,41,5,1,2),_PtpPortEnable_Type())
ptpPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortEnable.setStatus(_A)
class _PtpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ptpInitializing',0),('ptpFaulty',1),('ptpDisabled',2),('ptpListening',3),('ptpPreMaster',4),('ptpMaster',5),('ptpPassive',6),('ptpUncalibrated',7),('ptpSlave',8)))
_PtpPortStatus_Type.__name__=_C
_PtpPortStatus_Object=MibTableColumn
ptpPortStatus=_PtpPortStatus_Object((1,3,6,1,4,1,8691,7,99,1,41,5,1,3),_PtpPortStatus_Type())
ptpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ptpPortStatus.setStatus(_A)
_Diagnosis_ObjectIdentity=ObjectIdentity
diagnosis=_Diagnosis_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,42))
_LldpSetting_ObjectIdentity=ObjectIdentity
lldpSetting=_LldpSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,42,1))
class _EnableLLDP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableLLDP_Type.__name__=_C
_EnableLLDP_Object=MibScalar
enableLLDP=_EnableLLDP_Object((1,3,6,1,4,1,8691,7,99,1,42,1,1),_EnableLLDP_Type())
enableLLDP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableLLDP.setStatus(_A)
_LldpMSGInterval_Type=Integer32
_LldpMSGInterval_Object=MibScalar
lldpMSGInterval=_LldpMSGInterval_Object((1,3,6,1,4,1,8691,7,99,1,42,1,2),_LldpMSGInterval_Type())
lldpMSGInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpMSGInterval.setStatus(_A)
_WebTimeout_Type=Integer32
_WebTimeout_Object=MibScalar
webTimeout=_WebTimeout_Object((1,3,6,1,4,1,8691,7,99,1,43),_WebTimeout_Type())
webTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:webTimeout.setStatus(_A)
_AgeTime_Type=Integer32
_AgeTime_Object=MibScalar
ageTime=_AgeTime_Object((1,3,6,1,4,1,8691,7,99,1,44),_AgeTime_Type())
ageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ageTime.setStatus(_A)
_GarpSetting_ObjectIdentity=ObjectIdentity
garpSetting=_GarpSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,45))
_JoinTime_Type=Integer32
_JoinTime_Object=MibScalar
joinTime=_JoinTime_Object((1,3,6,1,4,1,8691,7,99,1,45,1),_JoinTime_Type())
joinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:joinTime.setStatus(_A)
_LeaveTime_Type=Integer32
_LeaveTime_Object=MibScalar
leaveTime=_LeaveTime_Object((1,3,6,1,4,1,8691,7,99,1,45,2),_LeaveTime_Type())
leaveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:leaveTime.setStatus(_A)
_LeaveAllTime_Type=Integer32
_LeaveAllTime_Object=MibScalar
leaveAllTime=_LeaveAllTime_Object((1,3,6,1,4,1,8691,7,99,1,45,3),_LeaveAllTime_Type())
leaveAllTime.setMaxAccess(_B)
if mibBuilder.loadTexts:leaveAllTime.setStatus(_A)
_Eventlog_ObjectIdentity=ObjectIdentity
eventlog=_Eventlog_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,46))
_EventlogTable_Object=MibTable
eventlogTable=_EventlogTable_Object((1,3,6,1,4,1,8691,7,99,1,46,1))
if mibBuilder.loadTexts:eventlogTable.setStatus(_A)
_EventlogEntry_Object=MibTableRow
eventlogEntry=_EventlogEntry_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1))
eventlogEntry.setIndexNames((0,_E,_AX))
if mibBuilder.loadTexts:eventlogEntry.setStatus(_A)
_EventlogIndex_Type=Integer32
_EventlogIndex_Object=MibTableColumn
eventlogIndex=_EventlogIndex_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1,1),_EventlogIndex_Type())
eventlogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogIndex.setStatus(_A)
_EventlogBootup_Type=Integer32
_EventlogBootup_Object=MibTableColumn
eventlogBootup=_EventlogBootup_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1,2),_EventlogBootup_Type())
eventlogBootup.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogBootup.setStatus(_A)
_EventlogDate_Type=DisplayString
_EventlogDate_Object=MibTableColumn
eventlogDate=_EventlogDate_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1,3),_EventlogDate_Type())
eventlogDate.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogDate.setStatus(_A)
_EventlogTime_Type=DisplayString
_EventlogTime_Object=MibTableColumn
eventlogTime=_EventlogTime_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1,4),_EventlogTime_Type())
eventlogTime.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogTime.setStatus(_A)
_EventlogUptime_Type=DisplayString
_EventlogUptime_Object=MibTableColumn
eventlogUptime=_EventlogUptime_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1,5),_EventlogUptime_Type())
eventlogUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogUptime.setStatus(_A)
_EventlogEvent_Type=DisplayString
_EventlogEvent_Object=MibTableColumn
eventlogEvent=_EventlogEvent_Object((1,3,6,1,4,1,8691,7,99,1,46,1,1,6),_EventlogEvent_Type())
eventlogEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogEvent.setStatus(_A)
class _EventlogClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noop',0),('clear',1)))
_EventlogClear_Type.__name__=_C
_EventlogClear_Object=MibScalar
eventlogClear=_EventlogClear_Object((1,3,6,1,4,1,8691,7,99,1,46,2),_EventlogClear_Type())
eventlogClear.setMaxAccess(_B)
if mibBuilder.loadTexts:eventlogClear.setStatus(_A)
_IndustrialProtocol_ObjectIdentity=ObjectIdentity
industrialProtocol=_IndustrialProtocol_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,47))
_EipSetting_ObjectIdentity=ObjectIdentity
eipSetting=_EipSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,47,1))
class _EnableEtherNetIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableEtherNetIP_Type.__name__=_C
_EnableEtherNetIP_Object=MibScalar
enableEtherNetIP=_EnableEtherNetIP_Object((1,3,6,1,4,1,8691,7,99,1,47,1,1),_EnableEtherNetIP_Type())
enableEtherNetIP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableEtherNetIP.setStatus(_A)
_ModbusTCPSetting_ObjectIdentity=ObjectIdentity
modbusTCPSetting=_ModbusTCPSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,47,2))
class _EnableModbusTCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableModbusTCP_Type.__name__=_C
_EnableModbusTCP_Object=MibScalar
enableModbusTCP=_EnableModbusTCP_Object((1,3,6,1,4,1,8691,7,99,1,47,2,1),_EnableModbusTCP_Type())
enableModbusTCP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableModbusTCP.setStatus(_A)
_ProfinetioSetting_ObjectIdentity=ObjectIdentity
profinetioSetting=_ProfinetioSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,47,3))
class _EnableProfinetIO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableProfinetIO_Type.__name__=_C
_EnableProfinetIO_Object=MibScalar
enableProfinetIO=_EnableProfinetIO_Object((1,3,6,1,4,1,8691,7,99,1,47,3,1),_EnableProfinetIO_Type())
enableProfinetIO.setMaxAccess(_B)
if mibBuilder.loadTexts:enableProfinetIO.setStatus(_A)
class _EnableFactoryDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('activate',1))
_EnableFactoryDefault_Type.__name__=_C
_EnableFactoryDefault_Object=MibScalar
enableFactoryDefault=_EnableFactoryDefault_Object((1,3,6,1,4,1,8691,7,99,1,48),_EnableFactoryDefault_Type())
enableFactoryDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:enableFactoryDefault.setStatus(_A)
class _EnableJumboFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EnableJumboFrame_Type.__name__=_C
_EnableJumboFrame_Object=MibScalar
enableJumboFrame=_EnableJumboFrame_Object((1,3,6,1,4,1,8691,7,99,1,49),_EnableJumboFrame_Type())
enableJumboFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:enableJumboFrame.setStatus(_A)
_MaxJumboFrame_Type=Integer32
_MaxJumboFrame_Object=MibScalar
maxJumboFrame=_MaxJumboFrame_Object((1,3,6,1,4,1,8691,7,99,1,50),_MaxJumboFrame_Type())
maxJumboFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:maxJumboFrame.setStatus(_A)
class _ConsoleLoginMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('menu',0),('cli',1)))
_ConsoleLoginMode_Type.__name__=_C
_ConsoleLoginMode_Object=MibScalar
consoleLoginMode=_ConsoleLoginMode_Object((1,3,6,1,4,1,8691,7,99,1,51),_ConsoleLoginMode_Type())
consoleLoginMode.setMaxAccess(_B)
if mibBuilder.loadTexts:consoleLoginMode.setStatus(_A)
_AccessControlList_ObjectIdentity=ObjectIdentity
accessControlList=_AccessControlList_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,52))
_AccessControlTable_Object=MibTable
accessControlTable=_AccessControlTable_Object((1,3,6,1,4,1,8691,7,99,1,52,1))
if mibBuilder.loadTexts:accessControlTable.setStatus(_A)
_AccessControlEntry_Object=MibTableRow
accessControlEntry=_AccessControlEntry_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1))
accessControlEntry.setIndexNames((0,_E,_AY))
if mibBuilder.loadTexts:accessControlEntry.setStatus(_A)
_AclRuleIndex_Type=Integer32
_AclRuleIndex_Object=MibTableColumn
aclRuleIndex=_AclRuleIndex_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,1),_AclRuleIndex_Type())
aclRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:aclRuleIndex.setStatus(_A)
_ListID_Type=Integer32
_ListID_Object=MibTableColumn
listID=_ListID_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,2),_ListID_Type())
listID.setMaxAccess(_F)
if mibBuilder.loadTexts:listID.setStatus(_A)
class _FilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ipBase',0),('macBase',1)))
_FilterType_Type.__name__=_C
_FilterType_Object=MibTableColumn
filterType=_FilterType_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,3),_FilterType_Type())
filterType.setMaxAccess(_F)
if mibBuilder.loadTexts:filterType.setStatus(_A)
class _ActionFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('permit',0),('deny',1)))
_ActionFlag_Type.__name__=_C
_ActionFlag_Object=MibTableColumn
actionFlag=_ActionFlag_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,4),_ActionFlag_Type())
actionFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:actionFlag.setStatus(_A)
_SrcMacAddr_Type=MacAddress
_SrcMacAddr_Object=MibTableColumn
srcMacAddr=_SrcMacAddr_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,5),_SrcMacAddr_Type())
srcMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:srcMacAddr.setStatus(_A)
_SrcMacMask_Type=MacAddress
_SrcMacMask_Object=MibTableColumn
srcMacMask=_SrcMacMask_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,6),_SrcMacMask_Type())
srcMacMask.setMaxAccess(_F)
if mibBuilder.loadTexts:srcMacMask.setStatus(_A)
_DstMacAddr_Type=MacAddress
_DstMacAddr_Object=MibTableColumn
dstMacAddr=_DstMacAddr_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,7),_DstMacAddr_Type())
dstMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:dstMacAddr.setStatus(_A)
_DstMacMask_Type=MacAddress
_DstMacMask_Object=MibTableColumn
dstMacMask=_DstMacMask_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,8),_DstMacMask_Type())
dstMacMask.setMaxAccess(_F)
if mibBuilder.loadTexts:dstMacMask.setStatus(_A)
_EtherType_Type=Integer32
_EtherType_Object=MibTableColumn
etherType=_EtherType_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,9),_EtherType_Type())
etherType.setMaxAccess(_F)
if mibBuilder.loadTexts:etherType.setStatus(_A)
class _VlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanID_Type.__name__=_C
_VlanID_Object=MibTableColumn
vlanID=_VlanID_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,10),_VlanID_Type())
vlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanID.setStatus(_A)
_SrcIpAddr_Type=IpAddress
_SrcIpAddr_Object=MibTableColumn
srcIpAddr=_SrcIpAddr_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,11),_SrcIpAddr_Type())
srcIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:srcIpAddr.setStatus(_A)
_SrcNetmask_Type=IpAddress
_SrcNetmask_Object=MibTableColumn
srcNetmask=_SrcNetmask_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,12),_SrcNetmask_Type())
srcNetmask.setMaxAccess(_F)
if mibBuilder.loadTexts:srcNetmask.setStatus(_A)
_DstIpAddr_Type=IpAddress
_DstIpAddr_Object=MibTableColumn
dstIpAddr=_DstIpAddr_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,13),_DstIpAddr_Type())
dstIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:dstIpAddr.setStatus(_A)
_DstNetmask_Type=IpAddress
_DstNetmask_Object=MibTableColumn
dstNetmask=_DstNetmask_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,14),_DstNetmask_Type())
dstNetmask.setMaxAccess(_F)
if mibBuilder.loadTexts:dstNetmask.setStatus(_A)
_ProtocolCode_Type=Integer32
_ProtocolCode_Object=MibTableColumn
protocolCode=_ProtocolCode_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,15),_ProtocolCode_Type())
protocolCode.setMaxAccess(_F)
if mibBuilder.loadTexts:protocolCode.setStatus(_A)
_SrcsocketPort_Type=Integer32
_SrcsocketPort_Object=MibTableColumn
srcsocketPort=_SrcsocketPort_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,16),_SrcsocketPort_Type())
srcsocketPort.setMaxAccess(_F)
if mibBuilder.loadTexts:srcsocketPort.setStatus(_A)
_DstsocketPort_Type=Integer32
_DstsocketPort_Object=MibTableColumn
dstsocketPort=_DstsocketPort_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,17),_DstsocketPort_Type())
dstsocketPort.setMaxAccess(_F)
if mibBuilder.loadTexts:dstsocketPort.setStatus(_A)
class _AclStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_AclStatus_Type.__name__=_C
_AclStatus_Object=MibTableColumn
aclStatus=_AclStatus_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,18),_AclStatus_Type())
aclStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:aclStatus.setStatus(_A)
class _IpDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues(('any',-1))
_IpDSCP_Type.__name__=_C
_IpDSCP_Object=MibTableColumn
ipDSCP=_IpDSCP_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,19),_IpDSCP_Type())
ipDSCP.setMaxAccess(_F)
if mibBuilder.loadTexts:ipDSCP.setStatus(_A)
class _OverrideDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues((_L,-1))
_OverrideDSCP_Type.__name__=_C
_OverrideDSCP_Object=MibTableColumn
overrideDSCP=_OverrideDSCP_Object((1,3,6,1,4,1,8691,7,99,1,52,1,1,20),_OverrideDSCP_Type())
overrideDSCP.setMaxAccess(_F)
if mibBuilder.loadTexts:overrideDSCP.setStatus(_A)
_AclAttachmentTable_Object=MibTable
aclAttachmentTable=_AclAttachmentTable_Object((1,3,6,1,4,1,8691,7,99,1,52,2))
if mibBuilder.loadTexts:aclAttachmentTable.setStatus(_A)
_AclAttachmentEntry_Object=MibTableRow
aclAttachmentEntry=_AclAttachmentEntry_Object((1,3,6,1,4,1,8691,7,99,1,52,2,1))
aclAttachmentEntry.setIndexNames((0,_E,'aclID'))
if mibBuilder.loadTexts:aclAttachmentEntry.setStatus(_A)
_AclID_Type=Integer32
_AclID_Object=MibTableColumn
aclID=_AclID_Object((1,3,6,1,4,1,8691,7,99,1,52,2,1,1),_AclID_Type())
aclID.setMaxAccess(_F)
if mibBuilder.loadTexts:aclID.setStatus(_A)
_IngressPort_Type=PortList
_IngressPort_Object=MibTableColumn
ingressPort=_IngressPort_Object((1,3,6,1,4,1,8691,7,99,1,52,2,1,2),_IngressPort_Type())
ingressPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ingressPort.setStatus(_A)
_EgressPort_Type=PortList
_EgressPort_Object=MibTableColumn
egressPort=_EgressPort_Object((1,3,6,1,4,1,8691,7,99,1,52,2,1,3),_EgressPort_Type())
egressPort.setMaxAccess(_F)
if mibBuilder.loadTexts:egressPort.setStatus(_A)
_AclListName_Type=DisplayString
_AclListName_Object=MibTableColumn
aclListName=_AclListName_Object((1,3,6,1,4,1,8691,7,99,1,52,2,1,4),_AclListName_Type())
aclListName.setMaxAccess(_F)
if mibBuilder.loadTexts:aclListName.setStatus(_A)
_CpuLoading5s_Type=Integer32
_CpuLoading5s_Object=MibScalar
cpuLoading5s=_CpuLoading5s_Object((1,3,6,1,4,1,8691,7,99,1,53),_CpuLoading5s_Type())
cpuLoading5s.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLoading5s.setStatus(_A)
_CpuLoading30s_Type=Integer32
_CpuLoading30s_Object=MibScalar
cpuLoading30s=_CpuLoading30s_Object((1,3,6,1,4,1,8691,7,99,1,54),_CpuLoading30s_Type())
cpuLoading30s.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLoading30s.setStatus(_A)
_CpuLoading300s_Type=Integer32
_CpuLoading300s_Object=MibScalar
cpuLoading300s=_CpuLoading300s_Object((1,3,6,1,4,1,8691,7,99,1,55),_CpuLoading300s_Type())
cpuLoading300s.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLoading300s.setStatus(_A)
_TotalMemory_Type=Integer32
_TotalMemory_Object=MibScalar
totalMemory=_TotalMemory_Object((1,3,6,1,4,1,8691,7,99,1,56),_TotalMemory_Type())
totalMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:totalMemory.setStatus(_A)
_FreeMemory_Type=Integer32
_FreeMemory_Object=MibScalar
freeMemory=_FreeMemory_Object((1,3,6,1,4,1,8691,7,99,1,57),_FreeMemory_Type())
freeMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:freeMemory.setStatus(_A)
_UsedMemory_Type=Integer32
_UsedMemory_Object=MibScalar
usedMemory=_UsedMemory_Object((1,3,6,1,4,1,8691,7,99,1,58),_UsedMemory_Type())
usedMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:usedMemory.setStatus(_A)
_MemoryUsage_Type=Integer32
_MemoryUsage_Object=MibScalar
memoryUsage=_MemoryUsage_Object((1,3,6,1,4,1,8691,7,99,1,59),_MemoryUsage_Type())
memoryUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryUsage.setStatus(_A)
class _LoopProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_LoopProtection_Type.__name__=_C
_LoopProtection_Object=MibScalar
loopProtection=_LoopProtection_Object((1,3,6,1,4,1,8691,7,99,1,61),_LoopProtection_Type())
loopProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:loopProtection.setStatus(_A)
_EventSettings_ObjectIdentity=ObjectIdentity
eventSettings=_EventSettings_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,62))
_SystemEventSettingsTable_Object=MibTable
systemEventSettingsTable=_SystemEventSettingsTable_Object((1,3,6,1,4,1,8691,7,99,1,62,1))
if mibBuilder.loadTexts:systemEventSettingsTable.setStatus(_A)
_SystemEventSettingsEntry_Object=MibTableRow
systemEventSettingsEntry=_SystemEventSettingsEntry_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1))
systemEventSettingsEntry.setIndexNames((0,_E,_AZ))
if mibBuilder.loadTexts:systemEventSettingsEntry.setStatus(_A)
_SystemEventIndex_Type=Integer32
_SystemEventIndex_Object=MibTableColumn
systemEventIndex=_SystemEventIndex_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1,1),_SystemEventIndex_Type())
systemEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:systemEventIndex.setStatus(_A)
class _SystemEventActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_u,0),(_K,1)))
_SystemEventActive_Type.__name__=_C
_SystemEventActive_Object=MibTableColumn
systemEventActive=_SystemEventActive_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1,2),_SystemEventActive_Type())
systemEventActive.setMaxAccess(_B)
if mibBuilder.loadTexts:systemEventActive.setStatus(_A)
_SystemEventName_Type=DisplayString
_SystemEventName_Object=MibTableColumn
systemEventName=_SystemEventName_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1,3),_SystemEventName_Type())
systemEventName.setMaxAccess(_D)
if mibBuilder.loadTexts:systemEventName.setStatus(_A)
class _SystemEventSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,30,31)));namedValues=NamedValues(*((_L,0),('support-SNMPTrap-only',1),('support-Email-only',2),('support-SNMP-Trap-Email',3),('support-Syslog-only',4),('support-SNMPTrap-Syslog',5),('support-Email-Syslog',6),('support-SNMPTrap-Email-Syslog',7),('support-Relay1-only',8),('support-SNMPTrap-Relay1',9),('support-Email-Relay1',10),('support-SNMPTrap-Email-Relay1',11),('support-Syslog-Relay1',12),('support-SNMPTrap-Syslog-Relay1',13),('support-Email-Syslog-Relay1',14),('support-SNMPTrap-Email-Syslog-Relay1',15),('support-Relay2-only',16),('support-SNMPTrap-Relay2',17),('support-Email-Relay2',18),('support-SNMPTrap-Email-Relay2',19),('support-Syslog-Relay2',20),('support-SNMPTrap-Syslog-Relay2',21),('support-Email-Syslog-Relay2',22),('support-SNMPTrap-Email-Syslog-Relay2',23),('support-Relay1-Relay2',24),('support-SNMPTrap-Relay1-Relay2',25),('support-Syslog-Relay1-Relay2',28),('support-Email-Syslog-Relay1-Relay2',30),('support-all-SNMPTrap-Email-Syslog-Relay1-Relay2',31)))
_SystemEventSupport_Type.__name__=_C
_SystemEventSupport_Object=MibTableColumn
systemEventSupport=_SystemEventSupport_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1,4),_SystemEventSupport_Type())
systemEventSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:systemEventSupport.setStatus(_A)
class _SystemEventModuleEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,30,31)));namedValues=NamedValues(*((_L,0),(_Aa,1),(_Ab,2),(_Ac,3),(_Ad,4),(_Ae,5),(_Af,6),(_Ag,7),(_Ah,8),(_Ai,9),(_Aj,10),(_Ak,11),(_Al,12),(_Am,13),(_An,14),(_Ao,15),(_Ap,16),(_Aq,17),(_Ar,18),(_As,19),(_At,20),(_Au,21),(_Av,22),(_Aw,23),(_Ax,24),(_Ay,25),(_Az,28),(_A_,30),(_B0,31)))
_SystemEventModuleEnable_Type.__name__=_C
_SystemEventModuleEnable_Object=MibTableColumn
systemEventModuleEnable=_SystemEventModuleEnable_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1,5),_SystemEventModuleEnable_Type())
systemEventModuleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:systemEventModuleEnable.setStatus(_A)
class _SystemEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_B1,0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),(_B2,6),('debug',7)))
_SystemEventSeverity_Type.__name__=_C
_SystemEventSeverity_Object=MibTableColumn
systemEventSeverity=_SystemEventSeverity_Object((1,3,6,1,4,1,8691,7,99,1,62,1,1,6),_SystemEventSeverity_Type())
systemEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:systemEventSeverity.setStatus(_A)
_PortEventSettingsTable_Object=MibTable
portEventSettingsTable=_PortEventSettingsTable_Object((1,3,6,1,4,1,8691,7,99,1,62,2))
if mibBuilder.loadTexts:portEventSettingsTable.setStatus(_A)
_PortEventSettingsEntry_Object=MibTableRow
portEventSettingsEntry=_PortEventSettingsEntry_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1))
portEventSettingsEntry.setIndexNames((0,_E,_B3))
if mibBuilder.loadTexts:portEventSettingsEntry.setStatus(_A)
_PortEventIndex_Type=Integer32
_PortEventIndex_Object=MibTableColumn
portEventIndex=_PortEventIndex_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,1),_PortEventIndex_Type())
portEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portEventIndex.setStatus(_A)
_PortEventLabel_Type=DisplayString
_PortEventLabel_Object=MibTableColumn
portEventLabel=_PortEventLabel_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,2),_PortEventLabel_Type())
portEventLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:portEventLabel.setStatus(_A)
class _PortEventActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_u,0),(_K,1)))
_PortEventActive_Type.__name__=_C
_PortEventActive_Object=MibTableColumn
portEventActive=_PortEventActive_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,3),_PortEventActive_Type())
portEventActive.setMaxAccess(_B)
if mibBuilder.loadTexts:portEventActive.setStatus(_A)
class _PortEventEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,0),('enable-LinkOn-only',1),('enable-LinkOff-only',2),('enable-LinkOn-LinkOff',3),('enable-TrafficOverload-only',4),('enable-LinkOn-TrafficOverload',5),('enable-LinkOff-TrafficOverload',6),('enable-All-LinkOn-LinkOff-TrafficOverload',7)))
_PortEventEnable_Type.__name__=_C
_PortEventEnable_Object=MibTableColumn
portEventEnable=_PortEventEnable_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,4),_PortEventEnable_Type())
portEventEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portEventEnable.setStatus(_A)
class _PortEventTrafficThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PortEventTrafficThreshold_Type.__name__=_C
_PortEventTrafficThreshold_Object=MibTableColumn
portEventTrafficThreshold=_PortEventTrafficThreshold_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,5),_PortEventTrafficThreshold_Type())
portEventTrafficThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:portEventTrafficThreshold.setStatus(_A)
class _PortEventTrafficDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PortEventTrafficDuration_Type.__name__=_C
_PortEventTrafficDuration_Object=MibTableColumn
portEventTrafficDuration=_PortEventTrafficDuration_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,6),_PortEventTrafficDuration_Type())
portEventTrafficDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:portEventTrafficDuration.setStatus(_A)
class _PortEventModuleEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,30,31)));namedValues=NamedValues(*((_L,0),(_Aa,1),(_Ab,2),(_Ac,3),(_Ad,4),(_Ae,5),(_Af,6),(_Ag,7),(_Ah,8),(_Ai,9),(_Aj,10),(_Ak,11),(_Al,12),(_Am,13),(_An,14),(_Ao,15),(_Ap,16),(_Aq,17),(_Ar,18),(_As,19),(_At,20),(_Au,21),(_Av,22),(_Aw,23),(_Ax,24),(_Ay,25),(_Az,28),(_A_,30),(_B0,31)))
_PortEventModuleEnable_Type.__name__=_C
_PortEventModuleEnable_Object=MibTableColumn
portEventModuleEnable=_PortEventModuleEnable_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,7),_PortEventModuleEnable_Type())
portEventModuleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portEventModuleEnable.setStatus(_A)
class _PortEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_B1,0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),(_B2,6),('debug',7)))
_PortEventSeverity_Type.__name__=_C
_PortEventSeverity_Object=MibTableColumn
portEventSeverity=_PortEventSeverity_Object((1,3,6,1,4,1,8691,7,99,1,62,2,1,8),_PortEventSeverity_Type())
portEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:portEventSeverity.setStatus(_A)
_SwitchLocator_ObjectIdentity=ObjectIdentity
switchLocator=_SwitchLocator_ObjectIdentity((1,3,6,1,4,1,8691,7,99,1,64))
class _BlinkingLocatorLED_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_BlinkingLocatorLED_Type.__name__=_C
_BlinkingLocatorLED_Object=MibScalar
blinkingLocatorLED=_BlinkingLocatorLED_Object((1,3,6,1,4,1,8691,7,99,1,64,1),_BlinkingLocatorLED_Type())
blinkingLocatorLED.setMaxAccess(_B)
if mibBuilder.loadTexts:blinkingLocatorLED.setStatus(_A)
_DisableLocatorLEDTime_Type=Integer32
_DisableLocatorLEDTime_Object=MibScalar
disableLocatorLEDTime=_DisableLocatorLEDTime_Object((1,3,6,1,4,1,8691,7,99,1,64,2),_DisableLocatorLEDTime_Type())
disableLocatorLEDTime.setMaxAccess(_B)
if mibBuilder.loadTexts:disableLocatorLEDTime.setStatus(_A)
_SwTraps_ObjectIdentity=ObjectIdentity
swTraps=_SwTraps_ObjectIdentity((1,3,6,1,4,1,8691,7,99,2))
class _VarconfigChangeTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('configChanged',2)))
_VarconfigChangeTrap_Type.__name__=_C
_VarconfigChangeTrap_Object=MibScalar
varconfigChangeTrap=_VarconfigChangeTrap_Object((1,3,6,1,4,1,8691,7,99,2,1),_VarconfigChangeTrap_Type())
varconfigChangeTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varconfigChangeTrap.setStatus(_A)
class _Varpower1Trap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_w,2),(_x,3)))
_Varpower1Trap_Type.__name__=_C
_Varpower1Trap_Object=MibScalar
varpower1Trap=_Varpower1Trap_Object((1,3,6,1,4,1,8691,7,99,2,2),_Varpower1Trap_Type())
varpower1Trap.setMaxAccess(_D)
if mibBuilder.loadTexts:varpower1Trap.setStatus(_A)
class _Varpower2Trap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_w,2),(_x,3)))
_Varpower2Trap_Type.__name__=_C
_Varpower2Trap_Object=MibScalar
varpower2Trap=_Varpower2Trap_Object((1,3,6,1,4,1,8691,7,99,2,3),_Varpower2Trap_Type())
varpower2Trap.setMaxAccess(_D)
if mibBuilder.loadTexts:varpower2Trap.setStatus(_A)
_VartrafficOverloadTrap_Type=Integer32
_VartrafficOverloadTrap_Object=MibScalar
vartrafficOverloadTrap=_VartrafficOverloadTrap_Object((1,3,6,1,4,1,8691,7,99,2,4),_VartrafficOverloadTrap_Type())
vartrafficOverloadTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:vartrafficOverloadTrap.setStatus(_A)
class _VarredundancyTopologyChangedTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('topologyChanged',2)))
_VarredundancyTopologyChangedTrap_Type.__name__=_C
_VarredundancyTopologyChangedTrap_Object=MibScalar
varredundancyTopologyChangedTrap=_VarredundancyTopologyChangedTrap_Object((1,3,6,1,4,1,8691,7,99,2,5),_VarredundancyTopologyChangedTrap_Type())
varredundancyTopologyChangedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varredundancyTopologyChangedTrap.setStatus(_A)
class _VarturboRingCouplingPortChangedTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('couplingPortChanged',2)))
_VarturboRingCouplingPortChangedTrap_Type.__name__=_C
_VarturboRingCouplingPortChangedTrap_Object=MibScalar
varturboRingCouplingPortChangedTrap=_VarturboRingCouplingPortChangedTrap_Object((1,3,6,1,4,1,8691,7,99,2,6),_VarturboRingCouplingPortChangedTrap_Type())
varturboRingCouplingPortChangedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varturboRingCouplingPortChangedTrap.setStatus(_A)
class _VarturboRingMasterChangedTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('ringMasterChanged',2)))
_VarturboRingMasterChangedTrap_Type.__name__=_C
_VarturboRingMasterChangedTrap_Object=MibScalar
varturboRingMasterChangedTrap=_VarturboRingMasterChangedTrap_Object((1,3,6,1,4,1,8691,7,99,2,7),_VarturboRingMasterChangedTrap_Type())
varturboRingMasterChangedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varturboRingMasterChangedTrap.setStatus(_A)
_VarPortLoopDetectedTrap_Type=Integer32
_VarPortLoopDetectedTrap_Object=MibScalar
varPortLoopDetectedTrap=_VarPortLoopDetectedTrap_Object((1,3,6,1,4,1,8691,7,99,2,17),_VarPortLoopDetectedTrap_Type())
varPortLoopDetectedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varPortLoopDetectedTrap.setStatus(_A)
class _VarRateLimitedOnTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('rateLimitON',2),('rateLimitOFF',3)))
_VarRateLimitedOnTrap_Type.__name__=_C
_VarRateLimitedOnTrap_Object=MibScalar
varRateLimitedOnTrap=_VarRateLimitedOnTrap_Object((1,3,6,1,4,1,8691,7,99,2,18),_VarRateLimitedOnTrap_Type())
varRateLimitedOnTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varRateLimitedOnTrap.setStatus(_A)
_VarLLDPChgTrap_Type=Integer32
_VarLLDPChgTrap_Object=MibScalar
varLLDPChgTrap=_VarLLDPChgTrap_Object((1,3,6,1,4,1,8691,7,99,2,19),_VarLLDPChgTrap_Type())
varLLDPChgTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varLLDPChgTrap.setStatus(_A)
class _VarABC02WarningTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noEnoughSpace',1),('nnauthorizedMediaIsDetected',2),('exportConfigurationFail',3),('exportLogFail',4),('autoImportConfigurationFail',5)))
_VarABC02WarningTrap_Type.__name__=_C
_VarABC02WarningTrap_Object=MibScalar
varABC02WarningTrap=_VarABC02WarningTrap_Object((1,3,6,1,4,1,8691,7,99,2,20),_VarABC02WarningTrap_Type())
varABC02WarningTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varABC02WarningTrap.setStatus(_A)
class _VarturboRingMasterMismatchTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('ringMasterMismatch',2)))
_VarturboRingMasterMismatchTrap_Type.__name__=_C
_VarturboRingMasterMismatchTrap_Object=MibScalar
varturboRingMasterMismatchTrap=_VarturboRingMasterMismatchTrap_Object((1,3,6,1,4,1,8691,7,99,2,22),_VarturboRingMasterMismatchTrap_Type())
varturboRingMasterMismatchTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varturboRingMasterMismatchTrap.setStatus(_A)
_L3Mgmt_ObjectIdentity=ObjectIdentity
l3Mgmt=_L3Mgmt_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3))
_IpIfSetting_ObjectIdentity=ObjectIdentity
ipIfSetting=_IpIfSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,1))
_IpIfSettingTable_Object=MibTable
ipIfSettingTable=_IpIfSettingTable_Object((1,3,6,1,4,1,8691,7,99,3,1,1))
if mibBuilder.loadTexts:ipIfSettingTable.setStatus(_A)
_IpIfSettingEntry_Object=MibTableRow
ipIfSettingEntry=_IpIfSettingEntry_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1))
ipIfSettingEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:ipIfSettingEntry.setStatus(_A)
_IpIfIndex_Type=Integer32
_IpIfIndex_Object=MibTableColumn
ipIfIndex=_IpIfIndex_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,1),_IpIfIndex_Type())
ipIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfIndex.setStatus(_A)
_IpIfName_Type=DisplayString
_IpIfName_Object=MibTableColumn
ipIfName=_IpIfName_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,2),_IpIfName_Type())
ipIfName.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfName.setStatus(_A)
_IpIfAddr_Type=IpAddress
_IpIfAddr_Object=MibTableColumn
ipIfAddr=_IpIfAddr_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,3),_IpIfAddr_Type())
ipIfAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfAddr.setStatus(_A)
_IpIfNetmask_Type=IpAddress
_IpIfNetmask_Object=MibTableColumn
ipIfNetmask=_IpIfNetmask_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,4),_IpIfNetmask_Type())
ipIfNetmask.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfNetmask.setStatus(_A)
class _IpIfVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IpIfVlan_Type.__name__=_C
_IpIfVlan_Object=MibTableColumn
ipIfVlan=_IpIfVlan_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,5),_IpIfVlan_Type())
ipIfVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfVlan.setStatus(_A)
class _IpIfProxyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_IpIfProxyArp_Type.__name__=_C
_IpIfProxyArp_Object=MibTableColumn
ipIfProxyArp=_IpIfProxyArp_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,6),_IpIfProxyArp_Type())
ipIfProxyArp.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfProxyArp.setStatus(_A)
class _IpIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_IpIfStatus_Type.__name__=_C
_IpIfStatus_Object=MibTableColumn
ipIfStatus=_IpIfStatus_Object((1,3,6,1,4,1,8691,7,99,3,1,1,1,7),_IpIfStatus_Type())
ipIfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ipIfStatus.setStatus(_A)
_StaticRoute_ObjectIdentity=ObjectIdentity
staticRoute=_StaticRoute_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,2))
_StaticRouteTable_Object=MibTable
staticRouteTable=_StaticRouteTable_Object((1,3,6,1,4,1,8691,7,99,3,2,1))
if mibBuilder.loadTexts:staticRouteTable.setStatus(_A)
_StaticRouteEntry_Object=MibTableRow
staticRouteEntry=_StaticRouteEntry_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1))
staticRouteEntry.setIndexNames((0,_E,_B4))
if mibBuilder.loadTexts:staticRouteEntry.setStatus(_A)
_StaticRouteIndex_Type=Integer32
_StaticRouteIndex_Object=MibTableColumn
staticRouteIndex=_StaticRouteIndex_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1,1),_StaticRouteIndex_Type())
staticRouteIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:staticRouteIndex.setStatus(_A)
_StaticRouteAddr_Type=IpAddress
_StaticRouteAddr_Object=MibTableColumn
staticRouteAddr=_StaticRouteAddr_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1,2),_StaticRouteAddr_Type())
staticRouteAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:staticRouteAddr.setStatus(_A)
_StaticRouteNetmask_Type=IpAddress
_StaticRouteNetmask_Object=MibTableColumn
staticRouteNetmask=_StaticRouteNetmask_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1,3),_StaticRouteNetmask_Type())
staticRouteNetmask.setMaxAccess(_F)
if mibBuilder.loadTexts:staticRouteNetmask.setStatus(_A)
_StaticRouteNexthop_Type=IpAddress
_StaticRouteNexthop_Object=MibTableColumn
staticRouteNexthop=_StaticRouteNexthop_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1,4),_StaticRouteNexthop_Type())
staticRouteNexthop.setMaxAccess(_F)
if mibBuilder.loadTexts:staticRouteNexthop.setStatus(_A)
class _StaticRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_StaticRouteMetric_Type.__name__=_C
_StaticRouteMetric_Object=MibTableColumn
staticRouteMetric=_StaticRouteMetric_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1,5),_StaticRouteMetric_Type())
staticRouteMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:staticRouteMetric.setStatus(_A)
class _StaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_StaticRouteStatus_Type.__name__=_C
_StaticRouteStatus_Object=MibTableColumn
staticRouteStatus=_StaticRouteStatus_Object((1,3,6,1,4,1,8691,7,99,3,2,1,1,6),_StaticRouteStatus_Type())
staticRouteStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:staticRouteStatus.setStatus(_A)
_Rip_ObjectIdentity=ObjectIdentity
rip=_Rip_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,3))
class _RipEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RipEnable_Type.__name__=_C
_RipEnable_Object=MibScalar
ripEnable=_RipEnable_Object((1,3,6,1,4,1,8691,7,99,3,3,1),_RipEnable_Type())
ripEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ripEnable.setStatus(_A)
class _RipVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v1compatible',3)))
_RipVersion_Type.__name__=_C
_RipVersion_Object=MibScalar
ripVersion=_RipVersion_Object((1,3,6,1,4,1,8691,7,99,3,3,2),_RipVersion_Type())
ripVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ripVersion.setStatus(_A)
class _RipRedistConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RipRedistConnected_Type.__name__=_C
_RipRedistConnected_Object=MibScalar
ripRedistConnected=_RipRedistConnected_Object((1,3,6,1,4,1,8691,7,99,3,3,3),_RipRedistConnected_Type())
ripRedistConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:ripRedistConnected.setStatus(_A)
class _RipRedistStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RipRedistStatic_Type.__name__=_C
_RipRedistStatic_Object=MibScalar
ripRedistStatic=_RipRedistStatic_Object((1,3,6,1,4,1,8691,7,99,3,3,4),_RipRedistStatic_Type())
ripRedistStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:ripRedistStatic.setStatus(_A)
class _RipRedistOspf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RipRedistOspf_Type.__name__=_C
_RipRedistOspf_Object=MibScalar
ripRedistOspf=_RipRedistOspf_Object((1,3,6,1,4,1,8691,7,99,3,3,5),_RipRedistOspf_Type())
ripRedistOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:ripRedistOspf.setStatus(_A)
_RipInterfaceTable_Object=MibTable
ripInterfaceTable=_RipInterfaceTable_Object((1,3,6,1,4,1,8691,7,99,3,3,6))
if mibBuilder.loadTexts:ripInterfaceTable.setStatus(_A)
_RipInterfaceEntry_Object=MibTableRow
ripInterfaceEntry=_RipInterfaceEntry_Object((1,3,6,1,4,1,8691,7,99,3,3,6,1))
ripInterfaceEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:ripInterfaceEntry.setStatus(_A)
_RipIfName_Type=DisplayString
_RipIfName_Object=MibTableColumn
ripIfName=_RipIfName_Object((1,3,6,1,4,1,8691,7,99,3,3,6,1,1),_RipIfName_Type())
ripIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:ripIfName.setStatus(_A)
_RipIfAddr_Type=IpAddress
_RipIfAddr_Object=MibTableColumn
ripIfAddr=_RipIfAddr_Object((1,3,6,1,4,1,8691,7,99,3,3,6,1,2),_RipIfAddr_Type())
ripIfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ripIfAddr.setStatus(_A)
_RipIfVlan_Type=Integer32
_RipIfVlan_Object=MibTableColumn
ripIfVlan=_RipIfVlan_Object((1,3,6,1,4,1,8691,7,99,3,3,6,1,3),_RipIfVlan_Type())
ripIfVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ripIfVlan.setStatus(_A)
class _RipIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RipIfEnable_Type.__name__=_C
_RipIfEnable_Object=MibTableColumn
ripIfEnable=_RipIfEnable_Object((1,3,6,1,4,1,8691,7,99,3,3,6,1,4),_RipIfEnable_Type())
ripIfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ripIfEnable.setStatus(_A)
_Ospf_ObjectIdentity=ObjectIdentity
ospf=_Ospf_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,4))
_OspfGlobal_ObjectIdentity=ObjectIdentity
ospfGlobal=_OspfGlobal_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,4,1))
class _OspfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OspfEnable_Type.__name__=_C
_OspfEnable_Object=MibScalar
ospfEnable=_OspfEnable_Object((1,3,6,1,4,1,8691,7,99,3,4,1,1),_OspfEnable_Type())
ospfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfEnable.setStatus(_A)
_OspfRouterId_Type=IpAddress
_OspfRouterId_Object=MibScalar
ospfRouterId=_OspfRouterId_Object((1,3,6,1,4,1,8691,7,99,3,4,1,2),_OspfRouterId_Type())
ospfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRouterId.setStatus(_A)
_OspfCurrentRouterId_Type=IpAddress
_OspfCurrentRouterId_Object=MibScalar
ospfCurrentRouterId=_OspfCurrentRouterId_Object((1,3,6,1,4,1,8691,7,99,3,4,1,3),_OspfCurrentRouterId_Type())
ospfCurrentRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfCurrentRouterId.setStatus(_A)
class _OspfRedistConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OspfRedistConnected_Type.__name__=_C
_OspfRedistConnected_Object=MibScalar
ospfRedistConnected=_OspfRedistConnected_Object((1,3,6,1,4,1,8691,7,99,3,4,1,4),_OspfRedistConnected_Type())
ospfRedistConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistConnected.setStatus(_A)
class _OspfRedistStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OspfRedistStatic_Type.__name__=_C
_OspfRedistStatic_Object=MibScalar
ospfRedistStatic=_OspfRedistStatic_Object((1,3,6,1,4,1,8691,7,99,3,4,1,5),_OspfRedistStatic_Type())
ospfRedistStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistStatic.setStatus(_A)
class _OspfRedistRip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OspfRedistRip_Type.__name__=_C
_OspfRedistRip_Object=MibScalar
ospfRedistRip=_OspfRedistRip_Object((1,3,6,1,4,1,8691,7,99,3,4,1,6),_OspfRedistRip_Type())
ospfRedistRip.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistRip.setStatus(_A)
_OspfArea_ObjectIdentity=ObjectIdentity
ospfArea=_OspfArea_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,4,2))
_OspfAreaTable_Object=MibTable
ospfAreaTable=_OspfAreaTable_Object((1,3,6,1,4,1,8691,7,99,3,4,2,1))
if mibBuilder.loadTexts:ospfAreaTable.setStatus(_A)
_OspfAreaEntry_Object=MibTableRow
ospfAreaEntry=_OspfAreaEntry_Object((1,3,6,1,4,1,8691,7,99,3,4,2,1,1))
ospfAreaEntry.setIndexNames((0,_E,_B5))
if mibBuilder.loadTexts:ospfAreaEntry.setStatus(_A)
_OspfAreaId_Type=IpAddress
_OspfAreaId_Object=MibTableColumn
ospfAreaId=_OspfAreaId_Object((1,3,6,1,4,1,8691,7,99,3,4,2,1,1,1),_OspfAreaId_Type())
ospfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfAreaId.setStatus(_A)
class _OspfAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_d,0),('stub',1),('nssa',2)))
_OspfAreaType_Type.__name__=_C
_OspfAreaType_Object=MibTableColumn
ospfAreaType=_OspfAreaType_Object((1,3,6,1,4,1,8691,7,99,3,4,2,1,1,2),_OspfAreaType_Type())
ospfAreaType.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfAreaType.setStatus(_A)
class _OspfAreaMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OspfAreaMetric_Type.__name__=_C
_OspfAreaMetric_Object=MibTableColumn
ospfAreaMetric=_OspfAreaMetric_Object((1,3,6,1,4,1,8691,7,99,3,4,2,1,1,3),_OspfAreaMetric_Type())
ospfAreaMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfAreaMetric.setStatus(_A)
class _OspfAreaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_OspfAreaStatus_Type.__name__=_C
_OspfAreaStatus_Object=MibTableColumn
ospfAreaStatus=_OspfAreaStatus_Object((1,3,6,1,4,1,8691,7,99,3,4,2,1,1,4),_OspfAreaStatus_Type())
ospfAreaStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfAreaStatus.setStatus(_A)
_OspfInterface_ObjectIdentity=ObjectIdentity
ospfInterface=_OspfInterface_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,4,3))
_OspfInterfaceTable_Object=MibTable
ospfInterfaceTable=_OspfInterfaceTable_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1))
if mibBuilder.loadTexts:ospfInterfaceTable.setStatus(_A)
_OspfInterfaceEntry_Object=MibTableRow
ospfInterfaceEntry=_OspfInterfaceEntry_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1))
ospfInterfaceEntry.setIndexNames((0,_E,_B6))
if mibBuilder.loadTexts:ospfInterfaceEntry.setStatus(_A)
_OspfIfIndex_Type=Integer32
_OspfIfIndex_Object=MibTableColumn
ospfIfIndex=_OspfIfIndex_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,1),_OspfIfIndex_Type())
ospfIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfIfIndex.setStatus(_A)
_OspfIfName_Type=DisplayString
_OspfIfName_Object=MibTableColumn
ospfIfName=_OspfIfName_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,2),_OspfIfName_Type())
ospfIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfName.setStatus(_A)
_OspfIfAddr_Type=IpAddress
_OspfIfAddr_Object=MibTableColumn
ospfIfAddr=_OspfIfAddr_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,3),_OspfIfAddr_Type())
ospfIfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfAddr.setStatus(_A)
_OspfIfAreaId_Type=IpAddress
_OspfIfAreaId_Object=MibTableColumn
ospfIfAreaId=_OspfIfAreaId_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,4),_OspfIfAreaId_Type())
ospfIfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfAreaId.setStatus(_A)
_OspfIfState_Type=DisplayString
_OspfIfState_Object=MibTableColumn
ospfIfState=_OspfIfState_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,5),_OspfIfState_Type())
ospfIfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfState.setStatus(_A)
class _OspfIfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfIfPriority_Type.__name__=_C
_OspfIfPriority_Object=MibTableColumn
ospfIfPriority=_OspfIfPriority_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,6),_OspfIfPriority_Type())
ospfIfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfPriority.setStatus(_A)
class _OspfIfHelloInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfIfHelloInterval_Type.__name__=_C
_OspfIfHelloInterval_Object=MibTableColumn
ospfIfHelloInterval=_OspfIfHelloInterval_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,7),_OspfIfHelloInterval_Type())
ospfIfHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfHelloInterval.setStatus(_A)
class _OspfIfDeadInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfIfDeadInterval_Type.__name__=_C
_OspfIfDeadInterval_Object=MibTableColumn
ospfIfDeadInterval=_OspfIfDeadInterval_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,8),_OspfIfDeadInterval_Type())
ospfIfDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfDeadInterval.setStatus(_A)
class _OspfIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('null',0),('simple',1),('md5',2)))
_OspfIfAuthType_Type.__name__=_C
_OspfIfAuthType_Object=MibTableColumn
ospfIfAuthType=_OspfIfAuthType_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,9),_OspfIfAuthType_Type())
ospfIfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfAuthType.setStatus(_A)
_OspfIfAuthKey_Type=DisplayString
_OspfIfAuthKey_Object=MibTableColumn
ospfIfAuthKey=_OspfIfAuthKey_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,10),_OspfIfAuthKey_Type())
ospfIfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfAuthKey.setStatus(_A)
class _OspfIfMd5KeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OspfIfMd5KeyId_Type.__name__=_C
_OspfIfMd5KeyId_Object=MibTableColumn
ospfIfMd5KeyId=_OspfIfMd5KeyId_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,11),_OspfIfMd5KeyId_Type())
ospfIfMd5KeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMd5KeyId.setStatus(_A)
class _OspfIfMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfIfMetric_Type.__name__=_C
_OspfIfMetric_Object=MibTableColumn
ospfIfMetric=_OspfIfMetric_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,12),_OspfIfMetric_Type())
ospfIfMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMetric.setStatus(_A)
class _OspfIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_OspfIfStatus_Type.__name__=_C
_OspfIfStatus_Object=MibTableColumn
ospfIfStatus=_OspfIfStatus_Object((1,3,6,1,4,1,8691,7,99,3,4,3,1,1,13),_OspfIfStatus_Type())
ospfIfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfIfStatus.setStatus(_A)
_OspfVirtualLink_ObjectIdentity=ObjectIdentity
ospfVirtualLink=_OspfVirtualLink_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,4,4))
_OspfVlinkTable_Object=MibTable
ospfVlinkTable=_OspfVlinkTable_Object((1,3,6,1,4,1,8691,7,99,3,4,4,1))
if mibBuilder.loadTexts:ospfVlinkTable.setStatus(_A)
_OspfVlinkEntry_Object=MibTableRow
ospfVlinkEntry=_OspfVlinkEntry_Object((1,3,6,1,4,1,8691,7,99,3,4,4,1,1))
ospfVlinkEntry.setIndexNames((0,_E,_B7))
if mibBuilder.loadTexts:ospfVlinkEntry.setStatus(_A)
_OspfVlinkIndex_Type=Integer32
_OspfVlinkIndex_Object=MibTableColumn
ospfVlinkIndex=_OspfVlinkIndex_Object((1,3,6,1,4,1,8691,7,99,3,4,4,1,1,1),_OspfVlinkIndex_Type())
ospfVlinkIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfVlinkIndex.setStatus(_A)
_OspfTransitAreaId_Type=IpAddress
_OspfTransitAreaId_Object=MibTableColumn
ospfTransitAreaId=_OspfTransitAreaId_Object((1,3,6,1,4,1,8691,7,99,3,4,4,1,1,2),_OspfTransitAreaId_Type())
ospfTransitAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTransitAreaId.setStatus(_A)
_OspfNeighborAreaId_Type=IpAddress
_OspfNeighborAreaId_Object=MibTableColumn
ospfNeighborAreaId=_OspfNeighborAreaId_Object((1,3,6,1,4,1,8691,7,99,3,4,4,1,1,3),_OspfNeighborAreaId_Type())
ospfNeighborAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNeighborAreaId.setStatus(_A)
class _OspfVlinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_OspfVlinkStatus_Type.__name__=_C
_OspfVlinkStatus_Object=MibTableColumn
ospfVlinkStatus=_OspfVlinkStatus_Object((1,3,6,1,4,1,8691,7,99,3,4,4,1,1,4),_OspfVlinkStatus_Type())
ospfVlinkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfVlinkStatus.setStatus(_A)
_OspfAggregation_ObjectIdentity=ObjectIdentity
ospfAggregation=_OspfAggregation_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,4,5))
_OspfAggregationTable_Object=MibTable
ospfAggregationTable=_OspfAggregationTable_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1))
if mibBuilder.loadTexts:ospfAggregationTable.setStatus(_A)
_OspfAggregationEntry_Object=MibTableRow
ospfAggregationEntry=_OspfAggregationEntry_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1,1))
ospfAggregationEntry.setIndexNames((0,_E,_B8))
if mibBuilder.loadTexts:ospfAggregationEntry.setStatus(_A)
_OspfAggrIndex_Type=Integer32
_OspfAggrIndex_Object=MibTableColumn
ospfAggrIndex=_OspfAggrIndex_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1,1,1),_OspfAggrIndex_Type())
ospfAggrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfAggrIndex.setStatus(_A)
_OspfAggrAreaId_Type=IpAddress
_OspfAggrAreaId_Object=MibTableColumn
ospfAggrAreaId=_OspfAggrAreaId_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1,1,2),_OspfAggrAreaId_Type())
ospfAggrAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAggrAreaId.setStatus(_A)
_OspfAggrAddr_Type=IpAddress
_OspfAggrAddr_Object=MibTableColumn
ospfAggrAddr=_OspfAggrAddr_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1,1,3),_OspfAggrAddr_Type())
ospfAggrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAggrAddr.setStatus(_A)
_OspfAggrMask_Type=IpAddress
_OspfAggrMask_Object=MibTableColumn
ospfAggrMask=_OspfAggrMask_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1,1,4),_OspfAggrMask_Type())
ospfAggrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAggrMask.setStatus(_A)
class _OspfAggrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_K,1),(_P,4),(_Q,5),(_R,6)))
_OspfAggrStatus_Type.__name__=_C
_OspfAggrStatus_Object=MibTableColumn
ospfAggrStatus=_OspfAggrStatus_Object((1,3,6,1,4,1,8691,7,99,3,4,5,1,1,5),_OspfAggrStatus_Type())
ospfAggrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ospfAggrStatus.setStatus(_A)
_IpRoutingTable_Object=MibTable
ipRoutingTable=_IpRoutingTable_Object((1,3,6,1,4,1,8691,7,99,3,5))
if mibBuilder.loadTexts:ipRoutingTable.setStatus(_A)
_IpRoutingEntry_Object=MibTableRow
ipRoutingEntry=_IpRoutingEntry_Object((1,3,6,1,4,1,8691,7,99,3,5,1))
ipRoutingEntry.setIndexNames((0,_E,_B9))
if mibBuilder.loadTexts:ipRoutingEntry.setStatus(_A)
_IpRoutingIndex_Type=Integer32
_IpRoutingIndex_Object=MibTableColumn
ipRoutingIndex=_IpRoutingIndex_Object((1,3,6,1,4,1,8691,7,99,3,5,1,1),_IpRoutingIndex_Type())
ipRoutingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingIndex.setStatus(_A)
_IpRoutingType_Type=DisplayString
_IpRoutingType_Object=MibTableColumn
ipRoutingType=_IpRoutingType_Object((1,3,6,1,4,1,8691,7,99,3,5,1,2),_IpRoutingType_Type())
ipRoutingType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingType.setStatus(_A)
_IpRoutingDest_Type=DisplayString
_IpRoutingDest_Object=MibTableColumn
ipRoutingDest=_IpRoutingDest_Object((1,3,6,1,4,1,8691,7,99,3,5,1,3),_IpRoutingDest_Type())
ipRoutingDest.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingDest.setStatus(_A)
_IpRoutingNextHop_Type=IpAddress
_IpRoutingNextHop_Object=MibTableColumn
ipRoutingNextHop=_IpRoutingNextHop_Object((1,3,6,1,4,1,8691,7,99,3,5,1,4),_IpRoutingNextHop_Type())
ipRoutingNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingNextHop.setStatus(_A)
_IpRoutingIfName_Type=DisplayString
_IpRoutingIfName_Object=MibTableColumn
ipRoutingIfName=_IpRoutingIfName_Object((1,3,6,1,4,1,8691,7,99,3,5,1,5),_IpRoutingIfName_Type())
ipRoutingIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingIfName.setStatus(_A)
_IpRoutingMetric_Type=Integer32
_IpRoutingMetric_Object=MibTableColumn
ipRoutingMetric=_IpRoutingMetric_Object((1,3,6,1,4,1,8691,7,99,3,5,1,6),_IpRoutingMetric_Type())
ipRoutingMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingMetric.setStatus(_A)
_IpRoutingVlan_Type=Integer32
_IpRoutingVlan_Object=MibTableColumn
ipRoutingVlan=_IpRoutingVlan_Object((1,3,6,1,4,1,8691,7,99,3,5,1,7),_IpRoutingVlan_Type())
ipRoutingVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRoutingVlan.setStatus(_A)
_Vrrp_ObjectIdentity=ObjectIdentity
vrrp=_Vrrp_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,6))
_VrrpInterfaceTable_Object=MibTable
vrrpInterfaceTable=_VrrpInterfaceTable_Object((1,3,6,1,4,1,8691,7,99,3,6,1))
if mibBuilder.loadTexts:vrrpInterfaceTable.setStatus(_A)
_VrrpInterfaceEntry_Object=MibTableRow
vrrpInterfaceEntry=_VrrpInterfaceEntry_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1))
vrrpInterfaceEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:vrrpInterfaceEntry.setStatus(_A)
_VrrpIfName_Type=DisplayString
_VrrpIfName_Object=MibTableColumn
vrrpIfName=_VrrpIfName_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,1),_VrrpIfName_Type())
vrrpIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpIfName.setStatus(_A)
_VrrpIfAddr_Type=IpAddress
_VrrpIfAddr_Object=MibTableColumn
vrrpIfAddr=_VrrpIfAddr_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,2),_VrrpIfAddr_Type())
vrrpIfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpIfAddr.setStatus(_A)
_VrrpIfVlan_Type=Integer32
_VrrpIfVlan_Object=MibTableColumn
vrrpIfVlan=_VrrpIfVlan_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,3),_VrrpIfVlan_Type())
vrrpIfVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpIfVlan.setStatus(_A)
class _VrrpIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_VrrpIfEnable_Type.__name__=_C
_VrrpIfEnable_Object=MibTableColumn
vrrpIfEnable=_VrrpIfEnable_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,4),_VrrpIfEnable_Type())
vrrpIfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfEnable.setStatus(_A)
_VrrpIfVirtualIp_Type=IpAddress
_VrrpIfVirtualIp_Object=MibTableColumn
vrrpIfVirtualIp=_VrrpIfVirtualIp_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,5),_VrrpIfVirtualIp_Type())
vrrpIfVirtualIp.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfVirtualIp.setStatus(_A)
class _VrrpIfRouterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpIfRouterId_Type.__name__=_C
_VrrpIfRouterId_Object=MibTableColumn
vrrpIfRouterId=_VrrpIfRouterId_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,6),_VrrpIfRouterId_Type())
vrrpIfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfRouterId.setStatus(_A)
class _VrrpIfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpIfPriority_Type.__name__=_C
_VrrpIfPriority_Object=MibTableColumn
vrrpIfPriority=_VrrpIfPriority_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,7),_VrrpIfPriority_Type())
vrrpIfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfPriority.setStatus(_A)
class _VrrpIfPreemptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_VrrpIfPreemptionMode_Type.__name__=_C
_VrrpIfPreemptionMode_Object=MibTableColumn
vrrpIfPreemptionMode=_VrrpIfPreemptionMode_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,8),_VrrpIfPreemptionMode_Type())
vrrpIfPreemptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfPreemptionMode.setStatus(_A)
_VrrpIfStatus_Type=DisplayString
_VrrpIfStatus_Object=MibTableColumn
vrrpIfStatus=_VrrpIfStatus_Object((1,3,6,1,4,1,8691,7,99,3,6,1,1,9),_VrrpIfStatus_Type())
vrrpIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpIfStatus.setStatus(_A)
class _VrrpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_VrrpEnable_Type.__name__=_C
_VrrpEnable_Object=MibScalar
vrrpEnable=_VrrpEnable_Object((1,3,6,1,4,1,8691,7,99,3,6,2),_VrrpEnable_Type())
vrrpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpEnable.setStatus(_A)
class _VrrpAdverInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,1000))
_VrrpAdverInt_Type.__name__=_C
_VrrpAdverInt_Object=MibScalar
vrrpAdverInt=_VrrpAdverInt_Object((1,3,6,1,4,1,8691,7,99,3,6,3),_VrrpAdverInt_Type())
vrrpAdverInt.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpAdverInt.setStatus(_A)
_Dvmrp_ObjectIdentity=ObjectIdentity
dvmrp=_Dvmrp_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,7))
class _DvmrpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DvmrpEnable_Type.__name__=_C
_DvmrpEnable_Object=MibScalar
dvmrpEnable=_DvmrpEnable_Object((1,3,6,1,4,1,8691,7,99,3,7,1),_DvmrpEnable_Type())
dvmrpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpEnable.setStatus(_A)
_DvmrpInterfaceTable_Object=MibTable
dvmrpInterfaceTable=_DvmrpInterfaceTable_Object((1,3,6,1,4,1,8691,7,99,3,7,2))
if mibBuilder.loadTexts:dvmrpInterfaceTable.setStatus(_A)
_DvmrpInterfaceEntry_Object=MibTableRow
dvmrpInterfaceEntry=_DvmrpInterfaceEntry_Object((1,3,6,1,4,1,8691,7,99,3,7,2,1))
dvmrpInterfaceEntry.setIndexNames((0,_E,_BA))
if mibBuilder.loadTexts:dvmrpInterfaceEntry.setStatus(_A)
_DvmrpIfIndex_Type=Integer32
_DvmrpIfIndex_Object=MibTableColumn
dvmrpIfIndex=_DvmrpIfIndex_Object((1,3,6,1,4,1,8691,7,99,3,7,2,1,1),_DvmrpIfIndex_Type())
dvmrpIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIfIndex.setStatus(_A)
_DvmrpIfName_Type=DisplayString
_DvmrpIfName_Object=MibTableColumn
dvmrpIfName=_DvmrpIfName_Object((1,3,6,1,4,1,8691,7,99,3,7,2,1,2),_DvmrpIfName_Type())
dvmrpIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIfName.setStatus(_A)
_DvmrpIfAddr_Type=IpAddress
_DvmrpIfAddr_Object=MibTableColumn
dvmrpIfAddr=_DvmrpIfAddr_Object((1,3,6,1,4,1,8691,7,99,3,7,2,1,3),_DvmrpIfAddr_Type())
dvmrpIfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIfAddr.setStatus(_A)
_DvmrpIfVlan_Type=Integer32
_DvmrpIfVlan_Object=MibTableColumn
dvmrpIfVlan=_DvmrpIfVlan_Object((1,3,6,1,4,1,8691,7,99,3,7,2,1,4),_DvmrpIfVlan_Type())
dvmrpIfVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIfVlan.setStatus(_A)
class _DvmrpIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DvmrpIfEnable_Type.__name__=_C
_DvmrpIfEnable_Object=MibTableColumn
dvmrpIfEnable=_DvmrpIfEnable_Object((1,3,6,1,4,1,8691,7,99,3,7,2,1,5),_DvmrpIfEnable_Type())
dvmrpIfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIfEnable.setStatus(_A)
_DvmrpMulticastRoutingTable_Object=MibTable
dvmrpMulticastRoutingTable=_DvmrpMulticastRoutingTable_Object((1,3,6,1,4,1,8691,7,99,3,7,3))
if mibBuilder.loadTexts:dvmrpMulticastRoutingTable.setStatus(_A)
_DvmrpMulticastRoutingEntry_Object=MibTableRow
dvmrpMulticastRoutingEntry=_DvmrpMulticastRoutingEntry_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1))
dvmrpMulticastRoutingEntry.setIndexNames((0,_E,_BB))
if mibBuilder.loadTexts:dvmrpMulticastRoutingEntry.setStatus(_A)
_DvmrpMRIndex_Type=Integer32
_DvmrpMRIndex_Object=MibTableColumn
dvmrpMRIndex=_DvmrpMRIndex_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,1),_DvmrpMRIndex_Type())
dvmrpMRIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpMRIndex.setStatus(_A)
_DvmrpMRGroup_Type=IpAddress
_DvmrpMRGroup_Object=MibTableColumn
dvmrpMRGroup=_DvmrpMRGroup_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,2),_DvmrpMRGroup_Type())
dvmrpMRGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRGroup.setStatus(_A)
_DvmrpMRSource_Type=IpAddress
_DvmrpMRSource_Object=MibTableColumn
dvmrpMRSource=_DvmrpMRSource_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,3),_DvmrpMRSource_Type())
dvmrpMRSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRSource.setStatus(_A)
_DvmrpMRUpstream_Type=DisplayString
_DvmrpMRUpstream_Object=MibTableColumn
dvmrpMRUpstream=_DvmrpMRUpstream_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,4),_DvmrpMRUpstream_Type())
dvmrpMRUpstream.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRUpstream.setStatus(_A)
_DvmrpMRIncomingIfname_Type=DisplayString
_DvmrpMRIncomingIfname_Object=MibTableColumn
dvmrpMRIncomingIfname=_DvmrpMRIncomingIfname_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,5),_DvmrpMRIncomingIfname_Type())
dvmrpMRIncomingIfname.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRIncomingIfname.setStatus(_A)
_DvmrpMRVid_Type=DisplayString
_DvmrpMRVid_Object=MibTableColumn
dvmrpMRVid=_DvmrpMRVid_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,6),_DvmrpMRVid_Type())
dvmrpMRVid.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRVid.setStatus(_A)
_DvmrpMRExpiretime_Type=DisplayString
_DvmrpMRExpiretime_Object=MibTableColumn
dvmrpMRExpiretime=_DvmrpMRExpiretime_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,7),_DvmrpMRExpiretime_Type())
dvmrpMRExpiretime.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRExpiretime.setStatus(_A)
_DvmrpMRLefttime_Type=DisplayString
_DvmrpMRLefttime_Object=MibTableColumn
dvmrpMRLefttime=_DvmrpMRLefttime_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,8),_DvmrpMRLefttime_Type())
dvmrpMRLefttime.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRLefttime.setStatus(_A)
_DvmrpMRDowntreamVid_Type=DisplayString
_DvmrpMRDowntreamVid_Object=MibTableColumn
dvmrpMRDowntreamVid=_DvmrpMRDowntreamVid_Object((1,3,6,1,4,1,8691,7,99,3,7,3,1,9),_DvmrpMRDowntreamVid_Type())
dvmrpMRDowntreamVid.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpMRDowntreamVid.setStatus(_A)
_Pimdm_ObjectIdentity=ObjectIdentity
pimdm=_Pimdm_ObjectIdentity((1,3,6,1,4,1,8691,7,99,3,8))
class _PimdmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_PimdmEnable_Type.__name__=_C
_PimdmEnable_Object=MibScalar
pimdmEnable=_PimdmEnable_Object((1,3,6,1,4,1,8691,7,99,3,8,1),_PimdmEnable_Type())
pimdmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pimdmEnable.setStatus(_A)
_PimdmInterfaceTable_Object=MibTable
pimdmInterfaceTable=_PimdmInterfaceTable_Object((1,3,6,1,4,1,8691,7,99,3,8,2))
if mibBuilder.loadTexts:pimdmInterfaceTable.setStatus(_A)
_PimdmInterfaceEntry_Object=MibTableRow
pimdmInterfaceEntry=_PimdmInterfaceEntry_Object((1,3,6,1,4,1,8691,7,99,3,8,2,1))
pimdmInterfaceEntry.setIndexNames((0,_E,_BC))
if mibBuilder.loadTexts:pimdmInterfaceEntry.setStatus(_A)
_PimdmIfIndex_Type=Integer32
_PimdmIfIndex_Object=MibTableColumn
pimdmIfIndex=_PimdmIfIndex_Object((1,3,6,1,4,1,8691,7,99,3,8,2,1,1),_PimdmIfIndex_Type())
pimdmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmIfIndex.setStatus(_A)
_PimdmIfName_Type=DisplayString
_PimdmIfName_Object=MibTableColumn
pimdmIfName=_PimdmIfName_Object((1,3,6,1,4,1,8691,7,99,3,8,2,1,2),_PimdmIfName_Type())
pimdmIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmIfName.setStatus(_A)
_PimdmIfAddr_Type=IpAddress
_PimdmIfAddr_Object=MibTableColumn
pimdmIfAddr=_PimdmIfAddr_Object((1,3,6,1,4,1,8691,7,99,3,8,2,1,3),_PimdmIfAddr_Type())
pimdmIfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmIfAddr.setStatus(_A)
_PimdmIfVlan_Type=Integer32
_PimdmIfVlan_Object=MibTableColumn
pimdmIfVlan=_PimdmIfVlan_Object((1,3,6,1,4,1,8691,7,99,3,8,2,1,4),_PimdmIfVlan_Type())
pimdmIfVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmIfVlan.setStatus(_A)
class _PimdmIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_PimdmIfEnable_Type.__name__=_C
_PimdmIfEnable_Object=MibTableColumn
pimdmIfEnable=_PimdmIfEnable_Object((1,3,6,1,4,1,8691,7,99,3,8,2,1,5),_PimdmIfEnable_Type())
pimdmIfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pimdmIfEnable.setStatus(_A)
_PimdmMulticastRoutingTable_Object=MibTable
pimdmMulticastRoutingTable=_PimdmMulticastRoutingTable_Object((1,3,6,1,4,1,8691,7,99,3,8,3))
if mibBuilder.loadTexts:pimdmMulticastRoutingTable.setStatus(_A)
_PimdmMulticastRoutingEntry_Object=MibTableRow
pimdmMulticastRoutingEntry=_PimdmMulticastRoutingEntry_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1))
pimdmMulticastRoutingEntry.setIndexNames((0,_E,_BD))
if mibBuilder.loadTexts:pimdmMulticastRoutingEntry.setStatus(_A)
_PimdmMRIndex_Type=Integer32
_PimdmMRIndex_Object=MibTableColumn
pimdmMRIndex=_PimdmMRIndex_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,1),_PimdmMRIndex_Type())
pimdmMRIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pimdmMRIndex.setStatus(_A)
_PimdmMRGroup_Type=IpAddress
_PimdmMRGroup_Object=MibTableColumn
pimdmMRGroup=_PimdmMRGroup_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,2),_PimdmMRGroup_Type())
pimdmMRGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRGroup.setStatus(_A)
_PimdmMRSource_Type=IpAddress
_PimdmMRSource_Object=MibTableColumn
pimdmMRSource=_PimdmMRSource_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,3),_PimdmMRSource_Type())
pimdmMRSource.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRSource.setStatus(_A)
_PimdmMRUpstream_Type=DisplayString
_PimdmMRUpstream_Object=MibTableColumn
pimdmMRUpstream=_PimdmMRUpstream_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,4),_PimdmMRUpstream_Type())
pimdmMRUpstream.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRUpstream.setStatus(_A)
_PimdmMRIncomingIfname_Type=DisplayString
_PimdmMRIncomingIfname_Object=MibTableColumn
pimdmMRIncomingIfname=_PimdmMRIncomingIfname_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,5),_PimdmMRIncomingIfname_Type())
pimdmMRIncomingIfname.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRIncomingIfname.setStatus(_A)
_PimdmMRVid_Type=Integer32
_PimdmMRVid_Object=MibTableColumn
pimdmMRVid=_PimdmMRVid_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,6),_PimdmMRVid_Type())
pimdmMRVid.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRVid.setStatus(_A)
_PimdmMRLefttime_Type=DisplayString
_PimdmMRLefttime_Object=MibTableColumn
pimdmMRLefttime=_PimdmMRLefttime_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,7),_PimdmMRLefttime_Type())
pimdmMRLefttime.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRLefttime.setStatus(_A)
_PimdmMRDowntreamVid_Type=DisplayString
_PimdmMRDowntreamVid_Object=MibTableColumn
pimdmMRDowntreamVid=_PimdmMRDowntreamVid_Object((1,3,6,1,4,1,8691,7,99,3,8,3,1,8),_PimdmMRDowntreamVid_Type())
pimdmMRDowntreamVid.setMaxAccess(_D)
if mibBuilder.loadTexts:pimdmMRDowntreamVid.setStatus(_A)
configChangeTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,1))
configChangeTrap.setObjects((_E,_BE))
if mibBuilder.loadTexts:configChangeTrap.setStatus(_A)
power1Trap=NotificationType((1,3,6,1,4,1,8691,7,99,0,2))
power1Trap.setObjects((_E,_BF))
if mibBuilder.loadTexts:power1Trap.setStatus(_A)
power2Trap=NotificationType((1,3,6,1,4,1,8691,7,99,0,3))
power2Trap.setObjects((_E,_BG))
if mibBuilder.loadTexts:power2Trap.setStatus(_A)
trafficOverloadTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,4))
trafficOverloadTrap.setObjects((_E,_BH))
if mibBuilder.loadTexts:trafficOverloadTrap.setStatus(_A)
redundancyTopologyChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,5))
redundancyTopologyChangedTrap.setObjects((_E,_BI))
if mibBuilder.loadTexts:redundancyTopologyChangedTrap.setStatus(_A)
turboRingCouplingPortChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,6))
turboRingCouplingPortChangedTrap.setObjects((_E,_BJ))
if mibBuilder.loadTexts:turboRingCouplingPortChangedTrap.setStatus(_A)
turboRingMasterChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,7))
turboRingMasterChangedTrap.setObjects((_E,_A7))
if mibBuilder.loadTexts:turboRingMasterChangedTrap.setStatus(_A)
portLoopDetectedTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,17))
portLoopDetectedTrap.setObjects((_E,_BK))
if mibBuilder.loadTexts:portLoopDetectedTrap.setStatus(_A)
rateLimitedOnTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,18))
rateLimitedOnTrap.setObjects((_E,_BL))
if mibBuilder.loadTexts:rateLimitedOnTrap.setStatus(_A)
lldpChgTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,19))
lldpChgTrap.setObjects((_E,_BM))
if mibBuilder.loadTexts:lldpChgTrap.setStatus(_A)
abc02WarningTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,20))
abc02WarningTrap.setObjects((_E,_BN))
if mibBuilder.loadTexts:abc02WarningTrap.setStatus(_A)
turboRingMasterMismatchTrap=NotificationType((1,3,6,1,4,1,8691,7,99,0,22))
turboRingMasterMismatchTrap.setObjects((_E,_A7))
if mibBuilder.loadTexts:turboRingMasterMismatchTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'moxa':moxa,'industrialEthernet':industrialEthernet,'icsg7826a':icsg7826a,'mibNotificationsPrefix':mibNotificationsPrefix,'configChangeTrap':configChangeTrap,'power1Trap':power1Trap,'power2Trap':power2Trap,'trafficOverloadTrap':trafficOverloadTrap,'redundancyTopologyChangedTrap':redundancyTopologyChangedTrap,'turboRingCouplingPortChangedTrap':turboRingCouplingPortChangedTrap,'turboRingMasterChangedTrap':turboRingMasterChangedTrap,'portLoopDetectedTrap':portLoopDetectedTrap,'rateLimitedOnTrap':rateLimitedOnTrap,'lldpChgTrap':lldpChgTrap,'abc02WarningTrap':abc02WarningTrap,'turboRingMasterMismatchTrap':turboRingMasterMismatchTrap,'swMgmt':swMgmt,'numberOfPorts':numberOfPorts,'switchModel':switchModel,'firmwareVersion':firmwareVersion,'enableWebConfig':enableWebConfig,'enableTelnetConsole':enableTelnetConsole,'lineSwapRecovery':lineSwapRecovery,'networkSetting':networkSetting,'switchIpAddr':switchIpAddr,'switchIpMask':switchIpMask,'defaultGateway':defaultGateway,'enableAutoIpConfig':enableAutoIpConfig,'dnsServer1IpAddr':dnsServer1IpAddr,'snmpTrapCommunity':snmpTrapCommunity,'trapServerAddr':trapServerAddr,'dnsServer2IpAddr':dnsServer2IpAddr,'snmpReadCommunity':snmpReadCommunity,'snmpTrap2Community':snmpTrap2Community,'trap2ServerAddr':trap2ServerAddr,'snmpInformEnable':snmpInformEnable,'snmpInformRetries':snmpInformRetries,'snmpInformTimeout':snmpInformTimeout,'dhcpRetryPeriods':dhcpRetryPeriods,'dhcpRetryTimes':dhcpRetryTimes,'portSetting':portSetting,'portTable':portTable,'portEntry':portEntry,_M:portIndex,'portDesc':portDesc,'portEnable':portEnable,'portSpeed':portSpeed,'portMDI':portMDI,'portFDXFlowCtrl':portFDXFlowCtrl,'portName':portName,'monitor':monitor,'power1InputStatus':power1InputStatus,'power2InputStatus':power2InputStatus,'monitorPortTable':monitorPortTable,'monitorPortEntry':monitorPortEntry,'monitorLinkStatus':monitorLinkStatus,'monitorSpeed':monitorSpeed,'monitorAutoMDI':monitorAutoMDI,'monitorTraffic':monitorTraffic,'monitorFDXFlowCtrl':monitorFDXFlowCtrl,'monitorTxTraffic':monitorTxTraffic,'monitorRxTraffic':monitorRxTraffic,'monitorDiTable':monitorDiTable,'monitorDiEntry':monitorDiEntry,_p:diIndex,'diInputStatus':diInputStatus,'monitorSFPTable':monitorSFPTable,'monitorSFPEntry':monitorSFPEntry,'sfpPort':sfpPort,'sfpModelName':sfpModelName,'sfpTemperature':sfpTemperature,'sfpVoltage':sfpVoltage,'sfpTxPower':sfpTxPower,'sfpRxPower':sfpRxPower,'powerConsumption':powerConsumption,'emailWarning':emailWarning,'emailService':emailService,'emailWarningMailServer':emailWarningMailServer,'emailWarningFirstEmailAddr':emailWarningFirstEmailAddr,'emailWarningSecondEmailAddr':emailWarningSecondEmailAddr,'emailWarningThirdEmailAddr':emailWarningThirdEmailAddr,'emailWarningFourthEmailAddr':emailWarningFourthEmailAddr,'emailWarningSMTPPort':emailWarningSMTPPort,'setDeviceIp':setDeviceIp,'setDevIpTable':setDevIpTable,'setDevIpEntry':setDevIpEntry,_AF:setDevIpIndex,'setDevIpCurrentIpofDevice':setDevIpCurrentIpofDevice,'setDevIpPresentBy':setDevIpPresentBy,'setDevIpDedicatedIp':setDevIpDedicatedIp,'mirroring':mirroring,'targetPort':targetPort,'mirroringPort':mirroringPort,'monitorDirection':monitorDirection,'portTrunking':portTrunking,'trunkSettingTable':trunkSettingTable,'trunkSettingEntry':trunkSettingEntry,_AG:trunkSettingIndex,'trunkType':trunkType,'trunkMemberPorts':trunkMemberPorts,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_AH:trunkIndex,_AI:trunkPort,'trunkStatus':trunkStatus,'commRedundancy':commRedundancy,'protocolOfRedundancySetup':protocolOfRedundancySetup,_r:turboRing,'turboRingMaster':turboRingMaster,'turboRingMasterSetup':turboRingMasterSetup,'turboRingPortTable':turboRingPortTable,'turboRingPortEntry':turboRingPortEntry,_AJ:turboRingPortIndex,'turboRingPortStatus':turboRingPortStatus,'turboRingPortDesignatedBridge':turboRingPortDesignatedBridge,'turboRingPortDesignatedPort':turboRingPortDesignatedPort,'turboRingDesignatedMaster':turboRingDesignatedMaster,'turboRingRdntPort1':turboRingRdntPort1,'turboRingRdntPort2':turboRingRdntPort2,'turboRingEnableCoupling':turboRingEnableCoupling,'turboRingCouplingPort':turboRingCouplingPort,'turboRingCouplingPortStatus':turboRingCouplingPortStatus,'turboRingControlPort':turboRingControlPort,'turboRingControlPortStatus':turboRingControlPortStatus,'turboRingBrokenStatus':turboRingBrokenStatus,_q:spanningTree,'spanningTreeRoot':spanningTreeRoot,'spanningTreeBridgePriority':spanningTreeBridgePriority,'spanningTreeHelloTime':spanningTreeHelloTime,'spanningTreeMaxAge':spanningTreeMaxAge,'spanningTreeForwardingDelay':spanningTreeForwardingDelay,'spanningTreeTable':spanningTreeTable,'spanningTreeEntry':spanningTreeEntry,_AK:spanningTreeIndex,'enableSpanningTree':enableSpanningTree,'spanningTreePortPriority':spanningTreePortPriority,'spanningTreePortCost':spanningTreePortCost,'spanningTreePortStatus':spanningTreePortStatus,'spanningTreePortEdge':spanningTreePortEdge,'activeProtocolOfRedundancy':activeProtocolOfRedundancy,_s:turboRingV2,'turboRingV2Ring1':turboRingV2Ring1,'ringIndexRing1':ringIndexRing1,'ringEnableRing1':ringEnableRing1,'masterSetupRing1':masterSetupRing1,'masterStatusRing1':masterStatusRing1,'designatedMasterRing1':designatedMasterRing1,'rdnt1stPortRing1':rdnt1stPortRing1,'rdnt1stPortStatusRing1':rdnt1stPortStatusRing1,'rdnt2ndPortRing1':rdnt2ndPortRing1,'rdnt2ndPortStatusRing1':rdnt2ndPortStatusRing1,'brokenStatusRing1':brokenStatusRing1,'turboRingV2Ring2':turboRingV2Ring2,'ringIndexRing2':ringIndexRing2,'ringEnableRing2':ringEnableRing2,'masterSetupRing2':masterSetupRing2,'masterStatusRing2':masterStatusRing2,'designatedMasterRing2':designatedMasterRing2,'rdnt1stPortRing2':rdnt1stPortRing2,'rdnt1stPortStatusRing2':rdnt1stPortStatusRing2,'rdnt2ndPortRing2':rdnt2ndPortRing2,'rdnt2ndPortStatusRing2':rdnt2ndPortStatusRing2,'brokenStatusRing2':brokenStatusRing2,'turboRingV2Coupling':turboRingV2Coupling,'couplingEnable':couplingEnable,'couplingMode':couplingMode,'coupling1stPort':coupling1stPort,'coupling1stPortStatus':coupling1stPortStatus,'coupling2ndPort':coupling2ndPort,'coupling2ndPortStatus':coupling2ndPortStatus,_t:turboChain,'turboChainRole':turboChainRole,'turboChainPort1':turboChainPort1,'turboChainPort2':turboChainPort2,'turboChainPort1Status':turboChainPort1Status,'turboChainPort2Status':turboChainPort2Status,'turboChainPort1PartnerBridge':turboChainPort1PartnerBridge,'turboChainPort2PartnerBridge':turboChainPort2PartnerBridge,'relayWarning':relayWarning,'relayWarningTable':relayWarningTable,'relayWarningEntry':relayWarningEntry,_h:relayAlarmIndex,'relayWarningRelayContact':relayWarningRelayContact,'overrideRelayWarningSetting':overrideRelayWarningSetting,'relayWarningPower1Off':relayWarningPower1Off,'relayWarningPower1OffStatus':relayWarningPower1OffStatus,'relayWarningPower2Off':relayWarningPower2Off,'relayWarningPower2OffStatus':relayWarningPower2OffStatus,'relayWarningTurboRingBreak':relayWarningTurboRingBreak,'relayWarningTurboRingBreakStatus':relayWarningTurboRingBreakStatus,'portRelayWarningTable':portRelayWarningTable,'portRelayWarningEntry':portRelayWarningEntry,'relayWarningLinkChanged':relayWarningLinkChanged,'relayWarningLinkChangedStatus':relayWarningLinkChangedStatus,'relayWarningTrafficOverload':relayWarningTrafficOverload,'relayWarningTrafficOverloadStatus':relayWarningTrafficOverloadStatus,'relayWarningRxTrafficThreshold':relayWarningRxTrafficThreshold,'relayWarningTrafficDuration':relayWarningTrafficDuration,'diRelayWarningTable':diRelayWarningTable,'diRelayWarningEntry':diRelayWarningEntry,'relayWarningDiInputChanged':relayWarningDiInputChanged,'relayWarningDiInputChangedStatus':relayWarningDiInputChangedStatus,'trafficPrioritization':trafficPrioritization,'qosClassification':qosClassification,'queuingMechanism':queuingMechanism,'qosPortTable':qosPortTable,'qosPortEntry':qosPortEntry,'inspectTos':inspectTos,'inspectCos':inspectCos,'portPriority':portPriority,'cosMapping':cosMapping,'cosMappingTable':cosMappingTable,'cosMappingEntry':cosMappingEntry,'cosTag':cosTag,'cosMappedPriority':cosMappedPriority,'tosMapping':tosMapping,'tosMappingTable':tosMappingTable,'tosMappingEntry':tosMappingEntry,'tosClass':tosClass,'tosMappedPriority':tosMappedPriority,'vlan':vlan,'vlanPortSettingTable':vlanPortSettingTable,'vlanPortSettingEntry':vlanPortSettingEntry,'portVlanType':portVlanType,'portDefaultVid':portDefaultVid,'portFixedVid':portFixedVid,'portForbiddenVid':portForbiddenVid,'portFixedVidUntag':portFixedVidUntag,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_A3:vlanId,'joinedAccessPorts':joinedAccessPorts,'joinedTrunkPorts':joinedTrunkPorts,'joinedHybridPorts':joinedHybridPorts,'managementVlanId':managementVlanId,'vlanType':vlanType,'enableGvrp':enableGvrp,'qinqSettingTable':qinqSettingTable,'qinqSettingEntry':qinqSettingEntry,'qinqEnable':qinqEnable,'qinqTpid':qinqTpid,'multicastFiltering':multicastFiltering,'igmpSnooping':igmpSnooping,'querierQueryInterval':querierQueryInterval,'igmpSnoopingSettingTable':igmpSnoopingSettingTable,'igmpSnoopingSettingEntry':igmpSnoopingSettingEntry,'enableIgmpSnooping':enableIgmpSnooping,'enableQuerier':enableQuerier,'fixedMulticastQuerierPorts':fixedMulticastQuerierPorts,'learnedMulticastQuerierPorts':learnedMulticastQuerierPorts,'enableGlobalIgmpSnooping':enableGlobalIgmpSnooping,'igmpSnoopingStreamTable':igmpSnoopingStreamTable,'igmpSnoopingStreamEntry':igmpSnoopingStreamEntry,_AM:igmpSnoopingStreamIndex,'igmpSnoopingStreamGroup':igmpSnoopingStreamGroup,'igmpSnoopingStreamSource':igmpSnoopingStreamSource,'igmpSnoopingStreamPort':igmpSnoopingStreamPort,'igmpSnoopingMemberPorts':igmpSnoopingMemberPorts,'multicastFastForwarding':multicastFastForwarding,'staticMulticast':staticMulticast,'staticMulticastTable':staticMulticastTable,'staticMulticastEntry':staticMulticastEntry,_AN:staticMulticastAddress,'staticMulticastPorts':staticMulticastPorts,'staticMulticastStatus':staticMulticastStatus,'gmrp':gmrp,'gmrpSettingTable':gmrpSettingTable,'gmrpSettingEntry':gmrpSettingEntry,'enableGMRP':enableGMRP,'gmrpTable':gmrpTable,'gmrpEntry':gmrpEntry,_AO:gmrpMulticastGroup,'gmrpFixedPorts':gmrpFixedPorts,'gmrpLearnedPorts':gmrpLearnedPorts,'mfb':mfb,'mfbSettingTable':mfbSettingTable,'mfbSettingEntry':mfbSettingEntry,'filterBehavior':filterBehavior,'rateLimiting':rateLimiting,'normalModeRateLimitingIngressTable':normalModeRateLimitingIngressTable,'normalModeRateLimitingIngressEntry':normalModeRateLimitingIngressEntry,'limitMode':limitMode,'ingressLimitRate':ingressLimitRate,'egressLimit':egressLimit,'broadcastStormProtection':broadcastStormProtection,'unicastFilterBehavior':unicastFilterBehavior,'ufbIncludeUnkonwnUcast':ufbIncludeUnkonwnUcast,'portDisableMode':portDisableMode,'portDisableModePeriod':portDisableModePeriod,'portDisableModeTable':portDisableModeTable,'portDisableModeEntry':portDisableModeEntry,'ingressLimit':ingressLimit,'rateLimitingMode':rateLimitingMode,'security':security,'userLoginSetting':userLoginSetting,'userLoginServer':userLoginServer,'tacacsServerSetting':tacacsServerSetting,'tacacsLoginAuthServer':tacacsLoginAuthServer,'tacacsLoginAuthPort':tacacsLoginAuthPort,'tacacsLoginAuthSharedKey':tacacsLoginAuthSharedKey,'tacacsLoginAuthAuthType':tacacsLoginAuthAuthType,'tacacsLoginAuthTimeout':tacacsLoginAuthTimeout,'radiusServerSetting':radiusServerSetting,'radiusLoginAuthServer':radiusLoginAuthServer,'radiusLoginAuthPort':radiusLoginAuthPort,'radiusLoginAuthSharedKey':radiusLoginAuthSharedKey,'radiusLoginAuthAuthType':radiusLoginAuthAuthType,'radiusLoginAuthTimeout':radiusLoginAuthTimeout,'portAccessControl':portAccessControl,'staticPortLock':staticPortLock,'staticPortLockAddress':staticPortLockAddress,'staticPortLockPort':staticPortLockPort,'staticPortLockStatus':staticPortLockStatus,'dot1x':dot1x,'dataBaseOption':dataBaseOption,'dot1xReauthEnable':dot1xReauthEnable,'dot1xReauthPeriod':dot1xReauthPeriod,'dot1xSettingTable':dot1xSettingTable,'dot1xSettingEntry':dot1xSettingEntry,'enableDot1X':enableDot1X,'dot1xReauthTable':dot1xReauthTable,'dot1xReauthEntry':dot1xReauthEntry,_AQ:dot1xReauthPortIndex,'dot1xReauth':dot1xReauth,'dot1xRadius':dot1xRadius,'dot1xSameAsAuthServer':dot1xSameAsAuthServer,'dot1x1stRadiusServer':dot1x1stRadiusServer,'dot1x1stRadiusPort':dot1x1stRadiusPort,'dot1x1stRadiusSharedKey':dot1x1stRadiusSharedKey,'dot1x2ndRadiusServer':dot1x2ndRadiusServer,'dot1x2ndRadiusPort':dot1x2ndRadiusPort,'dot1x2ndRadiusSharedKey':dot1x2ndRadiusSharedKey,'portAccessControlTable':portAccessControlTable,'portAccessControlEntry':portAccessControlEntry,_AR:portAccessControlAddress,'portAccessControlPortNo':portAccessControlPortNo,'portAccessControlAccessStatus':portAccessControlAccessStatus,'portAccessControlStatus':portAccessControlStatus,'accessibleIP':accessibleIP,'enableAccessibleIP':enableAccessibleIP,'accessibleIpTable':accessibleIpTable,'accessibleIpEntry':accessibleIpEntry,_AS:accessibleIpAddress,'accessibleIpNetMask':accessibleIpNetMask,'accessibleIpStatus':accessibleIpStatus,'sysFileUpdate':sysFileUpdate,'tftpServer':tftpServer,'firmwarePathName':firmwarePathName,'logPathName':logPathName,'confPathName':confPathName,'tftpUpdate':tftpUpdate,'timeSetting':timeSetting,'sysDateTime':sysDateTime,'calibratePeriod':calibratePeriod,'timeServer1':timeServer1,'timeServer2':timeServer2,'daylightSaving':daylightSaving,'startMonth':startMonth,'startWeek':startWeek,'startDay':startDay,'startHour':startHour,'endMonth':endMonth,'endWeek':endWeek,'endDay':endDay,'endHour':endHour,'offsetHours':offsetHours,'enableNTPServer':enableNTPServer,'timeProtocolOption':timeProtocolOption,'backupMediaSetting':backupMediaSetting,'backupMediaAutoLoad':backupMediaAutoLoad,'enableWarmStart':enableWarmStart,'syslogSetting':syslogSetting,'syslogServer1':syslogServer1,'syslogServer1port':syslogServer1port,'syslogServer2':syslogServer2,'syslogServer2port':syslogServer2port,'syslogServer3':syslogServer3,'syslogServer3port':syslogServer3port,'dhcpRelayAgentSetting':dhcpRelayAgentSetting,'dhcpServer1':dhcpServer1,'dhcpServer2':dhcpServer2,'dhcpServer3':dhcpServer3,'dhcpServer4':dhcpServer4,'option82Setting':option82Setting,'enableOption82':enableOption82,'option82Type':option82Type,'option82Value':option82Value,'option82ValueDisplay':option82ValueDisplay,'dhcpFunctionTable':dhcpFunctionTable,'dhcpFunctionEntry':dhcpFunctionEntry,_AT:dhcpPortIndex,'circuitID':circuitID,'option82Enable':option82Enable,'ieee1588Setting':ieee1588Setting,'ptpv1Setting':ptpv1Setting,'enablePtpv1':enablePtpv1,'clockModev1':clockModev1,'syncIntervalv1':syncIntervalv1,'subDomainNamev1':subDomainNamev1,'preferMasterv1':preferMasterv1,'ptpv2Setting':ptpv2Setting,'enablePtp':enablePtp,'clockMode':clockMode,'transport':transport,'syncInterval':syncInterval,'logMinDelayReqInterval':logMinDelayReqInterval,'logMinPdelayReqInterval':logMinPdelayReqInterval,'logAnnounceInterval':logAnnounceInterval,'announceReceiptTimeout':announceReceiptTimeout,_i:priority1,_j:priority2,'clockClass':clockClass,'domainNumber':domainNumber,'localUtcOffset':localUtcOffset,'localUtcOffsetValid':localUtcOffsetValid,'localLeap59':localLeap59,'localLeap61':localLeap61,'localPtpTimescale':localPtpTimescale,'localArbTime':localArbTime,'ptpv1Status':ptpv1Status,'offsetToMasterv1':offsetToMasterv1,'meanPathDelayv1':meanPathDelayv1,'grandMasterUuidv1':grandMasterUuidv1,'parentUuidv1':parentUuidv1,'clockStratumv1':clockStratumv1,'clockIdentifierv1':clockIdentifierv1,'ptpv2Status':ptpv2Status,'offsetToMaster':offsetToMaster,'meanPathDelay':meanPathDelay,'parentIdentity':parentIdentity,'grandmasterIdentity':grandmasterIdentity,'grandmasterClockClass':grandmasterClockClass,'grandmasterClockAccuracy':grandmasterClockAccuracy,'grandmasterPriority1':grandmasterPriority1,'grandmasterPriority2':grandmasterPriority2,'stepsRemoved':stepsRemoved,'currentUtcOffset':currentUtcOffset,'currentUtcOffsetValid':currentUtcOffsetValid,'leap59':leap59,'leap61':leap61,'ptpTimescale':ptpTimescale,'timesource':timesource,'ptpPortTable':ptpPortTable,'ptpPortEntry':ptpPortEntry,_AW:ptpPortIndex,'ptpPortEnable':ptpPortEnable,'ptpPortStatus':ptpPortStatus,'diagnosis':diagnosis,'lldpSetting':lldpSetting,'enableLLDP':enableLLDP,'lldpMSGInterval':lldpMSGInterval,'webTimeout':webTimeout,'ageTime':ageTime,'garpSetting':garpSetting,'joinTime':joinTime,'leaveTime':leaveTime,'leaveAllTime':leaveAllTime,'eventlog':eventlog,'eventlogTable':eventlogTable,'eventlogEntry':eventlogEntry,_AX:eventlogIndex,'eventlogBootup':eventlogBootup,'eventlogDate':eventlogDate,'eventlogTime':eventlogTime,'eventlogUptime':eventlogUptime,'eventlogEvent':eventlogEvent,'eventlogClear':eventlogClear,'industrialProtocol':industrialProtocol,'eipSetting':eipSetting,'enableEtherNetIP':enableEtherNetIP,'modbusTCPSetting':modbusTCPSetting,'enableModbusTCP':enableModbusTCP,'profinetioSetting':profinetioSetting,'enableProfinetIO':enableProfinetIO,'enableFactoryDefault':enableFactoryDefault,'enableJumboFrame':enableJumboFrame,'maxJumboFrame':maxJumboFrame,'consoleLoginMode':consoleLoginMode,'accessControlList':accessControlList,'accessControlTable':accessControlTable,'accessControlEntry':accessControlEntry,_AY:aclRuleIndex,'listID':listID,'filterType':filterType,'actionFlag':actionFlag,'srcMacAddr':srcMacAddr,'srcMacMask':srcMacMask,'dstMacAddr':dstMacAddr,'dstMacMask':dstMacMask,'etherType':etherType,'vlanID':vlanID,'srcIpAddr':srcIpAddr,'srcNetmask':srcNetmask,'dstIpAddr':dstIpAddr,'dstNetmask':dstNetmask,'protocolCode':protocolCode,'srcsocketPort':srcsocketPort,'dstsocketPort':dstsocketPort,'aclStatus':aclStatus,'ipDSCP':ipDSCP,'overrideDSCP':overrideDSCP,'aclAttachmentTable':aclAttachmentTable,'aclAttachmentEntry':aclAttachmentEntry,'aclID':aclID,'ingressPort':ingressPort,'egressPort':egressPort,'aclListName':aclListName,'cpuLoading5s':cpuLoading5s,'cpuLoading30s':cpuLoading30s,'cpuLoading300s':cpuLoading300s,'totalMemory':totalMemory,'freeMemory':freeMemory,'usedMemory':usedMemory,'memoryUsage':memoryUsage,'loopProtection':loopProtection,'eventSettings':eventSettings,'systemEventSettingsTable':systemEventSettingsTable,'systemEventSettingsEntry':systemEventSettingsEntry,_AZ:systemEventIndex,'systemEventActive':systemEventActive,'systemEventName':systemEventName,'systemEventSupport':systemEventSupport,'systemEventModuleEnable':systemEventModuleEnable,'systemEventSeverity':systemEventSeverity,'portEventSettingsTable':portEventSettingsTable,'portEventSettingsEntry':portEventSettingsEntry,_B3:portEventIndex,'portEventLabel':portEventLabel,'portEventActive':portEventActive,'portEventEnable':portEventEnable,'portEventTrafficThreshold':portEventTrafficThreshold,'portEventTrafficDuration':portEventTrafficDuration,'portEventModuleEnable':portEventModuleEnable,'portEventSeverity':portEventSeverity,'switchLocator':switchLocator,'blinkingLocatorLED':blinkingLocatorLED,'disableLocatorLEDTime':disableLocatorLEDTime,'swTraps':swTraps,_BE:varconfigChangeTrap,_BF:varpower1Trap,_BG:varpower2Trap,_BH:vartrafficOverloadTrap,_BI:varredundancyTopologyChangedTrap,_BJ:varturboRingCouplingPortChangedTrap,_A7:varturboRingMasterChangedTrap,_BK:varPortLoopDetectedTrap,_BL:varRateLimitedOnTrap,_BM:varLLDPChgTrap,_BN:varABC02WarningTrap,'varturboRingMasterMismatchTrap':varturboRingMasterMismatchTrap,'l3Mgmt':l3Mgmt,'ipIfSetting':ipIfSetting,'ipIfSettingTable':ipIfSettingTable,'ipIfSettingEntry':ipIfSettingEntry,_n:ipIfIndex,'ipIfName':ipIfName,'ipIfAddr':ipIfAddr,'ipIfNetmask':ipIfNetmask,'ipIfVlan':ipIfVlan,'ipIfProxyArp':ipIfProxyArp,'ipIfStatus':ipIfStatus,'staticRoute':staticRoute,'staticRouteTable':staticRouteTable,'staticRouteEntry':staticRouteEntry,_B4:staticRouteIndex,'staticRouteAddr':staticRouteAddr,'staticRouteNetmask':staticRouteNetmask,'staticRouteNexthop':staticRouteNexthop,'staticRouteMetric':staticRouteMetric,'staticRouteStatus':staticRouteStatus,'rip':rip,'ripEnable':ripEnable,'ripVersion':ripVersion,'ripRedistConnected':ripRedistConnected,'ripRedistStatic':ripRedistStatic,'ripRedistOspf':ripRedistOspf,'ripInterfaceTable':ripInterfaceTable,'ripInterfaceEntry':ripInterfaceEntry,'ripIfName':ripIfName,'ripIfAddr':ripIfAddr,'ripIfVlan':ripIfVlan,'ripIfEnable':ripIfEnable,'ospf':ospf,'ospfGlobal':ospfGlobal,'ospfEnable':ospfEnable,'ospfRouterId':ospfRouterId,'ospfCurrentRouterId':ospfCurrentRouterId,'ospfRedistConnected':ospfRedistConnected,'ospfRedistStatic':ospfRedistStatic,'ospfRedistRip':ospfRedistRip,'ospfArea':ospfArea,'ospfAreaTable':ospfAreaTable,'ospfAreaEntry':ospfAreaEntry,_B5:ospfAreaId,'ospfAreaType':ospfAreaType,'ospfAreaMetric':ospfAreaMetric,'ospfAreaStatus':ospfAreaStatus,'ospfInterface':ospfInterface,'ospfInterfaceTable':ospfInterfaceTable,'ospfInterfaceEntry':ospfInterfaceEntry,_B6:ospfIfIndex,'ospfIfName':ospfIfName,'ospfIfAddr':ospfIfAddr,'ospfIfAreaId':ospfIfAreaId,'ospfIfState':ospfIfState,'ospfIfPriority':ospfIfPriority,'ospfIfHelloInterval':ospfIfHelloInterval,'ospfIfDeadInterval':ospfIfDeadInterval,'ospfIfAuthType':ospfIfAuthType,'ospfIfAuthKey':ospfIfAuthKey,'ospfIfMd5KeyId':ospfIfMd5KeyId,'ospfIfMetric':ospfIfMetric,'ospfIfStatus':ospfIfStatus,'ospfVirtualLink':ospfVirtualLink,'ospfVlinkTable':ospfVlinkTable,'ospfVlinkEntry':ospfVlinkEntry,_B7:ospfVlinkIndex,'ospfTransitAreaId':ospfTransitAreaId,'ospfNeighborAreaId':ospfNeighborAreaId,'ospfVlinkStatus':ospfVlinkStatus,'ospfAggregation':ospfAggregation,'ospfAggregationTable':ospfAggregationTable,'ospfAggregationEntry':ospfAggregationEntry,_B8:ospfAggrIndex,'ospfAggrAreaId':ospfAggrAreaId,'ospfAggrAddr':ospfAggrAddr,'ospfAggrMask':ospfAggrMask,'ospfAggrStatus':ospfAggrStatus,'ipRoutingTable':ipRoutingTable,'ipRoutingEntry':ipRoutingEntry,_B9:ipRoutingIndex,'ipRoutingType':ipRoutingType,'ipRoutingDest':ipRoutingDest,'ipRoutingNextHop':ipRoutingNextHop,'ipRoutingIfName':ipRoutingIfName,'ipRoutingMetric':ipRoutingMetric,'ipRoutingVlan':ipRoutingVlan,'vrrp':vrrp,'vrrpInterfaceTable':vrrpInterfaceTable,'vrrpInterfaceEntry':vrrpInterfaceEntry,'vrrpIfName':vrrpIfName,'vrrpIfAddr':vrrpIfAddr,'vrrpIfVlan':vrrpIfVlan,'vrrpIfEnable':vrrpIfEnable,'vrrpIfVirtualIp':vrrpIfVirtualIp,'vrrpIfRouterId':vrrpIfRouterId,'vrrpIfPriority':vrrpIfPriority,'vrrpIfPreemptionMode':vrrpIfPreemptionMode,'vrrpIfStatus':vrrpIfStatus,'vrrpEnable':vrrpEnable,'vrrpAdverInt':vrrpAdverInt,'dvmrp':dvmrp,'dvmrpEnable':dvmrpEnable,'dvmrpInterfaceTable':dvmrpInterfaceTable,'dvmrpInterfaceEntry':dvmrpInterfaceEntry,_BA:dvmrpIfIndex,'dvmrpIfName':dvmrpIfName,'dvmrpIfAddr':dvmrpIfAddr,'dvmrpIfVlan':dvmrpIfVlan,'dvmrpIfEnable':dvmrpIfEnable,'dvmrpMulticastRoutingTable':dvmrpMulticastRoutingTable,'dvmrpMulticastRoutingEntry':dvmrpMulticastRoutingEntry,_BB:dvmrpMRIndex,'dvmrpMRGroup':dvmrpMRGroup,'dvmrpMRSource':dvmrpMRSource,'dvmrpMRUpstream':dvmrpMRUpstream,'dvmrpMRIncomingIfname':dvmrpMRIncomingIfname,'dvmrpMRVid':dvmrpMRVid,'dvmrpMRExpiretime':dvmrpMRExpiretime,'dvmrpMRLefttime':dvmrpMRLefttime,'dvmrpMRDowntreamVid':dvmrpMRDowntreamVid,'pimdm':pimdm,'pimdmEnable':pimdmEnable,'pimdmInterfaceTable':pimdmInterfaceTable,'pimdmInterfaceEntry':pimdmInterfaceEntry,_BC:pimdmIfIndex,'pimdmIfName':pimdmIfName,'pimdmIfAddr':pimdmIfAddr,'pimdmIfVlan':pimdmIfVlan,'pimdmIfEnable':pimdmIfEnable,'pimdmMulticastRoutingTable':pimdmMulticastRoutingTable,'pimdmMulticastRoutingEntry':pimdmMulticastRoutingEntry,_BD:pimdmMRIndex,'pimdmMRGroup':pimdmMRGroup,'pimdmMRSource':pimdmMRSource,'pimdmMRUpstream':pimdmMRUpstream,'pimdmMRIncomingIfname':pimdmMRIncomingIfname,'pimdmMRVid':pimdmMRVid,'pimdmMRLefttime':pimdmMRLefttime,'pimdmMRDowntreamVid':pimdmMRDowntreamVid})