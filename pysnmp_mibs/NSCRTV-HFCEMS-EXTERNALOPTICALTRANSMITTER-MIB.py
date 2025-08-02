_J='otxDCPowerIndex'
_I='otxFansIndex'
_H='otxModuleIndex'
_G='off'
_F='NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB'
_E='read-write'
_D='Integer32'
_C='mandatory'
_B='optional'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
otxIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','otxIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_OtxVendorOID_Type=ObjectIdentifier
_OtxVendorOID_Object=MibScalar
otxVendorOID=_OtxVendorOID_Object((1,3,6,1,4,1,17409,1,7,1),_OtxVendorOID_Type())
otxVendorOID.setMaxAccess(_A)
if mibBuilder.loadTexts:otxVendorOID.setStatus(_B)
_OtxSlotNumber_Type=Integer32
_OtxSlotNumber_Object=MibScalar
otxSlotNumber=_OtxSlotNumber_Object((1,3,6,1,4,1,17409,1,7,2),_OtxSlotNumber_Type())
otxSlotNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:otxSlotNumber.setStatus(_C)
_OtxModuleTable_Object=MibTable
otxModuleTable=_OtxModuleTable_Object((1,3,6,1,4,1,17409,1,7,3))
if mibBuilder.loadTexts:otxModuleTable.setStatus(_C)
_OtxModuleEntry_Object=MibTableRow
otxModuleEntry=_OtxModuleEntry_Object((1,3,6,1,4,1,17409,1,7,3,1))
otxModuleEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:otxModuleEntry.setStatus(_C)
_OtxModuleIndex_Type=Integer32
_OtxModuleIndex_Object=MibTableColumn
otxModuleIndex=_OtxModuleIndex_Object((1,3,6,1,4,1,17409,1,7,3,1,1),_OtxModuleIndex_Type())
otxModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:otxModuleIndex.setStatus(_C)
class _OtxLaserControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_G,2)))
_OtxLaserControl_Type.__name__=_D
_OtxLaserControl_Object=MibTableColumn
otxLaserControl=_OtxLaserControl_Object((1,3,6,1,4,1,17409,1,7,3,1,2),_OtxLaserControl_Type())
otxLaserControl.setMaxAccess(_E)
if mibBuilder.loadTexts:otxLaserControl.setStatus(_C)
class _OtxConfigurationAGCMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('modeAgcOff',1),('modeCWUnmodulatedAgcOn',2),('modeVideoModulatedAgcOn',3)))
_OtxConfigurationAGCMode_Type.__name__=_D
_OtxConfigurationAGCMode_Object=MibTableColumn
otxConfigurationAGCMode=_OtxConfigurationAGCMode_Object((1,3,6,1,4,1,17409,1,7,3,1,3),_OtxConfigurationAGCMode_Type())
otxConfigurationAGCMode.setMaxAccess(_E)
if mibBuilder.loadTexts:otxConfigurationAGCMode.setStatus(_B)
_OtxConfigurationOmi_Type=Integer32
_OtxConfigurationOmi_Object=MibTableColumn
otxConfigurationOmi=_OtxConfigurationOmi_Object((1,3,6,1,4,1,17409,1,7,3,1,4),_OtxConfigurationOmi_Type())
otxConfigurationOmi.setMaxAccess(_E)
if mibBuilder.loadTexts:otxConfigurationOmi.setStatus(_B)
_OtxConfigurationRfGain_Type=Integer32
_OtxConfigurationRfGain_Object=MibTableColumn
otxConfigurationRfGain=_OtxConfigurationRfGain_Object((1,3,6,1,4,1,17409,1,7,3,1,5),_OtxConfigurationRfGain_Type())
otxConfigurationRfGain.setMaxAccess(_E)
if mibBuilder.loadTexts:otxConfigurationRfGain.setStatus(_B)
_OtxConfigurationSbsSuppression_Type=Integer32
_OtxConfigurationSbsSuppression_Object=MibTableColumn
otxConfigurationSbsSuppression=_OtxConfigurationSbsSuppression_Object((1,3,6,1,4,1,17409,1,7,3,1,6),_OtxConfigurationSbsSuppression_Type())
otxConfigurationSbsSuppression.setMaxAccess(_E)
if mibBuilder.loadTexts:otxConfigurationSbsSuppression.setStatus(_B)
_OtxConfigurationChannelDistance_Type=Integer32
_OtxConfigurationChannelDistance_Object=MibTableColumn
otxConfigurationChannelDistance=_OtxConfigurationChannelDistance_Object((1,3,6,1,4,1,17409,1,7,3,1,7),_OtxConfigurationChannelDistance_Type())
otxConfigurationChannelDistance.setMaxAccess(_E)
if mibBuilder.loadTexts:otxConfigurationChannelDistance.setStatus(_B)
_OtxConfigurationItuFrequency_Type=Integer32
_OtxConfigurationItuFrequency_Object=MibTableColumn
otxConfigurationItuFrequency=_OtxConfigurationItuFrequency_Object((1,3,6,1,4,1,17409,1,7,3,1,8),_OtxConfigurationItuFrequency_Type())
otxConfigurationItuFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:otxConfigurationItuFrequency.setStatus(_B)
_OtxItuFrequencyMin_Type=Integer32
_OtxItuFrequencyMin_Object=MibTableColumn
otxItuFrequencyMin=_OtxItuFrequencyMin_Object((1,3,6,1,4,1,17409,1,7,3,1,9),_OtxItuFrequencyMin_Type())
otxItuFrequencyMin.setMaxAccess(_A)
if mibBuilder.loadTexts:otxItuFrequencyMin.setStatus(_B)
_OtxItuFrequencyMax_Type=Integer32
_OtxItuFrequencyMax_Object=MibTableColumn
otxItuFrequencyMax=_OtxItuFrequencyMax_Object((1,3,6,1,4,1,17409,1,7,3,1,10),_OtxItuFrequencyMax_Type())
otxItuFrequencyMax.setMaxAccess(_A)
if mibBuilder.loadTexts:otxItuFrequencyMax.setStatus(_B)
_OtxItuFrequencyStep_Type=Integer32
_OtxItuFrequencyStep_Object=MibTableColumn
otxItuFrequencyStep=_OtxItuFrequencyStep_Object((1,3,6,1,4,1,17409,1,7,3,1,11),_OtxItuFrequencyStep_Type())
otxItuFrequencyStep.setMaxAccess(_A)
if mibBuilder.loadTexts:otxItuFrequencyStep.setStatus(_B)
_OtxInputRFLevel_Type=Integer32
_OtxInputRFLevel_Object=MibTableColumn
otxInputRFLevel=_OtxInputRFLevel_Object((1,3,6,1,4,1,17409,1,7,3,1,12),_OtxInputRFLevel_Type())
otxInputRFLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:otxInputRFLevel.setStatus(_B)
_OtxRfGain_Type=Integer32
_OtxRfGain_Object=MibTableColumn
otxRfGain=_OtxRfGain_Object((1,3,6,1,4,1,17409,1,7,3,1,13),_OtxRfGain_Type())
otxRfGain.setMaxAccess(_A)
if mibBuilder.loadTexts:otxRfGain.setStatus(_B)
_OtxLaserCurrent_Type=Integer32
_OtxLaserCurrent_Object=MibTableColumn
otxLaserCurrent=_OtxLaserCurrent_Object((1,3,6,1,4,1,17409,1,7,3,1,14),_OtxLaserCurrent_Type())
otxLaserCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:otxLaserCurrent.setStatus(_C)
_OtxLaserOutputPower_Type=Integer32
_OtxLaserOutputPower_Object=MibTableColumn
otxLaserOutputPower=_OtxLaserOutputPower_Object((1,3,6,1,4,1,17409,1,7,3,1,15),_OtxLaserOutputPower_Type())
otxLaserOutputPower.setMaxAccess(_A)
if mibBuilder.loadTexts:otxLaserOutputPower.setStatus(_C)
_OtxLaserTemperature_Type=Integer32
_OtxLaserTemperature_Object=MibTableColumn
otxLaserTemperature=_OtxLaserTemperature_Object((1,3,6,1,4,1,17409,1,7,3,1,16),_OtxLaserTemperature_Type())
otxLaserTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:otxLaserTemperature.setStatus(_C)
_OtxLaserTecCurrent_Type=Integer32
_OtxLaserTecCurrent_Object=MibTableColumn
otxLaserTecCurrent=_OtxLaserTecCurrent_Object((1,3,6,1,4,1,17409,1,7,3,1,17),_OtxLaserTecCurrent_Type())
otxLaserTecCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:otxLaserTecCurrent.setStatus(_C)
_OtxOmi_Type=Integer32
_OtxOmi_Object=MibTableColumn
otxOmi=_OtxOmi_Object((1,3,6,1,4,1,17409,1,7,3,1,18),_OtxOmi_Type())
otxOmi.setMaxAccess(_A)
if mibBuilder.loadTexts:otxOmi.setStatus(_B)
_OtxFansNumber_Type=Integer32
_OtxFansNumber_Object=MibScalar
otxFansNumber=_OtxFansNumber_Object((1,3,6,1,4,1,17409,1,7,4),_OtxFansNumber_Type())
otxFansNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:otxFansNumber.setStatus(_C)
_OtxFansTable_Object=MibTable
otxFansTable=_OtxFansTable_Object((1,3,6,1,4,1,17409,1,7,5))
if mibBuilder.loadTexts:otxFansTable.setStatus(_B)
_OtxFansEntry_Object=MibTableRow
otxFansEntry=_OtxFansEntry_Object((1,3,6,1,4,1,17409,1,7,5,1))
otxFansEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:otxFansEntry.setStatus(_B)
_OtxFansIndex_Type=Integer32
_OtxFansIndex_Object=MibTableColumn
otxFansIndex=_OtxFansIndex_Object((1,3,6,1,4,1,17409,1,7,5,1,1),_OtxFansIndex_Type())
otxFansIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:otxFansIndex.setStatus(_B)
class _OtxFansState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fault',2),(_G,3)))
_OtxFansState_Type.__name__=_D
_OtxFansState_Object=MibTableColumn
otxFansState=_OtxFansState_Object((1,3,6,1,4,1,17409,1,7,5,1,2),_OtxFansState_Type())
otxFansState.setMaxAccess(_A)
if mibBuilder.loadTexts:otxFansState.setStatus(_B)
_OtxFansSpeed_Type=Integer32
_OtxFansSpeed_Object=MibTableColumn
otxFansSpeed=_OtxFansSpeed_Object((1,3,6,1,4,1,17409,1,7,5,1,3),_OtxFansSpeed_Type())
otxFansSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:otxFansSpeed.setStatus(_B)
class _OtxFansControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_G,2)))
_OtxFansControl_Type.__name__=_D
_OtxFansControl_Object=MibTableColumn
otxFansControl=_OtxFansControl_Object((1,3,6,1,4,1,17409,1,7,5,1,4),_OtxFansControl_Type())
otxFansControl.setMaxAccess(_E)
if mibBuilder.loadTexts:otxFansControl.setStatus(_B)
_OtxFansName_Type=DisplayString
_OtxFansName_Object=MibTableColumn
otxFansName=_OtxFansName_Object((1,3,6,1,4,1,17409,1,7,5,1,5),_OtxFansName_Type())
otxFansName.setMaxAccess(_A)
if mibBuilder.loadTexts:otxFansName.setStatus(_B)
class _OtxNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_OtxNumberDCPowerSupply_Type.__name__=_D
_OtxNumberDCPowerSupply_Object=MibScalar
otxNumberDCPowerSupply=_OtxNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,7,6),_OtxNumberDCPowerSupply_Type())
otxNumberDCPowerSupply.setMaxAccess(_A)
if mibBuilder.loadTexts:otxNumberDCPowerSupply.setStatus(_C)
class _OtxDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2),('aloneSupply',3)))
_OtxDCPowerSupplyMode_Type.__name__=_D
_OtxDCPowerSupplyMode_Object=MibScalar
otxDCPowerSupplyMode=_OtxDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,7,7),_OtxDCPowerSupplyMode_Type())
otxDCPowerSupplyMode.setMaxAccess(_A)
if mibBuilder.loadTexts:otxDCPowerSupplyMode.setStatus(_B)
_OtxDCPowerTable_Object=MibTable
otxDCPowerTable=_OtxDCPowerTable_Object((1,3,6,1,4,1,17409,1,7,8))
if mibBuilder.loadTexts:otxDCPowerTable.setStatus(_C)
_OtxDCPowerEntry_Object=MibTableRow
otxDCPowerEntry=_OtxDCPowerEntry_Object((1,3,6,1,4,1,17409,1,7,8,1))
otxDCPowerEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:otxDCPowerEntry.setStatus(_C)
_OtxDCPowerIndex_Type=Integer32
_OtxDCPowerIndex_Object=MibTableColumn
otxDCPowerIndex=_OtxDCPowerIndex_Object((1,3,6,1,4,1,17409,1,7,8,1,1),_OtxDCPowerIndex_Type())
otxDCPowerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:otxDCPowerIndex.setStatus(_C)
class _OtxDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OtxDCPowerVoltage_Type.__name__=_D
_OtxDCPowerVoltage_Object=MibTableColumn
otxDCPowerVoltage=_OtxDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,7,8,1,2),_OtxDCPowerVoltage_Type())
otxDCPowerVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:otxDCPowerVoltage.setStatus(_C)
class _OtxDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OtxDCPowerCurrent_Type.__name__=_D
_OtxDCPowerCurrent_Object=MibTableColumn
otxDCPowerCurrent=_OtxDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,7,8,1,3),_OtxDCPowerCurrent_Type())
otxDCPowerCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:otxDCPowerCurrent.setStatus(_B)
_OtxDCPowerName_Type=DisplayString
_OtxDCPowerName_Object=MibTableColumn
otxDCPowerName=_OtxDCPowerName_Object((1,3,6,1,4,1,17409,1,7,8,1,4),_OtxDCPowerName_Type())
otxDCPowerName.setMaxAccess(_A)
if mibBuilder.loadTexts:otxDCPowerName.setStatus(_C)
mibBuilder.exportSymbols(_F,**{'otxVendorOID':otxVendorOID,'otxSlotNumber':otxSlotNumber,'otxModuleTable':otxModuleTable,'otxModuleEntry':otxModuleEntry,_H:otxModuleIndex,'otxLaserControl':otxLaserControl,'otxConfigurationAGCMode':otxConfigurationAGCMode,'otxConfigurationOmi':otxConfigurationOmi,'otxConfigurationRfGain':otxConfigurationRfGain,'otxConfigurationSbsSuppression':otxConfigurationSbsSuppression,'otxConfigurationChannelDistance':otxConfigurationChannelDistance,'otxConfigurationItuFrequency':otxConfigurationItuFrequency,'otxItuFrequencyMin':otxItuFrequencyMin,'otxItuFrequencyMax':otxItuFrequencyMax,'otxItuFrequencyStep':otxItuFrequencyStep,'otxInputRFLevel':otxInputRFLevel,'otxRfGain':otxRfGain,'otxLaserCurrent':otxLaserCurrent,'otxLaserOutputPower':otxLaserOutputPower,'otxLaserTemperature':otxLaserTemperature,'otxLaserTecCurrent':otxLaserTecCurrent,'otxOmi':otxOmi,'otxFansNumber':otxFansNumber,'otxFansTable':otxFansTable,'otxFansEntry':otxFansEntry,_I:otxFansIndex,'otxFansState':otxFansState,'otxFansSpeed':otxFansSpeed,'otxFansControl':otxFansControl,'otxFansName':otxFansName,'otxNumberDCPowerSupply':otxNumberDCPowerSupply,'otxDCPowerSupplyMode':otxDCPowerSupplyMode,'otxDCPowerTable':otxDCPowerTable,'otxDCPowerEntry':otxDCPowerEntry,_J:otxDCPowerIndex,'otxDCPowerVoltage':otxDCPowerVoltage,'otxDCPowerCurrent':otxDCPowerCurrent,'otxDCPowerName':otxDCPowerName})