_S='stsConfigInputIndex'
_R='stsLogIndex'
_Q='stsInputFailureIndex'
_P='stsInputFlowIndex'
_O='stsInputIndex'
_N='NotificationType'
_M='0.1 Second'
_L='off'
_K='source-2'
_J='source-1'
_I='0.1 V'
_H='DeltaSTS-MIB'
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
_Delta_ObjectIdentity=ObjectIdentity
delta=_Delta_ObjectIdentity((1,3,6,1,4,1,2254))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,2254,2))
_Sts_ObjectIdentity=ObjectIdentity
sts=_Sts_ObjectIdentity((1,3,6,1,4,1,2254,2,80))
_StsAgent_ObjectIdentity=ObjectIdentity
stsAgent=_StsAgent_ObjectIdentity((1,3,6,1,4,1,2254,2,80,1))
class _StsAgentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_StsAgentManufacturer_Type.__name__=_G
_StsAgentManufacturer_Object=MibScalar
stsAgentManufacturer=_StsAgentManufacturer_Object((1,3,6,1,4,1,2254,2,80,1,1),_StsAgentManufacturer_Type())
stsAgentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:stsAgentManufacturer.setStatus(_A)
class _StsAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_StsAgentVersion_Type.__name__=_G
_StsAgentVersion_Object=MibScalar
stsAgentVersion=_StsAgentVersion_Object((1,3,6,1,4,1,2254,2,80,1,2),_StsAgentVersion_Type())
stsAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:stsAgentVersion.setStatus(_A)
_StsAgentModbus_ObjectIdentity=ObjectIdentity
stsAgentModbus=_StsAgentModbus_ObjectIdentity((1,3,6,1,4,1,2254,2,80,1,3))
class _StsAgentModbusLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linked',1),('un-linked',2)))
_StsAgentModbusLink_Type.__name__=_C
_StsAgentModbusLink_Object=MibScalar
stsAgentModbusLink=_StsAgentModbusLink_Object((1,3,6,1,4,1,2254,2,80,1,3,1),_StsAgentModbusLink_Type())
stsAgentModbusLink.setMaxAccess(_B)
if mibBuilder.loadTexts:stsAgentModbusLink.setStatus(_A)
_StsIdent_ObjectIdentity=ObjectIdentity
stsIdent=_StsIdent_ObjectIdentity((1,3,6,1,4,1,2254,2,80,2))
class _StsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_StsIdentModel_Type.__name__=_G
_StsIdentModel_Object=MibScalar
stsIdentModel=_StsIdentModel_Object((1,3,6,1,4,1,2254,2,80,2,1),_StsIdentModel_Type())
stsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:stsIdentModel.setStatus(_A)
class _StsIdentFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_StsIdentFWVersion_Type.__name__=_G
_StsIdentFWVersion_Object=MibScalar
stsIdentFWVersion=_StsIdentFWVersion_Object((1,3,6,1,4,1,2254,2,80,2,2),_StsIdentFWVersion_Type())
stsIdentFWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:stsIdentFWVersion.setStatus(_A)
class _StsIdentRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_StsIdentRelease_Type.__name__=_G
_StsIdentRelease_Object=MibScalar
stsIdentRelease=_StsIdentRelease_Object((1,3,6,1,4,1,2254,2,80,2,3),_StsIdentRelease_Type())
stsIdentRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:stsIdentRelease.setStatus(_A)
class _StsIdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_StsIdentSerialNumber_Type.__name__=_G
_StsIdentSerialNumber_Object=MibScalar
stsIdentSerialNumber=_StsIdentSerialNumber_Object((1,3,6,1,4,1,2254,2,80,2,4),_StsIdentSerialNumber_Type())
stsIdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:stsIdentSerialNumber.setStatus(_A)
class _StsIdentIDCodes_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_StsIdentIDCodes_Type.__name__=_G
_StsIdentIDCodes_Object=MibScalar
stsIdentIDCodes=_StsIdentIDCodes_Object((1,3,6,1,4,1,2254,2,80,2,5),_StsIdentIDCodes_Type())
stsIdentIDCodes.setMaxAccess(_D)
if mibBuilder.loadTexts:stsIdentIDCodes.setStatus(_A)
_StsMeasure_ObjectIdentity=ObjectIdentity
stsMeasure=_StsMeasure_ObjectIdentity((1,3,6,1,4,1,2254,2,80,3))
_StsInputTable_Object=MibTable
stsInputTable=_StsInputTable_Object((1,3,6,1,4,1,2254,2,80,3,1))
if mibBuilder.loadTexts:stsInputTable.setStatus(_A)
_StsInputEntry_Object=MibTableRow
stsInputEntry=_StsInputEntry_Object((1,3,6,1,4,1,2254,2,80,3,1,1))
stsInputEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:stsInputEntry.setStatus(_A)
class _StsInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_StsInputIndex_Type.__name__=_C
_StsInputIndex_Object=MibTableColumn
stsInputIndex=_StsInputIndex_Object((1,3,6,1,4,1,2254,2,80,3,1,1,1),_StsInputIndex_Type())
stsInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputIndex.setStatus(_A)
_StsInputVoltage_Type=Integer32
_StsInputVoltage_Object=MibTableColumn
stsInputVoltage=_StsInputVoltage_Object((1,3,6,1,4,1,2254,2,80,3,1,1,2),_StsInputVoltage_Type())
stsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:stsInputVoltage.setUnits(_I)
_StsInputFrequency_Type=Integer32
_StsInputFrequency_Object=MibTableColumn
stsInputFrequency=_StsInputFrequency_Object((1,3,6,1,4,1,2254,2,80,3,1,1,3),_StsInputFrequency_Type())
stsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFrequency.setStatus(_A)
if mibBuilder.loadTexts:stsInputFrequency.setUnits('0.1 Hz')
_StsOutput_ObjectIdentity=ObjectIdentity
stsOutput=_StsOutput_ObjectIdentity((1,3,6,1,4,1,2254,2,80,3,2))
_StsOutputVoltage_Type=Integer32
_StsOutputVoltage_Object=MibScalar
stsOutputVoltage=_StsOutputVoltage_Object((1,3,6,1,4,1,2254,2,80,3,2,1),_StsOutputVoltage_Type())
stsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:stsOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:stsOutputVoltage.setUnits(_I)
_StsOutputCurrent_Type=Integer32
_StsOutputCurrent_Object=MibScalar
stsOutputCurrent=_StsOutputCurrent_Object((1,3,6,1,4,1,2254,2,80,3,2,2),_StsOutputCurrent_Type())
stsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:stsOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:stsOutputCurrent.setUnits('0.1 A')
_StsMeasureTemperatureC_Type=Integer32
_StsMeasureTemperatureC_Object=MibScalar
stsMeasureTemperatureC=_StsMeasureTemperatureC_Object((1,3,6,1,4,1,2254,2,80,3,3),_StsMeasureTemperatureC_Type())
stsMeasureTemperatureC.setMaxAccess(_B)
if mibBuilder.loadTexts:stsMeasureTemperatureC.setStatus(_A)
if mibBuilder.loadTexts:stsMeasureTemperatureC.setUnits('1 Celsius')
_StsMeasureTemperatureF_Type=Integer32
_StsMeasureTemperatureF_Object=MibScalar
stsMeasureTemperatureF=_StsMeasureTemperatureF_Object((1,3,6,1,4,1,2254,2,80,3,4),_StsMeasureTemperatureF_Type())
stsMeasureTemperatureF.setMaxAccess(_B)
if mibBuilder.loadTexts:stsMeasureTemperatureF.setStatus(_A)
if mibBuilder.loadTexts:stsMeasureTemperatureF.setUnits('1 Fahrenheit')
_StsMessureRunTime_Type=Integer32
_StsMessureRunTime_Object=MibScalar
stsMessureRunTime=_StsMessureRunTime_Object((1,3,6,1,4,1,2254,2,80,3,5),_StsMessureRunTime_Type())
stsMessureRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stsMessureRunTime.setStatus(_A)
if mibBuilder.loadTexts:stsMessureRunTime.setUnits('1 second')
_StsMessureTransferedTimes_Type=Integer32
_StsMessureTransferedTimes_Object=MibScalar
stsMessureTransferedTimes=_StsMessureTransferedTimes_Object((1,3,6,1,4,1,2254,2,80,3,6),_StsMessureTransferedTimes_Type())
stsMessureTransferedTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:stsMessureTransferedTimes.setStatus(_A)
class _StsMessureOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('initialization',1),('diagnosis',2),(_L,3),(_J,4),(_K,5),('safe',6),('fault',7)))
_StsMessureOperationMode_Type.__name__=_C
_StsMessureOperationMode_Object=MibScalar
stsMessureOperationMode=_StsMessureOperationMode_Object((1,3,6,1,4,1,2254,2,80,3,7),_StsMessureOperationMode_Type())
stsMessureOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:stsMessureOperationMode.setStatus(_A)
_StsStatus_ObjectIdentity=ObjectIdentity
stsStatus=_StsStatus_ObjectIdentity((1,3,6,1,4,1,2254,2,80,4))
_StsInputFlowIndicator_Type=Integer32
_StsInputFlowIndicator_Object=MibScalar
stsInputFlowIndicator=_StsInputFlowIndicator_Object((1,3,6,1,4,1,2254,2,80,4,1),_StsInputFlowIndicator_Type())
stsInputFlowIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFlowIndicator.setStatus(_A)
_StsInputFlowTable_Object=MibTable
stsInputFlowTable=_StsInputFlowTable_Object((1,3,6,1,4,1,2254,2,80,4,2))
if mibBuilder.loadTexts:stsInputFlowTable.setStatus(_A)
_StsInputFlowEntry_Object=MibTableRow
stsInputFlowEntry=_StsInputFlowEntry_Object((1,3,6,1,4,1,2254,2,80,4,2,1))
stsInputFlowEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:stsInputFlowEntry.setStatus(_A)
class _StsInputFlowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_StsInputFlowIndex_Type.__name__=_C
_StsInputFlowIndex_Object=MibTableColumn
stsInputFlowIndex=_StsInputFlowIndex_Object((1,3,6,1,4,1,2254,2,80,4,2,1,1),_StsInputFlowIndex_Type())
stsInputFlowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFlowIndex.setStatus(_A)
class _StsInputFlowRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_StsInputFlowRelay_Type.__name__=_C
_StsInputFlowRelay_Object=MibTableColumn
stsInputFlowRelay=_StsInputFlowRelay_Object((1,3,6,1,4,1,2254,2,80,4,2,1,2),_StsInputFlowRelay_Type())
stsInputFlowRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFlowRelay.setStatus(_A)
class _StsInputFlowSCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_StsInputFlowSCR_Type.__name__=_C
_StsInputFlowSCR_Object=MibTableColumn
stsInputFlowSCR=_StsInputFlowSCR_Object((1,3,6,1,4,1,2254,2,80,4,2,1,3),_StsInputFlowSCR_Type())
stsInputFlowSCR.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFlowSCR.setStatus(_A)
class _StsInputFlowParallelRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_L,2)))
_StsInputFlowParallelRelay_Type.__name__=_C
_StsInputFlowParallelRelay_Object=MibTableColumn
stsInputFlowParallelRelay=_StsInputFlowParallelRelay_Object((1,3,6,1,4,1,2254,2,80,4,2,1,4),_StsInputFlowParallelRelay_Type())
stsInputFlowParallelRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFlowParallelRelay.setStatus(_A)
_StsInputFailureIndicator_Type=Integer32
_StsInputFailureIndicator_Object=MibScalar
stsInputFailureIndicator=_StsInputFailureIndicator_Object((1,3,6,1,4,1,2254,2,80,4,3),_StsInputFailureIndicator_Type())
stsInputFailureIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureIndicator.setStatus(_A)
_StsInputFailureTable_Object=MibTable
stsInputFailureTable=_StsInputFailureTable_Object((1,3,6,1,4,1,2254,2,80,4,4))
if mibBuilder.loadTexts:stsInputFailureTable.setStatus(_A)
_StsInputFailureEntry_Object=MibTableRow
stsInputFailureEntry=_StsInputFailureEntry_Object((1,3,6,1,4,1,2254,2,80,4,4,1))
stsInputFailureEntry.setIndexNames((0,_H,_Q))
if mibBuilder.loadTexts:stsInputFailureEntry.setStatus(_A)
class _StsInputFailureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_StsInputFailureIndex_Type.__name__=_C
_StsInputFailureIndex_Object=MibTableColumn
stsInputFailureIndex=_StsInputFailureIndex_Object((1,3,6,1,4,1,2254,2,80,4,4,1,1),_StsInputFailureIndex_Type())
stsInputFailureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureIndex.setStatus(_A)
class _StsInputFailureRelayOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureRelayOpen_Type.__name__=_C
_StsInputFailureRelayOpen_Object=MibTableColumn
stsInputFailureRelayOpen=_StsInputFailureRelayOpen_Object((1,3,6,1,4,1,2254,2,80,4,4,1,2),_StsInputFailureRelayOpen_Type())
stsInputFailureRelayOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureRelayOpen.setStatus(_A)
class _StsInputFailureRelayShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureRelayShort_Type.__name__=_C
_StsInputFailureRelayShort_Object=MibTableColumn
stsInputFailureRelayShort=_StsInputFailureRelayShort_Object((1,3,6,1,4,1,2254,2,80,4,4,1,3),_StsInputFailureRelayShort_Type())
stsInputFailureRelayShort.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureRelayShort.setStatus(_A)
class _StsInputFailureSCROpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureSCROpen_Type.__name__=_C
_StsInputFailureSCROpen_Object=MibTableColumn
stsInputFailureSCROpen=_StsInputFailureSCROpen_Object((1,3,6,1,4,1,2254,2,80,4,4,1,4),_StsInputFailureSCROpen_Type())
stsInputFailureSCROpen.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureSCROpen.setStatus(_A)
class _StsInputFailureSCRShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureSCRShort_Type.__name__=_C
_StsInputFailureSCRShort_Object=MibTableColumn
stsInputFailureSCRShort=_StsInputFailureSCRShort_Object((1,3,6,1,4,1,2254,2,80,4,4,1,5),_StsInputFailureSCRShort_Type())
stsInputFailureSCRShort.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureSCRShort.setStatus(_A)
class _StsInputFailureSCRThermal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureSCRThermal_Type.__name__=_C
_StsInputFailureSCRThermal_Object=MibTableColumn
stsInputFailureSCRThermal=_StsInputFailureSCRThermal_Object((1,3,6,1,4,1,2254,2,80,4,4,1,6),_StsInputFailureSCRThermal_Type())
stsInputFailureSCRThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureSCRThermal.setStatus(_A)
class _StsInputFailureAuxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureAuxPower_Type.__name__=_C
_StsInputFailureAuxPower_Object=MibTableColumn
stsInputFailureAuxPower=_StsInputFailureAuxPower_Object((1,3,6,1,4,1,2254,2,80,4,4,1,7),_StsInputFailureAuxPower_Type())
stsInputFailureAuxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureAuxPower.setStatus(_A)
class _StsInputFailureDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureDrop_Type.__name__=_C
_StsInputFailureDrop_Object=MibTableColumn
stsInputFailureDrop=_StsInputFailureDrop_Object((1,3,6,1,4,1,2254,2,80,4,4,1,8),_StsInputFailureDrop_Type())
stsInputFailureDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureDrop.setStatus(_A)
class _StsInputFailureBrownout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureBrownout_Type.__name__=_C
_StsInputFailureBrownout_Object=MibTableColumn
stsInputFailureBrownout=_StsInputFailureBrownout_Object((1,3,6,1,4,1,2254,2,80,4,4,1,9),_StsInputFailureBrownout_Type())
stsInputFailureBrownout.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureBrownout.setStatus(_A)
class _StsInputFailureFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureFrequency_Type.__name__=_C
_StsInputFailureFrequency_Object=MibTableColumn
stsInputFailureFrequency=_StsInputFailureFrequency_Object((1,3,6,1,4,1,2254,2,80,4,4,1,10),_StsInputFailureFrequency_Type())
stsInputFailureFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureFrequency.setStatus(_A)
class _StsInputFailureNotOperable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsInputFailureNotOperable_Type.__name__=_C
_StsInputFailureNotOperable_Object=MibTableColumn
stsInputFailureNotOperable=_StsInputFailureNotOperable_Object((1,3,6,1,4,1,2254,2,80,4,4,1,11),_StsInputFailureNotOperable_Type())
stsInputFailureNotOperable.setMaxAccess(_B)
if mibBuilder.loadTexts:stsInputFailureNotOperable.setStatus(_A)
_StsFailureIndicator_Type=Integer32
_StsFailureIndicator_Object=MibScalar
stsFailureIndicator=_StsFailureIndicator_Object((1,3,6,1,4,1,2254,2,80,4,5),_StsFailureIndicator_Type())
stsFailureIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:stsFailureIndicator.setStatus(_A)
_StsFailure_ObjectIdentity=ObjectIdentity
stsFailure=_StsFailure_ObjectIdentity((1,3,6,1,4,1,2254,2,80,4,6))
class _StsFailureSwitchFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsFailureSwitchFault_Type.__name__=_C
_StsFailureSwitchFault_Object=MibScalar
stsFailureSwitchFault=_StsFailureSwitchFault_Object((1,3,6,1,4,1,2254,2,80,4,6,1),_StsFailureSwitchFault_Type())
stsFailureSwitchFault.setMaxAccess(_B)
if mibBuilder.loadTexts:stsFailureSwitchFault.setStatus(_A)
class _StsFailureNoOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsFailureNoOutput_Type.__name__=_C
_StsFailureNoOutput_Object=MibScalar
stsFailureNoOutput=_StsFailureNoOutput_Object((1,3,6,1,4,1,2254,2,80,4,6,2),_StsFailureNoOutput_Type())
stsFailureNoOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:stsFailureNoOutput.setStatus(_A)
class _StsFailureOutputOC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsFailureOutputOC_Type.__name__=_C
_StsFailureOutputOC_Object=MibScalar
stsFailureOutputOC=_StsFailureOutputOC_Object((1,3,6,1,4,1,2254,2,80,4,6,3),_StsFailureOutputOC_Type())
stsFailureOutputOC.setMaxAccess(_B)
if mibBuilder.loadTexts:stsFailureOutputOC.setStatus(_A)
class _StsFailureOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_StsFailureOverTemperature_Type.__name__=_C
_StsFailureOverTemperature_Object=MibScalar
stsFailureOverTemperature=_StsFailureOverTemperature_Object((1,3,6,1,4,1,2254,2,80,4,6,4),_StsFailureOverTemperature_Type())
stsFailureOverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:stsFailureOverTemperature.setStatus(_A)
_StsLog_ObjectIdentity=ObjectIdentity
stsLog=_StsLog_ObjectIdentity((1,3,6,1,4,1,2254,2,80,5))
_StsLogNum_Type=Integer32
_StsLogNum_Object=MibScalar
stsLogNum=_StsLogNum_Object((1,3,6,1,4,1,2254,2,80,5,1),_StsLogNum_Type())
stsLogNum.setMaxAccess(_B)
if mibBuilder.loadTexts:stsLogNum.setStatus(_A)
_StsLogTable_Object=MibTable
stsLogTable=_StsLogTable_Object((1,3,6,1,4,1,2254,2,80,5,2))
if mibBuilder.loadTexts:stsLogTable.setStatus(_A)
_StsLogEntry_Object=MibTableRow
stsLogEntry=_StsLogEntry_Object((1,3,6,1,4,1,2254,2,80,5,2,1))
stsLogEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:stsLogEntry.setStatus(_A)
class _StsLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StsLogIndex_Type.__name__=_C
_StsLogIndex_Object=MibTableColumn
stsLogIndex=_StsLogIndex_Object((1,3,6,1,4,1,2254,2,80,5,2,1,1),_StsLogIndex_Type())
stsLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stsLogIndex.setStatus(_A)
_StsLogTime_Type=TimeTicks
_StsLogTime_Object=MibTableColumn
stsLogTime=_StsLogTime_Object((1,3,6,1,4,1,2254,2,80,5,2,1,2),_StsLogTime_Type())
stsLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stsLogTime.setStatus(_A)
if mibBuilder.loadTexts:stsLogTime.setUnits('1 Second')
_StsLogCode_Type=Integer32
_StsLogCode_Object=MibTableColumn
stsLogCode=_StsLogCode_Object((1,3,6,1,4,1,2254,2,80,5,2,1,3),_StsLogCode_Type())
stsLogCode.setMaxAccess(_B)
if mibBuilder.loadTexts:stsLogCode.setStatus(_A)
class _StsLogTimeText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_StsLogTimeText_Type.__name__=_G
_StsLogTimeText_Object=MibTableColumn
stsLogTimeText=_StsLogTimeText_Object((1,3,6,1,4,1,2254,2,80,5,2,1,4),_StsLogTimeText_Type())
stsLogTimeText.setMaxAccess(_B)
if mibBuilder.loadTexts:stsLogTimeText.setStatus(_A)
_StsConfig_ObjectIdentity=ObjectIdentity
stsConfig=_StsConfig_ObjectIdentity((1,3,6,1,4,1,2254,2,80,6))
_StsConfigTime_ObjectIdentity=ObjectIdentity
stsConfigTime=_StsConfigTime_ObjectIdentity((1,3,6,1,4,1,2254,2,80,6,1))
_StsConfigTimeRTC_Type=Integer32
_StsConfigTimeRTC_Object=MibScalar
stsConfigTimeRTC=_StsConfigTimeRTC_Object((1,3,6,1,4,1,2254,2,80,6,1,1),_StsConfigTimeRTC_Type())
stsConfigTimeRTC.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigTimeRTC.setStatus(_A)
class _StsConfigTimeTextDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_StsConfigTimeTextDate_Type.__name__=_G
_StsConfigTimeTextDate_Object=MibScalar
stsConfigTimeTextDate=_StsConfigTimeTextDate_Object((1,3,6,1,4,1,2254,2,80,6,1,2),_StsConfigTimeTextDate_Type())
stsConfigTimeTextDate.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigTimeTextDate.setStatus(_A)
class _StsConfigTimeTextTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_StsConfigTimeTextTime_Type.__name__=_G
_StsConfigTimeTextTime_Object=MibScalar
stsConfigTimeTextTime=_StsConfigTimeTextTime_Object((1,3,6,1,4,1,2254,2,80,6,1,3),_StsConfigTimeTextTime_Type())
stsConfigTimeTextTime.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigTimeTextTime.setStatus(_A)
_StsConfigInputTable_Object=MibTable
stsConfigInputTable=_StsConfigInputTable_Object((1,3,6,1,4,1,2254,2,80,6,2))
if mibBuilder.loadTexts:stsConfigInputTable.setStatus(_A)
_StsConfigInputEntry_Object=MibTableRow
stsConfigInputEntry=_StsConfigInputEntry_Object((1,3,6,1,4,1,2254,2,80,6,2,1))
stsConfigInputEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:stsConfigInputEntry.setStatus(_A)
class _StsConfigInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_StsConfigInputIndex_Type.__name__=_C
_StsConfigInputIndex_Object=MibTableColumn
stsConfigInputIndex=_StsConfigInputIndex_Object((1,3,6,1,4,1,2254,2,80,6,2,1,1),_StsConfigInputIndex_Type())
stsConfigInputIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputIndex.setStatus(_A)
_StsConfigInputTrip_Type=Integer32
_StsConfigInputTrip_Object=MibTableColumn
stsConfigInputTrip=_StsConfigInputTrip_Object((1,3,6,1,4,1,2254,2,80,6,2,1,2),_StsConfigInputTrip_Type())
stsConfigInputTrip.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputTrip.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputTrip.setUnits(_I)
_StsConfigInputBrownoutLow_Type=Integer32
_StsConfigInputBrownoutLow_Object=MibTableColumn
stsConfigInputBrownoutLow=_StsConfigInputBrownoutLow_Object((1,3,6,1,4,1,2254,2,80,6,2,1,3),_StsConfigInputBrownoutLow_Type())
stsConfigInputBrownoutLow.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputBrownoutLow.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputBrownoutLow.setUnits(_I)
_StsConfigInputBrownoutHigh_Type=Integer32
_StsConfigInputBrownoutHigh_Object=MibTableColumn
stsConfigInputBrownoutHigh=_StsConfigInputBrownoutHigh_Object((1,3,6,1,4,1,2254,2,80,6,2,1,4),_StsConfigInputBrownoutHigh_Type())
stsConfigInputBrownoutHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputBrownoutHigh.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputBrownoutHigh.setUnits(_I)
_StsConfigInputRecover_Type=Integer32
_StsConfigInputRecover_Object=MibTableColumn
stsConfigInputRecover=_StsConfigInputRecover_Object((1,3,6,1,4,1,2254,2,80,6,2,1,5),_StsConfigInputRecover_Type())
stsConfigInputRecover.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputRecover.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputRecover.setUnits(_M)
_StsConfigInputMaxVoltage_Type=Integer32
_StsConfigInputMaxVoltage_Object=MibTableColumn
stsConfigInputMaxVoltage=_StsConfigInputMaxVoltage_Object((1,3,6,1,4,1,2254,2,80,6,2,1,6),_StsConfigInputMaxVoltage_Type())
stsConfigInputMaxVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputMaxVoltage.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputMaxVoltage.setUnits('1 V')
_StsConfigInputMaxTime_Type=Integer32
_StsConfigInputMaxTime_Object=MibTableColumn
stsConfigInputMaxTime=_StsConfigInputMaxTime_Object((1,3,6,1,4,1,2254,2,80,6,2,1,7),_StsConfigInputMaxTime_Type())
stsConfigInputMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigInputMaxTime.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputMaxTime.setUnits(_M)
_StsConfigInputDelayTime_Type=Integer32
_StsConfigInputDelayTime_Object=MibTableColumn
stsConfigInputDelayTime=_StsConfigInputDelayTime_Object((1,3,6,1,4,1,2254,2,80,6,2,1,8),_StsConfigInputDelayTime_Type())
stsConfigInputDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stsConfigInputDelayTime.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputDelayTime.setUnits(_M)
_StsConfigInputVoltageRating_Type=Integer32
_StsConfigInputVoltageRating_Object=MibScalar
stsConfigInputVoltageRating=_StsConfigInputVoltageRating_Object((1,3,6,1,4,1,2254,2,80,6,3),_StsConfigInputVoltageRating_Type())
stsConfigInputVoltageRating.setMaxAccess(_B)
if mibBuilder.loadTexts:stsConfigInputVoltageRating.setStatus(_A)
if mibBuilder.loadTexts:stsConfigInputVoltageRating.setUnits(_I)
_StsConfigRandomTime_Type=Integer32
_StsConfigRandomTime_Object=MibScalar
stsConfigRandomTime=_StsConfigRandomTime_Object((1,3,6,1,4,1,2254,2,80,6,4),_StsConfigRandomTime_Type())
stsConfigRandomTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stsConfigRandomTime.setStatus(_A)
if mibBuilder.loadTexts:stsConfigRandomTime.setUnits(_M)
class _StsConfigPreferred_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_StsConfigPreferred_Type.__name__=_C
_StsConfigPreferred_Object=MibScalar
stsConfigPreferred=_StsConfigPreferred_Object((1,3,6,1,4,1,2254,2,80,6,5),_StsConfigPreferred_Type())
stsConfigPreferred.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigPreferred.setStatus(_A)
class _StsConfigSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_StsConfigSensitivity_Type.__name__=_C
_StsConfigSensitivity_Object=MibScalar
stsConfigSensitivity=_StsConfigSensitivity_Object((1,3,6,1,4,1,2254,2,80,6,6),_StsConfigSensitivity_Type())
stsConfigSensitivity.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigSensitivity.setStatus(_A)
class _StsConfigTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_StsConfigTest_Type.__name__=_C
_StsConfigTest_Object=MibScalar
stsConfigTest=_StsConfigTest_Object((1,3,6,1,4,1,2254,2,80,6,7),_StsConfigTest_Type())
stsConfigTest.setMaxAccess(_D)
if mibBuilder.loadTexts:stsConfigTest.setStatus(_A)
_StsUpgrade_ObjectIdentity=ObjectIdentity
stsUpgrade=_StsUpgrade_ObjectIdentity((1,3,6,1,4,1,2254,2,80,7))
class _StsUpgradeProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('run',2),('error',3)))
_StsUpgradeProcess_Type.__name__=_C
_StsUpgradeProcess_Object=MibScalar
stsUpgradeProcess=_StsUpgradeProcess_Object((1,3,6,1,4,1,2254,2,80,7,1),_StsUpgradeProcess_Type())
stsUpgradeProcess.setMaxAccess(_B)
if mibBuilder.loadTexts:stsUpgradeProcess.setStatus(_A)
class _StsUpgradeStep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('fileid',2),('auth',3),('addr',4),('erase',5),('program',6),('read',7)))
_StsUpgradeStep_Type.__name__=_C
_StsUpgradeStep_Object=MibScalar
stsUpgradeStep=_StsUpgradeStep_Object((1,3,6,1,4,1,2254,2,80,7,2),_StsUpgradeStep_Type())
stsUpgradeStep.setMaxAccess(_B)
if mibBuilder.loadTexts:stsUpgradeStep.setStatus(_A)
_StsUpgradePercentage_Type=Integer32
_StsUpgradePercentage_Object=MibScalar
stsUpgradePercentage=_StsUpgradePercentage_Object((1,3,6,1,4,1,2254,2,80,7,3),_StsUpgradePercentage_Type())
stsUpgradePercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:stsUpgradePercentage.setStatus(_A)
if mibBuilder.loadTexts:stsUpgradePercentage.setUnits('0.1%')
_StsTraps_ObjectIdentity=ObjectIdentity
stsTraps=_StsTraps_ObjectIdentity((1,3,6,1,4,1,2254,2,80,20))
stsTrapCommLost=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,1))
if mibBuilder.loadTexts:stsTrapCommLost.setStatus('')
stsTrapCommEstablished=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,2))
if mibBuilder.loadTexts:stsTrapCommEstablished.setStatus('')
stsTrapConfigChange=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,3))
if mibBuilder.loadTexts:stsTrapConfigChange.setStatus('')
stsTrapFlowChange=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,4))
if mibBuilder.loadTexts:stsTrapFlowChange.setStatus('')
stsTrapInput1Alarm=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,5))
if mibBuilder.loadTexts:stsTrapInput1Alarm.setStatus('')
stsTrapInput1AlarmRecover=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,6))
if mibBuilder.loadTexts:stsTrapInput1AlarmRecover.setStatus('')
stsTrapInput2Alarm=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,7))
if mibBuilder.loadTexts:stsTrapInput2Alarm.setStatus('')
stsTrapInput2AlarmRecover=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,8))
if mibBuilder.loadTexts:stsTrapInput2AlarmRecover.setStatus('')
stsTrapAlarm=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,9))
if mibBuilder.loadTexts:stsTrapAlarm.setStatus('')
stsTrapAlarmRecover=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,10))
if mibBuilder.loadTexts:stsTrapAlarmRecover.setStatus('')
stsTrapUpgradeBegin=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,11))
if mibBuilder.loadTexts:stsTrapUpgradeBegin.setStatus('')
stsTrapUpgradeEnd=NotificationType((1,3,6,1,4,1,2254,2,80,20,0,12))
if mibBuilder.loadTexts:stsTrapUpgradeEnd.setStatus('')
mibBuilder.exportSymbols(_H,**{'delta':delta,'ups':ups,'sts':sts,'stsAgent':stsAgent,'stsAgentManufacturer':stsAgentManufacturer,'stsAgentVersion':stsAgentVersion,'stsAgentModbus':stsAgentModbus,'stsAgentModbusLink':stsAgentModbusLink,'stsIdent':stsIdent,'stsIdentModel':stsIdentModel,'stsIdentFWVersion':stsIdentFWVersion,'stsIdentRelease':stsIdentRelease,'stsIdentSerialNumber':stsIdentSerialNumber,'stsIdentIDCodes':stsIdentIDCodes,'stsMeasure':stsMeasure,'stsInputTable':stsInputTable,'stsInputEntry':stsInputEntry,_O:stsInputIndex,'stsInputVoltage':stsInputVoltage,'stsInputFrequency':stsInputFrequency,'stsOutput':stsOutput,'stsOutputVoltage':stsOutputVoltage,'stsOutputCurrent':stsOutputCurrent,'stsMeasureTemperatureC':stsMeasureTemperatureC,'stsMeasureTemperatureF':stsMeasureTemperatureF,'stsMessureRunTime':stsMessureRunTime,'stsMessureTransferedTimes':stsMessureTransferedTimes,'stsMessureOperationMode':stsMessureOperationMode,'stsStatus':stsStatus,'stsInputFlowIndicator':stsInputFlowIndicator,'stsInputFlowTable':stsInputFlowTable,'stsInputFlowEntry':stsInputFlowEntry,_P:stsInputFlowIndex,'stsInputFlowRelay':stsInputFlowRelay,'stsInputFlowSCR':stsInputFlowSCR,'stsInputFlowParallelRelay':stsInputFlowParallelRelay,'stsInputFailureIndicator':stsInputFailureIndicator,'stsInputFailureTable':stsInputFailureTable,'stsInputFailureEntry':stsInputFailureEntry,_Q:stsInputFailureIndex,'stsInputFailureRelayOpen':stsInputFailureRelayOpen,'stsInputFailureRelayShort':stsInputFailureRelayShort,'stsInputFailureSCROpen':stsInputFailureSCROpen,'stsInputFailureSCRShort':stsInputFailureSCRShort,'stsInputFailureSCRThermal':stsInputFailureSCRThermal,'stsInputFailureAuxPower':stsInputFailureAuxPower,'stsInputFailureDrop':stsInputFailureDrop,'stsInputFailureBrownout':stsInputFailureBrownout,'stsInputFailureFrequency':stsInputFailureFrequency,'stsInputFailureNotOperable':stsInputFailureNotOperable,'stsFailureIndicator':stsFailureIndicator,'stsFailure':stsFailure,'stsFailureSwitchFault':stsFailureSwitchFault,'stsFailureNoOutput':stsFailureNoOutput,'stsFailureOutputOC':stsFailureOutputOC,'stsFailureOverTemperature':stsFailureOverTemperature,'stsLog':stsLog,'stsLogNum':stsLogNum,'stsLogTable':stsLogTable,'stsLogEntry':stsLogEntry,_R:stsLogIndex,'stsLogTime':stsLogTime,'stsLogCode':stsLogCode,'stsLogTimeText':stsLogTimeText,'stsConfig':stsConfig,'stsConfigTime':stsConfigTime,'stsConfigTimeRTC':stsConfigTimeRTC,'stsConfigTimeTextDate':stsConfigTimeTextDate,'stsConfigTimeTextTime':stsConfigTimeTextTime,'stsConfigInputTable':stsConfigInputTable,'stsConfigInputEntry':stsConfigInputEntry,_S:stsConfigInputIndex,'stsConfigInputTrip':stsConfigInputTrip,'stsConfigInputBrownoutLow':stsConfigInputBrownoutLow,'stsConfigInputBrownoutHigh':stsConfigInputBrownoutHigh,'stsConfigInputRecover':stsConfigInputRecover,'stsConfigInputMaxVoltage':stsConfigInputMaxVoltage,'stsConfigInputMaxTime':stsConfigInputMaxTime,'stsConfigInputDelayTime':stsConfigInputDelayTime,'stsConfigInputVoltageRating':stsConfigInputVoltageRating,'stsConfigRandomTime':stsConfigRandomTime,'stsConfigPreferred':stsConfigPreferred,'stsConfigSensitivity':stsConfigSensitivity,'stsConfigTest':stsConfigTest,'stsUpgrade':stsUpgrade,'stsUpgradeProcess':stsUpgradeProcess,'stsUpgradeStep':stsUpgradeStep,'stsUpgradePercentage':stsUpgradePercentage,'stsTraps':stsTraps,'stsTrapCommLost':stsTrapCommLost,'stsTrapCommEstablished':stsTrapCommEstablished,'stsTrapConfigChange':stsTrapConfigChange,'stsTrapFlowChange':stsTrapFlowChange,'stsTrapInput1Alarm':stsTrapInput1Alarm,'stsTrapInput1AlarmRecover':stsTrapInput1AlarmRecover,'stsTrapInput2Alarm':stsTrapInput2Alarm,'stsTrapInput2AlarmRecover':stsTrapInput2AlarmRecover,'stsTrapAlarm':stsTrapAlarm,'stsTrapAlarmRecover':stsTrapAlarmRecover,'stsTrapUpgradeBegin':stsTrapUpgradeBegin,'stsTrapUpgradeEnd':stsTrapUpgradeEnd})