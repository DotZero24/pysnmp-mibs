_Av='cmmFanRpmMax'
_Au='cmmFanRpmMin'
_At='cmmStackUnitCpuUtilCriticalThreshold'
_As='cmmStackUnitCpuUtilAlertThreshold'
_Ar='accessible-for-notify'
_Aq='cmmSysCpldIndex'
_Ap='cmmCpuCoreIndex'
_Ao='cmmSwitchTemperatureSensorIndex'
_An='dc-reverse'
_Am='dc-normal'
_Al='ac-reverse'
_Ak='ac-normal'
_Aj='unsupported'
_Ai='supported'
_Ah='tx-disable'
_Ag='fcs-100mbps'
_Af='fcs-200mbps'
_Ae='fcs-400mbps'
_Ad='fcs-800mbps'
_Ac='fcs-1200mbps'
_Ab='fcs-1600mbps'
_Aa='fcs-3200mbps'
_AZ='vendor-specific'
_AY='DisplayString'
_AX='cmmTransVendorSerialNumber'
_AW='cmmTransVendorName'
_AV='cmmTransTxPowerAlertThresholdMax'
_AU='cmmTransTxPowerAlertThresholdMin'
_AT='cmmTransTxPowerCriticalThresholdMax'
_AS='cmmTransTxPowerCriticalThresholdMin'
_AR='cmmTransRxPowerAlertThresholdMax'
_AQ='cmmTransRxPowerAlertThresholdMin'
_AP='cmmTransRxPowerCriticalThresholdMax'
_AO='cmmTransRxPowerCriticalThresholdMin'
_AN='cmmTransLaserBiasCurrAlertThresholdMax'
_AM='cmmTransLaserBiasCurrAlertThresholdMin'
_AL='cmmTransLaserBiasCurrCriticalThresholdMax'
_AK='cmmTransLaserBiasCurrCriticalThresholdMin'
_AJ='cmmTransVoltAlertThresholdMax'
_AI='cmmTransVoltAlertThresholdMin'
_AH='cmmTransVoltCriticalThresholdMax'
_AG='cmmTransVoltCriticalThresholdMin'
_AF='cmmTransTempAlertThresholdMax'
_AE='cmmTransTempAlertThresholdMin'
_AD='cmmTransTempCriticalThresholdMax'
_AC='cmmTransTempCriticalThresholdMin'
_AB='cmmFanSerialNumber'
_AA='cmmPsuSerialNumber'
_A9='cmmSysPowerSupplyOperStatus'
_A8='cmmSysTempEmergencyThresholdMax'
_A7='cmmSysTempEmergencyThresholdMin'
_A6='cmmSysHarddiskCriticalThreshold'
_A5='cmmSysHarddiskAlertThreshold'
_A4='cmmSysRamCriticalThreshold'
_A3='cmmSysRamAlertThreshold'
_A2='cmmStackCpuLoad1minCriticalThreshold'
_A1='cmmStackCpuLoad1minAlertThreshold'
_A0='cmmStackUnitCpuLoad5Min'
_z='cmmStackCpuLoad5minCriticalThreshold'
_y='cmmStackUnitCpuLoad15Min'
_x='cmmStackCpuLoad15minCriticalThreshold'
_w='not-applicable'
_v='disable'
_u='enable'
_t='10 m'
_s='reserved'
_r='cmmSysTempCriticalThresholdMax'
_q='cmmSysTempCriticalThresholdMin'
_p='cmmSysTempAlertThresholdMax'
_o='cmmSysTempAlertThresholdMin'
_n='cmmSysHarddiskUsedMem'
_m='cmmSysRamUsedMem'
_l='cmmStackUnitCpuUtilization'
_k='cmmStackUnitCpuLoad1Min'
_j='0.001 mA'
_i='0.001 V'
_h='not-accessible'
_g='cmmTransTxPower'
_f='cmmTransRxPower'
_e='cmmTransLaserBiasCurrent'
_d='cmmTransVoltage'
_c='cmmTransTemperature'
_b='notpresent'
_a='OctetString'
_Z='major-fault'
_Y='minor-fault'
_X='cmmFanIndex'
_W=' % '
_V='cmmSysPSUIndex'
_U='normal'
_T='0.001 dBm'
_S='cmmSysTemperatureSensorName'
_R='cmmSysTemperatureValue'
_Q='0.01 %'
_P='cmmSysTemperatureSensorIndex'
_O='cmmFanTrayNumber'
_N='Bits'
_M='0.01 C'
_L='cmmTransChannelIndex'
_K='fail'
_J='good'
_I='notapplicable'
_H='cmmTransType'
_G='cmmTransIndex'
_F='unknown'
_E='Integer32'
_D='cmmStackUnitIndex'
_C='read-only'
_B='CMM-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_AY,'MacAddress','PhysAddress','RowStatus','TextualConvention')
cmm=ModuleIdentity((1,3,6,1,4,1,36673,100))
class LedColorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,30)));namedValues=NamedValues(*(('none',1),('green',2),('blinking-green',3),('solid-green',4),('amber',5),('blinking-amber',6),('solid-amber',7),('red',8),('blinking-red',9),('solid-red',10),('blue',11),('blinking-blue',12),('yellow',13),('blinking-yellow',14),('orange',15),('slow-blinking-green',16),('fast-blinking-green',17),(_F,30)))
class SystemStatusCode(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('cpu',0),('ram',1),('disk',2),('low-temperature',3),('high-temperature',4),('fan',5),('power',6),('software',7)))
_CmmChassisObject_ObjectIdentity=ObjectIdentity
CmmChassisObject=_CmmChassisObject_ObjectIdentity((1,3,6,1,4,1,36673,100,1))
_CmmObjects_ObjectIdentity=ObjectIdentity
cmmObjects=_CmmObjects_ObjectIdentity((1,3,6,1,4,1,36673,100,1,1))
_CmmNumStackUnits_Type=Integer32
_CmmNumStackUnits_Object=MibScalar
cmmNumStackUnits=_CmmNumStackUnits_Object((1,3,6,1,4,1,36673,100,1,1,1),_CmmNumStackUnits_Type())
cmmNumStackUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmNumStackUnits.setStatus(_A)
_CmmSysObjects_ObjectIdentity=ObjectIdentity
cmmSysObjects=_CmmSysObjects_ObjectIdentity((1,3,6,1,4,1,36673,100,1,2))
_CmmStackUnitTable_Object=MibTable
cmmStackUnitTable=_CmmStackUnitTable_Object((1,3,6,1,4,1,36673,100,1,2,1))
if mibBuilder.loadTexts:cmmStackUnitTable.setStatus(_A)
_CmmStackUnitEntry_Object=MibTableRow
cmmStackUnitEntry=_CmmStackUnitEntry_Object((1,3,6,1,4,1,36673,100,1,2,1,1))
cmmStackUnitEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmStackUnitEntry.setStatus(_A)
_CmmStackUnitIndex_Type=Integer32
_CmmStackUnitIndex_Object=MibTableColumn
cmmStackUnitIndex=_CmmStackUnitIndex_Object((1,3,6,1,4,1,36673,100,1,2,1,1,1),_CmmStackUnitIndex_Type())
cmmStackUnitIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:cmmStackUnitIndex.setStatus(_A)
_CmmStackUnitModelName_Type=DisplayString
_CmmStackUnitModelName_Object=MibTableColumn
cmmStackUnitModelName=_CmmStackUnitModelName_Object((1,3,6,1,4,1,36673,100,1,2,1,1,2),_CmmStackUnitModelName_Type())
cmmStackUnitModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitModelName.setStatus(_A)
_CmmStackUnitSerialNumber_Type=DisplayString
_CmmStackUnitSerialNumber_Object=MibTableColumn
cmmStackUnitSerialNumber=_CmmStackUnitSerialNumber_Object((1,3,6,1,4,1,36673,100,1,2,1,1,3),_CmmStackUnitSerialNumber_Type())
cmmStackUnitSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitSerialNumber.setStatus(_A)
_CmmStackUnitUpTime_Type=TimeTicks
_CmmStackUnitUpTime_Object=MibTableColumn
cmmStackUnitUpTime=_CmmStackUnitUpTime_Object((1,3,6,1,4,1,36673,100,1,2,1,1,4),_CmmStackUnitUpTime_Type())
cmmStackUnitUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitUpTime.setStatus(_A)
_CmmStackUnitMfgDate_Type=DateAndTime
_CmmStackUnitMfgDate_Object=MibTableColumn
cmmStackUnitMfgDate=_CmmStackUnitMfgDate_Object((1,3,6,1,4,1,36673,100,1,2,1,1,5),_CmmStackUnitMfgDate_Type())
cmmStackUnitMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitMfgDate.setStatus(_A)
_CmmStackUnitMacAddress_Type=MacAddress
_CmmStackUnitMacAddress_Object=MibTableColumn
cmmStackUnitMacAddress=_CmmStackUnitMacAddress_Object((1,3,6,1,4,1,36673,100,1,2,1,1,6),_CmmStackUnitMacAddress_Type())
cmmStackUnitMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitMacAddress.setStatus(_A)
_CmmStackUnitPartNum_Type=DisplayString
_CmmStackUnitPartNum_Object=MibTableColumn
cmmStackUnitPartNum=_CmmStackUnitPartNum_Object((1,3,6,1,4,1,36673,100,1,2,1,1,7),_CmmStackUnitPartNum_Type())
cmmStackUnitPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitPartNum.setStatus(_A)
_CmmStackLabelRevision_Type=DisplayString
_CmmStackLabelRevision_Object=MibTableColumn
cmmStackLabelRevision=_CmmStackLabelRevision_Object((1,3,6,1,4,1,36673,100,1,2,1,1,8),_CmmStackLabelRevision_Type())
cmmStackLabelRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackLabelRevision.setStatus(_A)
class _CmmStackUnitCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CmmStackUnitCountryCode_Type.__name__=_a
_CmmStackUnitCountryCode_Object=MibTableColumn
cmmStackUnitCountryCode=_CmmStackUnitCountryCode_Object((1,3,6,1,4,1,36673,100,1,2,1,1,9),_CmmStackUnitCountryCode_Type())
cmmStackUnitCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCountryCode.setStatus(_A)
class _CmmStackUnitServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_CmmStackUnitServiceTag_Type.__name__=_AY
_CmmStackUnitServiceTag_Object=MibTableColumn
cmmStackUnitServiceTag=_CmmStackUnitServiceTag_Object((1,3,6,1,4,1,36673,100,1,2,1,1,10),_CmmStackUnitServiceTag_Type())
cmmStackUnitServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitServiceTag.setStatus(_A)
_CmmStackPlatformName_Type=DisplayString
_CmmStackPlatformName_Object=MibTableColumn
cmmStackPlatformName=_CmmStackPlatformName_Object((1,3,6,1,4,1,36673,100,1,2,1,1,11),_CmmStackPlatformName_Type())
cmmStackPlatformName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackPlatformName.setStatus(_A)
_CmmStackOnieVersion_Type=DisplayString
_CmmStackOnieVersion_Object=MibTableColumn
cmmStackOnieVersion=_CmmStackOnieVersion_Object((1,3,6,1,4,1,36673,100,1,2,1,1,12),_CmmStackOnieVersion_Type())
cmmStackOnieVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackOnieVersion.setStatus(_A)
_CmmStackMfgName_Type=DisplayString
_CmmStackMfgName_Object=MibTableColumn
cmmStackMfgName=_CmmStackMfgName_Object((1,3,6,1,4,1,36673,100,1,2,1,1,13),_CmmStackMfgName_Type())
cmmStackMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackMfgName.setStatus(_A)
_CmmStackVendorName_Type=DisplayString
_CmmStackVendorName_Object=MibTableColumn
cmmStackVendorName=_CmmStackVendorName_Object((1,3,6,1,4,1,36673,100,1,2,1,1,14),_CmmStackVendorName_Type())
cmmStackVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackVendorName.setStatus(_A)
_CmmStackDiagVersion_Type=DisplayString
_CmmStackDiagVersion_Object=MibTableColumn
cmmStackDiagVersion=_CmmStackDiagVersion_Object((1,3,6,1,4,1,36673,100,1,2,1,1,15),_CmmStackDiagVersion_Type())
cmmStackDiagVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackDiagVersion.setStatus(_A)
class _CmmStackCrc32_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CmmStackCrc32_Type.__name__=_a
_CmmStackCrc32_Object=MibTableColumn
cmmStackCrc32=_CmmStackCrc32_Object((1,3,6,1,4,1,36673,100,1,2,1,1,16),_CmmStackCrc32_Type())
cmmStackCrc32.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackCrc32.setStatus(_A)
_CmmStackUnitNumFanControllers_Type=Integer32
_CmmStackUnitNumFanControllers_Object=MibTableColumn
cmmStackUnitNumFanControllers=_CmmStackUnitNumFanControllers_Object((1,3,6,1,4,1,36673,100,1,2,1,1,17),_CmmStackUnitNumFanControllers_Type())
cmmStackUnitNumFanControllers.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumFanControllers.setStatus(_A)
_CmmStackUnitNumFanTrays_Type=Integer32
_CmmStackUnitNumFanTrays_Object=MibTableColumn
cmmStackUnitNumFanTrays=_CmmStackUnitNumFanTrays_Object((1,3,6,1,4,1,36673,100,1,2,1,1,18),_CmmStackUnitNumFanTrays_Type())
cmmStackUnitNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumFanTrays.setStatus(_A)
_CmmStackUnitNumPowerSupplies_Type=Integer32
_CmmStackUnitNumPowerSupplies_Object=MibTableColumn
cmmStackUnitNumPowerSupplies=_CmmStackUnitNumPowerSupplies_Object((1,3,6,1,4,1,36673,100,1,2,1,1,19),_CmmStackUnitNumPowerSupplies_Type())
cmmStackUnitNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumPowerSupplies.setStatus(_A)
_CmmStackUnitNumPluggableModules_Type=Integer32
_CmmStackUnitNumPluggableModules_Object=MibTableColumn
cmmStackUnitNumPluggableModules=_CmmStackUnitNumPluggableModules_Object((1,3,6,1,4,1,36673,100,1,2,1,1,20),_CmmStackUnitNumPluggableModules_Type())
cmmStackUnitNumPluggableModules.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumPluggableModules.setStatus(_A)
_CmmStackUnitNumFastEtherPorts_Type=Integer32
_CmmStackUnitNumFastEtherPorts_Object=MibTableColumn
cmmStackUnitNumFastEtherPorts=_CmmStackUnitNumFastEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,21),_CmmStackUnitNumFastEtherPorts_Type())
cmmStackUnitNumFastEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumFastEtherPorts.setStatus(_A)
_CmmStackUnitNumGigEtherPorts_Type=Integer32
_CmmStackUnitNumGigEtherPorts_Object=MibTableColumn
cmmStackUnitNumGigEtherPorts=_CmmStackUnitNumGigEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,22),_CmmStackUnitNumGigEtherPorts_Type())
cmmStackUnitNumGigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumGigEtherPorts.setStatus(_A)
_CmmStackUnitNum10GigEtherPorts_Type=Integer32
_CmmStackUnitNum10GigEtherPorts_Object=MibTableColumn
cmmStackUnitNum10GigEtherPorts=_CmmStackUnitNum10GigEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,23),_CmmStackUnitNum10GigEtherPorts_Type())
cmmStackUnitNum10GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNum10GigEtherPorts.setStatus(_A)
_CmmStackUnitNum25GigEtherPorts_Type=Integer32
_CmmStackUnitNum25GigEtherPorts_Object=MibTableColumn
cmmStackUnitNum25GigEtherPorts=_CmmStackUnitNum25GigEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,24),_CmmStackUnitNum25GigEtherPorts_Type())
cmmStackUnitNum25GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNum25GigEtherPorts.setStatus(_A)
_CmmStackUnitNum40GigEtherPorts_Type=Integer32
_CmmStackUnitNum40GigEtherPorts_Object=MibTableColumn
cmmStackUnitNum40GigEtherPorts=_CmmStackUnitNum40GigEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,25),_CmmStackUnitNum40GigEtherPorts_Type())
cmmStackUnitNum40GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNum40GigEtherPorts.setStatus(_A)
_CmmStackUnitNum50GigEtherPorts_Type=Integer32
_CmmStackUnitNum50GigEtherPorts_Object=MibTableColumn
cmmStackUnitNum50GigEtherPorts=_CmmStackUnitNum50GigEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,26),_CmmStackUnitNum50GigEtherPorts_Type())
cmmStackUnitNum50GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNum50GigEtherPorts.setStatus(_A)
_CmmStackUnitNum100GigEtherPorts_Type=Integer32
_CmmStackUnitNum100GigEtherPorts_Object=MibTableColumn
cmmStackUnitNum100GigEtherPorts=_CmmStackUnitNum100GigEtherPorts_Object((1,3,6,1,4,1,36673,100,1,2,1,1,27),_CmmStackUnitNum100GigEtherPorts_Type())
cmmStackUnitNum100GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNum100GigEtherPorts.setStatus(_A)
_CmmStackUnitSwitchChipRev_Type=DisplayString
_CmmStackUnitSwitchChipRev_Object=MibTableColumn
cmmStackUnitSwitchChipRev=_CmmStackUnitSwitchChipRev_Object((1,3,6,1,4,1,36673,100,1,2,1,1,28),_CmmStackUnitSwitchChipRev_Type())
cmmStackUnitSwitchChipRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitSwitchChipRev.setStatus(_A)
_CmmStackSupportedLabelRevision_Type=DisplayString
_CmmStackSupportedLabelRevision_Object=MibTableColumn
cmmStackSupportedLabelRevision=_CmmStackSupportedLabelRevision_Object((1,3,6,1,4,1,36673,100,1,2,1,1,29),_CmmStackSupportedLabelRevision_Type())
cmmStackSupportedLabelRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackSupportedLabelRevision.setStatus(_A)
_CmmStackUnitSupportedSwitchChipRev_Type=DisplayString
_CmmStackUnitSupportedSwitchChipRev_Object=MibTableColumn
cmmStackUnitSupportedSwitchChipRev=_CmmStackUnitSupportedSwitchChipRev_Object((1,3,6,1,4,1,36673,100,1,2,1,1,30),_CmmStackUnitSupportedSwitchChipRev_Type())
cmmStackUnitSupportedSwitchChipRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitSupportedSwitchChipRev.setStatus(_A)
_CmmTransEEPROMTable_Object=MibTable
cmmTransEEPROMTable=_CmmTransEEPROMTable_Object((1,3,6,1,4,1,36673,100,1,2,2))
if mibBuilder.loadTexts:cmmTransEEPROMTable.setStatus(_A)
_CmmTransEEPROMEntry_Object=MibTableRow
cmmTransEEPROMEntry=_CmmTransEEPROMEntry_Object((1,3,6,1,4,1,36673,100,1,2,2,1))
cmmTransEEPROMEntry.setIndexNames((0,_B,_D),(0,_B,_G))
if mibBuilder.loadTexts:cmmTransEEPROMEntry.setStatus(_A)
_CmmTransIndex_Type=Integer32
_CmmTransIndex_Object=MibTableColumn
cmmTransIndex=_CmmTransIndex_Object((1,3,6,1,4,1,36673,100,1,2,2,1,1),_CmmTransIndex_Type())
cmmTransIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:cmmTransIndex.setStatus(_A)
class _CmmTransType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sfp',1),('qsfp',2),(_F,3)))
_CmmTransType_Type.__name__=_E
_CmmTransType_Object=MibTableColumn
cmmTransType=_CmmTransType_Object((1,3,6,1,4,1,36673,100,1,2,2,1,2),_CmmTransType_Type())
cmmTransType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransType.setStatus(_A)
_CmmTransNoOfChannels_Type=Integer32
_CmmTransNoOfChannels_Object=MibTableColumn
cmmTransNoOfChannels=_CmmTransNoOfChannels_Object((1,3,6,1,4,1,36673,100,1,2,2,1,3),_CmmTransNoOfChannels_Type())
cmmTransNoOfChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransNoOfChannels.setStatus(_A)
class _CmmTransidentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_F,1),('gbic',2),('soldered-to-motherboard',3),('sfp-or-sfpplus-or-sfp28',4),('xbi-300pin',5),('xenpak',6),('xep',7),('xff',8),('xfpe',9),('xpak',10),('x2',11),('dwdmsfp-or-dwdmsfpplus',12),('qsfp',13),('qsfpplus-or-later',14),('cxp-or-later',15),('shielded-mini-multilane-hd4x',16),('shielded-mini-multilane-hd8x',17),('qsfp28-or-later',18),('cxp2-aka-cxp28-or-later',19),('cdfpstyle1-or-cdfpstyle2',20),('shielded-mini-multilane-hd4x-fanoutcable',21),('shielded-mini-multilane-hd8x-fanoutcable',22),('cdfpstyle3',23),('microqsfp',24),('qsfp-doubledensity-8x-pluggable-transceiver',25),(_s,26),(_AZ,27)))
_CmmTransidentifier_Type.__name__=_E
_CmmTransidentifier_Object=MibTableColumn
cmmTransidentifier=_CmmTransidentifier_Object((1,3,6,1,4,1,36673,100,1,2,2,1,4),_CmmTransidentifier_Type())
cmmTransidentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransidentifier.setStatus(_A)
class _CmmTransSFPextendedidentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('gbic-notspecified-or-compliant-with-moddef',1),('gbic-compliant-with-moddef1',2),('gbic-compliant-with-moddef2',3),('gbic-compliant-with-moddef3',4),('gbic-or-sfp-definedby-twowire-interfaceid-only',5),('gbic-compliant-with-moddef5',6),('gbic-compliant-with-moddef6',7),('gbic-compliant-with-moddef7',8),('unallocated',9),(_F,10)))
_CmmTransSFPextendedidentifier_Type.__name__=_E
_CmmTransSFPextendedidentifier_Object=MibTableColumn
cmmTransSFPextendedidentifier=_CmmTransSFPextendedidentifier_Object((1,3,6,1,4,1,36673,100,1,2,2,1,5),_CmmTransSFPextendedidentifier_Type())
cmmTransSFPextendedidentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSFPextendedidentifier.setStatus(_A)
class _CmmTransQSFPextendedidentifier_Type(Bits):namedValues=NamedValues(*(('powerclass1-1dot5wmax',0),('powerclass2-2wmax',1),('powerclass3-2dot5wmax',2),('powerclass4-3dot5wmax',3),('cleicode-present',4),('cdrpresent-in-tx',5),('cdrpresent-in-rx',6),('powerclass5-4wmax',7),('powerclass6-4dot5wmax',8),('powerclass7-5wmax',9)))
_CmmTransQSFPextendedidentifier_Type.__name__=_N
_CmmTransQSFPextendedidentifier_Object=MibTableColumn
cmmTransQSFPextendedidentifier=_CmmTransQSFPextendedidentifier_Object((1,3,6,1,4,1,36673,100,1,2,2,1,6),_CmmTransQSFPextendedidentifier_Type())
cmmTransQSFPextendedidentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransQSFPextendedidentifier.setStatus(_A)
class _CmmTransconnectortype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_F,1),('subscriber-connector',2),('fibrechannel-style1-copperconnector',3),('fibrechannel-style2-copperconnector',4),('bayonet-or-threaded-neill-concelman',5),('fibrechannel-coaxheaders',6),('fiber-jack',7),('lucent-connector',8),('mechanical-transfer-registeredjack',9),('multiple-optical',10),('sg',11),('optical-pigtail',12),('multifiber-paralleloptic-1x12',13),('multifiber-paralleloptic-1x16',14),('hssdcii',16),('copper-pigtail',17),('rj45',18),('no-separable-connector',19),('mxc2-x16',20),(_s,21),(_AZ,22)))
_CmmTransconnectortype_Type.__name__=_E
_CmmTransconnectortype_Object=MibTableColumn
cmmTransconnectortype=_CmmTransconnectortype_Object((1,3,6,1,4,1,36673,100,1,2,2,1,7),_CmmTransconnectortype_Type())
cmmTransconnectortype.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransconnectortype.setStatus(_A)
class _CmmTransEthCompliance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('ec-unknown',1),('ec-10gbase-sr',2),('ec-10gbase-lr',3),('ec-10gbase-lrm',4),('ec-10gbase-er',5),('ec-1000base-sx',6),('ec-1000base-lx',7),('ec-1000base-cx',8),('ec-1000base-t',9),('ec-100base-lx-or-lx10',10),('ec-100base-fx',11),('ec-base-bx10',12),('ec-base-px',13),('ec-40gbase-cr4',14),('ec-40gbase-sr4',15),('ec-40gbase-lr4',16),('ec-40g-activecable',17)))
_CmmTransEthCompliance_Type.__name__=_E
_CmmTransEthCompliance_Object=MibTableColumn
cmmTransEthCompliance=_CmmTransEthCompliance_Object((1,3,6,1,4,1,36673,100,1,2,2,1,8),_CmmTransEthCompliance_Type())
cmmTransEthCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransEthCompliance.setStatus(_A)
class _CmmTransExtEthCompliance_Type(Bits):namedValues=NamedValues(*(('eec-unspecified',0),('eec-100g-activeopticalcable-or-25g-auic2maoc',1),('eec-100gbase-sr4-or-25gbase-sr',2),('eec-100gbase-lr4-or-25gbase-lr',3),('eec-100gbase-er4-or-25gbase-er',4),('eec-100gbase-sr10',5),('eec-100g-cwdm4',6),('eec-100g-psm4-parallelsmf',7),('eec-100g-activecoppercable-or-25g-auic2macc',8),('eec-obsolete',9),('eec-reserved',10),('eec-100gbase-cr4-or-25gbase-crca-l',11),('eec-25gbase-crca-s',12),('eec-25gbase-crca-n',13),('eec-40gbase-er4',14),('eec-4x10gbase-sr',15),('eec-40g-psm4-parallelsmf',16),('eec-g959-dot1-profilep1-i1-2d1',17),('eec-g959-dot1-profilep1-s1-2d2',18),('eec-g959-dot1-profilep1-l1-2d2',19),('eec-100gbase-t-with-sfi-electricalinterface',20),('eec-100g-clr4',21),('eec-100g-aoc-or-25g-auic2maoc',22),('eec-100g-acc-or-25g-auic2macc',23),('eec-100ge-dwdm2',24)))
_CmmTransExtEthCompliance_Type.__name__=_N
_CmmTransExtEthCompliance_Object=MibTableColumn
cmmTransExtEthCompliance=_CmmTransExtEthCompliance_Object((1,3,6,1,4,1,36673,100,1,2,2,1,9),_CmmTransExtEthCompliance_Type())
cmmTransExtEthCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransExtEthCompliance.setStatus(_A)
class _CmmTransSonetCompliance_Type(Bits):namedValues=NamedValues(*(('oc192-shortreach',0),('sonet-reachspecifier-bit1',1),('sonet-reachspecifier-bit2',2),('oc48-longreach',3),('oc48-intermediatereach',4),('oc48-shortreach',5),('oc12-singlemode-longreach',6),('oc12-singlemode-intermediatereach',7),('oc12-singlemode-shortreach',8),('oc3-singlemode-longreach',9),('oc3-singlemode-intermediatereach',10),('oc3-singlemode-shortreach',11)))
_CmmTransSonetCompliance_Type.__name__=_N
_CmmTransSonetCompliance_Object=MibTableColumn
cmmTransSonetCompliance=_CmmTransSonetCompliance_Object((1,3,6,1,4,1,36673,100,1,2,2,1,10),_CmmTransSonetCompliance_Type())
cmmTransSonetCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSonetCompliance.setStatus(_A)
class _CmmTransFiberChnlLinkLen_Type(Bits):namedValues=NamedValues(*(('short',0),('medium',1),('intermediate',2),('long',3),('verylong',4)))
_CmmTransFiberChnlLinkLen_Type.__name__=_N
_CmmTransFiberChnlLinkLen_Object=MibTableColumn
cmmTransFiberChnlLinkLen=_CmmTransFiberChnlLinkLen_Object((1,3,6,1,4,1,36673,100,1,2,2,1,11),_CmmTransFiberChnlLinkLen_Type())
cmmTransFiberChnlLinkLen.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransFiberChnlLinkLen.setStatus(_A)
class _CmmTransFiberChnlTransTech_Type(Bits):namedValues=NamedValues(*(('shortwaveLaserLinearRx',0),('longwaveLaserLC',1),('electricalInter-Enclosure',2),('electricalIntra-Enclosure',3),('shortwaveLaserWithOutOFC',4),('shortwaveLaserwithOFC',5),('longwaveLaserLL',6)))
_CmmTransFiberChnlTransTech_Type.__name__=_N
_CmmTransFiberChnlTransTech_Object=MibTableColumn
cmmTransFiberChnlTransTech=_CmmTransFiberChnlTransTech_Object((1,3,6,1,4,1,36673,100,1,2,2,1,12),_CmmTransFiberChnlTransTech_Type())
cmmTransFiberChnlTransTech.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransFiberChnlTransTech.setStatus(_A)
class _CmmTransFiberChnlTransMedia_Type(Bits):namedValues=NamedValues(*(('twinaxial-pair',0),('twisted-pair',1),('miniature-coax',2),('video-coax',3),('multi-mode62dot5m',4),('multi-mode50m',5),('multi-mode50um',6),('single-mode',7)))
_CmmTransFiberChnlTransMedia_Type.__name__=_N
_CmmTransFiberChnlTransMedia_Object=MibTableColumn
cmmTransFiberChnlTransMedia=_CmmTransFiberChnlTransMedia_Object((1,3,6,1,4,1,36673,100,1,2,2,1,13),_CmmTransFiberChnlTransMedia_Type())
cmmTransFiberChnlTransMedia.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransFiberChnlTransMedia.setStatus(_A)
class _CmmTransSFPFiberChnlSpeed_Type(Bits):namedValues=NamedValues(*((_Aa,0),(_Ab,1),(_Ac,2),(_Ad,3),(_Ae,4),(_Af,5),(_Ag,6)))
_CmmTransSFPFiberChnlSpeed_Type.__name__=_N
_CmmTransSFPFiberChnlSpeed_Object=MibTableColumn
cmmTransSFPFiberChnlSpeed=_CmmTransSFPFiberChnlSpeed_Object((1,3,6,1,4,1,36673,100,1,2,2,1,14),_CmmTransSFPFiberChnlSpeed_Type())
cmmTransSFPFiberChnlSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSFPFiberChnlSpeed.setStatus(_A)
class _CmmTransQSFPFiberChnlSpeed_Type(Bits):namedValues=NamedValues(*((_Aa,0),(_Ab,1),(_Ac,2),(_Ad,3),(_Ae,4),(_Af,5),(_Ag,6)))
_CmmTransQSFPFiberChnlSpeed_Type.__name__=_N
_CmmTransQSFPFiberChnlSpeed_Object=MibTableColumn
cmmTransQSFPFiberChnlSpeed=_CmmTransQSFPFiberChnlSpeed_Object((1,3,6,1,4,1,36673,100,1,2,2,1,15),_CmmTransQSFPFiberChnlSpeed_Type())
cmmTransQSFPFiberChnlSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransQSFPFiberChnlSpeed.setStatus(_A)
class _CmmTransSFPInfiniBandCompliance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ibc-1xsx',1),('ibc-1xlx',2),('ibc-1xcopperactive',3),('ibc-1xcopperpassive',4),('ibc-unknown',5),('ibc-notapplicable',6)))
_CmmTransSFPInfiniBandCompliance_Type.__name__=_E
_CmmTransSFPInfiniBandCompliance_Object=MibTableColumn
cmmTransSFPInfiniBandCompliance=_CmmTransSFPInfiniBandCompliance_Object((1,3,6,1,4,1,36673,100,1,2,2,1,16),_CmmTransSFPInfiniBandCompliance_Type())
cmmTransSFPInfiniBandCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSFPInfiniBandCompliance.setStatus(_A)
class _CmmTransSFPEsconCompliance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('escon-mmf-1310nm-led',1),('escon-smf-1310nm-laser',2),(_F,3),(_I,4)))
_CmmTransSFPEsconCompliance_Type.__name__=_E
_CmmTransSFPEsconCompliance_Object=MibTableColumn
cmmTransSFPEsconCompliance=_CmmTransSFPEsconCompliance_Object((1,3,6,1,4,1,36673,100,1,2,2,1,17),_CmmTransSFPEsconCompliance_Type())
cmmTransSFPEsconCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSFPEsconCompliance.setStatus(_A)
class _CmmTransSfpPlusCableTech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('passive',2),(_F,3),(_I,4)))
_CmmTransSfpPlusCableTech_Type.__name__=_E
_CmmTransSfpPlusCableTech_Object=MibTableColumn
cmmTransSfpPlusCableTech=_CmmTransSfpPlusCableTech_Object((1,3,6,1,4,1,36673,100,1,2,2,1,18),_CmmTransSfpPlusCableTech_Type())
cmmTransSfpPlusCableTech.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSfpPlusCableTech.setStatus(_A)
class _CmmTransEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('enc-unspecified',1),('enc-8b-or-10b',2),('enc-4b-or-5b',3),('enc-nrz',4),('enc-manchester',5),('enc-sonet-scrambled',6),('enc-64b-or-66b',7),('enc-256b-or-257b',8),('enc-pam4',9),('enc-reserved',10)))
_CmmTransEncoding_Type.__name__=_E
_CmmTransEncoding_Object=MibTableColumn
cmmTransEncoding=_CmmTransEncoding_Object((1,3,6,1,4,1,36673,100,1,2,2,1,19),_CmmTransEncoding_Type())
cmmTransEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransEncoding.setStatus(_A)
_CmmTransLengthKmtrs_Type=Integer32
_CmmTransLengthKmtrs_Object=MibTableColumn
cmmTransLengthKmtrs=_CmmTransLengthKmtrs_Object((1,3,6,1,4,1,36673,100,1,2,2,1,20),_CmmTransLengthKmtrs_Type())
cmmTransLengthKmtrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLengthKmtrs.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLengthKmtrs.setUnits('km')
_CmmTransLengthMtrs_Type=Integer32
_CmmTransLengthMtrs_Object=MibTableColumn
cmmTransLengthMtrs=_CmmTransLengthMtrs_Object((1,3,6,1,4,1,36673,100,1,2,2,1,21),_CmmTransLengthMtrs_Type())
cmmTransLengthMtrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLengthMtrs.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLengthMtrs.setUnits('100 m')
_CmmTransLengthOM1_Type=Integer32
_CmmTransLengthOM1_Object=MibTableColumn
cmmTransLengthOM1=_CmmTransLengthOM1_Object((1,3,6,1,4,1,36673,100,1,2,2,1,22),_CmmTransLengthOM1_Type())
cmmTransLengthOM1.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLengthOM1.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLengthOM1.setUnits(_t)
_CmmTransLengthOM2_Type=Integer32
_CmmTransLengthOM2_Object=MibTableColumn
cmmTransLengthOM2=_CmmTransLengthOM2_Object((1,3,6,1,4,1,36673,100,1,2,2,1,23),_CmmTransLengthOM2_Type())
cmmTransLengthOM2.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLengthOM2.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLengthOM2.setUnits(_t)
_CmmTransLengthOM3_Type=Integer32
_CmmTransLengthOM3_Object=MibTableColumn
cmmTransLengthOM3=_CmmTransLengthOM3_Object((1,3,6,1,4,1,36673,100,1,2,2,1,24),_CmmTransLengthOM3_Type())
cmmTransLengthOM3.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLengthOM3.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLengthOM3.setUnits(_t)
_CmmTransLengthOM4_Type=Integer32
_CmmTransLengthOM4_Object=MibTableColumn
cmmTransLengthOM4=_CmmTransLengthOM4_Object((1,3,6,1,4,1,36673,100,1,2,2,1,25),_CmmTransLengthOM4_Type())
cmmTransLengthOM4.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLengthOM4.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLengthOM4.setUnits(_t)
_CmmTransVendorName_Type=DisplayString
_CmmTransVendorName_Object=MibTableColumn
cmmTransVendorName=_CmmTransVendorName_Object((1,3,6,1,4,1,36673,100,1,2,2,1,26),_CmmTransVendorName_Type())
cmmTransVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVendorName.setStatus(_A)
_CmmTransVendorOUI_Type=DisplayString
_CmmTransVendorOUI_Object=MibTableColumn
cmmTransVendorOUI=_CmmTransVendorOUI_Object((1,3,6,1,4,1,36673,100,1,2,2,1,27),_CmmTransVendorOUI_Type())
cmmTransVendorOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVendorOUI.setStatus(_A)
_CmmTransVendorPartNumber_Type=DisplayString
_CmmTransVendorPartNumber_Object=MibTableColumn
cmmTransVendorPartNumber=_CmmTransVendorPartNumber_Object((1,3,6,1,4,1,36673,100,1,2,2,1,28),_CmmTransVendorPartNumber_Type())
cmmTransVendorPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVendorPartNumber.setStatus(_A)
_CmmTransVendorRevision_Type=DisplayString
_CmmTransVendorRevision_Object=MibTableColumn
cmmTransVendorRevision=_CmmTransVendorRevision_Object((1,3,6,1,4,1,36673,100,1,2,2,1,29),_CmmTransVendorRevision_Type())
cmmTransVendorRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVendorRevision.setStatus(_A)
class _CmmTransCheckCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CmmTransCheckCode_Type.__name__=_a
_CmmTransCheckCode_Object=MibTableColumn
cmmTransCheckCode=_CmmTransCheckCode_Object((1,3,6,1,4,1,36673,100,1,2,2,1,30),_CmmTransCheckCode_Type())
cmmTransCheckCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransCheckCode.setStatus(_A)
class _CmmTransCheckCodeExtended_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CmmTransCheckCodeExtended_Type.__name__=_a
_CmmTransCheckCodeExtended_Object=MibTableColumn
cmmTransCheckCodeExtended=_CmmTransCheckCodeExtended_Object((1,3,6,1,4,1,36673,100,1,2,2,1,31),_CmmTransCheckCodeExtended_Type())
cmmTransCheckCodeExtended.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransCheckCodeExtended.setStatus(_A)
_CmmTransNominalBitRate_Type=Integer32
_CmmTransNominalBitRate_Object=MibTableColumn
cmmTransNominalBitRate=_CmmTransNominalBitRate_Object((1,3,6,1,4,1,36673,100,1,2,2,1,32),_CmmTransNominalBitRate_Type())
cmmTransNominalBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransNominalBitRate.setStatus(_A)
if mibBuilder.loadTexts:cmmTransNominalBitRate.setUnits('100MBd')
_CmmTransBitRateMax_Type=Integer32
_CmmTransBitRateMax_Object=MibTableColumn
cmmTransBitRateMax=_CmmTransBitRateMax_Object((1,3,6,1,4,1,36673,100,1,2,2,1,33),_CmmTransBitRateMax_Type())
cmmTransBitRateMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransBitRateMax.setStatus(_A)
_CmmTransBitRateMin_Type=Integer32
_CmmTransBitRateMin_Object=MibTableColumn
cmmTransBitRateMin=_CmmTransBitRateMin_Object((1,3,6,1,4,1,36673,100,1,2,2,1,34),_CmmTransBitRateMin_Type())
cmmTransBitRateMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransBitRateMin.setStatus(_A)
_CmmTransVendorSerialNumber_Type=DisplayString
_CmmTransVendorSerialNumber_Object=MibTableColumn
cmmTransVendorSerialNumber=_CmmTransVendorSerialNumber_Object((1,3,6,1,4,1,36673,100,1,2,2,1,35),_CmmTransVendorSerialNumber_Type())
cmmTransVendorSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVendorSerialNumber.setStatus(_A)
_CmmTransDateCode_Type=DisplayString
_CmmTransDateCode_Object=MibTableColumn
cmmTransDateCode=_CmmTransDateCode_Object((1,3,6,1,4,1,36673,100,1,2,2,1,36),_CmmTransDateCode_Type())
cmmTransDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransDateCode.setStatus(_A)
class _CmmTransDDMSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('yes',1),('no',2),(_F,3)))
_CmmTransDDMSupport_Type.__name__=_E
_CmmTransDDMSupport_Object=MibTableColumn
cmmTransDDMSupport=_CmmTransDDMSupport_Object((1,3,6,1,4,1,36673,100,1,2,2,1,37),_CmmTransDDMSupport_Type())
cmmTransDDMSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransDDMSupport.setStatus(_A)
_CmmTransMaxCaseTemp_Type=Integer32
_CmmTransMaxCaseTemp_Object=MibTableColumn
cmmTransMaxCaseTemp=_CmmTransMaxCaseTemp_Object((1,3,6,1,4,1,36673,100,1,2,2,1,38),_CmmTransMaxCaseTemp_Type())
cmmTransMaxCaseTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransMaxCaseTemp.setStatus(_A)
if mibBuilder.loadTexts:cmmTransMaxCaseTemp.setUnits(' 0.01 C ')
class _CmmTransSFPOptionsImp_Type(Bits):namedValues=NamedValues(*((_s,0),('power-level3',1),('paging',2),('internal-retimer-or-cdr',3),('cooled-laser-transmitter',4),('power-level2',5),('power-level1',6),('linear-receiver-output',7),('receiver-decision-threshold',8),('transmitter-wavelength-or-tunable-frequency',9),('rate-select',10),(_Ah,11),('tx-fault',12),('rx-loss-of-signal',13)))
_CmmTransSFPOptionsImp_Type.__name__=_N
_CmmTransSFPOptionsImp_Object=MibTableColumn
cmmTransSFPOptionsImp=_CmmTransSFPOptionsImp_Object((1,3,6,1,4,1,36673,100,1,2,2,1,39),_CmmTransSFPOptionsImp_Type())
cmmTransSFPOptionsImp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransSFPOptionsImp.setStatus(_A)
class _CmmTransQSFPOptionsImp_Type(Bits):namedValues=NamedValues(*((_s,0),('tx-inputequalization-auto-adaptive',1),('tx-inputequalization-fixed-programmable',2),('tx-outputemphasis-fixed-programmable',3),('tx-outputamplitude-fixed-programmable',4),('tx-cdr-on-or-off-controllable',5),('tx-cdr-on-or-off-fixed',6),('rx-cdr-on-or-off-controllable',7),('rx-cdr-on-or-off-fixed',8),('tx-cdr-lossoflock',9),('rx-cdr-lossoflock',10),('rx-squelch-disable',11),('rx-output-disable',12),('tx-squelch-disable',13),('tx-squelch',14),('page2-provided',15),('page1-provided',16),('rateselect-controllable',17),('rateselect-fixed',18),(_Ah,19),('tx-fault',20),('tx-squelch-to-reduce-pave',21),('tx-squelch-to-reduce-oma',22),('tx-loss-of-signal',23)))
_CmmTransQSFPOptionsImp_Type.__name__=_N
_CmmTransQSFPOptionsImp_Object=MibTableColumn
cmmTransQSFPOptionsImp=_CmmTransQSFPOptionsImp_Object((1,3,6,1,4,1,36673,100,1,2,2,1,40),_CmmTransQSFPOptionsImp_Type())
cmmTransQSFPOptionsImp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransQSFPOptionsImp.setStatus(_A)
class _CmmTransPresence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('present',1),(_b,2),(_F,3)))
_CmmTransPresence_Type.__name__=_E
_CmmTransPresence_Object=MibTableColumn
cmmTransPresence=_CmmTransPresence_Object((1,3,6,1,4,1,36673,100,1,2,2,1,41),_CmmTransPresence_Type())
cmmTransPresence.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransPresence.setStatus(_A)
_CmmTransDDMTable_Object=MibTable
cmmTransDDMTable=_CmmTransDDMTable_Object((1,3,6,1,4,1,36673,100,1,2,3))
if mibBuilder.loadTexts:cmmTransDDMTable.setStatus(_A)
_CmmTransDDMEntry_Object=MibTableRow
cmmTransDDMEntry=_CmmTransDDMEntry_Object((1,3,6,1,4,1,36673,100,1,2,3,1))
cmmTransDDMEntry.setIndexNames((0,_B,_D),(0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:cmmTransDDMEntry.setStatus(_A)
_CmmTransChannelIndex_Type=Integer32
_CmmTransChannelIndex_Object=MibTableColumn
cmmTransChannelIndex=_CmmTransChannelIndex_Object((1,3,6,1,4,1,36673,100,1,2,3,1,1),_CmmTransChannelIndex_Type())
cmmTransChannelIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:cmmTransChannelIndex.setStatus(_A)
_CmmTransTemperature_Type=Integer32
_CmmTransTemperature_Object=MibTableColumn
cmmTransTemperature=_CmmTransTemperature_Object((1,3,6,1,4,1,36673,100,1,2,3,1,2),_CmmTransTemperature_Type())
cmmTransTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTemperature.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTemperature.setUnits(_M)
_CmmTransTempCriticalThresholdMin_Type=Integer32
_CmmTransTempCriticalThresholdMin_Object=MibTableColumn
cmmTransTempCriticalThresholdMin=_CmmTransTempCriticalThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,3),_CmmTransTempCriticalThresholdMin_Type())
cmmTransTempCriticalThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTempCriticalThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTempCriticalThresholdMin.setUnits(_M)
_CmmTransTempCriticalThresholdMax_Type=Integer32
_CmmTransTempCriticalThresholdMax_Object=MibTableColumn
cmmTransTempCriticalThresholdMax=_CmmTransTempCriticalThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,4),_CmmTransTempCriticalThresholdMax_Type())
cmmTransTempCriticalThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTempCriticalThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTempCriticalThresholdMax.setUnits(_M)
_CmmTransTempAlertThresholdMin_Type=Integer32
_CmmTransTempAlertThresholdMin_Object=MibTableColumn
cmmTransTempAlertThresholdMin=_CmmTransTempAlertThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,5),_CmmTransTempAlertThresholdMin_Type())
cmmTransTempAlertThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTempAlertThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTempAlertThresholdMin.setUnits(_M)
_CmmTransTempAlertThresholdMax_Type=Integer32
_CmmTransTempAlertThresholdMax_Object=MibTableColumn
cmmTransTempAlertThresholdMax=_CmmTransTempAlertThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,6),_CmmTransTempAlertThresholdMax_Type())
cmmTransTempAlertThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTempAlertThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTempAlertThresholdMax.setUnits(_M)
_CmmTransVoltage_Type=Integer32
_CmmTransVoltage_Object=MibTableColumn
cmmTransVoltage=_CmmTransVoltage_Object((1,3,6,1,4,1,36673,100,1,2,3,1,7),_CmmTransVoltage_Type())
cmmTransVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVoltage.setStatus(_A)
if mibBuilder.loadTexts:cmmTransVoltage.setUnits(_i)
_CmmTransVoltCriticalThresholdMin_Type=Integer32
_CmmTransVoltCriticalThresholdMin_Object=MibTableColumn
cmmTransVoltCriticalThresholdMin=_CmmTransVoltCriticalThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,8),_CmmTransVoltCriticalThresholdMin_Type())
cmmTransVoltCriticalThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVoltCriticalThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransVoltCriticalThresholdMin.setUnits(_i)
_CmmTransVoltCriticalThresholdMax_Type=Integer32
_CmmTransVoltCriticalThresholdMax_Object=MibTableColumn
cmmTransVoltCriticalThresholdMax=_CmmTransVoltCriticalThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,9),_CmmTransVoltCriticalThresholdMax_Type())
cmmTransVoltCriticalThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVoltCriticalThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransVoltCriticalThresholdMax.setUnits(_i)
_CmmTransVoltAlertThresholdMin_Type=Integer32
_CmmTransVoltAlertThresholdMin_Object=MibTableColumn
cmmTransVoltAlertThresholdMin=_CmmTransVoltAlertThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,10),_CmmTransVoltAlertThresholdMin_Type())
cmmTransVoltAlertThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVoltAlertThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransVoltAlertThresholdMin.setUnits(_i)
_CmmTransVoltAlertThresholdMax_Type=Integer32
_CmmTransVoltAlertThresholdMax_Object=MibTableColumn
cmmTransVoltAlertThresholdMax=_CmmTransVoltAlertThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,11),_CmmTransVoltAlertThresholdMax_Type())
cmmTransVoltAlertThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransVoltAlertThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransVoltAlertThresholdMax.setUnits(_i)
_CmmTransLaserBiasCurrent_Type=Integer32
_CmmTransLaserBiasCurrent_Object=MibTableColumn
cmmTransLaserBiasCurrent=_CmmTransLaserBiasCurrent_Object((1,3,6,1,4,1,36673,100,1,2,3,1,12),_CmmTransLaserBiasCurrent_Type())
cmmTransLaserBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrent.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrent.setUnits(_j)
_CmmTransLaserBiasCurrCriticalThresholdMin_Type=Integer32
_CmmTransLaserBiasCurrCriticalThresholdMin_Object=MibTableColumn
cmmTransLaserBiasCurrCriticalThresholdMin=_CmmTransLaserBiasCurrCriticalThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,13),_CmmTransLaserBiasCurrCriticalThresholdMin_Type())
cmmTransLaserBiasCurrCriticalThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrCriticalThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrCriticalThresholdMin.setUnits(_j)
_CmmTransLaserBiasCurrCriticalThresholdMax_Type=Integer32
_CmmTransLaserBiasCurrCriticalThresholdMax_Object=MibTableColumn
cmmTransLaserBiasCurrCriticalThresholdMax=_CmmTransLaserBiasCurrCriticalThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,14),_CmmTransLaserBiasCurrCriticalThresholdMax_Type())
cmmTransLaserBiasCurrCriticalThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrCriticalThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrCriticalThresholdMax.setUnits(_j)
_CmmTransLaserBiasCurrAlertThresholdMin_Type=Integer32
_CmmTransLaserBiasCurrAlertThresholdMin_Object=MibTableColumn
cmmTransLaserBiasCurrAlertThresholdMin=_CmmTransLaserBiasCurrAlertThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,15),_CmmTransLaserBiasCurrAlertThresholdMin_Type())
cmmTransLaserBiasCurrAlertThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrAlertThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrAlertThresholdMin.setUnits(_j)
_CmmTransLaserBiasCurrAlertThresholdMax_Type=Integer32
_CmmTransLaserBiasCurrAlertThresholdMax_Object=MibTableColumn
cmmTransLaserBiasCurrAlertThresholdMax=_CmmTransLaserBiasCurrAlertThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,16),_CmmTransLaserBiasCurrAlertThresholdMax_Type())
cmmTransLaserBiasCurrAlertThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrAlertThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransLaserBiasCurrAlertThresholdMax.setUnits(_j)
_CmmTransTxPower_Type=Integer32
_CmmTransTxPower_Object=MibTableColumn
cmmTransTxPower=_CmmTransTxPower_Object((1,3,6,1,4,1,36673,100,1,2,3,1,17),_CmmTransTxPower_Type())
cmmTransTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxPower.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTxPower.setUnits(_T)
_CmmTransTxPowerCriticalThresholdMin_Type=Integer32
_CmmTransTxPowerCriticalThresholdMin_Object=MibTableColumn
cmmTransTxPowerCriticalThresholdMin=_CmmTransTxPowerCriticalThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,18),_CmmTransTxPowerCriticalThresholdMin_Type())
cmmTransTxPowerCriticalThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxPowerCriticalThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTxPowerCriticalThresholdMin.setUnits(_T)
_CmmTransTxPowerCriticalThresholdMax_Type=Integer32
_CmmTransTxPowerCriticalThresholdMax_Object=MibTableColumn
cmmTransTxPowerCriticalThresholdMax=_CmmTransTxPowerCriticalThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,19),_CmmTransTxPowerCriticalThresholdMax_Type())
cmmTransTxPowerCriticalThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxPowerCriticalThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTxPowerCriticalThresholdMax.setUnits(_T)
_CmmTransTxPowerAlertThresholdMin_Type=Integer32
_CmmTransTxPowerAlertThresholdMin_Object=MibTableColumn
cmmTransTxPowerAlertThresholdMin=_CmmTransTxPowerAlertThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,20),_CmmTransTxPowerAlertThresholdMin_Type())
cmmTransTxPowerAlertThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxPowerAlertThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTxPowerAlertThresholdMin.setUnits(_T)
_CmmTransTxPowerAlertThresholdMax_Type=Integer32
_CmmTransTxPowerAlertThresholdMax_Object=MibTableColumn
cmmTransTxPowerAlertThresholdMax=_CmmTransTxPowerAlertThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,21),_CmmTransTxPowerAlertThresholdMax_Type())
cmmTransTxPowerAlertThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxPowerAlertThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransTxPowerAlertThresholdMax.setUnits(_T)
_CmmTransRxPower_Type=Integer32
_CmmTransRxPower_Object=MibTableColumn
cmmTransRxPower=_CmmTransRxPower_Object((1,3,6,1,4,1,36673,100,1,2,3,1,22),_CmmTransRxPower_Type())
cmmTransRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxPower.setStatus(_A)
if mibBuilder.loadTexts:cmmTransRxPower.setUnits(_T)
_CmmTransRxPowerCriticalThresholdMin_Type=Integer32
_CmmTransRxPowerCriticalThresholdMin_Object=MibTableColumn
cmmTransRxPowerCriticalThresholdMin=_CmmTransRxPowerCriticalThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,23),_CmmTransRxPowerCriticalThresholdMin_Type())
cmmTransRxPowerCriticalThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxPowerCriticalThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransRxPowerCriticalThresholdMin.setUnits(_T)
_CmmTransRxPowerCriticalThresholdMax_Type=Integer32
_CmmTransRxPowerCriticalThresholdMax_Object=MibTableColumn
cmmTransRxPowerCriticalThresholdMax=_CmmTransRxPowerCriticalThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,24),_CmmTransRxPowerCriticalThresholdMax_Type())
cmmTransRxPowerCriticalThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxPowerCriticalThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransRxPowerCriticalThresholdMax.setUnits(_T)
_CmmTransRxPowerAlertThresholdMin_Type=Integer32
_CmmTransRxPowerAlertThresholdMin_Object=MibTableColumn
cmmTransRxPowerAlertThresholdMin=_CmmTransRxPowerAlertThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,3,1,25),_CmmTransRxPowerAlertThresholdMin_Type())
cmmTransRxPowerAlertThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxPowerAlertThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmTransRxPowerAlertThresholdMin.setUnits(_T)
_CmmTransRxPowerAlertThresholdMax_Type=Integer32
_CmmTransRxPowerAlertThresholdMax_Object=MibTableColumn
cmmTransRxPowerAlertThresholdMax=_CmmTransRxPowerAlertThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,3,1,26),_CmmTransRxPowerAlertThresholdMax_Type())
cmmTransRxPowerAlertThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxPowerAlertThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmTransRxPowerAlertThresholdMax.setUnits(_T)
class _CmmTransTxPowerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Ai,1),(_Aj,2),(_I,3),(_F,4)))
_CmmTransTxPowerSupported_Type.__name__=_E
_CmmTransTxPowerSupported_Object=MibTableColumn
cmmTransTxPowerSupported=_CmmTransTxPowerSupported_Object((1,3,6,1,4,1,36673,100,1,2,3,1,27),_CmmTransTxPowerSupported_Type())
cmmTransTxPowerSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxPowerSupported.setStatus(_A)
class _CmmTransRxPowerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Ai,1),(_Aj,2),(_I,3),(_F,4)))
_CmmTransRxPowerSupported_Type.__name__=_E
_CmmTransRxPowerSupported_Object=MibTableColumn
cmmTransRxPowerSupported=_CmmTransRxPowerSupported_Object((1,3,6,1,4,1,36673,100,1,2,3,1,28),_CmmTransRxPowerSupported_Type())
cmmTransRxPowerSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxPowerSupported.setStatus(_A)
class _CmmTransDDMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('activeunsupported',2),('inactive',3),('inactiveunsupported',4),(_I,5),(_F,6)))
_CmmTransDDMStatus_Type.__name__=_E
_CmmTransDDMStatus_Object=MibTableColumn
cmmTransDDMStatus=_CmmTransDDMStatus_Object((1,3,6,1,4,1,36673,100,1,2,3,1,29),_CmmTransDDMStatus_Type())
cmmTransDDMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransDDMStatus.setStatus(_A)
class _CmmTransTxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),(_v,2),(_F,3)))
_CmmTransTxState_Type.__name__=_E
_CmmTransTxState_Object=MibTableColumn
cmmTransTxState=_CmmTransTxState_Object((1,3,6,1,4,1,36673,100,1,2,3,1,30),_CmmTransTxState_Type())
cmmTransTxState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxState.setStatus(_A)
class _CmmTransRxLosState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),(_v,2),(_F,3)))
_CmmTransRxLosState_Type.__name__=_E
_CmmTransRxLosState_Object=MibTableColumn
cmmTransRxLosState=_CmmTransRxLosState_Object((1,3,6,1,4,1,36673,100,1,2,3,1,31),_CmmTransRxLosState_Type())
cmmTransRxLosState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransRxLosState.setStatus(_A)
class _CmmTransTxLosState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),(_v,2),(_F,3)))
_CmmTransTxLosState_Type.__name__=_E
_CmmTransTxLosState_Object=MibTableColumn
cmmTransTxLosState=_CmmTransTxLosState_Object((1,3,6,1,4,1,36673,100,1,2,3,1,32),_CmmTransTxLosState_Type())
cmmTransTxLosState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransTxLosState.setStatus(_A)
class _CmmTransResetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('reset',2),(_F,3)))
_CmmTransResetState_Type.__name__=_E
_CmmTransResetState_Object=MibTableColumn
cmmTransResetState=_CmmTransResetState_Object((1,3,6,1,4,1,36673,100,1,2,3,1,33),_CmmTransResetState_Type())
cmmTransResetState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransResetState.setStatus(_A)
class _CmmTransPowerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('high',2),(_F,3)))
_CmmTransPowerMode_Type.__name__=_E
_CmmTransPowerMode_Object=MibTableColumn
cmmTransPowerMode=_CmmTransPowerMode_Object((1,3,6,1,4,1,36673,100,1,2,3,1,34),_CmmTransPowerMode_Type())
cmmTransPowerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTransPowerMode.setStatus(_A)
_CmmSysRamTable_Object=MibTable
cmmSysRamTable=_CmmSysRamTable_Object((1,3,6,1,4,1,36673,100,1,2,4))
if mibBuilder.loadTexts:cmmSysRamTable.setStatus(_A)
_CmmSysRamEntry_Object=MibTableRow
cmmSysRamEntry=_CmmSysRamEntry_Object((1,3,6,1,4,1,36673,100,1,2,4,1))
cmmSysRamEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmSysRamEntry.setStatus(_A)
_CmmSysRamTotalMem_Type=Integer32
_CmmSysRamTotalMem_Object=MibTableColumn
cmmSysRamTotalMem=_CmmSysRamTotalMem_Object((1,3,6,1,4,1,36673,100,1,2,4,1,1),_CmmSysRamTotalMem_Type())
cmmSysRamTotalMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysRamTotalMem.setStatus(_A)
if mibBuilder.loadTexts:cmmSysRamTotalMem.setUnits(' MBytes ')
_CmmSysRamUsedMem_Type=Integer32
_CmmSysRamUsedMem_Object=MibTableColumn
cmmSysRamUsedMem=_CmmSysRamUsedMem_Object((1,3,6,1,4,1,36673,100,1,2,4,1,2),_CmmSysRamUsedMem_Type())
cmmSysRamUsedMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysRamUsedMem.setStatus(_A)
if mibBuilder.loadTexts:cmmSysRamUsedMem.setUnits(_W)
_CmmSysRamFreeMem_Type=Integer32
_CmmSysRamFreeMem_Object=MibTableColumn
cmmSysRamFreeMem=_CmmSysRamFreeMem_Object((1,3,6,1,4,1,36673,100,1,2,4,1,3),_CmmSysRamFreeMem_Type())
cmmSysRamFreeMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysRamFreeMem.setStatus(_A)
if mibBuilder.loadTexts:cmmSysRamFreeMem.setUnits(_W)
_CmmSysRamCriticalThreshold_Type=Integer32
_CmmSysRamCriticalThreshold_Object=MibTableColumn
cmmSysRamCriticalThreshold=_CmmSysRamCriticalThreshold_Object((1,3,6,1,4,1,36673,100,1,2,4,1,4),_CmmSysRamCriticalThreshold_Type())
cmmSysRamCriticalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysRamCriticalThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmSysRamCriticalThreshold.setUnits(_W)
_CmmSysRamAlertThreshold_Type=Integer32
_CmmSysRamAlertThreshold_Object=MibTableColumn
cmmSysRamAlertThreshold=_CmmSysRamAlertThreshold_Object((1,3,6,1,4,1,36673,100,1,2,4,1,5),_CmmSysRamAlertThreshold_Type())
cmmSysRamAlertThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysRamAlertThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmSysRamAlertThreshold.setUnits(_W)
_CmmStackCpuTable_Object=MibTable
cmmStackCpuTable=_CmmStackCpuTable_Object((1,3,6,1,4,1,36673,100,1,2,5))
if mibBuilder.loadTexts:cmmStackCpuTable.setStatus(_A)
_CmmStackCpuEntry_Object=MibTableRow
cmmStackCpuEntry=_CmmStackCpuEntry_Object((1,3,6,1,4,1,36673,100,1,2,5,1))
cmmStackCpuEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmStackCpuEntry.setStatus(_A)
_CmmStackUnitNumCpuProcessor_Type=Integer32
_CmmStackUnitNumCpuProcessor_Object=MibTableColumn
cmmStackUnitNumCpuProcessor=_CmmStackUnitNumCpuProcessor_Object((1,3,6,1,4,1,36673,100,1,2,5,1,1),_CmmStackUnitNumCpuProcessor_Type())
cmmStackUnitNumCpuProcessor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitNumCpuProcessor.setStatus(_A)
_CmmStackUnitCpuLoad1Min_Type=Integer32
_CmmStackUnitCpuLoad1Min_Object=MibTableColumn
cmmStackUnitCpuLoad1Min=_CmmStackUnitCpuLoad1Min_Object((1,3,6,1,4,1,36673,100,1,2,5,1,2),_CmmStackUnitCpuLoad1Min_Type())
cmmStackUnitCpuLoad1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCpuLoad1Min.setStatus(_A)
if mibBuilder.loadTexts:cmmStackUnitCpuLoad1Min.setUnits(_Q)
_CmmStackUnitCpuLoad5Min_Type=Integer32
_CmmStackUnitCpuLoad5Min_Object=MibTableColumn
cmmStackUnitCpuLoad5Min=_CmmStackUnitCpuLoad5Min_Object((1,3,6,1,4,1,36673,100,1,2,5,1,3),_CmmStackUnitCpuLoad5Min_Type())
cmmStackUnitCpuLoad5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCpuLoad5Min.setStatus(_A)
if mibBuilder.loadTexts:cmmStackUnitCpuLoad5Min.setUnits(_Q)
_CmmStackUnitCpuLoad15Min_Type=Integer32
_CmmStackUnitCpuLoad15Min_Object=MibTableColumn
cmmStackUnitCpuLoad15Min=_CmmStackUnitCpuLoad15Min_Object((1,3,6,1,4,1,36673,100,1,2,5,1,4),_CmmStackUnitCpuLoad15Min_Type())
cmmStackUnitCpuLoad15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCpuLoad15Min.setStatus(_A)
if mibBuilder.loadTexts:cmmStackUnitCpuLoad15Min.setUnits(_Q)
_CmmStackCpuLoad1minAlertThreshold_Type=Integer32
_CmmStackCpuLoad1minAlertThreshold_Object=MibTableColumn
cmmStackCpuLoad1minAlertThreshold=_CmmStackCpuLoad1minAlertThreshold_Object((1,3,6,1,4,1,36673,100,1,2,5,1,5),_CmmStackCpuLoad1minAlertThreshold_Type())
cmmStackCpuLoad1minAlertThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackCpuLoad1minAlertThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmStackCpuLoad1minAlertThreshold.setUnits(_Q)
_CmmStackCpuLoad1minCriticalThreshold_Type=Integer32
_CmmStackCpuLoad1minCriticalThreshold_Object=MibTableColumn
cmmStackCpuLoad1minCriticalThreshold=_CmmStackCpuLoad1minCriticalThreshold_Object((1,3,6,1,4,1,36673,100,1,2,5,1,6),_CmmStackCpuLoad1minCriticalThreshold_Type())
cmmStackCpuLoad1minCriticalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackCpuLoad1minCriticalThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmStackCpuLoad1minCriticalThreshold.setUnits(_Q)
_CmmStackCpuLoad5minCriticalThreshold_Type=Integer32
_CmmStackCpuLoad5minCriticalThreshold_Object=MibTableColumn
cmmStackCpuLoad5minCriticalThreshold=_CmmStackCpuLoad5minCriticalThreshold_Object((1,3,6,1,4,1,36673,100,1,2,5,1,7),_CmmStackCpuLoad5minCriticalThreshold_Type())
cmmStackCpuLoad5minCriticalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackCpuLoad5minCriticalThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmStackCpuLoad5minCriticalThreshold.setUnits(_Q)
_CmmStackCpuLoad15minCriticalThreshold_Type=Integer32
_CmmStackCpuLoad15minCriticalThreshold_Object=MibTableColumn
cmmStackCpuLoad15minCriticalThreshold=_CmmStackCpuLoad15minCriticalThreshold_Object((1,3,6,1,4,1,36673,100,1,2,5,1,8),_CmmStackCpuLoad15minCriticalThreshold_Type())
cmmStackCpuLoad15minCriticalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackCpuLoad15minCriticalThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmStackCpuLoad15minCriticalThreshold.setUnits(_Q)
_CmmStackUnitCpuUtilization_Type=Integer32
_CmmStackUnitCpuUtilization_Object=MibTableColumn
cmmStackUnitCpuUtilization=_CmmStackUnitCpuUtilization_Object((1,3,6,1,4,1,36673,100,1,2,5,1,9),_CmmStackUnitCpuUtilization_Type())
cmmStackUnitCpuUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCpuUtilization.setStatus(_A)
if mibBuilder.loadTexts:cmmStackUnitCpuUtilization.setUnits(_Q)
_CmmStackUnitCpuUtilAlertThreshold_Type=Integer32
_CmmStackUnitCpuUtilAlertThreshold_Object=MibTableColumn
cmmStackUnitCpuUtilAlertThreshold=_CmmStackUnitCpuUtilAlertThreshold_Object((1,3,6,1,4,1,36673,100,1,2,5,1,10),_CmmStackUnitCpuUtilAlertThreshold_Type())
cmmStackUnitCpuUtilAlertThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCpuUtilAlertThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmStackUnitCpuUtilAlertThreshold.setUnits(_Q)
_CmmStackUnitCpuUtilCriticalThreshold_Type=Integer32
_CmmStackUnitCpuUtilCriticalThreshold_Object=MibTableColumn
cmmStackUnitCpuUtilCriticalThreshold=_CmmStackUnitCpuUtilCriticalThreshold_Object((1,3,6,1,4,1,36673,100,1,2,5,1,11),_CmmStackUnitCpuUtilCriticalThreshold_Type())
cmmStackUnitCpuUtilCriticalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmStackUnitCpuUtilCriticalThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmStackUnitCpuUtilCriticalThreshold.setUnits(_Q)
_CmmSysPowerSupplyTable_Object=MibTable
cmmSysPowerSupplyTable=_CmmSysPowerSupplyTable_Object((1,3,6,1,4,1,36673,100,1,2,6))
if mibBuilder.loadTexts:cmmSysPowerSupplyTable.setStatus(_A)
_CmmSysPowerSupplyEntry_Object=MibTableRow
cmmSysPowerSupplyEntry=_CmmSysPowerSupplyEntry_Object((1,3,6,1,4,1,36673,100,1,2,6,1))
cmmSysPowerSupplyEntry.setIndexNames((0,_B,_D),(0,_B,_V))
if mibBuilder.loadTexts:cmmSysPowerSupplyEntry.setStatus(_A)
_CmmSysPSUIndex_Type=Integer32
_CmmSysPSUIndex_Object=MibTableColumn
cmmSysPSUIndex=_CmmSysPSUIndex_Object((1,3,6,1,4,1,36673,100,1,2,6,1,1),_CmmSysPSUIndex_Type())
cmmSysPSUIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSUIndex.setStatus(_A)
class _CmmSysPowerSupplyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),('running',2),('faulty',3),(_F,4)))
_CmmSysPowerSupplyOperStatus_Type.__name__=_E
_CmmSysPowerSupplyOperStatus_Object=MibTableColumn
cmmSysPowerSupplyOperStatus=_CmmSysPowerSupplyOperStatus_Object((1,3,6,1,4,1,36673,100,1,2,6,1,2),_CmmSysPowerSupplyOperStatus_Type())
cmmSysPowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPowerSupplyOperStatus.setStatus(_A)
class _CmmSysPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Ak,1),(_Al,2),(_Am,3),(_An,4),(_F,5),(_I,6)))
_CmmSysPowerSupplyType_Type.__name__=_E
_CmmSysPowerSupplyType_Object=MibTableColumn
cmmSysPowerSupplyType=_CmmSysPowerSupplyType_Object((1,3,6,1,4,1,36673,100,1,2,6,1,3),_CmmSysPowerSupplyType_Type())
cmmSysPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPowerSupplyType.setStatus(_A)
class _CmmSysHotSwapStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3)))
_CmmSysHotSwapStat_Type.__name__=_E
_CmmSysHotSwapStat_Object=MibTableColumn
cmmSysHotSwapStat=_CmmSysHotSwapStat_Object((1,3,6,1,4,1,36673,100,1,2,6,1,4),_CmmSysHotSwapStat_Type())
cmmSysHotSwapStat.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHotSwapStat.setStatus(_A)
_CmmSysPSConsumption_Type=Integer32
_CmmSysPSConsumption_Object=MibTableColumn
cmmSysPSConsumption=_CmmSysPSConsumption_Object((1,3,6,1,4,1,36673,100,1,2,6,1,5),_CmmSysPSConsumption_Type())
cmmSysPSConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSConsumption.setStatus(_A)
if mibBuilder.loadTexts:cmmSysPSConsumption.setUnits('0.01 W')
_CmmSysInputPower_Type=Integer32
_CmmSysInputPower_Object=MibTableColumn
cmmSysInputPower=_CmmSysInputPower_Object((1,3,6,1,4,1,36673,100,1,2,6,1,6),_CmmSysInputPower_Type())
cmmSysInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysInputPower.setStatus(_A)
if mibBuilder.loadTexts:cmmSysInputPower.setUnits('0.01 W')
_CmmSysInputVoltage_Type=Integer32
_CmmSysInputVoltage_Object=MibTableColumn
cmmSysInputVoltage=_CmmSysInputVoltage_Object((1,3,6,1,4,1,36673,100,1,2,6,1,7),_CmmSysInputVoltage_Type())
cmmSysInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:cmmSysInputVoltage.setUnits('0.01 V')
_CmmSysOutputVoltage_Type=Integer32
_CmmSysOutputVoltage_Object=MibTableColumn
cmmSysOutputVoltage=_CmmSysOutputVoltage_Object((1,3,6,1,4,1,36673,100,1,2,6,1,8),_CmmSysOutputVoltage_Type())
cmmSysOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:cmmSysOutputVoltage.setUnits('0.01 V')
_CmmSysInputCurrent_Type=Integer32
_CmmSysInputCurrent_Object=MibTableColumn
cmmSysInputCurrent=_CmmSysInputCurrent_Object((1,3,6,1,4,1,36673,100,1,2,6,1,9),_CmmSysInputCurrent_Type())
cmmSysInputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysInputCurrent.setStatus(_A)
if mibBuilder.loadTexts:cmmSysInputCurrent.setUnits('0.01 A')
_CmmSysOutputCurrent_Type=Integer32
_CmmSysOutputCurrent_Object=MibTableColumn
cmmSysOutputCurrent=_CmmSysOutputCurrent_Object((1,3,6,1,4,1,36673,100,1,2,6,1,10),_CmmSysOutputCurrent_Type())
cmmSysOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:cmmSysOutputCurrent.setUnits('0.01 A')
_CmmSysPSTemperature1_Type=Integer32
_CmmSysPSTemperature1_Object=MibTableColumn
cmmSysPSTemperature1=_CmmSysPSTemperature1_Object((1,3,6,1,4,1,36673,100,1,2,6,1,11),_CmmSysPSTemperature1_Type())
cmmSysPSTemperature1.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSTemperature1.setStatus(_A)
if mibBuilder.loadTexts:cmmSysPSTemperature1.setUnits(_M)
_CmmSysPSTemperature2_Type=Integer32
_CmmSysPSTemperature2_Object=MibTableColumn
cmmSysPSTemperature2=_CmmSysPSTemperature2_Object((1,3,6,1,4,1,36673,100,1,2,6,1,12),_CmmSysPSTemperature2_Type())
cmmSysPSTemperature2.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSTemperature2.setStatus(_A)
if mibBuilder.loadTexts:cmmSysPSTemperature2.setUnits(_M)
_CmmSysPSFan1Rpm_Type=Integer32
_CmmSysPSFan1Rpm_Object=MibTableColumn
cmmSysPSFan1Rpm=_CmmSysPSFan1Rpm_Object((1,3,6,1,4,1,36673,100,1,2,6,1,13),_CmmSysPSFan1Rpm_Type())
cmmSysPSFan1Rpm.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSFan1Rpm.setStatus(_A)
_CmmSysPSFan2Rpm_Type=Integer32
_CmmSysPSFan2Rpm_Object=MibTableColumn
cmmSysPSFan2Rpm=_CmmSysPSFan2Rpm_Object((1,3,6,1,4,1,36673,100,1,2,6,1,14),_CmmSysPSFan2Rpm_Type())
cmmSysPSFan2Rpm.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSFan2Rpm.setStatus(_A)
class _CmmSysPS12VPg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3)))
_CmmSysPS12VPg_Type.__name__=_E
_CmmSysPS12VPg_Object=MibTableColumn
cmmSysPS12VPg=_CmmSysPS12VPg_Object((1,3,6,1,4,1,36673,100,1,2,6,1,15),_CmmSysPS12VPg_Type())
cmmSysPS12VPg.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPS12VPg.setStatus(_A)
class _CmmSysPSAcAlert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3)))
_CmmSysPSAcAlert_Type.__name__=_E
_CmmSysPSAcAlert_Object=MibTableColumn
cmmSysPSAcAlert=_CmmSysPSAcAlert_Object((1,3,6,1,4,1,36673,100,1,2,6,1,16),_CmmSysPSAcAlert_Type())
cmmSysPSAcAlert.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSAcAlert.setStatus(_A)
class _CmmSysPSParamsSupport_Type(Bits):namedValues=NamedValues(*(('volt-in',0),('volt-out',1),('curr-in',2),('curr-out',3),('power-in',4),('power-out',5),('temp-1',6),('temp-2',7),('fan-1',8),('fan-2',9)))
_CmmSysPSParamsSupport_Type.__name__=_N
_CmmSysPSParamsSupport_Object=MibTableColumn
cmmSysPSParamsSupport=_CmmSysPSParamsSupport_Object((1,3,6,1,4,1,36673,100,1,2,6,1,17),_CmmSysPSParamsSupport_Type())
cmmSysPSParamsSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPSParamsSupport.setStatus(_A)
_CmmSysPowerRailTable_Object=MibTable
cmmSysPowerRailTable=_CmmSysPowerRailTable_Object((1,3,6,1,4,1,36673,100,1,2,7))
if mibBuilder.loadTexts:cmmSysPowerRailTable.setStatus(_A)
_CmmSysPowerRailEntry_Object=MibTableRow
cmmSysPowerRailEntry=_CmmSysPowerRailEntry_Object((1,3,6,1,4,1,36673,100,1,2,7,1))
cmmSysPowerRailEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmSysPowerRailEntry.setStatus(_A)
class _CmmSysPOWERVDDR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysPOWERVDDR_Type.__name__=_E
_CmmSysPOWERVDDR_Object=MibTableColumn
cmmSysPOWERVDDR=_CmmSysPOWERVDDR_Object((1,3,6,1,4,1,36673,100,1,2,7,1,1),_CmmSysPOWERVDDR_Type())
cmmSysPOWERVDDR.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPOWERVDDR.setStatus(_A)
class _CmmSysPOWERCORE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysPOWERCORE_Type.__name__=_E
_CmmSysPOWERCORE_Object=MibTableColumn
cmmSysPOWERCORE=_CmmSysPOWERCORE_Object((1,3,6,1,4,1,36673,100,1,2,7,1,2),_CmmSysPOWERCORE_Type())
cmmSysPOWERCORE.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPOWERCORE.setStatus(_A)
class _CmmSysV1P1POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV1P1POWERRAIL_Type.__name__=_E
_CmmSysV1P1POWERRAIL_Object=MibTableColumn
cmmSysV1P1POWERRAIL=_CmmSysV1P1POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,3),_CmmSysV1P1POWERRAIL_Type())
cmmSysV1P1POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV1P1POWERRAIL.setStatus(_A)
class _CmmSysMAINBOARDPOWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysMAINBOARDPOWERRAIL_Type.__name__=_E
_CmmSysMAINBOARDPOWERRAIL_Object=MibTableColumn
cmmSysMAINBOARDPOWERRAIL=_CmmSysMAINBOARDPOWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,4),_CmmSysMAINBOARDPOWERRAIL_Type())
cmmSysMAINBOARDPOWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysMAINBOARDPOWERRAIL.setStatus(_A)
class _CmmSysV1P05POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV1P05POWERRAIL_Type.__name__=_E
_CmmSysV1P05POWERRAIL_Object=MibTableColumn
cmmSysV1P05POWERRAIL=_CmmSysV1P05POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,5),_CmmSysV1P05POWERRAIL_Type())
cmmSysV1P05POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV1P05POWERRAIL.setStatus(_A)
class _CmmSysV1P5POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV1P5POWERRAIL_Type.__name__=_E
_CmmSysV1P5POWERRAIL_Object=MibTableColumn
cmmSysV1P5POWERRAIL=_CmmSysV1P5POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,6),_CmmSysV1P5POWERRAIL_Type())
cmmSysV1P5POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV1P5POWERRAIL.setStatus(_A)
class _CmmSysVCCPOWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCPOWERRAIL_Type.__name__=_E
_CmmSysVCCPOWERRAIL_Object=MibTableColumn
cmmSysVCCPOWERRAIL=_CmmSysVCCPOWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,7),_CmmSysVCCPOWERRAIL_Type())
cmmSysVCCPOWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCPOWERRAIL.setStatus(_A)
class _CmmSysSBV1P5POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysSBV1P5POWERRAIL_Type.__name__=_E
_CmmSysSBV1P5POWERRAIL_Object=MibTableColumn
cmmSysSBV1P5POWERRAIL=_CmmSysSBV1P5POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,8),_CmmSysSBV1P5POWERRAIL_Type())
cmmSysSBV1P5POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysSBV1P5POWERRAIL.setStatus(_A)
class _CmmSysV1P0POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV1P0POWERRAIL_Type.__name__=_E
_CmmSysV1P0POWERRAIL_Object=MibTableColumn
cmmSysV1P0POWERRAIL=_CmmSysV1P0POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,9),_CmmSysV1P0POWERRAIL_Type())
cmmSysV1P0POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV1P0POWERRAIL.setStatus(_A)
class _CmmSysV3P3POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV3P3POWERRAIL_Type.__name__=_E
_CmmSysV3P3POWERRAIL_Object=MibTableColumn
cmmSysV3P3POWERRAIL=_CmmSysV3P3POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,10),_CmmSysV3P3POWERRAIL_Type())
cmmSysV3P3POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV3P3POWERRAIL.setStatus(_A)
class _CmmSysV1P8POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV1P8POWERRAIL_Type.__name__=_E
_CmmSysV1P8POWERRAIL_Object=MibTableColumn
cmmSysV1P8POWERRAIL=_CmmSysV1P8POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,11),_CmmSysV1P8POWERRAIL_Type())
cmmSysV1P8POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV1P8POWERRAIL.setStatus(_A)
class _CmmSysV1P35POWERRAIL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysV1P35POWERRAIL_Type.__name__=_E
_CmmSysV1P35POWERRAIL_Object=MibTableColumn
cmmSysV1P35POWERRAIL=_CmmSysV1P35POWERRAIL_Object((1,3,6,1,4,1,36673,100,1,2,7,1,12),_CmmSysV1P35POWERRAIL_Type())
cmmSysV1P35POWERRAIL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysV1P35POWERRAIL.setStatus(_A)
class _CmmSysVCC5V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCC5V_Type.__name__=_E
_CmmSysVCC5V_Object=MibTableColumn
cmmSysVCC5V=_CmmSysVCC5V_Object((1,3,6,1,4,1,36673,100,1,2,7,1,13),_CmmSysVCC5V_Type())
cmmSysVCC5V.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCC5V.setStatus(_A)
class _CmmSysVCC33V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCC33V_Type.__name__=_E
_CmmSysVCC33V_Object=MibTableColumn
cmmSysVCC33V=_CmmSysVCC33V_Object((1,3,6,1,4,1,36673,100,1,2,7,1,14),_CmmSysVCC33V_Type())
cmmSysVCC33V.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCC33V.setStatus(_A)
class _CmmSysVCCMAC1V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCMAC1V_Type.__name__=_E
_CmmSysVCCMAC1V_Object=MibTableColumn
cmmSysVCCMAC1V=_CmmSysVCCMAC1V_Object((1,3,6,1,4,1,36673,100,1,2,7,1,15),_CmmSysVCCMAC1V_Type())
cmmSysVCCMAC1V.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCMAC1V.setStatus(_A)
class _CmmSysVCCMACAVS1V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCMACAVS1V_Type.__name__=_E
_CmmSysVCCMACAVS1V_Object=MibTableColumn
cmmSysVCCMACAVS1V=_CmmSysVCCMACAVS1V_Object((1,3,6,1,4,1,36673,100,1,2,7,1,16),_CmmSysVCCMACAVS1V_Type())
cmmSysVCCMACAVS1V.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCMACAVS1V.setStatus(_A)
class _CmmSysVCCV1P05_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCV1P05_Type.__name__=_E
_CmmSysVCCV1P05_Object=MibTableColumn
cmmSysVCCV1P05=_CmmSysVCCV1P05_Object((1,3,6,1,4,1,36673,100,1,2,7,1,17),_CmmSysVCCV1P05_Type())
cmmSysVCCV1P05.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCV1P05.setStatus(_A)
class _CmmSysVCCV1P5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCV1P5_Type.__name__=_E
_CmmSysVCCV1P5_Object=MibTableColumn
cmmSysVCCV1P5=_CmmSysVCCV1P5_Object((1,3,6,1,4,1,36673,100,1,2,7,1,18),_CmmSysVCCV1P5_Type())
cmmSysVCCV1P5.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCV1P5.setStatus(_A)
class _CmmSysVCCV1P8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCV1P8_Type.__name__=_E
_CmmSysVCCV1P8_Object=MibTableColumn
cmmSysVCCV1P8=_CmmSysVCCV1P8_Object((1,3,6,1,4,1,36673,100,1,2,7,1,19),_CmmSysVCCV1P8_Type())
cmmSysVCCV1P8.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCV1P8.setStatus(_A)
class _CmmSysVCCAVS1V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysVCCAVS1V_Type.__name__=_E
_CmmSysVCCAVS1V_Object=MibTableColumn
cmmSysVCCAVS1V=_CmmSysVCCAVS1V_Object((1,3,6,1,4,1,36673,100,1,2,7,1,20),_CmmSysVCCAVS1V_Type())
cmmSysVCCAVS1V.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysVCCAVS1V.setStatus(_A)
class _CmmSysDDRVTT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_CmmSysDDRVTT_Type.__name__=_E
_CmmSysDDRVTT_Object=MibTableColumn
cmmSysDDRVTT=_CmmSysDDRVTT_Object((1,3,6,1,4,1,36673,100,1,2,7,1,21),_CmmSysDDRVTT_Type())
cmmSysDDRVTT.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysDDRVTT.setStatus(_A)
_CmmFanTrayTable_Object=MibTable
cmmFanTrayTable=_CmmFanTrayTable_Object((1,3,6,1,4,1,36673,100,1,2,8))
if mibBuilder.loadTexts:cmmFanTrayTable.setStatus(_A)
_CmmFanTrayEntry_Object=MibTableRow
cmmFanTrayEntry=_CmmFanTrayEntry_Object((1,3,6,1,4,1,36673,100,1,2,8,1))
cmmFanTrayEntry.setIndexNames((0,_B,_D),(0,_B,_O))
if mibBuilder.loadTexts:cmmFanTrayEntry.setStatus(_A)
_CmmFanTrayNumber_Type=Integer32
_CmmFanTrayNumber_Object=MibTableColumn
cmmFanTrayNumber=_CmmFanTrayNumber_Object((1,3,6,1,4,1,36673,100,1,2,8,1,1),_CmmFanTrayNumber_Type())
cmmFanTrayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanTrayNumber.setStatus(_A)
class _CmmFanTrayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),('present',2),(_F,3)))
_CmmFanTrayStatus_Type.__name__=_E
_CmmFanTrayStatus_Object=MibTableColumn
cmmFanTrayStatus=_CmmFanTrayStatus_Object((1,3,6,1,4,1,36673,100,1,2,8,1,2),_CmmFanTrayStatus_Type())
cmmFanTrayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanTrayStatus.setStatus(_A)
_CmmFanTrayLedColor_Type=LedColorCode
_CmmFanTrayLedColor_Object=MibTableColumn
cmmFanTrayLedColor=_CmmFanTrayLedColor_Object((1,3,6,1,4,1,36673,100,1,2,8,1,3),_CmmFanTrayLedColor_Type())
cmmFanTrayLedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanTrayLedColor.setStatus(_A)
_CmmFanTable_Object=MibTable
cmmFanTable=_CmmFanTable_Object((1,3,6,1,4,1,36673,100,1,2,9))
if mibBuilder.loadTexts:cmmFanTable.setStatus(_A)
_CmmFanEntry_Object=MibTableRow
cmmFanEntry=_CmmFanEntry_Object((1,3,6,1,4,1,36673,100,1,2,9,1))
cmmFanEntry.setIndexNames((0,_B,_D),(0,_B,_O),(0,_B,_X))
if mibBuilder.loadTexts:cmmFanEntry.setStatus(_A)
_CmmFanIndex_Type=Integer32
_CmmFanIndex_Object=MibTableColumn
cmmFanIndex=_CmmFanIndex_Object((1,3,6,1,4,1,36673,100,1,2,9,1,1),_CmmFanIndex_Type())
cmmFanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanIndex.setStatus(_A)
_CmmFanRpm_Type=Integer32
_CmmFanRpm_Object=MibTableColumn
cmmFanRpm=_CmmFanRpm_Object((1,3,6,1,4,1,36673,100,1,2,9,1,2),_CmmFanRpm_Type())
cmmFanRpm.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanRpm.setStatus(_A)
_CmmFanRpmMin_Type=Integer32
_CmmFanRpmMin_Object=MibTableColumn
cmmFanRpmMin=_CmmFanRpmMin_Object((1,3,6,1,4,1,36673,100,1,2,9,1,3),_CmmFanRpmMin_Type())
cmmFanRpmMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanRpmMin.setStatus(_A)
_CmmFanRpmMax_Type=Integer32
_CmmFanRpmMax_Object=MibTableColumn
cmmFanRpmMax=_CmmFanRpmMax_Object((1,3,6,1,4,1,36673,100,1,2,9,1,4),_CmmFanRpmMax_Type())
cmmFanRpmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanRpmMax.setStatus(_A)
class _CmmFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_b,1),('running',2),('faulty',3),('stalled',4),(_F,5)))
_CmmFanStatus_Type.__name__=_E
_CmmFanStatus_Object=MibTableColumn
cmmFanStatus=_CmmFanStatus_Object((1,3,6,1,4,1,36673,100,1,2,9,1,5),_CmmFanStatus_Type())
cmmFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanStatus.setStatus(_A)
class _CmmFanLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('front',1),('rear',2),(_F,3),(_w,4)))
_CmmFanLocation_Type.__name__=_E
_CmmFanLocation_Object=MibTableColumn
cmmFanLocation=_CmmFanLocation_Object((1,3,6,1,4,1,36673,100,1,2,9,1,6),_CmmFanLocation_Type())
cmmFanLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanLocation.setStatus(_A)
_CmmSysTemperatureTable_Object=MibTable
cmmSysTemperatureTable=_CmmSysTemperatureTable_Object((1,3,6,1,4,1,36673,100,1,2,10))
if mibBuilder.loadTexts:cmmSysTemperatureTable.setStatus(_A)
_CmmSysTemperatureEntry_Object=MibTableRow
cmmSysTemperatureEntry=_CmmSysTemperatureEntry_Object((1,3,6,1,4,1,36673,100,1,2,10,1))
cmmSysTemperatureEntry.setIndexNames((0,_B,_D),(0,_B,_P))
if mibBuilder.loadTexts:cmmSysTemperatureEntry.setStatus(_A)
_CmmSysTemperatureSensorIndex_Type=Integer32
_CmmSysTemperatureSensorIndex_Object=MibTableColumn
cmmSysTemperatureSensorIndex=_CmmSysTemperatureSensorIndex_Object((1,3,6,1,4,1,36673,100,1,2,10,1,1),_CmmSysTemperatureSensorIndex_Type())
cmmSysTemperatureSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTemperatureSensorIndex.setStatus(_A)
_CmmSysTemperatureSensorName_Type=DisplayString
_CmmSysTemperatureSensorName_Object=MibTableColumn
cmmSysTemperatureSensorName=_CmmSysTemperatureSensorName_Object((1,3,6,1,4,1,36673,100,1,2,10,1,2),_CmmSysTemperatureSensorName_Type())
cmmSysTemperatureSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTemperatureSensorName.setStatus(_A)
_CmmSysTemperatureValue_Type=Integer32
_CmmSysTemperatureValue_Object=MibTableColumn
cmmSysTemperatureValue=_CmmSysTemperatureValue_Object((1,3,6,1,4,1,36673,100,1,2,10,1,3),_CmmSysTemperatureValue_Type())
cmmSysTemperatureValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTemperatureValue.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTemperatureValue.setUnits(_M)
_CmmSysTempEmergencyThresholdMin_Type=Integer32
_CmmSysTempEmergencyThresholdMin_Object=MibTableColumn
cmmSysTempEmergencyThresholdMin=_CmmSysTempEmergencyThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,10,1,4),_CmmSysTempEmergencyThresholdMin_Type())
cmmSysTempEmergencyThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTempEmergencyThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTempEmergencyThresholdMin.setUnits(_M)
_CmmSysTempEmergencyThresholdMax_Type=Integer32
_CmmSysTempEmergencyThresholdMax_Object=MibTableColumn
cmmSysTempEmergencyThresholdMax=_CmmSysTempEmergencyThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,10,1,5),_CmmSysTempEmergencyThresholdMax_Type())
cmmSysTempEmergencyThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTempEmergencyThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTempEmergencyThresholdMax.setUnits(_M)
_CmmSysTempAlertThresholdMin_Type=Integer32
_CmmSysTempAlertThresholdMin_Object=MibTableColumn
cmmSysTempAlertThresholdMin=_CmmSysTempAlertThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,10,1,6),_CmmSysTempAlertThresholdMin_Type())
cmmSysTempAlertThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTempAlertThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTempAlertThresholdMin.setUnits(_M)
_CmmSysTempAlertThresholdMax_Type=Integer32
_CmmSysTempAlertThresholdMax_Object=MibTableColumn
cmmSysTempAlertThresholdMax=_CmmSysTempAlertThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,10,1,7),_CmmSysTempAlertThresholdMax_Type())
cmmSysTempAlertThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTempAlertThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTempAlertThresholdMax.setUnits(_M)
_CmmSysTempCriticalThresholdMin_Type=Integer32
_CmmSysTempCriticalThresholdMin_Object=MibTableColumn
cmmSysTempCriticalThresholdMin=_CmmSysTempCriticalThresholdMin_Object((1,3,6,1,4,1,36673,100,1,2,10,1,8),_CmmSysTempCriticalThresholdMin_Type())
cmmSysTempCriticalThresholdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTempCriticalThresholdMin.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTempCriticalThresholdMin.setUnits(_M)
_CmmSysTempCriticalThresholdMax_Type=Integer32
_CmmSysTempCriticalThresholdMax_Object=MibTableColumn
cmmSysTempCriticalThresholdMax=_CmmSysTempCriticalThresholdMax_Object((1,3,6,1,4,1,36673,100,1,2,10,1,9),_CmmSysTempCriticalThresholdMax_Type())
cmmSysTempCriticalThresholdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTempCriticalThresholdMax.setStatus(_A)
if mibBuilder.loadTexts:cmmSysTempCriticalThresholdMax.setUnits(_M)
_CmmSysComponentStatusTable_Object=MibTable
cmmSysComponentStatusTable=_CmmSysComponentStatusTable_Object((1,3,6,1,4,1,36673,100,1,2,11))
if mibBuilder.loadTexts:cmmSysComponentStatusTable.setStatus(_A)
_CmmSysComponentStatusEntry_Object=MibTableRow
cmmSysComponentStatusEntry=_CmmSysComponentStatusEntry_Object((1,3,6,1,4,1,36673,100,1,2,11,1))
cmmSysComponentStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmSysComponentStatusEntry.setStatus(_A)
class _CmmSysPsu1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysPsu1Status_Type.__name__=_E
_CmmSysPsu1Status_Object=MibTableColumn
cmmSysPsu1Status=_CmmSysPsu1Status_Object((1,3,6,1,4,1,36673,100,1,2,11,1,1),_CmmSysPsu1Status_Type())
cmmSysPsu1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPsu1Status.setStatus(_A)
_CmmSysPsu1LedColor_Type=LedColorCode
_CmmSysPsu1LedColor_Object=MibTableColumn
cmmSysPsu1LedColor=_CmmSysPsu1LedColor_Object((1,3,6,1,4,1,36673,100,1,2,11,1,2),_CmmSysPsu1LedColor_Type())
cmmSysPsu1LedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPsu1LedColor.setStatus(_A)
class _CmmSysPsu2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysPsu2Status_Type.__name__=_E
_CmmSysPsu2Status_Object=MibTableColumn
cmmSysPsu2Status=_CmmSysPsu2Status_Object((1,3,6,1,4,1,36673,100,1,2,11,1,3),_CmmSysPsu2Status_Type())
cmmSysPsu2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPsu2Status.setStatus(_A)
_CmmSysPsu2LedColor_Type=LedColorCode
_CmmSysPsu2LedColor_Object=MibTableColumn
cmmSysPsu2LedColor=_CmmSysPsu2LedColor_Object((1,3,6,1,4,1,36673,100,1,2,11,1,4),_CmmSysPsu2LedColor_Type())
cmmSysPsu2LedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysPsu2LedColor.setStatus(_A)
class _CmmSysLocatorLedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),('on',2),('off',3),(_F,4)))
_CmmSysLocatorLedStatus_Type.__name__=_E
_CmmSysLocatorLedStatus_Object=MibTableColumn
cmmSysLocatorLedStatus=_CmmSysLocatorLedStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,5),_CmmSysLocatorLedStatus_Type())
cmmSysLocatorLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysLocatorLedStatus.setStatus(_A)
_CmmSysLocatorLedColor_Type=LedColorCode
_CmmSysLocatorLedColor_Object=MibTableColumn
cmmSysLocatorLedColor=_CmmSysLocatorLedColor_Object((1,3,6,1,4,1,36673,100,1,2,11,1,6),_CmmSysLocatorLedColor_Type())
cmmSysLocatorLedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysLocatorLedColor.setStatus(_A)
class _CmmSysMasterLedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),('on',2),('off',3),(_F,4)))
_CmmSysMasterLedStatus_Type.__name__=_E
_CmmSysMasterLedStatus_Object=MibTableColumn
cmmSysMasterLedStatus=_CmmSysMasterLedStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,7),_CmmSysMasterLedStatus_Type())
cmmSysMasterLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysMasterLedStatus.setStatus(_A)
_CmmSysMasterLedColor_Type=LedColorCode
_CmmSysMasterLedColor_Object=MibTableColumn
cmmSysMasterLedColor=_CmmSysMasterLedColor_Object((1,3,6,1,4,1,36673,100,1,2,11,1,8),_CmmSysMasterLedColor_Type())
cmmSysMasterLedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysMasterLedColor.setStatus(_A)
class _CmmSysFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysFanStatus_Type.__name__=_E
_CmmSysFanStatus_Object=MibTableColumn
cmmSysFanStatus=_CmmSysFanStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,9),_CmmSysFanStatus_Type())
cmmSysFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysFanStatus.setStatus(_A)
_CmmSysFrontFanLedColor_Type=LedColorCode
_CmmSysFrontFanLedColor_Object=MibTableColumn
cmmSysFrontFanLedColor=_CmmSysFrontFanLedColor_Object((1,3,6,1,4,1,36673,100,1,2,11,1,10),_CmmSysFrontFanLedColor_Type())
cmmSysFrontFanLedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysFrontFanLedColor.setStatus(_A)
class _CmmSysRamStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysRamStatus_Type.__name__=_E
_CmmSysRamStatus_Object=MibTableColumn
cmmSysRamStatus=_CmmSysRamStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,11),_CmmSysRamStatus_Type())
cmmSysRamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysRamStatus.setStatus(_A)
class _CmmSysCpuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysCpuStatus_Type.__name__=_E
_CmmSysCpuStatus_Object=MibTableColumn
cmmSysCpuStatus=_CmmSysCpuStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,12),_CmmSysCpuStatus_Type())
cmmSysCpuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysCpuStatus.setStatus(_A)
class _CmmSysDiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysDiskStatus_Type.__name__=_E
_CmmSysDiskStatus_Object=MibTableColumn
cmmSysDiskStatus=_CmmSysDiskStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,13),_CmmSysDiskStatus_Type())
cmmSysDiskStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysDiskStatus.setStatus(_A)
class _CmmSysTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysTemperatureStatus_Type.__name__=_E
_CmmSysTemperatureStatus_Object=MibTableColumn
cmmSysTemperatureStatus=_CmmSysTemperatureStatus_Object((1,3,6,1,4,1,36673,100,1,2,11,1,14),_CmmSysTemperatureStatus_Type())
cmmSysTemperatureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysTemperatureStatus.setStatus(_A)
_CmmSysSwModuleTable_Object=MibTable
cmmSysSwModuleTable=_CmmSysSwModuleTable_Object((1,3,6,1,4,1,36673,100,1,2,12))
if mibBuilder.loadTexts:cmmSysSwModuleTable.setStatus(_A)
_CmmSysSwModuleEntry_Object=MibTableRow
cmmSysSwModuleEntry=_CmmSysSwModuleEntry_Object((1,3,6,1,4,1,36673,100,1,2,12,1))
cmmSysSwModuleEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmSysSwModuleEntry.setStatus(_A)
_CmmSysSwRuntimeImgVersion_Type=DisplayString
_CmmSysSwRuntimeImgVersion_Object=MibTableColumn
cmmSysSwRuntimeImgVersion=_CmmSysSwRuntimeImgVersion_Object((1,3,6,1,4,1,36673,100,1,2,12,1,1),_CmmSysSwRuntimeImgVersion_Type())
cmmSysSwRuntimeImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysSwRuntimeImgVersion.setStatus(_A)
_CmmSysSwRuntimeImgDate_Type=DateAndTime
_CmmSysSwRuntimeImgDate_Object=MibTableColumn
cmmSysSwRuntimeImgDate=_CmmSysSwRuntimeImgDate_Object((1,3,6,1,4,1,36673,100,1,2,12,1,2),_CmmSysSwRuntimeImgDate_Type())
cmmSysSwRuntimeImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysSwRuntimeImgDate.setStatus(_A)
_CmmSwitchTemperatureTable_Object=MibTable
cmmSwitchTemperatureTable=_CmmSwitchTemperatureTable_Object((1,3,6,1,4,1,36673,100,1,2,13))
if mibBuilder.loadTexts:cmmSwitchTemperatureTable.setStatus(_A)
_CmmSwitchTemperatureEntry_Object=MibTableRow
cmmSwitchTemperatureEntry=_CmmSwitchTemperatureEntry_Object((1,3,6,1,4,1,36673,100,1,2,13,1))
cmmSwitchTemperatureEntry.setIndexNames((0,_B,_D),(0,_B,_Ao))
if mibBuilder.loadTexts:cmmSwitchTemperatureEntry.setStatus(_A)
_CmmSwitchTemperatureSensorIndex_Type=Integer32
_CmmSwitchTemperatureSensorIndex_Object=MibTableColumn
cmmSwitchTemperatureSensorIndex=_CmmSwitchTemperatureSensorIndex_Object((1,3,6,1,4,1,36673,100,1,2,13,1,1),_CmmSwitchTemperatureSensorIndex_Type())
cmmSwitchTemperatureSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSwitchTemperatureSensorIndex.setStatus(_A)
_CmmSwitchTemperatureValue_Type=Integer32
_CmmSwitchTemperatureValue_Object=MibTableColumn
cmmSwitchTemperatureValue=_CmmSwitchTemperatureValue_Object((1,3,6,1,4,1,36673,100,1,2,13,1,2),_CmmSwitchTemperatureValue_Type())
cmmSwitchTemperatureValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSwitchTemperatureValue.setStatus(_A)
if mibBuilder.loadTexts:cmmSwitchTemperatureValue.setUnits(_M)
_CmmSwitchTempPeakValue_Type=Integer32
_CmmSwitchTempPeakValue_Object=MibTableColumn
cmmSwitchTempPeakValue=_CmmSwitchTempPeakValue_Object((1,3,6,1,4,1,36673,100,1,2,13,1,3),_CmmSwitchTempPeakValue_Type())
cmmSwitchTempPeakValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSwitchTempPeakValue.setStatus(_A)
if mibBuilder.loadTexts:cmmSwitchTempPeakValue.setUnits(_M)
_CmmSysHardDiskTable_Object=MibTable
cmmSysHardDiskTable=_CmmSysHardDiskTable_Object((1,3,6,1,4,1,36673,100,1,2,14))
if mibBuilder.loadTexts:cmmSysHardDiskTable.setStatus(_A)
_CmmSysHardDiskEntry_Object=MibTableRow
cmmSysHardDiskEntry=_CmmSysHardDiskEntry_Object((1,3,6,1,4,1,36673,100,1,2,14,1))
cmmSysHardDiskEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmSysHardDiskEntry.setStatus(_A)
_CmmSysHarddiskSerialno_Type=DisplayString
_CmmSysHarddiskSerialno_Object=MibTableColumn
cmmSysHarddiskSerialno=_CmmSysHarddiskSerialno_Object((1,3,6,1,4,1,36673,100,1,2,14,1,1),_CmmSysHarddiskSerialno_Type())
cmmSysHarddiskSerialno.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskSerialno.setStatus(_A)
_CmmSysHarddiskModelno_Type=DisplayString
_CmmSysHarddiskModelno_Object=MibTableColumn
cmmSysHarddiskModelno=_CmmSysHarddiskModelno_Object((1,3,6,1,4,1,36673,100,1,2,14,1,2),_CmmSysHarddiskModelno_Type())
cmmSysHarddiskModelno.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskModelno.setStatus(_A)
_CmmSysHarddiskFirmwarerev_Type=DisplayString
_CmmSysHarddiskFirmwarerev_Object=MibTableColumn
cmmSysHarddiskFirmwarerev=_CmmSysHarddiskFirmwarerev_Object((1,3,6,1,4,1,36673,100,1,2,14,1,3),_CmmSysHarddiskFirmwarerev_Type())
cmmSysHarddiskFirmwarerev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskFirmwarerev.setStatus(_A)
_CmmSysHarddiskCylinders_Type=Integer32
_CmmSysHarddiskCylinders_Object=MibTableColumn
cmmSysHarddiskCylinders=_CmmSysHarddiskCylinders_Object((1,3,6,1,4,1,36673,100,1,2,14,1,4),_CmmSysHarddiskCylinders_Type())
cmmSysHarddiskCylinders.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskCylinders.setStatus(_A)
_CmmSysHarddiskHeads_Type=Integer32
_CmmSysHarddiskHeads_Object=MibTableColumn
cmmSysHarddiskHeads=_CmmSysHarddiskHeads_Object((1,3,6,1,4,1,36673,100,1,2,14,1,5),_CmmSysHarddiskHeads_Type())
cmmSysHarddiskHeads.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskHeads.setStatus(_A)
_CmmSysHarddiskSectors_Type=Integer32
_CmmSysHarddiskSectors_Object=MibTableColumn
cmmSysHarddiskSectors=_CmmSysHarddiskSectors_Object((1,3,6,1,4,1,36673,100,1,2,14,1,6),_CmmSysHarddiskSectors_Type())
cmmSysHarddiskSectors.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskSectors.setStatus(_A)
_CmmSysHarddiskUnformattedBytesorTrack_Type=Integer32
_CmmSysHarddiskUnformattedBytesorTrack_Object=MibTableColumn
cmmSysHarddiskUnformattedBytesorTrack=_CmmSysHarddiskUnformattedBytesorTrack_Object((1,3,6,1,4,1,36673,100,1,2,14,1,7),_CmmSysHarddiskUnformattedBytesorTrack_Type())
cmmSysHarddiskUnformattedBytesorTrack.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskUnformattedBytesorTrack.setStatus(_A)
_CmmSysHarddiskUnformattedBytesorSector_Type=Integer32
_CmmSysHarddiskUnformattedBytesorSector_Object=MibTableColumn
cmmSysHarddiskUnformattedBytesorSector=_CmmSysHarddiskUnformattedBytesorSector_Object((1,3,6,1,4,1,36673,100,1,2,14,1,8),_CmmSysHarddiskUnformattedBytesorSector_Type())
cmmSysHarddiskUnformattedBytesorSector.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskUnformattedBytesorSector.setStatus(_A)
_CmmSysHarddiskRevisionNum_Type=DisplayString
_CmmSysHarddiskRevisionNum_Object=MibTableColumn
cmmSysHarddiskRevisionNum=_CmmSysHarddiskRevisionNum_Object((1,3,6,1,4,1,36673,100,1,2,14,1,9),_CmmSysHarddiskRevisionNum_Type())
cmmSysHarddiskRevisionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskRevisionNum.setStatus(_A)
_CmmSysHarddiskTotalsize_Type=Integer32
_CmmSysHarddiskTotalsize_Object=MibTableColumn
cmmSysHarddiskTotalsize=_CmmSysHarddiskTotalsize_Object((1,3,6,1,4,1,36673,100,1,2,14,1,10),_CmmSysHarddiskTotalsize_Type())
cmmSysHarddiskTotalsize.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskTotalsize.setStatus(_A)
if mibBuilder.loadTexts:cmmSysHarddiskTotalsize.setUnits(' MBytes ')
_CmmSysHarddiskUsedMem_Type=Integer32
_CmmSysHarddiskUsedMem_Object=MibTableColumn
cmmSysHarddiskUsedMem=_CmmSysHarddiskUsedMem_Object((1,3,6,1,4,1,36673,100,1,2,14,1,11),_CmmSysHarddiskUsedMem_Type())
cmmSysHarddiskUsedMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskUsedMem.setStatus(_A)
if mibBuilder.loadTexts:cmmSysHarddiskUsedMem.setUnits(_W)
_CmmSysHarddiskFreeMem_Type=Integer32
_CmmSysHarddiskFreeMem_Object=MibTableColumn
cmmSysHarddiskFreeMem=_CmmSysHarddiskFreeMem_Object((1,3,6,1,4,1,36673,100,1,2,14,1,12),_CmmSysHarddiskFreeMem_Type())
cmmSysHarddiskFreeMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskFreeMem.setStatus(_A)
if mibBuilder.loadTexts:cmmSysHarddiskFreeMem.setUnits(_W)
_CmmSysHarddiskCriticalThreshold_Type=Integer32
_CmmSysHarddiskCriticalThreshold_Object=MibTableColumn
cmmSysHarddiskCriticalThreshold=_CmmSysHarddiskCriticalThreshold_Object((1,3,6,1,4,1,36673,100,1,2,14,1,13),_CmmSysHarddiskCriticalThreshold_Type())
cmmSysHarddiskCriticalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskCriticalThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmSysHarddiskCriticalThreshold.setUnits(_W)
_CmmSysHarddiskAlertThreshold_Type=Integer32
_CmmSysHarddiskAlertThreshold_Object=MibTableColumn
cmmSysHarddiskAlertThreshold=_CmmSysHarddiskAlertThreshold_Object((1,3,6,1,4,1,36673,100,1,2,14,1,14),_CmmSysHarddiskAlertThreshold_Type())
cmmSysHarddiskAlertThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysHarddiskAlertThreshold.setStatus(_A)
if mibBuilder.loadTexts:cmmSysHarddiskAlertThreshold.setUnits(_W)
_CmmSystemStatusTable_Object=MibTable
cmmSystemStatusTable=_CmmSystemStatusTable_Object((1,3,6,1,4,1,36673,100,1,2,15))
if mibBuilder.loadTexts:cmmSystemStatusTable.setStatus(_A)
_CmmSystemStatusEntry_Object=MibTableRow
cmmSystemStatusEntry=_CmmSystemStatusEntry_Object((1,3,6,1,4,1,36673,100,1,2,15,1))
cmmSystemStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cmmSystemStatusEntry.setStatus(_A)
_CmmSystemMinorFaultStatus_Type=SystemStatusCode
_CmmSystemMinorFaultStatus_Object=MibTableColumn
cmmSystemMinorFaultStatus=_CmmSystemMinorFaultStatus_Object((1,3,6,1,4,1,36673,100,1,2,15,1,1),_CmmSystemMinorFaultStatus_Type())
cmmSystemMinorFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSystemMinorFaultStatus.setStatus(_A)
_CmmSystemMajorFaultStatus_Type=SystemStatusCode
_CmmSystemMajorFaultStatus_Object=MibTableColumn
cmmSystemMajorFaultStatus=_CmmSystemMajorFaultStatus_Object((1,3,6,1,4,1,36673,100,1,2,15,1,2),_CmmSystemMajorFaultStatus_Type())
cmmSystemMajorFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSystemMajorFaultStatus.setStatus(_A)
class _CmmSysStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_Z,3),(_F,4)))
_CmmSysStatus_Type.__name__=_E
_CmmSysStatus_Object=MibTableColumn
cmmSysStatus=_CmmSysStatus_Object((1,3,6,1,4,1,36673,100,1,2,15,1,3),_CmmSysStatus_Type())
cmmSysStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysStatus.setStatus(_A)
_CmmSysLedColor_Type=LedColorCode
_CmmSysLedColor_Object=MibTableColumn
cmmSysLedColor=_CmmSysLedColor_Object((1,3,6,1,4,1,36673,100,1,2,15,1,4),_CmmSysLedColor_Type())
cmmSysLedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysLedColor.setStatus(_A)
_CmmCpuCoreUtilTable_Object=MibTable
cmmCpuCoreUtilTable=_CmmCpuCoreUtilTable_Object((1,3,6,1,4,1,36673,100,1,2,16))
if mibBuilder.loadTexts:cmmCpuCoreUtilTable.setStatus(_A)
_CmmCpuCoreUtilEntry_Object=MibTableRow
cmmCpuCoreUtilEntry=_CmmCpuCoreUtilEntry_Object((1,3,6,1,4,1,36673,100,1,2,16,1))
cmmCpuCoreUtilEntry.setIndexNames((0,_B,_D),(0,_B,_Ap))
if mibBuilder.loadTexts:cmmCpuCoreUtilEntry.setStatus(_A)
_CmmCpuCoreIndex_Type=Integer32
_CmmCpuCoreIndex_Object=MibTableColumn
cmmCpuCoreIndex=_CmmCpuCoreIndex_Object((1,3,6,1,4,1,36673,100,1,2,16,1,1),_CmmCpuCoreIndex_Type())
cmmCpuCoreIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:cmmCpuCoreIndex.setStatus(_A)
_CmmCpuCoreUtilization_Type=Integer32
_CmmCpuCoreUtilization_Object=MibTableColumn
cmmCpuCoreUtilization=_CmmCpuCoreUtilization_Object((1,3,6,1,4,1,36673,100,1,2,16,1,2),_CmmCpuCoreUtilization_Type())
cmmCpuCoreUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmCpuCoreUtilization.setStatus(_A)
if mibBuilder.loadTexts:cmmCpuCoreUtilization.setUnits(_Q)
_CmmCpuCoreModelName_Type=DisplayString
_CmmCpuCoreModelName_Object=MibTableColumn
cmmCpuCoreModelName=_CmmCpuCoreModelName_Object((1,3,6,1,4,1,36673,100,1,2,16,1,3),_CmmCpuCoreModelName_Type())
cmmCpuCoreModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmCpuCoreModelName.setStatus(_A)
_CmmPsuFruTable_Object=MibTable
cmmPsuFruTable=_CmmPsuFruTable_Object((1,3,6,1,4,1,36673,100,1,2,17))
if mibBuilder.loadTexts:cmmPsuFruTable.setStatus(_A)
_CmmPsuFruEntry_Object=MibTableRow
cmmPsuFruEntry=_CmmPsuFruEntry_Object((1,3,6,1,4,1,36673,100,1,2,17,1))
cmmPsuFruEntry.setIndexNames((0,_B,_D),(0,_B,_V))
if mibBuilder.loadTexts:cmmPsuFruEntry.setStatus(_A)
_CmmPsuPpid_Type=DisplayString
_CmmPsuPpid_Object=MibTableColumn
cmmPsuPpid=_CmmPsuPpid_Object((1,3,6,1,4,1,36673,100,1,2,17,1,1),_CmmPsuPpid_Type())
cmmPsuPpid.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuPpid.setStatus(_A)
_CmmPsuCountryofOrigin_Type=DisplayString
_CmmPsuCountryofOrigin_Object=MibTableColumn
cmmPsuCountryofOrigin=_CmmPsuCountryofOrigin_Object((1,3,6,1,4,1,36673,100,1,2,17,1,2),_CmmPsuCountryofOrigin_Type())
cmmPsuCountryofOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuCountryofOrigin.setStatus(_A)
_CmmPsuPpidPartNum_Type=DisplayString
_CmmPsuPpidPartNum_Object=MibTableColumn
cmmPsuPpidPartNum=_CmmPsuPpidPartNum_Object((1,3,6,1,4,1,36673,100,1,2,17,1,3),_CmmPsuPpidPartNum_Type())
cmmPsuPpidPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuPpidPartNum.setStatus(_A)
_CmmPsuPpidPartNumRev_Type=DisplayString
_CmmPsuPpidPartNumRev_Object=MibTableColumn
cmmPsuPpidPartNumRev=_CmmPsuPpidPartNumRev_Object((1,3,6,1,4,1,36673,100,1,2,17,1,4),_CmmPsuPpidPartNumRev_Type())
cmmPsuPpidPartNumRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuPpidPartNumRev.setStatus(_A)
_CmmPsuManufactureId_Type=DisplayString
_CmmPsuManufactureId_Object=MibTableColumn
cmmPsuManufactureId=_CmmPsuManufactureId_Object((1,3,6,1,4,1,36673,100,1,2,17,1,5),_CmmPsuManufactureId_Type())
cmmPsuManufactureId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuManufactureId.setStatus(_A)
class _CmmPsuDateCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(11,11))
_CmmPsuDateCode_Type.__name__=_a
_CmmPsuDateCode_Object=MibTableColumn
cmmPsuDateCode=_CmmPsuDateCode_Object((1,3,6,1,4,1,36673,100,1,2,17,1,6),_CmmPsuDateCode_Type())
cmmPsuDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuDateCode.setStatus(_A)
_CmmPsuSerialNumber_Type=DisplayString
_CmmPsuSerialNumber_Object=MibTableColumn
cmmPsuSerialNumber=_CmmPsuSerialNumber_Object((1,3,6,1,4,1,36673,100,1,2,17,1,7),_CmmPsuSerialNumber_Type())
cmmPsuSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuSerialNumber.setStatus(_A)
_CmmPsuPartNum_Type=DisplayString
_CmmPsuPartNum_Object=MibTableColumn
cmmPsuPartNum=_CmmPsuPartNum_Object((1,3,6,1,4,1,36673,100,1,2,17,1,8),_CmmPsuPartNum_Type())
cmmPsuPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuPartNum.setStatus(_A)
_CmmPsuPartNumRev_Type=DisplayString
_CmmPsuPartNumRev_Object=MibTableColumn
cmmPsuPartNumRev=_CmmPsuPartNumRev_Object((1,3,6,1,4,1,36673,100,1,2,17,1,9),_CmmPsuPartNumRev_Type())
cmmPsuPartNumRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuPartNumRev.setStatus(_A)
_CmmPsuNumOfFanPerTray_Type=Integer32
_CmmPsuNumOfFanPerTray_Object=MibTableColumn
cmmPsuNumOfFanPerTray=_CmmPsuNumOfFanPerTray_Object((1,3,6,1,4,1,36673,100,1,2,17,1,10),_CmmPsuNumOfFanPerTray_Type())
cmmPsuNumOfFanPerTray.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuNumOfFanPerTray.setStatus(_A)
class _CmmPsuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Ak,1),(_Al,2),(_Am,3),(_An,4),(_w,5)))
_CmmPsuType_Type.__name__=_E
_CmmPsuType_Object=MibTableColumn
cmmPsuType=_CmmPsuType_Object((1,3,6,1,4,1,36673,100,1,2,17,1,11),_CmmPsuType_Type())
cmmPsuType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuType.setStatus(_A)
_CmmPsuServiceTag_Type=DisplayString
_CmmPsuServiceTag_Object=MibTableColumn
cmmPsuServiceTag=_CmmPsuServiceTag_Object((1,3,6,1,4,1,36673,100,1,2,17,1,12),_CmmPsuServiceTag_Type())
cmmPsuServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuServiceTag.setStatus(_A)
_CmmPsuIanaNum_Type=DisplayString
_CmmPsuIanaNum_Object=MibTableColumn
cmmPsuIanaNum=_CmmPsuIanaNum_Object((1,3,6,1,4,1,36673,100,1,2,17,1,13),_CmmPsuIanaNum_Type())
cmmPsuIanaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuIanaNum.setStatus(_A)
_CmmPsuFanMaxRpm_Type=Integer32
_CmmPsuFanMaxRpm_Object=MibTableColumn
cmmPsuFanMaxRpm=_CmmPsuFanMaxRpm_Object((1,3,6,1,4,1,36673,100,1,2,17,1,14),_CmmPsuFanMaxRpm_Type())
cmmPsuFanMaxRpm.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuFanMaxRpm.setStatus(_A)
_CmmPsuAirFlowDir_Type=DisplayString
_CmmPsuAirFlowDir_Object=MibTableColumn
cmmPsuAirFlowDir=_CmmPsuAirFlowDir_Object((1,3,6,1,4,1,36673,100,1,2,17,1,15),_CmmPsuAirFlowDir_Type())
cmmPsuAirFlowDir.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuAirFlowDir.setStatus(_A)
_CmmPsuMaxOutputWatt_Type=Integer32
_CmmPsuMaxOutputWatt_Object=MibTableColumn
cmmPsuMaxOutputWatt=_CmmPsuMaxOutputWatt_Object((1,3,6,1,4,1,36673,100,1,2,17,1,16),_CmmPsuMaxOutputWatt_Type())
cmmPsuMaxOutputWatt.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmPsuMaxOutputWatt.setStatus(_A)
_CmmFanFruTable_Object=MibTable
cmmFanFruTable=_CmmFanFruTable_Object((1,3,6,1,4,1,36673,100,1,2,18))
if mibBuilder.loadTexts:cmmFanFruTable.setStatus(_A)
_CmmFanFruEntry_Object=MibTableRow
cmmFanFruEntry=_CmmFanFruEntry_Object((1,3,6,1,4,1,36673,100,1,2,18,1))
cmmFanFruEntry.setIndexNames((0,_B,_D),(0,_B,_O))
if mibBuilder.loadTexts:cmmFanFruEntry.setStatus(_A)
_CmmFanPpid_Type=DisplayString
_CmmFanPpid_Object=MibTableColumn
cmmFanPpid=_CmmFanPpid_Object((1,3,6,1,4,1,36673,100,1,2,18,1,1),_CmmFanPpid_Type())
cmmFanPpid.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanPpid.setStatus(_A)
_CmmFanCountryofOrigin_Type=DisplayString
_CmmFanCountryofOrigin_Object=MibTableColumn
cmmFanCountryofOrigin=_CmmFanCountryofOrigin_Object((1,3,6,1,4,1,36673,100,1,2,18,1,2),_CmmFanCountryofOrigin_Type())
cmmFanCountryofOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanCountryofOrigin.setStatus(_A)
_CmmFanPpidPartNum_Type=DisplayString
_CmmFanPpidPartNum_Object=MibTableColumn
cmmFanPpidPartNum=_CmmFanPpidPartNum_Object((1,3,6,1,4,1,36673,100,1,2,18,1,3),_CmmFanPpidPartNum_Type())
cmmFanPpidPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanPpidPartNum.setStatus(_A)
_CmmFanPpidPartNumRev_Type=DisplayString
_CmmFanPpidPartNumRev_Object=MibTableColumn
cmmFanPpidPartNumRev=_CmmFanPpidPartNumRev_Object((1,3,6,1,4,1,36673,100,1,2,18,1,4),_CmmFanPpidPartNumRev_Type())
cmmFanPpidPartNumRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanPpidPartNumRev.setStatus(_A)
_CmmFanManufactureId_Type=DisplayString
_CmmFanManufactureId_Object=MibTableColumn
cmmFanManufactureId=_CmmFanManufactureId_Object((1,3,6,1,4,1,36673,100,1,2,18,1,5),_CmmFanManufactureId_Type())
cmmFanManufactureId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanManufactureId.setStatus(_A)
_CmmFanDateCode_Type=DisplayString
_CmmFanDateCode_Object=MibTableColumn
cmmFanDateCode=_CmmFanDateCode_Object((1,3,6,1,4,1,36673,100,1,2,18,1,6),_CmmFanDateCode_Type())
cmmFanDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanDateCode.setStatus(_A)
_CmmFanSerialNumber_Type=DisplayString
_CmmFanSerialNumber_Object=MibTableColumn
cmmFanSerialNumber=_CmmFanSerialNumber_Object((1,3,6,1,4,1,36673,100,1,2,18,1,7),_CmmFanSerialNumber_Type())
cmmFanSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanSerialNumber.setStatus(_A)
_CmmFanPartNum_Type=DisplayString
_CmmFanPartNum_Object=MibTableColumn
cmmFanPartNum=_CmmFanPartNum_Object((1,3,6,1,4,1,36673,100,1,2,18,1,8),_CmmFanPartNum_Type())
cmmFanPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanPartNum.setStatus(_A)
_CmmFanPartNumRev_Type=DisplayString
_CmmFanPartNumRev_Object=MibTableColumn
cmmFanPartNumRev=_CmmFanPartNumRev_Object((1,3,6,1,4,1,36673,100,1,2,18,1,9),_CmmFanPartNumRev_Type())
cmmFanPartNumRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanPartNumRev.setStatus(_A)
_CmmFanNumOfFanPerTray_Type=Integer32
_CmmFanNumOfFanPerTray_Object=MibTableColumn
cmmFanNumOfFanPerTray=_CmmFanNumOfFanPerTray_Object((1,3,6,1,4,1,36673,100,1,2,18,1,10),_CmmFanNumOfFanPerTray_Type())
cmmFanNumOfFanPerTray.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanNumOfFanPerTray.setStatus(_A)
class _CmmFanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blow-outfan',1),('blow-infan',2),(_w,3)))
_CmmFanType_Type.__name__=_E
_CmmFanType_Object=MibTableColumn
cmmFanType=_CmmFanType_Object((1,3,6,1,4,1,36673,100,1,2,18,1,11),_CmmFanType_Type())
cmmFanType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanType.setStatus(_A)
_CmmFanServiceTag_Type=DisplayString
_CmmFanServiceTag_Object=MibTableColumn
cmmFanServiceTag=_CmmFanServiceTag_Object((1,3,6,1,4,1,36673,100,1,2,18,1,12),_CmmFanServiceTag_Type())
cmmFanServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanServiceTag.setStatus(_A)
_CmmFanIanaNum_Type=DisplayString
_CmmFanIanaNum_Object=MibTableColumn
cmmFanIanaNum=_CmmFanIanaNum_Object((1,3,6,1,4,1,36673,100,1,2,18,1,13),_CmmFanIanaNum_Type())
cmmFanIanaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanIanaNum.setStatus(_A)
_CmmFanMaxRpm_Type=Integer32
_CmmFanMaxRpm_Object=MibTableColumn
cmmFanMaxRpm=_CmmFanMaxRpm_Object((1,3,6,1,4,1,36673,100,1,2,18,1,14),_CmmFanMaxRpm_Type())
cmmFanMaxRpm.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmFanMaxRpm.setStatus(_A)
_CmmSysCpldTable_Object=MibTable
cmmSysCpldTable=_CmmSysCpldTable_Object((1,3,6,1,4,1,36673,100,1,2,19))
if mibBuilder.loadTexts:cmmSysCpldTable.setStatus(_A)
_CmmSysCpldEntry_Object=MibTableRow
cmmSysCpldEntry=_CmmSysCpldEntry_Object((1,3,6,1,4,1,36673,100,1,2,19,1))
cmmSysCpldEntry.setIndexNames((0,_B,_D),(0,_B,_Aq))
if mibBuilder.loadTexts:cmmSysCpldEntry.setStatus(_A)
_CmmSysCpldIndex_Type=Integer32
_CmmSysCpldIndex_Object=MibTableColumn
cmmSysCpldIndex=_CmmSysCpldIndex_Object((1,3,6,1,4,1,36673,100,1,2,19,1,1),_CmmSysCpldIndex_Type())
cmmSysCpldIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:cmmSysCpldIndex.setStatus(_A)
_CmmSysCpldName_Type=DisplayString
_CmmSysCpldName_Object=MibTableColumn
cmmSysCpldName=_CmmSysCpldName_Object((1,3,6,1,4,1,36673,100,1,2,19,1,2),_CmmSysCpldName_Type())
cmmSysCpldName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysCpldName.setStatus(_A)
_CmmSysCpldSupportedVer_Type=DisplayString
_CmmSysCpldSupportedVer_Object=MibTableColumn
cmmSysCpldSupportedVer=_CmmSysCpldSupportedVer_Object((1,3,6,1,4,1,36673,100,1,2,19,1,3),_CmmSysCpldSupportedVer_Type())
cmmSysCpldSupportedVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysCpldSupportedVer.setStatus(_A)
_CmmSysCpldCurrentVer_Type=DisplayString
_CmmSysCpldCurrentVer_Object=MibTableColumn
cmmSysCpldCurrentVer=_CmmSysCpldCurrentVer_Object((1,3,6,1,4,1,36673,100,1,2,19,1,4),_CmmSysCpldCurrentVer_Type())
cmmSysCpldCurrentVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSysCpldCurrentVer.setStatus(_A)
_CmmAlarmObjects_ObjectIdentity=ObjectIdentity
cmmAlarmObjects=_CmmAlarmObjects_ObjectIdentity((1,3,6,1,4,1,36673,100,1,3))
_CmmAlarmVariable_ObjectIdentity=ObjectIdentity
cmmAlarmVariable=_CmmAlarmVariable_ObjectIdentity((1,3,6,1,4,1,36673,100,1,3,0))
_CmmAlarmVarInteger_Type=Integer32
_CmmAlarmVarInteger_Object=MibScalar
cmmAlarmVarInteger=_CmmAlarmVarInteger_Object((1,3,6,1,4,1,36673,100,1,3,0,1),_CmmAlarmVarInteger_Type())
cmmAlarmVarInteger.setMaxAccess(_Ar)
if mibBuilder.loadTexts:cmmAlarmVarInteger.setStatus(_A)
_CmmAlarmVarString_Type=OctetString
_CmmAlarmVarString_Object=MibScalar
cmmAlarmVarString=_CmmAlarmVarString_Object((1,3,6,1,4,1,36673,100,1,3,0,2),_CmmAlarmVarString_Type())
cmmAlarmVarString.setMaxAccess(_Ar)
if mibBuilder.loadTexts:cmmAlarmVarString.setStatus(_A)
_CmmAlarmMibNotifications_ObjectIdentity=ObjectIdentity
cmmAlarmMibNotifications=_CmmAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,36673,100,1,3,1))
_CmmTransMibNotifications_ObjectIdentity=ObjectIdentity
cmmTransMibNotifications=_CmmTransMibNotifications_ObjectIdentity((1,3,6,1,4,1,36673,100,1,3,2))
cmmCpuLoad15MinCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,1))
cmmCpuLoad15MinCritical.setObjects(*((_B,_D),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cmmCpuLoad15MinCritical.setStatus(_A)
cmmCpuLoad5MinCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,2))
cmmCpuLoad5MinCritical.setObjects(*((_B,_D),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cmmCpuLoad5MinCritical.setStatus(_A)
cmmCpuLoad1MinAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,3))
cmmCpuLoad1MinAlert.setObjects(*((_B,_D),(_B,_A1),(_B,_k)))
if mibBuilder.loadTexts:cmmCpuLoad1MinAlert.setStatus(_A)
cmmCpuLoad1MinCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,4))
cmmCpuLoad1MinCritical.setObjects(*((_B,_D),(_B,_A2),(_B,_k)))
if mibBuilder.loadTexts:cmmCpuLoad1MinCritical.setStatus(_A)
cmmCpuLoad1MinAlertRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,5))
cmmCpuLoad1MinAlertRecovery.setObjects(*((_B,_D),(_B,_A1),(_B,_k)))
if mibBuilder.loadTexts:cmmCpuLoad1MinAlertRecovery.setStatus(_A)
cmmCpuLoad15MinCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,6))
cmmCpuLoad15MinCriticalRecovery.setObjects(*((_B,_D),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cmmCpuLoad15MinCriticalRecovery.setStatus(_A)
cmmCpuLoad5MinCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,7))
cmmCpuLoad5MinCriticalRecovery.setObjects(*((_B,_D),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cmmCpuLoad5MinCriticalRecovery.setStatus(_A)
cmmCpuLoad1MinCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,8))
cmmCpuLoad1MinCriticalRecovery.setObjects(*((_B,_D),(_B,_A2),(_B,_k)))
if mibBuilder.loadTexts:cmmCpuLoad1MinCriticalRecovery.setStatus(_A)
cmmCpuCoreUtilHighAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,9))
cmmCpuCoreUtilHighAlert.setObjects(*((_B,_D),(_B,_As),(_B,_l)))
if mibBuilder.loadTexts:cmmCpuCoreUtilHighAlert.setStatus(_A)
cmmCpuCoreUtilHighCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,10))
cmmCpuCoreUtilHighCritical.setObjects(*((_B,_D),(_B,_At),(_B,_l)))
if mibBuilder.loadTexts:cmmCpuCoreUtilHighCritical.setStatus(_A)
cmmCpuCoreUtilHighAlertRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,11))
cmmCpuCoreUtilHighAlertRecovery.setObjects(*((_B,_D),(_B,_l)))
if mibBuilder.loadTexts:cmmCpuCoreUtilHighAlertRecovery.setStatus(_A)
cmmCpuCoreUtilHighCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,12))
cmmCpuCoreUtilHighCriticalRecovery.setObjects(*((_B,_D),(_B,_l)))
if mibBuilder.loadTexts:cmmCpuCoreUtilHighCriticalRecovery.setStatus(_A)
cmmRamUsageRisingAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,21))
cmmRamUsageRisingAlert.setObjects(*((_B,_D),(_B,_m),(_B,_A3)))
if mibBuilder.loadTexts:cmmRamUsageRisingAlert.setStatus(_A)
cmmRamUsageRisingCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,22))
cmmRamUsageRisingCritical.setObjects(*((_B,_D),(_B,_m),(_B,_A4)))
if mibBuilder.loadTexts:cmmRamUsageRisingCritical.setStatus(_A)
cmmRamUsageAlertRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,23))
cmmRamUsageAlertRecovery.setObjects(*((_B,_D),(_B,_m),(_B,_A3)))
if mibBuilder.loadTexts:cmmRamUsageAlertRecovery.setStatus(_A)
cmmRamUsageCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,24))
cmmRamUsageCriticalRecovery.setObjects(*((_B,_D),(_B,_m),(_B,_A4)))
if mibBuilder.loadTexts:cmmRamUsageCriticalRecovery.setStatus(_A)
cmmHardDiskUsageRisingAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,25))
cmmHardDiskUsageRisingAlert.setObjects(*((_B,_D),(_B,_n),(_B,_A5)))
if mibBuilder.loadTexts:cmmHardDiskUsageRisingAlert.setStatus(_A)
cmmHardDiskUsageRisingCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,26))
cmmHardDiskUsageRisingCritical.setObjects(*((_B,_D),(_B,_n),(_B,_A6)))
if mibBuilder.loadTexts:cmmHardDiskUsageRisingCritical.setStatus(_A)
cmmHardDiskUsageAlertRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,27))
cmmHardDiskUsageAlertRecovery.setObjects(*((_B,_D),(_B,_n),(_B,_A5)))
if mibBuilder.loadTexts:cmmHardDiskUsageAlertRecovery.setStatus(_A)
cmmHardDiskUsageCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,28))
cmmHardDiskUsageCriticalRecovery.setObjects(*((_B,_D),(_B,_n),(_B,_A6)))
if mibBuilder.loadTexts:cmmHardDiskUsageCriticalRecovery.setStatus(_A)
cmmTemperatureLowEmergency=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,31))
cmmTemperatureLowEmergency.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_A7),(_B,_A8),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureLowEmergency.setStatus(_A)
cmmTemperatureHighEmergency=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,32))
cmmTemperatureHighEmergency.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_A7),(_B,_A8),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureHighEmergency.setStatus(_A)
cmmTemperatureLowAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,33))
cmmTemperatureLowAlert.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_o),(_B,_p),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureLowAlert.setStatus(_A)
cmmTemperatureHighAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,34))
cmmTemperatureHighAlert.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_o),(_B,_p),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureHighAlert.setStatus(_A)
cmmTemperatureLowCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,35))
cmmTemperatureLowCritical.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_q),(_B,_r),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureLowCritical.setStatus(_A)
cmmTemperatureHighCritical=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,36))
cmmTemperatureHighCritical.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_q),(_B,_r),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureHighCritical.setStatus(_A)
cmmTemperatureHighAlertRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,37))
cmmTemperatureHighAlertRecovery.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_o),(_B,_p),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureHighAlertRecovery.setStatus(_A)
cmmTemperatureLowAlertRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,38))
cmmTemperatureLowAlertRecovery.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_o),(_B,_p),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureLowAlertRecovery.setStatus(_A)
cmmTemperatureHighCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,39))
cmmTemperatureHighCriticalRecovery.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_q),(_B,_r),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureHighCriticalRecovery.setStatus(_A)
cmmTemperatureLowCriticalRecovery=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,40))
cmmTemperatureLowCriticalRecovery.setObjects(*((_B,_D),(_B,_P),(_B,_R),(_B,_q),(_B,_r),(_B,_S)))
if mibBuilder.loadTexts:cmmTemperatureLowCriticalRecovery.setStatus(_A)
cmmPsuInsertedNotify=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,41))
cmmPsuInsertedNotify.setObjects(*((_B,_D),(_B,_V),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cmmPsuInsertedNotify.setStatus(_A)
cmmPsuRemovedAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,42))
cmmPsuRemovedAlert.setObjects(*((_B,_D),(_B,_V),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cmmPsuRemovedAlert.setStatus(_A)
cmmPsuAcFailedAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,43))
cmmPsuAcFailedAlert.setObjects(*((_B,_D),(_B,_V)))
if mibBuilder.loadTexts:cmmPsuAcFailedAlert.setStatus(_A)
cmmPsuAcRecover=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,44))
cmmPsuAcRecover.setObjects(*((_B,_D),(_B,_V)))
if mibBuilder.loadTexts:cmmPsuAcRecover.setStatus(_A)
cmmPsu12vPgFailedAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,45))
cmmPsu12vPgFailedAlert.setObjects(*((_B,_D),(_B,_V)))
if mibBuilder.loadTexts:cmmPsu12vPgFailedAlert.setStatus(_A)
cmmPsu12vPgRecover=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,46))
cmmPsu12vPgRecover.setObjects(*((_B,_D),(_B,_V)))
if mibBuilder.loadTexts:cmmPsu12vPgRecover.setStatus(_A)
cmmFanTrayInsertedNotify=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,51))
cmmFanTrayInsertedNotify.setObjects(*((_B,_D),(_B,_O),(_B,_AB)))
if mibBuilder.loadTexts:cmmFanTrayInsertedNotify.setStatus(_A)
cmmFanTrayRemovedAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,52))
cmmFanTrayRemovedAlert.setObjects(*((_B,_D),(_B,_O),(_B,_AB)))
if mibBuilder.loadTexts:cmmFanTrayRemovedAlert.setStatus(_A)
cmmFanTrayFaultyAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,53))
cmmFanTrayFaultyAlert.setObjects(*((_B,_D),(_B,_O),(_B,_X)))
if mibBuilder.loadTexts:cmmFanTrayFaultyAlert.setStatus(_A)
cmmFanTrayRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,54))
cmmFanTrayRecovered.setObjects(*((_B,_D),(_B,_O),(_B,_X)))
if mibBuilder.loadTexts:cmmFanTrayRecovered.setStatus(_A)
cmmFanTrayStallAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,55))
cmmFanTrayStallAlert.setObjects(*((_B,_D),(_B,_O),(_B,_X)))
if mibBuilder.loadTexts:cmmFanTrayStallAlert.setStatus(_A)
cmmFanTrayStallRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,56))
cmmFanTrayStallRecovered.setObjects(*((_B,_D),(_B,_O),(_B,_X)))
if mibBuilder.loadTexts:cmmFanTrayStallRecovered.setStatus(_A)
cmmFanRPMMinAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,57))
cmmFanRPMMinAlert.setObjects(*((_B,_D),(_B,_O),(_B,_X),(_B,_Au)))
if mibBuilder.loadTexts:cmmFanRPMMinAlert.setStatus(_A)
cmmFanRPMMaxAlert=NotificationType((1,3,6,1,4,1,36673,100,1,3,1,58))
cmmFanRPMMaxAlert.setObjects(*((_B,_D),(_B,_O),(_B,_X),(_B,_Av)))
if mibBuilder.loadTexts:cmmFanRPMMaxAlert.setStatus(_A)
cmmTransCriticalTempHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,1))
cmmTransCriticalTempHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_c),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cmmTransCriticalTempHigh.setStatus(_A)
cmmTransCriticalTempLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,2))
cmmTransCriticalTempLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_c),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cmmTransCriticalTempLow.setStatus(_A)
cmmTransAlertTempHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,3))
cmmTransAlertTempHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_c),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:cmmTransAlertTempHigh.setStatus(_A)
cmmTransAlertTempLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,4))
cmmTransAlertTempLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_c),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:cmmTransAlertTempLow.setStatus(_A)
cmmTransNotifyTransceiverTempRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,5))
cmmTransNotifyTransceiverTempRecovered.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_c)))
if mibBuilder.loadTexts:cmmTransNotifyTransceiverTempRecovered.setStatus(_A)
cmmTransCriticalVoltageHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,11))
cmmTransCriticalVoltageHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_d),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cmmTransCriticalVoltageHigh.setStatus(_A)
cmmTransCriticalVoltageLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,12))
cmmTransCriticalVoltageLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_d),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cmmTransCriticalVoltageLow.setStatus(_A)
cmmTransAlertVoltageHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,13))
cmmTransAlertVoltageHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_d),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cmmTransAlertVoltageHigh.setStatus(_A)
cmmTransAlertVoltageLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,14))
cmmTransAlertVoltageLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_d),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cmmTransAlertVoltageLow.setStatus(_A)
cmmTransNotifyTransceiverVoltRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,15))
cmmTransNotifyTransceiverVoltRecovered.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_d)))
if mibBuilder.loadTexts:cmmTransNotifyTransceiverVoltRecovered.setStatus(_A)
cmmTransCriticalBiasHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,21))
cmmTransCriticalBiasHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_e),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:cmmTransCriticalBiasHigh.setStatus(_A)
cmmTransCriticalBiasLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,22))
cmmTransCriticalBiasLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_e),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:cmmTransCriticalBiasLow.setStatus(_A)
cmmTransAlertBiashigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,23))
cmmTransAlertBiashigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_e),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:cmmTransAlertBiashigh.setStatus(_A)
cmmTransAlertBiasLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,24))
cmmTransAlertBiasLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_e),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:cmmTransAlertBiasLow.setStatus(_A)
cmmTransNotifyTransceiverBiasRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,25))
cmmTransNotifyTransceiverBiasRecovered.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_e)))
if mibBuilder.loadTexts:cmmTransNotifyTransceiverBiasRecovered.setStatus(_A)
cmmTransCriticalRxPowerHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,31))
cmmTransCriticalRxPowerHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_f),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:cmmTransCriticalRxPowerHigh.setStatus(_A)
cmmTransCriticalRxPowerLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,32))
cmmTransCriticalRxPowerLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_f),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:cmmTransCriticalRxPowerLow.setStatus(_A)
cmmTransAlertRxPowerHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,33))
cmmTransAlertRxPowerHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_f),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:cmmTransAlertRxPowerHigh.setStatus(_A)
cmmTransAlertRxPowerLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,34))
cmmTransAlertRxPowerLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_f),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:cmmTransAlertRxPowerLow.setStatus(_A)
cmmTransNotifyTransceiverRxPowRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,35))
cmmTransNotifyTransceiverRxPowRecovered.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_f)))
if mibBuilder.loadTexts:cmmTransNotifyTransceiverRxPowRecovered.setStatus(_A)
cmmTransCriticalTxPowerHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,41))
cmmTransCriticalTxPowerHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_g),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:cmmTransCriticalTxPowerHigh.setStatus(_A)
cmmTransCriticalTxPowerLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,42))
cmmTransCriticalTxPowerLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_g),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:cmmTransCriticalTxPowerLow.setStatus(_A)
cmmTransAlertTxPowerHigh=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,43))
cmmTransAlertTxPowerHigh.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_g),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:cmmTransAlertTxPowerHigh.setStatus(_A)
cmmTransAlertTxPowerLow=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,44))
cmmTransAlertTxPowerLow.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_g),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:cmmTransAlertTxPowerLow.setStatus(_A)
cmmTransNotifyTransceiverTxPowRecovered=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,45))
cmmTransNotifyTransceiverTxPowRecovered.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_L),(_B,_g)))
if mibBuilder.loadTexts:cmmTransNotifyTransceiverTxPowRecovered.setStatus(_A)
cmmTransNotifyTransceiverInserted=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,51))
cmmTransNotifyTransceiverInserted.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:cmmTransNotifyTransceiverInserted.setStatus(_A)
cmmTransAlertTransceiverRemoved=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,52))
cmmTransAlertTransceiverRemoved.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:cmmTransAlertTransceiverRemoved.setStatus(_A)
cmmTransAlertFaultyTransceiverInserted=NotificationType((1,3,6,1,4,1,36673,100,1,3,2,53))
cmmTransAlertFaultyTransceiverInserted.setObjects(*((_B,_D),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cmmTransAlertFaultyTransceiverInserted.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LedColorCode':LedColorCode,'SystemStatusCode':SystemStatusCode,'cmm':cmm,'CmmChassisObject':CmmChassisObject,'cmmObjects':cmmObjects,'cmmNumStackUnits':cmmNumStackUnits,'cmmSysObjects':cmmSysObjects,'cmmStackUnitTable':cmmStackUnitTable,'cmmStackUnitEntry':cmmStackUnitEntry,_D:cmmStackUnitIndex,'cmmStackUnitModelName':cmmStackUnitModelName,'cmmStackUnitSerialNumber':cmmStackUnitSerialNumber,'cmmStackUnitUpTime':cmmStackUnitUpTime,'cmmStackUnitMfgDate':cmmStackUnitMfgDate,'cmmStackUnitMacAddress':cmmStackUnitMacAddress,'cmmStackUnitPartNum':cmmStackUnitPartNum,'cmmStackLabelRevision':cmmStackLabelRevision,'cmmStackUnitCountryCode':cmmStackUnitCountryCode,'cmmStackUnitServiceTag':cmmStackUnitServiceTag,'cmmStackPlatformName':cmmStackPlatformName,'cmmStackOnieVersion':cmmStackOnieVersion,'cmmStackMfgName':cmmStackMfgName,'cmmStackVendorName':cmmStackVendorName,'cmmStackDiagVersion':cmmStackDiagVersion,'cmmStackCrc32':cmmStackCrc32,'cmmStackUnitNumFanControllers':cmmStackUnitNumFanControllers,'cmmStackUnitNumFanTrays':cmmStackUnitNumFanTrays,'cmmStackUnitNumPowerSupplies':cmmStackUnitNumPowerSupplies,'cmmStackUnitNumPluggableModules':cmmStackUnitNumPluggableModules,'cmmStackUnitNumFastEtherPorts':cmmStackUnitNumFastEtherPorts,'cmmStackUnitNumGigEtherPorts':cmmStackUnitNumGigEtherPorts,'cmmStackUnitNum10GigEtherPorts':cmmStackUnitNum10GigEtherPorts,'cmmStackUnitNum25GigEtherPorts':cmmStackUnitNum25GigEtherPorts,'cmmStackUnitNum40GigEtherPorts':cmmStackUnitNum40GigEtherPorts,'cmmStackUnitNum50GigEtherPorts':cmmStackUnitNum50GigEtherPorts,'cmmStackUnitNum100GigEtherPorts':cmmStackUnitNum100GigEtherPorts,'cmmStackUnitSwitchChipRev':cmmStackUnitSwitchChipRev,'cmmStackSupportedLabelRevision':cmmStackSupportedLabelRevision,'cmmStackUnitSupportedSwitchChipRev':cmmStackUnitSupportedSwitchChipRev,'cmmTransEEPROMTable':cmmTransEEPROMTable,'cmmTransEEPROMEntry':cmmTransEEPROMEntry,_G:cmmTransIndex,_H:cmmTransType,'cmmTransNoOfChannels':cmmTransNoOfChannels,'cmmTransidentifier':cmmTransidentifier,'cmmTransSFPextendedidentifier':cmmTransSFPextendedidentifier,'cmmTransQSFPextendedidentifier':cmmTransQSFPextendedidentifier,'cmmTransconnectortype':cmmTransconnectortype,'cmmTransEthCompliance':cmmTransEthCompliance,'cmmTransExtEthCompliance':cmmTransExtEthCompliance,'cmmTransSonetCompliance':cmmTransSonetCompliance,'cmmTransFiberChnlLinkLen':cmmTransFiberChnlLinkLen,'cmmTransFiberChnlTransTech':cmmTransFiberChnlTransTech,'cmmTransFiberChnlTransMedia':cmmTransFiberChnlTransMedia,'cmmTransSFPFiberChnlSpeed':cmmTransSFPFiberChnlSpeed,'cmmTransQSFPFiberChnlSpeed':cmmTransQSFPFiberChnlSpeed,'cmmTransSFPInfiniBandCompliance':cmmTransSFPInfiniBandCompliance,'cmmTransSFPEsconCompliance':cmmTransSFPEsconCompliance,'cmmTransSfpPlusCableTech':cmmTransSfpPlusCableTech,'cmmTransEncoding':cmmTransEncoding,'cmmTransLengthKmtrs':cmmTransLengthKmtrs,'cmmTransLengthMtrs':cmmTransLengthMtrs,'cmmTransLengthOM1':cmmTransLengthOM1,'cmmTransLengthOM2':cmmTransLengthOM2,'cmmTransLengthOM3':cmmTransLengthOM3,'cmmTransLengthOM4':cmmTransLengthOM4,_AW:cmmTransVendorName,'cmmTransVendorOUI':cmmTransVendorOUI,'cmmTransVendorPartNumber':cmmTransVendorPartNumber,'cmmTransVendorRevision':cmmTransVendorRevision,'cmmTransCheckCode':cmmTransCheckCode,'cmmTransCheckCodeExtended':cmmTransCheckCodeExtended,'cmmTransNominalBitRate':cmmTransNominalBitRate,'cmmTransBitRateMax':cmmTransBitRateMax,'cmmTransBitRateMin':cmmTransBitRateMin,_AX:cmmTransVendorSerialNumber,'cmmTransDateCode':cmmTransDateCode,'cmmTransDDMSupport':cmmTransDDMSupport,'cmmTransMaxCaseTemp':cmmTransMaxCaseTemp,'cmmTransSFPOptionsImp':cmmTransSFPOptionsImp,'cmmTransQSFPOptionsImp':cmmTransQSFPOptionsImp,'cmmTransPresence':cmmTransPresence,'cmmTransDDMTable':cmmTransDDMTable,'cmmTransDDMEntry':cmmTransDDMEntry,_L:cmmTransChannelIndex,_c:cmmTransTemperature,_AC:cmmTransTempCriticalThresholdMin,_AD:cmmTransTempCriticalThresholdMax,_AE:cmmTransTempAlertThresholdMin,_AF:cmmTransTempAlertThresholdMax,_d:cmmTransVoltage,_AG:cmmTransVoltCriticalThresholdMin,_AH:cmmTransVoltCriticalThresholdMax,_AI:cmmTransVoltAlertThresholdMin,_AJ:cmmTransVoltAlertThresholdMax,_e:cmmTransLaserBiasCurrent,_AK:cmmTransLaserBiasCurrCriticalThresholdMin,_AL:cmmTransLaserBiasCurrCriticalThresholdMax,_AM:cmmTransLaserBiasCurrAlertThresholdMin,_AN:cmmTransLaserBiasCurrAlertThresholdMax,_g:cmmTransTxPower,_AS:cmmTransTxPowerCriticalThresholdMin,_AT:cmmTransTxPowerCriticalThresholdMax,_AU:cmmTransTxPowerAlertThresholdMin,_AV:cmmTransTxPowerAlertThresholdMax,_f:cmmTransRxPower,_AO:cmmTransRxPowerCriticalThresholdMin,_AP:cmmTransRxPowerCriticalThresholdMax,_AQ:cmmTransRxPowerAlertThresholdMin,_AR:cmmTransRxPowerAlertThresholdMax,'cmmTransTxPowerSupported':cmmTransTxPowerSupported,'cmmTransRxPowerSupported':cmmTransRxPowerSupported,'cmmTransDDMStatus':cmmTransDDMStatus,'cmmTransTxState':cmmTransTxState,'cmmTransRxLosState':cmmTransRxLosState,'cmmTransTxLosState':cmmTransTxLosState,'cmmTransResetState':cmmTransResetState,'cmmTransPowerMode':cmmTransPowerMode,'cmmSysRamTable':cmmSysRamTable,'cmmSysRamEntry':cmmSysRamEntry,'cmmSysRamTotalMem':cmmSysRamTotalMem,_m:cmmSysRamUsedMem,'cmmSysRamFreeMem':cmmSysRamFreeMem,_A4:cmmSysRamCriticalThreshold,_A3:cmmSysRamAlertThreshold,'cmmStackCpuTable':cmmStackCpuTable,'cmmStackCpuEntry':cmmStackCpuEntry,'cmmStackUnitNumCpuProcessor':cmmStackUnitNumCpuProcessor,_k:cmmStackUnitCpuLoad1Min,_A0:cmmStackUnitCpuLoad5Min,_y:cmmStackUnitCpuLoad15Min,_A1:cmmStackCpuLoad1minAlertThreshold,_A2:cmmStackCpuLoad1minCriticalThreshold,_z:cmmStackCpuLoad5minCriticalThreshold,_x:cmmStackCpuLoad15minCriticalThreshold,_l:cmmStackUnitCpuUtilization,_As:cmmStackUnitCpuUtilAlertThreshold,_At:cmmStackUnitCpuUtilCriticalThreshold,'cmmSysPowerSupplyTable':cmmSysPowerSupplyTable,'cmmSysPowerSupplyEntry':cmmSysPowerSupplyEntry,_V:cmmSysPSUIndex,_A9:cmmSysPowerSupplyOperStatus,'cmmSysPowerSupplyType':cmmSysPowerSupplyType,'cmmSysHotSwapStat':cmmSysHotSwapStat,'cmmSysPSConsumption':cmmSysPSConsumption,'cmmSysInputPower':cmmSysInputPower,'cmmSysInputVoltage':cmmSysInputVoltage,'cmmSysOutputVoltage':cmmSysOutputVoltage,'cmmSysInputCurrent':cmmSysInputCurrent,'cmmSysOutputCurrent':cmmSysOutputCurrent,'cmmSysPSTemperature1':cmmSysPSTemperature1,'cmmSysPSTemperature2':cmmSysPSTemperature2,'cmmSysPSFan1Rpm':cmmSysPSFan1Rpm,'cmmSysPSFan2Rpm':cmmSysPSFan2Rpm,'cmmSysPS12VPg':cmmSysPS12VPg,'cmmSysPSAcAlert':cmmSysPSAcAlert,'cmmSysPSParamsSupport':cmmSysPSParamsSupport,'cmmSysPowerRailTable':cmmSysPowerRailTable,'cmmSysPowerRailEntry':cmmSysPowerRailEntry,'cmmSysPOWERVDDR':cmmSysPOWERVDDR,'cmmSysPOWERCORE':cmmSysPOWERCORE,'cmmSysV1P1POWERRAIL':cmmSysV1P1POWERRAIL,'cmmSysMAINBOARDPOWERRAIL':cmmSysMAINBOARDPOWERRAIL,'cmmSysV1P05POWERRAIL':cmmSysV1P05POWERRAIL,'cmmSysV1P5POWERRAIL':cmmSysV1P5POWERRAIL,'cmmSysVCCPOWERRAIL':cmmSysVCCPOWERRAIL,'cmmSysSBV1P5POWERRAIL':cmmSysSBV1P5POWERRAIL,'cmmSysV1P0POWERRAIL':cmmSysV1P0POWERRAIL,'cmmSysV3P3POWERRAIL':cmmSysV3P3POWERRAIL,'cmmSysV1P8POWERRAIL':cmmSysV1P8POWERRAIL,'cmmSysV1P35POWERRAIL':cmmSysV1P35POWERRAIL,'cmmSysVCC5V':cmmSysVCC5V,'cmmSysVCC33V':cmmSysVCC33V,'cmmSysVCCMAC1V':cmmSysVCCMAC1V,'cmmSysVCCMACAVS1V':cmmSysVCCMACAVS1V,'cmmSysVCCV1P05':cmmSysVCCV1P05,'cmmSysVCCV1P5':cmmSysVCCV1P5,'cmmSysVCCV1P8':cmmSysVCCV1P8,'cmmSysVCCAVS1V':cmmSysVCCAVS1V,'cmmSysDDRVTT':cmmSysDDRVTT,'cmmFanTrayTable':cmmFanTrayTable,'cmmFanTrayEntry':cmmFanTrayEntry,_O:cmmFanTrayNumber,'cmmFanTrayStatus':cmmFanTrayStatus,'cmmFanTrayLedColor':cmmFanTrayLedColor,'cmmFanTable':cmmFanTable,'cmmFanEntry':cmmFanEntry,_X:cmmFanIndex,'cmmFanRpm':cmmFanRpm,_Au:cmmFanRpmMin,_Av:cmmFanRpmMax,'cmmFanStatus':cmmFanStatus,'cmmFanLocation':cmmFanLocation,'cmmSysTemperatureTable':cmmSysTemperatureTable,'cmmSysTemperatureEntry':cmmSysTemperatureEntry,_P:cmmSysTemperatureSensorIndex,_S:cmmSysTemperatureSensorName,_R:cmmSysTemperatureValue,_A7:cmmSysTempEmergencyThresholdMin,_A8:cmmSysTempEmergencyThresholdMax,_o:cmmSysTempAlertThresholdMin,_p:cmmSysTempAlertThresholdMax,_q:cmmSysTempCriticalThresholdMin,_r:cmmSysTempCriticalThresholdMax,'cmmSysComponentStatusTable':cmmSysComponentStatusTable,'cmmSysComponentStatusEntry':cmmSysComponentStatusEntry,'cmmSysPsu1Status':cmmSysPsu1Status,'cmmSysPsu1LedColor':cmmSysPsu1LedColor,'cmmSysPsu2Status':cmmSysPsu2Status,'cmmSysPsu2LedColor':cmmSysPsu2LedColor,'cmmSysLocatorLedStatus':cmmSysLocatorLedStatus,'cmmSysLocatorLedColor':cmmSysLocatorLedColor,'cmmSysMasterLedStatus':cmmSysMasterLedStatus,'cmmSysMasterLedColor':cmmSysMasterLedColor,'cmmSysFanStatus':cmmSysFanStatus,'cmmSysFrontFanLedColor':cmmSysFrontFanLedColor,'cmmSysRamStatus':cmmSysRamStatus,'cmmSysCpuStatus':cmmSysCpuStatus,'cmmSysDiskStatus':cmmSysDiskStatus,'cmmSysTemperatureStatus':cmmSysTemperatureStatus,'cmmSysSwModuleTable':cmmSysSwModuleTable,'cmmSysSwModuleEntry':cmmSysSwModuleEntry,'cmmSysSwRuntimeImgVersion':cmmSysSwRuntimeImgVersion,'cmmSysSwRuntimeImgDate':cmmSysSwRuntimeImgDate,'cmmSwitchTemperatureTable':cmmSwitchTemperatureTable,'cmmSwitchTemperatureEntry':cmmSwitchTemperatureEntry,_Ao:cmmSwitchTemperatureSensorIndex,'cmmSwitchTemperatureValue':cmmSwitchTemperatureValue,'cmmSwitchTempPeakValue':cmmSwitchTempPeakValue,'cmmSysHardDiskTable':cmmSysHardDiskTable,'cmmSysHardDiskEntry':cmmSysHardDiskEntry,'cmmSysHarddiskSerialno':cmmSysHarddiskSerialno,'cmmSysHarddiskModelno':cmmSysHarddiskModelno,'cmmSysHarddiskFirmwarerev':cmmSysHarddiskFirmwarerev,'cmmSysHarddiskCylinders':cmmSysHarddiskCylinders,'cmmSysHarddiskHeads':cmmSysHarddiskHeads,'cmmSysHarddiskSectors':cmmSysHarddiskSectors,'cmmSysHarddiskUnformattedBytesorTrack':cmmSysHarddiskUnformattedBytesorTrack,'cmmSysHarddiskUnformattedBytesorSector':cmmSysHarddiskUnformattedBytesorSector,'cmmSysHarddiskRevisionNum':cmmSysHarddiskRevisionNum,'cmmSysHarddiskTotalsize':cmmSysHarddiskTotalsize,_n:cmmSysHarddiskUsedMem,'cmmSysHarddiskFreeMem':cmmSysHarddiskFreeMem,_A6:cmmSysHarddiskCriticalThreshold,_A5:cmmSysHarddiskAlertThreshold,'cmmSystemStatusTable':cmmSystemStatusTable,'cmmSystemStatusEntry':cmmSystemStatusEntry,'cmmSystemMinorFaultStatus':cmmSystemMinorFaultStatus,'cmmSystemMajorFaultStatus':cmmSystemMajorFaultStatus,'cmmSysStatus':cmmSysStatus,'cmmSysLedColor':cmmSysLedColor,'cmmCpuCoreUtilTable':cmmCpuCoreUtilTable,'cmmCpuCoreUtilEntry':cmmCpuCoreUtilEntry,_Ap:cmmCpuCoreIndex,'cmmCpuCoreUtilization':cmmCpuCoreUtilization,'cmmCpuCoreModelName':cmmCpuCoreModelName,'cmmPsuFruTable':cmmPsuFruTable,'cmmPsuFruEntry':cmmPsuFruEntry,'cmmPsuPpid':cmmPsuPpid,'cmmPsuCountryofOrigin':cmmPsuCountryofOrigin,'cmmPsuPpidPartNum':cmmPsuPpidPartNum,'cmmPsuPpidPartNumRev':cmmPsuPpidPartNumRev,'cmmPsuManufactureId':cmmPsuManufactureId,'cmmPsuDateCode':cmmPsuDateCode,_AA:cmmPsuSerialNumber,'cmmPsuPartNum':cmmPsuPartNum,'cmmPsuPartNumRev':cmmPsuPartNumRev,'cmmPsuNumOfFanPerTray':cmmPsuNumOfFanPerTray,'cmmPsuType':cmmPsuType,'cmmPsuServiceTag':cmmPsuServiceTag,'cmmPsuIanaNum':cmmPsuIanaNum,'cmmPsuFanMaxRpm':cmmPsuFanMaxRpm,'cmmPsuAirFlowDir':cmmPsuAirFlowDir,'cmmPsuMaxOutputWatt':cmmPsuMaxOutputWatt,'cmmFanFruTable':cmmFanFruTable,'cmmFanFruEntry':cmmFanFruEntry,'cmmFanPpid':cmmFanPpid,'cmmFanCountryofOrigin':cmmFanCountryofOrigin,'cmmFanPpidPartNum':cmmFanPpidPartNum,'cmmFanPpidPartNumRev':cmmFanPpidPartNumRev,'cmmFanManufactureId':cmmFanManufactureId,'cmmFanDateCode':cmmFanDateCode,_AB:cmmFanSerialNumber,'cmmFanPartNum':cmmFanPartNum,'cmmFanPartNumRev':cmmFanPartNumRev,'cmmFanNumOfFanPerTray':cmmFanNumOfFanPerTray,'cmmFanType':cmmFanType,'cmmFanServiceTag':cmmFanServiceTag,'cmmFanIanaNum':cmmFanIanaNum,'cmmFanMaxRpm':cmmFanMaxRpm,'cmmSysCpldTable':cmmSysCpldTable,'cmmSysCpldEntry':cmmSysCpldEntry,_Aq:cmmSysCpldIndex,'cmmSysCpldName':cmmSysCpldName,'cmmSysCpldSupportedVer':cmmSysCpldSupportedVer,'cmmSysCpldCurrentVer':cmmSysCpldCurrentVer,'cmmAlarmObjects':cmmAlarmObjects,'cmmAlarmVariable':cmmAlarmVariable,'cmmAlarmVarInteger':cmmAlarmVarInteger,'cmmAlarmVarString':cmmAlarmVarString,'cmmAlarmMibNotifications':cmmAlarmMibNotifications,'cmmCpuLoad15MinCritical':cmmCpuLoad15MinCritical,'cmmCpuLoad5MinCritical':cmmCpuLoad5MinCritical,'cmmCpuLoad1MinAlert':cmmCpuLoad1MinAlert,'cmmCpuLoad1MinCritical':cmmCpuLoad1MinCritical,'cmmCpuLoad1MinAlertRecovery':cmmCpuLoad1MinAlertRecovery,'cmmCpuLoad15MinCriticalRecovery':cmmCpuLoad15MinCriticalRecovery,'cmmCpuLoad5MinCriticalRecovery':cmmCpuLoad5MinCriticalRecovery,'cmmCpuLoad1MinCriticalRecovery':cmmCpuLoad1MinCriticalRecovery,'cmmCpuCoreUtilHighAlert':cmmCpuCoreUtilHighAlert,'cmmCpuCoreUtilHighCritical':cmmCpuCoreUtilHighCritical,'cmmCpuCoreUtilHighAlertRecovery':cmmCpuCoreUtilHighAlertRecovery,'cmmCpuCoreUtilHighCriticalRecovery':cmmCpuCoreUtilHighCriticalRecovery,'cmmRamUsageRisingAlert':cmmRamUsageRisingAlert,'cmmRamUsageRisingCritical':cmmRamUsageRisingCritical,'cmmRamUsageAlertRecovery':cmmRamUsageAlertRecovery,'cmmRamUsageCriticalRecovery':cmmRamUsageCriticalRecovery,'cmmHardDiskUsageRisingAlert':cmmHardDiskUsageRisingAlert,'cmmHardDiskUsageRisingCritical':cmmHardDiskUsageRisingCritical,'cmmHardDiskUsageAlertRecovery':cmmHardDiskUsageAlertRecovery,'cmmHardDiskUsageCriticalRecovery':cmmHardDiskUsageCriticalRecovery,'cmmTemperatureLowEmergency':cmmTemperatureLowEmergency,'cmmTemperatureHighEmergency':cmmTemperatureHighEmergency,'cmmTemperatureLowAlert':cmmTemperatureLowAlert,'cmmTemperatureHighAlert':cmmTemperatureHighAlert,'cmmTemperatureLowCritical':cmmTemperatureLowCritical,'cmmTemperatureHighCritical':cmmTemperatureHighCritical,'cmmTemperatureHighAlertRecovery':cmmTemperatureHighAlertRecovery,'cmmTemperatureLowAlertRecovery':cmmTemperatureLowAlertRecovery,'cmmTemperatureHighCriticalRecovery':cmmTemperatureHighCriticalRecovery,'cmmTemperatureLowCriticalRecovery':cmmTemperatureLowCriticalRecovery,'cmmPsuInsertedNotify':cmmPsuInsertedNotify,'cmmPsuRemovedAlert':cmmPsuRemovedAlert,'cmmPsuAcFailedAlert':cmmPsuAcFailedAlert,'cmmPsuAcRecover':cmmPsuAcRecover,'cmmPsu12vPgFailedAlert':cmmPsu12vPgFailedAlert,'cmmPsu12vPgRecover':cmmPsu12vPgRecover,'cmmFanTrayInsertedNotify':cmmFanTrayInsertedNotify,'cmmFanTrayRemovedAlert':cmmFanTrayRemovedAlert,'cmmFanTrayFaultyAlert':cmmFanTrayFaultyAlert,'cmmFanTrayRecovered':cmmFanTrayRecovered,'cmmFanTrayStallAlert':cmmFanTrayStallAlert,'cmmFanTrayStallRecovered':cmmFanTrayStallRecovered,'cmmFanRPMMinAlert':cmmFanRPMMinAlert,'cmmFanRPMMaxAlert':cmmFanRPMMaxAlert,'cmmTransMibNotifications':cmmTransMibNotifications,'cmmTransCriticalTempHigh':cmmTransCriticalTempHigh,'cmmTransCriticalTempLow':cmmTransCriticalTempLow,'cmmTransAlertTempHigh':cmmTransAlertTempHigh,'cmmTransAlertTempLow':cmmTransAlertTempLow,'cmmTransNotifyTransceiverTempRecovered':cmmTransNotifyTransceiverTempRecovered,'cmmTransCriticalVoltageHigh':cmmTransCriticalVoltageHigh,'cmmTransCriticalVoltageLow':cmmTransCriticalVoltageLow,'cmmTransAlertVoltageHigh':cmmTransAlertVoltageHigh,'cmmTransAlertVoltageLow':cmmTransAlertVoltageLow,'cmmTransNotifyTransceiverVoltRecovered':cmmTransNotifyTransceiverVoltRecovered,'cmmTransCriticalBiasHigh':cmmTransCriticalBiasHigh,'cmmTransCriticalBiasLow':cmmTransCriticalBiasLow,'cmmTransAlertBiashigh':cmmTransAlertBiashigh,'cmmTransAlertBiasLow':cmmTransAlertBiasLow,'cmmTransNotifyTransceiverBiasRecovered':cmmTransNotifyTransceiverBiasRecovered,'cmmTransCriticalRxPowerHigh':cmmTransCriticalRxPowerHigh,'cmmTransCriticalRxPowerLow':cmmTransCriticalRxPowerLow,'cmmTransAlertRxPowerHigh':cmmTransAlertRxPowerHigh,'cmmTransAlertRxPowerLow':cmmTransAlertRxPowerLow,'cmmTransNotifyTransceiverRxPowRecovered':cmmTransNotifyTransceiverRxPowRecovered,'cmmTransCriticalTxPowerHigh':cmmTransCriticalTxPowerHigh,'cmmTransCriticalTxPowerLow':cmmTransCriticalTxPowerLow,'cmmTransAlertTxPowerHigh':cmmTransAlertTxPowerHigh,'cmmTransAlertTxPowerLow':cmmTransAlertTxPowerLow,'cmmTransNotifyTransceiverTxPowRecovered':cmmTransNotifyTransceiverTxPowRecovered,'cmmTransNotifyTransceiverInserted':cmmTransNotifyTransceiverInserted,'cmmTransAlertTransceiverRemoved':cmmTransAlertTransceiverRemoved,'cmmTransAlertFaultyTransceiverInserted':cmmTransAlertFaultyTransceiverInserted})