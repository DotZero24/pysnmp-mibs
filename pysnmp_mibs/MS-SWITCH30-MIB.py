_AE='ringAlarmDuration'
_AD='ringStatus'
_AC='sfpDetect'
_AB='sfpPortnumber'
_AA='deviceTemperatureLevel'
_A9='poepsePortId'
_A8='radiusServerId'
_A7='syslogDestId'
_A6='snmpTrapDestId'
_A5='applyAndSaveManually'
_A4='saveManually'
_A3='applyAndSaveImmediately'
_A2='rtcSNTPServerId'
_A1='igmpsGroupId'
_A0='igmpsPortId'
_z='pacMacLockPortId'
_y='pacConfPortId'
_x='parallel8021XMACauth'
_w='forceUnauthorized'
_v='radiusMacAuthentication'
_u='macLocking'
_t='forceAuthorized'
_s='pacStatPortId'
_r='relaisId'
_q='standby'
_p='forwarding'
_o='blocked'
_n='ringId'
_m='prioDiffservId'
_l='prioIeeeTagId'
_k='prioPortId'
_j='vlanFilterEnhId'
_i='vlanFilterId'
_h='vlanPortId'
_g='disalbed'
_f='portConfigId'
_e='undetected'
_d='detected'
_c='ringNumber'
_b='portStatusLink'
_a='supplyId'
_Z='reset'
_Y='OctetString'
_X='learn'
_W='tobedone2'
_V='unauthorized2'
_U='authorized2'
_T='tobedone1'
_S='unauthorized1'
_R='authorized1'
_Q='Bits'
_P='fixed'
_O='portStatusId'
_N='normalOperation'
_M='supported'
_L='DisplayString'
_K='undefined'
_J='MS-SWITCH30-MIB'
_I='no'
_H='yes'
_G='enabled'
_F='disabled'
_E='read-only'
_D='unsupported'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Q,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
mib3=ModuleIdentity((1,3,6,1,4,1,3181,10,3))
if mibBuilder.loadTexts:mib3.setRevisions(('2012-01-23 00:00','2011-04-11 00:00','2011-03-03 00:00','2010-12-18 00:00','2010-08-30 00:00','2010-06-24 00:00','2010-05-03 00:00','2010-01-19 00:00','2009-12-22 00:00','2009-11-17 00:00','2009-06-03 00:00','2009-04-29 00:00','2009-01-12 00:00','2008-09-01 00:00','2008-06-17 00:00','2007-07-12 00:00'))
_Microsens_ObjectIdentity=ObjectIdentity
microsens=_Microsens_ObjectIdentity((1,3,6,1,4,1,3181))
_ManagedSwitches_ObjectIdentity=ObjectIdentity
managedSwitches=_ManagedSwitches_ObjectIdentity((1,3,6,1,4,1,3181,10))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,3181,10,3,1))
class _DeviceArtNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DeviceArtNo_Type.__name__=_L
_DeviceArtNo_Object=MibScalar
deviceArtNo=_DeviceArtNo_Object((1,3,6,1,4,1,3181,10,3,1,1),_DeviceArtNo_Type())
deviceArtNo.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceArtNo.setStatus(_A)
class _DeviceSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DeviceSerNo_Type.__name__=_L
_DeviceSerNo_Object=MibScalar
deviceSerNo=_DeviceSerNo_Object((1,3,6,1,4,1,3181,10,3,1,2),_DeviceSerNo_Type())
deviceSerNo.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceSerNo.setStatus(_A)
class _DeviceHardware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DeviceHardware_Type.__name__=_L
_DeviceHardware_Object=MibScalar
deviceHardware=_DeviceHardware_Object((1,3,6,1,4,1,3181,10,3,1,3),_DeviceHardware_Type())
deviceHardware.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceHardware.setStatus(_A)
class _DeviceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DeviceDescription_Type.__name__=_L
_DeviceDescription_Object=MibScalar
deviceDescription=_DeviceDescription_Object((1,3,6,1,4,1,3181,10,3,1,4),_DeviceDescription_Type())
deviceDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceDescription.setStatus(_A)
class _DeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_DeviceName_Type.__name__=_L
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,3181,10,3,1,5),_DeviceName_Type())
deviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
class _DeviceLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_DeviceLocation_Type.__name__=_L
_DeviceLocation_Object=MibScalar
deviceLocation=_DeviceLocation_Object((1,3,6,1,4,1,3181,10,3,1,6),_DeviceLocation_Type())
deviceLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLocation.setStatus(_A)
class _DeviceContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_DeviceContact_Type.__name__=_L
_DeviceContact_Object=MibScalar
deviceContact=_DeviceContact_Object((1,3,6,1,4,1,3181,10,3,1,7),_DeviceContact_Type())
deviceContact.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceContact.setStatus(_A)
class _DeviceGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_DeviceGroup_Type.__name__=_L
_DeviceGroup_Object=MibScalar
deviceGroup=_DeviceGroup_Object((1,3,6,1,4,1,3181,10,3,1,8),_DeviceGroup_Type())
deviceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceGroup.setStatus(_A)
_DeviceTemperature_Type=Integer32
_DeviceTemperature_Object=MibScalar
deviceTemperature=_DeviceTemperature_Object((1,3,6,1,4,1,3181,10,3,1,9),_DeviceTemperature_Type())
deviceTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceTemperature.setStatus(_A)
class _DeviceTemperatureLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,254,255)));namedValues=NamedValues(*(('criticalLow',1),('low',2),('normal',3),('high',4),('criticalHigh',5),('shutdown',6),(_K,254),(_D,255)))
_DeviceTemperatureLevel_Type.__name__=_B
_DeviceTemperatureLevel_Object=MibScalar
deviceTemperatureLevel=_DeviceTemperatureLevel_Object((1,3,6,1,4,1,3181,10,3,1,10),_DeviceTemperatureLevel_Type())
deviceTemperatureLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceTemperatureLevel.setStatus(_A)
_DeviceUpTime_Type=TimeTicks
_DeviceUpTime_Object=MibScalar
deviceUpTime=_DeviceUpTime_Object((1,3,6,1,4,1,3181,10,3,1,11),_DeviceUpTime_Type())
deviceUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceUpTime.setStatus(_A)
_DeviceFddActiveTime_Type=TimeTicks
_DeviceFddActiveTime_Object=MibScalar
deviceFddActiveTime=_DeviceFddActiveTime_Object((1,3,6,1,4,1,3181,10,3,1,12),_DeviceFddActiveTime_Type())
deviceFddActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceFddActiveTime.setStatus(_A)
_DeviceFddPassiveTime_Type=TimeTicks
_DeviceFddPassiveTime_Object=MibScalar
deviceFddPassiveTime=_DeviceFddPassiveTime_Object((1,3,6,1,4,1,3181,10,3,1,13),_DeviceFddPassiveTime_Type())
deviceFddPassiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceFddPassiveTime.setStatus(_A)
class _DeviceInventory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DeviceInventory_Type.__name__=_L
_DeviceInventory_Object=MibScalar
deviceInventory=_DeviceInventory_Object((1,3,6,1,4,1,3181,10,3,1,14),_DeviceInventory_Type())
deviceInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceInventory.setStatus(_A)
_Agent_ObjectIdentity=ObjectIdentity
agent=_Agent_ObjectIdentity((1,3,6,1,4,1,3181,10,3,2))
class _AgentFirmware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgentFirmware_Type.__name__=_L
_AgentFirmware_Object=MibScalar
agentFirmware=_AgentFirmware_Object((1,3,6,1,4,1,3181,10,3,2,1),_AgentFirmware_Type())
agentFirmware.setMaxAccess(_E)
if mibBuilder.loadTexts:agentFirmware.setStatus(_A)
_AgentMacAddress_Type=PhysAddress
_AgentMacAddress_Object=MibScalar
agentMacAddress=_AgentMacAddress_Object((1,3,6,1,4,1,3181,10,3,2,2),_AgentMacAddress_Type())
agentMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMacAddress.setStatus(_A)
class _AgentIpv4Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('static',1),('dhcp',2),(_K,254),(_D,255)))
_AgentIpv4Mode_Type.__name__=_B
_AgentIpv4Mode_Object=MibScalar
agentIpv4Mode=_AgentIpv4Mode_Object((1,3,6,1,4,1,3181,10,3,2,3),_AgentIpv4Mode_Type())
agentIpv4Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv4Mode.setStatus(_A)
_AgentIpv4Address_Type=IpAddress
_AgentIpv4Address_Object=MibScalar
agentIpv4Address=_AgentIpv4Address_Object((1,3,6,1,4,1,3181,10,3,2,4),_AgentIpv4Address_Type())
agentIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv4Address.setStatus(_A)
_AgentIpv4SubnetMask_Type=IpAddress
_AgentIpv4SubnetMask_Object=MibScalar
agentIpv4SubnetMask=_AgentIpv4SubnetMask_Object((1,3,6,1,4,1,3181,10,3,2,5),_AgentIpv4SubnetMask_Type())
agentIpv4SubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv4SubnetMask.setStatus(_A)
_AgentIpv4Gateway_Type=IpAddress
_AgentIpv4Gateway_Object=MibScalar
agentIpv4Gateway=_AgentIpv4Gateway_Object((1,3,6,1,4,1,3181,10,3,2,6),_AgentIpv4Gateway_Type())
agentIpv4Gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv4Gateway.setStatus(_A)
class _AgentConfigReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_Z,1)))
_AgentConfigReset_Type.__name__=_B
_AgentConfigReset_Object=MibScalar
agentConfigReset=_AgentConfigReset_Object((1,3,6,1,4,1,3181,10,3,2,7),_AgentConfigReset_Type())
agentConfigReset.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConfigReset.setStatus(_A)
class _AgentConfigFactoryDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('factoryResetTemp',1),('factoryResetPerm',2)))
_AgentConfigFactoryDefault_Type.__name__=_B
_AgentConfigFactoryDefault_Object=MibScalar
agentConfigFactoryDefault=_AgentConfigFactoryDefault_Object((1,3,6,1,4,1,3181,10,3,2,8),_AgentConfigFactoryDefault_Type())
agentConfigFactoryDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConfigFactoryDefault.setStatus(_A)
class _AgentConfigEnableFactoryButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_AgentConfigEnableFactoryButton_Type.__name__=_B
_AgentConfigEnableFactoryButton_Object=MibScalar
agentConfigEnableFactoryButton=_AgentConfigEnableFactoryButton_Object((1,3,6,1,4,1,3181,10,3,2,9),_AgentConfigEnableFactoryButton_Type())
agentConfigEnableFactoryButton.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConfigEnableFactoryButton.setStatus(_A)
class _AgentSecureAddressFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('useSecure',1),('useNormal',2),(_D,255)))
_AgentSecureAddressFlag_Type.__name__=_B
_AgentSecureAddressFlag_Object=MibScalar
agentSecureAddressFlag=_AgentSecureAddressFlag_Object((1,3,6,1,4,1,3181,10,3,2,10),_AgentSecureAddressFlag_Type())
agentSecureAddressFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSecureAddressFlag.setStatus(_A)
class _AgentStorageMediaCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('noCardInserted',1),('invalidCardDetected',2),('validCardDetected',3),('bootedFromCard',4),('bootedFromCardwithMac',5),(_D,255)))
_AgentStorageMediaCardStatus_Type.__name__=_B
_AgentStorageMediaCardStatus_Object=MibScalar
agentStorageMediaCardStatus=_AgentStorageMediaCardStatus_Object((1,3,6,1,4,1,3181,10,3,2,11),_AgentStorageMediaCardStatus_Type())
agentStorageMediaCardStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentStorageMediaCardStatus.setStatus(_A)
class _AgentStorageMediaCardBoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*((_N,0),('bootSmcTemp',1),('bootSmcPerm',2),(_D,255)))
_AgentStorageMediaCardBoot_Type.__name__=_B
_AgentStorageMediaCardBoot_Object=MibScalar
agentStorageMediaCardBoot=_AgentStorageMediaCardBoot_Object((1,3,6,1,4,1,3181,10,3,2,12),_AgentStorageMediaCardBoot_Type())
agentStorageMediaCardBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:agentStorageMediaCardBoot.setStatus(_A)
class _AgentStorageMediaCardMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('useMacFromSMC',1),('useOriginalMac',2),(_D,255)))
_AgentStorageMediaCardMac_Type.__name__=_B
_AgentStorageMediaCardMac_Object=MibScalar
agentStorageMediaCardMac=_AgentStorageMediaCardMac_Object((1,3,6,1,4,1,3181,10,3,2,13),_AgentStorageMediaCardMac_Type())
agentStorageMediaCardMac.setMaxAccess(_C)
if mibBuilder.loadTexts:agentStorageMediaCardMac.setStatus(_A)
class _AgentStoreConfigToStorageMediaCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),('store',1),(_D,255)))
_AgentStoreConfigToStorageMediaCard_Type.__name__=_B
_AgentStoreConfigToStorageMediaCard_Object=MibScalar
agentStoreConfigToStorageMediaCard=_AgentStoreConfigToStorageMediaCard_Object((1,3,6,1,4,1,3181,10,3,2,14),_AgentStoreConfigToStorageMediaCard_Type())
agentStoreConfigToStorageMediaCard.setMaxAccess(_C)
if mibBuilder.loadTexts:agentStoreConfigToStorageMediaCard.setStatus(_A)
class _AgentDhcpConfigRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_AgentDhcpConfigRequest_Type.__name__=_B
_AgentDhcpConfigRequest_Object=MibScalar
agentDhcpConfigRequest=_AgentDhcpConfigRequest_Object((1,3,6,1,4,1,3181,10,3,2,15),_AgentDhcpConfigRequest_Type())
agentDhcpConfigRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpConfigRequest.setStatus(_A)
_Port_ObjectIdentity=ObjectIdentity
port=_Port_ObjectIdentity((1,3,6,1,4,1,3181,10,3,3))
_PortCount_Type=Integer32
_PortCount_Object=MibScalar
portCount=_PortCount_Object((1,3,6,1,4,1,3181,10,3,3,1),_PortCount_Type())
portCount.setMaxAccess(_E)
if mibBuilder.loadTexts:portCount.setStatus(_A)
_PortStatusTable_Object=MibTable
portStatusTable=_PortStatusTable_Object((1,3,6,1,4,1,3181,10,3,3,10))
if mibBuilder.loadTexts:portStatusTable.setStatus(_A)
_PortStatusTableEntry_Object=MibTableRow
portStatusTableEntry=_PortStatusTableEntry_Object((1,3,6,1,4,1,3181,10,3,3,10,1))
portStatusTableEntry.setIndexNames((0,_J,_O))
if mibBuilder.loadTexts:portStatusTableEntry.setStatus(_A)
class _PortStatusId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PortStatusId_Type.__name__=_B
_PortStatusId_Object=MibTableColumn
portStatusId=_PortStatusId_Object((1,3,6,1,4,1,3181,10,3,3,10,1,1),_PortStatusId_Type())
portStatusId.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusId.setStatus(_A)
class _PortStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,254)));namedValues=NamedValues(*(('port-tx10-100',1),('port-t10-100-1000',2),('port-fx100',3),('port-fx100-1000-sfp',4),('port-x1000',5),('port-tx10-100-1000-sfp',6),('port-tx10-100-1000-1x9',7),(_K,254)))
_PortStatusType_Type.__name__=_B
_PortStatusType_Object=MibTableColumn
portStatusType=_PortStatusType_Object((1,3,6,1,4,1,3181,10,3,3,10,1,2),_PortStatusType_Type())
portStatusType.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusType.setStatus(_A)
class _PortStatusLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254)));namedValues=NamedValues(*(('up',1),('down',2),(_K,254)))
_PortStatusLink_Type.__name__=_B
_PortStatusLink_Object=MibTableColumn
portStatusLink=_PortStatusLink_Object((1,3,6,1,4,1,3181,10,3,3,10,1,3),_PortStatusLink_Type())
portStatusLink.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusLink.setStatus(_A)
class _PortStatusSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,254)));namedValues=NamedValues(*(('speed10',1),('speed100',2),('speed1000',3),(_K,254)))
_PortStatusSpeed_Type.__name__=_B
_PortStatusSpeed_Object=MibTableColumn
portStatusSpeed=_PortStatusSpeed_Object((1,3,6,1,4,1,3181,10,3,3,10,1,4),_PortStatusSpeed_Type())
portStatusSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusSpeed.setStatus(_A)
class _PortStatusDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254)));namedValues=NamedValues(*(('halfduplex',1),('fullduplex',2),(_K,254)))
_PortStatusDuplex_Type.__name__=_B
_PortStatusDuplex_Object=MibTableColumn
portStatusDuplex=_PortStatusDuplex_Object((1,3,6,1,4,1,3181,10,3,3,10,1,5),_PortStatusDuplex_Type())
portStatusDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusDuplex.setStatus(_A)
class _PortStatusFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_K,254),(_D,255)))
_PortStatusFlowControl_Type.__name__=_B
_PortStatusFlowControl_Object=MibTableColumn
portStatusFlowControl=_PortStatusFlowControl_Object((1,3,6,1,4,1,3181,10,3,3,10,1,6),_PortStatusFlowControl_Type())
portStatusFlowControl.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusFlowControl.setStatus(_A)
class _PortStatusPinout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('mdi',1),('mdix',2),(_K,254),(_D,255)))
_PortStatusPinout_Type.__name__=_B
_PortStatusPinout_Object=MibTableColumn
portStatusPinout=_PortStatusPinout_Object((1,3,6,1,4,1,3181,10,3,3,10,1,7),_PortStatusPinout_Type())
portStatusPinout.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusPinout.setStatus(_A)
class _PortStatusFarEndFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_d,1),(_e,2),(_K,254),(_D,255)))
_PortStatusFarEndFault_Type.__name__=_B
_PortStatusFarEndFault_Object=MibTableColumn
portStatusFarEndFault=_PortStatusFarEndFault_Object((1,3,6,1,4,1,3181,10,3,3,10,1,8),_PortStatusFarEndFault_Type())
portStatusFarEndFault.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusFarEndFault.setStatus(_A)
class _PortStatusRxNetload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_PortStatusRxNetload_Type.__name__=_B
_PortStatusRxNetload_Object=MibTableColumn
portStatusRxNetload=_PortStatusRxNetload_Object((1,3,6,1,4,1,3181,10,3,3,10,1,9),_PortStatusRxNetload_Type())
portStatusRxNetload.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusRxNetload.setStatus(_A)
class _PortStatusTxNetload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_PortStatusTxNetload_Type.__name__=_B
_PortStatusTxNetload_Object=MibTableColumn
portStatusTxNetload=_PortStatusTxNetload_Object((1,3,6,1,4,1,3181,10,3,3,10,1,10),_PortStatusTxNetload_Type())
portStatusTxNetload.setMaxAccess(_E)
if mibBuilder.loadTexts:portStatusTxNetload.setStatus(_A)
_PortConfigTable_Object=MibTable
portConfigTable=_PortConfigTable_Object((1,3,6,1,4,1,3181,10,3,3,20))
if mibBuilder.loadTexts:portConfigTable.setStatus(_A)
_PortConfigTableEntry_Object=MibTableRow
portConfigTableEntry=_PortConfigTableEntry_Object((1,3,6,1,4,1,3181,10,3,3,20,1))
portConfigTableEntry.setIndexNames((0,_J,_f))
if mibBuilder.loadTexts:portConfigTableEntry.setStatus(_A)
class _PortConfigId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PortConfigId_Type.__name__=_B
_PortConfigId_Object=MibTableColumn
portConfigId=_PortConfigId_Object((1,3,6,1,4,1,3181,10,3,3,20,1,1),_PortConfigId_Type())
portConfigId.setMaxAccess(_E)
if mibBuilder.loadTexts:portConfigId.setStatus(_A)
class _PortConfigAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_PortConfigAlias_Type.__name__=_L
_PortConfigAlias_Object=MibTableColumn
portConfigAlias=_PortConfigAlias_Object((1,3,6,1,4,1,3181,10,3,3,20,1,2),_PortConfigAlias_Type())
portConfigAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigAlias.setStatus(_A)
class _PortConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_K,254),(_D,255)))
_PortConfigEnable_Type.__name__=_B
_PortConfigEnable_Object=MibTableColumn
portConfigEnable=_PortConfigEnable_Object((1,3,6,1,4,1,3181,10,3,3,20,1,3),_PortConfigEnable_Type())
portConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigEnable.setStatus(_A)
class _PortConfigAutonego_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_K,254),(_D,255)))
_PortConfigAutonego_Type.__name__=_B
_PortConfigAutonego_Object=MibTableColumn
portConfigAutonego=_PortConfigAutonego_Object((1,3,6,1,4,1,3181,10,3,3,20,1,4),_PortConfigAutonego_Type())
portConfigAutonego.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigAutonego.setStatus(_A)
class _PortConfigSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,254,255)));namedValues=NamedValues(*(('force10',1),('force100',2),('force1000',3),(_K,254),(_D,255)))
_PortConfigSpeed_Type.__name__=_B
_PortConfigSpeed_Object=MibTableColumn
portConfigSpeed=_PortConfigSpeed_Object((1,3,6,1,4,1,3181,10,3,3,20,1,5),_PortConfigSpeed_Type())
portConfigSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigSpeed.setStatus(_A)
class _PortConfigDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('forcehalf',1),('forcefull',2),(_K,254),(_D,255)))
_PortConfigDuplex_Type.__name__=_B
_PortConfigDuplex_Object=MibTableColumn
portConfigDuplex=_PortConfigDuplex_Object((1,3,6,1,4,1,3181,10,3,3,20,1,6),_PortConfigDuplex_Type())
portConfigDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigDuplex.setStatus(_A)
class _PortConfigFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('advertise',1),('avoid',2),(_K,254),(_D,255)))
_PortConfigFlowControl_Type.__name__=_B
_PortConfigFlowControl_Object=MibTableColumn
portConfigFlowControl=_PortConfigFlowControl_Object((1,3,6,1,4,1,3181,10,3,3,20,1,7),_PortConfigFlowControl_Type())
portConfigFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigFlowControl.setStatus(_A)
class _PortConfigPinout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,254,255)));namedValues=NamedValues(*(('auto',0),('mdi',1),('mdix',2),(_K,254),(_D,255)))
_PortConfigPinout_Type.__name__=_B
_PortConfigPinout_Object=MibTableColumn
portConfigPinout=_PortConfigPinout_Object((1,3,6,1,4,1,3181,10,3,3,20,1,8),_PortConfigPinout_Type())
portConfigPinout.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigPinout.setStatus(_A)
class _PortConfigFarEndFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_G,1),(_g,2),(_K,254),(_D,255)))
_PortConfigFarEndFault_Type.__name__=_B
_PortConfigFarEndFault_Object=MibTableColumn
portConfigFarEndFault=_PortConfigFarEndFault_Object((1,3,6,1,4,1,3181,10,3,3,20,1,9),_PortConfigFarEndFault_Type())
portConfigFarEndFault.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigFarEndFault.setStatus(_A)
class _PortConfigAdvertise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('advertiseGigabit',1),('avoidGigabit',2),(_K,254),(_D,255)))
_PortConfigAdvertise_Type.__name__=_B
_PortConfigAdvertise_Object=MibTableColumn
portConfigAdvertise=_PortConfigAdvertise_Object((1,3,6,1,4,1,3181,10,3,3,20,1,10),_PortConfigAdvertise_Type())
portConfigAdvertise.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigAdvertise.setStatus(_A)
class _PortConfigFibreDownDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_G,1),(_g,2),(_K,254),(_D,255)))
_PortConfigFibreDownDetection_Type.__name__=_B
_PortConfigFibreDownDetection_Object=MibTableColumn
portConfigFibreDownDetection=_PortConfigFibreDownDetection_Object((1,3,6,1,4,1,3181,10,3,3,20,1,11),_PortConfigFibreDownDetection_Type())
portConfigFibreDownDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigFibreDownDetection.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,3181,10,3,4))
class _VlanSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),('notsupported',255)))
_VlanSupport_Type.__name__=_B
_VlanSupport_Object=MibScalar
vlanSupport=_VlanSupport_Object((1,3,6,1,4,1,3181,10,3,4,1),_VlanSupport_Type())
vlanSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSupport.setStatus(_A)
class _VlanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_K,254),(_D,255)))
_VlanEnable_Type.__name__=_B
_VlanEnable_Object=MibScalar
vlanEnable=_VlanEnable_Object((1,3,6,1,4,1,3181,10,3,4,2),_VlanEnable_Type())
vlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanEnable.setStatus(_A)
class _VlanForceDefaultVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_G,1),(_F,2),('perport',3),(_D,255)))
_VlanForceDefaultVID_Type.__name__=_B
_VlanForceDefaultVID_Object=MibScalar
vlanForceDefaultVID=_VlanForceDefaultVID_Object((1,3,6,1,4,1,3181,10,3,4,3),_VlanForceDefaultVID_Type())
vlanForceDefaultVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanForceDefaultVID.setStatus(_A)
_VlanFilterCount_Type=Integer32
_VlanFilterCount_Object=MibScalar
vlanFilterCount=_VlanFilterCount_Object((1,3,6,1,4,1,3181,10,3,4,4),_VlanFilterCount_Type())
vlanFilterCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanFilterCount.setStatus(_A)
class _VlanVoiceVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanVoiceVID_Type.__name__=_B
_VlanVoiceVID_Object=MibScalar
vlanVoiceVID=_VlanVoiceVID_Object((1,3,6,1,4,1,3181,10,3,4,5),_VlanVoiceVID_Type())
vlanVoiceVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceVID.setStatus(_A)
class _VlanRstpVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanRstpVID_Type.__name__=_B
_VlanRstpVID_Object=MibScalar
vlanRstpVID=_VlanRstpVID_Object((1,3,6,1,4,1,3181,10,3,4,6),_VlanRstpVID_Type())
vlanRstpVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanRstpVID.setStatus(_A)
class _VlanUnauthVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanUnauthVID_Type.__name__=_B
_VlanUnauthVID_Object=MibScalar
vlanUnauthVID=_VlanUnauthVID_Object((1,3,6,1,4,1,3181,10,3,4,7),_VlanUnauthVID_Type())
vlanUnauthVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanUnauthVID.setStatus(_A)
_VlanPortTable_Object=MibTable
vlanPortTable=_VlanPortTable_Object((1,3,6,1,4,1,3181,10,3,4,10))
if mibBuilder.loadTexts:vlanPortTable.setStatus(_A)
_VlanPortTableEntry_Object=MibTableRow
vlanPortTableEntry=_VlanPortTableEntry_Object((1,3,6,1,4,1,3181,10,3,4,10,1))
vlanPortTableEntry.setIndexNames((0,_J,_h))
if mibBuilder.loadTexts:vlanPortTableEntry.setStatus(_A)
class _VlanPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_VlanPortId_Type.__name__=_B
_VlanPortId_Object=MibTableColumn
vlanPortId=_VlanPortId_Object((1,3,6,1,4,1,3181,10,3,4,10,1,1),_VlanPortId_Type())
vlanPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanPortId.setStatus(_A)
class _VlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,254,255)));namedValues=NamedValues(*(('access',1),('trunk',2),('hybrid',3),(_K,254),(_D,255)))
_VlanPortMode_Type.__name__=_B
_VlanPortMode_Object=MibTableColumn
vlanPortMode=_VlanPortMode_Object((1,3,6,1,4,1,3181,10,3,4,10,1,2),_VlanPortMode_Type())
vlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPortMode.setStatus(_A)
class _VlanDefaultVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanDefaultVID_Type.__name__=_B
_VlanDefaultVID_Object=MibTableColumn
vlanDefaultVID=_VlanDefaultVID_Object((1,3,6,1,4,1,3181,10,3,4,10,1,3),_VlanDefaultVID_Type())
vlanDefaultVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDefaultVID.setStatus(_A)
class _VlanDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanDefaultPriority_Type.__name__=_B
_VlanDefaultPriority_Object=MibTableColumn
vlanDefaultPriority=_VlanDefaultPriority_Object((1,3,6,1,4,1,3181,10,3,4,10,1,4),_VlanDefaultPriority_Type())
vlanDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDefaultPriority.setStatus(_A)
class _VlanPortFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_VlanPortFlags_Type.__name__=_B
_VlanPortFlags_Object=MibTableColumn
vlanPortFlags=_VlanPortFlags_Object((1,3,6,1,4,1,3181,10,3,4,10,1,5),_VlanPortFlags_Type())
vlanPortFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPortFlags.setStatus(_A)
_VlanFilterTable_Object=MibTable
vlanFilterTable=_VlanFilterTable_Object((1,3,6,1,4,1,3181,10,3,4,20))
if mibBuilder.loadTexts:vlanFilterTable.setStatus(_A)
_VlanFilterTableEntry_Object=MibTableRow
vlanFilterTableEntry=_VlanFilterTableEntry_Object((1,3,6,1,4,1,3181,10,3,4,20,1))
vlanFilterTableEntry.setIndexNames((0,_J,_i))
if mibBuilder.loadTexts:vlanFilterTableEntry.setStatus(_A)
class _VlanFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_VlanFilterId_Type.__name__=_B
_VlanFilterId_Object=MibTableColumn
vlanFilterId=_VlanFilterId_Object((1,3,6,1,4,1,3181,10,3,4,20,1,1),_VlanFilterId_Type())
vlanFilterId.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanFilterId.setStatus(_A)
class _VlanFilterVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanFilterVID_Type.__name__=_B
_VlanFilterVID_Object=MibTableColumn
vlanFilterVID=_VlanFilterVID_Object((1,3,6,1,4,1,3181,10,3,4,20,1,2),_VlanFilterVID_Type())
vlanFilterVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanFilterVID.setStatus(_A)
class _VlanFilterAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VlanFilterAlias_Type.__name__=_L
_VlanFilterAlias_Object=MibTableColumn
vlanFilterAlias=_VlanFilterAlias_Object((1,3,6,1,4,1,3181,10,3,4,20,1,3),_VlanFilterAlias_Type())
vlanFilterAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanFilterAlias.setStatus(_A)
class _VlanFilterEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_VlanFilterEnable_Type.__name__=_B
_VlanFilterEnable_Object=MibTableColumn
vlanFilterEnable=_VlanFilterEnable_Object((1,3,6,1,4,1,3181,10,3,4,20,1,4),_VlanFilterEnable_Type())
vlanFilterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanFilterEnable.setStatus(_A)
class _VlanMemberManager_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberManager_Type.__name__=_B
_VlanMemberManager_Object=MibTableColumn
vlanMemberManager=_VlanMemberManager_Object((1,3,6,1,4,1,3181,10,3,4,20,1,5),_VlanMemberManager_Type())
vlanMemberManager.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberManager.setStatus(_A)
class _VlanMemberPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort1_Type.__name__=_B
_VlanMemberPort1_Object=MibTableColumn
vlanMemberPort1=_VlanMemberPort1_Object((1,3,6,1,4,1,3181,10,3,4,20,1,6),_VlanMemberPort1_Type())
vlanMemberPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort1.setStatus(_A)
class _VlanMemberPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort2_Type.__name__=_B
_VlanMemberPort2_Object=MibTableColumn
vlanMemberPort2=_VlanMemberPort2_Object((1,3,6,1,4,1,3181,10,3,4,20,1,7),_VlanMemberPort2_Type())
vlanMemberPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort2.setStatus(_A)
class _VlanMemberPort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort3_Type.__name__=_B
_VlanMemberPort3_Object=MibTableColumn
vlanMemberPort3=_VlanMemberPort3_Object((1,3,6,1,4,1,3181,10,3,4,20,1,8),_VlanMemberPort3_Type())
vlanMemberPort3.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort3.setStatus(_A)
class _VlanMemberPort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort4_Type.__name__=_B
_VlanMemberPort4_Object=MibTableColumn
vlanMemberPort4=_VlanMemberPort4_Object((1,3,6,1,4,1,3181,10,3,4,20,1,9),_VlanMemberPort4_Type())
vlanMemberPort4.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort4.setStatus(_A)
class _VlanMemberPort5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort5_Type.__name__=_B
_VlanMemberPort5_Object=MibTableColumn
vlanMemberPort5=_VlanMemberPort5_Object((1,3,6,1,4,1,3181,10,3,4,20,1,10),_VlanMemberPort5_Type())
vlanMemberPort5.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort5.setStatus(_A)
class _VlanMemberPort6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort6_Type.__name__=_B
_VlanMemberPort6_Object=MibTableColumn
vlanMemberPort6=_VlanMemberPort6_Object((1,3,6,1,4,1,3181,10,3,4,20,1,11),_VlanMemberPort6_Type())
vlanMemberPort6.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort6.setStatus(_A)
class _VlanMemberPort7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort7_Type.__name__=_B
_VlanMemberPort7_Object=MibTableColumn
vlanMemberPort7=_VlanMemberPort7_Object((1,3,6,1,4,1,3181,10,3,4,20,1,12),_VlanMemberPort7_Type())
vlanMemberPort7.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort7.setStatus(_A)
class _VlanMemberPort8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort8_Type.__name__=_B
_VlanMemberPort8_Object=MibTableColumn
vlanMemberPort8=_VlanMemberPort8_Object((1,3,6,1,4,1,3181,10,3,4,20,1,13),_VlanMemberPort8_Type())
vlanMemberPort8.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort8.setStatus(_A)
class _VlanMemberPort9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort9_Type.__name__=_B
_VlanMemberPort9_Object=MibTableColumn
vlanMemberPort9=_VlanMemberPort9_Object((1,3,6,1,4,1,3181,10,3,4,20,1,14),_VlanMemberPort9_Type())
vlanMemberPort9.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort9.setStatus(_A)
class _VlanMemberPort10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort10_Type.__name__=_B
_VlanMemberPort10_Object=MibTableColumn
vlanMemberPort10=_VlanMemberPort10_Object((1,3,6,1,4,1,3181,10,3,4,20,1,15),_VlanMemberPort10_Type())
vlanMemberPort10.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort10.setStatus(_A)
class _VlanMemberPort11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort11_Type.__name__=_B
_VlanMemberPort11_Object=MibTableColumn
vlanMemberPort11=_VlanMemberPort11_Object((1,3,6,1,4,1,3181,10,3,4,20,1,16),_VlanMemberPort11_Type())
vlanMemberPort11.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort11.setStatus(_A)
class _VlanMemberPort12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort12_Type.__name__=_B
_VlanMemberPort12_Object=MibTableColumn
vlanMemberPort12=_VlanMemberPort12_Object((1,3,6,1,4,1,3181,10,3,4,20,1,17),_VlanMemberPort12_Type())
vlanMemberPort12.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort12.setStatus(_A)
class _VlanMemberPort13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort13_Type.__name__=_B
_VlanMemberPort13_Object=MibTableColumn
vlanMemberPort13=_VlanMemberPort13_Object((1,3,6,1,4,1,3181,10,3,4,20,1,18),_VlanMemberPort13_Type())
vlanMemberPort13.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort13.setStatus(_A)
class _VlanMemberPort14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort14_Type.__name__=_B
_VlanMemberPort14_Object=MibTableColumn
vlanMemberPort14=_VlanMemberPort14_Object((1,3,6,1,4,1,3181,10,3,4,20,1,19),_VlanMemberPort14_Type())
vlanMemberPort14.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort14.setStatus(_A)
class _VlanMemberPort15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort15_Type.__name__=_B
_VlanMemberPort15_Object=MibTableColumn
vlanMemberPort15=_VlanMemberPort15_Object((1,3,6,1,4,1,3181,10,3,4,20,1,20),_VlanMemberPort15_Type())
vlanMemberPort15.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort15.setStatus(_A)
class _VlanMemberPort16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort16_Type.__name__=_B
_VlanMemberPort16_Object=MibTableColumn
vlanMemberPort16=_VlanMemberPort16_Object((1,3,6,1,4,1,3181,10,3,4,20,1,21),_VlanMemberPort16_Type())
vlanMemberPort16.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort16.setStatus(_A)
class _VlanMemberPort17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort17_Type.__name__=_B
_VlanMemberPort17_Object=MibTableColumn
vlanMemberPort17=_VlanMemberPort17_Object((1,3,6,1,4,1,3181,10,3,4,20,1,22),_VlanMemberPort17_Type())
vlanMemberPort17.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort17.setStatus(_A)
class _VlanMemberPort18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort18_Type.__name__=_B
_VlanMemberPort18_Object=MibTableColumn
vlanMemberPort18=_VlanMemberPort18_Object((1,3,6,1,4,1,3181,10,3,4,20,1,23),_VlanMemberPort18_Type())
vlanMemberPort18.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort18.setStatus(_A)
class _VlanMemberPort19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort19_Type.__name__=_B
_VlanMemberPort19_Object=MibTableColumn
vlanMemberPort19=_VlanMemberPort19_Object((1,3,6,1,4,1,3181,10,3,4,20,1,24),_VlanMemberPort19_Type())
vlanMemberPort19.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort19.setStatus(_A)
class _VlanMemberPort20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort20_Type.__name__=_B
_VlanMemberPort20_Object=MibTableColumn
vlanMemberPort20=_VlanMemberPort20_Object((1,3,6,1,4,1,3181,10,3,4,20,1,25),_VlanMemberPort20_Type())
vlanMemberPort20.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort20.setStatus(_A)
class _VlanMemberPort21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort21_Type.__name__=_B
_VlanMemberPort21_Object=MibTableColumn
vlanMemberPort21=_VlanMemberPort21_Object((1,3,6,1,4,1,3181,10,3,4,20,1,26),_VlanMemberPort21_Type())
vlanMemberPort21.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort21.setStatus(_A)
class _VlanMemberPort22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort22_Type.__name__=_B
_VlanMemberPort22_Object=MibTableColumn
vlanMemberPort22=_VlanMemberPort22_Object((1,3,6,1,4,1,3181,10,3,4,20,1,27),_VlanMemberPort22_Type())
vlanMemberPort22.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort22.setStatus(_A)
class _VlanMemberPort23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort23_Type.__name__=_B
_VlanMemberPort23_Object=MibTableColumn
vlanMemberPort23=_VlanMemberPort23_Object((1,3,6,1,4,1,3181,10,3,4,20,1,28),_VlanMemberPort23_Type())
vlanMemberPort23.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort23.setStatus(_A)
class _VlanMemberPort24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_VlanMemberPort24_Type.__name__=_B
_VlanMemberPort24_Object=MibTableColumn
vlanMemberPort24=_VlanMemberPort24_Object((1,3,6,1,4,1,3181,10,3,4,20,1,29),_VlanMemberPort24_Type())
vlanMemberPort24.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMemberPort24.setStatus(_A)
_VlanFilterEnhTable_Object=MibTable
vlanFilterEnhTable=_VlanFilterEnhTable_Object((1,3,6,1,4,1,3181,10,3,4,30))
if mibBuilder.loadTexts:vlanFilterEnhTable.setStatus(_A)
_VlanFilterEnhTableEntry_Object=MibTableRow
vlanFilterEnhTableEntry=_VlanFilterEnhTableEntry_Object((1,3,6,1,4,1,3181,10,3,4,30,1))
vlanFilterEnhTableEntry.setIndexNames((0,_J,_j))
if mibBuilder.loadTexts:vlanFilterEnhTableEntry.setStatus(_A)
class _VlanFilterEnhId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_VlanFilterEnhId_Type.__name__=_B
_VlanFilterEnhId_Object=MibTableColumn
vlanFilterEnhId=_VlanFilterEnhId_Object((1,3,6,1,4,1,3181,10,3,4,30,1,1),_VlanFilterEnhId_Type())
vlanFilterEnhId.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanFilterEnhId.setStatus(_A)
class _VlanFilterEnhFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_VlanFilterEnhFlags_Type.__name__=_B
_VlanFilterEnhFlags_Object=MibTableColumn
vlanFilterEnhFlags=_VlanFilterEnhFlags_Object((1,3,6,1,4,1,3181,10,3,4,30,1,2),_VlanFilterEnhFlags_Type())
vlanFilterEnhFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanFilterEnhFlags.setStatus(_A)
class _VlanFilterEnhPriOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanFilterEnhPriOverride_Type.__name__=_B
_VlanFilterEnhPriOverride_Object=MibTableColumn
vlanFilterEnhPriOverride=_VlanFilterEnhPriOverride_Object((1,3,6,1,4,1,3181,10,3,4,30,1,3),_VlanFilterEnhPriOverride_Type())
vlanFilterEnhPriOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanFilterEnhPriOverride.setStatus(_A)
_Prioritization_ObjectIdentity=ObjectIdentity
prioritization=_Prioritization_ObjectIdentity((1,3,6,1,4,1,3181,10,3,5))
class _PrioSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_PrioSupport_Type.__name__=_B
_PrioSupport_Object=MibScalar
prioSupport=_PrioSupport_Object((1,3,6,1,4,1,3181,10,3,5,1),_PrioSupport_Type())
prioSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:prioSupport.setStatus(_A)
_PrioQueueCount_Type=Integer32
_PrioQueueCount_Object=MibScalar
prioQueueCount=_PrioQueueCount_Object((1,3,6,1,4,1,3181,10,3,5,2),_PrioQueueCount_Type())
prioQueueCount.setMaxAccess(_E)
if mibBuilder.loadTexts:prioQueueCount.setStatus(_A)
class _PrioQueueScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('weighted',1),(_P,2),(_D,255)))
_PrioQueueScheme_Type.__name__=_B
_PrioQueueScheme_Object=MibScalar
prioQueueScheme=_PrioQueueScheme_Object((1,3,6,1,4,1,3181,10,3,5,3),_PrioQueueScheme_Type())
prioQueueScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:prioQueueScheme.setStatus(_A)
class _PrioPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PrioPortEnable_Type.__name__=_B
_PrioPortEnable_Object=MibScalar
prioPortEnable=_PrioPortEnable_Object((1,3,6,1,4,1,3181,10,3,5,4),_PrioPortEnable_Type())
prioPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:prioPortEnable.setStatus(_A)
class _PrioIeeeTagEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PrioIeeeTagEnable_Type.__name__=_B
_PrioIeeeTagEnable_Object=MibScalar
prioIeeeTagEnable=_PrioIeeeTagEnable_Object((1,3,6,1,4,1,3181,10,3,5,5),_PrioIeeeTagEnable_Type())
prioIeeeTagEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIeeeTagEnable.setStatus(_A)
class _PrioDiffservEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PrioDiffservEnable_Type.__name__=_B
_PrioDiffservEnable_Object=MibScalar
prioDiffservEnable=_PrioDiffservEnable_Object((1,3,6,1,4,1,3181,10,3,5,6),_PrioDiffservEnable_Type())
prioDiffservEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:prioDiffservEnable.setStatus(_A)
_PrioPortTable_Object=MibTable
prioPortTable=_PrioPortTable_Object((1,3,6,1,4,1,3181,10,3,5,10))
if mibBuilder.loadTexts:prioPortTable.setStatus(_A)
_PrioPortTableEntry_Object=MibTableRow
prioPortTableEntry=_PrioPortTableEntry_Object((1,3,6,1,4,1,3181,10,3,5,10,1))
prioPortTableEntry.setIndexNames((0,_J,_k))
if mibBuilder.loadTexts:prioPortTableEntry.setStatus(_A)
class _PrioPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PrioPortId_Type.__name__=_B
_PrioPortId_Object=MibTableColumn
prioPortId=_PrioPortId_Object((1,3,6,1,4,1,3181,10,3,5,10,1,1),_PrioPortId_Type())
prioPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:prioPortId.setStatus(_A)
class _PrioPortQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_PrioPortQueue_Type.__name__=_B
_PrioPortQueue_Object=MibTableColumn
prioPortQueue=_PrioPortQueue_Object((1,3,6,1,4,1,3181,10,3,5,10,1,2),_PrioPortQueue_Type())
prioPortQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:prioPortQueue.setStatus(_A)
_PrioIeeeTagTable_Object=MibTable
prioIeeeTagTable=_PrioIeeeTagTable_Object((1,3,6,1,4,1,3181,10,3,5,20))
if mibBuilder.loadTexts:prioIeeeTagTable.setStatus(_A)
_PrioIeeeTagTableEntry_Object=MibTableRow
prioIeeeTagTableEntry=_PrioIeeeTagTableEntry_Object((1,3,6,1,4,1,3181,10,3,5,20,1))
prioIeeeTagTableEntry.setIndexNames((0,_J,_l))
if mibBuilder.loadTexts:prioIeeeTagTableEntry.setStatus(_A)
class _PrioIeeeTagId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIeeeTagId_Type.__name__=_B
_PrioIeeeTagId_Object=MibTableColumn
prioIeeeTagId=_PrioIeeeTagId_Object((1,3,6,1,4,1,3181,10,3,5,20,1,1),_PrioIeeeTagId_Type())
prioIeeeTagId.setMaxAccess(_E)
if mibBuilder.loadTexts:prioIeeeTagId.setStatus(_A)
_PrioIeeeTagQueue_Type=Integer32
_PrioIeeeTagQueue_Object=MibTableColumn
prioIeeeTagQueue=_PrioIeeeTagQueue_Object((1,3,6,1,4,1,3181,10,3,5,20,1,2),_PrioIeeeTagQueue_Type())
prioIeeeTagQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIeeeTagQueue.setStatus(_A)
_PrioDiffservTable_Object=MibTable
prioDiffservTable=_PrioDiffservTable_Object((1,3,6,1,4,1,3181,10,3,5,30))
if mibBuilder.loadTexts:prioDiffservTable.setStatus(_A)
_PrioDiffservTableEntry_Object=MibTableRow
prioDiffservTableEntry=_PrioDiffservTableEntry_Object((1,3,6,1,4,1,3181,10,3,5,30,1))
prioDiffservTableEntry.setIndexNames((0,_J,_m))
if mibBuilder.loadTexts:prioDiffservTableEntry.setStatus(_A)
class _PrioDiffservId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PrioDiffservId_Type.__name__=_B
_PrioDiffservId_Object=MibTableColumn
prioDiffservId=_PrioDiffservId_Object((1,3,6,1,4,1,3181,10,3,5,30,1,1),_PrioDiffservId_Type())
prioDiffservId.setMaxAccess(_E)
if mibBuilder.loadTexts:prioDiffservId.setStatus(_A)
_PrioDiffservQueue_Type=Integer32
_PrioDiffservQueue_Object=MibTableColumn
prioDiffservQueue=_PrioDiffservQueue_Object((1,3,6,1,4,1,3181,10,3,5,30,1,2),_PrioDiffservQueue_Type())
prioDiffservQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:prioDiffservQueue.setStatus(_A)
_Monitor_ObjectIdentity=ObjectIdentity
monitor=_Monitor_ObjectIdentity((1,3,6,1,4,1,3181,10,3,6))
class _MonitorSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_MonitorSupport_Type.__name__=_B
_MonitorSupport_Object=MibScalar
monitorSupport=_MonitorSupport_Object((1,3,6,1,4,1,3181,10,3,6,1),_MonitorSupport_Type())
monitorSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:monitorSupport.setStatus(_A)
class _MonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('txonly',1),('both',2),(_F,3),('hubmode',4),(_D,255)))
_MonitorMode_Type.__name__=_B
_MonitorMode_Object=MibScalar
monitorMode=_MonitorMode_Object((1,3,6,1,4,1,3181,10,3,6,2),_MonitorMode_Type())
monitorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:monitorMode.setStatus(_A)
class _MonitorSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_MonitorSource_Type.__name__=_B
_MonitorSource_Object=MibScalar
monitorSource=_MonitorSource_Object((1,3,6,1,4,1,3181,10,3,6,3),_MonitorSource_Type())
monitorSource.setMaxAccess(_C)
if mibBuilder.loadTexts:monitorSource.setStatus(_A)
class _MonitorDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_MonitorDestination_Type.__name__=_B
_MonitorDestination_Object=MibScalar
monitorDestination=_MonitorDestination_Object((1,3,6,1,4,1,3181,10,3,6,4),_MonitorDestination_Type())
monitorDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:monitorDestination.setStatus(_A)
_Ring_ObjectIdentity=ObjectIdentity
ring=_Ring_ObjectIdentity((1,3,6,1,4,1,3181,10,3,7))
class _RingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_RingSupport_Type.__name__=_B
_RingSupport_Object=MibScalar
ringSupport=_RingSupport_Object((1,3,6,1,4,1,3181,10,3,7,1),_RingSupport_Type())
ringSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:ringSupport.setStatus(_A)
_RingCount_Type=Integer32
_RingCount_Object=MibScalar
ringCount=_RingCount_Object((1,3,6,1,4,1,3181,10,3,7,2),_RingCount_Type())
ringCount.setMaxAccess(_E)
if mibBuilder.loadTexts:ringCount.setStatus(_A)
_RingTable_Object=MibTable
ringTable=_RingTable_Object((1,3,6,1,4,1,3181,10,3,7,10))
if mibBuilder.loadTexts:ringTable.setStatus(_A)
_RingTableEntry_Object=MibTableRow
ringTableEntry=_RingTableEntry_Object((1,3,6,1,4,1,3181,10,3,7,10,1))
ringTableEntry.setIndexNames((0,_J,_n))
if mibBuilder.loadTexts:ringTableEntry.setStatus(_A)
class _RingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_RingId_Type.__name__=_B
_RingId_Object=MibTableColumn
ringId=_RingId_Object((1,3,6,1,4,1,3181,10,3,7,10,1,1),_RingId_Type())
ringId.setMaxAccess(_E)
if mibBuilder.loadTexts:ringId.setStatus(_A)
class _RingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('slave',1),('master',2),(_F,3),(_D,255)))
_RingMode_Type.__name__=_B
_RingMode_Object=MibTableColumn
ringMode=_RingMode_Object((1,3,6,1,4,1,3181,10,3,7,10,1,2),_RingMode_Type())
ringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ringMode.setStatus(_A)
class _RingPortA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_RingPortA_Type.__name__=_B
_RingPortA_Object=MibTableColumn
ringPortA=_RingPortA_Object((1,3,6,1,4,1,3181,10,3,7,10,1,3),_RingPortA_Type())
ringPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:ringPortA.setStatus(_A)
class _RingPortB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_RingPortB_Type.__name__=_B
_RingPortB_Object=MibTableColumn
ringPortB=_RingPortB_Object((1,3,6,1,4,1,3181,10,3,7,10,1,4),_RingPortB_Type())
ringPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:ringPortB.setStatus(_A)
class _RingNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RingNumber_Type.__name__=_B
_RingNumber_Object=MibTableColumn
ringNumber=_RingNumber_Object((1,3,6,1,4,1,3181,10,3,7,10,1,5),_RingNumber_Type())
ringNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ringNumber.setStatus(_A)
class _RingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('ringOk',1),('ringFailure',2),('ringDisabled',3),(_D,255)))
_RingStatus_Type.__name__=_B
_RingStatus_Object=MibTableColumn
ringStatus=_RingStatus_Object((1,3,6,1,4,1,3181,10,3,7,10,1,6),_RingStatus_Type())
ringStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ringStatus.setStatus(_A)
_RingAlarmDuration_Type=TimeTicks
_RingAlarmDuration_Object=MibTableColumn
ringAlarmDuration=_RingAlarmDuration_Object((1,3,6,1,4,1,3181,10,3,7,10,1,7),_RingAlarmDuration_Type())
ringAlarmDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:ringAlarmDuration.setStatus(_A)
_Couplingred_ObjectIdentity=ObjectIdentity
couplingred=_Couplingred_ObjectIdentity((1,3,6,1,4,1,3181,10,3,8))
class _CouplingredSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_CouplingredSupport_Type.__name__=_B
_CouplingredSupport_Object=MibScalar
couplingredSupport=_CouplingredSupport_Object((1,3,6,1,4,1,3181,10,3,8,1),_CouplingredSupport_Type())
couplingredSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:couplingredSupport.setStatus(_A)
class _CouplingredPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CouplingredPort_Type.__name__=_B
_CouplingredPort_Object=MibScalar
couplingredPort=_CouplingredPort_Object((1,3,6,1,4,1,3181,10,3,8,2),_CouplingredPort_Type())
couplingredPort.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingredPort.setStatus(_A)
class _CouplingredMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('backup',1),('main',2),(_F,3),(_D,255)))
_CouplingredMode_Type.__name__=_B
_CouplingredMode_Object=MibScalar
couplingredMode=_CouplingredMode_Object((1,3,6,1,4,1,3181,10,3,8,3),_CouplingredMode_Type())
couplingredMode.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingredMode.setStatus(_A)
_CouplingredPartnerIpv4Address_Type=IpAddress
_CouplingredPartnerIpv4Address_Object=MibScalar
couplingredPartnerIpv4Address=_CouplingredPartnerIpv4Address_Object((1,3,6,1,4,1,3181,10,3,8,4),_CouplingredPartnerIpv4Address_Type())
couplingredPartnerIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingredPartnerIpv4Address.setStatus(_A)
class _CouplingredStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*((_F,0),(_o,1),('link',2),(_p,3),(_q,4),(_K,5),(_D,255)))
_CouplingredStatus_Type.__name__=_B
_CouplingredStatus_Object=MibScalar
couplingredStatus=_CouplingredStatus_Object((1,3,6,1,4,1,3181,10,3,8,5),_CouplingredStatus_Type())
couplingredStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:couplingredStatus.setStatus(_A)
class _CouplingredPartnerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*((_F,0),(_o,1),('link',2),(_p,3),(_q,4),(_K,5),(_D,255)))
_CouplingredPartnerStatus_Type.__name__=_B
_CouplingredPartnerStatus_Object=MibScalar
couplingredPartnerStatus=_CouplingredPartnerStatus_Object((1,3,6,1,4,1,3181,10,3,8,6),_CouplingredPartnerStatus_Type())
couplingredPartnerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:couplingredPartnerStatus.setStatus(_A)
_CouplingredValidationFlag_Type=Integer32
_CouplingredValidationFlag_Object=MibScalar
couplingredValidationFlag=_CouplingredValidationFlag_Object((1,3,6,1,4,1,3181,10,3,8,7),_CouplingredValidationFlag_Type())
couplingredValidationFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:couplingredValidationFlag.setStatus(_A)
_Sfp_ObjectIdentity=ObjectIdentity
sfp=_Sfp_ObjectIdentity((1,3,6,1,4,1,3181,10,3,9))
class _SfpSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_SfpSupport_Type.__name__=_B
_SfpSupport_Object=MibScalar
sfpSupport=_SfpSupport_Object((1,3,6,1,4,1,3181,10,3,9,1),_SfpSupport_Type())
sfpSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpSupport.setStatus(_A)
_SfpCount_Type=Integer32
_SfpCount_Object=MibScalar
sfpCount=_SfpCount_Object((1,3,6,1,4,1,3181,10,3,9,2),_SfpCount_Type())
sfpCount.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpCount.setStatus(_A)
_SfpTable_Object=MibTable
sfpTable=_SfpTable_Object((1,3,6,1,4,1,3181,10,3,9,10))
if mibBuilder.loadTexts:sfpTable.setStatus(_A)
_SfpTableEntry_Object=MibTableRow
sfpTableEntry=_SfpTableEntry_Object((1,3,6,1,4,1,3181,10,3,9,10,1))
sfpTableEntry.setIndexNames((0,_J,'sfpId'))
if mibBuilder.loadTexts:sfpTableEntry.setStatus(_A)
class _SfpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SfpId_Type.__name__=_B
_SfpId_Object=MibTableColumn
sfpId=_SfpId_Object((1,3,6,1,4,1,3181,10,3,9,10,1,1),_SfpId_Type())
sfpId.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpId.setStatus(_A)
_SfpPortnumber_Type=Integer32
_SfpPortnumber_Object=MibTableColumn
sfpPortnumber=_SfpPortnumber_Object((1,3,6,1,4,1,3181,10,3,9,10,1,2),_SfpPortnumber_Type())
sfpPortnumber.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpPortnumber.setStatus(_A)
class _SfpDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('plugged',1),('unplugged',2),(_D,255)))
_SfpDetect_Type.__name__=_B
_SfpDetect_Object=MibTableColumn
sfpDetect=_SfpDetect_Object((1,3,6,1,4,1,3181,10,3,9,10,1,3),_SfpDetect_Type())
sfpDetect.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpDetect.setStatus(_A)
class _SfpVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendor_Type.__name__=_L
_SfpVendor_Object=MibTableColumn
sfpVendor=_SfpVendor_Object((1,3,6,1,4,1,3181,10,3,9,10,1,4),_SfpVendor_Type())
sfpVendor.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpVendor.setStatus(_A)
class _SfpVendorPartnumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorPartnumber_Type.__name__=_L
_SfpVendorPartnumber_Object=MibTableColumn
sfpVendorPartnumber=_SfpVendorPartnumber_Object((1,3,6,1,4,1,3181,10,3,9,10,1,5),_SfpVendorPartnumber_Type())
sfpVendorPartnumber.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpVendorPartnumber.setStatus(_A)
class _SfpVendorSerialnumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorSerialnumber_Type.__name__=_L
_SfpVendorSerialnumber_Object=MibTableColumn
sfpVendorSerialnumber=_SfpVendorSerialnumber_Object((1,3,6,1,4,1,3181,10,3,9,10,1,6),_SfpVendorSerialnumber_Type())
sfpVendorSerialnumber.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpVendorSerialnumber.setStatus(_A)
class _SfpConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7,8,255)));namedValues=NamedValues(*(('connSC',1),('connLC',7),('connMTRJ',8),(_D,255)))
_SfpConnector_Type.__name__=_B
_SfpConnector_Object=MibTableColumn
sfpConnector=_SfpConnector_Object((1,3,6,1,4,1,3181,10,3,9,10,1,7),_SfpConnector_Type())
sfpConnector.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpConnector.setStatus(_A)
_SfpNominalBitrate_Type=Integer32
_SfpNominalBitrate_Object=MibTableColumn
sfpNominalBitrate=_SfpNominalBitrate_Object((1,3,6,1,4,1,3181,10,3,9,10,1,8),_SfpNominalBitrate_Type())
sfpNominalBitrate.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpNominalBitrate.setStatus(_A)
class _SfpDiagnostic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('supportedWithInternalCalibration',1),('supportedWithExternalCalibration',2),(_K,254),(_D,255)))
_SfpDiagnostic_Type.__name__=_B
_SfpDiagnostic_Object=MibTableColumn
sfpDiagnostic=_SfpDiagnostic_Object((1,3,6,1,4,1,3181,10,3,9,10,1,9),_SfpDiagnostic_Type())
sfpDiagnostic.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpDiagnostic.setStatus(_A)
_SfpTemperature_Type=Integer32
_SfpTemperature_Object=MibTableColumn
sfpTemperature=_SfpTemperature_Object((1,3,6,1,4,1,3181,10,3,9,10,1,10),_SfpTemperature_Type())
sfpTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpTemperature.setStatus(_A)
_SfpVoltage_Type=Integer32
_SfpVoltage_Object=MibTableColumn
sfpVoltage=_SfpVoltage_Object((1,3,6,1,4,1,3181,10,3,9,10,1,11),_SfpVoltage_Type())
sfpVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpVoltage.setStatus(_A)
_SfpTxBias_Type=Integer32
_SfpTxBias_Object=MibTableColumn
sfpTxBias=_SfpTxBias_Object((1,3,6,1,4,1,3181,10,3,9,10,1,12),_SfpTxBias_Type())
sfpTxBias.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpTxBias.setStatus(_A)
_SfpTxPower_Type=Integer32
_SfpTxPower_Object=MibTableColumn
sfpTxPower=_SfpTxPower_Object((1,3,6,1,4,1,3181,10,3,9,10,1,13),_SfpTxPower_Type())
sfpTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpTxPower.setStatus(_A)
_SfpRxPower_Type=Integer32
_SfpRxPower_Object=MibTableColumn
sfpRxPower=_SfpRxPower_Object((1,3,6,1,4,1,3181,10,3,9,10,1,14),_SfpRxPower_Type())
sfpRxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpRxPower.setStatus(_A)
class _SfpWarnings_Type(Bits):namedValues=NamedValues(*(('tempHighWarn',0),('tempLowWarn',1),('vccHighWarn',2),('vccLowWarn',3),('txBiasHighWarn',4),('txBiasLowWarn',5),('txPowerHighWarn',6),('txPowerLowWarn',7),('rxPowerHighWarn',8),('rxPowerLowWarn',9)))
_SfpWarnings_Type.__name__=_Q
_SfpWarnings_Object=MibTableColumn
sfpWarnings=_SfpWarnings_Object((1,3,6,1,4,1,3181,10,3,9,10,1,15),_SfpWarnings_Type())
sfpWarnings.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpWarnings.setStatus(_A)
class _SfpAlarms_Type(Bits):namedValues=NamedValues(*(('tempHighAlarm',0),('tempLowAlarm',1),('vccHighAlarm',2),('vccLowAlarm',3),('txBiasHighAlarm',4),('txBiasLowAlarm',5),('txPowerHighAlarm',6),('txPowerLowAlarm',7),('rxPowerHighAlarm',8),('rxPowerLowAlarm',9)))
_SfpAlarms_Type.__name__=_Q
_SfpAlarms_Object=MibTableColumn
sfpAlarms=_SfpAlarms_Object((1,3,6,1,4,1,3181,10,3,9,10,1,16),_SfpAlarms_Type())
sfpAlarms.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpAlarms.setStatus(_A)
_Relais_ObjectIdentity=ObjectIdentity
relais=_Relais_ObjectIdentity((1,3,6,1,4,1,3181,10,3,11))
class _RelaisSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_RelaisSupport_Type.__name__=_B
_RelaisSupport_Object=MibScalar
relaisSupport=_RelaisSupport_Object((1,3,6,1,4,1,3181,10,3,11,1),_RelaisSupport_Type())
relaisSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:relaisSupport.setStatus(_A)
_RelaisCount_Type=Integer32
_RelaisCount_Object=MibScalar
relaisCount=_RelaisCount_Object((1,3,6,1,4,1,3181,10,3,11,2),_RelaisCount_Type())
relaisCount.setMaxAccess(_E)
if mibBuilder.loadTexts:relaisCount.setStatus(_A)
_RelaisTable_Object=MibTable
relaisTable=_RelaisTable_Object((1,3,6,1,4,1,3181,10,3,11,10))
if mibBuilder.loadTexts:relaisTable.setStatus(_A)
_RelaisTableEntry_Object=MibTableRow
relaisTableEntry=_RelaisTableEntry_Object((1,3,6,1,4,1,3181,10,3,11,10,1))
relaisTableEntry.setIndexNames((0,_J,_r))
if mibBuilder.loadTexts:relaisTableEntry.setStatus(_A)
class _RelaisId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RelaisId_Type.__name__=_B
_RelaisId_Object=MibTableColumn
relaisId=_RelaisId_Object((1,3,6,1,4,1,3181,10,3,11,10,1,1),_RelaisId_Type())
relaisId.setMaxAccess(_E)
if mibBuilder.loadTexts:relaisId.setStatus(_A)
class _RelaisAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RelaisAlias_Type.__name__=_L
_RelaisAlias_Object=MibTableColumn
relaisAlias=_RelaisAlias_Object((1,3,6,1,4,1,3181,10,3,11,10,1,2),_RelaisAlias_Type())
relaisAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:relaisAlias.setStatus(_A)
class _RelaisMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('openOnEvent',1),('closeOnEvent',2),(_D,255)))
_RelaisMode_Type.__name__=_B
_RelaisMode_Object=MibTableColumn
relaisMode=_RelaisMode_Object((1,3,6,1,4,1,3181,10,3,11,10,1,3),_RelaisMode_Type())
relaisMode.setMaxAccess(_C)
if mibBuilder.loadTexts:relaisMode.setStatus(_A)
class _RelaisStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('closed',1),('opened',2),(_D,255)))
_RelaisStatus_Type.__name__=_B
_RelaisStatus_Object=MibTableColumn
relaisStatus=_RelaisStatus_Object((1,3,6,1,4,1,3181,10,3,11,10,1,4),_RelaisStatus_Type())
relaisStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:relaisStatus.setStatus(_A)
_Portaccessctrl_ObjectIdentity=ObjectIdentity
portaccessctrl=_Portaccessctrl_ObjectIdentity((1,3,6,1,4,1,3181,10,3,12))
class _PacSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_PacSupport_Type.__name__=_B
_PacSupport_Object=MibScalar
pacSupport=_PacSupport_Object((1,3,6,1,4,1,3181,10,3,12,1),_PacSupport_Type())
pacSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:pacSupport.setStatus(_A)
class _PacEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacEnable_Type.__name__=_B
_PacEnable_Object=MibScalar
pacEnable=_PacEnable_Object((1,3,6,1,4,1,3181,10,3,12,2),_PacEnable_Type())
pacEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pacEnable.setStatus(_A)
class _PacUnauthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('block',1),('useDefaultVID',2),(_D,255)))
_PacUnauthMode_Type.__name__=_B
_PacUnauthMode_Object=MibScalar
pacUnauthMode=_PacUnauthMode_Object((1,3,6,1,4,1,3181,10,3,12,3),_PacUnauthMode_Type())
pacUnauthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pacUnauthMode.setStatus(_A)
class _PacUnauthVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PacUnauthVID_Type.__name__=_B
_PacUnauthVID_Object=MibScalar
pacUnauthVID=_PacUnauthVID_Object((1,3,6,1,4,1,3181,10,3,12,4),_PacUnauthVID_Type())
pacUnauthVID.setMaxAccess(_C)
if mibBuilder.loadTexts:pacUnauthVID.setStatus(_A)
_PacMaxNumberOfAllowedHostsPerPort_Type=Integer32
_PacMaxNumberOfAllowedHostsPerPort_Object=MibScalar
pacMaxNumberOfAllowedHostsPerPort=_PacMaxNumberOfAllowedHostsPerPort_Object((1,3,6,1,4,1,3181,10,3,12,5),_PacMaxNumberOfAllowedHostsPerPort_Type())
pacMaxNumberOfAllowedHostsPerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:pacMaxNumberOfAllowedHostsPerPort.setStatus(_A)
class _PacFallbackRequestEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacFallbackRequestEnable_Type.__name__=_B
_PacFallbackRequestEnable_Object=MibScalar
pacFallbackRequestEnable=_PacFallbackRequestEnable_Object((1,3,6,1,4,1,3181,10,3,12,6),_PacFallbackRequestEnable_Type())
pacFallbackRequestEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pacFallbackRequestEnable.setStatus(_A)
class _PacFallbackRequestTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_PacFallbackRequestTimeout_Type.__name__=_B
_PacFallbackRequestTimeout_Object=MibScalar
pacFallbackRequestTimeout=_PacFallbackRequestTimeout_Object((1,3,6,1,4,1,3181,10,3,12,7),_PacFallbackRequestTimeout_Type())
pacFallbackRequestTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pacFallbackRequestTimeout.setStatus(_A)
class _PacFallbackRejectsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacFallbackRejectsEnable_Type.__name__=_B
_PacFallbackRejectsEnable_Object=MibScalar
pacFallbackRejectsEnable=_PacFallbackRejectsEnable_Object((1,3,6,1,4,1,3181,10,3,12,8),_PacFallbackRejectsEnable_Type())
pacFallbackRejectsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pacFallbackRejectsEnable.setStatus(_A)
class _PacFallbackMaxRejects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PacFallbackMaxRejects_Type.__name__=_B
_PacFallbackMaxRejects_Object=MibScalar
pacFallbackMaxRejects=_PacFallbackMaxRejects_Object((1,3,6,1,4,1,3181,10,3,12,9),_PacFallbackMaxRejects_Type())
pacFallbackMaxRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pacFallbackMaxRejects.setStatus(_A)
class _PacSupplicantTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PacSupplicantTimeout_Type.__name__=_B
_PacSupplicantTimeout_Object=MibScalar
pacSupplicantTimeout=_PacSupplicantTimeout_Object((1,3,6,1,4,1,3181,10,3,12,10),_PacSupplicantTimeout_Type())
pacSupplicantTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pacSupplicantTimeout.setStatus(_A)
class _PacReauthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacReauthEnable_Type.__name__=_B
_PacReauthEnable_Object=MibScalar
pacReauthEnable=_PacReauthEnable_Object((1,3,6,1,4,1,3181,10,3,12,11),_PacReauthEnable_Type())
pacReauthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pacReauthEnable.setStatus(_A)
class _PacReauthTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PacReauthTime_Type.__name__=_B
_PacReauthTime_Object=MibScalar
pacReauthTime=_PacReauthTime_Object((1,3,6,1,4,1,3181,10,3,12,12),_PacReauthTime_Type())
pacReauthTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pacReauthTime.setStatus(_A)
_PacStatusTable_Object=MibTable
pacStatusTable=_PacStatusTable_Object((1,3,6,1,4,1,3181,10,3,12,100))
if mibBuilder.loadTexts:pacStatusTable.setStatus(_A)
_PacStatusTableEntry_Object=MibTableRow
pacStatusTableEntry=_PacStatusTableEntry_Object((1,3,6,1,4,1,3181,10,3,12,100,1))
pacStatusTableEntry.setIndexNames((0,_J,_s))
if mibBuilder.loadTexts:pacStatusTableEntry.setStatus(_A)
class _PacStatPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PacStatPortId_Type.__name__=_B
_PacStatPortId_Object=MibTableColumn
pacStatPortId=_PacStatPortId_Object((1,3,6,1,4,1,3181,10,3,12,100,1,1),_PacStatPortId_Type())
pacStatPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatPortId.setStatus(_A)
class _PacStatPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,254,255)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3),('ieee8021XAuthentication',4),(_w,5),(_x,6),(_K,254),(_D,255)))
_PacStatPortMode_Type.__name__=_B
_PacStatPortMode_Object=MibTableColumn
pacStatPortMode=_PacStatPortMode_Object((1,3,6,1,4,1,3181,10,3,12,100,1,2),_PacStatPortMode_Type())
pacStatPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatPortMode.setStatus(_A)
class _PacStatPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2),(_K,254),(_D,255)))
_PacStatPortStatus_Type.__name__=_B
_PacStatPortStatus_Object=MibTableColumn
pacStatPortStatus=_PacStatPortStatus_Object((1,3,6,1,4,1,3181,10,3,12,100,1,3),_PacStatPortStatus_Type())
pacStatPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatPortStatus.setStatus(_A)
class _PacStatUserStatus1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,20,21,22,254,255)));namedValues=NamedValues(*((_R,10),(_S,11),(_T,12),(_U,20),(_V,21),(_W,22),(_K,254),(_D,255)))
_PacStatUserStatus1_Type.__name__=_B
_PacStatUserStatus1_Object=MibTableColumn
pacStatUserStatus1=_PacStatUserStatus1_Object((1,3,6,1,4,1,3181,10,3,12,100,1,4),_PacStatUserStatus1_Type())
pacStatUserStatus1.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserStatus1.setStatus(_A)
class _PacStatUserStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,20,21,22,254,255)));namedValues=NamedValues(*((_R,10),(_S,11),(_T,12),(_U,20),(_V,21),(_W,22),(_K,254),(_D,255)))
_PacStatUserStatus2_Type.__name__=_B
_PacStatUserStatus2_Object=MibTableColumn
pacStatUserStatus2=_PacStatUserStatus2_Object((1,3,6,1,4,1,3181,10,3,12,100,1,5),_PacStatUserStatus2_Type())
pacStatUserStatus2.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserStatus2.setStatus(_A)
class _PacStatUserStatus3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,20,21,22,254,255)));namedValues=NamedValues(*((_R,10),(_S,11),(_T,12),(_U,20),(_V,21),(_W,22),(_K,254),(_D,255)))
_PacStatUserStatus3_Type.__name__=_B
_PacStatUserStatus3_Object=MibTableColumn
pacStatUserStatus3=_PacStatUserStatus3_Object((1,3,6,1,4,1,3181,10,3,12,100,1,6),_PacStatUserStatus3_Type())
pacStatUserStatus3.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserStatus3.setStatus(_A)
class _PacStatUserStatus4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,20,21,22,254,255)));namedValues=NamedValues(*((_R,10),(_S,11),(_T,12),(_U,20),(_V,21),(_W,22),(_K,254),(_D,255)))
_PacStatUserStatus4_Type.__name__=_B
_PacStatUserStatus4_Object=MibTableColumn
pacStatUserStatus4=_PacStatUserStatus4_Object((1,3,6,1,4,1,3181,10,3,12,100,1,7),_PacStatUserStatus4_Type())
pacStatUserStatus4.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserStatus4.setStatus(_A)
_PacStatUserMac1_Type=PhysAddress
_PacStatUserMac1_Object=MibTableColumn
pacStatUserMac1=_PacStatUserMac1_Object((1,3,6,1,4,1,3181,10,3,12,100,1,8),_PacStatUserMac1_Type())
pacStatUserMac1.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserMac1.setStatus(_A)
_PacStatUserMac2_Type=PhysAddress
_PacStatUserMac2_Object=MibTableColumn
pacStatUserMac2=_PacStatUserMac2_Object((1,3,6,1,4,1,3181,10,3,12,100,1,9),_PacStatUserMac2_Type())
pacStatUserMac2.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserMac2.setStatus(_A)
_PacStatUserMac3_Type=PhysAddress
_PacStatUserMac3_Object=MibTableColumn
pacStatUserMac3=_PacStatUserMac3_Object((1,3,6,1,4,1,3181,10,3,12,100,1,10),_PacStatUserMac3_Type())
pacStatUserMac3.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserMac3.setStatus(_A)
_PacStatUserMac4_Type=PhysAddress
_PacStatUserMac4_Object=MibTableColumn
pacStatUserMac4=_PacStatUserMac4_Object((1,3,6,1,4,1,3181,10,3,12,100,1,11),_PacStatUserMac4_Type())
pacStatUserMac4.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserMac4.setStatus(_A)
class _PacStatUserName1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PacStatUserName1_Type.__name__=_L
_PacStatUserName1_Object=MibTableColumn
pacStatUserName1=_PacStatUserName1_Object((1,3,6,1,4,1,3181,10,3,12,100,1,12),_PacStatUserName1_Type())
pacStatUserName1.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserName1.setStatus(_A)
class _PacStatUserName2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PacStatUserName2_Type.__name__=_L
_PacStatUserName2_Object=MibTableColumn
pacStatUserName2=_PacStatUserName2_Object((1,3,6,1,4,1,3181,10,3,12,100,1,13),_PacStatUserName2_Type())
pacStatUserName2.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserName2.setStatus(_A)
class _PacStatUserName3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PacStatUserName3_Type.__name__=_L
_PacStatUserName3_Object=MibTableColumn
pacStatUserName3=_PacStatUserName3_Object((1,3,6,1,4,1,3181,10,3,12,100,1,14),_PacStatUserName3_Type())
pacStatUserName3.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserName3.setStatus(_A)
class _PacStatUserName4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PacStatUserName4_Type.__name__=_L
_PacStatUserName4_Object=MibTableColumn
pacStatUserName4=_PacStatUserName4_Object((1,3,6,1,4,1,3181,10,3,12,100,1,15),_PacStatUserName4_Type())
pacStatUserName4.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserName4.setStatus(_A)
_PacStatUserIp1_Type=IpAddress
_PacStatUserIp1_Object=MibTableColumn
pacStatUserIp1=_PacStatUserIp1_Object((1,3,6,1,4,1,3181,10,3,12,100,1,16),_PacStatUserIp1_Type())
pacStatUserIp1.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserIp1.setStatus(_A)
_PacStatUserIp2_Type=IpAddress
_PacStatUserIp2_Object=MibTableColumn
pacStatUserIp2=_PacStatUserIp2_Object((1,3,6,1,4,1,3181,10,3,12,100,1,17),_PacStatUserIp2_Type())
pacStatUserIp2.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserIp2.setStatus(_A)
_PacStatUserIp3_Type=IpAddress
_PacStatUserIp3_Object=MibTableColumn
pacStatUserIp3=_PacStatUserIp3_Object((1,3,6,1,4,1,3181,10,3,12,100,1,18),_PacStatUserIp3_Type())
pacStatUserIp3.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserIp3.setStatus(_A)
_PacStatUserIp4_Type=IpAddress
_PacStatUserIp4_Object=MibTableColumn
pacStatUserIp4=_PacStatUserIp4_Object((1,3,6,1,4,1,3181,10,3,12,100,1,19),_PacStatUserIp4_Type())
pacStatUserIp4.setMaxAccess(_E)
if mibBuilder.loadTexts:pacStatUserIp4.setStatus(_A)
_PacConfigTable_Object=MibTable
pacConfigTable=_PacConfigTable_Object((1,3,6,1,4,1,3181,10,3,12,110))
if mibBuilder.loadTexts:pacConfigTable.setStatus(_A)
_PacConfigTableEntry_Object=MibTableRow
pacConfigTableEntry=_PacConfigTableEntry_Object((1,3,6,1,4,1,3181,10,3,12,110,1))
pacConfigTableEntry.setIndexNames((0,_J,_y))
if mibBuilder.loadTexts:pacConfigTableEntry.setStatus(_A)
class _PacConfPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PacConfPortId_Type.__name__=_B
_PacConfPortId_Object=MibTableColumn
pacConfPortId=_PacConfPortId_Object((1,3,6,1,4,1,3181,10,3,12,110,1,1),_PacConfPortId_Type())
pacConfPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:pacConfPortId.setStatus(_A)
class _PacConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,254,255)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3),('ieee8021xAuthentication',4),(_w,5),(_x,6),(_K,254),(_D,255)))
_PacConfMode_Type.__name__=_B
_PacConfMode_Object=MibTableColumn
pacConfMode=_PacConfMode_Object((1,3,6,1,4,1,3181,10,3,12,110,1,2),_PacConfMode_Type())
pacConfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pacConfMode.setStatus(_A)
class _PacConfMaxMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_PacConfMaxMacCount_Type.__name__=_B
_PacConfMaxMacCount_Object=MibTableColumn
pacConfMaxMacCount=_PacConfMaxMacCount_Object((1,3,6,1,4,1,3181,10,3,12,110,1,3),_PacConfMaxMacCount_Type())
pacConfMaxMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pacConfMaxMacCount.setStatus(_A)
_PacMacLockingTable_Object=MibTable
pacMacLockingTable=_PacMacLockingTable_Object((1,3,6,1,4,1,3181,10,3,12,120))
if mibBuilder.loadTexts:pacMacLockingTable.setStatus(_A)
_PacMacLockTableEntry_Object=MibTableRow
pacMacLockTableEntry=_PacMacLockTableEntry_Object((1,3,6,1,4,1,3181,10,3,12,120,1))
pacMacLockTableEntry.setIndexNames((0,_J,_z))
if mibBuilder.loadTexts:pacMacLockTableEntry.setStatus(_A)
class _PacMacLockPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PacMacLockPortId_Type.__name__=_B
_PacMacLockPortId_Object=MibTableColumn
pacMacLockPortId=_PacMacLockPortId_Object((1,3,6,1,4,1,3181,10,3,12,120,1,1),_PacMacLockPortId_Type())
pacMacLockPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:pacMacLockPortId.setStatus(_A)
class _PacMacLockEnable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacMacLockEnable1_Type.__name__=_B
_PacMacLockEnable1_Object=MibTableColumn
pacMacLockEnable1=_PacMacLockEnable1_Object((1,3,6,1,4,1,3181,10,3,12,120,1,2),_PacMacLockEnable1_Type())
pacMacLockEnable1.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockEnable1.setStatus(_A)
class _PacMacLockEnable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacMacLockEnable2_Type.__name__=_B
_PacMacLockEnable2_Object=MibTableColumn
pacMacLockEnable2=_PacMacLockEnable2_Object((1,3,6,1,4,1,3181,10,3,12,120,1,3),_PacMacLockEnable2_Type())
pacMacLockEnable2.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockEnable2.setStatus(_A)
class _PacMacLockEnable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacMacLockEnable3_Type.__name__=_B
_PacMacLockEnable3_Object=MibTableColumn
pacMacLockEnable3=_PacMacLockEnable3_Object((1,3,6,1,4,1,3181,10,3,12,120,1,4),_PacMacLockEnable3_Type())
pacMacLockEnable3.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockEnable3.setStatus(_A)
class _PacMacLockEnable4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PacMacLockEnable4_Type.__name__=_B
_PacMacLockEnable4_Object=MibTableColumn
pacMacLockEnable4=_PacMacLockEnable4_Object((1,3,6,1,4,1,3181,10,3,12,120,1,5),_PacMacLockEnable4_Type())
pacMacLockEnable4.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockEnable4.setStatus(_A)
class _PacMacLockLearn1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_X,1),(_P,2),(_D,255)))
_PacMacLockLearn1_Type.__name__=_B
_PacMacLockLearn1_Object=MibTableColumn
pacMacLockLearn1=_PacMacLockLearn1_Object((1,3,6,1,4,1,3181,10,3,12,120,1,6),_PacMacLockLearn1_Type())
pacMacLockLearn1.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockLearn1.setStatus(_A)
class _PacMacLockLearn2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_X,1),(_P,2),(_D,255)))
_PacMacLockLearn2_Type.__name__=_B
_PacMacLockLearn2_Object=MibTableColumn
pacMacLockLearn2=_PacMacLockLearn2_Object((1,3,6,1,4,1,3181,10,3,12,120,1,7),_PacMacLockLearn2_Type())
pacMacLockLearn2.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockLearn2.setStatus(_A)
class _PacMacLockLearn3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_X,1),(_P,2),(_D,255)))
_PacMacLockLearn3_Type.__name__=_B
_PacMacLockLearn3_Object=MibTableColumn
pacMacLockLearn3=_PacMacLockLearn3_Object((1,3,6,1,4,1,3181,10,3,12,120,1,8),_PacMacLockLearn3_Type())
pacMacLockLearn3.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockLearn3.setStatus(_A)
class _PacMacLockLearn4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_X,1),(_P,2),(_D,255)))
_PacMacLockLearn4_Type.__name__=_B
_PacMacLockLearn4_Object=MibTableColumn
pacMacLockLearn4=_PacMacLockLearn4_Object((1,3,6,1,4,1,3181,10,3,12,120,1,9),_PacMacLockLearn4_Type())
pacMacLockLearn4.setMaxAccess(_C)
if mibBuilder.loadTexts:pacMacLockLearn4.setStatus(_A)
_PacLockedMac1_Type=PhysAddress
_PacLockedMac1_Object=MibTableColumn
pacLockedMac1=_PacLockedMac1_Object((1,3,6,1,4,1,3181,10,3,12,120,1,10),_PacLockedMac1_Type())
pacLockedMac1.setMaxAccess(_C)
if mibBuilder.loadTexts:pacLockedMac1.setStatus(_A)
_PacLockedMac2_Type=PhysAddress
_PacLockedMac2_Object=MibTableColumn
pacLockedMac2=_PacLockedMac2_Object((1,3,6,1,4,1,3181,10,3,12,120,1,11),_PacLockedMac2_Type())
pacLockedMac2.setMaxAccess(_C)
if mibBuilder.loadTexts:pacLockedMac2.setStatus(_A)
_PacLockedMac3_Type=PhysAddress
_PacLockedMac3_Object=MibTableColumn
pacLockedMac3=_PacLockedMac3_Object((1,3,6,1,4,1,3181,10,3,12,120,1,12),_PacLockedMac3_Type())
pacLockedMac3.setMaxAccess(_C)
if mibBuilder.loadTexts:pacLockedMac3.setStatus(_A)
_PacLockedMac4_Type=PhysAddress
_PacLockedMac4_Object=MibTableColumn
pacLockedMac4=_PacLockedMac4_Object((1,3,6,1,4,1,3181,10,3,12,120,1,13),_PacLockedMac4_Type())
pacLockedMac4.setMaxAccess(_C)
if mibBuilder.loadTexts:pacLockedMac4.setStatus(_A)
_Igmps_ObjectIdentity=ObjectIdentity
igmps=_Igmps_ObjectIdentity((1,3,6,1,4,1,3181,10,3,13))
class _IgmpsSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_IgmpsSupport_Type.__name__=_B
_IgmpsSupport_Object=MibScalar
igmpsSupport=_IgmpsSupport_Object((1,3,6,1,4,1,3181,10,3,13,1),_IgmpsSupport_Type())
igmpsSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsSupport.setStatus(_A)
class _IgmpsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_IgmpsEnable_Type.__name__=_B
_IgmpsEnable_Object=MibScalar
igmpsEnable=_IgmpsEnable_Object((1,3,6,1,4,1,3181,10,3,13,2),_IgmpsEnable_Type())
igmpsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsEnable.setStatus(_A)
class _IgmpsFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_IgmpsFastLeave_Type.__name__=_B
_IgmpsFastLeave_Object=MibScalar
igmpsFastLeave=_IgmpsFastLeave_Object((1,3,6,1,4,1,3181,10,3,13,3),_IgmpsFastLeave_Type())
igmpsFastLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsFastLeave.setStatus(_A)
class _IgmpsReportAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_IgmpsReportAggregation_Type.__name__=_B
_IgmpsReportAggregation_Object=MibScalar
igmpsReportAggregation=_IgmpsReportAggregation_Object((1,3,6,1,4,1,3181,10,3,13,4),_IgmpsReportAggregation_Type())
igmpsReportAggregation.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsReportAggregation.setStatus(_A)
class _IgmpsFloodingUnregPack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_IgmpsFloodingUnregPack_Type.__name__=_B
_IgmpsFloodingUnregPack_Object=MibScalar
igmpsFloodingUnregPack=_IgmpsFloodingUnregPack_Object((1,3,6,1,4,1,3181,10,3,13,5),_IgmpsFloodingUnregPack_Type())
igmpsFloodingUnregPack.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsFloodingUnregPack.setStatus(_A)
_IgmpsMaxGroupLimit_Type=Integer32
_IgmpsMaxGroupLimit_Object=MibScalar
igmpsMaxGroupLimit=_IgmpsMaxGroupLimit_Object((1,3,6,1,4,1,3181,10,3,13,6),_IgmpsMaxGroupLimit_Type())
igmpsMaxGroupLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsMaxGroupLimit.setStatus(_A)
_IgmpsGroupLimit_Type=Integer32
_IgmpsGroupLimit_Object=MibScalar
igmpsGroupLimit=_IgmpsGroupLimit_Object((1,3,6,1,4,1,3181,10,3,13,7),_IgmpsGroupLimit_Type())
igmpsGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsGroupLimit.setStatus(_A)
_IgmpsGroupNumber_Type=Integer32
_IgmpsGroupNumber_Object=MibScalar
igmpsGroupNumber=_IgmpsGroupNumber_Object((1,3,6,1,4,1,3181,10,3,13,8),_IgmpsGroupNumber_Type())
igmpsGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupNumber.setStatus(_A)
class _IgmpsRouterDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('discovery',1),('query',2),(_D,255)))
_IgmpsRouterDetection_Type.__name__=_B
_IgmpsRouterDetection_Object=MibScalar
igmpsRouterDetection=_IgmpsRouterDetection_Object((1,3,6,1,4,1,3181,10,3,13,9),_IgmpsRouterDetection_Type())
igmpsRouterDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsRouterDetection.setStatus(_A)
class _IgmpsGroupMembershipInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_IgmpsGroupMembershipInterval_Type.__name__=_B
_IgmpsGroupMembershipInterval_Object=MibScalar
igmpsGroupMembershipInterval=_IgmpsGroupMembershipInterval_Object((1,3,6,1,4,1,3181,10,3,13,10),_IgmpsGroupMembershipInterval_Type())
igmpsGroupMembershipInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsGroupMembershipInterval.setStatus(_A)
class _IgmpsMaximumResposeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_IgmpsMaximumResposeTime_Type.__name__=_B
_IgmpsMaximumResposeTime_Object=MibScalar
igmpsMaximumResposeTime=_IgmpsMaximumResposeTime_Object((1,3,6,1,4,1,3181,10,3,13,11),_IgmpsMaximumResposeTime_Type())
igmpsMaximumResposeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsMaximumResposeTime.setStatus(_A)
class _IgmpsLastMemeberQueryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,175))
_IgmpsLastMemeberQueryTime_Type.__name__=_B
_IgmpsLastMemeberQueryTime_Object=MibScalar
igmpsLastMemeberQueryTime=_IgmpsLastMemeberQueryTime_Object((1,3,6,1,4,1,3181,10,3,13,12),_IgmpsLastMemeberQueryTime_Type())
igmpsLastMemeberQueryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsLastMemeberQueryTime.setStatus(_A)
class _IgmpsNeighborDeadInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,554))
_IgmpsNeighborDeadInterval_Type.__name__=_B
_IgmpsNeighborDeadInterval_Object=MibScalar
igmpsNeighborDeadInterval=_IgmpsNeighborDeadInterval_Object((1,3,6,1,4,1,3181,10,3,13,13),_IgmpsNeighborDeadInterval_Type())
igmpsNeighborDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsNeighborDeadInterval.setStatus(_A)
class _IgmpsRouterAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_IgmpsRouterAgingTime_Type.__name__=_B
_IgmpsRouterAgingTime_Object=MibScalar
igmpsRouterAgingTime=_IgmpsRouterAgingTime_Object((1,3,6,1,4,1,3181,10,3,13,14),_IgmpsRouterAgingTime_Type())
igmpsRouterAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsRouterAgingTime.setStatus(_A)
_IgmpsRxMessageGeneralQuery_Type=Integer32
_IgmpsRxMessageGeneralQuery_Object=MibScalar
igmpsRxMessageGeneralQuery=_IgmpsRxMessageGeneralQuery_Object((1,3,6,1,4,1,3181,10,3,13,15),_IgmpsRxMessageGeneralQuery_Type())
igmpsRxMessageGeneralQuery.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsRxMessageGeneralQuery.setStatus(_A)
_IgmpsRxMessageSpecificQuery_Type=Integer32
_IgmpsRxMessageSpecificQuery_Object=MibScalar
igmpsRxMessageSpecificQuery=_IgmpsRxMessageSpecificQuery_Object((1,3,6,1,4,1,3181,10,3,13,16),_IgmpsRxMessageSpecificQuery_Type())
igmpsRxMessageSpecificQuery.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsRxMessageSpecificQuery.setStatus(_A)
_IgmpsRxMessageReport_Type=Integer32
_IgmpsRxMessageReport_Object=MibScalar
igmpsRxMessageReport=_IgmpsRxMessageReport_Object((1,3,6,1,4,1,3181,10,3,13,17),_IgmpsRxMessageReport_Type())
igmpsRxMessageReport.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsRxMessageReport.setStatus(_A)
_IgmpsRxMessageLeave_Type=Integer32
_IgmpsRxMessageLeave_Object=MibScalar
igmpsRxMessageLeave=_IgmpsRxMessageLeave_Object((1,3,6,1,4,1,3181,10,3,13,18),_IgmpsRxMessageLeave_Type())
igmpsRxMessageLeave.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsRxMessageLeave.setStatus(_A)
_IgmpsRxMessageAdvertisement_Type=Integer32
_IgmpsRxMessageAdvertisement_Object=MibScalar
igmpsRxMessageAdvertisement=_IgmpsRxMessageAdvertisement_Object((1,3,6,1,4,1,3181,10,3,13,19),_IgmpsRxMessageAdvertisement_Type())
igmpsRxMessageAdvertisement.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsRxMessageAdvertisement.setStatus(_A)
_IgmpsRxMessageTermination_Type=Integer32
_IgmpsRxMessageTermination_Object=MibScalar
igmpsRxMessageTermination=_IgmpsRxMessageTermination_Object((1,3,6,1,4,1,3181,10,3,13,20),_IgmpsRxMessageTermination_Type())
igmpsRxMessageTermination.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsRxMessageTermination.setStatus(_A)
_IgmpsTxMessageSolicitation_Type=Integer32
_IgmpsTxMessageSolicitation_Object=MibScalar
igmpsTxMessageSolicitation=_IgmpsTxMessageSolicitation_Object((1,3,6,1,4,1,3181,10,3,13,21),_IgmpsTxMessageSolicitation_Type())
igmpsTxMessageSolicitation.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsTxMessageSolicitation.setStatus(_A)
class _IgmpsCounterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_Z,1),(_D,255)))
_IgmpsCounterReset_Type.__name__=_B
_IgmpsCounterReset_Object=MibScalar
igmpsCounterReset=_IgmpsCounterReset_Object((1,3,6,1,4,1,3181,10,3,13,22),_IgmpsCounterReset_Type())
igmpsCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsCounterReset.setStatus(_A)
_IgmpsPortTable_Object=MibTable
igmpsPortTable=_IgmpsPortTable_Object((1,3,6,1,4,1,3181,10,3,13,30))
if mibBuilder.loadTexts:igmpsPortTable.setStatus(_A)
_IgmpsPortTableEntry_Object=MibTableRow
igmpsPortTableEntry=_IgmpsPortTableEntry_Object((1,3,6,1,4,1,3181,10,3,13,30,1))
igmpsPortTableEntry.setIndexNames((0,_J,_A0))
if mibBuilder.loadTexts:igmpsPortTableEntry.setStatus(_A)
class _IgmpsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IgmpsPortId_Type.__name__=_B
_IgmpsPortId_Object=MibTableColumn
igmpsPortId=_IgmpsPortId_Object((1,3,6,1,4,1,3181,10,3,13,30,1,1),_IgmpsPortId_Type())
igmpsPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsPortId.setStatus(_A)
class _IgmpsPortSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_IgmpsPortSnooping_Type.__name__=_B
_IgmpsPortSnooping_Object=MibTableColumn
igmpsPortSnooping=_IgmpsPortSnooping_Object((1,3,6,1,4,1,3181,10,3,13,30,1,2),_IgmpsPortSnooping_Type())
igmpsPortSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsPortSnooping.setStatus(_A)
class _IgmpsPortStaticRouter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_IgmpsPortStaticRouter_Type.__name__=_B
_IgmpsPortStaticRouter_Object=MibTableColumn
igmpsPortStaticRouter=_IgmpsPortStaticRouter_Object((1,3,6,1,4,1,3181,10,3,13,30,1,3),_IgmpsPortStaticRouter_Type())
igmpsPortStaticRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpsPortStaticRouter.setStatus(_A)
class _IgmpsPortDynamicRouter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_d,1),(_e,2),(_D,255)))
_IgmpsPortDynamicRouter_Type.__name__=_B
_IgmpsPortDynamicRouter_Object=MibTableColumn
igmpsPortDynamicRouter=_IgmpsPortDynamicRouter_Object((1,3,6,1,4,1,3181,10,3,13,30,1,4),_IgmpsPortDynamicRouter_Type())
igmpsPortDynamicRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsPortDynamicRouter.setStatus(_A)
_IgmpsGroupTable_Object=MibTable
igmpsGroupTable=_IgmpsGroupTable_Object((1,3,6,1,4,1,3181,10,3,13,40))
if mibBuilder.loadTexts:igmpsGroupTable.setStatus(_A)
_IgmpsGroupTableEntry_Object=MibTableRow
igmpsGroupTableEntry=_IgmpsGroupTableEntry_Object((1,3,6,1,4,1,3181,10,3,13,40,1))
igmpsGroupTableEntry.setIndexNames((0,_J,_A1))
if mibBuilder.loadTexts:igmpsGroupTableEntry.setStatus(_A)
_IgmpsGroupId_Type=Unsigned32
_IgmpsGroupId_Object=MibTableColumn
igmpsGroupId=_IgmpsGroupId_Object((1,3,6,1,4,1,3181,10,3,13,40,1,1),_IgmpsGroupId_Type())
igmpsGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupId.setStatus(_A)
_IgmpsGroupMac_Type=PhysAddress
_IgmpsGroupMac_Object=MibTableColumn
igmpsGroupMac=_IgmpsGroupMac_Object((1,3,6,1,4,1,3181,10,3,13,40,1,2),_IgmpsGroupMac_Type())
igmpsGroupMac.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMac.setStatus(_A)
_IgmpsGroupVlanId_Type=Integer32
_IgmpsGroupVlanId_Object=MibTableColumn
igmpsGroupVlanId=_IgmpsGroupVlanId_Object((1,3,6,1,4,1,3181,10,3,13,40,1,3),_IgmpsGroupVlanId_Type())
igmpsGroupVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupVlanId.setStatus(_A)
_IgmpsGroupTimestamp_Type=Integer32
_IgmpsGroupTimestamp_Object=MibTableColumn
igmpsGroupTimestamp=_IgmpsGroupTimestamp_Object((1,3,6,1,4,1,3181,10,3,13,40,1,4),_IgmpsGroupTimestamp_Type())
igmpsGroupTimestamp.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupTimestamp.setStatus(_A)
class _IgmpsGroupLeaveFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('set',1),('unset',2),(_D,255)))
_IgmpsGroupLeaveFlag_Type.__name__=_B
_IgmpsGroupLeaveFlag_Object=MibTableColumn
igmpsGroupLeaveFlag=_IgmpsGroupLeaveFlag_Object((1,3,6,1,4,1,3181,10,3,13,40,1,5),_IgmpsGroupLeaveFlag_Type())
igmpsGroupLeaveFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupLeaveFlag.setStatus(_A)
class _IgmpsGroupMemberPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort1_Type.__name__=_B
_IgmpsGroupMemberPort1_Object=MibTableColumn
igmpsGroupMemberPort1=_IgmpsGroupMemberPort1_Object((1,3,6,1,4,1,3181,10,3,13,40,1,6),_IgmpsGroupMemberPort1_Type())
igmpsGroupMemberPort1.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort1.setStatus(_A)
class _IgmpsGroupMemberPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort2_Type.__name__=_B
_IgmpsGroupMemberPort2_Object=MibTableColumn
igmpsGroupMemberPort2=_IgmpsGroupMemberPort2_Object((1,3,6,1,4,1,3181,10,3,13,40,1,7),_IgmpsGroupMemberPort2_Type())
igmpsGroupMemberPort2.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort2.setStatus(_A)
class _IgmpsGroupMemberPort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort3_Type.__name__=_B
_IgmpsGroupMemberPort3_Object=MibTableColumn
igmpsGroupMemberPort3=_IgmpsGroupMemberPort3_Object((1,3,6,1,4,1,3181,10,3,13,40,1,8),_IgmpsGroupMemberPort3_Type())
igmpsGroupMemberPort3.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort3.setStatus(_A)
class _IgmpsGroupMemberPort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort4_Type.__name__=_B
_IgmpsGroupMemberPort4_Object=MibTableColumn
igmpsGroupMemberPort4=_IgmpsGroupMemberPort4_Object((1,3,6,1,4,1,3181,10,3,13,40,1,9),_IgmpsGroupMemberPort4_Type())
igmpsGroupMemberPort4.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort4.setStatus(_A)
class _IgmpsGroupMemberPort5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort5_Type.__name__=_B
_IgmpsGroupMemberPort5_Object=MibTableColumn
igmpsGroupMemberPort5=_IgmpsGroupMemberPort5_Object((1,3,6,1,4,1,3181,10,3,13,40,1,10),_IgmpsGroupMemberPort5_Type())
igmpsGroupMemberPort5.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort5.setStatus(_A)
class _IgmpsGroupMemberPort6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort6_Type.__name__=_B
_IgmpsGroupMemberPort6_Object=MibTableColumn
igmpsGroupMemberPort6=_IgmpsGroupMemberPort6_Object((1,3,6,1,4,1,3181,10,3,13,40,1,11),_IgmpsGroupMemberPort6_Type())
igmpsGroupMemberPort6.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort6.setStatus(_A)
class _IgmpsGroupMemberPort7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort7_Type.__name__=_B
_IgmpsGroupMemberPort7_Object=MibTableColumn
igmpsGroupMemberPort7=_IgmpsGroupMemberPort7_Object((1,3,6,1,4,1,3181,10,3,13,40,1,12),_IgmpsGroupMemberPort7_Type())
igmpsGroupMemberPort7.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort7.setStatus(_A)
class _IgmpsGroupMemberPort8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort8_Type.__name__=_B
_IgmpsGroupMemberPort8_Object=MibTableColumn
igmpsGroupMemberPort8=_IgmpsGroupMemberPort8_Object((1,3,6,1,4,1,3181,10,3,13,40,1,13),_IgmpsGroupMemberPort8_Type())
igmpsGroupMemberPort8.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort8.setStatus(_A)
class _IgmpsGroupMemberPort9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort9_Type.__name__=_B
_IgmpsGroupMemberPort9_Object=MibTableColumn
igmpsGroupMemberPort9=_IgmpsGroupMemberPort9_Object((1,3,6,1,4,1,3181,10,3,13,40,1,14),_IgmpsGroupMemberPort9_Type())
igmpsGroupMemberPort9.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort9.setStatus(_A)
class _IgmpsGroupMemberPort10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort10_Type.__name__=_B
_IgmpsGroupMemberPort10_Object=MibTableColumn
igmpsGroupMemberPort10=_IgmpsGroupMemberPort10_Object((1,3,6,1,4,1,3181,10,3,13,40,1,15),_IgmpsGroupMemberPort10_Type())
igmpsGroupMemberPort10.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort10.setStatus(_A)
class _IgmpsGroupMemberPort11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort11_Type.__name__=_B
_IgmpsGroupMemberPort11_Object=MibTableColumn
igmpsGroupMemberPort11=_IgmpsGroupMemberPort11_Object((1,3,6,1,4,1,3181,10,3,13,40,1,16),_IgmpsGroupMemberPort11_Type())
igmpsGroupMemberPort11.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort11.setStatus(_A)
class _IgmpsGroupMemberPort12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort12_Type.__name__=_B
_IgmpsGroupMemberPort12_Object=MibTableColumn
igmpsGroupMemberPort12=_IgmpsGroupMemberPort12_Object((1,3,6,1,4,1,3181,10,3,13,40,1,17),_IgmpsGroupMemberPort12_Type())
igmpsGroupMemberPort12.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort12.setStatus(_A)
class _IgmpsGroupMemberPort13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort13_Type.__name__=_B
_IgmpsGroupMemberPort13_Object=MibTableColumn
igmpsGroupMemberPort13=_IgmpsGroupMemberPort13_Object((1,3,6,1,4,1,3181,10,3,13,40,1,18),_IgmpsGroupMemberPort13_Type())
igmpsGroupMemberPort13.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort13.setStatus(_A)
class _IgmpsGroupMemberPort14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort14_Type.__name__=_B
_IgmpsGroupMemberPort14_Object=MibTableColumn
igmpsGroupMemberPort14=_IgmpsGroupMemberPort14_Object((1,3,6,1,4,1,3181,10,3,13,40,1,19),_IgmpsGroupMemberPort14_Type())
igmpsGroupMemberPort14.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort14.setStatus(_A)
class _IgmpsGroupMemberPort15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort15_Type.__name__=_B
_IgmpsGroupMemberPort15_Object=MibTableColumn
igmpsGroupMemberPort15=_IgmpsGroupMemberPort15_Object((1,3,6,1,4,1,3181,10,3,13,40,1,20),_IgmpsGroupMemberPort15_Type())
igmpsGroupMemberPort15.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort15.setStatus(_A)
class _IgmpsGroupMemberPort16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort16_Type.__name__=_B
_IgmpsGroupMemberPort16_Object=MibTableColumn
igmpsGroupMemberPort16=_IgmpsGroupMemberPort16_Object((1,3,6,1,4,1,3181,10,3,13,40,1,21),_IgmpsGroupMemberPort16_Type())
igmpsGroupMemberPort16.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort16.setStatus(_A)
class _IgmpsGroupMemberPort17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort17_Type.__name__=_B
_IgmpsGroupMemberPort17_Object=MibTableColumn
igmpsGroupMemberPort17=_IgmpsGroupMemberPort17_Object((1,3,6,1,4,1,3181,10,3,13,40,1,22),_IgmpsGroupMemberPort17_Type())
igmpsGroupMemberPort17.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort17.setStatus(_A)
class _IgmpsGroupMemberPort18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort18_Type.__name__=_B
_IgmpsGroupMemberPort18_Object=MibTableColumn
igmpsGroupMemberPort18=_IgmpsGroupMemberPort18_Object((1,3,6,1,4,1,3181,10,3,13,40,1,23),_IgmpsGroupMemberPort18_Type())
igmpsGroupMemberPort18.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort18.setStatus(_A)
class _IgmpsGroupMemberPort19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort19_Type.__name__=_B
_IgmpsGroupMemberPort19_Object=MibTableColumn
igmpsGroupMemberPort19=_IgmpsGroupMemberPort19_Object((1,3,6,1,4,1,3181,10,3,13,40,1,24),_IgmpsGroupMemberPort19_Type())
igmpsGroupMemberPort19.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort19.setStatus(_A)
class _IgmpsGroupMemberPort20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort20_Type.__name__=_B
_IgmpsGroupMemberPort20_Object=MibTableColumn
igmpsGroupMemberPort20=_IgmpsGroupMemberPort20_Object((1,3,6,1,4,1,3181,10,3,13,40,1,25),_IgmpsGroupMemberPort20_Type())
igmpsGroupMemberPort20.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort20.setStatus(_A)
class _IgmpsGroupMemberPort21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort21_Type.__name__=_B
_IgmpsGroupMemberPort21_Object=MibTableColumn
igmpsGroupMemberPort21=_IgmpsGroupMemberPort21_Object((1,3,6,1,4,1,3181,10,3,13,40,1,26),_IgmpsGroupMemberPort21_Type())
igmpsGroupMemberPort21.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort21.setStatus(_A)
class _IgmpsGroupMemberPort22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort22_Type.__name__=_B
_IgmpsGroupMemberPort22_Object=MibTableColumn
igmpsGroupMemberPort22=_IgmpsGroupMemberPort22_Object((1,3,6,1,4,1,3181,10,3,13,40,1,27),_IgmpsGroupMemberPort22_Type())
igmpsGroupMemberPort22.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort22.setStatus(_A)
class _IgmpsGroupMemberPort23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort23_Type.__name__=_B
_IgmpsGroupMemberPort23_Object=MibTableColumn
igmpsGroupMemberPort23=_IgmpsGroupMemberPort23_Object((1,3,6,1,4,1,3181,10,3,13,40,1,28),_IgmpsGroupMemberPort23_Type())
igmpsGroupMemberPort23.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort23.setStatus(_A)
class _IgmpsGroupMemberPort24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_I,2),(_D,255)))
_IgmpsGroupMemberPort24_Type.__name__=_B
_IgmpsGroupMemberPort24_Object=MibTableColumn
igmpsGroupMemberPort24=_IgmpsGroupMemberPort24_Object((1,3,6,1,4,1,3181,10,3,13,40,1,29),_IgmpsGroupMemberPort24_Type())
igmpsGroupMemberPort24.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpsGroupMemberPort24.setStatus(_A)
_Rtc_ObjectIdentity=ObjectIdentity
rtc=_Rtc_ObjectIdentity((1,3,6,1,4,1,3181,10,3,15))
class _RtcSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_RtcSupport_Type.__name__=_B
_RtcSupport_Object=MibScalar
rtcSupport=_RtcSupport_Object((1,3,6,1,4,1,3181,10,3,15,1),_RtcSupport_Type())
rtcSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcSupport.setStatus(_A)
class _RtcFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('sntpenabled',1),('dstenabled',2),(_D,255)))
_RtcFlags_Type.__name__=_B
_RtcFlags_Object=MibScalar
rtcFlags=_RtcFlags_Object((1,3,6,1,4,1,3181,10,3,15,2),_RtcFlags_Type())
rtcFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcFlags.setStatus(_A)
class _RtcLocalTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,25));fixedLength=25
_RtcLocalTime_Type.__name__=_L
_RtcLocalTime_Object=MibScalar
rtcLocalTime=_RtcLocalTime_Object((1,3,6,1,4,1,3181,10,3,15,3),_RtcLocalTime_Type())
rtcLocalTime.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcLocalTime.setStatus(_A)
class _RtcManualTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,25));fixedLength=25
_RtcManualTime_Type.__name__=_L
_RtcManualTime_Object=MibScalar
rtcManualTime=_RtcManualTime_Object((1,3,6,1,4,1,3181,10,3,15,4),_RtcManualTime_Type())
rtcManualTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcManualTime.setStatus(_A)
class _RtcTimeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('unset',1),('manuallyset',2),('synchronized',3),('unsynchronized',4),(_D,255)))
_RtcTimeStatus_Type.__name__=_B
_RtcTimeStatus_Object=MibScalar
rtcTimeStatus=_RtcTimeStatus_Object((1,3,6,1,4,1,3181,10,3,15,5),_RtcTimeStatus_Type())
rtcTimeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcTimeStatus.setStatus(_A)
class _RtcTimezoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,24))
_RtcTimezoneOffset_Type.__name__=_B
_RtcTimezoneOffset_Object=MibScalar
rtcTimezoneOffset=_RtcTimezoneOffset_Object((1,3,6,1,4,1,3181,10,3,15,6),_RtcTimezoneOffset_Type())
rtcTimezoneOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcTimezoneOffset.setStatus(_A)
class _RtcDSTOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_RtcDSTOffset_Type.__name__=_B
_RtcDSTOffset_Object=MibScalar
rtcDSTOffset=_RtcDSTOffset_Object((1,3,6,1,4,1,3181,10,3,15,7),_RtcDSTOffset_Type())
rtcDSTOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcDSTOffset.setStatus(_A)
class _RtcDSTbegin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_RtcDSTbegin_Type.__name__=_Y
_RtcDSTbegin_Object=MibScalar
rtcDSTbegin=_RtcDSTbegin_Object((1,3,6,1,4,1,3181,10,3,15,8),_RtcDSTbegin_Type())
rtcDSTbegin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcDSTbegin.setStatus(_A)
class _RtcDSTend_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_RtcDSTend_Type.__name__=_Y
_RtcDSTend_Object=MibScalar
rtcDSTend=_RtcDSTend_Object((1,3,6,1,4,1,3181,10,3,15,9),_RtcDSTend_Type())
rtcDSTend.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcDSTend.setStatus(_A)
class _RtcDSTstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('isdst',1),('isnotdst',2),(_D,255)))
_RtcDSTstatus_Type.__name__=_B
_RtcDSTstatus_Object=MibScalar
rtcDSTstatus=_RtcDSTstatus_Object((1,3,6,1,4,1,3181,10,3,15,10),_RtcDSTstatus_Type())
rtcDSTstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcDSTstatus.setStatus(_A)
_RtcSNTPsyncInterval_Type=Integer32
_RtcSNTPsyncInterval_Object=MibScalar
rtcSNTPsyncInterval=_RtcSNTPsyncInterval_Object((1,3,6,1,4,1,3181,10,3,15,11),_RtcSNTPsyncInterval_Type())
rtcSNTPsyncInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcSNTPsyncInterval.setStatus(_A)
class _RtcSNTPsyncNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),('syncNow',1),(_D,255)))
_RtcSNTPsyncNow_Type.__name__=_B
_RtcSNTPsyncNow_Object=MibScalar
rtcSNTPsyncNow=_RtcSNTPsyncNow_Object((1,3,6,1,4,1,3181,10,3,15,12),_RtcSNTPsyncNow_Type())
rtcSNTPsyncNow.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcSNTPsyncNow.setStatus(_A)
class _RtcSNTPServerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_RtcSNTPServerCount_Type.__name__=_B
_RtcSNTPServerCount_Object=MibScalar
rtcSNTPServerCount=_RtcSNTPServerCount_Object((1,3,6,1,4,1,3181,10,3,15,13),_RtcSNTPServerCount_Type())
rtcSNTPServerCount.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcSNTPServerCount.setStatus(_A)
_RtcSNTPServerTable_Object=MibTable
rtcSNTPServerTable=_RtcSNTPServerTable_Object((1,3,6,1,4,1,3181,10,3,15,20))
if mibBuilder.loadTexts:rtcSNTPServerTable.setStatus(_A)
_RtcSNTPServerTableEntry_Object=MibTableRow
rtcSNTPServerTableEntry=_RtcSNTPServerTableEntry_Object((1,3,6,1,4,1,3181,10,3,15,20,1))
rtcSNTPServerTableEntry.setIndexNames((0,_J,_A2))
if mibBuilder.loadTexts:rtcSNTPServerTableEntry.setStatus(_A)
class _RtcSNTPServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RtcSNTPServerId_Type.__name__=_B
_RtcSNTPServerId_Object=MibTableColumn
rtcSNTPServerId=_RtcSNTPServerId_Object((1,3,6,1,4,1,3181,10,3,15,20,1,1),_RtcSNTPServerId_Type())
rtcSNTPServerId.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcSNTPServerId.setStatus(_A)
class _RtcSNTPServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,7,255)));namedValues=NamedValues(*(('ok',0),('busy',1),('timeout',2),('nomemory',3),('portbusy',4),('alarm',5),('unknown',7),(_D,255)))
_RtcSNTPServerStatus_Type.__name__=_B
_RtcSNTPServerStatus_Object=MibTableColumn
rtcSNTPServerStatus=_RtcSNTPServerStatus_Object((1,3,6,1,4,1,3181,10,3,15,20,1,2),_RtcSNTPServerStatus_Type())
rtcSNTPServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rtcSNTPServerStatus.setStatus(_A)
class _RtcSNTPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_RtcSNTPServerEnable_Type.__name__=_B
_RtcSNTPServerEnable_Object=MibTableColumn
rtcSNTPServerEnable=_RtcSNTPServerEnable_Object((1,3,6,1,4,1,3181,10,3,15,20,1,3),_RtcSNTPServerEnable_Type())
rtcSNTPServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcSNTPServerEnable.setStatus(_A)
_RtcSNTPServerIpv4Address_Type=IpAddress
_RtcSNTPServerIpv4Address_Object=MibTableColumn
rtcSNTPServerIpv4Address=_RtcSNTPServerIpv4Address_Object((1,3,6,1,4,1,3181,10,3,15,20,1,4),_RtcSNTPServerIpv4Address_Type())
rtcSNTPServerIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:rtcSNTPServerIpv4Address.setStatus(_A)
_Consoleinterface_ObjectIdentity=ObjectIdentity
consoleinterface=_Consoleinterface_ObjectIdentity((1,3,6,1,4,1,3181,10,3,20))
class _ConsoleSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ConsoleSupport_Type.__name__=_B
_ConsoleSupport_Object=MibScalar
consoleSupport=_ConsoleSupport_Object((1,3,6,1,4,1,3181,10,3,20,1),_ConsoleSupport_Type())
consoleSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:consoleSupport.setStatus(_A)
class _ConsoleEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ConsoleEnable_Type.__name__=_B
_ConsoleEnable_Object=MibScalar
consoleEnable=_ConsoleEnable_Object((1,3,6,1,4,1,3181,10,3,20,2),_ConsoleEnable_Type())
consoleEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleEnable.setStatus(_A)
_ConsoleTimeout_Type=Integer32
_ConsoleTimeout_Object=MibScalar
consoleTimeout=_ConsoleTimeout_Object((1,3,6,1,4,1,3181,10,3,20,3),_ConsoleTimeout_Type())
consoleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleTimeout.setStatus(_A)
class _ConsoleApplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A3,1),(_A4,2),(_A5,3)))
_ConsoleApplyMode_Type.__name__=_B
_ConsoleApplyMode_Object=MibScalar
consoleApplyMode=_ConsoleApplyMode_Object((1,3,6,1,4,1,3181,10,3,20,4),_ConsoleApplyMode_Type())
consoleApplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleApplyMode.setStatus(_A)
class _ConsolePrompt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ConsolePrompt_Type.__name__=_L
_ConsolePrompt_Object=MibScalar
consolePrompt=_ConsolePrompt_Object((1,3,6,1,4,1,3181,10,3,20,5),_ConsolePrompt_Type())
consolePrompt.setMaxAccess(_C)
if mibBuilder.loadTexts:consolePrompt.setStatus(_A)
_Webinterface_ObjectIdentity=ObjectIdentity
webinterface=_Webinterface_ObjectIdentity((1,3,6,1,4,1,3181,10,3,21))
class _WebSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WebSupport_Type.__name__=_B
_WebSupport_Object=MibScalar
webSupport=_WebSupport_Object((1,3,6,1,4,1,3181,10,3,21,1),_WebSupport_Type())
webSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:webSupport.setStatus(_A)
class _WebEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WebEnable_Type.__name__=_B
_WebEnable_Object=MibScalar
webEnable=_WebEnable_Object((1,3,6,1,4,1,3181,10,3,21,2),_WebEnable_Type())
webEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:webEnable.setStatus(_A)
_Snmpinterface_ObjectIdentity=ObjectIdentity
snmpinterface=_Snmpinterface_ObjectIdentity((1,3,6,1,4,1,3181,10,3,22))
class _SnmpSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpSupport_Type.__name__=_B
_SnmpSupport_Object=MibScalar
snmpSupport=_SnmpSupport_Object((1,3,6,1,4,1,3181,10,3,22,1),_SnmpSupport_Type())
snmpSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpSupport.setStatus(_A)
class _SnmpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpEnable_Type.__name__=_B
_SnmpEnable_Object=MibScalar
snmpEnable=_SnmpEnable_Object((1,3,6,1,4,1,3181,10,3,22,2),_SnmpEnable_Type())
snmpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpEnable.setStatus(_A)
class _SnmpApplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A3,1),(_A4,2),(_A5,3)))
_SnmpApplyMode_Type.__name__=_B
_SnmpApplyMode_Object=MibScalar
snmpApplyMode=_SnmpApplyMode_Object((1,3,6,1,4,1,3181,10,3,22,3),_SnmpApplyMode_Type())
snmpApplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpApplyMode.setStatus(_A)
class _SnmpApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('applyNow',1),('applyAndSaveNow',2)))
_SnmpApply_Type.__name__=_B
_SnmpApply_Object=MibScalar
snmpApply=_SnmpApply_Object((1,3,6,1,4,1,3181,10,3,22,4),_SnmpApply_Type())
snmpApply.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpApply.setStatus(_A)
class _SnmpTrapTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,255)));namedValues=NamedValues(*(('inactive',0),('genColdstart',1),('genWarmstart',2),('genLinkdown',3),('genLinkup',4),('genAuthfailure',5),('genEgpneighborloss',6),('entLinkchange',7),('entFactoryreset',8),('entTemplevelchange',9),('entErrorcounter',10),('entOverundervoltage',11),('entTempshutdown',12),('entPoelimitexceeded',13),('entSupplystatuschange',14),('entSfpplugchange',15),('entLoginfailure',16),('entRingbroken',17),('entRingalarm',18),('entAuthpwfail',19),('entPrivpwfail',20),('entAccesspermission',21),('entSeclevelfail',22),(_D,255)))
_SnmpTrapTest_Type.__name__=_B
_SnmpTrapTest_Object=MibScalar
snmpTrapTest=_SnmpTrapTest_Object((1,3,6,1,4,1,3181,10,3,22,5),_SnmpTrapTest_Type())
snmpTrapTest.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapTest.setStatus(_A)
_SnmpTrapDestCount_Type=Integer32
_SnmpTrapDestCount_Object=MibScalar
snmpTrapDestCount=_SnmpTrapDestCount_Object((1,3,6,1,4,1,3181,10,3,22,6),_SnmpTrapDestCount_Type())
snmpTrapDestCount.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpTrapDestCount.setStatus(_A)
class _SnmpCommunityRead_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnmpCommunityRead_Type.__name__=_L
_SnmpCommunityRead_Object=MibScalar
snmpCommunityRead=_SnmpCommunityRead_Object((1,3,6,1,4,1,3181,10,3,22,7),_SnmpCommunityRead_Type())
snmpCommunityRead.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCommunityRead.setStatus(_A)
class _SnmpCommunityWrite_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnmpCommunityWrite_Type.__name__=_L
_SnmpCommunityWrite_Object=MibScalar
snmpCommunityWrite=_SnmpCommunityWrite_Object((1,3,6,1,4,1,3181,10,3,22,8),_SnmpCommunityWrite_Type())
snmpCommunityWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpCommunityWrite.setStatus(_A)
class _SnmpTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEnable_Type.__name__=_B
_SnmpTrapEnable_Object=MibScalar
snmpTrapEnable=_SnmpTrapEnable_Object((1,3,6,1,4,1,3181,10,3,22,9),_SnmpTrapEnable_Type())
snmpTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEnable.setStatus(_A)
_SnmpTrapDestTable_Object=MibTable
snmpTrapDestTable=_SnmpTrapDestTable_Object((1,3,6,1,4,1,3181,10,3,22,10))
if mibBuilder.loadTexts:snmpTrapDestTable.setStatus(_A)
_SnmpTrapDestTableEntry_Object=MibTableRow
snmpTrapDestTableEntry=_SnmpTrapDestTableEntry_Object((1,3,6,1,4,1,3181,10,3,22,10,1))
snmpTrapDestTableEntry.setIndexNames((0,_J,_A6))
if mibBuilder.loadTexts:snmpTrapDestTableEntry.setStatus(_A)
class _SnmpTrapDestId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SnmpTrapDestId_Type.__name__=_B
_SnmpTrapDestId_Object=MibTableColumn
snmpTrapDestId=_SnmpTrapDestId_Object((1,3,6,1,4,1,3181,10,3,22,10,1,1),_SnmpTrapDestId_Type())
snmpTrapDestId.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpTrapDestId.setStatus(_A)
class _SnmpTrapDestAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnmpTrapDestAlias_Type.__name__=_L
_SnmpTrapDestAlias_Object=MibTableColumn
snmpTrapDestAlias=_SnmpTrapDestAlias_Object((1,3,6,1,4,1,3181,10,3,22,10,1,2),_SnmpTrapDestAlias_Type())
snmpTrapDestAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapDestAlias.setStatus(_A)
class _SnmpTrapDestEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,255)));namedValues=NamedValues(*((_F,0),('v1',1),('v2c',2),('v3',3),(_D,255)))
_SnmpTrapDestEn_Type.__name__=_B
_SnmpTrapDestEn_Object=MibTableColumn
snmpTrapDestEn=_SnmpTrapDestEn_Object((1,3,6,1,4,1,3181,10,3,22,10,1,3),_SnmpTrapDestEn_Type())
snmpTrapDestEn.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapDestEn.setStatus(_A)
_SnmpTrapDestIPv4Address_Type=IpAddress
_SnmpTrapDestIPv4Address_Object=MibTableColumn
snmpTrapDestIPv4Address=_SnmpTrapDestIPv4Address_Object((1,3,6,1,4,1,3181,10,3,22,10,1,4),_SnmpTrapDestIPv4Address_Type())
snmpTrapDestIPv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapDestIPv4Address.setStatus(_A)
class _SnmpTrapDestCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnmpTrapDestCommunity_Type.__name__=_L
_SnmpTrapDestCommunity_Object=MibTableColumn
snmpTrapDestCommunity=_SnmpTrapDestCommunity_Object((1,3,6,1,4,1,3181,10,3,22,10,1,5),_SnmpTrapDestCommunity_Type())
snmpTrapDestCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapDestCommunity.setStatus(_A)
class _SnmpTrapGenColdstart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapGenColdstart_Type.__name__=_B
_SnmpTrapGenColdstart_Object=MibTableColumn
snmpTrapGenColdstart=_SnmpTrapGenColdstart_Object((1,3,6,1,4,1,3181,10,3,22,10,1,6),_SnmpTrapGenColdstart_Type())
snmpTrapGenColdstart.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapGenColdstart.setStatus(_A)
class _SnmpTrapGenWarmstart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapGenWarmstart_Type.__name__=_B
_SnmpTrapGenWarmstart_Object=MibTableColumn
snmpTrapGenWarmstart=_SnmpTrapGenWarmstart_Object((1,3,6,1,4,1,3181,10,3,22,10,1,7),_SnmpTrapGenWarmstart_Type())
snmpTrapGenWarmstart.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpTrapGenWarmstart.setStatus(_A)
class _SnmpTrapGenLinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapGenLinkDown_Type.__name__=_B
_SnmpTrapGenLinkDown_Object=MibTableColumn
snmpTrapGenLinkDown=_SnmpTrapGenLinkDown_Object((1,3,6,1,4,1,3181,10,3,22,10,1,8),_SnmpTrapGenLinkDown_Type())
snmpTrapGenLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapGenLinkDown.setStatus(_A)
class _SnmpTrapGenLinkUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapGenLinkUp_Type.__name__=_B
_SnmpTrapGenLinkUp_Object=MibTableColumn
snmpTrapGenLinkUp=_SnmpTrapGenLinkUp_Object((1,3,6,1,4,1,3181,10,3,22,10,1,9),_SnmpTrapGenLinkUp_Type())
snmpTrapGenLinkUp.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapGenLinkUp.setStatus(_A)
class _SnmpTrapGenAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapGenAuthFailure_Type.__name__=_B
_SnmpTrapGenAuthFailure_Object=MibTableColumn
snmpTrapGenAuthFailure=_SnmpTrapGenAuthFailure_Object((1,3,6,1,4,1,3181,10,3,22,10,1,10),_SnmpTrapGenAuthFailure_Type())
snmpTrapGenAuthFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapGenAuthFailure.setStatus(_A)
class _SnmpTrapGenEgpNeighborLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapGenEgpNeighborLoss_Type.__name__=_B
_SnmpTrapGenEgpNeighborLoss_Object=MibTableColumn
snmpTrapGenEgpNeighborLoss=_SnmpTrapGenEgpNeighborLoss_Object((1,3,6,1,4,1,3181,10,3,22,10,1,11),_SnmpTrapGenEgpNeighborLoss_Type())
snmpTrapGenEgpNeighborLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpTrapGenEgpNeighborLoss.setStatus(_A)
class _SnmpTrapEntLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntLinkChange_Type.__name__=_B
_SnmpTrapEntLinkChange_Object=MibTableColumn
snmpTrapEntLinkChange=_SnmpTrapEntLinkChange_Object((1,3,6,1,4,1,3181,10,3,22,10,1,12),_SnmpTrapEntLinkChange_Type())
snmpTrapEntLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntLinkChange.setStatus(_A)
class _SnmpTrapEntFactoryReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntFactoryReset_Type.__name__=_B
_SnmpTrapEntFactoryReset_Object=MibTableColumn
snmpTrapEntFactoryReset=_SnmpTrapEntFactoryReset_Object((1,3,6,1,4,1,3181,10,3,22,10,1,13),_SnmpTrapEntFactoryReset_Type())
snmpTrapEntFactoryReset.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntFactoryReset.setStatus(_A)
class _SnmpTrapEntTemperatureLevelChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntTemperatureLevelChange_Type.__name__=_B
_SnmpTrapEntTemperatureLevelChange_Object=MibTableColumn
snmpTrapEntTemperatureLevelChange=_SnmpTrapEntTemperatureLevelChange_Object((1,3,6,1,4,1,3181,10,3,22,10,1,14),_SnmpTrapEntTemperatureLevelChange_Type())
snmpTrapEntTemperatureLevelChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntTemperatureLevelChange.setStatus(_A)
class _SnmpTrapEntErrorCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntErrorCounter_Type.__name__=_B
_SnmpTrapEntErrorCounter_Object=MibTableColumn
snmpTrapEntErrorCounter=_SnmpTrapEntErrorCounter_Object((1,3,6,1,4,1,3181,10,3,22,10,1,15),_SnmpTrapEntErrorCounter_Type())
snmpTrapEntErrorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntErrorCounter.setStatus(_A)
class _SnmpTrapEntUnderOverVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntUnderOverVoltage_Type.__name__=_B
_SnmpTrapEntUnderOverVoltage_Object=MibTableColumn
snmpTrapEntUnderOverVoltage=_SnmpTrapEntUnderOverVoltage_Object((1,3,6,1,4,1,3181,10,3,22,10,1,16),_SnmpTrapEntUnderOverVoltage_Type())
snmpTrapEntUnderOverVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntUnderOverVoltage.setStatus(_A)
class _SnmpTrapEntTempShutDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntTempShutDown_Type.__name__=_B
_SnmpTrapEntTempShutDown_Object=MibTableColumn
snmpTrapEntTempShutDown=_SnmpTrapEntTempShutDown_Object((1,3,6,1,4,1,3181,10,3,22,10,1,17),_SnmpTrapEntTempShutDown_Type())
snmpTrapEntTempShutDown.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntTempShutDown.setStatus(_A)
class _SnmpTrapEntPoeLimitExceeded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntPoeLimitExceeded_Type.__name__=_B
_SnmpTrapEntPoeLimitExceeded_Object=MibTableColumn
snmpTrapEntPoeLimitExceeded=_SnmpTrapEntPoeLimitExceeded_Object((1,3,6,1,4,1,3181,10,3,22,10,1,18),_SnmpTrapEntPoeLimitExceeded_Type())
snmpTrapEntPoeLimitExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntPoeLimitExceeded.setStatus(_A)
class _SnmpTrapEntSupplyStatusChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntSupplyStatusChange_Type.__name__=_B
_SnmpTrapEntSupplyStatusChange_Object=MibTableColumn
snmpTrapEntSupplyStatusChange=_SnmpTrapEntSupplyStatusChange_Object((1,3,6,1,4,1,3181,10,3,22,10,1,19),_SnmpTrapEntSupplyStatusChange_Type())
snmpTrapEntSupplyStatusChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntSupplyStatusChange.setStatus(_A)
class _SnmpTrapEntSfpPlugChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntSfpPlugChange_Type.__name__=_B
_SnmpTrapEntSfpPlugChange_Object=MibTableColumn
snmpTrapEntSfpPlugChange=_SnmpTrapEntSfpPlugChange_Object((1,3,6,1,4,1,3181,10,3,22,10,1,20),_SnmpTrapEntSfpPlugChange_Type())
snmpTrapEntSfpPlugChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntSfpPlugChange.setStatus(_A)
class _SnmpTrapEntLoginFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntLoginFailure_Type.__name__=_B
_SnmpTrapEntLoginFailure_Object=MibTableColumn
snmpTrapEntLoginFailure=_SnmpTrapEntLoginFailure_Object((1,3,6,1,4,1,3181,10,3,22,10,1,21),_SnmpTrapEntLoginFailure_Type())
snmpTrapEntLoginFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntLoginFailure.setStatus(_A)
class _SnmpTrapEntRingBroken_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntRingBroken_Type.__name__=_B
_SnmpTrapEntRingBroken_Object=MibTableColumn
snmpTrapEntRingBroken=_SnmpTrapEntRingBroken_Object((1,3,6,1,4,1,3181,10,3,22,10,1,22),_SnmpTrapEntRingBroken_Type())
snmpTrapEntRingBroken.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntRingBroken.setStatus(_A)
class _SnmpTrapEntRingAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntRingAlarm_Type.__name__=_B
_SnmpTrapEntRingAlarm_Object=MibTableColumn
snmpTrapEntRingAlarm=_SnmpTrapEntRingAlarm_Object((1,3,6,1,4,1,3181,10,3,22,10,1,23),_SnmpTrapEntRingAlarm_Type())
snmpTrapEntRingAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntRingAlarm.setStatus(_A)
class _SnmpTrapEntAuthPwFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntAuthPwFail_Type.__name__=_B
_SnmpTrapEntAuthPwFail_Object=MibTableColumn
snmpTrapEntAuthPwFail=_SnmpTrapEntAuthPwFail_Object((1,3,6,1,4,1,3181,10,3,22,10,1,24),_SnmpTrapEntAuthPwFail_Type())
snmpTrapEntAuthPwFail.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntAuthPwFail.setStatus(_A)
class _SnmpTrapEntPrivPwFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntPrivPwFail_Type.__name__=_B
_SnmpTrapEntPrivPwFail_Object=MibTableColumn
snmpTrapEntPrivPwFail=_SnmpTrapEntPrivPwFail_Object((1,3,6,1,4,1,3181,10,3,22,10,1,25),_SnmpTrapEntPrivPwFail_Type())
snmpTrapEntPrivPwFail.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntPrivPwFail.setStatus(_A)
class _SnmpTrapEntAccessPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntAccessPermission_Type.__name__=_B
_SnmpTrapEntAccessPermission_Object=MibTableColumn
snmpTrapEntAccessPermission=_SnmpTrapEntAccessPermission_Object((1,3,6,1,4,1,3181,10,3,22,10,1,26),_SnmpTrapEntAccessPermission_Type())
snmpTrapEntAccessPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntAccessPermission.setStatus(_A)
class _SnmpTrapEntSeclevelFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SnmpTrapEntSeclevelFail_Type.__name__=_B
_SnmpTrapEntSeclevelFail_Object=MibTableColumn
snmpTrapEntSeclevelFail=_SnmpTrapEntSeclevelFail_Object((1,3,6,1,4,1,3181,10,3,22,10,1,27),_SnmpTrapEntSeclevelFail_Type())
snmpTrapEntSeclevelFail.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTrapEntSeclevelFail.setStatus(_A)
_Udpinterface_ObjectIdentity=ObjectIdentity
udpinterface=_Udpinterface_ObjectIdentity((1,3,6,1,4,1,3181,10,3,23))
class _UdpSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,255)));namedValues=NamedValues(*((_M,1),('umac',3),(_D,255)))
_UdpSupport_Type.__name__=_B
_UdpSupport_Object=MibScalar
udpSupport=_UdpSupport_Object((1,3,6,1,4,1,3181,10,3,23,1),_UdpSupport_Type())
udpSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:udpSupport.setStatus(_A)
class _UdpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_UdpEnable_Type.__name__=_B
_UdpEnable_Object=MibScalar
udpEnable=_UdpEnable_Object((1,3,6,1,4,1,3181,10,3,23,2),_UdpEnable_Type())
udpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:udpEnable.setStatus(_A)
class _UdpUmacEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_G,1),(_D,255)))
_UdpUmacEnable_Type.__name__=_B
_UdpUmacEnable_Object=MibScalar
udpUmacEnable=_UdpUmacEnable_Object((1,3,6,1,4,1,3181,10,3,23,3),_UdpUmacEnable_Type())
udpUmacEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:udpUmacEnable.setStatus(_A)
_Syslog_ObjectIdentity=ObjectIdentity
syslog=_Syslog_ObjectIdentity((1,3,6,1,4,1,3181,10,3,24))
class _SyslogSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_SyslogSupport_Type.__name__=_B
_SyslogSupport_Object=MibScalar
syslogSupport=_SyslogSupport_Object((1,3,6,1,4,1,3181,10,3,24,1),_SyslogSupport_Type())
syslogSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:syslogSupport.setStatus(_A)
class _SyslogEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SyslogEnable_Type.__name__=_B
_SyslogEnable_Object=MibScalar
syslogEnable=_SyslogEnable_Object((1,3,6,1,4,1,3181,10,3,24,2),_SyslogEnable_Type())
syslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogEnable.setStatus(_A)
class _SyslogMessageTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*(('inactive',0),('sendmessage',1),(_D,255)))
_SyslogMessageTest_Type.__name__=_B
_SyslogMessageTest_Object=MibScalar
syslogMessageTest=_SyslogMessageTest_Object((1,3,6,1,4,1,3181,10,3,24,3),_SyslogMessageTest_Type())
syslogMessageTest.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMessageTest.setStatus(_A)
_SyslogDestCount_Type=Integer32
_SyslogDestCount_Object=MibScalar
syslogDestCount=_SyslogDestCount_Object((1,3,6,1,4,1,3181,10,3,24,4),_SyslogDestCount_Type())
syslogDestCount.setMaxAccess(_E)
if mibBuilder.loadTexts:syslogDestCount.setStatus(_A)
_SyslogDestTable_Object=MibTable
syslogDestTable=_SyslogDestTable_Object((1,3,6,1,4,1,3181,10,3,24,10))
if mibBuilder.loadTexts:syslogDestTable.setStatus(_A)
_SyslogDestTableEntry_Object=MibTableRow
syslogDestTableEntry=_SyslogDestTableEntry_Object((1,3,6,1,4,1,3181,10,3,24,10,1))
syslogDestTableEntry.setIndexNames((0,_J,_A7))
if mibBuilder.loadTexts:syslogDestTableEntry.setStatus(_A)
class _SyslogDestId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SyslogDestId_Type.__name__=_B
_SyslogDestId_Object=MibTableColumn
syslogDestId=_SyslogDestId_Object((1,3,6,1,4,1,3181,10,3,24,10,1,1),_SyslogDestId_Type())
syslogDestId.setMaxAccess(_E)
if mibBuilder.loadTexts:syslogDestId.setStatus(_A)
class _SyslogDestAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SyslogDestAlias_Type.__name__=_L
_SyslogDestAlias_Object=MibTableColumn
syslogDestAlias=_SyslogDestAlias_Object((1,3,6,1,4,1,3181,10,3,24,10,1,2),_SyslogDestAlias_Type())
syslogDestAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDestAlias.setStatus(_A)
class _SyslogDestEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_SyslogDestEnable_Type.__name__=_B
_SyslogDestEnable_Object=MibTableColumn
syslogDestEnable=_SyslogDestEnable_Object((1,3,6,1,4,1,3181,10,3,24,10,1,3),_SyslogDestEnable_Type())
syslogDestEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDestEnable.setStatus(_A)
_SyslogDestIpv4Address_Type=IpAddress
_SyslogDestIpv4Address_Object=MibTableColumn
syslogDestIpv4Address=_SyslogDestIpv4Address_Object((1,3,6,1,4,1,3181,10,3,24,10,1,4),_SyslogDestIpv4Address_Type())
syslogDestIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDestIpv4Address.setStatus(_A)
_SyslogDestPort_Type=Integer32
_SyslogDestPort_Object=MibTableColumn
syslogDestPort=_SyslogDestPort_Object((1,3,6,1,4,1,3181,10,3,24,10,1,5),_SyslogDestPort_Type())
syslogDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDestPort.setStatus(_A)
class _SyslogDestFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernelMessage',0),('userLevelMessage',1),('mailSystem',2),('systemDaemon',3),('securityMessage1',4),('syslogdMessage',5),('linePrinterSubsystem',6),('networkNewsSubsystem',7),('uucpSubsystem',8),('clockDeamon1',9),('securityMessage2',10),('ftpDeamon',11),('ntpSubsystem',12),('logAudit',13),('logAlert',14),('clockDeamon2',15),('localUse0',16),('localUse1',17),('localUse2',18),('localUse3',19),('localUse4',20),('localUse5',21),('localUse6',22),('localUse7',23)))
_SyslogDestFacility_Type.__name__=_B
_SyslogDestFacility_Object=MibTableColumn
syslogDestFacility=_SyslogDestFacility_Object((1,3,6,1,4,1,3181,10,3,24,10,1,6),_SyslogDestFacility_Type())
syslogDestFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDestFacility.setStatus(_A)
class _SyslogDestEventFilter_Type(Bits):namedValues=NamedValues(*((_Z,0),('linkchange',1),('configchange',2),('login',3),('firmwareupdate',4),('powerredundancy',5),('portauth',6),('temperature',7),('ring',8),('sfp',9),('poe',10),('rtc',11),('vct',12),('debug',29),('statusreport',30),('test',31)))
_SyslogDestEventFilter_Type.__name__=_Q
_SyslogDestEventFilter_Object=MibTableColumn
syslogDestEventFilter=_SyslogDestEventFilter_Object((1,3,6,1,4,1,3181,10,3,24,10,1,7),_SyslogDestEventFilter_Type())
syslogDestEventFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDestEventFilter.setStatus(_A)
_Radius_ObjectIdentity=ObjectIdentity
radius=_Radius_ObjectIdentity((1,3,6,1,4,1,3181,10,3,25))
class _RadiusSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_RadiusSupport_Type.__name__=_B
_RadiusSupport_Object=MibScalar
radiusSupport=_RadiusSupport_Object((1,3,6,1,4,1,3181,10,3,25,1),_RadiusSupport_Type())
radiusSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSupport.setStatus(_A)
class _RadiusAccessEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_RadiusAccessEnable_Type.__name__=_B
_RadiusAccessEnable_Object=MibScalar
radiusAccessEnable=_RadiusAccessEnable_Object((1,3,6,1,4,1,3181,10,3,25,2),_RadiusAccessEnable_Type())
radiusAccessEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusAccessEnable.setStatus(_A)
class _RadiusAccountEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_RadiusAccountEnable_Type.__name__=_B
_RadiusAccountEnable_Object=MibScalar
radiusAccountEnable=_RadiusAccountEnable_Object((1,3,6,1,4,1,3181,10,3,25,3),_RadiusAccountEnable_Type())
radiusAccountEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusAccountEnable.setStatus(_A)
_RadiusServerCount_Type=Integer32
_RadiusServerCount_Object=MibScalar
radiusServerCount=_RadiusServerCount_Object((1,3,6,1,4,1,3181,10,3,25,4),_RadiusServerCount_Type())
radiusServerCount.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusServerCount.setStatus(_A)
class _RadiusMacAuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RadiusMacAuthPassword_Type.__name__=_L
_RadiusMacAuthPassword_Object=MibScalar
radiusMacAuthPassword=_RadiusMacAuthPassword_Object((1,3,6,1,4,1,3181,10,3,25,5),_RadiusMacAuthPassword_Type())
radiusMacAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusMacAuthPassword.setStatus(_A)
class _RadiusUseMacAsPassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_RadiusUseMacAsPassword_Type.__name__=_B
_RadiusUseMacAsPassword_Object=MibScalar
radiusUseMacAsPassword=_RadiusUseMacAsPassword_Object((1,3,6,1,4,1,3181,10,3,25,6),_RadiusUseMacAsPassword_Type())
radiusUseMacAsPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusUseMacAsPassword.setStatus(_A)
class _RadiusMacSeparator_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_RadiusMacSeparator_Type.__name__=_L
_RadiusMacSeparator_Object=MibScalar
radiusMacSeparator=_RadiusMacSeparator_Object((1,3,6,1,4,1,3181,10,3,25,7),_RadiusMacSeparator_Type())
radiusMacSeparator.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusMacSeparator.setStatus(_A)
class _RadiusTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusTimeout_Type.__name__=_B
_RadiusTimeout_Object=MibScalar
radiusTimeout=_RadiusTimeout_Object((1,3,6,1,4,1,3181,10,3,25,8),_RadiusTimeout_Type())
radiusTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusTimeout.setStatus(_A)
class _RadiusMacLettercase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lower',1),('upper',2)))
_RadiusMacLettercase_Type.__name__=_B
_RadiusMacLettercase_Object=MibScalar
radiusMacLettercase=_RadiusMacLettercase_Object((1,3,6,1,4,1,3181,10,3,25,9),_RadiusMacLettercase_Type())
radiusMacLettercase.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusMacLettercase.setStatus(_A)
_RadiusServerTable_Object=MibTable
radiusServerTable=_RadiusServerTable_Object((1,3,6,1,4,1,3181,10,3,25,10))
if mibBuilder.loadTexts:radiusServerTable.setStatus(_A)
_RadiusServerTableEntry_Object=MibTableRow
radiusServerTableEntry=_RadiusServerTableEntry_Object((1,3,6,1,4,1,3181,10,3,25,10,1))
radiusServerTableEntry.setIndexNames((0,_J,_A8))
if mibBuilder.loadTexts:radiusServerTableEntry.setStatus(_A)
class _RadiusServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RadiusServerId_Type.__name__=_B
_RadiusServerId_Object=MibTableColumn
radiusServerId=_RadiusServerId_Object((1,3,6,1,4,1,3181,10,3,25,10,1,1),_RadiusServerId_Type())
radiusServerId.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusServerId.setStatus(_A)
class _RadiusServerAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RadiusServerAlias_Type.__name__=_L
_RadiusServerAlias_Object=MibTableColumn
radiusServerAlias=_RadiusServerAlias_Object((1,3,6,1,4,1,3181,10,3,25,10,1,2),_RadiusServerAlias_Type())
radiusServerAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerAlias.setStatus(_A)
class _RadiusServerEnableAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_RadiusServerEnableAccess_Type.__name__=_B
_RadiusServerEnableAccess_Object=MibTableColumn
radiusServerEnableAccess=_RadiusServerEnableAccess_Object((1,3,6,1,4,1,3181,10,3,25,10,1,3),_RadiusServerEnableAccess_Type())
radiusServerEnableAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerEnableAccess.setStatus(_A)
class _RadiusServerEnableAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_RadiusServerEnableAccount_Type.__name__=_B
_RadiusServerEnableAccount_Object=MibTableColumn
radiusServerEnableAccount=_RadiusServerEnableAccount_Object((1,3,6,1,4,1,3181,10,3,25,10,1,4),_RadiusServerEnableAccount_Type())
radiusServerEnableAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerEnableAccount.setStatus(_A)
_RadiusServerIpv4Address_Type=IpAddress
_RadiusServerIpv4Address_Object=MibTableColumn
radiusServerIpv4Address=_RadiusServerIpv4Address_Object((1,3,6,1,4,1,3181,10,3,25,10,1,5),_RadiusServerIpv4Address_Type())
radiusServerIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerIpv4Address.setStatus(_A)
_RadiusServerAccessPort_Type=Integer32
_RadiusServerAccessPort_Object=MibTableColumn
radiusServerAccessPort=_RadiusServerAccessPort_Object((1,3,6,1,4,1,3181,10,3,25,10,1,6),_RadiusServerAccessPort_Type())
radiusServerAccessPort.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerAccessPort.setStatus(_A)
_RadiusServerAccountPort_Type=Integer32
_RadiusServerAccountPort_Object=MibTableColumn
radiusServerAccountPort=_RadiusServerAccountPort_Object((1,3,6,1,4,1,3181,10,3,25,10,1,7),_RadiusServerAccountPort_Type())
radiusServerAccountPort.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerAccountPort.setStatus(_A)
class _RadiusServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RadiusServerSecret_Type.__name__=_L
_RadiusServerSecret_Object=MibTableColumn
radiusServerSecret=_RadiusServerSecret_Object((1,3,6,1,4,1,3181,10,3,25,10,1,8),_RadiusServerSecret_Type())
radiusServerSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerSecret.setStatus(_A)
_Supply_ObjectIdentity=ObjectIdentity
supply=_Supply_ObjectIdentity((1,3,6,1,4,1,3181,10,3,30))
_SupplyCount_Type=Integer32
_SupplyCount_Object=MibScalar
supplyCount=_SupplyCount_Object((1,3,6,1,4,1,3181,10,3,30,1),_SupplyCount_Type())
supplyCount.setMaxAccess(_E)
if mibBuilder.loadTexts:supplyCount.setStatus(_A)
_SupplyTable_Object=MibTable
supplyTable=_SupplyTable_Object((1,3,6,1,4,1,3181,10,3,30,10))
if mibBuilder.loadTexts:supplyTable.setStatus(_A)
_SupplyTableEntry_Object=MibTableRow
supplyTableEntry=_SupplyTableEntry_Object((1,3,6,1,4,1,3181,10,3,30,10,1))
supplyTableEntry.setIndexNames((0,_J,_a))
if mibBuilder.loadTexts:supplyTableEntry.setStatus(_A)
class _SupplyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SupplyId_Type.__name__=_B
_SupplyId_Object=MibTableColumn
supplyId=_SupplyId_Object((1,3,6,1,4,1,3181,10,3,30,10,1,1),_SupplyId_Type())
supplyId.setMaxAccess(_E)
if mibBuilder.loadTexts:supplyId.setStatus(_A)
class _SupplyUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('used',1),('unused',2),(_D,255)))
_SupplyUsed_Type.__name__=_B
_SupplyUsed_Object=MibTableColumn
supplyUsed=_SupplyUsed_Object((1,3,6,1,4,1,3181,10,3,30,10,1,2),_SupplyUsed_Type())
supplyUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyUsed.setStatus(_A)
class _SupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('valid',1),('invalid',2),(_K,254),(_D,255)))
_SupplyStatus_Type.__name__=_B
_SupplyStatus_Object=MibTableColumn
supplyStatus=_SupplyStatus_Object((1,3,6,1,4,1,3181,10,3,30,10,1,3),_SupplyStatus_Type())
supplyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:supplyStatus.setStatus(_A)
_Poepse_ObjectIdentity=ObjectIdentity
poepse=_Poepse_ObjectIdentity((1,3,6,1,4,1,3181,10,3,31))
class _PoepseSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_PoepseSupport_Type.__name__=_B
_PoepseSupport_Object=MibScalar
poepseSupport=_PoepseSupport_Object((1,3,6,1,4,1,3181,10,3,31,1),_PoepseSupport_Type())
poepseSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:poepseSupport.setStatus(_A)
class _PoepseEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PoepseEnable_Type.__name__=_B
_PoepseEnable_Object=MibScalar
poepseEnable=_PoepseEnable_Object((1,3,6,1,4,1,3181,10,3,31,2),_PoepseEnable_Type())
poepseEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:poepseEnable.setStatus(_A)
_PoepseTotalInputPower_Type=Integer32
_PoepseTotalInputPower_Object=MibScalar
poepseTotalInputPower=_PoepseTotalInputPower_Object((1,3,6,1,4,1,3181,10,3,31,3),_PoepseTotalInputPower_Type())
poepseTotalInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:poepseTotalInputPower.setStatus(_A)
_PoepseMaxInputPower_Type=Integer32
_PoepseMaxInputPower_Object=MibScalar
poepseMaxInputPower=_PoepseMaxInputPower_Object((1,3,6,1,4,1,3181,10,3,31,4),_PoepseMaxInputPower_Type())
poepseMaxInputPower.setMaxAccess(_E)
if mibBuilder.loadTexts:poepseMaxInputPower.setStatus(_A)
_PoepseDeviceSupplyPower_Type=Integer32
_PoepseDeviceSupplyPower_Object=MibScalar
poepseDeviceSupplyPower=_PoepseDeviceSupplyPower_Object((1,3,6,1,4,1,3181,10,3,31,5),_PoepseDeviceSupplyPower_Type())
poepseDeviceSupplyPower.setMaxAccess(_E)
if mibBuilder.loadTexts:poepseDeviceSupplyPower.setStatus(_A)
_PseAvailablePower_Type=Integer32
_PseAvailablePower_Object=MibScalar
pseAvailablePower=_PseAvailablePower_Object((1,3,6,1,4,1,3181,10,3,31,6),_PseAvailablePower_Type())
pseAvailablePower.setMaxAccess(_E)
if mibBuilder.loadTexts:pseAvailablePower.setStatus(_A)
class _PoepseExtendedVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_PoepseExtendedVoltage_Type.__name__=_B
_PoepseExtendedVoltage_Object=MibScalar
poepseExtendedVoltage=_PoepseExtendedVoltage_Object((1,3,6,1,4,1,3181,10,3,31,7),_PoepseExtendedVoltage_Type())
poepseExtendedVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:poepseExtendedVoltage.setStatus(_A)
_PoepsePortTable_Object=MibTable
poepsePortTable=_PoepsePortTable_Object((1,3,6,1,4,1,3181,10,3,31,10))
if mibBuilder.loadTexts:poepsePortTable.setStatus(_A)
_PoepsePortTableEntry_Object=MibTableRow
poepsePortTableEntry=_PoepsePortTableEntry_Object((1,3,6,1,4,1,3181,10,3,31,10,1))
poepsePortTableEntry.setIndexNames((0,_J,_A9))
if mibBuilder.loadTexts:poepsePortTableEntry.setStatus(_A)
class _PoepsePortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_PoepsePortId_Type.__name__=_B
_PoepsePortId_Object=MibTableColumn
poepsePortId=_PoepsePortId_Object((1,3,6,1,4,1,3181,10,3,31,10,1,1),_PoepsePortId_Type())
poepsePortId.setMaxAccess(_E)
if mibBuilder.loadTexts:poepsePortId.setStatus(_A)
class _PoepsePortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,254,255)));namedValues=NamedValues(*(('poe8023af',1),('poeForced',2),('poeDisabled',3),(_K,254),(_D,255)))
_PoepsePortMode_Type.__name__=_B
_PoepsePortMode_Object=MibTableColumn
poepsePortMode=_PoepsePortMode_Object((1,3,6,1,4,1,3181,10,3,31,10,1,2),_PoepsePortMode_Type())
poepsePortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:poepsePortMode.setStatus(_A)
class _PoepsePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,254,255)));namedValues=NamedValues(*(('off',0),('discovering',1),('powered',2),('fault',3),(_F,4),('overcurrent',5),(_K,254),(_D,255)))
_PoepsePortStatus_Type.__name__=_B
_PoepsePortStatus_Object=MibTableColumn
poepsePortStatus=_PoepsePortStatus_Object((1,3,6,1,4,1,3181,10,3,31,10,1,3),_PoepsePortStatus_Type())
poepsePortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:poepsePortStatus.setStatus(_A)
class _PoepsePortMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15400))
_PoepsePortMaxPower_Type.__name__=_B
_PoepsePortMaxPower_Object=MibTableColumn
poepsePortMaxPower=_PoepsePortMaxPower_Object((1,3,6,1,4,1,3181,10,3,31,10,1,4),_PoepsePortMaxPower_Type())
poepsePortMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:poepsePortMaxPower.setStatus(_A)
_PoepsePortMeasuredPower_Type=Integer32
_PoepsePortMeasuredPower_Object=MibTableColumn
poepsePortMeasuredPower=_PoepsePortMeasuredPower_Object((1,3,6,1,4,1,3181,10,3,31,10,1,5),_PoepsePortMeasuredPower_Type())
poepsePortMeasuredPower.setMaxAccess(_E)
if mibBuilder.loadTexts:poepsePortMeasuredPower.setStatus(_A)
class _PoepsePortMaxClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254,255)));namedValues=NamedValues(*(('class0',0),('class1',1),('class2',2),('class3',3),('class4',4),(_K,254),(_D,255)))
_PoepsePortMaxClass_Type.__name__=_B
_PoepsePortMaxClass_Object=MibTableColumn
poepsePortMaxClass=_PoepsePortMaxClass_Object((1,3,6,1,4,1,3181,10,3,31,10,1,6),_PoepsePortMaxClass_Type())
poepsePortMaxClass.setMaxAccess(_C)
if mibBuilder.loadTexts:poepsePortMaxClass.setStatus(_A)
class _PoepsePortDetectedClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254,255)));namedValues=NamedValues(*(('class0',0),('class1',1),('class2',2),('class3',3),('class4',4),(_K,254),(_D,255)))
_PoepsePortDetectedClass_Type.__name__=_B
_PoepsePortDetectedClass_Object=MibTableColumn
poepsePortDetectedClass=_PoepsePortDetectedClass_Object((1,3,6,1,4,1,3181,10,3,31,10,1,7),_PoepsePortDetectedClass_Type())
poepsePortDetectedClass.setMaxAccess(_E)
if mibBuilder.loadTexts:poepsePortDetectedClass.setStatus(_A)
_PoepsePortMeasuredVoltage_Type=Integer32
_PoepsePortMeasuredVoltage_Object=MibTableColumn
poepsePortMeasuredVoltage=_PoepsePortMeasuredVoltage_Object((1,3,6,1,4,1,3181,10,3,31,10,1,8),_PoepsePortMeasuredVoltage_Type())
poepsePortMeasuredVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:poepsePortMeasuredVoltage.setStatus(_A)
_Poepd_ObjectIdentity=ObjectIdentity
poepd=_Poepd_ObjectIdentity((1,3,6,1,4,1,3181,10,3,32))
class _PoepdSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_PoepdSupport_Type.__name__=_B
_PoepdSupport_Object=MibScalar
poepdSupport=_PoepdSupport_Object((1,3,6,1,4,1,3181,10,3,32,1),_PoepdSupport_Type())
poepdSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:poepdSupport.setStatus(_A)
_Hardwarecode_ObjectIdentity=ObjectIdentity
hardwarecode=_Hardwarecode_ObjectIdentity((1,3,6,1,4,1,3181,10,3,33))
class _HardwarecodeSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_HardwarecodeSupport_Type.__name__=_B
_HardwarecodeSupport_Object=MibScalar
hardwarecodeSupport=_HardwarecodeSupport_Object((1,3,6,1,4,1,3181,10,3,33,1),_HardwarecodeSupport_Type())
hardwarecodeSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:hardwarecodeSupport.setStatus(_A)
_HardwarecodeNumber_Type=Integer32
_HardwarecodeNumber_Object=MibScalar
hardwarecodeNumber=_HardwarecodeNumber_Object((1,3,6,1,4,1,3181,10,3,33,2),_HardwarecodeNumber_Type())
hardwarecodeNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hardwarecodeNumber.setStatus(_A)
_Spanningtree_ObjectIdentity=ObjectIdentity
spanningtree=_Spanningtree_ObjectIdentity((1,3,6,1,4,1,3181,10,3,34))
class _StpSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_M,1),(_D,255)))
_StpSupport_Type.__name__=_B
_StpSupport_Object=MibScalar
stpSupport=_StpSupport_Object((1,3,6,1,4,1,3181,10,3,34,1),_StpSupport_Type())
stpSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:stpSupport.setStatus(_A)
class _StpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_F,2),(_D,255)))
_StpEnable_Type.__name__=_B
_StpEnable_Object=MibScalar
stpEnable=_StpEnable_Object((1,3,6,1,4,1,3181,10,3,34,2),_StpEnable_Type())
stpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:stpEnable.setStatus(_A)
_MsSwitchNotifications_ObjectIdentity=ObjectIdentity
msSwitchNotifications=_MsSwitchNotifications_ObjectIdentity((1,3,6,1,4,1,3181,10,3,100))
linkChangeNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,1))
linkChangeNotification.setObjects(*((_J,_O),(_J,_b)))
if mibBuilder.loadTexts:linkChangeNotification.setStatus(_A)
factoryResetNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,2))
if mibBuilder.loadTexts:factoryResetNotification.setStatus(_A)
temperatureLevelChangeNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,3))
temperatureLevelChangeNotification.setObjects((_J,_AA))
if mibBuilder.loadTexts:temperatureLevelChangeNotification.setStatus(_A)
errorcountNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,4))
errorcountNotification.setObjects((_J,_O))
if mibBuilder.loadTexts:errorcountNotification.setStatus(_A)
underOverVoltageNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,5))
underOverVoltageNotification.setObjects((_J,_O))
if mibBuilder.loadTexts:underOverVoltageNotification.setStatus(_A)
temperatureShutdownNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,6))
if mibBuilder.loadTexts:temperatureShutdownNotification.setStatus(_A)
portPoELimitExceededNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,7))
portPoELimitExceededNotification.setObjects((_J,_O))
if mibBuilder.loadTexts:portPoELimitExceededNotification.setStatus(_A)
powerSupplyStatusChangeNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,8))
powerSupplyStatusChangeNotification.setObjects((_J,_a))
if mibBuilder.loadTexts:powerSupplyStatusChangeNotification.setStatus(_A)
sfpPlugChangeNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,9))
sfpPlugChangeNotification.setObjects(*((_J,_AB),(_J,_AC)))
if mibBuilder.loadTexts:sfpPlugChangeNotification.setStatus(_A)
loginFailureNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,10))
if mibBuilder.loadTexts:loginFailureNotification.setStatus(_A)
ringBrokenNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,11))
ringBrokenNotification.setObjects(*((_J,_c),(_J,_O),(_J,_b)))
if mibBuilder.loadTexts:ringBrokenNotification.setStatus(_A)
ringAlarmNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,12))
ringAlarmNotification.setObjects(*((_J,_c),(_J,_AD),(_J,_AE)))
if mibBuilder.loadTexts:ringAlarmNotification.setStatus(_A)
snmpv3AuthenticationPwFailNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,13))
if mibBuilder.loadTexts:snmpv3AuthenticationPwFailNotification.setStatus(_A)
snmpv3PrivacyPwFailNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,14))
if mibBuilder.loadTexts:snmpv3PrivacyPwFailNotification.setStatus(_A)
snmpv3AccessPermissionNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,15))
if mibBuilder.loadTexts:snmpv3AccessPermissionNotification.setStatus(_A)
snmpv3SeclevelFailNotification=NotificationType((1,3,6,1,4,1,3181,10,3,100,16))
if mibBuilder.loadTexts:snmpv3SeclevelFailNotification.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'microsens':microsens,'managedSwitches':managedSwitches,'mib3':mib3,'device':device,'deviceArtNo':deviceArtNo,'deviceSerNo':deviceSerNo,'deviceHardware':deviceHardware,'deviceDescription':deviceDescription,'deviceName':deviceName,'deviceLocation':deviceLocation,'deviceContact':deviceContact,'deviceGroup':deviceGroup,'deviceTemperature':deviceTemperature,_AA:deviceTemperatureLevel,'deviceUpTime':deviceUpTime,'deviceFddActiveTime':deviceFddActiveTime,'deviceFddPassiveTime':deviceFddPassiveTime,'deviceInventory':deviceInventory,'agent':agent,'agentFirmware':agentFirmware,'agentMacAddress':agentMacAddress,'agentIpv4Mode':agentIpv4Mode,'agentIpv4Address':agentIpv4Address,'agentIpv4SubnetMask':agentIpv4SubnetMask,'agentIpv4Gateway':agentIpv4Gateway,'agentConfigReset':agentConfigReset,'agentConfigFactoryDefault':agentConfigFactoryDefault,'agentConfigEnableFactoryButton':agentConfigEnableFactoryButton,'agentSecureAddressFlag':agentSecureAddressFlag,'agentStorageMediaCardStatus':agentStorageMediaCardStatus,'agentStorageMediaCardBoot':agentStorageMediaCardBoot,'agentStorageMediaCardMac':agentStorageMediaCardMac,'agentStoreConfigToStorageMediaCard':agentStoreConfigToStorageMediaCard,'agentDhcpConfigRequest':agentDhcpConfigRequest,'port':port,'portCount':portCount,'portStatusTable':portStatusTable,'portStatusTableEntry':portStatusTableEntry,_O:portStatusId,'portStatusType':portStatusType,_b:portStatusLink,'portStatusSpeed':portStatusSpeed,'portStatusDuplex':portStatusDuplex,'portStatusFlowControl':portStatusFlowControl,'portStatusPinout':portStatusPinout,'portStatusFarEndFault':portStatusFarEndFault,'portStatusRxNetload':portStatusRxNetload,'portStatusTxNetload':portStatusTxNetload,'portConfigTable':portConfigTable,'portConfigTableEntry':portConfigTableEntry,_f:portConfigId,'portConfigAlias':portConfigAlias,'portConfigEnable':portConfigEnable,'portConfigAutonego':portConfigAutonego,'portConfigSpeed':portConfigSpeed,'portConfigDuplex':portConfigDuplex,'portConfigFlowControl':portConfigFlowControl,'portConfigPinout':portConfigPinout,'portConfigFarEndFault':portConfigFarEndFault,'portConfigAdvertise':portConfigAdvertise,'portConfigFibreDownDetection':portConfigFibreDownDetection,'vlan':vlan,'vlanSupport':vlanSupport,'vlanEnable':vlanEnable,'vlanForceDefaultVID':vlanForceDefaultVID,'vlanFilterCount':vlanFilterCount,'vlanVoiceVID':vlanVoiceVID,'vlanRstpVID':vlanRstpVID,'vlanUnauthVID':vlanUnauthVID,'vlanPortTable':vlanPortTable,'vlanPortTableEntry':vlanPortTableEntry,_h:vlanPortId,'vlanPortMode':vlanPortMode,'vlanDefaultVID':vlanDefaultVID,'vlanDefaultPriority':vlanDefaultPriority,'vlanPortFlags':vlanPortFlags,'vlanFilterTable':vlanFilterTable,'vlanFilterTableEntry':vlanFilterTableEntry,_i:vlanFilterId,'vlanFilterVID':vlanFilterVID,'vlanFilterAlias':vlanFilterAlias,'vlanFilterEnable':vlanFilterEnable,'vlanMemberManager':vlanMemberManager,'vlanMemberPort1':vlanMemberPort1,'vlanMemberPort2':vlanMemberPort2,'vlanMemberPort3':vlanMemberPort3,'vlanMemberPort4':vlanMemberPort4,'vlanMemberPort5':vlanMemberPort5,'vlanMemberPort6':vlanMemberPort6,'vlanMemberPort7':vlanMemberPort7,'vlanMemberPort8':vlanMemberPort8,'vlanMemberPort9':vlanMemberPort9,'vlanMemberPort10':vlanMemberPort10,'vlanMemberPort11':vlanMemberPort11,'vlanMemberPort12':vlanMemberPort12,'vlanMemberPort13':vlanMemberPort13,'vlanMemberPort14':vlanMemberPort14,'vlanMemberPort15':vlanMemberPort15,'vlanMemberPort16':vlanMemberPort16,'vlanMemberPort17':vlanMemberPort17,'vlanMemberPort18':vlanMemberPort18,'vlanMemberPort19':vlanMemberPort19,'vlanMemberPort20':vlanMemberPort20,'vlanMemberPort21':vlanMemberPort21,'vlanMemberPort22':vlanMemberPort22,'vlanMemberPort23':vlanMemberPort23,'vlanMemberPort24':vlanMemberPort24,'vlanFilterEnhTable':vlanFilterEnhTable,'vlanFilterEnhTableEntry':vlanFilterEnhTableEntry,_j:vlanFilterEnhId,'vlanFilterEnhFlags':vlanFilterEnhFlags,'vlanFilterEnhPriOverride':vlanFilterEnhPriOverride,'prioritization':prioritization,'prioSupport':prioSupport,'prioQueueCount':prioQueueCount,'prioQueueScheme':prioQueueScheme,'prioPortEnable':prioPortEnable,'prioIeeeTagEnable':prioIeeeTagEnable,'prioDiffservEnable':prioDiffservEnable,'prioPortTable':prioPortTable,'prioPortTableEntry':prioPortTableEntry,_k:prioPortId,'prioPortQueue':prioPortQueue,'prioIeeeTagTable':prioIeeeTagTable,'prioIeeeTagTableEntry':prioIeeeTagTableEntry,_l:prioIeeeTagId,'prioIeeeTagQueue':prioIeeeTagQueue,'prioDiffservTable':prioDiffservTable,'prioDiffservTableEntry':prioDiffservTableEntry,_m:prioDiffservId,'prioDiffservQueue':prioDiffservQueue,'monitor':monitor,'monitorSupport':monitorSupport,'monitorMode':monitorMode,'monitorSource':monitorSource,'monitorDestination':monitorDestination,'ring':ring,'ringSupport':ringSupport,'ringCount':ringCount,'ringTable':ringTable,'ringTableEntry':ringTableEntry,_n:ringId,'ringMode':ringMode,'ringPortA':ringPortA,'ringPortB':ringPortB,_c:ringNumber,_AD:ringStatus,_AE:ringAlarmDuration,'couplingred':couplingred,'couplingredSupport':couplingredSupport,'couplingredPort':couplingredPort,'couplingredMode':couplingredMode,'couplingredPartnerIpv4Address':couplingredPartnerIpv4Address,'couplingredStatus':couplingredStatus,'couplingredPartnerStatus':couplingredPartnerStatus,'couplingredValidationFlag':couplingredValidationFlag,'sfp':sfp,'sfpSupport':sfpSupport,'sfpCount':sfpCount,'sfpTable':sfpTable,'sfpTableEntry':sfpTableEntry,'sfpId':sfpId,_AB:sfpPortnumber,_AC:sfpDetect,'sfpVendor':sfpVendor,'sfpVendorPartnumber':sfpVendorPartnumber,'sfpVendorSerialnumber':sfpVendorSerialnumber,'sfpConnector':sfpConnector,'sfpNominalBitrate':sfpNominalBitrate,'sfpDiagnostic':sfpDiagnostic,'sfpTemperature':sfpTemperature,'sfpVoltage':sfpVoltage,'sfpTxBias':sfpTxBias,'sfpTxPower':sfpTxPower,'sfpRxPower':sfpRxPower,'sfpWarnings':sfpWarnings,'sfpAlarms':sfpAlarms,'relais':relais,'relaisSupport':relaisSupport,'relaisCount':relaisCount,'relaisTable':relaisTable,'relaisTableEntry':relaisTableEntry,_r:relaisId,'relaisAlias':relaisAlias,'relaisMode':relaisMode,'relaisStatus':relaisStatus,'portaccessctrl':portaccessctrl,'pacSupport':pacSupport,'pacEnable':pacEnable,'pacUnauthMode':pacUnauthMode,'pacUnauthVID':pacUnauthVID,'pacMaxNumberOfAllowedHostsPerPort':pacMaxNumberOfAllowedHostsPerPort,'pacFallbackRequestEnable':pacFallbackRequestEnable,'pacFallbackRequestTimeout':pacFallbackRequestTimeout,'pacFallbackRejectsEnable':pacFallbackRejectsEnable,'pacFallbackMaxRejects':pacFallbackMaxRejects,'pacSupplicantTimeout':pacSupplicantTimeout,'pacReauthEnable':pacReauthEnable,'pacReauthTime':pacReauthTime,'pacStatusTable':pacStatusTable,'pacStatusTableEntry':pacStatusTableEntry,_s:pacStatPortId,'pacStatPortMode':pacStatPortMode,'pacStatPortStatus':pacStatPortStatus,'pacStatUserStatus1':pacStatUserStatus1,'pacStatUserStatus2':pacStatUserStatus2,'pacStatUserStatus3':pacStatUserStatus3,'pacStatUserStatus4':pacStatUserStatus4,'pacStatUserMac1':pacStatUserMac1,'pacStatUserMac2':pacStatUserMac2,'pacStatUserMac3':pacStatUserMac3,'pacStatUserMac4':pacStatUserMac4,'pacStatUserName1':pacStatUserName1,'pacStatUserName2':pacStatUserName2,'pacStatUserName3':pacStatUserName3,'pacStatUserName4':pacStatUserName4,'pacStatUserIp1':pacStatUserIp1,'pacStatUserIp2':pacStatUserIp2,'pacStatUserIp3':pacStatUserIp3,'pacStatUserIp4':pacStatUserIp4,'pacConfigTable':pacConfigTable,'pacConfigTableEntry':pacConfigTableEntry,_y:pacConfPortId,'pacConfMode':pacConfMode,'pacConfMaxMacCount':pacConfMaxMacCount,'pacMacLockingTable':pacMacLockingTable,'pacMacLockTableEntry':pacMacLockTableEntry,_z:pacMacLockPortId,'pacMacLockEnable1':pacMacLockEnable1,'pacMacLockEnable2':pacMacLockEnable2,'pacMacLockEnable3':pacMacLockEnable3,'pacMacLockEnable4':pacMacLockEnable4,'pacMacLockLearn1':pacMacLockLearn1,'pacMacLockLearn2':pacMacLockLearn2,'pacMacLockLearn3':pacMacLockLearn3,'pacMacLockLearn4':pacMacLockLearn4,'pacLockedMac1':pacLockedMac1,'pacLockedMac2':pacLockedMac2,'pacLockedMac3':pacLockedMac3,'pacLockedMac4':pacLockedMac4,'igmps':igmps,'igmpsSupport':igmpsSupport,'igmpsEnable':igmpsEnable,'igmpsFastLeave':igmpsFastLeave,'igmpsReportAggregation':igmpsReportAggregation,'igmpsFloodingUnregPack':igmpsFloodingUnregPack,'igmpsMaxGroupLimit':igmpsMaxGroupLimit,'igmpsGroupLimit':igmpsGroupLimit,'igmpsGroupNumber':igmpsGroupNumber,'igmpsRouterDetection':igmpsRouterDetection,'igmpsGroupMembershipInterval':igmpsGroupMembershipInterval,'igmpsMaximumResposeTime':igmpsMaximumResposeTime,'igmpsLastMemeberQueryTime':igmpsLastMemeberQueryTime,'igmpsNeighborDeadInterval':igmpsNeighborDeadInterval,'igmpsRouterAgingTime':igmpsRouterAgingTime,'igmpsRxMessageGeneralQuery':igmpsRxMessageGeneralQuery,'igmpsRxMessageSpecificQuery':igmpsRxMessageSpecificQuery,'igmpsRxMessageReport':igmpsRxMessageReport,'igmpsRxMessageLeave':igmpsRxMessageLeave,'igmpsRxMessageAdvertisement':igmpsRxMessageAdvertisement,'igmpsRxMessageTermination':igmpsRxMessageTermination,'igmpsTxMessageSolicitation':igmpsTxMessageSolicitation,'igmpsCounterReset':igmpsCounterReset,'igmpsPortTable':igmpsPortTable,'igmpsPortTableEntry':igmpsPortTableEntry,_A0:igmpsPortId,'igmpsPortSnooping':igmpsPortSnooping,'igmpsPortStaticRouter':igmpsPortStaticRouter,'igmpsPortDynamicRouter':igmpsPortDynamicRouter,'igmpsGroupTable':igmpsGroupTable,'igmpsGroupTableEntry':igmpsGroupTableEntry,_A1:igmpsGroupId,'igmpsGroupMac':igmpsGroupMac,'igmpsGroupVlanId':igmpsGroupVlanId,'igmpsGroupTimestamp':igmpsGroupTimestamp,'igmpsGroupLeaveFlag':igmpsGroupLeaveFlag,'igmpsGroupMemberPort1':igmpsGroupMemberPort1,'igmpsGroupMemberPort2':igmpsGroupMemberPort2,'igmpsGroupMemberPort3':igmpsGroupMemberPort3,'igmpsGroupMemberPort4':igmpsGroupMemberPort4,'igmpsGroupMemberPort5':igmpsGroupMemberPort5,'igmpsGroupMemberPort6':igmpsGroupMemberPort6,'igmpsGroupMemberPort7':igmpsGroupMemberPort7,'igmpsGroupMemberPort8':igmpsGroupMemberPort8,'igmpsGroupMemberPort9':igmpsGroupMemberPort9,'igmpsGroupMemberPort10':igmpsGroupMemberPort10,'igmpsGroupMemberPort11':igmpsGroupMemberPort11,'igmpsGroupMemberPort12':igmpsGroupMemberPort12,'igmpsGroupMemberPort13':igmpsGroupMemberPort13,'igmpsGroupMemberPort14':igmpsGroupMemberPort14,'igmpsGroupMemberPort15':igmpsGroupMemberPort15,'igmpsGroupMemberPort16':igmpsGroupMemberPort16,'igmpsGroupMemberPort17':igmpsGroupMemberPort17,'igmpsGroupMemberPort18':igmpsGroupMemberPort18,'igmpsGroupMemberPort19':igmpsGroupMemberPort19,'igmpsGroupMemberPort20':igmpsGroupMemberPort20,'igmpsGroupMemberPort21':igmpsGroupMemberPort21,'igmpsGroupMemberPort22':igmpsGroupMemberPort22,'igmpsGroupMemberPort23':igmpsGroupMemberPort23,'igmpsGroupMemberPort24':igmpsGroupMemberPort24,'rtc':rtc,'rtcSupport':rtcSupport,'rtcFlags':rtcFlags,'rtcLocalTime':rtcLocalTime,'rtcManualTime':rtcManualTime,'rtcTimeStatus':rtcTimeStatus,'rtcTimezoneOffset':rtcTimezoneOffset,'rtcDSTOffset':rtcDSTOffset,'rtcDSTbegin':rtcDSTbegin,'rtcDSTend':rtcDSTend,'rtcDSTstatus':rtcDSTstatus,'rtcSNTPsyncInterval':rtcSNTPsyncInterval,'rtcSNTPsyncNow':rtcSNTPsyncNow,'rtcSNTPServerCount':rtcSNTPServerCount,'rtcSNTPServerTable':rtcSNTPServerTable,'rtcSNTPServerTableEntry':rtcSNTPServerTableEntry,_A2:rtcSNTPServerId,'rtcSNTPServerStatus':rtcSNTPServerStatus,'rtcSNTPServerEnable':rtcSNTPServerEnable,'rtcSNTPServerIpv4Address':rtcSNTPServerIpv4Address,'consoleinterface':consoleinterface,'consoleSupport':consoleSupport,'consoleEnable':consoleEnable,'consoleTimeout':consoleTimeout,'consoleApplyMode':consoleApplyMode,'consolePrompt':consolePrompt,'webinterface':webinterface,'webSupport':webSupport,'webEnable':webEnable,'snmpinterface':snmpinterface,'snmpSupport':snmpSupport,'snmpEnable':snmpEnable,'snmpApplyMode':snmpApplyMode,'snmpApply':snmpApply,'snmpTrapTest':snmpTrapTest,'snmpTrapDestCount':snmpTrapDestCount,'snmpCommunityRead':snmpCommunityRead,'snmpCommunityWrite':snmpCommunityWrite,'snmpTrapEnable':snmpTrapEnable,'snmpTrapDestTable':snmpTrapDestTable,'snmpTrapDestTableEntry':snmpTrapDestTableEntry,_A6:snmpTrapDestId,'snmpTrapDestAlias':snmpTrapDestAlias,'snmpTrapDestEn':snmpTrapDestEn,'snmpTrapDestIPv4Address':snmpTrapDestIPv4Address,'snmpTrapDestCommunity':snmpTrapDestCommunity,'snmpTrapGenColdstart':snmpTrapGenColdstart,'snmpTrapGenWarmstart':snmpTrapGenWarmstart,'snmpTrapGenLinkDown':snmpTrapGenLinkDown,'snmpTrapGenLinkUp':snmpTrapGenLinkUp,'snmpTrapGenAuthFailure':snmpTrapGenAuthFailure,'snmpTrapGenEgpNeighborLoss':snmpTrapGenEgpNeighborLoss,'snmpTrapEntLinkChange':snmpTrapEntLinkChange,'snmpTrapEntFactoryReset':snmpTrapEntFactoryReset,'snmpTrapEntTemperatureLevelChange':snmpTrapEntTemperatureLevelChange,'snmpTrapEntErrorCounter':snmpTrapEntErrorCounter,'snmpTrapEntUnderOverVoltage':snmpTrapEntUnderOverVoltage,'snmpTrapEntTempShutDown':snmpTrapEntTempShutDown,'snmpTrapEntPoeLimitExceeded':snmpTrapEntPoeLimitExceeded,'snmpTrapEntSupplyStatusChange':snmpTrapEntSupplyStatusChange,'snmpTrapEntSfpPlugChange':snmpTrapEntSfpPlugChange,'snmpTrapEntLoginFailure':snmpTrapEntLoginFailure,'snmpTrapEntRingBroken':snmpTrapEntRingBroken,'snmpTrapEntRingAlarm':snmpTrapEntRingAlarm,'snmpTrapEntAuthPwFail':snmpTrapEntAuthPwFail,'snmpTrapEntPrivPwFail':snmpTrapEntPrivPwFail,'snmpTrapEntAccessPermission':snmpTrapEntAccessPermission,'snmpTrapEntSeclevelFail':snmpTrapEntSeclevelFail,'udpinterface':udpinterface,'udpSupport':udpSupport,'udpEnable':udpEnable,'udpUmacEnable':udpUmacEnable,'syslog':syslog,'syslogSupport':syslogSupport,'syslogEnable':syslogEnable,'syslogMessageTest':syslogMessageTest,'syslogDestCount':syslogDestCount,'syslogDestTable':syslogDestTable,'syslogDestTableEntry':syslogDestTableEntry,_A7:syslogDestId,'syslogDestAlias':syslogDestAlias,'syslogDestEnable':syslogDestEnable,'syslogDestIpv4Address':syslogDestIpv4Address,'syslogDestPort':syslogDestPort,'syslogDestFacility':syslogDestFacility,'syslogDestEventFilter':syslogDestEventFilter,'radius':radius,'radiusSupport':radiusSupport,'radiusAccessEnable':radiusAccessEnable,'radiusAccountEnable':radiusAccountEnable,'radiusServerCount':radiusServerCount,'radiusMacAuthPassword':radiusMacAuthPassword,'radiusUseMacAsPassword':radiusUseMacAsPassword,'radiusMacSeparator':radiusMacSeparator,'radiusTimeout':radiusTimeout,'radiusMacLettercase':radiusMacLettercase,'radiusServerTable':radiusServerTable,'radiusServerTableEntry':radiusServerTableEntry,_A8:radiusServerId,'radiusServerAlias':radiusServerAlias,'radiusServerEnableAccess':radiusServerEnableAccess,'radiusServerEnableAccount':radiusServerEnableAccount,'radiusServerIpv4Address':radiusServerIpv4Address,'radiusServerAccessPort':radiusServerAccessPort,'radiusServerAccountPort':radiusServerAccountPort,'radiusServerSecret':radiusServerSecret,'supply':supply,'supplyCount':supplyCount,'supplyTable':supplyTable,'supplyTableEntry':supplyTableEntry,_a:supplyId,'supplyUsed':supplyUsed,'supplyStatus':supplyStatus,'poepse':poepse,'poepseSupport':poepseSupport,'poepseEnable':poepseEnable,'poepseTotalInputPower':poepseTotalInputPower,'poepseMaxInputPower':poepseMaxInputPower,'poepseDeviceSupplyPower':poepseDeviceSupplyPower,'pseAvailablePower':pseAvailablePower,'poepseExtendedVoltage':poepseExtendedVoltage,'poepsePortTable':poepsePortTable,'poepsePortTableEntry':poepsePortTableEntry,_A9:poepsePortId,'poepsePortMode':poepsePortMode,'poepsePortStatus':poepsePortStatus,'poepsePortMaxPower':poepsePortMaxPower,'poepsePortMeasuredPower':poepsePortMeasuredPower,'poepsePortMaxClass':poepsePortMaxClass,'poepsePortDetectedClass':poepsePortDetectedClass,'poepsePortMeasuredVoltage':poepsePortMeasuredVoltage,'poepd':poepd,'poepdSupport':poepdSupport,'hardwarecode':hardwarecode,'hardwarecodeSupport':hardwarecodeSupport,'hardwarecodeNumber':hardwarecodeNumber,'spanningtree':spanningtree,'stpSupport':stpSupport,'stpEnable':stpEnable,'msSwitchNotifications':msSwitchNotifications,'linkChangeNotification':linkChangeNotification,'factoryResetNotification':factoryResetNotification,'temperatureLevelChangeNotification':temperatureLevelChangeNotification,'errorcountNotification':errorcountNotification,'underOverVoltageNotification':underOverVoltageNotification,'temperatureShutdownNotification':temperatureShutdownNotification,'portPoELimitExceededNotification':portPoELimitExceededNotification,'powerSupplyStatusChangeNotification':powerSupplyStatusChangeNotification,'sfpPlugChangeNotification':sfpPlugChangeNotification,'loginFailureNotification':loginFailureNotification,'ringBrokenNotification':ringBrokenNotification,'ringAlarmNotification':ringAlarmNotification,'snmpv3AuthenticationPwFailNotification':snmpv3AuthenticationPwFailNotification,'snmpv3PrivacyPwFailNotification':snmpv3PrivacyPwFailNotification,'snmpv3AccessPermissionNotification':snmpv3AccessPermissionNotification,'snmpv3SeclevelFailNotification':snmpv3SeclevelFailNotification})