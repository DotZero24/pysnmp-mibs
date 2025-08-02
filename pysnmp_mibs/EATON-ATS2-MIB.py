_R='ats2ContactIndex'
_Q='internalFailure'
_P='ats2InputStatusIndex'
_O='outOfRange'
_N='normal'
_M='ats2InputIndex'
_L='percent'
_K='degrees Centigrade'
_J='source2'
_I='source1'
_H='EATON-ATS2-MIB'
_G='good'
_F='1 V'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sts,=mibBuilder.importSymbols('EATON-OIDS','sts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ats2=ModuleIdentity((1,3,6,1,4,1,534,10,2))
if mibBuilder.loadTexts:ats2.setRevisions(('2014-07-31 12:00',))
class UnixTimeStamp(TextualConvention,Counter32):status=_A;displayHint='dddddddddd'
_Ats2Ident_ObjectIdentity=ObjectIdentity
ats2Ident=_Ats2Ident_ObjectIdentity((1,3,6,1,4,1,534,10,2,1))
class _Ats2IdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ats2IdentManufacturer_Type.__name__=_D
_Ats2IdentManufacturer_Object=MibScalar
ats2IdentManufacturer=_Ats2IdentManufacturer_Object((1,3,6,1,4,1,534,10,2,1,1),_Ats2IdentManufacturer_Type())
ats2IdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentManufacturer.setStatus(_A)
class _Ats2IdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Ats2IdentModel_Type.__name__=_D
_Ats2IdentModel_Object=MibScalar
ats2IdentModel=_Ats2IdentModel_Object((1,3,6,1,4,1,534,10,2,1,2),_Ats2IdentModel_Type())
ats2IdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentModel.setStatus(_A)
class _Ats2IdentFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ats2IdentFWVersion_Type.__name__=_D
_Ats2IdentFWVersion_Object=MibScalar
ats2IdentFWVersion=_Ats2IdentFWVersion_Object((1,3,6,1,4,1,534,10,2,1,3),_Ats2IdentFWVersion_Type())
ats2IdentFWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentFWVersion.setStatus(_A)
class _Ats2IdentRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ats2IdentRelease_Type.__name__=_D
_Ats2IdentRelease_Object=MibScalar
ats2IdentRelease=_Ats2IdentRelease_Object((1,3,6,1,4,1,534,10,2,1,4),_Ats2IdentRelease_Type())
ats2IdentRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentRelease.setStatus(_A)
class _Ats2IdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Ats2IdentSerialNumber_Type.__name__=_D
_Ats2IdentSerialNumber_Object=MibScalar
ats2IdentSerialNumber=_Ats2IdentSerialNumber_Object((1,3,6,1,4,1,534,10,2,1,5),_Ats2IdentSerialNumber_Type())
ats2IdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentSerialNumber.setStatus(_A)
class _Ats2IdentPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Ats2IdentPartNumber_Type.__name__=_D
_Ats2IdentPartNumber_Object=MibScalar
ats2IdentPartNumber=_Ats2IdentPartNumber_Object((1,3,6,1,4,1,534,10,2,1,6),_Ats2IdentPartNumber_Type())
ats2IdentPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentPartNumber.setStatus(_A)
class _Ats2IdentAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Ats2IdentAgentVersion_Type.__name__=_D
_Ats2IdentAgentVersion_Object=MibScalar
ats2IdentAgentVersion=_Ats2IdentAgentVersion_Object((1,3,6,1,4,1,534,10,2,1,7),_Ats2IdentAgentVersion_Type())
ats2IdentAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2IdentAgentVersion.setStatus(_A)
_Ats2Measure_ObjectIdentity=ObjectIdentity
ats2Measure=_Ats2Measure_ObjectIdentity((1,3,6,1,4,1,534,10,2,2))
_Ats2Input_ObjectIdentity=ObjectIdentity
ats2Input=_Ats2Input_ObjectIdentity((1,3,6,1,4,1,534,10,2,2,1))
_Ats2InputDephasing_Type=Integer32
_Ats2InputDephasing_Object=MibScalar
ats2InputDephasing=_Ats2InputDephasing_Object((1,3,6,1,4,1,534,10,2,2,1,1),_Ats2InputDephasing_Type())
ats2InputDephasing.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputDephasing.setStatus(_A)
if mibBuilder.loadTexts:ats2InputDephasing.setUnits('degrees')
_Ats2InputTable_Object=MibTable
ats2InputTable=_Ats2InputTable_Object((1,3,6,1,4,1,534,10,2,2,2))
if mibBuilder.loadTexts:ats2InputTable.setStatus(_A)
_Ats2InputEntry_Object=MibTableRow
ats2InputEntry=_Ats2InputEntry_Object((1,3,6,1,4,1,534,10,2,2,2,1))
ats2InputEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:ats2InputEntry.setStatus(_A)
class _Ats2InputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Ats2InputIndex_Type.__name__=_C
_Ats2InputIndex_Object=MibTableColumn
ats2InputIndex=_Ats2InputIndex_Object((1,3,6,1,4,1,534,10,2,2,2,1,1),_Ats2InputIndex_Type())
ats2InputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputIndex.setStatus(_A)
_Ats2InputVoltage_Type=Integer32
_Ats2InputVoltage_Object=MibTableColumn
ats2InputVoltage=_Ats2InputVoltage_Object((1,3,6,1,4,1,534,10,2,2,2,1,2),_Ats2InputVoltage_Type())
ats2InputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputVoltage.setStatus(_A)
if mibBuilder.loadTexts:ats2InputVoltage.setUnits('0.1 V')
_Ats2InputFrequency_Type=Integer32
_Ats2InputFrequency_Object=MibTableColumn
ats2InputFrequency=_Ats2InputFrequency_Object((1,3,6,1,4,1,534,10,2,2,2,1,3),_Ats2InputFrequency_Type())
ats2InputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputFrequency.setStatus(_A)
if mibBuilder.loadTexts:ats2InputFrequency.setUnits('0.1 Hz')
_Ats2Output_ObjectIdentity=ObjectIdentity
ats2Output=_Ats2Output_ObjectIdentity((1,3,6,1,4,1,534,10,2,2,3))
_Ats2OutputVoltage_Type=Integer32
_Ats2OutputVoltage_Object=MibScalar
ats2OutputVoltage=_Ats2OutputVoltage_Object((1,3,6,1,4,1,534,10,2,2,3,1),_Ats2OutputVoltage_Type())
ats2OutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2OutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:ats2OutputVoltage.setUnits('0.1 V')
_Ats2OutputCurrent_Type=Integer32
_Ats2OutputCurrent_Object=MibScalar
ats2OutputCurrent=_Ats2OutputCurrent_Object((1,3,6,1,4,1,534,10,2,2,3,2),_Ats2OutputCurrent_Type())
ats2OutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2OutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:ats2OutputCurrent.setUnits('0.1 A')
class _Ats2OperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('initialization',1),('diagnosis',2),('off',3),(_I,4),(_J,5),('safe',6),('fault',7)))
_Ats2OperationMode_Type.__name__=_C
_Ats2OperationMode_Object=MibScalar
ats2OperationMode=_Ats2OperationMode_Object((1,3,6,1,4,1,534,10,2,2,4),_Ats2OperationMode_Type())
ats2OperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2OperationMode.setStatus(_A)
_Ats2Status_ObjectIdentity=ObjectIdentity
ats2Status=_Ats2Status_ObjectIdentity((1,3,6,1,4,1,534,10,2,3))
_Ats2InputStatus_ObjectIdentity=ObjectIdentity
ats2InputStatus=_Ats2InputStatus_ObjectIdentity((1,3,6,1,4,1,534,10,2,3,1))
class _Ats2InputStatusDephasing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_Ats2InputStatusDephasing_Type.__name__=_C
_Ats2InputStatusDephasing_Object=MibScalar
ats2InputStatusDephasing=_Ats2InputStatusDephasing_Object((1,3,6,1,4,1,534,10,2,3,1,1),_Ats2InputStatusDephasing_Type())
ats2InputStatusDephasing.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusDephasing.setStatus(_A)
_Ats2InputStatusTable_Object=MibTable
ats2InputStatusTable=_Ats2InputStatusTable_Object((1,3,6,1,4,1,534,10,2,3,2))
if mibBuilder.loadTexts:ats2InputStatusTable.setStatus(_A)
_Ats2InputStatusEntry_Object=MibTableRow
ats2InputStatusEntry=_Ats2InputStatusEntry_Object((1,3,6,1,4,1,534,10,2,3,2,1))
ats2InputStatusEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:ats2InputStatusEntry.setStatus(_A)
class _Ats2InputStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Ats2InputStatusIndex_Type.__name__=_C
_Ats2InputStatusIndex_Object=MibTableColumn
ats2InputStatusIndex=_Ats2InputStatusIndex_Object((1,3,6,1,4,1,534,10,2,3,2,1,1),_Ats2InputStatusIndex_Type())
ats2InputStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusIndex.setStatus(_A)
class _Ats2InputStatusFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_O,2)))
_Ats2InputStatusFrequency_Type.__name__=_C
_Ats2InputStatusFrequency_Object=MibTableColumn
ats2InputStatusFrequency=_Ats2InputStatusFrequency_Object((1,3,6,1,4,1,534,10,2,3,2,1,2),_Ats2InputStatusFrequency_Type())
ats2InputStatusFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusFrequency.setStatus(_A)
class _Ats2InputStatusGood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('voltageOrFreqOutofRange',1),('voltageAndFreqNormalRange',2),('voltageDeratedRangeAndFreqNormalRange',3),('voltageAndFreqNormalRangeWaveformNok',4)))
_Ats2InputStatusGood_Type.__name__=_C
_Ats2InputStatusGood_Object=MibTableColumn
ats2InputStatusGood=_Ats2InputStatusGood_Object((1,3,6,1,4,1,534,10,2,3,2,1,3),_Ats2InputStatusGood_Type())
ats2InputStatusGood.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusGood.setStatus(_A)
class _Ats2InputStatusInternalFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_Q,2)))
_Ats2InputStatusInternalFailure_Type.__name__=_C
_Ats2InputStatusInternalFailure_Object=MibTableColumn
ats2InputStatusInternalFailure=_Ats2InputStatusInternalFailure_Object((1,3,6,1,4,1,534,10,2,3,2,1,4),_Ats2InputStatusInternalFailure_Type())
ats2InputStatusInternalFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusInternalFailure.setStatus(_A)
class _Ats2InputStatusVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normalRange',1),('deratedRange',2),('outofRange',3),('missing',4)))
_Ats2InputStatusVoltage_Type.__name__=_C
_Ats2InputStatusVoltage_Object=MibTableColumn
ats2InputStatusVoltage=_Ats2InputStatusVoltage_Object((1,3,6,1,4,1,534,10,2,3,2,1,5),_Ats2InputStatusVoltage_Type())
ats2InputStatusVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusVoltage.setStatus(_A)
class _Ats2InputStatusUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notPoweringLoad',1),('poweringLoad',2)))
_Ats2InputStatusUsed_Type.__name__=_C
_Ats2InputStatusUsed_Object=MibTableColumn
ats2InputStatusUsed=_Ats2InputStatusUsed_Object((1,3,6,1,4,1,534,10,2,3,2,1,6),_Ats2InputStatusUsed_Type())
ats2InputStatusUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2InputStatusUsed.setStatus(_A)
_Ats2OutputStatus_ObjectIdentity=ObjectIdentity
ats2OutputStatus=_Ats2OutputStatus_ObjectIdentity((1,3,6,1,4,1,534,10,2,3,3))
class _Ats2StatusInternalFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_Q,2)))
_Ats2StatusInternalFailure_Type.__name__=_C
_Ats2StatusInternalFailure_Object=MibScalar
ats2StatusInternalFailure=_Ats2StatusInternalFailure_Object((1,3,6,1,4,1,534,10,2,3,3,1),_Ats2StatusInternalFailure_Type())
ats2StatusInternalFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusInternalFailure.setStatus(_A)
class _Ats2StatusOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outputNotPowered',1),('outputPowered',2)))
_Ats2StatusOutput_Type.__name__=_C
_Ats2StatusOutput_Object=MibScalar
ats2StatusOutput=_Ats2StatusOutput_Object((1,3,6,1,4,1,534,10,2,3,3,2),_Ats2StatusOutput_Type())
ats2StatusOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusOutput.setStatus(_A)
class _Ats2StatusOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOverload',1),('warningOverload',2),('criticalOverload',3)))
_Ats2StatusOverload_Type.__name__=_C
_Ats2StatusOverload_Object=MibScalar
ats2StatusOverload=_Ats2StatusOverload_Object((1,3,6,1,4,1,534,10,2,3,3,3),_Ats2StatusOverload_Type())
ats2StatusOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusOverload.setStatus(_A)
class _Ats2StatusOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOverTemperature',1),('overTemperature',2)))
_Ats2StatusOverTemperature_Type.__name__=_C
_Ats2StatusOverTemperature_Object=MibScalar
ats2StatusOverTemperature=_Ats2StatusOverTemperature_Object((1,3,6,1,4,1,534,10,2,3,3,4),_Ats2StatusOverTemperature_Type())
ats2StatusOverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusOverTemperature.setStatus(_A)
class _Ats2StatusShortCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noShortCircuit',1),('shortCircuit',2)))
_Ats2StatusShortCircuit_Type.__name__=_C
_Ats2StatusShortCircuit_Object=MibScalar
ats2StatusShortCircuit=_Ats2StatusShortCircuit_Object((1,3,6,1,4,1,534,10,2,3,3,5),_Ats2StatusShortCircuit_Type())
ats2StatusShortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusShortCircuit.setStatus(_A)
class _Ats2StatusCommunicationLost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('communicationLost',2)))
_Ats2StatusCommunicationLost_Type.__name__=_C
_Ats2StatusCommunicationLost_Object=MibScalar
ats2StatusCommunicationLost=_Ats2StatusCommunicationLost_Object((1,3,6,1,4,1,534,10,2,3,3,6),_Ats2StatusCommunicationLost_Type())
ats2StatusCommunicationLost.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusCommunicationLost.setStatus(_A)
class _Ats2StatusConfigurationFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('configurationFailure',2)))
_Ats2StatusConfigurationFailure_Type.__name__=_C
_Ats2StatusConfigurationFailure_Object=MibScalar
ats2StatusConfigurationFailure=_Ats2StatusConfigurationFailure_Object((1,3,6,1,4,1,534,10,2,3,3,7),_Ats2StatusConfigurationFailure_Type())
ats2StatusConfigurationFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2StatusConfigurationFailure.setStatus(_A)
_Ats2Config_ObjectIdentity=ObjectIdentity
ats2Config=_Ats2Config_ObjectIdentity((1,3,6,1,4,1,534,10,2,4))
_Ats2ConfigTime_ObjectIdentity=ObjectIdentity
ats2ConfigTime=_Ats2ConfigTime_ObjectIdentity((1,3,6,1,4,1,534,10,2,4,1))
_Ats2ConfigTimeRTC_Type=UnixTimeStamp
_Ats2ConfigTimeRTC_Object=MibScalar
ats2ConfigTimeRTC=_Ats2ConfigTimeRTC_Object((1,3,6,1,4,1,534,10,2,4,1,1),_Ats2ConfigTimeRTC_Type())
ats2ConfigTimeRTC.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ConfigTimeRTC.setStatus(_A)
class _Ats2ConfigTimeTextDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Ats2ConfigTimeTextDate_Type.__name__=_D
_Ats2ConfigTimeTextDate_Object=MibScalar
ats2ConfigTimeTextDate=_Ats2ConfigTimeTextDate_Object((1,3,6,1,4,1,534,10,2,4,1,2),_Ats2ConfigTimeTextDate_Type())
ats2ConfigTimeTextDate.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigTimeTextDate.setStatus(_A)
class _Ats2ConfigTimeTextTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ats2ConfigTimeTextTime_Type.__name__=_D
_Ats2ConfigTimeTextTime_Object=MibScalar
ats2ConfigTimeTextTime=_Ats2ConfigTimeTextTime_Object((1,3,6,1,4,1,534,10,2,4,1,3),_Ats2ConfigTimeTextTime_Type())
ats2ConfigTimeTextTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigTimeTextTime.setStatus(_A)
_Ats2ConfigInputVoltageRating_Type=Integer32
_Ats2ConfigInputVoltageRating_Object=MibScalar
ats2ConfigInputVoltageRating=_Ats2ConfigInputVoltageRating_Object((1,3,6,1,4,1,534,10,2,4,2),_Ats2ConfigInputVoltageRating_Type())
ats2ConfigInputVoltageRating.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigInputVoltageRating.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigInputVoltageRating.setUnits(_F)
_Ats2ConfigInputFrequencyRating_Type=Integer32
_Ats2ConfigInputFrequencyRating_Object=MibScalar
ats2ConfigInputFrequencyRating=_Ats2ConfigInputFrequencyRating_Object((1,3,6,1,4,1,534,10,2,4,3),_Ats2ConfigInputFrequencyRating_Type())
ats2ConfigInputFrequencyRating.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigInputFrequencyRating.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigInputFrequencyRating.setUnits('Hz')
_Ats2ConfigOutputVoltage_Type=Integer32
_Ats2ConfigOutputVoltage_Object=MibScalar
ats2ConfigOutputVoltage=_Ats2ConfigOutputVoltage_Object((1,3,6,1,4,1,534,10,2,4,4),_Ats2ConfigOutputVoltage_Type())
ats2ConfigOutputVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ConfigOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigOutputVoltage.setUnits(_F)
class _Ats2ConfigPreferred_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Ats2ConfigPreferred_Type.__name__=_C
_Ats2ConfigPreferred_Object=MibScalar
ats2ConfigPreferred=_Ats2ConfigPreferred_Object((1,3,6,1,4,1,534,10,2,4,5),_Ats2ConfigPreferred_Type())
ats2ConfigPreferred.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ConfigPreferred.setStatus(_A)
class _Ats2ConfigSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('highSensitivity',2),('lowSensitivity',3)))
_Ats2ConfigSensitivity_Type.__name__=_C
_Ats2ConfigSensitivity_Object=MibScalar
ats2ConfigSensitivity=_Ats2ConfigSensitivity_Object((1,3,6,1,4,1,534,10,2,4,6),_Ats2ConfigSensitivity_Type())
ats2ConfigSensitivity.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ConfigSensitivity.setStatus(_A)
class _Ats2ConfigTransferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('gap',2)))
_Ats2ConfigTransferMode_Type.__name__=_C
_Ats2ConfigTransferMode_Object=MibScalar
ats2ConfigTransferMode=_Ats2ConfigTransferMode_Object((1,3,6,1,4,1,534,10,2,4,7),_Ats2ConfigTransferMode_Type())
ats2ConfigTransferMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ConfigTransferMode.setStatus(_A)
class _Ats2ConfigTransferTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('doneAndPassed',1),('doneAndWarning',2),('doneAndError',3),('aborted',4),('inProgress',5),('noTestInitiated',6)))
_Ats2ConfigTransferTest_Type.__name__=_C
_Ats2ConfigTransferTest_Object=MibScalar
ats2ConfigTransferTest=_Ats2ConfigTransferTest_Object((1,3,6,1,4,1,534,10,2,4,8),_Ats2ConfigTransferTest_Type())
ats2ConfigTransferTest.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigTransferTest.setStatus(_A)
_Ats2ConfigBrownoutLow_Type=Integer32
_Ats2ConfigBrownoutLow_Object=MibScalar
ats2ConfigBrownoutLow=_Ats2ConfigBrownoutLow_Object((1,3,6,1,4,1,534,10,2,4,9),_Ats2ConfigBrownoutLow_Type())
ats2ConfigBrownoutLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigBrownoutLow.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigBrownoutLow.setUnits(_F)
_Ats2ConfigBrownoutLowDerated_Type=Integer32
_Ats2ConfigBrownoutLowDerated_Object=MibScalar
ats2ConfigBrownoutLowDerated=_Ats2ConfigBrownoutLowDerated_Object((1,3,6,1,4,1,534,10,2,4,10),_Ats2ConfigBrownoutLowDerated_Type())
ats2ConfigBrownoutLowDerated.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigBrownoutLowDerated.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigBrownoutLowDerated.setUnits(_F)
_Ats2ConfigBrownoutHigh_Type=Integer32
_Ats2ConfigBrownoutHigh_Object=MibScalar
ats2ConfigBrownoutHigh=_Ats2ConfigBrownoutHigh_Object((1,3,6,1,4,1,534,10,2,4,11),_Ats2ConfigBrownoutHigh_Type())
ats2ConfigBrownoutHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigBrownoutHigh.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigBrownoutHigh.setUnits(_F)
_Ats2ConfigHysteresisVoltage_Type=Integer32
_Ats2ConfigHysteresisVoltage_Object=MibScalar
ats2ConfigHysteresisVoltage=_Ats2ConfigHysteresisVoltage_Object((1,3,6,1,4,1,534,10,2,4,12),_Ats2ConfigHysteresisVoltage_Type())
ats2ConfigHysteresisVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ConfigHysteresisVoltage.setStatus(_A)
if mibBuilder.loadTexts:ats2ConfigHysteresisVoltage.setUnits(_F)
_Ats2Environment_ObjectIdentity=ObjectIdentity
ats2Environment=_Ats2Environment_ObjectIdentity((1,3,6,1,4,1,534,10,2,5))
class _Ats2EnvRemoteTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,200))
_Ats2EnvRemoteTemp_Type.__name__=_C
_Ats2EnvRemoteTemp_Object=MibScalar
ats2EnvRemoteTemp=_Ats2EnvRemoteTemp_Object((1,3,6,1,4,1,534,10,2,5,1),_Ats2EnvRemoteTemp_Type())
ats2EnvRemoteTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2EnvRemoteTemp.setStatus(_A)
if mibBuilder.loadTexts:ats2EnvRemoteTemp.setUnits(_K)
class _Ats2EnvRemoteHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ats2EnvRemoteHumidity_Type.__name__=_C
_Ats2EnvRemoteHumidity_Object=MibScalar
ats2EnvRemoteHumidity=_Ats2EnvRemoteHumidity_Object((1,3,6,1,4,1,534,10,2,5,2),_Ats2EnvRemoteHumidity_Type())
ats2EnvRemoteHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2EnvRemoteHumidity.setStatus(_A)
if mibBuilder.loadTexts:ats2EnvRemoteHumidity.setUnits(_L)
class _Ats2EnvNumContacts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Ats2EnvNumContacts_Type.__name__=_C
_Ats2EnvNumContacts_Object=MibScalar
ats2EnvNumContacts=_Ats2EnvNumContacts_Object((1,3,6,1,4,1,534,10,2,5,3),_Ats2EnvNumContacts_Type())
ats2EnvNumContacts.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2EnvNumContacts.setStatus(_A)
_Ats2ContactSenseTable_Object=MibTable
ats2ContactSenseTable=_Ats2ContactSenseTable_Object((1,3,6,1,4,1,534,10,2,5,4))
if mibBuilder.loadTexts:ats2ContactSenseTable.setStatus(_A)
_Ats2ContactsTableEntry_Object=MibTableRow
ats2ContactsTableEntry=_Ats2ContactsTableEntry_Object((1,3,6,1,4,1,534,10,2,5,4,1))
ats2ContactsTableEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:ats2ContactsTableEntry.setStatus(_A)
class _Ats2ContactIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Ats2ContactIndex_Type.__name__=_C
_Ats2ContactIndex_Object=MibTableColumn
ats2ContactIndex=_Ats2ContactIndex_Object((1,3,6,1,4,1,534,10,2,5,4,1,1),_Ats2ContactIndex_Type())
ats2ContactIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ContactIndex.setStatus(_A)
class _Ats2ContactType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normallyOpen',1),('normallyClosed',2),('anyChange',3),('notUsed',4)))
_Ats2ContactType_Type.__name__=_C
_Ats2ContactType_Object=MibTableColumn
ats2ContactType=_Ats2ContactType_Object((1,3,6,1,4,1,534,10,2,5,4,1,2),_Ats2ContactType_Type())
ats2ContactType.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ContactType.setStatus(_A)
class _Ats2ContactState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('open',1),('closed',2),('openWithNotice',3),('closedWithNotice',4)))
_Ats2ContactState_Type.__name__=_C
_Ats2ContactState_Object=MibTableColumn
ats2ContactState=_Ats2ContactState_Object((1,3,6,1,4,1,534,10,2,5,4,1,3),_Ats2ContactState_Type())
ats2ContactState.setMaxAccess(_B)
if mibBuilder.loadTexts:ats2ContactState.setStatus(_A)
class _Ats2ContactDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Ats2ContactDescr_Type.__name__=_D
_Ats2ContactDescr_Object=MibTableColumn
ats2ContactDescr=_Ats2ContactDescr_Object((1,3,6,1,4,1,534,10,2,5,4,1,4),_Ats2ContactDescr_Type())
ats2ContactDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2ContactDescr.setStatus(_A)
class _Ats2EnvRemoteTempLowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,200))
_Ats2EnvRemoteTempLowerLimit_Type.__name__=_C
_Ats2EnvRemoteTempLowerLimit_Object=MibScalar
ats2EnvRemoteTempLowerLimit=_Ats2EnvRemoteTempLowerLimit_Object((1,3,6,1,4,1,534,10,2,5,5),_Ats2EnvRemoteTempLowerLimit_Type())
ats2EnvRemoteTempLowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2EnvRemoteTempLowerLimit.setStatus(_A)
if mibBuilder.loadTexts:ats2EnvRemoteTempLowerLimit.setUnits(_K)
class _Ats2EnvRemoteTempUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,200))
_Ats2EnvRemoteTempUpperLimit_Type.__name__=_C
_Ats2EnvRemoteTempUpperLimit_Object=MibScalar
ats2EnvRemoteTempUpperLimit=_Ats2EnvRemoteTempUpperLimit_Object((1,3,6,1,4,1,534,10,2,5,6),_Ats2EnvRemoteTempUpperLimit_Type())
ats2EnvRemoteTempUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2EnvRemoteTempUpperLimit.setStatus(_A)
if mibBuilder.loadTexts:ats2EnvRemoteTempUpperLimit.setUnits(_K)
class _Ats2EnvRemoteHumidityLowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ats2EnvRemoteHumidityLowerLimit_Type.__name__=_C
_Ats2EnvRemoteHumidityLowerLimit_Object=MibScalar
ats2EnvRemoteHumidityLowerLimit=_Ats2EnvRemoteHumidityLowerLimit_Object((1,3,6,1,4,1,534,10,2,5,7),_Ats2EnvRemoteHumidityLowerLimit_Type())
ats2EnvRemoteHumidityLowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2EnvRemoteHumidityLowerLimit.setStatus(_A)
if mibBuilder.loadTexts:ats2EnvRemoteHumidityLowerLimit.setUnits(_L)
class _Ats2EnvRemoteHumidityUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ats2EnvRemoteHumidityUpperLimit_Type.__name__=_C
_Ats2EnvRemoteHumidityUpperLimit_Object=MibScalar
ats2EnvRemoteHumidityUpperLimit=_Ats2EnvRemoteHumidityUpperLimit_Object((1,3,6,1,4,1,534,10,2,5,8),_Ats2EnvRemoteHumidityUpperLimit_Type())
ats2EnvRemoteHumidityUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:ats2EnvRemoteHumidityUpperLimit.setStatus(_A)
if mibBuilder.loadTexts:ats2EnvRemoteHumidityUpperLimit.setUnits(_L)
_Ats2Traps_ObjectIdentity=ObjectIdentity
ats2Traps=_Ats2Traps_ObjectIdentity((1,3,6,1,4,1,534,10,2,10))
ats2TrapCommunicationLost=NotificationType((1,3,6,1,4,1,534,10,2,10,1))
if mibBuilder.loadTexts:ats2TrapCommunicationLost.setStatus(_A)
ats2TrapCommunicationRecovered=NotificationType((1,3,6,1,4,1,534,10,2,10,2))
if mibBuilder.loadTexts:ats2TrapCommunicationRecovered.setStatus(_A)
ats2TrapOutputPowered=NotificationType((1,3,6,1,4,1,534,10,2,10,3))
if mibBuilder.loadTexts:ats2TrapOutputPowered.setStatus(_A)
ats2TrapOutputNotPowered=NotificationType((1,3,6,1,4,1,534,10,2,10,4))
if mibBuilder.loadTexts:ats2TrapOutputNotPowered.setStatus(_A)
ats2TrapOverload=NotificationType((1,3,6,1,4,1,534,10,2,10,5))
if mibBuilder.loadTexts:ats2TrapOverload.setStatus(_A)
ats2TrapNoOverLoad=NotificationType((1,3,6,1,4,1,534,10,2,10,6))
if mibBuilder.loadTexts:ats2TrapNoOverLoad.setStatus(_A)
ats2TrapInternalFailure=NotificationType((1,3,6,1,4,1,534,10,2,10,7))
if mibBuilder.loadTexts:ats2TrapInternalFailure.setStatus(_A)
ats2TrapNoInternalFailure=NotificationType((1,3,6,1,4,1,534,10,2,10,8))
if mibBuilder.loadTexts:ats2TrapNoInternalFailure.setStatus(_A)
ats2TrapSource1Normal=NotificationType((1,3,6,1,4,1,534,10,2,10,9))
if mibBuilder.loadTexts:ats2TrapSource1Normal.setStatus(_A)
ats2TrapSource1OutOfRange=NotificationType((1,3,6,1,4,1,534,10,2,10,10))
if mibBuilder.loadTexts:ats2TrapSource1OutOfRange.setStatus(_A)
ats2TrapSource2Normal=NotificationType((1,3,6,1,4,1,534,10,2,10,11))
if mibBuilder.loadTexts:ats2TrapSource2Normal.setStatus(_A)
ats2TrapSource2OutOfRange=NotificationType((1,3,6,1,4,1,534,10,2,10,12))
if mibBuilder.loadTexts:ats2TrapSource2OutOfRange.setStatus(_A)
ats2TrapSourceDesynchronized=NotificationType((1,3,6,1,4,1,534,10,2,10,13))
if mibBuilder.loadTexts:ats2TrapSourceDesynchronized.setStatus(_A)
ats2TrapSourceSynchronized=NotificationType((1,3,6,1,4,1,534,10,2,10,14))
if mibBuilder.loadTexts:ats2TrapSourceSynchronized.setStatus(_A)
ats2TrapOutputPoweredBySource1=NotificationType((1,3,6,1,4,1,534,10,2,10,15))
if mibBuilder.loadTexts:ats2TrapOutputPoweredBySource1.setStatus(_A)
ats2TrapOutputPoweredBySource2=NotificationType((1,3,6,1,4,1,534,10,2,10,16))
if mibBuilder.loadTexts:ats2TrapOutputPoweredBySource2.setStatus(_A)
ats2TrapRemoteTempLow=NotificationType((1,3,6,1,4,1,534,10,2,10,20))
if mibBuilder.loadTexts:ats2TrapRemoteTempLow.setStatus(_A)
ats2TrapRemoteTempHigh=NotificationType((1,3,6,1,4,1,534,10,2,10,21))
if mibBuilder.loadTexts:ats2TrapRemoteTempHigh.setStatus(_A)
ats2TrapRemoteTempNormal=NotificationType((1,3,6,1,4,1,534,10,2,10,22))
if mibBuilder.loadTexts:ats2TrapRemoteTempNormal.setStatus(_A)
ats2TrapRemoteHumidityLow=NotificationType((1,3,6,1,4,1,534,10,2,10,23))
if mibBuilder.loadTexts:ats2TrapRemoteHumidityLow.setStatus(_A)
ats2TrapRemoteHumidityHigh=NotificationType((1,3,6,1,4,1,534,10,2,10,24))
if mibBuilder.loadTexts:ats2TrapRemoteHumidityHigh.setStatus(_A)
ats2TrapRemoteHumidityNormal=NotificationType((1,3,6,1,4,1,534,10,2,10,25))
if mibBuilder.loadTexts:ats2TrapRemoteHumidityNormal.setStatus(_A)
ats2Contact1ActiveNotice=NotificationType((1,3,6,1,4,1,534,10,2,10,26))
if mibBuilder.loadTexts:ats2Contact1ActiveNotice.setStatus(_A)
ats2Contact1InactiveNotice=NotificationType((1,3,6,1,4,1,534,10,2,10,27))
if mibBuilder.loadTexts:ats2Contact1InactiveNotice.setStatus(_A)
ats2Contact2ActiveNotice=NotificationType((1,3,6,1,4,1,534,10,2,10,28))
if mibBuilder.loadTexts:ats2Contact2ActiveNotice.setStatus(_A)
ats2Contact2InactiveNotice=NotificationType((1,3,6,1,4,1,534,10,2,10,29))
if mibBuilder.loadTexts:ats2Contact2InactiveNotice.setStatus(_A)
ats2TestTrap=NotificationType((1,3,6,1,4,1,534,10,2,10,40))
if mibBuilder.loadTexts:ats2TestTrap.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'UnixTimeStamp':UnixTimeStamp,'ats2':ats2,'ats2Ident':ats2Ident,'ats2IdentManufacturer':ats2IdentManufacturer,'ats2IdentModel':ats2IdentModel,'ats2IdentFWVersion':ats2IdentFWVersion,'ats2IdentRelease':ats2IdentRelease,'ats2IdentSerialNumber':ats2IdentSerialNumber,'ats2IdentPartNumber':ats2IdentPartNumber,'ats2IdentAgentVersion':ats2IdentAgentVersion,'ats2Measure':ats2Measure,'ats2Input':ats2Input,'ats2InputDephasing':ats2InputDephasing,'ats2InputTable':ats2InputTable,'ats2InputEntry':ats2InputEntry,_M:ats2InputIndex,'ats2InputVoltage':ats2InputVoltage,'ats2InputFrequency':ats2InputFrequency,'ats2Output':ats2Output,'ats2OutputVoltage':ats2OutputVoltage,'ats2OutputCurrent':ats2OutputCurrent,'ats2OperationMode':ats2OperationMode,'ats2Status':ats2Status,'ats2InputStatus':ats2InputStatus,'ats2InputStatusDephasing':ats2InputStatusDephasing,'ats2InputStatusTable':ats2InputStatusTable,'ats2InputStatusEntry':ats2InputStatusEntry,_P:ats2InputStatusIndex,'ats2InputStatusFrequency':ats2InputStatusFrequency,'ats2InputStatusGood':ats2InputStatusGood,'ats2InputStatusInternalFailure':ats2InputStatusInternalFailure,'ats2InputStatusVoltage':ats2InputStatusVoltage,'ats2InputStatusUsed':ats2InputStatusUsed,'ats2OutputStatus':ats2OutputStatus,'ats2StatusInternalFailure':ats2StatusInternalFailure,'ats2StatusOutput':ats2StatusOutput,'ats2StatusOverload':ats2StatusOverload,'ats2StatusOverTemperature':ats2StatusOverTemperature,'ats2StatusShortCircuit':ats2StatusShortCircuit,'ats2StatusCommunicationLost':ats2StatusCommunicationLost,'ats2StatusConfigurationFailure':ats2StatusConfigurationFailure,'ats2Config':ats2Config,'ats2ConfigTime':ats2ConfigTime,'ats2ConfigTimeRTC':ats2ConfigTimeRTC,'ats2ConfigTimeTextDate':ats2ConfigTimeTextDate,'ats2ConfigTimeTextTime':ats2ConfigTimeTextTime,'ats2ConfigInputVoltageRating':ats2ConfigInputVoltageRating,'ats2ConfigInputFrequencyRating':ats2ConfigInputFrequencyRating,'ats2ConfigOutputVoltage':ats2ConfigOutputVoltage,'ats2ConfigPreferred':ats2ConfigPreferred,'ats2ConfigSensitivity':ats2ConfigSensitivity,'ats2ConfigTransferMode':ats2ConfigTransferMode,'ats2ConfigTransferTest':ats2ConfigTransferTest,'ats2ConfigBrownoutLow':ats2ConfigBrownoutLow,'ats2ConfigBrownoutLowDerated':ats2ConfigBrownoutLowDerated,'ats2ConfigBrownoutHigh':ats2ConfigBrownoutHigh,'ats2ConfigHysteresisVoltage':ats2ConfigHysteresisVoltage,'ats2Environment':ats2Environment,'ats2EnvRemoteTemp':ats2EnvRemoteTemp,'ats2EnvRemoteHumidity':ats2EnvRemoteHumidity,'ats2EnvNumContacts':ats2EnvNumContacts,'ats2ContactSenseTable':ats2ContactSenseTable,'ats2ContactsTableEntry':ats2ContactsTableEntry,_R:ats2ContactIndex,'ats2ContactType':ats2ContactType,'ats2ContactState':ats2ContactState,'ats2ContactDescr':ats2ContactDescr,'ats2EnvRemoteTempLowerLimit':ats2EnvRemoteTempLowerLimit,'ats2EnvRemoteTempUpperLimit':ats2EnvRemoteTempUpperLimit,'ats2EnvRemoteHumidityLowerLimit':ats2EnvRemoteHumidityLowerLimit,'ats2EnvRemoteHumidityUpperLimit':ats2EnvRemoteHumidityUpperLimit,'ats2Traps':ats2Traps,'ats2TrapCommunicationLost':ats2TrapCommunicationLost,'ats2TrapCommunicationRecovered':ats2TrapCommunicationRecovered,'ats2TrapOutputPowered':ats2TrapOutputPowered,'ats2TrapOutputNotPowered':ats2TrapOutputNotPowered,'ats2TrapOverload':ats2TrapOverload,'ats2TrapNoOverLoad':ats2TrapNoOverLoad,'ats2TrapInternalFailure':ats2TrapInternalFailure,'ats2TrapNoInternalFailure':ats2TrapNoInternalFailure,'ats2TrapSource1Normal':ats2TrapSource1Normal,'ats2TrapSource1OutOfRange':ats2TrapSource1OutOfRange,'ats2TrapSource2Normal':ats2TrapSource2Normal,'ats2TrapSource2OutOfRange':ats2TrapSource2OutOfRange,'ats2TrapSourceDesynchronized':ats2TrapSourceDesynchronized,'ats2TrapSourceSynchronized':ats2TrapSourceSynchronized,'ats2TrapOutputPoweredBySource1':ats2TrapOutputPoweredBySource1,'ats2TrapOutputPoweredBySource2':ats2TrapOutputPoweredBySource2,'ats2TrapRemoteTempLow':ats2TrapRemoteTempLow,'ats2TrapRemoteTempHigh':ats2TrapRemoteTempHigh,'ats2TrapRemoteTempNormal':ats2TrapRemoteTempNormal,'ats2TrapRemoteHumidityLow':ats2TrapRemoteHumidityLow,'ats2TrapRemoteHumidityHigh':ats2TrapRemoteHumidityHigh,'ats2TrapRemoteHumidityNormal':ats2TrapRemoteHumidityNormal,'ats2Contact1ActiveNotice':ats2Contact1ActiveNotice,'ats2Contact1InactiveNotice':ats2Contact1InactiveNotice,'ats2Contact2ActiveNotice':ats2Contact2ActiveNotice,'ats2Contact2InactiveNotice':ats2Contact2InactiveNotice,'ats2TestTrap':ats2TestTrap})