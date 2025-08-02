_I='addDCPowerIndex'
_H='addRFPortIndex'
_G='NSCRTV-HFCEMS-AMPLIFIER-MIB'
_F='none'
_E='read-write'
_D='mandatory'
_C='optional'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
addIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','addIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_AddVendorOID_Type=ObjectIdentifier
_AddVendorOID_Object=MibScalar
addVendorOID=_AddVendorOID_Object((1,3,6,1,4,1,17409,1,12,1),_AddVendorOID_Type())
addVendorOID.setMaxAccess(_B)
if mibBuilder.loadTexts:addVendorOID.setStatus(_C)
class _AddNumberRFPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AddNumberRFPort_Type.__name__=_A
_AddNumberRFPort_Object=MibScalar
addNumberRFPort=_AddNumberRFPort_Object((1,3,6,1,4,1,17409,1,12,2),_AddNumberRFPort_Type())
addNumberRFPort.setMaxAccess(_B)
if mibBuilder.loadTexts:addNumberRFPort.setStatus(_D)
class _AddPortMasterAttenuationControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('low',2),('high',3)))
_AddPortMasterAttenuationControl_Type.__name__=_A
_AddPortMasterAttenuationControl_Object=MibScalar
addPortMasterAttenuationControl=_AddPortMasterAttenuationControl_Object((1,3,6,1,4,1,17409,1,12,3),_AddPortMasterAttenuationControl_Type())
addPortMasterAttenuationControl.setMaxAccess(_E)
if mibBuilder.loadTexts:addPortMasterAttenuationControl.setStatus(_C)
_AddRFPortTable_Object=MibTable
addRFPortTable=_AddRFPortTable_Object((1,3,6,1,4,1,17409,1,12,4))
if mibBuilder.loadTexts:addRFPortTable.setStatus(_D)
_AddRFPortEntry_Object=MibTableRow
addRFPortEntry=_AddRFPortEntry_Object((1,3,6,1,4,1,17409,1,12,4,1))
addRFPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:addRFPortEntry.setStatus(_D)
_AddRFPortIndex_Type=Integer32
_AddRFPortIndex_Object=MibTableColumn
addRFPortIndex=_AddRFPortIndex_Object((1,3,6,1,4,1,17409,1,12,4,1,1),_AddRFPortIndex_Type())
addRFPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortIndex.setStatus(_D)
class _AddRFPortControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('alc',1),('asc',2),('agc',3),(_F,4)))
_AddRFPortControlType_Type.__name__=_A
_AddRFPortControlType_Object=MibTableColumn
addRFPortControlType=_AddRFPortControlType_Object((1,3,6,1,4,1,17409,1,12,4,1,2),_AddRFPortControlType_Type())
addRFPortControlType.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortControlType.setStatus(_C)
_AddRFPortControlLevel_Type=Integer32
_AddRFPortControlLevel_Object=MibTableColumn
addRFPortControlLevel=_AddRFPortControlLevel_Object((1,3,6,1,4,1,17409,1,12,4,1,3),_AddRFPortControlLevel_Type())
addRFPortControlLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortControlLevel.setStatus(_C)
class _AddRFPortOutputRFLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AddRFPortOutputRFLevel_Type.__name__=_A
_AddRFPortOutputRFLevel_Object=MibTableColumn
addRFPortOutputRFLevel=_AddRFPortOutputRFLevel_Object((1,3,6,1,4,1,17409,1,12,4,1,4),_AddRFPortOutputRFLevel_Type())
addRFPortOutputRFLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortOutputRFLevel.setStatus(_C)
_AddRFPortName_Type=DisplayString
_AddRFPortName_Object=MibTableColumn
addRFPortName=_AddRFPortName_Object((1,3,6,1,4,1,17409,1,12,4,1,5),_AddRFPortName_Type())
addRFPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortName.setStatus(_D)
class _AddRFPortReverseAttenuationControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('low',2),('high',3)))
_AddRFPortReverseAttenuationControl_Type.__name__=_A
_AddRFPortReverseAttenuationControl_Object=MibTableColumn
addRFPortReverseAttenuationControl=_AddRFPortReverseAttenuationControl_Object((1,3,6,1,4,1,17409,1,12,4,1,6),_AddRFPortReverseAttenuationControl_Type())
addRFPortReverseAttenuationControl.setMaxAccess(_E)
if mibBuilder.loadTexts:addRFPortReverseAttenuationControl.setStatus(_C)
class _AddRFPortPowerFeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AddRFPortPowerFeedStatus_Type.__name__=_A
_AddRFPortPowerFeedStatus_Object=MibTableColumn
addRFPortPowerFeedStatus=_AddRFPortPowerFeedStatus_Object((1,3,6,1,4,1,17409,1,12,4,1,7),_AddRFPortPowerFeedStatus_Type())
addRFPortPowerFeedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortPowerFeedStatus.setStatus(_C)
class _AddRFPortInputRFLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AddRFPortInputRFLevel_Type.__name__=_A
_AddRFPortInputRFLevel_Object=MibTableColumn
addRFPortInputRFLevel=_AddRFPortInputRFLevel_Object((1,3,6,1,4,1,17409,1,12,4,1,8),_AddRFPortInputRFLevel_Type())
addRFPortInputRFLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:addRFPortInputRFLevel.setStatus(_C)
class _AddRFPortattenuation1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_AddRFPortattenuation1_Type.__name__=_A
_AddRFPortattenuation1_Object=MibTableColumn
addRFPortattenuation1=_AddRFPortattenuation1_Object((1,3,6,1,4,1,17409,1,12,4,1,9),_AddRFPortattenuation1_Type())
addRFPortattenuation1.setMaxAccess(_E)
if mibBuilder.loadTexts:addRFPortattenuation1.setStatus(_C)
class _AddRFPortattenuation2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_AddRFPortattenuation2_Type.__name__=_A
_AddRFPortattenuation2_Object=MibTableColumn
addRFPortattenuation2=_AddRFPortattenuation2_Object((1,3,6,1,4,1,17409,1,12,4,1,10),_AddRFPortattenuation2_Type())
addRFPortattenuation2.setMaxAccess(_E)
if mibBuilder.loadTexts:addRFPortattenuation2.setStatus(_C)
class _AddRFPorteq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AddRFPorteq_Type.__name__=_A
_AddRFPorteq_Object=MibTableColumn
addRFPorteq=_AddRFPorteq_Object((1,3,6,1,4,1,17409,1,12,4,1,11),_AddRFPorteq_Type())
addRFPorteq.setMaxAccess(_E)
if mibBuilder.loadTexts:addRFPorteq.setStatus(_C)
class _AddLinePowerVoltage1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AddLinePowerVoltage1_Type.__name__=_A
_AddLinePowerVoltage1_Object=MibScalar
addLinePowerVoltage1=_AddLinePowerVoltage1_Object((1,3,6,1,4,1,17409,1,12,5),_AddLinePowerVoltage1_Type())
addLinePowerVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:addLinePowerVoltage1.setStatus(_C)
class _AddLinePowerVoltage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AddLinePowerVoltage2_Type.__name__=_A
_AddLinePowerVoltage2_Object=MibScalar
addLinePowerVoltage2=_AddLinePowerVoltage2_Object((1,3,6,1,4,1,17409,1,12,6),_AddLinePowerVoltage2_Type())
addLinePowerVoltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:addLinePowerVoltage2.setStatus(_C)
class _AddLinePowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AddLinePowerCurrent_Type.__name__=_A
_AddLinePowerCurrent_Object=MibScalar
addLinePowerCurrent=_AddLinePowerCurrent_Object((1,3,6,1,4,1,17409,1,12,7),_AddLinePowerCurrent_Type())
addLinePowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:addLinePowerCurrent.setStatus(_C)
class _AddNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AddNumberDCPowerSupply_Type.__name__=_A
_AddNumberDCPowerSupply_Object=MibScalar
addNumberDCPowerSupply=_AddNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,12,8),_AddNumberDCPowerSupply_Type())
addNumberDCPowerSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:addNumberDCPowerSupply.setStatus(_D)
class _AddDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2),('aloneSupply',3)))
_AddDCPowerSupplyMode_Type.__name__=_A
_AddDCPowerSupplyMode_Object=MibScalar
addDCPowerSupplyMode=_AddDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,12,9),_AddDCPowerSupplyMode_Type())
addDCPowerSupplyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:addDCPowerSupplyMode.setStatus(_C)
_AddDCPowerTable_Object=MibTable
addDCPowerTable=_AddDCPowerTable_Object((1,3,6,1,4,1,17409,1,12,10))
if mibBuilder.loadTexts:addDCPowerTable.setStatus(_D)
_AddDCPowerEntry_Object=MibTableRow
addDCPowerEntry=_AddDCPowerEntry_Object((1,3,6,1,4,1,17409,1,12,10,1))
addDCPowerEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:addDCPowerEntry.setStatus(_D)
_AddDCPowerIndex_Type=Integer32
_AddDCPowerIndex_Object=MibTableColumn
addDCPowerIndex=_AddDCPowerIndex_Object((1,3,6,1,4,1,17409,1,12,10,1,1),_AddDCPowerIndex_Type())
addDCPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:addDCPowerIndex.setStatus(_D)
class _AddDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_AddDCPowerVoltage_Type.__name__=_A
_AddDCPowerVoltage_Object=MibTableColumn
addDCPowerVoltage=_AddDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,12,10,1,2),_AddDCPowerVoltage_Type())
addDCPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:addDCPowerVoltage.setStatus(_D)
class _AddDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AddDCPowerCurrent_Type.__name__=_A
_AddDCPowerCurrent_Object=MibTableColumn
addDCPowerCurrent=_AddDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,12,10,1,3),_AddDCPowerCurrent_Type())
addDCPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:addDCPowerCurrent.setStatus(_C)
_AddDCPowerName_Type=DisplayString
_AddDCPowerName_Object=MibTableColumn
addDCPowerName=_AddDCPowerName_Object((1,3,6,1,4,1,17409,1,12,10,1,4),_AddDCPowerName_Type())
addDCPowerName.setMaxAccess(_B)
if mibBuilder.loadTexts:addDCPowerName.setStatus(_D)
class _AddChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_AddChannelNumber_Type.__name__=_A
_AddChannelNumber_Object=MibScalar
addChannelNumber=_AddChannelNumber_Object((1,3,6,1,4,1,17409,1,12,11),_AddChannelNumber_Type())
addChannelNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:addChannelNumber.setStatus(_D)
class _AddFanControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_AddFanControl_Type.__name__=_A
_AddFanControl_Object=MibScalar
addFanControl=_AddFanControl_Object((1,3,6,1,4,1,17409,1,12,12),_AddFanControl_Type())
addFanControl.setMaxAccess(_E)
if mibBuilder.loadTexts:addFanControl.setStatus(_D)
mibBuilder.exportSymbols(_G,**{'addVendorOID':addVendorOID,'addNumberRFPort':addNumberRFPort,'addPortMasterAttenuationControl':addPortMasterAttenuationControl,'addRFPortTable':addRFPortTable,'addRFPortEntry':addRFPortEntry,_H:addRFPortIndex,'addRFPortControlType':addRFPortControlType,'addRFPortControlLevel':addRFPortControlLevel,'addRFPortOutputRFLevel':addRFPortOutputRFLevel,'addRFPortName':addRFPortName,'addRFPortReverseAttenuationControl':addRFPortReverseAttenuationControl,'addRFPortPowerFeedStatus':addRFPortPowerFeedStatus,'addRFPortInputRFLevel':addRFPortInputRFLevel,'addRFPortattenuation1':addRFPortattenuation1,'addRFPortattenuation2':addRFPortattenuation2,'addRFPorteq':addRFPorteq,'addLinePowerVoltage1':addLinePowerVoltage1,'addLinePowerVoltage2':addLinePowerVoltage2,'addLinePowerCurrent':addLinePowerCurrent,'addNumberDCPowerSupply':addNumberDCPowerSupply,'addDCPowerSupplyMode':addDCPowerSupplyMode,'addDCPowerTable':addDCPowerTable,'addDCPowerEntry':addDCPowerEntry,_I:addDCPowerIndex,'addDCPowerVoltage':addDCPowerVoltage,'addDCPowerCurrent':addDCPowerCurrent,'addDCPowerName':addDCPowerName,'addChannelNumber':addChannelNumber,'addFanControl':addFanControl})