_x='tcamStatusIndex'
_w='ioSignalStatusIndex'
_v='cableTestStatusPortIndex'
_u='deviceLedsIndex'
_t='portLedsPortIndex'
_s='dualMedia'
_r='portInfoPortIndex'
_q='slotInfoIndex'
_p='notPresent'
_o='moduleInfoIndex'
_n='notInstalled'
_m='unmanaged'
_l='notApplicable'
_k='fuseFail'
_j='inputLow'
_i='overload'
_h='highTemp'
_g='redundancyFail'
_f='whileRunning'
_e='alarmWhenLow'
_d='alarmWhenHigh'
_c='ioSignalConfigIndex'
_b='cableTestConfigPortIndex'
_a='static'
_Z='terminationHigh'
_Y='terminationLow'
_X='crossPairShort'
_W='samePairShort'
_V='pairOpen'
_U='pairOk'
_T='enabled'
_S='notAvailable'
_R='disabled'
_Q='not-accessible'
_P='G6-HARDWARE-MIB'
_O='noLed'
_N='white'
_M='magenta'
_L='cyan'
_K='orange'
_J='red'
_I='green'
_H='blue'
_G='off'
_F='true'
_E='false'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,31))
_HardwareLedTest_Type=DisplayString
_HardwareLedTest_Object=MibScalar
hardwareLedTest=_HardwareLedTest_Object((1,3,6,1,4,1,3181,10,6,1,31,1),_HardwareLedTest_Type())
hardwareLedTest.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwareLedTest.setStatus(_A)
class _HardwareLedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('dynamic',0),(_a,1),('quiet',2),('dark',3),('lightshow',4)))
_HardwareLedMode_Type.__name__=_B
_HardwareLedMode_Object=MibScalar
hardwareLedMode=_HardwareLedMode_Object((1,3,6,1,4,1,3181,10,6,1,31,2),_HardwareLedMode_Type())
hardwareLedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwareLedMode.setStatus(_A)
class _HardwarePowerSupply1Monitored_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_T,1)))
_HardwarePowerSupply1Monitored_Type.__name__=_B
_HardwarePowerSupply1Monitored_Object=MibScalar
hardwarePowerSupply1Monitored=_HardwarePowerSupply1Monitored_Object((1,3,6,1,4,1,3181,10,6,1,31,3),_HardwarePowerSupply1Monitored_Type())
hardwarePowerSupply1Monitored.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwarePowerSupply1Monitored.setStatus(_A)
class _HardwarePowerSupply2Monitored_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_T,1)))
_HardwarePowerSupply2Monitored_Type.__name__=_B
_HardwarePowerSupply2Monitored_Object=MibScalar
hardwarePowerSupply2Monitored=_HardwarePowerSupply2Monitored_Object((1,3,6,1,4,1,3181,10,6,1,31,4),_HardwarePowerSupply2Monitored_Type())
hardwarePowerSupply2Monitored.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwarePowerSupply2Monitored.setStatus(_A)
class _HardwareFactoryResetButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_T,1)))
_HardwareFactoryResetButton_Type.__name__=_B
_HardwareFactoryResetButton_Object=MibScalar
hardwareFactoryResetButton=_HardwareFactoryResetButton_Object((1,3,6,1,4,1,3181,10,6,1,31,5),_HardwareFactoryResetButton_Type())
hardwareFactoryResetButton.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwareFactoryResetButton.setStatus(_A)
_CableTestConfigTable_Object=MibTable
cableTestConfigTable=_CableTestConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,31,6))
if mibBuilder.loadTexts:cableTestConfigTable.setStatus(_A)
_CableTestConfigEntry_Object=MibTableRow
cableTestConfigEntry=_CableTestConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1))
cableTestConfigEntry.setIndexNames((0,_P,_b))
if mibBuilder.loadTexts:cableTestConfigEntry.setStatus(_A)
class _CableTestConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CableTestConfigPortIndex_Type.__name__=_B
_CableTestConfigPortIndex_Object=MibTableColumn
cableTestConfigPortIndex=_CableTestConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1,1),_CableTestConfigPortIndex_Type())
cableTestConfigPortIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:cableTestConfigPortIndex.setStatus(_A)
class _CableTestConfigEnableAutoCableTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_T,1)))
_CableTestConfigEnableAutoCableTest_Type.__name__=_B
_CableTestConfigEnableAutoCableTest_Object=MibTableColumn
cableTestConfigEnableAutoCableTest=_CableTestConfigEnableAutoCableTest_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1,2),_CableTestConfigEnableAutoCableTest_Type())
cableTestConfigEnableAutoCableTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cableTestConfigEnableAutoCableTest.setStatus(_A)
class _CableTestConfigEventGeneration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('anyChange',1),('connectionsOnly',2)))
_CableTestConfigEventGeneration_Type.__name__=_B
_CableTestConfigEventGeneration_Object=MibTableColumn
cableTestConfigEventGeneration=_CableTestConfigEventGeneration_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1,3),_CableTestConfigEventGeneration_Type())
cableTestConfigEventGeneration.setMaxAccess(_D)
if mibBuilder.loadTexts:cableTestConfigEventGeneration.setStatus(_A)
class _CableTestConfigReflectionThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestConfigReflectionThreshold_Type.__name__=_B
_CableTestConfigReflectionThreshold_Object=MibTableColumn
cableTestConfigReflectionThreshold=_CableTestConfigReflectionThreshold_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1,4),_CableTestConfigReflectionThreshold_Type())
cableTestConfigReflectionThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cableTestConfigReflectionThreshold.setStatus(_A)
class _CableTestConfigReflectionHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestConfigReflectionHysteresis_Type.__name__=_B
_CableTestConfigReflectionHysteresis_Object=MibTableColumn
cableTestConfigReflectionHysteresis=_CableTestConfigReflectionHysteresis_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1,5),_CableTestConfigReflectionHysteresis_Type())
cableTestConfigReflectionHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:cableTestConfigReflectionHysteresis.setStatus(_A)
_CableTestConfigStartTestNow_Type=DisplayString
_CableTestConfigStartTestNow_Object=MibTableColumn
cableTestConfigStartTestNow=_CableTestConfigStartTestNow_Object((1,3,6,1,4,1,3181,10,6,1,31,6,1,6),_CableTestConfigStartTestNow_Type())
cableTestConfigStartTestNow.setMaxAccess(_D)
if mibBuilder.loadTexts:cableTestConfigStartTestNow.setStatus(_A)
_IoSignalConfigTable_Object=MibTable
ioSignalConfigTable=_IoSignalConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,31,7))
if mibBuilder.loadTexts:ioSignalConfigTable.setStatus(_A)
_IoSignalConfigEntry_Object=MibTableRow
ioSignalConfigEntry=_IoSignalConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1))
ioSignalConfigEntry.setIndexNames((0,_P,_c))
if mibBuilder.loadTexts:ioSignalConfigEntry.setStatus(_A)
class _IoSignalConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_IoSignalConfigIndex_Type.__name__=_B
_IoSignalConfigIndex_Object=MibTableColumn
ioSignalConfigIndex=_IoSignalConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,1),_IoSignalConfigIndex_Type())
ioSignalConfigIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:ioSignalConfigIndex.setStatus(_A)
class _IoSignalConfigSignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_a,0),('ledBlink',1),('relayBlink',2)))
_IoSignalConfigSignalMode_Type.__name__=_B
_IoSignalConfigSignalMode_Object=MibTableColumn
ioSignalConfigSignalMode=_IoSignalConfigSignalMode_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,2),_IoSignalConfigSignalMode_Type())
ioSignalConfigSignalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigSignalMode.setStatus(_A)
class _IoSignalConfigInput1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),(_d,1),(_e,2)))
_IoSignalConfigInput1Mode_Type.__name__=_B
_IoSignalConfigInput1Mode_Object=MibTableColumn
ioSignalConfigInput1Mode=_IoSignalConfigInput1Mode_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,3),_IoSignalConfigInput1Mode_Type())
ioSignalConfigInput1Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigInput1Mode.setStatus(_A)
_IoSignalConfigInput1Name_Type=DisplayString
_IoSignalConfigInput1Name_Object=MibTableColumn
ioSignalConfigInput1Name=_IoSignalConfigInput1Name_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,4),_IoSignalConfigInput1Name_Type())
ioSignalConfigInput1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigInput1Name.setStatus(_A)
class _IoSignalConfigInput2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),(_d,1),(_e,2)))
_IoSignalConfigInput2Mode_Type.__name__=_B
_IoSignalConfigInput2Mode_Object=MibTableColumn
ioSignalConfigInput2Mode=_IoSignalConfigInput2Mode_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,5),_IoSignalConfigInput2Mode_Type())
ioSignalConfigInput2Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigInput2Mode.setStatus(_A)
_IoSignalConfigInput2Name_Type=DisplayString
_IoSignalConfigInput2Name_Object=MibTableColumn
ioSignalConfigInput2Name=_IoSignalConfigInput2Name_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,6),_IoSignalConfigInput2Name_Type())
ioSignalConfigInput2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigInput2Name.setStatus(_A)
class _IoSignalConfigOutput1Trigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_R,0),(_f,1),(_g,2),(_h,3),(_G,4),('on',5)))
_IoSignalConfigOutput1Trigger_Type.__name__=_B
_IoSignalConfigOutput1Trigger_Object=MibTableColumn
ioSignalConfigOutput1Trigger=_IoSignalConfigOutput1Trigger_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,7),_IoSignalConfigOutput1Trigger_Type())
ioSignalConfigOutput1Trigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigOutput1Trigger.setStatus(_A)
_IoSignalConfigOutput1Name_Type=DisplayString
_IoSignalConfigOutput1Name_Object=MibTableColumn
ioSignalConfigOutput1Name=_IoSignalConfigOutput1Name_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,8),_IoSignalConfigOutput1Name_Type())
ioSignalConfigOutput1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigOutput1Name.setStatus(_A)
class _IoSignalConfigOutput2Trigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_R,0),(_f,1),(_g,2),(_h,3),(_G,4),('on',5)))
_IoSignalConfigOutput2Trigger_Type.__name__=_B
_IoSignalConfigOutput2Trigger_Object=MibTableColumn
ioSignalConfigOutput2Trigger=_IoSignalConfigOutput2Trigger_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,9),_IoSignalConfigOutput2Trigger_Type())
ioSignalConfigOutput2Trigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigOutput2Trigger.setStatus(_A)
_IoSignalConfigOutput2Name_Type=DisplayString
_IoSignalConfigOutput2Name_Object=MibTableColumn
ioSignalConfigOutput2Name=_IoSignalConfigOutput2Name_Object((1,3,6,1,4,1,3181,10,6,1,31,7,1,10),_IoSignalConfigOutput2Name_Type())
ioSignalConfigOutput2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:ioSignalConfigOutput2Name.setStatus(_A)
class _HardwarePowerSupply1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',0),(_i,1),(_j,2),(_k,3),(_l,4),(_m,5),(_n,6)))
_HardwarePowerSupply1Status_Type.__name__=_B
_HardwarePowerSupply1Status_Object=MibScalar
hardwarePowerSupply1Status=_HardwarePowerSupply1Status_Object((1,3,6,1,4,1,3181,10,6,1,31,100),_HardwarePowerSupply1Status_Type())
hardwarePowerSupply1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwarePowerSupply1Status.setStatus(_A)
class _HardwarePowerSupply2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',0),(_i,1),(_j,2),(_k,3),(_l,4),(_m,5),(_n,6)))
_HardwarePowerSupply2Status_Type.__name__=_B
_HardwarePowerSupply2Status_Object=MibScalar
hardwarePowerSupply2Status=_HardwarePowerSupply2Status_Object((1,3,6,1,4,1,3181,10,6,1,31,101),_HardwarePowerSupply2Status_Type())
hardwarePowerSupply2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwarePowerSupply2Status.setStatus(_A)
class _HardwareRunningOnPoe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_HardwareRunningOnPoe_Type.__name__=_B
_HardwareRunningOnPoe_Object=MibScalar
hardwareRunningOnPoe=_HardwareRunningOnPoe_Object((1,3,6,1,4,1,3181,10,6,1,31,102),_HardwareRunningOnPoe_Type())
hardwareRunningOnPoe.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareRunningOnPoe.setStatus(_A)
class _HardwareFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unused',0),('ok',1),('degraded',2),('fail',3),('missing',4)))
_HardwareFanStatus_Type.__name__=_B
_HardwareFanStatus_Object=MibScalar
hardwareFanStatus=_HardwareFanStatus_Object((1,3,6,1,4,1,3181,10,6,1,31,103),_HardwareFanStatus_Type())
hardwareFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareFanStatus.setStatus(_A)
class _HardwareSdCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('empty',0),('inserted',1),('writeProtected',2),('writing',3)))
_HardwareSdCardStatus_Type.__name__=_B
_HardwareSdCardStatus_Object=MibScalar
hardwareSdCardStatus=_HardwareSdCardStatus_Object((1,3,6,1,4,1,3181,10,6,1,31,104),_HardwareSdCardStatus_Type())
hardwareSdCardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareSdCardStatus.setStatus(_A)
class _HardwareNumOfPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HardwareNumOfPorts_Type.__name__=_B
_HardwareNumOfPorts_Object=MibScalar
hardwareNumOfPorts=_HardwareNumOfPorts_Object((1,3,6,1,4,1,3181,10,6,1,31,105),_HardwareNumOfPorts_Type())
hardwareNumOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareNumOfPorts.setStatus(_A)
_HardwareMaskOfExistingPorts_Type=Integer32
_HardwareMaskOfExistingPorts_Object=MibScalar
hardwareMaskOfExistingPorts=_HardwareMaskOfExistingPorts_Object((1,3,6,1,4,1,3181,10,6,1,31,106),_HardwareMaskOfExistingPorts_Type())
hardwareMaskOfExistingPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareMaskOfExistingPorts.setStatus(_A)
_HardwareMaskOfSfpPorts_Type=Integer32
_HardwareMaskOfSfpPorts_Object=MibScalar
hardwareMaskOfSfpPorts=_HardwareMaskOfSfpPorts_Object((1,3,6,1,4,1,3181,10,6,1,31,107),_HardwareMaskOfSfpPorts_Type())
hardwareMaskOfSfpPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareMaskOfSfpPorts.setStatus(_A)
_HardwareMaskOfPoePorts_Type=Integer32
_HardwareMaskOfPoePorts_Object=MibScalar
hardwareMaskOfPoePorts=_HardwareMaskOfPoePorts_Object((1,3,6,1,4,1,3181,10,6,1,31,108),_HardwareMaskOfPoePorts_Type())
hardwareMaskOfPoePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareMaskOfPoePorts.setStatus(_A)
_ModuleInfoTable_Object=MibTable
moduleInfoTable=_ModuleInfoTable_Object((1,3,6,1,4,1,3181,10,6,1,31,109))
if mibBuilder.loadTexts:moduleInfoTable.setStatus(_A)
_ModuleInfoEntry_Object=MibTableRow
moduleInfoEntry=_ModuleInfoEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1))
moduleInfoEntry.setIndexNames((0,_P,_o))
if mibBuilder.loadTexts:moduleInfoEntry.setStatus(_A)
class _ModuleInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ModuleInfoIndex_Type.__name__=_B
_ModuleInfoIndex_Object=MibTableColumn
moduleInfoIndex=_ModuleInfoIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,1),_ModuleInfoIndex_Type())
moduleInfoIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:moduleInfoIndex.setStatus(_A)
class _ModuleInfoUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_p,0),('baseUnit',1),('expansion',2)))
_ModuleInfoUnitType_Type.__name__=_B
_ModuleInfoUnitType_Object=MibTableColumn
moduleInfoUnitType=_ModuleInfoUnitType_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,2),_ModuleInfoUnitType_Type())
moduleInfoUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoUnitType.setStatus(_A)
_ModuleInfoArticleNumber_Type=DisplayString
_ModuleInfoArticleNumber_Object=MibTableColumn
moduleInfoArticleNumber=_ModuleInfoArticleNumber_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,3),_ModuleInfoArticleNumber_Type())
moduleInfoArticleNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoArticleNumber.setStatus(_A)
_ModuleInfoSerialNumber_Type=DisplayString
_ModuleInfoSerialNumber_Object=MibTableColumn
moduleInfoSerialNumber=_ModuleInfoSerialNumber_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,4),_ModuleInfoSerialNumber_Type())
moduleInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoSerialNumber.setStatus(_A)
_ModuleInfoHardwareVersion_Type=DisplayString
_ModuleInfoHardwareVersion_Object=MibTableColumn
moduleInfoHardwareVersion=_ModuleInfoHardwareVersion_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,5),_ModuleInfoHardwareVersion_Type())
moduleInfoHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoHardwareVersion.setStatus(_A)
_ModuleInfoProjectNumber_Type=DisplayString
_ModuleInfoProjectNumber_Object=MibTableColumn
moduleInfoProjectNumber=_ModuleInfoProjectNumber_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,6),_ModuleInfoProjectNumber_Type())
moduleInfoProjectNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoProjectNumber.setStatus(_A)
_ModuleInfoOccupiedSlots_Type=DisplayString
_ModuleInfoOccupiedSlots_Object=MibTableColumn
moduleInfoOccupiedSlots=_ModuleInfoOccupiedSlots_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,7),_ModuleInfoOccupiedSlots_Type())
moduleInfoOccupiedSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoOccupiedSlots.setStatus(_A)
_ModuleInfoDescription_Type=DisplayString
_ModuleInfoDescription_Object=MibTableColumn
moduleInfoDescription=_ModuleInfoDescription_Object((1,3,6,1,4,1,3181,10,6,1,31,109,1,8),_ModuleInfoDescription_Type())
moduleInfoDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleInfoDescription.setStatus(_A)
_SlotInfoTable_Object=MibTable
slotInfoTable=_SlotInfoTable_Object((1,3,6,1,4,1,3181,10,6,1,31,110))
if mibBuilder.loadTexts:slotInfoTable.setStatus(_A)
_SlotInfoEntry_Object=MibTableRow
slotInfoEntry=_SlotInfoEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,110,1))
slotInfoEntry.setIndexNames((0,_P,_q))
if mibBuilder.loadTexts:slotInfoEntry.setStatus(_A)
class _SlotInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SlotInfoIndex_Type.__name__=_B
_SlotInfoIndex_Object=MibTableColumn
slotInfoIndex=_SlotInfoIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,110,1,1),_SlotInfoIndex_Type())
slotInfoIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:slotInfoIndex.setStatus(_A)
class _SlotInfoBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_p,0),('undefined',1),('power',2),('cpu',3),('port',4),('io',5),('ms10gPort',6)))
_SlotInfoBoardType_Type.__name__=_B
_SlotInfoBoardType_Object=MibTableColumn
slotInfoBoardType=_SlotInfoBoardType_Object((1,3,6,1,4,1,3181,10,6,1,31,110,1,2),_SlotInfoBoardType_Type())
slotInfoBoardType.setMaxAccess(_C)
if mibBuilder.loadTexts:slotInfoBoardType.setStatus(_A)
_SlotInfoBoardId_Type=Unsigned32
_SlotInfoBoardId_Object=MibTableColumn
slotInfoBoardId=_SlotInfoBoardId_Object((1,3,6,1,4,1,3181,10,6,1,31,110,1,3),_SlotInfoBoardId_Type())
slotInfoBoardId.setMaxAccess(_C)
if mibBuilder.loadTexts:slotInfoBoardId.setStatus(_A)
class _SlotInfoVersionBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SlotInfoVersionBits_Type.__name__=_B
_SlotInfoVersionBits_Object=MibTableColumn
slotInfoVersionBits=_SlotInfoVersionBits_Object((1,3,6,1,4,1,3181,10,6,1,31,110,1,4),_SlotInfoVersionBits_Type())
slotInfoVersionBits.setMaxAccess(_C)
if mibBuilder.loadTexts:slotInfoVersionBits.setStatus(_A)
_PortInfoTable_Object=MibTable
portInfoTable=_PortInfoTable_Object((1,3,6,1,4,1,3181,10,6,1,31,111))
if mibBuilder.loadTexts:portInfoTable.setStatus(_A)
_PortInfoEntry_Object=MibTableRow
portInfoEntry=_PortInfoEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1))
portInfoEntry.setIndexNames((0,_P,_r))
if mibBuilder.loadTexts:portInfoEntry.setStatus(_A)
class _PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortInfoPortIndex_Type.__name__=_B
_PortInfoPortIndex_Object=MibTableColumn
portInfoPortIndex=_PortInfoPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,1),_PortInfoPortIndex_Type())
portInfoPortIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:portInfoPortIndex.setStatus(_A)
class _PortInfoSystemSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortInfoSystemSlot_Type.__name__=_B
_PortInfoSystemSlot_Object=MibTableColumn
portInfoSystemSlot=_PortInfoSystemSlot_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,2),_PortInfoSystemSlot_Type())
portInfoSystemSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoSystemSlot.setStatus(_A)
class _PortInfoSwitchPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortInfoSwitchPort_Type.__name__=_B
_PortInfoSwitchPort_Object=MibTableColumn
portInfoSwitchPort=_PortInfoSwitchPort_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,3),_PortInfoSwitchPort_Type())
portInfoSwitchPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoSwitchPort.setStatus(_A)
class _PortInfoUserSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortInfoUserSlot_Type.__name__=_B
_PortInfoUserSlot_Object=MibTableColumn
portInfoUserSlot=_PortInfoUserSlot_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,4),_PortInfoUserSlot_Type())
portInfoUserSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoUserSlot.setStatus(_A)
class _PortInfoUserPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortInfoUserPort_Type.__name__=_B
_PortInfoUserPort_Object=MibTableColumn
portInfoUserPort=_PortInfoUserPort_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,5),_PortInfoUserPort_Type())
portInfoUserPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoUserPort.setStatus(_A)
class _PortInfoSnmpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortInfoSnmpPort_Type.__name__=_B
_PortInfoSnmpPort_Object=MibTableColumn
portInfoSnmpPort=_PortInfoSnmpPort_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,6),_PortInfoSnmpPort_Type())
portInfoSnmpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoSnmpPort.setStatus(_A)
class _PortInfoSnmpInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortInfoSnmpInstance_Type.__name__=_B
_PortInfoSnmpInstance_Object=MibTableColumn
portInfoSnmpInstance=_PortInfoSnmpInstance_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,7),_PortInfoSnmpInstance_Type())
portInfoSnmpInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoSnmpInstance.setStatus(_A)
class _PortInfoHardwarePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortInfoHardwarePort_Type.__name__=_B
_PortInfoHardwarePort_Object=MibTableColumn
portInfoHardwarePort=_PortInfoHardwarePort_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,8),_PortInfoHardwarePort_Type())
portInfoHardwarePort.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoHardwarePort.setStatus(_A)
class _PortInfoInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('copper',0),('optical',1),(_s,2)))
_PortInfoInterfaceType_Type.__name__=_B
_PortInfoInterfaceType_Object=MibTableColumn
portInfoInterfaceType=_PortInfoInterfaceType_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,9),_PortInfoInterfaceType_Type())
portInfoInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoInterfaceType.setStatus(_A)
class _PortInfoProperties_Type(Bits):namedValues=NamedValues(*(('internal',0),('ms10Mb',1),('ms100Mb',2),('ms1000Mb',3),('rj45',4),('sfp',5),('ms1x9',6),('poe',7),('poePlus',8),('pd',9),(_s,10),('linkPort',11),('csfp',12)))
_PortInfoProperties_Type.__name__='Bits'
_PortInfoProperties_Object=MibTableColumn
portInfoProperties=_PortInfoProperties_Object((1,3,6,1,4,1,3181,10,6,1,31,111,1,10),_PortInfoProperties_Type())
portInfoProperties.setMaxAccess(_C)
if mibBuilder.loadTexts:portInfoProperties.setStatus(_A)
_PortLedsTable_Object=MibTable
portLedsTable=_PortLedsTable_Object((1,3,6,1,4,1,3181,10,6,1,31,112))
if mibBuilder.loadTexts:portLedsTable.setStatus(_A)
_PortLedsEntry_Object=MibTableRow
portLedsEntry=_PortLedsEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,112,1))
portLedsEntry.setIndexNames((0,_P,_t))
if mibBuilder.loadTexts:portLedsEntry.setStatus(_A)
class _PortLedsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PortLedsPortIndex_Type.__name__=_B
_PortLedsPortIndex_Object=MibTableColumn
portLedsPortIndex=_PortLedsPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,112,1,1),_PortLedsPortIndex_Type())
portLedsPortIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:portLedsPortIndex.setStatus(_A)
class _PortLedsEthernetColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_PortLedsEthernetColor_Type.__name__=_B
_PortLedsEthernetColor_Object=MibTableColumn
portLedsEthernetColor=_PortLedsEthernetColor_Object((1,3,6,1,4,1,3181,10,6,1,31,112,1,2),_PortLedsEthernetColor_Type())
portLedsEthernetColor.setMaxAccess(_C)
if mibBuilder.loadTexts:portLedsEthernetColor.setStatus(_A)
class _PortLedsEthernetBlinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortLedsEthernetBlinking_Type.__name__=_B
_PortLedsEthernetBlinking_Object=MibTableColumn
portLedsEthernetBlinking=_PortLedsEthernetBlinking_Object((1,3,6,1,4,1,3181,10,6,1,31,112,1,3),_PortLedsEthernetBlinking_Type())
portLedsEthernetBlinking.setMaxAccess(_C)
if mibBuilder.loadTexts:portLedsEthernetBlinking.setStatus(_A)
class _PortLedsPoeColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_PortLedsPoeColor_Type.__name__=_B
_PortLedsPoeColor_Object=MibTableColumn
portLedsPoeColor=_PortLedsPoeColor_Object((1,3,6,1,4,1,3181,10,6,1,31,112,1,4),_PortLedsPoeColor_Type())
portLedsPoeColor.setMaxAccess(_C)
if mibBuilder.loadTexts:portLedsPoeColor.setStatus(_A)
class _PortLedsPoeBlinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortLedsPoeBlinking_Type.__name__=_B
_PortLedsPoeBlinking_Object=MibTableColumn
portLedsPoeBlinking=_PortLedsPoeBlinking_Object((1,3,6,1,4,1,3181,10,6,1,31,112,1,5),_PortLedsPoeBlinking_Type())
portLedsPoeBlinking.setMaxAccess(_C)
if mibBuilder.loadTexts:portLedsPoeBlinking.setStatus(_A)
_DeviceLedsTable_Object=MibTable
deviceLedsTable=_DeviceLedsTable_Object((1,3,6,1,4,1,3181,10,6,1,31,113))
if mibBuilder.loadTexts:deviceLedsTable.setStatus(_A)
_DeviceLedsEntry_Object=MibTableRow
deviceLedsEntry=_DeviceLedsEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1))
deviceLedsEntry.setIndexNames((0,_P,_u))
if mibBuilder.loadTexts:deviceLedsEntry.setStatus(_A)
class _DeviceLedsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_DeviceLedsIndex_Type.__name__=_B
_DeviceLedsIndex_Object=MibTableColumn
deviceLedsIndex=_DeviceLedsIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,1),_DeviceLedsIndex_Type())
deviceLedsIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:deviceLedsIndex.setStatus(_A)
class _DeviceLedsSystem1Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsSystem1Color_Type.__name__=_B
_DeviceLedsSystem1Color_Object=MibTableColumn
deviceLedsSystem1Color=_DeviceLedsSystem1Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,2),_DeviceLedsSystem1Color_Type())
deviceLedsSystem1Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSystem1Color.setStatus(_A)
class _DeviceLedsSystem1Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsSystem1Blinking_Type.__name__=_B
_DeviceLedsSystem1Blinking_Object=MibTableColumn
deviceLedsSystem1Blinking=_DeviceLedsSystem1Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,3),_DeviceLedsSystem1Blinking_Type())
deviceLedsSystem1Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSystem1Blinking.setStatus(_A)
class _DeviceLedsSystem2Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsSystem2Color_Type.__name__=_B
_DeviceLedsSystem2Color_Object=MibTableColumn
deviceLedsSystem2Color=_DeviceLedsSystem2Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,4),_DeviceLedsSystem2Color_Type())
deviceLedsSystem2Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSystem2Color.setStatus(_A)
class _DeviceLedsSystem2Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsSystem2Blinking_Type.__name__=_B
_DeviceLedsSystem2Blinking_Object=MibTableColumn
deviceLedsSystem2Blinking=_DeviceLedsSystem2Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,5),_DeviceLedsSystem2Blinking_Type())
deviceLedsSystem2Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSystem2Blinking.setStatus(_A)
class _DeviceLedsPowerOn1Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsPowerOn1Color_Type.__name__=_B
_DeviceLedsPowerOn1Color_Object=MibTableColumn
deviceLedsPowerOn1Color=_DeviceLedsPowerOn1Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,6),_DeviceLedsPowerOn1Color_Type())
deviceLedsPowerOn1Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsPowerOn1Color.setStatus(_A)
class _DeviceLedsPowerOn1Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsPowerOn1Blinking_Type.__name__=_B
_DeviceLedsPowerOn1Blinking_Object=MibTableColumn
deviceLedsPowerOn1Blinking=_DeviceLedsPowerOn1Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,7),_DeviceLedsPowerOn1Blinking_Type())
deviceLedsPowerOn1Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsPowerOn1Blinking.setStatus(_A)
class _DeviceLedsPowerOn2Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsPowerOn2Color_Type.__name__=_B
_DeviceLedsPowerOn2Color_Object=MibTableColumn
deviceLedsPowerOn2Color=_DeviceLedsPowerOn2Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,8),_DeviceLedsPowerOn2Color_Type())
deviceLedsPowerOn2Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsPowerOn2Color.setStatus(_A)
class _DeviceLedsPowerOn2Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsPowerOn2Blinking_Type.__name__=_B
_DeviceLedsPowerOn2Blinking_Object=MibTableColumn
deviceLedsPowerOn2Blinking=_DeviceLedsPowerOn2Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,9),_DeviceLedsPowerOn2Blinking_Type())
deviceLedsPowerOn2Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsPowerOn2Blinking.setStatus(_A)
class _DeviceLedsRing1Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsRing1Color_Type.__name__=_B
_DeviceLedsRing1Color_Object=MibTableColumn
deviceLedsRing1Color=_DeviceLedsRing1Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,10),_DeviceLedsRing1Color_Type())
deviceLedsRing1Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsRing1Color.setStatus(_A)
class _DeviceLedsRing1Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsRing1Blinking_Type.__name__=_B
_DeviceLedsRing1Blinking_Object=MibTableColumn
deviceLedsRing1Blinking=_DeviceLedsRing1Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,11),_DeviceLedsRing1Blinking_Type())
deviceLedsRing1Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsRing1Blinking.setStatus(_A)
class _DeviceLedsRing2Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsRing2Color_Type.__name__=_B
_DeviceLedsRing2Color_Object=MibTableColumn
deviceLedsRing2Color=_DeviceLedsRing2Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,12),_DeviceLedsRing2Color_Type())
deviceLedsRing2Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsRing2Color.setStatus(_A)
class _DeviceLedsRing2Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsRing2Blinking_Type.__name__=_B
_DeviceLedsRing2Blinking_Object=MibTableColumn
deviceLedsRing2Blinking=_DeviceLedsRing2Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,13),_DeviceLedsRing2Blinking_Type())
deviceLedsRing2Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsRing2Blinking.setStatus(_A)
class _DeviceLedsSignalIn1Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsSignalIn1Color_Type.__name__=_B
_DeviceLedsSignalIn1Color_Object=MibTableColumn
deviceLedsSignalIn1Color=_DeviceLedsSignalIn1Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,14),_DeviceLedsSignalIn1Color_Type())
deviceLedsSignalIn1Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalIn1Color.setStatus(_A)
class _DeviceLedsSignalIn1Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsSignalIn1Blinking_Type.__name__=_B
_DeviceLedsSignalIn1Blinking_Object=MibTableColumn
deviceLedsSignalIn1Blinking=_DeviceLedsSignalIn1Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,15),_DeviceLedsSignalIn1Blinking_Type())
deviceLedsSignalIn1Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalIn1Blinking.setStatus(_A)
class _DeviceLedsSignalIn2Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsSignalIn2Color_Type.__name__=_B
_DeviceLedsSignalIn2Color_Object=MibTableColumn
deviceLedsSignalIn2Color=_DeviceLedsSignalIn2Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,16),_DeviceLedsSignalIn2Color_Type())
deviceLedsSignalIn2Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalIn2Color.setStatus(_A)
class _DeviceLedsSignalIn2Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsSignalIn2Blinking_Type.__name__=_B
_DeviceLedsSignalIn2Blinking_Object=MibTableColumn
deviceLedsSignalIn2Blinking=_DeviceLedsSignalIn2Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,17),_DeviceLedsSignalIn2Blinking_Type())
deviceLedsSignalIn2Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalIn2Blinking.setStatus(_A)
class _DeviceLedsSignalOut1Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsSignalOut1Color_Type.__name__=_B
_DeviceLedsSignalOut1Color_Object=MibTableColumn
deviceLedsSignalOut1Color=_DeviceLedsSignalOut1Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,18),_DeviceLedsSignalOut1Color_Type())
deviceLedsSignalOut1Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalOut1Color.setStatus(_A)
class _DeviceLedsSignalOut1Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsSignalOut1Blinking_Type.__name__=_B
_DeviceLedsSignalOut1Blinking_Object=MibTableColumn
deviceLedsSignalOut1Blinking=_DeviceLedsSignalOut1Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,19),_DeviceLedsSignalOut1Blinking_Type())
deviceLedsSignalOut1Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalOut1Blinking.setStatus(_A)
class _DeviceLedsSignalOut2Color_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_DeviceLedsSignalOut2Color_Type.__name__=_B
_DeviceLedsSignalOut2Color_Object=MibTableColumn
deviceLedsSignalOut2Color=_DeviceLedsSignalOut2Color_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,20),_DeviceLedsSignalOut2Color_Type())
deviceLedsSignalOut2Color.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalOut2Color.setStatus(_A)
class _DeviceLedsSignalOut2Blinking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DeviceLedsSignalOut2Blinking_Type.__name__=_B
_DeviceLedsSignalOut2Blinking_Object=MibTableColumn
deviceLedsSignalOut2Blinking=_DeviceLedsSignalOut2Blinking_Object((1,3,6,1,4,1,3181,10,6,1,31,113,1,21),_DeviceLedsSignalOut2Blinking_Type())
deviceLedsSignalOut2Blinking.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceLedsSignalOut2Blinking.setStatus(_A)
_CableTestStatusTable_Object=MibTable
cableTestStatusTable=_CableTestStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,31,114))
if mibBuilder.loadTexts:cableTestStatusTable.setStatus(_A)
_CableTestStatusEntry_Object=MibTableRow
cableTestStatusEntry=_CableTestStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1))
cableTestStatusEntry.setIndexNames((0,_P,_v))
if mibBuilder.loadTexts:cableTestStatusEntry.setStatus(_A)
class _CableTestStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CableTestStatusPortIndex_Type.__name__=_B
_CableTestStatusPortIndex_Object=MibTableColumn
cableTestStatusPortIndex=_CableTestStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,1),_CableTestStatusPortIndex_Type())
cableTestStatusPortIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:cableTestStatusPortIndex.setStatus(_A)
_CableTestStatusUpdateTimeStamp_Type=DisplayString
_CableTestStatusUpdateTimeStamp_Object=MibTableColumn
cableTestStatusUpdateTimeStamp=_CableTestStatusUpdateTimeStamp_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,2),_CableTestStatusUpdateTimeStamp_Type())
cableTestStatusUpdateTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusUpdateTimeStamp.setStatus(_A)
class _CableTestStatusPair0State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),(_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6)))
_CableTestStatusPair0State_Type.__name__=_B
_CableTestStatusPair0State_Object=MibTableColumn
cableTestStatusPair0State=_CableTestStatusPair0State_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,3),_CableTestStatusPair0State_Type())
cableTestStatusPair0State.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair0State.setStatus(_A)
class _CableTestStatusPair0DistanceToFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestStatusPair0DistanceToFault_Type.__name__=_B
_CableTestStatusPair0DistanceToFault_Object=MibTableColumn
cableTestStatusPair0DistanceToFault=_CableTestStatusPair0DistanceToFault_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,4),_CableTestStatusPair0DistanceToFault_Type())
cableTestStatusPair0DistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair0DistanceToFault.setStatus(_A)
class _CableTestStatusPair1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),(_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6)))
_CableTestStatusPair1State_Type.__name__=_B
_CableTestStatusPair1State_Object=MibTableColumn
cableTestStatusPair1State=_CableTestStatusPair1State_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,5),_CableTestStatusPair1State_Type())
cableTestStatusPair1State.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair1State.setStatus(_A)
class _CableTestStatusPair1DistanceToFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestStatusPair1DistanceToFault_Type.__name__=_B
_CableTestStatusPair1DistanceToFault_Object=MibTableColumn
cableTestStatusPair1DistanceToFault=_CableTestStatusPair1DistanceToFault_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,6),_CableTestStatusPair1DistanceToFault_Type())
cableTestStatusPair1DistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair1DistanceToFault.setStatus(_A)
class _CableTestStatusPair2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),(_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6)))
_CableTestStatusPair2State_Type.__name__=_B
_CableTestStatusPair2State_Object=MibTableColumn
cableTestStatusPair2State=_CableTestStatusPair2State_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,7),_CableTestStatusPair2State_Type())
cableTestStatusPair2State.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair2State.setStatus(_A)
class _CableTestStatusPair2DistanceToFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestStatusPair2DistanceToFault_Type.__name__=_B
_CableTestStatusPair2DistanceToFault_Object=MibTableColumn
cableTestStatusPair2DistanceToFault=_CableTestStatusPair2DistanceToFault_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,8),_CableTestStatusPair2DistanceToFault_Type())
cableTestStatusPair2DistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair2DistanceToFault.setStatus(_A)
class _CableTestStatusPair3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),(_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6)))
_CableTestStatusPair3State_Type.__name__=_B
_CableTestStatusPair3State_Object=MibTableColumn
cableTestStatusPair3State=_CableTestStatusPair3State_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,9),_CableTestStatusPair3State_Type())
cableTestStatusPair3State.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair3State.setStatus(_A)
class _CableTestStatusPair3DistanceToFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestStatusPair3DistanceToFault_Type.__name__=_B
_CableTestStatusPair3DistanceToFault_Object=MibTableColumn
cableTestStatusPair3DistanceToFault=_CableTestStatusPair3DistanceToFault_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,10),_CableTestStatusPair3DistanceToFault_Type())
cableTestStatusPair3DistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusPair3DistanceToFault.setStatus(_A)
class _CableTestStatusReflectionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CableTestStatusReflectionValue_Type.__name__=_B
_CableTestStatusReflectionValue_Object=MibTableColumn
cableTestStatusReflectionValue=_CableTestStatusReflectionValue_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,11),_CableTestStatusReflectionValue_Type())
cableTestStatusReflectionValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusReflectionValue.setStatus(_A)
class _CableTestStatusCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),('noCable',1),('pluggedInLocally',2),('pluggedInRemotely',3),('terminatedCable',4),('terminationTooLow',5),('defective',6)))
_CableTestStatusCableStatus_Type.__name__=_B
_CableTestStatusCableStatus_Object=MibTableColumn
cableTestStatusCableStatus=_CableTestStatusCableStatus_Object((1,3,6,1,4,1,3181,10,6,1,31,114,1,12),_CableTestStatusCableStatus_Type())
cableTestStatusCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cableTestStatusCableStatus.setStatus(_A)
_IoSignalStatusTable_Object=MibTable
ioSignalStatusTable=_IoSignalStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,31,115))
if mibBuilder.loadTexts:ioSignalStatusTable.setStatus(_A)
_IoSignalStatusEntry_Object=MibTableRow
ioSignalStatusEntry=_IoSignalStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,115,1))
ioSignalStatusEntry.setIndexNames((0,_P,_w))
if mibBuilder.loadTexts:ioSignalStatusEntry.setStatus(_A)
class _IoSignalStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_IoSignalStatusIndex_Type.__name__=_B
_IoSignalStatusIndex_Object=MibTableColumn
ioSignalStatusIndex=_IoSignalStatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,115,1,1),_IoSignalStatusIndex_Type())
ioSignalStatusIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:ioSignalStatusIndex.setStatus(_A)
class _IoSignalStatusInput1AlarmActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_IoSignalStatusInput1AlarmActive_Type.__name__=_B
_IoSignalStatusInput1AlarmActive_Object=MibTableColumn
ioSignalStatusInput1AlarmActive=_IoSignalStatusInput1AlarmActive_Object((1,3,6,1,4,1,3181,10,6,1,31,115,1,2),_IoSignalStatusInput1AlarmActive_Type())
ioSignalStatusInput1AlarmActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ioSignalStatusInput1AlarmActive.setStatus(_A)
class _IoSignalStatusInput2AlarmActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_IoSignalStatusInput2AlarmActive_Type.__name__=_B
_IoSignalStatusInput2AlarmActive_Object=MibTableColumn
ioSignalStatusInput2AlarmActive=_IoSignalStatusInput2AlarmActive_Object((1,3,6,1,4,1,3181,10,6,1,31,115,1,3),_IoSignalStatusInput2AlarmActive_Type())
ioSignalStatusInput2AlarmActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ioSignalStatusInput2AlarmActive.setStatus(_A)
class _IoSignalStatusOutput1RelayActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_IoSignalStatusOutput1RelayActive_Type.__name__=_B
_IoSignalStatusOutput1RelayActive_Object=MibTableColumn
ioSignalStatusOutput1RelayActive=_IoSignalStatusOutput1RelayActive_Object((1,3,6,1,4,1,3181,10,6,1,31,115,1,4),_IoSignalStatusOutput1RelayActive_Type())
ioSignalStatusOutput1RelayActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ioSignalStatusOutput1RelayActive.setStatus(_A)
class _IoSignalStatusOutput2RelayActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_IoSignalStatusOutput2RelayActive_Type.__name__=_B
_IoSignalStatusOutput2RelayActive_Object=MibTableColumn
ioSignalStatusOutput2RelayActive=_IoSignalStatusOutput2RelayActive_Object((1,3,6,1,4,1,3181,10,6,1,31,115,1,5),_IoSignalStatusOutput2RelayActive_Type())
ioSignalStatusOutput2RelayActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ioSignalStatusOutput2RelayActive.setStatus(_A)
_TcamStatusTable_Object=MibTable
tcamStatusTable=_TcamStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,31,116))
if mibBuilder.loadTexts:tcamStatusTable.setStatus(_A)
_TcamStatusEntry_Object=MibTableRow
tcamStatusEntry=_TcamStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,31,116,1))
tcamStatusEntry.setIndexNames((0,_P,_x))
if mibBuilder.loadTexts:tcamStatusEntry.setStatus(_A)
class _TcamStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TcamStatusIndex_Type.__name__=_B
_TcamStatusIndex_Object=MibTableColumn
tcamStatusIndex=_TcamStatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,31,116,1,1),_TcamStatusIndex_Type())
tcamStatusIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:tcamStatusIndex.setStatus(_A)
_TcamStatusControlFile_Type=DisplayString
_TcamStatusControlFile_Object=MibTableColumn
tcamStatusControlFile=_TcamStatusControlFile_Object((1,3,6,1,4,1,3181,10,6,1,31,116,1,2),_TcamStatusControlFile_Type())
tcamStatusControlFile.setMaxAccess(_C)
if mibBuilder.loadTexts:tcamStatusControlFile.setStatus(_A)
_TcamStatusDescription_Type=DisplayString
_TcamStatusDescription_Object=MibTableColumn
tcamStatusDescription=_TcamStatusDescription_Object((1,3,6,1,4,1,3181,10,6,1,31,116,1,3),_TcamStatusDescription_Type())
tcamStatusDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tcamStatusDescription.setStatus(_A)
mibBuilder.exportSymbols(_P,**{'device':device,'hardware':hardware,'hardwareLedTest':hardwareLedTest,'hardwareLedMode':hardwareLedMode,'hardwarePowerSupply1Monitored':hardwarePowerSupply1Monitored,'hardwarePowerSupply2Monitored':hardwarePowerSupply2Monitored,'hardwareFactoryResetButton':hardwareFactoryResetButton,'cableTestConfigTable':cableTestConfigTable,'cableTestConfigEntry':cableTestConfigEntry,_b:cableTestConfigPortIndex,'cableTestConfigEnableAutoCableTest':cableTestConfigEnableAutoCableTest,'cableTestConfigEventGeneration':cableTestConfigEventGeneration,'cableTestConfigReflectionThreshold':cableTestConfigReflectionThreshold,'cableTestConfigReflectionHysteresis':cableTestConfigReflectionHysteresis,'cableTestConfigStartTestNow':cableTestConfigStartTestNow,'ioSignalConfigTable':ioSignalConfigTable,'ioSignalConfigEntry':ioSignalConfigEntry,_c:ioSignalConfigIndex,'ioSignalConfigSignalMode':ioSignalConfigSignalMode,'ioSignalConfigInput1Mode':ioSignalConfigInput1Mode,'ioSignalConfigInput1Name':ioSignalConfigInput1Name,'ioSignalConfigInput2Mode':ioSignalConfigInput2Mode,'ioSignalConfigInput2Name':ioSignalConfigInput2Name,'ioSignalConfigOutput1Trigger':ioSignalConfigOutput1Trigger,'ioSignalConfigOutput1Name':ioSignalConfigOutput1Name,'ioSignalConfigOutput2Trigger':ioSignalConfigOutput2Trigger,'ioSignalConfigOutput2Name':ioSignalConfigOutput2Name,'hardwarePowerSupply1Status':hardwarePowerSupply1Status,'hardwarePowerSupply2Status':hardwarePowerSupply2Status,'hardwareRunningOnPoe':hardwareRunningOnPoe,'hardwareFanStatus':hardwareFanStatus,'hardwareSdCardStatus':hardwareSdCardStatus,'hardwareNumOfPorts':hardwareNumOfPorts,'hardwareMaskOfExistingPorts':hardwareMaskOfExistingPorts,'hardwareMaskOfSfpPorts':hardwareMaskOfSfpPorts,'hardwareMaskOfPoePorts':hardwareMaskOfPoePorts,'moduleInfoTable':moduleInfoTable,'moduleInfoEntry':moduleInfoEntry,_o:moduleInfoIndex,'moduleInfoUnitType':moduleInfoUnitType,'moduleInfoArticleNumber':moduleInfoArticleNumber,'moduleInfoSerialNumber':moduleInfoSerialNumber,'moduleInfoHardwareVersion':moduleInfoHardwareVersion,'moduleInfoProjectNumber':moduleInfoProjectNumber,'moduleInfoOccupiedSlots':moduleInfoOccupiedSlots,'moduleInfoDescription':moduleInfoDescription,'slotInfoTable':slotInfoTable,'slotInfoEntry':slotInfoEntry,_q:slotInfoIndex,'slotInfoBoardType':slotInfoBoardType,'slotInfoBoardId':slotInfoBoardId,'slotInfoVersionBits':slotInfoVersionBits,'portInfoTable':portInfoTable,'portInfoEntry':portInfoEntry,_r:portInfoPortIndex,'portInfoSystemSlot':portInfoSystemSlot,'portInfoSwitchPort':portInfoSwitchPort,'portInfoUserSlot':portInfoUserSlot,'portInfoUserPort':portInfoUserPort,'portInfoSnmpPort':portInfoSnmpPort,'portInfoSnmpInstance':portInfoSnmpInstance,'portInfoHardwarePort':portInfoHardwarePort,'portInfoInterfaceType':portInfoInterfaceType,'portInfoProperties':portInfoProperties,'portLedsTable':portLedsTable,'portLedsEntry':portLedsEntry,_t:portLedsPortIndex,'portLedsEthernetColor':portLedsEthernetColor,'portLedsEthernetBlinking':portLedsEthernetBlinking,'portLedsPoeColor':portLedsPoeColor,'portLedsPoeBlinking':portLedsPoeBlinking,'deviceLedsTable':deviceLedsTable,'deviceLedsEntry':deviceLedsEntry,_u:deviceLedsIndex,'deviceLedsSystem1Color':deviceLedsSystem1Color,'deviceLedsSystem1Blinking':deviceLedsSystem1Blinking,'deviceLedsSystem2Color':deviceLedsSystem2Color,'deviceLedsSystem2Blinking':deviceLedsSystem2Blinking,'deviceLedsPowerOn1Color':deviceLedsPowerOn1Color,'deviceLedsPowerOn1Blinking':deviceLedsPowerOn1Blinking,'deviceLedsPowerOn2Color':deviceLedsPowerOn2Color,'deviceLedsPowerOn2Blinking':deviceLedsPowerOn2Blinking,'deviceLedsRing1Color':deviceLedsRing1Color,'deviceLedsRing1Blinking':deviceLedsRing1Blinking,'deviceLedsRing2Color':deviceLedsRing2Color,'deviceLedsRing2Blinking':deviceLedsRing2Blinking,'deviceLedsSignalIn1Color':deviceLedsSignalIn1Color,'deviceLedsSignalIn1Blinking':deviceLedsSignalIn1Blinking,'deviceLedsSignalIn2Color':deviceLedsSignalIn2Color,'deviceLedsSignalIn2Blinking':deviceLedsSignalIn2Blinking,'deviceLedsSignalOut1Color':deviceLedsSignalOut1Color,'deviceLedsSignalOut1Blinking':deviceLedsSignalOut1Blinking,'deviceLedsSignalOut2Color':deviceLedsSignalOut2Color,'deviceLedsSignalOut2Blinking':deviceLedsSignalOut2Blinking,'cableTestStatusTable':cableTestStatusTable,'cableTestStatusEntry':cableTestStatusEntry,_v:cableTestStatusPortIndex,'cableTestStatusUpdateTimeStamp':cableTestStatusUpdateTimeStamp,'cableTestStatusPair0State':cableTestStatusPair0State,'cableTestStatusPair0DistanceToFault':cableTestStatusPair0DistanceToFault,'cableTestStatusPair1State':cableTestStatusPair1State,'cableTestStatusPair1DistanceToFault':cableTestStatusPair1DistanceToFault,'cableTestStatusPair2State':cableTestStatusPair2State,'cableTestStatusPair2DistanceToFault':cableTestStatusPair2DistanceToFault,'cableTestStatusPair3State':cableTestStatusPair3State,'cableTestStatusPair3DistanceToFault':cableTestStatusPair3DistanceToFault,'cableTestStatusReflectionValue':cableTestStatusReflectionValue,'cableTestStatusCableStatus':cableTestStatusCableStatus,'ioSignalStatusTable':ioSignalStatusTable,'ioSignalStatusEntry':ioSignalStatusEntry,_w:ioSignalStatusIndex,'ioSignalStatusInput1AlarmActive':ioSignalStatusInput1AlarmActive,'ioSignalStatusInput2AlarmActive':ioSignalStatusInput2AlarmActive,'ioSignalStatusOutput1RelayActive':ioSignalStatusOutput1RelayActive,'ioSignalStatusOutput2RelayActive':ioSignalStatusOutput2RelayActive,'tcamStatusTable':tcamStatusTable,'tcamStatusEntry':tcamStatusEntry,_x:tcamStatusIndex,'tcamStatusControlFile':tcamStatusControlFile,'tcamStatusDescription':tcamStatusDescription})