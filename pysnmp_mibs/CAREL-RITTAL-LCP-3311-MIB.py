_H='off'
_G='read-write'
_F='C'
_E='alarm'
_D='ok'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
carel=ModuleIdentity((1,3,6,1,4,1,9839))
if mibBuilder.loadTexts:carel.setRevisions(('2021-06-29 00:00',))
class DivBy10(TextualConvention,Integer32):status=_A;displayHint='d-1'
_Rittal_ObjectIdentity=ObjectIdentity
rittal=_Rittal_ObjectIdentity((1,3,6,1,4,1,9839,2606))
_RittalLCP3311_ObjectIdentity=ObjectIdentity
rittalLCP3311=_RittalLCP3311_ObjectIdentity((1,3,6,1,4,1,9839,2606,2))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,9839,2606,2,1))
_Digital_ObjectIdentity=ObjectIdentity
digital=_Digital_ObjectIdentity((1,3,6,1,4,1,9839,2606,2,1,1))
class _CompressorOverloadAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorOverloadAlarm_Type.__name__=_C
_CompressorOverloadAlarm_Object=MibScalar
compressorOverloadAlarm=_CompressorOverloadAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,2),_CompressorOverloadAlarm_Type())
compressorOverloadAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorOverloadAlarm.setStatus(_A)
class _HighPressureAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HighPressureAlarm_Type.__name__=_C
_HighPressureAlarm_Object=MibScalar
highPressureAlarm=_HighPressureAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,3),_HighPressureAlarm_Type())
highPressureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:highPressureAlarm.setStatus(_A)
class _RemoteOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('on',1)))
_RemoteOnOff_Type.__name__=_C
_RemoteOnOff_Object=MibScalar
remoteOnOff=_RemoteOnOff_Object((1,3,6,1,4,1,9839,2606,2,1,1,8),_RemoteOnOff_Type())
remoteOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteOnOff.setStatus(_A)
class _InverterAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_InverterAlarm_Type.__name__=_C
_InverterAlarm_Object=MibScalar
inverterAlarm=_InverterAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,11),_InverterAlarm_Type())
inverterAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:inverterAlarm.setStatus(_A)
class _DriveAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DriveAlarm_Type.__name__=_C
_DriveAlarm_Object=MibScalar
driveAlarm=_DriveAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,12),_DriveAlarm_Type())
driveAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:driveAlarm.setStatus(_A)
class _InverterOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('on',1)))
_InverterOnOff_Type.__name__=_C
_InverterOnOff_Object=MibScalar
inverterOnOff=_InverterOnOff_Object((1,3,6,1,4,1,9839,2606,2,1,1,17),_InverterOnOff_Type())
inverterOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:inverterOnOff.setStatus(_A)
class _GeneralAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GeneralAlarm_Type.__name__=_C
_GeneralAlarm_Object=MibScalar
generalAlarm=_GeneralAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,23),_GeneralAlarm_Type())
generalAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:generalAlarm.setStatus(_A)
class _ResetAllAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_ResetAllAlarms_Type.__name__=_C
_ResetAllAlarms_Object=MibScalar
resetAllAlarms=_ResetAllAlarms_Object((1,3,6,1,4,1,9839,2606,2,1,1,29),_ResetAllAlarms_Type())
resetAllAlarms.setMaxAccess(_G)
if mibBuilder.loadTexts:resetAllAlarms.setStatus(_A)
class _CompressorEnvelopeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorEnvelopeAlarm_Type.__name__=_C
_CompressorEnvelopeAlarm_Object=MibScalar
compressorEnvelopeAlarm=_CompressorEnvelopeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,30),_CompressorEnvelopeAlarm_Type())
compressorEnvelopeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorEnvelopeAlarm.setStatus(_A)
class _CompressorStartupFailureAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorStartupFailureAlarm_Type.__name__=_C
_CompressorStartupFailureAlarm_Object=MibScalar
compressorStartupFailureAlarm=_CompressorStartupFailureAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,31),_CompressorStartupFailureAlarm_Type())
compressorStartupFailureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorStartupFailureAlarm.setStatus(_A)
class _MaxDischargeTemperatureAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MaxDischargeTemperatureAlarm_Type.__name__=_C
_MaxDischargeTemperatureAlarm_Object=MibScalar
maxDischargeTemperatureAlarm=_MaxDischargeTemperatureAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,33),_MaxDischargeTemperatureAlarm_Type())
maxDischargeTemperatureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:maxDischargeTemperatureAlarm.setStatus(_A)
class _CompressorDeltaPressureAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorDeltaPressureAlarm_Type.__name__=_C
_CompressorDeltaPressureAlarm_Object=MibScalar
compressorDeltaPressureAlarm=_CompressorDeltaPressureAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,35),_CompressorDeltaPressureAlarm_Type())
compressorDeltaPressureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorDeltaPressureAlarm.setStatus(_A)
class _OilReturnAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_OilReturnAlarm_Type.__name__=_C
_OilReturnAlarm_Object=MibScalar
oilReturnAlarm=_OilReturnAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,36),_OilReturnAlarm_Type())
oilReturnAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:oilReturnAlarm.setStatus(_A)
class _OutputTemperatureTopProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_OutputTemperatureTopProbeAlarm_Type.__name__=_C
_OutputTemperatureTopProbeAlarm_Object=MibScalar
outputTemperatureTopProbeAlarm=_OutputTemperatureTopProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,38),_OutputTemperatureTopProbeAlarm_Type())
outputTemperatureTopProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureTopProbeAlarm.setStatus(_A)
class _OutputTemperatureMidProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_OutputTemperatureMidProbeAlarm_Type.__name__=_C
_OutputTemperatureMidProbeAlarm_Object=MibScalar
outputTemperatureMidProbeAlarm=_OutputTemperatureMidProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,39),_OutputTemperatureMidProbeAlarm_Type())
outputTemperatureMidProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureMidProbeAlarm.setStatus(_A)
class _OutputTemperatureBottomProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_OutputTemperatureBottomProbeAlarm_Type.__name__=_C
_OutputTemperatureBottomProbeAlarm_Object=MibScalar
outputTemperatureBottomProbeAlarm=_OutputTemperatureBottomProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,40),_OutputTemperatureBottomProbeAlarm_Type())
outputTemperatureBottomProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureBottomProbeAlarm.setStatus(_A)
class _InputTemperatureTopProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_InputTemperatureTopProbeAlarm_Type.__name__=_C
_InputTemperatureTopProbeAlarm_Object=MibScalar
inputTemperatureTopProbeAlarm=_InputTemperatureTopProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,42),_InputTemperatureTopProbeAlarm_Type())
inputTemperatureTopProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureTopProbeAlarm.setStatus(_A)
class _InputTemperatureMidProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_InputTemperatureMidProbeAlarm_Type.__name__=_C
_InputTemperatureMidProbeAlarm_Object=MibScalar
inputTemperatureMidProbeAlarm=_InputTemperatureMidProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,43),_InputTemperatureMidProbeAlarm_Type())
inputTemperatureMidProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureMidProbeAlarm.setStatus(_A)
class _InputTemperatureBottomProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_InputTemperatureBottomProbeAlarm_Type.__name__=_C
_InputTemperatureBottomProbeAlarm_Object=MibScalar
inputTemperatureBottomProbeAlarm=_InputTemperatureBottomProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,44),_InputTemperatureBottomProbeAlarm_Type())
inputTemperatureBottomProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureBottomProbeAlarm.setStatus(_A)
class _CompressorDischargeTemperatureProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorDischargeTemperatureProbeAlarm_Type.__name__=_C
_CompressorDischargeTemperatureProbeAlarm_Object=MibScalar
compressorDischargeTemperatureProbeAlarm=_CompressorDischargeTemperatureProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,45),_CompressorDischargeTemperatureProbeAlarm_Type())
compressorDischargeTemperatureProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorDischargeTemperatureProbeAlarm.setStatus(_A)
class _CompressorSuctionTemperatureProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorSuctionTemperatureProbeAlarm_Type.__name__=_C
_CompressorSuctionTemperatureProbeAlarm_Object=MibScalar
compressorSuctionTemperatureProbeAlarm=_CompressorSuctionTemperatureProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,46),_CompressorSuctionTemperatureProbeAlarm_Type())
compressorSuctionTemperatureProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorSuctionTemperatureProbeAlarm.setStatus(_A)
class _CompressorDischargePressureProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorDischargePressureProbeAlarm_Type.__name__=_C
_CompressorDischargePressureProbeAlarm_Object=MibScalar
compressorDischargePressureProbeAlarm=_CompressorDischargePressureProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,47),_CompressorDischargePressureProbeAlarm_Type())
compressorDischargePressureProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorDischargePressureProbeAlarm.setStatus(_A)
class _CompressorSuctionPressureProbeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CompressorSuctionPressureProbeAlarm_Type.__name__=_C
_CompressorSuctionPressureProbeAlarm_Object=MibScalar
compressorSuctionPressureProbeAlarm=_CompressorSuctionPressureProbeAlarm_Object((1,3,6,1,4,1,9839,2606,2,1,1,48),_CompressorSuctionPressureProbeAlarm_Type())
compressorSuctionPressureProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorSuctionPressureProbeAlarm.setStatus(_A)
class _Reboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_Reboot_Type.__name__=_C
_Reboot_Object=MibScalar
reboot=_Reboot_Object((1,3,6,1,4,1,9839,2606,2,1,1,100),_Reboot_Type())
reboot.setMaxAccess(_G)
if mibBuilder.loadTexts:reboot.setStatus(_A)
_Analog_ObjectIdentity=ObjectIdentity
analog=_Analog_ObjectIdentity((1,3,6,1,4,1,9839,2606,2,1,2))
_OutputTemperatureTopSensor_Type=DivBy10
_OutputTemperatureTopSensor_Object=MibScalar
outputTemperatureTopSensor=_OutputTemperatureTopSensor_Object((1,3,6,1,4,1,9839,2606,2,1,2,2),_OutputTemperatureTopSensor_Type())
outputTemperatureTopSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureTopSensor.setStatus(_A)
if mibBuilder.loadTexts:outputTemperatureTopSensor.setUnits(_F)
_OutputTemperatureMidSensor_Type=DivBy10
_OutputTemperatureMidSensor_Object=MibScalar
outputTemperatureMidSensor=_OutputTemperatureMidSensor_Object((1,3,6,1,4,1,9839,2606,2,1,2,3),_OutputTemperatureMidSensor_Type())
outputTemperatureMidSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureMidSensor.setStatus(_A)
if mibBuilder.loadTexts:outputTemperatureMidSensor.setUnits(_F)
_OutputTemperatureBottomSensor_Type=DivBy10
_OutputTemperatureBottomSensor_Object=MibScalar
outputTemperatureBottomSensor=_OutputTemperatureBottomSensor_Object((1,3,6,1,4,1,9839,2606,2,1,2,4),_OutputTemperatureBottomSensor_Type())
outputTemperatureBottomSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureBottomSensor.setStatus(_A)
if mibBuilder.loadTexts:outputTemperatureBottomSensor.setUnits(_F)
_InputTemperatureTopSensor_Type=DivBy10
_InputTemperatureTopSensor_Object=MibScalar
inputTemperatureTopSensor=_InputTemperatureTopSensor_Object((1,3,6,1,4,1,9839,2606,2,1,2,6),_InputTemperatureTopSensor_Type())
inputTemperatureTopSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureTopSensor.setStatus(_A)
if mibBuilder.loadTexts:inputTemperatureTopSensor.setUnits(_F)
_InputTemperatureMidSensor_Type=DivBy10
_InputTemperatureMidSensor_Object=MibScalar
inputTemperatureMidSensor=_InputTemperatureMidSensor_Object((1,3,6,1,4,1,9839,2606,2,1,2,7),_InputTemperatureMidSensor_Type())
inputTemperatureMidSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureMidSensor.setStatus(_A)
if mibBuilder.loadTexts:inputTemperatureMidSensor.setUnits(_F)
_InputTemperatureBottomSensor_Type=DivBy10
_InputTemperatureBottomSensor_Object=MibScalar
inputTemperatureBottomSensor=_InputTemperatureBottomSensor_Object((1,3,6,1,4,1,9839,2606,2,1,2,8),_InputTemperatureBottomSensor_Type())
inputTemperatureBottomSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureBottomSensor.setStatus(_A)
if mibBuilder.loadTexts:inputTemperatureBottomSensor.setUnits(_F)
_CompressorDischargeTemperature_Type=DivBy10
_CompressorDischargeTemperature_Object=MibScalar
compressorDischargeTemperature=_CompressorDischargeTemperature_Object((1,3,6,1,4,1,9839,2606,2,1,2,9),_CompressorDischargeTemperature_Type())
compressorDischargeTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorDischargeTemperature.setStatus(_A)
if mibBuilder.loadTexts:compressorDischargeTemperature.setUnits(_F)
_CompressorSuctionTemperature_Type=DivBy10
_CompressorSuctionTemperature_Object=MibScalar
compressorSuctionTemperature=_CompressorSuctionTemperature_Object((1,3,6,1,4,1,9839,2606,2,1,2,10),_CompressorSuctionTemperature_Type())
compressorSuctionTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorSuctionTemperature.setStatus(_A)
if mibBuilder.loadTexts:compressorSuctionTemperature.setUnits(_F)
_CompressorDischargePressure_Type=DivBy10
_CompressorDischargePressure_Object=MibScalar
compressorDischargePressure=_CompressorDischargePressure_Object((1,3,6,1,4,1,9839,2606,2,1,2,11),_CompressorDischargePressure_Type())
compressorDischargePressure.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorDischargePressure.setStatus(_A)
if mibBuilder.loadTexts:compressorDischargePressure.setUnits('bar')
_CompressorSuctionPressure_Type=DivBy10
_CompressorSuctionPressure_Object=MibScalar
compressorSuctionPressure=_CompressorSuctionPressure_Object((1,3,6,1,4,1,9839,2606,2,1,2,12),_CompressorSuctionPressure_Type())
compressorSuctionPressure.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorSuctionPressure.setStatus(_A)
if mibBuilder.loadTexts:compressorSuctionPressure.setUnits('bar')
_EvaporatorTemperature_Type=DivBy10
_EvaporatorTemperature_Object=MibScalar
evaporatorTemperature=_EvaporatorTemperature_Object((1,3,6,1,4,1,9839,2606,2,1,2,13),_EvaporatorTemperature_Type())
evaporatorTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:evaporatorTemperature.setStatus(_A)
if mibBuilder.loadTexts:evaporatorTemperature.setUnits(_F)
_CondensingTemperature_Type=DivBy10
_CondensingTemperature_Object=MibScalar
condensingTemperature=_CondensingTemperature_Object((1,3,6,1,4,1,9839,2606,2,1,2,14),_CondensingTemperature_Type())
condensingTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:condensingTemperature.setStatus(_A)
if mibBuilder.loadTexts:condensingTemperature.setUnits(_F)
_InputTemperatureAverage_Type=DivBy10
_InputTemperatureAverage_Object=MibScalar
inputTemperatureAverage=_InputTemperatureAverage_Object((1,3,6,1,4,1,9839,2606,2,1,2,21),_InputTemperatureAverage_Type())
inputTemperatureAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:inputTemperatureAverage.setStatus(_A)
if mibBuilder.loadTexts:inputTemperatureAverage.setUnits(_F)
_OutputTemperatureAverage_Type=DivBy10
_OutputTemperatureAverage_Object=MibScalar
outputTemperatureAverage=_OutputTemperatureAverage_Object((1,3,6,1,4,1,9839,2606,2,1,2,22),_OutputTemperatureAverage_Type())
outputTemperatureAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:outputTemperatureAverage.setStatus(_A)
if mibBuilder.loadTexts:outputTemperatureAverage.setUnits(_F)
_CompressorRotorSpeed_Type=DivBy10
_CompressorRotorSpeed_Object=MibScalar
compressorRotorSpeed=_CompressorRotorSpeed_Object((1,3,6,1,4,1,9839,2606,2,1,2,45),_CompressorRotorSpeed_Type())
compressorRotorSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorRotorSpeed.setStatus(_A)
if mibBuilder.loadTexts:compressorRotorSpeed.setUnits('rps')
_CompressorMotorCurrent_Type=DivBy10
_CompressorMotorCurrent_Object=MibScalar
compressorMotorCurrent=_CompressorMotorCurrent_Object((1,3,6,1,4,1,9839,2606,2,1,2,46),_CompressorMotorCurrent_Type())
compressorMotorCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorMotorCurrent.setStatus(_A)
if mibBuilder.loadTexts:compressorMotorCurrent.setUnits('A')
_LcpSetpoint_Type=DivBy10
_LcpSetpoint_Object=MibScalar
lcpSetpoint=_LcpSetpoint_Object((1,3,6,1,4,1,9839,2606,2,1,2,48),_LcpSetpoint_Type())
lcpSetpoint.setMaxAccess(_G)
if mibBuilder.loadTexts:lcpSetpoint.setStatus(_A)
if mibBuilder.loadTexts:lcpSetpoint.setUnits(_F)
_Integer_ObjectIdentity=ObjectIdentity
integer=_Integer_ObjectIdentity((1,3,6,1,4,1,9839,2606,2,1,3))
class _CompressorRotorSpeedHz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CompressorRotorSpeedHz_Type.__name__=_C
_CompressorRotorSpeedHz_Object=MibScalar
compressorRotorSpeedHz=_CompressorRotorSpeedHz_Object((1,3,6,1,4,1,9839,2606,2,1,3,1),_CompressorRotorSpeedHz_Type())
compressorRotorSpeedHz.setMaxAccess(_B)
if mibBuilder.loadTexts:compressorRotorSpeedHz.setStatus(_A)
if mibBuilder.loadTexts:compressorRotorSpeedHz.setUnits('Hz')
class _DriverPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stop',1),('run',2),(_E,3)))
_DriverPowerStatus_Type.__name__=_C
_DriverPowerStatus_Object=MibScalar
driverPowerStatus=_DriverPowerStatus_Object((1,3,6,1,4,1,9839,2606,2,1,3,2),_DriverPowerStatus_Type())
driverPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:driverPowerStatus.setStatus(_A)
class _CurrentErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('OK',0),('ALA02',2),('ALA03',3),('ALA04',4),('ALA05',5),('ALA06',6),('ALA07',7),('ALA08',8),('ALA09',9),('ALA10',10),('ALA11',11),('ALA12',12),('ALB01',13),('ALB02',14),('ALB03',15),('ALC01',16),('ALC03',17),('ALC04',18),('ALC05',19),('ALC06',20),('ALF01',21),('ALD02',22),('ALD03',23),('ALD04',24),('ALD05',25),('ALD06',26),('ALD07',27),('ALD08',28),('ALD09',29),('ALL01',30),('ALL02',31),('ALL99',32),('ALW04',33)))
_CurrentErrorCode_Type.__name__=_C
_CurrentErrorCode_Object=MibScalar
currentErrorCode=_CurrentErrorCode_Object((1,3,6,1,4,1,9839,2606,2,1,3,3),_CurrentErrorCode_Type())
currentErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:currentErrorCode.setStatus(_A)
_DriverTemperature_Type=DivBy10
_DriverTemperature_Object=MibScalar
driverTemperature=_DriverTemperature_Object((1,3,6,1,4,1,9839,2606,2,1,3,4),_DriverTemperature_Type())
driverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:driverTemperature.setStatus(_A)
if mibBuilder.loadTexts:driverTemperature.setUnits(_F)
_DcBusVoltage_Type=DivBy10
_DcBusVoltage_Object=MibScalar
dcBusVoltage=_DcBusVoltage_Object((1,3,6,1,4,1,9839,2606,2,1,3,5),_DcBusVoltage_Type())
dcBusVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dcBusVoltage.setStatus(_A)
if mibBuilder.loadTexts:dcBusVoltage.setUnits('V')
_MotorVoltage_Type=DivBy10
_MotorVoltage_Object=MibScalar
motorVoltage=_MotorVoltage_Object((1,3,6,1,4,1,9839,2606,2,1,3,6),_MotorVoltage_Type())
motorVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:motorVoltage.setStatus(_A)
if mibBuilder.loadTexts:motorVoltage.setUnits('V')
_PowerRequest_Type=DivBy10
_PowerRequest_Object=MibScalar
powerRequest=_PowerRequest_Object((1,3,6,1,4,1,9839,2606,2,1,3,7),_PowerRequest_Type())
powerRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:powerRequest.setStatus(_A)
if mibBuilder.loadTexts:powerRequest.setUnits('%')
class _UnitOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('on',1),('energy-save',2),('auto',3)))
_UnitOnOff_Type.__name__=_C
_UnitOnOff_Object=MibScalar
unitOnOff=_UnitOnOff_Object((1,3,6,1,4,1,9839,2606,2,1,3,13),_UnitOnOff_Type())
unitOnOff.setMaxAccess(_G)
if mibBuilder.loadTexts:unitOnOff.setStatus(_A)
class _EnvelopeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,0),('maximum-compression-ratio',1),('maximum-discharge-power',2),('current-limit',3),('maximum-suction-power',4),('minimum-compression-ratio',5),('minimum-delta-power',6),('minimum-discharge-power',7),('minimum-suction-power',8)))
_EnvelopeZone_Type.__name__=_C
_EnvelopeZone_Object=MibScalar
envelopeZone=_EnvelopeZone_Object((1,3,6,1,4,1,9839,2606,2,1,3,14),_EnvelopeZone_Type())
envelopeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeZone.setStatus(_A)
class _CoolingCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CoolingCapacity_Type.__name__=_C
_CoolingCapacity_Object=MibScalar
coolingCapacity=_CoolingCapacity_Object((1,3,6,1,4,1,9839,2606,2,1,3,16),_CoolingCapacity_Type())
coolingCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:coolingCapacity.setStatus(_A)
if mibBuilder.loadTexts:coolingCapacity.setUnits('%')
class _EvdValveSteps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,540))
_EvdValveSteps_Type.__name__=_C
_EvdValveSteps_Object=MibScalar
evdValveSteps=_EvdValveSteps_Object((1,3,6,1,4,1,9839,2606,2,1,3,17),_EvdValveSteps_Type())
evdValveSteps.setMaxAccess(_B)
if mibBuilder.loadTexts:evdValveSteps.setStatus(_A)
if mibBuilder.loadTexts:evdValveSteps.setUnits('steps')
class _FanSpeedPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FanSpeedPercent_Type.__name__=_C
_FanSpeedPercent_Object=MibScalar
fanSpeedPercent=_FanSpeedPercent_Object((1,3,6,1,4,1,9839,2606,2,1,3,28),_FanSpeedPercent_Type())
fanSpeedPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeedPercent.setStatus(_A)
if mibBuilder.loadTexts:fanSpeedPercent.setUnits('%')
class _FanSpeedRpm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3700))
_FanSpeedRpm_Type.__name__=_C
_FanSpeedRpm_Object=MibScalar
fanSpeedRpm=_FanSpeedRpm_Object((1,3,6,1,4,1,9839,2606,2,1,3,29),_FanSpeedRpm_Type())
fanSpeedRpm.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeedRpm.setStatus(_A)
if mibBuilder.loadTexts:fanSpeedRpm.setUnits('rpm')
class _EvdValveOpening_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EvdValveOpening_Type.__name__=_C
_EvdValveOpening_Object=MibScalar
evdValveOpening=_EvdValveOpening_Object((1,3,6,1,4,1,9839,2606,2,1,3,30),_EvdValveOpening_Type())
evdValveOpening.setMaxAccess(_B)
if mibBuilder.loadTexts:evdValveOpening.setStatus(_A)
if mibBuilder.loadTexts:evdValveOpening.setUnits('%')
mibBuilder.exportSymbols('CAREL-RITTAL-LCP-3311-MIB',**{'DivBy10':DivBy10,'carel':carel,'rittal':rittal,'rittalLCP3311':rittalLCP3311,'sensors':sensors,'digital':digital,'compressorOverloadAlarm':compressorOverloadAlarm,'highPressureAlarm':highPressureAlarm,'remoteOnOff':remoteOnOff,'inverterAlarm':inverterAlarm,'driveAlarm':driveAlarm,'inverterOnOff':inverterOnOff,'generalAlarm':generalAlarm,'resetAllAlarms':resetAllAlarms,'compressorEnvelopeAlarm':compressorEnvelopeAlarm,'compressorStartupFailureAlarm':compressorStartupFailureAlarm,'maxDischargeTemperatureAlarm':maxDischargeTemperatureAlarm,'compressorDeltaPressureAlarm':compressorDeltaPressureAlarm,'oilReturnAlarm':oilReturnAlarm,'outputTemperatureTopProbeAlarm':outputTemperatureTopProbeAlarm,'outputTemperatureMidProbeAlarm':outputTemperatureMidProbeAlarm,'outputTemperatureBottomProbeAlarm':outputTemperatureBottomProbeAlarm,'inputTemperatureTopProbeAlarm':inputTemperatureTopProbeAlarm,'inputTemperatureMidProbeAlarm':inputTemperatureMidProbeAlarm,'inputTemperatureBottomProbeAlarm':inputTemperatureBottomProbeAlarm,'compressorDischargeTemperatureProbeAlarm':compressorDischargeTemperatureProbeAlarm,'compressorSuctionTemperatureProbeAlarm':compressorSuctionTemperatureProbeAlarm,'compressorDischargePressureProbeAlarm':compressorDischargePressureProbeAlarm,'compressorSuctionPressureProbeAlarm':compressorSuctionPressureProbeAlarm,'reboot':reboot,'analog':analog,'outputTemperatureTopSensor':outputTemperatureTopSensor,'outputTemperatureMidSensor':outputTemperatureMidSensor,'outputTemperatureBottomSensor':outputTemperatureBottomSensor,'inputTemperatureTopSensor':inputTemperatureTopSensor,'inputTemperatureMidSensor':inputTemperatureMidSensor,'inputTemperatureBottomSensor':inputTemperatureBottomSensor,'compressorDischargeTemperature':compressorDischargeTemperature,'compressorSuctionTemperature':compressorSuctionTemperature,'compressorDischargePressure':compressorDischargePressure,'compressorSuctionPressure':compressorSuctionPressure,'evaporatorTemperature':evaporatorTemperature,'condensingTemperature':condensingTemperature,'inputTemperatureAverage':inputTemperatureAverage,'outputTemperatureAverage':outputTemperatureAverage,'compressorRotorSpeed':compressorRotorSpeed,'compressorMotorCurrent':compressorMotorCurrent,'lcpSetpoint':lcpSetpoint,'integer':integer,'compressorRotorSpeedHz':compressorRotorSpeedHz,'driverPowerStatus':driverPowerStatus,'currentErrorCode':currentErrorCode,'driverTemperature':driverTemperature,'dcBusVoltage':dcBusVoltage,'motorVoltage':motorVoltage,'powerRequest':powerRequest,'unitOnOff':unitOnOff,'envelopeZone':envelopeZone,'coolingCapacity':coolingCapacity,'evdValveSteps':evdValveSteps,'fanSpeedPercent':fanSpeedPercent,'fanSpeedRpm':fanSpeedRpm,'evdValveOpening':evdValveOpening})