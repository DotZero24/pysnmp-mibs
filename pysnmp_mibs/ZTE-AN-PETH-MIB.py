_Y='zxAnPethPseVoltageLowerThresh'
_X='zxAnPethPseVoltageUpperThresh'
_W='zxAnPethPsePortOperStatusDetail'
_V='zxAnPethPseSlot'
_U='zxAnPethPseShelf'
_T='zxAnPethPseRack'
_S='0.1Watts'
_R='centigrade'
_Q='zxAnPethPdePortPowerSupplyStatus'
_P='zxAnPethPsePortOperStatus'
_O='zxAnPethPseChipTempAlmThresh'
_N='zxAnPethPseChipTemp'
_M='not-accessible'
_L='DisplayString'
_K='ifIndex'
_J='IF-MIB'
_I='disabled'
_H='enabled'
_G='0.1V'
_F='zxAnPethPseActualVoltage'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ZTE-AN-PETH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention','TruthValue')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnPethMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,300))
_ZxAnPethObjects_ObjectIdentity=ObjectIdentity
zxAnPethObjects=_ZxAnPethObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,300,1))
_ZxAnPethGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnPethGlobalObjects=_ZxAnPethGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,300,1,1))
class _ZxAnPethPsePmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('staticPowerWithPriority',2),('dynamicPowerWithPriority',3),('staticPowerWithoutPriority',4),('dynamicPowerWithoutPriority',5)))
_ZxAnPethPsePmMode_Type.__name__=_C
_ZxAnPethPsePmMode_Object=MibScalar
zxAnPethPsePmMode=_ZxAnPethPsePmMode_Object((1,3,6,1,4,1,3902,1015,300,1,1,1),_ZxAnPethPsePmMode_Type())
zxAnPethPsePmMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPsePmMode.setStatus(_A)
_ZxAnPethPseActualCurrent_Type=Integer32
_ZxAnPethPseActualCurrent_Object=MibScalar
zxAnPethPseActualCurrent=_ZxAnPethPseActualCurrent_Object((1,3,6,1,4,1,3902,1015,300,1,1,2),_ZxAnPethPseActualCurrent_Type())
zxAnPethPseActualCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPseActualCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPseActualCurrent.setUnits('mA')
_ZxAnPethPseActualVoltage_Type=Integer32
_ZxAnPethPseActualVoltage_Object=MibScalar
zxAnPethPseActualVoltage=_ZxAnPethPseActualVoltage_Object((1,3,6,1,4,1,3902,1015,300,1,1,3),_ZxAnPethPseActualVoltage_Type())
zxAnPethPseActualVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPseActualVoltage.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPseActualVoltage.setUnits(_G)
_ZxAnPethPseChipTemp_Type=Integer32
_ZxAnPethPseChipTemp_Object=MibScalar
zxAnPethPseChipTemp=_ZxAnPethPseChipTemp_Object((1,3,6,1,4,1,3902,1015,300,1,1,4),_ZxAnPethPseChipTemp_Type())
zxAnPethPseChipTemp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPseChipTemp.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPseChipTemp.setUnits(_R)
class _ZxAnPethPseChipTempAlmThresh_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,250))
_ZxAnPethPseChipTempAlmThresh_Type.__name__=_C
_ZxAnPethPseChipTempAlmThresh_Object=MibScalar
zxAnPethPseChipTempAlmThresh=_ZxAnPethPseChipTempAlmThresh_Object((1,3,6,1,4,1,3902,1015,300,1,1,5),_ZxAnPethPseChipTempAlmThresh_Type())
zxAnPethPseChipTempAlmThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPseChipTempAlmThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPseChipTempAlmThresh.setUnits(_R)
class _ZxAnPethPseChipTempTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnPethPseChipTempTrapEnable_Type.__name__=_C
_ZxAnPethPseChipTempTrapEnable_Object=MibScalar
zxAnPethPseChipTempTrapEnable=_ZxAnPethPseChipTempTrapEnable_Object((1,3,6,1,4,1,3902,1015,300,1,1,6),_ZxAnPethPseChipTempTrapEnable_Type())
zxAnPethPseChipTempTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPseChipTempTrapEnable.setStatus(_A)
class _ZxAnPethPseOutVoltageUpperThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(440,585))
_ZxAnPethPseOutVoltageUpperThresh_Type.__name__=_C
_ZxAnPethPseOutVoltageUpperThresh_Object=MibScalar
zxAnPethPseOutVoltageUpperThresh=_ZxAnPethPseOutVoltageUpperThresh_Object((1,3,6,1,4,1,3902,1015,300,1,1,7),_ZxAnPethPseOutVoltageUpperThresh_Type())
zxAnPethPseOutVoltageUpperThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPseOutVoltageUpperThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPseOutVoltageUpperThresh.setUnits(_G)
class _ZxAnPethPseOutVoltageLowerThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(440,585))
_ZxAnPethPseOutVoltageLowerThresh_Type.__name__=_C
_ZxAnPethPseOutVoltageLowerThresh_Object=MibScalar
zxAnPethPseOutVoltageLowerThresh=_ZxAnPethPseOutVoltageLowerThresh_Object((1,3,6,1,4,1,3902,1015,300,1,1,8),_ZxAnPethPseOutVoltageLowerThresh_Type())
zxAnPethPseOutVoltageLowerThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPseOutVoltageLowerThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPseOutVoltageLowerThresh.setUnits(_G)
class _ZxAnPethPseFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnPethPseFirmwareVersion_Type.__name__=_L
_ZxAnPethPseFirmwareVersion_Object=MibScalar
zxAnPethPseFirmwareVersion=_ZxAnPethPseFirmwareVersion_Object((1,3,6,1,4,1,3902,1015,300,1,1,9),_ZxAnPethPseFirmwareVersion_Type())
zxAnPethPseFirmwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPseFirmwareVersion.setStatus(_A)
class _ZxAnPethMainPsePowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnPethMainPsePowerLimit_Type.__name__=_C
_ZxAnPethMainPsePowerLimit_Object=MibScalar
zxAnPethMainPsePowerLimit=_ZxAnPethMainPsePowerLimit_Object((1,3,6,1,4,1,3902,1015,300,1,1,10),_ZxAnPethMainPsePowerLimit_Type())
zxAnPethMainPsePowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethMainPsePowerLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethMainPsePowerLimit.setUnits(_S)
class _ZxAnPethMainPsePowerUsageThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnPethMainPsePowerUsageThresh_Type.__name__=_C
_ZxAnPethMainPsePowerUsageThresh_Object=MibScalar
zxAnPethMainPsePowerUsageThresh=_ZxAnPethMainPsePowerUsageThresh_Object((1,3,6,1,4,1,3902,1015,300,1,1,11),_ZxAnPethMainPsePowerUsageThresh_Type())
zxAnPethMainPsePowerUsageThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethMainPsePowerUsageThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethMainPsePowerUsageThresh.setUnits(_S)
_ZxAnPethPsePortTable_Object=MibTable
zxAnPethPsePortTable=_ZxAnPethPsePortTable_Object((1,3,6,1,4,1,3902,1015,300,1,2))
if mibBuilder.loadTexts:zxAnPethPsePortTable.setStatus(_A)
_ZxAnPethPsePortEntry_Object=MibTableRow
zxAnPethPsePortEntry=_ZxAnPethPsePortEntry_Object((1,3,6,1,4,1,3902,1015,300,1,2,1))
zxAnPethPsePortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:zxAnPethPsePortEntry.setStatus(_A)
class _ZxAnPethPsePortForcePowerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnPethPsePortForcePowerEnable_Type.__name__=_C
_ZxAnPethPsePortForcePowerEnable_Object=MibTableColumn
zxAnPethPsePortForcePowerEnable=_ZxAnPethPsePortForcePowerEnable_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,1),_ZxAnPethPsePortForcePowerEnable_Type())
zxAnPethPsePortForcePowerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPsePortForcePowerEnable.setStatus(_A)
_ZxAnPethPsePortActualVoltage_Type=Integer32
_ZxAnPethPsePortActualVoltage_Object=MibTableColumn
zxAnPethPsePortActualVoltage=_ZxAnPethPsePortActualVoltage_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,2),_ZxAnPethPsePortActualVoltage_Type())
zxAnPethPsePortActualVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPsePortActualVoltage.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPsePortActualVoltage.setUnits(_G)
_ZxAnPethPsePortActualCurrent_Type=Integer32
_ZxAnPethPsePortActualCurrent_Object=MibTableColumn
zxAnPethPsePortActualCurrent=_ZxAnPethPsePortActualCurrent_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,3),_ZxAnPethPsePortActualCurrent_Type())
zxAnPethPsePortActualCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPsePortActualCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPsePortActualCurrent.setUnits('mA')
_ZxAnPethPsePortActualPower_Type=Integer32
_ZxAnPethPsePortActualPower_Object=MibTableColumn
zxAnPethPsePortActualPower=_ZxAnPethPsePortActualPower_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,4),_ZxAnPethPsePortActualPower_Type())
zxAnPethPsePortActualPower.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPsePortActualPower.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPsePortActualPower.setUnits('0.1W')
class _ZxAnPethPsePortMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_ZxAnPethPsePortMaxPower_Type.__name__=_C
_ZxAnPethPsePortMaxPower_Object=MibTableColumn
zxAnPethPsePortMaxPower=_ZxAnPethPsePortMaxPower_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,5),_ZxAnPethPsePortMaxPower_Type())
zxAnPethPsePortMaxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPsePortMaxPower.setStatus(_A)
if mibBuilder.loadTexts:zxAnPethPsePortMaxPower.setUnits('0.1W')
class _ZxAnPethPsePortDetectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noDetection',1),('legacyOnly',2),('fourPointOnly',3),('fourPointLegacy',4),('twoPointOnly',5),('twoPointLegacy',6)))
_ZxAnPethPsePortDetectionType_Type.__name__=_C
_ZxAnPethPsePortDetectionType_Object=MibTableColumn
zxAnPethPsePortDetectionType=_ZxAnPethPsePortDetectionType_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,6),_ZxAnPethPsePortDetectionType_Type())
zxAnPethPsePortDetectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPsePortDetectionType.setStatus(_A)
class _ZxAnPethPsePortWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee8023af',1),('ieee8023at',2)))
_ZxAnPethPsePortWorkMode_Type.__name__=_C
_ZxAnPethPsePortWorkMode_Object=MibTableColumn
zxAnPethPsePortWorkMode=_ZxAnPethPsePortWorkMode_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,7),_ZxAnPethPsePortWorkMode_Type())
zxAnPethPsePortWorkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPsePortWorkMode.setStatus(_A)
class _ZxAnPethPsePortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_ZxAnPethPsePortReset_Type.__name__=_C
_ZxAnPethPsePortReset_Object=MibTableColumn
zxAnPethPsePortReset=_ZxAnPethPsePortReset_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,8),_ZxAnPethPsePortReset_Type())
zxAnPethPsePortReset.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPsePortReset.setStatus(_A)
class _ZxAnPethPsePortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ZxAnPethPsePortOperStatus_Type.__name__=_C
_ZxAnPethPsePortOperStatus_Object=MibTableColumn
zxAnPethPsePortOperStatus=_ZxAnPethPsePortOperStatus_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,9),_ZxAnPethPsePortOperStatus_Type())
zxAnPethPsePortOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPsePortOperStatus.setStatus(_A)
class _ZxAnPethPsePortDetailInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnPethPsePortDetailInfo_Type.__name__=_L
_ZxAnPethPsePortDetailInfo_Object=MibTableColumn
zxAnPethPsePortDetailInfo=_ZxAnPethPsePortDetailInfo_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,10),_ZxAnPethPsePortDetailInfo_Type())
zxAnPethPsePortDetailInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPsePortDetailInfo.setStatus(_A)
class _ZxAnPethPsePortTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnPethPsePortTrapEnable_Type.__name__=_C
_ZxAnPethPsePortTrapEnable_Object=MibTableColumn
zxAnPethPsePortTrapEnable=_ZxAnPethPsePortTrapEnable_Object((1,3,6,1,4,1,3902,1015,300,1,2,1,11),_ZxAnPethPsePortTrapEnable_Type())
zxAnPethPsePortTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPsePortTrapEnable.setStatus(_A)
_ZxAnPethPseCardTable_Object=MibTable
zxAnPethPseCardTable=_ZxAnPethPseCardTable_Object((1,3,6,1,4,1,3902,1015,300,1,3))
if mibBuilder.loadTexts:zxAnPethPseCardTable.setStatus(_A)
_ZxAnPethPseCardEntry_Object=MibTableRow
zxAnPethPseCardEntry=_ZxAnPethPseCardEntry_Object((1,3,6,1,4,1,3902,1015,300,1,3,1))
zxAnPethPseCardEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:zxAnPethPseCardEntry.setStatus(_A)
_ZxAnPethPseRack_Type=Integer32
_ZxAnPethPseRack_Object=MibTableColumn
zxAnPethPseRack=_ZxAnPethPseRack_Object((1,3,6,1,4,1,3902,1015,300,1,3,1,1),_ZxAnPethPseRack_Type())
zxAnPethPseRack.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnPethPseRack.setStatus(_A)
_ZxAnPethPseShelf_Type=Integer32
_ZxAnPethPseShelf_Object=MibTableColumn
zxAnPethPseShelf=_ZxAnPethPseShelf_Object((1,3,6,1,4,1,3902,1015,300,1,3,1,2),_ZxAnPethPseShelf_Type())
zxAnPethPseShelf.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnPethPseShelf.setStatus(_A)
_ZxAnPethPseSlot_Type=Integer32
_ZxAnPethPseSlot_Object=MibTableColumn
zxAnPethPseSlot=_ZxAnPethPseSlot_Object((1,3,6,1,4,1,3902,1015,300,1,3,1,3),_ZxAnPethPseSlot_Type())
zxAnPethPseSlot.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnPethPseSlot.setStatus(_A)
_ZxAnPethPseCardSupportPoe_Type=TruthValue
_ZxAnPethPseCardSupportPoe_Object=MibTableColumn
zxAnPethPseCardSupportPoe=_ZxAnPethPseCardSupportPoe_Object((1,3,6,1,4,1,3902,1015,300,1,3,1,4),_ZxAnPethPseCardSupportPoe_Type())
zxAnPethPseCardSupportPoe.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPseCardSupportPoe.setStatus(_A)
_ZxAnPethPdePortTable_Object=MibTable
zxAnPethPdePortTable=_ZxAnPethPdePortTable_Object((1,3,6,1,4,1,3902,1015,300,1,4))
if mibBuilder.loadTexts:zxAnPethPdePortTable.setStatus(_A)
_ZxAnPethPdePortEntry_Object=MibTableRow
zxAnPethPdePortEntry=_ZxAnPethPdePortEntry_Object((1,3,6,1,4,1,3902,1015,300,1,4,1))
zxAnPethPdePortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:zxAnPethPdePortEntry.setStatus(_A)
class _ZxAnPethPdePortAutoCheckEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnPethPdePortAutoCheckEnable_Type.__name__=_C
_ZxAnPethPdePortAutoCheckEnable_Object=MibTableColumn
zxAnPethPdePortAutoCheckEnable=_ZxAnPethPdePortAutoCheckEnable_Object((1,3,6,1,4,1,3902,1015,300,1,4,1,1),_ZxAnPethPdePortAutoCheckEnable_Type())
zxAnPethPdePortAutoCheckEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPethPdePortAutoCheckEnable.setStatus(_A)
class _ZxAnPethPdePortPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('on',2),('off',3)))
_ZxAnPethPdePortPowerSupplyStatus_Type.__name__=_C
_ZxAnPethPdePortPowerSupplyStatus_Object=MibTableColumn
zxAnPethPdePortPowerSupplyStatus=_ZxAnPethPdePortPowerSupplyStatus_Object((1,3,6,1,4,1,3902,1015,300,1,4,1,2),_ZxAnPethPdePortPowerSupplyStatus_Type())
zxAnPethPdePortPowerSupplyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPethPdePortPowerSupplyStatus.setStatus(_A)
_ZxAnPethTrapObjects_ObjectIdentity=ObjectIdentity
zxAnPethTrapObjects=_ZxAnPethTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,300,2))
zxAnPethPseChipHighTempAlm=NotificationType((1,3,6,1,4,1,3902,1015,300,2,1))
zxAnPethPseChipHighTempAlm.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:zxAnPethPseChipHighTempAlm.setStatus(_A)
zxAnPethPseChipHighTempClr=NotificationType((1,3,6,1,4,1,3902,1015,300,2,2))
zxAnPethPseChipHighTempClr.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:zxAnPethPseChipHighTempClr.setStatus(_A)
zxAnPethPsePortStatusUp=NotificationType((1,3,6,1,4,1,3902,1015,300,2,3))
zxAnPethPsePortStatusUp.setObjects(*((_B,_P),(_B,_W)))
if mibBuilder.loadTexts:zxAnPethPsePortStatusUp.setStatus(_A)
zxAnPethPsePortStatusDown=NotificationType((1,3,6,1,4,1,3902,1015,300,2,4))
zxAnPethPsePortStatusDown.setObjects(*((_B,_P),(_B,_W)))
if mibBuilder.loadTexts:zxAnPethPsePortStatusDown.setStatus(_A)
zxAnPethPseOverVoltageAlm=NotificationType((1,3,6,1,4,1,3902,1015,300,2,5))
zxAnPethPseOverVoltageAlm.setObjects(*((_B,_F),(_B,_X)))
if mibBuilder.loadTexts:zxAnPethPseOverVoltageAlm.setStatus(_A)
zxAnPethPseOverVoltageClr=NotificationType((1,3,6,1,4,1,3902,1015,300,2,6))
zxAnPethPseOverVoltageClr.setObjects(*((_B,_F),(_B,_X)))
if mibBuilder.loadTexts:zxAnPethPseOverVoltageClr.setStatus(_A)
zxAnPethPseUnderVoltageAlm=NotificationType((1,3,6,1,4,1,3902,1015,300,2,7))
zxAnPethPseUnderVoltageAlm.setObjects(*((_B,_F),(_B,_Y)))
if mibBuilder.loadTexts:zxAnPethPseUnderVoltageAlm.setStatus(_A)
zxAnPethPseUnderVoltageClr=NotificationType((1,3,6,1,4,1,3902,1015,300,2,8))
zxAnPethPseUnderVoltageClr.setObjects(*((_B,_F),(_B,_Y)))
if mibBuilder.loadTexts:zxAnPethPseUnderVoltageClr.setStatus(_A)
zxAnPethPdePortPowerOffAlm=NotificationType((1,3,6,1,4,1,3902,1015,300,2,9))
zxAnPethPdePortPowerOffAlm.setObjects((_B,_Q))
if mibBuilder.loadTexts:zxAnPethPdePortPowerOffAlm.setStatus(_A)
zxAnPethPdePortPowerOffClr=NotificationType((1,3,6,1,4,1,3902,1015,300,2,10))
zxAnPethPdePortPowerOffClr.setObjects((_B,_Q))
if mibBuilder.loadTexts:zxAnPethPdePortPowerOffClr.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnPethMib':zxAnPethMib,'zxAnPethObjects':zxAnPethObjects,'zxAnPethGlobalObjects':zxAnPethGlobalObjects,'zxAnPethPsePmMode':zxAnPethPsePmMode,'zxAnPethPseActualCurrent':zxAnPethPseActualCurrent,_F:zxAnPethPseActualVoltage,_N:zxAnPethPseChipTemp,_O:zxAnPethPseChipTempAlmThresh,'zxAnPethPseChipTempTrapEnable':zxAnPethPseChipTempTrapEnable,'zxAnPethPseOutVoltageUpperThresh':zxAnPethPseOutVoltageUpperThresh,'zxAnPethPseOutVoltageLowerThresh':zxAnPethPseOutVoltageLowerThresh,'zxAnPethPseFirmwareVersion':zxAnPethPseFirmwareVersion,'zxAnPethMainPsePowerLimit':zxAnPethMainPsePowerLimit,'zxAnPethMainPsePowerUsageThresh':zxAnPethMainPsePowerUsageThresh,'zxAnPethPsePortTable':zxAnPethPsePortTable,'zxAnPethPsePortEntry':zxAnPethPsePortEntry,'zxAnPethPsePortForcePowerEnable':zxAnPethPsePortForcePowerEnable,'zxAnPethPsePortActualVoltage':zxAnPethPsePortActualVoltage,'zxAnPethPsePortActualCurrent':zxAnPethPsePortActualCurrent,'zxAnPethPsePortActualPower':zxAnPethPsePortActualPower,'zxAnPethPsePortMaxPower':zxAnPethPsePortMaxPower,'zxAnPethPsePortDetectionType':zxAnPethPsePortDetectionType,'zxAnPethPsePortWorkMode':zxAnPethPsePortWorkMode,'zxAnPethPsePortReset':zxAnPethPsePortReset,_P:zxAnPethPsePortOperStatus,'zxAnPethPsePortDetailInfo':zxAnPethPsePortDetailInfo,'zxAnPethPsePortTrapEnable':zxAnPethPsePortTrapEnable,'zxAnPethPseCardTable':zxAnPethPseCardTable,'zxAnPethPseCardEntry':zxAnPethPseCardEntry,_T:zxAnPethPseRack,_U:zxAnPethPseShelf,_V:zxAnPethPseSlot,'zxAnPethPseCardSupportPoe':zxAnPethPseCardSupportPoe,'zxAnPethPdePortTable':zxAnPethPdePortTable,'zxAnPethPdePortEntry':zxAnPethPdePortEntry,'zxAnPethPdePortAutoCheckEnable':zxAnPethPdePortAutoCheckEnable,_Q:zxAnPethPdePortPowerSupplyStatus,'zxAnPethTrapObjects':zxAnPethTrapObjects,'zxAnPethPseChipHighTempAlm':zxAnPethPseChipHighTempAlm,'zxAnPethPseChipHighTempClr':zxAnPethPseChipHighTempClr,'zxAnPethPsePortStatusUp':zxAnPethPsePortStatusUp,'zxAnPethPsePortStatusDown':zxAnPethPsePortStatusDown,'zxAnPethPseOverVoltageAlm':zxAnPethPseOverVoltageAlm,'zxAnPethPseOverVoltageClr':zxAnPethPseOverVoltageClr,'zxAnPethPseUnderVoltageAlm':zxAnPethPseUnderVoltageAlm,'zxAnPethPseUnderVoltageClr':zxAnPethPseUnderVoltageClr,'zxAnPethPdePortPowerOffAlm':zxAnPethPdePortPowerOffAlm,'zxAnPethPdePortPowerOffClr':zxAnPethPdePortPowerOffClr})