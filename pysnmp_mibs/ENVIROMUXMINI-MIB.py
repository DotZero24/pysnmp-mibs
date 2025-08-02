_AD='overflowTrap'
_AC='waterSensor1Trap'
_AB='dryContactSensor4Trap'
_AA='dryContactSensor3Trap'
_A9='dryContactSensor2Trap'
_A8='dryContactSensor1Trap'
_A7='humiditySensor2Trap'
_A6='humiditySensor1Trap'
_A5='temperatureSensor2Trap'
_A4='temperatureSensor1Trap'
_A3='sysGateway'
_A2='sysLocation'
_A1='waterAlertStatus'
_A0='waterName'
_z='waterAlert'
_y='waterStatus'
_x='dryContact4AlertStatus'
_w='dryContact4Name'
_v='dryContact4Alert'
_u='dryContact4Status'
_t='dryContact3AlertStatus'
_s='dryContact3Name'
_r='dryContact3Alert'
_q='dryContact3Status'
_p='dryContact2AlertStatus'
_o='dryContact2Name'
_n='dryContact2Alert'
_m='dryContact2Status'
_l='dryContact1AlertStatus'
_k='dryContact1Name'
_j='dryContact1Alert'
_i='dryContact1Status'
_h='humiditySensor2HighThreshold'
_g='humiditySensor2LowThreshold'
_f='humiditySensor2Name'
_e='humiditySensor2Alert'
_d='humiditySensor2CurrentValue'
_c='humiditySensor1HighThreshold'
_b='humiditySensor1LowThreshold'
_a='humiditySensor1Name'
_Z='humiditySensor1Alert'
_Y='humiditySensor1CurrentValue'
_X='temperatureSensor2HighThreshold'
_W='temperatureSensor2LowThreshold'
_V='temperatureSensor2Unit'
_U='temperatureSensor2Name'
_T='temperatureSensor2Alert'
_S='temperatureSensor2CurrentValue'
_R='temperatureSensor1HighThreshold'
_Q='temperatureSensor1LowThreshold'
_P='temperatureSensor1Unit'
_O='temperatureSensor1Name'
_N='temperatureSensor1Alert'
_M='temperatureSensor1CurrentValue'
_L='version'
_K='alertWhenClosed'
_J='alertWhenOpen'
_I='closed'
_H='open'
_G='on'
_F='off'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='ENVIROMUXMINI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
enviromuxMini=ModuleIdentity((1,3,6,1,4,1,3699,1,1,3))
if mibBuilder.loadTexts:enviromuxMini.setRevisions(('2009-09-24 14:00','2007-04-13 14:00','2005-03-30 14:00'))
class DecimalPointValue(TextualConvention,Integer32):status=_A;displayHint='d-1';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,1000))
_Nti_ObjectIdentity=ObjectIdentity
nti=_Nti_ObjectIdentity((1,3,6,1,4,1,3699))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,3699,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,3699,1,1))
_Monitoring_ObjectIdentity=ObjectIdentity
monitoring=_Monitoring_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1))
_TemperatureSensor1_ObjectIdentity=ObjectIdentity
temperatureSensor1=_TemperatureSensor1_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,1))
_TemperatureSensor1CurrentValue_Type=DecimalPointValue
_TemperatureSensor1CurrentValue_Object=MibScalar
temperatureSensor1CurrentValue=_TemperatureSensor1CurrentValue_Object((1,3,6,1,4,1,3699,1,1,3,1,1,1),_TemperatureSensor1CurrentValue_Type())
temperatureSensor1CurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureSensor1CurrentValue.setStatus(_A)
class _TemperatureSensor1Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TemperatureSensor1Alert_Type.__name__=_E
_TemperatureSensor1Alert_Object=MibScalar
temperatureSensor1Alert=_TemperatureSensor1Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,1,2),_TemperatureSensor1Alert_Type())
temperatureSensor1Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureSensor1Alert.setStatus(_A)
_TemperatureSensor2_ObjectIdentity=ObjectIdentity
temperatureSensor2=_TemperatureSensor2_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,2))
_TemperatureSensor2CurrentValue_Type=DecimalPointValue
_TemperatureSensor2CurrentValue_Object=MibScalar
temperatureSensor2CurrentValue=_TemperatureSensor2CurrentValue_Object((1,3,6,1,4,1,3699,1,1,3,1,2,1),_TemperatureSensor2CurrentValue_Type())
temperatureSensor2CurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureSensor2CurrentValue.setStatus(_A)
class _TemperatureSensor2Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TemperatureSensor2Alert_Type.__name__=_E
_TemperatureSensor2Alert_Object=MibScalar
temperatureSensor2Alert=_TemperatureSensor2Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,2,2),_TemperatureSensor2Alert_Type())
temperatureSensor2Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureSensor2Alert.setStatus(_A)
_HumiditySensor1_ObjectIdentity=ObjectIdentity
humiditySensor1=_HumiditySensor1_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,3))
_HumiditySensor1CurrentValue_Type=DecimalPointValue
_HumiditySensor1CurrentValue_Object=MibScalar
humiditySensor1CurrentValue=_HumiditySensor1CurrentValue_Object((1,3,6,1,4,1,3699,1,1,3,1,3,1),_HumiditySensor1CurrentValue_Type())
humiditySensor1CurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:humiditySensor1CurrentValue.setStatus(_A)
class _HumiditySensor1Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_HumiditySensor1Alert_Type.__name__=_E
_HumiditySensor1Alert_Object=MibScalar
humiditySensor1Alert=_HumiditySensor1Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,3,2),_HumiditySensor1Alert_Type())
humiditySensor1Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:humiditySensor1Alert.setStatus(_A)
_HumiditySensor2_ObjectIdentity=ObjectIdentity
humiditySensor2=_HumiditySensor2_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,4))
_HumiditySensor2CurrentValue_Type=DecimalPointValue
_HumiditySensor2CurrentValue_Object=MibScalar
humiditySensor2CurrentValue=_HumiditySensor2CurrentValue_Object((1,3,6,1,4,1,3699,1,1,3,1,4,1),_HumiditySensor2CurrentValue_Type())
humiditySensor2CurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:humiditySensor2CurrentValue.setStatus(_A)
class _HumiditySensor2Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_HumiditySensor2Alert_Type.__name__=_E
_HumiditySensor2Alert_Object=MibScalar
humiditySensor2Alert=_HumiditySensor2Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,4,2),_HumiditySensor2Alert_Type())
humiditySensor2Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:humiditySensor2Alert.setStatus(_A)
_DryContact1_ObjectIdentity=ObjectIdentity
dryContact1=_DryContact1_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,5))
class _DryContact1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DryContact1Status_Type.__name__=_E
_DryContact1Status_Object=MibScalar
dryContact1Status=_DryContact1Status_Object((1,3,6,1,4,1,3699,1,1,3,1,5,1),_DryContact1Status_Type())
dryContact1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact1Status.setStatus(_A)
class _DryContact1Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DryContact1Alert_Type.__name__=_E
_DryContact1Alert_Object=MibScalar
dryContact1Alert=_DryContact1Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,5,2),_DryContact1Alert_Type())
dryContact1Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact1Alert.setStatus(_A)
_DryContact2_ObjectIdentity=ObjectIdentity
dryContact2=_DryContact2_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,6))
class _DryContact2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DryContact2Status_Type.__name__=_E
_DryContact2Status_Object=MibScalar
dryContact2Status=_DryContact2Status_Object((1,3,6,1,4,1,3699,1,1,3,1,6,1),_DryContact2Status_Type())
dryContact2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact2Status.setStatus(_A)
class _DryContact2Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DryContact2Alert_Type.__name__=_E
_DryContact2Alert_Object=MibScalar
dryContact2Alert=_DryContact2Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,6,2),_DryContact2Alert_Type())
dryContact2Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact2Alert.setStatus(_A)
_DryContact3_ObjectIdentity=ObjectIdentity
dryContact3=_DryContact3_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,7))
class _DryContact3Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DryContact3Status_Type.__name__=_E
_DryContact3Status_Object=MibScalar
dryContact3Status=_DryContact3Status_Object((1,3,6,1,4,1,3699,1,1,3,1,7,1),_DryContact3Status_Type())
dryContact3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact3Status.setStatus(_A)
class _DryContact3Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DryContact3Alert_Type.__name__=_E
_DryContact3Alert_Object=MibScalar
dryContact3Alert=_DryContact3Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,7,2),_DryContact3Alert_Type())
dryContact3Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact3Alert.setStatus(_A)
_DryContact4_ObjectIdentity=ObjectIdentity
dryContact4=_DryContact4_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,8))
class _DryContact4Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DryContact4Status_Type.__name__=_E
_DryContact4Status_Object=MibScalar
dryContact4Status=_DryContact4Status_Object((1,3,6,1,4,1,3699,1,1,3,1,8,1),_DryContact4Status_Type())
dryContact4Status.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact4Status.setStatus(_A)
class _DryContact4Alert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DryContact4Alert_Type.__name__=_E
_DryContact4Alert_Object=MibScalar
dryContact4Alert=_DryContact4Alert_Object((1,3,6,1,4,1,3699,1,1,3,1,8,2),_DryContact4Alert_Type())
dryContact4Alert.setMaxAccess(_C)
if mibBuilder.loadTexts:dryContact4Alert.setStatus(_A)
_WaterSensor_ObjectIdentity=ObjectIdentity
waterSensor=_WaterSensor_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,1,9))
class _WaterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_WaterStatus_Type.__name__=_E
_WaterStatus_Object=MibScalar
waterStatus=_WaterStatus_Object((1,3,6,1,4,1,3699,1,1,3,1,9,1),_WaterStatus_Type())
waterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:waterStatus.setStatus(_A)
class _WaterAlert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_WaterAlert_Type.__name__=_E
_WaterAlert_Object=MibScalar
waterAlert=_WaterAlert_Object((1,3,6,1,4,1,3699,1,1,3,1,9,2),_WaterAlert_Type())
waterAlert.setMaxAccess(_C)
if mibBuilder.loadTexts:waterAlert.setStatus(_A)
_Administration_ObjectIdentity=ObjectIdentity
administration=_Administration_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2))
_HostSystem_ObjectIdentity=ObjectIdentity
hostSystem=_HostSystem_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,1))
_SysName_Type=DisplayString
_SysName_Object=MibScalar
sysName=_SysName_Object((1,3,6,1,4,1,3699,1,1,3,2,1,1),_SysName_Type())
sysName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysName.setStatus(_A)
_SysLocation_Type=DisplayString
_SysLocation_Object=MibScalar
sysLocation=_SysLocation_Object((1,3,6,1,4,1,3699,1,1,3,2,1,2),_SysLocation_Type())
sysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLocation.setStatus(_A)
_SysIP_Type=DisplayString
_SysIP_Object=MibScalar
sysIP=_SysIP_Object((1,3,6,1,4,1,3699,1,1,3,2,1,3),_SysIP_Type())
sysIP.setMaxAccess(_C)
if mibBuilder.loadTexts:sysIP.setStatus(_A)
_SysMask_Type=DisplayString
_SysMask_Object=MibScalar
sysMask=_SysMask_Object((1,3,6,1,4,1,3699,1,1,3,2,1,4),_SysMask_Type())
sysMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMask.setStatus(_A)
_SysGateway_Type=DisplayString
_SysGateway_Object=MibScalar
sysGateway=_SysGateway_Object((1,3,6,1,4,1,3699,1,1,3,2,1,5),_SysGateway_Type())
sysGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:sysGateway.setStatus(_A)
_SysDNS_Type=DisplayString
_SysDNS_Object=MibScalar
sysDNS=_SysDNS_Object((1,3,6,1,4,1,3699,1,1,3,2,1,6),_SysDNS_Type())
sysDNS.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDNS.setStatus(_A)
_TemperatureSensor1Adm_ObjectIdentity=ObjectIdentity
temperatureSensor1Adm=_TemperatureSensor1Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,2))
_TemperatureSensor1Name_Type=DisplayString
_TemperatureSensor1Name_Object=MibScalar
temperatureSensor1Name=_TemperatureSensor1Name_Object((1,3,6,1,4,1,3699,1,1,3,2,2,1),_TemperatureSensor1Name_Type())
temperatureSensor1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor1Name.setStatus(_A)
_TemperatureSensor1Unit_Type=DisplayString
_TemperatureSensor1Unit_Object=MibScalar
temperatureSensor1Unit=_TemperatureSensor1Unit_Object((1,3,6,1,4,1,3699,1,1,3,2,2,2),_TemperatureSensor1Unit_Type())
temperatureSensor1Unit.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor1Unit.setStatus(_A)
_TemperatureSensor1LowThreshold_Type=DisplayString
_TemperatureSensor1LowThreshold_Object=MibScalar
temperatureSensor1LowThreshold=_TemperatureSensor1LowThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,2,3),_TemperatureSensor1LowThreshold_Type())
temperatureSensor1LowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor1LowThreshold.setStatus(_A)
_TemperatureSensor1HighThreshold_Type=DisplayString
_TemperatureSensor1HighThreshold_Object=MibScalar
temperatureSensor1HighThreshold=_TemperatureSensor1HighThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,2,4),_TemperatureSensor1HighThreshold_Type())
temperatureSensor1HighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor1HighThreshold.setStatus(_A)
_TemperatureSensor2Adm_ObjectIdentity=ObjectIdentity
temperatureSensor2Adm=_TemperatureSensor2Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,3))
_TemperatureSensor2Name_Type=DisplayString
_TemperatureSensor2Name_Object=MibScalar
temperatureSensor2Name=_TemperatureSensor2Name_Object((1,3,6,1,4,1,3699,1,1,3,2,3,1),_TemperatureSensor2Name_Type())
temperatureSensor2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor2Name.setStatus(_A)
_TemperatureSensor2Unit_Type=DisplayString
_TemperatureSensor2Unit_Object=MibScalar
temperatureSensor2Unit=_TemperatureSensor2Unit_Object((1,3,6,1,4,1,3699,1,1,3,2,3,2),_TemperatureSensor2Unit_Type())
temperatureSensor2Unit.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor2Unit.setStatus(_A)
_TemperatureSensor2LowThreshold_Type=DisplayString
_TemperatureSensor2LowThreshold_Object=MibScalar
temperatureSensor2LowThreshold=_TemperatureSensor2LowThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,3,3),_TemperatureSensor2LowThreshold_Type())
temperatureSensor2LowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor2LowThreshold.setStatus(_A)
_TemperatureSensor2HighThreshold_Type=DisplayString
_TemperatureSensor2HighThreshold_Object=MibScalar
temperatureSensor2HighThreshold=_TemperatureSensor2HighThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,3,4),_TemperatureSensor2HighThreshold_Type())
temperatureSensor2HighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureSensor2HighThreshold.setStatus(_A)
_HumiditySensor1Adm_ObjectIdentity=ObjectIdentity
humiditySensor1Adm=_HumiditySensor1Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,4))
_HumiditySensor1Name_Type=DisplayString
_HumiditySensor1Name_Object=MibScalar
humiditySensor1Name=_HumiditySensor1Name_Object((1,3,6,1,4,1,3699,1,1,3,2,4,1),_HumiditySensor1Name_Type())
humiditySensor1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensor1Name.setStatus(_A)
_HumiditySensor1LowThreshold_Type=DisplayString
_HumiditySensor1LowThreshold_Object=MibScalar
humiditySensor1LowThreshold=_HumiditySensor1LowThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,4,2),_HumiditySensor1LowThreshold_Type())
humiditySensor1LowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensor1LowThreshold.setStatus(_A)
_HumiditySensor1HighThreshold_Type=DisplayString
_HumiditySensor1HighThreshold_Object=MibScalar
humiditySensor1HighThreshold=_HumiditySensor1HighThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,4,3),_HumiditySensor1HighThreshold_Type())
humiditySensor1HighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensor1HighThreshold.setStatus(_A)
_HumiditySensor2Adm_ObjectIdentity=ObjectIdentity
humiditySensor2Adm=_HumiditySensor2Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,5))
_HumiditySensor2Name_Type=DisplayString
_HumiditySensor2Name_Object=MibScalar
humiditySensor2Name=_HumiditySensor2Name_Object((1,3,6,1,4,1,3699,1,1,3,2,5,1),_HumiditySensor2Name_Type())
humiditySensor2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensor2Name.setStatus(_A)
_HumiditySensor2LowThreshold_Type=DisplayString
_HumiditySensor2LowThreshold_Object=MibScalar
humiditySensor2LowThreshold=_HumiditySensor2LowThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,5,2),_HumiditySensor2LowThreshold_Type())
humiditySensor2LowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensor2LowThreshold.setStatus(_A)
_HumiditySensor2HighThreshold_Type=DisplayString
_HumiditySensor2HighThreshold_Object=MibScalar
humiditySensor2HighThreshold=_HumiditySensor2HighThreshold_Object((1,3,6,1,4,1,3699,1,1,3,2,5,3),_HumiditySensor2HighThreshold_Type())
humiditySensor2HighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensor2HighThreshold.setStatus(_A)
_DryContact1Adm_ObjectIdentity=ObjectIdentity
dryContact1Adm=_DryContact1Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,6))
_DryContact1Name_Type=DisplayString
_DryContact1Name_Object=MibScalar
dryContact1Name=_DryContact1Name_Object((1,3,6,1,4,1,3699,1,1,3,2,6,1),_DryContact1Name_Type())
dryContact1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact1Name.setStatus(_A)
class _DryContact1AlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_DryContact1AlertStatus_Type.__name__=_E
_DryContact1AlertStatus_Object=MibScalar
dryContact1AlertStatus=_DryContact1AlertStatus_Object((1,3,6,1,4,1,3699,1,1,3,2,6,2),_DryContact1AlertStatus_Type())
dryContact1AlertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact1AlertStatus.setStatus(_A)
_DryContact2Adm_ObjectIdentity=ObjectIdentity
dryContact2Adm=_DryContact2Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,7))
_DryContact2Name_Type=DisplayString
_DryContact2Name_Object=MibScalar
dryContact2Name=_DryContact2Name_Object((1,3,6,1,4,1,3699,1,1,3,2,7,1),_DryContact2Name_Type())
dryContact2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact2Name.setStatus(_A)
class _DryContact2AlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_DryContact2AlertStatus_Type.__name__=_E
_DryContact2AlertStatus_Object=MibScalar
dryContact2AlertStatus=_DryContact2AlertStatus_Object((1,3,6,1,4,1,3699,1,1,3,2,7,2),_DryContact2AlertStatus_Type())
dryContact2AlertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact2AlertStatus.setStatus(_A)
_DryContact3Adm_ObjectIdentity=ObjectIdentity
dryContact3Adm=_DryContact3Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,8))
_DryContact3Name_Type=DisplayString
_DryContact3Name_Object=MibScalar
dryContact3Name=_DryContact3Name_Object((1,3,6,1,4,1,3699,1,1,3,2,8,1),_DryContact3Name_Type())
dryContact3Name.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact3Name.setStatus(_A)
class _DryContact3AlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_DryContact3AlertStatus_Type.__name__=_E
_DryContact3AlertStatus_Object=MibScalar
dryContact3AlertStatus=_DryContact3AlertStatus_Object((1,3,6,1,4,1,3699,1,1,3,2,8,2),_DryContact3AlertStatus_Type())
dryContact3AlertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact3AlertStatus.setStatus(_A)
_DryContact4Adm_ObjectIdentity=ObjectIdentity
dryContact4Adm=_DryContact4Adm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,9))
_DryContact4Name_Type=DisplayString
_DryContact4Name_Object=MibScalar
dryContact4Name=_DryContact4Name_Object((1,3,6,1,4,1,3699,1,1,3,2,9,1),_DryContact4Name_Type())
dryContact4Name.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact4Name.setStatus(_A)
class _DryContact4AlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_DryContact4AlertStatus_Type.__name__=_E
_DryContact4AlertStatus_Object=MibScalar
dryContact4AlertStatus=_DryContact4AlertStatus_Object((1,3,6,1,4,1,3699,1,1,3,2,9,2),_DryContact4AlertStatus_Type())
dryContact4AlertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dryContact4AlertStatus.setStatus(_A)
_WaterSensorAdm_ObjectIdentity=ObjectIdentity
waterSensorAdm=_WaterSensorAdm_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,2,10))
_WaterName_Type=DisplayString
_WaterName_Object=MibScalar
waterName=_WaterName_Object((1,3,6,1,4,1,3699,1,1,3,2,10,1),_WaterName_Type())
waterName.setMaxAccess(_D)
if mibBuilder.loadTexts:waterName.setStatus(_A)
class _WaterAlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_WaterAlertStatus_Type.__name__=_E
_WaterAlertStatus_Object=MibScalar
waterAlertStatus=_WaterAlertStatus_Object((1,3,6,1,4,1,3699,1,1,3,2,10,2),_WaterAlertStatus_Type())
waterAlertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:waterAlertStatus.setStatus(_A)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,3699,1,1,3,3),_Version_Type())
version.setMaxAccess(_C)
if mibBuilder.loadTexts:version.setStatus(_A)
_EnvTraps_ObjectIdentity=ObjectIdentity
envTraps=_EnvTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,100))
_EnvGroups_ObjectIdentity=ObjectIdentity
envGroups=_EnvGroups_ObjectIdentity((1,3,6,1,4,1,3699,1,1,3,200))
_OtherProduct_ObjectIdentity=ObjectIdentity
otherProduct=_OtherProduct_ObjectIdentity((1,3,6,1,4,1,3699,1,1,200))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,3699,1,2))
unitGroup=ObjectGroup((1,3,6,1,4,1,3699,1,1,3,200,1))
unitGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,'sysName'),(_B,_A2),(_B,'sysIP'),(_B,'sysMask'),(_B,_A3),(_B,'sysDNS')))
if mibBuilder.loadTexts:unitGroup.setStatus(_A)
temperatureSensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,1))
if mibBuilder.loadTexts:temperatureSensor1Trap.setStatus(_A)
temperatureSensor2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,2))
if mibBuilder.loadTexts:temperatureSensor2Trap.setStatus(_A)
humiditySensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,3))
if mibBuilder.loadTexts:humiditySensor1Trap.setStatus(_A)
humiditySensor2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,4))
if mibBuilder.loadTexts:humiditySensor2Trap.setStatus(_A)
dryContactSensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,5))
if mibBuilder.loadTexts:dryContactSensor1Trap.setStatus(_A)
dryContactSensor2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,6))
if mibBuilder.loadTexts:dryContactSensor2Trap.setStatus(_A)
dryContactSensor3Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,7))
if mibBuilder.loadTexts:dryContactSensor3Trap.setStatus(_A)
dryContactSensor4Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,8))
if mibBuilder.loadTexts:dryContactSensor4Trap.setStatus(_A)
waterSensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,9))
if mibBuilder.loadTexts:waterSensor1Trap.setStatus(_A)
temperatureSensor1RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,11))
if mibBuilder.loadTexts:temperatureSensor1RetTrap.setStatus(_A)
temperatureSensor2RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,12))
if mibBuilder.loadTexts:temperatureSensor2RetTrap.setStatus(_A)
humiditySensor1RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,13))
if mibBuilder.loadTexts:humiditySensor1RetTrap.setStatus(_A)
humiditySensor2RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,14))
if mibBuilder.loadTexts:humiditySensor2RetTrap.setStatus(_A)
dryContactSensor1RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,15))
if mibBuilder.loadTexts:dryContactSensor1RetTrap.setStatus(_A)
dryContactSensor2RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,16))
if mibBuilder.loadTexts:dryContactSensor2RetTrap.setStatus(_A)
dryContactSensor3RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,17))
if mibBuilder.loadTexts:dryContactSensor3RetTrap.setStatus(_A)
dryContactSensor4RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,18))
if mibBuilder.loadTexts:dryContactSensor4RetTrap.setStatus(_A)
waterSensor1RetTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,19))
if mibBuilder.loadTexts:waterSensor1RetTrap.setStatus(_A)
logTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,100))
if mibBuilder.loadTexts:logTrap.setStatus(_A)
overflowTrap=NotificationType((1,3,6,1,4,1,3699,1,1,3,100,101))
if mibBuilder.loadTexts:overflowTrap.setStatus(_A)
envTrapsGroup=NotificationGroup((1,3,6,1,4,1,3699,1,1,3,200,2))
envTrapsGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,'logTrap'),(_B,_AD)))
if mibBuilder.loadTexts:envTrapsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DecimalPointValue':DecimalPointValue,'nti':nti,'products':products,'hardware':hardware,'enviromuxMini':enviromuxMini,'monitoring':monitoring,'temperatureSensor1':temperatureSensor1,_M:temperatureSensor1CurrentValue,_N:temperatureSensor1Alert,'temperatureSensor2':temperatureSensor2,_S:temperatureSensor2CurrentValue,_T:temperatureSensor2Alert,'humiditySensor1':humiditySensor1,_Y:humiditySensor1CurrentValue,_Z:humiditySensor1Alert,'humiditySensor2':humiditySensor2,_d:humiditySensor2CurrentValue,_e:humiditySensor2Alert,'dryContact1':dryContact1,_i:dryContact1Status,_j:dryContact1Alert,'dryContact2':dryContact2,_m:dryContact2Status,_n:dryContact2Alert,'dryContact3':dryContact3,_q:dryContact3Status,_r:dryContact3Alert,'dryContact4':dryContact4,_u:dryContact4Status,_v:dryContact4Alert,'waterSensor':waterSensor,_y:waterStatus,_z:waterAlert,'administration':administration,'hostSystem':hostSystem,'sysName':sysName,_A2:sysLocation,'sysIP':sysIP,'sysMask':sysMask,_A3:sysGateway,'sysDNS':sysDNS,'temperatureSensor1Adm':temperatureSensor1Adm,_O:temperatureSensor1Name,_P:temperatureSensor1Unit,_Q:temperatureSensor1LowThreshold,_R:temperatureSensor1HighThreshold,'temperatureSensor2Adm':temperatureSensor2Adm,_U:temperatureSensor2Name,_V:temperatureSensor2Unit,_W:temperatureSensor2LowThreshold,_X:temperatureSensor2HighThreshold,'humiditySensor1Adm':humiditySensor1Adm,_a:humiditySensor1Name,_b:humiditySensor1LowThreshold,_c:humiditySensor1HighThreshold,'humiditySensor2Adm':humiditySensor2Adm,_f:humiditySensor2Name,_g:humiditySensor2LowThreshold,_h:humiditySensor2HighThreshold,'dryContact1Adm':dryContact1Adm,_k:dryContact1Name,_l:dryContact1AlertStatus,'dryContact2Adm':dryContact2Adm,_o:dryContact2Name,_p:dryContact2AlertStatus,'dryContact3Adm':dryContact3Adm,_s:dryContact3Name,_t:dryContact3AlertStatus,'dryContact4Adm':dryContact4Adm,_w:dryContact4Name,_x:dryContact4AlertStatus,'waterSensorAdm':waterSensorAdm,_A0:waterName,_A1:waterAlertStatus,_L:version,'envTraps':envTraps,_A4:temperatureSensor1Trap,_A5:temperatureSensor2Trap,_A6:humiditySensor1Trap,_A7:humiditySensor2Trap,_A8:dryContactSensor1Trap,_A9:dryContactSensor2Trap,_AA:dryContactSensor3Trap,_AB:dryContactSensor4Trap,_AC:waterSensor1Trap,'temperatureSensor1RetTrap':temperatureSensor1RetTrap,'temperatureSensor2RetTrap':temperatureSensor2RetTrap,'humiditySensor1RetTrap':humiditySensor1RetTrap,'humiditySensor2RetTrap':humiditySensor2RetTrap,'dryContactSensor1RetTrap':dryContactSensor1RetTrap,'dryContactSensor2RetTrap':dryContactSensor2RetTrap,'dryContactSensor3RetTrap':dryContactSensor3RetTrap,'dryContactSensor4RetTrap':dryContactSensor4RetTrap,'waterSensor1RetTrap':waterSensor1RetTrap,'logTrap':logTrap,_AD:overflowTrap,'envGroups':envGroups,'unitGroup':unitGroup,'envTrapsGroup':envTrapsGroup,'otherProduct':otherProduct,'software':software})