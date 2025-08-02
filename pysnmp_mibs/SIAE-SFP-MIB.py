_L='sfpPhysicalQuantity'
_K='microWatts (uW)'
_J='DisplayString'
_I='sfpModuleId'
_H='read-write'
_G='SIAE-SFP-MIB'
_F='Integer32'
_E='AlarmSeverityCode'
_D='OctetString'
_C='Bits'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_E,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_C,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention','TruthValue')
sfp=ModuleIdentity((1,3,6,1,4,1,3373,1103,74))
if mibBuilder.loadTexts:sfp.setRevisions(('2016-12-15 00:00','2016-09-29 00:00','2014-02-03 00:00','2013-12-05 00:00'))
class Temperature(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,2000))
class PhysicalQuantity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('phyQtTemperature',1),('phyQtVoltage',2),('phyQtTxBias',3),('phyQtTxPower',4),('phyQtRxPower',5)))
class _SfpMibVersion_Type(Integer32):defaultValue=1
_SfpMibVersion_Type.__name__=_F
_SfpMibVersion_Object=MibScalar
sfpMibVersion=_SfpMibVersion_Object((1,3,6,1,4,1,3373,1103,74,1),_SfpMibVersion_Type())
sfpMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpMibVersion.setStatus(_A)
_SfpSerialIdTable_Object=MibTable
sfpSerialIdTable=_SfpSerialIdTable_Object((1,3,6,1,4,1,3373,1103,74,2))
if mibBuilder.loadTexts:sfpSerialIdTable.setStatus(_A)
_SfpSerialIdEntry_Object=MibTableRow
sfpSerialIdEntry=_SfpSerialIdEntry_Object((1,3,6,1,4,1,3373,1103,74,2,1))
sfpSerialIdEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:sfpSerialIdEntry.setStatus(_A)
_SfpModuleId_Type=Integer32
_SfpModuleId_Object=MibTableColumn
sfpModuleId=_SfpModuleId_Object((1,3,6,1,4,1,3373,1103,74,2,1,1),_SfpModuleId_Type())
sfpModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpModuleId.setStatus(_A)
_SfpSerialIdValid_Type=TruthValue
_SfpSerialIdValid_Object=MibTableColumn
sfpSerialIdValid=_SfpSerialIdValid_Object((1,3,6,1,4,1,3373,1103,74,2,1,2),_SfpSerialIdValid_Type())
sfpSerialIdValid.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpSerialIdValid.setStatus(_A)
class _SfpVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorName_Type.__name__=_D
_SfpVendorName_Object=MibTableColumn
sfpVendorName=_SfpVendorName_Object((1,3,6,1,4,1,3373,1103,74,2,1,3),_SfpVendorName_Type())
sfpVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVendorName.setStatus(_A)
class _SfpVendorPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorPartNumber_Type.__name__=_D
_SfpVendorPartNumber_Object=MibTableColumn
sfpVendorPartNumber=_SfpVendorPartNumber_Object((1,3,6,1,4,1,3373,1103,74,2,1,4),_SfpVendorPartNumber_Type())
sfpVendorPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVendorPartNumber.setStatus(_A)
class _SfpVendorRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_SfpVendorRev_Type.__name__=_D
_SfpVendorRev_Object=MibTableColumn
sfpVendorRev=_SfpVendorRev_Object((1,3,6,1,4,1,3373,1103,74,2,1,5),_SfpVendorRev_Type())
sfpVendorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVendorRev.setStatus(_A)
class _SfpVendorSN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorSN_Type.__name__=_D
_SfpVendorSN_Object=MibTableColumn
sfpVendorSN=_SfpVendorSN_Object((1,3,6,1,4,1,3373,1103,74,2,1,6),_SfpVendorSN_Type())
sfpVendorSN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVendorSN.setStatus(_A)
class _SfpVendorDateCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SfpVendorDateCode_Type.__name__=_D
_SfpVendorDateCode_Object=MibTableColumn
sfpVendorDateCode=_SfpVendorDateCode_Object((1,3,6,1,4,1,3373,1103,74,2,1,7),_SfpVendorDateCode_Type())
sfpVendorDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVendorDateCode.setStatus(_A)
class _SfpDiagMonitorCode_Type(Bits):namedValues=NamedValues(*(('sfpDMCtypeLegacy',0),('sfpDMCtypeImplemented',1),('sfpDMCtypeInternalCal',2),('sfpDMCtypeExternalCal',3),('sfpDMCtypeRxAvgPwr',4),('sfpDMCtypeAddrChngReqrd',5)))
_SfpDiagMonitorCode_Type.__name__=_C
_SfpDiagMonitorCode_Object=MibTableColumn
sfpDiagMonitorCode=_SfpDiagMonitorCode_Object((1,3,6,1,4,1,3373,1103,74,2,1,8),_SfpDiagMonitorCode_Type())
sfpDiagMonitorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagMonitorCode.setStatus(_A)
class _SfpEnhancedOptionsCode_Type(Bits):namedValues=NamedValues(*(('sfpEOCalarmsImplemented',0),('sfpEOCSoftTxDisable',1),('sfpEOCSoftTxFault',2),('sfpEOCSoftRxLOS',3),('sfpEOCSoftRateSelect',4)))
_SfpEnhancedOptionsCode_Type.__name__=_C
_SfpEnhancedOptionsCode_Object=MibTableColumn
sfpEnhancedOptionsCode=_SfpEnhancedOptionsCode_Object((1,3,6,1,4,1,3373,1103,74,2,1,9),_SfpEnhancedOptionsCode_Type())
sfpEnhancedOptionsCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpEnhancedOptionsCode.setStatus(_A)
class _SfpOptions_Type(Bits):namedValues=NamedValues(*(('sfpOPTRateSelect',0),('sfpOPTTxDisable',1),('sfpOPTTxFault',2),('sfpOPTInvertedLOS',3),('sfpOPTlos',4)))
_SfpOptions_Type.__name__=_C
_SfpOptions_Object=MibTableColumn
sfpOptions=_SfpOptions_Object((1,3,6,1,4,1,3373,1103,74,2,1,10),_SfpOptions_Type())
sfpOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpOptions.setStatus(_A)
class _SfpFibreChannelMedia_Type(Bits):namedValues=NamedValues(*(('sfpMultiMode62u5',0),('sfpMultiMode50u0',1),('sfpSingleMode',2),('sfpTwistedAxialPair',3),('sfpShieldedTwistedPair',4),('sfpMiniatureCoax',5),('sfpVideoCoax',6)))
_SfpFibreChannelMedia_Type.__name__=_C
_SfpFibreChannelMedia_Object=MibTableColumn
sfpFibreChannelMedia=_SfpFibreChannelMedia_Object((1,3,6,1,4,1,3373,1103,74,2,1,11),_SfpFibreChannelMedia_Type())
sfpFibreChannelMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpFibreChannelMedia.setStatus(_A)
class _SfpCompliance_Type(Bits):namedValues=NamedValues(*(('sfpSonetReachSpecifier1',0),('sfpSonetReachSpecifier2',1),('sfpSonetOC48LongReach',2),('sfpSonetOC48IntermediateReach',3),('sfpSonetOC48ShortReach',4),('sfpSonetOC12LongReach',5),('sfpSonetOC12IntermediateReach',6),('sfpSonetOC12ShortReach',7),('sfpSonetOC3LongReach',8),('sfpSonetOC3IntermediateReach',9),('sfpSonetOC3ShortReach',10),('sfp1000BaseT',11),('sfp1000BaseCX',12),('sfp1000BaseLX',13),('sfp1000baseSX',14),('sfpBasePX',15),('sfpBaseBX10',16),('sfp100BaseFX',17),('sfp100BaseLX',18)))
_SfpCompliance_Type.__name__=_C
_SfpCompliance_Object=MibTableColumn
sfpCompliance=_SfpCompliance_Object((1,3,6,1,4,1,3373,1103,74,2,1,12),_SfpCompliance_Type())
sfpCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpCompliance.setStatus(_A)
_SfpWavelength_Type=Integer32
_SfpWavelength_Object=MibTableColumn
sfpWavelength=_SfpWavelength_Object((1,3,6,1,4,1,3373,1103,74,2,1,13),_SfpWavelength_Type())
sfpWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpWavelength.setStatus(_A)
if mibBuilder.loadTexts:sfpWavelength.setUnits('nm')
_SfpNominalBitRate_Type=Integer32
_SfpNominalBitRate_Object=MibTableColumn
sfpNominalBitRate=_SfpNominalBitRate_Object((1,3,6,1,4,1,3373,1103,74,2,1,14),_SfpNominalBitRate_Type())
sfpNominalBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpNominalBitRate.setStatus(_A)
_SfpLinkLength9u_Type=Integer32
_SfpLinkLength9u_Object=MibTableColumn
sfpLinkLength9u=_SfpLinkLength9u_Object((1,3,6,1,4,1,3373,1103,74,2,1,15),_SfpLinkLength9u_Type())
sfpLinkLength9u.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLinkLength9u.setStatus(_A)
if mibBuilder.loadTexts:sfpLinkLength9u.setUnits('m')
_SfpLinkLength50u_Type=Integer32
_SfpLinkLength50u_Object=MibTableColumn
sfpLinkLength50u=_SfpLinkLength50u_Object((1,3,6,1,4,1,3373,1103,74,2,1,16),_SfpLinkLength50u_Type())
sfpLinkLength50u.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLinkLength50u.setStatus(_A)
if mibBuilder.loadTexts:sfpLinkLength50u.setUnits('m')
_SfpLinkLength62u5_Type=Integer32
_SfpLinkLength62u5_Object=MibTableColumn
sfpLinkLength62u5=_SfpLinkLength62u5_Object((1,3,6,1,4,1,3373,1103,74,2,1,17),_SfpLinkLength62u5_Type())
sfpLinkLength62u5.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLinkLength62u5.setStatus(_A)
if mibBuilder.loadTexts:sfpLinkLength62u5.setUnits('m')
_SfpLinkLengthCopper_Type=Integer32
_SfpLinkLengthCopper_Object=MibTableColumn
sfpLinkLengthCopper=_SfpLinkLengthCopper_Object((1,3,6,1,4,1,3373,1103,74,2,1,18),_SfpLinkLengthCopper_Type())
sfpLinkLengthCopper.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLinkLengthCopper.setStatus(_A)
if mibBuilder.loadTexts:sfpLinkLengthCopper.setUnits('m')
class _SfpLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SfpLabel_Type.__name__=_J
_SfpLabel_Object=MibTableColumn
sfpLabel=_SfpLabel_Object((1,3,6,1,4,1,3373,1103,74,2,1,19),_SfpLabel_Type())
sfpLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLabel.setStatus(_A)
_SfpFailAlarm_Type=AlarmStatus
_SfpFailAlarm_Object=MibTableColumn
sfpFailAlarm=_SfpFailAlarm_Object((1,3,6,1,4,1,3373,1103,74,2,1,20),_SfpFailAlarm_Type())
sfpFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpFailAlarm.setStatus(_A)
class _SfpFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_SfpFailAlarmSeverityCode_Type.__name__=_E
_SfpFailAlarmSeverityCode_Object=MibScalar
sfpFailAlarmSeverityCode=_SfpFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,74,6),_SfpFailAlarmSeverityCode_Type())
sfpFailAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpFailAlarmSeverityCode.setStatus(_A)
_SfpDiagnosticTable_Object=MibTable
sfpDiagnosticTable=_SfpDiagnosticTable_Object((1,3,6,1,4,1,3373,1103,74,7))
if mibBuilder.loadTexts:sfpDiagnosticTable.setStatus(_A)
_SfpDiagnosticEntry_Object=MibTableRow
sfpDiagnosticEntry=_SfpDiagnosticEntry_Object((1,3,6,1,4,1,3373,1103,74,7,1))
sfpDiagnosticEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:sfpDiagnosticEntry.setStatus(_A)
_SfpDiagnosticValid_Type=TruthValue
_SfpDiagnosticValid_Object=MibTableColumn
sfpDiagnosticValid=_SfpDiagnosticValid_Object((1,3,6,1,4,1,3373,1103,74,7,1,1),_SfpDiagnosticValid_Type())
sfpDiagnosticValid.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagnosticValid.setStatus(_A)
_SfpLOSPinOut_Type=TruthValue
_SfpLOSPinOut_Object=MibTableColumn
sfpLOSPinOut=_SfpLOSPinOut_Object((1,3,6,1,4,1,3373,1103,74,7,1,2),_SfpLOSPinOut_Type())
sfpLOSPinOut.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLOSPinOut.setStatus(_A)
_SfpTxFaultPinOut_Type=TruthValue
_SfpTxFaultPinOut_Object=MibTableColumn
sfpTxFaultPinOut=_SfpTxFaultPinOut_Object((1,3,6,1,4,1,3373,1103,74,7,1,3),_SfpTxFaultPinOut_Type())
sfpTxFaultPinOut.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTxFaultPinOut.setStatus(_A)
_SfpRateSelectPinIn_Type=TruthValue
_SfpRateSelectPinIn_Object=MibTableColumn
sfpRateSelectPinIn=_SfpRateSelectPinIn_Object((1,3,6,1,4,1,3373,1103,74,7,1,4),_SfpRateSelectPinIn_Type())
sfpRateSelectPinIn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpRateSelectPinIn.setStatus(_A)
_SfpTxDisablePinIn_Type=TruthValue
_SfpTxDisablePinIn_Object=MibTableColumn
sfpTxDisablePinIn=_SfpTxDisablePinIn_Object((1,3,6,1,4,1,3373,1103,74,7,1,5),_SfpTxDisablePinIn_Type())
sfpTxDisablePinIn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTxDisablePinIn.setStatus(_A)
_SfpTemperature_Type=Temperature
_SfpTemperature_Object=MibTableColumn
sfpTemperature=_SfpTemperature_Object((1,3,6,1,4,1,3373,1103,74,7,1,6),_SfpTemperature_Type())
sfpTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTemperature.setStatus(_A)
if mibBuilder.loadTexts:sfpTemperature.setUnits('C/10')
class _SfpVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpVoltage_Type.__name__=_F
_SfpVoltage_Object=MibTableColumn
sfpVoltage=_SfpVoltage_Object((1,3,6,1,4,1,3373,1103,74,7,1,7),_SfpVoltage_Type())
sfpVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVoltage.setStatus(_A)
if mibBuilder.loadTexts:sfpVoltage.setUnits('milliVolts (mV)')
class _SfpTxBias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131000))
_SfpTxBias_Type.__name__=_F
_SfpTxBias_Object=MibTableColumn
sfpTxBias=_SfpTxBias_Object((1,3,6,1,4,1,3373,1103,74,7,1,8),_SfpTxBias_Type())
sfpTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTxBias.setStatus(_A)
if mibBuilder.loadTexts:sfpTxBias.setUnits('microAmps (uA)')
class _SfpTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpTxPower_Type.__name__=_F
_SfpTxPower_Object=MibTableColumn
sfpTxPower=_SfpTxPower_Object((1,3,6,1,4,1,3373,1103,74,7,1,9),_SfpTxPower_Type())
sfpTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTxPower.setStatus(_A)
if mibBuilder.loadTexts:sfpTxPower.setUnits(_K)
class _SfpRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpRxPower_Type.__name__=_F
_SfpRxPower_Object=MibTableColumn
sfpRxPower=_SfpRxPower_Object((1,3,6,1,4,1,3373,1103,74,7,1,10),_SfpRxPower_Type())
sfpRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpRxPower.setStatus(_A)
if mibBuilder.loadTexts:sfpRxPower.setUnits(_K)
class _SfpInternalAlarms_Type(Bits):namedValues=NamedValues(*(('sfpIntAlarmTempHigh',0),('sfpIntAlarmTempLow',1),('sfpIntAlarmVoltageHigh',2),('sfpIntAlarmVoltageLow',3),('sfpIntAlarmTxBiasHigh',4),('sfpIntAlarmTxBiasLow',5),('sfpIntAlarmTxPowerHigh',6),('sfpIntAlarmTxPowerLow',7),('sfpIntAlarmRxPowerHigh',8),('sfpIntAlarmRxPowerLow',9)))
_SfpInternalAlarms_Type.__name__=_C
_SfpInternalAlarms_Object=MibTableColumn
sfpInternalAlarms=_SfpInternalAlarms_Object((1,3,6,1,4,1,3373,1103,74,7,1,11),_SfpInternalAlarms_Type())
sfpInternalAlarms.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpInternalAlarms.setStatus(_A)
class _SfpInternalWarnings_Type(Bits):namedValues=NamedValues(*(('sfpIntWarnTempHigh',0),('sfpIntWarnTempLow',1),('sfpIntWarnVoltageHigh',2),('sfpIntWarnVoltageLow',3),('sfpIntWarnTxBiasHigh',4),('sfpIntWarnTxBiasLow',5),('sfpIntWarnTxPowerHigh',6),('sfpIntWarnTxPowerLow',7),('sfpIntWarnRxPowerHigh',8),('sfpIntWarnRxPowerLow',9)))
_SfpInternalWarnings_Type.__name__=_C
_SfpInternalWarnings_Object=MibTableColumn
sfpInternalWarnings=_SfpInternalWarnings_Object((1,3,6,1,4,1,3373,1103,74,7,1,12),_SfpInternalWarnings_Type())
sfpInternalWarnings.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpInternalWarnings.setStatus(_A)
_SfpAlarmTable_Object=MibTable
sfpAlarmTable=_SfpAlarmTable_Object((1,3,6,1,4,1,3373,1103,74,10))
if mibBuilder.loadTexts:sfpAlarmTable.setStatus(_A)
_SfpAlarmEntry_Object=MibTableRow
sfpAlarmEntry=_SfpAlarmEntry_Object((1,3,6,1,4,1,3373,1103,74,10,1))
sfpAlarmEntry.setIndexNames((0,_G,_I),(0,_G,_L))
if mibBuilder.loadTexts:sfpAlarmEntry.setStatus(_A)
_SfpPhysicalQuantity_Type=PhysicalQuantity
_SfpPhysicalQuantity_Object=MibTableColumn
sfpPhysicalQuantity=_SfpPhysicalQuantity_Object((1,3,6,1,4,1,3373,1103,74,10,1,1),_SfpPhysicalQuantity_Type())
sfpPhysicalQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpPhysicalQuantity.setStatus(_A)
_SfpThresholdHighAlarm_Type=Integer32
_SfpThresholdHighAlarm_Object=MibTableColumn
sfpThresholdHighAlarm=_SfpThresholdHighAlarm_Object((1,3,6,1,4,1,3373,1103,74,10,1,2),_SfpThresholdHighAlarm_Type())
sfpThresholdHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpThresholdHighAlarm.setStatus(_A)
_SfpThresholdHighWarning_Type=Integer32
_SfpThresholdHighWarning_Object=MibTableColumn
sfpThresholdHighWarning=_SfpThresholdHighWarning_Object((1,3,6,1,4,1,3373,1103,74,10,1,3),_SfpThresholdHighWarning_Type())
sfpThresholdHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpThresholdHighWarning.setStatus(_A)
_SfpThresholdLowAlarm_Type=Integer32
_SfpThresholdLowAlarm_Object=MibTableColumn
sfpThresholdLowAlarm=_SfpThresholdLowAlarm_Object((1,3,6,1,4,1,3373,1103,74,10,1,4),_SfpThresholdLowAlarm_Type())
sfpThresholdLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpThresholdLowAlarm.setStatus(_A)
_SfpThresholdLowWarning_Type=Integer32
_SfpThresholdLowWarning_Object=MibTableColumn
sfpThresholdLowWarning=_SfpThresholdLowWarning_Object((1,3,6,1,4,1,3373,1103,74,10,1,5),_SfpThresholdLowWarning_Type())
sfpThresholdLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpThresholdLowWarning.setStatus(_A)
_SfpHighAlarm_Type=AlarmStatus
_SfpHighAlarm_Object=MibTableColumn
sfpHighAlarm=_SfpHighAlarm_Object((1,3,6,1,4,1,3373,1103,74,10,1,6),_SfpHighAlarm_Type())
sfpHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpHighAlarm.setStatus(_A)
_SfpHighWarningAlarm_Type=AlarmStatus
_SfpHighWarningAlarm_Object=MibTableColumn
sfpHighWarningAlarm=_SfpHighWarningAlarm_Object((1,3,6,1,4,1,3373,1103,74,10,1,7),_SfpHighWarningAlarm_Type())
sfpHighWarningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpHighWarningAlarm.setStatus(_A)
_SfpLowAlarm_Type=AlarmStatus
_SfpLowAlarm_Object=MibTableColumn
sfpLowAlarm=_SfpLowAlarm_Object((1,3,6,1,4,1,3373,1103,74,10,1,8),_SfpLowAlarm_Type())
sfpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLowAlarm.setStatus(_A)
_SfpLowWarningAlarm_Type=AlarmStatus
_SfpLowWarningAlarm_Object=MibTableColumn
sfpLowWarningAlarm=_SfpLowWarningAlarm_Object((1,3,6,1,4,1,3373,1103,74,10,1,9),_SfpLowWarningAlarm_Type())
sfpLowWarningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpLowWarningAlarm.setStatus(_A)
class _SfpHighAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_SfpHighAlarmSeverityCode_Type.__name__=_E
_SfpHighAlarmSeverityCode_Object=MibScalar
sfpHighAlarmSeverityCode=_SfpHighAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,74,11),_SfpHighAlarmSeverityCode_Type())
sfpHighAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpHighAlarmSeverityCode.setStatus(_A)
class _SfpHighWarningAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_SfpHighWarningAlarmSeverityCode_Type.__name__=_E
_SfpHighWarningAlarmSeverityCode_Object=MibScalar
sfpHighWarningAlarmSeverityCode=_SfpHighWarningAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,74,12),_SfpHighWarningAlarmSeverityCode_Type())
sfpHighWarningAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpHighWarningAlarmSeverityCode.setStatus(_A)
class _SfpLowAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_SfpLowAlarmSeverityCode_Type.__name__=_E
_SfpLowAlarmSeverityCode_Object=MibScalar
sfpLowAlarmSeverityCode=_SfpLowAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,74,13),_SfpLowAlarmSeverityCode_Type())
sfpLowAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpLowAlarmSeverityCode.setStatus(_A)
class _SfpLowWarningAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_SfpLowWarningAlarmSeverityCode_Type.__name__=_E
_SfpLowWarningAlarmSeverityCode_Object=MibScalar
sfpLowWarningAlarmSeverityCode=_SfpLowWarningAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,74,14),_SfpLowWarningAlarmSeverityCode_Type())
sfpLowWarningAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpLowWarningAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'Temperature':Temperature,'PhysicalQuantity':PhysicalQuantity,'sfp':sfp,'sfpMibVersion':sfpMibVersion,'sfpSerialIdTable':sfpSerialIdTable,'sfpSerialIdEntry':sfpSerialIdEntry,_I:sfpModuleId,'sfpSerialIdValid':sfpSerialIdValid,'sfpVendorName':sfpVendorName,'sfpVendorPartNumber':sfpVendorPartNumber,'sfpVendorRev':sfpVendorRev,'sfpVendorSN':sfpVendorSN,'sfpVendorDateCode':sfpVendorDateCode,'sfpDiagMonitorCode':sfpDiagMonitorCode,'sfpEnhancedOptionsCode':sfpEnhancedOptionsCode,'sfpOptions':sfpOptions,'sfpFibreChannelMedia':sfpFibreChannelMedia,'sfpCompliance':sfpCompliance,'sfpWavelength':sfpWavelength,'sfpNominalBitRate':sfpNominalBitRate,'sfpLinkLength9u':sfpLinkLength9u,'sfpLinkLength50u':sfpLinkLength50u,'sfpLinkLength62u5':sfpLinkLength62u5,'sfpLinkLengthCopper':sfpLinkLengthCopper,'sfpLabel':sfpLabel,'sfpFailAlarm':sfpFailAlarm,'sfpFailAlarmSeverityCode':sfpFailAlarmSeverityCode,'sfpDiagnosticTable':sfpDiagnosticTable,'sfpDiagnosticEntry':sfpDiagnosticEntry,'sfpDiagnosticValid':sfpDiagnosticValid,'sfpLOSPinOut':sfpLOSPinOut,'sfpTxFaultPinOut':sfpTxFaultPinOut,'sfpRateSelectPinIn':sfpRateSelectPinIn,'sfpTxDisablePinIn':sfpTxDisablePinIn,'sfpTemperature':sfpTemperature,'sfpVoltage':sfpVoltage,'sfpTxBias':sfpTxBias,'sfpTxPower':sfpTxPower,'sfpRxPower':sfpRxPower,'sfpInternalAlarms':sfpInternalAlarms,'sfpInternalWarnings':sfpInternalWarnings,'sfpAlarmTable':sfpAlarmTable,'sfpAlarmEntry':sfpAlarmEntry,_L:sfpPhysicalQuantity,'sfpThresholdHighAlarm':sfpThresholdHighAlarm,'sfpThresholdHighWarning':sfpThresholdHighWarning,'sfpThresholdLowAlarm':sfpThresholdLowAlarm,'sfpThresholdLowWarning':sfpThresholdLowWarning,'sfpHighAlarm':sfpHighAlarm,'sfpHighWarningAlarm':sfpHighWarningAlarm,'sfpLowAlarm':sfpLowAlarm,'sfpLowWarningAlarm':sfpLowWarningAlarm,'sfpHighAlarmSeverityCode':sfpHighAlarmSeverityCode,'sfpHighWarningAlarmSeverityCode':sfpHighWarningAlarmSeverityCode,'sfpLowAlarmSeverityCode':sfpLowAlarmSeverityCode,'sfpLowWarningAlarmSeverityCode':sfpLowWarningAlarmSeverityCode})