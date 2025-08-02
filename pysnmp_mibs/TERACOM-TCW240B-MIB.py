_BW='tcw240bTrapGroup'
_BV='tcw240bMonitorGroup'
_BU='tcw240bSetupGroup'
_BT='tcw240bProductGroup'
_BS='snmp-trap-notification'
_BR='hardwareErr'
_BQ='temperatureUnit'
_BP='configurationSaved'
_BO='relay4Pulse'
_BN='relay4State'
_BM='relay3Pulse'
_BL='relay3State'
_BK='relay2Pulse'
_BJ='relay2State'
_BI='relay1Pulse'
_BH='relay1State'
_BG='voltage4x100Int'
_BF='voltage3x100Int'
_BE='voltage2x100Int'
_BD='voltage1x100Int'
_BC='relay4controlledBy'
_BB='relay4pulseWidth'
_BA='relay4description'
_B9='relay3controlledBy'
_B8='relay3pulseWidth'
_B7='relay3description'
_B6='relay2controlledBy'
_B5='relay2pulseWidth'
_B4='relay2description'
_B3='relay1controlledBy'
_B2='relay1pulseWidth'
_B1='relay1description'
_B0='digitalInput4description'
_A_='digitalInput3description'
_Az='digitalInput2description'
_Ay='digitalInput1description'
_Ax='voltage4hyst'
_Aw='voltage4min'
_Av='voltage4max'
_Au='voltage4description'
_At='voltage3hyst'
_As='voltage3min'
_Ar='voltage3max'
_Aq='voltage3description'
_Ap='voltage2hyst'
_Ao='voltage2min'
_An='voltage2max'
_Am='voltage2description'
_Al='voltage1hyst'
_Ak='voltage1min'
_Aj='voltage1max'
_Ai='voltage1description'
_Ah='s82HYSTx10Int'
_Ag='s82MINx10Int'
_Af='s82MAXx10Int'
_Ae='s81HYSTx10Int'
_Ad='s81MINx10Int'
_Ac='s81MAXx10Int'
_Ab='s8description'
_Aa='s72HYSTx10Int'
_AZ='s72MINx10Int'
_AY='s72MAXx10Int'
_AX='s71HYSTx10Int'
_AW='s71MINx10Int'
_AV='s71MAXx10Int'
_AU='s7description'
_AT='s62HYSTx10Int'
_AS='s62MINx10Int'
_AR='s62MAXx10Int'
_AQ='s61HYSTx10Int'
_AP='s61MINx10Int'
_AO='s61MAXx10Int'
_AN='s6description'
_AM='s52HYSTx10Int'
_AL='s52MINx10Int'
_AK='s52MAXx10Int'
_AJ='s51HYSTx10Int'
_AI='s51MINx10Int'
_AH='s51MAXx10Int'
_AG='s5description'
_AF='s42HYSTx10Int'
_AE='s42MINx10Int'
_AD='s42MAXx10Int'
_AC='s41HYSTx10Int'
_AB='s41MINx10Int'
_AA='s41MAXx10Int'
_A9='s4description'
_A8='s32HYSTx10Int'
_A7='s32MINx10Int'
_A6='s32MAXx10Int'
_A5='s31HYSTx10Int'
_A4='s31MINx10Int'
_A3='s31MAXx10Int'
_A2='s3description'
_A1='s22HYSTx10Int'
_A0='s22MINx10Int'
_z='s22MAXx10Int'
_y='s21HYSTx10Int'
_x='s21MINx10Int'
_w='s21MAXx10Int'
_v='s2description'
_u='s12HYSTx10Int'
_t='s12MINx10Int'
_s='s12MAXx10Int'
_r='s11HYSTx10Int'
_q='s11MINx10Int'
_p='s11MAXx10Int'
_o='s1description'
_n='deviceIP'
_m='hostName'
_l='deviceID'
_k='dateTime'
_j='version'
_i='restartDevice'
_h='digitalInput4State'
_g='digitalInput3State'
_f='digitalInput2State'
_e='digitalInput1State'
_d='voltage4x10Int'
_c='voltage3x10Int'
_b='voltage2x10Int'
_a='voltage1x10Int'
_Z='s82x10Int'
_Y='s81x10Int'
_X='s72x10Int'
_W='s71x10Int'
_V='s62x10Int'
_U='s61x10Int'
_T='s52x10Int'
_S='s51x10Int'
_R='s42x10Int'
_Q='s41x10Int'
_P='s32x10Int'
_O='s31x10Int'
_N='s22x10Int'
_M='s21x10Int'
_L='s12x10Int'
_K='s11x10Int'
_J='open'
_I='closed'
_H='on'
_G='off'
_F='Integer32'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='current'
_A='TERACOM-TCW240B-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','snmpModules')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','TextualConvention')
snmpMIB=ModuleIdentity((1,3,6,1,6,3,1))
if mibBuilder.loadTexts:snmpMIB.setRevisions(('2016-08-23 00:00',))
class CONTROLLED(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)));namedValues=NamedValues(*(('manual',0),('sensor11',1),('sensor21',2),('sensor31',3),('sensor41',4),('sensor51',5),('sensor61',6),('sensor71',7),('sensor81',8),('sensor12',9),('sensor22',10),('sensor32',11),('sensor42',12),('sensor52',13),('sensor62',14),('sensor72',15),('sensor82',16),('analog1',17),('analog2',18),('analog3',19),('analog4',20),('digital1',21),('digital2',22),('digital3',23),('digital4',24),('scheduler1',25),('scheduler2',26),('scheduler3',27),('scheduler4',28)))
_Teracom_ObjectIdentity=ObjectIdentity
teracom=_Teracom_ObjectIdentity((1,3,6,1,4,1,38783))
_Tcw240b_ObjectIdentity=ObjectIdentity
tcw240b=_Tcw240b_ObjectIdentity((1,3,6,1,4,1,38783,1))
_TrapNotifications_ObjectIdentity=ObjectIdentity
trapNotifications=_TrapNotifications_ObjectIdentity((1,3,6,1,4,1,38783,1,0))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,38783,1,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,38783,1,1,1),_Name_Type())
name.setMaxAccess(_D)
if mibBuilder.loadTexts:name.setStatus(_B)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,38783,1,1,2),_Version_Type())
version.setMaxAccess(_D)
if mibBuilder.loadTexts:version.setStatus(_B)
_DateTime_Type=DateAndTime
_DateTime_Object=MibScalar
dateTime=_DateTime_Object((1,3,6,1,4,1,38783,1,1,3),_DateTime_Type())
dateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dateTime.setStatus(_B)
_Setup_ObjectIdentity=ObjectIdentity
setup=_Setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2))
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,38783,1,2,1))
_DeviceID_Type=MacAddress
_DeviceID_Object=MibScalar
deviceID=_DeviceID_Object((1,3,6,1,4,1,38783,1,2,1,1),_DeviceID_Type())
deviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceID.setStatus(_B)
class _HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_HostName_Type.__name__=_E
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,38783,1,2,1,2),_HostName_Type())
hostName.setMaxAccess(_D)
if mibBuilder.loadTexts:hostName.setStatus(_B)
_DeviceIP_Type=IpAddress
_DeviceIP_Object=MibScalar
deviceIP=_DeviceIP_Object((1,3,6,1,4,1,38783,1,2,1,3),_DeviceIP_Type())
deviceIP.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceIP.setStatus(_B)
_Io_ObjectIdentity=ObjectIdentity
io=_Io_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2))
_SensorsSetup_ObjectIdentity=ObjectIdentity
sensorsSetup=_SensorsSetup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1))
_Sensor1setup_ObjectIdentity=ObjectIdentity
sensor1setup=_Sensor1setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,1))
class _S1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S1description_Type.__name__=_E
_S1description_Object=MibScalar
s1description=_S1description_Object((1,3,6,1,4,1,38783,1,2,2,1,1,1),_S1description_Type())
s1description.setMaxAccess(_C)
if mibBuilder.loadTexts:s1description.setStatus(_B)
_Sensor11setup_ObjectIdentity=ObjectIdentity
sensor11setup=_Sensor11setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,1,2))
_S11MAXx10Int_Type=Integer32
_S11MAXx10Int_Object=MibScalar
s11MAXx10Int=_S11MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,1,2,1),_S11MAXx10Int_Type())
s11MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s11MAXx10Int.setStatus(_B)
_S11MINx10Int_Type=Integer32
_S11MINx10Int_Object=MibScalar
s11MINx10Int=_S11MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,1,2,2),_S11MINx10Int_Type())
s11MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s11MINx10Int.setStatus(_B)
_S11HYSTx10Int_Type=Integer32
_S11HYSTx10Int_Object=MibScalar
s11HYSTx10Int=_S11HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,1,2,3),_S11HYSTx10Int_Type())
s11HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s11HYSTx10Int.setStatus(_B)
_Sensor12setup_ObjectIdentity=ObjectIdentity
sensor12setup=_Sensor12setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,1,3))
_S12MAXx10Int_Type=Integer32
_S12MAXx10Int_Object=MibScalar
s12MAXx10Int=_S12MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,1,3,1),_S12MAXx10Int_Type())
s12MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s12MAXx10Int.setStatus(_B)
_S12MINx10Int_Type=Integer32
_S12MINx10Int_Object=MibScalar
s12MINx10Int=_S12MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,1,3,2),_S12MINx10Int_Type())
s12MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s12MINx10Int.setStatus(_B)
_S12HYSTx10Int_Type=Integer32
_S12HYSTx10Int_Object=MibScalar
s12HYSTx10Int=_S12HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,1,3,3),_S12HYSTx10Int_Type())
s12HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s12HYSTx10Int.setStatus(_B)
_Sensor2setup_ObjectIdentity=ObjectIdentity
sensor2setup=_Sensor2setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,2))
class _S2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S2description_Type.__name__=_E
_S2description_Object=MibScalar
s2description=_S2description_Object((1,3,6,1,4,1,38783,1,2,2,1,2,1),_S2description_Type())
s2description.setMaxAccess(_C)
if mibBuilder.loadTexts:s2description.setStatus(_B)
_Sensor21setup_ObjectIdentity=ObjectIdentity
sensor21setup=_Sensor21setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,2,2))
_S21MAXx10Int_Type=Integer32
_S21MAXx10Int_Object=MibScalar
s21MAXx10Int=_S21MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,2,2,1),_S21MAXx10Int_Type())
s21MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s21MAXx10Int.setStatus(_B)
_S21MINx10Int_Type=Integer32
_S21MINx10Int_Object=MibScalar
s21MINx10Int=_S21MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,2,2,2),_S21MINx10Int_Type())
s21MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s21MINx10Int.setStatus(_B)
_S21HYSTx10Int_Type=Integer32
_S21HYSTx10Int_Object=MibScalar
s21HYSTx10Int=_S21HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,2,2,3),_S21HYSTx10Int_Type())
s21HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s21HYSTx10Int.setStatus(_B)
_Sensor22setup_ObjectIdentity=ObjectIdentity
sensor22setup=_Sensor22setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,2,3))
_S22MAXx10Int_Type=Integer32
_S22MAXx10Int_Object=MibScalar
s22MAXx10Int=_S22MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,2,3,1),_S22MAXx10Int_Type())
s22MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s22MAXx10Int.setStatus(_B)
_S22MINx10Int_Type=Integer32
_S22MINx10Int_Object=MibScalar
s22MINx10Int=_S22MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,2,3,2),_S22MINx10Int_Type())
s22MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s22MINx10Int.setStatus(_B)
_S22HYSTx10Int_Type=Integer32
_S22HYSTx10Int_Object=MibScalar
s22HYSTx10Int=_S22HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,2,3,3),_S22HYSTx10Int_Type())
s22HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s22HYSTx10Int.setStatus(_B)
_Sensor3setup_ObjectIdentity=ObjectIdentity
sensor3setup=_Sensor3setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,3))
class _S3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S3description_Type.__name__=_E
_S3description_Object=MibScalar
s3description=_S3description_Object((1,3,6,1,4,1,38783,1,2,2,1,3,1),_S3description_Type())
s3description.setMaxAccess(_C)
if mibBuilder.loadTexts:s3description.setStatus(_B)
_Sensor31setup_ObjectIdentity=ObjectIdentity
sensor31setup=_Sensor31setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,3,2))
_S31MAXx10Int_Type=Integer32
_S31MAXx10Int_Object=MibScalar
s31MAXx10Int=_S31MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,3,2,1),_S31MAXx10Int_Type())
s31MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s31MAXx10Int.setStatus(_B)
_S31MINx10Int_Type=Integer32
_S31MINx10Int_Object=MibScalar
s31MINx10Int=_S31MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,3,2,2),_S31MINx10Int_Type())
s31MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s31MINx10Int.setStatus(_B)
_S31HYSTx10Int_Type=Integer32
_S31HYSTx10Int_Object=MibScalar
s31HYSTx10Int=_S31HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,3,2,3),_S31HYSTx10Int_Type())
s31HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s31HYSTx10Int.setStatus(_B)
_Sensor32setup_ObjectIdentity=ObjectIdentity
sensor32setup=_Sensor32setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,3,3))
_S32MAXx10Int_Type=Integer32
_S32MAXx10Int_Object=MibScalar
s32MAXx10Int=_S32MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,3,3,1),_S32MAXx10Int_Type())
s32MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s32MAXx10Int.setStatus(_B)
_S32MINx10Int_Type=Integer32
_S32MINx10Int_Object=MibScalar
s32MINx10Int=_S32MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,3,3,2),_S32MINx10Int_Type())
s32MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s32MINx10Int.setStatus(_B)
_S32HYSTx10Int_Type=Integer32
_S32HYSTx10Int_Object=MibScalar
s32HYSTx10Int=_S32HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,3,3,3),_S32HYSTx10Int_Type())
s32HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s32HYSTx10Int.setStatus(_B)
_Sensor4setup_ObjectIdentity=ObjectIdentity
sensor4setup=_Sensor4setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,4))
class _S4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S4description_Type.__name__=_E
_S4description_Object=MibScalar
s4description=_S4description_Object((1,3,6,1,4,1,38783,1,2,2,1,4,1),_S4description_Type())
s4description.setMaxAccess(_C)
if mibBuilder.loadTexts:s4description.setStatus(_B)
_Sensor41setup_ObjectIdentity=ObjectIdentity
sensor41setup=_Sensor41setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,4,2))
_S41MAXx10Int_Type=Integer32
_S41MAXx10Int_Object=MibScalar
s41MAXx10Int=_S41MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,4,2,1),_S41MAXx10Int_Type())
s41MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s41MAXx10Int.setStatus(_B)
_S41MINx10Int_Type=Integer32
_S41MINx10Int_Object=MibScalar
s41MINx10Int=_S41MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,4,2,2),_S41MINx10Int_Type())
s41MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s41MINx10Int.setStatus(_B)
_S41HYSTx10Int_Type=Integer32
_S41HYSTx10Int_Object=MibScalar
s41HYSTx10Int=_S41HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,4,2,3),_S41HYSTx10Int_Type())
s41HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s41HYSTx10Int.setStatus(_B)
_Sensor42setup_ObjectIdentity=ObjectIdentity
sensor42setup=_Sensor42setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,4,3))
_S42MAXx10Int_Type=Integer32
_S42MAXx10Int_Object=MibScalar
s42MAXx10Int=_S42MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,4,3,1),_S42MAXx10Int_Type())
s42MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s42MAXx10Int.setStatus(_B)
_S42MINx10Int_Type=Integer32
_S42MINx10Int_Object=MibScalar
s42MINx10Int=_S42MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,4,3,2),_S42MINx10Int_Type())
s42MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s42MINx10Int.setStatus(_B)
_S42HYSTx10Int_Type=Integer32
_S42HYSTx10Int_Object=MibScalar
s42HYSTx10Int=_S42HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,4,3,3),_S42HYSTx10Int_Type())
s42HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s42HYSTx10Int.setStatus(_B)
_Sensor5setup_ObjectIdentity=ObjectIdentity
sensor5setup=_Sensor5setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,5))
class _S5description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S5description_Type.__name__=_E
_S5description_Object=MibScalar
s5description=_S5description_Object((1,3,6,1,4,1,38783,1,2,2,1,5,1),_S5description_Type())
s5description.setMaxAccess(_C)
if mibBuilder.loadTexts:s5description.setStatus(_B)
_Sensor51setup_ObjectIdentity=ObjectIdentity
sensor51setup=_Sensor51setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,5,2))
_S51MAXx10Int_Type=Integer32
_S51MAXx10Int_Object=MibScalar
s51MAXx10Int=_S51MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,5,2,1),_S51MAXx10Int_Type())
s51MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s51MAXx10Int.setStatus(_B)
_S51MINx10Int_Type=Integer32
_S51MINx10Int_Object=MibScalar
s51MINx10Int=_S51MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,5,2,2),_S51MINx10Int_Type())
s51MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s51MINx10Int.setStatus(_B)
_S51HYSTx10Int_Type=Integer32
_S51HYSTx10Int_Object=MibScalar
s51HYSTx10Int=_S51HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,5,2,3),_S51HYSTx10Int_Type())
s51HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s51HYSTx10Int.setStatus(_B)
_Sensor52setup_ObjectIdentity=ObjectIdentity
sensor52setup=_Sensor52setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,5,3))
_S52MAXx10Int_Type=Integer32
_S52MAXx10Int_Object=MibScalar
s52MAXx10Int=_S52MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,5,3,1),_S52MAXx10Int_Type())
s52MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s52MAXx10Int.setStatus(_B)
_S52MINx10Int_Type=Integer32
_S52MINx10Int_Object=MibScalar
s52MINx10Int=_S52MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,5,3,2),_S52MINx10Int_Type())
s52MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s52MINx10Int.setStatus(_B)
_S52HYSTx10Int_Type=Integer32
_S52HYSTx10Int_Object=MibScalar
s52HYSTx10Int=_S52HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,5,3,3),_S52HYSTx10Int_Type())
s52HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s52HYSTx10Int.setStatus(_B)
_Sensor6setup_ObjectIdentity=ObjectIdentity
sensor6setup=_Sensor6setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,6))
class _S6description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S6description_Type.__name__=_E
_S6description_Object=MibScalar
s6description=_S6description_Object((1,3,6,1,4,1,38783,1,2,2,1,6,1),_S6description_Type())
s6description.setMaxAccess(_C)
if mibBuilder.loadTexts:s6description.setStatus(_B)
_Sensor61setup_ObjectIdentity=ObjectIdentity
sensor61setup=_Sensor61setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,6,2))
_S61MAXx10Int_Type=Integer32
_S61MAXx10Int_Object=MibScalar
s61MAXx10Int=_S61MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,6,2,1),_S61MAXx10Int_Type())
s61MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s61MAXx10Int.setStatus(_B)
_S61MINx10Int_Type=Integer32
_S61MINx10Int_Object=MibScalar
s61MINx10Int=_S61MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,6,2,2),_S61MINx10Int_Type())
s61MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s61MINx10Int.setStatus(_B)
_S61HYSTx10Int_Type=Integer32
_S61HYSTx10Int_Object=MibScalar
s61HYSTx10Int=_S61HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,6,2,3),_S61HYSTx10Int_Type())
s61HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s61HYSTx10Int.setStatus(_B)
_Sensor62setup_ObjectIdentity=ObjectIdentity
sensor62setup=_Sensor62setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,6,3))
_S62MAXx10Int_Type=Integer32
_S62MAXx10Int_Object=MibScalar
s62MAXx10Int=_S62MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,6,3,1),_S62MAXx10Int_Type())
s62MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s62MAXx10Int.setStatus(_B)
_S62MINx10Int_Type=Integer32
_S62MINx10Int_Object=MibScalar
s62MINx10Int=_S62MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,6,3,2),_S62MINx10Int_Type())
s62MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s62MINx10Int.setStatus(_B)
_S62HYSTx10Int_Type=Integer32
_S62HYSTx10Int_Object=MibScalar
s62HYSTx10Int=_S62HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,6,3,3),_S62HYSTx10Int_Type())
s62HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s62HYSTx10Int.setStatus(_B)
_Sensor7setup_ObjectIdentity=ObjectIdentity
sensor7setup=_Sensor7setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,7))
class _S7description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S7description_Type.__name__=_E
_S7description_Object=MibScalar
s7description=_S7description_Object((1,3,6,1,4,1,38783,1,2,2,1,7,1),_S7description_Type())
s7description.setMaxAccess(_C)
if mibBuilder.loadTexts:s7description.setStatus(_B)
_Sensor71setup_ObjectIdentity=ObjectIdentity
sensor71setup=_Sensor71setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,7,2))
_S71MAXx10Int_Type=Integer32
_S71MAXx10Int_Object=MibScalar
s71MAXx10Int=_S71MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,7,2,1),_S71MAXx10Int_Type())
s71MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s71MAXx10Int.setStatus(_B)
_S71MINx10Int_Type=Integer32
_S71MINx10Int_Object=MibScalar
s71MINx10Int=_S71MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,7,2,2),_S71MINx10Int_Type())
s71MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s71MINx10Int.setStatus(_B)
_S71HYSTx10Int_Type=Integer32
_S71HYSTx10Int_Object=MibScalar
s71HYSTx10Int=_S71HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,7,2,3),_S71HYSTx10Int_Type())
s71HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s71HYSTx10Int.setStatus(_B)
_Sensor72setup_ObjectIdentity=ObjectIdentity
sensor72setup=_Sensor72setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,7,3))
_S72MAXx10Int_Type=Integer32
_S72MAXx10Int_Object=MibScalar
s72MAXx10Int=_S72MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,7,3,1),_S72MAXx10Int_Type())
s72MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s72MAXx10Int.setStatus(_B)
_S72MINx10Int_Type=Integer32
_S72MINx10Int_Object=MibScalar
s72MINx10Int=_S72MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,7,3,2),_S72MINx10Int_Type())
s72MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s72MINx10Int.setStatus(_B)
_S72HYSTx10Int_Type=Integer32
_S72HYSTx10Int_Object=MibScalar
s72HYSTx10Int=_S72HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,7,3,3),_S72HYSTx10Int_Type())
s72HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s72HYSTx10Int.setStatus(_B)
_Sensor8setup_ObjectIdentity=ObjectIdentity
sensor8setup=_Sensor8setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,8))
class _S8description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_S8description_Type.__name__=_E
_S8description_Object=MibScalar
s8description=_S8description_Object((1,3,6,1,4,1,38783,1,2,2,1,8,1),_S8description_Type())
s8description.setMaxAccess(_C)
if mibBuilder.loadTexts:s8description.setStatus(_B)
_Sensor81setup_ObjectIdentity=ObjectIdentity
sensor81setup=_Sensor81setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,8,2))
_S81MAXx10Int_Type=Integer32
_S81MAXx10Int_Object=MibScalar
s81MAXx10Int=_S81MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,8,2,1),_S81MAXx10Int_Type())
s81MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s81MAXx10Int.setStatus(_B)
_S81MINx10Int_Type=Integer32
_S81MINx10Int_Object=MibScalar
s81MINx10Int=_S81MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,8,2,2),_S81MINx10Int_Type())
s81MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s81MINx10Int.setStatus(_B)
_S81HYSTx10Int_Type=Integer32
_S81HYSTx10Int_Object=MibScalar
s81HYSTx10Int=_S81HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,8,2,3),_S81HYSTx10Int_Type())
s81HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s81HYSTx10Int.setStatus(_B)
_Sensor82setup_ObjectIdentity=ObjectIdentity
sensor82setup=_Sensor82setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,1,8,3))
_S82MAXx10Int_Type=Integer32
_S82MAXx10Int_Object=MibScalar
s82MAXx10Int=_S82MAXx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,8,3,1),_S82MAXx10Int_Type())
s82MAXx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s82MAXx10Int.setStatus(_B)
_S82MINx10Int_Type=Integer32
_S82MINx10Int_Object=MibScalar
s82MINx10Int=_S82MINx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,8,3,2),_S82MINx10Int_Type())
s82MINx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s82MINx10Int.setStatus(_B)
_S82HYSTx10Int_Type=Integer32
_S82HYSTx10Int_Object=MibScalar
s82HYSTx10Int=_S82HYSTx10Int_Object((1,3,6,1,4,1,38783,1,2,2,1,8,3,3),_S82HYSTx10Int_Type())
s82HYSTx10Int.setMaxAccess(_C)
if mibBuilder.loadTexts:s82HYSTx10Int.setStatus(_B)
_AnalogSetup_ObjectIdentity=ObjectIdentity
analogSetup=_AnalogSetup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,2))
_Analog1setup_ObjectIdentity=ObjectIdentity
analog1setup=_Analog1setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,2,1))
class _Voltage1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage1description_Type.__name__=_E
_Voltage1description_Object=MibScalar
voltage1description=_Voltage1description_Object((1,3,6,1,4,1,38783,1,2,2,2,1,1),_Voltage1description_Type())
voltage1description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1description.setStatus(_B)
_Voltage1max_Type=Integer32
_Voltage1max_Object=MibScalar
voltage1max=_Voltage1max_Object((1,3,6,1,4,1,38783,1,2,2,2,1,2),_Voltage1max_Type())
voltage1max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1max.setStatus(_B)
_Voltage1min_Type=Integer32
_Voltage1min_Object=MibScalar
voltage1min=_Voltage1min_Object((1,3,6,1,4,1,38783,1,2,2,2,1,3),_Voltage1min_Type())
voltage1min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1min.setStatus(_B)
_Voltage1hyst_Type=Integer32
_Voltage1hyst_Object=MibScalar
voltage1hyst=_Voltage1hyst_Object((1,3,6,1,4,1,38783,1,2,2,2,1,4),_Voltage1hyst_Type())
voltage1hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage1hyst.setStatus(_B)
_Analog2setup_ObjectIdentity=ObjectIdentity
analog2setup=_Analog2setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,2,2))
class _Voltage2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage2description_Type.__name__=_E
_Voltage2description_Object=MibScalar
voltage2description=_Voltage2description_Object((1,3,6,1,4,1,38783,1,2,2,2,2,1),_Voltage2description_Type())
voltage2description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2description.setStatus(_B)
_Voltage2max_Type=Integer32
_Voltage2max_Object=MibScalar
voltage2max=_Voltage2max_Object((1,3,6,1,4,1,38783,1,2,2,2,2,2),_Voltage2max_Type())
voltage2max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2max.setStatus(_B)
_Voltage2min_Type=Integer32
_Voltage2min_Object=MibScalar
voltage2min=_Voltage2min_Object((1,3,6,1,4,1,38783,1,2,2,2,2,3),_Voltage2min_Type())
voltage2min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2min.setStatus(_B)
_Voltage2hyst_Type=Integer32
_Voltage2hyst_Object=MibScalar
voltage2hyst=_Voltage2hyst_Object((1,3,6,1,4,1,38783,1,2,2,2,2,4),_Voltage2hyst_Type())
voltage2hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage2hyst.setStatus(_B)
_Analog3setup_ObjectIdentity=ObjectIdentity
analog3setup=_Analog3setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,2,3))
class _Voltage3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage3description_Type.__name__=_E
_Voltage3description_Object=MibScalar
voltage3description=_Voltage3description_Object((1,3,6,1,4,1,38783,1,2,2,2,3,1),_Voltage3description_Type())
voltage3description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3description.setStatus(_B)
_Voltage3max_Type=Integer32
_Voltage3max_Object=MibScalar
voltage3max=_Voltage3max_Object((1,3,6,1,4,1,38783,1,2,2,2,3,2),_Voltage3max_Type())
voltage3max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3max.setStatus(_B)
_Voltage3min_Type=Integer32
_Voltage3min_Object=MibScalar
voltage3min=_Voltage3min_Object((1,3,6,1,4,1,38783,1,2,2,2,3,3),_Voltage3min_Type())
voltage3min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3min.setStatus(_B)
_Voltage3hyst_Type=Integer32
_Voltage3hyst_Object=MibScalar
voltage3hyst=_Voltage3hyst_Object((1,3,6,1,4,1,38783,1,2,2,2,3,4),_Voltage3hyst_Type())
voltage3hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage3hyst.setStatus(_B)
_Analog4setup_ObjectIdentity=ObjectIdentity
analog4setup=_Analog4setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,2,4))
class _Voltage4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Voltage4description_Type.__name__=_E
_Voltage4description_Object=MibScalar
voltage4description=_Voltage4description_Object((1,3,6,1,4,1,38783,1,2,2,2,4,1),_Voltage4description_Type())
voltage4description.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4description.setStatus(_B)
_Voltage4max_Type=Integer32
_Voltage4max_Object=MibScalar
voltage4max=_Voltage4max_Object((1,3,6,1,4,1,38783,1,2,2,2,4,2),_Voltage4max_Type())
voltage4max.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4max.setStatus(_B)
_Voltage4min_Type=Integer32
_Voltage4min_Object=MibScalar
voltage4min=_Voltage4min_Object((1,3,6,1,4,1,38783,1,2,2,2,4,3),_Voltage4min_Type())
voltage4min.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4min.setStatus(_B)
_Voltage4hyst_Type=Integer32
_Voltage4hyst_Object=MibScalar
voltage4hyst=_Voltage4hyst_Object((1,3,6,1,4,1,38783,1,2,2,2,4,4),_Voltage4hyst_Type())
voltage4hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:voltage4hyst.setStatus(_B)
_DigitalSetup_ObjectIdentity=ObjectIdentity
digitalSetup=_DigitalSetup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,3))
class _DigitalInput1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput1description_Type.__name__=_E
_DigitalInput1description_Object=MibScalar
digitalInput1description=_DigitalInput1description_Object((1,3,6,1,4,1,38783,1,2,2,3,1),_DigitalInput1description_Type())
digitalInput1description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput1description.setStatus(_B)
class _DigitalInput2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput2description_Type.__name__=_E
_DigitalInput2description_Object=MibScalar
digitalInput2description=_DigitalInput2description_Object((1,3,6,1,4,1,38783,1,2,2,3,2),_DigitalInput2description_Type())
digitalInput2description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput2description.setStatus(_B)
class _DigitalInput3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput3description_Type.__name__=_E
_DigitalInput3description_Object=MibScalar
digitalInput3description=_DigitalInput3description_Object((1,3,6,1,4,1,38783,1,2,2,3,3),_DigitalInput3description_Type())
digitalInput3description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput3description.setStatus(_B)
class _DigitalInput4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_DigitalInput4description_Type.__name__=_E
_DigitalInput4description_Object=MibScalar
digitalInput4description=_DigitalInput4description_Object((1,3,6,1,4,1,38783,1,2,2,3,4),_DigitalInput4description_Type())
digitalInput4description.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInput4description.setStatus(_B)
_RelaysSetup_ObjectIdentity=ObjectIdentity
relaysSetup=_RelaysSetup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,4))
_Relay1setup_ObjectIdentity=ObjectIdentity
relay1setup=_Relay1setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,4,1))
class _Relay1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay1description_Type.__name__=_E
_Relay1description_Object=MibScalar
relay1description=_Relay1description_Object((1,3,6,1,4,1,38783,1,2,2,4,1,1),_Relay1description_Type())
relay1description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1description.setStatus(_B)
class _Relay1pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay1pulseWidth_Type.__name__=_F
_Relay1pulseWidth_Object=MibScalar
relay1pulseWidth=_Relay1pulseWidth_Object((1,3,6,1,4,1,38783,1,2,2,4,1,2),_Relay1pulseWidth_Type())
relay1pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1pulseWidth.setStatus(_B)
_Relay1controlledBy_Type=CONTROLLED
_Relay1controlledBy_Object=MibScalar
relay1controlledBy=_Relay1controlledBy_Object((1,3,6,1,4,1,38783,1,2,2,4,1,3),_Relay1controlledBy_Type())
relay1controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1controlledBy.setStatus(_B)
_Relay2setup_ObjectIdentity=ObjectIdentity
relay2setup=_Relay2setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,4,2))
class _Relay2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay2description_Type.__name__=_E
_Relay2description_Object=MibScalar
relay2description=_Relay2description_Object((1,3,6,1,4,1,38783,1,2,2,4,2,1),_Relay2description_Type())
relay2description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2description.setStatus(_B)
class _Relay2pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay2pulseWidth_Type.__name__=_F
_Relay2pulseWidth_Object=MibScalar
relay2pulseWidth=_Relay2pulseWidth_Object((1,3,6,1,4,1,38783,1,2,2,4,2,2),_Relay2pulseWidth_Type())
relay2pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2pulseWidth.setStatus(_B)
_Relay2controlledBy_Type=CONTROLLED
_Relay2controlledBy_Object=MibScalar
relay2controlledBy=_Relay2controlledBy_Object((1,3,6,1,4,1,38783,1,2,2,4,2,3),_Relay2controlledBy_Type())
relay2controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2controlledBy.setStatus(_B)
_Relay3setup_ObjectIdentity=ObjectIdentity
relay3setup=_Relay3setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,4,3))
class _Relay3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay3description_Type.__name__=_E
_Relay3description_Object=MibScalar
relay3description=_Relay3description_Object((1,3,6,1,4,1,38783,1,2,2,4,3,1),_Relay3description_Type())
relay3description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3description.setStatus(_B)
class _Relay3pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay3pulseWidth_Type.__name__=_F
_Relay3pulseWidth_Object=MibScalar
relay3pulseWidth=_Relay3pulseWidth_Object((1,3,6,1,4,1,38783,1,2,2,4,3,2),_Relay3pulseWidth_Type())
relay3pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3pulseWidth.setStatus(_B)
_Relay3controlledBy_Type=CONTROLLED
_Relay3controlledBy_Object=MibScalar
relay3controlledBy=_Relay3controlledBy_Object((1,3,6,1,4,1,38783,1,2,2,4,3,3),_Relay3controlledBy_Type())
relay3controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3controlledBy.setStatus(_B)
_Relay4setup_ObjectIdentity=ObjectIdentity
relay4setup=_Relay4setup_ObjectIdentity((1,3,6,1,4,1,38783,1,2,2,4,4))
class _Relay4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_Relay4description_Type.__name__=_E
_Relay4description_Object=MibScalar
relay4description=_Relay4description_Object((1,3,6,1,4,1,38783,1,2,2,4,4,1),_Relay4description_Type())
relay4description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4description.setStatus(_B)
class _Relay4pulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Relay4pulseWidth_Type.__name__=_F
_Relay4pulseWidth_Object=MibScalar
relay4pulseWidth=_Relay4pulseWidth_Object((1,3,6,1,4,1,38783,1,2,2,4,4,2),_Relay4pulseWidth_Type())
relay4pulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4pulseWidth.setStatus(_B)
_Relay4controlledBy_Type=CONTROLLED
_Relay4controlledBy_Object=MibScalar
relay4controlledBy=_Relay4controlledBy_Object((1,3,6,1,4,1,38783,1,2,2,4,4,3),_Relay4controlledBy_Type())
relay4controlledBy.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4controlledBy.setStatus(_B)
_MonitorNcontrol_ObjectIdentity=ObjectIdentity
monitorNcontrol=_MonitorNcontrol_ObjectIdentity((1,3,6,1,4,1,38783,1,3))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1))
_Sensor1_ObjectIdentity=ObjectIdentity
sensor1=_Sensor1_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,1))
_S11x10Int_Type=Integer32
_S11x10Int_Object=MibScalar
s11x10Int=_S11x10Int_Object((1,3,6,1,4,1,38783,1,3,1,1,1),_S11x10Int_Type())
s11x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s11x10Int.setStatus(_B)
_S12x10Int_Type=Integer32
_S12x10Int_Object=MibScalar
s12x10Int=_S12x10Int_Object((1,3,6,1,4,1,38783,1,3,1,1,2),_S12x10Int_Type())
s12x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s12x10Int.setStatus(_B)
_S1ID_Type=MacAddress
_S1ID_Object=MibScalar
s1ID=_S1ID_Object((1,3,6,1,4,1,38783,1,3,1,1,3),_S1ID_Type())
s1ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s1ID.setStatus(_B)
_Sensor2_ObjectIdentity=ObjectIdentity
sensor2=_Sensor2_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,2))
_S21x10Int_Type=Integer32
_S21x10Int_Object=MibScalar
s21x10Int=_S21x10Int_Object((1,3,6,1,4,1,38783,1,3,1,2,1),_S21x10Int_Type())
s21x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s21x10Int.setStatus(_B)
_S22x10Int_Type=Integer32
_S22x10Int_Object=MibScalar
s22x10Int=_S22x10Int_Object((1,3,6,1,4,1,38783,1,3,1,2,2),_S22x10Int_Type())
s22x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s22x10Int.setStatus(_B)
_S2ID_Type=MacAddress
_S2ID_Object=MibScalar
s2ID=_S2ID_Object((1,3,6,1,4,1,38783,1,3,1,2,3),_S2ID_Type())
s2ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s2ID.setStatus(_B)
_Sensor3_ObjectIdentity=ObjectIdentity
sensor3=_Sensor3_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,3))
_S31x10Int_Type=Integer32
_S31x10Int_Object=MibScalar
s31x10Int=_S31x10Int_Object((1,3,6,1,4,1,38783,1,3,1,3,1),_S31x10Int_Type())
s31x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s31x10Int.setStatus(_B)
_S32x10Int_Type=Integer32
_S32x10Int_Object=MibScalar
s32x10Int=_S32x10Int_Object((1,3,6,1,4,1,38783,1,3,1,3,2),_S32x10Int_Type())
s32x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s32x10Int.setStatus(_B)
_S3ID_Type=MacAddress
_S3ID_Object=MibScalar
s3ID=_S3ID_Object((1,3,6,1,4,1,38783,1,3,1,3,3),_S3ID_Type())
s3ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s3ID.setStatus(_B)
_Sensor4_ObjectIdentity=ObjectIdentity
sensor4=_Sensor4_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,4))
_S41x10Int_Type=Integer32
_S41x10Int_Object=MibScalar
s41x10Int=_S41x10Int_Object((1,3,6,1,4,1,38783,1,3,1,4,1),_S41x10Int_Type())
s41x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s41x10Int.setStatus(_B)
_S42x10Int_Type=Integer32
_S42x10Int_Object=MibScalar
s42x10Int=_S42x10Int_Object((1,3,6,1,4,1,38783,1,3,1,4,2),_S42x10Int_Type())
s42x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s42x10Int.setStatus(_B)
_S4ID_Type=MacAddress
_S4ID_Object=MibScalar
s4ID=_S4ID_Object((1,3,6,1,4,1,38783,1,3,1,4,3),_S4ID_Type())
s4ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s4ID.setStatus(_B)
_Sensor5_ObjectIdentity=ObjectIdentity
sensor5=_Sensor5_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,5))
_S51x10Int_Type=Integer32
_S51x10Int_Object=MibScalar
s51x10Int=_S51x10Int_Object((1,3,6,1,4,1,38783,1,3,1,5,1),_S51x10Int_Type())
s51x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s51x10Int.setStatus(_B)
_S52x10Int_Type=Integer32
_S52x10Int_Object=MibScalar
s52x10Int=_S52x10Int_Object((1,3,6,1,4,1,38783,1,3,1,5,2),_S52x10Int_Type())
s52x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s52x10Int.setStatus(_B)
_S5ID_Type=MacAddress
_S5ID_Object=MibScalar
s5ID=_S5ID_Object((1,3,6,1,4,1,38783,1,3,1,5,3),_S5ID_Type())
s5ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s5ID.setStatus(_B)
_Sensor6_ObjectIdentity=ObjectIdentity
sensor6=_Sensor6_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,6))
_S61x10Int_Type=Integer32
_S61x10Int_Object=MibScalar
s61x10Int=_S61x10Int_Object((1,3,6,1,4,1,38783,1,3,1,6,1),_S61x10Int_Type())
s61x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s61x10Int.setStatus(_B)
_S62x10Int_Type=Integer32
_S62x10Int_Object=MibScalar
s62x10Int=_S62x10Int_Object((1,3,6,1,4,1,38783,1,3,1,6,2),_S62x10Int_Type())
s62x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s62x10Int.setStatus(_B)
_S6ID_Type=MacAddress
_S6ID_Object=MibScalar
s6ID=_S6ID_Object((1,3,6,1,4,1,38783,1,3,1,6,3),_S6ID_Type())
s6ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s6ID.setStatus(_B)
_Sensor7_ObjectIdentity=ObjectIdentity
sensor7=_Sensor7_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,7))
_S71x10Int_Type=Integer32
_S71x10Int_Object=MibScalar
s71x10Int=_S71x10Int_Object((1,3,6,1,4,1,38783,1,3,1,7,1),_S71x10Int_Type())
s71x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s71x10Int.setStatus(_B)
_S72x10Int_Type=Integer32
_S72x10Int_Object=MibScalar
s72x10Int=_S72x10Int_Object((1,3,6,1,4,1,38783,1,3,1,7,2),_S72x10Int_Type())
s72x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s72x10Int.setStatus(_B)
_S7ID_Type=MacAddress
_S7ID_Object=MibScalar
s7ID=_S7ID_Object((1,3,6,1,4,1,38783,1,3,1,7,3),_S7ID_Type())
s7ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s7ID.setStatus(_B)
_Sensor8_ObjectIdentity=ObjectIdentity
sensor8=_Sensor8_ObjectIdentity((1,3,6,1,4,1,38783,1,3,1,8))
_S81x10Int_Type=Integer32
_S81x10Int_Object=MibScalar
s81x10Int=_S81x10Int_Object((1,3,6,1,4,1,38783,1,3,1,8,1),_S81x10Int_Type())
s81x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s81x10Int.setStatus(_B)
_S82x10Int_Type=Integer32
_S82x10Int_Object=MibScalar
s82x10Int=_S82x10Int_Object((1,3,6,1,4,1,38783,1,3,1,8,2),_S82x10Int_Type())
s82x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:s82x10Int.setStatus(_B)
_S8ID_Type=MacAddress
_S8ID_Object=MibScalar
s8ID=_S8ID_Object((1,3,6,1,4,1,38783,1,3,1,8,3),_S8ID_Type())
s8ID.setMaxAccess(_D)
if mibBuilder.loadTexts:s8ID.setStatus(_B)
_Analog_ObjectIdentity=ObjectIdentity
analog=_Analog_ObjectIdentity((1,3,6,1,4,1,38783,1,3,2))
_Voltage1x10Int_Type=Integer32
_Voltage1x10Int_Object=MibScalar
voltage1x10Int=_Voltage1x10Int_Object((1,3,6,1,4,1,38783,1,3,2,1),_Voltage1x10Int_Type())
voltage1x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage1x10Int.setStatus(_B)
_Voltage2x10Int_Type=Integer32
_Voltage2x10Int_Object=MibScalar
voltage2x10Int=_Voltage2x10Int_Object((1,3,6,1,4,1,38783,1,3,2,2),_Voltage2x10Int_Type())
voltage2x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage2x10Int.setStatus(_B)
_Voltage3x10Int_Type=Integer32
_Voltage3x10Int_Object=MibScalar
voltage3x10Int=_Voltage3x10Int_Object((1,3,6,1,4,1,38783,1,3,2,3),_Voltage3x10Int_Type())
voltage3x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage3x10Int.setStatus(_B)
_Voltage4x10Int_Type=Integer32
_Voltage4x10Int_Object=MibScalar
voltage4x10Int=_Voltage4x10Int_Object((1,3,6,1,4,1,38783,1,3,2,4),_Voltage4x10Int_Type())
voltage4x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage4x10Int.setStatus(_B)
_Voltage1x100Int_Type=Integer32
_Voltage1x100Int_Object=MibScalar
voltage1x100Int=_Voltage1x100Int_Object((1,3,6,1,4,1,38783,1,3,2,5),_Voltage1x100Int_Type())
voltage1x100Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage1x100Int.setStatus(_B)
_Voltage2x100Int_Type=Integer32
_Voltage2x100Int_Object=MibScalar
voltage2x100Int=_Voltage2x100Int_Object((1,3,6,1,4,1,38783,1,3,2,6),_Voltage2x100Int_Type())
voltage2x100Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage2x100Int.setStatus(_B)
_Voltage3x100Int_Type=Integer32
_Voltage3x100Int_Object=MibScalar
voltage3x100Int=_Voltage3x100Int_Object((1,3,6,1,4,1,38783,1,3,2,7),_Voltage3x100Int_Type())
voltage3x100Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage3x100Int.setStatus(_B)
_Voltage4x100Int_Type=Integer32
_Voltage4x100Int_Object=MibScalar
voltage4x100Int=_Voltage4x100Int_Object((1,3,6,1,4,1,38783,1,3,2,8),_Voltage4x100Int_Type())
voltage4x100Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage4x100Int.setStatus(_B)
_Digital_ObjectIdentity=ObjectIdentity
digital=_Digital_ObjectIdentity((1,3,6,1,4,1,38783,1,3,3))
class _DigitalInput1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput1State_Type.__name__=_F
_DigitalInput1State_Object=MibScalar
digitalInput1State=_DigitalInput1State_Object((1,3,6,1,4,1,38783,1,3,3,1),_DigitalInput1State_Type())
digitalInput1State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput1State.setStatus(_B)
class _DigitalInput2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput2State_Type.__name__=_F
_DigitalInput2State_Object=MibScalar
digitalInput2State=_DigitalInput2State_Object((1,3,6,1,4,1,38783,1,3,3,2),_DigitalInput2State_Type())
digitalInput2State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput2State.setStatus(_B)
class _DigitalInput3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput3State_Type.__name__=_F
_DigitalInput3State_Object=MibScalar
digitalInput3State=_DigitalInput3State_Object((1,3,6,1,4,1,38783,1,3,3,3),_DigitalInput3State_Type())
digitalInput3State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput3State.setStatus(_B)
class _DigitalInput4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DigitalInput4State_Type.__name__=_F
_DigitalInput4State_Object=MibScalar
digitalInput4State=_DigitalInput4State_Object((1,3,6,1,4,1,38783,1,3,3,4),_DigitalInput4State_Type())
digitalInput4State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput4State.setStatus(_B)
_Relays_ObjectIdentity=ObjectIdentity
relays=_Relays_ObjectIdentity((1,3,6,1,4,1,38783,1,3,4))
_Relay1_ObjectIdentity=ObjectIdentity
relay1=_Relay1_ObjectIdentity((1,3,6,1,4,1,38783,1,3,4,1))
class _Relay1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay1State_Type.__name__=_F
_Relay1State_Object=MibScalar
relay1State=_Relay1State_Object((1,3,6,1,4,1,38783,1,3,4,1,1),_Relay1State_Type())
relay1State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1State.setStatus(_B)
class _Relay1Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay1Pulse_Type.__name__=_F
_Relay1Pulse_Object=MibScalar
relay1Pulse=_Relay1Pulse_Object((1,3,6,1,4,1,38783,1,3,4,1,2),_Relay1Pulse_Type())
relay1Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1Pulse.setStatus(_B)
_Relay2_ObjectIdentity=ObjectIdentity
relay2=_Relay2_ObjectIdentity((1,3,6,1,4,1,38783,1,3,4,2))
class _Relay2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay2State_Type.__name__=_F
_Relay2State_Object=MibScalar
relay2State=_Relay2State_Object((1,3,6,1,4,1,38783,1,3,4,2,1),_Relay2State_Type())
relay2State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2State.setStatus(_B)
class _Relay2Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay2Pulse_Type.__name__=_F
_Relay2Pulse_Object=MibScalar
relay2Pulse=_Relay2Pulse_Object((1,3,6,1,4,1,38783,1,3,4,2,2),_Relay2Pulse_Type())
relay2Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2Pulse.setStatus(_B)
_Relay3_ObjectIdentity=ObjectIdentity
relay3=_Relay3_ObjectIdentity((1,3,6,1,4,1,38783,1,3,4,3))
class _Relay3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay3State_Type.__name__=_F
_Relay3State_Object=MibScalar
relay3State=_Relay3State_Object((1,3,6,1,4,1,38783,1,3,4,3,1),_Relay3State_Type())
relay3State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3State.setStatus(_B)
class _Relay3Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay3Pulse_Type.__name__=_F
_Relay3Pulse_Object=MibScalar
relay3Pulse=_Relay3Pulse_Object((1,3,6,1,4,1,38783,1,3,4,3,2),_Relay3Pulse_Type())
relay3Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3Pulse.setStatus(_B)
_Relay4_ObjectIdentity=ObjectIdentity
relay4=_Relay4_ObjectIdentity((1,3,6,1,4,1,38783,1,3,4,4))
class _Relay4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay4State_Type.__name__=_F
_Relay4State_Object=MibScalar
relay4State=_Relay4State_Object((1,3,6,1,4,1,38783,1,3,4,4,1),_Relay4State_Type())
relay4State.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4State.setStatus(_B)
class _Relay4Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_Relay4Pulse_Type.__name__=_F
_Relay4Pulse_Object=MibScalar
relay4Pulse=_Relay4Pulse_Object((1,3,6,1,4,1,38783,1,3,4,4,2),_Relay4Pulse_Type())
relay4Pulse.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4Pulse.setStatus(_B)
class _ConfigurationSaved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsaved',0),('saved',1)))
_ConfigurationSaved_Type.__name__=_F
_ConfigurationSaved_Object=MibScalar
configurationSaved=_ConfigurationSaved_Object((1,3,6,1,4,1,38783,1,3,5),_ConfigurationSaved_Type())
configurationSaved.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationSaved.setStatus(_B)
class _RestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cancel',0),('restart',1)))
_RestartDevice_Type.__name__=_F
_RestartDevice_Object=MibScalar
restartDevice=_RestartDevice_Object((1,3,6,1,4,1,38783,1,3,6),_RestartDevice_Type())
restartDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:restartDevice.setStatus(_B)
class _TemperatureUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('celcius',0),('fahrenheit',1)))
_TemperatureUnit_Type.__name__=_F
_TemperatureUnit_Object=MibScalar
temperatureUnit=_TemperatureUnit_Object((1,3,6,1,4,1,38783,1,3,7),_TemperatureUnit_Type())
temperatureUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureUnit.setStatus(_B)
class _HardwareErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noErr',0),('owErr',1),('hwErr',2)))
_HardwareErr_Type.__name__=_F
_HardwareErr_Object=MibScalar
hardwareErr=_HardwareErr_Object((1,3,6,1,4,1,38783,1,3,8),_HardwareErr_Type())
hardwareErr.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwareErr.setStatus(_B)
_Tcw240bMIBConformance_ObjectIdentity=ObjectIdentity
tcw240bMIBConformance=_Tcw240bMIBConformance_ObjectIdentity((1,3,6,1,4,1,38783,1,4))
_Tcw240bMIBCompliances_ObjectIdentity=ObjectIdentity
tcw240bMIBCompliances=_Tcw240bMIBCompliances_ObjectIdentity((1,3,6,1,4,1,38783,1,4,1))
_Tcw240bMIBGroups_ObjectIdentity=ObjectIdentity
tcw240bMIBGroups=_Tcw240bMIBGroups_ObjectIdentity((1,3,6,1,4,1,38783,1,4,2))
tcw240bProductGroup=ObjectGroup((1,3,6,1,4,1,38783,1,4,2,1))
tcw240bProductGroup.setObjects(*((_A,'name'),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:tcw240bProductGroup.setStatus(_B)
tcw240bSetupGroup=ObjectGroup((1,3,6,1,4,1,38783,1,4,2,2))
tcw240bSetupGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC)))
if mibBuilder.loadTexts:tcw240bSetupGroup.setStatus(_B)
tcw240bMonitorGroup=ObjectGroup((1,3,6,1,4,1,38783,1,4,2,3))
tcw240bMonitorGroup.setObjects(*((_A,_K),(_A,_L),(_A,'s1ID'),(_A,_M),(_A,_N),(_A,'s2ID'),(_A,_O),(_A,_P),(_A,'s3ID'),(_A,_Q),(_A,_R),(_A,'s4ID'),(_A,_S),(_A,_T),(_A,'s5ID'),(_A,_U),(_A,_V),(_A,'s6ID'),(_A,_W),(_A,_X),(_A,'s7ID'),(_A,_Y),(_A,_Z),(_A,'s8ID'),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_i),(_A,_BQ),(_A,_BR)))
if mibBuilder.loadTexts:tcw240bMonitorGroup.setStatus(_B)
snmp_trap_notification=NotificationType((1,3,6,1,4,1,38783,1,0,1))
snmp_trap_notification.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_i)))
if mibBuilder.loadTexts:snmp_trap_notification.setStatus(_B)
tcw240bTrapGroup=NotificationGroup((1,3,6,1,4,1,38783,1,4,2,4))
tcw240bTrapGroup.setObjects((_A,_BS))
if mibBuilder.loadTexts:tcw240bTrapGroup.setStatus(_B)
tcw240bMIBCompliances1=ModuleCompliance((1,3,6,1,4,1,38783,1,4,1,1))
tcw240bMIBCompliances1.setObjects(*((_A,_BT),(_A,_BU),(_A,_BV),(_A,_BW)))
if mibBuilder.loadTexts:tcw240bMIBCompliances1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CONTROLLED':CONTROLLED,'teracom':teracom,'tcw240b':tcw240b,'trapNotifications':trapNotifications,_BS:snmp_trap_notification,'product':product,'name':name,_j:version,_k:dateTime,'setup':setup,'network':network,_l:deviceID,_m:hostName,_n:deviceIP,'io':io,'sensorsSetup':sensorsSetup,'sensor1setup':sensor1setup,_o:s1description,'sensor11setup':sensor11setup,_p:s11MAXx10Int,_q:s11MINx10Int,_r:s11HYSTx10Int,'sensor12setup':sensor12setup,_s:s12MAXx10Int,_t:s12MINx10Int,_u:s12HYSTx10Int,'sensor2setup':sensor2setup,_v:s2description,'sensor21setup':sensor21setup,_w:s21MAXx10Int,_x:s21MINx10Int,_y:s21HYSTx10Int,'sensor22setup':sensor22setup,_z:s22MAXx10Int,_A0:s22MINx10Int,_A1:s22HYSTx10Int,'sensor3setup':sensor3setup,_A2:s3description,'sensor31setup':sensor31setup,_A3:s31MAXx10Int,_A4:s31MINx10Int,_A5:s31HYSTx10Int,'sensor32setup':sensor32setup,_A6:s32MAXx10Int,_A7:s32MINx10Int,_A8:s32HYSTx10Int,'sensor4setup':sensor4setup,_A9:s4description,'sensor41setup':sensor41setup,_AA:s41MAXx10Int,_AB:s41MINx10Int,_AC:s41HYSTx10Int,'sensor42setup':sensor42setup,_AD:s42MAXx10Int,_AE:s42MINx10Int,_AF:s42HYSTx10Int,'sensor5setup':sensor5setup,_AG:s5description,'sensor51setup':sensor51setup,_AH:s51MAXx10Int,_AI:s51MINx10Int,_AJ:s51HYSTx10Int,'sensor52setup':sensor52setup,_AK:s52MAXx10Int,_AL:s52MINx10Int,_AM:s52HYSTx10Int,'sensor6setup':sensor6setup,_AN:s6description,'sensor61setup':sensor61setup,_AO:s61MAXx10Int,_AP:s61MINx10Int,_AQ:s61HYSTx10Int,'sensor62setup':sensor62setup,_AR:s62MAXx10Int,_AS:s62MINx10Int,_AT:s62HYSTx10Int,'sensor7setup':sensor7setup,_AU:s7description,'sensor71setup':sensor71setup,_AV:s71MAXx10Int,_AW:s71MINx10Int,_AX:s71HYSTx10Int,'sensor72setup':sensor72setup,_AY:s72MAXx10Int,_AZ:s72MINx10Int,_Aa:s72HYSTx10Int,'sensor8setup':sensor8setup,_Ab:s8description,'sensor81setup':sensor81setup,_Ac:s81MAXx10Int,_Ad:s81MINx10Int,_Ae:s81HYSTx10Int,'sensor82setup':sensor82setup,_Af:s82MAXx10Int,_Ag:s82MINx10Int,_Ah:s82HYSTx10Int,'analogSetup':analogSetup,'analog1setup':analog1setup,_Ai:voltage1description,_Aj:voltage1max,_Ak:voltage1min,_Al:voltage1hyst,'analog2setup':analog2setup,_Am:voltage2description,_An:voltage2max,_Ao:voltage2min,_Ap:voltage2hyst,'analog3setup':analog3setup,_Aq:voltage3description,_Ar:voltage3max,_As:voltage3min,_At:voltage3hyst,'analog4setup':analog4setup,_Au:voltage4description,_Av:voltage4max,_Aw:voltage4min,_Ax:voltage4hyst,'digitalSetup':digitalSetup,_Ay:digitalInput1description,_Az:digitalInput2description,_A_:digitalInput3description,_B0:digitalInput4description,'relaysSetup':relaysSetup,'relay1setup':relay1setup,_B1:relay1description,_B2:relay1pulseWidth,_B3:relay1controlledBy,'relay2setup':relay2setup,_B4:relay2description,_B5:relay2pulseWidth,_B6:relay2controlledBy,'relay3setup':relay3setup,_B7:relay3description,_B8:relay3pulseWidth,_B9:relay3controlledBy,'relay4setup':relay4setup,_BA:relay4description,_BB:relay4pulseWidth,_BC:relay4controlledBy,'monitorNcontrol':monitorNcontrol,'sensors':sensors,'sensor1':sensor1,_K:s11x10Int,_L:s12x10Int,'s1ID':s1ID,'sensor2':sensor2,_M:s21x10Int,_N:s22x10Int,'s2ID':s2ID,'sensor3':sensor3,_O:s31x10Int,_P:s32x10Int,'s3ID':s3ID,'sensor4':sensor4,_Q:s41x10Int,_R:s42x10Int,'s4ID':s4ID,'sensor5':sensor5,_S:s51x10Int,_T:s52x10Int,'s5ID':s5ID,'sensor6':sensor6,_U:s61x10Int,_V:s62x10Int,'s6ID':s6ID,'sensor7':sensor7,_W:s71x10Int,_X:s72x10Int,'s7ID':s7ID,'sensor8':sensor8,_Y:s81x10Int,_Z:s82x10Int,'s8ID':s8ID,'analog':analog,_a:voltage1x10Int,_b:voltage2x10Int,_c:voltage3x10Int,_d:voltage4x10Int,_BD:voltage1x100Int,_BE:voltage2x100Int,_BF:voltage3x100Int,_BG:voltage4x100Int,'digital':digital,_e:digitalInput1State,_f:digitalInput2State,_g:digitalInput3State,_h:digitalInput4State,'relays':relays,'relay1':relay1,_BH:relay1State,_BI:relay1Pulse,'relay2':relay2,_BJ:relay2State,_BK:relay2Pulse,'relay3':relay3,_BL:relay3State,_BM:relay3Pulse,'relay4':relay4,_BN:relay4State,_BO:relay4Pulse,_BP:configurationSaved,_i:restartDevice,_BQ:temperatureUnit,_BR:hardwareErr,'tcw240bMIBConformance':tcw240bMIBConformance,'tcw240bMIBCompliances':tcw240bMIBCompliances,'tcw240bMIBCompliances1':tcw240bMIBCompliances1,'tcw240bMIBGroups':tcw240bMIBGroups,_BT:tcw240bProductGroup,_BU:tcw240bSetupGroup,_BV:tcw240bMonitorGroup,_BW:tcw240bTrapGroup,'snmpMIB':snmpMIB})