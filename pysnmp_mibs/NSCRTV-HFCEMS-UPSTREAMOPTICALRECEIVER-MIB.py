_H='uporDCPowerIndex'
_G='uporIndex'
_F='NSCRTV-HFCEMS-UPSTREAMOPTICALRECEIVER-MIB'
_E='read-write'
_D='optional'
_C='read-only'
_B='mandatory'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
uporIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','uporIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_UporVendorOID_Type=ObjectIdentifier
_UporVendorOID_Object=MibScalar
uporVendorOID=_UporVendorOID_Object((1,3,6,1,4,1,17409,1,8,1),_UporVendorOID_Type())
uporVendorOID.setMaxAccess(_C)
if mibBuilder.loadTexts:uporVendorOID.setStatus(_D)
class _UporSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_UporSlotNumber_Type.__name__=_A
_UporSlotNumber_Object=MibScalar
uporSlotNumber=_UporSlotNumber_Object((1,3,6,1,4,1,17409,1,8,2),_UporSlotNumber_Type())
uporSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:uporSlotNumber.setStatus(_B)
_UporDeviceTable_Object=MibTable
uporDeviceTable=_UporDeviceTable_Object((1,3,6,1,4,1,17409,1,8,3))
if mibBuilder.loadTexts:uporDeviceTable.setStatus(_B)
_UporDeviceEntry_Object=MibTableRow
uporDeviceEntry=_UporDeviceEntry_Object((1,3,6,1,4,1,17409,1,8,3,1))
uporDeviceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:uporDeviceEntry.setStatus(_B)
class _UporIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_UporIndex_Type.__name__=_A
_UporIndex_Object=MibTableColumn
uporIndex=_UporIndex_Object((1,3,6,1,4,1,17409,1,8,3,1,1),_UporIndex_Type())
uporIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:uporIndex.setStatus(_B)
class _UporOpicalInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_UporOpicalInputPower_Type.__name__=_A
_UporOpicalInputPower_Object=MibTableColumn
uporOpicalInputPower=_UporOpicalInputPower_Object((1,3,6,1,4,1,17409,1,8,3,1,2),_UporOpicalInputPower_Type())
uporOpicalInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:uporOpicalInputPower.setStatus(_B)
class _UporOutputRFAttenuationRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_UporOutputRFAttenuationRange_Type.__name__=_A
_UporOutputRFAttenuationRange_Object=MibTableColumn
uporOutputRFAttenuationRange=_UporOutputRFAttenuationRange_Object((1,3,6,1,4,1,17409,1,8,3,1,3),_UporOutputRFAttenuationRange_Type())
uporOutputRFAttenuationRange.setMaxAccess(_C)
if mibBuilder.loadTexts:uporOutputRFAttenuationRange.setStatus(_D)
class _UporOutputRFAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_UporOutputRFAttenuation_Type.__name__=_A
_UporOutputRFAttenuation_Object=MibTableColumn
uporOutputRFAttenuation=_UporOutputRFAttenuation_Object((1,3,6,1,4,1,17409,1,8,3,1,4),_UporOutputRFAttenuation_Type())
uporOutputRFAttenuation.setMaxAccess(_E)
if mibBuilder.loadTexts:uporOutputRFAttenuation.setStatus(_D)
class _UporAGCControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_UporAGCControl_Type.__name__=_A
_UporAGCControl_Object=MibTableColumn
uporAGCControl=_UporAGCControl_Object((1,3,6,1,4,1,17409,1,8,3,1,5),_UporAGCControl_Type())
uporAGCControl.setMaxAccess(_E)
if mibBuilder.loadTexts:uporAGCControl.setStatus(_D)
class _UporNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_UporNumberDCPowerSupply_Type.__name__=_A
_UporNumberDCPowerSupply_Object=MibScalar
uporNumberDCPowerSupply=_UporNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,8,4),_UporNumberDCPowerSupply_Type())
uporNumberDCPowerSupply.setMaxAccess(_C)
if mibBuilder.loadTexts:uporNumberDCPowerSupply.setStatus(_B)
class _UporDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2),('aloneSupply',3)))
_UporDCPowerSupplyMode_Type.__name__=_A
_UporDCPowerSupplyMode_Object=MibScalar
uporDCPowerSupplyMode=_UporDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,8,5),_UporDCPowerSupplyMode_Type())
uporDCPowerSupplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:uporDCPowerSupplyMode.setStatus(_D)
_UporDCPowerTable_Object=MibTable
uporDCPowerTable=_UporDCPowerTable_Object((1,3,6,1,4,1,17409,1,8,6))
if mibBuilder.loadTexts:uporDCPowerTable.setStatus(_B)
_UporDCPowerEntry_Object=MibTableRow
uporDCPowerEntry=_UporDCPowerEntry_Object((1,3,6,1,4,1,17409,1,8,6,1))
uporDCPowerEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:uporDCPowerEntry.setStatus(_B)
_UporDCPowerIndex_Type=Integer32
_UporDCPowerIndex_Object=MibTableColumn
uporDCPowerIndex=_UporDCPowerIndex_Object((1,3,6,1,4,1,17409,1,8,6,1,1),_UporDCPowerIndex_Type())
uporDCPowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:uporDCPowerIndex.setStatus(_B)
class _UporDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_UporDCPowerVoltage_Type.__name__=_A
_UporDCPowerVoltage_Object=MibTableColumn
uporDCPowerVoltage=_UporDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,8,6,1,2),_UporDCPowerVoltage_Type())
uporDCPowerVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:uporDCPowerVoltage.setStatus(_B)
class _UporDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UporDCPowerCurrent_Type.__name__=_A
_UporDCPowerCurrent_Object=MibTableColumn
uporDCPowerCurrent=_UporDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,8,6,1,3),_UporDCPowerCurrent_Type())
uporDCPowerCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:uporDCPowerCurrent.setStatus(_D)
_UporDCPowerName_Type=DisplayString
_UporDCPowerName_Object=MibTableColumn
uporDCPowerName=_UporDCPowerName_Object((1,3,6,1,4,1,17409,1,8,6,1,4),_UporDCPowerName_Type())
uporDCPowerName.setMaxAccess(_C)
if mibBuilder.loadTexts:uporDCPowerName.setStatus(_B)
mibBuilder.exportSymbols(_F,**{'uporVendorOID':uporVendorOID,'uporSlotNumber':uporSlotNumber,'uporDeviceTable':uporDeviceTable,'uporDeviceEntry':uporDeviceEntry,_G:uporIndex,'uporOpicalInputPower':uporOpicalInputPower,'uporOutputRFAttenuationRange':uporOutputRFAttenuationRange,'uporOutputRFAttenuation':uporOutputRFAttenuation,'uporAGCControl':uporAGCControl,'uporNumberDCPowerSupply':uporNumberDCPowerSupply,'uporDCPowerSupplyMode':uporDCPowerSupplyMode,'uporDCPowerTable':uporDCPowerTable,'uporDCPowerEntry':uporDCPowerEntry,_H:uporDCPowerIndex,'uporDCPowerVoltage':uporDCPowerVoltage,'uporDCPowerCurrent':uporDCPowerCurrent,'uporDCPowerName':uporDCPowerName})