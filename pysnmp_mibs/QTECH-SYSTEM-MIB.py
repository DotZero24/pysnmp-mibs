_A9='qtechSystemMIBGroup'
_A8='qtechSystemHwFan'
_A7='qtechSystemHwPower'
_A6='qtechSystemHardChangeDesc'
_A5='qtechSwitchLayer'
_A4='qtechSystemOutBandRate'
_A3='qtechSystemReset'
_A2='qtechSystemParametersSave'
_A1='qtechSystemSysCtrlVersion'
_A0='qtechSystemBootVersion'
_z='qtechSystemSwVersion'
_y='qtechSystemHwVersion'
_x='qtechSystemOamFanPad3Index'
_w='qtechSystemOamFanPad2Index'
_v='qtechSystemOamFanPad1Index'
_u='qtechSystemPowerSNIndex'
_t='qtechSystemDsfIndex'
_s='qtechSystemFanPadIndex'
_r='qtechSystemApStatMacAddr'
_q='reserved'
_p='qtechSystemApDescMacAddr'
_o='qtechSystemMultipleTemperatureIndex'
_n='qtechSystemFanInformationFanIndex'
_m='qtechSystemFanInformationDeviceIndex'
_l='qtechSystemElectricalInformationIndex'
_k='qtechSystemElectricalInformationDeviceIndex'
_j='qtechSystemBoardTemperatureIndex'
_i='qtechSystemLankApMacAddr'
_h='qtechSystemVersionIndex'
_g='qtechSystemTemperatureIndex'
_f='qtechSystemFanIsNormalIndex'
_e='qtechSystemElectricalSourceIsNormalIndex'
_d='seconds'
_c='obsolete'
_b='restart'
_a='qtechSystemFanStatus'
_Z='qtechSystemSwitchID'
_Y='qtechSystemTemperatureCurrent'
_X='qtechSystemFanStatusDeviceIndex'
_W='qtechSystemMultipleTemperatureDeviceIndex'
_V='qtechSystemFanStatusIndex'
_U='qtechSystemFanStatusFanIndex'
_T='qtechSystemPowerIndex'
_S='unknow'
_R='powerbutabnormal'
_Q='existreadypower'
_P='existnopower'
_O='noexist'
_N='qtechCPUUtilization1Min'
_M='QTECH-PROCESS-MIB'
_L='qtechMemoryPoolCurrentUtilization'
_K='QTECH-MEMORY-MIB'
_J='qtechSystemMultipleTemperatureSlotIndex'
_I='qtechApMacAddr'
_H='QTECH-AC-MGMT-MIB'
_G='normal'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='QTECH-SYSTEM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechApMacAddr,=mibBuilder.importSymbols(_H,_I)
qtechMemoryPoolCurrentUtilization,=mibBuilder.importSymbols(_K,_L)
Percent,qtechCPUUtilization1Min=mibBuilder.importSymbols(_M,'Percent',_N)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
qtechSystemMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,1))
if mibBuilder.loadTexts:qtechSystemMIB.setRevisions(('2002-03-20 00:00',))
_QtechSystemMIBObjects_ObjectIdentity=ObjectIdentity
qtechSystemMIBObjects=_QtechSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,1,1))
class _QtechSystemHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSystemHwVersion_Type.__name__=_F
_QtechSystemHwVersion_Object=MibScalar
qtechSystemHwVersion=_QtechSystemHwVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,1),_QtechSystemHwVersion_Type())
qtechSystemHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemHwVersion.setStatus(_A)
class _QtechSystemSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSystemSwVersion_Type.__name__=_F
_QtechSystemSwVersion_Object=MibScalar
qtechSystemSwVersion=_QtechSystemSwVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,2),_QtechSystemSwVersion_Type())
qtechSystemSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSwVersion.setStatus(_A)
class _QtechSystemBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSystemBootVersion_Type.__name__=_F
_QtechSystemBootVersion_Object=MibScalar
qtechSystemBootVersion=_QtechSystemBootVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,3),_QtechSystemBootVersion_Type())
qtechSystemBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemBootVersion.setStatus(_A)
class _QtechSystemSysCtrlVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSystemSysCtrlVersion_Type.__name__=_F
_QtechSystemSysCtrlVersion_Object=MibScalar
qtechSystemSysCtrlVersion=_QtechSystemSysCtrlVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,4),_QtechSystemSysCtrlVersion_Type())
qtechSystemSysCtrlVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSysCtrlVersion.setStatus(_A)
_QtechSystemParametersSave_Type=Integer32
_QtechSystemParametersSave_Object=MibScalar
qtechSystemParametersSave=_QtechSystemParametersSave_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,5),_QtechSystemParametersSave_Type())
qtechSystemParametersSave.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemParametersSave.setStatus(_A)
class _QtechSystemOutBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('baud9600',1),('baud19200',2),('baud38400',3),('baud57600',4),('baud115200',5)))
_QtechSystemOutBandRate_Type.__name__=_D
_QtechSystemOutBandRate_Object=MibScalar
qtechSystemOutBandRate=_QtechSystemOutBandRate_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,6),_QtechSystemOutBandRate_Type())
qtechSystemOutBandRate.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemOutBandRate.setStatus(_A)
class _QtechSystemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_b,1)))
_QtechSystemReset_Type.__name__=_D
_QtechSystemReset_Object=MibScalar
qtechSystemReset=_QtechSystemReset_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,7),_QtechSystemReset_Type())
qtechSystemReset.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemReset.setStatus(_A)
class _QtechSwitchLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('layer2',1),('layer3',2),('router',3)))
_QtechSwitchLayer_Type.__name__=_D
_QtechSwitchLayer_Object=MibScalar
qtechSwitchLayer=_QtechSwitchLayer_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,8),_QtechSwitchLayer_Type())
qtechSwitchLayer.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSwitchLayer.setStatus(_A)
class _QtechSystemHwPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rpsNoLink',1),('rpsLinkAndNoPower',2),('rpsLinkAndReadyForPower',3),('rpsLinkAndPower',4)))
_QtechSystemHwPower_Type.__name__=_D
_QtechSystemHwPower_Object=MibScalar
qtechSystemHwPower=_QtechSystemHwPower_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,9),_QtechSystemHwPower_Type())
qtechSystemHwPower.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemHwPower.setStatus(_A)
class _QtechSystemHwFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('work',1),('stop',2)))
_QtechSystemHwFan_Type.__name__=_D
_QtechSystemHwFan_Object=MibScalar
qtechSystemHwFan=_QtechSystemHwFan_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,10),_QtechSystemHwFan_Type())
qtechSystemHwFan.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemHwFan.setStatus(_A)
class _QtechSystemOutBandTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_QtechSystemOutBandTimeout_Type.__name__=_D
_QtechSystemOutBandTimeout_Object=MibScalar
qtechSystemOutBandTimeout=_QtechSystemOutBandTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,11),_QtechSystemOutBandTimeout_Type())
qtechSystemOutBandTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemOutBandTimeout.setStatus(_c)
if mibBuilder.loadTexts:qtechSystemOutBandTimeout.setUnits(_d)
class _QtechSystemTelnetTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_QtechSystemTelnetTimeout_Type.__name__=_D
_QtechSystemTelnetTimeout_Object=MibScalar
qtechSystemTelnetTimeout=_QtechSystemTelnetTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,12),_QtechSystemTelnetTimeout_Type())
qtechSystemTelnetTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemTelnetTimeout.setStatus(_c)
if mibBuilder.loadTexts:qtechSystemTelnetTimeout.setUnits(_d)
class _QtechSystemMainFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QtechSystemMainFile_Type.__name__=_F
_QtechSystemMainFile_Object=MibScalar
qtechSystemMainFile=_QtechSystemMainFile_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,13),_QtechSystemMainFile_Type())
qtechSystemMainFile.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMainFile.setStatus(_A)
_QtechSystemCurrentPower_Type=Integer32
_QtechSystemCurrentPower_Object=MibScalar
qtechSystemCurrentPower=_QtechSystemCurrentPower_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,14),_QtechSystemCurrentPower_Type())
qtechSystemCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemCurrentPower.setStatus(_A)
_QtechSystemRemainPower_Type=Integer32
_QtechSystemRemainPower_Object=MibScalar
qtechSystemRemainPower=_QtechSystemRemainPower_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,15),_QtechSystemRemainPower_Type())
qtechSystemRemainPower.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemRemainPower.setStatus(_A)
_QtechSystemTemperature_Type=Integer32
_QtechSystemTemperature_Object=MibScalar
qtechSystemTemperature=_QtechSystemTemperature_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,16),_QtechSystemTemperature_Type())
qtechSystemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemTemperature.setStatus(_A)
_QtechSystemElectricalSourceNum_Type=Integer32
_QtechSystemElectricalSourceNum_Object=MibScalar
qtechSystemElectricalSourceNum=_QtechSystemElectricalSourceNum_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,17),_QtechSystemElectricalSourceNum_Type())
qtechSystemElectricalSourceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalSourceNum.setStatus(_A)
_QtechSystemElectricalSourceIsNormalTable_Object=MibTable
qtechSystemElectricalSourceIsNormalTable=_QtechSystemElectricalSourceIsNormalTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,18))
if mibBuilder.loadTexts:qtechSystemElectricalSourceIsNormalTable.setStatus(_A)
_QtechSystemElectricalSourceIsNormalEntry_Object=MibTableRow
qtechSystemElectricalSourceIsNormalEntry=_QtechSystemElectricalSourceIsNormalEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,18,1))
qtechSystemElectricalSourceIsNormalEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:qtechSystemElectricalSourceIsNormalEntry.setStatus(_A)
_QtechSystemElectricalSourceIsNormalIndex_Type=Integer32
_QtechSystemElectricalSourceIsNormalIndex_Object=MibTableColumn
qtechSystemElectricalSourceIsNormalIndex=_QtechSystemElectricalSourceIsNormalIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,18,1,1),_QtechSystemElectricalSourceIsNormalIndex_Type())
qtechSystemElectricalSourceIsNormalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalSourceIsNormalIndex.setStatus(_A)
class _QtechSystemElectricalSourceIsNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_G,4),(_R,5),(_S,6)))
_QtechSystemElectricalSourceIsNormal_Type.__name__=_D
_QtechSystemElectricalSourceIsNormal_Object=MibTableColumn
qtechSystemElectricalSourceIsNormal=_QtechSystemElectricalSourceIsNormal_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,18,1,2),_QtechSystemElectricalSourceIsNormal_Type())
qtechSystemElectricalSourceIsNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalSourceIsNormal.setStatus(_A)
_QtechSystemElectricalSourceName_Type=DisplayString
_QtechSystemElectricalSourceName_Object=MibTableColumn
qtechSystemElectricalSourceName=_QtechSystemElectricalSourceName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,18,1,3),_QtechSystemElectricalSourceName_Type())
qtechSystemElectricalSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalSourceName.setStatus(_A)
_QtechSystemCurrentVoltage_Type=Integer32
_QtechSystemCurrentVoltage_Object=MibScalar
qtechSystemCurrentVoltage=_QtechSystemCurrentVoltage_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,19),_QtechSystemCurrentVoltage_Type())
qtechSystemCurrentVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemCurrentVoltage.setStatus(_A)
_QtechSystemFanNUM_Type=Integer32
_QtechSystemFanNUM_Object=MibScalar
qtechSystemFanNUM=_QtechSystemFanNUM_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,20),_QtechSystemFanNUM_Type())
qtechSystemFanNUM.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanNUM.setStatus(_A)
_QtechSystemFanIsNormalTable_Object=MibTable
qtechSystemFanIsNormalTable=_QtechSystemFanIsNormalTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,21))
if mibBuilder.loadTexts:qtechSystemFanIsNormalTable.setStatus(_A)
_QtechSystemFanIsNormalEntry_Object=MibTableRow
qtechSystemFanIsNormalEntry=_QtechSystemFanIsNormalEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,21,1))
qtechSystemFanIsNormalEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:qtechSystemFanIsNormalEntry.setStatus(_A)
_QtechSystemFanIsNormalIndex_Type=Integer32
_QtechSystemFanIsNormalIndex_Object=MibTableColumn
qtechSystemFanIsNormalIndex=_QtechSystemFanIsNormalIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,21,1,1),_QtechSystemFanIsNormalIndex_Type())
qtechSystemFanIsNormalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanIsNormalIndex.setStatus(_A)
class _QtechSystemFanIsNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_G,4),(_R,5),(_S,6)))
_QtechSystemFanIsNormal_Type.__name__=_D
_QtechSystemFanIsNormal_Object=MibTableColumn
qtechSystemFanIsNormal=_QtechSystemFanIsNormal_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,21,1,2),_QtechSystemFanIsNormal_Type())
qtechSystemFanIsNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanIsNormal.setStatus(_A)
_QtechSystemFanName_Type=DisplayString
_QtechSystemFanName_Object=MibTableColumn
qtechSystemFanName=_QtechSystemFanName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,21,1,3),_QtechSystemFanName_Type())
qtechSystemFanName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanName.setStatus(_A)
_QtechSystemFanSpeed_Type=Integer32
_QtechSystemFanSpeed_Object=MibTableColumn
qtechSystemFanSpeed=_QtechSystemFanSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,21,1,4),_QtechSystemFanSpeed_Type())
qtechSystemFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanSpeed.setStatus(_A)
_QtechSystemReloadTimeRemain_Type=Integer32
_QtechSystemReloadTimeRemain_Object=MibScalar
qtechSystemReloadTimeRemain=_QtechSystemReloadTimeRemain_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,22),_QtechSystemReloadTimeRemain_Type())
qtechSystemReloadTimeRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemReloadTimeRemain.setStatus(_A)
_QtechSystemTemperatureTable_Object=MibTable
qtechSystemTemperatureTable=_QtechSystemTemperatureTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23))
if mibBuilder.loadTexts:qtechSystemTemperatureTable.setStatus(_A)
_QtechSystemTemperatureEntry_Object=MibTableRow
qtechSystemTemperatureEntry=_QtechSystemTemperatureEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23,1))
qtechSystemTemperatureEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:qtechSystemTemperatureEntry.setStatus(_A)
_QtechSystemTemperatureIndex_Type=Integer32
_QtechSystemTemperatureIndex_Object=MibTableColumn
qtechSystemTemperatureIndex=_QtechSystemTemperatureIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23,1,1),_QtechSystemTemperatureIndex_Type())
qtechSystemTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemTemperatureIndex.setStatus(_A)
_QtechSystemTemperatureName_Type=DisplayString
_QtechSystemTemperatureName_Object=MibTableColumn
qtechSystemTemperatureName=_QtechSystemTemperatureName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23,1,2),_QtechSystemTemperatureName_Type())
qtechSystemTemperatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemTemperatureName.setStatus(_A)
_QtechSystemTemperatureCurrent_Type=Integer32
_QtechSystemTemperatureCurrent_Object=MibTableColumn
qtechSystemTemperatureCurrent=_QtechSystemTemperatureCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23,1,3),_QtechSystemTemperatureCurrent_Type())
qtechSystemTemperatureCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemTemperatureCurrent.setStatus(_A)
_QtechSystemTemperatureWarningVaule_Type=Integer32
_QtechSystemTemperatureWarningVaule_Object=MibTableColumn
qtechSystemTemperatureWarningVaule=_QtechSystemTemperatureWarningVaule_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23,1,4),_QtechSystemTemperatureWarningVaule_Type())
qtechSystemTemperatureWarningVaule.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemTemperatureWarningVaule.setStatus(_A)
_QtechSystemTemperatureCritialVaule_Type=Integer32
_QtechSystemTemperatureCritialVaule_Object=MibTableColumn
qtechSystemTemperatureCritialVaule=_QtechSystemTemperatureCritialVaule_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,23,1,5),_QtechSystemTemperatureCritialVaule_Type())
qtechSystemTemperatureCritialVaule.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemTemperatureCritialVaule.setStatus(_A)
_QtechSystemSerialno_Type=DisplayString
_QtechSystemSerialno_Object=MibScalar
qtechSystemSerialno=_QtechSystemSerialno_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,24),_QtechSystemSerialno_Type())
qtechSystemSerialno.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSerialno.setStatus(_A)
_QtechSystemVersionTable_Object=MibTable
qtechSystemVersionTable=_QtechSystemVersionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25))
if mibBuilder.loadTexts:qtechSystemVersionTable.setStatus(_A)
_QtechSystemVersionEntry_Object=MibTableRow
qtechSystemVersionEntry=_QtechSystemVersionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1))
qtechSystemVersionEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:qtechSystemVersionEntry.setStatus(_A)
_QtechSystemVersionIndex_Type=Unsigned32
_QtechSystemVersionIndex_Object=MibTableColumn
qtechSystemVersionIndex=_QtechSystemVersionIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,1),_QtechSystemVersionIndex_Type())
qtechSystemVersionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionIndex.setStatus(_A)
_QtechSystemVersionName_Type=DisplayString
_QtechSystemVersionName_Object=MibTableColumn
qtechSystemVersionName=_QtechSystemVersionName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,2),_QtechSystemVersionName_Type())
qtechSystemVersionName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionName.setStatus(_A)
_QtechSystemVersionSwBoot_Type=DisplayString
_QtechSystemVersionSwBoot_Object=MibTableColumn
qtechSystemVersionSwBoot=_QtechSystemVersionSwBoot_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,3),_QtechSystemVersionSwBoot_Type())
qtechSystemVersionSwBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionSwBoot.setStatus(_A)
_QtechSystemVersionSwCtrl_Type=DisplayString
_QtechSystemVersionSwCtrl_Object=MibTableColumn
qtechSystemVersionSwCtrl=_QtechSystemVersionSwCtrl_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,4),_QtechSystemVersionSwCtrl_Type())
qtechSystemVersionSwCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionSwCtrl.setStatus(_A)
_QtechSystemVersionSwMain_Type=DisplayString
_QtechSystemVersionSwMain_Object=MibTableColumn
qtechSystemVersionSwMain=_QtechSystemVersionSwMain_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,5),_QtechSystemVersionSwMain_Type())
qtechSystemVersionSwMain.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionSwMain.setStatus(_A)
_QtechSystemVersionHw_Type=DisplayString
_QtechSystemVersionHw_Object=MibTableColumn
qtechSystemVersionHw=_QtechSystemVersionHw_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,6),_QtechSystemVersionHw_Type())
qtechSystemVersionHw.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionHw.setStatus(_A)
_QtechSystemVersionSerialno_Type=DisplayString
_QtechSystemVersionSerialno_Object=MibTableColumn
qtechSystemVersionSerialno=_QtechSystemVersionSerialno_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,25,1,7),_QtechSystemVersionSerialno_Type())
qtechSystemVersionSerialno.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemVersionSerialno.setStatus(_A)
_QtechSystemSysModel_Type=DisplayString
_QtechSystemSysModel_Object=MibScalar
qtechSystemSysModel=_QtechSystemSysModel_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,26),_QtechSystemSysModel_Type())
qtechSystemSysModel.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSysModel.setStatus(_A)
_QtechSystemUptime_Type=Integer32
_QtechSystemUptime_Object=MibScalar
qtechSystemUptime=_QtechSystemUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,27),_QtechSystemUptime_Type())
qtechSystemUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemUptime.setStatus(_A)
_QtechSystemSampleTime_Type=Integer32
_QtechSystemSampleTime_Object=MibScalar
qtechSystemSampleTime=_QtechSystemSampleTime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,28),_QtechSystemSampleTime_Type())
qtechSystemSampleTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemSampleTime.setStatus(_A)
_QtechSystemStatWindowTime_Type=Integer32
_QtechSystemStatWindowTime_Object=MibScalar
qtechSystemStatWindowTime=_QtechSystemStatWindowTime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,29),_QtechSystemStatWindowTime_Type())
qtechSystemStatWindowTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemStatWindowTime.setStatus(_A)
_QtechSystemManufacturer_Type=DisplayString
_QtechSystemManufacturer_Object=MibScalar
qtechSystemManufacturer=_QtechSystemManufacturer_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,30),_QtechSystemManufacturer_Type())
qtechSystemManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemManufacturer.setStatus(_A)
_QtechSystemCurrentTime_Type=DisplayString
_QtechSystemCurrentTime_Object=MibScalar
qtechSystemCurrentTime=_QtechSystemCurrentTime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,31),_QtechSystemCurrentTime_Type())
qtechSystemCurrentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemCurrentTime.setStatus(_A)
_QtechSystemWarnResendTime_Type=Integer32
_QtechSystemWarnResendTime_Object=MibScalar
qtechSystemWarnResendTime=_QtechSystemWarnResendTime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,32),_QtechSystemWarnResendTime_Type())
qtechSystemWarnResendTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemWarnResendTime.setStatus(_A)
_QtechSystemSoftwareName_Type=DisplayString
_QtechSystemSoftwareName_Object=MibScalar
qtechSystemSoftwareName=_QtechSystemSoftwareName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,33),_QtechSystemSoftwareName_Type())
qtechSystemSoftwareName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSoftwareName.setStatus(_A)
_QtechSystemSoftwareManufacturer_Type=DisplayString
_QtechSystemSoftwareManufacturer_Object=MibScalar
qtechSystemSoftwareManufacturer=_QtechSystemSoftwareManufacturer_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,34),_QtechSystemSoftwareManufacturer_Type())
qtechSystemSoftwareManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSoftwareManufacturer.setStatus(_A)
_QtechSystemCpuType_Type=DisplayString
_QtechSystemCpuType_Object=MibScalar
qtechSystemCpuType=_QtechSystemCpuType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,35),_QtechSystemCpuType_Type())
qtechSystemCpuType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemCpuType.setStatus(_A)
_QtechSystemMemoryType_Type=DisplayString
_QtechSystemMemoryType_Object=MibScalar
qtechSystemMemoryType=_QtechSystemMemoryType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,36),_QtechSystemMemoryType_Type())
qtechSystemMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMemoryType.setStatus(_A)
_QtechSystemMemorySize_Type=Gauge32
_QtechSystemMemorySize_Object=MibScalar
qtechSystemMemorySize=_QtechSystemMemorySize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,37),_QtechSystemMemorySize_Type())
qtechSystemMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMemorySize.setStatus(_A)
_QtechSystemFlashSize_Type=Gauge32
_QtechSystemFlashSize_Object=MibScalar
qtechSystemFlashSize=_QtechSystemFlashSize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,38),_QtechSystemFlashSize_Type())
qtechSystemFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFlashSize.setStatus(_A)
_QtechSystemLankApTable_Object=MibTable
qtechSystemLankApTable=_QtechSystemLankApTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39))
if mibBuilder.loadTexts:qtechSystemLankApTable.setStatus(_A)
_QtechSystemLankApEntry_Object=MibTableRow
qtechSystemLankApEntry=_QtechSystemLankApEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1))
qtechSystemLankApEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:qtechSystemLankApEntry.setStatus(_A)
_QtechSystemLankApMacAddr_Type=MacAddress
_QtechSystemLankApMacAddr_Object=MibTableColumn
qtechSystemLankApMacAddr=_QtechSystemLankApMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,1),_QtechSystemLankApMacAddr_Type())
qtechSystemLankApMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApMacAddr.setStatus(_A)
_QtechSystemLankApStatWindowTime_Type=Integer32
_QtechSystemLankApStatWindowTime_Object=MibTableColumn
qtechSystemLankApStatWindowTime=_QtechSystemLankApStatWindowTime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,2),_QtechSystemLankApStatWindowTime_Type())
qtechSystemLankApStatWindowTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemLankApStatWindowTime.setStatus(_A)
_QtechSystemLankApSampleTime_Type=Integer32
_QtechSystemLankApSampleTime_Object=MibTableColumn
qtechSystemLankApSampleTime=_QtechSystemLankApSampleTime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,3),_QtechSystemLankApSampleTime_Type())
qtechSystemLankApSampleTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemLankApSampleTime.setStatus(_A)
class _QtechSystemLankApReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_b,1)))
_QtechSystemLankApReset_Type.__name__=_D
_QtechSystemLankApReset_Object=MibTableColumn
qtechSystemLankApReset=_QtechSystemLankApReset_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,4),_QtechSystemLankApReset_Type())
qtechSystemLankApReset.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemLankApReset.setStatus(_A)
_QtechSystemLankApSoftwareName_Type=DisplayString
_QtechSystemLankApSoftwareName_Object=MibTableColumn
qtechSystemLankApSoftwareName=_QtechSystemLankApSoftwareName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,5),_QtechSystemLankApSoftwareName_Type())
qtechSystemLankApSoftwareName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApSoftwareName.setStatus(_A)
class _QtechSystemLankApSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSystemLankApSwVersion_Type.__name__=_F
_QtechSystemLankApSwVersion_Object=MibTableColumn
qtechSystemLankApSwVersion=_QtechSystemLankApSwVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,6),_QtechSystemLankApSwVersion_Type())
qtechSystemLankApSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApSwVersion.setStatus(_A)
_QtechSystemLankApSoftwareManufacturer_Type=DisplayString
_QtechSystemLankApSoftwareManufacturer_Object=MibTableColumn
qtechSystemLankApSoftwareManufacturer=_QtechSystemLankApSoftwareManufacturer_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,7),_QtechSystemLankApSoftwareManufacturer_Type())
qtechSystemLankApSoftwareManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApSoftwareManufacturer.setStatus(_A)
_QtechSystemLankApCpuType_Type=DisplayString
_QtechSystemLankApCpuType_Object=MibTableColumn
qtechSystemLankApCpuType=_QtechSystemLankApCpuType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,8),_QtechSystemLankApCpuType_Type())
qtechSystemLankApCpuType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApCpuType.setStatus(_A)
_QtechSystemLankApMemoryType_Type=DisplayString
_QtechSystemLankApMemoryType_Object=MibTableColumn
qtechSystemLankApMemoryType=_QtechSystemLankApMemoryType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,9),_QtechSystemLankApMemoryType_Type())
qtechSystemLankApMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApMemoryType.setStatus(_A)
_QtechSystemLankApMemorySize_Type=Gauge32
_QtechSystemLankApMemorySize_Object=MibTableColumn
qtechSystemLankApMemorySize=_QtechSystemLankApMemorySize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,10),_QtechSystemLankApMemorySize_Type())
qtechSystemLankApMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApMemorySize.setStatus(_A)
_QtechSystemLankAPFlashSize_Type=Gauge32
_QtechSystemLankAPFlashSize_Object=MibTableColumn
qtechSystemLankAPFlashSize=_QtechSystemLankAPFlashSize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,11),_QtechSystemLankAPFlashSize_Type())
qtechSystemLankAPFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankAPFlashSize.setStatus(_A)
_QtechSystemLankApManufacturer_Type=DisplayString
_QtechSystemLankApManufacturer_Object=MibTableColumn
qtechSystemLankApManufacturer=_QtechSystemLankApManufacturer_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,12),_QtechSystemLankApManufacturer_Type())
qtechSystemLankApManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApManufacturer.setStatus(_A)
_QtechSystemLankApSerialno_Type=DisplayString
_QtechSystemLankApSerialno_Object=MibTableColumn
qtechSystemLankApSerialno=_QtechSystemLankApSerialno_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,13),_QtechSystemLankApSerialno_Type())
qtechSystemLankApSerialno.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApSerialno.setStatus(_A)
_QtechSystemLankApSysModel_Type=DisplayString
_QtechSystemLankApSysModel_Object=MibTableColumn
qtechSystemLankApSysModel=_QtechSystemLankApSysModel_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,14),_QtechSystemLankApSysModel_Type())
qtechSystemLankApSysModel.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApSysModel.setStatus(_A)
_QtechSystemLankApUptime_Type=Integer32
_QtechSystemLankApUptime_Object=MibTableColumn
qtechSystemLankApUptime=_QtechSystemLankApUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,15),_QtechSystemLankApUptime_Type())
qtechSystemLankApUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApUptime.setStatus(_A)
_QtechSystemLankApAccurateUptime_Type=TimeTicks
_QtechSystemLankApAccurateUptime_Object=MibTableColumn
qtechSystemLankApAccurateUptime=_QtechSystemLankApAccurateUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,16),_QtechSystemLankApAccurateUptime_Type())
qtechSystemLankApAccurateUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApAccurateUptime.setStatus(_A)
class _QtechSystemLankApHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSystemLankApHwVersion_Type.__name__=_F
_QtechSystemLankApHwVersion_Object=MibTableColumn
qtechSystemLankApHwVersion=_QtechSystemLankApHwVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,39,1,17),_QtechSystemLankApHwVersion_Type())
qtechSystemLankApHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemLankApHwVersion.setStatus(_A)
_QtechSystemBoardTemperatureTable_Object=MibTable
qtechSystemBoardTemperatureTable=_QtechSystemBoardTemperatureTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,40))
if mibBuilder.loadTexts:qtechSystemBoardTemperatureTable.setStatus(_A)
_QtechSystemBoardTemperatureEntry_Object=MibTableRow
qtechSystemBoardTemperatureEntry=_QtechSystemBoardTemperatureEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,40,1))
qtechSystemBoardTemperatureEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:qtechSystemBoardTemperatureEntry.setStatus(_A)
_QtechSystemBoardTemperatureIndex_Type=Integer32
_QtechSystemBoardTemperatureIndex_Object=MibTableColumn
qtechSystemBoardTemperatureIndex=_QtechSystemBoardTemperatureIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,40,1,1),_QtechSystemBoardTemperatureIndex_Type())
qtechSystemBoardTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemBoardTemperatureIndex.setStatus(_A)
_QtechSystemBoardTemperatureName_Type=DisplayString
_QtechSystemBoardTemperatureName_Object=MibTableColumn
qtechSystemBoardTemperatureName=_QtechSystemBoardTemperatureName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,40,1,2),_QtechSystemBoardTemperatureName_Type())
qtechSystemBoardTemperatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemBoardTemperatureName.setStatus(_A)
_QtechSystemBoardTemperatureCurrent_Type=Integer32
_QtechSystemBoardTemperatureCurrent_Object=MibTableColumn
qtechSystemBoardTemperatureCurrent=_QtechSystemBoardTemperatureCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,40,1,3),_QtechSystemBoardTemperatureCurrent_Type())
qtechSystemBoardTemperatureCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemBoardTemperatureCurrent.setStatus(_A)
_QtechSystemElectricalInformationTable_Object=MibTable
qtechSystemElectricalInformationTable=_QtechSystemElectricalInformationTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41))
if mibBuilder.loadTexts:qtechSystemElectricalInformationTable.setStatus(_A)
_QtechSystemElectricalInformationEntry_Object=MibTableRow
qtechSystemElectricalInformationEntry=_QtechSystemElectricalInformationEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1))
qtechSystemElectricalInformationEntry.setIndexNames((0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:qtechSystemElectricalInformationEntry.setStatus(_A)
_QtechSystemElectricalInformationDeviceIndex_Type=Integer32
_QtechSystemElectricalInformationDeviceIndex_Object=MibTableColumn
qtechSystemElectricalInformationDeviceIndex=_QtechSystemElectricalInformationDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,1),_QtechSystemElectricalInformationDeviceIndex_Type())
qtechSystemElectricalInformationDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationDeviceIndex.setStatus(_A)
_QtechSystemElectricalInformationIndex_Type=Integer32
_QtechSystemElectricalInformationIndex_Object=MibTableColumn
qtechSystemElectricalInformationIndex=_QtechSystemElectricalInformationIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,2),_QtechSystemElectricalInformationIndex_Type())
qtechSystemElectricalInformationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationIndex.setStatus(_A)
class _QtechSystemElectricalInformationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_G,4),(_R,5),(_S,6)))
_QtechSystemElectricalInformationStatus_Type.__name__=_D
_QtechSystemElectricalInformationStatus_Object=MibTableColumn
qtechSystemElectricalInformationStatus=_QtechSystemElectricalInformationStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,3),_QtechSystemElectricalInformationStatus_Type())
qtechSystemElectricalInformationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationStatus.setStatus(_A)
_QtechSystemElectricalInformationType_Type=DisplayString
_QtechSystemElectricalInformationType_Object=MibTableColumn
qtechSystemElectricalInformationType=_QtechSystemElectricalInformationType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,4),_QtechSystemElectricalInformationType_Type())
qtechSystemElectricalInformationType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationType.setStatus(_A)
_QtechSystemElectricalInformationAttribute_Type=DisplayString
_QtechSystemElectricalInformationAttribute_Object=MibTableColumn
qtechSystemElectricalInformationAttribute=_QtechSystemElectricalInformationAttribute_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,5),_QtechSystemElectricalInformationAttribute_Type())
qtechSystemElectricalInformationAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationAttribute.setStatus(_A)
_QtechSystemElectricalInformationSofeVersion_Type=DisplayString
_QtechSystemElectricalInformationSofeVersion_Object=MibTableColumn
qtechSystemElectricalInformationSofeVersion=_QtechSystemElectricalInformationSofeVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,6),_QtechSystemElectricalInformationSofeVersion_Type())
qtechSystemElectricalInformationSofeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationSofeVersion.setStatus(_A)
_QtechSystemElectricalInformationHardwareVersion_Type=DisplayString
_QtechSystemElectricalInformationHardwareVersion_Object=MibTableColumn
qtechSystemElectricalInformationHardwareVersion=_QtechSystemElectricalInformationHardwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,7),_QtechSystemElectricalInformationHardwareVersion_Type())
qtechSystemElectricalInformationHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationHardwareVersion.setStatus(_A)
_QtechSystemElectricalInformationSerial_Type=DisplayString
_QtechSystemElectricalInformationSerial_Object=MibTableColumn
qtechSystemElectricalInformationSerial=_QtechSystemElectricalInformationSerial_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,8),_QtechSystemElectricalInformationSerial_Type())
qtechSystemElectricalInformationSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationSerial.setStatus(_A)
_QtechSystemElectricalInformationProductionDate_Type=DisplayString
_QtechSystemElectricalInformationProductionDate_Object=MibTableColumn
qtechSystemElectricalInformationProductionDate=_QtechSystemElectricalInformationProductionDate_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,9),_QtechSystemElectricalInformationProductionDate_Type())
qtechSystemElectricalInformationProductionDate.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationProductionDate.setStatus(_A)
_QtechSystemElectricalInformationRatedPower_Type=Integer32
_QtechSystemElectricalInformationRatedPower_Object=MibTableColumn
qtechSystemElectricalInformationRatedPower=_QtechSystemElectricalInformationRatedPower_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,10),_QtechSystemElectricalInformationRatedPower_Type())
qtechSystemElectricalInformationRatedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationRatedPower.setStatus(_A)
_QtechSystemElectricalInformationInVoltage_Type=Integer32
_QtechSystemElectricalInformationInVoltage_Object=MibTableColumn
qtechSystemElectricalInformationInVoltage=_QtechSystemElectricalInformationInVoltage_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,11),_QtechSystemElectricalInformationInVoltage_Type())
qtechSystemElectricalInformationInVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationInVoltage.setStatus(_A)
_QtechSystemElectricalInformationInCurrent_Type=Integer32
_QtechSystemElectricalInformationInCurrent_Object=MibTableColumn
qtechSystemElectricalInformationInCurrent=_QtechSystemElectricalInformationInCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,12),_QtechSystemElectricalInformationInCurrent_Type())
qtechSystemElectricalInformationInCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationInCurrent.setStatus(_A)
_QtechSystemElectricalInformationOutVoltage_Type=Integer32
_QtechSystemElectricalInformationOutVoltage_Object=MibTableColumn
qtechSystemElectricalInformationOutVoltage=_QtechSystemElectricalInformationOutVoltage_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,13),_QtechSystemElectricalInformationOutVoltage_Type())
qtechSystemElectricalInformationOutVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationOutVoltage.setStatus(_A)
_QtechSystemElectricalInformationOutCurrent_Type=Integer32
_QtechSystemElectricalInformationOutCurrent_Object=MibTableColumn
qtechSystemElectricalInformationOutCurrent=_QtechSystemElectricalInformationOutCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,14),_QtechSystemElectricalInformationOutCurrent_Type())
qtechSystemElectricalInformationOutCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationOutCurrent.setStatus(_A)
_QtechSystemElectricalInformationOutPower_Type=Integer32
_QtechSystemElectricalInformationOutPower_Object=MibTableColumn
qtechSystemElectricalInformationOutPower=_QtechSystemElectricalInformationOutPower_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,15),_QtechSystemElectricalInformationOutPower_Type())
qtechSystemElectricalInformationOutPower.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationOutPower.setStatus(_A)
_QtechSystemElectricalInformationTemperature_Type=Integer32
_QtechSystemElectricalInformationTemperature_Object=MibTableColumn
qtechSystemElectricalInformationTemperature=_QtechSystemElectricalInformationTemperature_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,16),_QtechSystemElectricalInformationTemperature_Type())
qtechSystemElectricalInformationTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationTemperature.setStatus(_A)
_QtechSystemElectricalInformationAirflowCoexist_Type=DisplayString
_QtechSystemElectricalInformationAirflowCoexist_Object=MibTableColumn
qtechSystemElectricalInformationAirflowCoexist=_QtechSystemElectricalInformationAirflowCoexist_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,17),_QtechSystemElectricalInformationAirflowCoexist_Type())
qtechSystemElectricalInformationAirflowCoexist.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationAirflowCoexist.setStatus(_A)
_QtechSystemElectricalInformationWarningStatus_Type=DisplayString
_QtechSystemElectricalInformationWarningStatus_Object=MibTableColumn
qtechSystemElectricalInformationWarningStatus=_QtechSystemElectricalInformationWarningStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,41,1,18),_QtechSystemElectricalInformationWarningStatus_Type())
qtechSystemElectricalInformationWarningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemElectricalInformationWarningStatus.setStatus(_A)
_QtechSystemFanInformationTable_Object=MibTable
qtechSystemFanInformationTable=_QtechSystemFanInformationTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42))
if mibBuilder.loadTexts:qtechSystemFanInformationTable.setStatus(_A)
_QtechSystemFanInformationEntry_Object=MibTableRow
qtechSystemFanInformationEntry=_QtechSystemFanInformationEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1))
qtechSystemFanInformationEntry.setIndexNames((0,_C,_m),(0,_C,_n))
if mibBuilder.loadTexts:qtechSystemFanInformationEntry.setStatus(_A)
_QtechSystemFanInformationDeviceIndex_Type=Integer32
_QtechSystemFanInformationDeviceIndex_Object=MibTableColumn
qtechSystemFanInformationDeviceIndex=_QtechSystemFanInformationDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,1),_QtechSystemFanInformationDeviceIndex_Type())
qtechSystemFanInformationDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationDeviceIndex.setStatus(_A)
_QtechSystemFanInformationFanIndex_Type=Integer32
_QtechSystemFanInformationFanIndex_Object=MibTableColumn
qtechSystemFanInformationFanIndex=_QtechSystemFanInformationFanIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,2),_QtechSystemFanInformationFanIndex_Type())
qtechSystemFanInformationFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationFanIndex.setStatus(_A)
class _QtechSystemFanInformationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_G,4),(_R,5),(_S,6)))
_QtechSystemFanInformationStatus_Type.__name__=_D
_QtechSystemFanInformationStatus_Object=MibTableColumn
qtechSystemFanInformationStatus=_QtechSystemFanInformationStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,3),_QtechSystemFanInformationStatus_Type())
qtechSystemFanInformationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationStatus.setStatus(_A)
_QtechSystemFanInformationType_Type=DisplayString
_QtechSystemFanInformationType_Object=MibTableColumn
qtechSystemFanInformationType=_QtechSystemFanInformationType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,4),_QtechSystemFanInformationType_Type())
qtechSystemFanInformationType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationType.setStatus(_A)
_QtechSystemFanInformationAttribute_Type=DisplayString
_QtechSystemFanInformationAttribute_Object=MibTableColumn
qtechSystemFanInformationAttribute=_QtechSystemFanInformationAttribute_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,5),_QtechSystemFanInformationAttribute_Type())
qtechSystemFanInformationAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationAttribute.setStatus(_A)
_QtechSystemFanInformationSofeVersion_Type=DisplayString
_QtechSystemFanInformationSofeVersion_Object=MibTableColumn
qtechSystemFanInformationSofeVersion=_QtechSystemFanInformationSofeVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,6),_QtechSystemFanInformationSofeVersion_Type())
qtechSystemFanInformationSofeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationSofeVersion.setStatus(_A)
_QtechSystemFanInformationFirmwareVersion_Type=DisplayString
_QtechSystemFanInformationFirmwareVersion_Object=MibTableColumn
qtechSystemFanInformationFirmwareVersion=_QtechSystemFanInformationFirmwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,7),_QtechSystemFanInformationFirmwareVersion_Type())
qtechSystemFanInformationFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationFirmwareVersion.setStatus(_A)
_QtechSystemFanInformationHardwareVersion_Type=DisplayString
_QtechSystemFanInformationHardwareVersion_Object=MibTableColumn
qtechSystemFanInformationHardwareVersion=_QtechSystemFanInformationHardwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,8),_QtechSystemFanInformationHardwareVersion_Type())
qtechSystemFanInformationHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationHardwareVersion.setStatus(_A)
_QtechSystemFanInformationSerial_Type=DisplayString
_QtechSystemFanInformationSerial_Object=MibTableColumn
qtechSystemFanInformationSerial=_QtechSystemFanInformationSerial_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,9),_QtechSystemFanInformationSerial_Type())
qtechSystemFanInformationSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationSerial.setStatus(_A)
_QtechSystemFanInformationProductionDate_Type=DisplayString
_QtechSystemFanInformationProductionDate_Object=MibTableColumn
qtechSystemFanInformationProductionDate=_QtechSystemFanInformationProductionDate_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,10),_QtechSystemFanInformationProductionDate_Type())
qtechSystemFanInformationProductionDate.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationProductionDate.setStatus(_A)
_QtechSystemFanInformationTemperature_Type=Integer32
_QtechSystemFanInformationTemperature_Object=MibTableColumn
qtechSystemFanInformationTemperature=_QtechSystemFanInformationTemperature_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,11),_QtechSystemFanInformationTemperature_Type())
qtechSystemFanInformationTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationTemperature.setStatus(_A)
_QtechSystemFanInformationNumber_Type=Integer32
_QtechSystemFanInformationNumber_Object=MibTableColumn
qtechSystemFanInformationNumber=_QtechSystemFanInformationNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,12),_QtechSystemFanInformationNumber_Type())
qtechSystemFanInformationNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationNumber.setStatus(_A)
_QtechSystemFanInformationAirflowCoexist_Type=DisplayString
_QtechSystemFanInformationAirflowCoexist_Object=MibTableColumn
qtechSystemFanInformationAirflowCoexist=_QtechSystemFanInformationAirflowCoexist_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,13),_QtechSystemFanInformationAirflowCoexist_Type())
qtechSystemFanInformationAirflowCoexist.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationAirflowCoexist.setStatus(_A)
_QtechSystemFanInformationWarningStatus_Type=DisplayString
_QtechSystemFanInformationWarningStatus_Object=MibTableColumn
qtechSystemFanInformationWarningStatus=_QtechSystemFanInformationWarningStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,42,1,14),_QtechSystemFanInformationWarningStatus_Type())
qtechSystemFanInformationWarningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanInformationWarningStatus.setStatus(_A)
_QtechSystemFanStatusTable_Object=MibTable
qtechSystemFanStatusTable=_QtechSystemFanStatusTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43))
if mibBuilder.loadTexts:qtechSystemFanStatusTable.setStatus(_A)
_QtechSystemFanStatusEntry_Object=MibTableRow
qtechSystemFanStatusEntry=_QtechSystemFanStatusEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1))
qtechSystemFanStatusEntry.setIndexNames((0,_C,_X),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:qtechSystemFanStatusEntry.setStatus(_A)
_QtechSystemFanStatusDeviceIndex_Type=Integer32
_QtechSystemFanStatusDeviceIndex_Object=MibTableColumn
qtechSystemFanStatusDeviceIndex=_QtechSystemFanStatusDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1,1),_QtechSystemFanStatusDeviceIndex_Type())
qtechSystemFanStatusDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanStatusDeviceIndex.setStatus(_A)
_QtechSystemFanStatusFanIndex_Type=Integer32
_QtechSystemFanStatusFanIndex_Object=MibTableColumn
qtechSystemFanStatusFanIndex=_QtechSystemFanStatusFanIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1,2),_QtechSystemFanStatusFanIndex_Type())
qtechSystemFanStatusFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanStatusFanIndex.setStatus(_A)
_QtechSystemFanStatusIndex_Type=Integer32
_QtechSystemFanStatusIndex_Object=MibTableColumn
qtechSystemFanStatusIndex=_QtechSystemFanStatusIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1,3),_QtechSystemFanStatusIndex_Type())
qtechSystemFanStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanStatusIndex.setStatus(_A)
class _QtechSystemFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_G,4),(_R,5),(_S,6)))
_QtechSystemFanStatus_Type.__name__=_D
_QtechSystemFanStatus_Object=MibTableColumn
qtechSystemFanStatus=_QtechSystemFanStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1,4),_QtechSystemFanStatus_Type())
qtechSystemFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanStatus.setStatus(_A)
_QtechSystemFanStatusLevel_Type=Integer32
_QtechSystemFanStatusLevel_Object=MibTableColumn
qtechSystemFanStatusLevel=_QtechSystemFanStatusLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1,5),_QtechSystemFanStatusLevel_Type())
qtechSystemFanStatusLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanStatusLevel.setStatus(_A)
_QtechSystemFanStatusSpeed_Type=Integer32
_QtechSystemFanStatusSpeed_Object=MibTableColumn
qtechSystemFanStatusSpeed=_QtechSystemFanStatusSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,43,1,6),_QtechSystemFanStatusSpeed_Type())
qtechSystemFanStatusSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanStatusSpeed.setStatus(_A)
_QtechSystemMultipleTemperatureTable_Object=MibTable
qtechSystemMultipleTemperatureTable=_QtechSystemMultipleTemperatureTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44))
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureTable.setStatus(_A)
_QtechSystemMultipleTemperatureEntry_Object=MibTableRow
qtechSystemMultipleTemperatureEntry=_QtechSystemMultipleTemperatureEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1))
qtechSystemMultipleTemperatureEntry.setIndexNames((0,_C,_W),(0,_C,_J),(0,_C,_o))
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureEntry.setStatus(_A)
_QtechSystemMultipleTemperatureDeviceIndex_Type=Integer32
_QtechSystemMultipleTemperatureDeviceIndex_Object=MibTableColumn
qtechSystemMultipleTemperatureDeviceIndex=_QtechSystemMultipleTemperatureDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,1),_QtechSystemMultipleTemperatureDeviceIndex_Type())
qtechSystemMultipleTemperatureDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureDeviceIndex.setStatus(_A)
_QtechSystemMultipleTemperatureSlotIndex_Type=Integer32
_QtechSystemMultipleTemperatureSlotIndex_Object=MibTableColumn
qtechSystemMultipleTemperatureSlotIndex=_QtechSystemMultipleTemperatureSlotIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,2),_QtechSystemMultipleTemperatureSlotIndex_Type())
qtechSystemMultipleTemperatureSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureSlotIndex.setStatus(_A)
_QtechSystemMultipleTemperatureIndex_Type=Integer32
_QtechSystemMultipleTemperatureIndex_Object=MibTableColumn
qtechSystemMultipleTemperatureIndex=_QtechSystemMultipleTemperatureIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,3),_QtechSystemMultipleTemperatureIndex_Type())
qtechSystemMultipleTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureIndex.setStatus(_A)
_QtechSystemMultipleTemperatureName_Type=DisplayString
_QtechSystemMultipleTemperatureName_Object=MibTableColumn
qtechSystemMultipleTemperatureName=_QtechSystemMultipleTemperatureName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,4),_QtechSystemMultipleTemperatureName_Type())
qtechSystemMultipleTemperatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureName.setStatus(_A)
_QtechSystemMultipleTemperatureCurrent_Type=Integer32
_QtechSystemMultipleTemperatureCurrent_Object=MibTableColumn
qtechSystemMultipleTemperatureCurrent=_QtechSystemMultipleTemperatureCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,5),_QtechSystemMultipleTemperatureCurrent_Type())
qtechSystemMultipleTemperatureCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureCurrent.setStatus(_A)
_QtechSystemMultipleTemperatureWarning_Type=Integer32
_QtechSystemMultipleTemperatureWarning_Object=MibTableColumn
qtechSystemMultipleTemperatureWarning=_QtechSystemMultipleTemperatureWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,6),_QtechSystemMultipleTemperatureWarning_Type())
qtechSystemMultipleTemperatureWarning.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureWarning.setStatus(_A)
_QtechSystemMultipleTemperatureCritical_Type=Integer32
_QtechSystemMultipleTemperatureCritical_Object=MibTableColumn
qtechSystemMultipleTemperatureCritical=_QtechSystemMultipleTemperatureCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,44,1,7),_QtechSystemMultipleTemperatureCritical_Type())
qtechSystemMultipleTemperatureCritical.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSystemMultipleTemperatureCritical.setStatus(_A)
_QtechSystemAccurateUptime_Type=TimeTicks
_QtechSystemAccurateUptime_Object=MibScalar
qtechSystemAccurateUptime=_QtechSystemAccurateUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,45),_QtechSystemAccurateUptime_Type())
qtechSystemAccurateUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemAccurateUptime.setStatus(_A)
_QtechSystemPowerIndex_Type=Integer32
_QtechSystemPowerIndex_Object=MibScalar
qtechSystemPowerIndex=_QtechSystemPowerIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,46),_QtechSystemPowerIndex_Type())
qtechSystemPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemPowerIndex.setStatus(_A)
_QtechSystemSwitchID_Type=Integer32
_QtechSystemSwitchID_Object=MibScalar
qtechSystemSwitchID=_QtechSystemSwitchID_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,47),_QtechSystemSwitchID_Type())
qtechSystemSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemSwitchID.setStatus(_A)
_QtechSystemApDeviceDescriptionTable_Object=MibTable
qtechSystemApDeviceDescriptionTable=_QtechSystemApDeviceDescriptionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48))
if mibBuilder.loadTexts:qtechSystemApDeviceDescriptionTable.setStatus(_A)
_QtechSystemApDeviceDescriptionEntry_Object=MibTableRow
qtechSystemApDeviceDescriptionEntry=_QtechSystemApDeviceDescriptionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1))
qtechSystemApDeviceDescriptionEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:qtechSystemApDeviceDescriptionEntry.setStatus(_A)
_QtechSystemApDescMacAddr_Type=MacAddress
_QtechSystemApDescMacAddr_Object=MibTableColumn
qtechSystemApDescMacAddr=_QtechSystemApDescMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,1),_QtechSystemApDescMacAddr_Type())
qtechSystemApDescMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApDescMacAddr.setStatus(_A)
class _QtechSystemApMemoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_q,0),('sdram',1),('ddram',2)))
_QtechSystemApMemoryType_Type.__name__=_D
_QtechSystemApMemoryType_Object=MibTableColumn
qtechSystemApMemoryType=_QtechSystemApMemoryType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,2),_QtechSystemApMemoryType_Type())
qtechSystemApMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApMemoryType.setStatus(_A)
_QtechSystemApMemorySize_Type=Gauge32
_QtechSystemApMemorySize_Object=MibTableColumn
qtechSystemApMemorySize=_QtechSystemApMemorySize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,3),_QtechSystemApMemorySize_Type())
qtechSystemApMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApMemorySize.setStatus(_A)
class _QtechSystemAPFlashType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_q,0),('nor',1),('non-nor',2)))
_QtechSystemAPFlashType_Type.__name__=_D
_QtechSystemAPFlashType_Object=MibTableColumn
qtechSystemAPFlashType=_QtechSystemAPFlashType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,4),_QtechSystemAPFlashType_Type())
qtechSystemAPFlashType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemAPFlashType.setStatus(_A)
_QtechSystemAPFlashSize_Type=Gauge32
_QtechSystemAPFlashSize_Object=MibTableColumn
qtechSystemAPFlashSize=_QtechSystemAPFlashSize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,5),_QtechSystemAPFlashSize_Type())
qtechSystemAPFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemAPFlashSize.setStatus(_A)
_QtechSystemApNVRAMSize_Type=Gauge32
_QtechSystemApNVRAMSize_Object=MibTableColumn
qtechSystemApNVRAMSize=_QtechSystemApNVRAMSize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,6),_QtechSystemApNVRAMSize_Type())
qtechSystemApNVRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApNVRAMSize.setStatus(_A)
_QtechSystemApCFSize_Type=Gauge32
_QtechSystemApCFSize_Object=MibTableColumn
qtechSystemApCFSize=_QtechSystemApCFSize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,7),_QtechSystemApCFSize_Type())
qtechSystemApCFSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApCFSize.setStatus(_A)
_QtechSystemApCPUType_Type=DisplayString
_QtechSystemApCPUType_Object=MibTableColumn
qtechSystemApCPUType=_QtechSystemApCPUType_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,48,1,8),_QtechSystemApCPUType_Type())
qtechSystemApCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApCPUType.setStatus(_A)
_QtechSystemApDeviceStatisticsTable_Object=MibTable
qtechSystemApDeviceStatisticsTable=_QtechSystemApDeviceStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49))
if mibBuilder.loadTexts:qtechSystemApDeviceStatisticsTable.setStatus(_A)
_QtechSystemApDeviceStatisticsEntry_Object=MibTableRow
qtechSystemApDeviceStatisticsEntry=_QtechSystemApDeviceStatisticsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1))
qtechSystemApDeviceStatisticsEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:qtechSystemApDeviceStatisticsEntry.setStatus(_A)
_QtechSystemApStatMacAddr_Type=MacAddress
_QtechSystemApStatMacAddr_Object=MibTableColumn
qtechSystemApStatMacAddr=_QtechSystemApStatMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,1),_QtechSystemApStatMacAddr_Type())
qtechSystemApStatMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApStatMacAddr.setStatus(_A)
_QtechSystemApInterfaceNum_Type=Integer32
_QtechSystemApInterfaceNum_Object=MibTableColumn
qtechSystemApInterfaceNum=_QtechSystemApInterfaceNum_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,2),_QtechSystemApInterfaceNum_Type())
qtechSystemApInterfaceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApInterfaceNum.setStatus(_A)
_QtechSystemApUptime_Type=TimeTicks
_QtechSystemApUptime_Object=MibTableColumn
qtechSystemApUptime=_QtechSystemApUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,3),_QtechSystemApUptime_Type())
qtechSystemApUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApUptime.setStatus(_A)
_QtechSystemApCPUUtilizationCurrent_Type=Percent
_QtechSystemApCPUUtilizationCurrent_Object=MibTableColumn
qtechSystemApCPUUtilizationCurrent=_QtechSystemApCPUUtilizationCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,4),_QtechSystemApCPUUtilizationCurrent_Type())
qtechSystemApCPUUtilizationCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApCPUUtilizationCurrent.setStatus(_A)
_QtechSystemApCPUUtilizationAverage_Type=Percent
_QtechSystemApCPUUtilizationAverage_Object=MibTableColumn
qtechSystemApCPUUtilizationAverage=_QtechSystemApCPUUtilizationAverage_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,5),_QtechSystemApCPUUtilizationAverage_Type())
qtechSystemApCPUUtilizationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApCPUUtilizationAverage.setStatus(_A)
_QtechSystemApMemoryPoolCurrentUtilization_Type=Percent
_QtechSystemApMemoryPoolCurrentUtilization_Object=MibTableColumn
qtechSystemApMemoryPoolCurrentUtilization=_QtechSystemApMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,6),_QtechSystemApMemoryPoolCurrentUtilization_Type())
qtechSystemApMemoryPoolCurrentUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApMemoryPoolCurrentUtilization.setStatus(_A)
_QtechSystemApMemoryPoolAverageUtilization_Type=Percent
_QtechSystemApMemoryPoolAverageUtilization_Object=MibTableColumn
qtechSystemApMemoryPoolAverageUtilization=_QtechSystemApMemoryPoolAverageUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,7),_QtechSystemApMemoryPoolAverageUtilization_Type())
qtechSystemApMemoryPoolAverageUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApMemoryPoolAverageUtilization.setStatus(_A)
_QtechSystemApFlashFreeSize_Type=Unsigned32
_QtechSystemApFlashFreeSize_Object=MibTableColumn
qtechSystemApFlashFreeSize=_QtechSystemApFlashFreeSize_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,8),_QtechSystemApFlashFreeSize_Type())
qtechSystemApFlashFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemApFlashFreeSize.setStatus(_A)
_QtechSystemAPDeviceTemperature_Type=Integer32
_QtechSystemAPDeviceTemperature_Object=MibTableColumn
qtechSystemAPDeviceTemperature=_QtechSystemAPDeviceTemperature_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,49,1,9),_QtechSystemAPDeviceTemperature_Type())
qtechSystemAPDeviceTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemAPDeviceTemperature.setStatus(_A)
_QtechSystemUptimeMsLow_Type=Unsigned32
_QtechSystemUptimeMsLow_Object=MibScalar
qtechSystemUptimeMsLow=_QtechSystemUptimeMsLow_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,50),_QtechSystemUptimeMsLow_Type())
qtechSystemUptimeMsLow.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemUptimeMsLow.setStatus(_A)
_QtechSystemUptimeMsHigh_Type=Unsigned32
_QtechSystemUptimeMsHigh_Object=MibScalar
qtechSystemUptimeMsHigh=_QtechSystemUptimeMsHigh_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,51),_QtechSystemUptimeMsHigh_Type())
qtechSystemUptimeMsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemUptimeMsHigh.setStatus(_A)
_QtechSystemFanSNTable_Object=MibTable
qtechSystemFanSNTable=_QtechSystemFanSNTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,52))
if mibBuilder.loadTexts:qtechSystemFanSNTable.setStatus(_A)
_QtechSystemFanSNEntry_Object=MibTableRow
qtechSystemFanSNEntry=_QtechSystemFanSNEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,52,1))
qtechSystemFanSNEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:qtechSystemFanSNEntry.setStatus(_A)
_QtechSystemFanPadIndex_Type=Integer32
_QtechSystemFanPadIndex_Object=MibTableColumn
qtechSystemFanPadIndex=_QtechSystemFanPadIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,52,1,1),_QtechSystemFanPadIndex_Type())
qtechSystemFanPadIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPadIndex.setStatus(_A)
_QtechSystemFanPadName_Type=DisplayString
_QtechSystemFanPadName_Object=MibTableColumn
qtechSystemFanPadName=_QtechSystemFanPadName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,52,1,2),_QtechSystemFanPadName_Type())
qtechSystemFanPadName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPadName.setStatus(_A)
_QtechSystemFanPadSN_Type=DisplayString
_QtechSystemFanPadSN_Object=MibTableColumn
qtechSystemFanPadSN=_QtechSystemFanPadSN_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,52,1,3),_QtechSystemFanPadSN_Type())
qtechSystemFanPadSN.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPadSN.setStatus(_A)
_QtechSystemDsfSNTable_Object=MibTable
qtechSystemDsfSNTable=_QtechSystemDsfSNTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,53))
if mibBuilder.loadTexts:qtechSystemDsfSNTable.setStatus(_A)
_QtechSystemDsfSNEntry_Object=MibTableRow
qtechSystemDsfSNEntry=_QtechSystemDsfSNEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,53,1))
qtechSystemDsfSNEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:qtechSystemDsfSNEntry.setStatus(_A)
_QtechSystemDsfIndex_Type=Integer32
_QtechSystemDsfIndex_Object=MibTableColumn
qtechSystemDsfIndex=_QtechSystemDsfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,53,1,1),_QtechSystemDsfIndex_Type())
qtechSystemDsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemDsfIndex.setStatus(_A)
_QtechSystemDsfName_Type=DisplayString
_QtechSystemDsfName_Object=MibTableColumn
qtechSystemDsfName=_QtechSystemDsfName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,53,1,2),_QtechSystemDsfName_Type())
qtechSystemDsfName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemDsfName.setStatus(_A)
_QtechSystemDsfSN_Type=DisplayString
_QtechSystemDsfSN_Object=MibTableColumn
qtechSystemDsfSN=_QtechSystemDsfSN_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,53,1,3),_QtechSystemDsfSN_Type())
qtechSystemDsfSN.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemDsfSN.setStatus(_A)
_QtechSystemPowerSNTable_Object=MibTable
qtechSystemPowerSNTable=_QtechSystemPowerSNTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,54))
if mibBuilder.loadTexts:qtechSystemPowerSNTable.setStatus(_A)
_QtechSystemPowerSNEntry_Object=MibTableRow
qtechSystemPowerSNEntry=_QtechSystemPowerSNEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,54,1))
qtechSystemPowerSNEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:qtechSystemPowerSNEntry.setStatus(_A)
_QtechSystemPowerSNIndex_Type=Integer32
_QtechSystemPowerSNIndex_Object=MibTableColumn
qtechSystemPowerSNIndex=_QtechSystemPowerSNIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,54,1,1),_QtechSystemPowerSNIndex_Type())
qtechSystemPowerSNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemPowerSNIndex.setStatus(_A)
_QtechSystemPowerSNName_Type=DisplayString
_QtechSystemPowerSNName_Object=MibTableColumn
qtechSystemPowerSNName=_QtechSystemPowerSNName_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,54,1,2),_QtechSystemPowerSNName_Type())
qtechSystemPowerSNName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemPowerSNName.setStatus(_A)
_QtechSystemPowerSN_Type=DisplayString
_QtechSystemPowerSN_Object=MibTableColumn
qtechSystemPowerSN=_QtechSystemPowerSN_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,54,1,3),_QtechSystemPowerSN_Type())
qtechSystemPowerSN.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemPowerSN.setStatus(_A)
_QtechSystemFanPad1SpeedTable_Object=MibTable
qtechSystemFanPad1SpeedTable=_QtechSystemFanPad1SpeedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55))
if mibBuilder.loadTexts:qtechSystemFanPad1SpeedTable.setStatus(_A)
_QtechSystemFanPad1SpeedEntry_Object=MibTableRow
qtechSystemFanPad1SpeedEntry=_QtechSystemFanPad1SpeedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1))
qtechSystemFanPad1SpeedEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:qtechSystemFanPad1SpeedEntry.setStatus(_A)
_QtechSystemOamFanPad1Index_Type=Integer32
_QtechSystemOamFanPad1Index_Object=MibTableColumn
qtechSystemOamFanPad1Index=_QtechSystemOamFanPad1Index_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,1),_QtechSystemOamFanPad1Index_Type())
qtechSystemOamFanPad1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemOamFanPad1Index.setStatus(_A)
_QtechSystemOamFanPad1Name_Type=DisplayString
_QtechSystemOamFanPad1Name_Object=MibTableColumn
qtechSystemOamFanPad1Name=_QtechSystemOamFanPad1Name_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,2),_QtechSystemOamFanPad1Name_Type())
qtechSystemOamFanPad1Name.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemOamFanPad1Name.setStatus(_A)
_QtechSystemFanPad1Speed1_Type=Integer32
_QtechSystemFanPad1Speed1_Object=MibTableColumn
qtechSystemFanPad1Speed1=_QtechSystemFanPad1Speed1_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,3),_QtechSystemFanPad1Speed1_Type())
qtechSystemFanPad1Speed1.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed1.setStatus(_A)
_QtechSystemFanPad1Speed2_Type=Integer32
_QtechSystemFanPad1Speed2_Object=MibTableColumn
qtechSystemFanPad1Speed2=_QtechSystemFanPad1Speed2_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,4),_QtechSystemFanPad1Speed2_Type())
qtechSystemFanPad1Speed2.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed2.setStatus(_A)
_QtechSystemFanPad1Speed3_Type=Integer32
_QtechSystemFanPad1Speed3_Object=MibTableColumn
qtechSystemFanPad1Speed3=_QtechSystemFanPad1Speed3_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,5),_QtechSystemFanPad1Speed3_Type())
qtechSystemFanPad1Speed3.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed3.setStatus(_A)
_QtechSystemFanPad1Speed4_Type=Integer32
_QtechSystemFanPad1Speed4_Object=MibTableColumn
qtechSystemFanPad1Speed4=_QtechSystemFanPad1Speed4_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,6),_QtechSystemFanPad1Speed4_Type())
qtechSystemFanPad1Speed4.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed4.setStatus(_A)
_QtechSystemFanPad1Speed5_Type=Integer32
_QtechSystemFanPad1Speed5_Object=MibTableColumn
qtechSystemFanPad1Speed5=_QtechSystemFanPad1Speed5_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,7),_QtechSystemFanPad1Speed5_Type())
qtechSystemFanPad1Speed5.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed5.setStatus(_A)
_QtechSystemFanPad1Speed6_Type=Integer32
_QtechSystemFanPad1Speed6_Object=MibTableColumn
qtechSystemFanPad1Speed6=_QtechSystemFanPad1Speed6_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,8),_QtechSystemFanPad1Speed6_Type())
qtechSystemFanPad1Speed6.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed6.setStatus(_A)
_QtechSystemFanPad1Speed7_Type=Integer32
_QtechSystemFanPad1Speed7_Object=MibTableColumn
qtechSystemFanPad1Speed7=_QtechSystemFanPad1Speed7_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,9),_QtechSystemFanPad1Speed7_Type())
qtechSystemFanPad1Speed7.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed7.setStatus(_A)
_QtechSystemFanPad1Speed8_Type=Integer32
_QtechSystemFanPad1Speed8_Object=MibTableColumn
qtechSystemFanPad1Speed8=_QtechSystemFanPad1Speed8_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,10),_QtechSystemFanPad1Speed8_Type())
qtechSystemFanPad1Speed8.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed8.setStatus(_A)
_QtechSystemFanPad1Speed9_Type=Integer32
_QtechSystemFanPad1Speed9_Object=MibTableColumn
qtechSystemFanPad1Speed9=_QtechSystemFanPad1Speed9_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,55,1,11),_QtechSystemFanPad1Speed9_Type())
qtechSystemFanPad1Speed9.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad1Speed9.setStatus(_A)
_QtechSystemFanPad2SpeedTable_Object=MibTable
qtechSystemFanPad2SpeedTable=_QtechSystemFanPad2SpeedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56))
if mibBuilder.loadTexts:qtechSystemFanPad2SpeedTable.setStatus(_A)
_QtechSystemFanPad2SpeedEntry_Object=MibTableRow
qtechSystemFanPad2SpeedEntry=_QtechSystemFanPad2SpeedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56,1))
qtechSystemFanPad2SpeedEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:qtechSystemFanPad2SpeedEntry.setStatus(_A)
_QtechSystemOamFanPad2Index_Type=Integer32
_QtechSystemOamFanPad2Index_Object=MibTableColumn
qtechSystemOamFanPad2Index=_QtechSystemOamFanPad2Index_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56,1,1),_QtechSystemOamFanPad2Index_Type())
qtechSystemOamFanPad2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemOamFanPad2Index.setStatus(_A)
_QtechSystemOamFanPad2Name_Type=DisplayString
_QtechSystemOamFanPad2Name_Object=MibTableColumn
qtechSystemOamFanPad2Name=_QtechSystemOamFanPad2Name_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56,1,2),_QtechSystemOamFanPad2Name_Type())
qtechSystemOamFanPad2Name.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemOamFanPad2Name.setStatus(_A)
_QtechSystemFanPad2Speed1_Type=Integer32
_QtechSystemFanPad2Speed1_Object=MibTableColumn
qtechSystemFanPad2Speed1=_QtechSystemFanPad2Speed1_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56,1,3),_QtechSystemFanPad2Speed1_Type())
qtechSystemFanPad2Speed1.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad2Speed1.setStatus(_A)
_QtechSystemFanPad2Speed2_Type=Integer32
_QtechSystemFanPad2Speed2_Object=MibTableColumn
qtechSystemFanPad2Speed2=_QtechSystemFanPad2Speed2_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56,1,4),_QtechSystemFanPad2Speed2_Type())
qtechSystemFanPad2Speed2.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad2Speed2.setStatus(_A)
_QtechSystemFanPad2Speed3_Type=Integer32
_QtechSystemFanPad2Speed3_Object=MibTableColumn
qtechSystemFanPad2Speed3=_QtechSystemFanPad2Speed3_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,56,1,5),_QtechSystemFanPad2Speed3_Type())
qtechSystemFanPad2Speed3.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad2Speed3.setStatus(_A)
_QtechSystemFanPad3SpeedTable_Object=MibTable
qtechSystemFanPad3SpeedTable=_QtechSystemFanPad3SpeedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57))
if mibBuilder.loadTexts:qtechSystemFanPad3SpeedTable.setStatus(_A)
_QtechSystemFanPad3SpeedEntry_Object=MibTableRow
qtechSystemFanPad3SpeedEntry=_QtechSystemFanPad3SpeedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1))
qtechSystemFanPad3SpeedEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:qtechSystemFanPad3SpeedEntry.setStatus(_A)
_QtechSystemOamFanPad3Index_Type=Integer32
_QtechSystemOamFanPad3Index_Object=MibTableColumn
qtechSystemOamFanPad3Index=_QtechSystemOamFanPad3Index_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,1),_QtechSystemOamFanPad3Index_Type())
qtechSystemOamFanPad3Index.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemOamFanPad3Index.setStatus(_A)
_QtechSystemOamFanPad3Name_Type=DisplayString
_QtechSystemOamFanPad3Name_Object=MibTableColumn
qtechSystemOamFanPad3Name=_QtechSystemOamFanPad3Name_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,2),_QtechSystemOamFanPad3Name_Type())
qtechSystemOamFanPad3Name.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemOamFanPad3Name.setStatus(_A)
_QtechSystemFanPad3Speed1_Type=Integer32
_QtechSystemFanPad3Speed1_Object=MibTableColumn
qtechSystemFanPad3Speed1=_QtechSystemFanPad3Speed1_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,3),_QtechSystemFanPad3Speed1_Type())
qtechSystemFanPad3Speed1.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad3Speed1.setStatus(_A)
_QtechSystemFanPad3Speed2_Type=Integer32
_QtechSystemFanPad3Speed2_Object=MibTableColumn
qtechSystemFanPad3Speed2=_QtechSystemFanPad3Speed2_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,4),_QtechSystemFanPad3Speed2_Type())
qtechSystemFanPad3Speed2.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad3Speed2.setStatus(_A)
_QtechSystemFanPad3Speed3_Type=Integer32
_QtechSystemFanPad3Speed3_Object=MibTableColumn
qtechSystemFanPad3Speed3=_QtechSystemFanPad3Speed3_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,5),_QtechSystemFanPad3Speed3_Type())
qtechSystemFanPad3Speed3.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad3Speed3.setStatus(_A)
_QtechSystemFanPad3Speed4_Type=Integer32
_QtechSystemFanPad3Speed4_Object=MibTableColumn
qtechSystemFanPad3Speed4=_QtechSystemFanPad3Speed4_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,6),_QtechSystemFanPad3Speed4_Type())
qtechSystemFanPad3Speed4.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad3Speed4.setStatus(_A)
_QtechSystemFanPad3Speed5_Type=Integer32
_QtechSystemFanPad3Speed5_Object=MibTableColumn
qtechSystemFanPad3Speed5=_QtechSystemFanPad3Speed5_Object((1,3,6,1,4,1,27514,1,1,10,2,1,1,57,1,7),_QtechSystemFanPad3Speed5_Type())
qtechSystemFanPad3Speed5.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSystemFanPad3Speed5.setStatus(_A)
_QtechSystemMIBTraps_ObjectIdentity=ObjectIdentity
qtechSystemMIBTraps=_QtechSystemMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,1,2))
_QtechSystemHardChangeDesc_Type=DisplayString
_QtechSystemHardChangeDesc_Object=MibScalar
qtechSystemHardChangeDesc=_QtechSystemHardChangeDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,1,2,1),_QtechSystemHardChangeDesc_Type())
qtechSystemHardChangeDesc.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:qtechSystemHardChangeDesc.setStatus(_A)
_QtechSystemMIBConformance_ObjectIdentity=ObjectIdentity
qtechSystemMIBConformance=_QtechSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,1,3))
_QtechSystemMIBCompliances_ObjectIdentity=ObjectIdentity
qtechSystemMIBCompliances=_QtechSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,1,3,1))
_QtechSystemMIBGroups_ObjectIdentity=ObjectIdentity
qtechSystemMIBGroups=_QtechSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,1,3,2))
qtechSystemMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,1,3,2,1))
qtechSystemMIBGroup.setObjects(*((_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2),(_C,_A3),(_C,_A4),(_C,_A5)))
if mibBuilder.loadTexts:qtechSystemMIBGroup.setStatus(_A)
qtechSystemHardChangeDetected=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,2))
qtechSystemHardChangeDetected.setObjects((_C,_A6))
if mibBuilder.loadTexts:qtechSystemHardChangeDetected.setStatus(_A)
qtechSystemPowerStateChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,3))
qtechSystemPowerStateChange.setObjects((_C,_A7))
if mibBuilder.loadTexts:qtechSystemPowerStateChange.setStatus(_A)
qtechSystemFanStateChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,4))
qtechSystemFanStateChange.setObjects((_C,_A8))
if mibBuilder.loadTexts:qtechSystemFanStateChange.setStatus(_A)
qtechSystemCPUusageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,5))
qtechSystemCPUusageTooHighTrap.setObjects((_M,_N))
if mibBuilder.loadTexts:qtechSystemCPUusageTooHighTrap.setStatus(_A)
qtechSystemCPUusageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,6))
qtechSystemCPUusageTooHighRecovTrap.setObjects((_M,_N))
if mibBuilder.loadTexts:qtechSystemCPUusageTooHighRecovTrap.setStatus(_A)
qtechSystemTmpTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,7))
qtechSystemTmpTooHighTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:qtechSystemTmpTooHighTrap.setStatus(_A)
qtechSystemTmpTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,8))
qtechSystemTmpTooHighRecovTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:qtechSystemTmpTooHighRecovTrap.setStatus(_A)
qtechSystemMemusageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,9))
qtechSystemMemusageTooHighTrap.setObjects((_K,_L))
if mibBuilder.loadTexts:qtechSystemMemusageTooHighTrap.setStatus(_A)
qtechSystemMemusageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,10))
qtechSystemMemusageTooHighRecovTrap.setObjects((_K,_L))
if mibBuilder.loadTexts:qtechSystemMemusageTooHighRecovTrap.setStatus(_A)
qtechSystemLankApCPUusageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,11))
qtechSystemLankApCPUusageTooHighTrap.setObjects(*((_H,_I),(_M,_N)))
if mibBuilder.loadTexts:qtechSystemLankApCPUusageTooHighTrap.setStatus(_A)
qtechSystemLankApCPUusageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,12))
qtechSystemLankApCPUusageTooHighRecovTrap.setObjects(*((_H,_I),(_M,_N)))
if mibBuilder.loadTexts:qtechSystemLankApCPUusageTooHighRecovTrap.setStatus(_A)
qtechSystemLankApMemusageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,13))
qtechSystemLankApMemusageTooHighTrap.setObjects(*((_H,_I),(_K,_L)))
if mibBuilder.loadTexts:qtechSystemLankApMemusageTooHighTrap.setStatus(_A)
qtechSystemLankApMemusageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,14))
qtechSystemLankApMemusageTooHighRecovTrap.setObjects(*((_H,_I),(_K,_L)))
if mibBuilder.loadTexts:qtechSystemLankApMemusageTooHighRecovTrap.setStatus(_A)
qtechSystemResetTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,15))
if mibBuilder.loadTexts:qtechSystemResetTrap.setStatus(_A)
qtechSystemLankApResetTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,16))
qtechSystemLankApResetTrap.setObjects((_H,_I))
if mibBuilder.loadTexts:qtechSystemLankApResetTrap.setStatus(_A)
qtechSystemPowerOnTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,17))
qtechSystemPowerOnTrap.setObjects((_C,_T))
if mibBuilder.loadTexts:qtechSystemPowerOnTrap.setStatus(_A)
qtechSystemPowerOffTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,18))
qtechSystemPowerOffTrap.setObjects((_C,_T))
if mibBuilder.loadTexts:qtechSystemPowerOffTrap.setStatus(_A)
qtechSystemPowerOnTrapInVSU=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,19))
qtechSystemPowerOnTrapInVSU.setObjects(*((_C,_Z),(_C,_T)))
if mibBuilder.loadTexts:qtechSystemPowerOnTrapInVSU.setStatus(_A)
qtechSystemPowerOffTrapInVSU=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,20))
qtechSystemPowerOffTrapInVSU.setObjects(*((_C,_Z),(_C,_T)))
if mibBuilder.loadTexts:qtechSystemPowerOffTrapInVSU.setStatus(_A)
qtechSystemTmpTableTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,21))
qtechSystemTmpTableTooHighTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:qtechSystemTmpTableTooHighTrap.setStatus(_A)
qtechSystemTmpTableTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,22))
qtechSystemTmpTableTooHighRecovTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:qtechSystemTmpTableTooHighRecovTrap.setStatus(_A)
qtechSystemTmpTableTooHighTrapVSU=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,23))
qtechSystemTmpTableTooHighTrapVSU.setObjects(*((_C,_W),(_C,_J)))
if mibBuilder.loadTexts:qtechSystemTmpTableTooHighTrapVSU.setStatus(_A)
qtechSystemTmpTableTooHighRecovTrapVSU=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,24))
qtechSystemTmpTableTooHighRecovTrapVSU.setObjects(*((_C,_W),(_C,_J)))
if mibBuilder.loadTexts:qtechSystemTmpTableTooHighRecovTrapVSU.setStatus(_A)
qtechSystemFanTableStateChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,25))
qtechSystemFanTableStateChange.setObjects(*((_C,_U),(_C,_V),(_C,_a)))
if mibBuilder.loadTexts:qtechSystemFanTableStateChange.setStatus(_A)
qtechSystemFanTableStateChangeVSU=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,1,2,26))
qtechSystemFanTableStateChangeVSU.setObjects(*((_C,_X),(_C,_U),(_C,_V),(_C,_a)))
if mibBuilder.loadTexts:qtechSystemFanTableStateChangeVSU.setStatus(_A)
qtechSystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,1,3,1,1))
qtechSystemMIBCompliance.setObjects((_C,_A9))
if mibBuilder.loadTexts:qtechSystemMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'qtechSystemMIB':qtechSystemMIB,'qtechSystemMIBObjects':qtechSystemMIBObjects,_y:qtechSystemHwVersion,_z:qtechSystemSwVersion,_A0:qtechSystemBootVersion,_A1:qtechSystemSysCtrlVersion,_A2:qtechSystemParametersSave,_A4:qtechSystemOutBandRate,_A3:qtechSystemReset,_A5:qtechSwitchLayer,_A7:qtechSystemHwPower,_A8:qtechSystemHwFan,'qtechSystemOutBandTimeout':qtechSystemOutBandTimeout,'qtechSystemTelnetTimeout':qtechSystemTelnetTimeout,'qtechSystemMainFile':qtechSystemMainFile,'qtechSystemCurrentPower':qtechSystemCurrentPower,'qtechSystemRemainPower':qtechSystemRemainPower,'qtechSystemTemperature':qtechSystemTemperature,'qtechSystemElectricalSourceNum':qtechSystemElectricalSourceNum,'qtechSystemElectricalSourceIsNormalTable':qtechSystemElectricalSourceIsNormalTable,'qtechSystemElectricalSourceIsNormalEntry':qtechSystemElectricalSourceIsNormalEntry,_e:qtechSystemElectricalSourceIsNormalIndex,'qtechSystemElectricalSourceIsNormal':qtechSystemElectricalSourceIsNormal,'qtechSystemElectricalSourceName':qtechSystemElectricalSourceName,'qtechSystemCurrentVoltage':qtechSystemCurrentVoltage,'qtechSystemFanNUM':qtechSystemFanNUM,'qtechSystemFanIsNormalTable':qtechSystemFanIsNormalTable,'qtechSystemFanIsNormalEntry':qtechSystemFanIsNormalEntry,_f:qtechSystemFanIsNormalIndex,'qtechSystemFanIsNormal':qtechSystemFanIsNormal,'qtechSystemFanName':qtechSystemFanName,'qtechSystemFanSpeed':qtechSystemFanSpeed,'qtechSystemReloadTimeRemain':qtechSystemReloadTimeRemain,'qtechSystemTemperatureTable':qtechSystemTemperatureTable,'qtechSystemTemperatureEntry':qtechSystemTemperatureEntry,_g:qtechSystemTemperatureIndex,'qtechSystemTemperatureName':qtechSystemTemperatureName,_Y:qtechSystemTemperatureCurrent,'qtechSystemTemperatureWarningVaule':qtechSystemTemperatureWarningVaule,'qtechSystemTemperatureCritialVaule':qtechSystemTemperatureCritialVaule,'qtechSystemSerialno':qtechSystemSerialno,'qtechSystemVersionTable':qtechSystemVersionTable,'qtechSystemVersionEntry':qtechSystemVersionEntry,_h:qtechSystemVersionIndex,'qtechSystemVersionName':qtechSystemVersionName,'qtechSystemVersionSwBoot':qtechSystemVersionSwBoot,'qtechSystemVersionSwCtrl':qtechSystemVersionSwCtrl,'qtechSystemVersionSwMain':qtechSystemVersionSwMain,'qtechSystemVersionHw':qtechSystemVersionHw,'qtechSystemVersionSerialno':qtechSystemVersionSerialno,'qtechSystemSysModel':qtechSystemSysModel,'qtechSystemUptime':qtechSystemUptime,'qtechSystemSampleTime':qtechSystemSampleTime,'qtechSystemStatWindowTime':qtechSystemStatWindowTime,'qtechSystemManufacturer':qtechSystemManufacturer,'qtechSystemCurrentTime':qtechSystemCurrentTime,'qtechSystemWarnResendTime':qtechSystemWarnResendTime,'qtechSystemSoftwareName':qtechSystemSoftwareName,'qtechSystemSoftwareManufacturer':qtechSystemSoftwareManufacturer,'qtechSystemCpuType':qtechSystemCpuType,'qtechSystemMemoryType':qtechSystemMemoryType,'qtechSystemMemorySize':qtechSystemMemorySize,'qtechSystemFlashSize':qtechSystemFlashSize,'qtechSystemLankApTable':qtechSystemLankApTable,'qtechSystemLankApEntry':qtechSystemLankApEntry,_i:qtechSystemLankApMacAddr,'qtechSystemLankApStatWindowTime':qtechSystemLankApStatWindowTime,'qtechSystemLankApSampleTime':qtechSystemLankApSampleTime,'qtechSystemLankApReset':qtechSystemLankApReset,'qtechSystemLankApSoftwareName':qtechSystemLankApSoftwareName,'qtechSystemLankApSwVersion':qtechSystemLankApSwVersion,'qtechSystemLankApSoftwareManufacturer':qtechSystemLankApSoftwareManufacturer,'qtechSystemLankApCpuType':qtechSystemLankApCpuType,'qtechSystemLankApMemoryType':qtechSystemLankApMemoryType,'qtechSystemLankApMemorySize':qtechSystemLankApMemorySize,'qtechSystemLankAPFlashSize':qtechSystemLankAPFlashSize,'qtechSystemLankApManufacturer':qtechSystemLankApManufacturer,'qtechSystemLankApSerialno':qtechSystemLankApSerialno,'qtechSystemLankApSysModel':qtechSystemLankApSysModel,'qtechSystemLankApUptime':qtechSystemLankApUptime,'qtechSystemLankApAccurateUptime':qtechSystemLankApAccurateUptime,'qtechSystemLankApHwVersion':qtechSystemLankApHwVersion,'qtechSystemBoardTemperatureTable':qtechSystemBoardTemperatureTable,'qtechSystemBoardTemperatureEntry':qtechSystemBoardTemperatureEntry,_j:qtechSystemBoardTemperatureIndex,'qtechSystemBoardTemperatureName':qtechSystemBoardTemperatureName,'qtechSystemBoardTemperatureCurrent':qtechSystemBoardTemperatureCurrent,'qtechSystemElectricalInformationTable':qtechSystemElectricalInformationTable,'qtechSystemElectricalInformationEntry':qtechSystemElectricalInformationEntry,_k:qtechSystemElectricalInformationDeviceIndex,_l:qtechSystemElectricalInformationIndex,'qtechSystemElectricalInformationStatus':qtechSystemElectricalInformationStatus,'qtechSystemElectricalInformationType':qtechSystemElectricalInformationType,'qtechSystemElectricalInformationAttribute':qtechSystemElectricalInformationAttribute,'qtechSystemElectricalInformationSofeVersion':qtechSystemElectricalInformationSofeVersion,'qtechSystemElectricalInformationHardwareVersion':qtechSystemElectricalInformationHardwareVersion,'qtechSystemElectricalInformationSerial':qtechSystemElectricalInformationSerial,'qtechSystemElectricalInformationProductionDate':qtechSystemElectricalInformationProductionDate,'qtechSystemElectricalInformationRatedPower':qtechSystemElectricalInformationRatedPower,'qtechSystemElectricalInformationInVoltage':qtechSystemElectricalInformationInVoltage,'qtechSystemElectricalInformationInCurrent':qtechSystemElectricalInformationInCurrent,'qtechSystemElectricalInformationOutVoltage':qtechSystemElectricalInformationOutVoltage,'qtechSystemElectricalInformationOutCurrent':qtechSystemElectricalInformationOutCurrent,'qtechSystemElectricalInformationOutPower':qtechSystemElectricalInformationOutPower,'qtechSystemElectricalInformationTemperature':qtechSystemElectricalInformationTemperature,'qtechSystemElectricalInformationAirflowCoexist':qtechSystemElectricalInformationAirflowCoexist,'qtechSystemElectricalInformationWarningStatus':qtechSystemElectricalInformationWarningStatus,'qtechSystemFanInformationTable':qtechSystemFanInformationTable,'qtechSystemFanInformationEntry':qtechSystemFanInformationEntry,_m:qtechSystemFanInformationDeviceIndex,_n:qtechSystemFanInformationFanIndex,'qtechSystemFanInformationStatus':qtechSystemFanInformationStatus,'qtechSystemFanInformationType':qtechSystemFanInformationType,'qtechSystemFanInformationAttribute':qtechSystemFanInformationAttribute,'qtechSystemFanInformationSofeVersion':qtechSystemFanInformationSofeVersion,'qtechSystemFanInformationFirmwareVersion':qtechSystemFanInformationFirmwareVersion,'qtechSystemFanInformationHardwareVersion':qtechSystemFanInformationHardwareVersion,'qtechSystemFanInformationSerial':qtechSystemFanInformationSerial,'qtechSystemFanInformationProductionDate':qtechSystemFanInformationProductionDate,'qtechSystemFanInformationTemperature':qtechSystemFanInformationTemperature,'qtechSystemFanInformationNumber':qtechSystemFanInformationNumber,'qtechSystemFanInformationAirflowCoexist':qtechSystemFanInformationAirflowCoexist,'qtechSystemFanInformationWarningStatus':qtechSystemFanInformationWarningStatus,'qtechSystemFanStatusTable':qtechSystemFanStatusTable,'qtechSystemFanStatusEntry':qtechSystemFanStatusEntry,_X:qtechSystemFanStatusDeviceIndex,_U:qtechSystemFanStatusFanIndex,_V:qtechSystemFanStatusIndex,_a:qtechSystemFanStatus,'qtechSystemFanStatusLevel':qtechSystemFanStatusLevel,'qtechSystemFanStatusSpeed':qtechSystemFanStatusSpeed,'qtechSystemMultipleTemperatureTable':qtechSystemMultipleTemperatureTable,'qtechSystemMultipleTemperatureEntry':qtechSystemMultipleTemperatureEntry,_W:qtechSystemMultipleTemperatureDeviceIndex,_J:qtechSystemMultipleTemperatureSlotIndex,_o:qtechSystemMultipleTemperatureIndex,'qtechSystemMultipleTemperatureName':qtechSystemMultipleTemperatureName,'qtechSystemMultipleTemperatureCurrent':qtechSystemMultipleTemperatureCurrent,'qtechSystemMultipleTemperatureWarning':qtechSystemMultipleTemperatureWarning,'qtechSystemMultipleTemperatureCritical':qtechSystemMultipleTemperatureCritical,'qtechSystemAccurateUptime':qtechSystemAccurateUptime,_T:qtechSystemPowerIndex,_Z:qtechSystemSwitchID,'qtechSystemApDeviceDescriptionTable':qtechSystemApDeviceDescriptionTable,'qtechSystemApDeviceDescriptionEntry':qtechSystemApDeviceDescriptionEntry,_p:qtechSystemApDescMacAddr,'qtechSystemApMemoryType':qtechSystemApMemoryType,'qtechSystemApMemorySize':qtechSystemApMemorySize,'qtechSystemAPFlashType':qtechSystemAPFlashType,'qtechSystemAPFlashSize':qtechSystemAPFlashSize,'qtechSystemApNVRAMSize':qtechSystemApNVRAMSize,'qtechSystemApCFSize':qtechSystemApCFSize,'qtechSystemApCPUType':qtechSystemApCPUType,'qtechSystemApDeviceStatisticsTable':qtechSystemApDeviceStatisticsTable,'qtechSystemApDeviceStatisticsEntry':qtechSystemApDeviceStatisticsEntry,_r:qtechSystemApStatMacAddr,'qtechSystemApInterfaceNum':qtechSystemApInterfaceNum,'qtechSystemApUptime':qtechSystemApUptime,'qtechSystemApCPUUtilizationCurrent':qtechSystemApCPUUtilizationCurrent,'qtechSystemApCPUUtilizationAverage':qtechSystemApCPUUtilizationAverage,'qtechSystemApMemoryPoolCurrentUtilization':qtechSystemApMemoryPoolCurrentUtilization,'qtechSystemApMemoryPoolAverageUtilization':qtechSystemApMemoryPoolAverageUtilization,'qtechSystemApFlashFreeSize':qtechSystemApFlashFreeSize,'qtechSystemAPDeviceTemperature':qtechSystemAPDeviceTemperature,'qtechSystemUptimeMsLow':qtechSystemUptimeMsLow,'qtechSystemUptimeMsHigh':qtechSystemUptimeMsHigh,'qtechSystemFanSNTable':qtechSystemFanSNTable,'qtechSystemFanSNEntry':qtechSystemFanSNEntry,_s:qtechSystemFanPadIndex,'qtechSystemFanPadName':qtechSystemFanPadName,'qtechSystemFanPadSN':qtechSystemFanPadSN,'qtechSystemDsfSNTable':qtechSystemDsfSNTable,'qtechSystemDsfSNEntry':qtechSystemDsfSNEntry,_t:qtechSystemDsfIndex,'qtechSystemDsfName':qtechSystemDsfName,'qtechSystemDsfSN':qtechSystemDsfSN,'qtechSystemPowerSNTable':qtechSystemPowerSNTable,'qtechSystemPowerSNEntry':qtechSystemPowerSNEntry,_u:qtechSystemPowerSNIndex,'qtechSystemPowerSNName':qtechSystemPowerSNName,'qtechSystemPowerSN':qtechSystemPowerSN,'qtechSystemFanPad1SpeedTable':qtechSystemFanPad1SpeedTable,'qtechSystemFanPad1SpeedEntry':qtechSystemFanPad1SpeedEntry,_v:qtechSystemOamFanPad1Index,'qtechSystemOamFanPad1Name':qtechSystemOamFanPad1Name,'qtechSystemFanPad1Speed1':qtechSystemFanPad1Speed1,'qtechSystemFanPad1Speed2':qtechSystemFanPad1Speed2,'qtechSystemFanPad1Speed3':qtechSystemFanPad1Speed3,'qtechSystemFanPad1Speed4':qtechSystemFanPad1Speed4,'qtechSystemFanPad1Speed5':qtechSystemFanPad1Speed5,'qtechSystemFanPad1Speed6':qtechSystemFanPad1Speed6,'qtechSystemFanPad1Speed7':qtechSystemFanPad1Speed7,'qtechSystemFanPad1Speed8':qtechSystemFanPad1Speed8,'qtechSystemFanPad1Speed9':qtechSystemFanPad1Speed9,'qtechSystemFanPad2SpeedTable':qtechSystemFanPad2SpeedTable,'qtechSystemFanPad2SpeedEntry':qtechSystemFanPad2SpeedEntry,_w:qtechSystemOamFanPad2Index,'qtechSystemOamFanPad2Name':qtechSystemOamFanPad2Name,'qtechSystemFanPad2Speed1':qtechSystemFanPad2Speed1,'qtechSystemFanPad2Speed2':qtechSystemFanPad2Speed2,'qtechSystemFanPad2Speed3':qtechSystemFanPad2Speed3,'qtechSystemFanPad3SpeedTable':qtechSystemFanPad3SpeedTable,'qtechSystemFanPad3SpeedEntry':qtechSystemFanPad3SpeedEntry,_x:qtechSystemOamFanPad3Index,'qtechSystemOamFanPad3Name':qtechSystemOamFanPad3Name,'qtechSystemFanPad3Speed1':qtechSystemFanPad3Speed1,'qtechSystemFanPad3Speed2':qtechSystemFanPad3Speed2,'qtechSystemFanPad3Speed3':qtechSystemFanPad3Speed3,'qtechSystemFanPad3Speed4':qtechSystemFanPad3Speed4,'qtechSystemFanPad3Speed5':qtechSystemFanPad3Speed5,'qtechSystemMIBTraps':qtechSystemMIBTraps,_A6:qtechSystemHardChangeDesc,'qtechSystemHardChangeDetected':qtechSystemHardChangeDetected,'qtechSystemPowerStateChange':qtechSystemPowerStateChange,'qtechSystemFanStateChange':qtechSystemFanStateChange,'qtechSystemCPUusageTooHighTrap':qtechSystemCPUusageTooHighTrap,'qtechSystemCPUusageTooHighRecovTrap':qtechSystemCPUusageTooHighRecovTrap,'qtechSystemTmpTooHighTrap':qtechSystemTmpTooHighTrap,'qtechSystemTmpTooHighRecovTrap':qtechSystemTmpTooHighRecovTrap,'qtechSystemMemusageTooHighTrap':qtechSystemMemusageTooHighTrap,'qtechSystemMemusageTooHighRecovTrap':qtechSystemMemusageTooHighRecovTrap,'qtechSystemLankApCPUusageTooHighTrap':qtechSystemLankApCPUusageTooHighTrap,'qtechSystemLankApCPUusageTooHighRecovTrap':qtechSystemLankApCPUusageTooHighRecovTrap,'qtechSystemLankApMemusageTooHighTrap':qtechSystemLankApMemusageTooHighTrap,'qtechSystemLankApMemusageTooHighRecovTrap':qtechSystemLankApMemusageTooHighRecovTrap,'qtechSystemResetTrap':qtechSystemResetTrap,'qtechSystemLankApResetTrap':qtechSystemLankApResetTrap,'qtechSystemPowerOnTrap':qtechSystemPowerOnTrap,'qtechSystemPowerOffTrap':qtechSystemPowerOffTrap,'qtechSystemPowerOnTrapInVSU':qtechSystemPowerOnTrapInVSU,'qtechSystemPowerOffTrapInVSU':qtechSystemPowerOffTrapInVSU,'qtechSystemTmpTableTooHighTrap':qtechSystemTmpTableTooHighTrap,'qtechSystemTmpTableTooHighRecovTrap':qtechSystemTmpTableTooHighRecovTrap,'qtechSystemTmpTableTooHighTrapVSU':qtechSystemTmpTableTooHighTrapVSU,'qtechSystemTmpTableTooHighRecovTrapVSU':qtechSystemTmpTableTooHighRecovTrapVSU,'qtechSystemFanTableStateChange':qtechSystemFanTableStateChange,'qtechSystemFanTableStateChangeVSU':qtechSystemFanTableStateChangeVSU,'qtechSystemMIBConformance':qtechSystemMIBConformance,'qtechSystemMIBCompliances':qtechSystemMIBCompliances,'qtechSystemMIBCompliance':qtechSystemMIBCompliance,'qtechSystemMIBGroups':qtechSystemMIBGroups,_A9:qtechSystemMIBGroup})