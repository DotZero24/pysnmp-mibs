_d='mySystemMIBGroup'
_c='mySystemHwFan'
_b='mySystemHwPower'
_a='mySystemHardChangeDesc'
_Z='mySwitchLayer'
_Y='mySystemOutBandRate'
_X='mySystemReset'
_W='mySystemParametersSave'
_V='mySystemSysCtrlVersion'
_U='mySystemBootVersion'
_T='mySystemSwVersion'
_S='mySystemHwVersion'
_R='mySystemVersionIndex'
_Q='mySystemTemperatureIndex'
_P='mySystemFanIsNormalIndex'
_O='unknow'
_N='powerbutabnormal'
_M='normal'
_L='existreadypower'
_K='existnopower'
_J='noexist'
_I='mySystemElectricalSourceIsNormalIndex'
_H='seconds'
_G='obsolete'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='DES7200-SYSTEM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
mySystemMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,1))
if mibBuilder.loadTexts:mySystemMIB.setRevisions(('2002-03-20 00:00',))
_MySystemMIBObjects_ObjectIdentity=ObjectIdentity
mySystemMIBObjects=_MySystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,1,1))
class _MySystemHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MySystemHwVersion_Type.__name__=_F
_MySystemHwVersion_Object=MibScalar
mySystemHwVersion=_MySystemHwVersion_Object((1,3,6,1,4,1,171,10,97,2,1,1,1),_MySystemHwVersion_Type())
mySystemHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemHwVersion.setStatus(_A)
class _MySystemSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MySystemSwVersion_Type.__name__=_F
_MySystemSwVersion_Object=MibScalar
mySystemSwVersion=_MySystemSwVersion_Object((1,3,6,1,4,1,171,10,97,2,1,1,2),_MySystemSwVersion_Type())
mySystemSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemSwVersion.setStatus(_A)
class _MySystemBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MySystemBootVersion_Type.__name__=_F
_MySystemBootVersion_Object=MibScalar
mySystemBootVersion=_MySystemBootVersion_Object((1,3,6,1,4,1,171,10,97,2,1,1,3),_MySystemBootVersion_Type())
mySystemBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemBootVersion.setStatus(_A)
class _MySystemSysCtrlVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MySystemSysCtrlVersion_Type.__name__=_F
_MySystemSysCtrlVersion_Object=MibScalar
mySystemSysCtrlVersion=_MySystemSysCtrlVersion_Object((1,3,6,1,4,1,171,10,97,2,1,1,4),_MySystemSysCtrlVersion_Type())
mySystemSysCtrlVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemSysCtrlVersion.setStatus(_A)
_MySystemParametersSave_Type=Integer32
_MySystemParametersSave_Object=MibScalar
mySystemParametersSave=_MySystemParametersSave_Object((1,3,6,1,4,1,171,10,97,2,1,1,5),_MySystemParametersSave_Type())
mySystemParametersSave.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemParametersSave.setStatus(_A)
class _MySystemOutBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('baud9600',1),('baud19200',2),('baud38400',3),('baud57600',4),('baud115200',5)))
_MySystemOutBandRate_Type.__name__=_D
_MySystemOutBandRate_Object=MibScalar
mySystemOutBandRate=_MySystemOutBandRate_Object((1,3,6,1,4,1,171,10,97,2,1,1,6),_MySystemOutBandRate_Type())
mySystemOutBandRate.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemOutBandRate.setStatus(_A)
_MySystemReset_Type=Integer32
_MySystemReset_Object=MibScalar
mySystemReset=_MySystemReset_Object((1,3,6,1,4,1,171,10,97,2,1,1,7),_MySystemReset_Type())
mySystemReset.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemReset.setStatus(_A)
class _MySwitchLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('layer2',1),('layer3',2),('router',3)))
_MySwitchLayer_Type.__name__=_D
_MySwitchLayer_Object=MibScalar
mySwitchLayer=_MySwitchLayer_Object((1,3,6,1,4,1,171,10,97,2,1,1,8),_MySwitchLayer_Type())
mySwitchLayer.setMaxAccess(_B)
if mibBuilder.loadTexts:mySwitchLayer.setStatus(_A)
class _MySystemHwPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rpsNoLink',1),('rpsLinkAndNoPower',2),('rpsLinkAndReadyForPower',3),('rpsLinkAndPower',4)))
_MySystemHwPower_Type.__name__=_D
_MySystemHwPower_Object=MibScalar
mySystemHwPower=_MySystemHwPower_Object((1,3,6,1,4,1,171,10,97,2,1,1,9),_MySystemHwPower_Type())
mySystemHwPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemHwPower.setStatus(_A)
class _MySystemHwFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('work',1),('stop',2)))
_MySystemHwFan_Type.__name__=_D
_MySystemHwFan_Object=MibScalar
mySystemHwFan=_MySystemHwFan_Object((1,3,6,1,4,1,171,10,97,2,1,1,10),_MySystemHwFan_Type())
mySystemHwFan.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemHwFan.setStatus(_A)
class _MySystemOutBandTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MySystemOutBandTimeout_Type.__name__=_D
_MySystemOutBandTimeout_Object=MibScalar
mySystemOutBandTimeout=_MySystemOutBandTimeout_Object((1,3,6,1,4,1,171,10,97,2,1,1,11),_MySystemOutBandTimeout_Type())
mySystemOutBandTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemOutBandTimeout.setStatus(_G)
if mibBuilder.loadTexts:mySystemOutBandTimeout.setUnits(_H)
class _MySystemTelnetTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MySystemTelnetTimeout_Type.__name__=_D
_MySystemTelnetTimeout_Object=MibScalar
mySystemTelnetTimeout=_MySystemTelnetTimeout_Object((1,3,6,1,4,1,171,10,97,2,1,1,12),_MySystemTelnetTimeout_Type())
mySystemTelnetTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemTelnetTimeout.setStatus(_G)
if mibBuilder.loadTexts:mySystemTelnetTimeout.setUnits(_H)
class _MySystemMainFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MySystemMainFile_Type.__name__=_F
_MySystemMainFile_Object=MibScalar
mySystemMainFile=_MySystemMainFile_Object((1,3,6,1,4,1,171,10,97,2,1,1,13),_MySystemMainFile_Type())
mySystemMainFile.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemMainFile.setStatus(_A)
_MySystemCurrentPower_Type=Integer32
_MySystemCurrentPower_Object=MibScalar
mySystemCurrentPower=_MySystemCurrentPower_Object((1,3,6,1,4,1,171,10,97,2,1,1,14),_MySystemCurrentPower_Type())
mySystemCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemCurrentPower.setStatus(_A)
_MySystemRemainPower_Type=Integer32
_MySystemRemainPower_Object=MibScalar
mySystemRemainPower=_MySystemRemainPower_Object((1,3,6,1,4,1,171,10,97,2,1,1,15),_MySystemRemainPower_Type())
mySystemRemainPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemRemainPower.setStatus(_A)
_MySystemTemperature_Type=Integer32
_MySystemTemperature_Object=MibScalar
mySystemTemperature=_MySystemTemperature_Object((1,3,6,1,4,1,171,10,97,2,1,1,16),_MySystemTemperature_Type())
mySystemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemTemperature.setStatus(_A)
_MySystemElectricalSourceNum_Type=Integer32
_MySystemElectricalSourceNum_Object=MibScalar
mySystemElectricalSourceNum=_MySystemElectricalSourceNum_Object((1,3,6,1,4,1,171,10,97,2,1,1,17),_MySystemElectricalSourceNum_Type())
mySystemElectricalSourceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemElectricalSourceNum.setStatus(_A)
_MySystemElectricalSourceIsNormalTable_Object=MibTable
mySystemElectricalSourceIsNormalTable=_MySystemElectricalSourceIsNormalTable_Object((1,3,6,1,4,1,171,10,97,2,1,1,18))
if mibBuilder.loadTexts:mySystemElectricalSourceIsNormalTable.setStatus(_A)
_MySystemElectricalSourceIsNormalEntry_Object=MibTableRow
mySystemElectricalSourceIsNormalEntry=_MySystemElectricalSourceIsNormalEntry_Object((1,3,6,1,4,1,171,10,97,2,1,1,18,1))
mySystemElectricalSourceIsNormalEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:mySystemElectricalSourceIsNormalEntry.setStatus(_A)
_MySystemElectricalSourceIsNormalIndex_Type=Integer32
_MySystemElectricalSourceIsNormalIndex_Object=MibTableColumn
mySystemElectricalSourceIsNormalIndex=_MySystemElectricalSourceIsNormalIndex_Object((1,3,6,1,4,1,171,10,97,2,1,1,18,1,1),_MySystemElectricalSourceIsNormalIndex_Type())
mySystemElectricalSourceIsNormalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemElectricalSourceIsNormalIndex.setStatus(_A)
class _MySystemElectricalSourceIsNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6)))
_MySystemElectricalSourceIsNormal_Type.__name__=_D
_MySystemElectricalSourceIsNormal_Object=MibTableColumn
mySystemElectricalSourceIsNormal=_MySystemElectricalSourceIsNormal_Object((1,3,6,1,4,1,171,10,97,2,1,1,18,1,2),_MySystemElectricalSourceIsNormal_Type())
mySystemElectricalSourceIsNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemElectricalSourceIsNormal.setStatus(_A)
_MySystemElectricalSourceName_Type=DisplayString
_MySystemElectricalSourceName_Object=MibTableColumn
mySystemElectricalSourceName=_MySystemElectricalSourceName_Object((1,3,6,1,4,1,171,10,97,2,1,1,18,1,3),_MySystemElectricalSourceName_Type())
mySystemElectricalSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemElectricalSourceName.setStatus(_A)
_MySystemCurrentVoltage_Type=Integer32
_MySystemCurrentVoltage_Object=MibScalar
mySystemCurrentVoltage=_MySystemCurrentVoltage_Object((1,3,6,1,4,1,171,10,97,2,1,1,19),_MySystemCurrentVoltage_Type())
mySystemCurrentVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemCurrentVoltage.setStatus(_A)
_MySystemFanNUM_Type=Integer32
_MySystemFanNUM_Object=MibScalar
mySystemFanNUM=_MySystemFanNUM_Object((1,3,6,1,4,1,171,10,97,2,1,1,20),_MySystemFanNUM_Type())
mySystemFanNUM.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemFanNUM.setStatus(_A)
_MySystemFanIsNormalTable_Object=MibTable
mySystemFanIsNormalTable=_MySystemFanIsNormalTable_Object((1,3,6,1,4,1,171,10,97,2,1,1,21))
if mibBuilder.loadTexts:mySystemFanIsNormalTable.setStatus(_A)
_MySystemFanIsNormalEntry_Object=MibTableRow
mySystemFanIsNormalEntry=_MySystemFanIsNormalEntry_Object((1,3,6,1,4,1,171,10,97,2,1,1,21,1))
mySystemFanIsNormalEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:mySystemFanIsNormalEntry.setStatus(_A)
_MySystemFanIsNormalIndex_Type=Integer32
_MySystemFanIsNormalIndex_Object=MibTableColumn
mySystemFanIsNormalIndex=_MySystemFanIsNormalIndex_Object((1,3,6,1,4,1,171,10,97,2,1,1,21,1,1),_MySystemFanIsNormalIndex_Type())
mySystemFanIsNormalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemFanIsNormalIndex.setStatus(_A)
class _MySystemFanIsNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6)))
_MySystemFanIsNormal_Type.__name__=_D
_MySystemFanIsNormal_Object=MibTableColumn
mySystemFanIsNormal=_MySystemFanIsNormal_Object((1,3,6,1,4,1,171,10,97,2,1,1,21,1,2),_MySystemFanIsNormal_Type())
mySystemFanIsNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemFanIsNormal.setStatus(_A)
_MySystemFanName_Type=DisplayString
_MySystemFanName_Object=MibTableColumn
mySystemFanName=_MySystemFanName_Object((1,3,6,1,4,1,171,10,97,2,1,1,21,1,3),_MySystemFanName_Type())
mySystemFanName.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemFanName.setStatus(_A)
_MySystemReloadTimeRemain_Type=Integer32
_MySystemReloadTimeRemain_Object=MibScalar
mySystemReloadTimeRemain=_MySystemReloadTimeRemain_Object((1,3,6,1,4,1,171,10,97,2,1,1,22),_MySystemReloadTimeRemain_Type())
mySystemReloadTimeRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemReloadTimeRemain.setStatus(_A)
_MySystemTemperatureTable_Object=MibTable
mySystemTemperatureTable=_MySystemTemperatureTable_Object((1,3,6,1,4,1,171,10,97,2,1,1,23))
if mibBuilder.loadTexts:mySystemTemperatureTable.setStatus(_A)
_MySystemTemperatureEntry_Object=MibTableRow
mySystemTemperatureEntry=_MySystemTemperatureEntry_Object((1,3,6,1,4,1,171,10,97,2,1,1,23,1))
mySystemTemperatureEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:mySystemTemperatureEntry.setStatus(_A)
_MySystemTemperatureIndex_Type=Integer32
_MySystemTemperatureIndex_Object=MibTableColumn
mySystemTemperatureIndex=_MySystemTemperatureIndex_Object((1,3,6,1,4,1,171,10,97,2,1,1,23,1,1),_MySystemTemperatureIndex_Type())
mySystemTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemTemperatureIndex.setStatus(_A)
_MySystemTemperatureName_Type=DisplayString
_MySystemTemperatureName_Object=MibTableColumn
mySystemTemperatureName=_MySystemTemperatureName_Object((1,3,6,1,4,1,171,10,97,2,1,1,23,1,2),_MySystemTemperatureName_Type())
mySystemTemperatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemTemperatureName.setStatus(_A)
_MySystemTemperatureCurrent_Type=Integer32
_MySystemTemperatureCurrent_Object=MibTableColumn
mySystemTemperatureCurrent=_MySystemTemperatureCurrent_Object((1,3,6,1,4,1,171,10,97,2,1,1,23,1,3),_MySystemTemperatureCurrent_Type())
mySystemTemperatureCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemTemperatureCurrent.setStatus(_A)
_MySystemTemperatureWarningVaule_Type=Integer32
_MySystemTemperatureWarningVaule_Object=MibTableColumn
mySystemTemperatureWarningVaule=_MySystemTemperatureWarningVaule_Object((1,3,6,1,4,1,171,10,97,2,1,1,23,1,4),_MySystemTemperatureWarningVaule_Type())
mySystemTemperatureWarningVaule.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemTemperatureWarningVaule.setStatus(_A)
_MySystemTemperatureCritialVaule_Type=Integer32
_MySystemTemperatureCritialVaule_Object=MibTableColumn
mySystemTemperatureCritialVaule=_MySystemTemperatureCritialVaule_Object((1,3,6,1,4,1,171,10,97,2,1,1,23,1,5),_MySystemTemperatureCritialVaule_Type())
mySystemTemperatureCritialVaule.setMaxAccess(_E)
if mibBuilder.loadTexts:mySystemTemperatureCritialVaule.setStatus(_A)
_MySystemSerialno_Type=DisplayString
_MySystemSerialno_Object=MibScalar
mySystemSerialno=_MySystemSerialno_Object((1,3,6,1,4,1,171,10,97,2,1,1,24),_MySystemSerialno_Type())
mySystemSerialno.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemSerialno.setStatus(_A)
_MySystemVersionTable_Object=MibTable
mySystemVersionTable=_MySystemVersionTable_Object((1,3,6,1,4,1,171,10,97,2,1,1,25))
if mibBuilder.loadTexts:mySystemVersionTable.setStatus(_A)
_MySystemVersionEntry_Object=MibTableRow
mySystemVersionEntry=_MySystemVersionEntry_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1))
mySystemVersionEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:mySystemVersionEntry.setStatus(_A)
_MySystemVersionIndex_Type=Unsigned32
_MySystemVersionIndex_Object=MibTableColumn
mySystemVersionIndex=_MySystemVersionIndex_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,1),_MySystemVersionIndex_Type())
mySystemVersionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionIndex.setStatus(_A)
_MySystemVersionName_Type=DisplayString
_MySystemVersionName_Object=MibTableColumn
mySystemVersionName=_MySystemVersionName_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,2),_MySystemVersionName_Type())
mySystemVersionName.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionName.setStatus(_A)
_MySystemVersionSwBoot_Type=DisplayString
_MySystemVersionSwBoot_Object=MibTableColumn
mySystemVersionSwBoot=_MySystemVersionSwBoot_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,3),_MySystemVersionSwBoot_Type())
mySystemVersionSwBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionSwBoot.setStatus(_A)
_MySystemVersionSwCtrl_Type=DisplayString
_MySystemVersionSwCtrl_Object=MibTableColumn
mySystemVersionSwCtrl=_MySystemVersionSwCtrl_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,4),_MySystemVersionSwCtrl_Type())
mySystemVersionSwCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionSwCtrl.setStatus(_A)
_MySystemVersionSwMain_Type=DisplayString
_MySystemVersionSwMain_Object=MibTableColumn
mySystemVersionSwMain=_MySystemVersionSwMain_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,5),_MySystemVersionSwMain_Type())
mySystemVersionSwMain.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionSwMain.setStatus(_A)
_MySystemVersionHw_Type=DisplayString
_MySystemVersionHw_Object=MibTableColumn
mySystemVersionHw=_MySystemVersionHw_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,6),_MySystemVersionHw_Type())
mySystemVersionHw.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionHw.setStatus(_A)
_MySystemVersionSerialno_Type=DisplayString
_MySystemVersionSerialno_Object=MibTableColumn
mySystemVersionSerialno=_MySystemVersionSerialno_Object((1,3,6,1,4,1,171,10,97,2,1,1,25,1,7),_MySystemVersionSerialno_Type())
mySystemVersionSerialno.setMaxAccess(_B)
if mibBuilder.loadTexts:mySystemVersionSerialno.setStatus(_A)
_MySystemMIBTraps_ObjectIdentity=ObjectIdentity
mySystemMIBTraps=_MySystemMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,1,2))
_MySystemHardChangeDesc_Type=DisplayString
_MySystemHardChangeDesc_Object=MibScalar
mySystemHardChangeDesc=_MySystemHardChangeDesc_Object((1,3,6,1,4,1,171,10,97,2,1,2,1),_MySystemHardChangeDesc_Type())
mySystemHardChangeDesc.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:mySystemHardChangeDesc.setStatus(_A)
_MySystemMIBConformance_ObjectIdentity=ObjectIdentity
mySystemMIBConformance=_MySystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,1,3))
_MySystemMIBCompliances_ObjectIdentity=ObjectIdentity
mySystemMIBCompliances=_MySystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,1,3,1))
_MySystemMIBGroups_ObjectIdentity=ObjectIdentity
mySystemMIBGroups=_MySystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,1,3,2))
mySystemMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,1,3,2,1))
mySystemMIBGroup.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:mySystemMIBGroup.setStatus(_A)
mySystemHardChangeDetected=NotificationType((1,3,6,1,4,1,171,10,97,2,1,2,2))
mySystemHardChangeDetected.setObjects((_C,_a))
if mibBuilder.loadTexts:mySystemHardChangeDetected.setStatus(_A)
mySystemPowerStateChange=NotificationType((1,3,6,1,4,1,171,10,97,2,1,2,3))
mySystemPowerStateChange.setObjects((_C,_b))
if mibBuilder.loadTexts:mySystemPowerStateChange.setStatus(_A)
mySystemFanStateChange=NotificationType((1,3,6,1,4,1,171,10,97,2,1,2,4))
mySystemFanStateChange.setObjects((_C,_c))
if mibBuilder.loadTexts:mySystemFanStateChange.setStatus(_A)
mySystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,1,3,1,1))
mySystemMIBCompliance.setObjects((_C,_d))
if mibBuilder.loadTexts:mySystemMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mySystemMIB':mySystemMIB,'mySystemMIBObjects':mySystemMIBObjects,_S:mySystemHwVersion,_T:mySystemSwVersion,_U:mySystemBootVersion,_V:mySystemSysCtrlVersion,_W:mySystemParametersSave,_Y:mySystemOutBandRate,_X:mySystemReset,_Z:mySwitchLayer,_b:mySystemHwPower,_c:mySystemHwFan,'mySystemOutBandTimeout':mySystemOutBandTimeout,'mySystemTelnetTimeout':mySystemTelnetTimeout,'mySystemMainFile':mySystemMainFile,'mySystemCurrentPower':mySystemCurrentPower,'mySystemRemainPower':mySystemRemainPower,'mySystemTemperature':mySystemTemperature,'mySystemElectricalSourceNum':mySystemElectricalSourceNum,'mySystemElectricalSourceIsNormalTable':mySystemElectricalSourceIsNormalTable,'mySystemElectricalSourceIsNormalEntry':mySystemElectricalSourceIsNormalEntry,_I:mySystemElectricalSourceIsNormalIndex,'mySystemElectricalSourceIsNormal':mySystemElectricalSourceIsNormal,'mySystemElectricalSourceName':mySystemElectricalSourceName,'mySystemCurrentVoltage':mySystemCurrentVoltage,'mySystemFanNUM':mySystemFanNUM,'mySystemFanIsNormalTable':mySystemFanIsNormalTable,'mySystemFanIsNormalEntry':mySystemFanIsNormalEntry,_P:mySystemFanIsNormalIndex,'mySystemFanIsNormal':mySystemFanIsNormal,'mySystemFanName':mySystemFanName,'mySystemReloadTimeRemain':mySystemReloadTimeRemain,'mySystemTemperatureTable':mySystemTemperatureTable,'mySystemTemperatureEntry':mySystemTemperatureEntry,_Q:mySystemTemperatureIndex,'mySystemTemperatureName':mySystemTemperatureName,'mySystemTemperatureCurrent':mySystemTemperatureCurrent,'mySystemTemperatureWarningVaule':mySystemTemperatureWarningVaule,'mySystemTemperatureCritialVaule':mySystemTemperatureCritialVaule,'mySystemSerialno':mySystemSerialno,'mySystemVersionTable':mySystemVersionTable,'mySystemVersionEntry':mySystemVersionEntry,_R:mySystemVersionIndex,'mySystemVersionName':mySystemVersionName,'mySystemVersionSwBoot':mySystemVersionSwBoot,'mySystemVersionSwCtrl':mySystemVersionSwCtrl,'mySystemVersionSwMain':mySystemVersionSwMain,'mySystemVersionHw':mySystemVersionHw,'mySystemVersionSerialno':mySystemVersionSerialno,'mySystemMIBTraps':mySystemMIBTraps,_a:mySystemHardChangeDesc,'mySystemHardChangeDetected':mySystemHardChangeDetected,'mySystemPowerStateChange':mySystemPowerStateChange,'mySystemFanStateChange':mySystemFanStateChange,'mySystemMIBConformance':mySystemMIBConformance,'mySystemMIBCompliances':mySystemMIBCompliances,'mySystemMIBCompliance':mySystemMIBCompliance,'mySystemMIBGroups':mySystemMIBGroups,_d:mySystemMIBGroup})