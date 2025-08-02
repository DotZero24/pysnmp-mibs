_h='zhoneTacTestResultsOutput'
_g='zhoneTacTestResultStatus'
_f='zhoneTacTestResultsTimeEnded'
_e='zhoneTacTestResultsTimeStarted'
_d='zhoneTacTestId'
_c='zhoneTacTestMode'
_b='zhoneTacInterfaceIndex'
_a='zhoneCardDiagRowStatus'
_Z='zhoneCardDiagEndTime'
_Y='zhoneCardDiagStartTime'
_X='zhoneCardDiagDetails'
_W='zhoneCardDiagFailCount'
_V='zhoneCardDiagPassCount'
_U='zhoneCardDiagResult'
_T='zhoneCardDiagDuration'
_S='zhoneCardDiagRepetition'
_R='zhoneCardDiagAction'
_Q='zhoneCardDiagType'
_P='zhoneCardDiagNextIndex'
_O='not-accessible'
_N='zhoneCardDiagIndex'
_M='ZhoneDiagAction'
_L='InterfaceIndexOrZero'
_K='zhoneTacIndex'
_J='zhoneSlotIndex'
_I='zhoneShelfIndex'
_H='OctetString'
_G='read-create'
_F='Zhone'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ZHONE-CARD-DIAGNOSTICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
zhoneCard,zhoneModules,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_F,'zhoneCard','zhoneModules',_I,_J)
ZhoneDiagAction,ZhoneDiagResult,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC',_M,'ZhoneDiagResult','ZhoneRowStatus')
zhoneCardDiagnosticsModule=ModuleIdentity((1,3,6,1,4,1,5504,6,11))
if mibBuilder.loadTexts:zhoneCardDiagnosticsModule.setRevisions(('2010-03-05 14:05','2009-05-14 09:39','2009-05-07 22:37','2009-01-12 15:36','2008-10-22 05:28','2006-07-24 11:28','2001-11-14 15:28','2001-08-30 11:21','2001-08-27 18:14','2001-06-28 12:01','2001-06-26 12:40','2000-12-12 16:30','2000-10-19 19:45','2000-10-17 10:32','2000-09-12 11:07'))
_ZhoneCardDiagNextTable_Object=MibTable
zhoneCardDiagNextTable=_ZhoneCardDiagNextTable_Object((1,3,6,1,4,1,5504,3,3,5))
if mibBuilder.loadTexts:zhoneCardDiagNextTable.setStatus(_A)
_ZhoneCardDiagNextEntry_Object=MibTableRow
zhoneCardDiagNextEntry=_ZhoneCardDiagNextEntry_Object((1,3,6,1,4,1,5504,3,3,5,1))
zhoneCardDiagNextEntry.setIndexNames((0,_F,_I),(0,_F,_J))
if mibBuilder.loadTexts:zhoneCardDiagNextEntry.setStatus(_A)
class _ZhoneCardDiagNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZhoneCardDiagNextIndex_Type.__name__=_C
_ZhoneCardDiagNextIndex_Object=MibTableColumn
zhoneCardDiagNextIndex=_ZhoneCardDiagNextIndex_Object((1,3,6,1,4,1,5504,3,3,5,1,1),_ZhoneCardDiagNextIndex_Type())
zhoneCardDiagNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagNextIndex.setStatus(_A)
_ZhoneCardDiagTable_Object=MibTable
zhoneCardDiagTable=_ZhoneCardDiagTable_Object((1,3,6,1,4,1,5504,3,3,6))
if mibBuilder.loadTexts:zhoneCardDiagTable.setStatus(_A)
_ZhoneCardDiagEntry_Object=MibTableRow
zhoneCardDiagEntry=_ZhoneCardDiagEntry_Object((1,3,6,1,4,1,5504,3,3,6,1))
zhoneCardDiagEntry.setIndexNames((0,_F,_I),(0,_F,_J),(0,_B,_N))
if mibBuilder.loadTexts:zhoneCardDiagEntry.setStatus(_A)
class _ZhoneCardDiagIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZhoneCardDiagIndex_Type.__name__=_C
_ZhoneCardDiagIndex_Object=MibTableColumn
zhoneCardDiagIndex=_ZhoneCardDiagIndex_Object((1,3,6,1,4,1,5504,3,3,6,1,1),_ZhoneCardDiagIndex_Type())
zhoneCardDiagIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:zhoneCardDiagIndex.setStatus(_A)
class _ZhoneCardDiagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('selftest',1),('supvBus',2),('cardEEprom',3),('frbus',4),('pcmcia',5),('shelfLamp',6),('realTimeClock',7),('fanTray',8),('shelfMonitor',9),('ioCard',10),('mezzanineCard',11),('backPlane',12),('midPlane',13)))
_ZhoneCardDiagType_Type.__name__=_C
_ZhoneCardDiagType_Object=MibTableColumn
zhoneCardDiagType=_ZhoneCardDiagType_Object((1,3,6,1,4,1,5504,3,3,6,1,2),_ZhoneCardDiagType_Type())
zhoneCardDiagType.setMaxAccess(_G)
if mibBuilder.loadTexts:zhoneCardDiagType.setStatus(_A)
class _ZhoneCardDiagAction_Type(ZhoneDiagAction):defaultValue=1
_ZhoneCardDiagAction_Type.__name__=_M
_ZhoneCardDiagAction_Object=MibTableColumn
zhoneCardDiagAction=_ZhoneCardDiagAction_Object((1,3,6,1,4,1,5504,3,3,6,1,3),_ZhoneCardDiagAction_Type())
zhoneCardDiagAction.setMaxAccess(_G)
if mibBuilder.loadTexts:zhoneCardDiagAction.setStatus(_A)
class _ZhoneCardDiagRepetition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_ZhoneCardDiagRepetition_Type.__name__=_C
_ZhoneCardDiagRepetition_Object=MibTableColumn
zhoneCardDiagRepetition=_ZhoneCardDiagRepetition_Object((1,3,6,1,4,1,5504,3,3,6,1,4),_ZhoneCardDiagRepetition_Type())
zhoneCardDiagRepetition.setMaxAccess(_G)
if mibBuilder.loadTexts:zhoneCardDiagRepetition.setStatus(_A)
class _ZhoneCardDiagDuration_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_ZhoneCardDiagDuration_Type.__name__=_C
_ZhoneCardDiagDuration_Object=MibTableColumn
zhoneCardDiagDuration=_ZhoneCardDiagDuration_Object((1,3,6,1,4,1,5504,3,3,6,1,5),_ZhoneCardDiagDuration_Type())
zhoneCardDiagDuration.setMaxAccess(_G)
if mibBuilder.loadTexts:zhoneCardDiagDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneCardDiagDuration.setUnits('seconds')
_ZhoneCardDiagResult_Type=ZhoneDiagResult
_ZhoneCardDiagResult_Object=MibTableColumn
zhoneCardDiagResult=_ZhoneCardDiagResult_Object((1,3,6,1,4,1,5504,3,3,6,1,6),_ZhoneCardDiagResult_Type())
zhoneCardDiagResult.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagResult.setStatus(_A)
_ZhoneCardDiagPassCount_Type=Counter32
_ZhoneCardDiagPassCount_Object=MibTableColumn
zhoneCardDiagPassCount=_ZhoneCardDiagPassCount_Object((1,3,6,1,4,1,5504,3,3,6,1,7),_ZhoneCardDiagPassCount_Type())
zhoneCardDiagPassCount.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagPassCount.setStatus(_A)
_ZhoneCardDiagFailCount_Type=Counter32
_ZhoneCardDiagFailCount_Object=MibTableColumn
zhoneCardDiagFailCount=_ZhoneCardDiagFailCount_Object((1,3,6,1,4,1,5504,3,3,6,1,8),_ZhoneCardDiagFailCount_Type())
zhoneCardDiagFailCount.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagFailCount.setStatus(_A)
class _ZhoneCardDiagDetails_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZhoneCardDiagDetails_Type.__name__=_H
_ZhoneCardDiagDetails_Object=MibTableColumn
zhoneCardDiagDetails=_ZhoneCardDiagDetails_Object((1,3,6,1,4,1,5504,3,3,6,1,9),_ZhoneCardDiagDetails_Type())
zhoneCardDiagDetails.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagDetails.setStatus(_A)
_ZhoneCardDiagStartTime_Type=DateAndTime
_ZhoneCardDiagStartTime_Object=MibTableColumn
zhoneCardDiagStartTime=_ZhoneCardDiagStartTime_Object((1,3,6,1,4,1,5504,3,3,6,1,10),_ZhoneCardDiagStartTime_Type())
zhoneCardDiagStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagStartTime.setStatus(_A)
_ZhoneCardDiagEndTime_Type=DateAndTime
_ZhoneCardDiagEndTime_Object=MibTableColumn
zhoneCardDiagEndTime=_ZhoneCardDiagEndTime_Object((1,3,6,1,4,1,5504,3,3,6,1,11),_ZhoneCardDiagEndTime_Type())
zhoneCardDiagEndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCardDiagEndTime.setStatus(_A)
_ZhoneCardDiagRowStatus_Type=ZhoneRowStatus
_ZhoneCardDiagRowStatus_Object=MibTableColumn
zhoneCardDiagRowStatus=_ZhoneCardDiagRowStatus_Object((1,3,6,1,4,1,5504,3,3,6,1,12),_ZhoneCardDiagRowStatus_Type())
zhoneCardDiagRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zhoneCardDiagRowStatus.setStatus(_A)
_ZhoneTacTestTable_Object=MibTable
zhoneTacTestTable=_ZhoneTacTestTable_Object((1,3,6,1,4,1,5504,3,3,7))
if mibBuilder.loadTexts:zhoneTacTestTable.setStatus(_A)
_ZhoneTacTestEntry_Object=MibTableRow
zhoneTacTestEntry=_ZhoneTacTestEntry_Object((1,3,6,1,4,1,5504,3,3,7,1))
zhoneTacTestEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zhoneTacTestEntry.setStatus(_A)
class _ZhoneTacIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ZhoneTacIndex_Type.__name__=_C
_ZhoneTacIndex_Object=MibTableColumn
zhoneTacIndex=_ZhoneTacIndex_Object((1,3,6,1,4,1,5504,3,3,7,1,1),_ZhoneTacIndex_Type())
zhoneTacIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:zhoneTacIndex.setStatus(_A)
class _ZhoneTacInterfaceIndex_Type(InterfaceIndexOrZero):defaultValue=0
_ZhoneTacInterfaceIndex_Type.__name__=_L
_ZhoneTacInterfaceIndex_Object=MibTableColumn
zhoneTacInterfaceIndex=_ZhoneTacInterfaceIndex_Object((1,3,6,1,4,1,5504,3,3,7,1,2),_ZhoneTacInterfaceIndex_Type())
zhoneTacInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacInterfaceIndex.setStatus(_A)
class _ZhoneTacTestMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mtacModeBridge',1),('mtacModeLookIn',2),('mtacModeLookOut',3),('mtacModeNone',4)))
_ZhoneTacTestMode_Type.__name__=_C
_ZhoneTacTestMode_Object=MibTableColumn
zhoneTacTestMode=_ZhoneTacTestMode_Object((1,3,6,1,4,1,5504,3,3,7,1,3),_ZhoneTacTestMode_Type())
zhoneTacTestMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestMode.setStatus(_A)
class _ZhoneTacTestId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*(('none',1),('runAllTests',2),('abortTest',3),('calibration',4),('foreignDCVoltage',5),('foreignACVoltage',6),('dcLoopResistance',7),('threeElementInsulationResistance',8),('fiveElementInsulationResistance',9),('threeElementCapacitance',10),('receiverOffHook',11),('distanceToOpen',12),('foreignACCurrents',13),('ringerEquivalencyNumber',14),('dtmfAndPulseDigitMeasurement',15),('noiseMeasurement',16),('signalToNoiseRatio',17),('arbitrarySignalToneMeasurement',18),('toneGeneration',19),('transHybridLoss',20),('drawAndBreakDialTone',21),('inwardCurrent',22),('dcFeedSelf',23),('onAndOffHookSelfTest',24),('ringingSelfTest',25),('ringingMonitor',26),('meteringSelfTest',27),('transmissionSelfTest',28),('dialingSelfTest',29),('howlerTest',30),('fuseTest',31),('readLoopAndBatteryConditions',32)))
_ZhoneTacTestId_Type.__name__=_C
_ZhoneTacTestId_Object=MibTableColumn
zhoneTacTestId=_ZhoneTacTestId_Object((1,3,6,1,4,1,5504,3,3,7,1,4),_ZhoneTacTestId_Type())
zhoneTacTestId.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestId.setStatus(_A)
class _ZhoneTacTestParam1_Type(Integer32):defaultValue=0
_ZhoneTacTestParam1_Type.__name__=_C
_ZhoneTacTestParam1_Object=MibTableColumn
zhoneTacTestParam1=_ZhoneTacTestParam1_Object((1,3,6,1,4,1,5504,3,3,7,1,5),_ZhoneTacTestParam1_Type())
zhoneTacTestParam1.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestParam1.setStatus(_A)
class _ZhoneTacTestParam2_Type(Integer32):defaultValue=0
_ZhoneTacTestParam2_Type.__name__=_C
_ZhoneTacTestParam2_Object=MibTableColumn
zhoneTacTestParam2=_ZhoneTacTestParam2_Object((1,3,6,1,4,1,5504,3,3,7,1,6),_ZhoneTacTestParam2_Type())
zhoneTacTestParam2.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestParam2.setStatus(_A)
class _ZhoneTacTestParam3_Type(Integer32):defaultValue=0
_ZhoneTacTestParam3_Type.__name__=_C
_ZhoneTacTestParam3_Object=MibTableColumn
zhoneTacTestParam3=_ZhoneTacTestParam3_Object((1,3,6,1,4,1,5504,3,3,7,1,7),_ZhoneTacTestParam3_Type())
zhoneTacTestParam3.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestParam3.setStatus(_A)
class _ZhoneTacTestParam4_Type(Integer32):defaultValue=0
_ZhoneTacTestParam4_Type.__name__=_C
_ZhoneTacTestParam4_Object=MibTableColumn
zhoneTacTestParam4=_ZhoneTacTestParam4_Object((1,3,6,1,4,1,5504,3,3,7,1,8),_ZhoneTacTestParam4_Type())
zhoneTacTestParam4.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestParam4.setStatus(_A)
class _ZhoneTacTestParam5_Type(Integer32):defaultValue=0
_ZhoneTacTestParam5_Type.__name__=_C
_ZhoneTacTestParam5_Object=MibTableColumn
zhoneTacTestParam5=_ZhoneTacTestParam5_Object((1,3,6,1,4,1,5504,3,3,7,1,9),_ZhoneTacTestParam5_Type())
zhoneTacTestParam5.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneTacTestParam5.setStatus(_A)
_ZhoneTacTestResultsTable_Object=MibTable
zhoneTacTestResultsTable=_ZhoneTacTestResultsTable_Object((1,3,6,1,4,1,5504,3,3,12))
if mibBuilder.loadTexts:zhoneTacTestResultsTable.setStatus(_A)
_ZhoneTacTestResultsEntry_Object=MibTableRow
zhoneTacTestResultsEntry=_ZhoneTacTestResultsEntry_Object((1,3,6,1,4,1,5504,3,3,12,1))
zhoneTacTestResultsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zhoneTacTestResultsEntry.setStatus(_A)
_ZhoneTacTestResultsTimeStarted_Type=TimeTicks
_ZhoneTacTestResultsTimeStarted_Object=MibTableColumn
zhoneTacTestResultsTimeStarted=_ZhoneTacTestResultsTimeStarted_Object((1,3,6,1,4,1,5504,3,3,12,1,1),_ZhoneTacTestResultsTimeStarted_Type())
zhoneTacTestResultsTimeStarted.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneTacTestResultsTimeStarted.setStatus(_A)
_ZhoneTacTestResultsTimeEnded_Type=TimeTicks
_ZhoneTacTestResultsTimeEnded_Object=MibTableColumn
zhoneTacTestResultsTimeEnded=_ZhoneTacTestResultsTimeEnded_Object((1,3,6,1,4,1,5504,3,3,12,1,2),_ZhoneTacTestResultsTimeEnded_Type())
zhoneTacTestResultsTimeEnded.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneTacTestResultsTimeEnded.setStatus(_A)
class _ZhoneTacTestResultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('testNotStarted',1),('testInProgress',2),('testCompleted',3),('testAborted',4),('testNotSupported',5)))
_ZhoneTacTestResultStatus_Type.__name__=_C
_ZhoneTacTestResultStatus_Object=MibTableColumn
zhoneTacTestResultStatus=_ZhoneTacTestResultStatus_Object((1,3,6,1,4,1,5504,3,3,12,1,3),_ZhoneTacTestResultStatus_Type())
zhoneTacTestResultStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneTacTestResultStatus.setStatus(_A)
class _ZhoneTacTestResultsOutput_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8000))
_ZhoneTacTestResultsOutput_Type.__name__=_H
_ZhoneTacTestResultsOutput_Object=MibTableColumn
zhoneTacTestResultsOutput=_ZhoneTacTestResultsOutput_Object((1,3,6,1,4,1,5504,3,3,12,1,4),_ZhoneTacTestResultsOutput_Type())
zhoneTacTestResultsOutput.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneTacTestResultsOutput.setStatus(_A)
_ZhoneTacTestTraps_ObjectIdentity=ObjectIdentity
zhoneTacTestTraps=_ZhoneTacTestTraps_ObjectIdentity((1,3,6,1,4,1,5504,3,3,13))
if mibBuilder.loadTexts:zhoneTacTestTraps.setStatus(_A)
_ZhoneRingerTraps_ObjectIdentity=ObjectIdentity
zhoneRingerTraps=_ZhoneRingerTraps_ObjectIdentity((1,3,6,1,4,1,5504,3,3,13,0))
if mibBuilder.loadTexts:zhoneRingerTraps.setStatus(_A)
zhoneCardDiagObjects=ObjectGroup((1,3,6,1,4,1,5504,6,11,1))
zhoneCardDiagObjects.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:zhoneCardDiagObjects.setStatus(_A)
zhoneTacTestObjects=ObjectGroup((1,3,6,1,4,1,5504,6,11,2))
zhoneTacTestObjects.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:zhoneTacTestObjects.setStatus(_A)
zhoneRingerStatusAlarm=NotificationType((1,3,6,1,4,1,5504,3,3,13,0,1))
if mibBuilder.loadTexts:zhoneRingerStatusAlarm.setStatus(_A)
zhoneRingerBusFaultAlarm=NotificationType((1,3,6,1,4,1,5504,3,3,13,0,2))
if mibBuilder.loadTexts:zhoneRingerBusFaultAlarm.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhoneCardDiagNextTable':zhoneCardDiagNextTable,'zhoneCardDiagNextEntry':zhoneCardDiagNextEntry,_P:zhoneCardDiagNextIndex,'zhoneCardDiagTable':zhoneCardDiagTable,'zhoneCardDiagEntry':zhoneCardDiagEntry,_N:zhoneCardDiagIndex,_Q:zhoneCardDiagType,_R:zhoneCardDiagAction,_S:zhoneCardDiagRepetition,_T:zhoneCardDiagDuration,_U:zhoneCardDiagResult,_V:zhoneCardDiagPassCount,_W:zhoneCardDiagFailCount,_X:zhoneCardDiagDetails,_Y:zhoneCardDiagStartTime,_Z:zhoneCardDiagEndTime,_a:zhoneCardDiagRowStatus,'zhoneTacTestTable':zhoneTacTestTable,'zhoneTacTestEntry':zhoneTacTestEntry,_K:zhoneTacIndex,_b:zhoneTacInterfaceIndex,_c:zhoneTacTestMode,_d:zhoneTacTestId,'zhoneTacTestParam1':zhoneTacTestParam1,'zhoneTacTestParam2':zhoneTacTestParam2,'zhoneTacTestParam3':zhoneTacTestParam3,'zhoneTacTestParam4':zhoneTacTestParam4,'zhoneTacTestParam5':zhoneTacTestParam5,'zhoneTacTestResultsTable':zhoneTacTestResultsTable,'zhoneTacTestResultsEntry':zhoneTacTestResultsEntry,_e:zhoneTacTestResultsTimeStarted,_f:zhoneTacTestResultsTimeEnded,_g:zhoneTacTestResultStatus,_h:zhoneTacTestResultsOutput,'zhoneTacTestTraps':zhoneTacTestTraps,'zhoneRingerTraps':zhoneRingerTraps,'zhoneRingerStatusAlarm':zhoneRingerStatusAlarm,'zhoneRingerBusFaultAlarm':zhoneRingerBusFaultAlarm,'zhoneCardDiagnosticsModule':zhoneCardDiagnosticsModule,'zhoneCardDiagObjects':zhoneCardDiagObjects,'zhoneTacTestObjects':zhoneTacTestObjects})