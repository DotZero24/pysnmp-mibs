_S='atsConfigInputIndex'
_R='atsLogIndex'
_Q='atsInputFailureIndex'
_P='atsInputFlowIndex'
_O='atsInputIndex'
_N='NotificationType'
_M='0.1 Second'
_L='off'
_K='source-2'
_J='source-1'
_I='0.1 V'
_H='EatonSTS-MIB'
_G='DisplayString'
_F='normal'
_E='abnormal'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Eaton_ObjectIdentity=ObjectIdentity
eaton=_Eaton_ObjectIdentity((1,3,6,1,4,1,534))
_Sts_ObjectIdentity=ObjectIdentity
sts=_Sts_ObjectIdentity((1,3,6,1,4,1,534,10))
_Ats_ObjectIdentity=ObjectIdentity
ats=_Ats_ObjectIdentity((1,3,6,1,4,1,534,10,1))
_AtsAgent_ObjectIdentity=ObjectIdentity
atsAgent=_AtsAgent_ObjectIdentity((1,3,6,1,4,1,534,10,1,1))
class _AtsAgentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AtsAgentManufacturer_Type.__name__=_G
_AtsAgentManufacturer_Object=MibScalar
atsAgentManufacturer=_AtsAgentManufacturer_Object((1,3,6,1,4,1,534,10,1,1,1),_AtsAgentManufacturer_Type())
atsAgentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:atsAgentManufacturer.setStatus(_A)
class _AtsAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtsAgentVersion_Type.__name__=_G
_AtsAgentVersion_Object=MibScalar
atsAgentVersion=_AtsAgentVersion_Object((1,3,6,1,4,1,534,10,1,1,2),_AtsAgentVersion_Type())
atsAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atsAgentVersion.setStatus(_A)
_AtsAgentModbus_ObjectIdentity=ObjectIdentity
atsAgentModbus=_AtsAgentModbus_ObjectIdentity((1,3,6,1,4,1,534,10,1,1,3))
class _AtsAgentModbusLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linked',1),('un-linked',2)))
_AtsAgentModbusLink_Type.__name__=_C
_AtsAgentModbusLink_Object=MibScalar
atsAgentModbusLink=_AtsAgentModbusLink_Object((1,3,6,1,4,1,534,10,1,1,3,1),_AtsAgentModbusLink_Type())
atsAgentModbusLink.setMaxAccess(_B)
if mibBuilder.loadTexts:atsAgentModbusLink.setStatus(_A)
_AtsIdent_ObjectIdentity=ObjectIdentity
atsIdent=_AtsIdent_ObjectIdentity((1,3,6,1,4,1,534,10,1,2))
class _AtsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AtsIdentModel_Type.__name__=_G
_AtsIdentModel_Object=MibScalar
atsIdentModel=_AtsIdentModel_Object((1,3,6,1,4,1,534,10,1,2,1),_AtsIdentModel_Type())
atsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:atsIdentModel.setStatus(_A)
class _AtsIdentFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AtsIdentFWVersion_Type.__name__=_G
_AtsIdentFWVersion_Object=MibScalar
atsIdentFWVersion=_AtsIdentFWVersion_Object((1,3,6,1,4,1,534,10,1,2,2),_AtsIdentFWVersion_Type())
atsIdentFWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atsIdentFWVersion.setStatus(_A)
class _AtsIdentRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AtsIdentRelease_Type.__name__=_G
_AtsIdentRelease_Object=MibScalar
atsIdentRelease=_AtsIdentRelease_Object((1,3,6,1,4,1,534,10,1,2,3),_AtsIdentRelease_Type())
atsIdentRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:atsIdentRelease.setStatus(_A)
class _AtsIdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtsIdentSerialNumber_Type.__name__=_G
_AtsIdentSerialNumber_Object=MibScalar
atsIdentSerialNumber=_AtsIdentSerialNumber_Object((1,3,6,1,4,1,534,10,1,2,4),_AtsIdentSerialNumber_Type())
atsIdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atsIdentSerialNumber.setStatus(_A)
class _AtsIdentIDCodes_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtsIdentIDCodes_Type.__name__=_G
_AtsIdentIDCodes_Object=MibScalar
atsIdentIDCodes=_AtsIdentIDCodes_Object((1,3,6,1,4,1,534,10,1,2,5),_AtsIdentIDCodes_Type())
atsIdentIDCodes.setMaxAccess(_D)
if mibBuilder.loadTexts:atsIdentIDCodes.setStatus(_A)
_AtsMeasure_ObjectIdentity=ObjectIdentity
atsMeasure=_AtsMeasure_ObjectIdentity((1,3,6,1,4,1,534,10,1,3))
_AtsInputTable_Object=MibTable
atsInputTable=_AtsInputTable_Object((1,3,6,1,4,1,534,10,1,3,1))
if mibBuilder.loadTexts:atsInputTable.setStatus(_A)
_AtsInputEntry_Object=MibTableRow
atsInputEntry=_AtsInputEntry_Object((1,3,6,1,4,1,534,10,1,3,1,1))
atsInputEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:atsInputEntry.setStatus(_A)
class _AtsInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtsInputIndex_Type.__name__=_C
_AtsInputIndex_Object=MibTableColumn
atsInputIndex=_AtsInputIndex_Object((1,3,6,1,4,1,534,10,1,3,1,1,1),_AtsInputIndex_Type())
atsInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputIndex.setStatus(_A)
_AtsInputVoltage_Type=Integer32
_AtsInputVoltage_Object=MibTableColumn
atsInputVoltage=_AtsInputVoltage_Object((1,3,6,1,4,1,534,10,1,3,1,1,2),_AtsInputVoltage_Type())
atsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:atsInputVoltage.setUnits(_I)
_AtsInputFrequency_Type=Integer32
_AtsInputFrequency_Object=MibTableColumn
atsInputFrequency=_AtsInputFrequency_Object((1,3,6,1,4,1,534,10,1,3,1,1,3),_AtsInputFrequency_Type())
atsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFrequency.setStatus(_A)
if mibBuilder.loadTexts:atsInputFrequency.setUnits('0.1 Hz')
_AtsOutput_ObjectIdentity=ObjectIdentity
atsOutput=_AtsOutput_ObjectIdentity((1,3,6,1,4,1,534,10,1,3,2))
_AtsOutputVoltage_Type=Integer32
_AtsOutputVoltage_Object=MibScalar
atsOutputVoltage=_AtsOutputVoltage_Object((1,3,6,1,4,1,534,10,1,3,2,1),_AtsOutputVoltage_Type())
atsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:atsOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:atsOutputVoltage.setUnits(_I)
_AtsOutputCurrent_Type=Integer32
_AtsOutputCurrent_Object=MibScalar
atsOutputCurrent=_AtsOutputCurrent_Object((1,3,6,1,4,1,534,10,1,3,2,2),_AtsOutputCurrent_Type())
atsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:atsOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:atsOutputCurrent.setUnits('0.1 A')
_AtsMeasureTemperatureC_Type=Integer32
_AtsMeasureTemperatureC_Object=MibScalar
atsMeasureTemperatureC=_AtsMeasureTemperatureC_Object((1,3,6,1,4,1,534,10,1,3,3),_AtsMeasureTemperatureC_Type())
atsMeasureTemperatureC.setMaxAccess(_B)
if mibBuilder.loadTexts:atsMeasureTemperatureC.setStatus(_A)
if mibBuilder.loadTexts:atsMeasureTemperatureC.setUnits('1 Celsius')
_AtsMeasureTemperatureF_Type=Integer32
_AtsMeasureTemperatureF_Object=MibScalar
atsMeasureTemperatureF=_AtsMeasureTemperatureF_Object((1,3,6,1,4,1,534,10,1,3,4),_AtsMeasureTemperatureF_Type())
atsMeasureTemperatureF.setMaxAccess(_B)
if mibBuilder.loadTexts:atsMeasureTemperatureF.setStatus(_A)
if mibBuilder.loadTexts:atsMeasureTemperatureF.setUnits('1 Fahrenheit')
_AtsMessureRunTime_Type=Integer32
_AtsMessureRunTime_Object=MibScalar
atsMessureRunTime=_AtsMessureRunTime_Object((1,3,6,1,4,1,534,10,1,3,5),_AtsMessureRunTime_Type())
atsMessureRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atsMessureRunTime.setStatus(_A)
if mibBuilder.loadTexts:atsMessureRunTime.setUnits('1 second')
_AtsMessureTransferedTimes_Type=Integer32
_AtsMessureTransferedTimes_Object=MibScalar
atsMessureTransferedTimes=_AtsMessureTransferedTimes_Object((1,3,6,1,4,1,534,10,1,3,6),_AtsMessureTransferedTimes_Type())
atsMessureTransferedTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:atsMessureTransferedTimes.setStatus(_A)
class _AtsMessureOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('initialization',1),('diagnosis',2),(_L,3),(_J,4),(_K,5),('safe',6),('fault',7)))
_AtsMessureOperationMode_Type.__name__=_C
_AtsMessureOperationMode_Object=MibScalar
atsMessureOperationMode=_AtsMessureOperationMode_Object((1,3,6,1,4,1,534,10,1,3,7),_AtsMessureOperationMode_Type())
atsMessureOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:atsMessureOperationMode.setStatus(_A)
_AtsStatus_ObjectIdentity=ObjectIdentity
atsStatus=_AtsStatus_ObjectIdentity((1,3,6,1,4,1,534,10,1,4))
_AtsInputFlowIndicator_Type=Integer32
_AtsInputFlowIndicator_Object=MibScalar
atsInputFlowIndicator=_AtsInputFlowIndicator_Object((1,3,6,1,4,1,534,10,1,4,1),_AtsInputFlowIndicator_Type())
atsInputFlowIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFlowIndicator.setStatus(_A)
_AtsInputFlowTable_Object=MibTable
atsInputFlowTable=_AtsInputFlowTable_Object((1,3,6,1,4,1,534,10,1,4,2))
if mibBuilder.loadTexts:atsInputFlowTable.setStatus(_A)
_AtsInputFlowEntry_Object=MibTableRow
atsInputFlowEntry=_AtsInputFlowEntry_Object((1,3,6,1,4,1,534,10,1,4,2,1))
atsInputFlowEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:atsInputFlowEntry.setStatus(_A)
class _AtsInputFlowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtsInputFlowIndex_Type.__name__=_C
_AtsInputFlowIndex_Object=MibTableColumn
atsInputFlowIndex=_AtsInputFlowIndex_Object((1,3,6,1,4,1,534,10,1,4,2,1,1),_AtsInputFlowIndex_Type())
atsInputFlowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFlowIndex.setStatus(_A)
class _AtsInputFlowRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_AtsInputFlowRelay_Type.__name__=_C
_AtsInputFlowRelay_Object=MibTableColumn
atsInputFlowRelay=_AtsInputFlowRelay_Object((1,3,6,1,4,1,534,10,1,4,2,1,2),_AtsInputFlowRelay_Type())
atsInputFlowRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFlowRelay.setStatus(_A)
class _AtsInputFlowSCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_AtsInputFlowSCR_Type.__name__=_C
_AtsInputFlowSCR_Object=MibTableColumn
atsInputFlowSCR=_AtsInputFlowSCR_Object((1,3,6,1,4,1,534,10,1,4,2,1,3),_AtsInputFlowSCR_Type())
atsInputFlowSCR.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFlowSCR.setStatus(_A)
class _AtsInputFlowParallelRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_AtsInputFlowParallelRelay_Type.__name__=_C
_AtsInputFlowParallelRelay_Object=MibTableColumn
atsInputFlowParallelRelay=_AtsInputFlowParallelRelay_Object((1,3,6,1,4,1,534,10,1,4,2,1,4),_AtsInputFlowParallelRelay_Type())
atsInputFlowParallelRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFlowParallelRelay.setStatus(_A)
_AtsInputFailureIndicator_Type=Integer32
_AtsInputFailureIndicator_Object=MibScalar
atsInputFailureIndicator=_AtsInputFailureIndicator_Object((1,3,6,1,4,1,534,10,1,4,3),_AtsInputFailureIndicator_Type())
atsInputFailureIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureIndicator.setStatus(_A)
_AtsInputFailureTable_Object=MibTable
atsInputFailureTable=_AtsInputFailureTable_Object((1,3,6,1,4,1,534,10,1,4,4))
if mibBuilder.loadTexts:atsInputFailureTable.setStatus(_A)
_AtsInputFailureEntry_Object=MibTableRow
atsInputFailureEntry=_AtsInputFailureEntry_Object((1,3,6,1,4,1,534,10,1,4,4,1))
atsInputFailureEntry.setIndexNames((0,_H,_Q))
if mibBuilder.loadTexts:atsInputFailureEntry.setStatus(_A)
class _AtsInputFailureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtsInputFailureIndex_Type.__name__=_C
_AtsInputFailureIndex_Object=MibTableColumn
atsInputFailureIndex=_AtsInputFailureIndex_Object((1,3,6,1,4,1,534,10,1,4,4,1,1),_AtsInputFailureIndex_Type())
atsInputFailureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureIndex.setStatus(_A)
class _AtsInputFailureRelayOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureRelayOpen_Type.__name__=_C
_AtsInputFailureRelayOpen_Object=MibTableColumn
atsInputFailureRelayOpen=_AtsInputFailureRelayOpen_Object((1,3,6,1,4,1,534,10,1,4,4,1,2),_AtsInputFailureRelayOpen_Type())
atsInputFailureRelayOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureRelayOpen.setStatus(_A)
class _AtsInputFailureRelayShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureRelayShort_Type.__name__=_C
_AtsInputFailureRelayShort_Object=MibTableColumn
atsInputFailureRelayShort=_AtsInputFailureRelayShort_Object((1,3,6,1,4,1,534,10,1,4,4,1,3),_AtsInputFailureRelayShort_Type())
atsInputFailureRelayShort.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureRelayShort.setStatus(_A)
class _AtsInputFailureSCROpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureSCROpen_Type.__name__=_C
_AtsInputFailureSCROpen_Object=MibTableColumn
atsInputFailureSCROpen=_AtsInputFailureSCROpen_Object((1,3,6,1,4,1,534,10,1,4,4,1,4),_AtsInputFailureSCROpen_Type())
atsInputFailureSCROpen.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureSCROpen.setStatus(_A)
class _AtsInputFailureSCRShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureSCRShort_Type.__name__=_C
_AtsInputFailureSCRShort_Object=MibTableColumn
atsInputFailureSCRShort=_AtsInputFailureSCRShort_Object((1,3,6,1,4,1,534,10,1,4,4,1,5),_AtsInputFailureSCRShort_Type())
atsInputFailureSCRShort.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureSCRShort.setStatus(_A)
class _AtsInputFailureSCRThermal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureSCRThermal_Type.__name__=_C
_AtsInputFailureSCRThermal_Object=MibTableColumn
atsInputFailureSCRThermal=_AtsInputFailureSCRThermal_Object((1,3,6,1,4,1,534,10,1,4,4,1,6),_AtsInputFailureSCRThermal_Type())
atsInputFailureSCRThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureSCRThermal.setStatus(_A)
class _AtsInputFailureAuxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureAuxPower_Type.__name__=_C
_AtsInputFailureAuxPower_Object=MibTableColumn
atsInputFailureAuxPower=_AtsInputFailureAuxPower_Object((1,3,6,1,4,1,534,10,1,4,4,1,7),_AtsInputFailureAuxPower_Type())
atsInputFailureAuxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureAuxPower.setStatus(_A)
class _AtsInputFailureDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureDrop_Type.__name__=_C
_AtsInputFailureDrop_Object=MibTableColumn
atsInputFailureDrop=_AtsInputFailureDrop_Object((1,3,6,1,4,1,534,10,1,4,4,1,8),_AtsInputFailureDrop_Type())
atsInputFailureDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureDrop.setStatus(_A)
class _AtsInputFailureBrownout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureBrownout_Type.__name__=_C
_AtsInputFailureBrownout_Object=MibTableColumn
atsInputFailureBrownout=_AtsInputFailureBrownout_Object((1,3,6,1,4,1,534,10,1,4,4,1,9),_AtsInputFailureBrownout_Type())
atsInputFailureBrownout.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureBrownout.setStatus(_A)
class _AtsInputFailureFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureFrequency_Type.__name__=_C
_AtsInputFailureFrequency_Object=MibTableColumn
atsInputFailureFrequency=_AtsInputFailureFrequency_Object((1,3,6,1,4,1,534,10,1,4,4,1,10),_AtsInputFailureFrequency_Type())
atsInputFailureFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureFrequency.setStatus(_A)
class _AtsInputFailureNotOperable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsInputFailureNotOperable_Type.__name__=_C
_AtsInputFailureNotOperable_Object=MibTableColumn
atsInputFailureNotOperable=_AtsInputFailureNotOperable_Object((1,3,6,1,4,1,534,10,1,4,4,1,11),_AtsInputFailureNotOperable_Type())
atsInputFailureNotOperable.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputFailureNotOperable.setStatus(_A)
_AtsFailureIndicator_Type=Integer32
_AtsFailureIndicator_Object=MibScalar
atsFailureIndicator=_AtsFailureIndicator_Object((1,3,6,1,4,1,534,10,1,4,5),_AtsFailureIndicator_Type())
atsFailureIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:atsFailureIndicator.setStatus(_A)
_AtsFailure_ObjectIdentity=ObjectIdentity
atsFailure=_AtsFailure_ObjectIdentity((1,3,6,1,4,1,534,10,1,4,6))
class _AtsFailureSwitchFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsFailureSwitchFault_Type.__name__=_C
_AtsFailureSwitchFault_Object=MibScalar
atsFailureSwitchFault=_AtsFailureSwitchFault_Object((1,3,6,1,4,1,534,10,1,4,6,1),_AtsFailureSwitchFault_Type())
atsFailureSwitchFault.setMaxAccess(_B)
if mibBuilder.loadTexts:atsFailureSwitchFault.setStatus(_A)
class _AtsFailureNoOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsFailureNoOutput_Type.__name__=_C
_AtsFailureNoOutput_Object=MibScalar
atsFailureNoOutput=_AtsFailureNoOutput_Object((1,3,6,1,4,1,534,10,1,4,6,2),_AtsFailureNoOutput_Type())
atsFailureNoOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:atsFailureNoOutput.setStatus(_A)
class _AtsFailureOutputOC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsFailureOutputOC_Type.__name__=_C
_AtsFailureOutputOC_Object=MibScalar
atsFailureOutputOC=_AtsFailureOutputOC_Object((1,3,6,1,4,1,534,10,1,4,6,3),_AtsFailureOutputOC_Type())
atsFailureOutputOC.setMaxAccess(_B)
if mibBuilder.loadTexts:atsFailureOutputOC.setStatus(_A)
class _AtsFailureOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtsFailureOverTemperature_Type.__name__=_C
_AtsFailureOverTemperature_Object=MibScalar
atsFailureOverTemperature=_AtsFailureOverTemperature_Object((1,3,6,1,4,1,534,10,1,4,6,4),_AtsFailureOverTemperature_Type())
atsFailureOverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:atsFailureOverTemperature.setStatus(_A)
_AtsLog_ObjectIdentity=ObjectIdentity
atsLog=_AtsLog_ObjectIdentity((1,3,6,1,4,1,534,10,1,5))
_AtsLogNum_Type=Integer32
_AtsLogNum_Object=MibScalar
atsLogNum=_AtsLogNum_Object((1,3,6,1,4,1,534,10,1,5,1),_AtsLogNum_Type())
atsLogNum.setMaxAccess(_B)
if mibBuilder.loadTexts:atsLogNum.setStatus(_A)
_AtsLogTable_Object=MibTable
atsLogTable=_AtsLogTable_Object((1,3,6,1,4,1,534,10,1,5,2))
if mibBuilder.loadTexts:atsLogTable.setStatus(_A)
_AtsLogEntry_Object=MibTableRow
atsLogEntry=_AtsLogEntry_Object((1,3,6,1,4,1,534,10,1,5,2,1))
atsLogEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:atsLogEntry.setStatus(_A)
class _AtsLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AtsLogIndex_Type.__name__=_C
_AtsLogIndex_Object=MibTableColumn
atsLogIndex=_AtsLogIndex_Object((1,3,6,1,4,1,534,10,1,5,2,1,1),_AtsLogIndex_Type())
atsLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atsLogIndex.setStatus(_A)
_AtsLogTime_Type=TimeTicks
_AtsLogTime_Object=MibTableColumn
atsLogTime=_AtsLogTime_Object((1,3,6,1,4,1,534,10,1,5,2,1,2),_AtsLogTime_Type())
atsLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atsLogTime.setStatus(_A)
if mibBuilder.loadTexts:atsLogTime.setUnits('1 Second')
_AtsLogCode_Type=Integer32
_AtsLogCode_Object=MibTableColumn
atsLogCode=_AtsLogCode_Object((1,3,6,1,4,1,534,10,1,5,2,1,3),_AtsLogCode_Type())
atsLogCode.setMaxAccess(_B)
if mibBuilder.loadTexts:atsLogCode.setStatus(_A)
class _AtsLogTimeText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtsLogTimeText_Type.__name__=_G
_AtsLogTimeText_Object=MibTableColumn
atsLogTimeText=_AtsLogTimeText_Object((1,3,6,1,4,1,534,10,1,5,2,1,4),_AtsLogTimeText_Type())
atsLogTimeText.setMaxAccess(_B)
if mibBuilder.loadTexts:atsLogTimeText.setStatus(_A)
_AtsConfig_ObjectIdentity=ObjectIdentity
atsConfig=_AtsConfig_ObjectIdentity((1,3,6,1,4,1,534,10,1,6))
_AtsConfigTime_ObjectIdentity=ObjectIdentity
atsConfigTime=_AtsConfigTime_ObjectIdentity((1,3,6,1,4,1,534,10,1,6,1))
_AtsConfigTimeRTC_Type=Integer32
_AtsConfigTimeRTC_Object=MibScalar
atsConfigTimeRTC=_AtsConfigTimeRTC_Object((1,3,6,1,4,1,534,10,1,6,1,1),_AtsConfigTimeRTC_Type())
atsConfigTimeRTC.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigTimeRTC.setStatus(_A)
class _AtsConfigTimeTextDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_AtsConfigTimeTextDate_Type.__name__=_G
_AtsConfigTimeTextDate_Object=MibScalar
atsConfigTimeTextDate=_AtsConfigTimeTextDate_Object((1,3,6,1,4,1,534,10,1,6,1,2),_AtsConfigTimeTextDate_Type())
atsConfigTimeTextDate.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigTimeTextDate.setStatus(_A)
class _AtsConfigTimeTextTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AtsConfigTimeTextTime_Type.__name__=_G
_AtsConfigTimeTextTime_Object=MibScalar
atsConfigTimeTextTime=_AtsConfigTimeTextTime_Object((1,3,6,1,4,1,534,10,1,6,1,3),_AtsConfigTimeTextTime_Type())
atsConfigTimeTextTime.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigTimeTextTime.setStatus(_A)
_AtsConfigInputTable_Object=MibTable
atsConfigInputTable=_AtsConfigInputTable_Object((1,3,6,1,4,1,534,10,1,6,2))
if mibBuilder.loadTexts:atsConfigInputTable.setStatus(_A)
_AtsConfigInputEntry_Object=MibTableRow
atsConfigInputEntry=_AtsConfigInputEntry_Object((1,3,6,1,4,1,534,10,1,6,2,1))
atsConfigInputEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:atsConfigInputEntry.setStatus(_A)
class _AtsConfigInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AtsConfigInputIndex_Type.__name__=_C
_AtsConfigInputIndex_Object=MibTableColumn
atsConfigInputIndex=_AtsConfigInputIndex_Object((1,3,6,1,4,1,534,10,1,6,2,1,1),_AtsConfigInputIndex_Type())
atsConfigInputIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputIndex.setStatus(_A)
_AtsConfigInputTrip_Type=Integer32
_AtsConfigInputTrip_Object=MibTableColumn
atsConfigInputTrip=_AtsConfigInputTrip_Object((1,3,6,1,4,1,534,10,1,6,2,1,2),_AtsConfigInputTrip_Type())
atsConfigInputTrip.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputTrip.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputTrip.setUnits(_I)
_AtsConfigInputBrownoutLow_Type=Integer32
_AtsConfigInputBrownoutLow_Object=MibTableColumn
atsConfigInputBrownoutLow=_AtsConfigInputBrownoutLow_Object((1,3,6,1,4,1,534,10,1,6,2,1,3),_AtsConfigInputBrownoutLow_Type())
atsConfigInputBrownoutLow.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputBrownoutLow.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputBrownoutLow.setUnits(_I)
_AtsConfigInputBrownoutHigh_Type=Integer32
_AtsConfigInputBrownoutHigh_Object=MibTableColumn
atsConfigInputBrownoutHigh=_AtsConfigInputBrownoutHigh_Object((1,3,6,1,4,1,534,10,1,6,2,1,4),_AtsConfigInputBrownoutHigh_Type())
atsConfigInputBrownoutHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputBrownoutHigh.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputBrownoutHigh.setUnits(_I)
_AtsConfigInputRecover_Type=Integer32
_AtsConfigInputRecover_Object=MibTableColumn
atsConfigInputRecover=_AtsConfigInputRecover_Object((1,3,6,1,4,1,534,10,1,6,2,1,5),_AtsConfigInputRecover_Type())
atsConfigInputRecover.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputRecover.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputRecover.setUnits(_M)
_AtsConfigInputMaxVoltage_Type=Integer32
_AtsConfigInputMaxVoltage_Object=MibTableColumn
atsConfigInputMaxVoltage=_AtsConfigInputMaxVoltage_Object((1,3,6,1,4,1,534,10,1,6,2,1,6),_AtsConfigInputMaxVoltage_Type())
atsConfigInputMaxVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputMaxVoltage.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputMaxVoltage.setUnits('1 V')
_AtsConfigInputMaxTime_Type=Integer32
_AtsConfigInputMaxTime_Object=MibTableColumn
atsConfigInputMaxTime=_AtsConfigInputMaxTime_Object((1,3,6,1,4,1,534,10,1,6,2,1,7),_AtsConfigInputMaxTime_Type())
atsConfigInputMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigInputMaxTime.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputMaxTime.setUnits(_M)
_AtsConfigInputDelayTime_Type=Integer32
_AtsConfigInputDelayTime_Object=MibTableColumn
atsConfigInputDelayTime=_AtsConfigInputDelayTime_Object((1,3,6,1,4,1,534,10,1,6,2,1,8),_AtsConfigInputDelayTime_Type())
atsConfigInputDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atsConfigInputDelayTime.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputDelayTime.setUnits(_M)
_AtsConfigInputVoltageRating_Type=Integer32
_AtsConfigInputVoltageRating_Object=MibScalar
atsConfigInputVoltageRating=_AtsConfigInputVoltageRating_Object((1,3,6,1,4,1,534,10,1,6,3),_AtsConfigInputVoltageRating_Type())
atsConfigInputVoltageRating.setMaxAccess(_B)
if mibBuilder.loadTexts:atsConfigInputVoltageRating.setStatus(_A)
if mibBuilder.loadTexts:atsConfigInputVoltageRating.setUnits(_I)
_AtsConfigRandomTime_Type=Integer32
_AtsConfigRandomTime_Object=MibScalar
atsConfigRandomTime=_AtsConfigRandomTime_Object((1,3,6,1,4,1,534,10,1,6,4),_AtsConfigRandomTime_Type())
atsConfigRandomTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atsConfigRandomTime.setStatus(_A)
if mibBuilder.loadTexts:atsConfigRandomTime.setUnits(_M)
class _AtsConfigPreferred_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtsConfigPreferred_Type.__name__=_C
_AtsConfigPreferred_Object=MibScalar
atsConfigPreferred=_AtsConfigPreferred_Object((1,3,6,1,4,1,534,10,1,6,5),_AtsConfigPreferred_Type())
atsConfigPreferred.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigPreferred.setStatus(_A)
class _AtsConfigSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_AtsConfigSensitivity_Type.__name__=_C
_AtsConfigSensitivity_Object=MibScalar
atsConfigSensitivity=_AtsConfigSensitivity_Object((1,3,6,1,4,1,534,10,1,6,6),_AtsConfigSensitivity_Type())
atsConfigSensitivity.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigSensitivity.setStatus(_A)
class _AtsConfigTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_AtsConfigTest_Type.__name__=_C
_AtsConfigTest_Object=MibScalar
atsConfigTest=_AtsConfigTest_Object((1,3,6,1,4,1,534,10,1,6,7),_AtsConfigTest_Type())
atsConfigTest.setMaxAccess(_D)
if mibBuilder.loadTexts:atsConfigTest.setStatus(_A)
_AtsUpgrade_ObjectIdentity=ObjectIdentity
atsUpgrade=_AtsUpgrade_ObjectIdentity((1,3,6,1,4,1,534,10,1,7))
class _AtsUpgradeProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('run',2),('error',3)))
_AtsUpgradeProcess_Type.__name__=_C
_AtsUpgradeProcess_Object=MibScalar
atsUpgradeProcess=_AtsUpgradeProcess_Object((1,3,6,1,4,1,534,10,1,7,1),_AtsUpgradeProcess_Type())
atsUpgradeProcess.setMaxAccess(_B)
if mibBuilder.loadTexts:atsUpgradeProcess.setStatus(_A)
class _AtsUpgradeStep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('fileid',2),('auth',3),('addr',4),('erase',5),('program',6),('read',7)))
_AtsUpgradeStep_Type.__name__=_C
_AtsUpgradeStep_Object=MibScalar
atsUpgradeStep=_AtsUpgradeStep_Object((1,3,6,1,4,1,534,10,1,7,2),_AtsUpgradeStep_Type())
atsUpgradeStep.setMaxAccess(_B)
if mibBuilder.loadTexts:atsUpgradeStep.setStatus(_A)
_AtsUpgradePercentage_Type=Integer32
_AtsUpgradePercentage_Object=MibScalar
atsUpgradePercentage=_AtsUpgradePercentage_Object((1,3,6,1,4,1,534,10,1,7,3),_AtsUpgradePercentage_Type())
atsUpgradePercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:atsUpgradePercentage.setStatus(_A)
if mibBuilder.loadTexts:atsUpgradePercentage.setUnits('0.1%')
_AtsTraps_ObjectIdentity=ObjectIdentity
atsTraps=_AtsTraps_ObjectIdentity((1,3,6,1,4,1,534,10,1,20))
atsTrapCommLost=NotificationType((1,3,6,1,4,1,534,10,1,20,0,1))
if mibBuilder.loadTexts:atsTrapCommLost.setStatus('')
atsTrapCommEstablished=NotificationType((1,3,6,1,4,1,534,10,1,20,0,2))
if mibBuilder.loadTexts:atsTrapCommEstablished.setStatus('')
atsTrapConfigChange=NotificationType((1,3,6,1,4,1,534,10,1,20,0,3))
if mibBuilder.loadTexts:atsTrapConfigChange.setStatus('')
atsTrapFlowChange=NotificationType((1,3,6,1,4,1,534,10,1,20,0,4))
if mibBuilder.loadTexts:atsTrapFlowChange.setStatus('')
atsTrapInput1Alarm=NotificationType((1,3,6,1,4,1,534,10,1,20,0,5))
if mibBuilder.loadTexts:atsTrapInput1Alarm.setStatus('')
atsTrapInput1AlarmRecover=NotificationType((1,3,6,1,4,1,534,10,1,20,0,6))
if mibBuilder.loadTexts:atsTrapInput1AlarmRecover.setStatus('')
atsTrapInput2Alarm=NotificationType((1,3,6,1,4,1,534,10,1,20,0,7))
if mibBuilder.loadTexts:atsTrapInput2Alarm.setStatus('')
atsTrapInput2AlarmRecover=NotificationType((1,3,6,1,4,1,534,10,1,20,0,8))
if mibBuilder.loadTexts:atsTrapInput2AlarmRecover.setStatus('')
atsTrapAlarm=NotificationType((1,3,6,1,4,1,534,10,1,20,0,9))
if mibBuilder.loadTexts:atsTrapAlarm.setStatus('')
atsTrapAlarmRecover=NotificationType((1,3,6,1,4,1,534,10,1,20,0,10))
if mibBuilder.loadTexts:atsTrapAlarmRecover.setStatus('')
atsTrapUpgradeBegin=NotificationType((1,3,6,1,4,1,534,10,1,20,0,11))
if mibBuilder.loadTexts:atsTrapUpgradeBegin.setStatus('')
atsTrapUpgradeEnd=NotificationType((1,3,6,1,4,1,534,10,1,20,0,12))
if mibBuilder.loadTexts:atsTrapUpgradeEnd.setStatus('')
mibBuilder.exportSymbols(_H,**{'eaton':eaton,'sts':sts,'ats':ats,'atsAgent':atsAgent,'atsAgentManufacturer':atsAgentManufacturer,'atsAgentVersion':atsAgentVersion,'atsAgentModbus':atsAgentModbus,'atsAgentModbusLink':atsAgentModbusLink,'atsIdent':atsIdent,'atsIdentModel':atsIdentModel,'atsIdentFWVersion':atsIdentFWVersion,'atsIdentRelease':atsIdentRelease,'atsIdentSerialNumber':atsIdentSerialNumber,'atsIdentIDCodes':atsIdentIDCodes,'atsMeasure':atsMeasure,'atsInputTable':atsInputTable,'atsInputEntry':atsInputEntry,_O:atsInputIndex,'atsInputVoltage':atsInputVoltage,'atsInputFrequency':atsInputFrequency,'atsOutput':atsOutput,'atsOutputVoltage':atsOutputVoltage,'atsOutputCurrent':atsOutputCurrent,'atsMeasureTemperatureC':atsMeasureTemperatureC,'atsMeasureTemperatureF':atsMeasureTemperatureF,'atsMessureRunTime':atsMessureRunTime,'atsMessureTransferedTimes':atsMessureTransferedTimes,'atsMessureOperationMode':atsMessureOperationMode,'atsStatus':atsStatus,'atsInputFlowIndicator':atsInputFlowIndicator,'atsInputFlowTable':atsInputFlowTable,'atsInputFlowEntry':atsInputFlowEntry,_P:atsInputFlowIndex,'atsInputFlowRelay':atsInputFlowRelay,'atsInputFlowSCR':atsInputFlowSCR,'atsInputFlowParallelRelay':atsInputFlowParallelRelay,'atsInputFailureIndicator':atsInputFailureIndicator,'atsInputFailureTable':atsInputFailureTable,'atsInputFailureEntry':atsInputFailureEntry,_Q:atsInputFailureIndex,'atsInputFailureRelayOpen':atsInputFailureRelayOpen,'atsInputFailureRelayShort':atsInputFailureRelayShort,'atsInputFailureSCROpen':atsInputFailureSCROpen,'atsInputFailureSCRShort':atsInputFailureSCRShort,'atsInputFailureSCRThermal':atsInputFailureSCRThermal,'atsInputFailureAuxPower':atsInputFailureAuxPower,'atsInputFailureDrop':atsInputFailureDrop,'atsInputFailureBrownout':atsInputFailureBrownout,'atsInputFailureFrequency':atsInputFailureFrequency,'atsInputFailureNotOperable':atsInputFailureNotOperable,'atsFailureIndicator':atsFailureIndicator,'atsFailure':atsFailure,'atsFailureSwitchFault':atsFailureSwitchFault,'atsFailureNoOutput':atsFailureNoOutput,'atsFailureOutputOC':atsFailureOutputOC,'atsFailureOverTemperature':atsFailureOverTemperature,'atsLog':atsLog,'atsLogNum':atsLogNum,'atsLogTable':atsLogTable,'atsLogEntry':atsLogEntry,_R:atsLogIndex,'atsLogTime':atsLogTime,'atsLogCode':atsLogCode,'atsLogTimeText':atsLogTimeText,'atsConfig':atsConfig,'atsConfigTime':atsConfigTime,'atsConfigTimeRTC':atsConfigTimeRTC,'atsConfigTimeTextDate':atsConfigTimeTextDate,'atsConfigTimeTextTime':atsConfigTimeTextTime,'atsConfigInputTable':atsConfigInputTable,'atsConfigInputEntry':atsConfigInputEntry,_S:atsConfigInputIndex,'atsConfigInputTrip':atsConfigInputTrip,'atsConfigInputBrownoutLow':atsConfigInputBrownoutLow,'atsConfigInputBrownoutHigh':atsConfigInputBrownoutHigh,'atsConfigInputRecover':atsConfigInputRecover,'atsConfigInputMaxVoltage':atsConfigInputMaxVoltage,'atsConfigInputMaxTime':atsConfigInputMaxTime,'atsConfigInputDelayTime':atsConfigInputDelayTime,'atsConfigInputVoltageRating':atsConfigInputVoltageRating,'atsConfigRandomTime':atsConfigRandomTime,'atsConfigPreferred':atsConfigPreferred,'atsConfigSensitivity':atsConfigSensitivity,'atsConfigTest':atsConfigTest,'atsUpgrade':atsUpgrade,'atsUpgradeProcess':atsUpgradeProcess,'atsUpgradeStep':atsUpgradeStep,'atsUpgradePercentage':atsUpgradePercentage,'atsTraps':atsTraps,'atsTrapCommLost':atsTrapCommLost,'atsTrapCommEstablished':atsTrapCommEstablished,'atsTrapConfigChange':atsTrapConfigChange,'atsTrapFlowChange':atsTrapFlowChange,'atsTrapInput1Alarm':atsTrapInput1Alarm,'atsTrapInput1AlarmRecover':atsTrapInput1AlarmRecover,'atsTrapInput2Alarm':atsTrapInput2Alarm,'atsTrapInput2AlarmRecover':atsTrapInput2AlarmRecover,'atsTrapAlarm':atsTrapAlarm,'atsTrapAlarmRecover':atsTrapAlarmRecover,'atsTrapUpgradeBegin':atsTrapUpgradeBegin,'atsTrapUpgradeEnd':atsTrapUpgradeEnd})