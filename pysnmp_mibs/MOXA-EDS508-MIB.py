_A7='accessibleIpAddress'
_A6='staticUnicastAddress'
_A5='staticMulticastAddress'
_A4='igmpSnoopingIpGroup'
_A3='spanningTreeIndex'
_A2='priority0'
_A1='turboRingPortIndex'
_A0='setDevIpIndex'
_z='emailWarningPortIndex'
_y='monitorPortIndex'
_x='present'
_w='not-present'
_v='speed10M-Half'
_u='speed10M-Full'
_t='speed100M-Half'
_s='speed100M-Full'
_r='DisplayString'
_q='limit16M'
_p='destroy'
_o='createAndWait'
_n='createAndGo'
_m='mandatory'
_l='turboRing'
_k='spanningTree'
_j='vlanId'
_i='high'
_h='medium'
_g='low'
_f='relayAlarmIndex'
_e='active'
_d='forwarding'
_c='blocked'
_b='linkDown'
_a='portDisabled'
_Z='diIndex'
_Y='on'
_X='off'
_W='limit8M'
_V='limit4M'
_U='limit2M'
_T='limit1M'
_S='limit512k'
_R='limit256k'
_Q='limit128k'
_P='notlimit'
_O='triggered'
_N='not-triggered'
_M='OctetString'
_L='normal'
_K='yes'
_J='portIndex'
_I='no'
_H='read-create'
_G='MOXA-EDS508-MIB'
_F='enable'
_E='disable'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_r,'PhysAddress','TextualConvention')
etherDeviceSwitch=ModuleIdentity((1,3,6,1,4,1,8691,7,1))
if mibBuilder.loadTexts:etherDeviceSwitch.setRevisions(('2005-03-23 00:00','2005-03-22 00:00','2005-03-17 00:00','2004-12-08 00:00','2004-08-31 00:00','2004-07-19 00:00'))
class DisplayString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_Moxa_ObjectIdentity=ObjectIdentity
moxa=_Moxa_ObjectIdentity((1,3,6,1,4,1,8691))
_IndustrialEthernet_ObjectIdentity=ObjectIdentity
industrialEthernet=_IndustrialEthernet_ObjectIdentity((1,3,6,1,4,1,8691,7))
_PortsNumber_Type=Integer32
_PortsNumber_Object=MibScalar
portsNumber=_PortsNumber_Object((1,3,6,1,4,1,8691,7,1,1),_PortsNumber_Type())
portsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:portsNumber.setStatus(_A)
_SwitchModel_Type=DisplayString
_SwitchModel_Object=MibScalar
switchModel=_SwitchModel_Object((1,3,6,1,4,1,8691,7,1,2),_SwitchModel_Type())
switchModel.setMaxAccess(_D)
if mibBuilder.loadTexts:switchModel.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,8691,7,1,4),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
class _EnableWebConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableWebConfig_Type.__name__=_C
_EnableWebConfig_Object=MibScalar
enableWebConfig=_EnableWebConfig_Object((1,3,6,1,4,1,8691,7,1,5),_EnableWebConfig_Type())
enableWebConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:enableWebConfig.setStatus(_A)
class _EnableTelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableTelnetConsole_Type.__name__=_C
_EnableTelnetConsole_Object=MibScalar
enableTelnetConsole=_EnableTelnetConsole_Object((1,3,6,1,4,1,8691,7,1,6),_EnableTelnetConsole_Type())
enableTelnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:enableTelnetConsole.setStatus(_A)
class _LineSwapRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LineSwapRecovery_Type.__name__=_C
_LineSwapRecovery_Object=MibScalar
lineSwapRecovery=_LineSwapRecovery_Object((1,3,6,1,4,1,8691,7,1,7),_LineSwapRecovery_Type())
lineSwapRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:lineSwapRecovery.setStatus(_A)
_NetworkSetting_ObjectIdentity=ObjectIdentity
networkSetting=_NetworkSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,1,8))
_SwitchIpAddr_Type=IpAddress
_SwitchIpAddr_Object=MibScalar
switchIpAddr=_SwitchIpAddr_Object((1,3,6,1,4,1,8691,7,1,8,1),_SwitchIpAddr_Type())
switchIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:switchIpAddr.setStatus(_A)
_SwitchIpMask_Type=IpAddress
_SwitchIpMask_Object=MibScalar
switchIpMask=_SwitchIpMask_Object((1,3,6,1,4,1,8691,7,1,8,2),_SwitchIpMask_Type())
switchIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:switchIpMask.setStatus(_A)
_DefaultGateway_Type=IpAddress
_DefaultGateway_Object=MibScalar
defaultGateway=_DefaultGateway_Object((1,3,6,1,4,1,8691,7,1,8,3),_DefaultGateway_Type())
defaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:defaultGateway.setStatus(_A)
class _EnableAutoIpConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('enableDHCP',1),('enableBOOTP',2)))
_EnableAutoIpConfig_Type.__name__=_C
_EnableAutoIpConfig_Object=MibScalar
enableAutoIpConfig=_EnableAutoIpConfig_Object((1,3,6,1,4,1,8691,7,1,8,4),_EnableAutoIpConfig_Type())
enableAutoIpConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAutoIpConfig.setStatus(_A)
_DnsServer1IpAddr_Type=IpAddress
_DnsServer1IpAddr_Object=MibScalar
dnsServer1IpAddr=_DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,7,1,8,5),_DnsServer1IpAddr_Type())
dnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer1IpAddr.setStatus(_A)
_SnmpCommunityName_Type=DisplayString
_SnmpCommunityName_Object=MibScalar
snmpCommunityName=_SnmpCommunityName_Object((1,3,6,1,4,1,8691,7,1,8,6),_SnmpCommunityName_Type())
snmpCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpCommunityName.setStatus(_A)
_TrapServerAddr_Type=DisplayString
_TrapServerAddr_Object=MibScalar
trapServerAddr=_TrapServerAddr_Object((1,3,6,1,4,1,8691,7,1,8,7),_TrapServerAddr_Type())
trapServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerAddr.setStatus(_A)
_DnsServer2IpAddr_Type=IpAddress
_DnsServer2IpAddr_Object=MibScalar
dnsServer2IpAddr=_DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,7,1,8,8),_DnsServer2IpAddr_Type())
dnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer2IpAddr.setStatus(_A)
_PortSetting_ObjectIdentity=ObjectIdentity
portSetting=_PortSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,1,9))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,8691,7,1,9,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,8691,7,1,9,1,1))
portEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PortIndex_Type.__name__=_C
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,8691,7,1,9,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortEnable_Type.__name__=_C
_PortEnable_Object=MibTableColumn
portEnable=_PortEnable_Object((1,3,6,1,4,1,8691,7,1,9,1,1,2),_PortEnable_Type())
portEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portEnable.setStatus(_A)
class _PortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('auto',0),(_s,1),(_t,2),(_u,3),(_v,4)))
_PortSpeed_Type.__name__=_C
_PortSpeed_Object=MibTableColumn
portSpeed=_PortSpeed_Object((1,3,6,1,4,1,8691,7,1,9,1,1,3),_PortSpeed_Type())
portSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:portSpeed.setStatus(_A)
class _PortMDI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('auto',0),('mdiX',1),('mdi',2),(_I,3)))
_PortMDI_Type.__name__=_C
_PortMDI_Object=MibTableColumn
portMDI=_PortMDI_Object((1,3,6,1,4,1,8691,7,1,9,1,1,4),_PortMDI_Type())
portMDI.setMaxAccess(_B)
if mibBuilder.loadTexts:portMDI.setStatus(_A)
class _PortFDXFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortFDXFlowCtrl_Type.__name__=_C
_PortFDXFlowCtrl_Object=MibTableColumn
portFDXFlowCtrl=_PortFDXFlowCtrl_Object((1,3,6,1,4,1,8691,7,1,9,1,1,5),_PortFDXFlowCtrl_Type())
portFDXFlowCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFDXFlowCtrl.setStatus(_A)
_PortName_Type=DisplayString
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,8691,7,1,9,1,1,6),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortTrunkingGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('trunkingGroup1',1),('trunkingGroup2',2),('trunkingGroup3',3),('trunkingGroup4',4)))
_PortTrunkingGroup_Type.__name__=_C
_PortTrunkingGroup_Object=MibTableColumn
portTrunkingGroup=_PortTrunkingGroup_Object((1,3,6,1,4,1,8691,7,1,9,1,1,7),_PortTrunkingGroup_Type())
portTrunkingGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkingGroup.setStatus(_A)
_Monitor_ObjectIdentity=ObjectIdentity
monitor=_Monitor_ObjectIdentity((1,3,6,1,4,1,8691,7,1,10))
class _Power1InputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_w,0),(_x,1)))
_Power1InputStatus_Type.__name__=_C
_Power1InputStatus_Object=MibScalar
power1InputStatus=_Power1InputStatus_Object((1,3,6,1,4,1,8691,7,1,10,1),_Power1InputStatus_Type())
power1InputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power1InputStatus.setStatus(_A)
class _Power2InputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_w,0),(_x,1)))
_Power2InputStatus_Type.__name__=_C
_Power2InputStatus_Object=MibScalar
power2InputStatus=_Power2InputStatus_Object((1,3,6,1,4,1,8691,7,1,10,2),_Power2InputStatus_Type())
power2InputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:power2InputStatus.setStatus(_A)
_MonitorPortTable_Object=MibTable
monitorPortTable=_MonitorPortTable_Object((1,3,6,1,4,1,8691,7,1,10,3))
if mibBuilder.loadTexts:monitorPortTable.setStatus(_A)
_MonitorPortEntry_Object=MibTableRow
monitorPortEntry=_MonitorPortEntry_Object((1,3,6,1,4,1,8691,7,1,10,3,1))
monitorPortEntry.setIndexNames((0,_G,_y))
if mibBuilder.loadTexts:monitorPortEntry.setStatus(_A)
class _MonitorPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_MonitorPortIndex_Type.__name__=_C
_MonitorPortIndex_Object=MibTableColumn
monitorPortIndex=_MonitorPortIndex_Object((1,3,6,1,4,1,8691,7,1,10,3,1,1),_MonitorPortIndex_Type())
monitorPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorPortIndex.setStatus(_A)
class _MonitorLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_E,-1),(_X,0),(_Y,1)))
_MonitorLinkStatus_Type.__name__=_C
_MonitorLinkStatus_Object=MibTableColumn
monitorLinkStatus=_MonitorLinkStatus_Object((1,3,6,1,4,1,8691,7,1,10,3,1,2),_MonitorLinkStatus_Type())
monitorLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorLinkStatus.setStatus(_A)
class _MonitorSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3)));namedValues=NamedValues(*(('na',-1),(_v,0),(_u,1),(_t,2),(_s,3)))
_MonitorSpeed_Type.__name__=_C
_MonitorSpeed_Object=MibTableColumn
monitorSpeed=_MonitorSpeed_Object((1,3,6,1,4,1,8691,7,1,10,3,1,3),_MonitorSpeed_Type())
monitorSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSpeed.setStatus(_A)
class _MonitorAutoMDI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*(('na',-1),('mdi',0),('mdiX',1)))
_MonitorAutoMDI_Type.__name__=_C
_MonitorAutoMDI_Object=MibTableColumn
monitorAutoMDI=_MonitorAutoMDI_Object((1,3,6,1,4,1,8691,7,1,10,3,1,4),_MonitorAutoMDI_Type())
monitorAutoMDI.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorAutoMDI.setStatus(_A)
_MonitorTraffic_Type=Integer32
_MonitorTraffic_Object=MibTableColumn
monitorTraffic=_MonitorTraffic_Object((1,3,6,1,4,1,8691,7,1,10,3,1,5),_MonitorTraffic_Type())
monitorTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTraffic.setStatus(_A)
class _MonitorFDXFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_MonitorFDXFlowCtrl_Type.__name__=_C
_MonitorFDXFlowCtrl_Object=MibTableColumn
monitorFDXFlowCtrl=_MonitorFDXFlowCtrl_Object((1,3,6,1,4,1,8691,7,1,10,3,1,6),_MonitorFDXFlowCtrl_Type())
monitorFDXFlowCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFDXFlowCtrl.setStatus(_A)
_MonitorDiTable_Object=MibTable
monitorDiTable=_MonitorDiTable_Object((1,3,6,1,4,1,8691,7,1,10,4))
if mibBuilder.loadTexts:monitorDiTable.setStatus(_A)
_MonitorDiEntry_Object=MibTableRow
monitorDiEntry=_MonitorDiEntry_Object((1,3,6,1,4,1,8691,7,1,10,4,1))
monitorDiEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:monitorDiEntry.setStatus(_A)
class _DiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DiIndex_Type.__name__=_C
_DiIndex_Object=MibTableColumn
diIndex=_DiIndex_Object((1,3,6,1,4,1,8691,7,1,10,4,1,1),_DiIndex_Type())
diIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:diIndex.setStatus(_A)
class _DiInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_DiInputStatus_Type.__name__=_C
_DiInputStatus_Object=MibTableColumn
diInputStatus=_DiInputStatus_Object((1,3,6,1,4,1,8691,7,1,10,4,1,2),_DiInputStatus_Type())
diInputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:diInputStatus.setStatus(_A)
_EmailWarning_ObjectIdentity=ObjectIdentity
emailWarning=_EmailWarning_ObjectIdentity((1,3,6,1,4,1,8691,7,1,11))
_EmailService_ObjectIdentity=ObjectIdentity
emailService=_EmailService_ObjectIdentity((1,3,6,1,4,1,8691,7,1,11,1))
_EmailWarningMailServer_Type=DisplayString
_EmailWarningMailServer_Object=MibScalar
emailWarningMailServer=_EmailWarningMailServer_Object((1,3,6,1,4,1,8691,7,1,11,1,1),_EmailWarningMailServer_Type())
emailWarningMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningMailServer.setStatus(_A)
_EmailWarningFirstEmailAddr_Type=DisplayString
_EmailWarningFirstEmailAddr_Object=MibScalar
emailWarningFirstEmailAddr=_EmailWarningFirstEmailAddr_Object((1,3,6,1,4,1,8691,7,1,11,1,2),_EmailWarningFirstEmailAddr_Type())
emailWarningFirstEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFirstEmailAddr.setStatus(_A)
_EmailWarningSecondEmailAddr_Type=DisplayString
_EmailWarningSecondEmailAddr_Object=MibScalar
emailWarningSecondEmailAddr=_EmailWarningSecondEmailAddr_Object((1,3,6,1,4,1,8691,7,1,11,1,3),_EmailWarningSecondEmailAddr_Type())
emailWarningSecondEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSecondEmailAddr.setStatus(_A)
_EmailWarningThirdEmailAddr_Type=DisplayString
_EmailWarningThirdEmailAddr_Object=MibScalar
emailWarningThirdEmailAddr=_EmailWarningThirdEmailAddr_Object((1,3,6,1,4,1,8691,7,1,11,1,4),_EmailWarningThirdEmailAddr_Type())
emailWarningThirdEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningThirdEmailAddr.setStatus(_A)
_EmailWarningFourthEmailAddr_Type=DisplayString
_EmailWarningFourthEmailAddr_Object=MibScalar
emailWarningFourthEmailAddr=_EmailWarningFourthEmailAddr_Object((1,3,6,1,4,1,8691,7,1,11,1,5),_EmailWarningFourthEmailAddr_Type())
emailWarningFourthEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFourthEmailAddr.setStatus(_A)
_EmailWarningEventType_ObjectIdentity=ObjectIdentity
emailWarningEventType=_EmailWarningEventType_ObjectIdentity((1,3,6,1,4,1,8691,7,1,11,2))
class _EmailWarningEventServerColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventServerColdStart_Type.__name__=_C
_EmailWarningEventServerColdStart_Object=MibScalar
emailWarningEventServerColdStart=_EmailWarningEventServerColdStart_Object((1,3,6,1,4,1,8691,7,1,11,2,1),_EmailWarningEventServerColdStart_Type())
emailWarningEventServerColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventServerColdStart.setStatus(_A)
class _EmailWarningEventServerWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventServerWarmStart_Type.__name__=_C
_EmailWarningEventServerWarmStart_Object=MibScalar
emailWarningEventServerWarmStart=_EmailWarningEventServerWarmStart_Object((1,3,6,1,4,1,8691,7,1,11,2,2),_EmailWarningEventServerWarmStart_Type())
emailWarningEventServerWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventServerWarmStart.setStatus(_A)
class _EmailWarningEventConfigChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventConfigChange_Type.__name__=_C
_EmailWarningEventConfigChange_Object=MibScalar
emailWarningEventConfigChange=_EmailWarningEventConfigChange_Object((1,3,6,1,4,1,8691,7,1,11,2,3),_EmailWarningEventConfigChange_Type())
emailWarningEventConfigChange.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventConfigChange.setStatus(_A)
class _EmailWarningEventPowerOn2Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPowerOn2Off_Type.__name__=_C
_EmailWarningEventPowerOn2Off_Object=MibScalar
emailWarningEventPowerOn2Off=_EmailWarningEventPowerOn2Off_Object((1,3,6,1,4,1,8691,7,1,11,2,4),_EmailWarningEventPowerOn2Off_Type())
emailWarningEventPowerOn2Off.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPowerOn2Off.setStatus(_A)
class _EmailWarningEventPowerOff2On_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPowerOff2On_Type.__name__=_C
_EmailWarningEventPowerOff2On_Object=MibScalar
emailWarningEventPowerOff2On=_EmailWarningEventPowerOff2On_Object((1,3,6,1,4,1,8691,7,1,11,2,5),_EmailWarningEventPowerOff2On_Type())
emailWarningEventPowerOff2On.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPowerOff2On.setStatus(_A)
class _EmailWarningEventAuthFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventAuthFail_Type.__name__=_C
_EmailWarningEventAuthFail_Object=MibScalar
emailWarningEventAuthFail=_EmailWarningEventAuthFail_Object((1,3,6,1,4,1,8691,7,1,11,2,6),_EmailWarningEventAuthFail_Type())
emailWarningEventAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventAuthFail.setStatus(_A)
class _EmailWarningEventCommRedundancyTopologyChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventCommRedundancyTopologyChanged_Type.__name__=_C
_EmailWarningEventCommRedundancyTopologyChanged_Object=MibScalar
emailWarningEventCommRedundancyTopologyChanged=_EmailWarningEventCommRedundancyTopologyChanged_Object((1,3,6,1,4,1,8691,7,1,11,2,7),_EmailWarningEventCommRedundancyTopologyChanged_Type())
emailWarningEventCommRedundancyTopologyChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventCommRedundancyTopologyChanged.setStatus(_A)
_EmailWarningEventPortTable_Object=MibTable
emailWarningEventPortTable=_EmailWarningEventPortTable_Object((1,3,6,1,4,1,8691,7,1,11,3))
if mibBuilder.loadTexts:emailWarningEventPortTable.setStatus(_A)
_EmailWarningEventPortEntry_Object=MibTableRow
emailWarningEventPortEntry=_EmailWarningEventPortEntry_Object((1,3,6,1,4,1,8691,7,1,11,3,1))
emailWarningEventPortEntry.setIndexNames((0,_G,_z))
if mibBuilder.loadTexts:emailWarningEventPortEntry.setStatus(_A)
class _EmailWarningPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_EmailWarningPortIndex_Type.__name__=_C
_EmailWarningPortIndex_Object=MibTableColumn
emailWarningPortIndex=_EmailWarningPortIndex_Object((1,3,6,1,4,1,8691,7,1,11,3,1,1),_EmailWarningPortIndex_Type())
emailWarningPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:emailWarningPortIndex.setStatus(_A)
class _EmailWarningEventPortLinkOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPortLinkOn_Type.__name__=_C
_EmailWarningEventPortLinkOn_Object=MibTableColumn
emailWarningEventPortLinkOn=_EmailWarningEventPortLinkOn_Object((1,3,6,1,4,1,8691,7,1,11,3,1,2),_EmailWarningEventPortLinkOn_Type())
emailWarningEventPortLinkOn.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortLinkOn.setStatus(_A)
class _EmailWarningEventPortLinkOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPortLinkOff_Type.__name__=_C
_EmailWarningEventPortLinkOff_Object=MibTableColumn
emailWarningEventPortLinkOff=_EmailWarningEventPortLinkOff_Object((1,3,6,1,4,1,8691,7,1,11,3,1,3),_EmailWarningEventPortLinkOff_Type())
emailWarningEventPortLinkOff.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortLinkOff.setStatus(_A)
class _EmailWarningEventPortTrafficOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventPortTrafficOverload_Type.__name__=_C
_EmailWarningEventPortTrafficOverload_Object=MibTableColumn
emailWarningEventPortTrafficOverload=_EmailWarningEventPortTrafficOverload_Object((1,3,6,1,4,1,8691,7,1,11,3,1,4),_EmailWarningEventPortTrafficOverload_Type())
emailWarningEventPortTrafficOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortTrafficOverload.setStatus(_A)
_EmailWarningEventPortTrafficThreshold_Type=Integer32
_EmailWarningEventPortTrafficThreshold_Object=MibTableColumn
emailWarningEventPortTrafficThreshold=_EmailWarningEventPortTrafficThreshold_Object((1,3,6,1,4,1,8691,7,1,11,3,1,5),_EmailWarningEventPortTrafficThreshold_Type())
emailWarningEventPortTrafficThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortTrafficThreshold.setStatus(_A)
_EmailWarningEventPortTrafficDuration_Type=Integer32
_EmailWarningEventPortTrafficDuration_Object=MibTableColumn
emailWarningEventPortTrafficDuration=_EmailWarningEventPortTrafficDuration_Object((1,3,6,1,4,1,8691,7,1,11,3,1,6),_EmailWarningEventPortTrafficDuration_Type())
emailWarningEventPortTrafficDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventPortTrafficDuration.setStatus(_A)
_EmailWarningEventDiTable_Object=MibTable
emailWarningEventDiTable=_EmailWarningEventDiTable_Object((1,3,6,1,4,1,8691,7,1,11,4))
if mibBuilder.loadTexts:emailWarningEventDiTable.setStatus(_A)
_EmailWarningEventDiEntry_Object=MibTableRow
emailWarningEventDiEntry=_EmailWarningEventDiEntry_Object((1,3,6,1,4,1,8691,7,1,11,4,1))
emailWarningEventDiEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:emailWarningEventDiEntry.setStatus(_A)
class _EmailWarningEventDiInputOn2Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventDiInputOn2Off_Type.__name__=_C
_EmailWarningEventDiInputOn2Off_Object=MibTableColumn
emailWarningEventDiInputOn2Off=_EmailWarningEventDiInputOn2Off_Object((1,3,6,1,4,1,8691,7,1,11,4,1,1),_EmailWarningEventDiInputOn2Off_Type())
emailWarningEventDiInputOn2Off.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventDiInputOn2Off.setStatus(_A)
class _EmailWarningEventDiInputOff2On_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EmailWarningEventDiInputOff2On_Type.__name__=_C
_EmailWarningEventDiInputOff2On_Object=MibTableColumn
emailWarningEventDiInputOff2On=_EmailWarningEventDiInputOff2On_Object((1,3,6,1,4,1,8691,7,1,11,4,1,2),_EmailWarningEventDiInputOff2On_Type())
emailWarningEventDiInputOff2On.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningEventDiInputOff2On.setStatus(_A)
_SetDeviceIp_ObjectIdentity=ObjectIdentity
setDeviceIp=_SetDeviceIp_ObjectIdentity((1,3,6,1,4,1,8691,7,1,12))
_SetDevIpTable_Object=MibTable
setDevIpTable=_SetDevIpTable_Object((1,3,6,1,4,1,8691,7,1,12,1))
if mibBuilder.loadTexts:setDevIpTable.setStatus(_A)
_SetDevIpEntry_Object=MibTableRow
setDevIpEntry=_SetDevIpEntry_Object((1,3,6,1,4,1,8691,7,1,12,1,1))
setDevIpEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:setDevIpEntry.setStatus(_A)
class _SetDevIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SetDevIpIndex_Type.__name__=_C
_SetDevIpIndex_Object=MibTableColumn
setDevIpIndex=_SetDevIpIndex_Object((1,3,6,1,4,1,8691,7,1,12,1,1,1),_SetDevIpIndex_Type())
setDevIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpIndex.setStatus(_A)
_SetDevIpCurrentIpofDevice_Type=DisplayString
_SetDevIpCurrentIpofDevice_Object=MibTableColumn
setDevIpCurrentIpofDevice=_SetDevIpCurrentIpofDevice_Object((1,3,6,1,4,1,8691,7,1,12,1,1,2),_SetDevIpCurrentIpofDevice_Type())
setDevIpCurrentIpofDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpCurrentIpofDevice.setStatus(_A)
class _SetDevIpPresentBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_I,0),('dhcpClient',1),('rarp',2),('bootp',4)))
_SetDevIpPresentBy_Type.__name__=_C
_SetDevIpPresentBy_Object=MibTableColumn
setDevIpPresentBy=_SetDevIpPresentBy_Object((1,3,6,1,4,1,8691,7,1,12,1,1,3),_SetDevIpPresentBy_Type())
setDevIpPresentBy.setMaxAccess(_D)
if mibBuilder.loadTexts:setDevIpPresentBy.setStatus(_A)
_SetDevIpDedicatedIp_Type=IpAddress
_SetDevIpDedicatedIp_Object=MibTableColumn
setDevIpDedicatedIp=_SetDevIpDedicatedIp_Object((1,3,6,1,4,1,8691,7,1,12,1,1,4),_SetDevIpDedicatedIp_Type())
setDevIpDedicatedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:setDevIpDedicatedIp.setStatus(_A)
_Mirroring_ObjectIdentity=ObjectIdentity
mirroring=_Mirroring_ObjectIdentity((1,3,6,1,4,1,8691,7,1,13))
class _TargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TargetPort_Type.__name__=_C
_TargetPort_Object=MibScalar
targetPort=_TargetPort_Object((1,3,6,1,4,1,8691,7,1,13,1),_TargetPort_Type())
targetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:targetPort.setStatus(_A)
class _MirroringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_MirroringPort_Type.__name__=_C
_MirroringPort_Object=MibScalar
mirroringPort=_MirroringPort_Object((1,3,6,1,4,1,8691,7,1,13,2),_MirroringPort_Type())
mirroringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirroringPort.setStatus(_A)
class _MonitorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outputDataStream',1),('biDirectional',2)))
_MonitorDirection_Type.__name__=_C
_MonitorDirection_Object=MibScalar
monitorDirection=_MonitorDirection_Object((1,3,6,1,4,1,8691,7,1,13,3),_MonitorDirection_Type())
monitorDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:monitorDirection.setStatus(_A)
_CommRedundancy_ObjectIdentity=ObjectIdentity
commRedundancy=_CommRedundancy_ObjectIdentity((1,3,6,1,4,1,8691,7,1,16))
class _ProtocolOfRedundancySetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_ProtocolOfRedundancySetup_Type.__name__=_C
_ProtocolOfRedundancySetup_Object=MibScalar
protocolOfRedundancySetup=_ProtocolOfRedundancySetup_Object((1,3,6,1,4,1,8691,7,1,16,1),_ProtocolOfRedundancySetup_Type())
protocolOfRedundancySetup.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolOfRedundancySetup.setStatus(_A)
_TurboRing_ObjectIdentity=ObjectIdentity
turboRing=_TurboRing_ObjectIdentity((1,3,6,1,4,1,8691,7,1,16,2))
class _TurboRingMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_TurboRingMaster_Type.__name__=_C
_TurboRingMaster_Object=MibScalar
turboRingMaster=_TurboRingMaster_Object((1,3,6,1,4,1,8691,7,1,16,2,1),_TurboRingMaster_Type())
turboRingMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingMaster.setStatus(_A)
class _TurboRingMasterSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_TurboRingMasterSetup_Type.__name__=_C
_TurboRingMasterSetup_Object=MibScalar
turboRingMasterSetup=_TurboRingMasterSetup_Object((1,3,6,1,4,1,8691,7,1,16,2,2),_TurboRingMasterSetup_Type())
turboRingMasterSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingMasterSetup.setStatus(_A)
_TurboRingPortTable_Object=MibTable
turboRingPortTable=_TurboRingPortTable_Object((1,3,6,1,4,1,8691,7,1,16,2,3))
if mibBuilder.loadTexts:turboRingPortTable.setStatus(_A)
_TurboRingPortEntry_Object=MibTableRow
turboRingPortEntry=_TurboRingPortEntry_Object((1,3,6,1,4,1,8691,7,1,16,2,3,1))
turboRingPortEntry.setIndexNames((0,_G,_A1))
if mibBuilder.loadTexts:turboRingPortEntry.setStatus(_A)
_TurboRingPortIndex_Type=Integer32
_TurboRingPortIndex_Object=MibTableColumn
turboRingPortIndex=_TurboRingPortIndex_Object((1,3,6,1,4,1,8691,7,1,16,2,3,1,1),_TurboRingPortIndex_Type())
turboRingPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortIndex.setStatus(_A)
class _TurboRingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),('notTurboRingPort',1),(_b,2),(_c,3),('learning',4),(_d,5)))
_TurboRingPortStatus_Type.__name__=_C
_TurboRingPortStatus_Object=MibTableColumn
turboRingPortStatus=_TurboRingPortStatus_Object((1,3,6,1,4,1,8691,7,1,16,2,3,1,2),_TurboRingPortStatus_Type())
turboRingPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortStatus.setStatus(_A)
class _TurboRingPortDesignatedBridge_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TurboRingPortDesignatedBridge_Type.__name__=_M
_TurboRingPortDesignatedBridge_Object=MibTableColumn
turboRingPortDesignatedBridge=_TurboRingPortDesignatedBridge_Object((1,3,6,1,4,1,8691,7,1,16,2,3,1,3),_TurboRingPortDesignatedBridge_Type())
turboRingPortDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortDesignatedBridge.setStatus(_m)
_TurboRingPortDesignatedPort_Type=Integer32
_TurboRingPortDesignatedPort_Object=MibTableColumn
turboRingPortDesignatedPort=_TurboRingPortDesignatedPort_Object((1,3,6,1,4,1,8691,7,1,16,2,3,1,4),_TurboRingPortDesignatedPort_Type())
turboRingPortDesignatedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingPortDesignatedPort.setStatus(_m)
class _TurboRingDesignatedMaster_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TurboRingDesignatedMaster_Type.__name__=_M
_TurboRingDesignatedMaster_Object=MibScalar
turboRingDesignatedMaster=_TurboRingDesignatedMaster_Object((1,3,6,1,4,1,8691,7,1,16,2,6),_TurboRingDesignatedMaster_Type())
turboRingDesignatedMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingDesignatedMaster.setStatus(_m)
class _TurboRingRdntPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TurboRingRdntPort1_Type.__name__=_C
_TurboRingRdntPort1_Object=MibScalar
turboRingRdntPort1=_TurboRingRdntPort1_Object((1,3,6,1,4,1,8691,7,1,16,2,7),_TurboRingRdntPort1_Type())
turboRingRdntPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort1.setStatus(_A)
class _TurboRingRdntPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TurboRingRdntPort2_Type.__name__=_C
_TurboRingRdntPort2_Object=MibScalar
turboRingRdntPort2=_TurboRingRdntPort2_Object((1,3,6,1,4,1,8691,7,1,16,2,8),_TurboRingRdntPort2_Type())
turboRingRdntPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort2.setStatus(_A)
class _TurboRingEnableCoupling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TurboRingEnableCoupling_Type.__name__=_C
_TurboRingEnableCoupling_Object=MibScalar
turboRingEnableCoupling=_TurboRingEnableCoupling_Object((1,3,6,1,4,1,8691,7,1,16,2,9),_TurboRingEnableCoupling_Type())
turboRingEnableCoupling.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingEnableCoupling.setStatus(_A)
class _TurboRingCouplingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_TurboRingCouplingPort_Type.__name__=_C
_TurboRingCouplingPort_Object=MibScalar
turboRingCouplingPort=_TurboRingCouplingPort_Object((1,3,6,1,4,1,8691,7,1,16,2,10),_TurboRingCouplingPort_Type())
turboRingCouplingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingCouplingPort.setStatus(_A)
class _TurboRingCouplingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5)));namedValues=NamedValues(*((_a,0),('notCouplingPort',1),(_b,2),(_c,3),(_d,5)))
_TurboRingCouplingPortStatus_Type.__name__=_C
_TurboRingCouplingPortStatus_Object=MibScalar
turboRingCouplingPortStatus=_TurboRingCouplingPortStatus_Object((1,3,6,1,4,1,8691,7,1,16,2,11),_TurboRingCouplingPortStatus_Type())
turboRingCouplingPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingCouplingPortStatus.setStatus(_A)
class _TurboRingControlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_TurboRingControlPort_Type.__name__=_C
_TurboRingControlPort_Object=MibScalar
turboRingControlPort=_TurboRingControlPort_Object((1,3,6,1,4,1,8691,7,1,16,2,12),_TurboRingControlPort_Type())
turboRingControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingControlPort.setStatus(_A)
class _TurboRingControlPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7)));namedValues=NamedValues(*((_a,0),('notControlPort',1),(_b,2),(_c,3),(_d,5),('inactive',6),(_e,7)))
_TurboRingControlPortStatus_Type.__name__=_C
_TurboRingControlPortStatus_Object=MibScalar
turboRingControlPortStatus=_TurboRingControlPortStatus_Object((1,3,6,1,4,1,8691,7,1,16,2,13),_TurboRingControlPortStatus_Type())
turboRingControlPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingControlPortStatus.setStatus(_A)
class _TurboRingBrokenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('na',0),(_L,1),('broken',2)))
_TurboRingBrokenStatus_Type.__name__=_C
_TurboRingBrokenStatus_Object=MibScalar
turboRingBrokenStatus=_TurboRingBrokenStatus_Object((1,3,6,1,4,1,8691,7,1,16,2,14),_TurboRingBrokenStatus_Type())
turboRingBrokenStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:turboRingBrokenStatus.setStatus(_A)
_SpanningTree_ObjectIdentity=ObjectIdentity
spanningTree=_SpanningTree_ObjectIdentity((1,3,6,1,4,1,8691,7,1,16,3))
class _SpanningTreeRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SpanningTreeRoot_Type.__name__=_C
_SpanningTreeRoot_Object=MibScalar
spanningTreeRoot=_SpanningTreeRoot_Object((1,3,6,1,4,1,8691,7,1,16,3,1),_SpanningTreeRoot_Type())
spanningTreeRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreeRoot.setStatus(_A)
class _SpanningTreeBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4096,8192,12288,16384,20480,24576,28672,32768,36864,40960,45056,49152,53248,57344,61440)));namedValues=NamedValues(*((_A2,0),('priority4096',4096),('priority8192',8192),('priority12288',12288),('priority16384',16384),('priority20480',20480),('priority24576',24576),('priority28672',28672),('priority32768',32768),('priority36864',36864),('priority40960',40960),('priority45056',45056),('priority49152',49152),('priority53248',53248),('priority57344',57344),('priority61440',61440)))
_SpanningTreeBridgePriority_Type.__name__=_C
_SpanningTreeBridgePriority_Object=MibScalar
spanningTreeBridgePriority=_SpanningTreeBridgePriority_Object((1,3,6,1,4,1,8691,7,1,16,3,2),_SpanningTreeBridgePriority_Type())
spanningTreeBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeBridgePriority.setStatus(_A)
_SpanningTreeHelloTime_Type=Integer32
_SpanningTreeHelloTime_Object=MibScalar
spanningTreeHelloTime=_SpanningTreeHelloTime_Object((1,3,6,1,4,1,8691,7,1,16,3,3),_SpanningTreeHelloTime_Type())
spanningTreeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeHelloTime.setStatus(_A)
_SpanningTreeMaxAge_Type=Integer32
_SpanningTreeMaxAge_Object=MibScalar
spanningTreeMaxAge=_SpanningTreeMaxAge_Object((1,3,6,1,4,1,8691,7,1,16,3,4),_SpanningTreeMaxAge_Type())
spanningTreeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeMaxAge.setStatus(_A)
_SpanningTreeForwardingDelay_Type=Integer32
_SpanningTreeForwardingDelay_Object=MibScalar
spanningTreeForwardingDelay=_SpanningTreeForwardingDelay_Object((1,3,6,1,4,1,8691,7,1,16,3,5),_SpanningTreeForwardingDelay_Type())
spanningTreeForwardingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeForwardingDelay.setStatus(_A)
_SpanningTreeTable_Object=MibTable
spanningTreeTable=_SpanningTreeTable_Object((1,3,6,1,4,1,8691,7,1,16,3,6))
if mibBuilder.loadTexts:spanningTreeTable.setStatus(_A)
_SpanningTreeEntry_Object=MibTableRow
spanningTreeEntry=_SpanningTreeEntry_Object((1,3,6,1,4,1,8691,7,1,16,3,6,1))
spanningTreeEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:spanningTreeEntry.setStatus(_A)
class _SpanningTreeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SpanningTreeIndex_Type.__name__=_C
_SpanningTreeIndex_Object=MibTableColumn
spanningTreeIndex=_SpanningTreeIndex_Object((1,3,6,1,4,1,8691,7,1,16,3,6,1,1),_SpanningTreeIndex_Type())
spanningTreeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreeIndex.setStatus(_A)
class _EnableSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableSpanningTree_Type.__name__=_C
_EnableSpanningTree_Object=MibTableColumn
enableSpanningTree=_EnableSpanningTree_Object((1,3,6,1,4,1,8691,7,1,16,3,6,1,2),_EnableSpanningTree_Type())
enableSpanningTree.setMaxAccess(_B)
if mibBuilder.loadTexts:enableSpanningTree.setStatus(_A)
class _SpanningTreePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240)));namedValues=NamedValues(*((_A2,0),('priority16',16),('priority32',32),('priority48',48),('priority64',64),('priority80',80),('priority96',96),('priority112',112),('priority128',128),('priority144',144),('priority160',160),('priority176',176),('priority192',192),('priority208',208),('priority224',224),('priority240',240)))
_SpanningTreePortPriority_Type.__name__=_C
_SpanningTreePortPriority_Object=MibTableColumn
spanningTreePortPriority=_SpanningTreePortPriority_Object((1,3,6,1,4,1,8691,7,1,16,3,6,1,3),_SpanningTreePortPriority_Type())
spanningTreePortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortPriority.setStatus(_A)
_SpanningTreePortCost_Type=Integer32
_SpanningTreePortCost_Object=MibTableColumn
spanningTreePortCost=_SpanningTreePortCost_Object((1,3,6,1,4,1,8691,7,1,16,3,6,1,4),_SpanningTreePortCost_Type())
spanningTreePortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortCost.setStatus(_A)
class _SpanningTreePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),('notSpanningTreePort',1),(_b,2),(_c,3),('learning',4),(_d,5)))
_SpanningTreePortStatus_Type.__name__=_C
_SpanningTreePortStatus_Object=MibTableColumn
spanningTreePortStatus=_SpanningTreePortStatus_Object((1,3,6,1,4,1,8691,7,1,16,3,6,1,5),_SpanningTreePortStatus_Type())
spanningTreePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:spanningTreePortStatus.setStatus(_A)
class _ActiveProtocolOfRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),(_k,1),(_l,2)))
_ActiveProtocolOfRedundancy_Type.__name__=_C
_ActiveProtocolOfRedundancy_Object=MibScalar
activeProtocolOfRedundancy=_ActiveProtocolOfRedundancy_Object((1,3,6,1,4,1,8691,7,1,16,4),_ActiveProtocolOfRedundancy_Type())
activeProtocolOfRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:activeProtocolOfRedundancy.setStatus(_A)
_RelayWarning_ObjectIdentity=ObjectIdentity
relayWarning=_RelayWarning_ObjectIdentity((1,3,6,1,4,1,8691,7,1,17))
_RelayWarningTable_Object=MibTable
relayWarningTable=_RelayWarningTable_Object((1,3,6,1,4,1,8691,7,1,17,11))
if mibBuilder.loadTexts:relayWarningTable.setStatus(_A)
_RelayWarningEntry_Object=MibTableRow
relayWarningEntry=_RelayWarningEntry_Object((1,3,6,1,4,1,8691,7,1,17,11,1))
relayWarningEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:relayWarningEntry.setStatus(_A)
class _RelayAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RelayAlarmIndex_Type.__name__=_C
_RelayAlarmIndex_Object=MibTableColumn
relayAlarmIndex=_RelayAlarmIndex_Object((1,3,6,1,4,1,8691,7,1,17,11,1,1),_RelayAlarmIndex_Type())
relayAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:relayAlarmIndex.setStatus(_A)
class _RelayWarningRelayContact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('opened',1)))
_RelayWarningRelayContact_Type.__name__=_C
_RelayWarningRelayContact_Object=MibTableColumn
relayWarningRelayContact=_RelayWarningRelayContact_Object((1,3,6,1,4,1,8691,7,1,17,11,1,2),_RelayWarningRelayContact_Type())
relayWarningRelayContact.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningRelayContact.setStatus(_A)
class _OverrideRelayWarningSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_OverrideRelayWarningSetting_Type.__name__=_C
_OverrideRelayWarningSetting_Object=MibTableColumn
overrideRelayWarningSetting=_OverrideRelayWarningSetting_Object((1,3,6,1,4,1,8691,7,1,17,11,1,3),_OverrideRelayWarningSetting_Type())
overrideRelayWarningSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:overrideRelayWarningSetting.setStatus(_A)
class _RelayWarningPower1Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningPower1Off_Type.__name__=_C
_RelayWarningPower1Off_Object=MibTableColumn
relayWarningPower1Off=_RelayWarningPower1Off_Object((1,3,6,1,4,1,8691,7,1,17,11,1,4),_RelayWarningPower1Off_Type())
relayWarningPower1Off.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningPower1Off.setStatus(_A)
class _RelayWarningPower1OffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_RelayWarningPower1OffStatus_Type.__name__=_C
_RelayWarningPower1OffStatus_Object=MibTableColumn
relayWarningPower1OffStatus=_RelayWarningPower1OffStatus_Object((1,3,6,1,4,1,8691,7,1,17,11,1,5),_RelayWarningPower1OffStatus_Type())
relayWarningPower1OffStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningPower1OffStatus.setStatus(_A)
class _RelayWarningPower2Off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningPower2Off_Type.__name__=_C
_RelayWarningPower2Off_Object=MibTableColumn
relayWarningPower2Off=_RelayWarningPower2Off_Object((1,3,6,1,4,1,8691,7,1,17,11,1,6),_RelayWarningPower2Off_Type())
relayWarningPower2Off.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningPower2Off.setStatus(_A)
class _RelayWarningPower2OffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_RelayWarningPower2OffStatus_Type.__name__=_C
_RelayWarningPower2OffStatus_Object=MibTableColumn
relayWarningPower2OffStatus=_RelayWarningPower2OffStatus_Object((1,3,6,1,4,1,8691,7,1,17,11,1,7),_RelayWarningPower2OffStatus_Type())
relayWarningPower2OffStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningPower2OffStatus.setStatus(_A)
_PortRelayWarningTable_Object=MibTable
portRelayWarningTable=_PortRelayWarningTable_Object((1,3,6,1,4,1,8691,7,1,17,12))
if mibBuilder.loadTexts:portRelayWarningTable.setStatus(_A)
_PortRelayWarningEntry_Object=MibTableRow
portRelayWarningEntry=_PortRelayWarningEntry_Object((1,3,6,1,4,1,8691,7,1,17,12,1))
portRelayWarningEntry.setIndexNames((0,_G,_J),(0,_G,_f))
if mibBuilder.loadTexts:portRelayWarningEntry.setStatus(_A)
class _RelayWarningLinkChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ignore',0),('on2off',1),('off2on',2)))
_RelayWarningLinkChanged_Type.__name__=_C
_RelayWarningLinkChanged_Object=MibTableColumn
relayWarningLinkChanged=_RelayWarningLinkChanged_Object((1,3,6,1,4,1,8691,7,1,17,12,1,1),_RelayWarningLinkChanged_Type())
relayWarningLinkChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningLinkChanged.setStatus(_A)
class _RelayWarningLinkChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_RelayWarningLinkChangedStatus_Type.__name__=_C
_RelayWarningLinkChangedStatus_Object=MibTableColumn
relayWarningLinkChangedStatus=_RelayWarningLinkChangedStatus_Object((1,3,6,1,4,1,8691,7,1,17,12,1,2),_RelayWarningLinkChangedStatus_Type())
relayWarningLinkChangedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningLinkChangedStatus.setStatus(_A)
class _RelayWarningTrafficOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RelayWarningTrafficOverload_Type.__name__=_C
_RelayWarningTrafficOverload_Object=MibTableColumn
relayWarningTrafficOverload=_RelayWarningTrafficOverload_Object((1,3,6,1,4,1,8691,7,1,17,12,1,3),_RelayWarningTrafficOverload_Type())
relayWarningTrafficOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficOverload.setStatus(_A)
class _RelayWarningTrafficOverloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_RelayWarningTrafficOverloadStatus_Type.__name__=_C
_RelayWarningTrafficOverloadStatus_Object=MibTableColumn
relayWarningTrafficOverloadStatus=_RelayWarningTrafficOverloadStatus_Object((1,3,6,1,4,1,8691,7,1,17,12,1,4),_RelayWarningTrafficOverloadStatus_Type())
relayWarningTrafficOverloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningTrafficOverloadStatus.setStatus(_A)
_RelayWarningTrafficThreshold_Type=Integer32
_RelayWarningTrafficThreshold_Object=MibTableColumn
relayWarningTrafficThreshold=_RelayWarningTrafficThreshold_Object((1,3,6,1,4,1,8691,7,1,17,12,1,5),_RelayWarningTrafficThreshold_Type())
relayWarningTrafficThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficThreshold.setStatus(_A)
_RelayWarningTrafficDuration_Type=Integer32
_RelayWarningTrafficDuration_Object=MibTableColumn
relayWarningTrafficDuration=_RelayWarningTrafficDuration_Object((1,3,6,1,4,1,8691,7,1,17,12,1,6),_RelayWarningTrafficDuration_Type())
relayWarningTrafficDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningTrafficDuration.setStatus(_A)
_DiRelayWarningTable_Object=MibTable
diRelayWarningTable=_DiRelayWarningTable_Object((1,3,6,1,4,1,8691,7,1,17,13))
if mibBuilder.loadTexts:diRelayWarningTable.setStatus(_A)
_DiRelayWarningEntry_Object=MibTableRow
diRelayWarningEntry=_DiRelayWarningEntry_Object((1,3,6,1,4,1,8691,7,1,17,13,1))
diRelayWarningEntry.setIndexNames((0,_G,_Z),(0,_G,_f))
if mibBuilder.loadTexts:diRelayWarningEntry.setStatus(_A)
class _RelayWarningDiInputChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_X,1),(_Y,2)))
_RelayWarningDiInputChanged_Type.__name__=_C
_RelayWarningDiInputChanged_Object=MibTableColumn
relayWarningDiInputChanged=_RelayWarningDiInputChanged_Object((1,3,6,1,4,1,8691,7,1,17,13,1,1),_RelayWarningDiInputChanged_Type())
relayWarningDiInputChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:relayWarningDiInputChanged.setStatus(_A)
class _RelayWarningDiInputChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_RelayWarningDiInputChangedStatus_Type.__name__=_C
_RelayWarningDiInputChangedStatus_Object=MibTableColumn
relayWarningDiInputChangedStatus=_RelayWarningDiInputChangedStatus_Object((1,3,6,1,4,1,8691,7,1,17,13,1,2),_RelayWarningDiInputChangedStatus_Type())
relayWarningDiInputChangedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayWarningDiInputChangedStatus.setStatus(_A)
_TrafficPrioritization_ObjectIdentity=ObjectIdentity
trafficPrioritization=_TrafficPrioritization_ObjectIdentity((1,3,6,1,4,1,8691,7,1,18))
_QosClassification_ObjectIdentity=ObjectIdentity
qosClassification=_QosClassification_ObjectIdentity((1,3,6,1,4,1,8691,7,1,18,1))
class _QueuingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('schedweightfair',0),('schedstrict',1)))
_QueuingMechanism_Type.__name__=_C
_QueuingMechanism_Object=MibScalar
queuingMechanism=_QueuingMechanism_Object((1,3,6,1,4,1,8691,7,1,18,1,1),_QueuingMechanism_Type())
queuingMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:queuingMechanism.setStatus(_A)
_QosPortTable_Object=MibTable
qosPortTable=_QosPortTable_Object((1,3,6,1,4,1,8691,7,1,18,1,2))
if mibBuilder.loadTexts:qosPortTable.setStatus(_A)
_QosPortEntry_Object=MibTableRow
qosPortEntry=_QosPortEntry_Object((1,3,6,1,4,1,8691,7,1,18,1,2,1))
qosPortEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:qosPortEntry.setStatus(_A)
class _InspectTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_InspectTos_Type.__name__=_C
_InspectTos_Object=MibTableColumn
inspectTos=_InspectTos_Object((1,3,6,1,4,1,8691,7,1,18,1,2,1,1),_InspectTos_Type())
inspectTos.setMaxAccess(_B)
if mibBuilder.loadTexts:inspectTos.setStatus(_A)
class _InspectCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_InspectCos_Type.__name__=_C
_InspectCos_Object=MibTableColumn
inspectCos=_InspectCos_Object((1,3,6,1,4,1,8691,7,1,18,1,2,1,2),_InspectCos_Type())
inspectCos.setMaxAccess(_B)
if mibBuilder.loadTexts:inspectCos.setStatus(_A)
class _DefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_g,0),(_L,1),(_h,2),(_i,3)))
_DefaultPriority_Type.__name__=_C
_DefaultPriority_Object=MibTableColumn
defaultPriority=_DefaultPriority_Object((1,3,6,1,4,1,8691,7,1,18,1,2,1,3),_DefaultPriority_Type())
defaultPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultPriority.setStatus(_A)
_CosMapping_ObjectIdentity=ObjectIdentity
cosMapping=_CosMapping_ObjectIdentity((1,3,6,1,4,1,8691,7,1,18,2))
_CosMappingTable_Object=MibTable
cosMappingTable=_CosMappingTable_Object((1,3,6,1,4,1,8691,7,1,18,2,1))
if mibBuilder.loadTexts:cosMappingTable.setStatus(_A)
_CosMappingEntry_Object=MibTableRow
cosMappingEntry=_CosMappingEntry_Object((1,3,6,1,4,1,8691,7,1,18,2,1,1))
cosMappingEntry.setIndexNames((0,_G,'cosTag'))
if mibBuilder.loadTexts:cosMappingEntry.setStatus(_A)
class _CosTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CosTag_Type.__name__=_C
_CosTag_Object=MibTableColumn
cosTag=_CosTag_Object((1,3,6,1,4,1,8691,7,1,18,2,1,1,1),_CosTag_Type())
cosTag.setMaxAccess(_D)
if mibBuilder.loadTexts:cosTag.setStatus(_A)
class _CosMappedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_g,0),(_L,1),(_h,2),(_i,3)))
_CosMappedPriority_Type.__name__=_C
_CosMappedPriority_Object=MibTableColumn
cosMappedPriority=_CosMappedPriority_Object((1,3,6,1,4,1,8691,7,1,18,2,1,1,2),_CosMappedPriority_Type())
cosMappedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cosMappedPriority.setStatus(_A)
_TosMapping_ObjectIdentity=ObjectIdentity
tosMapping=_TosMapping_ObjectIdentity((1,3,6,1,4,1,8691,7,1,18,3))
_TosMappingTable_Object=MibTable
tosMappingTable=_TosMappingTable_Object((1,3,6,1,4,1,8691,7,1,18,3,1))
if mibBuilder.loadTexts:tosMappingTable.setStatus(_A)
_TosMappingEntry_Object=MibTableRow
tosMappingEntry=_TosMappingEntry_Object((1,3,6,1,4,1,8691,7,1,18,3,1,1))
tosMappingEntry.setIndexNames((0,_G,'tosClass'))
if mibBuilder.loadTexts:tosMappingEntry.setStatus(_A)
_TosClass_Type=Integer32
_TosClass_Object=MibTableColumn
tosClass=_TosClass_Object((1,3,6,1,4,1,8691,7,1,18,3,1,1,1),_TosClass_Type())
tosClass.setMaxAccess(_D)
if mibBuilder.loadTexts:tosClass.setStatus(_A)
class _TosMappedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_g,0),(_L,1),(_h,2),(_i,3)))
_TosMappedPriority_Type.__name__=_C
_TosMappedPriority_Object=MibTableColumn
tosMappedPriority=_TosMappedPriority_Object((1,3,6,1,4,1,8691,7,1,18,3,1,1,2),_TosMappedPriority_Type())
tosMappedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tosMappedPriority.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,8691,7,1,19))
_VlanPortSettingTable_Object=MibTable
vlanPortSettingTable=_VlanPortSettingTable_Object((1,3,6,1,4,1,8691,7,1,19,1))
if mibBuilder.loadTexts:vlanPortSettingTable.setStatus(_A)
_VlanPortSettingEntry_Object=MibTableRow
vlanPortSettingEntry=_VlanPortSettingEntry_Object((1,3,6,1,4,1,8691,7,1,19,1,1))
vlanPortSettingEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:vlanPortSettingEntry.setStatus(_A)
class _PortVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('access',0),('trunk',1)))
_PortVlanType_Type.__name__=_C
_PortVlanType_Object=MibTableColumn
portVlanType=_PortVlanType_Object((1,3,6,1,4,1,8691,7,1,19,1,1,1),_PortVlanType_Type())
portVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:portVlanType.setStatus(_A)
class _PortDefaultVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortDefaultVid_Type.__name__=_C
_PortDefaultVid_Object=MibTableColumn
portDefaultVid=_PortDefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,1,1,2),_PortDefaultVid_Type())
portDefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portDefaultVid.setStatus(_A)
_PortFixedVid_Type=DisplayString
_PortFixedVid_Object=MibTableColumn
portFixedVid=_PortFixedVid_Object((1,3,6,1,4,1,8691,7,1,19,1,1,3),_PortFixedVid_Type())
portFixedVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portFixedVid.setStatus(_A)
_PortForbiddenVid_Type=DisplayString
_PortForbiddenVid_Object=MibTableColumn
portForbiddenVid=_PortForbiddenVid_Object((1,3,6,1,4,1,8691,7,1,19,1,1,4),_PortForbiddenVid_Type())
portForbiddenVid.setMaxAccess(_B)
if mibBuilder.loadTexts:portForbiddenVid.setStatus(_A)
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,8691,7,1,19,2))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,8691,7,1,19,2,1))
vlanEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanId_Type.__name__=_C
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,8691,7,1,19,2,1,1),_VlanId_Type())
vlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
_JoinedAccessPorts_Type=OctetString
_JoinedAccessPorts_Object=MibTableColumn
joinedAccessPorts=_JoinedAccessPorts_Object((1,3,6,1,4,1,8691,7,1,19,2,1,2),_JoinedAccessPorts_Type())
joinedAccessPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedAccessPorts.setStatus(_A)
_JoinedTrunkPorts_Type=OctetString
_JoinedTrunkPorts_Object=MibTableColumn
joinedTrunkPorts=_JoinedTrunkPorts_Object((1,3,6,1,4,1,8691,7,1,19,2,1,3),_JoinedTrunkPorts_Type())
joinedTrunkPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:joinedTrunkPorts.setStatus(_A)
_PortVidSetTable_ObjectIdentity=ObjectIdentity
portVidSetTable=_PortVidSetTable_ObjectIdentity((1,3,6,1,4,1,8691,7,1,19,3))
_Port1DefaultVid_Type=Integer32
_Port1DefaultVid_Object=MibScalar
port1DefaultVid=_Port1DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,1),_Port1DefaultVid_Type())
port1DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port1DefaultVid.setStatus(_A)
_Port2DefaultVid_Type=Integer32
_Port2DefaultVid_Object=MibScalar
port2DefaultVid=_Port2DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,2),_Port2DefaultVid_Type())
port2DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port2DefaultVid.setStatus(_A)
_Port3DefaultVid_Type=Integer32
_Port3DefaultVid_Object=MibScalar
port3DefaultVid=_Port3DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,3),_Port3DefaultVid_Type())
port3DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port3DefaultVid.setStatus(_A)
_Port4DefaultVid_Type=Integer32
_Port4DefaultVid_Object=MibScalar
port4DefaultVid=_Port4DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,4),_Port4DefaultVid_Type())
port4DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port4DefaultVid.setStatus(_A)
_Port5DefaultVid_Type=Integer32
_Port5DefaultVid_Object=MibScalar
port5DefaultVid=_Port5DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,5),_Port5DefaultVid_Type())
port5DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port5DefaultVid.setStatus(_A)
_Port6DefaultVid_Type=Integer32
_Port6DefaultVid_Object=MibScalar
port6DefaultVid=_Port6DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,6),_Port6DefaultVid_Type())
port6DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port6DefaultVid.setStatus(_A)
_Port7DefaultVid_Type=Integer32
_Port7DefaultVid_Object=MibScalar
port7DefaultVid=_Port7DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,7),_Port7DefaultVid_Type())
port7DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port7DefaultVid.setStatus(_A)
_Port8DefaultVid_Type=Integer32
_Port8DefaultVid_Object=MibScalar
port8DefaultVid=_Port8DefaultVid_Object((1,3,6,1,4,1,8691,7,1,19,3,8),_Port8DefaultVid_Type())
port8DefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:port8DefaultVid.setStatus(_A)
_ManagementVlanId_Type=Integer32
_ManagementVlanId_Object=MibScalar
managementVlanId=_ManagementVlanId_Object((1,3,6,1,4,1,8691,7,1,19,3,9),_ManagementVlanId_Type())
managementVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:managementVlanId.setStatus(_A)
class _PvidsAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('activate',1)))
_PvidsAction_Type.__name__=_C
_PvidsAction_Object=MibScalar
pvidsAction=_PvidsAction_Object((1,3,6,1,4,1,8691,7,1,19,3,10),_PvidsAction_Type())
pvidsAction.setMaxAccess(_B)
if mibBuilder.loadTexts:pvidsAction.setStatus(_A)
_MulticastFiltering_ObjectIdentity=ObjectIdentity
multicastFiltering=_MulticastFiltering_ObjectIdentity((1,3,6,1,4,1,8691,7,1,20))
_IgmpSnooping_ObjectIdentity=ObjectIdentity
igmpSnooping=_IgmpSnooping_ObjectIdentity((1,3,6,1,4,1,8691,7,1,20,1))
_QuerierQueryInterval_Type=Integer32
_QuerierQueryInterval_Object=MibScalar
querierQueryInterval=_QuerierQueryInterval_Object((1,3,6,1,4,1,8691,7,1,20,1,1),_QuerierQueryInterval_Type())
querierQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:querierQueryInterval.setStatus(_A)
_IgmpSnoopingSettingTable_Object=MibTable
igmpSnoopingSettingTable=_IgmpSnoopingSettingTable_Object((1,3,6,1,4,1,8691,7,1,20,1,2))
if mibBuilder.loadTexts:igmpSnoopingSettingTable.setStatus(_A)
_IgmpSnoopingSettingEntry_Object=MibTableRow
igmpSnoopingSettingEntry=_IgmpSnoopingSettingEntry_Object((1,3,6,1,4,1,8691,7,1,20,1,2,1))
igmpSnoopingSettingEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:igmpSnoopingSettingEntry.setStatus(_A)
class _EnableIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableIgmpSnooping_Type.__name__=_C
_EnableIgmpSnooping_Object=MibTableColumn
enableIgmpSnooping=_EnableIgmpSnooping_Object((1,3,6,1,4,1,8691,7,1,20,1,2,1,1),_EnableIgmpSnooping_Type())
enableIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:enableIgmpSnooping.setStatus(_A)
class _EnableQuerier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableQuerier_Type.__name__=_C
_EnableQuerier_Object=MibTableColumn
enableQuerier=_EnableQuerier_Object((1,3,6,1,4,1,8691,7,1,20,1,2,1,2),_EnableQuerier_Type())
enableQuerier.setMaxAccess(_B)
if mibBuilder.loadTexts:enableQuerier.setStatus(_A)
_FixedMulticastRouterPorts_Type=OctetString
_FixedMulticastRouterPorts_Object=MibTableColumn
fixedMulticastRouterPorts=_FixedMulticastRouterPorts_Object((1,3,6,1,4,1,8691,7,1,20,1,2,1,3),_FixedMulticastRouterPorts_Type())
fixedMulticastRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fixedMulticastRouterPorts.setStatus(_A)
_LearnedMulticastRouterPorts_Type=OctetString
_LearnedMulticastRouterPorts_Object=MibTableColumn
learnedMulticastRouterPorts=_LearnedMulticastRouterPorts_Object((1,3,6,1,4,1,8691,7,1,20,1,2,1,4),_LearnedMulticastRouterPorts_Type())
learnedMulticastRouterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:learnedMulticastRouterPorts.setStatus(_A)
_IgmpSnoopingMulticastGroupTable_Object=MibTable
igmpSnoopingMulticastGroupTable=_IgmpSnoopingMulticastGroupTable_Object((1,3,6,1,4,1,8691,7,1,20,1,3))
if mibBuilder.loadTexts:igmpSnoopingMulticastGroupTable.setStatus(_A)
_IgmpSnoopingMulticastGroupEntry_Object=MibTableRow
igmpSnoopingMulticastGroupEntry=_IgmpSnoopingMulticastGroupEntry_Object((1,3,6,1,4,1,8691,7,1,20,1,3,1))
igmpSnoopingMulticastGroupEntry.setIndexNames((0,_G,_j),(0,_G,_A4))
if mibBuilder.loadTexts:igmpSnoopingMulticastGroupEntry.setStatus(_A)
_IgmpSnoopingIpGroup_Type=IpAddress
_IgmpSnoopingIpGroup_Object=MibTableColumn
igmpSnoopingIpGroup=_IgmpSnoopingIpGroup_Object((1,3,6,1,4,1,8691,7,1,20,1,3,1,1),_IgmpSnoopingIpGroup_Type())
igmpSnoopingIpGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingIpGroup.setStatus(_A)
_IgmpSnoopingMacGroup_Type=OctetString
_IgmpSnoopingMacGroup_Object=MibTableColumn
igmpSnoopingMacGroup=_IgmpSnoopingMacGroup_Object((1,3,6,1,4,1,8691,7,1,20,1,3,1,2),_IgmpSnoopingMacGroup_Type())
igmpSnoopingMacGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingMacGroup.setStatus(_A)
_IgmpSnoopingJoinedPorts_Type=OctetString
_IgmpSnoopingJoinedPorts_Object=MibTableColumn
igmpSnoopingJoinedPorts=_IgmpSnoopingJoinedPorts_Object((1,3,6,1,4,1,8691,7,1,20,1,3,1,3),_IgmpSnoopingJoinedPorts_Type())
igmpSnoopingJoinedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopingJoinedPorts.setStatus(_A)
class _EnableGlobalIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableGlobalIgmpSnooping_Type.__name__=_C
_EnableGlobalIgmpSnooping_Object=MibScalar
enableGlobalIgmpSnooping=_EnableGlobalIgmpSnooping_Object((1,3,6,1,4,1,8691,7,1,20,1,4),_EnableGlobalIgmpSnooping_Type())
enableGlobalIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:enableGlobalIgmpSnooping.setStatus(_A)
_StaticMulticast_ObjectIdentity=ObjectIdentity
staticMulticast=_StaticMulticast_ObjectIdentity((1,3,6,1,4,1,8691,7,1,20,2))
_StaticMulticastTable_Object=MibTable
staticMulticastTable=_StaticMulticastTable_Object((1,3,6,1,4,1,8691,7,1,20,2,1))
if mibBuilder.loadTexts:staticMulticastTable.setStatus(_A)
_StaticMulticastEntry_Object=MibTableRow
staticMulticastEntry=_StaticMulticastEntry_Object((1,3,6,1,4,1,8691,7,1,20,2,1,1))
staticMulticastEntry.setIndexNames((0,_G,_A5))
if mibBuilder.loadTexts:staticMulticastEntry.setStatus(_A)
class _StaticMulticastAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_StaticMulticastAddress_Type.__name__=_M
_StaticMulticastAddress_Object=MibTableColumn
staticMulticastAddress=_StaticMulticastAddress_Object((1,3,6,1,4,1,8691,7,1,20,2,1,1,1),_StaticMulticastAddress_Type())
staticMulticastAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:staticMulticastAddress.setStatus(_A)
_StaticMulticastPortMask_Type=OctetString
_StaticMulticastPortMask_Object=MibTableColumn
staticMulticastPortMask=_StaticMulticastPortMask_Object((1,3,6,1,4,1,8691,7,1,20,2,1,1,2),_StaticMulticastPortMask_Type())
staticMulticastPortMask.setMaxAccess(_H)
if mibBuilder.loadTexts:staticMulticastPortMask.setStatus(_A)
class _StaticMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_e,1),(_n,4),(_o,5),(_p,6)))
_StaticMulticastStatus_Type.__name__=_C
_StaticMulticastStatus_Object=MibTableColumn
staticMulticastStatus=_StaticMulticastStatus_Object((1,3,6,1,4,1,8691,7,1,20,2,1,1,3),_StaticMulticastStatus_Type())
staticMulticastStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:staticMulticastStatus.setStatus(_A)
_RateLimiting_ObjectIdentity=ObjectIdentity
rateLimiting=_RateLimiting_ObjectIdentity((1,3,6,1,4,1,8691,7,1,21))
_RateLimitingTable_Object=MibTable
rateLimitingTable=_RateLimitingTable_Object((1,3,6,1,4,1,8691,7,1,21,1))
if mibBuilder.loadTexts:rateLimitingTable.setStatus(_A)
_RateLimitingEntry_Object=MibTableRow
rateLimitingEntry=_RateLimitingEntry_Object((1,3,6,1,4,1,8691,7,1,21,1,1))
rateLimitingEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:rateLimitingEntry.setStatus(_A)
class _IngressLimitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('bmucast',1),('bmcast',2),('bcast',3)))
_IngressLimitMode_Type.__name__=_C
_IngressLimitMode_Object=MibTableColumn
ingressLimitMode=_IngressLimitMode_Object((1,3,6,1,4,1,8691,7,1,21,1,1,1),_IngressLimitMode_Type())
ingressLimitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressLimitMode.setStatus(_A)
class _IngressLowPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_IngressLowPriLimitRate_Type.__name__=_C
_IngressLowPriLimitRate_Object=MibTableColumn
ingressLowPriLimitRate=_IngressLowPriLimitRate_Object((1,3,6,1,4,1,8691,7,1,21,1,1,2),_IngressLowPriLimitRate_Type())
ingressLowPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressLowPriLimitRate.setStatus(_A)
class _IngressNormalPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_q,8)))
_IngressNormalPriLimitRate_Type.__name__=_C
_IngressNormalPriLimitRate_Object=MibTableColumn
ingressNormalPriLimitRate=_IngressNormalPriLimitRate_Object((1,3,6,1,4,1,8691,7,1,21,1,1,3),_IngressNormalPriLimitRate_Type())
ingressNormalPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressNormalPriLimitRate.setStatus(_A)
class _IngressMediumPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_q,8),('limit32M',9)))
_IngressMediumPriLimitRate_Type.__name__=_C
_IngressMediumPriLimitRate_Object=MibTableColumn
ingressMediumPriLimitRate=_IngressMediumPriLimitRate_Object((1,3,6,1,4,1,8691,7,1,21,1,1,4),_IngressMediumPriLimitRate_Type())
ingressMediumPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressMediumPriLimitRate.setStatus(_A)
class _IngressHighPriLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_q,8),('limit32M',9),('limit64M',10)))
_IngressHighPriLimitRate_Type.__name__=_C
_IngressHighPriLimitRate_Object=MibTableColumn
ingressHighPriLimitRate=_IngressHighPriLimitRate_Object((1,3,6,1,4,1,8691,7,1,21,1,1,5),_IngressHighPriLimitRate_Type())
ingressHighPriLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ingressHighPriLimitRate.setStatus(_A)
class _EgressLimitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_EgressLimitRate_Type.__name__=_C
_EgressLimitRate_Object=MibTableColumn
egressLimitRate=_EgressLimitRate_Object((1,3,6,1,4,1,8691,7,1,21,1,1,6),_EgressLimitRate_Type())
egressLimitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:egressLimitRate.setStatus(_A)
_PortLock_ObjectIdentity=ObjectIdentity
portLock=_PortLock_ObjectIdentity((1,3,6,1,4,1,8691,7,1,22))
_PortLockTable_Object=MibTable
portLockTable=_PortLockTable_Object((1,3,6,1,4,1,8691,7,1,22,1))
if mibBuilder.loadTexts:portLockTable.setStatus(_A)
_PortLockEntry_Object=MibTableRow
portLockEntry=_PortLockEntry_Object((1,3,6,1,4,1,8691,7,1,22,1,1))
portLockEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:portLockEntry.setStatus(_A)
class _EnablePortLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnablePortLock_Type.__name__=_C
_EnablePortLock_Object=MibTableColumn
enablePortLock=_EnablePortLock_Object((1,3,6,1,4,1,8691,7,1,22,1,1,1),_EnablePortLock_Type())
enablePortLock.setMaxAccess(_B)
if mibBuilder.loadTexts:enablePortLock.setStatus(_A)
_StaticUnicastTable_Object=MibTable
staticUnicastTable=_StaticUnicastTable_Object((1,3,6,1,4,1,8691,7,1,22,2))
if mibBuilder.loadTexts:staticUnicastTable.setStatus(_A)
_StaticUnicastEntry_Object=MibTableRow
staticUnicastEntry=_StaticUnicastEntry_Object((1,3,6,1,4,1,8691,7,1,22,2,1))
staticUnicastEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:staticUnicastEntry.setStatus(_A)
class _StaticUnicastAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_StaticUnicastAddress_Type.__name__=_M
_StaticUnicastAddress_Object=MibTableColumn
staticUnicastAddress=_StaticUnicastAddress_Object((1,3,6,1,4,1,8691,7,1,22,2,1,1),_StaticUnicastAddress_Type())
staticUnicastAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:staticUnicastAddress.setStatus(_A)
_StaticUnicastPort_Type=Integer32
_StaticUnicastPort_Object=MibTableColumn
staticUnicastPort=_StaticUnicastPort_Object((1,3,6,1,4,1,8691,7,1,22,2,1,2),_StaticUnicastPort_Type())
staticUnicastPort.setMaxAccess(_H)
if mibBuilder.loadTexts:staticUnicastPort.setStatus(_A)
class _StaticUnicastPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_g,0),(_L,1),(_h,2),(_i,3)))
_StaticUnicastPriority_Type.__name__=_C
_StaticUnicastPriority_Object=MibTableColumn
staticUnicastPriority=_StaticUnicastPriority_Object((1,3,6,1,4,1,8691,7,1,22,2,1,3),_StaticUnicastPriority_Type())
staticUnicastPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:staticUnicastPriority.setStatus(_A)
class _StaticUnicastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_e,1),(_n,4),(_o,5),(_p,6)))
_StaticUnicastStatus_Type.__name__=_C
_StaticUnicastStatus_Object=MibTableColumn
staticUnicastStatus=_StaticUnicastStatus_Object((1,3,6,1,4,1,8691,7,1,22,2,1,4),_StaticUnicastStatus_Type())
staticUnicastStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:staticUnicastStatus.setStatus(_A)
_AccessibleIP_ObjectIdentity=ObjectIdentity
accessibleIP=_AccessibleIP_ObjectIdentity((1,3,6,1,4,1,8691,7,1,30))
class _EnableAccessibleIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_EnableAccessibleIP_Type.__name__=_C
_EnableAccessibleIP_Object=MibScalar
enableAccessibleIP=_EnableAccessibleIP_Object((1,3,6,1,4,1,8691,7,1,30,1),_EnableAccessibleIP_Type())
enableAccessibleIP.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAccessibleIP.setStatus(_A)
_AccessibleIpTable_Object=MibTable
accessibleIpTable=_AccessibleIpTable_Object((1,3,6,1,4,1,8691,7,1,30,2))
if mibBuilder.loadTexts:accessibleIpTable.setStatus(_A)
_AccessibleIpEntry_Object=MibTableRow
accessibleIpEntry=_AccessibleIpEntry_Object((1,3,6,1,4,1,8691,7,1,30,2,1))
accessibleIpEntry.setIndexNames((0,_G,_A7))
if mibBuilder.loadTexts:accessibleIpEntry.setStatus(_A)
_AccessibleIpAddress_Type=IpAddress
_AccessibleIpAddress_Object=MibTableColumn
accessibleIpAddress=_AccessibleIpAddress_Object((1,3,6,1,4,1,8691,7,1,30,2,1,1),_AccessibleIpAddress_Type())
accessibleIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:accessibleIpAddress.setStatus(_A)
_AccessibleIpNetMask_Type=IpAddress
_AccessibleIpNetMask_Object=MibTableColumn
accessibleIpNetMask=_AccessibleIpNetMask_Object((1,3,6,1,4,1,8691,7,1,30,2,1,2),_AccessibleIpNetMask_Type())
accessibleIpNetMask.setMaxAccess(_H)
if mibBuilder.loadTexts:accessibleIpNetMask.setStatus(_A)
class _AIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6)));namedValues=NamedValues(*((_e,1),(_n,4),(_o,5),(_p,6)))
_AIpStatus_Type.__name__=_C
_AIpStatus_Object=MibTableColumn
aIpStatus=_AIpStatus_Object((1,3,6,1,4,1,8691,7,1,30,2,1,3),_AIpStatus_Type())
aIpStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:aIpStatus.setStatus(_A)
_SysFileUpdate_ObjectIdentity=ObjectIdentity
sysFileUpdate=_SysFileUpdate_ObjectIdentity((1,3,6,1,4,1,8691,7,1,31))
_TftpServer_Type=DisplayString
_TftpServer_Object=MibScalar
tftpServer=_TftpServer_Object((1,3,6,1,4,1,8691,7,1,31,1),_TftpServer_Type())
tftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpServer.setStatus(_A)
_FirmwarePathName_Type=DisplayString
_FirmwarePathName_Object=MibScalar
firmwarePathName=_FirmwarePathName_Object((1,3,6,1,4,1,8691,7,1,31,2),_FirmwarePathName_Type())
firmwarePathName.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwarePathName.setStatus(_A)
_LogPathName_Type=DisplayString
_LogPathName_Object=MibScalar
logPathName=_LogPathName_Object((1,3,6,1,4,1,8691,7,1,31,3),_LogPathName_Type())
logPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:logPathName.setStatus(_A)
_ConfPathName_Type=DisplayString
_ConfPathName_Object=MibScalar
confPathName=_ConfPathName_Object((1,3,6,1,4,1,8691,7,1,31,4),_ConfPathName_Type())
confPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:confPathName.setStatus(_A)
_TimeSetting_ObjectIdentity=ObjectIdentity
timeSetting=_TimeSetting_ObjectIdentity((1,3,6,1,4,1,8691,7,1,32))
_SysDateTime_Type=DateAndTime
_SysDateTime_Object=MibScalar
sysDateTime=_SysDateTime_Object((1,3,6,1,4,1,8691,7,1,32,1),_SysDateTime_Type())
sysDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDateTime.setStatus(_A)
_CalibratePeriod_Type=Integer32
_CalibratePeriod_Object=MibScalar
calibratePeriod=_CalibratePeriod_Object((1,3,6,1,4,1,8691,7,1,32,2),_CalibratePeriod_Type())
calibratePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:calibratePeriod.setStatus(_A)
_TimeServer1_Type=DisplayString
_TimeServer1_Object=MibScalar
timeServer1=_TimeServer1_Object((1,3,6,1,4,1,8691,7,1,32,3),_TimeServer1_Type())
timeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer1.setStatus(_A)
_TimeServer2_Type=DisplayString
_TimeServer2_Object=MibScalar
timeServer2=_TimeServer2_Object((1,3,6,1,4,1,8691,7,1,32,4),_TimeServer2_Type())
timeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer2.setStatus(_A)
configChangeTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,10))
if mibBuilder.loadTexts:configChangeTrap.setStatus('')
powerOn2OffTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,11))
if mibBuilder.loadTexts:powerOn2OffTrap.setStatus('')
powerOff2OnTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,12))
if mibBuilder.loadTexts:powerOff2OnTrap.setStatus('')
trafficOverloadTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,13))
if mibBuilder.loadTexts:trafficOverloadTrap.setStatus('')
redundancyTopologyChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,14))
if mibBuilder.loadTexts:redundancyTopologyChangedTrap.setStatus('')
turboRingCouplingPortChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,15))
if mibBuilder.loadTexts:turboRingCouplingPortChangedTrap.setStatus('')
turboRingMasterChangedTrap=NotificationType((1,3,6,1,4,1,8691,7,1,0,16))
if mibBuilder.loadTexts:turboRingMasterChangedTrap.setStatus('')
mibBuilder.exportSymbols(_G,**{_r:DisplayString,'moxa':moxa,'industrialEthernet':industrialEthernet,'etherDeviceSwitch':etherDeviceSwitch,'configChangeTrap':configChangeTrap,'powerOn2OffTrap':powerOn2OffTrap,'powerOff2OnTrap':powerOff2OnTrap,'trafficOverloadTrap':trafficOverloadTrap,'redundancyTopologyChangedTrap':redundancyTopologyChangedTrap,'turboRingCouplingPortChangedTrap':turboRingCouplingPortChangedTrap,'turboRingMasterChangedTrap':turboRingMasterChangedTrap,'portsNumber':portsNumber,'switchModel':switchModel,'firmwareVersion':firmwareVersion,'enableWebConfig':enableWebConfig,'enableTelnetConsole':enableTelnetConsole,'lineSwapRecovery':lineSwapRecovery,'networkSetting':networkSetting,'switchIpAddr':switchIpAddr,'switchIpMask':switchIpMask,'defaultGateway':defaultGateway,'enableAutoIpConfig':enableAutoIpConfig,'dnsServer1IpAddr':dnsServer1IpAddr,'snmpCommunityName':snmpCommunityName,'trapServerAddr':trapServerAddr,'dnsServer2IpAddr':dnsServer2IpAddr,'portSetting':portSetting,'portTable':portTable,'portEntry':portEntry,_J:portIndex,'portEnable':portEnable,'portSpeed':portSpeed,'portMDI':portMDI,'portFDXFlowCtrl':portFDXFlowCtrl,'portName':portName,'portTrunkingGroup':portTrunkingGroup,'monitor':monitor,'power1InputStatus':power1InputStatus,'power2InputStatus':power2InputStatus,'monitorPortTable':monitorPortTable,'monitorPortEntry':monitorPortEntry,_y:monitorPortIndex,'monitorLinkStatus':monitorLinkStatus,'monitorSpeed':monitorSpeed,'monitorAutoMDI':monitorAutoMDI,'monitorTraffic':monitorTraffic,'monitorFDXFlowCtrl':monitorFDXFlowCtrl,'monitorDiTable':monitorDiTable,'monitorDiEntry':monitorDiEntry,_Z:diIndex,'diInputStatus':diInputStatus,'emailWarning':emailWarning,'emailService':emailService,'emailWarningMailServer':emailWarningMailServer,'emailWarningFirstEmailAddr':emailWarningFirstEmailAddr,'emailWarningSecondEmailAddr':emailWarningSecondEmailAddr,'emailWarningThirdEmailAddr':emailWarningThirdEmailAddr,'emailWarningFourthEmailAddr':emailWarningFourthEmailAddr,'emailWarningEventType':emailWarningEventType,'emailWarningEventServerColdStart':emailWarningEventServerColdStart,'emailWarningEventServerWarmStart':emailWarningEventServerWarmStart,'emailWarningEventConfigChange':emailWarningEventConfigChange,'emailWarningEventPowerOn2Off':emailWarningEventPowerOn2Off,'emailWarningEventPowerOff2On':emailWarningEventPowerOff2On,'emailWarningEventAuthFail':emailWarningEventAuthFail,'emailWarningEventCommRedundancyTopologyChanged':emailWarningEventCommRedundancyTopologyChanged,'emailWarningEventPortTable':emailWarningEventPortTable,'emailWarningEventPortEntry':emailWarningEventPortEntry,_z:emailWarningPortIndex,'emailWarningEventPortLinkOn':emailWarningEventPortLinkOn,'emailWarningEventPortLinkOff':emailWarningEventPortLinkOff,'emailWarningEventPortTrafficOverload':emailWarningEventPortTrafficOverload,'emailWarningEventPortTrafficThreshold':emailWarningEventPortTrafficThreshold,'emailWarningEventPortTrafficDuration':emailWarningEventPortTrafficDuration,'emailWarningEventDiTable':emailWarningEventDiTable,'emailWarningEventDiEntry':emailWarningEventDiEntry,'emailWarningEventDiInputOn2Off':emailWarningEventDiInputOn2Off,'emailWarningEventDiInputOff2On':emailWarningEventDiInputOff2On,'setDeviceIp':setDeviceIp,'setDevIpTable':setDevIpTable,'setDevIpEntry':setDevIpEntry,_A0:setDevIpIndex,'setDevIpCurrentIpofDevice':setDevIpCurrentIpofDevice,'setDevIpPresentBy':setDevIpPresentBy,'setDevIpDedicatedIp':setDevIpDedicatedIp,'mirroring':mirroring,'targetPort':targetPort,'mirroringPort':mirroringPort,'monitorDirection':monitorDirection,'commRedundancy':commRedundancy,'protocolOfRedundancySetup':protocolOfRedundancySetup,_l:turboRing,'turboRingMaster':turboRingMaster,'turboRingMasterSetup':turboRingMasterSetup,'turboRingPortTable':turboRingPortTable,'turboRingPortEntry':turboRingPortEntry,_A1:turboRingPortIndex,'turboRingPortStatus':turboRingPortStatus,'turboRingPortDesignatedBridge':turboRingPortDesignatedBridge,'turboRingPortDesignatedPort':turboRingPortDesignatedPort,'turboRingDesignatedMaster':turboRingDesignatedMaster,'turboRingRdntPort1':turboRingRdntPort1,'turboRingRdntPort2':turboRingRdntPort2,'turboRingEnableCoupling':turboRingEnableCoupling,'turboRingCouplingPort':turboRingCouplingPort,'turboRingCouplingPortStatus':turboRingCouplingPortStatus,'turboRingControlPort':turboRingControlPort,'turboRingControlPortStatus':turboRingControlPortStatus,'turboRingBrokenStatus':turboRingBrokenStatus,_k:spanningTree,'spanningTreeRoot':spanningTreeRoot,'spanningTreeBridgePriority':spanningTreeBridgePriority,'spanningTreeHelloTime':spanningTreeHelloTime,'spanningTreeMaxAge':spanningTreeMaxAge,'spanningTreeForwardingDelay':spanningTreeForwardingDelay,'spanningTreeTable':spanningTreeTable,'spanningTreeEntry':spanningTreeEntry,_A3:spanningTreeIndex,'enableSpanningTree':enableSpanningTree,'spanningTreePortPriority':spanningTreePortPriority,'spanningTreePortCost':spanningTreePortCost,'spanningTreePortStatus':spanningTreePortStatus,'activeProtocolOfRedundancy':activeProtocolOfRedundancy,'relayWarning':relayWarning,'relayWarningTable':relayWarningTable,'relayWarningEntry':relayWarningEntry,_f:relayAlarmIndex,'relayWarningRelayContact':relayWarningRelayContact,'overrideRelayWarningSetting':overrideRelayWarningSetting,'relayWarningPower1Off':relayWarningPower1Off,'relayWarningPower1OffStatus':relayWarningPower1OffStatus,'relayWarningPower2Off':relayWarningPower2Off,'relayWarningPower2OffStatus':relayWarningPower2OffStatus,'portRelayWarningTable':portRelayWarningTable,'portRelayWarningEntry':portRelayWarningEntry,'relayWarningLinkChanged':relayWarningLinkChanged,'relayWarningLinkChangedStatus':relayWarningLinkChangedStatus,'relayWarningTrafficOverload':relayWarningTrafficOverload,'relayWarningTrafficOverloadStatus':relayWarningTrafficOverloadStatus,'relayWarningTrafficThreshold':relayWarningTrafficThreshold,'relayWarningTrafficDuration':relayWarningTrafficDuration,'diRelayWarningTable':diRelayWarningTable,'diRelayWarningEntry':diRelayWarningEntry,'relayWarningDiInputChanged':relayWarningDiInputChanged,'relayWarningDiInputChangedStatus':relayWarningDiInputChangedStatus,'trafficPrioritization':trafficPrioritization,'qosClassification':qosClassification,'queuingMechanism':queuingMechanism,'qosPortTable':qosPortTable,'qosPortEntry':qosPortEntry,'inspectTos':inspectTos,'inspectCos':inspectCos,'defaultPriority':defaultPriority,'cosMapping':cosMapping,'cosMappingTable':cosMappingTable,'cosMappingEntry':cosMappingEntry,'cosTag':cosTag,'cosMappedPriority':cosMappedPriority,'tosMapping':tosMapping,'tosMappingTable':tosMappingTable,'tosMappingEntry':tosMappingEntry,'tosClass':tosClass,'tosMappedPriority':tosMappedPriority,'vlan':vlan,'vlanPortSettingTable':vlanPortSettingTable,'vlanPortSettingEntry':vlanPortSettingEntry,'portVlanType':portVlanType,'portDefaultVid':portDefaultVid,'portFixedVid':portFixedVid,'portForbiddenVid':portForbiddenVid,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_j:vlanId,'joinedAccessPorts':joinedAccessPorts,'joinedTrunkPorts':joinedTrunkPorts,'portVidSetTable':portVidSetTable,'port1DefaultVid':port1DefaultVid,'port2DefaultVid':port2DefaultVid,'port3DefaultVid':port3DefaultVid,'port4DefaultVid':port4DefaultVid,'port5DefaultVid':port5DefaultVid,'port6DefaultVid':port6DefaultVid,'port7DefaultVid':port7DefaultVid,'port8DefaultVid':port8DefaultVid,'managementVlanId':managementVlanId,'pvidsAction':pvidsAction,'multicastFiltering':multicastFiltering,'igmpSnooping':igmpSnooping,'querierQueryInterval':querierQueryInterval,'igmpSnoopingSettingTable':igmpSnoopingSettingTable,'igmpSnoopingSettingEntry':igmpSnoopingSettingEntry,'enableIgmpSnooping':enableIgmpSnooping,'enableQuerier':enableQuerier,'fixedMulticastRouterPorts':fixedMulticastRouterPorts,'learnedMulticastRouterPorts':learnedMulticastRouterPorts,'igmpSnoopingMulticastGroupTable':igmpSnoopingMulticastGroupTable,'igmpSnoopingMulticastGroupEntry':igmpSnoopingMulticastGroupEntry,_A4:igmpSnoopingIpGroup,'igmpSnoopingMacGroup':igmpSnoopingMacGroup,'igmpSnoopingJoinedPorts':igmpSnoopingJoinedPorts,'enableGlobalIgmpSnooping':enableGlobalIgmpSnooping,'staticMulticast':staticMulticast,'staticMulticastTable':staticMulticastTable,'staticMulticastEntry':staticMulticastEntry,_A5:staticMulticastAddress,'staticMulticastPortMask':staticMulticastPortMask,'staticMulticastStatus':staticMulticastStatus,'rateLimiting':rateLimiting,'rateLimitingTable':rateLimitingTable,'rateLimitingEntry':rateLimitingEntry,'ingressLimitMode':ingressLimitMode,'ingressLowPriLimitRate':ingressLowPriLimitRate,'ingressNormalPriLimitRate':ingressNormalPriLimitRate,'ingressMediumPriLimitRate':ingressMediumPriLimitRate,'ingressHighPriLimitRate':ingressHighPriLimitRate,'egressLimitRate':egressLimitRate,'portLock':portLock,'portLockTable':portLockTable,'portLockEntry':portLockEntry,'enablePortLock':enablePortLock,'staticUnicastTable':staticUnicastTable,'staticUnicastEntry':staticUnicastEntry,_A6:staticUnicastAddress,'staticUnicastPort':staticUnicastPort,'staticUnicastPriority':staticUnicastPriority,'staticUnicastStatus':staticUnicastStatus,'accessibleIP':accessibleIP,'enableAccessibleIP':enableAccessibleIP,'accessibleIpTable':accessibleIpTable,'accessibleIpEntry':accessibleIpEntry,_A7:accessibleIpAddress,'accessibleIpNetMask':accessibleIpNetMask,'aIpStatus':aIpStatus,'sysFileUpdate':sysFileUpdate,'tftpServer':tftpServer,'firmwarePathName':firmwarePathName,'logPathName':logPathName,'confPathName':confPathName,'timeSetting':timeSetting,'sysDateTime':sysDateTime,'calibratePeriod':calibratePeriod,'timeServer1':timeServer1,'timeServer2':timeServer2})