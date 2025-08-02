_x='10 Seconds'
_w='psSeverityMapIndex'
_v='dontload'
_u='dontactivate'
_t='psLogIndex'
_s='psMonthlyIndex'
_r='psDailyIndex'
_q='psHourlyIndex'
_p='psDryContactor2Index'
_o='psDryContactor1Index'
_n='psDryContactorIndex'
_m='undervoltage'
_l='overvoltage'
_k='psINUIndex'
_j='temperature'
_i='voltage'
_h='pscurrent'
_g='inprogress'
_f='psPSUIndex'
_e='negative'
_d='positive'
_c='psBatteryIndex'
_b='bad'
_a='off'
_Z='on'
_Y='DisplayString'
_X='close'
_W='open'
_V='notok'
_U='activate'
_T='yes'
_S='ok'
_R='psTrapSeverity'
_Q='OctetString'
_P='no'
_O='psTrapStatus'
_N='GAMATRONIC-MIB'
_M='notactive'
_L='set'
_K='notset'
_J='warning'
_I='minor'
_H='major'
_G='critical'
_F='enable'
_E='disable'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Y,'PhysAddress','TextualConvention')
gamatronicLTD=ModuleIdentity((1,3,6,1,4,1,6050))
class PsAlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_PsMIB_ObjectIdentity=ObjectIdentity
psMIB=_PsMIB_ObjectIdentity((1,3,6,1,4,1,6050,1))
_PsUnit_ObjectIdentity=ObjectIdentity
psUnit=_PsUnit_ObjectIdentity((1,3,6,1,4,1,6050,1,1))
class _PsUnitSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitSysName_Type.__name__=_Y
_PsUnitSysName_Object=MibScalar
psUnitSysName=_PsUnitSysName_Object((1,3,6,1,4,1,6050,1,1,1),_PsUnitSysName_Type())
psUnitSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitSysName.setStatus(_A)
class _PsUnitManufacture_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitManufacture_Type.__name__=_Y
_PsUnitManufacture_Object=MibScalar
psUnitManufacture=_PsUnitManufacture_Object((1,3,6,1,4,1,6050,1,1,2),_PsUnitManufacture_Type())
psUnitManufacture.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitManufacture.setStatus(_A)
class _PsUnitBatteryType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitBatteryType_Type.__name__=_Y
_PsUnitBatteryType_Object=MibScalar
psUnitBatteryType=_PsUnitBatteryType_Object((1,3,6,1,4,1,6050,1,1,3),_PsUnitBatteryType_Type())
psUnitBatteryType.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitBatteryType.setStatus(_A)
class _PsUnitPSType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitPSType_Type.__name__=_Y
_PsUnitPSType_Object=MibScalar
psUnitPSType=_PsUnitPSType_Object((1,3,6,1,4,1,6050,1,1,4),_PsUnitPSType_Type())
psUnitPSType.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitPSType.setStatus(_A)
class _PsUnitControllerType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitControllerType_Type.__name__=_Y
_PsUnitControllerType_Object=MibScalar
psUnitControllerType=_PsUnitControllerType_Object((1,3,6,1,4,1,6050,1,1,5),_PsUnitControllerType_Type())
psUnitControllerType.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitControllerType.setStatus(_A)
class _PsUnitSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitSoftwareVersion_Type.__name__=_Y
_PsUnitSoftwareVersion_Object=MibScalar
psUnitSoftwareVersion=_PsUnitSoftwareVersion_Object((1,3,6,1,4,1,6050,1,1,6),_PsUnitSoftwareVersion_Type())
psUnitSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitSoftwareVersion.setStatus(_A)
class _PsUnitComProtocolVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitComProtocolVersion_Type.__name__=_Y
_PsUnitComProtocolVersion_Object=MibScalar
psUnitComProtocolVersion=_PsUnitComProtocolVersion_Object((1,3,6,1,4,1,6050,1,1,7),_PsUnitComProtocolVersion_Type())
psUnitComProtocolVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitComProtocolVersion.setStatus(_A)
class _PsUnitSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PsUnitSerialNumber_Type.__name__=_Y
_PsUnitSerialNumber_Object=MibScalar
psUnitSerialNumber=_PsUnitSerialNumber_Object((1,3,6,1,4,1,6050,1,1,8),_PsUnitSerialNumber_Type())
psUnitSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:psUnitSerialNumber.setStatus(_A)
_PsUnitRTCDay_Type=Integer32
_PsUnitRTCDay_Object=MibScalar
psUnitRTCDay=_PsUnitRTCDay_Object((1,3,6,1,4,1,6050,1,1,9),_PsUnitRTCDay_Type())
psUnitRTCDay.setMaxAccess(_B)
if mibBuilder.loadTexts:psUnitRTCDay.setStatus(_A)
_PsUnitRTCMonth_Type=Integer32
_PsUnitRTCMonth_Object=MibScalar
psUnitRTCMonth=_PsUnitRTCMonth_Object((1,3,6,1,4,1,6050,1,1,10),_PsUnitRTCMonth_Type())
psUnitRTCMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:psUnitRTCMonth.setStatus(_A)
_PsUnitRTCYear_Type=Integer32
_PsUnitRTCYear_Object=MibScalar
psUnitRTCYear=_PsUnitRTCYear_Object((1,3,6,1,4,1,6050,1,1,11),_PsUnitRTCYear_Type())
psUnitRTCYear.setMaxAccess(_B)
if mibBuilder.loadTexts:psUnitRTCYear.setStatus(_A)
_PsUnitRTCHour_Type=Integer32
_PsUnitRTCHour_Object=MibScalar
psUnitRTCHour=_PsUnitRTCHour_Object((1,3,6,1,4,1,6050,1,1,12),_PsUnitRTCHour_Type())
psUnitRTCHour.setMaxAccess(_B)
if mibBuilder.loadTexts:psUnitRTCHour.setStatus(_A)
_PsUnitRTCMinute_Type=Integer32
_PsUnitRTCMinute_Object=MibScalar
psUnitRTCMinute=_PsUnitRTCMinute_Object((1,3,6,1,4,1,6050,1,1,13),_PsUnitRTCMinute_Type())
psUnitRTCMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:psUnitRTCMinute.setStatus(_A)
_PsUnitRTCSecond_Type=Integer32
_PsUnitRTCSecond_Object=MibScalar
psUnitRTCSecond=_PsUnitRTCSecond_Object((1,3,6,1,4,1,6050,1,1,14),_PsUnitRTCSecond_Type())
psUnitRTCSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:psUnitRTCSecond.setStatus(_A)
_PsWorkingTime_Type=Integer32
_PsWorkingTime_Object=MibScalar
psWorkingTime=_PsWorkingTime_Object((1,3,6,1,4,1,6050,1,1,15),_PsWorkingTime_Type())
psWorkingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:psWorkingTime.setStatus(_A)
class _PsScreenShot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(160,160));fixedLength=160
_PsScreenShot_Type.__name__=_Q
_PsScreenShot_Object=MibScalar
psScreenShot=_PsScreenShot_Object((1,3,6,1,4,1,6050,1,1,16),_PsScreenShot_Type())
psScreenShot.setMaxAccess(_B)
if mibBuilder.loadTexts:psScreenShot.setStatus(_A)
_PsSpareIde0_Type=Integer32
_PsSpareIde0_Object=MibScalar
psSpareIde0=_PsSpareIde0_Object((1,3,6,1,4,1,6050,1,1,17),_PsSpareIde0_Type())
psSpareIde0.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde0.setStatus(_A)
_PsSpareIde1_Type=Integer32
_PsSpareIde1_Object=MibScalar
psSpareIde1=_PsSpareIde1_Object((1,3,6,1,4,1,6050,1,1,18),_PsSpareIde1_Type())
psSpareIde1.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde1.setStatus(_A)
_PsSpareIde2_Type=Integer32
_PsSpareIde2_Object=MibScalar
psSpareIde2=_PsSpareIde2_Object((1,3,6,1,4,1,6050,1,1,19),_PsSpareIde2_Type())
psSpareIde2.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde2.setStatus(_A)
_PsSpareIde3_Type=Integer32
_PsSpareIde3_Object=MibScalar
psSpareIde3=_PsSpareIde3_Object((1,3,6,1,4,1,6050,1,1,20),_PsSpareIde3_Type())
psSpareIde3.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde3.setStatus(_A)
_PsSpareIde4_Type=Integer32
_PsSpareIde4_Object=MibScalar
psSpareIde4=_PsSpareIde4_Object((1,3,6,1,4,1,6050,1,1,21),_PsSpareIde4_Type())
psSpareIde4.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde4.setStatus(_A)
_PsSpareIde5_Type=Integer32
_PsSpareIde5_Object=MibScalar
psSpareIde5=_PsSpareIde5_Object((1,3,6,1,4,1,6050,1,1,22),_PsSpareIde5_Type())
psSpareIde5.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde5.setStatus(_A)
_PsSpareIde6_Type=Integer32
_PsSpareIde6_Object=MibScalar
psSpareIde6=_PsSpareIde6_Object((1,3,6,1,4,1,6050,1,1,23),_PsSpareIde6_Type())
psSpareIde6.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde6.setStatus(_A)
_PsSpareIde7_Type=Integer32
_PsSpareIde7_Object=MibScalar
psSpareIde7=_PsSpareIde7_Object((1,3,6,1,4,1,6050,1,1,24),_PsSpareIde7_Type())
psSpareIde7.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpareIde7.setStatus(_A)
_PsBattery_ObjectIdentity=ObjectIdentity
psBattery=_PsBattery_ObjectIdentity((1,3,6,1,4,1,6050,1,2))
_PsBatteryNumber_Type=Integer32
_PsBatteryNumber_Object=MibScalar
psBatteryNumber=_PsBatteryNumber_Object((1,3,6,1,4,1,6050,1,2,1),_PsBatteryNumber_Type())
psBatteryNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryNumber.setStatus(_A)
_PsBatteryVoltage_Type=Integer32
_PsBatteryVoltage_Object=MibScalar
psBatteryVoltage=_PsBatteryVoltage_Object((1,3,6,1,4,1,6050,1,2,2),_PsBatteryVoltage_Type())
psBatteryVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryVoltage.setStatus(_A)
class _PsBatteryTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_PsBatteryTestStatus_Type.__name__=_C
_PsBatteryTestStatus_Object=MibScalar
psBatteryTestStatus=_PsBatteryTestStatus_Object((1,3,6,1,4,1,6050,1,2,3),_PsBatteryTestStatus_Type())
psBatteryTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryTestStatus.setStatus(_A)
_PsBatteryNominalCapacity_Type=Integer32
_PsBatteryNominalCapacity_Object=MibScalar
psBatteryNominalCapacity=_PsBatteryNominalCapacity_Object((1,3,6,1,4,1,6050,1,2,4),_PsBatteryNominalCapacity_Type())
psBatteryNominalCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryNominalCapacity.setStatus(_A)
_PsBatteryActualCapacity_Type=Integer32
_PsBatteryActualCapacity_Object=MibScalar
psBatteryActualCapacity=_PsBatteryActualCapacity_Object((1,3,6,1,4,1,6050,1,2,5),_PsBatteryActualCapacity_Type())
psBatteryActualCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryActualCapacity.setStatus(_A)
_PsBatteryTestTime_Type=Integer32
_PsBatteryTestTime_Object=MibScalar
psBatteryTestTime=_PsBatteryTestTime_Object((1,3,6,1,4,1,6050,1,2,6),_PsBatteryTestTime_Type())
psBatteryTestTime.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryTestTime.setStatus(_A)
_PsBatteryLoadTime_Type=Integer32
_PsBatteryLoadTime_Object=MibScalar
psBatteryLoadTime=_PsBatteryLoadTime_Object((1,3,6,1,4,1,6050,1,2,7),_PsBatteryLoadTime_Type())
psBatteryLoadTime.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryLoadTime.setStatus(_A)
_PsBatteryNearestTestMonth_Type=Integer32
_PsBatteryNearestTestMonth_Object=MibScalar
psBatteryNearestTestMonth=_PsBatteryNearestTestMonth_Object((1,3,6,1,4,1,6050,1,2,8),_PsBatteryNearestTestMonth_Type())
psBatteryNearestTestMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryNearestTestMonth.setStatus(_A)
_PsBatteryNearestTestDay_Type=Integer32
_PsBatteryNearestTestDay_Object=MibScalar
psBatteryNearestTestDay=_PsBatteryNearestTestDay_Object((1,3,6,1,4,1,6050,1,2,9),_PsBatteryNearestTestDay_Type())
psBatteryNearestTestDay.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryNearestTestDay.setStatus(_A)
_PsBatteryNearestTestHour_Type=Integer32
_PsBatteryNearestTestHour_Object=MibScalar
psBatteryNearestTestHour=_PsBatteryNearestTestHour_Object((1,3,6,1,4,1,6050,1,2,10),_PsBatteryNearestTestHour_Type())
psBatteryNearestTestHour.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryNearestTestHour.setStatus(_A)
_PsBatteryNearestTestMinute_Type=Integer32
_PsBatteryNearestTestMinute_Object=MibScalar
psBatteryNearestTestMinute=_PsBatteryNearestTestMinute_Object((1,3,6,1,4,1,6050,1,2,11),_PsBatteryNearestTestMinute_Type())
psBatteryNearestTestMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryNearestTestMinute.setStatus(_A)
class _PsBatteryChargeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('floating',0),('equalizes',1)))
_PsBatteryChargeMode_Type.__name__=_C
_PsBatteryChargeMode_Object=MibScalar
psBatteryChargeMode=_PsBatteryChargeMode_Object((1,3,6,1,4,1,6050,1,2,12),_PsBatteryChargeMode_Type())
psBatteryChargeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryChargeMode.setStatus(_A)
_PsBatteryEqRunTimeHours_Type=Integer32
_PsBatteryEqRunTimeHours_Object=MibScalar
psBatteryEqRunTimeHours=_PsBatteryEqRunTimeHours_Object((1,3,6,1,4,1,6050,1,2,13),_PsBatteryEqRunTimeHours_Type())
psBatteryEqRunTimeHours.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryEqRunTimeHours.setStatus(_A)
_PsBatteryEqRunTimeMinutes_Type=Integer32
_PsBatteryEqRunTimeMinutes_Object=MibScalar
psBatteryEqRunTimeMinutes=_PsBatteryEqRunTimeMinutes_Object((1,3,6,1,4,1,6050,1,2,14),_PsBatteryEqRunTimeMinutes_Type())
psBatteryEqRunTimeMinutes.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryEqRunTimeMinutes.setStatus(_A)
_PsBatterySpareRead1_Type=Integer32
_PsBatterySpareRead1_Object=MibScalar
psBatterySpareRead1=_PsBatterySpareRead1_Object((1,3,6,1,4,1,6050,1,2,15),_PsBatterySpareRead1_Type())
psBatterySpareRead1.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatterySpareRead1.setStatus(_A)
_PsBatterySpareRead2_Type=Integer32
_PsBatterySpareRead2_Object=MibScalar
psBatterySpareRead2=_PsBatterySpareRead2_Object((1,3,6,1,4,1,6050,1,2,16),_PsBatterySpareRead2_Type())
psBatterySpareRead2.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatterySpareRead2.setStatus(_A)
_PsBatterySpareRead3_Type=Integer32
_PsBatterySpareRead3_Object=MibScalar
psBatterySpareRead3=_PsBatterySpareRead3_Object((1,3,6,1,4,1,6050,1,2,17),_PsBatterySpareRead3_Type())
psBatterySpareRead3.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatterySpareRead3.setStatus(_A)
_PsBatterySpareWrite1_Type=Integer32
_PsBatterySpareWrite1_Object=MibScalar
psBatterySpareWrite1=_PsBatterySpareWrite1_Object((1,3,6,1,4,1,6050,1,2,18),_PsBatterySpareWrite1_Type())
psBatterySpareWrite1.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite1.setStatus(_A)
_PsBatterySpareWrite2_Type=Integer32
_PsBatterySpareWrite2_Object=MibScalar
psBatterySpareWrite2=_PsBatterySpareWrite2_Object((1,3,6,1,4,1,6050,1,2,19),_PsBatterySpareWrite2_Type())
psBatterySpareWrite2.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite2.setStatus(_A)
_PsBatterySpareWrite3_Type=Integer32
_PsBatterySpareWrite3_Object=MibScalar
psBatterySpareWrite3=_PsBatterySpareWrite3_Object((1,3,6,1,4,1,6050,1,2,20),_PsBatterySpareWrite3_Type())
psBatterySpareWrite3.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite3.setStatus(_A)
_PsBatterySpareWrite4_Type=Integer32
_PsBatterySpareWrite4_Object=MibScalar
psBatterySpareWrite4=_PsBatterySpareWrite4_Object((1,3,6,1,4,1,6050,1,2,21),_PsBatterySpareWrite4_Type())
psBatterySpareWrite4.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite4.setStatus(_A)
_PsBatterySpareWrite5_Type=Integer32
_PsBatterySpareWrite5_Object=MibScalar
psBatterySpareWrite5=_PsBatterySpareWrite5_Object((1,3,6,1,4,1,6050,1,2,22),_PsBatterySpareWrite5_Type())
psBatterySpareWrite5.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite5.setStatus(_A)
_PsBatterySpareWrite6_Type=Integer32
_PsBatterySpareWrite6_Object=MibScalar
psBatterySpareWrite6=_PsBatterySpareWrite6_Object((1,3,6,1,4,1,6050,1,2,23),_PsBatterySpareWrite6_Type())
psBatterySpareWrite6.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite6.setStatus(_A)
_PsBatterySpareWrite7_Type=Integer32
_PsBatterySpareWrite7_Object=MibScalar
psBatterySpareWrite7=_PsBatterySpareWrite7_Object((1,3,6,1,4,1,6050,1,2,24),_PsBatterySpareWrite7_Type())
psBatterySpareWrite7.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite7.setStatus(_A)
_PsBatterySpareWrite8_Type=Integer32
_PsBatterySpareWrite8_Object=MibScalar
psBatterySpareWrite8=_PsBatterySpareWrite8_Object((1,3,6,1,4,1,6050,1,2,25),_PsBatterySpareWrite8_Type())
psBatterySpareWrite8.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatterySpareWrite8.setStatus(_A)
_PsBatteryTable_Object=MibTable
psBatteryTable=_PsBatteryTable_Object((1,3,6,1,4,1,6050,1,2,26))
if mibBuilder.loadTexts:psBatteryTable.setStatus(_A)
_PsBatteryEntry_Object=MibTableRow
psBatteryEntry=_PsBatteryEntry_Object((1,3,6,1,4,1,6050,1,2,26,1))
psBatteryEntry.setIndexNames((0,_N,_c))
if mibBuilder.loadTexts:psBatteryEntry.setStatus(_A)
_PsBatteryIndex_Type=Integer32
_PsBatteryIndex_Object=MibTableColumn
psBatteryIndex=_PsBatteryIndex_Object((1,3,6,1,4,1,6050,1,2,26,1,1),_PsBatteryIndex_Type())
psBatteryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryIndex.setStatus(_A)
_PsBatteryCurrentDirection_Type=Integer32
_PsBatteryCurrentDirection_Object=MibTableColumn
psBatteryCurrentDirection=_PsBatteryCurrentDirection_Object((1,3,6,1,4,1,6050,1,2,26,1,2),_PsBatteryCurrentDirection_Type())
psBatteryCurrentDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryCurrentDirection.setStatus(_A)
_PsBatteryCurrent_Type=Integer32
_PsBatteryCurrent_Object=MibTableColumn
psBatteryCurrent=_PsBatteryCurrent_Object((1,3,6,1,4,1,6050,1,2,26,1,3),_PsBatteryCurrent_Type())
psBatteryCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryCurrent.setStatus(_A)
class _PsBatteryTemperatureSign_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_e,1)))
_PsBatteryTemperatureSign_Type.__name__=_C
_PsBatteryTemperatureSign_Object=MibTableColumn
psBatteryTemperatureSign=_PsBatteryTemperatureSign_Object((1,3,6,1,4,1,6050,1,2,26,1,4),_PsBatteryTemperatureSign_Type())
psBatteryTemperatureSign.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryTemperatureSign.setStatus(_A)
_PsBatteryTemperature_Type=Integer32
_PsBatteryTemperature_Object=MibTableColumn
psBatteryTemperature=_PsBatteryTemperature_Object((1,3,6,1,4,1,6050,1,2,26,1,5),_PsBatteryTemperature_Type())
psBatteryTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryTemperature.setStatus(_A)
class _PsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('passed',0),('failed',1),('low',2)))
_PsBatteryStatus_Type.__name__=_C
_PsBatteryStatus_Object=MibTableColumn
psBatteryStatus=_PsBatteryStatus_Object((1,3,6,1,4,1,6050,1,2,26,1,6),_PsBatteryStatus_Type())
psBatteryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryStatus.setStatus(_A)
class _PsBatteryFuseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_b,1)))
_PsBatteryFuseStatus_Type.__name__=_C
_PsBatteryFuseStatus_Object=MibTableColumn
psBatteryFuseStatus=_PsBatteryFuseStatus_Object((1,3,6,1,4,1,6050,1,2,26,1,7),_PsBatteryFuseStatus_Type())
psBatteryFuseStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psBatteryFuseStatus.setStatus(_A)
_PsBatteryInstalationYear_Type=Integer32
_PsBatteryInstalationYear_Object=MibTableColumn
psBatteryInstalationYear=_PsBatteryInstalationYear_Object((1,3,6,1,4,1,6050,1,2,26,1,8),_PsBatteryInstalationYear_Type())
psBatteryInstalationYear.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryInstalationYear.setStatus(_A)
_PsBatteryInstalationMonth_Type=Integer32
_PsBatteryInstalationMonth_Object=MibTableColumn
psBatteryInstalationMonth=_PsBatteryInstalationMonth_Object((1,3,6,1,4,1,6050,1,2,26,1,9),_PsBatteryInstalationMonth_Type())
psBatteryInstalationMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryInstalationMonth.setStatus(_A)
_PsBatteryInstalationDay_Type=Integer32
_PsBatteryInstalationDay_Object=MibTableColumn
psBatteryInstalationDay=_PsBatteryInstalationDay_Object((1,3,6,1,4,1,6050,1,2,26,1,10),_PsBatteryInstalationDay_Type())
psBatteryInstalationDay.setMaxAccess(_B)
if mibBuilder.loadTexts:psBatteryInstalationDay.setStatus(_A)
_PsPSU_ObjectIdentity=ObjectIdentity
psPSU=_PsPSU_ObjectIdentity((1,3,6,1,4,1,6050,1,3))
_PsPSUNumber_Type=Integer32
_PsPSUNumber_Object=MibScalar
psPSUNumber=_PsPSUNumber_Object((1,3,6,1,4,1,6050,1,3,1),_PsPSUNumber_Type())
psPSUNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUNumber.setStatus(_A)
_PsPSUTable_Object=MibTable
psPSUTable=_PsPSUTable_Object((1,3,6,1,4,1,6050,1,3,2))
if mibBuilder.loadTexts:psPSUTable.setStatus(_A)
_PsPSUEntry_Object=MibTableRow
psPSUEntry=_PsPSUEntry_Object((1,3,6,1,4,1,6050,1,3,2,1))
psPSUEntry.setIndexNames((0,_N,_f))
if mibBuilder.loadTexts:psPSUEntry.setStatus(_A)
_PsPSUIndex_Type=Integer32
_PsPSUIndex_Object=MibTableColumn
psPSUIndex=_PsPSUIndex_Object((1,3,6,1,4,1,6050,1,3,2,1,1),_PsPSUIndex_Type())
psPSUIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUIndex.setStatus(_A)
_PsPSUVoltage_Type=Integer32
_PsPSUVoltage_Object=MibTableColumn
psPSUVoltage=_PsPSUVoltage_Object((1,3,6,1,4,1,6050,1,3,2,1,2),_PsPSUVoltage_Type())
psPSUVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUVoltage.setStatus(_A)
_PsPSUCurrent_Type=Integer32
_PsPSUCurrent_Object=MibTableColumn
psPSUCurrent=_PsPSUCurrent_Object((1,3,6,1,4,1,6050,1,3,2,1,3),_PsPSUCurrent_Type())
psPSUCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUCurrent.setStatus(_A)
_PsPSUTemperature_Type=Integer32
_PsPSUTemperature_Object=MibTableColumn
psPSUTemperature=_PsPSUTemperature_Object((1,3,6,1,4,1,6050,1,3,2,1,4),_PsPSUTemperature_Type())
psPSUTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUTemperature.setStatus(_A)
class _PsPSUActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),(_Z,1)))
_PsPSUActivity_Type.__name__=_C
_PsPSUActivity_Object=MibTableColumn
psPSUActivity=_PsPSUActivity_Object((1,3,6,1,4,1,6050,1,3,2,1,5),_PsPSUActivity_Type())
psPSUActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:psPSUActivity.setStatus(_A)
_PsPSUPsType_Type=Integer32
_PsPSUPsType_Object=MibTableColumn
psPSUPsType=_PsPSUPsType_Object((1,3,6,1,4,1,6050,1,3,2,1,6),_PsPSUPsType_Type())
psPSUPsType.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUPsType.setStatus(_A)
_PsPSUStatus_Type=Integer32
_PsPSUStatus_Object=MibTableColumn
psPSUStatus=_PsPSUStatus_Object((1,3,6,1,4,1,6050,1,3,2,1,7),_PsPSUStatus_Type())
psPSUStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUStatus.setStatus(_A)
class _PsPSUPsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsPSUPsOK_Type.__name__=_C
_PsPSUPsOK_Object=MibTableColumn
psPSUPsOK=_PsPSUPsOK_Object((1,3,6,1,4,1,6050,1,3,2,1,8),_PsPSUPsOK_Type())
psPSUPsOK.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUPsOK.setStatus(_A)
class _PsPSUNotRespond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_b,1)))
_PsPSUNotRespond_Type.__name__=_C
_PsPSUNotRespond_Object=MibTableColumn
psPSUNotRespond=_PsPSUNotRespond_Object((1,3,6,1,4,1,6050,1,3,2,1,9),_PsPSUNotRespond_Type())
psPSUNotRespond.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUNotRespond.setStatus(_A)
class _PsPSUNOOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUNOOut_Type.__name__=_C
_PsPSUNOOut_Object=MibTableColumn
psPSUNOOut=_PsPSUNOOut_Object((1,3,6,1,4,1,6050,1,3,2,1,10),_PsPSUNOOut_Type())
psPSUNOOut.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUNOOut.setStatus(_A)
class _PsPSUPSpareBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsPSUPSpareBit_Type.__name__=_C
_PsPSUPSpareBit_Object=MibTableColumn
psPSUPSpareBit=_PsPSUPSpareBit_Object((1,3,6,1,4,1,6050,1,3,2,1,11),_PsPSUPSpareBit_Type())
psPSUPSpareBit.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUPSpareBit.setStatus(_A)
class _PsPSUBadSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsPSUBadSharing_Type.__name__=_C
_PsPSUBadSharing_Object=MibTableColumn
psPSUBadSharing=_PsPSUBadSharing_Object((1,3,6,1,4,1,6050,1,3,2,1,12),_PsPSUBadSharing_Type())
psPSUBadSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUBadSharing.setStatus(_A)
_PsPSUReserve1_Type=Integer32
_PsPSUReserve1_Object=MibTableColumn
psPSUReserve1=_PsPSUReserve1_Object((1,3,6,1,4,1,6050,1,3,2,1,13),_PsPSUReserve1_Type())
psPSUReserve1.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUReserve1.setStatus(_A)
_PsPSUReserve2_Type=Integer32
_PsPSUReserve2_Object=MibTableColumn
psPSUReserve2=_PsPSUReserve2_Object((1,3,6,1,4,1,6050,1,3,2,1,14),_PsPSUReserve2_Type())
psPSUReserve2.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUReserve2.setStatus(_A)
_PsPSUReserve3_Type=Integer32
_PsPSUReserve3_Object=MibTableColumn
psPSUReserve3=_PsPSUReserve3_Object((1,3,6,1,4,1,6050,1,3,2,1,15),_PsPSUReserve3_Type())
psPSUReserve3.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUReserve3.setStatus(_A)
class _PsPSUShutInstruction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUShutInstruction_Type.__name__=_C
_PsPSUShutInstruction_Object=MibTableColumn
psPSUShutInstruction=_PsPSUShutInstruction_Object((1,3,6,1,4,1,6050,1,3,2,1,16),_PsPSUShutInstruction_Type())
psPSUShutInstruction.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUShutInstruction.setStatus(_A)
class _PsPSUTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notintest',0),(_g,1)))
_PsPSUTestStatus_Type.__name__=_C
_PsPSUTestStatus_Object=MibTableColumn
psPSUTestStatus=_PsPSUTestStatus_Object((1,3,6,1,4,1,6050,1,3,2,1,17),_PsPSUTestStatus_Type())
psPSUTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUTestStatus.setStatus(_A)
class _PsPSUCurrentLimitDecreased_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUCurrentLimitDecreased_Type.__name__=_C
_PsPSUCurrentLimitDecreased_Object=MibTableColumn
psPSUCurrentLimitDecreased=_PsPSUCurrentLimitDecreased_Object((1,3,6,1,4,1,6050,1,3,2,1,18),_PsPSUCurrentLimitDecreased_Type())
psPSUCurrentLimitDecreased.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUCurrentLimitDecreased.setStatus(_A)
class _PsPSUACInputOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsPSUACInputOK_Type.__name__=_C
_PsPSUACInputOK_Object=MibTableColumn
psPSUACInputOK=_PsPSUACInputOK_Object((1,3,6,1,4,1,6050,1,3,2,1,19),_PsPSUACInputOK_Type())
psPSUACInputOK.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUACInputOK.setStatus(_A)
class _PsPSUSelfTestPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsPSUSelfTestPass_Type.__name__=_C
_PsPSUSelfTestPass_Object=MibTableColumn
psPSUSelfTestPass=_PsPSUSelfTestPass_Object((1,3,6,1,4,1,6050,1,3,2,1,20),_PsPSUSelfTestPass_Type())
psPSUSelfTestPass.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUSelfTestPass.setStatus(_A)
class _PsPSUCurrentLimitExceed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUCurrentLimitExceed_Type.__name__=_C
_PsPSUCurrentLimitExceed_Object=MibTableColumn
psPSUCurrentLimitExceed=_PsPSUCurrentLimitExceed_Object((1,3,6,1,4,1,6050,1,3,2,1,21),_PsPSUCurrentLimitExceed_Type())
psPSUCurrentLimitExceed.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUCurrentLimitExceed.setStatus(_A)
class _PsPSUShutHighTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUShutHighTemp_Type.__name__=_C
_PsPSUShutHighTemp_Object=MibTableColumn
psPSUShutHighTemp=_PsPSUShutHighTemp_Object((1,3,6,1,4,1,6050,1,3,2,1,22),_PsPSUShutHighTemp_Type())
psPSUShutHighTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUShutHighTemp.setStatus(_A)
class _PsPSUShutHighVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUShutHighVolt_Type.__name__=_C
_PsPSUShutHighVolt_Object=MibTableColumn
psPSUShutHighVolt=_PsPSUShutHighVolt_Object((1,3,6,1,4,1,6050,1,3,2,1,23),_PsPSUShutHighVolt_Type())
psPSUShutHighVolt.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUShutHighVolt.setStatus(_A)
class _PsPSURemoteMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSURemoteMode_Type.__name__=_C
_PsPSURemoteMode_Object=MibTableColumn
psPSURemoteMode=_PsPSURemoteMode_Object((1,3,6,1,4,1,6050,1,3,2,1,24),_PsPSURemoteMode_Type())
psPSURemoteMode.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSURemoteMode.setStatus(_A)
class _PsPSUFloatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUFloatingMode_Type.__name__=_C
_PsPSUFloatingMode_Object=MibTableColumn
psPSUFloatingMode=_PsPSUFloatingMode_Object((1,3,6,1,4,1,6050,1,3,2,1,25),_PsPSUFloatingMode_Type())
psPSUFloatingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUFloatingMode.setStatus(_A)
class _PsPSUEqualizeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsPSUEqualizeMode_Type.__name__=_C
_PsPSUEqualizeMode_Object=MibTableColumn
psPSUEqualizeMode=_PsPSUEqualizeMode_Object((1,3,6,1,4,1,6050,1,3,2,1,26),_PsPSUEqualizeMode_Type())
psPSUEqualizeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUEqualizeMode.setStatus(_A)
class _PsPSUFanStataus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_b,1)))
_PsPSUFanStataus_Type.__name__=_C
_PsPSUFanStataus_Object=MibTableColumn
psPSUFanStataus=_PsPSUFanStataus_Object((1,3,6,1,4,1,6050,1,3,2,1,27),_PsPSUFanStataus_Type())
psPSUFanStataus.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUFanStataus.setStatus(_A)
class _PsPSUIndication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_h,0),(_i,1),(_j,3)))
_PsPSUIndication_Type.__name__=_C
_PsPSUIndication_Object=MibTableColumn
psPSUIndication=_PsPSUIndication_Object((1,3,6,1,4,1,6050,1,3,2,1,28),_PsPSUIndication_Type())
psPSUIndication.setMaxAccess(_D)
if mibBuilder.loadTexts:psPSUIndication.setStatus(_A)
_PsINU_ObjectIdentity=ObjectIdentity
psINU=_PsINU_ObjectIdentity((1,3,6,1,4,1,6050,1,4))
_PsINUNumber_Type=Integer32
_PsINUNumber_Object=MibScalar
psINUNumber=_PsINUNumber_Object((1,3,6,1,4,1,6050,1,4,1),_PsINUNumber_Type())
psINUNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUNumber.setStatus(_A)
_PsINUTable_Object=MibTable
psINUTable=_PsINUTable_Object((1,3,6,1,4,1,6050,1,4,2))
if mibBuilder.loadTexts:psINUTable.setStatus(_A)
_PsINUEntry_Object=MibTableRow
psINUEntry=_PsINUEntry_Object((1,3,6,1,4,1,6050,1,4,2,1))
psINUEntry.setIndexNames((0,_N,_k))
if mibBuilder.loadTexts:psINUEntry.setStatus(_A)
_PsINUIndex_Type=Integer32
_PsINUIndex_Object=MibTableColumn
psINUIndex=_PsINUIndex_Object((1,3,6,1,4,1,6050,1,4,2,1,1),_PsINUIndex_Type())
psINUIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUIndex.setStatus(_A)
_PsINUVoltage_Type=Integer32
_PsINUVoltage_Object=MibTableColumn
psINUVoltage=_PsINUVoltage_Object((1,3,6,1,4,1,6050,1,4,2,1,2),_PsINUVoltage_Type())
psINUVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUVoltage.setStatus(_A)
_PsINUCurrent_Type=Integer32
_PsINUCurrent_Object=MibTableColumn
psINUCurrent=_PsINUCurrent_Object((1,3,6,1,4,1,6050,1,4,2,1,3),_PsINUCurrent_Type())
psINUCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUCurrent.setStatus(_A)
_PsINUTemperature_Type=Integer32
_PsINUTemperature_Object=MibTableColumn
psINUTemperature=_PsINUTemperature_Object((1,3,6,1,4,1,6050,1,4,2,1,4),_PsINUTemperature_Type())
psINUTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUTemperature.setStatus(_A)
class _PsINUActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),(_Z,1)))
_PsINUActivity_Type.__name__=_C
_PsINUActivity_Object=MibTableColumn
psINUActivity=_PsINUActivity_Object((1,3,6,1,4,1,6050,1,4,2,1,5),_PsINUActivity_Type())
psINUActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:psINUActivity.setStatus(_A)
_PsINUPsType_Type=Integer32
_PsINUPsType_Object=MibTableColumn
psINUPsType=_PsINUPsType_Object((1,3,6,1,4,1,6050,1,4,2,1,6),_PsINUPsType_Type())
psINUPsType.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUPsType.setStatus(_A)
_PsINUStatus_Type=Integer32
_PsINUStatus_Object=MibTableColumn
psINUStatus=_PsINUStatus_Object((1,3,6,1,4,1,6050,1,4,2,1,7),_PsINUStatus_Type())
psINUStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUStatus.setStatus(_A)
class _PsINUPsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsINUPsOK_Type.__name__=_C
_PsINUPsOK_Object=MibTableColumn
psINUPsOK=_PsINUPsOK_Object((1,3,6,1,4,1,6050,1,4,2,1,8),_PsINUPsOK_Type())
psINUPsOK.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUPsOK.setStatus(_A)
class _PsINUNotRespond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_b,1)))
_PsINUNotRespond_Type.__name__=_C
_PsINUNotRespond_Object=MibTableColumn
psINUNotRespond=_PsINUNotRespond_Object((1,3,6,1,4,1,6050,1,4,2,1,9),_PsINUNotRespond_Type())
psINUNotRespond.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUNotRespond.setStatus(_A)
class _PsINUNOOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINUNOOut_Type.__name__=_C
_PsINUNOOut_Object=MibTableColumn
psINUNOOut=_PsINUNOOut_Object((1,3,6,1,4,1,6050,1,4,2,1,10),_PsINUNOOut_Type())
psINUNOOut.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUNOOut.setStatus(_A)
class _PsINUPSpareBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsINUPSpareBit_Type.__name__=_C
_PsINUPSpareBit_Object=MibTableColumn
psINUPSpareBit=_PsINUPSpareBit_Object((1,3,6,1,4,1,6050,1,4,2,1,11),_PsINUPSpareBit_Type())
psINUPSpareBit.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUPSpareBit.setStatus(_A)
class _PsINUBadSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsINUBadSharing_Type.__name__=_C
_PsINUBadSharing_Object=MibTableColumn
psINUBadSharing=_PsINUBadSharing_Object((1,3,6,1,4,1,6050,1,4,2,1,12),_PsINUBadSharing_Type())
psINUBadSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUBadSharing.setStatus(_A)
_PsINUReserve1_Type=Integer32
_PsINUReserve1_Object=MibTableColumn
psINUReserve1=_PsINUReserve1_Object((1,3,6,1,4,1,6050,1,4,2,1,13),_PsINUReserve1_Type())
psINUReserve1.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve1.setStatus(_A)
_PsINUReserve2_Type=Integer32
_PsINUReserve2_Object=MibTableColumn
psINUReserve2=_PsINUReserve2_Object((1,3,6,1,4,1,6050,1,4,2,1,14),_PsINUReserve2_Type())
psINUReserve2.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve2.setStatus(_A)
_PsINUReserve3_Type=Integer32
_PsINUReserve3_Object=MibTableColumn
psINUReserve3=_PsINUReserve3_Object((1,3,6,1,4,1,6050,1,4,2,1,15),_PsINUReserve3_Type())
psINUReserve3.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve3.setStatus(_A)
class _PsINUShutInstruction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINUShutInstruction_Type.__name__=_C
_PsINUShutInstruction_Object=MibTableColumn
psINUShutInstruction=_PsINUShutInstruction_Object((1,3,6,1,4,1,6050,1,4,2,1,16),_PsINUShutInstruction_Type())
psINUShutInstruction.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUShutInstruction.setStatus(_A)
_PsINUReserve7_Type=Integer32
_PsINUReserve7_Object=MibTableColumn
psINUReserve7=_PsINUReserve7_Object((1,3,6,1,4,1,6050,1,4,2,1,17),_PsINUReserve7_Type())
psINUReserve7.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve7.setStatus(_A)
class _PsINUCurrentLimitDecreased_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINUCurrentLimitDecreased_Type.__name__=_C
_PsINUCurrentLimitDecreased_Object=MibTableColumn
psINUCurrentLimitDecreased=_PsINUCurrentLimitDecreased_Object((1,3,6,1,4,1,6050,1,4,2,1,18),_PsINUCurrentLimitDecreased_Type())
psINUCurrentLimitDecreased.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUCurrentLimitDecreased.setStatus(_A)
_PsINUReserve8_Type=Integer32
_PsINUReserve8_Object=MibTableColumn
psINUReserve8=_PsINUReserve8_Object((1,3,6,1,4,1,6050,1,4,2,1,19),_PsINUReserve8_Type())
psINUReserve8.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve8.setStatus(_A)
class _PsINUSelfTestPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsINUSelfTestPass_Type.__name__=_C
_PsINUSelfTestPass_Object=MibTableColumn
psINUSelfTestPass=_PsINUSelfTestPass_Object((1,3,6,1,4,1,6050,1,4,2,1,20),_PsINUSelfTestPass_Type())
psINUSelfTestPass.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUSelfTestPass.setStatus(_A)
class _PsINUCurrentLimitExceed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINUCurrentLimitExceed_Type.__name__=_C
_PsINUCurrentLimitExceed_Object=MibTableColumn
psINUCurrentLimitExceed=_PsINUCurrentLimitExceed_Object((1,3,6,1,4,1,6050,1,4,2,1,21),_PsINUCurrentLimitExceed_Type())
psINUCurrentLimitExceed.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUCurrentLimitExceed.setStatus(_A)
class _PsINUShutHighTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINUShutHighTemp_Type.__name__=_C
_PsINUShutHighTemp_Object=MibTableColumn
psINUShutHighTemp=_PsINUShutHighTemp_Object((1,3,6,1,4,1,6050,1,4,2,1,22),_PsINUShutHighTemp_Type())
psINUShutHighTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUShutHighTemp.setStatus(_A)
class _PsINUShutHighVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINUShutHighVolt_Type.__name__=_C
_PsINUShutHighVolt_Object=MibTableColumn
psINUShutHighVolt=_PsINUShutHighVolt_Object((1,3,6,1,4,1,6050,1,4,2,1,23),_PsINUShutHighVolt_Type())
psINUShutHighVolt.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUShutHighVolt.setStatus(_A)
class _PsINURemoteMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsINURemoteMode_Type.__name__=_C
_PsINURemoteMode_Object=MibTableColumn
psINURemoteMode=_PsINURemoteMode_Object((1,3,6,1,4,1,6050,1,4,2,1,24),_PsINURemoteMode_Type())
psINURemoteMode.setMaxAccess(_D)
if mibBuilder.loadTexts:psINURemoteMode.setStatus(_A)
_PsINUReserve9_Type=Integer32
_PsINUReserve9_Object=MibTableColumn
psINUReserve9=_PsINUReserve9_Object((1,3,6,1,4,1,6050,1,4,2,1,25),_PsINUReserve9_Type())
psINUReserve9.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve9.setStatus(_A)
_PsINUReserve10_Type=Integer32
_PsINUReserve10_Object=MibTableColumn
psINUReserve10=_PsINUReserve10_Object((1,3,6,1,4,1,6050,1,4,2,1,26),_PsINUReserve10_Type())
psINUReserve10.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUReserve10.setStatus(_A)
class _PsINUFanStataus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_b,1)))
_PsINUFanStataus_Type.__name__=_C
_PsINUFanStataus_Object=MibTableColumn
psINUFanStataus=_PsINUFanStataus_Object((1,3,6,1,4,1,6050,1,4,2,1,27),_PsINUFanStataus_Type())
psINUFanStataus.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUFanStataus.setStatus(_A)
class _PsINUIndication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_h,0),(_i,1),(_j,3)))
_PsINUIndication_Type.__name__=_C
_PsINUIndication_Object=MibTableColumn
psINUIndication=_PsINUIndication_Object((1,3,6,1,4,1,6050,1,4,2,1,28),_PsINUIndication_Type())
psINUIndication.setMaxAccess(_D)
if mibBuilder.loadTexts:psINUIndication.setStatus(_A)
_PsACInput_ObjectIdentity=ObjectIdentity
psACInput=_PsACInput_ObjectIdentity((1,3,6,1,4,1,6050,1,5))
_PsACInputVoltage1_Type=Integer32
_PsACInputVoltage1_Object=MibScalar
psACInputVoltage1=_PsACInputVoltage1_Object((1,3,6,1,4,1,6050,1,5,1),_PsACInputVoltage1_Type())
psACInputVoltage1.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputVoltage1.setStatus(_A)
_PsACInputVoltage2_Type=Integer32
_PsACInputVoltage2_Object=MibScalar
psACInputVoltage2=_PsACInputVoltage2_Object((1,3,6,1,4,1,6050,1,5,2),_PsACInputVoltage2_Type())
psACInputVoltage2.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputVoltage2.setStatus(_A)
_PsACInputVoltage3_Type=Integer32
_PsACInputVoltage3_Object=MibScalar
psACInputVoltage3=_PsACInputVoltage3_Object((1,3,6,1,4,1,6050,1,5,3),_PsACInputVoltage3_Type())
psACInputVoltage3.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputVoltage3.setStatus(_A)
_PsACInputCurrent1_Type=Integer32
_PsACInputCurrent1_Object=MibScalar
psACInputCurrent1=_PsACInputCurrent1_Object((1,3,6,1,4,1,6050,1,5,4),_PsACInputCurrent1_Type())
psACInputCurrent1.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputCurrent1.setStatus(_A)
_PsACInputCurrent2_Type=Integer32
_PsACInputCurrent2_Object=MibScalar
psACInputCurrent2=_PsACInputCurrent2_Object((1,3,6,1,4,1,6050,1,5,5),_PsACInputCurrent2_Type())
psACInputCurrent2.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputCurrent2.setStatus(_A)
_PsACInputCurrent3_Type=Integer32
_PsACInputCurrent3_Object=MibScalar
psACInputCurrent3=_PsACInputCurrent3_Object((1,3,6,1,4,1,6050,1,5,6),_PsACInputCurrent3_Type())
psACInputCurrent3.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputCurrent3.setStatus(_A)
_PsACInputFrequency_Type=Integer32
_PsACInputFrequency_Object=MibScalar
psACInputFrequency=_PsACInputFrequency_Object((1,3,6,1,4,1,6050,1,5,7),_PsACInputFrequency_Type())
psACInputFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputFrequency.setStatus(_A)
class _PsACInputACStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsACInputACStatus_Type.__name__=_C
_PsACInputACStatus_Object=MibScalar
psACInputACStatus=_PsACInputACStatus_Object((1,3,6,1,4,1,6050,1,5,8),_PsACInputACStatus_Type())
psACInputACStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputACStatus.setStatus(_A)
class _PsACInputSurgeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsACInputSurgeStatus_Type.__name__=_C
_PsACInputSurgeStatus_Object=MibScalar
psACInputSurgeStatus=_PsACInputSurgeStatus_Object((1,3,6,1,4,1,6050,1,5,9),_PsACInputSurgeStatus_Type())
psACInputSurgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSurgeStatus.setStatus(_A)
_PsACInputSpareInp0_Type=Integer32
_PsACInputSpareInp0_Object=MibScalar
psACInputSpareInp0=_PsACInputSpareInp0_Object((1,3,6,1,4,1,6050,1,5,10),_PsACInputSpareInp0_Type())
psACInputSpareInp0.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp0.setStatus(_A)
_PsACInputSpareInp1_Type=Integer32
_PsACInputSpareInp1_Object=MibScalar
psACInputSpareInp1=_PsACInputSpareInp1_Object((1,3,6,1,4,1,6050,1,5,11),_PsACInputSpareInp1_Type())
psACInputSpareInp1.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp1.setStatus(_A)
_PsACInputSpareInp2_Type=Integer32
_PsACInputSpareInp2_Object=MibScalar
psACInputSpareInp2=_PsACInputSpareInp2_Object((1,3,6,1,4,1,6050,1,5,12),_PsACInputSpareInp2_Type())
psACInputSpareInp2.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp2.setStatus(_A)
_PsACInputSpareInp3_Type=Integer32
_PsACInputSpareInp3_Object=MibScalar
psACInputSpareInp3=_PsACInputSpareInp3_Object((1,3,6,1,4,1,6050,1,5,14),_PsACInputSpareInp3_Type())
psACInputSpareInp3.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp3.setStatus(_A)
_PsACInputSpareInp4_Type=Integer32
_PsACInputSpareInp4_Object=MibScalar
psACInputSpareInp4=_PsACInputSpareInp4_Object((1,3,6,1,4,1,6050,1,5,15),_PsACInputSpareInp4_Type())
psACInputSpareInp4.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp4.setStatus(_A)
_PsACInputSpareInp5_Type=Integer32
_PsACInputSpareInp5_Object=MibScalar
psACInputSpareInp5=_PsACInputSpareInp5_Object((1,3,6,1,4,1,6050,1,5,16),_PsACInputSpareInp5_Type())
psACInputSpareInp5.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp5.setStatus(_A)
_PsACInputSpareInp6_Type=Integer32
_PsACInputSpareInp6_Object=MibScalar
psACInputSpareInp6=_PsACInputSpareInp6_Object((1,3,6,1,4,1,6050,1,5,17),_PsACInputSpareInp6_Type())
psACInputSpareInp6.setMaxAccess(_D)
if mibBuilder.loadTexts:psACInputSpareInp6.setStatus(_A)
_PsDCOutput_ObjectIdentity=ObjectIdentity
psDCOutput=_PsDCOutput_ObjectIdentity((1,3,6,1,4,1,6050,1,6))
_PsDCoutputVoltage_Type=Integer32
_PsDCoutputVoltage_Object=MibScalar
psDCoutputVoltage=_PsDCoutputVoltage_Object((1,3,6,1,4,1,6050,1,6,1),_PsDCoutputVoltage_Type())
psDCoutputVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputVoltage.setStatus(_A)
_PsDCoutputCurrent1_Type=Integer32
_PsDCoutputCurrent1_Object=MibScalar
psDCoutputCurrent1=_PsDCoutputCurrent1_Object((1,3,6,1,4,1,6050,1,6,2),_PsDCoutputCurrent1_Type())
psDCoutputCurrent1.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputCurrent1.setStatus(_A)
_PsDCoutputCurrent2_Type=Integer32
_PsDCoutputCurrent2_Object=MibScalar
psDCoutputCurrent2=_PsDCoutputCurrent2_Object((1,3,6,1,4,1,6050,1,6,3),_PsDCoutputCurrent2_Type())
psDCoutputCurrent2.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputCurrent2.setStatus(_A)
_PsDCoutputCurrent3_Type=Integer32
_PsDCoutputCurrent3_Object=MibScalar
psDCoutputCurrent3=_PsDCoutputCurrent3_Object((1,3,6,1,4,1,6050,1,6,4),_PsDCoutputCurrent3_Type())
psDCoutputCurrent3.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputCurrent3.setStatus(_A)
_PsDCoutputCurrent4_Type=Integer32
_PsDCoutputCurrent4_Object=MibScalar
psDCoutputCurrent4=_PsDCoutputCurrent4_Object((1,3,6,1,4,1,6050,1,6,5),_PsDCoutputCurrent4_Type())
psDCoutputCurrent4.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputCurrent4.setStatus(_A)
_PsDCoutputCurrent5_Type=Integer32
_PsDCoutputCurrent5_Object=MibScalar
psDCoutputCurrent5=_PsDCoutputCurrent5_Object((1,3,6,1,4,1,6050,1,6,6),_PsDCoutputCurrent5_Type())
psDCoutputCurrent5.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputCurrent5.setStatus(_A)
class _PsDCoutputDCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),(_l,1),(_m,2),('disconnected',3)))
_PsDCoutputDCStatus_Type.__name__=_C
_PsDCoutputDCStatus_Object=MibScalar
psDCoutputDCStatus=_PsDCoutputDCStatus_Object((1,3,6,1,4,1,6050,1,6,11),_PsDCoutputDCStatus_Type())
psDCoutputDCStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputDCStatus.setStatus(_A)
class _PsDCoutputSurgeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_V,1)))
_PsDCoutputSurgeStatus_Type.__name__=_C
_PsDCoutputSurgeStatus_Object=MibScalar
psDCoutputSurgeStatus=_PsDCoutputSurgeStatus_Object((1,3,6,1,4,1,6050,1,6,12),_PsDCoutputSurgeStatus_Type())
psDCoutputSurgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSurgeStatus.setStatus(_A)
_PsDCoutputInvertorVoltage_Type=Integer32
_PsDCoutputInvertorVoltage_Object=MibScalar
psDCoutputInvertorVoltage=_PsDCoutputInvertorVoltage_Object((1,3,6,1,4,1,6050,1,6,13),_PsDCoutputInvertorVoltage_Type())
psDCoutputInvertorVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputInvertorVoltage.setStatus(_A)
class _PsDCOutputDCOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),(_l,1),(_m,2),('disconnect',3)))
_PsDCOutputDCOutput_Type.__name__=_C
_PsDCOutputDCOutput_Object=MibScalar
psDCOutputDCOutput=_PsDCOutputDCOutput_Object((1,3,6,1,4,1,6050,1,6,14),_PsDCOutputDCOutput_Type())
psDCOutputDCOutput.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCOutputDCOutput.setStatus(_A)
_PsDCoutputSpare1_Type=Integer32
_PsDCoutputSpare1_Object=MibScalar
psDCoutputSpare1=_PsDCoutputSpare1_Object((1,3,6,1,4,1,6050,1,6,15),_PsDCoutputSpare1_Type())
psDCoutputSpare1.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSpare1.setStatus(_A)
_PsDCoutputSpare2_Type=Integer32
_PsDCoutputSpare2_Object=MibScalar
psDCoutputSpare2=_PsDCoutputSpare2_Object((1,3,6,1,4,1,6050,1,6,16),_PsDCoutputSpare2_Type())
psDCoutputSpare2.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSpare2.setStatus(_A)
_PsDCoutputSpare3_Type=Integer32
_PsDCoutputSpare3_Object=MibScalar
psDCoutputSpare3=_PsDCoutputSpare3_Object((1,3,6,1,4,1,6050,1,6,17),_PsDCoutputSpare3_Type())
psDCoutputSpare3.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSpare3.setStatus(_A)
_PsDCoutputSpare4_Type=Integer32
_PsDCoutputSpare4_Object=MibScalar
psDCoutputSpare4=_PsDCoutputSpare4_Object((1,3,6,1,4,1,6050,1,6,18),_PsDCoutputSpare4_Type())
psDCoutputSpare4.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSpare4.setStatus(_A)
_PsDCoutputSpare5_Type=Integer32
_PsDCoutputSpare5_Object=MibScalar
psDCoutputSpare5=_PsDCoutputSpare5_Object((1,3,6,1,4,1,6050,1,6,19),_PsDCoutputSpare5_Type())
psDCoutputSpare5.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSpare5.setStatus(_A)
_PsDCoutputSpare6_Type=Integer32
_PsDCoutputSpare6_Object=MibScalar
psDCoutputSpare6=_PsDCoutputSpare6_Object((1,3,6,1,4,1,6050,1,6,20),_PsDCoutputSpare6_Type())
psDCoutputSpare6.setMaxAccess(_D)
if mibBuilder.loadTexts:psDCoutputSpare6.setStatus(_A)
_PsContuctor_ObjectIdentity=ObjectIdentity
psContuctor=_PsContuctor_ObjectIdentity((1,3,6,1,4,1,6050,1,7))
class _PsContuctor1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor1_Type.__name__=_C
_PsContuctor1_Object=MibScalar
psContuctor1=_PsContuctor1_Object((1,3,6,1,4,1,6050,1,7,1),_PsContuctor1_Type())
psContuctor1.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor1.setStatus(_A)
class _PsContuctor2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor2_Type.__name__=_C
_PsContuctor2_Object=MibScalar
psContuctor2=_PsContuctor2_Object((1,3,6,1,4,1,6050,1,7,2),_PsContuctor2_Type())
psContuctor2.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor2.setStatus(_A)
class _PsContuctor3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor3_Type.__name__=_C
_PsContuctor3_Object=MibScalar
psContuctor3=_PsContuctor3_Object((1,3,6,1,4,1,6050,1,7,3),_PsContuctor3_Type())
psContuctor3.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor3.setStatus(_A)
class _PsContuctor4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor4_Type.__name__=_C
_PsContuctor4_Object=MibScalar
psContuctor4=_PsContuctor4_Object((1,3,6,1,4,1,6050,1,7,4),_PsContuctor4_Type())
psContuctor4.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor4.setStatus(_A)
class _PsContuctor5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor5_Type.__name__=_C
_PsContuctor5_Object=MibScalar
psContuctor5=_PsContuctor5_Object((1,3,6,1,4,1,6050,1,7,5),_PsContuctor5_Type())
psContuctor5.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor5.setStatus(_A)
class _PsContuctor6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor6_Type.__name__=_C
_PsContuctor6_Object=MibScalar
psContuctor6=_PsContuctor6_Object((1,3,6,1,4,1,6050,1,7,6),_PsContuctor6_Type())
psContuctor6.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor6.setStatus(_A)
class _PsContuctor7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor7_Type.__name__=_C
_PsContuctor7_Object=MibScalar
psContuctor7=_PsContuctor7_Object((1,3,6,1,4,1,6050,1,7,7),_PsContuctor7_Type())
psContuctor7.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor7.setStatus(_A)
class _PsContuctor8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor8_Type.__name__=_C
_PsContuctor8_Object=MibScalar
psContuctor8=_PsContuctor8_Object((1,3,6,1,4,1,6050,1,7,8),_PsContuctor8_Type())
psContuctor8.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor8.setStatus(_A)
class _PsContuctor9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor9_Type.__name__=_C
_PsContuctor9_Object=MibScalar
psContuctor9=_PsContuctor9_Object((1,3,6,1,4,1,6050,1,7,9),_PsContuctor9_Type())
psContuctor9.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor9.setStatus(_A)
class _PsContuctor10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_PsContuctor10_Type.__name__=_C
_PsContuctor10_Object=MibScalar
psContuctor10=_PsContuctor10_Object((1,3,6,1,4,1,6050,1,7,10),_PsContuctor10_Type())
psContuctor10.setMaxAccess(_B)
if mibBuilder.loadTexts:psContuctor10.setStatus(_A)
_PsDryContactTable_Object=MibTable
psDryContactTable=_PsDryContactTable_Object((1,3,6,1,4,1,6050,1,7,11))
if mibBuilder.loadTexts:psDryContactTable.setStatus(_A)
_PsDryContactorEntry_Object=MibTableRow
psDryContactorEntry=_PsDryContactorEntry_Object((1,3,6,1,4,1,6050,1,7,11,1))
psDryContactorEntry.setIndexNames((0,_N,_n))
if mibBuilder.loadTexts:psDryContactorEntry.setStatus(_A)
_PsDryContactorIndex_Type=Integer32
_PsDryContactorIndex_Object=MibTableColumn
psDryContactorIndex=_PsDryContactorIndex_Object((1,3,6,1,4,1,6050,1,7,11,1,1),_PsDryContactorIndex_Type())
psDryContactorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psDryContactorIndex.setStatus(_A)
class _PsDryContactorAlarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm1_Type.__name__=_C
_PsDryContactorAlarm1_Object=MibTableColumn
psDryContactorAlarm1=_PsDryContactorAlarm1_Object((1,3,6,1,4,1,6050,1,7,11,1,2),_PsDryContactorAlarm1_Type())
psDryContactorAlarm1.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm1.setStatus(_A)
class _PsDryContactorAlarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm2_Type.__name__=_C
_PsDryContactorAlarm2_Object=MibTableColumn
psDryContactorAlarm2=_PsDryContactorAlarm2_Object((1,3,6,1,4,1,6050,1,7,11,1,3),_PsDryContactorAlarm2_Type())
psDryContactorAlarm2.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm2.setStatus(_A)
class _PsDryContactorAlarm3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm3_Type.__name__=_C
_PsDryContactorAlarm3_Object=MibTableColumn
psDryContactorAlarm3=_PsDryContactorAlarm3_Object((1,3,6,1,4,1,6050,1,7,11,1,4),_PsDryContactorAlarm3_Type())
psDryContactorAlarm3.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm3.setStatus(_A)
class _PsDryContactorAlarm4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm4_Type.__name__=_C
_PsDryContactorAlarm4_Object=MibTableColumn
psDryContactorAlarm4=_PsDryContactorAlarm4_Object((1,3,6,1,4,1,6050,1,7,11,1,5),_PsDryContactorAlarm4_Type())
psDryContactorAlarm4.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm4.setStatus(_A)
class _PsDryContactorAlarm5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm5_Type.__name__=_C
_PsDryContactorAlarm5_Object=MibTableColumn
psDryContactorAlarm5=_PsDryContactorAlarm5_Object((1,3,6,1,4,1,6050,1,7,11,1,6),_PsDryContactorAlarm5_Type())
psDryContactorAlarm5.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm5.setStatus(_A)
class _PsDryContactorAlarm6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm6_Type.__name__=_C
_PsDryContactorAlarm6_Object=MibTableColumn
psDryContactorAlarm6=_PsDryContactorAlarm6_Object((1,3,6,1,4,1,6050,1,7,11,1,7),_PsDryContactorAlarm6_Type())
psDryContactorAlarm6.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm6.setStatus(_A)
class _PsDryContactorAlarm7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm7_Type.__name__=_C
_PsDryContactorAlarm7_Object=MibTableColumn
psDryContactorAlarm7=_PsDryContactorAlarm7_Object((1,3,6,1,4,1,6050,1,7,11,1,8),_PsDryContactorAlarm7_Type())
psDryContactorAlarm7.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm7.setStatus(_A)
class _PsDryContactorAlarm8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm8_Type.__name__=_C
_PsDryContactorAlarm8_Object=MibTableColumn
psDryContactorAlarm8=_PsDryContactorAlarm8_Object((1,3,6,1,4,1,6050,1,7,11,1,9),_PsDryContactorAlarm8_Type())
psDryContactorAlarm8.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm8.setStatus(_A)
class _PsDryContactorAlarm9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm9_Type.__name__=_C
_PsDryContactorAlarm9_Object=MibTableColumn
psDryContactorAlarm9=_PsDryContactorAlarm9_Object((1,3,6,1,4,1,6050,1,7,11,1,10),_PsDryContactorAlarm9_Type())
psDryContactorAlarm9.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm9.setStatus(_A)
class _PsDryContactorAlarm10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm10_Type.__name__=_C
_PsDryContactorAlarm10_Object=MibTableColumn
psDryContactorAlarm10=_PsDryContactorAlarm10_Object((1,3,6,1,4,1,6050,1,7,11,1,11),_PsDryContactorAlarm10_Type())
psDryContactorAlarm10.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm10.setStatus(_A)
class _PsDryContactorAlarm11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm11_Type.__name__=_C
_PsDryContactorAlarm11_Object=MibTableColumn
psDryContactorAlarm11=_PsDryContactorAlarm11_Object((1,3,6,1,4,1,6050,1,7,11,1,12),_PsDryContactorAlarm11_Type())
psDryContactorAlarm11.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm11.setStatus(_A)
class _PsDryContactorAlarm12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm12_Type.__name__=_C
_PsDryContactorAlarm12_Object=MibTableColumn
psDryContactorAlarm12=_PsDryContactorAlarm12_Object((1,3,6,1,4,1,6050,1,7,11,1,13),_PsDryContactorAlarm12_Type())
psDryContactorAlarm12.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm12.setStatus(_A)
class _PsDryContactorAlarm13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm13_Type.__name__=_C
_PsDryContactorAlarm13_Object=MibTableColumn
psDryContactorAlarm13=_PsDryContactorAlarm13_Object((1,3,6,1,4,1,6050,1,7,11,1,14),_PsDryContactorAlarm13_Type())
psDryContactorAlarm13.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm13.setStatus(_A)
class _PsDryContactorAlarm14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm14_Type.__name__=_C
_PsDryContactorAlarm14_Object=MibTableColumn
psDryContactorAlarm14=_PsDryContactorAlarm14_Object((1,3,6,1,4,1,6050,1,7,11,1,15),_PsDryContactorAlarm14_Type())
psDryContactorAlarm14.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm14.setStatus(_A)
class _PsDryContactorAlarm15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm15_Type.__name__=_C
_PsDryContactorAlarm15_Object=MibTableColumn
psDryContactorAlarm15=_PsDryContactorAlarm15_Object((1,3,6,1,4,1,6050,1,7,11,1,16),_PsDryContactorAlarm15_Type())
psDryContactorAlarm15.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm15.setStatus(_A)
class _PsDryContactorAlarm16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm16_Type.__name__=_C
_PsDryContactorAlarm16_Object=MibTableColumn
psDryContactorAlarm16=_PsDryContactorAlarm16_Object((1,3,6,1,4,1,6050,1,7,11,1,17),_PsDryContactorAlarm16_Type())
psDryContactorAlarm16.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm16.setStatus(_A)
class _PsDryContactorAlarm17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm17_Type.__name__=_C
_PsDryContactorAlarm17_Object=MibTableColumn
psDryContactorAlarm17=_PsDryContactorAlarm17_Object((1,3,6,1,4,1,6050,1,7,11,1,18),_PsDryContactorAlarm17_Type())
psDryContactorAlarm17.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm17.setStatus(_A)
class _PsDryContactorAlarm18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm18_Type.__name__=_C
_PsDryContactorAlarm18_Object=MibTableColumn
psDryContactorAlarm18=_PsDryContactorAlarm18_Object((1,3,6,1,4,1,6050,1,7,11,1,19),_PsDryContactorAlarm18_Type())
psDryContactorAlarm18.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm18.setStatus(_A)
class _PsDryContactorAlarm19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm19_Type.__name__=_C
_PsDryContactorAlarm19_Object=MibTableColumn
psDryContactorAlarm19=_PsDryContactorAlarm19_Object((1,3,6,1,4,1,6050,1,7,11,1,20),_PsDryContactorAlarm19_Type())
psDryContactorAlarm19.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm19.setStatus(_A)
class _PsDryContactorAlarm20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm20_Type.__name__=_C
_PsDryContactorAlarm20_Object=MibTableColumn
psDryContactorAlarm20=_PsDryContactorAlarm20_Object((1,3,6,1,4,1,6050,1,7,11,1,21),_PsDryContactorAlarm20_Type())
psDryContactorAlarm20.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm20.setStatus(_A)
class _PsDryContactorAlarm21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm21_Type.__name__=_C
_PsDryContactorAlarm21_Object=MibTableColumn
psDryContactorAlarm21=_PsDryContactorAlarm21_Object((1,3,6,1,4,1,6050,1,7,11,1,22),_PsDryContactorAlarm21_Type())
psDryContactorAlarm21.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm21.setStatus(_A)
class _PsDryContactorAlarm22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm22_Type.__name__=_C
_PsDryContactorAlarm22_Object=MibTableColumn
psDryContactorAlarm22=_PsDryContactorAlarm22_Object((1,3,6,1,4,1,6050,1,7,11,1,23),_PsDryContactorAlarm22_Type())
psDryContactorAlarm22.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm22.setStatus(_A)
class _PsDryContactorAlarm23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm23_Type.__name__=_C
_PsDryContactorAlarm23_Object=MibTableColumn
psDryContactorAlarm23=_PsDryContactorAlarm23_Object((1,3,6,1,4,1,6050,1,7,11,1,24),_PsDryContactorAlarm23_Type())
psDryContactorAlarm23.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm23.setStatus(_A)
class _PsDryContactorAlarm24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm24_Type.__name__=_C
_PsDryContactorAlarm24_Object=MibTableColumn
psDryContactorAlarm24=_PsDryContactorAlarm24_Object((1,3,6,1,4,1,6050,1,7,11,1,25),_PsDryContactorAlarm24_Type())
psDryContactorAlarm24.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm24.setStatus(_A)
class _PsDryContactorAlarm25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm25_Type.__name__=_C
_PsDryContactorAlarm25_Object=MibTableColumn
psDryContactorAlarm25=_PsDryContactorAlarm25_Object((1,3,6,1,4,1,6050,1,7,11,1,26),_PsDryContactorAlarm25_Type())
psDryContactorAlarm25.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm25.setStatus(_A)
class _PsDryContactorAlarm26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm26_Type.__name__=_C
_PsDryContactorAlarm26_Object=MibTableColumn
psDryContactorAlarm26=_PsDryContactorAlarm26_Object((1,3,6,1,4,1,6050,1,7,11,1,27),_PsDryContactorAlarm26_Type())
psDryContactorAlarm26.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm26.setStatus(_A)
class _PsDryContactorAlarm27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm27_Type.__name__=_C
_PsDryContactorAlarm27_Object=MibTableColumn
psDryContactorAlarm27=_PsDryContactorAlarm27_Object((1,3,6,1,4,1,6050,1,7,11,1,28),_PsDryContactorAlarm27_Type())
psDryContactorAlarm27.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm27.setStatus(_A)
class _PsDryContactorAlarm28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm28_Type.__name__=_C
_PsDryContactorAlarm28_Object=MibTableColumn
psDryContactorAlarm28=_PsDryContactorAlarm28_Object((1,3,6,1,4,1,6050,1,7,11,1,29),_PsDryContactorAlarm28_Type())
psDryContactorAlarm28.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm28.setStatus(_A)
class _PsDryContactorAlarm29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm29_Type.__name__=_C
_PsDryContactorAlarm29_Object=MibTableColumn
psDryContactorAlarm29=_PsDryContactorAlarm29_Object((1,3,6,1,4,1,6050,1,7,11,1,30),_PsDryContactorAlarm29_Type())
psDryContactorAlarm29.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm29.setStatus(_A)
class _PsDryContactorAlarm30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm30_Type.__name__=_C
_PsDryContactorAlarm30_Object=MibTableColumn
psDryContactorAlarm30=_PsDryContactorAlarm30_Object((1,3,6,1,4,1,6050,1,7,11,1,31),_PsDryContactorAlarm30_Type())
psDryContactorAlarm30.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm30.setStatus(_A)
class _PsDryContactorAlarm31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm31_Type.__name__=_C
_PsDryContactorAlarm31_Object=MibTableColumn
psDryContactorAlarm31=_PsDryContactorAlarm31_Object((1,3,6,1,4,1,6050,1,7,11,1,32),_PsDryContactorAlarm31_Type())
psDryContactorAlarm31.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm31.setStatus(_A)
class _PsDryContactorAlarm32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactorAlarm32_Type.__name__=_C
_PsDryContactorAlarm32_Object=MibTableColumn
psDryContactorAlarm32=_PsDryContactorAlarm32_Object((1,3,6,1,4,1,6050,1,7,11,1,33),_PsDryContactorAlarm32_Type())
psDryContactorAlarm32.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactorAlarm32.setStatus(_A)
_PsDryContactStatus_Type=Integer32
_PsDryContactStatus_Object=MibScalar
psDryContactStatus=_PsDryContactStatus_Object((1,3,6,1,4,1,6050,1,7,12),_PsDryContactStatus_Type())
psDryContactStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psDryContactStatus.setStatus(_A)
_PsDryContact1Table_Object=MibTable
psDryContact1Table=_PsDryContact1Table_Object((1,3,6,1,4,1,6050,1,7,13))
if mibBuilder.loadTexts:psDryContact1Table.setStatus(_A)
_PsDryContactor1Entry_Object=MibTableRow
psDryContactor1Entry=_PsDryContactor1Entry_Object((1,3,6,1,4,1,6050,1,7,13,1))
psDryContactor1Entry.setIndexNames((0,_N,_o))
if mibBuilder.loadTexts:psDryContactor1Entry.setStatus(_A)
_PsDryContactor1Index_Type=Integer32
_PsDryContactor1Index_Object=MibTableColumn
psDryContactor1Index=_PsDryContactor1Index_Object((1,3,6,1,4,1,6050,1,7,13,1,1),_PsDryContactor1Index_Type())
psDryContactor1Index.setMaxAccess(_D)
if mibBuilder.loadTexts:psDryContactor1Index.setStatus(_A)
class _PsDryContactor1Alarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm1_Type.__name__=_C
_PsDryContactor1Alarm1_Object=MibTableColumn
psDryContactor1Alarm1=_PsDryContactor1Alarm1_Object((1,3,6,1,4,1,6050,1,7,13,1,2),_PsDryContactor1Alarm1_Type())
psDryContactor1Alarm1.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm1.setStatus(_A)
class _PsDryContactor1Alarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm2_Type.__name__=_C
_PsDryContactor1Alarm2_Object=MibTableColumn
psDryContactor1Alarm2=_PsDryContactor1Alarm2_Object((1,3,6,1,4,1,6050,1,7,13,1,3),_PsDryContactor1Alarm2_Type())
psDryContactor1Alarm2.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm2.setStatus(_A)
class _PsDryContactor1Alarm3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm3_Type.__name__=_C
_PsDryContactor1Alarm3_Object=MibTableColumn
psDryContactor1Alarm3=_PsDryContactor1Alarm3_Object((1,3,6,1,4,1,6050,1,7,13,1,4),_PsDryContactor1Alarm3_Type())
psDryContactor1Alarm3.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm3.setStatus(_A)
class _PsDryContactor1Alarm4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm4_Type.__name__=_C
_PsDryContactor1Alarm4_Object=MibTableColumn
psDryContactor1Alarm4=_PsDryContactor1Alarm4_Object((1,3,6,1,4,1,6050,1,7,13,1,5),_PsDryContactor1Alarm4_Type())
psDryContactor1Alarm4.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm4.setStatus(_A)
class _PsDryContactor1Alarm5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm5_Type.__name__=_C
_PsDryContactor1Alarm5_Object=MibTableColumn
psDryContactor1Alarm5=_PsDryContactor1Alarm5_Object((1,3,6,1,4,1,6050,1,7,13,1,6),_PsDryContactor1Alarm5_Type())
psDryContactor1Alarm5.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm5.setStatus(_A)
class _PsDryContactor1Alarm6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm6_Type.__name__=_C
_PsDryContactor1Alarm6_Object=MibTableColumn
psDryContactor1Alarm6=_PsDryContactor1Alarm6_Object((1,3,6,1,4,1,6050,1,7,13,1,7),_PsDryContactor1Alarm6_Type())
psDryContactor1Alarm6.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm6.setStatus(_A)
class _PsDryContactor1Alarm7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm7_Type.__name__=_C
_PsDryContactor1Alarm7_Object=MibTableColumn
psDryContactor1Alarm7=_PsDryContactor1Alarm7_Object((1,3,6,1,4,1,6050,1,7,13,1,8),_PsDryContactor1Alarm7_Type())
psDryContactor1Alarm7.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm7.setStatus(_A)
class _PsDryContactor1Alarm8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm8_Type.__name__=_C
_PsDryContactor1Alarm8_Object=MibTableColumn
psDryContactor1Alarm8=_PsDryContactor1Alarm8_Object((1,3,6,1,4,1,6050,1,7,13,1,9),_PsDryContactor1Alarm8_Type())
psDryContactor1Alarm8.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm8.setStatus(_A)
class _PsDryContactor1Alarm9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm9_Type.__name__=_C
_PsDryContactor1Alarm9_Object=MibTableColumn
psDryContactor1Alarm9=_PsDryContactor1Alarm9_Object((1,3,6,1,4,1,6050,1,7,13,1,10),_PsDryContactor1Alarm9_Type())
psDryContactor1Alarm9.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm9.setStatus(_A)
class _PsDryContactor1Alarm10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm10_Type.__name__=_C
_PsDryContactor1Alarm10_Object=MibTableColumn
psDryContactor1Alarm10=_PsDryContactor1Alarm10_Object((1,3,6,1,4,1,6050,1,7,13,1,11),_PsDryContactor1Alarm10_Type())
psDryContactor1Alarm10.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm10.setStatus(_A)
class _PsDryContactor1Alarm11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm11_Type.__name__=_C
_PsDryContactor1Alarm11_Object=MibTableColumn
psDryContactor1Alarm11=_PsDryContactor1Alarm11_Object((1,3,6,1,4,1,6050,1,7,13,1,12),_PsDryContactor1Alarm11_Type())
psDryContactor1Alarm11.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm11.setStatus(_A)
class _PsDryContactor1Alarm12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm12_Type.__name__=_C
_PsDryContactor1Alarm12_Object=MibTableColumn
psDryContactor1Alarm12=_PsDryContactor1Alarm12_Object((1,3,6,1,4,1,6050,1,7,13,1,13),_PsDryContactor1Alarm12_Type())
psDryContactor1Alarm12.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm12.setStatus(_A)
class _PsDryContactor1Alarm13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm13_Type.__name__=_C
_PsDryContactor1Alarm13_Object=MibTableColumn
psDryContactor1Alarm13=_PsDryContactor1Alarm13_Object((1,3,6,1,4,1,6050,1,7,13,1,14),_PsDryContactor1Alarm13_Type())
psDryContactor1Alarm13.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm13.setStatus(_A)
class _PsDryContactor1Alarm14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm14_Type.__name__=_C
_PsDryContactor1Alarm14_Object=MibTableColumn
psDryContactor1Alarm14=_PsDryContactor1Alarm14_Object((1,3,6,1,4,1,6050,1,7,13,1,15),_PsDryContactor1Alarm14_Type())
psDryContactor1Alarm14.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm14.setStatus(_A)
class _PsDryContactor1Alarm15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm15_Type.__name__=_C
_PsDryContactor1Alarm15_Object=MibTableColumn
psDryContactor1Alarm15=_PsDryContactor1Alarm15_Object((1,3,6,1,4,1,6050,1,7,13,1,16),_PsDryContactor1Alarm15_Type())
psDryContactor1Alarm15.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm15.setStatus(_A)
class _PsDryContactor1Alarm16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm16_Type.__name__=_C
_PsDryContactor1Alarm16_Object=MibTableColumn
psDryContactor1Alarm16=_PsDryContactor1Alarm16_Object((1,3,6,1,4,1,6050,1,7,13,1,17),_PsDryContactor1Alarm16_Type())
psDryContactor1Alarm16.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm16.setStatus(_A)
class _PsDryContactor1Alarm17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm17_Type.__name__=_C
_PsDryContactor1Alarm17_Object=MibTableColumn
psDryContactor1Alarm17=_PsDryContactor1Alarm17_Object((1,3,6,1,4,1,6050,1,7,13,1,18),_PsDryContactor1Alarm17_Type())
psDryContactor1Alarm17.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm17.setStatus(_A)
class _PsDryContactor1Alarm18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm18_Type.__name__=_C
_PsDryContactor1Alarm18_Object=MibTableColumn
psDryContactor1Alarm18=_PsDryContactor1Alarm18_Object((1,3,6,1,4,1,6050,1,7,13,1,19),_PsDryContactor1Alarm18_Type())
psDryContactor1Alarm18.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm18.setStatus(_A)
class _PsDryContactor1Alarm19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm19_Type.__name__=_C
_PsDryContactor1Alarm19_Object=MibTableColumn
psDryContactor1Alarm19=_PsDryContactor1Alarm19_Object((1,3,6,1,4,1,6050,1,7,13,1,20),_PsDryContactor1Alarm19_Type())
psDryContactor1Alarm19.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm19.setStatus(_A)
class _PsDryContactor1Alarm20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm20_Type.__name__=_C
_PsDryContactor1Alarm20_Object=MibTableColumn
psDryContactor1Alarm20=_PsDryContactor1Alarm20_Object((1,3,6,1,4,1,6050,1,7,13,1,21),_PsDryContactor1Alarm20_Type())
psDryContactor1Alarm20.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm20.setStatus(_A)
class _PsDryContactor1Alarm21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm21_Type.__name__=_C
_PsDryContactor1Alarm21_Object=MibTableColumn
psDryContactor1Alarm21=_PsDryContactor1Alarm21_Object((1,3,6,1,4,1,6050,1,7,13,1,22),_PsDryContactor1Alarm21_Type())
psDryContactor1Alarm21.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm21.setStatus(_A)
class _PsDryContactor1Alarm22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm22_Type.__name__=_C
_PsDryContactor1Alarm22_Object=MibTableColumn
psDryContactor1Alarm22=_PsDryContactor1Alarm22_Object((1,3,6,1,4,1,6050,1,7,13,1,23),_PsDryContactor1Alarm22_Type())
psDryContactor1Alarm22.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm22.setStatus(_A)
class _PsDryContactor1Alarm23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm23_Type.__name__=_C
_PsDryContactor1Alarm23_Object=MibTableColumn
psDryContactor1Alarm23=_PsDryContactor1Alarm23_Object((1,3,6,1,4,1,6050,1,7,13,1,24),_PsDryContactor1Alarm23_Type())
psDryContactor1Alarm23.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm23.setStatus(_A)
class _PsDryContactor1Alarm24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm24_Type.__name__=_C
_PsDryContactor1Alarm24_Object=MibTableColumn
psDryContactor1Alarm24=_PsDryContactor1Alarm24_Object((1,3,6,1,4,1,6050,1,7,13,1,25),_PsDryContactor1Alarm24_Type())
psDryContactor1Alarm24.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm24.setStatus(_A)
class _PsDryContactor1Alarm25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm25_Type.__name__=_C
_PsDryContactor1Alarm25_Object=MibTableColumn
psDryContactor1Alarm25=_PsDryContactor1Alarm25_Object((1,3,6,1,4,1,6050,1,7,13,1,26),_PsDryContactor1Alarm25_Type())
psDryContactor1Alarm25.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm25.setStatus(_A)
class _PsDryContactor1Alarm26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm26_Type.__name__=_C
_PsDryContactor1Alarm26_Object=MibTableColumn
psDryContactor1Alarm26=_PsDryContactor1Alarm26_Object((1,3,6,1,4,1,6050,1,7,13,1,27),_PsDryContactor1Alarm26_Type())
psDryContactor1Alarm26.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm26.setStatus(_A)
class _PsDryContactor1Alarm27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm27_Type.__name__=_C
_PsDryContactor1Alarm27_Object=MibTableColumn
psDryContactor1Alarm27=_PsDryContactor1Alarm27_Object((1,3,6,1,4,1,6050,1,7,13,1,28),_PsDryContactor1Alarm27_Type())
psDryContactor1Alarm27.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm27.setStatus(_A)
class _PsDryContactor1Alarm28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm28_Type.__name__=_C
_PsDryContactor1Alarm28_Object=MibTableColumn
psDryContactor1Alarm28=_PsDryContactor1Alarm28_Object((1,3,6,1,4,1,6050,1,7,13,1,29),_PsDryContactor1Alarm28_Type())
psDryContactor1Alarm28.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm28.setStatus(_A)
class _PsDryContactor1Alarm29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm29_Type.__name__=_C
_PsDryContactor1Alarm29_Object=MibTableColumn
psDryContactor1Alarm29=_PsDryContactor1Alarm29_Object((1,3,6,1,4,1,6050,1,7,13,1,30),_PsDryContactor1Alarm29_Type())
psDryContactor1Alarm29.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm29.setStatus(_A)
class _PsDryContactor1Alarm30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm30_Type.__name__=_C
_PsDryContactor1Alarm30_Object=MibTableColumn
psDryContactor1Alarm30=_PsDryContactor1Alarm30_Object((1,3,6,1,4,1,6050,1,7,13,1,31),_PsDryContactor1Alarm30_Type())
psDryContactor1Alarm30.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm30.setStatus(_A)
class _PsDryContactor1Alarm31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm31_Type.__name__=_C
_PsDryContactor1Alarm31_Object=MibTableColumn
psDryContactor1Alarm31=_PsDryContactor1Alarm31_Object((1,3,6,1,4,1,6050,1,7,13,1,32),_PsDryContactor1Alarm31_Type())
psDryContactor1Alarm31.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm31.setStatus(_A)
class _PsDryContactor1Alarm32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor1Alarm32_Type.__name__=_C
_PsDryContactor1Alarm32_Object=MibTableColumn
psDryContactor1Alarm32=_PsDryContactor1Alarm32_Object((1,3,6,1,4,1,6050,1,7,13,1,33),_PsDryContactor1Alarm32_Type())
psDryContactor1Alarm32.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor1Alarm32.setStatus(_A)
_PsDryContact1Status_Type=Integer32
_PsDryContact1Status_Object=MibScalar
psDryContact1Status=_PsDryContact1Status_Object((1,3,6,1,4,1,6050,1,7,14),_PsDryContact1Status_Type())
psDryContact1Status.setMaxAccess(_D)
if mibBuilder.loadTexts:psDryContact1Status.setStatus(_A)
_PsDryContact2Table_Object=MibTable
psDryContact2Table=_PsDryContact2Table_Object((1,3,6,1,4,1,6050,1,7,15))
if mibBuilder.loadTexts:psDryContact2Table.setStatus(_A)
_PsDryContactor2Entry_Object=MibTableRow
psDryContactor2Entry=_PsDryContactor2Entry_Object((1,3,6,1,4,1,6050,1,7,15,1))
psDryContactor2Entry.setIndexNames((0,_N,_p))
if mibBuilder.loadTexts:psDryContactor2Entry.setStatus(_A)
_PsDryContactor2Index_Type=Integer32
_PsDryContactor2Index_Object=MibTableColumn
psDryContactor2Index=_PsDryContactor2Index_Object((1,3,6,1,4,1,6050,1,7,15,1,1),_PsDryContactor2Index_Type())
psDryContactor2Index.setMaxAccess(_D)
if mibBuilder.loadTexts:psDryContactor2Index.setStatus(_A)
class _PsDryContactor2Alarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm1_Type.__name__=_C
_PsDryContactor2Alarm1_Object=MibTableColumn
psDryContactor2Alarm1=_PsDryContactor2Alarm1_Object((1,3,6,1,4,1,6050,1,7,15,1,2),_PsDryContactor2Alarm1_Type())
psDryContactor2Alarm1.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm1.setStatus(_A)
class _PsDryContactor2Alarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm2_Type.__name__=_C
_PsDryContactor2Alarm2_Object=MibTableColumn
psDryContactor2Alarm2=_PsDryContactor2Alarm2_Object((1,3,6,1,4,1,6050,1,7,15,1,3),_PsDryContactor2Alarm2_Type())
psDryContactor2Alarm2.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm2.setStatus(_A)
class _PsDryContactor2Alarm3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm3_Type.__name__=_C
_PsDryContactor2Alarm3_Object=MibTableColumn
psDryContactor2Alarm3=_PsDryContactor2Alarm3_Object((1,3,6,1,4,1,6050,1,7,15,1,4),_PsDryContactor2Alarm3_Type())
psDryContactor2Alarm3.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm3.setStatus(_A)
class _PsDryContactor2Alarm4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm4_Type.__name__=_C
_PsDryContactor2Alarm4_Object=MibTableColumn
psDryContactor2Alarm4=_PsDryContactor2Alarm4_Object((1,3,6,1,4,1,6050,1,7,15,1,5),_PsDryContactor2Alarm4_Type())
psDryContactor2Alarm4.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm4.setStatus(_A)
class _PsDryContactor2Alarm5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm5_Type.__name__=_C
_PsDryContactor2Alarm5_Object=MibTableColumn
psDryContactor2Alarm5=_PsDryContactor2Alarm5_Object((1,3,6,1,4,1,6050,1,7,15,1,6),_PsDryContactor2Alarm5_Type())
psDryContactor2Alarm5.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm5.setStatus(_A)
class _PsDryContactor2Alarm6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm6_Type.__name__=_C
_PsDryContactor2Alarm6_Object=MibTableColumn
psDryContactor2Alarm6=_PsDryContactor2Alarm6_Object((1,3,6,1,4,1,6050,1,7,15,1,7),_PsDryContactor2Alarm6_Type())
psDryContactor2Alarm6.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm6.setStatus(_A)
class _PsDryContactor2Alarm7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm7_Type.__name__=_C
_PsDryContactor2Alarm7_Object=MibTableColumn
psDryContactor2Alarm7=_PsDryContactor2Alarm7_Object((1,3,6,1,4,1,6050,1,7,15,1,8),_PsDryContactor2Alarm7_Type())
psDryContactor2Alarm7.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm7.setStatus(_A)
class _PsDryContactor2Alarm8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm8_Type.__name__=_C
_PsDryContactor2Alarm8_Object=MibTableColumn
psDryContactor2Alarm8=_PsDryContactor2Alarm8_Object((1,3,6,1,4,1,6050,1,7,15,1,9),_PsDryContactor2Alarm8_Type())
psDryContactor2Alarm8.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm8.setStatus(_A)
class _PsDryContactor2Alarm9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm9_Type.__name__=_C
_PsDryContactor2Alarm9_Object=MibTableColumn
psDryContactor2Alarm9=_PsDryContactor2Alarm9_Object((1,3,6,1,4,1,6050,1,7,15,1,10),_PsDryContactor2Alarm9_Type())
psDryContactor2Alarm9.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm9.setStatus(_A)
class _PsDryContactor2Alarm10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm10_Type.__name__=_C
_PsDryContactor2Alarm10_Object=MibTableColumn
psDryContactor2Alarm10=_PsDryContactor2Alarm10_Object((1,3,6,1,4,1,6050,1,7,15,1,11),_PsDryContactor2Alarm10_Type())
psDryContactor2Alarm10.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm10.setStatus(_A)
class _PsDryContactor2Alarm11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm11_Type.__name__=_C
_PsDryContactor2Alarm11_Object=MibTableColumn
psDryContactor2Alarm11=_PsDryContactor2Alarm11_Object((1,3,6,1,4,1,6050,1,7,15,1,12),_PsDryContactor2Alarm11_Type())
psDryContactor2Alarm11.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm11.setStatus(_A)
class _PsDryContactor2Alarm12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm12_Type.__name__=_C
_PsDryContactor2Alarm12_Object=MibTableColumn
psDryContactor2Alarm12=_PsDryContactor2Alarm12_Object((1,3,6,1,4,1,6050,1,7,15,1,13),_PsDryContactor2Alarm12_Type())
psDryContactor2Alarm12.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm12.setStatus(_A)
class _PsDryContactor2Alarm13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm13_Type.__name__=_C
_PsDryContactor2Alarm13_Object=MibTableColumn
psDryContactor2Alarm13=_PsDryContactor2Alarm13_Object((1,3,6,1,4,1,6050,1,7,15,1,14),_PsDryContactor2Alarm13_Type())
psDryContactor2Alarm13.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm13.setStatus(_A)
class _PsDryContactor2Alarm14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm14_Type.__name__=_C
_PsDryContactor2Alarm14_Object=MibTableColumn
psDryContactor2Alarm14=_PsDryContactor2Alarm14_Object((1,3,6,1,4,1,6050,1,7,15,1,15),_PsDryContactor2Alarm14_Type())
psDryContactor2Alarm14.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm14.setStatus(_A)
class _PsDryContactor2Alarm15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm15_Type.__name__=_C
_PsDryContactor2Alarm15_Object=MibTableColumn
psDryContactor2Alarm15=_PsDryContactor2Alarm15_Object((1,3,6,1,4,1,6050,1,7,15,1,16),_PsDryContactor2Alarm15_Type())
psDryContactor2Alarm15.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm15.setStatus(_A)
class _PsDryContactor2Alarm16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm16_Type.__name__=_C
_PsDryContactor2Alarm16_Object=MibTableColumn
psDryContactor2Alarm16=_PsDryContactor2Alarm16_Object((1,3,6,1,4,1,6050,1,7,15,1,17),_PsDryContactor2Alarm16_Type())
psDryContactor2Alarm16.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm16.setStatus(_A)
class _PsDryContactor2Alarm17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm17_Type.__name__=_C
_PsDryContactor2Alarm17_Object=MibTableColumn
psDryContactor2Alarm17=_PsDryContactor2Alarm17_Object((1,3,6,1,4,1,6050,1,7,15,1,18),_PsDryContactor2Alarm17_Type())
psDryContactor2Alarm17.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm17.setStatus(_A)
class _PsDryContactor2Alarm18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm18_Type.__name__=_C
_PsDryContactor2Alarm18_Object=MibTableColumn
psDryContactor2Alarm18=_PsDryContactor2Alarm18_Object((1,3,6,1,4,1,6050,1,7,15,1,19),_PsDryContactor2Alarm18_Type())
psDryContactor2Alarm18.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm18.setStatus(_A)
class _PsDryContactor2Alarm19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm19_Type.__name__=_C
_PsDryContactor2Alarm19_Object=MibTableColumn
psDryContactor2Alarm19=_PsDryContactor2Alarm19_Object((1,3,6,1,4,1,6050,1,7,15,1,20),_PsDryContactor2Alarm19_Type())
psDryContactor2Alarm19.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm19.setStatus(_A)
class _PsDryContactor2Alarm20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm20_Type.__name__=_C
_PsDryContactor2Alarm20_Object=MibTableColumn
psDryContactor2Alarm20=_PsDryContactor2Alarm20_Object((1,3,6,1,4,1,6050,1,7,15,1,21),_PsDryContactor2Alarm20_Type())
psDryContactor2Alarm20.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm20.setStatus(_A)
class _PsDryContactor2Alarm21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm21_Type.__name__=_C
_PsDryContactor2Alarm21_Object=MibTableColumn
psDryContactor2Alarm21=_PsDryContactor2Alarm21_Object((1,3,6,1,4,1,6050,1,7,15,1,22),_PsDryContactor2Alarm21_Type())
psDryContactor2Alarm21.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm21.setStatus(_A)
class _PsDryContactor2Alarm22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm22_Type.__name__=_C
_PsDryContactor2Alarm22_Object=MibTableColumn
psDryContactor2Alarm22=_PsDryContactor2Alarm22_Object((1,3,6,1,4,1,6050,1,7,15,1,23),_PsDryContactor2Alarm22_Type())
psDryContactor2Alarm22.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm22.setStatus(_A)
class _PsDryContactor2Alarm23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm23_Type.__name__=_C
_PsDryContactor2Alarm23_Object=MibTableColumn
psDryContactor2Alarm23=_PsDryContactor2Alarm23_Object((1,3,6,1,4,1,6050,1,7,15,1,24),_PsDryContactor2Alarm23_Type())
psDryContactor2Alarm23.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm23.setStatus(_A)
class _PsDryContactor2Alarm24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm24_Type.__name__=_C
_PsDryContactor2Alarm24_Object=MibTableColumn
psDryContactor2Alarm24=_PsDryContactor2Alarm24_Object((1,3,6,1,4,1,6050,1,7,15,1,25),_PsDryContactor2Alarm24_Type())
psDryContactor2Alarm24.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm24.setStatus(_A)
class _PsDryContactor2Alarm25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm25_Type.__name__=_C
_PsDryContactor2Alarm25_Object=MibTableColumn
psDryContactor2Alarm25=_PsDryContactor2Alarm25_Object((1,3,6,1,4,1,6050,1,7,15,1,26),_PsDryContactor2Alarm25_Type())
psDryContactor2Alarm25.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm25.setStatus(_A)
class _PsDryContactor2Alarm26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm26_Type.__name__=_C
_PsDryContactor2Alarm26_Object=MibTableColumn
psDryContactor2Alarm26=_PsDryContactor2Alarm26_Object((1,3,6,1,4,1,6050,1,7,15,1,27),_PsDryContactor2Alarm26_Type())
psDryContactor2Alarm26.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm26.setStatus(_A)
class _PsDryContactor2Alarm27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm27_Type.__name__=_C
_PsDryContactor2Alarm27_Object=MibTableColumn
psDryContactor2Alarm27=_PsDryContactor2Alarm27_Object((1,3,6,1,4,1,6050,1,7,15,1,28),_PsDryContactor2Alarm27_Type())
psDryContactor2Alarm27.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm27.setStatus(_A)
class _PsDryContactor2Alarm28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm28_Type.__name__=_C
_PsDryContactor2Alarm28_Object=MibTableColumn
psDryContactor2Alarm28=_PsDryContactor2Alarm28_Object((1,3,6,1,4,1,6050,1,7,15,1,29),_PsDryContactor2Alarm28_Type())
psDryContactor2Alarm28.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm28.setStatus(_A)
class _PsDryContactor2Alarm29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm29_Type.__name__=_C
_PsDryContactor2Alarm29_Object=MibTableColumn
psDryContactor2Alarm29=_PsDryContactor2Alarm29_Object((1,3,6,1,4,1,6050,1,7,15,1,30),_PsDryContactor2Alarm29_Type())
psDryContactor2Alarm29.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm29.setStatus(_A)
class _PsDryContactor2Alarm30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm30_Type.__name__=_C
_PsDryContactor2Alarm30_Object=MibTableColumn
psDryContactor2Alarm30=_PsDryContactor2Alarm30_Object((1,3,6,1,4,1,6050,1,7,15,1,31),_PsDryContactor2Alarm30_Type())
psDryContactor2Alarm30.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm30.setStatus(_A)
class _PsDryContactor2Alarm31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm31_Type.__name__=_C
_PsDryContactor2Alarm31_Object=MibTableColumn
psDryContactor2Alarm31=_PsDryContactor2Alarm31_Object((1,3,6,1,4,1,6050,1,7,15,1,32),_PsDryContactor2Alarm31_Type())
psDryContactor2Alarm31.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm31.setStatus(_A)
class _PsDryContactor2Alarm32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PsDryContactor2Alarm32_Type.__name__=_C
_PsDryContactor2Alarm32_Object=MibTableColumn
psDryContactor2Alarm32=_PsDryContactor2Alarm32_Object((1,3,6,1,4,1,6050,1,7,15,1,33),_PsDryContactor2Alarm32_Type())
psDryContactor2Alarm32.setMaxAccess(_B)
if mibBuilder.loadTexts:psDryContactor2Alarm32.setStatus(_A)
_PsDryContact2Status_Type=Integer32
_PsDryContact2Status_Object=MibScalar
psDryContact2Status=_PsDryContact2Status_Object((1,3,6,1,4,1,6050,1,7,16),_PsDryContact2Status_Type())
psDryContact2Status.setMaxAccess(_D)
if mibBuilder.loadTexts:psDryContact2Status.setStatus(_A)
_PsConfNominal_ObjectIdentity=ObjectIdentity
psConfNominal=_PsConfNominal_ObjectIdentity((1,3,6,1,4,1,6050,1,8))
class _PsConfEnableCurrentLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PsConfEnableCurrentLimit_Type.__name__=_C
_PsConfEnableCurrentLimit_Object=MibScalar
psConfEnableCurrentLimit=_PsConfEnableCurrentLimit_Object((1,3,6,1,4,1,6050,1,8,1),_PsConfEnableCurrentLimit_Type())
psConfEnableCurrentLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEnableCurrentLimit.setStatus(_A)
class _PsConfEnablePeriodicEqualize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PsConfEnablePeriodicEqualize_Type.__name__=_C
_PsConfEnablePeriodicEqualize_Object=MibScalar
psConfEnablePeriodicEqualize=_PsConfEnablePeriodicEqualize_Object((1,3,6,1,4,1,6050,1,8,2),_PsConfEnablePeriodicEqualize_Type())
psConfEnablePeriodicEqualize.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEnablePeriodicEqualize.setStatus(_A)
_PsConfGHighTempAlarm_Type=Integer32
_PsConfGHighTempAlarm_Object=MibScalar
psConfGHighTempAlarm=_PsConfGHighTempAlarm_Object((1,3,6,1,4,1,6050,1,8,3),_PsConfGHighTempAlarm_Type())
psConfGHighTempAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfGHighTempAlarm.setStatus(_A)
class _PsConfLowTempAlarmSign_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_e,1)))
_PsConfLowTempAlarmSign_Type.__name__=_C
_PsConfLowTempAlarmSign_Object=MibScalar
psConfLowTempAlarmSign=_PsConfLowTempAlarmSign_Object((1,3,6,1,4,1,6050,1,8,4),_PsConfLowTempAlarmSign_Type())
psConfLowTempAlarmSign.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfLowTempAlarmSign.setStatus(_A)
_PsConfLowTempAlarm_Type=Integer32
_PsConfLowTempAlarm_Object=MibScalar
psConfLowTempAlarm=_PsConfLowTempAlarm_Object((1,3,6,1,4,1,6050,1,8,5),_PsConfLowTempAlarm_Type())
psConfLowTempAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfLowTempAlarm.setStatus(_A)
_PsConfTemperatureCoefficient_Type=Integer32
_PsConfTemperatureCoefficient_Object=MibScalar
psConfTemperatureCoefficient=_PsConfTemperatureCoefficient_Object((1,3,6,1,4,1,6050,1,8,6),_PsConfTemperatureCoefficient_Type())
psConfTemperatureCoefficient.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfTemperatureCoefficient.setStatus(_A)
_PsConfNumOfInvertors_Type=Integer32
_PsConfNumOfInvertors_Object=MibScalar
psConfNumOfInvertors=_PsConfNumOfInvertors_Object((1,3,6,1,4,1,6050,1,8,7),_PsConfNumOfInvertors_Type())
psConfNumOfInvertors.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNumOfInvertors.setStatus(_A)
_PsConfNumOfRectifiers_Type=Integer32
_PsConfNumOfRectifiers_Object=MibScalar
psConfNumOfRectifiers=_PsConfNumOfRectifiers_Object((1,3,6,1,4,1,6050,1,8,8),_PsConfNumOfRectifiers_Type())
psConfNumOfRectifiers.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNumOfRectifiers.setStatus(_A)
_PsConfACHigh_Type=Integer32
_PsConfACHigh_Object=MibScalar
psConfACHigh=_PsConfACHigh_Object((1,3,6,1,4,1,6050,1,8,9),_PsConfACHigh_Type())
psConfACHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfACHigh.setStatus(_A)
_PsConfACLow_Type=Integer32
_PsConfACLow_Object=MibScalar
psConfACLow=_PsConfACLow_Object((1,3,6,1,4,1,6050,1,8,10),_PsConfACLow_Type())
psConfACLow.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfACLow.setStatus(_A)
_PsConfCurrentLimit_Type=Integer32
_PsConfCurrentLimit_Object=MibScalar
psConfCurrentLimit=_PsConfCurrentLimit_Object((1,3,6,1,4,1,6050,1,8,11),_PsConfCurrentLimit_Type())
psConfCurrentLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfCurrentLimit.setStatus(_A)
_PsConfHIA_Type=Integer32
_PsConfHIA_Object=MibScalar
psConfHIA=_PsConfHIA_Object((1,3,6,1,4,1,6050,1,8,12),_PsConfHIA_Type())
psConfHIA.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfHIA.setStatus(_A)
_PsConfBDOC_Type=Integer32
_PsConfBDOC_Object=MibScalar
psConfBDOC=_PsConfBDOC_Object((1,3,6,1,4,1,6050,1,8,13),_PsConfBDOC_Type())
psConfBDOC.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfBDOC.setStatus(_A)
_PsConfBatteryNominalCapacity_Type=Integer32
_PsConfBatteryNominalCapacity_Object=MibScalar
psConfBatteryNominalCapacity=_PsConfBatteryNominalCapacity_Object((1,3,6,1,4,1,6050,1,8,14),_PsConfBatteryNominalCapacity_Type())
psConfBatteryNominalCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfBatteryNominalCapacity.setStatus(_A)
_PsConfEqualStopTime_Type=Integer32
_PsConfEqualStopTime_Object=MibScalar
psConfEqualStopTime=_PsConfEqualStopTime_Object((1,3,6,1,4,1,6050,1,8,15),_PsConfEqualStopTime_Type())
psConfEqualStopTime.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqualStopTime.setStatus(_A)
_PsConfEqualStopCurrent_Type=Integer32
_PsConfEqualStopCurrent_Object=MibScalar
psConfEqualStopCurrent=_PsConfEqualStopCurrent_Object((1,3,6,1,4,1,6050,1,8,16),_PsConfEqualStopCurrent_Type())
psConfEqualStopCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqualStopCurrent.setStatus(_A)
_PsConfEqualPeriod_Type=Integer32
_PsConfEqualPeriod_Object=MibScalar
psConfEqualPeriod=_PsConfEqualPeriod_Object((1,3,6,1,4,1,6050,1,8,17),_PsConfEqualPeriod_Type())
psConfEqualPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqualPeriod.setStatus(_A)
_PsConfEqualStartCurrent_Type=Integer32
_PsConfEqualStartCurrent_Object=MibScalar
psConfEqualStartCurrent=_PsConfEqualStartCurrent_Object((1,3,6,1,4,1,6050,1,8,18),_PsConfEqualStartCurrent_Type())
psConfEqualStartCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqualStartCurrent.setStatus(_A)
_PsConfMajorLowVoltage1_Type=Integer32
_PsConfMajorLowVoltage1_Object=MibScalar
psConfMajorLowVoltage1=_PsConfMajorLowVoltage1_Object((1,3,6,1,4,1,6050,1,8,19),_PsConfMajorLowVoltage1_Type())
psConfMajorLowVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfMajorLowVoltage1.setStatus(_A)
_PsConfMajorLowVoltage_Type=Integer32
_PsConfMajorLowVoltage_Object=MibScalar
psConfMajorLowVoltage=_PsConfMajorLowVoltage_Object((1,3,6,1,4,1,6050,1,8,20),_PsConfMajorLowVoltage_Type())
psConfMajorLowVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfMajorLowVoltage.setStatus(_A)
_PsConfMinorLowVoltage_Type=Integer32
_PsConfMinorLowVoltage_Object=MibScalar
psConfMinorLowVoltage=_PsConfMinorLowVoltage_Object((1,3,6,1,4,1,6050,1,8,21),_PsConfMinorLowVoltage_Type())
psConfMinorLowVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfMinorLowVoltage.setStatus(_A)
_PsConfMinorHighVoltage_Type=Integer32
_PsConfMinorHighVoltage_Object=MibScalar
psConfMinorHighVoltage=_PsConfMinorHighVoltage_Object((1,3,6,1,4,1,6050,1,8,22),_PsConfMinorHighVoltage_Type())
psConfMinorHighVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfMinorHighVoltage.setStatus(_A)
_PsConfMajorHighVoltage_Type=Integer32
_PsConfMajorHighVoltage_Object=MibScalar
psConfMajorHighVoltage=_PsConfMajorHighVoltage_Object((1,3,6,1,4,1,6050,1,8,23),_PsConfMajorHighVoltage_Type())
psConfMajorHighVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfMajorHighVoltage.setStatus(_A)
_PsConfFloatingVoltage_Type=Integer32
_PsConfFloatingVoltage_Object=MibScalar
psConfFloatingVoltage=_PsConfFloatingVoltage_Object((1,3,6,1,4,1,6050,1,8,24),_PsConfFloatingVoltage_Type())
psConfFloatingVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfFloatingVoltage.setStatus(_A)
_PsConfEqualizingVoltage_Type=Integer32
_PsConfEqualizingVoltage_Object=MibScalar
psConfEqualizingVoltage=_PsConfEqualizingVoltage_Object((1,3,6,1,4,1,6050,1,8,25),_PsConfEqualizingVoltage_Type())
psConfEqualizingVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqualizingVoltage.setStatus(_A)
_PsConfNumberOfBattery_Type=Integer32
_PsConfNumberOfBattery_Object=MibScalar
psConfNumberOfBattery=_PsConfNumberOfBattery_Object((1,3,6,1,4,1,6050,1,8,26),_PsConfNumberOfBattery_Type())
psConfNumberOfBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNumberOfBattery.setStatus(_A)
class _PsConfEnableTempComp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PsConfEnableTempComp_Type.__name__=_C
_PsConfEnableTempComp_Object=MibScalar
psConfEnableTempComp=_PsConfEnableTempComp_Object((1,3,6,1,4,1,6050,1,8,27),_PsConfEnableTempComp_Type())
psConfEnableTempComp.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEnableTempComp.setStatus(_A)
_PsConfNumberOfLVD_Type=Integer32
_PsConfNumberOfLVD_Object=MibScalar
psConfNumberOfLVD=_PsConfNumberOfLVD_Object((1,3,6,1,4,1,6050,1,8,28),_PsConfNumberOfLVD_Type())
psConfNumberOfLVD.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNumberOfLVD.setStatus(_A)
_PsConfEqMajorLowVoltageLV1_Type=Integer32
_PsConfEqMajorLowVoltageLV1_Object=MibScalar
psConfEqMajorLowVoltageLV1=_PsConfEqMajorLowVoltageLV1_Object((1,3,6,1,4,1,6050,1,8,29),_PsConfEqMajorLowVoltageLV1_Type())
psConfEqMajorLowVoltageLV1.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqMajorLowVoltageLV1.setStatus(_A)
_PsConfEqMajorLowVoltageLv_Type=Integer32
_PsConfEqMajorLowVoltageLv_Object=MibScalar
psConfEqMajorLowVoltageLv=_PsConfEqMajorLowVoltageLv_Object((1,3,6,1,4,1,6050,1,8,30),_PsConfEqMajorLowVoltageLv_Type())
psConfEqMajorLowVoltageLv.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqMajorLowVoltageLv.setStatus(_A)
_PsConfEqMinorLowVoltageLV_Type=Integer32
_PsConfEqMinorLowVoltageLV_Object=MibScalar
psConfEqMinorLowVoltageLV=_PsConfEqMinorLowVoltageLV_Object((1,3,6,1,4,1,6050,1,8,31),_PsConfEqMinorLowVoltageLV_Type())
psConfEqMinorLowVoltageLV.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqMinorLowVoltageLV.setStatus(_A)
_PsConfEqMinorHighVoltageHV_Type=Integer32
_PsConfEqMinorHighVoltageHV_Object=MibScalar
psConfEqMinorHighVoltageHV=_PsConfEqMinorHighVoltageHV_Object((1,3,6,1,4,1,6050,1,8,32),_PsConfEqMinorHighVoltageHV_Type())
psConfEqMinorHighVoltageHV.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqMinorHighVoltageHV.setStatus(_A)
_PsConfEqMajorHighVoltageHV_Type=Integer32
_PsConfEqMajorHighVoltageHV_Object=MibScalar
psConfEqMajorHighVoltageHV=_PsConfEqMajorHighVoltageHV_Object((1,3,6,1,4,1,6050,1,8,33),_PsConfEqMajorHighVoltageHV_Type())
psConfEqMajorHighVoltageHV.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfEqMajorHighVoltageHV.setStatus(_A)
_PsConfInvertorVoltage_Type=Integer32
_PsConfInvertorVoltage_Object=MibScalar
psConfInvertorVoltage=_PsConfInvertorVoltage_Object((1,3,6,1,4,1,6050,1,8,34),_PsConfInvertorVoltage_Type())
psConfInvertorVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfInvertorVoltage.setStatus(_A)
_PsConfInvertorHighVoltage_Type=Integer32
_PsConfInvertorHighVoltage_Object=MibScalar
psConfInvertorHighVoltage=_PsConfInvertorHighVoltage_Object((1,3,6,1,4,1,6050,1,8,35),_PsConfInvertorHighVoltage_Type())
psConfInvertorHighVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfInvertorHighVoltage.setStatus(_A)
_PsConfInvertorLowVoltage_Type=Integer32
_PsConfInvertorLowVoltage_Object=MibScalar
psConfInvertorLowVoltage=_PsConfInvertorLowVoltage_Object((1,3,6,1,4,1,6050,1,8,36),_PsConfInvertorLowVoltage_Type())
psConfInvertorLowVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfInvertorLowVoltage.setStatus(_A)
_PsConfLVDDisconnectTime_Type=Integer32
_PsConfLVDDisconnectTime_Object=MibScalar
psConfLVDDisconnectTime=_PsConfLVDDisconnectTime_Object((1,3,6,1,4,1,6050,1,8,37),_PsConfLVDDisconnectTime_Type())
psConfLVDDisconnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfLVDDisconnectTime.setStatus(_A)
_PsConfNomSpare0_Type=Integer32
_PsConfNomSpare0_Object=MibScalar
psConfNomSpare0=_PsConfNomSpare0_Object((1,3,6,1,4,1,6050,1,8,38),_PsConfNomSpare0_Type())
psConfNomSpare0.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare0.setStatus(_A)
_PsConfNomSpare1_Type=Integer32
_PsConfNomSpare1_Object=MibScalar
psConfNomSpare1=_PsConfNomSpare1_Object((1,3,6,1,4,1,6050,1,8,39),_PsConfNomSpare1_Type())
psConfNomSpare1.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare1.setStatus(_A)
_PsConfNomSpare2_Type=Integer32
_PsConfNomSpare2_Object=MibScalar
psConfNomSpare2=_PsConfNomSpare2_Object((1,3,6,1,4,1,6050,1,8,40),_PsConfNomSpare2_Type())
psConfNomSpare2.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare2.setStatus(_A)
_PsConfNomSpare3_Type=Integer32
_PsConfNomSpare3_Object=MibScalar
psConfNomSpare3=_PsConfNomSpare3_Object((1,3,6,1,4,1,6050,1,8,41),_PsConfNomSpare3_Type())
psConfNomSpare3.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare3.setStatus(_A)
_PsConfNomSpare4_Type=Integer32
_PsConfNomSpare4_Object=MibScalar
psConfNomSpare4=_PsConfNomSpare4_Object((1,3,6,1,4,1,6050,1,8,42),_PsConfNomSpare4_Type())
psConfNomSpare4.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare4.setStatus(_A)
_PsConfNomSpare5_Type=Integer32
_PsConfNomSpare5_Object=MibScalar
psConfNomSpare5=_PsConfNomSpare5_Object((1,3,6,1,4,1,6050,1,8,43),_PsConfNomSpare5_Type())
psConfNomSpare5.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare5.setStatus(_A)
_PsConfNomSpare6_Type=Integer32
_PsConfNomSpare6_Object=MibScalar
psConfNomSpare6=_PsConfNomSpare6_Object((1,3,6,1,4,1,6050,1,8,44),_PsConfNomSpare6_Type())
psConfNomSpare6.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare6.setStatus(_A)
_PsConfNomSpare7_Type=Integer32
_PsConfNomSpare7_Object=MibScalar
psConfNomSpare7=_PsConfNomSpare7_Object((1,3,6,1,4,1,6050,1,8,45),_PsConfNomSpare7_Type())
psConfNomSpare7.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare7.setStatus(_A)
_PsConfNomSpare8_Type=Integer32
_PsConfNomSpare8_Object=MibScalar
psConfNomSpare8=_PsConfNomSpare8_Object((1,3,6,1,4,1,6050,1,8,46),_PsConfNomSpare8_Type())
psConfNomSpare8.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare8.setStatus(_A)
_PsConfNomSpare9_Type=Integer32
_PsConfNomSpare9_Object=MibScalar
psConfNomSpare9=_PsConfNomSpare9_Object((1,3,6,1,4,1,6050,1,8,47),_PsConfNomSpare9_Type())
psConfNomSpare9.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare9.setStatus(_A)
_PsConfNomSpare10_Type=Integer32
_PsConfNomSpare10_Object=MibScalar
psConfNomSpare10=_PsConfNomSpare10_Object((1,3,6,1,4,1,6050,1,8,48),_PsConfNomSpare10_Type())
psConfNomSpare10.setMaxAccess(_B)
if mibBuilder.loadTexts:psConfNomSpare10.setStatus(_A)
_PsStatus_ObjectIdentity=ObjectIdentity
psStatus=_PsStatus_ObjectIdentity((1,3,6,1,4,1,6050,1,9))
class _PsStatusAlarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm1_Type.__name__=_C
_PsStatusAlarm1_Object=MibScalar
psStatusAlarm1=_PsStatusAlarm1_Object((1,3,6,1,4,1,6050,1,9,1),_PsStatusAlarm1_Type())
psStatusAlarm1.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm1.setStatus(_A)
class _PsStatusAlarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm2_Type.__name__=_C
_PsStatusAlarm2_Object=MibScalar
psStatusAlarm2=_PsStatusAlarm2_Object((1,3,6,1,4,1,6050,1,9,2),_PsStatusAlarm2_Type())
psStatusAlarm2.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm2.setStatus(_A)
class _PsStatusAlarm3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm3_Type.__name__=_C
_PsStatusAlarm3_Object=MibScalar
psStatusAlarm3=_PsStatusAlarm3_Object((1,3,6,1,4,1,6050,1,9,3),_PsStatusAlarm3_Type())
psStatusAlarm3.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm3.setStatus(_A)
class _PsStatusAlarm4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm4_Type.__name__=_C
_PsStatusAlarm4_Object=MibScalar
psStatusAlarm4=_PsStatusAlarm4_Object((1,3,6,1,4,1,6050,1,9,4),_PsStatusAlarm4_Type())
psStatusAlarm4.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm4.setStatus(_A)
class _PsStatusAlarm5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm5_Type.__name__=_C
_PsStatusAlarm5_Object=MibScalar
psStatusAlarm5=_PsStatusAlarm5_Object((1,3,6,1,4,1,6050,1,9,5),_PsStatusAlarm5_Type())
psStatusAlarm5.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm5.setStatus(_A)
class _PsStatusAlarm6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm6_Type.__name__=_C
_PsStatusAlarm6_Object=MibScalar
psStatusAlarm6=_PsStatusAlarm6_Object((1,3,6,1,4,1,6050,1,9,6),_PsStatusAlarm6_Type())
psStatusAlarm6.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm6.setStatus(_A)
class _PsStatusAlarm7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm7_Type.__name__=_C
_PsStatusAlarm7_Object=MibScalar
psStatusAlarm7=_PsStatusAlarm7_Object((1,3,6,1,4,1,6050,1,9,7),_PsStatusAlarm7_Type())
psStatusAlarm7.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm7.setStatus(_A)
class _PsStatusAlarm8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm8_Type.__name__=_C
_PsStatusAlarm8_Object=MibScalar
psStatusAlarm8=_PsStatusAlarm8_Object((1,3,6,1,4,1,6050,1,9,8),_PsStatusAlarm8_Type())
psStatusAlarm8.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm8.setStatus(_A)
class _PsStatusAlarm9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm9_Type.__name__=_C
_PsStatusAlarm9_Object=MibScalar
psStatusAlarm9=_PsStatusAlarm9_Object((1,3,6,1,4,1,6050,1,9,9),_PsStatusAlarm9_Type())
psStatusAlarm9.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm9.setStatus(_A)
class _PsStatusAlarm10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm10_Type.__name__=_C
_PsStatusAlarm10_Object=MibScalar
psStatusAlarm10=_PsStatusAlarm10_Object((1,3,6,1,4,1,6050,1,9,10),_PsStatusAlarm10_Type())
psStatusAlarm10.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm10.setStatus(_A)
class _PsStatusAlarm11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm11_Type.__name__=_C
_PsStatusAlarm11_Object=MibScalar
psStatusAlarm11=_PsStatusAlarm11_Object((1,3,6,1,4,1,6050,1,9,11),_PsStatusAlarm11_Type())
psStatusAlarm11.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm11.setStatus(_A)
class _PsStatusAlarm12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm12_Type.__name__=_C
_PsStatusAlarm12_Object=MibScalar
psStatusAlarm12=_PsStatusAlarm12_Object((1,3,6,1,4,1,6050,1,9,12),_PsStatusAlarm12_Type())
psStatusAlarm12.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm12.setStatus(_A)
class _PsStatusAlarm13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm13_Type.__name__=_C
_PsStatusAlarm13_Object=MibScalar
psStatusAlarm13=_PsStatusAlarm13_Object((1,3,6,1,4,1,6050,1,9,13),_PsStatusAlarm13_Type())
psStatusAlarm13.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm13.setStatus(_A)
class _PsStatusAlarm14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm14_Type.__name__=_C
_PsStatusAlarm14_Object=MibScalar
psStatusAlarm14=_PsStatusAlarm14_Object((1,3,6,1,4,1,6050,1,9,14),_PsStatusAlarm14_Type())
psStatusAlarm14.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm14.setStatus(_A)
class _PsStatusAlarm15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm15_Type.__name__=_C
_PsStatusAlarm15_Object=MibScalar
psStatusAlarm15=_PsStatusAlarm15_Object((1,3,6,1,4,1,6050,1,9,15),_PsStatusAlarm15_Type())
psStatusAlarm15.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm15.setStatus(_A)
class _PsStatusAlarm16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm16_Type.__name__=_C
_PsStatusAlarm16_Object=MibScalar
psStatusAlarm16=_PsStatusAlarm16_Object((1,3,6,1,4,1,6050,1,9,16),_PsStatusAlarm16_Type())
psStatusAlarm16.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm16.setStatus(_A)
class _PsStatusAlarm17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm17_Type.__name__=_C
_PsStatusAlarm17_Object=MibScalar
psStatusAlarm17=_PsStatusAlarm17_Object((1,3,6,1,4,1,6050,1,9,17),_PsStatusAlarm17_Type())
psStatusAlarm17.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm17.setStatus(_A)
class _PsStatusAlarm18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm18_Type.__name__=_C
_PsStatusAlarm18_Object=MibScalar
psStatusAlarm18=_PsStatusAlarm18_Object((1,3,6,1,4,1,6050,1,9,18),_PsStatusAlarm18_Type())
psStatusAlarm18.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm18.setStatus(_A)
class _PsStatusAlarm19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm19_Type.__name__=_C
_PsStatusAlarm19_Object=MibScalar
psStatusAlarm19=_PsStatusAlarm19_Object((1,3,6,1,4,1,6050,1,9,19),_PsStatusAlarm19_Type())
psStatusAlarm19.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm19.setStatus(_A)
class _PsStatusAlarm20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm20_Type.__name__=_C
_PsStatusAlarm20_Object=MibScalar
psStatusAlarm20=_PsStatusAlarm20_Object((1,3,6,1,4,1,6050,1,9,20),_PsStatusAlarm20_Type())
psStatusAlarm20.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm20.setStatus(_A)
class _PsStatusAlarm21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm21_Type.__name__=_C
_PsStatusAlarm21_Object=MibScalar
psStatusAlarm21=_PsStatusAlarm21_Object((1,3,6,1,4,1,6050,1,9,21),_PsStatusAlarm21_Type())
psStatusAlarm21.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm21.setStatus(_A)
class _PsStatusAlarm22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm22_Type.__name__=_C
_PsStatusAlarm22_Object=MibScalar
psStatusAlarm22=_PsStatusAlarm22_Object((1,3,6,1,4,1,6050,1,9,22),_PsStatusAlarm22_Type())
psStatusAlarm22.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm22.setStatus(_A)
class _PsStatusAlarm23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm23_Type.__name__=_C
_PsStatusAlarm23_Object=MibScalar
psStatusAlarm23=_PsStatusAlarm23_Object((1,3,6,1,4,1,6050,1,9,23),_PsStatusAlarm23_Type())
psStatusAlarm23.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm23.setStatus(_A)
class _PsStatusAlarm24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm24_Type.__name__=_C
_PsStatusAlarm24_Object=MibScalar
psStatusAlarm24=_PsStatusAlarm24_Object((1,3,6,1,4,1,6050,1,9,24),_PsStatusAlarm24_Type())
psStatusAlarm24.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm24.setStatus(_A)
class _PsStatusAlarm25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm25_Type.__name__=_C
_PsStatusAlarm25_Object=MibScalar
psStatusAlarm25=_PsStatusAlarm25_Object((1,3,6,1,4,1,6050,1,9,25),_PsStatusAlarm25_Type())
psStatusAlarm25.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm25.setStatus(_A)
class _PsStatusAlarm26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm26_Type.__name__=_C
_PsStatusAlarm26_Object=MibScalar
psStatusAlarm26=_PsStatusAlarm26_Object((1,3,6,1,4,1,6050,1,9,26),_PsStatusAlarm26_Type())
psStatusAlarm26.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm26.setStatus(_A)
class _PsStatusAlarm27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm27_Type.__name__=_C
_PsStatusAlarm27_Object=MibScalar
psStatusAlarm27=_PsStatusAlarm27_Object((1,3,6,1,4,1,6050,1,9,27),_PsStatusAlarm27_Type())
psStatusAlarm27.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm27.setStatus(_A)
class _PsStatusAlarm28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm28_Type.__name__=_C
_PsStatusAlarm28_Object=MibScalar
psStatusAlarm28=_PsStatusAlarm28_Object((1,3,6,1,4,1,6050,1,9,28),_PsStatusAlarm28_Type())
psStatusAlarm28.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm28.setStatus(_A)
class _PsStatusAlarm29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm29_Type.__name__=_C
_PsStatusAlarm29_Object=MibScalar
psStatusAlarm29=_PsStatusAlarm29_Object((1,3,6,1,4,1,6050,1,9,29),_PsStatusAlarm29_Type())
psStatusAlarm29.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm29.setStatus(_A)
class _PsStatusAlarm30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm30_Type.__name__=_C
_PsStatusAlarm30_Object=MibScalar
psStatusAlarm30=_PsStatusAlarm30_Object((1,3,6,1,4,1,6050,1,9,30),_PsStatusAlarm30_Type())
psStatusAlarm30.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm30.setStatus(_A)
class _PsStatusAlarm31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm31_Type.__name__=_C
_PsStatusAlarm31_Object=MibScalar
psStatusAlarm31=_PsStatusAlarm31_Object((1,3,6,1,4,1,6050,1,9,31),_PsStatusAlarm31_Type())
psStatusAlarm31.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm31.setStatus(_A)
class _PsStatusAlarm32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm32_Type.__name__=_C
_PsStatusAlarm32_Object=MibScalar
psStatusAlarm32=_PsStatusAlarm32_Object((1,3,6,1,4,1,6050,1,9,32),_PsStatusAlarm32_Type())
psStatusAlarm32.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm32.setStatus(_A)
class _PsStatusAlarm33_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm33_Type.__name__=_C
_PsStatusAlarm33_Object=MibScalar
psStatusAlarm33=_PsStatusAlarm33_Object((1,3,6,1,4,1,6050,1,9,33),_PsStatusAlarm33_Type())
psStatusAlarm33.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm33.setStatus(_A)
class _PsStatusAlarm34_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm34_Type.__name__=_C
_PsStatusAlarm34_Object=MibScalar
psStatusAlarm34=_PsStatusAlarm34_Object((1,3,6,1,4,1,6050,1,9,34),_PsStatusAlarm34_Type())
psStatusAlarm34.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm34.setStatus(_A)
class _PsStatusAlarm35_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm35_Type.__name__=_C
_PsStatusAlarm35_Object=MibScalar
psStatusAlarm35=_PsStatusAlarm35_Object((1,3,6,1,4,1,6050,1,9,35),_PsStatusAlarm35_Type())
psStatusAlarm35.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm35.setStatus(_A)
class _PsStatusAlarm36_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm36_Type.__name__=_C
_PsStatusAlarm36_Object=MibScalar
psStatusAlarm36=_PsStatusAlarm36_Object((1,3,6,1,4,1,6050,1,9,36),_PsStatusAlarm36_Type())
psStatusAlarm36.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm36.setStatus(_A)
class _PsStatusAlarm37_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm37_Type.__name__=_C
_PsStatusAlarm37_Object=MibScalar
psStatusAlarm37=_PsStatusAlarm37_Object((1,3,6,1,4,1,6050,1,9,37),_PsStatusAlarm37_Type())
psStatusAlarm37.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm37.setStatus(_A)
class _PsStatusAlarm38_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm38_Type.__name__=_C
_PsStatusAlarm38_Object=MibScalar
psStatusAlarm38=_PsStatusAlarm38_Object((1,3,6,1,4,1,6050,1,9,38),_PsStatusAlarm38_Type())
psStatusAlarm38.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm38.setStatus(_A)
class _PsStatusAlarm39_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm39_Type.__name__=_C
_PsStatusAlarm39_Object=MibScalar
psStatusAlarm39=_PsStatusAlarm39_Object((1,3,6,1,4,1,6050,1,9,39),_PsStatusAlarm39_Type())
psStatusAlarm39.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm39.setStatus(_A)
class _PsStatusAlarm40_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm40_Type.__name__=_C
_PsStatusAlarm40_Object=MibScalar
psStatusAlarm40=_PsStatusAlarm40_Object((1,3,6,1,4,1,6050,1,9,40),_PsStatusAlarm40_Type())
psStatusAlarm40.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm40.setStatus(_A)
class _PsStatusAlarm41_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm41_Type.__name__=_C
_PsStatusAlarm41_Object=MibScalar
psStatusAlarm41=_PsStatusAlarm41_Object((1,3,6,1,4,1,6050,1,9,41),_PsStatusAlarm41_Type())
psStatusAlarm41.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm41.setStatus(_A)
class _PsStatusAlarm42_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm42_Type.__name__=_C
_PsStatusAlarm42_Object=MibScalar
psStatusAlarm42=_PsStatusAlarm42_Object((1,3,6,1,4,1,6050,1,9,42),_PsStatusAlarm42_Type())
psStatusAlarm42.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm42.setStatus(_A)
class _PsStatusAlarm43_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm43_Type.__name__=_C
_PsStatusAlarm43_Object=MibScalar
psStatusAlarm43=_PsStatusAlarm43_Object((1,3,6,1,4,1,6050,1,9,43),_PsStatusAlarm43_Type())
psStatusAlarm43.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm43.setStatus(_A)
class _PsStatusAlarm44_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm44_Type.__name__=_C
_PsStatusAlarm44_Object=MibScalar
psStatusAlarm44=_PsStatusAlarm44_Object((1,3,6,1,4,1,6050,1,9,44),_PsStatusAlarm44_Type())
psStatusAlarm44.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm44.setStatus(_A)
class _PsStatusAlarm45_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm45_Type.__name__=_C
_PsStatusAlarm45_Object=MibScalar
psStatusAlarm45=_PsStatusAlarm45_Object((1,3,6,1,4,1,6050,1,9,45),_PsStatusAlarm45_Type())
psStatusAlarm45.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm45.setStatus(_A)
class _PsStatusAlarm46_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm46_Type.__name__=_C
_PsStatusAlarm46_Object=MibScalar
psStatusAlarm46=_PsStatusAlarm46_Object((1,3,6,1,4,1,6050,1,9,46),_PsStatusAlarm46_Type())
psStatusAlarm46.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm46.setStatus(_A)
class _PsStatusAlarm47_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm47_Type.__name__=_C
_PsStatusAlarm47_Object=MibScalar
psStatusAlarm47=_PsStatusAlarm47_Object((1,3,6,1,4,1,6050,1,9,47),_PsStatusAlarm47_Type())
psStatusAlarm47.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm47.setStatus(_A)
class _PsStatusAlarm48_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm48_Type.__name__=_C
_PsStatusAlarm48_Object=MibScalar
psStatusAlarm48=_PsStatusAlarm48_Object((1,3,6,1,4,1,6050,1,9,48),_PsStatusAlarm48_Type())
psStatusAlarm48.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm48.setStatus(_A)
class _PsStatusAlarm49_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm49_Type.__name__=_C
_PsStatusAlarm49_Object=MibScalar
psStatusAlarm49=_PsStatusAlarm49_Object((1,3,6,1,4,1,6050,1,9,49),_PsStatusAlarm49_Type())
psStatusAlarm49.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm49.setStatus(_A)
class _PsStatusAlarm50_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm50_Type.__name__=_C
_PsStatusAlarm50_Object=MibScalar
psStatusAlarm50=_PsStatusAlarm50_Object((1,3,6,1,4,1,6050,1,9,50),_PsStatusAlarm50_Type())
psStatusAlarm50.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm50.setStatus(_A)
class _PsStatusAlarm51_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm51_Type.__name__=_C
_PsStatusAlarm51_Object=MibScalar
psStatusAlarm51=_PsStatusAlarm51_Object((1,3,6,1,4,1,6050,1,9,51),_PsStatusAlarm51_Type())
psStatusAlarm51.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm51.setStatus(_A)
class _PsStatusAlarm52_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm52_Type.__name__=_C
_PsStatusAlarm52_Object=MibScalar
psStatusAlarm52=_PsStatusAlarm52_Object((1,3,6,1,4,1,6050,1,9,52),_PsStatusAlarm52_Type())
psStatusAlarm52.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm52.setStatus(_A)
class _PsStatusAlarm53_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm53_Type.__name__=_C
_PsStatusAlarm53_Object=MibScalar
psStatusAlarm53=_PsStatusAlarm53_Object((1,3,6,1,4,1,6050,1,9,53),_PsStatusAlarm53_Type())
psStatusAlarm53.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm53.setStatus(_A)
class _PsStatusAlarm54_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm54_Type.__name__=_C
_PsStatusAlarm54_Object=MibScalar
psStatusAlarm54=_PsStatusAlarm54_Object((1,3,6,1,4,1,6050,1,9,54),_PsStatusAlarm54_Type())
psStatusAlarm54.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm54.setStatus(_A)
class _PsStatusAlarm55_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm55_Type.__name__=_C
_PsStatusAlarm55_Object=MibScalar
psStatusAlarm55=_PsStatusAlarm55_Object((1,3,6,1,4,1,6050,1,9,55),_PsStatusAlarm55_Type())
psStatusAlarm55.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm55.setStatus(_A)
class _PsStatusAlarm56_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm56_Type.__name__=_C
_PsStatusAlarm56_Object=MibScalar
psStatusAlarm56=_PsStatusAlarm56_Object((1,3,6,1,4,1,6050,1,9,56),_PsStatusAlarm56_Type())
psStatusAlarm56.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm56.setStatus(_A)
class _PsStatusAlarm57_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm57_Type.__name__=_C
_PsStatusAlarm57_Object=MibScalar
psStatusAlarm57=_PsStatusAlarm57_Object((1,3,6,1,4,1,6050,1,9,57),_PsStatusAlarm57_Type())
psStatusAlarm57.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm57.setStatus(_A)
class _PsStatusAlarm58_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm58_Type.__name__=_C
_PsStatusAlarm58_Object=MibScalar
psStatusAlarm58=_PsStatusAlarm58_Object((1,3,6,1,4,1,6050,1,9,58),_PsStatusAlarm58_Type())
psStatusAlarm58.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm58.setStatus(_A)
class _PsStatusAlarm59_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm59_Type.__name__=_C
_PsStatusAlarm59_Object=MibScalar
psStatusAlarm59=_PsStatusAlarm59_Object((1,3,6,1,4,1,6050,1,9,59),_PsStatusAlarm59_Type())
psStatusAlarm59.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm59.setStatus(_A)
class _PsStatusAlarm60_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm60_Type.__name__=_C
_PsStatusAlarm60_Object=MibScalar
psStatusAlarm60=_PsStatusAlarm60_Object((1,3,6,1,4,1,6050,1,9,60),_PsStatusAlarm60_Type())
psStatusAlarm60.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm60.setStatus(_A)
class _PsStatusAlarm61_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm61_Type.__name__=_C
_PsStatusAlarm61_Object=MibScalar
psStatusAlarm61=_PsStatusAlarm61_Object((1,3,6,1,4,1,6050,1,9,61),_PsStatusAlarm61_Type())
psStatusAlarm61.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm61.setStatus(_A)
class _PsStatusAlarm62_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm62_Type.__name__=_C
_PsStatusAlarm62_Object=MibScalar
psStatusAlarm62=_PsStatusAlarm62_Object((1,3,6,1,4,1,6050,1,9,62),_PsStatusAlarm62_Type())
psStatusAlarm62.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm62.setStatus(_A)
class _PsStatusAlarm63_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm63_Type.__name__=_C
_PsStatusAlarm63_Object=MibScalar
psStatusAlarm63=_PsStatusAlarm63_Object((1,3,6,1,4,1,6050,1,9,63),_PsStatusAlarm63_Type())
psStatusAlarm63.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm63.setStatus(_A)
class _PsStatusAlarm64_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm64_Type.__name__=_C
_PsStatusAlarm64_Object=MibScalar
psStatusAlarm64=_PsStatusAlarm64_Object((1,3,6,1,4,1,6050,1,9,64),_PsStatusAlarm64_Type())
psStatusAlarm64.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm64.setStatus(_A)
class _PsStatusAlarm65_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm65_Type.__name__=_C
_PsStatusAlarm65_Object=MibScalar
psStatusAlarm65=_PsStatusAlarm65_Object((1,3,6,1,4,1,6050,1,9,65),_PsStatusAlarm65_Type())
psStatusAlarm65.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm65.setStatus(_A)
class _PsStatusAlarm66_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm66_Type.__name__=_C
_PsStatusAlarm66_Object=MibScalar
psStatusAlarm66=_PsStatusAlarm66_Object((1,3,6,1,4,1,6050,1,9,66),_PsStatusAlarm66_Type())
psStatusAlarm66.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm66.setStatus(_A)
class _PsStatusAlarm67_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm67_Type.__name__=_C
_PsStatusAlarm67_Object=MibScalar
psStatusAlarm67=_PsStatusAlarm67_Object((1,3,6,1,4,1,6050,1,9,67),_PsStatusAlarm67_Type())
psStatusAlarm67.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm67.setStatus(_A)
class _PsStatusAlarm68_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm68_Type.__name__=_C
_PsStatusAlarm68_Object=MibScalar
psStatusAlarm68=_PsStatusAlarm68_Object((1,3,6,1,4,1,6050,1,9,68),_PsStatusAlarm68_Type())
psStatusAlarm68.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm68.setStatus(_A)
class _PsStatusAlarm69_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm69_Type.__name__=_C
_PsStatusAlarm69_Object=MibScalar
psStatusAlarm69=_PsStatusAlarm69_Object((1,3,6,1,4,1,6050,1,9,69),_PsStatusAlarm69_Type())
psStatusAlarm69.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm69.setStatus(_A)
class _PsStatusAlarm70_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm70_Type.__name__=_C
_PsStatusAlarm70_Object=MibScalar
psStatusAlarm70=_PsStatusAlarm70_Object((1,3,6,1,4,1,6050,1,9,70),_PsStatusAlarm70_Type())
psStatusAlarm70.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm70.setStatus(_A)
class _PsStatusAlarm71_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm71_Type.__name__=_C
_PsStatusAlarm71_Object=MibScalar
psStatusAlarm71=_PsStatusAlarm71_Object((1,3,6,1,4,1,6050,1,9,71),_PsStatusAlarm71_Type())
psStatusAlarm71.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm71.setStatus(_A)
class _PsStatusAlarm72_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm72_Type.__name__=_C
_PsStatusAlarm72_Object=MibScalar
psStatusAlarm72=_PsStatusAlarm72_Object((1,3,6,1,4,1,6050,1,9,72),_PsStatusAlarm72_Type())
psStatusAlarm72.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm72.setStatus(_A)
class _PsStatusAlarm73_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm73_Type.__name__=_C
_PsStatusAlarm73_Object=MibScalar
psStatusAlarm73=_PsStatusAlarm73_Object((1,3,6,1,4,1,6050,1,9,73),_PsStatusAlarm73_Type())
psStatusAlarm73.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm73.setStatus(_A)
class _PsStatusAlarm74_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm74_Type.__name__=_C
_PsStatusAlarm74_Object=MibScalar
psStatusAlarm74=_PsStatusAlarm74_Object((1,3,6,1,4,1,6050,1,9,74),_PsStatusAlarm74_Type())
psStatusAlarm74.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm74.setStatus(_A)
class _PsStatusAlarm75_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm75_Type.__name__=_C
_PsStatusAlarm75_Object=MibScalar
psStatusAlarm75=_PsStatusAlarm75_Object((1,3,6,1,4,1,6050,1,9,75),_PsStatusAlarm75_Type())
psStatusAlarm75.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm75.setStatus(_A)
class _PsStatusAlarm76_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm76_Type.__name__=_C
_PsStatusAlarm76_Object=MibScalar
psStatusAlarm76=_PsStatusAlarm76_Object((1,3,6,1,4,1,6050,1,9,76),_PsStatusAlarm76_Type())
psStatusAlarm76.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm76.setStatus(_A)
class _PsStatusAlarm77_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm77_Type.__name__=_C
_PsStatusAlarm77_Object=MibScalar
psStatusAlarm77=_PsStatusAlarm77_Object((1,3,6,1,4,1,6050,1,9,77),_PsStatusAlarm77_Type())
psStatusAlarm77.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm77.setStatus(_A)
class _PsStatusAlarm78_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm78_Type.__name__=_C
_PsStatusAlarm78_Object=MibScalar
psStatusAlarm78=_PsStatusAlarm78_Object((1,3,6,1,4,1,6050,1,9,78),_PsStatusAlarm78_Type())
psStatusAlarm78.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm78.setStatus(_A)
class _PsStatusAlarm79_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm79_Type.__name__=_C
_PsStatusAlarm79_Object=MibScalar
psStatusAlarm79=_PsStatusAlarm79_Object((1,3,6,1,4,1,6050,1,9,79),_PsStatusAlarm79_Type())
psStatusAlarm79.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm79.setStatus(_A)
class _PsStatusAlarm80_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm80_Type.__name__=_C
_PsStatusAlarm80_Object=MibScalar
psStatusAlarm80=_PsStatusAlarm80_Object((1,3,6,1,4,1,6050,1,9,80),_PsStatusAlarm80_Type())
psStatusAlarm80.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm80.setStatus(_A)
class _PsStatusAlarm81_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm81_Type.__name__=_C
_PsStatusAlarm81_Object=MibScalar
psStatusAlarm81=_PsStatusAlarm81_Object((1,3,6,1,4,1,6050,1,9,81),_PsStatusAlarm81_Type())
psStatusAlarm81.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm81.setStatus(_A)
class _PsStatusAlarm82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm82_Type.__name__=_C
_PsStatusAlarm82_Object=MibScalar
psStatusAlarm82=_PsStatusAlarm82_Object((1,3,6,1,4,1,6050,1,9,82),_PsStatusAlarm82_Type())
psStatusAlarm82.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm82.setStatus(_A)
class _PsStatusAlarm83_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm83_Type.__name__=_C
_PsStatusAlarm83_Object=MibScalar
psStatusAlarm83=_PsStatusAlarm83_Object((1,3,6,1,4,1,6050,1,9,83),_PsStatusAlarm83_Type())
psStatusAlarm83.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm83.setStatus(_A)
class _PsStatusAlarm84_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm84_Type.__name__=_C
_PsStatusAlarm84_Object=MibScalar
psStatusAlarm84=_PsStatusAlarm84_Object((1,3,6,1,4,1,6050,1,9,84),_PsStatusAlarm84_Type())
psStatusAlarm84.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm84.setStatus(_A)
class _PsStatusAlarm85_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm85_Type.__name__=_C
_PsStatusAlarm85_Object=MibScalar
psStatusAlarm85=_PsStatusAlarm85_Object((1,3,6,1,4,1,6050,1,9,85),_PsStatusAlarm85_Type())
psStatusAlarm85.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm85.setStatus(_A)
class _PsStatusAlarm86_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm86_Type.__name__=_C
_PsStatusAlarm86_Object=MibScalar
psStatusAlarm86=_PsStatusAlarm86_Object((1,3,6,1,4,1,6050,1,9,86),_PsStatusAlarm86_Type())
psStatusAlarm86.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm86.setStatus(_A)
class _PsStatusAlarm87_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm87_Type.__name__=_C
_PsStatusAlarm87_Object=MibScalar
psStatusAlarm87=_PsStatusAlarm87_Object((1,3,6,1,4,1,6050,1,9,87),_PsStatusAlarm87_Type())
psStatusAlarm87.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm87.setStatus(_A)
class _PsStatusAlarm88_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm88_Type.__name__=_C
_PsStatusAlarm88_Object=MibScalar
psStatusAlarm88=_PsStatusAlarm88_Object((1,3,6,1,4,1,6050,1,9,88),_PsStatusAlarm88_Type())
psStatusAlarm88.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm88.setStatus(_A)
class _PsStatusAlarm89_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm89_Type.__name__=_C
_PsStatusAlarm89_Object=MibScalar
psStatusAlarm89=_PsStatusAlarm89_Object((1,3,6,1,4,1,6050,1,9,89),_PsStatusAlarm89_Type())
psStatusAlarm89.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm89.setStatus(_A)
class _PsStatusAlarm90_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm90_Type.__name__=_C
_PsStatusAlarm90_Object=MibScalar
psStatusAlarm90=_PsStatusAlarm90_Object((1,3,6,1,4,1,6050,1,9,90),_PsStatusAlarm90_Type())
psStatusAlarm90.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm90.setStatus(_A)
class _PsStatusAlarm91_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm91_Type.__name__=_C
_PsStatusAlarm91_Object=MibScalar
psStatusAlarm91=_PsStatusAlarm91_Object((1,3,6,1,4,1,6050,1,9,91),_PsStatusAlarm91_Type())
psStatusAlarm91.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm91.setStatus(_A)
class _PsStatusAlarm92_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm92_Type.__name__=_C
_PsStatusAlarm92_Object=MibScalar
psStatusAlarm92=_PsStatusAlarm92_Object((1,3,6,1,4,1,6050,1,9,92),_PsStatusAlarm92_Type())
psStatusAlarm92.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm92.setStatus(_A)
class _PsStatusAlarm93_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm93_Type.__name__=_C
_PsStatusAlarm93_Object=MibScalar
psStatusAlarm93=_PsStatusAlarm93_Object((1,3,6,1,4,1,6050,1,9,93),_PsStatusAlarm93_Type())
psStatusAlarm93.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm93.setStatus(_A)
class _PsStatusAlarm94_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm94_Type.__name__=_C
_PsStatusAlarm94_Object=MibScalar
psStatusAlarm94=_PsStatusAlarm94_Object((1,3,6,1,4,1,6050,1,9,94),_PsStatusAlarm94_Type())
psStatusAlarm94.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm94.setStatus(_A)
class _PsStatusAlarm95_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm95_Type.__name__=_C
_PsStatusAlarm95_Object=MibScalar
psStatusAlarm95=_PsStatusAlarm95_Object((1,3,6,1,4,1,6050,1,9,95),_PsStatusAlarm95_Type())
psStatusAlarm95.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm95.setStatus(_A)
class _PsStatusAlarm96_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_PsStatusAlarm96_Type.__name__=_C
_PsStatusAlarm96_Object=MibScalar
psStatusAlarm96=_PsStatusAlarm96_Object((1,3,6,1,4,1,6050,1,9,96),_PsStatusAlarm96_Type())
psStatusAlarm96.setMaxAccess(_B)
if mibBuilder.loadTexts:psStatusAlarm96.setStatus(_A)
_PsStatusAlarmStruct_Type=Integer32
_PsStatusAlarmStruct_Object=MibScalar
psStatusAlarmStruct=_PsStatusAlarmStruct_Object((1,3,6,1,4,1,6050,1,9,97),_PsStatusAlarmStruct_Type())
psStatusAlarmStruct.setMaxAccess(_D)
if mibBuilder.loadTexts:psStatusAlarmStruct.setStatus(_A)
_PsStatusAlarmStruct1_Type=Integer32
_PsStatusAlarmStruct1_Object=MibScalar
psStatusAlarmStruct1=_PsStatusAlarmStruct1_Object((1,3,6,1,4,1,6050,1,9,98),_PsStatusAlarmStruct1_Type())
psStatusAlarmStruct1.setMaxAccess(_D)
if mibBuilder.loadTexts:psStatusAlarmStruct1.setStatus(_A)
_PsStatusAlarmStruct2_Type=Integer32
_PsStatusAlarmStruct2_Object=MibScalar
psStatusAlarmStruct2=_PsStatusAlarmStruct2_Object((1,3,6,1,4,1,6050,1,9,99),_PsStatusAlarmStruct2_Type())
psStatusAlarmStruct2.setMaxAccess(_D)
if mibBuilder.loadTexts:psStatusAlarmStruct2.setStatus(_A)
_PsStatistics_ObjectIdentity=ObjectIdentity
psStatistics=_PsStatistics_ObjectIdentity((1,3,6,1,4,1,6050,1,10))
_PsHourlyTable_Object=MibTable
psHourlyTable=_PsHourlyTable_Object((1,3,6,1,4,1,6050,1,10,1))
if mibBuilder.loadTexts:psHourlyTable.setStatus(_A)
_PsHourlyEntry_Object=MibTableRow
psHourlyEntry=_PsHourlyEntry_Object((1,3,6,1,4,1,6050,1,10,1,1))
psHourlyEntry.setIndexNames((0,_N,_q))
if mibBuilder.loadTexts:psHourlyEntry.setStatus(_A)
_PsHourlyIndex_Type=Integer32
_PsHourlyIndex_Object=MibTableColumn
psHourlyIndex=_PsHourlyIndex_Object((1,3,6,1,4,1,6050,1,10,1,1,1),_PsHourlyIndex_Type())
psHourlyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyIndex.setStatus(_A)
_PsHourlyMaxVoltage_Type=Integer32
_PsHourlyMaxVoltage_Object=MibTableColumn
psHourlyMaxVoltage=_PsHourlyMaxVoltage_Object((1,3,6,1,4,1,6050,1,10,1,1,2),_PsHourlyMaxVoltage_Type())
psHourlyMaxVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyMaxVoltage.setStatus(_A)
_PsHourlyMinVoltage_Type=Integer32
_PsHourlyMinVoltage_Object=MibTableColumn
psHourlyMinVoltage=_PsHourlyMinVoltage_Object((1,3,6,1,4,1,6050,1,10,1,1,3),_PsHourlyMinVoltage_Type())
psHourlyMinVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyMinVoltage.setStatus(_A)
_PsHourlyAvrVoltage_Type=Integer32
_PsHourlyAvrVoltage_Object=MibTableColumn
psHourlyAvrVoltage=_PsHourlyAvrVoltage_Object((1,3,6,1,4,1,6050,1,10,1,1,4),_PsHourlyAvrVoltage_Type())
psHourlyAvrVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyAvrVoltage.setStatus(_A)
_PsHourlyMinCurrent_Type=Integer32
_PsHourlyMinCurrent_Object=MibTableColumn
psHourlyMinCurrent=_PsHourlyMinCurrent_Object((1,3,6,1,4,1,6050,1,10,1,1,5),_PsHourlyMinCurrent_Type())
psHourlyMinCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyMinCurrent.setStatus(_A)
_PsHourlyMaxCurrent_Type=Integer32
_PsHourlyMaxCurrent_Object=MibTableColumn
psHourlyMaxCurrent=_PsHourlyMaxCurrent_Object((1,3,6,1,4,1,6050,1,10,1,1,6),_PsHourlyMaxCurrent_Type())
psHourlyMaxCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyMaxCurrent.setStatus(_A)
_PsHourlyAvrCurrent_Type=Integer32
_PsHourlyAvrCurrent_Object=MibTableColumn
psHourlyAvrCurrent=_PsHourlyAvrCurrent_Object((1,3,6,1,4,1,6050,1,10,1,1,7),_PsHourlyAvrCurrent_Type())
psHourlyAvrCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyAvrCurrent.setStatus(_A)
class _PsHourlyEndTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_PsHourlyEndTime_Type.__name__=_C
_PsHourlyEndTime_Object=MibTableColumn
psHourlyEndTime=_PsHourlyEndTime_Object((1,3,6,1,4,1,6050,1,10,1,1,8),_PsHourlyEndTime_Type())
psHourlyEndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyEndTime.setStatus(_A)
_PsDailyTable_Object=MibTable
psDailyTable=_PsDailyTable_Object((1,3,6,1,4,1,6050,1,10,2))
if mibBuilder.loadTexts:psDailyTable.setStatus(_A)
_PsDailyEntry_Object=MibTableRow
psDailyEntry=_PsDailyEntry_Object((1,3,6,1,4,1,6050,1,10,2,1))
psDailyEntry.setIndexNames((0,_N,_r))
if mibBuilder.loadTexts:psDailyEntry.setStatus(_A)
_PsDailyIndex_Type=Integer32
_PsDailyIndex_Object=MibTableColumn
psDailyIndex=_PsDailyIndex_Object((1,3,6,1,4,1,6050,1,10,2,1,1),_PsDailyIndex_Type())
psDailyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyIndex.setStatus(_A)
_PsDailyMaxVoltage_Type=Integer32
_PsDailyMaxVoltage_Object=MibTableColumn
psDailyMaxVoltage=_PsDailyMaxVoltage_Object((1,3,6,1,4,1,6050,1,10,2,1,2),_PsDailyMaxVoltage_Type())
psDailyMaxVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyMaxVoltage.setStatus(_A)
_PsDailyMinVoltage_Type=Integer32
_PsDailyMinVoltage_Object=MibTableColumn
psDailyMinVoltage=_PsDailyMinVoltage_Object((1,3,6,1,4,1,6050,1,10,2,1,3),_PsDailyMinVoltage_Type())
psDailyMinVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyMinVoltage.setStatus(_A)
_PsDailyAvrVoltage_Type=Integer32
_PsDailyAvrVoltage_Object=MibTableColumn
psDailyAvrVoltage=_PsDailyAvrVoltage_Object((1,3,6,1,4,1,6050,1,10,2,1,4),_PsDailyAvrVoltage_Type())
psDailyAvrVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyAvrVoltage.setStatus(_A)
_PsDailyMinCurrent_Type=Integer32
_PsDailyMinCurrent_Object=MibTableColumn
psDailyMinCurrent=_PsDailyMinCurrent_Object((1,3,6,1,4,1,6050,1,10,2,1,5),_PsDailyMinCurrent_Type())
psDailyMinCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyMinCurrent.setStatus(_A)
_PsDailyMaxCurrent_Type=Integer32
_PsDailyMaxCurrent_Object=MibTableColumn
psDailyMaxCurrent=_PsDailyMaxCurrent_Object((1,3,6,1,4,1,6050,1,10,2,1,6),_PsDailyMaxCurrent_Type())
psDailyMaxCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyMaxCurrent.setStatus(_A)
_PsDailyAvrCurrent_Type=Integer32
_PsDailyAvrCurrent_Object=MibTableColumn
psDailyAvrCurrent=_PsDailyAvrCurrent_Object((1,3,6,1,4,1,6050,1,10,2,1,7),_PsDailyAvrCurrent_Type())
psDailyAvrCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyAvrCurrent.setStatus(_A)
class _PsDailyDayOfMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_PsDailyDayOfMonth_Type.__name__=_C
_PsDailyDayOfMonth_Object=MibTableColumn
psDailyDayOfMonth=_PsDailyDayOfMonth_Object((1,3,6,1,4,1,6050,1,10,2,1,8),_PsDailyDayOfMonth_Type())
psDailyDayOfMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyDayOfMonth.setStatus(_A)
_PsMonthlyTable_Object=MibTable
psMonthlyTable=_PsMonthlyTable_Object((1,3,6,1,4,1,6050,1,10,3))
if mibBuilder.loadTexts:psMonthlyTable.setStatus(_A)
_PsMonthlyEntry_Object=MibTableRow
psMonthlyEntry=_PsMonthlyEntry_Object((1,3,6,1,4,1,6050,1,10,3,1))
psMonthlyEntry.setIndexNames((0,_N,_s))
if mibBuilder.loadTexts:psMonthlyEntry.setStatus(_A)
_PsMonthlyIndex_Type=Integer32
_PsMonthlyIndex_Object=MibTableColumn
psMonthlyIndex=_PsMonthlyIndex_Object((1,3,6,1,4,1,6050,1,10,3,1,1),_PsMonthlyIndex_Type())
psMonthlyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyIndex.setStatus(_A)
_PsMonthlyMaxVoltage_Type=Integer32
_PsMonthlyMaxVoltage_Object=MibTableColumn
psMonthlyMaxVoltage=_PsMonthlyMaxVoltage_Object((1,3,6,1,4,1,6050,1,10,3,1,2),_PsMonthlyMaxVoltage_Type())
psMonthlyMaxVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyMaxVoltage.setStatus(_A)
_PsMonthlyMinVoltage_Type=Integer32
_PsMonthlyMinVoltage_Object=MibTableColumn
psMonthlyMinVoltage=_PsMonthlyMinVoltage_Object((1,3,6,1,4,1,6050,1,10,3,1,3),_PsMonthlyMinVoltage_Type())
psMonthlyMinVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyMinVoltage.setStatus(_A)
_PsMonthlyAvrVoltage_Type=Integer32
_PsMonthlyAvrVoltage_Object=MibTableColumn
psMonthlyAvrVoltage=_PsMonthlyAvrVoltage_Object((1,3,6,1,4,1,6050,1,10,3,1,4),_PsMonthlyAvrVoltage_Type())
psMonthlyAvrVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyAvrVoltage.setStatus(_A)
_PsMonthlyMinCurrent_Type=Integer32
_PsMonthlyMinCurrent_Object=MibTableColumn
psMonthlyMinCurrent=_PsMonthlyMinCurrent_Object((1,3,6,1,4,1,6050,1,10,3,1,5),_PsMonthlyMinCurrent_Type())
psMonthlyMinCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyMinCurrent.setStatus(_A)
_PsMonthlyMaxCurrent_Type=Integer32
_PsMonthlyMaxCurrent_Object=MibTableColumn
psMonthlyMaxCurrent=_PsMonthlyMaxCurrent_Object((1,3,6,1,4,1,6050,1,10,3,1,6),_PsMonthlyMaxCurrent_Type())
psMonthlyMaxCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyMaxCurrent.setStatus(_A)
_PsMonthlyAvrCurrent_Type=Integer32
_PsMonthlyAvrCurrent_Object=MibTableColumn
psMonthlyAvrCurrent=_PsMonthlyAvrCurrent_Object((1,3,6,1,4,1,6050,1,10,3,1,7),_PsMonthlyAvrCurrent_Type())
psMonthlyAvrCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyAvrCurrent.setStatus(_A)
class _PsMonthlyMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_PsMonthlyMonth_Type.__name__=_C
_PsMonthlyMonth_Object=MibTableColumn
psMonthlyMonth=_PsMonthlyMonth_Object((1,3,6,1,4,1,6050,1,10,3,1,8),_PsMonthlyMonth_Type())
psMonthlyMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyMonth.setStatus(_A)
_PsHourlyFirst_Type=Integer32
_PsHourlyFirst_Object=MibScalar
psHourlyFirst=_PsHourlyFirst_Object((1,3,6,1,4,1,6050,1,10,4),_PsHourlyFirst_Type())
psHourlyFirst.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyFirst.setStatus(_A)
_PsHourlyLast_Type=Integer32
_PsHourlyLast_Object=MibScalar
psHourlyLast=_PsHourlyLast_Object((1,3,6,1,4,1,6050,1,10,5),_PsHourlyLast_Type())
psHourlyLast.setMaxAccess(_D)
if mibBuilder.loadTexts:psHourlyLast.setStatus(_A)
_PsDailyFirst_Type=Integer32
_PsDailyFirst_Object=MibScalar
psDailyFirst=_PsDailyFirst_Object((1,3,6,1,4,1,6050,1,10,6),_PsDailyFirst_Type())
psDailyFirst.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyFirst.setStatus(_A)
_PsDailyLast_Type=Integer32
_PsDailyLast_Object=MibScalar
psDailyLast=_PsDailyLast_Object((1,3,6,1,4,1,6050,1,10,7),_PsDailyLast_Type())
psDailyLast.setMaxAccess(_D)
if mibBuilder.loadTexts:psDailyLast.setStatus(_A)
_PsMonthlyFirst_Type=Integer32
_PsMonthlyFirst_Object=MibScalar
psMonthlyFirst=_PsMonthlyFirst_Object((1,3,6,1,4,1,6050,1,10,8),_PsMonthlyFirst_Type())
psMonthlyFirst.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyFirst.setStatus(_A)
_PsMonthlyLast_Type=Integer32
_PsMonthlyLast_Object=MibScalar
psMonthlyLast=_PsMonthlyLast_Object((1,3,6,1,4,1,6050,1,10,9),_PsMonthlyLast_Type())
psMonthlyLast.setMaxAccess(_D)
if mibBuilder.loadTexts:psMonthlyLast.setStatus(_A)
_PsLog_ObjectIdentity=ObjectIdentity
psLog=_PsLog_ObjectIdentity((1,3,6,1,4,1,6050,1,11))
_PsLogTable_Object=MibTable
psLogTable=_PsLogTable_Object((1,3,6,1,4,1,6050,1,11,1))
if mibBuilder.loadTexts:psLogTable.setStatus(_A)
_PsLogEntry_Object=MibTableRow
psLogEntry=_PsLogEntry_Object((1,3,6,1,4,1,6050,1,11,1,1))
psLogEntry.setIndexNames((0,_N,_t))
if mibBuilder.loadTexts:psLogEntry.setStatus(_A)
_PsLogIndex_Type=Integer32
_PsLogIndex_Object=MibTableColumn
psLogIndex=_PsLogIndex_Object((1,3,6,1,4,1,6050,1,11,1,1,1),_PsLogIndex_Type())
psLogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogIndex.setStatus(_A)
_PsLogDateYear_Type=Integer32
_PsLogDateYear_Object=MibTableColumn
psLogDateYear=_PsLogDateYear_Object((1,3,6,1,4,1,6050,1,11,1,1,2),_PsLogDateYear_Type())
psLogDateYear.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateYear.setStatus(_A)
_PsLogDateMonth_Type=Integer32
_PsLogDateMonth_Object=MibTableColumn
psLogDateMonth=_PsLogDateMonth_Object((1,3,6,1,4,1,6050,1,11,1,1,3),_PsLogDateMonth_Type())
psLogDateMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateMonth.setStatus(_A)
_PsLogDateDay_Type=Integer32
_PsLogDateDay_Object=MibTableColumn
psLogDateDay=_PsLogDateDay_Object((1,3,6,1,4,1,6050,1,11,1,1,4),_PsLogDateDay_Type())
psLogDateDay.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateDay.setStatus(_A)
_PsLogDateHour_Type=Integer32
_PsLogDateHour_Object=MibTableColumn
psLogDateHour=_PsLogDateHour_Object((1,3,6,1,4,1,6050,1,11,1,1,5),_PsLogDateHour_Type())
psLogDateHour.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateHour.setStatus(_A)
_PsLogDateMinute_Type=Integer32
_PsLogDateMinute_Object=MibTableColumn
psLogDateMinute=_PsLogDateMinute_Object((1,3,6,1,4,1,6050,1,11,1,1,6),_PsLogDateMinute_Type())
psLogDateMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateMinute.setStatus(_A)
_PsLogDateSecond_Type=Integer32
_PsLogDateSecond_Object=MibTableColumn
psLogDateSecond=_PsLogDateSecond_Object((1,3,6,1,4,1,6050,1,11,1,1,7),_PsLogDateSecond_Type())
psLogDateSecond.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateSecond.setStatus(_A)
_PsLogDCVoltage_Type=Integer32
_PsLogDCVoltage_Object=MibTableColumn
psLogDCVoltage=_PsLogDCVoltage_Object((1,3,6,1,4,1,6050,1,11,1,1,8),_PsLogDCVoltage_Type())
psLogDCVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDCVoltage.setStatus(_A)
_PsLogStatus_Type=Integer32
_PsLogStatus_Object=MibTableColumn
psLogStatus=_PsLogStatus_Object((1,3,6,1,4,1,6050,1,11,1,1,9),_PsLogStatus_Type())
psLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogStatus.setStatus(_A)
_PsLogAlarmCode_Type=Integer32
_PsLogAlarmCode_Object=MibTableColumn
psLogAlarmCode=_PsLogAlarmCode_Object((1,3,6,1,4,1,6050,1,11,1,1,10),_PsLogAlarmCode_Type())
psLogAlarmCode.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogAlarmCode.setStatus(_A)
_PsLogDateTime_Type=Integer32
_PsLogDateTime_Object=MibTableColumn
psLogDateTime=_PsLogDateTime_Object((1,3,6,1,4,1,6050,1,11,1,1,11),_PsLogDateTime_Type())
psLogDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogDateTime.setStatus(_A)
_PsLogGeneral_Type=Integer32
_PsLogGeneral_Object=MibTableColumn
psLogGeneral=_PsLogGeneral_Object((1,3,6,1,4,1,6050,1,11,1,1,12),_PsLogGeneral_Type())
psLogGeneral.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogGeneral.setStatus(_A)
_PsLogFirst_Type=Integer32
_PsLogFirst_Object=MibScalar
psLogFirst=_PsLogFirst_Object((1,3,6,1,4,1,6050,1,11,2),_PsLogFirst_Type())
psLogFirst.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogFirst.setStatus(_A)
_PsLogLast_Type=Integer32
_PsLogLast_Object=MibScalar
psLogLast=_PsLogLast_Object((1,3,6,1,4,1,6050,1,11,3),_PsLogLast_Type())
psLogLast.setMaxAccess(_D)
if mibBuilder.loadTexts:psLogLast.setStatus(_A)
_PsTrap_ObjectIdentity=ObjectIdentity
psTrap=_PsTrap_ObjectIdentity((1,3,6,1,4,1,6050,1,12))
_PsTrapSeverity_Type=PsAlarmSeverity
_PsTrapSeverity_Object=MibScalar
psTrapSeverity=_PsTrapSeverity_Object((1,3,6,1,4,1,6050,1,12,1),_PsTrapSeverity_Type())
psTrapSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:psTrapSeverity.setStatus(_A)
class _PsTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),(_Z,1)))
_PsTrapStatus_Type.__name__=_C
_PsTrapStatus_Object=MibScalar
psTrapStatus=_PsTrapStatus_Object((1,3,6,1,4,1,6050,1,12,2),_PsTrapStatus_Type())
psTrapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psTrapStatus.setStatus(_A)
class _PsTrapActivation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),(_Z,1)))
_PsTrapActivation_Type.__name__=_C
_PsTrapActivation_Object=MibScalar
psTrapActivation=_PsTrapActivation_Object((1,3,6,1,4,1,6050,1,12,3),_PsTrapActivation_Type())
psTrapActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:psTrapActivation.setStatus(_A)
_PsAlarm1006_ObjectIdentity=ObjectIdentity
psAlarm1006=_PsAlarm1006_ObjectIdentity((1,3,6,1,4,1,6050,1,12,10))
_PsTrapPrefix1006_ObjectIdentity=ObjectIdentity
psTrapPrefix1006=_PsTrapPrefix1006_ObjectIdentity((1,3,6,1,4,1,6050,1,12,10,0))
_PsAlarm_ObjectIdentity=ObjectIdentity
psAlarm=_PsAlarm_ObjectIdentity((1,3,6,1,4,1,6050,1,12,11))
_PsTrapPrefix_ObjectIdentity=ObjectIdentity
psTrapPrefix=_PsTrapPrefix_ObjectIdentity((1,3,6,1,4,1,6050,1,12,11,0))
_PsAlarmSet_ObjectIdentity=ObjectIdentity
psAlarmSet=_PsAlarmSet_ObjectIdentity((1,3,6,1,4,1,6050,1,13))
class _PsAlarmSet1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet1_Type.__name__=_C
_PsAlarmSet1_Object=MibScalar
psAlarmSet1=_PsAlarmSet1_Object((1,3,6,1,4,1,6050,1,13,1),_PsAlarmSet1_Type())
psAlarmSet1.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet1.setStatus(_A)
class _PsAlarmSet2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet2_Type.__name__=_C
_PsAlarmSet2_Object=MibScalar
psAlarmSet2=_PsAlarmSet2_Object((1,3,6,1,4,1,6050,1,13,2),_PsAlarmSet2_Type())
psAlarmSet2.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet2.setStatus(_A)
class _PsAlarmSet3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet3_Type.__name__=_C
_PsAlarmSet3_Object=MibScalar
psAlarmSet3=_PsAlarmSet3_Object((1,3,6,1,4,1,6050,1,13,3),_PsAlarmSet3_Type())
psAlarmSet3.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet3.setStatus(_A)
class _PsAlarmSet4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet4_Type.__name__=_C
_PsAlarmSet4_Object=MibScalar
psAlarmSet4=_PsAlarmSet4_Object((1,3,6,1,4,1,6050,1,13,4),_PsAlarmSet4_Type())
psAlarmSet4.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet4.setStatus(_A)
class _PsAlarmSet5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet5_Type.__name__=_C
_PsAlarmSet5_Object=MibScalar
psAlarmSet5=_PsAlarmSet5_Object((1,3,6,1,4,1,6050,1,13,5),_PsAlarmSet5_Type())
psAlarmSet5.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet5.setStatus(_A)
class _PsAlarmSet6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet6_Type.__name__=_C
_PsAlarmSet6_Object=MibScalar
psAlarmSet6=_PsAlarmSet6_Object((1,3,6,1,4,1,6050,1,13,6),_PsAlarmSet6_Type())
psAlarmSet6.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet6.setStatus(_A)
class _PsAlarmSet7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet7_Type.__name__=_C
_PsAlarmSet7_Object=MibScalar
psAlarmSet7=_PsAlarmSet7_Object((1,3,6,1,4,1,6050,1,13,7),_PsAlarmSet7_Type())
psAlarmSet7.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet7.setStatus(_A)
class _PsAlarmSet8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet8_Type.__name__=_C
_PsAlarmSet8_Object=MibScalar
psAlarmSet8=_PsAlarmSet8_Object((1,3,6,1,4,1,6050,1,13,8),_PsAlarmSet8_Type())
psAlarmSet8.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet8.setStatus(_A)
class _PsAlarmSet9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet9_Type.__name__=_C
_PsAlarmSet9_Object=MibScalar
psAlarmSet9=_PsAlarmSet9_Object((1,3,6,1,4,1,6050,1,13,9),_PsAlarmSet9_Type())
psAlarmSet9.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet9.setStatus(_A)
class _PsAlarmSet10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet10_Type.__name__=_C
_PsAlarmSet10_Object=MibScalar
psAlarmSet10=_PsAlarmSet10_Object((1,3,6,1,4,1,6050,1,13,10),_PsAlarmSet10_Type())
psAlarmSet10.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet10.setStatus(_A)
class _PsAlarmSet11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet11_Type.__name__=_C
_PsAlarmSet11_Object=MibScalar
psAlarmSet11=_PsAlarmSet11_Object((1,3,6,1,4,1,6050,1,13,11),_PsAlarmSet11_Type())
psAlarmSet11.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet11.setStatus(_A)
class _PsAlarmSet12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet12_Type.__name__=_C
_PsAlarmSet12_Object=MibScalar
psAlarmSet12=_PsAlarmSet12_Object((1,3,6,1,4,1,6050,1,13,12),_PsAlarmSet12_Type())
psAlarmSet12.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet12.setStatus(_A)
class _PsAlarmSet13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet13_Type.__name__=_C
_PsAlarmSet13_Object=MibScalar
psAlarmSet13=_PsAlarmSet13_Object((1,3,6,1,4,1,6050,1,13,13),_PsAlarmSet13_Type())
psAlarmSet13.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet13.setStatus(_A)
class _PsAlarmSet14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet14_Type.__name__=_C
_PsAlarmSet14_Object=MibScalar
psAlarmSet14=_PsAlarmSet14_Object((1,3,6,1,4,1,6050,1,13,14),_PsAlarmSet14_Type())
psAlarmSet14.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet14.setStatus(_A)
class _PsAlarmSet15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet15_Type.__name__=_C
_PsAlarmSet15_Object=MibScalar
psAlarmSet15=_PsAlarmSet15_Object((1,3,6,1,4,1,6050,1,13,15),_PsAlarmSet15_Type())
psAlarmSet15.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet15.setStatus(_A)
class _PsAlarmSet16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet16_Type.__name__=_C
_PsAlarmSet16_Object=MibScalar
psAlarmSet16=_PsAlarmSet16_Object((1,3,6,1,4,1,6050,1,13,16),_PsAlarmSet16_Type())
psAlarmSet16.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet16.setStatus(_A)
class _PsAlarmSet17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet17_Type.__name__=_C
_PsAlarmSet17_Object=MibScalar
psAlarmSet17=_PsAlarmSet17_Object((1,3,6,1,4,1,6050,1,13,17),_PsAlarmSet17_Type())
psAlarmSet17.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet17.setStatus(_A)
class _PsAlarmSet18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet18_Type.__name__=_C
_PsAlarmSet18_Object=MibScalar
psAlarmSet18=_PsAlarmSet18_Object((1,3,6,1,4,1,6050,1,13,18),_PsAlarmSet18_Type())
psAlarmSet18.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet18.setStatus(_A)
class _PsAlarmSet19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet19_Type.__name__=_C
_PsAlarmSet19_Object=MibScalar
psAlarmSet19=_PsAlarmSet19_Object((1,3,6,1,4,1,6050,1,13,19),_PsAlarmSet19_Type())
psAlarmSet19.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet19.setStatus(_A)
class _PsAlarmSet20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet20_Type.__name__=_C
_PsAlarmSet20_Object=MibScalar
psAlarmSet20=_PsAlarmSet20_Object((1,3,6,1,4,1,6050,1,13,20),_PsAlarmSet20_Type())
psAlarmSet20.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet20.setStatus(_A)
class _PsAlarmSet21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet21_Type.__name__=_C
_PsAlarmSet21_Object=MibScalar
psAlarmSet21=_PsAlarmSet21_Object((1,3,6,1,4,1,6050,1,13,21),_PsAlarmSet21_Type())
psAlarmSet21.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet21.setStatus(_A)
class _PsAlarmSet22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet22_Type.__name__=_C
_PsAlarmSet22_Object=MibScalar
psAlarmSet22=_PsAlarmSet22_Object((1,3,6,1,4,1,6050,1,13,22),_PsAlarmSet22_Type())
psAlarmSet22.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet22.setStatus(_A)
class _PsAlarmSet23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet23_Type.__name__=_C
_PsAlarmSet23_Object=MibScalar
psAlarmSet23=_PsAlarmSet23_Object((1,3,6,1,4,1,6050,1,13,23),_PsAlarmSet23_Type())
psAlarmSet23.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet23.setStatus(_A)
class _PsAlarmSet24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet24_Type.__name__=_C
_PsAlarmSet24_Object=MibScalar
psAlarmSet24=_PsAlarmSet24_Object((1,3,6,1,4,1,6050,1,13,24),_PsAlarmSet24_Type())
psAlarmSet24.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet24.setStatus(_A)
class _PsAlarmSet25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet25_Type.__name__=_C
_PsAlarmSet25_Object=MibScalar
psAlarmSet25=_PsAlarmSet25_Object((1,3,6,1,4,1,6050,1,13,25),_PsAlarmSet25_Type())
psAlarmSet25.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet25.setStatus(_A)
class _PsAlarmSet26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet26_Type.__name__=_C
_PsAlarmSet26_Object=MibScalar
psAlarmSet26=_PsAlarmSet26_Object((1,3,6,1,4,1,6050,1,13,26),_PsAlarmSet26_Type())
psAlarmSet26.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet26.setStatus(_A)
class _PsAlarmSet27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet27_Type.__name__=_C
_PsAlarmSet27_Object=MibScalar
psAlarmSet27=_PsAlarmSet27_Object((1,3,6,1,4,1,6050,1,13,27),_PsAlarmSet27_Type())
psAlarmSet27.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet27.setStatus(_A)
class _PsAlarmSet28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet28_Type.__name__=_C
_PsAlarmSet28_Object=MibScalar
psAlarmSet28=_PsAlarmSet28_Object((1,3,6,1,4,1,6050,1,13,28),_PsAlarmSet28_Type())
psAlarmSet28.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet28.setStatus(_A)
class _PsAlarmSet29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet29_Type.__name__=_C
_PsAlarmSet29_Object=MibScalar
psAlarmSet29=_PsAlarmSet29_Object((1,3,6,1,4,1,6050,1,13,29),_PsAlarmSet29_Type())
psAlarmSet29.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet29.setStatus(_A)
class _PsAlarmSet30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet30_Type.__name__=_C
_PsAlarmSet30_Object=MibScalar
psAlarmSet30=_PsAlarmSet30_Object((1,3,6,1,4,1,6050,1,13,30),_PsAlarmSet30_Type())
psAlarmSet30.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet30.setStatus(_A)
class _PsAlarmSet31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet31_Type.__name__=_C
_PsAlarmSet31_Object=MibScalar
psAlarmSet31=_PsAlarmSet31_Object((1,3,6,1,4,1,6050,1,13,31),_PsAlarmSet31_Type())
psAlarmSet31.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet31.setStatus(_A)
class _PsAlarmSet32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet32_Type.__name__=_C
_PsAlarmSet32_Object=MibScalar
psAlarmSet32=_PsAlarmSet32_Object((1,3,6,1,4,1,6050,1,13,32),_PsAlarmSet32_Type())
psAlarmSet32.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet32.setStatus(_A)
class _PsAlarmSet33_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet33_Type.__name__=_C
_PsAlarmSet33_Object=MibScalar
psAlarmSet33=_PsAlarmSet33_Object((1,3,6,1,4,1,6050,1,13,33),_PsAlarmSet33_Type())
psAlarmSet33.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet33.setStatus(_A)
class _PsAlarmSet34_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet34_Type.__name__=_C
_PsAlarmSet34_Object=MibScalar
psAlarmSet34=_PsAlarmSet34_Object((1,3,6,1,4,1,6050,1,13,34),_PsAlarmSet34_Type())
psAlarmSet34.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet34.setStatus(_A)
class _PsAlarmSet35_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet35_Type.__name__=_C
_PsAlarmSet35_Object=MibScalar
psAlarmSet35=_PsAlarmSet35_Object((1,3,6,1,4,1,6050,1,13,35),_PsAlarmSet35_Type())
psAlarmSet35.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet35.setStatus(_A)
class _PsAlarmSet36_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet36_Type.__name__=_C
_PsAlarmSet36_Object=MibScalar
psAlarmSet36=_PsAlarmSet36_Object((1,3,6,1,4,1,6050,1,13,36),_PsAlarmSet36_Type())
psAlarmSet36.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet36.setStatus(_A)
class _PsAlarmSet37_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet37_Type.__name__=_C
_PsAlarmSet37_Object=MibScalar
psAlarmSet37=_PsAlarmSet37_Object((1,3,6,1,4,1,6050,1,13,37),_PsAlarmSet37_Type())
psAlarmSet37.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet37.setStatus(_A)
class _PsAlarmSet38_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet38_Type.__name__=_C
_PsAlarmSet38_Object=MibScalar
psAlarmSet38=_PsAlarmSet38_Object((1,3,6,1,4,1,6050,1,13,38),_PsAlarmSet38_Type())
psAlarmSet38.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet38.setStatus(_A)
class _PsAlarmSet39_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet39_Type.__name__=_C
_PsAlarmSet39_Object=MibScalar
psAlarmSet39=_PsAlarmSet39_Object((1,3,6,1,4,1,6050,1,13,39),_PsAlarmSet39_Type())
psAlarmSet39.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet39.setStatus(_A)
class _PsAlarmSet40_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet40_Type.__name__=_C
_PsAlarmSet40_Object=MibScalar
psAlarmSet40=_PsAlarmSet40_Object((1,3,6,1,4,1,6050,1,13,40),_PsAlarmSet40_Type())
psAlarmSet40.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet40.setStatus(_A)
class _PsAlarmSet41_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet41_Type.__name__=_C
_PsAlarmSet41_Object=MibScalar
psAlarmSet41=_PsAlarmSet41_Object((1,3,6,1,4,1,6050,1,13,41),_PsAlarmSet41_Type())
psAlarmSet41.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet41.setStatus(_A)
class _PsAlarmSet42_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet42_Type.__name__=_C
_PsAlarmSet42_Object=MibScalar
psAlarmSet42=_PsAlarmSet42_Object((1,3,6,1,4,1,6050,1,13,42),_PsAlarmSet42_Type())
psAlarmSet42.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet42.setStatus(_A)
class _PsAlarmSet43_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet43_Type.__name__=_C
_PsAlarmSet43_Object=MibScalar
psAlarmSet43=_PsAlarmSet43_Object((1,3,6,1,4,1,6050,1,13,43),_PsAlarmSet43_Type())
psAlarmSet43.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet43.setStatus(_A)
class _PsAlarmSet44_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet44_Type.__name__=_C
_PsAlarmSet44_Object=MibScalar
psAlarmSet44=_PsAlarmSet44_Object((1,3,6,1,4,1,6050,1,13,44),_PsAlarmSet44_Type())
psAlarmSet44.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet44.setStatus(_A)
class _PsAlarmSet45_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet45_Type.__name__=_C
_PsAlarmSet45_Object=MibScalar
psAlarmSet45=_PsAlarmSet45_Object((1,3,6,1,4,1,6050,1,13,45),_PsAlarmSet45_Type())
psAlarmSet45.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet45.setStatus(_A)
class _PsAlarmSet46_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet46_Type.__name__=_C
_PsAlarmSet46_Object=MibScalar
psAlarmSet46=_PsAlarmSet46_Object((1,3,6,1,4,1,6050,1,13,46),_PsAlarmSet46_Type())
psAlarmSet46.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet46.setStatus(_A)
class _PsAlarmSet47_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet47_Type.__name__=_C
_PsAlarmSet47_Object=MibScalar
psAlarmSet47=_PsAlarmSet47_Object((1,3,6,1,4,1,6050,1,13,47),_PsAlarmSet47_Type())
psAlarmSet47.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet47.setStatus(_A)
class _PsAlarmSet48_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet48_Type.__name__=_C
_PsAlarmSet48_Object=MibScalar
psAlarmSet48=_PsAlarmSet48_Object((1,3,6,1,4,1,6050,1,13,48),_PsAlarmSet48_Type())
psAlarmSet48.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet48.setStatus(_A)
class _PsAlarmSet49_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet49_Type.__name__=_C
_PsAlarmSet49_Object=MibScalar
psAlarmSet49=_PsAlarmSet49_Object((1,3,6,1,4,1,6050,1,13,49),_PsAlarmSet49_Type())
psAlarmSet49.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet49.setStatus(_A)
class _PsAlarmSet50_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet50_Type.__name__=_C
_PsAlarmSet50_Object=MibScalar
psAlarmSet50=_PsAlarmSet50_Object((1,3,6,1,4,1,6050,1,13,50),_PsAlarmSet50_Type())
psAlarmSet50.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet50.setStatus(_A)
class _PsAlarmSet51_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet51_Type.__name__=_C
_PsAlarmSet51_Object=MibScalar
psAlarmSet51=_PsAlarmSet51_Object((1,3,6,1,4,1,6050,1,13,51),_PsAlarmSet51_Type())
psAlarmSet51.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet51.setStatus(_A)
class _PsAlarmSet52_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet52_Type.__name__=_C
_PsAlarmSet52_Object=MibScalar
psAlarmSet52=_PsAlarmSet52_Object((1,3,6,1,4,1,6050,1,13,52),_PsAlarmSet52_Type())
psAlarmSet52.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet52.setStatus(_A)
class _PsAlarmSet53_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet53_Type.__name__=_C
_PsAlarmSet53_Object=MibScalar
psAlarmSet53=_PsAlarmSet53_Object((1,3,6,1,4,1,6050,1,13,53),_PsAlarmSet53_Type())
psAlarmSet53.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet53.setStatus(_A)
class _PsAlarmSet54_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet54_Type.__name__=_C
_PsAlarmSet54_Object=MibScalar
psAlarmSet54=_PsAlarmSet54_Object((1,3,6,1,4,1,6050,1,13,54),_PsAlarmSet54_Type())
psAlarmSet54.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet54.setStatus(_A)
class _PsAlarmSet55_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet55_Type.__name__=_C
_PsAlarmSet55_Object=MibScalar
psAlarmSet55=_PsAlarmSet55_Object((1,3,6,1,4,1,6050,1,13,55),_PsAlarmSet55_Type())
psAlarmSet55.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet55.setStatus(_A)
class _PsAlarmSet56_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet56_Type.__name__=_C
_PsAlarmSet56_Object=MibScalar
psAlarmSet56=_PsAlarmSet56_Object((1,3,6,1,4,1,6050,1,13,56),_PsAlarmSet56_Type())
psAlarmSet56.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet56.setStatus(_A)
class _PsAlarmSet57_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet57_Type.__name__=_C
_PsAlarmSet57_Object=MibScalar
psAlarmSet57=_PsAlarmSet57_Object((1,3,6,1,4,1,6050,1,13,57),_PsAlarmSet57_Type())
psAlarmSet57.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet57.setStatus(_A)
class _PsAlarmSet58_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet58_Type.__name__=_C
_PsAlarmSet58_Object=MibScalar
psAlarmSet58=_PsAlarmSet58_Object((1,3,6,1,4,1,6050,1,13,58),_PsAlarmSet58_Type())
psAlarmSet58.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet58.setStatus(_A)
class _PsAlarmSet59_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet59_Type.__name__=_C
_PsAlarmSet59_Object=MibScalar
psAlarmSet59=_PsAlarmSet59_Object((1,3,6,1,4,1,6050,1,13,59),_PsAlarmSet59_Type())
psAlarmSet59.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet59.setStatus(_A)
class _PsAlarmSet60_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet60_Type.__name__=_C
_PsAlarmSet60_Object=MibScalar
psAlarmSet60=_PsAlarmSet60_Object((1,3,6,1,4,1,6050,1,13,60),_PsAlarmSet60_Type())
psAlarmSet60.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet60.setStatus(_A)
class _PsAlarmSet61_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet61_Type.__name__=_C
_PsAlarmSet61_Object=MibScalar
psAlarmSet61=_PsAlarmSet61_Object((1,3,6,1,4,1,6050,1,13,61),_PsAlarmSet61_Type())
psAlarmSet61.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet61.setStatus(_A)
class _PsAlarmSet62_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet62_Type.__name__=_C
_PsAlarmSet62_Object=MibScalar
psAlarmSet62=_PsAlarmSet62_Object((1,3,6,1,4,1,6050,1,13,62),_PsAlarmSet62_Type())
psAlarmSet62.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet62.setStatus(_A)
class _PsAlarmSet63_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet63_Type.__name__=_C
_PsAlarmSet63_Object=MibScalar
psAlarmSet63=_PsAlarmSet63_Object((1,3,6,1,4,1,6050,1,13,63),_PsAlarmSet63_Type())
psAlarmSet63.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet63.setStatus(_A)
class _PsAlarmSet64_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet64_Type.__name__=_C
_PsAlarmSet64_Object=MibScalar
psAlarmSet64=_PsAlarmSet64_Object((1,3,6,1,4,1,6050,1,13,64),_PsAlarmSet64_Type())
psAlarmSet64.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet64.setStatus(_A)
class _PsAlarmSet65_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet65_Type.__name__=_C
_PsAlarmSet65_Object=MibScalar
psAlarmSet65=_PsAlarmSet65_Object((1,3,6,1,4,1,6050,1,13,65),_PsAlarmSet65_Type())
psAlarmSet65.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet65.setStatus(_A)
class _PsAlarmSet66_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet66_Type.__name__=_C
_PsAlarmSet66_Object=MibScalar
psAlarmSet66=_PsAlarmSet66_Object((1,3,6,1,4,1,6050,1,13,66),_PsAlarmSet66_Type())
psAlarmSet66.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet66.setStatus(_A)
class _PsAlarmSet67_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet67_Type.__name__=_C
_PsAlarmSet67_Object=MibScalar
psAlarmSet67=_PsAlarmSet67_Object((1,3,6,1,4,1,6050,1,13,67),_PsAlarmSet67_Type())
psAlarmSet67.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet67.setStatus(_A)
class _PsAlarmSet68_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet68_Type.__name__=_C
_PsAlarmSet68_Object=MibScalar
psAlarmSet68=_PsAlarmSet68_Object((1,3,6,1,4,1,6050,1,13,68),_PsAlarmSet68_Type())
psAlarmSet68.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet68.setStatus(_A)
class _PsAlarmSet69_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet69_Type.__name__=_C
_PsAlarmSet69_Object=MibScalar
psAlarmSet69=_PsAlarmSet69_Object((1,3,6,1,4,1,6050,1,13,69),_PsAlarmSet69_Type())
psAlarmSet69.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet69.setStatus(_A)
class _PsAlarmSet70_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet70_Type.__name__=_C
_PsAlarmSet70_Object=MibScalar
psAlarmSet70=_PsAlarmSet70_Object((1,3,6,1,4,1,6050,1,13,70),_PsAlarmSet70_Type())
psAlarmSet70.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet70.setStatus(_A)
class _PsAlarmSet71_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet71_Type.__name__=_C
_PsAlarmSet71_Object=MibScalar
psAlarmSet71=_PsAlarmSet71_Object((1,3,6,1,4,1,6050,1,13,71),_PsAlarmSet71_Type())
psAlarmSet71.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet71.setStatus(_A)
class _PsAlarmSet72_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet72_Type.__name__=_C
_PsAlarmSet72_Object=MibScalar
psAlarmSet72=_PsAlarmSet72_Object((1,3,6,1,4,1,6050,1,13,72),_PsAlarmSet72_Type())
psAlarmSet72.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet72.setStatus(_A)
class _PsAlarmSet73_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet73_Type.__name__=_C
_PsAlarmSet73_Object=MibScalar
psAlarmSet73=_PsAlarmSet73_Object((1,3,6,1,4,1,6050,1,13,73),_PsAlarmSet73_Type())
psAlarmSet73.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet73.setStatus(_A)
class _PsAlarmSet74_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet74_Type.__name__=_C
_PsAlarmSet74_Object=MibScalar
psAlarmSet74=_PsAlarmSet74_Object((1,3,6,1,4,1,6050,1,13,74),_PsAlarmSet74_Type())
psAlarmSet74.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet74.setStatus(_A)
class _PsAlarmSet75_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet75_Type.__name__=_C
_PsAlarmSet75_Object=MibScalar
psAlarmSet75=_PsAlarmSet75_Object((1,3,6,1,4,1,6050,1,13,75),_PsAlarmSet75_Type())
psAlarmSet75.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet75.setStatus(_A)
class _PsAlarmSet76_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet76_Type.__name__=_C
_PsAlarmSet76_Object=MibScalar
psAlarmSet76=_PsAlarmSet76_Object((1,3,6,1,4,1,6050,1,13,76),_PsAlarmSet76_Type())
psAlarmSet76.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet76.setStatus(_A)
class _PsAlarmSet77_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet77_Type.__name__=_C
_PsAlarmSet77_Object=MibScalar
psAlarmSet77=_PsAlarmSet77_Object((1,3,6,1,4,1,6050,1,13,77),_PsAlarmSet77_Type())
psAlarmSet77.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet77.setStatus(_A)
class _PsAlarmSet78_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet78_Type.__name__=_C
_PsAlarmSet78_Object=MibScalar
psAlarmSet78=_PsAlarmSet78_Object((1,3,6,1,4,1,6050,1,13,78),_PsAlarmSet78_Type())
psAlarmSet78.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet78.setStatus(_A)
class _PsAlarmSet79_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet79_Type.__name__=_C
_PsAlarmSet79_Object=MibScalar
psAlarmSet79=_PsAlarmSet79_Object((1,3,6,1,4,1,6050,1,13,79),_PsAlarmSet79_Type())
psAlarmSet79.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet79.setStatus(_A)
class _PsAlarmSet80_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet80_Type.__name__=_C
_PsAlarmSet80_Object=MibScalar
psAlarmSet80=_PsAlarmSet80_Object((1,3,6,1,4,1,6050,1,13,80),_PsAlarmSet80_Type())
psAlarmSet80.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet80.setStatus(_A)
class _PsAlarmSet81_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet81_Type.__name__=_C
_PsAlarmSet81_Object=MibScalar
psAlarmSet81=_PsAlarmSet81_Object((1,3,6,1,4,1,6050,1,13,81),_PsAlarmSet81_Type())
psAlarmSet81.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet81.setStatus(_A)
class _PsAlarmSet82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet82_Type.__name__=_C
_PsAlarmSet82_Object=MibScalar
psAlarmSet82=_PsAlarmSet82_Object((1,3,6,1,4,1,6050,1,13,82),_PsAlarmSet82_Type())
psAlarmSet82.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet82.setStatus(_A)
class _PsAlarmSet83_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet83_Type.__name__=_C
_PsAlarmSet83_Object=MibScalar
psAlarmSet83=_PsAlarmSet83_Object((1,3,6,1,4,1,6050,1,13,83),_PsAlarmSet83_Type())
psAlarmSet83.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet83.setStatus(_A)
class _PsAlarmSet84_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet84_Type.__name__=_C
_PsAlarmSet84_Object=MibScalar
psAlarmSet84=_PsAlarmSet84_Object((1,3,6,1,4,1,6050,1,13,84),_PsAlarmSet84_Type())
psAlarmSet84.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet84.setStatus(_A)
class _PsAlarmSet85_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet85_Type.__name__=_C
_PsAlarmSet85_Object=MibScalar
psAlarmSet85=_PsAlarmSet85_Object((1,3,6,1,4,1,6050,1,13,85),_PsAlarmSet85_Type())
psAlarmSet85.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet85.setStatus(_A)
class _PsAlarmSet86_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet86_Type.__name__=_C
_PsAlarmSet86_Object=MibScalar
psAlarmSet86=_PsAlarmSet86_Object((1,3,6,1,4,1,6050,1,13,86),_PsAlarmSet86_Type())
psAlarmSet86.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet86.setStatus(_A)
class _PsAlarmSet87_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet87_Type.__name__=_C
_PsAlarmSet87_Object=MibScalar
psAlarmSet87=_PsAlarmSet87_Object((1,3,6,1,4,1,6050,1,13,87),_PsAlarmSet87_Type())
psAlarmSet87.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet87.setStatus(_A)
class _PsAlarmSet88_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet88_Type.__name__=_C
_PsAlarmSet88_Object=MibScalar
psAlarmSet88=_PsAlarmSet88_Object((1,3,6,1,4,1,6050,1,13,88),_PsAlarmSet88_Type())
psAlarmSet88.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet88.setStatus(_A)
class _PsAlarmSet89_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet89_Type.__name__=_C
_PsAlarmSet89_Object=MibScalar
psAlarmSet89=_PsAlarmSet89_Object((1,3,6,1,4,1,6050,1,13,89),_PsAlarmSet89_Type())
psAlarmSet89.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet89.setStatus(_A)
class _PsAlarmSet90_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet90_Type.__name__=_C
_PsAlarmSet90_Object=MibScalar
psAlarmSet90=_PsAlarmSet90_Object((1,3,6,1,4,1,6050,1,13,90),_PsAlarmSet90_Type())
psAlarmSet90.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet90.setStatus(_A)
class _PsAlarmSet91_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet91_Type.__name__=_C
_PsAlarmSet91_Object=MibScalar
psAlarmSet91=_PsAlarmSet91_Object((1,3,6,1,4,1,6050,1,13,91),_PsAlarmSet91_Type())
psAlarmSet91.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet91.setStatus(_A)
class _PsAlarmSet92_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet92_Type.__name__=_C
_PsAlarmSet92_Object=MibScalar
psAlarmSet92=_PsAlarmSet92_Object((1,3,6,1,4,1,6050,1,13,92),_PsAlarmSet92_Type())
psAlarmSet92.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet92.setStatus(_A)
class _PsAlarmSet93_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet93_Type.__name__=_C
_PsAlarmSet93_Object=MibScalar
psAlarmSet93=_PsAlarmSet93_Object((1,3,6,1,4,1,6050,1,13,93),_PsAlarmSet93_Type())
psAlarmSet93.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet93.setStatus(_A)
class _PsAlarmSet94_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet94_Type.__name__=_C
_PsAlarmSet94_Object=MibScalar
psAlarmSet94=_PsAlarmSet94_Object((1,3,6,1,4,1,6050,1,13,94),_PsAlarmSet94_Type())
psAlarmSet94.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet94.setStatus(_A)
class _PsAlarmSet95_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet95_Type.__name__=_C
_PsAlarmSet95_Object=MibScalar
psAlarmSet95=_PsAlarmSet95_Object((1,3,6,1,4,1,6050,1,13,95),_PsAlarmSet95_Type())
psAlarmSet95.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet95.setStatus(_A)
class _PsAlarmSet96_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_PsAlarmSet96_Type.__name__=_C
_PsAlarmSet96_Object=MibScalar
psAlarmSet96=_PsAlarmSet96_Object((1,3,6,1,4,1,6050,1,13,96),_PsAlarmSet96_Type())
psAlarmSet96.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmSet96.setStatus(_A)
_PsSecurity_ObjectIdentity=ObjectIdentity
psSecurity=_PsSecurity_ObjectIdentity((1,3,6,1,4,1,6050,1,14))
class _PsSecurityComunity1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PsSecurityComunity1_Type.__name__=_Q
_PsSecurityComunity1_Object=MibScalar
psSecurityComunity1=_PsSecurityComunity1_Object((1,3,6,1,4,1,6050,1,14,1),_PsSecurityComunity1_Type())
psSecurityComunity1.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityComunity1.setStatus(_A)
class _PsSecurityComunity2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PsSecurityComunity2_Type.__name__=_Q
_PsSecurityComunity2_Object=MibScalar
psSecurityComunity2=_PsSecurityComunity2_Object((1,3,6,1,4,1,6050,1,14,2),_PsSecurityComunity2_Type())
psSecurityComunity2.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityComunity2.setStatus(_A)
class _PsSecurityComunity3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PsSecurityComunity3_Type.__name__=_Q
_PsSecurityComunity3_Object=MibScalar
psSecurityComunity3=_PsSecurityComunity3_Object((1,3,6,1,4,1,6050,1,14,3),_PsSecurityComunity3_Type())
psSecurityComunity3.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityComunity3.setStatus(_A)
class _PsSecurityPasswordComunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PsSecurityPasswordComunity_Type.__name__=_Q
_PsSecurityPasswordComunity_Object=MibScalar
psSecurityPasswordComunity=_PsSecurityPasswordComunity_Object((1,3,6,1,4,1,6050,1,14,4),_PsSecurityPasswordComunity_Type())
psSecurityPasswordComunity.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityPasswordComunity.setStatus(_A)
class _PsSecurityPasswordSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PsSecurityPasswordSet_Type.__name__=_Q
_PsSecurityPasswordSet_Object=MibScalar
psSecurityPasswordSet=_PsSecurityPasswordSet_Object((1,3,6,1,4,1,6050,1,14,5),_PsSecurityPasswordSet_Type())
psSecurityPasswordSet.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityPasswordSet.setStatus(_A)
class _PsSecuritySetGetPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PsSecuritySetGetPassword_Type.__name__=_Q
_PsSecuritySetGetPassword_Object=MibScalar
psSecuritySetGetPassword=_PsSecuritySetGetPassword_Object((1,3,6,1,4,1,6050,1,14,6),_PsSecuritySetGetPassword_Type())
psSecuritySetGetPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecuritySetGetPassword.setStatus(_A)
class _PsSecurityErasePassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dont',0),('reset',1)))
_PsSecurityErasePassword_Type.__name__=_C
_PsSecurityErasePassword_Object=MibScalar
psSecurityErasePassword=_PsSecurityErasePassword_Object((1,3,6,1,4,1,6050,1,14,7),_PsSecurityErasePassword_Type())
psSecurityErasePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityErasePassword.setStatus(_A)
_PsSecurityTrapIp1_Type=IpAddress
_PsSecurityTrapIp1_Object=MibScalar
psSecurityTrapIp1=_PsSecurityTrapIp1_Object((1,3,6,1,4,1,6050,1,14,8),_PsSecurityTrapIp1_Type())
psSecurityTrapIp1.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityTrapIp1.setStatus(_A)
_PsSecurityTrapIp2_Type=IpAddress
_PsSecurityTrapIp2_Object=MibScalar
psSecurityTrapIp2=_PsSecurityTrapIp2_Object((1,3,6,1,4,1,6050,1,14,9),_PsSecurityTrapIp2_Type())
psSecurityTrapIp2.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityTrapIp2.setStatus(_A)
_PsSecurityTrapIp3_Type=IpAddress
_PsSecurityTrapIp3_Object=MibScalar
psSecurityTrapIp3=_PsSecurityTrapIp3_Object((1,3,6,1,4,1,6050,1,14,10),_PsSecurityTrapIp3_Type())
psSecurityTrapIp3.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityTrapIp3.setStatus(_A)
_PsSecurityTrapIp4_Type=IpAddress
_PsSecurityTrapIp4_Object=MibScalar
psSecurityTrapIp4=_PsSecurityTrapIp4_Object((1,3,6,1,4,1,6050,1,14,11),_PsSecurityTrapIp4_Type())
psSecurityTrapIp4.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityTrapIp4.setStatus(_A)
_PsSecurityInterfaceIP_Type=IpAddress
_PsSecurityInterfaceIP_Object=MibScalar
psSecurityInterfaceIP=_PsSecurityInterfaceIP_Object((1,3,6,1,4,1,6050,1,14,12),_PsSecurityInterfaceIP_Type())
psSecurityInterfaceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityInterfaceIP.setStatus(_A)
_PsSecurityInterfaceNetMask_Type=IpAddress
_PsSecurityInterfaceNetMask_Object=MibScalar
psSecurityInterfaceNetMask=_PsSecurityInterfaceNetMask_Object((1,3,6,1,4,1,6050,1,14,13),_PsSecurityInterfaceNetMask_Type())
psSecurityInterfaceNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityInterfaceNetMask.setStatus(_A)
_PsSecurityInterfaceGateWay_Type=IpAddress
_PsSecurityInterfaceGateWay_Object=MibScalar
psSecurityInterfaceGateWay=_PsSecurityInterfaceGateWay_Object((1,3,6,1,4,1,6050,1,14,14),_PsSecurityInterfaceGateWay_Type())
psSecurityInterfaceGateWay.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityInterfaceGateWay.setStatus(_A)
class _PsSecurityInterfaceActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('donot',0),(_U,1)))
_PsSecurityInterfaceActivate_Type.__name__=_C
_PsSecurityInterfaceActivate_Object=MibScalar
psSecurityInterfaceActivate=_PsSecurityInterfaceActivate_Object((1,3,6,1,4,1,6050,1,14,15),_PsSecurityInterfaceActivate_Type())
psSecurityInterfaceActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:psSecurityInterfaceActivate.setStatus(_A)
_PsCommand_ObjectIdentity=ObjectIdentity
psCommand=_PsCommand_ObjectIdentity((1,3,6,1,4,1,6050,1,15))
class _PsCommandGoFloat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsCommandGoFloat_Type.__name__=_C
_PsCommandGoFloat_Object=MibScalar
psCommandGoFloat=_PsCommandGoFloat_Object((1,3,6,1,4,1,6050,1,15,1),_PsCommandGoFloat_Type())
psCommandGoFloat.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandGoFloat.setStatus(_A)
class _PsCommandGoEqualizing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,72))
_PsCommandGoEqualizing_Type.__name__=_C
_PsCommandGoEqualizing_Object=MibScalar
psCommandGoEqualizing=_PsCommandGoEqualizing_Object((1,3,6,1,4,1,6050,1,15,2),_PsCommandGoEqualizing_Type())
psCommandGoEqualizing.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandGoEqualizing.setStatus(_A)
class _PsCommandDoSelfTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_T,1)))
_PsCommandDoSelfTest_Type.__name__=_C
_PsCommandDoSelfTest_Object=MibScalar
psCommandDoSelfTest=_PsCommandDoSelfTest_Object((1,3,6,1,4,1,6050,1,15,3),_PsCommandDoSelfTest_Type())
psCommandDoSelfTest.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandDoSelfTest.setStatus(_A)
class _PsCommandRunFlash1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_u,0),(_U,1)))
_PsCommandRunFlash1_Type.__name__=_C
_PsCommandRunFlash1_Object=MibScalar
psCommandRunFlash1=_PsCommandRunFlash1_Object((1,3,6,1,4,1,6050,1,15,4),_PsCommandRunFlash1_Type())
psCommandRunFlash1.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandRunFlash1.setStatus(_A)
class _PsCommandRunFlash2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_u,0),(_U,1)))
_PsCommandRunFlash2_Type.__name__=_C
_PsCommandRunFlash2_Object=MibScalar
psCommandRunFlash2=_PsCommandRunFlash2_Object((1,3,6,1,4,1,6050,1,15,5),_PsCommandRunFlash2_Type())
psCommandRunFlash2.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandRunFlash2.setStatus(_A)
class _PsCommandTestBatteryAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_PsCommandTestBatteryAll_Type.__name__=_C
_PsCommandTestBatteryAll_Object=MibScalar
psCommandTestBatteryAll=_PsCommandTestBatteryAll_Object((1,3,6,1,4,1,6050,1,15,6),_PsCommandTestBatteryAll_Type())
psCommandTestBatteryAll.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandTestBatteryAll.setStatus(_A)
class _PsCommandDoBoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dont',0),('do',1)))
_PsCommandDoBoot_Type.__name__=_C
_PsCommandDoBoot_Object=MibScalar
psCommandDoBoot=_PsCommandDoBoot_Object((1,3,6,1,4,1,6050,1,15,7),_PsCommandDoBoot_Type())
psCommandDoBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandDoBoot.setStatus(_A)
class _PsCommandLoadDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_v,0),('load',1)))
_PsCommandLoadDefault_Type.__name__=_C
_PsCommandLoadDefault_Object=MibScalar
psCommandLoadDefault=_PsCommandLoadDefault_Object((1,3,6,1,4,1,6050,1,15,8),_PsCommandLoadDefault_Type())
psCommandLoadDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandLoadDefault.setStatus(_A)
class _PsCommandProgramNonActiveFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_v,0),('load',1)))
_PsCommandProgramNonActiveFlash_Type.__name__=_C
_PsCommandProgramNonActiveFlash_Object=MibScalar
psCommandProgramNonActiveFlash=_PsCommandProgramNonActiveFlash_Object((1,3,6,1,4,1,6050,1,15,9),_PsCommandProgramNonActiveFlash_Type())
psCommandProgramNonActiveFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandProgramNonActiveFlash.setStatus(_A)
_PsCommandNonActiveFlash_Type=Integer32
_PsCommandNonActiveFlash_Object=MibScalar
psCommandNonActiveFlash=_PsCommandNonActiveFlash_Object((1,3,6,1,4,1,6050,1,15,10),_PsCommandNonActiveFlash_Type())
psCommandNonActiveFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandNonActiveFlash.setStatus(_A)
_PsCommandNonActiveStatus_Type=Integer32
_PsCommandNonActiveStatus_Object=MibScalar
psCommandNonActiveStatus=_PsCommandNonActiveStatus_Object((1,3,6,1,4,1,6050,1,15,11),_PsCommandNonActiveStatus_Type())
psCommandNonActiveStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandNonActiveStatus.setStatus(_A)
class _PsCommandDownLoadSoftware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandDownLoadSoftware_Type.__name__=_C
_PsCommandDownLoadSoftware_Object=MibScalar
psCommandDownLoadSoftware=_PsCommandDownLoadSoftware_Object((1,3,6,1,4,1,6050,1,15,12),_PsCommandDownLoadSoftware_Type())
psCommandDownLoadSoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandDownLoadSoftware.setStatus(_A)
class _PsCommandDownLoadCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('completeok',0),(_g,1),('notok1',2),('notok2',3),('notok3',4)))
_PsCommandDownLoadCheck_Type.__name__=_C
_PsCommandDownLoadCheck_Object=MibScalar
psCommandDownLoadCheck=_PsCommandDownLoadCheck_Object((1,3,6,1,4,1,6050,1,15,13),_PsCommandDownLoadCheck_Type())
psCommandDownLoadCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandDownLoadCheck.setStatus(_A)
_PsCommandFileName_Type=DisplayString
_PsCommandFileName_Object=MibScalar
psCommandFileName=_PsCommandFileName_Object((1,3,6,1,4,1,6050,1,15,14),_PsCommandFileName_Type())
psCommandFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandFileName.setStatus(_A)
_PsCommandIpAddress_Type=IpAddress
_PsCommandIpAddress_Object=MibScalar
psCommandIpAddress=_PsCommandIpAddress_Object((1,3,6,1,4,1,6050,1,15,15),_PsCommandIpAddress_Type())
psCommandIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandIpAddress.setStatus(_A)
class _PsCommandAbortBatTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('abort',1)))
_PsCommandAbortBatTest_Type.__name__=_C
_PsCommandAbortBatTest_Object=MibScalar
psCommandAbortBatTest=_PsCommandAbortBatTest_Object((1,3,6,1,4,1,6050,1,15,16),_PsCommandAbortBatTest_Type())
psCommandAbortBatTest.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandAbortBatTest.setStatus(_A)
class _PsCommandEraseTotalTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('erase',1)))
_PsCommandEraseTotalTime_Type.__name__=_C
_PsCommandEraseTotalTime_Object=MibScalar
psCommandEraseTotalTime=_PsCommandEraseTotalTime_Object((1,3,6,1,4,1,6050,1,15,17),_PsCommandEraseTotalTime_Type())
psCommandEraseTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandEraseTotalTime.setStatus(_A)
class _PsCommandAbortProgramFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandAbortProgramFlash_Type.__name__=_C
_PsCommandAbortProgramFlash_Object=MibScalar
psCommandAbortProgramFlash=_PsCommandAbortProgramFlash_Object((1,3,6,1,4,1,6050,1,15,18),_PsCommandAbortProgramFlash_Type())
psCommandAbortProgramFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandAbortProgramFlash.setStatus(_A)
class _PsCommandUserDefine2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandUserDefine2_Type.__name__=_C
_PsCommandUserDefine2_Object=MibScalar
psCommandUserDefine2=_PsCommandUserDefine2_Object((1,3,6,1,4,1,6050,1,15,19),_PsCommandUserDefine2_Type())
psCommandUserDefine2.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandUserDefine2.setStatus(_A)
class _PsCommandUserDefine3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandUserDefine3_Type.__name__=_C
_PsCommandUserDefine3_Object=MibScalar
psCommandUserDefine3=_PsCommandUserDefine3_Object((1,3,6,1,4,1,6050,1,15,20),_PsCommandUserDefine3_Type())
psCommandUserDefine3.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandUserDefine3.setStatus(_A)
class _PsCommandUserDefine4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandUserDefine4_Type.__name__=_C
_PsCommandUserDefine4_Object=MibScalar
psCommandUserDefine4=_PsCommandUserDefine4_Object((1,3,6,1,4,1,6050,1,15,21),_PsCommandUserDefine4_Type())
psCommandUserDefine4.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandUserDefine4.setStatus(_A)
class _PsCommandUserDefine5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandUserDefine5_Type.__name__=_C
_PsCommandUserDefine5_Object=MibScalar
psCommandUserDefine5=_PsCommandUserDefine5_Object((1,3,6,1,4,1,6050,1,15,22),_PsCommandUserDefine5_Type())
psCommandUserDefine5.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandUserDefine5.setStatus(_A)
_PsCommandFlash1Protect_Type=Integer32
_PsCommandFlash1Protect_Object=MibScalar
psCommandFlash1Protect=_PsCommandFlash1Protect_Object((1,3,6,1,4,1,6050,1,15,23),_PsCommandFlash1Protect_Type())
psCommandFlash1Protect.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFlash1Protect.setStatus(_A)
_PsCommandFlash2Protect_Type=Integer32
_PsCommandFlash2Protect_Object=MibScalar
psCommandFlash2Protect=_PsCommandFlash2Protect_Object((1,3,6,1,4,1,6050,1,15,24),_PsCommandFlash2Protect_Type())
psCommandFlash2Protect.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFlash2Protect.setStatus(_A)
_PsCommandFlashFix_Type=Integer32
_PsCommandFlashFix_Object=MibScalar
psCommandFlashFix=_PsCommandFlashFix_Object((1,3,6,1,4,1,6050,1,15,25),_PsCommandFlashFix_Type())
psCommandFlashFix.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFlashFix.setStatus(_A)
_PsCommandFlashFixNumber_Type=Integer32
_PsCommandFlashFixNumber_Object=MibScalar
psCommandFlashFixNumber=_PsCommandFlashFixNumber_Object((1,3,6,1,4,1,6050,1,15,26),_PsCommandFlashFixNumber_Type())
psCommandFlashFixNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFlashFixNumber.setStatus(_A)
_PsCommandRemoteTest_Type=Integer32
_PsCommandRemoteTest_Object=MibScalar
psCommandRemoteTest=_PsCommandRemoteTest_Object((1,3,6,1,4,1,6050,1,15,27),_PsCommandRemoteTest_Type())
psCommandRemoteTest.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandRemoteTest.setStatus(_A)
_PsCommandControlerStatus_Type=Integer32
_PsCommandControlerStatus_Object=MibScalar
psCommandControlerStatus=_PsCommandControlerStatus_Object((1,3,6,1,4,1,6050,1,15,28),_PsCommandControlerStatus_Type())
psCommandControlerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandControlerStatus.setStatus(_A)
class _PsCommandFirmwareRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PsCommandFirmwareRev_Type.__name__=_Q
_PsCommandFirmwareRev_Object=MibScalar
psCommandFirmwareRev=_PsCommandFirmwareRev_Object((1,3,6,1,4,1,6050,1,15,29),_PsCommandFirmwareRev_Type())
psCommandFirmwareRev.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFirmwareRev.setStatus(_A)
class _PsCommandFlash2SWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_PsCommandFlash2SWRev_Type.__name__=_Q
_PsCommandFlash2SWRev_Object=MibScalar
psCommandFlash2SWRev=_PsCommandFlash2SWRev_Object((1,3,6,1,4,1,6050,1,15,30),_PsCommandFlash2SWRev_Type())
psCommandFlash2SWRev.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFlash2SWRev.setStatus(_A)
class _PsCommandFlash1SWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_PsCommandFlash1SWRev_Type.__name__=_Q
_PsCommandFlash1SWRev_Object=MibScalar
psCommandFlash1SWRev=_PsCommandFlash1SWRev_Object((1,3,6,1,4,1,6050,1,15,31),_PsCommandFlash1SWRev_Type())
psCommandFlash1SWRev.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandFlash1SWRev.setStatus(_A)
class _PsCommandMBXSWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_PsCommandMBXSWRev_Type.__name__=_Q
_PsCommandMBXSWRev_Object=MibScalar
psCommandMBXSWRev=_PsCommandMBXSWRev_Object((1,3,6,1,4,1,6050,1,15,32),_PsCommandMBXSWRev_Type())
psCommandMBXSWRev.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandMBXSWRev.setStatus(_A)
_PsCommandLeds_Type=Integer32
_PsCommandLeds_Object=MibScalar
psCommandLeds=_PsCommandLeds_Object((1,3,6,1,4,1,6050,1,15,33),_PsCommandLeds_Type())
psCommandLeds.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandLeds.setStatus(_A)
_PsCommandProgramingInProcess_Type=Integer32
_PsCommandProgramingInProcess_Object=MibScalar
psCommandProgramingInProcess=_PsCommandProgramingInProcess_Object((1,3,6,1,4,1,6050,1,15,34),_PsCommandProgramingInProcess_Type())
psCommandProgramingInProcess.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandProgramingInProcess.setStatus(_A)
class _PsCommandLoadUserDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandLoadUserDefaults_Type.__name__=_C
_PsCommandLoadUserDefaults_Object=MibScalar
psCommandLoadUserDefaults=_PsCommandLoadUserDefaults_Object((1,3,6,1,4,1,6050,1,15,35),_PsCommandLoadUserDefaults_Type())
psCommandLoadUserDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandLoadUserDefaults.setStatus(_A)
class _PsCommandStoreUserDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandStoreUserDefaults_Type.__name__=_C
_PsCommandStoreUserDefaults_Object=MibScalar
psCommandStoreUserDefaults=_PsCommandStoreUserDefaults_Object((1,3,6,1,4,1,6050,1,15,36),_PsCommandStoreUserDefaults_Type())
psCommandStoreUserDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandStoreUserDefaults.setStatus(_A)
class _PsCommandLoadUserParameters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandLoadUserParameters_Type.__name__=_C
_PsCommandLoadUserParameters_Object=MibScalar
psCommandLoadUserParameters=_PsCommandLoadUserParameters_Object((1,3,6,1,4,1,6050,1,15,37),_PsCommandLoadUserParameters_Type())
psCommandLoadUserParameters.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandLoadUserParameters.setStatus(_A)
class _PsCommandStoreUserParameters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_U,1)))
_PsCommandStoreUserParameters_Type.__name__=_C
_PsCommandStoreUserParameters_Object=MibScalar
psCommandStoreUserParameters=_PsCommandStoreUserParameters_Object((1,3,6,1,4,1,6050,1,15,38),_PsCommandStoreUserParameters_Type())
psCommandStoreUserParameters.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandStoreUserParameters.setStatus(_A)
_PsCommandDryInStatus_Type=Integer32
_PsCommandDryInStatus_Object=MibScalar
psCommandDryInStatus=_PsCommandDryInStatus_Object((1,3,6,1,4,1,6050,1,15,39),_PsCommandDryInStatus_Type())
psCommandDryInStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandDryInStatus.setStatus(_A)
_PsCommandSpareR0_Type=Integer32
_PsCommandSpareR0_Object=MibScalar
psCommandSpareR0=_PsCommandSpareR0_Object((1,3,6,1,4,1,6050,1,15,40),_PsCommandSpareR0_Type())
psCommandSpareR0.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR0.setStatus(_A)
_PsCommandSpareR1_Type=Integer32
_PsCommandSpareR1_Object=MibScalar
psCommandSpareR1=_PsCommandSpareR1_Object((1,3,6,1,4,1,6050,1,15,41),_PsCommandSpareR1_Type())
psCommandSpareR1.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR1.setStatus(_A)
_PsCommandSpareR2_Type=Integer32
_PsCommandSpareR2_Object=MibScalar
psCommandSpareR2=_PsCommandSpareR2_Object((1,3,6,1,4,1,6050,1,15,42),_PsCommandSpareR2_Type())
psCommandSpareR2.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR2.setStatus(_A)
_PsCommandSpareR3_Type=Integer32
_PsCommandSpareR3_Object=MibScalar
psCommandSpareR3=_PsCommandSpareR3_Object((1,3,6,1,4,1,6050,1,15,43),_PsCommandSpareR3_Type())
psCommandSpareR3.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR3.setStatus(_A)
_PsCommandSpareR4_Type=Integer32
_PsCommandSpareR4_Object=MibScalar
psCommandSpareR4=_PsCommandSpareR4_Object((1,3,6,1,4,1,6050,1,15,44),_PsCommandSpareR4_Type())
psCommandSpareR4.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR4.setStatus(_A)
_PsCommandSpareR5_Type=Integer32
_PsCommandSpareR5_Object=MibScalar
psCommandSpareR5=_PsCommandSpareR5_Object((1,3,6,1,4,1,6050,1,15,45),_PsCommandSpareR5_Type())
psCommandSpareR5.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR5.setStatus(_A)
_PsCommandSpareR6_Type=Integer32
_PsCommandSpareR6_Object=MibScalar
psCommandSpareR6=_PsCommandSpareR6_Object((1,3,6,1,4,1,6050,1,15,46),_PsCommandSpareR6_Type())
psCommandSpareR6.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR6.setStatus(_A)
_PsCommandSpareR7_Type=Integer32
_PsCommandSpareR7_Object=MibScalar
psCommandSpareR7=_PsCommandSpareR7_Object((1,3,6,1,4,1,6050,1,15,47),_PsCommandSpareR7_Type())
psCommandSpareR7.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR7.setStatus(_A)
_PsCommandSpareR8_Type=Integer32
_PsCommandSpareR8_Object=MibScalar
psCommandSpareR8=_PsCommandSpareR8_Object((1,3,6,1,4,1,6050,1,15,48),_PsCommandSpareR8_Type())
psCommandSpareR8.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR8.setStatus(_A)
_PsCommandSpareR9_Type=Integer32
_PsCommandSpareR9_Object=MibScalar
psCommandSpareR9=_PsCommandSpareR9_Object((1,3,6,1,4,1,6050,1,15,49),_PsCommandSpareR9_Type())
psCommandSpareR9.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR9.setStatus(_A)
_PsCommandSpareR10_Type=Integer32
_PsCommandSpareR10_Object=MibScalar
psCommandSpareR10=_PsCommandSpareR10_Object((1,3,6,1,4,1,6050,1,15,50),_PsCommandSpareR10_Type())
psCommandSpareR10.setMaxAccess(_D)
if mibBuilder.loadTexts:psCommandSpareR10.setStatus(_A)
_PsCommandSpareW0_Type=Integer32
_PsCommandSpareW0_Object=MibScalar
psCommandSpareW0=_PsCommandSpareW0_Object((1,3,6,1,4,1,6050,1,15,51),_PsCommandSpareW0_Type())
psCommandSpareW0.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW0.setStatus(_A)
_PsCommandSpareW1_Type=Integer32
_PsCommandSpareW1_Object=MibScalar
psCommandSpareW1=_PsCommandSpareW1_Object((1,3,6,1,4,1,6050,1,15,52),_PsCommandSpareW1_Type())
psCommandSpareW1.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW1.setStatus(_A)
_PsCommandSpareW2_Type=Integer32
_PsCommandSpareW2_Object=MibScalar
psCommandSpareW2=_PsCommandSpareW2_Object((1,3,6,1,4,1,6050,1,15,53),_PsCommandSpareW2_Type())
psCommandSpareW2.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW2.setStatus(_A)
_PsCommandSpareW3_Type=Integer32
_PsCommandSpareW3_Object=MibScalar
psCommandSpareW3=_PsCommandSpareW3_Object((1,3,6,1,4,1,6050,1,15,54),_PsCommandSpareW3_Type())
psCommandSpareW3.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW3.setStatus(_A)
_PsCommandSpareW4_Type=Integer32
_PsCommandSpareW4_Object=MibScalar
psCommandSpareW4=_PsCommandSpareW4_Object((1,3,6,1,4,1,6050,1,15,55),_PsCommandSpareW4_Type())
psCommandSpareW4.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW4.setStatus(_A)
_PsCommandSpareW5_Type=Integer32
_PsCommandSpareW5_Object=MibScalar
psCommandSpareW5=_PsCommandSpareW5_Object((1,3,6,1,4,1,6050,1,15,56),_PsCommandSpareW5_Type())
psCommandSpareW5.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW5.setStatus(_A)
_PsCommandSpareW6_Type=Integer32
_PsCommandSpareW6_Object=MibScalar
psCommandSpareW6=_PsCommandSpareW6_Object((1,3,6,1,4,1,6050,1,15,57),_PsCommandSpareW6_Type())
psCommandSpareW6.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW6.setStatus(_A)
_PsCommandSpareW7_Type=Integer32
_PsCommandSpareW7_Object=MibScalar
psCommandSpareW7=_PsCommandSpareW7_Object((1,3,6,1,4,1,6050,1,15,58),_PsCommandSpareW7_Type())
psCommandSpareW7.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW7.setStatus(_A)
_PsCommandSpareW8_Type=Integer32
_PsCommandSpareW8_Object=MibScalar
psCommandSpareW8=_PsCommandSpareW8_Object((1,3,6,1,4,1,6050,1,15,59),_PsCommandSpareW8_Type())
psCommandSpareW8.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW8.setStatus(_A)
_PsCommandSpareW9_Type=Integer32
_PsCommandSpareW9_Object=MibScalar
psCommandSpareW9=_PsCommandSpareW9_Object((1,3,6,1,4,1,6050,1,15,60),_PsCommandSpareW9_Type())
psCommandSpareW9.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW9.setStatus(_A)
_PsCommandSpareW10_Type=Integer32
_PsCommandSpareW10_Object=MibScalar
psCommandSpareW10=_PsCommandSpareW10_Object((1,3,6,1,4,1,6050,1,15,61),_PsCommandSpareW10_Type())
psCommandSpareW10.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW10.setStatus(_A)
_PsCommandSpareW11_Type=Integer32
_PsCommandSpareW11_Object=MibScalar
psCommandSpareW11=_PsCommandSpareW11_Object((1,3,6,1,4,1,6050,1,15,62),_PsCommandSpareW11_Type())
psCommandSpareW11.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW11.setStatus(_A)
_PsCommandSpareW12_Type=Integer32
_PsCommandSpareW12_Object=MibScalar
psCommandSpareW12=_PsCommandSpareW12_Object((1,3,6,1,4,1,6050,1,15,63),_PsCommandSpareW12_Type())
psCommandSpareW12.setMaxAccess(_B)
if mibBuilder.loadTexts:psCommandSpareW12.setStatus(_A)
_PsSeverityMap_ObjectIdentity=ObjectIdentity
psSeverityMap=_PsSeverityMap_ObjectIdentity((1,3,6,1,4,1,6050,1,16))
_PsSeverityMapTable_Object=MibTable
psSeverityMapTable=_PsSeverityMapTable_Object((1,3,6,1,4,1,6050,1,16,1))
if mibBuilder.loadTexts:psSeverityMapTable.setStatus(_A)
_PsSeverityMapEntry_Object=MibTableRow
psSeverityMapEntry=_PsSeverityMapEntry_Object((1,3,6,1,4,1,6050,1,16,1,1))
psSeverityMapEntry.setIndexNames((0,_N,_w))
if mibBuilder.loadTexts:psSeverityMapEntry.setStatus(_A)
_PsSeverityMapIndex_Type=Integer32
_PsSeverityMapIndex_Object=MibTableColumn
psSeverityMapIndex=_PsSeverityMapIndex_Object((1,3,6,1,4,1,6050,1,16,1,1,1),_PsSeverityMapIndex_Type())
psSeverityMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:psSeverityMapIndex.setStatus(_A)
_PsSeverityMapAlarm1to32_Type=Integer32
_PsSeverityMapAlarm1to32_Object=MibTableColumn
psSeverityMapAlarm1to32=_PsSeverityMapAlarm1to32_Object((1,3,6,1,4,1,6050,1,16,1,1,2),_PsSeverityMapAlarm1to32_Type())
psSeverityMapAlarm1to32.setMaxAccess(_D)
if mibBuilder.loadTexts:psSeverityMapAlarm1to32.setStatus(_A)
_PsSeverityMapAlarm33to64_Type=Integer32
_PsSeverityMapAlarm33to64_Object=MibTableColumn
psSeverityMapAlarm33to64=_PsSeverityMapAlarm33to64_Object((1,3,6,1,4,1,6050,1,16,1,1,3),_PsSeverityMapAlarm33to64_Type())
psSeverityMapAlarm33to64.setMaxAccess(_D)
if mibBuilder.loadTexts:psSeverityMapAlarm33to64.setStatus(_A)
_PsSeverityMapAlarm65to96_Type=Integer32
_PsSeverityMapAlarm65to96_Object=MibTableColumn
psSeverityMapAlarm65to96=_PsSeverityMapAlarm65to96_Object((1,3,6,1,4,1,6050,1,16,1,1,4),_PsSeverityMapAlarm65to96_Type())
psSeverityMapAlarm65to96.setMaxAccess(_D)
if mibBuilder.loadTexts:psSeverityMapAlarm65to96.setStatus(_A)
_PsSpare_ObjectIdentity=ObjectIdentity
psSpare=_PsSpare_ObjectIdentity((1,3,6,1,4,1,6050,1,17))
_PsSpare1_Type=Integer32
_PsSpare1_Object=MibScalar
psSpare1=_PsSpare1_Object((1,3,6,1,4,1,6050,1,17,1),_PsSpare1_Type())
psSpare1.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare1.setStatus(_A)
_PsSpare2_Type=Integer32
_PsSpare2_Object=MibScalar
psSpare2=_PsSpare2_Object((1,3,6,1,4,1,6050,1,17,2),_PsSpare2_Type())
psSpare2.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare2.setStatus(_A)
_PsSpare3_Type=Integer32
_PsSpare3_Object=MibScalar
psSpare3=_PsSpare3_Object((1,3,6,1,4,1,6050,1,17,3),_PsSpare3_Type())
psSpare3.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare3.setStatus(_A)
_PsSpare4_Type=Integer32
_PsSpare4_Object=MibScalar
psSpare4=_PsSpare4_Object((1,3,6,1,4,1,6050,1,17,4),_PsSpare4_Type())
psSpare4.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare4.setStatus(_A)
_PsSpare5_Type=Integer32
_PsSpare5_Object=MibScalar
psSpare5=_PsSpare5_Object((1,3,6,1,4,1,6050,1,17,5),_PsSpare5_Type())
psSpare5.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare5.setStatus(_A)
_PsSpare6_Type=Integer32
_PsSpare6_Object=MibScalar
psSpare6=_PsSpare6_Object((1,3,6,1,4,1,6050,1,17,6),_PsSpare6_Type())
psSpare6.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare6.setStatus(_A)
_PsSpare7_Type=Integer32
_PsSpare7_Object=MibScalar
psSpare7=_PsSpare7_Object((1,3,6,1,4,1,6050,1,17,7),_PsSpare7_Type())
psSpare7.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare7.setStatus(_A)
_PsSpare8_Type=Integer32
_PsSpare8_Object=MibScalar
psSpare8=_PsSpare8_Object((1,3,6,1,4,1,6050,1,17,8),_PsSpare8_Type())
psSpare8.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare8.setStatus(_A)
_PsSpare9_Type=Integer32
_PsSpare9_Object=MibScalar
psSpare9=_PsSpare9_Object((1,3,6,1,4,1,6050,1,17,9),_PsSpare9_Type())
psSpare9.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare9.setStatus(_A)
_PsSpare10_Type=Integer32
_PsSpare10_Object=MibScalar
psSpare10=_PsSpare10_Object((1,3,6,1,4,1,6050,1,17,10),_PsSpare10_Type())
psSpare10.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare10.setStatus(_A)
_PsSpare11_Type=Integer32
_PsSpare11_Object=MibScalar
psSpare11=_PsSpare11_Object((1,3,6,1,4,1,6050,1,17,11),_PsSpare11_Type())
psSpare11.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare11.setStatus(_A)
_PsSpare12_Type=Integer32
_PsSpare12_Object=MibScalar
psSpare12=_PsSpare12_Object((1,3,6,1,4,1,6050,1,17,12),_PsSpare12_Type())
psSpare12.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare12.setStatus(_A)
_PsSpare13_Type=Integer32
_PsSpare13_Object=MibScalar
psSpare13=_PsSpare13_Object((1,3,6,1,4,1,6050,1,17,13),_PsSpare13_Type())
psSpare13.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare13.setStatus(_A)
_PsSpare14_Type=Integer32
_PsSpare14_Object=MibScalar
psSpare14=_PsSpare14_Object((1,3,6,1,4,1,6050,1,17,14),_PsSpare14_Type())
psSpare14.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare14.setStatus(_A)
_PsSpare15_Type=Integer32
_PsSpare15_Object=MibScalar
psSpare15=_PsSpare15_Object((1,3,6,1,4,1,6050,1,17,15),_PsSpare15_Type())
psSpare15.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare15.setStatus(_A)
_PsSpare16_Type=Integer32
_PsSpare16_Object=MibScalar
psSpare16=_PsSpare16_Object((1,3,6,1,4,1,6050,1,17,16),_PsSpare16_Type())
psSpare16.setMaxAccess(_B)
if mibBuilder.loadTexts:psSpare16.setStatus(_A)
_PsSpare17_Type=Integer32
_PsSpare17_Object=MibScalar
psSpare17=_PsSpare17_Object((1,3,6,1,4,1,6050,1,17,17),_PsSpare17_Type())
psSpare17.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare17.setStatus(_A)
_PsSpare18_Type=Integer32
_PsSpare18_Object=MibScalar
psSpare18=_PsSpare18_Object((1,3,6,1,4,1,6050,1,17,18),_PsSpare18_Type())
psSpare18.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare18.setStatus(_A)
_PsSpare19_Type=Integer32
_PsSpare19_Object=MibScalar
psSpare19=_PsSpare19_Object((1,3,6,1,4,1,6050,1,17,19),_PsSpare19_Type())
psSpare19.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare19.setStatus(_A)
_PsSpare20_Type=Integer32
_PsSpare20_Object=MibScalar
psSpare20=_PsSpare20_Object((1,3,6,1,4,1,6050,1,17,20),_PsSpare20_Type())
psSpare20.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare20.setStatus(_A)
_PsSpare21_Type=Integer32
_PsSpare21_Object=MibScalar
psSpare21=_PsSpare21_Object((1,3,6,1,4,1,6050,1,17,21),_PsSpare21_Type())
psSpare21.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare21.setStatus(_A)
_PsSpare22_Type=Integer32
_PsSpare22_Object=MibScalar
psSpare22=_PsSpare22_Object((1,3,6,1,4,1,6050,1,17,22),_PsSpare22_Type())
psSpare22.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare22.setStatus(_A)
_PsSpare23_Type=Integer32
_PsSpare23_Object=MibScalar
psSpare23=_PsSpare23_Object((1,3,6,1,4,1,6050,1,17,23),_PsSpare23_Type())
psSpare23.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare23.setStatus(_A)
_PsSpare24_Type=Integer32
_PsSpare24_Object=MibScalar
psSpare24=_PsSpare24_Object((1,3,6,1,4,1,6050,1,17,24),_PsSpare24_Type())
psSpare24.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare24.setStatus(_A)
_PsSpare25_Type=Integer32
_PsSpare25_Object=MibScalar
psSpare25=_PsSpare25_Object((1,3,6,1,4,1,6050,1,17,25),_PsSpare25_Type())
psSpare25.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare25.setStatus(_A)
_PsSpare26_Type=Integer32
_PsSpare26_Object=MibScalar
psSpare26=_PsSpare26_Object((1,3,6,1,4,1,6050,1,17,26),_PsSpare26_Type())
psSpare26.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare26.setStatus(_A)
_PsSpare27_Type=Integer32
_PsSpare27_Object=MibScalar
psSpare27=_PsSpare27_Object((1,3,6,1,4,1,6050,1,17,27),_PsSpare27_Type())
psSpare27.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare27.setStatus(_A)
_PsSpare28_Type=Integer32
_PsSpare28_Object=MibScalar
psSpare28=_PsSpare28_Object((1,3,6,1,4,1,6050,1,17,28),_PsSpare28_Type())
psSpare28.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare28.setStatus(_A)
_PsSpare29_Type=Integer32
_PsSpare29_Object=MibScalar
psSpare29=_PsSpare29_Object((1,3,6,1,4,1,6050,1,17,29),_PsSpare29_Type())
psSpare29.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare29.setStatus(_A)
_PsSpare30_Type=Integer32
_PsSpare30_Object=MibScalar
psSpare30=_PsSpare30_Object((1,3,6,1,4,1,6050,1,17,30),_PsSpare30_Type())
psSpare30.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare30.setStatus(_A)
_PsSpare31_Type=Integer32
_PsSpare31_Object=MibScalar
psSpare31=_PsSpare31_Object((1,3,6,1,4,1,6050,1,17,31),_PsSpare31_Type())
psSpare31.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare31.setStatus(_A)
_PsSpare32_Type=Integer32
_PsSpare32_Object=MibScalar
psSpare32=_PsSpare32_Object((1,3,6,1,4,1,6050,1,17,32),_PsSpare32_Type())
psSpare32.setMaxAccess(_D)
if mibBuilder.loadTexts:psSpare32.setStatus(_A)
_PsDial_ObjectIdentity=ObjectIdentity
psDial=_PsDial_ObjectIdentity((1,3,6,1,4,1,6050,1,18))
class _PsDialATDModemSetUp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_PsDialATDModemSetUp_Type.__name__=_Q
_PsDialATDModemSetUp_Object=MibScalar
psDialATDModemSetUp=_PsDialATDModemSetUp_Object((1,3,6,1,4,1,6050,1,18,1),_PsDialATDModemSetUp_Type())
psDialATDModemSetUp.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialATDModemSetUp.setStatus(_A)
class _PsDialATDDialOut_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_PsDialATDDialOut_Type.__name__=_Q
_PsDialATDDialOut_Object=MibScalar
psDialATDDialOut=_PsDialATDDialOut_Object((1,3,6,1,4,1,6050,1,18,2),_PsDialATDDialOut_Type())
psDialATDDialOut.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialATDDialOut.setStatus(_A)
class _PsDialOutFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nodialout',0),('dialout',1)))
_PsDialOutFlag_Type.__name__=_C
_PsDialOutFlag_Object=MibScalar
psDialOutFlag=_PsDialOutFlag_Object((1,3,6,1,4,1,6050,1,18,3),_PsDialOutFlag_Type())
psDialOutFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialOutFlag.setStatus(_A)
_PsDialOutNumRetries_Type=Integer32
_PsDialOutNumRetries_Object=MibScalar
psDialOutNumRetries=_PsDialOutNumRetries_Object((1,3,6,1,4,1,6050,1,18,4),_PsDialOutNumRetries_Type())
psDialOutNumRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialOutNumRetries.setStatus(_A)
_PsDialOutNumRetriesActual_Type=Integer32
_PsDialOutNumRetriesActual_Object=MibScalar
psDialOutNumRetriesActual=_PsDialOutNumRetriesActual_Object((1,3,6,1,4,1,6050,1,18,5),_PsDialOutNumRetriesActual_Type())
psDialOutNumRetriesActual.setMaxAccess(_D)
if mibBuilder.loadTexts:psDialOutNumRetriesActual.setStatus(_A)
_PsDialTimeOutBetweenRetries_Type=Integer32
_PsDialTimeOutBetweenRetries_Object=MibScalar
psDialTimeOutBetweenRetries=_PsDialTimeOutBetweenRetries_Object((1,3,6,1,4,1,6050,1,18,6),_PsDialTimeOutBetweenRetries_Type())
psDialTimeOutBetweenRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialTimeOutBetweenRetries.setStatus(_A)
if mibBuilder.loadTexts:psDialTimeOutBetweenRetries.setUnits(_x)
_PsDialTimeOutAfterLastSuccess_Type=Integer32
_PsDialTimeOutAfterLastSuccess_Object=MibScalar
psDialTimeOutAfterLastSuccess=_PsDialTimeOutAfterLastSuccess_Object((1,3,6,1,4,1,6050,1,18,7),_PsDialTimeOutAfterLastSuccess_Type())
psDialTimeOutAfterLastSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialTimeOutAfterLastSuccess.setStatus(_A)
if mibBuilder.loadTexts:psDialTimeOutAfterLastSuccess.setUnits(_x)
_PsDialTimeOutAfterLastRetryFailed_Type=Integer32
_PsDialTimeOutAfterLastRetryFailed_Object=MibScalar
psDialTimeOutAfterLastRetryFailed=_PsDialTimeOutAfterLastRetryFailed_Object((1,3,6,1,4,1,6050,1,18,8),_PsDialTimeOutAfterLastRetryFailed_Type())
psDialTimeOutAfterLastRetryFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:psDialTimeOutAfterLastRetryFailed.setStatus(_A)
if mibBuilder.loadTexts:psDialTimeOutAfterLastRetryFailed.setUnits('Minutes')
_PsPowerPlus_ObjectIdentity=ObjectIdentity
psPowerPlus=_PsPowerPlus_ObjectIdentity((1,3,6,1,4,1,6050,1,19))
class _PsPowerPlus1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus1_Type.__name__=_Q
_PsPowerPlus1_Object=MibScalar
psPowerPlus1=_PsPowerPlus1_Object((1,3,6,1,4,1,6050,1,19,1),_PsPowerPlus1_Type())
psPowerPlus1.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus1.setStatus(_A)
class _PsPowerPlus2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus2_Type.__name__=_Q
_PsPowerPlus2_Object=MibScalar
psPowerPlus2=_PsPowerPlus2_Object((1,3,6,1,4,1,6050,1,19,2),_PsPowerPlus2_Type())
psPowerPlus2.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus2.setStatus(_A)
class _PsPowerPlus3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus3_Type.__name__=_Q
_PsPowerPlus3_Object=MibScalar
psPowerPlus3=_PsPowerPlus3_Object((1,3,6,1,4,1,6050,1,19,3),_PsPowerPlus3_Type())
psPowerPlus3.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus3.setStatus(_A)
class _PsPowerPlus4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus4_Type.__name__=_Q
_PsPowerPlus4_Object=MibScalar
psPowerPlus4=_PsPowerPlus4_Object((1,3,6,1,4,1,6050,1,19,4),_PsPowerPlus4_Type())
psPowerPlus4.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus4.setStatus(_A)
class _PsPowerPlus5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus5_Type.__name__=_Q
_PsPowerPlus5_Object=MibScalar
psPowerPlus5=_PsPowerPlus5_Object((1,3,6,1,4,1,6050,1,19,5),_PsPowerPlus5_Type())
psPowerPlus5.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus5.setStatus(_A)
class _PsPowerPlus6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus6_Type.__name__=_Q
_PsPowerPlus6_Object=MibScalar
psPowerPlus6=_PsPowerPlus6_Object((1,3,6,1,4,1,6050,1,19,6),_PsPowerPlus6_Type())
psPowerPlus6.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus6.setStatus(_A)
class _PsPowerPlus7_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus7_Type.__name__=_Q
_PsPowerPlus7_Object=MibScalar
psPowerPlus7=_PsPowerPlus7_Object((1,3,6,1,4,1,6050,1,19,7),_PsPowerPlus7_Type())
psPowerPlus7.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus7.setStatus(_A)
class _PsPowerPlus8_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus8_Type.__name__=_Q
_PsPowerPlus8_Object=MibScalar
psPowerPlus8=_PsPowerPlus8_Object((1,3,6,1,4,1,6050,1,19,8),_PsPowerPlus8_Type())
psPowerPlus8.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus8.setStatus(_A)
class _PsPowerPlus9_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus9_Type.__name__=_Q
_PsPowerPlus9_Object=MibScalar
psPowerPlus9=_PsPowerPlus9_Object((1,3,6,1,4,1,6050,1,19,9),_PsPowerPlus9_Type())
psPowerPlus9.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus9.setStatus(_A)
class _PsPowerPlus10_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus10_Type.__name__=_Q
_PsPowerPlus10_Object=MibScalar
psPowerPlus10=_PsPowerPlus10_Object((1,3,6,1,4,1,6050,1,19,10),_PsPowerPlus10_Type())
psPowerPlus10.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus10.setStatus(_A)
class _PsPowerPlus11_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus11_Type.__name__=_Q
_PsPowerPlus11_Object=MibScalar
psPowerPlus11=_PsPowerPlus11_Object((1,3,6,1,4,1,6050,1,19,11),_PsPowerPlus11_Type())
psPowerPlus11.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus11.setStatus(_A)
class _PsPowerPlus12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus12_Type.__name__=_Q
_PsPowerPlus12_Object=MibScalar
psPowerPlus12=_PsPowerPlus12_Object((1,3,6,1,4,1,6050,1,19,12),_PsPowerPlus12_Type())
psPowerPlus12.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus12.setStatus(_A)
class _PsPowerPlus13_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus13_Type.__name__=_Q
_PsPowerPlus13_Object=MibScalar
psPowerPlus13=_PsPowerPlus13_Object((1,3,6,1,4,1,6050,1,19,13),_PsPowerPlus13_Type())
psPowerPlus13.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus13.setStatus(_A)
class _PsPowerPlus14_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus14_Type.__name__=_Q
_PsPowerPlus14_Object=MibScalar
psPowerPlus14=_PsPowerPlus14_Object((1,3,6,1,4,1,6050,1,19,14),_PsPowerPlus14_Type())
psPowerPlus14.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus14.setStatus(_A)
class _PsPowerPlus15_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_PsPowerPlus15_Type.__name__=_Q
_PsPowerPlus15_Object=MibScalar
psPowerPlus15=_PsPowerPlus15_Object((1,3,6,1,4,1,6050,1,19,15),_PsPowerPlus15_Type())
psPowerPlus15.setMaxAccess(_D)
if mibBuilder.loadTexts:psPowerPlus15.setStatus(_A)
psTrap1006ACLow=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,1))
psTrap1006ACLow.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006ACLow.setStatus(_A)
psTrap1006Battery2TestFault=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,2))
psTrap1006Battery2TestFault.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006Battery2TestFault.setStatus(_A)
psTrap1006Battery1TestFault=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,3))
psTrap1006Battery1TestFault.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006Battery1TestFault.setStatus(_A)
psTrap1006LVD2Open=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,4))
psTrap1006LVD2Open.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006LVD2Open.setStatus(_A)
psTrap1006LVD1Open=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,5))
psTrap1006LVD1Open.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006LVD1Open.setStatus(_A)
psTrap1006AUXContactOpen=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,6))
psTrap1006AUXContactOpen.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006AUXContactOpen.setStatus(_A)
psTrap1006AUXBreakerOpen=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,7))
psTrap1006AUXBreakerOpen.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006AUXBreakerOpen.setStatus(_A)
psTrap1006BatteryBreakerOpen=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,8))
psTrap1006BatteryBreakerOpen.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006BatteryBreakerOpen.setStatus(_A)
psTrap1006LoadBreakerOpen=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,9))
psTrap1006LoadBreakerOpen.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006LoadBreakerOpen.setStatus(_A)
psTrap1006DCLOWLow=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,10))
psTrap1006DCLOWLow.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006DCLOWLow.setStatus(_A)
psTrap1006Rectifier=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,11))
psTrap1006Rectifier.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006Rectifier.setStatus(_A)
psTrap1006OverTemptature=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,12))
psTrap1006OverTemptature.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006OverTemptature.setStatus(_A)
psTrap1006LVDBypassOpen=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,13))
psTrap1006LVDBypassOpen.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006LVDBypassOpen.setStatus(_A)
psTrap1006DCHigh=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,14))
psTrap1006DCHigh.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006DCHigh.setStatus(_A)
psTrap1006DCLow=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,15))
psTrap1006DCLow.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006DCLow.setStatus(_A)
psTrap1006ACHigh=NotificationType((1,3,6,1,4,1,6050,1,12,10,0,16))
psTrap1006ACHigh.setObjects((_N,_O))
if mibBuilder.loadTexts:psTrap1006ACHigh.setStatus(_A)
psTrapRFAMAJ=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,1))
psTrapRFAMAJ.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapRFAMAJ.setStatus(_A)
psTrapRFAMIN=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,2))
psTrapRFAMIN.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapRFAMIN.setStatus(_A)
psTrapACFAIL=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,3))
psTrapACFAIL.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapACFAIL.setStatus(_A)
psTrapLVDX2=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,4))
psTrapLVDX2.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapLVDX2.setStatus(_A)
psTrapSYSOT=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,5))
psTrapSYSOT.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapSYSOT.setStatus(_A)
psTrapLVDX1=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,6))
psTrapLVDX1.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapLVDX1.setStatus(_A)
psTrapCBOPEN=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,7))
psTrapCBOPEN.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapCBOPEN.setStatus(_A)
psTrapEQHST=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,8))
psTrapEQHST.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapEQHST.setStatus(_A)
psTrapBATTST=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,9))
psTrapBATTST.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapBATTST.setStatus(_A)
psTrapINUBAD=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,10))
psTrapINUBAD.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapINUBAD.setStatus(_A)
psTrapUNIVPD=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,11))
psTrapUNIVPD.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapUNIVPD.setStatus(_A)
psTrapIBADIN=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,12))
psTrapIBADIN.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapIBADIN.setStatus(_A)
psTrapRBADIN=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,13))
psTrapRBADIN.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapRBADIN.setStatus(_A)
psTrapSLFTST=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,14))
psTrapSLFTST.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapSLFTST.setStatus(_A)
psTrapFUSEBD=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,15))
psTrapFUSEBD.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapFUSEBD.setStatus(_A)
psTrapLOADHI=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,16))
psTrapLOADHI.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapLOADHI.setStatus(_A)
psTrapSURGBD=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,17))
psTrapSURGBD.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapSURGBD.setStatus(_A)
psTrapEQLONG=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,18))
psTrapEQLONG.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapEQLONG.setStatus(_A)
psTrapFUSE24=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,19))
psTrapFUSE24.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapFUSE24.setStatus(_A)
psTrapFUSE48=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,20))
psTrapFUSE48.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapFUSE48.setStatus(_A)
psTrapBYPS2=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,21))
psTrapBYPS2.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapBYPS2.setStatus(_A)
psTrapBYPS1=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,22))
psTrapBYPS1.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapBYPS1.setStatus(_A)
psTrapCB24CR=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,23))
psTrapCB24CR.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapCB24CR.setStatus(_A)
psTrapCB48CR=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,24))
psTrapCB48CR.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapCB48CR.setStatus(_A)
psTrapBATOT=NotificationType((1,3,6,1,4,1,6050,1,12,11,0,25))
psTrapBATOT.setObjects(*((_N,_R),(_N,_O)))
if mibBuilder.loadTexts:psTrapBATOT.setStatus(_A)
mibBuilder.exportSymbols(_N,**{'PsAlarmSeverity':PsAlarmSeverity,'gamatronicLTD':gamatronicLTD,'psMIB':psMIB,'psUnit':psUnit,'psUnitSysName':psUnitSysName,'psUnitManufacture':psUnitManufacture,'psUnitBatteryType':psUnitBatteryType,'psUnitPSType':psUnitPSType,'psUnitControllerType':psUnitControllerType,'psUnitSoftwareVersion':psUnitSoftwareVersion,'psUnitComProtocolVersion':psUnitComProtocolVersion,'psUnitSerialNumber':psUnitSerialNumber,'psUnitRTCDay':psUnitRTCDay,'psUnitRTCMonth':psUnitRTCMonth,'psUnitRTCYear':psUnitRTCYear,'psUnitRTCHour':psUnitRTCHour,'psUnitRTCMinute':psUnitRTCMinute,'psUnitRTCSecond':psUnitRTCSecond,'psWorkingTime':psWorkingTime,'psScreenShot':psScreenShot,'psSpareIde0':psSpareIde0,'psSpareIde1':psSpareIde1,'psSpareIde2':psSpareIde2,'psSpareIde3':psSpareIde3,'psSpareIde4':psSpareIde4,'psSpareIde5':psSpareIde5,'psSpareIde6':psSpareIde6,'psSpareIde7':psSpareIde7,'psBattery':psBattery,'psBatteryNumber':psBatteryNumber,'psBatteryVoltage':psBatteryVoltage,'psBatteryTestStatus':psBatteryTestStatus,'psBatteryNominalCapacity':psBatteryNominalCapacity,'psBatteryActualCapacity':psBatteryActualCapacity,'psBatteryTestTime':psBatteryTestTime,'psBatteryLoadTime':psBatteryLoadTime,'psBatteryNearestTestMonth':psBatteryNearestTestMonth,'psBatteryNearestTestDay':psBatteryNearestTestDay,'psBatteryNearestTestHour':psBatteryNearestTestHour,'psBatteryNearestTestMinute':psBatteryNearestTestMinute,'psBatteryChargeMode':psBatteryChargeMode,'psBatteryEqRunTimeHours':psBatteryEqRunTimeHours,'psBatteryEqRunTimeMinutes':psBatteryEqRunTimeMinutes,'psBatterySpareRead1':psBatterySpareRead1,'psBatterySpareRead2':psBatterySpareRead2,'psBatterySpareRead3':psBatterySpareRead3,'psBatterySpareWrite1':psBatterySpareWrite1,'psBatterySpareWrite2':psBatterySpareWrite2,'psBatterySpareWrite3':psBatterySpareWrite3,'psBatterySpareWrite4':psBatterySpareWrite4,'psBatterySpareWrite5':psBatterySpareWrite5,'psBatterySpareWrite6':psBatterySpareWrite6,'psBatterySpareWrite7':psBatterySpareWrite7,'psBatterySpareWrite8':psBatterySpareWrite8,'psBatteryTable':psBatteryTable,'psBatteryEntry':psBatteryEntry,_c:psBatteryIndex,'psBatteryCurrentDirection':psBatteryCurrentDirection,'psBatteryCurrent':psBatteryCurrent,'psBatteryTemperatureSign':psBatteryTemperatureSign,'psBatteryTemperature':psBatteryTemperature,'psBatteryStatus':psBatteryStatus,'psBatteryFuseStatus':psBatteryFuseStatus,'psBatteryInstalationYear':psBatteryInstalationYear,'psBatteryInstalationMonth':psBatteryInstalationMonth,'psBatteryInstalationDay':psBatteryInstalationDay,'psPSU':psPSU,'psPSUNumber':psPSUNumber,'psPSUTable':psPSUTable,'psPSUEntry':psPSUEntry,_f:psPSUIndex,'psPSUVoltage':psPSUVoltage,'psPSUCurrent':psPSUCurrent,'psPSUTemperature':psPSUTemperature,'psPSUActivity':psPSUActivity,'psPSUPsType':psPSUPsType,'psPSUStatus':psPSUStatus,'psPSUPsOK':psPSUPsOK,'psPSUNotRespond':psPSUNotRespond,'psPSUNOOut':psPSUNOOut,'psPSUPSpareBit':psPSUPSpareBit,'psPSUBadSharing':psPSUBadSharing,'psPSUReserve1':psPSUReserve1,'psPSUReserve2':psPSUReserve2,'psPSUReserve3':psPSUReserve3,'psPSUShutInstruction':psPSUShutInstruction,'psPSUTestStatus':psPSUTestStatus,'psPSUCurrentLimitDecreased':psPSUCurrentLimitDecreased,'psPSUACInputOK':psPSUACInputOK,'psPSUSelfTestPass':psPSUSelfTestPass,'psPSUCurrentLimitExceed':psPSUCurrentLimitExceed,'psPSUShutHighTemp':psPSUShutHighTemp,'psPSUShutHighVolt':psPSUShutHighVolt,'psPSURemoteMode':psPSURemoteMode,'psPSUFloatingMode':psPSUFloatingMode,'psPSUEqualizeMode':psPSUEqualizeMode,'psPSUFanStataus':psPSUFanStataus,'psPSUIndication':psPSUIndication,'psINU':psINU,'psINUNumber':psINUNumber,'psINUTable':psINUTable,'psINUEntry':psINUEntry,_k:psINUIndex,'psINUVoltage':psINUVoltage,'psINUCurrent':psINUCurrent,'psINUTemperature':psINUTemperature,'psINUActivity':psINUActivity,'psINUPsType':psINUPsType,'psINUStatus':psINUStatus,'psINUPsOK':psINUPsOK,'psINUNotRespond':psINUNotRespond,'psINUNOOut':psINUNOOut,'psINUPSpareBit':psINUPSpareBit,'psINUBadSharing':psINUBadSharing,'psINUReserve1':psINUReserve1,'psINUReserve2':psINUReserve2,'psINUReserve3':psINUReserve3,'psINUShutInstruction':psINUShutInstruction,'psINUReserve7':psINUReserve7,'psINUCurrentLimitDecreased':psINUCurrentLimitDecreased,'psINUReserve8':psINUReserve8,'psINUSelfTestPass':psINUSelfTestPass,'psINUCurrentLimitExceed':psINUCurrentLimitExceed,'psINUShutHighTemp':psINUShutHighTemp,'psINUShutHighVolt':psINUShutHighVolt,'psINURemoteMode':psINURemoteMode,'psINUReserve9':psINUReserve9,'psINUReserve10':psINUReserve10,'psINUFanStataus':psINUFanStataus,'psINUIndication':psINUIndication,'psACInput':psACInput,'psACInputVoltage1':psACInputVoltage1,'psACInputVoltage2':psACInputVoltage2,'psACInputVoltage3':psACInputVoltage3,'psACInputCurrent1':psACInputCurrent1,'psACInputCurrent2':psACInputCurrent2,'psACInputCurrent3':psACInputCurrent3,'psACInputFrequency':psACInputFrequency,'psACInputACStatus':psACInputACStatus,'psACInputSurgeStatus':psACInputSurgeStatus,'psACInputSpareInp0':psACInputSpareInp0,'psACInputSpareInp1':psACInputSpareInp1,'psACInputSpareInp2':psACInputSpareInp2,'psACInputSpareInp3':psACInputSpareInp3,'psACInputSpareInp4':psACInputSpareInp4,'psACInputSpareInp5':psACInputSpareInp5,'psACInputSpareInp6':psACInputSpareInp6,'psDCOutput':psDCOutput,'psDCoutputVoltage':psDCoutputVoltage,'psDCoutputCurrent1':psDCoutputCurrent1,'psDCoutputCurrent2':psDCoutputCurrent2,'psDCoutputCurrent3':psDCoutputCurrent3,'psDCoutputCurrent4':psDCoutputCurrent4,'psDCoutputCurrent5':psDCoutputCurrent5,'psDCoutputDCStatus':psDCoutputDCStatus,'psDCoutputSurgeStatus':psDCoutputSurgeStatus,'psDCoutputInvertorVoltage':psDCoutputInvertorVoltage,'psDCOutputDCOutput':psDCOutputDCOutput,'psDCoutputSpare1':psDCoutputSpare1,'psDCoutputSpare2':psDCoutputSpare2,'psDCoutputSpare3':psDCoutputSpare3,'psDCoutputSpare4':psDCoutputSpare4,'psDCoutputSpare5':psDCoutputSpare5,'psDCoutputSpare6':psDCoutputSpare6,'psContuctor':psContuctor,'psContuctor1':psContuctor1,'psContuctor2':psContuctor2,'psContuctor3':psContuctor3,'psContuctor4':psContuctor4,'psContuctor5':psContuctor5,'psContuctor6':psContuctor6,'psContuctor7':psContuctor7,'psContuctor8':psContuctor8,'psContuctor9':psContuctor9,'psContuctor10':psContuctor10,'psDryContactTable':psDryContactTable,'psDryContactorEntry':psDryContactorEntry,_n:psDryContactorIndex,'psDryContactorAlarm1':psDryContactorAlarm1,'psDryContactorAlarm2':psDryContactorAlarm2,'psDryContactorAlarm3':psDryContactorAlarm3,'psDryContactorAlarm4':psDryContactorAlarm4,'psDryContactorAlarm5':psDryContactorAlarm5,'psDryContactorAlarm6':psDryContactorAlarm6,'psDryContactorAlarm7':psDryContactorAlarm7,'psDryContactorAlarm8':psDryContactorAlarm8,'psDryContactorAlarm9':psDryContactorAlarm9,'psDryContactorAlarm10':psDryContactorAlarm10,'psDryContactorAlarm11':psDryContactorAlarm11,'psDryContactorAlarm12':psDryContactorAlarm12,'psDryContactorAlarm13':psDryContactorAlarm13,'psDryContactorAlarm14':psDryContactorAlarm14,'psDryContactorAlarm15':psDryContactorAlarm15,'psDryContactorAlarm16':psDryContactorAlarm16,'psDryContactorAlarm17':psDryContactorAlarm17,'psDryContactorAlarm18':psDryContactorAlarm18,'psDryContactorAlarm19':psDryContactorAlarm19,'psDryContactorAlarm20':psDryContactorAlarm20,'psDryContactorAlarm21':psDryContactorAlarm21,'psDryContactorAlarm22':psDryContactorAlarm22,'psDryContactorAlarm23':psDryContactorAlarm23,'psDryContactorAlarm24':psDryContactorAlarm24,'psDryContactorAlarm25':psDryContactorAlarm25,'psDryContactorAlarm26':psDryContactorAlarm26,'psDryContactorAlarm27':psDryContactorAlarm27,'psDryContactorAlarm28':psDryContactorAlarm28,'psDryContactorAlarm29':psDryContactorAlarm29,'psDryContactorAlarm30':psDryContactorAlarm30,'psDryContactorAlarm31':psDryContactorAlarm31,'psDryContactorAlarm32':psDryContactorAlarm32,'psDryContactStatus':psDryContactStatus,'psDryContact1Table':psDryContact1Table,'psDryContactor1Entry':psDryContactor1Entry,_o:psDryContactor1Index,'psDryContactor1Alarm1':psDryContactor1Alarm1,'psDryContactor1Alarm2':psDryContactor1Alarm2,'psDryContactor1Alarm3':psDryContactor1Alarm3,'psDryContactor1Alarm4':psDryContactor1Alarm4,'psDryContactor1Alarm5':psDryContactor1Alarm5,'psDryContactor1Alarm6':psDryContactor1Alarm6,'psDryContactor1Alarm7':psDryContactor1Alarm7,'psDryContactor1Alarm8':psDryContactor1Alarm8,'psDryContactor1Alarm9':psDryContactor1Alarm9,'psDryContactor1Alarm10':psDryContactor1Alarm10,'psDryContactor1Alarm11':psDryContactor1Alarm11,'psDryContactor1Alarm12':psDryContactor1Alarm12,'psDryContactor1Alarm13':psDryContactor1Alarm13,'psDryContactor1Alarm14':psDryContactor1Alarm14,'psDryContactor1Alarm15':psDryContactor1Alarm15,'psDryContactor1Alarm16':psDryContactor1Alarm16,'psDryContactor1Alarm17':psDryContactor1Alarm17,'psDryContactor1Alarm18':psDryContactor1Alarm18,'psDryContactor1Alarm19':psDryContactor1Alarm19,'psDryContactor1Alarm20':psDryContactor1Alarm20,'psDryContactor1Alarm21':psDryContactor1Alarm21,'psDryContactor1Alarm22':psDryContactor1Alarm22,'psDryContactor1Alarm23':psDryContactor1Alarm23,'psDryContactor1Alarm24':psDryContactor1Alarm24,'psDryContactor1Alarm25':psDryContactor1Alarm25,'psDryContactor1Alarm26':psDryContactor1Alarm26,'psDryContactor1Alarm27':psDryContactor1Alarm27,'psDryContactor1Alarm28':psDryContactor1Alarm28,'psDryContactor1Alarm29':psDryContactor1Alarm29,'psDryContactor1Alarm30':psDryContactor1Alarm30,'psDryContactor1Alarm31':psDryContactor1Alarm31,'psDryContactor1Alarm32':psDryContactor1Alarm32,'psDryContact1Status':psDryContact1Status,'psDryContact2Table':psDryContact2Table,'psDryContactor2Entry':psDryContactor2Entry,_p:psDryContactor2Index,'psDryContactor2Alarm1':psDryContactor2Alarm1,'psDryContactor2Alarm2':psDryContactor2Alarm2,'psDryContactor2Alarm3':psDryContactor2Alarm3,'psDryContactor2Alarm4':psDryContactor2Alarm4,'psDryContactor2Alarm5':psDryContactor2Alarm5,'psDryContactor2Alarm6':psDryContactor2Alarm6,'psDryContactor2Alarm7':psDryContactor2Alarm7,'psDryContactor2Alarm8':psDryContactor2Alarm8,'psDryContactor2Alarm9':psDryContactor2Alarm9,'psDryContactor2Alarm10':psDryContactor2Alarm10,'psDryContactor2Alarm11':psDryContactor2Alarm11,'psDryContactor2Alarm12':psDryContactor2Alarm12,'psDryContactor2Alarm13':psDryContactor2Alarm13,'psDryContactor2Alarm14':psDryContactor2Alarm14,'psDryContactor2Alarm15':psDryContactor2Alarm15,'psDryContactor2Alarm16':psDryContactor2Alarm16,'psDryContactor2Alarm17':psDryContactor2Alarm17,'psDryContactor2Alarm18':psDryContactor2Alarm18,'psDryContactor2Alarm19':psDryContactor2Alarm19,'psDryContactor2Alarm20':psDryContactor2Alarm20,'psDryContactor2Alarm21':psDryContactor2Alarm21,'psDryContactor2Alarm22':psDryContactor2Alarm22,'psDryContactor2Alarm23':psDryContactor2Alarm23,'psDryContactor2Alarm24':psDryContactor2Alarm24,'psDryContactor2Alarm25':psDryContactor2Alarm25,'psDryContactor2Alarm26':psDryContactor2Alarm26,'psDryContactor2Alarm27':psDryContactor2Alarm27,'psDryContactor2Alarm28':psDryContactor2Alarm28,'psDryContactor2Alarm29':psDryContactor2Alarm29,'psDryContactor2Alarm30':psDryContactor2Alarm30,'psDryContactor2Alarm31':psDryContactor2Alarm31,'psDryContactor2Alarm32':psDryContactor2Alarm32,'psDryContact2Status':psDryContact2Status,'psConfNominal':psConfNominal,'psConfEnableCurrentLimit':psConfEnableCurrentLimit,'psConfEnablePeriodicEqualize':psConfEnablePeriodicEqualize,'psConfGHighTempAlarm':psConfGHighTempAlarm,'psConfLowTempAlarmSign':psConfLowTempAlarmSign,'psConfLowTempAlarm':psConfLowTempAlarm,'psConfTemperatureCoefficient':psConfTemperatureCoefficient,'psConfNumOfInvertors':psConfNumOfInvertors,'psConfNumOfRectifiers':psConfNumOfRectifiers,'psConfACHigh':psConfACHigh,'psConfACLow':psConfACLow,'psConfCurrentLimit':psConfCurrentLimit,'psConfHIA':psConfHIA,'psConfBDOC':psConfBDOC,'psConfBatteryNominalCapacity':psConfBatteryNominalCapacity,'psConfEqualStopTime':psConfEqualStopTime,'psConfEqualStopCurrent':psConfEqualStopCurrent,'psConfEqualPeriod':psConfEqualPeriod,'psConfEqualStartCurrent':psConfEqualStartCurrent,'psConfMajorLowVoltage1':psConfMajorLowVoltage1,'psConfMajorLowVoltage':psConfMajorLowVoltage,'psConfMinorLowVoltage':psConfMinorLowVoltage,'psConfMinorHighVoltage':psConfMinorHighVoltage,'psConfMajorHighVoltage':psConfMajorHighVoltage,'psConfFloatingVoltage':psConfFloatingVoltage,'psConfEqualizingVoltage':psConfEqualizingVoltage,'psConfNumberOfBattery':psConfNumberOfBattery,'psConfEnableTempComp':psConfEnableTempComp,'psConfNumberOfLVD':psConfNumberOfLVD,'psConfEqMajorLowVoltageLV1':psConfEqMajorLowVoltageLV1,'psConfEqMajorLowVoltageLv':psConfEqMajorLowVoltageLv,'psConfEqMinorLowVoltageLV':psConfEqMinorLowVoltageLV,'psConfEqMinorHighVoltageHV':psConfEqMinorHighVoltageHV,'psConfEqMajorHighVoltageHV':psConfEqMajorHighVoltageHV,'psConfInvertorVoltage':psConfInvertorVoltage,'psConfInvertorHighVoltage':psConfInvertorHighVoltage,'psConfInvertorLowVoltage':psConfInvertorLowVoltage,'psConfLVDDisconnectTime':psConfLVDDisconnectTime,'psConfNomSpare0':psConfNomSpare0,'psConfNomSpare1':psConfNomSpare1,'psConfNomSpare2':psConfNomSpare2,'psConfNomSpare3':psConfNomSpare3,'psConfNomSpare4':psConfNomSpare4,'psConfNomSpare5':psConfNomSpare5,'psConfNomSpare6':psConfNomSpare6,'psConfNomSpare7':psConfNomSpare7,'psConfNomSpare8':psConfNomSpare8,'psConfNomSpare9':psConfNomSpare9,'psConfNomSpare10':psConfNomSpare10,'psStatus':psStatus,'psStatusAlarm1':psStatusAlarm1,'psStatusAlarm2':psStatusAlarm2,'psStatusAlarm3':psStatusAlarm3,'psStatusAlarm4':psStatusAlarm4,'psStatusAlarm5':psStatusAlarm5,'psStatusAlarm6':psStatusAlarm6,'psStatusAlarm7':psStatusAlarm7,'psStatusAlarm8':psStatusAlarm8,'psStatusAlarm9':psStatusAlarm9,'psStatusAlarm10':psStatusAlarm10,'psStatusAlarm11':psStatusAlarm11,'psStatusAlarm12':psStatusAlarm12,'psStatusAlarm13':psStatusAlarm13,'psStatusAlarm14':psStatusAlarm14,'psStatusAlarm15':psStatusAlarm15,'psStatusAlarm16':psStatusAlarm16,'psStatusAlarm17':psStatusAlarm17,'psStatusAlarm18':psStatusAlarm18,'psStatusAlarm19':psStatusAlarm19,'psStatusAlarm20':psStatusAlarm20,'psStatusAlarm21':psStatusAlarm21,'psStatusAlarm22':psStatusAlarm22,'psStatusAlarm23':psStatusAlarm23,'psStatusAlarm24':psStatusAlarm24,'psStatusAlarm25':psStatusAlarm25,'psStatusAlarm26':psStatusAlarm26,'psStatusAlarm27':psStatusAlarm27,'psStatusAlarm28':psStatusAlarm28,'psStatusAlarm29':psStatusAlarm29,'psStatusAlarm30':psStatusAlarm30,'psStatusAlarm31':psStatusAlarm31,'psStatusAlarm32':psStatusAlarm32,'psStatusAlarm33':psStatusAlarm33,'psStatusAlarm34':psStatusAlarm34,'psStatusAlarm35':psStatusAlarm35,'psStatusAlarm36':psStatusAlarm36,'psStatusAlarm37':psStatusAlarm37,'psStatusAlarm38':psStatusAlarm38,'psStatusAlarm39':psStatusAlarm39,'psStatusAlarm40':psStatusAlarm40,'psStatusAlarm41':psStatusAlarm41,'psStatusAlarm42':psStatusAlarm42,'psStatusAlarm43':psStatusAlarm43,'psStatusAlarm44':psStatusAlarm44,'psStatusAlarm45':psStatusAlarm45,'psStatusAlarm46':psStatusAlarm46,'psStatusAlarm47':psStatusAlarm47,'psStatusAlarm48':psStatusAlarm48,'psStatusAlarm49':psStatusAlarm49,'psStatusAlarm50':psStatusAlarm50,'psStatusAlarm51':psStatusAlarm51,'psStatusAlarm52':psStatusAlarm52,'psStatusAlarm53':psStatusAlarm53,'psStatusAlarm54':psStatusAlarm54,'psStatusAlarm55':psStatusAlarm55,'psStatusAlarm56':psStatusAlarm56,'psStatusAlarm57':psStatusAlarm57,'psStatusAlarm58':psStatusAlarm58,'psStatusAlarm59':psStatusAlarm59,'psStatusAlarm60':psStatusAlarm60,'psStatusAlarm61':psStatusAlarm61,'psStatusAlarm62':psStatusAlarm62,'psStatusAlarm63':psStatusAlarm63,'psStatusAlarm64':psStatusAlarm64,'psStatusAlarm65':psStatusAlarm65,'psStatusAlarm66':psStatusAlarm66,'psStatusAlarm67':psStatusAlarm67,'psStatusAlarm68':psStatusAlarm68,'psStatusAlarm69':psStatusAlarm69,'psStatusAlarm70':psStatusAlarm70,'psStatusAlarm71':psStatusAlarm71,'psStatusAlarm72':psStatusAlarm72,'psStatusAlarm73':psStatusAlarm73,'psStatusAlarm74':psStatusAlarm74,'psStatusAlarm75':psStatusAlarm75,'psStatusAlarm76':psStatusAlarm76,'psStatusAlarm77':psStatusAlarm77,'psStatusAlarm78':psStatusAlarm78,'psStatusAlarm79':psStatusAlarm79,'psStatusAlarm80':psStatusAlarm80,'psStatusAlarm81':psStatusAlarm81,'psStatusAlarm82':psStatusAlarm82,'psStatusAlarm83':psStatusAlarm83,'psStatusAlarm84':psStatusAlarm84,'psStatusAlarm85':psStatusAlarm85,'psStatusAlarm86':psStatusAlarm86,'psStatusAlarm87':psStatusAlarm87,'psStatusAlarm88':psStatusAlarm88,'psStatusAlarm89':psStatusAlarm89,'psStatusAlarm90':psStatusAlarm90,'psStatusAlarm91':psStatusAlarm91,'psStatusAlarm92':psStatusAlarm92,'psStatusAlarm93':psStatusAlarm93,'psStatusAlarm94':psStatusAlarm94,'psStatusAlarm95':psStatusAlarm95,'psStatusAlarm96':psStatusAlarm96,'psStatusAlarmStruct':psStatusAlarmStruct,'psStatusAlarmStruct1':psStatusAlarmStruct1,'psStatusAlarmStruct2':psStatusAlarmStruct2,'psStatistics':psStatistics,'psHourlyTable':psHourlyTable,'psHourlyEntry':psHourlyEntry,_q:psHourlyIndex,'psHourlyMaxVoltage':psHourlyMaxVoltage,'psHourlyMinVoltage':psHourlyMinVoltage,'psHourlyAvrVoltage':psHourlyAvrVoltage,'psHourlyMinCurrent':psHourlyMinCurrent,'psHourlyMaxCurrent':psHourlyMaxCurrent,'psHourlyAvrCurrent':psHourlyAvrCurrent,'psHourlyEndTime':psHourlyEndTime,'psDailyTable':psDailyTable,'psDailyEntry':psDailyEntry,_r:psDailyIndex,'psDailyMaxVoltage':psDailyMaxVoltage,'psDailyMinVoltage':psDailyMinVoltage,'psDailyAvrVoltage':psDailyAvrVoltage,'psDailyMinCurrent':psDailyMinCurrent,'psDailyMaxCurrent':psDailyMaxCurrent,'psDailyAvrCurrent':psDailyAvrCurrent,'psDailyDayOfMonth':psDailyDayOfMonth,'psMonthlyTable':psMonthlyTable,'psMonthlyEntry':psMonthlyEntry,_s:psMonthlyIndex,'psMonthlyMaxVoltage':psMonthlyMaxVoltage,'psMonthlyMinVoltage':psMonthlyMinVoltage,'psMonthlyAvrVoltage':psMonthlyAvrVoltage,'psMonthlyMinCurrent':psMonthlyMinCurrent,'psMonthlyMaxCurrent':psMonthlyMaxCurrent,'psMonthlyAvrCurrent':psMonthlyAvrCurrent,'psMonthlyMonth':psMonthlyMonth,'psHourlyFirst':psHourlyFirst,'psHourlyLast':psHourlyLast,'psDailyFirst':psDailyFirst,'psDailyLast':psDailyLast,'psMonthlyFirst':psMonthlyFirst,'psMonthlyLast':psMonthlyLast,'psLog':psLog,'psLogTable':psLogTable,'psLogEntry':psLogEntry,_t:psLogIndex,'psLogDateYear':psLogDateYear,'psLogDateMonth':psLogDateMonth,'psLogDateDay':psLogDateDay,'psLogDateHour':psLogDateHour,'psLogDateMinute':psLogDateMinute,'psLogDateSecond':psLogDateSecond,'psLogDCVoltage':psLogDCVoltage,'psLogStatus':psLogStatus,'psLogAlarmCode':psLogAlarmCode,'psLogDateTime':psLogDateTime,'psLogGeneral':psLogGeneral,'psLogFirst':psLogFirst,'psLogLast':psLogLast,'psTrap':psTrap,_R:psTrapSeverity,_O:psTrapStatus,'psTrapActivation':psTrapActivation,'psAlarm1006':psAlarm1006,'psTrapPrefix1006':psTrapPrefix1006,'psTrap1006ACLow':psTrap1006ACLow,'psTrap1006Battery2TestFault':psTrap1006Battery2TestFault,'psTrap1006Battery1TestFault':psTrap1006Battery1TestFault,'psTrap1006LVD2Open':psTrap1006LVD2Open,'psTrap1006LVD1Open':psTrap1006LVD1Open,'psTrap1006AUXContactOpen':psTrap1006AUXContactOpen,'psTrap1006AUXBreakerOpen':psTrap1006AUXBreakerOpen,'psTrap1006BatteryBreakerOpen':psTrap1006BatteryBreakerOpen,'psTrap1006LoadBreakerOpen':psTrap1006LoadBreakerOpen,'psTrap1006DCLOWLow':psTrap1006DCLOWLow,'psTrap1006Rectifier':psTrap1006Rectifier,'psTrap1006OverTemptature':psTrap1006OverTemptature,'psTrap1006LVDBypassOpen':psTrap1006LVDBypassOpen,'psTrap1006DCHigh':psTrap1006DCHigh,'psTrap1006DCLow':psTrap1006DCLow,'psTrap1006ACHigh':psTrap1006ACHigh,'psAlarm':psAlarm,'psTrapPrefix':psTrapPrefix,'psTrapRFAMAJ':psTrapRFAMAJ,'psTrapRFAMIN':psTrapRFAMIN,'psTrapACFAIL':psTrapACFAIL,'psTrapLVDX2':psTrapLVDX2,'psTrapSYSOT':psTrapSYSOT,'psTrapLVDX1':psTrapLVDX1,'psTrapCBOPEN':psTrapCBOPEN,'psTrapEQHST':psTrapEQHST,'psTrapBATTST':psTrapBATTST,'psTrapINUBAD':psTrapINUBAD,'psTrapUNIVPD':psTrapUNIVPD,'psTrapIBADIN':psTrapIBADIN,'psTrapRBADIN':psTrapRBADIN,'psTrapSLFTST':psTrapSLFTST,'psTrapFUSEBD':psTrapFUSEBD,'psTrapLOADHI':psTrapLOADHI,'psTrapSURGBD':psTrapSURGBD,'psTrapEQLONG':psTrapEQLONG,'psTrapFUSE24':psTrapFUSE24,'psTrapFUSE48':psTrapFUSE48,'psTrapBYPS2':psTrapBYPS2,'psTrapBYPS1':psTrapBYPS1,'psTrapCB24CR':psTrapCB24CR,'psTrapCB48CR':psTrapCB48CR,'psTrapBATOT':psTrapBATOT,'psAlarmSet':psAlarmSet,'psAlarmSet1':psAlarmSet1,'psAlarmSet2':psAlarmSet2,'psAlarmSet3':psAlarmSet3,'psAlarmSet4':psAlarmSet4,'psAlarmSet5':psAlarmSet5,'psAlarmSet6':psAlarmSet6,'psAlarmSet7':psAlarmSet7,'psAlarmSet8':psAlarmSet8,'psAlarmSet9':psAlarmSet9,'psAlarmSet10':psAlarmSet10,'psAlarmSet11':psAlarmSet11,'psAlarmSet12':psAlarmSet12,'psAlarmSet13':psAlarmSet13,'psAlarmSet14':psAlarmSet14,'psAlarmSet15':psAlarmSet15,'psAlarmSet16':psAlarmSet16,'psAlarmSet17':psAlarmSet17,'psAlarmSet18':psAlarmSet18,'psAlarmSet19':psAlarmSet19,'psAlarmSet20':psAlarmSet20,'psAlarmSet21':psAlarmSet21,'psAlarmSet22':psAlarmSet22,'psAlarmSet23':psAlarmSet23,'psAlarmSet24':psAlarmSet24,'psAlarmSet25':psAlarmSet25,'psAlarmSet26':psAlarmSet26,'psAlarmSet27':psAlarmSet27,'psAlarmSet28':psAlarmSet28,'psAlarmSet29':psAlarmSet29,'psAlarmSet30':psAlarmSet30,'psAlarmSet31':psAlarmSet31,'psAlarmSet32':psAlarmSet32,'psAlarmSet33':psAlarmSet33,'psAlarmSet34':psAlarmSet34,'psAlarmSet35':psAlarmSet35,'psAlarmSet36':psAlarmSet36,'psAlarmSet37':psAlarmSet37,'psAlarmSet38':psAlarmSet38,'psAlarmSet39':psAlarmSet39,'psAlarmSet40':psAlarmSet40,'psAlarmSet41':psAlarmSet41,'psAlarmSet42':psAlarmSet42,'psAlarmSet43':psAlarmSet43,'psAlarmSet44':psAlarmSet44,'psAlarmSet45':psAlarmSet45,'psAlarmSet46':psAlarmSet46,'psAlarmSet47':psAlarmSet47,'psAlarmSet48':psAlarmSet48,'psAlarmSet49':psAlarmSet49,'psAlarmSet50':psAlarmSet50,'psAlarmSet51':psAlarmSet51,'psAlarmSet52':psAlarmSet52,'psAlarmSet53':psAlarmSet53,'psAlarmSet54':psAlarmSet54,'psAlarmSet55':psAlarmSet55,'psAlarmSet56':psAlarmSet56,'psAlarmSet57':psAlarmSet57,'psAlarmSet58':psAlarmSet58,'psAlarmSet59':psAlarmSet59,'psAlarmSet60':psAlarmSet60,'psAlarmSet61':psAlarmSet61,'psAlarmSet62':psAlarmSet62,'psAlarmSet63':psAlarmSet63,'psAlarmSet64':psAlarmSet64,'psAlarmSet65':psAlarmSet65,'psAlarmSet66':psAlarmSet66,'psAlarmSet67':psAlarmSet67,'psAlarmSet68':psAlarmSet68,'psAlarmSet69':psAlarmSet69,'psAlarmSet70':psAlarmSet70,'psAlarmSet71':psAlarmSet71,'psAlarmSet72':psAlarmSet72,'psAlarmSet73':psAlarmSet73,'psAlarmSet74':psAlarmSet74,'psAlarmSet75':psAlarmSet75,'psAlarmSet76':psAlarmSet76,'psAlarmSet77':psAlarmSet77,'psAlarmSet78':psAlarmSet78,'psAlarmSet79':psAlarmSet79,'psAlarmSet80':psAlarmSet80,'psAlarmSet81':psAlarmSet81,'psAlarmSet82':psAlarmSet82,'psAlarmSet83':psAlarmSet83,'psAlarmSet84':psAlarmSet84,'psAlarmSet85':psAlarmSet85,'psAlarmSet86':psAlarmSet86,'psAlarmSet87':psAlarmSet87,'psAlarmSet88':psAlarmSet88,'psAlarmSet89':psAlarmSet89,'psAlarmSet90':psAlarmSet90,'psAlarmSet91':psAlarmSet91,'psAlarmSet92':psAlarmSet92,'psAlarmSet93':psAlarmSet93,'psAlarmSet94':psAlarmSet94,'psAlarmSet95':psAlarmSet95,'psAlarmSet96':psAlarmSet96,'psSecurity':psSecurity,'psSecurityComunity1':psSecurityComunity1,'psSecurityComunity2':psSecurityComunity2,'psSecurityComunity3':psSecurityComunity3,'psSecurityPasswordComunity':psSecurityPasswordComunity,'psSecurityPasswordSet':psSecurityPasswordSet,'psSecuritySetGetPassword':psSecuritySetGetPassword,'psSecurityErasePassword':psSecurityErasePassword,'psSecurityTrapIp1':psSecurityTrapIp1,'psSecurityTrapIp2':psSecurityTrapIp2,'psSecurityTrapIp3':psSecurityTrapIp3,'psSecurityTrapIp4':psSecurityTrapIp4,'psSecurityInterfaceIP':psSecurityInterfaceIP,'psSecurityInterfaceNetMask':psSecurityInterfaceNetMask,'psSecurityInterfaceGateWay':psSecurityInterfaceGateWay,'psSecurityInterfaceActivate':psSecurityInterfaceActivate,'psCommand':psCommand,'psCommandGoFloat':psCommandGoFloat,'psCommandGoEqualizing':psCommandGoEqualizing,'psCommandDoSelfTest':psCommandDoSelfTest,'psCommandRunFlash1':psCommandRunFlash1,'psCommandRunFlash2':psCommandRunFlash2,'psCommandTestBatteryAll':psCommandTestBatteryAll,'psCommandDoBoot':psCommandDoBoot,'psCommandLoadDefault':psCommandLoadDefault,'psCommandProgramNonActiveFlash':psCommandProgramNonActiveFlash,'psCommandNonActiveFlash':psCommandNonActiveFlash,'psCommandNonActiveStatus':psCommandNonActiveStatus,'psCommandDownLoadSoftware':psCommandDownLoadSoftware,'psCommandDownLoadCheck':psCommandDownLoadCheck,'psCommandFileName':psCommandFileName,'psCommandIpAddress':psCommandIpAddress,'psCommandAbortBatTest':psCommandAbortBatTest,'psCommandEraseTotalTime':psCommandEraseTotalTime,'psCommandAbortProgramFlash':psCommandAbortProgramFlash,'psCommandUserDefine2':psCommandUserDefine2,'psCommandUserDefine3':psCommandUserDefine3,'psCommandUserDefine4':psCommandUserDefine4,'psCommandUserDefine5':psCommandUserDefine5,'psCommandFlash1Protect':psCommandFlash1Protect,'psCommandFlash2Protect':psCommandFlash2Protect,'psCommandFlashFix':psCommandFlashFix,'psCommandFlashFixNumber':psCommandFlashFixNumber,'psCommandRemoteTest':psCommandRemoteTest,'psCommandControlerStatus':psCommandControlerStatus,'psCommandFirmwareRev':psCommandFirmwareRev,'psCommandFlash2SWRev':psCommandFlash2SWRev,'psCommandFlash1SWRev':psCommandFlash1SWRev,'psCommandMBXSWRev':psCommandMBXSWRev,'psCommandLeds':psCommandLeds,'psCommandProgramingInProcess':psCommandProgramingInProcess,'psCommandLoadUserDefaults':psCommandLoadUserDefaults,'psCommandStoreUserDefaults':psCommandStoreUserDefaults,'psCommandLoadUserParameters':psCommandLoadUserParameters,'psCommandStoreUserParameters':psCommandStoreUserParameters,'psCommandDryInStatus':psCommandDryInStatus,'psCommandSpareR0':psCommandSpareR0,'psCommandSpareR1':psCommandSpareR1,'psCommandSpareR2':psCommandSpareR2,'psCommandSpareR3':psCommandSpareR3,'psCommandSpareR4':psCommandSpareR4,'psCommandSpareR5':psCommandSpareR5,'psCommandSpareR6':psCommandSpareR6,'psCommandSpareR7':psCommandSpareR7,'psCommandSpareR8':psCommandSpareR8,'psCommandSpareR9':psCommandSpareR9,'psCommandSpareR10':psCommandSpareR10,'psCommandSpareW0':psCommandSpareW0,'psCommandSpareW1':psCommandSpareW1,'psCommandSpareW2':psCommandSpareW2,'psCommandSpareW3':psCommandSpareW3,'psCommandSpareW4':psCommandSpareW4,'psCommandSpareW5':psCommandSpareW5,'psCommandSpareW6':psCommandSpareW6,'psCommandSpareW7':psCommandSpareW7,'psCommandSpareW8':psCommandSpareW8,'psCommandSpareW9':psCommandSpareW9,'psCommandSpareW10':psCommandSpareW10,'psCommandSpareW11':psCommandSpareW11,'psCommandSpareW12':psCommandSpareW12,'psSeverityMap':psSeverityMap,'psSeverityMapTable':psSeverityMapTable,'psSeverityMapEntry':psSeverityMapEntry,_w:psSeverityMapIndex,'psSeverityMapAlarm1to32':psSeverityMapAlarm1to32,'psSeverityMapAlarm33to64':psSeverityMapAlarm33to64,'psSeverityMapAlarm65to96':psSeverityMapAlarm65to96,'psSpare':psSpare,'psSpare1':psSpare1,'psSpare2':psSpare2,'psSpare3':psSpare3,'psSpare4':psSpare4,'psSpare5':psSpare5,'psSpare6':psSpare6,'psSpare7':psSpare7,'psSpare8':psSpare8,'psSpare9':psSpare9,'psSpare10':psSpare10,'psSpare11':psSpare11,'psSpare12':psSpare12,'psSpare13':psSpare13,'psSpare14':psSpare14,'psSpare15':psSpare15,'psSpare16':psSpare16,'psSpare17':psSpare17,'psSpare18':psSpare18,'psSpare19':psSpare19,'psSpare20':psSpare20,'psSpare21':psSpare21,'psSpare22':psSpare22,'psSpare23':psSpare23,'psSpare24':psSpare24,'psSpare25':psSpare25,'psSpare26':psSpare26,'psSpare27':psSpare27,'psSpare28':psSpare28,'psSpare29':psSpare29,'psSpare30':psSpare30,'psSpare31':psSpare31,'psSpare32':psSpare32,'psDial':psDial,'psDialATDModemSetUp':psDialATDModemSetUp,'psDialATDDialOut':psDialATDDialOut,'psDialOutFlag':psDialOutFlag,'psDialOutNumRetries':psDialOutNumRetries,'psDialOutNumRetriesActual':psDialOutNumRetriesActual,'psDialTimeOutBetweenRetries':psDialTimeOutBetweenRetries,'psDialTimeOutAfterLastSuccess':psDialTimeOutAfterLastSuccess,'psDialTimeOutAfterLastRetryFailed':psDialTimeOutAfterLastRetryFailed,'psPowerPlus':psPowerPlus,'psPowerPlus1':psPowerPlus1,'psPowerPlus2':psPowerPlus2,'psPowerPlus3':psPowerPlus3,'psPowerPlus4':psPowerPlus4,'psPowerPlus5':psPowerPlus5,'psPowerPlus6':psPowerPlus6,'psPowerPlus7':psPowerPlus7,'psPowerPlus8':psPowerPlus8,'psPowerPlus9':psPowerPlus9,'psPowerPlus10':psPowerPlus10,'psPowerPlus11':psPowerPlus11,'psPowerPlus12':psPowerPlus12,'psPowerPlus13':psPowerPlus13,'psPowerPlus14':psPowerPlus14,'psPowerPlus15':psPowerPlus15})