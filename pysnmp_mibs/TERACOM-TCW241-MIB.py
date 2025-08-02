_C2='tcw241TrapGroup'
_C1='tcw241MonitorGroup'
_C0='tcw241SetupGroup'
_B_='tcw241ProductGroup'
_Bz='snmp-trap-notification'
_By='pressureUnit'
_Bx='hardwareErr'
_Bw='temperatureUnit'
_Bv='configurationSaved'
_Bu='relay4Pulse'
_Bt='relay4State'
_Bs='relay3Pulse'
_Br='relay3State'
_Bq='relay2Pulse'
_Bp='relay2State'
_Bo='relay1Pulse'
_Bn='relay1State'
_Bm='virtualInput4Parent'
_Bl='virtualInput4hyst'
_Bk='virtualInput4min'
_Bj='virtualInput4max'
_Bi='virtualInput4description'
_Bh='virtualInput3Parent'
_Bg='virtualInput3hyst'
_Bf='virtualInput3min'
_Be='virtualInput3max'
_Bd='virtualInput3description'
_Bc='virtualInput2Parent'
_Bb='virtualInput2hyst'
_Ba='virtualInput2min'
_BZ='virtualInput2max'
_BY='virtualInput2description'
_BX='virtualInput1Parent'
_BW='virtualInput1hyst'
_BV='virtualInput1min'
_BU='virtualInput1max'
_BT='virtualInput1description'
_BS='relay4action'
_BR='relay4controlledBy'
_BQ='relay4pulseWidth'
_BP='relay4description'
_BO='relay3action'
_BN='relay3controlledBy'
_BM='relay3pulseWidth'
_BL='relay3description'
_BK='relay2action'
_BJ='relay2controlledBy'
_BI='relay2pulseWidth'
_BH='relay2description'
_BG='relay1action'
_BF='relay1controlledBy'
_BE='relay1pulseWidth'
_BD='relay1description'
_BC='digitalInput4description'
_BB='digitalInput3description'
_BA='digitalInput2description'
_B9='digitalInput1description'
_B8='voltage4hyst'
_B7='voltage4min'
_B6='voltage4max'
_B5='voltage4description'
_B4='voltage3hyst'
_B3='voltage3min'
_B2='voltage3max'
_B1='voltage3description'
_B0='voltage2hyst'
_A_='voltage2min'
_Az='voltage2max'
_Ay='voltage2description'
_Ax='voltage1hyst'
_Aw='voltage1min'
_Av='voltage1max'
_Au='voltage1description'
_At='s82HYSTInt'
_As='s82MINInt'
_Ar='s82MAXInt'
_Aq='s81HYSTInt'
_Ap='s81MINInt'
_Ao='s81MAXInt'
_An='s8description'
_Am='s72HYSTInt'
_Al='s72MINInt'
_Ak='s72MAXInt'
_Aj='s71HYSTInt'
_Ai='s71MINInt'
_Ah='s71MAXInt'
_Ag='s7description'
_Af='s62HYSTInt'
_Ae='s62MINInt'
_Ad='s62MAXInt'
_Ac='s61HYSTInt'
_Ab='s61MINInt'
_Aa='s61MAXInt'
_AZ='s6description'
_AY='s52HYSTInt'
_AX='s52MINInt'
_AW='s52MAXInt'
_AV='s51HYSTInt'
_AU='s51MINInt'
_AT='s51MAXInt'
_AS='s5description'
_AR='s42HYSTInt'
_AQ='s42MINInt'
_AP='s42MAXInt'
_AO='s41HYSTInt'
_AN='s41MINInt'
_AM='s41MAXInt'
_AL='s4description'
_AK='s32HYSTInt'
_AJ='s32MINInt'
_AI='s32MAXInt'
_AH='s31HYSTInt'
_AG='s31MINInt'
_AF='s31MAXInt'
_AE='s3description'
_AD='s22HYSTInt'
_AC='s22MINInt'
_AB='s22MAXInt'
_AA='s21HYSTInt'
_A9='s21MINInt'
_A8='s21MAXInt'
_A7='s2description'
_A6='s12HYSTInt'
_A5='s12MINInt'
_A4='s12MAXInt'
_A3='s11HYSTInt'
_A2='s11MINInt'
_A1='s11MAXInt'
_A0='s1description'
_z='sensor31'
_y='sensor22'
_x='sensor21'
_w='sensor12'
_v='sensor11'
_u='virtualInput4Int'
_t='virtualInput3Int'
_s='virtualInput2Int'
_r='virtualInput1Int'
_q='func4State'
_p='func3State'
_o='func2State'
_n='func1State'
_m='restartDevice'
_l='digitalInput4State'
_k='digitalInput3State'
_j='digitalInput2State'
_i='digitalInput1State'
_h='voltage4Int'
_g='voltage3Int'
_f='voltage2Int'
_e='voltage1Int'
_d='s82Int'
_c='s81Int'
_b='s72Int'
_a='s71Int'
_Z='s62Int'
_Y='s61Int'
_X='s52Int'
_W='s51Int'
_V='s42Int'
_U='s41Int'
_T='s32Int'
_S='s31Int'
_R='s22Int'
_Q='s21Int'
_P='s12Int'
_O='s11Int'
_N='deviceIP'
_M='d-3'
_L='true'
_K='false'
_J='open'
_I='closed'
_H='on'
_G='off'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='current'
_A='TERACOM-TCW241-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','snmpModules')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','TextualConvention')
snmpMIB=ModuleIdentity((1,3,6,1,6,3,1))
if mibBuilder.loadTexts:snmpMIB.setRevisions(('2018-01-30 00:00',))
class CONTROLLED(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)));namedValues=NamedValues(*(('manual',0),(_v,1),(_w,2),(_x,3),(_y,4),(_z,5),('sensor32',6),('sensor41',7),('sensor42',8),('sensor51',9),('sensor52',10),('sensor61',11),('sensor62',12),('sensor71',13),('sensor72',14),('sensor81',15),('sensor82',16),('analog1',17),('analog2',18),('analog3',19),('analog4',20),('digital1',21),('digital2',22),('digital3',23),('digital4',24),('anyAlarm',25),('anySensor',26),('anyAnalog',27),('anyDigital',28),('func1',29),('func2',30),('func3',31),('func4',32),('shedule1',33),('shedule2',34),('shedule3',35),('shedule4',36),('virtual1',37),('virtual2',38),('virtual3',39),('virtual4',40)))
class RELAYACTION(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('turnon',0),('pulse',2)))
class VIRTUALPARENT(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('none',0),(_v,1),(_w,2),(_x,3),(_y,4),(_z,5),('sensor32',6),('sensor41',7),('sensor42',8),('sensor51',9),('sensor52',10),('sensor61',11),('sensor62',12),('sensor71',13),('sensor72',14),('sensor81',15),('sensor82',16),('analog1',17),('analog2',18),('analog3',19),('analog4',20)))
class SensorId(TextualConvention,OctetString):status=_B;displayHint='16a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class AnalogValue(TextualConvention,Integer32):status=_B;displayHint=_M
class SensorValue(TextualConvention,Integer32):status=_B;displayHint=_M
class VirtualValue(TextualConvention,Integer32):status=_B;displayHint=_M
_Teracom_ObjectIdentity=ObjectIdentity
teracom=_Teracom_ObjectIdentity((1,3,6,1,4,1,38783))
_Tcw241_ObjectIdentity=ObjectIdentity
tcw241=_Tcw241_ObjectIdentity((1,3,6,1,4,1,38783,3))
_TrapNotifications_ObjectIdentity=ObjectIdentity
trapNotifications=_TrapNotifications_ObjectIdentity((1,3,6,1,4,1,38783,3,0))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,38783,3,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,38783,3,1,1),_Name_Type())
name.setMaxAccess(_D)
if mibBuilder.loadTexts:name.setStatus(_B)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,38783,3,1,2),_Version_Type())
version.setMaxAccess(_D)
if mibBuilder.loadTexts:version.setStatus(_B)
_DateTime_Type=DateAndTime
_DateTime_Object=MibScalar
dateTime=_DateTime_Object((1,3,6,1,4,1,38783,3,1,3),_DateTime_Type())
dateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dateTime.setStatus(_B)
_Setup_ObjectIdentity=ObjectIdentity
setup=_Setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2))
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,38783,3,2,1))
_DeviceID_Type=MacAddress
_DeviceID_Object=MibScalar
deviceID=_DeviceID_Object((1,3,6,1,4,1,38783,3,2,1,1),_DeviceID_Type())
deviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceID.setStatus(_B)
class _HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_HostName_Type.__name__=_F
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,38783,3,2,1,2),_HostName_Type())
hostName.setMaxAccess(_D)
if mibBuilder.loadTexts:hostName.setStatus(_B)
_DeviceIP_Type=IpAddress
_DeviceIP_Object=MibScalar
deviceIP=_DeviceIP_Object((1,3,6,1,4,1,38783,3,2,1,3),_DeviceIP_Type())
deviceIP.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceIP.setStatus(_B)
_Io_ObjectIdentity=ObjectIdentity
io=_Io_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2))
_SensorsSetup_ObjectIdentity=ObjectIdentity
sensorsSetup=_SensorsSetup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1))
_Sensor1setup_ObjectIdentity=ObjectIdentity
sensor1setup=_Sensor1setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,1))
class _S1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S1description_Type.__name__=_F
_S1description_Object=MibScalar
s1description=_S1description_Object((1,3,6,1,4,1,38783,3,2,2,1,1,1),_S1description_Type())
s1description.setMaxAccess(_C)
if mibBuilder.loadTexts:s1description.setStatus(_B)
_Sensor11setup_ObjectIdentity=ObjectIdentity
sensor11setup=_Sensor11setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,1,2))
_S11MAXInt_Type=SensorValue
_S11MAXInt_Object=MibScalar
s11MAXInt=_S11MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,1,2,1),_S11MAXInt_Type())
s11MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s11MAXInt.setStatus(_B)
_S11MINInt_Type=SensorValue
_S11MINInt_Object=MibScalar
s11MINInt=_S11MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,1,2,2),_S11MINInt_Type())
s11MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s11MINInt.setStatus(_B)
_S11HYSTInt_Type=SensorValue
_S11HYSTInt_Object=MibScalar
s11HYSTInt=_S11HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,1,2,3),_S11HYSTInt_Type())
s11HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s11HYSTInt.setStatus(_B)
_Sensor12setup_ObjectIdentity=ObjectIdentity
sensor12setup=_Sensor12setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,1,3))
_S12MAXInt_Type=SensorValue
_S12MAXInt_Object=MibScalar
s12MAXInt=_S12MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,1,3,1),_S12MAXInt_Type())
s12MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s12MAXInt.setStatus(_B)
_S12MINInt_Type=SensorValue
_S12MINInt_Object=MibScalar
s12MINInt=_S12MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,1,3,2),_S12MINInt_Type())
s12MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s12MINInt.setStatus(_B)
_S12HYSTInt_Type=SensorValue
_S12HYSTInt_Object=MibScalar
s12HYSTInt=_S12HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,1,3,3),_S12HYSTInt_Type())
s12HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s12HYSTInt.setStatus(_B)
_Sensor2setup_ObjectIdentity=ObjectIdentity
sensor2setup=_Sensor2setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,2))
class _S2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S2description_Type.__name__=_F
_S2description_Object=MibScalar
s2description=_S2description_Object((1,3,6,1,4,1,38783,3,2,2,1,2,1),_S2description_Type())
s2description.setMaxAccess(_C)
if mibBuilder.loadTexts:s2description.setStatus(_B)
_Sensor21setup_ObjectIdentity=ObjectIdentity
sensor21setup=_Sensor21setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,2,2))
_S21MAXInt_Type=SensorValue
_S21MAXInt_Object=MibScalar
s21MAXInt=_S21MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,2,2,1),_S21MAXInt_Type())
s21MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s21MAXInt.setStatus(_B)
_S21MINInt_Type=SensorValue
_S21MINInt_Object=MibScalar
s21MINInt=_S21MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,2,2,2),_S21MINInt_Type())
s21MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s21MINInt.setStatus(_B)
_S21HYSTInt_Type=SensorValue
_S21HYSTInt_Object=MibScalar
s21HYSTInt=_S21HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,2,2,3),_S21HYSTInt_Type())
s21HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s21HYSTInt.setStatus(_B)
_Sensor22setup_ObjectIdentity=ObjectIdentity
sensor22setup=_Sensor22setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,2,3))
_S22MAXInt_Type=SensorValue
_S22MAXInt_Object=MibScalar
s22MAXInt=_S22MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,2,3,1),_S22MAXInt_Type())
s22MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s22MAXInt.setStatus(_B)
_S22MINInt_Type=SensorValue
_S22MINInt_Object=MibScalar
s22MINInt=_S22MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,2,3,2),_S22MINInt_Type())
s22MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s22MINInt.setStatus(_B)
_S22HYSTInt_Type=SensorValue
_S22HYSTInt_Object=MibScalar
s22HYSTInt=_S22HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,2,3,3),_S22HYSTInt_Type())
s22HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s22HYSTInt.setStatus(_B)
_Sensor3setup_ObjectIdentity=ObjectIdentity
sensor3setup=_Sensor3setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,3))
class _S3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S3description_Type.__name__=_F
_S3description_Object=MibScalar
s3description=_S3description_Object((1,3,6,1,4,1,38783,3,2,2,1,3,1),_S3description_Type())
s3description.setMaxAccess(_C)
if mibBuilder.loadTexts:s3description.setStatus(_B)
_Sensor31setup_ObjectIdentity=ObjectIdentity
sensor31setup=_Sensor31setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,3,2))
_S31MAXInt_Type=SensorValue
_S31MAXInt_Object=MibScalar
s31MAXInt=_S31MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,3,2,1),_S31MAXInt_Type())
s31MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s31MAXInt.setStatus(_B)
_S31MINInt_Type=SensorValue
_S31MINInt_Object=MibScalar
s31MINInt=_S31MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,3,2,2),_S31MINInt_Type())
s31MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s31MINInt.setStatus(_B)
_S31HYSTInt_Type=SensorValue
_S31HYSTInt_Object=MibScalar
s31HYSTInt=_S31HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,3,2,3),_S31HYSTInt_Type())
s31HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s31HYSTInt.setStatus(_B)
_Sensor32setup_ObjectIdentity=ObjectIdentity
sensor32setup=_Sensor32setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,3,3))
_S32MAXInt_Type=SensorValue
_S32MAXInt_Object=MibScalar
s32MAXInt=_S32MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,3,3,1),_S32MAXInt_Type())
s32MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s32MAXInt.setStatus(_B)
_S32MINInt_Type=SensorValue
_S32MINInt_Object=MibScalar
s32MINInt=_S32MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,3,3,2),_S32MINInt_Type())
s32MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s32MINInt.setStatus(_B)
_S32HYSTInt_Type=SensorValue
_S32HYSTInt_Object=MibScalar
s32HYSTInt=_S32HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,3,3,3),_S32HYSTInt_Type())
s32HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s32HYSTInt.setStatus(_B)
_Sensor4setup_ObjectIdentity=ObjectIdentity
sensor4setup=_Sensor4setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,4))
class _S4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S4description_Type.__name__=_F
_S4description_Object=MibScalar
s4description=_S4description_Object((1,3,6,1,4,1,38783,3,2,2,1,4,1),_S4description_Type())
s4description.setMaxAccess(_C)
if mibBuilder.loadTexts:s4description.setStatus(_B)
_Sensor41setup_ObjectIdentity=ObjectIdentity
sensor41setup=_Sensor41setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,4,2))
_S41MAXInt_Type=SensorValue
_S41MAXInt_Object=MibScalar
s41MAXInt=_S41MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,4,2,1),_S41MAXInt_Type())
s41MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s41MAXInt.setStatus(_B)
_S41MINInt_Type=SensorValue
_S41MINInt_Object=MibScalar
s41MINInt=_S41MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,4,2,2),_S41MINInt_Type())
s41MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s41MINInt.setStatus(_B)
_S41HYSTInt_Type=SensorValue
_S41HYSTInt_Object=MibScalar
s41HYSTInt=_S41HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,4,2,3),_S41HYSTInt_Type())
s41HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s41HYSTInt.setStatus(_B)
_Sensor42setup_ObjectIdentity=ObjectIdentity
sensor42setup=_Sensor42setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,4,3))
_S42MAXInt_Type=SensorValue
_S42MAXInt_Object=MibScalar
s42MAXInt=_S42MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,4,3,1),_S42MAXInt_Type())
s42MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s42MAXInt.setStatus(_B)
_S42MINInt_Type=SensorValue
_S42MINInt_Object=MibScalar
s42MINInt=_S42MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,4,3,2),_S42MINInt_Type())
s42MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s42MINInt.setStatus(_B)
_S42HYSTInt_Type=SensorValue
_S42HYSTInt_Object=MibScalar
s42HYSTInt=_S42HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,4,3,3),_S42HYSTInt_Type())
s42HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s42HYSTInt.setStatus(_B)
_Sensor5setup_ObjectIdentity=ObjectIdentity
sensor5setup=_Sensor5setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,5))
class _S5description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S5description_Type.__name__=_F
_S5description_Object=MibScalar
s5description=_S5description_Object((1,3,6,1,4,1,38783,3,2,2,1,5,1),_S5description_Type())
s5description.setMaxAccess(_C)
if mibBuilder.loadTexts:s5description.setStatus(_B)
_Sensor51setup_ObjectIdentity=ObjectIdentity
sensor51setup=_Sensor51setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,5,2))
_S51MAXInt_Type=SensorValue
_S51MAXInt_Object=MibScalar
s51MAXInt=_S51MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,5,2,1),_S51MAXInt_Type())
s51MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s51MAXInt.setStatus(_B)
_S51MINInt_Type=SensorValue
_S51MINInt_Object=MibScalar
s51MINInt=_S51MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,5,2,2),_S51MINInt_Type())
s51MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s51MINInt.setStatus(_B)
_S51HYSTInt_Type=SensorValue
_S51HYSTInt_Object=MibScalar
s51HYSTInt=_S51HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,5,2,3),_S51HYSTInt_Type())
s51HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s51HYSTInt.setStatus(_B)
_Sensor52setup_ObjectIdentity=ObjectIdentity
sensor52setup=_Sensor52setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,5,3))
_S52MAXInt_Type=SensorValue
_S52MAXInt_Object=MibScalar
s52MAXInt=_S52MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,5,3,1),_S52MAXInt_Type())
s52MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s52MAXInt.setStatus(_B)
_S52MINInt_Type=SensorValue
_S52MINInt_Object=MibScalar
s52MINInt=_S52MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,5,3,2),_S52MINInt_Type())
s52MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s52MINInt.setStatus(_B)
_S52HYSTInt_Type=SensorValue
_S52HYSTInt_Object=MibScalar
s52HYSTInt=_S52HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,5,3,3),_S52HYSTInt_Type())
s52HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s52HYSTInt.setStatus(_B)
_Sensor6setup_ObjectIdentity=ObjectIdentity
sensor6setup=_Sensor6setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,6))
class _S6description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S6description_Type.__name__=_F
_S6description_Object=MibScalar
s6description=_S6description_Object((1,3,6,1,4,1,38783,3,2,2,1,6,1),_S6description_Type())
s6description.setMaxAccess(_C)
if mibBuilder.loadTexts:s6description.setStatus(_B)
_Sensor61setup_ObjectIdentity=ObjectIdentity
sensor61setup=_Sensor61setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,6,2))
_S61MAXInt_Type=SensorValue
_S61MAXInt_Object=MibScalar
s61MAXInt=_S61MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,6,2,1),_S61MAXInt_Type())
s61MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s61MAXInt.setStatus(_B)
_S61MINInt_Type=SensorValue
_S61MINInt_Object=MibScalar
s61MINInt=_S61MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,6,2,2),_S61MINInt_Type())
s61MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s61MINInt.setStatus(_B)
_S61HYSTInt_Type=SensorValue
_S61HYSTInt_Object=MibScalar
s61HYSTInt=_S61HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,6,2,3),_S61HYSTInt_Type())
s61HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s61HYSTInt.setStatus(_B)
_Sensor62setup_ObjectIdentity=ObjectIdentity
sensor62setup=_Sensor62setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,6,3))
_S62MAXInt_Type=SensorValue
_S62MAXInt_Object=MibScalar
s62MAXInt=_S62MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,6,3,1),_S62MAXInt_Type())
s62MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s62MAXInt.setStatus(_B)
_S62MINInt_Type=SensorValue
_S62MINInt_Object=MibScalar
s62MINInt=_S62MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,6,3,2),_S62MINInt_Type())
s62MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s62MINInt.setStatus(_B)
_S62HYSTInt_Type=SensorValue
_S62HYSTInt_Object=MibScalar
s62HYSTInt=_S62HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,6,3,3),_S62HYSTInt_Type())
s62HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s62HYSTInt.setStatus(_B)
_Sensor7setup_ObjectIdentity=ObjectIdentity
sensor7setup=_Sensor7setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,7))
class _S7description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S7description_Type.__name__=_F
_S7description_Object=MibScalar
s7description=_S7description_Object((1,3,6,1,4,1,38783,3,2,2,1,7,1),_S7description_Type())
s7description.setMaxAccess(_C)
if mibBuilder.loadTexts:s7description.setStatus(_B)
_Sensor71setup_ObjectIdentity=ObjectIdentity
sensor71setup=_Sensor71setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,7,2))
_S71MAXInt_Type=SensorValue
_S71MAXInt_Object=MibScalar
s71MAXInt=_S71MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,7,2,1),_S71MAXInt_Type())
s71MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s71MAXInt.setStatus(_B)
_S71MINInt_Type=SensorValue
_S71MINInt_Object=MibScalar
s71MINInt=_S71MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,7,2,2),_S71MINInt_Type())
s71MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s71MINInt.setStatus(_B)
_S71HYSTInt_Type=SensorValue
_S71HYSTInt_Object=MibScalar
s71HYSTInt=_S71HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,7,2,3),_S71HYSTInt_Type())
s71HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s71HYSTInt.setStatus(_B)
_Sensor72setup_ObjectIdentity=ObjectIdentity
sensor72setup=_Sensor72setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,7,3))
_S72MAXInt_Type=SensorValue
_S72MAXInt_Object=MibScalar
s72MAXInt=_S72MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,7,3,1),_S72MAXInt_Type())
s72MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s72MAXInt.setStatus(_B)
_S72MINInt_Type=SensorValue
_S72MINInt_Object=MibScalar
s72MINInt=_S72MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,7,3,2),_S72MINInt_Type())
s72MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s72MINInt.setStatus(_B)
_S72HYSTInt_Type=SensorValue
_S72HYSTInt_Object=MibScalar
s72HYSTInt=_S72HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,7,3,3),_S72HYSTInt_Type())
s72HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s72HYSTInt.setStatus(_B)
_Sensor8setup_ObjectIdentity=ObjectIdentity
sensor8setup=_Sensor8setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,8))
class _S8description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S8description_Type.__name__=_F
_S8description_Object=MibScalar
s8description=_S8description_Object((1,3,6,1,4,1,38783,3,2,2,1,8,1),_S8description_Type())
s8description.setMaxAccess(_C)
if mibBuilder.loadTexts:s8description.setStatus(_B)
_Sensor81setup_ObjectIdentity=ObjectIdentity
sensor81setup=_Sensor81setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,8,2))
_S81MAXInt_Type=SensorValue
_S81MAXInt_Object=MibScalar
s81MAXInt=_S81MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,8,2,1),_S81MAXInt_Type())
s81MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s81MAXInt.setStatus(_B)
_S81MINInt_Type=SensorValue
_S81MINInt_Object=MibScalar
s81MINInt=_S81MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,8,2,2),_S81MINInt_Type())
s81MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s81MINInt.setStatus(_B)
_S81HYSTInt_Type=SensorValue
_S81HYSTInt_Object=MibScalar
s81HYSTInt=_S81HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,8,2,3),_S81HYSTInt_Type())
s81HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s81HYSTInt.setStatus(_B)
_Sensor82setup_ObjectIdentity=ObjectIdentity
sensor82setup=_Sensor82setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,1,8,3))
_S82MAXInt_Type=SensorValue
_S82MAXInt_Object=MibScalar
s82MAXInt=_S82MAXInt_Object((1,3,6,1,4,1,38783,3,2,2,1,8,3,1),_S82MAXInt_Type())
s82MAXInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s82MAXInt.setStatus(_B)
_S82MINInt_Type=SensorValue
_S82MINInt_Object=MibScalar
s82MINInt=_S82MINInt_Object((1,3,6,1,4,1,38783,3,2,2,1,8,3,2),_S82MINInt_Type())
s82MINInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s82MINInt.setStatus(_B)
_S82HYSTInt_Type=SensorValue
_S82HYSTInt_Object=MibScalar
s82HYSTInt=_S82HYSTInt_Object((1,3,6,1,4,1,38783,3,2,2,1,8,3,3),_S82HYSTInt_Type())
s82HYSTInt.setMaxAccess(_C)
if mibBuilder.loadTexts:s82HYSTInt.setStatus(_B)
_AnalogSetup_ObjectIdentity=ObjectIdentity
analogSetup=_AnalogSetup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,2))
_Analog1setup_ObjectIdentity=ObjectIdentity
analog1setup=_Analog1setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,2,1))
class _Voltage1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage1description_Type.__name__=_F
_Voltage1description_Object=MibScalar
voltage1description=_Voltage1description_Object((1,3,6,1,4,1,38783,3,2,2,2,1,1),_Voltage1description_Type())
voltage1description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1description.setStatus(_B)
_Voltage1max_Type=AnalogValue
_Voltage1max_Object=MibScalar
voltage1max=_Voltage1max_Object((1,3,6,1,4,1,38783,3,2,2,2,1,2),_Voltage1max_Type())
voltage1max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1max.setStatus(_B)
_Voltage1min_Type=AnalogValue
_Voltage1min_Object=MibScalar
voltage1min=_Voltage1min_Object((1,3,6,1,4,1,38783,3,2,2,2,1,3),_Voltage1min_Type())
voltage1min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1min.setStatus(_B)
_Voltage1hyst_Type=AnalogValue
_Voltage1hyst_Object=MibScalar
voltage1hyst=_Voltage1hyst_Object((1,3,6,1,4,1,38783,3,2,2,2,1,4),_Voltage1hyst_Type())
voltage1hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1hyst.setStatus(_B)
_Analog2setup_ObjectIdentity=ObjectIdentity
analog2setup=_Analog2setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,2,2))
class _Voltage2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage2description_Type.__name__=_F
_Voltage2description_Object=MibScalar
voltage2description=_Voltage2description_Object((1,3,6,1,4,1,38783,3,2,2,2,2,1),_Voltage2description_Type())
voltage2description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2description.setStatus(_B)
_Voltage2max_Type=AnalogValue
_Voltage2max_Object=MibScalar
voltage2max=_Voltage2max_Object((1,3,6,1,4,1,38783,3,2,2,2,2,2),_Voltage2max_Type())
voltage2max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2max.setStatus(_B)
_Voltage2min_Type=AnalogValue
_Voltage2min_Object=MibScalar
voltage2min=_Voltage2min_Object((1,3,6,1,4,1,38783,3,2,2,2,2,3),_Voltage2min_Type())
voltage2min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2min.setStatus(_B)
_Voltage2hyst_Type=AnalogValue
_Voltage2hyst_Object=MibScalar
voltage2hyst=_Voltage2hyst_Object((1,3,6,1,4,1,38783,3,2,2,2,2,4),_Voltage2hyst_Type())
voltage2hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2hyst.setStatus(_B)
_Analog3setup_ObjectIdentity=ObjectIdentity
analog3setup=_Analog3setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,2,3))
class _Voltage3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage3description_Type.__name__=_F
_Voltage3description_Object=MibScalar
voltage3description=_Voltage3description_Object((1,3,6,1,4,1,38783,3,2,2,2,3,1),_Voltage3description_Type())
voltage3description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3description.setStatus(_B)
_Voltage3max_Type=AnalogValue
_Voltage3max_Object=MibScalar
voltage3max=_Voltage3max_Object((1,3,6,1,4,1,38783,3,2,2,2,3,2),_Voltage3max_Type())
voltage3max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3max.setStatus(_B)
_Voltage3min_Type=AnalogValue
_Voltage3min_Object=MibScalar
voltage3min=_Voltage3min_Object((1,3,6,1,4,1,38783,3,2,2,2,3,3),_Voltage3min_Type())
voltage3min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3min.setStatus(_B)
_Voltage3hyst_Type=AnalogValue
_Voltage3hyst_Object=MibScalar
voltage3hyst=_Voltage3hyst_Object((1,3,6,1,4,1,38783,3,2,2,2,3,4),_Voltage3hyst_Type())
voltage3hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3hyst.setStatus(_B)
_Analog4setup_ObjectIdentity=ObjectIdentity
analog4setup=_Analog4setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,2,4))
class _Voltage4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage4description_Type.__name__=_F
_Voltage4description_Object=MibScalar
voltage4description=_Voltage4description_Object((1,3,6,1,4,1,38783,3,2,2,2,4,1),_Voltage4description_Type())
voltage4description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4description.setStatus(_B)
_Voltage4max_Type=AnalogValue
_Voltage4max_Object=MibScalar
voltage4max=_Voltage4max_Object((1,3,6,1,4,1,38783,3,2,2,2,4,2),_Voltage4max_Type())
voltage4max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4max.setStatus(_B)
_Voltage4min_Type=AnalogValue
_Voltage4min_Object=MibScalar
voltage4min=_Voltage4min_Object((1,3,6,1,4,1,38783,3,2,2,2,4,3),_Voltage4min_Type())
voltage4min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4min.setStatus(_B)
_Voltage4hyst_Type=AnalogValue
_Voltage4hyst_Object=MibScalar
voltage4hyst=_Voltage4hyst_Object((1,3,6,1,4,1,38783,3,2,2,2,4,4),_Voltage4hyst_Type())
voltage4hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4hyst.setStatus(_B)
_DigitalSetup_ObjectIdentity=ObjectIdentity
digitalSetup=_DigitalSetup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,3))
class _DigitalInput1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput1description_Type.__name__=_F
_DigitalInput1description_Object=MibScalar
digitalInput1description=_DigitalInput1description_Object((1,3,6,1,4,1,38783,3,2,2,3,1),_DigitalInput1description_Type())
digitalInput1description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput1description.setStatus(_B)
class _DigitalInput2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput2description_Type.__name__=_F
_DigitalInput2description_Object=MibScalar
digitalInput2description=_DigitalInput2description_Object((1,3,6,1,4,1,38783,3,2,2,3,2),_DigitalInput2description_Type())
digitalInput2description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput2description.setStatus(_B)
class _DigitalInput3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput3description_Type.__name__=_F
_DigitalInput3description_Object=MibScalar
digitalInput3description=_DigitalInput3description_Object((1,3,6,1,4,1,38783,3,2,2,3,3),_DigitalInput3description_Type())
digitalInput3description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput3description.setStatus(_B)
class _DigitalInput4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput4description_Type.__name__=_F
_DigitalInput4description_Object=MibScalar
digitalInput4description=_DigitalInput4description_Object((1,3,6,1,4,1,38783,3,2,2,3,4),_DigitalInput4description_Type())
digitalInput4description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput4description.setStatus(_B)
_RelaysSetup_ObjectIdentity=ObjectIdentity
relaysSetup=_RelaysSetup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,4))
_Relay1setup_ObjectIdentity=ObjectIdentity
relay1setup=_Relay1setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,4,1))
class _Relay1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay1description_Type.__name__=_F
_Relay1description_Object=MibScalar
relay1description=_Relay1description_Object((1,3,6,1,4,1,38783,3,2,2,4,1,1),_Relay1description_Type())
relay1description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1description.setStatus(_B)
class _Relay1pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay1pulseWidth_Type.__name__=_E
_Relay1pulseWidth_Object=MibScalar
relay1pulseWidth=_Relay1pulseWidth_Object((1,3,6,1,4,1,38783,3,2,2,4,1,2),_Relay1pulseWidth_Type())
relay1pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1pulseWidth.setStatus(_B)
_Relay1controlledBy_Type=CONTROLLED
_Relay1controlledBy_Object=MibScalar
relay1controlledBy=_Relay1controlledBy_Object((1,3,6,1,4,1,38783,3,2,2,4,1,3),_Relay1controlledBy_Type())
relay1controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1controlledBy.setStatus(_B)
_Relay1action_Type=RELAYACTION
_Relay1action_Object=MibScalar
relay1action=_Relay1action_Object((1,3,6,1,4,1,38783,3,2,2,4,1,4),_Relay1action_Type())
relay1action.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1action.setStatus(_B)
_Relay2setup_ObjectIdentity=ObjectIdentity
relay2setup=_Relay2setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,4,2))
class _Relay2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay2description_Type.__name__=_F
_Relay2description_Object=MibScalar
relay2description=_Relay2description_Object((1,3,6,1,4,1,38783,3,2,2,4,2,1),_Relay2description_Type())
relay2description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2description.setStatus(_B)
class _Relay2pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay2pulseWidth_Type.__name__=_E
_Relay2pulseWidth_Object=MibScalar
relay2pulseWidth=_Relay2pulseWidth_Object((1,3,6,1,4,1,38783,3,2,2,4,2,2),_Relay2pulseWidth_Type())
relay2pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2pulseWidth.setStatus(_B)
_Relay2controlledBy_Type=CONTROLLED
_Relay2controlledBy_Object=MibScalar
relay2controlledBy=_Relay2controlledBy_Object((1,3,6,1,4,1,38783,3,2,2,4,2,3),_Relay2controlledBy_Type())
relay2controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2controlledBy.setStatus(_B)
_Relay2action_Type=RELAYACTION
_Relay2action_Object=MibScalar
relay2action=_Relay2action_Object((1,3,6,1,4,1,38783,3,2,2,4,2,4),_Relay2action_Type())
relay2action.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2action.setStatus(_B)
_Relay3setup_ObjectIdentity=ObjectIdentity
relay3setup=_Relay3setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,4,3))
class _Relay3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay3description_Type.__name__=_F
_Relay3description_Object=MibScalar
relay3description=_Relay3description_Object((1,3,6,1,4,1,38783,3,2,2,4,3,1),_Relay3description_Type())
relay3description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3description.setStatus(_B)
class _Relay3pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay3pulseWidth_Type.__name__=_E
_Relay3pulseWidth_Object=MibScalar
relay3pulseWidth=_Relay3pulseWidth_Object((1,3,6,1,4,1,38783,3,2,2,4,3,2),_Relay3pulseWidth_Type())
relay3pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3pulseWidth.setStatus(_B)
_Relay3controlledBy_Type=CONTROLLED
_Relay3controlledBy_Object=MibScalar
relay3controlledBy=_Relay3controlledBy_Object((1,3,6,1,4,1,38783,3,2,2,4,3,3),_Relay3controlledBy_Type())
relay3controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3controlledBy.setStatus(_B)
_Relay3action_Type=RELAYACTION
_Relay3action_Object=MibScalar
relay3action=_Relay3action_Object((1,3,6,1,4,1,38783,3,2,2,4,3,4),_Relay3action_Type())
relay3action.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3action.setStatus(_B)
_Relay4setup_ObjectIdentity=ObjectIdentity
relay4setup=_Relay4setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,4,4))
class _Relay4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay4description_Type.__name__=_F
_Relay4description_Object=MibScalar
relay4description=_Relay4description_Object((1,3,6,1,4,1,38783,3,2,2,4,4,1),_Relay4description_Type())
relay4description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4description.setStatus(_B)
class _Relay4pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay4pulseWidth_Type.__name__=_E
_Relay4pulseWidth_Object=MibScalar
relay4pulseWidth=_Relay4pulseWidth_Object((1,3,6,1,4,1,38783,3,2,2,4,4,2),_Relay4pulseWidth_Type())
relay4pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4pulseWidth.setStatus(_B)
_Relay4controlledBy_Type=CONTROLLED
_Relay4controlledBy_Object=MibScalar
relay4controlledBy=_Relay4controlledBy_Object((1,3,6,1,4,1,38783,3,2,2,4,4,3),_Relay4controlledBy_Type())
relay4controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4controlledBy.setStatus(_B)
_Relay4action_Type=RELAYACTION
_Relay4action_Object=MibScalar
relay4action=_Relay4action_Object((1,3,6,1,4,1,38783,3,2,2,4,4,4),_Relay4action_Type())
relay4action.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4action.setStatus(_B)
_VirtualSetup_ObjectIdentity=ObjectIdentity
virtualSetup=_VirtualSetup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,5))
_Virtual1setup_ObjectIdentity=ObjectIdentity
virtual1setup=_Virtual1setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,5,1))
class _VirtualInput1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_VirtualInput1description_Type.__name__=_F
_VirtualInput1description_Object=MibScalar
virtualInput1description=_VirtualInput1description_Object((1,3,6,1,4,1,38783,3,2,2,5,1,1),_VirtualInput1description_Type())
virtualInput1description.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput1description.setStatus(_B)
_VirtualInput1max_Type=VirtualValue
_VirtualInput1max_Object=MibScalar
virtualInput1max=_VirtualInput1max_Object((1,3,6,1,4,1,38783,3,2,2,5,1,2),_VirtualInput1max_Type())
virtualInput1max.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput1max.setStatus(_B)
_VirtualInput1min_Type=VirtualValue
_VirtualInput1min_Object=MibScalar
virtualInput1min=_VirtualInput1min_Object((1,3,6,1,4,1,38783,3,2,2,5,1,3),_VirtualInput1min_Type())
virtualInput1min.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput1min.setStatus(_B)
_VirtualInput1hyst_Type=VirtualValue
_VirtualInput1hyst_Object=MibScalar
virtualInput1hyst=_VirtualInput1hyst_Object((1,3,6,1,4,1,38783,3,2,2,5,1,4),_VirtualInput1hyst_Type())
virtualInput1hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput1hyst.setStatus(_B)
_VirtualInput1Parent_Type=VIRTUALPARENT
_VirtualInput1Parent_Object=MibScalar
virtualInput1Parent=_VirtualInput1Parent_Object((1,3,6,1,4,1,38783,3,2,2,5,1,5),_VirtualInput1Parent_Type())
virtualInput1Parent.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput1Parent.setStatus(_B)
_Virtual2setup_ObjectIdentity=ObjectIdentity
virtual2setup=_Virtual2setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,5,2))
class _VirtualInput2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_VirtualInput2description_Type.__name__=_F
_VirtualInput2description_Object=MibScalar
virtualInput2description=_VirtualInput2description_Object((1,3,6,1,4,1,38783,3,2,2,5,2,1),_VirtualInput2description_Type())
virtualInput2description.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput2description.setStatus(_B)
_VirtualInput2max_Type=VirtualValue
_VirtualInput2max_Object=MibScalar
virtualInput2max=_VirtualInput2max_Object((1,3,6,1,4,1,38783,3,2,2,5,2,2),_VirtualInput2max_Type())
virtualInput2max.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput2max.setStatus(_B)
_VirtualInput2min_Type=VirtualValue
_VirtualInput2min_Object=MibScalar
virtualInput2min=_VirtualInput2min_Object((1,3,6,1,4,1,38783,3,2,2,5,2,3),_VirtualInput2min_Type())
virtualInput2min.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput2min.setStatus(_B)
_VirtualInput2hyst_Type=VirtualValue
_VirtualInput2hyst_Object=MibScalar
virtualInput2hyst=_VirtualInput2hyst_Object((1,3,6,1,4,1,38783,3,2,2,5,2,4),_VirtualInput2hyst_Type())
virtualInput2hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput2hyst.setStatus(_B)
_VirtualInput2Parent_Type=VIRTUALPARENT
_VirtualInput2Parent_Object=MibScalar
virtualInput2Parent=_VirtualInput2Parent_Object((1,3,6,1,4,1,38783,3,2,2,5,2,5),_VirtualInput2Parent_Type())
virtualInput2Parent.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput2Parent.setStatus(_B)
_Virtual3setup_ObjectIdentity=ObjectIdentity
virtual3setup=_Virtual3setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,5,3))
class _VirtualInput3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_VirtualInput3description_Type.__name__=_F
_VirtualInput3description_Object=MibScalar
virtualInput3description=_VirtualInput3description_Object((1,3,6,1,4,1,38783,3,2,2,5,3,1),_VirtualInput3description_Type())
virtualInput3description.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput3description.setStatus(_B)
_VirtualInput3max_Type=VirtualValue
_VirtualInput3max_Object=MibScalar
virtualInput3max=_VirtualInput3max_Object((1,3,6,1,4,1,38783,3,2,2,5,3,2),_VirtualInput3max_Type())
virtualInput3max.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput3max.setStatus(_B)
_VirtualInput3min_Type=VirtualValue
_VirtualInput3min_Object=MibScalar
virtualInput3min=_VirtualInput3min_Object((1,3,6,1,4,1,38783,3,2,2,5,3,3),_VirtualInput3min_Type())
virtualInput3min.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput3min.setStatus(_B)
_VirtualInput3hyst_Type=VirtualValue
_VirtualInput3hyst_Object=MibScalar
virtualInput3hyst=_VirtualInput3hyst_Object((1,3,6,1,4,1,38783,3,2,2,5,3,4),_VirtualInput3hyst_Type())
virtualInput3hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput3hyst.setStatus(_B)
_VirtualInput3Parent_Type=VIRTUALPARENT
_VirtualInput3Parent_Object=MibScalar
virtualInput3Parent=_VirtualInput3Parent_Object((1,3,6,1,4,1,38783,3,2,2,5,3,5),_VirtualInput3Parent_Type())
virtualInput3Parent.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput3Parent.setStatus(_B)
_Virtual4setup_ObjectIdentity=ObjectIdentity
virtual4setup=_Virtual4setup_ObjectIdentity((1,3,6,1,4,1,38783,3,2,2,5,4))
class _VirtualInput4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_VirtualInput4description_Type.__name__=_F
_VirtualInput4description_Object=MibScalar
virtualInput4description=_VirtualInput4description_Object((1,3,6,1,4,1,38783,3,2,2,5,4,1),_VirtualInput4description_Type())
virtualInput4description.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput4description.setStatus(_B)
_VirtualInput4max_Type=VirtualValue
_VirtualInput4max_Object=MibScalar
virtualInput4max=_VirtualInput4max_Object((1,3,6,1,4,1,38783,3,2,2,5,4,2),_VirtualInput4max_Type())
virtualInput4max.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput4max.setStatus(_B)
_VirtualInput4min_Type=VirtualValue
_VirtualInput4min_Object=MibScalar
virtualInput4min=_VirtualInput4min_Object((1,3,6,1,4,1,38783,3,2,2,5,4,3),_VirtualInput4min_Type())
virtualInput4min.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput4min.setStatus(_B)
_VirtualInput4hyst_Type=VirtualValue
_VirtualInput4hyst_Object=MibScalar
virtualInput4hyst=_VirtualInput4hyst_Object((1,3,6,1,4,1,38783,3,2,2,5,4,4),_VirtualInput4hyst_Type())
virtualInput4hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput4hyst.setStatus(_B)
_VirtualInput4Parent_Type=VIRTUALPARENT
_VirtualInput4Parent_Object=MibScalar
virtualInput4Parent=_VirtualInput4Parent_Object((1,3,6,1,4,1,38783,3,2,2,5,4,5),_VirtualInput4Parent_Type())
virtualInput4Parent.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualInput4Parent.setStatus(_B)
_MonitorNcontrol_ObjectIdentity=ObjectIdentity
monitorNcontrol=_MonitorNcontrol_ObjectIdentity((1,3,6,1,4,1,38783,3,3))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1))
_Sensor1_ObjectIdentity=ObjectIdentity
sensor1=_Sensor1_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,1))
_S11Int_Type=SensorValue
_S11Int_Object=MibScalar
s11Int=_S11Int_Object((1,3,6,1,4,1,38783,3,3,1,1,1),_S11Int_Type())
s11Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s11Int.setStatus(_B)
_S12Int_Type=SensorValue
_S12Int_Object=MibScalar
s12Int=_S12Int_Object((1,3,6,1,4,1,38783,3,3,1,1,2),_S12Int_Type())
s12Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s12Int.setStatus(_B)
_S1ID_Type=SensorId
_S1ID_Object=MibScalar
s1ID=_S1ID_Object((1,3,6,1,4,1,38783,3,3,1,1,3),_S1ID_Type())
s1ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s1ID.setStatus(_B)
_Sensor2_ObjectIdentity=ObjectIdentity
sensor2=_Sensor2_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,2))
_S21Int_Type=SensorValue
_S21Int_Object=MibScalar
s21Int=_S21Int_Object((1,3,6,1,4,1,38783,3,3,1,2,1),_S21Int_Type())
s21Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s21Int.setStatus(_B)
_S22Int_Type=SensorValue
_S22Int_Object=MibScalar
s22Int=_S22Int_Object((1,3,6,1,4,1,38783,3,3,1,2,2),_S22Int_Type())
s22Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s22Int.setStatus(_B)
_S2ID_Type=SensorId
_S2ID_Object=MibScalar
s2ID=_S2ID_Object((1,3,6,1,4,1,38783,3,3,1,2,3),_S2ID_Type())
s2ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s2ID.setStatus(_B)
_Sensor3_ObjectIdentity=ObjectIdentity
sensor3=_Sensor3_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,3))
_S31Int_Type=SensorValue
_S31Int_Object=MibScalar
s31Int=_S31Int_Object((1,3,6,1,4,1,38783,3,3,1,3,1),_S31Int_Type())
s31Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s31Int.setStatus(_B)
_S32Int_Type=SensorValue
_S32Int_Object=MibScalar
s32Int=_S32Int_Object((1,3,6,1,4,1,38783,3,3,1,3,2),_S32Int_Type())
s32Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s32Int.setStatus(_B)
_S3ID_Type=SensorId
_S3ID_Object=MibScalar
s3ID=_S3ID_Object((1,3,6,1,4,1,38783,3,3,1,3,3),_S3ID_Type())
s3ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s3ID.setStatus(_B)
_Sensor4_ObjectIdentity=ObjectIdentity
sensor4=_Sensor4_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,4))
_S41Int_Type=SensorValue
_S41Int_Object=MibScalar
s41Int=_S41Int_Object((1,3,6,1,4,1,38783,3,3,1,4,1),_S41Int_Type())
s41Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s41Int.setStatus(_B)
_S42Int_Type=SensorValue
_S42Int_Object=MibScalar
s42Int=_S42Int_Object((1,3,6,1,4,1,38783,3,3,1,4,2),_S42Int_Type())
s42Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s42Int.setStatus(_B)
_S4ID_Type=SensorId
_S4ID_Object=MibScalar
s4ID=_S4ID_Object((1,3,6,1,4,1,38783,3,3,1,4,3),_S4ID_Type())
s4ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s4ID.setStatus(_B)
_Sensor5_ObjectIdentity=ObjectIdentity
sensor5=_Sensor5_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,5))
_S51Int_Type=SensorValue
_S51Int_Object=MibScalar
s51Int=_S51Int_Object((1,3,6,1,4,1,38783,3,3,1,5,1),_S51Int_Type())
s51Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s51Int.setStatus(_B)
_S52Int_Type=SensorValue
_S52Int_Object=MibScalar
s52Int=_S52Int_Object((1,3,6,1,4,1,38783,3,3,1,5,2),_S52Int_Type())
s52Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s52Int.setStatus(_B)
_S5ID_Type=SensorId
_S5ID_Object=MibScalar
s5ID=_S5ID_Object((1,3,6,1,4,1,38783,3,3,1,5,3),_S5ID_Type())
s5ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s5ID.setStatus(_B)
_Sensor6_ObjectIdentity=ObjectIdentity
sensor6=_Sensor6_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,6))
_S61Int_Type=SensorValue
_S61Int_Object=MibScalar
s61Int=_S61Int_Object((1,3,6,1,4,1,38783,3,3,1,6,1),_S61Int_Type())
s61Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s61Int.setStatus(_B)
_S62Int_Type=SensorValue
_S62Int_Object=MibScalar
s62Int=_S62Int_Object((1,3,6,1,4,1,38783,3,3,1,6,2),_S62Int_Type())
s62Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s62Int.setStatus(_B)
_S6ID_Type=SensorId
_S6ID_Object=MibScalar
s6ID=_S6ID_Object((1,3,6,1,4,1,38783,3,3,1,6,3),_S6ID_Type())
s6ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s6ID.setStatus(_B)
_Sensor7_ObjectIdentity=ObjectIdentity
sensor7=_Sensor7_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,7))
_S71Int_Type=SensorValue
_S71Int_Object=MibScalar
s71Int=_S71Int_Object((1,3,6,1,4,1,38783,3,3,1,7,1),_S71Int_Type())
s71Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s71Int.setStatus(_B)
_S72Int_Type=SensorValue
_S72Int_Object=MibScalar
s72Int=_S72Int_Object((1,3,6,1,4,1,38783,3,3,1,7,2),_S72Int_Type())
s72Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s72Int.setStatus(_B)
_S7ID_Type=SensorId
_S7ID_Object=MibScalar
s7ID=_S7ID_Object((1,3,6,1,4,1,38783,3,3,1,7,3),_S7ID_Type())
s7ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s7ID.setStatus(_B)
_Sensor8_ObjectIdentity=ObjectIdentity
sensor8=_Sensor8_ObjectIdentity((1,3,6,1,4,1,38783,3,3,1,8))
_S81Int_Type=SensorValue
_S81Int_Object=MibScalar
s81Int=_S81Int_Object((1,3,6,1,4,1,38783,3,3,1,8,1),_S81Int_Type())
s81Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s81Int.setStatus(_B)
_S82Int_Type=SensorValue
_S82Int_Object=MibScalar
s82Int=_S82Int_Object((1,3,6,1,4,1,38783,3,3,1,8,2),_S82Int_Type())
s82Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s82Int.setStatus(_B)
_S8ID_Type=SensorId
_S8ID_Object=MibScalar
s8ID=_S8ID_Object((1,3,6,1,4,1,38783,3,3,1,8,3),_S8ID_Type())
s8ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s8ID.setStatus(_B)
_Analog_ObjectIdentity=ObjectIdentity
analog=_Analog_ObjectIdentity((1,3,6,1,4,1,38783,3,3,2))
_Voltage1Int_Type=AnalogValue
_Voltage1Int_Object=MibScalar
voltage1Int=_Voltage1Int_Object((1,3,6,1,4,1,38783,3,3,2,1),_Voltage1Int_Type())
voltage1Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage1Int.setStatus(_B)
_Voltage2Int_Type=AnalogValue
_Voltage2Int_Object=MibScalar
voltage2Int=_Voltage2Int_Object((1,3,6,1,4,1,38783,3,3,2,2),_Voltage2Int_Type())
voltage2Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage2Int.setStatus(_B)
_Voltage3Int_Type=AnalogValue
_Voltage3Int_Object=MibScalar
voltage3Int=_Voltage3Int_Object((1,3,6,1,4,1,38783,3,3,2,3),_Voltage3Int_Type())
voltage3Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage3Int.setStatus(_B)
_Voltage4Int_Type=AnalogValue
_Voltage4Int_Object=MibScalar
voltage4Int=_Voltage4Int_Object((1,3,6,1,4,1,38783,3,3,2,4),_Voltage4Int_Type())
voltage4Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage4Int.setStatus(_B)
_Digital_ObjectIdentity=ObjectIdentity
digital=_Digital_ObjectIdentity((1,3,6,1,4,1,38783,3,3,3))
class _DigitalInput1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput1State_Type.__name__=_E
_DigitalInput1State_Object=MibScalar
digitalInput1State=_DigitalInput1State_Object((1,3,6,1,4,1,38783,3,3,3,1),_DigitalInput1State_Type())
digitalInput1State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput1State.setStatus(_B)
class _DigitalInput2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput2State_Type.__name__=_E
_DigitalInput2State_Object=MibScalar
digitalInput2State=_DigitalInput2State_Object((1,3,6,1,4,1,38783,3,3,3,2),_DigitalInput2State_Type())
digitalInput2State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput2State.setStatus(_B)
class _DigitalInput3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput3State_Type.__name__=_E
_DigitalInput3State_Object=MibScalar
digitalInput3State=_DigitalInput3State_Object((1,3,6,1,4,1,38783,3,3,3,3),_DigitalInput3State_Type())
digitalInput3State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput3State.setStatus(_B)
class _DigitalInput4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput4State_Type.__name__=_E
_DigitalInput4State_Object=MibScalar
digitalInput4State=_DigitalInput4State_Object((1,3,6,1,4,1,38783,3,3,3,4),_DigitalInput4State_Type())
digitalInput4State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput4State.setStatus(_B)
_Relays_ObjectIdentity=ObjectIdentity
relays=_Relays_ObjectIdentity((1,3,6,1,4,1,38783,3,3,4))
_Relay1_ObjectIdentity=ObjectIdentity
relay1=_Relay1_ObjectIdentity((1,3,6,1,4,1,38783,3,3,4,1))
class _Relay1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay1State_Type.__name__=_E
_Relay1State_Object=MibScalar
relay1State=_Relay1State_Object((1,3,6,1,4,1,38783,3,3,4,1,1),_Relay1State_Type())
relay1State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1State.setStatus(_B)
class _Relay1Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay1Pulse_Type.__name__=_E
_Relay1Pulse_Object=MibScalar
relay1Pulse=_Relay1Pulse_Object((1,3,6,1,4,1,38783,3,3,4,1,2),_Relay1Pulse_Type())
relay1Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1Pulse.setStatus(_B)
_Relay2_ObjectIdentity=ObjectIdentity
relay2=_Relay2_ObjectIdentity((1,3,6,1,4,1,38783,3,3,4,2))
class _Relay2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay2State_Type.__name__=_E
_Relay2State_Object=MibScalar
relay2State=_Relay2State_Object((1,3,6,1,4,1,38783,3,3,4,2,1),_Relay2State_Type())
relay2State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2State.setStatus(_B)
class _Relay2Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay2Pulse_Type.__name__=_E
_Relay2Pulse_Object=MibScalar
relay2Pulse=_Relay2Pulse_Object((1,3,6,1,4,1,38783,3,3,4,2,2),_Relay2Pulse_Type())
relay2Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2Pulse.setStatus(_B)
_Relay3_ObjectIdentity=ObjectIdentity
relay3=_Relay3_ObjectIdentity((1,3,6,1,4,1,38783,3,3,4,3))
class _Relay3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay3State_Type.__name__=_E
_Relay3State_Object=MibScalar
relay3State=_Relay3State_Object((1,3,6,1,4,1,38783,3,3,4,3,1),_Relay3State_Type())
relay3State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3State.setStatus(_B)
class _Relay3Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay3Pulse_Type.__name__=_E
_Relay3Pulse_Object=MibScalar
relay3Pulse=_Relay3Pulse_Object((1,3,6,1,4,1,38783,3,3,4,3,2),_Relay3Pulse_Type())
relay3Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3Pulse.setStatus(_B)
_Relay4_ObjectIdentity=ObjectIdentity
relay4=_Relay4_ObjectIdentity((1,3,6,1,4,1,38783,3,3,4,4))
class _Relay4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay4State_Type.__name__=_E
_Relay4State_Object=MibScalar
relay4State=_Relay4State_Object((1,3,6,1,4,1,38783,3,3,4,4,1),_Relay4State_Type())
relay4State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4State.setStatus(_B)
class _Relay4Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay4Pulse_Type.__name__=_E
_Relay4Pulse_Object=MibScalar
relay4Pulse=_Relay4Pulse_Object((1,3,6,1,4,1,38783,3,3,4,4,2),_Relay4Pulse_Type())
relay4Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4Pulse.setStatus(_B)
class _ConfigurationSaved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsaved',0),('saved',1)))
_ConfigurationSaved_Type.__name__=_E
_ConfigurationSaved_Object=MibScalar
configurationSaved=_ConfigurationSaved_Object((1,3,6,1,4,1,38783,3,3,5),_ConfigurationSaved_Type())
configurationSaved.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationSaved.setStatus(_B)
class _RestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cancel',0),('restart',1)))
_RestartDevice_Type.__name__=_E
_RestartDevice_Object=MibScalar
restartDevice=_RestartDevice_Object((1,3,6,1,4,1,38783,3,3,6),_RestartDevice_Type())
restartDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:restartDevice.setStatus(_B)
class _TemperatureUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('celcius',0),('fahrenheit',1)))
_TemperatureUnit_Type.__name__=_E
_TemperatureUnit_Object=MibScalar
temperatureUnit=_TemperatureUnit_Object((1,3,6,1,4,1,38783,3,3,7),_TemperatureUnit_Type())
temperatureUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureUnit.setStatus(_B)
class _HardwareErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noErr',0),('owErr',1),('hwErr',2)))
_HardwareErr_Type.__name__=_E
_HardwareErr_Object=MibScalar
hardwareErr=_HardwareErr_Object((1,3,6,1,4,1,38783,3,3,8),_HardwareErr_Type())
hardwareErr.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwareErr.setStatus(_B)
class _PressureUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hPa',0),('mbar',1),('mmhg',2)))
_PressureUnit_Type.__name__=_E
_PressureUnit_Object=MibScalar
pressureUnit=_PressureUnit_Object((1,3,6,1,4,1,38783,3,3,9),_PressureUnit_Type())
pressureUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:pressureUnit.setStatus(_B)
_Functions_ObjectIdentity=ObjectIdentity
functions=_Functions_ObjectIdentity((1,3,6,1,4,1,38783,3,3,10))
class _Func1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Func1State_Type.__name__=_E
_Func1State_Object=MibScalar
func1State=_Func1State_Object((1,3,6,1,4,1,38783,3,3,10,1),_Func1State_Type())
func1State.setMaxAccess(_D)
if mibBuilder.loadTexts:func1State.setStatus(_B)
class _Func2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Func2State_Type.__name__=_E
_Func2State_Object=MibScalar
func2State=_Func2State_Object((1,3,6,1,4,1,38783,3,3,10,2),_Func2State_Type())
func2State.setMaxAccess(_D)
if mibBuilder.loadTexts:func2State.setStatus(_B)
class _Func3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Func3State_Type.__name__=_E
_Func3State_Object=MibScalar
func3State=_Func3State_Object((1,3,6,1,4,1,38783,3,3,10,3),_Func3State_Type())
func3State.setMaxAccess(_D)
if mibBuilder.loadTexts:func3State.setStatus(_B)
class _Func4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Func4State_Type.__name__=_E
_Func4State_Object=MibScalar
func4State=_Func4State_Object((1,3,6,1,4,1,38783,3,3,10,4),_Func4State_Type())
func4State.setMaxAccess(_D)
if mibBuilder.loadTexts:func4State.setStatus(_B)
_Virtual_ObjectIdentity=ObjectIdentity
virtual=_Virtual_ObjectIdentity((1,3,6,1,4,1,38783,3,3,11))
_VirtualInput1Int_Type=VirtualValue
_VirtualInput1Int_Object=MibScalar
virtualInput1Int=_VirtualInput1Int_Object((1,3,6,1,4,1,38783,3,3,11,1),_VirtualInput1Int_Type())
virtualInput1Int.setMaxAccess(_D)
if mibBuilder.loadTexts:virtualInput1Int.setStatus(_B)
_VirtualInput2Int_Type=VirtualValue
_VirtualInput2Int_Object=MibScalar
virtualInput2Int=_VirtualInput2Int_Object((1,3,6,1,4,1,38783,3,3,11,2),_VirtualInput2Int_Type())
virtualInput2Int.setMaxAccess(_D)
if mibBuilder.loadTexts:virtualInput2Int.setStatus(_B)
_VirtualInput3Int_Type=VirtualValue
_VirtualInput3Int_Object=MibScalar
virtualInput3Int=_VirtualInput3Int_Object((1,3,6,1,4,1,38783,3,3,11,3),_VirtualInput3Int_Type())
virtualInput3Int.setMaxAccess(_D)
if mibBuilder.loadTexts:virtualInput3Int.setStatus(_B)
_VirtualInput4Int_Type=VirtualValue
_VirtualInput4Int_Object=MibScalar
virtualInput4Int=_VirtualInput4Int_Object((1,3,6,1,4,1,38783,3,3,11,4),_VirtualInput4Int_Type())
virtualInput4Int.setMaxAccess(_D)
if mibBuilder.loadTexts:virtualInput4Int.setStatus(_B)
_Tcw241MIBConformance_ObjectIdentity=ObjectIdentity
tcw241MIBConformance=_Tcw241MIBConformance_ObjectIdentity((1,3,6,1,4,1,38783,3,4))
_Tcw241MIBCompliances_ObjectIdentity=ObjectIdentity
tcw241MIBCompliances=_Tcw241MIBCompliances_ObjectIdentity((1,3,6,1,4,1,38783,3,4,1))
_Tcw241MIBGroups_ObjectIdentity=ObjectIdentity
tcw241MIBGroups=_Tcw241MIBGroups_ObjectIdentity((1,3,6,1,4,1,38783,3,4,2))
tcw241ProductGroup=ObjectGroup((1,3,6,1,4,1,38783,3,4,2,1))
tcw241ProductGroup.setObjects(*((_A,'name'),(_A,'version'),(_A,'dateTime')))
if mibBuilder.loadTexts:tcw241ProductGroup.setStatus(_B)
tcw241SetupGroup=ObjectGroup((1,3,6,1,4,1,38783,3,4,2,2))
tcw241SetupGroup.setObjects(*((_A,'deviceID'),(_A,'hostName'),(_A,_N),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ),(_A,_BR),(_A,_BS),(_A,_BT),(_A,_BU),(_A,_BV),(_A,_BW),(_A,_BX),(_A,_BY),(_A,_BZ),(_A,_Ba),(_A,_Bb),(_A,_Bc),(_A,_Bd),(_A,_Be),(_A,_Bf),(_A,_Bg),(_A,_Bh),(_A,_Bi),(_A,_Bj),(_A,_Bk),(_A,_Bl),(_A,_Bm)))
if mibBuilder.loadTexts:tcw241SetupGroup.setStatus(_B)
tcw241MonitorGroup=ObjectGroup((1,3,6,1,4,1,38783,3,4,2,3))
tcw241MonitorGroup.setObjects(*((_A,_O),(_A,_P),(_A,'s1ID'),(_A,_Q),(_A,_R),(_A,'s2ID'),(_A,_S),(_A,_T),(_A,'s3ID'),(_A,_U),(_A,_V),(_A,'s4ID'),(_A,_W),(_A,_X),(_A,'s5ID'),(_A,_Y),(_A,_Z),(_A,'s6ID'),(_A,_a),(_A,_b),(_A,'s7ID'),(_A,_c),(_A,_d),(_A,'s8ID'),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_Bn),(_A,_Bo),(_A,_Bp),(_A,_Bq),(_A,_Br),(_A,_Bs),(_A,_Bt),(_A,_Bu),(_A,_Bv),(_A,_m),(_A,_Bw),(_A,_Bx),(_A,_By),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:tcw241MonitorGroup.setStatus(_B)
snmp_trap_notification=NotificationType((1,3,6,1,4,1,38783,3,0,1))
snmp_trap_notification.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_m),(_A,_N),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:snmp_trap_notification.setStatus(_B)
tcw241TrapGroup=NotificationGroup((1,3,6,1,4,1,38783,3,4,2,4))
tcw241TrapGroup.setObjects((_A,_Bz))
if mibBuilder.loadTexts:tcw241TrapGroup.setStatus(_B)
tcw241MIBCompliances1=ModuleCompliance((1,3,6,1,4,1,38783,3,4,1,1))
tcw241MIBCompliances1.setObjects(*((_A,_B_),(_A,_C0),(_A,_C1),(_A,_C2)))
if mibBuilder.loadTexts:tcw241MIBCompliances1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CONTROLLED':CONTROLLED,'RELAYACTION':RELAYACTION,'VIRTUALPARENT':VIRTUALPARENT,'SensorId':SensorId,'AnalogValue':AnalogValue,'SensorValue':SensorValue,'VirtualValue':VirtualValue,'teracom':teracom,'tcw241':tcw241,'trapNotifications':trapNotifications,_Bz:snmp_trap_notification,'product':product,'name':name,'version':version,'dateTime':dateTime,'setup':setup,'network':network,'deviceID':deviceID,'hostName':hostName,_N:deviceIP,'io':io,'sensorsSetup':sensorsSetup,'sensor1setup':sensor1setup,_A0:s1description,'sensor11setup':sensor11setup,_A1:s11MAXInt,_A2:s11MINInt,_A3:s11HYSTInt,'sensor12setup':sensor12setup,_A4:s12MAXInt,_A5:s12MINInt,_A6:s12HYSTInt,'sensor2setup':sensor2setup,_A7:s2description,'sensor21setup':sensor21setup,_A8:s21MAXInt,_A9:s21MINInt,_AA:s21HYSTInt,'sensor22setup':sensor22setup,_AB:s22MAXInt,_AC:s22MINInt,_AD:s22HYSTInt,'sensor3setup':sensor3setup,_AE:s3description,'sensor31setup':sensor31setup,_AF:s31MAXInt,_AG:s31MINInt,_AH:s31HYSTInt,'sensor32setup':sensor32setup,_AI:s32MAXInt,_AJ:s32MINInt,_AK:s32HYSTInt,'sensor4setup':sensor4setup,_AL:s4description,'sensor41setup':sensor41setup,_AM:s41MAXInt,_AN:s41MINInt,_AO:s41HYSTInt,'sensor42setup':sensor42setup,_AP:s42MAXInt,_AQ:s42MINInt,_AR:s42HYSTInt,'sensor5setup':sensor5setup,_AS:s5description,'sensor51setup':sensor51setup,_AT:s51MAXInt,_AU:s51MINInt,_AV:s51HYSTInt,'sensor52setup':sensor52setup,_AW:s52MAXInt,_AX:s52MINInt,_AY:s52HYSTInt,'sensor6setup':sensor6setup,_AZ:s6description,'sensor61setup':sensor61setup,_Aa:s61MAXInt,_Ab:s61MINInt,_Ac:s61HYSTInt,'sensor62setup':sensor62setup,_Ad:s62MAXInt,_Ae:s62MINInt,_Af:s62HYSTInt,'sensor7setup':sensor7setup,_Ag:s7description,'sensor71setup':sensor71setup,_Ah:s71MAXInt,_Ai:s71MINInt,_Aj:s71HYSTInt,'sensor72setup':sensor72setup,_Ak:s72MAXInt,_Al:s72MINInt,_Am:s72HYSTInt,'sensor8setup':sensor8setup,_An:s8description,'sensor81setup':sensor81setup,_Ao:s81MAXInt,_Ap:s81MINInt,_Aq:s81HYSTInt,'sensor82setup':sensor82setup,_Ar:s82MAXInt,_As:s82MINInt,_At:s82HYSTInt,'analogSetup':analogSetup,'analog1setup':analog1setup,_Au:voltage1description,_Av:voltage1max,_Aw:voltage1min,_Ax:voltage1hyst,'analog2setup':analog2setup,_Ay:voltage2description,_Az:voltage2max,_A_:voltage2min,_B0:voltage2hyst,'analog3setup':analog3setup,_B1:voltage3description,_B2:voltage3max,_B3:voltage3min,_B4:voltage3hyst,'analog4setup':analog4setup,_B5:voltage4description,_B6:voltage4max,_B7:voltage4min,_B8:voltage4hyst,'digitalSetup':digitalSetup,_B9:digitalInput1description,_BA:digitalInput2description,_BB:digitalInput3description,_BC:digitalInput4description,'relaysSetup':relaysSetup,'relay1setup':relay1setup,_BD:relay1description,_BE:relay1pulseWidth,_BF:relay1controlledBy,_BG:relay1action,'relay2setup':relay2setup,_BH:relay2description,_BI:relay2pulseWidth,_BJ:relay2controlledBy,_BK:relay2action,'relay3setup':relay3setup,_BL:relay3description,_BM:relay3pulseWidth,_BN:relay3controlledBy,_BO:relay3action,'relay4setup':relay4setup,_BP:relay4description,_BQ:relay4pulseWidth,_BR:relay4controlledBy,_BS:relay4action,'virtualSetup':virtualSetup,'virtual1setup':virtual1setup,_BT:virtualInput1description,_BU:virtualInput1max,_BV:virtualInput1min,_BW:virtualInput1hyst,_BX:virtualInput1Parent,'virtual2setup':virtual2setup,_BY:virtualInput2description,_BZ:virtualInput2max,_Ba:virtualInput2min,_Bb:virtualInput2hyst,_Bc:virtualInput2Parent,'virtual3setup':virtual3setup,_Bd:virtualInput3description,_Be:virtualInput3max,_Bf:virtualInput3min,_Bg:virtualInput3hyst,_Bh:virtualInput3Parent,'virtual4setup':virtual4setup,_Bi:virtualInput4description,_Bj:virtualInput4max,_Bk:virtualInput4min,_Bl:virtualInput4hyst,_Bm:virtualInput4Parent,'monitorNcontrol':monitorNcontrol,'sensors':sensors,'sensor1':sensor1,_O:s11Int,_P:s12Int,'s1ID':s1ID,'sensor2':sensor2,_Q:s21Int,_R:s22Int,'s2ID':s2ID,'sensor3':sensor3,_S:s31Int,_T:s32Int,'s3ID':s3ID,'sensor4':sensor4,_U:s41Int,_V:s42Int,'s4ID':s4ID,'sensor5':sensor5,_W:s51Int,_X:s52Int,'s5ID':s5ID,'sensor6':sensor6,_Y:s61Int,_Z:s62Int,'s6ID':s6ID,'sensor7':sensor7,_a:s71Int,_b:s72Int,'s7ID':s7ID,'sensor8':sensor8,_c:s81Int,_d:s82Int,'s8ID':s8ID,'analog':analog,_e:voltage1Int,_f:voltage2Int,_g:voltage3Int,_h:voltage4Int,'digital':digital,_i:digitalInput1State,_j:digitalInput2State,_k:digitalInput3State,_l:digitalInput4State,'relays':relays,'relay1':relay1,_Bn:relay1State,_Bo:relay1Pulse,'relay2':relay2,_Bp:relay2State,_Bq:relay2Pulse,'relay3':relay3,_Br:relay3State,_Bs:relay3Pulse,'relay4':relay4,_Bt:relay4State,_Bu:relay4Pulse,_Bv:configurationSaved,_m:restartDevice,_Bw:temperatureUnit,_Bx:hardwareErr,_By:pressureUnit,'functions':functions,_n:func1State,_o:func2State,_p:func3State,_q:func4State,'virtual':virtual,_r:virtualInput1Int,_s:virtualInput2Int,_t:virtualInput3Int,_u:virtualInput4Int,'tcw241MIBConformance':tcw241MIBConformance,'tcw241MIBCompliances':tcw241MIBCompliances,'tcw241MIBCompliances1':tcw241MIBCompliances1,'tcw241MIBGroups':tcw241MIBGroups,_B_:tcw241ProductGroup,_C0:tcw241SetupGroup,_C1:tcw241MonitorGroup,_C2:tcw241TrapGroup,'snmpMIB':snmpMIB})