_N='Degrees Centigrade'
_M='NotificationType'
_L='percentage'
_K='0.1 A'
_J='0.1 V'
_I='normalClose'
_H='normalOpen'
_G='DisplayString'
_F='read-write'
_E='on'
_D='off'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_M,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_M,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Socomec_ObjectIdentity=ObjectIdentity
socomec=_Socomec_ObjectIdentity((1,3,6,1,4,1,4555))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,4555,2))
_Pdu_ObjectIdentity=ObjectIdentity
pdu=_Pdu_ObjectIdentity((1,3,6,1,4,1,4555,2,30))
_DpduIdent_ObjectIdentity=ObjectIdentity
dpduIdent=_DpduIdent_ObjectIdentity((1,3,6,1,4,1,4555,2,30,1))
class _DpduIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpduIdentManufacturer_Type.__name__=_G
_DpduIdentManufacturer_Object=MibScalar
dpduIdentManufacturer=_DpduIdentManufacturer_Object((1,3,6,1,4,1,4555,2,30,1,1),_DpduIdentManufacturer_Type())
dpduIdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduIdentManufacturer.setStatus(_A)
class _DpduIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpduIdentModel_Type.__name__=_G
_DpduIdentModel_Object=MibScalar
dpduIdentModel=_DpduIdentModel_Object((1,3,6,1,4,1,4555,2,30,1,2),_DpduIdentModel_Type())
dpduIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduIdentModel.setStatus(_A)
class _DpduIdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DpduIdentSerialNumber_Type.__name__=_G
_DpduIdentSerialNumber_Object=MibScalar
dpduIdentSerialNumber=_DpduIdentSerialNumber_Object((1,3,6,1,4,1,4555,2,30,1,3),_DpduIdentSerialNumber_Type())
dpduIdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduIdentSerialNumber.setStatus(_A)
class _DpduIdentPDUFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DpduIdentPDUFirmwareVersion_Type.__name__=_G
_DpduIdentPDUFirmwareVersion_Object=MibScalar
dpduIdentPDUFirmwareVersion=_DpduIdentPDUFirmwareVersion_Object((1,3,6,1,4,1,4555,2,30,1,4),_DpduIdentPDUFirmwareVersion_Type())
dpduIdentPDUFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduIdentPDUFirmwareVersion.setStatus(_A)
class _DpduIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DpduIdentAgentSoftwareVersion_Type.__name__=_G
_DpduIdentAgentSoftwareVersion_Object=MibScalar
dpduIdentAgentSoftwareVersion=_DpduIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,4555,2,30,1,5),_DpduIdentAgentSoftwareVersion_Type())
dpduIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduIdentAgentSoftwareVersion.setStatus(_A)
class _DpduIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpduIdentName_Type.__name__=_G
_DpduIdentName_Object=MibScalar
dpduIdentName=_DpduIdentName_Object((1,3,6,1,4,1,4555,2,30,1,6),_DpduIdentName_Type())
dpduIdentName.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduIdentName.setStatus(_A)
class _DpduAttachedDevices_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_DpduAttachedDevices_Type.__name__=_G
_DpduAttachedDevices_Object=MibScalar
dpduAttachedDevices=_DpduAttachedDevices_Object((1,3,6,1,4,1,4555,2,30,1,7),_DpduAttachedDevices_Type())
dpduAttachedDevices.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduAttachedDevices.setStatus(_A)
_DpduOutput_ObjectIdentity=ObjectIdentity
dpduOutput=_DpduOutput_ObjectIdentity((1,3,6,1,4,1,4555,2,30,2))
_DpduOutputFrequency_Type=Integer32
_DpduOutputFrequency_Object=MibScalar
dpduOutputFrequency=_DpduOutputFrequency_Object((1,3,6,1,4,1,4555,2,30,2,1),_DpduOutputFrequency_Type())
dpduOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputFrequency.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputFrequency.setUnits('0.1 Hertz')
_DpduOutputVoltage1_Type=Integer32
_DpduOutputVoltage1_Object=MibScalar
dpduOutputVoltage1=_DpduOutputVoltage1_Object((1,3,6,1,4,1,4555,2,30,2,2),_DpduOutputVoltage1_Type())
dpduOutputVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputVoltage1.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputVoltage1.setUnits(_J)
_DpduOutputCurrent1_Type=Integer32
_DpduOutputCurrent1_Object=MibScalar
dpduOutputCurrent1=_DpduOutputCurrent1_Object((1,3,6,1,4,1,4555,2,30,2,3),_DpduOutputCurrent1_Type())
dpduOutputCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputCurrent1.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputCurrent1.setUnits(_K)
_DpduOutputVoltage2_Type=Integer32
_DpduOutputVoltage2_Object=MibScalar
dpduOutputVoltage2=_DpduOutputVoltage2_Object((1,3,6,1,4,1,4555,2,30,2,4),_DpduOutputVoltage2_Type())
dpduOutputVoltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputVoltage2.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputVoltage2.setUnits(_J)
_DpduOutputCurrent2_Type=Integer32
_DpduOutputCurrent2_Object=MibScalar
dpduOutputCurrent2=_DpduOutputCurrent2_Object((1,3,6,1,4,1,4555,2,30,2,5),_DpduOutputCurrent2_Type())
dpduOutputCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputCurrent2.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputCurrent2.setUnits(_K)
_DpduOutputVoltage3_Type=Integer32
_DpduOutputVoltage3_Object=MibScalar
dpduOutputVoltage3=_DpduOutputVoltage3_Object((1,3,6,1,4,1,4555,2,30,2,6),_DpduOutputVoltage3_Type())
dpduOutputVoltage3.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputVoltage3.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputVoltage3.setUnits(_J)
_DpduOutputCurrent3_Type=Integer32
_DpduOutputCurrent3_Object=MibScalar
dpduOutputCurrent3=_DpduOutputCurrent3_Object((1,3,6,1,4,1,4555,2,30,2,7),_DpduOutputCurrent3_Type())
dpduOutputCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduOutputCurrent3.setStatus(_A)
if mibBuilder.loadTexts:dpduOutputCurrent3.setUnits(_K)
_DpduAlarm_ObjectIdentity=ObjectIdentity
dpduAlarm=_DpduAlarm_ObjectIdentity((1,3,6,1,4,1,4555,2,30,3))
class _DpduAlarmDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmDisconnect_Type.__name__=_C
_DpduAlarmDisconnect_Object=MibScalar
dpduAlarmDisconnect=_DpduAlarmDisconnect_Object((1,3,6,1,4,1,4555,2,30,3,1),_DpduAlarmDisconnect_Type())
dpduAlarmDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmDisconnect.setStatus(_A)
class _DpduAlarmL1LoadMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL1LoadMajor_Type.__name__=_C
_DpduAlarmL1LoadMajor_Object=MibScalar
dpduAlarmL1LoadMajor=_DpduAlarmL1LoadMajor_Object((1,3,6,1,4,1,4555,2,30,3,2),_DpduAlarmL1LoadMajor_Type())
dpduAlarmL1LoadMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL1LoadMajor.setStatus(_A)
class _DpduAlarmL1LoadMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL1LoadMinor_Type.__name__=_C
_DpduAlarmL1LoadMinor_Object=MibScalar
dpduAlarmL1LoadMinor=_DpduAlarmL1LoadMinor_Object((1,3,6,1,4,1,4555,2,30,3,3),_DpduAlarmL1LoadMinor_Type())
dpduAlarmL1LoadMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL1LoadMinor.setStatus(_A)
class _DpduAlarmL1OutVoltMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL1OutVoltMajor_Type.__name__=_C
_DpduAlarmL1OutVoltMajor_Object=MibScalar
dpduAlarmL1OutVoltMajor=_DpduAlarmL1OutVoltMajor_Object((1,3,6,1,4,1,4555,2,30,3,4),_DpduAlarmL1OutVoltMajor_Type())
dpduAlarmL1OutVoltMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL1OutVoltMajor.setStatus(_A)
class _DpduAlarmL1OutVoltMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL1OutVoltMinor_Type.__name__=_C
_DpduAlarmL1OutVoltMinor_Object=MibScalar
dpduAlarmL1OutVoltMinor=_DpduAlarmL1OutVoltMinor_Object((1,3,6,1,4,1,4555,2,30,3,5),_DpduAlarmL1OutVoltMinor_Type())
dpduAlarmL1OutVoltMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL1OutVoltMinor.setStatus(_A)
class _DpduAlarmL2LoadMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL2LoadMajor_Type.__name__=_C
_DpduAlarmL2LoadMajor_Object=MibScalar
dpduAlarmL2LoadMajor=_DpduAlarmL2LoadMajor_Object((1,3,6,1,4,1,4555,2,30,3,6),_DpduAlarmL2LoadMajor_Type())
dpduAlarmL2LoadMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL2LoadMajor.setStatus(_A)
class _DpduAlarmL2LoadMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL2LoadMinor_Type.__name__=_C
_DpduAlarmL2LoadMinor_Object=MibScalar
dpduAlarmL2LoadMinor=_DpduAlarmL2LoadMinor_Object((1,3,6,1,4,1,4555,2,30,3,7),_DpduAlarmL2LoadMinor_Type())
dpduAlarmL2LoadMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL2LoadMinor.setStatus(_A)
class _DpduAlarmL2OutVoltMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL2OutVoltMajor_Type.__name__=_C
_DpduAlarmL2OutVoltMajor_Object=MibScalar
dpduAlarmL2OutVoltMajor=_DpduAlarmL2OutVoltMajor_Object((1,3,6,1,4,1,4555,2,30,3,8),_DpduAlarmL2OutVoltMajor_Type())
dpduAlarmL2OutVoltMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL2OutVoltMajor.setStatus(_A)
class _DpduAlarmL2OutVoltMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL2OutVoltMinor_Type.__name__=_C
_DpduAlarmL2OutVoltMinor_Object=MibScalar
dpduAlarmL2OutVoltMinor=_DpduAlarmL2OutVoltMinor_Object((1,3,6,1,4,1,4555,2,30,3,9),_DpduAlarmL2OutVoltMinor_Type())
dpduAlarmL2OutVoltMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL2OutVoltMinor.setStatus(_A)
class _DpduAlarmL3LoadMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL3LoadMajor_Type.__name__=_C
_DpduAlarmL3LoadMajor_Object=MibScalar
dpduAlarmL3LoadMajor=_DpduAlarmL3LoadMajor_Object((1,3,6,1,4,1,4555,2,30,3,10),_DpduAlarmL3LoadMajor_Type())
dpduAlarmL3LoadMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL3LoadMajor.setStatus(_A)
class _DpduAlarmL3LoadMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL3LoadMinor_Type.__name__=_C
_DpduAlarmL3LoadMinor_Object=MibScalar
dpduAlarmL3LoadMinor=_DpduAlarmL3LoadMinor_Object((1,3,6,1,4,1,4555,2,30,3,11),_DpduAlarmL3LoadMinor_Type())
dpduAlarmL3LoadMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL3LoadMinor.setStatus(_A)
class _DpduAlarmL3OutVoltMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL3OutVoltMajor_Type.__name__=_C
_DpduAlarmL3OutVoltMajor_Object=MibScalar
dpduAlarmL3OutVoltMajor=_DpduAlarmL3OutVoltMajor_Object((1,3,6,1,4,1,4555,2,30,3,12),_DpduAlarmL3OutVoltMajor_Type())
dpduAlarmL3OutVoltMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL3OutVoltMajor.setStatus(_A)
class _DpduAlarmL3OutVoltMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL3OutVoltMinor_Type.__name__=_C
_DpduAlarmL3OutVoltMinor_Object=MibScalar
dpduAlarmL3OutVoltMinor=_DpduAlarmL3OutVoltMinor_Object((1,3,6,1,4,1,4555,2,30,3,13),_DpduAlarmL3OutVoltMinor_Type())
dpduAlarmL3OutVoltMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL3OutVoltMinor.setStatus(_A)
class _DpduAlarmL12LoadMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL12LoadMajor_Type.__name__=_C
_DpduAlarmL12LoadMajor_Object=MibScalar
dpduAlarmL12LoadMajor=_DpduAlarmL12LoadMajor_Object((1,3,6,1,4,1,4555,2,30,3,14),_DpduAlarmL12LoadMajor_Type())
dpduAlarmL12LoadMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL12LoadMajor.setStatus(_A)
class _DpduAlarmL12LoadMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmL12LoadMinor_Type.__name__=_C
_DpduAlarmL12LoadMinor_Object=MibScalar
dpduAlarmL12LoadMinor=_DpduAlarmL12LoadMinor_Object((1,3,6,1,4,1,4555,2,30,3,15),_DpduAlarmL12LoadMinor_Type())
dpduAlarmL12LoadMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmL12LoadMinor.setStatus(_A)
_DpduEnvironment_ObjectIdentity=ObjectIdentity
dpduEnvironment=_DpduEnvironment_ObjectIdentity((1,3,6,1,4,1,4555,2,30,4))
_DpduEnvTemperature_Type=Integer32
_DpduEnvTemperature_Object=MibScalar
dpduEnvTemperature=_DpduEnvTemperature_Object((1,3,6,1,4,1,4555,2,30,4,1),_DpduEnvTemperature_Type())
dpduEnvTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduEnvTemperature.setStatus(_A)
if mibBuilder.loadTexts:dpduEnvTemperature.setUnits('0.1 Degrees Centigrade')
_DpduEnvHumidity_Type=Integer32
_DpduEnvHumidity_Object=MibScalar
dpduEnvHumidity=_DpduEnvHumidity_Object((1,3,6,1,4,1,4555,2,30,4,2),_DpduEnvHumidity_Type())
dpduEnvHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduEnvHumidity.setStatus(_A)
if mibBuilder.loadTexts:dpduEnvHumidity.setUnits(_L)
_DpduEnvSetTemperatureWarnLimit_Type=Integer32
_DpduEnvSetTemperatureWarnLimit_Object=MibScalar
dpduEnvSetTemperatureWarnLimit=_DpduEnvSetTemperatureWarnLimit_Object((1,3,6,1,4,1,4555,2,30,4,3),_DpduEnvSetTemperatureWarnLimit_Type())
dpduEnvSetTemperatureWarnLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetTemperatureWarnLimit.setStatus(_A)
if mibBuilder.loadTexts:dpduEnvSetTemperatureWarnLimit.setUnits(_N)
_DpduEnvSetTemperatureAlarmLimit_Type=Integer32
_DpduEnvSetTemperatureAlarmLimit_Object=MibScalar
dpduEnvSetTemperatureAlarmLimit=_DpduEnvSetTemperatureAlarmLimit_Object((1,3,6,1,4,1,4555,2,30,4,4),_DpduEnvSetTemperatureAlarmLimit_Type())
dpduEnvSetTemperatureAlarmLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetTemperatureAlarmLimit.setStatus(_A)
if mibBuilder.loadTexts:dpduEnvSetTemperatureAlarmLimit.setUnits(_N)
_DpduEnvSetHumidityWarnLimit_Type=Integer32
_DpduEnvSetHumidityWarnLimit_Object=MibScalar
dpduEnvSetHumidityWarnLimit=_DpduEnvSetHumidityWarnLimit_Object((1,3,6,1,4,1,4555,2,30,4,5),_DpduEnvSetHumidityWarnLimit_Type())
dpduEnvSetHumidityWarnLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetHumidityWarnLimit.setStatus(_A)
if mibBuilder.loadTexts:dpduEnvSetHumidityWarnLimit.setUnits(_L)
_DpduEnvSetHumidityAlarmLimit_Type=Integer32
_DpduEnvSetHumidityAlarmLimit_Object=MibScalar
dpduEnvSetHumidityAlarmLimit=_DpduEnvSetHumidityAlarmLimit_Object((1,3,6,1,4,1,4555,2,30,4,6),_DpduEnvSetHumidityAlarmLimit_Type())
dpduEnvSetHumidityAlarmLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetHumidityAlarmLimit.setStatus(_A)
if mibBuilder.loadTexts:dpduEnvSetHumidityAlarmLimit.setUnits(_L)
class _DpduEnvSetEnvRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DpduEnvSetEnvRelay1_Type.__name__=_C
_DpduEnvSetEnvRelay1_Object=MibScalar
dpduEnvSetEnvRelay1=_DpduEnvSetEnvRelay1_Object((1,3,6,1,4,1,4555,2,30,4,7),_DpduEnvSetEnvRelay1_Type())
dpduEnvSetEnvRelay1.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetEnvRelay1.setStatus(_A)
class _DpduEnvSetEnvRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DpduEnvSetEnvRelay2_Type.__name__=_C
_DpduEnvSetEnvRelay2_Object=MibScalar
dpduEnvSetEnvRelay2=_DpduEnvSetEnvRelay2_Object((1,3,6,1,4,1,4555,2,30,4,8),_DpduEnvSetEnvRelay2_Type())
dpduEnvSetEnvRelay2.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetEnvRelay2.setStatus(_A)
class _DpduEnvSetEnvRelay3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DpduEnvSetEnvRelay3_Type.__name__=_C
_DpduEnvSetEnvRelay3_Object=MibScalar
dpduEnvSetEnvRelay3=_DpduEnvSetEnvRelay3_Object((1,3,6,1,4,1,4555,2,30,4,9),_DpduEnvSetEnvRelay3_Type())
dpduEnvSetEnvRelay3.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetEnvRelay3.setStatus(_A)
class _DpduEnvSetEnvRelay4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DpduEnvSetEnvRelay4_Type.__name__=_C
_DpduEnvSetEnvRelay4_Object=MibScalar
dpduEnvSetEnvRelay4=_DpduEnvSetEnvRelay4_Object((1,3,6,1,4,1,4555,2,30,4,10),_DpduEnvSetEnvRelay4_Type())
dpduEnvSetEnvRelay4.setMaxAccess(_F)
if mibBuilder.loadTexts:dpduEnvSetEnvRelay4.setStatus(_A)
class _DpduWarnOverEnvTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduWarnOverEnvTemperature_Type.__name__=_C
_DpduWarnOverEnvTemperature_Object=MibScalar
dpduWarnOverEnvTemperature=_DpduWarnOverEnvTemperature_Object((1,3,6,1,4,1,4555,2,30,4,11),_DpduWarnOverEnvTemperature_Type())
dpduWarnOverEnvTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduWarnOverEnvTemperature.setStatus(_A)
class _DpduAlarmOverEnvTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmOverEnvTemperature_Type.__name__=_C
_DpduAlarmOverEnvTemperature_Object=MibScalar
dpduAlarmOverEnvTemperature=_DpduAlarmOverEnvTemperature_Object((1,3,6,1,4,1,4555,2,30,4,12),_DpduAlarmOverEnvTemperature_Type())
dpduAlarmOverEnvTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmOverEnvTemperature.setStatus(_A)
class _DpduWarnmOverEnvHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduWarnmOverEnvHumidity_Type.__name__=_C
_DpduWarnmOverEnvHumidity_Object=MibScalar
dpduWarnmOverEnvHumidity=_DpduWarnmOverEnvHumidity_Object((1,3,6,1,4,1,4555,2,30,4,13),_DpduWarnmOverEnvHumidity_Type())
dpduWarnmOverEnvHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduWarnmOverEnvHumidity.setStatus(_A)
class _DpduAlarmOverEnvHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmOverEnvHumidity_Type.__name__=_C
_DpduAlarmOverEnvHumidity_Object=MibScalar
dpduAlarmOverEnvHumidity=_DpduAlarmOverEnvHumidity_Object((1,3,6,1,4,1,4555,2,30,4,14),_DpduAlarmOverEnvHumidity_Type())
dpduAlarmOverEnvHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmOverEnvHumidity.setStatus(_A)
class _DpduAlarmEnvRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmEnvRelay1_Type.__name__=_C
_DpduAlarmEnvRelay1_Object=MibScalar
dpduAlarmEnvRelay1=_DpduAlarmEnvRelay1_Object((1,3,6,1,4,1,4555,2,30,4,15),_DpduAlarmEnvRelay1_Type())
dpduAlarmEnvRelay1.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmEnvRelay1.setStatus(_A)
class _DpduAlarmEnvRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmEnvRelay2_Type.__name__=_C
_DpduAlarmEnvRelay2_Object=MibScalar
dpduAlarmEnvRelay2=_DpduAlarmEnvRelay2_Object((1,3,6,1,4,1,4555,2,30,4,16),_DpduAlarmEnvRelay2_Type())
dpduAlarmEnvRelay2.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmEnvRelay2.setStatus(_A)
class _DpduAlarmEnvRelay3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmEnvRelay3_Type.__name__=_C
_DpduAlarmEnvRelay3_Object=MibScalar
dpduAlarmEnvRelay3=_DpduAlarmEnvRelay3_Object((1,3,6,1,4,1,4555,2,30,4,17),_DpduAlarmEnvRelay3_Type())
dpduAlarmEnvRelay3.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmEnvRelay3.setStatus(_A)
class _DpduAlarmEnvRelay4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DpduAlarmEnvRelay4_Type.__name__=_C
_DpduAlarmEnvRelay4_Object=MibScalar
dpduAlarmEnvRelay4=_DpduAlarmEnvRelay4_Object((1,3,6,1,4,1,4555,2,30,4,18),_DpduAlarmEnvRelay4_Type())
dpduAlarmEnvRelay4.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmEnvRelay4.setStatus(_A)
class _DpduAlarmEnvDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_DpduAlarmEnvDisconnect_Type.__name__=_C
_DpduAlarmEnvDisconnect_Object=MibScalar
dpduAlarmEnvDisconnect=_DpduAlarmEnvDisconnect_Object((1,3,6,1,4,1,4555,2,30,4,19),_DpduAlarmEnvDisconnect_Type())
dpduAlarmEnvDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:dpduAlarmEnvDisconnect.setStatus(_A)
_DpduTraps_ObjectIdentity=ObjectIdentity
dpduTraps=_DpduTraps_ObjectIdentity((1,3,6,1,4,1,4555,2,30,20))
dpduCommunicationLost=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,1))
if mibBuilder.loadTexts:dpduCommunicationLost.setStatus('')
dpduCommunicationEstablished=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,2))
if mibBuilder.loadTexts:dpduCommunicationEstablished.setStatus('')
dpduL1LoadMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,3))
if mibBuilder.loadTexts:dpduL1LoadMajorAlarm.setStatus('')
dpduL1LoadMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,4))
if mibBuilder.loadTexts:dpduL1LoadMajorAlarmRecover.setStatus('')
dpduL1LoadMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,5))
if mibBuilder.loadTexts:dpduL1LoadMinorAlarm.setStatus('')
dpduL1LoadMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,6))
if mibBuilder.loadTexts:dpduL1LoadMinorAlarmRecover.setStatus('')
dpduL1OutVoltMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,7))
if mibBuilder.loadTexts:dpduL1OutVoltMajorAlarm.setStatus('')
dpduL1OutVoltMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,8))
if mibBuilder.loadTexts:dpduL1OutVoltMajorAlarmRecover.setStatus('')
dpduL1OutVoltMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,9))
if mibBuilder.loadTexts:dpduL1OutVoltMinorAlarm.setStatus('')
dpduL1OutVoltMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,10))
if mibBuilder.loadTexts:dpduL1OutVoltMinorAlarmRecover.setStatus('')
dpduL2LoadMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,11))
if mibBuilder.loadTexts:dpduL2LoadMajorAlarm.setStatus('')
dpduL2LoadMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,12))
if mibBuilder.loadTexts:dpduL2LoadMajorAlarmRecover.setStatus('')
dpduL2LoadMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,13))
if mibBuilder.loadTexts:dpduL2LoadMinorAlarm.setStatus('')
dpduL2LoadMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,14))
if mibBuilder.loadTexts:dpduL2LoadMinorAlarmRecover.setStatus('')
dpduL2OutVoltMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,15))
if mibBuilder.loadTexts:dpduL2OutVoltMajorAlarm.setStatus('')
dpduL2OutVoltMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,16))
if mibBuilder.loadTexts:dpduL2OutVoltMajorAlarmRecover.setStatus('')
dpduL2OutVoltMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,17))
if mibBuilder.loadTexts:dpduL2OutVoltMinorAlarm.setStatus('')
dpduL2OutVoltMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,18))
if mibBuilder.loadTexts:dpduL2OutVoltMinorAlarmRecover.setStatus('')
dpduL3LoadMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,19))
if mibBuilder.loadTexts:dpduL3LoadMajorAlarm.setStatus('')
dpduL3LoadMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,20))
if mibBuilder.loadTexts:dpduL3LoadMajorAlarmRecover.setStatus('')
dpduL3LoadMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,21))
if mibBuilder.loadTexts:dpduL3LoadMinorAlarm.setStatus('')
dpduL3LoadMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,22))
if mibBuilder.loadTexts:dpduL3LoadMinorAlarmRecover.setStatus('')
dpduL3OutVoltMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,23))
if mibBuilder.loadTexts:dpduL3OutVoltMajorAlarm.setStatus('')
dpduL3OutVoltMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,24))
if mibBuilder.loadTexts:dpduL3OutVoltMajorAlarmRecover.setStatus('')
dpduL3OutVoltMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,25))
if mibBuilder.loadTexts:dpduL3OutVoltMinorAlarm.setStatus('')
dpduL3OutVoltMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,26))
if mibBuilder.loadTexts:dpduL3OutVoltMinorAlarmRecover.setStatus('')
dpduL12LoadMajorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,27))
if mibBuilder.loadTexts:dpduL12LoadMajorAlarm.setStatus('')
dpduL12LoadMajorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,28))
if mibBuilder.loadTexts:dpduL12LoadMajorAlarmRecover.setStatus('')
dpduL12LoadMinorAlarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,29))
if mibBuilder.loadTexts:dpduL12LoadMinorAlarm.setStatus('')
dpduL12LoadMinorAlarmRecover=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,30))
if mibBuilder.loadTexts:dpduL12LoadMinorAlarmRecover.setStatus('')
dpduEnvCommunicationLost=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,31))
if mibBuilder.loadTexts:dpduEnvCommunicationLost.setStatus('')
dpduEnvCommunicationEstablished=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,32))
if mibBuilder.loadTexts:dpduEnvCommunicationEstablished.setStatus('')
dpduEnvOverWarnTemperature=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,33))
if mibBuilder.loadTexts:dpduEnvOverWarnTemperature.setStatus('')
dpduNoLongerEnvOverWarnTemperature=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,34))
if mibBuilder.loadTexts:dpduNoLongerEnvOverWarnTemperature.setStatus('')
dpduEnvOverWarnHumidity=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,35))
if mibBuilder.loadTexts:dpduEnvOverWarnHumidity.setStatus('')
dpduNoLongerEnvOverWarnHumidity=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,36))
if mibBuilder.loadTexts:dpduNoLongerEnvOverWarnHumidity.setStatus('')
dpduEnvOverAlarmTemperature=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,37))
if mibBuilder.loadTexts:dpduEnvOverAlarmTemperature.setStatus('')
dpduNoLongerEnvOverAlarmTemperature=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,38))
if mibBuilder.loadTexts:dpduNoLongerEnvOverAlarmTemperature.setStatus('')
dpduEnvOverAlarmHumidity=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,39))
if mibBuilder.loadTexts:dpduEnvOverAlarmHumidity.setStatus('')
dpduNoLongerEnvOverAlarmHumidity=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,40))
if mibBuilder.loadTexts:dpduNoLongerEnvOverAlarmHumidity.setStatus('')
dpduEnvRelay1Alarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,41))
if mibBuilder.loadTexts:dpduEnvRelay1Alarm.setStatus('')
dpduEnvRelay1Normal=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,42))
if mibBuilder.loadTexts:dpduEnvRelay1Normal.setStatus('')
dpduEnvRelay2Alarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,43))
if mibBuilder.loadTexts:dpduEnvRelay2Alarm.setStatus('')
dpduEnvRelay2Normal=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,44))
if mibBuilder.loadTexts:dpduEnvRelay2Normal.setStatus('')
dpduEnvRelay3Alarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,45))
if mibBuilder.loadTexts:dpduEnvRelay3Alarm.setStatus('')
dpduEnvRelay3Normal=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,46))
if mibBuilder.loadTexts:dpduEnvRelay3Normal.setStatus('')
dpduEnvRelay4Alarm=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,47))
if mibBuilder.loadTexts:dpduEnvRelay4Alarm.setStatus('')
dpduEnvRelay4Normal=NotificationType((1,3,6,1,4,1,4555,2,30,20,0,48))
if mibBuilder.loadTexts:dpduEnvRelay4Normal.setStatus('')
mibBuilder.exportSymbols('SOCOMECPDU-MIB',**{'socomec':socomec,'ups':ups,'pdu':pdu,'dpduIdent':dpduIdent,'dpduIdentManufacturer':dpduIdentManufacturer,'dpduIdentModel':dpduIdentModel,'dpduIdentSerialNumber':dpduIdentSerialNumber,'dpduIdentPDUFirmwareVersion':dpduIdentPDUFirmwareVersion,'dpduIdentAgentSoftwareVersion':dpduIdentAgentSoftwareVersion,'dpduIdentName':dpduIdentName,'dpduAttachedDevices':dpduAttachedDevices,'dpduOutput':dpduOutput,'dpduOutputFrequency':dpduOutputFrequency,'dpduOutputVoltage1':dpduOutputVoltage1,'dpduOutputCurrent1':dpduOutputCurrent1,'dpduOutputVoltage2':dpduOutputVoltage2,'dpduOutputCurrent2':dpduOutputCurrent2,'dpduOutputVoltage3':dpduOutputVoltage3,'dpduOutputCurrent3':dpduOutputCurrent3,'dpduAlarm':dpduAlarm,'dpduAlarmDisconnect':dpduAlarmDisconnect,'dpduAlarmL1LoadMajor':dpduAlarmL1LoadMajor,'dpduAlarmL1LoadMinor':dpduAlarmL1LoadMinor,'dpduAlarmL1OutVoltMajor':dpduAlarmL1OutVoltMajor,'dpduAlarmL1OutVoltMinor':dpduAlarmL1OutVoltMinor,'dpduAlarmL2LoadMajor':dpduAlarmL2LoadMajor,'dpduAlarmL2LoadMinor':dpduAlarmL2LoadMinor,'dpduAlarmL2OutVoltMajor':dpduAlarmL2OutVoltMajor,'dpduAlarmL2OutVoltMinor':dpduAlarmL2OutVoltMinor,'dpduAlarmL3LoadMajor':dpduAlarmL3LoadMajor,'dpduAlarmL3LoadMinor':dpduAlarmL3LoadMinor,'dpduAlarmL3OutVoltMajor':dpduAlarmL3OutVoltMajor,'dpduAlarmL3OutVoltMinor':dpduAlarmL3OutVoltMinor,'dpduAlarmL12LoadMajor':dpduAlarmL12LoadMajor,'dpduAlarmL12LoadMinor':dpduAlarmL12LoadMinor,'dpduEnvironment':dpduEnvironment,'dpduEnvTemperature':dpduEnvTemperature,'dpduEnvHumidity':dpduEnvHumidity,'dpduEnvSetTemperatureWarnLimit':dpduEnvSetTemperatureWarnLimit,'dpduEnvSetTemperatureAlarmLimit':dpduEnvSetTemperatureAlarmLimit,'dpduEnvSetHumidityWarnLimit':dpduEnvSetHumidityWarnLimit,'dpduEnvSetHumidityAlarmLimit':dpduEnvSetHumidityAlarmLimit,'dpduEnvSetEnvRelay1':dpduEnvSetEnvRelay1,'dpduEnvSetEnvRelay2':dpduEnvSetEnvRelay2,'dpduEnvSetEnvRelay3':dpduEnvSetEnvRelay3,'dpduEnvSetEnvRelay4':dpduEnvSetEnvRelay4,'dpduWarnOverEnvTemperature':dpduWarnOverEnvTemperature,'dpduAlarmOverEnvTemperature':dpduAlarmOverEnvTemperature,'dpduWarnmOverEnvHumidity':dpduWarnmOverEnvHumidity,'dpduAlarmOverEnvHumidity':dpduAlarmOverEnvHumidity,'dpduAlarmEnvRelay1':dpduAlarmEnvRelay1,'dpduAlarmEnvRelay2':dpduAlarmEnvRelay2,'dpduAlarmEnvRelay3':dpduAlarmEnvRelay3,'dpduAlarmEnvRelay4':dpduAlarmEnvRelay4,'dpduAlarmEnvDisconnect':dpduAlarmEnvDisconnect,'dpduTraps':dpduTraps,'dpduCommunicationLost':dpduCommunicationLost,'dpduCommunicationEstablished':dpduCommunicationEstablished,'dpduL1LoadMajorAlarm':dpduL1LoadMajorAlarm,'dpduL1LoadMajorAlarmRecover':dpduL1LoadMajorAlarmRecover,'dpduL1LoadMinorAlarm':dpduL1LoadMinorAlarm,'dpduL1LoadMinorAlarmRecover':dpduL1LoadMinorAlarmRecover,'dpduL1OutVoltMajorAlarm':dpduL1OutVoltMajorAlarm,'dpduL1OutVoltMajorAlarmRecover':dpduL1OutVoltMajorAlarmRecover,'dpduL1OutVoltMinorAlarm':dpduL1OutVoltMinorAlarm,'dpduL1OutVoltMinorAlarmRecover':dpduL1OutVoltMinorAlarmRecover,'dpduL2LoadMajorAlarm':dpduL2LoadMajorAlarm,'dpduL2LoadMajorAlarmRecover':dpduL2LoadMajorAlarmRecover,'dpduL2LoadMinorAlarm':dpduL2LoadMinorAlarm,'dpduL2LoadMinorAlarmRecover':dpduL2LoadMinorAlarmRecover,'dpduL2OutVoltMajorAlarm':dpduL2OutVoltMajorAlarm,'dpduL2OutVoltMajorAlarmRecover':dpduL2OutVoltMajorAlarmRecover,'dpduL2OutVoltMinorAlarm':dpduL2OutVoltMinorAlarm,'dpduL2OutVoltMinorAlarmRecover':dpduL2OutVoltMinorAlarmRecover,'dpduL3LoadMajorAlarm':dpduL3LoadMajorAlarm,'dpduL3LoadMajorAlarmRecover':dpduL3LoadMajorAlarmRecover,'dpduL3LoadMinorAlarm':dpduL3LoadMinorAlarm,'dpduL3LoadMinorAlarmRecover':dpduL3LoadMinorAlarmRecover,'dpduL3OutVoltMajorAlarm':dpduL3OutVoltMajorAlarm,'dpduL3OutVoltMajorAlarmRecover':dpduL3OutVoltMajorAlarmRecover,'dpduL3OutVoltMinorAlarm':dpduL3OutVoltMinorAlarm,'dpduL3OutVoltMinorAlarmRecover':dpduL3OutVoltMinorAlarmRecover,'dpduL12LoadMajorAlarm':dpduL12LoadMajorAlarm,'dpduL12LoadMajorAlarmRecover':dpduL12LoadMajorAlarmRecover,'dpduL12LoadMinorAlarm':dpduL12LoadMinorAlarm,'dpduL12LoadMinorAlarmRecover':dpduL12LoadMinorAlarmRecover,'dpduEnvCommunicationLost':dpduEnvCommunicationLost,'dpduEnvCommunicationEstablished':dpduEnvCommunicationEstablished,'dpduEnvOverWarnTemperature':dpduEnvOverWarnTemperature,'dpduNoLongerEnvOverWarnTemperature':dpduNoLongerEnvOverWarnTemperature,'dpduEnvOverWarnHumidity':dpduEnvOverWarnHumidity,'dpduNoLongerEnvOverWarnHumidity':dpduNoLongerEnvOverWarnHumidity,'dpduEnvOverAlarmTemperature':dpduEnvOverAlarmTemperature,'dpduNoLongerEnvOverAlarmTemperature':dpduNoLongerEnvOverAlarmTemperature,'dpduEnvOverAlarmHumidity':dpduEnvOverAlarmHumidity,'dpduNoLongerEnvOverAlarmHumidity':dpduNoLongerEnvOverAlarmHumidity,'dpduEnvRelay1Alarm':dpduEnvRelay1Alarm,'dpduEnvRelay1Normal':dpduEnvRelay1Normal,'dpduEnvRelay2Alarm':dpduEnvRelay2Alarm,'dpduEnvRelay2Normal':dpduEnvRelay2Normal,'dpduEnvRelay3Alarm':dpduEnvRelay3Alarm,'dpduEnvRelay3Normal':dpduEnvRelay3Normal,'dpduEnvRelay4Alarm':dpduEnvRelay4Alarm,'dpduEnvRelay4Normal':dpduEnvRelay4Normal})