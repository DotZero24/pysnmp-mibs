_J='otdDCPowerIndex'
_I='otdFansIndex'
_H='otdIndex'
_G='off'
_F='NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB'
_E='read-write'
_D='mandatory'
_C='Integer32'
_B='optional'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
otdIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','otdIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_OtdVendorOID_Type=ObjectIdentifier
_OtdVendorOID_Object=MibScalar
otdVendorOID=_OtdVendorOID_Object((1,3,6,1,4,1,17409,1,6,1),_OtdVendorOID_Type())
otdVendorOID.setMaxAccess(_A)
if mibBuilder.loadTexts:otdVendorOID.setStatus(_B)
class _OtdSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_OtdSlotNumber_Type.__name__=_C
_OtdSlotNumber_Object=MibScalar
otdSlotNumber=_OtdSlotNumber_Object((1,3,6,1,4,1,17409,1,6,2),_OtdSlotNumber_Type())
otdSlotNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:otdSlotNumber.setStatus(_D)
_OtdOptDeviceTable_Object=MibTable
otdOptDeviceTable=_OtdOptDeviceTable_Object((1,3,6,1,4,1,17409,1,6,3))
if mibBuilder.loadTexts:otdOptDeviceTable.setStatus(_D)
_OtdOptDeviceEntry_Object=MibTableRow
otdOptDeviceEntry=_OtdOptDeviceEntry_Object((1,3,6,1,4,1,17409,1,6,3,1))
otdOptDeviceEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:otdOptDeviceEntry.setStatus(_D)
class _OtdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_OtdIndex_Type.__name__=_C
_OtdIndex_Object=MibTableColumn
otdIndex=_OtdIndex_Object((1,3,6,1,4,1,17409,1,6,3,1,1),_OtdIndex_Type())
otdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:otdIndex.setStatus(_D)
_OtdLaserWavelength_Type=DisplayString
_OtdLaserWavelength_Object=MibTableColumn
otdLaserWavelength=_OtdLaserWavelength_Object((1,3,6,1,4,1,17409,1,6,3,1,2),_OtdLaserWavelength_Type())
otdLaserWavelength.setMaxAccess(_A)
if mibBuilder.loadTexts:otdLaserWavelength.setStatus(_D)
_OtdLaserType_Type=DisplayString
_OtdLaserType_Object=MibTableColumn
otdLaserType=_OtdLaserType_Object((1,3,6,1,4,1,17409,1,6,3,1,3),_OtdLaserType_Type())
otdLaserType.setMaxAccess(_A)
if mibBuilder.loadTexts:otdLaserType.setStatus(_B)
class _OtdDriveLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_OtdDriveLevel_Type.__name__=_C
_OtdDriveLevel_Object=MibTableColumn
otdDriveLevel=_OtdDriveLevel_Object((1,3,6,1,4,1,17409,1,6,3,1,4),_OtdDriveLevel_Type())
otdDriveLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:otdDriveLevel.setStatus(_B)
class _OtdInputRFLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_OtdInputRFLevel_Type.__name__=_C
_OtdInputRFLevel_Object=MibTableColumn
otdInputRFLevel=_OtdInputRFLevel_Object((1,3,6,1,4,1,17409,1,6,3,1,5),_OtdInputRFLevel_Type())
otdInputRFLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:otdInputRFLevel.setStatus(_B)
class _OtdInputRFAttenuationRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_OtdInputRFAttenuationRange_Type.__name__=_C
_OtdInputRFAttenuationRange_Object=MibTableColumn
otdInputRFAttenuationRange=_OtdInputRFAttenuationRange_Object((1,3,6,1,4,1,17409,1,6,3,1,6),_OtdInputRFAttenuationRange_Type())
otdInputRFAttenuationRange.setMaxAccess(_A)
if mibBuilder.loadTexts:otdInputRFAttenuationRange.setStatus(_B)
class _OtdInputRFAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OtdInputRFAttenuation_Type.__name__=_C
_OtdInputRFAttenuation_Object=MibTableColumn
otdInputRFAttenuation=_OtdInputRFAttenuation_Object((1,3,6,1,4,1,17409,1,6,3,1,7),_OtdInputRFAttenuation_Type())
otdInputRFAttenuation.setMaxAccess(_E)
if mibBuilder.loadTexts:otdInputRFAttenuation.setStatus(_B)
class _OtdLaserTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OtdLaserTemp_Type.__name__=_C
_OtdLaserTemp_Object=MibTableColumn
otdLaserTemp=_OtdLaserTemp_Object((1,3,6,1,4,1,17409,1,6,3,1,8),_OtdLaserTemp_Type())
otdLaserTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:otdLaserTemp.setStatus(_D)
class _OtdLaserCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OtdLaserCurrent_Type.__name__=_C
_OtdLaserCurrent_Object=MibTableColumn
otdLaserCurrent=_OtdLaserCurrent_Object((1,3,6,1,4,1,17409,1,6,3,1,9),_OtdLaserCurrent_Type())
otdLaserCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:otdLaserCurrent.setStatus(_D)
class _OtdOpicalOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_OtdOpicalOutputPower_Type.__name__=_C
_OtdOpicalOutputPower_Object=MibTableColumn
otdOpicalOutputPower=_OtdOpicalOutputPower_Object((1,3,6,1,4,1,17409,1,6,3,1,10),_OtdOpicalOutputPower_Type())
otdOpicalOutputPower.setMaxAccess(_A)
if mibBuilder.loadTexts:otdOpicalOutputPower.setStatus(_D)
class _OtdTecCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OtdTecCurrent_Type.__name__=_C
_OtdTecCurrent_Object=MibTableColumn
otdTecCurrent=_OtdTecCurrent_Object((1,3,6,1,4,1,17409,1,6,3,1,11),_OtdTecCurrent_Type())
otdTecCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:otdTecCurrent.setStatus(_B)
class _OtdAGCControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('on',2)))
_OtdAGCControl_Type.__name__=_C
_OtdAGCControl_Object=MibTableColumn
otdAGCControl=_OtdAGCControl_Object((1,3,6,1,4,1,17409,1,6,3,1,12),_OtdAGCControl_Type())
otdAGCControl.setMaxAccess(_E)
if mibBuilder.loadTexts:otdAGCControl.setStatus(_B)
_OtdConfigurationDriveLevel_Type=Integer32
_OtdConfigurationDriveLevel_Object=MibTableColumn
otdConfigurationDriveLevel=_OtdConfigurationDriveLevel_Object((1,3,6,1,4,1,17409,1,6,3,1,13),_OtdConfigurationDriveLevel_Type())
otdConfigurationDriveLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:otdConfigurationDriveLevel.setStatus(_B)
_OtdConfigurationRFAttenuation_Type=Integer32
_OtdConfigurationRFAttenuation_Object=MibTableColumn
otdConfigurationRFAttenuation=_OtdConfigurationRFAttenuation_Object((1,3,6,1,4,1,17409,1,6,3,1,14),_OtdConfigurationRFAttenuation_Type())
otdConfigurationRFAttenuation.setMaxAccess(_E)
if mibBuilder.loadTexts:otdConfigurationRFAttenuation.setStatus(_B)
_OtdConfigurationRFChannels_Type=Integer32
_OtdConfigurationRFChannels_Object=MibTableColumn
otdConfigurationRFChannels=_OtdConfigurationRFChannels_Object((1,3,6,1,4,1,17409,1,6,3,1,15),_OtdConfigurationRFChannels_Type())
otdConfigurationRFChannels.setMaxAccess(_E)
if mibBuilder.loadTexts:otdConfigurationRFChannels.setStatus(_B)
_OtdFansNumber_Type=Integer32
_OtdFansNumber_Object=MibScalar
otdFansNumber=_OtdFansNumber_Object((1,3,6,1,4,1,17409,1,6,4),_OtdFansNumber_Type())
otdFansNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:otdFansNumber.setStatus(_D)
_OtdFansTable_Object=MibTable
otdFansTable=_OtdFansTable_Object((1,3,6,1,4,1,17409,1,6,5))
if mibBuilder.loadTexts:otdFansTable.setStatus(_B)
_OtdFansEntry_Object=MibTableRow
otdFansEntry=_OtdFansEntry_Object((1,3,6,1,4,1,17409,1,6,5,1))
otdFansEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:otdFansEntry.setStatus(_B)
_OtdFansIndex_Type=Integer32
_OtdFansIndex_Object=MibTableColumn
otdFansIndex=_OtdFansIndex_Object((1,3,6,1,4,1,17409,1,6,5,1,1),_OtdFansIndex_Type())
otdFansIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:otdFansIndex.setStatus(_B)
class _OtdFansState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fault',2),(_G,3)))
_OtdFansState_Type.__name__=_C
_OtdFansState_Object=MibTableColumn
otdFansState=_OtdFansState_Object((1,3,6,1,4,1,17409,1,6,5,1,2),_OtdFansState_Type())
otdFansState.setMaxAccess(_A)
if mibBuilder.loadTexts:otdFansState.setStatus(_B)
_OtdFansSpeed_Type=Integer32
_OtdFansSpeed_Object=MibTableColumn
otdFansSpeed=_OtdFansSpeed_Object((1,3,6,1,4,1,17409,1,6,5,1,3),_OtdFansSpeed_Type())
otdFansSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:otdFansSpeed.setStatus(_B)
class _OtdFansControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_G,2)))
_OtdFansControl_Type.__name__=_C
_OtdFansControl_Object=MibTableColumn
otdFansControl=_OtdFansControl_Object((1,3,6,1,4,1,17409,1,6,5,1,4),_OtdFansControl_Type())
otdFansControl.setMaxAccess(_E)
if mibBuilder.loadTexts:otdFansControl.setStatus(_B)
_OtdFansName_Type=DisplayString
_OtdFansName_Object=MibTableColumn
otdFansName=_OtdFansName_Object((1,3,6,1,4,1,17409,1,6,5,1,5),_OtdFansName_Type())
otdFansName.setMaxAccess(_A)
if mibBuilder.loadTexts:otdFansName.setStatus(_B)
class _OtdNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_OtdNumberDCPowerSupply_Type.__name__=_C
_OtdNumberDCPowerSupply_Object=MibScalar
otdNumberDCPowerSupply=_OtdNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,6,6),_OtdNumberDCPowerSupply_Type())
otdNumberDCPowerSupply.setMaxAccess(_A)
if mibBuilder.loadTexts:otdNumberDCPowerSupply.setStatus(_D)
class _OtdDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedredundant',2),('alonesupply',3)))
_OtdDCPowerSupplyMode_Type.__name__=_C
_OtdDCPowerSupplyMode_Object=MibScalar
otdDCPowerSupplyMode=_OtdDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,6,7),_OtdDCPowerSupplyMode_Type())
otdDCPowerSupplyMode.setMaxAccess(_A)
if mibBuilder.loadTexts:otdDCPowerSupplyMode.setStatus(_B)
_OtdDCPowerTable_Object=MibTable
otdDCPowerTable=_OtdDCPowerTable_Object((1,3,6,1,4,1,17409,1,6,8))
if mibBuilder.loadTexts:otdDCPowerTable.setStatus(_D)
_OtdDCPowerEntry_Object=MibTableRow
otdDCPowerEntry=_OtdDCPowerEntry_Object((1,3,6,1,4,1,17409,1,6,8,1))
otdDCPowerEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:otdDCPowerEntry.setStatus(_D)
_OtdDCPowerIndex_Type=Integer32
_OtdDCPowerIndex_Object=MibTableColumn
otdDCPowerIndex=_OtdDCPowerIndex_Object((1,3,6,1,4,1,17409,1,6,8,1,1),_OtdDCPowerIndex_Type())
otdDCPowerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:otdDCPowerIndex.setStatus(_D)
class _OtdDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OtdDCPowerVoltage_Type.__name__=_C
_OtdDCPowerVoltage_Object=MibTableColumn
otdDCPowerVoltage=_OtdDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,6,8,1,2),_OtdDCPowerVoltage_Type())
otdDCPowerVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:otdDCPowerVoltage.setStatus(_D)
class _OtdDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OtdDCPowerCurrent_Type.__name__=_C
_OtdDCPowerCurrent_Object=MibTableColumn
otdDCPowerCurrent=_OtdDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,6,8,1,3),_OtdDCPowerCurrent_Type())
otdDCPowerCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:otdDCPowerCurrent.setStatus(_B)
_OtdDCPowerName_Type=DisplayString
_OtdDCPowerName_Object=MibTableColumn
otdDCPowerName=_OtdDCPowerName_Object((1,3,6,1,4,1,17409,1,6,8,1,4),_OtdDCPowerName_Type())
otdDCPowerName.setMaxAccess(_A)
if mibBuilder.loadTexts:otdDCPowerName.setStatus(_D)
mibBuilder.exportSymbols(_F,**{'otdVendorOID':otdVendorOID,'otdSlotNumber':otdSlotNumber,'otdOptDeviceTable':otdOptDeviceTable,'otdOptDeviceEntry':otdOptDeviceEntry,_H:otdIndex,'otdLaserWavelength':otdLaserWavelength,'otdLaserType':otdLaserType,'otdDriveLevel':otdDriveLevel,'otdInputRFLevel':otdInputRFLevel,'otdInputRFAttenuationRange':otdInputRFAttenuationRange,'otdInputRFAttenuation':otdInputRFAttenuation,'otdLaserTemp':otdLaserTemp,'otdLaserCurrent':otdLaserCurrent,'otdOpicalOutputPower':otdOpicalOutputPower,'otdTecCurrent':otdTecCurrent,'otdAGCControl':otdAGCControl,'otdConfigurationDriveLevel':otdConfigurationDriveLevel,'otdConfigurationRFAttenuation':otdConfigurationRFAttenuation,'otdConfigurationRFChannels':otdConfigurationRFChannels,'otdFansNumber':otdFansNumber,'otdFansTable':otdFansTable,'otdFansEntry':otdFansEntry,_I:otdFansIndex,'otdFansState':otdFansState,'otdFansSpeed':otdFansSpeed,'otdFansControl':otdFansControl,'otdFansName':otdFansName,'otdNumberDCPowerSupply':otdNumberDCPowerSupply,'otdDCPowerSupplyMode':otdDCPowerSupplyMode,'otdDCPowerTable':otdDCPowerTable,'otdDCPowerEntry':otdDCPowerEntry,_J:otdDCPowerIndex,'otdDCPowerVoltage':otdDCPowerVoltage,'otdDCPowerCurrent':otdDCPowerCurrent,'otdDCPowerName':otdDCPowerName})