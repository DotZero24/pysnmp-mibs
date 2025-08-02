_s='sBTASourceSwitchCount'
_r='sBTAVoltageSource'
_q='mtrapargsTimeTicks'
_p='sBTAModulesEnvironmentalSensorsIndex'
_o='sBTAModulesEnvironmentalModulesIndex'
_n='sBTAControlUserIndex'
_m='noreset'
_l='sRPCBreakersBreakersIndex'
_k='sRPCBreakersPortIndex'
_j='sRPCBreakersModIndex'
_i='sBTAModulesRPCBreakersBreakersIndex'
_h='sBTAModulesRPCBreakersModulesIndex'
_g='groupCurrentIndex'
_f='sRPCOutletIndex'
_e='sRPCOutletPortIndex'
_d='sRPCOutletModuleIndex'
_c='sRPCPortIndex'
_b='sRPCModuleIndex'
_a='sBTAModulesRPCOutletIndex'
_Z='sBTAModulesRPCOutletModuleIndex'
_Y='sBTAModulesRPCIndex'
_X='enable'
_W='disable'
_V='trapIndex'
_U='DisplayString'
_T='NotificationType'
_S='unlock'
_R='lockoff'
_Q='lockon'
_P='reboot'
_O='unknown'
_N='sBTAOutletIndex'
_M='sBTASensorIndex'
_L='on'
_K='off'
_J='enabled'
_I='disabled'
_H='mtrapargsString'
_G='sBTAModuleIndex'
_F='mtrapargsInteger'
_E='Integer32'
_D='read-write'
_C='Baytech-MIB-401-4'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_T,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_T,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_U,'PhysAddress','TextualConvention')
_Baytech_ObjectIdentity=ObjectIdentity
baytech=_Baytech_ObjectIdentity((1,3,6,1,4,1,4779))
_Btadevices_ObjectIdentity=ObjectIdentity
btadevices=_Btadevices_ObjectIdentity((1,3,6,1,4,1,4779,1))
_SBTAIdent_ObjectIdentity=ObjectIdentity
sBTAIdent=_SBTAIdent_ObjectIdentity((1,3,6,1,4,1,4779,1,1))
_SBTAIdentFirmwareRev_Type=DisplayString
_SBTAIdentFirmwareRev_Object=MibScalar
sBTAIdentFirmwareRev=_SBTAIdentFirmwareRev_Object((1,3,6,1,4,1,4779,1,1,1),_SBTAIdentFirmwareRev_Type())
sBTAIdentFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAIdentFirmwareRev.setStatus(_A)
_SBTAIdentSerialNumber_Type=Integer32
_SBTAIdentSerialNumber_Object=MibScalar
sBTAIdentSerialNumber=_SBTAIdentSerialNumber_Object((1,3,6,1,4,1,4779,1,1,2),_SBTAIdentSerialNumber_Type())
sBTAIdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAIdentSerialNumber.setStatus(_A)
class _SBTAIdentUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SBTAIdentUnitName_Type.__name__=_U
_SBTAIdentUnitName_Object=MibScalar
sBTAIdentUnitName=_SBTAIdentUnitName_Object((1,3,6,1,4,1,4779,1,1,3),_SBTAIdentUnitName_Type())
sBTAIdentUnitName.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAIdentUnitName.setStatus(_A)
_SBTANetworkConfig_ObjectIdentity=ObjectIdentity
sBTANetworkConfig=_SBTANetworkConfig_ObjectIdentity((1,3,6,1,4,1,4779,1,2))
class _SBTANetworkConfigBootpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigBootpEnable_Type.__name__=_E
_SBTANetworkConfigBootpEnable_Object=MibScalar
sBTANetworkConfigBootpEnable=_SBTANetworkConfigBootpEnable_Object((1,3,6,1,4,1,4779,1,2,1),_SBTANetworkConfigBootpEnable_Type())
sBTANetworkConfigBootpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigBootpEnable.setStatus(_A)
class _SBTANetworkConfigDHCPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigDHCPEnable_Type.__name__=_E
_SBTANetworkConfigDHCPEnable_Object=MibScalar
sBTANetworkConfigDHCPEnable=_SBTANetworkConfigDHCPEnable_Object((1,3,6,1,4,1,4779,1,2,2),_SBTANetworkConfigDHCPEnable_Type())
sBTANetworkConfigDHCPEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigDHCPEnable.setStatus(_A)
class _SBTANetworkConfigSSHEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigSSHEnable_Type.__name__=_E
_SBTANetworkConfigSSHEnable_Object=MibScalar
sBTANetworkConfigSSHEnable=_SBTANetworkConfigSSHEnable_Object((1,3,6,1,4,1,4779,1,2,3),_SBTANetworkConfigSSHEnable_Type())
sBTANetworkConfigSSHEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigSSHEnable.setStatus(_A)
class _SBTANetworkConfigTelnetEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigTelnetEnable_Type.__name__=_E
_SBTANetworkConfigTelnetEnable_Object=MibScalar
sBTANetworkConfigTelnetEnable=_SBTANetworkConfigTelnetEnable_Object((1,3,6,1,4,1,4779,1,2,4),_SBTANetworkConfigTelnetEnable_Type())
sBTANetworkConfigTelnetEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigTelnetEnable.setStatus(_A)
_SBTANetworkConfigActivityTimeout_Type=Integer32
_SBTANetworkConfigActivityTimeout_Object=MibScalar
sBTANetworkConfigActivityTimeout=_SBTANetworkConfigActivityTimeout_Object((1,3,6,1,4,1,4779,1,2,5),_SBTANetworkConfigActivityTimeout_Type())
sBTANetworkConfigActivityTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigActivityTimeout.setStatus(_A)
class _SBTANetworkConfigDirectConnEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigDirectConnEnable_Type.__name__=_E
_SBTANetworkConfigDirectConnEnable_Object=MibScalar
sBTANetworkConfigDirectConnEnable=_SBTANetworkConfigDirectConnEnable_Object((1,3,6,1,4,1,4779,1,2,6),_SBTANetworkConfigDirectConnEnable_Type())
sBTANetworkConfigDirectConnEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigDirectConnEnable.setStatus(_A)
_SBTANetworkConfigSNMP_ObjectIdentity=ObjectIdentity
sBTANetworkConfigSNMP=_SBTANetworkConfigSNMP_ObjectIdentity((1,3,6,1,4,1,4779,1,2,8))
_SBTANetworkConfigSNMPReadOnlyCommunity_Type=DisplayString
_SBTANetworkConfigSNMPReadOnlyCommunity_Object=MibScalar
sBTANetworkConfigSNMPReadOnlyCommunity=_SBTANetworkConfigSNMPReadOnlyCommunity_Object((1,3,6,1,4,1,4779,1,2,8,1),_SBTANetworkConfigSNMPReadOnlyCommunity_Type())
sBTANetworkConfigSNMPReadOnlyCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigSNMPReadOnlyCommunity.setStatus(_A)
_SBTANetworkConfigSNMPReadWriteCommunity_Type=DisplayString
_SBTANetworkConfigSNMPReadWriteCommunity_Object=MibScalar
sBTANetworkConfigSNMPReadWriteCommunity=_SBTANetworkConfigSNMPReadWriteCommunity_Object((1,3,6,1,4,1,4779,1,2,8,2),_SBTANetworkConfigSNMPReadWriteCommunity_Type())
sBTANetworkConfigSNMPReadWriteCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigSNMPReadWriteCommunity.setStatus(_A)
_SBTANetworkConfigSNMPNumTrapReceivers_Type=Integer32
_SBTANetworkConfigSNMPNumTrapReceivers_Object=MibScalar
sBTANetworkConfigSNMPNumTrapReceivers=_SBTANetworkConfigSNMPNumTrapReceivers_Object((1,3,6,1,4,1,4779,1,2,8,3),_SBTANetworkConfigSNMPNumTrapReceivers_Type())
sBTANetworkConfigSNMPNumTrapReceivers.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTANetworkConfigSNMPNumTrapReceivers.setStatus(_A)
_SBTANetworkConfigSNMPTrapReceiverTable_Object=MibTable
sBTANetworkConfigSNMPTrapReceiverTable=_SBTANetworkConfigSNMPTrapReceiverTable_Object((1,3,6,1,4,1,4779,1,2,8,4))
if mibBuilder.loadTexts:sBTANetworkConfigSNMPTrapReceiverTable.setStatus(_A)
_SBTANetworkConfigSNMPTrapReceiverEntry_Object=MibTableRow
sBTANetworkConfigSNMPTrapReceiverEntry=_SBTANetworkConfigSNMPTrapReceiverEntry_Object((1,3,6,1,4,1,4779,1,2,8,4,1))
sBTANetworkConfigSNMPTrapReceiverEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:sBTANetworkConfigSNMPTrapReceiverEntry.setStatus(_A)
_TrapIndex_Type=Integer32
_TrapIndex_Object=MibTableColumn
trapIndex=_TrapIndex_Object((1,3,6,1,4,1,4779,1,2,8,4,1,1),_TrapIndex_Type())
trapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trapIndex.setStatus(_A)
_ReceiverAddress_Type=IpAddress
_ReceiverAddress_Object=MibTableColumn
receiverAddress=_ReceiverAddress_Object((1,3,6,1,4,1,4779,1,2,8,4,1,2),_ReceiverAddress_Type())
receiverAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverAddress.setStatus(_A)
_SBTANetworkConfigRadius_ObjectIdentity=ObjectIdentity
sBTANetworkConfigRadius=_SBTANetworkConfigRadius_ObjectIdentity((1,3,6,1,4,1,4779,1,2,9))
class _SBTANetworkConfigRadiusEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_SBTANetworkConfigRadiusEnable_Type.__name__=_E
_SBTANetworkConfigRadiusEnable_Object=MibScalar
sBTANetworkConfigRadiusEnable=_SBTANetworkConfigRadiusEnable_Object((1,3,6,1,4,1,4779,1,2,9,1),_SBTANetworkConfigRadiusEnable_Type())
sBTANetworkConfigRadiusEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigRadiusEnable.setStatus(_A)
_SBTANetworkConfigRadiusPrimaryServer_Type=IpAddress
_SBTANetworkConfigRadiusPrimaryServer_Object=MibScalar
sBTANetworkConfigRadiusPrimaryServer=_SBTANetworkConfigRadiusPrimaryServer_Object((1,3,6,1,4,1,4779,1,2,9,2),_SBTANetworkConfigRadiusPrimaryServer_Type())
sBTANetworkConfigRadiusPrimaryServer.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigRadiusPrimaryServer.setStatus(_A)
_SBTANetworkConfigRadiusSecondaryServer_Type=IpAddress
_SBTANetworkConfigRadiusSecondaryServer_Object=MibScalar
sBTANetworkConfigRadiusSecondaryServer=_SBTANetworkConfigRadiusSecondaryServer_Object((1,3,6,1,4,1,4779,1,2,9,3),_SBTANetworkConfigRadiusSecondaryServer_Type())
sBTANetworkConfigRadiusSecondaryServer.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigRadiusSecondaryServer.setStatus(_A)
class _SBTANetworkConfigRadiusLocalLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_SBTANetworkConfigRadiusLocalLogin_Type.__name__=_E
_SBTANetworkConfigRadiusLocalLogin_Object=MibScalar
sBTANetworkConfigRadiusLocalLogin=_SBTANetworkConfigRadiusLocalLogin_Object((1,3,6,1,4,1,4779,1,2,9,4),_SBTANetworkConfigRadiusLocalLogin_Type())
sBTANetworkConfigRadiusLocalLogin.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigRadiusLocalLogin.setStatus(_A)
_SBTANetworkConfigWEB_ObjectIdentity=ObjectIdentity
sBTANetworkConfigWEB=_SBTANetworkConfigWEB_ObjectIdentity((1,3,6,1,4,1,4779,1,2,10))
class _SBTANetworkConfigWebEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigWebEnable_Type.__name__=_E
_SBTANetworkConfigWebEnable_Object=MibScalar
sBTANetworkConfigWebEnable=_SBTANetworkConfigWebEnable_Object((1,3,6,1,4,1,4779,1,2,10,1),_SBTANetworkConfigWebEnable_Type())
sBTANetworkConfigWebEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigWebEnable.setStatus(_A)
class _SBTANetworkConfigWebSecureEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigWebSecureEnable_Type.__name__=_E
_SBTANetworkConfigWebSecureEnable_Object=MibScalar
sBTANetworkConfigWebSecureEnable=_SBTANetworkConfigWebSecureEnable_Object((1,3,6,1,4,1,4779,1,2,10,2),_SBTANetworkConfigWebSecureEnable_Type())
sBTANetworkConfigWebSecureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigWebSecureEnable.setStatus(_A)
class _SBTANetworkConfigWebLoginEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SBTANetworkConfigWebLoginEnable_Type.__name__=_E
_SBTANetworkConfigWebLoginEnable_Object=MibScalar
sBTANetworkConfigWebLoginEnable=_SBTANetworkConfigWebLoginEnable_Object((1,3,6,1,4,1,4779,1,2,10,3),_SBTANetworkConfigWebLoginEnable_Type())
sBTANetworkConfigWebLoginEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigWebLoginEnable.setStatus(_A)
_SBTANetworkConfigWebActivityTimeout_Type=Integer32
_SBTANetworkConfigWebActivityTimeout_Object=MibScalar
sBTANetworkConfigWebActivityTimeout=_SBTANetworkConfigWebActivityTimeout_Object((1,3,6,1,4,1,4779,1,2,10,4),_SBTANetworkConfigWebActivityTimeout_Type())
sBTANetworkConfigWebActivityTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTANetworkConfigWebActivityTimeout.setStatus(_A)
_SBTAModules_ObjectIdentity=ObjectIdentity
sBTAModules=_SBTAModules_ObjectIdentity((1,3,6,1,4,1,4779,1,3))
_SBTAModulesNumberOfModules_Type=Integer32
_SBTAModulesNumberOfModules_Object=MibScalar
sBTAModulesNumberOfModules=_SBTAModulesNumberOfModules_Object((1,3,6,1,4,1,4779,1,3,1),_SBTAModulesNumberOfModules_Type())
sBTAModulesNumberOfModules.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesNumberOfModules.setStatus(_A)
_SBTAModulesModulesInstalled_Type=DisplayString
_SBTAModulesModulesInstalled_Object=MibScalar
sBTAModulesModulesInstalled=_SBTAModulesModulesInstalled_Object((1,3,6,1,4,1,4779,1,3,2),_SBTAModulesModulesInstalled_Type())
sBTAModulesModulesInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesModulesInstalled.setStatus(_A)
_SBTAModulesResetModulesCmd_Type=Integer32
_SBTAModulesResetModulesCmd_Object=MibScalar
sBTAModulesResetModulesCmd=_SBTAModulesResetModulesCmd_Object((1,3,6,1,4,1,4779,1,3,3),_SBTAModulesResetModulesCmd_Type())
sBTAModulesResetModulesCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesResetModulesCmd.setStatus('deprecated')
_SBTAModulesNumberOfIntelligentModules_Type=Integer32
_SBTAModulesNumberOfIntelligentModules_Object=MibScalar
sBTAModulesNumberOfIntelligentModules=_SBTAModulesNumberOfIntelligentModules_Object((1,3,6,1,4,1,4779,1,3,4),_SBTAModulesNumberOfIntelligentModules_Type())
sBTAModulesNumberOfIntelligentModules.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesNumberOfIntelligentModules.setStatus(_A)
_SBTAModulesRPC_ObjectIdentity=ObjectIdentity
sBTAModulesRPC=_SBTAModulesRPC_ObjectIdentity((1,3,6,1,4,1,4779,1,3,5))
_SBTAModulesNumberOfRPCModules_Type=Integer32
_SBTAModulesNumberOfRPCModules_Object=MibScalar
sBTAModulesNumberOfRPCModules=_SBTAModulesNumberOfRPCModules_Object((1,3,6,1,4,1,4779,1,3,5,1),_SBTAModulesNumberOfRPCModules_Type())
sBTAModulesNumberOfRPCModules.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesNumberOfRPCModules.setStatus(_A)
_SBTAModulesRPCTable_Object=MibTable
sBTAModulesRPCTable=_SBTAModulesRPCTable_Object((1,3,6,1,4,1,4779,1,3,5,2))
if mibBuilder.loadTexts:sBTAModulesRPCTable.setStatus(_A)
_SBTAModulesRPCEntry_Object=MibTableRow
sBTAModulesRPCEntry=_SBTAModulesRPCEntry_Object((1,3,6,1,4,1,4779,1,3,5,2,1))
sBTAModulesRPCEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:sBTAModulesRPCEntry.setStatus(_A)
_SBTAModulesRPCIndex_Type=Integer32
_SBTAModulesRPCIndex_Object=MibTableColumn
sBTAModulesRPCIndex=_SBTAModulesRPCIndex_Object((1,3,6,1,4,1,4779,1,3,5,2,1,1),_SBTAModulesRPCIndex_Type())
sBTAModulesRPCIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCIndex.setStatus(_A)
_SBTAModulesRPCName_Type=DisplayString
_SBTAModulesRPCName_Object=MibTableColumn
sBTAModulesRPCName=_SBTAModulesRPCName_Object((1,3,6,1,4,1,4779,1,3,5,2,1,2),_SBTAModulesRPCName_Type())
sBTAModulesRPCName.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCName.setStatus(_A)
_SBTAModulesRPCFirmwareVersion_Type=DisplayString
_SBTAModulesRPCFirmwareVersion_Object=MibTableColumn
sBTAModulesRPCFirmwareVersion=_SBTAModulesRPCFirmwareVersion_Object((1,3,6,1,4,1,4779,1,3,5,2,1,3),_SBTAModulesRPCFirmwareVersion_Type())
sBTAModulesRPCFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCFirmwareVersion.setStatus(_A)
_SBTAModulesRPCCurrent_Type=Integer32
_SBTAModulesRPCCurrent_Object=MibTableColumn
sBTAModulesRPCCurrent=_SBTAModulesRPCCurrent_Object((1,3,6,1,4,1,4779,1,3,5,2,1,4),_SBTAModulesRPCCurrent_Type())
sBTAModulesRPCCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCCurrent.setStatus(_A)
_SBTAModulesRPCMaxCurrent_Type=Integer32
_SBTAModulesRPCMaxCurrent_Object=MibTableColumn
sBTAModulesRPCMaxCurrent=_SBTAModulesRPCMaxCurrent_Object((1,3,6,1,4,1,4779,1,3,5,2,1,5),_SBTAModulesRPCMaxCurrent_Type())
sBTAModulesRPCMaxCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCMaxCurrent.setStatus(_A)
_SBTAModulesRPCVoltage_Type=Integer32
_SBTAModulesRPCVoltage_Object=MibTableColumn
sBTAModulesRPCVoltage=_SBTAModulesRPCVoltage_Object((1,3,6,1,4,1,4779,1,3,5,2,1,6),_SBTAModulesRPCVoltage_Type())
sBTAModulesRPCVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCVoltage.setStatus(_A)
_SBTAModulesRPCPower_Type=Integer32
_SBTAModulesRPCPower_Object=MibTableColumn
sBTAModulesRPCPower=_SBTAModulesRPCPower_Object((1,3,6,1,4,1,4779,1,3,5,2,1,7),_SBTAModulesRPCPower_Type())
sBTAModulesRPCPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCPower.setStatus(_A)
_SBTAModulesRPCTemperature_Type=Integer32
_SBTAModulesRPCTemperature_Object=MibTableColumn
sBTAModulesRPCTemperature=_SBTAModulesRPCTemperature_Object((1,3,6,1,4,1,4779,1,3,5,2,1,8),_SBTAModulesRPCTemperature_Type())
sBTAModulesRPCTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCTemperature.setStatus(_A)
_SBTAModulesRPCRebootTimeout_Type=Integer32
_SBTAModulesRPCRebootTimeout_Object=MibTableColumn
sBTAModulesRPCRebootTimeout=_SBTAModulesRPCRebootTimeout_Object((1,3,6,1,4,1,4779,1,3,5,2,1,9),_SBTAModulesRPCRebootTimeout_Type())
sBTAModulesRPCRebootTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCRebootTimeout.setStatus(_A)
class _SBTAModulesRPCAllOutletsCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_K,0),(_L,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_O,6)))
_SBTAModulesRPCAllOutletsCmd_Type.__name__=_E
_SBTAModulesRPCAllOutletsCmd_Object=MibTableColumn
sBTAModulesRPCAllOutletsCmd=_SBTAModulesRPCAllOutletsCmd_Object((1,3,6,1,4,1,4779,1,3,5,2,1,10),_SBTAModulesRPCAllOutletsCmd_Type())
sBTAModulesRPCAllOutletsCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCAllOutletsCmd.setStatus(_A)
_SBTAModulesRPCAllOutletsStatus_Type=DisplayString
_SBTAModulesRPCAllOutletsStatus_Object=MibTableColumn
sBTAModulesRPCAllOutletsStatus=_SBTAModulesRPCAllOutletsStatus_Object((1,3,6,1,4,1,4779,1,3,5,2,1,11),_SBTAModulesRPCAllOutletsStatus_Type())
sBTAModulesRPCAllOutletsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCAllOutletsStatus.setStatus(_A)
_SBTAModulesRPCCurrentAlarmThreshold_Type=Integer32
_SBTAModulesRPCCurrentAlarmThreshold_Object=MibTableColumn
sBTAModulesRPCCurrentAlarmThreshold=_SBTAModulesRPCCurrentAlarmThreshold_Object((1,3,6,1,4,1,4779,1,3,5,2,1,12),_SBTAModulesRPCCurrentAlarmThreshold_Type())
sBTAModulesRPCCurrentAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCCurrentAlarmThreshold.setStatus(_A)
_SBTAModulesRPCOverVoltageThreshold_Type=Integer32
_SBTAModulesRPCOverVoltageThreshold_Object=MibTableColumn
sBTAModulesRPCOverVoltageThreshold=_SBTAModulesRPCOverVoltageThreshold_Object((1,3,6,1,4,1,4779,1,3,5,2,1,13),_SBTAModulesRPCOverVoltageThreshold_Type())
sBTAModulesRPCOverVoltageThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCOverVoltageThreshold.setStatus(_A)
_SBTAModulesRPCUnderVoltageThreshold_Type=Integer32
_SBTAModulesRPCUnderVoltageThreshold_Object=MibTableColumn
sBTAModulesRPCUnderVoltageThreshold=_SBTAModulesRPCUnderVoltageThreshold_Object((1,3,6,1,4,1,4779,1,3,5,2,1,14),_SBTAModulesRPCUnderVoltageThreshold_Type())
sBTAModulesRPCUnderVoltageThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCUnderVoltageThreshold.setStatus(_A)
_SBTAModulesRPCNumberOfOutlets_Type=Integer32
_SBTAModulesRPCNumberOfOutlets_Object=MibTableColumn
sBTAModulesRPCNumberOfOutlets=_SBTAModulesRPCNumberOfOutlets_Object((1,3,6,1,4,1,4779,1,3,5,2,1,15),_SBTAModulesRPCNumberOfOutlets_Type())
sBTAModulesRPCNumberOfOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCNumberOfOutlets.setStatus(_A)
class _SBTAModulesRPCCircuitBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_SBTAModulesRPCCircuitBreaker_Type.__name__=_E
_SBTAModulesRPCCircuitBreaker_Object=MibTableColumn
sBTAModulesRPCCircuitBreaker=_SBTAModulesRPCCircuitBreaker_Object((1,3,6,1,4,1,4779,1,3,5,2,1,16),_SBTAModulesRPCCircuitBreaker_Type())
sBTAModulesRPCCircuitBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCCircuitBreaker.setStatus(_A)
_SBTAModulesRPCOverTempThreshold_Type=Integer32
_SBTAModulesRPCOverTempThreshold_Object=MibTableColumn
sBTAModulesRPCOverTempThreshold=_SBTAModulesRPCOverTempThreshold_Object((1,3,6,1,4,1,4779,1,3,5,2,1,17),_SBTAModulesRPCOverTempThreshold_Type())
sBTAModulesRPCOverTempThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCOverTempThreshold.setStatus(_A)
_SBTAModulesRPCUnitVA_Type=Integer32
_SBTAModulesRPCUnitVA_Object=MibTableColumn
sBTAModulesRPCUnitVA=_SBTAModulesRPCUnitVA_Object((1,3,6,1,4,1,4779,1,3,5,2,1,18),_SBTAModulesRPCUnitVA_Type())
sBTAModulesRPCUnitVA.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCUnitVA.setStatus(_A)
_SBTAModulesRPCNumberOfBreakers_Type=Integer32
_SBTAModulesRPCNumberOfBreakers_Object=MibTableColumn
sBTAModulesRPCNumberOfBreakers=_SBTAModulesRPCNumberOfBreakers_Object((1,3,6,1,4,1,4779,1,3,5,2,1,19),_SBTAModulesRPCNumberOfBreakers_Type())
sBTAModulesRPCNumberOfBreakers.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCNumberOfBreakers.setStatus(_A)
_SBTAModulesRPCLowCurrentThreshold_Type=Integer32
_SBTAModulesRPCLowCurrentThreshold_Object=MibTableColumn
sBTAModulesRPCLowCurrentThreshold=_SBTAModulesRPCLowCurrentThreshold_Object((1,3,6,1,4,1,4779,1,3,5,2,1,20),_SBTAModulesRPCLowCurrentThreshold_Type())
sBTAModulesRPCLowCurrentThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCLowCurrentThreshold.setStatus(_A)
_SBTAModulesRPCVoltageSource_Type=Integer32
_SBTAModulesRPCVoltageSource_Object=MibTableColumn
sBTAModulesRPCVoltageSource=_SBTAModulesRPCVoltageSource_Object((1,3,6,1,4,1,4779,1,3,5,2,1,21),_SBTAModulesRPCVoltageSource_Type())
sBTAModulesRPCVoltageSource.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCVoltageSource.setStatus(_A)
_SBTAModulesRPCSourceSwitchCount_Type=Integer32
_SBTAModulesRPCSourceSwitchCount_Object=MibTableColumn
sBTAModulesRPCSourceSwitchCount=_SBTAModulesRPCSourceSwitchCount_Object((1,3,6,1,4,1,4779,1,3,5,2,1,22),_SBTAModulesRPCSourceSwitchCount_Type())
sBTAModulesRPCSourceSwitchCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCSourceSwitchCount.setStatus(_A)
_SBTAModulesRPCNumberOfSensors_Type=Integer32
_SBTAModulesRPCNumberOfSensors_Object=MibTableColumn
sBTAModulesRPCNumberOfSensors=_SBTAModulesRPCNumberOfSensors_Object((1,3,6,1,4,1,4779,1,3,5,2,1,23),_SBTAModulesRPCNumberOfSensors_Type())
sBTAModulesRPCNumberOfSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCNumberOfSensors.setStatus(_A)
_SBTAModulesRPCType_Type=DisplayString
_SBTAModulesRPCType_Object=MibTableColumn
sBTAModulesRPCType=_SBTAModulesRPCType_Object((1,3,6,1,4,1,4779,1,3,5,2,1,24),_SBTAModulesRPCType_Type())
sBTAModulesRPCType.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCType.setStatus(_A)
_SBTAModulesRPCOutletTable_Object=MibTable
sBTAModulesRPCOutletTable=_SBTAModulesRPCOutletTable_Object((1,3,6,1,4,1,4779,1,3,5,3))
if mibBuilder.loadTexts:sBTAModulesRPCOutletTable.setStatus(_A)
_SBTAModulesRPCOutletEntry_Object=MibTableRow
sBTAModulesRPCOutletEntry=_SBTAModulesRPCOutletEntry_Object((1,3,6,1,4,1,4779,1,3,5,3,1))
sBTAModulesRPCOutletEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:sBTAModulesRPCOutletEntry.setStatus(_A)
_SBTAModulesRPCOutletModuleIndex_Type=Integer32
_SBTAModulesRPCOutletModuleIndex_Object=MibTableColumn
sBTAModulesRPCOutletModuleIndex=_SBTAModulesRPCOutletModuleIndex_Object((1,3,6,1,4,1,4779,1,3,5,3,1,1),_SBTAModulesRPCOutletModuleIndex_Type())
sBTAModulesRPCOutletModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCOutletModuleIndex.setStatus(_A)
_SBTAModulesRPCOutletIndex_Type=Integer32
_SBTAModulesRPCOutletIndex_Object=MibTableColumn
sBTAModulesRPCOutletIndex=_SBTAModulesRPCOutletIndex_Object((1,3,6,1,4,1,4779,1,3,5,3,1,2),_SBTAModulesRPCOutletIndex_Type())
sBTAModulesRPCOutletIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCOutletIndex.setStatus(_A)
class _SBTAModulesRPCOutletState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_K,0),(_L,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_O,6)))
_SBTAModulesRPCOutletState_Type.__name__=_E
_SBTAModulesRPCOutletState_Object=MibTableColumn
sBTAModulesRPCOutletState=_SBTAModulesRPCOutletState_Object((1,3,6,1,4,1,4779,1,3,5,3,1,3),_SBTAModulesRPCOutletState_Type())
sBTAModulesRPCOutletState.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCOutletState.setStatus(_A)
_SBTAModulesRPCOutletName_Type=DisplayString
_SBTAModulesRPCOutletName_Object=MibTableColumn
sBTAModulesRPCOutletName=_SBTAModulesRPCOutletName_Object((1,3,6,1,4,1,4779,1,3,5,3,1,4),_SBTAModulesRPCOutletName_Type())
sBTAModulesRPCOutletName.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCOutletName.setStatus(_A)
_SBTAModulesRPCGroupCmd_Type=DisplayString
_SBTAModulesRPCGroupCmd_Object=MibScalar
sBTAModulesRPCGroupCmd=_SBTAModulesRPCGroupCmd_Object((1,3,6,1,4,1,4779,1,3,5,4),_SBTAModulesRPCGroupCmd_Type())
sBTAModulesRPCGroupCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCGroupCmd.setStatus(_A)
_SBTAModulesRPCModPortTable_Object=MibTable
sBTAModulesRPCModPortTable=_SBTAModulesRPCModPortTable_Object((1,3,6,1,4,1,4779,1,3,5,5))
if mibBuilder.loadTexts:sBTAModulesRPCModPortTable.setStatus(_A)
_SBTAModulesRPCModPortEntry_Object=MibTableRow
sBTAModulesRPCModPortEntry=_SBTAModulesRPCModPortEntry_Object((1,3,6,1,4,1,4779,1,3,5,5,1))
sBTAModulesRPCModPortEntry.setIndexNames((0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:sBTAModulesRPCModPortEntry.setStatus(_A)
_SRPCModuleIndex_Type=Integer32
_SRPCModuleIndex_Object=MibTableColumn
sRPCModuleIndex=_SRPCModuleIndex_Object((1,3,6,1,4,1,4779,1,3,5,5,1,1),_SRPCModuleIndex_Type())
sRPCModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCModuleIndex.setStatus(_A)
_SRPCPortIndex_Type=Integer32
_SRPCPortIndex_Object=MibTableColumn
sRPCPortIndex=_SRPCPortIndex_Object((1,3,6,1,4,1,4779,1,3,5,5,1,2),_SRPCPortIndex_Type())
sRPCPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCPortIndex.setStatus(_A)
_SRPCType_Type=DisplayString
_SRPCType_Object=MibTableColumn
sRPCType=_SRPCType_Object((1,3,6,1,4,1,4779,1,3,5,5,1,3),_SRPCType_Type())
sRPCType.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCType.setStatus(_A)
_SRPCName_Type=DisplayString
_SRPCName_Object=MibTableColumn
sRPCName=_SRPCName_Object((1,3,6,1,4,1,4779,1,3,5,5,1,4),_SRPCName_Type())
sRPCName.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCName.setStatus(_A)
_SRPCFirmwareVersion_Type=DisplayString
_SRPCFirmwareVersion_Object=MibTableColumn
sRPCFirmwareVersion=_SRPCFirmwareVersion_Object((1,3,6,1,4,1,4779,1,3,5,5,1,5),_SRPCFirmwareVersion_Type())
sRPCFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCFirmwareVersion.setStatus(_A)
_SRPCCurrent_Type=Integer32
_SRPCCurrent_Object=MibTableColumn
sRPCCurrent=_SRPCCurrent_Object((1,3,6,1,4,1,4779,1,3,5,5,1,6),_SRPCCurrent_Type())
sRPCCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCCurrent.setStatus(_A)
_SRPCMaxCurrent_Type=Integer32
_SRPCMaxCurrent_Object=MibTableColumn
sRPCMaxCurrent=_SRPCMaxCurrent_Object((1,3,6,1,4,1,4779,1,3,5,5,1,7),_SRPCMaxCurrent_Type())
sRPCMaxCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCMaxCurrent.setStatus(_A)
_SRPCVoltage_Type=Integer32
_SRPCVoltage_Object=MibTableColumn
sRPCVoltage=_SRPCVoltage_Object((1,3,6,1,4,1,4779,1,3,5,5,1,8),_SRPCVoltage_Type())
sRPCVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCVoltage.setStatus(_A)
_SRPCPower_Type=Integer32
_SRPCPower_Object=MibTableColumn
sRPCPower=_SRPCPower_Object((1,3,6,1,4,1,4779,1,3,5,5,1,9),_SRPCPower_Type())
sRPCPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCPower.setStatus(_A)
_SRPCTemperature_Type=Integer32
_SRPCTemperature_Object=MibTableColumn
sRPCTemperature=_SRPCTemperature_Object((1,3,6,1,4,1,4779,1,3,5,5,1,10),_SRPCTemperature_Type())
sRPCTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCTemperature.setStatus(_A)
_SRPCRebootTimeout_Type=Integer32
_SRPCRebootTimeout_Object=MibTableColumn
sRPCRebootTimeout=_SRPCRebootTimeout_Object((1,3,6,1,4,1,4779,1,3,5,5,1,11),_SRPCRebootTimeout_Type())
sRPCRebootTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCRebootTimeout.setStatus(_A)
class _SRPCAllOutletsCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_K,0),(_L,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_O,6)))
_SRPCAllOutletsCmd_Type.__name__=_E
_SRPCAllOutletsCmd_Object=MibTableColumn
sRPCAllOutletsCmd=_SRPCAllOutletsCmd_Object((1,3,6,1,4,1,4779,1,3,5,5,1,12),_SRPCAllOutletsCmd_Type())
sRPCAllOutletsCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCAllOutletsCmd.setStatus(_A)
_SRPCAllOutletsStatus_Type=DisplayString
_SRPCAllOutletsStatus_Object=MibTableColumn
sRPCAllOutletsStatus=_SRPCAllOutletsStatus_Object((1,3,6,1,4,1,4779,1,3,5,5,1,13),_SRPCAllOutletsStatus_Type())
sRPCAllOutletsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCAllOutletsStatus.setStatus(_A)
_SRPCCurrentAlarmThreshold_Type=Integer32
_SRPCCurrentAlarmThreshold_Object=MibTableColumn
sRPCCurrentAlarmThreshold=_SRPCCurrentAlarmThreshold_Object((1,3,6,1,4,1,4779,1,3,5,5,1,14),_SRPCCurrentAlarmThreshold_Type())
sRPCCurrentAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCCurrentAlarmThreshold.setStatus(_A)
_SRPCOverVoltageThreshold_Type=Integer32
_SRPCOverVoltageThreshold_Object=MibTableColumn
sRPCOverVoltageThreshold=_SRPCOverVoltageThreshold_Object((1,3,6,1,4,1,4779,1,3,5,5,1,15),_SRPCOverVoltageThreshold_Type())
sRPCOverVoltageThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCOverVoltageThreshold.setStatus(_A)
_SRPCUnderVoltageThreshold_Type=Integer32
_SRPCUnderVoltageThreshold_Object=MibTableColumn
sRPCUnderVoltageThreshold=_SRPCUnderVoltageThreshold_Object((1,3,6,1,4,1,4779,1,3,5,5,1,16),_SRPCUnderVoltageThreshold_Type())
sRPCUnderVoltageThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCUnderVoltageThreshold.setStatus(_A)
_SRPCNumberOfOutlets_Type=Integer32
_SRPCNumberOfOutlets_Object=MibTableColumn
sRPCNumberOfOutlets=_SRPCNumberOfOutlets_Object((1,3,6,1,4,1,4779,1,3,5,5,1,17),_SRPCNumberOfOutlets_Type())
sRPCNumberOfOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCNumberOfOutlets.setStatus(_A)
class _SRPCCircuitBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_SRPCCircuitBreaker_Type.__name__=_E
_SRPCCircuitBreaker_Object=MibTableColumn
sRPCCircuitBreaker=_SRPCCircuitBreaker_Object((1,3,6,1,4,1,4779,1,3,5,5,1,18),_SRPCCircuitBreaker_Type())
sRPCCircuitBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCCircuitBreaker.setStatus(_A)
_SRPCOverTempThreshold_Type=Integer32
_SRPCOverTempThreshold_Object=MibTableColumn
sRPCOverTempThreshold=_SRPCOverTempThreshold_Object((1,3,6,1,4,1,4779,1,3,5,5,1,19),_SRPCOverTempThreshold_Type())
sRPCOverTempThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCOverTempThreshold.setStatus(_A)
_SRPCUnitVA_Type=Integer32
_SRPCUnitVA_Object=MibTableColumn
sRPCUnitVA=_SRPCUnitVA_Object((1,3,6,1,4,1,4779,1,3,5,5,1,20),_SRPCUnitVA_Type())
sRPCUnitVA.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCUnitVA.setStatus(_A)
_SRPCNumberOfBreakers_Type=Integer32
_SRPCNumberOfBreakers_Object=MibTableColumn
sRPCNumberOfBreakers=_SRPCNumberOfBreakers_Object((1,3,6,1,4,1,4779,1,3,5,5,1,21),_SRPCNumberOfBreakers_Type())
sRPCNumberOfBreakers.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCNumberOfBreakers.setStatus(_A)
_SRPCLowCurrentThreshold_Type=Integer32
_SRPCLowCurrentThreshold_Object=MibTableColumn
sRPCLowCurrentThreshold=_SRPCLowCurrentThreshold_Object((1,3,6,1,4,1,4779,1,3,5,5,1,22),_SRPCLowCurrentThreshold_Type())
sRPCLowCurrentThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCLowCurrentThreshold.setStatus(_A)
_SRPCVoltageSource_Type=Integer32
_SRPCVoltageSource_Object=MibTableColumn
sRPCVoltageSource=_SRPCVoltageSource_Object((1,3,6,1,4,1,4779,1,3,5,5,1,23),_SRPCVoltageSource_Type())
sRPCVoltageSource.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCVoltageSource.setStatus(_A)
_SRPCSourceSwitchCount_Type=Integer32
_SRPCSourceSwitchCount_Object=MibTableColumn
sRPCSourceSwitchCount=_SRPCSourceSwitchCount_Object((1,3,6,1,4,1,4779,1,3,5,5,1,24),_SRPCSourceSwitchCount_Type())
sRPCSourceSwitchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCSourceSwitchCount.setStatus(_A)
_SRPCNumberOfSensors_Type=Integer32
_SRPCNumberOfSensors_Object=MibTableColumn
sRPCNumberOfSensors=_SRPCNumberOfSensors_Object((1,3,6,1,4,1,4779,1,3,5,5,1,25),_SRPCNumberOfSensors_Type())
sRPCNumberOfSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCNumberOfSensors.setStatus(_A)
_SBTAModulesRPCModPortOutletTable_Object=MibTable
sBTAModulesRPCModPortOutletTable=_SBTAModulesRPCModPortOutletTable_Object((1,3,6,1,4,1,4779,1,3,5,6))
if mibBuilder.loadTexts:sBTAModulesRPCModPortOutletTable.setStatus(_A)
_SBTAModulesRPCModPortOutletEntry_Object=MibTableRow
sBTAModulesRPCModPortOutletEntry=_SBTAModulesRPCModPortOutletEntry_Object((1,3,6,1,4,1,4779,1,3,5,6,1))
sBTAModulesRPCModPortOutletEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:sBTAModulesRPCModPortOutletEntry.setStatus(_A)
_SRPCOutletModuleIndex_Type=Integer32
_SRPCOutletModuleIndex_Object=MibTableColumn
sRPCOutletModuleIndex=_SRPCOutletModuleIndex_Object((1,3,6,1,4,1,4779,1,3,5,6,1,1),_SRPCOutletModuleIndex_Type())
sRPCOutletModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCOutletModuleIndex.setStatus(_A)
_SRPCOutletPortIndex_Type=Integer32
_SRPCOutletPortIndex_Object=MibTableColumn
sRPCOutletPortIndex=_SRPCOutletPortIndex_Object((1,3,6,1,4,1,4779,1,3,5,6,1,2),_SRPCOutletPortIndex_Type())
sRPCOutletPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCOutletPortIndex.setStatus(_A)
_SRPCOutletIndex_Type=Integer32
_SRPCOutletIndex_Object=MibTableColumn
sRPCOutletIndex=_SRPCOutletIndex_Object((1,3,6,1,4,1,4779,1,3,5,6,1,3),_SRPCOutletIndex_Type())
sRPCOutletIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCOutletIndex.setStatus(_A)
class _SRPCOutletState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_K,0),(_L,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_O,6)))
_SRPCOutletState_Type.__name__=_E
_SRPCOutletState_Object=MibTableColumn
sRPCOutletState=_SRPCOutletState_Object((1,3,6,1,4,1,4779,1,3,5,6,1,4),_SRPCOutletState_Type())
sRPCOutletState.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCOutletState.setStatus(_A)
_SRPCOutletName_Type=DisplayString
_SRPCOutletName_Object=MibTableColumn
sRPCOutletName=_SRPCOutletName_Object((1,3,6,1,4,1,4779,1,3,5,6,1,5),_SRPCOutletName_Type())
sRPCOutletName.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCOutletName.setStatus(_A)
_SBTAModulesRPCModPortGroupCmd_Type=DisplayString
_SBTAModulesRPCModPortGroupCmd_Object=MibScalar
sBTAModulesRPCModPortGroupCmd=_SBTAModulesRPCModPortGroupCmd_Object((1,3,6,1,4,1,4779,1,3,5,7),_SBTAModulesRPCModPortGroupCmd_Type())
sBTAModulesRPCModPortGroupCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCModPortGroupCmd.setStatus(_A)
_SBTAModulesRPCCurrentGroupsCurrentTable_Object=MibTable
sBTAModulesRPCCurrentGroupsCurrentTable=_SBTAModulesRPCCurrentGroupsCurrentTable_Object((1,3,6,1,4,1,4779,1,3,5,8))
if mibBuilder.loadTexts:sBTAModulesRPCCurrentGroupsCurrentTable.setStatus(_A)
_SBTAModulesRPCCurrentGroupsCurrentEntry_Object=MibTableRow
sBTAModulesRPCCurrentGroupsCurrentEntry=_SBTAModulesRPCCurrentGroupsCurrentEntry_Object((1,3,6,1,4,1,4779,1,3,5,8,1))
sBTAModulesRPCCurrentGroupsCurrentEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:sBTAModulesRPCCurrentGroupsCurrentEntry.setStatus(_A)
_GroupCurrentIndex_Type=Integer32
_GroupCurrentIndex_Object=MibTableColumn
groupCurrentIndex=_GroupCurrentIndex_Object((1,3,6,1,4,1,4779,1,3,5,8,1,1),_GroupCurrentIndex_Type())
groupCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:groupCurrentIndex.setStatus(_A)
_GroupCurrent_Type=Integer32
_GroupCurrent_Object=MibTableColumn
groupCurrent=_GroupCurrent_Object((1,3,6,1,4,1,4779,1,3,5,8,1,2),_GroupCurrent_Type())
groupCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:groupCurrent.setStatus(_A)
_RpcGroup_Type=DisplayString
_RpcGroup_Object=MibTableColumn
rpcGroup=_RpcGroup_Object((1,3,6,1,4,1,4779,1,3,5,8,1,3),_RpcGroup_Type())
rpcGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:rpcGroup.setStatus(_A)
_WarningThreshold_Type=Integer32
_WarningThreshold_Object=MibTableColumn
warningThreshold=_WarningThreshold_Object((1,3,6,1,4,1,4779,1,3,5,8,1,4),_WarningThreshold_Type())
warningThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:warningThreshold.setStatus(_A)
_EmergencyThreshold_Type=Integer32
_EmergencyThreshold_Object=MibTableColumn
emergencyThreshold=_EmergencyThreshold_Object((1,3,6,1,4,1,4779,1,3,5,8,1,5),_EmergencyThreshold_Type())
emergencyThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:emergencyThreshold.setStatus(_A)
_SBTAModulesRPCBreakersTable_Object=MibTable
sBTAModulesRPCBreakersTable=_SBTAModulesRPCBreakersTable_Object((1,3,6,1,4,1,4779,1,3,5,9))
if mibBuilder.loadTexts:sBTAModulesRPCBreakersTable.setStatus(_A)
_SBTAModulesRPCBreakersEntry_Object=MibTableRow
sBTAModulesRPCBreakersEntry=_SBTAModulesRPCBreakersEntry_Object((1,3,6,1,4,1,4779,1,3,5,9,1))
sBTAModulesRPCBreakersEntry.setIndexNames((0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:sBTAModulesRPCBreakersEntry.setStatus(_A)
_SBTAModulesRPCBreakersModulesIndex_Type=Integer32
_SBTAModulesRPCBreakersModulesIndex_Object=MibTableColumn
sBTAModulesRPCBreakersModulesIndex=_SBTAModulesRPCBreakersModulesIndex_Object((1,3,6,1,4,1,4779,1,3,5,9,1,1),_SBTAModulesRPCBreakersModulesIndex_Type())
sBTAModulesRPCBreakersModulesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersModulesIndex.setStatus(_A)
_SBTAModulesRPCBreakersBreakersIndex_Type=Integer32
_SBTAModulesRPCBreakersBreakersIndex_Object=MibTableColumn
sBTAModulesRPCBreakersBreakersIndex=_SBTAModulesRPCBreakersBreakersIndex_Object((1,3,6,1,4,1,4779,1,3,5,9,1,2),_SBTAModulesRPCBreakersBreakersIndex_Type())
sBTAModulesRPCBreakersBreakersIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersBreakersIndex.setStatus(_A)
class _SBTAModulesRPCBreakersCircuitBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_SBTAModulesRPCBreakersCircuitBreaker_Type.__name__=_E
_SBTAModulesRPCBreakersCircuitBreaker_Object=MibTableColumn
sBTAModulesRPCBreakersCircuitBreaker=_SBTAModulesRPCBreakersCircuitBreaker_Object((1,3,6,1,4,1,4779,1,3,5,9,1,3),_SBTAModulesRPCBreakersCircuitBreaker_Type())
sBTAModulesRPCBreakersCircuitBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersCircuitBreaker.setStatus(_A)
_SBTAModulesRPCBreakersCurrent_Type=Integer32
_SBTAModulesRPCBreakersCurrent_Object=MibTableColumn
sBTAModulesRPCBreakersCurrent=_SBTAModulesRPCBreakersCurrent_Object((1,3,6,1,4,1,4779,1,3,5,9,1,4),_SBTAModulesRPCBreakersCurrent_Type())
sBTAModulesRPCBreakersCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersCurrent.setStatus(_A)
_SBTAModulesRPCBreakersMaxCurrent_Type=Integer32
_SBTAModulesRPCBreakersMaxCurrent_Object=MibTableColumn
sBTAModulesRPCBreakersMaxCurrent=_SBTAModulesRPCBreakersMaxCurrent_Object((1,3,6,1,4,1,4779,1,3,5,9,1,5),_SBTAModulesRPCBreakersMaxCurrent_Type())
sBTAModulesRPCBreakersMaxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersMaxCurrent.setStatus(_A)
_SBTAModulesRPCBreakersVoltage_Type=Integer32
_SBTAModulesRPCBreakersVoltage_Object=MibTableColumn
sBTAModulesRPCBreakersVoltage=_SBTAModulesRPCBreakersVoltage_Object((1,3,6,1,4,1,4779,1,3,5,9,1,6),_SBTAModulesRPCBreakersVoltage_Type())
sBTAModulesRPCBreakersVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersVoltage.setStatus(_A)
_SBTAModulesRPCBreakersPower_Type=Integer32
_SBTAModulesRPCBreakersPower_Object=MibTableColumn
sBTAModulesRPCBreakersPower=_SBTAModulesRPCBreakersPower_Object((1,3,6,1,4,1,4779,1,3,5,9,1,7),_SBTAModulesRPCBreakersPower_Type())
sBTAModulesRPCBreakersPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersPower.setStatus(_A)
_SBTAModulesRPCBreakersVA_Type=Integer32
_SBTAModulesRPCBreakersVA_Object=MibTableColumn
sBTAModulesRPCBreakersVA=_SBTAModulesRPCBreakersVA_Object((1,3,6,1,4,1,4779,1,3,5,9,1,8),_SBTAModulesRPCBreakersVA_Type())
sBTAModulesRPCBreakersVA.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersVA.setStatus(_A)
_SBTAModulesRPCBreakersCurrentAlarmThreshold_Type=Integer32
_SBTAModulesRPCBreakersCurrentAlarmThreshold_Object=MibTableColumn
sBTAModulesRPCBreakersCurrentAlarmThreshold=_SBTAModulesRPCBreakersCurrentAlarmThreshold_Object((1,3,6,1,4,1,4779,1,3,5,9,1,9),_SBTAModulesRPCBreakersCurrentAlarmThreshold_Type())
sBTAModulesRPCBreakersCurrentAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesRPCBreakersCurrentAlarmThreshold.setStatus(_A)
_SRPCModPortBreakersTable_Object=MibTable
sRPCModPortBreakersTable=_SRPCModPortBreakersTable_Object((1,3,6,1,4,1,4779,1,3,5,10))
if mibBuilder.loadTexts:sRPCModPortBreakersTable.setStatus(_A)
_SRPCModPortBreakersEntry_Object=MibTableRow
sRPCModPortBreakersEntry=_SRPCModPortBreakersEntry_Object((1,3,6,1,4,1,4779,1,3,5,10,1))
sRPCModPortBreakersEntry.setIndexNames((0,_C,_j),(0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:sRPCModPortBreakersEntry.setStatus(_A)
_SRPCBreakersModIndex_Type=Integer32
_SRPCBreakersModIndex_Object=MibTableColumn
sRPCBreakersModIndex=_SRPCBreakersModIndex_Object((1,3,6,1,4,1,4779,1,3,5,10,1,1),_SRPCBreakersModIndex_Type())
sRPCBreakersModIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersModIndex.setStatus(_A)
_SRPCBreakersPortIndex_Type=Integer32
_SRPCBreakersPortIndex_Object=MibTableColumn
sRPCBreakersPortIndex=_SRPCBreakersPortIndex_Object((1,3,6,1,4,1,4779,1,3,5,10,1,2),_SRPCBreakersPortIndex_Type())
sRPCBreakersPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersPortIndex.setStatus(_A)
_SRPCBreakersBreakersIndex_Type=Integer32
_SRPCBreakersBreakersIndex_Object=MibTableColumn
sRPCBreakersBreakersIndex=_SRPCBreakersBreakersIndex_Object((1,3,6,1,4,1,4779,1,3,5,10,1,3),_SRPCBreakersBreakersIndex_Type())
sRPCBreakersBreakersIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersBreakersIndex.setStatus(_A)
class _SRPCBreakersCircuitBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_SRPCBreakersCircuitBreaker_Type.__name__=_E
_SRPCBreakersCircuitBreaker_Object=MibTableColumn
sRPCBreakersCircuitBreaker=_SRPCBreakersCircuitBreaker_Object((1,3,6,1,4,1,4779,1,3,5,10,1,4),_SRPCBreakersCircuitBreaker_Type())
sRPCBreakersCircuitBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersCircuitBreaker.setStatus(_A)
_SRPCBreakersCurrent_Type=Integer32
_SRPCBreakersCurrent_Object=MibTableColumn
sRPCBreakersCurrent=_SRPCBreakersCurrent_Object((1,3,6,1,4,1,4779,1,3,5,10,1,5),_SRPCBreakersCurrent_Type())
sRPCBreakersCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersCurrent.setStatus(_A)
_SRPCBreakersMaxCurrent_Type=Integer32
_SRPCBreakersMaxCurrent_Object=MibTableColumn
sRPCBreakersMaxCurrent=_SRPCBreakersMaxCurrent_Object((1,3,6,1,4,1,4779,1,3,5,10,1,6),_SRPCBreakersMaxCurrent_Type())
sRPCBreakersMaxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersMaxCurrent.setStatus(_A)
_SRPCBreakersVoltage_Type=Integer32
_SRPCBreakersVoltage_Object=MibTableColumn
sRPCBreakersVoltage=_SRPCBreakersVoltage_Object((1,3,6,1,4,1,4779,1,3,5,10,1,7),_SRPCBreakersVoltage_Type())
sRPCBreakersVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersVoltage.setStatus(_A)
_SRPCBreakersPower_Type=Integer32
_SRPCBreakersPower_Object=MibTableColumn
sRPCBreakersPower=_SRPCBreakersPower_Object((1,3,6,1,4,1,4779,1,3,5,10,1,8),_SRPCBreakersPower_Type())
sRPCBreakersPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersPower.setStatus(_A)
_SRPCBreakersVA_Type=Integer32
_SRPCBreakersVA_Object=MibTableColumn
sRPCBreakersVA=_SRPCBreakersVA_Object((1,3,6,1,4,1,4779,1,3,5,10,1,9),_SRPCBreakersVA_Type())
sRPCBreakersVA.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCBreakersVA.setStatus(_A)
_SRPCBreakersCurrentAlarmThreshold_Type=Integer32
_SRPCBreakersCurrentAlarmThreshold_Object=MibTableColumn
sRPCBreakersCurrentAlarmThreshold=_SRPCBreakersCurrentAlarmThreshold_Object((1,3,6,1,4,1,4779,1,3,5,10,1,10),_SRPCBreakersCurrentAlarmThreshold_Type())
sRPCBreakersCurrentAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCBreakersCurrentAlarmThreshold.setStatus(_A)
_SBTAModulesSerial_ObjectIdentity=ObjectIdentity
sBTAModulesSerial=_SBTAModulesSerial_ObjectIdentity((1,3,6,1,4,1,4779,1,3,6))
_SBTAModulesModem_ObjectIdentity=ObjectIdentity
sBTAModulesModem=_SBTAModulesModem_ObjectIdentity((1,3,6,1,4,1,4779,1,3,7))
_SBTAControl_ObjectIdentity=ObjectIdentity
sBTAControl=_SBTAControl_ObjectIdentity((1,3,6,1,4,1,4779,1,4))
class _SBTAControlResetUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_m,0),('reset',1)))
_SBTAControlResetUnit_Type.__name__=_E
_SBTAControlResetUnit_Object=MibScalar
sBTAControlResetUnit=_SBTAControlResetUnit_Object((1,3,6,1,4,1,4779,1,4,1),_SBTAControlResetUnit_Type())
sBTAControlResetUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAControlResetUnit.setStatus(_A)
class _SBTAControlResetModules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_m,0),('reset',1)))
_SBTAControlResetModules_Type.__name__=_E
_SBTAControlResetModules_Object=MibScalar
sBTAControlResetModules=_SBTAControlResetModules_Object((1,3,6,1,4,1,4779,1,4,2),_SBTAControlResetModules_Type())
sBTAControlResetModules.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAControlResetModules.setStatus(_A)
_SBTAControlNumOfLoggedUsers_Type=Integer32
_SBTAControlNumOfLoggedUsers_Object=MibScalar
sBTAControlNumOfLoggedUsers=_SBTAControlNumOfLoggedUsers_Object((1,3,6,1,4,1,4779,1,4,3),_SBTAControlNumOfLoggedUsers_Type())
sBTAControlNumOfLoggedUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlNumOfLoggedUsers.setStatus(_A)
_SBTAControlUserTable_Object=MibTable
sBTAControlUserTable=_SBTAControlUserTable_Object((1,3,6,1,4,1,4779,1,4,4))
if mibBuilder.loadTexts:sBTAControlUserTable.setStatus(_A)
_SBTAControlUserEntry_Object=MibTableRow
sBTAControlUserEntry=_SBTAControlUserEntry_Object((1,3,6,1,4,1,4779,1,4,4,1))
sBTAControlUserEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:sBTAControlUserEntry.setStatus(_A)
_SBTAControlUserIndex_Type=Integer32
_SBTAControlUserIndex_Object=MibTableColumn
sBTAControlUserIndex=_SBTAControlUserIndex_Object((1,3,6,1,4,1,4779,1,4,4,1,1),_SBTAControlUserIndex_Type())
sBTAControlUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlUserIndex.setStatus(_A)
_SBTAControlUserName_Type=DisplayString
_SBTAControlUserName_Object=MibTableColumn
sBTAControlUserName=_SBTAControlUserName_Object((1,3,6,1,4,1,4779,1,4,4,1,2),_SBTAControlUserName_Type())
sBTAControlUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlUserName.setStatus(_A)
_SBTAControlUserAddress_Type=IpAddress
_SBTAControlUserAddress_Object=MibTableColumn
sBTAControlUserAddress=_SBTAControlUserAddress_Object((1,3,6,1,4,1,4779,1,4,4,1,3),_SBTAControlUserAddress_Type())
sBTAControlUserAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlUserAddress.setStatus(_A)
class _SBTAControlUserConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('serialport',0),('telnet',1),('ssh',2),(_O,4)))
_SBTAControlUserConnection_Type.__name__=_E
_SBTAControlUserConnection_Object=MibTableColumn
sBTAControlUserConnection=_SBTAControlUserConnection_Object((1,3,6,1,4,1,4779,1,4,4,1,4),_SBTAControlUserConnection_Type())
sBTAControlUserConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlUserConnection.setStatus(_A)
_SBTAControlUserConnModule_Type=Integer32
_SBTAControlUserConnModule_Object=MibTableColumn
sBTAControlUserConnModule=_SBTAControlUserConnModule_Object((1,3,6,1,4,1,4779,1,4,4,1,5),_SBTAControlUserConnModule_Type())
sBTAControlUserConnModule.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlUserConnModule.setStatus(_A)
_SBTAControlUserConnPort_Type=Integer32
_SBTAControlUserConnPort_Object=MibTableColumn
sBTAControlUserConnPort=_SBTAControlUserConnPort_Object((1,3,6,1,4,1,4779,1,4,4,1,6),_SBTAControlUserConnPort_Type())
sBTAControlUserConnPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAControlUserConnPort.setStatus(_A)
class _SBTAControlUserTerminateUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('terminate',1))
_SBTAControlUserTerminateUser_Type.__name__=_E
_SBTAControlUserTerminateUser_Object=MibTableColumn
sBTAControlUserTerminateUser=_SBTAControlUserTerminateUser_Object((1,3,6,1,4,1,4779,1,4,4,1,7),_SBTAControlUserTerminateUser_Type())
sBTAControlUserTerminateUser.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAControlUserTerminateUser.setStatus(_A)
_SBTAFileTransfer_ObjectIdentity=ObjectIdentity
sBTAFileTransfer=_SBTAFileTransfer_ObjectIdentity((1,3,6,1,4,1,4779,1,5))
class _SBTAFileTransferEnableUpgradeFTPFileTransfer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('enableUpgradeFileTransferDownloadViaFTP',1))
_SBTAFileTransferEnableUpgradeFTPFileTransfer_Type.__name__=_E
_SBTAFileTransferEnableUpgradeFTPFileTransfer_Object=MibScalar
sBTAFileTransferEnableUpgradeFTPFileTransfer=_SBTAFileTransferEnableUpgradeFTPFileTransfer_Object((1,3,6,1,4,1,4779,1,5,1),_SBTAFileTransferEnableUpgradeFTPFileTransfer_Type())
sBTAFileTransferEnableUpgradeFTPFileTransfer.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAFileTransferEnableUpgradeFTPFileTransfer.setStatus(_A)
_SBTAEnvironmental_ObjectIdentity=ObjectIdentity
sBTAEnvironmental=_SBTAEnvironmental_ObjectIdentity((1,3,6,1,4,1,4779,1,6))
_SBTAModulesEnvironmentalObjectsTable_Object=MibTable
sBTAModulesEnvironmentalObjectsTable=_SBTAModulesEnvironmentalObjectsTable_Object((1,3,6,1,4,1,4779,1,6,1))
if mibBuilder.loadTexts:sBTAModulesEnvironmentalObjectsTable.setStatus(_A)
_SBTAModulesEnvironmentalObjectsEntry_Object=MibTableRow
sBTAModulesEnvironmentalObjectsEntry=_SBTAModulesEnvironmentalObjectsEntry_Object((1,3,6,1,4,1,4779,1,6,1,1))
sBTAModulesEnvironmentalObjectsEntry.setIndexNames((0,_C,_o),(0,_C,_p))
if mibBuilder.loadTexts:sBTAModulesEnvironmentalObjectsEntry.setStatus(_A)
_SBTAModulesEnvironmentalModulesIndex_Type=Integer32
_SBTAModulesEnvironmentalModulesIndex_Object=MibTableColumn
sBTAModulesEnvironmentalModulesIndex=_SBTAModulesEnvironmentalModulesIndex_Object((1,3,6,1,4,1,4779,1,6,1,1,1),_SBTAModulesEnvironmentalModulesIndex_Type())
sBTAModulesEnvironmentalModulesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalModulesIndex.setStatus(_A)
_SBTAModulesEnvironmentalSensorsIndex_Type=Integer32
_SBTAModulesEnvironmentalSensorsIndex_Object=MibTableColumn
sBTAModulesEnvironmentalSensorsIndex=_SBTAModulesEnvironmentalSensorsIndex_Object((1,3,6,1,4,1,4779,1,6,1,1,2),_SBTAModulesEnvironmentalSensorsIndex_Type())
sBTAModulesEnvironmentalSensorsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalSensorsIndex.setStatus(_A)
_SBTAModulesEnvironmentalType_Type=Integer32
_SBTAModulesEnvironmentalType_Object=MibTableColumn
sBTAModulesEnvironmentalType=_SBTAModulesEnvironmentalType_Object((1,3,6,1,4,1,4779,1,6,1,1,3),_SBTAModulesEnvironmentalType_Type())
sBTAModulesEnvironmentalType.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalType.setStatus(_A)
_SBTAModulesEnvironmentalName_Type=DisplayString
_SBTAModulesEnvironmentalName_Object=MibTableColumn
sBTAModulesEnvironmentalName=_SBTAModulesEnvironmentalName_Object((1,3,6,1,4,1,4779,1,6,1,1,4),_SBTAModulesEnvironmentalName_Type())
sBTAModulesEnvironmentalName.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalName.setStatus(_A)
_SBTAModulesEnvironmentalMeasurement_Type=Integer32
_SBTAModulesEnvironmentalMeasurement_Object=MibTableColumn
sBTAModulesEnvironmentalMeasurement=_SBTAModulesEnvironmentalMeasurement_Object((1,3,6,1,4,1,4779,1,6,1,1,5),_SBTAModulesEnvironmentalMeasurement_Type())
sBTAModulesEnvironmentalMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalMeasurement.setStatus(_A)
_SBTAModulesEnvironmentalHiThreshold_Type=Integer32
_SBTAModulesEnvironmentalHiThreshold_Object=MibTableColumn
sBTAModulesEnvironmentalHiThreshold=_SBTAModulesEnvironmentalHiThreshold_Object((1,3,6,1,4,1,4779,1,6,1,1,6),_SBTAModulesEnvironmentalHiThreshold_Type())
sBTAModulesEnvironmentalHiThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalHiThreshold.setStatus(_A)
_SBTAModulesEnvironmentalLoThreshold_Type=Integer32
_SBTAModulesEnvironmentalLoThreshold_Object=MibTableColumn
sBTAModulesEnvironmentalLoThreshold=_SBTAModulesEnvironmentalLoThreshold_Object((1,3,6,1,4,1,4779,1,6,1,1,7),_SBTAModulesEnvironmentalLoThreshold_Type())
sBTAModulesEnvironmentalLoThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalLoThreshold.setStatus(_A)
_SBTAModulesEnvironmentalMax_Type=Integer32
_SBTAModulesEnvironmentalMax_Object=MibTableColumn
sBTAModulesEnvironmentalMax=_SBTAModulesEnvironmentalMax_Object((1,3,6,1,4,1,4779,1,6,1,1,8),_SBTAModulesEnvironmentalMax_Type())
sBTAModulesEnvironmentalMax.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalMax.setStatus(_A)
_SBTAModulesEnvironmentalMin_Type=Integer32
_SBTAModulesEnvironmentalMin_Object=MibTableColumn
sBTAModulesEnvironmentalMin=_SBTAModulesEnvironmentalMin_Object((1,3,6,1,4,1,4779,1,6,1,1,9),_SBTAModulesEnvironmentalMin_Type())
sBTAModulesEnvironmentalMin.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalMin.setStatus(_A)
_SBTAModulesEnvironmentalHiThresholdEn_Type=Integer32
_SBTAModulesEnvironmentalHiThresholdEn_Object=MibTableColumn
sBTAModulesEnvironmentalHiThresholdEn=_SBTAModulesEnvironmentalHiThresholdEn_Object((1,3,6,1,4,1,4779,1,6,1,1,10),_SBTAModulesEnvironmentalHiThresholdEn_Type())
sBTAModulesEnvironmentalHiThresholdEn.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalHiThresholdEn.setStatus(_A)
_SBTAModulesEnvironmentalLoThresholdEn_Type=Integer32
_SBTAModulesEnvironmentalLoThresholdEn_Object=MibTableColumn
sBTAModulesEnvironmentalLoThresholdEn=_SBTAModulesEnvironmentalLoThresholdEn_Object((1,3,6,1,4,1,4779,1,6,1,1,11),_SBTAModulesEnvironmentalLoThresholdEn_Type())
sBTAModulesEnvironmentalLoThresholdEn.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalLoThresholdEn.setStatus(_A)
_SBTAModulesEnvironmentalStateTrapEn_Type=Integer32
_SBTAModulesEnvironmentalStateTrapEn_Object=MibTableColumn
sBTAModulesEnvironmentalStateTrapEn=_SBTAModulesEnvironmentalStateTrapEn_Object((1,3,6,1,4,1,4779,1,6,1,1,12),_SBTAModulesEnvironmentalStateTrapEn_Type())
sBTAModulesEnvironmentalStateTrapEn.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAModulesEnvironmentalStateTrapEn.setStatus(_A)
_SRPCEnvironmentalObjectsTable_Object=MibTable
sRPCEnvironmentalObjectsTable=_SRPCEnvironmentalObjectsTable_Object((1,3,6,1,4,1,4779,1,6,2))
if mibBuilder.loadTexts:sRPCEnvironmentalObjectsTable.setStatus(_A)
_SRPCEnvironmentalObjectsEntry_Object=MibTableRow
sRPCEnvironmentalObjectsEntry=_SRPCEnvironmentalObjectsEntry_Object((1,3,6,1,4,1,4779,1,6,2,1))
sRPCEnvironmentalObjectsEntry.setIndexNames((0,_C,'sBTAEnvironmentalModuleIndex'),(0,_C,'sBTAEnvironmentalPortIndex'),(0,_C,'sBTAEnvironmentalSensorsIndex'))
if mibBuilder.loadTexts:sRPCEnvironmentalObjectsEntry.setStatus(_A)
_SRPCEnvironmentalModuleIndex_Type=Integer32
_SRPCEnvironmentalModuleIndex_Object=MibTableColumn
sRPCEnvironmentalModuleIndex=_SRPCEnvironmentalModuleIndex_Object((1,3,6,1,4,1,4779,1,6,2,1,1),_SRPCEnvironmentalModuleIndex_Type())
sRPCEnvironmentalModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCEnvironmentalModuleIndex.setStatus(_A)
_SRPCEnvironmentalPortIndex_Type=Integer32
_SRPCEnvironmentalPortIndex_Object=MibTableColumn
sRPCEnvironmentalPortIndex=_SRPCEnvironmentalPortIndex_Object((1,3,6,1,4,1,4779,1,6,2,1,2),_SRPCEnvironmentalPortIndex_Type())
sRPCEnvironmentalPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCEnvironmentalPortIndex.setStatus(_A)
_SRPCEnvironmentalSensorsIndex_Type=Integer32
_SRPCEnvironmentalSensorsIndex_Object=MibTableColumn
sRPCEnvironmentalSensorsIndex=_SRPCEnvironmentalSensorsIndex_Object((1,3,6,1,4,1,4779,1,6,2,1,3),_SRPCEnvironmentalSensorsIndex_Type())
sRPCEnvironmentalSensorsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCEnvironmentalSensorsIndex.setStatus(_A)
_SRPCEnvironmentalType_Type=Integer32
_SRPCEnvironmentalType_Object=MibTableColumn
sRPCEnvironmentalType=_SRPCEnvironmentalType_Object((1,3,6,1,4,1,4779,1,6,2,1,4),_SRPCEnvironmentalType_Type())
sRPCEnvironmentalType.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCEnvironmentalType.setStatus(_A)
_SRPCEnvironmentalName_Type=DisplayString
_SRPCEnvironmentalName_Object=MibTableColumn
sRPCEnvironmentalName=_SRPCEnvironmentalName_Object((1,3,6,1,4,1,4779,1,6,2,1,5),_SRPCEnvironmentalName_Type())
sRPCEnvironmentalName.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalName.setStatus(_A)
_SRPCEnvironmentalMeasurement_Type=Integer32
_SRPCEnvironmentalMeasurement_Object=MibTableColumn
sRPCEnvironmentalMeasurement=_SRPCEnvironmentalMeasurement_Object((1,3,6,1,4,1,4779,1,6,2,1,6),_SRPCEnvironmentalMeasurement_Type())
sRPCEnvironmentalMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:sRPCEnvironmentalMeasurement.setStatus(_A)
_SRPCEnvironmentalHiThreshold_Type=Integer32
_SRPCEnvironmentalHiThreshold_Object=MibTableColumn
sRPCEnvironmentalHiThreshold=_SRPCEnvironmentalHiThreshold_Object((1,3,6,1,4,1,4779,1,6,2,1,7),_SRPCEnvironmentalHiThreshold_Type())
sRPCEnvironmentalHiThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalHiThreshold.setStatus(_A)
_SRPCEnvironmentalLoThreshold_Type=Integer32
_SRPCEnvironmentalLoThreshold_Object=MibTableColumn
sRPCEnvironmentalLoThreshold=_SRPCEnvironmentalLoThreshold_Object((1,3,6,1,4,1,4779,1,6,2,1,8),_SRPCEnvironmentalLoThreshold_Type())
sRPCEnvironmentalLoThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalLoThreshold.setStatus(_A)
_SRPCEnvironmentalMax_Type=Integer32
_SRPCEnvironmentalMax_Object=MibTableColumn
sRPCEnvironmentalMax=_SRPCEnvironmentalMax_Object((1,3,6,1,4,1,4779,1,6,2,1,9),_SRPCEnvironmentalMax_Type())
sRPCEnvironmentalMax.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalMax.setStatus(_A)
_SRPCEnvironmentalMin_Type=Integer32
_SRPCEnvironmentalMin_Object=MibTableColumn
sRPCEnvironmentalMin=_SRPCEnvironmentalMin_Object((1,3,6,1,4,1,4779,1,6,2,1,10),_SRPCEnvironmentalMin_Type())
sRPCEnvironmentalMin.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalMin.setStatus(_A)
_SRPCEnvironmentalHiThresholdEn_Type=Integer32
_SRPCEnvironmentalHiThresholdEn_Object=MibTableColumn
sRPCEnvironmentalHiThresholdEn=_SRPCEnvironmentalHiThresholdEn_Object((1,3,6,1,4,1,4779,1,6,2,1,11),_SRPCEnvironmentalHiThresholdEn_Type())
sRPCEnvironmentalHiThresholdEn.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalHiThresholdEn.setStatus(_A)
_SRPCEnvironmentalLoThresholdEn_Type=Integer32
_SRPCEnvironmentalLoThresholdEn_Object=MibTableColumn
sRPCEnvironmentalLoThresholdEn=_SRPCEnvironmentalLoThresholdEn_Object((1,3,6,1,4,1,4779,1,6,2,1,12),_SRPCEnvironmentalLoThresholdEn_Type())
sRPCEnvironmentalLoThresholdEn.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalLoThresholdEn.setStatus(_A)
_SRPCEnvironmentalStateTrapEn_Type=Integer32
_SRPCEnvironmentalStateTrapEn_Object=MibTableColumn
sRPCEnvironmentalStateTrapEn=_SRPCEnvironmentalStateTrapEn_Object((1,3,6,1,4,1,4779,1,6,2,1,13),_SRPCEnvironmentalStateTrapEn_Type())
sRPCEnvironmentalStateTrapEn.setMaxAccess(_D)
if mibBuilder.loadTexts:sRPCEnvironmentalStateTrapEn.setStatus(_A)
_SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Type=Integer32
_SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Object=MibScalar
sBTAEnvironmentalAllTemperatureSensorsHiThreshold=_SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Object((1,3,6,1,4,1,4779,1,6,3),_SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Type())
sBTAEnvironmentalAllTemperatureSensorsHiThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAEnvironmentalAllTemperatureSensorsHiThreshold.setStatus(_A)
_SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Type=Integer32
_SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Object=MibScalar
sBTAEnvironmentalAllTemperatureSensorsLoThreshold=_SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Object((1,3,6,1,4,1,4779,1,6,4),_SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Type())
sBTAEnvironmentalAllTemperatureSensorsLoThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAEnvironmentalAllTemperatureSensorsLoThreshold.setStatus(_A)
_SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Type=Integer32
_SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Object=MibScalar
sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable=_SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Object((1,3,6,1,4,1,4779,1,6,5),_SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Type())
sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable.setStatus(_A)
_SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Type=Integer32
_SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Object=MibScalar
sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable=_SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Object((1,3,6,1,4,1,4779,1,6,6),_SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Type())
sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable.setStatus(_A)
_SBTAEnvironmentalAllSensorsStateTrapEnable_Type=Integer32
_SBTAEnvironmentalAllSensorsStateTrapEnable_Object=MibScalar
sBTAEnvironmentalAllSensorsStateTrapEnable=_SBTAEnvironmentalAllSensorsStateTrapEnable_Object((1,3,6,1,4,1,4779,1,6,7),_SBTAEnvironmentalAllSensorsStateTrapEnable_Type())
sBTAEnvironmentalAllSensorsStateTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAEnvironmentalAllSensorsStateTrapEnable.setStatus(_A)
_Mtrapargs_ObjectIdentity=ObjectIdentity
mtrapargs=_Mtrapargs_ObjectIdentity((1,3,6,1,4,1,4779,3))
_MtrapargsInteger_Type=Integer32
_MtrapargsInteger_Object=MibScalar
mtrapargsInteger=_MtrapargsInteger_Object((1,3,6,1,4,1,4779,3,1),_MtrapargsInteger_Type())
mtrapargsInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:mtrapargsInteger.setStatus(_A)
_MtrapargsIpAddress_Type=IpAddress
_MtrapargsIpAddress_Object=MibScalar
mtrapargsIpAddress=_MtrapargsIpAddress_Object((1,3,6,1,4,1,4779,3,2),_MtrapargsIpAddress_Type())
mtrapargsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mtrapargsIpAddress.setStatus(_A)
_MtrapargsString_Type=DisplayString
_MtrapargsString_Object=MibScalar
mtrapargsString=_MtrapargsString_Object((1,3,6,1,4,1,4779,3,3),_MtrapargsString_Type())
mtrapargsString.setMaxAccess(_B)
if mibBuilder.loadTexts:mtrapargsString.setStatus(_A)
_MtrapargsGauge_Type=Gauge32
_MtrapargsGauge_Object=MibScalar
mtrapargsGauge=_MtrapargsGauge_Object((1,3,6,1,4,1,4779,3,4),_MtrapargsGauge_Type())
mtrapargsGauge.setMaxAccess(_B)
if mibBuilder.loadTexts:mtrapargsGauge.setStatus(_A)
_MtrapargsTimeTicks_Type=TimeTicks
_MtrapargsTimeTicks_Object=MibScalar
mtrapargsTimeTicks=_MtrapargsTimeTicks_Object((1,3,6,1,4,1,4779,3,5),_MtrapargsTimeTicks_Type())
mtrapargsTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:mtrapargsTimeTicks.setStatus(_A)
_SBTAModuleIndex_Type=Integer32
_SBTAModuleIndex_Object=MibScalar
sBTAModuleIndex=_SBTAModuleIndex_Object((1,3,6,1,4,1,4779,3,6),_SBTAModuleIndex_Type())
sBTAModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAModuleIndex.setStatus(_A)
_SBTAOutletIndex_Type=Integer32
_SBTAOutletIndex_Object=MibScalar
sBTAOutletIndex=_SBTAOutletIndex_Object((1,3,6,1,4,1,4779,3,7),_SBTAOutletIndex_Type())
sBTAOutletIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAOutletIndex.setStatus(_A)
_SBTAPortIndex_Type=Integer32
_SBTAPortIndex_Object=MibScalar
sBTAPortIndex=_SBTAPortIndex_Object((1,3,6,1,4,1,4779,3,8),_SBTAPortIndex_Type())
sBTAPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTAPortIndex.setStatus(_A)
_SBTAVoltageSource_Type=Integer32
_SBTAVoltageSource_Object=MibScalar
sBTAVoltageSource=_SBTAVoltageSource_Object((1,3,6,1,4,1,4779,3,9),_SBTAVoltageSource_Type())
sBTAVoltageSource.setMaxAccess(_D)
if mibBuilder.loadTexts:sBTAVoltageSource.setStatus(_A)
_SBTASourceSwitchCount_Type=Integer32
_SBTASourceSwitchCount_Object=MibScalar
sBTASourceSwitchCount=_SBTASourceSwitchCount_Object((1,3,6,1,4,1,4779,3,10),_SBTASourceSwitchCount_Type())
sBTASourceSwitchCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTASourceSwitchCount.setStatus(_A)
_SBTASensorIndex_Type=Integer32
_SBTASensorIndex_Object=MibScalar
sBTASensorIndex=_SBTASensorIndex_Object((1,3,6,1,4,1,4779,3,11),_SBTASensorIndex_Type())
sBTASensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTASensorIndex.setStatus(_A)
_SBTABreakerIndex_Type=Integer32
_SBTABreakerIndex_Object=MibScalar
sBTABreakerIndex=_SBTABreakerIndex_Object((1,3,6,1,4,1,4779,3,12),_SBTABreakerIndex_Type())
sBTABreakerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sBTABreakerIndex.setStatus(_A)
communicationLost=NotificationType((1,3,6,1,4,1,4779,0,1))
communicationLost.setObjects((_C,_q))
if mibBuilder.loadTexts:communicationLost.setStatus('')
communicationEstablished=NotificationType((1,3,6,1,4,1,4779,0,2))
communicationEstablished.setObjects((_C,_H))
if mibBuilder.loadTexts:communicationEstablished.setStatus('')
outletOn=NotificationType((1,3,6,1,4,1,4779,0,3))
outletOn.setObjects(*((_C,_G),(_C,_N)))
if mibBuilder.loadTexts:outletOn.setStatus('')
outletOff=NotificationType((1,3,6,1,4,1,4779,0,4))
outletOff.setObjects(*((_C,_G),(_C,_N)))
if mibBuilder.loadTexts:outletOff.setStatus('')
outletReboot=NotificationType((1,3,6,1,4,1,4779,0,5))
outletReboot.setObjects(*((_C,_G),(_C,_N)))
if mibBuilder.loadTexts:outletReboot.setStatus('')
outletLocked=NotificationType((1,3,6,1,4,1,4779,0,6))
outletLocked.setObjects(*((_C,_G),(_C,_N)))
if mibBuilder.loadTexts:outletLocked.setStatus('')
outletUnlocked=NotificationType((1,3,6,1,4,1,4779,0,7))
outletUnlocked.setObjects(*((_C,_G),(_C,_N)))
if mibBuilder.loadTexts:outletUnlocked.setStatus('')
configChangeSNMP=NotificationType((1,3,6,1,4,1,4779,0,8))
if mibBuilder.loadTexts:configChangeSNMP.setStatus('')
configChangeOutlet=NotificationType((1,3,6,1,4,1,4779,0,9))
configChangeOutlet.setObjects(*((_C,_G),(_C,_N)))
if mibBuilder.loadTexts:configChangeOutlet.setStatus('')
accessViolationConsole=NotificationType((1,3,6,1,4,1,4779,0,10))
accessViolationConsole.setObjects((_C,_H))
if mibBuilder.loadTexts:accessViolationConsole.setStatus('')
accessViolationNetwork=NotificationType((1,3,6,1,4,1,4779,0,11))
accessViolationNetwork.setObjects((_C,_H))
if mibBuilder.loadTexts:accessViolationNetwork.setStatus('')
userPasswordChange=NotificationType((1,3,6,1,4,1,4779,0,12))
userPasswordChange.setObjects((_C,_H))
if mibBuilder.loadTexts:userPasswordChange.setStatus('')
userAdded=NotificationType((1,3,6,1,4,1,4779,0,13))
userAdded.setObjects((_C,_H))
if mibBuilder.loadTexts:userAdded.setStatus('')
userLoggedIn=NotificationType((1,3,6,1,4,1,4779,0,14))
userLoggedIn.setObjects((_C,_H))
if mibBuilder.loadTexts:userLoggedIn.setStatus('')
temperatureThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,15))
temperatureThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:temperatureThresholdViolation.setStatus('')
temperatureThresholdViolationCleared=NotificationType((1,3,6,1,4,1,4779,0,16))
temperatureThresholdViolationCleared.setObjects((_C,_F))
if mibBuilder.loadTexts:temperatureThresholdViolationCleared.setStatus('')
currentThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,17))
currentThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:currentThresholdViolation.setStatus('')
currentThresholdViolationCleared=NotificationType((1,3,6,1,4,1,4779,0,18))
currentThresholdViolationCleared.setObjects((_C,_H))
if mibBuilder.loadTexts:currentThresholdViolationCleared.setStatus('')
resetModulesEvent=NotificationType((1,3,6,1,4,1,4779,0,19))
resetModulesEvent.setObjects((_C,_H))
if mibBuilder.loadTexts:resetModulesEvent.setStatus('')
resetModulesComplete=NotificationType((1,3,6,1,4,1,4779,0,20))
resetModulesComplete.setObjects((_C,_H))
if mibBuilder.loadTexts:resetModulesComplete.setStatus('')
errorExecutingSNMPCommand=NotificationType((1,3,6,1,4,1,4779,0,21))
errorExecutingSNMPCommand.setObjects((_C,_H))
if mibBuilder.loadTexts:errorExecutingSNMPCommand.setStatus('')
fileTransferComplete=NotificationType((1,3,6,1,4,1,4779,0,22))
if mibBuilder.loadTexts:fileTransferComplete.setStatus('')
userTerminated=NotificationType((1,3,6,1,4,1,4779,0,23))
userTerminated.setObjects((_C,_F))
if mibBuilder.loadTexts:userTerminated.setStatus('')
voltageOverThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,24))
voltageOverThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:voltageOverThresholdViolation.setStatus('')
voltageOverThresholdViolationCleared=NotificationType((1,3,6,1,4,1,4779,0,25))
voltageOverThresholdViolationCleared.setObjects((_C,_F))
if mibBuilder.loadTexts:voltageOverThresholdViolationCleared.setStatus('')
voltageUnderThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,26))
voltageUnderThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:voltageUnderThresholdViolation.setStatus('')
voltageUnderThresholdViolationCleared=NotificationType((1,3,6,1,4,1,4779,0,27))
voltageUnderThresholdViolationCleared.setObjects((_C,_F))
if mibBuilder.loadTexts:voltageUnderThresholdViolationCleared.setStatus('')
circuitBreakerAlarm=NotificationType((1,3,6,1,4,1,4779,0,28))
circuitBreakerAlarm.setObjects((_C,_F))
if mibBuilder.loadTexts:circuitBreakerAlarm.setStatus('')
rpcFailureAlarm=NotificationType((1,3,6,1,4,1,4779,0,29))
rpcFailureAlarm.setObjects((_C,_F))
if mibBuilder.loadTexts:rpcFailureAlarm.setStatus('')
userDeleted=NotificationType((1,3,6,1,4,1,4779,0,30))
userDeleted.setObjects((_C,_H))
if mibBuilder.loadTexts:userDeleted.setStatus('')
warningThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,31))
warningThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:warningThresholdViolation.setStatus('')
warningThresholdViolationClear=NotificationType((1,3,6,1,4,1,4779,0,32))
warningThresholdViolationClear.setObjects((_C,_F))
if mibBuilder.loadTexts:warningThresholdViolationClear.setStatus('')
emergencyThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,33))
emergencyThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:emergencyThresholdViolation.setStatus('')
emergencyThresholdViolationClear=NotificationType((1,3,6,1,4,1,4779,0,34))
emergencyThresholdViolationClear.setObjects((_C,_F))
if mibBuilder.loadTexts:emergencyThresholdViolationClear.setStatus('')
circuitBreakerAlarmClearTrap=NotificationType((1,3,6,1,4,1,4779,0,35))
circuitBreakerAlarmClearTrap.setObjects((_C,_F))
if mibBuilder.loadTexts:circuitBreakerAlarmClearTrap.setStatus('')
currentUnderThresholdViolation=NotificationType((1,3,6,1,4,1,4779,0,36))
currentUnderThresholdViolation.setObjects((_C,_F))
if mibBuilder.loadTexts:currentUnderThresholdViolation.setStatus('')
currentUnderThresholdViolationCleared=NotificationType((1,3,6,1,4,1,4779,0,37))
currentUnderThresholdViolationCleared.setObjects((_C,_F))
if mibBuilder.loadTexts:currentUnderThresholdViolationCleared.setStatus('')
voltageSourceChangeAlarm=NotificationType((1,3,6,1,4,1,4779,0,38))
voltageSourceChangeAlarm.setObjects(*((_C,_G),(_C,_r),(_C,_s)))
if mibBuilder.loadTexts:voltageSourceChangeAlarm.setStatus('')
sensorTempThreshHiAlarmTrap=NotificationType((1,3,6,1,4,1,4779,0,39))
sensorTempThreshHiAlarmTrap.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:sensorTempThreshHiAlarmTrap.setStatus('')
sensorTempThreshHiAlarmClearedTrap=NotificationType((1,3,6,1,4,1,4779,0,40))
sensorTempThreshHiAlarmClearedTrap.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:sensorTempThreshHiAlarmClearedTrap.setStatus('')
sensorTempThreshLoAlarmTrap=NotificationType((1,3,6,1,4,1,4779,0,41))
sensorTempThreshLoAlarmTrap.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:sensorTempThreshLoAlarmTrap.setStatus('')
sensorTempThreshLoAlarmClearedTrap=NotificationType((1,3,6,1,4,1,4779,0,42))
sensorTempThreshLoAlarmClearedTrap.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:sensorTempThreshLoAlarmClearedTrap.setStatus('')
sensorStateChangeTrap=NotificationType((1,3,6,1,4,1,4779,0,43))
sensorStateChangeTrap.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:sensorStateChangeTrap.setStatus('')
configChangeSensor=NotificationType((1,3,6,1,4,1,4779,0,44))
configChangeSensor.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:configChangeSensor.setStatus('')
sensorTypeChange=NotificationType((1,3,6,1,4,1,4779,0,45))
sensorTypeChange.setObjects(*((_C,_G),(_C,_M)))
if mibBuilder.loadTexts:sensorTypeChange.setStatus('')
mibBuilder.exportSymbols(_C,**{'baytech':baytech,'communicationLost':communicationLost,'communicationEstablished':communicationEstablished,'outletOn':outletOn,'outletOff':outletOff,'outletReboot':outletReboot,'outletLocked':outletLocked,'outletUnlocked':outletUnlocked,'configChangeSNMP':configChangeSNMP,'configChangeOutlet':configChangeOutlet,'accessViolationConsole':accessViolationConsole,'accessViolationNetwork':accessViolationNetwork,'userPasswordChange':userPasswordChange,'userAdded':userAdded,'userLoggedIn':userLoggedIn,'temperatureThresholdViolation':temperatureThresholdViolation,'temperatureThresholdViolationCleared':temperatureThresholdViolationCleared,'currentThresholdViolation':currentThresholdViolation,'currentThresholdViolationCleared':currentThresholdViolationCleared,'resetModulesEvent':resetModulesEvent,'resetModulesComplete':resetModulesComplete,'errorExecutingSNMPCommand':errorExecutingSNMPCommand,'fileTransferComplete':fileTransferComplete,'userTerminated':userTerminated,'voltageOverThresholdViolation':voltageOverThresholdViolation,'voltageOverThresholdViolationCleared':voltageOverThresholdViolationCleared,'voltageUnderThresholdViolation':voltageUnderThresholdViolation,'voltageUnderThresholdViolationCleared':voltageUnderThresholdViolationCleared,'circuitBreakerAlarm':circuitBreakerAlarm,'rpcFailureAlarm':rpcFailureAlarm,'userDeleted':userDeleted,'warningThresholdViolation':warningThresholdViolation,'warningThresholdViolationClear':warningThresholdViolationClear,'emergencyThresholdViolation':emergencyThresholdViolation,'emergencyThresholdViolationClear':emergencyThresholdViolationClear,'circuitBreakerAlarmClearTrap':circuitBreakerAlarmClearTrap,'currentUnderThresholdViolation':currentUnderThresholdViolation,'currentUnderThresholdViolationCleared':currentUnderThresholdViolationCleared,'voltageSourceChangeAlarm':voltageSourceChangeAlarm,'sensorTempThreshHiAlarmTrap':sensorTempThreshHiAlarmTrap,'sensorTempThreshHiAlarmClearedTrap':sensorTempThreshHiAlarmClearedTrap,'sensorTempThreshLoAlarmTrap':sensorTempThreshLoAlarmTrap,'sensorTempThreshLoAlarmClearedTrap':sensorTempThreshLoAlarmClearedTrap,'sensorStateChangeTrap':sensorStateChangeTrap,'configChangeSensor':configChangeSensor,'sensorTypeChange':sensorTypeChange,'btadevices':btadevices,'sBTAIdent':sBTAIdent,'sBTAIdentFirmwareRev':sBTAIdentFirmwareRev,'sBTAIdentSerialNumber':sBTAIdentSerialNumber,'sBTAIdentUnitName':sBTAIdentUnitName,'sBTANetworkConfig':sBTANetworkConfig,'sBTANetworkConfigBootpEnable':sBTANetworkConfigBootpEnable,'sBTANetworkConfigDHCPEnable':sBTANetworkConfigDHCPEnable,'sBTANetworkConfigSSHEnable':sBTANetworkConfigSSHEnable,'sBTANetworkConfigTelnetEnable':sBTANetworkConfigTelnetEnable,'sBTANetworkConfigActivityTimeout':sBTANetworkConfigActivityTimeout,'sBTANetworkConfigDirectConnEnable':sBTANetworkConfigDirectConnEnable,'sBTANetworkConfigSNMP':sBTANetworkConfigSNMP,'sBTANetworkConfigSNMPReadOnlyCommunity':sBTANetworkConfigSNMPReadOnlyCommunity,'sBTANetworkConfigSNMPReadWriteCommunity':sBTANetworkConfigSNMPReadWriteCommunity,'sBTANetworkConfigSNMPNumTrapReceivers':sBTANetworkConfigSNMPNumTrapReceivers,'sBTANetworkConfigSNMPTrapReceiverTable':sBTANetworkConfigSNMPTrapReceiverTable,'sBTANetworkConfigSNMPTrapReceiverEntry':sBTANetworkConfigSNMPTrapReceiverEntry,_V:trapIndex,'receiverAddress':receiverAddress,'sBTANetworkConfigRadius':sBTANetworkConfigRadius,'sBTANetworkConfigRadiusEnable':sBTANetworkConfigRadiusEnable,'sBTANetworkConfigRadiusPrimaryServer':sBTANetworkConfigRadiusPrimaryServer,'sBTANetworkConfigRadiusSecondaryServer':sBTANetworkConfigRadiusSecondaryServer,'sBTANetworkConfigRadiusLocalLogin':sBTANetworkConfigRadiusLocalLogin,'sBTANetworkConfigWEB':sBTANetworkConfigWEB,'sBTANetworkConfigWebEnable':sBTANetworkConfigWebEnable,'sBTANetworkConfigWebSecureEnable':sBTANetworkConfigWebSecureEnable,'sBTANetworkConfigWebLoginEnable':sBTANetworkConfigWebLoginEnable,'sBTANetworkConfigWebActivityTimeout':sBTANetworkConfigWebActivityTimeout,'sBTAModules':sBTAModules,'sBTAModulesNumberOfModules':sBTAModulesNumberOfModules,'sBTAModulesModulesInstalled':sBTAModulesModulesInstalled,'sBTAModulesResetModulesCmd':sBTAModulesResetModulesCmd,'sBTAModulesNumberOfIntelligentModules':sBTAModulesNumberOfIntelligentModules,'sBTAModulesRPC':sBTAModulesRPC,'sBTAModulesNumberOfRPCModules':sBTAModulesNumberOfRPCModules,'sBTAModulesRPCTable':sBTAModulesRPCTable,'sBTAModulesRPCEntry':sBTAModulesRPCEntry,_Y:sBTAModulesRPCIndex,'sBTAModulesRPCName':sBTAModulesRPCName,'sBTAModulesRPCFirmwareVersion':sBTAModulesRPCFirmwareVersion,'sBTAModulesRPCCurrent':sBTAModulesRPCCurrent,'sBTAModulesRPCMaxCurrent':sBTAModulesRPCMaxCurrent,'sBTAModulesRPCVoltage':sBTAModulesRPCVoltage,'sBTAModulesRPCPower':sBTAModulesRPCPower,'sBTAModulesRPCTemperature':sBTAModulesRPCTemperature,'sBTAModulesRPCRebootTimeout':sBTAModulesRPCRebootTimeout,'sBTAModulesRPCAllOutletsCmd':sBTAModulesRPCAllOutletsCmd,'sBTAModulesRPCAllOutletsStatus':sBTAModulesRPCAllOutletsStatus,'sBTAModulesRPCCurrentAlarmThreshold':sBTAModulesRPCCurrentAlarmThreshold,'sBTAModulesRPCOverVoltageThreshold':sBTAModulesRPCOverVoltageThreshold,'sBTAModulesRPCUnderVoltageThreshold':sBTAModulesRPCUnderVoltageThreshold,'sBTAModulesRPCNumberOfOutlets':sBTAModulesRPCNumberOfOutlets,'sBTAModulesRPCCircuitBreaker':sBTAModulesRPCCircuitBreaker,'sBTAModulesRPCOverTempThreshold':sBTAModulesRPCOverTempThreshold,'sBTAModulesRPCUnitVA':sBTAModulesRPCUnitVA,'sBTAModulesRPCNumberOfBreakers':sBTAModulesRPCNumberOfBreakers,'sBTAModulesRPCLowCurrentThreshold':sBTAModulesRPCLowCurrentThreshold,'sBTAModulesRPCVoltageSource':sBTAModulesRPCVoltageSource,'sBTAModulesRPCSourceSwitchCount':sBTAModulesRPCSourceSwitchCount,'sBTAModulesRPCNumberOfSensors':sBTAModulesRPCNumberOfSensors,'sBTAModulesRPCType':sBTAModulesRPCType,'sBTAModulesRPCOutletTable':sBTAModulesRPCOutletTable,'sBTAModulesRPCOutletEntry':sBTAModulesRPCOutletEntry,_Z:sBTAModulesRPCOutletModuleIndex,_a:sBTAModulesRPCOutletIndex,'sBTAModulesRPCOutletState':sBTAModulesRPCOutletState,'sBTAModulesRPCOutletName':sBTAModulesRPCOutletName,'sBTAModulesRPCGroupCmd':sBTAModulesRPCGroupCmd,'sBTAModulesRPCModPortTable':sBTAModulesRPCModPortTable,'sBTAModulesRPCModPortEntry':sBTAModulesRPCModPortEntry,_b:sRPCModuleIndex,_c:sRPCPortIndex,'sRPCType':sRPCType,'sRPCName':sRPCName,'sRPCFirmwareVersion':sRPCFirmwareVersion,'sRPCCurrent':sRPCCurrent,'sRPCMaxCurrent':sRPCMaxCurrent,'sRPCVoltage':sRPCVoltage,'sRPCPower':sRPCPower,'sRPCTemperature':sRPCTemperature,'sRPCRebootTimeout':sRPCRebootTimeout,'sRPCAllOutletsCmd':sRPCAllOutletsCmd,'sRPCAllOutletsStatus':sRPCAllOutletsStatus,'sRPCCurrentAlarmThreshold':sRPCCurrentAlarmThreshold,'sRPCOverVoltageThreshold':sRPCOverVoltageThreshold,'sRPCUnderVoltageThreshold':sRPCUnderVoltageThreshold,'sRPCNumberOfOutlets':sRPCNumberOfOutlets,'sRPCCircuitBreaker':sRPCCircuitBreaker,'sRPCOverTempThreshold':sRPCOverTempThreshold,'sRPCUnitVA':sRPCUnitVA,'sRPCNumberOfBreakers':sRPCNumberOfBreakers,'sRPCLowCurrentThreshold':sRPCLowCurrentThreshold,'sRPCVoltageSource':sRPCVoltageSource,'sRPCSourceSwitchCount':sRPCSourceSwitchCount,'sRPCNumberOfSensors':sRPCNumberOfSensors,'sBTAModulesRPCModPortOutletTable':sBTAModulesRPCModPortOutletTable,'sBTAModulesRPCModPortOutletEntry':sBTAModulesRPCModPortOutletEntry,_d:sRPCOutletModuleIndex,_e:sRPCOutletPortIndex,_f:sRPCOutletIndex,'sRPCOutletState':sRPCOutletState,'sRPCOutletName':sRPCOutletName,'sBTAModulesRPCModPortGroupCmd':sBTAModulesRPCModPortGroupCmd,'sBTAModulesRPCCurrentGroupsCurrentTable':sBTAModulesRPCCurrentGroupsCurrentTable,'sBTAModulesRPCCurrentGroupsCurrentEntry':sBTAModulesRPCCurrentGroupsCurrentEntry,_g:groupCurrentIndex,'groupCurrent':groupCurrent,'rpcGroup':rpcGroup,'warningThreshold':warningThreshold,'emergencyThreshold':emergencyThreshold,'sBTAModulesRPCBreakersTable':sBTAModulesRPCBreakersTable,'sBTAModulesRPCBreakersEntry':sBTAModulesRPCBreakersEntry,_h:sBTAModulesRPCBreakersModulesIndex,_i:sBTAModulesRPCBreakersBreakersIndex,'sBTAModulesRPCBreakersCircuitBreaker':sBTAModulesRPCBreakersCircuitBreaker,'sBTAModulesRPCBreakersCurrent':sBTAModulesRPCBreakersCurrent,'sBTAModulesRPCBreakersMaxCurrent':sBTAModulesRPCBreakersMaxCurrent,'sBTAModulesRPCBreakersVoltage':sBTAModulesRPCBreakersVoltage,'sBTAModulesRPCBreakersPower':sBTAModulesRPCBreakersPower,'sBTAModulesRPCBreakersVA':sBTAModulesRPCBreakersVA,'sBTAModulesRPCBreakersCurrentAlarmThreshold':sBTAModulesRPCBreakersCurrentAlarmThreshold,'sRPCModPortBreakersTable':sRPCModPortBreakersTable,'sRPCModPortBreakersEntry':sRPCModPortBreakersEntry,_j:sRPCBreakersModIndex,_k:sRPCBreakersPortIndex,_l:sRPCBreakersBreakersIndex,'sRPCBreakersCircuitBreaker':sRPCBreakersCircuitBreaker,'sRPCBreakersCurrent':sRPCBreakersCurrent,'sRPCBreakersMaxCurrent':sRPCBreakersMaxCurrent,'sRPCBreakersVoltage':sRPCBreakersVoltage,'sRPCBreakersPower':sRPCBreakersPower,'sRPCBreakersVA':sRPCBreakersVA,'sRPCBreakersCurrentAlarmThreshold':sRPCBreakersCurrentAlarmThreshold,'sBTAModulesSerial':sBTAModulesSerial,'sBTAModulesModem':sBTAModulesModem,'sBTAControl':sBTAControl,'sBTAControlResetUnit':sBTAControlResetUnit,'sBTAControlResetModules':sBTAControlResetModules,'sBTAControlNumOfLoggedUsers':sBTAControlNumOfLoggedUsers,'sBTAControlUserTable':sBTAControlUserTable,'sBTAControlUserEntry':sBTAControlUserEntry,_n:sBTAControlUserIndex,'sBTAControlUserName':sBTAControlUserName,'sBTAControlUserAddress':sBTAControlUserAddress,'sBTAControlUserConnection':sBTAControlUserConnection,'sBTAControlUserConnModule':sBTAControlUserConnModule,'sBTAControlUserConnPort':sBTAControlUserConnPort,'sBTAControlUserTerminateUser':sBTAControlUserTerminateUser,'sBTAFileTransfer':sBTAFileTransfer,'sBTAFileTransferEnableUpgradeFTPFileTransfer':sBTAFileTransferEnableUpgradeFTPFileTransfer,'sBTAEnvironmental':sBTAEnvironmental,'sBTAModulesEnvironmentalObjectsTable':sBTAModulesEnvironmentalObjectsTable,'sBTAModulesEnvironmentalObjectsEntry':sBTAModulesEnvironmentalObjectsEntry,_o:sBTAModulesEnvironmentalModulesIndex,_p:sBTAModulesEnvironmentalSensorsIndex,'sBTAModulesEnvironmentalType':sBTAModulesEnvironmentalType,'sBTAModulesEnvironmentalName':sBTAModulesEnvironmentalName,'sBTAModulesEnvironmentalMeasurement':sBTAModulesEnvironmentalMeasurement,'sBTAModulesEnvironmentalHiThreshold':sBTAModulesEnvironmentalHiThreshold,'sBTAModulesEnvironmentalLoThreshold':sBTAModulesEnvironmentalLoThreshold,'sBTAModulesEnvironmentalMax':sBTAModulesEnvironmentalMax,'sBTAModulesEnvironmentalMin':sBTAModulesEnvironmentalMin,'sBTAModulesEnvironmentalHiThresholdEn':sBTAModulesEnvironmentalHiThresholdEn,'sBTAModulesEnvironmentalLoThresholdEn':sBTAModulesEnvironmentalLoThresholdEn,'sBTAModulesEnvironmentalStateTrapEn':sBTAModulesEnvironmentalStateTrapEn,'sRPCEnvironmentalObjectsTable':sRPCEnvironmentalObjectsTable,'sRPCEnvironmentalObjectsEntry':sRPCEnvironmentalObjectsEntry,'sRPCEnvironmentalModuleIndex':sRPCEnvironmentalModuleIndex,'sRPCEnvironmentalPortIndex':sRPCEnvironmentalPortIndex,'sRPCEnvironmentalSensorsIndex':sRPCEnvironmentalSensorsIndex,'sRPCEnvironmentalType':sRPCEnvironmentalType,'sRPCEnvironmentalName':sRPCEnvironmentalName,'sRPCEnvironmentalMeasurement':sRPCEnvironmentalMeasurement,'sRPCEnvironmentalHiThreshold':sRPCEnvironmentalHiThreshold,'sRPCEnvironmentalLoThreshold':sRPCEnvironmentalLoThreshold,'sRPCEnvironmentalMax':sRPCEnvironmentalMax,'sRPCEnvironmentalMin':sRPCEnvironmentalMin,'sRPCEnvironmentalHiThresholdEn':sRPCEnvironmentalHiThresholdEn,'sRPCEnvironmentalLoThresholdEn':sRPCEnvironmentalLoThresholdEn,'sRPCEnvironmentalStateTrapEn':sRPCEnvironmentalStateTrapEn,'sBTAEnvironmentalAllTemperatureSensorsHiThreshold':sBTAEnvironmentalAllTemperatureSensorsHiThreshold,'sBTAEnvironmentalAllTemperatureSensorsLoThreshold':sBTAEnvironmentalAllTemperatureSensorsLoThreshold,'sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable':sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable,'sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable':sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable,'sBTAEnvironmentalAllSensorsStateTrapEnable':sBTAEnvironmentalAllSensorsStateTrapEnable,'mtrapargs':mtrapargs,_F:mtrapargsInteger,'mtrapargsIpAddress':mtrapargsIpAddress,_H:mtrapargsString,'mtrapargsGauge':mtrapargsGauge,_q:mtrapargsTimeTicks,_G:sBTAModuleIndex,_N:sBTAOutletIndex,'sBTAPortIndex':sBTAPortIndex,_r:sBTAVoltageSource,_s:sBTASourceSwitchCount,_M:sBTASensorIndex,'sBTABreakerIndex':sBTABreakerIndex})