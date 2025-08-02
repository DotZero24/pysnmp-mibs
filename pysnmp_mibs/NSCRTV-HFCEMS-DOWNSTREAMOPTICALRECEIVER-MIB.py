_I='dorDCPowerIndex'
_H='dorOutputIndex'
_G='dorInputIndex'
_F='NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB'
_E='optional'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dorIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','dorIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_DorVendorOID_Type=ObjectIdentifier
_DorVendorOID_Object=MibScalar
dorVendorOID=_DorVendorOID_Object((1,3,6,1,4,1,17409,1,9,1),_DorVendorOID_Type())
dorVendorOID.setMaxAccess(_B)
if mibBuilder.loadTexts:dorVendorOID.setStatus(_E)
_DorRxInputNumber_Type=Integer32
_DorRxInputNumber_Object=MibScalar
dorRxInputNumber=_DorRxInputNumber_Object((1,3,6,1,4,1,17409,1,9,2),_DorRxInputNumber_Type())
dorRxInputNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dorRxInputNumber.setStatus(_A)
_DorRxInputTable_Object=MibTable
dorRxInputTable=_DorRxInputTable_Object((1,3,6,1,4,1,17409,1,9,3))
if mibBuilder.loadTexts:dorRxInputTable.setStatus(_A)
_DorRxInputEntry_Object=MibTableRow
dorRxInputEntry=_DorRxInputEntry_Object((1,3,6,1,4,1,17409,1,9,3,1))
dorRxInputEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dorRxInputEntry.setStatus(_A)
_DorInputIndex_Type=Integer32
_DorInputIndex_Object=MibTableColumn
dorInputIndex=_DorInputIndex_Object((1,3,6,1,4,1,17409,1,9,3,1,1),_DorInputIndex_Type())
dorInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dorInputIndex.setStatus(_A)
_DorInputPower_Type=Integer32
_DorInputPower_Object=MibTableColumn
dorInputPower=_DorInputPower_Object((1,3,6,1,4,1,17409,1,9,3,1,2),_DorInputPower_Type())
dorInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dorInputPower.setStatus(_A)
_DorInputWavelengthControl_Type=Integer32
_DorInputWavelengthControl_Object=MibTableColumn
dorInputWavelengthControl=_DorInputWavelengthControl_Object((1,3,6,1,4,1,17409,1,9,3,1,3),_DorInputWavelengthControl_Type())
dorInputWavelengthControl.setMaxAccess(_D)
if mibBuilder.loadTexts:dorInputWavelengthControl.setStatus(_A)
class _DorInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('fault',2)))
_DorInputStatus_Type.__name__=_C
_DorInputStatus_Object=MibTableColumn
dorInputStatus=_DorInputStatus_Object((1,3,6,1,4,1,17409,1,9,3,1,4),_DorInputStatus_Type())
dorInputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dorInputStatus.setStatus(_A)
_DorRxOutputNumber_Type=Integer32
_DorRxOutputNumber_Object=MibScalar
dorRxOutputNumber=_DorRxOutputNumber_Object((1,3,6,1,4,1,17409,1,9,4),_DorRxOutputNumber_Type())
dorRxOutputNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dorRxOutputNumber.setStatus(_A)
_DorRxOutputTable_Object=MibTable
dorRxOutputTable=_DorRxOutputTable_Object((1,3,6,1,4,1,17409,1,9,5))
if mibBuilder.loadTexts:dorRxOutputTable.setStatus(_A)
_DorRxOutputEntry_Object=MibTableRow
dorRxOutputEntry=_DorRxOutputEntry_Object((1,3,6,1,4,1,17409,1,9,5,1))
dorRxOutputEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:dorRxOutputEntry.setStatus(_A)
_DorOutputIndex_Type=Integer32
_DorOutputIndex_Object=MibTableColumn
dorOutputIndex=_DorOutputIndex_Object((1,3,6,1,4,1,17409,1,9,5,1,1),_DorOutputIndex_Type())
dorOutputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dorOutputIndex.setStatus(_A)
class _DorOutputControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_DorOutputControl_Type.__name__=_C
_DorOutputControl_Object=MibTableColumn
dorOutputControl=_DorOutputControl_Object((1,3,6,1,4,1,17409,1,9,5,1,2),_DorOutputControl_Type())
dorOutputControl.setMaxAccess(_D)
if mibBuilder.loadTexts:dorOutputControl.setStatus(_A)
class _DorOutputGainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('constantLevel',1),('constantGain',2)))
_DorOutputGainType_Type.__name__=_C
_DorOutputGainType_Object=MibTableColumn
dorOutputGainType=_DorOutputGainType_Object((1,3,6,1,4,1,17409,1,9,5,1,3),_DorOutputGainType_Type())
dorOutputGainType.setMaxAccess(_D)
if mibBuilder.loadTexts:dorOutputGainType.setStatus(_E)
_DorOutputLevel_Type=Integer32
_DorOutputLevel_Object=MibTableColumn
dorOutputLevel=_DorOutputLevel_Object((1,3,6,1,4,1,17409,1,9,5,1,4),_DorOutputLevel_Type())
dorOutputLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dorOutputLevel.setStatus(_A)
_DorConfiguartionOutputLevel_Type=Integer32
_DorConfiguartionOutputLevel_Object=MibTableColumn
dorConfiguartionOutputLevel=_DorConfiguartionOutputLevel_Object((1,3,6,1,4,1,17409,1,9,5,1,5),_DorConfiguartionOutputLevel_Type())
dorConfiguartionOutputLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:dorConfiguartionOutputLevel.setStatus(_E)
_DorOutputRFlevelatt_Type=Integer32
_DorOutputRFlevelatt_Object=MibTableColumn
dorOutputRFlevelatt=_DorOutputRFlevelatt_Object((1,3,6,1,4,1,17409,1,9,5,1,6),_DorOutputRFlevelatt_Type())
dorOutputRFlevelatt.setMaxAccess(_D)
if mibBuilder.loadTexts:dorOutputRFlevelatt.setStatus(_A)
_DorConfigurationOutputRFlevelatt_Type=Integer32
_DorConfigurationOutputRFlevelatt_Object=MibTableColumn
dorConfigurationOutputRFlevelatt=_DorConfigurationOutputRFlevelatt_Object((1,3,6,1,4,1,17409,1,9,5,1,7),_DorConfigurationOutputRFlevelatt_Type())
dorConfigurationOutputRFlevelatt.setMaxAccess(_D)
if mibBuilder.loadTexts:dorConfigurationOutputRFlevelatt.setStatus(_E)
_DorOutputRFName_Type=DisplayString
_DorOutputRFName_Object=MibTableColumn
dorOutputRFName=_DorOutputRFName_Object((1,3,6,1,4,1,17409,1,9,5,1,8),_DorOutputRFName_Type())
dorOutputRFName.setMaxAccess(_B)
if mibBuilder.loadTexts:dorOutputRFName.setStatus(_A)
class _DorNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_DorNumberDCPowerSupply_Type.__name__=_C
_DorNumberDCPowerSupply_Object=MibScalar
dorNumberDCPowerSupply=_DorNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,9,6),_DorNumberDCPowerSupply_Type())
dorNumberDCPowerSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:dorNumberDCPowerSupply.setStatus(_A)
class _DorDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2),('aloneSupply',3)))
_DorDCPowerSupplyMode_Type.__name__=_C
_DorDCPowerSupplyMode_Object=MibScalar
dorDCPowerSupplyMode=_DorDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,9,7),_DorDCPowerSupplyMode_Type())
dorDCPowerSupplyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dorDCPowerSupplyMode.setStatus(_E)
_DorDCPowerTable_Object=MibTable
dorDCPowerTable=_DorDCPowerTable_Object((1,3,6,1,4,1,17409,1,9,8))
if mibBuilder.loadTexts:dorDCPowerTable.setStatus(_A)
_DorDCPowerEntry_Object=MibTableRow
dorDCPowerEntry=_DorDCPowerEntry_Object((1,3,6,1,4,1,17409,1,9,8,1))
dorDCPowerEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:dorDCPowerEntry.setStatus(_A)
_DorDCPowerIndex_Type=Integer32
_DorDCPowerIndex_Object=MibTableColumn
dorDCPowerIndex=_DorDCPowerIndex_Object((1,3,6,1,4,1,17409,1,9,8,1,1),_DorDCPowerIndex_Type())
dorDCPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dorDCPowerIndex.setStatus(_A)
class _DorDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_DorDCPowerVoltage_Type.__name__=_C
_DorDCPowerVoltage_Object=MibTableColumn
dorDCPowerVoltage=_DorDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,9,8,1,2),_DorDCPowerVoltage_Type())
dorDCPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dorDCPowerVoltage.setStatus(_A)
class _DorDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DorDCPowerCurrent_Type.__name__=_C
_DorDCPowerCurrent_Object=MibTableColumn
dorDCPowerCurrent=_DorDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,9,8,1,3),_DorDCPowerCurrent_Type())
dorDCPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:dorDCPowerCurrent.setStatus(_E)
_DorDCPowerName_Type=DisplayString
_DorDCPowerName_Object=MibTableColumn
dorDCPowerName=_DorDCPowerName_Object((1,3,6,1,4,1,17409,1,9,8,1,4),_DorDCPowerName_Type())
dorDCPowerName.setMaxAccess(_B)
if mibBuilder.loadTexts:dorDCPowerName.setStatus(_A)
class _DorReverseOptPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_DorReverseOptPower_Type.__name__=_C
_DorReverseOptPower_Object=MibScalar
dorReverseOptPower=_DorReverseOptPower_Object((1,3,6,1,4,1,17409,1,9,9),_DorReverseOptPower_Type())
dorReverseOptPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dorReverseOptPower.setStatus(_A)
class _DorReverseCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DorReverseCurrent_Type.__name__=_C
_DorReverseCurrent_Object=MibScalar
dorReverseCurrent=_DorReverseCurrent_Object((1,3,6,1,4,1,17409,1,9,10),_DorReverseCurrent_Type())
dorReverseCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:dorReverseCurrent.setStatus(_A)
class _DorChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DorChannelNum_Type.__name__=_C
_DorChannelNum_Object=MibScalar
dorChannelNum=_DorChannelNum_Object((1,3,6,1,4,1,17409,1,9,11),_DorChannelNum_Type())
dorChannelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:dorChannelNum.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'dorVendorOID':dorVendorOID,'dorRxInputNumber':dorRxInputNumber,'dorRxInputTable':dorRxInputTable,'dorRxInputEntry':dorRxInputEntry,_G:dorInputIndex,'dorInputPower':dorInputPower,'dorInputWavelengthControl':dorInputWavelengthControl,'dorInputStatus':dorInputStatus,'dorRxOutputNumber':dorRxOutputNumber,'dorRxOutputTable':dorRxOutputTable,'dorRxOutputEntry':dorRxOutputEntry,_H:dorOutputIndex,'dorOutputControl':dorOutputControl,'dorOutputGainType':dorOutputGainType,'dorOutputLevel':dorOutputLevel,'dorConfiguartionOutputLevel':dorConfiguartionOutputLevel,'dorOutputRFlevelatt':dorOutputRFlevelatt,'dorConfigurationOutputRFlevelatt':dorConfigurationOutputRFlevelatt,'dorOutputRFName':dorOutputRFName,'dorNumberDCPowerSupply':dorNumberDCPowerSupply,'dorDCPowerSupplyMode':dorDCPowerSupplyMode,'dorDCPowerTable':dorDCPowerTable,'dorDCPowerEntry':dorDCPowerEntry,_I:dorDCPowerIndex,'dorDCPowerVoltage':dorDCPowerVoltage,'dorDCPowerCurrent':dorDCPowerCurrent,'dorDCPowerName':dorDCPowerName,'dorReverseOptPower':dorReverseOptPower,'dorReverseCurrent':dorReverseCurrent,'dorChannelNum':dorChannelNum})