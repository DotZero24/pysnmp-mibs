_N='testing'
_M='boostAmp'
_L='preAmp'
_K='Integer32'
_J='read-write'
_I='dBm'
_H='read-only'
_G='sysName'
_F='SNMPv2-MIB'
_E='adTrapInformSeqNum'
_D='ADTRAN-GENTRAPINFORM-MIB'
_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adTrapInformSeqNum,=mibBuilder.importSymbols(_D,_E)
adGenOpticalAmplifier,adGenOpticalAmplifierID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenOpticalAmplifier','adGenOpticalAmplifierID')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenOpticalAmplifierMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,41,1))
if mibBuilder.loadTexts:adGenOpticalAmplifierMIB.setRevisions(('2013-07-23 00:00','2012-08-27 00:00','2012-04-12 00:00','2012-01-17 00:00','2011-10-20 00:00','2011-08-08 00:00'))
_AdGenOpticalAmplifierProduct_ObjectIdentity=ObjectIdentity
adGenOpticalAmplifierProduct=_AdGenOpticalAmplifierProduct_ObjectIdentity((1,3,6,1,4,1,664,5,70,41,1))
_AdGenOpticalAmplifierTable_Object=MibTable
adGenOpticalAmplifierTable=_AdGenOpticalAmplifierTable_Object((1,3,6,1,4,1,664,5,70,41,1,1))
if mibBuilder.loadTexts:adGenOpticalAmplifierTable.setStatus(_A)
_AdGenOpticalAmplifierEntry_Object=MibTableRow
adGenOpticalAmplifierEntry=_AdGenOpticalAmplifierEntry_Object((1,3,6,1,4,1,664,5,70,41,1,1,1))
adGenOpticalAmplifierEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenOpticalAmplifierEntry.setStatus(_A)
class _AdGenOpticalAmplifierProdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('midStageAmp',3)))
_AdGenOpticalAmplifierProdType_Type.__name__=_K
_AdGenOpticalAmplifierProdType_Object=MibTableColumn
adGenOpticalAmplifierProdType=_AdGenOpticalAmplifierProdType_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,1),_AdGenOpticalAmplifierProdType_Type())
adGenOpticalAmplifierProdType.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierProdType.setStatus(_A)
class _AdGenOpticalAmplifierStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('moduleDisabled',1),('eyeSafeMode',2),('moduleOk',3),('powerOrGainLimited',4)))
_AdGenOpticalAmplifierStatus_Type.__name__=_K
_AdGenOpticalAmplifierStatus_Object=MibTableColumn
adGenOpticalAmplifierStatus=_AdGenOpticalAmplifierStatus_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,2),_AdGenOpticalAmplifierStatus_Type())
adGenOpticalAmplifierStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierStatus.setStatus(_A)
_AdGenOpticalAmplifierInputPower_Type=Integer32
_AdGenOpticalAmplifierInputPower_Object=MibTableColumn
adGenOpticalAmplifierInputPower=_AdGenOpticalAmplifierInputPower_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,3),_AdGenOpticalAmplifierInputPower_Type())
adGenOpticalAmplifierInputPower.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPower.setStatus(_A)
_AdGenOpticalAmplifierOutputPower_Type=Integer32
_AdGenOpticalAmplifierOutputPower_Object=MibTableColumn
adGenOpticalAmplifierOutputPower=_AdGenOpticalAmplifierOutputPower_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,4),_AdGenOpticalAmplifierOutputPower_Type())
adGenOpticalAmplifierOutputPower.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPower.setStatus(_A)
_AdGenOpticalAmplifierGain_Type=Integer32
_AdGenOpticalAmplifierGain_Object=MibTableColumn
adGenOpticalAmplifierGain=_AdGenOpticalAmplifierGain_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,5),_AdGenOpticalAmplifierGain_Type())
adGenOpticalAmplifierGain.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierGain.setStatus(_A)
_AdGenOpticalAmplifierCaseTemperature_Type=Integer32
_AdGenOpticalAmplifierCaseTemperature_Object=MibTableColumn
adGenOpticalAmplifierCaseTemperature=_AdGenOpticalAmplifierCaseTemperature_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,6),_AdGenOpticalAmplifierCaseTemperature_Type())
adGenOpticalAmplifierCaseTemperature.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierCaseTemperature.setStatus(_A)
_AdGenOpticalAmplifierBoardTemperature_Type=Integer32
_AdGenOpticalAmplifierBoardTemperature_Object=MibTableColumn
adGenOpticalAmplifierBoardTemperature=_AdGenOpticalAmplifierBoardTemperature_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,7),_AdGenOpticalAmplifierBoardTemperature_Type())
adGenOpticalAmplifierBoardTemperature.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierBoardTemperature.setStatus(_A)
_AdGenOpticalAmplifierPumpTemperature_Type=Integer32
_AdGenOpticalAmplifierPumpTemperature_Object=MibTableColumn
adGenOpticalAmplifierPumpTemperature=_AdGenOpticalAmplifierPumpTemperature_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,8),_AdGenOpticalAmplifierPumpTemperature_Type())
adGenOpticalAmplifierPumpTemperature.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierPumpTemperature.setStatus(_A)
_AdGenOpticalAmplifierLaserPumpOperatingCurrent_Type=Integer32
_AdGenOpticalAmplifierLaserPumpOperatingCurrent_Object=MibTableColumn
adGenOpticalAmplifierLaserPumpOperatingCurrent=_AdGenOpticalAmplifierLaserPumpOperatingCurrent_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,9),_AdGenOpticalAmplifierLaserPumpOperatingCurrent_Type())
adGenOpticalAmplifierLaserPumpOperatingCurrent.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierLaserPumpOperatingCurrent.setStatus(_A)
_AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Type=Integer32
_AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Object=MibTableColumn
adGenOpticalAmplifierLaserPumpEndOfLifeCurrent=_AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,10),_AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Type())
adGenOpticalAmplifierLaserPumpEndOfLifeCurrent.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierLaserPumpEndOfLifeCurrent.setStatus(_A)
_AdGenOpticalAmplifierLaserPumpReflectedPower_Type=Integer32
_AdGenOpticalAmplifierLaserPumpReflectedPower_Object=MibTableColumn
adGenOpticalAmplifierLaserPumpReflectedPower=_AdGenOpticalAmplifierLaserPumpReflectedPower_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,11),_AdGenOpticalAmplifierLaserPumpReflectedPower_Type())
adGenOpticalAmplifierLaserPumpReflectedPower.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierLaserPumpReflectedPower.setStatus(_A)
class _AdGenOpticalAmplifierInputPowerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,31),ValueRangeConstraint(32767,32767))
_AdGenOpticalAmplifierInputPowerThreshold_Type.__name__=_K
_AdGenOpticalAmplifierInputPowerThreshold_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThreshold=_AdGenOpticalAmplifierInputPowerThreshold_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,12),_AdGenOpticalAmplifierInputPowerThreshold_Type())
adGenOpticalAmplifierInputPowerThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThreshold.setStatus('deprecated')
_AdGenOpticalAmplifierIfIndexReference_Type=InterfaceIndex
_AdGenOpticalAmplifierIfIndexReference_Object=MibTableColumn
adGenOpticalAmplifierIfIndexReference=_AdGenOpticalAmplifierIfIndexReference_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,13),_AdGenOpticalAmplifierIfIndexReference_Type())
adGenOpticalAmplifierIfIndexReference.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierIfIndexReference.setStatus(_A)
_AdGenOpticalAmplifierInputPowerThresholdLow_Type=Integer32
_AdGenOpticalAmplifierInputPowerThresholdLow_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThresholdLow=_AdGenOpticalAmplifierInputPowerThresholdLow_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,14),_AdGenOpticalAmplifierInputPowerThresholdLow_Type())
adGenOpticalAmplifierInputPowerThresholdLow.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdLow.setStatus(_A)
_AdGenOpticalAmplifierInputPowerThresholdHigh_Type=Integer32
_AdGenOpticalAmplifierInputPowerThresholdHigh_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThresholdHigh=_AdGenOpticalAmplifierInputPowerThresholdHigh_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,15),_AdGenOpticalAmplifierInputPowerThresholdHigh_Type())
adGenOpticalAmplifierInputPowerThresholdHigh.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdHigh.setStatus(_A)
_AdGenOpticalAmplifierOutputPowerThresholdLow_Type=Integer32
_AdGenOpticalAmplifierOutputPowerThresholdLow_Object=MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdLow=_AdGenOpticalAmplifierOutputPowerThresholdLow_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,16),_AdGenOpticalAmplifierOutputPowerThresholdLow_Type())
adGenOpticalAmplifierOutputPowerThresholdLow.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdLow.setStatus(_A)
_AdGenOpticalAmplifierOutputPowerThresholdHigh_Type=Integer32
_AdGenOpticalAmplifierOutputPowerThresholdHigh_Object=MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdHigh=_AdGenOpticalAmplifierOutputPowerThresholdHigh_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,17),_AdGenOpticalAmplifierOutputPowerThresholdHigh_Type())
adGenOpticalAmplifierOutputPowerThresholdHigh.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdHigh.setStatus(_A)
_AdGenOpticalAmplifierMidStageAttenuation_Type=Integer32
_AdGenOpticalAmplifierMidStageAttenuation_Object=MibTableColumn
adGenOpticalAmplifierMidStageAttenuation=_AdGenOpticalAmplifierMidStageAttenuation_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,18),_AdGenOpticalAmplifierMidStageAttenuation_Type())
adGenOpticalAmplifierMidStageAttenuation.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierMidStageAttenuation.setStatus(_A)
_AdGenOpticalAmplifierVariableGain_Type=Integer32
_AdGenOpticalAmplifierVariableGain_Object=MibTableColumn
adGenOpticalAmplifierVariableGain=_AdGenOpticalAmplifierVariableGain_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,19),_AdGenOpticalAmplifierVariableGain_Type())
adGenOpticalAmplifierVariableGain.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierVariableGain.setStatus(_A)
class _AdGenOpticalAmplifierMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AdGenOpticalAmplifierMode_Type.__name__=_K
_AdGenOpticalAmplifierMode_Object=MibTableColumn
adGenOpticalAmplifierMode=_AdGenOpticalAmplifierMode_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,20),_AdGenOpticalAmplifierMode_Type())
adGenOpticalAmplifierMode.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierMode.setStatus(_A)
class _AdGenOpticalAmplifierAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_N,3)))
_AdGenOpticalAmplifierAdminState_Type.__name__=_K
_AdGenOpticalAmplifierAdminState_Object=MibTableColumn
adGenOpticalAmplifierAdminState=_AdGenOpticalAmplifierAdminState_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,21),_AdGenOpticalAmplifierAdminState_Type())
adGenOpticalAmplifierAdminState.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenOpticalAmplifierAdminState.setStatus(_A)
class _AdGenOpticalAmplifierOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_N,3)))
_AdGenOpticalAmplifierOperState_Type.__name__=_K
_AdGenOpticalAmplifierOperState_Object=MibTableColumn
adGenOpticalAmplifierOperState=_AdGenOpticalAmplifierOperState_Object((1,3,6,1,4,1,664,5,70,41,1,1,1,22),_AdGenOpticalAmplifierOperState_Type())
adGenOpticalAmplifierOperState.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierOperState.setStatus(_A)
_AdGenOpticalAmplifierSupplementTable_Object=MibTable
adGenOpticalAmplifierSupplementTable=_AdGenOpticalAmplifierSupplementTable_Object((1,3,6,1,4,1,664,5,70,41,1,2))
if mibBuilder.loadTexts:adGenOpticalAmplifierSupplementTable.setStatus(_A)
_AdGenOpticalAmplifierSupplementEntry_Object=MibTableRow
adGenOpticalAmplifierSupplementEntry=_AdGenOpticalAmplifierSupplementEntry_Object((1,3,6,1,4,1,664,5,70,41,1,2,1))
adGenOpticalAmplifierSupplementEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenOpticalAmplifierSupplementEntry.setStatus(_A)
_AdGenOpticalAmplifierInputPowerThresholdLowMax_Type=Integer32
_AdGenOpticalAmplifierInputPowerThresholdLowMax_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThresholdLowMax=_AdGenOpticalAmplifierInputPowerThresholdLowMax_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,1),_AdGenOpticalAmplifierInputPowerThresholdLowMax_Type())
adGenOpticalAmplifierInputPowerThresholdLowMax.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdLowMax.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdLowMax.setUnits(_I)
_AdGenOpticalAmplifierInputPowerThresholdLowMin_Type=Integer32
_AdGenOpticalAmplifierInputPowerThresholdLowMin_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThresholdLowMin=_AdGenOpticalAmplifierInputPowerThresholdLowMin_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,2),_AdGenOpticalAmplifierInputPowerThresholdLowMin_Type())
adGenOpticalAmplifierInputPowerThresholdLowMin.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdLowMin.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdLowMin.setUnits(_I)
_AdGenOpticalAmplifierInputPowerThresholdHighMax_Type=Integer32
_AdGenOpticalAmplifierInputPowerThresholdHighMax_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThresholdHighMax=_AdGenOpticalAmplifierInputPowerThresholdHighMax_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,3),_AdGenOpticalAmplifierInputPowerThresholdHighMax_Type())
adGenOpticalAmplifierInputPowerThresholdHighMax.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdHighMax.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdHighMax.setUnits(_I)
_AdGenOpticalAmplifierInputPowerThresholdHighMin_Type=Integer32
_AdGenOpticalAmplifierInputPowerThresholdHighMin_Object=MibTableColumn
adGenOpticalAmplifierInputPowerThresholdHighMin=_AdGenOpticalAmplifierInputPowerThresholdHighMin_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,4),_AdGenOpticalAmplifierInputPowerThresholdHighMin_Type())
adGenOpticalAmplifierInputPowerThresholdHighMin.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdHighMin.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierInputPowerThresholdHighMin.setUnits(_I)
_AdGenOpticalAmplifierOutputPowerThresholdLowMax_Type=Integer32
_AdGenOpticalAmplifierOutputPowerThresholdLowMax_Object=MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdLowMax=_AdGenOpticalAmplifierOutputPowerThresholdLowMax_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,5),_AdGenOpticalAmplifierOutputPowerThresholdLowMax_Type())
adGenOpticalAmplifierOutputPowerThresholdLowMax.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdLowMax.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdLowMax.setUnits(_I)
_AdGenOpticalAmplifierOutputPowerThresholdLowMin_Type=Integer32
_AdGenOpticalAmplifierOutputPowerThresholdLowMin_Object=MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdLowMin=_AdGenOpticalAmplifierOutputPowerThresholdLowMin_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,6),_AdGenOpticalAmplifierOutputPowerThresholdLowMin_Type())
adGenOpticalAmplifierOutputPowerThresholdLowMin.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdLowMin.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdLowMin.setUnits(_I)
_AdGenOpticalAmplifierOutputPowerThresholdHighMax_Type=Integer32
_AdGenOpticalAmplifierOutputPowerThresholdHighMax_Object=MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdHighMax=_AdGenOpticalAmplifierOutputPowerThresholdHighMax_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,7),_AdGenOpticalAmplifierOutputPowerThresholdHighMax_Type())
adGenOpticalAmplifierOutputPowerThresholdHighMax.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdHighMax.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdHighMax.setUnits(_I)
_AdGenOpticalAmplifierOutputPowerThresholdHighMin_Type=Integer32
_AdGenOpticalAmplifierOutputPowerThresholdHighMin_Object=MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdHighMin=_AdGenOpticalAmplifierOutputPowerThresholdHighMin_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,8),_AdGenOpticalAmplifierOutputPowerThresholdHighMin_Type())
adGenOpticalAmplifierOutputPowerThresholdHighMin.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdHighMin.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierOutputPowerThresholdHighMin.setUnits(_I)
_AdGenOpticalAmplifierMidStageAttenuationMax_Type=Integer32
_AdGenOpticalAmplifierMidStageAttenuationMax_Object=MibTableColumn
adGenOpticalAmplifierMidStageAttenuationMax=_AdGenOpticalAmplifierMidStageAttenuationMax_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,9),_AdGenOpticalAmplifierMidStageAttenuationMax_Type())
adGenOpticalAmplifierMidStageAttenuationMax.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierMidStageAttenuationMax.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierMidStageAttenuationMax.setUnits(_I)
_AdGenOpticalAmplifierMidStageAttenuationMin_Type=Integer32
_AdGenOpticalAmplifierMidStageAttenuationMin_Object=MibTableColumn
adGenOpticalAmplifierMidStageAttenuationMin=_AdGenOpticalAmplifierMidStageAttenuationMin_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,10),_AdGenOpticalAmplifierMidStageAttenuationMin_Type())
adGenOpticalAmplifierMidStageAttenuationMin.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierMidStageAttenuationMin.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierMidStageAttenuationMin.setUnits(_I)
_AdGenOpticalAmplifierVariableGainMin_Type=Integer32
_AdGenOpticalAmplifierVariableGainMin_Object=MibTableColumn
adGenOpticalAmplifierVariableGainMin=_AdGenOpticalAmplifierVariableGainMin_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,11),_AdGenOpticalAmplifierVariableGainMin_Type())
adGenOpticalAmplifierVariableGainMin.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierVariableGainMin.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierVariableGainMin.setUnits('dB')
_AdGenOpticalAmplifierVariableGainMax_Type=Integer32
_AdGenOpticalAmplifierVariableGainMax_Object=MibTableColumn
adGenOpticalAmplifierVariableGainMax=_AdGenOpticalAmplifierVariableGainMax_Object((1,3,6,1,4,1,664,5,70,41,1,2,1,12),_AdGenOpticalAmplifierVariableGainMax_Type())
adGenOpticalAmplifierVariableGainMax.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenOpticalAmplifierVariableGainMax.setStatus(_A)
if mibBuilder.loadTexts:adGenOpticalAmplifierVariableGainMax.setUnits('dB')
_AdGenOpticalAmplifierAlrms_ObjectIdentity=ObjectIdentity
adGenOpticalAmplifierAlrms=_AdGenOpticalAmplifierAlrms_ObjectIdentity((1,3,6,1,4,1,664,5,70,41,1,100))
_AdGenOpticalAmplifierEvents_ObjectIdentity=ObjectIdentity
adGenOpticalAmplifierEvents=_AdGenOpticalAmplifierEvents_ObjectIdentity((1,3,6,1,4,1,664,5,70,41,1,100,0))
adGenInputPowerThrAlarmClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,1))
adGenInputPowerThrAlarmClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenInputPowerThrAlarmClear.setStatus(_A)
adGenInputPowerThrAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,2))
adGenInputPowerThrAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenInputPowerThrAlrmSet.setStatus(_A)
adGenOutputPowerLossClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,3))
adGenOutputPowerLossClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOutputPowerLossClear.setStatus(_A)
adGenOutputPowerLossAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,4))
adGenOutputPowerLossAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOutputPowerLossAlrmSet.setStatus(_A)
adGenBoardTempClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,5))
adGenBoardTempClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenBoardTempClear.setStatus(_A)
adGenBoardTempAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,6))
adGenBoardTempAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenBoardTempAlrmSet.setStatus(_A)
adGenModuleTempLowClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,7))
adGenModuleTempLowClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenModuleTempLowClear.setStatus(_A)
adGenModuleTempLowAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,8))
adGenModuleTempLowAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenModuleTempLowAlrmSet.setStatus(_A)
adGenModuleTempHighClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,9))
adGenModuleTempHighClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenModuleTempHighClear.setStatus(_A)
adGenModuleTempHighAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,10))
adGenModuleTempHighAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenModuleTempHighAlrmSet.setStatus(_A)
adGenLaserPumpTempClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,11))
adGenLaserPumpTempClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenLaserPumpTempClear.setStatus(_A)
adGenLaserPumpTempAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,12))
adGenLaserPumpTempAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenLaserPumpTempAlrmSet.setStatus(_A)
adGenLaserPumpEOLClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,13))
adGenLaserPumpEOLClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenLaserPumpEOLClear.setStatus(_A)
adGenLaserPumpEOLAlrmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,14))
adGenLaserPumpEOLAlrmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenLaserPumpEOLAlrmSet.setStatus(_A)
adGenInputPowerThLowAlarmClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,15))
adGenInputPowerThLowAlarmClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenInputPowerThLowAlarmClear.setStatus(_A)
adGenInputPowerThLowAlarmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,16))
adGenInputPowerThLowAlarmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenInputPowerThLowAlarmSet.setStatus(_A)
adGenInputPowerThHighAlarmClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,17))
adGenInputPowerThHighAlarmClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenInputPowerThHighAlarmClear.setStatus(_A)
adGenInputPowerThHighAlarmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,18))
adGenInputPowerThHighAlarmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenInputPowerThHighAlarmSet.setStatus(_A)
adGenOutputPowerThLowAlarmClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,19))
adGenOutputPowerThLowAlarmClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOutputPowerThLowAlarmClear.setStatus(_A)
adGenOutputPowerThLowAlarmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,20))
adGenOutputPowerThLowAlarmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOutputPowerThLowAlarmSet.setStatus(_A)
adGenOutputPowerThHighAlarmClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,21))
adGenOutputPowerThHighAlarmClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOutputPowerThHighAlarmClear.setStatus(_A)
adGenOutputPowerThHighAlarmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,22))
adGenOutputPowerThHighAlarmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOutputPowerThHighAlarmSet.setStatus(_A)
adGenAmplifierLOSAlarmClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,23))
adGenAmplifierLOSAlarmClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenAmplifierLOSAlarmClear.setStatus(_A)
adGenAmplifierLOSAlarmSet=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,24))
adGenAmplifierLOSAlarmSet.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenAmplifierLOSAlarmSet.setStatus(_A)
adGenOpticalAmplifierLossOfMidStageInActiveClear=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,25))
adGenOpticalAmplifierLossOfMidStageInActiveClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOpticalAmplifierLossOfMidStageInActiveClear.setStatus(_A)
adGenOpticalAmplifierLossOfMidStageInActive=NotificationType((1,3,6,1,4,1,664,5,70,41,1,100,0,26))
adGenOpticalAmplifierLossOfMidStageInActive.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adGenOpticalAmplifierLossOfMidStageInActive.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GEN-OPTICAL-AMPLIFIER-MIB',**{'adGenOpticalAmplifierProduct':adGenOpticalAmplifierProduct,'adGenOpticalAmplifierTable':adGenOpticalAmplifierTable,'adGenOpticalAmplifierEntry':adGenOpticalAmplifierEntry,'adGenOpticalAmplifierProdType':adGenOpticalAmplifierProdType,'adGenOpticalAmplifierStatus':adGenOpticalAmplifierStatus,'adGenOpticalAmplifierInputPower':adGenOpticalAmplifierInputPower,'adGenOpticalAmplifierOutputPower':adGenOpticalAmplifierOutputPower,'adGenOpticalAmplifierGain':adGenOpticalAmplifierGain,'adGenOpticalAmplifierCaseTemperature':adGenOpticalAmplifierCaseTemperature,'adGenOpticalAmplifierBoardTemperature':adGenOpticalAmplifierBoardTemperature,'adGenOpticalAmplifierPumpTemperature':adGenOpticalAmplifierPumpTemperature,'adGenOpticalAmplifierLaserPumpOperatingCurrent':adGenOpticalAmplifierLaserPumpOperatingCurrent,'adGenOpticalAmplifierLaserPumpEndOfLifeCurrent':adGenOpticalAmplifierLaserPumpEndOfLifeCurrent,'adGenOpticalAmplifierLaserPumpReflectedPower':adGenOpticalAmplifierLaserPumpReflectedPower,'adGenOpticalAmplifierInputPowerThreshold':adGenOpticalAmplifierInputPowerThreshold,'adGenOpticalAmplifierIfIndexReference':adGenOpticalAmplifierIfIndexReference,'adGenOpticalAmplifierInputPowerThresholdLow':adGenOpticalAmplifierInputPowerThresholdLow,'adGenOpticalAmplifierInputPowerThresholdHigh':adGenOpticalAmplifierInputPowerThresholdHigh,'adGenOpticalAmplifierOutputPowerThresholdLow':adGenOpticalAmplifierOutputPowerThresholdLow,'adGenOpticalAmplifierOutputPowerThresholdHigh':adGenOpticalAmplifierOutputPowerThresholdHigh,'adGenOpticalAmplifierMidStageAttenuation':adGenOpticalAmplifierMidStageAttenuation,'adGenOpticalAmplifierVariableGain':adGenOpticalAmplifierVariableGain,'adGenOpticalAmplifierMode':adGenOpticalAmplifierMode,'adGenOpticalAmplifierAdminState':adGenOpticalAmplifierAdminState,'adGenOpticalAmplifierOperState':adGenOpticalAmplifierOperState,'adGenOpticalAmplifierSupplementTable':adGenOpticalAmplifierSupplementTable,'adGenOpticalAmplifierSupplementEntry':adGenOpticalAmplifierSupplementEntry,'adGenOpticalAmplifierInputPowerThresholdLowMax':adGenOpticalAmplifierInputPowerThresholdLowMax,'adGenOpticalAmplifierInputPowerThresholdLowMin':adGenOpticalAmplifierInputPowerThresholdLowMin,'adGenOpticalAmplifierInputPowerThresholdHighMax':adGenOpticalAmplifierInputPowerThresholdHighMax,'adGenOpticalAmplifierInputPowerThresholdHighMin':adGenOpticalAmplifierInputPowerThresholdHighMin,'adGenOpticalAmplifierOutputPowerThresholdLowMax':adGenOpticalAmplifierOutputPowerThresholdLowMax,'adGenOpticalAmplifierOutputPowerThresholdLowMin':adGenOpticalAmplifierOutputPowerThresholdLowMin,'adGenOpticalAmplifierOutputPowerThresholdHighMax':adGenOpticalAmplifierOutputPowerThresholdHighMax,'adGenOpticalAmplifierOutputPowerThresholdHighMin':adGenOpticalAmplifierOutputPowerThresholdHighMin,'adGenOpticalAmplifierMidStageAttenuationMax':adGenOpticalAmplifierMidStageAttenuationMax,'adGenOpticalAmplifierMidStageAttenuationMin':adGenOpticalAmplifierMidStageAttenuationMin,'adGenOpticalAmplifierVariableGainMin':adGenOpticalAmplifierVariableGainMin,'adGenOpticalAmplifierVariableGainMax':adGenOpticalAmplifierVariableGainMax,'adGenOpticalAmplifierAlrms':adGenOpticalAmplifierAlrms,'adGenOpticalAmplifierEvents':adGenOpticalAmplifierEvents,'adGenInputPowerThrAlarmClear':adGenInputPowerThrAlarmClear,'adGenInputPowerThrAlrmSet':adGenInputPowerThrAlrmSet,'adGenOutputPowerLossClear':adGenOutputPowerLossClear,'adGenOutputPowerLossAlrmSet':adGenOutputPowerLossAlrmSet,'adGenBoardTempClear':adGenBoardTempClear,'adGenBoardTempAlrmSet':adGenBoardTempAlrmSet,'adGenModuleTempLowClear':adGenModuleTempLowClear,'adGenModuleTempLowAlrmSet':adGenModuleTempLowAlrmSet,'adGenModuleTempHighClear':adGenModuleTempHighClear,'adGenModuleTempHighAlrmSet':adGenModuleTempHighAlrmSet,'adGenLaserPumpTempClear':adGenLaserPumpTempClear,'adGenLaserPumpTempAlrmSet':adGenLaserPumpTempAlrmSet,'adGenLaserPumpEOLClear':adGenLaserPumpEOLClear,'adGenLaserPumpEOLAlrmSet':adGenLaserPumpEOLAlrmSet,'adGenInputPowerThLowAlarmClear':adGenInputPowerThLowAlarmClear,'adGenInputPowerThLowAlarmSet':adGenInputPowerThLowAlarmSet,'adGenInputPowerThHighAlarmClear':adGenInputPowerThHighAlarmClear,'adGenInputPowerThHighAlarmSet':adGenInputPowerThHighAlarmSet,'adGenOutputPowerThLowAlarmClear':adGenOutputPowerThLowAlarmClear,'adGenOutputPowerThLowAlarmSet':adGenOutputPowerThLowAlarmSet,'adGenOutputPowerThHighAlarmClear':adGenOutputPowerThHighAlarmClear,'adGenOutputPowerThHighAlarmSet':adGenOutputPowerThHighAlarmSet,'adGenAmplifierLOSAlarmClear':adGenAmplifierLOSAlarmClear,'adGenAmplifierLOSAlarmSet':adGenAmplifierLOSAlarmSet,'adGenOpticalAmplifierLossOfMidStageInActiveClear':adGenOpticalAmplifierLossOfMidStageInActiveClear,'adGenOpticalAmplifierLossOfMidStageInActive':adGenOpticalAmplifierLossOfMidStageInActive,'adGenOpticalAmplifierMIB':adGenOpticalAmplifierMIB})