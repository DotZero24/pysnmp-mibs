_N='chassisPortLEDIFIndex'
_M='chassisTemperatureSlotIndex'
_L='chassisSlotIndex'
_K='chassisFanIndex'
_J='chassisPowerIndex'
_I='blinking-green'
_H='steady-green'
_G='chassisControlModuleLEDInfoIndex'
_F='in-operation'
_E='failed'
_D='DGS-6600-EQUIPMENT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dgs6600_system,=mibBuilder.importSymbols('DGS-6600-ID-MIB','dgs6600-system')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
dgs6600EquipmentMIB=ModuleIdentity((1,3,6,1,4,1,171,10,120,100,1,2))
_ChassisControlModuleLEDInfo_ObjectIdentity=ObjectIdentity
chassisControlModuleLEDInfo=_ChassisControlModuleLEDInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,2,1))
_ChassisControlModuleLEDInfoTable_Object=MibTable
chassisControlModuleLEDInfoTable=_ChassisControlModuleLEDInfoTable_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1))
if mibBuilder.loadTexts:chassisControlModuleLEDInfoTable.setStatus(_A)
_ChassisControlModuleLEDInfoEntry_Object=MibTableRow
chassisControlModuleLEDInfoEntry=_ChassisControlModuleLEDInfoEntry_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1))
chassisControlModuleLEDInfoEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:chassisControlModuleLEDInfoEntry.setStatus(_A)
class _ChassisControlModuleLEDInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ChassisControlModuleLEDInfoIndex_Type.__name__=_C
_ChassisControlModuleLEDInfoIndex_Object=MibTableColumn
chassisControlModuleLEDInfoIndex=_ChassisControlModuleLEDInfoIndex_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1,1),_ChassisControlModuleLEDInfoIndex_Type())
chassisControlModuleLEDInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisControlModuleLEDInfoIndex.setStatus(_A)
class _ChassisControlModuleLEDInfoConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rs232',1),('usb',2)))
_ChassisControlModuleLEDInfoConsole_Type.__name__=_C
_ChassisControlModuleLEDInfoConsole_Object=MibTableColumn
chassisControlModuleLEDInfoConsole=_ChassisControlModuleLEDInfoConsole_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1,2),_ChassisControlModuleLEDInfoConsole_Type())
chassisControlModuleLEDInfoConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisControlModuleLEDInfoConsole.setStatus(_A)
class _ChassisControlModuleLEDInfoMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
_ChassisControlModuleLEDInfoMaster_Type.__name__=_C
_ChassisControlModuleLEDInfoMaster_Object=MibTableColumn
chassisControlModuleLEDInfoMaster=_ChassisControlModuleLEDInfoMaster_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1,3),_ChassisControlModuleLEDInfoMaster_Type())
chassisControlModuleLEDInfoMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisControlModuleLEDInfoMaster.setStatus(_A)
class _ChassisControlModuleLEDInfoCPUUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('zero-LED',0),('one-LED',1),('two-LEDs',2),('three-LEDs',3),('four-LEDs',4),('five-LEDs',5),('six-LEDs',6),('seven-LEDs',7),('eight-LEDs',8)))
_ChassisControlModuleLEDInfoCPUUtilization_Type.__name__=_C
_ChassisControlModuleLEDInfoCPUUtilization_Object=MibTableColumn
chassisControlModuleLEDInfoCPUUtilization=_ChassisControlModuleLEDInfoCPUUtilization_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1,4),_ChassisControlModuleLEDInfoCPUUtilization_Type())
chassisControlModuleLEDInfoCPUUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisControlModuleLEDInfoCPUUtilization.setStatus(_A)
class _ChassisControlModuleLEDInfoMgmtPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),(_H,2),(_I,3)))
_ChassisControlModuleLEDInfoMgmtPortStatus_Type.__name__=_C
_ChassisControlModuleLEDInfoMgmtPortStatus_Object=MibTableColumn
chassisControlModuleLEDInfoMgmtPortStatus=_ChassisControlModuleLEDInfoMgmtPortStatus_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1,5),_ChassisControlModuleLEDInfoMgmtPortStatus_Type())
chassisControlModuleLEDInfoMgmtPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisControlModuleLEDInfoMgmtPortStatus.setStatus(_A)
class _ChassisControlModuleLEDInfoMgmtPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('link-0',1),('link-100',2),('link-1000',3)))
_ChassisControlModuleLEDInfoMgmtPortSpeed_Type.__name__=_C
_ChassisControlModuleLEDInfoMgmtPortSpeed_Object=MibTableColumn
chassisControlModuleLEDInfoMgmtPortSpeed=_ChassisControlModuleLEDInfoMgmtPortSpeed_Object((1,3,6,1,4,1,171,10,120,100,1,2,1,1,1,6),_ChassisControlModuleLEDInfoMgmtPortSpeed_Type())
chassisControlModuleLEDInfoMgmtPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisControlModuleLEDInfoMgmtPortSpeed.setStatus(_A)
_ChassisPowerInfo_ObjectIdentity=ObjectIdentity
chassisPowerInfo=_ChassisPowerInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,2,2))
_ChassisPowerInfoTable_Object=MibTable
chassisPowerInfoTable=_ChassisPowerInfoTable_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1))
if mibBuilder.loadTexts:chassisPowerInfoTable.setStatus(_A)
_ChassisPowerInfoEntry_Object=MibTableRow
chassisPowerInfoEntry=_ChassisPowerInfoEntry_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1))
chassisPowerInfoEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:chassisPowerInfoEntry.setStatus(_A)
class _ChassisPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ChassisPowerIndex_Type.__name__=_C
_ChassisPowerIndex_Object=MibTableColumn
chassisPowerIndex=_ChassisPowerIndex_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,1),_ChassisPowerIndex_Type())
chassisPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerIndex.setStatus(_A)
class _ChassisPowerExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('empty',1),('exist',2)))
_ChassisPowerExist_Type.__name__=_C
_ChassisPowerExist_Object=MibTableColumn
chassisPowerExist=_ChassisPowerExist_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,2),_ChassisPowerExist_Type())
chassisPowerExist.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerExist.setStatus(_A)
class _ChassisPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('AC',1),('DC',2),('Unknown',3)))
_ChassisPowerType_Type.__name__=_C
_ChassisPowerType_Object=MibTableColumn
chassisPowerType=_ChassisPowerType_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,3),_ChassisPowerType_Type())
chassisPowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerType.setStatus(_A)
class _ChassisPowerAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ChassisPowerAlive_Type.__name__=_C
_ChassisPowerAlive_Object=MibTableColumn
chassisPowerAlive=_ChassisPowerAlive_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,4),_ChassisPowerAlive_Type())
chassisPowerAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerAlive.setStatus(_A)
_ChassisPowerVoltage_Type=Integer32
_ChassisPowerVoltage_Object=MibTableColumn
chassisPowerVoltage=_ChassisPowerVoltage_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,5),_ChassisPowerVoltage_Type())
chassisPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerVoltage.setStatus(_A)
_ChassisPowerCurrent_Type=Integer32
_ChassisPowerCurrent_Object=MibTableColumn
chassisPowerCurrent=_ChassisPowerCurrent_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,6),_ChassisPowerCurrent_Type())
chassisPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerCurrent.setStatus(_A)
_ChassisPowerPowerWatt_Type=Integer32
_ChassisPowerPowerWatt_Object=MibTableColumn
chassisPowerPowerWatt=_ChassisPowerPowerWatt_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,7),_ChassisPowerPowerWatt_Type())
chassisPowerPowerWatt.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerPowerWatt.setStatus(_A)
_ChassisPowerFanSpeed_Type=Integer32
_ChassisPowerFanSpeed_Object=MibTableColumn
chassisPowerFanSpeed=_ChassisPowerFanSpeed_Object((1,3,6,1,4,1,171,10,120,100,1,2,2,1,1,8),_ChassisPowerFanSpeed_Type())
chassisPowerFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPowerFanSpeed.setStatus(_A)
_ChassisFanTrayInfo_ObjectIdentity=ObjectIdentity
chassisFanTrayInfo=_ChassisFanTrayInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,2,3))
class _ChassisFanTrayInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-exist',1),(_E,2),(_F,3)))
_ChassisFanTrayInfoState_Type.__name__=_C
_ChassisFanTrayInfoState_Object=MibScalar
chassisFanTrayInfoState=_ChassisFanTrayInfoState_Object((1,3,6,1,4,1,171,10,120,100,1,2,3,1),_ChassisFanTrayInfoState_Type())
chassisFanTrayInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFanTrayInfoState.setStatus(_A)
_ChassisFanInfoTable_Object=MibTable
chassisFanInfoTable=_ChassisFanInfoTable_Object((1,3,6,1,4,1,171,10,120,100,1,2,3,2))
if mibBuilder.loadTexts:chassisFanInfoTable.setStatus(_A)
_ChassisFanInfoEntry_Object=MibTableRow
chassisFanInfoEntry=_ChassisFanInfoEntry_Object((1,3,6,1,4,1,171,10,120,100,1,2,3,2,1))
chassisFanInfoEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:chassisFanInfoEntry.setStatus(_A)
class _ChassisFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ChassisFanIndex_Type.__name__=_C
_ChassisFanIndex_Object=MibTableColumn
chassisFanIndex=_ChassisFanIndex_Object((1,3,6,1,4,1,171,10,120,100,1,2,3,2,1,1),_ChassisFanIndex_Type())
chassisFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFanIndex.setStatus(_A)
class _ChassisFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('ok',2)))
_ChassisFanStatus_Type.__name__=_C
_ChassisFanStatus_Object=MibTableColumn
chassisFanStatus=_ChassisFanStatus_Object((1,3,6,1,4,1,171,10,120,100,1,2,3,2,1,2),_ChassisFanStatus_Type())
chassisFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFanStatus.setStatus(_A)
_ChassisFanSpeed_Type=Integer32
_ChassisFanSpeed_Object=MibTableColumn
chassisFanSpeed=_ChassisFanSpeed_Object((1,3,6,1,4,1,171,10,120,100,1,2,3,2,1,3),_ChassisFanSpeed_Type())
chassisFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFanSpeed.setStatus(_A)
_ChassisSlotInfo_ObjectIdentity=ObjectIdentity
chassisSlotInfo=_ChassisSlotInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,2,4))
_ChassisSlotInfoTable_Object=MibTable
chassisSlotInfoTable=_ChassisSlotInfoTable_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1))
if mibBuilder.loadTexts:chassisSlotInfoTable.setStatus(_A)
_ChassisSlotInfoEntry_Object=MibTableRow
chassisSlotInfoEntry=_ChassisSlotInfoEntry_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1))
chassisSlotInfoEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:chassisSlotInfoEntry.setStatus(_A)
class _ChassisSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ChassisSlotIndex_Type.__name__=_C
_ChassisSlotIndex_Object=MibTableColumn
chassisSlotIndex=_ChassisSlotIndex_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,1),_ChassisSlotIndex_Type())
chassisSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotIndex.setStatus(_A)
class _ChassisSlotState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('empty',1),('no-power',2),(_E,3),('booting',4),(_F,5)))
_ChassisSlotState_Type.__name__=_C
_ChassisSlotState_Object=MibTableColumn
chassisSlotState=_ChassisSlotState_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,2),_ChassisSlotState_Type())
chassisSlotState.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotState.setStatus(_A)
class _ChassisSlotLEDPoEModeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_ChassisSlotLEDPoEModeEnabled_Type.__name__=_C
_ChassisSlotLEDPoEModeEnabled_Object=MibTableColumn
chassisSlotLEDPoEModeEnabled=_ChassisSlotLEDPoEModeEnabled_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,3),_ChassisSlotLEDPoEModeEnabled_Type())
chassisSlotLEDPoEModeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotLEDPoEModeEnabled.setStatus(_A)
_ChassisSlotModel_Type=DisplayString
_ChassisSlotModel_Object=MibTableColumn
chassisSlotModel=_ChassisSlotModel_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,4),_ChassisSlotModel_Type())
chassisSlotModel.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotModel.setStatus(_A)
_ChassisSlotSerialNumber_Type=DisplayString
_ChassisSlotSerialNumber_Object=MibTableColumn
chassisSlotSerialNumber=_ChassisSlotSerialNumber_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,5),_ChassisSlotSerialNumber_Type())
chassisSlotSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotSerialNumber.setStatus(_A)
_ChassisSlotHwVersion_Type=DisplayString
_ChassisSlotHwVersion_Object=MibTableColumn
chassisSlotHwVersion=_ChassisSlotHwVersion_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,6),_ChassisSlotHwVersion_Type())
chassisSlotHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotHwVersion.setStatus(_A)
_ChassisSlotPCBAVersion_Type=DisplayString
_ChassisSlotPCBAVersion_Object=MibTableColumn
chassisSlotPCBAVersion=_ChassisSlotPCBAVersion_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,7),_ChassisSlotPCBAVersion_Type())
chassisSlotPCBAVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotPCBAVersion.setStatus(_A)
_ChassisSlotBootloaderVersion_Type=DisplayString
_ChassisSlotBootloaderVersion_Object=MibTableColumn
chassisSlotBootloaderVersion=_ChassisSlotBootloaderVersion_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,8),_ChassisSlotBootloaderVersion_Type())
chassisSlotBootloaderVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotBootloaderVersion.setStatus(_A)
_ChassisSlotRuntimeVersion_Type=DisplayString
_ChassisSlotRuntimeVersion_Object=MibTableColumn
chassisSlotRuntimeVersion=_ChassisSlotRuntimeVersion_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,9),_ChassisSlotRuntimeVersion_Type())
chassisSlotRuntimeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotRuntimeVersion.setStatus(_A)
_ChassisSlotCPLDVersion_Type=DisplayString
_ChassisSlotCPLDVersion_Object=MibTableColumn
chassisSlotCPLDVersion=_ChassisSlotCPLDVersion_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,10),_ChassisSlotCPLDVersion_Type())
chassisSlotCPLDVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotCPLDVersion.setStatus(_A)
_ChassisSlotFirsMacAddress_Type=MacAddress
_ChassisSlotFirsMacAddress_Object=MibTableColumn
chassisSlotFirsMacAddress=_ChassisSlotFirsMacAddress_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,11),_ChassisSlotFirsMacAddress_Type())
chassisSlotFirsMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotFirsMacAddress.setStatus(_A)
_ChassisSlotNumberOfMacAddress_Type=Integer32
_ChassisSlotNumberOfMacAddress_Object=MibTableColumn
chassisSlotNumberOfMacAddress=_ChassisSlotNumberOfMacAddress_Object((1,3,6,1,4,1,171,10,120,100,1,2,4,1,1,12),_ChassisSlotNumberOfMacAddress_Type())
chassisSlotNumberOfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotNumberOfMacAddress.setStatus(_A)
_ChassisTemperatureInfo_ObjectIdentity=ObjectIdentity
chassisTemperatureInfo=_ChassisTemperatureInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,2,5))
_ChassisTemperatureInfoTable_Object=MibTable
chassisTemperatureInfoTable=_ChassisTemperatureInfoTable_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1))
if mibBuilder.loadTexts:chassisTemperatureInfoTable.setStatus(_A)
_ChassisTemperatureInfoEntry_Object=MibTableRow
chassisTemperatureInfoEntry=_ChassisTemperatureInfoEntry_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1))
chassisTemperatureInfoEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:chassisTemperatureInfoEntry.setStatus(_A)
class _ChassisTemperatureSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ChassisTemperatureSlotIndex_Type.__name__=_C
_ChassisTemperatureSlotIndex_Object=MibTableColumn
chassisTemperatureSlotIndex=_ChassisTemperatureSlotIndex_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,1),_ChassisTemperatureSlotIndex_Type())
chassisTemperatureSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureSlotIndex.setStatus(_A)
_ChassisTemperatureInletCurrent_Type=DisplayString
_ChassisTemperatureInletCurrent_Object=MibTableColumn
chassisTemperatureInletCurrent=_ChassisTemperatureInletCurrent_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,2),_ChassisTemperatureInletCurrent_Type())
chassisTemperatureInletCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureInletCurrent.setStatus(_A)
_ChassisTemperatureInletOverheat_Type=DisplayString
_ChassisTemperatureInletOverheat_Object=MibTableColumn
chassisTemperatureInletOverheat=_ChassisTemperatureInletOverheat_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,3),_ChassisTemperatureInletOverheat_Type())
chassisTemperatureInletOverheat.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureInletOverheat.setStatus(_A)
_ChassisTemperatureInletHeatdown_Type=DisplayString
_ChassisTemperatureInletHeatdown_Object=MibTableColumn
chassisTemperatureInletHeatdown=_ChassisTemperatureInletHeatdown_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,4),_ChassisTemperatureInletHeatdown_Type())
chassisTemperatureInletHeatdown.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureInletHeatdown.setStatus(_A)
_ChassisTemperatureCenterCurrent_Type=DisplayString
_ChassisTemperatureCenterCurrent_Object=MibTableColumn
chassisTemperatureCenterCurrent=_ChassisTemperatureCenterCurrent_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,5),_ChassisTemperatureCenterCurrent_Type())
chassisTemperatureCenterCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureCenterCurrent.setStatus(_A)
_ChassisTemperatureCenterOverheat_Type=DisplayString
_ChassisTemperatureCenterOverheat_Object=MibTableColumn
chassisTemperatureCenterOverheat=_ChassisTemperatureCenterOverheat_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,6),_ChassisTemperatureCenterOverheat_Type())
chassisTemperatureCenterOverheat.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureCenterOverheat.setStatus(_A)
_ChassisTemperatureCenterHeatdown_Type=DisplayString
_ChassisTemperatureCenterHeatdown_Object=MibTableColumn
chassisTemperatureCenterHeatdown=_ChassisTemperatureCenterHeatdown_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,7),_ChassisTemperatureCenterHeatdown_Type())
chassisTemperatureCenterHeatdown.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureCenterHeatdown.setStatus(_A)
_ChassisTemperatureOutletCurrent_Type=DisplayString
_ChassisTemperatureOutletCurrent_Object=MibTableColumn
chassisTemperatureOutletCurrent=_ChassisTemperatureOutletCurrent_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,8),_ChassisTemperatureOutletCurrent_Type())
chassisTemperatureOutletCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureOutletCurrent.setStatus(_A)
_ChassisTemperatureOutletOverheat_Type=DisplayString
_ChassisTemperatureOutletOverheat_Object=MibTableColumn
chassisTemperatureOutletOverheat=_ChassisTemperatureOutletOverheat_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,9),_ChassisTemperatureOutletOverheat_Type())
chassisTemperatureOutletOverheat.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureOutletOverheat.setStatus(_A)
_ChassisTemperatureOutletHeatdown_Type=DisplayString
_ChassisTemperatureOutletHeatdown_Object=MibTableColumn
chassisTemperatureOutletHeatdown=_ChassisTemperatureOutletHeatdown_Object((1,3,6,1,4,1,171,10,120,100,1,2,5,1,1,10),_ChassisTemperatureOutletHeatdown_Type())
chassisTemperatureOutletHeatdown.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisTemperatureOutletHeatdown.setStatus(_A)
_ChassisPortLEDInfo_ObjectIdentity=ObjectIdentity
chassisPortLEDInfo=_ChassisPortLEDInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,2,6))
_ChassisPortLEDInfoTable_Object=MibTable
chassisPortLEDInfoTable=_ChassisPortLEDInfoTable_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1))
if mibBuilder.loadTexts:chassisPortLEDInfoTable.setStatus(_A)
_ChassisPortLEDInfoEntry_Object=MibTableRow
chassisPortLEDInfoEntry=_ChassisPortLEDInfoEntry_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1,1))
chassisPortLEDInfoEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:chassisPortLEDInfoEntry.setStatus(_A)
_ChassisPortLEDIFIndex_Type=Integer32
_ChassisPortLEDIFIndex_Object=MibTableColumn
chassisPortLEDIFIndex=_ChassisPortLEDIFIndex_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1,1,1),_ChassisPortLEDIFIndex_Type())
chassisPortLEDIFIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPortLEDIFIndex.setStatus(_A)
_ChassisPortLEDIFName_Type=DisplayString
_ChassisPortLEDIFName_Object=MibTableColumn
chassisPortLEDIFName=_ChassisPortLEDIFName_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1,1,2),_ChassisPortLEDIFName_Type())
chassisPortLEDIFName.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPortLEDIFName.setStatus(_A)
class _ChassisPortLEDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('steady-amber',2),(_H,3),('blinking-amber',4),(_I,5)))
_ChassisPortLEDStatus_Type.__name__=_C
_ChassisPortLEDStatus_Object=MibTableColumn
chassisPortLEDStatus=_ChassisPortLEDStatus_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1,1,3),_ChassisPortLEDStatus_Type())
chassisPortLEDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPortLEDStatus.setStatus(_A)
class _ChassisPortLEDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('poe',2)))
_ChassisPortLEDMode_Type.__name__=_C
_ChassisPortLEDMode_Object=MibTableColumn
chassisPortLEDMode=_ChassisPortLEDMode_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1,1,4),_ChassisPortLEDMode_Type())
chassisPortLEDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPortLEDMode.setStatus(_A)
class _ChassisPortLEDMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copper',1),('fiber',2)))
_ChassisPortLEDMediumType_Type.__name__=_C
_ChassisPortLEDMediumType_Object=MibTableColumn
chassisPortLEDMediumType=_ChassisPortLEDMediumType_Object((1,3,6,1,4,1,171,10,120,100,1,2,6,1,1,5),_ChassisPortLEDMediumType_Type())
chassisPortLEDMediumType.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisPortLEDMediumType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'dgs6600EquipmentMIB':dgs6600EquipmentMIB,'chassisControlModuleLEDInfo':chassisControlModuleLEDInfo,'chassisControlModuleLEDInfoTable':chassisControlModuleLEDInfoTable,'chassisControlModuleLEDInfoEntry':chassisControlModuleLEDInfoEntry,_G:chassisControlModuleLEDInfoIndex,'chassisControlModuleLEDInfoConsole':chassisControlModuleLEDInfoConsole,'chassisControlModuleLEDInfoMaster':chassisControlModuleLEDInfoMaster,'chassisControlModuleLEDInfoCPUUtilization':chassisControlModuleLEDInfoCPUUtilization,'chassisControlModuleLEDInfoMgmtPortStatus':chassisControlModuleLEDInfoMgmtPortStatus,'chassisControlModuleLEDInfoMgmtPortSpeed':chassisControlModuleLEDInfoMgmtPortSpeed,'chassisPowerInfo':chassisPowerInfo,'chassisPowerInfoTable':chassisPowerInfoTable,'chassisPowerInfoEntry':chassisPowerInfoEntry,_J:chassisPowerIndex,'chassisPowerExist':chassisPowerExist,'chassisPowerType':chassisPowerType,'chassisPowerAlive':chassisPowerAlive,'chassisPowerVoltage':chassisPowerVoltage,'chassisPowerCurrent':chassisPowerCurrent,'chassisPowerPowerWatt':chassisPowerPowerWatt,'chassisPowerFanSpeed':chassisPowerFanSpeed,'chassisFanTrayInfo':chassisFanTrayInfo,'chassisFanTrayInfoState':chassisFanTrayInfoState,'chassisFanInfoTable':chassisFanInfoTable,'chassisFanInfoEntry':chassisFanInfoEntry,_K:chassisFanIndex,'chassisFanStatus':chassisFanStatus,'chassisFanSpeed':chassisFanSpeed,'chassisSlotInfo':chassisSlotInfo,'chassisSlotInfoTable':chassisSlotInfoTable,'chassisSlotInfoEntry':chassisSlotInfoEntry,_L:chassisSlotIndex,'chassisSlotState':chassisSlotState,'chassisSlotLEDPoEModeEnabled':chassisSlotLEDPoEModeEnabled,'chassisSlotModel':chassisSlotModel,'chassisSlotSerialNumber':chassisSlotSerialNumber,'chassisSlotHwVersion':chassisSlotHwVersion,'chassisSlotPCBAVersion':chassisSlotPCBAVersion,'chassisSlotBootloaderVersion':chassisSlotBootloaderVersion,'chassisSlotRuntimeVersion':chassisSlotRuntimeVersion,'chassisSlotCPLDVersion':chassisSlotCPLDVersion,'chassisSlotFirsMacAddress':chassisSlotFirsMacAddress,'chassisSlotNumberOfMacAddress':chassisSlotNumberOfMacAddress,'chassisTemperatureInfo':chassisTemperatureInfo,'chassisTemperatureInfoTable':chassisTemperatureInfoTable,'chassisTemperatureInfoEntry':chassisTemperatureInfoEntry,_M:chassisTemperatureSlotIndex,'chassisTemperatureInletCurrent':chassisTemperatureInletCurrent,'chassisTemperatureInletOverheat':chassisTemperatureInletOverheat,'chassisTemperatureInletHeatdown':chassisTemperatureInletHeatdown,'chassisTemperatureCenterCurrent':chassisTemperatureCenterCurrent,'chassisTemperatureCenterOverheat':chassisTemperatureCenterOverheat,'chassisTemperatureCenterHeatdown':chassisTemperatureCenterHeatdown,'chassisTemperatureOutletCurrent':chassisTemperatureOutletCurrent,'chassisTemperatureOutletOverheat':chassisTemperatureOutletOverheat,'chassisTemperatureOutletHeatdown':chassisTemperatureOutletHeatdown,'chassisPortLEDInfo':chassisPortLEDInfo,'chassisPortLEDInfoTable':chassisPortLEDInfoTable,'chassisPortLEDInfoEntry':chassisPortLEDInfoEntry,_N:chassisPortLEDIFIndex,'chassisPortLEDIFName':chassisPortLEDIFName,'chassisPortLEDStatus':chassisPortLEDStatus,'chassisPortLEDMode':chassisPortLEDMode,'chassisPortLEDMediumType':chassisPortLEDMediumType})