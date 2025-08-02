_AL='varLLDPChgTrap'
_AK='varturboRingMasterChangedTrap'
_AJ='varturboRingCouplingPortChangedTrap'
_AI='varredundancyTopologyChangedTrap'
_AH='vartrafficOverloadTrap'
_AG='varpower2Trap'
_AF='varpower1Trap'
_AE='varconfigChangeTrap'
_AD='eventlogIndex'
_AC='dhcpPortIndex'
_AB='accessibleIpAddress'
_AA='notlimited'
_A9='gmrpMulticastGroup'
_A8='createAndWait'
_A7='createAndGo'
_A6='staticMulticastAddress'
_A5='portbaseVlanSettingIndex'
_A4='notTurboChainPort'
_A3='spanningTreeIndex'
_A2='turboRingPortIndex'
_A1='setDevIpIndex'
_A0='not-present'
_z='speed10M-Half'
_y='speed10M-Full'
_x='speed100M-Half'
_w='speed100M-Full'
_v='limit16M'
_u='vlanId'
_t='off2on'
_s='on2off'
_r='relayAlarmIndex'
_q='priority0'
_p='broken'
_o='active'
_n='turboChain'
_m='turboRingV2'
_l='turboRing'
_k='spanningTree'
_j='auto'
_i='limit8M'
_h='limit4M'
_g='limit2M'
_f='limit1M'
_e='limit512k'
_d='limit256k'
_c='limit128k'
_b='notlimit'
_a='portDisabled'
_Z='triggered'
_Y='not-triggered'
_X='on'
_W='off'
_V='linkdown'
_U='notRedundant'
_T='disabled'
_S='normal'
_R='blocked'
_Q='linkDown'
_P='read-create'
_O='none'
_N='blocking'
_M='learning'
_L='portIndex'
_K='yes'
_J='forwarding'
_I='no'
_H='na'
_G='MOXA-EDS405A-MIB'
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
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
eds405a=ModuleIdentity((1,3,6,1,4,1,8691,7,6))
if mibBuilder.loadTexts:eds405a.setRevisions(('2016-11-02 00:00','2016-02-19 00:00','2012-10-05 00:00','2012-07-22 00:00'))
class PortList(TextualConvention,OctetString):status=_A
_Moxa_ObjectIdentity=ObjectIdentity
moxa=_Moxa_ObjectIdentity((1,3,6,1,4,1,8691))
_IndustrialEthernet_ObjectIdentity=ObjectIdentity
industrialEthernet=_IndustrialEthernet_ObjectIdentity((1,3,6,1,4,1,8691,7))
_MibNotificationsPrefix_ObjectIdentity=ObjectIdentity
mibNotificationsPrefix=_MibNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,8691,7,6,0))
_SwMgmt_ObjectIdentity=ObjectIdentity
swMgmt=_SwMgmt_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1))
_NumberOfPorts_Type=Integer32
_NumberOfPorts_Object=MibScalar
numberOfPorts=_NumberOfPorts_Object((1,3,6,1,4,1,8691,7,6,1,1),_NumberOfPorts_Type())
numberOfPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:numberOfPorts.setStatus(_A)
_SwitchModel_Type=DisplayString
_SwitchModel_Object=MibScalar
switchModel=_SwitchModel_Object((1,3,6,1,4,1,8691,7,6,1,2),_SwitchModel_Type())
switchModel.setMaxAccess(_D)
if mibBuilder.loadTexts:switchModel.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,8691,7,6,1,4),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
class _EnableWebConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableWebConfig_Type.__name__=_C
_EnableWebConfig_Object=MibScalar
enableWebConfig=_EnableWebConfig_Object((1,3,6,1,4,1,8691,7,6,1,5),_EnableWebConfig_Type())
enableWebConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:enableWebConfig.setStatus(_A)
class _EnableTelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableTelnetConsole_Type.__name__=_C
_EnableTelnetConsole_Object=MibScalar
enableTelnetConsole=_EnableTelnetConsole_Object((1,3,6,1,4,1,8691,7,6,1,6),_EnableTelnetConsole_Type())
enableTelnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:enableTelnetConsole.setStatus(_A)
class _LineSwapRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LineSwapRecovery_Type.__name__=_C
_LineSwapRecovery_Object=MibScalar
lineSwapRecovery=_LineSwapRecovery_Object((1,3,6,1,4,1,8691,7,6,1,7),_LineSwapRecovery_Type())
lineSwapRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:lineSwapRecovery.setStatus(_A)
_NetworkSetting_ObjectIdentity=ObjectIdentity
networkSetting=_NetworkSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,8))
_SwitchIpAddr_Type=IpAddress
_SwitchIpAddr_Object=MibScalar
switchIpAddr=_SwitchIpAddr_Object((1,3,6,1,4,1,8691,7,6,1,8,1),_SwitchIpAddr_Type())
switchIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:switchIpAddr.setStatus(_A)
_SwitchIpMask_Type=IpAddress
_SwitchIpMask_Object=MibScalar
switchIpMask=_SwitchIpMask_Object((1,3,6,1,4,1,8691,7,6,1,8,2),_SwitchIpMask_Type())
switchIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:switchIpMask.setStatus(_A)
_DefaultGateway_Type=IpAddress
_DefaultGateway_Object=MibScalar
defaultGateway=_DefaultGateway_Object((1,3,6,1,4,1,8691,7,6,1,8,3),_DefaultGateway_Type())
defaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultGateway.setStatus(_A)
class _EnableAutoIpConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('enableDHCP',1),('enableBOOTP',2)))
_EnableAutoIpConfig_Type.__name__=_C
_EnableAutoIpConfig_Object=MibScalar
enableAutoIpConfig=_EnableAutoIpConfig_Object((1,3,6,1,4,1,8691,7,6,1,8,4),_EnableAutoIpConfig_Type())
enableAutoIpConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAutoIpConfig.setStatus(_A)
_DnsServer1IpAddr_Type=IpAddress
_DnsServer1IpAddr_Object=MibScalar
dnsServer1IpAddr=_DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,7,6,1,8,5),_DnsServer1IpAddr_Type())
dnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer1IpAddr.setStatus(_A)
_SnmpTrapCommunity_Type=DisplayString
_SnmpTrapCommunity_Object=MibScalar
snmpTrapCommunity=_SnmpTrapCommunity_Object((1,3,6,1,4,1,8691,7,6,1,8,6),_SnmpTrapCommunity_Type())
snmpTrapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapCommunity.setStatus(_A)
_TrapServerAddr_Type=DisplayString
_TrapServerAddr_Object=MibScalar
trapServerAddr=_TrapServerAddr_Object((1,3,6,1,4,1,8691,7,6,1,8,7),_TrapServerAddr_Type())
trapServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerAddr.setStatus(_A)
_DnsServer2IpAddr_Type=IpAddress
_DnsServer2IpAddr_Object=MibScalar
dnsServer2IpAddr=_DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,7,6,1,8,8),_DnsServer2IpAddr_Type())
dnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer2IpAddr.setStatus(_A)
_SnmpReadCommunity_Type=DisplayString
_SnmpReadCommunity_Object=MibScalar
snmpReadCommunity=_SnmpReadCommunity_Object((1,3,6,1,4,1,8691,7,6,1,8,9),_SnmpReadCommunity_Type())
snmpReadCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpReadCommunity.setStatus(_A)
_SnmpTrap2Community_Type=DisplayString
_SnmpTrap2Community_Object=MibScalar
snmpTrap2Community=_SnmpTrap2Community_Object((1,3,6,1,4,1,8691,7,6,1,8,11),_SnmpTrap2Community_Type())
snmpTrap2Community.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrap2Community.setStatus(_A)
_Trap2ServerAddr_Type=DisplayString
_Trap2ServerAddr_Object=MibScalar
trap2ServerAddr=_Trap2ServerAddr_Object((1,3,6,1,4,1,8691,7,6,1,8,12),_Trap2ServerAddr_Type())
trap2ServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trap2ServerAddr.setStatus(_A)
class _SnmpInformEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnmpInformEnable_Type.__name__=_C
_SnmpInformEnable_Object=MibScalar
snmpInformEnable=_SnmpInformEnable_Object((1,3,6,1,4,1,8691,7,6,1,8,13),_SnmpInformEnable_Type())
snmpInformEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInformEnable.setStatus(_A)
class _SnmpInformRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_SnmpInformRetries_Type.__name__=_C
_SnmpInformRetries_Object=MibScalar
snmpInformRetries=_SnmpInformRetries_Object((1,3,6,1,4,1,8691,7,6,1,8,14),_SnmpInformRetries_Type())
snmpInformRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInformRetries.setStatus(_A)
class _SnmpInformTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_SnmpInformTimeout_Type.__name__=_C
_SnmpInformTimeout_Object=MibScalar
snmpInformTimeout=_SnmpInformTimeout_Object((1,3,6,1,4,1,8691,7,6,1,8,15),_SnmpInformTimeout_Type())
snmpInformTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInformTimeout.setStatus(_A)
_DhcpRetryPeriods_Type=Integer32
_DhcpRetryPeriods_Object=MibScalar
dhcpRetryPeriods=_DhcpRetryPeriods_Object((1,3,6,1,4,1,8691,7,6,1,8,16),_DhcpRetryPeriods_Type())
dhcpRetryPeriods.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRetryPeriods.setStatus(_A)
_DhcpRetryTimes_Type=Integer32
_DhcpRetryTimes_Object=MibScalar
dhcpRetryTimes=_DhcpRetryTimes_Object((1,3,6,1,4,1,8691,7,6,1,8,17),_DhcpRetryTimes_Type())
dhcpRetryTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRetryTimes.setStatus(_A)
_PortSetting_ObjectIdentity=ObjectIdentity
portSetting=_PortSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,9))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,8691,7,6,1,9,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1))
portEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
_PortDesc_Type=DisplayString
_PortDesc_Object=MibTableColumn
portDesc=_PortDesc_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,2),_PortDesc_Type())
portDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:portDesc.setStatus(_A)
class _PortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortEnable_Type.__name__=_C
_PortEnable_Object=MibTableColumn
portEnable=_PortEnable_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,3),_PortEnable_Type())
portEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portEnable.setStatus(_A)
class _PortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_j,0),(_w,1),(_x,2),(_y,3),(_z,4)))
_PortSpeed_Type.__name__=_C
_PortSpeed_Object=MibTableColumn
portSpeed=_PortSpeed_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,4),_PortSpeed_Type())
portSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:portSpeed.setStatus(_A)
class _PortMDI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_j,1),('mdi',2),('mdiX',3)))
_PortMDI_Type.__name__=_C
_PortMDI_Object=MibTableColumn
portMDI=_PortMDI_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,5),_PortMDI_Type())
portMDI.setMaxAccess(_B)
if mibBuilder.loadTexts:portMDI.setStatus(_A)
class _PortFDXFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortFDXFlowCtrl_Type.__name__=_C
_PortFDXFlowCtrl_Object=MibTableColumn
portFDXFlowCtrl=_PortFDXFlowCtrl_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,6),_PortFDXFlowCtrl_Type())
portFDXFlowCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFDXFlowCtrl.setStatus(_A)
_PortName_Type=DisplayString
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,7),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
_PortSubdesc_Type=DisplayString
_PortSubdesc_Object=MibTableColumn
portSubdesc=_PortSubdesc_Object((1,3,6,1,4,1,8691,7,6,1,9,1,1,8),_PortSubdesc_Type())
portSubdesc.setMaxAccess(_D)
if mibBuilder.loadTexts:portSubdesc.setStatus(_A)
_Monitor_ObjectIdentity=ObjectIdentity
monitor=_Monitor_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,10))
class _Power1InputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_A0,0),('present',1)))
_Power1InputStatus_Type.__name__=_C
_Power1InputStatus_Object=MibScalar
power1InputStatus=_Power1InputStatus_Object((1,3,6,1,4,1,8691,7,6,1,10,1),_Power1InputStatus_Type())
power1InputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power1InputStatus.setStatus(_A)
class _Power2InputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_A0,0),('present',1)))
_Power2InputStatus_Type.__name__=_C
_Power2InputStatus_Object=MibScalar
power2InputStatus=_Power2InputStatus_Object((1,3,6,1,4,1,8691,7,6,1,10,2),_Power2InputStatus_Type())
power2InputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power2InputStatus.setStatus(_A)
_MonitorPortTable_Object=MibTable
monitorPortTable=_MonitorPortTable_Object((1,3,6,1,4,1,8691,7,6,1,10,3))
if mibBuilder.loadTexts:monitorPortTable.setStatus(_A)
_MonitorPortEntry_Object=MibTableRow
monitorPortEntry=_MonitorPortEntry_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1))
monitorPortEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:monitorPortEntry.setStatus(_A)
class _MonitorLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_E,-1),(_W,0),(_X,1)))
_MonitorLinkStatus_Type.__name__=_C
_MonitorLinkStatus_Object=MibTableColumn
monitorLinkStatus=_MonitorLinkStatus_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,2),_MonitorLinkStatus_Type())
monitorLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorLinkStatus.setStatus(_A)
class _MonitorSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3)));namedValues=NamedValues(*((_H,-1),(_z,0),(_y,1),(_x,2),(_w,3)))
_MonitorSpeed_Type.__name__=_C
_MonitorSpeed_Object=MibTableColumn
monitorSpeed=_MonitorSpeed_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,3),_MonitorSpeed_Type())
monitorSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSpeed.setStatus(_A)
class _MonitorAutoMDI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_H,-1),('mdi',0),('mdiX',1)))
_MonitorAutoMDI_Type.__name__=_C
_MonitorAutoMDI_Object=MibTableColumn
monitorAutoMDI=_MonitorAutoMDI_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,4),_MonitorAutoMDI_Type())
monitorAutoMDI.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorAutoMDI.setStatus(_A)
_MonitorTraffic_Type=Integer32
_MonitorTraffic_Object=MibTableColumn
monitorTraffic=_MonitorTraffic_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,5),_MonitorTraffic_Type())
monitorTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTraffic.setStatus(_A)
class _MonitorFDXFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_MonitorFDXFlowCtrl_Type.__name__=_C
_MonitorFDXFlowCtrl_Object=MibTableColumn
monitorFDXFlowCtrl=_MonitorFDXFlowCtrl_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,6),_MonitorFDXFlowCtrl_Type())
monitorFDXFlowCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFDXFlowCtrl.setStatus(_A)
_MonitorTxTraffic_Type=Integer32
_MonitorTxTraffic_Object=MibTableColumn
monitorTxTraffic=_MonitorTxTraffic_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,7),_MonitorTxTraffic_Type())
monitorTxTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTxTraffic.setStatus(_A)
_MonitorRxTraffic_Type=Integer32
_MonitorRxTraffic_Object=MibTableColumn
monitorRxTraffic=_MonitorRxTraffic_Object((1,3,6,1,4,1,8691,7,6,1,10,3,1,8),_MonitorRxTraffic_Type())
monitorRxTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRxTraffic.setStatus(_A)
_EmailWarning_ObjectIdentity=ObjectIdentity
emailWarning=_EmailWarning_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,11))
_EmailService_ObjectIdentity=ObjectIdentity
emailService=_EmailService_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,11,1))
_EmailWarningMailServer_Type=DisplayString
_EmailWarningMailServer_Object=MibScalar
emailWarningMailServer=_EmailWarningMailServer_Object((1,3,6,1,4,1,8691,7,6,1,11,1,1),_EmailWarningMailServer_Type())
emailWarningMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningMailServer.setStatus(_A)
_EmailWarningFirstEmailAddr_Type=DisplayString
_EmailWarningFirstEmailAddr_Object=MibScalar
emailWarningFirstEmailAddr=_EmailWarningFirstEmailAddr_Object((1,3,6,1,4,1,8691,7,6,1,11,1,2),_EmailWarningFirstEmailAddr_Type())
emailWarningFirstEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFirstEmailAddr.setStatus(_A)
_EmailWarningSecondEmailAddr_Type=DisplayString
_EmailWarningSecondEmailAddr_Object=MibScalar
emailWarningSecondEmailAddr=_EmailWarningSecondEmailAddr_Object((1,3,6,1,4,1,8691,7,6,1,11,1,3),_EmailWarningSecondEmailAddr_Type())
emailWarningSecondEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSecondEmailAddr.setStatus(_A)
_EmailWarningThirdEmailAddr_Type=DisplayString
_EmailWarningThirdEmailAddr_Object=MibScalar
emailWarningThirdEmailAddr=_EmailWarningThirdEmailAddr_Object((1,3,6,1,4,1,8691,7,6,1,11,1,4),_EmailWarningThirdEmailAddr_Type())
emailWarningThirdEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningThirdEmailAddr.setStatus(_A)
_EmailWarningFourthEmailAddr_Type=DisplayString
_EmailWarningFourthEmailAddr_Object=MibScalar
emailWarningFourthEmailAddr=_EmailWarningFourthEmailAddr_Object((1,3,6,1,4,1,8691,7,6,1,11,1,5),_EmailWarningFourthEmailAddr_Type())
emailWarningFourthEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFourthEmailAddr.setStatus(_A)
class _EmailWarningSMTPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_EmailWarningSMTPPort_Type.__name__=_C
_EmailWarningSMTPPort_Object=MibScalar
emailWarningSMTPPort=_EmailWarningSMTPPort_Object((1,3,6,1,4,1,8691,7,6,1,11,1,6),_EmailWarningSMTPPort_Type())
emailWarningSMTPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSMTPPort.setStatus(_A)
_EmailWarningEventType_ObjectIdentity=ObjectIdentity
emailWarningEventType=_EmailWarningEventType_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,11,2))
class _EmailWarningEventServerColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventServerColdStart_Type.__name__=_C
_EmailWarningEventServerColdStart_Object=MibScalar
emailWarningEventServerColdStart=_EmailWarningEventServerColdStart_Object((1,3,6,1,4,1,8691,7,6,1,11,2,1),_EmailWarningEventServerColdStart_Type())
emailWarningEventServerColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventServerColdStart.setStatus(_A)
class _EmailWarningEventServerWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventServerWarmStart_Type.__name__=_C
_EmailWarningEventServerWarmStart_Object=MibScalar
emailWarningEventServerWarmStart=_EmailWarningEventServerWarmStart_Object((1,3,6,1,4,1,8691,7,6,1,11,2,2),_EmailWarningEventServerWarmStart_Type())
emailWarningEventServerWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventServerWarmStart.setStatus(_A)
class _EmailWarningEventConfigChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventConfigChange_Type.__name__=_C
_EmailWarningEventConfigChange_Object=MibScalar
emailWarningEventConfigChange=_EmailWarningEventConfigChange_Object((1,3,6,1,4,1,8691,7,6,1,11,2,3),_EmailWarningEventConfigChange_Type())
emailWarningEventConfigChange.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventConfigChange.setStatus(_A)
class _EmailWarningEventPowerOn2Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPowerOn2Off_Type.__name__=_C
_EmailWarningEventPowerOn2Off_Object=MibScalar
emailWarningEventPowerOn2Off=_EmailWarningEventPowerOn2Off_Object((1,3,6,1,4,1,8691,7,6,1,11,2,4),_EmailWarningEventPowerOn2Off_Type())
emailWarningEventPowerOn2Off.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPowerOn2Off.setStatus(_A)
class _EmailWarningEventPowerOff2On_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPowerOff2On_Type.__name__=_C
_EmailWarningEventPowerOff2On_Object=MibScalar
emailWarningEventPowerOff2On=_EmailWarningEventPowerOff2On_Object((1,3,6,1,4,1,8691,7,6,1,11,2,5),_EmailWarningEventPowerOff2On_Type())
emailWarningEventPowerOff2On.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPowerOff2On.setStatus(_A)
class _EmailWarningEventAuthFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventAuthFail_Type.__name__=_C
_EmailWarningEventAuthFail_Object=MibScalar
emailWarningEventAuthFail=_EmailWarningEventAuthFail_Object((1,3,6,1,4,1,8691,7,6,1,11,2,6),_EmailWarningEventAuthFail_Type())
emailWarningEventAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventAuthFail.setStatus(_A)
class _EmailWarningEventTopologyChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventTopologyChanged_Type.__name__=_C
_EmailWarningEventTopologyChanged_Object=MibScalar
emailWarningEventTopologyChanged=_EmailWarningEventTopologyChanged_Object((1,3,6,1,4,1,8691,7,6,1,11,2,7),_EmailWarningEventTopologyChanged_Type())
emailWarningEventTopologyChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventTopologyChanged.setStatus(_A)
_EmailWarningEventPortTable_Object=MibTable
emailWarningEventPortTable=_EmailWarningEventPortTable_Object((1,3,6,1,4,1,8691,7,6,1,11,3))
if mibBuilder.loadTexts:emailWarningEventPortTable.setStatus(_A)
_EmailWarningEventPortEntry_Object=MibTableRow
emailWarningEventPortEntry=_EmailWarningEventPortEntry_Object((1,3,6,1,4,1,8691,7,6,1,11,3,1))
emailWarningEventPortEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:emailWarningEventPortEntry.setStatus(_A)
class _EmailWarningEventPortLinkOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPortLinkOn_Type.__name__=_C
_EmailWarningEventPortLinkOn_Object=MibTableColumn
emailWarningEventPortLinkOn=_EmailWarningEventPortLinkOn_Object((1,3,6,1,4,1,8691,7,6,1,11,3,1,2),_EmailWarningEventPortLinkOn_Type())
emailWarningEventPortLinkOn.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortLinkOn.setStatus(_A)
class _EmailWarningEventPortLinkOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPortLinkOff_Type.__name__=_C
_EmailWarningEventPortLinkOff_Object=MibTableColumn
emailWarningEventPortLinkOff=_EmailWarningEventPortLinkOff_Object((1,3,6,1,4,1,8691,7,6,1,11,3,1,3),_EmailWarningEventPortLinkOff_Type())
emailWarningEventPortLinkOff.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortLinkOff.setStatus(_A)
class _EmailWarningEventPortTrafficOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPortTrafficOverload_Type.__name__=_C
_EmailWarningEventPortTrafficOverload_Object=MibTableColumn
emailWarningEventPortTrafficOverload=_EmailWarningEventPortTrafficOverload_Object((1,3,6,1,4,1,8691,7,6,1,11,3,1,4),_EmailWarningEventPortTrafficOverload_Type())
emailWarningEventPortTrafficOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortTrafficOverload.setStatus(_A)
_EmailWarningEventPortRxTrafficThreshold_Type=Integer32
_EmailWarningEventPortRxTrafficThreshold_Object=MibTableColumn
emailWarningEventPortRxTrafficThreshold=_EmailWarningEventPortRxTrafficThreshold_Object((1,3,6,1,4,1,8691,7,6,1,11,3,1,5),_EmailWarningEventPortRxTrafficThreshold_Type())
emailWarningEventPortRxTrafficThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortRxTrafficThreshold.setStatus(_A)
_EmailWarningEventPortTrafficDuration_Type=Integer32
_EmailWarningEventPortTrafficDuration_Object=MibTableColumn
emailWarningEventPortTrafficDuration=_EmailWarningEventPortTrafficDuration_Object((1,3,6,1,4,1,8691,7,6,1,11,3,1,6),_EmailWarningEventPortTrafficDuration_Type())
emailWarningEventPortTrafficDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortTrafficDuration.setStatus(_A)
_SetDeviceIp_ObjectIdentity=ObjectIdentity
setDeviceIp=_SetDeviceIp_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,12))
_SetDevIpTable_Object=MibTable
setDevIpTable=_SetDevIpTable_Object((1,3,6,1,4,1,8691,7,6,1,12,1))
if mibBuilder.loadTexts:setDevIpTable.setStatus(_A)
_SetDevIpEntry_Object=MibTableRow
setDevIpEntry=_SetDevIpEntry_Object((1,3,6,1,4,1,8691,7,6,1,12,1,1))
setDevIpEntry.setIndexNames((0,_G,_A1))
if mibBuilder.loadTexts:setDevIpEntry.setStatus(_A)
_SetDevIpIndex_Type=Integer32
_SetDevIpIndex_Object=MibTableColumn
setDevIpIndex=_SetDevIpIndex_Object((1,3,6,1,4,1,8691,7,6,1,12,1,1,1),_SetDevIpIndex_Type())
setDevIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpIndex.setStatus(_A)
_SetDevIpCurrentIpofDevice_Type=DisplayString
_SetDevIpCurrentIpofDevice_Object=MibTableColumn
setDevIpCurrentIpofDevice=_SetDevIpCurrentIpofDevice_Object((1,3,6,1,4,1,8691,7,6,1,12,1,1,2),_SetDevIpCurrentIpofDevice_Type())
setDevIpCurrentIpofDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpCurrentIpofDevice.setStatus(_A)
class _SetDevIpPresentBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_I,0),('dhcpClient',1),('rarp',2),('bootp',4)))
_SetDevIpPresentBy_Type.__name__=_C
_SetDevIpPresentBy_Object=MibTableColumn
setDevIpPresentBy=_SetDevIpPresentBy_Object((1,3,6,1,4,1,8691,7,6,1,12,1,1,3),_SetDevIpPresentBy_Type())
setDevIpPresentBy.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpPresentBy.setStatus(_A)
_SetDevIpDedicatedIp_Type=IpAddress
_SetDevIpDedicatedIp_Object=MibTableColumn
setDevIpDedicatedIp=_SetDevIpDedicatedIp_Object((1,3,6,1,4,1,8691,7,6,1,12,1,1,4),_SetDevIpDedicatedIp_Type())
setDevIpDedicatedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:setDevIpDedicatedIp.setStatus(_A)
_Mirroring_ObjectIdentity=ObjectIdentity
mirroring=_Mirroring_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,13))
_TargetPort_Type=Integer32
_TargetPort_Object=MibScalar
targetPort=_TargetPort_Object((1,3,6,1,4,1,8691,7,6,1,13,1),_TargetPort_Type())
targetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:targetPort.setStatus(_A)
_MirroringPort_Type=Integer32
_MirroringPort_Object=MibScalar
mirroringPort=_MirroringPort_Object((1,3,6,1,4,1,8691,7,6,1,13,2),_MirroringPort_Type())
mirroringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirroringPort.setStatus(_A)
class _MonitorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outputDataStream',1),('biDirectional',2)))
_MonitorDirection_Type.__name__=_C
_MonitorDirection_Object=MibScalar
monitorDirection=_MonitorDirection_Object((1,3,6,1,4,1,8691,7,6,1,13,3),_MonitorDirection_Type())
monitorDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:monitorDirection.setStatus(_A)
_CommRedundancy_ObjectIdentity=ObjectIdentity
commRedundancy=_CommRedundancy_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16))
class _ProtocolOfRedundancySetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),(_n,4)))
_ProtocolOfRedundancySetup_Type.__name__=_C
_ProtocolOfRedundancySetup_Object=MibScalar
protocolOfRedundancySetup=_ProtocolOfRedundancySetup_Object((1,3,6,1,4,1,8691,7,6,1,16,1),_ProtocolOfRedundancySetup_Type())
protocolOfRedundancySetup.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolOfRedundancySetup.setStatus(_A)
_TurboRing_ObjectIdentity=ObjectIdentity
turboRing=_TurboRing_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,2))
class _TurboRingMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_TurboRingMaster_Type.__name__=_C
_TurboRingMaster_Object=MibScalar
turboRingMaster=_TurboRingMaster_Object((1,3,6,1,4,1,8691,7,6,1,16,2,1),_TurboRingMaster_Type())
turboRingMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingMaster.setStatus(_A)
class _TurboRingMasterSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_TurboRingMasterSetup_Type.__name__=_C
_TurboRingMasterSetup_Object=MibScalar
turboRingMasterSetup=_TurboRingMasterSetup_Object((1,3,6,1,4,1,8691,7,6,1,16,2,2),_TurboRingMasterSetup_Type())
turboRingMasterSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingMasterSetup.setStatus(_A)
_TurboRingPortTable_Object=MibTable
turboRingPortTable=_TurboRingPortTable_Object((1,3,6,1,4,1,8691,7,6,1,16,2,3))
if mibBuilder.loadTexts:turboRingPortTable.setStatus(_A)
_TurboRingPortEntry_Object=MibTableRow
turboRingPortEntry=_TurboRingPortEntry_Object((1,3,6,1,4,1,8691,7,6,1,16,2,3,1))
turboRingPortEntry.setIndexNames((0,_G,_A2))
if mibBuilder.loadTexts:turboRingPortEntry.setStatus(_A)
_TurboRingPortIndex_Type=Integer32
_TurboRingPortIndex_Object=MibTableColumn
turboRingPortIndex=_TurboRingPortIndex_Object((1,3,6,1,4,1,8691,7,6,1,16,2,3,1,1),_TurboRingPortIndex_Type())
turboRingPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortIndex.setStatus(_A)
class _TurboRingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),('notTurboRingPort',1),(_Q,2),(_R,3),(_M,4),(_J,5)))
_TurboRingPortStatus_Type.__name__=_C
_TurboRingPortStatus_Object=MibTableColumn
turboRingPortStatus=_TurboRingPortStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,2,3,1,2),_TurboRingPortStatus_Type())
turboRingPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortStatus.setStatus(_A)
_TurboRingPortDesignatedBridge_Type=MacAddress
_TurboRingPortDesignatedBridge_Object=MibTableColumn
turboRingPortDesignatedBridge=_TurboRingPortDesignatedBridge_Object((1,3,6,1,4,1,8691,7,6,1,16,2,3,1,3),_TurboRingPortDesignatedBridge_Type())
turboRingPortDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortDesignatedBridge.setStatus(_A)
_TurboRingPortDesignatedPort_Type=Integer32
_TurboRingPortDesignatedPort_Object=MibTableColumn
turboRingPortDesignatedPort=_TurboRingPortDesignatedPort_Object((1,3,6,1,4,1,8691,7,6,1,16,2,3,1,4),_TurboRingPortDesignatedPort_Type())
turboRingPortDesignatedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortDesignatedPort.setStatus(_A)
_TurboRingDesignatedMaster_Type=MacAddress
_TurboRingDesignatedMaster_Object=MibScalar
turboRingDesignatedMaster=_TurboRingDesignatedMaster_Object((1,3,6,1,4,1,8691,7,6,1,16,2,6),_TurboRingDesignatedMaster_Type())
turboRingDesignatedMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingDesignatedMaster.setStatus(_A)
_TurboRingRdntPort1_Type=Integer32
_TurboRingRdntPort1_Object=MibScalar
turboRingRdntPort1=_TurboRingRdntPort1_Object((1,3,6,1,4,1,8691,7,6,1,16,2,7),_TurboRingRdntPort1_Type())
turboRingRdntPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort1.setStatus(_A)
_TurboRingRdntPort2_Type=Integer32
_TurboRingRdntPort2_Object=MibScalar
turboRingRdntPort2=_TurboRingRdntPort2_Object((1,3,6,1,4,1,8691,7,6,1,16,2,8),_TurboRingRdntPort2_Type())
turboRingRdntPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort2.setStatus(_A)
class _TurboRingEnableCoupling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TurboRingEnableCoupling_Type.__name__=_C
_TurboRingEnableCoupling_Object=MibScalar
turboRingEnableCoupling=_TurboRingEnableCoupling_Object((1,3,6,1,4,1,8691,7,6,1,16,2,9),_TurboRingEnableCoupling_Type())
turboRingEnableCoupling.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingEnableCoupling.setStatus(_A)
_TurboRingCouplingPort_Type=Integer32
_TurboRingCouplingPort_Object=MibScalar
turboRingCouplingPort=_TurboRingCouplingPort_Object((1,3,6,1,4,1,8691,7,6,1,16,2,10),_TurboRingCouplingPort_Type())
turboRingCouplingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingCouplingPort.setStatus(_A)
class _TurboRingCouplingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5)));namedValues=NamedValues(*((_a,0),('notCouplingPort',1),(_Q,2),(_R,3),(_J,5)))
_TurboRingCouplingPortStatus_Type.__name__=_C
_TurboRingCouplingPortStatus_Object=MibScalar
turboRingCouplingPortStatus=_TurboRingCouplingPortStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,2,11),_TurboRingCouplingPortStatus_Type())
turboRingCouplingPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingCouplingPortStatus.setStatus(_A)
_TurboRingControlPort_Type=Integer32
_TurboRingControlPort_Object=MibScalar
turboRingControlPort=_TurboRingControlPort_Object((1,3,6,1,4,1,8691,7,6,1,16,2,12),_TurboRingControlPort_Type())
turboRingControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingControlPort.setStatus(_A)
class _TurboRingControlPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7)));namedValues=NamedValues(*((_a,0),('notControlPort',1),(_Q,2),(_R,3),(_J,5),('inactive',6),(_o,7)))
_TurboRingControlPortStatus_Type.__name__=_C
_TurboRingControlPortStatus_Object=MibScalar
turboRingControlPortStatus=_TurboRingControlPortStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,2,13),_TurboRingControlPortStatus_Type())
turboRingControlPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingControlPortStatus.setStatus(_A)
class _TurboRingBrokenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_S,1),(_p,2)))
_TurboRingBrokenStatus_Type.__name__=_C
_TurboRingBrokenStatus_Object=MibScalar
turboRingBrokenStatus=_TurboRingBrokenStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,2,14),_TurboRingBrokenStatus_Type())
turboRingBrokenStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingBrokenStatus.setStatus(_A)
_SpanningTree_ObjectIdentity=ObjectIdentity
spanningTree=_SpanningTree_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,3))
class _SpanningTreeRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SpanningTreeRoot_Type.__name__=_C
_SpanningTreeRoot_Object=MibScalar
spanningTreeRoot=_SpanningTreeRoot_Object((1,3,6,1,4,1,8691,7,6,1,16,3,1),_SpanningTreeRoot_Type())
spanningTreeRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreeRoot.setStatus(_A)
class _SpanningTreeBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4096,8192,12288,16384,20480,24576,28672,32768,36864,40960,45056,49152,53248,57344,61440)));namedValues=NamedValues(*((_q,0),('priority4096',4096),('priority8192',8192),('priority12288',12288),('priority16384',16384),('priority20480',20480),('priority24576',24576),('priority28672',28672),('priority32768',32768),('priority36864',36864),('priority40960',40960),('priority45056',45056),('priority49152',49152),('priority53248',53248),('priority57344',57344),('priority61440',61440)))
_SpanningTreeBridgePriority_Type.__name__=_C
_SpanningTreeBridgePriority_Object=MibScalar
spanningTreeBridgePriority=_SpanningTreeBridgePriority_Object((1,3,6,1,4,1,8691,7,6,1,16,3,2),_SpanningTreeBridgePriority_Type())
spanningTreeBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeBridgePriority.setStatus(_A)
_SpanningTreeHelloTime_Type=Integer32
_SpanningTreeHelloTime_Object=MibScalar
spanningTreeHelloTime=_SpanningTreeHelloTime_Object((1,3,6,1,4,1,8691,7,6,1,16,3,3),_SpanningTreeHelloTime_Type())
spanningTreeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeHelloTime.setStatus(_A)
_SpanningTreeMaxAge_Type=Integer32
_SpanningTreeMaxAge_Object=MibScalar
spanningTreeMaxAge=_SpanningTreeMaxAge_Object((1,3,6,1,4,1,8691,7,6,1,16,3,4),_SpanningTreeMaxAge_Type())
spanningTreeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeMaxAge.setStatus(_A)
_SpanningTreeForwardingDelay_Type=Integer32
_SpanningTreeForwardingDelay_Object=MibScalar
spanningTreeForwardingDelay=_SpanningTreeForwardingDelay_Object((1,3,6,1,4,1,8691,7,6,1,16,3,5),_SpanningTreeForwardingDelay_Type())
spanningTreeForwardingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeForwardingDelay.setStatus(_A)
_SpanningTreeTable_Object=MibTable
spanningTreeTable=_SpanningTreeTable_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6))
if mibBuilder.loadTexts:spanningTreeTable.setStatus(_A)
_SpanningTreeEntry_Object=MibTableRow
spanningTreeEntry=_SpanningTreeEntry_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1))
spanningTreeEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:spanningTreeEntry.setStatus(_A)
_SpanningTreeIndex_Type=Integer32
_SpanningTreeIndex_Object=MibTableColumn
spanningTreeIndex=_SpanningTreeIndex_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1,1),_SpanningTreeIndex_Type())
spanningTreeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreeIndex.setStatus(_A)
class _EnableSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableSpanningTree_Type.__name__=_C
_EnableSpanningTree_Object=MibTableColumn
enableSpanningTree=_EnableSpanningTree_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1,2),_EnableSpanningTree_Type())
enableSpanningTree.setMaxAccess(_B)
if mibBuilder.loadTexts:enableSpanningTree.setStatus(_A)
class _SpanningTreePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240)));namedValues=NamedValues(*((_q,0),('priority16',16),('priority32',32),('priority48',48),('priority64',64),('priority80',80),('priority96',96),('priority112',112),('priority128',128),('priority144',144),('priority160',160),('priority176',176),('priority192',192),('priority208',208),('priority224',224),('priority240',240)))
_SpanningTreePortPriority_Type.__name__=_C
_SpanningTreePortPriority_Object=MibTableColumn
spanningTreePortPriority=_SpanningTreePortPriority_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1,3),_SpanningTreePortPriority_Type())
spanningTreePortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortPriority.setStatus(_A)
_SpanningTreePortCost_Type=Integer32
_SpanningTreePortCost_Object=MibTableColumn
spanningTreePortCost=_SpanningTreePortCost_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1,4),_SpanningTreePortCost_Type())
spanningTreePortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortCost.setStatus(_A)
class _SpanningTreePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),('notSpanningTreePort',1),(_Q,2),(_R,3),(_M,4),(_J,5)))
_SpanningTreePortStatus_Type.__name__=_C
_SpanningTreePortStatus_Object=MibTableColumn
spanningTreePortStatus=_SpanningTreePortStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1,5),_SpanningTreePortStatus_Type())
spanningTreePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreePortStatus.setStatus(_A)
class _SpanningTreePortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_j,0),('forceEdge',1),('false',2)))
_SpanningTreePortEdge_Type.__name__=_C
_SpanningTreePortEdge_Object=MibTableColumn
spanningTreePortEdge=_SpanningTreePortEdge_Object((1,3,6,1,4,1,8691,7,6,1,16,3,6,1,6),_SpanningTreePortEdge_Type())
spanningTreePortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortEdge.setStatus(_A)
class _ActiveProtocolOfRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_O,0),(_k,1),(_l,2),(_m,3),(_n,4)))
_ActiveProtocolOfRedundancy_Type.__name__=_C
_ActiveProtocolOfRedundancy_Object=MibScalar
activeProtocolOfRedundancy=_ActiveProtocolOfRedundancy_Object((1,3,6,1,4,1,8691,7,6,1,16,4),_ActiveProtocolOfRedundancy_Type())
activeProtocolOfRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:activeProtocolOfRedundancy.setStatus(_A)
_TurboRingV2_ObjectIdentity=ObjectIdentity
turboRingV2=_TurboRingV2_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,5))
_TurboRingV2Ring1_ObjectIdentity=ObjectIdentity
turboRingV2Ring1=_TurboRingV2Ring1_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,5,1))
class _RingIndexRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RingIndexRing1_Type.__name__=_C
_RingIndexRing1_Object=MibScalar
ringIndexRing1=_RingIndexRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,1),_RingIndexRing1_Type())
ringIndexRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:ringIndexRing1.setStatus(_A)
class _RingEnableRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RingEnableRing1_Type.__name__=_C
_RingEnableRing1_Object=MibScalar
ringEnableRing1=_RingEnableRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,2),_RingEnableRing1_Type())
ringEnableRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:ringEnableRing1.setStatus(_A)
class _MasterSetupRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_MasterSetupRing1_Type.__name__=_C
_MasterSetupRing1_Object=MibScalar
masterSetupRing1=_MasterSetupRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,3),_MasterSetupRing1_Type())
masterSetupRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:masterSetupRing1.setStatus(_A)
class _MasterStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_MasterStatusRing1_Type.__name__=_C
_MasterStatusRing1_Object=MibScalar
masterStatusRing1=_MasterStatusRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,4),_MasterStatusRing1_Type())
masterStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:masterStatusRing1.setStatus(_A)
_DesignatedMasterRing1_Type=MacAddress
_DesignatedMasterRing1_Object=MibScalar
designatedMasterRing1=_DesignatedMasterRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,5),_DesignatedMasterRing1_Type())
designatedMasterRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:designatedMasterRing1.setStatus(_A)
_Rdnt1stPortRing1_Type=Integer32
_Rdnt1stPortRing1_Object=MibScalar
rdnt1stPortRing1=_Rdnt1stPortRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,6),_Rdnt1stPortRing1_Type())
rdnt1stPortRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt1stPortRing1.setStatus(_A)
class _Rdnt1stPortStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_N,3),(_M,4),(_J,5)))
_Rdnt1stPortStatusRing1_Type.__name__=_C
_Rdnt1stPortStatusRing1_Object=MibScalar
rdnt1stPortStatusRing1=_Rdnt1stPortStatusRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,7),_Rdnt1stPortStatusRing1_Type())
rdnt1stPortStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt1stPortStatusRing1.setStatus(_A)
_Rdnt2ndPortRing1_Type=Integer32
_Rdnt2ndPortRing1_Object=MibScalar
rdnt2ndPortRing1=_Rdnt2ndPortRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,8),_Rdnt2ndPortRing1_Type())
rdnt2ndPortRing1.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt2ndPortRing1.setStatus(_A)
class _Rdnt2ndPortStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_N,3),(_M,4),(_J,5)))
_Rdnt2ndPortStatusRing1_Type.__name__=_C
_Rdnt2ndPortStatusRing1_Object=MibScalar
rdnt2ndPortStatusRing1=_Rdnt2ndPortStatusRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,9),_Rdnt2ndPortStatusRing1_Type())
rdnt2ndPortStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt2ndPortStatusRing1.setStatus(_A)
class _BrokenStatusRing1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_S,1),(_p,2)))
_BrokenStatusRing1_Type.__name__=_C
_BrokenStatusRing1_Object=MibScalar
brokenStatusRing1=_BrokenStatusRing1_Object((1,3,6,1,4,1,8691,7,6,1,16,5,1,10),_BrokenStatusRing1_Type())
brokenStatusRing1.setMaxAccess(_D)
if mibBuilder.loadTexts:brokenStatusRing1.setStatus(_A)
_TurboRingV2Ring2_ObjectIdentity=ObjectIdentity
turboRingV2Ring2=_TurboRingV2Ring2_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,5,2))
class _RingIndexRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RingIndexRing2_Type.__name__=_C
_RingIndexRing2_Object=MibScalar
ringIndexRing2=_RingIndexRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,1),_RingIndexRing2_Type())
ringIndexRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:ringIndexRing2.setStatus(_A)
class _RingEnableRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RingEnableRing2_Type.__name__=_C
_RingEnableRing2_Object=MibScalar
ringEnableRing2=_RingEnableRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,2),_RingEnableRing2_Type())
ringEnableRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:ringEnableRing2.setStatus(_A)
class _MasterSetupRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_MasterSetupRing2_Type.__name__=_C
_MasterSetupRing2_Object=MibScalar
masterSetupRing2=_MasterSetupRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,3),_MasterSetupRing2_Type())
masterSetupRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:masterSetupRing2.setStatus(_A)
class _MasterStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_MasterStatusRing2_Type.__name__=_C
_MasterStatusRing2_Object=MibScalar
masterStatusRing2=_MasterStatusRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,4),_MasterStatusRing2_Type())
masterStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:masterStatusRing2.setStatus(_A)
_DesignatedMasterRing2_Type=MacAddress
_DesignatedMasterRing2_Object=MibScalar
designatedMasterRing2=_DesignatedMasterRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,5),_DesignatedMasterRing2_Type())
designatedMasterRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:designatedMasterRing2.setStatus(_A)
_Rdnt1stPortRing2_Type=Integer32
_Rdnt1stPortRing2_Object=MibScalar
rdnt1stPortRing2=_Rdnt1stPortRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,6),_Rdnt1stPortRing2_Type())
rdnt1stPortRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt1stPortRing2.setStatus(_A)
class _Rdnt1stPortStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_N,3),(_M,4),(_J,5)))
_Rdnt1stPortStatusRing2_Type.__name__=_C
_Rdnt1stPortStatusRing2_Object=MibScalar
rdnt1stPortStatusRing2=_Rdnt1stPortStatusRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,7),_Rdnt1stPortStatusRing2_Type())
rdnt1stPortStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt1stPortStatusRing2.setStatus(_A)
_Rdnt2ndPortRing2_Type=Integer32
_Rdnt2ndPortRing2_Object=MibScalar
rdnt2ndPortRing2=_Rdnt2ndPortRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,8),_Rdnt2ndPortRing2_Type())
rdnt2ndPortRing2.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnt2ndPortRing2.setStatus(_A)
class _Rdnt2ndPortStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_N,3),(_M,4),(_J,5)))
_Rdnt2ndPortStatusRing2_Type.__name__=_C
_Rdnt2ndPortStatusRing2_Object=MibScalar
rdnt2ndPortStatusRing2=_Rdnt2ndPortStatusRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,9),_Rdnt2ndPortStatusRing2_Type())
rdnt2ndPortStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:rdnt2ndPortStatusRing2.setStatus(_A)
class _BrokenStatusRing2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_S,1),(_p,2)))
_BrokenStatusRing2_Type.__name__=_C
_BrokenStatusRing2_Object=MibScalar
brokenStatusRing2=_BrokenStatusRing2_Object((1,3,6,1,4,1,8691,7,6,1,16,5,2,10),_BrokenStatusRing2_Type())
brokenStatusRing2.setMaxAccess(_D)
if mibBuilder.loadTexts:brokenStatusRing2.setStatus(_A)
_TurboRingV2Coupling_ObjectIdentity=ObjectIdentity
turboRingV2Coupling=_TurboRingV2Coupling_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,5,3))
class _CouplingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingEnable_Type.__name__=_C
_CouplingEnable_Object=MibScalar
couplingEnable=_CouplingEnable_Object((1,3,6,1,4,1,8691,7,6,1,16,5,3,1),_CouplingEnable_Type())
couplingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:couplingEnable.setStatus(_A)
class _CouplingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dualHoming',1),('couplingBackup',2),('couplingPrimary',3)))
_CouplingMode_Type.__name__=_C
_CouplingMode_Object=MibScalar
couplingMode=_CouplingMode_Object((1,3,6,1,4,1,8691,7,6,1,16,5,3,2),_CouplingMode_Type())
couplingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:couplingMode.setStatus(_A)
_Coupling1stPort_Type=Integer32
_Coupling1stPort_Object=MibScalar
coupling1stPort=_Coupling1stPort_Object((1,3,6,1,4,1,8691,7,6,1,16,5,3,3),_Coupling1stPort_Type())
coupling1stPort.setMaxAccess(_B)
if mibBuilder.loadTexts:coupling1stPort.setStatus(_A)
class _Coupling1stPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_N,3),(_M,4),(_J,5)))
_Coupling1stPortStatus_Type.__name__=_C
_Coupling1stPortStatus_Object=MibScalar
coupling1stPortStatus=_Coupling1stPortStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,5,3,4),_Coupling1stPortStatus_Type())
coupling1stPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coupling1stPortStatus.setStatus(_A)
_Coupling2ndPort_Type=Integer32
_Coupling2ndPort_Object=MibScalar
coupling2ndPort=_Coupling2ndPort_Object((1,3,6,1,4,1,8691,7,6,1,16,5,3,5),_Coupling2ndPort_Type())
coupling2ndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:coupling2ndPort.setStatus(_A)
class _Coupling2ndPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_N,3),(_M,4),(_J,5)))
_Coupling2ndPortStatus_Type.__name__=_C
_Coupling2ndPortStatus_Object=MibScalar
coupling2ndPortStatus=_Coupling2ndPortStatus_Object((1,3,6,1,4,1,8691,7,6,1,16,5,3,6),_Coupling2ndPortStatus_Type())
coupling2ndPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coupling2ndPortStatus.setStatus(_A)
_TurboChain_ObjectIdentity=ObjectIdentity
turboChain=_TurboChain_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,16,6))
class _TurboChainRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('head',1),('member',2),('tail',3)))
_TurboChainRole_Type.__name__=_C
_TurboChainRole_Object=MibScalar
turboChainRole=_TurboChainRole_Object((1,3,6,1,4,1,8691,7,6,1,16,6,1),_TurboChainRole_Type())
turboChainRole.setMaxAccess(_B)
if mibBuilder.loadTexts:turboChainRole.setStatus(_A)
_TurboChainPort1_Type=Integer32
_TurboChainPort1_Object=MibScalar
turboChainPort1=_TurboChainPort1_Object((1,3,6,1,4,1,8691,7,6,1,16,6,2),_TurboChainPort1_Type())
turboChainPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboChainPort1.setStatus(_A)
_TurboChainPort2_Type=Integer32
_TurboChainPort2_Object=MibScalar
turboChainPort2=_TurboChainPort2_Object((1,3,6,1,4,1,8691,7,6,1,16,6,3),_TurboChainPort2_Type())
turboChainPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboChainPort2.setStatus(_A)
class _TurboChainPort1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A4,0),(_Q,1),(_N,2),(_R,3),(_J,4),(_H,5)))
_TurboChainPort1Status_Type.__name__=_C
_TurboChainPort1Status_Object=MibScalar
turboChainPort1Status=_TurboChainPort1Status_Object((1,3,6,1,4,1,8691,7,6,1,16,6,4),_TurboChainPort1Status_Type())
turboChainPort1Status.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort1Status.setStatus(_A)
class _TurboChainPort2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A4,0),(_Q,1),(_N,2),(_R,3),(_J,4),(_H,5)))
_TurboChainPort2Status_Type.__name__=_C
_TurboChainPort2Status_Object=MibScalar
turboChainPort2Status=_TurboChainPort2Status_Object((1,3,6,1,4,1,8691,7,6,1,16,6,5),_TurboChainPort2Status_Type())
turboChainPort2Status.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort2Status.setStatus(_A)
_TurboChainPort1PartnerBridge_Type=MacAddress
_TurboChainPort1PartnerBridge_Object=MibScalar
turboChainPort1PartnerBridge=_TurboChainPort1PartnerBridge_Object((1,3,6,1,4,1,8691,7,6,1,16,6,6),_TurboChainPort1PartnerBridge_Type())
turboChainPort1PartnerBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort1PartnerBridge.setStatus(_A)
_TurboChainPort2PartnerBridge_Type=MacAddress
_TurboChainPort2PartnerBridge_Object=MibScalar
turboChainPort2PartnerBridge=_TurboChainPort2PartnerBridge_Object((1,3,6,1,4,1,8691,7,6,1,16,6,7),_TurboChainPort2PartnerBridge_Type())
turboChainPort2PartnerBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboChainPort2PartnerBridge.setStatus(_A)
_RelayWarning_ObjectIdentity=ObjectIdentity
relayWarning=_RelayWarning_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,17))
_RelayWarningTable_Object=MibTable
relayWarningTable=_RelayWarningTable_Object((1,3,6,1,4,1,8691,7,6,1,17,11))
if mibBuilder.loadTexts:relayWarningTable.setStatus(_A)
_RelayWarningEntry_Object=MibTableRow
relayWarningEntry=_RelayWarningEntry_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1))
relayWarningEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:relayWarningEntry.setStatus(_A)
_RelayAlarmIndex_Type=Integer32
_RelayAlarmIndex_Object=MibTableColumn
relayAlarmIndex=_RelayAlarmIndex_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,1),_RelayAlarmIndex_Type())
relayAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:relayAlarmIndex.setStatus(_A)
class _RelayWarningRelayContact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('opened',1)))
_RelayWarningRelayContact_Type.__name__=_C
_RelayWarningRelayContact_Object=MibTableColumn
relayWarningRelayContact=_RelayWarningRelayContact_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,2),_RelayWarningRelayContact_Type())
relayWarningRelayContact.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningRelayContact.setStatus(_A)
class _OverrideRelayWarningSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_OverrideRelayWarningSetting_Type.__name__=_C
_OverrideRelayWarningSetting_Object=MibTableColumn
overrideRelayWarningSetting=_OverrideRelayWarningSetting_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,3),_OverrideRelayWarningSetting_Type())
overrideRelayWarningSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:overrideRelayWarningSetting.setStatus(_A)
class _RelayWarningPower1Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningPower1Off_Type.__name__=_C
_RelayWarningPower1Off_Object=MibTableColumn
relayWarningPower1Off=_RelayWarningPower1Off_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,4),_RelayWarningPower1Off_Type())
relayWarningPower1Off.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningPower1Off.setStatus(_A)
class _RelayWarningPower1OffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_RelayWarningPower1OffStatus_Type.__name__=_C
_RelayWarningPower1OffStatus_Object=MibTableColumn
relayWarningPower1OffStatus=_RelayWarningPower1OffStatus_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,5),_RelayWarningPower1OffStatus_Type())
relayWarningPower1OffStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningPower1OffStatus.setStatus(_A)
class _RelayWarningPower2Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningPower2Off_Type.__name__=_C
_RelayWarningPower2Off_Object=MibTableColumn
relayWarningPower2Off=_RelayWarningPower2Off_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,6),_RelayWarningPower2Off_Type())
relayWarningPower2Off.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningPower2Off.setStatus(_A)
class _RelayWarningPower2OffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_RelayWarningPower2OffStatus_Type.__name__=_C
_RelayWarningPower2OffStatus_Object=MibTableColumn
relayWarningPower2OffStatus=_RelayWarningPower2OffStatus_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,7),_RelayWarningPower2OffStatus_Type())
relayWarningPower2OffStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningPower2OffStatus.setStatus(_A)
class _RelayWarningTurboRingBreak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningTurboRingBreak_Type.__name__=_C
_RelayWarningTurboRingBreak_Object=MibTableColumn
relayWarningTurboRingBreak=_RelayWarningTurboRingBreak_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,8),_RelayWarningTurboRingBreak_Type())
relayWarningTurboRingBreak.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTurboRingBreak.setStatus(_A)
class _RelayWarningTurboRingBreakStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_RelayWarningTurboRingBreakStatus_Type.__name__=_C
_RelayWarningTurboRingBreakStatus_Object=MibTableColumn
relayWarningTurboRingBreakStatus=_RelayWarningTurboRingBreakStatus_Object((1,3,6,1,4,1,8691,7,6,1,17,11,1,9),_RelayWarningTurboRingBreakStatus_Type())
relayWarningTurboRingBreakStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningTurboRingBreakStatus.setStatus(_A)
_PortRelayWarningTable_Object=MibTable
portRelayWarningTable=_PortRelayWarningTable_Object((1,3,6,1,4,1,8691,7,6,1,17,12))
if mibBuilder.loadTexts:portRelayWarningTable.setStatus(_A)
_PortRelayWarningEntry_Object=MibTableRow
portRelayWarningEntry=_PortRelayWarningEntry_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1))
portRelayWarningEntry.setIndexNames((0,_G,_L),(0,_G,_r))
if mibBuilder.loadTexts:portRelayWarningEntry.setStatus(_A)
class _RelayWarningLinkChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ignore',0),(_s,1),(_t,2)))
_RelayWarningLinkChanged_Type.__name__=_C
_RelayWarningLinkChanged_Object=MibTableColumn
relayWarningLinkChanged=_RelayWarningLinkChanged_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1,1),_RelayWarningLinkChanged_Type())
relayWarningLinkChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningLinkChanged.setStatus(_A)
class _RelayWarningLinkChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_RelayWarningLinkChangedStatus_Type.__name__=_C
_RelayWarningLinkChangedStatus_Object=MibTableColumn
relayWarningLinkChangedStatus=_RelayWarningLinkChangedStatus_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1,2),_RelayWarningLinkChangedStatus_Type())
relayWarningLinkChangedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningLinkChangedStatus.setStatus(_A)
class _RelayWarningTrafficOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningTrafficOverload_Type.__name__=_C
_RelayWarningTrafficOverload_Object=MibTableColumn
relayWarningTrafficOverload=_RelayWarningTrafficOverload_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1,3),_RelayWarningTrafficOverload_Type())
relayWarningTrafficOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficOverload.setStatus(_A)
class _RelayWarningTrafficOverloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_RelayWarningTrafficOverloadStatus_Type.__name__=_C
_RelayWarningTrafficOverloadStatus_Object=MibTableColumn
relayWarningTrafficOverloadStatus=_RelayWarningTrafficOverloadStatus_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1,4),_RelayWarningTrafficOverloadStatus_Type())
relayWarningTrafficOverloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningTrafficOverloadStatus.setStatus(_A)
_RelayWarningRxTrafficThreshold_Type=Integer32
_RelayWarningRxTrafficThreshold_Object=MibTableColumn
relayWarningRxTrafficThreshold=_RelayWarningRxTrafficThreshold_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1,5),_RelayWarningRxTrafficThreshold_Type())
relayWarningRxTrafficThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningRxTrafficThreshold.setStatus(_A)
_RelayWarningTrafficDuration_Type=Integer32
_RelayWarningTrafficDuration_Object=MibTableColumn
relayWarningTrafficDuration=_RelayWarningTrafficDuration_Object((1,3,6,1,4,1,8691,7,6,1,17,12,1,6),_RelayWarningTrafficDuration_Type())
relayWarningTrafficDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficDuration.setStatus(_A)
_TrafficPrioritization_ObjectIdentity=ObjectIdentity
trafficPrioritization=_TrafficPrioritization_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,18))
_QosClassification_ObjectIdentity=ObjectIdentity
qosClassification=_QosClassification_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,18,1))
class _QueuingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('schedweightfair',0),('schedstrict',1)))
_QueuingMechanism_Type.__name__=_C
_QueuingMechanism_Object=MibScalar
queuingMechanism=_QueuingMechanism_Object((1,3,6,1,4,1,8691,7,6,1,18,1,1),_QueuingMechanism_Type())
queuingMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:queuingMechanism.setStatus(_A)
_QosPortTable_Object=MibTable
qosPortTable=_QosPortTable_Object((1,3,6,1,4,1,8691,7,6,1,18,1,2))
if mibBuilder.loadTexts:qosPortTable.setStatus(_A)
_QosPortEntry_Object=MibTableRow
qosPortEntry=_QosPortEntry_Object((1,3,6,1,4,1,8691,7,6,1,18,1,2,1))
qosPortEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:qosPortEntry.setStatus(_A)
class _InspectTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_InspectTos_Type.__name__=_C
_InspectTos_Object=MibTableColumn
inspectTos=_InspectTos_Object((1,3,6,1,4,1,8691,7,6,1,18,1,2,1,1),_InspectTos_Type())
inspectTos.setMaxAccess(_B)
if mibBuilder.loadTexts:inspectTos.setStatus(_A)
class _InspectCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_InspectCos_Type.__name__=_C
_InspectCos_Object=MibTableColumn
inspectCos=_InspectCos_Object((1,3,6,1,4,1,8691,7,6,1,18,1,2,1,2),_InspectCos_Type())
inspectCos.setMaxAccess(_B)
if mibBuilder.loadTexts:inspectCos.setStatus(_A)
class _PortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_q,0),('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5),('priority6',6),('priority7',7)))
_PortPriority_Type.__name__=_C
_PortPriority_Object=MibTableColumn
portPriority=_PortPriority_Object((1,3,6,1,4,1,8691,7,6,1,18,1,2,1,3),_PortPriority_Type())
portPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:portPriority.setStatus(_A)
_CosMapping_ObjectIdentity=ObjectIdentity
cosMapping=_CosMapping_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,18,2))
_CosMappingTable_Object=MibTable
cosMappingTable=_CosMappingTable_Object((1,3,6,1,4,1,8691,7,6,1,18,2,1))
if mibBuilder.loadTexts:cosMappingTable.setStatus(_A)
_CosMappingEntry_Object=MibTableRow
cosMappingEntry=_CosMappingEntry_Object((1,3,6,1,4,1,8691,7,6,1,18,2,1,1))
cosMappingEntry.setIndexNames((0,_G,'cosTag'))
if mibBuilder.loadTexts:cosMappingEntry.setStatus(_A)
class _CosTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CosTag_Type.__name__=_C
_CosTag_Object=MibTableColumn
cosTag=_CosTag_Object((1,3,6,1,4,1,8691,7,6,1,18,2,1,1,1),_CosTag_Type())
cosTag.setMaxAccess(_D)
if mibBuilder.loadTexts:cosTag.setStatus(_A)
class _CosMappedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('low',0),(_S,1),('medium',2),('high',3)))
_CosMappedPriority_Type.__name__=_C
_CosMappedPriority_Object=MibTableColumn
cosMappedPriority=_CosMappedPriority_Object((1,3,6,1,4,1,8691,7,6,1,18,2,1,1,2),_CosMappedPriority_Type())
cosMappedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cosMappedPriority.setStatus(_A)
_TosMapping_ObjectIdentity=ObjectIdentity
tosMapping=_TosMapping_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,18,3))
_TosMappingTable_Object=MibTable
tosMappingTable=_TosMappingTable_Object((1,3,6,1,4,1,8691,7,6,1,18,3,1))
if mibBuilder.loadTexts:tosMappingTable.setStatus(_A)
_TosMappingEntry_Object=MibTableRow
tosMappingEntry=_TosMappingEntry_Object((1,3,6,1,4,1,8691,7,6,1,18,3,1,1))
tosMappingEntry.setIndexNames((0,_G,'tosClass'))
if mibBuilder.loadTexts:tosMappingEntry.setStatus(_A)
_TosClass_Type=Integer32
_TosClass_Object=MibTableColumn
tosClass=_TosClass_Object((1,3,6,1,4,1,8691,7,6,1,18,3,1,1,1),_TosClass_Type())
tosClass.setMaxAccess(_D)
if mibBuilder.loadTexts:tosClass.setStatus(_A)
class _TosMappedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('low',0),(_S,1),('medium',2),('high',3)))
_TosMappedPriority_Type.__name__=_C
_TosMappedPriority_Object=MibTableColumn
tosMappedPriority=_TosMappedPriority_Object((1,3,6,1,4,1,8691,7,6,1,18,3,1,1,2),_TosMappedPriority_Type())
tosMappedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tosMappedPriority.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,19))
_VlanPortSettingTable_Object=MibTable
vlanPortSettingTable=_VlanPortSettingTable_Object((1,3,6,1,4,1,8691,7,6,1,19,1))
if mibBuilder.loadTexts:vlanPortSettingTable.setStatus(_A)
_VlanPortSettingEntry_Object=MibTableRow
vlanPortSettingEntry=_VlanPortSettingEntry_Object((1,3,6,1,4,1,8691,7,6,1,19,1,1))
vlanPortSettingEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:vlanPortSettingEntry.setStatus(_A)
class _PortVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('access',0),('trunk',1),('hybrid',2)))
_PortVlanType_Type.__name__=_C
_PortVlanType_Object=MibTableColumn
portVlanType=_PortVlanType_Object((1,3,6,1,4,1,8691,7,6,1,19,1,1,1),_PortVlanType_Type())
portVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:portVlanType.setStatus(_A)
class _PortDefaultVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortDefaultVid_Type.__name__=_C
_PortDefaultVid_Object=MibTableColumn
portDefaultVid=_PortDefaultVid_Object((1,3,6,1,4,1,8691,7,6,1,19,1,1,2),_PortDefaultVid_Type())
portDefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portDefaultVid.setStatus(_A)
_PortFixedVid_Type=DisplayString
_PortFixedVid_Object=MibTableColumn
portFixedVid=_PortFixedVid_Object((1,3,6,1,4,1,8691,7,6,1,19,1,1,3),_PortFixedVid_Type())
portFixedVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portFixedVid.setStatus(_A)
_PortForbiddenVid_Type=DisplayString
_PortForbiddenVid_Object=MibTableColumn
portForbiddenVid=_PortForbiddenVid_Object((1,3,6,1,4,1,8691,7,6,1,19,1,1,4),_PortForbiddenVid_Type())
portForbiddenVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portForbiddenVid.setStatus(_A)
_PortFixedVidUntag_Type=DisplayString
_PortFixedVidUntag_Object=MibTableColumn
portFixedVidUntag=_PortFixedVidUntag_Object((1,3,6,1,4,1,8691,7,6,1,19,1,1,5),_PortFixedVidUntag_Type())
portFixedVidUntag.setMaxAccess(_B)
if mibBuilder.loadTexts:portFixedVidUntag.setStatus(_A)
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,8691,7,6,1,19,2))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,8691,7,6,1,19,2,1))
vlanEntry.setIndexNames((0,_G,_u))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanId_Type.__name__=_C
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,8691,7,6,1,19,2,1,1),_VlanId_Type())
vlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
_JoinedAccessPorts_Type=PortList
_JoinedAccessPorts_Object=MibTableColumn
joinedAccessPorts=_JoinedAccessPorts_Object((1,3,6,1,4,1,8691,7,6,1,19,2,1,2),_JoinedAccessPorts_Type())
joinedAccessPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedAccessPorts.setStatus(_A)
_JoinedTrunkPorts_Type=PortList
_JoinedTrunkPorts_Object=MibTableColumn
joinedTrunkPorts=_JoinedTrunkPorts_Object((1,3,6,1,4,1,8691,7,6,1,19,2,1,3),_JoinedTrunkPorts_Type())
joinedTrunkPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedTrunkPorts.setStatus(_A)
_JoinedHybridPorts_Type=PortList
_JoinedHybridPorts_Object=MibTableColumn
joinedHybridPorts=_JoinedHybridPorts_Object((1,3,6,1,4,1,8691,7,6,1,19,2,1,4),_JoinedHybridPorts_Type())
joinedHybridPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedHybridPorts.setStatus(_A)
_ManagementVlanId_Type=Integer32
_ManagementVlanId_Object=MibScalar
managementVlanId=_ManagementVlanId_Object((1,3,6,1,4,1,8691,7,6,1,19,3),_ManagementVlanId_Type())
managementVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:managementVlanId.setStatus(_A)
class _VlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tagBased',0),('portBased',1)))
_VlanType_Type.__name__=_C
_VlanType_Object=MibScalar
vlanType=_VlanType_Object((1,3,6,1,4,1,8691,7,6,1,19,4),_VlanType_Type())
vlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanType.setStatus(_A)
_PortbaseVlanSettingTable_Object=MibTable
portbaseVlanSettingTable=_PortbaseVlanSettingTable_Object((1,3,6,1,4,1,8691,7,6,1,19,5))
if mibBuilder.loadTexts:portbaseVlanSettingTable.setStatus(_A)
_PortbaseVlanSettingEntry_Object=MibTableRow
portbaseVlanSettingEntry=_PortbaseVlanSettingEntry_Object((1,3,6,1,4,1,8691,7,6,1,19,5,1))
portbaseVlanSettingEntry.setIndexNames((0,_G,_A5))
if mibBuilder.loadTexts:portbaseVlanSettingEntry.setStatus(_A)
_PortbaseVlanSettingIndex_Type=Integer32
_PortbaseVlanSettingIndex_Object=MibTableColumn
portbaseVlanSettingIndex=_PortbaseVlanSettingIndex_Object((1,3,6,1,4,1,8691,7,6,1,19,5,1,1),_PortbaseVlanSettingIndex_Type())
portbaseVlanSettingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portbaseVlanSettingIndex.setStatus(_A)
_PortbaseVlanMemberPorts_Type=PortList
_PortbaseVlanMemberPorts_Object=MibTableColumn
portbaseVlanMemberPorts=_PortbaseVlanMemberPorts_Object((1,3,6,1,4,1,8691,7,6,1,19,5,1,2),_PortbaseVlanMemberPorts_Type())
portbaseVlanMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:portbaseVlanMemberPorts.setStatus(_A)
class _EnableGvrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableGvrp_Type.__name__=_C
_EnableGvrp_Object=MibScalar
enableGvrp=_EnableGvrp_Object((1,3,6,1,4,1,8691,7,6,1,19,6),_EnableGvrp_Type())
enableGvrp.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGvrp.setStatus(_A)
_MulticastFiltering_ObjectIdentity=ObjectIdentity
multicastFiltering=_MulticastFiltering_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,20))
_IgmpSnooping_ObjectIdentity=ObjectIdentity
igmpSnooping=_IgmpSnooping_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,20,1))
class _QuerierQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,600))
_QuerierQueryInterval_Type.__name__=_C
_QuerierQueryInterval_Object=MibScalar
querierQueryInterval=_QuerierQueryInterval_Object((1,3,6,1,4,1,8691,7,6,1,20,1,1),_QuerierQueryInterval_Type())
querierQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:querierQueryInterval.setStatus(_A)
_IgmpSnoopingSettingTable_Object=MibTable
igmpSnoopingSettingTable=_IgmpSnoopingSettingTable_Object((1,3,6,1,4,1,8691,7,6,1,20,1,2))
if mibBuilder.loadTexts:igmpSnoopingSettingTable.setStatus(_A)
_IgmpSnoopingSettingEntry_Object=MibTableRow
igmpSnoopingSettingEntry=_IgmpSnoopingSettingEntry_Object((1,3,6,1,4,1,8691,7,6,1,20,1,2,1))
igmpSnoopingSettingEntry.setIndexNames((0,_G,_u))
if mibBuilder.loadTexts:igmpSnoopingSettingEntry.setStatus(_A)
class _EnableIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableIgmpSnooping_Type.__name__=_C
_EnableIgmpSnooping_Object=MibTableColumn
enableIgmpSnooping=_EnableIgmpSnooping_Object((1,3,6,1,4,1,8691,7,6,1,20,1,2,1,1),_EnableIgmpSnooping_Type())
enableIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:enableIgmpSnooping.setStatus(_A)
class _EnableQuerier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableQuerier_Type.__name__=_C
_EnableQuerier_Object=MibTableColumn
enableQuerier=_EnableQuerier_Object((1,3,6,1,4,1,8691,7,6,1,20,1,2,1,2),_EnableQuerier_Type())
enableQuerier.setMaxAccess(_B)
if mibBuilder.loadTexts:enableQuerier.setStatus(_A)
_FixedMulticastQuerierPorts_Type=PortList
_FixedMulticastQuerierPorts_Object=MibTableColumn
fixedMulticastQuerierPorts=_FixedMulticastQuerierPorts_Object((1,3,6,1,4,1,8691,7,6,1,20,1,2,1,3),_FixedMulticastQuerierPorts_Type())
fixedMulticastQuerierPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fixedMulticastQuerierPorts.setStatus(_A)
_LearnedMulticastQuerierPorts_Type=PortList
_LearnedMulticastQuerierPorts_Object=MibTableColumn
learnedMulticastQuerierPorts=_LearnedMulticastQuerierPorts_Object((1,3,6,1,4,1,8691,7,6,1,20,1,2,1,4),_LearnedMulticastQuerierPorts_Type())
learnedMulticastQuerierPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:learnedMulticastQuerierPorts.setStatus(_A)
class _EnableGlobalIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableGlobalIgmpSnooping_Type.__name__=_C
_EnableGlobalIgmpSnooping_Object=MibScalar
enableGlobalIgmpSnooping=_EnableGlobalIgmpSnooping_Object((1,3,6,1,4,1,8691,7,6,1,20,1,4),_EnableGlobalIgmpSnooping_Type())
enableGlobalIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGlobalIgmpSnooping.setStatus(_A)
_StaticMulticast_ObjectIdentity=ObjectIdentity
staticMulticast=_StaticMulticast_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,20,2))
_StaticMulticastTable_Object=MibTable
staticMulticastTable=_StaticMulticastTable_Object((1,3,6,1,4,1,8691,7,6,1,20,2,1))
if mibBuilder.loadTexts:staticMulticastTable.setStatus(_A)
_StaticMulticastEntry_Object=MibTableRow
staticMulticastEntry=_StaticMulticastEntry_Object((1,3,6,1,4,1,8691,7,6,1,20,2,1,1))
staticMulticastEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:staticMulticastEntry.setStatus(_A)
_StaticMulticastAddress_Type=MacAddress
_StaticMulticastAddress_Object=MibTableColumn
staticMulticastAddress=_StaticMulticastAddress_Object((1,3,6,1,4,1,8691,7,6,1,20,2,1,1,1),_StaticMulticastAddress_Type())
staticMulticastAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:staticMulticastAddress.setStatus(_A)
_StaticMulticastPorts_Type=PortList
_StaticMulticastPorts_Object=MibTableColumn
staticMulticastPorts=_StaticMulticastPorts_Object((1,3,6,1,4,1,8691,7,6,1,20,2,1,1,2),_StaticMulticastPorts_Type())
staticMulticastPorts.setMaxAccess(_P)
if mibBuilder.loadTexts:staticMulticastPorts.setStatus(_A)
class _StaticMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_o,1),(_A7,4),(_A8,5),('destroy',6)))
_StaticMulticastStatus_Type.__name__=_C
_StaticMulticastStatus_Object=MibTableColumn
staticMulticastStatus=_StaticMulticastStatus_Object((1,3,6,1,4,1,8691,7,6,1,20,2,1,1,3),_StaticMulticastStatus_Type())
staticMulticastStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:staticMulticastStatus.setStatus(_A)
_Gmrp_ObjectIdentity=ObjectIdentity
gmrp=_Gmrp_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,20,3))
_GmrpSettingTable_Object=MibTable
gmrpSettingTable=_GmrpSettingTable_Object((1,3,6,1,4,1,8691,7,6,1,20,3,1))
if mibBuilder.loadTexts:gmrpSettingTable.setStatus(_A)
_GmrpSettingEntry_Object=MibTableRow
gmrpSettingEntry=_GmrpSettingEntry_Object((1,3,6,1,4,1,8691,7,6,1,20,3,1,1))
gmrpSettingEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:gmrpSettingEntry.setStatus(_A)
class _EnableGMRP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableGMRP_Type.__name__=_C
_EnableGMRP_Object=MibTableColumn
enableGMRP=_EnableGMRP_Object((1,3,6,1,4,1,8691,7,6,1,20,3,1,1,1),_EnableGMRP_Type())
enableGMRP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGMRP.setStatus(_A)
_GmrpTable_Object=MibTable
gmrpTable=_GmrpTable_Object((1,3,6,1,4,1,8691,7,6,1,20,3,2))
if mibBuilder.loadTexts:gmrpTable.setStatus(_A)
_GmrpEntry_Object=MibTableRow
gmrpEntry=_GmrpEntry_Object((1,3,6,1,4,1,8691,7,6,1,20,3,2,1))
gmrpEntry.setIndexNames((0,_G,_A9))
if mibBuilder.loadTexts:gmrpEntry.setStatus(_A)
_GmrpMulticastGroup_Type=MacAddress
_GmrpMulticastGroup_Object=MibTableColumn
gmrpMulticastGroup=_GmrpMulticastGroup_Object((1,3,6,1,4,1,8691,7,6,1,20,3,2,1,1),_GmrpMulticastGroup_Type())
gmrpMulticastGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:gmrpMulticastGroup.setStatus(_A)
_GmrpFixedPorts_Type=PortList
_GmrpFixedPorts_Object=MibTableColumn
gmrpFixedPorts=_GmrpFixedPorts_Object((1,3,6,1,4,1,8691,7,6,1,20,3,2,1,2),_GmrpFixedPorts_Type())
gmrpFixedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:gmrpFixedPorts.setStatus(_A)
_GmrpLearnedPorts_Type=PortList
_GmrpLearnedPorts_Object=MibTableColumn
gmrpLearnedPorts=_GmrpLearnedPorts_Object((1,3,6,1,4,1,8691,7,6,1,20,3,2,1,3),_GmrpLearnedPorts_Type())
gmrpLearnedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:gmrpLearnedPorts.setStatus(_A)
_RateLimiting_ObjectIdentity=ObjectIdentity
rateLimiting=_RateLimiting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,21))
_NormalModeRateLimitingIngressTable_Object=MibTable
normalModeRateLimitingIngressTable=_NormalModeRateLimitingIngressTable_Object((1,3,6,1,4,1,8691,7,6,1,21,1))
if mibBuilder.loadTexts:normalModeRateLimitingIngressTable.setStatus(_A)
_NormalModeRateLimitingIngressEntry_Object=MibTableRow
normalModeRateLimitingIngressEntry=_NormalModeRateLimitingIngressEntry_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1))
normalModeRateLimitingIngressEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:normalModeRateLimitingIngressEntry.setStatus(_A)
class _LimitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('bmucast',1),('bmcast',2),('bcast',3)))
_LimitMode_Type.__name__=_C
_LimitMode_Object=MibTableColumn
limitMode=_LimitMode_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1,1),_LimitMode_Type())
limitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:limitMode.setStatus(_A)
class _LowPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,0),(_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7)))
_LowPriLimitRate_Type.__name__=_C
_LowPriLimitRate_Object=MibTableColumn
lowPriLimitRate=_LowPriLimitRate_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1,2),_LowPriLimitRate_Type())
lowPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:lowPriLimitRate.setStatus(_A)
class _NormalPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_b,0),(_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_v,8)))
_NormalPriLimitRate_Type.__name__=_C
_NormalPriLimitRate_Object=MibTableColumn
normalPriLimitRate=_NormalPriLimitRate_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1,3),_NormalPriLimitRate_Type())
normalPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:normalPriLimitRate.setStatus(_A)
class _MediumPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_b,0),(_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_v,8),('limit32M',9)))
_MediumPriLimitRate_Type.__name__=_C
_MediumPriLimitRate_Object=MibTableColumn
mediumPriLimitRate=_MediumPriLimitRate_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1,4),_MediumPriLimitRate_Type())
mediumPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mediumPriLimitRate.setStatus(_A)
class _HighPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_b,0),(_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_v,8),('limit32M',9),('limit64M',10)))
_HighPriLimitRate_Type.__name__=_C
_HighPriLimitRate_Object=MibTableColumn
highPriLimitRate=_HighPriLimitRate_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1,5),_HighPriLimitRate_Type())
highPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:highPriLimitRate.setStatus(_A)
class _EgressLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_AA,0),('percentage03',1),('percentage05',2),('percentage10',3),('percentage15',4),('percentage25',5),('percentage35',6),('percentage50',7),('percentage65',8),('percentage85',9)))
_EgressLimit_Type.__name__=_C
_EgressLimit_Object=MibTableColumn
egressLimit=_EgressLimit_Object((1,3,6,1,4,1,8691,7,6,1,21,1,1,6),_EgressLimit_Type())
egressLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:egressLimit.setStatus(_A)
_PortDisableMode_ObjectIdentity=ObjectIdentity
portDisableMode=_PortDisableMode_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,21,3))
class _PortDisableModePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PortDisableModePeriod_Type.__name__=_C
_PortDisableModePeriod_Object=MibScalar
portDisableModePeriod=_PortDisableModePeriod_Object((1,3,6,1,4,1,8691,7,6,1,21,3,1),_PortDisableModePeriod_Type())
portDisableModePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:portDisableModePeriod.setStatus(_A)
_PortDisableModeTable_Object=MibTable
portDisableModeTable=_PortDisableModeTable_Object((1,3,6,1,4,1,8691,7,6,1,21,3,2))
if mibBuilder.loadTexts:portDisableModeTable.setStatus(_A)
_PortDisableModeEntry_Object=MibTableRow
portDisableModeEntry=_PortDisableModeEntry_Object((1,3,6,1,4,1,8691,7,6,1,21,3,2,1))
portDisableModeEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:portDisableModeEntry.setStatus(_A)
class _IngressLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_AA,0),('rateMega1Fps4464',1),('rateMega2Fps7441',2),('rateMega3Fps14881',3),('rateMega4Fps22322',4),('rateMega5Fps37203',5),('rateMega6Fps52084',6),('rateMega7Fps74405',7),('rateGiga1Fps44640',8),('rateGiga2Fps74410',9),('rateGiga3Fps148810',10),('rateGiga4Fps223220',11),('rateGiga5Fps372030',12),('rateGiga6Fps520840',13),('rateGiga7Fps744050',14)))
_IngressLimit_Type.__name__=_C
_IngressLimit_Object=MibTableColumn
ingressLimit=_IngressLimit_Object((1,3,6,1,4,1,8691,7,6,1,21,3,2,1,1),_IngressLimit_Type())
ingressLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressLimit.setStatus(_A)
class _RateLimitingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),('portDisable',1)))
_RateLimitingMode_Type.__name__=_C
_RateLimitingMode_Object=MibScalar
rateLimitingMode=_RateLimitingMode_Object((1,3,6,1,4,1,8691,7,6,1,21,4),_RateLimitingMode_Type())
rateLimitingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitingMode.setStatus(_A)
_AccessibleIP_ObjectIdentity=ObjectIdentity
accessibleIP=_AccessibleIP_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,30))
class _EnableAccessibleIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableAccessibleIP_Type.__name__=_C
_EnableAccessibleIP_Object=MibScalar
enableAccessibleIP=_EnableAccessibleIP_Object((1,3,6,1,4,1,8691,7,6,1,30,1),_EnableAccessibleIP_Type())
enableAccessibleIP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAccessibleIP.setStatus(_A)
_AccessibleIpTable_Object=MibTable
accessibleIpTable=_AccessibleIpTable_Object((1,3,6,1,4,1,8691,7,6,1,30,2))
if mibBuilder.loadTexts:accessibleIpTable.setStatus(_A)
_AccessibleIpEntry_Object=MibTableRow
accessibleIpEntry=_AccessibleIpEntry_Object((1,3,6,1,4,1,8691,7,6,1,30,2,1))
accessibleIpEntry.setIndexNames((0,_G,_AB))
if mibBuilder.loadTexts:accessibleIpEntry.setStatus(_A)
_AccessibleIpAddress_Type=IpAddress
_AccessibleIpAddress_Object=MibTableColumn
accessibleIpAddress=_AccessibleIpAddress_Object((1,3,6,1,4,1,8691,7,6,1,30,2,1,1),_AccessibleIpAddress_Type())
accessibleIpAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:accessibleIpAddress.setStatus(_A)
_AccessibleIpNetMask_Type=IpAddress
_AccessibleIpNetMask_Object=MibTableColumn
accessibleIpNetMask=_AccessibleIpNetMask_Object((1,3,6,1,4,1,8691,7,6,1,30,2,1,2),_AccessibleIpNetMask_Type())
accessibleIpNetMask.setMaxAccess(_P)
if mibBuilder.loadTexts:accessibleIpNetMask.setStatus(_A)
class _AccessibleIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_o,1),(_A7,4),(_A8,5),('destroy',6)))
_AccessibleIpStatus_Type.__name__=_C
_AccessibleIpStatus_Object=MibTableColumn
accessibleIpStatus=_AccessibleIpStatus_Object((1,3,6,1,4,1,8691,7,6,1,30,2,1,3),_AccessibleIpStatus_Type())
accessibleIpStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:accessibleIpStatus.setStatus(_A)
_SysFileUpdate_ObjectIdentity=ObjectIdentity
sysFileUpdate=_SysFileUpdate_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,31))
_TftpServer_Type=DisplayString
_TftpServer_Object=MibScalar
tftpServer=_TftpServer_Object((1,3,6,1,4,1,8691,7,6,1,31,1),_TftpServer_Type())
tftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpServer.setStatus(_A)
_FirmwarePathName_Type=DisplayString
_FirmwarePathName_Object=MibScalar
firmwarePathName=_FirmwarePathName_Object((1,3,6,1,4,1,8691,7,6,1,31,2),_FirmwarePathName_Type())
firmwarePathName.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwarePathName.setStatus(_A)
_LogPathName_Type=DisplayString
_LogPathName_Object=MibScalar
logPathName=_LogPathName_Object((1,3,6,1,4,1,8691,7,6,1,31,3),_LogPathName_Type())
logPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:logPathName.setStatus(_A)
_ConfPathName_Type=DisplayString
_ConfPathName_Object=MibScalar
confPathName=_ConfPathName_Object((1,3,6,1,4,1,8691,7,6,1,31,4),_ConfPathName_Type())
confPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:confPathName.setStatus(_A)
class _TftpUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('importFirmware',1),('importConfig',2),('exportConfig',3),('exportLog',4)))
_TftpUpdate_Type.__name__=_C
_TftpUpdate_Object=MibScalar
tftpUpdate=_TftpUpdate_Object((1,3,6,1,4,1,8691,7,6,1,31,5),_TftpUpdate_Type())
tftpUpdate.setMaxAccess(_P)
if mibBuilder.loadTexts:tftpUpdate.setStatus(_A)
_TimeSetting_ObjectIdentity=ObjectIdentity
timeSetting=_TimeSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,32))
_SysDateTime_Type=DateAndTime
_SysDateTime_Object=MibScalar
sysDateTime=_SysDateTime_Object((1,3,6,1,4,1,8691,7,6,1,32,1),_SysDateTime_Type())
sysDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDateTime.setStatus(_A)
_CalibratePeriod_Type=Integer32
_CalibratePeriod_Object=MibScalar
calibratePeriod=_CalibratePeriod_Object((1,3,6,1,4,1,8691,7,6,1,32,2),_CalibratePeriod_Type())
calibratePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:calibratePeriod.setStatus(_A)
_TimeServer1_Type=DisplayString
_TimeServer1_Object=MibScalar
timeServer1=_TimeServer1_Object((1,3,6,1,4,1,8691,7,6,1,32,3),_TimeServer1_Type())
timeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer1.setStatus(_A)
_TimeServer2_Type=DisplayString
_TimeServer2_Object=MibScalar
timeServer2=_TimeServer2_Object((1,3,6,1,4,1,8691,7,6,1,32,4),_TimeServer2_Type())
timeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer2.setStatus(_A)
_DaylightSaving_ObjectIdentity=ObjectIdentity
daylightSaving=_DaylightSaving_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,32,5))
class _StartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_H,0),('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_StartMonth_Type.__name__=_C
_StartMonth_Object=MibScalar
startMonth=_StartMonth_Object((1,3,6,1,4,1,8691,7,6,1,32,5,1),_StartMonth_Type())
startMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:startMonth.setStatus(_A)
class _StartWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6)));namedValues=NamedValues(*((_H,0),('week1',1),('week2',2),('week3',3),('week4',4),('weeklast',6)))
_StartWeek_Type.__name__=_C
_StartWeek_Object=MibScalar
startWeek=_StartWeek_Object((1,3,6,1,4,1,8691,7,6,1,32,5,2),_StartWeek_Type())
startWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:startWeek.setStatus(_A)
class _StartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_StartDay_Type.__name__=_C
_StartDay_Object=MibScalar
startDay=_StartDay_Object((1,3,6,1,4,1,8691,7,6,1,32,5,3),_StartDay_Type())
startDay.setMaxAccess(_B)
if mibBuilder.loadTexts:startDay.setStatus(_A)
_StartHour_Type=Integer32
_StartHour_Object=MibScalar
startHour=_StartHour_Object((1,3,6,1,4,1,8691,7,6,1,32,5,4),_StartHour_Type())
startHour.setMaxAccess(_B)
if mibBuilder.loadTexts:startHour.setStatus(_A)
class _EndMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_H,0),('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_EndMonth_Type.__name__=_C
_EndMonth_Object=MibScalar
endMonth=_EndMonth_Object((1,3,6,1,4,1,8691,7,6,1,32,5,5),_EndMonth_Type())
endMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:endMonth.setStatus(_A)
class _EndWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6)));namedValues=NamedValues(*((_H,0),('week1',1),('week2',2),('week3',3),('week4',4),('weeklast',6)))
_EndWeek_Type.__name__=_C
_EndWeek_Object=MibScalar
endWeek=_EndWeek_Object((1,3,6,1,4,1,8691,7,6,1,32,5,6),_EndWeek_Type())
endWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:endWeek.setStatus(_A)
class _EndDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_EndDay_Type.__name__=_C
_EndDay_Object=MibScalar
endDay=_EndDay_Object((1,3,6,1,4,1,8691,7,6,1,32,5,7),_EndDay_Type())
endDay.setMaxAccess(_B)
if mibBuilder.loadTexts:endDay.setStatus(_A)
_EndHour_Type=Integer32
_EndHour_Object=MibScalar
endHour=_EndHour_Object((1,3,6,1,4,1,8691,7,6,1,32,5,8),_EndHour_Type())
endHour.setMaxAccess(_B)
if mibBuilder.loadTexts:endHour.setStatus(_A)
_OffsetHours_Type=Integer32
_OffsetHours_Object=MibScalar
offsetHours=_OffsetHours_Object((1,3,6,1,4,1,8691,7,6,1,32,5,9),_OffsetHours_Type())
offsetHours.setMaxAccess(_B)
if mibBuilder.loadTexts:offsetHours.setStatus(_A)
class _EnableNTPServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableNTPServer_Type.__name__=_C
_EnableNTPServer_Object=MibScalar
enableNTPServer=_EnableNTPServer_Object((1,3,6,1,4,1,8691,7,6,1,32,6),_EnableNTPServer_Type())
enableNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:enableNTPServer.setStatus(_A)
class _TimeProtocolOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('sntp',1),('ntp',2)))
_TimeProtocolOption_Type.__name__=_C
_TimeProtocolOption_Object=MibScalar
timeProtocolOption=_TimeProtocolOption_Object((1,3,6,1,4,1,8691,7,6,1,32,7),_TimeProtocolOption_Type())
timeProtocolOption.setMaxAccess(_B)
if mibBuilder.loadTexts:timeProtocolOption.setStatus(_A)
_DipSwitchSetting_ObjectIdentity=ObjectIdentity
dipSwitchSetting=_DipSwitchSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,34))
class _DipSwitchEnableTurboRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DipSwitchEnableTurboRing_Type.__name__=_C
_DipSwitchEnableTurboRing_Object=MibScalar
dipSwitchEnableTurboRing=_DipSwitchEnableTurboRing_Object((1,3,6,1,4,1,8691,7,6,1,34,1),_DipSwitchEnableTurboRing_Type())
dipSwitchEnableTurboRing.setMaxAccess(_B)
if mibBuilder.loadTexts:dipSwitchEnableTurboRing.setStatus(_A)
class _DipSwitchTurboRingPole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_DipSwitchTurboRingPole_Type.__name__=_C
_DipSwitchTurboRingPole_Object=MibScalar
dipSwitchTurboRingPole=_DipSwitchTurboRingPole_Object((1,3,6,1,4,1,8691,7,6,1,34,2),_DipSwitchTurboRingPole_Type())
dipSwitchTurboRingPole.setMaxAccess(_D)
if mibBuilder.loadTexts:dipSwitchTurboRingPole.setStatus(_A)
class _DipSwitchRingCouplingPole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_DipSwitchRingCouplingPole_Type.__name__=_C
_DipSwitchRingCouplingPole_Object=MibScalar
dipSwitchRingCouplingPole=_DipSwitchRingCouplingPole_Object((1,3,6,1,4,1,8691,7,6,1,34,3),_DipSwitchRingCouplingPole_Type())
dipSwitchRingCouplingPole.setMaxAccess(_D)
if mibBuilder.loadTexts:dipSwitchRingCouplingPole.setStatus(_A)
class _DipSwitchRingMasterPole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_DipSwitchRingMasterPole_Type.__name__=_C
_DipSwitchRingMasterPole_Object=MibScalar
dipSwitchRingMasterPole=_DipSwitchRingMasterPole_Object((1,3,6,1,4,1,8691,7,6,1,34,4),_DipSwitchRingMasterPole_Type())
dipSwitchRingMasterPole.setMaxAccess(_D)
if mibBuilder.loadTexts:dipSwitchRingMasterPole.setStatus(_A)
_BackupMediaSetting_ObjectIdentity=ObjectIdentity
backupMediaSetting=_BackupMediaSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,35))
class _BackupMediaAutoLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_BackupMediaAutoLoad_Type.__name__=_C
_BackupMediaAutoLoad_Object=MibScalar
backupMediaAutoLoad=_BackupMediaAutoLoad_Object((1,3,6,1,4,1,8691,7,6,1,35,1),_BackupMediaAutoLoad_Type())
backupMediaAutoLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:backupMediaAutoLoad.setStatus(_A)
class _EnableWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_EnableWarmStart_Type.__name__=_C
_EnableWarmStart_Object=MibScalar
enableWarmStart=_EnableWarmStart_Object((1,3,6,1,4,1,8691,7,6,1,36),_EnableWarmStart_Type())
enableWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:enableWarmStart.setStatus(_A)
_SyslogSetting_ObjectIdentity=ObjectIdentity
syslogSetting=_SyslogSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,37))
_SyslogServer1_Type=DisplayString
_SyslogServer1_Object=MibScalar
syslogServer1=_SyslogServer1_Object((1,3,6,1,4,1,8691,7,6,1,37,1),_SyslogServer1_Type())
syslogServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer1.setStatus(_A)
_SyslogServer1port_Type=Integer32
_SyslogServer1port_Object=MibScalar
syslogServer1port=_SyslogServer1port_Object((1,3,6,1,4,1,8691,7,6,1,37,2),_SyslogServer1port_Type())
syslogServer1port.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer1port.setStatus(_A)
_SyslogServer2_Type=DisplayString
_SyslogServer2_Object=MibScalar
syslogServer2=_SyslogServer2_Object((1,3,6,1,4,1,8691,7,6,1,37,3),_SyslogServer2_Type())
syslogServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer2.setStatus(_A)
_SyslogServer2port_Type=Integer32
_SyslogServer2port_Object=MibScalar
syslogServer2port=_SyslogServer2port_Object((1,3,6,1,4,1,8691,7,6,1,37,4),_SyslogServer2port_Type())
syslogServer2port.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer2port.setStatus(_A)
_SyslogServer3_Type=DisplayString
_SyslogServer3_Object=MibScalar
syslogServer3=_SyslogServer3_Object((1,3,6,1,4,1,8691,7,6,1,37,5),_SyslogServer3_Type())
syslogServer3.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer3.setStatus(_A)
_SyslogServer3port_Type=Integer32
_SyslogServer3port_Object=MibScalar
syslogServer3port=_SyslogServer3port_Object((1,3,6,1,4,1,8691,7,6,1,37,6),_SyslogServer3port_Type())
syslogServer3port.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServer3port.setStatus(_A)
_DhcpRelayAgentSetting_ObjectIdentity=ObjectIdentity
dhcpRelayAgentSetting=_DhcpRelayAgentSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,39))
_DhcpServer1_Type=DisplayString
_DhcpServer1_Object=MibScalar
dhcpServer1=_DhcpServer1_Object((1,3,6,1,4,1,8691,7,6,1,39,1),_DhcpServer1_Type())
dhcpServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer1.setStatus(_A)
_DhcpServer2_Type=DisplayString
_DhcpServer2_Object=MibScalar
dhcpServer2=_DhcpServer2_Object((1,3,6,1,4,1,8691,7,6,1,39,2),_DhcpServer2_Type())
dhcpServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer2.setStatus(_A)
_DhcpServer3_Type=DisplayString
_DhcpServer3_Object=MibScalar
dhcpServer3=_DhcpServer3_Object((1,3,6,1,4,1,8691,7,6,1,39,3),_DhcpServer3_Type())
dhcpServer3.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer3.setStatus(_A)
_DhcpServer4_Type=DisplayString
_DhcpServer4_Object=MibScalar
dhcpServer4=_DhcpServer4_Object((1,3,6,1,4,1,8691,7,6,1,39,4),_DhcpServer4_Type())
dhcpServer4.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServer4.setStatus(_A)
_Option82Setting_ObjectIdentity=ObjectIdentity
option82Setting=_Option82Setting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,39,5))
class _EnableOption82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableOption82_Type.__name__=_C
_EnableOption82_Object=MibScalar
enableOption82=_EnableOption82_Object((1,3,6,1,4,1,8691,7,6,1,39,5,1),_EnableOption82_Type())
enableOption82.setMaxAccess(_B)
if mibBuilder.loadTexts:enableOption82.setStatus(_A)
class _Option82Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ip',0),('mac',1),('client-id',2),('other',3)))
_Option82Type_Type.__name__=_C
_Option82Type_Object=MibScalar
option82Type=_Option82Type_Object((1,3,6,1,4,1,8691,7,6,1,39,5,2),_Option82Type_Type())
option82Type.setMaxAccess(_B)
if mibBuilder.loadTexts:option82Type.setStatus(_A)
_Option82Value_Type=DisplayString
_Option82Value_Object=MibScalar
option82Value=_Option82Value_Object((1,3,6,1,4,1,8691,7,6,1,39,5,3),_Option82Value_Type())
option82Value.setMaxAccess(_B)
if mibBuilder.loadTexts:option82Value.setStatus(_A)
_Option82ValueDisplay_Type=DisplayString
_Option82ValueDisplay_Object=MibScalar
option82ValueDisplay=_Option82ValueDisplay_Object((1,3,6,1,4,1,8691,7,6,1,39,5,4),_Option82ValueDisplay_Type())
option82ValueDisplay.setMaxAccess(_D)
if mibBuilder.loadTexts:option82ValueDisplay.setStatus(_A)
_DhcpFunctionTable_Object=MibTable
dhcpFunctionTable=_DhcpFunctionTable_Object((1,3,6,1,4,1,8691,7,6,1,39,6))
if mibBuilder.loadTexts:dhcpFunctionTable.setStatus(_A)
_DhcpFunctionEntry_Object=MibTableRow
dhcpFunctionEntry=_DhcpFunctionEntry_Object((1,3,6,1,4,1,8691,7,6,1,39,6,1))
dhcpFunctionEntry.setIndexNames((0,_G,_AC))
if mibBuilder.loadTexts:dhcpFunctionEntry.setStatus(_A)
_DhcpPortIndex_Type=Integer32
_DhcpPortIndex_Object=MibTableColumn
dhcpPortIndex=_DhcpPortIndex_Object((1,3,6,1,4,1,8691,7,6,1,39,6,1,1),_DhcpPortIndex_Type())
dhcpPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpPortIndex.setStatus(_A)
_CircuitID_Type=DisplayString
_CircuitID_Object=MibTableColumn
circuitID=_CircuitID_Object((1,3,6,1,4,1,8691,7,6,1,39,6,1,2),_CircuitID_Type())
circuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:circuitID.setStatus(_A)
class _Option82Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Option82Enable_Type.__name__=_C
_Option82Enable_Object=MibTableColumn
option82Enable=_Option82Enable_Object((1,3,6,1,4,1,8691,7,6,1,39,6,1,3),_Option82Enable_Type())
option82Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:option82Enable.setStatus(_A)
_Diagnosis_ObjectIdentity=ObjectIdentity
diagnosis=_Diagnosis_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,42))
_LldpSetting_ObjectIdentity=ObjectIdentity
lldpSetting=_LldpSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,42,1))
class _EnableLLDP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableLLDP_Type.__name__=_C
_EnableLLDP_Object=MibScalar
enableLLDP=_EnableLLDP_Object((1,3,6,1,4,1,8691,7,6,1,42,1,1),_EnableLLDP_Type())
enableLLDP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableLLDP.setStatus(_A)
_LldpMSGInterval_Type=Integer32
_LldpMSGInterval_Object=MibScalar
lldpMSGInterval=_LldpMSGInterval_Object((1,3,6,1,4,1,8691,7,6,1,42,1,2),_LldpMSGInterval_Type())
lldpMSGInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpMSGInterval.setStatus(_A)
_WebTimeout_Type=Integer32
_WebTimeout_Object=MibScalar
webTimeout=_WebTimeout_Object((1,3,6,1,4,1,8691,7,6,1,43),_WebTimeout_Type())
webTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:webTimeout.setStatus(_A)
_AgeTime_Type=Integer32
_AgeTime_Object=MibScalar
ageTime=_AgeTime_Object((1,3,6,1,4,1,8691,7,6,1,44),_AgeTime_Type())
ageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ageTime.setStatus(_A)
_GarpSetting_ObjectIdentity=ObjectIdentity
garpSetting=_GarpSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,45))
_JoinTime_Type=Integer32
_JoinTime_Object=MibScalar
joinTime=_JoinTime_Object((1,3,6,1,4,1,8691,7,6,1,45,1),_JoinTime_Type())
joinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:joinTime.setStatus(_A)
_LeaveTime_Type=Integer32
_LeaveTime_Object=MibScalar
leaveTime=_LeaveTime_Object((1,3,6,1,4,1,8691,7,6,1,45,2),_LeaveTime_Type())
leaveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:leaveTime.setStatus(_A)
_LeaveAllTime_Type=Integer32
_LeaveAllTime_Object=MibScalar
leaveAllTime=_LeaveAllTime_Object((1,3,6,1,4,1,8691,7,6,1,45,3),_LeaveAllTime_Type())
leaveAllTime.setMaxAccess(_B)
if mibBuilder.loadTexts:leaveAllTime.setStatus(_A)
_Eventlog_ObjectIdentity=ObjectIdentity
eventlog=_Eventlog_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,46))
_EventlogTable_Object=MibTable
eventlogTable=_EventlogTable_Object((1,3,6,1,4,1,8691,7,6,1,46,1))
if mibBuilder.loadTexts:eventlogTable.setStatus(_A)
_EventlogEntry_Object=MibTableRow
eventlogEntry=_EventlogEntry_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1))
eventlogEntry.setIndexNames((0,_G,_AD))
if mibBuilder.loadTexts:eventlogEntry.setStatus(_A)
_EventlogIndex_Type=Integer32
_EventlogIndex_Object=MibTableColumn
eventlogIndex=_EventlogIndex_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1,1),_EventlogIndex_Type())
eventlogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogIndex.setStatus(_A)
_EventlogBootup_Type=Integer32
_EventlogBootup_Object=MibTableColumn
eventlogBootup=_EventlogBootup_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1,2),_EventlogBootup_Type())
eventlogBootup.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogBootup.setStatus(_A)
_EventlogDate_Type=DisplayString
_EventlogDate_Object=MibTableColumn
eventlogDate=_EventlogDate_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1,3),_EventlogDate_Type())
eventlogDate.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogDate.setStatus(_A)
_EventlogTime_Type=DisplayString
_EventlogTime_Object=MibTableColumn
eventlogTime=_EventlogTime_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1,4),_EventlogTime_Type())
eventlogTime.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogTime.setStatus(_A)
_EventlogUptime_Type=DisplayString
_EventlogUptime_Object=MibTableColumn
eventlogUptime=_EventlogUptime_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1,5),_EventlogUptime_Type())
eventlogUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogUptime.setStatus(_A)
_EventlogEvent_Type=DisplayString
_EventlogEvent_Object=MibTableColumn
eventlogEvent=_EventlogEvent_Object((1,3,6,1,4,1,8691,7,6,1,46,1,1,6),_EventlogEvent_Type())
eventlogEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:eventlogEvent.setStatus(_A)
class _EventlogClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noop',0),('clear',1)))
_EventlogClear_Type.__name__=_C
_EventlogClear_Object=MibScalar
eventlogClear=_EventlogClear_Object((1,3,6,1,4,1,8691,7,6,1,46,2),_EventlogClear_Type())
eventlogClear.setMaxAccess(_B)
if mibBuilder.loadTexts:eventlogClear.setStatus(_A)
_IndustrialProtocol_ObjectIdentity=ObjectIdentity
industrialProtocol=_IndustrialProtocol_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,47))
_EipSetting_ObjectIdentity=ObjectIdentity
eipSetting=_EipSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,47,1))
class _EnableEtherNetIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableEtherNetIP_Type.__name__=_C
_EnableEtherNetIP_Object=MibScalar
enableEtherNetIP=_EnableEtherNetIP_Object((1,3,6,1,4,1,8691,7,6,1,47,1,1),_EnableEtherNetIP_Type())
enableEtherNetIP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableEtherNetIP.setStatus(_A)
_ModbusSetting_ObjectIdentity=ObjectIdentity
modbusSetting=_ModbusSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,47,2))
class _EnableModbus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableModbus_Type.__name__=_C
_EnableModbus_Object=MibScalar
enableModbus=_EnableModbus_Object((1,3,6,1,4,1,8691,7,6,1,47,2,1),_EnableModbus_Type())
enableModbus.setMaxAccess(_B)
if mibBuilder.loadTexts:enableModbus.setStatus(_A)
_ProfinetioSetting_ObjectIdentity=ObjectIdentity
profinetioSetting=_ProfinetioSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,6,1,47,3))
class _EnableProfinetIO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableProfinetIO_Type.__name__=_C
_EnableProfinetIO_Object=MibScalar
enableProfinetIO=_EnableProfinetIO_Object((1,3,6,1,4,1,8691,7,6,1,47,3,1),_EnableProfinetIO_Type())
enableProfinetIO.setMaxAccess(_B)
if mibBuilder.loadTexts:enableProfinetIO.setStatus(_A)
class _EnableFactoryDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('activate',1))
_EnableFactoryDefault_Type.__name__=_C
_EnableFactoryDefault_Object=MibScalar
enableFactoryDefault=_EnableFactoryDefault_Object((1,3,6,1,4,1,8691,7,6,1,48),_EnableFactoryDefault_Type())
enableFactoryDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:enableFactoryDefault.setStatus(_A)
class _ConsoleLoginMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('menu',0),('cli',1)))
_ConsoleLoginMode_Type.__name__=_C
_ConsoleLoginMode_Object=MibScalar
consoleLoginMode=_ConsoleLoginMode_Object((1,3,6,1,4,1,8691,7,6,1,51),_ConsoleLoginMode_Type())
consoleLoginMode.setMaxAccess(_B)
if mibBuilder.loadTexts:consoleLoginMode.setStatus(_A)
_CpuLoading5s_Type=Integer32
_CpuLoading5s_Object=MibScalar
cpuLoading5s=_CpuLoading5s_Object((1,3,6,1,4,1,8691,7,6,1,53),_CpuLoading5s_Type())
cpuLoading5s.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLoading5s.setStatus(_A)
_CpuLoading30s_Type=Integer32
_CpuLoading30s_Object=MibScalar
cpuLoading30s=_CpuLoading30s_Object((1,3,6,1,4,1,8691,7,6,1,54),_CpuLoading30s_Type())
cpuLoading30s.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLoading30s.setStatus(_A)
_CpuLoading300s_Type=Integer32
_CpuLoading300s_Object=MibScalar
cpuLoading300s=_CpuLoading300s_Object((1,3,6,1,4,1,8691,7,6,1,55),_CpuLoading300s_Type())
cpuLoading300s.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuLoading300s.setStatus(_A)
_TotalMemory_Type=Integer32
_TotalMemory_Object=MibScalar
totalMemory=_TotalMemory_Object((1,3,6,1,4,1,8691,7,6,1,56),_TotalMemory_Type())
totalMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:totalMemory.setStatus(_A)
_FreeMemory_Type=Integer32
_FreeMemory_Object=MibScalar
freeMemory=_FreeMemory_Object((1,3,6,1,4,1,8691,7,6,1,57),_FreeMemory_Type())
freeMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:freeMemory.setStatus(_A)
_UsedMemory_Type=Integer32
_UsedMemory_Object=MibScalar
usedMemory=_UsedMemory_Object((1,3,6,1,4,1,8691,7,6,1,58),_UsedMemory_Type())
usedMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:usedMemory.setStatus(_A)
_MemoryUsage_Type=Integer32
_MemoryUsage_Object=MibScalar
memoryUsage=_MemoryUsage_Object((1,3,6,1,4,1,8691,7,6,1,59),_MemoryUsage_Type())
memoryUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryUsage.setStatus(_A)
class _LoopProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LoopProtection_Type.__name__=_C
_LoopProtection_Object=MibScalar
loopProtection=_LoopProtection_Object((1,3,6,1,4,1,8691,7,6,1,61),_LoopProtection_Type())
loopProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:loopProtection.setStatus(_A)
_SwTraps_ObjectIdentity=ObjectIdentity
swTraps=_SwTraps_ObjectIdentity((1,3,6,1,4,1,8691,7,6,2))
class _VarconfigChangeTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('configChanged',2)))
_VarconfigChangeTrap_Type.__name__=_C
_VarconfigChangeTrap_Object=MibScalar
varconfigChangeTrap=_VarconfigChangeTrap_Object((1,3,6,1,4,1,8691,7,6,2,1),_VarconfigChangeTrap_Type())
varconfigChangeTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varconfigChangeTrap.setStatus(_A)
class _Varpower1Trap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_s,2),(_t,3)))
_Varpower1Trap_Type.__name__=_C
_Varpower1Trap_Object=MibScalar
varpower1Trap=_Varpower1Trap_Object((1,3,6,1,4,1,8691,7,6,2,2),_Varpower1Trap_Type())
varpower1Trap.setMaxAccess(_D)
if mibBuilder.loadTexts:varpower1Trap.setStatus(_A)
class _Varpower2Trap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_s,2),(_t,3)))
_Varpower2Trap_Type.__name__=_C
_Varpower2Trap_Object=MibScalar
varpower2Trap=_Varpower2Trap_Object((1,3,6,1,4,1,8691,7,6,2,3),_Varpower2Trap_Type())
varpower2Trap.setMaxAccess(_D)
if mibBuilder.loadTexts:varpower2Trap.setStatus(_A)
_VartrafficOverloadTrap_Type=Integer32
_VartrafficOverloadTrap_Object=MibScalar
vartrafficOverloadTrap=_VartrafficOverloadTrap_Object((1,3,6,1,4,1,8691,7,6,2,4),_VartrafficOverloadTrap_Type())
vartrafficOverloadTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:vartrafficOverloadTrap.setStatus(_A)
class _VarredundancyTopologyChangedTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('topologyChanged',2),('topologyChangedTurboChainHead',3),('topologyChangedTurboChainTail',4)))
_VarredundancyTopologyChangedTrap_Type.__name__=_C
_VarredundancyTopologyChangedTrap_Object=MibScalar
varredundancyTopologyChangedTrap=_VarredundancyTopologyChangedTrap_Object((1,3,6,1,4,1,8691,7,6,2,5),_VarredundancyTopologyChangedTrap_Type())
varredundancyTopologyChangedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varredundancyTopologyChangedTrap.setStatus(_A)
class _VarturboRingCouplingPortChangedTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('couplingPortChanged',2)))
_VarturboRingCouplingPortChangedTrap_Type.__name__=_C
_VarturboRingCouplingPortChangedTrap_Object=MibScalar
varturboRingCouplingPortChangedTrap=_VarturboRingCouplingPortChangedTrap_Object((1,3,6,1,4,1,8691,7,6,2,6),_VarturboRingCouplingPortChangedTrap_Type())
varturboRingCouplingPortChangedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varturboRingCouplingPortChangedTrap.setStatus(_A)
class _VarturboRingMasterChangedTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('ringMasterChanged',2)))
_VarturboRingMasterChangedTrap_Type.__name__=_C
_VarturboRingMasterChangedTrap_Object=MibScalar
varturboRingMasterChangedTrap=_VarturboRingMasterChangedTrap_Object((1,3,6,1,4,1,8691,7,6,2,7),_VarturboRingMasterChangedTrap_Type())
varturboRingMasterChangedTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varturboRingMasterChangedTrap.setStatus(_A)
_VarLLDPChgTrap_Type=Integer32
_VarLLDPChgTrap_Object=MibScalar
varLLDPChgTrap=_VarLLDPChgTrap_Object((1,3,6,1,4,1,8691,7,6,2,19),_VarLLDPChgTrap_Type())
varLLDPChgTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:varLLDPChgTrap.setStatus(_A)
configChangeTrap=NotificationType((1,3,6,1,4,1,8691,7,6,0,1))
configChangeTrap.setObjects((_G,_AE))
if mibBuilder.loadTexts:configChangeTrap.setStatus(_A)
power1Trap=NotificationType((1,3,6,1,4,1,8691,7,6,0,2))
power1Trap.setObjects((_G,_AF))
if mibBuilder.loadTexts:power1Trap.setStatus(_A)
power2Trap=NotificationType((1,3,6,1,4,1,8691,7,6,0,3))
power2Trap.setObjects((_G,_AG))
if mibBuilder.loadTexts:power2Trap.setStatus(_A)
trafficOverloadTrap=NotificationType((1,3,6,1,4,1,8691,7,6,0,4))
trafficOverloadTrap.setObjects((_G,_AH))
if mibBuilder.loadTexts:trafficOverloadTrap.setStatus(_A)
redundancyTopologyChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,6,0,5))
redundancyTopologyChangedTrap.setObjects((_G,_AI))
if mibBuilder.loadTexts:redundancyTopologyChangedTrap.setStatus(_A)
turboRingCouplingPortChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,6,0,6))
turboRingCouplingPortChangedTrap.setObjects((_G,_AJ))
if mibBuilder.loadTexts:turboRingCouplingPortChangedTrap.setStatus(_A)
turboRingMasterChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,6,0,7))
turboRingMasterChangedTrap.setObjects((_G,_AK))
if mibBuilder.loadTexts:turboRingMasterChangedTrap.setStatus(_A)
lldpChgTrap=NotificationType((1,3,6,1,4,1,8691,7,6,0,19))
lldpChgTrap.setObjects((_G,_AL))
if mibBuilder.loadTexts:lldpChgTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'PortList':PortList,'moxa':moxa,'industrialEthernet':industrialEthernet,'eds405a':eds405a,'mibNotificationsPrefix':mibNotificationsPrefix,'configChangeTrap':configChangeTrap,'power1Trap':power1Trap,'power2Trap':power2Trap,'trafficOverloadTrap':trafficOverloadTrap,'redundancyTopologyChangedTrap':redundancyTopologyChangedTrap,'turboRingCouplingPortChangedTrap':turboRingCouplingPortChangedTrap,'turboRingMasterChangedTrap':turboRingMasterChangedTrap,'lldpChgTrap':lldpChgTrap,'swMgmt':swMgmt,'numberOfPorts':numberOfPorts,'switchModel':switchModel,'firmwareVersion':firmwareVersion,'enableWebConfig':enableWebConfig,'enableTelnetConsole':enableTelnetConsole,'lineSwapRecovery':lineSwapRecovery,'networkSetting':networkSetting,'switchIpAddr':switchIpAddr,'switchIpMask':switchIpMask,'defaultGateway':defaultGateway,'enableAutoIpConfig':enableAutoIpConfig,'dnsServer1IpAddr':dnsServer1IpAddr,'snmpTrapCommunity':snmpTrapCommunity,'trapServerAddr':trapServerAddr,'dnsServer2IpAddr':dnsServer2IpAddr,'snmpReadCommunity':snmpReadCommunity,'snmpTrap2Community':snmpTrap2Community,'trap2ServerAddr':trap2ServerAddr,'snmpInformEnable':snmpInformEnable,'snmpInformRetries':snmpInformRetries,'snmpInformTimeout':snmpInformTimeout,'dhcpRetryPeriods':dhcpRetryPeriods,'dhcpRetryTimes':dhcpRetryTimes,'portSetting':portSetting,'portTable':portTable,'portEntry':portEntry,_L:portIndex,'portDesc':portDesc,'portEnable':portEnable,'portSpeed':portSpeed,'portMDI':portMDI,'portFDXFlowCtrl':portFDXFlowCtrl,'portName':portName,'portSubdesc':portSubdesc,'monitor':monitor,'power1InputStatus':power1InputStatus,'power2InputStatus':power2InputStatus,'monitorPortTable':monitorPortTable,'monitorPortEntry':monitorPortEntry,'monitorLinkStatus':monitorLinkStatus,'monitorSpeed':monitorSpeed,'monitorAutoMDI':monitorAutoMDI,'monitorTraffic':monitorTraffic,'monitorFDXFlowCtrl':monitorFDXFlowCtrl,'monitorTxTraffic':monitorTxTraffic,'monitorRxTraffic':monitorRxTraffic,'emailWarning':emailWarning,'emailService':emailService,'emailWarningMailServer':emailWarningMailServer,'emailWarningFirstEmailAddr':emailWarningFirstEmailAddr,'emailWarningSecondEmailAddr':emailWarningSecondEmailAddr,'emailWarningThirdEmailAddr':emailWarningThirdEmailAddr,'emailWarningFourthEmailAddr':emailWarningFourthEmailAddr,'emailWarningSMTPPort':emailWarningSMTPPort,'emailWarningEventType':emailWarningEventType,'emailWarningEventServerColdStart':emailWarningEventServerColdStart,'emailWarningEventServerWarmStart':emailWarningEventServerWarmStart,'emailWarningEventConfigChange':emailWarningEventConfigChange,'emailWarningEventPowerOn2Off':emailWarningEventPowerOn2Off,'emailWarningEventPowerOff2On':emailWarningEventPowerOff2On,'emailWarningEventAuthFail':emailWarningEventAuthFail,'emailWarningEventTopologyChanged':emailWarningEventTopologyChanged,'emailWarningEventPortTable':emailWarningEventPortTable,'emailWarningEventPortEntry':emailWarningEventPortEntry,'emailWarningEventPortLinkOn':emailWarningEventPortLinkOn,'emailWarningEventPortLinkOff':emailWarningEventPortLinkOff,'emailWarningEventPortTrafficOverload':emailWarningEventPortTrafficOverload,'emailWarningEventPortRxTrafficThreshold':emailWarningEventPortRxTrafficThreshold,'emailWarningEventPortTrafficDuration':emailWarningEventPortTrafficDuration,'setDeviceIp':setDeviceIp,'setDevIpTable':setDevIpTable,'setDevIpEntry':setDevIpEntry,_A1:setDevIpIndex,'setDevIpCurrentIpofDevice':setDevIpCurrentIpofDevice,'setDevIpPresentBy':setDevIpPresentBy,'setDevIpDedicatedIp':setDevIpDedicatedIp,'mirroring':mirroring,'targetPort':targetPort,'mirroringPort':mirroringPort,'monitorDirection':monitorDirection,'commRedundancy':commRedundancy,'protocolOfRedundancySetup':protocolOfRedundancySetup,_l:turboRing,'turboRingMaster':turboRingMaster,'turboRingMasterSetup':turboRingMasterSetup,'turboRingPortTable':turboRingPortTable,'turboRingPortEntry':turboRingPortEntry,_A2:turboRingPortIndex,'turboRingPortStatus':turboRingPortStatus,'turboRingPortDesignatedBridge':turboRingPortDesignatedBridge,'turboRingPortDesignatedPort':turboRingPortDesignatedPort,'turboRingDesignatedMaster':turboRingDesignatedMaster,'turboRingRdntPort1':turboRingRdntPort1,'turboRingRdntPort2':turboRingRdntPort2,'turboRingEnableCoupling':turboRingEnableCoupling,'turboRingCouplingPort':turboRingCouplingPort,'turboRingCouplingPortStatus':turboRingCouplingPortStatus,'turboRingControlPort':turboRingControlPort,'turboRingControlPortStatus':turboRingControlPortStatus,'turboRingBrokenStatus':turboRingBrokenStatus,_k:spanningTree,'spanningTreeRoot':spanningTreeRoot,'spanningTreeBridgePriority':spanningTreeBridgePriority,'spanningTreeHelloTime':spanningTreeHelloTime,'spanningTreeMaxAge':spanningTreeMaxAge,'spanningTreeForwardingDelay':spanningTreeForwardingDelay,'spanningTreeTable':spanningTreeTable,'spanningTreeEntry':spanningTreeEntry,_A3:spanningTreeIndex,'enableSpanningTree':enableSpanningTree,'spanningTreePortPriority':spanningTreePortPriority,'spanningTreePortCost':spanningTreePortCost,'spanningTreePortStatus':spanningTreePortStatus,'spanningTreePortEdge':spanningTreePortEdge,'activeProtocolOfRedundancy':activeProtocolOfRedundancy,_m:turboRingV2,'turboRingV2Ring1':turboRingV2Ring1,'ringIndexRing1':ringIndexRing1,'ringEnableRing1':ringEnableRing1,'masterSetupRing1':masterSetupRing1,'masterStatusRing1':masterStatusRing1,'designatedMasterRing1':designatedMasterRing1,'rdnt1stPortRing1':rdnt1stPortRing1,'rdnt1stPortStatusRing1':rdnt1stPortStatusRing1,'rdnt2ndPortRing1':rdnt2ndPortRing1,'rdnt2ndPortStatusRing1':rdnt2ndPortStatusRing1,'brokenStatusRing1':brokenStatusRing1,'turboRingV2Ring2':turboRingV2Ring2,'ringIndexRing2':ringIndexRing2,'ringEnableRing2':ringEnableRing2,'masterSetupRing2':masterSetupRing2,'masterStatusRing2':masterStatusRing2,'designatedMasterRing2':designatedMasterRing2,'rdnt1stPortRing2':rdnt1stPortRing2,'rdnt1stPortStatusRing2':rdnt1stPortStatusRing2,'rdnt2ndPortRing2':rdnt2ndPortRing2,'rdnt2ndPortStatusRing2':rdnt2ndPortStatusRing2,'brokenStatusRing2':brokenStatusRing2,'turboRingV2Coupling':turboRingV2Coupling,'couplingEnable':couplingEnable,'couplingMode':couplingMode,'coupling1stPort':coupling1stPort,'coupling1stPortStatus':coupling1stPortStatus,'coupling2ndPort':coupling2ndPort,'coupling2ndPortStatus':coupling2ndPortStatus,_n:turboChain,'turboChainRole':turboChainRole,'turboChainPort1':turboChainPort1,'turboChainPort2':turboChainPort2,'turboChainPort1Status':turboChainPort1Status,'turboChainPort2Status':turboChainPort2Status,'turboChainPort1PartnerBridge':turboChainPort1PartnerBridge,'turboChainPort2PartnerBridge':turboChainPort2PartnerBridge,'relayWarning':relayWarning,'relayWarningTable':relayWarningTable,'relayWarningEntry':relayWarningEntry,_r:relayAlarmIndex,'relayWarningRelayContact':relayWarningRelayContact,'overrideRelayWarningSetting':overrideRelayWarningSetting,'relayWarningPower1Off':relayWarningPower1Off,'relayWarningPower1OffStatus':relayWarningPower1OffStatus,'relayWarningPower2Off':relayWarningPower2Off,'relayWarningPower2OffStatus':relayWarningPower2OffStatus,'relayWarningTurboRingBreak':relayWarningTurboRingBreak,'relayWarningTurboRingBreakStatus':relayWarningTurboRingBreakStatus,'portRelayWarningTable':portRelayWarningTable,'portRelayWarningEntry':portRelayWarningEntry,'relayWarningLinkChanged':relayWarningLinkChanged,'relayWarningLinkChangedStatus':relayWarningLinkChangedStatus,'relayWarningTrafficOverload':relayWarningTrafficOverload,'relayWarningTrafficOverloadStatus':relayWarningTrafficOverloadStatus,'relayWarningRxTrafficThreshold':relayWarningRxTrafficThreshold,'relayWarningTrafficDuration':relayWarningTrafficDuration,'trafficPrioritization':trafficPrioritization,'qosClassification':qosClassification,'queuingMechanism':queuingMechanism,'qosPortTable':qosPortTable,'qosPortEntry':qosPortEntry,'inspectTos':inspectTos,'inspectCos':inspectCos,'portPriority':portPriority,'cosMapping':cosMapping,'cosMappingTable':cosMappingTable,'cosMappingEntry':cosMappingEntry,'cosTag':cosTag,'cosMappedPriority':cosMappedPriority,'tosMapping':tosMapping,'tosMappingTable':tosMappingTable,'tosMappingEntry':tosMappingEntry,'tosClass':tosClass,'tosMappedPriority':tosMappedPriority,'vlan':vlan,'vlanPortSettingTable':vlanPortSettingTable,'vlanPortSettingEntry':vlanPortSettingEntry,'portVlanType':portVlanType,'portDefaultVid':portDefaultVid,'portFixedVid':portFixedVid,'portForbiddenVid':portForbiddenVid,'portFixedVidUntag':portFixedVidUntag,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_u:vlanId,'joinedAccessPorts':joinedAccessPorts,'joinedTrunkPorts':joinedTrunkPorts,'joinedHybridPorts':joinedHybridPorts,'managementVlanId':managementVlanId,'vlanType':vlanType,'portbaseVlanSettingTable':portbaseVlanSettingTable,'portbaseVlanSettingEntry':portbaseVlanSettingEntry,_A5:portbaseVlanSettingIndex,'portbaseVlanMemberPorts':portbaseVlanMemberPorts,'enableGvrp':enableGvrp,'multicastFiltering':multicastFiltering,'igmpSnooping':igmpSnooping,'querierQueryInterval':querierQueryInterval,'igmpSnoopingSettingTable':igmpSnoopingSettingTable,'igmpSnoopingSettingEntry':igmpSnoopingSettingEntry,'enableIgmpSnooping':enableIgmpSnooping,'enableQuerier':enableQuerier,'fixedMulticastQuerierPorts':fixedMulticastQuerierPorts,'learnedMulticastQuerierPorts':learnedMulticastQuerierPorts,'enableGlobalIgmpSnooping':enableGlobalIgmpSnooping,'staticMulticast':staticMulticast,'staticMulticastTable':staticMulticastTable,'staticMulticastEntry':staticMulticastEntry,_A6:staticMulticastAddress,'staticMulticastPorts':staticMulticastPorts,'staticMulticastStatus':staticMulticastStatus,'gmrp':gmrp,'gmrpSettingTable':gmrpSettingTable,'gmrpSettingEntry':gmrpSettingEntry,'enableGMRP':enableGMRP,'gmrpTable':gmrpTable,'gmrpEntry':gmrpEntry,_A9:gmrpMulticastGroup,'gmrpFixedPorts':gmrpFixedPorts,'gmrpLearnedPorts':gmrpLearnedPorts,'rateLimiting':rateLimiting,'normalModeRateLimitingIngressTable':normalModeRateLimitingIngressTable,'normalModeRateLimitingIngressEntry':normalModeRateLimitingIngressEntry,'limitMode':limitMode,'lowPriLimitRate':lowPriLimitRate,'normalPriLimitRate':normalPriLimitRate,'mediumPriLimitRate':mediumPriLimitRate,'highPriLimitRate':highPriLimitRate,'egressLimit':egressLimit,'portDisableMode':portDisableMode,'portDisableModePeriod':portDisableModePeriod,'portDisableModeTable':portDisableModeTable,'portDisableModeEntry':portDisableModeEntry,'ingressLimit':ingressLimit,'rateLimitingMode':rateLimitingMode,'accessibleIP':accessibleIP,'enableAccessibleIP':enableAccessibleIP,'accessibleIpTable':accessibleIpTable,'accessibleIpEntry':accessibleIpEntry,_AB:accessibleIpAddress,'accessibleIpNetMask':accessibleIpNetMask,'accessibleIpStatus':accessibleIpStatus,'sysFileUpdate':sysFileUpdate,'tftpServer':tftpServer,'firmwarePathName':firmwarePathName,'logPathName':logPathName,'confPathName':confPathName,'tftpUpdate':tftpUpdate,'timeSetting':timeSetting,'sysDateTime':sysDateTime,'calibratePeriod':calibratePeriod,'timeServer1':timeServer1,'timeServer2':timeServer2,'daylightSaving':daylightSaving,'startMonth':startMonth,'startWeek':startWeek,'startDay':startDay,'startHour':startHour,'endMonth':endMonth,'endWeek':endWeek,'endDay':endDay,'endHour':endHour,'offsetHours':offsetHours,'enableNTPServer':enableNTPServer,'timeProtocolOption':timeProtocolOption,'dipSwitchSetting':dipSwitchSetting,'dipSwitchEnableTurboRing':dipSwitchEnableTurboRing,'dipSwitchTurboRingPole':dipSwitchTurboRingPole,'dipSwitchRingCouplingPole':dipSwitchRingCouplingPole,'dipSwitchRingMasterPole':dipSwitchRingMasterPole,'backupMediaSetting':backupMediaSetting,'backupMediaAutoLoad':backupMediaAutoLoad,'enableWarmStart':enableWarmStart,'syslogSetting':syslogSetting,'syslogServer1':syslogServer1,'syslogServer1port':syslogServer1port,'syslogServer2':syslogServer2,'syslogServer2port':syslogServer2port,'syslogServer3':syslogServer3,'syslogServer3port':syslogServer3port,'dhcpRelayAgentSetting':dhcpRelayAgentSetting,'dhcpServer1':dhcpServer1,'dhcpServer2':dhcpServer2,'dhcpServer3':dhcpServer3,'dhcpServer4':dhcpServer4,'option82Setting':option82Setting,'enableOption82':enableOption82,'option82Type':option82Type,'option82Value':option82Value,'option82ValueDisplay':option82ValueDisplay,'dhcpFunctionTable':dhcpFunctionTable,'dhcpFunctionEntry':dhcpFunctionEntry,_AC:dhcpPortIndex,'circuitID':circuitID,'option82Enable':option82Enable,'diagnosis':diagnosis,'lldpSetting':lldpSetting,'enableLLDP':enableLLDP,'lldpMSGInterval':lldpMSGInterval,'webTimeout':webTimeout,'ageTime':ageTime,'garpSetting':garpSetting,'joinTime':joinTime,'leaveTime':leaveTime,'leaveAllTime':leaveAllTime,'eventlog':eventlog,'eventlogTable':eventlogTable,'eventlogEntry':eventlogEntry,_AD:eventlogIndex,'eventlogBootup':eventlogBootup,'eventlogDate':eventlogDate,'eventlogTime':eventlogTime,'eventlogUptime':eventlogUptime,'eventlogEvent':eventlogEvent,'eventlogClear':eventlogClear,'industrialProtocol':industrialProtocol,'eipSetting':eipSetting,'enableEtherNetIP':enableEtherNetIP,'modbusSetting':modbusSetting,'enableModbus':enableModbus,'profinetioSetting':profinetioSetting,'enableProfinetIO':enableProfinetIO,'enableFactoryDefault':enableFactoryDefault,'consoleLoginMode':consoleLoginMode,'cpuLoading5s':cpuLoading5s,'cpuLoading30s':cpuLoading30s,'cpuLoading300s':cpuLoading300s,'totalMemory':totalMemory,'freeMemory':freeMemory,'usedMemory':usedMemory,'memoryUsage':memoryUsage,'loopProtection':loopProtection,'swTraps':swTraps,_AE:varconfigChangeTrap,_AF:varpower1Trap,_AG:varpower2Trap,_AH:vartrafficOverloadTrap,_AI:varredundancyTopologyChangedTrap,_AJ:varturboRingCouplingPortChangedTrap,_AK:varturboRingMasterChangedTrap,_AL:varLLDPChgTrap})