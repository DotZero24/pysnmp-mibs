_Y='upsEstimatedMinutesRemaining'
_X='upsIdentAttachedDevices'
_W='noTestsInitiated'
_V='upsAlarmId'
_U='upsAlarmTestInProgress'
_T='upsAlarmShutdownImminent'
_S='upsAlarmShutdownPending'
_R='upsAlarmCommunicationsLost'
_Q='upsAlarmDiagnosticTestFailed'
_P='upsAlarmOutputOffAsRequested'
_O='upsAlarmOutputOverload'
_N='upsAlarmTempBad'
_M='upsAlarmDepletedBattery'
_L='upsAlarmLowBattery'
_K='upsAlarmOnBattery'
_J='upsAlarmBatteryBad'
_I='upsOutputLineIndex'
_H='upsInputLineIndex'
_G='NotificationType'
_F='TRIPPUPS1-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Tripplite_ObjectIdentity=ObjectIdentity
tripplite=_Tripplite_ObjectIdentity((1,3,6,1,4,1,850))
_TrippUPS1_ObjectIdentity=ObjectIdentity
trippUPS1=_TrippUPS1_ObjectIdentity((1,3,6,1,4,1,850,1))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,850,1,1))
_UpsIdent_ObjectIdentity=ObjectIdentity
upsIdent=_UpsIdent_ObjectIdentity((1,3,6,1,4,1,850,1,1,1))
class _UpsIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsIdentManufacturer_Type.__name__=_E
_UpsIdentManufacturer_Object=MibScalar
upsIdentManufacturer=_UpsIdentManufacturer_Object((1,3,6,1,4,1,850,1,1,1,1),_UpsIdentManufacturer_Type())
upsIdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentManufacturer.setStatus(_A)
class _UpsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentModel_Type.__name__=_E
_UpsIdentModel_Object=MibScalar
upsIdentModel=_UpsIdentModel_Object((1,3,6,1,4,1,850,1,1,1,2),_UpsIdentModel_Type())
upsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentModel.setStatus(_A)
class _UpsIdentUPSSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentUPSSoftwareVersion_Type.__name__=_E
_UpsIdentUPSSoftwareVersion_Object=MibScalar
upsIdentUPSSoftwareVersion=_UpsIdentUPSSoftwareVersion_Object((1,3,6,1,4,1,850,1,1,1,3),_UpsIdentUPSSoftwareVersion_Type())
upsIdentUPSSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentUPSSoftwareVersion.setStatus(_A)
class _UpsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentAgentSoftwareVersion_Type.__name__=_E
_UpsIdentAgentSoftwareVersion_Object=MibScalar
upsIdentAgentSoftwareVersion=_UpsIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,850,1,1,1,4),_UpsIdentAgentSoftwareVersion_Type())
upsIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentAgentSoftwareVersion.setStatus(_A)
class _UpsIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentName_Type.__name__=_E
_UpsIdentName_Object=MibScalar
upsIdentName=_UpsIdentName_Object((1,3,6,1,4,1,850,1,1,1,5),_UpsIdentName_Type())
upsIdentName.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentName.setStatus(_A)
class _UpsIdentAttachedDevices_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentAttachedDevices_Type.__name__=_E
_UpsIdentAttachedDevices_Object=MibScalar
upsIdentAttachedDevices=_UpsIdentAttachedDevices_Object((1,3,6,1,4,1,850,1,1,1,6),_UpsIdentAttachedDevices_Type())
upsIdentAttachedDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentAttachedDevices.setStatus(_A)
_UpsBattery_ObjectIdentity=ObjectIdentity
upsBattery=_UpsBattery_ObjectIdentity((1,3,6,1,4,1,850,1,1,2))
class _UpsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4)))
_UpsBatteryStatus_Type.__name__=_D
_UpsBatteryStatus_Object=MibScalar
upsBatteryStatus=_UpsBatteryStatus_Object((1,3,6,1,4,1,850,1,1,2,1),_UpsBatteryStatus_Type())
upsBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryStatus.setStatus(_A)
_UpsSecondsOnBattery_Type=Integer32
_UpsSecondsOnBattery_Object=MibScalar
upsSecondsOnBattery=_UpsSecondsOnBattery_Object((1,3,6,1,4,1,850,1,1,2,2),_UpsSecondsOnBattery_Type())
upsSecondsOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSecondsOnBattery.setStatus(_A)
_UpsEstimatedMinutesRemaining_Type=Integer32
_UpsEstimatedMinutesRemaining_Object=MibScalar
upsEstimatedMinutesRemaining=_UpsEstimatedMinutesRemaining_Object((1,3,6,1,4,1,850,1,1,2,3),_UpsEstimatedMinutesRemaining_Type())
upsEstimatedMinutesRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEstimatedMinutesRemaining.setStatus(_A)
class _UpsBatteryChargeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UpsBatteryChargeRemaining_Type.__name__=_D
_UpsBatteryChargeRemaining_Object=MibScalar
upsBatteryChargeRemaining=_UpsBatteryChargeRemaining_Object((1,3,6,1,4,1,850,1,1,2,4),_UpsBatteryChargeRemaining_Type())
upsBatteryChargeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryChargeRemaining.setStatus(_A)
_UpsBatteryVoltage_Type=Integer32
_UpsBatteryVoltage_Object=MibScalar
upsBatteryVoltage=_UpsBatteryVoltage_Object((1,3,6,1,4,1,850,1,1,2,5),_UpsBatteryVoltage_Type())
upsBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltage.setStatus(_A)
_UpsBatteryTemperature_Type=Integer32
_UpsBatteryTemperature_Object=MibScalar
upsBatteryTemperature=_UpsBatteryTemperature_Object((1,3,6,1,4,1,850,1,1,2,7),_UpsBatteryTemperature_Type())
upsBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryTemperature.setStatus(_A)
_UpsInput_ObjectIdentity=ObjectIdentity
upsInput=_UpsInput_ObjectIdentity((1,3,6,1,4,1,850,1,1,3))
_UpsInputFrequency_Type=Integer32
_UpsInputFrequency_Object=MibScalar
upsInputFrequency=_UpsInputFrequency_Object((1,3,6,1,4,1,850,1,1,3,1),_UpsInputFrequency_Type())
upsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputFrequency.setStatus(_A)
_UpsInputLineBads_Type=Counter32
_UpsInputLineBads_Object=MibScalar
upsInputLineBads=_UpsInputLineBads_Object((1,3,6,1,4,1,850,1,1,3,2),_UpsInputLineBads_Type())
upsInputLineBads.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputLineBads.setStatus(_A)
_UpsInputNumLines_Type=Integer32
_UpsInputNumLines_Object=MibScalar
upsInputNumLines=_UpsInputNumLines_Object((1,3,6,1,4,1,850,1,1,3,3),_UpsInputNumLines_Type())
upsInputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputNumLines.setStatus(_A)
_UpsInputVolt_Type=Integer32
_UpsInputVolt_Object=MibScalar
upsInputVolt=_UpsInputVolt_Object((1,3,6,1,4,1,850,1,1,3,4),_UpsInputVolt_Type())
upsInputVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVolt.setStatus(_A)
_UpsInputTable_Object=MibTable
upsInputTable=_UpsInputTable_Object((1,3,6,1,4,1,850,1,1,3,5))
if mibBuilder.loadTexts:upsInputTable.setStatus(_A)
_UpsInputEntry_Object=MibTableRow
upsInputEntry=_UpsInputEntry_Object((1,3,6,1,4,1,850,1,1,3,5,1))
upsInputEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:upsInputEntry.setStatus(_A)
_UpsInputLineIndex_Type=Integer32
_UpsInputLineIndex_Object=MibTableColumn
upsInputLineIndex=_UpsInputLineIndex_Object((1,3,6,1,4,1,850,1,1,3,5,1,1),_UpsInputLineIndex_Type())
upsInputLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputLineIndex.setStatus(_A)
_UpsInputVoltage_Type=Integer32
_UpsInputVoltage_Object=MibTableColumn
upsInputVoltage=_UpsInputVoltage_Object((1,3,6,1,4,1,850,1,1,3,5,1,2),_UpsInputVoltage_Type())
upsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltage.setStatus(_A)
_UpsOutput_ObjectIdentity=ObjectIdentity
upsOutput=_UpsOutput_ObjectIdentity((1,3,6,1,4,1,850,1,1,4))
class _UpsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('none',2),('normal',3),('bypass',4),('battery',5),('booster',6),('reducer',7)))
_UpsOutputSource_Type.__name__=_D
_UpsOutputSource_Object=MibScalar
upsOutputSource=_UpsOutputSource_Object((1,3,6,1,4,1,850,1,1,4,1),_UpsOutputSource_Type())
upsOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputSource.setStatus(_A)
_UpsOutputFrequency_Type=Integer32
_UpsOutputFrequency_Object=MibScalar
upsOutputFrequency=_UpsOutputFrequency_Object((1,3,6,1,4,1,850,1,1,4,2),_UpsOutputFrequency_Type())
upsOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputFrequency.setStatus(_A)
_UpsOutputNumLines_Type=Integer32
_UpsOutputNumLines_Object=MibScalar
upsOutputNumLines=_UpsOutputNumLines_Object((1,3,6,1,4,1,850,1,1,4,3),_UpsOutputNumLines_Type())
upsOutputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputNumLines.setStatus(_A)
_UpsOutputPercLoad_Type=Integer32
_UpsOutputPercLoad_Object=MibScalar
upsOutputPercLoad=_UpsOutputPercLoad_Object((1,3,6,1,4,1,850,1,1,4,4),_UpsOutputPercLoad_Type())
upsOutputPercLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPercLoad.setStatus(_A)
_UpsOutputTable_Object=MibTable
upsOutputTable=_UpsOutputTable_Object((1,3,6,1,4,1,850,1,1,4,5))
if mibBuilder.loadTexts:upsOutputTable.setStatus(_A)
_UpsOutputEntry_Object=MibTableRow
upsOutputEntry=_UpsOutputEntry_Object((1,3,6,1,4,1,850,1,1,4,5,1))
upsOutputEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:upsOutputEntry.setStatus(_A)
_UpsOutputLineIndex_Type=Integer32
_UpsOutputLineIndex_Object=MibTableColumn
upsOutputLineIndex=_UpsOutputLineIndex_Object((1,3,6,1,4,1,850,1,1,4,5,1,1),_UpsOutputLineIndex_Type())
upsOutputLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputLineIndex.setStatus(_A)
_UpsOutputVoltage_Type=Integer32
_UpsOutputVoltage_Object=MibTableColumn
upsOutputVoltage=_UpsOutputVoltage_Object((1,3,6,1,4,1,850,1,1,4,5,1,2),_UpsOutputVoltage_Type())
upsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputVoltage.setStatus(_A)
_UpsOutputCurrent_Type=Integer32
_UpsOutputCurrent_Object=MibTableColumn
upsOutputCurrent=_UpsOutputCurrent_Object((1,3,6,1,4,1,850,1,1,4,5,1,3),_UpsOutputCurrent_Type())
upsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputCurrent.setStatus(_A)
_UpsOutputPower_Type=Integer32
_UpsOutputPower_Object=MibTableColumn
upsOutputPower=_UpsOutputPower_Object((1,3,6,1,4,1,850,1,1,4,5,1,4),_UpsOutputPower_Type())
upsOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPower.setStatus(_A)
_UpsOutputPercentLoad_Type=Integer32
_UpsOutputPercentLoad_Object=MibTableColumn
upsOutputPercentLoad=_UpsOutputPercentLoad_Object((1,3,6,1,4,1,850,1,1,4,5,1,5),_UpsOutputPercentLoad_Type())
upsOutputPercentLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPercentLoad.setStatus(_A)
_UpsAlarm_ObjectIdentity=ObjectIdentity
upsAlarm=_UpsAlarm_ObjectIdentity((1,3,6,1,4,1,850,1,1,6))
_UpsAlarmsPresent_Type=Gauge32
_UpsAlarmsPresent_Object=MibScalar
upsAlarmsPresent=_UpsAlarmsPresent_Object((1,3,6,1,4,1,850,1,1,6,1),_UpsAlarmsPresent_Type())
upsAlarmsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmsPresent.setStatus(_A)
class _UpsAlarmID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),('upsAlarmOutputOff',8),(_Q,9),(_R,10),(_S,11),(_T,12),(_U,13)))
_UpsAlarmID_Type.__name__=_D
_UpsAlarmID_Object=MibScalar
upsAlarmID=_UpsAlarmID_Object((1,3,6,1,4,1,850,1,1,6,2),_UpsAlarmID_Type())
upsAlarmID.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmID.setStatus(_A)
class _UpsAlarmDESCR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsAlarmDESCR_Type.__name__=_E
_UpsAlarmDESCR_Object=MibScalar
upsAlarmDESCR=_UpsAlarmDESCR_Object((1,3,6,1,4,1,850,1,1,6,3),_UpsAlarmDESCR_Type())
upsAlarmDESCR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDESCR.setStatus(_A)
_UpsAlarmTable_Object=MibTable
upsAlarmTable=_UpsAlarmTable_Object((1,3,6,1,4,1,850,1,1,6,4))
if mibBuilder.loadTexts:upsAlarmTable.setStatus(_A)
_UpsAlarmEntry_Object=MibTableRow
upsAlarmEntry=_UpsAlarmEntry_Object((1,3,6,1,4,1,850,1,1,6,4,1))
upsAlarmEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:upsAlarmEntry.setStatus(_A)
_UpsAlarmId_Type=Integer32
_UpsAlarmId_Object=MibTableColumn
upsAlarmId=_UpsAlarmId_Object((1,3,6,1,4,1,850,1,1,6,4,1,1),_UpsAlarmId_Type())
upsAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmId.setStatus(_A)
class _UpsAlarmDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsAlarmDescr_Type.__name__=_E
_UpsAlarmDescr_Object=MibTableColumn
upsAlarmDescr=_UpsAlarmDescr_Object((1,3,6,1,4,1,850,1,1,6,4,1,2),_UpsAlarmDescr_Type())
upsAlarmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDescr.setStatus(_A)
_UpsAlarmTime_Type=TimeTicks
_UpsAlarmTime_Object=MibTableColumn
upsAlarmTime=_UpsAlarmTime_Object((1,3,6,1,4,1,850,1,1,6,4,1,3),_UpsAlarmTime_Type())
upsAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTime.setStatus(_A)
_UpsWellKnownAlarms_ObjectIdentity=ObjectIdentity
upsWellKnownAlarms=_UpsWellKnownAlarms_ObjectIdentity((1,3,6,1,4,1,850,1,1,7))
_UpsAlarmBatteryBad_Type=Integer32
_UpsAlarmBatteryBad_Object=MibScalar
upsAlarmBatteryBad=_UpsAlarmBatteryBad_Object((1,3,6,1,4,1,850,1,1,7,1),_UpsAlarmBatteryBad_Type())
upsAlarmBatteryBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryBad.setStatus(_A)
_UpsAlarmOnBattery_Type=Integer32
_UpsAlarmOnBattery_Object=MibScalar
upsAlarmOnBattery=_UpsAlarmOnBattery_Object((1,3,6,1,4,1,850,1,1,7,2),_UpsAlarmOnBattery_Type())
upsAlarmOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOnBattery.setStatus(_A)
_UpsAlarmLowBattery_Type=Integer32
_UpsAlarmLowBattery_Object=MibScalar
upsAlarmLowBattery=_UpsAlarmLowBattery_Object((1,3,6,1,4,1,850,1,1,7,3),_UpsAlarmLowBattery_Type())
upsAlarmLowBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmLowBattery.setStatus(_A)
_UpsAlarmDepletedBattery_Type=Integer32
_UpsAlarmDepletedBattery_Object=MibScalar
upsAlarmDepletedBattery=_UpsAlarmDepletedBattery_Object((1,3,6,1,4,1,850,1,1,7,4),_UpsAlarmDepletedBattery_Type())
upsAlarmDepletedBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDepletedBattery.setStatus(_A)
_UpsAlarmTempBad_Type=Integer32
_UpsAlarmTempBad_Object=MibScalar
upsAlarmTempBad=_UpsAlarmTempBad_Object((1,3,6,1,4,1,850,1,1,7,5),_UpsAlarmTempBad_Type())
upsAlarmTempBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTempBad.setStatus(_A)
_UpsAlarmOutputOverload_Type=Integer32
_UpsAlarmOutputOverload_Object=MibScalar
upsAlarmOutputOverload=_UpsAlarmOutputOverload_Object((1,3,6,1,4,1,850,1,1,7,6),_UpsAlarmOutputOverload_Type())
upsAlarmOutputOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputOverload.setStatus(_A)
_UpsAlarmOutputOffAsRequested_Type=Integer32
_UpsAlarmOutputOffAsRequested_Object=MibScalar
upsAlarmOutputOffAsRequested=_UpsAlarmOutputOffAsRequested_Object((1,3,6,1,4,1,850,1,1,7,7),_UpsAlarmOutputOffAsRequested_Type())
upsAlarmOutputOffAsRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputOffAsRequested.setStatus(_A)
_UpsAlarmUpsOutputOff_Type=Integer32
_UpsAlarmUpsOutputOff_Object=MibScalar
upsAlarmUpsOutputOff=_UpsAlarmUpsOutputOff_Object((1,3,6,1,4,1,850,1,1,7,8),_UpsAlarmUpsOutputOff_Type())
upsAlarmUpsOutputOff.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmUpsOutputOff.setStatus(_A)
_UpsAlarmDiagnosticTestFailed_Type=Integer32
_UpsAlarmDiagnosticTestFailed_Object=MibScalar
upsAlarmDiagnosticTestFailed=_UpsAlarmDiagnosticTestFailed_Object((1,3,6,1,4,1,850,1,1,7,9),_UpsAlarmDiagnosticTestFailed_Type())
upsAlarmDiagnosticTestFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDiagnosticTestFailed.setStatus(_A)
_UpsAlarmCommunicationsLost_Type=Integer32
_UpsAlarmCommunicationsLost_Object=MibScalar
upsAlarmCommunicationsLost=_UpsAlarmCommunicationsLost_Object((1,3,6,1,4,1,850,1,1,7,10),_UpsAlarmCommunicationsLost_Type())
upsAlarmCommunicationsLost.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmCommunicationsLost.setStatus(_A)
_UpsAlarmShutdownPending_Type=Integer32
_UpsAlarmShutdownPending_Object=MibScalar
upsAlarmShutdownPending=_UpsAlarmShutdownPending_Object((1,3,6,1,4,1,850,1,1,7,11),_UpsAlarmShutdownPending_Type())
upsAlarmShutdownPending.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmShutdownPending.setStatus(_A)
_UpsAlarmShutdownImminent_Type=Integer32
_UpsAlarmShutdownImminent_Object=MibScalar
upsAlarmShutdownImminent=_UpsAlarmShutdownImminent_Object((1,3,6,1,4,1,850,1,1,7,12),_UpsAlarmShutdownImminent_Type())
upsAlarmShutdownImminent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmShutdownImminent.setStatus(_A)
_UpsAlarmTestInProgress_Type=Integer32
_UpsAlarmTestInProgress_Object=MibScalar
upsAlarmTestInProgress=_UpsAlarmTestInProgress_Object((1,3,6,1,4,1,850,1,1,7,13),_UpsAlarmTestInProgress_Type())
upsAlarmTestInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTestInProgress.setStatus(_A)
_UpsTest_ObjectIdentity=ObjectIdentity
upsTest=_UpsTest_ObjectIdentity((1,3,6,1,4,1,850,1,1,8))
class _UpsTestId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),('abortTestInProgress',2),('generalSystemsTest',3),('checkBatteryTest',4),('deepBatteryCalibration',5)))
_UpsTestId_Type.__name__=_D
_UpsTestId_Object=MibScalar
upsTestId=_UpsTestId_Object((1,3,6,1,4,1,850,1,1,8,1),_UpsTestId_Type())
upsTestId.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestId.setStatus(_A)
class _UpsTestResultsSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('donePass',1),('doneWarning',2),('doneError',3),('aborted',4),('inProgress',5),(_W,6)))
_UpsTestResultsSummary_Type.__name__=_D
_UpsTestResultsSummary_Object=MibScalar
upsTestResultsSummary=_UpsTestResultsSummary_Object((1,3,6,1,4,1,850,1,1,8,2),_UpsTestResultsSummary_Type())
upsTestResultsSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestResultsSummary.setStatus(_A)
_UpsControl_ObjectIdentity=ObjectIdentity
upsControl=_UpsControl_ObjectIdentity((1,3,6,1,4,1,850,1,1,9))
class _UpsShutdownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('output',1),('system',2)))
_UpsShutdownType_Type.__name__=_D
_UpsShutdownType_Object=MibScalar
upsShutdownType=_UpsShutdownType_Object((1,3,6,1,4,1,850,1,1,9,1),_UpsShutdownType_Type())
upsShutdownType.setMaxAccess(_C)
if mibBuilder.loadTexts:upsShutdownType.setStatus(_A)
class _UpsShutdownAfterDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32767))
_UpsShutdownAfterDelay_Type.__name__=_D
_UpsShutdownAfterDelay_Object=MibScalar
upsShutdownAfterDelay=_UpsShutdownAfterDelay_Object((1,3,6,1,4,1,850,1,1,9,2),_UpsShutdownAfterDelay_Type())
upsShutdownAfterDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:upsShutdownAfterDelay.setStatus(_A)
class _UpsStartupAfterDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32767))
_UpsStartupAfterDelay_Type.__name__=_D
_UpsStartupAfterDelay_Object=MibScalar
upsStartupAfterDelay=_UpsStartupAfterDelay_Object((1,3,6,1,4,1,850,1,1,9,3),_UpsStartupAfterDelay_Type())
upsStartupAfterDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:upsStartupAfterDelay.setStatus(_A)
class _UpsRebootDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_UpsRebootDuration_Type.__name__=_D
_UpsRebootDuration_Object=MibScalar
upsRebootDuration=_UpsRebootDuration_Object((1,3,6,1,4,1,850,1,1,9,4),_UpsRebootDuration_Type())
upsRebootDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:upsRebootDuration.setStatus(_A)
class _UpsAutoRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_UpsAutoRestart_Type.__name__=_D
_UpsAutoRestart_Object=MibScalar
upsAutoRestart=_UpsAutoRestart_Object((1,3,6,1,4,1,850,1,1,9,5),_UpsAutoRestart_Type())
upsAutoRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAutoRestart.setStatus(_A)
_UpsConfig_ObjectIdentity=ObjectIdentity
upsConfig=_UpsConfig_ObjectIdentity((1,3,6,1,4,1,850,1,1,10))
_UpsConfigInputVoltageHigh_Type=Integer32
_UpsConfigInputVoltageHigh_Object=MibScalar
upsConfigInputVoltageHigh=_UpsConfigInputVoltageHigh_Object((1,3,6,1,4,1,850,1,1,10,11),_UpsConfigInputVoltageHigh_Type())
upsConfigInputVoltageHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigInputVoltageHigh.setStatus(_A)
_UpsConfigInputVoltageLow_Type=Integer32
_UpsConfigInputVoltageLow_Object=MibScalar
upsConfigInputVoltageLow=_UpsConfigInputVoltageLow_Object((1,3,6,1,4,1,850,1,1,10,12),_UpsConfigInputVoltageLow_Type())
upsConfigInputVoltageLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigInputVoltageLow.setStatus(_A)
_UpsConfigOutputPercLoadHigh_Type=Integer32
_UpsConfigOutputPercLoadHigh_Object=MibScalar
upsConfigOutputPercLoadHigh=_UpsConfigOutputPercLoadHigh_Object((1,3,6,1,4,1,850,1,1,10,13),_UpsConfigOutputPercLoadHigh_Type())
upsConfigOutputPercLoadHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigOutputPercLoadHigh.setStatus(_A)
_UpsConfigBatteryPercLow_Type=Integer32
_UpsConfigBatteryPercLow_Object=MibScalar
upsConfigBatteryPercLow=_UpsConfigBatteryPercLow_Object((1,3,6,1,4,1,850,1,1,10,14),_UpsConfigBatteryPercLow_Type())
upsConfigBatteryPercLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigBatteryPercLow.setStatus(_A)
_UpsConfigBatteryTemperatureHigh_Type=Integer32
_UpsConfigBatteryTemperatureHigh_Object=MibScalar
upsConfigBatteryTemperatureHigh=_UpsConfigBatteryTemperatureHigh_Object((1,3,6,1,4,1,850,1,1,10,15),_UpsConfigBatteryTemperatureHigh_Type())
upsConfigBatteryTemperatureHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigBatteryTemperatureHigh.setStatus(_A)
upsOnBattery=NotificationType((1,3,6,1,4,1,850,0,5))
upsOnBattery.setObjects(*((_F,_X),(_F,_Y)))
if mibBuilder.loadTexts:upsOnBattery.setStatus('')
powerRestored=NotificationType((1,3,6,1,4,1,850,0,6))
if mibBuilder.loadTexts:powerRestored.setStatus('')
lowBattery=NotificationType((1,3,6,1,4,1,850,0,7))
if mibBuilder.loadTexts:lowBattery.setStatus('')
returnFromLowBattery=NotificationType((1,3,6,1,4,1,850,0,8))
if mibBuilder.loadTexts:returnFromLowBattery.setStatus('')
communicationEstablished=NotificationType((1,3,6,1,4,1,850,0,9))
if mibBuilder.loadTexts:communicationEstablished.setStatus('')
communicationLost=NotificationType((1,3,6,1,4,1,850,0,10))
if mibBuilder.loadTexts:communicationLost.setStatus('')
upsOverload=NotificationType((1,3,6,1,4,1,850,0,11))
if mibBuilder.loadTexts:upsOverload.setStatus('')
upsDiagnosticsFailed=NotificationType((1,3,6,1,4,1,850,0,12))
if mibBuilder.loadTexts:upsDiagnosticsFailed.setStatus('')
upsDiagnosticsPassed=NotificationType((1,3,6,1,4,1,850,0,13))
if mibBuilder.loadTexts:upsDiagnosticsPassed.setStatus('')
utilityVoltageHigh=NotificationType((1,3,6,1,4,1,850,0,14))
if mibBuilder.loadTexts:utilityVoltageHigh.setStatus('')
utilityVoltageLow=NotificationType((1,3,6,1,4,1,850,0,15))
if mibBuilder.loadTexts:utilityVoltageLow.setStatus('')
utilityVoltageReturnToNormal=NotificationType((1,3,6,1,4,1,850,0,16))
if mibBuilder.loadTexts:utilityVoltageReturnToNormal.setStatus('')
batteryTemperatureHigh=NotificationType((1,3,6,1,4,1,850,0,17))
if mibBuilder.loadTexts:batteryTemperatureHigh.setStatus('')
shutdownPending=NotificationType((1,3,6,1,4,1,850,0,18))
if mibBuilder.loadTexts:shutdownPending.setStatus('')
upsSleeping=NotificationType((1,3,6,1,4,1,850,0,19))
if mibBuilder.loadTexts:upsSleeping.setStatus('')
upsWokeup=NotificationType((1,3,6,1,4,1,850,0,20))
if mibBuilder.loadTexts:upsWokeup.setStatus('')
upsBatteryNeedsReplacement=NotificationType((1,3,6,1,4,1,850,0,21))
if mibBuilder.loadTexts:upsBatteryNeedsReplacement.setStatus('')
mibBuilder.exportSymbols(_F,**{'tripplite':tripplite,'upsOnBattery':upsOnBattery,'powerRestored':powerRestored,'lowBattery':lowBattery,'returnFromLowBattery':returnFromLowBattery,'communicationEstablished':communicationEstablished,'communicationLost':communicationLost,'upsOverload':upsOverload,'upsDiagnosticsFailed':upsDiagnosticsFailed,'upsDiagnosticsPassed':upsDiagnosticsPassed,'utilityVoltageHigh':utilityVoltageHigh,'utilityVoltageLow':utilityVoltageLow,'utilityVoltageReturnToNormal':utilityVoltageReturnToNormal,'batteryTemperatureHigh':batteryTemperatureHigh,'shutdownPending':shutdownPending,'upsSleeping':upsSleeping,'upsWokeup':upsWokeup,'upsBatteryNeedsReplacement':upsBatteryNeedsReplacement,'trippUPS1':trippUPS1,'ups':ups,'upsIdent':upsIdent,'upsIdentManufacturer':upsIdentManufacturer,'upsIdentModel':upsIdentModel,'upsIdentUPSSoftwareVersion':upsIdentUPSSoftwareVersion,'upsIdentAgentSoftwareVersion':upsIdentAgentSoftwareVersion,'upsIdentName':upsIdentName,_X:upsIdentAttachedDevices,'upsBattery':upsBattery,'upsBatteryStatus':upsBatteryStatus,'upsSecondsOnBattery':upsSecondsOnBattery,_Y:upsEstimatedMinutesRemaining,'upsBatteryChargeRemaining':upsBatteryChargeRemaining,'upsBatteryVoltage':upsBatteryVoltage,'upsBatteryTemperature':upsBatteryTemperature,'upsInput':upsInput,'upsInputFrequency':upsInputFrequency,'upsInputLineBads':upsInputLineBads,'upsInputNumLines':upsInputNumLines,'upsInputVolt':upsInputVolt,'upsInputTable':upsInputTable,'upsInputEntry':upsInputEntry,_H:upsInputLineIndex,'upsInputVoltage':upsInputVoltage,'upsOutput':upsOutput,'upsOutputSource':upsOutputSource,'upsOutputFrequency':upsOutputFrequency,'upsOutputNumLines':upsOutputNumLines,'upsOutputPercLoad':upsOutputPercLoad,'upsOutputTable':upsOutputTable,'upsOutputEntry':upsOutputEntry,_I:upsOutputLineIndex,'upsOutputVoltage':upsOutputVoltage,'upsOutputCurrent':upsOutputCurrent,'upsOutputPower':upsOutputPower,'upsOutputPercentLoad':upsOutputPercentLoad,'upsAlarm':upsAlarm,'upsAlarmsPresent':upsAlarmsPresent,'upsAlarmID':upsAlarmID,'upsAlarmDESCR':upsAlarmDESCR,'upsAlarmTable':upsAlarmTable,'upsAlarmEntry':upsAlarmEntry,_V:upsAlarmId,'upsAlarmDescr':upsAlarmDescr,'upsAlarmTime':upsAlarmTime,'upsWellKnownAlarms':upsWellKnownAlarms,_J:upsAlarmBatteryBad,_K:upsAlarmOnBattery,_L:upsAlarmLowBattery,_M:upsAlarmDepletedBattery,_N:upsAlarmTempBad,_O:upsAlarmOutputOverload,_P:upsAlarmOutputOffAsRequested,'upsAlarmUpsOutputOff':upsAlarmUpsOutputOff,_Q:upsAlarmDiagnosticTestFailed,_R:upsAlarmCommunicationsLost,_S:upsAlarmShutdownPending,_T:upsAlarmShutdownImminent,_U:upsAlarmTestInProgress,'upsTest':upsTest,'upsTestId':upsTestId,'upsTestResultsSummary':upsTestResultsSummary,'upsControl':upsControl,'upsShutdownType':upsShutdownType,'upsShutdownAfterDelay':upsShutdownAfterDelay,'upsStartupAfterDelay':upsStartupAfterDelay,'upsRebootDuration':upsRebootDuration,'upsAutoRestart':upsAutoRestart,'upsConfig':upsConfig,'upsConfigInputVoltageHigh':upsConfigInputVoltageHigh,'upsConfigInputVoltageLow':upsConfigInputVoltageLow,'upsConfigOutputPercLoadHigh':upsConfigOutputPercLoadHigh,'upsConfigBatteryPercLow':upsConfigBatteryPercLow,'upsConfigBatteryTemperatureHigh':upsConfigBatteryTemperatureHigh})